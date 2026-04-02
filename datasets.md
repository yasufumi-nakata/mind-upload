---
layout: default
title: "Data & Hands-on: Where to start and how to get to L0"
description: "From the selection of public data (mainly EEG) to the minimum loop of BIDS → QC → preprocessing → evaluation, organized on one page."
article_type: Resource
subtitle: "Connect ``what to use'' and ``how to reproduce'' in the shortest route without separating them."
author: Mind Uploading Research Project
last_updated: "2026-04-02"
note: "Curated List + L0 Practice"
audience: "People who are wondering which public data to start with, people who are looking for an L0 practice board"
reading_time: "12-20 minutes"
page_intro: "This page is a practical guide that answers both ``Which public data should I start validation with first?'' and ``How do I proceed to L0 reproducible analysis?'' in one place. It does not stop at a list of dataset names; it connects BIDS, QC, splitting, and baselines in a single path."
accuracy_note: "The datasets listed here are entry candidates. They are listed from the perspective of ease of use and reproducibility, and cannot cover all the issues of WBE."
page_highlights:
  - "We look at the shared infrastructure first, then the starter datasets."
  - "Starter data is a practice board for L0-L1, not the ground truth of EEG source imaging."
  - "The page now also fixes a component-addition / ablation ladder for maintenance-state routes, so glial substrate-routing, astrocyte-state, neurovascular / BBB, and clearance augmentations are compared against a named neuron-first baseline instead of being piled into one multimodal boost."
  - "A same-subject support-state bundle is no longer treated as self-interpreting; route class, effective window, quantity bridge, common-driver audit, missingness policy, disagreement topology, repeatability, transfer window, and abstention are now fixed as practical fields."
  - "Even inside direct-validation data, stimulation ground truth, simultaneous invasive recording, and postsurgical outcome are different evidence classes."
  - "A fair inverse-problem benchmark also has to separate focal-centre versus source-extent targets, inverse family, uncertainty object, montage / coverage policy, and geometry / conductivity sensitivity rather than naming only a winning method."
  - "High density is not the only meaningful route: targeted-density and DeepSIF-like low-density ESI can work in bounded regimes, but the gain is still solver-, geometry-, and source-regime-conditioned."
  - "Each starter dataset has different annotation provenance, time fidelity, and independent split units."
  - "Within-session / cross-session / cross-subject / adaptation are different evaluation families and should not be placed side by side under the same score."
  - "Benchmark name is still too coarse: predicted object, independent prediction unit, hold-out unit, adaptation regime, and operations budget can all change what the same score means."
  - "Metric semantics are task-dependent: in imbalanced or rare-event tasks, accuracy or AUROC alone do not fix event sensitivity, false alarms, minority-class failure, or calibration."
  - "Cross-session and adaptation labels are not yet temporal-validity claims; state annotation, fixed decoder interval, recalibration burden, and transfer ceiling still have to be disclosed separately."
  - "Clock domain, stream alignment, digital trigger capture, physical output onset, and uncontrolled-response timing are different timing-validation classes rather than one sync field."
  - "Even when the score is numerically the same, you still have to separate the target neural variable from eye movement, EMG, behavior, feedback routes, subject / session fingerprint, and acquisition-distribution shortcuts such as site / device / reference / electrode layout."
  - "Even when foundation / self-supervised EEG models are used, pretraining-corpus, coordinate-route / reference-family, omitted-channel, and label-budget audits are still required."
  - "Official challenge rules, submission constraints, and later postmortems can change what a benchmark score means, so benchmark provenance is part of the dataset / benchmark card rather than administrative detail."
  - "BIDS raw layout, BIDS derivatives / lineage, workflow recipe, benchmark harness, benchmark-governance snapshot, and runtime pin are different reproducibility layers; naming only the dataset and tool remains too coarse."
  - "Reference system, channel map, electrode layout, and device protocol are not cosmetic metadata; they can move scores and belong in the dataset card."
  - "The ultimate goal is to make it possible for a third party to rerun the result under the same conditions."
  - "The L0 artifact pack now follows this page's stricter site rule: event fidelity, label provenance, acquisition-distribution summary, derivative lineage, and a stopping claim are required alongside version/BIDS/QC/split/baseline."
known_points:
  - "Public EEG data is useful for L0 recall analysis and L1 baseline practice."
  - "When selecting data for the first time, you will move forward if you prioritize ease of retesting over difficulty."
  - "Starter EEG datasets are still neuron-first baselines; maintenance-state claims need paired support-state data or aligned proxy logs, one-family-at-a-time augmentation, and strongest-single-row versus bundle comparison."
  - "Glial substrate-routing and astrocyte-state are different augmentation families: a named astrocyte observable does not fix supplier cell / neuronal sink / fuel object, and a glial fuel-support route does not by itself identify astrocyte ensembles."
  - "A same-subject support-state bundle can still mix common drivers, smaller complete-case slices, and opposite-sign rows, so family-split augmentation is not read strongly on this site without its own augmentation card."
  - "Cue-locked events, expert interval annotations, sleep hypnograms, and physician report-derived labels have different meanings even though they are the same 'public EEG data'."
  - "Even if the accuracy is the same, the strength of the argument that can be read will change depending on which generalization condition the score was obtained under."
  - "The same benchmark name can still hide different predicted objects, independent units, grouped hold-out units, adaptation regimes, and inference budgets."
  - "For class-imbalanced or rare-event tasks, a task-matched metric bundle is required: event sensitivity plus false alarms for seizure tasks, and macro / per-stage agreement for sleep staging, rather than one headline number."
  - "Cross-session accuracy and cross-session adaptation still do not say whether a fixed decoder survived, how much recalibration was needed, or what transfer ceiling remains."
  - "A dataset card that says only `events.tsv` or `LSL` still leaves open whether timing was checked at the stored-data, trigger, physical-output, or uncontrolled-response level."
  - "A same-day score may reflect movement / EOG / EMG / feedback routes, subject / session fingerprint, or acquisition-distribution shortcuts rather than the target signal."
  - "Foundation-model improvements are not comparable unless the pretraining corpus, channel-mismatch handling, acquisition-distribution summary, and adaptation regime are disclosed."
  - "A benchmark name alone is not enough; version, split / randomization rule, hidden grouping, extra-data policy, pretrained-checkpoint policy, and inference-stage restrictions can all change what a score means."
  - "A dataset or pipeline name alone is still not enough; raw layout, derivative lineage, workflow recipe, and runtime pin can each move what the result means."
  - "Reference system, device, electrode layout, and filter chain can change what looks like the same EEG benchmark."
  - "With only starter data and no individual MRI or invasive ground truth, we cannot make strong claims about improved ESI accuracy."
  - "At source-imaging stage C, named validation class still matters because stimulation ground truth, simultaneous SEEG, and clinical outcome do not answer the same error question."
  - "Low-density or targeted-density ESI can be scientifically meaningful in bounded regimes, but montage design, generator depth/orientation, and validation class still have to be declared before the result is compared with HD-EEG or treated as portable."
  - "For inverse-problem claims, same raw data is still not enough; same head model, same preprocessing, same source regime, same inverse family / target object, and a sensitivity report are also required before comparing solver families."
  - "At L0, a reusable artifact pack now also requires event fidelity, label provenance, hold-out ancestry, acquisition-distribution summary, derivative lineage, and a stopping claim rather than only version/BIDS/QC/split/baseline."
unknown_points:
  - "Starter datasets alone cannot solve all the issues of WBE."
  - "We have not yet determined which data will be most effective for future causal/closed-loop verification."
  - "We have not decided yet which public data will be the default route for the annotation fidelity benchmark."
  - "We have not determined yet which public benchmark board should become the default for comparing focal-centre and source-extent inverse methods under the same montage / geometry controls and uncertainty sweep."
  - "We still do not have a default public EEG benchmark that logs state annotation, fixed decoder interval, recalibration burden, and transfer ceiling under one shared temporal-validity schema."
  - "We still do not have a default public dataset bundle that jointly fixes a neuron-first baseline, family-split support-state augmentation, and strongest-single-row versus bundle comparison under one shared missingness and common-driver audit."
wiki_links:
  - label: "Wiki: Basics of EEG"
    url: "/wiki/eeg-basics.html"
    description: "For people who want to understand the EEG signal itself before looking at the dataset."
  - label: "Wiki: Minimum artifact pack for L0"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "Organize L0 deliverables including BIDS, QC, splits, baselines, and execution steps."
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Learn why you need benches and registrations, not just data."
  - label: "Wiki: Data partitioning and leaks"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "We will explain how to divide train/test and common leak accidents from the beginning."
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Explaining why raw EEG alone is not enough from an event and synchronization perspective."
  - label: "Wiki: state/trait/drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Organize longitudinal reading to avoid confusing same-day score and cross-day stability."
  - label: "Wiki: EEG foundation models and pretraining"
    url: "/wiki/eeg-foundation-models.html"
    description: "Use this page when benchmark rules, pretraining corpora, and leaderboard interpretation start to blur together."
  - label: "Wiki: Basics of multimodal integration"
    url: "/wiki/multimodal-integration-basics.html"
    description: "We will explain from the basics what can be supplemented by adding to EEG."
  - label: "Wiki: Standards/Location/Validator/Benchmark"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "We will clarify the role differences between BIDS, OpenNeuro, Validator, and Benchmark."
recommended_pages:
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Verification base"
    url: "/verification.html"
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Use</h2>
<p>
This page is a practical list to help you decide which data to practice with first. First, we use public data to create a state in which we can reproduce the same results (L0), and then check to see if we can predict and withstand changes in conditions (L1-L2).
</p>
</div>

<div class="note-box">
<strong>Criteria for selection</strong>
<p>
When selecting data at the beginning, it is important to choose data that is easy for others to follow in terms of procedures and results, rather than data that is extremely difficult. Rather than aiming for everything from the beginning, a shortcut is to create the smallest loop using public data that is easy to reproduce.
</p>
</div>
<div class="note-box">
<strong>When you want to understand where this page fits</strong>
<p>
This page is the practical entry point for deciding where to start and how to complete the minimum L0 loop. The <a href="verification.html">verification platform</a> handles what counts as progress, and the <a href="verification.html#casework">casework section within the verification platform</a> handles examples from other fields. If you want a one-page guide to how the practical pages differ from the rest of the site, please see <a href="wiki/practical-pages-reading-guide.html">Wiki: Guide to reading practical pages</a>.
</p>
</div>
<div class="note-box">
<strong>When you want to complete with just this page</strong>
<p>
The minimal loop procedure from the old <code>hands_on.md</code> has been integrated into this page. Therefore, you can read straight through to the L0 skeleton, QC, baseline, and completion conditions without having to go to another page after data selection.
</p>
</div>
<div class="note-box">
<strong>If you want the RQ-by-RQ route from datasets back to mind-upload questions</strong>
<p>
This page is the practical data portal, not the full research-question map. If you want to move from a dataset bucket here to a specific mind-upload research question, a fixed EEG-ready claim, and a grant-ready theme, start with the <a href="wiki/mind-upload-current-public-six-rq-brief.html">current public six-RQ brief</a>, then use the <a href="wiki/mind-upload-eeg-rq60-feasibility-and-funds.html">RQ60 EEG feasibility page</a>, the <a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ-by-RQ deep dossiers</a>, the <a href="wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html">grant and dataset playbook</a>, and the <a href="https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md">current funding shortlist</a>.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>What I want to do</th>
<th>First data</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I want to practice the basics of preprocessing and classification</strong></td>
<td><strong>EEG Motor Movement/Imagery</strong> is easy to enter. The problem settings are relatively easy to understand, making it suitable for L0-L1 practice. </td>
</tr>
<tr>
<td><strong>I want to experience long-term data and event detection</strong></td>
<td><strong>CHB-MIT</strong> is a good fit. It lets you practice handling noise, long recordings, and event detection together. </td>
</tr>
<tr>
<td><strong>I want to handle state transitions</strong></td>
<td><strong>Sleep-EDF</strong> is a good fit. It is useful for learning how states change over time. </td>
</tr>
<tr>
<td><strong>I want to see the difficulty of large-scale data</strong></td>
<td><strong>TUH EEG</strong> is also a candidate. However, it is heavy for a first dataset, so it is safer to become familiar with the first three first. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Avoid expecting too much when selecting data at the beginning</strong>
<p>
The starter dataset is not intended to solve all WBE problems at once. The first things you want to get here are <strong>reproducible input organization</strong>, <strong>QC habits</strong>, and <strong>baseline comparison</strong>. Strong points such as identity and causal identity cannot be resolved with just the data at this stage.
</p>
</div>
<div class="note-box">
<strong>Keep the public dataset route conservative</strong>
<p>
This public page stays at the entry level. When one unresolved question is actively being turned into an EEG-ready work package, stronger routing details such as fixed <code>Dxx + DOI</code> anchors, first-pass KPIs, and stopping rules are kept in the wiki rather than promoted here as a public conclusion. Use the <a href="wiki/mind-upload-current-public-six-rq-brief.html">current public six-RQ brief</a>, the <a href="wiki/mind-upload-eeg-rq60-feasibility-and-funds.html">RQ60 EEG feasibility page</a>, and the <a href="wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.html">RQ-by-RQ deep dossiers</a> when you need the current one-question-at-a-time packages.
</p>
</div>

<div class="note-box">
<strong>Seeing before precision</strong>
<p>
When you read a dataset introduction, it is tempting to jump straight to "what score was achieved?" The first questions should instead be <strong>what the train/test split unit is</strong>, <strong>whether leakage was checked</strong>, and <strong>whether the result was compared against a simple baseline</strong>. If this is still unclear, please read <a href="wiki/dataset-splits-and-leakage.html">Wiki: Data Splits and Data Leakage</a> first.
</p>
</div>
<div class="note-box">
<strong>Even if the score is the same, the meaning will change if the generalization conditions are different</strong>
<p>
MOABB treats <strong>within-session</strong>, <strong>cross-session</strong>, and <strong>cross-subject</strong> as separate evaluation families. In other words, even if the 70% is the same, the 70% obtained by "same day, same person, same setup" and the 70% obtained by hold-out on "different day" or "different person" are different achievements. If you want to sort out short-term state fluctuations and long-term drift first, please also have a look at <a href="wiki/state-trait-and-drift.html">Wiki: state/trait/drift</a>.
</p>
</div>
<div class="note-box">
<strong>See label provenance before data name</strong>
<p>
Even with the same "public EEG data", the meaning of comparison is different for <strong>cue-locked annotation channel</strong>, <strong>expert interval annotation</strong>, <strong>whole-night hypnogram</strong>, and <strong>physician report-derived label</strong>. Therefore, on this page, in addition to the dataset name, be sure to include <strong>where the label came from</strong>, <strong>at what time granularity</strong>, and <strong>what is considered as an independent unit of split</strong>.
</p>
</div>
<div class="note-box">
<strong>When you are wondering what to get for L0</strong>
<p>
Even if you just decide on the data name, if the form of the submission is ambiguous, it is easy to get stuck. If you want to see BIDS, Validator, QC logs, division rules, baselines, execution steps, and failure examples in one page, please see <a href="wiki/l0-minimum-artifact-pack.html">Wiki: Minimum L0 artifact pack</a>.
</p>
</div>
<div class="note-box">
<strong>When you want to see the entire order from EEG to L0 in one straight line</strong>
<p>
After the introduction to EEG, if you would like to see the flow of selecting data on this page, going around in the L0 practice section, and confirming it as L0 in Verification, please see <a href="wiki/eeg-to-l0-route.html">Wiki: Straight path from EEG to L0</a>.
</p>
</div>

<div class="note-box">
<strong>Raw EEG is not enough</strong>
<p>
Even if the waveform file is published, if the <strong>event definition</strong>, <strong>stimulus log</strong>, <strong>time synchronization</strong>, and <strong>bad channel / bad segment recording</strong> are weak, it will be difficult to compare again later. Furthermore, in the 2026-03 re-audit, we added to the site rule that event semantics are not fixed just by having `events.tsv`, and hardware delay cannot be audited just by having LSL. If you want to understand this point from the beginning, please see <a href="wiki/event-sync-and-measurement-logs.html">Wiki: Basics of event synchronization and observation logs</a> first.
</p>
</div>

<div class="note-box">
<strong>Event Fidelity Card now required</strong>
<p>
Future dataset cards must include at least <strong>(1) onset / duration / sample</strong>, <strong>(2) clock domain plus stream-alignment rule</strong>, <strong>(3) timing-validation class such as stored-data anchor / digital trigger / physical onset / uncontrolled-response test</strong>, <strong>(4) event semantics such as <code>trial_type</code>, HED, and scoring rules</strong>, <strong>(5) provenance / scorer / report-usage flag</strong>, <strong>(6) independent split units</strong>, and <strong>(7) a clear stopping claim</strong>. Cards without these fields are insufficient as reusable L0 guides.
</p>
</div>

<div class="note-box">
<strong>BIDS, Derivatives, Pipeline, OpenNeuro, and Benchmark are not the same</strong>
<p>
BIDS is a raw-data standard, BIDS Derivatives keeps processed-output lineage explicit, OpenNeuro and PhysioNet are storage areas, Validator is a formal check, MNE-BIDS is a loader, MNE-BIDS-Pipeline or a BIDS App is a workflow recipe, and Benchmark is a comparison rule. If you want to sort out this role difference from the beginning, please use <a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: Standards/Repositories/Validators/Benchmarks</a>.
</p>
</div>

<div class="note-box">
<strong>Plan for future expansion</strong>
<p>
EEG-based starter datasets are enough to begin, but later you may want to add spatial or structural information. If you want to map out what can be added to EEG first, please see <a href="wiki/multimodal-integration-basics.html">Wiki: Multimodal integration basics</a>.
</p>
</div>

<div class="note-box">
<strong>If you want to test whether adding glial, astrocyte, or clearance variables really changes the result</strong>
<p>
This page had one practical weakness: it explained how to build a reproducible neuron-first EEG baseline, but it still lacked a public rule for testing whether adding <strong>maintenance-state / support-state</strong> variables changes prediction, stability, or explanation. The current primary literature does not support one compressed <code>support-variable</code> bucket. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a>, <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a>, <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> sharpen distinct <strong>astrocyte-state</strong> routes across minute-scale network encoding, recall, multiday stabilization, and fear-state support. By contrast, <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a>, <a href="https://doi.org/10.1038/s42255-022-00528-6" target="_blank">Silva et al. (2022)</a>, <a href="https://doi.org/10.1038/s42255-025-01416-5" target="_blank">Pavlowsky et al. (2025)</a>, and <a href="https://doi.org/10.1038/s42255-025-01389-5" target="_blank">Greda et al. (2025)</a> sharpen distinct <strong>glial substrate-routing</strong> routes across lactate support, ketone-body support under starvation, learning-linked fatty-acid routing, and apoE / sortilin-dependent lipid delivery under limited glucose. <a href="https://doi.org/10.1038/s41467-025-61312-0" target="_blank">Mai-Morente et al. (2025)</a> sharpens a pericyte / capillary-support route; <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> sharpens a meningeal-lymphatics / microglia route for synaptic physiology; <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> sharpen bounded human clearance-side observables; and <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a> raises tracer-specific BBB transport quantification while explicitly leaving human ground truth and test-retest for future work. Therefore, this page now fixes a <strong>component-addition / ablation ladder</strong> that separates <strong>glial substrate-routing</strong> from <strong>astrocyte-state</strong> instead of letting readers pile both into one multimodal boost.
</p>
</div>

<section class="section" id="maintenance-component-ablation">
<h2 class="section-title">A practical component-addition / ablation ladder for maintenance-state routes</h2>
<table class="data-table">
<thead>
<tr>
<th>Family added on top of the neuron-first baseline</th>
<th>Minimum paired data requirement</th>
<th>What you may say if the gain survives</th>
<th>What still must stop here</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Glial substrate-routing route</strong></td>
<td>Same-subject neural and behavioral target, plus a named glia-to-neuron fuel-support observable or perturbation with supplier cell, neuronal sink, fuel object / carrier, and nutrient or learning regime fixed.</td>
<td>A declared glial substrate-routing family improved prediction, recall, or a bounded memory-support readout in that named nutrient or learning regime.</td>
<td>That astrocyte ensemble state was identified, or that one glial fuel route generalizes across lactate, ketone-body, fatty-acid, and apoE / sortilin-dependent lipid delivery.</td>
</tr>
<tr>
<td><strong>Astrocyte-state route</strong></td>
<td>Same-subject neural and behavioral target, plus a named astrocyte-state observable or perturbation aligned to the same recall, stabilization, or fear-state window.</td>
<td>A named astrocyte-state family improved prediction, recall, stabilization, or fear-state decoding in that declared window.</td>
<td>That the responsible whole-brain astrocyte controller was identified, or that astrocyte-state evidence fixed glial fuel routing, clearance control, or one general support state across all tasks and timescales.</td>
</tr>
<tr>
<td><strong>Neurovascular / BBB / pericyte support route</strong></td>
<td>Same-subject neural and behavioral target, plus a named capillary, BBB-exchange, or BBB-transport observable with shared arousal / vascular-driver logging.</td>
<td>A declared vascular-support family reduced one error term or improved one prediction slice under the named physiological regime.</td>
<td>That a generic BBB state was measured, or that the added row directly read out the neuronal variable of interest.</td>
</tr>
<tr>
<td><strong>Clearance / immune / lymphatic route</strong></td>
<td>Same-subject neural or biomarker target, plus a named CSF-mobility, tracer-transport, or sleep-linked efflux route with sleep / time-of-day handling fixed.</td>
<td>A declared transport-side or immune-side route explained incremental variance or changed a bounded physiological readout.</td>
<td>That local microglial control, route-free whole-brain clearance truth, or one universal maintenance controller was identified.</td>
</tr>
<tr>
<td><strong>Bundle comparison rule</strong></td>
<td>Compare the neuron-only baseline, each single added family, and the full bundle under the same subjects, split rule, missingness policy, and common-driver audit.</td>
<td>The bundle improved the declared task under a named availability and regime constraint, beyond the strongest single added row.</td>
<td>That the full bundle proves the minimum required biological configuration or closes U3 by itself.</td>
</tr>
</tbody>
</table>

<ol>
<li>Freeze the <strong>neuron-first baseline</strong>, target object, split unit, and metric bundle before adding any maintenance-state row.</li>
<li>Add <strong>one family at a time</strong> under the same subjects, same sessions, same missingness rule, and same evaluation family.</li>
<li>Name the <strong>direct observable</strong>, <strong>time window</strong>, <strong>spatial unit</strong>, and <strong>route class</strong> for every added family, because local causal perturbation and bounded human proxy do not carry the same claim.</li>
<li>Report the <strong>strongest single added row</strong>, the <strong>full bundle</strong>, and their disagreement / missing-modality behavior under the same split.</li>
<li>Stop the claim at <strong>incremental predictive, stability, or physiological gain</strong> unless the result also survives common-driver controls, out-of-regime checks, and a named abstention boundary.</li>
</ol>
</section>

<div class="note-box">
<strong>Starter EEG datasets are still only the baseline arm of this ladder</strong>
<p>
EEG Motor Movement/Imagery, CHB-MIT, Sleep-EDF, and TUH help you fix the neuron-first baseline, split unit, QC discipline, and leakage checks. By themselves they do not close glial substrate-routing, astrocyte-state, pericyte / BBB support, clearance transport, or other maintenance-state families. Any public maintenance-state claim on this site therefore needs paired support-state data, aligned proxy logs, or a named perturbation route, and it must be compared against the strongest single added family rather than only against the all-in bundle.
</p>
</div>

<div class="note-box">
<strong>A same-subject support-state bundle still needs its own augmentation card</strong>
<p>
The page still had one practical weakness after the family split: it could leave the impression that once several support-state rows are collected in the same subject, the bundle itself is already close to one aligned biological variable. The current primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed that spontaneous multimodal measures contain both <strong>common</strong> and <strong>divergent</strong> cortical structure. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed that simultaneous EEG-PET-MRI can display tightly coupled temporal evolution while still preserving <strong>spatially distinct hemodynamic and metabolic patterns</strong>. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that a major low-frequency global fMRI pattern is substantially coupled to <strong>autonomic physiology</strong>, while <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that about <strong>40%</strong> of gray-matter voxels with significant task BOLD changes exhibited <strong>opposing oxygen-metabolism changes</strong>. Bundle-level gain is real but still conditional: <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a> showed that adding markers can reduce prognostic uncertainty, <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> showed that direct same-sample comparison shrank to <strong>48 patients</strong> with all EEG and fMRI features, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> showed higher <strong>inter-modality disagreement</strong> in minimally conscious or improving patients even as performance improved with more modalities. Row-local stability is separate again: <a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B&oslash;gh et al. (2024)</a> fixed a named repeatability window for a 3 T deuterium route, and <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a> showed reproducible EEG-fMRI connectome relations only under explicitly harmonized simultaneous acquisition. Therefore, this page now requires a <strong>practical support-state augmentation card</strong> before a same-subject bundle is read as more than row addition.
</p>
</div>

<section class="section" id="support-state-augmentation-card">
<h2 class="section-title">A practical support-state augmentation card for dataset bundles</h2>
<table class="data-table">
<thead>
<tr>
<th>Field to log before reading a same-subject bundle strongly</th>
<th>Why this field is necessary</th>
<th>What overread it blocks</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Route class and bridge type</strong></td>
<td>State whether a row is a same-subject human proxy, a same-subject perturbation, a sequential bridge, or a mixed-species causal support row.</td>
<td>Do not read rodent causal support and bounded human proxy rows as interchangeable evidence just because they concern the same family label.</td>
</tr>
<tr>
<td><strong>Effective time window and physiological regime</strong></td>
<td>Log whether rows target the same trial epoch, sleep stage, arousal window, pharmacological state, or multiday stabilization regime.</td>
<td>Do not read co-acquisition or same-session wording as if one support-state sample had been aligned automatically.</td>
</tr>
<tr>
<td><strong>Direct observable and quantity type</strong></td>
<td>Name whether the added row is density, transport, exchange, mobility, flux, metabolism, or an indirect classifier / score.</td>
<td>Do not collapse tracer transport, glucose uptake, BOLD fluctuation, and bounded biomarker efflux into one solved maintenance variable.</td>
</tr>
<tr>
<td><strong>Shared-driver / quantity-bridge audit</strong></td>
<td>Disclose vascular, respiratory, autonomic, motion, drug, and time-of-day covariates, and say whether the bundle established a shared trajectory, a common driver, or a true quantity bridge.</td>
<td>Do not read correlated rows as one biological quantity when the coupling may be driven by arousal or another shared nuisance source.</td>
</tr>
<tr>
<td><strong>Availability slice and missing-modality policy</strong></td>
<td>Report the exact complete-case subset, any imputation or substitution rule, and whether the comparison is same-sample or maximum-available-data.</td>
<td>Do not hide that the bundle result may depend on a much smaller or specially filtered subgroup than the headline cohort.</td>
</tr>
<tr>
<td><strong>Strongest single row and disagreement topology</strong></td>
<td>Compare the best single added family against the full bundle and state where modalities agree, diverge, or change sign.</td>
<td>Do not promote the full bundle if it only repackages the strongest single row or if disagreement is concentrated in the hardest regime.</td>
</tr>
<tr>
<td><strong>Row-local repeatability and transfer window</strong></td>
<td>Name the hardware, sequence, preprocessing, centre, and acquisition window under which each added row is repeatable or portable.</td>
<td>Do not treat one named proxy route as field-ready or cross-centre stable just because it worked once in one harmonized setup.</td>
</tr>
<tr>
<td><strong>Abstention and stopping claim</strong></td>
<td>State what remains latent after the gain, such as controller identity, cell specificity, or out-of-regime failure.</td>
<td>Do not turn bundle improvement into a minimum-biological-configuration claim or a U3 closure claim by default.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>What this card changes in practice</strong>
<p>
On this page, a support-state addition now stays at <strong>family-split augmentation evidence</strong> unless the dataset card logs the fields above and then compares <strong>neuron-first baseline</strong>, <strong>strongest single added row</strong>, and <strong>full bundle</strong> under the same split, availability slice, and abstention rule. If the bundle mixes living-human proxy classes, use the <a href="verification.html#human-proxy-composition-card">Verification: Human Proxy Composition Card</a> alongside the <a href="verification.html#fusion-card">Verification: Fusion Card</a> instead of treating co-acquisition as sufficient.
</p>
</div>
</section>

<section class="section" id="platforms">
<h2 class="section-title">1) Shared infrastructure to establish first</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>OpenNeuro (BIDS-based sharing)</h4>
<p>A platform for sharing BIDS-compliant neuroimaging and electrophysiology datasets, including EEG, MEG, and fMRI. </p>
<a href="https://openneuro.org/" target="_blank" class="btn-action">Open OpenNeuro</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>PhysioNet (biosignals and benchmark culture)</h4>
<p>A public platform for biosignal datasets and related resources, including many standard EEG corpora. </p>
<a href="https://physionet.org/" target="_blank" class="btn-action">Open PhysioNet</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>Human Connectome Project (large-scale human imaging)</h4>
<p>A representative public resource for large-scale human brain imaging data and analysis tools. </p>
<a href="https://www.humanconnectome.org/" target="_blank" class="btn-action">Open HCP</a>
</div>
</div>
</div>

<div class="note-box">
<strong>Reproducibility depends on the full execution chain</strong>
<p>
OpenNeuro and PhysioNet are entry points, but they do not guarantee reproducibility by themselves. First fix the <strong>snapshot / version</strong>, then align it with <strong>BIDS / EEG-BIDS</strong>, fix the reading and conversion path with tools such as <strong>MNE-BIDS</strong>, and finally define the comparison setting with a benchmark harness such as <strong>MOABB</strong> for <strong>within-session / cross-session / cross-subject</strong>. If you mix up repository, loader, and benchmark settings, the same dataset name will still yield incomparable results.
</p>
</div>
</section>

<section class="section" id="starter">
<h2 class="section-title">2) EEG starter pack (start with this from L0 to L1)</h2>
<p>
The following are representative examples of introductory EEG datasets that emphasize ease of use and extensive reference. We focused on practicing the preprocessing pipeline and reaching L0 to L1, and narrowed it down to a range where we can immediately start comparing reproduced baselines.
</p>

<table class="data-table">
<thead>
<tr>
<th>Dataset</th>
<th>What you can do (example)</th>
<th>Link</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>Motor/motor recall classification, preprocessing practice, baseline comparison</td>
<td><a href="https://physionet.org/content/eegmmidb/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>CHB-MIT Scalp EEG</strong></td>
<td>Epileptic seizure detection, event detection, long-term EEG handling</td>
<td><a href="https://physionet.org/content/chbmit/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>Estimating sleep stages, modeling state transitions, handling longitudinal fluctuations</td>
<td><a href="https://physionet.org/content/sleep-edfx/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>TUH EEG Corpus (large scale)</strong></td>
<td>Scaling EEG classification, difficulty in distribution for actual operation, data leak countermeasures</td>
<td><a href="https://www.isip.piconepress.com/projects/tuh_eeg/" target="_blank">TUH EEG</a></td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>Dataset</th>
<th>Good first release</th>
<th>Why this is a good first release</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>Baseline accuracy and preprocessing log for two-class classification</td>
<td>The task setup is simple, so it is easy to build a minimal loop from preprocessing to evaluation. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>Reproduction baseline and exclusion reason log for seizure event detection</td>
<td>It is a good way to learn the practical difficulties of long recordings and event detection, including failure cases. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>Basic baseline for sleep stage classification and confusion matrix of state transitions</td>
<td>It shows not only accuracy but also how state transitions fail, which makes errors easier to interpret. </td>
</tr>
<tr>
<td><strong>TUH EEG Corpus</strong></td>
<td>Reproduction experiment with a small subset and clarifying data division rules</td>
<td>It is more important to lock down leak prevention and split rules first than to process the full corpus from the start. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="generalization-families">
<h2 class="section-title">2.5) The same score means different things across generalization settings</h2>
<p>
This is one of the current weak points of the site. `within-session`, `cross-session`, `cross-subject`, and `adaptation` may all report "classification accuracy," but they answer different questions about generalization. The official MOABB documentation also implements them as separate evaluation classes, and in the 5-day MI dataset of Ma et al. (2022), the average subject-specific accuracy dropped from <strong>within-session 68.8%</strong> to <strong>cross-session 53.7%</strong>, then recovered to <strong>cross-session adaptation 78.9%</strong> when a small amount of target-session data was used. Therefore, this site will no longer list scores alone; it will also state <strong>what was held out, what was allowed to vary, and what remains unresolved</strong>.
</p>

<table class="data-table">
<thead>
<tr>
<th>Evaluation family</th>
<th>What is held out</th>
<th>What this supports</th>
<th>What not to overread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>within-session</strong></td>
<td>Folds within the same subject and the same session. </td>
<td>It can show whether classes separate under the same-day, same-setup condition and whether preprocessing plus baseline modeling work at all. </td>
<td>Do not treat this as evidence of cross-day robustness or deployable decoding. </td>
</tr>
<tr>
<td><strong>cross-session</strong></td>
<td>A different session or day from the same subject. </td>
<td>It can show how long subject-specific features persist across days and how sensitive they are to state changes and re-setup effects. </td>
<td>Do not read this as subject-independent generalization or zero-recalibration operation. </td>
</tr>
<tr>
<td><strong>cross-subject</strong></td>
<td>One or more entire subjects. </td>
<td>It can show whether population-level shared structure exists and how far a cold-start decoder might go at initial installation. </td>
<td>Do not equate this score with a decoder optimized for a specific individual. </td>
</tr>
<tr>
<td><strong>cross-session adaptation</strong></td>
<td>Another session is held out, then a small amount of target-session data is used for recalibration. </td>
<td>It can show how much performance is recoverable through recalibration and how much room there is for operational adaptation. </td>
<td>Do not describe this as a stable decoder that worked from the beginning without adaptation. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Why this distinction matters scientifically</strong>
<p>
Musall et al. (2019) showed that neural activity during tasks can be strongly dominated by uninstructed movements. A high same-day score may therefore reflect not only a task variable but also the behavioral state or artifact structure of that day. Furthermore, Wilson et al. (2025) showed that long-term BCI operation accumulates changes in neural activity and requires <strong>frequent recalibration</strong>. In other words, even for the same subject, <strong>short-term resolution</strong>, <strong>cross-day tolerance</strong>, and <strong>long-term operation</strong> are different barriers.
</p>
</div>

<div class="note-box">
<strong>2026-03-22 addendum: evaluation family is not yet temporal validity</strong>
<p>
The practical gap on this page was subtler than simple split naming. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> showed over a <strong>10-hour EEG day</strong> that movement-related decoding changes enough to motivate <strong>adaptive decoders</strong>, <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a> showed that <strong>latent-dynamics alignment</strong> can stabilize BCI performance but is still a rescue route for interface instability, <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> showed up to <strong>one month of unsupervised recalibration</strong> in online cursor iBCI use, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> showed that a speech neuroprosthesis can be impressively fast while still remaining a <strong>participant-specific communication route</strong> rather than a generic temporal-validity benchmark. Therefore, on this site, <strong>cross-session</strong>, <strong>adaptation</strong>, and <strong>online use</strong> are still not enough by themselves. A temporal claim also has to name <strong>state annotation</strong>, <strong>fixed decoder interval</strong>, <strong>recalibration burden</strong>, and <strong>transfer ceiling</strong>. The operational rule is <a href="verification.html#temporal-validity-card">Verification: Temporal Validity Card</a>, with technical background in <a href="wiki/state-trait-and-drift.html">Wiki: state, trait, and drift</a>.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>If the result is reported as...</th>
<th>You still have to disclose</th>
<th>Stopped claim if missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cross-session</strong></td>
<td>State annotation, fixed decoder interval, and whether the setup was reattached, re-referenced, or otherwise changed.</td>
<td>Read only as cross-day tolerance under named conditions, not as durable decoding.</td>
</tr>
<tr>
<td><strong>cross-session adaptation</strong></td>
<td>How much target-session data was used, when recalibration happened, and what the pre-adaptation score was.</td>
<td>Do not promote to fixed-decoder stability or low-burden deployment.</td>
</tr>
<tr>
<td><strong>longitudinal / chronic use</strong></td>
<td>Fixed decoder interval, recalibration burden, failure / fallback mode, and participant / site / task transfer ceiling.</td>
<td>Do not promote to generic long-term robustness or deployability.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>2026-03-18 addendum: fix the route behind the same score</strong>
<p>
Even when a within-session score is high, it can still be explained by eye-movement confounds shown by <a href="https://doi.org/10.1523/ENEURO.0401-17.2018" target="_blank">Mostert et al. (2018)</a>, the EMG route shown by <a href="https://doi.org/10.1088/1741-2560/2/4/014" target="_blank">McFarland et al. (2005)</a>, post-onset auditory feedback shown by <a href="https://doi.org/10.1038/s42256-024-00837-5" target="_blank">Chen et al. (2024)</a>, identity confounding shown by <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>, time-robust resting-state fingerprints shown by <a href="https://doi.org/10.1016/j.patcog.2020.107381" target="_blank">Wang et al. (2020)</a> and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a>, or subject-driven EEG variation summarized by <a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">Gibson et al. (2022)</a>. For that reason, this site now overlays the <a href="verification.html#specificity-shortcut-card">Verification: Specificity &amp; Shortcut Card</a> on dataset cards and baseline results, fixing <strong>plausible nuisance routes</strong>, <strong>auxiliary channels such as EOG / EMG / behavior / audio / metadata</strong>, <strong>nuisance-only baselines</strong>, <strong>fingerprint audit</strong>, <strong>nuisance-regime hold-outs</strong>, and <strong>the claim that must stop here</strong>.
</p>
</div>

<div class="note-box">
<strong>2026-03-18 addendum: acquisition distribution is also an independent shortcut family</strong>
<p>
This site previously stopped more clearly at <strong>subject / session fingerprint</strong> than at <strong>setup effects</strong>. That was too weak. <a href="https://doi.org/10.1088/1741-2552/aacfe4" target="_blank">Hu et al. (2018)</a> showed that the measured scalp potential itself changes with reference montage and electrode setup, <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017)</a> showed that EEG recordings vary not only by subject and session but also by recording system, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a> showed that cross-dataset EEG decoding is degraded by environmental variability such as amplifier, cap, sampling rate, and filtering, <a href="https://doi.org/10.1002/brb3.2789" target="_blank">Ceballos-Villegas et al. (2022)</a> explicitly modeled multinational batch effects across studies and devices, and <a href="https://doi.org/10.1016/j.brainresbull.2024.110906" target="_blank">Dong et al. (2024)</a> showed that even comparative study across different channel locations needs explicit harmonization. Therefore, this site now treats <strong>site / device / reference system / electrode layout / protocol distribution</strong> as an independent shortcut family rather than as harmless metadata.
</p>
</div>

<div class="note-box">
<strong>2026-03-25 addendum: benchmark governance is part of the benchmark</strong>
<p>
The next practical weakness on this page was that <strong>split / leak / harmonization</strong> were visible, while <strong>benchmark governance</strong> could still be treated as administrative detail. The current primary and official sources do not support that shortcut. The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) homepage</a> states that the original challenge preprint became outdated during execution and that the website plus starter kit should be treated as current. The official <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> require disclosure of <strong>additional pretraining datasets</strong>, <strong>pretrained models / fine-tuning method</strong>, <strong>code submission at inference stage</strong>, and a <strong>single-GPU 20 GB</strong> inference budget. The official <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> then disclosed that <strong>Challenge 2 samples had not been randomized</strong>, allowing contiguous-trial same-subject structure to affect what the ranking meant and forcing separate awards. That warning is aligned with benchmark-side primary sources: <a href="https://arxiv.org/abs/2508.17742" target="_blank">Xiong et al. (2025)</a> argued that inconsistent evaluation protocols make cross-model EEG-FM comparisons unreliable, and <a href="https://arxiv.org/abs/2601.17883" target="_blank">Liu et al. (2026)</a> showed across <strong>12 open-source foundation models</strong> and <strong>13 datasets</strong> that ranking depends materially on transfer regime and benchmarking choices. Therefore, when this site reads a leaderboard, challenge result, or foundation-model benchmark, the card must also name <strong>benchmark version</strong>, <strong>split / randomization rule</strong>, <strong>hidden grouping structure</strong>, <strong>extra-data / pretrained-checkpoint policy</strong>, <strong>adaptation regime</strong>, <strong>inference-stage restrictions</strong>, and <strong>later organizer postmortems</strong>. If those fields are missing, we treat the result only as a qualified benchmark snapshot, not as a stable measure of portable EEG generalization.
</p>
</div>

<div class="note-box">
<strong>2026-03-31 addendum: benchmark name is not yet the benchmark object</strong>
<p>
The next practical weakness was narrower. Even after benchmark governance became visible, a reader could still talk as if the benchmark name fixed the <strong>predicted object</strong>, <strong>independent prediction unit</strong>, <strong>grouped hold-out unit</strong>, <strong>adaptation regime</strong>, and <strong>operations budget</strong>. The current primary and official sources do not support that shortcut. The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) homepage</a> separates <strong>Challenge 1</strong> response-time regression from <strong>Challenge 2</strong> subject-level externalizing prediction, the official <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> and <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a> add an <strong>inference-only code-submission workflow</strong> under a <strong>single-GPU 20 GB</strong> budget, <a href="https://doi.org/10.1038/s41597-022-01647-1" target="_blank">Ma et al. (2022)</a> use one five-session motor-imagery dataset to separate <strong>within-session</strong>, <strong>cross-session</strong>, and <strong>cross-session adaptation</strong>, <a href="https://arxiv.org/abs/2601.17883" target="_blank">Liu et al. (2026)</a> separate <strong>leave-one-subject-out cross-subject evaluation</strong> from <strong>within-subject few-shot calibration</strong>, and <a href="https://arxiv.org/abs/2603.02268" target="_blank">Lahiri et al. (2026)</a> show that <strong>six benchmark inconsistencies</strong> can reverse rankings on identical datasets by up to <strong>24 percentage points</strong>. Therefore, on this site, a dataset or leaderboard name is still too coarse until the object / unit / budget matrix is disclosed explicitly.
</p>
</div>

<div class="note-box">
<strong>2026-04-02 addendum: setup diversity is not yet physiology-equivalent transfer</strong>
<p>
The next weak point on this page was different from benchmark governance. A dataset or benchmark card could already expose <strong>site / device / reference / layout diversity</strong> and still leave a reader with the impression that a setup-agnostic foundation model had already solved <strong>physiology-preserving transfer</strong>. The current primary literature does not support that shortcut. <a href="https://arxiv.org/abs/2507.14141" target="_blank">Han et al. (2025)</a> target <strong>channel-permutation equivariance</strong>, <a href="https://arxiv.org/abs/2510.12515" target="_blank">Chen et al. (2025)</a> target <strong>coordinate-based adaptation across heterogeneous devices and more than 150 layouts</strong>, and <a href="https://arxiv.org/abs/2510.21585" target="_blank">El Ouahidi et al. (2025)</a> push setup-agnostic pretraining to more than <strong>60,000 hours</strong> from <strong>92 datasets</strong> and <strong>25,000 subjects</strong>. Those papers advance <strong>recording-frame compatibility</strong>. They still do not prove that different montages, coordinate routes, and reference families already preserve one shared <strong>physiology-side representation</strong>. <a href="https://arxiv.org/abs/2602.17251" target="_blank">Ma et al. (2026)</a> then show that strong EEG foundation models can still generalize poorly when <strong>subject-level supervision is limited</strong> unless extra adaptation structure is added. Therefore, this page now treats <strong>setup diversity</strong>, <strong>coordinate route</strong>, <strong>reference family</strong>, <strong>omitted-channel policy</strong>, and <strong>label-limited adaptation burden</strong> as separate dataset / benchmark-card fields rather than one merged claim of portable generalization.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Case</th>
<th>What the named benchmark or dataset actually predicts</th>
<th>What still has to be frozen separately</th>
<th>Safe ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Challenge 1</strong><br>official homepage + rules</td>
<td><strong>Trial-level</strong> response-time regression from the CCD task.</td>
<td>The <strong>trial</strong> is the scoring unit, but grouped subject structure and the <strong>inference-only single-GPU 20 GB</strong> budget still have to be disclosed separately.</td>
<td>A named transfer benchmark under a fixed operations budget, not a general EEG decoder verdict.</td>
</tr>
<tr>
<td><strong>EEG Challenge 2</strong><br>official homepage + leaderboard</td>
<td><strong>Subject-level</strong> externalizing-factor prediction from EEG across multiple paradigms.</td>
<td>The <strong>subject</strong> is the natural independent unit, and the organizer postmortem shows that hidden contiguous-trial grouping can still change what the benchmark measured.</td>
<td>A subject-invariance benchmark attempt whose meaning remains contingent on grouping policy, not proof that subject invariance is solved.</td>
</tr>
<tr>
<td><strong>Ma et al. (2022)</strong><br>five-session motor-imagery dataset</td>
<td>The same raw dataset supports <strong>within-session</strong>, <strong>cross-session</strong>, and <strong>cross-session adaptation</strong> evaluation families.</td>
<td>The dataset name alone does not tell you whether <strong>target-session data</strong> were used, when recalibration happened, or what the <strong>pre-adaptation score</strong> was.</td>
<td>A useful session-shift practice board, not automatic fixed-decoder durability.</td>
</tr>
<tr>
<td><strong>Liu et al. (2026)</strong><br>foundation-model benchmark matrix</td>
<td>Cross-model comparison across <strong>13 EEG datasets</strong> and <strong>nine paradigms</strong> under multiple transfer settings.</td>
<td>The paper explicitly separates <strong>leave-one-subject-out</strong> transfer from <strong>within-subject few-shot calibration</strong>, so hold-out unit and adaptation regime still have to be named separately.</td>
<td>A transfer-regime comparison board, not one portable score of EEG generalization.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Site rule from this section</strong>
<p>
From this section onward, dataset cards and baseline results must report at least <strong>(1) evaluation family</strong>, <strong>(2) benchmark object plus independent prediction unit</strong>, <strong>(3) the independent hold-out unit</strong>, <strong>(4) raw-recording / window ancestry</strong>, <strong>(5) subject / session / site / device / reference-system / electrode-layout disjointness together with metadata-only baselines</strong>, <strong>(6) the channel-map / coordinate-route / reference-family / omitted-channel / sample-rate / filter harmonization log</strong>, <strong>(7) whether target-session, target-subject, or target-site data were used</strong>, <strong>(8) recalibration amount and timing or extra label budget</strong>, <strong>(9) for leaderboard or challenge claims, benchmark provenance including version, split / randomization rule, hidden grouping, extra-data / checkpoint policy, inference-stage restrictions or operations budget, and postmortem disclosures</strong>, and <strong>(10) a stopping claim</strong>. If the claim spans more than one session or day, it must additionally disclose the site's <strong>Temporal Validity</strong> fields: <strong>state annotation</strong>, <strong>fixed decoder interval</strong>, <strong>recalibration burden</strong>, and <strong>transfer ceiling</strong>. Scores without this context will be treated as limited L1 decode results, fingerprint-unresolved / acquisition-distribution-unresolved classifiers, or benchmark-object-unresolved / benchmark-governance-unresolved leaderboards rather than evidence of long-term stability or deployability.
</p>
</div>

<div class="note-box">
<strong>2026-03-25 addendum: metric semantics are part of the benchmark</strong>
<p>
The next practical weakness on this page was that <strong>split / leak / harmonization</strong> and <strong>benchmark governance</strong> were visible, while <strong>metric semantics</strong> could still hide behind one headline number. The primary literature does not support that shortcut. <a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp; Rehmsmeier (2015)</a> showed why <strong>precision-recall</strong> views can be more informative than ROC summaries under strong class imbalance. In seizure tasks, <a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">Roy et al. (2021)</a> and <a href="https://doi.org/10.1097/WNP.0000000000000709" target="_blank">Scheuer et al. (2021)</a> show that practical evaluation still turns on <strong>sensitivity</strong>, <strong>false alarms per hour or day</strong>, event-overlap logic, and latency rather than plain accuracy, while <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">Segal et al. (2023)</a> show that <strong>false-alarm control</strong> is itself a design target in seizure prediction rather than an afterthought. In sleep staging, <a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">Sun et al. (2017)</a> used <strong>Cohen's kappa</strong> and showed that imbalance in stage proportions changes performance estimates, while <a href="https://doi.org/10.7554/eLife.70092" target="_blank">Vallat &amp; Walker (2021)</a> show that pooled performance can still hide especially weak <strong>N1-stage</strong> agreement. Therefore, on this site, a dataset or benchmark card must now also disclose a <strong>task-matched metric bundle</strong>, not only a split and a score.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Task family</th>
<th>Minimum metric bundle on this site</th>
<th>Overread to block</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cue-locked classification / decoding</strong></td>
<td>Balanced accuracy or macro-F1, confusion matrix, subject-wise aggregation, and calibration / abstention if probabilities are output.</td>
<td>Do not let one accuracy number hide minority-class collapse or confidence miscalibration.</td>
</tr>
<tr>
<td><strong>Seizure detection / forecasting</strong></td>
<td>Event sensitivity or recall, false alarms per hour or per day, event-overlap rule, detection / warning latency when relevant, and calibration if thresholds or alarms are used.</td>
<td>Do not let accuracy, AUROC, or one threshold-free summary stand in for clinically usable alarm behavior.</td>
</tr>
<tr>
<td><strong>Sleep staging</strong></td>
<td>Cohen's kappa or macro-F1, per-stage recall / F1, and a confusion matrix that keeps minority stages visible.</td>
<td>Do not let pooled accuracy hide weak N1 or transition-stage performance.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dataset-audit">
<h2 class="section-title">3) Audit to avoid overestimating starter data</h2>
<p>
The above four cases are very useful as a practice base for L0-L1, but they are not the ground truth for directly verifying the strong claims of EEG source imaging and WBE. What is needed here is not a dichotomy of ``usable/unusable,'' but rather a fixation on <strong>which claims can be supported</strong>.
</p>

<div class="note-box">
<strong>The last two columns in this section reflect this site's operating logic</strong>
<p>
The <strong>stopping claims</strong> and <strong>minimum operational rules</strong> in the table below are operational boundaries drawn from what is directly observed and annotated in the official dataset descriptions and primary literature. In other words, they are not claims explicitly made by the dataset providers; they are site rules derived from <strong>annotation provenance and time fidelity</strong>.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Dataset</th>
<th>Things that are easy to verify now</th>
<th>Still difficult to verify</th>
<th>Minimum precautions</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>Since it is a cue-locked task of 64ch, 160Hz, and 109 people, it is suitable for practicing preprocessing, subject-based split, and simple baseline comparison. </td>
<td>Without individualized MRI, electrode coordinates, and invasive ground truth, claims of improved ESI accuracy and deep reconstruction cannot be audited. </td>
<td>Since the task involves presenting left/right/up/down cues on the screen, we will check for inclusion of line of sight, myoelectricity, and cue-locked artifacts, and fix the split for each subject. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>Suitable for learning long-term EEG, seizure event detection, and logging of missing and exclusion reasons. </td>
<td>Since it strongly depends on the clinical conditions of children, intractable epilepsy, and drug withdrawal, it cannot be used as a general-purpose benchmark for general recognition or source imaging. </td>
<td>Split in case units and handle while retaining the gap and montage summary between records. The disparity between seizures and seizures will also be clarified first. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>It is suitable for learning how to handle state transitions, sleep stage classification, and longitudinal fluctuations using whole-night PSG. </td>
<td>The primary EEG is Fpz-Cz / Pz-Oz 2-lead, 100 Hz, so it is not a benchmark for spatial resolution or source imaging. </td>
<td>The labels are manual scoring based on the Rechtschaffen &amp; Kales standard, so when comparing with new sleep stage studies, we will clearly indicate the label correspondence. </td>
</tr>
<tr>
<td><strong>TUH EEG Corpus</strong></td>
<td>Suitable for learning the difficulties of real-world distribution such as large scale, clinical noise, repeated sessions, and physician reports. </td>
<td>It is not suitable for direct validation of source imaging improvements as it is not a controlled biophysical benchmark due to large variations in channel number and clinical conditions. </td>
<td>Fix patient/session unit split, fixed channel subset, montage normalization, and text leakage prevention when using reports first. </td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>Dataset</th>
<th>Label/Event origin</th>
<th>Time fidelity</th>
<th>Claim to stop here</th>
<th>Minimum operational rules</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td><code>.event</code> and annotation channel T0/T1/T2 indicate cue-locked onset of real/imagined motion. </td>
<td>Cue-onset level for 160 Hz recording. </td>
<td>Do not promote open-ended thought decoding or subject-independent semantic readout. </td>
<td>Split by subject + run and audit visual cue and myoelectric/ocular contributions separately. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>The summary and <code>.seizure</code> annotations for each case mark seizure intervals during long-term recording. In addition, <code>chb21</code> is the same subject as <code>chb01</code>. </td>
<td>Expert interval annotation, gap between files also remains. </td>
<td>Do not treat this as gap-free continuous monitoring or count cases as if they were independent subjects. </td>
<td>Split by subject and case chronology rather than by file, and keep gap plus montage summaries in the runbook. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>Comes with an R&amp;K hypnogram by a well-trained technician and a 1 Hz event marker. </td>
<td>The whole-night stage annotation is coarse, and even though the EEG is 100 Hz, the marker is 1 Hz. </td>
<td>Stop claiming that sub-second event onset and AASM equivalent labels are self-evident. </td>
<td>If you split by subject-night and map from R&amp;K to AASM, specify the mapping rule. </td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>TUH has a patient/session hierarchy and a clinician report <code>.txt</code>, while TUSZ goes through a selection including report keyword search and automatic triage. </td>
<td>Clinical label at session/file level and expert seizure annotation at some subset. </td>
<td>Do not write report-assisted labels as if they were pure EEG-only benchmark accuracy. </td>
<td>Require patient / session unit splits and a <strong>report-usage flag</strong>, and do not feed report text into signal-only evaluation. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>The most important site rule to add now</strong>
<p>
When introducing starter data, always include <strong>(1) label provenance</strong>, <strong>(2) time granularity</strong>, <strong>(3) clock domain plus stream-alignment rule</strong>, <strong>(4) timing-validation class</strong>, <strong>(5) event semantics</strong>, <strong>(6) independent split unit</strong>, <strong>(7) acquisition-distribution summary plus harmonization policy</strong>, and <strong>(8) stopping claim</strong>. A dataset card that does not include this will be considered insufficient as a practical guide for L0.
</p>
</div>

<div class="note-box">
<strong>BIDS is a requirement, but not a ground truth</strong>
<p>
BIDS/EEG-BIDS is important, but it alone cannot prove the validity of source imaging or the comparability of cross-dataset decoding. The BIDS specification itself also requires <code>EEGReference</code>, <code>SamplingFrequency</code>, <code>SoftwareFilters</code>, and if <code>*_electrodes.tsv</code> is issued, <code>*_coordsystem.json</code> is also required. However, this is a condition that makes it possible for a third party to trace the incident, not a condition that allows the true source to be known or that automatically harmonizes reference mismatch, electrode-layout mismatch, and device / filter differences across cohorts.
</p>
</div>

<div class="note-box">
<strong>If you want to claim ESI improvement, you need a different chain of evidence</strong>
<p>
Please provide at least the following four points.
</p>
<ul>
<li><strong>Individual anatomy:</strong> Individual MRI/CT or EEG-BIDS recordings with digitized electrode positions and <code>*_electrodes.tsv</code> / <code>*_coordsystem.json</code></li>
<li><strong>Forward model audit:</strong> Head model and skull-conductivity sensitivity analysis</li>
<li><strong>External standards:</strong> Ground truth such as phantoms, simultaneous invasive recording, intracranial stimulation, or TMS-EEG</li>
<li><strong>Uncertainty:</strong> Report not only point estimates but also localization errors and interval estimates</li>
</ul>
</div>
</section>

<section class="section" id="validation-ladder">
<h2 class="section-title">4) If you want to dig deeper into source imaging, divide the data into three stages</h2>
<p>
The weak point of this page was that it only stopped by saying, ``Starter data is not a direct benchmark for source imaging,'' but then it was weak in deciding what to choose next. Here, we divide the data into three levels depending on the strength of the argument.
</p>

<table class="data-table">
<thead>
<tr>
<th>stage</th>
<th>Representative data</th>
<th>Supported argument</th>
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>A: Practice table</strong></td>
<td>EEG Motor Movement/Imagery, CHB-MIT, Sleep-EDF, TUH EEG</td>
<td>L0-L1 reproducibility analysis, QC, split design, baseline comparison</td>
<td>ESI localization error improvement, deep source claim, strong WBE-oriented reconstruction claim</td>
</tr>
<tr>
<td><strong>B: Reconstruction with anatomical constraints</strong></td>
<td>Records including <code>*_electrodes.tsv</code> / <code>*_coordsystem.json</code> for individualized MRI, digitized electrodes, and EEG-BIDS</td>
<td>Audit of forward model, comparison of reconstruction near the cortical surface, sensitivity analysis of electrode placement and conductivity assumptions</td>
<td>Deep source accuracy guarantee without direct ground truth, generalized unique recovery claim</td>
</tr>
<tr>
<td><strong>C: Direct validation</strong></td>
<td>Localize-MI (Mikulan et al., 2020), scalp EEG with intracranial stimulation, simultaneous HD-EEG/SEEG, presurgical cohort with postoperative outcome</td>
<td>Named validation-class audit: localization error against known stimulation sites, concordance with simultaneous invasive recording, or clinical concordance against postoperative outcome</td>
<td>Universal performance guarantee beyond task/cohort/montage</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Stage C is not one box</strong>
<p>
On this site, you should still write which C-stage validation class you used:
</p>
<ul>
<li><strong>stimulation ground truth:</strong> asks localization error against a known stimulation site and time (Mikulan et al., 2020; Unnwongse et al., 2023).</li>
<li><strong>simultaneous invasive recording:</strong> asks concordance with concurrent SEEG/ECoG under the same event regime (Hao et al., 2025).</li>
<li><strong>postsurgical outcome / clinical concordance:</strong> asks whether the source estimate points toward clinically relevant tissue, not whether the source was uniquely observed (Birot et al., 2014).</li>
</ul>
</div>

<div class="note-box">
<strong>The most important thing now is the C stage public benchmark</strong>
<p>
Localize-MI by Mikulan et al. (2020) is a rare data resource that exposes intracerebral stimulation with 256ch scalp EEG and stereo-EEG, allowing source imaging to be directly audited against “known stimulation locations.” Hao et al. (2025) reported average localization errors of 14.07 mm for ictal ESI and 17.38 mm for interictal ESI in 29 simultaneous HD-EEG/SEEG cases, indicating that source power and source depth greatly affect accuracy. Jahromi et al. (2026) then added a <strong>3D-printed pediatric deep-source phantom</strong>, showing that even phantom validation is not one universal board once <strong>deep epileptic source class</strong> and <strong>geometry</strong> are changed. Therefore, if you want to improve your source imaging, you need not only a C-level benchmark, but also a named C-stage validation class rather than an A-level starter dataset alone.
</p>
</div>

<div class="note-box">
<strong>High density is no longer the only credible route, but it is still not a solver-free shortcut</strong>
<p>
One remaining simplification on this page was to make the entrance sound too close to <strong>HD-EEG is the serious route and low-density EEG is the weak route</strong>. The current primary literature is narrower than that. <a href="https://doi.org/10.1016/j.clinph.2023.08.009" target="_blank">Horrillo-Maysonnial et al. (2023)</a> showed that a targeted <strong>33-36-electrode</strong> montage reached <strong>54/58 sublobar concordance (93%)</strong> against an <strong>83-electrode</strong> HD montage, but still showed larger peak-vertex distance for <strong>tangential generators</strong>. <a href="https://doi.org/10.1016/j.clinph.2025.04.009" target="_blank">Rong et al. (2025)</a> then showed that a DeepSIF-based approach stayed comparatively stable from <strong>75 to 16 electrodes</strong>, with average spatial dispersions of <strong>7.9/9.0 mm</strong> versus <strong>21.9/28.1 mm</strong> for sLORETA and <strong>20.0/28.9 mm</strong> for LCMV. But these papers do not erase the direct-validation ceiling. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> showed that coverage geometry and conductivity assumptions still move localization error in direct validation, and <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> showed that ictal and interictal ESI differed (<strong>14.07 ± 4.62 mm</strong> versus <strong>17.38 ± 4.16 mm</strong>) and that <strong>source depth</strong> and <strong>spike power</strong> still matter. Therefore, this site no longer treats <strong>high density</strong> versus <strong>low density</strong> as the right first split. The safer split is <strong>named montage / coverage policy + inverse family + source regime + validation class</strong>.
</p>
</div>

<div class="note-box">
<strong>Postoperative outcomes can be used, but should not be equated with ground truth</strong>
<p>
In a systematic review by Mouthaan et al. (2019), the summary sensitivity of electric source imaging in presurgical epilepsy was 82% and specificity was 53%. In other words, although postoperative outcomes and SOZ concordance are useful external criteria, source imaging itself cannot be fixed as the true value. Even at the C stage, what you can say now is ``How far has the error been reduced with this benchmark?'', not ``I was able to uniquely read the source in my brain.''
</p>
</div>

<div class="note-box">
<strong>Practical reading</strong>
<p>
The first question when selecting data is not ``what is interesting?'' but <strong>what level of argument do you want to support this time</strong>? Level A is sufficient for practicing L0-L1. If you want to proceed with claiming improvements in source imaging, please put your claim on hold unless you audit the head model in stage B and take direct validation in stage C. If you do proceed to solver comparison, the next section fixes what has to stay the same across methods before any leaderboard is accepted.
</p>
</div>
</section>

<section class="section" id="inverse-benchmark-board">
<h2 class="section-title">4.5) Inverse-problem benchmark board: compare error questions, not solver names</h2>
<p>
The weakness of this page after the 2026-03-18 validation-class update was that it could still let a reader jump from ``we used C-stage data'' to ``solver X won.'' That is too weak. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">Michel &amp; Brunet (2019)</a> describe ESI as a pipeline rather than a single algorithm, but the current literature is stricter still. <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a> expose a <strong>probabilistic focal-support family</strong>, <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025)</a> expose a <strong>sparse debiased-inference family</strong>, and <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> target <strong>extended-source reconstruction</strong>. Those papers do not return the same target object or the same uncertainty object. <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">Pascarella et al. (2023)</a> then showed on an in-vivo focal-source benchmark that ten methods differ not only in best localization error but also in sensitivity to regularization and montage density, while <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>, <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a>, and <a href="https://doi.org/10.1016/j.compbiomed.2026.111449" target="_blank">Jahromi et al. (2026)</a> show that direct-validation boards themselves differ by stimulation class, simultaneous invasive reference, and deep-source phantom geometry. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> and <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026)</a> further show that forward-model uncertainty is a separate audit rather than a property inherited from a nicer inverse map. Therefore, this site now treats inverse-problem comparison as a board with five fixed axes: <strong>validation class</strong>, <strong>source regime / target object</strong>, <strong>inverse family / uncertainty object</strong>, <strong>same-geometry controls</strong>, and <strong>sensitivity sweep</strong>.
</p>

<div class="note-box">
<strong>Inverse family is not just a solver style label</strong>
<p>
This page now has to stop another shortcut explicitly. A <strong>posterior-support map</strong>, a <strong>debiased sparse interval</strong>, and an <strong>extended-source overlap estimate</strong> are not three visualizations of one identical hidden object. <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a> return posterior support for focal alternatives, <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025)</a> return debiased estimation / inference for sparse spatial-temporal sources, and <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> return uncertainty-aware <strong>extended-source</strong> reconstructions. Therefore, a benchmark on this site must name not only the board, but also which <strong>inverse family</strong> was used, what <strong>target object</strong> it aimed to recover, and what <strong>uncertainty object</strong> it actually returned.
</p>
</div>

<div class="note-box">
<strong>Centre error and source extent are different benchmark objects</strong>
<p>
Another shortcut still had to be blocked here. A benchmark can be “directly validated” and still score only the <strong>geometric center</strong> of a source. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> explicitly target <strong>extended-source reconstruction</strong> rather than focal-center localization. <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> likewise note that their <strong>ECD</strong>-based distance comparison neglects the spatial extent of the seizure-onset and irritative zones, and argue that future localization work should incorporate <strong>source extent</strong> in addition to geometric center. Therefore, a solver that wins a focal-site distance board is not automatically the best method for distributed, extended, or propagation-rich sources, and a public benchmark on this site must state whether it scores <strong>centre</strong>, <strong>extent</strong>, <strong>overlap</strong>, or <strong>propagation pattern</strong>.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Benchmark question</th>
<th>Keep fixed across methods</th>
<th>Primary metric to publish</th>
<th>What not to overread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Focal-source localization against known stimulation site</strong></td>
<td>Same raw recording, event window, electrode coordinates, head model, conductivity sweep, source space, and bad-channel mask.</td>
<td>Distance to known stimulation site/time, plus spread across conductivity and regularization settings.</td>
<td>Do not crown a universal solver for extended or distributed sources from a focal-source board alone.</td>
</tr>
<tr>
<td><strong>Concordance with simultaneous SEEG/ECoG under the same event</strong></td>
<td>Same event definition, same reference montage, same source-depth stratification, same preprocessing, and same concordance rule.</td>
<td>Distance or overlap to invasive reference together with source depth and source power strata.</td>
<td>Do not read concordance as direct ground truth for all generators, especially low-amplitude or deep activity.</td>
</tr>
<tr>
<td><strong>Clinical concordance / postsurgical outcome</strong></td>
<td>Same SOZ/resection definition, same outcome window, same blinding rule, and same patient inclusion criteria.</td>
<td>Sensitivity/specificity or concordance against clinical outcome, clearly separated from localization error.</td>
<td>Do not relabel surgical concordance as precise source-localization ground truth.</td>
</tr>
<tr>
<td><strong>Extended-source reconstruction or multimodal-prior reconstruction</strong></td>
<td>Same definition of source extent, same prior source, same anatomical constraints, and the same focal-versus-extended evaluation split.</td>
<td>Extent overlap or reconstruction error for distributed sources, plus the gain from the added prior.</td>
<td>Do not compare an extended-source method only on a focal-source leaderboard and call it inferior in general.</td>
</tr>
<tr>
<td><strong>Inverse-family comparison under one named board</strong></td>
<td>Same validation class, same raw data, same geometry, same source regime, and an explicit statement of whether each method returns posterior support, sparse debiased intervals, focal centres, or source extent / overlap.</td>
<td>Family-typed result table: target object, uncertainty object, primary board metric, and the spread induced by conductivity / hyperparameter sweeps.</td>
<td>Do not collapse a probabilistic focal family, a sparse debiased family, and an extended-source family into one shared winner or one generic “better ESI” claim.</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>If MNE / beamformer / Champagne disagree</th>
<th>What to publish now</th>
<th>Safe reading on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td>Ranking flips when skull conductivity, head model, or electrode geometry is perturbed.</td>
<td>Show the family-specific ranking under the full sensitivity sweep instead of only the best run.</td>
<td>Method-conditioned improvement in a bounded geometry regime, not a solver winner in general.</td>
</tr>
<tr>
<td>A method wins only at one hand-tuned regularization point.</td>
<td>Publish the localization-error curve or interval across the tested hyperparameter range.</td>
<td>Best-case performance only; robustness remains unresolved.</td>
</tr>
<tr>
<td>Dense montages reduce dispersion but not localization error.</td>
<td>Report localization error and spatial dispersion separately.</td>
<td>Better concentration of the estimate, not automatic improvement in true-source accuracy.</td>
</tr>
<tr>
<td>Deep and superficial sources behave differently.</td>
<td>Stratify results by source depth rather than pooling into one mean.</td>
<td>Conditional detectability only; do not generalize to deep sources as a whole.</td>
</tr>
<tr>
<td>A focal-source board and an extended-source board favor different families.</td>
<td>Keep separate leaderboards for focal, sparse, and extended-source tasks.</td>
<td>Source-regime-specific strength, not a contradiction that can be collapsed into one number.</td>
</tr>
<tr>
<td>Probabilistic focal support, sparse debiased inference, and extent-aware reconstruction return different uncertainty objects.</td>
<td>Publish the family label, target object, and uncertainty object beside the main score instead of hiding them in Methods.</td>
<td>Board-specific, family-specific evidence only; do not read disagreement as generic noise around one common truth object.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Site rule from this section</strong>
<p>
A public inverse-problem comparison on this site must now disclose at least <strong>(1) validation class</strong>, <strong>(2) source regime and target object (focal-centre / sparse / extended / propagation-aware)</strong>, <strong>(3) inverse family plus the uncertainty object it returns</strong>, <strong>(4) same-geometry controls including montage / coverage policy</strong>, <strong>(5) sensitivity sweep over conductivity and key hyperparameters</strong>, <strong>(6) inter-method disagreement summary</strong>, and <strong>(7) the claim that must stop here</strong>. Without these fields, a result will be treated as a method illustration or lab-specific pipeline note, not as a reusable benchmark.
</p>
</div>
</section>

<section class="section" id="benchmark-mindset">
<h2 class="section-title">5) Checklist that does not end with just “there is data”</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>Version fixed:</strong>Does OpenNeuro snapshot, PhysioNet version, DOI, acquisition date remain?</li>
<li><strong>Reproduction:</strong>Can you write the acquisition procedure, license, preprocessing conditions, random numbers, and environment</li>
<li><strong>Metadata:</strong>Do you have sampling, reference, electrode placement, event definition, clock domain, and a named timing-validation class?</li>
<li><strong>Annotation provenance:</strong> Did you clearly indicate whether the label came from an annotation channel, manual scoring, or a report-derived rule?</li>
<li><strong>QC:</strong>Are noise, defects, and artifacts quantified?</li>
<li><strong>Comparison:</strong>Is there a baseline and can be compared using the same metrics as the evaluation family</li>
<li><strong>Metric bundle:</strong>If the task is imbalanced or event-based, are event sensitivity, false alarms, per-stage agreement, or calibration disclosed rather than one headline number?</li>
<li><strong>Benchmark provenance:</strong>If the result comes from a challenge or leaderboard, are benchmark version, split / randomization, hidden grouping, extra-data policy, pretrained-checkpoint policy, inference-stage restrictions, and later postmortems fixed?</li>
<li><strong>Inverse-problem governance:</strong>If source imaging is compared, are validation class, source regime, inverse family / uncertainty object, geometry/control sweep, and inter-method disagreement disclosed before declaring a winner?</li>
<li><strong>Rebuttal evidence:</strong>Are there data leak tests, counterfactual tests, and records of failures</li>
</ul>
</div>

<div class="note-box">
<strong>Official benchmark postmortems are part of reproducibility, not footnotes</strong>
<p>
In practical work, a benchmark page, rules page, submission constraint, and final leaderboard can each fix a different part of what your score means. That is why this page now routes EEG foundation-model benchmarking not only through split / leakage hygiene but also through <strong>benchmark provenance</strong>. If the benchmark uses evolving challenge operations, continue directly to <a href="wiki/eeg-foundation-models.html">Wiki: EEG foundation models and pretraining</a> and <a href="verification.html#pretraining-card">Verification: Pretraining Card</a> before treating the ranking as portable generalization evidence.
</p>
</div>
</section>

<section class="section" id="l0-practice">
<h2 class="section-title">6) Run the L0 minimum loop here</h2>
<p>
The goal here is not to compete for high accuracy, but to create the smallest loop that a third party can follow in the same way. The minimum pack on this site is no longer just <strong>version + BIDS + QC + split + baseline</strong>. It now also requires <strong>event fidelity</strong>, <strong>label provenance</strong>, <strong>acquisition-distribution summary</strong>, <strong>derivative lineage</strong>, and <strong>a stopping claim</strong> so later accuracy can still be read correctly.
</p>

<div class="key-points">
<h4>L0 Loop</h4>
<ul>
<li><strong>Version:</strong>OpenNeuro snapshot / PhysioNet version / DOI / leave acquisition date</li>
<li><strong>Input:</strong>Create a format that can be placed in BIDS / EEG-BIDS (data + metadata + reference / channels / electrodes / events)</li>
<li><strong>Event fidelity:</strong>Record onset / duration / sample, clock domain, stream-alignment rule, timing-validation class, delay / jitter evidence, and event semantics</li>
<li><strong>Label provenance:</strong>State whether the target comes from annotation channels, expert scoring, clinician reports, or other rules</li>
<li><strong>Quality: </strong>Record missing, noise, artifact, and exclusion reasons in numerical form</li>
<li><strong>Processing:</strong>Fix preprocessing conditions, random numbers, software version, and derivative lineage from raw to outputs</li>
<li><strong>Evaluation: </strong>Fix one of within-session / cross-session / cross-subject first, together with the independent hold-out unit and raw-recording / window ancestry</li>
<li><strong>Output:</strong>Even if it is simple, publish at least one baseline indicator that can be compared later, and state what claim must stop here</li>
<li><strong>Audit:</strong>Failure cases, leak tests, harmonization logs, and pending conditions are also recorded along with the results</li>
</ul>
</div>

<div class="note-box">
<strong>2026-03-20 addendum: the public L0 pack is now synchronized</strong>
<p>
The weakness of this page was that the public checklist had become stricter than the wiki page readers actually use when assembling an L0 submission. That gap is now closed. If you want the submission shape itself, not only the route on this page, go directly to <a href="wiki/l0-minimum-artifact-pack.html">Wiki: Minimum artifact pack for L0</a>. The synced pack now fixes <strong>dataset identity</strong>, <strong>event fidelity</strong>, <strong>label provenance</strong>, <strong>evaluation family + hold-out ancestry</strong>, <strong>acquisition-distribution summary</strong>, <strong>derivative lineage</strong>, and <strong>stopping claim</strong> as first-class deliverables.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Easy to get clogged</th>
<th>To cut first</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I think I can reproduce it with the same dataset name</strong></td>
<td>Fix the OpenNeuro snapshot tag and PhysioNet version first, and leave the acquisition date and DOI in the runbook. </td>
</tr>
<tr>
<td><strong>Stops in the form of BIDS</strong></td>
<td>Before inputting the actual data, first create a directory skeleton, <code>dataset_description.json</code>, <code>participants.tsv</code>, and <code>events.tsv</code>. </td>
</tr>
<tr>
<td><strong>I wonder how much QC to leave</strong></td>
<td>It is safer to fix just the four items: missing, noise, artifact, and reason for exclusion, and increase them later. </td>
</tr>
<tr>
<td><strong>Cannot determine baseline</strong></td>
<td>Prefer a simple and easy-to-reproduce model, such as motor recall 2 classes or spectral summary, rather than a complex model. </td>
</tr>
<tr>
<td><strong>Getting lost in train/test</strong></td>
<td>First decide whether the comparison is within-session, cross-session, or cross-subject, then lock the split unit for each subject or session. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Step 0: Freeze the version</strong>
<p>
The dataset name alone is not enough. OpenNeuro manages snapshots with semantic-version Git tags, and PhysioNet also displays and cites dataset versions for each project. Therefore, the first runbook should record <strong>snapshot / version / DOI / retrieval date</strong>, not just the <strong>dataset name</strong>.
</p>
</div>

<div class="note-box">
<strong>Step 1: Create the BIDS skeleton first</strong>
<p>
Even if the contents are not aligned at first, just fixing the placement will reduce rework. If you create a file name and metadata template with the premise of passing it through a validator, subsequent QC and comparisons will become much easier.
</p>
</div>

<div class="note-box">
<strong>Step 2: Eliminate standard violations first with Validator</strong>
<p>
Eliminate any problems found with the machine at an early stage. Passing the BIDS Validator is not a sufficient condition for research, but it is close to the minimum requirement for sharing.
</p>
</div>

<div class="note-box">
<strong>Step 2.5: Separate and fix loader and benchmark</strong>
<p>
MNE-BIDS is a tool that helps with BIDSPath handling, data loading, and metadata extraction, while MOABB fixes the paradigm and evaluation family. There is a difference between being able to <strong>read</strong> data and being <strong>able to make fair comparisons</strong>. In particular, MNE-BIDS treats write-back of modified or preloaded data as an exception, so it is safer to treat preprocessed data as derivatives with explicit lineage.
</p>
</div>

<div class="note-box">
<strong>Step 3: Leave QC logs as numerical values ​​instead of waveforms</strong>
<p>
With just the raw waveform, it is difficult for a third party to reconstruct what went wrong and what was left out. The main body of L0 is to record bad channels, bad segments, event synchronization, stimulus logs, and reaction logs with numerical values ​​and threshold values.
</p>
</div>

<div class="note-box">
<strong>Step 4: Fix only one baseline</strong>
<p>
Rather than using SOTA, first place a comparison axis that is easy to reproduce. Having an initial baseline allows you to compare what has improved even after updating the preprocessing or updating the model.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>Check items</th>
<th>Lowest line of L0</th>
<th>Where to go back to when you're running low</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data version</strong></td>
<td>snapshot / version / DOI / acquisition date is fixed</td>
<td><a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: Standards/Repositories/Validators/Benchmarks</a></td>
</tr>
<tr>
<td><strong>Data structure</strong></td>
<td>Can be stored in BIDS format</td>
<td><a href="#bids">The shortest route to shareable data</a></td>
</tr>
<tr>
<td><strong>Quality control</strong></td>
<td>QC logs and exclusion criteria remain</td>
<td><a href="wiki/event-sync-and-measurement-logs.html">Wiki: Event synchronization and observation logs</a></td>
</tr>
<tr>
<td><strong>Comparability</strong></td>
<td>One baseline and evaluation family / train/test rules are fixed</td>
<td><a href="wiki/dataset-splits-and-leakage.html">Wiki: Data splits and data leaks</a></td>
</tr>
<tr>
<td><strong>Prepare to share</strong></td>
<td>Execution steps, environment, and failure examples can be passed on to a third party</td>
<td><a href="verification.html">Verification infrastructure</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="bids">
<h2 class="section-title">7) The shortest route to "shareable data" with Mind-Upload</h2>
<p>
Mind-Upload's goal is not just to collect data, but to leave it in a form that can be verified by a third party.
The shortest route to that end is to approach BIDS/EEG-BIDS.
</p>
<div class="cta-box">
<h4>Verification Commons</h4>
<p>Click here for the blueprint for "Standards + Storage + Evaluation". </p>
<a href="verification.html">View verification platform →</a>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">8) References and official pages</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS 1.11.1: Task events</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS 1.11.1: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021), HED for FAIR event annotation</a></li>
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025), HED library schema for EEG data annotation</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00136" target="_blank">Kothe et al. (2025), Lab Streaming Layer</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024), Motion-BIDS</a></li>
<li><a href="https://docs.openneuro.org/git.html" target="_blank">OpenNeuro Docs: Git access and snapshots</a></li>
<li><a href="https://docs.openneuro.org/user_guide.html" target="_blank">OpenNeuro Docs: Dataset landing page and snapshot metadata</a></li>
<li><a href="https://physionet.org/about/" target="_blank">PhysioNet: About and citation policy</a></li>
<li><a href="https://physionet.org/about/content/" target="_blank">PhysioNet: Resources and citation guidance</a></li>
<li><a href="https://doi.org/10.21105/joss.01896" target="_blank">Appelhoff et al. (2019), MNE-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS Docs: write_raw_bids</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018), MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB Docs</a></li>
<li><a href="https://moabb.neurotechx.com/docs/generated/moabb.evaluations.WithinSessionEvaluation.html" target="_blank">MOABB Docs: WithinSessionEvaluation</a></li>
<li><a href="https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSessionEvaluation.html" target="_blank">MOABB Docs: CrossSessionEvaluation</a></li>
<li><a href="https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSubjectEvaluation.html" target="_blank">MOABB Docs: CrossSubjectEvaluation</a></li>
<li><a href="https://doi.org/10.1038/s41597-022-01647-1" target="_blank">Ma et al. (2022), A large EEG dataset for studying cross-session variability in motor imagery BCI</a></li>
<li><a href="https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf" target="_blank">Jiang et al. (2024), Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI</a></li>
<li><a href="https://proceedings.mlr.press/v267/lee25a.html" target="_blank">Lee et al. (2025), Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning</a></li>
<li><a href="https://arxiv.org/abs/2507.14141" target="_blank">Han et al. (2025), DIVER-0: A Fully Channel Equivariant EEG Foundation Model</a></li>
<li><a href="https://arxiv.org/abs/2510.12515" target="_blank">Chen et al. (2025), HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Representation</a></li>
<li><a href="https://arxiv.org/abs/2510.21585" target="_blank">El Ouahidi et al. (2025), REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects</a></li>
<li><a href="https://arxiv.org/abs/2602.17251" target="_blank">Ma et al. (2026), Structured Prototype-Guided Adaptation for EEG Foundation Models</a></li>
<li><a href="https://arxiv.org/abs/2601.17883" target="_blank">Liu et al. (2026), EEG Foundation Models: Progresses, Benchmarking, and Open Problems</a></li>
<li><a href="https://arxiv.org/abs/2603.02268" target="_blank">Lahiri et al. (2026), PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis</a></li>
<li><a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025), official homepage</a></li>
<li><a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge (2025), rules</a></li>
<li><a href="https://eeg2025.github.io/submission/" target="_blank">EEG Challenge (2025), submission page</a></li>
<li><a href="https://eeg2025.github.io/leaderboard/" target="_blank">EEG Challenge (2025), leaderboard</a></li>
<li><a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019), Single-trial neural dynamics are dominated by richly varied movements</a></li>
<li><a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024), Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025), Stabilizing brain-computer interfaces through alignment of latent dynamics</a></li>
<li><a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025), Long-term unsupervised recalibration of cursor-based intracortical BCIs</a></li>
<li><a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025), An instantaneous voice-synthesis neuroprosthesis</a></li>
<li><a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp; Rehmsmeier (2015), The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets</a></li>
<li><a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">Roy et al. (2021), Evaluation of artificial intelligence systems for assisting neurologists with fast and accurate annotations of scalp electroencephalography data</a></li>
<li><a href="https://doi.org/10.1097/WNP.0000000000000709" target="_blank">Scheuer et al. (2021), Seizure Detection: Interreader Agreement and Detection Algorithm Assessments Using a Large Dataset</a></li>
<li><a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">Segal et al. (2023), Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction</a></li>
<li><a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">Sun et al. (2017), Large-Scale Automated Sleep Staging</a></li>
<li><a href="https://doi.org/10.7554/eLife.70092" target="_blank">Vallat &amp; Walker (2021), An open-source, high-performance tool for automated sleep staging</a></li>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), TUH EEG Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), TUH Seizure Detection Corpus</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009), Sleep classification difference between AASM and Rechtschaffen &amp; Kales</a></li>
<li><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020), Localize-MI</a></li>
<li><a href="https://doi.org/10.1088/0031-9155/46/1/306" target="_blank">Baillet et al. (2001), Evaluation of inverse methods and head models using a human skull phantom</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2004.10.030" target="_blank">Phillips et al. (2005), An empirical Bayesian solution to the source reconstruction problem in EEG</a></li>
<li><a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">Michel &amp; Brunet (2019), EEG source imaging: a practical review of the analysis steps</a></li>
<li><a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">Aydin et al. (2019), Influence of head tissue conductivity uncertainties on EEG dipole reconstruction</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2020.117411" target="_blank">Cai et al. (2021), Robust estimation of noise for electromagnetic brain imaging with the Champagne algorithm</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">Pascarella et al. (2023), An in-vivo validation of ESI methods with focal sources</a></li>
<li><a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025), HD-EEG source imaging with simultaneous SEEG</a></li>
<li><a href="https://doi.org/10.1016/j.nicl.2014.06.005" target="_blank">Birot et al. (2014), Head model and electrical source imaging</a></li>
<li><a href="https://doi.org/10.1016/j.clinph.2018.12.016" target="_blank">Mouthaan et al. (2019), E-PILEPSY systematic review</a></li>
<li><a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023), Validating EEG source imaging using intracranial electrical stimulation</a></li>
<li><a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019), Subcortical electrophysiological activity is detectable with high-density EEG source imaging</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024), Global sensitivity of EEG source analysis to tissue conductivity uncertainties</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024), The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG</a></li>
<li><a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025), Debiased estimation and inference for spatial-temporal EEG/MEG source imaging</a></li>
<li><a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025), Block-Champagne for extended E/MEG source imaging</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026), Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy</a></li>
<li><a href="https://doi.org/10.1016/j.compbiomed.2026.111449" target="_blank">Jahromi et al. (2026), 3D printed pediatric head phantom for assessing deep epileptic sources localization</a></li>
<li><a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024), Network-level encoding of local neurotransmitters in cortical astrocytes</a></li>
<li><a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011), Astrocyte-neuron lactate transport is required for long-term memory formation</a></li>
<li><a href="https://doi.org/10.1038/s42255-022-00528-6" target="_blank">Silva et al. (2022), Glial ketogenesis regulates memory maintenance during starvation</a></li>
<li><a href="https://doi.org/10.1038/s42255-025-01416-5" target="_blank">Pavlowsky et al. (2025), Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila</a></li>
<li><a href="https://doi.org/10.1038/s42255-025-01389-5" target="_blank">Greda et al. (2025), Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel</a></li>
<li><a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025), Learning-associated astrocyte ensembles regulate memory recall</a></li>
<li><a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025), The astrocytic ensemble acts as a multiday trace to stabilize memory</a></li>
<li><a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026), Astrocytes enable amygdala neural representations supporting memory</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-61312-0" target="_blank">Mai-Morente et al. (2025), Pericyte pannexin1 controls cerebral capillary diameter and supports memory function</a></li>
<li><a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025), Meningeal lymphatics-microglia axis regulates synaptic physiology</a></li>
<li><a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025), Region-specific drivers of CSF mobility measured with MRI in humans</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025), Quantitative PET imaging and modeling of molecular blood-brain barrier permeability</a></li>
<li><a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026), The glymphatic system clears amyloid beta and tau from brain to plasma in humans</a></li>
<li><a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024), Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025), Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep</a></li>
<li><a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025), Autonomic physiological coupling of the global fMRI signal</a></li>
<li><a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025), BOLD signal changes can oppose oxygen metabolism across the human cortex</a></li>
<li><a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024), Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury</a></li>
<li><a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023), Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study</a></li>
<li><a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026), Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness</a></li>
<li><a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B&oslash;gh et al. (2024), Repeatability of deuterium metabolic imaging in healthy volunteers at 3 T</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021), The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5 T to 7T</a></li>
</ul>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="eeg_101.html">Introduction to EEG →</a></li>
<li><a href="tech_roadmap.html#measurement">Roadmap: Measurement →</a></li>
<li><a href="verification.html#casework">Verification: Casework →</a></li>
<li><a href="glossary.html">Glossary →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Links</h4>
<ul>
<li><a href="https://bids.neuroimaging.io/" target="_blank">BIDS</a></li>
<li><a href="https://openneuro.org/" target="_blank">OpenNeuro</a></li>
<li><a href="https://physionet.org/" target="_blank">PhysioNet</a></li>
</ul>
</div>

</aside>
</main>
