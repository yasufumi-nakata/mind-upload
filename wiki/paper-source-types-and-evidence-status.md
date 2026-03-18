---
layout: default
title: "Wiki: How to read source types, status labels, and evidence classes"
description: "Sort out what Scopus, arXiv, Review, Media, source_logged, curated, and evidence classes each mean and what they do not mean."
article_type: Wiki
subtitle: "Auxiliary page to avoid confusing badge, source, status, and what a paper directly strengthens"
author: Mind Uploading Research Project
last_updated: "2026-03-18"
note: "Reading guide"
audience: "People who don't want to misread labels on collections of papers or bibliographic maps, and people who want to know where to go back to the original text."
reading_time: "8-12 minutes"
page_intro: "This page is an auxiliary page that organizes labels such as ``Scopus,'' ``arXiv,'' ``Review,'' ``Media,'' ``source_logged,'' ``curated,'' and evidence classes that appear in collections and bibliographic maps for beginners. The important thing here is to read these labels separately and understand what information each one represents."
accuracy_note: "Labels are a reading aid and do not automatically guarantee the correctness of the article content. When using them as evidence, always refer back to the DOI, main text, and primary research."
page_highlights:
  - "We explain publication source, document type, site status, and evidence class as separate axes."
  - "We show how to separate source labels from the question of what a paper directly strengthens."
  - "You can use the table to see where to stop and return to the original text."
  - "Human measurement papers are kept separate as observability-class advances rather than being folded into demo or hidden-state bins."
known_points:
  - "Even for the same document, publication source, document type, site status, and evidence class must be viewed separately."
  - "Scopus is an index, arXiv is a preprint storage, and Review is a document type, and they do not have the same meaning."
  - "source_logged and curated are labels that indicate how organized this site is."
  - "A human PET/MRS/MRI paper can strengthen observability without closing hidden state or proving causal sufficiency."
unknown_points:
  - "The extent to which individual papers ultimately remain central evidence will depend on subsequent scrutiny."
  - "Top stories traced from reviews and news may weaken when returned to primary research."
wiki_links:
  - label: "Wiki: How to read the literature and evidence page"
    url: "/wiki/literature-and-evidence-reading.html"
    description: "First, we will clarify the differences in the roles of collections of papers, bibliographic maps, and proposal pages."
  - label: "Wiki: How to read claims and evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "It helps you understand how to read the 'strength of claim' on the label."
  - label: "Wiki: U number guide"
    url: "/wiki/u-number-guide.html"
    description: "This is an auxiliary page to see which open questions are related to the bibliographic map."
recommended_pages:
  - label: "Collection of papers"
    url: "/mind_uploading_papers.html"
  - label: "Literature map"
    url: "/research_harvest_50.html"
  - label: "Casework"
    url: "/verification.html#casework"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>First divide into four parts</h2>
<p>
What can be confusing on literature pages is that <strong>where</strong> a paper is listed, <strong>what type of literature</strong> it is, <strong>its current status on this site</strong>, and <strong>what it directly strengthens</strong> can all appear to be the same thing. By separating these four things first, you can significantly reduce misreadings.
</p>
</div>

<section class="section" id="three-axes">
<h2 class="section-title">Labels have four axes</h2>
<table class="data-table">
<thead>
<tr>
<th>axis</th>
<th>What does it represent</th>
<th>Example</th>
<th>That's not all I can say</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Publisher/Badge</strong></td>
<td>It's about where you can trace the document and which entrance you picked it up from. </td>
<td>Scopus / arXiv / Academic journal page / DOI</td>
<td>It is not determined that the content is strong, correct, or central. </td>
</tr>
<tr>
<td><strong>Document type</strong></td>
<td>Whether the document is primary research, a review, or news. </td>
<td>Primary / Review / Media</td>
<td>It is necessary to separately confirm whether there is new data or whether it is strong enough to be used directly for verification. </td>
</tr>
<tr>
<td><strong>Site status</strong></td>
<td>Indicates whether input has been accepted, organized, or excluded on this site. </td>
<td>source_logged / curated / noise_excluded</td>
<td>It does not necessarily mean that the content of the paper is true or of low value. </td>
</tr>
<tr>
<td><strong>Evidence class</strong></td>
<td>Indicates what the paper directly strengthens in the technical reading flow. </td>
<td>Direct validator / system demo / observability-class advance / benchmark / hidden-state boundary</td>
<td>It is still not a claim that the whole problem is solved. It only fixes <strong>which evidential axis moved</strong>.</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>Multiple attributes overlap in the same document</strong>
<p>
For example, a document may be a <strong>review article on Scopus</strong>, a <strong>preprint of primary research on arXiv</strong>, or a <strong>curated human-MRI paper that belongs to the observability-class-advance bin</strong>. Do not rely on only one label.
</p>
</div>

<section class="section" id="source-kinds">
<h2 class="section-title">How to read publication source and type</h2>
<table class="data-table">
<thead>
<tr>
<th>Display</th>
<th>In everyday language</th>
<th>Useful points</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scopus</strong></td>
<td>These are documents found via the academic literature index database. </td>
<td>It is easy to organize bibliographic information and becomes an entry point for picking up a wide range of academic literature. </td>
<td>Scopus is an index and does not automatically guarantee the strength of peer review or the degree of direct connection to the issue. </td>
</tr>
<tr>
<td><strong>arXiv</strong></td>
<td>This is a public storage area for preprints. </td>
<td>You can find new research quickly. </td>
<td>Many papers have not yet been peer-reviewed at the time of submission, so you need to confirm the methods and limitations yourself. </td>
</tr>
<tr>
<td><strong>Review</strong></td>
<td>This is a review article that summarizes multiple studies. </td>
<td>It is suitable for grasping the map of the entire field and the main points of discussion. </td>
<td>Since our own new experiments are not always the main character, we return to primary research when using it as strong evidence. </td>
</tr>
<tr>
<td><strong>Media</strong></td>
<td>News articles, explanatory articles, and general introductions. </td>
<td>It can be used as an entry point to a topic or as a clue for searching for primary literature. </td>
<td>It is weak as an academic basis as it is, and it is necessary to trace it back to the original paper or presentation. </td>
</tr>
<tr>
<td><strong>Primary</strong></td>
<td>Primary research that directly produces new data, experiments, and analyses. </td>
<td>The evidence can be traced most directly by reviewing the method, evaluation, and limitations. </td>
<td>Even primary research can have weak sample conditions, statistics, and reproducibility, so it cannot be used unconditionally. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="evidence-class">
<h2 class="section-title">How to read evidence class</h2>
<table class="data-table">
<thead>
<tr>
<th>Evidence class</th>
<th>What it directly strengthens</th>
<th>Typical examples</th>
<th>What it still does not justify</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>direct validator / causal calibration</strong></td>
<td>Error sources, calibration limits, and local ground-truth checks.</td>
<td>Mikulan (2020), Unnwongse (2023), Hao (2025)</td>
<td>Whole-brain uniqueness recovery or full hidden-state closure.</td>
</tr>
<tr>
<td><strong>task-limited system demonstration</strong></td>
<td>Decode or closed-loop performance on a specific task and interface.</td>
<td>Tang (2023), Willett (2023), Littlejohn (2025), Wairagkar (2025)</td>
<td>Whole-brain emulation, identity continuity, or hidden-state completeness.</td>
</tr>
<tr>
<td><strong>dataset / benchmark / standard / toolchain</strong></td>
<td>Comparability, synchronization, governance, and reproducibility.</td>
<td>EEG-BIDS, Motion-BIDS, LSL, MOABB</td>
<td>Biological sufficiency or mechanistic truth.</td>
</tr>
<tr>
<td><strong>observability-class advance / human proxy ladder</strong></td>
<td>What humans can directly observe or approximate at a specific measurement class.</td>
<td>Shapson-Coe (2024), Johansen (2024), Lucchetti (2025), Baadsvik (2024), Rzechorzek (2022), Hirschler (2025)</td>
<td>State-complete measurement. Each proxy or atlas still has a claim ceiling.</td>
</tr>
<tr>
<td><strong>mechanistic boundary / hidden-state evidence</strong></td>
<td>What still remains latent or omitted even after connectome, cell type, or a strong demo.</td>
<td>Gouwens (2021), Hengen (2016), Xu (2024), Looser (2024), Cahill (2024)</td>
<td>Direct validation or a finished implementation.</td>
</tr>
<tr>
<td><strong>review / synthesis</strong></td>
<td>Field map, terminology, and issue clustering.</td>
<td>Review articles and benchmark syntheses</td>
<td>Strong conclusions without returning to primary research.</td>
</tr>
<tr>
<td><strong>context / philosophy / law / culture</strong></td>
<td>Context around the topic and its surrounding debates.</td>
<td>Ethics, legal analysis, metaphysics, cultural studies</td>
<td>The technical or natural-science frontier by itself.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-labels">
<h2 class="section-title">How to read site status labels</h2>
<table class="data-table">
<thead>
<tr>
<th>Label</th>
<th>In everyday language</th>
<th>What you need next</th>
<th>Easy to misread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>source_logged</strong></td>
<td>This is the stage where we accept URLs and DOIs as entry points and include them in our tracking targets. </td>
<td>Relevance confirmation, primary literature tracking, U number assignment, and abstract scrutiny are required. </td>
<td>It does not mean "recruitment confirmed" or "high quality confirmed". </td>
</tr>
<tr>
<td><strong>curated</strong></td>
<td>This site has been organized and arranged according to the points of discussion. </td>
<td>It will continue to be necessary to eliminate duplicates, replace with strong evidence, and track updates. </td>
<td>It is not a label that guarantees that the content is true. </td>
</tr>
<tr>
<td><strong>noise_excluded</strong></td>
<td>We are at the stage where we have determined that the relationship is weak, the contamination is large, and we will not use it at this time. </td>
<td>It is important to leave the reason for exclusion and prevent contamination of the same species. </td>
<td>This does not mean that the paper itself has no value, but it may be out of sync with the main points of this site. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="when-to-return">
<h2 class="section-title">Where to stop and return to the original text</h2>
<table class="data-table">
<thead>
<tr>
<th>Current purpose</th>
<th>You can stop here</th>
<th>Return to original text</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to pick up a wide range of topics</td>
<td>Once you know whether you are interested by Badge, summary, or 5-point arrangement. </td>
<td>When you want to support a strong argument by citing the paper. </td>
</tr>
<tr>
<td>Looking at source_logged items</td>
<td>When you understand that you are still at the entrance stage. </td>
<td>When you want to judge whether you can pursue primary research or whether it will be included in the U number. </td>
</tr>
<tr>
<td>Looking at Reviews and Media</td>
<td>When you have a map of the issues and related keywords. </td>
<td>When you want to use evaluations, methods, and numerical values as evidence. </td>
</tr>
<tr>
<td>Comparing documents from Scopus and arXiv</td>
<td>When you can figure out which entrance it was picked up from. </td>
<td>When you want to check the peer review status, experimental conditions, limitations, and possibility of follow-up testing. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">Common misreadings</h2>
<div class="key-points">
<h4>Misread</h4>
<ul>
<li><strong>“Scopus is strong”:</strong> Scopus is an index. Check the text and method to see how it applies to the issue. </li>
<li><strong>“It's all weak because it's arXiv”:</strong> There are important entry points even before peer review. Check the content to see if it's weak or not. </li>
<li><strong>“Review is enough”:</strong> Review articles are useful as maps, but for direct evidence you need to go back to primary research. </li>
<li><strong>“Source_logged, so accepted”:</strong> This is still an acceptance log, and the decision to integrate or exclude is a follow-up work. </li>
<li><strong>“curated so it is true”:</strong> Being organized and ultimately correct are two different things. </li>
<li><strong>“A human proxy paper solved hidden state”:</strong> A human PET/MRS/MRI advance often raises an observability class, not a full state-complete readout.</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">Where to return next</h2>
<p>
If you want to have a broad view of the papers, go back to <a href="../mind_uploading_papers.html">Collection of Papers</a>, if you want to see how they correspond to unresolved issues, go to <a href="../research_harvest_50.html">Literature Map</a>, and if you want to organize them based on the differences in their roles, go back to <a href="literature-and-evidence-reading.html">How to read the literature and evidence page</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="literature-and-evidence-reading.html">How to read the literature and evidence page →</a></li>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
<li><a href="u-number-guide.html">U number guide →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../mind_uploading_papers.html">Collection of papers →</a></li>
<li><a href="../research_harvest_50.html">Bibliography map →</a></li>
<li><a href="../verification.html#casework">Casework →</a></li>
</ul>
</div>
</aside>
</main>
