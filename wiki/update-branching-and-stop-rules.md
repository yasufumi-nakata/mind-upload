---
layout: default
title: "Wiki: Update/branch/stop rules"
description: "We'll sort out the differences between model updates, version control, branching, stopping conditions, and kill switches from the beginning."
article_type: Wiki
subtitle: "Basics for auditing changing systems as they change"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Learning guide"
audience: "People who are unclear about the difference between learning updates, branches, and stop rules"
reading_time: "10-15 minutes"
page_intro: "This page is a wiki that breaks down the ``updates,'' ``versions,'' ``branches,'' ``stopping rules,'' and ``kill switches'' that frequently appear in Mind-Upload from the beginning. Don't just assume that just because your score has increased, it's a natural progression of the same system; use it as a basis for auditing changes with a history."
accuracy_note: "What is shown here is a basic arrangement for operation and verification. The final criteria for how much change should be maintained and which stopping rule is sufficient are still undetermined depending on issues and theories."
page_highlights:
  - "It is important not to confuse updates, branches, stopping rules, and kill switches."
  - "Version control and difference logs are the prerequisites for identity evaluation and security evaluation."
  - "Score improvement alone does not guarantee safe updates or consistency."
known_points:
  - "If learning and model updates are allowed, history management and differential recording are necessary."
  - "When bifurcation occurs, it becomes difficult to treat it as a single 'same individual.'"
  - "Stopping rules are stronger if you fix them in advance rather than after you see the results."
unknown_points:
  - "It is undetermined how much drift or divergence is considered to be within the range of identity."
  - "The handling of responsibilities and rights after the L4/L5 bifurcation is unresolved, including the institutional aspects."
wiki_links:
  - label: "Wiki: Identity assessment and continuity test"
    url: "/wiki/identity-and-continuity-tests.html"
    description: "Takes you back to the full L4 continuity test."
  - label: "Wiki: state/trait/drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Complete how to distinguish between updates and long-term changes."
  - label: "Wiki: Baseline/Pre-registration/Model Card"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Compensates for the role difference between pre-registration and result recording."
  - label: "Wiki: Closed loop, delay, jitter, safe stop"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Complements how to think about safe stops in real time."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "You can return to other auxiliary pages."
recommended_pages:
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
  - label: "Verification base"
    url: "/verification.html"
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest distinction</h2>
<p>
<strong>Update</strong> is a change that inherits the same history, <strong>Branch</strong> is when multiple histories are run from the same starting point, <strong>Stop rule</strong> is a pre-rule for what results to cancel or suspend, and <strong>Kill switch</strong> is an emergency stop method in case of danger. They are similar, but their roles are different.
</p>
</div>

<section class="section" id="why-this-matters">
<h2 class="section-title">Why is this distinction necessary?</h2>
<p>
When it comes to WBE and identity, the system is not fixed. If you learn, it will change, if you copy it, it will separate, and if you use it, you will have to decide whether to stop it. If this is left vague, it is easy to read things too strongly, such as, ``It's better than the previous version, so it's a healthy progression of the same system,'' or ``Even after the divergence, it's all the same person.''
</p>
</section>

<section class="section" id="terms">
<h2 class="section-title">First, separate terms</h2>
<table class="data-table">
<thead>
<tr>
<th>Term</th>
<th>Rough meaning</th>
<th>Important points here</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>update</strong></td>
<td>Introducing new learning or setting changes to the same system. </td>
<td>If you do not record what has changed in the differences, the meaning of the evaluation will be ambiguous. </td>
</tr>
<tr>
<td><strong>version</strong></td>
<td>The ID assigned to the fixed state at that point. </td>
<td>It is important to be able to go back and compare without overwriting previous versions. </td>
</tr>
<tr>
<td><strong>branch</strong></td>
<td>Separate update histories start running from the same starting point. </td>
<td>Since the history after branching is different, it is safer not to mix them in the same evaluation unit. </td>
</tr>
<tr>
<td><strong>stop rule</strong></td>
<td>These are advance rules that determine which results should be used to cancel, suspend, or withdraw. </td>
<td>It will be stronger as a verification if you fix it first rather than deciding after seeing the results. </td>
</tr>
<tr>
<td><strong>Kill Switch / Isolation</strong></td>
<td>This is a mechanism that stops or disconnects operations when a safety problem occurs. </td>
<td>Unlike stopping rules, the main purpose is to ensure safety rather than statistical judgment. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="safe-update">
<h2 class="section-title">Minimum check to see if it is OK to update</h2>
<table class="data-table">
<thead>
<tr>
<th>Check items</th>
<th>The minimum thing I want to do</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Clarification of changes</strong></td>
<td>Write down the changes made to the data, preprocessing, model, and evaluation metrics. </td>
</tr>
<tr>
<td><strong>Save previous version</strong></td>
<td>Does not overwrite the previous version, leaving a state where it can be rerun with the same input. </td>
</tr>
<tr>
<td><strong>Fixing comparison conditions</strong></td>
<td>Compare with the previous version using the same test, the same evaluation metrics, and the same baseline. </td>
</tr>
<tr>
<td><strong>Recheck for leaks</strong></td>
<td>Recheck that the train/test boundaries and normalization procedure are not corrupted by updating. </td>
</tr>
<tr>
<td><strong>Handling in case of failure</strong></td>
<td>Decide first where to suspend or cancel updates in the event of performance deterioration or instability. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Important</strong>
<p>
Just because your score has increased doesn't mean it's a safe update. Since the numbers can increase due to leaks, evaluation changes, or convenient subset selection, it is necessary to keep a set of <strong>differences</strong> and <strong>comparison conditions</strong>.
</p>
</div>
</section>

<section class="section" id="branching">
<h2 class="section-title">What to fix when a branch occurs</h2>
<table class="data-table">
<thead>
<tr>
<th>What you want to fix</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Branch point</strong></td>
<td>This is to clarify which version and data point the branch was made from. </td>
</tr>
<tr>
<td><strong>Parent-child relationship</strong></td>
<td>Enables auditing of which branch inherited which parent version. </td>
</tr>
<tr>
<td><strong>Individual ID / Instance ID</strong></td>
<td>This is to avoid confusing multiple histories as the same individual. </td>
</tr>
<tr>
<td><strong>Evaluation period</strong></td>
<td>This is to distinguish between whether they are similar just after the branch or whether they are similar for a long time. </td>
</tr>
<tr>
<td><strong>Attribution rules</strong></td>
<td>This is to fix which results are recorded as achievements/failures of which branch. </td>
</tr>
</tbody>
</table>
<p>
Particularly in discussions of identity, it is dangerous to collectively refer to all results after branching as the "principal." At a minimum, you should record<strong>up to what point you treat them as the same unit of</strong>evaluation.
</p>
</section>

<section class="section" id="stop-vs-kill">
<h2 class="section-title">Stopping rules and kill switches are different</h2>
<table class="data-table">
<thead>
<tr>
<th>How it works</th>
<th>When to decide</th>
<th>Main purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Stopping rules</strong></td>
<td>Before experiments and evaluation. </td>
<td>This is to avoid leaving the failure judgment and withdrawal line behind. </td>
</tr>
<tr>
<td><strong>Hold / freeze</strong></td>
<td>This is when the problem was discovered. </td>
<td>This is to temporarily suspend updates and publishing until the cause is determined. </td>
</tr>
<tr>
<td><strong>Kill Switch / Isolation</strong></td>
<td>Implement it in advance in case of safety issues. </td>
<td>This is to quickly stop any dangerous behavior or deviation. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Common confusion</strong>
<p>
``I stopped because the results were bad'' is about stopping rules, and ``I stopped immediately because it was dangerous'' is about safety. The same word ``stop'' has different meanings when it comes to handling evidence and safety measures.
</p>
</div>
<p>
Particularly in closed-loop implementations, safe stopping for delays and abnormal behavior becomes additionally important. If you want to organize only real-time system entrances first, please see <a href="closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed loop, delay, jitter, and safety stops</a>.
</p>
</section>

<section class="section" id="logs">
<h2 class="section-title">The minimum log you want to keep</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>version ID:</strong>Which version have you just evaluated? </li>
<li><strong>parent / branch ID:</strong>Where you branched from. </li>
<li><strong>Change Diff:</strong>What changed in the data, preprocessing, model, and evaluation? </li>
<li><strong>Comparison results: Differences, improvements, deteriorations, and uncertainties from the previous version. </li>
<li><strong>Stopping decision:</strong>What rules were touched or not touched? </li>
<li><strong>Failure example:</strong>Conditions that did not work or collapsed. </li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">3 questions when reading strong arguments</h2>
<ol>
<li><strong>Are there any differences before and after the update?</strong>If it's unclear what has changed, it's safe not to read too much into the meaning of the improvement. </li>
<li><strong>Do you have a branch ID and observation period?</strong> Check if you have combined multiple histories into one. </li>
<li><strong>Have the stopping rules been determined in advance?</strong>Check whether the handling when a bad result is obtained has not been rewritten later. </li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
If you want to go back to I5 / I8 / V7 of Roadmap, please use <a href="../tech_roadmap.html">Technology Roadmap</a>, if you want to go back to Registry / Audit of verification platform, please use <a href="../verification.html">Verification Platform</a>, and if you want to go back to L0 practice, please use <a href="../datasets.html#l0-practice">Hands-on</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="identity-and-continuity-tests.html">Identity assessment and continuity tests →</a></li>
<li><a href="state-trait-and-drift.html">state / trait / drift →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">Baselines/preregistration/model cards →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../tech_roadmap.html">Technology roadmap →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
</ul>
</div>
</aside>
</main>
