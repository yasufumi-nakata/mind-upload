---
layout: default
title: "Verification: Mind Uploading Verification Commons"
description: "A blueprint of standards, benchmarks, registries, and audits for turning mind uploading and WBE into a science with measurable progress."
article_type: Platform
subtitle: "Use the logic of PDB x BIDS x PhysioNet x OSF to define WBE success conditions and reproducible progress"
author: Mind Uploading Research Project
last_updated: "2026-03-18"
note: "Operational Specification"
audience: "Readers who want the site's core policy and anyone checking what must exist before progress can honestly be claimed"
reading_time: "15-25 min"
page_intro: "This page is the core blueprint of Mind-Upload. It explains how to define progress in advance rather than retroactively by aligning data, evaluation, failure conditions, and reproduction procedures first."
accuracy_note: "This page does not claim that WBE is already possible. It defines the substrate needed to test whether it is."
page_highlights:
  - "Standards, repositories, benchmarks, and audits must be built as one package."
  - "Claim levels and failure conditions are fixed up front so decoding is not confused with emulation."
  - "For decode / biomarker scores, the Specificity & Shortcut Card separates the target neural variable from nuisance routes and audits subject / session fingerprint plus acquisition-distribution shortcuts independently."
  - "This page explains why collecting data alone is not the same as making progress."
  - "For brain-to-text and speech decode, the Neural Contribution Card fixes task constraint, language prior, candidate set, no-brain / no-LM / shuffle baselines, and subject cooperation."
  - "For multimodal or atlas-prior results, the Fusion Card is added on top of the Observability Budget so acquisition relation, synchronization, fusion model, vascular-state / CVR limits for hemodynamic stacks, and external validation are fixed explicitly."
  - "At L2 and above, the latent-state error budget is added on top of the Observability Budget so the still-unobserved states that stop the claim are disclosed."
  - "At L2 and above, perisynaptic ECM / PNN state is separated from synaptic weights and glia when a claim depends on adult plasticity, receptor mobility, or memory stabilization."
  - "At L2 and above, local proteostasis / synaptic-tagging state is separated from current weights and transcription when a claim depends on late-LTP capture, consolidation, or reconsolidation."
  - "At L2 and above, ionic milieu / chloride homeostasis is separated from excitability and glial support when a claim depends on inhibitory polarity, rhythm stability, or state transitions."
  - "At L2 and above, thermal-state is separated from timing-state and bioenergetics when a claim depends on membrane kinetics, field-potential amplitude, or sequence timing."
  - "At L2 and above, bioenergetic / mitochondrial support is separated from glial support when a claim depends on repeated-burst reliability, local ATP reserve, or dendritic plasticity."
  - "At L2 and above, delay is treated as timing-state rather than one scalar, so device latency, biological conduction timing, and human macro timing proxies are not collapsed into one number."
  - "At L2 and above for intervention / closed-loop results, the Intervention Card fixes trigger rule, timing audit, control / sham, safe stop, and recalibration burden."
  - "For cross-day or longitudinal claims, the Temporal Validity Card audits fixed decoder interval, state annotation, recalibration burden, and transfer ceiling independently."
  - "For cross-day or remote-memory claims, the maintenance-state error budget reports controller state, sleep history, and support-state proxies separately, so temporal success is not auto-promoted to a maintenance-consistent claim."
  - "For chronic invasive claims, signal-chain drift and implant tissue response are audited separately rather than being folded into unit-identity audit alone."
  - "For outputs that include probabilities, intervals, prediction sets, or abstention, the Calibration & Abstention Card fixes fit/calibration/test separation, evaluation family, coverage-risk, and fallback behavior."
known_points:
  - "Comparable progress does not exist unless standards, shared infrastructure, evaluation, and auditing are aligned together."
  - "At L0-L2, reproducibility and falsification conditions can be designed in advance."
  - "Decode and emulate are distinct claims and require different evidence."
  - "The same decoding score is not target-specific evidence if eye movement, EMG, uninstructed movement, auditory feedback, subject / session fingerprint, or acquisition-distribution shortcuts remain unresolved."
  - "A multimodal result is not one thing; simultaneous acquisition, geometric fusion, invasive calibration, and atlas priors must be audited separately."
  - "A BOLD or fNIRS amplitude difference without vascular-state / CVR audit remains a hemodynamic-limited difference rather than a clean neural difference."
  - "A synapse list or weight estimate does not by itself fix perisynaptic ECM / PNN state, so plasticity and stabilization claims need a separate ceiling."
  - "A weight estimate does not fix which tagged synapses or dendritic branches capture plasticity-related proteins, so late-stabilization claims need a separate proteostasis ceiling."
  - "A connectome, cell type, and weight estimate do not by themselves fix ionic milieu / chloride homeostasis, so inhibitory sign and state-transition claims need a separate ceiling."
  - "A connectome, cell type, and timing proxy do not by themselves fix local thermal-state, so field-potential and sequence-timing claims need a separate ceiling."
  - "A connectome, cell type, and glial proxy do not by themselves fix local ATP reserve or mitochondrial positioning, so repeated-burst and dendritic-plasticity claims need a separate bioenergetic ceiling."
  - "Passing a hardware latency audit is not the same as recovering biological timing-state; claims that depend on phase or synchrony need both sides separated."
  - "In chronic invasive recording, unit-matching uncertainty and tissue response around the implant are separate audit items."
unknown_points:
  - "There is still no settled answer on which causal-structure approximation would be sufficient for L4 personal identity."
  - "A final success condition integrating thermodynamics, closed-loop behavior, and identity is still incomplete."
  - "L5 institutional design cannot be determined by technical requirements alone."
wiki_links:
  - label: "Wiki: Verification Basics"
    url: "/wiki/verification-basics.html"
    description: "A beginner explanation of why standards, benchmarks, registries, and audits are needed."
  - label: "Wiki: How To Read Public Page Headers"
    url: "/wiki/page-header-reading-guide.html"
    description: "Explains how to use the guidance blocks, known/unknown sections, and wiki routes at the top of this page."
  - label: "Wiki: Reading Routes By L0-L5 Level"
    url: "/wiki/claim-level-reading-routes.html"
    description: "Shows which page to visit next depending on which L0-L5 claim level you want to follow."
  - label: "Wiki: Minimum Artifact Pack For L0"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "Organizes the minimum set of BIDS, QC, split rules, baselines, execution steps, and failure cases."
  - label: "Wiki: Reading Partial Solutions, Exploratory Stages, And Unfinished Areas"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "Clarifies the difference between designed, unimplemented, insufficient, and unfinished states."
  - label: "Wiki: Reading Claims And Evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "A practice page for reading L0-L5 claims by evidence strength."
  - label: "Wiki: Data Splits And Leakage"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "Explains split units and leakage failures that must be checked before accuracy numbers."
  - label: "Wiki: From Observation To Estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Organizes ESI, DCM, SCM, and causal equivalence classes through the distinction between observation and estimation."
  - label: "Wiki: Why A Connectome Is Not Enough"
    url: "/wiki/connectome-is-not-enough.html"
    description: "Organizes the state variables that remain missing if you only have a connectome, including synapses, delays, neuromodulation, and glia."
  - label: "Wiki: Observability And Claim Ceiling By Measurement Stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Shows what each measurement stack directly observes and where its claim ceiling appears."
  - label: "Wiki: Counterfactuals, Interventions, And Perturbations"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "Explains from first principles the difference between held-out accuracy and causal perturbation testing."
  - label: "Wiki: Uncertainty, Calibration, And Abstention"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "Introduces point estimates, intervals, propagation, and abstention under low confidence."
  - label: "Wiki: Identity Evaluation And Continuity Tests"
    url: "/wiki/identity-and-continuity-tests.html"
    description: "Organizes what L4 is trying to test, and how far, from the perspective of continuity."
  - label: "Wiki: Baselines, Preregistration, And Model Cards"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Explains the distinct roles of baselines, preregistered rules, result logs, and failure cases."
  - label: "Wiki: Update, Branching, And Stop Rules"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "Introduces diff logs for updates, branch IDs, and stop conditions from the basics upward."
  - label: "Wiki: Standards, Repositories, Validators, And Benchmarks"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "Clarifies the role differences among standards, shared infrastructure, formal validation, and comparison rules."
  - label: "Wiki: Closed Loops, Latency, Jitter, And Safety Stops"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Explains the differences among latency, jitter, safety stops, and abstention required at L3."
  - label: "Wiki: Basics Of Thermodynamic Grounding"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Introduces Landauer, dissipation, NESS, and EPR from the ground up."
recommended_pages:
  - label: "Technical Roadmap"
    url: "/tech_roadmap.html"
  - label: "Datasets and Benchmarks"
    url: "/datasets.html"
  - label: "Contribution Guide"
    url: "/issue.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>One Problem</h2>
<p>
To keep mind uploading and WBE from remaining only a dream narrative, the first requirement is <strong>a shared rule set</strong>. Mind-Upload puts data layout, evaluation, failure judgment, and reproduction procedures in place first so anyone can check the same result against the same criteria.
</p>
</div>

<div class="note-box">
<strong>What To Fix First On This Page</strong>
<p>
This page aligns four things first: <strong>standards (how artifacts are structured)</strong>, <strong>shared infrastructure (where they live)</strong>, <strong>evaluation (what comparisons are allowed)</strong>, and <strong>audit (how failures and updates are recorded)</strong>. Any one of these on its own is insufficient for comparable progress.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>What You Want To Know Now</th>
<th>Read This Section First</th>
<th>What It Gives You</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to know what this site calls "progress"</td>
<td><a href="#definition">The One Question This Site Is Solving</a></td>
<td>Shows what must be satisfied before progress can be claimed, in terms of claim level and reproducibility conditions.</td>
</tr>
<tr>
<td>I want to know the minimum public goods that must exist</td>
<td><a href="#deliverables">Deliverables Of The Mind-Upload Commons</a></td>
<td>Explains the division of roles among the Data Standard, Benchmark, Registry, and Leaderboard.</td>
</tr>
<tr>
<td>I want to know what is already implemented</td>
<td><a href="#current-status">Implementation Status</a></td>
<td>Separates what is already designed from what remains unpublished or unimplemented.</td>
</tr>
<tr>
<td>I only want the stricter verification conditions</td>
<td><a href="#observability-budget">Observability Budget</a> / <a href="#verification-rigor">Verification Rigor Requirements</a></td>
<td>Shows what is directly observed, what is inferred, and how uncertainty and preprocessing fidelity are handled.</td>
</tr>
<tr>
<td>I want to know how this differs from ordinary accuracy evaluation</td>
<td><a href="#causal-perturbation-suite">Causal Perturbation Suite</a></td>
<td>Explains why comparison must include responses to changed conditions, not only output matching.</td>
</tr>
<tr>
<td>I want to know why thermodynamics matters here</td>
<td><a href="#thermodynamic-verification">Thermodynamic Verification Requirements</a></td>
<td>Explains why verification must cover not only information processing but also dissipation and energy constraints.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>If You Get Stuck On The Difference Between Missing, Unimplemented, And Incomplete</strong>
<p>
This page distinguishes among things that are already designed, things whose public operations are still unprepared, and things still lacking benchmark or audit support. If you want a one-page guide to those progress terms, see <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: Reading Partial Solutions, Exploratory Stages, And Unfinished Areas</a>.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck On What "Known / Unknown" Means</strong>
<p>
The known/unknown sections and accuracy assumptions at the top of this page mark the boundary of what can be asserted. If you want that logic organized as a site-wide reading rule, see <a href="wiki/known-unknown-and-status-reading.html">Wiki: How To Read "What Is Known / Not Yet Known"</a>.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck On How To Use The Header Guidance</strong>
<p>
Verification is a long blueprint, so it helps to use the top-of-page guidance blocks, how to read this page, who it is for, the accuracy assumptions, and the wiki route, to decide your reading scope before entering the main text. For that shared rule set, see <a href="wiki/page-header-reading-guide.html">Wiki: How To Read Public Page Headers</a>.
</p>
</div>
<div class="note-box">
<strong>If You Want The Next Page Chosen By Claim Level</strong>
<p>
Because this page is a blueprint for every level, the next page changes depending on whether you want L0 practical work, L3 closed-loop work, or L4 identity questions. For a one-page route map by level, see <a href="wiki/claim-level-reading-routes.html">Wiki: Reading Routes By L0-L5 Level</a>.
</p>
</div>
<div class="note-box">
<strong>If You Are Unsure About The Roles Of Practical Pages</strong>
<p>
Verification is the blueprint for success and falsification conditions. Entry datasets and the minimum L0 loop belong to <a href="datasets.html">Datasets and Hands-On Work</a>, reference examples belong to the <a href="#casework">Casework</a> section on this page, and proposal organization plus external dependency separation belong to the <a href="issue.html#proposal-integration">integrated proposal section of the Contribution Guide</a>. For a one-page guide to the practical pages only, see <a href="wiki/practical-pages-reading-guide.html">Wiki: Practical Page Reading Guide</a>.
</p>
</div>
<div class="note-box">
<strong>If You Want A Single Practical Route From EEG To L0</strong>
<p>
If you want one straight route from the EEG introduction, through public dataset selection and the L0 hands-on section inside Datasets, to checking on this page what was actually satisfied, see <a href="wiki/eeg-to-l0-route.html">Wiki: One Straight Route From EEG To L0</a>.
</p>
</div>
<div class="note-box">
<strong>If You Want To Choose The Next Single Page After This One</strong>
<p>
After reading Verification, if you want a one-page map of whether to return to L0 implementation, move to L2 intervention testing, examine L3 closed loops, or examine L4 identity, see <a href="wiki/verification-next-routes.html">Wiki: Four Routes After Verification</a>.
</p>
</div>
<div class="note-box">
<strong>If You Understand The Meaning But Are Unsure Whether You Can Act Next</strong>
<p>
If you want to separate "I read the summary" from "I checked the conditions and know where to make changes," see <a href="wiki/understanding-vs-action-readiness.html">Wiki: The Difference Between Understanding And Being Ready To Proceed</a>.
</p>
</div>

<section class="section" id="tldr">
<h2 class="section-title">TL;DR (For Human Readers)</h2>
<div class="key-points">
<h4>Remember Only These Three Things</h4>
<ul>
<li><strong>Metrics come before claims:</strong> if you do not fix what counts as progress, results cannot be compared.</li>
<li><strong>Data alone is still insufficient:</strong> standards, a shared repository, and evaluation benchmarks have to come together.</li>
<li><strong>WBE especially invites scope substitution:</strong> do not confuse decoding (correlation) with emulation (generation / causality).</li>
</ul>
</div>
</section>

<section class="section" id="definition">
<h2 class="section-title">The One Question This Site Tries To Solve</h2>
<p>
<strong>Question:</strong> Fix in advance what must be satisfied before we call something "progress," and build a state in which third parties can reach the same conclusion from the same inputs.
</p>
<div class="key-points">
<h4>Outcome</h4>
<ul>
<li><strong>Fix the win condition:</strong> state the Claim Ladder (L0-L5) explicitly and prevent scope substitution such as describing L1 as if it were L4.</li>
<li><strong>Provide reproducible inputs:</strong> standards such as BIDS plus metadata must let third parties receive and rerun the analysis target.</li>
<li><strong>Provide comparable outputs:</strong> publish an evaluation suite that includes scores, logs, and failure cases.</li>
<li><strong>Support continuous operation:</strong> accumulate public goods through benchmark updates, versioning, and audit logs.</li>
</ul>
</div>
</section>

<section class="section" id="claim-level-evidence">
<h2 class="section-title">Minimum Evidence Needed At Each Claim Level</h2>
<table class="data-table">
<thead>
<tr>
<th>Claim Level</th>
<th>Minimum Required Evidence</th>
<th>What Still Remains Insufficient</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong> Reproducible Analysis</td>
<td>The data, code, environment, and execution logs are all available, and a third party can reproduce the same result.</td>
<td>This alone cannot support strong claims about identity or consciousness.</td>
</tr>
<tr>
<td><strong>L1</strong> Decoding</td>
<td>Baseline comparisons, leakage checks, and reproducible accuracy under non-OOD conditions.</td>
<td>This still does not show internal causal structure or generative ability under unseen conditions.</td>
</tr>
<tr>
<td><strong>L2</strong> Generation And Intervention Prediction</td>
<td>Prediction agreement under unseen conditions, counterfactuals, and condition changes.</td>
<td>This still does not establish closed-loop stability or long-term operation.</td>
</tr>
<tr>
<td><strong>L3</strong> Closed Loop</td>
<td>Stability in real-time operation, latency management, and safe-stop conditions.</td>
<td>Even then, identity and rights questions still require separate verification.</td>
</tr>
<tr>
<td><strong>L4</strong> Identity</td>
<td>Preregistered continuity tests and branching checks for memory, values, and learning.</td>
<td>Full establishment at the level of social institutions and long-term governance is still a separate stage.</td>
</tr>
<tr>
<td><strong>L5</strong> Social deployment</td>
<td>Operational design including rights, consent, stop criteria, and audit structure.</td>
<td>A technical demo alone does not reach this stage.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>At L4, The Test Design Itself Is The Bottleneck</strong>
<p>
For identity claims, preregistering what is being treated as continuous matters more than merely reporting a high score. If you want a beginner guide to memory, values, learning, branching, and longitudinal continuity, see <a href="wiki/identity-and-continuity-tests.html">Wiki: Identity Evaluation and Continuity Tests</a>.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck At The L3 Entry Point</strong>
<p>
Closed-loop work needs more than offline accuracy. It also needs end-to-end latency, jitter, drift handling, and safety-stop design. For a beginner guide to that distinction, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed Loops, Latency, Jitter, and Safety Stops</a>.
</p>
</div>
</section>

<div class="note-box">
<strong>Check These Three Things Before Looking At Scores</strong>
<p>
Before reading L1 accuracy or L2 prediction agreement, check <strong>what unit train/test was split on</strong>, <strong>whether preprocessing or normalization looked at the test set</strong>, and <strong>whether the test set was reused for model selection</strong>. If those points are unclear, the evaluation foundation fails before claim level even becomes relevant. For the shortest beginner guide, see <a href="wiki/dataset-splits-and-leakage.html">Wiki: Data Splits and Leakage</a>.
</p>
</div>

<section class="section" id="non-goals">
<h2 class="section-title">What This Is Not</h2>
<div class="note-box">
<strong>Non-goals</strong>
<p>
This page is not where mind uploading is declared possible or impossible. What Mind-Upload is building is a <strong>verification substrate that can eventually justify such a claim</strong>, meaning the rules for measurement, evaluation, and falsification.
</p>
</div>
</section>

<section class="section" id="deliverables">
<h2 class="section-title">Deliverables Of The Mind-Upload Commons</h2>
<div class="note-box">
<strong>A School-Test Analogy</strong>
<p>
The roles of these four components become easier to see with a school-test analogy. The <strong>Data Standard</strong> is the same answer sheet, the <strong>Benchmark Suite</strong> is the same grading rubric, <strong>Registry &amp; Prereg</strong> is the set of rules distributed before the exam, and <strong>Leaderboard &amp; Model Cards</strong> is the report card that includes not only scores but also how the test was solved and where mistakes occurred.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck On The Difference Between Standards, Repositories, And Validators</strong>
<p>
BIDS, OpenNeuro, PhysioNet, the BIDS Validator, and benchmarks are all parts of research infrastructure, but they do different jobs. For a beginner explanation of that division of labor, see <a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: Standards, Repositories, Validators, and Benchmarks</a>.
</p>
</div>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Data Standard</h4>
<p>Build a shareable standard, based on BIDS/EEG-BIDS, that extends metadata for tasks, stimuli, synchronization, QC, and anonymization into a form that remains analyzable by others.</p>
<div class="tag-list">
<span class="tag">BIDS</span><span class="tag">EEG</span><span class="tag">Metadata</span><span class="tag">QC</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Benchmark Suite</h4>
<p>Define tasks that cover not only decoding correlations but also <strong>counterfactual / intervention prediction</strong> and <strong>closed-loop stability</strong>, so results can be compared against the same ruler.</p>
<div class="tag-list">
<span class="tag">Counterfactual</span><span class="tag">Intervention</span><span class="tag">Closed-loop</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">03</div>
<div class="stage-body">
<h4>Registry &amp; Prereg</h4>
<p>Preregister experiments and analysis plans so exploration and verification stay separated. Submit templated assumptions, evaluation metrics, and stop conditions first, then append update diffs to the review log to reduce reporting bias.</p>
<div class="tag-list">
<span class="tag">Preregistration</span><span class="tag">Protocol</span><span class="tag">Audit</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">04</div>
<div class="stage-body">
<h4>Leaderboard &amp; Model Cards</h4>
<p>Publish not only scores but also leakage countermeasures, failure cases, compute usage, known weaknesses, and, for L1 and above, an <strong>Observability Budget</strong> that states <strong>what was directly observed and what remains latent state</strong>, so reproducibility and safety are preserved.</p>
<div class="tag-list">
<span class="tag">Leaderboard</span><span class="tag">Reproducibility</span><span class="tag">Safety</span>
</div>
</div>
</div>
</div>
<div class="note-box">
<strong>If You Get Stuck On Updates, Branching, And Stop Rules</strong>
<p>
Even with a registry in place, it is easy to get stuck on how much updating to allow, how to log branches, and how to distinguish stop rules from kill switches. For a beginner guide to those issues, see <a href="wiki/update-branching-and-stop-rules.html">Wiki: Update, Branching, and Stop Rules</a>.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Missing Component</th>
<th>What Breaks Without It</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No Data Standard</strong></td>
<td>Input formats and conditions drift apart, making it hard to tell whether two groups are even solving the same task.</td>
</tr>
<tr>
<td><strong>No Benchmark Suite</strong></td>
<td>Each group uses a different ruler, so even a claimed win cannot be judged as genuine progress.</td>
</tr>
<tr>
<td><strong>No Registry &amp; Prereg</strong></td>
<td>People can choose favorable metrics and conditions after the fact, blurring the line between failure and success.</td>
</tr>
<tr>
<td><strong>No Leaderboard &amp; Model Cards</strong></td>
<td>Scores travel alone while leakage, weaknesses, and missing reproduction steps are too easily overlooked.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Raw EEG Alone Is Not A Data Standard</strong>
<p>
Comparable inputs require more than waveform files. They also need <strong>event markers</strong>, <strong>stimulus logs</strong>, <strong>time synchronization</strong>, and records of <strong>bad channels / bad segments</strong>. If those remain ambiguous, later replication of the same task becomes impossible. For a beginner guide, see <a href="wiki/event-sync-and-measurement-logs.html">Wiki: Event Synchronization and Measurement Logs</a>.
</p>
</div>
</section>

<section class="section" id="example">
<h2 class="section-title">Example: What One Comparable Advance Looks Like</h2>
<p>If the example is "a model that estimates state from EEG," the commons needs the following four components.</p>
<table class="data-table">
<thead>
<tr>
<th>Component</th>
<th>Minimum Contents (Example)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Input (Data)</strong></td>
<td>A BIDS-compliant data package, measurement conditions, sync logs, QC logs, and the scope of anonymization/consent</td>
</tr>
<tr>
<td><strong>Procedure (Code / Protocol)</strong></td>
<td>A fixed recipe for preprocessing -> features -> training -> evaluation, plus environment info and random seeds</td>
</tr>
<tr>
<td><strong>Output (Metrics)</strong></td>
<td>Scores for accuracy / uncertainty / robustness, failure cases, and deltas from baselines</td>
</tr>
<tr>
<td><strong>Falsification</strong></td>
<td>Leakage checks, counterfactual tests, and logs of prediction failures when stimulus conditions change</td>
</tr>
</tbody>
</table>
<p>Once these are aligned, comparison becomes possible under the same conditions regardless of who runs the work, and only then can progress accumulate honestly.</p>

<div class="note-box">
<strong>If This Still Feels Too Abstract, Use The Walkthrough</strong>
<p>
If you want to see how these four elements actually fit together in a small EEG example, step by step, see <a href="wiki/verification-example-walkthrough.html">Wiki: Verification Example Walkthrough</a>. The public page keeps the blueprint concise, while the tutorial material lives on the wiki side.
</p>
</div>
<div class="note-box">
<strong>If You Want Only The Minimum L0 Artifact Set First</strong>
<p>
This page is the blueprint for the full public-good stack. If you want the shortest path to a single pack containing BIDS, the Validator, QC, splits, baselines, execution steps, and failure cases, see <a href="wiki/l0-minimum-artifact-pack.html">Wiki: Minimum Artifact Pack For L0</a>.
</p>
</div>
<div class="note-box">
<strong>At L1 And Above, "What Was Directly Observed" Is Part Of The Artifact</strong>
<p>
The weakness exposed in this re-audit was that even when hidden states were listed, the artifact still did not fix <strong>which measurement stack directly observed which variables</strong>. Accordingly, for results at L1 and above, we attach an <a href="#observability-budget">Observability Budget</a> in addition to the standard model card, including the claim ceiling and abstention conditions.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck On Operational Terms</strong>
<p>
Baselines, benchmarks, preregistration, model cards, and failure cases all matter, but they do not play the same role. If you want that difference organized from the ground up, see <a href="wiki/baselines-prereg-and-model-cards.html">Wiki: Baselines, Preregistration, and Model Cards</a>.
</p>
</div>
</section>

<div class="note-box">
<strong>If You Get Stuck On Uncertainty Or Causal Equivalence Classes</strong>
<p>
In Verification, estimates derived from observed signals are not treated as the single truth by default. If you want the relationships among inverse problems, ESI, DCM, SCM, and causal equivalence classes organized first, see <a href="wiki/observation-to-estimation.html">Wiki: From Observation To Estimation</a>. If you also want point estimates, intervals, and abstention under low confidence, see <a href="wiki/uncertainty-confidence-and-abstention.html">Wiki: Uncertainty, Calibration, and Abstention</a>.
</p>
</div>

<section class="section" id="casework">
<h2 class="section-title">Designs Borrowed From Historical Casework</h2>
<p>
The design of Mind-Upload is not a "new invention" but a transfer of verification patterns that other fields have already worked out. The key points from the former <code>casework.md</code> have been integrated into this section so they can be compared directly here.
</p>
<div class="note-box">
<strong>How To Transfer A Pattern Correctly</strong>
<p>
Patterns such as PDB (a single archive), BIDS plus OpenNeuro (standard plus repository), PhysioNet (data plus evaluation), and OSF/PROSPERO (preregistration) create structures in which progress can be measured even across different fields. WBE especially requires <strong>success conditions</strong> and <strong>falsification conditions</strong> to be fixed in advance.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Prior Pattern</th>
<th>Problem Solved In That Field</th>
<th>Design Borrowed By Mind-Upload</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PDB / INSDC</strong></td>
<td>It reduced the problem of references being scattered, where comparison breaks even when people think they are looking at the same data.</td>
<td>We place a single reference source, stable IDs, version control, and minimum submission-time validation first.</td>
</tr>
<tr>
<td><strong>BIDS + OpenNeuro</strong></td>
<td>It reduced the problem that differences in brain-measurement formats and missing metadata made replication difficult.</td>
<td>We design BIDS and the sharing platform as one package rather than separating "how to store it" from "where to store it."</td>
</tr>
<tr>
<td><strong>PhysioNet / ImageNet / MLPerf</strong></td>
<td>It reduced the problem that tasks and metrics were inconsistent, making year-over-year comparison of progress impossible.</td>
<td>We fix baselines, submission formats, comparison metrics, and leakage audits so improvement can be measured.</td>
</tr>
<tr>
<td><strong>OSF / PROSPERO</strong></td>
<td>It reduced the problem that exploration and verification were mixed together and only favorable reports survived.</td>
<td>We preserve preregistration, stop conditions, failure cases, and reasons for deferral as part of the artifact set.</td>
</tr>
<tr>
<td><strong>W3C / IETF / Unicode</strong></td>
<td>It reduced the problem that separate systems would not connect and would fail through semantic mismatch.</td>
<td>We align terminology, metadata vocabularies, synchronization logs, and audit vocabularies for interoperability first.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Why We Do Not Copy Historical Cases Unchanged</strong>
<p>
WBE includes strong issues such as identity and causal equivalence, so it is not completed by data sharing alone. Even so, the ordering itself, putting standards, repositories, benchmarks, registration, and audit in place first, can be borrowed quite strongly from successful cases in other fields.
</p>
</div>
</section>

<section class="section" id="current-status">
<h2 class="section-title">Implementation Status (Transparency Report)</h2>
<div class="note-box">
<strong>The Frank Current State</strong>
<p>
For scientific integrity, we state the current implementation status of each deliverable explicitly. Please do not confuse "the design document is complete" with "the implementation is complete."
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Deliverable</th>
<th>Design Status</th>
<th>Implementation Status</th>
<th>Next Step</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard</strong></td>
<td>The BIDS/EEG-BIDS-compatible extension specification has been documented.</td>
<td>No sample dataset has been published yet. The validator is not implemented.</td>
<td>Publish a BIDS conversion pipeline and validation scripts for one dataset.</td>
</tr>
<tr>
<td><strong>Benchmark Suite</strong></td>
<td>The task definitions and metric definitions have been documented.</td>
<td>The benchmark code and baseline results are not yet public.</td>
<td>Implement and publish one minimum L0/L1 benchmark set.</td>
</tr>
<tr>
<td><strong>Registry & Prereg</strong></td>
<td>The template design is complete.</td>
<td>The registration system has not been built. Only the template is documented.</td>
<td>Build a lightweight registration flow through OSF integration or GitHub Issues.</td>
</tr>
<tr>
<td><strong>Leaderboard</strong></td>
<td>The Model Card format has been defined.</td>
<td>There is no entry yet based on real data.</td>
<td>Register the first entry after the benchmark implementation exists.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="gap-analysis">
<h2 class="section-title">Scientific Gap Analysis</h2>
<p>
For the Verification Commons to contribute to science, it must recognize the following gaps and address them as priorities.
</p>
<div class="key-points">
<h4>Priority Gaps To Address</h4>
<ul>
<li><strong>Realizing L0:</strong> the first priority is a state in which third parties can assemble the code, data, and environment and reproduce the same result. At present, no repository contains the full set of components required for that.</li>
<li><strong>Operationalizing counterfactual tests:</strong> "counterfactual" and "intervention prediction" are defined conceptually, but their concrete experimental test procedures remain unsettled.</li>
<li><strong>Connecting to existing benchmarks:</strong> compatibility and differences relative to benchmarks such as the BCI Competition and MOABB must be made explicit to avoid reinventing the wheel.</li>
<li><strong>Systematizing failure cases:</strong> the Commons design includes collecting and publishing negative results, but the incentive design for collecting them has not yet been built.</li>
</ul>
</div>
</section>

<section class="section" id="observability-budget">
<h2 class="section-title">2026-03 Addendum: Make Observability Budget a required submission</h2>
<p>
The most important update in this pass is that the criticism that ``important hidden state remains'' has finally been translated into <strong>submission format</strong>. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">Yao et al. (2023)</a> show that whole-brain atlases strengthen cell-type taxonomy and spatial arrangement, but do not directly provide current state. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> greatly advance same-brain structure-function links, but still remain in the domain of local conditional prediction. Furthermore, as <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> and <a href="https://doi.org/10.1007/s00415-025-12886-9" target="_blank">Hao et al. (2025)</a> show, even externally validated HD-EEG / ESI remains dependent on source depth and head model and does not provide a generally unique restoration. Therefore, this site requires an <strong>Observability Budget</strong> for submissions above L1 so that they first state what was directly observed and what remains estimated.
</p>
<table class="data-table">
<thead>
<tr>
<th>Observability Budget column</th>
<th>Minimum things to write</th>
<th>What happens without this</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>measurement stack</strong></td>
<td>Whether you used EEG / MEG / fMRI, whole-brain atlas, Patch-seq, volume EM, same-brain function, local transmitter / glia imaging. </td>
<td>Only the words "multimodal," "atlas," and "same-brain" take on a life of their own, and the differences in direct observable quantities disappear. </td>
</tr>
<tr>
<td><strong>direct observables</strong></td>
<td>Write only the variables directly measured by the stack. BOLD / HbO / HbR, field potential, cell-type label, EM synapse, local ACh dynamics, etc. </td>
<td>It is easy to misread the estimated latent state as if it had been observed from the beginning. </td>
</tr>
<tr>
<td><strong>remaining latent state</strong></td>
<td>List the remaining variables, including weights, local proteostasis / synaptic-tagging state, perisynaptic ECM / PNN state, ionic milieu / chloride homeostasis, delay/myelin, intrinsic excitability/homeostatic set point, neuromodulation, glia/metabolic support, sleep-history, and, for hemodynamic stacks, unresolved vascular transfer state such as baseline vascular state / CVR or superficial systemic contamination. </td>
<td>It is easier to roll up non-state-complete results to emulation-complete or internal state unique solutions. </td>
</tr>
<tr>
<td><strong>external calibration route</strong></td>
<td>Write external validation pathways such as phantom, intracranial stimulation, concurrent invasive recording, same-brain co-registration, and Patch-seq bridge. </td>
<td>It is easy to confuse improvements in accuracy and visualization with getting closer to the ground truth. </td>
</tr>
<tr>
<td><strong>validity horizon</strong></td>
<td>Write how far within-session, cross-state, cross-day, perturbation, and recovery have been verified. </td>
<td>It is easier to unduly extend same-day fit into long-term stability or memory claims. </td>
</tr>
<tr>
<td><strong>claim ceiling and abstention</strong></td>
<td>Write the upper limits that the results can reach, such as "macro state tracking," "structural scaffold," and "local conditional prediction," as well as the conditions under which you will quit if they exceed them. </td>
<td>It is easy to overtranslate the advancement of the paper and falsely promote L1 results to L2/L3/L4. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-18 addendum: hemodynamic modalities need a vascular-state / CVR audit</strong>
<p>
Hemodynamic stacks do not carry only neural uncertainty; they also carry a <strong>vascular transfer state</strong>. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> showed that inter-subject CBF / CBV differences contribute to BOLD reactivity and that breath-hold-derived vascular-reactivity covariates improve group analyses. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> showed that task BOLD magnitude is strongly predicted by hypercapnia-based CVR across multiple cortical regions, <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> showed that baseline CBF partly explains age-related components of multiple-demand-network BOLD responses, <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015)</a> showed that short-separation regression is required to reduce superficial autonomic confounds in fNIRS, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that about 40% of voxels with significant task BOLD changes can show opposite oxygen-metabolism changes. Therefore, when a submission uses BOLD or fNIRS amplitude to argue a group difference, longitudinal change, or multimodal fusion result, this site asks authors to disclose a <strong>vascular-state / CVR calibration route</strong> or to abstain and write the result as a <strong>hemodynamic-limited difference</strong> rather than a neural difference.
</p>
</div>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this card is missing, this site treats the result as <strong>L0/L1 reproducible analysis or limited decode</strong> and does not promote it to L2 or above. For example, the default ceiling is <strong>macro-state tracking</strong> for <strong>EEG / HD-EEG + MRI only</strong>, <strong>an implant-region local population window</strong> for <strong>high-density extracellular probe only</strong>, <strong>structural scaffold</strong> for <strong>volume EM only</strong>, <strong>molecular / spatial prior</strong> for <strong>whole-brain atlas only</strong>, and still only <strong>local conditional prediction</strong> even for <strong>same-brain calcium + EM</strong>. For hemodynamic modalities, a group or cross-day BOLD / fNIRS difference without <strong>vascular-state / CVR</strong> or <strong>short-separation / superficial-bias</strong> audit is not accepted here as a neural difference. If a chronic-probe result lacks a unit-identity audit, single-unit longitudinal claims are not accepted. Detailed stack-specific ceilings and the <strong>state variable × timescale</strong> matrix are summarized in <a href="wiki/measurement-stack-and-claim-ceiling.html#state-variable-matrix">Wiki: observability and claim ceiling by measurement stack</a>.
</p>
</div>
</section>

<section class="section" id="latent-state-error-budget">
<h2 class="section-title">Latent-state error budget</h2>
<p>
The <strong>Observability Budget</strong> fixes what entered the sensor and what was directly measured. The next question is different: <strong>which still-unobserved variables dominate the remaining error and stop the claim from being raised?</strong> This site therefore asks L2 and above submissions to disclose a <strong>latent-state error budget</strong> rather than only saying that "important hidden state remains." The purpose is to separate <strong>connectome-only or sensor-only limits</strong> from <strong>augmentation claims</strong>, and to show which omitted state family still blocks the current ceiling.
</p>
<table class="data-table">
<thead>
<tr>
<th>Latent-state family</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if still latent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Current synaptic efficacy / short-term state</strong></td>
<td>Write whether current weights, release probability, receptor occupancy, or short-term state were directly measured, externally calibrated, modeled from proxy, or left latent.</td>
<td>Mechanistic intervention prediction, closed-loop stability, and timing-sensitive reconstruction are demoted back toward structural or correlational claims.</td>
</tr>
<tr>
<td><strong>Intrinsic excitability / homeostatic controller</strong></td>
<td>Separate relative excitability for allocation, AIS / channel state, and recovery controller, and disclose which parts were measured versus only inferred.</td>
<td>Cross-day stability, memory-allocation, and perturbation-recovery claims stay provisional.</td>
</tr>
<tr>
<td><strong>Activity-dependent transcription / chromatin state</strong></td>
<td>Disclose whether current transcriptional / chromatin state was time-stamped, causally perturbed, externally calibrated, or replaced by a static atlas / DEG clue.</td>
<td>Allocation eligibility, late stabilization, and locus-specific plasticity-control claims remain latent.</td>
</tr>
<tr>
<td><strong>Local proteostasis / synaptic-tagging route</strong></td>
<td>State whether tag / PRP capture, branch-local translation-degradation balance, autophagy, or branch-local proxy was observed or only assumed.</td>
<td>Late stabilization, reconsolidation, and cross-event capture do not become closed mechanisms.</td>
</tr>
<tr>
<td><strong>Ionic milieu / chloride homeostasis</strong></td>
<td>Disclose whether chloride set point, transporter state, extracellular K<sup>+</sup> / Ca<sup>2+</sup> / pH composition, or an externally calibrated ionic proxy was measured, perturbed, or left latent.</td>
<td>Inhibitory polarity, rhythm stability, and state-transition claims stay provisional or fall back to coarse excitability proxies.</td>
</tr>
<tr>
<td><strong>Timing-state / conduction support</strong></td>
<td>Separate device latency from biological timing-state, and disclose whether timing variables were measured, externally calibrated, absorbed into a constant, or left latent.</td>
<td>Phase, synchrony, and timing-complete reconstruction claims are demoted to hardware-fast or macro-timing proxy claims.</td>
</tr>
<tr>
<td><strong>Neuromodulatory specificity</strong></td>
<td>Disclose whether the route was a mixed arousal proxy, local axon / transmitter sensor, receptor / transporter atlas, occupancy PET, or release-sensitive displacement PET; then report receptor family, ligand / challenge, temporal window, spatial scope, and abstention boundary.</td>
<td>Momentary whole-brain transmitter-field, receptor-family-complete internal-state, and lamina- or cell-specific modulatory-effect claims fall back to coarse covariate, regional prior, or challenge-limited proxy claims.</td>
</tr>
<tr>
<td><strong>Glial / slow-state support</strong></td>
<td>Disclose whether astrocyte / glial / slow-state variables were measured, causally perturbed, externally calibrated, or left latent, together with species and timescale limits.</td>
<td>Long-horizon plasticity and multiday stabilization claims remain partial-model claims.</td>
</tr>
<tr>
<td><strong>Chronic unit identity</strong></td>
<td>For chronic invasive work, report whether unit matching, tissue response, and interface drift were separately audited.</td>
<td>Single-unit longitudinal and chronic closed-loop claims are not accepted as stable identity claims.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>How to use this budget on this site</strong>
<p>
The latent-state error budget is not a second abstract. It is a <strong>submission-side stop-rule table</strong>. If a paper adds one extra evidence layer, such as transcriptomics, SV2A PET, receptor / transporter atlas priors, occupancy or displacement PET, myelin imaging, or a glial perturbation, it should say <strong>which error term that layer reduces under the same held-out condition</strong> and which latent families remain untouched. This is the site-wide rule behind the augmentation / ablation logic in <a href="#state-completeness-gate">State variable integrity gate</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: neuromodulation is a ladder, not one proxy</strong>
<p>
On this site, <strong>mixed arousal proxy</strong>, <strong>local transmitter sensor</strong>, <strong>receptor / transporter atlas</strong>, and <strong>occupancy or displacement PET</strong> are not treated as equivalent. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> showed that pupil fluctuations track both adrenergic and cholinergic activity, <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> showed that local cortical ACh depends on axon activity and local clearance, <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> and <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">Goulas et al. (2021)</a> showed that receptor maps are structured regional priors, and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a> plus <a href="https://doi.org/10.1038/s41467-019-09897-z" target="_blank">Lippert et al. (2019)</a> showed that raclopride PET gives task- and window-limited dopamine-release proxy. Therefore, a result must say which rung it used before any claim ceiling is raised.
</p>
</div>
</section>

<section class="section" id="maintenance-state-error-budget">
<h2 class="section-title">Maintenance-state error budget</h2>
<p>
Cross-day and remote-memory claims fail for a different reason than same-session decoding claims. Even when short-term performance holds, the result may still leave the <strong>maintenance route</strong> almost completely latent. This site therefore asks cross-day, recovery, reconsolidation, or remote-memory submissions to disclose a <strong>maintenance-state error budget</strong> that keeps controller state, sleep history, timing support, thermal-state, bioenergetic / mitochondrial support, glial / astrocyte support, and other multiday support-state proxies separate.
</p>
<table class="data-table">
<thead>
<tr>
<th>Maintenance-state field</th>
<th>Minimum disclosure</th>
<th>Ceiling if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Controller state</strong></td>
<td>State whether relative excitability, homeostatic return target, or allocation-related controller variables were measured, perturbed, externally calibrated, or left latent.</td>
<td>Same-day fit does not become maintenance-consistent or memory-allocation-consistent.</td>
</tr>
<tr>
<td><strong>Sleep / wake history</strong></td>
<td>Report sleep / wake interval, deprivation, nap / recovery condition, and the time window over which renormalization was or was not checked.</td>
<td>Cross-day hold is not promoted to overnight maintenance or post-learning re-equilibration.</td>
</tr>
<tr>
<td><strong>Timing support</strong></td>
<td>Separate hardware latency from tissue-side timing support such as myelin / conduction proxy or externally calibrated timing-state.</td>
<td>Hardware-fast remains hardware-fast; it does not become timing-complete maintenance evidence.</td>
</tr>
<tr>
<td><strong>Thermal-state</strong></td>
<td>Report whether brain temperature, heating / cooling logs, MRS thermometry, or other thermal covariates were measured, externally calibrated, held fixed, or left latent.</td>
<td>Field-potential amplitude, membrane-kinetic, and sequence-timing claims are not promoted to thermal-state-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Ionic / chloride state</strong></td>
<td>Report whether chloride-related or ionic-state variables were directly measured, causally perturbed, approximated by sodium / macro ionic proxy, or left latent.</td>
<td>Cross-day or recovery success is not promoted to inhibitory-polarity-consistent or state-transition-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Bioenergetic / mitochondrial support</strong></td>
<td>Disclose whether 31P-MRS, dynamic DMRSI, fatigue / repeated-burst logs, or other energetic proxies were available, and what local ATP reserve, mitochondrial positioning, fission/fusion, or redox variables remained latent.</td>
<td>Repeated-stimulation reliability and energetic mechanisms of dendritic plasticity remain provisional.</td>
</tr>
<tr>
<td><strong>Glial / astrocyte support</strong></td>
<td>Write whether glial or astrocyte variables were directly measured, causally perturbed, approximated by macro proxies, or left latent.</td>
<td>Memory retrieval, multiday stabilization, and slow-state support remain partial-model claims.</td>
</tr>
<tr>
<td><strong>Clearance / immune support</strong></td>
<td>Report CSF / glymphatic / immune-related measurements, what part was a macro proxy, and what cell-specific clearance controller remained unobserved.</td>
<td>Multiday recovery and protein-clearance claims remain support-proxy claims rather than local maintenance-state claims.</td>
</tr>
<tr>
<td><strong>Human evidence class / observability ceiling</strong></td>
<td>Label each human-side route as <strong>structural scaffold</strong>, <strong>regional density proxy</strong>, <strong>macro biochemical / energetic / ionic / thermal / myelin / support proxy</strong>, or <strong>perturbation-conditioned proxy</strong>, and state which local hidden states still remain.</td>
<td>Human proxy bundles are not promoted to state-complete maintenance snapshots.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Do not collapse energetic support into glial support</strong>
<p>
<a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">Rangaraju et al. (2014)</a>, <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">Rangaraju et al. (2019)</a>, <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">Divakaruni et al. (2018)</a>, <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">Bapat et al. (2024)</a>, and <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">Hu et al. (2025)</a> support a narrower rule: local ATP supply, mitochondrial positioning, and energetic micro-organization can change repeated-burst reliability and dendritic plasticity even before one asks whether astrocyte or clearance-state matched. Conversely, human <a href="https://doi.org/10.1002/nbm.3384" target="_blank">31P-MRS (Ren et al., 2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">dynamic DMRSI (Li et al., 2025)</a> remain macro energetic proxies rather than direct readouts of branch-local mitochondrial state. This site therefore records energetic route and glial route separately.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: thermal-state is not a background constant</strong>
<p>
<a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">Hardingham &amp; Larkman (1998)</a> showed that excitatory-transmission reliability in rat visual cortex is temperature dependent, <a href="https://doi.org/10.1111/j.1469-7793.2000.00059.x" target="_blank">Volgushev et al. (2000)</a> showed that reversible cooling changes membrane properties and spike generation, <a href="https://doi.org/10.1126/science.8446900" target="_blank">Moser et al. (1993)</a> showed that dentate field potentials can track brain temperature strongly enough to mask learning-specific change, and <a href="https://doi.org/10.1038/nature07448" target="_blank">Long &amp; Fee (2008)</a> showed that local cooling dilates neural-sequence timing. Healthy-human <a href="https://doi.org/10.1093/brain/awab466" target="_blank">MRS thermometry (Rzechorzek et al., 2022)</a> is therefore treated here as a <strong>macro thermal proxy</strong>, not as cell-specific thermal-state ground truth. This site records thermal-state separately whenever amplitude, timing, or repeated-state interpretation depends on it.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: human maintenance evidence must be class-labeled</strong>
<p>
On this site, <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#human-observability-ceiling">Wiki: Homeostatic plasticity and maintenance-state</a> now distinguishes <strong>fixed-tissue structural scaffold</strong>, <strong>regional synaptic-density proxy</strong>, <strong>macro-biochemical scaffold</strong>, <strong>macro energetic proxy</strong>, <strong>macro ionic proxy</strong>, <strong>macro thermal proxy</strong>, <strong>macro-myelin proxy</strong>, <strong>perturbation-conditioned plasticity proxy</strong>, and <strong>macro support-state proxy</strong>. Human-side evidence is therefore not submitted as one generic “maintenance signal.” Each route must be class-labeled before the claim ceiling is interpreted.
</p>
</div>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this budget is missing, this site allows at most <strong>same-session fit</strong>, <strong>cross-day performance with unresolved maintenance route</strong>, or <strong>support-proxy-aligned evidence</strong>. It does not promote the result to <strong>maintenance-consistent</strong>, <strong>reconsolidation-consistent</strong>, or <strong>remote-memory-relevant</strong>. In particular, if <strong>sleep / wake history</strong>, <strong>timing support</strong>, <strong>thermal-state</strong>, <strong>ionic / chloride state</strong>, <strong>bioenergetic support</strong>, <strong>glial / astrocyte support</strong>, and <strong>clearance / immune proxy class</strong> are all absent, this site stops the reader from rephrasing a temporal hold as long-horizon maintenance evidence.
</p>
</div>
</section>

<section class="section" id="specificity-shortcut-card">
<h2 class="section-title">2026-03 addendum: attach a Specificity &amp; Shortcut Card to decode / biomarker results</h2>
<p>
The weakness that became clearer in the re-audit was that the <strong>Observability Budget</strong> can say what entered the sensor, but by itself it cannot fix whether predictive information came from the <strong>target neural variable</strong> or from shortcut routes such as eye movement, EMG, uninstructed movement, report paths, auditory feedback, subject / session fingerprint, or acquisition-distribution cues carried by site / device / reference / electrode layout. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> showed that neural dynamics during task can be strongly dominated by uninstructed movements, <a href="https://doi.org/10.1523/ENEURO.0401-17.2018" target="_blank">Mostert et al. (2018)</a> showed that visual-working-memory decode can retain an eye-movement confound even under attempted fixation, <a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">Muthukumaraswamy (2013)</a> summarized the overlap between high-frequency EEG/MEG and muscle artifact, <a href="https://doi.org/10.1088/1741-2560/2/4/014" target="_blank">McFarland et al. (2005)</a> showed that EMG can boost early BCI-session performance, and <a href="https://doi.org/10.1038/s42256-024-00837-5" target="_blank">Chen et al. (2024)</a> showed that post-onset auditory feedback can inflate offline speech-decoding scores. For that reason, this site now requires an independent deliverable that fixes not only <strong>"there is information"</strong> but also <strong>"which route that information came from."</strong>
</p>
<table class="data-table">
<thead>
<tr>
<th>Specificity &amp; Shortcut Card field</th>
<th>What must be written at minimum</th>
<th>What goes wrong if it is omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>target variable / intended causal path</strong></td>
<td>Fix in one line what you want to read, such as motor intention, stimulus category, memory content, state marker, or speech intent, together with the intended signal path.</td>
<td>Task labels, behavioral output, device state, or session fingerprint become easy to confuse with the target neural variable.</td>
</tr>
<tr>
<td><strong>plausible nuisance routes</strong></td>
<td>List the main alternative routes, such as EOG, facial / jaw / neck EMG, button press, posture / body movement, speech motor output, auditory feedback, report path, cue timing, and acquisition-distribution cues such as device / impedance / session fingerprint, reference system, electrode layout, and protocol differences.</td>
<td>The explanation of a high score collapses to one favored story and the shortcut hypothesis cannot be audited later.</td>
</tr>
<tr>
<td><strong>nuisance observables / auxiliary channels</strong></td>
<td>State whether EOG / EMG, audio, video / motion capture, button / force, pupil / gaze, impedance / hardware logs, channel-map / reference / sample-rate / filter logs, and stimulus / feedback logs exist and how they are used.</td>
<td>The paper can stop at saying it "paid attention" to nuisances without leaving measured audit traces behind.</td>
</tr>
<tr>
<td><strong>nuisance-only / nuisance-matched baselines</strong></td>
<td>Report which of EOG-only, EMG-only, video / behavior-only, audio-only, no-brain, LM-only, feedback-on/off, time-shuffle, or label-preserving nuisance-match baselines were used.</td>
<td>You cannot separate prediction gain coming from target-neural information from gain that can be reproduced by auxiliary routes alone.</td>
</tr>
<tr>
<td><strong>fingerprint / acquisition-distribution audit / independence unit</strong></td>
<td>Report raw-recording ancestry, whether windows / epochs cut from the same recording ever cross train/test, subject / session / site / device / reference-system / electrode-layout disjointness, metadata-only baselines, harmonization logs, and identity classifiers.</td>
<td>A diagnosis or state-decode score can be driven only by who, when, where, or under which recording setup the data was acquired, and that failure would remain invisible.</td>
</tr>
<tr>
<td><strong>slice-wise hold-out across nuisance regimes</strong></td>
<td>Report whether evaluation was split across low/high movement, fixed gaze/free viewing, silent/overt, feedback on/off, device/session/subject/reference/protocol hold-out, artifact-burden slices, and state slices.</td>
<td>In-distribution success is too easily misread as target-specific evidence that survives when nuisance conditions change.</td>
</tr>
<tr>
<td><strong>countermeasure / perturbation check</strong></td>
<td>Report whether fixation enforcement, EMG suppression, masking / sham, feedback removal, cue scrambling, behavior-matched controls, or dedicated countermeasure tasks were used to break shortcut routes.</td>
<td>Even when the same output can be reproduced through a different route, the reader may still leap to the target-causal interpretation.</td>
</tr>
<tr>
<td><strong>residual shortcut gap / claim ceiling</strong></td>
<td>Fix in one line which nuisance routes remain unaudited, what shortcut possibilities still remain, and which ceiling this result is allowed to reach.</td>
<td>Exploratory decode or behavior-linked biomarkers are too easily mispromoted to target-specific neural readouts or mechanistic markers.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-18 addendum: subject / session fingerprint is an independent shortcut family</strong>
<p>
<a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> showed that diagnostic learning can absorb subject characteristics when repeated measures are not participant-disjoint, while <a href="https://doi.org/10.1016/j.patcog.2020.107381" target="_blank">Wang et al. (2020)</a> and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> showed that resting-state EEG alone can support accurate, time-robust person identification. <a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">Gibson et al. (2022)</a> further summarized strong subject-driven components in EEG variability. For that reason, this site treats subject / session fingerprint as a shortcut family on the same level as movement or EMG, and fixes <strong>independence unit</strong> plus <strong>metadata-only baselines</strong> as separate required fields.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: acquisition-distribution shortcut is also independent</strong>
<p>
<a href="https://doi.org/10.1088/1741-2552/aacfe4" target="_blank">Hu et al. (2018)</a> showed that reference montage and electrode setup alter the measured scalp potential itself, <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017)</a> showed that EEG differences arise from system as well as subject and session, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a> showed that cross-dataset EEG decoding is degraded by environmental variability such as amplifier, cap, sampling rate, and filtering, and <a href="https://doi.org/10.1016/j.brainresbull.2024.110906" target="_blank">Dong et al. (2024)</a> showed that comparative work across different channel locations needs explicit harmonization. For that reason, this site treats <strong>site / device / reference system / electrode layout / protocol distribution</strong> as a shortcut family on the same level as subject fingerprint, and requires <strong>setup disjointness</strong> plus <strong>harmonization logs</strong> as independent deliverables.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: the Neural Contribution Card is the language-specific version of this general card</strong>
<p>
The Specificity &amp; Shortcut Card is the general form that covers motor, memory, biomarker, speech, and related decode settings. The <a href="#neural-contribution-card">Neural Contribution Card</a> is its language-specific specialization for text / speech / generative reconstruction settings, where <strong>language priors, candidate sets, prompts, vocoders, and causal deployment guards</strong> become dominant. In speech / brain-to-text work, the general shortcut audit is therefore stacked together with the Neural Contribution Card.
</p>
</div>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this card is missing, this site treats the result by default as <strong>exploratory decode</strong>, <strong>behavior-linked biomarker</strong>, or <strong>nuisance-unresolved classification</strong>, and does not promote it to a target-specific neural readout, mechanistic biomarker, or deployable controller. In particular, if any of <strong>plausible nuisance routes</strong>, <strong>nuisance-only baselines</strong>, <strong>fingerprint / acquisition-distribution audit / independence unit</strong>, or <strong>slice-wise hold-out</strong> is missing, this site stops the reader from rephrasing the result as "we learned what this variable means."
</p>
</div>
<div class="note-box">
<strong>How this differs from the existing cards</strong>
<p>
The Observability Budget fixes <strong>what was directly observed</strong>. The Specificity &amp; Shortcut Card fixes <strong>which route the predictive information came from</strong>. The Temporal Validity Card fixes <strong>how far the result can be extrapolated across time</strong>, the Calibration &amp; Abstention Card fixes <strong>what confidence and fallback mean</strong>, and the Intervention Card fixes <strong>what was actually changed</strong>. On this site, decode / biomarker results therefore submit shortcut audit separately instead of mixing "the sensor contains information" with "the information is target-specific."
</p>
</div>
</section>

<section class="section" id="state-completeness-gate">
<h2 class="section-title">State variable integrity gate</h2>
<p>
In our March 2026 primary-literature audit, we reconfirmed that there are at least ten loose state classes between <strong>“having a wiring diagram”</strong> and <strong>“being able to behave generatively”</strong>. In addition to cell types, synapses, delays, neuromodulation, and glia, we now also treat <strong>activity-dependent transcription / chromatin state</strong>, <strong>intrinsic excitability / homeostatic set points</strong>, <strong>local proteostasis / synaptic-tagging state</strong>, <strong>perisynaptic ECM / PNN state</strong>, and <strong>ionic milieu / chloride homeostasis</strong> as independent classes. Therefore, on this site, we do not accept <strong>edge-list submissions alone</strong> as a condition for passing L2 or above.
</p>
<table class="data-table">
<thead>
<tr>
<th>State class</th>
<th>Why wiring diagram alone is not enough</th>
<th>Range that can be said in case of missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cell type label</strong></td>
<td>Even with the same adjacency relationship, different transcript types have different binding motifs, synaptic properties, and myelination tendencies. </td>
<td>Although useful as a structural atlas or candidate scaffold, it is not a sufficient condition for functional reproduction. </td>
</tr>
<tr>
<td><strong>Activity-dependent transcription / chromatin / epigenetic state</strong></td>
<td>Even with the same graph and cell type, allocation eligibility, late memory-stabilization programs, and locus-specific plasticity rules can still differ over hours to weeks. </td>
<td>Static atlas labels or one-shot DEG lists stay as identity/context clues; memory-stabilization controller remains latent unless temporal or causal evidence is shown. </td>
</tr>
<tr>
<td><strong>Intrinsic excitability/homeostasis/maintenance state</strong></td>
<td>Even with the same graph and cell type, the response to the same input and long-term recovery will differ if the threshold, gain, firing-rate return destination, sleep/wake-dependent renormalization, and compensation are different. </td>
<td>Even if there is short-term activity matching, cross-day stability, long-term stability, and memory allocation remain in the latent state. </td>
</tr>
<tr>
<td><strong>Synaptic efficiency/short-term state</strong></td>
<td>Weight, emission probability, and plastic change cannot be determined solely by the presence or absence of edges. </td>
<td>It is possible to describe static wiring, but it cannot claim L2 intervention prediction or L3 stability control. </td>
</tr>
<tr>
<td><strong>Local proteostasis / synaptic-tagging state</strong></td>
<td>Even with the same graph and current weights, late-LTP capture, branch-specific stabilization, and the balance of local translation/degradation/autophagy can still differ. </td>
<td>Stop treating late stabilization, cross-event capture, or reconsolidation as closed, and keep the tag/proteostasis route explicit as latent or externally calibrated. </td>
</tr>
<tr>
<td><strong>Perisynaptic ECM / PNN state</strong></td>
<td>Even with the same synapse graph, extracellular matrix organization can change receptor mobility, inhibitory plasticity, memory-update resistance, and the opening or closing of adult plasticity windows. </td>
<td>Stop treating adult plasticity, reconsolidation resistance, or inhibitory stabilization as closed, and keep ECM / PNN state explicit as latent or externally calibrated. </td>
</tr>
<tr>
<td><strong>Ionic milieu / chloride homeostasis</strong></td>
<td>Even with the same graph, cell type, and nominal weights, local chloride set point, transporter state, and extracellular ion composition can still change inhibitory sign, network gain, rhythm stability, and state transitions. </td>
<td>Stop treating inhibition sign, rhythm stability, or state transitions as fixed, and keep ionic / chloride state explicit as latent, perturbed, externally calibrated, or only coarsely proxied. </td>
</tr>
<tr>
<td><strong>Delay / timing-state</strong></td>
<td>Even with the same graph, different myelin thickness, node/internode geometry, periaxonal structure, or glial control can change conduction speed, synchrony, and phase. </td>
<td>Stop claiming closed loops, phase consistency, or timing-complete reconstruction, and make timing-state uncertainty explicit. </td>
</tr>
<tr>
<td><strong>Neural modification field</strong></td>
<td>The states of alertness and learning rate cannot be restored from static wiring, and pupil diameter and HRV remain as coarse proxies. </td>
<td>We do not insist on transmitter-specific internal states, but treat them as covariates and stratification factors. </td>
</tr>
<tr>
<td><strong>Glial-metabolic coupling status</strong></td>
<td>Astrocytes are causally involved in plasticity and memory retrieval, and are not just supporting tissues. </td>
<td>Plasticity and long-term stability are treated as partial models and the scope of application is limited. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Practical rules here</strong>
<p>
connectome-complete does not mean<strong>emulation-complete</strong>. Detailed primary literature and the technical basis for which state variables should be included in the minimum submission are summarized in <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams alone are not enough</a>. The newly emphasized issues of <strong>activity-dependent transcription / chromatin state</strong>, <strong>local proteostasis / synaptic-tagging state</strong>, and <strong>intrinsic excitability/homeostasis/maintenance state</strong> are discussed in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: cell-type atlas is not current transcriptional state</strong>
<p>
<a href="https://doi.org/10.1126/science.adg9982" target="_blank">Santoni et al. (2024)</a> showed that chromatin plasticity predetermines neuronal eligibility for memory-trace formation, <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">Traunmüller et al. (2025)</a> showed temporally defined and region-specific chromatin / gene-expression changes after novel-environment exposure, <a href="https://doi.org/10.1038/s41588-025-02195-z" target="_blank">Coda et al. (2025)</a> showed cell-type- and locus-specific epigenetic editing of memory expression, and <a href="https://doi.org/10.1038/s41586-025-09334-w" target="_blank">Terceros et al. (2026)</a> showed distinct thalamocortical transcriptional gates for memory stabilization. Therefore, when a claim depends on allocation eligibility, late stabilization, or locus-specific plasticity, this site asks authors to disclose whether transcriptional / chromatin state was measured, perturbed, externally calibrated, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: current weight is not the late-stabilization route</strong>
<p>
<a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a> proposed synaptic tagging as the condition that allows late LTP to capture plasticity-related proteins, <a href="https://doi.org/10.1038/ncomms2250" target="_blank">Shires et al. (2012)</a> demonstrated synaptic tagging and capture in the living rat, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a> showed that the dendritic branch is a preferred integrative unit for protein-synthesis-dependent LTP, <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">Fonseca et al. (2006)</a> showed that late-LTP maintenance depends on the balance of protein synthesis and proteasome-dependent degradation, <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a> linked local autophagy-coupled translation to long-term memory formation, and <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">Thomas et al. (2025)</a> showed that actin/spine states can persist on the timescale of the synaptic tag. Therefore, when a claim depends on late stabilization, reconsolidation, or cross-event capture, this site asks authors to disclose whether the local proteostasis / synaptic-tag route was measured, perturbed, externally calibrated, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03 Addendum: delay is not one scalar</strong>
<p>
Hardware latency audit and biological timing-state audit solve different problems. <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a>, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a>, <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a>, <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">Micheva et al. (2021)</a>, and <a href="https://doi.org/10.7554/eLife.73827" target="_blank">Dubey et al. (2022)</a> show that node/internode geometry, periaxonal coupling, astrocyte control, and PV-axon myelination can all alter spike-arrival timing and synchrony. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">van Blooijs et al. (2023)</a> pushes human tract-scale transmission-speed measurement forward, but it still remains a macro proxy. Therefore, when a claim depends on phase, synchrony, or closed-loop timing, this site asks authors to disclose whether biological timing-state was measured, externally calibrated, absorbed into a constant, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: ECM / PNN is not just static scaffold</strong>
<p>
<a href="https://doi.org/10.1126/science.1072699" target="_blank">Pizzorusso et al. (2002)</a> showed that digesting chondroitin-sulfate proteoglycans can reopen adult ocular-dominance plasticity, <a href="https://doi.org/10.1038/nn.2338" target="_blank">Frischknecht et al. (2009)</a> showed that brain extracellular matrix constrains AMPA-receptor lateral mobility and short-term synaptic plasticity, <a href="https://doi.org/10.1126/science.1174146" target="_blank">Gogolla et al. (2009)</a> showed that perineuronal nets protect fear memories from erasure, and <a href="https://doi.org/10.1016/j.matbio.2024.11.001" target="_blank">Jabłońska et al. (2024)</a> showed that ECM integrity regulates hippocampal GABAergic plasticity. Human evidence such as <a href="https://doi.org/10.3390/ijms23158197" target="_blank">Boonen et al. (2022)</a> is still mainly ex vivo pathology rather than in vivo whole-brain ground truth. Therefore, when a claim depends on plasticity windows, receptor diffusion, or stabilization against erasure, this site asks authors to disclose whether ECM / PNN state was measured, perturbed, externally calibrated, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: ionic milieu is not background chemistry</strong>
<p>
<a href="https://doi.org/10.1126/science.1245423" target="_blank">Glykys et al. (2014)</a> showed that local impermeant anions help establish neuronal chloride concentration, <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">Heubl et al. (2017)</a> showed that GABA<sub>A</sub>-receptor-mediated inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase, <a href="https://doi.org/10.1126/science.aad4821" target="_blank">Ding et al. (2016)</a> showed that changing interstitial K<sup>+</sup>, Ca<sup>2+</sup>, Mg<sup>2+</sup>, and H<sup>+</sup> is sufficient to shift cortical activity and sleep/wake state, <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">Huberfeld et al. (2007)</a> showed perturbed chloride homeostasis with depolarizing GABAergic signaling in human temporal-lobe epilepsy, and <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> showed that present human in vivo routes are still coarse sodium proxies. Therefore, when a claim depends on inhibitory sign, rhythm stability, or state transitions, this site asks authors to disclose whether ionic / chloride state was measured, perturbed, externally calibrated, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03 Addendum: Use augmentation / ablation instead of enumeration</strong>
<p>
The weakness found in this re-audit was that by simply listing the state variables as ``missing,'' it was difficult to convey to the reader what could be added to make the claim even stronger. Therefore, on this site, we will compare the <strong>connectome-only baseline</strong> and the <strong>model with additional variables</strong> under the same held-out conditions, and request submissions that show which augmentation reduced which error term.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>augmentation claim</th>
<th>Minimum desired comparison</th>
<th>What you can say even more strongly when you pass</th>
<th>Replacement in case of failure</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>+ same-brain function / behavior</strong></td>
<td>Compare the model that adds the connectome-only baseline and the same-brain function/behavior using the same split. </td>
<td>We can limit the extent to which the structural atlas is effective for state-dependent response prediction within the same individual. </td>
<td>Contains structural scaffolding and annotation, and does not promote dynamical claims. </td>
</tr>
<tr>
<td><strong>+ transcriptomic / cell-type label</strong></td>
<td>Ablation with the condition that removes the node label, and generates gain of target specificity and held-out response. </td>
<td>You can say how much cell-type information improves target-specific connectivity and response prediction. </td>
<td>cell-type is a descriptive tag and does not auto-complete until threshold / gain / set point. </td>
</tr>
<tr>
<td><strong>+ transcriptional / chromatin state audit</strong></td>
<td>Compare a cell-atlas or connectome baseline against the same model with time-stamped expression / chromatin measurements or causal epigenetic perturbation under the same held-out learning or stabilization condition, and disclose gains separately. </td>
<td>You can state more narrowly how much allocation eligibility, late stabilization, or locus-specific plasticity control improves once current transcriptional / chromatin state is treated explicitly. </td>
<td>A static atlas or one-shot DEG list remains identity/context annotation or a time-stamped clue, and does not become ground truth of current plasticity state. </td>
</tr>
<tr>
<td><strong>+ local proteostasis / synaptic-tagging audit</strong></td>
<td>Compare a synapse- or transcription-aware baseline against the same model with tag/PRP capture measurements, local translation/degradation/autophagy perturbation, or branch-local tag proxy under the same held-out stabilization or reconsolidation condition, and disclose gains separately. </td>
<td>You can state more narrowly how much late stabilization, branch-local persistence, or cross-event capture improves once the local proteostasis route is treated explicitly. </td>
<td>A current weight estimate or one-shot transcriptomic change remains a snapshot and does not become ground truth of the late-stabilization route. </td>
</tr>
<tr>
<td><strong>+ ECM / PNN state audit</strong></td>
<td>Compare a synapse- or connectome-based baseline against the same model with matrix markers, local matrix perturbation, or externally calibrated ECM state under the same held-out plasticity or recovery conditions, and disclose gains in plasticity / reversal / stabilization separately. </td>
<td>You can state more narrowly how much plasticity-gate control, inhibitory stabilization, or memory-update resistance improves once ECM / PNN state is treated explicitly. </td>
<td>Histology, pathology, or generic scaffold annotation alone remain structural context and do not become a ground truth of current ECM / PNN state in vivo. </td>
</tr>
<tr>
<td><strong>+ ionic milieu / chloride-homeostasis audit</strong></td>
<td>Compare a synapse- or excitability-aware baseline against the same model with chloride-state measurements, ionic manipulation, transporter-state perturbation, or externally calibrated ionic proxy under the same held-out memory, rhythm, or state-transition condition, and disclose gains separately. </td>
<td>You can state more narrowly how much inhibitory polarity, rhythm stability, or state-transition prediction improves once ionic / chloride state is treated explicitly. </td>
<td>Human sodium MRI or pathology alone remains a macro or disease-linked proxy and does not become ground truth of current local chloride homeostasis in vivo. </td>
</tr>
<tr>
<td><strong>+ timing-state / conduction audit</strong></td>
<td>Compare a fixed-delay baseline against a model or analysis that adds measured or externally calibrated timing variables under the same held-out conditions, and disclose phase / synchrony / perturbation gains separately. </td>
<td>You can state more narrowly how much timing-sensitive prediction improves once biological conduction timing is treated explicitly rather than absorbed into a constant. </td>
<td>Human myelin maps or tract-speed estimates remain macro timing proxies; without external calibration they do not become per-axon timing ground truth. </td>
</tr>
<tr>
<td><strong>+ neuromodulatory route audit</strong></td>
<td>Compare the same baseline against mixed arousal proxy, local transmitter sensor, receptor / transporter atlas, occupancy PET, or release-sensitive PET under the same held-out state transition, and report ligand / challenge / time-window plus abstention separately. </td>
<td>You can state more narrowly how much a selected transmitter-linked covariate, regional receptor prior, or challenge-limited release proxy improved prediction or stratification. </td>
<td>Mixed proxy remains a covariate, receptor atlas remains a regional prior, and occupancy / displacement PET remains a ligand- and challenge-limited proxy rather than whole-brain neuromodulatory ground truth. </td>
</tr>
<tr>
<td><strong>+ glial / slow-state</strong></td>
<td>Show gains in recovery, plasticity, and perturbation aftermath on the order of minutes, and include species differences and cell-type dependence. </td>
<td>Some parts of slow network state and plasticity can be read as conditional models involving glia. </td>
<td>Neuron-only approximations keep limited applicability and demote long-term stability claims. </td>
</tr>
<tr>
<td><strong>+ excitability / homeostatic recovery log</strong></td>
<td>Issuing held-out degradation, recovery time, and memory allocation proxy for cross-day/cross-perturbation. </td>
<td>It can be said even more strongly that the state on the controller side had an effect on long-term stability and memory allocation. </td>
<td>Retain short-term activity fit, and return long-term claims and memory claims to latent state. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 Addendum: Add measurement stack to augmentation claim</strong>
<p>
Even if the same "transcriptomic label is added" or "same-brain function is added", the variables directly observed by the whole-brain spatial atlas, Patch-seq, volume EM, same-brain calcium+EM, and local transmitter sensor are different. Therefore, on this site, we always include <strong>Which measurement stack provided the additional information</strong> in the augmentation claim, and also write the claim ceiling for each stack separately. For a summary table, see <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: observability and claim ceiling by measurement stack</a>.
</p>
</div>
</section>

<section class="section" id="verification-rigor">
<h2 class="section-title">Verification rigor requirements (reorganized in 2026-03 scientific audit)</h2>
<p>
Based on the primary literature audit in March 2026, this section has been rewritten to separate "requirements that are currently close to standards" and "requirements that are promising but are still in the exploratory stage." There are three main amendments: <strong>Do not require specific tool names</strong>, <strong>Require external validation for source imaging claims</strong>, <strong>Reduce TMS-EEG and thermodynamic indicators with application conditions</strong>.
</p>
<div class="note-box">
<strong>Weaknesses found in audit</strong>
<p>
In the previous text, methods with different characteristics, such as ASR, ZapLine-plus, PCI-ST, Effective Information, and EPR, were listed as the same "essential requirements." But first and foremost, COBIDAS-MEEG and EEG-BIDS emphasize<strong>transparent reporting</strong>, <strong>shareable metadata</strong>, and <strong>comparable baselines</strong>. Therefore, on this page, we reposition <strong>foundation of reproducibility</strong> as required, <strong>methodology selection</strong> recommended, and<strong>additional theory-driven indicators</strong> as exploration.
</p>
</div>
<div class="key-points">
<h4>Essential requirements (close to standard at this time)</h4>
<ul>
<li><strong>Shareable inputs: </strong>Compliant with BIDS / EEG-BIDS, leaving <code>events.tsv</code> and JSON sidecar, electrode coordinates, coordinate system, task description, instructions, and key artifact factors. It is strongly recommended that event semantics be supplemented with machine-readable vocabularies such as HED and CogAtlasID. </li>
<li><strong>Transparent reporting:</strong>Publish acquisition conditions, reference methods, filters, bad channel processing, exclusion trials, ICA/regression/interpolation order and parameters in line with COBIDAS-MEEG. We do not use "automatic preprocessing" that cannot be reproduced. </li>
<li><strong>External validation of ESI claims:</strong>When claiming improvements in EEG source imaging, clarify individual MRI, coordinates, and forward models as much as possible, and verify errors using simulations, phantoms, simultaneous invasive recordings, or intracranial stimulation. Deep accuracy should not be claimed simply by introducing high-density EEG or MRI. </li>
<li><strong>Comparison design:</strong>The evaluation will not be completed with the accuracy of a single dataset, but will be divided by subject or session, compared with the existing baseline, and any failures, abstention conditions, and uncertainties will be disclosed. Improvements on a single dataset do not guarantee external generalization. </li>
</ul>
</div>
<div class="key-points">
<h4>Recommended requirements (issue-dependent, but improves reproducibility)</h4>
<ul>
<li><strong>Sensitivity analysis of preprocessing:</strong>ASR, Autoreject, ICA, ZapLine-plus, Riemannian geometry, etc. are candidates and are not a universal correct answer. Leave at least one alternative setting or sensitivity analysis to see which treatment drove the results. </li>
<li><strong>Signal preservation audit:</strong>Record the amount of change in the before and after spectra, exclusion rate, interpolation rate, and key indicators to check not only that the noise has been reduced but also that it is not destroying the target signal. </li>
<li><strong>Specifying conditions for TMS-EEG/PCI:</strong>If perturbation complexity is used, report stimulation site, intensity, coil angle, auditory masking, myoelectric/stimulus artifact window, repeatability assessment, and follow TMS-EEG recommendations. </li>
</ul>
</div>
<div class="key-points">
<h4>Search requirements (promising but not currently gate conditions)</h4>
<ul>
<li><strong>PCI-ST Spatial Distribution, Effective Information, Causal Density, Transfer Entropy:</strong>While these can be useful for research, they are highly task- and implementation-dependent and are currently not included in the required core metrics of the common bench. </li>
<li><strong>Persistence diagram, Bottleneck distance, Fisher information distance:</strong>Promises as an auxiliary indicator for structural comparison, but lacks standardization in interpretation and stability. Submit as an auxiliary analysis, and place the primary judgment on simpler, more easily auditable metrics. </li>
<li><strong>Thermodynamic irreversibility / EPR:</strong> Research on non-equilibrium brain dynamics is progressing, but the current main evidence still relies heavily on fMRI, ECoG, and theoretical models. It is too early to use this as an essential KPI for pass / fail decisions in WBE verification. </li>
</ul>
</div>
</section>

<section class="section" id="consciousness-readout-gate">
<h2 class="section-title">2026-03 Addendum: Consciousness readout is accepted at 4 gates</h2>
<p>
The weakness that should have been explored more deeply this time is that simply classifying EEG/DoC/anesthesia literature into "no-report," "PCI," "resting-state," and "multimodal" was not enough to determine which conditions would allow the claim to be raised to the next level. Cohen et al. (2024) and Fahrenfort et al. (2025) showed that construct validity is broken unless report / post-perceptual confound and criterion placement are broken separately. Gogulski et al. (2024) and Biabani et al. (2024) showed that TMS-EEG reliability and sensory contamination depend on target and time window, and Breyton et al. (2025) and Casarotto et al. (2024) showed that TMS-EEG reliability and sensory contamination depend on target and time window, and Breyton et al. Indicates that calibration is required. Furthermore, Rohaut et al. (2024), Kawai et al. (2025), and Manasova et al. (2026) have shown progress in multimodal panels, but this also means that deployability cannot be claimed unless behavior-only baseline and missing-modality conditions are exceeded. Therefore, this site accepts consciousness-related readouts at the following four gates.
</p>
<table class="data-table">
<thead>
<tr>
<th>Gate</th>
<th>Minimum requirement</th>
<th>Assertion to stop when not passing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Construct-validity gate</strong></td>
<td>Separate no-report / report, separate log for criterion placement, fixing failure conditions in advance, at least design basis for crushing task / report confound. </td>
<td>This means that this neural marker has read the contents of consciousness itself. The current situation leaves open the possibility of picking up decision strategy or post-perceptual processing. </td>
</tr>
<tr>
<td><strong>Perturbational gate</strong></td>
<td>TMS-EEG/intracranial perturbation stimulation site, intensity, control, auditory/somatosensory control, artifact window, target-specific reliability. </td>
<td>It is just a PCI / PCI-ST style value and is called a state-level benchmark. If there is no condition log, the comparison itself will break down. </td>
</tr>
<tr>
<td><strong>Calibration gate</strong></td>
<td> Calibrate PCI, behavioral assessment, clinical outcomes, pipeline sensitivity analysis, and withdrawal thresholds in the same cohort. </td>
<td>The resting-state complexity, criticality, and passive EEG classifier is called a single bedside meter. Leave it as an auxiliary proxy before external calibration. </td>
</tr>
<tr>
<td><strong>Incremental / deployability gate</strong></td>
<td>Comparison with behavior-only baseline, generalization outside the facility, robustness under missing-modality conditions, calibration error, and reporting of measurement burden. </td>
<td> Multimodal panel is written as ready-to-deploy. Average accuracy alone is not the basis for clinical operation. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
No-report / criterion placement is treated as a <strong>construct-validity gate</strong>, PCI / PCI-ST is treated as a main benchmark candidate only after it passes a <strong>perturbational gate</strong>, resting-state complexity / criticality remains an auxiliary proxy until it passes a <strong>calibration gate</strong>, and a multimodal clinical panel remains exploratory until it passes an <strong>incremental / deployability gate</strong>. In other words, on this site, the same "awareness index" can have a different claim ceiling depending on which gate it has passed.
</p>
</div>
</section>

<section class="section" id="causal-perturbation-suite">
<h2 class="section-title">Causal perturbation suite (reorganized to 4-gate system)</h2>
<p>
The March 2026 primary-literature audit reconfirmed that current BCI and neuromodulation papers provide <strong>causal evidence with different strengths at different stages</strong>, not a one-step demonstration of "counterfactual equivalence." Therefore, this site treats offline accuracy, online human-in-the-loop, local causal intervention, and long-term closed loops separately, and does not promote merely high-accuracy results to L2 / L3.
</p>
<div class="note-box">
<strong>What is different from ordinary accuracy evaluation</strong>
<p>
A normal accuracy evaluation asks whether the system gives the same answer to the same question. The causal perturbation suite goes one step further and compares <strong>how performance collapses and how it recovers when conditions are intentionally changed</strong>. In other words, it is not only a test of answer matching, but also a test of whether internal mechanisms react in comparable ways.
</p>
</div>
<div class="note-box">
<strong>When you want to organize only the entrance first</strong>
<p>
If you want an everyday-language explanation of the differences between held-out accuracy, intervention, counterfactual reasoning, and perturbation-based verification, read <a href="wiki/counterfactual-and-perturbation-verification.html">Wiki: Counterfactual and Perturbation Verification</a> first.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Gate</th>
<th>Minimum desired proof</th>
<th>Current representative examples</th>
<th>What this still does not justify</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1 / online decode</strong></td>
<td>The subject performs continuous operations or conversations while viewing the output, and compares using online indicators instead of offline. </td>
<td>Forenzo et al. (2024), Willett et al. (2023), Littlejohn et al. (2025)</td>
<td>This alone does not lead to causal structure matching or counterfactual equivalence. </td>
</tr>
<tr>
<td><strong>Gate 2 / bidirectional perturbation</strong></td>
<td>Feedback or a bidirectional loop in which a stimulus changes the next input, and behavior changes due to intervention. </td>
<td>Flesher et al. (2021)</td>
<td>Even if we can show the causal gain of local subsystems, we cannot show that whole-brain WBE holds true. </td>
</tr>
<tr>
<td><strong>Gate 3 / state-dependent intervention</strong></td>
<td>Switch stimulation and control according to the detected state, and show improvement by comparing real-life blocks. </td>
<td>Oehrn et al. (2024), Dixon et al. (2026)</td>
<td>Task-specific controller effectiveness may be shown, but state completeness remains unresolved. </td>
</tr>
<tr>
<td><strong>Gate 4 / longitudinal stability</strong></td>
<td>Disclose the degradation, recalibration frequency, abandonment rate, and termination conditions of fixed decoders. </td>
<td>Wairagkar et al. (2025), Wilson et al. (2025), Cascino et al. (2026)</td>
<td>A system that cannot operate stably over time cannot be treated as L3-complete on the basis of a short demonstration. </td>
</tr>
</tbody>
</table>
<div class="key-points">
<h4>Three-stage introduction</h4>
<ul>
<li><strong>Stage A / Validation that can be performed now:</strong> Preregister and compare out-of-subject generalization, unlearning conditions, online indicators, abstention, and calibration error using public EEG and existing BCI data. Even if Stage A is passed, the argument remains at L1 to weak L2. </li>
<li><strong>Stage B / Intermediate validation with external standards:</strong> Measure response error, uncertainty, and recovery time in systems with ground truth, such as simulations, phantoms, intracranial stimulation, and simultaneous invasive recordings. Strong claims about source-imaging improvement or perturbation response should not be made until this stage has been passed. </li>
<li><strong>Stage C / Actual intervention:</strong> TMS-EEG, adaptive stimulation, and pharmacological interventions have strong validation power, but they require IRB approval, equipment, and subject operations. In this repository, the requirements specification and public log format are prepared in advance, while experiment execution itself is treated as an external dependency task. </li>
</ul>
</div>
<div class="note-box">
<strong>Evaluation metrics</strong>
<p>
In the first judgment, we prioritize pre-registered effect size, robustness under OOD conditions, calibration error, abstention rate, and uncertainty range, as well as <strong>end-to-end latency P50 / P95 / P99</strong>, <strong>jitter</strong>, <strong>dropout</strong>, <strong>recalibration burden</strong>, and <strong>recovery time after perturbation</strong>. PCI-ST spatial distribution, bottleneck distance on persistence diagrams, and Fisher Information Metric (FIM) distances between generated models are left as auxiliary analyses; the main pass / fail judgment does not depend on any single method.
</p>
</div>
<div class="note-box">
<strong>Don't sell the word counterfactual cheaply</strong>
<p>
If the branching conditions, comparison rules, failure conditions, and stimulus artifact windows are not fixed in advance, we do not refer to it as a "counterfactual equivalence" on this site, but rather as an <strong>intervention response test</strong> or a <strong>perturbation generalization test</strong>.
</p>
</div>
</section>

<section class="section" id="verification-rigor-2026-02">
<h2 class="section-title">Additional audit logs (with applicable conditions)</h2>
<p>
In response to technical criticisms (Issue #257-#260) submitted in the latter half of February 2026, this section clarifies the role of additional logs. The goal is not to make everything mandatory, but to clarify <strong>what should be included once a given analysis has actually been run</strong>.
</p>
<div class="key-points">
<h4>Log with applicable conditions</h4>
<ul>
<li><strong>ESI/HBM logs:</strong>Only when making anatomical source claims, attach uncertainty maps from cranial conductivity, forward model sensitivity analysis, or hierarchical Bayesian estimation. </li>
<li><strong>Alternative model log:</strong>Does not claim that the estimated model is the only solution, but reports the existence of alternative models or equivalence classes that can explain the same observed statistics. </li>
<li><strong>Preprocessing Fidelity Log:</strong>Records before and after spectra, exclusion/interpolation rates, changes in key metrics, and at least one task-consistent signal preservation metric, with or without ASR. </li>
<li><strong>Event Semantics Log:</strong> Attach HED to BIDS metadata and map to CogAtlas / CogPO / NIF / SCORE etc. as necessary. Fixing to a specific ontology is not a common requirement. </li>
<li><strong>Perturbation log:</strong>If local interventions or stimulation were used, expose the stimulation site, intensity, artifact window, masking, safe stop conditions, and retry conditions. If not used, specify "No perturbation evidence." </li>
<li><strong>Supplementary thermodynamic log:</strong>When reporting irreversibility or EPR, specify coarse-graining, modality, sampling, estimator, lower bound or main body estimation, and isolation of hardware power and computational cost. </li>
</ul>
</div>
<div class="note-box">
<strong>Handling external dependent tasks</strong>
<p>
Validations that require real subject intervention (TMS/tDCS), IRB review, and equipment procurement are managed as externally dependent tasks. In this repository, "requirement specifications, judgment conditions, and public log format" will be implemented in advance, and the experiment implementation itself will proceed on a separate track.
</p>
</div>
</section>

<section class="section" id="thermodynamic-verification">
<h2 class="section-title">Thermodynamic indicators (exploration track)</h2>
<p>
Although research investigating brain dynamics using NESS (Non-Equilibrium Steady State) and time irreversibility is important, this site positions it as a <strong>Supplementary Research Track</strong> as of 2026-03. While the usefulness of irreversibility indicators is being shown, they are still a common acceptance criterion for WBE validation because of the strong influence of modality dependence and estimation assumptions. In particular, entropy production estimated from coarse-grained neural data is often <strong>information-theoretic lower bound</strong> and must be read separately from microscopic physical dissipation itself.
</p>
<div class="key-points">
<h4>What can be said at the moment</h4>
<ul>
<li><strong>Breach of detailed equilibrium can be observed:</strong>There are studies that estimate the lower bound of entropy production from brain activity, and it is supported that irreversibility contains information about neural dynamics. </li>
<li><strong>However, interpretation is modality-dependent:</strong>The relationship between state of consciousness and irreversibility has also been reported in fMRI, ECoG, etc., but the appearance changes depending on coarse-graining, temporal resolution, preprocessing, and estimator. EEG/ECoG/fMRI irreversibility should not be equated with metabolic dissipation or hardware power. </li>
<li><strong>Therefore, we do not use it as a gate condition:</strong>At this stage, thermodynamic indicators alone do not determine WBE identity or validity. </li>
</ul>
</div>
<div class="key-points">
<h4>Minimum requirements for hiring</h4>
<ul>
<li><strong>Disclosure of estimation conditions:</strong> Be sure to write whether coarse-graining, sampling period, state space reconstruction, Markov assumption, and lower bound estimation are used. </li>
<li><strong>Cost Isolation:</strong>We report hardware power, wall-clock energy, FLOPs, and communication costs separately, and treat the approximately 20W of biological brains only as a background value for comparison. </li>
<li><strong>Submitted as ancillary indicators:</strong>Read alongside existing reproducibility indicators, source validation, perturbed responses, baseline comparisons, and do not draw conclusions on their own. </li>
</ul>
</div>
<div class="note-box">
<strong>What to do now with this repository</strong>
<p>
In this repository, we do not make thermodynamic indicators a "required submission," but rather leave them at the stage where log formats and literature monitoring are in place. This will be treated as an exploratory auxiliary analysis until stable operation using actual data and estimation error auditing are confirmed.
</p>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References (main)</h2>
<ol>
<li>Gorgolewski, K. J., et al. (2016). The brain imaging data structure. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS EEG Specification</a>（official documentation）</li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Bigdely-Shamlo, N., et al. (2016). Hierarchical Event Descriptors (HED). <a href="https://doi.org/10.3389/fninf.2016.00042" target="_blank">doi:10.3389/fninf.2016.00042</a></li>
<li>Hermes, D., et al. (2025). HED library schema for EEG data annotation. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">doi:10.1038/s41597-025-05791-2</a></li>
<li>Pernet, C., et al. (2020). COBIDAS-MEEG recommendations. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Markiewicz, C. J., et al. (2021). OpenNeuro resource paper. <a href="https://doi.org/10.7554/eLife.71774" target="_blank">doi:10.7554/eLife.71774</a></li>
<li>Goldberger, A. L., et al. (2000). PhysioBank / PhysioNet. <a href="https://doi.org/10.1161/01.CIR.101.23.e215" target="_blank">doi:10.1161/01.CIR.101.23.e215</a></li>
<li>Jayaram, V., &amp; Barachant, A. (2018). MOABB: trustworthy algorithm benchmarking for BCIs. <a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">doi:10.1088/1741-2552/aadea0</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Unnwongse, K., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, W., et al. (2025). Localization accuracy of interictal and ictal EEG source imaging in simultaneous HD-EEG and SEEG. <a href="https://doi.org/10.1007/s00415-025-12886-9" target="_blank">doi:10.1007/s00415-025-12886-9</a></li>
<li>Delorme, A. (2023). EEG is better left alone. <a href="https://doi.org/10.1038/s41598-023-27528-0" target="_blank">doi:10.1038/s41598-023-27528-0</a></li>
<li>Klug, M., &amp; Kloosterman, N. A. (2022). Zapline-plus. <a href="https://doi.org/10.1002/hbm.25832" target="_blank">doi:10.1002/hbm.25832</a></li>
<li>Hernandez-Pavon, J. C., et al. (2023). TMS combined with EEG: recommendations and open issues. <a href="https://doi.org/10.1016/j.brs.2023.02.009" target="_blank">doi:10.1016/j.brs.2023.02.009</a></li>
<li>Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
<li>Forenzo, D., et al. (2024). Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. <a href="https://doi.org/10.1093/pnasnexus/pgae145" target="_blank">doi:10.1093/pnasnexus/pgae145</a></li>
<li>Willett, F. R., et al. (2023). A high-performance speech neuroprosthesis. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Flesher, S. N., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Wilson, G. H., et al. (2025). Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Oehrn, C. R., et al. (2024). Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Dixon, S., et al. (2026). Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. <a href="https://doi.org/10.1038/s41551-025-01592-5" target="_blank">doi:10.1038/s41551-025-01592-5</a></li>
<li>Cascino, S., et al. (2026). Chronic adaptive deep brain stimulation in Parkinson’s disease: ADAPT-START findings and programming principles. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
<li>Lynn, C. W., et al. (2021). Broken detailed balance and entropy production in the human brain. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>de la Fuente, L. A., et al. (2022). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing. <a href="https://doi.org/10.1093/cercor/bhae415" target="_blank">doi:10.1093/cercor/bhae415</a></li>
<li>Fahrenfort, J. J., et al. (2025). Criterion placement threatens the construct validity of neural measures of consciousness. <a href="https://doi.org/10.7554/eLife.102335" target="_blank">doi:10.7554/eLife.102335</a></li>
<li>Gogulski, J., et al. (2024). The reliability and variability of TMS-evoked potentials in the dorsolateral prefrontal cortex in healthy adults. <a href="https://doi.org/10.1016/j.brs.2024.06.001" target="_blank">doi:10.1016/j.brs.2024.06.001</a></li>
<li>Biabani, M., et al. (2024). Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. <a href="https://doi.org/10.1162/imag_a_00349" target="_blank">doi:10.1162/imag_a_00349</a></li>
<li>Breyton, M., et al. (2025). Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms. <a href="https://doi.org/10.7554/eLife.98920" target="_blank">doi:10.7554/eLife.98920</a></li>
<li>Rohaut, B., et al. (2024). Multimodal imaging reveals partially preserved semantic cognition in comatose patients after cardiac arrest. <a href="https://doi.org/10.1212/WNL.0000000000209439" target="_blank">doi:10.1212/WNL.0000000000209439</a></li>
<li>Kawai, R., et al. (2025). Multimodal assessment improves neuroprognosis performance after out-of-hospital cardiac arrest. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu, S., Tyler, L. K., Henson, R. N. A., Rowe, J. B., Cam-CAN, &amp; Tsvetanov, K. A. (2023). Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Yucel, M. A. Y., Selb, J., Aasted, C. M. A., Petkov, M. P., Becerra, L., Borsook, D., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>Epp, S. M., Castrillon, G., Yuan, B., Andrews-Hanna, J., Preibisch, C., &amp; Riedl, V. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Santoni, G., et al. (2024). Chromatin plasticity predetermines neuronal eligibility for memory trace formation. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">doi:10.1126/science.adg9982</a></li>
<li>Traunmüller, L., et al. (2025). Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">doi:10.1038/s41467-025-63029-6</a></li>
<li>Coda, B., et al. (2025). Cell-type- and locus-specific epigenetic editing of memory expression. <a href="https://doi.org/10.1038/s41588-025-02195-z" target="_blank">doi:10.1038/s41588-025-02195-z</a></li>
<li>Terceros, Y., et al. (2026). Thalamocortical transcriptional gates coordinate memory stabilization. <a href="https://doi.org/10.1038/s41586-025-09334-w" target="_blank">doi:10.1038/s41586-025-09334-w</a></li>
<li>Frey, U., &amp; Morris, R. G. M. (1997). Synaptic tagging and long-term potentiation. <a href="https://doi.org/10.1038/385533a0" target="_blank">doi:10.1038/385533a0</a></li>
<li>Fonseca, R., Vabulas, R. M., Hartl, F. U., Bonhoeffer, T., &amp; Nägerl, U. V. (2006). A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">doi:10.1016/j.neuron.2006.08.015</a></li>
<li>Govindarajan, A., Israely, I., Huang, S.-Y., &amp; Tonegawa, S. (2011). The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">doi:10.1016/j.neuron.2010.12.008</a></li>
<li>Shires, K. L., Da Silva, B. M., Hawthorne, J. P., Morris, R. G. M., &amp; Martin, S. J. (2012). Synaptic tagging and capture in the living rat. <a href="https://doi.org/10.1038/ncomms2250" target="_blank">doi:10.1038/ncomms2250</a></li>
<li>Pandey, K., Yu, X.-W., Steinmetz, A., &amp; Alberini, C. M. (2021). Autophagy coupled to translation is required for long-term memory formation. <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">doi:10.1080/15548627.2020.1775393</a></li>
<li>Thomas, M., Bogaciu, C.-A., Rizzoli, S. O., et al. (2025). Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">doi:10.1038/s42003-025-08459-0</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Pizzorusso, T., Medini, P., Berardi, N., Chierzi, S., Fawcett, J. W., &amp; Maffei, L. (2002). Reactivation of ocular dominance plasticity in the adult visual cortex. <a href="https://doi.org/10.1126/science.1072699" target="_blank">doi:10.1126/science.1072699</a></li>
<li>Frischknecht, R., Heine, M., Perrais, D., Seidenbecher, C. I., Choquet, D., &amp; Gundelfinger, E. D. (2009). Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. <a href="https://doi.org/10.1038/nn.2338" target="_blank">doi:10.1038/nn.2338</a></li>
<li>Gogolla, N., Caroni, P., Lüthi, A., &amp; Herry, C. (2009). Perineuronal nets protect fear memories from erasure. <a href="https://doi.org/10.1126/science.1174146" target="_blank">doi:10.1126/science.1174146</a></li>
<li>Jabłońska, K., Kaczor, K., Kółeczko, M., et al. (2024). Extracellular matrix integrity regulates GABAergic plasticity in the hippocampus. <a href="https://doi.org/10.1016/j.matbio.2024.11.001" target="_blank">doi:10.1016/j.matbio.2024.11.001</a></li>
<li>Boonen, M., Hellings, N., Hoedemaekers, T., et al. (2022). Reorganization of the brain extracellular matrix in hippocampal sclerosis. <a href="https://doi.org/10.3390/ijms23158197" target="_blank">doi:10.3390/ijms23158197</a></li>
<li>Glykys, J., Dzhala, V., Egawa, K., Balena, T., Saponjian, Y., Kuchibhotla, K. V., Bacskai, B. J., Kahle, K. T., Zeuthen, T., &amp; Staley, K. J. (2014). Local impermeant anions establish the neuronal chloride concentration. <a href="https://doi.org/10.1126/science.1245423" target="_blank">doi:10.1126/science.1245423</a></li>
<li>Heubl, M., Zhang, J., Pressey, J. C., Al Awabdh, S., Renner, M., Gomez-Castro, F., Moutkine, I., Eugène, E., Russeau, M., Kahle, K. T., Poncer, J.-C., &amp; Lévi, S. (2017). GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">doi:10.1038/s41467-017-01749-0</a></li>
<li>Ding, F., O'Donnell, J., Xu, Q., Kang, N., Goldman, N., &amp; Nedergaard, M. (2016). Changes in the composition of brain interstitial ions control the sleep-wake cycle. <a href="https://doi.org/10.1126/science.aad4821" target="_blank">doi:10.1126/science.aad4821</a></li>
<li>Huberfeld, G., Wittner, L., Clemenceau, S., Baulac, M., Kaila, K., Miles, R., &amp; Rivera, C. (2007). Perturbed chloride homeostasis and GABAergic signaling in human temporal lobe epilepsy. <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">doi:10.1523/JNEUROSCI.2761-07.2007</a></li>
<li>Qian, Y., Zhao, T., Zheng, H., Weimer, J., &amp; Boada, F. E. (2012). High-resolution sodium imaging of human brain at 7 T. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">doi:10.1002/mrm.23225</a></li>
<li>Hardingham, N. R., &amp; Larkman, A. U. (1998). The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">doi:10.1111/j.1469-7793.1998.249bu.x</a></li>
<li>Volgushev, M., Vidyasagar, T. R., Chistiakova, M., Yousef, T., &amp; Eysel, U. T. (2000). Membrane properties and spike generation in rat visual cortical cells during reversible cooling. <a href="https://doi.org/10.1111/j.1469-7793.2000.00059.x" target="_blank">doi:10.1111/j.1469-7793.2000.00059.x</a></li>
<li>Moser, E., Mathiesen, I., &amp; Andersen, P. (1993). Association between brain temperature and dentate field potentials in exploring and swimming rats. <a href="https://doi.org/10.1126/science.8446900" target="_blank">doi:10.1126/science.8446900</a></li>
<li>Long, M. A., &amp; Fee, M. S. (2008). Using temperature to analyse temporal dynamics in the songbird motor pathway. <a href="https://doi.org/10.1038/nature07448" target="_blank">doi:10.1038/nature07448</a></li>
<li>Rangaraju, V., Calloway, N., &amp; Ryan, T. A. (2014). Activity-driven local ATP synthesis is required for synaptic function. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">doi:10.1016/j.cell.2013.12.042</a></li>
<li>Rangaraju, V., Lauterbach, M., &amp; Schuman, E. M. (2019). Spatially stable mitochondrial compartments fuel local translation during plasticity. <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">doi:10.1016/j.cell.2018.12.013</a></li>
<li>Divakaruni, S. S., Van Dyke, A. M., Chandra, R., et al. (2018). Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">doi:10.1016/j.neuron.2018.09.025</a></li>
<li>Bapat, P., Nirschl, J. J., Wilkerson, J. R., et al. (2024). VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">doi:10.1038/s41467-023-44233-8</a></li>
<li>Hu, H., Tang, J., Wu, Y., et al. (2025). Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">doi:10.1038/s42003-025-08963-3</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Rzechorzek, N. M., Thrippleton, M. J., Chappell, F. M., et al. (2022). A daily temperature rhythm in the human brain predicts survival after brain injury. <a href="https://doi.org/10.1093/brain/awab466" target="_blank">doi:10.1093/brain/awab466</a></li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Goulas, A., Changeux, J.-P., Wagstyl, K., Amunts, K., Palomero-Gallagher, N., &amp; Hilgetag, C. C. (2021). The natural axis of transmitter receptor distribution in the human cerebral cortex. <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">doi:10.1073/pnas.2020574118</a></li>
<li>Koepp, M. J., Gunn, R. N., Lawrence, A. D., et al. (1998). Evidence for striatal dopamine release during a video game. <a href="https://doi.org/10.1038/30498" target="_blank">doi:10.1038/30498</a></li>
<li>Lippert, R. N., Bolding, K. A., Abbott, L. F., et al. (2019). Time-dependent assessment of stimulus-evoked regional dopamine release. <a href="https://doi.org/10.1038/s41467-019-09897-z" target="_blank">doi:10.1038/s41467-019-09897-z</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Nosek, B. A., et al. (2015). Promoting an open research culture. <a href="https://doi.org/10.1126/science.aab2374" target="_blank">doi:10.1126/science.aab2374</a></li>
<li>Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles. <a href="https://doi.org/10.1038/sdata.2016.18" target="_blank">doi:10.1038/sdata.2016.18</a></li>
</ol>
</section>




</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="tech_roadmap.html#definition">Definition of forward movement (Roadmap) →</a></li>
<li><a href="verification.html#casework">Casework (historical type) →</a></li>
<li><a href="research_harvest_50.html">50 worker literature map (unsolved problem decomposition) →</a></li>
<li><a href="issue.html#proposal-integration">List of technical proposals (linked to issues) →</a></li>
<li><a href="glossary.html">Glossary →</a></li>
<li><a href="datasets.html">Data & Bench (Datasets) →</a></li>
<li><a href="faq.html">FAQ →</a></li>
<li><a href="datasets.html#l0-practice">L0 practice (in Datasets) →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related Pages</h4>
<ul>
<li><a href="perspective.html#design-principles">Framework →</a></li>
<li><a href="mind_uploading_papers.html">Papers→</a></li>
<li><a href="issue.html">Contribute →</a></li>
</ul>
</div>

<div class="note-box">
<strong>Scope</strong>
<p>
This page is not where a "final conclusion" is declared. It is where <strong>rules and artifacts</strong> are placed so that research can accumulate in a falsifiable way. The larger the claim, the more it must be broken down into smaller parts that can be disproved.
</p>
</div>

</aside>
</main>
