---
layout: default
title: 'Wiki: Verification example walkthrough'
description: A small example of EEG will walk you through how the Data Standard, Benchmark,
  Registry, and Model Card fit together.
article_type: Wiki
subtitle: Read the blueprint by reducing it to one small example
author: Mind Uploading Research Project
last_updated: '2026-03-14'
note: Worked example
audience: People who find the Verification page abstract, and people who want to understand
  the relationships between elements through concrete examples.
reading_time: 10-15 minutes
page_intro: This page is a wiki where you can read the Verification Commons blueprint
  in order by converting it into a "small example of state classification using EEG".
  Rather than increasing the number of abstract words, visualize how input, procedure,
  evaluation, and falsification are connected.
accuracy_note: This is a minimal example for understanding. This alone does not support
  WBE's strong claims; it is a supplementary course that embodies the entrance to
  L0-L2.
page_highlights:
- You can see the differences in the roles of Data Standard, Benchmark, Registry,
  and Model Card in one example.
- You can understand why just ``having data'' is not enough by looking at the order
  of tasks.
- We will use actual examples to clarify where the issues are still unresolved.
known_points:
- You can also practice creating a minimal form of Verification Commons with public
  EEG data.
- Simply keeping inputs, procedures, evaluations, and counterevidence separate greatly
  increases comparability.
- Even in small cases, leak prevention and failure recording are essential.
unknown_points:
- Small examples like this alone do not allow us to proceed to the examination of
  identity or phenomenal consciousness.
- Which tasks have the strongest connections to future L3 and beyond is still being
  explored.
wiki_links:
- label: 'Wiki: Basics of verification infrastructure'
  url: /wiki/verification-basics.html
  description: This is for people who want to get an overview of the role first.
- label: 'Wiki: Data partitioning and leaks'
  url: /wiki/dataset-splits-and-leakage.html
  description: This complements the train/test bounds assumed in this example.
- label: Wiki Home
  url: /wiki/
  description: You can return to other auxiliary pages.
recommended_pages:
- label: Verification platform
  url: /verification.html
- label: hands-on
  url: /datasets.html#l0-practice
- label: Data & Bench
  url: /datasets.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>This small example</h2>
<p>
Here, we will use a small model that uses public EEG data to classify two states as an example. The goal is not to achieve high accuracy, but to understand<strong>the smallest set that others can check under the same conditions</strong>.
</p>
</div>

<section class="section" id="whole-picture">
<h2 class="section-title">Arrange the four parts first</h2>
<table class="data-table">
<thead>
<tr>
<th>Parts</th>
<th>What to put in this example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard</strong></td>
<td>EEG data in BIDS format, subject information, event definitions, and QC logs. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>What to predict, which division to compare, and which index to score. </td>
</tr>
<tr>
<td><strong>Registry</strong></td>
<td>This is a record in which preprocessing conditions, division rules, stopping conditions, and baselines are fixed in advance. </td>
</tr>
<tr>
<td><strong>Model Card</strong></td>
<td>Summary of final scores, failure examples, leak tests, weaknesses, and calculation conditions. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="step1">
<h2 class="section-title">Step 1: First, fix the input shape</h2>
<p>
Even with the same EEG data, missing event definitions and electrode information will prevent others from reproducing the same analysis. The first thing you need isn't an "amazing model"; you need <strong>a clear idea of ​​what you're passing as input</strong>.
</p>
<div class="key-points">
<h4>What you want at least</h4>
<ul>
<li><strong>BIDS format:</strong> Matches file placement and metadata format. </li>
<li><strong>QC Log:</strong>Leaves missing, noisy, and exclusion reasons. </li>
<li><strong>Division unit:</strong>Specify whether it is by subject or session. </li>
</ul>
</div>
</section>

<section class="section" id="step2">
<h2 class="section-title">Step 2: Fix the comparison method</h2>
<p>
Next, put Benchmark. This is the part where you decide what to consider as the correct answer and what to compare it with. If this is vague, you will be able to escape to a more convenient indicator later.
</p>
<table class="data-table">
<thead>
<tr>
<th>Item</th>
<th>Fixed content in this example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Assignment</strong></td>
<td>2 Do the state classification and fix it first. </td>
</tr>
<tr>
<td><strong>Split</strong></td>
<td>Separate train/validation/test for each subject. </td>
</tr>
<tr>
<td><strong>Indicators</strong></td>
<td>In addition to accuracy, it also records confusion matrices and failure examples. </td>
</tr>
<tr>
<td><strong>Baseline</strong></td>
<td>Place one simple classifier and check the improvement. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="step3">
<h2 class="section-title">Step 3: Leave a promise before doing it</h2>
<p>
Registry is a component that prevents you from changing the conditions later and assuming you won. For example, first write down which preprocessing to use, when to stop it, and where to not use test.
</p>
<div class="note-box">
<strong>What I would like to write here first</strong>
<p>
These are preprocessing candidates, division rules, baselines, scoring indicators, conditions for failure, and what to keep as differences when updating. Being able to read and audit later is more important than fancy formatting.
</p>
</div>
</section>

<section class="section" id="step4">
<h2 class="section-title">Step 4: Finally, publish with Model Card</h2>
<p>
In the end, what we need to do is not just announce the scores, but also record ``where we won and where we collapsed.'' This is the role of the Model Card.
</p>
<div class="key-points">
<h4>Minimum items you want to include</h4>
<ul>
<li><strong>Results:</strong>Key metrics, differences from baseline, rerun conditions. </li>
<li><strong>Leak check:</strong>Is test information mixed in during splitting or preprocessing? </li>
<li><strong>Example of failure:</strong>For which subjects and under what conditions does it tend to collapse? </li>
<li><strong>Weaknesses:</strong>OOD, noise, computational cost, known limitations. </li>
</ul>
</div>
</section>

<section class="section" id="boundary">
<h2 class="section-title">What you can learn/don't understand from this example</h2>
<table class="data-table">
<thead>
<tr>
<th>What you can learn from this example</th>
<th>Things you can't understand from this example only</th>
</tr>
</thead>
<tbody>
<tr>
<td>How to create a reproducible minimum loop between L0 and L1. </td>
<td>Individuality, phenomenal consciousness, conditions for L4 and beyond. </td>
</tr>
<tr>
<td>A form of comparable evaluation that avoids leaks. </td>
<td>Strong causal claims that include interventions and closed loops. </td>
</tr>
<tr>
<td>What should I record to make it easier for others to try again? </td>
<td>Which theory is ultimately correct as an explanation of consciousness? </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
If you want to go back to the blueprint itself, read <a href="../verification.html">Verification Foundation</a>, if you want to actually run the minimal loop, read <a href="../datasets.html#l0-practice">Hands-on</a>, and if you want to review the input data, read <a href="../datasets.html">Data & Bench</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="dataset-splits-and-leakage.html">Data splits and data leaks →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG preprocessing and QC →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
<li><a href="../datasets.html">Data & Bench →</a></li>
</ul>
</div>
</aside>
</main>