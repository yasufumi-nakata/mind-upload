---
layout: default
title: "Wiki: Standards, Repositories, Validators, and Benchmarks"
description: "Separates BIDS, OpenNeuro/PhysioNet, HED, LSL, BIDS Derivatives, MNE-BIDS, workflow / pipeline recipes, MOABB, and benchmark-governance artifacts so reproducibility failures are not hidden inside one label."
article_type: Wiki
subtitle: "Separate standards, repositories, derivatives, workflow recipes, validators, benchmark harnesses, and benchmark provenance"
author: Mind Uploading Research Project
last_updated: "2026-04-02"
note: "Operational guide"
audience: "People who see BIDS, OpenNeuro, PhysioNet, MNE-BIDS, MNE-BIDS-Pipeline, and MOABB as the same kind of thing"
reading_time: "10-15 minutes"
page_intro: "This page organizes the roles of ``Standards,'' ``Repositories,'' ``Validators,'' ``Derivatives,'' ``Workflow / model recipes,'' ``Benchmarks,'' and ``benchmark provenance / governance,'' together with version freezing, event semantics, synchronization middleware, and loader / benchmark tooling. The goal is not to memorize product names but to understand where reproducibility actually breaks."
accuracy_note: "What I will explain here is a basic organization of roles. BIDS vessels, HED semantics, and LSL synchronization are complementary, and the final validity of any one is not guaranteed."
page_highlights:
  - "BIDS is a standard, OpenNeuro and PhysioNet are storage areas, Validator is a mechanical inspection, and Benchmark is a comparison rule."
  - "BIDS Derivatives and result provenance are separate from raw-data layout: processed outputs need their own lineage and pipeline description."
  - "If you do not fix the OpenNeuro snapshot or the PhysioNet version, you will not be able to reproduce the same data name."
  - "HED and Motion-BIDS are extensions to BIDS that carry machine-readable semantics and additional metadata."
  - "LSL is a synchronization middleware and is not a replacement for BIDS or benchmark."
  - "BIDS/HED/LSL do not by themselves validate multimodal biological fusion; that requires a separate Fusion Card."
  - "A loader like MNE-BIDS, a workflow like MNE-BIDS-Pipeline or BIDS Apps, a model recipe like BIDS Stats Models, and a benchmark harness like MOABB have different roles."
  - "Benchmark harness and benchmark provenance are different objects: official rules, split/randomization, extra-data policy, pretrained-checkpoint policy, inference-stage restrictions, and later organizer postmortems can all change what the score means."
  - "Official challenge homepages, rules pages, submission constraints, and leaderboard corrections count as part of the benchmark object rather than as administrative footnotes."
  - "A pipeline name alone is still too coarse: derivative lineage, config, skipped steps, software version, and runtime container remain separate reproducibility fields."
known_points:
  - "To make research comparable, it is necessary to separate the data format, publication destination, derivative lineage, workflow recipe, testing methods, and evaluation rules."
  - "BIDS and EEG-BIDS are standards for 'how to place' them, not scoring rules themselves."
  - "Event semantics like HED have the role of supplementing the meaning of events listed in BIDS in a machine-readable manner."
  - "LSL helps with clock alignment between streams, but is not the ground truth for hardware delays."
  - "Even if clocks are aligned and metadata are standardized, multimodal claims still need a separate audit of fusion model, co-registration, and calibration."
  - "OpenNeuro and PhysioNet are public platforms, but they do not automatically guarantee all input formats and evaluation procedures."
  - "Raw BIDS and BIDS derivatives are separate layers; processed data should carry explicit lineage rather than silently replacing raw."
  - "A workflow name alone is not a frozen recipe: config files, skipped stages, model graph, and software / container versions can all change outputs."
  - "Even if the dataset name is the same, it cannot be compared if the snapshot / version and evaluation family are different."
  - "A benchmark title alone is still insufficient: benchmark meaning can move with current rule snapshot, split construction, hidden grouping, extra-data / pretrained-model policy, inference-stage budget, and organizer postmortems."
  - "MOABB fixes evaluation families such as within-session / cross-session / cross-subject, but challenge operations can add additional constraints that are not visible in the harness name alone."
  - "Containerized execution helps software portability, but it does not by itself freeze benchmark meaning or full result provenance."
unknown_points:
  - "It is unclear what granularity the final common benchmark for WBE should be."
  - "Which validators and audit items will become the final standard will depend on future operational design."
  - "The best common schema for workflow provenance across decoding, source imaging, and multimodal pipelines is still evolving."
wiki_links:
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Return to the larger map of Standards, Bench, Registration, and Audit."
  - label: "Wiki: Baseline/Pre-registration/Model Card"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Compensates for differences in operational language beyond Benchmark."
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Add specific examples of log information you want to include in the standard."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "You can return to other auxiliary pages."
recommended_pages:
  - label: "Data & Bench"
    url: "/datasets.html"
  - label: "Verification base"
    url: "/verification.html"
  - label: "Casework"
    url: "/verification.html#casework"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest distinction</h2>
<p>
<strong>Standards</strong> fix raw-data layout, <strong>repositories</strong> fix where a versioned dataset is published, <strong>validators</strong> check schema compliance, <strong>derivative specifications</strong> fix how processed outputs stay linked to their sources, <strong>workflow / model recipes</strong> fix how outputs are produced, and <strong>benchmark harnesses</strong> plus <strong>benchmark provenance / governance</strong> fix what the score means. Even though they all look like ``research infrastructure,'' their roles are different.
</p>
</div>

<div class="note-box">
<strong>2026-03-26 correction: benchmark provenance is part of the benchmark</strong>
<p>
The old version of this page still let <strong>benchmark</strong> sound like a stable comparison label once the harness name was known. That is too weak. The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) homepage</a> states that the original challenge preprint became <strong>out of date</strong> during execution and that the website should be treated as current. The official <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> then fix <strong>downsampling after 0.5-50 Hz filtering</strong>, <strong>additional-data disclosure</strong>, <strong>pretrained-model disclosure</strong>, and a <strong>single-GPU 20 GB inference-stage constraint</strong>. The official <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a> further fixes that it is an <strong>inference-only code submission</strong>, and the final <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> later disclosed a <strong>Challenge 2 randomization error</strong> and separated the final awards. Recent benchmark papers make the same point in more general form: <a href="https://doi.org/10.48550/arXiv.2508.17742" target="_blank">Xiong et al. (2025/2026)</a> argue that inconsistent evaluation protocols make EEG-foundation-model comparisons unreliable, and <a href="https://doi.org/10.48550/arXiv.2601.17883" target="_blank">Liu et al. (2026)</a> show across <strong>12 open-source foundation models</strong> and <strong>13 datasets</strong> that the reading of transfer quality depends materially on protocol choice. Therefore, on this site, <strong>benchmark provenance / governance</strong> is treated as a first-class part of reproducibility rather than as after-the-fact administration.
</p>
</div>

<div class="note-box">
<strong>2026-04-02 correction: BIDS plus a benchmark name still do not fix derivatives, workflow recipe, or result provenance</strong>
<p>
The remaining weakness on this page was subtler. It still let <strong>BIDS + repository + benchmark name</strong> sound almost sufficient for reproducibility. Current official and primary sources do not support that reading. <a href="https://doi.org/10.7554/eLife.71774" target="_blank">Markiewicz et al. (2021)</a> show that OpenNeuro plus BIDS helps freeze a shareable, versioned raw input. But the BIDS specification separately requires derived datasets to carry <strong>GeneratedBy</strong> and <strong>SourceDatasets</strong>, and derivative files to keep explicit <strong>Sources</strong>. <a href="https://doi.org/10.1371/journal.pcbi.1005209" target="_blank">Gorgolewski et al. (2017)</a> show that BIDS Apps solve deployment and interface portability, not automatic benchmark meaning; <a href="https://mne.tools/mne-bids-pipeline/stable/" target="_blank">MNE-BIDS-Pipeline</a> explicitly exposes a text-file configuration, cached intermediate steps, and summary reports; <a href="https://bids-standard.github.io/stats-models/index.html" target="_blank">BIDS Stats Models</a> defines a separate machine-readable model recipe; and <a href="https://doi.org/10.1038/sdata.2016.102" target="_blank">Maumet et al. (2016)</a> show that result provenance itself can be packaged as a separate standardized object. Therefore, on this site, <strong>derivative specification</strong>, <strong>workflow / model recipe</strong>, and <strong>execution / result provenance</strong> are now treated as distinct layers rather than as details hidden inside ``BIDS'' or ``benchmark.''
</p>
</div>

<section class="section" id="why-separate">
<h2 class="section-title">Why consider separately</h2>
<p>
If you confuse these layers, you'll get the wrong impression, such as, ``There's a benchmark because you uploaded it to OpenNeuro,'' ``Because it's BIDS, the processed outputs are already traceable,'' ``Because the pipeline name was given, the recipe is already frozen,'' or ``Because MOABB was named, the benchmark meaning is already fixed.'' In reality, the tasks of aligning raw data, naming derivative lineage, freezing workflow and model recipes, defining comparison rules, and freezing the exact benchmark governance are different things.
</p>
</section>

<section class="section" id="terms">
<h2 class="section-title">First, separate terms</h2>
<table class="data-table">
<thead>
<tr>
<th>Term</th>
<th>What it does</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>standard (raw layout)</strong></td>
<td>The way to place the file, name it, and write the metadata will be the same. </td>
<td>BIDS, EEG-BIDS. </td>
</tr>
<tr>
<td><strong>Storage/shared infrastructure (repository)</strong></td>
<td>Publish your data so others can retrieve it. </td>
<td>OpenNeuro, PhysioNet, PDB, etc. </td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>Mechanically inspects for standard violations and missing metadata. </td>
<td>BIDS Validator. </td>
</tr>
<tr>
<td><strong>derivative specification / lineage</strong></td>
<td>Keep processed outputs separate from raw and link them back to their direct sources and generating pipeline. </td>
<td>BIDS Derivatives, <code>GeneratedBy</code>, <code>SourceDatasets</code>, <code>Sources</code>. </td>
</tr>
<tr>
<td><strong>loader / converter</strong></td>
<td>Read or write datasets in a standardized way and bridge them into the analysis library. </td>
<td>MNE-BIDS. </td>
</tr>
<tr>
<td><strong>workflow / model recipe</strong></td>
<td>Fix the ordered steps, config values, optional branches, grouping logic, and analysis graph that generate the outputs. </td>
<td>MNE-BIDS-Pipeline config, BIDS Apps CLI, BIDS Stats Models JSON. </td>
</tr>
<tr>
<td><strong>execution / result provenance</strong></td>
<td>Record which software, version, container, code, and activity actually produced the reported outputs and reports. </td>
<td>NIDM-Results, pipeline reports, DataLad / BABS audit trail. </td>
</tr>
<tr>
<td><strong>benchmark harness</strong></td>
<td>Fix issues, divisions, indicators, and prohibitions to make them comparable. </td>
<td>MOABB, MLPerf, ImageNet type operation. </td>
</tr>
<tr>
<td><strong>benchmark provenance / governance</strong></td>
<td>Fix which exact rule snapshot, split construction, hidden grouping, extra-data policy, pretrained-checkpoint policy, execution constraints, and postmortems defined the score. </td>
<td>Official challenge homepage / rules / submission / leaderboard, benchmark postmortems. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="operational-stack">
<h2 class="section-title">In practice, the short labels are not enough, so we look at 11 layers</h2>
<table class="data-table">
<thead>
<tr>
<th>layer</th>
<th>Representative examples</th>
<th>What to fix here</th>
<th>No guarantees yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Standards</strong></td>
<td>BIDS, EEG-BIDS</td>
<td>File name, required metadata, coordinate system, events/channels/electrodes format. </td>
<td>train/test Splits and indicators are not determined. </td>
</tr>
<tr>
<td><strong>2. Public version</strong></td>
<td>OpenNeuro snapshot, PhysioNet version</td>
<td>A third party can return to the same input to know which version was obtained. </td>
<td>The version does not necessarily fix the benchmark split or preprocessing conditions. </td>
</tr>
<tr>
<td><strong>3. Event semantics/extension schema</strong></td>
<td>HED, Motion-BIDS</td>
<td><code>trial_type</code> meaning, event tag, additional sensor metadata, and coordinate frame. </td>
<td>Clock alignment and benchmark split are not determined automatically. </td>
</tr>
<tr>
<td><strong>4. Synchronization middleware</strong></td>
<td>LSL</td>
<td>Time alignment of multiple streams, clock offset estimation, and stream metadata. </td>
<td>We do not guarantee the true value of device-side delay or stimulus presentation delay. </td>
</tr>
<tr>
<td><strong>5. Derivative specification / lineage</strong></td>
<td>BIDS Derivatives, <code>GeneratedBy</code>, <code>SourceDatasets</code>, <code>Sources</code></td>
<td>Keep processed outputs separate from raw and make source ancestry plus generating pipeline explicit. </td>
<td>A clean or epoched file can still be overread as self-explanatory if lineage is missing. </td>
</tr>
<tr>
<td><strong>6. Conversion/Reading</strong></td>
<td>MNE-BIDS</td>
<td>BIDSPath, metadata extraction, reading path to MNE, format conversion when necessary. </td>
<td>Comparison indicators and evaluation families are not fixed. </td>
</tr>
<tr>
<td><strong>7. Workflow / model recipe</strong></td>
<td>MNE-BIDS-Pipeline config, BIDS Apps CLI, BIDS Stats Models JSON</td>
<td>Fix step order, skipped or optional stages, model graph, and config values that determine derived outputs. </td>
<td>The same raw input can still produce different derivatives when the recipe changes. </td>
</tr>
<tr>
<td><strong>8. Execution / result provenance</strong></td>
<td>NIDM-Results, pipeline reports, DataLad / BABS run records</td>
<td>Record which software, version, container, commands, and activities actually produced the outputs being reported. </td>
<td>A figure or score table can still be detached from the software state that created it. </td>
</tr>
<tr>
<td><strong>9. Benchmark harness</strong></td>
<td>MOABB</td>
<td>paradigm, evaluation family, statistical comparison, cross-sectional evaluation of the same pipeline. </td>
<td>Current rule snapshot, hidden grouping, extra-data policy, and execution constraints are not fixed unless governance documents are also frozen. </td>
</tr>
<tr>
<td><strong>10. Benchmark provenance / governance</strong></td>
<td>Official homepage, rules page, submission page, leaderboard / postmortem</td>
<td>Current benchmark version, split / randomization, hidden grouping, extra-data and pretrained-model policy, inference-stage restrictions, and later corrections. </td>
<td>This still does not prove target-signal specificity, source-imaging truth, or operational safety outside the stated benchmark. </td>
</tr>
<tr>
<td><strong>11. Learner / runtime environment</strong></td>
<td>Linear classifier, Riemannian pipeline, deep model, container image, lockfile</td>
<td>Which estimator was run with which preprocessing, random numbers, runtime image, and hyperparameters. </td>
<td>If 1-10 above are not fixed, it will not be a fair comparison. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>2026-03 site rule</strong>
<p>
OpenNeuro treats the snapshot as a git tag of the semantic version, and PhysioNet also explicitly cites the version for each project. Therefore, on this site, we include not only the dataset name but also the <strong>snapshot / version / DOI or persistent URL</strong> in the artifact. Additionally, BIDS is a raw-data container, BIDS Derivatives is the processed-data layer, HED/Motion-BIDS is semantics and additional metadata, LSL is synchronization, MNE-BIDS is an input/output path, MNE-BIDS-Pipeline or a BIDS App is a workflow recipe, BIDS Stats Models is a model recipe, NIDM-Results is result provenance packaging, and MOABB is a comparison rule. Please don't mix these up and read that ``Since I used BIDS, I was able to get past the benchmark'' or ``Since I installed LSL, I was able to solve the hardware delay.''
</p>
</div>
<div class="note-box">
<strong>2026-03-20 addendum: synchronization infrastructure is not a Fusion Card</strong>
<p>
The remaining weakness was to let <strong>BIDS + HED + LSL</strong> sound like a complete multimodal validity package. That is too strong. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> made clear that LSL solves synchronized stream transport rather than device-side delay truth. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a> showed that EEG-fMRI fusion remains model-conditioned, and <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> plus <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed that simultaneous multimodal recordings can retain modality-specific structure even when acquired together. Therefore, on this site, standards and synchronization infrastructure are necessary inputs to a multimodal study, but a separate <a href="../verification.html#fusion-card">Fusion Card</a> is still required before the claim ceiling is raised.
</p>
</div>
<div class="note-box">
<strong>2026-03-26 addendum: a benchmark name is not yet a fixed benchmark object</strong>
<p>
<a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB</a> correctly fixes evaluation families such as <strong>within-session</strong>, <strong>cross-session</strong>, and <strong>cross-subject</strong>, but current EEG challenge operations show that this is only one part of the benchmark object. The official <a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge rules</a> fixed the filter / downsample route, additional-data policy, pretrained-model disclosure, and inference-stage memory budget, the official <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a> fixed that the competition was <strong>inference-only</strong>, and the final <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> disclosed a <strong>non-randomized Challenge 2 split</strong> that changed the prize structure. Therefore, on this site, a benchmark claim is incomplete unless the <strong>harness</strong> and the <strong>current governance / provenance documents</strong> are frozen together.
</p>
</div>
</section>

<section class="section" id="benchmark-provenance">
<h2 class="section-title">Benchmark provenance is part of reproducibility</h2>
<p>
The practical weakness on this page was to stop at <strong>benchmark harness</strong>. Recent official and primary sources do not support that shortcut. The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge homepage</a> explicitly says the original preprint became outdated during execution, the official <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> fix operational constraints, the official <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a> narrows the executable object to <strong>inference-only code</strong>, and the final <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> discloses a split-construction failure that changed how the ranking had to be interpreted. In parallel, <a href="https://doi.org/10.48550/arXiv.2508.17742" target="_blank">Xiong et al. (2025/2026)</a> and <a href="https://doi.org/10.48550/arXiv.2601.17883" target="_blank">Liu et al. (2026)</a> both argue that fair EEG-foundation-model comparison requires standardized protocols and that rankings still depend materially on evaluation choices. Therefore, this site now separates <strong>benchmark provenance / governance</strong> from the harness name itself.
</p>
<table class="data-table">
<thead>
<tr>
<th>Benchmark field</th>
<th>What it fixes</th>
<th>Unsafe shortcut if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Current rule snapshot</strong></td>
<td>Which homepage / rules / starter-kit state was actually in force when the run was made.</td>
<td>Reading an outdated proposal paper as the final benchmark definition.</td>
</tr>
<tr>
<td><strong>Split / randomization / hidden grouping</strong></td>
<td>Whether trial order, subject contiguity, session grouping, or other hidden structure could be exploited.</td>
<td>Reading a leaderboard as if it reflected portable subject-invariant generalization by default.</td>
</tr>
<tr>
<td><strong>Extra-data / pretrained-model policy</strong></td>
<td>Whether external corpora, checkpoints, or fine-tuning routes were allowed and how they had to be disclosed.</td>
<td>Comparing runs as if they were trained under the same information budget.</td>
</tr>
<tr>
<td><strong>Inference-stage execution constraints</strong></td>
<td>Whether the object being compared was a full training pipeline, an inference-only submission, or a memory / hardware-bounded executable.</td>
<td>Treating challenge rank as a pure representation-learning comparison independent of systems constraints.</td>
</tr>
<tr>
<td><strong>Postmortem / correction status</strong></td>
<td>Whether organizers later disclosed split flaws, score-definition changes, or prize-structure revisions.</td>
<td>Reading an early leaderboard snapshot as final scientific truth.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="eeg-example">
<h2 class="section-title">Looking at the example of EEG</h2>
<table class="data-table">
<thead>
<tr>
<th>stage</th>
<th>What to do there</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Align to standards</strong></td>
<td>Align EEG files, events.tsv, channels.tsv, and metadata to BIDS format. </td>
</tr>
<tr>
<td><strong>2. Add event semantics</strong></td>
<td>Specify <code>trial_type</code>, condition description, HED tags, manual scoring rule, and report usage flag. </td>
</tr>
<tr>
<td><strong>3. Audit synchronization</strong></td>
<td>How to measure clock domain, LSL / TTL / photodiode, delay / jitter / drift will be left. </td>
</tr>
<tr>
<td><strong>4. Check with Validator</strong></td>
<td>Mechanically identifies violations of standards and missing items. </td>
</tr>
<tr>
<td><strong>5. Publish to storage</strong></td>
<td>Put it on a shared platform like OpenNeuro or PhysioNet so it can be retrieved by third parties. </td>
</tr>
<tr>
<td><strong>6. Freeze derivative lineage</strong></td>
<td>Keep preprocessed outputs, epochs, features, and reports as derivatives with explicit source ancestry. </td>
</tr>
<tr>
<td><strong>7. Freeze workflow / model recipe</strong></td>
<td>Record the pipeline config, optional branches, model graph, and software settings that generated the outputs. </td>
</tr>
<tr>
<td><strong>8. Compare with benchmarks</strong></td>
<td>Compare models with the same train/test split, the same metrics, and the same baseline. </td>
</tr>
<tr>
<td><strong>9. Freeze benchmark provenance</strong></td>
<td>Record the active rules page, split/randomization policy, extra-data / pretrained-model policy, inference-stage restrictions, and postmortem status together with the score. </td>
</tr>
<tr>
<td><strong>10. Freeze runtime / result provenance</strong></td>
<td>Record software versions, container or lockfile, commands, reports, and result bundles so the published figure or score can be traced back to the run that made it. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>This is important</strong>
<p>
Just by aligning to the standard, there is still no "rule for comparison." But even if there is a benchmark, the comparison can still break if derivative lineage, workflow recipe, or runtime provenance are left implicit. All of those layers matter.
</p>
</div>
</section>

<section class="section" id="missing-piece">
<h2 class="section-title">What is missing?</h2>
<table class="data-table">
<thead>
<tr>
<th>What is missing</th>
<th>Problems that are likely to occur</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standards</strong></td>
<td>The file name and metadata are different for each person, and it stops at the entrance to the supplementary exam. </td>
</tr>
<tr>
<td><strong>Storage place</strong></td>
<td>Even if you know about its existence, you will not be able to obtain it or reuse it, and the circle of comparison will not expand. </td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>Notice of violation of standards is delayed, and accidents occur immediately before sharing or during reanalysis. </td>
</tr>
<tr>
<td><strong>Derivative specification / lineage</strong></td>
<td>Processed outputs can be mistaken for raw or for each other, and later readers cannot tell which source files or branches generated them. </td>
</tr>
<tr>
<td><strong>Workflow / model recipe</strong></td>
<td>The same pipeline name can hide different optional steps, configs, and model graphs, so the rerun does not actually reproduce the same analysis. </td>
</tr>
<tr>
<td><strong>Execution / result provenance</strong></td>
<td>A figure, table, or derivative can no longer be traced back to the exact software, version, container, and commands that created it. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Each person evaluates using different divisions and indicators, and the meaning of "winning" fluctuates. </td>
</tr>
<tr>
<td><strong>Benchmark provenance / governance</strong></td>
<td>The same benchmark name hides different rule snapshots, hidden grouping, inference limits, or later corrections, so the score is overread. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="raw-is-not-enough">
<h2 class="section-title">Why raw files alone are not enough</h2>
<p>
Just having a waveform file is not enough for standards or benchmarks. At the very least, without event definitions, stimulus logs, synchronization information, QC logs, and reasons for exclusion, it will be difficult to repeat the same challenge.
</p>
<div class="note-box">
<strong>Safe reading</strong>
<p>
Being "publicly available" and being "comparable" are two different things. Publication is the first step, comparability is the next step in design.
</p>
</div>
</section>

<section class="section" id="common-confusions">
<h2 class="section-title">Common confusion</h2>
<table class="data-table">
<thead>
<tr>
<th>Things I tend to say</th>
<th>More accurate paraphrase</th>
</tr>
</thead>
<tbody>
<tr>
<td>“Since we chose BIDS, there is a benchmark”</td>
<td>BIDS is an input format standard, not a comparison rule itself. </td>
</tr>
<tr>
<td>“It was standardized because it was placed in OpenNeuro”</td>
<td>Even if it is posted in the storage area, the standards and metadata are not necessarily sufficient. </td>
</tr>
<tr>
<td>"We used the same input because the dataset name is the same"</td>
<td>Unless you fix OpenNeuro snapshot or PhysioNet version, it cannot be said that it is the same input. </td>
</tr>
<tr>
<td>"The benchmark name alone fixes what the score means"</td>
<td>You still need the active rules snapshot, split / randomization / hidden grouping policy, extra-data / pretrained-model policy, execution constraints, and postmortem status. </td>
</tr>
<tr>
<td>"Validator passed, so it's enough for research"</td>
<td>Validator is a formal check and does not guarantee the validity of the research or the strength of the benchmark. </td>
</tr>
<tr>
<td>"It became a benchmark because I could read it with MNE-BIDS"</td>
<td>MNE-BIDS is a reading/conversion aid; fixing evaluation families and comparison statistics is a separate task. </td>
</tr>
<tr>
<td>"Because the data are in BIDS, the processed outputs are already self-explanatory"</td>
<td>Raw BIDS and BIDS derivatives are separate layers, and processed outputs still need explicit lineage and source ancestry. </td>
</tr>
<tr>
<td>"Naming MNE-BIDS-Pipeline or a BIDS App already freezes the workflow"</td>
<td>The pipeline name alone is still too coarse; config values, skipped stages, model recipe, and software version have to be frozen as well. </td>
</tr>
<tr>
<td>"A containerized run already captures what the score means"</td>
<td>Container and runtime pin help software portability, but benchmark harness and benchmark governance still remain separate objects. </td>
</tr>
<tr>
<td>“Event semantics are fixed because there is `events.tsv`”</td>
<td><code>events.tsv</code> is a container for time and columns, and condition meanings and scorer rules must be fixed separately in <code>events.json</code>, HED, and auxiliary logs. </td>
</tr>
<tr>
<td>"Using LSL even solved the hardware delay"</td>
<td>LSL helps with stream synchronization, but device-side delay for display/audio/amplifier requires separate measurement. </td>
</tr>
<tr>
<td>“MOABB scores can be directly compared across tasks”</td>
<td>Within-session, cross-session, and cross-subject are different evaluation families and cannot be treated equally. </td>
</tr>
<tr>
<td>"It's safe to convert preprocessed files back to raw BIDS"</td>
<td>BIDS and MNE-BIDS basically assume unprocessed or minimally processed data, and it is safer to treat modified data as derivatives by specifying the lineage. </td>
</tr>
<tr>
<td>"We won the benchmark, so it's good enough for actual operation"</td>
<td>Benchmark is a yardstick for comparison and does not automatically guarantee actual operation or the establishment of L4/L5. </td>
</tr>
<tr>
<td>"The challenge proposal paper is the final benchmark specification"</td>
<td>Execution-phase websites, rules, starter kits, and final postmortems can supersede the original proposal and must be frozen with the result. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="freeze-ids">
<h2 class="section-title">Minimum 7 IDs that you want to fix</h2>
<table class="data-table">
<thead>
<tr>
<th>ID</th>
<th>What I want at least</th>
<th>What happens when it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Input ID</strong></td>
<td>OpenNeuro snapshot tag, PhysioNet version, DOI, acquisition date. </td>
<td>If you mix different versions with the same dataset name, you will not be able to try again. </td>
</tr>
<tr>
<td><strong>Schema ID</strong></td>
<td>The version of BIDS/EEG-BIDS, the version of Validator, and the reason for the warning left. </td>
<td>It is not possible to distinguish between standard differences and implementation differences. </td>
</tr>
<tr>
<td><strong>Derivative ID</strong></td>
<td>Derived dataset name, <code>GeneratedBy</code>, <code>SourceDatasets</code>, and direct <code>Sources</code> lineage. </td>
<td>Preprocessed outputs can be confused with raw or with another derivative branch. </td>
</tr>
<tr>
<td><strong>Workflow ID</strong></td>
<td>MNE-BIDS-Pipeline / BIDS App / config file / model-graph version and settings. </td>
<td>Even with the same input version, a different recipe can still generate a different result. </td>
</tr>
<tr>
<td><strong>Evaluation ID</strong></td>
<td>Within-session / cross-session / cross-subject, indicators, split seed, and prohibitions. </td>
<td>The meaning of score will be different and fair comparison will be broken. </td>
</tr>
<tr>
<td><strong>Benchmark Governance ID</strong></td>
<td>Rules URL or archived snapshot, split / randomization policy, hidden grouping note, extra-data / pretrained-model policy, inference-stage restrictions, and postmortem status. </td>
<td>The benchmark title will stay too coarse, and the same leaderboard name may hide different scientific meanings. </td>
</tr>
<tr>
<td><strong>Runtime / Result Provenance ID</strong></td>
<td>Software version, container or lockfile, command log, and result bundle or report identifier. </td>
<td>The published figure or score cannot be traced back to the exact run that created it. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">9 questions when reading strong arguments</h2>
<ol>
<li><strong>What is the input standard?</strong> Check to see if the format is consistent using BIDS, etc. </li>
<li><strong>What version was used:</strong>See if the snapshot, version, DOI, and acquisition date are fixed. </li>
<li><strong>What are the event semantics and clock domain: </strong>Look at <code>trial_type</code>, HED, scorer rule, LSL/TTL/photodiode, delay/jitter audits. </li>
<li><strong>Did they separate raw and derivative?</strong>See if processed outputs remain explicit derivatives with followable lineage. </li>
<li><strong>What was used to read/write:</strong>Look at the loader/transformer and see if its version is specified. </li>
<li><strong>What workflow or model recipe generated the outputs?</strong>Look for config files, optional branches, model graph, and software settings. </li>
<li><strong>What runtime or result-provenance record exists?</strong>Check container / lockfile, command logs, reports, or result bundles. </li>
<li><strong>What benchmark harness was used?</strong>See if evaluation family, metrics, and comparison statistics are fixed. </li>
<li><strong>What benchmark provenance was in force?</strong>Check the active rules snapshot, split/randomization, extra-data / checkpoint policy, inference-stage restrictions, and postmortem status. </li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">References and official pages</h2>
<ul>
<li><a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">Gorgolewski et al. (2016), BIDS</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS Specification: Task events</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS Specification: Electroencephalography</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">BIDS Specification: dataset_description, GeneratedBy, and SourceDatasets</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html" target="_blank">BIDS Derivatives: common data types and lineage metadata</a></li>
<li><a href="https://bids-standard.github.io/stats-models/index.html" target="_blank">BIDS Stats Models Specification</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021), HED for FAIR event annotation</a></li>
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025), HED library schema for EEG data annotation</a></li>
<li><a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025), The lab streaming layer for synchronized multimodal recording</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024), Motion-BIDS</a></li>
<li><a href="https://doi.org/10.7554/eLife.71774" target="_blank">Markiewicz et al. (2021), OpenNeuro</a></li>
<li><a href="https://docs.openneuro.org/git.html" target="_blank">OpenNeuro Docs: Git access and snapshots</a></li>
<li><a href="https://docs.openneuro.org/user_guide.html" target="_blank">OpenNeuro Docs: Dataset landing page and snapshot metadata</a></li>
<li><a href="https://physionet.org/about/" target="_blank">PhysioNet: About and citation policy</a></li>
<li><a href="https://physionet.org/about/content/" target="_blank">PhysioNet: Resources and citation guidance</a></li>
<li><a href="https://doi.org/10.21105/joss.01896" target="_blank">Appelhoff et al. (2019), MNE-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS Docs: write_raw_bids</a></li>
<li><a href="https://mne.tools/mne-bids-pipeline/stable/" target="_blank">MNE-BIDS-Pipeline Docs</a></li>
<li><a href="https://doi.org/10.1371/journal.pcbi.1005209" target="_blank">Gorgolewski et al. (2017), BIDS Apps</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00074" target="_blank">Zhao et al. (2024), BABS and large-scale BIDS-App audit trails</a></li>
<li><a href="https://doi.org/10.1038/sdata.2016.102" target="_blank">Maumet et al. (2016), NIDM-Results</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018), MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB Docs</a></li>
<li><a href="https://moabb.neurotechx.com/docs/auto_examples/paradigm_examples/index.html" target="_blank">MOABB Docs: paradigm and evaluation examples</a></li>
<li><a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025): homepage</a></li>
<li><a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge (2025): rules</a></li>
<li><a href="https://eeg2025.github.io/submission/" target="_blank">EEG Challenge (2025): submission</a></li>
<li><a href="https://eeg2025.github.io/leaderboard/" target="_blank">EEG Challenge (2025): final leaderboard and organizer correction</a></li>
<li><a href="https://doi.org/10.48550/arXiv.2508.17742" target="_blank">Xiong et al. (2025/2026), EEG-FM-Bench</a></li>
<li><a href="https://doi.org/10.48550/arXiv.2601.17883" target="_blank">Liu et al. (2026), EEG Foundation Models: Progresses, Benchmarking, and Open Problems</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020), Bayesian fusion and multimodal DCM for EEG and fMRI</a></li>
<li><a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024), multimodal spontaneous brain-activity organization</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025), simultaneous EEG-PET-MRI across wakefulness and NREM sleep</a></li>
</ul>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
Please use <a href="../datasets.html">Data & Bench</a> to return to the practical entry point, <a href="../verification.html">Verification Platform</a> to return to overall design, and <a href="../verification.html#casework">Casework</a> to return to examples from other fields.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">Baselines/preregistration/model cards →</a></li>
<li><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../datasets.html">Data & Bench →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../verification.html#casework">Casework →</a></li>
</ul>
</div>
</aside>
</main>
