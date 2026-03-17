---
layout: default
title: 'Wiki: 4 paths to follow after Verification'
description: 'After reading Verification, organize where to proceed: L0 implementation,
  L2 verification, L3 closed loop, and L4 identity.'
article_type: Wiki
subtitle: A guide to help you decide the next page without hesitation after reading
  the verification platform
author: Mind Uploading Research Project
last_updated: '2026-03-14'
note: Reading route
audience: People who are confused about where to go next after reading Verification
reading_time: 6-10 minutes
page_intro: This page is a guide to help you decide which page to publish next depending
  on what you want to know after reading Verification. The next page will change depending
  on whether you go back to L0 implementation, L2 intervention verification, L3 closed
  loop, or L4 identity.
accuracy_note: Here is the next entrance to Verification. Please be sure to check
  the actual conditions for each route in the main text of the original page.
page_highlights:
- 'After reading Verification, organize it into four routes: L0, L2, L3, and L4.'
- Specify that the next required page changes as the claim level increases.
- Reduce the situation of ``I read the verification platform, but I don't know what
  to read next''.
known_points:
- Verification is an overall blueprint, so the next page is too large as it is.
- The page to return to differs depending on L0 implementation, L2 verification, L3
  closed loop, and L4 identity.
- If you fix the route after Verification, the reading becomes much more stable.
unknown_points:
- Which route will ultimately become the most important may change as the project
  progresses.
- The final conditions for L4 and L5 are still undetermined.
wiki_links:
- label: 'Wiki: How to read each L0 to L5'
  url: /wiki/claim-level-reading-routes.html
  description: This is for those who want to return to the overall path of the level.
- label: 'Wiki: Guide to reading practical pages'
  url: /wiki/practical-pages-reading-guide.html
  description: This is for those who want to see the role differences between Verification,
    Datasets, and Hands-on first.
- label: 'Wiki: Straight path from EEG to L0'
  url: /wiki/eeg-to-l0-route.html
  description: This is for people who want to see only the specific route on the L0
    side right away.
recommended_pages:
- label: Verification platform
  url: /verification.html
- label: hands-on
  url: /datasets.html#l0-practice
- label: technology roadmap
  url: /tech_roadmap.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Decide the next page</h2>
<p>
Verification is important as a blueprint, but just reading it is too broad for the next work. Here, we will divide it into four paths based on <strong>What do you want to know next</strong> and pin the next page.
</p>
</div>

<section class="section" id="four-routes">
<h2 class="section-title">Four paths to follow after Verification</h2>
<table class="data-table">
<thead>
<tr>
<th>What I want to know</th>
<th>Next page</th>
<th>What to decide there</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I want to create an implementation of L0</strong></td>
<td><a href="../datasets.html#l0-practice">Hands-on</a></td>
<td>Fix the procedure that connects input, QC, preprocessing, baseline, and failure cases. </td>
</tr>
<tr>
<td><strong>I want to know about L2 intervention/counterfactual verification</strong></td>
<td><a href="../tech_roadmap.html">Roadmap</a></td>
<td>Check which issues lead to causal verification and generation prediction using dependency relationships. </td>
</tr>
<tr>
<td><strong>I want to know the closed loop conditions of L3</strong></td>
<td><a href="../eeg_101.html">EEG 101</a> or <a href="closed-loop-latency-jitter-and-safety-stops.html">Closed-loop/delay/jitter/safety stops</a></td>
<td>Separate the difference between offline accuracy and real-time stability. </td>
</tr>
<tr>
<td><strong>I want to know the identity of L4</strong></td>
<td><a href="../wbe_101.html">WBE 101</a> or <a href="identity-and-continuity-tests.html">Identity Assessment and Continuity Tests</a></td>
<td>Check what you want to consider as continuous in terms of memory, values, learning, and branching. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why">
<h2 class="section-title">Why this division</h2>
<table class="data-table">
<thead>
<tr>
<th>way</th>
<th>Reasons for going to that page after Verification</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0 implementation</strong></td>
<td>This is because it is necessary to translate the passing conditions determined in Verification into actual deliverables in Hands-on. </td>
</tr>
<tr>
<td><strong>L2 validation</strong></td>
<td>It's easy to jump into interventions and counterfactuals if you don't look at the roadmap to see which points need to be addressed first. </td>
</tr>
<tr>
<td><strong>L3 Closed Loop</strong></td>
<td>For closed loops, it is not enough to just evaluate the verification design; it is also necessary to look at measurement and real-time constraints. </td>
</tr>
<tr>
<td><strong>L4 Personality</strong></td>
<td>This is because you can't measure your identity based on your score alone; you need to first organize what you want to pre-register and test. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="helper-wiki">
<h2 class="section-title">Each-way assistance wiki</h2>
<table class="data-table">
<thead>
<tr>
<th>way</th>
<th>Wiki worth watching together</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0 implementation</strong></td>
<td><a href="eeg-to-l0-route.html">A straight path from EEG to L0</a> / <a href="l0-minimum-artifact-pack.html">The minimum artifact pack for L0</a></td>
</tr>
<tr>
<td><strong>L2 validation</strong></td>
<td><a href="counterfactual-and-perturbation-verification.html">Verification of counterfactuals, interventions, and perturbations</a> / <a href="observation-to-estimation.html">From observation to estimation</a></td>
</tr>
<tr>
<td><strong>L3 Closed Loop</strong></td>
<td><a href="closed-loop-latency-jitter-and-safety-stops.html">Closed-loop/delay/jitter/safety stops</a></td>
</tr>
<tr>
<td><strong>L4 Personality</strong></td>
<td><a href="identity-and-continuity-tests.html">Personhood assessment and continuity tests</a> / <a href="personhood-and-copy-problem.html">Personhood and copy problems</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">Common ways to get lost</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>Just reading Verification makes me feel like I've decided what to do next:</strong> Actually, I need to narrow it down to one route. </li>
<li><strong>Start tracking L0 and L2 at the same time:</strong> It is easier to establish reproducible analysis first, as it will require less rework. </li>
<li><strong>Think of L3 in terms of accuracy only:</strong> Closed loops require additional delays and safety stops. </li>
<li><strong>Think of L4 as an extension of the score:</strong> It is necessary to separately design in advance what is considered to be continuous in terms of individuality. </li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">Where to return next</h2>
<p>
To return to the main text of Verification, please use <a href="../verification.html">Verification base</a>. To return to the route of the entire level, please use <a href="claim-level-reading-routes.html">How to read each L0 to L5</a>. To return to the role differences across practical pages, please use <a href="practical-pages-reading-guide.html">Reading guide for practical pages</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="claim-level-reading-routes.html">How to read each L0 to L5 →</a></li>
<li><a href="practical-pages-reading-guide.html">Reading guide for practical pages →</a></li>
<li><a href="eeg-to-l0-route.html">Single road from EEG to L0 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
<li><a href="../tech_roadmap.html">Technology roadmap →</a></li>
</ul>
</div>
</aside>
</main>