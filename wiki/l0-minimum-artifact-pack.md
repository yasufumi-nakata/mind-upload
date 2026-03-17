---
layout: default
title: "Wiki: Minimum artifact pack for L0"
description: "Organize the minimum L0 deliverables such as dataset version, BIDS, Validator, QC log, split rules, baseline, execution steps, failure examples, etc."
article_type: Wiki
subtitle: "Auxiliary page for checking 'Minimal Loop' in the form of submissions"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Operational guide"
audience: "People who have started creating L0, and people who want to check to what extent it can be called reproducible analysis."
reading_time: "8-12 minutes"
page_intro: "This page is an auxiliary page that organizes what should be finalized as a set when creating a reproducible analysis of L0. Rather than a procedure manual, it is used to focus on the form of the submission and check ``what is necessary for a third party to rerun?''"
accuracy_note: "What we are dealing with here is the bare minimum of L0. Although this alone will not allow us to proceed to a discussion of causal claims or identity, it is important as a starting point for comparison."
page_highlights:
  - "Dataset version, BIDS, Validator, QC, split, baseline, execution steps, and failure examples are organized in one pack."
  - "It makes it easier to find omissions such as 'there is a procedure but no log' or 'there is accuracy but no division rule'."
  - "It bridges the work procedure of hands_on and the product design of verification."
known_points:
  - "For L0, it is more important than high accuracy that a third party can rerun under the same conditions."
  - "Comparability is greatly improved just by having the BIDS format, QC logs, splitting rules, and baselines in place."
  - "Even if the dataset name is the same, if the snapshot or version is different, it will not be reproduced."
  - "Examples of failures and known stumbling blocks should be included as part of the deliverables."
unknown_points:
  - "Which baselines and QC metrics ultimately work best will vary from challenge to challenge."
  - "Beyond L0, the extent to which it will be extended to L1/L2 standard deliverables will depend on future development."
wiki_links:
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "You can see from the beginning why artifacts are fixed first."
  - label: "Wiki: Data partitioning and leaks"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "Supplements the reason why splitting rules go into artifacts."
  - label: "Wiki: Baseline/Pre-registration/Model Card"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Compensates for the role differences between baseline and failure examples."
recommended_pages:
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
  - label: "Data & Bench"
    url: "/datasets.html"
  - label: "Verification base"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>First, think in terms of one pack</h2>
<p>
The L0 artifact is not a single file or a single score. Only when the <strong>version of the input</strong>, <strong>form of the input</strong>, <strong>quality trail</strong>, <strong>evaluation rules</strong>, and <strong>re-execution steps</strong> are in place can a third party track the results.
</p>
</div>

<section class="section" id="artifact-pack">
<h2 class="section-title">Minimum 8 points you want to have in L0</h2>
<table class="data-table">
<thead>
<tr>
<th>Deliverables</th>
<th>Minimum desired contents</th>
<th>What is the problem if it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Data version</strong></td>
<td>OpenNeuro snapshot, PhysioNet version, DOI, acquisition date, or persistent URL. </td>
<td>Even with the same dataset name, different versions are mixed, making it impossible to reproduce. </td>
</tr>
<tr>
<td><strong>2. Data skeleton</strong></td>
<td>BIDS skeleton, minimum metadata, task name, electrode information. </td>
<td>Different people cannot have the same input, and the starting points for comparison will not be the same. </td>
</tr>
<tr>
<td><strong>3. Standards confirmation results</strong></td>
<td>The reason for the warning left by the BIDS Validator. </td>
<td>It is easier to overlook non-shareable standard violations. </td>
</tr>
<tr>
<td><strong>4. QC log</strong></td>
<td>Numerical record of missingness, noise, artifacts, and reasons for exclusion. </td>
<td>Which data is bad will depend on the person, and reproducibility will be broken. </td>
</tr>
<tr>
<td><strong>5. Split rule</strong></td>
<td>Within-session / cross-session / cross-subject, train/test unit, leak prevention rules, promise not to touch test. </td>
<td>Unable to see the upward swing in the numbers, the entire evaluation collapses. </td>
</tr>
<tr>
<td><strong>6. Baseline results</strong></td>
<td>One simple indicator, settings and results table. </td>
<td>There will be no starting point for claiming improvements. </td>
</tr>
<tr>
<td><strong>7. Execution steps</strong></td>
<td>Commands, environments, random numbers, preprocessing conditions, known stumbling blocks. </td>
<td>Other people cannot rerun the same flow. </td>
</tr>
<tr>
<td><strong>8. Failure example</strong></td>
<td>Excluded conditions, settings that did not work, and points to note. </td>
<td>Only successes remain, and the next person repeats the same failure. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="minimum-shape">
<h2 class="section-title">In short,</h2>
<div class="key-points">
<h4>Pack</h4>
<ul>
<li><strong>Input:</strong> Fixed version + BIDS shape</li>
<li><strong>Quality:</strong> QC and Validator</li>
<li><strong>Evaluation:</strong> Split rules and baselines</li>
<li><strong>Replay:</strong> Execution steps and failure examples</li>
</ul>
</div>
</section>

<section class="section" id="common-gaps">
<h2 class="section-title">Common omissions</h2>
<table class="data-table">
<thead>
<tr>
<th>Common conditions</th>
<th>What is still missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>dataset name exists</strong></td>
<td>Snapshot, version, DOI, and acquisition date may not remain. </td>
</tr>
<tr>
<td><strong>Waveform file is available</strong></td>
<td>Events, synchronization, bad segments, and issue definitions may be missing. </td>
</tr>
<tr>
<td><strong>Accuracy is there</strong></td>
<td>There may be no difference from the splitting rule, leak check, or baseline. </td>
</tr>
<tr>
<td><strong>There is a code</strong></td>
<td>Environment, random numbers, execution order, and known failure conditions may not be written. </td>
</tr>
<tr>
<td><strong>I thought I did QC</strong></td>
<td>Numeric logs and exclusion reasons may not remain. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="exit-criteria">
<h2 class="section-title">Simple judgment of L0 completion</h2>
<table class="data-table">
<thead>
<tr>
<th>Question</th>
<th>If yes, move forward</th>
<th>If no, what to do next</th>
</tr>
</thead>
<tbody>
<tr>
<td>Can other people have the same version of input</td>
<td>Snapshot / version / DOI and BIDS skeleton are complete. </td>
<td>Fix the data version and skeleton first. </td>
</tr>
<tr>
<td>Do you know what data was excluded?</td>
<td>QC logs and exclusion reasons remain. </td>
<td>Download to numerical log. </td>
</tr>
<tr>
<td>Can you explain how to make numbers</td>
<td>Split rules and baselines are fixed. </td>
<td>Fix train/test and comparison partner first. </td>
</tr>
<tr>
<td>Can someone else run it again</td>
<td>Command, environment, and known failure conditions remain. </td>
<td>Create a short runbook. </td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>What this page doesn't do</strong>
<p>
Here we do not decide which model is the strongest or which indicators are ultimately correct. The first objective of L0 is to create a comparable starting point.
</p>
</div>

<section class="section" id="next-step">
<h2 class="section-title">Where to return next</h2>
<p>
Return to <a href="../datasets.html#l0-practice">Hands-On</a> if you want to follow the actual steps, <a href="../datasets.html">Data & Bench</a> if you want to reselect the input data, or return to <a href="../verification.html">Verification Infrastructure</a> if you want to see how this product stacks up as a public good.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="dataset-splits-and-leakage.html">Data splits and data leaks →</a></li>
<li><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">Baselines/preregistration/model cards →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
<li><a href="../datasets.html">Data & Bench →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
</aside>
</main>
