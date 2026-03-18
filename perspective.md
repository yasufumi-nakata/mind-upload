---
layout: default
title: "Toward Mind Uploading: An Integrated Technical and Theoretical Approach"
description: "A research note that audits theories, measurement paths, and implementation routes for mind uploading/WBE against primary literature and known limits."
article_type: Perspective
subtitle: "Audit the hypothesis of reproducing brain information processing on another substrate through the barriers of measurability, identifiability, and maintenance state"
author: Mind Uploading Research Project
last_updated: '2026-03-19'
note: "Research note (updated with the March 2026 re-audit)"
audience: "Readers who want to follow theory all the way into implementation, including limits and objections"
reading_time: "30-45 min"
page_intro: "This page is a long research note that follows the theoretical, measurement, and implementation questions around mind uploading while keeping primary literature and hard limits side by side. It is written to separate what can reasonably be claimed now from what remains unresolved, rather than leaning into either pure optimism or pure pessimism."
accuracy_note: "This page does not assume that any specific theory of consciousness has already been proven correct. Supportive evidence and unresolved points are treated separately."
page_highlights:
  - "It does not stop at introducing theories; it follows the constraints that appear when those theories are pushed toward implementation."
  - "The page now separates local connectomics, human structural scaffold evidence, synaptic-density PET, macro energetic / myelin / ionic proxies, and hemodynamic transfer audits instead of collapsing them into one 'multimodal' advance."
  - "The connectome-dynamics gap is now written as a 10-class latent-state problem rather than a loose warning that wiring alone is not enough."
  - "The stronger the claim, the more explicitly it is checked against falsification criteria, alternative explanations, and abstention conditions."
  - "Even though it is long, the introduction and framing notes alone should make the page's overall stance clear."
known_points:
  - "No major theory has become a decisive standalone answer at this point."
  - "EEG alone is constrained by inverse-problem uncertainty and spatial resolution limits, so it is insufficient as the sole basis for strong claims."
  - "Progress in local connectomics or source imaging does not imply state-complete observation of the human whole brain."
  - "Human whole-brain evidence remains layered and proxy-based; no current route directly fixes current transcription / chromatin state, ECM / PNN gate state, local proteostasis / synaptic-tag capture, chloride set point, or branch-local mitochondrial positioning."
  - "Hemodynamic modalities carry vascular transfer / CVR uncertainty in addition to neural-side uncertainty."
  - "Strong claims that omit causal perturbation, reproducibility, and explicit exclusion of alternative explanations remain on shaky ground."
unknown_points:
  - "It remains unsettled which combination of theories, if any, will ultimately amount to a sufficient condition."
  - "Which combination of measurement classes could eventually reduce enough latent-state error for stronger WBE claims is still unsettled."
  - "How to connect final judgments about personhood and phenomenal consciousness to engineering criteria is unresolved."
wiki_links:
  - label: "Wiki: Consciousness Theory Map"
    url: "/wiki/consciousness-theory-map.html"
    description: "Explains the differences and roles of IIT, GNWT, FEP, and PCI from first principles."
  - label: "Wiki: Reading Partial Progress, Exploratory Stages, and Gaps"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "Clarifies how to read labels such as insufficient, uncertain, and unresolved on this page."
  - label: "Wiki: Personhood and the Copy Problem"
    url: "/wiki/personhood-and-copy-problem.html"
    description: "Explains the more philosophical issues that appear on this page in plain language."
  - label: "Wiki: EEG Preprocessing and QC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "Shows where EEG's limits come from by walking through the processing pipeline."
  - label: "Wiki: Observability and Claim Ceilings by Measurement Stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Explains what each modality directly observes and where each one hits its claim ceiling."
  - label: "Wiki: Homeostatic Plasticity and Maintenance State"
    url: "/wiki/homeostatic-plasticity-and-maintenance-state.html"
    description: "Adds background on maintenance-state variables such as sleep/wake dynamics, myelination, and glial metabolism."
  - label: "Wiki: How to Read Claims and Evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "A helper page for reading theoretical discussion through the lens of claim strength."
  - label: "Wiki: Closed Loops, Latency, Jitter, and Safety Stops"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Adds the basics of latency, jitter, and safety-stop design in closed-loop implementations."
  - label: "Wiki: Thermodynamic Grounding Basics"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Introduces Landauer, dissipation, NESS, and EPR from the ground up."
recommended_pages:
  - label: "Verification"
    url: "/verification.html"
  - label: "Roadmap"
    url: "/tech_roadmap.html"
  - label: "WBE 101"
    url: "/wbe_101.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<!-- Abstract -->
<div class="abstract-box">
<h2>Abstract</h2>
<p>This page is a long-form research note aimed at turning mind uploading (WBE) into something that can be evaluated as real research. It is organized in three stages: <strong>how to measure</strong>, <strong>how to infer</strong>, and <strong>how to implement</strong>. It treats recent results, failures, and limits with the same weight so that the boundary between what can and cannot be claimed remains explicit.</p>
</div>

<div class="cta-box">
<h4>Start Here: Verification Commons</h4>
<p>The core of Mind-Upload is to define progress up front and build a verification commons that lets different results be compared on the same basis.</p>
<a href="verification.html">Open Verification Commons -&gt;</a>
</div>

<div class="note-box">
<strong>If you are new here</strong>
<p>This is a long research note. It is easier to navigate if you first read <a href="wbe_101.html">WBE 101</a> and <a href="eeg_101.html">EEG 101</a>, and then return here with the <a href="glossary.html">Glossary</a> if needed.</p>
</div>

<div class="note-box">
<strong>If you need background first</strong>
<p>If you get stuck on the differences between major theories, start with the <a href="wiki/consciousness-theory-map.html">Wiki: Consciousness Theory Map</a>. If the copy problem or personhood questions are the blocker, use the <a href="wiki/personhood-and-copy-problem.html">Wiki: Personhood and the Copy Problem</a>. If the limits of EEG are the issue, go to the <a href="wiki/eeg-preprocessing-and-qc.html">Wiki: EEG Preprocessing and QC</a>. For the bridge from measurement terms to modeling terms, use the <a href="wiki/measurement-and-modeling-terms.html">Wiki: Measurement and Modeling Terms</a>. For uncertainty and abstention, use the <a href="wiki/uncertainty-confidence-and-abstention.html">Wiki: Uncertainty, Calibration, and Abstention</a>. For multimodal integration, use the <a href="wiki/multimodal-integration-basics.html">Wiki: Multimodal Integration Basics</a>. For longitudinal evaluation and drift, use the <a href="wiki/state-trait-and-drift.html">Wiki: State, Trait, and Drift</a>. For closed-loop latency and safety stops, use the <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed Loops, Latency, Jitter, and Safety Stops</a>. For thermodynamics and dissipation, use the <a href="wiki/thermodynamic-grounding-basics.html">Wiki: Thermodynamic Grounding Basics</a>.</p>
</div>
<div class="note-box">
<strong>When you are confused about the different roles of theory pages</strong>
<p>Perspective is a long notebook that brings together theories, measurements, counterarguments, limitations, and the design principles adopted on this site. If you want to align claim levels first, start with <a href="wbe_101.html">WBE 101</a>. If you want the dependency map, use the <a href="tech_roadmap.html">technology roadmap</a>. If you want a one-page guide to the theory section, see <a href="wiki/theory-pages-reading-guide.html">Wiki: Guide to reading theory pages</a>.</p>
</div>
<div class="note-box">
<strong>When you are confused between research notes, theoretical frames, proposals, and issues</strong>
<p>This page is a long-form research note that lists observations and limitations; it is not primarily a task list or a proposal list. If you want a one-page guide to the differences between facts, hypotheses, proposals, and execution tasks, please see <a href="wiki/facts-hypotheses-proposals-and-tasks.html">Wiki: Difference between fact, hypothesis, proposal, and execution task</a>.</p>
</div>
<div class="note-box">
<strong>When you want to see the theoretical route from WBE introduction to here</strong>
<p>If you want to see why the reading path moves from WBE 101 to this long note, including common misunderstandings and the shift toward design principles, please see <a href="wiki/wbe-to-theory-route.html">Wiki: 4 routes to deepen the theory from WBE introduction</a>.</p>
</div>
<div class="note-box">
<strong>When you want to separate the weight of “insufficient”, “unconfirmed”, and “unresolved”</strong>
<p>This page covers many limitations and counterarguments, so you need to distinguish clearly between <strong>partial solutions</strong>, <strong>exploration-stage results</strong>, and <strong>undeveloped areas</strong>. If you want a one-page guide to those progress labels, please read <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: How to read partial solution / exploration stage / undeveloped</a> first.</p>
</div>

<div class="key-points">
<h4>Things to check before reading</h4>
<ul>
<li><strong>Role of this page:</strong> This page does not simply list favorable positions; it tracks evidence and limitations at the same time.</li>
<li><strong>What you can say on this page:</strong> You can sort out what the major theories explain and where the main difficulties remain.</li>
<li><strong>Things that can't be said on this page alone:</strong> We have not reached the final conclusion that ``this completely explains consciousness.''</li>
</ul>
</div>

<div class="note-box">
<strong>Reading order when lost</strong>
<p>First confirm the overall position in the introduction, then read the <a href="#design-principles">design principles</a> section on thinking in terms of migration rather than copying, and only after that move into the measurement, modeling, and implementation sections. If you get stuck on a philosophical issue, it is often easier to step out to the <a href="faq.html">FAQ</a> and then return.</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Issues that interest me now</th>
<th>What to read first</th>
<th>What you can find out there</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to know where the main theory is failing.</td>
<td><a href="#introduction">Introduction</a></td>
<td>Be the first to see how we are repositioning IIT, GNWT, and FEP.</td>
</tr>
<tr>
<td>I want to see the overall design from measurement to implementation.</td>
<td><a href="#technical-framework">Technical Framework</a></td>
<td>You can follow the assumptions that connect the three stages of measurement, decoding, and implementation.</td>
</tr>
<tr>
<td>I want to know what is missing between decode and emulate</td>
<td><a href="#decoding-to-emulation-gap">Decoding to Emulation Gap</a></td>
<td>Correlation-based readouts reveal gaps to proceed to causal verification.</td>
</tr>
<tr>
<td>I want to know what kind of research plan I will fall into.</td>
<td><a href="#research-program">Research Program</a> / <a href="#eeg-consciousness-roadmap">EEG Consciousness Roadmap</a></td>
<td>You can check what you will actually accumulate as a research plan.</td>
</tr>
<tr>
<td>I want to know the limitations of this page first.</td>
<td><a href="#limitations">Limitations</a></td>
<td>You can separate and read the theoretical limits, engineering limits, and operational limits.</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>What can be said relatively strongly on this page</th>
<th>What this page still treats as a hypothesis</th>
</tr>
</thead>
<tbody>
<tr>
<td>None of the major theories is single-handedly definitive at this point.</td>
<td>It is unclear which combination of theories will ultimately be a sufficient condition for WBE.</td>
</tr>
<tr>
<td>EEG alone has fundamental limitations in inverse problems and spatial resolution.</td>
<td>The extent to which this limitation can be overcome by integrating other modalities is still a research topic.</td>
</tr>
<tr>
<td>Strong claims that exclude causal perturbations, retestability, and thermodynamic constraints are dangerous.</td>
<td>Which threshold is considered "sufficient" depends on future bench design.</td>
</tr>
</tbody>
</table>

<section class="section" id="design-principles">
<h2 class="section-title">Design Principles: Design as a migration, not a copy</h2>
<p>This section integrates the theoretical frames that were once separated in the old <code>idea.md</code> into the design principles of this research note. The goal is not to multiply philosophical positions, but to make it clear <strong>which assumptions should actually be built into the design conditions</strong> without separating them from the main text.</p>

<div class="key-points">
<h4>Design principles adopted</h4>
<ul>
<li><strong>Dynamic migration instead of static copy:</strong>The question is how to continue the process of not only storing information in the brain but also continuously updating it.</li>
<li><strong>Use theories as working hypotheses:</strong>IIT, FEP, and predictive coding are not truth declarations, but are treated as auxiliary lines to the requirements definition.</li>
<li><strong>Returning identity to design conditions:</strong>The copy problem does not stop at abstractions, but is broken down into continuity tests, intervention responses, causal conservation, and thermodynamic constraints.</li>
</ul>
</div>

<table class="data-table">
<thead>
<tr>
<th>What to fix first in the design</th>
<th>The position of this page</th>
<th>Things still unresolved</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>identity</strong></td>
<td>We place more emphasis on whether the process of updating is continuous, rather than whether the data is the same.</td>
<td>It is unclear which continuity measure should be considered a sufficient condition.</td>
</tr>
<tr>
<td><strong>How to use consciousness theory</strong></td>
<td>Rather than making IIT, GNWT, and FEP compete, we convert them into measurement/perturbation/integration indicators and use them.</td>
<td>There is still a lack of common specifications that can be stably used across theories.</td>
</tr>
<tr>
<td><strong>thermodynamics</strong></td>
<td>If a dynamic process is maintained, not only logical costs but also dissipation and non-equilibrium should be audited.</td>
<td>It remains an open question which thermodynamic KPIs are directly linked to the quality of identity and consciousness.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>In everyday language</strong>
<p>Saving a single photo is a different matter than transferring a video with the same movements. If Mind-Upload is to be treated as something closer to the latter than the former, what is needed is not only ``replication of structure'' but also ``continuous transition,'' ``response to intervention,'' and ``maintenance cost.''</p>
</div>

<div class="note-box">
<strong>Where this position falls into implementation</strong>
<p>Measurements will require BIDS, synchronization, QC, and perturbation logging, modeling will require ESI/DCM/SCM uncertainty management, and implementation will require closed-loop stability and thermodynamic constraints. Therefore, the correct way to use this clause is to read it not as an abstract declaration, but as an entry point for binding the requirements of subsequent clauses.</p>
</div>
</section>

<!-- Introduction -->
<section class="section" id="introduction">
<h2 class="section-title">Introduction: Theoretical Foundations Revisited</h2>

<h3>1.1. Science of consciousness: Reexamining the theoretical foundations and the impact of “Adversarial Collaboration”</h3>
<div class="note-box">
<strong>What I want to decide in this section</strong>
<p>The point of this section is not to declare a winning theory. Instead, when the major theories are placed side by side, the first question is <strong>which verification conditions are common across them</strong>.</p>
</div>
<p>What is the "consciousness" that mind upload (WBE) should reproduce? This project historically leaned toward a combined reading of Integrated Information Theory (IIT) and Global Neuronal Workspace Theory (GNWT). However, the pre-registered adversarial collaboration published in 2025 partially supported predictions from IIT, GNWT, and RPT while also falsifying some key predictions, so no single theory emerged as the winner.<sup><a href="#ref-54">[54]</a></sup> Candidate markers for conscious content were also separated from markers of report and task relevance, making it clear that confound control must be fixed before theory choice is elevated. Therefore, this site does not commit to a single theory. Instead, it translates theories into <strong>pre-registered prediction sets</strong> that must compete under no-report conditions, perturbation benchmarks, and external generalization tests. FEP / predictive coding remains one candidate route, not the default one.</p>

<table class="data-table">
<thead>
<tr>
<th>Theory</th>
<th>Main target of explanation</th>
<th>Main weakness / failure point</th>
<th>How to use with Mind-Upload</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT</strong></td>
<td>Seeks to explain the integrated quality and causal structure of consciousness.</td>
<td>The problem is the Unfolding Argument, which is computationally heavy and can be judged as unconscious even though it is functionally the same.</td>
<td>It is treated as a <strong>candidate measuring framework</strong> for the quality and integration of consciousness, but in implementation it is reduced to approximate indices such as PCI-family measures.</td>
</tr>
<tr>
<td><strong>GNWT</strong></td>
<td>Seeks to explain why conscious access emerges when information is shared widely.</td>
<td>It is difficult to separate prefrontal cortex ignition from reporting behavior, and its correspondence with consciousness itself tends to be unstable.</td>
<td>It is used as a <strong>working hypothesis</strong> for asking under what conditions wide-area sharing and reportability emerge.</td>
</tr>
<tr>
<td><strong>FEP/Predictive Coding</strong></td>
<td>Seeks to explain how a system can maintain stable inference while interacting with the environment.</td>
<td>It cannot fully explain phenomenal consciousness by itself, and because it is highly abstract, it is easy to appear as if it has explained everything.</td>
<td>It is treated as a <strong>candidate model family</strong> for describing closed loops, prediction errors, and adaptation, and must compete with DCM, SCM, and state-space models.</td>
</tr>
</tbody>
</table>

<div class="question-box">
<h4>Central issue: How to design prediction competition rather than theoretical preferences</h4>
<p>Nature 2025's adversarial test showed that signals related to conscious content are distributed in multiple occipital/temporal/frontal regions, and that some markers also track task relevance and report requirements.<sup><a href="#ref-54">[54]</a></sup>. Therefore, rather than deciding which theory to name, it is more scientific to first decide which predictions to make and under which conditions.</p>
<div class="resolution-box">
<h5>Direction of solution: Return theory to the ``prediction source'' rather than the ``winner''</h5>
<p>This site treats IIT, GNWT, RPT, and FEP as competing <strong>prediction generators</strong>. Acceptance depends on whether the resulting predictions pass no-report conditions, perturbation conditions, task-relevance control, and cross-dataset / cross-center generalization.</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 6px;"><strong>Theoretical layer:</strong>Each theory registers in advance which spatiotemporal patterns, which condition differences, and which failure conditions it predicts.</li>
<li style="margin-bottom: 6px;"><strong>Indicator layer:</strong> PCI / PCI-ST, complexity, and criticality are not theories themselves; they are benchmark candidates for operationalizing theoretical predictions.</li>
<li style="margin-bottom: 6px;"><strong>Design layer:</strong> A theory is not advanced unless it satisfies no-report conditions, artifact management, delay / jitter auditing, and external validation.</li>
</ul>
<p>In addition, the time requirements and counterfactual virtual equivalence of closed-loop systems are not determined using a single threshold or a single theory, but rather the latency budget and failure mode for each task are first disclosed, and then treated as a verification issue.<sup><a href="#ref-76">[76]</a></sup>.</p>
</div>
</div>

<h3>1.2. From theory to implementation: technical and philosophical challenges</h3>
<p><strong>Challenges of porting IIT to digital infrastructure:</strong> IIT 4.0<sup><a
href="#ref-17">[17]</a></sup> Applying it to WBE leaves the unresolved question of how its axiomatic system could be satisfied on a digital platform. In particular, the axiom of "intrinsic reality"<sup><a
href="#ref-44">[44]</a></sup> is unlikely to be satisfied in principle by a discrete computing system such as a standard von Neumann computer, which is one form of the Unfolding Argument. In this project, we therefore avoid calling digital emulation an "approximation" of IIT and instead specify a shift toward <strong>physical mapping of causal structure using neuromorphic hardware</strong>. Alternatively, following Albantakis et al. (2023),<sup><a href="#ref-17">[17]</a></sup> we also treat <strong>hybrid systems</strong> that combine biological neurons with digital elements as candidates for preserving causal power at the physical level rather than merely matching outputs computationally.</p>

<p><strong>Psychological continuity and copying problems:</strong>Derek Parfit's Psychological Continuity Theory<sup><a
href="#ref-4">[4]</a></sup>The basis of identity is continuity of memory and personality. This requires WBE to maintain a "dynamic process" rather than just a static data copy. In response to the ``copying problem (alter ego paradox)'' posed by this theory, we aim to translate thought experiments such as ``stepwise neural replacement'' and ``hybrid brain systems'' into verifiable engineering protocols.</p>
<p><strong>Turning to process philosophy:</strong>Whitehead's process philosophy is based on the perspective of viewing consciousness not as a static "thing" but as a "process" that is constantly updated through interaction with the environment.<sup><a
href="#ref-32">[32]</a></sup>, Friston's free energy principle<sup><a
href="#ref-14">[14]</a></sup>/active reasoning<sup><a
href="#ref-45">[45]</a></sup>It also resonates with me. This project focuses on the technical requirements (e.g. Slow
Continuous Mind Uploading)<sup><a href="#ref-59">[59]</a></sup>.</p>
<div class="note-box">
<strong>Promise as research</strong>
<p>Operate the following as "minimum guardrails": Attach sources such as primary/review articles to major claims; Distinguish between hypotheses, facts, and value judgments, and include uncertainty; Define evaluation indicators and procedures first, and prioritize reproducibility.</p>
</div>
</section>


<!-- Technical Framework -->
<section class="section" id="technical-framework">
<h2 class="section-title">Technical Framework</h2>

<p>The technological roadmap for realizing Mind Upload is organized into three stages: "Measurement," "Decoding," and "Implementation." It combines the classic WBE roadmap<sup><a
href="#ref-8">[8]</a></sup>, more recent whole-brain-architecture roadmaps<sup><a
href="#ref-7">[7]</a></sup>, and large-scale simulation plans such as Blue Brain<sup><a
href="#ref-16">[16]</a></sup>.</p>

<div class="note-box">
<strong>2026-03 Reasons for changing the writing style of this section in the literature audit</strong>
<p>Earlier versions gave similar weight to elements with very different roles, such as Block-Champagne, Active Inference, PCI, TDA, and thermodynamic logs. When we compare direct EEG source-imaging validation studies, TMS-EEG recommendations, and theoretical papers, the common core is much narrower: <strong>transparent reporting</strong>, <strong>disclosure of forward models and electrode geometry</strong>, <strong>validation against external criteria</strong>, and <strong>OOD / perturbation / abstention design</strong>. Specific solvers, theories, and thermodynamic indicators are better treated as conditional or exploratory tracks.<sup><a href="#ref-78">[78]</a></sup><sup><a href="#ref-79">[79]</a></sup><sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>.</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>issue</th>
<th>Points that were weak before correction</th>
<th>Reasonable arrangement as of 2026-03</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG source imaging</strong></td>
<td>The name of the algorithm was too prominent.</td>
<td>The core requirements are external validation, uncertainty reporting, and conductivity sensitivity analysis; Block-Champagne and related methods are promising candidates, not the standard by themselves.<sup><a href="#ref-78">[78]</a></sup><sup><a href="#ref-79">[79]</a></sup><sup><a href="#ref-101">[101]</a></sup>.</td>
</tr>
<tr>
<td><strong>Perturbation / PCI</strong></td>
<td>I was writing PCI close to the ground truth.</td>
<td>PCI / PCI-ST is a strong external benchmark candidate, but it is not a universal KPI because TMS-EEG requires strict stimulus control and artifact management.<sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>.</td>
</tr>
<tr>
<td><strong>Active Inference / Counterfactual Equivalence</strong></td>
<td>It was written in a way that read like a verified central indicator.</td>
<td>At present, we use it as a theory-driven source of hypotheses and model families, then narrow it through OOD generalization, intervention, and model competition.<sup><a href="#ref-76">[76]</a></sup><sup><a href="#ref-80">[80]</a></sup>.</td>
</tr>
<tr>
<td><strong>Criticality / TDA / Irreversibility</strong></td>
<td>It was previously treated too much like a core indicator.</td>
<td>Complexity and criticality are promising, but for now they remain auxiliary analyses while primary judgments rely on indicator bundles that are easier to audit.<sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-56">[56]</a></sup><sup><a href="#ref-92">[92]</a></sup>.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>The most reinforced points this time</strong>
<p>The weakness of this central page was that atlas data, patch-seq, EM connectomics, same-brain function, and neuromodulator / glia imaging could all be collapsed into the single phrase "advanced by multimodal." The primary literature makes clear that each stack observes different variables directly, so each stack also has a different upper limit on what can be claimed. If we blur those differences, <strong>advancing a structural scaffold</strong>, <strong>strengthening a cell-type prior</strong>, <strong>improving local conditional prediction</strong>, and <strong>calibrating slow-state proxies</strong> all start to look like the same kind of progress when they are not.</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>measurement stack</th>
<th>what is directly observed</th>
<th>a stronger argument</th>
<th>What remains latent</th>
<th>ceiling on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG / fMRI / fNIRS</strong></td>
<td>These are macro current fields, hemodynamic proxies, and wide-area state transitions.</td>
<td>Global state tracking, timing constraints, relatively coarse network occupancy, and for hemodynamic stacks the need for vascular transfer / CVR calibration can be audited.</td>
<td>Cell type, current synaptic efficacy, vascular transfer state, neuromodulatory field, and glial/metabolic state are not directly determined.</td>
<td><strong>Macro-state tracking, hemodynamic-limited inference, and weak L2</strong>. It is not listed as state-complete reconstruction.</td>
</tr>
<tr>
<td><strong>whole-brain spatial atlas</strong></td>
<td><a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">Yao et al. (2023)</a> substantially expanded cell-type taxonomy and spatial organization.</td>
<td>Molecular identity and spatial prior can be greatly enhanced.</td>
<td>The destinations to return to after threshold/gain, current state, sleep-history, and perturbation remain.</td>
<td><strong>Up to cell-type and spatial priors</strong>. It is not presented as dynamic completeness.</td>
</tr>
<tr>
<td><strong>Patch-seq / morpho-electric bridge</strong></td>
<td><a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> and <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">Gamlin et al. (2025)</a> provide bridges between transcriptomes, morphology, electrophysiology, and local wiring.</td>
<td>The mapping from cell-type labels to morpho-electric phenotypes and local motifs can be enhanced.</td>
<td>Whole-brain coverage, same-brain network context, and longitudinal maintenance-state remain.</td>
<td><strong>Local parameter prior and bridge</strong>. It is not used as evidence of whole-brain state completeness.</td>
</tr>
<tr>
<td><strong>volume EM / same-brain connectomics</strong></td>
<td><a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> strengthen the structural scaffold, while <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> strengthen same-brain structure-function links.</td>
<td>Local digital twins, conditional response predictions, and cell-type dependent wiring rules can be further enhanced.</td>
<td>The current synaptic weight, all-state generalization, whole-brain coverage, and homeostatic controller remain.</td>
<td><strong>Structural scaffold and local functional twin</strong>. It cannot be placed on the same level as human whole-brain WBE.</td>
</tr>
<tr>
<td><strong>neuromodulator / glia imaging</strong></td>
<td><a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> provide transmitter-linked covariates, and <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> strengthen astrocyte-network state readouts.</td>
<td>Calibration of arousal proxies, modeling of slow-states, and prohibition of glia omissions can be strengthened.</td>
<td>The sufficiency of the whole-brain transmitter field, receptor state, and cross-day maintenance-state remains.</td>
<td><strong>Up to proxy calibration and slow-state constraints</strong>. It is not presented as whole-brain ground truth for internal state.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Modification rules resulting from this table</strong>
<p>From this point onward, this page treats <strong>atlas</strong>, <strong>bridge</strong>, <strong>scaffold</strong>, <strong>local functional twin</strong>, and <strong>proxy calibration</strong> as separate categories. In other words, we do not allow readings such as "state-complete because it is multimodal," "whole-brain because it is same-brain," or "long-term maintenance is sufficient because there is local causal evidence." Any claim must be issued together with its measurement stack, direct observables, remaining latent state, and abstention conditions.</p>
</div>

<div class="note-box">
<strong>2026-03-18 correction: human evidence is layered, not one progress bar</strong>
<p>One weakness of the earlier version of this page was that it could make very different human evidence classes look like one kind of advance. The current literature does not support that reading. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a>, <a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">Finnema et al. (2016)</a>, <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a>, <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a>, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a>, <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a>, and <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a> reduce different error terms rather than one common "state completeness" score.</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Human route</th>
<th>What it actually advances</th>
<th>What it still does not fix</th>
<th>Safe reading on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Local human nanoscale ultrastructure</strong><br><a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a></td>
<td>Fixed-tissue local organization of human neurons, glia, axons, and synapses at nanoscale resolution.</td>
<td>Living whole-brain dynamics, current synaptic efficacy, maintenance-state, and cross-brain generalization.</td>
<td><strong>Local structural scaffold</strong>, not living human state completeness.</td>
</tr>
<tr>
<td><strong>Regional synaptic-density PET</strong><br><a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">Finnema et al. (2016)</a>; <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>; <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a></td>
<td>Regional in vivo proxy for synaptic density and its spatial distribution.</td>
<td>Release probability, tagged-spine history, receptor mobility, and branch-local stabilization routes.</td>
<td><strong>Regional synaptic-density proxy</strong>, not direct ground truth of current synaptic state.</td>
</tr>
<tr>
<td><strong>Parcel-level biochemical / energetic organization</strong><br><a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a>; <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a>; <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a></td>
<td>Macro biochemical organization, ATP-related metabolism, and whole-brain energetic turnover patterns.</td>
<td>Branch-local ATP reserve, mitochondrial positioning, local proteostasis, and cell-specific energetic fragility.</td>
<td><strong>Macro biochemical / energetic proxy</strong>, not branch-local neuronal energetic state.</td>
</tr>
<tr>
<td><strong>Macro support-state proxies</strong><br><a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a>; <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a>; <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a></td>
<td>In vivo macro maps for myelin bilayer, tissue sodium, and whole-brain thermal rhythms.</td>
<td>Cell-specific chloride set point, microtemperature gradients, adaptive conduction timing, and local inhibitory reversal potential.</td>
<td><strong>Macro support-state proxy</strong>, not cell-specific timing or ionic ground truth.</td>
</tr>
<tr>
<td><strong>Hemodynamic transfer audit</strong><br><a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a>; <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a>; <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a></td>
<td>Calibration of baseline vascular state, cerebrovascular reactivity, and interpretation limits for BOLD / HbO / HbR differences.</td>
<td>A clean neural difference unless the vascular transfer side has also been audited.</td>
<td><strong>Hemodynamic-limited evidence</strong> unless vascular transfer / CVR is explicitly calibrated.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>What this correction changes in practice</strong>
<p>The point is not that these routes are weak. The point is that each route lowers a <strong>different</strong> latent-state error term. On this page, "human evidence advanced" now means "a specific layer advanced under a specific ceiling," not "the human whole-brain state became nearly observable."</p>
</div>

<div class="stage-list">
<div class="stage-item" id="proposal-46">
<div class="stage-number"></div>
<div class="stage-body">
<h4>1. Sensing: Precise reading of brain activity and quantification of uncertainty</h4>
<p>Electroencephalography (EEG) offers high temporal resolution and is therefore a powerful input signal for WBE, but its low spatial resolution remains a fundamental limitation. EEG source imaging (ESI) is a computational response to that problem, yet it remains an <strong>ill-posed problem</strong><sup><a href="#ref-5">[5]</a></sup> and therefore does not yield a unique solution. For engineering goals that demand very high reliability, such as WBE, relying only on traditional minimum-norm methods or point estimates such as dSPM risks propagating estimation error throughout the system.</p>
<p>What matters here is not the <strong>solver name</strong> but the <strong>evidence chain</strong>. Empirical Bayesian methods,<sup><a href="#ref-78">[78]</a></sup> high-density EEG, and individualized MRI are all promising ways to improve estimation conditions, but no method should be called a standard unless it is paired with EEG-BIDS-aligned reporting,<sup><a href="#ref-26">[26]</a></sup> disclosure of electrode coordinates and forward models, sensitivity analysis for conductivity uncertainty,<sup><a href="#ref-79">[79]</a></sup> and external validation.</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>Positioning of high-density EEG and Bayesian estimation:</strong> The Block-Champagne framework,<sup><a href="#ref-78">[78]</a></sup> FEM / BEM forward models, high-density EEG, and individualized MRI are important for improving estimation conditions. However, greater sensor density does not guarantee source uniqueness, because skull-induced spatial smoothing and inverse-problem non-uniqueness still remain.<sup><a href="#ref-101">[101]</a></sup> In this project, they are treated not as a <strong>guarantee</strong> but as <strong>preconditions for narrowing error sources</strong>.</li>
<li style="margin-bottom: 8px;">
<strong>Visualization and external validation of uncertainty:</strong>The estimated brain activity map includes not only amplitude but also<strong>"Credible Intervals"</strong>Alternatively, indicate the concentration of the posterior distribution to clearly indicate areas of high uncertainty. Furthermore, we cannot call something ``improved'' unless we report how much the error has been reduced under which conditions relative to external standards such as simulations, phantoms, simultaneous invasive recordings, and intracranial stimulation.</li>
<li style="margin-bottom: 8px;">
<strong>Uncertainty and error propagation for forward problems:</strong>Errors in the conductivity and shape of head tissues (especially the skull) directly affect localization errors.<sup><a href="#ref-79">[79]</a></sup>, include at least a sensitivity analysis or range assessment in your submission. Although full probabilistic modeling is powerful, it is not universally required as of 2026-03, and we will prioritize allowing a third party to audit the error range.</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">External Validation</span>
<span class="tag">Forward Model Audit</span>
<span class="tag">Sensitivity Analysis</span>
<span class="tag">Uncertainty Quantification</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>2. Decoding: Introducing active inference and counterfactual virtual equivalence</h4>
<p>In the "Decoding" section, traditional decoding techniques such as Mind Captioning are still mappings based on correlation. To make a claim that approaches WBE, it is not enough to imitate inputs and outputs; the system must also expose unlearning conditions, intervention conditions, failure conditions, and <strong>generative predictive performance</strong>. What matters here is not fixing a single theory as the correct answer, but arranging multiple generative models so that they can be compared.</p>
<p>Laukkonen et al.'s discussion of <strong>"counterfactual equivalence"</strong><sup><a href="#ref-76">[76]</a></sup> together with active-inference-oriented discussions<sup><a href="#ref-80">[80]</a></sup> is useful for deciding what should be tested. However, as of 2026-03, it is still not a shared acceptance standard by itself. On this page it is treated as a <strong>design hypothesis</strong> that must be evaluated together with OOD generalization, perturbation response, calibration, abstention, and alternative-model reporting.</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>Position of Active Inference:</strong> It is a powerful way to view the brain as a generative model that interacts with the environment rather than as a passive decoder.<sup><a href="#ref-80">[80]</a></sup> In this project, however, it is not the only implementation principle; together with DCM, state-space models, and SCM, it is treated as a candidate in <strong>model competition</strong>.</li>
<li style="margin-bottom: 8px;">
<strong>Extension of the Turing test (causal perturbation protocol):</strong> Because static counterfactuals cannot be tested by observation alone, we use a "Causal Perturbation Protocol" that extends the Turing Test. The biological brain's response to physical perturbations such as TMS is compared with the response distribution to virtual perturbations in emulation, and PCI is treated as <strong>one external benchmark</strong>, not as ground truth itself.<sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>.
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Model Competition</span>
<span class="tag">OOD Generalization</span>
<span class="tag">Perturbation</span>
<span class="tag">Causal Structure</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>3. Implementation: Consideration of computational limitations of IIT 4.0 and alternative indicators</h4>
<p>This project has traditionally relied on integrated information theory (IIT 4.0), but its biggest implementation problems are the <strong>explosion of computational cost (NP-hard)</strong> and the ambiguity of "intrinsic reality" in digital infrastructures. Rather than treating IIT dogmatically, we use the <strong>Adversarial Collaboration</strong> results<sup><a href="#ref-54">[54]</a></sup> to separate <strong>main judgments</strong> from <strong>auxiliary analyses</strong> in the implementation stack.</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>Position of computable approximate indicators:</strong> Direct calculation of Phi (integrated information) scales exponentially with system size. Approximation methods using PCI-ST and low-dimensional embeddings<sup><a href="#ref-81">[81]</a></sup> are therefore treated as <strong>engineering proxies</strong>, not as direct substitutes for consciousness or identity.</li>
<li style="margin-bottom: 8px;">
<strong>Geometric comparison of neural activity manifolds (Neural Manifold Geometry):</strong> To capture structural differences that scalar values such as PCI cannot show, graph indicators, TDA, and persistent homology are introduced as <strong>auxiliary analyses</strong>. Interpretation consistency and noise robustness are still not standardized well enough for primary pass/fail decisions, so those decisions remain tied to simpler and more auditable metrics.</li>
<li style="margin-bottom: 8px;">
<strong>Introducing thermodynamic constraints:</strong> We keep the idea of auditing computational cost and physical cost separately, but irreversibility and entropy production are currently only <strong>exploratory auxiliary logs</strong>. Quantities extracted from coarse-grained neural data should not be equated directly with microscopic dissipation or with necessary conditions for consciousness.<sup><a href="#ref-92">[92]</a></sup>.
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">IIT 4.0 Limits</span>
<span class="tag">Evidence Tiers</span>
<span class="tag">Exploratory Metrics</span>
<span class="tag">Resource Audits</span>
</div>
</div>
</div>
</div>
</section>

<!-- Decoding vs Emulation -->
<section class="section" id="decoding-to-emulation-gap">
<h2 class="section-title">From decoding to emulation: Explanation of logical gaps and verification design</h2>

<div class="note-box">
<strong>TL;DR</strong>
<p>Decoding that “reads” sentences from brain activity is powerful, but it is basically a <strong>translation of observed outputs</strong>, whereas WBE requires the <strong>generation of brain dynamics through an autonomous causal model</strong>.<sup><a
href="#ref-8">[8]</a></sup> To close that gap, the generative model must be explicit about inputs, internal state, and outputs, and it must be validated with predictions about interventions and perturbations.<sup><a
href="#ref-13">[13]</a></sup><sup><a href="#ref-45">[45]</a></sup>.</p>
</div>

<h3>Contents of the gap (paraphrase that even high school students can understand)</h3>
<p>For example, even if you read the "test answers",<strong>what the person usually thinks</strong>(How to respond to new problems) cannot necessarily be reproduced. Similarly, although brain-to-text can express ``brain activity at this moment,'' it does not guarantee the ``process of continuously updating the state while interacting with the environment'' required by WBE.</p>

<div class="visual-diagram diagram-decoding-gap">
  <div class="diagram-side decoding">
    <div class="diagram-icon">🧠</div>
    <div class="arrow-box">Decoding<br><span style="font-size:10px; font-weight:400; opacity:0.8;">(Translation)</span></div>
    <div class="diagram-icon">📝</div>
    <p class="diagram-caption">Output: Text/Media<br>(Static)</p>
  </div>
  <div class="diagram-divider">VS</div>
  <div class="diagram-side emulation">
    <div class="diagram-icon">🧠</div>
    <div class="arrow-box active">Emulation<br><span style="font-size:10px; font-weight:400; opacity:0.8;">(Causal Model)</span></div>
    <div class="diagram-icon">⚙️</div>
    <p class="diagram-caption">Output: Dynamics<br>(Process)</p>
  </div>
</div>

<h3>Points that are academically problematic (what should be additionally shown)</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>Difference between decode and emulate:</strong>Mind Captioning<sup><a
href="#ref-11">[11]</a></sup>and continuous language recovery<sup><a href="#ref-30">[30]</a></sup>showed that meaning and sentences can be reconstructed from brain signals. However, WBE requires the reproduction of the causal process itself: how internal states transition and how future outputs (actions, thoughts, self-models) are generated when the same input (sensation) is given.<sup><a
href="#ref-8">[8]</a></sup>.
</li>
<li style="margin-bottom: 8px;">
<strong>Problems where the language-prior distribution (LLM) wins:</strong> Because LLMs are fluent, weak evidence can still produce plausible-looking sentences, i.e. hallucinated outputs.<sup><a
href="#ref-28">[28]</a></sup> Therefore, it is necessary to baseline how much brain-signal information actually contributes to the output by using counterfactual inputs such as shuffles, and to define abstention conditions up front.</li>
<li style="margin-bottom: 8px;">
<strong>Many-to-one (different models explaining the same observation) problem:</strong>Just as EEG source estimation is an ill-posed problem,<sup><a
href="#ref-5">[5]</a></sup>, there can be multiple explanations that fit the observed data. Definitional non-uniqueness is also discussed in IIT.<sup><a
href="#ref-3">[3]</a></sup>. For WBE, <strong>intervention prediction, not observational agreement alone</strong>, is what narrows the model family.</li>
<li style="margin-bottom: 8px;">
<strong>Verification of preservation of consciousness and identity:</strong>The position that views identity in terms of psychological continuity includes the copying problem (multiplicity).<sup><a
href="#ref-4">[4]</a></sup><sup><a href="#ref-58">[58]</a></sup>. Even if one adopts the Slow Continuous Mind Uploading hypothesis<sup><a
href="#ref-59">[59]</a></sup>, it is still necessary to audit whether "conscious capacity" is preserved using behaviorally independent indicators such as the PCI family.<sup><a
href="#ref-47">[47]</a></sup>.
</li>
</ul>

<h3>Demonstration plan to fill the gap (minimum)</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Make the generative model explicit:</strong>Using DCM etc., clarify what is a state and what is a parameter, and present it in a form that allows model comparison.<sup><a
href="#ref-13">[13]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Preregister intervention (perturbation) predictions:</strong>Incorporate the propagation and complexity of reactions to perturbations into the evaluation axis, like PCI/PCI-ST<sup><a
href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Require a counterfactual baseline:</strong>Quantify the output produced by linguistic prior distribution alone by input shuffling, trial replacement, model temperature fixation, etc., and report it as an effect size.<sup><a
href="#ref-28">[28]</a></sup>.</li>
</ol>

<h3>Verification boundaries for causal structure, state completeness, and physical constraints (updated in 2026-03 audit)</h3>
<p>In translating the demonstration plan into implementation terms, the most important correction was to stop treating different limitations as a single kind of "difficulty." In the primary literature, at least <strong>observability</strong>, <strong>identifiability</strong>, <strong>maintenance-state</strong>, <strong>intervention</strong>, and <strong>thermodynamic readout</strong> are separate barriers, and progress on any one of them cannot substitute for all the others.</p>

<table class="data-table">
<thead>
<tr>
<th>wall</th>
<th>What the primary literature now supports</th>
<th>Don't support it yet</th>
<th>Correction policy on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Wall of Observability</strong></td>
<td><a href="https://doi.org/10.1038/s41586-024-07558-y">Dorkenwald et al. (2024)</a> and <a href="https://doi.org/10.1038/s41586-025-08790-w">MICrONS Consortium et al. (2025)</a> significantly advanced the correspondence between local connectomics and same-brain function. On the scalp EEG side, forward-model and head-conductivity sensitivity analysis can also be audited.<sup><a href="#ref-5">[5]</a></sup><sup><a href="#ref-79">[79]</a></sup>.</td>
<td>Still, we cannot say that we have been able to directly observe the human whole-brain in a state-complete manner. Improvements in local digital twin and source imaging cannot be translated directly into observability of the whole brain and all states.</td>
<td>Instead of writing local connectomics, non-invasive ESI, and whole-brain WBE in the same breath, we first clarify the claim ceiling for each measurement stack.</td>
</tr>
<tr>
<td><strong>Wall of identity</strong></td>
<td>The EEG inverse problem can be improved considerably if the head model, conductivity assumptions, and model space comparisons are carefully handled.<sup><a href="#ref-5">[5]</a></sup><sup><a href="#ref-79">[79]</a></sup>. On the DCM side, Regression DCM and Causal Fingerprinting also advance candidate model family comparison and test-retest auditing.<sup><a href="#ref-96">[96]</a></sup>.</td>
<td>However, improved predictability or localization does not guarantee general uniqueness recovery. As long as there are other model families or equivalence classes that fit the observed data, ``good accuracy'' cannot be written as ``the internal state was uniquely known.''</td>
<td>This page prioritizes evidence chain over solver name and requires family comparison, sensitivity analysis, and abstention conditions.</td>
</tr>
<tr>
<td><strong>Maintenance-state wall</strong></td>
<td><a href="https://doi.org/10.1016/j.cell.2016.01.046">Hengen et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuron.2021.04.004">Torrado Pacheco et al. (2021)</a>, and <a href="https://doi.org/10.1038/s41467-024-47838-5">Xu et al. (2024)</a> support homeostatic recovery that depends on sleep / wake dynamics. <a href="https://doi.org/10.1038/s41593-023-01558-3">Looser et al. (2024)</a> highlights oligodendrocyte-axon metabolic coupling, while <a href="https://doi.org/10.1038/s41586-024-07311-5">Cahill et al. (2024)</a> and <a href="https://doi.org/10.1073/pnas.2211572119">Lee et al. (2022)</a> strengthen the case for glial and active maintenance.</td>
<td>From same-day decode performance and short-term activity matches to cross-day stability, overnight recovery, and timing-sensitive maintenance, they cannot be considered the same.</td>
<td>State-completeness gates include sleep history, myelin/delay, and glial/metabolic support, and cross-day claims require maintenance-state longitudinal logs.</td>
</tr>
<tr>
<td><strong>Intervention wall</strong></td>
<td><a href="https://doi.org/10.1016/j.brs.2023.02.009">Hernandez-Pavon et al. (2023)</a> for organized TMS-EEG, <a href="https://doi.org/10.1126/science.abd0380">Flesher et al. (2021)</a> for bidirectional BCI, and <a href="https://doi.org/10.1038/s41591-024-03196-z">Oehrn et al. (2024)</a> for adaptive DBS together provide strong causal evidence in local subsystems and disease settings.</td>
<td>Still, the success of locally closed loops does not directly support whole-brain branch-equivalence or identity preservation. If you remove the stimulus site, intensity, latency/jitter, and artifact windows, the comparison itself collapses.</td>
<td>Treat intervention evidence as staged evidence, and write separately for passive observation, held-out perturbation, online loop, and long-term adaptive operation.</td>
</tr>
<tr>
<td><strong>Thermodynamic readout wall</strong></td>
<td><a href="https://doi.org/10.1073/pnas.2109889118">Lynn et al. (2021)</a> and <a href="https://doi.org/10.1093/cercor/bhac177">de la Fuente et al. (2022)</a> showed that time-irreversibility signatures appear in coarse-grained neural dynamics.</td>
<td>However, what is measured here is a lower bound on information-entropy production derived from coarse-grained neural data, not microscopic physical dissipation itself. <a href="https://doi.org/10.1038/s41467-025-66669-w">Ishihara &amp; Shimazaki (2025)</a> also show that stable measurement of the arrow of time from spiking remains difficult.</td>
<td>EPR/irreversibility is lowered to the auxiliary log, and the main judgment is made with a bundle of OOD, perturbation, external validation, and abstention conditions.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Replacements prohibited in this section</strong>
<p>Interpretations such as ``the human whole-brain state was achieved because of advances in local connectomics'', ``the internal state could be uniquely restored because the ESI was improved'', ``the identity of the person could be verified because the closed loop was activated'', and ``physical identity was guaranteed because of irreversibility'' are not supported by the current primary literature.</p>
</div>

<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 12px;"><strong>DCM and causal indicators are used with family-comparison assumptions:</strong> DCM, Effective Information, Causal Density, and Symbolic Transfer Entropy (STE)<sup><a href="#ref-99">[99]</a></sup> are useful as additional analyses, but they should not be used as stand-alone universal pass/fail criteria. Key judgments still require reporting equivalence classes and test-retest reliability.</li>
<li style="margin-bottom: 12px;"><strong>Fix the minimal evidence chain:</strong>For L2 and higher claims, the lowest line is (a) pre-registered hold-out/OOD conditions, (b) validation with perturbations or external criteria, (c) uncertainty and abstention conditions, (d) reporting of alternative models or equivalence classes, (e) maintenance-state logs including cross-days, and (f) separation of computational cost and hardware power.</li>
</ol>

</section>

<!-- Reproducibility -->
<section class="section" id="reproducibility">
<h2 class="section-title">Substance and Reproducibility of the project</h2>
<p>As the name "Mind-Upload" suggests, this research depends heavily on computational methods. However, the current GitHub repository is still centered on the website and does not yet present enough substance or reproducibility as a research project <strong>in a form that a third party can execute</strong>. To address that gap, this project adopts BIDS and EEG-BIDS extensions as data-organization conventions,<sup><a
href="#ref-25">[25]</a></sup><sup><a href="#ref-26">[26]</a></sup> and is gradually building an analysis pipeline, data schema, and experimental-condition log that can support the site's claims in executable form.</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>Data processing pipeline:</strong> Publish minimum executable processing scripts aligned with BIDS / EEG-BIDS<sup><a href="#ref-25">[25]</a></sup><sup><a
href="#ref-26">[26]</a></sup>, using Python / MNE-Python and wrappers for SPM, FieldTrip, and related tools.</li>
<li style="margin-bottom: 8px;"><strong>Decoding model:</strong>Mind
Captioning-like Transformer model definitions and training / inference code using dummy data will be published.</li>
<li style="margin-bottom: 8px;">
<strong>Expanding data schema:</strong> In addition to `dataset_description.json`, publish example `eeg.json` schemas that document EEG structure and measurement protocols, so the project moves from merely formal BIDS compliance toward substantive compliance.</li>
</ul>
</section>

<!-- Current Status -->
<section class="section" id="key-technical-challenges">
<h2 class="section-title">Key Technical Challenges</h2>

<h3>Gap between connectome and dynamics</h3>
<p>Research on the structural connectome has advanced substantially in 2024-2025. <a href="https://doi.org/10.1038/s41586-024-07558-y">Dorkenwald et al. (2024)</a> mapped the wiring diagram of an adult Drosophila whole brain, while <a href="https://doi.org/10.1038/s41586-025-08790-w">MICrONS Consortium et al. (2025)</a> proposed a local functional digital twin that combines functional measurements with connectomics from the same individual. What follows directly from these results is that the wiring diagram is a strong scaffold, not that wiring alone determines the full state.</p>
<p>Likewise, <a href="https://doi.org/10.1038/s41586-023-06812-z">Yao et al. (2023)</a> strengthened whole-brain spatial atlases for cell identity and spatial priors, <a href="https://doi.org/10.1038/s41586-020-2907-3">Gouwens et al. (2021)</a> and <a href="https://doi.org/10.1038/s41586-025-08805-6">Gamlin et al. (2025)</a> strengthened the bridge from transcriptomes to morpho-electric phenotypes and local motifs, and <a href="https://doi.org/10.1126/science.adk4858">Shapson-Coe et al. (2024)</a>, <a href="https://doi.org/10.1126/scitranslmed.aaf6667">Finnema et al. (2016)</a>, <a href="https://doi.org/10.1038/s41467-025-66124-w">Lucchetti et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-024-07311-5">Cahill et al. (2024)</a> strengthened different human evidence classes. Importantly, these solve <strong>different kinds of deficits</strong>; improvement in one stack cannot be treated as if it meant "we now see everything."</p>
<p>Even if one already grants current synaptic efficacy as a separate missing variable, current public evidence still leaves at least ten additional hidden-state families. <a href="https://doi.org/10.1038/s41586-020-2907-3">Gouwens et al. (2021)</a> and <a href="https://doi.org/10.1016/j.cell.2016.01.046">Hengen et al. (2016)</a> show that intrinsic excitability and firing-rate set points are not fixed by graph plus cell-type label alone. <a href="https://doi.org/10.1038/s42003-025-08459-0">Thomas et al. (2025)</a> and <a href="https://doi.org/10.1080/15548627.2020.1775393">Pandey et al. (2021)</a> show that late stabilization depends on local synaptic tagging and proteostasis. <a href="https://doi.org/10.1038/s41467-021-23520-2">Schreiner et al. (2021)</a>, <a href="https://doi.org/10.1038/s41467-024-49572-8">Schreiner et al. (2024)</a>, and <a href="https://doi.org/10.1016/j.neuron.2025.03.020">Deng et al. (2025)</a> show that replay-coupling and specific sleep windows matter for consolidation. <a href="https://doi.org/10.1038/s41593-023-01558-3">Looser et al. (2024)</a> shows that timing support remains partly myelin-dependent, <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x">Hardingham &amp; Larkman (1998)</a> and <a href="https://doi.org/10.1038/nature07448">Long &amp; Fee (2008)</a> show that local thermal-state can alter kinetics without rewiring, <a href="https://doi.org/10.1126/science.1072699">Pizzorusso et al. (2002)</a> and <a href="https://doi.org/10.1126/science.1174146">Gogolla et al. (2009)</a> show that ECM / PNN state changes plasticity gates, <a href="https://doi.org/10.1126/science.1245423">Glykys et al. (2014)</a> and <a href="https://doi.org/10.1126/science.aad4821">Ding et al. (2016)</a> show that ionic milieu / chloride homeostasis changes inhibitory polarity and state transitions, <a href="https://doi.org/10.1016/j.cell.2018.12.013">Rangaraju et al. (2019)</a> and <a href="https://doi.org/10.1038/s41467-023-44233-8">Bapat et al. (2024)</a> show that branch-local mitochondrial support remains consequential, and <a href="https://doi.org/10.1038/s41586-024-07311-5">Cahill et al. (2024)</a> together with <a href="https://doi.org/10.1073/pnas.2211572119">Lee et al. (2022)</a> show that glial / metabolic support remains part of active maintenance.</p>

<table class="data-table">
<thead>
<tr>
<th>Hidden-state class</th>
<th>Why connectome + cell type still leaves it open</th>
<th>Safe reading on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Intrinsic excitability / homeostatic set point</strong></td>
<td>Threshold, gain, and post-perturbation return point can differ within the same transcriptomic label.</td>
<td>Do not read short-term activity matching as proof of long-horizon dynamical equivalence.</td>
</tr>
<tr>
<td><strong>Activity-dependent transcription / chromatin state</strong></td>
<td>Allocation eligibility and late stabilization programs can differ over hours to weeks on the same graph.</td>
<td>Do not read atlas completeness as if current memory-allocation state were already fixed.</td>
</tr>
<tr>
<td><strong>Local proteostasis / synaptic-tagging state</strong></td>
<td>Tagged spines and branches can differ in PRP capture, translation, degradation, and autophagy balance even when current weights look similar.</td>
<td>Do not treat a weight snapshot as the late-stabilization route.</td>
</tr>
<tr>
<td><strong>Sleep architecture / replay-coupling state</strong></td>
<td>Slow-oscillation / spindle / ripple coordination and consolidation-permissive NREM windows are not fixed by the daytime graph.</td>
<td>Do not treat sleep duration or same-day recovery as proof of replay-equivalent maintenance.</td>
</tr>
<tr>
<td><strong>Delay / myelin state</strong></td>
<td>Conduction timing and axonal support remain plastic and can shift synchrony even without rewiring.</td>
<td>Timing-sensitive claims need more than a structural graph plus one scalar delay constant.</td>
</tr>
<tr>
<td><strong>Thermal-state</strong></td>
<td>Local temperature still shifts membrane kinetics, spike generation, and field-potential amplitude on the same graph.</td>
<td>Macro thermometry is not proof that local timing-state matched.</td>
</tr>
<tr>
<td><strong>Perisynaptic ECM / PNN state</strong></td>
<td>Plasticity gate, receptor mobility, and memory-update resistance still vary without changing the synapse list.</td>
<td>Do not treat synapse counts or static weights as sufficient for adult plasticity claims.</td>
</tr>
<tr>
<td><strong>Ionic milieu / chloride homeostasis</strong></td>
<td>Local chloride set point and extracellular ion composition can change inhibitory sign and state-transition logic.</td>
<td>Do not treat connectome plus nominal weights as sufficient for inhibitory polarity or rhythm claims.</td>
</tr>
<tr>
<td><strong>Bioenergetic / mitochondrial state</strong></td>
<td>Branch-local ATP reserve, mitochondrial positioning, and fission/fusion still change repeated-burst reliability and dendritic plasticity.</td>
<td>Macro energetic proxies are not ground truth for branch-local energetic state.</td>
</tr>
<tr>
<td><strong>Glial / metabolic support</strong></td>
<td>Astrocyte network state, lactate support, and memory maintenance under turnover remain active variables.</td>
<td>Do not reinterpret persistence as static storage; active maintenance remains visible in the evidence.</td>
</tr>
</tbody>
</table>

<p>Brain emulation therefore requires more than reproducing neuronal connectivity. Current connectomics, atlas work, and human proxy layers are all valuable, but they push different parts of the problem. On this page the correction rule is simple: each claim must state <strong>which hidden-state families were directly measured</strong>, <strong>which were only constrained by priors or proxies</strong>, and <strong>which remained latent and forced abstention</strong>. Bridging the gap between static structure and dynamic state still requires transcriptomic connectomics<sup><a href="#ref-33">[33]</a></sup> plus stepwise verification through state-completeness gates.</p>

<!-- Figure: Connectome Progress -->
<div class="figure-box">
<div class="figure-content">
<div class="timeline-visual">
<div class="timeline-item">
<div class="timeline-dot done"></div>
<div class="timeline-label">nematode<br><strong>302</strong> neurons</div>
</div>
<div class="timeline-item">
<div class="timeline-dot done"></div>
<div class="timeline-label">Drosophila (FlyWire whole brain)<br><strong>~139,000</strong> neurons<br><span style="font-size:10px; opacity:0.7;">Dorkenwald et al., Nature 2024</span></div>
</div>
<div class="timeline-item">
<div class="timeline-dot current"></div>
<div class="timeline-label">mouse<br><strong>~71M</strong> neurons</div>
</div>
<div class="timeline-item">
<div class="timeline-dot"></div>
<div class="timeline-label">human<br><strong>~86B</strong> neurons</div>
</div>
</div>
</div>
<p class="figure-label">Figure 1</p>
<p class="figure-caption">Progress and scale of connectome research. Nematodes (<em>C.
elegans</em>), the connectome of the entire nervous system is being developed.<sup><a href="#ref-20">[20]</a></sup>In Drosophila, the adult whole brain connectome (approximately 139,000 neurons) was completed in 2024 by the FlyWire project (Dorkenwald et al., 2024).<sup><a
href="#ref-21">[21]</a></sup>. However, identification of functional dynamics (state-dependent changes in connectivity) and dynamics involving synaptic strength, neuronal modification, and glia remains a challenge. Although saturated reconstructions have been achieved in small cortical volumes in mice,<sup><a
href="#ref-22">[22]</a></sup>, whole-brain-scale reconstruction is currently in progress. The human brain has approximately 86 billion neurons<sup><a
href="#ref-57">[57]</a></sup>.
</p>
</div>

<!-- Figure: Verification Stack -->
<div class="figure-box">
<div class="figure-content">
<div class="flow-visual">
<div class="flow-step">
<div class="flow-title">measurement</div>
<div class="flow-sub">HD-EEG / fMRI / MEG<br>Quality assurance/synchronization</div>
</div>
<div class="flow-step">
<div class="flow-title">inverse problem</div>
<div class="flow-sub">Source estimation/uncertainty<br>retained as a distribution</div>
</div>
<div class="flow-step">
<div class="flow-title">causal modeling</div>
<div class="flow-sub">SCM/intervention design<br>Verification of counterfactual hypothesis</div>
</div>
<div class="flow-step">
<div class="flow-title">Identity verification</div>
<div class="flow-sub">PCI/Structure Preservation<br>minimum branch set</div>
</div>
</div>
</div>
<p class="figure-label">Figure 2</p>
<p class="figure-caption">The chain of "measurement → reconstruction → cause and effect → verification" required for WBE verification. Uncertainty at each stage is carried over to the next stage, and counterfactual equivalence is evaluated through intervention.</p>
</div>
</section>

<!-- Research Program -->
<section class="section" id="research-program">
<h2 class="section-title">Research Program</h2>

<p>A demonstration plan with publication in mind will comprehensively show each stage of measurement, deciphering, and implementation. The goal is to design and publish a ``personality maintenance'' evaluation system that integrates multimodal measurement and neural decoding. In addition, we will focus on EEG as a pillar of the measurement stage.<strong>Behavior-independent awareness index</strong>A roadmap of (complexity x perturbation response x criticality) is also specified.</p>

<!-- Table: Roadmap -->
<table class="data-table">
<thead>
<tr>
<th>Phase</th>
<th>Measurement/data</th>
<th>Decoding/Analysis</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>HD-EEG/fMRI simultaneous measurement setup, reproducibility data collection. Adoption of IHM and expansion of BIDS metadata.</td>
<td>In the brain-to-text system,<strong>No brain / No LM / shuffle / OOD / drift / latency</strong>Fix the evaluation pack to simultaneously audit and separate linguistic priors and neural contributions.</td>
</tr>
<tr>
<td>2</td>
<td>Fusion of ESI signal separation and MEG data. Validation of inverse problem constraints.</td>
<td>Inter-site causal dynamics analysis and generative model identification using Dynamic Causal Modeling (DCM).</td>
</tr>
<tr>
<td>3</td>
<td>Operation verification with WBA integration framework. Modeling of non-neuronal cells (glia).</td>
<td><strong>Neural Turing Test</strong>: Verifying the statistical identity of the "perturbation response (PCI)" of the original brain and the emulation.</td>
</tr>
</tbody>
</table>
</section>

<!-- Brain-to-Text Update -->
<section class="section" id="llm-research-update">
<h2 class="section-title" id="brain-to-text-update">Brain-to-Text update: language priors, streaming, evidence gate</h2>
<p>As of 2026-03, the primary literature does not show that a "general-purpose LLM operating theory" is the core of brain decoding. What matters is separating <strong>which modality</strong>, <strong>which task</strong>, <strong>which generalization condition</strong>, and <strong>whether a neural contribution beyond the language-prior distribution was actually confirmed</strong>. Tang et al.'s non-invasive semantic reconstruction required participant cooperation during both training and application.<sup><a href="#ref-30">[30]</a></sup> Horikawa et al.'s Mind Captioning advanced the generation of descriptions for visual content,<sup><a href="#ref-11">[11]</a></sup> but the question remains how much meaning can be restored through the communication subsystem alone. Non-invasive speech-perception decoding by Defossez et al.,<sup><a href="#ref-106">[106]</a></sup> word decoding by d'Ascoli et al.,<sup><a href="#ref-107">[107]</a></sup> and invasive speech neuroprostheses by Willett et al., Littlejohn et al., and Wairagkar et al.<sup><a href="#ref-108">[108]</a></sup><sup><a href="#ref-109">[109]</a></sup><sup><a href="#ref-110">[110]</a></sup> have all advanced the language and communication route. They do not, however, amount to WBE or self-model reproduction.</p>

<div class="note-box">
<strong>Site rule for 2026-03</strong>
<p>In this section, general discussions of RLHF, RAG, and agentic workflows are not the main evidence. The main evidence comes from the primary literature on <strong>brain-to-text, speech neuroprostheses, and neural encoding</strong>; general-purpose LLM papers are kept only as implementation notes.</p>
</div>

<h3>Dividing the evidence hierarchy into four parts</h3>
<table class="data-table">
<thead>
<tr>
<th>track</th>
<th>What the primary literature now supports</th>
<th>What this still does not justify</th>
<th>Treatment on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Non-invasive semantic/caption decoding</strong></td>
<td>Tang et al. showed semantic reconstruction of continuous language from fMRI, and Horikawa et al. showed description generation for visual content from brain activity.<sup><a href="#ref-30">[30]</a></sup><sup><a href="#ref-11">[11]</a></sup>.</td>
<td>It does not show subject-independent decoding, streaming of everyday interaction, or reproduction of causal internal states. Tang et al. themselves report that both training and application require participant cooperation.<sup><a href="#ref-30">[30]</a></sup>.</td>
<td><strong>L1-equivalent meaning restoration</strong></td>
</tr>
<tr>
<td><strong>Non-invasive word/speech decoding</strong></td>
<td>Defossez et al. demonstrated discrimination of 3-second speech intervals from non-invasive recordings, and d'Ascoli et al. showed that MEG, task design, and dataset size strongly affect large-scale word-decoding performance.<sup><a href="#ref-106">[106]</a></sup><sup><a href="#ref-107">[107]</a></sup>.</td>
<td>It does not demonstrate open-vocabulary's stable communication, reliable decoding in a single attempt, or long-term drift resistance.</td>
<td><strong>L1 enhancement candidates</strong></td>
</tr>
<tr>
<td><strong>invasive streaming speech neuroprosthesis</strong></td>
<td>Willett et al. demonstrated high-performance speech BCI with a vocabulary of 125,000 words, Littlejohn et al. demonstrated streaming brain-to-voice at 48 words per minute, and Wairagkar et al. demonstrated near-instant voice synthesis at roughly 10 ms latency.<sup><a href="#ref-108">[108]</a></sup><sup><a href="#ref-109">[109]</a></sup><sup><a href="#ref-110">[110]</a></sup>.</td>
<td>Whole-brain WBE, branch-equivalence, and long-term stable operation without the need for recalibration are not demonstrated. What was demonstrated here is a closed loop communication subsystem.</td>
<td><strong>Local benchmark for L2~L3</strong></td>
</tr>
<tr>
<td><strong>Neural encoding with LLM embedding</strong></td>
<td>Zada et al. and Goldstein et al. showed that contextual embeddings and representations of semantic relationships can predict brain activity during natural-language tasks.<sup><a href="#ref-111">[111]</a></sup><sup><a href="#ref-112">[112]</a></sup>.</td>
<td>This is neither thought reading nor decoder. Even if the LLM embedding explains brain responses well, it does not mean that it has "read the inside of the brain."</td>
<td><strong>measurement model / encoding benchmark</strong></td>
</tr>
</tbody>
</table>

<h3>Minimum required evaluation pack</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Isolation of neural contribution:</strong><code>no-brain</code>, <code>time-shuffle</code>, <code>trial-shuffle</code>, <code>LM-only</code>, and <code>no-LM</code>. When searching from a candidate set, specify the candidate set size.</li>
<li style="margin-bottom: 8px;"><strong>Boundary of generalization:</strong> Report held-out sentences, held-out stories, held-out vocabulary, cross-day, cross-task, and cross-subject separately, and state openly if participant cooperation or individual adaptation is required.<sup><a href="#ref-30">[30]</a></sup><sup><a href="#ref-107">[107]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Real-time metrics:</strong> If you claim streaming performance, do not report words per minute alone. Also report <strong>P50 / P95 / P99 latency</strong>, silence / abstention rate, dropout, recalibration burden, and recovery time.<sup><a href="#ref-109">[109]</a></sup><sup><a href="#ref-110">[110]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Reproduction log:</strong>The brain encoder, language model, vocoder, context window, beam width, external corpus, prompt, and calibration procedure are fixed, and if the model update crosses evaluation, it will be treated as a separate run.</li>
</ul>

<h3>Operation rules on Mind-Upload side</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Conditions for claiming L1:</strong>Show a neural contribution that exceeds the LM-only/shuffle baseline and do not hide candidate sets or evaluation conditions.</li>
<li style="margin-bottom: 8px;"><strong>Conditions for claiming L2:</strong>Include held-out conditions, cross-day or cross-task generalizations, and abstinence when confidence is low.</li>
<li style="margin-bottom: 8px;"><strong>Conditions for claiming L3:</strong>Submit streaming log, tail latency, silence/freeze, recalibration burden, and disclose closed-loop failure mode.</li>
<li style="margin-bottom: 8px;"><strong>Prohibitions for higher claims:</strong>Success in decoding, resemblance in embedding, and naturalness of conversation cannot be interpreted as emulate/WBE/preservation of identity.</li>
</ol>

<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Brain-to-Text</span>
<span class="tag">Language Prior</span>
<span class="tag">Streaming BCI</span>
<span class="tag">Abstention</span>
<span class="tag">Drift</span>
</div>
</section>

<!-- EEG Consciousness Roadmap -->
<section class="section" id="eeg-consciousness-roadmap">
<h2 class="section-title">Measuring consciousness with EEG: reading perturbation indicators as the main axis and resting indicators as an aid</h2>

<p>EEG is effective when handling consciousness-related information in the "measurement" stage of WBE, but it is not a device that can independently determine whether someone is "conscious or not." Current primary literature strongly supports that (a) perturbation response complexity is a candidate state-level benchmark, (b) no-report paradigms and criterion placement control are design conditions to reduce report/post-perceptual confound, (c) resting-state complexity/criticality is promising but remains an auxiliary readout, and (d) multimodal/multisite validation is required for clinical operation.<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-100">[100]</a></sup><sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup><sup><a href="#ref-104">[104]</a></sup><sup><a href="#ref-105">[105]</a></sup><sup><a href="#ref-113">[113]</a></sup>. Therefore, in this section we treat EEG not as a “single consciousness meter” but as a bundle of indicators with different strengths of evidence.</p>

<div class="note-box">
<strong>Site rule for this section</strong><br>On this site, <strong>no-report / criterion placement</strong> is the <strong>construct-validity gate</strong>, <strong>PCI / PCI-ST</strong> is the <strong>main benchmark candidate when sensory control and reliability logs are present</strong>, <strong>resting-state complexity / criticality</strong> remains an <strong>auxiliary proxy that must be calibrated within the same cohort</strong>, and <strong>clinical claims</strong> will not be promoted unless they come from a <strong>multimodal panel that exceeds the behavior-only baseline</strong>.</div>

<div class="note-box">
<strong>Construct validity must be audited separately</strong><br>Visual and auditory no-report studies are <strong>design conditions</strong>, not direct proof that EEG alone can serve as a bedside consciousness meter. On this site, cross-modal no-report evidence is used only as <strong>evidence for confound control</strong> and is kept separate from EEG benchmark evidence.<sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup><sup><a href="#ref-113">[113]</a></sup>.
</div>

<div class="note-box">
<strong>Listing four tracks is not enough</strong><br>Earlier versions of this page had the right direction, but the latest primary literature shows that even for the same "awareness index," the claim ceiling changes unless <strong>construct validity</strong>, <strong>perturbational validity</strong>, <strong>same-cohort calibration</strong>, and <strong>incremental validity over behavior</strong> are audited as separate gates. Remove criterion-placement control and the interpretation of no-report breaks down. Remove sensory contamination control and target-specific reliability, and the PCI / TMS-EEG readout becomes unstable. Remove same-cohort calibration and resting-state indicators remain proxies. Remove the behavior-only baseline and multimodal panels cannot claim deployability. Promotion therefore depends on whether the <a href="verification.html#consciousness-readout-gate">4 Gates of Verification</a> are passed.<sup><a href="#ref-113">[113]</a></sup><sup><a href="#ref-124">[124]</a></sup><sup><a href="#ref-125">[125]</a></sup><sup><a href="#ref-126">[126]</a></sup><sup><a href="#ref-127">[127]</a></sup><sup><a href="#ref-128">[128]</a></sup>.
</div>

<h3>5 conditions to fix first in this section</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Remove report confounds first</strong>: No-report paradigms are not consciousness readouts by themselves; they are design conditions for separating perception from post-report processing.<sup><a href="#ref-48">[48]</a></sup><sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Audit criterion placement in a separate log</strong>: Even with a no-report setup, leaving the response criterion unspecified risks picking up judgment strategy rather than conscious content.<sup><a href="#ref-113">[113]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Keep perturbation benchmarks on the main axis</strong>: PCI / PCI-ST is a powerful benchmark across altered states and disorders of consciousness, but TMS-EEG stimulus conditions and artifact management are prerequisites.<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-100">[100]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Use resting indicators only with external calibration</strong>: LZ complexity and criticality are promising, but they should not be used as primary judgments unless calibrated against perturbation metrics and clinical outcomes.<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-104">[104]</a></sup>.</li>
<li style="margin-bottom: 8px;"><strong>Require multimodal external validation for clinical claims</strong>: We prioritize incremental validity from bundles of behavior, imaging, and electrophysiology rather than the apparent strength of a single indicator.<sup><a href="#ref-55">[55]</a></sup><sup><a href="#ref-105">[105]</a></sup>.</li>
</ol>

<h3>4 tracks with different strengths of evidence</h3>
<table class="data-table">
<thead>
<tr>
<th>Track</th>
<th>What the primary literature supports now</th>
<th>What it still does not justify</th>
<th>Position on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PCI / PCI-ST</strong></td>
<td>Complex responses to perturbation are candidates for state-level benchmarks across anesthesia, sleep, and disorders of consciousness.<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-55">[55]</a></sup>.</td>
<td>They do not by themselves determine conscious content, personal identity, or theory validity. In prefrontal TMS-EEG, reliability and sensory contamination are target- and window-dependent, so omitting stimulus conditions, controls, or artifact windows makes benchmark comparisons invalid.<sup><a href="#ref-124">[124]</a></sup><sup><a href="#ref-125">[125]</a></sup>.</td>
<td><strong>Main benchmark candidate</strong></td>
</tr>
<tr>
<td><strong>No-report / criterion placement</strong></td>
<td>The literature increasingly supports these designs as ways to separate post-perceptual processing from response criterion in both vision and audition.<sup><a href="#ref-48">[48]</a></sup><sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup><sup><a href="#ref-113">[113]</a></sup>.</td>
<td>They do not by themselves become bedside meters, and without logs for criterion placement and report strategy, neural markers may still reflect judgment strategy rather than conscious content.</td>
<td><strong>Confound control</strong></td>
</tr>
<tr>
<td><strong>Resting complexity/criticality</strong></td>
<td>Changes associated with anesthesia, links to PCI, and the possibility of classifying consciousness without perturbation have been reported.<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-56">[56]</a></sup><sup><a href="#ref-126">[126]</a></sup>.</td>
<td>These are not replacements for perturbation-based indicators. Because spontaneous and evoked markers can dissociate in MCS,<sup><a href="#ref-104">[104]</a></sup> they will not be promoted to primary judgment unless calibrated against PCI, behavioral outcomes, and clinical outcomes in the same cohort.</td>
<td><strong>Auxiliary / exploration track</strong></td>
</tr>
<tr>
<td><strong>Multimodal clinical panel</strong></td>
<td>A multimodal panel that combines behavioral evaluation, HD-EEG, MRI, PET, and clinical variables may outperform behavior-only baselines for diagnosis and prognosis in coma / DoC.<sup><a href="#ref-105">[105]</a></sup><sup><a href="#ref-127">[127]</a></sup><sup><a href="#ref-128">[128]</a></sup>.</td>
<td>It still cannot be described as ready to deploy unless it shows incremental validity, out-of-site generalization, and robustness to missing modalities beyond the baseline.</td>
<td><strong>Deployability gate</strong></td>
</tr>
</tbody>
</table>

<h3>4 gates that determine promotion</h3>
<table class="data-table">
<thead>
<tr>
<th>gate</th>
<th>Minimum requirement</th>
<th>Claim to stop if it is not passed</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Construct validity</strong></td>
<td>Separate no-report from report, log criterion placement separately, and predefine failure conditions.</td>
<td>Do not claim that a neural marker directly reads conscious content itself.</td>
</tr>
<tr>
<td><strong>Perturbational validity</strong></td>
<td>TMS-EEG or intracranial perturbation conditions, sensory control, artifact windows, and target-specific reliability.</td>
<td>Do not call PCI-like values alone a state-level benchmark.</td>
</tr>
<tr>
<td><strong>Same-cohort calibration</strong></td>
<td>Calibrate PCI, behavior, clinical outcomes, and pipeline sensitivity analyses within the same cohort.</td>
<td>Do not call a resting-state metric a standalone bedside meter.</td>
</tr>
<tr>
<td><strong>Incremental validity</strong></td>
<td>Behavior-only baseline comparisons, external-site generalization, and calibration error under missing-modality conditions.</td>
<td>Do not describe a multimodal panel as ready to deploy.</td>
</tr>
</tbody>
</table>

<h3>Research priorities (A→C)</h3>
<table class="data-table">
<thead>
<tr>
<th>Track</th>
<th>Aim</th>
<th>Why prioritize now?</th>
<th>Conditions to proceed</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>Establish a perturbation benchmark</td>
<td>It currently offers the strongest verification basis and is comparatively easy to compare across state differences.<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup>.</td>
<td>Publish TMS-EEG stimulus-system logs, artifact windows, and test-retest reliability.<sup><a href="#ref-100">[100]</a></sup>.</td>
</tr>
<tr>
<td>B</td>
<td>Calibrate the resting proxy to the benchmark</td>
<td>It may reduce equipment burden, but it has not yet been shown to replace perturbation-based indices.<sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-104">[104]</a></sup>.</td>
<td>Proceed only with same-cohort calibration against PCI, behavioral outcomes, and clinical outcomes.</td>
</tr>
<tr>
<td>C</td>
<td>External validation with multimodal/multicentre</td>
<td>Clinical value is determined by incremental predictive power and cross-site reproducibility, not by single-lab success.<sup><a href="#ref-105">[105]</a></sup>.</td>
<td>Exceed the behavior-only baseline, be robust to missing measurements, and disclose calibration errors.</td>
</tr>
</tbody>
</table>

<h3>Roadmap (assuming graduate school)</h3>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>Phase 0: Infrastructure development (~1 year) - solidify “measurable” and “reproducible”</h4>
<p>Fix the EEG analysis pipeline so that the resting state index and report/criterion confound control can be reproduced on the same data.</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">Reproducible analysis including preprocessing, artifact removal, and logging (BIDS, etc.)</li>
<li style="margin-bottom: 8px;">In published data, associated with anesthesia/sedation<strong>Complexity/Spectrum/Connectivity</strong>Reproduce the changes in<sup><a href="#ref-23">[23]</a></sup><sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-53">[53]</a></sup></li>
<li style="margin-bottom: 8px;">Design the task so that both conditions with and without report can be run concurrently, and align with both visual/auditory no-report literature and criterion placement audits.<sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup><sup><a href="#ref-113">[113]</a></sup></li>
<li style="margin-bottom: 8px;">First check the test-retest reliability of LZ complexity, criticality, and spectral index using the same data.</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Reproducible Pipeline</span>
<span class="tag">No-Report</span>
<span class="tag">Spontaneous Metrics</span>
<span class="tag">Reliability</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>Phase 1: Perturbation benchmark (equivalent to years 1-2)—make the “PCI/PCI-ST line” auditable</h4>
<p>The response complexity to perturbations (TMS, sensory stimulation, etc.) is used as the main benchmark to enable state-level comparison.</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">Ideal: TMS-EEG handles PCI-based indicators and exposes the stimulation site, intensity, masking, and artifact window.<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-100">[100]</a></sup></li>
<li style="margin-bottom: 8px;">Real solution: When transferring the PCI-ST idea to other perturbations, the comparison target and failure mode should be fixed first.<sup><a href="#ref-51">[51]</a></sup></li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Perturbation</span>
<span class="tag">PCI / PCI-ST</span>
<span class="tag">Artifact Audit</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>Phase 2: Calibration of resting proxy (equivalent to 2nd to 3rd year)—“no perturbation” is included as an adjunct rather than a substitute</h4>
<p>Externally calibrate resting EEG complexity and criticality to perturbation metrics, behavioral, and clinical outcomes. The purpose is not to replace PCI, but to quantify how far it can be used as a proxy.</p>
<p style="margin-top: 8px;">Maschke et al. showed a relationship between criticality index and PCI under anesthesia induction.<sup><a href="#ref-52">[52]</a></sup>, Casarotto et al. reported that spontaneous markers and evoked markers can dissociate in MCS.<sup><a href="#ref-104">[104]</a></sup>. Therefore, we do not say "sufficient without perturbation", but instead audit condition-specific proxy performance.</p>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Resting-State EEG</span>
<span class="tag">Critical Dynamics</span>
<span class="tag">External Calibration</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>Phase 3: External validation (equivalent to years 3-4)—showing multimodal gains rather than “single indicators”</h4>
<p>In the final stage, we bundle EEG indicators with behavior/imaging/clinical variables and evaluate incremental validity from the perspectives of diagnosis, prognosis, and tolerance for missing data.</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">Rather than reporting the AUC of a single metric, it reports how much it beats the baseline and maintains calibration.<sup><a href="#ref-105">[105]</a></sup></li>
<li style="margin-bottom: 8px;">Evaluate deployability, including facility differences, measurement burden, and missing measurements</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Multimodal</span>
<span class="tag">Calibration</span>
<span class="tag">External Validation</span>
</div>
</div>
</div>
</div>

<div class="resolution-box">
<h5>ToDos from the past 1 to 3 months (in order of least effective)</h5>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 13px; line-height: 1.5; color: #d7e2cf;">
<li style="margin-bottom: 6px;">Fix the analysis pipeline and log schema and test-retest reliability of resting indicators first</li>
<li style="margin-bottom: 6px;">Correlate report presence/absence conditions with visual/auditory no-report documents and audit criterion placement in a separate log.<sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup><sup><a href="#ref-113">[113]</a></sup></li>
<li style="margin-bottom: 6px;">Reproduce changes associated with anesthesia/sedation once using public data<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup></li>
<li style="margin-bottom: 6px;">Pre-register stimulus logs and artifact windows for PCI/PCI-ST lines depending on whether or not to introduce perturbations.<sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-100">[100]</a></sup></li>
<li>Decide the public metrics for multimodal validation first to avoid misreading the resting proxy as a bedside meter.<sup><a href="#ref-105">[105]</a></sup></li>
</ul>
</div>

<h3>Technical position and goals</h3>
<p>This roadmap does not aim to prove the correctness of a particular theory of consciousness, but rather to make it possible to compare perturbation indicators, no-report control, resting state proxies, and multimodal clinical evaluations using the same audit schema. What Ferrante et al.'s adversarial test showed was not ``convergence to a single theory,'' but the point that theory and task design should be audited separately.<sup><a href="#ref-54">[54]</a></sup>.</p>
<p>Therefore, the goal of this section is not to declare a "world-standard standalone consciousness meter." As the multisite study by Manasova et al. shows, diagnosis and prognosis can improve when multimodal integration is added to behavioral assessment, but the indicators do not substitute for one another.<sup><a href="#ref-105">[105]</a></sup> The goal of this site is to accumulate a public benchmark that includes pre-registration, external validation, and abstention.</p>
</section>

<!-- Technical Proposals -->
<section class="section" id="technical-proposals">
<h2 class="section-title">Technical Proposals</h2>
<p>This is a concrete technology proposal that supports the research roadmap. Here, we have integrated the proposals into the main text and organized them to provide an overview of the evidence and implementation focus.</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">46</div>
<div class="stage-body">
<h4>Integration of measurement QA, synchronization and BIDS compliance</h4>
<p>Measurement-quality visualization (impedance / noise floor / CMRR) and synchronization standardization should be linked directly to the EEG-BIDS metadata structure. EEG-BIDS provides a framework centered on explicit metadata such as <code>dataset_description.json</code>, <code>eeg.json</code>, <code>channels.tsv</code>, and <code>electrodes.tsv</code>, which improves reproducibility and portability.</p>
<ul>
<li>Link the structure and essential metadata of BIDS-EEG with the QA log to leave a reproducible "measurement trail"<sup><a href="#ref-83">[83]</a></sup></li>
<li>Multimodal synchronization standardizes LSL sample timestamp and jitter correction<sup><a href="#ref-84">[84]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>

<div class="stage-item" id="proposal-47">
<div class="stage-number">47</div>
<div class="stage-body">
<h4>Enhanced preprocessing reproducibility and connectivity ceilings</h4>
<p>The emphasis is on ensuring reproducible artifact and line-noise control first, while keeping a separate audit ceiling for connectivity claims. Automatic ASR removal and ZapLine can improve reproducibility of cleanup, but they do <strong>not</strong> by themselves solve volume conduction, source leakage, or directional identifiability for wPLI, source-space connectivity, or STE.<sup><a href="#ref-85">[85]</a></sup><sup><a href="#ref-86">[86]</a></sup><sup><a href="#ref-129">[129]</a></sup><sup><a href="#ref-130">[130]</a></sup></p>
<ul>
<li>ASR is being evaluated as an automatic artifact removal method, and guidelines for parameter ranges have been provided.<sup><a href="#ref-85">[85]</a></sup></li>
<li>ZapLine is a proven method for line noise removal and can be applied to EEG/MEG<sup><a href="#ref-86">[86]</a></sup></li>
<li>wPLI reduces sensitivity to some zero-lag mixing and noise, but it is not a leak-proof inter-areal coupling meter; simulated EEG and source-space analyses still show source leakage and ghost-interaction ceilings.<sup><a href="#ref-87">[87]</a></sup><sup><a href="#ref-129">[129]</a></sup><sup><a href="#ref-130">[130]</a></sup></li>
<li>STE is useful as a directed-dependence estimator, but observational EEG alone does not settle causality. Ye et al. evaluated STE under TMS perturbation precisely because causality is difficult to identify from observations alone.<sup><a href="#ref-88">[88]</a></sup><sup><a href="#ref-131">[131]</a></sup></li>
<li>Recent benchmarking still finds that rereferencing, epoch design, and metric choice materially change sensor-space connectivity estimates, so this site treats connectivity pipelines as auditable configurations rather than stable readouts.<sup><a href="#ref-132">[132]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>

<div class="stage-item" id="proposal-48">
<div class="stage-number">48</div>
<div class="stage-body">
<h4>Neurotechnical enhancement (OPM-MEG/Hyper-scanning)</h4>
<p>OPM-MEG's portability and freedom of movement make measurements under VR and natural behavior realistic. The demonstration of wearable MEG provides the basis for incorporating "high time resolution measurement while moving" into the research pipeline.</p>
<ul>
<li>Demonstration of wearable MEG has made it possible to measure with natural movements<sup><a href="#ref-89">[89]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>

<div class="stage-item" id="proposal-56">
<div class="stage-number">56</div>
<div class="stage-body">
<h4>Identifiability and Causal Intervention (PCI/do-calculus)</h4>
<p>Counterfactual hypotheses cannot be tested through observation alone; they require intervention data. PCI, as TMS-EEG-based perturbation complexity, can therefore serve as <strong>one external benchmark</strong>, but it is not ground truth by itself. It should be used for comparing intervention-response distributions only when TMS-EEG recommendations on stimulation site, intensity, auditory masking, and myoelectric / stimulation artifact windows are satisfied.<sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>.</p>
<ul>
<li>The causal hierarchy consists of three layers: observation, intervention, and counterfactual hypotheticals.<sup><a href="#ref-91">[91]</a></sup></li>
<li>PCI has been proposed as a consciousness index using TMS-EEG response complexity, but should be read in conjunction with OOD conditions, calibration, and abstention conditions.<sup><a href="#ref-90">[90]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>

<div class="stage-item" id="proposal-58">
<div class="stage-number">58</div>
<div class="stage-body">
<h4>Addressing gaps in thermodynamics, causality, and IIT computational complexity</h4>
<p>"Logical costs" alone are not enough; computational costs and physical costs must be audited separately. However, Irreversibility and EPR will remain as exploratory supplementary logs for now, and IIT and EPR will not be made common required KPIs. The main decision is made using a bundle of perturbation, OOD, validation, and abstention conditions.</p>
<ul>
<li>Entropy production in non-equilibrium systems has been established as a quantitative indicator of irreversibility.<sup><a href="#ref-92">[92]</a></sup></li>
<li>IIT's MIP search has an exponential cost relative to the system size, so approximations and calculation strategies are required.<sup><a href="#ref-93">[93]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>

<div class="stage-item" id="proposal-61">
<div class="stage-number">61</div>
<div class="stage-body">
<h4>Reinforcing the logic gap in causality and thermodynamics</h4>
<p>The main focus is auditing of causal structure preservation, and irreversibility logs are supplemented only when necessary. EPR<sup><a href="#ref-92">[92]</a></sup>are treated as exploratory signals of coarse-grained neural dynamics and are not elevated to identity requirements.</p>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>

<div class="stage-item" id="proposal-62">
<div class="stage-number">62</div>
<div class="stage-body">
<h4>Strengthening thermodynamic and causal validity</h4>
<p>PCI<sup><a href="#ref-90">[90]</a></sup>and SCM<sup><a href="#ref-91">[91]</a></sup>The main focus is the irreversible log and the power/communication log, if necessary. Although we maintain the idea of ​​looking at both counterfactual and dissipation, EPR<sup><a href="#ref-92">[92]</a></sup>is not used as a standalone pass/fail indicator.</p>
<p><a href="issue.html#proposal-integration">→ To organize the proposal status and external dependencies, please refer to the contribution guide.</a></p>
</div>
</div>
</div>
</section>

<!-- Limitations -->
<section class="section" id="limitations">
<h2 class="section-title">Limitations and Epistemic Humility</h2>

<div class="note-box">
<strong>Clarify the limits of this page</strong>
<p>As a research note, we recognize and specify the following structural limitations. These are not "weaknesses" but requirements of scientific integrity.</p>
</div>

<h3>theoretical limits</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Avoiding hard problems:</strong>This page uses functional equivalence as an operational definition, but the identity of phenomenal consciousness is not subject to verification. Whether functionally complete emulation is a sufficient condition for ``having consciousness'' cannot be determined within the framework of this project (Chalmers, 1995).</li>
<li style="margin-bottom: 8px;"><strong>Limits of theoretical neutrality:</strong>Although it declares that it is ``independent of theory,'' the selection of indicators such as PCI itself may include implicit assumptions that favor IIT. This potential bias cannot be completely eliminated.</li>
<li style="margin-bottom: 8px;"><strong>FEP falsifiability:</strong>The free energy principle has been criticized as being too comprehensive and unfalsifiable. This project adopts FEP as the "implementation principle," but its validity needs to be separately verified using empirical results.</li>
<li style="margin-bottom: 8px;"><strong>Implications of Unfolding Argument:</strong>Doerig et al. (2019)<sup><a href="#ref-40">[40]</a></sup>If the above argument is correct, consciousness in the sense of IIT (Φ>0) does not arise in principle in digital emulation. A shift to neuromorphic infrastructure is essential, but its engineering feasibility remains untested.</li>
</ul>

<h3>engineering limits</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Observability upper limit:</strong> Non-invasive EEG / MEG / fMRI are macro proxies, and advances in local connectomics such as <a href="https://doi.org/10.1038/s41586-024-07558-y">Dorkenwald et al. (2024)</a> or <a href="https://doi.org/10.1038/s41586-025-08790-w">MICrONS Consortium et al. (2025)</a> do not directly imply state-complete observation of the human whole brain.</li>
<li style="margin-bottom: 8px;"><strong>Identifiability upper limit:</strong> The EEG inverse problem can be improved, but dependence on head model, conductivity, and candidate model family remains.<sup><a href="#ref-5">[5]</a></sup><sup><a href="#ref-79">[79]</a></sup><sup><a href="#ref-96">[96]</a></sup> Therefore, high fit quality and localization accuracy cannot be treated as unique reconstruction of internal state.</li>
<li style="margin-bottom: 8px;"><strong>Maintenance-state upper limit:</strong> <a href="https://doi.org/10.1016/j.cell.2016.01.046">Hengen et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuron.2021.04.004">Torrado Pacheco et al. (2021)</a>, <a href="https://doi.org/10.1038/s41467-024-47838-5">Xu et al. (2024)</a>, <a href="https://doi.org/10.1038/s41593-023-01558-3">Looser et al. (2024)</a>, and <a href="https://doi.org/10.1038/s41586-024-07311-5">Cahill et al. (2024)</a> together show that sleep / wake state, myelin, and glial / metabolic support remain separate variables. Reproducing same-day behavior and maintaining cross-day state are different problems.</li>
<li style="margin-bottom: 8px;"><strong>Upper limit of intervention scope:</strong> <a href="https://doi.org/10.1016/j.brs.2023.02.009">TMS-EEG recommendations</a>, <a href="https://doi.org/10.1126/science.abd0380">bidirectional BCI</a>, and <a href="https://doi.org/10.1038/s41591-024-03196-z">adaptive DBS</a> support local causal gain, but not whole-brain branch-equivalence. Comparability cannot be guaranteed without disclosing latency, jitter, and artifacts.</li>
<li style="margin-bottom: 8px;"><strong>Current state of reproducibility:</strong>The L0 (third-party reproducibility) set forth by this project has not been achieved at this time. The repository mainly contains website content, and executable code, data, and environment information are not made public.</li>
<li style="margin-bottom: 8px;"><strong>The severity of the connectome-dynamics gap:</strong>Although FlyWire and MICrONS have strengthened the structural scaffold, mapping structure to function, maintenance, and intervention response remains a core open question.</li>
</ul>

<h3>Limits of project management</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>Personal project:</strong>At this point, this is a personal research note and not a peer-reviewed study. External verification and expansion of joint research are necessary.</li>
<li style="margin-bottom: 8px;"><strong>Discrepancy between design and implementation:</strong>Many of the design policies described on this page remain at the document level and have not been made public as implementation code, test data, or evaluation results.</li>
</ul>
</section>

<!-- About -->
<section class="section" id="about">
<h2 class="section-title">About</h2>
<p><strong>Yasufumi Nakata</strong><br>Belongs to Keio University Faculty of Environment and Information Studies / Atsushi Aoyama Laboratory.<br>This site is a public research note regarding mind upload research.</p>
</section>

<!-- References -->
<section class="section references" id="references">
<h2 class="section-title">References</h2>
<ol>
<li id="ref-1" value="1">Fleming, S. M., et al. (2023). Open letter regarding "The integrated information
theory of consciousness". <em>Neuroscience of Consciousness</em>, 2023(1), niad001. <a
href="https://doi.org/10.31234/osf.io/zsr78">doi:10.31234/osf.io/zsr78</a></li>
<li id="ref-2" value="2">Tononi, G., et al. (2016). Integrated information theory: from consciousness to its
physical substrate. <em>Nat. Rev. Neurosci.</em>, 17, 450–461. <a
href="https://doi.org/10.1038/nrn.2016.44">doi:10.1038/nrn.2016.44</a></li>
<li id="ref-3" value="3">Hanson, J. R. (2023). On the non-uniqueness problem in integrated information theory.
<em>Neuroscience of Consciousness</em>, 2023(1), niad014. <a
href="https://doi.org/10.1093/nc/niad014">doi:10.1093/nc/niad014</a>
</li>
<li id="ref-4" value="4">Parfit, D. (1984). <em>Reasons and Persons</em>. Oxford University Press.</li>
<li id="ref-5" value="5">Michel, C. M., & Brunet, D. (2019). EEG source imaging: a practical review of the
methodology. <em>Frontiers in Neurology</em>, 10, 325. <a
href="https://doi.org/10.3389/fneur.2019.00325">doi:10.3389/fneur.2019.00325</a></li>
<li id="ref-6" value="6">Koch, C., Massimini, M., Boly, M., & Tononi, G. (2016). Neural correlates of consciousness: Progress and
problems. <em>Nature Reviews Neuroscience</em>, 17(5), 307–321. <a
href="https://doi.org/10.1038/nrn.2016.22">doi:10.1038/nrn.2016.22</a></li>
<li id="ref-7" value="7">Yamakawa, H., et al. (2024). Technology roadmap toward the completion of whole-brain
architecture with BRA-driven development. <em>Cognitive Systems Research</em>, 88, 101300. <a
href="https://doi.org/10.1016/j.cogsys.2024.101300">doi:10.1016/j.cogsys.2024.101300</a>
</li>
<li id="ref-8" value="8">Sandberg, A., & Bostrom, N. (2008). <em>Whole Brain Emulation: A Roadmap</em>. Future
of Humanity Institute, Oxford University. <a
href="https://www.philosophyofbrains.com/wp-content/uploads/2013/08/2008-3.pdf">Link</a>
</li>
<li id="ref-9" value="9">Logothetis, N. K. (2008). What we can do and what we cannot do with fMRI.
<em>Nature</em>, 453(7197), 869-878. <a
href="https://doi.org/10.1038/nature06976">doi:10.1038/nature06976</a>
</li>
<li id="ref-10" value="10">Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI.
<em>Nature</em>, 551(7679), 159-163. <a
href="https://doi.org/10.1038/551159a">doi:10.1038/551159a</a>
</li>
<li id="ref-11" value="11">Horikawa, T., et al. (2025). Mind captioning: Evolving descriptive text of mental
content from human brain activity. <em>Science Advances</em>, 11(45), eadw1464. <a
href="https://doi.org/10.1126/sciadv.adw1464">doi:10.1126/sciadv.adw1464</a></li>
<li id="ref-12" value="12">Kozlov, M. (2025). 'Mind-captioning' AI decodes brain activity to turn thoughts into
text. <em>Nature</em>, 647(8089), 297. <a
href="https://doi.org/10.1038/d41586-025-03624-1">doi:10.1038/d41586-025-03624-1</a>(Note: News article. For primary research, see [11])</li>
<li id="ref-13" value="13">Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling.
<em>NeuroImage</em>, 19(4), 1177-1202. <a
href="https://doi.org/10.1016/S1053-8119(03)00202-7">doi:10.1016/S1053-8119(03)00202-7</a>
</li>
<li id="ref-14" value="14">Friston, K. (2010). The free-energy principle: a rough guide to the brain.
<em>Nature Reviews Neuroscience</em>, 11(2), 127–138. <a
href="https://doi.org/10.1038/nrn2787">doi:10.1038/nrn2787</a>
</li>
<li id="ref-15" value="15">Vorwerk, J., et al. (2014). A guideline for head volume conductor modeling in EEG and MEG.
<em>NeuroImage</em>, 100, 590–607. <a
href="https://doi.org/10.1016/j.neuroimage.2014.06.040">doi:10.1016/j.neuroimage.2014.06.040</a></li>
<li id="ref-16" value="16">Markram, H. (2006). The Blue Brain Project. <em>Nature Reviews Neuroscience</em>,
7(2), 153-160. <a href="https://doi.org/10.1038/nrn1860">doi:10.1038/nrn1860</a></li>
<li id="ref-17" value="17">Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating
the properties of phenomenal existence in physical terms. <em>PLOS Computational Biology</em>,
19(10), e1011465. <a
href="https://doi.org/10.1371/journal.pcbi.1011465">doi:10.1371/journal.pcbi.1011465</a>
</li>
<li id="ref-18" value="18">Wipf, D., & Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging.
<em>NeuroImage</em>, 44(3), 947–966. <a
href="https://doi.org/10.1016/j.neuroimage.2008.02.059">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li id="ref-19" value="19">Özçete, Ö. D., et al. (2024). Mechanisms of neuromodulatory volume transmission.
<em>Molecular Psychiatry</em>. <a href="https://doi.org/10.1038/s41380-024-02608-3">doi:10.1038/s41380-024-02608-3</a></li>
<li id="ref-20" value="20">Cook, S. J., et al. (2019). Whole-animal connectomes of both <em>Caenorhabditis elegans</em> sexes.
<em>Nature</em>, 571(7763), 63–71. <a href="https://doi.org/10.1038/s41586-019-1352-7">doi:10.1038/s41586-019-1352-7</a></li>
<li id="ref-21" value="21">Scheffer, L. K., et al. (2020). A connectome and analysis of the adult <em>Drosophila</em> central
brain. <em>eLife</em>, 9. <a href="https://doi.org/10.7554/eLife.57443">doi:10.7554/eLife.57443</a></li>
<li id="ref-22" value="22">Kasthuri, N., et al. (2015). Saturated reconstruction of a volume of neocortex.
<em>Cell</em>, 162(3), 648–661. <a href="https://doi.org/10.1016/j.cell.2015.06.054">doi:10.1016/j.cell.2015.06.054</a></li>
<li id="ref-23" value="23">Purdon, P. L., et al. (2013). Electroencephalogram signatures of loss and recovery of consciousness from
propofol. <em>PNAS</em>, 110(12), E1142–E1151. <a href="https://doi.org/10.1073/pnas.1221180110">doi:10.1073/pnas.1221180110</a></li>
<li id="ref-24" value="24">Schumer, C., et al. (2025). <em>Management of Individuals' Neural Data (MIND) Act of
2025</em>. U.S. Senate Bill. (Note: Proposed bill as of Jan 12, 2026).</li>
<li id="ref-25" value="25">Gorgolewski, K. J., et al. (2016). The brain imaging data structure, a format for organizing and
describing outputs of neuroimaging experiments. <em>Scientific Data</em>, 3. <a
href="https://doi.org/10.1038/sdata.2016.44">doi:10.1038/sdata.2016.44</a></li>
<li id="ref-26" value="26">Pernet, C. R., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for
electroencephalography. <em>Scientific Data</em>, 6(1). <a
href="https://doi.org/10.1038/s41597-019-0104-8">doi:10.1038/s41597-019-0104-8</a></li>
<li id="ref-27" value="27">Ienca, M., & Andorno, R. (2017). Towards new human rights in neuroscience. <em>Life
Sciences, Society and Policy</em>, 13(1), 5. <a
href="https://doi.org/10.1186/s40504-017-0050-1">doi:10.1186/s40504-017-0050-1</a></li>
<li id="ref-28" value="28">Ji, Z., et al. (2023). Survey of Hallucination in Natural Language Generation. <em>ACM Computing
Surveys</em>, 55(12). <a href="https://doi.org/10.1145/3571730">doi:10.1145/3571730</a></li>
<li id="ref-29" value="29">Huth, A. G., et al. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex.
<em>Nature</em>, 532(7600), 453–458. <a href="https://doi.org/10.1038/nature17637">doi:10.1038/nature17637</a></li>
<li id="ref-30" value="30">Tang, J., et al. (2023). Semantic reconstruction of continuous language from non-invasive brain
recordings. <em>Nature Neuroscience</em>, 26(5), 858–866. <a
href="https://doi.org/10.1038/s41593-023-01304-9">doi:10.1038/s41593-023-01304-9</a></li>
<li id="ref-31" value="31">Boly, M., et al. (2017). Are the neural correlates of consciousness in the front or in the back of the
cerebral cortex? Clinical and neuroimaging evidence. <em>Journal of Neuroscience</em>, 37(40),
9603–9613. <a href="https://doi.org/10.1523/JNEUROSCI.3218-16.2017">doi:10.1523/JNEUROSCI.3218-16.2017</a></li>
<li id="ref-32" value="32">Whitehead, A. N. (1929). <em>Process and Reality: An Essay in Cosmology</em>Macmillan.
(Note: A classic of process philosophy. The year of publication and publisher may vary depending on the edition.)</li>
<li id="ref-33" value="33">Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual
cortex. <em>Nature</em>, 640(8058), 497–505. <a
href="https://doi.org/10.1038/s41586-025-08805-6">doi:10.1038/s41586-025-08805-6</a></li>
<li id="ref-39" value="39">Jun, S., Altmann, A., Sadaghiani, S., et al. (2025). Modulatory Neurotransmitter Genotypes Shape Dynamic
Functional Connectome Reconfigurations. <em>Journal of Neuroscience</em>, 45(10). <a
href="https://doi.org/10.1523/JNEUROSCI.1939-24.2025">doi:10.1523/JNEUROSCI.1939-24.2025</a>
(Open Access: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11884390/">PMC11884390</a>)</li>
<li id="ref-40" value="40">Doerig, A., et al. (2019). The unfolding argument: Why IIT and other causal
structure theories cannot explain consciousness. <em>Consciousness and Cognition</em>, 72, 49–59. <a
href="https://doi.org/10.1016/j.concog.2019.04.002">doi:10.1016/j.concog.2019.04.002</a>
</li>
<li id="ref-41" value="41">Santello, M., et al. (2019). Astrocyte-neuron interactions: from synapses to
networks and behavior. <em>Neuron</em>, 103(6), 985-1000. <a
href="https://doi.org/10.1016/j.neuron.2019.08.024">doi:10.1016/j.neuron.2019.08.024</a>
</li>
<li id="ref-42" value="42">Melloni, L., et al. (2023). An adversarial collaboration protocol for testing
contrasting predictions of global neuronal workspace and integrated information theory. <em>PLoS
ONE</em>, 18(3), e0282855. <a
href="https://doi.org/10.1371/journal.pone.0282855">doi:10.1371/journal.pone.0282855</a>
</li>
<li id="ref-43" value="43">Dehaene, S., Kerszberg, M., & Changeux, J. P. (1998). A neuronal model of a global
workspace in effortful cognitive tasks. <em>Proceedings of the National Academy of
Sciences</em>, 95(24), 14529-14534. <a
href="https://doi.org/10.1073/pnas.95.24.14529">doi:10.1073/pnas.95.24.14529</a></li>
<li id="ref-44" value="44">Tononi, G. (2015). Integrated information theory. <em>Scholarpedia</em>, 10(1),
4164. <a
href="http://www.scholarpedia.org/article/Integrated_information_theory">doi:10.4249/scholarpedia.4164</a>(Note: For a discussion of IIT's Intrinsic Existence axiom, see this review and [17])</li>
<li id="ref-45" value="45">Friston, K. (2017). Active inference: a process theory. <em>Neural Computation</em>, 29(1), 1–49. <a
href="https://doi.org/10.1162/NECO_a_00912">doi:10.1162/NECO_a_00912</a></li>
<li id="ref-46" value="46">Parr, T., & Friston, K. J. (2019). Generalised free energy and active inference.
<em>Biological cybernetics</em>, 113(4), 495-513. <a
href="https://doi.org/10.1007/s00422-019-00803-8">doi:10.1007/s00422-019-00803-8</a>
</li>
<li id="ref-47" value="47">Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R.,
... & Massimini, M. (2013). A theoretically based index of consciousness independent of sensory
processing and
behavior. <em>Science Translational Medicine</em>, 5(198), 198ra105. <a
href="https://doi.org/10.1126/scitranslmed.3006294">doi:10.1126/scitranslmed.3006294</a>
</li>
<li id="ref-48" value="48">Tsuchiya, N., et al. (2015). No-Report Paradigms: Extracting the True Neural Correlates of
Consciousness. <em>Trends in Cognitive Sciences</em>, 19(12), 757–770. <a
href="https://doi.org/10.1016/j.tics.2015.10.002">doi:10.1016/j.tics.2015.10.002</a></li>
<li id="ref-49" value="49">Massimini, M., et al. (2005). Breakdown of cortical effective connectivity during sleep.
<em>Science</em>, 309(5744), 2228–2232. <a href="https://doi.org/10.1126/science.1117256">doi:10.1126/science.1117256</a>
(Open Access: <a href="https://air.unimi.it/handle/2434/15471">air.unimi.it</a>)</li>
<li id="ref-50" value="50">Schartner, M., et al. (2015). Complexity of multi-dimensional spontaneous EEG decreases during
propofol induced general anaesthesia. <em>PLOS ONE</em>, 10(8). <a
href="https://doi.org/10.1371/journal.pone.0133532">doi:10.1371/journal.pone.0133532</a>
(Open Access: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4529106/">PMCID: PMC4529106</a>)</li>
<li id="ref-51" value="51">Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of
brain responses to transcranial and intracranial stimulations. <em>Brain Stimulation</em>, 12(5),
1280–1289. <a href="https://doi.org/10.1016/j.brs.2019.05.013">doi:10.1016/j.brs.2019.05.013</a></li>
<li id="ref-52" value="52">Maschke, C., et al. (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of
consciousness and perturbational complexity. <em>Communications Biology</em>, 7(1). <a
href="https://doi.org/10.1038/s42003-024-06613-8">doi:10.1038/s42003-024-06613-8</a></li>
<li id="ref-53" value="53">Anusha, A. S., et al. (2021). Brain Functional Connectivity as Biomarker for Propofol-Induced
Alterations of Consciousness. <em>Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)</em>, 1928–1931. <a
href="https://doi.org/10.1109/EMBC46164.2021.9629617">doi:10.1109/EMBC46164.2021.9629617</a></li>
<li id="ref-54" value="54">Ferrante, O., et al. (2025). Adversarial testing of global neuronal workspace and integrated
information theories of consciousness. <em>Nature</em>, 642(8066), 133–142. <a
href="https://doi.org/10.1038/s41586-025-08888-1">doi:10.1038/s41586-025-08888-1</a></li>
<li id="ref-55" value="55">Sinitsyn, D. O., et al. (2020). Detecting the potential for consciousness in unresponsive patients
using the perturbational complexity index. <em>Brain Sciences</em>, 10(12), 917. <a
href="https://doi.org/10.3390/brainsci10120917">doi:10.3390/brainsci10120917</a></li>
<li id="ref-56" value="56">Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex.
<em>The Neuroscientist</em>, 19(1), 88–100. <a
href="https://doi.org/10.1177/1073858412445487">doi:10.1177/1073858412445487</a></li>
<li id="ref-57" value="57">Azevedo, F. A., Carvalho, L. R., Grinberg, L. T., Farfel, J. M., Ferretti, R. E.,
Leite, R. E., ... & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells
make the human brain an isometrically scaled-up primate brain. <em>Journal of Comparative
Neurology</em>, 513(5), 532-541. <a
href="https://doi.org/10.1002/cne.21974">doi:10.1002/cne.21974</a></li>
<li id="ref-58" value="58">Weber, C. (2025). The multiplicity objection against uploading optimism.
<em>Synthese</em>, 205(6). <a href="https://doi.org/10.1007/s11229-025-05057-9">doi:10.1007/s11229-025-05057-9</a></li>
<li id="ref-59" value="59">Clowes, R. W. (2021). Slow Continuous Mind Uploading. <em>Studies in Brain and Mind</em>, 18,
161–183. <a href="https://doi.org/10.1007/978-3-030-72644-7_8">doi:10.1007/978-3-030-72644-7_8</a></li>
<li id="ref-60" value="60">Vaswani, A., et al. (2017). Attention Is All You Need. <em>Advances in Neural
Information Processing Systems (NeurIPS)</em>. <a
href="https://arxiv.org/abs/1706.03762">arXiv:1706.03762</a></li>
<li id="ref-61" value="61">Ouyang, L., et al. (2022). Training language models to follow instructions with
human feedback. <em>arXiv:2203.02155</em>. <a href="https://arxiv.org/abs/2203.02155">arXiv</a>
</li>
<li id="ref-62" value="62">Rafailov, R., et al. (2023). Direct Preference Optimization: Your Language Model is
Secretly a Reward Model. <em>arXiv:2305.18290</em>. <a
href="https://arxiv.org/abs/2305.18290">arXiv</a></li>
<li id="ref-63" value="63">Dettmers, T., et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs.
<em>arXiv:2305.14314</em>. <a href="https://arxiv.org/abs/2305.14314">arXiv</a></li>
<li id="ref-64" value="64">Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP
Tasks. <em>arXiv:2005.11401</em>. <a href="https://arxiv.org/abs/2005.11401">arXiv</a></li>
<li id="ref-65" value="65">Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models.
<em>arXiv:2210.03629</em>. <a href="https://arxiv.org/abs/2210.03629">arXiv</a></li>
<li id="ref-66" value="66">Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use
Tools. <em>arXiv:2302.04761</em>. <a href="https://arxiv.org/abs/2302.04761">arXiv</a></li>
<li id="ref-67" value="67">Manakul, P., et al. (2023). SelfCheckGPT: Zero-Resource Black-Box Hallucination
Detection for Generative Large Language Models. <em>arXiv:2303.08896</em>. <a
href="https://arxiv.org/abs/2303.08896">arXiv</a></li>
<li id="ref-70" value="70">Friston, K. J., et al. (2017). Active inference, mathematical constitution, and pure consciousness. <em>Frontiers in Psychology</em>, 8, 1322.</li>
<li id="ref-71" value="71">Zanichelli, N., et al. (2025). State of Brain Emulation Report 2025. <em>arXiv:2510.15745</em>.</li>
<li id="ref-73" value="73">Koulouri, A. (2025). Bayesian model parameter learning in linear inverse problems. <em>Machine Learning: Science and Technology</em>.</li>
<li id="ref-74" value="74">Nzakuna, P. S., et al. (2025). Monte Carlo-based Strategy for Assessing the Impact of EEG Data Uncertainty. <em>IEEE Transactions on Instrumentation and Measurement</em>.</li>
<li id="ref-76" value="76">Laukkonen, R. E., Friston, K., & Chandaria, S. (2025). A beautiful loop: An active inference theory of consciousness. <em>Neuroscience & Biobehavioral Reviews</em>, 183, 106296. <a href="https://doi.org/10.1016/j.neubiorev.2025.106296">doi:10.1016/j.neubiorev.2025.106296</a></li>
<li id="ref-77" value="77">Clark, A. (2013). The Mark of the Mental: In Search of the Markov Blanket. In: <em>The Mark of the Mental</em>. Oxford University Press.</li>
<li id="ref-78" value="78">Feng, Z., et al. (2025). Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620">doi:10.1109/TMI.2025.3642620</a></li>
<li id="ref-79" value="79">Aydin, U., Vorwerk, J., Küpper, P., et al. (2019). Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531">doi:10.3389/fnins.2019.00531</a></li>
<li id="ref-80" value="80">Whyte, C. J., Hohwy, J., Baltieri, M., et al. (2025). On the minimal theory of consciousness implicit in active inference. <em>Physics of Life Reviews</em>. <a href="https://doi.org/10.1016/j.plrev.2025.11.002">doi:10.1016/j.plrev.2025.11.002</a></li>
<li id="ref-81" value="81">Li, J., et al. (2025). Computational complexity reduction in Integrated Information Theory via low-dimensional embedding. <em>Chaos, Solitons & Fractals</em>.</li>
<li id="ref-82" value="82">Cai, C., et al. (2021). Robust estimation of noise for electromagnetic brain imaging with the Champagne algorithm. <em>NeuroImage</em>.</li>
<li id="ref-83" value="83">Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8">doi:10.1038/s41597-019-0104-8</a></li>
<li id="ref-84" value="84">Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136">doi:10.1162/IMAG.a.136</a></li>
<li id="ref-85" value="85">Chang, C.-Y., Hsu, S.-H., Pion-Tonachini, L., & Jung, T.-P. (2018). Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. <em>Proc. IEEE EMBC</em>. <a href="https://doi.org/10.1109/EMBC.2018.8512547">doi:10.1109/EMBC.2018.8512547</a></li>
<li id="ref-86" value="86">de Cheveigne, A. (2020). ZapLine: A simple and effective method to remove power line artifacts. <em>NeuroImage</em>, 207, 116356. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li id="ref-87" value="87">Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., & Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>, 55(4), 1548–1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li id="ref-88" value="88">Staniek, M., & Lehnertz, K. (2008). Symbolic Transfer Entropy. <em>Physical Review Letters</em>, 100, 158101. <a href="https://doi.org/10.1103/PhysRevLett.100.158101">doi:10.1103/PhysRevLett.100.158101</a></li>
<li id="ref-89" value="89">Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657–661. <a href="https://doi.org/10.1038/nature26147">doi:10.1038/nature26147</a></li>
<li id="ref-90" value="90">Casali, A. G., Gosseries, O., Rosanova, M., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <em>Science Translational Medicine</em>, 5(198), 198ra105. <a href="https://doi.org/10.1126/scitranslmed.3006294">doi:10.1126/scitranslmed.3006294</a></li>
<li id="ref-91" value="91">Correa, J. D., Lee, S., & Bareinboim, E. (2021). Nested Counterfactual Identification from Arbitrary Surrogate Experiments. <em>arXiv:2107.03190</em>. <a href="https://arxiv.org/abs/2107.03190">arXiv</a></li>
<li id="ref-92" value="92">Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001">doi:10.1088/0034-4885/75/12/126001</a></li>
<li id="ref-93" value="93">Kitazono, J., Kanai, R., & Oizumi, M. (2018). Efficient Algorithms for Searching the Minimum Information Partition in Integrated Information Theory. <em>Entropy</em>, 20(3), 173. <a href="https://doi.org/10.3390/e20030173">doi:10.3390/e20030173</a></li>
<li id="ref-94" value="94">Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y">doi:10.1038/s41586-024-07558-y</a></li>
<li id="ref-95" value="95">Chalmers, D. J. (1995). Facing up to the problem of consciousness. <em>Journal of Consciousness Studies</em>, 2(3), 200-219.</li>
<li id="ref-96" value="96">Frässle, S., et al. (2021). Regression DCMs for fMRI. <em>NeuroImage</em>, 227, 117566. <a href="https://doi.org/10.1016/j.neuroimage.2020.117566">doi:10.1016/j.neuroimage.2020.117566</a></li>
<li id="ref-97" value="97">Hoel, E., Albantakis, L., & Tononi, G. (2016). Can the macro beat the micro? Integrated information across spatiotemporal scales. <em>Neuroscience</em>, 311, 393–401. <a href="https://doi.org/10.1016/j.neuroscience.2016.09.049">doi:10.1016/j.neuroscience.2016.09.049</a></li>
<li id="ref-98" value="98">Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001">doi:10.1088/0034-4885/75/12/126001</a></li>
<li id="ref-99" value="99">Staniek, M. & Lehnertz, K. (2008). Symbolic Transfer Entropy. <em>Physical Review Letters</em>, 100(15), 158101. <a href="https://doi.org/10.1103/PhysRevLett.100.158101">doi:10.1103/PhysRevLett.100.158101</a></li>
<li id="ref-100" value="100">Hernandez-Pavon, J. C., Metsomaa, J., Mutanen, T. P., et al. (2023). TMS combined with EEG: Recommendations and open issues. <em>Brain Stimulation</em>, 16(2), 350–366. <a href="https://doi.org/10.1016/j.brs.2023.02.009">doi:10.1016/j.brs.2023.02.009</a></li>
<li id="ref-101" value="101">Srinivasan, R., Nunez, P. L., Tucker, D. M., Silberstein, R. B., & Cadusch, P. J. (1996). Spatial sampling and filtering of EEG with spline Laplacians to estimate cortical potentials. <em>Brain Topography</em>, 8(4), 355–366. <a href="https://doi.org/10.1007/BF01186911">doi:10.1007/BF01186911</a></li>
<li id="ref-102" value="102">Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing. <em>Cerebral Cortex</em>, 34(11), bhae415. <a href="https://doi.org/10.1093/cercor/bhae415">doi:10.1093/cercor/bhae415</a></li>
<li id="ref-103" value="103">Dellert, T., Balster, M., Schlossmacher, I., Bruchmann, M., Moeck, R., Straube, T., & Jacobsen, T. (2025). Neural correlates of consciousness in an auditory no-report fMRI study. <em>Current Biology</em>. <a href="https://doi.org/10.1016/j.cub.2025.10.026">doi:10.1016/j.cub.2025.10.026</a></li>
<li id="ref-104" value="104">Casarotto, S., Hassan, M., Rosanova, M., Sarasso, S., Derchi, C. C., Trimarchi, P. D., Viganò, A., Russo, S., Moraes, T., Naro, A., Pigorini, A., Leonardi, G., Gosseries, O., Laureys, S., Boly, M., Bodart, O., Casali, A. G., Colombo, M. A., Casali, K. R., & Comolatti, R. (2024). Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. <em>European Journal of Neuroscience</em>. <a href="https://doi.org/10.1111/ejn.16299">doi:10.1111/ejn.16299</a></li>
<li id="ref-105" value="105">Manasova, D., Belloli, T., Rosenfelder, M., Willacker, L., Fló Rama, M., Valota, A., Sinitsyn, D. O., Bourdillon, P., Comanducci, A., Heine, L., Sanz, L. R. D., Aabid, A., El-Daher, E., Liégeois-Chauvel, C., Biagioli, G., Woodruff, M., van Erp, W. S., Gomez, F., Gisquet, H., et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <em>Brain</em>. <a href="https://doi.org/10.1093/brain/awaf412">doi:10.1093/brain/awaf412</a></li>
<li id="ref-106" value="106">Défossez, A., Caucheteux, C., Rapin, J., Kabeli, O., & King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. <em>Nature Machine Intelligence</em>, 5, 1097–1107. <a href="https://doi.org/10.1038/s42256-023-00714-5">doi:10.1038/s42256-023-00714-5</a></li>
<li id="ref-107" value="107">d'Ascoli, S., Ferrante, O., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <em>Nature Communications</em>, 16, 10521. <a href="https://doi.org/10.1038/s41467-025-65499-0">doi:10.1038/s41467-025-65499-0</a></li>
<li id="ref-108" value="108">Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <em>Nature</em>, 620, 1031–1036. <a href="https://doi.org/10.1038/s41586-023-06377-x">doi:10.1038/s41586-023-06377-x</a></li>
<li id="ref-109" value="109">Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>, 28, 1711–1719. <a href="https://doi.org/10.1038/s41593-025-01905-6">doi:10.1038/s41593-025-01905-6</a></li>
<li id="ref-110" value="110">Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644, 145–152. <a href="https://doi.org/10.1038/s41586-025-09127-3">doi:10.1038/s41586-025-09127-3</a></li>
<li id="ref-111" value="111">Zada, Z., Goldstein, A., et al. (2024). Contextual embeddings from deep language models predict fMRI responses to naturalistic language. <em>Neuron</em>, 112(22), 3725–3740.e9. <a href="https://doi.org/10.1016/j.neuron.2024.09.018">doi:10.1016/j.neuron.2024.09.018</a></li>
<li id="ref-112" value="112">Goldstein, A., Bar, A., et al. (2025). Connecting concepts in the brain by mapping cortical representations of semantic relations. <em>Nature Neuroscience</em>, 28, 1841–1848. <a href="https://doi.org/10.1038/s41593-025-01903-8">doi:10.1038/s41593-025-01903-8</a></li>
<li id="ref-113" value="113">Fahrenfort, J. J., Johnson, D., Kloosterman, N. A., Stein, T., van Gaal, S., Pitts, M., & de Graaf, T. A. (2025). Criterion placement threatens the construct validity of neural measures of consciousness. <em>eLife</em>, 13, RP102335. <a href="https://doi.org/10.7554/eLife.102335">doi:10.7554/eLife.102335</a></li>
<li id="ref-114" value="114">Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144–150. <a href="https://doi.org/10.1038/s41586-020-2907-3">doi:10.1038/s41586-020-2907-3</a></li>
<li id="ref-115" value="115">Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <em>Nature</em>, 624, 317–332. <a href="https://doi.org/10.1038/s41586-023-06812-z">doi:10.1038/s41586-023-06812-z</a></li>
<li id="ref-116" value="116">MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w">doi:10.1038/s41586-025-08790-w</a></li>
<li id="ref-117" value="117">Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., & Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>, 165(1), 180–191. <a href="https://doi.org/10.1016/j.cell.2016.01.046">doi:10.1016/j.cell.2016.01.046</a></li>
<li id="ref-118" value="118">Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <em>Neuron</em>, 109(3), 530–544.e6. <a href="https://doi.org/10.1016/j.neuron.2021.04.004">doi:10.1016/j.neuron.2021.04.004</a></li>
<li id="ref-119" value="119">Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Communications</em>, 15, 3820. <a href="https://doi.org/10.1038/s41467-024-47838-5">doi:10.1038/s41467-024-47838-5</a></li>
<li id="ref-120" value="120">Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808">doi:10.1016/j.celrep.2024.114808</a></li>
<li id="ref-121" value="121">Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <em>Nature Neuroscience</em>, 27, 1598–1609. <a href="https://doi.org/10.1038/s41593-023-01558-3">doi:10.1038/s41593-023-01558-3</a></li>
<li id="ref-122" value="122">Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5">doi:10.1038/s41586-024-07311-5</a></li>
<li id="ref-123" value="123">Lee, J.-C., Wang, C.-Y., Lin, C.-L., & Lu, H.-C. (2022). Synaptic memory survives molecular turnover. <em>PNAS</em>, 119(42), e2211572119. <a href="https://doi.org/10.1073/pnas.2211572119">doi:10.1073/pnas.2211572119</a></li>
<li id="ref-124" value="124">Gogulski, J., Bailey, N. W., Hoy, K. E., & Rogasch, N. C. (2024). The reliability and variability of TMS-evoked potentials in the dorsolateral prefrontal cortex in healthy adults. <em>Brain Stimulation</em>, 17(4), 547–556. <a href="https://doi.org/10.1016/j.brs.2024.06.001">doi:10.1016/j.brs.2024.06.001</a></li>
<li id="ref-125" value="125">Biabani, M., Perera, T., Zalesky, A., et al. (2024). Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. <em>Imaging Neuroscience</em>, 2. <a href="https://doi.org/10.1162/imag_a_00349">doi:10.1162/imag_a_00349</a></li>
<li id="ref-126" value="126">Breyton, M., Lado, M. J., Laureys, S., et al. (2025). Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms. <em>eLife</em>, 13, RP98920. <a href="https://doi.org/10.7554/eLife.98920">doi:10.7554/eLife.98920</a></li>
<li id="ref-127" value="127">Rohaut, B., Naccache, L., Sitt, J. D., et al. (2024). Multimodal imaging reveals partially preserved semantic cognition in comatose patients after cardiac arrest. <em>Neurology</em>, 103(3), e209439. <a href="https://doi.org/10.1212/WNL.0000000000209439">doi:10.1212/WNL.0000000000209439</a></li>
<li id="ref-128" value="128">Kawai, R., Migdady, I., Kim, M. H., et al. (2025). Multimodal assessment improves neuroprognosis performance after out-of-hospital cardiac arrest. <em>Nature Medicine</em>, 31, 1065–1073. <a href="https://doi.org/10.1038/s41591-024-03019-1">doi:10.1038/s41591-024-03019-1</a></li>
<li id="ref-129" value="129">Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: A simulation study. <em>NeuroImage</em>, 64, 120–133. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li id="ref-130" value="130">Palva, J. M., Wang, S. H., Palva, S., Zhigalov, A., Monto, S., Brookes, M. J., Schoffelen, J.-M., &amp; Jerbi, K. (2018). Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <em>NeuroImage</em>, 173, 632–643. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li id="ref-131" value="131">Ye, S., Kitajo, K., &amp; Kitano, K. (2020). Information-theoretic approach to detect directional information flow in EEG signals induced by TMS. <em>Neuroscience Research</em>, 154, 87–96. <a href="https://doi.org/10.1016/j.neures.2019.09.003">doi:10.1016/j.neures.2019.09.003</a></li>
<li id="ref-132" value="132">Miljevic, A., Murphy, O. W., Fitzgerald, P. B., &amp; Bailey, N. W. (2025). Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. <em>Clinical Neurophysiology</em>, 174, 73–83. <a href="https://doi.org/10.1016/j.clinph.2025.03.043">doi:10.1016/j.clinph.2025.03.043</a></li>
</ol>
</section>

</article>

<!-- Sidebar -->
<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="verification.html">Verification infrastructure (Verification Commons) →</a></li>
<li><a href="verification.html#casework">Casework (historical pattern) →</a></li>
<li><a href="tech_roadmap.html#definition">Definition of forward movement (Roadmap) →</a></li>
<li><a href="perspective.html#design-principles">Theory frame section (Framework) →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Contents</h4>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#technical-framework">Technical Framework</a></li>
<li><a href="#decoding-to-emulation-gap">Decoding → Emulation</a></li>
<li><a href="#reproducibility">Reproducibility</a></li>
<li><a href="#key-technical-challenges">Key Technical Challenges</a></li>
<li><a href="#research-program">Research Program</a></li>
<li><a href="#llm-research-update">Brain-to-Text Update</a></li>
<li><a href="#eeg-consciousness-roadmap">EEG Consciousness Roadmap</a></li>
<li><a href="#technical-proposals">Technical Proposals</a></li>
<li><a href="#about">About</a></li>
<li><a href="#references">References</a></li>
</ul>
</div>

<div class="key-points">
<h4>Highlights</h4>
<ul>
<li>Translating theoretical conflicts such as IIT/GNWT into implementation requirements</li>
<li>Specify measures to overcome ESI inverse problems (IHM/uncertainty quantification)</li>
<li>Fixed claim ceiling for each measurement stack in the main text</li>
<li>Roadmap behavior-independent consciousness index using EEG complexity x perturbation response x criticality</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Study Overview</h4>
<p><strong>Objective:</strong>Design of a “maintenance of identity” evaluation system that integrates multimodal measurement and neural decoding</p>
<p style="margin-top:8px;"><strong>Design:</strong>Task-based + longitudinal collection at rest, comparison of invasive/non-invasive data</p>
</div>

<div class="sidebar-box">
<h4>Focus Areas</h4>
<ul>
<li>Measurement of brain activity (HD-EEG, ESI, fMRI)</li>
<li>Computational neuroscience (DCM, Transformer)</li>
<li>Theory of consciousness (IIT, psychological continuity)</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Technical Proposals</h4>
<ul>
<li><a href="#proposal-46">Issue #46: Measurement QA & BIDS</a></li>
<li><a href="#proposal-47">Issue #47: Strategic Extension</a></li>
<li><a href="#proposal-48">Issue #48: Neuroengineering & IIT</a></li>
<li><a href="#proposal-56">Issue #56: Identifiability & Intervention</a></li>
<li><a href="#proposal-58">Issue #58: Irreversibility & IIT Scaling</a></li>
<li><a href="#proposal-61">Issue #61: Causal & Thermodynamic Critique</a></li>
<li><a href="#proposal-62">Issue #62: Thermodynamic/Causal Validity</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Roadmaps</h4>
<ul>
<li><a href="tech_roadmap.html">Technology roadmap (learning) →</a></li>
<li><a href="#eeg-consciousness-roadmap">Consciousness Metrics (EEG) →</a>
<ul style="padding-left: 15px; margin-top: 4px; list-style-type: '— ';">
<li>Perturbation benchmark (PCI/PCI-ST)<sup><a href="#ref-47">[47]</a></sup></li>
<li>Separate report confound with no-report design<sup><a href="#ref-48">[48]</a></sup></li>
<li>Resting index calibrated as an auxiliary track<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup></li>
<li>emphasis on multimodal generalization<sup><a href="#ref-105">[105]</a></sup></li>
</ul>
</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Data Standards</h4>
<ul>
<li>Compliance with BIDS / EEG-BIDS standards<sup><a href="#ref-25">[25]</a></sup><sup><a href="#ref-26">[26]</a></sup> (<strong>task:</strong> metadata expansion is still urgently needed)</li>
<li>Publishing data structures and schema examples</li>
<li>Ensuring multi-center interoperability</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Resources</h4>
<ul>
<li><a href="brain_science_dictionary.html">Brain Science Dictionary →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Research Notes</h4>
<ul>
<li><a href="perspective.html#design-principles">theoretical frame clause</a></li>
<li><a href="issue.html#external-collaboration">External dependence/cooperation clause</a></li>
<li><a href="issue.html">Contribution Guide (Research Community)</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Paper Collection</h4>
<p>We are publishing materials that have been collected and translated from academic papers related to "Mind Uploading" over the past 10 years.</p>
<a href="mind_uploading_papers.html"
style="display: inline-block; margin-top: 10px; font-weight: bold; color: var(--color-accent);">View collection of papers
(HTML) →</a>
</div>

<div class="cta-box">
<h4>Contribute</h4>
<p>Would you like to participate in this project?</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">raise an issue</a>
</div>

</aside>
</main>
