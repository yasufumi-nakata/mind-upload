---
layout: default
title: "Wiki: Data partitioning and data leaks"
description: "We will explain how to divide train/test, subject division, time division, and patient/session/report leakage from the beginning."
article_type: Wiki
subtitle: "Even if the accuracy is high, the evaluation will be corrupted if the classification is lax"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Practical guide"
audience: "People who create initial evaluations using public data, people who are easily confused by leaks and splits"
reading_time: "10-15 minutes"
page_intro: "This page is a wiki that explains from the beginning how to divide datasets and why data leaks are dangerous. In order to reduce accidents where data is highly accurate but cannot be trusted, we will at least organize where to look."
accuracy_note: "These are basic principles. The best partitioning method depends on the problem and the structure of the data, so there is no one-size-fits-all rule."
page_highlights:
  - "Difficulty varies greatly depending on whether the unit is divided into subjects, sessions, or time."
  - "Leaks occur not only due to 'cheating' but also due to well-intentioned pre-processing and splitting."
  - "Even across four starter datasets, the independent unit differs: subject, case, night, or session."
  - "The first thing you should look at is the division rules and leak countermeasures rather than the accuracy itself."
known_points:
  - "Accuracy can easily be overestimated if the train/test separation is loose."
  - "Apparent performance tends to improve when fragments from the same subject, same session, and near time are included on both sides."
  - "In clinical EEG, report text and report-derived labels can also be leakage sources."
  - "Preprocessing, normalization, and feature selection can also be a source of leaks if they are performed after looking at all the data."
unknown_points:
  - "Which division is closest to future actual operation depends on the task setting and usage situation."
  - "A deep understanding and auditing of data structures is required to be able to claim that leaks have been completely eliminated."
  - "How to standardize report-derived labels from signal-only benchmarks is still in the process of operational design."
wiki_links:
  - label: "Wiki: EEG pretreatment and QC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "Compensates for where the preprocessing itself changes the result."
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "See why leak prevention is 'part of operations'."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "You can return to the overall map of the learning page."
recommended_pages:
  - label: "Data & Bench"
    url: "/datasets.html"
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
  - label: "Verification base"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest explanation</h2>
<p>
Data division is the process of ``determining how far you can look before comparing the answers.'' A data leak is when that boundary is inadvertently crossed and information that cannot be used in production is mixed into learning and adjustment.
</p>
</div>

<section class="section" id="why-split-matters">
<h2 class="section-title">Why partitioning matters so much</h2>
<p>
On school tests, if you practice the questions while looking at the answers, you will get a higher score. However, that score cannot be said to indicate the ability to solve truly new problems. The same goes for machine learning, if the information seen during learning bleeds into the test side, only the numbers will look good.
</p>
</section>

<section class="section" id="split-units">
<h2 class="section-title">First, be aware of the unit of division</h2>
<table class="data-table">
<thead>
<tr>
<th>Unit of division</th>
<th>What kind of scene is it?</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Subject unit</strong></td>
<td>When you want to see if you can generalize to new people. </td>
<td>It's easier than it looks when you have pieces of the same person in both train and test. </td>
</tr>
<tr>
<td><strong>Per session</strong></td>
<td>When you want to see if the same person will be stable on different days. </td>
<td>If you divide only by recording on the same day, you will overlook differences in daily differences and electrode conditions. </td>
</tr>
<tr>
<td><strong>Time unit</strong></td>
<td>When envisioning future predictions or continuous operation. </td>
<td>If you enter windows with similar times on both sides, you may see almost the same fragment. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dataset-specific-units">
<h2 class="section-title">4 starter data items, independent units are not the same</h2>
<div class="note-box">
<strong>The last two columns are the operational reasoning for this site</strong>
<p>
<strong>Why leaks</strong> and <strong>Safe classification</strong> in the table below are operational rules drawn by this site based on the official explanation of each dataset and the hierarchical structure shown in primary documents.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Dataset</th>
<th>What should be prioritized as an independent unit</th>
<th>Common misdivision</th>
<th>Why does it leak</th>
<th>How to divide on the safe side</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>subject, run if necessary</td>
<td>Random split of epoch / trial</td>
<td>Signal characteristics and cue structures of the same subject and session span train / test. </td>
<td>First of all, separate the subject unit and the run unit even if the evaluation is within the same subject. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>subject and case chronology</td>
<td>Random division by file</td>
<td><code>chb21</code> is the same subject as <code>chb01</code>, and the gap between files also has a context. </td>
<td>Check for subject correspondence instead of case, and split while preserving sequential order and gap. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>subject-night</td>
<td>Random split of epoch</td>
<td>Sequential hypnograms and subject-specific sleep structures from the same night span train / test. </td>
<td>Keep each night and declare first whether it is generalization across subjects or within-subject. </td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>patient / session</td>
<td>Random division of segment / file, signal-only evaluation with report included</td>
<td>This is because multiple sessions and de-identified reports of the same patient have information close to the label. </td>
<td>Require per patient/session split and <strong>report usage flag</strong>. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-leaks">
<h2 class="section-title">5 common leak patterns</h2>
<table class="data-table">
<thead>
<tr>
<th>Common accidents</th>
<th>What's happening</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fragments of the same subject enter on both sides</strong></td>
<td>The individual's unique habits are memorized, and the generalization performance to new people appears to be higher. </td>
</tr>
<tr>
<td><strong>Mix adjacent time windows</strong></td>
<td>Separating almost the same waveform slices into train/test, it underestimates the difficulty of predicting the future. </td>
</tr>
<tr>
<td><strong>Normalize and select features on all data</strong></td>
<td>The statistics on the test side are used during training, and the information flows backwards. </td>
</tr>
<tr>
<td><strong>Repeat model selection with test</strong></td>
<td>test essentially takes on the role of validation, and the final score is optimistic. </td>
</tr>
<tr>
<td><strong>Miss duplicate or derived samples</strong></td>
<td>Data originally cut from the same record is included on both sides, resulting in a comparison that is not an independent sample. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dataset-specific-traps">
<h2 class="section-title">Leak warning specific to the dataset added this time</h2>
<table class="data-table">
<thead>
<tr>
<th>dataset</th>
<th>Notes to be fixed this time</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>Since it is a cue-locked motor task, even if the split is made stricter, the visual cue/eyeball/myoelectric contributions will still be audited separately. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>Do not confuse subject numbers with case numbers. Don't shuffle files and pin gap and chronology to runbook. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>Do not silently mix R&K hypnogram as equivalent to AASM. No cross-dataset comparison without writing label mapping. </td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>Do not mix report text, triage and session metadata derived from report keyword into input of signal-only benchmark. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-to-report">
<h2 class="section-title">At least I would like to report this</h2>
<div class="key-points">
<h4>Report Items</h4>
<ul>
<li><strong>Divided by:</strong>Whether by subject, session, or time. </li>
<li><strong>Split rule:</strong>How many items were placed in train/validation/test? </li>
<li><strong>Independent ID: Which of the subject / case / night / session is considered an independent unit. </li>
<li><strong>Report usage: signal-only or multimodal evaluation with report/metadata? </li>
<li><strong>label manual: If there is a manual scoring or mapping rule, the standard. </li>
<li><strong>Preprocessing boundaries:</strong> Did you fit normalization and feature selection using only train? </li>
<li><strong>Baseline:</strong>What is the improvement compared to the simpler method? </li>
<li><strong>Failure example:</strong>Under what conditions did it fail and what was the reason for its exclusion? </li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ul>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), The Temple University Hospital EEG Data Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), The Temple University Hospital Seizure Detection Corpus</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009), Sleep classification according to AASM and Rechtschaffen &amp; Kales</a></li>
</ul>
</section>

<section class="section" id="beginner-rule">
<h2 class="section-title">Safety measures if you get lost in the first book</h2>
<p>
When in doubt, it is safe to follow these three points: <strong>Separate train/test for each subject</strong> <strong>Do not touch test until the end</strong><strong>For normalization and feature selection, fit only with train</strong>. Even if it seems too harsh, reliable accuracy is more valuable than fancy numbers.
</p>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
Go back to <a href="../datasets.html">Data & Bench</a> if you want to review the actual starter data, <a href="../datasets.html#l0-practice">Hands-on</a> if you want to go back to creating minimal loops, or go back to <a href="../verification.html">Verification Foundation</a> if you want to see why this is part of the verification foundation.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-preprocessing-and-qc.html">EEG preprocessing and QC →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../datasets.html">Data & Bench →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
</aside>
</main>
