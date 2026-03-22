---
layout: default
title: "Verification: Mind Uploading Verification Commons"
description: "A blueprint of standards, benchmarks, registries, and audits for turning mind uploading and WBE into a science with measurable progress."
article_type: Platform
subtitle: "Use the logic of PDB x BIDS x PhysioNet x OSF to define WBE success conditions and reproducible progress"
author: Mind Uploading Research Project
last_updated: "2026-03-22"
note: "Operational Specification"
audience: "Readers who want the site's core policy and anyone checking what must exist before progress can honestly be claimed"
reading_time: "15-25 min"
page_intro: "This page is the core blueprint of Mind-Upload. It explains how to define progress in advance rather than retroactively by aligning data, evaluation, failure conditions, and reproduction procedures first."
accuracy_note: "This page does not claim that WBE is already possible. It defines the substrate needed to test whether it is."
page_highlights:
  - "Standards, repositories, benchmarks, and audits must be built as one package."
  - "Claim levels and failure conditions are fixed up front so decoding is not confused with emulation."
  - "For maintenance-state claims, local causal evidence and living-human proxy evidence are kept on separate axes, so bridge assumptions must be disclosed rather than silently fused."
  - "For decode / biomarker scores, the Specificity & Shortcut Card separates the target neural variable from nuisance routes and audits subject / session fingerprint plus acquisition-distribution shortcuts independently."
  - "This page explains why collecting data alone is not the same as making progress."
  - "For foundation / self-supervised EEG results, the Pretraining Card fixes corpus identity, overlap audit, setup diversity, harmonization, adaptation regime, benchmark provenance including split randomness / hidden grouping and inference-stage budget, and scale / efficiency before any transfer claim is read strongly."
  - "For brain-to-text and speech decode, the Neural Contribution Card fixes task constraint, language prior, candidate set, no-brain / no-LM / shuffle baselines, and subject cooperation."
  - "For multimodal or atlas-prior results, the Fusion Card is added on top of the Observability Budget so acquisition relation, synchronization, fusion model, vascular-state / CVR limits for hemodynamic stacks, and external validation are fixed explicitly."
  - "For living-human proxy bundles, the Human Proxy Composition Card fixes direct observable by row, same-subject relation, model burden, incremental evidence, and residual latent-state ceiling before several proxy routes may be promoted together."
  - "For living-human maintenance routes, submissions must separate proxy class, operational maturity, and calibrator role, because a real human proxy may still calibrate only one bounded hidden-state family."
  - "For sequential cross-regime claims that bridge live measurement to later fixation / ex vivo follow-up or cross-day reacquisition, the State-Continuity Bridge Card fixes acquisition order, elapsed time, regime continuity, coordinate transfer / deformation model, bridge validation rung, and residual drift ceiling before same-state language is allowed."
  - "For diffusion-MRI tractography connectomes, the Observability Budget now requires a tractography route card that names direct observables, endpoint assignment, graph-construction choices, uncertainty, and abstention."
  - "For tractography connectomes, cortical endpoint assignment and graph-construction choices are separate audit items; a graph metric without them remains pipeline-conditioned."
  - "For MRSI-derived metabolic-connectome claims, the Observability Budget now requires a metabolic-similarity route card that names the metabolite set, parceling, correction model, spectral QC, and whether the object is static similarity or kinetic rate imaging."
  - "For SV2A / synaptic-density PET claims, the maintenance-state budget now requires a route card that names tracer / quantification route, comparison family, functional target, and abstention before regional density is overread as current synaptic state."
  - "For destructive ultrastructure claims, the Observability Budget now requires a destructive-structure route card that names preservation route, live-to-fix delay, registration scope, section-loss / segmentation QA, throughput scale, and omitted live-state families."
  - "For connectome-constrained predictors, the Observability Budget now requires a conditional-model route card that names the structural prior, fitted degrees of freedom, task/state regime, omitted mechanisms, validation class, and abstention boundary."
  - "For inverse and model-based claims, the Identifiability Card now separates observability, structural identifiability, and practical identifiability, and requires candidate-space, experiment-design, and abstention disclosure before uniqueness language is allowed."
  - "For sleep replay claims, the maintenance-state budget now requires a route card that names preparation, event definition, timing policy, item-selection regime, and abstention before overnight gain is read mechanistically."
  - "For myelin / oligodendrocyte claims, the maintenance-state budget now requires a route card that names claim family, structural unit, function target, recovery boundary, human proxy class, and abstention."
  - "For ionic / chloride claims, the maintenance-state budget now requires a route card that names claim family, direct ionic observable, spatial regime, perturbation route, human proxy class, and abstention."
  - "For neuromodulatory claims, the maintenance-state budget now requires a route card that names claim family, transmitter axis, direct observable, challenge or administered-drug route, time window / model burden, and abstention."
  - "For clearance / immune claims, the maintenance-state budget now requires a route card that names claim family, direct observable, driver / perturbation route, human model burden, function target, and abstention."
  - "For bioenergetic / mitochondrial claims, the maintenance-state budget now requires a route card that names claim family, compartment, direct energetic observable, quantity type / model burden, function target, human proxy class, and abstention."
  - "For astrocyte / glial-state claims, the maintenance-state budget now requires a route card that names claim family, direct astrocyte observable, perturbation route, function target, human proxy class, and abstention."
  - "For phospho-signaling / second-messenger claims, the maintenance-state budget now requires a route card that names claim family, assay / direct observable, compartment scope, timing window, causal leverage, and abstention."
  - "For post-transcriptional RNA-state claims, the maintenance-state budget now requires a route card that names claim family, RNA control axis, assay / direct observable, downstream object, time window, human observability ceiling, and abstention."
  - "For local proteostasis / synaptic-tagging claims, the maintenance-state budget now requires a route card that names claim family, integrative unit, direct observable, turnover window, perturbation route, human observability ceiling, and abstention."
  - "For DCM / effective-connectivity claims, the Observability Budget now requires an effective-connectivity route card that names candidate model space, observation-model assumptions, validation, reliability, and abstention."
  - "For irreversibility / thermodynamic claims, the route card now names signal route, coarse-graining / timescale, observed-state closure / hidden-degree risk, estimator family plus dynamical assumptions, null control, quantity type, physiology-side grounding when energetic language is used, and cost isolation before any claim ceiling is raised."
  - "For ESI claims, simulation / phantom, stimulation ground truth, simultaneous invasive recording, and postsurgical outcome are separate validation classes; 'externally validated' alone is insufficient."
  - "For ESI claims, one best inverse map is not enough; this page now asks for cross-solver / cross-parameter spread or posterior / ensemble width before anatomical claims are read strongly."
  - "For ESI claims, a field-formation audit now asks whether the target source class should reach the scalp at all given extent, orientation, cancellation, and tissue-model assumptions."
  - "At L2 and above, the latent-state error budget is added on top of the Observability Budget so the still-unobserved states that stop the claim are disclosed."
  - "At L2 and above, perisynaptic ECM / PNN state is separated from synaptic weights and glia when a claim depends on adult plasticity, receptor mobility, or memory stabilization."
  - "At L2 and above, post-transcriptional RNA-state is separated from gene-level transcript abundance and proteostasis when a claim depends on isoform choice, m6A-dependent translation / degradation, or RNA-editing ratios."
  - "At L2 and above, phospho-signaling / second-messenger state is separated from transcriptomics, proteomics, and nominal weights when a claim depends on phosphosite occupancy, kinase/phosphatase balance, or signaling nanodomains."
  - "At L2 and above, local proteostasis / synaptic-tagging state is separated from current weights and transcription when a claim depends on late-LTP capture, consolidation, or reconsolidation."
  - "At L2 and above, cargo-transport / cytoskeletal trafficking state is separated from proteostasis and bioenergetics when a claim depends on compartment-specific delivery of receptors, endosomes, RNA cargoes, or presynaptic components."
  - "At L2 and above, ionic milieu / chloride homeostasis is separated from excitability and glial support when a claim depends on inhibitory polarity, rhythm stability, or state transitions."
  - "At L2 and above, shared extracellular / electrical state is separated from chemical synapses and ionic proxy classes, and electrical-state claims now require a route card naming claim family, direct electrical observable, spatial regime, perturbation / calibration route, human evidence class, and abstention."
  - "For thermal-state claims, the maintenance-state budget now requires a route card that names claim family, direct thermal observable, driver / perturbation route, time window, function target, human proxy class, and abstention."
  - "At L2 and above, bioenergetic / mitochondrial support is separated from glial support when a claim depends on repeated-burst reliability, local ATP reserve, or dendritic plasticity."
  - "At L2 and above, astrocyte network / ensemble state is separated from generic support background when a claim depends on recall, multiday stabilization, or fear-state representations."
  - "At L2 and above, clearance / immune support is separated from astrocyte / glial-state when a claim depends on multiday recovery, protein clearance, or microglia-mediated synaptic maintenance."
  - "At L2 and above, delay is treated as timing-state rather than one scalar, so device latency, biological conduction timing, and human macro timing proxies are not collapsed into one number."
  - "At L2 and above for intervention / closed-loop results, the Intervention Card fixes trigger rule, timing audit, control / sham, safe stop, and recalibration burden."
  - "At L3 and above for embodied-loop results, the Body / Environment Boundary Card fixes which sensory, motor, and interoceptive channels were preserved, substituted, or omitted."
  - "For cross-day or longitudinal claims, the Temporal Validity Card audits fixed decoder interval, state annotation, recalibration burden, and transfer ceiling independently."
  - "For cross-day or remote-memory claims, the maintenance-state error budget reports controller state, sleep history, sleep architecture / replay-coupling state, and support-state proxies separately, so temporal success is not auto-promoted to a maintenance-consistent claim."
  - "For chronic invasive claims, signal-chain drift and implant tissue response are audited separately rather than being folded into unit-identity audit alone."
  - "For outputs that include probabilities, intervals, prediction sets, or abstention, the Calibration & Abstention Card fixes fit/calibration/test separation, evaluation family, coverage-risk, and fallback behavior."
known_points:
  - "Comparable progress does not exist unless standards, shared infrastructure, evaluation, and auditing are aligned together."
  - "At L0-L2, reproducibility and falsification conditions can be designed in advance."
  - "Decode and emulate are distinct claims and require different evidence."
  - "A maintenance-state claim that combines rodent causal evidence with human proxy evidence still needs an explicit bridge statement naming the matched state family, proxy class, and remaining latent controller."
  - "The same decoding score is not target-specific evidence if eye movement, EMG, uninstructed movement, auditory feedback, subject / session fingerprint, or acquisition-distribution shortcuts remain unresolved."
  - "A foundation-model score without corpus-overlap, harmonization, adaptation, and benchmark-version disclosure, including split randomness / hidden grouping, remains qualified decoding evidence rather than portable transfer evidence."
  - "A multimodal result is not one thing; simultaneous acquisition, geometric fusion, invasive calibration, and atlas priors must be audited separately."
  - "Several living-human proxy routes do not add automatically; without same-subject relation, model disclosure, and cross-row calibration, the bundle remains below state-identification language."
  - "A same-subject or same-brain pipeline can still be sequential and bridge-limited; live-to-fix delay, regime mismatch, deformation correction, and state drift remain separate audit items."
  - "For ESI, passing one validation class does not auto-pass the others; stimulation error, simultaneous invasive concordance, and postsurgical outcome answer different questions."
  - "For ESI, inverse-family, package, parameter, and conductivity choices can materially shift the reconstructed source, so solver-disagreement and uncertainty width are themselves audit items."
  - "For ESI, the target generator may already be filtered out upstream by field formation, so visibility, cancellation, and CSF-aware head-model assumptions are separate audit items from inverse choice."
  - "A BOLD or fNIRS amplitude difference without vascular-state / CVR audit remains a hemodynamic-limited difference rather than a clean neural difference."
  - "An MRSI-derived metabolic-connectome label without metabolite-set, parceling, correction-model, and QC disclosure remains a macro-biochemical similarity scaffold rather than tractography or flux imaging."
  - "A connectome-constrained activity predictor without structural-prior, fitted-parameter, task-regime, omitted-mechanism, validation, and abstention disclosure remains a conditional model rather than internal-state recovery."
  - "More direct observables do not by themselves guarantee unique recovery; degeneracy can persist unless candidate-model space, recorded subset, and perturbation design are disclosed."
  - "An effective-connectivity label without candidate-model, validation, and reliability disclosure remains a model-conditioned hypothesis rather than discovered causal wiring."
  - "An irreversibility label without signal-route, coarse-graining / timescale, estimator-family, dynamical-assumption, and quantity-type disclosure remains an exploratory auxiliary result rather than a portable thermodynamic measurement."
  - "A synapse list or weight estimate does not by itself fix perisynaptic ECM / PNN state, so plasticity and stabilization claims need a separate ceiling."
  - "A cell atlas or gene-level transcript count does not by itself fix post-transcriptional RNA-state, so isoform-, m6A-, and RNA-editing-dependent claims need a separate ceiling."
  - "A transcriptomic or proteomic snapshot does not by itself fix phospho-signaling / second-messenger state, so phosphosite-dependent plasticity and nanodomain-signaling claims need a separate ceiling."
  - "A weight estimate does not fix which tagged synapses or dendritic branches capture plasticity-related proteins, so late-stabilization claims need a separate proteostasis ceiling."
  - "A weight estimate or local-translation clue does not by itself fix branch- or bouton-specific cargo delivery, so compartment-specific stabilization and synaptogenesis claims need a separate transport ceiling."
  - "Sleep duration or deprivation alone does not fix slow-oscillation / spindle / ripple coordination, so overnight retention claims need a separate sleep-architecture ceiling."
  - "A connectome, cell type, and weight estimate do not by themselves fix ionic milieu / chloride homeostasis, so inhibitory sign and state-transition claims need a separate ceiling."
  - "A chemical connectome and nominal inhibition do not by themselves fix electrical coupling, endogenous field effects, or local inhibitory driving force, so fast-synchrony and oscillatory-coordination claims need a separate ceiling."
  - "A connectome, cell type, and timing proxy do not by themselves fix local thermal-state, so field-potential and sequence-timing claims need a separate ceiling."
  - "A connectome, cell type, and glial proxy do not by themselves fix local ATP reserve or mitochondrial positioning, so repeated-burst and dendritic-plasticity claims need a separate bioenergetic ceiling."
  - "A glial proxy or generic metabolic note does not by itself fix astrocyte network / ensemble state, so recall, reconsolidation, and multiday-stabilization claims need a separate astrocyte-state ceiling."
  - "A CSF-mobility or glymphatic result without cell-specific immune / synaptic-maintenance disclosure remains a macro support-state proxy rather than local clearance-controller evidence."
  - "Passing a hardware latency audit is not the same as recovering biological timing-state; claims that depend on phase or synchrony need both sides separated."
  - "Passing a latency audit is not the same as fixing the body / environment boundary; L3 claims still need retained/substituted loop disclosure."
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
  - label: "Wiki: State-Continuity Bridge"
    url: "/wiki/state-continuity-bridge.html"
    description: "Explains why same-subject or same-brain sequential workflows still need a bridge audit before same-state language is allowed."
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
<td>Stability in real-time operation, latency management, safe-stop conditions, and a disclosed body / environment boundary with retained or substituted loop channels.</td>
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
Closed-loop work needs more than offline accuracy. It also needs end-to-end latency, jitter, drift handling, safety-stop design, and an explicit statement of which body / environment loops were preserved or replaced. For a beginner guide to the timing side, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed Loops, Latency, Jitter, and Safety Stops</a>.
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

<div class="note-box">
<strong>If A Paper Says "Effective Connectivity"</strong>
<p>
On this site, the phrase alone does not count as causal-wiring discovery. DCM and related effective-connectivity methods are read here as <strong>model-conditioned causal hypotheses</strong> unless the paper also discloses the compared model space, omitted alternatives, neural / hemodynamic assumptions, family comparison or model recovery, perturbation or external validation, test-retest window, and abstention boundary. The shortest operational rule is <a href="wiki/observation-to-estimation.html#effective-connectivity-route-card">Wiki: effective-connectivity route card</a>.
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
The most important update in this pass is that the criticism that ``important hidden state remains'' has finally been translated into <strong>submission format</strong>. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">Yao et al. (2023)</a> show that whole-brain atlases strengthen cell-type taxonomy and spatial arrangement, but do not directly provide current state. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> greatly advance same-brain structure-function links, but still remain in the domain of local conditional prediction. Furthermore, as <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> and <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> show, even externally validated HD-EEG / ESI remains dependent on source depth and head model and does not provide a generally unique restoration. Therefore, this site requires an <strong>Observability Budget</strong> for submissions above L1 so that they first state what was directly observed and what remains estimated.
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
<td>Write the named validation class, such as simulation / phantom, intracranial stimulation, concurrent invasive recording, postsurgical outcome, same-brain co-registration, and Patch-seq bridge, together with which error term it audits. </td>
<td>It is easy to confuse improvements in accuracy and visualization with getting closer to the ground truth. </td>
</tr>
<tr>
<td><strong>solution-set stability</strong></td>
<td>For inverse/model-based claims, write the cross-solver / cross-parameter spread or posterior / ensemble width, and say whether the displayed map is best-case, median, or ensemble summary. </td>
<td>It is easy to publish one clean-looking map and hide that the inference is strongly method-conditioned. </td>
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
<h3 class="section-title" id="identifiability-card">Identifiability Card for inverse and model-based claims</h3>
<div class="note-box">
<strong>2026-03-20 addendum: observability and identifiability must be logged separately</strong>
<p>
The remaining weakness after adding the <strong>Observability Budget</strong> was that richer measurement could still be overread as if it had already collapsed the solution set. The primary literature does not support that shortcut. <a href="https://doi.org/10.1155/2019/8497093" target="_blank">Villaverde (2019)</a> reviewed that <strong>observability</strong> and <strong>structural identifiability</strong> are different theoretical questions, and <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde et al. (2019)</a> showed that unknown states, parameters, and inputs must often be treated jointly rather than as separable audits. In neuroscience, <a href="https://doi.org/10.1038/nn1352" target="_blank">Prinz et al. (2004)</a> showed that similar circuit activity can arise from disparate parameters, <a href="https://doi.org/10.1162/netn_a_00354" target="_blank">Rasero et al. (2024)</a> showed that similar human activation patterns can still hide different macroscopic network states, and <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that connectome-constrained recurrent networks remain degenerate until additional recordings collapse the space of compatible dynamics. <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">Liu et al. (2025)</a> then showed that practical identifiability depends on experiment design and data-collection policy, not only on the estimation algorithm. Therefore, this site now asks inverse and model-based claims to attach an <strong>Identifiability Card</strong> on top of the Observability Budget.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Identifiability Card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claim object</strong></td>
<td>Name whether the submission claims source location, latent state, parameter set, effective connectivity, controller variable, or connectome-conditioned predictor, and specify the timescale and spatial unit of that object.</td>
<td>The paper is not read as if all forms of "recovery" were interchangeable.</td>
</tr>
<tr>
<td><strong>Structural identifiability layer</strong></td>
<td>State whether the declared equations / priors / outputs make the target theoretically identifiable, and name known symmetries, reparameterizations, or variables that remain non-identifiable even with noise-free data.</td>
<td>Finite-data success is not promoted to in-principle uniqueness.</td>
</tr>
<tr>
<td><strong>Practical identifiability layer</strong></td>
<td>Report the finite-data evidence such as posterior width, profile likelihood, bootstrap / ensemble spread, SNR dependence, and sample or time-window dependence under the actual dataset.</td>
<td>A theoretically identifiable model is not read as practically recoverable from the submitted data.</td>
</tr>
<tr>
<td><strong>Competing solution set</strong></td>
<td>Name the alternative model families, near-equivalent fits, solver families, or local optima that remained competitive, and summarize how different their internal variables still are.</td>
<td>One good fit is not read as recovered mechanism or unique internal state.</td>
</tr>
<tr>
<td><strong>Experiment-design leverage</strong></td>
<td>Disclose which perturbations, tasks, stimulus regimes, or active data-collection choices were intentionally used to collapse degeneracy, and say explicitly if the evidence is passive-observation only.</td>
<td>Passive fit is not promoted to solved identification just because prediction improved.</td>
</tr>
<tr>
<td><strong>Coverage / recorded subset</strong></td>
<td>Name which regions, neurons, channels, or variables were actually observed, how that subset was chosen, and what latent compartments remain unmeasured but could still change the solution.</td>
<td>Sparse or convenience coverage is not read as state closure for the whole system.</td>
</tr>
<tr>
<td><strong>Held-out falsification route</strong></td>
<td>Report held-out perturbation prediction, external calibration, or an explicit failure test that the chosen solution had to pass rather than explain post hoc.</td>
<td>Observed fit is not read as uniquely recovered state dynamics.</td>
</tr>
<tr>
<td><strong>Abstention boundary</strong></td>
<td>Name which uniqueness claim is <em>not</em> being made, and under which alternative assumptions the interpretation changes materially.</td>
<td>The result is not promoted from predictive/localized/model-conditioned evidence to unique recovery language.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Minimum operating rule</strong>
<p>
If this card is missing, this site stops at <strong>predictive fit</strong>, <strong>localized source hypothesis</strong>, or <strong>model-conditioned mechanism</strong>. It does not promote the result to <strong>unique internal-state recovery</strong>, <strong>state-complete reconstruction</strong>, or <strong>mechanism uniquely identified</strong> language.
</p>
</div>
<h3 class="section-title" id="fusion-card">Fusion Card for multimodal or atlas-prior results</h3>
<div class="note-box">
<strong>2026-03-20 addendum: multimodal and atlas-prior results need a Fusion Card</strong>
<p>
The remaining weakness after adding the <strong>Observability Budget</strong> was that the words <strong>simultaneous</strong>, <strong>multimodal</strong>, or <strong>atlas-informed</strong> could still be overread as if the fusion step itself had already been validated. The primary literature does not support that shortcut. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> showed that synchronization middleware can align streams, but does not by itself certify device-side delay truth or biological equivalence. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a> showed that EEG-fMRI fusion remains a model-conditioned inference problem. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> and <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> then showed that even simultaneous multimodal acquisition can reveal both convergent and divergent structure across modalities rather than one self-validating ground truth. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> and <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al. (2019)</a> further showed that low-frequency/global fMRI-linked components can carry autonomic physiology, so a shared factor is still not automatic target-variable specificity. Therefore, this site now asks multimodal or atlas-prior claims to attach a <strong>Fusion Card</strong> on top of the Observability Budget.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Fusion Card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Acquisition relation</strong></td>
<td>Name whether the evidence is same-subject, same-session, same-perturbation, cross-day, atlas-prior only, or post hoc cross-cohort fusion, and specify which stacks were actually acquired together.</td>
<td>The result is not read as same-subject cross-stack evidence and stays at the strongest directly supported single-stack or atlas-conditioned ceiling.</td>
</tr>
<tr>
<td><strong>Clock / lag audit</strong></td>
<td>Name the synchronization route such as LSL / TTL / photodiode / trigger lines, unresolved hardware delay and jitter, and whether timing was audited only between streams or also against device-side ground truth.</td>
<td>The result is not read as temporally aligned latent-state evidence just because the streams share timestamps.</td>
</tr>
<tr>
<td><strong>Geometry / registration scope</strong></td>
<td>Name subject-specific MRI / head model / atlas use, parceling or voxel alignment, whether co-registration is same-brain or atlas-to-subject, and which spatial mismatch remains unresolved.</td>
<td>The result is not read as if the modalities were already in one common anatomical state space.</td>
</tr>
<tr>
<td><strong>Fusion object and model burden</strong></td>
<td>State whether fusion used Bayesian model comparison, atlas priors, joint embeddings, canonical correlation, graph fusion, or only side-by-side interpretation, separate direct observables from inferred latent variables for each stack, and, for hemodynamic stacks, disclose vascular-transfer / CVR / short-separation calibration if neural-side interpretation is attempted.</td>
<td>The result is not promoted from multimodal correlation or prior-conditioned estimation to direct state identification.</td>
</tr>
<tr>
<td><strong>Shared-vs-specific component disclosure</strong></td>
<td>Name whether the claimed effect lives in a shared cross-modal component, a modality-specific residual, or a physiology-linked/global factor; specify the decomposition or comparison logic used, and say what mismatch remains unresolved after fusion.</td>
<td>The result is not read as one shared biological state variable just because a common factor or coupled trajectory was reported.</td>
</tr>
<tr>
<td><strong>Incremental evidence over unimodal / prior-only baselines</strong></td>
<td>Report what improves relative to each unimodal stack alone and to the atlas- or prior-only baseline under the same task/state split, including whether the gain is spatial, temporal, predictive, or calibration-only.</td>
<td>The fusion step is not treated as self-justifying progress.</td>
</tr>
<tr>
<td><strong>External calibration and abstention</strong></td>
<td>Name whether validation came from stimulation, simultaneous invasive recording, same-brain co-registration, phantom/simulation, postsurgical outcome, or none, and specify where the claim ceiling and abstention boundary begin.</td>
<td>The result is not read as externally validated cross-stack state recovery.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Minimum operating rule</strong>
<p>
If this card is missing, this site reads a multimodal or atlas-prior result at the ceiling of the <strong>strongest individually supported stack</strong>, not as <strong>same-subject, cross-stack, externally calibrated state identification</strong>. An atlas prior plus one live measurement remains an atlas-conditioned measurement, not automatic state completeness. A synchronized common factor without shared-vs-specific disclosure remains fused evidence, not one solved biological state variable.
</p>
</div>
<h3 class="section-title" id="human-proxy-composition-card">Human Proxy Composition Card for living-human multi-stack claims</h3>
<div class="note-box">
<strong>2026-03-21 addendum: proxy-rich human evidence must be composed explicitly, not rhetorically</strong>
<p>
After adding the <strong>Observability Budget</strong> and the <strong>Fusion Card</strong>, one weak point still remained: several living-human proxy rows could still be listed side by side as if coverage automatically added up. The primary literature does not support that shortcut. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> provide a <strong>33-participant SV2A atlas</strong> calibrated to autoradiography, which is a cohort-level synaptic-density proxy. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> define a <strong>five-metabolite within-subject similarity graph</strong> in <strong>51 healthy adolescents</strong> with <strong>13-person site replication</strong>, not kinetic flux imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> provide <strong>7 T dynamic DMRSI kinetic maps</strong> in <strong>five healthy participants</strong>. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> provide <strong>myelin-bilayer mapping</strong> in <strong>two healthy volunteers</strong> on specialized hardware. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> provide a specialized <strong>7 T CSF-mobility route</strong> whose whole-brain rest maps were shown in <strong>20 healthy younger individuals</strong>, with driver analyses reported in <strong>11 of 24 total healthy participants</strong>. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> infer sleep-linked glymphatic clearance through <strong>older-adult crossover cohorts</strong>, an <strong>investigational wearable</strong>, and a <strong>compartmental model</strong>. These routes differ in direct observable, <strong>quantity type</strong>, time window, spatial unit, model burden, deployment maturity, and even the likely nuisance sources that can make rows move together. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed both common and divergent organization across simultaneous Ca<sup>2+</sup> and BOLD, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed tightly coupled global progressions alongside <strong>two distinct network patterns</strong> in simultaneous EEG-PET-MRI, <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that a major global fMRI mode is substantially coupled to autonomic physiology, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can coexist with opposite oxygen-metabolism changes across many cortical voxels. Therefore, this site now requires a <strong>Human Proxy Composition Card</strong> whenever multiple living-human proxy rows are used together to raise a claim ceiling.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Human Proxy Composition Card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claimed latent variable family</strong></td>
<td>Name the exact hidden-state family or maintenance-state bundle the combined rows are supposed to constrain, and specify the spatial unit and timescale of that claim.</td>
<td>A proxy bundle is not read as if it had already become one coherent state object.</td>
</tr>
<tr>
<td><strong>Proxy-row inventory and direct observables</strong></td>
<td>For each row, name the stack, direct observable, spatial unit, time window, and whether the row is a structural scaffold, regional density proxy, macro biochemical / energetic / ionic / thermal / myelin / support proxy, or perturbation-conditioned proxy.</td>
<td>Several rows are not allowed to collapse into the vague statement that “human evidence exists.”</td>
</tr>
<tr>
<td><strong>Quantity-type / common-axis compatibility</strong></td>
<td>State whether each row is a density, occupancy, rate, similarity, mobility, support-state, or perturbation-sensitivity measure; then name the explicit calibration, model, or bridge that licenses reading those rows on one shared biological axis, or say that no such common axis was established.</td>
<td>Several rows are not promoted to one validated latent coordinate or the same biological quantity.</td>
</tr>
<tr>
<td><strong>Evidence relation across rows</strong></td>
<td>State whether the rows come from the same subject, same session, same perturbation, same day, cross-day, atlas prior, or post hoc cross-cohort juxtaposition, and say explicitly which rows were never acquired together.</td>
<td>The bundle is not promoted to same-subject or same-state evidence.</td>
</tr>
<tr>
<td><strong>Measurement-model and acquisition burden</strong></td>
<td>Name the tracer / kinetic model / blood-input route, field strength, specialized hardware, scan burden, correction model, or compartment model that each row depends on, plus any small-cohort or proof-of-principle limitation.</td>
<td>A specialized or model-heavy route is not read as field-ready generic observability.</td>
</tr>
<tr>
<td><strong>Cross-row nuisance / independence audit</strong></td>
<td>State whether the apparent agreement across rows could still be explained by shared arousal / autonomic / vascular / motion / device-side factors; report any shared-vs-specific decomposition, nuisance calibration, matched-perturbation control, or explicit absence of such tests.</td>
<td>Several rows are not read as independent evidence about one target variable.</td>
</tr>
<tr>
<td><strong>Increment over the strongest single row</strong></td>
<td>Report, under matched cohort / condition or held-out evaluation when available, what the bundle adds beyond the strongest individual row under the same reading rule: reduced latent-state family, narrower ceiling, better calibration, better prediction, or none.</td>
<td>Listing multiple rows is not treated as self-justifying progress.</td>
</tr>
<tr>
<td><strong>Cross-row calibration / bridge</strong></td>
<td>Name any same-brain co-registration, invasive calibration, perturbation bridge, pharmacological challenge, or external dataset that justifies reading the rows as evidence about one shared biological variable, and say when no such bridge exists.</td>
<td>The bundle is not promoted to one externally calibrated cross-stack state measurement.</td>
</tr>
<tr>
<td><strong>Residual latent state and abstention</strong></td>
<td>List which hidden-state families still remain latent after composition, and state the exact claim ceiling that remains in force.</td>
<td>The bundle is not promoted from proxy-rich human evidence to state-complete or maintenance-complete language.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Same-session correlation is not yet same quantity</strong>
<p>
Even if several rows were acquired together, the card still asks whether they measure the same thing. A bundle that mixes <strong>SV2A density</strong>, <strong>metabolic similarity</strong>, <strong>kinetic glucose-rate imaging</strong>, <strong>CSF mobility</strong>, and <strong>clearance-efflux modeling</strong> does not yet define one common state axis by default, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that even hemodynamic and oxygen-metabolism rows can move in opposite directions. Therefore, same-session alignment or positive correlation is not enough on this site unless the paper discloses the quantity bridge explicitly.
</p>
</div>
<div class="note-box">
<strong>Minimum operating rule</strong>
<p>
If this card is missing, this site reads a living-human proxy bundle at the ceiling of the <strong>strongest individually supported row</strong>, or at most as <strong>proxy-rich but ceiling-limited human evidence</strong>. It is not promoted to <strong>same-subject, cross-stack, externally calibrated state identification</strong>.
</p>
</div>
<div class="note-box">
<strong>Promotion rule beyond row diversity</strong>
<p>
On this site, row diversity alone is not enough. A bundle is promoted only when the paper discloses whether the apparent agreement survives a <strong>shared-driver audit</strong> and what the bundle adds beyond the <strong>strongest single row</strong> under a matched-condition reading. Otherwise, the result remains <strong>proxy-rich but ceiling-limited</strong> rather than same-subject state identification.
</p>
</div>
<h3 class="section-title" id="state-continuity-bridge-card">State-Continuity Bridge Card for sequential cross-regime claims</h3>
<div class="note-box">
<strong>2026-03-21 addendum: same-subject is not enough when the bridge itself is sequential</strong>
<p>
After adding the <strong>Fusion Card</strong>, the <strong>Human Proxy Composition Card</strong>, and the <strong>Destructive-Structure Route Card</strong>, one weak point still remained: a result could still be described as <strong>same-subject</strong> or <strong>same-brain</strong> even when the claim depended on bridging across live measurement, later fixation, ex vivo follow-up, or cross-day reacquisition as if those stages sampled one latent state. The primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that preservation route and fixation time course alter extracellular-space retention and geometry. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a> showed that bridging in vivo two-photon physiology to synchrotron microtomography and serial block-face EM requires a multistage landmark-based correlative workflow. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> showed that same-brain function plus EM remains a <strong>sequential local pipeline</strong>, not simultaneous whole-state capture. <a href="https://doi.org/10.1038/nature14467" target="_blank">Attardo et al. (2015)</a> further showed that adult CA1 spine lifetimes are on the order of <strong>1-2 weeks</strong>, so relaxed bridge windows cannot be treated as silent continuity. Therefore, this site now requires a <strong>State-Continuity Bridge Card</strong> whenever a claim depends on treating measurements from different acquisition regimes as one latent-state sample.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>State-Continuity Bridge Card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bridge target and acquisition order</strong></td>
<td>Name which stacks were linked, in which order, and which claim depends on that bridge: for example live imaging -&gt; fixation -&gt; ex vivo EM, same-day live stack A -&gt; live stack B, or cross-day reacquisition.</td>
<td>A multi-stage workflow is not read as one state object by default.</td>
</tr>
<tr>
<td><strong>Elapsed time and state window</strong></td>
<td>Report the delay between acquisitions or between live physiology and fixation, whether the bridge stayed within one trial / session / day / sleep cycle or crossed days, and which hidden-state families could drift over that interval.</td>
<td><strong>Same-subject</strong> is not read as <strong>same-time</strong> or <strong>same-state</strong>.</td>
</tr>
<tr>
<td><strong>Physiological / perturbation regime continuity</strong></td>
<td>Name whether task, arousal, anesthesia, deprivation, pharmacology, and behavioral context were matched, intentionally shifted, or left unmatched across the bridge.</td>
<td>A bridge is not read as if calibration transfers automatically across state regimes.</td>
</tr>
<tr>
<td><strong>Coordinate transfer and deformation model</strong></td>
<td>Name fiducials, vascular landmarks, subject-specific MRI, warping or shrinkage correction, manual versus automated matching, and which spatial mismatch remains unresolved.</td>
<td><strong>Same-brain</strong> is not read as cell-precise or deformation-free correspondence.</td>
</tr>
<tr>
<td><strong>Bridge validation rung</strong></td>
<td>Name what validates the bridge itself: repeated live measurement, vascular / cellular landmark recovery, stimulation-site correspondence, histology recovery, or no external validation.</td>
<td>The bridge is not promoted to externally validated same-state evidence.</td>
</tr>
<tr>
<td><strong>Residual drift, omitted state families, and ceiling</strong></td>
<td>List which latent-state families could still change across the bridge, including synaptic efficacy, excitability, neuromodulatory context, support-state, and structural turnover where relevant, then declare the remaining claim ceiling and abstention boundary.</td>
<td>The result is not promoted to same-state cross-regime reconstruction, maintenance-consistent language, or state-complete readout.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Minimum operating rule</strong>
<p>
If this card is missing, this site reads a sequential cross-regime result at the ceiling of the <strong>strongest directly supported live or destructive stage</strong> plus, at most, an <strong>unvalidated bridge hypothesis</strong>. It is not promoted to <strong>same-state</strong>, <strong>same-time</strong>, or <strong>maintenance-consistent</strong> evidence.
</p>
</div>
<div class="note-box">
<strong>Need the longer bridge critique?</strong>
<p>
For the background logic behind preservation change, cross-day regime mismatch, bridge-validation rungs, and card stacking, see <a href="wiki/state-continuity-bridge.html">Wiki: State-Continuity Bridge</a>.
</p>
</div>
<h3 class="section-title" id="destructive-structure-card">Destructive-Structure Route Card for ultrastructure claims</h3>
<div class="note-box">
<strong>2026-03-20 addendum: destructive ultrastructure routes need their own card</strong>
<p>
The remaining weakness after the <strong>Observability Budget</strong> and <strong>Fusion Card</strong> was that words such as <strong>nanoscale</strong>, <strong>petascale</strong>, or <strong>same-brain</strong> could still be overread as if the destructive route had already preserved native state, solved scaling, and certified reconstruction quality in one move. The primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that conventional aldehyde fixation collapses extracellular space, that fixation itself has a non-negligible time course, and that even high-pressure freezing preserves extracellular space only in samples thinner than about <strong>200 μm</strong>. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> then showed that extraordinary human ultrastructure can now be reconstructed, but still from a rapidly preserved <strong>1.05 mm<sup>3</sup></strong> surgical fragment with <strong>1.8 PB</strong> raw data and <strong>326 days</strong> of imaging. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> showed that same-brain function plus EM is a <strong>sequential local pipeline</strong>, with in vivo two-photon imaging first and fixation / sectioning / ex vivo EM afterward, producing about <strong>2 Pb</strong> of raw data over about <strong>6 months</strong>. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> further showed that even the adult-fly whole-brain frontier still depended on proofreading, thresholding, and about <strong>33 person-years</strong> of manual correction. Therefore, this site now asks destructive ultrastructure claims to attach a <strong>Destructive-Structure Route Card</strong> instead of letting resolution language silently stand in for native-state completeness.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Destructive-Structure Card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Preservation route and live-to-fix window</strong></td>
<td>Name immersion / perfusion / cryo route, the interval from live physiology or resection to fixation/freezing, whether extracellular-space preservation was audited, and any osmotic / staining manipulations that materially shape ultrastructure.</td>
<td>The result is not read as if native geometry or microenvironment were automatically preserved by the word <code>EM</code> or <code>nanoscale</code>.</td>
</tr>
<tr>
<td><strong>Sample origin and physiological regime</strong></td>
<td>Name species, brain region, whether the tissue was ex vivo surgical, acute slice, perfusion-fixed animal, or same-brain postmortem follow-up to in vivo recording, and what behavioural / state regime was actually sampled before fixation.</td>
<td>A local or pathology-bounded fragment is not promoted to a generic living-brain state claim.</td>
</tr>
<tr>
<td><strong>Registration scope to live data</strong></td>
<td>Name whether registration is none, atlas-level, same-brain structural, same-brain functional, or same-perturbation; state which correspondences were manual versus automated and which mismatch remains unresolved.</td>
<td><strong>Same-brain</strong> is not read as <strong>same-time whole-state capture</strong>.</td>
</tr>
<tr>
<td><strong>Sectioning / imaging scale and loss audit</strong></td>
<td>Report imaged volume, section count, voxel size, acquisition time, section loss / folds / cracks, whether multiple subvolumes had to be stitched, and where tissue was omitted or alignment deemed insufficient.</td>
<td>A petascale stack is not read as operationally complete or whole-brain-ready by default.</td>
</tr>
<tr>
<td><strong>Segmentation / proofreading status</strong></td>
<td>Name automated segmentation family, merge / split trade-offs, proofreading scope, released versions, attachment / completeness metrics when available, and which analyses depend on thresholds or proofread subsets.</td>
<td>A polished reconstruction is not read as error-free ground truth.</td>
</tr>
<tr>
<td><strong>Omitted live-state families and ceiling</strong></td>
<td>Explicitly list which current-state families remain absent, including current synaptic efficacy, neuromodulatory context, ionic milieu, glial / metabolic support, phospho-signaling, and other maintenance-state variables; then declare the claim ceiling and abstention boundary.</td>
<td>The result is not promoted from <strong>structural scaffold</strong> or <strong>local ex vivo scaffold</strong> to native-state capture, maintenance-consistent readout, or sufficient-condition language for WBE.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-18 addendum: ESI validation is a ladder, not one checkbox</strong>
<p>
This site no longer accepts the phrase <strong>external validation</strong> without naming the validation class. Simulation / phantom audits solver behavior under known generative conditions, intracranial stimulation audits localization error to a known site and time (<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al., 2020</a>; <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al., 2023</a>), simultaneous invasive recording audits concordance under the same event (<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al., 2025</a>), and postsurgical outcome audits clinical relevance rather than direct source ground truth (<a href="https://doi.org/10.1016/j.nicl.2014.06.005" target="_blank">Birot et al., 2014</a>). Passing one rung does not auto-pass the others.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Validation class</th>
<th>What it constrains</th>
<th>Ceiling if only this exists</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Simulation / phantom</strong></td>
<td>Numerical stability, geometry sensitivity, and regression under known conditions.</td>
<td>Method-behavior evidence, not living-brain ground truth.</td>
</tr>
<tr>
<td><strong>Intracranial stimulation</strong></td>
<td>Localization error to a known site and time under fixed geometry.</td>
<td>Strong calibration for source error, but not spontaneous-dynamics or universal deep-source guarantees.</td>
</tr>
<tr>
<td><strong>Simultaneous invasive recording</strong></td>
<td>Concordance with concurrent SEEG/ECoG during the same event.</td>
<td>Cohort- and pathology-bounded concordance, not unique recovery of internal state.</td>
</tr>
<tr>
<td><strong>Postsurgical outcome</strong></td>
<td>Clinical relevance to resection or seizure-onset-zone workflow.</td>
<td>Decision-support evidence, not source ground truth.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-19 addendum: ESI claims need a solver-disagreement audit</strong>
<p>
The remaining weakness was to let one inverse solution stand in for the whole solution set. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.076" target="_blank">Mahjoory et al. (2017)</a> showed that inverse-method and software-package choice induces considerable variability and explicitly recommended verifying EEG source findings with more than one source-imaging procedure. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a> then showed on intracranial-stimulation ground truth that only a small fraction of tested solutions reached the session-wise optimum, even though the benchmark was tightly controlled. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> further showed that skull and skin conductivity uncertainty shifts reconstructed depth and location, especially for quasi-tangential sources. Therefore, when an anatomical source claim depends on one inverse family or one hand-picked parameter set, this site now asks for a <strong>solver-disagreement audit</strong> that reports compared solver families / packages, parameter window, and headline-location spread. If that is missing, the result stays at the <strong>method-sensitive source-hypothesis</strong> level rather than stable anatomical evidence.
</p>
</div>
<div class="note-box">
<strong>2026-03-22 addendum: ESI claims need a field-formation audit</strong>
<p>
The remaining weakness was upstream of the inverse solver itself. A paper can report a cleaner map, a lower benchmark error, or better regularization and still leave unasked whether the targeted source class was expected to generate a usable scalp field in the first place. <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a> showed with realistic tissue boundaries that source orientation matters far more for MEG than for EEG, with median lowest-to-highest sensitivity ratios of <strong>0.06</strong> for MEG and <strong>0.63</strong> for EEG. <a href="https://doi.org/10.1002/hbm.20851" target="_blank">Ahlfors et al. (2010)</a> and <a href="https://doi.org/10.1002/hbm.20571" target="_blank">Goldenholz et al. (2009)</a> showed that extended sources, cortical folding, and cancellation can materially reshape or suppress surface signals, while <a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al. (2021)</a> showed that omitting the <strong>CSF compartment</strong> overestimates EEG SNR and changes cortical / subcortical sensitivity comparisons. Therefore, when a submission claims deep-source recovery or anatomical improvement from EEG/MEG, this site now asks for a <strong>field-formation audit</strong> before the inverse result is read strongly.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Field-formation audit field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Target source class and expected extent</strong></td>
<td>Name the target generator family, its expected depth and orientation regime, whether the source is treated as focal or extended, and the synchrony / timescale assumed to make it visible.</td>
<td>A success on one benchmark is not promoted to generic deep-source observability.</td>
</tr>
<tr>
<td><strong>Geometry / cancellation sensitivity</strong></td>
<td>State whether cortical folding, opposing-bank cancellation, or source-extent effects were assessed for the target, and provide a sensitivity / SNR map or equivalent justification when anatomical visibility is central to the claim.</td>
<td>A missing or weak scalp signal is not read as source absence, and a visible scalp pattern is not read as unique state recovery.</td>
</tr>
<tr>
<td><strong>Head-model / tissue visibility assumptions</strong></td>
<td>Name the compartments and conductivity assumptions in the forward model, including whether CSF was modeled and whether uncertainty in skull / tissue parameters was tested.</td>
<td><strong>High-density</strong> or <strong>MRI-informed</strong> is not read as visibility-complete by default.</td>
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
<strong>2026-03-22 addendum: tractography connectomes need a tractography route card</strong>
<p>
For diffusion-MRI-derived connectomes, the modality label alone is not enough. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">Reveley et al. (2015)</a> showed that superficial white matter can block long-range tracking from roughly half of the cortical surface, <a href="https://doi.org/10.1002/hbm.23936" target="_blank">Schilling et al. (2018)</a> showed that tractography endpoints are biased toward gyral crowns across deterministic and probabilistic algorithms and even very high-resolution data, <a href="https://doi.org/10.1016/j.neuroimage.2023.120376" target="_blank">Sarwar et al. (2023)</a> showed that filtering gains are modest in complex human-like architectures, <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">He et al. (2024)</a> showed that filtering can significantly shift laterality indices for more than 10% of connections, <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">Gajwani et al. (2023)</a> showed across <strong>40 pipelines</strong> and <strong>44</strong> group-representative reconstructions that hub location is highly variable and hub connectivity correlates with regional surface area in <strong>69%</strong> of assessed pipelines, <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">McMaster et al. (2025)</a> showed that voxel size changes the resulting connectome and recommended resampling to <strong>1 mm isotropic</strong> for robust comparisons, <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">Manzano-Patrón et al. (2025)</a> made fibre-orientation uncertainty explicit rather than silent, and <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">Zhu et al. (2025)</a> improved tractography by fusing MRI with microscopy. Therefore, this site now asks any tractography-derived connectome claim to attach a <strong>tractography route card</strong> naming what was directly measured, how cortical endpoints were assigned, which priors, filtering, parcellation, and weighting choices shaped the graph, how uncertainty and resolution sensitivity were quantified, what external calibration exists, and where abstention begins. The longer public reading rule is summarized in <a href="wiki/connectome-is-not-enough.html#tractography-route-card">Wiki: tractography route card</a>.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Tractography route-card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Direct observables</strong></td>
<td>Write voxel size, shell / b-value scheme, orientation model, and state explicitly that the direct observable is diffusion signal / local fibre-orientation estimate.</td>
<td>The streamline graph is not read as directly observed edges.</td>
</tr>
<tr>
<td><strong>Cortical endpoint / surface-bias audit</strong></td>
<td>Name the white-matter / gray-matter boundary or surface-assignment route, whether superficial-white-matter or gyral-bias checks were performed, and which cortical territory remained endpoint-limited.</td>
<td>Cortical endpoint differences are not read as anatomical absence or edge specificity by default.</td>
</tr>
<tr>
<td><strong>Priors and filtering</strong></td>
<td>Write seeding rule, deterministic / probabilistic mode, start / end / exclusion ROIs, atlas constraints, stopping rules, and filtering / weighting method.</td>
<td>Prior-driven bundle recovery is not read as unbiased connectome discovery.</td>
</tr>
<tr>
<td><strong>Graph construction choices</strong></td>
<td>Name the parcellation / surface atlas, edge definition and weighting, density or threshold rule, and whether the headline metric survives reasonable alternative graph constructions.</td>
<td>Hub maps and graph metrics stay pipeline-conditioned rather than anatomical network organization.</td>
</tr>
<tr>
<td><strong>Uncertainty and stability</strong></td>
<td>Report resolution sensitivity, scan-rescan or ensemble stability, and posterior / bootstrap uncertainty for the headline graph metric.</td>
<td>Reported connectome differences stay pipeline-conditioned rather than anatomical by default.</td>
</tr>
<tr>
<td><strong>External calibration and ceiling</strong></td>
<td>Name any tracer / histology / microscopy / phantom route and declare the ceiling as macro pathway prior, targeted bundle hypothesis, or calibrated bundle comparison.</td>
<td>The result is not promoted to edge-complete graph or WBE-ready connectome language.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-19 addendum: connectome-constrained predictors need a conditional-model route card</strong>
<p>
For connectome-constrained neural predictors, the label alone is also not enough. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">Lappalainen et al. (2024)</a> showed that connectome structure plus task optimization can yield rich fly visual-system activity predictions, but the model still depended on partial motion-pathway reconstruction, simplified neuron/synapse dynamics, and an ensemble of multiple local optima. <a href="https://doi.org/10.1038/s41586-024-07763-9" target="_blank">Shiu et al. (2024)</a> showed that synapse-level connectivity plus neurotransmitter identity can predict specific fly sensorimotor circuits, while explicitly reading the result as a coarse description of named behaviours. <a href="https://doi.org/10.1038/s41586-024-07982-0" target="_blank">Pospisil et al. (2024)</a> used the connectome as a prior for perturbation-based effect estimation, but explicitly recovered a linear approximation to nonlinear dynamics. Finally, <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that even with the same synaptic weights, different biophysical parameters can still generate divergent recurrent dynamics. Therefore, this site now asks any connectome-constrained model claim to attach a <strong>conditional-model route card</strong> naming what structure was actually used, what remained fitted, which regime was tested, which mechanisms were omitted, how validation was done, and where abstention begins. The longer public reading rule is summarized in <a href="wiki/connectome-is-not-enough.html#conditional-predictor-route-card">Wiki: conditional-model route card</a>.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Conditional-model route-card field</th>
<th>Minimum disclosure</th>
<th>What this site stops claiming if absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Structural prior and coverage</strong></td>
<td>Name whether the model used EM edges, synapse counts, neurotransmitter signs, same-brain recordings, tractography priors, atlas averages, periodic tiling, and the exact spatial/cell-type coverage.</td>
<td>The result is not read as if the relevant circuit or state variables had been fully observed.</td>
</tr>
<tr>
<td><strong>Fitted degrees of freedom</strong></td>
<td>List the still-learned quantities such as time constants, resting potentials, unitary synapse strengths, decoder weights, gain functions, or Jacobian entries around the operating point.</td>
<td>“Connectome-constrained” is not read as direct state measurement.</td>
</tr>
<tr>
<td><strong>Task/state regime and omitted mechanisms</strong></td>
<td>Name the stimulus/behaviour/state regime, held-out/OOD slices, and omitted or frozen mechanisms such as electrical synapses, neuromodulation, glia, plasticity, or body/environment loops.</td>
<td>Task-bounded success is not promoted to arbitrary-task, whole-brain, or maintenance-complete competence.</td>
</tr>
<tr>
<td><strong>Validation, uncertainty, and ceiling</strong></td>
<td>Name whether validation came from held-out activity, same-brain physiology, perturbation, behaviour, or only task loss; then expose ensemble spread / alternative families and declare the ceiling.</td>
<td>The result is not promoted to unique internal-state recovery or general mechanistic solution.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this card is missing, this site treats the result as <strong>L0/L1 reproducible analysis or limited decode</strong> and does not promote it to L2 or above. For example, the default ceiling is <strong>macro-state tracking</strong> for <strong>EEG / HD-EEG + MRI only</strong>, <strong>an implant-region local population window</strong> for <strong>high-density extracellular probe only</strong>, <strong>structural scaffold</strong> for <strong>volume EM only</strong>, <strong>local ex vivo scaffold</strong> for <strong>human ultrastructure without a destructive-structure route card</strong>, <strong>molecular / spatial prior</strong> for <strong>whole-brain atlas only</strong>, and still only <strong>local conditional prediction</strong> even for <strong>same-brain calcium + EM</strong>. For inverse or model-based claims, a submission without an <strong>Identifiability Card</strong> is not accepted here as <strong>unique internal-state recovery</strong> and remains at the predictive / localization / model-conditioned ceiling even if its observability class improved. For living-human multi-stack proxy claims, a submission without a <strong>Human Proxy Composition Card</strong> is not accepted here as <strong>same-subject cross-stack state identification</strong> and remains at the <strong>strongest single-route</strong> or <strong>proxy-rich but ceiling-limited</strong> level. For sequential cross-regime claims, a submission without a <strong>State-Continuity Bridge Card</strong> is not accepted here as <strong>same-state evidence</strong> and remains at the <strong>strongest directly supported stage</strong> plus an unvalidated bridge. For hemodynamic modalities, a group or cross-day BOLD / fNIRS difference without <strong>vascular-state / CVR</strong> or <strong>short-separation / superficial-bias</strong> audit is not accepted here as a neural difference. For diffusion-MRI tractography, a connectome claim without a <strong>tractography route card</strong> is not accepted here as an edge-complete graph and remains at the <strong>macro pathway prior / targeted bundle hypothesis</strong> ceiling. For connectome-constrained predictors, a model claim without a <strong>conditional-model route card</strong> remains at the <strong>conditional hypothesis engine / task-bounded predictor</strong> ceiling and is not accepted here as unique internal-state recovery. If a chronic-probe result lacks a unit-identity audit, single-unit longitudinal claims are not accepted. Detailed stack-specific ceilings and the <strong>state variable × timescale</strong> matrix are summarized in <a href="wiki/measurement-stack-and-claim-ceiling.html#state-variable-matrix">Wiki: observability and claim ceiling by measurement stack</a>.
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
<td><strong>Post-transcriptional RNA-state</strong></td>
<td>Disclose whether splice-isoform ratios, RNA-editing state, m6A modification / reader route, or isoform-resolved long-read assay was directly measured, causally perturbed, externally calibrated, or replaced by gene-level abundance alone, and state which downstream object the paper actually constrained.</td>
<td>Isoform-specific receptor composition, m6A-dependent translation / degradation, and editing-dependent plasticity claims remain latent.</td>
</tr>
<tr>
<td><strong>Phospho-signaling / second-messenger state</strong></td>
<td>Disclose whether phosphosite occupancy, kinase/phosphatase balance, cAMP/Ca<sup>2+</sup>/PKA nanodomain state, or phospho-proteomic route was directly measured, causally perturbed, externally calibrated, or silently replaced by transcript/protein abundance alone.</td>
<td>Phosphosite-dependent plasticity, signaling-gate, and nanodomain-controller claims remain latent.</td>
</tr>
<tr>
<td><strong>Local proteostasis / synaptic-tagging route</strong></td>
<td>Disclose the claim family (tag / capture, branch-level integration, synthesis-degradation balance, autophagy-linked remodeling, turnover-resistant persistence, or proteasome-capacity intervention), the integrative unit, the direct observable, the turnover window, the perturbation route, and whether any human route is externally calibrated or remains latent.</td>
<td>Late stabilization, reconsolidation, cross-event capture, or turnover-resistant persistence do not become closed mechanisms.</td>
</tr>
<tr>
<td><strong>Cargo-transport / cytoskeletal trafficking route</strong></td>
<td>Disclose the <strong>claim family</strong> (postsynaptic receptor delivery, activity-dependent vesicle confinement, learning-dependent microtubule-state gate, axonal RNA localization / transport-granule route, or presynaptic cargo retention), the <strong>cargo object</strong>, the <strong>compartment scope</strong>, the <strong>transport phase / state variable</strong>, the <strong>trigger / time window</strong>, the <strong>direct observable</strong>, and whether the strongest human-facing evidence is still limited to a narrow preparation or no human route at all.</td>
<td>Compartment-specific stabilization, receptor localization, synaptogenesis, and branch-level maintenance claims remain latent.</td>
</tr>
<tr>
<td><strong>Ionic milieu / chloride homeostasis</strong></td>
<td>Attach an ionic / chloride route card that states the <strong>claim family</strong> (chloride-set-point / E<sub>GABAA</sub> tuning, transporter-state regulation, interstitial-ion state switching, perisynaptic K<sup>+</sup> clearance, pathology route, or human macro ionic proxy), the <strong>direct ionic observable</strong>, the <strong>spatial regime</strong>, the <strong>perturbation / controller route</strong>, and whether the strongest human-facing evidence is pathology tissue, CSF ion assay, sodium MRI proxy, or no human route at all.</td>
<td>Inhibitory polarity, rhythm stability, and state-transition claims stay provisional or fall back to coarse excitability proxies.</td>
</tr>
<tr>
<td><strong>Shared extracellular / electrical state</strong></td>
<td>Attach an electrical-state route card that states the <strong>claim family</strong> (gap-junction coupling network, endogenous-field / ephaptic route, inhibitory driving-force regime, activity-dependent electrical-synapse remodeling, or human perturbation-conditioned clue), the <strong>direct electrical observable</strong>, the <strong>spatial regime</strong>, the <strong>perturbation / calibration route</strong>, and whether the strongest human-facing evidence is a direct local preparation, a specialized optical assay, a pharmacological perturbation clue, or no human route at all.</td>
<td>Fast synchrony, oscillatory coordination, spindle / slow-oscillation coupling, and electrotonic-regime claims stay provisional or fall back to chemical-connectome-plus-proxy language.</td>
</tr>
<tr>
<td><strong>Timing-state / conduction support</strong></td>
<td>Separate device latency from biological timing-state, and disclose whether timing variables were measured, externally calibrated, absorbed into a constant, or left latent.</td>
<td>Phase, synchrony, and timing-complete reconstruction claims are demoted to hardware-fast or macro-timing proxy claims.</td>
</tr>
<tr>
<td><strong>Neuromodulatory specificity</strong></td>
<td>Disclose whether the route was a mixed arousal proxy, local axon / transmitter sensor, receptor / transporter atlas, occupancy PET, or release-sensitive displacement PET; then report receptor family, tracer / ligand, occupancy-versus-displacement design, challenge or administered drug plus dose when applicable, arterial-versus-reference quantification route, kinetic or simplified model, temporal window, spatial scope, partial-volume handling when relevant, and abstention boundary.</td>
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
The latent-state error budget is not a second abstract. It is a <strong>submission-side stop-rule table</strong>. If a paper adds one extra evidence layer, such as transcriptomics, SV2A PET, receptor / transporter atlas priors, occupancy PET, release-sensitive displacement PET, myelin imaging, or a glial perturbation, it should say <strong>which error term that layer reduces under the same held-out condition</strong> and which latent families remain untouched. This is the site-wide rule behind the augmentation / ablation logic in <a href="#state-completeness-gate">State variable integrity gate</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-22 addendum: neuromodulatory evidence also needs a route card</strong>
<p>
On this site, <strong>mixed arousal proxy</strong>, <strong>local transmitter sensor</strong>, <strong>receptor / transporter atlas</strong>, <strong>occupancy PET</strong>, and <strong>release-sensitive displacement PET</strong> are not treated as equivalent. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> showed that pupil fluctuations track both adrenergic and cholinergic activity, <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> showed that local cortical ACh depends on axon activity and local clearance, <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> and <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">Goulas et al. (2021)</a> showed that receptor maps are structured regional priors, <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> showed selected D<sub>2</sub>-receptor target engagement by an administered drug, and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, and <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> showed challenge- and window-limited dopamine or serotonin release proxies. Therefore, submissions that depend on neuromodulation now have to state not only <strong>which rung</strong> was used, but also the <strong>claim family</strong>, <strong>transmitter axis / receptor family</strong>, <strong>direct observable</strong>, <strong>challenge or administered-drug route</strong>, <strong>time window / model burden</strong>, and <strong>abstention boundary</strong> before any claim ceiling is raised. The longer public rule is in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#neuromodulatory-route-card">Wiki: neuromodulatory route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: PET-based evidence is unreadable without the measurement model</strong>
<p>
For PET-based routes, naming the modality is still too coarse. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a> showed for human SV2A PET that the quantification route depends on metabolite-corrected arterial input, reference-region choice, compartment model, and scan window. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">Smart et al. (2021)</a> showed that [<sup>11</sup>C]UCB-J binding measures stay unchanged during brief visual activation despite blood-flow-driven influx changes, so synaptic-density PET should not be read as momentary synaptic efficacy. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> showed that receptor atlas is built from group-average PET maps from more than 1,200 healthy individuals, <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> quantified occupancy for an administered antipsychotic, and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, and <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> used challenge-linked binding changes as displacement-based release proxies. This site therefore requires tracer, occupancy-versus-displacement design, challenge or administered drug plus dose when applicable, quantification route, model/window, and partial-volume handling where relevant before any PET-based claim ceiling is interpreted.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: synaptic-density PET is not one audit item</strong>
<p>
SV2A PET now gets its own route-card logic on this site. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a> fixes tracer and quantification burden, <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> is a healthy-human atlas, <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">Shatalina et al. (2024)</a> is a task / cognition association study, <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">Smart et al. (2021)</a> shows that brief activation does not produce a momentary SV2A state readout, and <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">Holmes et al. (2022)</a> shows that rapid ketamine response need not imply measurable SV2A change at 24 h. Therefore, submissions that cite synaptic-density PET must state whether the paper is an <strong>atlas</strong>, <strong>disease / risk contrast</strong>, <strong>task / cognition association</strong>, <strong>intervention / target-engagement design</strong>, or something narrower, and must disclose tracer, quantification route, anatomy / partial-volume handling, and abstention boundary before the claim ceiling is raised. The longer route is <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#sv2a-route-card">Wiki: SV2A / synaptic-density PET route card</a>.
</p>
</div>
</section>

<section class="section" id="maintenance-state-error-budget">
<h2 class="section-title">Maintenance-state error budget</h2>
<p>
Cross-day and remote-memory claims fail for a different reason than same-session decoding claims. Even when short-term performance holds, the result may still leave the <strong>maintenance route</strong> almost completely latent. This site therefore asks cross-day, recovery, reconsolidation, or remote-memory submissions to disclose a <strong>maintenance-state error budget</strong> that keeps controller state, post-transcriptional RNA-state, phospho-signaling / second-messenger state, sleep history, sleep architecture / replay-coupling state, timing support, thermal-state, bioenergetic / mitochondrial support, glial / astrocyte support, and other multiday support-state proxies separate.
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
<td><strong>Post-transcriptional RNA-state</strong></td>
<td>Report whether isoform ratios, m6A-dependent translation / degradation routes, RNA-editing ratios, or only gene-level transcript counts were available, and which assay or perturbation established the relevant RNA-state.</td>
<td>Cross-day stabilization, receptor-composition carryover, and editing-dependent maintenance claims are not promoted to RNA-state-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Phospho-signaling / second-messenger state</strong></td>
<td>Report <strong>claim family</strong> (phosphosite gate, kinase/phosphatase controller, compartmentalized second-messenger routing, region-structured phosphoproteome atlas, or phospho-mutant causal edit), the <strong>assay / direct observable</strong>, <strong>spatial or compartment scope</strong>, <strong>timing window</strong>, <strong>causal leverage</strong>, and whether only transcript/protein abundance was available.</td>
<td>Cross-day stabilization, phosphosite-dependent capture, and signaling-gate claims are not promoted to phospho-state-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Sleep / wake history</strong></td>
<td>Report sleep / wake interval, deprivation, nap / recovery condition, and the time window over which renormalization was or was not checked.</td>
<td>Cross-day hold is not promoted to overnight maintenance or post-learning re-equilibration.</td>
</tr>
<tr>
<td><strong>Sleep architecture / replay-coupling state</strong></td>
<td>Report stage composition, event definition, cue / stimulation timing policy, and, when relevant to consolidation claims, which slow-oscillation / spindle / ripple or targeted-memory-reactivation coupling measures were available, which were only proxy-estimated, and which replay-timing variables remained latent.</td>
<td>A night with sleep, a delivered cue, or average overnight gain is not promoted to replay-consistent or consolidation-mechanism evidence.</td>
</tr>
<tr>
<td><strong>Timing support</strong></td>
<td>Separate hardware latency from tissue-side timing support such as myelin / conduction proxy or externally calibrated timing-state.</td>
<td>Hardware-fast remains hardware-fast; it does not become timing-complete maintenance evidence.</td>
</tr>
<tr>
<td><strong>Thermal-state</strong></td>
<td>Attach a thermal route card that states the claim family, direct thermal observable, spatial / preparation regime, driver / perturbation route, time window, function target, and whether the evidence is local physiology, a field-potential confound audit, a device-heating artifact, a brain-state proxy, or only a human macro thermometry / task-linked thermal mapping route. Also disclose what microtemperature gradients, synapse-specific heating burden, thermal-controller variables, or local thermal sensitivities remained latent.</td>
<td>Field-potential amplitude, membrane-kinetic, rhythm-state, and sequence-timing claims are not promoted to thermal-state-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Ionic / chloride state</strong></td>
<td>Attach an ionic / chloride route card that states the claim family, direct ionic observable, spatial regime, perturbation / controller route, function target, and whether the evidence is local physiology, pathology tissue, CSF ion assay, sodium MRI proxy, or only a coarse external calibrator. Also disclose what chloride microdomains, transporter balance, perisynaptic K<sup>+</sup> handling, or local E<sub>GABAA</sub> variables remained latent.</td>
<td>Cross-day or recovery success is not promoted to inhibitory-polarity-consistent or state-transition-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Shared extracellular / electrical state</strong></td>
<td>Attach an electrical-state route card that states the claim family, direct electrical observable, spatial regime, perturbation / calibration route, function target, and whether the evidence is a gap-junction preparation, an endogenous-field / ephaptic perturbation, a direct inhibitory-driving-force assay, an activity-dependent electrical-synapse remodeling experiment, or only a human perturbation-conditioned clue. Also disclose what local coupling topology, extracellular-field geometry, inhibitory reversal / shunt regime, or state-switch thresholds remained latent.</td>
<td>Cross-day or recovery success is not promoted to electrical-state-consistent synchrony, oscillation, or spindle / slow-oscillation coordination evidence.</td>
</tr>
<tr>
<td><strong>Bioenergetic / mitochondrial support</strong></td>
<td>Attach a bioenergetic / mitochondrial route card that states the claim family, compartment, direct energetic observable, quantity type / model burden, function target, and whether the evidence is a local mechanism, a metabolic-tuning intervention, or only a human macro energetic proxy. Also disclose what local ATP reserve, mitochondrial positioning, fission/fusion, Ca<sup>2+</sup>-efflux control, or redox variables remained latent.</td>
<td>Repeated-stimulation reliability and energetic mechanisms of dendritic plasticity remain provisional.</td>
</tr>
<tr>
<td><strong>Cargo-transport / cytoskeletal trafficking support</strong></td>
<td>Attach a cargo-transport route card that states the claim family, cargo object, compartment scope, transport phase / state variable, trigger / time window, direct observable, causal leverage, and whether the evidence is only a narrow culture preparation or no human route at all. Also disclose which branch / spine / bouton destinations, motor states, or cargo classes remained latent.</td>
<td>Cross-day stabilization, synaptogenesis, and compartment-delivery claims are not promoted to transport-consistent maintenance evidence.</td>
</tr>
<tr>
<td><strong>Glial / astrocyte support</strong></td>
<td>Write whether the route is lactate-shuttle support, astrocyte network / ensemble state, fear-state representation, human MAO-B / reactive-astrogliosis PET, glial metabolic proxy, or only a macro support proxy, and name the species / region / timescale when rodent causal evidence is being used as support.</td>
<td>Memory retrieval, reconsolidation, multiday stabilization, and fear-state support remain partial-model claims.</td>
</tr>
<tr>
<td><strong>Clearance / immune support</strong></td>
<td>Report whether meningeal-lymphatic, CSF-interstitial, microglia-related, or sleep-linked clearance measurements were available, what part remained only a macro proxy, and what cell-specific controller remained unobserved.</td>
<td>Multiday recovery, protein-clearance, and synaptic-maintenance claims remain support-proxy claims rather than local maintenance-state claims.</td>
</tr>
<tr>
<td><strong>Human evidence class / observability ceiling</strong></td>
<td>Label each human-side route as <strong>structural scaffold</strong>, <strong>regional density proxy</strong>, <strong>macro biochemical / energetic / ionic / thermal / myelin / support proxy</strong>, or <strong>perturbation-conditioned proxy</strong>, then state its <strong>operational maturity</strong> and <strong>calibrator role</strong>, meaning which hidden-state family it safely constrains and which local states still remain latent. If the route is PET-based, also name the tracer, quantification model or validated scan window, and whether partial-volume correction or atlas calibration was used. If the route is MRSI-based, also name the <strong>metabolite set</strong>, <strong>parceling unit</strong>, <strong>resolution plus PSF / partial-volume correction</strong>, <strong>water / lipid handling</strong>, <strong>spectral QC thresholds</strong>, and whether the claim is <strong>static similarity</strong> or <strong>kinetic rate imaging</strong>. If several living-human routes are combined, also attach a <a href="#human-proxy-composition-card">Human Proxy Composition Card</a>.</td>
<td>Human proxy bundles are not promoted to state-complete maintenance snapshots.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-18 addendum: sleep history is not sleep architecture</strong>
<p>
<a href="https://doi.org/10.1016/j.neuron.2013.03.006" target="_blank">Ngo et al. (2013)</a> showed in humans that in-phase slow-oscillation stimulation enhances spindle coupling and memory whereas out-of-phase stimulation does not, <a href="https://doi.org/10.1038/nn.4304" target="_blank">Maingret et al. (2016)</a> and <a href="https://doi.org/10.1016/j.neuron.2017.06.025" target="_blank">Latchoumane et al. (2017)</a> showed in rodents that fine-tuned slow-oscillation / spindle / ripple coordination causally supports consolidation, <a href="https://doi.org/10.1038/s41467-021-23520-2" target="_blank">Schreiner et al. (2021)</a> showed that SO-spindle coupling precision predicts endogenous reactivation strength in humans, <a href="https://doi.org/10.1038/s41593-023-01324-5" target="_blank">Geva-Sagiv et al. (2023)</a> showed that real-time enhancement of hippocampal-prefrontal synchrony improves overnight human memory, <a href="https://doi.org/10.1038/s41467-024-49572-8" target="_blank">Schreiner et al. (2024)</a> linked spindle-locked ripples to human memory reactivation, and <a href="https://doi.org/10.1016/j.neuron.2025.03.020" target="_blank">Deng et al. (2025)</a> showed that NREM consolidation itself has a specific intracellular time window. This site therefore records <strong>sleep duration/history</strong> and <strong>sleep architecture / replay-coupling</strong> separately.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: sleep replay evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>sleep replay evidence</strong> could still compress a phase-locked healthy-human stimulation study, an endogenous scalp-decoding study, an intracranial closed-loop synchrony intervention, and an item-selective TMR result into one bucket. The primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41467-021-23520-2" target="_blank">Schreiner et al. (2021)</a> explicitly notes aggregated SO-spindle events, modest decoding levels, and scalp blindness to ripple ground truth, <a href="https://doi.org/10.1038/s41467-025-57766-x" target="_blank">Duan et al. (2025)</a> shows that strengthening and decaying items can coexist within the same human TMR session, and <a href="https://doi.org/10.1038/s41539-025-00340-3" target="_blank">Shin et al. (2025)</a> shows that behavioral benefit can concentrate in the challenging-memory regime rather than appearing uniformly across items. Therefore, this site now asks cross-day or sleep-replay claims to attach a <strong>sleep replay route card</strong> naming <strong>preparation</strong>, <strong>event definition</strong>, <strong>timing / control policy</strong>, <strong>memory target / selection regime</strong>, and <strong>abstention boundary</strong>. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#sleep-replay-route-card">Wiki: sleep replay route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: myelin evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>myelin evidence</strong> could still compress learning-dependent oligodendrogenesis, node / internode / periaxonal timing-state, developmental plasticity brake, remyelination-to-function recovery, and human macro-myelin proxy rows into one bucket. The primary literature does not support that shortcut. On this site, maintenance-state submissions must now state which inferential object they are actually using, what structural unit was directly observed, whether functional recovery occurred with partial versus complete remyelination, and whether the human evidence is only a proxy row rather than direct timing-state ground truth. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#myelin-route-card">Wiki: myelin / oligodendrocyte route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: do not collapse phospho-signaling into transcript or protein abundance</strong>
<p>
<a href="https://doi.org/10.1126/science.279.5352.870" target="_blank">Giese et al. (1998)</a>, <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">Lee et al. (2003)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.5303-03.2004" target="_blank">Rodrigues et al. (2004)</a>, <a href="https://doi.org/10.1016/j.neuron.2005.01.009" target="_blank">Tomita et al. (2005)</a>, and <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">Vierra et al. (2023)</a> show that phosphosite-specific and nanodomain-specific signaling states can determine plasticity expression and maintenance-relevant routing even when transcript or bulk protein abundance looks similar. Current human evidence such as the ex vivo phosphoproteome atlas from <a href="https://doi.org/10.1021/acs.jproteome.2c00244" target="_blank">Biswas et al. (2023)</a> is informative for region-specific ceiling setting, but it is still not a comparable in vivo whole-brain human route. Therefore, when a claim depends on phosphosite occupancy, kinase/phosphatase balance, or local second-messenger state, this site asks authors to disclose whether phospho-signaling was directly measured, causally perturbed, externally calibrated, or silently replaced by transcript/protein abundance alone.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: phospho-signaling evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>phosphosite-specific plasticity gates</strong>, <strong>compartmentalized second-messenger routing</strong>, <strong>region-structured phosphoproteome atlases</strong>, and <strong>single-site phospho-mutant memory interventions</strong> could still be compressed into one bucket called <strong>phospho evidence</strong>. The primary literature does not support that shortcut. <a href="https://doi.org/10.1523/JNEUROSCI.0248-16.2016" target="_blank">Havekes et al. (2016)</a> is about <strong>compartment-targeted PDE4A5 signaling in hippocampal memory</strong>, <a href="https://doi.org/10.1016/j.biopsych.2023.12.020" target="_blank">Altas et al. (2024)</a> is <strong>region-specific phosphorylation with synapse-type relocalization in mouse and human samples</strong>, <a href="https://doi.org/10.1523/JNEUROSCI.1619-24.2025" target="_blank">Rodriguez et al. (2025)</a> is a <strong>single-site phospho-mutant causal memory intervention</strong>, and <a href="https://doi.org/10.1021/acs.jproteome.2c00244" target="_blank">Biswas et al. (2023)</a> is a <strong>human ex vivo phosphoproteome atlas</strong>. On this site, phospho-signaling claims now have to disclose <strong>claim family</strong>, <strong>biological regime</strong>, <strong>time axis</strong>, <strong>assay and direct observable</strong>, <strong>spatial / compartment scope</strong>, <strong>causal leverage</strong>, and <strong>abstention boundary</strong>. The full operating rule is in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#phospho-route-card">Wiki: phospho-signaling route card</a>.
</p>
</div>
<div class="note-box">
<strong>Do not collapse energetic support into glial support</strong>
<p>
<a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">Rangaraju et al. (2014)</a>, <a href="https://doi.org/10.1038/s41598-023-40877-0" target="_blank">Underwood et al. (2023)</a>, <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">Rangaraju et al. (2019)</a>, <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">Divakaruni et al. (2018)</a>, <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">Bapat et al. (2024)</a>, <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">Hu et al. (2025)</a>, and <a href="https://doi.org/10.1038/s42255-026-01451-w" target="_blank">Vishwanath et al. (2026)</a> support a narrower rule: local ATP supply, respiration, mitochondrial positioning, and energetic micro-organization can change repeated-burst reliability and dendritic plasticity even before one asks whether astrocyte or clearance-state matched. Conversely, human <a href="https://doi.org/10.1002/nbm.3384" target="_blank">31P-MRS (Ren et al., 2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">dynamic DMRSI (Li et al., 2025)</a> remain macro energetic proxies rather than direct readouts of branch-local mitochondrial state. This site therefore records energetic route and glial route separately.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: bioenergetic evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>bioenergetic evidence</strong> could still compress <strong>presynaptic ATP-linked respiration</strong>, <strong>dendritic positioning / fission support</strong>, <strong>synaptic ATP-synthase nano-organization</strong>, <strong>mitochondrial Ca<sup>2+</sup>-efflux tuning</strong>, and <strong>human macro energetic imaging</strong> into one bucket. The primary literature does not support that shortcut. On this site, maintenance-state submissions must now state which inferential object they are actually using, which compartment was directly observed, whether the quantity is respiration, ATP-synthase arrangement, Ca<sup>2+</sup>-efflux-driven metabolic tuning, or only a macro 31P-MRS / dynamic DMRSI proxy, what function target was tested, and which local mitochondrial controller remained latent. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#bioenergetic-route-card">Wiki: bioenergetic / mitochondrial route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: astrocyte-state is not generic support background</strong>
<p>
<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> showed minute-scale cortical astrocyte-network encoding of local neurotransmitter input, <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a> showed that learning-associated astrocyte ensembles can regulate hippocampal memory recall, <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> showed that astrocytic ensembles can stabilize emotional memory across multiple days, and <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> showed that basolateral-amygdala astrocyte Ca<sup>2+</sup> signalling supports fear-memory retrieval / extinction representations. Therefore, this site does not accept a submission that depends on recall, multiday stabilization, or fear-state support while writing only a generic glial-support sentence. Authors now have to state whether the relevant astrocyte-state was directly measured, perturbed, only coarsely proxied, or left latent, and they must keep the rodent-to-human observability gap explicit.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: astrocyte evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>astrocyte evidence</strong> could still compress <strong>lactate-shuttle support</strong>, <strong>minute-scale cortical network encoding</strong>, <strong>learning-associated recall ensembles</strong>, <strong>multiday stabilization ensembles</strong>, <strong>fear-state representations</strong>, and <strong>human MAO-B / reactive-astrogliosis PET</strong> into one bucket. The primary literature does not support that shortcut. On this site, maintenance-state submissions must now state which inferential object they are actually using, what the direct astrocyte observable is, whether the result depends on transporter blockade, ensemble reactivation, gene deletion, astrocyte Ca<sup>2+</sup> intervention, or only tracer binding, what the functional target actually is, what human proxy class remains, and which human astrocyte controller is still latent. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#astrocyte-route-card">Wiki: astrocyte route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: clearance / immune support is not passive cleanup</strong>
<p>
<a href="https://doi.org/10.1038/nature14432" target="_blank">Louveau et al. (2015)</a> and <a href="https://doi.org/10.1038/s41586-019-1419-5" target="_blank">Ahn et al. (2019)</a> established meningeal-lymphatic drainage routes, <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> showed that a meningeal-lymphatics-microglia axis can regulate synaptic physiology, <a href="https://doi.org/10.1093/brain/awaa443" target="_blank">Eide &amp; Ringstad (2021)</a> showed that sleep deprivation impairs molecular clearance in humans, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> measured region-specific CSF-mobility drivers, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> linked sleep-active physiology to overnight Aβ / tau clearance to plasma in healthy older adults. Therefore, this site does not accept a submission that depends on multiday recovery, protein clearance, or maintenance support while naming only a generic cleanup story. Authors now have to state whether the relevant evidence was <strong>meningeal-lymphatic / CSF-interstitial / microglia-related</strong>, whether it remained only a <strong>macro support-state proxy</strong>, and which local immune or synaptic-maintenance controller remained latent.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: clearance / immune evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>clearance evidence</strong> could still compress <strong>drainage anatomy</strong>, <strong>microglia-mediated synaptic mechanism</strong>, <strong>human CSF-mobility MRI</strong>, and <strong>model-based human biomarker efflux</strong> into one bucket. The primary literature does not support that shortcut. On this site, maintenance-state submissions must now state which inferential object they are actually using, what the direct observable is, whether the result depends on a physiology / sleep / lymphatic perturbation route, what human acquisition or model burden remains, and which local immune or synaptic controller is still latent. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#clearance-route-card">Wiki: clearance / immune route card</a>.
</p>
</div>
<div class="note-box">
<strong>Do not collapse cargo delivery into proteostasis or ATP</strong>
<p>
<a href="https://doi.org/10.1016/j.neuron.2006.09.040" target="_blank">Park et al. (2006)</a> showed that recycling-endosome exocytosis is required for LTP-associated spine growth, <a href="https://doi.org/10.1073/pnas.0902304106" target="_blank">Maas et al. (2009)</a> showed that synaptic activation modifies microtubules that support postsynaptic cargo transport, <a href="https://doi.org/10.1016/j.neuron.2011.03.026" target="_blank">Yin et al. (2011)</a> and <a href="https://doi.org/10.7554/eLife.53456" target="_blank">Zhao et al. (2020)</a> showed that kinesin-dependent cargo routes change receptor levels, plasticity, and memory, <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">Swarnkar et al. (2021)</a> linked KIF5C-mediated transport to structural plasticity and long-term memory, and <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">Aiken &amp; Holzbaur (2024)</a> showed that axonal microtubule patterning controls presynaptic cargo delivery. This site therefore records cargo-transport state separately from both proteostasis and bioenergetics. Current human in vivo routes do not directly reveal branch- or bouton-specific cargo pausing, motor engagement, or microtubule traffic state, so this route stays latent unless externally calibrated.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: cargo evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>cargo evidence</strong> could still compress <strong>postsynaptic AMPAR / recycling-endosome delivery</strong>, <strong>learning-phase microtubule-state gating</strong>, <strong>activity-dependent vesicle confinement</strong>, <strong>axonal RNA localization</strong>, and <strong>presynaptic cargo retention</strong> into one bucket. The primary literature does not support that shortcut. <a href="https://doi.org/10.1038/nn2063" target="_blank">Correia et al. (2008)</a> is about <strong>myosin-Va-dependent transport of AMPARs into spines during LTP</strong>, <a href="https://doi.org/10.1038/ncomms5389" target="_blank">Uchida et al. (2014)</a> is about <strong>learning-phase microtubule stability controlling KIF5-mediated GluA2 localization and memory</strong>, <a href="https://doi.org/10.7554/eLife.80622" target="_blank">Wong et al. (2024)</a> is about <strong>local confinement of endogenous GluA1 vesicles near stimulated dendritic regions</strong>, <a href="https://doi.org/10.1038/s41467-025-57651-7" target="_blank">de Queiroz et al. (2025)</a> is about <strong>axonal RNA localization required for long-term memory in a mature in vivo circuit</strong>, and <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">Aiken &amp; Holzbaur (2024)</a> is about <strong>presynaptic cargo delivery and pausing in a human-neuron preparation</strong>. On this site, maintenance-state submissions must now state which inferential object they are actually using, what cargo was followed, whether the result is about long-range delivery, local pausing / confinement, spine entry, axonal RNA localization, or presynaptic retention, what preparation and time window were used, and whether the strongest human evidence is still limited to narrow preparations rather than living-human in vivo measurement. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#cargo-route-card">Wiki: cargo-transport / cytoskeletal trafficking route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-22 addendum: thermal evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>thermal evidence</strong> could still compress <strong>local operating-point physiology</strong>, <strong>field-potential confound</strong>, <strong>sequence / rhythm perturbation</strong>, <strong>device-heating artifact</strong>, and <strong>human macro thermometry / task-linked thermal mapping</strong> into one bucket. The primary literature does not support that shortcut. <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">Hardingham &amp; Larkman (1998)</a> is about <strong>temperature-dependent synaptic reliability</strong>, <a href="https://doi.org/10.1126/science.8446900" target="_blank">Moser et al. (1993)</a> is about <strong>field-potential amplitude being masked by temperature variation</strong>, <a href="https://doi.org/10.1038/nature07448" target="_blank">Long &amp; Fee (2008)</a> is about <strong>sequence timing under local cooling</strong>, <a href="https://doi.org/10.1038/s41593-019-0422-3" target="_blank">Owen et al. (2019)</a> is about <strong>heating introduced by the perturbation device itself</strong>, and <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a>, <a href="https://doi.org/10.3389/fnhum.2024.1398034" target="_blank">Rogala et al. (2024)</a>, plus <a href="https://doi.org/10.1007/s00062-024-01467-3" target="_blank">Tan et al. (2025)</a> remain <strong>macro human thermal routes</strong>. On this site, maintenance-state submissions must now state which inferential object they are actually using, what the direct thermal observable is, whether the result depends on local cooling / warming, a recording confound audit, or a device-heating burden, what time window and function target were tested, what human proxy class remains, and which local thermal controller is still latent. The full public rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#thermal-route-card">Wiki: thermal route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: human maintenance evidence must be class-labeled</strong>
<p>
On this site, <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#human-observability-ceiling">Wiki: Homeostatic plasticity and maintenance-state</a> now distinguishes <strong>fixed-tissue structural scaffold</strong>, <strong>regional synaptic-density proxy</strong>, <strong>macro-biochemical scaffold</strong>, <strong>macro energetic proxy</strong>, <strong>macro ionic proxy</strong>, <strong>macro thermal proxy</strong>, <strong>macro-myelin proxy</strong>, <strong>perturbation-conditioned plasticity proxy</strong>, and <strong>macro support-state proxy</strong>. Human-side evidence is therefore not submitted as one generic “maintenance signal.” Each route must be class-labeled before the claim ceiling is interpreted, and it must also disclose its <strong>calibrator role</strong>, meaning which hidden-state family it safely constrains rather than merely co-occurs with.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: causal relevance and human observability must be bridged, not fused</strong>
<p>
This site now keeps two axes separate when a maintenance-state claim cites both animal causal work and human proxy work. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2025)</a> and <a href="https://doi.org/10.1038/s41586-025-09774-6" target="_blank">Terceros et al. (2026)</a> strengthen controller-state and transcriptional-stabilization causality in rodents, while <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a>, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> strengthen perturbation-conditioned excitability or macro support-state observability in humans. These are not the same inferential step. Therefore, when a submission combines them, it must state <strong>which state family the causal paper makes relevant</strong>, <strong>which human proxy class was actually observed</strong>, <strong>which bridge assumptions remain unvalidated</strong>, and <strong>which local controller remains latent</strong>. Without that bridge disclosure, this site does not promote the result to measured human maintenance-state control.
</p>
</div>
<div class="note-box">
<strong>2026-03-19 addendum: MRSI metabolic connectome is a similarity graph, not a flux map</strong>
<p>
<a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> defined the human metabolic connectome as <strong>pairwise correlations among five metabolites across gray-matter parcels</strong> and reported only <strong>weak</strong> overall alignment with tractography-based structural connectivity. <a href="https://doi.org/10.1002/brb3.1852" target="_blank">Bhogal et al. (2020)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2022.119574" target="_blank">Wright et al. (2022)</a>, and <a href="https://doi.org/10.1148/radiol.232401" target="_blank">Baboli et al. (2024)</a> show why this route still needs a measurement-model audit: MRSI interpretation depends on SNR, partial-volume / lipid handling, and voxel-specific correction or tissue-water modeling. Therefore, on this site, an MRSI-derived metabolic connectome is read as a <strong>macro-biochemical similarity scaffold</strong> unless the submission names the <strong>metabolite set</strong>, <strong>parceling unit</strong>, <strong>correction model</strong>, <strong>spectral QC thresholds</strong>, and whether the object is <strong>static similarity</strong> or <strong>dynamic kinetic rate imaging</strong>. If the claim is about glucose-flux or rate mapping, the route must be audited separately against rate-imaging methods such as <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>.
</p>
</div>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this budget is missing, this site allows at most <strong>same-session fit</strong>, <strong>cross-day performance with unresolved maintenance route</strong>, or <strong>support-proxy-aligned evidence</strong>. It does not promote the result to <strong>maintenance-consistent</strong>, <strong>reconsolidation-consistent</strong>, or <strong>remote-memory-relevant</strong>. In particular, if <strong>phospho-signaling / second-messenger state</strong>, <strong>sleep / wake history</strong>, <strong>sleep architecture / replay-coupling state</strong>, <strong>timing support</strong>, <strong>thermal-state</strong>, <strong>ionic / chloride state</strong>, <strong>bioenergetic support</strong>, <strong>cargo-transport / cytoskeletal trafficking support</strong>, <strong>glial / astrocyte support</strong>, and <strong>clearance / immune proxy class</strong> are all absent, this site stops the reader from rephrasing a temporal hold as long-horizon maintenance evidence.
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

<section class="section" id="pretraining-card">
<h2 class="section-title">2026-03-20 addendum: attach a Pretraining Card to foundation / self-supervised EEG results</h2>
<p>
The remaining weakness after adding the <strong>Observability Budget</strong> and the <strong>Specificity &amp; Shortcut Card</strong> was that large EEG pretraining results could still be reported as if an ordinary model card were enough. The recent primary literature and current benchmark operations do not support that shortcut. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">Kostas et al. (2021)</a> framed transfer across unseen datasets, hardware, subjects, and tasks as the core challenge rather than as a solved default. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">Jiang et al. (2024)</a> explicitly listed electrode mismatch, unequal length, varied task design, and low SNR as central EEG-side barriers even while reporting strong LaBraM performance. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">Lee et al. (2025)</a> then reported only marginal gains, about 0.5%, over conventional deep baselines despite much larger parameter counts, while showing that PEFT can sharply reduce trainable parameters without degrading performance. <a href="https://arxiv.org/abs/2508.17742" target="_blank">Xiong et al. (2025)</a> argued that inconsistent protocols still make cross-model EEG-FM comparisons unreliable. The official <a href="https://eeg2025.github.io/submission/" target="_blank">EEG Challenge 2025 submission page</a> further fixed this as an <strong>inference-only code competition</strong>, and the final <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> later disclosed that Challenge 2 samples had not been randomized, allowing some teams to exploit contiguous-trial same-subject structure and forcing the organizers to award Challenge 1 and Challenge 2 separately. Therefore, this site now requires a <strong>Pretraining Card</strong> for foundation / self-supervised EEG submissions in addition to the standard model card.
</p>
<table class="data-table">
<thead>
<tr>
<th>Pretraining Card field</th>
<th>What must be written at minimum</th>
<th>What goes wrong if it is omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>corpus identity / overlap audit</strong></td>
<td>Name the pretraining corpus, version or snapshot, total hours, exclusions, and any overlap audit against downstream datasets, subjects, sessions, or near-duplicate recordings.</td>
<td>What looked like transfer can still be silent reuse of closely related data.</td>
</tr>
<tr>
<td><strong>population / setup diversity</strong></td>
<td>Report covered population, device families, clinical vs. lab setting, electrode schema, and reference-system distribution.</td>
<td>The number of datasets can be misread as recording diversity even when the corpus is narrow or setup-biased.</td>
</tr>
<tr>
<td><strong>harmonization policy</strong></td>
<td>Report channel mapping, reference handling, sample-rate conversion, token length, normalization, and missing-channel / missing-segment policy.</td>
<td>Formatting choices can be misread as model-capability differences.</td>
</tr>
<tr>
<td><strong>objective / inductive bias</strong></td>
<td>Name the pretraining objective, such as masked, autoregressive, contrastive, tokenizer-based, or reconstruction-heavy, and the major architectural prior.</td>
<td>The reader cannot tell whether the gain came from scale, objective choice, or domain-specific prior.</td>
</tr>
<tr>
<td><strong>adaptation regime</strong></td>
<td>State whether the downstream regime is frozen, linear-probe, PEFT, full fine-tune, or test-time training, together with target-data usage and label budget.</td>
<td>A heavily adapted result can be misread as clean zero-shot or general transfer.</td>
</tr>
<tr>
<td><strong>benchmark provenance</strong></td>
<td>Name the benchmark, version, split rule, sample-randomization / hidden-grouping policy, checkpoint-selection rule, segment length, preprocessing path, external hold-out construction, and any inference-stage compute or training restrictions.</td>
<td>Ranking changes driven by benchmark design can be misread as stable model superiority.</td>
</tr>
<tr>
<td><strong>scale / efficiency</strong></td>
<td>Report total parameter count, trainable fraction, pretraining steps or epochs, training time, adapter size, and inference cost.</td>
<td>"The large model won" can hide that the real driver was compute allocation or parameter-efficient adaptation.</td>
</tr>
<tr>
<td><strong>evaluation family / stop line</strong></td>
<td>Report hold-out unit, device / site hold-out, cross-day evaluation, abstention or fallback behavior, and a one-line stopped claim stating what still cannot be asserted.</td>
<td>A same-day benchmark win can be misread as deployability, source identifiability, or WBE-relevant state capture.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Official rules are not capability proof, but they are evidence of what comparability already requires</strong>
<p>
The EEG Challenge rules do not prove that any one model is best. They do something different and still important: they show that current operations already need <strong>pretraining-data disclosure</strong>, <strong>pretrained-model disclosure</strong>, and <strong>fine-tuning disclosure</strong> before a leaderboard is even interpretable. The later leaderboard postmortem sharpened the same point by showing that <strong>sample randomization</strong> and <strong>hidden grouping structure</strong> can change what the leaderboard was measuring at all. On this site, that operational lesson is promoted from benchmark-specific documentation to a general audit rule.
</p>
</div>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this card is missing, this site treats the result by default as <strong>qualified representation-learning / decoding evidence</strong>, not as portable transfer evidence, deployable robustness, source-identifiable recovery, or WBE-relevant state capture. In particular, if <strong>corpus identity / overlap audit</strong>, <strong>harmonization policy</strong>, <strong>adaptation regime</strong>, or <strong>benchmark provenance</strong> including <strong>split randomness / hidden grouping</strong> is missing, this site stops the reader from rephrasing the result as "generalization is solved."
</p>
</div>
<div class="note-box">
<strong>How this differs from the existing cards</strong>
<p>
The <a href="#observability-budget">Observability Budget</a> fixes <strong>what the sensor directly observed</strong>. The <a href="#specificity-shortcut-card">Specificity &amp; Shortcut Card</a> fixes <strong>which route predictive information came from</strong>. The Pretraining Card fixes <strong>what part of the reported transfer came from corpus composition, harmonization, adaptation, benchmark design, and compute allocation</strong>. The <a href="#temporal-validity-card">Temporal Validity Card</a> then fixes <strong>how far the result can be extrapolated across time</strong>. On this site, a foundation-model result needs all of these boundaries kept separate.
</p>
</div>
</section>

<section class="section" id="state-completeness-gate">
<h2 class="section-title">State variable integrity gate</h2>
<p>
In our March 2026 primary-literature audit, we reconfirmed that there are at least thirteen loose state classes between <strong>“having a wiring diagram”</strong> and <strong>“being able to behave generatively”</strong>. In addition to cell types, synapses, delays, neuromodulation, and glia, we now also treat <strong>activity-dependent transcription / chromatin state</strong>, <strong>post-transcriptional RNA-state</strong>, <strong>phospho-signaling / second-messenger state</strong>, <strong>intrinsic excitability / homeostatic set points</strong>, <strong>local proteostasis / synaptic-tagging state</strong>, <strong>perisynaptic ECM / PNN state</strong>, <strong>ionic milieu / chloride homeostasis</strong>, and <strong>shared extracellular / electrical state</strong> as independent classes. Therefore, on this site, we do not accept <strong>edge-list submissions alone</strong> as a condition for passing L2 or above.
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
<td><strong>Post-transcriptional RNA-state</strong></td>
<td>Even with the same graph, cell type, and gene-level transcript counts, alternative splicing, m6A-dependent translation / degradation, and RNA-editing ratios can still change receptor composition, downstream transcriptional control, plasticity rules, and maintenance behavior. </td>
<td>Stop treating gene-level abundance or DEG signatures as if isoform, m6A, and RNA-editing control were fixed; keep RNA-state explicit as latent, perturbed, externally calibrated, or isoform-resolved. </td>
</tr>
<tr>
<td><strong>Phospho-signaling / second-messenger state</strong></td>
<td>Even with the same graph, transcript state, and bulk protein abundance, phosphosite occupancy, kinase/phosphatase balance, and compartment-specific second-messenger nanodomains can still change plasticity expression and controller state. </td>
<td>Stop treating transcriptomics, proteomics, or nominal weights as if the active phospho-controller were fixed; keep phospho-signaling explicit as latent, perturbed, externally calibrated, or phosphosite-resolved. </td>
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
<td><strong>Cargo-transport / cytoskeletal trafficking state</strong></td>
<td>Even with the same graph, current weights, and local translation capacity, the branch/spine/bouton-specific delivery and retention of receptors, endosomes, mRNA cargoes, mitochondria, and presynaptic components can still differ. </td>
<td>Stop treating compartment-specific stabilization, receptor localization, or synaptogenesis as fixed, and keep cargo-transport state explicit as latent, perturbed, externally calibrated, or locally measured. </td>
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
<td><strong>Shared extracellular / electrical state</strong></td>
<td>Even with the same chemical graph, gap-junction coupling, endogenous electric fields, and local inhibitory driving force can still change fast synchrony, oscillatory coordination, spike timing, and state-switch thresholds. </td>
<td>Stop treating fast synchrony, oscillatory coordination, or electrical-state regime as fixed, and keep electrical coupling / field state explicit as latent, perturbed, externally calibrated, or locally measured. </td>
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
<td><strong>Astrocyte / glial-state</strong></td>
<td>Astrocyte network and ensemble state can causally influence transmitter integration, memory retrieval, multiday stabilization, and fear-state representations, and therefore cannot be collapsed into generic metabolic background. </td>
<td>Recall, reconsolidation, and long-horizon stability stay partial-model claims unless astrocyte-state is measured, perturbed, or explicitly left latent with a species-limited ceiling. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Practical rules here</strong>
<p>
connectome-complete does not mean<strong>emulation-complete</strong>. Detailed primary literature and the technical basis for which state variables should be included in the minimum submission are summarized in <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams alone are not enough</a>. The newly emphasized issues of <strong>activity-dependent transcription / chromatin state</strong>, <strong>post-transcriptional RNA-state</strong>, <strong>local proteostasis / synaptic-tagging state</strong>, <strong>cargo-transport / cytoskeletal trafficking state</strong>, <strong>astrocyte / glial-state</strong>, and <strong>intrinsic excitability/homeostasis/maintenance state</strong> are discussed in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-18 addendum: cell-type atlas is not current transcriptional state</strong>
<p>
<a href="https://doi.org/10.1126/science.adg9982" target="_blank">Santoni et al. (2024)</a> showed that chromatin plasticity predetermines neuronal eligibility for memory-trace formation, <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">Traunmüller et al. (2025)</a> showed temporally defined and region-specific chromatin / gene-expression changes after novel-environment exposure, <a href="https://doi.org/10.1038/s41588-025-02368-y" target="_blank">Coda et al. (2025)</a> showed cell-type- and locus-specific epigenetic editing of memory expression, and <a href="https://doi.org/10.1038/s41586-025-09774-6" target="_blank">Terceros et al. (2026)</a> showed distinct thalamocortical transcriptional gates for memory stabilization. Therefore, when a claim depends on allocation eligibility, late stabilization, or locus-specific plasticity, this site asks authors to disclose whether transcriptional / chromatin state was measured, perturbed, externally calibrated, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03-19 addendum: transcription / chromatin evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>allocation eligibility</strong>, <strong>time-resolved response map</strong>, <strong>persistent stabilization cascade</strong>, and <strong>locus-specific causal editability</strong> could still be compressed into one bucket called <strong>transcriptomic evidence</strong>. The primary literature does not support that shortcut. On this site, such claims now have to disclose <strong>claim family</strong>, <strong>species / region / task</strong>, <strong>sampling windows</strong>, <strong>assay and direct observable</strong>, <strong>animal-level independence / pseudoreplication handling</strong>, <strong>causal perturbation status</strong>, and <strong>abstention boundary</strong>. The full operating rule is in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#transcription-route-card">Wiki: transcription / chromatin route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: transcript count is not post-transcriptional RNA-state</strong>
<p>
<a href="https://doi.org/10.1038/nn.4069" target="_blank">Wang et al. (2015)</a> showed that a neuron-specific LSD1 splice isoform regulates memory formation, <a href="https://doi.org/10.1016/j.neuron.2019.03.032" target="_blank">Dai et al. (2019)</a> showed that presynaptic neurexin alternative splicing changes postsynaptic receptor balance and contextual memory, <a href="https://doi.org/10.1038/s41586-018-0666-1" target="_blank">Shi et al. (2018)</a> and <a href="https://doi.org/10.1002/advs.202514926" target="_blank">Li et al. (2025)</a> showed that m6A-reader routes can alter hippocampus-dependent learning and memory, and <a href="https://doi.org/10.1126/scisignal.adr1442" target="_blank">Peterson et al. (2025)</a> showed that ADAR2-mediated GluA2 editing contributes to homeostatic synaptic plasticity. Therefore, when a claim depends on isoform choice, m6A-dependent translation / degradation, or RNA-editing ratio, this site asks authors to disclose whether post-transcriptional RNA-state was directly measured, causally perturbed, externally calibrated, or silently replaced by gene-level abundance alone. Specialized long-read atlas work such as <a href="https://doi.org/10.1038/s41593-024-01616-4" target="_blank">Joglekar et al. (2024)</a> is informative for the ceiling but still not a comparable in vivo whole-brain human route.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: post-transcriptional RNA evidence now needs a route card</strong>
<p>
The remaining weakness was that <strong>alternative-splice controller papers</strong>, <strong>m6A-dependent translation papers</strong>, <strong>m6A-dependent degradation papers</strong>, <strong>RNA-editing controller papers</strong>, and <strong>long-read atlas papers</strong> could still be compressed into one bucket called <strong>post-transcriptional evidence</strong>. The primary literature does not support that shortcut. <a href="https://doi.org/10.1038/nn.4069" target="_blank">Wang et al. (2015)</a> is a splice-isoform route whose downstream object is chromatin / transcriptional control, <a href="https://doi.org/10.1016/j.neuron.2019.03.032" target="_blank">Dai et al. (2019)</a> is a splice-dependent transsynaptic receptor-balance route, <a href="https://doi.org/10.1038/s41586-018-0666-1" target="_blank">Shi et al. (2018)</a> and <a href="https://doi.org/10.1002/advs.202514926" target="_blank">Li et al. (2025)</a> are distinct m6A translation-versus-degradation routes, <a href="https://doi.org/10.1126/scisignal.adr1442" target="_blank">Peterson et al. (2025)</a> is an ADAR2 / GluA2 editing route for homeostatic scaling, and <a href="https://doi.org/10.1038/s41593-024-01616-4" target="_blank">Joglekar et al. (2024)</a> is an atlas / observability-ceiling route. On this site, post-transcriptional claims therefore have to disclose <strong>claim family</strong>, <strong>RNA control axis</strong>, <strong>time axis</strong>, <strong>assay and direct observable</strong>, <strong>downstream functional object</strong>, <strong>causal leverage</strong>, <strong>human observability ceiling</strong>, and <strong>abstention boundary</strong> before any claim ceiling is raised. The full operating rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#post-transcriptional-rna-route-card">Wiki: post-transcriptional RNA route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: transcript or protein abundance is not phospho-signaling state</strong>
<p>
<a href="https://doi.org/10.1126/science.279.5352.870" target="_blank">Giese et al. (1998)</a>, <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">Lee et al. (2003)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.5303-03.2004" target="_blank">Rodrigues et al. (2004)</a>, <a href="https://doi.org/10.1016/j.neuron.2005.01.009" target="_blank">Tomita et al. (2005)</a>, and <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">Vierra et al. (2023)</a> show that memory-relevant phosphosite occupancy and signaling nanodomains remain another control layer even when transcript or bulk protein abundance looks similar. Therefore, when a claim depends on kinase/phosphatase balance, phosphosite occupancy, or local second-messenger routing, this site asks authors to disclose whether phospho-signaling / second-messenger state was directly measured, causally perturbed, externally calibrated, or silently replaced by abundance-only evidence. Human phosphoproteome atlas work such as <a href="https://doi.org/10.1021/acs.jproteome.2c00244" target="_blank">Biswas et al. (2023)</a> is informative for the ceiling but still not a comparable in vivo whole-brain human route.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: local proteostasis evidence now needs a route card</strong>
<p>
<a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a> and <a href="https://doi.org/10.1038/ncomms2250" target="_blank">Shires et al. (2012)</a> are about <strong>tag / capture eligibility</strong>. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a> is about <strong>branch-level integration</strong>. <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">Fonseca et al. (2006)</a> and <a href="https://doi.org/10.1111/acel.14492" target="_blank">Parker et al. (2025)</a> are about <strong>synthesis-degradation or proteasome-capacity balance</strong>. <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a> and <a href="https://doi.org/10.1073/pnas.2315958121" target="_blank">Chang et al. (2024)</a> are about <strong>autophagy-linked plasticity routes</strong>. <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Lee et al. (2022)</a> and <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">Thomas et al. (2025)</a> are about <strong>turnover-resistant persistence or a candidate tag substrate</strong>. Therefore, when a claim depends on late stabilization, reconsolidation, or cross-event capture, this site now asks authors not only whether the local proteostasis / synaptic-tag route was measured or perturbed, but also <strong>which claim family</strong>, <strong>which integrative unit</strong>, <strong>which direct observable</strong>, <strong>which turnover window</strong>, and <strong>which human observability ceiling</strong> apply. Current human routes on this site do not directly resolve tagged branches, PRP capture, local ribosome / proteasome / autophagy state, or same-subject whole-brain late-stabilization controllers. The longer operating rule is in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#proteostasis-route-card">Wiki: local proteostasis / synaptic-tagging route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03 Addendum: delay is not one scalar</strong>
<p>
Hardware latency audit and biological timing-state audit solve different problems. <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a>, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a>, <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a>, <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">Micheva et al. (2021)</a>, and <a href="https://doi.org/10.7554/eLife.73827" target="_blank">Dubey et al. (2022)</a> show that node/internode geometry, periaxonal coupling, astrocyte control, and PV-axon myelination can all alter spike-arrival timing and synchrony. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">van Blooijs et al. (2023)</a> pushes human tract-scale transmission-speed measurement forward, but it still remains a macro proxy. Therefore, when a claim depends on phase, synchrony, or closed-loop timing, this site asks authors to disclose whether biological timing-state was measured, externally calibrated, absorbed into a constant, or left latent.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: ECM / PNN evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>ECM / PNN evidence</strong> could still compress several different inferential objects into one bucket. The primary literature does not support that shortcut. <a href="https://doi.org/10.1126/science.1072699" target="_blank">Pizzorusso et al. (2002)</a> is about <strong>plasticity-window reopening</strong>, <a href="https://doi.org/10.1038/nn.2338" target="_blank">Frischknecht et al. (2009)</a> is about <strong>receptor-mobility constraint</strong>, <a href="https://doi.org/10.1016/j.cell.2020.05.050" target="_blank">Nguyen et al. (2020)</a> is about <strong>microglia-driven ECM remodeling</strong>, <a href="https://doi.org/10.1523/JNEUROSCI.1626-24.2024" target="_blank">Alexander et al. (2025)</a> is about <strong>cell-type-specific memory support</strong>, <a href="https://doi.org/10.1111/acel.70139" target="_blank">Mehak et al. (2025)</a> is about an <strong>age-linked rescue route</strong>, and <a href="https://doi.org/10.1002/epi4.12963" target="_blank">Lehner et al. (2024)</a> plus <a href="https://doi.org/10.1007/s12035-024-04306-1" target="_blank">Banovac et al. (2025)</a> remain <strong>human ex vivo histology</strong>. On this site, ECM / PNN claims therefore have to disclose <strong>which claim family</strong>, <strong>which matrix object and cell population</strong>, <strong>which direct observable</strong>, <strong>which controller or perturbation route</strong>, <strong>which recovery boundary</strong>, <strong>which human observability ceiling</strong>, and <strong>which abstention boundary</strong> apply before any claim ceiling is raised. The full operating rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#ecm-pnn-route-card">Wiki: ECM / PNN route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: ionic / chloride evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>ionic evidence</strong> could still compress several different inferential objects into one bucket. The primary literature does not support that shortcut. <a href="https://doi.org/10.1126/science.1245423" target="_blank">Glykys et al. (2014)</a> is about <strong>local chloride set point</strong>, <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">Heubl et al. (2017)</a> is about <strong>activity-dependent KCC2 regulation</strong>, <a href="https://doi.org/10.1126/science.aad4821" target="_blank">Ding et al. (2016)</a> and <a href="https://doi.org/10.1111/jsr.13522" target="_blank">Forsberg et al. (2022)</a> are about <strong>interstitial / CSF ion composition linked to sleep-wake state</strong>, <a href="https://doi.org/10.1016/j.celrep.2023.112934" target="_blank">Byvaltsev et al. (2023)</a> is about <strong>perisynaptic K<sup>+</sup> clearance by reverse-mode KCC2</strong>, <a href="https://doi.org/10.1016/j.cub.2025.01.050" target="_blank">Alfonsa et al. (2025)</a> is about <strong>sleep-wake-history-dependent E<sub>GABAA</sub> shifts that change LTP induction</strong>, <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">Huberfeld et al. (2007)</a> is a <strong>human pathology route</strong>, and <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> plus <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">Qian et al. (2025)</a> are <strong>macro human sodium-proxy routes</strong>. On this site, ionic / chloride claims therefore have to disclose <strong>which claim family</strong>, <strong>which direct ionic observable</strong>, <strong>which spatial regime</strong>, <strong>which perturbation or controller route</strong>, <strong>which human proxy class</strong>, and <strong>which abstention boundary</strong> apply before any claim ceiling is raised. The full operating rule is summarized in <a href="wiki/homeostatic-plasticity-and-maintenance-state.html#ionic-route-card">Wiki: ionic / chloride route card</a>.
</p>
</div>
<div class="note-box">
<strong>2026-03-22 addendum: electrical-state evidence also needs a route card</strong>
<p>
The remaining weakness was that <strong>electrical-state evidence</strong> could still compress several different inferential objects into one bucket. The primary literature does not support that shortcut. <a href="https://doi.org/10.1038/47029" target="_blank">Galarreta &amp; Hestrin (1999)</a> is about <strong>gap-junction coupling networks</strong>, <a href="https://doi.org/10.1038/nn.2727" target="_blank">Anastassiou et al. (2011)</a> is about <strong>endogenous-field / ephaptic spike-timing bias</strong>, <a href="https://doi.org/10.1016/j.neuron.2023.08.005" target="_blank">Burman et al. (2023)</a> is about <strong>inhibitory driving-force regime in active cortex</strong>, <a href="https://doi.org/10.1073/pnas.2313042121" target="_blank">Yang et al. (2024)</a> is about <strong>activity-dependent electrical-synapse remodeling</strong>, <a href="https://doi.org/10.1038/s41467-024-53074-y" target="_blank">Selfe et al. (2024)</a> is a <strong>direct inhibitory-driving-force assay</strong> with a specialized local optical route, and <a href="https://doi.org/10.1111/ejn.70401" target="_blank">Feld et al. (2026)</a> remains a <strong>human perturbation-conditioned clue</strong> with pharmacological caveats rather than a local whole-brain readout. On this site, electrical-state claims therefore have to disclose <strong>which claim family</strong>, <strong>which direct electrical observable</strong>, <strong>which spatial regime</strong>, <strong>which perturbation or calibration route</strong>, <strong>which human evidence class</strong>, and <strong>which abstention boundary</strong> apply before any claim ceiling is raised. The full operating rule is summarized in <a href="wiki/connectome-is-not-enough.html#electrical-state-route-card">Wiki: electrical-state route card</a>.
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
<td><strong>+ shared extracellular / electrical-state audit</strong></td>
<td>Compare a chemical-connectome or synapse-aware baseline against the same model with gap-junction measurement or perturbation, local field calibration, or direct inhibitory-driving-force measurement under the same held-out synchrony, sleep-oscillation, or state-switch condition, and disclose gains separately. </td>
<td>You can state more narrowly how much fast synchrony, oscillatory coordination, or electrical-state prediction improves once electrical coupling and local driving-force state are treated explicitly. </td>
<td>Human macro field or perturbation evidence alone remains indirect and does not become ground truth of local electrical coupling or cell-specific inhibitory driving force in vivo. </td>
</tr>
<tr>
<td><strong>+ timing-state / conduction audit</strong></td>
<td>Compare a fixed-delay baseline against a model or analysis that adds measured or externally calibrated timing variables under the same held-out conditions, and disclose phase / synchrony / perturbation gains separately. </td>
<td>You can state more narrowly how much timing-sensitive prediction improves once biological conduction timing is treated explicitly rather than absorbed into a constant. </td>
<td>Human myelin maps or tract-speed estimates remain macro timing proxies; without external calibration they do not become per-axon timing ground truth. </td>
</tr>
<tr>
<td><strong>+ neuromodulatory route audit</strong></td>
<td>Compare the same baseline against mixed arousal proxy, local transmitter sensor, receptor / transporter atlas, occupancy PET, or release-sensitive displacement PET under the same held-out state transition, and report ligand / drug / challenge / dose / time-window plus abstention separately. </td>
<td>You can state more narrowly how much a selected transmitter-linked covariate, regional receptor prior, or challenge-limited release proxy improved prediction or stratification. </td>
<td>Mixed proxy remains a covariate, receptor atlas remains a regional prior, occupancy PET remains a ligand- and dose-limited target-engagement proxy, and displacement PET remains a receptor- and challenge-limited release proxy rather than whole-brain neuromodulatory ground truth. </td>
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
<li><strong>External validation of ESI claims:</strong>When claiming improvements in EEG source imaging, clarify individual MRI, coordinates, and forward models as much as possible, and verify errors using named validation classes such as simulations / phantoms, intracranial stimulation, simultaneous invasive recordings, or postsurgical outcome. Deep accuracy should not be claimed simply by introducing high-density EEG or MRI. </li>
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
The remaining weakness in this section was that simply sorting EEG / DoC / anesthesia papers into "no-report," "PCI," "resting-state," and "multimodal" still left the promotion rule too coarse. <a href="https://doi.org/10.1093/cercor/bhae415" target="_blank">Cohen et al. (2024)</a> and <a href="https://doi.org/10.7554/eLife.102335" target="_blank">Fahrenfort et al. (2025)</a> showed that post-perceptual / report confounds and criterion placement must be broken separately, so no-report design alone is not yet construct validity. <a href="https://doi.org/10.1093/cercor/bhae130" target="_blank">Gogulski et al. (2024)</a> showed that early/local dlPFC TMS-evoked responses vary markedly in reliability across targets and analysis windows, and <a href="https://doi.org/10.1162/imag_a_00349" target="_blank">Biabani et al. (2024)</a> showed that auditory and somatosensory inputs can materially contaminate TMS-evoked responses across prefrontal, premotor, and parietal stimulation. <a href="https://doi.org/10.7554/eLife.98920" target="_blank">Breyton et al. (2025)</a> then showed that spatiotemporal brain complexity can separate consciousness-related states outside perturbation paradigms, while <a href="https://doi.org/10.1111/ejn.16299" target="_blank">Casarotto et al. (2024)</a> showed that spontaneous EEG features and PCI can dissociate in minimally conscious patients, so resting-state markers still require same-cohort calibration rather than substitution for perturbational benchmarks. Finally, <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2022)</a>, <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> showed that multimodal panels can improve diagnosis / prognosis and cross-centre robustness, but only as bundles whose value must still be measured against behavior-only baselines, missing-modality slices, and site transfer. Therefore, this site accepts consciousness-related readouts at the following four gates.
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
<td>Separate no-report from report, log criterion placement separately, predefine failure conditions, and disclose how task / report confounds were suppressed. </td>
<td>Do not say the marker reads conscious content itself; decision strategy and post-perceptual processing remain viable alternatives. </td>
</tr>
<tr>
<td><strong>Perturbational gate</strong></td>
<td>For TMS-EEG or intracranial perturbation, report stimulation site, intensity, control / sham, auditory and somatosensory suppression, artifact window, analysis window, and target-specific reliability. </td>
<td>Do not call a PCI / PCI-ST-style value a stable state-level benchmark if the perturbation and reliability log is incomplete. </td>
</tr>
<tr>
<td><strong>Calibration gate</strong></td>
<td>Calibrate resting-state complexity / criticality, PCI, behavioral assessment, clinical outcomes, and pipeline sensitivity within the same cohort, and publish the decision / abstention threshold used at evaluation time. </td>
<td>Do not present resting-state complexity or passive EEG classifiers as standalone bedside meters; without same-cohort calibration they remain auxiliary proxies. </td>
</tr>
<tr>
<td><strong>Incremental / deployability gate</strong></td>
<td>Show incremental value over a behavior-only baseline, external-site generalization, robustness under missing-modality conditions, calibration error, and measurement burden. </td>
<td>Do not describe a multimodal panel as ready to deploy or portable across hospitals on average accuracy alone. </td>
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
<td>Feedback or a bidirectional loop in which a stimulus changes the next input, behavior changes due to intervention, and the surrogate body / environment mapping is disclosed. </td>
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

<section class="section" id="body-environment-boundary-card">
<h2 class="section-title">2026-03-19 addendum: attach a Body / Environment Boundary Card to L3 results</h2>
<p>
The weakness exposed in this pass was that latency, jitter, and safe-stop logs can show whether a loop is fast and stable, but not <strong>which subject boundary the loop actually preserved</strong>. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> and <a href="https://doi.org/10.1126/science.aav7893" target="_blank">Stringer et al. (2019)</a> showed that ongoing behavior explains a large fraction of cortical activity, <a href="https://doi.org/10.1038/nn.3567" target="_blank">Saleem et al. (2013)</a> and <a href="https://doi.org/10.1126/science.1232655" target="_blank">Ravassard et al. (2013)</a> showed that locomotion, optic flow, vestibular, and other sensory cues reshape cortical and hippocampal codes, <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">Zelano et al. (2016)</a> and <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">Raut et al. (2025)</a> showed that breathing and arousal link brain dynamics to organism-wide physiological state, and <a href="https://doi.org/10.1126/science.abd0380" target="_blank">Flesher et al. (2021)</a> showed that restoring tactile feedback improves a local bidirectional BCI. Therefore, a loop result cannot be read here as “embodiment solved” unless it names which sensory, motor, interoceptive, and surrogate-body channels were preserved, substituted, or omitted.
</p>
<table class="data-table">
<thead>
<tr>
<th>Body / Environment Boundary Card field</th>
<th>What must be written at minimum</th>
<th>What goes wrong if it is omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>declared boundary / target subsystem</strong></td>
<td>Fix whether the claim concerns a speech loop, grasp loop, navigation loop, memory-task loop, or a broader embodied agent, and state the maximum claim ceiling.</td>
<td>A local loop is too easily misread as if the whole subject boundary had been reproduced.</td>
</tr>
<tr>
<td><strong>retained / substituted sensory channels</strong></td>
<td>List which inputs were preserved or replaced: vision, touch, proprioception, vestibular cues, respiration-related cues, auditory feedback, dialogue partner, and task-state cues.</td>
<td>The reader cannot tell whether the observed performance depended on missing cues that were silently restored or on cues that never existed in the test.</td>
</tr>
<tr>
<td><strong>retained / substituted action channels</strong></td>
<td>Name the actual plant or actuator, such as cursor, robotic hand, speech synthesizer, virtual avatar, or stimulation output, together with its controllable degrees of freedom.</td>
<td>The loop can look “embodied” even though the output space was heavily simplified.</td>
</tr>
<tr>
<td><strong>interoceptive / autonomic / arousal routes</strong></td>
<td>State whether respiration, pupil, HR / HRV, effort, fatigue, or other body-state observables were logged, manipulated, or left latent.</td>
<td>Arousal- or body-state-driven gains can be misread as stable neural equivalence of the target subsystem.</td>
</tr>
<tr>
<td><strong>surrogate body / environment contract</strong></td>
<td>Describe the surrogate body or environment, including latency, noise, saturation, sensory remapping, and whether the environment was fixed, simulated, or interactive.</td>
<td>A local engineering convenience can be mistaken for a biologically comparable sensorimotor world.</td>
</tr>
<tr>
<td><strong>loop-removal / ablation test</strong></td>
<td>Report what happened when feedback, tactile input, self-motion cues, or another key loop element was removed, scrambled, or delayed.</td>
<td>The system may look robust only because the decisive loop component was never challenged.</td>
</tr>
<tr>
<td><strong>environment OOD / perturbation slices</strong></td>
<td>Report performance across changed environments, noise levels, partners, objects, tasks, or sensory conditions rather than only on the training setting.</td>
<td>The result can be overread as general closed-loop competence even if it is tightly locked to one environment.</td>
</tr>
<tr>
<td><strong>residual omitted loops / abstention boundary</strong></td>
<td>Fix which body / environment routes still remained absent and what stronger claim is therefore forbidden.</td>
<td>L3 subsystem evidence is too easily promoted to embodied equivalence or WBE readiness.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Minimum operating rules</strong>
<p>
If this card is missing, this site treats the result by default as a <strong>task-specific local controller</strong>, <strong>local subsystem loop</strong>, or <strong>surrogate-body demonstration</strong>. It does not promote the result to solved embodiment, subject-complete closed loop, or WBE-relevant body / environment equivalence.
</p>
</div>
<div class="note-box">
<strong>How this differs from the Intervention Card</strong>
<p>
The <a href="#causal-perturbation-suite">Intervention Card</a> fixes what was changed and how timing/safety were logged. The Body / Environment Boundary Card fixes <strong>what system boundary the loop actually used</strong>. On this site, a paper needs both before its L3 wording is allowed to rise.
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
<li><strong>Human Proxy Composition Card:</strong>When several living-human proxy rows are used together, name the claimed latent variable, direct observable by row, same-subject / same-session relation, model burden, incremental evidence over the strongest single row, cross-row calibration route, and residual latent-state ceiling. If this is missing, the bundle stays at the strongest single-row or proxy-rich ceiling rather than same-subject state identification. </li>
<li><strong>Fusion Card:</strong>When reporting multimodal or atlas-prior results, name the acquisition relation, synchronization route and unresolved lag, geometry / co-registration scope, fusion model, hemodynamic vascular-state / CVR calibration when applicable, unimodal and prior-only baselines, external calibration route, and abstention boundary. If this is missing, the result stays at the strongest unimodal or atlas-conditioned ceiling rather than same-subject cross-stack state identification. </li>
<li><strong>ESI/HBM logs:</strong>Only when making anatomical source claims, attach uncertainty maps from cranial conductivity, forward model sensitivity analysis, or hierarchical Bayesian estimation. </li>
<li><strong>Inverse-Solver Agreement Log:</strong>When reporting an anatomical ESI/HBM result, name the inverse families / packages compared, parameter window, headline-location spread or overlap metric, and whether the displayed map is best-case, median, or ensemble. If this is missing, the result stays at the method-sensitive source-hypothesis level. </li>
<li><strong>Identifiability Card:</strong>For inverse or model-based claims, name the claim object, structural-identifiability assumptions, practical-identifiability evidence, alternative solution set, experiment-design leverage, recorded subset, held-out falsification route, and abstention boundary. If this is missing, the result stays at predictive / localization / model-conditioned level rather than unique recovery. </li>
<li><strong>Alternative model log:</strong>Does not claim that the estimated model is the only solution, but reports the existence of alternative models or equivalence classes that can explain the same observed statistics. </li>
<li><strong>Connectome-Constrained Model Card:</strong>When reporting a connectome-constrained predictor, name the structural prior and coverage, fitted degrees of freedom, task/state regime plus OOD slices, omitted mechanisms, validation / perturbation class, ensemble spread or alternative families, and abstention boundary. If this is missing, the result stays at the conditional-model / hypothesis-engine level. </li>
<li><strong>Effective Connectivity Route Card:</strong>When reporting DCM or related effective-connectivity results, name the node set and omitted competitors, neural-mass / HRF / prior assumptions, family comparison or model-recovery results, perturbation / external validation route, reliability window, and abstention boundary. If this is missing, the result stays at the model-conditioned hypothesis level. </li>
<li><strong>Pretraining Card:</strong>When reporting a foundation / self-supervised EEG result, name corpus identity and overlap audit, setup diversity, harmonization policy, adaptation regime, benchmark provenance, scale / efficiency, and the stopped claim. If this is missing, the result stays at the qualified representation-learning / decoding level. </li>
<li><strong>Body / Environment Boundary Card:</strong>For online human-in-the-loop or embodied tasks, name retained / substituted sensory, motor, and interoceptive channels, the surrogate body / environment contract, loop-removal tests, OOD environment slices, and the abstention boundary. If this is missing, the result stays at the local-controller level. </li>
<li><strong>Preprocessing Fidelity Log:</strong>Records before and after spectra, exclusion/interpolation rates, changes in key metrics, and at least one task-consistent signal preservation metric, with or without ASR. </li>
<li><strong>Event Semantics Log:</strong> Attach HED to BIDS metadata and map to CogAtlas / CogPO / NIF / SCORE etc. as necessary. Fixing to a specific ontology is not a common requirement. </li>
<li><strong>Perturbation log:</strong>If local interventions or stimulation were used, expose the stimulation site, intensity, artifact window, masking, safe stop conditions, and retry conditions. If not used, specify "No perturbation evidence." </li>
<li><strong>Irreversibility / Thermodynamic Route Card:</strong>When reporting irreversibility, arrow-of-time, entropy production, or entropy flow, name signal route and state definition, estimator family, null / surrogate control, quantity type (lower bound / asymmetry / model-based), and isolation of hardware power and computational cost. If this is missing, the result stays at the exploratory auxiliary-log level. </li>
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
Although research investigating brain dynamics using NESS (Non-Equilibrium Steady State) and time irreversibility is important, this site positions it as a <strong>Supplementary Research Track</strong> as of 2026-03. While the usefulness of irreversibility indicators is being shown, they are still not a common acceptance criterion for WBE validation because the result can move materially with modality, coarse-graining, partial observability, hidden-cycle structure, temporal resolution, source model, finite-data regime, and dynamical assumptions. In particular, entropy production estimated from coarse-grained neural data is often <strong>information-theoretic lower bound</strong> and must be read separately from microscopic physical dissipation itself.
</p>
<div class="note-box">
<strong>2026-03-21 addendum: irreversibility claims need a route card and closure audit</strong>
<p>
<a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> estimated entropy-production lower bounds from coarse-grained BOLD state transitions and showed sensitivity to the number of coarse-grained states, <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a> used inversion decoding on ECoG and showed dependence on principal-component choice, feature set, and model complexity, <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> estimated model-based entropy flow from spike trains while explicitly stating pairwise and conditional-independence limits, <a href="https://doi.org/10.1103/PhysRevLett.125.110601" target="_blank">Teza &amp; Stella (2020)</a> and <a href="https://doi.org/10.1103/PhysRevE.105.L042601" target="_blank">Cocconi et al. (2022)</a> showed that coarse graining is part of the thermodynamic question rather than a harmless implementation detail, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that BOLD changes can oppose oxygen-metabolism changes. A second correction is required by the partial-observation literature. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">Martínez et al. (2019)</a> showed that waiting-time asymmetry can reveal hidden dissipation even when observable current vanishes, <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">Hartich &amp; Godec (2024)</a> showed that this reading can fail when coarse-graining and time reversal do not commute, <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">Martínez et al. (2024)</a> replied by limiting the original claim to coarse-grainings that are local in time and, where needed, second-order semi-Markov constructions, and <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">Blom et al. (2024)</a> showed that coarse lumping can hide dissipative cycles and induce memory so that estimates from partial observations become far too small when the observed trajectory is naively treated as Markov. Therefore, the phrase "thermodynamic result" does not yet tell us which quantity was computed, whether an energetic interpretation is grounded, or whether the observed trajectory is thermodynamically closed enough for the chosen estimator. On this site, any such claim now needs an <strong>Irreversibility / Thermodynamic Route Card</strong>; the longer public rule is summarized in <a href="wiki/thermodynamic-grounding-basics.html#irreversibility-route-card">Wiki: irreversibility route card</a>.
</p>
</div>
<div class="key-points">
<h4>What can be said at the moment</h4>
<ul>
<li><strong>Breach of detailed equilibrium can be observed:</strong>There are studies that estimate the lower bound of entropy production from brain activity, and it is supported that irreversibility contains information about neural dynamics. </li>
<li><strong>However, interpretation is route-dependent:</strong>The relationship between state of consciousness and irreversibility has also been reported in fMRI, ECoG, etc., but the appearance changes depending on coarse-graining, temporal resolution, preprocessing, source model, estimator family, and explicit model assumptions. EEG/ECoG/fMRI irreversibility should not be equated with metabolic dissipation or hardware power. </li>
<li><strong>Therefore, we do not use it as a gate condition:</strong>At this stage, thermodynamic indicators alone do not determine WBE identity or validity. </li>
</ul>
</div>
<div class="key-points">
<h4>Minimum reporting rule</h4>
<ul>
<li><strong>Route-card disclosure:</strong> Write signal route and state definition, coarse-graining / timescale, observed-state closure / hidden-degree risk, estimator family, and whether the reported number is a lower bound, asymmetry score, or model-based entropy-flow estimate. </li>
<li><strong>Dynamical-assumption disclosure:</strong> Name steady-state, Markov, pairwise, conditional-independence, source-model, or other explicit assumptions that materially shape the estimate. </li>
<li><strong>Memory-order / decimation disclosure:</strong> State whether the observed process is treated as Markov, 1st/2nd-order semi-Markov, or higher-order non-Markov, whether coarse-graining and time reversal commute under the adopted construction, which hidden states / cycles were collapsed, and whether waiting-time asymmetry or memory diagnostics were checked. </li>
<li><strong>Nulls and finite-data handling:</strong> Report time-reversal / label / trial shuffles, motion or nuisance controls, plus noise-floor, bootstrap, or rare-transition treatment when reverse transitions are sparse or absent. </li>
<li><strong>Physiology-side grounding when energetic language is used:</strong>Name calibrated CMRO<sub>2</sub>, FDG-PET, <sup>31</sup>P-MRS, or explicitly state that no direct metabolic route is present. </li>
<li><strong>Cost Isolation:</strong>We report hardware power, wall-clock energy, FLOPs, and communication costs separately, and treat the approximately 20W of biological brains only as a background value for comparison. </li>
<li><strong>Submitted as ancillary indicators:</strong>Read alongside existing reproducibility indicators, source validation, perturbed responses, baseline comparisons, and do not draw conclusions on their own. </li>
<li><strong>Declare abstention explicitly:</strong>State what remains unresolved, such as microscopic dissipation, direct metabolic cost, direct causal wiring, or identity-relevant sameness. </li>
</ul>
</div>
<div class="note-box">
<strong>What to do now with this repository</strong>
<p>
In this repository, we do not make thermodynamic indicators a "required submission," but rather leave them at the stage where route-card reporting, literature monitoring, and estimation-error auditing are in place. This will be treated as an exploratory auxiliary analysis until stable within-modality operation is confirmed.
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
<li>Ahlfors, S. P., Han, J., Belliveau, J. W., &amp; H&auml;m&auml;l&auml;inen, M. S. (2010). Sensitivity of MEG and EEG to source orientation. <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">doi:10.1007/s10548-010-0154-x</a></li>
<li>Ahlfors, S. P., Han, J., Lin, F.-H., Witzel, T., Belliveau, J. W., H&auml;m&auml;l&auml;inen, M. S., &amp; Halgren, E. (2010). Cancellation of EEG and MEG signals generated by extended and distributed sources. <a href="https://doi.org/10.1002/hbm.20851" target="_blank">doi:10.1002/hbm.20851</a></li>
<li>Goldenholz, D. M., Ahlfors, S. P., H&auml;m&auml;l&auml;inen, M. S., Sharon, D., Ishitobi, M., Vaina, L. M., &amp; Stufflebeam, S. M. (2009). Mapping the signal-to-noise-ratios of cortical sources in magnetoencephalography and electroencephalography. <a href="https://doi.org/10.1002/hbm.20571" target="_blank">doi:10.1002/hbm.20571</a></li>
<li>Mahjoory, K., Nikulin, V. V., Botrel, L., et al. (2017). Consistency of EEG source localization and connectivity estimates. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.076" target="_blank">doi:10.1016/j.neuroimage.2017.02.076</a></li>
<li>Mikulan, E., Russo, S., Parmigiani, S., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Piastra, M. C., N&uuml;&szlig;ing, A., Vorwerk, J., Clerc, M., Engwer, C., &amp; Wolters, C. H. (2021). A comprehensive study on electroencephalography and magnetoencephalography sensitivity to cortical and subcortical sources. <a href="https://doi.org/10.1002/hbm.25272" target="_blank">doi:10.1002/hbm.25272</a></li>
<li>Vorwerk, J., Wolters, C. H., &amp; Baumgarten, D. (2024). Global sensitivity of EEG source analysis to tissue conductivity uncertainties. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">doi:10.3389/fnhum.2024.1335212</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Birot, G., Spinelli, L., Vulliemoz, S., et al. (2014). Head model and electrical source imaging: a study of 38 epileptic patients. <a href="https://doi.org/10.1016/j.nicl.2014.06.005" target="_blank">doi:10.1016/j.nicl.2014.06.005</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., Medine, D., Boulay, C., Grivich, M. I., Artoni, F., Mullen, T., Delorme, A., &amp; Makeig, S. (2025). The lab streaming layer for synchronized multimodal recording. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H., Jafarian, A., Zeidman, P., Litvak, V., Razi, A., Garrido, M., Friston, K., &amp; Daunizeau, J. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., Catana, C., Polimeni, J. R., Fan, J., Droppa, K. S., Patel, R., Wey, H.-Y., Chang, C., Manoach, D. S., Price, J. C., Sander, C. Y., &amp; Rosen, B. R. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T. S., van den Brink, R. L., Song, C., et al. (2025). Autonomic physiological coupling of the global fMRI signal. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Özbay, P. S., Chang, C., Picchioni, D., et al. (2019). Sympathetic activity contributes to the fMRI signal. <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Reveley, C., Seth, A. K., Pierpaoli, C., Silva, A. C., Yu, D., Saunders, R. C., Leopold, D. A., &amp; Ye, F. Q. (2015). Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">doi:10.1073/pnas.1418198112</a></li>
<li>Schilling, K. G., Gao, Y., Janve, V., Stepniewska, I., Landman, B. A., &amp; Anderson, A. W. (2018). Confirmation of a gyral bias in diffusion MRI fiber tractography. <a href="https://doi.org/10.1002/hbm.23936" target="_blank">doi:10.1002/hbm.23936</a></li>
<li>Sarwar, T., Ramamohanarao, K., Daducci, A., Schiavi, S., Smith, R. E., &amp; Zalesky, A. (2023). Evaluation of tractogram filtering methods using human-like connectome phantoms. <a href="https://doi.org/10.1016/j.neuroimage.2023.120376" target="_blank">doi:10.1016/j.neuroimage.2023.120376</a></li>
<li>Gajwani, M., Oldham, S., Pang, J. C., Arnatkevičiūtė, A., Tiego, J., Bellgrove, M. A., &amp; Fornito, A. (2023). Can hubs of the human connectome be identified consistently with diffusion MRI? <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">doi:10.1162/netn_a_00324</a></li>
<li>He, Y., Hong, Y., Wu, Y., et al. (2024). Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">doi:10.1016/j.neuroimage.2024.120904</a></li>
<li>McMaster, E. M., Newlin, N. R., Rudravaram, G., et al. (2025). Harmonized connectome resampling for variance in voxel sizes. <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">doi:10.1016/j.mri.2025.110424</a></li>
<li>Manzano-Patrón, J. P., Deistler, M., Schröder, C., et al. (2025). Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">doi:10.1016/j.media.2025.103580</a></li>
<li>Zhu, S., Huszar, I. N., Cottaar, M., et al. (2025). Imaging the structural connectome with hybrid MRI-microscopy tractography. <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">doi:10.1016/j.media.2025.103498</a></li>
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
<li>Deco, G., Sanz Perl, Y., Bocaccio, H., Tagliazucchi, E., &amp; Kringelbach, M. L. (2022). The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">doi:10.1038/s42003-022-03505-7</a></li>
<li>de la Fuente, L. A., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Martínez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2019). Inferring broken detailed balance in the absence of observable currents. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">doi:10.1038/s41467-019-11051-w</a></li>
<li>Hartich, D., &amp; Godec, A. (2024). Comment on “Inferring broken detailed balance in the absence of observable currents”. <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">doi:10.1038/s41467-024-52602-0</a></li>
<li>Martínez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2024). Reply to: Comment on “Inferring broken detailed balance in the absence of observable currents”. <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">doi:10.1038/s41467-024-52603-z</a></li>
<li>Blom, K., Song, K., Vouga, E., Godec, A., &amp; Makarov, D. E. (2024). Milestoning estimators of dissipation in systems observed at a coarse resolution. <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">doi:10.1073/pnas.2318333121</a></li>
<li>Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing. <a href="https://doi.org/10.1093/cercor/bhae415" target="_blank">doi:10.1093/cercor/bhae415</a></li>
<li>Fahrenfort, J. J., et al. (2025). Criterion placement threatens the construct validity of neural measures of consciousness. <a href="https://doi.org/10.7554/eLife.102335" target="_blank">doi:10.7554/eLife.102335</a></li>
<li>Gogulski, J., et al. (2024). Reliability of the TMS-evoked potential in dorsolateral prefrontal cortex. <a href="https://doi.org/10.1093/cercor/bhae130" target="_blank">doi:10.1093/cercor/bhae130</a></li>
<li>Biabani, M., et al. (2024). Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. <a href="https://doi.org/10.1162/imag_a_00349" target="_blank">doi:10.1162/imag_a_00349</a></li>
<li>Breyton, M., et al. (2025). Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms. <a href="https://doi.org/10.7554/eLife.98920" target="_blank">doi:10.7554/eLife.98920</a></li>
<li>Casarotto, S., et al. (2024). Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. <a href="https://doi.org/10.1111/ejn.16299" target="_blank">doi:10.1111/ejn.16299</a></li>
<li>Amiri, A. M., et al. (2022). Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/brain/awac335</a></li>
<li>Rohaut, B., et al. (2024). Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Manasova, D., et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/brain/awaf412</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu, S., Tyler, L. K., Henson, R. N. A., Rowe, J. B., Cam-CAN, &amp; Tsvetanov, K. A. (2023). Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Yucel, M. A. Y., Selb, J., Aasted, C. M. A., Petkov, M. P., Becerra, L., Borsook, D., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>Epp, S. M., Castrillon, G., Yuan, B., Andrews-Hanna, J., Preibisch, C., &amp; Riedl, V. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Bosch, C., Pacureanu, A., Patiño, J., et al. (2022). Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Attardo, A., Fitzgerald, J. E., &amp; Schnitzer, M. J. (2015). Impermanence of dendritic spines in live adult CA1 hippocampus. <a href="https://doi.org/10.1038/nature14467" target="_blank">doi:10.1038/nature14467</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Santoni, G., et al. (2024). Chromatin plasticity predetermines neuronal eligibility for memory trace formation. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">doi:10.1126/science.adg9982</a></li>
<li>Traunmüller, L., et al. (2025). Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">doi:10.1038/s41467-025-63029-6</a></li>
<li>Coda, D. M., Watt, L., Glauser, L., et al. (2025). Cell-type- and locus-specific epigenetic editing of memory expression. <a href="https://doi.org/10.1038/s41588-025-02368-y" target="_blank">doi:10.1038/s41588-025-02368-y</a></li>
<li>Terceros, A., Chen, C., Harada, Y., et al. (2026). Thalamocortical transcriptional gates coordinate memory stabilization. <a href="https://doi.org/10.1038/s41586-025-09774-6" target="_blank">doi:10.1038/s41586-025-09774-6</a></li>
<li>Wang, J., Telese, F., Tan, Y., et al. (2015). LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. <a href="https://doi.org/10.1038/nn.4069" target="_blank">doi:10.1038/nn.4069</a></li>
<li>Dai, J., Aoto, J., &amp; Südhof, T. C. (2019). Alternative splicing of presynaptic neurexins differentially controls postsynaptic NMDA and AMPA receptor responses. <a href="https://doi.org/10.1016/j.neuron.2019.03.032" target="_blank">doi:10.1016/j.neuron.2019.03.032</a></li>
<li>Shi, H., Zhang, X., Weng, Y.-L., et al. (2018). m6A facilitates hippocampus-dependent learning and memory through YTHDF1. <a href="https://doi.org/10.1038/s41586-018-0666-1" target="_blank">doi:10.1038/s41586-018-0666-1</a></li>
<li>Peterson, L. N., Kasper, J. M., Allgaier, J. A., et al. (2025). ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. <a href="https://doi.org/10.1126/scisignal.adr1442" target="_blank">doi:10.1126/scisignal.adr1442</a></li>
<li>Joglekar, A., Prjibelski, A., Mahfouz, A., et al. (2024). Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. <a href="https://doi.org/10.1038/s41593-024-01616-4" target="_blank">doi:10.1038/s41593-024-01616-4</a></li>
<li>Li, Y., Zhu, M., Li, X., et al. (2025). Enhanced Protein Synthesis and Hippocampus-Dependent Memory via Inhibition of YTHDF2-Mediated m6A mRNA Degradation. <a href="https://doi.org/10.1002/advs.202514926" target="_blank">doi:10.1002/advs.202514926</a></li>
<li>Giese, K. P., Fedorov, N. B., Filipkowski, R. K., &amp; Silva, A. J. (1998). Autophosphorylation at Thr286 of the alpha calcium-calmodulin kinase II in LTP and learning. <a href="https://doi.org/10.1126/science.279.5352.870" target="_blank">doi:10.1126/science.279.5352.870</a></li>
<li>Lee, H.-K., Barbarosie, M., Kameyama, K., Bear, M. F., &amp; Huganir, R. L. (2003). Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">doi:10.1016/S0092-8674(03)00122-3</a></li>
<li>Rodrigues, S. M., Farb, C. R., Bauer, E. P., LeDoux, J. E., &amp; Schafe, G. E. (2004). Pavlovian fear conditioning regulates Thr286 autophosphorylation of Ca2+/calmodulin-dependent protein kinase II at lateral amygdala synapses. <a href="https://doi.org/10.1523/JNEUROSCI.5303-03.2004" target="_blank">doi:10.1523/JNEUROSCI.5303-03.2004</a></li>
<li>Tomita, S., Stein, V., Stocker, T. J., Nicoll, R. A., &amp; Bredt, D. S. (2005). Bidirectional synaptic plasticity regulated by phosphorylation of stargazin-like TARPs. <a href="https://doi.org/10.1016/j.neuron.2005.01.009" target="_blank">doi:10.1016/j.neuron.2005.01.009</a></li>
<li>Havekes, R., Park, A. J., Tolentino, R. E., et al. (2016). Compartmentalized PDE4A5 signaling impairs hippocampal synaptic plasticity and long-term memory. <a href="https://doi.org/10.1523/JNEUROSCI.0248-16.2016" target="_blank">doi:10.1523/JNEUROSCI.0248-16.2016</a></li>
<li>Vierra, N. C., et al. (2023). Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">doi:10.1038/s41467-023-40930-6</a></li>
<li>Altas, B., Tuffy, L. P., Patrizi, A., et al. (2024). Region-specific phosphorylation determines Neuroligin-3 localization to excitatory versus inhibitory synapses. <a href="https://doi.org/10.1016/j.biopsych.2023.12.020" target="_blank">doi:10.1016/j.biopsych.2023.12.020</a></li>
<li>Rodriguez, A. C., Kramár, E. A., Augustynski, A. S., et al. (2025). HDAC3 Serine 424 phospho-mimic and phospho-null mutants bidirectionally modulate long-term memory formation and synaptic plasticity in the adult and aging mouse brain. <a href="https://doi.org/10.1523/JNEUROSCI.1619-24.2025" target="_blank">doi:10.1523/JNEUROSCI.1619-24.2025</a></li>
<li>Biswas, D., et al. (2023). The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. <a href="https://doi.org/10.1021/acs.jproteome.2c00244" target="_blank">doi:10.1021/acs.jproteome.2c00244</a></li>
<li>Frey, U., &amp; Morris, R. G. M. (1997). Synaptic tagging and long-term potentiation. <a href="https://doi.org/10.1038/385533a0" target="_blank">doi:10.1038/385533a0</a></li>
<li>Fonseca, R., Vabulas, R. M., Hartl, F. U., Bonhoeffer, T., &amp; Nägerl, U. V. (2006). A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">doi:10.1016/j.neuron.2006.08.015</a></li>
<li>Govindarajan, A., Israely, I., Huang, S.-Y., &amp; Tonegawa, S. (2011). The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">doi:10.1016/j.neuron.2010.12.008</a></li>
<li>Shires, K. L., Da Silva, B. M., Hawthorne, J. P., Morris, R. G. M., &amp; Martin, S. J. (2012). Synaptic tagging and capture in the living rat. <a href="https://doi.org/10.1038/ncomms2250" target="_blank">doi:10.1038/ncomms2250</a></li>
<li>Pandey, K., Yu, X.-W., Steinmetz, A., &amp; Alberini, C. M. (2021). Autophagy coupled to translation is required for long-term memory formation. <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">doi:10.1080/15548627.2020.1775393</a></li>
<li>Thomas, M., Bogaciu, C.-A., Rizzoli, S. O., et al. (2025). Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">doi:10.1038/s42003-025-08459-0</a></li>
<li>Park, M., Salgado, J. M., Ostroff, L., Helton, T. D., Robinson, C. G., Harris, K. M., &amp; Ehlers, M. D. (2006). Plasticity-induced growth of dendritic spines by exocytic trafficking from recycling endosomes. <a href="https://doi.org/10.1016/j.neuron.2006.09.040" target="_blank">doi:10.1016/j.neuron.2006.09.040</a></li>
<li>Correia, S. S., Bassani, S., Brown, T. C., Lisé, M.-F., Backos, D. S., El-Husseini, A., Passafaro, M., &amp; Esteban, J. A. (2008). Motor protein-dependent transport of AMPA receptors into spines during long-term potentiation. <a href="https://doi.org/10.1038/nn2063" target="_blank">doi:10.1038/nn2063</a></li>
<li>Maas, C., Belgardt, D., Lee, H. K., Heisler, F. F., Lappe-Siefke, C., Magiera, M. M., van Dijk, J., Hausrat, T. J., Janke, C., &amp; Kneussel, M. (2009). Synaptic activation modifies microtubules underlying transport of postsynaptic cargo. <a href="https://doi.org/10.1073/pnas.0902304106" target="_blank">doi:10.1073/pnas.0902304106</a></li>
<li>Uchida, S., Martel, G., Pavlowsky, A., Takizawa, S., Hevi, C., Watanabe, Y., Alarcon, J. M., &amp; Shumyatsky, G. P. (2014). Learning-induced and stathmin-dependent changes in microtubule stability are critical for memory and disrupted in ageing. <a href="https://doi.org/10.1038/ncomms5389" target="_blank">doi:10.1038/ncomms5389</a></li>
<li>Yin, X., Takei, Y., Kido, M. A., &amp; Hirokawa, N. (2011). Molecular motor KIF17 is fundamental for memory and learning via differential support of synaptic NR2A/2B levels. <a href="https://doi.org/10.1016/j.neuron.2011.03.026" target="_blank">doi:10.1016/j.neuron.2011.03.026</a></li>
<li>Zhao, J., Fok, A. H. K., Fan, R., Kwan, P.-Y., Chan, H.-L., Lo, L. H.-Y., Chan, Y.-S., Yung, W.-H., Huang, J., Lai, C. S. W., &amp; Lai, K.-O. (2020). Specific depletion of the motor protein KIF5B leads to deficits in dendritic transport, synaptic plasticity and memory. <a href="https://doi.org/10.7554/eLife.53456" target="_blank">doi:10.7554/eLife.53456</a></li>
<li>Swarnkar, S., Avchalumov, Y., Espadas, I., Grinman, E., Liu, X.-A., Raveendra, B. L., Zucca, A., Mediouni, S., Sadhu, A., Valente, S., Page, D., Miller, K., &amp; Puthanveettil, S. V. (2021). Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">doi:10.1016/j.celrep.2021.109369</a></li>
<li>Wong, V. C., Houlihan, P. R., Liu, H., Walpita, D., DeSantis, M. C., Liu, Z., &amp; O'Shea, E. K. (2024). Plasticity-induced actin polymerization in the dendritic shaft regulates intracellular AMPA receptor trafficking. <a href="https://doi.org/10.7554/eLife.80622" target="_blank">doi:10.7554/eLife.80622</a></li>
<li>Aiken, J., &amp; Holzbaur, E. L. F. (2024). Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">doi:10.1016/j.cub.2024.03.010</a></li>
<li>de Queiroz, B. R., Laghrissi, H., Rajeev, S., Blot, L., De Graeve, F., Dehecq, M., Keleman, K., Ule, J., Hubstenberger, A., &amp; Besse, F. (2025). Axonal RNA localization is essential for long-term memory. <a href="https://doi.org/10.1038/s41467-025-57651-7" target="_blank">doi:10.1038/s41467-025-57651-7</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Villaverde, A. F. (2019). Observability and Structural Identifiability of Nonlinear Biological Systems. <em>Complexity</em>, 2019, 8497093. <a href="https://doi.org/10.1155/2019/8497093" target="_blank">doi:10.1155/2019/8497093</a></li>
<li>Villaverde, A. F., Tsiantis, N., &amp; Banga, J. R. (2019). Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. <em>Journal of The Royal Society Interface</em>, 16(156), 20190043. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Rasero, J., Betzel, R., Sentis, A. I., Kraynak, T. E., Gianaros, P. J., &amp; Verstynen, T. (2024). Similarity in evoked responses does not imply similarity in macroscopic network states. <em>Network Neuroscience</em>, 8(1), 335-354. <a href="https://doi.org/10.1162/netn_a_00354" target="_blank">doi:10.1162/netn_a_00354</a></li>
<li>Liu, X., Wanika, L., Chappell, M. J., &amp; Branke, J. (2025). Efficient data collection for establishing practical identifiability via active learning. <em>Computational and Structural Biotechnology Journal</em>, 27, 4992-5006. <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">doi:10.1016/j.csbj.2025.10.058</a></li>
<li>Shiu, P.-K., et al. (2024). A Drosophila computational brain model reveals sensorimotor processing. <a href="https://doi.org/10.1038/s41586-024-07763-9" target="_blank">doi:10.1038/s41586-024-07763-9</a></li>
<li>Pospisil, D. A., et al. (2024). The fly connectome reveals a path to the effectome. <a href="https://doi.org/10.1038/s41586-024-07982-0" target="_blank">doi:10.1038/s41586-024-07982-0</a></li>
<li>Galarreta, M., &amp; Hestrin, S. (1999). A network of fast-spiking cells in the neocortex connected by electrical synapses. <a href="https://doi.org/10.1038/47029" target="_blank">doi:10.1038/47029</a></li>
<li>Anastassiou, C. A., Perin, R., Markram, H., &amp; Koch, C. (2011). Ephaptic coupling of cortical neurons. <a href="https://doi.org/10.1038/nn.2727" target="_blank">doi:10.1038/nn.2727</a></li>
<li>Yang, Y.-C., Wang, G.-H., Chou, P., Hsueh, S.-W., Lai, Y.-C., &amp; Kuo, C.-C. (2024). Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. <a href="https://doi.org/10.1073/pnas.2313042121" target="_blank">doi:10.1073/pnas.2313042121</a></li>
<li>Selfe, J. S., et al. (2024). All-optical reporting of inhibitory receptor driving force in the nervous system. <a href="https://doi.org/10.1038/s41467-024-53074-y" target="_blank">doi:10.1038/s41467-024-53074-y</a></li>
<li>Feld, G. B., Niethard, N., Liu, J., et al. (2026). Electrical synapses contribute to sleep-dependent declarative memory retention. <a href="https://doi.org/10.1111/ejn.70401" target="_blank">doi:10.1111/ejn.70401</a></li>
<li>Pizzorusso, T., Medini, P., Berardi, N., Chierzi, S., Fawcett, J. W., &amp; Maffei, L. (2002). Reactivation of ocular dominance plasticity in the adult visual cortex. <a href="https://doi.org/10.1126/science.1072699" target="_blank">doi:10.1126/science.1072699</a></li>
<li>Frischknecht, R., Heine, M., Perrais, D., Seidenbecher, C. I., Choquet, D., &amp; Gundelfinger, E. D. (2009). Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. <a href="https://doi.org/10.1038/nn.2338" target="_blank">doi:10.1038/nn.2338</a></li>
<li>Gogolla, N., Caroni, P., Lüthi, A., &amp; Herry, C. (2009). Perineuronal nets protect fear memories from erasure. <a href="https://doi.org/10.1126/science.1174146" target="_blank">doi:10.1126/science.1174146</a></li>
<li>Jabłońska, K., Kaczor, K., Kółeczko, M., et al. (2024). Extracellular matrix integrity regulates GABAergic plasticity in the hippocampus. <a href="https://doi.org/10.1016/j.matbio.2024.11.001" target="_blank">doi:10.1016/j.matbio.2024.11.001</a></li>
<li>Boonen, M., Hellings, N., Hoedemaekers, T., et al. (2022). Reorganization of the brain extracellular matrix in hippocampal sclerosis. <a href="https://doi.org/10.3390/ijms23158197" target="_blank">doi:10.3390/ijms23158197</a></li>
<li>Nguyen, P. T., Dorman, L. C., Pan, S., et al. (2020). Microglial Remodeling of the Extracellular Matrix Promotes Synapse Plasticity. <a href="https://doi.org/10.1016/j.cell.2020.05.050" target="_blank">doi:10.1016/j.cell.2020.05.050</a></li>
<li>Lehner, A., Hoffmann, L., Rampp, S., et al. (2024). Age-dependent increase of perineuronal nets in the human hippocampus and precocious aging in epilepsy. <a href="https://doi.org/10.1002/epi4.12963" target="_blank">doi:10.1002/epi4.12963</a></li>
<li>Alexander, G. M., Nikolova, V. D., Stöber, T. M., Gruzdev, A., Moy, S. S., &amp; Dudek, S. M. (2025). Perineuronal Nets on CA2 Pyramidal Cells and Parvalbumin-Expressing Cells Differentially Regulate Hippocampal-Dependent Memory. <a href="https://doi.org/10.1523/JNEUROSCI.1626-24.2024" target="_blank">doi:10.1523/JNEUROSCI.1626-24.2024</a></li>
<li>Banovac, I., Prkačin, M. V., Kirchbaum, I., et al. (2025). Morphological and Molecular Characteristics of Perineuronal Nets in the Human Prefrontal Cortex-A Possible Link to Microcircuitry Specialization. <a href="https://doi.org/10.1007/s12035-024-04306-1" target="_blank">doi:10.1007/s12035-024-04306-1</a></li>
<li>Mehak, S. F., Shivakumar, A. B., Jijimon, F., Gupta, A., Pillai, V. G., &amp; Gangadharan, G. (2025). Targeting CA2 Perineuronal Nets Restores Recognition Memory and Theta Oscillations in Aged Mice. <a href="https://doi.org/10.1111/acel.70139" target="_blank">doi:10.1111/acel.70139</a></li>
<li>Glykys, J., Dzhala, V., Egawa, K., Balena, T., Saponjian, Y., Kuchibhotla, K. V., Bacskai, B. J., Kahle, K. T., Zeuthen, T., &amp; Staley, K. J. (2014). Local impermeant anions establish the neuronal chloride concentration. <a href="https://doi.org/10.1126/science.1245423" target="_blank">doi:10.1126/science.1245423</a></li>
<li>Heubl, M., Zhang, J., Pressey, J. C., Al Awabdh, S., Renner, M., Gomez-Castro, F., Moutkine, I., Eugène, E., Russeau, M., Kahle, K. T., Poncer, J.-C., &amp; Lévi, S. (2017). GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">doi:10.1038/s41467-017-01749-0</a></li>
<li>Ding, F., O'Donnell, J., Xu, Q., Kang, N., Goldman, N., &amp; Nedergaard, M. (2016). Changes in the composition of brain interstitial ions control the sleep-wake cycle. <a href="https://doi.org/10.1126/science.aad4821" target="_blank">doi:10.1126/science.aad4821</a></li>
<li>Huberfeld, G., Wittner, L., Clemenceau, S., Baulac, M., Kaila, K., Miles, R., &amp; Rivera, C. (2007). Perturbed chloride homeostasis and GABAergic signaling in human temporal lobe epilepsy. <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">doi:10.1523/JNEUROSCI.2761-07.2007</a></li>
<li>Qian, Y., Zhao, T., Zheng, H., Weimer, J., &amp; Boada, F. E. (2012). High-resolution sodium imaging of human brain at 7 T. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">doi:10.1002/mrm.23225</a></li>
<li>Forsberg, M., Olsson, M., Seth, H., Wasling, P., Zetterberg, H., Hedner, J., &amp; Hanse, E. (2022). Ion concentrations in cerebrospinal fluid in wakefulness, sleep and sleep deprivation in healthy humans. <a href="https://doi.org/10.1111/jsr.13522" target="_blank">doi:10.1111/jsr.13522</a></li>
<li>Byvaltsev, E., Behbood, M., Schleimer, J.-H., Gensch, T., Semyanov, A., Schreiber, S., &amp; Strauss, U. (2023). KCC2 reverse mode helps to clear postsynaptically released potassium at glutamatergic synapses. <a href="https://doi.org/10.1016/j.celrep.2023.112934" target="_blank">doi:10.1016/j.celrep.2023.112934</a></li>
<li>Alfonsa, H., Chakrabarty, A., Vyazovskiy, V. V., &amp; Akerman, C. J. (2025). Sleep-wake-related changes in intracellular chloride regulate plasticity at glutamatergic cortical synapses. <a href="https://doi.org/10.1016/j.cub.2025.01.050" target="_blank">doi:10.1016/j.cub.2025.01.050</a></li>
<li>Qian, Y., Lin, Y.-C., Chen, X., Ge, Y., Lui, Y. W., &amp; Boada, F. E. (2025). Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">doi:10.1038/s41598-025-07800-1</a></li>
<li>Hardingham, N. R., &amp; Larkman, A. U. (1998). The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">doi:10.1111/j.1469-7793.1998.249bu.x</a></li>
<li>Volgushev, M., Vidyasagar, T. R., Chistiakova, M., Yousef, T., &amp; Eysel, U. T. (2000). Membrane properties and spike generation in rat visual cortical cells during reversible cooling. <a href="https://doi.org/10.1111/j.1469-7793.2000.00059.x" target="_blank">doi:10.1111/j.1469-7793.2000.00059.x</a></li>
<li>Moser, E., Mathiesen, I., &amp; Andersen, P. (1993). Association between brain temperature and dentate field potentials in exploring and swimming rats. <a href="https://doi.org/10.1126/science.8446900" target="_blank">doi:10.1126/science.8446900</a></li>
<li>Long, M. A., &amp; Fee, M. S. (2008). Using temperature to analyse temporal dynamics in the songbird motor pathway. <a href="https://doi.org/10.1038/nature07448" target="_blank">doi:10.1038/nature07448</a></li>
<li>Owen, S. F., Liu, M. H., &amp; Kreitzer, A. C. (2019). Thermal constraints on in vivo optogenetic manipulations. <a href="https://doi.org/10.1038/s41593-019-0422-3" target="_blank">doi:10.1038/s41593-019-0422-3</a></li>
<li>Rangaraju, V., Calloway, N., &amp; Ryan, T. A. (2014). Activity-driven local ATP synthesis is required for synaptic function. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">doi:10.1016/j.cell.2013.12.042</a></li>
<li>Rangaraju, V., Lauterbach, M., &amp; Schuman, E. M. (2019). Spatially stable mitochondrial compartments fuel local translation during plasticity. <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">doi:10.1016/j.cell.2018.12.013</a></li>
<li>Divakaruni, S. S., Van Dyke, A. M., Chandra, R., et al. (2018). Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">doi:10.1016/j.neuron.2018.09.025</a></li>
<li>Underwood, E. L., Redell, J. B., Hood, K. N., et al. (2023). Enhanced presynaptic mitochondrial energy production is required for memory formation. <a href="https://doi.org/10.1038/s41598-023-40877-0" target="_blank">doi:10.1038/s41598-023-40877-0</a></li>
<li>Bapat, P., Nirschl, J. J., Wilkerson, J. R., et al. (2024). VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">doi:10.1038/s41467-023-44233-8</a></li>
<li>Hu, H., Tang, J., Wu, Y., et al. (2025). Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">doi:10.1038/s42003-025-08963-3</a></li>
<li>Vishwanath, A. A., Comyn, T., Mira, R. G., et al. (2026). Mitochondrial Ca2+ efflux controls neuronal metabolism and long-term memory across species. <a href="https://doi.org/10.1038/s42255-026-01451-w" target="_blank">doi:10.1038/s42255-026-01451-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Bhogal, A. A., Broeders, T. A. A., Morsinkhof, L., et al. (2020). Lipid-suppressed and tissue-fraction corrected metabolic distributions in human central brain structures using 2D <sup>1</sup>H magnetic resonance spectroscopic imaging at 7 T. <a href="https://doi.org/10.1002/brb3.1852" target="_blank">doi:10.1002/brb3.1852</a></li>
<li>Wright, A. M., Murali-Manohar, S., &amp; Henning, A. (2022). Quantitative T<sub>1</sub>-relaxation corrected metabolite mapping of 12 metabolites in the human brain at 9.4 T. <a href="https://doi.org/10.1016/j.neuroimage.2022.119574" target="_blank">doi:10.1016/j.neuroimage.2022.119574</a></li>
<li>Baboli, M., Wang, F., Dong, Z., et al. (2024). Absolute Metabolite Quantification in Individuals with Glioma and Healthy Individuals Using Whole-Brain Three-dimensional MR Spectroscopic and Echo-planar Time-resolved Imaging. <a href="https://doi.org/10.1148/radiol.232401" target="_blank">doi:10.1148/radiol.232401</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Rzechorzek, N. M., Thrippleton, M. J., Chappell, F. M., et al. (2022). A daily temperature rhythm in the human brain predicts survival after brain injury. <a href="https://doi.org/10.1093/brain/awab466" target="_blank">doi:10.1093/brain/awab466</a></li>
<li>Rogala, J., et al. (2024). Local variation in brain temperature explains gender-specificity of working memory performance. <a href="https://doi.org/10.3389/fnhum.2024.1398034" target="_blank">doi:10.3389/fnhum.2024.1398034</a></li>
<li>Tan, Y., Liu, W., Li, Y., et al. (2025). Measurement of Healthy Adult Brain Temperature Using <sup>1</sup>H Magnetic Resonance Spectroscopy Thermometry. <a href="https://doi.org/10.1007/s00062-024-01467-3" target="_blank">doi:10.1007/s00062-024-01467-3</a></li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Louveau, A., Smirnov, I., Keyes, T. J., et al. (2015). Structural and functional features of central nervous system lymphatic vessels. <a href="https://doi.org/10.1038/nature14432" target="_blank">doi:10.1038/nature14432</a></li>
<li>Ahn, J. H., Cho, H., Kim, J.-H., et al. (2019). Meningeal lymphatic vessels at the skull base drain cerebrospinal fluid. <a href="https://doi.org/10.1038/s41586-019-1419-5" target="_blank">doi:10.1038/s41586-019-1419-5</a></li>
<li>Kim, J., et al. (2025). Meningeal lymphatics-microglia axis regulates synaptic physiology. <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">doi:10.1016/j.cell.2025.02.022</a></li>
<li>Eide, P. K., &amp; Ringstad, G. (2021). Sleep deprivation impairs molecular clearance from the human brain. <a href="https://doi.org/10.1093/brain/awaa443" target="_blank">doi:10.1093/brain/awaa443</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Goulas, A., Changeux, J.-P., Wagstyl, K., Amunts, K., Palomero-Gallagher, N., &amp; Hilgetag, C. C. (2021). The natural axis of transmitter receptor distribution in the human cerebral cortex. <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">doi:10.1073/pnas.2020574118</a></li>
<li>Naganawa, M., Li, S., Nabulsi, N., et al. (2021). First-in-human evaluation of <sup>18</sup>F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">doi:10.2967/jnumed.120.249144</a></li>
<li>Smart, K., Liu, H., Matuskey, D., et al. (2021). Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">doi:10.1177/0271678X20946198</a></li>
<li>Shatalina, E., Onwordi, E. C., Whitehurst, T., et al. (2024). The relationship between SV2A levels, neural activity, and cognitive function in healthy humans: A [<sup>11</sup>C]UCB-J PET and fMRI study. <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">doi:10.1162/imag_a_00190</a></li>
<li>Holmes, S. E., Finnema, S. J., Naganawa, M., et al. (2022). Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">doi:10.1038/s41380-022-01465-2</a></li>
<li>Wong, D. F., Kuwabara, H., Hsu, D. J., et al. (2013). Determination of dopamine D<sub>2</sub> receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">doi:10.1007/s00213-013-3103-z</a></li>
<li>Koepp, M. J., Gunn, R. N., Lawrence, A. D., et al. (1998). Evidence for striatal dopamine release during a video game. <a href="https://doi.org/10.1038/30498" target="_blank">doi:10.1038/30498</a></li>
<li>Lippert, R. N., Cremer, A. L., Edwin Thanarajah, S., et al. (2019). Time-dependent assessment of stimulus-evoked regional dopamine release. <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">doi:10.1038/s41467-018-08143-4</a></li>
<li>Erritzoe, D., Ashok, A. H., Searle, G. E., et al. (2020). Serotonin release measured in the human brain: a PET study with [<sup>11</sup>C]CIMBI-36 and d-amphetamine challenge. <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">doi:10.1038/s41386-019-0567-5</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Villemagne, V. L., Harada, R., Dore, V., et al. (2022). First-in-Humans Evaluation of <sup>18</sup>F-SMBT-1, a Novel <sup>18</sup>F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">doi:10.2967/jnumed.121.263255</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Williamson, N. R., et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">doi:10.1038/s41586-024-08170-w</a></li>
<li>Dewa, K., et al. (2025). The astrocytic ensemble acts as a multiday trace to stabilize memory. <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">doi:10.1038/s41586-025-09619-2</a></li>
<li>Bukalo, O., et al. (2026). Astrocytes enable amygdala neural representations supporting memory. <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">doi:10.1038/s41586-025-10068-0</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2025). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Stringer, C., Pachitariu, M., Steinmetz, N., et al. (2019). Spontaneous behaviors drive multidimensional, brainwide activity. <a href="https://doi.org/10.1126/science.aav7893" target="_blank">doi:10.1126/science.aav7893</a></li>
<li>Saleem, A. B., Ayaz, A., Jeffery, K. J., Harris, K. D., &amp; Carandini, M. (2013). Integration of visual motion and locomotion in mouse visual cortex. <a href="https://doi.org/10.1038/nn.3567" target="_blank">doi:10.1038/nn.3567</a></li>
<li>Ravassard, P., Kees, A., Willers, B., et al. (2013). Multisensory control of hippocampal spatiotemporal selectivity. <a href="https://doi.org/10.1126/science.1232655" target="_blank">doi:10.1126/science.1232655</a></li>
<li>Zelano, C., Jiang, H., Zhou, G., et al. (2016). Nasal respiration entrains human limbic oscillations and modulates cognitive function. <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">doi:10.1523/JNEUROSCI.2586-16.2016</a></li>
<li>Raut, R. V., Rosenthal, Z. P., Wang, X., et al. (2025). Arousal as a universal embedding for spatiotemporal brain dynamics. <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">doi:10.1038/s41586-025-09544-4</a></li>
<li>Ngo, H.-V. V., Martinetz, T., Born, J., &amp; Mölle, M. (2013). Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. <a href="https://doi.org/10.1016/j.neuron.2013.03.006" target="_blank">doi:10.1016/j.neuron.2013.03.006</a></li>
<li>Maingret, N., Girardeau, G., Todorova, R., et al. (2016). Hippocampo-cortical coupling mediates memory consolidation during sleep. <a href="https://doi.org/10.1038/nn.4304" target="_blank">doi:10.1038/nn.4304</a></li>
<li>Latchoumane, C.-F. V., Ngo, H.-V. V., Born, J., &amp; Shin, H.-S. (2017). Thalamic Spindles Promote Memory Formation during Sleep through Triple Phase-Locking of Cortical, Thalamic, and Hippocampal Rhythms. <a href="https://doi.org/10.1016/j.neuron.2017.06.025" target="_blank">doi:10.1016/j.neuron.2017.06.025</a></li>
<li>Schreiner, T., Petzka, M., Staudigl, T., &amp; Staresina, B. P. (2021). Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. <a href="https://doi.org/10.1038/s41467-021-23520-2" target="_blank">doi:10.1038/s41467-021-23520-2</a></li>
<li>Geva-Sagiv, M., Mankin, E. A., Eliashiv, D., et al. (2023). Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans. <a href="https://doi.org/10.1038/s41593-023-01324-5" target="_blank">doi:10.1038/s41593-023-01324-5</a></li>
<li>Schreiner, T., Petzka, M., Staudigl, T., et al. (2024). Spindle-locked ripples mediate memory reactivation during human NREM sleep. <a href="https://doi.org/10.1038/s41467-024-49572-8" target="_blank">doi:10.1038/s41467-024-49572-8</a></li>
<li>Deng, Z., Fei, X., Zhang, S., &amp; Xu, M. (2025). A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. <a href="https://doi.org/10.1016/j.neuron.2025.03.020" target="_blank">doi:10.1016/j.neuron.2025.03.020</a></li>
<li>Duan, W., Xu, Z., Chen, D., et al. (2025). Electrophysiological signatures underlying variability in human memory consolidation. <a href="https://doi.org/10.1038/s41467-025-57766-x" target="_blank">doi:10.1038/s41467-025-57766-x</a></li>
<li>Shin, G.-H., Kweon, Y.-S., Oh, S., et al. (2025). Personalized targeted memory reactivation enhances consolidation of challenging memories via slow wave and spindle dynamics. <a href="https://doi.org/10.1038/s41539-025-00340-3" target="_blank">doi:10.1038/s41539-025-00340-3</a></li>
<li>Kostas, D., Aroca-Ouellette, S., &amp; Rudzicz, F. (2021). BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">doi:10.3389/fnhum.2021.653659</a></li>
<li>Jiang, W.-B., Zhao, L., &amp; Lu, B.-L. (2024). Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">ICLR 2024 proceedings</a></li>
<li>Lee, N., Barmpas, K., Panagakis, Y., Adamos, D., Laskaris, N., &amp; Zafeiriou, S. (2025). Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">ICML 2025 poster / OpenReview</a></li>
<li>EEG Challenge (2025). Rules. <a href="https://eeg2025.github.io/rules/" target="_blank">official rules</a></li>
<li>Xiong, W., Li, J., Li, J., Zhu, K., &amp; Jiang, C. (2025). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
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
