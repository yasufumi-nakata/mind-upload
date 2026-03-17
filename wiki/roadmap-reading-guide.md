---
layout: default
title: 'Wiki: How to read the roadmap'
description: This is a supplementary page that explains what the symbols P/M/R/I/V/D
  mean and in what order they should be read to avoid confusion.
article_type: Wiki
subtitle: Read your technology roadmap as a dependency map rather than a long list
author: Mind Uploading Research Project
last_updated: '2026-03-06'
note: Reading guide
audience: People who get lost because of the many symbols on the technology roadmap,
  and people who want to know the order in which to read them.
reading_time: 8-12 minutes
page_intro: This page is a supplementary page that explains what P/M/R/I/V/D in the
  technology roadmap means and where to start to read them to avoid getting lost.
  Rather than resummarizing the main text of the roadmap, we will organize the ``how
  to read the map'' itself.
accuracy_note: This page is a reading aid. Please be sure to return to the main text
  of the technology roadmap for the official list of issues and current arrangement.
page_highlights:
- We will explain P/M/R/I/V/D not as mere symbols but as ``types of questions.''
- It shows in which order the layers tend to get clogged and why the previous layer
  cannot be skipped.
- There are also separate entrances for reading according to interest.
known_points:
- P is the definition of progress, M is measurement, R is reconstruction, I is implementation,
  V is verification, and D is social implementation.
- The stronger the argument, the further back it is, and the more unorganized the
  previous layer is, the more difficult it is to move forward.
- It's best to read a roadmap as a map of dependencies rather than a collection of
  conclusions.
unknown_points:
- Which route is the shortest and most effective may change as data benches are developed
  in the future.
- The final conditions for V and D still have many unresolved issues.
wiki_links:
- label: 'Wiki: Basics of WBE'
  url: /wiki/mind-upload-basics.html
  description: This is for people who want to see the overall picture of why this
    map is needed.
- label: 'Wiki: Basics of verification infrastructure'
  url: /wiki/verification-basics.html
  description: Complement what you want to fix in the V series.
- label: Wiki Home
  url: /wiki/
  description: You can return to other basic pages.
recommended_pages:
- label: technology roadmap
  url: /tech_roadmap.html
- label: Introduction to WBE
  url: /wbe_101.html
- label: Verification platform
  url: /verification.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>First of all, in a nutshell</h2>
<p>
A technology roadmap is a map that shows what needs to be solved first before the future story will collapse. Although it may seem like a long list, it actually represents the dependency relationship of ``Assumption → Measurement → Estimation → Implementation → Verification → Social Implementation''.
</p>
</div>

<div class="note-box">
<strong>After deciding how to read, you also want to decide on the next page</strong>
<p>
If you want to see not only the meaning of the symbols on the roadmap, but also where to go in measurement, reconfiguration, implementation, verification, and social implementation after reading it, please see <a href="roadmap-next-routes.html">Five paths to follow after the roadmap</a>.
</p>
</div>

<section class="section" id="letters">
<h2 class="section-title">P/M/R/I/V/D in everyday language</h2>
<table class="data-table">
<thead>
<tr>
<th>Symbol</th>
<th>What question is it?</th>
<th>What will be the problem if this goes out</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>What we call success</td>
<td>The goal is not set, and the victory conditions can be changed later. </td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>What can be measured and with what precision</td>
<td>In the first place, I don't know what is in the input. </td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>What can we infer from observations</td>
<td>The measured signal is interpreted to have a stronger meaning than necessary. </td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>How to move the model</td>
<td>Even if it looks good on paper, it may not turn in reality. </td>
</tr>
<tr>
<td><strong>V</strong></td>
<td>What and how to check</td>
<td>I can't tell if I've moved forward or if it's just an appearance. </td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>How to be treated in society</td>
<td>Even if the technology works, it cannot be used due to rights and safety concerns. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="routes">
<h2 class="section-title">Reading order by interest</h2>
<table class="data-table">
<thead>
<tr>
<th>What I'm curious about now</th>
<th>Symbol to read first</th>
<th>Next symbol</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to know what I need to accomplish to move forward</td>
<td><strong>P</strong></td>
<td><strong>V</strong></td>
</tr>
<tr>
<td>I want to get into the limitations of EEG and fMRI</td>
<td><strong>M</strong></td>
<td><strong>R</strong></td>
</tr>
<tr>
<td>I want to know how the model works</td>
<td><strong>R</strong></td>
<td><strong>I</strong></td>
</tr>
<tr>
<td>I want to see the identity and social system</td>
<td><strong>V</strong></td>
<td><strong>D</strong></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="not-timeline">
<h2 class="section-title">This is a dependency, not a chronology</h2>
<p>
Even if the numbers are arranged in the order P → M → R → I → V → D, it does not mean that they will definitely go this far in this year. The important thing is that the later arguments are more vulnerable to the failures of the earlier layers. For example, if we proceed to a strong identity claim in V while M and R are ambiguous, input limitations and estimation uncertainties remain.
</p>
<div class="cta-box">
<h4>Next</h4>
<p>Please check the official issue list and index in the technology roadmap text. </p>
<a href="../tech_roadmap.html">Go to technology roadmap →</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE basics →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG preprocessing and QC →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../tech_roadmap.html">Technology roadmap →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
</ul>
</div>
</aside>
</main>