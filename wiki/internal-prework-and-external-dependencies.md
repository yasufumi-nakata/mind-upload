---
layout: default
title: "Wiki: Distinguishing between what to do first in-house and external dependencies"
description: "This is an auxiliary page for issues, joint research, experiments, and standardization proposals to separate what can be done within this repository and what requires a partner or system."
article_type: Wiki
subtitle: "Breaking down the work that looks like 'waiting for the other person' into preparation work"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Operational guide"
audience: "People who write issues, look at collaborative research candidates, and want to organize what changes can be made now."
reading_time: "8-12 minutes"
page_intro: "This page is an auxiliary page for reading the ``external dependencies'' that come up many times in the operation of Mind-Upload, not as a reason to stop, but as a target for decomposition.The focus here is to distinguish between things that can be created first with this repository and things that require a partner or system."
accuracy_note: "This page is an aid to help separate the work. This page alone cannot guarantee that an actual agreement, contract, IRB, or equipment use will be established."
page_highlights:
  - "Do not leave external dependencies as a box where nothing can be done, but break them down into in-house preparations."
  - "Organize the minimum preparations common to issues, joint research, experiments, and standardization proposals."
  - "Separate changes that can be completed in this repository now and work that should be managed on a separate track."
known_points:
  - "Even for externally dependent tasks, requirements specifications, judgment conditions, public log formats, comparison tables, etc. can be created in-house first."
  - "It will be easier to move forward if you organize the minimum deliverables and request details on one page before approaching the other party."
  - "Whether it's an issue or a joint research project, it's important to clearly state what can be done right now."
unknown_points:
  - "Which external candidates will actually agree and on what terms will depend on factors on the other side."
  - "IRB, contract, funding, and equipment availability timing will be determined outside of this page."
wiki_links:
  - label: "Wiki: How to read suggestions and state labels"
    url: "/wiki/proposal-status-reading.html"
    description: "We will first sort out the differences in stages such as proposals, document reflection, and external dependencies."
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Explains why requirements specifications and judgment conditions are created first."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "You can return to other auxiliary pages."
recommended_pages:
  - label: "Contribution Guide"
    url: "/issue.html"
  - label: "Collaboration candidate"
    url: "/issue.html#external-collaboration"
  - label: "Verification base"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>What I would like to share first</h2>
<p>
Externally dependent tasks are work that <strong>cannot be completed by itself. However, that doesn't mean that you can't do anything<strong>for us. You can make preparations before making a request, judgment conditions, public log format, comparison table, etc. in advance.
</p>
</div>

<div class="note-box">
<strong>When you want to decide the next page after the participation page</strong>
<p>
After reading Issues and Collaborations, if you want to see in one page whether you should move on to small modifications, condition design, working from literature, or L0 implementation preparation, please see <a href="participation-next-routes.html">Five paths to follow after participation/collaboration page</a>.
</p>
</div>

<section class="section" id="two-columns">
<h2 class="section-title">Read in-house production and external dependencies in two columns</h2>
<table class="data-table">
<thead>
<tr>
<th>Type</th>
<th>What you can do now with this repository</th>
<th>Becoming externally dependent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Experiment</strong></td>
<td>You can create requirement specifications, evaluation indicators, stopping conditions, public log formats, and pre-registration drafts. </td>
<td>IRB, subject recruitment, equipment usage, and measurement data acquisition are dependent on external parties. </td>
</tr>
<tr>
<td><strong>Joint research</strong></td>
<td>You can create a one-page summary, minimum deliverables, request scope, comparison table, and reanalysis plan. </td>
<td>Co-author agreements, contracts, partner approvals, and data sharing conditions are externally dependent. </td>
</tr>
<tr>
<td><strong>Standardization proposal</strong></td>
<td>You can create specification drafts, difference tables, sample logs, and assumed use cases. </td>
<td>Community adoption, official specification reflection, and external review are externally dependent. </td>
</tr>
<tr>
<td><strong>Funds/systems</strong></td>
<td>You can organize the purpose, minimum scope, deliverables, and required budget. </td>
<td>Formal decisions on adoption, budget allocation, legal decisions, and system design are externally dependent. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="prework-pack">
<h2 class="section-title">Minimum preparations that you want to make first even if there are external dependencies</h2>
<table class="data-table">
<thead>
<tr>
<th>Preparations</th>
<th>Minimum contents</th>
<th>Why is it necessary</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>One page summary</strong></td>
<td>Purpose, what you want from the other person, and what you already have. </td>
<td>This is so that the other person can quickly determine what you are talking about. </td>
</tr>
<tr>
<td><strong>Minimum deliverables</strong></td>
<td>This definition narrows down the minimum scope to one. </td>
<td>If the request is too large, it will be difficult to reach an initial agreement. </td>
</tr>
<tr>
<td><strong>Judgment conditions</strong></td>
<td>What should we do to move forward? What should we put on hold? What should we do to fail? </td>
<td>This is to prevent the goal from shifting as the story progresses. </td>
</tr>
<tr>
<td><strong>Publishable preparation</strong></td>
<td>Specification draft, QC log example, comparison table, BIDS template, checklist. </td>
<td>This is because it makes it easier to show how serious you are and how specific you are. </td>
</tr>
<tr>
<td><strong>External dependency boundaries</strong></td>
<td>Who needs to make decisions regarding IRB, equipment, contracts, legal matters, approval of the other party, etc.? </td>
<td>This is to avoid confusing immediate work with waiting work. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="issue-vs-collab">
<h2 class="section-title">Slight differences between issues and collaborative research</h2>
<table class="data-table">
<thead>
<tr>
<th>Scene</th>
<th>What I want to fix first</th>
<th>Things that become external dependencies</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>When creating an issue</strong></td>
<td>Where you stopped, what you lacked, conditions for progress, and conditions for disproving. </td>
<td>If we need experiments or legal matters, we will cut it out as a separate track. </td>
</tr>
<tr>
<td><strong>When looking at joint research candidates</strong></td>
<td>The scope of what you want to ask the other party for and the deliverables that you can produce first. </td>
<td>Agreement, co-authorship, data usage conditions, and equipment usage remain. </td>
</tr>
<tr>
<td><strong>When submitting a standardization proposal</strong></td>
<td> Difference tables, samples, and points that are lacking in the current standard. </td>
<td>Remains subject to community review and formal adoption. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">Common confusion</h2>
<div class="key-points">
<h4>Misread</h4>
<ul>
<li><strong>"Do nothing now because it depends on external sources":</strong> Specifications, comparison tables, log formats, and minimum deliverables can be created first. </li>
<li><strong>``It's progressing because it's written in writing'':</strong> The preliminary preparations to hand it over to the other party and the actual agreement being reached are two different things. </li>
<li><strong>"The bigger the plan, the better":</strong> If you don't cut the minimum scope at first, neither requests nor issues will work. </li>
<li><strong>"Treat external dependencies as complete in the main text":</strong> This should be especially avoided, and should be written separately from in-house changes that have a trail. </li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">Where to return next</h2>
<p>
Please return to <a href="../issue.html">Contribution Guide</a> to return to how to write an issue, <a href="../issue.html#external-collaboration">Collaboration Candidates</a> to organize joint research candidates, and return to <a href="../verification.html">Verification Platform</a> to solidify requirements specifications and judgment conditions.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="proposal-status-reading.html">How to read proposals and status labels →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="roadmap-reading-guide.html">How to read the roadmap →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../issue.html">Contribution guide →</a></li>
<li><a href="../issue.html#external-collaboration">Collaboration candidates →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
</aside>
</main>
