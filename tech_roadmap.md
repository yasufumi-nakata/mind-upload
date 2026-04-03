---
layout: default
title: "Technical Roadmap: Understanding WBE Through Measurement, Reconstruction, and Implementation"
description: "A learning roadmap for viewing mind uploading and WBE from the technical side, organized as a question tree from measurement to reconstruction, implementation, and verification."
article_type: "Roadmap (Definition #1)"
subtitle: "Break 'what counts as progress' into a question tree with reading order and minimum arrival conditions"
last_updated: "2026-04-03"
note: "Provisional draft (updated continuously; summary-layer astrocyte PET route sync on 2026-04-03)"
audience: "Readers who want the big picture, need a learning order, or want claim strength organized by level"
reading_time: "20-30 min (5 min for the index only)"
page_intro: "This page is a map of WBE questions arranged under measurement, reconstruction, implementation, verification, and social deployment. Its purpose is to keep the reader from losing track of which problems are foundational and which remain unresolved."
accuracy_note: "This page organizes the research landscape. It does not mean that the listed items are already solved."
page_highlights:
  - "P0-P2 fix what counts as success before measurement or implementation work is discussed."
  - "The index allows readers to jump directly to a specific question family."
  - "Stronger claims are deliberately placed later so earlier levels are not skipped."
  - "V8 now splits invasive language BCIs into throughput / expressivity, transfer-assisted initialization, fixed-decoder durability slices, and adaptive rescue, so one speech-BCI result is not silently promoted to all four."
  - "R0 now separates structural scaffold, fast executable state, and maintenance-state families, so `connectome + state` is not treated as one knob."
  - "R3 / R5 separate latent-state and maintenance-state questions by evidence tier and timescale, so same-day fit and multiday maintenance do not collapse into one success."
  - "R3 / R5 now force maintenance-relevant claims to name whether phospho-signaling, local proteostasis, and cargo-routing were measured, externally calibrated, model-estimated, or omitted, so a generic latent-state label is not treated as maintenance-complete evidence."
  - "M2 separates hardware latency from biological timing-state, so a fast device loop is not confused with timing-complete reconstruction."
  - "For phase-targeted closed loops, M2 / I1 now separate oscillation estimability, causal-versus-post-hoc targeting benchmark, circular targeting precision, downstream effect, and phase stability, so phase error alone is not treated as sufficient evidence."
  - "M1 / M5 keep neural state distinct from vascular transfer state, so a BOLD amplitude difference is not silently promoted to a neural difference."
  - "M1 / M3 now treat human in vivo evidence as a split ladder, so proxy class, operational maturity, calibrator role, and family-internal quantity / target / transport differences are kept separate instead of being collapsed into one observability score."
  - "M1 / M3 now also keep human barrier-side evidence split inside the blood-CSF-barrier lane itself, so choroid-plexus perfusion, blood-to-CSF transport, water cycling, and apparent BCSFB exchange are not silently merged into BBB water-exchange or tracer-specific BBB transport."
  - "M1 / M3 now also separate human local clinical-unit allocation from noninvasive perturbation-conditioned excitability routes, so `human excitability evidence` is not treated as one row."
  - "M1 / M3 now also split human astrocyte-related PET into SMBT-1 MAO-B target-validation / disease-context / quantification / biodistribution routes, SL25.1188 MAO-B quantification / severity-conditioned routes, and I2BS routes, so `astrocyte PET` is not treated as one interchangeable human row."
  - "M3 now also keeps cohort / physiological regime compatibility and row robustness / availability separate from those three per-row axes, so a proxy-rich bundle is not silently treated as one matched human baseline or one stable stack."
  - "M4 / I6 now treat the body / environment boundary as an explicit scientific audit item across fast loop routes and slow internal-milieu routes, so a fast local loop is not silently promoted to solved embodiment."
  - "M7 / V4 now separate state annotation, trait-like backbone, biological drift, interface / decoder drift, and recalibration burden, so same-day success and adaptive rescue do not collapse into one longitudinal claim."
  - "Wearable OPM-MEG is treated as movement-tolerant macro measurement only when shielding, field control, sensor calibration, and anatomy choice are disclosed."
  - "R6 treats personalization not as a pure performance trick, but as a verification problem that must separate target signal from subject fingerprint and setup shortcuts."
  - "R1 / R2 now separate focal posterior-support, sparse debiased inference, extended-source extent reconstruction, forward-model uncertainty, and validation board, so a newer inverse family is not silently treated as one generic truth upgrade."
  - "R4 now treats DCM / effective-connectivity outputs as route-card claims that must disclose model space, observed-subsystem closure / latent-confound audit, node-definition policy, sampling / transformation sensitivity, observation assumptions, validation, reliability, and abstention."
  - "R7 now separates observability, structural identifiability, practical identifiability, ambiguity class, and minimum-sufficiency stop rules, so richer proxies or more modalities are not silently promoted to uniqueness."
known_points:
  - "Splitting the problem into P/M/R/I/V/D makes it easier to see which questions are foundational and which sit higher up."
  - "The dependency structure that prevents strong claims from skipping earlier layers is fairly clear."
  - "This page should be read as a dependency map, not as a checklist of solved items."
  - "Invasive language BCI progress is multi-route: throughput, transfer initialization, fixed-decoder durability, and adaptive rescue need separate labels."
  - "A restoration target is not one dial; scaffold, fast state, and maintenance-state layers place different ceilings on what can be claimed."
  - "Even if connectome or local-activity evidence improves, latent-state and maintenance-state audits are still separate requirements."
  - "A prediction-useful latent variable is not automatically a maintenance-complete state estimate; phospho-signaling, local proteostasis, and cargo-routing can still remain omitted families."
  - "For hemodynamic modalities, neural interpretation and vascular transfer / CVR audit are separate requirements."
  - "Closed-loop device timing and biological conduction timing are different audits; passing one does not auto-pass the other."
  - "For phase-targeted loops, a low mean phase error still does not prove that the target oscillation was estimable, that the causal estimator matched a post-hoc benchmark, that the physiological or behavioral effect followed, or that one preferred phase stayed stable across time."
  - "A disclosed body / environment boundary, including slow internal-milieu disclosure, is a separate audit from low latency or online accuracy."
  - "Human-side advances reduce different error terms and remain differently deployment-limited; proxy-rich evidence is not yet same-subject, same-session, externally calibrated state identification."
  - "Proxy class, operational maturity, and calibrator role are different questions; a real human route may still calibrate only one bounded hidden-state family."
  - "A human route family name is not yet one row; 1H-MRSI similarity, high-resolution 1H-MRSI metabolite-distribution mapping, 31P metabolite / pH balance, 31P MT exchange-flux, 31P NAD-content mapping, localized functional 31P NAD-dynamics, deuterium metabolite-mapping / absolute-quantification routes, deuterium kinetic-rate imaging, tract-scale transmission-speed estimation, quantity-defined myelin MRI / tissue-health-sensitive ratios, BBB water-exchange, tracer-specific BBB PET transport, blood-CSF barrier / choroid-plexus perfusion / blood-to-CSF transport / water-cycling / apparent-exchange routes, SMBT-1 MAO-B target-validation / disease-context / quantification / biodistribution routes, SL25.1188 MAO-B quantification / severity-conditioned routes, and I2BS routes remain separate routes with different ceilings."
  - "Human clinical single-unit allocation, sleep-homeostasis / plasticity recalibration, and state-gated perturbation are also separate human routes with different direct observables and different ceilings."
  - "A named astrocyte-related PET paper is not yet one route family; MAO-B target validation, MAO-B disease-context contrast, MAO-B quantification / biodistribution burden, SL25.1188 covariate ceilings, and I2BS routes remain separate questions."
  - "Even when human proxy rows look complementary, cohort / physiological regime mismatch, route-local repeatability, cross-centre transfer, and complete-case availability still remain separate gates."
  - "Longitudinal success is not one axis; within-day state fluctuation, trait-like backbone, biological drift, interface / decoder drift, and recalibration burden answer different questions."
  - "OPM-MEG motion tolerance still depends on magnetic shielding, active nulling, calibration, and source-model disclosure."
  - "The fact that personalization helps performance is not the same as showing a population-level neural signal; subject-fingerprint and acquisition-distribution audits are still required."
  - "For ESI, source regime / target object, uncertainty object, forward-model uncertainty route, and validation board remain separate requirements; a stronger inverse family is not one universal answer type."
  - "Richer observability and better fit do not by themselves collapse the compatible solution set; ambiguity class, candidate-space, bridge / composition validity, experiment-design leverage, and minimum-sufficiency stop rules remain separate."
unknown_points:
  - "It is still unsettled which measurement granularity will ultimately be sufficient for WBE."
  - "V5 identity questions and D-series social deployment conditions remain unresolved."
  - "The shortest practical route may change as data and benchmark infrastructure improve."
  - "How specialized human routes can be fused into same-subject, same-session, externally calibrated evidence without recreating latent-state ambiguity remains unresolved."
  - "It also remains unsettled which backbone object should be the default target for WBE-relevant longitudinal claims: latent dynamics, representational geometry, or another cross-modal invariant."
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
  - label: "Wiki: State-Continuity Bridge"
    url: "/wiki/state-continuity-bridge.html"
    description: "Explains why same-subject or same-brain sequential workflows still need a bridge audit before same-state language is allowed."
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
<strong>If You Want The Current Human In Vivo Measurement Ladder First</strong>
<p>
This roadmap now distinguishes not only <strong>which variable class a human route constrains</strong> but also <strong>how specialized or model-heavy that route still is</strong>. The site's current rule is stricter than a simple three-axis ladder: per-row <strong>proxy class / operational maturity / calibrator role</strong> still has to be combined with bundle-level checks on <strong>cohort / physiological regime compatibility</strong> and <strong>row robustness / availability disclosure</strong>. For the front-door ladder, start with <a href="wbe_101.html#human-observability-ladder">WBE 101: human observability ladder</a>; for stack-specific ceilings and stop rules, see <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: observability and claim ceiling by measurement stack</a> and <a href="verification.html#observability-budget">Verification: Observability Budget</a>. If the argument also bridges live measurement to later fixation / ex vivo follow-up or cross-day reacquisition, add the <a href="verification.html#state-continuity-bridge-card">Verification: State-Continuity Bridge Card</a> and <a href="wiki/state-continuity-bridge.html">Wiki: State-Continuity Bridge</a> instead of reading <strong>same-subject</strong> or <strong>same-brain</strong> as <strong>same-state</strong> by default.
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
<div class="note-box">
<strong>If You Want The Quantitative Reason Non-invasive Routes Still Stop Early</strong>
<p>
The updated measurement-stack wiki now makes explicit why EEG / MEG remain conditional for deep sources even after intracranial validation, and why hemodynamic amplitudes remain limited by vascular-transfer and autonomic-state confounds. For the direct-validation numbers and the resulting ceiling, see <a href="wiki/measurement-stack-and-claim-ceiling.html#eeg-meg-validation-wall">Wiki: EEG / MEG visibility, inverse, and validation wall</a> and <a href="wiki/measurement-stack-and-claim-ceiling.html#hemodynamic-transfer-wall">Wiki: hemodynamic transfer wall</a>.
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
<td><strong>local transmitter sensor / axon imaging</strong></td>
<td>Local transmitter-linked fluorescence or cholinergic / neuromodulatory axon activity in a named region. </td>
<td>Calibrates what mixed arousal proxies do and do not mean, and constrains region-specific chemical timing under an explicit local observable. </td>
<td>Whole-brain transmitter field, unsampled receptor families, and same-subject human maintenance-state remain unresolved. </td>
</tr>
<tr>
<td><strong>local astrocyte imaging / ensemble readout</strong></td>
<td>Astrocyte Ca<sup>2+</sup> dynamics, network-state response, or labeled ensemble activity in a local preparation. </td>
<td>Strengthens slow-state omission audits and local transmitter-to-astrocyte coupling claims without pretending that glia are background noise. </td>
<td>Human whole-brain astrocyte-state, content-general controller identity, and cross-day maintenance completeness remain unresolved. </td>
</tr>
<tr>
<td><strong>human receptor / transporter atlas + occupancy PET + displacement / release PET</strong></td>
<td>Regional receptor / transporter density priors, administered-drug target engagement, or challenge-linked release proxies. </td>
<td>Constrains chemoarchitectural prior, selected receptor-target engagement, or bounded endogenous release proxy for named receptor families. </td>
<td>Instantaneous whole-brain transmitter field, unsampled receptor families, and cell-specific downstream effect remain unresolved. </td>
</tr>
<tr>
<td><strong>human astrocyte-related PET: MAO-B target-validation route</strong></td>
<td>Tracer-family-specific MAO-B binding in healthy humans under named blocker or kinetic-model assumptions. </td>
<td>Establishes that a named MAO-B tracer family has human brain entry, selective binding, and a bounded astrocyte-related route role. </td>
<td>Disease contrast, tracer-family transfer, covariate ceiling, local controller identity, and same-subject whole-brain maintenance-state remain unresolved. </td>
</tr>
<tr>
<td><strong>human astrocyte-related PET: MAO-B disease-context route</strong></td>
<td>Named-tracer MAO-B contrast across a declared cohort, disease stage, and reference-model choice. </td>
<td>Constrains a bounded disease- and cohort-conditioned astrocyte-related support-state contrast for that specific tracer family. </td>
<td>Route-general quantification, cross-cohort generalization, smoking / severity ceiling, local controller identity, and same-subject whole-brain maintenance-state remain unresolved. </td>
</tr>
<tr>
<td><strong>human astrocyte-related PET: MAO-B quantification / covariate route</strong></td>
<td>Arterial or simplified MAO-B quantification behavior plus cohort- or smoking-conditioned binding shift for a named tracer family. </td>
<td>Constrains scan-window / reference-region / kinetic-model choice and covariate ceilings instead of silently promoting the family to one generic meter. </td>
<td>Other tracer families, local controller identity, and same-subject whole-brain maintenance-state remain unresolved. </td>
</tr>
<tr>
<td><strong>human astrocyte-related PET: I<sub>2</sub>BS route</strong></td>
<td>Tracer-specific I<sub>2</sub>BS binding under named pharmacologic and kinetic-model assumptions. </td>
<td>Constrains a different target-defined astrocyte-related proxy family rather than a drop-in replacement for MAO-B. </td>
<td>Interchangeability with MAO-B routes, disease-general transfer, local controller identity, and same-subject whole-brain maintenance-state remain unresolved. </td>
</tr>
<tr>
<td><strong>human clearance-support proxy</strong></td>
<td>CSF mobility or biomarker-efflux proxy under named device and model assumptions. </td>
<td>Constrains macro support-state burden and blocks omission of human clearance routes from human arguments. </td>
<td>Local immune-controller identity, responsible synapse, and same-subject whole-brain maintenance-state remain unresolved. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-25 addendum: transmitter, astrocyte, receptor-PET, and clearance routes are not one stack</strong>
<p>
The remaining weakness at M1 was that one row still let <strong>local transmitter sensors</strong>, <strong>astrocyte-state readouts</strong>, <strong>human receptor / transporter PET routes</strong>, and <strong>human astrocyte / clearance proxies</strong> sound closer than they are. The primary literature does not support that compression. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> showed that pupil fluctuations track both adrenergic and cholinergic activity rather than one transmitter, <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> showed that local cortical acetylcholine depends on cholinergic axon activity and local clearance kinetics, <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> built a regional receptor / transporter atlas, <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a> constrain occupancy and challenge-limited release, <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> showed minute-scale cortical astrocyte-network encoding, <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">Villemagne et al. (2022)</a> established a first-in-human SMBT-1 MAO-B route, <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a> then measured reactive astrogliosis across the AD spectrum within that tracer family, <a href="https://doi.org/10.1007/s12149-025-02083-y" target="_blank">Hiraoka et al. (2025)</a> showed that SMBT-1 quantification still depends on named scan-window / reference-region choices relative to kinetic modeling, <a href="https://doi.org/10.1007/s12149-025-02144-2" target="_blank">Mesfin et al. (2026)</a> added a separate whole-body biodistribution burden for the same tracer family, <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">Matsuoka et al. (2026)</a> showed that 11C-SL25.1188 in AD depends on its own simplified quantification route, <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a> plus <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">Livingston et al. (2022)</a> showed that a human I<sub>2</sub>BS route is a different target class with region- and stage-dependent behavior, <a href="https://doi.org/10.1038/s41380-025-03355-9" target="_blank">Best et al. (2026)</a> showed that MAO-B binding can shift with cohort severity and daily cigarette use, <a href="https://doi.org/10.1007/s00401-024-02712-2" target="_blank">Jaisa-Aad et al. (2024)</a> showed in postmortem tissue that MAO-B is promising but still bounded as a reactive-astrogliosis biomarker, and <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> plus <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> constrain human CSF mobility and sleep-linked biomarker efflux. These routes do not share the same direct observable, target class, tracer family, quantity type, or safe claim ceiling. On this roadmap, they therefore stay separated into <strong>local chemical calibration</strong>, <strong>local astrocyte-state readout</strong>, <strong>human neuromodulatory PET prior / engagement</strong>, <strong>human MAO-B target-validation / disease-context / quantification routes</strong>, <strong>human I<sub>2</sub>BS astrocyte-related PET</strong>, and <strong>human support-state proxy</strong> rows.
</p>
</div>
<div class="note-box">
<strong>2026-04-01 addendum: astrocyte PET family labels are not one roadmap row</strong>
<p>
The remaining weakness after the earlier split was internal to the astrocyte-related PET family itself. <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">Villemagne et al. (2022)</a> answered the first-in-human target-validation question for SMBT-1, <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a> answered an AD-spectrum disease-context question, <a href="https://doi.org/10.1007/s12149-025-02083-y" target="_blank">Hiraoka et al. (2025)</a> answered a tracer-family quantification question, <a href="https://doi.org/10.1007/s12149-025-02144-2" target="_blank">Mesfin et al. (2026)</a> answered a whole-body biodistribution and operational-burden question, <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">Matsuoka et al. (2026)</a> answered a simplified SL25.1188 quantification question in AD, <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a> answered a first-in-human I<sub>2</sub>BS target question, and <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">Livingston et al. (2022)</a> plus <a href="https://doi.org/10.1038/s41380-025-03355-9" target="_blank">Best et al. (2026)</a> showed that cognitively impaired and AUD cohorts add stage, severity, and smoking ceilings rather than one route-free astrocyte scalar. In parallel, <a href="https://doi.org/10.1007/s00401-024-02712-2" target="_blank">Jaisa-Aad et al. (2024)</a> showed in postmortem tissue that MAO-B is a promising but bounded biomarker of reactive astrogliosis rather than a generic astrocyte-state meter. Therefore this roadmap now forces readers to keep <strong>target class</strong>, <strong>tracer family</strong>, <strong>route role</strong>, <strong>quantification choice</strong>, and <strong>cohort / covariate ceiling</strong> separate before promoting any human astrocyte-related PET result.
</p>
</div>
<div class="note-box">
<strong>2026-03 Supplement: multimodal is not a synonym for "I could see everything"</strong>
<p>
Mikulan et al. (2020), Seeber et al. (2019), Unnwongse et al. (2023), and Hao et al. (2025) moved forward what can be audited by combining HD-EEG with intracranial ground truth. By contrast, Yao et al. (2023)'s whole-brain spatial atlas, the Patch-seq bridges of Gouwens et al. (2021) and Gamlin et al. (2025), the connectomics of Dorkenwald et al. (2024) and MICrONS Consortium et al. (2025), local transmitter and astrocyte readouts such as Neyhart et al. (2024) and Cahill et al. (2024), and human proxy routes such as Hansen et al. (2022), Villemagne et al. (2022, SMBT-1 target validation / AD-spectrum), Hiraoka et al. (2025), Mesfin et al. (2026), Matsuoka et al. (2026), Tyacke et al. (2018), Livingston et al. (2022), Hirschler et al. (2025), and Dagum et al. (2026) each strengthen different variables while leaving different latent states unresolved. Therefore, this page distinguishes clearly between <strong>increasing the number of observations</strong> and <strong>sufficiently identifying the state variables required for WBE</strong>. For the stack-by-stack layout, see <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: observability and claim ceiling for each measurement stack</a>.
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
<p>
The phase-targeting case now needs one more split on this page. <a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">Zrenner et al. (2020)</a> showed that phase estimability itself worsens when oscillatory amplitude and SNR are low, <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">Gordon et al. (2021)</a> improved prefrontal theta targeting by adding amplitude and stability constraints together with a post-hoc benchmark, <a href="https://doi.org/10.1523/ENEURO.0050-23.2023" target="_blank">Kim et al. (2023)</a> showed across <strong>11 public datasets</strong> and <strong>484 participants</strong> that prediction accuracy mostly tracks power and SNR, <a href="https://doi.org/10.1111/ejn.14931" target="_blank">Vigué-Guix et al. (2022)</a> achieved reliable trial-to-trial alpha phase locking without a consistent reaction-time benefit, and <a href="https://doi.org/10.1016/j.brs.2025.09.019" target="_blank">Hougland et al. (2025)</a> showed within-session fluctuation and low test-retest reliability of the optimal mu phase. Therefore, this roadmap no longer treats phase-targeted control as one timing number. It separates <strong>oscillation estimability</strong>, <strong>causal-versus-post-hoc benchmark</strong>, <strong>circular targeting precision</strong>, <strong>downstream effect</strong>, and <strong>phase stability / adaptation policy</strong>.
</p>
<ul>
<li><strong>Do not fix the common gate to 1 ms:</strong>Measure the end-to-end median, P95/P99, and worst-case for each loop type. </li>
<li><strong>Audit device and tissue separately:</strong>Hardware latency/jitter does not prove that biological timing-state has been recovered. </li>
<li><strong>For phase-targeting, log the estimability gate:</strong>Target band and spatial filter, spectral peak or power/SNR threshold, no-stim rate, and any phase-reset rejection rule. </li>
<li><strong>For phase-targeting, keep four extra logs beyond mean phase error:</strong>Causal-versus-post-hoc benchmark, circular spread, off-target or random-phase comparator, and fixed-versus-adaptive phase policy. </li>
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
<li><strong>Upper bound on the connectomics front:</strong>This is an audit of structural scaffolds, sequential same-brain local scaffolds, stimulus-conditioned conditional predictors, and cell-type dependent connections, not a complete observation of current synaptic efficiency and neuromodulation fields. </li>
<li><strong>Remaining latent states:</strong>Synaptic weight, receptor state, delay / timing-state, intrinsic excitability / homeostatic set point, neuromodulatory field, glial / metabolic state, and plastic history remain as separate variables. </li>
</ul>
<div class="note-box">
<strong>2026-03-27 addendum: three per-row axes are still not enough without quantity / target / transport splits, cohort, and robustness gates</strong>
<p>
The remaining weakness in this roadmap was that M3 still let very different human-side advances sound like one generic increase in <strong>observability</strong> and still let family names stand in for one route. The primary literature does not support that compression. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> reconstructed a cubic millimeter of surgically resected human temporal cortex at nanoscale resolution, which is a <strong>local ex vivo structural scaffold</strong>. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> built an in vivo SV2A atlas in healthy humans (<strong>17F/16M</strong>) calibrated with postmortem autoradiography, which is a <strong>regional synaptic-density proxy</strong>. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> aggregated receptor / transporter PET into a <strong>regional chemoarchitectural prior</strong>, while <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> constrains <strong>selected occupancy / target engagement</strong> under an administered drug and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, plus <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> constrain <strong>challenge-linked dopamine / serotonin release proxies</strong> rather than a free readout of the whole transmitter field. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> derived a within-subject metabolic similarity matrix from <strong>five</strong> <sup>1</sup>H-MRSI metabolites in <strong>51 healthy participants</strong> with replication in <strong>13</strong>, whereas <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> measured <strong>ATP synthesis, phosphorus metabolites, and intra-/extracellular pH</strong> in <strong>12 resting human brains</strong> with <sup>31</sup>P-MRS, <a href="https://doi.org/10.1002/mrm.26560" target="_blank">Ren et al. (2017)</a> measured <strong>PCr&rarr;&gamma;-ATP and Pi&rarr;&gamma;-ATP exchange flux</strong> in <strong>six subjects</strong> using <strong>three band-inversion modules</strong> plus a <strong>five-pool Bloch-McConnell-Solomon model</strong>, <a href="https://doi.org/10.3389/fnins.2024.1389111" target="_blank">Guo et al. (2024)</a> mapped <strong>whole-brain intracellular NAD content</strong> at <strong>7 T</strong>, and <a href="https://doi.org/10.1177/0271678X261415784" target="_blank">Kaiser et al. (2026)</a> measured <strong>task-evoked NAD<sup>+</sup> dynamics</strong> in a <strong>functionally localized occipital voxel</strong>. The deuterium routes split again inside that family: <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a> implemented a <strong>7 T absolute-quantification route</strong> for HDO / Glc / Glx / Lac maps under a dedicated quantification pipeline, whereas <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> used <strong>7 T dynamic DMRSI</strong>, <strong>blood-input measurements</strong>, and an <strong>explicit kinetic model</strong> to image metabolic-rate terms. Even that is still not route-free: <a href="https://doi.org/10.1002/jmri.29532" target="_blank">Ahmadian et al. (2025)</a> showed that human-brain DMI signal depends materially on the administered <strong>[6,6'-<sup>2</sup>H<sub>2</sub>]glucose dose</strong>, and <a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B&oslash;gh et al. (2024)</a> showed that <strong>repeatability at 3 T</strong> depends on a named <strong>acquisition and time-point regime</strong>, with the best repeatability at <strong>120 min</strong> in that protocol. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">van Blooijs et al. (2023)</a> show that living-human timing-support already splits at the route-family level, because <strong>tract-scale transmission-speed estimation</strong> is not the same quantity as myelin-sensitive contrast. <a href="https://doi.org/10.1038/s41598-018-28852-6" target="_blank">Hagiwara et al. (2018)</a>, <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a>, and <a href="https://doi.org/10.1111/bpa.70010" target="_blank">Galbusera et al. (2025)</a> show that human myelin MRI is already a <strong>quantity-defined family</strong> rather than one interchangeable meter, while <a href="https://doi.org/10.1007/s00234-025-03875-9" target="_blank">Colaes et al. (2026)</a> show that <strong>T1w/FLAIR</strong> may remain a broader <strong>tissue-health-sensitive ratio</strong> rather than a myelin-specific readout. <a href="https://doi.org/10.1002/nbm.5256" target="_blank">Morgan et al. (2024)</a> and <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">Padrela et al. (2025)</a> measure <strong>BBB water exchange</strong> with ASL and expose method- and model-dependent burdens, while <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a> measures <strong>tracer-specific BBB permeability-surface-area products</strong> with high-temporal-resolution dynamic PET across <strong>three radiotracers</strong>. <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">Villemagne et al. (2022)</a> established a first-in-human SMBT-1 <strong>MAO-B route</strong> with pharmacological blockade, <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a> then measured reactive astrogliosis across the AD continuum within that tracer family, <a href="https://doi.org/10.1007/s12149-025-02083-y" target="_blank">Hiraoka et al. (2025)</a> showed that even SMBT-1 depends on scan-window / reference-region versus kinetic-model choices, and <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a>, <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">Livingston et al. (2022)</a>, <a href="https://doi.org/10.1007/s00401-024-02712-2" target="_blank">Jaisa-Aad et al. (2024)</a>, plus <a href="https://doi.org/10.1038/s41380-025-03355-9" target="_blank">Best et al. (2026)</a> show that target class, region / stage pattern, tissue expression, and cohort covariates still matter. Meanwhile, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> plus <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> advanced human-side CSF mobility and sleep-linked clearance routes, but still through <strong>specialized MRI</strong> or an <strong>investigational device plus multicompartment model</strong>. Therefore, this roadmap now asks readers to label not only <strong>(1) proxy class</strong>, <strong>(2) operational maturity / acquisition burden</strong>, and <strong>(3) safe calibrator role</strong>, but also the <strong>family-internal quantity / target / transport definition</strong> before promoting any human in vivo claim.
</p>
<p>
One more split is necessary inside the human maintenance-state family. <a href="https://doi.org/10.1038/s41598-025-21967-7" target="_blank">Tallman et al. (2025)</a> add a <strong>local human clinical single-unit allocation route</strong> in epilepsy patients, but with firing explicitly treated as only an indirect excitability index and with no whole-brain coverage. <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">Huber et al. (2013)</a>, <a href="https://doi.org/10.1038/ncomms12455" target="_blank">Kuhn et al. (2016)</a>, and <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">Fehér et al. (2026)</a> instead define <strong>sleep-homeostasis / plasticity-recalibration routes</strong> through TMS-EEG or PAS outcomes, while <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> plus <a href="https://doi.org/10.1016/j.brs.2024.12.1193" target="_blank">Khatri et al. (2025)</a> define <strong>state-gated perturbation routes</strong> whose direct observables remain bounded plasticity-assay or corticospinal responses. Therefore, this roadmap no longer lets <strong>human excitability evidence</strong> stand in for one row: local clinical-unit allocation and noninvasive perturbation-conditioned routes now stay separate.
</p>
<table class="data-table">
<thead>
<tr>
<th>Human route</th>
<th>Proxy class</th>
<th>Operational maturity / burden</th>
<th>Safe calibrator role on this page</th>
<th>Why the ceiling remains</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Local human ultrastructure</strong><br>Shapson-Coe et al. (2024)</td>
<td>Local ex vivo structural scaffold</td>
<td>Destructive surgical-fragment route; not repeatable living-human acquisition</td>
<td>Structural scaffold only</td>
<td>Ex vivo fragment from one surgical sample, not living whole-brain current state</td>
</tr>
<tr>
<td><strong>SV2A PET atlas</strong><br>Johansen et al. (2024)</td>
<td>Regional synaptic-density proxy</td>
<td>Healthy-cohort atlas; tracer and quantification dependent</td>
<td>Bounded synaptic-density prior</td>
<td>Tracer-defined atlas; not momentary synaptic efficacy or cell-specific plasticity state</td>
</tr>
<tr>
<td><strong>Receptor / transporter atlas</strong><br>Hansen et al. (2022)</td>
<td>Regional chemoarchitectural prior</td>
<td>Aggregated PET atlas across many healthy individuals; receptor-family limited</td>
<td>Bounded neuromodulatory-family prior</td>
<td>Does not read out current transmitter release, occupancy, or whole-brain neuromodulatory state</td>
</tr>
<tr>
<td><strong>Occupancy PET</strong><br>Wong et al. (2013)</td>
<td>Ligand- and dose-limited target-engagement proxy</td>
<td>Administered-drug, receptor-family, and bounded scan-window design</td>
<td>Selected receptor-target engagement</td>
<td>Does not recover endogenous transmitter release, the general transmitter field, unsampled receptor families, or cell-specific downstream effect</td>
</tr>
<tr>
<td><strong>Displacement / release-sensitive PET</strong><br>Koepp et al. (1998); Lippert et al. (2019); Erritzoe et al. (2020)</td>
<td>Challenge-linked endogenous release proxy</td>
<td>Task-, drug-, ligand-, receptor-family-, kinetic-model-, and window-specific design</td>
<td>Bounded dopamine / serotonin release proxy under a named challenge</td>
<td>Does not recover a task-general transmitter field, unsampled receptor families, or cell-specific downstream effect outside the measured window</td>
</tr>
<tr>
<td><strong><sup>1</sup>H-MRSI metabolic connectome</strong><br>Lucchetti et al. (2025)</td>
<td>Parcel-level biochemical similarity scaffold</td>
<td>51 healthy participants with 13-person replication; QC and parceling dependent</td>
<td>Bounded biochemical scaffold</td>
<td>Five-metabolite similarity matrix, not high-resolution metabolite distribution, not energetic balance, and not kinetic rate imaging</td>
</tr>
<tr>
<td><strong>Human <sup>31</sup>P-MRS energetic balance</strong><br>Ren et al. (2015)</td>
<td>Macro <sup>31</sup>P energetic-balance proxy</td>
<td>7 T resting-brain spectroscopy in 12 subjects; phosphorus-specific acquisition and fitting burden</td>
<td>Bounded energetic-balance proxy</td>
<td>ATP synthesis / phosphorus metabolite / pH balance, not branch-local mitochondrial controller state</td>
</tr>
<tr>
<td><strong>Human <sup>31</sup>P MT exchange-flux route</strong><br>Ren et al. (2017)</td>
<td>Model-conditioned macro <sup>31</sup>P MT exchange-flux proxy</td>
<td>7 T band-inversion transfer route in 6 subjects with three ~8 min modules and five-pool modeling burden</td>
<td>Bounded <sup>31</sup>P exchange-flux proxy</td>
<td>PCr&rarr;&gamma;-ATP and Pi&rarr;&gamma;-ATP exchange-flux under a named MT model, not resting energetic balance, NAD mapping, or branch-local mitochondrial controller state</td>
</tr>
<tr>
<td><strong>Human <sup>31</sup>P NAD-content mapping</strong><br>Guo et al. (2024)</td>
<td>Macro <sup>31</sup>P NAD-content map proxy</td>
<td>7 T whole-brain route with subspace-based denoising, low-concentration spectral fitting, and long acquisition burden</td>
<td>Bounded whole-brain NAD-content map proxy</td>
<td>Not task-evoked local NAD dynamics, not branch-local mitochondrial controller state, and not whole-brain moment-to-moment redox control</td>
</tr>
<tr>
<td><strong>Human <sup>31</sup>P functional NAD dynamics</strong><br>Kaiser et al. (2026)</td>
<td>Localized functional <sup>31</sup>P NAD-dynamics proxy</td>
<td>7 T task fMRS in 25 volunteers with prior fMRI localization and one occipital voxel</td>
<td>Bounded task-locked local NAD-dynamics proxy</td>
<td>Not whole-brain NAD-content mapping, not task-general energetic-controller identity, and not branch-local mitochondrial controller state</td>
</tr>
<tr>
<td><strong>Deuterium metabolite-mapping / absolute-quantification route</strong><br>Karkouri et al. (2026)</td>
<td>Macro deuterium metabolite-mapping / absolute-quantification proxy</td>
<td>7 T specialized route with absolute-quantification pipeline, dedicated hardware, limited cohorts, and route-specific dose / timing burden</td>
<td>Bounded deuterium metabolite-mapping proxy</td>
<td>Not kinetic-rate imaging, not branch-local ATP reserve, and not cell-specific bioenergetic controller state</td>
</tr>
<tr>
<td><strong>Deuterium kinetic-rate imaging</strong><br>Li et al. (2025)</td>
<td>Model-conditioned macro deuterium kinetic-rate proxy</td>
<td>7 T dynamic DMRSI with blood-input, explicit kinetic model, very small cohort, and route-specific dose / timing burden</td>
<td>Bounded deuterium kinetic-rate proxy</td>
<td>Not one general biochemical meter, not branch-local ATP reserve, and not cell-specific bioenergetic controller state</td>
</tr>
<tr>
<td><strong>Human tract-scale transmission-speed estimation</strong><br>van Blooijs et al. (2023)</td>
<td>Tract-scale timing-support proxy</td>
<td>Development-sensitive transfer-time / tract-geometry human route rather than myelin-specific quantification or per-axon measurement</td>
<td>Bounded tract-scale timing-support proxy</td>
<td>Not a myelin-specific quantity, not node / internode microgeometry, and not a per-axon conduction controller readout</td>
</tr>
<tr>
<td><strong>Quantity-defined myelin MRI / tissue-health-sensitive ratio family</strong><br>Hagiwara et al. (2018); Baadsvik et al. (2024); Galbusera et al. (2025); Colaes et al. (2026)</td>
<td>Quantity-defined macro myelin proxy family plus a tissue-health-sensitive ratio route</td>
<td>Metric-dependent validity; bilayer mapping remains proof-of-principle, remyelination calibration remains special-case, and T1w/FLAIR may remain broader than myelin</td>
<td>Bounded myelin / timing-support or broader tissue-health family, depending on route</td>
<td>MT<sub>sat</sub>, SyMRI, T1w/T2w, qT1, bilayer, and T1w/FLAIR routes do not share one interchangeable claim ceiling, one common quantity, do not collapse into tract-speed estimation, and do not provide a per-axon timing readout</td>
</tr>
<tr>
<td><strong>Human clinical single-unit allocation route</strong><br>Tallman et al. (2025)</td>
<td>Local clinical-unit allocation-related proxy</td>
<td>Implanted-human hippocampal single-unit route in epilepsy patients; high-locality and pathology-conditioned</td>
<td>Bounded local human allocation-related calibrator</td>
<td>Not a whole-brain excitability meter, not direct AIS / channel-state readout, and not a route-free separation of pre-existing versus learning-induced excitability</td>
</tr>
<tr>
<td><strong>Human sleep-homeostasis / plasticity route</strong><br>Huber et al. (2013); Kuhn et al. (2016); Fehér et al. (2026)</td>
<td>Perturbation-conditioned maintenance proxy</td>
<td>Noninvasive human TMS-EEG / PAS route with sleep-history manipulation burden</td>
<td>Bounded excitability / plasticity-support proxy</td>
<td>Does not identify which cell class, synapse, AIS / channel change, or recovery controller produced the change</td>
</tr>
<tr>
<td><strong>Human state-gated perturbation route</strong><br>Zrenner et al. (2018); Khatri et al. (2025)</td>
<td>State-gated perturbation proxy</td>
<td>Closed-loop stimulation route with state-estimator and stimulation-timing burden</td>
<td>Bounded state-gated excitability / corticospinal proxy</td>
<td>Does not measure excitability mechanism itself, AIS geometry, channel distribution, or long-horizon recovery control</td>
</tr>
<tr>
<td><strong>Human BBB water-exchange MRI</strong><br>Morgan et al. (2024); Padrela et al. (2025)</td>
<td>Macro BBB water-exchange proxy</td>
<td>ASL method- and model-dependent route with healthy-adult / lifespan burden</td>
<td>Bounded BBB water-exchange proxy</td>
<td>Water-exchange estimates are not tracer-specific transport and do not read out pericyte / endothelial controller identity</td>
</tr>
<tr>
<td><strong>Tracer-specific BBB PET transport</strong><br>Chung et al. (2025)</td>
<td>Tracer-specific BBB transport proxy</td>
<td>High-temporal-resolution dynamic PET plus kinetic modeling across three radiotracers</td>
<td>Bounded tracer-specific BBB transport proxy</td>
<td>Named tracer PS estimate, not one generic BBB permeability scalar or local controller readout</td>
</tr>
<tr>
<td><strong>Human blood-CSF barrier / choroid-plexus perfusion / transport family</strong><br>Zhao et al. (2020); Sun et al. (2024); Petitclerc et al. (2021, 2026); Anderson et al. (2022); Wu et al. (2026)</td>
<td>Choroid-plexus perfusion, blood-to-CSF water transport, choroid-plexus water cycling, apparent BCSFB exchange, or joint BBB-versus-BCSFB ASL exchange</td>
<td>ASL / ultra-long-TE ASL / DCE-MRI / REXI route family with route-specific model burden, validation ceiling, and small-cohort dependence outside the HCP-Aging perfusion analysis</td>
<td>Bounded BCSFB / choroid-plexus support-state proxy family</td>
<td>Perfusion is not blood-to-CSF transport, water cycling is not apparent exchange, and none of these rows identify a generic BBB scalar, a generic clearance truth, or choroid-plexus epithelial controller identity</td>
</tr>
<tr>
<td><strong>Human MAO-B PET: SMBT-1 first-in-human target validation</strong><br>Villemagne et al. (2022)</td>
<td>Tracer-family-specific MAO-B target-validation proxy</td>
<td>Dynamic human PET with selegiline block and reversible-binding readout</td>
<td>Bounded MAO-B target-validation route</td>
<td>Shows that SMBT-1 can read a human MAO-B route, not that MAO-B disease contrast, quantification transfer, or generic astrocyte-state are solved</td>
</tr>
<tr>
<td><strong>Human MAO-B PET: SMBT-1 AD-spectrum contrast</strong><br>Villemagne et al. (2022)</td>
<td>Pathology-context MAO-B contrast proxy</td>
<td>AD-continuum cohort route with subcortical-white-matter reference and cross-sectional cognitive / amyloid / tau comparison</td>
<td>Bounded AD-spectrum astrocyte-related support-state proxy</td>
<td>Not a route-free MAO-B meter, not generalizable to all diseases, and not a local controller readout</td>
</tr>
<tr>
<td><strong>Human MAO-B PET: SMBT-1 quantification / biodistribution burden</strong><br>Hiraoka et al. (2025); Mesfin et al. (2026)</td>
<td>Tracer-family quantification and biodistribution route</td>
<td>Quantification depends on named scan-window / reference choice or arterial modeling, while whole-body biodistribution adds organ-distribution and late-gallbladder burden</td>
<td>Bounded SMBT-1 acquisition / quantification route</td>
<td>Not interchangeable with disease contrast, not one generic MAO-B number, and not proof that other tracer families or cohorts share the same ceiling</td>
</tr>
<tr>
<td><strong>Human MAO-B PET: SL25.1188 disease / severity route</strong><br>Matsuoka et al. (2026); Best et al. (2026)</td>
<td>Tracer-family-specific MAO-B disease / covariate proxy</td>
<td>AD quantification without arterial sampling and AUD severity / smoking-conditioned binding route under named tracer and model assumptions</td>
<td>Bounded SL25.1188 disease- and covariate-conditioned proxy</td>
<td>Not a generic MAO-B readout across diseases, not covariate-free, and not interchangeable with SMBT-1 results</td>
</tr>
<tr>
<td><strong>Human I<sub>2</sub>BS astrocyte-related PET</strong><br>Tyacke et al. (2018); Livingston et al. (2022)</td>
<td>I<sub>2</sub>BS target-defined astrocyte-related proxy</td>
<td>First-in-human idazoxan-blocked PET plus cognitively impaired cohort route with region- and stage-dependent behavior</td>
<td>Bounded I<sub>2</sub>BS astrocyte-related proxy</td>
<td>Different target class from MAO-B, not drop-in comparable with MAO-B tracer families, and not a generic astrocyte-state meter</td>
</tr>
<tr>
<td><strong>Human clearance-support route families</strong><br>Fultz et al. (2019); Kim, Huang, &amp; Liu (2025); Lim et al. (2025); Yoo et al. (2025); Eide et al. (2023); Hirschler et al. (2025); Dagum et al. (2026)</td>
<td>Macro support-state proxy family</td>
<td>Sleep-linked CSF oscillation, parenchyma-CSF water exchange, respiration-conditioned net flow, exercise-conditioned contrast influx / meningeal-lymphatic flow, intrathecal tracer / CSF-to-blood clearance, specialized CSF-mobility MRI, or device- and model-heavy overnight biomarker-efflux inference</td>
<td>Bounded clearance-support proxy family</td>
<td>These are different clearance-transport rows with different observables, intervention regimes, crossed boundaries, and model burdens, not a route-free glymphatic meter or direct readout of cell-specific immune control, responsible synapse, or local maintenance controller</td>
</tr>
</tbody>
</table>
<p>
However, the per-row axes are still not enough when several human rows are combined in one argument. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> derive the main 1H-MRSI route from <strong>adolescents</strong> with a separate <strong>15-35-year</strong> replication cohort, <a href="https://doi.org/10.1002/nbm.5256" target="_blank">Morgan et al. (2024)</a> and <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">Padrela et al. (2025)</a> keep BBB water-exchange claims inside ASL method choices and healthy-adult cohorts, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> report a <strong>7 T healthy-younger-adult</strong> CSF-mobility route, <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> study <strong>healthy older adults</strong> in a randomized sleep-deprivation crossover, <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">Villemagne et al. (2022)</a> remains a <strong>healthy-volunteer first-in-human</strong> SMBT-1 target-validation route, <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a> remains a <strong>pathology-context MAO-B</strong> astrocyte-related PET route across the AD continuum, <a href="https://doi.org/10.1007/s12149-025-02083-y" target="_blank">Hiraoka et al. (2025)</a> shows that the SMBT-1 route still depends on scan-window / reference-region versus kinetic-model choice, <a href="https://doi.org/10.1007/s12149-025-02144-2" target="_blank">Mesfin et al. (2026)</a> keeps whole-body biodistribution as a separate operational burden, <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">Matsuoka et al. (2026)</a> adds an arterial-free SL25.1188 AD quantification route, <a href="https://doi.org/10.1038/s41380-025-03355-9" target="_blank">Best et al. (2026)</a> shows that MAO-B binding can shift with AUD severity and daily cigarette use, <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">Livingston et al. (2022)</a> shows that the I<sub>2</sub>BS route changes with region and impairment stage, and <a href="https://doi.org/10.1111/bpa.70010" target="_blank">Galbusera et al. (2025)</a> constrains remyelination sensitivity in <strong>postmortem multiple-sclerosis cortex</strong> rather than a living-human longitudinal baseline. Those are not one matched human baseline by default. In parallel, <a href="https://doi.org/10.1371/journal.pone.0206583" target="_blank">Holiga et al. (2018)</a> showed that MRI repeatability ranges from <strong>poor to excellent</strong> depending on the metric, <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a> showed that cross-setup reproducibility has to be demonstrated rather than assumed, <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> showed that same-sample multimodal comparison in CONNECT-ME depended on <strong>n = 48</strong> patients with all features and improved sensitivity despite a <strong>markedly decreased sample size</strong>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> showed that the main French dataset itself was highly unbalanced across rows (<strong>EEG-LG 290</strong>, <strong>dMRI 151</strong>, <strong>aMRI 101</strong>, <strong>FDG-PET 53</strong>, <strong>fMRI-RS 44</strong>), with missing values substituted by <strong>-1</strong> while pairwise disagreements rose in <strong>MCS</strong> and <strong>improved</strong> patients. Therefore, on this page, bundle promotion now also requires two bundle-level gates: <strong>(4) cohort / physiological regime compatibility</strong> and <strong>(5) row robustness / availability disclosure</strong> after any within-family quantity / target / transport split has already been fixed.
</p>
<ul>
<li><strong>Cohort / physiological regime compatibility:</strong> name age band, health or pathology regime, and why transfer across cohorts is justified for the claimed latent variable.</li>
<li><strong>Row robustness / availability disclosure:</strong> name route-local repeatability, cross-centre or cross-scanner transfer window if claimed, the row-overlap geometry, and whether missingness tracks site, severity, tolerance, contraindication, protocol, or only a declared missing-row policy.</li>
</ul>
<p>
If several rows are combined in one argument, this roadmap now asks for <strong>same-subject / same-session / same-perturbation</strong> acquisition, <strong>cohort / regime compatibility</strong>, <strong>row-level repeatability or route-local reproducibility</strong>, <strong>availability / complete-case disclosure</strong>, <strong>external calibration</strong>, and a <a href="verification.html#human-proxy-composition-card">Human Proxy Composition Card</a> before talking about state-complete human measurement. If the bridge is sequential across live and ex vivo or across separated state regimes, it also asks for a <a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> plus the longer background rule in <a href="wiki/state-continuity-bridge.html">Wiki: State-Continuity Bridge</a>. Otherwise the result stays at <strong>proxy-rich but ceiling-limited human evidence</strong>, because proxy class, operational maturity, calibrator role, cohort compatibility, and robustness still remain mismatched. The front-door table is in <a href="wbe_101.html#human-observability-ladder">WBE 101: human observability ladder</a>, the longer critique is in <a href="wiki/human-proxy-composition.html">Wiki: Human Proxy Composition and Route Maturity</a>, and the submission-side stop rule is <a href="verification.html#observability-budget">Verification: Observability Budget</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: destructive ultrastructure is not a shortcut around the observability wall</strong>
<p>
It would still be too strong to read <strong>nanoscale</strong>, <strong>petascale</strong>, or <strong>same-brain EM</strong> as if the route had already preserved native state and solved scaling by itself. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that fixation route materially changes extracellular-space preservation and that even high-pressure freezing remains thickness-limited, <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> showed that human nanoscale reconstruction is still a rapidly preserved local surgical fragment, and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> showed that same-brain function plus EM is a sequential local pipeline rather than simultaneous whole-state capture. Therefore, this roadmap now separates <strong>preservation route</strong>, <strong>registration scope</strong>, and <strong>throughput / proofreading burden</strong> from resolution itself. On this page, destructive ultrastructure without those disclosures stays at <strong>structural scaffold</strong> or <strong>local ex vivo scaffold</strong>, not state-complete measurement.
</p>
</div>
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
<p><strong>2026-03-19 supplement:</strong>Subject boundary is not a philosophical garnish. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> and <a href="https://doi.org/10.1126/science.aav7893" target="_blank">Stringer et al. (2019)</a> showed that ongoing behavior is embedded in large fractions of cortical activity, <a href="https://doi.org/10.1038/nn.3567" target="_blank">Saleem et al. (2013)</a> and <a href="https://doi.org/10.1126/science.1232655" target="_blank">Ravassard et al. (2013)</a> showed that locomotion, optic flow, vestibular, and other sensory cues reshape cortical and hippocampal codes, <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">Zelano et al. (2016)</a> and <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">Raut et al. (2025)</a> showed that respiration and arousal couple brain dynamics to organism-wide physiology, and <a href="https://doi.org/10.1126/science.abd0380" target="_blank">Flesher et al. (2021)</a> showed that reintroducing tactile feedback improves a local bidirectional BCI. A slower boundary remains as well: <a href="https://doi.org/10.1038/29542" target="_blank">de Quervain et al. (1998)</a> and <a href="https://doi.org/10.1007/s11682-007-9003-2" target="_blank">Oei et al. (2007)</a> showed that glucocorticoid state changes retrieval and hippocampal / prefrontal retrieval activity, while <a href="https://doi.org/10.1016/j.celrep.2020.108255" target="_blank">McCauley et al. (2020)</a>, <a href="https://doi.org/10.1126/sciadv.adj1010" target="_blank">Barone et al. (2023)</a>, and <a href="https://doi.org/10.1073/pnas.2211996120" target="_blank">Birnie et al. (2023)</a> showed that circadian timing and corticosteroid rhythm alter hippocampal plasticity machinery. Therefore, M4 now treats <strong>body / environment boundary disclosure</strong> as a measurement requirement rather than as a later interpretation issue, and that disclosure includes both <strong>fast loop routes</strong> and <strong>slow internal-milieu routes</strong>.</p>
<p><strong>Decision rule:</strong>If a submission does not name which sensory, motor, interoceptive, and slow internal-milieu routes were preserved, substituted, matched, perturbed, or omitted, the result stays at <strong>local controller</strong>, <strong>task-specific subsystem loop</strong>, or <strong>brain-side-only proxy</strong> and does not advance to subject-complete L3 language.</p>
<p><strong>Next:</strong> Operatively place the "boundary of subject" in verification (V0) and publish a boundary card listing retained / substituted channels, slow internal-milieu routes, surrogate body / environment mapping, loop-removal tests, and residual omitted loops.</p>
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
<p><strong>2026-03-19 supplement:</strong> OPM-MEG adds movement tolerance, but not a free pass on measurement conditions. <a href="https://doi.org/10.1038/nature26147" target="_blank">Boto et al. (2018)</a> and <a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">Seymour et al. (2021)</a> showed motion-tolerant OP-MEG recordings, <a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">Holmes et al. (2023)</a> and <a href="https://doi.org/10.3390/s23125454" target="_blank">Holmes et al. (2023)</a> extended this to ambulatory movement and two-person hyperscanning by coupling field nulling to optical tracking, <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">Holmes et al. (2025)</a> showed that lighter shielded rooms become plausible only with tSSS plus active compensation, and <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">Rhodes et al. (2025)</a> showed that pseudo-MRI can help when MRI is difficult but still leaves individual MRI as the gold standard. Therefore, on this roadmap, OPM-MEG is read as <strong>movement-tolerant macro electrophysiology under disclosed magnetic-field control, sensor calibration, and anatomy route</strong>, not as shield-free naturalistic brain readout.</p>
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
<p><strong>Question:</strong>Even in the same individual, brain states vary across minutes, hours, days, and months. The operational question here is no longer simply “is the person stable?” but <strong>which part of the result reflects state fluctuation, trait-like backbone, biological drift, interface / decoder drift, or adaptive rescue</strong>.</p>
<p><strong>2026-03-22 addendum:</strong>The older wording here was too weak because it still allowed <strong>same-day success</strong>, <strong>cross-day persistence</strong>, and <strong>algorithmically rescued performance</strong> to sound like one continuous longitudinal achievement. The primary literature does not support that compression. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> showed that trial-to-trial cortical dynamics are strongly shaped by richly varied movements, <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a> showed that spontaneous behavior rapidly changes functional-connectivity structure, and <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> showed 10-hour EEG changes that materially alter decoding and motivate adaptive decoders. By contrast, <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a> and <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">Noda et al. (2025)</a> show that a <strong>population-level backbone</strong> can remain more stable than individual units. Finally, <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a>, <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> show why <strong>stabilized operation</strong> and <strong>fixed-decoder durability</strong> must be reported separately. Therefore, M7 now treats longitudinal evidence as a multi-field audit, not one score.</p>
<table class="data-table">
<thead>
<tr>
<th>Audit field</th>
<th>What must be named</th>
<th>What this stops you from overreading</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state annotation</strong></td>
<td>Arousal, spontaneous behavior, movement, task mode, time-of-day, sleep pressure, medication, or stimulation state.</td>
<td>A same-day or cross-day difference cannot be read as trait instability if the state itself was left unlogged.</td>
</tr>
<tr>
<td><strong>trait-like backbone</strong></td>
<td>The named backbone object that remained stable: for example latent dynamics or representational geometry.</td>
<td>Do not treat single-unit or single-channel volatility as if it automatically disproved a stable population backbone.</td>
</tr>
<tr>
<td><strong>biological drift</strong></td>
<td>Plasticity, remapping, unit turnover, recovery, or learning-related change in the living system.</td>
<td>Do not collapse organism-side change into interface or preprocessing failure.</td>
</tr>
<tr>
<td><strong>interface / decoder drift</strong></td>
<td>Electrode shift, channel loss, impedance change, feature-distribution shift, or decoder mismatch.</td>
<td>Do not say the biological representation collapsed when the unstable object was the interface or decoder.</td>
</tr>
<tr>
<td><strong>fixed decoder interval / recalibration burden</strong></td>
<td>How long the decoder was held unchanged, how often rescue or recalibration occurred, what data it used, and what happened when it failed.</td>
<td>Do not rephrase adaptive rescue as if the original decoder had remained valid on its own.</td>
</tr>
</tbody>
</table>
<p><strong>Decision rule:</strong>If a result does not report <strong>state annotation</strong>, <strong>fixed decoder interval</strong>, and <strong>recalibration burden</strong> separately, this roadmap stops at <strong>state-conditioned performance</strong> or <strong>participant-specific stabilized operation</strong>. It does not promote the result to trait stability, durable fixed-decoder use, or long-horizon deployability.</p>
<p><strong>Next:</strong>Bundle <a href="verification.html#temporal-validity-card">Verification: Temporal Validity Card</a> with <a href="wiki/state-trait-and-drift.html">Wiki: State, Trait, and Drift</a>. If the evidence also bridges across acquisition regimes or days as if it were one latent state, add the <a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> rather than relying on same-subject wording alone.</p>
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
<p><strong>2026-03-19 literature audit:</strong>The older wording here was too weak because it made <strong>structure</strong>, <strong>state</strong>, and <strong>plasticity</strong> sound like three clean knobs. The primary literature does not support that simplification. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> showed that transcriptomic type still leaves morpho-electric spread within a cell class. <a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a>, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a>, <a href="https://doi.org/10.1038/nature13028" target="_blank">Yang et al. (2014)</a>, and <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a> show that long-term stabilization depends on synapse- and branch-specific tagging, clustered spine stabilization, and proteostatic maintenance rather than on graph structure alone. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuron.2017.06.025" target="_blank">Latchoumane et al. (2017)</a>, and <a href="https://doi.org/10.1038/s41586-025-09774-6" target="_blank">Terceros et al. (2026)</a> show that multi-day retention also depends on sleep / homeostatic / transcriptional programs. <a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a>, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a>, <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a>, <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a>, and <a href="https://doi.org/10.1126/science.1072699" target="_blank">Pizzorusso et al. (2002)</a> show that myelin / perinodal state, glial metabolic support, and extracellular-matrix state can change timing, plasticity, and memory expression without rewiring. Therefore, this roadmap no longer treats <code>structure + state</code> as one dial.</p>
<p><strong>Revised branching:</strong>(A) structural scaffold only / (B) structural scaffold + fast executable state / (C) structural scaffold + fast executable state + maintenance / plasticity state</p>

<table class="data-table">
<thead>
<tr>
<th>Layer inside the restoration target</th>
<th>What has to be named explicitly</th>
<th>What fails if it is omitted</th>
<th>Claim ceiling if still omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Structural scaffold</strong></td>
<td>Cell identity, gross morphology, connection graph, major axonal routing constraints</td>
<td>Local routing, lesion/perturbation path constraints, and circuit-level intervention matching have no substrate to run on</td>
<td><strong>Structural prior only</strong>, not an executable person model</td>
</tr>
<tr>
<td><strong>Fast executable state</strong></td>
<td>Momentary activity state, effective synaptic efficacy, intrinsic excitability / operating point, and current neuromodulatory regime (<a href="#qa-r10">R10</a>)</td>
<td>The same scaffold can express different immediate trajectories and intervention responses</td>
<td><strong>Structure-conditioned simulator</strong> or same-session proxy, not a demonstrated state match</td>
</tr>
<tr>
<td><strong>Maintenance / eligibility state</strong></td>
<td>Synaptic tags and capture conditions, local proteostatic support, sleep/replay coupling, transcriptional stabilization, myelin / perinodal state, glial metabolic support, ECM / PNN state</td>
<td>Learning persistence, day-to-day retention, timing stability, and recovery after perturbation become underdetermined</td>
<td><strong>Short-window replay only</strong>; no claim here about stable multiday learning or continuity</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Restoration-target card required</strong>
<p>
Every R0 claim on this site must publish a small card that states <strong>(1) which state families were directly measured</strong>, <strong>(2) which were only externally calibrated or model-estimated</strong>, <strong>(3) which were omitted</strong>, <strong>(4) which timescale each family is supposed to cover</strong> (milliseconds / seconds / hours / days / weeks), and <strong>(5) what claim ceiling and abstention boundary follow from those omissions</strong>. Without that card, same-session fit and multiday continuity collapse into one vague success label, which this roadmap no longer allows.
</p>
</div>

<p><strong>Failure condition:</strong>If the chosen restoration target cannot reproduce intervention response at the declared timescale, or if the conclusion changes once omitted maintenance-state families are reintroduced, the target fails. A model that fits same-session data while hiding multiday maintenance burdens is not accepted here as a general restore target.</p>
<p><strong>Next:</strong>Evaluate identifiability (R7) and computability (I3) simultaneously, but only after publishing the restoration-target card with omitted state families, audited timescales, and claim ceiling. For supporting background, use <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams are not enough</a> and <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>.</p>
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
<p><strong>Policy:</strong> In this project, no specific solver is fixed as the standard solution. Acceptance requires (1) an explicit uncertainty expression such as a posterior distribution, confidence interval, or bootstrap / ensemble range, (2) sensitivity analysis for individual MRI, FEM / BEM, conductivity assumptions, and electrode geometry, (3) external validation using simulation, phantoms, simultaneous invasive recording, or intracranial stimulation, and now also (4) a named <strong>source regime / target object</strong>, <strong>uncertainty object</strong>, and <strong>validation board / operating regime</strong>. Bayesian or empirical-Bayes approaches are good candidates, but auditability matters more than the method name. </p>
<p><strong>2026-03-31 addendum:</strong>The remaining weakness in this roadmap was to let <strong>inverse-family progress</strong> sound closer than it is to one shared truth scale. The current primary literature does not support that shortcut. <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a> sample posterior support for <strong>focal-source hypotheses</strong>, <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025)</a> target <strong>sparse spatial-temporal source imaging</strong> with debiased estimation and inference, and <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> target <strong>extended-source extent</strong> with empirical-Bayesian uncertainty maps. Upstream uncertainty remains separate: <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> showed that tissue-conductivity uncertainty materially shifts EEG source analysis, and <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026)</a> showed that conductivity estimation can reduce source-localization uncertainty in many presurgical epilepsy scenarios without erasing all depth / location exceptions. Therefore, this roadmap no longer reads <strong>new inverse family</strong> as one generic upgrade. It asks what object is being estimated, which uncertainty object is returned, and which physics and validation regime remain attached.</p>
<table class="data-table">
<thead>
<tr>
<th>R1 inverse-audit field</th>
<th>What this roadmap now asks for</th>
<th>Why it matters</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Source regime / target object</strong></td>
<td>Name whether the paper is estimating focal support, a sparse spatial-temporal source set, extended-source extent, or another declared object.</td>
<td>Different inverse families are not automatically estimating the same scientific target.</td>
</tr>
<tr>
<td><strong>Uncertainty object</strong></td>
<td>Name whether the method returns posterior support, debiased intervals / tests, extent-overlap maps, or only location spread.</td>
<td>Uncertainty is not one scalar if the returned object changes with the inverse family.</td>
</tr>
<tr>
<td><strong>Forward-model uncertainty route</strong></td>
<td>State whether conductivity, head-model, and electrode-geometry uncertainty were propagated, fixed, or calibrated.</td>
<td>A sharper posterior does not erase uncertainty that still sits upstream in the physics.</td>
</tr>
<tr>
<td><strong>Validation board / operating regime</strong></td>
<td>Name whether the evidence comes from simulation, phantom, DBS / stimulation ground truth, simultaneous invasive recording, or another board.</td>
<td>Success on one board does not automatically transfer to all source classes and clinical / experimental regimes.</td>
</tr>
</tbody>
</table>
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
<p><strong>2026-03-31 addendum:</strong>The older wording still made <strong>better source imaging</strong> sound too much like one shared representation goal. The current primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">Pascarella et al. (2023)</a> compare focal-source validation routes, <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> show depth- and skull-conductivity-dependent localization error across <strong>3,619 stimulation locations</strong> in <strong>11 patients</strong>, and <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> show simultaneous <strong>HD-EEG / SEEG</strong> concordance in a drug-resistant-epilepsy operating regime. Those boards do not yet define one universal scoreboard for focal, sparse, extended, and spontaneous sources. Therefore, R2 now asks the restoration target to say whether it wants <strong>focal support</strong>, <strong>sparse spatial-temporal source activity</strong>, <strong>extended-source extent</strong>, or another declared object before methods are compared.</p>
<table class="data-table">
<thead>
<tr>
<th>R2 representation family</th>
<th>What it can return relatively directly</th>
<th>What this roadmap still refuses to infer automatically</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Probabilistic focal-source family</strong></td>
<td>Posterior support and alternative configurations for a small-number focal-source hypothesis.</td>
<td>It is not promoted automatically to sparse spatial-temporal inference or extended-source extent recovery.</td>
</tr>
<tr>
<td><strong>Sparse spatial-temporal family</strong></td>
<td>Bias-corrected amplitudes, orientations, depths, and inference for sparse source sets over time.</td>
<td>It is not promoted automatically to focal-board optimum across all priors or to extended-source validation.</td>
</tr>
<tr>
<td><strong>Extended-source family</strong></td>
<td>Estimated location-plus-extent with uncertainty for spatially extended activation.</td>
<td>It is not promoted automatically to focal-source best case or to a universal benchmark win across source regimes.</td>
</tr>
</tbody>
</table>
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
<p><strong>2026-03-25 addendum:</strong>The remaining weakness in this roadmap was that <strong>latent state</strong> still sounded too close to one compressed hidden variable. The rest of this site no longer supports that shortcut. <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">Lee et al. (2003)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.0248-16.2016" target="_blank">Havekes et al. (2016)</a>, <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">Vierra et al. (2023)</a>, and <a href="https://doi.org/10.1016/j.biopsych.2023.12.020" target="_blank">Altas et al. (2024)</a> show that <strong>phospho-signaling / second-messenger routing</strong> can change plasticity expression without collapsing to transcript or bulk protein abundance. <a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a>, <a href="https://doi.org/10.1038/ncomms2250" target="_blank">Shires et al. (2012)</a>, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a>, <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a>, and <a href="https://doi.org/10.1073/pnas.2315958121" target="_blank">Chang et al. (2024)</a> show that <strong>local proteostasis / tag-capture route</strong> is another state family with its own integrative unit and turnover window. <a href="https://doi.org/10.1038/nn2063" target="_blank">Correia et al. (2008)</a>, <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">Swarnkar et al. (2021)</a>, <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">Aiken &amp; Holzbaur (2024)</a>, and <a href="https://doi.org/10.1038/s41467-025-57651-7" target="_blank">de Queiroz et al. (2025)</a> show that <strong>cargo-transport / cytoskeletal trafficking state</strong> is again a different route: what reaches the relevant spine, branch, bouton, or axon terminal can change plasticity and memory while the graph stays fixed. Therefore, on this page, a latent-state model is no longer accepted as a single unqualified object. It must say <strong>which family it is trying to recover</strong>, <strong>which family remained omitted</strong>, and <strong>what timescale the claimed state is supposed to govern</strong>.</p>
<table class="data-table">
<thead>
<tr>
<th>Latent-state family</th>
<th>What it constrains relatively directly</th>
<th>What still stays latent if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fast executable state</strong></td>
<td>Immediate activity trajectory, momentary effective synaptic efficacy, and same-session intervention response.</td>
<td>Why the same scaffold later stabilizes, forgets, or recovers differently across hours to days.</td>
</tr>
<tr>
<td><strong>Phospho-signaling / second-messenger route</strong></td>
<td>Compartment-specific gating, phosphosite occupancy logic, kinase/phosphatase balance, and local signaling nanodomains that modulate plasticity expression.</td>
<td>A model can fit next-step activity while still missing the controller that decides which plastic change is permitted, blocked, or redirected.</td>
</tr>
<tr>
<td><strong>Local proteostasis / tag-capture route</strong></td>
<td>Which tagged synapse or branch captures plasticity-related proteins, and which late changes survive local turnover.</td>
<td>Late stabilization, reconsolidation, and persistence remain underdetermined even if fast-state prediction improves.</td>
</tr>
<tr>
<td><strong>Cargo-transport / cytoskeletal trafficking route</strong></td>
<td>Which receptors, endosomes, RNA cargoes, and presynaptic components actually reach the required compartment in time.</td>
<td>Compartment-specific maintenance and structural plasticity remain latent even when transcript abundance, ATP support, or weight estimates look adequate.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>State-family card required for maintenance-relevant R3 claims</strong>
<p>
If an R3 claim is used to support <strong>persistence</strong>, <strong>reconsolidation</strong>, <strong>remote memory</strong>, <strong>recovery after perturbation</strong>, or <strong>same-state language across days or acquisition regimes</strong>, the submission must publish at least <strong>(1) family name</strong>, <strong>(2) direct observable or perturbation route</strong>, <strong>(3) dominant timescale</strong>, <strong>(4) integrative unit</strong> (synapse / branch / neuron / region / whole-brain proxy), <strong>(5) whether that family was directly measured, externally calibrated, model-estimated, or omitted</strong>, and <strong>(6) the abstention boundary that follows</strong>. If regimes or days are bridged, attach the <a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a>; if persistence or forgetting is part of the claim, attach the <a href="verification.html#maintenance-state-error-budget">Maintenance-State Error Budget</a>. Without that bundle, this roadmap treats the result as a <strong>prediction-useful latent variable</strong> or <strong>same-session proxy model</strong>, not as a maintenance-complete state estimate.
</p>
</div>
<p><strong>False condition:</strong>The latent state only serves to compress data, fails on held-out perturbations, or changes interpretation once omitted maintenance families such as phospho-signaling, local proteostasis, or cargo-routing are reintroduced.</p>
<p><strong>Next:</strong>Compare connectome-only, fast-state, and maintenance-augmented models on the same held-out perturbation and longitudinal benchmarks, then publish the omitted-family list and the resulting claim ceiling.</p>
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
<p><strong>Effective-connectivity route card required:</strong>Any R4 claim using DCM or a related effective-connectivity estimator must publish (1) compared node set plus omitted competitors, (2) observed-subsystem closure / latent-confound audit, (3) node-definition / parcellation policy, (4) neural-mass / HRF / prior assumptions plus sampling / transformation sensitivity, (5) family comparison and model recovery, (6) held-out perturbation or external validation, (7) test-retest window and condition dependence, and (8) abstention boundary. If those are missing, this roadmap stops at <strong>model-conditioned causal hypothesis</strong> and does not promote the result to discovered causal wiring or WBE-relevant causal structure.</p>
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
<p><strong>2026-03-25 addendum:</strong>The remaining weakness here was that <strong>plasticity</strong> still read too much like a yes/no switch: either learning is introduced or it is not. The primary literature does not support that simplification. <a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a> and <a href="https://doi.org/10.1038/ncomms2250" target="_blank">Shires et al. (2012)</a> show <strong>tag / capture eligibility</strong>, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a> shows <strong>branch-level integration</strong>, <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">Fonseca et al. (2006)</a>, <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a>, <a href="https://doi.org/10.1073/pnas.2315958121" target="_blank">Chang et al. (2024)</a>, and <a href="https://doi.org/10.1111/acel.14492" target="_blank">Parker et al. (2025)</a> show distinct <strong>synthesis-degradation / autophagy / proteasome-capacity routes</strong>, and <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">Lee et al. (2003)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.0248-16.2016" target="_blank">Havekes et al. (2016)</a>, <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">Vierra et al. (2023)</a>, and <a href="https://doi.org/10.1523/JNEUROSCI.1619-24.2025" target="_blank">Rodriguez et al. (2025)</a> show that phospho-state can be a gate rather than a stable weight itself. In parallel, <a href="https://doi.org/10.1038/nn2063" target="_blank">Correia et al. (2008)</a>, <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">Aiken &amp; Holzbaur (2024)</a>, and <a href="https://doi.org/10.1038/s41467-025-57651-7" target="_blank">de Queiroz et al. (2025)</a> show that delivery routes and local RNA localization constrain what plasticity can actually be expressed. Therefore, R5 is no longer treated here as a yes/no choice. It is a <strong>claim-timescale audit</strong>.</p>
<table class="data-table">
<thead>
<tr>
<th>Route</th>
<th>What it permits relatively safely</th>
<th>Minimum deliverables</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>(A) fixed model / no plasticity claim</strong></td>
<td>Same-session fit, bounded closed-loop control, or a narrow intervention result without persistence claims.</td>
<td>Fixed decoder horizon, same-session hold-out, abstention on forgetting / reconsolidation / recovery, and an explicit statement that no maintenance-complete claim is being made.</td>
</tr>
<tr>
<td><strong>(B) fixed fast-state model + maintenance disclosure</strong></td>
<td>Cross-day or cross-regime comparison without claiming that the controller of persistence has been identified.</td>
<td><a href="verification.html#temporal-validity-card">Temporal Validity Card</a>, state annotation, <a href="verification.html#maintenance-state-error-budget">Maintenance-State Error Budget</a>, fixed-decoder versus rescue-mode separation, and the relevant family route cards when phospho, proteostasis, cargo, or other maintenance controllers are cited.</td>
</tr>
<tr>
<td><strong>(C) explicit plasticity / maintenance model</strong></td>
<td>Named persistence, reconsolidation, recovery, or remote-memory claims with a declared controller family.</td>
<td>Named plasticity rule, family-level ablations, held-out perturbation prediction, fixed-decoder durability plus recalibration burden, <a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> when acquisition regimes are bridged, and a failure / fallback policy if the controller assumptions break.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Site rule for plasticity claims</strong>
<p>
On this site, the words <strong>plasticity</strong>, <strong>adaptation</strong>, <strong>consolidation</strong>, <strong>recovery</strong>, and <strong>long-term stabilization</strong> are not treated as one achievement. If the claim reaches beyond same-session fit, attach the <a href="verification.html#temporal-validity-card">Temporal Validity Card</a>. If it bridges across acquisition regimes or days as if it were one state sample, attach the <a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a>. If the claim depends on maintenance families, attach the <a href="verification.html#maintenance-state-error-budget">Maintenance-State Error Budget</a> plus the relevant family route cards for phospho-signaling, local proteostasis, cargo-routing, or other cited controllers. Without that bundle, R5 stops at an <strong>adaptive or learning-capable model</strong>, not a verified continuity-preserving plasticity route.
</p>
</div>
<p><strong>Next required:</strong>When learning is included, report fixed-decoder durability, rescue mode, recalibration burden, family-level ablations, and held-out perturbation response on the same benchmark; then disclose which timescale of plastic claim was actually passed.</p>
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
<p><strong>Next, we need:</strong>In addition to prior distribution/regularization, we publish all of the <strong>compared and excluded families</strong>, <strong>sensitivity analysis of electrode geometry, head model, and conductivity</strong>, <strong>simulation/phantom/invasive calibration</strong>, and <strong>abstention conditions when models overlap</strong>, and only adopt robust conclusions. The submission-side rule for this node is <a href="verification.html#identifiability-card">Verification: Identifiability Card</a>. </p>
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
<div class="note-box">
<strong>2026-03-26 supplement: richer observables are not the same as a collapsed solution set</strong>
<p>
The remaining weak point here was that <strong>more measured variables</strong> could still sound too close to <strong>unique recovery</strong>. <a href="https://doi.org/10.1155/2019/8497093" target="_blank">Villaverde (2019)</a> reviewed that observability and structural identifiability are different questions, and <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde et al. (2019)</a> showed that unknown inputs, states, and parameters often have to be analysed jointly. In neuroscience, <a href="https://doi.org/10.1038/nn1352" target="_blank">Prinz et al. (2004)</a> showed that similar circuit activity can arise from disparate parameters, <a href="https://doi.org/10.1162/netn_a_00354" target="_blank">Rasero et al. (2024)</a> showed that similar human activation patterns can still hide different macroscopic network states, and <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that connectome-constrained dynamics remain degenerate until additional recordings are supplied. A second weakness remained after that: <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed both <strong>common and divergent</strong> organization across simultaneous Ca<sup>2+</sup> and BOLD, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed tightly coupled global progression plus <strong>two distinct network patterns</strong> in simultaneous EEG-PET-MRI, and <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a>, <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> show why same-brain or same-subject sequential pipelines still remain exposed to preservation change and state drift. Therefore, this roadmap now treats R7 as a five-step audit: <strong>(1) observability budget</strong>, <strong>(2) structural identifiability in the declared model space</strong>, <strong>(3) practical identifiability under the actual dataset and perturbation design</strong>, <strong>(4) bridge / composition validity when multimodal or sequential evidence is invoked</strong>, and <strong>(5) external validation plus abstention when candidate sets still overlap</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Ambiguity class</th>
<th>How it fools the reader</th>
<th>What would actually raise the claim ceiling</th>
<th>What this roadmap still refuses to count</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Symmetry / reparameterization ambiguity</strong></td>
<td>Several parameter or state transformations still produce the same declared outputs, so a good fit looks unique when it is not.</td>
<td>Add a symmetry-breaking observable, known input / initial condition, or an explicit reformulation that removes the hidden transformation.</td>
<td>More optimizer restarts, longer fitting, or more repeats of the same uninformative protocol.</td>
</tr>
<tr>
<td><strong>Regime-restricted degeneracy</strong></td>
<td>Different internal states or parameter sets agree inside one narrow task, state, or operating regime and only diverge outside it.</td>
<td>Use state transitions, persistent excitation, targeted recordings, or perturbation contrasts that make the surviving alternatives separate.</td>
<td>More passive samples from the same narrow regime when the alternatives remain co-linear.</td>
</tr>
<tr>
<td><strong>Model-family / omitted-mechanism ambiguity</strong></td>
<td>An approximate family looks well identified until a complementary condition reveals systematic residuals or missing mechanisms.</td>
<td>Run a discrepancy stress test, compare richer / alternative model families, and require held-out falsification instead of post hoc explanation.</td>
<td>Narrower intervals inside one misspecified family or one headline fit improvement.</td>
</tr>
<tr>
<td><strong>Task-variable interaction / representation ambiguity</strong></td>
<td>A reduced representation predicts correlations while missing the interaction structure that actually drives behavior.</td>
<td>Preserve or perturb the task-variable interaction and compare intervention-side predictions of the competing representations.</td>
<td>Correlation-only dimensionality reduction, generic multimodal fusion, or interpretability language without perturbation.</td>
</tr>
</tbody>
</table>
<table class="data-table">
<thead>
<tr>
<th>Evidence pattern</th>
<th>What it can improve</th>
<th>What it still does not close</th>
<th>Required next audit on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Same-session multimodal bundle</strong></td>
<td>Can tighten observability and expose complementary errors</td>
<td>Does not by itself remove shared-driver risk, quantity mismatch, or latent-state multiplicity</td>
<td><a href="verification.html#fusion-card">Fusion Card</a> plus the R7 candidate-space audit</td>
</tr>
<tr>
<td><strong>Connectome-constrained predictor</strong></td>
<td>Can restrict one family of candidate dynamics</td>
<td>Does not by itself remove dynamical degeneracy or omitted-state families</td>
<td><a href="verification.html#observability-budget">Observability Budget (Connectome-Constrained Model Card)</a> plus held-out recordings / perturbations</td>
</tr>
<tr>
<td><strong>Same-brain or same-subject sequential pipeline</strong></td>
<td>Can connect specimen identity across stages</td>
<td>Does not by itself guarantee same-state continuity across fixation, delay, or regime shift</td>
<td><a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> plus temporal-validity disclosure</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-31 supplement: informative protocols must target ambiguity, stress omitted mechanisms, and declare minimum sufficiency</strong>
<p>
The remaining weakness after splitting observability from identifiability was that a protocol could still be described with generic words such as <strong>multimodal</strong>, <strong>naturalistic</strong>, or <strong>closed-loop</strong> without saying why that design should actually separate the survivors. The primary literature does not support that shortcut. <a href="https://doi.org/10.1109/CDC.1991.261405" target="_blank">Diop &amp; Fliess (1991)</a> made persistent trajectories explicit, and <a href="https://doi.org/10.1063/1.3528102" target="_blank">Raue et al. (2010)</a> showed that identifiability analysis can guide new experiments rather than only criticize old ones. <a href="https://doi.org/10.1016/j.mbs.2016.10.009" target="_blank">Chis et al. (2016)</a> then showed that <strong>sloppiness is not identifiability</strong> and that design should optimize explicit identifiability criteria rather than proxy uncertainty scores. <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">White et al. (2016)</a> showed that complementary experiments can expose <strong>omitted mechanisms</strong> rather than solve them. In current neuroscience, <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that a <strong>small targeted recording set</strong> can remove degeneracy in connectome-constrained networks, and <a href="https://doi.org/10.1038/s41593-025-01869-7" target="_blank">Langdon &amp; Engel (2025)</a> showed that preserving <strong>causal interactions among task variables</strong> can recover behaviorally relevant computation that correlation-only reductions miss. <a href="https://doi.org/10.1038/s41540-023-00325-1" target="_blank">Gevertz &amp; Kareva (2024)</a> then showed that identifiability analysis can derive a <strong>minimally sufficient</strong> schedule, and <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">Liu et al. (2025)</a> showed that active learning can reduce the observations needed to reach practical identifiability. Therefore, this roadmap now asks not only whether a protocol is richer, but <strong>which ambiguity it targeted</strong>, <strong>which identifiability objective chose it</strong>, <strong>whether it exposed omitted-mechanism error</strong>, and <strong>what minimum-sufficiency stop rule would have been enough</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Design-side audit field</th>
<th>What R7 now asks for</th>
<th>What this stops you from overreading</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Named ambiguity</strong></td>
<td>State which surviving states, parameters, controllers, or model families remain confusable after the current fit, and which one the next protocol step is trying to separate.</td>
<td><code>We added another task or modality</code> is not read as targeted ambiguity reduction.</td>
</tr>
<tr>
<td><strong>Identifiability objective</strong></td>
<td>Name whether the next condition was chosen to optimize practical identifiability, model discrimination, posterior contraction, profile-likelihood width, or another declared criterion.</td>
<td>A richer protocol is not read as informative merely because a generic optimization score improved.</td>
</tr>
<tr>
<td><strong>Orthogonal regime / targeted recording leverage</strong></td>
<td>Disclose the stimulus range, state transitions, perturbation timing, or targeted recording subset that should rotate the surviving candidates apart rather than merely resample one narrow regime.</td>
<td>More samples from the same operating slice are not read as collapsed degeneracy.</td>
</tr>
<tr>
<td><strong>Model-discrepancy stress</strong></td>
<td>Report whether the new condition exposed systematic residuals, failed fits, or omitted mechanisms, and what hierarchy of richer or alternative models was checked afterwards.</td>
<td>Tighter nominal uncertainty is not read as trustworthy when the design only forced hidden model error into view.</td>
</tr>
<tr>
<td><strong>Minimum-sufficiency stop rule</strong></td>
<td>Predefine the smallest condition / time-point / recording set required to raise the claim, the uncertainty or overlap threshold used to stop, and how much candidate overlap remained once that minimum design was reached.</td>
<td>Open-ended data accumulation is not read as solved identifiability if the stopping logic was never declared.</td>
</tr>
</tbody>
</table>
<p><strong>Operational link:</strong> When this design-side disclosure is missing, this roadmap stops at <strong>predictive fit</strong>, <strong>localized source hypothesis</strong>, or <strong>model-conditioned mechanism</strong>. The submission-side operational version remains <a href="verification.html#experiment-design-leverage">Verification: experiment-design leverage</a>.</p>
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
<p><strong>Question:</strong>Synaptic connections alone cannot reproduce state-dependent regulation of dopamine, serotonin, acetylcholine, and related volume-transmission systems. The weak point here was that this node still let <strong>pupil / HRV</strong>, <strong>local transmitter imaging</strong>, <strong>receptor maps</strong>, <strong>occupancy PET target engagement</strong>, and <strong>displacement / release-sensitive PET</strong> sound more interchangeable than they are. That was too weak. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> showed that pupil fluctuations track both adrenergic and cholinergic activity, <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> showed that local cortical ACh depends on axon activity and local clearance, <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> and <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">Goulas et al. (2021)</a> showed that receptor maps are structured regional priors, <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> showed ligand- and dose-limited D<sub>2</sub> target engagement under administered lurasidone, and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, plus <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> showed challenge- and time-window-limited dopamine or serotonin release proxies rather than a free readout of the whole transmitter field. </p>
<p><strong>Operational rule:</strong>On this site, neuromodulation is not treated as a <code>single mood scalar</code>. It is a ladder with at least five non-equivalent rungs. <strong>(1) mixed arousal proxy</strong> such as pupil / HRV / locomotion is a coarse covariate only. <strong>(2) local axon or transmitter sensor</strong> calibrates a measured region's chemical signal but not the whole brain. <strong>(3) receptor / transporter atlas</strong> is a regional chemoarchitectural prior, not the current state. <strong>(4) occupancy PET</strong> is ligand-, receptor-family-, dose-, and window-limited target engagement under an administered drug. <strong>(5) displacement / release-sensitive PET</strong> is a challenge-, ligand-, receptor-family-, and time-window-limited endogenous release proxy. None of these rungs alone is accepted here as the ground truth of the current whole-brain neuromodulatory state. </p>
<p><strong>Next:</strong>When an R10 claim is made, publish <strong>which rung was used</strong>, plus receptor family, ligand / challenge, dose when applicable, temporal window, spatial scope, and abstention boundary. Then compare the same baseline with and without that rung under the same held-out state transition. For the stack-level ceiling, see <a href="wiki/measurement-stack-and-claim-ceiling.html#neuromodulatory-proxy-ladder">Wiki: neuromodulatory proxy ladder</a>; for the broader hidden-state argument, see <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams alone are not enough</a>. </p>
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
<p><strong>Redefinition (2026-03):</strong> Instead of a single number, audit acceptable delays for at least <strong>(a) state feedback / neurofeedback</strong>, <strong>(b) ERP / command BCI</strong>, <strong>(c) phase-locked stimulation</strong>, and <strong>(d) burst/state-triggered neuromodulation</strong>. Phase-targeting now focuses first on <strong>oscillation estimability</strong> and then on <strong>phase error</strong>, <strong>causal-versus-post-hoc benchmark</strong>, <strong>circular precision</strong>, <strong>functional comparator</strong>, and <strong>fixed-versus-adaptive phase policy</strong>. Adaptive DBS focuses on biomarker burst detection delay and stopping rules. </p>
<p><strong>Supplement (Issue #46):</strong> We actually measure the <strong>end-to-end delay and jitter</strong> using CLET, photodiode, loopback, and TTL, and position LSL's time_correction as software offset correction. This is not to say that LSL alone guarantees actuation onset. </p>
<p><strong>Next:</strong> On the evaluation suite (V1) side, leave the loop class explicit, median/P95/P99/worst-case latency, number of abstentions/freezes/stops, and performance degradation curve for additional delay. For phase-targeted loops specifically, also leave the target band / spatial filter, power-SNR gate, no-stim rate, causal-versus-post-hoc benchmark, mean phase offset plus circular spread, off-target or random-phase comparator, and fixed-versus-adaptive phase policy. For information on organizing entrances, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed-loop, delay, jitter, and safety stops</a>. </p>
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
<p><strong>Stricter policy:</strong>The word “embodiment” is too cheap if it only means that some output device existed. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">Flesher et al. (2021)</a> showed that tactile feedback improves robotic-arm control, but this is evidence for a <strong>local surrogate sensorimotor loop</strong>, not that whole-body coupling is solved. Combined with <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a>, <a href="https://doi.org/10.1126/science.aav7893" target="_blank">Stringer et al. (2019)</a>, <a href="https://doi.org/10.1038/nn.3567" target="_blank">Saleem et al. (2013)</a>, <a href="https://doi.org/10.1126/science.1232655" target="_blank">Ravassard et al. (2013)</a>, and <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">Zelano et al. (2016)</a>, this means I6 must disclose which body / environment loops were present rather than talking about embodiment as a yes/no label.</p>
<ul>
<li><strong>Declare retained / substituted channels:</strong> vision, touch, proprioception, vestibular cues, respiration / arousal routes, dialogue partner, and task-state cues.</li>
<li><strong>Describe the surrogate plant:</strong> robotic hand, cursor, speech synthesizer, virtual avatar, or other actuator, together with latency, noise, and saturation.</li>
<li><strong>Run removal tests:</strong> feedback-off, sensory-substitution-off, altered environment, or loop perturbation conditions that show what really carries the performance.</li>
</ul>
<p><strong>Next:</strong> Fix the environment (VR/game/dialogue) and design an evaluation that can be repeated under the same conditions, then publish a body / environment boundary card plus ablation plan.</p>
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
<p><strong>2026-03 Literature Audit:</strong>Bérut et al. (2012) demonstrated a logically irreversible minimum dissipation lower bound for bit erasure, not wall-power or NESS reproduction conditions for the entire digital brain. What Lynn et al. (2021), de la Fuente et al. (2023), and Nartallo-Kaluarachchi et al. (2025) demonstrate is the usefulness of measuring broken detailed balance and time irreversibility from coarse-grained time series such as fMRI/ECoG/MEG, and is not an acceptance condition for microscopic physical dissipation or identity. Ishihara & Shimazaki (2025) also show that entropy flow estimation is a model-based quantity that requires assumptions such as state-space kinetic ising model, pairwise coupling, and mean-field approximation. A second correction is that the observed trajectory is not automatically thermodynamically closed. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">Martínez et al. (2019)</a> showed that waiting-time asymmetry can reveal hidden dissipation even when observable current vanishes, <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">Hartich &amp; Godec (2024)</a> showed that this interpretation can fail when coarse-graining and time reversal do not commute, <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">Martínez et al. (2024)</a> replied by limiting the original claim to local-in-time coarse-grainings and, where needed, second-order semi-Markov constructions, and <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">Blom et al. (2024)</a> showed that coarse lumping can hide dissipative cycles and induce memory so that estimates become far too small when the observed trajectory is naively treated as Markov. </p>
<div class="key-points">
<h4>Treatment to be fixed on this page</h4>
<ul>
<li><strong>Do not make it a required gate:</strong>Maintaining EPR > 0, <code>Virtual Dissipation Protocol</code>, biological brain 20W matching, and communication: calculation ratio matching are not set as acceptance conditions at this time. </li>
<li><strong>Treat as supplementary logs: </strong>Wall-plug power, FLOPs, time irreversibility, and model-based entropy flow are recorded separately. </li>
<li><strong>Explicit modality dependence:</strong>Since the estimators have different meanings for fMRI / MEG / ECoG / spike train, they are not directly substituted for each other. </li>
<li><strong>Name estimator family and null control:</strong>Transition-flux lower bounds, time-shifted correlation asymmetry, inversion classifiers, visibility-graph indices, and state-space kinetic Ising entropy flow are not interchangeable, and shuffle / surrogate controls are part of the claim. </li>
<li><strong>Audit observed-state closure and memory order:</strong>State whether the observed process is treated as Markov, 1st/2nd-order semi-Markov, or another non-Markov process, what hidden states / cycles were collapsed, and whether a low estimate could be caused by hidden dissipation rather than actual near-equilibrium behavior. </li>
<li><strong>Dividing the lower bound and the main body:</strong>The irreversibility obtained from the observation time series is often a coarse-grained lower bound, not the microscopic physical dissipation itself. </li>
</ul>
</div>
<p><strong>Next:</strong> We need an irreversibility benchmark that is reproducible within the same modality and preprocessing chain, plus a log schema that separates wall-plug power, FLOPs, and simulated metabolic overhead. At minimum, publish an <strong>irreversibility route card</strong> naming signal route, state definition, observed-state closure / memory order, estimator family, null / surrogate control, lower-bound or model-based quantity type, and hardware power isolation. For more information, see <a href="wiki/thermodynamic-grounding-basics.html#irreversibility-route-card">Wiki: irreversibility route card</a>. </p>
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
<p><strong>Required logs:</strong> Stimulation site, intensity, masking, artifact window, synchronization path, median end-to-end latency / P95 / P99, jitter, dropout, recovery time, and a <strong>body / environment boundary card</strong> naming retained / substituted sensory, motor, and interoceptive channels, slow internal-milieu routes such as circadian phase or glucocorticoid / metabolic regime, plus the surrogate body / environment contract. If these depart from the TMS-EEG recommendations summarized by Hernandez-Pavon et al. (2023), the result is not treated here as a comparable causal test. </p>
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
<p><strong>Question:</strong>Long-term verification is not just whether a score stayed high. It asks whether <strong>state fluctuation</strong>, <strong>trait-like backbone</strong>, <strong>biological drift</strong>, <strong>interface / decoder drift</strong>, and <strong>maintenance-route burden</strong> were separated well enough that the time claim becomes falsifiable.</p>
<p><strong>2026-03-22 addendum:</strong>The older wording was too close to an abstract question about “acceptable change.” The site's current technical rule is narrower. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> showed that long-term iBCI control can be maintained by unsupervised recalibration, but that usability and <strong>fixed-decoder durability</strong> are different claims. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> showed a strong communication route while also quantifying degradation of a decoder trained on a specific earlier day. Therefore, V4 now treats long-term verification as the conjunction of <strong>temporal validity</strong>, <strong>bridge validity when acquisition regimes are crossed</strong>, and <strong>maintenance-state disclosure when persistence or forgetting is the claim</strong>.</p>
<ul>
<li><strong>Temporal validity:</strong> audit fixed decoder interval, state annotation, interface / decoder drift, recalibration burden, and transfer ceiling.</li>
<li><strong>Bridge validity:</strong> if “same-subject” evidence crosses live-to-fix, cross-regime, or cross-day reacquisition, attach the <a href="verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a>; same-subject is not same-state by default.</li>
<li><strong>Maintenance route:</strong> if the claim concerns persistence, forgetting, reconsolidation, remote memory, or recovery, attach the <a href="verification.html#maintenance-state-error-budget">maintenance-state error budget</a> instead of treating temporal hold as sufficient evidence.</li>
</ul>
<p><strong>Required next:</strong>M7 longitudinal audit + <a href="verification.html#temporal-validity-card">Temporal Validity Card</a> + update log (P2). For multiday or cross-regime claims, add the relevant bridge and maintenance-route cards instead of leaving the time burden implicit.</p>
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
<td>Willett, Littlejohn, and Wairagkar made significant advances in speech BCI as a local communication subsystem. Large vocabulary, streaming throughput, and closed-loop own-voice synthesis are important achievements. </td>
<td>What is shown here is local progress in communication routes, not whole-brain emulation or identity preservation. Throughput also does not by itself determine transferability, fixed-decoder durability, or rescue burden. </td>
</tr>
<tr>
<td><strong>Transfer-assisted speech-decoder initialization</strong></td>
<td>Singh et al. showed that distributed intracranial recordings can support a group-derived decoder that outperforms models trained on individual data alone, enabling a transfer-learning route for individual initialization. </td>
<td>This is evidence for <strong>cross-subject initialization</strong> and shared latent structure, not for subject-independent final deployment or for durable fixed-decoder operation after initialization. </td>
</tr>
<tr>
<td><strong>Fixed-decoder durability slice</strong></td>
<td>Willett et al. reported a bounded no-new-day-training slice, and Wairagkar et al. made it impossible to ignore the distinction between fast voice synthesis and the time horizon over which a decoder remains usable without rescue. </td>
<td>This still does not show that fixed decoders remain adequate over long horizons, across changing tasks, or across body / environment regime changes. </td>
</tr>
<tr>
<td><strong>Adaptive stabilization / rescue</strong></td>
<td>Karpowicz et al. and Wilson et al. showed that latent-dynamics alignment and unsupervised recalibration can stabilize iBCI performance when recording conditions drift. </td>
<td>This is a <strong>rescue route</strong>, not proof that the original decoder stayed stable on its own. It therefore cannot be collapsed into fixed-decoder durability or subject-independent deployment. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>2026-03-28 addendum: invasive language BCIs need an operational split</strong>
<p>
The older front-door wording was still too coarse because it let readers compress several different achievements into one `speech BCI success` bucket. The primary literature does not support that. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a> strengthened same-session throughput and also exposed a bounded fixed-decoder slice, <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> strengthened streaming throughput / expressivity, <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> strengthened instantaneous voice synthesis with silence fallback, <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a> strengthened transfer-assisted initialization, and <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a> plus <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> strengthened adaptive stabilization. Those papers do not all answer the same operational question, so this roadmap no longer places them on one row.
</p>
</div>

<div class="note-box">
<strong>Minimum evaluation pack</strong>
<ul>
<li><strong>Isolation of neural contribution:</strong> Report <code>no brain</code>, <code>time-shuffle</code>, <code>trial-shuffle</code>, <code>LM-only</code>, and <code>no-LM</code>; if decoding is search-based, also publish candidate-set size. </li>
<li><strong>Bounds of generalization: </strong>Report held-out stories, held-out vocabulary, cross-day, cross-task, and cross-subject separately and do not hide the need for subject cooperation or individual adaptation. </li>
<li><strong>Operational route label:</strong> State whether the result is same-session throughput, transfer-assisted initialization, fixed-decoder durability, or adaptive rescue after alignment / recalibration. </li>
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
<td>Hybrid measurement protocol exists, and M4 / I6 now add a public body / environment boundary-card policy. </td>
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
<td>Boto et al. (2018), Seymour et al. (2021), Holmes et al. (2023), Holmes et al. (2025), Rhodes et al. (2025)</td>
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
<li>Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
<li>Seymour, R. A., Alexander, N., Mellor, S., O'Neill, G. C., Tierney, T. M., Barnes, G. R., &amp; Maguire, E. A. (2021). Using OPMs to measure neural activity in standing, mobile participants. <a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">doi:10.1016/j.neuroimage.2021.118604</a></li>
<li>Holmes, N., Rea, M., Hill, R. M., et al. (2023). Enabling ambulatory movement in wearable magnetoencephalography with matrix coil active magnetic shielding. <a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">doi:10.1016/j.neuroimage.2023.120157</a></li>
<li>Holmes, N., Rea, M., Hill, R. M., et al. (2023). Naturalistic hyperscanning with wearable magnetoencephalography. <a href="https://doi.org/10.3390/s23125454" target="_blank">doi:10.3390/s23125454</a></li>
<li>Holmes, N., Leggett, J., Hill, R. M., et al. (2025). Wearable magnetoencephalography in a lightly shielded environment. <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">doi:10.1109/TBME.2024.3465654</a></li>
<li>Iivanainen, J., Borna, A., Zetter, R., et al. (2022). Calibration and Localization of Optically Pumped Magnetometers Using Electromagnetic Coils. <a href="https://doi.org/10.3390/s22083059" target="_blank">doi:10.3390/s22083059</a></li>
<li>Rhodes, N., Rier, L., Boto, E., Hill, R. M., &amp; Brookes, M. J. (2025). Source reconstruction without an MRI using optically pumped magnetometer-based magnetoencephalography. <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">doi:10.1162/IMAG.a.8</a></li>
<li>Wu, T., Xiao, W., Peng, X., Wu, T., &amp; Guo, H. (2025). Crosstalk reduction in optically pumped magnetometers arrays for biomagnetic measurement. <a href="https://doi.org/10.1063/5.0273491" target="_blank">doi:10.1063/5.0273491</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Johansen, A., Beliveau, V., Colliander, E., et al. (2024). An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>van Blooijs, D., Nunes, A., van den Boom, M. A., et al. (2023). Developmental trajectory of transmission speed in the human brain. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">doi:10.1038/s41593-023-01272-0</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., Schildknecht, C. M., Ineichen, B. V., &amp; Pruessmann, K. P. (2024). Myelin bilayer mapping in the human brain in vivo. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Guo, R., Yang, S., Wiesner, H. M., Li, Y., Zhao, Y., Liang, Z.-P., Chen, W., &amp; Zhu, X.-H. (2024). Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. <a href="https://doi.org/10.3389/fnins.2024.1389111" target="_blank">doi:10.3389/fnins.2024.1389111</a></li>
<li>Kaiser, A., Vind, F. A., Duarte, J. M. N., Jelescu, I., Lin, Y., Yu, X., Widmaier, M., Wenz, D., &amp; Xin, L. (2026). Ultra-high field <sup>31</sup>P functional magnetic resonance spectroscopy reveals NAD<sup>+</sup> dynamics in brain energy metabolism during visual stimulation. <a href="https://doi.org/10.1177/0271678X261415784" target="_blank">doi:10.1177/0271678X261415784</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Karkouri, J., Novoselova, M., Rodgers, C. T., et al. (2026). Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. <a href="https://doi.org/10.1002/mrm.70308" target="_blank">doi:10.1002/mrm.70308</a></li>
<li>Hagiwara, A., Hori, M., Kamagata, K., et al. (2018). Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. <a href="https://doi.org/10.1038/s41598-018-28852-6" target="_blank">doi:10.1038/s41598-018-28852-6</a></li>
<li>Galbusera, R., Weigel, M., Bahn, E., et al. (2025). Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. <a href="https://doi.org/10.1111/bpa.70010" target="_blank">doi:10.1111/bpa.70010</a></li>
<li>Colaes, R., Radwan, A., Billiet, T., et al. (2026). Evaluating the T1w/FLAIR ratio as a proxy for myelin: Associations with myelin water imaging, diffusion metrics, and cognition. <a href="https://doi.org/10.1007/s00234-025-03875-9" target="_blank">doi:10.1007/s00234-025-03875-9</a></li>
<li>Morgan, C. A., Thomas, D. L., Shao, X., et al. (2024). Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. <a href="https://doi.org/10.1002/nbm.5256" target="_blank">doi:10.1002/nbm.5256</a></li>
<li>Padrela, B. E., Slivka, M., Sneve, M. H., et al. (2025). Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">doi:10.1016/j.neurobiolaging.2024.12.012</a></li>
<li>Chung, K. J., Abdelhafez, Y. G., Spencer, B. A., et al. (2025). Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">doi:10.1038/s41467-025-58356-7</a></li>
<li>Villemagne, V. L., Harada, R., Dore, V., et al. (2022). First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">doi:10.2967/jnumed.121.263254</a></li>
<li>Villemagne, V. L., Harada, R., Dore, V., et al. (2022). Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">doi:10.2967/jnumed.121.263255</a></li>
<li>Hiraoka, K., Mesfin, B., Wu, Y., et al. (2025). Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. <a href="https://doi.org/10.1007/s12149-025-02083-y" target="_blank">doi:10.1007/s12149-025-02083-y</a></li>
<li>Mesfin, B., Ishioka, Y., Ichinose, Y., et al. (2026). Whole-body biodistribution of [18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. <a href="https://doi.org/10.1007/s12149-025-02144-2" target="_blank">doi:10.1007/s12149-025-02144-2</a></li>
<li>Matsuoka, K., Takado, Y., Kimura, Y., et al. (2026). Quantification of monoamine oxidase B expression with 11C-SL25.1188 for imaging reactive astrocytes in patients with Alzheimer's disease. <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">doi:10.1007/s00259-025-07542-2</a></li>
<li>Tyacke, R. J., Myers, J. F. M., Venkataraman, A., et al. (2018). Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">doi:10.2967/jnumed.118.208009</a></li>
<li>Livingston, N. R., Calsolaro, V., Hinz, R., et al. (2022). Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">doi:10.1038/s41380-021-01429-y</a></li>
<li>Best, L. M., Truong, J., McCluskey, T., et al. (2026). MAO-B status in alcohol use disorder: a [11C]SL25.1188 PET imaging study of putative astrogliosis. <a href="https://doi.org/10.1038/s41380-025-03355-9" target="_blank">doi:10.1038/s41380-025-03355-9</a></li>
<li>Jaisa-Aad, M., Muñoz-Castro, C., Healey, M. A., Hyman, B. T., &amp; Serrano-Pozo, A. (2024). Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer’s disease and related dementias. <a href="https://doi.org/10.1007/s00401-024-02712-2" target="_blank">doi:10.1007/s00401-024-02712-2</a></li>
<li>Hirschler, L., Runderkamp, B. A. R., Decker, A., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., Elbert, D. L., Giovangrandi, L., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Tallman, C. W., Siler, S. N., Lee, H., et al. (2025). Neuronal allocation and sparse coding of episodic memories in the human hippocampus. <a href="https://doi.org/10.1038/s41598-025-21967-7" target="_blank">doi:10.1038/s41598-025-21967-7</a></li>
<li>Huber, R., Mäki, H., Rosanova, M., Casarotto, S., Canali, P., Casali, A. G., Tononi, G., &amp; Massimini, M. (2013). Human cortical excitability increases with time awake. <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">doi:10.1093/cercor/bhs014</a></li>
<li>Kuhn, M., Wolf, E., Maier, J. G., Mainberger, F., Feige, B., Schmid, H., et al. (2016). Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. <a href="https://doi.org/10.1038/ncomms12455" target="_blank">doi:10.1038/ncomms12455</a></li>
<li>Fehér, K. D., Henckaerts, P., Hirsch, V., Bucsenez, U., Kuhn, M., Maier, J. G., et al. (2026). A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">doi:10.1016/j.neuroimage.2026.121723</a></li>
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
<li>Khatri, U. U., Pulliam, K., Manesiya, M., Vieyra Cortez, M., Millán, J. del R., &amp; Hussain, S. J. (2025). Personalized whole-brain activity patterns predict human corticospinal tract activation in real-time. <a href="https://doi.org/10.1016/j.brs.2024.12.1193" target="_blank">doi:10.1016/j.brs.2024.12.1193</a></li>
<li>Holt, A. B., Kormann, E., Gulberti, A., et al. (2019). Phase-Dependent Suppression of Beta Oscillations in Parkinson's Disease Patients. <a href="https://doi.org/10.1523/JNEUROSCI.1913-18.2018" target="_blank">doi:10.1523/JNEUROSCI.1913-18.2018</a></li>
<li>Zrenner, C., Galevska, D., Nieminen, J. O., Baur, D., Stefanou, M. I., &amp; Ziemann, U. (2020). The shaky ground truth of real-time phase estimation. <a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">doi:10.1016/j.neuroimage.2020.116761</a></li>
<li>Gordon, P. C., Dörre, S., Belardinelli, P., Stenroos, M., Zrenner, B., Ziemann, U., &amp; Zrenner, C. (2021). Prefrontal Theta-Phase Synchronized Brain Stimulation With Real-Time EEG-Triggered TMS. <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">doi:10.3389/fnhum.2021.691821</a></li>
<li>Bruegger, D., &amp; Abegg, M. (2021). Prediction of cortical theta oscillations in humans for phase-locked visual stimulation. <a href="https://doi.org/10.1016/j.jneumeth.2021.109288" target="_blank">doi:10.1016/j.jneumeth.2021.109288</a></li>
<li>Vigué-Guix, I., Morís Fernández, L., Torralba Cuello, M., Ruzzoli, M., &amp; Soto-Faraco, S. (2022). Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain-computer interface (BCI)? <a href="https://doi.org/10.1111/ejn.14931" target="_blank">doi:10.1111/ejn.14931</a></li>
<li>Kim, B., Erickson, B. A., Fernandez-Nunez, G., Rich, R., Mentzelopoulos, G., Vitale, F., &amp; Medaglia, J. D. (2023). EEG Phase Can Be Predicted with Similar Accuracy across Cognitive States after Accounting for Power and Signal-to-Noise Ratio. <a href="https://doi.org/10.1523/ENEURO.0050-23.2023" target="_blank">doi:10.1523/ENEURO.0050-23.2023</a></li>
<li>Little, S., Pogosyan, A., Neal, S., et al. (2013). Adaptive deep brain stimulation in advanced Parkinson disease. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser, G., Pogosyan, A., Little, S., et al. (2017). The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Hernandez-Pavon, J. C., Metsomaa, J., Mutanen, T. P., et al. (2023). TMS combined with EEG: Recommendations and open issues. <a href="https://doi.org/10.1016/j.brs.2023.02.009" target="_blank">doi:10.1016/j.brs.2023.02.009</a></li>
<li>Hougland, J. R., Kirchhoff, M., Vetter, D. E., Ahola, O., Jooß, A., Humaidan, D., &amp; Ziemann, U. (2025). Fluctuations in the optimal sensorimotor mu-rhythm phase associated with high corticospinal excitability during TMS-EEG. <a href="https://doi.org/10.1016/j.brs.2025.09.019" target="_blank">doi:10.1016/j.brs.2025.09.019</a></li>
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
<li>Singh, A., Wu, E., Ramsey, N. F., et al. (2025). Transfer learning via distributed brain recordings enables reliable speech decoding. <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">doi:10.1038/s41467-025-63825-0</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain&ndash;computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
</ol>

<h3>E2. Longitudinal validity, state / trait / drift, and recalibration</h3>
<ol>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Benisty, H., Barson, D., Moberly, A. H., et al. (2024). Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Egger, A., Bayon, C., d'Almeida, J., et al. (2024). Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Gallego, J. A., Perich, M. G., Chowdhury, R. H., Solla, S. A., &amp; Miller, L. E. (2020). Long-term stability of cortical population dynamics underlying consistent behavior. <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">doi:10.1038/s41593-019-0555-4</a></li>
<li>Noda, T., Kienle, E., Eppler, J.-B., et al. (2025). Homeostasis of a representational map in the neocortex. <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">doi:10.1038/s41593-025-01982-7</a></li>
<li>Karpowicz, B. M., Ali, Y. H., Wimalasena, L. N., et al. (2025). Stabilizing brain-computer interfaces through alignment of latent dynamics. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">doi:10.1038/s41467-025-59652-y</a></li>
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
<li>Villaverde, A. F. (2019). Observability and Structural Identifiability of Nonlinear Biological Systems. <a href="https://doi.org/10.1155/2019/8497093" target="_blank">doi:10.1155/2019/8497093</a></li>
<li>Villaverde, A. F., Tsiantis, N., &amp; Banga, J. R. (2019). Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Massonis, G., &amp; Villaverde, A. F. (2020). Finding and breaking Lie symmetries: implications for structural identifiability and observability in biological modelling. <em>Symmetry</em>, 12(3), 469. <a href="https://doi.org/10.3390/sym12030469" target="_blank">doi:10.3390/sym12030469</a></li>
<li>Diop, S., &amp; Fliess, M. (1991). Nonlinear observability, identifiability, and persistent trajectories. <em>Proceedings of the 30th IEEE Conference on Decision and Control</em>, 714-719. <a href="https://doi.org/10.1109/CDC.1991.261405" target="_blank">doi:10.1109/CDC.1991.261405</a></li>
<li>Raue, A., Becker, V., Klingmüller, U., &amp; Timmer, J. (2010). Identifiability and observability analysis for experimental design in nonlinear dynamical models. <em>Chaos</em>, 20(4), 045105. <a href="https://doi.org/10.1063/1.3528102" target="_blank">doi:10.1063/1.3528102</a></li>
<li>Chis, O.-T., Villaverde, A. F., Banga, J. R., &amp; Balsa-Canto, E. (2016). On the relationship between sloppiness and identifiability. <em>Mathematical Biosciences</em>, 282, 147-161. <a href="https://doi.org/10.1016/j.mbs.2016.10.009" target="_blank">doi:10.1016/j.mbs.2016.10.009</a></li>
<li>White, A., Tolman, M., Thames, H. D., Withers, H. R., Mason, K. A., &amp; Transtrum, M. K. (2016). The limitations of model-based experimental design and parameter estimation in sloppy systems. <em>PLOS Computational Biology</em>, 12(12), e1005227. <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">doi:10.1371/journal.pcbi.1005227</a></li>
<li>Gevertz, J. L., &amp; Kareva, I. (2024). Minimally sufficient experimental design using identifiability analysis. <em>npj Systems Biology and Applications</em>, 10, 2. <a href="https://doi.org/10.1038/s41540-023-00325-1" target="_blank">doi:10.1038/s41540-023-00325-1</a></li>
<li>Liu, X., Wanika, L., Chappell, M. J., &amp; Branke, J. (2025). Efficient data collection for establishing practical identifiability via active learning. <em>Computational and Structural Biotechnology Journal</em>, 27, 4992-5006. <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">doi:10.1016/j.csbj.2025.10.058</a></li>
<li>Rasero, J., Betzel, R., Sentis, A. I., Kraynak, T. E., Gianaros, P. J., &amp; Verstynen, T. (2024). Similarity in evoked responses does not imply similarity in macroscopic network states. <a href="https://doi.org/10.1162/netn_a_00354" target="_blank">doi:10.1162/netn_a_00354</a></li>
<li>Langdon, C., &amp; Engel, T. A. (2025). Latent circuit inference from heterogeneous neural responses during cognitive tasks. <em>Nature Neuroscience</em>, 28, 665-675. <a href="https://doi.org/10.1038/s41593-025-01869-7" target="_blank">doi:10.1038/s41593-025-01869-7</a></li>
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
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Lee, H.-K., Barbarosie, M., Kameyama, K., Bear, M. F., &amp; Huganir, R. L. (2003). Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">doi:10.1016/S0092-8674(03)00122-3</a></li>
<li>Havekes, R., Park, A. J., Tolentino, R. E., et al. (2016). Compartmentalized PDE4A5 signaling impairs hippocampal synaptic plasticity and long-term memory. <a href="https://doi.org/10.1523/JNEUROSCI.0248-16.2016" target="_blank">doi:10.1523/JNEUROSCI.0248-16.2016</a></li>
<li>Vierra, N. C., et al. (2023). Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">doi:10.1038/s41467-023-40930-6</a></li>
<li>Altas, B., Tuffy, L. P., Patrizi, A., et al. (2024). Region-specific phosphorylation determines Neuroligin-3 localization to excitatory versus inhibitory synapses. <a href="https://doi.org/10.1016/j.biopsych.2023.12.020" target="_blank">doi:10.1016/j.biopsych.2023.12.020</a></li>
<li>Rodriguez, A. C., Kram&aacute;r, E. A., Augustynski, A. S., et al. (2025). HDAC3 Serine 424 phospho-mimic and phospho-null mutants bidirectionally modulate long-term memory formation and synaptic plasticity in the adult and aging mouse brain. <a href="https://doi.org/10.1523/JNEUROSCI.1619-24.2025" target="_blank">doi:10.1523/JNEUROSCI.1619-24.2025</a></li>
<li>Frey, U., &amp; Morris, R. G. M. (1997). Synaptic tagging and long-term potentiation. <a href="https://doi.org/10.1038/385533a0" target="_blank">doi:10.1038/385533a0</a></li>
<li>Shires, K. L., Da Silva, B. M., Hawthorne, J. P., et al. (2012). Synaptic tagging and capture in the living rat. <a href="https://doi.org/10.1038/ncomms2250" target="_blank">doi:10.1038/ncomms2250</a></li>
<li>Govindarajan, A., Israely, I., Huang, S.-Y., &amp; Tonegawa, S. (2011). The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">doi:10.1016/j.neuron.2010.12.008</a></li>
<li>Fonseca, R., Vabulas, R. M., Hartl, F. U., Bonhoeffer, T., &amp; Nagerl, U. V. (2006). A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">doi:10.1016/j.neuron.2006.08.015</a></li>
<li>Pandey, K., Yu, X.-W., Steinmetz, A., &amp; Alberini, C. M. (2021). Autophagy coupled to translation is required for long-term memory. <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">doi:10.1080/15548627.2020.1775393</a></li>
<li>Chang, Y. C., Gao, Y., Lee, J. Y., et al. (2024). Identification of secretory autophagy as a mechanism modulating activity-induced synaptic remodeling. <a href="https://doi.org/10.1073/pnas.2315958121" target="_blank">doi:10.1073/pnas.2315958121</a></li>
<li>Parker, D., Davidson, K., Osmulski, P. A., et al. (2025). Proteasome augmentation mitigates age-related cognitive decline in mice. <a href="https://doi.org/10.1111/acel.14492" target="_blank">doi:10.1111/acel.14492</a></li>
<li>Correia, S. S., Bassani, S., Brown, T. C., et al. (2008). Motor protein-dependent transport of AMPA receptors into spines during long-term potentiation. <a href="https://doi.org/10.1038/nn2063" target="_blank">doi:10.1038/nn2063</a></li>
<li>Swarnkar, S., Avchalumov, Y., Espadas, I., et al. (2021). Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">doi:10.1016/j.celrep.2021.109369</a></li>
<li>Aiken, J., &amp; Holzbaur, E. L. F. (2024). Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">doi:10.1016/j.cub.2024.03.010</a></li>
<li>de Queiroz, B. R., et al. (2025). Axonal RNA localization is essential for long-term memory. <a href="https://doi.org/10.1038/s41467-025-57651-7" target="_blank">doi:10.1038/s41467-025-57651-7</a></li>
<li>Stringer, C., Pachitariu, M., Steinmetz, N., et al. (2019). Spontaneous behaviors drive multidimensional, brainwide activity. <a href="https://doi.org/10.1126/science.aav7893" target="_blank">doi:10.1126/science.aav7893</a></li>
<li>Saleem, A. B., Ayaz, A., Jeffery, K. J., Harris, K. D., &amp; Carandini, M. (2013). Integration of visual motion and locomotion in mouse visual cortex. <a href="https://doi.org/10.1038/nn.3567" target="_blank">doi:10.1038/nn.3567</a></li>
<li>Ravassard, P., Kees, A., Willers, B., et al. (2013). Multisensory control of hippocampal spatiotemporal selectivity. <a href="https://doi.org/10.1126/science.1232655" target="_blank">doi:10.1126/science.1232655</a></li>
<li>Zelano, C., Jiang, H., Zhou, G., et al. (2016). Nasal respiration entrains human limbic oscillations and modulates cognitive function. <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">doi:10.1523/JNEUROSCI.2586-16.2016</a></li>
<li>Raut, R. V., Rosenthal, Z. P., Wang, X., et al. (2025). Arousal as a universal embedding for spatiotemporal brain dynamics. <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">doi:10.1038/s41586-025-09544-4</a></li>
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
<li>Martínez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2019). Inferring broken detailed balance in the absence of observable currents. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">doi:10.1038/s41467-019-11051-w</a></li>
<li>Hartich, D., &amp; Godec, A. (2024). Comment on “Inferring broken detailed balance in the absence of observable currents”. <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">doi:10.1038/s41467-024-52602-0</a></li>
<li>Martínez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2024). Reply to: Comment on “Inferring broken detailed balance in the absence of observable currents”. <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">doi:10.1038/s41467-024-52603-z</a></li>
<li>Blom, K., Song, K., Vouga, E., Godec, A., &amp; Makarov, D. E. (2024). Milestoning estimators of dissipation in systems observed at a coarse resolution. <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">doi:10.1073/pnas.2318333121</a></li>
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
