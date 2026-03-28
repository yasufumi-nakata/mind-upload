---
layout: default
title: 'Wiki: From observation to estimation'
description: We organize forward problems, inverse problems, ESI, DCM, SCM, and causal
  equivalence classes, including observability budget, identifiability, bridge/composition
  validity, and external validation.
article_type: Wiki
subtitle: Being consistent with observation, understanding internal states, and understanding
  cause and effect are different things.
author: Mind Uploading Research Project
last_updated: '2026-03-29'
note: Technical / natural science only
audience: People who want to organize inverse problems and the limitations of causal
  models based on primary literature
reading_time: 12-18 minutes
page_intro: This page is a wiki that organizes where to stop making claims and what
  to add to make them even stronger when estimating brain states and causal structures
  from observational signals such as EEG. Connect forward problems, inverse problems,
  ESI, DCM, SCM, and causal equivalence classes in the order of ``observation → estimation
  → intervention → validation.''
accuracy_note: This is not a fixed recipe for which method to use. This page first
  fixes audit items that cannot be avoided no matter what method you use.
page_highlights:
- Inverse problems are not evaluated solely by the solver name, but are also audited
  for geometry, conductivity, uncertainty, and external validation.
- For ESI, cross-solver / cross-parameter disagreement is itself evidence about uncertainty,
  so one best map is not accepted here as the whole answer.
- This page now separates observability, structural identifiability, and practical
  identifiability so richer measurements are not overread as uniqueness.
- "Different ambiguity classes need different remedies: symmetry-breaking observables, regime design, model-discrepancy stress tests, and task-interaction perturbations are not interchangeable."
- Same-session multimodal acquisition, same-brain sequential linkage, and connectome
  constraints do not collapse the candidate set by themselves; fusion, bridge, and
  conditional-model audits remain separate gates.
- DCM is a candidate model comparison rather than an automatic detector, and SCM is
  a language that facilitates describing interventions.
- Effective-connectivity claims now use a route card that names candidate model space,
  observed-subsystem closure / latent-confound audit, node-definition policy, sampling
  / transformation sensitivity, observation assumptions, validation, reliability,
  and abstention before the claim ceiling is raised.
- The key is to what extent we can narrow down the causal equivalence classes that
  remain based on observational data alone through intervention and calibration.
known_points:
- In principle, it is difficult to uniquely determine brain activity from scalp EEG,
  and estimation requires assumptions.
- High-density EEG, individualized MRI, FEM/BEM, and empirical Bayesian estimation
  can improve conditions, but alone do not guarantee unique recovery.
- More direct observables do not by themselves guarantee unique recovery; degeneracy
  can persist unless candidate space, recorded subset, and experiment design are
  exposed.
- Ambiguity is not one scalar; symmetry / reparameterization, narrow-regime degeneracy,
  omitted-mechanism discrepancy, and representation ambiguity require different
  fixes.
- Simultaneous multimodal acquisition can still retain shared and modality-specific
  structure, so a richer stack does not by itself define one validated latent target.
- For ESI, method/package/parameter choice can materially move the estimated source,
  so stability across standard pipelines is part of the claim.
- In effective connectivity, hidden nodes/common drives, node-definition choices,
  and sampling or observation transforms are separate failure modes; a winning model
  comparison does not erase them.
- Same-brain or same-subject linkage can still be a sequential bridge rather than
  same-state evidence.
- The causal structure cannot be determined by observational fit alone; a set of candidate
  models and an intervention design are required.
- Whole-brain or faster DCM improves tractability, but does not erase candidate-model
  dependence or observation-model assumptions.
unknown_points:
- It remains unclear which measurement/modeling combination is most effective for
  validating WBE.
- Research is currently underway to determine how detailed the causal structure and
  state variables can be stably restored using non-invasive measurements alone.
- How much same-session multimodal fusion, sequential same-brain linkage, and connectome-constrained
  prediction can jointly narrow the candidate set without recreating hidden-state
  ambiguity remains unresolved.
- Which external validation ladders will be pinned to the site-wide benchmark is still
  being worked out.
wiki_links:
- label: 'Wiki: From measurement to modeling'
  url: /wiki/measurement-and-modeling-terms.html
  description: You can return to the overall map of measurement, organization, estimation,
    and verification.
- label: 'Wiki: EEG pretreatment and QC'
  url: /wiki/eeg-preprocessing-and-qc.html
  description: In the first stage of estimation, we compensate for what changes the
    results.
- label: 'Wiki: Uncertainty, proofreading, abstaining'
  url: /wiki/uncertainty-confidence-and-abstention.html
  description: Instead of point estimation, we supplement the width and how to leave
    conditions for abstention.
- label: 'Wiki: Observability and claim ceiling by measurement stack'
  url: /wiki/measurement-stack-and-claim-ceiling.html
  description: Use this when you first need to separate direct observables from latent
    state families before asking identifiability questions.
- label: 'Wiki: Multimodal integration basics'
  url: /wiki/multimodal-integration-basics.html
  description: Use this when richer stacks could otherwise be misread as self-validating
    fusion.
- label: 'Wiki: State-Continuity Bridge'
  url: /wiki/state-continuity-bridge.html
  description: Use this when same-subject or same-brain linkage is sequential across
    live, fixed, or cross-day stages.
- label: 'Wiki: Counterfactuals/Interventions/Perturbations'
  url: /wiki/counterfactual-and-perturbation-verification.html
  description: It supplements the conditions for proceeding from observational adaptation
    to intervention validation.
recommended_pages:
- label: Introduction to EEG
  url: /eeg_101.html
- label: Verification platform
  url: /verification.html
- label: technology roadmap
  url: /tech_roadmap.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Conclusion</h2>
<p>
Even if a model that matches the observed signal is found, it cannot be said that the internal state has been uniquely determined or that the causal structure has been identified. Therefore, on this site, we now audit six points, <strong>geometry</strong>, <strong>observability budget</strong>, <strong>uncertainty</strong>, <strong>candidate model set</strong>, <strong>bridge / composition validity</strong>, and <strong>external validation</strong>, before looking at the solver name or theory name.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. We will organize the boundaries between observation, estimation, and causal claims based on primary literature from only the aspects of technology and natural science.
</p>
</div>

<section class="section" id="audit-gates">
<h2 class="section-title">Six audit gates to be fixed first</h2>
<table class="data-table">
<thead>
<tr>
<th>Audit gate</th>
<th>What I want at least</th>
<th>Claim that it stops when there is not enough</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1: Geometry and forward model</strong></td>
<td>Electrode coordinates, head model, conductivity assumption, presence or absence of individual MRI, sensitivity analysis. </td>
<td>I cannot make strong anatomical source claims. </td>
</tr>
<tr>
<td><strong>Gate 2: Observability budget</strong></td>
<td>Named measurement stack, direct observable, what remained latent, and the strongest stack-specific ceiling. </td>
<td>``More channels / modalities / same-brain registration'' cannot be rephrased as ``the target internal state was now directly seen.'' </td>
</tr>
<tr>
<td><strong>Gate 3: Visualizing uncertainty</strong></td>
<td>Posterior distribution, confidence interval, bootstrap/ensemble width, or solver/preprocessing sensitivity analysis. </td>
<td>It is not possible to write it as the only solution using only point estimation. </td>
</tr>
<tr>
<td><strong>Gate 4: Specifying candidate model set</strong></td>
<td>Compared model spaces, family comparisons, remaining equivalence classes, abstention conditions. </td>
<td>Even if we use DCM or SCM, we cannot say that we have uniquely discovered cause and effect. </td>
</tr>
<tr>
<td><strong>Gate 5: Bridge / composition validity</strong></td>
<td>Same-session relation, acquisition order, elapsed time, regime continuity, fusion model, shared-vs-specific disclosure, strongest-single-row gain, and bridge-validation rung. </td>
<td>``same-subject cross-stack'' or ``same-brain sequential'' cannot be rephrased as fused ground truth or same-state evidence. </td>
</tr>
<tr>
<td><strong>Gate 6: External validation/intervention</strong></td>
<td>Named validation classes such as simulation, phantom, simultaneous invasive recording, intracranial stimulation, postsurgical outcome, and held-out prediction of stimulus/lesion/task perturbations. </td>
<td> Observed fit cannot be promoted to causal validity or generalization performance. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="three-layers">
<h2 class="section-title">Keep three layers separate: observability, structural identifiability, practical identifiability</h2>
<p>
One remaining weakness in inverse-problem discussions is to let <strong>"more measured signals"</strong> sound too close to <strong>"the internal state is now uniquely known"</strong>. The systems-identification literature does not support that shortcut. <a href="https://doi.org/10.1155/2019/8497093" target="_blank">Villaverde (2019)</a> reviews that observability and structural identifiability are related but different questions, and <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde et al. (2019)</a> show that unknown inputs, states, and parameters often have to be analysed jointly rather than one at a time.
</p>
<table class="data-table">
<thead>
<tr>
<th>Layer</th>
<th>Question</th>
<th>What can still fail even if this layer looks good</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observability</strong></td>
<td>Does the chosen output route contain information about the target state at all?</td>
<td>You may still have multiple different internal states or parameter sets that generate the same observable pattern.</td>
</tr>
<tr>
<td><strong>Structural identifiability</strong></td>
<td>Given the declared equations and ideal noise-free data, is the target uniquely recoverable up to named symmetries or reparameterizations?</td>
<td>The real dataset may still be too short, too noisy, too sparse, or too weakly excited to recover that target in practice.</td>
</tr>
<tr>
<td><strong>Practical identifiability</strong></td>
<td>Under the actual finite data, SNR, sampling window, and perturbation design, does the compatible solution set become narrow enough to support the stated claim?</td>
<td>A theoretically identifiable model can still remain numerically or experimentally degenerate.</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>2026-03-20 deepening: similar outputs do not prove similar internal states</strong>
<p>
This separation is not only a control-theory point. <a href="https://doi.org/10.1038/nn1352" target="_blank">Prinz et al. (2004)</a> showed that similar circuit activity can arise from disparate parameters, <a href="https://doi.org/10.1162/netn_a_00354" target="_blank">Rasero et al. (2024)</a> showed that similar human activation patterns can still hide different macroscopic network states, and <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that even connectome-constrained recurrent networks remain degenerate until additional recordings are supplied. <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">Liu et al. (2025)</a> then showed that practical identifiability depends on data-collection policy, not only on the fitting method. On this site, that means <strong>observability</strong> and <strong>identifiability</strong> are audited separately.
</p>
</div>

<section class="section" id="ambiguity-classes">
<h2 class="section-title">Name the ambiguity class before saying more data will help</h2>
<p>
One remaining weakness was to describe all non-uniqueness as if it were one scalar problem of simply needing <strong>more data</strong>. The primary literature does not support that shortcut. <a href="https://doi.org/10.3390/sym12030469" target="_blank">Massonis &amp; Villaverde (2020)</a> showed that structural unidentifiability can come from <strong>symmetry</strong> and may require symmetry-breaking observables or reformulation. <a href="https://doi.org/10.1038/nn1352" target="_blank">Prinz et al. (2004)</a> and <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that different parameters can still generate near-equivalent dynamics even when connectivity is fixed. <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">White et al. (2016)</a> showed that complementary experiments can mainly expose <strong>omitted mechanisms</strong> rather than identify the intended parameters. <a href="https://doi.org/10.1038/s41593-025-01869-7" target="_blank">Langdon &amp; Engel (2025)</a> showed that preserving <strong>causal interactions among task variables</strong> can recover behaviorally relevant computations that correlation-only reductions miss. On this site, a stronger protocol therefore has to name <strong>which ambiguity class</strong> survives first.
</p>
<table class="data-table">
<thead>
<tr>
<th>Ambiguity class</th>
<th>How it fools the reader</th>
<th>What would actually raise the claim ceiling</th>
<th>What this site still refuses to count</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Symmetry / reparameterization ambiguity</strong></td>
<td>Several parameter or state transformations produce the same declared outputs, so a good fit looks unique when it is not.</td>
<td>Add a symmetry-breaking observable, a known input / initial condition, or a reformulation that removes the hidden transformation.</td>
<td>More fitting time, more random restarts, or more repeats of the same uninformative protocol.</td>
</tr>
<tr>
<td><strong>Regime-restricted degeneracy</strong></td>
<td>Different internal states or parameter sets agree inside one narrow operating regime and only diverge outside it.</td>
<td>Use state transitions, persistent excitation, targeted recordings, or perturbation contrasts that make the surviving candidates separate.</td>
<td>More passive samples from the same regime when the alternatives remain co-linear.</td>
</tr>
<tr>
<td><strong>Model-family / omitted-mechanism ambiguity</strong></td>
<td>An approximate model appears well identified until a complementary condition reveals systematic residuals or missing mechanisms.</td>
<td>Run a discrepancy stress test, compare richer / alternative model families, and require held-out falsification rather than post hoc explanation.</td>
<td>Narrower intervals inside one misspecified family or one headline accuracy gain.</td>
</tr>
<tr>
<td><strong>Task-variable interaction / representation ambiguity</strong></td>
<td>A latent factor or reduced representation predicts correlations but misses the interaction structure that actually drives behavior.</td>
<td>Preserve or perturb the task-variable interaction, and compare the intervention-side predictions of the competing representations.</td>
<td>Correlation-only dimensionality reduction, generic multimodal fusion, or interpretability language without perturbation.</td>
</tr>
</tbody>
</table>
<p>
If the apparent ambiguity mainly comes from shared modality drivers or physiology-linked common factors, this site routes the claim to the <a href="../verification.html#fusion-card">Fusion Card</a> instead of calling it solved identification.
</p>
</section>

<section class="section" id="conditioning-is-not-closure">
<h2 class="section-title">Richer conditioning is not candidate-set closure</h2>
<p>
One remaining weakness was to let a richer setup sound too close to a closed candidate set. The recent primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed that simultaneous multimodal recordings retain both common and divergent structure. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed in simultaneous EEG-PET-MRI that tightly coupled temporal progression can coexist with distinct network patterns across wakefulness and NREM sleep. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that preservation route changes extracellular-space retention, and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> explicitly describe a sequential in vivo-to-postmortem workflow rather than one simultaneous state sample. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> then showed that within-day EEG dynamics drift enough to motivate adaptive decoders. Therefore, on this site, richer conditioning is split into three separate audits instead of being read as one generic march toward uniqueness.
</p>
<table class="data-table">
<thead>
<tr>
<th>What got richer</th>
<th>What the primary literature really strengthened</th>
<th>What it still does not support</th>
<th>Card or rule required on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Same-session multimodal acquisition</strong></td>
<td>Shared clock, cross-modal comparison, and a bounded decomposition of common versus modality-specific structure.</td>
<td>One validated latent state, self-validating fusion, or state-complete measurement.</td>
<td><strong>Fusion Card</strong> plus the stack-specific <strong>Observability Budget</strong>.</td>
</tr>
<tr>
<td><strong>Same-brain or same-subject sequential linkage</strong></td>
<td>Specimen linkage, local correlative workflow, or repeated-acquisition design with named bridge burden.</td>
<td>Same-state evidence across live-to-fix transformation, cross-day drift, or separated physiological regimes.</td>
<td><strong>State-Continuity Bridge Card</strong>, and <strong>Temporal Validity Card</strong> when live drift across hours or days matters.</td>
</tr>
<tr>
<td><strong>Connectome-constrained prediction</strong></td>
<td>A narrower conditional model family under a declared structural prior and recorded subset.</td>
<td>Unique dynamics, solved omitted-mechanism risk, or in-principle internal-state recovery.</td>
<td><strong>Connectome-Constrained Model Card</strong> together with the <strong>Identifiability Card</strong>.</td>
</tr>
</tbody>
</table>
<p>
If these cards are missing, the ceiling stays at the strongest directly supported route: the strongest unimodal or prior-conditioned stack, the strongest directly supported bridge stage, or a conditional-model predictor rather than unique recovery.
</p>
</section>

<section class="section" id="levels">
<h2 class="section-title">Do not mix observation, estimation, and causal verification</h2>
<table class="data-table">
<thead>
<tr>
<th>stage</th>
<th>What we're doing here</th>
<th>Things that cannot be said at this stage yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observation</strong></td>
<td>Measures signals visible on the scalp and outside. </td>
<td>It cannot be said that the brain state has been uniquely restored. </td>
</tr>
<tr>
<td><strong>Estimation</strong></td>
<td>Place a head model or generative model to infer activity sources and connections. </td>
<td>It cannot be said that it is true even outside the candidate model. </td>
</tr>
<tr>
<td><strong>Intervention/validation</strong></td>
<td>Calibrate predictions with stimuli, lesions, task changes, intracranial stimulation, and concurrent invasive recordings. </td>
<td>Even with this, the branch-equivalence of whole-brain WBE cannot be said. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="forward-inverse">
<h2 class="section-title">Forward and inverse problems</h2>
<table class="data-table">
<thead>
<tr>
<th>Term</th>
<th>Meaning</th>
<th>Effective points in auditing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Order questions</strong></td>
<td>If there is this activity in the brain, calculate what it looks like in the scalp. </td>
<td>Head model, conductivity, and electrode placement assumptions come to the fore. </td>
</tr>
<tr>
<td><strong>Inverse problem</strong></td>
<td>We estimate the brain activity that can explain the signals seen on the scalp. </td>
<td>Uncertainty and sensitivity analysis is essential because multiple solutions can produce the same observation. </td>
</tr>
</tbody>
</table>
<p>
The inverse problem is difficult because<strong>multiple internal states can produce the same observation</strong>. Therefore, the important thing here is not to strongly insist on the "best one point" but to reveal what assumptions made and how far the results were narrowed down.
</p>
</section>

<section class="section" id="esi">
<h2 class="section-title">Read ESI in the validation ladder first, rather than the solver name</h2>
<p>
ESI is a framework for estimating source from scalp signals. However, as shown by direct validation studies by Mikulan et al. and Unnwongse et al., the error varies greatly depending on source depth, cranial conductivity, head model, electrode geometry, solver family, and implementation choice. Therefore, it is not possible to make a strong argument just by saying<strong>Because it is a high-density EEG or because it is a Bayesian solver</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Check with ESI first</th>
<th>Why is it important</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Geometry</strong></td>
<td>The source error will change if the electrode position, individual MRI, FEM/BEM, and conductivity assumptions are different. </td>
</tr>
<tr>
<td><strong>Uncertainty</strong></td>
<td>Empirical Bayes and ensemble are powerful, but what is essential is visualization of the width, not the solver name. </td>
</tr>
<tr>
<td><strong>Cross-solver stability</strong></td>
<td>If WMNE / eLORETA / beamformer / Bayesian families or reasonable parameter windows disagree materially, the spread itself has to be reported. </td>
</tr>
<tr>
<td><strong>Withholding deep/micro sources</strong></td>
<td>Detectable and general reconstruction are different, and deep generalization requires a suspension condition. </td>
</tr>
<tr>
<td><strong>External validation</strong></td>
<td>It is necessary to know which validation class was used and where the simulation, phantom, simultaneous invasive recording, intracranial stimulation, or postsurgical outcome was calibrated. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Replacement on this site</strong>
<p>
Bayesian / empirical Bayes / sparse Bayesian learning is a good candidate for<strong>estimation with uncertainty</strong>. However, on this site, rather than ``accepting a proposal because it is Bayesian'', the criteria for acceptance or rejection are <strong>how uncertainty is disclosed and what external standards were used for calibration</strong>.
</p>
</div>
<div class="note-box">
<strong>2026-03-19 deepening: one best map is not the same as a stable solution</strong>
<p>
The weak point here was to separate solver name from audit items, but still leave room for a reader to overtrust one polished map. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.076" target="_blank">Mahjoory et al. (2017)</a> showed that inverse-method and software-package choice induces considerable variability and explicitly encouraged verifying results with more than one source-imaging procedure. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a> then showed on intracranial-stimulation ground truth that only a small fraction of tested solutions reached the session-wise optimum. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> further showed that skull/skin conductivity uncertainty can move reconstructed depth and localization. Therefore, on this site, one best inverse map is read only as a <strong>candidate solution</strong> unless the paper also exposes <strong>cross-solver / cross-parameter spread</strong> or a <strong>posterior / ensemble width</strong>.
</p>
</div>
</section>

<section class="section" id="dcm">
<h2 class="section-title">DCM is not "a device that automatically discovers true cause and effect"</h2>
<p>
DCM is a framework that specifies candidate generative models and compares them to see which one is easier to explain observations. As shown in Friston et al.'s original paper and Penny et al.'s model comparison study, DCM conclusions depend on the candidate model space entered into the comparison. Therefore, winning in a model comparison means that it is ``good among the candidate set'' and does not mean that it is<strong>the only correct one in</strong>the world.
</p>
<div class="key-points">
<h4>Four points when reading DCM</h4>
<ul>
<li><strong>Candidate model space:</strong> Which nodes and join candidates were initially included in the comparison. </li>
<li><strong>Family comparison:</strong>Is the upper family stable, not the details? </li>
<li><strong>model recovery:</strong>Can the correct model be recovered through simulation? </li>
<li><strong>Intervention Calibration:</strong>Is the held-out prediction correct with the stimulus or perturbation? </li>
</ul>
</div>
</section>

<div class="note-box">
<strong>2026-03-19 deepening: why this page now needs a route card</strong>
<p>
The weak point here was not that it separated DCM from SCM, but that scaling advances could still be overread as if they had solved identifiability. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">Rosa et al. (2012)</a> showed that DCM can search a potentially huge model space quickly from one full model, <a href="https://doi.org/10.1002/hbm.23061" target="_blank">Frässle et al. (2016)</a> showed that reliability itself must be checked rather than assumed, <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">Frässle et al. (2021)</a> pushed directed-connectivity estimation to whole-brain human fMRI, and <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Wu et al. (2024)</a> reduced computation time further. Those are real advances in tractability, but they still operate inside explicit choices about node set, priors, hemodynamics, and omitted competitors. Therefore, on this site, scaling is read as <strong>better searchability of candidate models</strong>, not as automatic causal discovery.
</p>
</div>

<div class="note-box">
<strong>2026-03-29 deepening: directed graphs still fail under partial observation, node policy, and sampling transforms</strong>
<p>
The remaining weakness after adding a route card was that <strong>candidate model space</strong> could still be read too narrowly, as if it already covered the practically important failure modes of a directed graph. The primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a> showed in a large simulation benchmark that lag-based approaches perform poorly for fMRI and that <strong>functionally inaccurate ROIs</strong> are especially damaging to network estimation. <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">Barnett &amp; Seth (2017)</a> then showed that subsampling can create <strong>detectability black spots</strong> for Granger-causal interactions rather than a simple monotonic loss. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">Vink et al. (2020)</a> showed in TMS-EEG that resting-state EEG functional connectivity explains <strong>less than 10% of the variance</strong> in evoked propagation and varies substantially across stimulation sites and participants. <a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025)</a> refined the hemodynamic objection: if the HRF is minimum-phase, HRF variability alone need not create false positives across a wide range of plausible parameters, but <strong>slow BOLD sampling</strong> can still induce spurious Granger-causal inference. Most recently, <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">Yan et al. (2026)</a> showed that dynamical causal inference under <strong>latent confounders</strong> remains an active method-development problem in biological network reconstruction. Therefore, on this site, effective-connectivity claims must now separate <strong>observed-subsystem closure / latent-confound audit</strong>, <strong>node-definition policy</strong>, and <strong>sampling / transformation sensitivity</strong> from the older questions of model comparison and external validation.
</p>
</div>

<section class="section" id="effective-connectivity-route-card">
<h2 class="section-title">Effective-connectivity route card</h2>
<table class="data-table">
<thead>
<tr>
<th>Route-card field</th>
<th>What must be written</th>
<th>What misreading it blocks</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Candidate model space</strong></td>
<td>Compared node set, omitted nodes / edges, exogenous inputs, and the family of alternatives that were allowed to compete.</td>
<td>It blocks “the best compared model” from being rephrased as “the true circuit was found.”</td>
</tr>
<tr>
<td><strong>Observed subsystem / latent-confound audit</strong></td>
<td>Name which candidate hidden nodes, common drives, instantaneous interactions, or unmeasured exogenous inputs remain outside the observed subsystem, what sensitivity analysis or latent-confound method was used, and whether the reported directions survive that audit.</td>
<td>It blocks a partial recording or atlas-defined subgraph from sounding like a causally closed system.</td>
</tr>
<tr>
<td><strong>Node-definition policy</strong></td>
<td>State how ROIs or nodes were defined, whether alternative parcellations / functional localizers / decompositions were tested, and whether edge directions or family ranking change materially across those alternatives.</td>
<td>It blocks one directed graph from sounding node-invariant when the result actually depends on the chosen parcellation or ROI recipe.</td>
</tr>
<tr>
<td><strong>Observation model and priors</strong></td>
<td>Neural-mass assumptions, linearization, HRF choice, mean-field or independence assumptions, sparsity priors, and any structural constraints.</td>
<td>It blocks “effective connectivity” from sounding as if the result were independent of hemodynamic and prior assumptions.</td>
</tr>
<tr>
<td><strong>Sampling / transformation sensitivity</strong></td>
<td>State the sampling interval relative to the neural delays of interest, filtering or deconvolution choices, HRF / observation-transform assumptions, and whether inferred directions survive plausible transform alternatives or only one time-resolution regime.</td>
<td>It blocks directed-lag estimates from sounding biologically directional when they may still be shaped by sampling, filtering, or observation transforms.</td>
</tr>
<tr>
<td><strong>Family comparison / model recovery</strong></td>
<td>Family-level stability, simulation-based recovery, and whether nearby model families are confusable under the same data regime.</td>
<td>It blocks fragile one-model wins from being promoted to robust identifiability.</td>
</tr>
<tr>
<td><strong>Perturbation or external validation</strong></td>
<td>Held-out perturbation prediction, stimulation / lesion validation, or an external standard that the model had to predict rather than explain post hoc.</td>
<td>It blocks observational fit from being rephrased as causal validation.</td>
</tr>
<tr>
<td><strong>Reliability window</strong></td>
<td>Session interval, task or rest condition, site / scanner dependence, and whether reproducibility was shown only under closely matched conditions.</td>
<td>It blocks a same-lab repeatability result from being rephrased as general portability.</td>
</tr>
<tr>
<td><strong>Abstention boundary</strong></td>
<td>Which edge directions, strengths, or mechanisms remain unresolved and under what alternative assumptions the interpretation changes.</td>
<td>It blocks incomplete recovery from being silently collapsed into a complete causal graph.</td>
</tr>
</tbody>
</table>
<p>
If this card is missing, this site stops at <strong>model-conditioned causal hypothesis</strong>. A whole-brain DCM graph, an atlas-wide regression DCM estimate, or an activity-flow-compatible diagram is not promoted here to discovered wiring merely because it is dense, scalable, atlas-complete, or predictive.
</p>
</section>

<section class="section" id="identifiability-card">
<h2 class="section-title">Identifiability card for inverse and model-based claims</h2>
<table class="data-table">
<thead>
<tr>
<th>Card field</th>
<th>What must be written</th>
<th>What misreading it blocks</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claim object</strong></td>
<td>Name whether the target is source location, latent state, parameter, connectivity, controller variable, or connectome-conditioned predictor, together with its timescale and spatial unit.</td>
<td>It blocks different kinds of "recovery" from being read as one common achievement.</td>
</tr>
<tr>
<td><strong>Structural identifiability layer</strong></td>
<td>Name whether the declared model is identifiable in principle and disclose known symmetries, reparameterizations, or variables that remain non-identifiable even with ideal data.</td>
<td>It blocks finite-data success from being overread as in-principle uniqueness.</td>
</tr>
<tr>
<td><strong>Practical identifiability layer</strong></td>
<td>Report posterior/profile-likelihood width, ensemble spread, SNR dependence, sample-size or time-window dependence, and other finite-data limits under the submitted experiment.</td>
<td>It blocks a theoretically identifiable model from being overread as practically recovered.</td>
</tr>
<tr>
<td><strong>Competing solution set</strong></td>
<td>Name the alternative model families, local optima, or near-equivalent solutions that remain compatible with the observations.</td>
<td>It blocks one good fit from sounding like the only explanation.</td>
</tr>
<tr>
<td><strong>Design objective</strong></td>
<td>Name whether the next condition was chosen to optimize practical identifiability, model discrimination, posterior contraction, profile-likelihood width, or another declared criterion, and say explicitly if the choice was driven only by convenience, prediction score, or a sloppiness proxy.</td>
<td>It blocks a richer protocol from sounding informative merely because some generic score improved.</td>
</tr>
<tr>
<td><strong>Experiment-design leverage</strong></td>
<td>Name which unresolved ambiguity the protocol targeted, which orthogonal perturbations, regime shifts, targeted recordings, or active data-collection choices were used to reduce it, which identifiability objective selected them, and say explicitly if the evidence is passive only.</td>
<td>It blocks "better prediction" from being rephrased as "solved identification."</td>
</tr>
<tr>
<td><strong>Model-discrepancy stress test</strong></td>
<td>Report whether the new condition exposed systematic residuals, failed fits, or omitted mechanisms, what hierarchy of richer or alternative models was checked, and whether the protocol was revised after that stress test.</td>
<td>It blocks tighter nominal parameter estimates from being overread when the design only forced hidden model error into view.</td>
</tr>
<tr>
<td><strong>Minimum-sufficiency stop rule</strong></td>
<td>State the smallest condition/time-point/recording set required to raise the claim, the stopping threshold on uncertainty or overlap, and how much ambiguity remained once that minimum design was reached.</td>
<td>It blocks endless data collection from sounding like solved identifiability.</td>
</tr>
<tr>
<td><strong>Recorded subset and abstention</strong></td>
<td>Name which parts of the system were actually observed, what remained latent, and where the uniqueness claim stops.</td>
<td>It blocks sparse coverage from being overread as state closure.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-28 deepening: informative experiments must optimize identifiability, stress omitted mechanisms, and declare minimum sufficiency</strong>
<p>
This card needed one more tightening step. <a href="https://doi.org/10.1109/CDC.1991.261405" target="_blank">Diop &amp; Fliess (1991)</a> made persistent trajectories explicit, and <a href="https://doi.org/10.1063/1.3528102" target="_blank">Raue et al. (2010)</a> showed that identifiability analysis can guide new experiments rather than only criticize old ones. <a href="https://doi.org/10.1016/j.mbs.2016.10.009" target="_blank">Chis et al. (2016)</a> then showed that <strong>sloppiness is not identifiability</strong> and that design should optimize explicit identifiability criteria rather than proxy notions of being merely less sloppy. <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">White et al. (2016)</a> showed that complementary experiments can make previously omitted mechanisms relevant, so a nominally more informative design can simultaneously create large <strong>model discrepancy</strong>. In neurophysiology, <a href="https://doi.org/10.1162/neco.2008.08-07-594" target="_blank">Lewi et al. (2009)</a> showed that adaptive information-maximizing stimuli can accelerate parameter learning, and <a href="https://doi.org/10.1371/journal.pcbi.1011342" target="_blank">Gontier et al. (2023)</a> brought that logic to synaptic characterization. In current systems neuroscience, <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that a <strong>small targeted recording set</strong> can remove degeneracy in connectome-constrained networks and even prioritize which neurons should be recorded next, while <a href="https://doi.org/10.1038/s41593-025-01869-7" target="_blank">Langdon &amp; Engel (2025)</a> showed that preserving <strong>causal interactions among task variables</strong> can recover behaviorally relevant computation that correlation-only reductions miss. <a href="https://doi.org/10.1038/s41540-023-00325-1" target="_blank">Gevertz &amp; Kareva (2024)</a> then showed that identifiability analysis can derive a <strong>minimally sufficient</strong> schedule, and <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">Liu et al. (2025)</a> showed that active learning can reduce the observations needed to reach practical identifiability. Therefore, on this site, a stronger ambiguity-breaking design now has to answer four extra questions: <strong>Which identifiability objective chose the next condition?</strong> <strong>Why is the added regime or recording panel orthogonal enough to separate the survivors?</strong> <strong>Did the new condition expose omitted-mechanism error?</strong> and <strong>What minimum-sufficiency design would have been enough to stop?</strong> The submission-side operational version is <a href="../verification.html#experiment-design-leverage">Verification: experiment-design leverage</a>.
</p>
</div>
<p>
If this card is missing, this site stays at <strong>observed-fit / candidate-model</strong> level. The submission-side operational version is <a href="../verification.html#identifiability-card">Verification: Identifiability Card</a>.
</p>
</section>

<section class="section" id="scm">
<h2 class="section-title">SCM and causal discovery only become stronger with intervention</h2>
<p>
SCM is a framework that makes it easy to write down interventions and counterfactuals explicitly. However, when we learn only from observational data, we are often left with a<strong>Markov equivalence class</strong>. As shown by Hauser and Buhlmann, intervention data are important for narrowing this class of equivalences. Even in brain data, Vink et al. showed that resting-state functional connectivity remains a weak predictor of causal interaction, and it is dangerous to determine direction and mechanism based on correlation alone.
</p>
<div class="note-box">
<strong>Difference in role between SCM and DCM</strong>
<p>
DCM is useful for comparing neural circuit candidate generation models, and SCM is useful as a language for expressing interventions and counterfactuals. Both are important, but adding one does not automatically establish cause and effect.
</p>
</div>
</section>

<section class="section" id="validation">
<h2 class="section-title">External validation ladder for progressing to stronger claims</h2>
<table class="data-table">
<thead>
<tr>
<th>Validation ladder</th>
<th>What do we know</th>
<th>Limits that still remain</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Simulation</strong></td>
<td>You can see the lower limit performance of solver and model recovery. </td>
<td>It does not completely reproduce the real head geometry and biological noise. </td>
</tr>
<tr>
<td><strong>Phantom</strong></td>
<td>You can calibrate the geometry and validity of the forward model. </td>
<td>There is no biological plasticity or state dependence. </td>
</tr>
<tr>
<td><strong>Simultaneous invasive/non-invasive record</strong></td>
<td>Comparisons can be made close to the local ground truth. </td>
<td>coverage-limited, not whole-brain ground truth. </td>
</tr>
<tr>
<td><strong>Intracranial stimulation/perturbation</strong></td>
<td>Enables validation of intervention responses and time order. </td>
<td>Highly dependent on stimulus conditions and observation window design. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Operation rules adopted by this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>Don't write solver names as standard:</strong>Bayesian solver, minimum norm, DCM, and SCM are candidates, and acceptance or rejection is determined by audit items. </li>
<li><strong>Don't let richer conditioning stand in for closure:</strong>More modalities, same-brain linkage, and connectome constraints still need fusion, bridge, or identifiability disclosure. </li>
<li><strong>Don't raise causal claims based on observed fit alone:</strong>In the absence of intervention or external validation, stay at the equivalence class or candidate model level. </li>
<li><strong>Write with reservations for deep and fine-grained information:</strong>Do not confuse detectable with robust reconstruction. </li>
<li><strong>Abstain when there is wide uncertainty:</strong>If the solutions overlap, do not force them to collapse into one, but make your reservations clear. </li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Wipf, D., &amp; Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging. <em>NeuroImage</em>, 44(3), 947-966. <a href="https://doi.org/10.1016/j.neuroimage.2008.02.059" target="_blank">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li>Mahjoory, K., Nikulin, V. V., Botrel, L., Linkenkaer-Hansen, K., Fato, M. M., &amp; Haufe, S. (2017). Consistency of EEG source localization and connectivity estimates. <em>NeuroImage</em>, 152, 590-601. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.076" target="_blank">doi:10.1016/j.neuroimage.2017.02.076</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(1), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Vorwerk, J., Wolters, C. H., &amp; Baumgarten, D. (2024). Global sensitivity of EEG source analysis to tissue conductivity uncertainties. <em>Frontiers in Human Neuroscience</em>, 18, 1335212. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">doi:10.3389/fnhum.2024.1335212</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging extended E/MEG source activation with empirical Bayesian uncertainty quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <em>NeuroImage</em>, 19(4), 1273-1302. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <em>Journal of Neuroscience Methods</em>, 208(1), 66-78. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Lee, H.-L., Zahneisen, B., Hugger, T., et al. (2017). Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. <em>NeuroImage</em>, 149, 441-451. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.012" target="_blank">doi:10.1016/j.neuroimage.2017.02.012</a></li>
<li>Frässle, S., Paulus, F. M., Krach, S., &amp; Jansen, A. (2016). Test-retest reliability of effective connectivity in the face perception network. <em>Human Brain Mapping</em>, 37(2), 730-744. <a href="https://doi.org/10.1002/hbm.23061" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle, S., Manjaly, Z. M., Do, C. T., Kasper, L., Pruessmann, K. P., &amp; Stephan, K. E. (2021). Whole-brain estimates of directed connectivity for human connectomics. <em>NeuroImage</em>, 225, 117491. <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Wu, H., Hu, X., &amp; Zeng, Y. (2024). A fast dynamic causal modeling regression method for fMRI. <em>NeuroImage</em>, 304, 120954. <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">doi:10.1016/j.neuroimage.2024.120954</a></li>
<li>Jafarian, A., Assem, M. K., Kocagoncu, E., et al. (2024). Reliability of dynamic causal modelling of resting-state magnetoencephalography. <em>Human Brain Mapping</em>. <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Smith, S. M., Miller, K. L., Salimi-Khorshidi, G., Webster, M., Beckmann, C. F., Nichols, T. E., Ramsey, J. D., &amp; Woolrich, M. W. (2011). Network modelling methods for FMRI. <em>NeuroImage</em>, 54(2), 875-891. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">doi:10.1016/j.neuroimage.2010.08.063</a></li>
<li>Barnett, L., &amp; Seth, A. K. (2017). Detectability of Granger causality for subsampled continuous-time neurophysiological processes. <em>Journal of Neuroscience Methods</em>, 275, 93-121. <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">doi:10.1016/j.jneumeth.2016.10.016</a></li>
<li>Vink, J. J. T., Klooster, D. C. W., Ozdemir, R. A., Westover, M. B., Pascual-Leone, A., &amp; Shafi, M. M. (2020). EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. <em>Brain Topography</em>, 33(2), 221-237. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>Novelli, L., Barnett, L., Seth, A. K., &amp; Razi, A. (2025). Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. <em>Human Brain Mapping</em>, 46(10), e70285. <a href="https://doi.org/10.1002/hbm.70285" target="_blank">doi:10.1002/hbm.70285</a></li>
<li>Yan, J., Zhang, S.-W., Zhang, C., Huang, W., Shi, J., &amp; Chen, L. (2026). Dynamical Causality under Latent Confounders for Biological Network Reconstruction. <em>IEEE Transactions on Pattern Analysis and Machine Intelligence</em>. <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">doi:10.1109/TPAMI.2026.3658839</a></li>
<li>Hauser, A., &amp; Buhlmann, P. (2012). Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. <em>Journal of Machine Learning Research</em>, 13, 2409-2464. <a href="https://jmlr.org/papers/v13/hauser12a.html" target="_blank">JMLR</a></li>
<li>Vink, J. J., Ramos-Nuñez, A. I., Bellesi, A., et al. (2020). The brain's functional connectome is a poor predictor of the brain's causal activity flow. <em>PLOS Computational Biology</em>, 16(1), e1007866. <a href="https://doi.org/10.1371/journal.pcbi.1007866" target="_blank">doi:10.1371/journal.pcbi.1007866</a></li>
<li>Villaverde, A. F. (2019). Observability and Structural Identifiability of Nonlinear Biological Systems. <em>Complexity</em>, 2019, 8497093. <a href="https://doi.org/10.1155/2019/8497093" target="_blank">doi:10.1155/2019/8497093</a></li>
<li>Villaverde, A. F., Tsiantis, N., &amp; Banga, J. R. (2019). Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. <em>Journal of The Royal Society Interface</em>, 16(156), 20190043. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <em>Nature Neuroscience</em>, 7, 1345-1352. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
<li>Rasero, J., Betzel, R., Sentis, A. I., Kraynak, T. E., Gianaros, P. J., &amp; Verstynen, T. (2024). Similarity in evoked responses does not imply similarity in macroscopic network states. <em>Network Neuroscience</em>, 8(1), 335-354. <a href="https://doi.org/10.1162/netn_a_00354" target="_blank">doi:10.1162/netn_a_00354</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 2561-2574. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Langdon, C., &amp; Engel, T. A. (2025). Latent circuit inference from heterogeneous neural responses during cognitive tasks. <em>Nature Neuroscience</em>, 28, 665-675. <a href="https://doi.org/10.1038/s41593-025-01869-7" target="_blank">doi:10.1038/s41593-025-01869-7</a></li>
<li>Diop, S., &amp; Fliess, M. (1991). Nonlinear observability, identifiability, and persistent trajectories. <em>Proceedings of the 30th IEEE Conference on Decision and Control</em>, 714-719. <a href="https://doi.org/10.1109/CDC.1991.261405" target="_blank">doi:10.1109/CDC.1991.261405</a></li>
<li>Raue, A., Becker, V., Klingmüller, U., &amp; Timmer, J. (2010). Identifiability and observability analysis for experimental design in nonlinear dynamical models. <em>Chaos</em>, 20(4), 045105. <a href="https://doi.org/10.1063/1.3528102" target="_blank">doi:10.1063/1.3528102</a></li>
<li>Chis, O.-T., Villaverde, A. F., Banga, J. R., &amp; Balsa-Canto, E. (2016). On the relationship between sloppiness and identifiability. <em>Mathematical Biosciences</em>, 282, 147-161. <a href="https://doi.org/10.1016/j.mbs.2016.10.009" target="_blank">doi:10.1016/j.mbs.2016.10.009</a></li>
<li>Lewi, J., Butera, R., &amp; Paninski, L. (2009). Sequential Optimal Design of Neurophysiology Experiments. <em>Neural Computation</em>, 21(3), 619-687. <a href="https://doi.org/10.1162/neco.2008.08-07-594" target="_blank">doi:10.1162/neco.2008.08-07-594</a></li>
<li>Gontier, C., Surace, S. C., Delvendahl, I., Müller, M., &amp; Pfister, J.-P. (2023). Efficient sampling-based Bayesian Active Learning for synaptic characterization. <em>PLOS Computational Biology</em>, 19(8), e1011342. <a href="https://doi.org/10.1371/journal.pcbi.1011342" target="_blank">doi:10.1371/journal.pcbi.1011342</a></li>
<li>White, A., Tolman, M., Thames, H. D., Withers, H. R., Mason, K. A., &amp; Transtrum, M. K. (2016). The limitations of model-based experimental design and parameter estimation in sloppy systems. <em>PLOS Computational Biology</em>, 12(12), e1005227. <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">doi:10.1371/journal.pcbi.1005227</a></li>
<li>Gevertz, J. L., &amp; Kareva, I. (2024). Minimally sufficient experimental design using identifiability analysis. <em>npj Systems Biology and Applications</em>, 10, 2. <a href="https://doi.org/10.1038/s41540-023-00325-1" target="_blank">doi:10.1038/s41540-023-00325-1</a></li>
<li>Liu, X., Wanika, L., Chappell, M. J., &amp; Branke, J. (2025). Efficient data collection for establishing practical identifiability via active learning. <em>Computational and Structural Biotechnology Journal</em>, 27, 4992-5006. <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">doi:10.1016/j.csbj.2025.10.058</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>, 15, 229. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>, 16, 8887. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <em>Cell Reports Methods</em>, 3(7), 100520. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>MICrONS Consortium, Bae, J. A., et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435-447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Egger, J., Kostoglou, K., &amp; Müller-Putz, G. R. (2024). Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Scientific Reports</em>, 14, 20247. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="measurement-and-modeling-terms.html">From measurement to modeling →</a></li>
<li><a href="measurement-stack-and-claim-ceiling.html">Observability and claim ceiling →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">Uncertainty/proofreading/abstention →</a></li>
<li><a href="state-continuity-bridge.html">State-continuity bridge →</a></li>
<li><a href="counterfactual-and-perturbation-verification.html">Counterfactual/intervention/perturbation →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html">Introduction to EEG →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../tech_roadmap.html#qa-r1">R1 inverse problem →</a></li>
</ul>
</div>
</aside>
</main>
