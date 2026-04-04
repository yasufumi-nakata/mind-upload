---
layout: default
title: "Contribution Guide"
description: "How to participate in the Mind-Upload project, read issue status, and distinguish executable changes from external dependencies."
article_type: Guide
subtitle: "Join the research workflow and read the issue tracker"
author: Mind Uploading Research Project
last_updated: "2026-04-04"
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
This page separates contribution routes and issue work. If what you really want is the current one-question-at-a-time route from a mind-upload research question to a fundable theme and a fixed EEG dataset anchor, start with the <a href="wiki/mind-upload-rq-solvability-bridge.html">RQ solvability bridge</a>, then use the <a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">grant and dataset playbook</a>, the <a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ-by-RQ deep dossiers</a>, the <a href="wiki/mind-upload-current-public-six-rq-brief.html">current public six-RQ brief</a>, and the <a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">current funding shortlist</a>.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 4, 2026 (12:02 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-04 12:02 JST</code> after <code>mind-upload@f84f6e53753b8d8d9082f27d1bbe307e606bd3c2</code>, <code>EEG-DATA@017ae806c4dd30719223fc20470ef3ccd676ee29</code>, and <code>auto-research-funds@d4024a5b8a1aa7bdef83abe82eeacfc9c5a0d720</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> synchronizes the EEG recording-frame contract across public pages without widening the route, <code>EEG-DATA</code> deep-dives capacity-for-movement EEG datasets while still keeping <code>30,929</code> merged-unique rows, <code>28,892</code> high-confidence rows, <code>24,908</code> immediate rows, and <code>24,538</code> high-confidence immediate rows, and <code>auto-research-funds</code> still just carries the earlier <code>11:04 JST</code> funding addendum without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Sat, 04 Apr 2026 02:19:09 GMT</code>; the checked bodies already surfaced <code>2026-04-04 11:04 JST</code> wording on <code>issue / brief / bridge / playbook</code>, while the checked <code>U13-2</code> row packet still surfaced <code>2026-04-04 09:05 JST</code> before this source sync. Because the newest repository progress remains route-conservative but the first-row packet lagged behind the front door, this run only carries a bounded <code>12:02 JST</code> source sync across the front door, playbook, and <code>U13-2</code> row packet while leaving the queue unchanged. The practical funding bridge still stays narrow: <code>Kura Fund</code> remains open through <code>2026-04-17 17:00 JST</code>, the <code>Nakatani Foundation graduate scholarship</code> remains open through <code>2026-05-25 15:00 JST</code>, the <code>Kashinome Scholarship</code> still stays a <code>2026-04-09</code> must-arrive side route, the <code>Nakatani Foundation research grant</code> remains next-cycle watch, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit also still stays sufficient (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>Doumei=0</code>; <code>Kenkyu no Susume=0</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 4, 2026 (11:04 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-04 11:04 JST</code> after <code>mind-upload@812e1650bae1c3da50df7355cc73bb4510f33464</code>, <code>EEG-DATA@1deac45c75a2d0a2f0d21a9ce5e52df1ff9bb3c5</code>, and <code>auto-research-funds@9741ee45a02597d2253e58bbf0ea083b56fe9553</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> tightens glossary bridge-witness terminology without widening the route, <code>EEG-DATA</code> collapses duplicate EEG-fMRI override rows and now keeps <code>30,929</code> merged-unique rows, <code>28,892</code> high-confidence rows, <code>24,908</code> immediate rows, and <code>24,538</code> high-confidence immediate rows while leaving the current <code>D10 / D03 / D02 / D01</code> family unchanged, and <code>auto-research-funds</code> adds legacy coverage for current-cycle funding cards without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live front-door pages plus <code>U13-2</code> row packet again returned <code>HTTP/2 200</code> with <code>Last-Modified: Sat, 04 Apr 2026 01:14:45 GMT</code>; their checked bodies still surfaced <code>2026-04-04 09:05 JST</code> wording before this source sync. Because the newest repository progress is public-safe but still route-conservative, this run adds only a bounded <code>11:04 JST</code> source sync to the front-door route pages and playbook while leaving the row packets unchanged. Official spot checks still keep <code>Kura Fund</code> open through <code>2026-04-17 17:00 JST</code>, the <code>Nakatani Foundation graduate scholarship</code> open through <code>2026-05-25 15:00 JST</code>, the <code>Kashinome Scholarship</code> at <code>2026-04-09</code> must-arrive, the <code>Nakatani Foundation research grant</code> in next-cycle watch, and the <code>Secom General Research Grant</code> closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit also still stays sufficient (<code>items=206</code>; <code>projects=2</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 4, 2026 (09:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-04 09:05 JST</code> after <code>mind-upload@e571567f017d0b544317f900a21a966f1427c9c8</code>, <code>EEG-DATA@fbbb0d8c01e0aadfce6a2789ab262f73037cf521</code>, and <code>auto-research-funds@d7f6fb9bc158742be3a6adc2540a382d066de07f</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> now just carries the earlier <code>08:07 JST</code> route-hold sync on top of a recent pretraining-overlap audit, <code>EEG-DATA</code> still keeps <code>30,929</code> merged-unique rows, <code>28,892</code> high-confidence rows, <code>24,909</code> immediate rows, and <code>24,539</code> high-confidence immediate rows while treating <code>OpenNeuro ds007020</code> as a limited rest-side support note and keeping <code>HeartBEAM</code> plus figshare <code>EEG at rest and with TMS</code> only as backup families, and <code>auto-research-funds</code> adds deeply reviewed April 4 scholarship updates while still keeping <code>JGC-S</code> only as an adjacent runway. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live front-door pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 23:18:55 GMT</code>, and their route-facing bodies already surfaced the earlier <code>2026-04-04 08:07 JST</code> hold note before this source sync. The current-six row packets also returned <code>HTTP/2 200</code> with <code>Last-Modified: Sat, 04 Apr 2026 00:11:41 GMT</code>, but they still surfaced <code>2026-04-04 01:04 JST</code> wording before this row-packet sync. Official spot checks still keep <code>Kura Fund</code> open through <code>2026-04-17 17:00 JST</code>, the <code>Nakatani Foundation graduate scholarship</code> open through <code>2026-05-25 15:00 JST</code>, the <code>Kashinome Scholarship</code> at <code>2026-04-09</code> must-arrive, the <code>Nakatani Foundation research grant</code> in next-cycle watch, and the <code>Secom General Research Grant</code> closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit also still stays sufficient (<code>items=206</code>; <code>projects=2</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 4, 2026 (08:07 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-04 08:07 JST</code> after <code>mind-upload@418c8f5d0ef9e871531d9cfb8548887e57f54d68</code>, <code>EEG-DATA@dc6d833b83e9a5e6a181edfee5349f561f65b043</code>, and <code>auto-research-funds@58d8738be5d55cff13d7bd626479783d6818de1f</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> tightens the front-door human-proxy comparison without widening the route, <code>EEG-DATA</code> still keeps <code>30,929</code> merged-unique rows, <code>28,892</code> high-confidence rows, <code>24,909</code> immediate rows, and <code>24,539</code> high-confidence immediate rows while promoting <code>HeartBEAM</code> and figshare <code>EEG at rest and with TMS</code> only as backup families, and <code>auto-research-funds</code> adds the <code>JGC-S</code> foreign-student scholarship only as an adjacent runway without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 22:10:18 GMT</code>; their route-facing bodies still surfaced <code>2026-04-04 01:04 JST</code> wording before this source sync. Official spot checks still keep <code>Kura Fund</code> open through <code>2026-04-17 17:00 JST</code>, the <code>Nakatani Foundation graduate scholarship</code> open through <code>2026-05-25 15:00 JST</code>, the <code>Kashinome Scholarship</code> in its annual <code>mid-January to early-April</code> window and the repo-side <code>2026-04-09</code> must-arrive reading, the <code>Nakatani Foundation research grant</code> in next-cycle watch, and the <code>Secom General Research Grant</code> closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit also still stays sufficient (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>Keio graduate scholarship=2</code>; <code>G-7=1</code>; <code>ENEOS=1</code>; <code>Doumei=0</code>; <code>Kenkyu no Susume=0</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 4, 2026 (01:04 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-04 01:04 JST</code> after <code>mind-upload@9b6a8b971ba08949b377ece744539c19180ad76e</code>, <code>EEG-DATA@56d765da60ba8d67bf8cb5bc61e4f1fdb06229c</code>, and <code>auto-research-funds@3c8569e284d61c47a6ac5ed8d8091aa15c6d53b3</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> adds field-level disclosure tightening for the artifact stack without widening the route, <code>EEG-DATA</code> deepens the public OpenNeuro metadata for <code>Numbers</code> and <code>PRIOS</code> while <code>summary.json</code> still reports <code>30,921</code> merged-unique rows, <code>28,884</code> high-confidence rows, <code>24,900</code> immediate rows, and <code>24,530</code> high-confidence immediate rows, and <code>auto-research-funds</code> adds current coverage for <code>同盟育成会</code> and <code>研究のすゝめ奨学金</code> without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 15:13:06 GMT</code>; their route-facing bodies still surfaced <code>2026-04-04 00:06 JST</code> wording before this source sync. Official spot checks still keep <code>Kura Fund</code> open through <code>2026-04-17 17:00 JST</code>, the <code>Nakatani Foundation graduate scholarship</code> open through <code>2026-05-25 15:00 JST</code>, the <code>Kashinome Scholarship</code> at <code>2026-04-09</code> must-arrive, and the <code>Nakatani Foundation research grant</code> plus <code>Secom General Research Grant</code> in watch/closed status. A fresh read-only Todoist audit also still stays sufficient (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>Keio graduate scholarship=2</code>; <code>G-7=1</code>; <code>ENEOS=1</code>; <code>同盟会=0</code>; <code>研究のすゝめ=0</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 4, 2026 (00:06 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-04 00:06 JST</code> after <code>mind-upload@84d84fb5a82d22d70d12c92a957327b3937bc422</code>, <code>EEG-DATA@b468ecc5f8c0ed34fb85c0bbc2a2e3c9282ce965</code>, and <code>auto-research-funds@eccee095a939a604cd4c684a2af6379f9dc3fa88</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> now just carries the earlier <code>23:06 JST</code> route reread addenda, <code>EEG-DATA</code> adds <code>fast mapping semantic integration EEG dataset</code> while <code>summary.json</code> now reports <code>30,921</code> merged-unique rows, <code>28,884</code> high-confidence rows, <code>24,900</code> immediate rows, and <code>24,530</code> high-confidence immediate rows, and <code>auto-research-funds</code> adds <code>Iizuka current card and Korean legacy sync</code> without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 14:13:44 GMT</code>; their route-facing bodies still surfaced <code>22:04 JST</code> on <code>brief / bridge / U13-2</code> and <code>22:04/22:05 JST</code> on <code>issue</code> before this source sync. Official spot checks still keep <code>Kura Fund</code> open through <code>2026-04-17 17:00 JST</code>, the <code>Nakatani Foundation graduate scholarship</code> open through <code>2026-05-25 15:00 JST</code>, the <code>Kashinome Scholarship</code> at <code>2026-04-09</code> must-arrive, and the <code>Nakatani Foundation research grant</code> plus <code>Secom General Research Grant</code> in watch/closed status. A fresh read-only Todoist audit also still stays sufficient (<code>items=206</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>Keio graduate scholarship=2</code>; <code>G-7=1</code>; <code>ENEOS=1</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (22:04 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 22:04 JST</code> after <code>mind-upload@1ab35b64796f3936e525befb5d9428d789a16263</code>, <code>EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a</code>, and <code>auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07</code> still keeps the same public six in the same execution order. The newest pulled delta is now concentrated in <code>EEG-DATA</code>: <code>summary.json</code> reports <code>30,918</code> merged-unique rows, <code>28,881</code> high-confidence rows, <code>24,898</code> immediate rows, and <code>24,528</code> high-confidence immediate rows after the latest exhaustive refresh, while <code>mind-upload</code> and <code>auto-research-funds</code> now just carry their earlier <code>21:05 JST</code> addenda without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 12:24:26 GMT</code>; their route-facing bodies already surfaced <code>21:05 JST</code> on <code>issue / brief / bridge</code> while <code>U13-2 route</code> still surfaced <code>21:05 JST</code> and <code>11:07 JST</code>. Official spot checks still keep the practical bridge narrow: <code>Kura Fund</code> remains open (<code>2026-04-17 17:00 JST</code>), the <code>Nakatani Foundation graduate scholarship</code> remains open (<code>2026-04-01 - 2026-05-25 15:00 JST</code>), and the rest of the watch/closed reading stays unchanged from the earlier reread. A fresh read-only Todoist audit also still stays sufficient (<code>items=205</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>Keio graduate scholarship=2</code>; <code>G-7=1</code>; <code>ENEOS=0</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (22:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 22:05 JST</code> after <code>mind-upload@1ab35b64796f3936e525befb5d9428d789a16263</code>, <code>EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a</code>, and <code>auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> now just carries the earlier <code>21:05 JST</code> route-hold sync, <code>EEG-DATA</code> adds <code>three more deep EEG dataset overrides</code> while now reporting <code>30,918</code> merged-unique rows, <code>28,881</code> high-confidence rows, <code>24,898</code> immediate rows, and <code>24,528</code> high-confidence immediate rows, and <code>auto-research-funds</code> now just carries the earlier <code>21:05 JST</code> funding addendum without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 12:24:26 GMT</code>; their route-facing bodies already surfaced the earlier <code>21:05 JST</code> hold note on <code>issue / brief / bridge / U13-2</code> before this source sync. Official spot checks in this run still keep <code>Kura Fund</code> (<code>2026-02-02 - 2026-04-17 17:00 JST</code>) and the <code>Nakatani Foundation graduate scholarship</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) open while the <code>Kashinome Scholarship</code> stays a student-runway side route (<code>2026-04-09 must arrive</code>), the <code>Nakatani Foundation research grant</code> stays next-cycle watch because the current public page still marks it closed, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit still stays sufficient (<code>items=205</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>Keio graduate scholarship=2</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (21:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 21:05 JST</code> after <code>mind-upload@3db1aa653b74d164c3a57b75677e345ea10356e0</code>, <code>EEG-DATA@c10c95274ecf1397768eb28de48aac8ce925c22d</code>, and <code>auto-research-funds@4a67e06b530bc742521f80fa5b13ccbe1115ebb9</code> still keeps the same public six in the same execution order. The newest pulled deltas are still carry-forward only: <code>mind-upload</code> now just carries the earlier <code>20:05 JST</code> route-hold addendum, <code>EEG-DATA</code> adds BDSP manual deep dives for missing EEG datasets while now reporting <code>30,914</code> merged-unique rows, <code>28,877</code> high-confidence rows, <code>24,896</code> immediate rows, and <code>24,526</code> high-confidence immediate rows, and <code>auto-research-funds</code> now just carries the earlier <code>20:05 JST</code> funding addendum without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages again returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 11:17:44 GMT</code>; their route-facing bodies already surfaced the earlier <code>20:05 JST</code> hold note on <code>issue / brief / bridge</code> while <code>U13-2 route</code> still surfaced <code>11:07 JST</code>. Official spot checks in this run still keep <code>Kura Fund</code> (<code>2026-04-17 17:00 JST</code>) and the <code>Nakatani Foundation graduate scholarship</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) open while the <code>Kashinome Scholarship</code> stays a student-runway side route (<code>2026-04-09 must arrive</code>), the <code>Nakatani Foundation research grant</code> stays next-cycle watch because the current public page still marks it closed, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit still stays sufficient (<code>items=205</code>; <code>projects=2</code>; <code>Nakatani family=11</code>; <code>G-7=1</code>; <code>ENEOS=0</code>; <code>Keio graduate scholarship=2</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (20:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 20:05 JST</code> after <code>mind-upload@b4fd73d9e983</code>, <code>EEG-DATA@649ff098ab57</code>, and <code>auto-research-funds@7c1b835d1d13</code> still keeps the same public six in the same execution order. The newest pulled deltas still deepen support space rather than widen the active EEG-first batch: <code>mind-upload</code> now splits human thermal evidence outside the current six into <code>passive / task-linked macro thermometry</code> and <code>perturbation-conditioned thermal routes</code>, <code>EEG-DATA</code> adds a restricted <code>Transcranial Magnetic Stimulation in Alzheimer's disease-Data</code> BDSP deep dive while now reporting <code>30,912</code> merged-unique rows, <code>28,875</code> high-confidence rows, and <code>24,894</code> directly usable rows, and <code>auto-research-funds</code> completes current-card coverage for <code>ENEOS</code> and <code>G-7</code> scholarships while still reporting <code>8,600</code> aid IDs, <code>4,308</code> rows, and <code>3,959</code> official-source rows without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live public pages returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 10:19:46 GMT</code>, but their route-facing bodies still surfaced the earlier <code>11:05/11:07 JST</code> hold note before this source sync. Official spot checks in this run still keep <code>Kura Fund</code> (<code>2026-04-17 17:00 JST</code>) and the <code>Nakatani Foundation graduate scholarship</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) open while the <code>Kashinome Scholarship</code> stays a student-runway side route (<code>2026-04-09 must arrive</code>), the <code>Nakatani Foundation research grant</code> stays next-cycle watch because the current public page still marks it closed, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit still stays sufficient (<code>items=205</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (11:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 11:05 JST</code> after <code>mind-upload@f70432e4a6c8</code>, <code>EEG-DATA@1981d34c5f71</code>, and <code>auto-research-funds@bfebe94da875</code> still keeps the same public six in the same execution order. The newest pulled deltas still tighten support space rather than widen the active EEG-first batch: <code>mind-upload</code> now tightens the <code>sleep replay integrity / physiology-gate</code> wording outside the current six, <code>EEG-DATA</code> refreshes its inventory and deep-dives the <code>COG-BCI</code> family while now reporting <code>30,904</code> merged-unique rows, <code>28,867</code> high-confidence rows, and <code>24,890</code> directly usable rows, and <code>auto-research-funds</code> now carries forward the <code>10:06 JST mind-upload funding addendum</code> while reporting <code>8,596</code> aid IDs, <code>4,308</code> rows, and <code>3,958</code> official-source rows without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live route pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Fri, 03 Apr 2026 01:31:28 GMT</code>, but their route-facing bodies still surfaced the earlier <code>05:12 JST</code> hold note before this source sync. Official spot checks in this run still keep <code>Kura Fund</code> (<code>2026-04-17 17:00 JST</code>) and the <code>Nakatani Foundation graduate scholarship</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) open while the <code>Kashinome Scholarship</code> stays a student-runway side route (<code>2026-04-09 must arrive</code>), the <code>Nakatani Foundation research grant</code> stays next-cycle watch because the current public page still marks it closed, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (05:12 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 05:12 JST</code> after <code>mind-upload@a9fc5d1cb691</code>, <code>EEG-DATA@8c3ace28bad0</code>, and <code>auto-research-funds@35756f8381c4</code> still keeps the same public six in the same execution order. The newest pulled deltas still tighten support space rather than widen the active EEG-first batch: <code>mind-upload</code> is now at a <code>docs: sync github wiki export</code> head that keeps the exported route mirrors aligned without changing the active queue, <code>EEG-DATA</code> carries forward a <code>VR navigation dataset</code> output refresh on top of a recent <code>EESM17</code> metadata deepening while still reporting <code>30,900</code> merged-unique rows, <code>28,863</code> high-confidence rows, and <code>24,885</code> directly usable rows, and <code>auto-research-funds</code> adds <code>JSPS overseas fellow</code> current-card snapshots on top of a recent <code>JSSF research publication</code> refresh while now reporting <code>8,594</code> aid IDs, <code>4,307</code> rows, and <code>3,957</code> official-source rows without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live route pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 19:17:56 GMT</code>, but their route-facing bodies still surfaced the earlier <code>04:05/04:06 JST</code> hold note before this source sync. Official spot checks in this run still keep <code>Kura Fund</code> (<code>2026-04-17 17:00 JST</code>) and the <code>Nakatani Foundation graduate scholarship</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) open while the <code>Kashinome Scholarship</code> stays a student-runway side route (<code>2026-04-09 must arrive</code>), the <code>Nakatani Foundation research grant</code> stays next-cycle watch because the current public page still marks it closed, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 3, 2026 (04:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-03 04:05 JST</code> after <code>mind-upload@f5e13ebdc474</code>, <code>EEG-DATA@53f5c8166faf</code>, and <code>auto-research-funds@1f190fec93a9</code> still keeps the same public six in the same execution order. The newest pulled deltas still tighten support space rather than widen the active EEG-first batch: <code>mind-upload</code> carries forward a <code>BCSFB / human-proxy composition</code> literature sync outside the current six, <code>EEG-DATA</code> still reports <code>30,900</code> merged-unique rows, <code>28,863</code> high-confidence rows, and <code>24,885</code> directly usable rows after a catalog refresh that does not replace any current anchor family, and <code>auto-research-funds</code> refreshes <code>MUFJ research grant</code> data while now reporting <code>8,593</code> aid IDs, <code>4,306</code> rows, and <code>3,956</code> official-source rows without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live route pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 18:14:39 GMT</code>, official spot checks in this run still keep <code>Kura Fund</code> (<code>2026-04-17 17:00 JST</code>) and the <code>Nakatani Foundation graduate scholarship</code> (<code>2026-04-01 - 2026-05-25 15:00 JST</code>) open while the <code>Kashinome Scholarship</code> stays a student-runway side route (<code>2026-04-09 must arrive</code>), the <code>Nakatani Foundation research grant</code> stays next-cycle watch because the current public page still marks it closed, and the <code>Secom General Research Grant</code> remains closed after <code>2026-03-31 12:00 JST</code>. A fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>), so no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (23:08 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 23:08 JST</code> after <code>mind-upload@f5d1d1dd1683</code>, <code>EEG-DATA@ee1463d28288</code>, and <code>auto-research-funds@ec24a355abbc</code> still keeps the same public six in the same execution order. The newest pulled deltas still deepen route discipline and support space rather than widen the active EEG-first batch: <code>mind-upload</code> clarifies the causal-versus-human-proxy bridge outside the current six, <code>EEG-DATA</code> refines candidate curation and now reports <code>30,896</code> merged-unique rows, <code>28,859</code> high-confidence rows, and <code>24,882</code> directly usable rows, and <code>auto-research-funds</code> adds <code>Geo-Kagaku</code> current cards without displacing the practical shortlist. Public-safe wording therefore still keeps <code>D10</code> as the only clear public-open primary anchor in the current six while <code>D03/D02/D01</code> remain gated-support planning anchors. The checked live route pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 13:12:21 GMT</code>, official spot checks in this run still keep <code>Kura Fund</code> and the <code>Nakatani Foundation graduate scholarship</code> open while <code>Nakatani Foundation research grant</code> and <code>Secom General Research Grant</code> stay closed/watch, and a fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>). This update therefore remains a bounded route-hold addendum rather than a solved-claim update, and no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>If you want the current six research questions being turned into EEG-ready work packages</strong>
<p>
The active public deepening batch, listed in execution order, is <code>U13-2</code>, <code>U13-5</code>, <code>U0-2</code>, <code>U0-3</code>, <code>U14-4</code>, and <code>U14-2</code>. These are not solved questions. They are the current bounded work packages where one claim, one dataset anchor, one KPI bundle, and one explicit external-dependency boundary are being fixed first. As of April 3, 2026 after the <code>02:05 JST</code> actual-pull reread, this batch remains intentionally narrower: it concentrates on <code>inner-speech decoding + identity drift + reproducibility auditing</code> with the conservative anchor set <code>D10/D03/D01/D02</code>, because that is still the cleanest current bridge from mind-upload research questions to EEG-ready and fundable work packages. This is a route-setting update, not a solved-claim update. The latest actual-pull reread at <code>2026-04-03 02:05 JST</code> after <code>mind-upload@94a41524ca1a</code>, <code>EEG-DATA@03172b700180</code>, and <code>auto-research-funds@e6fde9b4f248</code> still keeps <code>D10</code> as the only clearly public-open primary anchor in the current six, while <code>D03</code>, <code>D02</code>, and <code>D01</code> still read as gated support anchors on the public route. The newest pulled deltas still deepen support rather than widen the route: <code>mind-upload</code> now clarifies the <code>BCSFB</code> front-door family outside the current six, <code>EEG-DATA</code> now reports <code>30,900</code> merged-unique rows, <code>28,863</code> high-confidence rows, and <code>24,885</code> directly usable rows after the latest Zenodo visual EEG deep dive, and <code>auto-research-funds</code> now carries forward an <code>NII</code> open-collab legacy funding card without displacing the current practical shortlist. The checked live route pages now returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 16:25:49 GMT</code>, and their body wording still served the bounded <code>00:07 JST</code> hold note, so this source edit only keeps the entry-page batch explanation on the same current basis rather than widening the batch. The current execution order therefore stays <code>U13-2 → U13-5 → U0-2 → U0-3 → U14-4 → U14-2</code>, and public-facing progress still means bounded artifacts rather than solved claims: a <code>brain-minus-prior</code> control table for <code>U13-2</code>, a perception-to-recall branch specification note for <code>U13-5</code>, an <code>offset/jitter + state-feature drift</code> audit for <code>U0-2</code>, a threshold-stability and overfit-exclusion rule for <code>U0-3</code>, filled Card examples for <code>U14-4</code>, and a fixed-split rerun contract for <code>U14-2</code>. The current row packets now also record one compact <code>first-pass KPI bundle + stop rule</code> per row, so readers can see what would stop the route before the claim widens. The main public-safe tightening in this reread stays row-specific rather than batch-level: <code>U13-5</code> still carries an explicit recall-validity caveat because the visible <code>D03</code> metadata is still a cognitive-load package, while <code>U14-4/U14-2</code> still state more explicitly that <code>D01</code> is only a latency/disclosure floor and still needs <code>D13</code> before broader rerun wording. <code>Kura Fund</code> and the <code>Nakatani Foundation graduate scholarship</code> remain the near-term bridge, the <code>Kashinome Scholarship</code> stays only as a student-runway side route, and the broader neuroscience grant routes stay in watch mode. A newer adjacent option is now visible on the funding side: the latest <code>NII</code> carry-forward is useful as a collaboration-side reminder, but it still fits better as an adjacent lane than as a reason to replace the current six. Larger social-deployment programs remain outside this current EEG-first route. If you want the shortest one-page summary of what EEG can close now, what still needs outside support, and what funding lane still fits, start with the <a href="wiki/mind-upload-rq-solvability-bridge.html">RQ solvability bridge</a>. If you want the cleanest public-open <code>A</code>-tier route outside the current six without changing the batch itself, continue with the <a href="wiki/u7-1-synchronization-contract-route.html">U7-1 synchronization-contract route packet</a>. If you want the adjacent row that turns synchronization error itself into explicit release-block metrics without changing either the current six or the next-watch headline queue, continue with the <a href="wiki/u7-2-timing-metric-route.html">U7-2 timing-metric route packet</a>, then the <a href="wiki/u1-2-uncertainty-calibration-route.html">U1-2 uncertainty-calibration route packet</a>, the <a href="wiki/u4-2-minimal-causal-route.html">U4-2 minimal-causal route packet</a>, and the <a href="wiki/u8-1-closed-loop-delay-tolerance-route.html">U8-1 closed-loop delay-tolerance route packet</a>. For a compact row-by-row version of the same six-question route, see the <a href="wiki/mind-upload-current-public-six-rq-brief.html">current public six route brief</a>. For the exact <code>Dxx + DOI</code> anchors, first-pass KPIs, one explicit stop rule per row, and the external dependencies kept outside the EEG claim, start with the <a href="wiki/mind-upload-rq60-deep-focus-notes.html">deep focus notes</a>, the <a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">grant and dataset playbook</a>, the <a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ-by-RQ deep dossiers</a>, and the <a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">current funding shortlist</a>.
</p>
<p>
If you read the current six as one narrow solve-first program rather than as six unrelated rows, the order still stays <code>U13-2 → U13-5</code> for the speech-side contribution floor, then <code>U0-2 → U0-3</code> for the identity-drift timing and threshold floor, then <code>U14-4 → U14-2</code> for the disclosure-to-rerun contract floor. The cleanest public-open support underneath those last four rows still stays outside the batch itself: <code>U7-1</code> keeps the synchronization contract public-open on <code>D11</code>, <code>U7-2</code> now turns that same family into explicit timing metrics and release-block thresholds, and <code>U1-2</code> keeps the inverse-uncertainty packet grounded on <code>D08</code>. That is why the batch stays fixed even though the supporting infrastructure rows are already public and readable.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (19:03 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 19:03 JST</code> after <code>mind-upload@e1a7e7e2f22c</code>, <code>EEG-DATA@a7f9390492fd</code>, and <code>auto-research-funds@00cdbaa9a122</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head deepens the <code>blood-CSF barrier / choroid-plexus</code> route split on human neurovascular pages outside the current six, <code>EEG-DATA</code> still reports <code>30,892</code> merged-unique rows, <code>28,855</code> high-confidence rows, and <code>24,880</code> directly usable rows after the <code>OSF gazx2</code> and <code>OpenNeuro ds007081</code> deep dives, and <code>auto-research-funds</code> still keeps its latest summary at <code>8,590</code> aid IDs, <code>4,301</code> rows, and <code>3,951</code> official-source rows. None of those changes replace <code>D10/D03/D02/D01</code>. The checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 09:37:54 GMT</code>, but the route-facing wording still surfaced the earlier <code>18:06 JST</code> hold note, so this run only adds a bounded route-hold sync instead of widening the claim surface. The official funding bridge still stays narrow (<code>Kura Fund = 2026-04-17 17:00</code>, <code>Nakatani Foundation graduate scholarship = 2026-05-25 15:00</code>, <code>Kashinome Scholarship = 2026-04-09 must arrive</code>, <code>Secom General Research Grant = closed</code>, <code>Nakatani Foundation research grant = next-cycle watch</code>), and a fresh read-only Todoist audit still stayed sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>; <code>AI for Aging-Society Problem Solving=0</code>). This update therefore remains a bounded route-hold addendum rather than a solved-claim update, and no new Todoist item was justified in this run.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (11:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 11:05 JST</code> after <code>mind-upload@208e59e2180c</code>, <code>EEG-DATA@00d85380f3fd</code>, and <code>auto-research-funds@f4ba35518400</code> still keeps the same public six and the same execution order. The newest <code>EEG-DATA</code> head deep-dives the maintained <code>ChineseEEG-2</code> release plus the public <code>auditory-eeg</code> family and still reports <code>30,887</code> merged-unique rows, <code>28,850</code> high-confidence rows, and <code>24,875</code> immediately usable rows. That strengthens the public-open speech-side backup ladder for <code>U13-2/U13-5</code>, but it still does not replace <code>D10</code> as the only clear public-open primary anchor or repair the recall-validity gap that keeps <code>U13-5</code> bounded. A direct live-access reread still shows <code>Subscription Required</code> and <code>LOGIN TO ACCESS DATASET FILES</code> on the current <code>D03/D02/D01</code> DataPort pages, the checked live public pages still returned <code>HTTP 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT</code>, the official funding bridge still stays narrow, and a fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>). This update therefore remains a bounded route-hold addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (11:09 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 11:09 JST</code> after <code>mind-upload@208e59e2180c</code>, <code>EEG-DATA@00d85380f3f</code>, and <code>auto-research-funds@f4ba35518400</code> still keeps the same public six and the same execution order. The current <code>mind-upload</code> head is the earlier 10:07 route-hold packet refresh itself, <code>EEG-DATA</code> adds public-open speech/listening and auditory-biometric deep dives while still reporting <code>30,887</code> merged-unique rows, <code>28,850</code> high-confidence rows, and <code>24,875</code> directly usable rows, and <code>auto-research-funds</code> keeps the same practical shortlist while its current repository stats stay at <code>8,585</code> aid IDs, <code>4,293</code> rows, and <code>3,943</code> official-source rows. None of those changes replace <code>D10/D03/D02/D01</code>: <code>ds007591</code> and <code>ds007602</code> strengthen speech-side backup coverage but still release only three participants each, <code>ChineseEEG-2</code> widens reading/listening alignment coverage but still does not expose the intended recall-labeled branch for <code>U13-5</code>, and PhysioNet <code>auditory-eeg</code> is clearly public-open but only single-day 4-channel coverage and therefore does not replace <code>D02</code> for the current identity-drift floor. The checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT</code>, the funding bridge still stays narrow, and a fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>). This update therefore remains a bounded route-hold addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (10:07 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 10:07 JST</code> after <code>mind-upload@be507c810b11</code>, <code>EEG-DATA@3f20f48cca6e</code>, and <code>auto-research-funds@fb32c05163f4</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head refines EEG foundation setup-equivalence boundaries outside the current six, <code>EEG-DATA</code> deep-dives the HBN EEG release 11 route and now reports <code>30,887</code> merged-unique rows, <code>28,850</code> high-confidence rows, and <code>24,871</code> directly usable rows, and <code>auto-research-funds</code> keeps the same practical shortlist while its current repository stats stay at <code>8,585</code> aid IDs, <code>4,293</code> rows, and <code>3,943</code> official-source rows. None of those changes replace <code>D10/D03/D02/D01</code>; the row-level reading only tightens one step further inside that unchanged batch: <code>U13-5</code> still carries an explicit recall-validity caveat because the visible <code>D03</code> metadata is still not a recall-labeled package, and <code>U14-4/U14-2</code> still keep <code>D13</code> as the first public-open rerun support family beyond the current <code>D01</code> disclosure floor. The checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Thu, 02 Apr 2026 00:15:06 GMT</code>, the funding bridge still stays narrow, and a fresh read-only Todoist audit still stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>; <code>Brain Science Foundation=8</code>; <code>Okawa=2</code>; <code>Japan Industrial Science Research Institute=1</code>). This update therefore remains a bounded route-hold addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (09:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 09:05 JST</code> after <code>mind-upload@d7f30648fc40</code>, <code>EEG-DATA@ac8cc6fc8e74</code>, and <code>auto-research-funds@31ec17305f6a</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head tightens a literature myelin-route split outside the current six, <code>EEG-DATA</code> now reports <code>merged_unique=30886</code>, <code>high_confidence=28849</code>, and <code>access_counts_high.immediate=24500</code>, and <code>auto-research-funds</code> carries forward the <code>Aoi graduate scholarship</code> / <code>JSSF research grant</code> merges plus a README-stat refresh to <code>8,585</code> aid IDs, <code>4,293</code> rows, and <code>3,943</code> official-source rows without changing the practical shortlist. None of those changes replace <code>D10/D03/D02/D01</code>, the checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Wed, 01 Apr 2026 23:29:12 GMT</code>, and the official funding bridge still stays narrow: <code>Kura Fund</code> remains open through <code>2026-04-17 17:00</code>, the <code>Nakatani Foundation graduate scholarship</code> remains open through <code>2026-05-25 15:00</code>, the <code>Nakatani Foundation research grant</code> remains next-cycle watch, the <code>Kashinome Scholarship</code> still reads on its official page as the annual <code>mid-January to early-April</code> window, and the <code>Secom General Research Grant</code> remains closed for the current cycle. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), and the live pages still surfaced the earlier <code>04:09 JST</code> / <code>03:08 JST</code> rereads before this source sync, so this update only refreshes the public route-hold wording on the entry page and still remains a bounded route-setting addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (04:09 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 04:09 JST</code> after <code>mind-upload@92d1547bfeb9</code>, <code>EEG-DATA@2e3799a174d9</code>, and <code>auto-research-funds@f5f55bcbf724</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head splits the beginner molecular-maintenance family outside the current six, <code>EEG-DATA</code> now reports <code>merged_unique=30877</code>, <code>high_confidence=28840</code>, and <code>access_counts_high.immediate=24492</code>, and <code>auto-research-funds</code> carries forward the April 2 funding refresh without changing the practical shortlist. None of those changes replace <code>D10/D03/D02/D01</code>, the checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Wed, 01 Apr 2026 18:24:31 GMT</code>, and the official funding bridge still stays narrow: <code>Kura Fund</code> remains open through <code>2026-04-17 17:00</code>, the <code>Nakatani Foundation graduate scholarship</code> remains open through <code>2026-05-25 15:00</code>, the <code>Nakatani Foundation research grant</code> remains next-cycle watch, the <code>Secom General Research Grant</code> remains closed for the current cycle, and the <code>Kashinome Scholarship</code> still stays only as a support-side runway route. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this source sync only refreshes the public route-hold wording on the entry page and still remains a bounded route-setting addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (03:08 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 03:08 JST</code> after <code>mind-upload@d391dbede29e</code>, <code>EEG-DATA@f9df9ba85a6</code>, and <code>auto-research-funds@95f804055809</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head splits ECM / PNN literature routes outside the current six, <code>EEG-DATA</code> adds two immediate-access deep-dive candidates (<code>10.48804/NV4RGL</code> and <code>10.7281/T1/B660D2</code>) without displacing the current anchor family, and <code>auto-research-funds</code> adds Gakusho / NII funding merges plus a README-stat refresh without changing the practical shortlist. None of those changes replace <code>D10/D03/D02/D01</code>, the checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Wed, 01 Apr 2026 17:27:08 GMT</code>, and the official funding windows still keep the same narrow bridge. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this source sync only refreshes the public route-hold wording on the entry pages and still remains a bounded route-setting addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 2, 2026 (00:03 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-02 00:03 JST</code> after <code>mind-upload@cff3abab58e8</code>, <code>EEG-DATA@a885ef3f029d</code>, and <code>auto-research-funds@0f60872538dc</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head tightens deuterium operating-point wording outside the current six, <code>EEG-DATA</code> adds the <code>DANDI 001187</code> deep dive and now reports <code>merged_unique=30875</code>, <code>high_confidence=28838</code>, and <code>access_counts_high.immediate=24492</code>, and <code>auto-research-funds</code> carries forward the <code>Isono</code>/<code>Okabe</code> refresh without replacing the practical shortlist. None of those changes replace <code>D10/D03/D02/D01</code>, the checked live public pages still returned <code>HTTP 200</code> with <code>Last-Modified: Wed, 01 Apr 2026 14:17:54 GMT</code>, and the official funding windows still keep the same narrow bridge. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>projects=2</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this source update remains a bounded route-setting addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026 (22:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-01 22:05 JST</code> after <code>mind-upload@84e5337</code>, <code>EEG-DATA@bbb8d6c63d7</code>, and <code>auto-research-funds@5ff33413e</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head clarifies clearance-route labels at the front door outside the current six, <code>EEG-DATA</code> refreshes deep-dive metadata while keeping <code>merged_unique=30873</code>, <code>high_confidence=28836</code>, and <code>access_counts_high.immediate=24487</code>, and <code>auto-research-funds</code> adds the <code>Yamaoka graduate scholarship</code> snapshot plus README-facing stats refresh without changing the practical shortlist. None of those changes replace <code>D10/D03/D02/D01</code>, the checked live public pages still returned <code>HTTP/2 200</code> with <code>Last-Modified: Wed, 01 Apr 2026 12:13:54 GMT</code>, and the official funding windows still keep the same narrow bridge. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this source update remains a bounded route-setting addendum rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026 (18:05 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-01 18:05 JST</code> after <code>mind-upload@9984d0b</code>, <code>EEG-DATA@5fc1df00f07</code>, and <code>auto-research-funds@d7092c8e9</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head deepens wearable <code>OPM / MEG</code> route synchronization and measurement-stack clarification outside the current six, <code>EEG-DATA</code> adds a continuous-pursuit EEG BCI deep dive and now reports <code>merged_unique=30873</code>, <code>high_confidence=28836</code>, and <code>access_counts_high.immediate=24486</code>, and <code>auto-research-funds</code> keeps the same practical shortlist after the recent carry-forward scholarship refresh. None of those changes replace <code>D10/D03/D02/D01</code>, the live public pages still return <code>200</code> with <code>Last-Modified: Wed, 01 Apr 2026 08:22:51 GMT</code>, and the official funding windows still keep the same narrow bridge. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this remains a bounded route-setting update rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026 (17:06 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-01 17:06 JST</code> after <code>mind-upload@c5a0550</code>, <code>EEG-DATA@82893f6ca6e</code>, and <code>auto-research-funds@ec6f7d068</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head deepens astrocyte PET route splits outside the current six, <code>EEG-DATA</code> deep-dives the KMI EEG dataset and now reports <code>merged_unique=30871</code>, <code>high_confidence=28834</code>, and <code>access_counts_high.immediate=24484</code>, and <code>auto-research-funds</code> adds the <code>Megachips 2026 scholarship</code> snapshot plus a README-stat refresh without changing the practical shortlist. None of those changes replace <code>D10/D03/D02/D01</code>, the live public pages still return <code>200</code> with <code>Last-Modified: Wed, 01 Apr 2026 07:16:09 GMT</code>, and the official funding windows still keep the same narrow bridge. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Nakatani graduate scholarship=7</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this remains a bounded route-setting update rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026 (14:08 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-01 14:08 JST</code> after <code>mind-upload@ccef40f</code>, <code>EEG-DATA@deefd5f95c6</code>, and <code>auto-research-funds@f5f76c485</code> keeps the same public six and the same execution order. The refreshed <code>EEG-DATA</code> head now reports <code>merged_unique=30869</code>, <code>high_confidence=28832</code>, and <code>access_counts_high.immediate=24482</code>, and its new experiment-metadata report now covers <code>18,312 / 28,832</code> rows with at least one experiment-facing field. Those gains still deepen route support rather than replace <code>D10/D03/D02/D01</code>. The route-safe access reading also stays narrow in one specific way: the refreshed local catalog still shows <code>D03/D02</code> as catalog-side immediate rows and <code>D01</code> as a mixed immediate/check-needed pair, but the live-access read remains stricter, so <code>D10</code> stays the only clear public-open primary anchor while <code>D03/D02/D01</code> still stay gated support anchors in public wording. The row-level wording is now slightly tighter inside that unchanged batch: visible <code>D03</code> metadata still does not expose a recall-specific label, and visible <code>D01</code> package contents still read as a latency/synchronization floor rather than a rerun benchmark, so <code>U13-5</code> keeps an explicit recall-validity caveat and <code>U14-4/U14-2</code> keep <code>D13</code> as the first public-open rerun support family. The live public pages still returned <code>200</code> and now share <code>Last-Modified: Wed, 01 Apr 2026 04:20:02 GMT</code>. The official funding bridge is still unchanged (<code>Kura Fund</code>, <code>Nakatani Foundation graduate scholarship</code>, <code>Kashinome Scholarship</code>, <code>Secom General Research Grant</code> closed), and a fresh read-only Todoist sync still shows the route already covered (<code>items=203</code>, <code>Kura=2</code>, <code>Nakatani family=11</code>, <code>Kashinome=2</code>, <code>Secom=3</code>), so this page still describes a bounded route-setting update rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026</strong>
<p>
A post-pull reread at <code>2026-04-01 11:06 JST</code> after <code>mind-upload@aa21ab9855c1</code>, <code>EEG-DATA@cccd137a3468</code>, and <code>auto-research-funds@3a691196cb9f</code> keeps the same public six and the same execution order. The newest <code>EEG-DATA</code> change deepens repository-wide metadata and the refreshed summary now reports <code>merged_unique=30866</code>, <code>high_confidence=28829</code>, and <code>access_counts_high.immediate=24479</code> without replacing <code>D10/D03/D02/D01</code> or reordering <code>U7-1/U1-2/U4-2/U8-1</code>, while the current <code>auto-research-funds</code> head refreshes repo-level stats without changing the practical shortlist. The route-safe access reading also stays narrow: <code>D10</code> remains the only clear public-open primary anchor, while <code>D03/D02/D01</code> remain gated support anchors. The live public pages still returned <code>200</code> and <code>issue.html</code> still names the same six in the same order, so this page continues to describe a bounded route-setting update rather than solved claims.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026 (14:09 JST)</strong>
<p>
An actual-pull reread at <code>2026-04-01 14:09 JST</code> after <code>mind-upload@ccef40f2f7cf</code>, <code>EEG-DATA@deefd5f95c6d</code>, and <code>auto-research-funds@f5f76c485ccb</code> still keeps the same public six and the same execution order. The newest <code>mind-upload</code> head clarifies presynaptic release-machinery ceilings outside the current six, <code>EEG-DATA</code> deepens Mendeley EEG metadata and now reports <code>merged_unique=30869</code>, <code>high_confidence=28832</code>, and <code>access_counts_high.immediate=24482</code>, and <code>auto-research-funds</code> only refreshes repo-level stats. None of those changes replace <code>D10/D03/D02/D01</code>, the live public pages still return <code>200</code> with <code>Last-Modified: Wed, 01 Apr 2026 04:20:02 GMT</code>, and the official funding windows still keep the same narrow bridge. A fresh read-only Todoist audit also stays sufficient (<code>items=203</code>; <code>Kura=2</code>; <code>Nakatani family=11</code>; <code>Kashinome=2</code>; <code>Secom=3</code>), so this remains a bounded route-setting update rather than a solved-claim update.
</p>
</div>
<div class="note-box">
<strong>Latest route hold on April 1, 2026 (12:06 JST)</strong>
<p>
A second no-op actual-pull reread at <code>2026-04-01 12:06 JST</code> after <code>mind-upload@9f4bc8e760b1</code>, <code>EEG-DATA@1324f9e1ae2b</code>, and <code>auto-research-funds@6548b1650535</code> still keeps the same public six and the same execution order. The newest <code>EEG-DATA</code> head now reports <code>merged_unique=30867</code>, <code>high_confidence=28830</code>, and <code>access_counts_high.immediate=24480</code>, but this is still metadata deepening rather than an anchor replacement, so the current public family remains <code>D10 / D03 / D02 / D01</code> and the next-watch order remains <code>U7-1 / U1-2 / U4-2 / U8-1</code>. A live browser-level recheck still returned <code>200</code> for <code>issue.html</code>, the public-six brief, the solvability bridge, and the <code>U8-1</code> route page, with <code>Last-Modified: Wed, 01 Apr 2026 02:26:28 GMT</code> on those public surfaces. The official funding pages still keep the same narrow bridge open or fixed in watch status: <code>Kura Fund = 2026-02-02 - 2026-04-17 17:00</code>, <code>Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00</code>, <code>Kashinome Scholarship = 2026-01-14 - 2026-04-09</code>, and <code>Secom General Research Grant</code> remains closed for the current cycle. This reread therefore adds no solved claim and no batch switch. It only keeps the current route public-safe and current.
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
