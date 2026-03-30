---
layout: default
title: "Contribution Guide"
description: "How to participate in the Mind-Upload project, read issue status, and distinguish executable changes from external dependencies."
article_type: Guide
subtitle: "Join the research workflow and read the issue tracker"
author: Mind Uploading Research Project
last_updated: "2026-03-30"
note: "Contribution + Issue tracker"
audience: "People who are joining for the first time, want to check the issue status, and want to start making viable contributions."
reading_time: "10-20 minutes"
page_intro: "This page explains how to participate in Mind-Upload, how to read issue status, and how to separate changes that can be made now from tasks that remain externally dependent."
accuracy_note: "Items listed here are not all implemented. This page separates proposals, documented designs, and external dependencies so they are not misread as completed work."
page_highlights:
  - "It highlights small but valuable ways to participate, such as improving writing, terminology, and link structure."
  - "It lets you track issue status without confusing document-level reflection with implemented artifacts."
  - "It prioritizes issues with clear achievement conditions and falsification conditions over vague strong claims."
known_points:
  - "Even small changes like improving the text, cleaning up terminology, and fixing links are important contributions to this site."
  - "Issue status labels are for reading the implementation status and publication status, and do not imply scientific confirmation."
  - "External dependent tasks should be treated separately from changes that can be made here and now."
unknown_points:
  - "Which proposal will go further into implementation or joint research in the future is not yet determined at the issue stage."
  - "This page alone cannot guarantee the completion time of externally dependent tasks or the agreement of the other party."
wiki_links:
  - label: "Wiki Home"
    url: "/wiki/"
    description: "This is an entry point for people who want to supplement their prerequisite knowledge in the field first."
  - label: "Wiki: Internal prework and external dependencies"
    url: "/wiki/internal-prework-and-external-dependencies.html"
    description: "Separates what can be done in this repository now from what becomes an external dependency."
  - label: "Wiki: WBE basics"
    url: "/wiki/mind-upload-basics.html"
    description: "A starting point if you want to understand the topic before contributing."
  - label: "Wiki: Verification basics"
    url: "/wiki/verification-basics.html"
    description: "Explains why achievement conditions and falsification conditions matter."
recommended_pages:
  - label: "Start Page"
    url: "/index.html"
  - label: "Verification"
    url: "/verification.html"
  - label: "Glossary"
    url: "/glossary.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<!-- Intro -->
<div class="abstract-box">
<h2>Welcome</h2>
<p>
Mind-Upload is an open community that advances mind uploading into verifiable research. Regardless of your field or experience, you can immediately participate in tasks that directly lead to improved reproducibility, such as improving sentences, organizing terminology, and pointing out misunderstandings.
</p>
</div>

<div class="key-points">
<h4>For first-time users</h4>
<ul>
<li><strong>When in doubt:</strong> <a href="index.html">Start</a> → <a href="verification.html">Verification</a> → <a href="tech_roadmap.html#definition">Defining progress</a></li>
<li><strong>If you are stuck on terminology:</strong> use the <a href="glossary.html">Glossary</a> and <a href="faq.html">FAQ</a>.</li>
<li><strong>A high-value first contribution:</strong> an issue that clearly states both achievement conditions and falsification conditions.</li>
</ul>
</div>

<div class="note-box">
<strong>Thoughts on participation</strong>
<p>
There is no need to start with a large implementation. Correcting ambiguous phrasing, checking term definitions, and pointing out broken links or missing evidence are all meaningful contributions here. This site values the accumulation of small corrections that improve reproducibility.
</p>
</div>
<div class="note-box">
<strong>When you are unsure whether to learn first or participate</strong>
<p>
If you want to sort the site into the three modes of getting the overview, learning from the beginning, and actually fixing or contributing, see <a href="wiki/site-usage-modes.html">Wiki: Three ways to use this site</a>.
</p>
</div>

<div class="note-box">
<strong>When you feel that the prerequisite knowledge is insufficient</strong>
<p>
It is safer to first understand the basics of WBE and verification infrastructure on <a href="wiki/">wiki</a> than to force yourself to start writing issues. Once you have your terminology assumptions in place, you can more accurately report where you stopped.
</p>
</div>
<div class="note-box">
<strong>When you want to see how to write an issue from the beginning</strong>
<p>
If you want to see how to turn "I do not know" into a useful issue, and how to set achievement conditions plus falsification conditions, see <a href="wiki/issue-writing-basics.html">Wiki: How to write your first issue</a>.
</p>
</div>
<div class="note-box">
<strong>If you are here specifically for RQ-by-RQ grant planning</strong>
<p>
This page separates contribution routes and issue work. If what you really want is the current one-question-at-a-time route from a mind-upload research question to a fundable theme and a fixed EEG dataset anchor, use the <a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">grant and dataset playbook</a>, the <a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ-by-RQ deep dossiers</a>, the <a href="wiki/mind-upload-current-public-six-rq-brief.html">current public six-RQ brief</a>, and the <a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">current funding shortlist</a>.
</p>
</div>
<div class="note-box">
<strong>If you want the current six research questions being turned into EEG-ready work packages</strong>
<p>
The active public deepening batch is <code>U13-2</code>, <code>U13-5</code>, <code>U14-4</code>, <code>U0-2</code>, <code>U0-3</code>, and <code>U14-2</code>. These are not solved questions. They are the current bounded work packages where one claim, one dataset anchor, one KPI bundle, and one explicit external-dependency boundary are being fixed first. As of March 30, 2026, this batch remains intentionally narrower: it concentrates on <code>inner-speech decoding + identity drift + reproducibility auditing</code> with the conservative anchor set <code>D10/D03/D01/D02</code>, because that is the cleanest current bridge from mind-upload research questions to EEG-ready and fundable work packages. This is a route-setting update, not a solved-claim update. After the March 30, 2026 02:05 JST live-site, official-window, and Todoist recheck, this public batch still stays unchanged while the row-level wiki anchors were synced more explicitly to <code>Dxx + DOI + dataset name + access class</code>. A further March 30, 2026 05:07 JST anchor-strength recheck keeps the same route but tightens the reading: <code>D10</code> and <code>D02</code> remain the stronger primary anchors for first artifacts, while <code>D03</code> and <code>D01</code> stay useful only as bounded support anchors until a richer speech-side or benchmark-style adjunct is added. The current execution order is fixed more explicitly as <code>U13-2 → U13-5 → U0-2 → U0-3 → U14-4 → U14-2</code>, so the route can remain narrow while minimum artifacts are closed one by one. What currently counts as public-facing progress is still artifact-level and narrow: a <code>brain-minus-prior</code> control table for <code>U13-2</code>, a perception-to-recall branch note for <code>U13-5</code>, an <code>offset/jitter + state-feature collapse</code> audit for <code>U0-2</code>, a threshold-stability and overfit-exclusion rule for <code>U0-3</code>, filled Card examples for <code>U14-4</code>, and a fixed-split rerun contract for <code>U14-2</code>. These are benchmark and disclosure milestones, not solved-claim milestones. <code>Kura Fund</code> and the <code>Nakatani Foundation graduate scholarship</code> remain the near-term bridge, the <code>Kashinome Scholarship</code> stays only as a student-runway side route, the <code>Secom General Research Grant</code> stays only as an urgency watch route, and the broader neuroscience grant routes stay in watch mode. Larger social-deployment programs remain outside this current EEG-first route. The row-level public brief now spells out, for each of the six, what EEG can honestly close now, what still needs outside support, and what submission wording stays public-safe. Dedicated row packets now cover <code>U13-2</code>, <code>U13-5</code>, and <code>U0-2</code>, so readers can inspect the anchor-choice rationale without widening the public claim surface. For a compact row-by-row version of the same six-question route, see the <a href="wiki/mind-upload-current-public-six-rq-brief.html">current public six route brief</a>. For the exact <code>Dxx + DOI</code> anchors, first-pass KPIs, and the external dependencies kept outside the EEG claim, start with the <a href="wiki/mind-upload-rq60-deep-focus-notes.html">deep focus notes</a>, the <a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">grant and dataset playbook</a>, and the <a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">current funding shortlist</a>.
</p>
</div>
<div class="note-box">
<strong>When you understand but are unsure whether to start working on it</strong>
<p>
If you want a step-by-step guide to the difference between understanding the topic, checking the source and conditions, and being ready to make a change, see <a href="wiki/understanding-vs-action-readiness.html">Wiki: The difference between understanding and being ready to act</a>.
</p>
</div>
<div class="note-box">
<strong>When you are confused between the roles of research notes, proposals, and issues</strong>
<p>
This page is an entry point for tasks that can be handled here and now, so its role is different from theory notes and proposal-organizing tables. If you want the difference between facts, hypotheses, proposals, and implementation tasks on one page, see <a href="wiki/facts-hypotheses-proposals-and-tasks.html">Wiki: Facts, hypotheses, proposals, and execution tasks</a>.
</p>
</div>
<div class="note-box">
<strong>When you get stuck in isolating external dependencies</strong>
<p>
Even when IRB, experiments, equipment, and legal matters are involved, the required specifications, decision conditions, and public log formats can still be prepared in-house first. See <a href="wiki/internal-prework-and-external-dependencies.html">Wiki: Internal prework and external dependencies</a> for the separation rule used in this repository.
</p>
</div>
<div class="note-box">
<strong>When you want to see the flow of posting to an issue after reading a document</strong>
<p>
After reading papers or literature maps, if you want to see which open problem to return to and under what conditions to raise it as an issue, see <a href="wiki/literature-to-action-route.html">Wiki: Straight path from literature to implementation and participation</a>.
</p>
</div>
<div class="note-box">
<strong>When you want to decide the next page after this page</strong>
<p>
If you want to participate but are unsure whether to make a small fix, move to condition design, or decompose external dependencies, see <a href="wiki/participation-next-routes.html">Wiki: Five routes after the participation / collaboration page</a>.
</p>
</div>
<div class="note-box">
<strong>When you are unsure which artifact to return what you have read</strong>
<p>
If you want the overall flow for turning what you read into literature organization, theory updates, proposals, issues, or external-dependency tasks, see <a href="wiki/reading-to-change-workflow.html">Wiki: Connecting reading to change</a>.
</p>
</div>

<section class="section" id="first-contribution-guide">
<h2 class="section-title">Quick guide for deciding your first step</h2>
<table class="data-table">
<thead>
<tr>
<th>At times like this</th>
<th>What to do first</th>
<th>Next page</th>
</tr>
</thead>
<tbody>
<tr>
<td>The text is difficult, but I can point to where I got stuck</td>
<td>Write in the issue which page, paragraph, or term blocked you.</td>
<td><a href="glossary.html">Glossary</a> / <a href="faq.html">FAQ</a></td>
</tr>
<tr>
<td>There is a claim, but I cannot see the success or falsification conditions</td>
<td>Point out both what would count as progress and what would count as failure.</td>
<td><a href="verification.html">Verification</a> / <a href="tech_roadmap.html">Roadmap</a></td>
</tr>
<tr>
<td>I found a new paper/article/data</td>
<td>Before summarizing the content, decide where it should be integrated into the existing pages.</td>
<td><a href="research_harvest_50.html">Research Harvest</a> / <a href="datasets.html">Datasets</a></td>
</tr>
<tr>
<td>There are typos, broken links, or small wording fixes that can be made immediately</td>
<td>Submit the correction as a Pull Request and, if needed, add one sentence clarifying the page's role.</td>
<td><a href="content_hub.html">Content Hub</a></td>
</tr>
<tr>
<td>I want to pursue work that requires experiments, IRB, equipment, or legal review</td>
<td>Separate the preparatory work that can be done now from the genuinely external dependencies.</td>
<td><a href="issue.html#external-collaboration">External dependency/collaboration clause</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-label-guide">
<h2 class="section-title">How to read state labels</h2>
<table class="data-table">
<thead>
<tr>
<th>Label</th>
<th>In everyday language</th>
<th>Still things to check</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reflected (document)</td>
<td>This status is reflected in the site's text.</td>
<td>It does not guarantee that all code, public data, and evaluation logs are available.</td>
</tr>
<tr>
<td>Proposed</td>
<td>The design for the change exists in text.</td>
<td>Implementation or third-party verification may still be missing.</td>
</tr>
<tr>
<td>Proposal acceptance (document)</td>
<td>The suggestion has been accepted and incorporated into the text.</td>
<td>Artifacts that satisfy reproducibility standards are still required separately.</td>
</tr>
<tr>
<td>Proposal under review</td>
<td>This is currently treated as a strong idea, but not a settled one.</td>
<td>The content may still change after rebuttals, alternatives, or feasibility checks.</td>
</tr>
<tr>
<td>Reflection of implementation policy (document) / Implementation planning (document)</td>
<td>The implementation direction and steps are organized in text.</td>
<td>Publishing working code and verification results remains a separate task.</td>
</tr>
<tr>
<td>Design completed (implementation code not released)</td>
<td>The idea is stable, but there is still no external retest path.</td>
<td>L0 reproducibility still requires code, data, and procedures to be public.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="good-issue-minimum">
<h2 class="section-title">Minimum requirements for high-value issues</h2>
<table class="data-table">
<thead>
<tr>
<th>Item</th>
<th>What should be included even in a short issue</th>
<th>Why it matters</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Where did it stop</strong></td>
<td>The exact location where the reader got stuck, such as the page, section, paragraph, or term.</td>
<td>This makes the repair target concrete instead of leaving only a vague "hard to understand" complaint.</td>
</tr>
<tr>
<td><strong>What's missing</strong></td>
<td>What kind of gap it is: insufficient definition, insufficient evidence, unclear conditions, or missing status labels.</td>
<td>Knowing the gap type makes it easier to distinguish between a text addition and a structural correction.</td>
</tr>
<tr>
<td><strong>Achievement conditions</strong></td>
<td>State in one sentence what would need to be added or changed for the issue to count as improved.</td>
<td>This reduces open-ended issues and makes it easier to decide when a fix is complete.</td>
</tr>
<tr>
<td><strong>Falsification conditions</strong></td>
<td>State what finding or condition would make you reject the claim or proposal.</td>
<td>On this site, stronger proposals require clearer conditions for deciding that they are wrong.</td>
</tr>
<tr>
<td><strong>External dependency or not</strong></td>
<td>Distinguish whether it can be fixed in-repo now or whether it requires IRB, experiments, equipment, or outside agreement.</td>
<td>This prevents immediately executable changes from being mixed with tasks that need a separate track.</td>
</tr>
</tbody>
</table>
</section>

<!-- Contribution Methods -->
<section class="section">
<h2 class="section-title">How to Contribute</h2>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Create an issue (Discussion)</h4>
<p>Suggest a new idea, report a bug, or discuss theory all in GitHub Issues. </p>
<div class="tag-list">
<span class="tag">Bug Report</span>
<span class="tag">Feature Request</span>
<span class="tag">Question</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Send a Pull Request (Implementation)</h4>
<p>Code fixes and documentation improvements are accepted through Pull Requests. Please fork, create a branch, and suggest changes. </p>
</div>
</div>
</div>

<div class="cta-box">
<h4>Start Contributing</h4>
<p>Join the discussion by creating a GitHub Issue. </p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">Open an Issue</a>
</div>
</section>

<!-- Resolved Issues -->
<section class="section">
<h2 class="section-title">Resolved Milestones</h2>
<p>Major issues solved with community contributions. </p>

<div class="key-points">
<h4>Design completed (implementation code not released)</h4>
<ul>
<li><strong>Issue #10:</strong> Three-axis benchmark for discriminant criteria (unpredictability, self-updating, and causal responsiveness) between MU and LLM simulations — <em>Design documentation is complete. Reproducible implementation code, test data, and evaluation results have not been published. </em></li>
<li><strong>Issue #12:</strong> Hybrid measurement protocol including glial and metabolic indicators for Boundary Problems — <em>Conceptual design completed. Protocol details, required equipment list, and pilot data are not yet available. </em></li>
<li><strong>Issue #34:</strong> JSON log output function for M8 quality control (QC) metrics — <em>Schema design complete. Implementation code has not been reflected in the repository. </em></li>
<li><strong>Issue #43:</strong> R2 Empirical Bayes Source Estimation and Uncertainty Quantification (Confidence Intervals) — <em>Theoretical framework is documented. The implementation code of <code>02_source_imaging.py</code> has not been released. </em></li>
</ul>
</div>
<div class="note-box">
<strong>Transparency Note</strong>
<p>
Although the issue above has been addressed at the document level on the site, it has not yet been published in a form (executable code, test data, evaluation results) that can be reproduced and verified by a third party. In order to meet the reproducibility standards (L0: reproducibility by third parties) set forth by this project, it is necessary to publish these implementations.
</p>
</div>
</section>

<section class="section" id="technical-issue-tracker">
<h2 class="section-title">Technical Issue Tracker (integrated text)</h2>
<p>
Below is the response status for the technical proposal issues. The rationale for each status links directly to the integrated proposal summary section in the research note.
</p>

<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>Compatible content (summary)</th>
<th>Status</th>
<th>Reason link</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#46</strong></td>
<td>Organize measurement QA, synchronization correction, artifact removal, and BIDS/Motion-BIDS integration policy</td>
<td>Proposed</td>
<td><a href="perspective.html#proposal-46">#46 Summary in Perspective</a></td>
</tr>
<tr>
<td><strong>#47</strong></td>
<td>Enhanced implementation policy for BIDS standardization, ASR/ZapLine, wPLI/STE, and LSL synchronization</td>
<td>Proposal acceptance (document)</td>
<td><a href="perspective.html#proposal-47">#47 Summary in Perspective</a></td>
</tr>
<tr>
<td><strong>#48</strong></td>
<td>OPM-MEG, transfer learning, Team Flow causality, IIT implementation extension proposal submitted</td>
<td>Proposal under review</td>
<td><a href="perspective.html#proposal-48">#48 Summary in Perspective</a></td>
</tr>
<tr>
<td><strong>#56</strong></td>
<td>Change to verification design that introduces PCI and do-calculus for counterfactual indistinguishability</td>
<td>Proposed</td>
<td><a href="perspective.html#proposal-56">#56 Summary in Perspective</a></td>
</tr>
<tr>
<td><strong>#58</strong></td>
<td>Clarified design policy for three issues: NESS dissipation, causal identifiability, and IIT approximate calculation</td>
<td>Proposed</td>
<td><a href="perspective.html#proposal-58">#58 Summary in Perspective</a></td>
</tr>
<tr>
<td><strong>#61</strong></td>
<td>Present unfolding issues, two-layer thermodynamic cost, SCM rigor, and corrections to multi-model inference</td>
<td>Implementation policy reflection (document)</td>
<td><a href="perspective.html#proposal-61">#61 Summary in Perspective</a></td>
</tr>
<tr>
<td><strong>#62</strong></td>
<td>Additional reinforcement of equivalence class warning and IIT approximation implementation plan in response to #58 criticism</td>
<td>Implementation planning (document)</td>
<td><a href="perspective.html#proposal-62">#62 Summary in Perspective</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Operation rules</strong>
<p>
This tracker updates only from trails that can be confirmed within the site. External implementation work such as experiments, legal review, or equipment procurement is separated as an external dependency and is not claimed as completed here.
</p>
</div>
</section>

<section class="section" id="proposal-integration">
<h2 class="section-title">Integrated text of technical proposal</h2>
<p>
The main points of the old <code>proposals.md</code> have been integrated into this section. Here you can track proposal status, rationale, and implementation impact without separating them from the issue path.
</p>

<table class="data-table">
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Remaining confirmations</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Publish proposal</strong></td>
<td>Published as text and available for review.</td>
<td>Its validity and priority still need evaluation.</td>
</tr>
<tr>
<td><strong>Proposal accepted</strong></td>
<td>We have judged that it is worth incorporating as policy.</td>
<td>The implementation method, evaluation conditions, and publication form still need to be worked out.</td>
</tr>
<tr>
<td><strong>Reflect implementation policy</strong></td>
<td>The idea is reflected in the text and design.</td>
<td>Code, data, and evaluation results that can be retested are still required separately.</td>
</tr>
<tr>
<td><strong>External dependencies</strong></td>
<td>Conditions outside the repository are required, such as experiments, equipment, legal review, or partner agreement.</td>
<td>Inside this repository, the requirement specifications, decision conditions, and log format are prepared first.</td>
</tr>
</tbody>
</table>

<div class="note-box" id="stream-e-rigor">
<strong>Stream E: Position of stricter proposal</strong>
<p>
Issues #257 to #260 collectively tighten the handling of inverse-problem uncertainty, causal equivalence classes, thermodynamic consistency, and missing BIDS semantics. On the main-text side, the changes land in <a href="verification.html#verification-rigor-2026-02">additional verification requirements</a>, <a href="verification.html#thermodynamic-verification">thermodynamic verification requirements</a>, and the <a href="verification.html#causal-perturbation-suite">causal perturbation suite</a>. On the issue side, this section tracks the rationale for those changes and isolates the external dependencies.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Technology stream</th>
<th>Main focus</th>
<th>Places to visit in text</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Measurement/Synchronization/BIDS</strong></td>
<td>Fix QA, synchronization correction, and metadata standardization as a measurement trail.</td>
<td><a href="perspective.html#proposal-46">In Perspective #46</a> / <a href="perspective.html#proposal-47">#47</a></td>
</tr>
<tr>
<td><strong>Preprocessing/Connectivity</strong></td>
<td>Treat ASR, ZapLine, wPLI, STE, and related tools as comparable preprocessing and metric systems.</td>
<td><a href="perspective.html#proposal-47">In Perspective #47</a></td>
</tr>
<tr>
<td><strong>Intervention/Causation</strong></td>
<td>Because observation alone is not enough, this stream pushes PCI and intervention design toward the ground-truth side.</td>
<td><a href="perspective.html#proposal-56">In Perspective #56</a></td>
</tr>
<tr>
<td><strong>Thermodynamics/Identifiability</strong></td>
<td>Separate logical cost from dissipative cost while auditing causal identifiability at the same time.</td>
<td><a href="perspective.html#proposal-58">In Perspective #58</a> / <a href="perspective.html#proposal-61">#61</a> / <a href="perspective.html#proposal-62">#62</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="recent-issue-responses">
<h2 class="section-title">Compatible with latest issues (#257–#263)</h2>
<p>
The following table records how issues added in the latter half of February 2026 were handled. It explicitly separates "changes executed in this pass" from "items still pending as external dependencies."
</p>

<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>Request</th>
<th>Changes to be performed this time</th>
<th>Status</th>
<th>Reference</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#257</strong></td>
<td>Stricter inverse problem uncertainty, causal equivalence, and thermodynamic consistency</td>
<td>Added HBM uncertainty map, causal equivalence class, and NESS/EPR requirements to main text standards</td>
<td>Reflected (document)</td>
<td><a href="issue.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification#verification-rigor-2026-02</a></td>
</tr>
<tr>
<td><strong>#258</strong></td>
<td>Clarification of IIT computational complexity constraints and thermodynamic verification requirements</td>
<td>Added PCI-ST central operation and thermodynamics KPI (logical cost/dissipation cost separation)</td>
<td>Reflected (document)</td>
<td><a href="issue.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#thermodynamic-verification">verification#thermodynamic-verification</a></td>
</tr>
<tr>
<td><strong>#259</strong></td>
<td>Response to ASR side effects and lack of BIDS semantics</td>
<td>Added MI/PLV audit and CogPO/NIF/subjective reporting metadata requirements before and after ASR</td>
<td>Reflected (document)</td>
<td><a href="issue.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification#verification-rigor-2026-02</a></td>
</tr>
<tr>
<td><strong>#260</strong></td>
<td>Strengthening the integration of inverse problems, counterfactual hypotheticals, and thermodynamics</td>
<td>Bundle additions #257 to #259 as integration requirements and redefine verification conditions</td>
<td>Reflected (document)</td>
<td><a href="issue.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#causal-perturbation-suite">verification#causal-perturbation-suite</a></td>
</tr>
<tr>
<td><strong>#261</strong></td>
<td>Add external article URL content</td>
<td>Add to collected literature path and register reference URL to Evidence Bank</td>
<td>Reflected (document)</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
<tr>
<td><strong>#262</strong></td>
<td>Addition of ScienceDirect/arXiv URL content</td>
<td>Add 2 URLs to Evidence Bank new acceptance log</td>
<td>Reflected (document)</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
<tr>
<td><strong>#263</strong></td>
<td>Add arXiv URL content</td>
<td>Add arXiv document to acceptance log and clearly indicate confirmation status</td>
<td>Reflected (document)</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Hold due to external dependency</strong>
<ul>
<li><strong>Task:</strong> TMS/tDCS intervention experiment on human subjects <strong>Owner:</strong> experiment PI <strong>Prerequisites:</strong> IRB approval, equipment secured, participant recruitment <strong>Completion condition:</strong> publishable data and audit logs are obtained under a preregistered protocol</li>
</ul>
</div>
</section>

<section class="section" id="external-collaboration">
<h2 class="section-title">External dependence/collaboration candidates</h2>
<p>
The main points of the old <code>collaborations.md</code> have been integrated into this section. The important point here is not the candidate name itself, but the separation between what can be prepared in-house first and what genuinely requires outside consent.
</p>

<table class="data-table">
<thead>
<tr>
<th>Type</th>
<th>What you can do further within this repository</th>
<th>What remains externally dependent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standardization preparation</strong></td>
<td>Definition of draft specifications, comparison tables, log formats, and audit requirements</td>
<td>Community adoption, reflection in official specifications</td>
</tr>
<tr>
<td><strong>Preparation for data publication</strong></td>
<td>Development of BIDS conversion, QC logs, explanations, and reproduction steps</td>
<td>Rights confirmation and acceptance by the external repository</td>
</tr>
<tr>
<td><strong>Joint research preparation</strong></td>
<td>One-page summary, minimum deliverables, evaluation design, and publication prep</td>
<td>IRB, equipment, co-author agreement, experiment implementation</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>Priority candidate</th>
<th>Minimum scope</th>
<th>What you want to make in-house first</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDS / EEG-BIDS Community</strong></td>
<td>Discussion of EEG QC logs, synchronization logs, and Derivatives extensions</td>
<td>Extension specification draft, example metadata, difference table</td>
</tr>
<tr>
<td><strong>OpenNeuro</strong></td>
<td>Preparing one BIDS dataset for publication with DOI</td>
<td>BIDS converted samples, Validator results, README</td>
</tr>
<tr>
<td><strong>MOABB / NeuroTechX</strong></td>
<td>L0/L1 bench comparison possible</td>
<td>Task definition, baseline, and minimum deliverable specifications</td>
</tr>
<tr>
<td><strong>MNE-Python</strong></td>
<td>BIDS → Preprocessing → Metrics reproduction pipeline</td>
<td>The minimum notebook/script that can be turned into a tutorial</td>
</tr>
<tr>
<td><strong>LSL Community</strong></td>
<td>Standardization of synchronous audit log</td>
<td>Defining templates, tolerances, and failure logs</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>How to read this section</strong>
<p>
The candidates listed here do not mean that they have been agreed upon or committed to implementation. What we need to do now is to prepare the required specifications, minimum deliverables, and judgment conditions in a form that can be made public before sending them to the other party.
</p>
</div>
</section>

<!-- Verification Audit -->
<section class="section" id="verification-audit">
<h2 class="section-title">Verification Audit (180 verification audits)</h2>
<p>
These are the results of a systematic verification audit of all site content conducted in February 2026. We have registered 180 GitHub issues in 4 categories and are responding to them through site corrections.
</p>

<table class="data-table">
<thead>
<tr>
<th>Category</th>
<th>Issue range</th>
<th>Number of cases</th>
<th>Compatibility status</th>
<th>Main modifications</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>LIT (Literature Verification)</strong></td>
<td>#71–#110</td>
<td>40 items</td>
<td>Document corrected</td>
<td>DOI verification, removal of duplicate references (ref-68/69/72/75), addition of FlyWire 2024, clear unverified citations</td>
</tr>
<tr>
<td><strong>THEO (theoretical gap)</strong></td>
<td>#111–#145</td>
<td>35 items</td>
<td>Document corrected</td>
<td>Clearing the position of hard problems, responding to Unfolding Argument, recognizing FEP criticism, expressing philosophical premises</td>
</tr>
<tr>
<td><strong>IMPL (Implementation Gap)</strong></td>
<td>#146–#195</td>
<td>50 items</td>
<td>Document corrected</td>
<td>Transparency reporting of implementation status, clear indication of non-achievement of L0, evidence gap analysis, addition of Deployment section</td>
</tr>
<tr>
<td><strong>METH (methodology/latest research)</strong></td>
<td>#196–#250</td>
<td>55 items</td>
<td>Document corrected</td>
<td>Connectome progress updated, alternative approach comparison table, ethics FAQ added, glossary expanded (13 terms added)</td>
</tr>
</tbody>
</table>

<div class="key-points">
<h4>Major corrections (cross-site)</h4>
<ul>
<li><strong>perspective.md:</strong>Removed 4 duplicate references, added Limitations section, updated FlyWire connectome, added Chalmers 1995</li>
<li><strong>idea.md: Added </strong>Limitations and Open Questions section, added DOI link to Weber 2025, added 5 references</li>
<li><strong>verification.md:</strong> Added implementation status transparency report sheet, added scientific gap analysis section, added MOABB/FAIR reference</li>
<li><strong>glossary.md:</strong>Added the theory of consciousness section (8 terms such as IIT/GNWT/FEP/PCI/Markov blanket) and the implementation infrastructure section (5 terms)</li>
<li><strong>faq.md: </strong>Added 5 questions: hard problem, copy problem, Cogitate results, ethics, comparison with other projects</li>
<li><strong>wbe_101.md:</strong>Added philosophical premise comparison table and alternative approach comparison table</li>
<li><strong>proposals.md:</strong>Add evidence gap section (clarification of ASR/OPM-MEG/do-calculus/NESS issues)</li>
<li><strong>tech_roadmap.md:</strong>Fixed I8/I9 structure bug, added Deployment & Governance section (D0-D3)</li>
</ul>
</div>

<div class="note-box">
<strong>Transparency Note</strong>
<p>
All of the above modifications are "document level". Publication of executable code, test data, and evaluation results (achieving L0) is required separately, and this audit prioritized clarifying the discrepancies.
</p>
</div>
</section>

<!-- Technical Critique Response -->
<section class="section" id="technical-critique">
<h2 class="section-title">Technical Critique compatible (#64–#70)</h2>
<p>
This is a response to seven technical and scientific criticisms (Issues #64–#70) submitted in February 2026. Common themes are summarized and reflected in each file.
</p>

<table class="data-table">
<thead>
<tr>
<th>Theme</th>
<th>Corresponding Issue</th>
<th>Modification details</th>
<th>Reflection destination</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT 4.0 Complexity/Unfolding Argument</strong></td>
<td>#64, #65, #68, #69</td>
<td>Explanation of philosophical zombie risk, emphasis on the necessity of neuromorphism, introduction of hierarchical coarse-graining</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a></td>
</tr>
<tr>
<td><strong>Limits of EEG spatial resolution</strong></td>
<td>#64, #66, #67, #70</td>
<td>Explaining the limits of information theory (7-digit gap), redefining the practical role in WBE</td>
<td><a href="eeg_101.html#information-theoretic-limits">eeg_101</a></td>
</tr>
<tr>
<td><strong>Insufficiency of counterfactual virtual equivalence</strong></td>
<td>#65, #66, #69, #70</td>
<td>Addition of 3 indicators: EI, Causal Density, and STE, evaluation framework using Pearl's causal ladder</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a> / <a href="verification.html#verification-rigor">verification</a></td>
</tr>
<tr>
<td><strong>NESS Thermodynamic Grounding</strong></td>
<td>#68</td>
<td>EPR requirements beyond Landauer limits, combined with Fisher Information</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a></td>
</tr>
<tr>
<td><strong>Limitations of DCM/Bayesian method</strong></td>
<td>#64, #65, #67, #70</td>
<td>Introduction of BMR, Causal Fingerprinting, and adaptive preprocessing (Riemannian Potato)</td>
<td><a href="issue.html#proposal-integration">proposals</a></td>
</tr>
<tr>
<td><strong>ESI uncertainty quantification</strong></td>
<td>#67, #69, #70</td>
<td>Mandatory confidence interval, adaptive ASR/ZapLine-plus, forward problem error propagation</td>
<td><a href="eeg_101.html#esi-uncertainty">eeg_101</a> / <a href="verification.html#verification-rigor">verification</a></td>
</tr>
</tbody>
</table>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Resources</h4>
<ul>
<li><a href="https://github.com/yasufumi-nakata/mind-upload" target="_blank">GitHub Repository →</a></li>
<li><a href="perspective.html#design-principles">Theoretical Framework →</a></li>
<li><a href="tech_roadmap.html">Technical Roadmap →</a></li>
</ul>
</div>

<div class="note-box">
<strong>Code of Conduct</strong>
<p>
Please treat each other with respect so that all participants feel comfortable discussing. Scientific criticism is welcome, but offensive language and behavior will not be tolerated.
</p>
</div>

</aside>
</main>
