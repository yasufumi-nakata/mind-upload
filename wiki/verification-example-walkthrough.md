---
layout: default
title: "Wiki: Verification example walkthrough"
description: "A worked EEG example showing how a small benchmark now needs not only data standard, benchmark, registry, and model card, but also an event contract, shortcut audit, temporal-validity note, and calibration / abstention note."
article_type: Wiki
subtitle: "Read the blueprint through one small EEG example without overreading timing, identity, or stability"
author: Mind Uploading Research Project
last_updated: "2026-03-28"
note: "Worked example / technical refresh"
audience: "People who find Verification too abstract, and people who want one concrete EEG example that already respects the site's newer stop lines"
reading_time: "12-18 minutes"
page_intro: "This page turns the Verification Commons into one small EEG example. The goal is still not to chase a large score. The goal is to show what has to be frozen before a small public EEG result can be read honestly: input contract, benchmark object, split regime, shortcut audit, temporal scope, calibration logic, and stopped claim."
accuracy_note: "This is a bounded L0/L1 tutorial. It does not support causal, source-identification, or WBE-level claims by itself. It shows how to build one small EEG result without silently overreading timing, subject identity, or temporal stability."
page_highlights:
  - "This worked example is no longer just data standard + benchmark + registry + model card; it now also carries an event contract, a shortcut audit, a temporal-validity note, and a calibration / abstention note."
  - "BIDS events, HED semantics, and LSL synchronization answer different questions and should not be compressed into one checkbox."
  - "A subject/session split is not enough if raw-recording ancestry, identity confounding, or acquisition-distribution shortcuts remain unresolved."
  - "Same-session success is not cross-day durability; fixed decoder interval and recalibration burden stay explicit."
  - "The safe ceiling of this example is a bounded reproducible EEG decode under a named observation contract, not a stable biomarker or hidden-state readout."
known_points:
  - "A small public EEG example can already teach most of the core verification logic if input contract, benchmark object, and stopped claim are frozen explicitly."
  - "Event timing, event meaning, split hygiene, shortcut resistance, and temporal scope are separate technical questions."
  - "High score alone is not enough; the site now asks where predictive information came from and how far the result can be extrapolated across time."
  - "If probabilities, thresholds, or prediction sets are reported, fit / calibration / test separation and abstention policy belong in the worked example."
unknown_points:
  - "This page still does not define one site-wide default calibration threshold or one universal temporal benchmark for every EEG task."
  - "Which backbone object should become the default target for future longitudinal EEG examples remains unsettled."
  - "This example does not decide which additional cards would be sufficient for stronger L2/L3 claims."
wiki_links:
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Start here if you want the role of each artifact before the example."
  - label: "Wiki: Event synchronization and observation logs"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Use this when the example reaches event timing, semantics, or clock-domain questions."
  - label: "Wiki: Data splits and leakage"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "Use this when split naming alone is not enough."
  - label: "Wiki: State, trait, and drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Use this when the example starts to imply cross-session or cross-day scope."
  - label: "Wiki: Uncertainty, calibration, and abstention"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "Use this when the example reports probabilities, thresholds, or reject options."
recommended_pages:
  - label: "Verification"
    url: "/verification.html"
  - label: "Wiki: Minimum artifact pack for L0"
    url: "/wiki/l0-minimum-artifact-pack.html"
  - label: "Datasets"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>This worked example in one sentence</h2>
<p>
We use one small public EEG classification task to show what a result has to freeze before the score means anything: <strong>what entered the file</strong>, <strong>what the benchmark object actually is</strong>, <strong>what train/test independence really means</strong>, <strong>which shortcut routes remain open</strong>, <strong>what time scope is being claimed</strong>, and <strong>where the claim must stop</strong>.
</p>
</div>

<div class="note-box">
<strong>Why this tutorial needed a 2026-03-28 repair</strong>
<p>
The older walkthrough was useful as a first orientation, but it still taught a weaker recipe than the current site allows. It could leave readers with the impression that <strong>BIDS + split + score + model card</strong> was already most of the work. The current literature and the rest of this site no longer support that shortcut. BIDS events, HED semantics, and LSL synchronization answer different questions; record-wise or weakly grouped splits can still learn identity; same-day success is not cross-day durability; and a score with no calibration or abstention rule is still not operationally interpretable.
</p>
</div>

<div class="note-box">
<strong>Safe reading of this example</strong>
<p>
If this example is filled well, the strongest safe outcome is a <strong>bounded reproducible EEG decode under a named observation contract</strong>. It still does <strong>not</strong> become source ground truth, a target-specific biomarker by default, a causal intervention result, or a WBE-relevant hidden-state readout.
</p>
</div>

<section class="section" id="scaffold">
<h2 class="section-title">The core scaffold is still four artifacts</h2>
<table class="data-table">
<thead>
<tr>
<th>Core artifact</th>
<th>What it does in this example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data standard</strong></td>
<td>Fixes the dataset snapshot, BIDS shape, event files, channel metadata, and QC context.</td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Fixes the task, target, split family, hold-out unit, metric bundle, and stopped claim.</td>
</tr>
<tr>
<td><strong>Registry</strong></td>
<td>Fixes preprocessing, split freeze, baselines, nuisance checks, and success/failure conditions before the result is known.</td>
</tr>
<tr>
<td><strong>Model card / audit log</strong></td>
<td>Records scores, failures, shortcut checks, calibration behavior, abstention behavior, and what still remains unresolved.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="companion-cards">
<h2 class="section-title">But the current tutorial also stacks companion cards</h2>
<table class="data-table">
<thead>
<tr>
<th>Companion card or note</th>
<th>Why this example now needs it</th>
<th>What goes wrong if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observation contract</strong></td>
<td>Separates event anchor, event semantics, clock domain, timing-validation class, and label provenance.</td>
<td><code>events.tsv</code>, HED, trigger lines, and synchronized streams are too easily read as one solved timing object.</td>
</tr>
<tr>
<td><strong>Observability Budget</strong></td>
<td>Fixes what EEG directly observed: scalp potentials under a named setup, not sources or hidden state by default.</td>
<td>A small scalp-level classifier is too easily promoted to internal-state evidence.</td>
</tr>
<tr>
<td><strong>Specificity &amp; Shortcut note</strong></td>
<td>Fixes which routes could still explain the score: subject fingerprint, setup distribution, residual movement, or other nuisance paths.</td>
<td>A clean split can still be mistaken for target-specific neural evidence.</td>
</tr>
<tr>
<td><strong>Temporal-validity note</strong></td>
<td>Fixes whether the example is within-session, same-day, cross-session, or cross-day, and whether the decoder was fixed or updated.</td>
<td>Same-session success is silently promoted to durability.</td>
</tr>
<tr>
<td><strong>Calibration &amp; Abstention note</strong></td>
<td>Fixes how probabilities or prediction sets were calibrated, and when the model should abstain instead of forcing output.</td>
<td>Thresholds, confidence, and coverage become uninterpretable.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="step1">
<h2 class="section-title">Step 1: Fix the input and the event contract</h2>
<p>
The first thing this example now freezes is not only <strong>which EEG file</strong> you used, but also <strong>what the time and label columns are allowed to mean</strong>. The current standards and timing literature require a narrower reading here. In BIDS, <code>onset</code> is measured from the <strong>first stored data point</strong>, not from physical screen or speaker onset. HED makes event semantics machine-readable. LSL can synchronize streams across a LAN and compensate offset and jitter, but it does not automatically measure device-side delay truth. Therefore, this site now asks the tutorial to log those pieces separately.
</p>
<table class="data-table">
<thead>
<tr>
<th>Input-side item</th>
<th>What to freeze in this example</th>
<th>Why it matters</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>dataset identity</strong></td>
<td>Snapshot or release, DOI or persistent URL, retrieval date, and license.</td>
<td>The same dataset name can still refer to different content over time.</td>
</tr>
<tr>
<td><strong>BIDS skeleton</strong></td>
<td><code>dataset_description.json</code>, participant/session/run layout, <code>*_eeg.json</code>, channel metadata, and electrode metadata when positions exist.</td>
<td>Without this, later readers cannot reconstruct the same measurement condition.</td>
</tr>
<tr>
<td><strong>event anchor</strong></td>
<td><code>events.tsv</code>, <code>events.json</code>, onset/duration/sample meaning, and any discarded-sample rule.</td>
<td>The epoch boundary can look precise while still referring only to stored-file time.</td>
</tr>
<tr>
<td><strong>event semantics</strong></td>
<td><code>trial_type</code>, HED tags when available, condition naming, and any manual scoring rule.</td>
<td>Two datasets can share a label name while meaning different things.</td>
</tr>
<tr>
<td><strong>clock domain + timing-validation class</strong></td>
<td>Whether the example has only a stored-data anchor, stream alignment, digital marker capture, or actual physical timing validation.</td>
<td>The site no longer lets BIDS, HED, LSL, TTL, and photodiode traces collapse into one timing claim.</td>
</tr>
<tr>
<td><strong>label provenance</strong></td>
<td>Whether the target label comes from cue markers, manual scoring, a report-derived rule, or another derived path.</td>
<td>A signal-only benchmark and a report-assisted benchmark are not the same evidence object.</td>
</tr>
<tr>
<td><strong>QC / exclusions</strong></td>
<td>Bad channels, bad segments, missing runs, and thresholds used to exclude data.</td>
<td>The score becomes impossible to audit if exclusions stay implicit.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Safe tutorial rule</strong>
<p>
For this worked example, writing only “the data are in BIDS” is no longer enough. The minimum safe wording is: <strong>which event anchor exists</strong>, <strong>which semantics exist</strong>, <strong>which timing-validation rung was actually tested</strong>, and <strong>where the label came from</strong>.
</p>
</div>
</section>

<section class="section" id="step2">
<h2 class="section-title">Step 2: Fix the benchmark object and the independence unit</h2>
<p>
The next weak point in older beginner workflows was to treat a split rule as if it already solved shortcut risk. The current literature does not support that shortcut. Record-wise splits can learn identity rather than the target variable, resting-state EEG can support time-robust person identification, and cross-dataset EEG performance can move with setup differences such as amplifier, cap, sampling rate, or filtering. This example therefore freezes not only <strong>the split</strong>, but also <strong>the independent hold-out unit</strong> and <strong>the shortcut families that remain plausible</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Benchmark field</th>
<th>What to write in this example</th>
<th>What not to overread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>target</strong></td>
<td>One bounded task such as two-state or few-class EEG classification.</td>
<td>Do not let a small task silently stand in for a general biomarker or latent-state decoder.</td>
</tr>
<tr>
<td><strong>evaluation family</strong></td>
<td>Within-session, cross-session, cross-subject, cross-dataset, or adaptation regime.</td>
<td>The same accuracy means different things in different families.</td>
</tr>
<tr>
<td><strong>independent hold-out unit</strong></td>
<td>Subject, session, or raw recording, not only windows or epochs.</td>
<td>A result can stay identity-confounded even when train/test windows are disjoint.</td>
</tr>
<tr>
<td><strong>raw-recording ancestry</strong></td>
<td>Whether windows cut from one raw recording ever cross train/test.</td>
<td>Window-level separation is not enough if the raw ancestor is shared.</td>
</tr>
<tr>
<td><strong>setup disjointness</strong></td>
<td>Participant, session, site, device, reference system, channel map, and protocol differences.</td>
<td>A classifier can still read acquisition-distribution structure rather than the intended signal.</td>
</tr>
<tr>
<td><strong>shortcut-aware baselines</strong></td>
<td>Metadata-only, subject-ID, or other nuisance-aware baselines when relevant.</td>
<td>Without them, the score can still be explained by who, when, or how the EEG was recorded.</td>
</tr>
<tr>
<td><strong>temporal scope</strong></td>
<td>Whether the example is same-session only or claims any reuse across time.</td>
<td>Do not promote a same-session result to cross-day durability after the fact.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="step3">
<h2 class="section-title">Step 3: Write the registry before training</h2>
<p>
The registry is where this example stops becoming a flexible demo and becomes an auditable result. The main point is not fancy formatting. The main point is that preprocessing, splits, baselines, and stopping conditions are fixed before the score appears. If the example will later report probabilities, prediction sets, or an abstain threshold, this is also where the <strong>fit / calibration / test</strong> separation must be frozen.
</p>
<table class="data-table">
<thead>
<tr>
<th>Registry field</th>
<th>What to freeze here</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>preprocessing recipe</strong></td>
<td>Filtering, referencing, artifact handling, rejected channels/segments, and derivative boundaries.</td>
</tr>
<tr>
<td><strong>split freeze</strong></td>
<td>The exact grouping rule for subjects, sessions, and raw recordings, plus any benchmark version.</td>
</tr>
<tr>
<td><strong>baseline plan</strong></td>
<td>Simple baseline, shortcut-aware baseline, and what counts as improvement over them.</td>
</tr>
<tr>
<td><strong>failure conditions</strong></td>
<td>What will count as collapse: low sensitivity, shortcut-only win, unstable calibration, or cross-session failure.</td>
</tr>
<tr>
<td><strong>calibration split</strong></td>
<td>Whether the model reports only hard labels or also probabilities / prediction sets, and which held-out slice is reserved for threshold or temperature tuning.</td>
</tr>
<tr>
<td><strong>stopped claim</strong></td>
<td>Write in advance the strongest safe claim if everything works exactly as planned.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>What the stopped claim should usually look like here</strong>
<p>
For a minimal public EEG example, the planned stopping point is usually something like: <strong>reproducible classification under a named observation contract and declared split regime</strong>. It is usually <strong>not</strong> stable biomarker evidence, target-specific neural proof, or cross-day deployability.
</p>
</div>
</section>

<section class="section" id="step4">
<h2 class="section-title">Step 4: Attach the route cards before reading the score</h2>
<p>
This is the main scientific tightening in the new tutorial. The score is no longer read alone. Before the score is interpreted, the example now stacks four companion checks that answer four different questions.
</p>
<table class="data-table">
<thead>
<tr>
<th>Companion check</th>
<th>Question it answers</th>
<th>Example answer in a small EEG tutorial</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observability Budget</strong></td>
<td>What did the sensor directly observe?</td>
<td>Scalp potentials under a declared montage and preprocessing regime; not hidden state, sources, or causal controller by default.</td>
</tr>
<tr>
<td><strong>Specificity &amp; Shortcut note</strong></td>
<td>Which route could still explain the score besides the intended target?</td>
<td>Subject/session fingerprint, setup distribution, residual behavior, or other nuisance routes may still contribute unless audited separately.</td>
</tr>
<tr>
<td><strong>Temporal-validity note</strong></td>
<td>How far across time may the result be extrapolated?</td>
<td>If the decoder was evaluated only within session, the example stops at within-session evidence even if the score is strong.</td>
</tr>
<tr>
<td><strong>Calibration &amp; Abstention note</strong></td>
<td>What do the output probabilities or sets mean, and when should output stop?</td>
<td>Fit/calibration/test are separated, and low-confidence outputs can be rejected instead of forced.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Why the temporal note is now mandatory once time enters the story</strong>
<p>
Egger et al. (2024) showed that hand-gesture EEG decoding moves across a 10-hour day and that a non-updated classifier can degrade steadily over time. On this site, that means a tutorial cannot jump from “clean split” to “stable result” without stating the <strong>fixed decoder interval</strong>, <strong>state annotation</strong>, and any <strong>recalibration burden</strong>.
</p>
</div>
</section>

<section class="section" id="step5">
<h2 class="section-title">Step 5: Publish a model card plus calibration and failure logs</h2>
<p>
At the end, the model card is still the visible artifact, but it is now narrower and more explicit than the older tutorial implied. The purpose is not only to show where the model wins, but also to expose where the route breaks and what the score is still allowed to mean.
</p>
<table class="data-table">
<thead>
<tr>
<th>Output-side item</th>
<th>What to include</th>
<th>Why it matters</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>headline metrics</strong></td>
<td>Main metric bundle, baseline deltas, and slice-wise results.</td>
<td>One number alone hides which regime actually carried the result.</td>
</tr>
<tr>
<td><strong>shortcut results</strong></td>
<td>Nuisance-aware baselines, metadata-only or identity baselines when relevant, and unresolved shortcut gaps.</td>
<td>The score can otherwise be overread as target-specific evidence.</td>
</tr>
<tr>
<td><strong>temporal note</strong></td>
<td>Whether the result is same-session only, same-day only, or tested further, and whether the decoder stayed fixed.</td>
<td>Prevents silent promotion to durability.</td>
</tr>
<tr>
<td><strong>calibration report</strong></td>
<td>Fit/calibration/test split, ECE/Brier/NLL or prediction-set coverage when applicable.</td>
<td>Confidence without calibration is not yet operationally meaningful.</td>
</tr>
<tr>
<td><strong>abstention / threshold policy</strong></td>
<td>Reject option, prediction-set rule, or explicit statement that the example does not yet support one.</td>
<td>Stops threshold tweaking from hiding inside the test result.</td>
</tr>
<tr>
<td><strong>failure ledger</strong></td>
<td>Subjects, sessions, states, or setup slices where the example collapses.</td>
<td>Without this, only favorable conditions survive into the narrative.</td>
</tr>
<tr>
<td><strong>stopped claim</strong></td>
<td>One or two lines stating what the result supports and what it still does not support.</td>
<td>Prevents the example from being reused as stronger evidence than it earned.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="boundary">
<h2 class="section-title">What this example now supports, and what it still does not support</h2>
<table class="data-table">
<thead>
<tr>
<th>What this example can support</th>
<th>What it still does not support</th>
</tr>
</thead>
<tbody>
<tr>
<td>A reproducible small EEG benchmark with a named event contract and a declared split regime.</td>
<td>Physical timing truth unless the highest timing-validation rung was actually measured.</td>
</tr>
<tr>
<td>A bounded score comparison against declared baselines under a declared independence unit.</td>
<td>Target-specific neural evidence if shortcut routes remain unresolved.</td>
</tr>
<tr>
<td>A same-session or explicitly bounded temporal result.</td>
<td>Cross-day durability, fixed-decoder stability, or deployability unless those were directly audited.</td>
</tr>
<tr>
<td>A calibrated or abstaining output only if calibration and abstention were frozen and reported explicitly.</td>
<td>Causal, source-identification, or WBE-level hidden-state claims.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="minimum-pack">
<h2 class="section-title">One small pack this page now expects</h2>
<div class="key-points">
<h4>Minimum pack</h4>
<ul>
<li><strong>Dataset identity:</strong> snapshot, DOI or URL, retrieval date, and license.</li>
<li><strong>Observation contract:</strong> event anchor, event semantics, timing-validation class, label provenance, and QC.</li>
<li><strong>Benchmark object:</strong> task, target, metric bundle, split family, and independent hold-out unit.</li>
<li><strong>Shortcut note:</strong> plausible shortcut families, shortcut-aware baselines, and unresolved shortcut gap.</li>
<li><strong>Temporal note:</strong> same-session or beyond, fixed decoder or updated decoder, and stopped time claim.</li>
<li><strong>Registry:</strong> preprocessing, split freeze, baselines, failure conditions, and calibration split when needed.</li>
<li><strong>Model card:</strong> results, failures, calibration behavior, abstention behavior, and stopped claim.</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go next</h2>
<p>
If you want the full blueprint again, return to <a href="../verification.html">Verification</a>. If you want the stricter L0 checklist, go next to <a href="l0-minimum-artifact-pack.html">Wiki: Minimum artifact pack for L0</a>. If the main uncertainty is event timing or label meaning, use <a href="event-sync-and-measurement-logs.html">Wiki: Event synchronization and observation logs</a>. If the problem is shortcut resistance or hold-out ancestry, use <a href="dataset-splits-and-leakage.html">Wiki: Data splits and leakage</a>. If the claim starts to cross sessions or days, continue to <a href="state-trait-and-drift.html">Wiki: State, trait, and drift</a>.
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">References behind this correction</h2>
<ol>
<li>Brain Imaging Data Structure. <em>Events</em>. <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS specification</a>.</li>
<li>Hermes D, Pal Attia T, Beniczky S, et al. Hierarchical Event Descriptor library schema for EEG data annotation. <em>Scientific Data</em>. 2025. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">doi:10.1038/s41597-025-05791-2</a></li>
<li>Kothe C, et al. The Lab Streaming Layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>. 2025. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Lepauvre A, Hirschhorn R, Bendtz K, Mudrik L, Melloni L. A standardized framework to test event-based experiments. <em>Behavior Research Methods</em>. 2024. <a href="https://doi.org/10.3758/s13428-024-02508-y" target="_blank">doi:10.3758/s13428-024-02508-y</a></li>
<li>Chaibub Neto E, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <em>npj Digital Medicine</em>. 2019;2:99. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu L, et al. Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. <em>Frontiers in Human Neuroscience</em>. 2020;14:103. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Di Y, et al. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. <em>Frontiers in Human Neuroscience</em>. 2021;15:672946. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>Egger J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Scientific Reports</em>. 2024;14:20247. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Lei J, G'Sell M, Rinaldo A, Tibshirani RJ, Wasserman L. Distribution-Free Predictive Inference for Regression. <em>Journal of the American Statistical Association</em>. 2018;113(523):1094-1111. <a href="https://doi.org/10.1080/01621459.2017.1307116" target="_blank">doi:10.1080/01621459.2017.1307116</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">Basics of verification infrastructure -&gt;</a></li>
<li><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs -&gt;</a></li>
<li><a href="dataset-splits-and-leakage.html">Data splits and leakage -&gt;</a></li>
<li><a href="state-trait-and-drift.html">State, trait, and drift -&gt;</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../verification.html">Verification -&gt;</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on -&gt;</a></li>
<li><a href="../datasets.html">Datasets -&gt;</a></li>
</ul>
</div>
</aside>
</main>
