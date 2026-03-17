---
layout: default
title: 'Wiki: How to read claims and evidence'
description: This is a basic page for reading Mind-Upload and neuroscience news based
  on the strength of the claims and the necessary evidence.
article_type: Wiki
subtitle: Don't let flashy wording lead to strong conclusions.
author: Mind Uploading Research Project
last_updated: '2026-03-06'
note: Reading guide
audience: People who don't want to misread news or research announcements, people
  who want to get a feel for L0-L5
reading_time: 10-15 minutes
page_intro: This page is a guide to help you read the strong language that comes up
  in the talk of neuroscience and Mind-Upload by bringing it back to the strength
  of the necessary evidence. Practice differentiating between ``It looks amazing''
  and ``What has been proven?''
accuracy_note: The organization here is not to weaken the argument, but to prevent
  both overestimation and underestimation.
page_highlights:
- Practice reading L0-L5 as the strength of your argument rather than the maturity
  of your research.
- Translate common news phrases to what level the story actually is.
- We'll also show you what's missing to take you to the next level.
known_points:
- Reproducible analysis and claims of identity differ greatly in the strength of evidence
  required.
- There is a difference between the output being correct and the internal mechanism
  being correct.
- It is safe to read strong claims without conditions to disprove them or steps to
  reproduce them.
unknown_points:
- It has not yet been decided at what stage L4 will proceed to assert its identity.
- We are not yet at the stage where we can completely integrate the differences between
  theories into one evaluation axis.
wiki_links:
- label: 'Wiki: Basics of WBE'
  url: /wiki/mind-upload-basics.html
  description: This is the overall picture that is the premise of this reading.
- label: 'Wiki: Basics of verification infrastructure'
  url: /wiki/verification-basics.html
  description: I will explain why the placement of evidence itself is important.
- label: Wiki Home
  url: /wiki/
  description: You can return to other basic pages.
recommended_pages:
- label: Introduction to WBE
  url: /wbe_101.html
- label: Verification platform
  url: /verification.html
- label: FAQ
  url: /faq.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Basic rules</h2>
<p>
The language in research publications often appears stronger than the actual evidence. Therefore, first, think about where to place ``What did this result do?'' from L0 to L5. The higher the level, the more evidence you need.
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">Rephrasing L0-L5 in everyday language</h2>
<table class="data-table">
<thead>
<tr>
<th>Level</th>
<th>Roughly speaking</th>
<th>Minimum evidence you want</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>Get the same result again</td>
<td>The data, code, environment, and logs are complete and can be reproduced by a third party. </td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>You can guess something from the signal</td>
<td>Reproducibility accuracy with baseline comparison, leak inspection, and matching conditions. </td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>Can be predicted even if conditions are changed</td>
<td>Predictive matching for unlearning conditions, counterfactuals, and interventions. </td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>Stable operation in closed loop</td>
<td>Real-time operation, delay management, safe stop conditions. </td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>Discussing identity</td>
<td>Pre-registered continuity test, branch verification of memory, values, and learning. </td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>Can be used in society</td>
<td>System design including rights, consent, suspension criteria, and audit structure. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="phrases">
<h2 class="section-title">Translating common phrases</h2>
<table class="data-table">
<thead>
<tr>
<th>How to write headings</th>
<th>What is most likely actually being said</th>
<th>Additional things to check</th>
</tr>
</thead>
<tbody>
<tr>
<td>"Recovered sentences from the brain"</td>
<td>Mostly L1 decoding. </td>
<td>We will see if it holds true even under unlearning conditions, and if it is different from LLM completion. </td>
</tr>
<tr>
<td>"Reproduced the brain state with high precision"</td>
<td>L1, at best, may be the entrance to L2. </td>
<td>Check whether you are looking at predictions for condition changes and interventions. </td>
</tr>
<tr>
<td>"Behaved just like a human"</td>
<td>There is a possibility that the story remains that the behavior is similar in appearance. </td>
<td>Check whether the internal state, memory continuity, and failure conditions are exposed. </td>
</tr>
<tr>
<td>“Now you can save your identity”</td>
<td>This is a very strong argument for L4. </td>
<td>It is necessary to have a pre-registered identity test or to eliminate alternative explanations. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="checklist">
<h2 class="section-title">Three points to check when reading</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>This is somewhere between L0 and L5:</strong>First, put the strength of your argument. </li>
<li><strong>What was measured:</strong>Look at whether it is just output matching or whether it includes condition changes and interventions. </li>
<li><strong>What's a failure?</strong> Check if there are counter-conditions and steps to reproduce. </li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">What is missing to advance to the next level of argument</h2>
<p>
Even if you have the results for L1, you can't jump straight to L4. Normally, we first solidify the reproducibility of L0, then test changing the conditions of L2, and proceed by separating out any remaining points. In other words,<strong>a higher level cannot jump over a lower level</strong>.
</p>
<div class="cta-box">
<h4>Next</h4>
<p>Here is the concept of "standards, benches, registration, and audits" that supports this reading. </p>
<a href="verification-basics.html">To the basics of verification infrastructure →</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE basics →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="eeg-basics.html">EEG basics →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
<li><a href="../verification.html">Verification →</a></li>
<li><a href="../faq.html">FAQ →</a></li>
</ul>
</div>
</aside>
</main>