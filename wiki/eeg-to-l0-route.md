---
layout: default
title: "Wiki: Straight path from EEG to L0"
description: "This is a guide that will help you understand the basics of EEG, select public data, minimize the L0 loop, and proceed through verification."
article_type: Wiki
subtitle: "From an introduction to EEG to reproducible analysis, a practical route to avoid getting lost"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Practical route"
audience: "People who want to start moving from EEG, and who want to fix the order up to the minimum loop of L0"
reading_time: "8-12 minutes"
page_intro: "This page is a practical guide that, after reading the basics of EEG, organizes in a straight line which public data to start with, what to keep as a set, and where to check the victory conditions. Use it as an auxiliary line to make it easier to go back and forth between EEG 101, Datasets, Hands-on, and Verification."
accuracy_note: "What we will deal with here is the entrance to reproducible analysis of L0. Arguments after L1 and discussions of identity will not be dealt with only through this route."
page_highlights:
  - "You can read the roles in the order of EEG 101 → Datasets → Hands-on → Verification."
  - "At each stage, clarify what to decide next and what to leave behind."
  - "Points that are easy to rework can be moved to the wiki in advance."
known_points:
  - "After understanding the basics of EEG, the flow of creating L0 with public data is relatively clear."
  - "In L0, it is more important to have reproducible input, QC, processing, output, and auditing cycles than high accuracy."
  - "Datasets, Hands-on, and Verification have different roles even in the same practice."
unknown_points:
  - "We have not yet determined which starter data will most lead to future L2 and L3."
  - "After L0, which task is the shortest way to proceed to generation/intervention prediction is task dependent."
wiki_links:
  - label: "Wiki: Basics of EEG"
    url: "/wiki/eeg-basics.html"
    description: "For those who want to go back to the basics of EEG signals and noise."
  - label: "Wiki: Guide to reading practical pages"
    url: "/wiki/practical-pages-reading-guide.html"
    description: "You can first sort out the role differences between Datasets, Hands-on, and Verification."
  - label: "Wiki: Minimum artifact pack for L0"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "See in one piece what you'll end up with."
  - label: "Wiki: Data partitioning and data leaks"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "It's for people who don't want to redo it in split units or in case of a leak accident."
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Complete what's left of raw EEG."
recommended_pages:
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Data & Bench"
    url: "/datasets.html"
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Proceed in one direction</h2>
<p>
After learning EEG, it's easy to get confused about <strong>whether to select data next</strong>,<strong>to move your hand suddenly</strong>, or<strong>to check the victory conditions</strong> first. In this route, the order is fixed to one path.
</p>
</div>

<section class="section" id="route">
<h2 class="section-title">6 steps from EEG to L0</h2>
<table class="data-table">
<thead>
<tr>
<th>Order</th>
<th>Page to open</th>
<th>What to decide here</th>
<th>Conditions for proceeding to the next</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td><a href="../eeg_101.html">EEG 101</a></td>
<td>Understand what EEG can measure and what it cannot say on its own. </td>
<td>Once you have established the premise that EEG is not to be read as a magical mind-reading technique, proceed to the next step. </td>
</tr>
<tr>
<td><strong>2</strong></td>
<td><a href="../datasets.html">Datasets</a></td>
<td>First decide which public data to start L0 with. </td>
<td>Once you have narrowed down the starter data to one piece, proceed to the next step. </td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><a href="dataset-splits-and-leakage.html">Data splits and data leaks</a></td>
<td>Fix the unit of train/test and the boundaries of test that should not be touched. </td>
<td>If you can write the division rule in text, proceed to the next step. </td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs</a></td>
<td>In addition to raw EEG, decide what events, stimulation logs, synchronization, and bad segments should be saved as. </td>
<td> Once you have enumerated the minimum items in the observation log, proceed to the next step. </td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><a href="../datasets.html#l0-practice">Hands-on</a></td>
<td>Go through the steps of connecting BIDS, QC, pre-processing, baseline, and failure cases. </td>
<td>Once you have all the L0 deliverables, proceed to the next step. </td>
</tr>
<tr>
<td><strong>6</strong></td>
<td><a href="../verification.html">Verification</a></td>
<td>Check what assertion level and what the L0 you just created satisfies. </td>
<td>It will be a break if we can explain without confusing L0 and L1 and beyond. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-to-output">
<h2 class="section-title">The last thing I want to leave behind on this one straight road</h2>
<div class="key-points">
<h4>Artifact Pack</h4>
<ul>
<li><strong>Input:</strong>Data in BIDS format, metadata, events, synchronization information. </li>
<li><strong>Quality:</strong> Recording of QC logs, exclusion criteria, bad channels/bad segments. </li>
<li><strong>Processing:</strong>Pre-processing conditions, random numbers, version used, execution steps. </li>
<li><strong>Output:</strong>At least one baseline metric and its recurrence log. </li>
<li><strong>Audit:</strong>Examples of failures, conditions that went wrong, and known weaknesses. </li>
</ul>
</div>
<p>
If you would like to check only the form of the submission in one page, <a href="l0-minimum-artifact-pack.html">L0 Minimum Artifact Pack</a> is the corresponding auxiliary page.
</p>
</section>

<section class="section" id="where-to-bounce">
<h2 class="section-title">Where to return to on the way</h2>
<table class="data-table">
<thead>
<tr>
<th>Place to stop</th>
<th>Page you should return to</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stops in the sense of EEG itself</td>
<td><a href="eeg-basics.html">EEG Basics</a> / <a href="../eeg_101.html">EEG 101</a></td>
</tr>
<tr>
<td>Stops due to difference between Datasets and Hands-on</td>
<td><a href="practical-pages-reading-guide.html">Reading guide for practical pages</a></td>
</tr>
<tr>
<td>Stops due to role difference between BIDS and Validator</td>
<td><a href="standards-repositories-validators-and-benchmarks.html">Standards/Repositories/Validators/Benchmarks</a></td>
</tr>
<tr>
<td>Stops at baseline or pre-registration role</td>
<td><a href="baselines-prereg-and-model-cards.html">Baselines/preregistration/model cards</a></td>
</tr>
<tr>
<td>Stops wherever you go after L0</td>
<td><a href="claim-level-reading-routes.html">How to read each L0 to L5</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">Accidents that are likely to occur on this route</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>Create a model immediately after EEG 101:</strong> If you don't fix the data selection and segmentation rules first, the numbers will be distorted later. </li>
<li><strong>I think raw EEG is sufficient:</strong> Without events or synchronized logs, there is no comparable input. </li>
<li><strong>Completion of Hands-on can be read as success in L1 or L2:</strong> Let's start with the reproducible analysis of L0. </li>
<li><strong>Finishing without reading Verification at the end:</strong> If you do not clearly state what has been and is not yet satisfied, the level of the claim will be off. </li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">Where to return next</h2>
<p>
If you want to go back to the entrance to EEG, go back to <a href="../eeg_101.html">Introduction to EEG</a>. If you go back to the role differences in practical pages, go to <a href="practical-pages-reading-guide.html">Reading Guide for Practical Pages</a>. If you want to see how to proceed after L0, go to <a href="claim-level-reading-routes.html">How to read from L0 to L5</a> Please use.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="practical-pages-reading-guide.html">Reading guide for practical pages →</a></li>
<li><a href="l0-minimum-artifact-pack.html">L0 minimum artifact pack →</a></li>
<li><a href="dataset-splits-and-leakage.html">Data splits and data leaks →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html">Introduction to EEG →</a></li>
<li><a href="../datasets.html">Data & Bench →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
</ul>
</div>
</aside>
</main>
