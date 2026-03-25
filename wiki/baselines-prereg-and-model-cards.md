---
layout: default
title: "Wiki: Baseline / Benchmark / Pre-registration / Model Card"
description: "Organizes baseline, benchmark, pre-registration, model cards, and claim-triggered companion cards so a score is not confused with comparable evidence."
article_type: Wiki
subtitle: "From score reporting to the artifact stack required by the claim"
author: Mind Uploading Research Project
last_updated: "2026-03-25"
note: "Learning guide"
audience: "People who find baseline, benchmark, pre-registration, and model-card language similar, and people who want to know which extra cards are required before a stronger claim is allowed"
reading_time: "12-18 minutes"
page_intro: "This page explains the operational difference among baseline, benchmark, pre-registration, model card, and the additional cards that become necessary when a result depends on multimodal fusion, large-scale pretraining, shortcut resistance, living-human proxy bundles, or sequential same-subject bridges."
accuracy_note: "This page is a learning guide to the artifact stack. The authoritative card fields and stop rules still live on the public Verification page."
page_highlights:
  - "A benchmark is not just a score sheet; on this site it also includes split rules, metric semantics, and benchmark governance."
  - "A normal model card is not enough for every claim shape; some results need claim-triggered companion cards."
  - "For decode or representation claims, shortcut resistance is a separate audit from score reporting."
  - "For multimodal or atlas-prior claims, a Fusion Card is separate from synchronization middleware or co-registration."
  - "For several living-human proxy rows used together, a Human Proxy Composition Card is required before same-subject state-identification language is allowed."
  - "For same-subject or same-brain sequential bridges, a State-Continuity Bridge Card is required before same-state language is allowed."
known_points:
  - "Comparable progress requires a baseline, a benchmark object, preregistered stopping rules, a result report, and explicit failure disclosure."
  - "Benchmark meaning depends not only on the dataset and score, but also on split randomness, metric bundle, extra-data policy, operational constraints, and postmortems."
  - "Observability Budget, Specificity & Shortcut Card, Fusion Card, Pretraining Card, Human Proxy Composition Card, and State-Continuity Bridge Card answer different failure modes."
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
<td><strong>Fusion Card</strong></td>
<td>The multimodal / atlas-prior integration audit.</td>
<td>Fixes acquisition relation, lag audit, co-registration, fusion model, unimodal baselines, external calibration, and abstention.</td>
</tr>
<tr>
<td><strong>Pretraining Card</strong></td>
<td>The EEG foundation / self-supervised transfer audit.</td>
<td>Fixes corpus identity / overlap, harmonization, adaptation regime, benchmark provenance, and efficiency constraints.</td>
</tr>
<tr>
<td><strong>Human Proxy Composition Card</strong></td>
<td>The bundle audit for several living-human proxy rows.</td>
<td>Fixes proxy class, direct observable, same-subject relation, model burden, incremental evidence, and residual latent-state ceiling.</td>
</tr>
<tr>
<td><strong>State-Continuity Bridge Card</strong></td>
<td>The sequential bridge audit.</td>
<td>Fixes acquisition order, elapsed time, regime continuity, coordinate transfer / deformation, and bridge-validation rung before same-state language is allowed.</td>
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
<td><strong>Multimodal or atlas-prior claim</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Fusion Card</strong></td>
<td>Stops simultaneity, synchronization middleware, or a prior from standing in for validated fusion.</td>
</tr>
<tr>
<td><strong>Several living-human proxy rows used together</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>Human Proxy Composition Card</strong></td>
<td>Stops proxy-rich bundles from being overread as same-subject state identification.</td>
</tr>
<tr>
<td><strong>Same-subject / same-brain sequential bridge</strong></td>
<td>Base stack + Observability Budget</td>
<td><strong>State-Continuity Bridge Card</strong></td>
<td>Stops specimen identity or repeated access from being overread as same-state evidence.</td>
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
<li><strong>If it is a foundation / self-supervised EEG result, is a Pretraining Card visible?</strong> Are corpus overlap, harmonization, adaptation regime, benchmark version, and inference-stage restrictions written?</li>
<li><strong>If it is multimodal or atlas-prior, is a Fusion Card visible?</strong> Are acquisition relation, lag audit, fusion baseline, and external calibration written?</li>
<li><strong>If several living-human proxy rows are used together, is a Human Proxy Composition Card visible?</strong> Are proxy class, model burden, and increment over the strongest single row disclosed?</li>
<li><strong>If the claim bridges same-subject or same-brain measurements across regimes, is a State-Continuity Bridge Card visible?</strong> Are elapsed time, regime continuity, deformation / registration burden, and bridge-validation rung written?</li>
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
<li><a href="human-proxy-composition.html">Human Proxy Composition -></a></li>
<li><a href="state-continuity-bridge.html">State-Continuity Bridge -></a></li>
</ul>
</div>
</aside>
</main>
