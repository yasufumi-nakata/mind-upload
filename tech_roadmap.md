---
layout: default
title: "Technical Roadmap: Understanding WBE Through Measurement, Reconstruction, and Implementation"
description: "A learning roadmap for viewing mind uploading and WBE from the technical side, organized as a question tree from measurement to reconstruction, implementation, and verification."
article_type: "Roadmap (Definition #1)"
subtitle: "Break 'what counts as progress' into a question tree with reading order and minimum arrival conditions"
last_updated: "2026-03-19"
note: "Provisional draft (updated continuously)"
audience: "Readers who want the big picture, need a learning order, or want claim strength organized by level"
reading_time: "20-30 min (5 min for the index only)"
page_intro: "This page is a map of WBE questions arranged under measurement, reconstruction, implementation, verification, and social deployment. Its purpose is to keep the reader from losing track of which problems are foundational and which remain unresolved."
accuracy_note: "This page organizes the research landscape. It does not mean that the listed items are already solved."
page_highlights:
  - "P0-P2 fix what counts as success before measurement or implementation work is discussed."
  - "The index allows readers to jump directly to a specific question family."
  - "Stronger claims are deliberately placed later so earlier levels are not skipped."
  - "R3 / R5 separate latent-state and maintenance-state questions by evidence tier and timescale, so same-day fit and multiday maintenance do not collapse into one success."
  - "M2 separates hardware latency from biological timing-state, so a fast device loop is not confused with timing-complete reconstruction."
  - "M1 / M5 keep neural state distinct from vascular transfer state, so a BOLD amplitude difference is not silently promoted to a neural difference."
  - "R6 treats personalization not as a pure performance trick, but as a verification problem that must separate target signal from subject fingerprint and setup shortcuts."
  - "R4 now treats DCM / effective-connectivity outputs as route-card claims that must disclose model space, observation assumptions, validation, reliability, and abstention."
known_points:
  - "Splitting the problem into P/M/R/I/V/D makes it easier to see which questions are foundational and which sit higher up."
  - "The dependency structure that prevents strong claims from skipping earlier layers is fairly clear."
  - "This page should be read as a dependency map, not as a checklist of solved items."
  - "Even if connectome or local-activity evidence improves, latent-state and maintenance-state audits are still separate requirements."
  - "For hemodynamic modalities, neural interpretation and vascular transfer / CVR audit are separate requirements."
  - "Closed-loop device timing and biological conduction timing are different audits; passing one does not auto-pass the other."
  - "The fact that personalization helps performance is not the same as showing a population-level neural signal; subject-fingerprint and acquisition-distribution audits are still required."
unknown_points:
  - "It is still unsettled which measurement granularity will ultimately be sufficient for WBE."
  - "V5 identity questions and D-series social deployment conditions remain unresolved."
  - "The shortest practical route may change as data and benchmark infrastructure improve."
wiki_links:
  - label: "Wiki: How To Read The Roadmap"
    url: "/wiki/roadmap-reading-guide.html"
    description: "A supporting page for following P/M/R/I/V/D from the basics."
  - label: "Wiki: Reading Routes By L0-L5 Level"
    url: "/wiki/claim-level-reading-routes.html"
    description: "Shows which page to visit next from each level of the claim ladder."
  - label: "Wiki: Reading Partial Solutions, Exploratory Stages, And Unfinished Areas"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "Explains what the status labels on this page are saying is still missing."
  - label: "Wiki: Reading Claims And Evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "Explains in plain language why stronger claims cannot skip earlier layers."
  - label: "Wiki: Why A Connectome Is Not Enough"
    url: "/wiki/connectome-is-not-enough.html"
    description: "Organizes the state variables often missed in the R-series, including synapses, delays, neuromodulation, and glia."
  - label: "Wiki: Observability And Claim Ceiling By Measurement Stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Explains what each modality directly observes and where its claim ceiling appears."
  - label: "Wiki: EEG Preprocessing And QC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "Supplies the basics of preprocessing and quality control that show up in the M-series."
  - label: "Wiki: Identity Evaluation And Continuity Tests"
    url: "/wiki/identity-and-continuity-tests.html"
    description: "Organizes V5 identity through the entry points of memory, values, learning, branching, and longitudinal change."
  - label: "Wiki: State, Trait, And Drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Explains the longitudinal evaluations important for M7/V4 through the differences among state, trait, and drift."
  - label: "Wiki: Update, Branching, And Stop Rules"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "Covers update operations, branch management, and stop conditions needed in I5/I8/V7."
  - label: "Wiki: Closed Loops, Latency, Jitter, And Safety Stops"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Covers latency, jitter, and real-time stability needed in I1/I8."
recommended_pages:
  - label: "WBE 101"
    url: "/wbe_101.html"
  - label: "EEG 101"
    url: "/eeg_101.html"
  - label: "Verification"
    url: "/verification.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Summary</h2>
<p>This page is the map of mind-uploading research. Instead of jumping straight to conclusions, it organizes in sequence <strong>what to measure</strong>, <strong>what to reconstruct</strong>, <strong>how to run it</strong>, and <strong>how to verify it</strong>. In practice, it visualizes where the field currently stands across <strong>measurement -> reconstruction -> implementation -> verification -> social deployment</strong>.</p>
</div>

<div class="note-box">
<strong>For New Readers</strong>
<p>
This page is dense. It is usually easier to read after <a href="wbe_101.html">WBE 101</a> and <a href="eeg_101.html">EEG 101</a>, with the <a href="glossary.html">Glossary</a> nearby if needed.
</p>
</div>

<div class="note-box">
<strong>If The Index Notation Feels Unclear</strong>
<p>
If you want a beginner explanation of the P/M/R/I/V/D notation and their dependency structure, start with <a href="wiki/roadmap-reading-guide.html">Wiki: How To Read The Roadmap</a>. The main text is closer to a map than a dictionary, so a supporting guide helps.
</p>
</div>
<div class="note-box">
<strong>If You Want To Know This Page's Role Among The Theory Pages</strong>
<p>
This page is less a theory essay than a map of dependencies among questions. The entry point for claim levels is <a href="wbe_101.html">WBE 101</a>, the long-form discussion of theory and limits is the <a href="perspective.html">research note</a>, and design principles live in the <a href="perspective.html#design-principles">framework section inside Perspective</a>. For a one-page view of the theory pages as a whole, see <a href="wiki/theory-pages-reading-guide.html">Wiki: Theory Page Reading Guide</a>.
</p>
</div>

<div class="note-box">
<strong>If You Want Only The V5 Identity Entry Point First</strong>
<p>
Identity questions span V5, V7, M7, R5, and related nodes in this roadmap. If you want to sort out in advance how to think about memory, values, learning, branching, and longitudinal continuity, start with <a href="wiki/identity-and-continuity-tests.html">Wiki: Identity Evaluation and Continuity Tests</a>.
</p>
</div>

<div class="note-box">
<strong>If You Get Stuck On Longitudinal Evaluation In M7 / V4</strong>
<p>
State on a given day, relatively stable trait, and drift caused by learning or updates are not the same thing. If you want to sort out the difference between short-term fluctuation and long-term continuity first, see <a href="wiki/state-trait-and-drift.html">Wiki: State, Trait, and Drift</a>.
</p>
</div>

<div class="note-box">
<strong>If You Get Stuck On Operations In I5 / I8 / V7</strong>
<p>
If the differences among safe updates, branch handling, stop rules, and kill switches are unclear, start with <a href="wiki/update-branching-and-stop-rules.html">Wiki: Update, Branching, and Stop Rules</a>. The roadmap points to the issues; the wiki supplies the operational basics.
</p>
</div>

<div class="note-box">
<strong>If You Get Stuck On Closed Loops In I1 / L3</strong>
<p>
Even when something is called "real-time," the difficulty depends on how latency, jitter, end-to-end return, and safety stops are measured. For a beginner entry point to that distinction, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed Loops, Latency, Jitter, and Safety Stops</a>.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck On "Isn't A Connectome Enough?"</strong>
<p>
In the R-series, the branching point is not only the wiring diagram but also how cell types, intrinsic excitability/homeostatic set points, synaptic efficiency, delay and myelination, neuromodulation, and glia are treated. If you want to see from primary literature which claims fail when those state variables are missing, see <a href="wiki/connectome-is-not-enough.html">Wiki: Why a Connectome Is Not Enough</a> and <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic Plasticity and Maintenance State</a>.
</p>
</div>
<div class="note-box">
<strong>If You Get Stuck On Terms Like Missing, Unfinished, Or Partially Solved</strong>
<p>
This page uses short status labels for what is still lacking in each node. If you want to clarify what <strong>partially solved</strong>, <strong>exploratory</strong>, <strong>not yet standardized</strong>, and <strong>unfinished</strong> each mean, start with <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: Reading Partial Solutions, Exploratory Stages, and Unfinished Areas</a>.
</p>
</div>
<div class="note-box">
<strong>If You Want To Organize Return Paths By Claim Ladder Level</strong>
<p>
Because Roadmap covers all of L0-L5, the next public page depends on which level you want to inspect now. For a one-page route map by claim level, see <a href="wiki/claim-level-reading-routes.html">Wiki: Reading Routes By L0-L5 Level</a>.
</p>
</div>
<div class="note-box">
<strong>If You Want To Choose The Next Single Page After This One</strong>
<p>
If you want a one-page view of where to go next after Roadmap, measurement, reconstruction, implementation, verification, or social deployment, see <a href="wiki/roadmap-next-routes.html">Wiki: Five Routes After the Roadmap</a>.
</p>
</div>

<div class="key-points">
<h4>Three Things To Fix First</h4>
<ul>
<li><strong>This page's role:</strong> not to declare conclusions, but to fix where each question lives.</li>
<li><strong>What this page can do:</strong> organize current research problems with order and dependencies attached.</li>
<li><strong>What this page cannot do alone:</strong> it cannot prove that the final questions of identity or consciousness are already settled.</li>
</ul>
</div>

<table class="data-table">
<thead>
<tr>
<th>Symbol</th>
<th>What It Groups Together</th>
<th>Read It First When...</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>Definition of progress. It decides what counts as success.</td>
<td>You want to align on the target before entering technical discussion.</td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>Measurement. It covers what can be observed, and at what precision.</td>
<td>You want to start from the differences among EEG, fMRI, invasive measurement, and related modalities.</td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>Reconstruction. It covers what can be estimated from observations.</td>
<td>You are interested in inverse problems, latent state, causal models, or uncertainty.</td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>Implementation. It covers how models run and where they break.</td>
<td>You want to inspect closed loops, latency, computational load, or safety design.</td>
</tr>
<tr>
<td><strong>V</strong></td>
<td>Verification. It covers what must be measured for progress and what counts as failure.</td>
<td>You want benchmarks, causal tests, identity questions, or replication criteria.</td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>Deployment. It covers rights, consent, fairness, and security.</td>
<td>You want to read beyond the technical layer into operations and institutions.</td>
</tr>
</tbody>
</table>

<section class="section" id="howto">
<h2 class="section-title">How to Use</h2>
<p>This page is not a book but a <strong>map</strong> of the full research landscape. First read through the question tree, then deepen each node according to the learning order. Only two operational rules are essential here: <strong>(1) keep the source links</strong> and <strong>(2) explicitly mark what remains provisional or uncertain</strong>.</p>
</section>

<section class="section" id="measurement-identifiability-audit">
<h2 class="section-title">2026-03 Literature audit: Three walls of measurement, identification, and intervention</h2>
<p>
In this re-audit, we focused on updating <strong>M3 (spatial granularity)</strong>, <strong>M6 (intervention design)</strong>, <strong>R7 (identifiability)</strong>, and <strong>V2 (causal testing)</strong> in this roadmap. The reason is simple: the most common misinterpretations in technical discussions surrounding WBE are to read <strong>increase in observables</strong> as <strong>state completeness</strong>, to read <strong>increase in prediction performance</strong> as <strong>obtaining a unique solution</strong>, and to read <strong>introducing one intervention</strong> as <strong>the completion of causal verification</strong>. The following three are lower limits that are relatively consistently supported by primary literature as of March 2026.
</p>
<table class="data-table">
<thead>
<tr>
<th>Wall</th>
<th>What the primary literature now supports</th>
<th>Revision policy on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Measurement granularity wall</strong></td>
<td>EEG / MEG provide global current-field measurements, while fMRI provides hemodynamic proxies, so what we obtain non-invasively in humans is basically macroscopic observation. By contrast, Dorkenwald et al. (2024) and MICrONS Consortium et al. (2025) advance structure-function correspondence in model organisms and local cortex, not state-complete measurement of the human whole brain. </td>
<td>In M3, ``what is directly visible and what remains latent'' is fixed for each granularity, and structural scaffolding and state completeness are written separately. </td>
</tr>
<tr>
<td><strong>Identifiability Wall</strong></td>
<td>Although progress has been made in direct validation of HD-EEG/ESI, Seeber et al. (2019), Unnwongse et al. (2023), and Hao et al. (2025) demonstrate conditional detectability and auditability of localized errors, not general unique recovery of internal states. The conclusion changes depending on the source depth, conductivity assumption, head model, and stimulation conditions. </td>
<td>R7 defines predictability, localization, and identity as separate levels, and requires family comparison and abstention conditions. </td>
</tr>
<tr>
<td><strong>Intervention validation wall</strong></td>
<td>TMS-EEG, phase-locked stimulation, adaptive DBS, and BCI closed loops are all strong evidence routes, but as Hernandez-Pavon et al. (2023), Zrenner et al. (2018), and Wilson et al. (2010) show, comparisons fail unless stimulation site, intensity, masking, artifact windows, and latency / jitter measurements are fixed. Intervention evidence is therefore tiered rather than binary. </td>
<td>In M6 and V2, we stage passive observation, held-out perturbation, online loop, local causal intervention, and long-term closed loop, and make request logs explicit. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Points of criticism clarified in this audit</strong>
<p>
Therefore, this roadmap will not allow the three short-circuits of <strong>``It's enough because it's multimodal''</strong>, <strong>``It's unique because it's highly accurate''</strong>, and <strong>``It's causal because it's stimulated''</strong>. The stronger the claim is, the closer to the WBE, the earlier the <strong>measurement granularity</strong>, <strong>candidate model space</strong>, <strong>intervention design</strong>, and <strong>abstention in case of failure</strong> should be made public.
</p>
</div>
</section>

<section class="section" id="roadmap-index">
<h2 class="section-title">Index (keywords → QA)</h2>
<p>You can jump directly to the corresponding QA from the term. The QA-ID is in parentheses. The same anchor is attached to the main text side. </p>

<div class="note-box">
<strong>How to use</strong>
<p>First, use the "Quick Index" to move to the target term, then use the "QA Index by Category" to traverse surrounding nodes. </p>
</div>

<h3>Quick index</h3>
<ul>
<li><a href="#qa-p0">Operational definition (P0)</a></li>
<li><a href="#qa-p1">Claim Stairs (P1)</a></li>
<li><a href="#qa-p2">Delivery template (P2)</a></li>
<li><a href="#qa-m0">Measurement line (non-invasive/invasive/destructive) (M0)</a></li>
<li><a href="#qa-m2">Temporal resolution (M2)</a></li>
<li><a href="#qa-m3">Spatial resolution (M3)</a></li>
<li><a href="#qa-m9">BIDS/Standardization (M9)</a></li>
<li><a href="#qa-r1">Inverse problem (R1)</a></li>
<li><a href="#qa-r3">Latent state (R3)</a></li>
<li><a href="#qa-r4">Causal model (R4)</a></li>
<li><a href="#qa-r7">Identifiability (R7)</a></li>
<li><a href="#qa-r8">Compression and Fidelity (R8)</a></li>
<li><a href="#qa-i1">Closed-loop delay (I1)</a></li>
<li><a href="#qa-i2">Model granularity (I2)</a></li>
<li><a href="#qa-i3">Computational bottleneck (I3)</a></li>
<li><a href="#qa-i5">Safe Update (I5)</a></li>
<li><a href="#qa-i8">containment / stop (I8)</a></li>
<li><a href="#qa-v1">Evaluation Suite (V1)</a></li>
<li><a href="#qa-v2">Causal testing (V2)</a></li>
<li><a href="#qa-v5">Authenticity (V5)</a></li>
<li><a href="#qa-v7">Copy/Branch (V7)</a></li>
<li><a href="#qa-v9">Make-up exam possibility (V9)</a></li>
<li><a href="#qa-d1">Consent and withdrawal (D1)</a></li>
<li><a href="#qa-d2">Access and Equity (D2)</a></li>
<li><a href="#qa-d3">Security (D3)</a></li>
</ul>

<h3>QA index by category (all items)</h3>
<details class="qa-index-group" open>
<summary><strong>Meta (definition of progress)</strong></summary>
<ul>
<li><a href="#qa-p0"><strong>P0</strong> What is the operational definition of "mind upload"? (What do you want to reproduce?)</a></li>
<li><a href="#qa-p1"><strong>P1</strong> Where should I place the claim level (claim ladder)? </a></li>
<li><a href="#qa-p2"><strong>P2</strong> What are the minimum deliverables? (Data, code, evaluation, audit)</a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Measurement</strong></summary>
<ul>
<li><a href="#qa-m0"><strong>M0</strong> Prerequisite for measurement: in vivo / invasive / destructive scan? </a></li>
<li><a href="#qa-m1"><strong>M1</strong> Observed variables: What is the difference between electricity (EEG)/blood flow (fMRI)/spikes (invasive)? </a></li>
<li><a href="#qa-m2"><strong>M2</strong> Lower bound on time resolution: which time scales should be “saved”? </a></li>
<li><a href="#qa-m3"><strong>M3</strong> Lower limit of spatial resolution: Which granularity (region/column/neuron/synapse) should we aim for? </a></li>
<li><a href="#qa-m4"><strong>M4</strong> Whole brain coverage: How much of the “whole” do we need to measure? </a></li>
<li><a href="#qa-m5"><strong>M5</strong> Multimodal integration: how to guarantee alignment (MRI/EEG/fMRI)? </a></li>
<li><a href="#qa-m6"><strong>M6</strong> Intervention/stimulus: What is the “experimental design” that increases the possibility of identification? </a></li>
<li><a href="#qa-m7"><strong>M7</strong> Longitudinal: Are “personal characteristics” stable against intra-day/day-to-day fluctuations? </a></li>
<li><a href="#qa-m8"><strong>M8</strong> Quality control: How to “quantify” and handle artifacts/missing/noise? </a></li>
<li><a href="#qa-m9"><strong>M9</strong> Standardization: How can I use BIDS/metadata to make it “possible for others to try again”? </a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Reconstruction</strong></summary>
<ul>
<li><a href="#qa-r0"><strong>R0</strong> What is the minimum set to restore? (Structure/state/learning rule)</a></li>
<li><a href="#qa-r1"><strong>R1</strong> Inverse problem: What can be uniquely inferred from observations (M1)? </a></li>
<li><a href="#qa-r2"><strong>R2</strong> Source estimation: “Which expression” of brain activity do you want from EEG? </a></li>
<li><a href="#qa-r3"><strong>R3</strong> State estimation: How to define latent state and how to verify it? </a></li>
<li><a href="#qa-r4"><strong>R4</strong> Causation: What models can predict response to an intervention? </a></li>
<li><a href="#qa-r5"><strong>R5</strong> Plasticity: What is the boundary between “introducing” and “not including” learning rules? </a></li>
<li><a href="#qa-r6"><strong>R6</strong> Personalization: general model + individual parameters? Or is it completely individual? </a></li>
<li><a href="#qa-r7"><strong>R7</strong> Identifiability: Does estimation approach the “unique solution”? What about uncertainty? </a></li>
<li><a href="#qa-r8"><strong>R8</strong> Compression: Can you maintain the “verification standard” even if you discard any information? </a></li>
<li><a href="#qa-r9"><strong>R9</strong> Audit: What is the mechanism to “record” model differences and failure examples? </a></li>
<li><a href="#qa-r10"><strong>R10</strong> Neuromodulation: How to incorporate mood, alertness, and volume transmission? </a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Implementation</strong></summary>
<ul>
<li><a href="#qa-i0"><strong>I0</strong> Execution platform: Which one are you aiming for: general-purpose computing/GPU/HPC/neuromorphic? </a></li>
<li><a href="#qa-i10"><strong>I10</strong> Time continuity: Discrete time (RNN) or continuous time (ODE)? </a></li>
<li><a href="#qa-i1"><strong>I1</strong> Closed loop: How many ms of delay is allowed in real time? </a></li>
<li><a href="#qa-i2"><strong>I2</strong> Model granularity: where do you fight between spiking/rate/abstraction? </a></li>
<li><a href="#qa-i3"><strong>I3</strong> Computation amount: Where are the bottlenecks in memory/power/parallelization? </a></li>
<li><a href="#qa-i4"><strong>I4</strong> Initialization: How to give the “initial state” of the model? </a></li>
<li><a href="#qa-i5"><strong>I5</strong> Learning and drift: How to design “safe updates” for learning? </a></li>
<li><a href="#qa-i6"><strong>I6</strong> Embodiment: How much input/output (sensors/movement/language) should we have? </a></li>
<li><a href="#qa-i7"><strong>I7</strong> Reproducibility: Is there a guarantee that the results will not change due to implementation differences (language/hardware)? </a></li>
<li><a href="#qa-i8"><strong>I8</strong> Safety: How to create isolation, monitoring, and containment? </a></li>
<li><a href="#qa-i9"><strong>I9</strong> Thermodynamics: Can digital infrastructure pay for the “physical cost of consciousness”? </a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Verification</strong></summary>
<ul>
<li><a href="#qa-v0"><strong>V0</strong> Verification target: Which of identity, consciousness, or behavior should be verified “engineeringly”? </a></li>
<li><a href="#qa-v1"><strong>V1</strong> Evaluation Suite: What should we measure as “progress”? (Pre-registration)</a></li>
<li><a href="#qa-v2"><strong>V2</strong> Causal testing: Can the stimulus/intervention produce the “same response”? </a></li>
<li><a href="#qa-v3"><strong>V3</strong> Generalization: Can you maintain your “identity” even in out-of-distribution (OOD)? </a></li>
<li><a href="#qa-v4"><strong>V4</strong> Long-term: How do you evaluate the handling of learning, drift, and forgetting? </a></li>
<li><a href="#qa-v5"><strong>V5</strong> Identity: What is “causal identity” that goes beyond psychological continuity? </a></li>
<li><a href="#qa-v6"><strong>V6</strong> Consciousness: To what extent can theory-dependent predictions be made “testable”? </a></li>
<li><a href="#qa-v7"><strong>V7</strong> Copy/branch: How should the “principal” be handled if multiple instances run? </a></li>
<li><a href="#qa-v8"><strong>V8</strong> LLM/Distinction from imitation: How do you judge whether the external appearance is similar but the contents are different? </a></li>
<li><a href="#qa-v9"><strong>V9</strong> Make-up exam: Is the design designed to allow a third party to reach the “same conclusion”? </a></li>
<li><a href="#qa-v10"><strong>V10</strong> Model distance: How do we measure the “closeness” between the biological brain and emulation? </a></li>
<li><a href="#qa-v11"><strong>V11</strong> Topology: Is the “structure” of consciousness conserved? </a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Deployment (social implementation)</strong></summary>
<ul>
<li><a href="#qa-d0"><strong>D0</strong> Ethical Framework: What are the rights of emulated beings? </a></li>
<li><a href="#qa-d1"><strong>D1</strong> Consent and withdrawal: How do we design informed consent? </a></li>
<li><a href="#qa-d2"><strong>D2</strong> Access and equity: who should have access to WBE? </a></li>
<li><a href="#qa-d3"><strong>D3</strong> Security: How to design for exploitation risks and controls? </a></li>
</ul>
</details>

</section>

<section class="section" id="definition" data-qa-group>
<h2 class="section-title">Definition of forward movement (fixed at the beginning)</h2>
<p>In order to claim "progress", it is first necessary to decide <strong>what can be reproduced to win</strong> (=evaluation axis) and<strong>what should happen to lose</strong> (=falsification conditions). Here, we will compress the underlying questions into three questions. </p>

<details open class="qa" data-tags="meta" id="qa-p0">
<summary>
<span class="qa-id">P0</span>
<span class="qa-title">What is the operational definition of "mind upload"? (What do you want to reproduce?)</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>How does this site treat “mind uploading / WBE”? (Is it only the behavior that can be seen from the outside? / Is it the internal causal structure? / Does it include the identity and consciousness?)</p>
<p><strong>Branch (example):</strong>(A) Reproduction of behavior/function (equivalent to black box) / (B) Reproduction of neural dynamics (emphasis on content) / (C) Includes continuity of individuality and subjectivity (strong assertion)</p>
<p><strong>Falsifiability:</strong>If we talk about results without vague definitions, evaluation becomes an “afterthought” and comparison of progress becomes impossible</p>
<p><strong>Next:</strong> Use the "Verification" node on this page to determine the <strong>measurable criteria</strong> and <strong>loss conditions</strong> for (A), (B), and (C).</p>
</div>
</details>

<details open class="qa" data-tags="meta" id="qa-p1">
<summary>
<span class="qa-id">P1</span>
<span class="qa-title">Where to place the claim level (claim staircase)? </span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>At what level should research results be considered "progress"? </p>
<ul>
<li><strong>L0:</strong>Data collection and reproducible analysis (standardization, quality control, retestability)</li>
<li><strong>L1:</strong>Decoding/encoding (neural → action/stimulus or vice versa prediction)</li>
<li><strong>L2:</strong>Generative model (can extrapolate neural/behavioral behavior even under unlearned conditions and predict interventions)</li>
<li><strong>L3:</strong>Closed-loop implementation (interacts with the environment in real time and operates stably)</li>
<li><strong>L4:</strong>Assertion of identity (assessing continuity of memory, values, and learning using pre-registered criteria)</li>
<li><strong>L5:</strong>Social implementation (rights, safety, and governance are established at the same time as technology)</li>
</ul>
<p><strong>Falsifiability:</strong>Preventing talking about “achieving L1” as “achieving L4” (switching scope)</p>
<p><strong>Next:</strong> Match the "required data", "required model", and "evaluation suite" for each level on this page</p>
</div>
</details>

<details open class="qa" data-tags="meta" id="qa-p2">
<summary>
<span class="qa-id">P2</span>
<span class="qa-title">What are the minimum deliverables? (Data/Code/Evaluation/Audit)</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>What must remain in order to make “progress” reproducible? </p>
<ul>
<li><strong>Data:</strong>Raw data + metadata (BIDS etc.) + anonymization/consent log</li>
<li><strong>Code:</strong>Fixed version analysis pipeline (including environment and dependencies)</li>
<li><strong>Evaluation:</strong>Pre-registered indicators/tests/baseline comparison</li>
<li><strong>Audit:</strong>Model differences, reproduction execution logs, failure examples (negative results)</li>
</ul>
<p><strong>Falsifiability:</strong>Only the “how to present” the results takes precedence, making the claim unverifiable</p>
<p><strong>Next:</strong> First, lock down the L0-L2 deliverable template for Mind-Upload, including data structure and evaluation scripts.</p>
</div>
</details>
</section>

<section class="section" id="tree">
<h2 class="section-title">Tree of questions (detailed version: consolidated on one page)</h2>
<p>Below, we will break down the technical questions into "measurement → reconstruction → implementation → verification → social implementation" and summarize them all on one page. Each item is collapsible (click to expand). </p>
<div class="key-points">
<h4>The shortest course for those who are lost</h4>
<ul>
<li><strong>People who want to know the whole picture first:</strong><a href="#qa-p0">P0</a> → <a href="#qa-m0">M0</a> → <a href="#qa-r1">R1</a> → <a href="#qa-v1">V1</a> If you read them in this order, you will understand in one go what to measure, restore, and verify. </li>
<li><strong>For those who want to start with EEG:</strong>Reading in the order of <a href="#qa-m0">M0</a> → <a href="#qa-m2">M2</a> → <a href="#qa-m9">M9</a> → <a href="#qa-v1">V1</a> will make it easier to follow from measurement conditions to evaluation. </li>
<li><strong>For those who want to start with the topic of identity:</strong><a href="#qa-p1">P1</a> → <a href="#qa-v5">V5</a> → <a href="#qa-v7">V7</a> → <a href="#qa-d1">D1</a> If you read in this order, you will see the conditions necessary for a strong argument and the institutional barriers. </li>
</ul>
</div>

<div class="node" id="measurement" data-qa-group>
<div class="node-kicker">1. Measurement</div>
<h3>Measurement: What resolution do you need? </h3>
<p class="mini"><strong>Central question:</strong> "What part of the brain, and at what spatiotemporal resolution, should be taken to arrive at a unique object to be reconstructed?"</p>

<details open class="qa" data-tags="measurement" id="qa-m0">
<summary>
<span class="qa-id">M0</span>
<span class="qa-title">Assumptions for measurement: In vivo / invasive / destructive scan? </span>
<span class="qa-tags"><span class="tag">MEASUREMENT</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Based on safety and scale constraints, fix "what to aim for" on which measurement route. </p>
<p><strong>Branch (example):</strong>(A) Train the model with non-invasive (EEG/MEG/fMRI) / (B) Strengthen causal inference with invasive (ECoG/deep/animal) / (C) Obtain structure with destructive/ultra-high resolution (future vision)</p>
<p><strong>Conditions for disproving: </strong>Even if only the measurement is “sophisticated” without the purpose (restored object) being defined, identification will become impossible</p>
<p><strong>Next:</strong> Determine R0 (restore target) and V0 (verification criteria) on this page first</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m1">
<summary>
<span class="qa-id">M1</span>
<span class="qa-title">What is the difference between observed variables: electricity (EEG)/blood flow (fMRI)/spikes (invasive)? </span>
<span class="qa-tags"><span class="tag">EEG</span><span class="tag">FMRI</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> When the observation changes, the recoverable target also changes, whether structure, state, or learning rule. What can be identified from which observations? </p>
<p><strong>Issues:</strong> Time-series speed, spatial resolution, ease of causal intervention, whole-brain coverage, and cost.</p>
<table class="data-table">
<thead>
<tr>
<th>Observation route</th>
<th>What is directly observed</th>
<th>I can say this relatively strongly</th>
<th>Latent state that remains as it is</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG</strong></td>
<td>It is a mixed field of globally synchronized currents. </td>
<td>You can follow ms-scale state transitions, global dynamics for each frequency band, and closed-loop time constraints. </td>
<td>The uniqueness of deep sources, cell type, neuromodification, glial status, and current synaptic efficiency are not directly determined. </td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>Hemodynamic proxy. </td>
<td>Region-scale recruitment, relatively slow network state, and wide coverage within the same individual are easy to see. </td>
<td>ms-scale timing, excitatory/inhibitory separation, fast intervention responses, and the separation of neural change from vascular transfer state / CVR are not directly visible. </td>
</tr>
<tr>
<td><strong>whole-brain spatial transcriptomics / cell atlas</strong></td>
<td>Ex vivo molecular labels and spatial arrangement. </td>
<td>You can enhance the cell-type taxonomy, distribution by region, and molecular map on the structural atlas. </td>
<td>Current firing rules, synaptic efficiency, neuromodulatory/glial state, and sleep-history are not directly determined. </td>
</tr>
<tr>
<td><strong>Patch-seq / morpho-electric-transcriptomics</strong></td>
<td>Compatible with single cell transcriptome, morphology, and electrophysiology. </td>
<td>It bridges the cell-type label and morpho-electric phenotype, and strengthens the parameter prior of the local circuit. </td>
<td>Whole-brain coverage, same-brain circuit context, current network state, and longitudinal plastic history remain. </td>
</tr>
<tr>
<td><strong>ECoG / SEEG</strong></td>
<td>Local field potential of the indwelling site and intervention response. </td>
<td>In the covered region, we proceed to local dynamics, stimulus response, and relatively strong causal verification. </td>
<td>Unindwelled areas, whole-brain coverage, and long-term state completeness remain. </td>
</tr>
<tr>
<td><strong>connectomics + same-brain function</strong></td>
<td>Correspondence between structural scaffold and functional response in the same brain. </td>
<td>Wiring rules for local circuits, cell-type dependent connections, and local correspondence between structure and function can be strengthened. </td>
<td>Current synaptic efficiency, intrinsic excitability/homeostatic set point, neuromodulatory fields, glial/metabolic state, and longitudinal plastic history are still separate variables. </td>
</tr>
<tr>
<td><strong>local transmitter / astrocyte imaging</strong></td>
<td>Local transmitter dynamics and astrocyte network response. </td>
<td>Allows better calibration of what a coarse proxy does and does not represent. </td>
<td>Full integration between whole-brain coverage, receptor state, long-timescale maintenance-state, and stack remains. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 Supplement: multimodal is not a synonym for "I could see everything"</strong>
<p>
Mikulan et al. (2020), Seeber et al. (2019), Unnwongse et al. (2023), and Hao et al. (2025) moved forward what can be audited by combining HD-EEG with intracranial ground truth. By contrast, Yao et al. (2023)'s whole-brain spatial atlas, the Patch-seq bridges of Gouwens et al. (2021) and Gamlin et al. (2025), the connectomics of Dorkenwald et al. (2024) and MICrONS Consortium et al. (2025), and the local state imaging of Neyhart et al. (2024) and Cahill et al. (2024) each strengthen different variables while leaving different latent states unresolved. Therefore, this page distinguishes clearly between <strong>increasing the number of observations</strong> and <strong>sufficiently identifying the state variables required for WBE</strong>. For the stack-by-stack layout, see <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: observability and claim ceiling for each measurement stack</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: hemodynamic proxy also has a vascular transfer ceiling</strong>
<p>
For hemodynamic modalities, the remaining uncertainty is not only on the neural side. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> showed that inter-subject CBF / CBV differences contribute to BOLD reactivity, <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> showed that task BOLD magnitude corresponds strongly to CVR across multiple cortical regions, <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> showed that baseline CBF partly explains age-related components of BOLD responses, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can oppose oxygen-metabolism changes across a large fraction of cortex. Therefore, this roadmap does not allow a raw hemodynamic amplitude difference to be promoted directly to a neural difference without a <strong>vascular-state / CVR calibration route</strong> or explicit abstention.
</p>
</div>
<p><strong>Next required:</strong>Same task/same individual, multimodal simultaneous measurement (possible range) + positioning (M5)</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m2">
<summary>
<span class="qa-id">M2</span>
<span class="qa-title">Lower limit on temporal resolution: which time scales should be “saved”? </span>
<span class="qa-tags"><span class="tag">RESOLUTION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>What is the necessary temporal resolution in order not to destroy phenomena related to cognition, learning, and consciousness? </p>
<ul>
<li><strong>Candidates:</strong>ms (spikes/phase), 10-100ms (coupling dynamics), seconds (state transitions), minutes to days (learning/plasticity)</li>
<li><strong>Conditions for disproving:</strong>The time resolution is too coarse, making it impossible to reproduce the intervention response or closed-loop control.</li>
<li><strong>Next:</strong> Measure the acceptable delay in the closed-loop task (I1) and back-calculate the required sampling</li>
</ul>
<div class="note-box">
<strong>There is no single closed-loop time requirement</strong>
<p>
In the re-audit in March 2026, we decided that closed-loop timing requirements should be handled separately for each <strong>loop class</strong>. Slow neurofeedback, ERP/command BCI, phase-locked stimulation, and adaptive DBS have different dominant time scales. Wilson et al. (2010) showed that it is necessary to actually measure the latency/jitter of the entire system using hardware, and Belinskaia et al. (2020) reported that an additional 250 / 500 ms delay in alpha neurofeedback worsens learning. On the other hand, in the phase-targeting systems of Mansouri et al. (2018) and Zrenner et al. (2018), the delay should be evaluated as the <strong>phase error with respect to the target frequency</strong>, rather than the ms value itself.
</p>
<p>
However, the deeper point is that <strong>biological timing is a separate audit from device latency</strong>. <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a> showed that node and internode geometry can be tuned to adjust action-potential timing, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a> showed that perinodal astrocytes can reversibly alter conduction velocity, <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a> showed that saltatory conduction depends on a periaxonal nanocircuit, and <a href="https://doi.org/10.7554/eLife.73827" target="_blank">Dubey et al. (2022)</a> showed that myelination loss in PV axons disrupts fast inhibition and gamma rhythms. A loop can therefore be hardware-fast while still leaving a timing-state latent on the tissue side.
</p>
<ul>
<li><strong>Do not fix the common gate to 1 ms:</strong>Measure the end-to-end median, P95/P99, and worst-case for each loop type. </li>
<li><strong>Audit device and tissue separately:</strong>Hardware latency/jitter does not prove that biological timing-state has been recovered. </li>
<li><strong>The phase system is read by the phase error:</strong>Evaluate the target frequency and the reliability of the estimated phase. </li>
<li><strong>Separate the synchronization system by path:</strong> Separately record where LSL/TTL/photodiode/loopback was measured. </li>
</ul>
<p>
Therefore, in this roadmap, we first fix ``which loop class is handled and which timing failure mode is audited'' rather than ``judging a completely closed loop using a single threshold.'' For information on organizing entrances, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed-loop, delay, jitter, and safety stops</a>.
</p>
</div>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m3">
<summary>
<span class="qa-id">M3</span>
<span class="qa-title">Lower limit of spatial resolution: Which granularity (region/column/neuron/synapse) should we aim for? </span>
<span class="qa-tags"><span class="tag">RESOLUTION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> At what spatial granularity do you assume that the information necessary for “the person's mental functions” resides? </p>
<p><strong>Branch (example):</strong>(A) Inter-area connections + states are sufficient / (B) Local circuits are necessary / (C) Synaptic connections are necessary</p>
<p><strong>Primary literature strongly supports:</strong> Human EEG / MEG / fMRI obtained non-invasively are basically <strong>macro proxies</strong>. EEG / MEG capture globally synchronized current fields, while fMRI captures hemodynamics, so they do not directly observe the state of each neuron or synapse. Conversely, Dorkenwald et al. (2024) and MICrONS Consortium et al. (2025) strengthen the link between high-density connectomics and same-brain function in model organisms and local cortex, but they do not justify claims of “state-complete measurement of the whole human brain.” </p>
<ul>
<li><strong>Upper limit of non-invasive human measurement: </strong>Tracking of region-to-network level state transitions, relatively global timing constraints, and condition differences. </li>
<li><strong>Upper bound on the connectomics front:</strong>This is an audit of structural scaffolds, local functional twins, and cell-type dependent connections, not a complete observation of current synaptic efficiency and neuromodulation fields. </li>
<li><strong>Remaining latent states:</strong>Synaptic weight, receptor state, delay / timing-state, intrinsic excitability / homeostatic set point, neuromodulatory field, glial / metabolic state, and plastic history remain as separate variables. </li>
</ul>
<p><strong>Temporary decision rule:</strong>If the observation path stays in the macro proxy, this roadmap first keeps the assertion between <strong>L1 and weak L2</strong>. In order to raise the claim to local circuits and synaptic granularity, we additionally require either structure/function correspondence in the same brain, external ground truth, or intervention response. </p>
<p><strong>Next, we need:</strong>For each assumption (A), (B), and (C), evaluate observability (M1), identifiability (R7), and computability (I3) in bundles, and disclose what to abstain at which granularity. For background, see <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams are not enough</a> and <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>. </p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m4">
<summary>
<span class="qa-id">M4</span>
<span class="qa-title">Whole brain coverage: How much of the “whole” do we need to measure? </span>
<span class="qa-tags"><span class="tag">COVERAGE</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>How do we handle “boundaries (what is included in the subject)” with limited measurements? </p>
<p><strong>Next:</strong> Operatively place the "boundary of subject" in verification (V0) and clearly state necessary and unnecessary areas</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m5">
<summary>
<span class="qa-id">M5</span>
<span class="qa-title">Multimodal integration: how to guarantee alignment (MRI/EEG/fMRI)? </span>
<span class="qa-tags"><span class="tag">FUSION</span><span class="tag">MRI</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Different measurements have different coordinate systems, delays, and noise structures. Are integration errors destroying the “signal you want to learn”? </p>
<p><strong>Conditions for disproving: </strong>Reconstruction (R2) becomes unstable due to alignment error and reproducibility (P2) decreases</p>
<p><strong>2026-03 supplement:</strong> For EEG + fMRI / fNIRS, a shared clock is still not enough. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> and <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> show that vascular reactivity alters the meaning of task BOLD amplitude, <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> shows that baseline CBF can partially explain age-related BOLD differences, and <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015)</a> show that fNIRS needs short-separation regression to suppress superficial autonomic contamination. Therefore, M5 now treats <strong>vascular-state / CVR calibration or abstention</strong> as part of multimodal alignment for hemodynamic stacks.</p>
<p><strong>Next required:</strong>Does the same data match in multiple pipelines (Analysis differential audit)</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m6">
<summary>
<span class="qa-id">M6</span>
<span class="qa-title">Intervention/Stimulation: What is the “experimental design” that increases the possibility of identification? </span>
<span class="qa-tags"><span class="tag">CAUSAL</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> When identification is not possible through passive observation alone, what kind of intervention (stimulus / task / environmental change) can increase identifiability? </p>
<p><strong>Primary literature strongly supports:</strong> Intervention is not a magic trick that automatically reveals causality. Identifiability increases only in designs that specify <strong>where, when, and how much stimulation was applied</strong>, <strong>how the artifact window was defined</strong>, and <strong>how latency / jitter were measured</strong>. </p>
<ul>
<li><strong>State-targeted stimulation:</strong> As in Zrenner et al. (2018), conditioning the stimulation time on brain state makes response differences easier to detect even for the same nominal stimulus. </li>
<li><strong>Interventions with ground-truth:</strong>Intracranial stimulation, simultaneous SEEG/ECoG, phantoms, and animal experiments can calibrate estimation errors on the scalp side with external standards. </li>
<li><strong>Closed-loop intervention:</strong>With BCI and adaptive stimulation, response differences cannot be interpreted as causal differences unless we measure not only mean latency but also jitter and worst-case path, as shown by Wilson et al. (2010). </li>
</ul>
<p><strong>What does not count as an intervention:</strong>Conditional differences in passive tasks, post-hoc cross-modal correlations, and offline analyzes without stimulus logs alone do not count as strong causal evidence on this page. </p>
<p><strong>Externally dependent tasks:</strong>TMS/DBS/invasive interventions on real subjects require IRB, equipment, and clinical cooperation. The first thing to do in this repository is to prepare the <strong>intervention grammar</strong>, <strong>synchronization log format</strong>, <strong>stop conditions in case of failure</strong>, and <strong>comparison rules</strong>. </p>
<p><strong>Next, we need:</strong> On the model (R4) side, perform a design back calculation that says ``This intervention will improve the discrimination between families,'' and fix the submission pack that includes where TTL / LSL / photodiode / loopback was measured. </p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m7">
<summary>
<span class="qa-id">M7</span>
<span class="qa-title">Longitudinal: Are “personal characteristics” stable against intra-day/day-to-day fluctuations? </span>
<span class="qa-tags"><span class="tag">LONGITUDINAL</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Even in the same individual, brain states vary. Which characteristics are strong enough to make us unique? </p>
<p><strong>Conditions for disproving:</strong>Reproducibility is limited to “the state of the day” and long-term identity evaluation (V5) is not possible</p>
<p><strong>Next:</strong>Tracking a predefined identification score (V1) across multiple sessions of the same subject</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m8">
<summary>
<span class="qa-id">M8</span>
<span class="qa-title">Quality control: How to “quantify” and handle artifacts/missing/noise? </span>
<span class="qa-tags"><span class="tag">QC</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Define “good data” in advance and make exclusion, complementation, and weighting transparent. In addition, how do we quantify <strong>quality deterioration</strong> caused by hardware, such as impedance/CMRR, noise floor, HMD interference, etc.? </p>
<ul>
<li><strong>Impedance/CMRR:</strong> Detects imbalance and warns before measurement. </li>
<li><strong>Noise floor/SNR:</strong> Visualize the effective SNR for each frequency band. </li>
<li><strong>VR Interference:</strong> Profile HMD electromagnetic and mechanical noise. </li>
</ul>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m9">
<summary>
<span class="qa-id">M9</span>
<span class="qa-title">Standardization: How can BIDS/metadata be used in a format that allows others to retest? </span>
<span class="qa-tags"><span class="tag">BIDS</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Even if the data can be shared, it is not possible to retest if the metadata is weak. What should be converted into metadata at least? </p>
<p><strong>Supplement (Issue #46):</strong> If VR/motion measurement is included, specify the coordinate system, time synchronization, and device specifications according to <strong>Motion-BIDS</strong>. </p>
<p><strong>Next:</strong> Leave the protocol (task/equipment/preprocessing) machine readable (P2)</p>
</div>
</details>
</div>

<div class="node" id="reconstruction" data-qa-group>
<div class="node-kicker">2. Reconstruction</div>
<h3>Reconfigure: What to restore? (Circuit/state/learning rule)</h3>
<p class="mini"><strong>Central question:</strong> "To what extent is structure (coupling), dynamic state (activity), and learning rules (plasticity) necessary for the individual's mental functions?"</p>

<details open class="qa" data-tags="reconstruction" id="qa-r0">
<summary>
<span class="qa-id">R0</span>
<span class="qa-title">What is the minimum set to restore? (Structure/state/learning rule)</span>
<span class="qa-tags"><span class="tag">RECONSTRUCTION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>How far do I have to restore to win in verification (V0)? </p>
<p><strong>Branching (example):</strong>(A) Structure + state (fixed) / (B) Structure + state + partial plasticity / (C) Fully dynamic, including plasticity</p>
<p><strong>False condition: </strong>Closed-loop learning (I5) cannot be reproduced in (A), cannot be identified in (B) and (C) and fails due to overfitting</p>
<p><strong>Next:</strong>Evaluate identifiability (R7) and computability (I3) simultaneously</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r1">
<summary>
<span class="qa-id">R1</span>
<span class="qa-title">Inverse problem: What can be uniquely inferred from observation (M1)? </span>
<span class="qa-tags"><span class="tag">INVERSE</span><span class="tag">BAYES</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> An inverse problem such as EEG source estimation is “ill-posed,” meaning the solution is not uniquely determined. Therefore, it is more important to audit <strong>how stable the conclusion remains when geometry, conductivity, electrode coordinates, and prior assumptions change</strong> than to ask <strong>which solver was chosen</strong>. </p>
<p><strong>Policy:</strong> In this project, no specific solver is fixed as the standard solution. Acceptance requires (1) an explicit uncertainty expression such as a posterior distribution, confidence interval, or bootstrap / ensemble range, (2) sensitivity analysis for individual MRI, FEM / BEM, conductivity assumptions, and electrode geometry, and (3) external validation using simulation, phantoms, simultaneous invasive recording, or intracranial stimulation. Bayesian or empirical-Bayes approaches are good candidates, but auditability matters more than the method name. </p>
<p><strong>Next, we need:</strong> In R2 and R7, isolate how much source depth, cranial conductivity, and candidate model space dominate the error, and disclose abstention conditions rather than forcibly collapsing overlapping solutions into one. </p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r2">
<summary>
<span class="qa-id">R2</span>
<span class="qa-title">Source estimation: “Which representation” of brain activity do you want from EEG? </span>
<span class="qa-tags"><span class="tag">EEG</span><span class="tag">ESI</span><span class="tag">BAYES</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> EEG source estimation is easy to obtain an expression of "area x time", but neurons/synapses cannot be directly seen. Select the expression according to the restoration target (R0). </p>
<p><strong>Issue:</strong>In the past, "high-density EEG (128 channels)" was recommended, but recent research has shown that ill-posedness cannot be solved by the number of channels alone. In particular, point estimation methods such as dSPM ignore uncertainty. </p>
<p><strong>Stricter policy:</strong>Estimation with uncertainty such as the Block-Champagne system, <strong>high-density EEG</strong>, and <strong>FEM/BEM forward model based on individual MRI</strong> are effective means to improve estimation conditions. However, these do not guarantee the accuracy of<strong>deep brain activity</strong>. The hiring condition is not that it can be said to be able to see deeply, but rather that it is able to audit which error sources have been reduced and to what extent. Therefore, submissions must include (1) posterior distributions or confidence intervals, (2) sensitivity analysis of conductivity, electrode coordinates, and head model, (3) validation against external criteria such as simulations/phantoms/concurrent invasive recordings/intracranial stimulation, and (4) conditions for withholding claims regarding deep sources. </p>
<p><strong>Next:</strong>Firstly, fix <strong>source imaging verification specifications</strong> and <strong>benchmarks with external standards</strong> without making it unclear whether or not they are publicly implemented. The implementation will then be made public in a form that allows for reproduction, including posterior distribution, sensitivity analysis, and failure examples. </p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r3">
<summary>
<span class="qa-id">R3</span>
<span class="qa-title">State estimation: How to define latent state and how to verify it? </span>
<span class="qa-tags"><span class="tag">STATE</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Can we separate observation noise from the true state and show that the state is “effective for prediction”? </p>
<p><strong>False condition:</strong>The latent state only serves to compress data and does not contribute to intervention prediction (R4)</p>
<p><strong>Next:</strong>Assess extrapolation in unlearned conditions and prediction error of intervention response</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r4">
<summary>
<span class="qa-id">R4</span>
<span class="qa-title">Causation: What models can predict response to intervention? </span>
<span class="qa-tags"><span class="tag">CAUSAL</span><span class="tag">MULTI-SCALE</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Rather than just applying correlations, can we say ``what should change'' in response to changes in stimuli or conditions? What chain of evidence should we use to make the leap from decoding (correlation) to emulation (causation)? </p>
<p><strong>Policy:</strong>This project treats Active Inference, DCM, state-space models, SCM, and mechanistic circuit models as <strong>competitive candidate sets</strong>. DCM is useful for comparing candidate generation models, and SCM is useful for describing interventions and counterfactuals, but neither is an automatic causal detector on its own. If only observational data is used, equivalence classes remain, so we require <strong>clarification of candidate model space</strong>, <strong>family-level comparison</strong>, <strong>model recovery</strong>, and <strong>held-out perturbation prediction</strong>. </p>
<p><strong>2026-03-19 addendum:</strong>The weakness of the older wording was that <strong>candidate model space</strong> remained a slogan rather than an operational gate. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">Penny et al. (2004)</a> already fixed that DCM inference is relative to the compared models, <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">Rosa et al. (2012)</a> showed that very large model spaces can be searched efficiently from a full model, <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">Frässle et al. (2021)</a> scaled directed-connectivity estimation to whole-brain human fMRI, and <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Wu et al. (2024)</a> accelerated regression-style DCM further. But that progress is progress in <strong>tractability</strong>, not an automatic solution to identifiability. Even whole-brain or faster effective-connectivity estimates still depend on the chosen node set, priors, hemodynamic assumptions, omitted alternatives, and validation design.</p>
<p><strong>Effective-connectivity route card required:</strong>Any R4 claim using DCM or a related effective-connectivity estimator must publish (1) compared node set plus omitted competitors, (2) neural-mass / HRF / prior assumptions, (3) family comparison and model recovery, (4) held-out perturbation or external validation, (5) test-retest window and condition dependence, and (6) abstention boundary. If those are missing, this roadmap stops at <strong>model-conditioned causal hypothesis</strong> and does not promote the result to discovered causal wiring or WBE-relevant causal structure.</p>
<p><strong>Improvement measures (positioning of Multi-scale):</strong> Multi-scale integration is a promising expansion route, but it should not be the default route. Even when passing EEG-derived macroconstraints to a circuit model, acceptance or rejection is not determined by the "theory name" but by prediction improvement for stimuli, lesions, and task perturbations, OOD generalization, and transparency of abstention conditions. </p>
<p><strong>Stricter implementation (Issue #52):</strong> The uncertainty obtained in the inverse problem (R1/R2) is explicitly propagated to the subsequent model. However, what we are fixing here is not the precision implementation of Active Inference itself, but rather the<strong>upstream uncertainty does not disappear downstream</strong>. The implementation differences between candidate theories are compared on the same bench. </p>
<p><strong>Next:</strong> Combine the Intervention Premise Evaluation Task (V2), Model Space Declaration, Family Comparison, and Perturbation Bench with External Validation into one deliverable pack. </p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r5">
<summary>
<span class="qa-id">R5</span>
<span class="qa-title">Plasticity: What is the boundary between “introducing” and “not including” learning rules? </span>
<span class="qa-tags"><span class="tag">PLASTICITY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>If we are dealing with long-term identity (V5), we have to include learning (renewal). However, with updates, verification becomes difficult. </p>
<p><strong>Branch (example):</strong>(A) Do not learn (fixed model) / (B) Learn with restrictions (safe update) / (C) Infer to learning rule</p>
<p><strong>Next required:</strong>Drift monitoring (V4) when learning is included and safety measures (I8)</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r6">
<summary>
<span class="qa-id">R6</span>
<span class="qa-title">Personalization: General model + individual parameters? Or is it completely individual? </span>
<span class="qa-tags"><span class="tag">PERSONALIZATION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Personalization is unavoidable when discussing identity. On the other hand, too much personalization leads to overfitting and broken reproducibility.</p>
<p><strong>2026-03-18 addendum:</strong>The reason this section was deepened is that if personalization is read only as a trick for improving performance, the distinction between the <strong>target neural variable</strong> and a <strong>subject / session fingerprint</strong> collapses. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> showed that diagnosis learning can absorb subject characteristics when repeated measures are not participant-disjoint, <a href="https://doi.org/10.1016/j.patcog.2020.107381" target="_blank">Wang et al. (2020)</a> and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> showed time-robust person identification from resting-state EEG alone, and <a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">Gibson et al. (2022)</a> summarized strong subject-driven EEG variation. The same boundary also extends to acquisition distribution: <a href="https://doi.org/10.1088/1741-2552/aacfe4" target="_blank">Hu et al. (2018)</a> showed that reference montage and electrode setup alter scalp potentials, <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017)</a> showed that system / subject / session all influence EEG, and <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a> showed that cross-dataset variability is driven in part by amplifier, cap, sampling rate, and filtering differences. The real boundary in R6 is therefore <strong>how much individual difference a given claim is allowed to use</strong> and <strong>how population signal is separated from fingerprint and setup routes</strong>.</p>
<table class="data-table">
<thead>
<tr>
<th>Route</th>
<th>What can be read relatively safely at this route</th>
<th>Minimum deliverables</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>(A) shared model + subject-disjoint evaluation</strong></td>
<td>Whether a person-independent signal remains and how far population-level generalization can be established.</td>
<td>Leave-one-subject-out / leave-one-session-out, raw-recording ancestry, subject/session/site/device/reference-system/electrode-layout metadata-only baselines, a fingerprint classifier, harmonization logs, and an explicit guarantee that windows cut from the same raw recording do not cross train/test.</td>
</tr>
<tr>
<td><strong>(B) shared encoder + light subject adaptation</strong></td>
<td>How much calibration is needed to land a shared representation on the target subject.</td>
<td>Frozen vs trainable parts, adaptation budget, when target-subject data is introduced, pre/post-adaptation scores, fixed decoder horizon, and cross-day degradation plus recalibration burden.</td>
</tr>
<tr>
<td><strong>(C) fully subject-specific decoder / controller</strong></td>
<td>How far a participant-conditioned communication / control route works for that individual.</td>
<td>Training time, cooperation burden, within-subject hold-out, cross-day hold-out, silence / abstention behavior, recalibration burden, and an explicit ceiling that does not claim other-person generalization.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Site rule for this section</strong>
<p>
On this site, any result that calls itself a diagnosis model, state biomarker, or general decoder must report at least <strong>(1) split independence unit</strong>, <strong>(2) raw-recording / window ancestry</strong>, <strong>(3) subject / session / site / device / reference-system / electrode-layout disjointness</strong>, <strong>(4) metadata-only or fingerprint baselines</strong>, <strong>(5) the harmonization log for channel map / reference / sample rate / filters</strong>, <strong>(6) when target-subject or target-site data was used</strong>, and <strong>(7) the adaptation budget</strong>. Without that, the result is treated first as a <strong>subject-aware classifier</strong>, <strong>participant-conditioned decoder</strong>, or <strong>fingerprint/setup-unresolved biomarker</strong>, not as a population marker or a subject-independent mechanism.
</p>
</div>
<p><strong>Branch example:</strong> Route (A) asks whether any population signal is present, route (B) asks how much transfer plus calibration burden is needed, and route (C) asks whether an individual route is operationally usable. Therefore, the fact that personalization scores higher is neither a success nor a failure by itself; it only becomes interpretable after you state <strong>which claim family you want to support</strong> and <strong>how far fingerprint and setup routes were controlled</strong>.</p>
<p><strong>Next required:</strong>Bundle the <a href="verification.html#specificity-shortcut-card">Verification: Specificity &amp; Shortcut Card</a>, the evaluation-family and split design on <a href="datasets.html">Datasets</a>, and the <a href="verification.html#temporal-validity-card">Temporal Validity Card</a> so same-subject success, cross-subject generalization, and cross-day maintenance are managed as different deliverables.</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r7">
<summary>
<span class="qa-id">R7</span>
<span class="qa-title">Identifiability: Does estimation approach the “unique solution”? What about uncertainty? </span>
<span class="qa-tags"><span class="tag">IDENTIFIABILITY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>When there are many different models that explain the same observation, which assumptions can be used to narrow it down? Where does the uncertainty come from: sensor geometry, conductivity, preprocessing, candidate model ensembles, and intervention design? </p>
<p><strong>Recondition:</strong>If the conclusion is significantly reversed due to small preconditioning differences, conductivity assumptions, or changes in the candidate model space, or cannot be recovered using held-out perturbations or external criteria, we do not consider the identification to be successful. </p>
<p><strong>Next, we need:</strong>In addition to prior distribution/regularization, we publish all of the <strong>compared and excluded families</strong>, <strong>sensitivity analysis of electrode geometry, head model, and conductivity</strong>, <strong>simulation/phantom/invasive calibration</strong>, and <strong>abstention conditions when models overlap</strong>, and only adopt robust conclusions. </p>
<div class="note-box">
<strong>Separate predictability, localization, and identity</strong>
<p>
This page does not treat <strong>improved held-out prediction</strong>, <strong>reduced localization error</strong>, and <strong>internal-state recovery that approaches a unique solution</strong> as claims of equal strength. The first two are important advances, but the third requires additional conditions before it can be claimed publicly.
</p>
<ul>
<li><strong>Predictability:</strong> The ability to conditionally predict the next observation. It is useful for model compression and proxy improvement, but it does not by itself guarantee uniqueness of internal state. </li>
<li><strong>Localization:</strong> Reduced positional error of a source under specified conditions. This matters for direct validation, but other uncertainties remain in deep, low-amplitude, and unobserved regions. </li>
<li><strong>Identifiability:</strong> Conclusions remain stable even when candidate families and sensitivity analyses are included, and they can be recovered with held-out perturbations and external criteria. </li>
</ul>
</div>
<div class="note-box">
<strong>2026-03 Supplement: Correlation, prediction, and identification are not treated with the same strength</strong>
<p>
The EEG literature with direct validation is rather revealing of its limitations when read carefully. Seeber et al. (2019) showed that the subcortical signal was <strong>conditionally detectable</strong> in 256ch scalp EEG, but did not claim general unique reconstruction. Unnwongse et al. (2023) showed in direct verification using intracranial stimulation that localization error depends on the conductivity assumption and source depth, and Hao et al. (2025) reported that source power and source depth greatly influenced the error in a patient cohort of simultaneous HD-EEG/SEEG. Therefore, even if a cross-modal correlation or a held-out prediction appears, it is primarily an improvement in predictability / localization, and does not necessarily lead to a unique solution to the internal state.
</p>
</div>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r8">
<summary>
<span class="qa-id">R8</span>
<span class="qa-title">Compression: Can the “verification standard” be maintained no matter what information is discarded? </span>
<span class="qa-tags"><span class="tag">COMPRESSION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> It would be ideal to “save everything” for WBE, but that is not realistic. Can we identify the minimum representation that still satisfies the evaluation target (V0)? </p>
<p><strong>Next:</strong> Vary the compression ratio and measure where the performance of the evaluation suite breaks down</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r9">
<summary>
<span class="qa-id">R9</span>
<span class="qa-title">Audit: What is the mechanism for "keeping" model differences and failure examples? </span>
<span class="qa-tags"><span class="tag">AUDIT</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Because this is an area where the conclusion changes every time it is updated, it is necessary to record differences, failures, and negative results. </p>
<p><strong>Next:</strong> Connect model/data/evaluation versions so that they can be reproduced by re-running (P2)</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r10">
<summary>
<span class="qa-id">R10</span>
<span class="qa-title">Neuromodulation: How to incorporate mood, alertness, and volume transmission? </span>
<span class="qa-tags"><span class="tag">NEUROMODULATION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Synaptic connections alone cannot reproduce state-dependent regulation of dopamine, serotonin, acetylcholine, and related volume-transmission systems. The weak point here was that this node still let <strong>pupil / HRV</strong>, <strong>local transmitter imaging</strong>, <strong>receptor maps</strong>, and <strong>PET target-engagement or displacement results</strong> sound more interchangeable than they are. That was too weak. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> showed that pupil fluctuations track both adrenergic and cholinergic activity, <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> showed that local cortical ACh depends on axon activity and local clearance, <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> and <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">Goulas et al. (2021)</a> showed that receptor maps are structured regional priors, and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a> plus <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a> showed that raclopride PET gives challenge- and time-window-limited dopamine-release proxy rather than a free readout of the whole transmitter field. </p>
<p><strong>Operational rule:</strong>On this site, neuromodulation is not treated as a <code>single mood scalar</code>. It is a ladder with at least four non-equivalent rungs. <strong>(1) mixed arousal proxy</strong> such as pupil / HRV / locomotion is a coarse covariate only. <strong>(2) local axon or transmitter sensor</strong> calibrates a measured region's chemical signal but not the whole brain. <strong>(3) receptor / transporter atlas</strong> is a regional chemoarchitectural prior, not the current state. <strong>(4) occupancy / displacement PET</strong> is ligand-, receptor-family-, challenge-, and time-window-limited target-engagement or release proxy. None of these rungs alone is accepted here as the ground truth of the current whole-brain neuromodulatory state. </p>
<p><strong>Next:</strong>When an R10 claim is made, publish <strong>which rung was used</strong>, plus receptor family, ligand / challenge, temporal window, spatial scope, and abstention boundary. Then compare the same baseline with and without that rung under the same held-out state transition. For the stack-level ceiling, see <a href="wiki/measurement-stack-and-claim-ceiling.html#neuromodulatory-proxy-ladder">Wiki: neuromodulatory proxy ladder</a>; for the broader hidden-state argument, see <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams alone are not enough</a>. </p>
</div>
</details>
</div>

<div class="node" id="implementation" data-qa-group>
<div class="node-kicker">3. Implementation</div>
<h3>Implementation: On what basis? What about real-time performance? </h3>
<p class="mini"><strong>Central question:</strong> "Which computational platform (HPC/cloud/neuromorphic/hybrid) should we use to run the restored model? Can it be put into a closed loop (body/environment)?"</p>

<details open class="qa" data-tags="implementation" id="qa-i0">
<summary>
<span class="qa-id">I0</span>
<span class="qa-title">Execution platform: Which one are you aiming for: general-purpose computing/GPU/HPC/neuromorphic? </span>
<span class="qa-tags"><span class="tag">IMPLEMENTATION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Can the implementation platform achieve both “sufficient fidelity” and “realistic cost” for the restoration target (R0)? </p>
<p><strong>Next:</strong>Estimate the model granularity (I2) and calculation amount (I3) as a set</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i10">
<summary>
<span class="qa-id">I10</span>
<span class="qa-title">Time continuity: Discrete time (RNN) or continuous time (ODE)? </span>
<span class="qa-tags"><span class="tag">NEURAL-ODE</span><span class="tag">DYNAMICS</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Biological brains operate in continuous time, whereas standard RNNs/Transformers are discrete time. This gap creates distortion in dynamics. </p>
<p><strong>Suggestion:</strong>Adopt <strong>Neural ODEs (Neural Ordinary Differential Equations)</strong> or <strong>CTRNNs</strong> as the implementation framework. By modeling as $\frac{dh(t)}{dt} = f(h(t), t, \theta)$, sampling at arbitrary time resolution and memory-efficient learning using the adjoint method are possible. </p>
<p><strong>Next:</strong>Integrating the different time scales of EEG (milliseconds) and fMRI (seconds) in the same system of differential equations</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i1">
<summary>
<span class="qa-id">I1</span>
<span class="qa-title">Closed loop: How many ms of delay can be tolerated in real time? </span>
<span class="qa-tags"><span class="tag">REALTIME</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>If we are to evaluate “personhood”, the essence is interaction with the environment (delay/noise). Tolerable delay is task dependent. </p>
<p><strong>Redefinition (2026-03):</strong> Instead of a single number, audit acceptable delays for at least <strong>(a) state feedback / neurofeedback</strong>, <strong>(b) ERP / command BCI</strong>, <strong>(c) phase-locked stimulation</strong>, and <strong>(d) burst/state-triggered neuromodulation</strong>. Phase-targeting focuses on phase error rather than ms, and adaptive DBS focuses on biomarker burst detection delay and stopping rules. </p>
<p><strong>Supplement (Issue #46):</strong> We actually measure the <strong>end-to-end delay and jitter</strong> using CLET, photodiode, loopback, and TTL, and position LSL's time_correction as software offset correction. This is not to say that LSL alone guarantees actuation onset. </p>
<p><strong>Next:</strong> On the evaluation suite (V1) side, leave the loop class explicit, median/P95/P99/worst-case latency, phase error or burst detection delay, number of abstentions/freezes/stops, and performance degradation curve for additional delay. For information on organizing entrances, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed-loop, delay, jitter, and safety stops</a>. </p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i2">
<summary>
<span class="qa-id">I2</span>
<span class="qa-title">Model granularity: Where do we fight between spiking/rate/abstraction? </span>
<span class="qa-tags"><span class="tag">GRANULARITY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>While the fidelity increases (tentatively) as the granularity increases, identification (R7) and calculation (I3) break down. What is the granularity to win? </p>
<p><strong>Next required:</strong>Associate "required measurement (M2/M3)", "required calculation (I3)", and "passing evaluation (V0)" for each granularity</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i3">
<summary>
<span class="qa-id">I3</span>
<span class="qa-title">Computational amount: Where are the bottlenecks in memory/power/parallelization? </span>
<span class="qa-tags"><span class="tag">SCALING</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Increasing the fidelity of a model will explode computational resources. Where should approximation/compression (R8) be performed? </p>
<p><strong>Next:</strong> Measure the boundaries of how the evaluation suite can be compressed without compromising performance</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i4">
<summary>
<span class="qa-id">I4</span>
<span class="qa-title">Initialization: How to give the “initial state” of the model? </span>
<span class="qa-tags"><span class="tag">INITIALIZATION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Even if the structure is the same, the behavior will be different if the initial state is different. At what point in measurement (M7) should we “start”? </p>
<p><strong>Disproval condition: </strong>The result is unstable due to the arbitrariness of the initialization, and the identity evaluation (V5) does not hold.</p>
<p><strong>Next:</strong> Fix the initialization procedure and measure the sensitivity (robustness) to initialization</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i5">
<summary>
<span class="qa-id">I5</span>
<span class="qa-title">Learning and Drift: How to design “safe updates” for learning? </span>
<span class="qa-tags"><span class="tag">LEARNING</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> Allowing learning (R5) involves identity (V5) and safety (D2). How do I monitor updates and where do I stop them? </p>
<p><strong>Next required:</strong>Drift indicator (V4) + kill switch/isolation (I8)</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i6">
<summary>
<span class="qa-id">I6</span>
<span class="qa-title">Embodiment: How much input/output (sensors/movement/language) should we have? </span>
<span class="qa-tags"><span class="tag">EMBODIMENT</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Closed-loop verification (I1/V1) requires an environment and a body (or a substitute thereof). What is the minimum physicality? </p>
<p><strong>Next:</strong> Fix the environment (VR/game/dialogue) and design an evaluation that can be repeated under the same conditions</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i7">
<summary>
<span class="qa-id">I7</span>
<span class="qa-title">Reproducibility: Is there a guarantee that the results will not change due to implementation differences (language/hardware)? </span>
<span class="qa-tags"><span class="tag">REPRO</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Even with the “same model”, the behavior changes depending on numerical errors and parallel order. How much decisiveness do you require? </p>
<p><strong>Next:</strong> Verify that the error is within tolerance using a fixed random number, fixed environment, and differential test (P2).</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i8">
<summary>
<span class="qa-id">I8</span>
<span class="qa-title">Safety: How to create isolation, monitoring, and containment? </span>
<span class="qa-tags"><span class="tag">SAFETY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>The closer you get to the strong claims (L4-L5 of P1), the more safety becomes a technical requirement. </p>
<p><strong>Next:</strong>Include a triad of isolation environments, monitoring metrics, and outage protocols in your L3 and beyond implementation plan</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i9">
<summary>
<span class="qa-id">I9</span>
<span class="qa-title">Thermodynamics: How to audit implementation costs and irreversibility? </span>
<span class="qa-tags"><span class="tag">THERMODYNAMICS</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>To what extent should thermodynamics be included in the evaluation when comparing WBE implementations? Things you should not mix here are <strong>Landauer lower bound</strong>, <strong>organizational-level energy budget</strong>, <strong>time irreversibility of coarse-grained neural dynamics</strong>, and <strong>model-based entropy flow</strong>. The question to ask is not ``Can this prove identity?'' but rather how to audit the physical costs and nonequilibrium indicators without overstating them. </p>
<p><strong>2026-03 Literature Audit:</strong>Bérut et al. (2012) demonstrated a logically irreversible minimum dissipation lower bound for bit erasure, not wall-power or NESS reproduction conditions for the entire digital brain. What Lynn et al. (2021), de la Fuente et al. (2023), and Nartallo-Kaluarachchi et al. (2025) demonstrate is the usefulness of measuring broken detailed balance and time irreversibility from coarse-grained time series such as fMRI/ECoG/MEG, and is not an acceptance condition for microscopic physical dissipation or identity. Ishihara & Shimazaki (2025) also show that entropy flow estimation is a model-based quantity that requires assumptions such as state-space kinetic ising model, pairwise coupling, and mean-field approximation. </p>
<div class="key-points">
<h4>Treatment to be fixed on this page</h4>
<ul>
<li><strong>Do not make it a required gate:</strong>Maintaining EPR > 0, <code>Virtual Dissipation Protocol</code>, biological brain 20W matching, and communication: calculation ratio matching are not set as acceptance conditions at this time. </li>
<li><strong>Treat as supplementary logs: </strong>Wall-plug power, FLOPs, time irreversibility, and model-based entropy flow are recorded separately. </li>
<li><strong>Explicit modality dependence:</strong>Since the estimators have different meanings for fMRI / MEG / ECoG / spike train, they are not directly substituted for each other. </li>
<li><strong>Name estimator family and null control:</strong>Transition-flux lower bounds, time-shifted correlation asymmetry, inversion classifiers, visibility-graph indices, and state-space kinetic Ising entropy flow are not interchangeable, and shuffle / surrogate controls are part of the claim. </li>
<li><strong>Dividing the lower bound and the main body:</strong>The irreversibility obtained from the observation time series is often a coarse-grained lower bound, not the microscopic physical dissipation itself. </li>
</ul>
</div>
<p><strong>Next:</strong> We need an irreversibility benchmark that is reproducible within the same modality and preprocessing chain, plus a log schema that separates wall-plug power, FLOPs, and simulated metabolic overhead. At minimum, publish an <strong>irreversibility route card</strong> naming signal route, state definition, estimator family, null / surrogate control, lower-bound or model-based quantity type, and hardware power isolation. For more information, see <a href="wiki/thermodynamic-grounding-basics.html#irreversibility-route-card">Wiki: irreversibility route card</a>. </p>
</div>
</details>
</div>
</details>

<div class="node" id="verification" data-qa-group>
<div class="node-kicker">4. Verification</div>
<h3>Verification: What must be met to say that they are the same? </h3>
<p class="mini"><strong>Central question:</strong>"How do we define technically verifiable criteria among identity/consciousness/behavior, and how do we set conditions for disproving it?"</p>

<details open class="qa" data-tags="verification" id="qa-v0">
<summary>
<span class="qa-id">V0</span>
<span class="qa-title">Target of verification: Which of identity, consciousness, or behavior should be verified “engineeringly”? </span>
<span class="qa-tags"><span class="tag">VERIFICATION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> You cannot verify what cannot be measured. What should count as “measurable conditions for success”? </p>
<p><strong>Branching (example):</strong>(A) Equivalence of behaviors and abilities / (B) Equivalence of intervention responses / (C) Continuity of autobiographical memories and values (need to be careful)</p>
<p><strong>Next:</strong> Pre-register the evaluation suite in V1 and link it to the claim ladder in P1.</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v1">
<summary>
<span class="qa-id">V1</span>
<span class="qa-title">Evaluation suite: What should we measure as “progress”? (Pre-registration)</span>
<span class="qa-tags"><span class="tag">BENCHMARK</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Fix tasks, metrics, baselines, statistics, and failure conditions in advance. </p>
<ul>
<li><strong>Behavior:</strong>Generalization in unlearned tasks, reaction times/errors, learning curves</li>
<li><strong>Neuro:</strong>State transitions, spectral features, network metrics, intervention responses</li>
<li><strong>Temporary identity:</strong>Coherence of autobiographical memory, stability of preferences, consistency of self-model</li>
</ul>
<p><strong>Next:</strong> First, create a “small but retestable” suite for L0-L2.</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v2">
<summary>
<span class="qa-id">V2</span>
<span class="qa-title">Causal testing: Can stimuli/interventions produce the “same response”? </span>
<span class="qa-tags"><span class="tag">CAUSAL</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Correlation matching can be achieved simply by “simulating” things. A strong verification will be whether there is agreement with the intervention. </p>
<p><strong>Strength of evidence is treated in four stages:</strong>This roadmap does not reduce causal testing to a single type of pass/fail. The primary literature now supports staged evidence of varying strength. </p>
<ul>
<li><strong>Gate 1 / held-out perturbation prediction:</strong>The ability to offline predict responses when changing task conditions, stimulus timing, and environmental changes. </li>
<li><strong>Gate 2 / online human-in-the-loop:</strong> A loop that includes real-time input and feedback while maintaining performance and auditing latency / jitter. </li>
<li><strong>Gate 3 / local causal intervention:</strong> Interventions such as TMS-EEG, intracranial stimulation, and adaptive DBS in which stimulation site, intensity, artifact handling, and safety-stop conditions are disclosed. </li>
<li><strong>Gate 4 / long-run closed loop:</strong>The ability to track recalibration loads, recovery times, and even failure modes over multiple sessions and long-term operations. </li>
</ul>
<p><strong>Required logs:</strong> Stimulation site, intensity, masking, artifact window, synchronization path, median end-to-end latency / P95 / P99, jitter, dropout, and recovery time. If these depart from the TMS-EEG recommendations summarized by Hernandez-Pavon et al. (2023), the result is not treated here as a comparable causal test. </p>
<p><strong>Decision rule:</strong>The success of Gate 1 alone does not assert L3 or "counterfactual equivalence." In order to advance to a stronger claim, it is necessary to submit a bundle of evaluation items, external validation, and abstention conditions that connect M6 (intervention design) and R4 (causal model). For detailed operational verification, see <a href="verification.html#causal-perturbation-suite">Verification Causal Perturbation Suite</a>. </p>
<p><strong>Next:</strong> Create evaluation items that connect M6 (intervention design) and R4 (causal model), and reduce at least Gate 1 / Gate 2 to specifications that can be re-executed by a third party. </p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v3">
<summary>
<span class="qa-id">V3</span>
<span class="qa-title">Generalization: Can you maintain your “identity” even in out-of-distribution (OOD)? </span>
<span class="qa-tags"><span class="tag">OOD</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>If it only works under the same conditions as training, it is more like "playback" than uploading. Measuring consistency in novel situations. </p>
<p><strong>Next:</strong>Define the performance degradation curve under untrained tasks, environmental changes, and noise conditions</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v4">
<summary>
<span class="qa-id">V4</span>
<span class="qa-title">Long-term: How to evaluate learning, drift, and forgetting? </span>
<span class="qa-tags"><span class="tag">LONGITUDINAL</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>The more you learn, the more likely you are to deviate from the original person. Define the range in which change is “acceptable”. </p>
<p><strong>Required next:</strong>Session identity index (M7) + update log (P2)</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v5">
<summary>
<span class="qa-id">V5</span>
<span class="qa-title">Identity: What is “causal identity” that goes beyond psychological continuity? </span>
<span class="qa-tags"><span class="tag">IDENTITY</span><span class="tag">LEGAL</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> Similarities in memory and personality alone, that is, psychological continuity, are not enough to distinguish identity from copying or imitation by an LLM-like system. A more rigorous engineering definition is needed. </p>
<ul>
<li><strong>New standard: Causal Identity:</strong>
Extending Parfit's psychological theory, the condition for identity is that the system's ``future predictive ability (accuracy of active inference)'' is statistically indistinguishable from that of the biological brain.
</li>
<li><strong>Indicator:</strong>Execute the<strong>Causal Perturbation Protocol</strong>, which is an extension of the Turing Test. We will introduce an index (e.g. Perturbational Complexity Index, PCI) to verify the statistical identity of the biological brain's response to physical perturbations such as TMS and the response to virtual perturbations in emulation, and confirm the correspondence of dynamic causal structures. </li>
<li><strong>Conditions for disproving:</strong>They have memory, but their adaptation/prediction patterns to new environments deviate from the original (zombie/imitator)</li>
<li><strong>Next:</strong> Make predictive accuracy a core metric in V8's "imitation-versus-imitation" testing.</li>
</ul>                        </div>
</details>

<details open class="qa" data-tags="verification" id="qa-v6">
<summary>
<span class="qa-id">V6</span>
<span class="qa-title">Consciousness: To what extent can theory-dependent predictions be made “testable”? </span>
<span class="qa-tags"><span class="tag">CONSCIOUSNESS</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Consciousness cannot be directly observed. Therefore, the question is whether the prediction differences produced by theories (IIT / GNWT / FEP, etc.) can be benchmarked while minimizing the task/report confound. </p>
<ul>
<li><strong>Theories are not accepted on a winner-take-all basis:</strong> Ferrante et al. (2025) demonstrated the need for preregistered prediction competition rather than the victory of a single theory. Therefore, on this site, IIT / GNWT / FEP will compete as a <strong>prediction family</strong>, and the theory name itself will not be used as a pass/fail indicator. </li>
<li><strong>PCI / PCI-ST is a perturbation benchmark:</strong> Casali et al. (2013) and Comolatti et al. (2019) gave a strong benchmark candidate, but not a universal meter. We treat it as an auxiliary measure of L2/L3 only if we disclose the stimulation site, intensity, masking, artifact window, and cohort calibration. </li>
<li><strong>Spontaneous complexity / criticality is a calibration track:</strong> Maschke et al. (2024) showed an association between spontaneous criticality and PCI, while Casarotto et al. (2024) showed a dissociation between spontaneous features and PCI in a minimally conscious state. Therefore, the resting-state marker is not a PCI replacement, but rather a proxy that requires external calibration. </li>
<li><strong>No-report / criterion placement is fixed first:</strong> As Cohen et al. (2024) and Fahrenfort et al. (2025) show, if we do not control for post-perceptual processing and criterion placement, there remains a possibility that we are looking at task/report confound rather than theoretical differences. </li>
</ul>
<p><strong>Note:</strong>Theory is treated only as a tool for hypothesis generation, and the success or failure of implementation (WBE) is determined not by "conformity to a specific theory" but by the bundle of V2 (causality), V3 (OOD), and V4 (long-term stability). Even when using geometry or topology, the main pass/fail points are placed in perturbation and generalization. </p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v7">
<summary>
<span class="qa-id">V7</span>
<span class="qa-title">Copy/branch: How do you handle the “principal” when multiple instances run? </span>
<span class="qa-tags"><span class="tag">BRANCHING</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Easy to reproduce from an engineering standpoint. Verification design will also fail if branching is not assumed. </p>
<p><strong>Next:</strong> Connect individual ID/version management (P2) with identity evaluation (V5)</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v8">
<summary>
<span class="qa-id">V8</span>
<span class="qa-title">LLM/Distinguishing from imitation: How do you judge whether the external appearance is similar but the content is different? </span>
<span class="qa-tags"><span class="tag">DISAMBIGUATION</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Conversations and reports are easy to imitate, and the stronger the prior distribution of the language model, the more likely it is. Therefore, what we want to distinguish here is not the abstract "AI-likeness" but the extent to which neural signals exceed language prior and the modality, task, and time scale in which they are established. </p>

<table class="data-table">
<thead>
<tr>
<th>Track</th>
<th>Relatively strong statements as of 2026-03</th>
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Non-invasive semantic / caption decoding</strong></td>
<td>Tang and Horikawa used fMRI to advance semantic reconstruction of continuous language and generation of descriptions of video content. The goal here is to<strong>transfer part of the semantic expression</strong>to an external sentence. </td>
<td>Since dependence on subject cooperation, task conditions, and caption candidate space remains, this alone cannot be said to be a reproduction of self-model or WBE. </td>
</tr>
<tr>
<td><strong>Non-invasive word / speech decoding</strong></td>
<td>Défossez et al. and d'Ascoli et al. have advanced speech/word decoding from MEG/EEG, showing that MEG and reading tasks are advantageous and data volume strongly dominates performance. </td>
<td>Open-ended thought reading and strong cross-day/cross-task generalizations are another matter. It is impossible to make a strong argument while hiding candidate set and device dependencies. </td>
</tr>
<tr>
<td><strong>Invasive streaming speech neuroprosthesis</strong></td>
<td>Willett, Littlejohn, and Wairagkar made significant advances in speech BCI as a local communication subsystem. Large vocabulary, fast decode, 80 ms updates, and closed-loop own-voice synthesis are important achievements. </td>
<td>What is shown here is local progress in communication routes, not whole-brain emulation or identity preservation. Furthermore, as shown by Wilson et al., long-term drift and recalibration burden remain another barrier. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Minimum evaluation pack</strong>
<ul>
<li><strong>Isolation of neural contribution:</strong> Report <code>no brain</code>, <code>time-shuffle</code>, <code>trial-shuffle</code>, <code>LM-only</code>, and <code>no-LM</code>; if decoding is search-based, also publish candidate-set size. </li>
<li><strong>Bounds of generalization: </strong>Report held-out stories, held-out vocabulary, cross-day, cross-task, and cross-subject separately and do not hide the need for subject cooperation or individual adaptation. </li>
<li><strong>Streaming metrics:</strong> Report not only words per minute but also <code>P50/P95/P99 latency</code>, silence / abstention, dropout, recalibration burden, and recovery time. </li>
<li><strong>Do not over-promote:</strong> Do not elevate decoding success, embedding similarity, or conversational naturalness into claims about emulation, WBE, or identity preservation. </li>
</ul>
</div>

<p><strong>Next:</strong> Connect an evaluation pack that bundles <code>LM-only / shuffle / OOD / cross-day / latency / abstention / recalibration</code> to V2 (intervention), I1 (closed loop), and R4 (causal modeling) so that progress on the communication route is not conflated with claims about WBE. </p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v9">
<summary>
<span class="qa-id">V9</span>
<span class="qa-title">Supplementary exam: Is the design designed to allow a third party to reach the “same conclusion”? </span>
<span class="qa-tags"><span class="tag">REPRO</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong> The shortest path to research is to create a situation in which other people can repeat the test. The more identity is debated, the more important repeatability becomes. </p>
<p><strong>Next:</strong>Make data/code/evaluation publicly available to the extent that P2 (deliverables) is met</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v10">
<summary>
<span class="qa-id">V10</span>
<span class="qa-title">Model distance: How do we measure the "closeness" between the biological brain and emulation? </span>
<span class="qa-tags"><span class="tag">METRIC</span><span class="tag">MATH</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Simple Euclidean distance in parameter space often does not reflect differences in the functional behavior of models. How do we quantify the more essential "closeness of behavior"? </p>
<p><strong>Policy:</strong> Do not adopt a single mathematical distance as the standard solution. At present, stronger external criteria come from observable behavior such as held-out perturbation responses, OOD degradation curves, calibration errors, and recovery times. Distances such as Fisher-Rao, representation distance, and manifold separation are compared as candidates, but none of them is the default pass / fail indicator. </p>
<p><strong>Next:</strong> Compare on the same benchmark how well candidate distances match the external standards in V2 / V3 / V4. Sensitivity analysis should reveal whether the ranking stays stable when preprocessing, sample count, and state differences are changed. </p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v11">
<summary>
<span class="qa-id">V11</span>
<span class="qa-title">Topology: Is the “structure” of consciousness conserved? </span>
<span class="qa-tags"><span class="tag">TDA</span><span class="tag">GEOMETRY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Scalar values such as PCI (complexity) alone do not tell us whether the "qualitative structure" of consciousness is the same. </p>
<p><strong>Policy:</strong>Topological data analysis (TDA) or manifold geometry is a promising track for<strong>ancillary</strong>describing structural differences falling in scalar indicators. Yoon et al. (2024) provided a mathematical basis for comparing topologies in cross-populations, but the iScience 2024 mouse V1 circular manifold study also showed that there are sampling obstacles to retrieving truthful topologies. Therefore, topology distance cannot be directly linked to guaranteeing consciousness structure or passing or failing WBE. </p>
<p><strong>Next:</strong> Through sampling, embedding dimension, distance function, preprocessing, session drift, and sensitivity analysis with perturbation responsiveness, only phase features that remain stable are reported as auxiliary indicators. </p>
</div>
</details>
</div>

<div class="node" id="deployment" data-qa-group>
<div class="node-kicker">5. Deployment & Governance</div>
<h3>Social implementation: What is needed beyond technology? </h3>
<p class="mini"><strong>Central question:</strong>"What kind of systems, ethics, and legal foundations other than technology are needed for L5 (social implementation)?"</p>

<details open class="qa" data-tags="deployment" id="qa-d0">
<summary>
<span class="qa-id">D0</span>
<span class="qa-title">Ethical Framework: What are the rights of emulated beings? </span>
<span class="qa-tags"><span class="tag">ETHICS</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>If WBE is successful, is emulation a rights subject? Is stopping “death”? Is reproduction “birth”? </p>
<p><strong>Current status:</strong>A framework for protecting neural data is being developed through the EU AI Act, the US MIND Act (proposed in 2025), etc., but it does not address the issues specific to WBE (duplication, suspension, modification). </p>
<p><strong>Next:</strong> Develop design guidelines for the ethics review committee in parallel with technical verification (L0-L2)</p>
</div>
</details>

<details open class="qa" data-tags="deployment" id="qa-d1">
<summary>
<span class="qa-id">D1</span>
<span class="qa-title">Consent and withdrawal: How do we design informed consent? </span>
<span class="qa-tags"><span class="tag">CONSENT</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>Consent to the WBE process is given in advance, but how can we guarantee the right to withdraw during and after the process? </p>
<p><strong>Next:</strong> Design a staged consent model (re-consent at each phase) and engineering implementation of termination rights</p>
</div>
</details>

<details open class="qa" data-tags="deployment" id="qa-d2">
<summary>
<span class="qa-id">D2</span>
<span class="qa-title">Access and equity: Who should have access to WBE? </span>
<span class="qa-tags"><span class="tag">EQUITY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>If WBE becomes a reality, how will we deal with the disparity problem where only the wealthy have access to "immortality"? </p>
<p><strong>Next need:</strong>Position open access design of verification commons as the first step to prevent disparities</p>
</div>
</details>

<details open class="qa" data-tags="deployment" id="qa-d3">
<summary>
<span class="qa-id">D3</span>
<span class="qa-title">Security: How to design for exploitation risks and controls? </span>
<span class="qa-tags"><span class="tag">SECURITY</span></span>
</summary>
<div class="qa-body">
<p><strong>Question:</strong>How to deal with the risks of emulation modification, forced mental manipulation, military use, etc.? </p>
<p><strong>Next:</strong> In conjunction with the I8 (containment) design, design technical guarantees for access control, modification auditing, and termination rights.</p>
</div>
</details>
</div>
</div>

</section>

<section class="section" id="unsolved">
<h2 class="section-title">Definition catalog of open problems (strict version)</h2>
<p>
Here, we don't use "unresolved" as an ambiguous term; we define <strong>what is input, what is output, and under what conditions it passes/fails</strong>. Even if there is a wealth of prior research, if the criteria for judgment are ambiguous, the research will not accumulate. On the other hand, if the definition is strict, small advances can be reliably accumulated.
</p>

<table class="data-table">
<thead>
<tr>
<th>ID</th>
<th>Definition of unsolved problems (rigorization)</th>
<th>Existing points</th>
<th>Unresolved boundary (next point to close)</th>
</tr>
</thead>
<tbody>
<tr>
<td>U0</td>
<td><strong>Operational identity</strong>: For intervention set I and time window T, can it be defined as "identical" if the conditional distribution difference between the biological system and the model system is less than a threshold? </td>
<td>There is a framework definition in V0/V5. Introduced the distinction between psychological continuity and causal identity. </td>
<td>The minimum completeness conditions, threshold settings, and pre-registration rules for intervention set I have not been determined. </td>
</tr>
<tr>
<td>U1</td>
<td><strong>Identifiability of the inverse problem</strong>: When estimating the potential source x from the observation y, is it possible to quantify "closeness to the unique solution" by the degree of concentration of the posterior distribution? </td>
<td>The policy for estimation with uncertainty has been clearly stated in R2. However, public implementation and external validation are incomplete. </td>
<td>Overall identification possibility including forward model error (conductivity/shape) has not been verified. </td>
</tr>
<tr>
<td>U2</td>
<td><strong>Lower limit of spatiotemporal resolution</strong>: Is it possible to define the minimum temporal/spatial resolution for each task without destroying cognition, learning, and intervention responses? </td>
<td>The points of discussion have been sorted out in M2/M3. </td>
<td>Insufficient measured boundaries (delay tolerance/granularity collapse point) in closed-loop tasks. </td>
</tr>
<tr>
<td>U3</td>
<td><strong>Subject Boundary</strong>: Can the minimum set of physiological, neurological, and environmental elements included in the subject be fixed with a verifiable operational definition? </td>
<td>Hybrid measurement protocol has been developed in Issue #12. </td>
<td>Sensitivity analysis of how much the V5 judgment changes when the boundary changes has not been completed. </td>
</tr>
<tr>
<td>U4</td>
<td><strong>Counterfactual Equivalence</strong>: Can equivalence be determined based on predicted matching of intervening branches rather than observed matching? </td>
<td>Theoretical policy was clarified in R4/V2/V6. </td>
<td>Insufficient implementation of counterfactual virtual generator, false intervention baseline, and stopping rules. </td>
</tr>
<tr>
<td>U5</td>
<td><strong>Learning rules and personality drift</strong>: If learning updates are allowed, to what extent is the expression change considered to be the same? </td>
<td>The problem has been raised in R5/V4. </td>
<td>The allowable drift threshold and kill switch conditions for each update rule are undefined. </td>
</tr>
<tr>
<td>U6</td>
<td><strong>Separation of personalization and generalization</strong>: Is it possible to identify individual-specific parameters and task-common parameters and avoid overfitting? </td>
<td>Present evaluation policy in R6. </td>
<td>There is a lack of standard benches and test plans for intra-individual/inter-individual decomposition. </td>
</tr>
<tr>
<td>U7</td>
<td><strong>Multimodal alignment</strong>: When integrating EEG/fMRI/behavior/physiology, can coordinates, delays, and noise differences be kept auditable? </td>
<td>Required in M5/M9, Motion-BIDS policy (Issue #46). </td>
<td>Concordance rate evaluation of multiple integrated pipelines using the same data is not yet developed. </td>
</tr>
<tr>
<td>U8</td>
<td><strong>Closed-loop stability</strong>: Can the model be controlled without breaking down under delays, noise, and environmental changes? </td>
<td>Organize requirements using I1/I6. </td>
<td>Identification of safe operation area based on actual measurements of delay and jitter is insufficient. </td>
</tr>
<tr>
<td>U9</td>
<td><strong>OOD robustness</strong>: Can the sameness index be maintained in unlearning environments, novel tasks, and noise conditions? </td>
<td>Clarified the problem in V3. </td>
<td>Standardization of the deterioration curve (at what speed it collapses) has not been established. </td>
</tr>
<tr>
<td>U10</td>
<td><strong>Thermodynamic consistency</strong>: Is it possible to formulate implementation conditions under which information processing satisfies physical irreversibility and dissipation constraints? </td>
<td>Theoretical organization has progressed with I9 and Issue #58/#61/#62. </td>
<td>The unification of measurable experimental indicators (dissipation rate, causal density, efficiency) has not yet been completed. </td>
</tr>
<tr>
<td>U11</td>
<td><strong>Calibration of perturbation/spontaneous/geometry proxies</strong>: Under what conditions do the PCI/PCI-ST, spontaneous complexity, criticality, and manifold/topology indicators match and under what conditions do they dissociate? </td>
<td>Defined the role difference between benchmark hierarchy and auxiliary analysis in V6 / V11. </td>
<td>Lack of external calibration across multicohort, no-report, and perturbation conditions. </td>
</tr>
<tr>
<td>U12</td>
<td><strong>Branch identity (multiple instances)</strong>: How to handle individual ID, responsibility, and evaluation attribution after multiple branches. </td>
<td>The necessity of version control was clearly demonstrated in V7. </td>
<td>A system design with a fixed branching point and evaluation period has not been started yet. </td>
</tr>
<tr>
<td>U13</td>
<td><strong>Imitation separation test</strong>: Can behavioral imitation (LLM type) and causal structure preservation be experimentally distinguished? </td>
<td>3-axis benchmark in Issue #10, integration policy in V8. </td>
<td>There is a lack of test groups that simultaneously impose intervention, closed loop, and internal state consistency. </td>
</tr>
<tr>
<td>U14</td>
<td><strong>Implementation of retestability</strong>: Is it possible to fix the operation so that a third party can reach the same conclusion using the same data and procedures? </td>
<td>Requirements have been sorted out in P2/V9. </td>
<td>The operational flow for publishing the execution environment, differential logs, and failure examples is incomplete. </td>
</tr>
<tr>
<td>U15</td>
<td><strong>Social implementation governance</strong>: Can rights, consent, and responsibility distribution be designed in synchronization with technical evaluation? </td>
<td>Issues have been extracted from D0-D2. </td>
<td>The linkage rules (including cancellation criteria) between technical KPI and system KPI are undefined. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Judgment rules</strong>
<p>
U0-U15 above are not "good ideas" but "falsifiable research questions". Each problem is determined to have been ``solved'' only when the <strong>inputs, outputs, evaluation indicators, and failure conditions</strong> are all complete.
</p>
</div>

<h3>Additional breakdown of the three most important issues (deeper)</h3>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>U4 causal equivalence</h4>
<ul>
<li>How to create a minimally complete set of intervention dictionaries (stimulus, task, pharmacology). </li>
<li>How to calibrate the thresholds of counterfactual matching (KL, JS, FIM, etc.). </li>
<li>How to suppress overestimation in sham intervention/sham conditions. </li>
<li>How to pre-register the Stop Rule in case of failure. </li>
</ul>
</div>
</div>
<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>U10 Thermodynamic consistency</h4>
<ul>
<li>In what time window should we measure the dissipation rate of information processing? </li>
<li>How to deal with the difference between physical irreversibility and computational irreversibility. </li>
<li>Is it possible to create a common index that can be compared even if the implementation platform changes? </li>
<li>How to optimize the trade-off between energy efficiency and causal performance. </li>
</ul>
</div>
</div>
<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>U12 Branched identity</h4>
<ul>
<li>Where to place the branch point definition (fixed initial condition). </li>
<li>How to set the evaluation attribution period after branching. </li>
<li>How to manage responsibility distribution and audit ID when there are multiple branches. </li>
<li>How to deal with the mismatch between legal subjectivity and technical identity. </li>
</ul>
</div>
</div>
</div>
</section>

<section class="section" id="priorwork-map">
<h2 class="section-title">Previous research map (by priority area)</h2>
<p>
Prior research necessary to solve unresolved problems is organized by field. The purpose is not to ``list the literature,'' but to clarify<strong>which evidence works for which problem</strong>.
</p>

<table class="data-table">
<thead>
<tr>
<th>area</th>
<th>Representative previous research (excerpt)</th>
<th>Contribution to U0-U15</th>
</tr>
</thead>
<tbody>
<tr>
<td>WBE basics/personality</td>
<td>Sandberg &amp; Bostrom (2008), Yamakawa et al. (2024), Parfit (1984), Clowes (2021), Weber (2025)</td>
<td>U0, U12, U15</td>
</tr>
<tr>
<td>Consciousness theory and verification</td>
<td>Tononi (2015), Tononi et al. (2016), Albantakis et al. (2023), Doerig et al. (2019), Ferrante et al. (2025), Casali et al. (2013), Comolatti et al. (2019)</td>
<td>U0, U4, U11</td>
</tr>
<tr>
<td>EEG/MEG inverse problem</td>
<td>Michel &amp; Brunet (2019), Wipf &amp; Nagarajan (2009), Cai et al. (2021), Sechet et al. (2025), Vorwerk et al. (2014), Medani et al. (2025)</td>
<td>U1, U2, U7</td>
</tr>
<tr>
<td>Preprocessing/synchronization/connectivity</td>
<td>Wilson et al. (2010), Thompson et al. (2013), Mowla et al. (2017), Belinskaia et al. (2020), Mansouri et al. (2018), Zrenner et al. (2018), Appelhoff &amp; Stenner (2021), Kothe et al. (2025)</td>
<td>U1, U7, U8, U14</td>
</tr>
<tr>
<td>Decoding</td>
<td>Huth et al. (2016), Tang et al. (2023), D&eacute;fossez et al. (2023), Horikawa (2025), d'Ascoli et al. (2025), Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025), Wilson et al. (2025)</td>
<td>U4, U8, U9, U13</td>
</tr>
<tr>
<td>Causal/active reasoning</td>
<td>Friston et al. (2003), Friston (2010), Friston (2017), Parr &amp; Friston (2019), Laukkonen et al. (2025), Correa et al. (2021)</td>
<td>U4, U5, U9</td>
</tr>
<tr>
<td>Biological constraints</td>
<td>Cook et al. (2019), Scheffer et al. (2020), Kasthuri et al. (2015), Santello et al. (2019), Ozcete et al. (2024), Gamlin et al. (2025)</td>
<td>U2, U3, U6, U7</td>
</tr>
<tr>
<td>Measurement extension (OPM etc.)</td>
<td>Boto et al. (2018), Logothetis (2008), Purdon et al. (2013)</td>
<td>U2, U7, U8</td>
</tr>
<tr>
<td>Standardization/Reproducibility</td>
<td>Gorgolewski et al. (2016), Pernet et al. (2019), EEG-BIDS update, Open benchmark practices</td>
<td>U14</td>
</tr>
<tr>
<td>Ethics, rights, legal system</td>
<td>Yuste et al. (2017), Ienca &amp; Andorno (2017), MIND Act discourse (2025)</td>
<td>U12, U15</td>
</tr>
<tr>
<td>Thermodynamics/computability</td>
<td>Seifert (2012), Kitazono et al. (2018), complexity reduction studies on IIT (2025)</td>
<td>U10, U11</td>
</tr>
</tbody>
</table>

<div class="key-points">
<h4>Reading order (for practical use)</h4>
<ul>
<li><strong>First layer:</strong> Solidify U1/U14 (measurement and reproducibility) first. If this is weak, all higher-level discussions will be unstable. </li>
<li><strong>Second layer:</strong> Verify U4/U9 (causal and generalization) on an intervention basis and establish the difference from imitation. </li>
<li><strong>Third layer:</strong> Update U10/U11/U12/U15 (physics, identity, system) by connecting it with the empirical results. </li>
</ul>
</div>
</section>

<section class="section" id="template">
<h2 class="section-title">Template for scientific core question page (recommended)</h2>
<p>When creating a new technical proposal or question page, we recommend copying and using the Markdown template below. It is configured to force a thought flow that fixes R0 (restoration target) and V0 (verification criteria) first. </p>

<details>
<summary><strong>View template (click to expand)</strong></summary>
<pre style="background: #f6f8fa; padding: 16px; border-radius: 6px; white-space: pre-wrap; font-size: 0.85em; overflow-x: auto;">
## Template for scientific core question page (all items included/can be copied and pasted as is)

> Purpose: **"Fix R0 (recovery target) and V0 (verification criteria) first, then discuss M0 (measurement) and I0 (identifiability)" **This is a template that enforces the order.
> *Each section is clearly marked as “unconfirmed if it is unconfirmed” so that you can proceed.

---

# 0. Title

* **Page title**:
* **One-sentence summary (conclusion first)**:

  * "This page identifies the necessary measurement requirements (spatiotemporal resolution, observed variables) in order to be able to restore _____ to the standard of _____."

---

# 1. Central Question (CQ)

* **Central question**:

  * “At what spatio-temporal resolution should _____ be acquired to bring the “object to be restored (R0)” closer to being unique?”
* **Focus of question** (which is the main battlefield):

  * [ ] Selection of observed variables (what to measure)
  * [ ] Lower limit of resolution/coverage (how fine/wide)
  * [ ] Tolerable range for noise, missing measurements, and individual differences
  * [ ] Identification including causality (possibility of intervention)

---

# 2. Fixed terminology/scope (disambiguation elimination)

* **Target species**: Human/Animal (species: ＿＿＿)/Simulation
* **Status range**: At rest/on task (task: _____)/sleep/pharmacological intervention
* **Time scale**: milliseconds to seconds/minutes to hours/days to years
* **Spatial scale**: cell/column/region/whole brain
* **Meaning of “restoration”** (by definition, not intuition): ＿＿＿＿

---

# 3. R0: Restore target (most important/determined first)

## 3.1 What to restore (definition of target)

* **Restore target R0**:

  *Example) Structure (wire connections) / dynamics (state transitions) / functions (input → output) / memory / strategies / self-models including subjective reports, etc.
* **R0 output format** (What should be output in the end to be considered “restored”):

  * Examples) Parameter sets, generative models, state space models, agent policies, simulators, etc.

## 3.2 Definition of identity (equivalence relation) = “success”

* **Equivalence relation (success if what is the same)**:

  * “If ＿＿＿＿ matches, R0 is considered the same.”
* **Tolerance** (No matter how different they are, they are treated the same):

  * Indicator: ＿＿＿＿, Threshold: ＿＿＿＿

## 3.3 Assumptions (assumptions implicitly included in R0)

*Example) The brain is Markovian/observable latent states exist/can be expressed as a learnable function class, etc.
* **List of assumptions**:

  * A1：＿＿＿＿
  * A2：＿＿＿＿
  * A3：＿＿＿＿

---

# 4. V0: Verification criteria (pass/fail test)

## 4.1 What constitutes “recovery” (test design)

* **Verification task**: ＿＿＿＿
* **Evaluation data**: Within-individual/inter-individual generalization/conditional extrapolation (counterfactual)
* **Baseline**: ＿＿＿＿ (e.g. simple model, existing method)

## 4.2 Indicators (quantitative) and passing lines (thresholds)

* **Main indicators**: ＿＿＿＿ (e.g. prediction accuracy, likelihood, causal effect agreement, behavioral distribution distance)
* **Passing line**: ＿＿＿＿ (threshold or ratio)
* **Reproducibility requirements**: n = ＿＿＿, recall rate ＿＿＿, presence or absence of pre-registration ＿＿＿

## 4.3 When using intervention/causation (recommended: include if possible)

* **Intervention measures**: stimulation/pharmacology/injury/closed-loop control
* **Concordance condition at the time of intervention**: ＿＿＿＿ (definition of “response matches”)

---

# 5. M0: Measurement premise (MEASUREMENT)

## 5.1 Assumptions of measurement route (which one to assume)

* **Assumption**:

  * [ ] in vivo (non-invasive)
  * [ ] in vivo (invasive)
  * [ ] Destructive scan (ex vivo / future vision)
* **Safety/Ethics/Scale constraints**: ＿＿＿＿

## 5.2 Observation target (what to measure) candidate list

* Electricity: EEG/MEG/ECoG/single/multipoint
*Blood flow: fMRI/fNIRS
*Optics: Ca imaging, etc.
* Structure: MRI/DTI/EM etc.
* **Observables mainly treated on this page**: ＿＿＿＿

## 5.3 Expected spatiotemporal resolution/coverage

* **Temporal resolution**: ＿＿＿＿
* **Spatial resolution**: ＿＿＿＿
* **Coverage**: local/wide area/whole brain
* **Sampling constraints (duration/number of times)**: ＿＿＿＿
* **Noise floor/missing**: ＿＿＿＿

---

# 6. P0: Estimated model/representation (specify model assumptions)

* **Latent representation to be estimated**: state space/factor model/generative model/agent policy/connectome, etc.
* **Learning paradigm**: Supervised/Self-supervised/Data assimilation/Simulator combination
* **Required induction bias**: _____ (e.g. low dimensionality, sparsity, symmetry, anatomical constraints)
* **Computational resources/implementation constraints**: ＿＿＿＿

---

# 7. I0: Identifiability (the “core” of this page)

## 7.1 Claim (in 1-2 sentences)

* **I0 claim**:

  * "In order to bring R0 close to uniqueness, it is necessary to obtain the observable quantity ____ in time and space ____ (at least ____ is the lower limit)."

## 7.2 Required conditions (lower limit: impossible without this)

* **Requirements (minimum set of observations)**: ＿＿＿＿
* **Intuition/Reason**: Unobserved degrees of freedom remain/becomes a many-to-one mapping/become indivisible due to noise, etc.
* **Specific example of “unidentifiable”**: ＿＿＿＿ (Another solution that produces the same observation can be constructed, etc.)

## 7.3 Sufficient condition (upper limit: theoretically possible if this is achieved)

* **Sufficient condition**: ＿＿＿＿
* **Reality**: Impossible now/Possible in the future/Alternatives

## 7.4 Failure modes (important: enumerated proactively)

* [ ] Many-to-one (different R0 yields the same observation)
* [ ] Model misspec (P0 is wrong)
* [ ] Cause and effect cannot be determined due to lack of intervention
* [ ] Generalization breaks down due to individual differences
* [ ] Unidentifiable due to noise floor/missing measurements
* **Detection method**: ＿＿＿＿ (Which indicator should be used to determine “failure”)

## 7.5 Measure of “approaching uniqueness”

* **Uniqueness score** (candidate): concentration of posterior distribution/equivalence class size/discrimination distance, etc.
* **Measures to be adopted**: ＿＿＿＿

---

# 8. Strategic branching (A/B/C) *Can be used as an example

> For each branch, be sure to write a set of not only the "difference in M0" but also the **route to reach V0** and **probability of satisfying I0**.

## A: Train the model non-invasively (EEG/MEG/fMRI, etc.)

* **Aim**: ＿＿＿＿ (Example: Gain generalization with large-scale, long-term data)
* **M0**: ＿＿＿＿ (resolution/coverage/constraints)
* **P0**: ＿＿＿＿ (expression/learning)
* **Route to reach V0**: ＿＿＿＿ (which test to pass)
* **Bottleneck on I0**: ＿＿＿＿ (What tends to make it impossible to identify)
* **“Judgment information” obtained from this branch**: ＿＿＿＿ (information that is effective in selecting the next branch)

## B: Invasion (ECoG/deep/animal) enhances causal inference

* **Aim**: ＿＿＿＿ (Example: Strengthen causality/identification through intervention)
* **M0**：＿＿＿＿
* **P0**：＿＿＿＿
* **Route to reach V0**: ＿＿＿＿
* **Improvements on I0**: ＿＿＿＿ (crushing many-to-one with intervention, etc.)
* **Handling of extrapolation (human generalization)**: ＿＿＿＿

## C: Obtain structure with destructive and ultra-high resolution (future vision)

* **Aim**: ＿＿＿＿ (Example: Consider upper limit on sufficient condition side)
* **M0**: ＿＿＿＿ (obtainable structure information)
* **P0**: ＿＿＿＿ (structure → function mapping assumption)
* **Route to reach V0**: ＿＿＿＿
* **I0's conclusion**: ＿＿＿＿ (Is it sufficient in principle/still insufficient?)

---

# 9. Rebuttal conditions/Stop rule

## 9.1 Total falsification (condition denying the root of the page)

* **Rebuttal conditions**:

  * “Even if only the measurement is advanced without defining R0 (recovery target), the inability to identify will not be resolved.”
  * Specifically: ＿＿＿＿ (the same observation can form another R0, it does not pass through V0, etc.)

## 9.2 Stopping rules by branch (withdrawal line)

* Stop of A: ＿＿＿＿
* Stop B: ＿＿＿＿
* Stop C: ＿＿＿＿
* **Pivot condition**: ＿＿＿＿ (judgment criteria for A → B, B → C, etc.)

---

# 10. Next action (fix priority on this page)

* **Confirm first**:

  1. R0 (restore target/equivalence relationship)
  2. V0 (pass/fail test)
  3. I0 (lower limit assertion of necessary conditions)
* **Things to do this week**: ＿＿＿＿
* **Next section to add**: ＿＿＿＿
* **Undecided points (list of questions)**:

  * Q1：＿＿＿＿
  * Q2：＿＿＿＿

---

## Appendix: “Summary of main points” frame for overview on one page (optional)

* **R0**：＿＿＿＿
* **V0**：＿＿＿＿
* **M0**：＿＿＿＿
* **P0**：＿＿＿＿
* **I0 Conclusion (lower limit/upper limit)**: ＿＿＿＿
* **Branch to adopt**: A/B/C (Reason: ＿＿＿＿)
* **Disproval/Suspension**: ＿＿＿＿

---
</pre>
</details>
</section>

<section class="section" id="learning">
<h2 class="section-title">Learning order (minimum overall picture)</h2>
<p>“Order” is important. Even if you are strong in measurement, you will not be able to claim progress if your verification standards are ambiguous. On the other hand, even if the verification is excellent, if the restoration target cannot be defined, the implementation will go astray. </p>
<ol>
<li><strong>Overall picture:</strong>WBE roadmap (overall process/bottleneck)</li>
<li><strong>Measurement:</strong>What is lost at what resolution (EEG/fMRI/invasive/connectome)</li>
<li><strong>Reconstruction: </strong>Inverse problem → state estimation → generative model → intervention prediction, and proceed to “falsifiable reconstruction”</li>
<li><strong>Implementation:</strong>Fix model granularity and enable auditing of impact of execution base differences</li>
<li><strong>Verification:</strong>Write the evaluation suite and counter-conditions first, and keep the update history</li>
</ol>
</section>



<section class="section" id="sources">
<h2 class="section-title">List of prior research (expanded version)</h2>
<p>
Below are the main documents directly related to the open questions of U0-U15. For a detailed list of extensions, please read <a href="mind_uploading_papers.html">Paper Collection</a> and <a href="perspective.html#references">Perspective References</a>.
</p>

<h3>A. WBE basics, personality, philosophy</h3>
<ol>
<li>Sandberg, A., &amp; Bostrom, N. (2008). <em>Whole Brain Emulation: A Roadmap</em>.</li>
<li>Yamakawa, H., et al. (2024). Technology roadmap toward the completion of whole-brain architecture.</li>
<li>Parfit, D. (1984). <em>Reasons and Persons</em>.</li>
<li>Whitehead, A. N. (1929). <em>Process and Reality</em>.</li>
<li>Clowes, R. W. (2021). Slow Continuous Mind Uploading.</li>
<li>Weber, C. (2025). The multiplicity objection against uploading optimism.</li>
</ol>

<h3>B. Consciousness theory/verification index</h3>
<ol>
<li>Tononi, G. (2015). Integrated information theory.</li>
<li>Tononi, G., et al. (2016). IIT: from consciousness to its physical substrate.</li>
<li>Albantakis, L., et al. (2023). IIT 4.0.</li>
<li>Doerig, A., et al. (2019). The unfolding argument.</li>
<li>Boly, M., et al. (2017). Front vs back NCC debate.</li>
<li>Tsuchiya, N., et al. (2015). No-report paradigms.</li>
<li>Casali, A. G., et al. (2013). PCI.</li>
<li>Comolatti, R., et al. (2019). PCI-ST.</li>
<li>Ferrante, O., et al. (2025). Adversarial testing of GNWT and IIT.</li>
<li>Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing.</li>
<li>Fahrenfort, J. J., et al. (2025). Criterion placement threatens the construct validity of neural measures of conscious contents.</li>
<li>Casarotto, S., et al. (2024). Dissociations between spontaneous electroencephalographic features and perturbational complexity index in the minimally conscious state.</li>
<li>Maschke, C., et al. (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity.</li>
<li>Yoon, B., et al. (2024). Tracking the topology of neural manifolds across populations.</li>
<li>The topological structure of population activity in mouse visual cortex encodes visual stimuli. (2024).</li>
<li>Massimini, M., et al. (2005). Breakdown of effective connectivity during sleep.</li>
</ol>

<h3>C. Measurement/inverse problems/uncertainty estimation</h3>
<ol>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging review.</li>
<li>Wipf, D., &amp; Nagarajan, S. (2009). Unified Bayesian framework for MEG/EEG source imaging.</li>
<li>Cai, C., et al. (2021). Robust noise estimation with Champagne. <a href="https://doi.org/10.1016/j.neuroimage.2020.117411" target="_blank">doi:10.1016/j.neuroimage.2020.117411</a></li>
<li>Sechet, D., Kowalski, M., Mokhtari, S., &amp; Torrésani, B. (2025). Revisiting CHAMPAGNE: Sparse Bayesian Learning as Reweighted Sparse Coding. <a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">doi:10.1109/SAMPTA64769.2025.11133512</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Vorwerk, J., et al. (2014). Head volume conductor modeling guideline.</li>
<li>Aydin, U., Vorwerk, J., K&uuml;pper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Logothetis, N. K. (2008). What we can do and what we cannot do with fMRI. <a href="https://doi.org/10.1038/nature06976" target="_blank">doi:10.1038/nature06976</a></li>
<li>Purdon, P. L., et al. (2013). EEG signatures of loss/recovery of consciousness.</li>
<li>Boto, E., et al. (2018). Wearable OPM-MEG.</li>
</ol>

<h3>D. Preprocessing/synchronization/network analysis</h3>
<ol>
<li>Chang, C.-Y., et al. (2018). Evaluation of Artifact Subspace Reconstruction.</li>
<li>de Cheveigne, A. (2020). ZapLine.</li>
<li>Vinck, M., et al. (2011). Weighted Phase Lag Index (wPLI).</li>
<li>Staniek, M., &amp; Lehnertz, K. (2008). Symbolic Transfer Entropy.</li>
<li>Wilson, J. A., Mellinger, J., Schalk, G., &amp; Williams, J. C. (2010). A procedure for measuring latencies in brain-computer interfaces. <a href="https://doi.org/10.1109/TBME.2010.2047259" target="_blank">doi:10.1109/TBME.2010.2047259</a></li>
<li>Thompson, D. E., Warschausky, S. A., &amp; Huggins, J. E. (2013). Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. <a href="https://doi.org/10.1088/1741-2560/10/1/016006" target="_blank">doi:10.1088/1741-2560/10/1/016006</a></li>
<li>Mowla, M. R., Huggins, J. E., &amp; Thompson, D. E. (2017). Enhancing P300-BCI performance using latency estimation. <a href="https://doi.org/10.1080/2326263X.2017.1338010" target="_blank">doi:10.1080/2326263X.2017.1338010</a></li>
<li>Belinskaia, A., Smetanin, N., Lebedev, M., &amp; Ossadtchi, A. (2020). Short-delay neurofeedback facilitates training of the parietal alpha rhythm. <a href="https://doi.org/10.1088/1741-2552/abc8d7" target="_blank">doi:10.1088/1741-2552/abc8d7</a></li>
<li>Mansouri, F., Fettes, P., Schulze, L., et al. (2018). A real-time phase-locking system for non-invasive brain stimulation. <a href="https://doi.org/10.3389/fnins.2018.00877" target="_blank">doi:10.3389/fnins.2018.00877</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in the human motor cortex. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Little, S., Pogosyan, A., Neal, S., et al. (2013). Adaptive deep brain stimulation in advanced Parkinson disease. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser, G., Pogosyan, A., Little, S., et al. (2017). The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Hernandez-Pavon, J. C., Metsomaa, J., Mutanen, T. P., et al. (2023). TMS combined with EEG: Recommendations and open issues. <a href="https://doi.org/10.1016/j.brs.2023.02.009" target="_blank">doi:10.1016/j.brs.2023.02.009</a></li>
<li>Appelhoff, S., &amp; Stenner, T. (2021). In COM we trust: Feasibility of USB-based event marking. <a href="https://doi.org/10.3758/s13428-021-01571-z" target="_blank">doi:10.3758/s13428-021-01571-z</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
</ol>

<h3>E. Decoding, generative model, imitation separation</h3>
<ol>
<li>Huth, A. G., de Heer, W. A., Griffiths, T. L., Theunissen, F. E., &amp; Gallant, J. L. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex. <a href="https://doi.org/10.1038/nature17637" target="_blank">doi:10.1038/nature17637</a></li>
<li>Tang, J., LeBel, A., Jain, S., et al. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>D&eacute;fossez, A., Caucheteux, C., Rapin, J., Kabeli, O., &amp; King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">doi:10.1038/s42256-023-00714-5</a></li>
<li>Horikawa, T. (2025). Mind captioning: Evolving descriptive text of mental content from human brain activity. <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">doi:10.1126/sciadv.adw1464</a></li>
<li>d'Ascoli, S., Ferrante, O., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain&ndash;computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
</ol>

<h3>F. Causal inference/active inference/counterfactual hypothetical</h3>
<ol>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Friston, K. (2010). Free-energy principle.</li>
<li>Friston, K. (2017). Active inference: a process theory.</li>
<li>Parr, T., &amp; Friston, K. J. (2019). Generalised free energy.</li>
<li>Lee, H.-L., Zahneisen, B., Hugger, T., et al. (2017). Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.012" target="_blank">doi:10.1016/j.neuroimage.2017.02.012</a></li>
<li>Frässle, S., Manjaly, Z. M., Do, C. T., Kasper, L., Pruessmann, K. P., &amp; Stephan, K. E. (2021). Whole-brain estimates of directed connectivity for human connectomics. <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Wu, H., Hu, X., &amp; Zeng, Y. (2024). A fast dynamic causal modeling regression method for fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">doi:10.1016/j.neuroimage.2024.120954</a></li>
<li>Jafarian, A., Assem, M. K., Kocagoncu, E., et al. (2024). Reliability of dynamic causal modelling of resting-state magnetoencephalography. <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Hauser, A., &amp; B&uuml;hlmann, P. (2012). Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. <a href="https://jmlr.org/papers/v13/hauser12a.html" target="_blank">JMLR</a></li>
<li>Vink, J. J., Ramos-Nu&ntilde;ez, A. I., Bellesi, A., et al. (2020). The brain's functional connectome is a poor predictor of the brain's causal activity flow. <a href="https://doi.org/10.1371/journal.pcbi.1007866" target="_blank">doi:10.1371/journal.pcbi.1007866</a></li>
<li>Laukkonen, R., Friston, K., &amp; Chandaria, S. (2025). A beautiful loop.</li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested counterfactual identification.</li>
</ol>

<h3>G. Biological constraints (connectome, neuromodulation, glia)</h3>
<ol>
<li>Cook, S. J., et al. (2019). Whole-animal connectomes of both <em>C. elegans</em> sexes.</li>
<li>Scheffer, L. K., et al. (2020). Adult <em>Drosophila</em> central brain connectome.</li>
<li>Kasthuri, N., et al. (2015). Saturated reconstruction of neocortex volume.</li>
<li>Santello, M., et al. (2019). Astrocyte-neuron interactions.</li>
<li>Ozcete, O. D., et al. (2024). Neuromodulatory volume transmission.</li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Goulas, A., Changeux, J.-P., Wagstyl, K., et al. (2021). The natural axis of transmitter receptor distribution in the human cerebral cortex. <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">doi:10.1073/pnas.2020574118</a></li>
<li>Koepp, M. J., Gunn, R. N., Lawrence, A. D., et al. (1998). Evidence for striatal dopamine release during a video game. <a href="https://doi.org/10.1038/30498" target="_blank">doi:10.1038/30498</a></li>
<li>Lippert, R. N., Cremer, A. L., Edwin Thanarajah, S., et al. (2019). Time-dependent assessment of stimulus-evoked regional dopamine release. <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">doi:10.1038/s41467-018-08143-4</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
</ol>

<h3>H. Standardization, reproducibility, ethics, system</h3>
<ol>
<li>Gorgolewski, K. J., et al. (2016). BIDS.</li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS.</li>
<li>Fleming, S. M., et al. (2023). Open letter on IIT interpretability and testability.</li>
<li>Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI.</li>
<li>Ienca, M., &amp; Andorno, R. (2017). New human rights in neuroscience.</li>
<li>Schumer, C., et al. (2025). MIND Act discourse.</li>
</ol>

<h3>I. Thermodynamics, irreversibility, energy budget</h3>
<ol>
<li>B&eacute;rut, A., Arakelyan, A., Petrosyan, A., et al. (2012). Experimental verification of Landauer&rsquo;s principle linking information and thermodynamics. <a href="https://doi.org/10.1038/nature10872" target="_blank">doi:10.1038/nature10872</a></li>
<li>Attwell, D., &amp; Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">doi:10.1097/00004647-200110000-00001</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., et al. (2021). Broken detailed balance and entropy production in the human brain. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>de la Fuente, L. A., Perl, Y. S., Zamberlan, F., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., Bonetti, L., Fern&aacute;ndez-Rubio, G., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="key-points">
<h4>What you get from this page</h4>
<ul>
<li>Summary of question tree (detailed version) on one page</li>
<li>Fixing the definition of advancement (claim staircase)</li>
<li>Search by folding and filtering</li>
<li>Learning order (don't get lost)</li>
<li>First primary/review link</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Filter</h4>
<input id="qaSearch" class="filter-input" type="text" placeholder="Narrow down by keywords (e.g. EEG, causality, identity)">
<p class="small" style="margin-top: 10px;">Category</p>
<div class="checkbox-grid" style="margin-top: 8px;">
<label><input type="checkbox" name="qaTag" value="meta">Meta</label>
<label><input type="checkbox" name="qaTag" value="measurement">Measurement</label>
<label><input type="checkbox" name="qaTag" value="reconstruction">Reconstruction</label>
<label><input type="checkbox" name="qaTag" value="implementation">Implementation</label>
<label><input type="checkbox" name="qaTag" value="verification">Verification</label>
<label><input type="checkbox" name="qaTag" value="deployment">Deployment</label>
</div>
<div class="controls" style="margin-top: 12px;">
<button class="btn" id="qaClear" type="button">Clear</button>
<button class="btn" id="qaExpandAll" type="button">Expand</button>
<button class="btn" id="qaCollapseAll" type="button">Collapse</button>
</div>
<p class="small" id="qaStatus" style="margin-top: 10px;">Display: -/-</p>
</div>

<div class="sidebar-box">
<h4>On this page</h4>
<ul>
<li><a href="#howto">How to Use</a></li>
<li><a href="#measurement-identifiability-audit">2026-03 Literature Audit</a></li>
<li><a href="#definition">Definition of forward</a></li>
<li><a href="#roadmap-index">Index</a></li>
<li><a href="#tree">Tree of questions</a></li>
<li><a href="#measurement">Measurement</a></li>
<li><a href="#reconstruction">Reconstruction</a></li>
<li><a href="#implementation">Implementation</a></li>
<li><a href="#verification">Verification</a></li>
<li><a href="#unsolved">Defining an unsolved problem</a></li>
<li><a href="#priorwork-map">Previous research map</a></li>
<li><a href="#deployment">Social implementation</a></li>
<li><a href="#learning">Learning order</a></li>
<li><a href="#mind-upload">Mind-Upload current location</a></li>
<li><a href="#sources">References</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Links</h4>
<ul>
<li><a href="index.html">Start</a></li>
<li><a href="issue.html#proposal-integration">Proposal integration clause in issue</a></li>
<li><a href="mind_uploading_papers.html">Paper Collection</a></li>
<li><a href="brain_science_dictionary.html">Brain Science Dictionary</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload" target="_blank">GitHub Repository</a></li>
<li><a href="issue.html">Contribute Guide</a></li>
</ul>
</div>

</aside>
</main>

<footer>
<p>Mind-Upload / Technology roadmap (tentative)</p>
</footer>

<script>
(function () {
var searchInput = document.getElementById('qaSearch');
var clearBtn = document.getElementById('qaClear');
var expandBtn = document.getElementById('qaExpandAll');
var collapseBtn = document.getElementById('qaCollapseAll');
var statusEl = document.getElementById('qaStatus');

if (!searchInput || !statusEl) return;

function toArray(nodeList) {
return Array.prototype.slice.call(nodeList || []);
}

var checkboxes = toArray(document.querySelectorAll('input[name="qaTag"]'));
var qas = toArray(document.querySelectorAll('details.qa'));
var groups = toArray(document.querySelectorAll('[data-qa-group]'));

function selectedTags() {
return checkboxes
.filter(function (cb) { return cb.checked; })
.map(function (cb) { return cb.value; });
}

function matchesTags(qaTags, selected) {
if (!selected.length) return true;
for (var i = 0; i < selected.length; i++) {
if (qaTags.indexOf(selected[i]) !== -1) return true;
}
return false;
}

function matchesText(text, query) {
if (!query) return true;
return text.indexOf(query) !== -1;
}

function applyFilters() {
var query = (searchInput.value || '').trim().toLowerCase();
var selected = selectedTags();
var visibleCount = 0;

qas.forEach(function (qa) {
var qaTags = (qa.getAttribute('data-tags') || '')
.split(/\s+/)
.filter(Boolean);
var text = (qa.textContent || '').toLowerCase();
var show = matchesTags(qaTags, selected) && matchesText(text, query);
qa.style.display = show ? '' : 'none';
if (show) visibleCount += 1;
});

groups.forEach(function (g) {
var groupQas = toArray(g.querySelectorAll('details.qa'));
var anyVisible = groupQas.some(function (qa) { return qa.style.display !== 'none'; });
g.style.display = anyVisible ? '' : 'none';
});

statusEl.textContent = 'Display: ' + visibleCount + '/' + qas.length;
}

function visibleQAs() {
return qas.filter(function (qa) { return qa.style.display !== 'none'; });
}

searchInput.addEventListener('input', applyFilters);
checkboxes.forEach(function (cb) { cb.addEventListener('change', applyFilters); });

if (clearBtn) {
clearBtn.addEventListener('click', function () {
searchInput.value = '';
checkboxes.forEach(function (cb) { cb.checked = false; });
applyFilters();
searchInput.focus();
});
}

if (expandBtn) {
expandBtn.addEventListener('click', function () {
visibleQAs().forEach(function (d) { d.open = true; });
});
}

if (collapseBtn) {
collapseBtn.addEventListener('click', function () {
visibleQAs().forEach(function (d) { d.open = false; });
});
}

applyFilters();
})();
</script>
