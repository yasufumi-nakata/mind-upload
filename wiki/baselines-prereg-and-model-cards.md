---
layout: default
title: "Wiki: Baseline / Benchmark / Pre-registration / Model Card"
description: "Organizes baseline, benchmark, pre-registration, model cards, and the current claim-triggered companion, route-specific, and field-level card requirements so a score is not confused with comparable evidence."
article_type: Wiki
subtitle: "From score reporting to the current artifact stack required by the claim"
author: Mind Uploading Research Project
last_updated: "2026-04-04"
note: "Learning guide / current card-field sync"
audience: "People who find baseline, benchmark, pre-registration, and model-card language similar, and people who want to know which extra cards are required before a stronger claim is allowed"
reading_time: "12-18 minutes"
page_intro: "This page explains the operational difference among baseline, benchmark, pre-registration, model card, and the additional cards that become necessary when a result depends on multimodal fusion, large-scale pretraining, shortcut resistance, language-facing decoding, route-specific measurement / inference claims, living-human proxy bundles, or sequential same-subject bridges. The current revision also shows where card names alone became too coarse and where field-level disclosure is now required."
accuracy_note: "This page is a learning guide to the artifact stack. The authoritative card fields and stop rules still live on the public Verification page."
page_highlights:
  - "A benchmark is not just a score sheet; on this site it also includes split rules, metric semantics, and benchmark governance."
  - "A normal model card is not enough for every claim shape; some results need claim-triggered companion cards, and some now also need route-specific cards or logs."
  - "For decode or representation claims, shortcut resistance is a separate audit from score reporting."
  - "For language-facing text / speech outputs, the Neural Contribution Card is now treated separately from the generic shortcut audit."
  - "For multimodal or atlas-prior claims, a Fusion Card is separate from synchronization middleware or co-registration, and now also has to separate effective-window mismatch, shared-vs-specific factors, quantity bridges, and bundle robustness."
  - "For ESI, tractography, effective-connectivity, and thermodynamic claims, the current site rule now asks for route-specific disclosure rather than only a generic model card."
  - "For several living-human proxy rows used together, a Human Proxy Composition Card is required before same-subject state-identification language is allowed, and it now also has to disclose role by row, regime compatibility, operational maturity, calibrator role, and disagreement topology."
  - "For same-subject or same-brain sequential bridges, a State-Continuity Bridge Card is required before same-state language is allowed, and it now also has to name the carried object, tolerance / failure rule, and rescue route."
known_points:
  - "Comparable progress requires a baseline, a benchmark object, preregistered stopping rules, a result report, and explicit failure disclosure."
  - "Benchmark meaning depends not only on the dataset and score, but also on split randomness, metric bundle, extra-data policy, operational constraints, and postmortems."
  - "Observability Budget, Specificity & Shortcut Card, Neural Contribution Card, Fusion Card, Pretraining Card, route-specific cards / logs, Human Proxy Composition Card, Temporal Validity Card, Calibration & Abstention Card, and State-Continuity Bridge Card answer different failure modes."
  - "Card names alone are no longer sufficient on this site: Fusion, Human Proxy Composition, and State-Continuity Bridge Cards each now require field-level disclosure to block newer forms of overreading."
  - "A higher score can still be scientifically weak if the artifact stack does not match the claim being made."
unknown_points:
  - "Which subsets of this artifact stack will become field-wide defaults beyond this site is still unsettled."
  - "The exact minimum disclosure expected for negative results and failure examples will continue to evolve."
wiki_links:
  - label: "Wiki: Verification Basics"
    url: "/wiki/verification-basics.html"
    description: "A wider map of why standards, benchmarks, registries, and audits are needed."
  - label: "Wiki: Dataset Splits and Leakage"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "Explains split hygiene, acquisition-distribution shortcuts, and benchmark provenance."
  - label: "Wiki: EEG Foundation Models"
    url: "/wiki/eeg-foundation-models.html"
    description: "Explains why pretraining claims need more than a generic model card."
  - label: "Wiki: Human Proxy Composition"
    url: "/wiki/human-proxy-composition.html"
    description: "Explains when several living-human proxy rows may or may not be promoted together."
  - label: "Wiki: From Observation To Estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Organizes inverse problems, ESI, effective connectivity, and causal-equivalence limits."
  - label: "Wiki: Uncertainty, Calibration, and Abstention"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "Explains when probabilities, prediction sets, and abstentions need their own card."
  - label: "Wiki: Thermodynamic Grounding Basics"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Explains why irreversibility language needs signal-route, estimator-family, and quantity-type disclosure."
  - label: "Wiki: Closed Loops, Latency, Jitter, and Safety Stops"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Explains why intervention timing and body/environment boundary are separate audits."
  - label: "Wiki: State-Continuity Bridge"
    url: "/wiki/state-continuity-bridge.html"
    description: "Explains why same-subject or same-brain wording does not automatically mean same-state evidence."
recommended_pages:
  - label: "Verification"
    url: "/verification.html"
  - label: "Datasets / L0 Practice"
    url: "/datasets.html#l0-practice"
  - label: "Verification Casework"
    url: "/verification.html#casework"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest map</h2>
<p>
A <strong>baseline</strong> is the minimum comparison partner. A <strong>benchmark</strong> fixes not only the task and score but also the split rules, metric bundle, and operational reading of the result. <strong>Pre-registration</strong> fixes what success, failure, and abstention mean before the run starts. A <strong>model card</strong> reports what happened. Additional cards are then attached depending on the claim shape. Without that stack, a good score is still not comparable progress.
</p>
</div>

<div class="note-box">
<strong>2026-03 addendum: L1 and above still need an Observability Budget</strong>
<p>
For L1 and higher results, this site still stacks the <a href="../verification.html#observability-budget">Observability Budget</a> on top of the usual model card so the measurement stack, direct observables, residual latent state, claim ceiling, and abstention conditions are visible rather than implied by the score.
</p>
</div>

<div class="note-box">
<strong>2026-03-25 addendum: a benchmark is not just data plus one score</strong>
<p>
The earlier version of this page still let <strong>benchmark</strong> sound like a static score sheet. That is too weak. The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) homepage</a> states that the original challenge preprint became outdated during execution and that the website plus starter kit should be treated as current. The official <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> require disclosure of <strong>additional pretraining data</strong>, <strong>pretrained models / fine-tuning method</strong>, and <strong>single-GPU 20 GB inference-stage constraints</strong>, while the official <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> later disclosed that Challenge 2 samples had not been randomized, which changed the prize structure and what the ranking meant. <a href="https://arxiv.org/abs/2508.17742" target="_blank">Xiong et al. (2025)</a> and <a href="https://arxiv.org/abs/2601.17883" target="_blank">Liu et al. (2026)</a> then showed more generally that protocol and evaluation choices materially affect EEG-foundation-model comparisons. Likewise, <a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp; Rehmsmeier (2015)</a>, <a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">Roy et al. (2021)</a>, <a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">Sun et al. (2017)</a>, and <a href="https://doi.org/10.7554/eLife.70092" target="_blank">Vallat &amp; Walker (2021)</a> show why <strong>metric semantics</strong> also change what a score means. Therefore, on this site, a benchmark now includes <strong>split / randomization rule</strong>, <strong>task-matched metric bundle</strong>, <strong>benchmark version</strong>, <strong>extra-data / checkpoint policy</strong>, <strong>inference-stage restrictions</strong>, and <strong>organizer postmortems</strong>, not only a dataset name and one number.
</p>
</div>

<div class="note-box">
<strong>2026-03-25 addendum: a model card is not the whole artifact stack</strong>
<p>
The next weakness was to let a generic <strong>model card</strong> sound like the final reporting layer for every result. That is also too weak. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a>, and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> show why decoding and transfer claims can still ride on <strong>subject / acquisition shortcuts</strong>, so score reporting alone does not establish target-variable specificity. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a>, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a>, and <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> show why <strong>simultaneous</strong> or <strong>multimodal</strong> does not replace a fusion audit. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a>, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a>, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> constrain different living-human quantity types and burdens rather than one already field-ready whole-brain meter. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a>, <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a>, <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a>, and <a href="https://doi.org/10.1038/nature14467" target="_blank">Attardo et al. (2015)</a> show why same-subject or same-brain wording still leaves a sequential bridge burden. Therefore, on this site, the model card is only one layer in a <strong>claim-triggered artifact stack</strong>.
</p>
</div>

<div class="note-box">
<strong>2026-03-30 addendum: generic companion cards are no longer enough for the current site rule</strong>
<p>
The next weakness on this page was narrower but important: it still listed only the earlier generic companion cards, even though the current public site now requires <strong>route-specific cards or logs</strong> for several claim families. The primary literature does not support compressing these routes into one generic reporting layer. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a>, <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> show why language-facing outputs need a <strong>Neural Contribution Card</strong> plus temporal and calibration disclosure rather than only a score. <a href="https://doi.org/10.1016/j.clinph.2023.08.009" target="_blank">Horrillo-Maysonnial et al. (2023)</a>, <a href="https://doi.org/10.1016/j.clinph.2025.04.009" target="_blank">Rong et al. (2025)</a>, and <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> show why ESI claims need validation-class, source-regime, and benchmark-object typing plus solver-disagreement disclosure. <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">Gajwani et al. (2023)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">He et al. (2024)</a>, and <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">Manzano-Patr&oacute;n et al. (2025)</a> show why tractography needs object typing rather than one graph headline. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a>, <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">Barnett &amp; Seth (2017)</a>, <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde et al. (2019)</a>, and <a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025)</a> show why effective-connectivity graphs remain model-conditioned unless closure, node policy, and sampling sensitivity are disclosed. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> show why irreversibility language hides multiple estimator families and closure assumptions. Therefore, this page now separates <strong>generic companion cards</strong> from <strong>route-specific cards / logs</strong> instead of treating them as one bucket.
</p>
</div>

<div class="note-box">
<strong>2026-04-04 addendum: three cards now need field-level disclosure, not name-level disclosure</strong>
<p>
The next weakness on this page became visible only after the route-stack expansion: three cards still sounded satisfied by a short label even though the current primary literature says otherwise. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>, <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a>, <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a>, <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> show why <strong>Fusion</strong> still has to separate synchronization, temporal-kernel relation, shared-vs-specific structure, quantity bridge, and bundle robustness. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B&oslash;gh et al. (2024)</a>, <a href="https://doi.org/10.1002/nbm.5256" target="_blank">Morgan et al. (2024)</a>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> show why <strong>Human Proxy Composition</strong> still has to separate quantity type, operating-point dependence, method-family non-equivalence, and disagreement topology. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a>, <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a>, <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a>, <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a>, <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> show why <strong>State-Continuity Bridge</strong> still has to name the carried object, tolerance rule, and rescue route rather than relying on specimen identity or score survival alone. Therefore, this guide no longer treats those three cards as satisfied by a short name plus one sentence.
</p>
</div>

<section class="section" id="roles">
<h2 class="section-title">First separate the roles</h2>
<table class="data-table">
<thead>
<tr>
<th>Artifact</th>
<th>Main role</th>
<th>What it fixes that the others do not</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Baseline</strong></td>
<td>The minimum comparison partner.</td>
<td>Prevents a new score from being read without context.</td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>The benchmark object: task, split rules, metric bundle, and governance.</td>
<td>Fixes what comparison actually means before any score is interpreted.</td>
</tr>
<tr>
<td><strong>Pre-registration</strong></td>
<td>The promise made before the run.</td>
<td>Fixes success, failure, stopping, and abstention rules before hindsight pressure appears.</td>
</tr>
<tr>
<td><strong>Model card</strong></td>
<td>The result report for one trained system.</td>
<td>Records scores, baselines, failure examples, compute usage, and practical weaknesses of the submitted system.</td>
</tr>
<tr>
<td><strong>Observability Budget</strong></td>
<td>The measurement-side ceiling.</td>
<td>Fixes what was directly observed, what remained latent, and which claim ceiling still applies.</td>
</tr>
<tr>
<td><strong>Specificity &amp; Shortcut Card</strong></td>
<td>The shortcut audit for decode / biomarker / transfer claims.</td>
<td>Separates the target neural variable from subject, session, site, device, protocol, and other nuisance routes.</td>
</tr>
<tr>
<td><strong>Neural Contribution Card</strong></td>
<td>The language-facing shortcut audit.</td>
<td>Fixes task constraint, candidate set, prompt or language-model scaffold, no-brain / no-LM / shuffle controls, and subject cooperation for text / speech outputs.</td>
</tr>
<tr>
<td><strong>Fusion Card</strong></td>
<td>The multimodal / atlas-prior integration audit.</td>
<td>Fixes acquisition relation, lag audit, <strong>effective-window / temporal-kernel relation</strong>, geometry / co-registration scope, fusion model, <strong>shared-vs-specific component disclosure</strong>, <strong>quantity bridge / physiology grounding</strong>, unimodal baselines, <strong>complete-case / missing-modality disclosure</strong>, transfer or disagreement window, external calibration, and abstention.</td>
</tr>
<tr>
<td><strong>Pretraining Card</strong></td>
<td>The EEG foundation / self-supervised transfer audit.</td>
<td>Fixes corpus identity / overlap, harmonization, adaptation regime, benchmark provenance, and efficiency constraints.</td>
</tr>
<tr>
<td><strong>Route-specific cards / logs</strong></td>
<td>The claim-family-specific disclosure layer.</td>
<td>Types ESI, tractography, effective-connectivity, irreversibility, intervention, and boundary claims by their own failure modes instead of compressing them into one generic report.</td>
</tr>
<tr>
<td><strong>Human Proxy Composition Card</strong></td>
<td>The bundle audit for several living-human proxy rows.</td>
<td>Fixes proxy class, <strong>direct observable and evidence role by row</strong>, same-subject relation, <strong>effective time window / state axis</strong>, regime compatibility, <strong>operational maturity</strong>, <strong>calibrator role</strong>, model burden, <strong>method-family non-equivalence</strong>, <strong>agreement / disagreement topology plus resolution policy</strong>, incremental evidence, and residual latent-state ceiling.</td>
</tr>
<tr>
<td><strong>State-Continuity Bridge Card</strong></td>
<td>The sequential bridge audit.</td>
<td>Fixes acquisition order, elapsed time, regime continuity, coordinate transfer / deformation, <strong>carried object / bridge witness</strong>, <strong>tolerance / failure rule</strong>, <strong>rescue route versus raw continuity</strong>, bridge-validation rung, and residual drift ceiling before same-state language is allowed.</td>
</tr>
<tr>
<td><strong>Temporal Validity Card</strong></td>
<td>The time-generalization ceiling.</td>
<td>Fixes fixed-decoder interval, state annotation, recalibration burden, drift handling, and transfer ceiling across hours to days.</td>
</tr>
<tr>
<td><strong>Calibration &amp; Abstention Card</strong></td>
<td>The uncertainty and fallback audit.</td>
<td>Fixes fit / calibration / test separation, evaluation slice, coverage-risk target, and fallback behavior when outputs include confidence or abstention.</td>
</tr>
<tr>
<td><strong>Failure examples / negative results</strong></td>
<td>The record of where things broke.</td>
<td>Prevents the field from learning only from accidental successes.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="benchmark-object">
<h2 class="section-title">What a benchmark fixes on this site</h2>
<table class="data-table">
<thead>
<tr>
<th>Benchmark field</th>
<th>Why it matters</th>
<th>What goes wrong if it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Task and target definition</strong></td>
<td>States exactly what is predicted or detected.</td>
<td>A score can be overread as if it applied to a broader task family.</td>
</tr>
<tr>
<td><strong>Split / randomization rule</strong></td>
<td>Defines whether subject, session, trial order, and hidden grouping were controlled.</td>
<td>Identity or contiguous-trial shortcuts can change the meaning of the leaderboard.</td>
</tr>
<tr>
<td><strong>Task-matched metric bundle</strong></td>
<td>Fixes which metrics are needed for this task, such as false alarms, latency, macro-F1, or kappa.</td>
<td>One headline score can hide the real failure mode.</td>
</tr>
<tr>
<td><strong>Extra-data / checkpoint policy</strong></td>
<td>States whether outside data or pretrained models changed the comparison.</td>
<td>Transfer gains can be misread as if they came only from the submitted pipeline.</td>
</tr>
<tr>
<td><strong>Operational restrictions</strong></td>
<td>Fixes inference-time compute, code-submission conditions, and other deployment-side constraints.</td>
<td>A result can be misread as portable when it depended on a looser operating regime.</td>
</tr>
<tr>
<td><strong>Version / postmortem status</strong></td>
<td>States whether organizer updates, starter-kit changes, or later error disclosures changed the benchmark object.</td>
<td>An obsolete preprint or early leaderboard can be overread as the final benchmark truth.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="claim-triggered-stack">
<h2 class="section-title">Which extra artifacts are triggered by the claim</h2>
<table class="data-table">
<thead>
<tr>
<th>Claim shape</th>
<th>Base stack</th>
<th>Extra artifact to add</th>
<th>What it blocks</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Any L1+ measurement claim</strong></td>
<td>Baseline + Benchmark + Pre-registration + Model card</td>
<td><strong>Observability Budget</strong></td>
<td>Stops a measurement stack from being overread as if it directly observed more than it did.</td>
</tr>
<tr>
<td><strong>Decode / biomarker / transfer claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Specificity &amp; Shortcut Card</strong></td>
<td>Stops subject / session / site / device / protocol shortcuts from being mistaken for target-variable capture.</td>
</tr>
<tr>
<td><strong>Foundation / self-supervised EEG claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Pretraining Card</strong> plus <strong>Specificity &amp; Shortcut Card</strong></td>
<td>Stops a transfer win from being overread as generic portability or shortcut-resistant representation learning.</td>
</tr>
<tr>
<td><strong>Language-facing text / speech / brain-to-text claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Neural Contribution Card</strong> plus <strong>Specificity &amp; Shortcut Card</strong>; add <strong>Calibration &amp; Abstention Card</strong> when confidence, retrieval-set, or prediction-set language is reported.</td>
<td>Stops fluent output or top-k retrieval from being overread as if neural contribution, confidence, and prompt dependence were already separated.</td>
</tr>
<tr>
<td><strong>EEG source imaging / inverse reconstruction claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Inverse-Solver Agreement Log</strong> plus named validation class, source regime, montage / coverage policy, and benchmark-object disclosure.</td>
<td>Stops one localization headline from being overread as if depth bias, source extent, coverage geometry, and solver disagreement were already resolved.</td>
</tr>
<tr>
<td><strong>Diffusion-MRI tractography / structural-connectome claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Tractography route card</strong></td>
<td>Stops one tractography graph from being overread as if acquisition, endpoint assignment, graph construction, uncertainty, and calibration were fixed.</td>
</tr>
<tr>
<td><strong>Effective-connectivity / DCM / directed-graph claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Effective-connectivity route card</strong></td>
<td>Stops a directed graph from being overread as discovered causal wiring when candidate-model family, closure, node policy, and sampling sensitivity remain implicit.</td>
</tr>
<tr>
<td><strong>Thermodynamic / irreversibility claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Irreversibility / thermodynamic route card</strong></td>
<td>Stops arrow-of-time or entropy-flow language from being overread as if signal route, coarse-graining, estimator family, and quantity type were already fixed.</td>
</tr>
<tr>
<td><strong>Multimodal or atlas-prior claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Fusion Card</strong></td>
<td>Stops simultaneity, synchronization middleware, or a prior from standing in for validated fusion.</td>
</tr>
<tr>
<td><strong>Intervention / closed-loop claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Intervention Card</strong>; for embodied or human-in-the-loop claims, also add the <strong>Body / Environment Boundary Card</strong>.</td>
<td>Stops low latency or one control trace from standing in for a typed intervention, preserved loop boundary, or safe deployment claim.</td>
</tr>
<tr>
<td><strong>Several living-human proxy rows used together</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Human Proxy Composition Card</strong></td>
<td>Stops proxy-rich bundles from being overread as same-subject state identification when role by row, regime compatibility, maturity, and disagreement remain implicit.</td>
</tr>
<tr>
<td><strong>Same-subject / same-brain sequential bridge</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>State-Continuity Bridge Card</strong>; add <strong>Temporal Validity Card</strong> when the bridge crosses hours to days or a fixed-decoder interval is claimed.</td>
<td>Stops specimen identity, score survival, or rescue-dependent stability from being overread as same-state evidence or stable time-generalization.</td>
</tr>
<tr>
<td><strong>Outputs with probabilities, intervals, prediction sets, or abstention</strong></td>
<td>Base stack + the cards already triggered by the claim</td>
<td><strong>Calibration &amp; Abstention Card</strong></td>
<td>Stops raw confidence, threshold tuning, or selective reporting from being overread as calibrated risk control.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="field-level-sync">
<h2 class="section-title">Three cards whose short labels had become too weak</h2>
<p>
The next problem was not card count but <strong>card sufficiency</strong>. After the stack expansion, these three cards still sounded satisfied by a short label even though the current site rule had already become stricter. This section brings the learning guide up to that current field-level requirement.
</p>
<table class="data-table">
<thead>
<tr>
<th>Card</th>
<th>Why the older short description is now too weak</th>
<th>Minimum fields this guide now expects</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fusion Card</strong></td>
<td><a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>, <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a>, <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a>, <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> show why synchronized acquisition, shared low-frequency structure, a quantity bridge, and bundle robustness are different achievements.</td>
<td><strong>Acquisition relation</strong>, <strong>effective-window / temporal-kernel relation</strong>, <strong>shared-vs-specific component disclosure</strong>, <strong>quantity bridge / physiology grounding</strong>, unimodal and prior-only baselines, <strong>complete-case / missing-modality policy</strong>, transfer or disagreement window, external calibration, and abstention.</td>
</tr>
<tr>
<td><strong>Human Proxy Composition Card</strong></td>
<td><a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B&oslash;gh et al. (2024)</a>, <a href="https://doi.org/10.1002/nbm.5256" target="_blank">Morgan et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> show why quantity type, operating point, common-driver burden, and disagreement topology still matter even when all rows are real human data.</td>
<td><strong>Proxy class</strong>, <strong>direct observable and evidence role by row</strong>, <strong>effective time window / state axis</strong>, regime compatibility, <strong>operational maturity</strong>, <strong>calibrator role</strong>, <strong>method-family non-equivalence</strong>, cross-row agreement / disagreement plus resolution policy, increment over the strongest single row, and residual latent-state ceiling.</td>
</tr>
<tr>
<td><strong>State-Continuity Bridge Card</strong></td>
<td><a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a>, <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a>, <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a>, <a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">Van De Ville et al. (2021)</a>, <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a>, <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> show why specimen identity, carried object, rescue strategy, and score survival are different objects.</td>
<td><strong>Bridge class</strong>, acquisition order, elapsed time, regime continuity, coordinate transfer / deformation, <strong>carried object / witness</strong>, <strong>tolerance / failure rule</strong>, <strong>rescue route versus raw continuity</strong>, bridge-validation rung, and residual drift ceiling.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="route-specific-cards">
<h2 class="section-title">Why route-specific cards had to be added</h2>
<table class="data-table">
<thead>
<tr>
<th>Claim family</th>
<th>Why a generic score sheet is too weak</th>
<th>Card or log this site now asks for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Language-facing decode / speech</strong></td>
<td>High scores can still come from candidate-set restriction, language priors, prompt scaffolds, or session-specific support rather than the target neural route alone.</td>
<td><strong>Neural Contribution Card</strong> plus <strong>Specificity &amp; Shortcut Card</strong>; add <strong>Calibration &amp; Abstention Card</strong> and <strong>Temporal Validity Card</strong> when the claim leaves same-session.</td>
</tr>
<tr>
<td><strong>EEG source imaging / inverse reconstruction</strong></td>
<td>A single localization score is too weak because validation class, source regime, montage / coverage policy, source depth or extent, and solver disagreement can all change what the result means.</td>
<td><strong>Inverse-Solver Agreement Log</strong> plus named validation class and benchmark-object disclosure.</td>
</tr>
<tr>
<td><strong>Tractography / structural connectome</strong></td>
<td>Hub maps and connectome metrics can shift with acquisition / harmonization, cortical endpoint assignment, graph construction, uncertainty routing, and external calibration; the graph is not one fixed object by default.</td>
<td><strong>Tractography route card</strong>.</td>
</tr>
<tr>
<td><strong>Effective connectivity / DCM</strong></td>
<td>The output still depends on candidate-model family, observed-subsystem closure / latent-confound audit, node-definition policy, sampling / transformation sensitivity, validation, and reliability window.</td>
<td><strong>Effective-connectivity route card</strong>.</td>
</tr>
<tr>
<td><strong>Thermodynamic irreversibility</strong></td>
<td>Different papers compute different quantities from different signal routes, coarse-grainings, and estimator families, so one irreversibility headline does not name one measurement object.</td>
<td><strong>Irreversibility / thermodynamic route card</strong>.</td>
</tr>
<tr>
<td><strong>Multimodal / atlas-prior integration</strong></td>
<td>A synchronized or atlas-informed result can still mix incompatible temporal objects, physiology-linked shared factors, missing-modality slices, and modality-specific disagreements instead of one validated biological quantity.</td>
<td><strong>Fusion Card</strong> with effective-window, shared-vs-specific, quantity-bridge, complete-case, and disagreement disclosure.</td>
</tr>
<tr>
<td><strong>Closed loop / embodied controller</strong></td>
<td>Latency alone does not tell you what was perturbed, which sensory / motor / interoceptive channels were preserved or omitted, or how far the result generalizes across time.</td>
<td><strong>Intervention Card</strong> plus <strong>Body / Environment Boundary Card</strong>; add <strong>Temporal Validity Card</strong> when the claim rises above a same-session demo.</td>
</tr>
<tr>
<td><strong>Living-human proxy bundle</strong></td>
<td>Proxy-rich human evidence can still mix different quantity types, spatial units, timescales, model burdens, role assignments, and disagreement topologies rather than one same-subject state sample.</td>
<td><strong>Human Proxy Composition Card</strong> with role by row, regime compatibility, maturity, calibrator role, and disagreement disclosure.</td>
</tr>
<tr>
<td><strong>Sequential same-subject / same-brain bridge</strong></td>
<td>Specimen identity does not by itself fix state continuity across fixation, deformation, sleep / wake regime, elapsed time, cross-day reacquisition, or adaptation-assisted score rescue.</td>
<td><strong>State-Continuity Bridge Card</strong>, plus <strong>Temporal Validity Card</strong> when the bridge spans hours to days, with carried object, tolerance rule, and rescue-mode disclosure.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-all-needed">
<h2 class="section-title">Why the stack is cumulative</h2>
<table class="data-table">
<thead>
<tr>
<th>If this is missing</th>
<th>The usual failure mode</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No baseline</strong></td>
<td>It becomes unclear whether a gain is meaningful or trivial.</td>
</tr>
<tr>
<td><strong>No benchmark object</strong></td>
<td>Different runs or papers are scored under different hidden rules and still get compared anyway.</td>
</tr>
<tr>
<td><strong>No pre-registration</strong></td>
<td>Success and stopping conditions can drift after the result is known.</td>
</tr>
<tr>
<td><strong>No model card</strong></td>
<td>Only the headline number remains visible while failure modes disappear.</td>
</tr>
<tr>
<td><strong>No companion card matched to the claim</strong></td>
<td>The result is silently promoted above the evidence it actually supports.</td>
</tr>
<tr>
<td><strong>No negative-result record</strong></td>
<td>The same failure gets rediscovered and renamed as if it were new.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="simple-flow">
<h2 class="section-title">View it as a minimal flow</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Put down a baseline</h4>
<p>Start with the minimum comparison partner, even if it is simple.</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Fix the benchmark object</h4>
<p>Align the task, split / randomization rule, task-matched metric bundle, and operational benchmark constraints before comparing systems.</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">03</div>
<div class="stage-body">
<h4>Pre-register success, failure, and abstention</h4>
<p>Decide in advance what counts as passing, stopping, or refusing a stronger claim.</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">04</div>
<div class="stage-body">
<h4>Report the result with the triggered companion cards</h4>
<p>Leave the model card, the Observability Budget, and any extra cards required by the claim shape.</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">05</div>
<div class="stage-body">
<h4>Keep failure examples visible</h4>
<p>Record where the pipeline broke, not only where it happened to work.</p>
</div>
</div>
</div>
</section>

<section class="section" id="negative-results">
<h2 class="section-title">Why failure examples stay in the stack</h2>
<p>
If only successful cases are kept, the field learns a distorted map of where the claim ceiling really is. On this site, a usable failure record states <strong>the condition</strong>, <strong>which metric failed</strong>, <strong>whether the failure came from leakage, OOD shift, compute limits, bridge failure, or fusion mismatch</strong>, and <strong>what stronger claim therefore remains blocked</strong>.
</p>
<div class="note-box">
<strong>Minimum failure record</strong>
<p>
State the data regime, split rule, metric bundle, triggered cards, and the first place the claim lost support. A vague sentence such as <strong>it did not generalize</strong> is weaker than a report that says <strong>cross-site transfer collapsed after harmonization changed, false alarms doubled, and the Specificity &amp; Shortcut Card stayed unresolved</strong>.
</p>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">Minimum checks when reading public pages</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>Is there a baseline?</strong> Is it clear what the new result is compared against?</li>
<li><strong>Is the benchmark object fixed?</strong> Are the task, split / randomization rule, metric bundle, version, and governance visible?</li>
<li><strong>Is there a pre-registration?</strong> Are success, failure, stopping, and abstention rules stated before the run?</li>
<li><strong>Is there a model card plus Observability Budget?</strong> Are scores, weaknesses, failure examples, direct observables, latent state, and claim ceiling visible?</li>
<li><strong>If it is a decode / biomarker / transfer result, is a Specificity &amp; Shortcut Card visible?</strong> Are subject, session, site, device, and protocol shortcuts audited separately?</li>
<li><strong>If it emits text or speech, is a Neural Contribution Card visible?</strong> Are candidate set, language-model or prompt scaffold, no-brain / no-LM controls, and subject cooperation disclosed?</li>
<li><strong>If it is a foundation / self-supervised EEG result, is a Pretraining Card visible?</strong> Are corpus overlap, harmonization, adaptation regime, benchmark version, and inference-stage restrictions written?</li>
<li><strong>If it is an ESI, tractography, effective-connectivity, or thermodynamic claim, is the route-specific card or log visible?</strong> Are validation class / graph object / closure / estimator-family details written rather than hidden in one headline?</li>
<li><strong>If it is multimodal or atlas-prior, is a Fusion Card visible?</strong> Are acquisition relation, effective-window / temporal-kernel relation, shared-vs-specific disclosure, quantity bridge, complete-case or missing-modality policy, and external calibration written?</li>
<li><strong>If it is a closed-loop or intervention result, is an Intervention Card visible, and if embodiment matters is a Body / Environment Boundary Card visible?</strong> Are trigger rule, timing audit, preserved loop channels, and slow-boundary omissions disclosed?</li>
<li><strong>If several living-human proxy rows are used together, is a Human Proxy Composition Card visible?</strong> Are proxy class, direct observable and role by row, regime compatibility, maturity / calibrator role, disagreement topology, and increment over the strongest single row disclosed?</li>
<li><strong>If the claim bridges same-subject or same-brain measurements across regimes, is a State-Continuity Bridge Card visible?</strong> Are carried object, tolerance / failure rule, rescue route, elapsed time, regime continuity, deformation / registration burden, and bridge-validation rung written?</li>
<li><strong>If the claim rises across hours to days or reports confidence / abstention, are Temporal Validity and Calibration &amp; Abstention Cards visible?</strong> Are recalibration burden, transfer ceiling, fit/calibration/test separation, and fallback behavior written?</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Saito, T., &amp; Rehmsmeier, M. (2015). The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets. <a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">doi:10.1371/journal.pone.0118432</a></li>
<li>Roy, Y., Banville, H., Albuquerque, I., et al. (2021). Deep learning-based electroencephalography analysis: a systematic review. <a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">doi:10.1016/j.ebiom.2021.103275</a></li>
<li>Sun, H., Paixao, L., Oliva, J. T., et al. (2017). Brain age from the electroencephalogram of sleep. <a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">doi:10.1093/sleep/zsx139</a></li>
<li>Vallat, R., &amp; Walker, M. P. (2021). An open-source, high-performance tool for automated sleep staging. <a href="https://doi.org/10.7554/eLife.70092" target="_blank">doi:10.7554/eLife.70092</a></li>
<li>Chaibub Neto, E., Pratap, A., Perumal, T. M., et al. (2019). Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu, M., Yao, S., Wei, Z., et al. (2020). Cross-dataset variability problem in EEG decoding with deep learning. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Di, Y., An, X., Zhong, W., Liu, S., &amp; Ming, D. (2021). The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>EEG Challenge (2025) homepage. <a href="https://eeg2025.github.io/" target="_blank">official site</a></li>
<li>EEG Challenge (2025) rules. <a href="https://eeg2025.github.io/rules/" target="_blank">official rules</a></li>
<li>EEG Challenge (2025) starter kit. <a href="https://eeg2025.github.io/baseline/" target="_blank">official starter kit page</a></li>
<li>EEG Challenge (2025) leaderboard and organizer postmortem. <a href="https://eeg2025.github.io/leaderboard/" target="_blank">official leaderboard</a></li>
<li>Xiong, W., Li, J., Li, J., Zhu, K., &amp; Jiang, C. (2025/2026). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>Liu, D., Chen, Y., Chen, Z., Cui, Z., Wen, Y., An, J., Luo, J., &amp; Wu, D. (2026). EEG Foundation Models: Progresses, Benchmarking, and Open Problems. <a href="https://arxiv.org/abs/2601.17883" target="_blank">arXiv:2601.17883</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H., Jafarian, A., Zeidman, P., et al. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Gregoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Johansen, A., Beliveau, V., Colliander, E., et al. (2024). An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., et al. (2024). Myelin bilayer mapping in the human brain in vivo. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Hirschler, L., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Bosch, C., Ackels, T., Pacureanu, A., et al. (2022). Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>MICrONS Consortium, Bae, J. A., Lee, W.-C. A., et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Attardo, A., Fitzgerald, J. E., &amp; Schnitzer, M. J. (2015). Impermanence of dendritic spines in live adult CA1 hippocampus. <a href="https://doi.org/10.1038/nature14467" target="_blank">doi:10.1038/nature14467</a></li>
<li>Tang, J., LeBel, A., Jain, S., &amp; Huth, A. G. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. <em>Nature Neuroscience</em>, 26, 858-866. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Défossez, A., Caucheteux, C., Rapin, J., Kabeli, O., &amp; King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. <em>Nature Machine Intelligence</em>, 5, 1097-1107. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">doi:10.1038/s42256-023-00714-5</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., Banville, H., Benchetrit, Y., Pallier, C., &amp; King, J.-R. (2025). Towards decoding individual words from non-invasive brain recordings. <em>Nature Communications</em>, 16, 10521. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., Hochberg, L. R., Brandman, D. M., &amp; Stavisky, S. D. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644(8075), 145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Horrillo-Maysonnial, A., Avigdor, T., Abdallah, C., et al. (2023). Targeted density electrode placement achieves high concordance with traditional high-density EEG for electrical source imaging in epilepsy. <em>Clinical Neurophysiology</em>, 156, 262-271. <a href="https://doi.org/10.1016/j.clinph.2023.08.009" target="_blank">doi:10.1016/j.clinph.2023.08.009</a></li>
<li>Rong, J., Sun, R., Joseph, B., Worrell, G., &amp; He, B. (2025). Deep learning-based EEG source imaging is robust under varying electrode configurations. <em>Clinical Neurophysiology</em>, 175, 2010730. <a href="https://doi.org/10.1016/j.clinph.2025.04.009" target="_blank">doi:10.1016/j.clinph.2025.04.009</a></li>
<li>Unnwongse, K., Van Klink, N., Tousseyn, S., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation. <em>Brain Communications</em>, 5(1), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Pascarella, A., Mikulan, E., Sciacchitano, F., et al. (2023). An in-vivo validation of ESI methods with focal sources. <em>NeuroImage</em>, 277, 120219. <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">doi:10.1016/j.neuroimage.2023.120219</a></li>
<li>Feng, Z., Guan, C., &amp; Sun, Y. (2025). Block-Champagne: A novel Bayesian framework for imaging extended E/MEG source. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Gajwani, M., Oldham, S., Pang, J. C., Arnatkevičiūtė, A., Tiego, J., Bellgrove, M. A., &amp; Fornito, A. (2023). Can hubs of the human connectome be identified consistently with diffusion MRI? <em>Network Neuroscience</em>, 7(4), 1277-1304. <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">doi:10.1162/netn_a_00324</a></li>
<li>He, Y., Hong, Y., Wu, Y., et al. (2024). Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. <em>NeuroImage</em>, 297, 120904. <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">doi:10.1016/j.neuroimage.2024.120904</a></li>
<li>McMaster, E. M., Newlin, N. R., Rudravaram, G., et al. (2025). Harmonized connectome resampling for variance in voxel sizes. <em>Magnetic Resonance Imaging</em>, 122, 110424. <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">doi:10.1016/j.mri.2025.110424</a></li>
<li>Bramati, I. B., Szczupak, D., Carneiro Monteiro, M., Meireles, F., Menezes Guimarães, D., Dean, R. J., Paul, L. K., &amp; Tovar-Moll, F. (2026). Diffusion MRI sampling schemes bias diffusion metrics and tractography. <em>Frontiers in Neuroimaging</em>, 5, 1670604. <a href="https://doi.org/10.3389/fnimg.2026.1670604" target="_blank">doi:10.3389/fnimg.2026.1670604</a></li>
<li>Manzano-Patrón, J. P., Deistler, M., Schröder, C., et al. (2025). Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. <em>Medical Image Analysis</em>, 103, 103580. <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">doi:10.1016/j.media.2025.103580</a></li>
<li>Zhu, S., Huszar, I. N., Cottaar, M., et al. (2025). Imaging the structural connectome with hybrid MRI-microscopy tractography. <em>Medical Image Analysis</em>, 102, 103498. <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">doi:10.1016/j.media.2025.103498</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <em>Journal of Neuroscience Methods</em>, 208(1), 66-78. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Smith, S. M., Miller, K. L., Salimi-Khorshidi, G., Webster, M., Beckmann, C. F., Nichols, T. E., Ramsey, J. D., &amp; Woolrich, M. W. (2011). Network modelling methods for FMRI. <em>NeuroImage</em>, 54(2), 875-891. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">doi:10.1016/j.neuroimage.2010.08.063</a></li>
<li>Barnett, L., &amp; Seth, A. K. (2017). Detectability of Granger causality for subsampled continuous-time neurophysiological processes. <em>Journal of Neuroscience Methods</em>, 275, 93-121. <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">doi:10.1016/j.jneumeth.2016.10.016</a></li>
<li>Vink, J. J. T., Klooster, D. C. W., Ozdemir, R. A., Westover, M. B., Pascual-Leone, A., &amp; Shafi, M. M. (2020). EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. <em>Brain Topography</em>, 33(2), 221-237. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>Villaverde, A. F., Tsiantis, N., &amp; Banga, J. R. (2019). Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. <em>Journal of the Royal Society Interface</em>, 16(156), 20190043. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Novelli, L., Barnett, L., Seth, A. K., &amp; Razi, A. (2025). Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. <em>Human Brain Mapping</em>, 46(10), e70285. <a href="https://doi.org/10.1002/hbm.70285" target="_blank">doi:10.1002/hbm.70285</a></li>
<li>Jafarian, A., Karadag Assem, M., Kocagoncu, E., et al. (2024). Reliability of dynamic causal modelling of resting-state magnetoencephalography. <em>Human Brain Mapping</em>, 45(10), e26782. <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Yan, J., Zhang, S.-W., Zhang, C., Huang, W., Shi, J., &amp; Chen, L. (2026). Dynamical Causality under Latent Confounders for Biological Network Reconstruction. <em>IEEE Transactions on Pattern Analysis and Machine Intelligence</em>. <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">doi:10.1109/TPAMI.2026.3658839</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., et al. (2021). Broken detailed balance and entropy production in the human brain. <em>PNAS</em>, 118(47), e2109889118. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Egger, A., Bayon, C., d'Almeida, J., et al. (2024). Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Scientific Reports</em>, 14, 20247. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Idziak, A., Inavalli, V. V. G. K., Bancelin, S., Arizono, M., &amp; Nagerl, U. V. (2023). The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. <em>eNeuro</em>. <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">doi:10.1523/ENEURO.0104-23.2023</a></li>
<li>Benisty, H., Barson, D., Moberly, A. H., et al. (2024). Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go next</h2>
<p>
Return to <a href="../verification.html">Verification</a> for the authoritative card fields, to <a href="../datasets.html#l0-practice">Datasets / L0 Practice</a> for hands-on implementation, or to <a href="../verification.html#casework">Verification Casework</a> for cross-domain precedents.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">Verification Basics -></a></li>
<li><a href="dataset-splits-and-leakage.html">Dataset Splits and Leakage -></a></li>
<li><a href="eeg-foundation-models.html">EEG Foundation Models -></a></li>
<li><a href="observation-to-estimation.html">From Observation To Estimation -></a></li>
<li><a href="uncertainty-confidence-and-abstention.html">Uncertainty, Calibration, and Abstention -></a></li>
<li><a href="thermodynamic-grounding-basics.html">Thermodynamic Grounding Basics -></a></li>
<li><a href="closed-loop-latency-jitter-and-safety-stops.html">Closed Loops, Latency, Jitter, and Safety Stops -></a></li>
<li><a href="human-proxy-composition.html">Human Proxy Composition -></a></li>
<li><a href="state-continuity-bridge.html">State-Continuity Bridge -></a></li>
</ul>
</div>
</aside>
</main>
