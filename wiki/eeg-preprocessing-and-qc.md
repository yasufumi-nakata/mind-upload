---
layout: default
title: "Wiki: EEG pretreatment and QC"
description: "We organize EEG preprocessing as acceptance conditions, including reference methods, filters, artifact processing, retention rates, and sensitivity analysis."
article_type: Wiki
subtitle: "Pre-processing is not a pretense, it is a condition for acceptance of a claim"
author: Mind Uploading Research Project
last_updated: "2026-03-19"
note: "Technical / practical guide"
audience: "People who want to understand how EEG preprocessing and QC affect the results with evidence."
reading_time: "12-18 minutes"
page_intro: "This page is a wiki that organizes EEG preprocessing and QC not as ``the process of adjusting the waveform at the end,'' but as ``an auditing process that determines which signals should be kept and which claims should be accepted.''"
accuracy_note: "We do not provide a one-size-fits-all procedure. From the primary literature and official specifications, we will sort out what should be fixed at the bare minimum and what should not be stated yet."
page_highlights:
  - "Reference methods, filters, and artifact processing can drive the very conclusions of ERP, connectivity, and decoding."
  - "EEG-BIDS and COBIDAS-MEEG emphasize completeness of metadata and reporting before algorithm name."
  - "Site, device, electrode layout, and reference system are part of the measurement condition rather than background implementation detail."
  - "Artifact removal does not always increase decoding accuracy, and reducing confound may result in decreased accuracy."
  - "Cleanup tools do not by themselves solve source leakage, ghost interactions, or causal direction."
  - "High beta/gamma bands overlap with myoelectric contamination, so don't make a strong case without myoelectric audit."
known_points:
  - "Preprocessing is not a small implementation difference, but a choice that determines which signals are considered neural."
  - "Reference method, filter design, bad channel processing, and exclusion criteria are the minimum information that should be kept."
  - "EEG-BIDS and COBIDAS-MEEG provide a fairly concrete floor for reproducible EEG reporting."
  - "Cross-dataset scores can move with amplifier, cap, channel layout, reference system, and protocol differences."
  - "Artifact suppression and signal preservation are different; accuracy alone does not determine the quality of preprocessing."
  - "A cleaner waveform does not automatically justify a stronger connectivity or causality claim."
unknown_points:
  - "It has not yet been decided which preprocessing group is optimal for which problem."
  - "To determine how much of the high-frequency components can be treated as neural, it is necessary to audit myoelectricity, body movement, and task dependence."
  - "Which sensitivity analysis set should be the site-wide standard is a future bench operation issue."
wiki_links:
  - label: "Wiki: Basics of EEG"
    url: "/wiki/eeg-basics.html"
    description: "Click here if you want to return from the nature of the signal itself."
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Supplements the time synchronization, event, and bad segment recording required before preprocessing."
  - label: "Wiki: Uncertainty, proofreading, abstaining"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "It supplements the idea of estimation width and abstention using preprocessing differences."
  - label: "Wiki: Standards/Location/Validator/Benchmark"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "Compensates for the role differences between BIDS, public version, loader, and benchmark."
recommended_pages:
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
  - label: "Data & Bench"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Shortest conclusion</h2>
<p>
EEG preprocessing is not a process to clean up the diagram. <strong>It is an auditing process that determines which signals are considered neural and which claims to withhold.</strong> Therefore, this site treats reference methods, filters, artifact treatments, retention rates, setup logs, and sensitivity analyses as <strong>acceptance conditions</strong> rather than supplements attached to results.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
Only the technical and natural science aspects will be dealt with here. Philosophy, legal systems, and individuality are not covered. The question to ask is not ``which preprocessing is just?'' but rather ``Which conditions must be fixed to exaggerate EEG-derived claims?''
</p>
</div>

<div class="note-box">
<strong>2026-03 correction for the beginner route</strong>
<p>
The older beginner route on this site treated preprocessing mostly as cleanup. That was too weak. For EEG, <strong>site / device / reference system / electrode layout / protocol</strong> are part of the measurement condition, and cleanup tools do not by themselves solve <strong>source leakage</strong>, <strong>ghost interactions</strong>, or <strong>directional identifiability</strong>.
</p>
</div>

<section class="section" id="why-this-matters">
<h2 class="section-title">Weaknesses to be explored in depth</h2>
<p>
The previous page correctly listed four issues: reference methods, filters, artifact handling, and exclusion criteria. However, the weakness is that <strong>why they can change the results themselves</strong> and <strong>what must be left behind to raise the level of claims</strong> was not an audit gate based on primary literature. COBIDAS-MEEG and EEG-BIDS provide a fairly concrete reporting platform, the PREP pipeline shows the interdependence of bad channel and rereference, and Widmann et al. established that the filter design itself can drive waveform and latency. More recent work also makes two additional corrections unavoidable: Xu et al. (2020) showed that cross-dataset EEG decoding moves with acquisition environment, and Haufe et al. (2013), Palva et al. (2018), and Miljevic et al. (2025) show that cleanup alone does not solve connectivity identifiability. Therefore, this issue is not a practical trick, but part of the core ceiling of EEG-derived claims.
</p>
</section>

<section class="section" id="audit-gates">
<h2 class="section-title">Seven audit gates to fix first</h2>
<table class="data-table">
<thead>
<tr>
<th>Gate</th>
<th>What primary documents and official specifications currently support</th>
<th>Assertion to stop when not passing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>metadata / reporting gate</strong></td>
<td>EEG-BIDS and COBIDAS-MEEG require minimal recording of references, ground, sampling rate, filters, bad channels, electrode coordinates, events, and exclusion rules. </td>
<td>Write it as ``reproducible EEG analysis'' or ``comparable clean EEG.'' </td>
</tr>
<tr>
<td><strong>Reference gate</strong></td>
<td>PREP pipeline and reference comparison studies show that bad channel processing and rereference drive waveform and network metrics. </td>
<td>Reading the topology, connectivity, and topography of sensor-space without reference dependencies. </td>
</tr>
<tr>
<td><strong>setup-distribution / harmonization gate</strong></td>
<td>Cross-dataset studies and channel-location benchmarks show that amplifier, cap, channel map, reference, sampling rate, and protocol differences can change the result even before the model changes. </td>
<td>Reading a cross-dataset or cross-site score as if it reflected only the target neural variable. </td>
</tr>
<tr>
<td><strong>filter gate</strong></td>
<td>Widmann et al. explained that cutoff, transition band, filter order, and causal/acausal can distort waveform and latency. </td>
<td>Emphasis on ERP onset, slow component, and high-frequency gain without knowing the filter design. </td>
</tr>
<tr>
<td><strong>artifact gate</strong></td>
<td>ICA, ICLabel, Autoreject, PREP, ASR, and ZapLine are promising cleanup tools, but research in 2025 showed that artifact correction does not necessarily improve decoding accuracy, and cleanup does not by itself validate connectivity. </td>
<td>It is read as "the preprocessing that produces the highest accuracy is the best." </td>
</tr>
<tr>
<td><strong>connectivity ceiling gate</strong></td>
<td>wPLI can reduce some zero-lag mixing, but simulation and source-space studies show that source leakage, ghost interactions, and pipeline dependence remain separate limits. </td>
<td>Reading artifact-cleaned connectivity or directed metrics as leak-proof or causal by name alone. </td>
</tr>
<tr>
<td><strong>Retention Rate / High Frequency Audit Gate</strong></td>
<td>Myoelectricity overlaps with high beta/gamma, and aggressive cleaning can also reduce neural signals. Therefore, it is necessary to keep numerical values ​​for retained trials, interpolation rate, exclusion rate, and raw-clean differences. </td>
<td>High beta/gamma neural claims and data after cleaning are sufficient. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="reporting-floor">
<h2 class="section-title">1. The reporting floor is the metadata, not the algorithm name</h2>
<p>
What EEG-BIDS and its official specifications first fix is not the flashy pipeline name, but what is measured, how it is measured, and in what state it is stored. You can write sampling frequency, low / high cutoff, notch, and channel status in `channels.tsv`, and `electrodes.tsv` and `coordsystem.json` fix the electrode position and coordinate system. COBIDAS-MEEG similarly requires detailed reporting of reference methods, filters, bad channel handling, exclusion rules, and artifact handling. The simple conclusion here is that <strong>clean EEG without metadata cannot be treated as a reproducible artifact</strong>.
</p>
<div class="note-box">
<strong>Rules on this site</strong>
<p>
At a minimum, please leave the <strong>raw reference</strong>, <strong>rereference method</strong>, <strong>filters</strong>, <strong>bad channel / bad segment</strong>, <strong>electrode coordinates</strong>, <strong>event time</strong>, and <strong>exclusion rules</strong>. Even if you only post processed data, it will not be accepted unless you can track the difference from raw to clean.
</p>
</div>
</section>

<section class="section" id="reference-choice">
<h2 class="section-title">2. The reference method is not a small implementation difference; it is part of the observation model</h2>
<p>
EEG is a potential difference measurement, so changing the reference changes the waveform, topography, and sensor-space connectivity. What the PREP pipeline emphasized is that<strong>taking the average reference while overlooking the bad channel pollutes the rereference itself</strong>. Furthermore, in reference comparison studies, functional connectivity graphs and task-related network metrics change depending on the reference. Therefore, on this site, references are treated as <strong>premises that determine the meaning of results</strong>, rather than as ``implementation notes.''
</p>
<table class="data-table">
<thead>
<tr>
<th>Minimum things to write</th>
<th>Why is it necessary</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>When recording reference / ground</strong></td>
<td>This is because the assumption of raw potential difference changes. </td>
</tr>
<tr>
<td><strong>rereference method</strong></td>
<td>This is because the meaning of the sensor-space metric changes with average, linked mastoid, REST, etc. </td>
</tr>
<tr>
<td><strong>Bad channel handling before rereference</strong></td>
<td>This is because mixing broken channels contaminates the rereference itself. </td>
</tr>
<tr>
<td><strong>Number of interpolated channels</strong></td>
<td>This is to distinguish between the actual measurement and the interpolation of the spatial pattern. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="setup-distribution">
<h2 class="section-title">3. Setup distribution and harmonization are not background noise</h2>
<p>
Two EEG datasets can use the same task name and still represent different measurement conditions. Xu et al. (2020) showed that deep-learning EEG decoding changes across datasets when amplifier, cap, sampling rate, and filtering change, and Dong et al. (2024) showed that even motor-imagery BCI comparisons require explicit harmonization across channel-location schemes. Therefore, this site does not treat <strong>site / device / reference system / electrode layout / protocol</strong> as background nuisance. They are part of the observation model.
</p>
<div class="note-box">
<strong>Rules on this site</strong>
<p>
If the claim spans more than one site, dataset, or recording setup, disclose the setup distribution and how harmonization was performed. Without that, a score is not read here as clean evidence of neural generalization.
</p>
</div>
</section>

<section class="section" id="filter-design">
<h2 class="section-title">4. A filter is not only a "pass-through band" but also a distortion design</h2>
<p>
As explained by Widmann et al., it is not enough to just write the cutoff frequency for filter. Transition band, filter order, passband / stopband ripple, causal / acausal, unidirectional / bidirectional application, latency and waveform move. Therefore, claims such as seeing a <strong>slow wave</strong>, an <strong>earlier onset</strong>, or an <strong>increase in gamma</strong> cannot be accepted without a record of the filter design.
</p>
<div class="note-box">
<strong>Rules on this site</strong>
<p>
Regarding filter, please leave not only the cutoff of <strong>high-pass</strong>, <strong>low-pass</strong>, and <strong>notch</strong>, but also <strong>filter type</strong>, <strong>order</strong>, <strong>causal / acausal</strong>, and the presence of <strong>forward-backward</strong>. When claiming ERP or latency, check conclusion drift in at least one alternative setting.
</p>
</div>
</section>

<section class="section" id="artifact-control">
<h2 class="section-title">5. Artifact suppression is not always an improvement</h2>
<p>
ICA, ICLabel, Autoreject, PREP, etc. are strong practical candidates. However, the important point here is not ``which one was used'', but whether it is possible to audit what was cut and what was left. A 2025 decoding study showed that artifact correction does not necessarily improve classification performance, but rather can reduce accuracy as a result of reducing artifact-related confounds. This does not mean that cleaning is meaningless, but rather that maximizing accuracy and maximizing neural specificity are not synonymous.
</p>
<table class="data-table">
<thead>
<tr>
<th>Candidate method</th>
<th>Role</th>
<th>Reason why it is not automatically promoted to standard solution</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PREP</strong></td>
<td>Clean the floor for line noise, bad channel, and robust reference. </td>
<td>This is because task-specific artifacts and signal preservation require a separate audit. </td>
</tr>
<tr>
<td><strong>Autoreject</strong></td>
<td>Automate threshold adjustment and interpolation in trial/sensor units. </td>
<td>This is because it is necessary to separately check how the retention rate and task-relevant signal worked. </td>
</tr>
<tr>
<td><strong>ICA + ICLabel</strong></td>
<td>Candidate independent components such as eyeballs, myoelectrics, and electrocardiograms. </td>
<td>Component removal may reduce the neural component, so full automation is dangerous. </td>
</tr>
<tr>
<td><strong>ASR / ZapLine</strong></td>
<td>Suppress large-amplitude artifacts and line-noise contamination in a reproducible way. </td>
<td>They are cleanup tools; they do not by themselves solve source leakage or directional identifiability. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Rules on this site</strong>
<p>
When reporting artifact processing, <strong>name of method used</strong> is not sufficient. Please include <strong>number of components / epochs / channels removed</strong>, <strong>interpolation rate</strong>, <strong>minutes / trials retained</strong>, <strong>raw-clean key metric differences</strong>, and if possible <strong>comparison with one alternative pipeline</strong>.
</p>
</div>
</section>

<section class="section" id="connectivity-ceiling">
<h2 class="section-title">6. Cleanup is not connectivity validation</h2>
<p>
It is tempting to think that once artifacts and line noise are suppressed, network metrics can be read more strongly. That is still too aggressive. Vinck et al. (2011) made wPLI safer against some zero-lag mixing, but Haufe et al. (2013) showed severe limits of sensor-space connectivity under volume conduction, Palva et al. (2018) showed ghost interactions even in source space, and Miljevic et al. (2025) showed strong dependence on rereference and epoch design. Therefore, this site does not promote a connectivity or directed-connectivity result only because the cleanup pipeline looks stronger.
</p>
<div class="note-box">
<strong>Rules on this site</strong>
<p>
If a paper or result outputs connectivity, directed connectivity, STE, Granger, or source-space graph measures, add a separate note stating what leakage control, external validation, and abstention boundary are still missing. Cleanup logs and connectivity validation logs are not interchangeable.
</p>
</div>
</section>

<section class="section" id="high-frequency-caution">
<h2 class="section-title">7. High beta/gamma does not write strongly without electromyographic audit</h2>
<p>
As outlined by Muthukumaraswamy, muscle artifacts overlap widely around 20-300 Hz and can be difficult to distinguish from high beta/gamma neural components. Therefore, if you claim to increase <strong>high-frequency power</strong> in a task that tends to involve activation of the forehead, jaw, and temporalis muscles, at least check for behavioral confounds such as <strong>topography</strong>, <strong>EOG / EMG auxiliary channels</strong>, and <strong>residual jaw / brow activity before and after cleaning</strong>. On this site, we will not read gamma as neural gain without doing this.
</p>
</section>

<section class="section" id="minimum-deliverables">
<h2 class="section-title">Minimum submissions</h2>
<table class="data-table">
<thead>
<tr>
<th>Submission</th>
<th>Minimum desired content</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>acquisition metadata</strong></td>
<td>reference, ground, device chain, sampling rate, line frequency, electrode coordinates, and event timing. </td>
</tr>
<tr>
<td><strong>bad channel / bad segment ledger</strong></td>
<td>What criteria were used to judge what was bad and what was interpolated is left. </td>
</tr>
<tr>
<td><strong>filter design report</strong></td>
<td>Leave cutoff, order, type, causal / acausal, notch. </td>
</tr>
<tr>
<td><strong>artifact model report</strong></td>
<td>Presence of PREP / ICA / ICLabel / Autoreject, etc., number of removals, threshold, and interpolation rate are left. </td>
</tr>
<tr>
<td><strong>setup / harmonization log</strong></td>
<td>Site, device, channel map, reference system, protocol differences, and the harmonization rule across them are disclosed. </td>
</tr>
<tr>
<td><strong>raw-clean delta</strong></td>
<td>Compare the amount of change in power spectrum, trial count, channel count, and major features between raw and clean. </td>
</tr>
<tr>
<td><strong>retention summary</strong></td>
<td>Finally, the number of minutes, number of trials, and number of channels remaining are displayed as numerical values. </td>
</tr>
<tr>
<td><strong>sensitivity analysis</strong></td>
<td>Check the conclusion drift with at least one alternative reference or artifact pipeline. </td>
</tr>
<tr>
<td><strong>high-frequency exception note</strong></td>
<td>If you claim beta/gamma, please separately explain how you passed the EMG audit. </td>
</tr>
<tr>
<td><strong>connectivity-ceiling note</strong></td>
<td>If connectivity or directionality is reported, state separately what leakage control, external validation, and abstention boundary remain. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="misreadings">
<h2 class="section-title">Misinterpretations that should be avoided from this criticism</h2>
<table class="data-table">
<thead>
<tr>
<th>Misreading</th>
<th>Replacement on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td>I got a clean waveform, so that's enough</td>
<td>Metadata, retention, and raw-clean diffs are not enough. </td>
</tr>
<tr>
<td>The pipeline with the highest decoding accuracy is the best</td>
<td>Since we may be picking up artifact confounds, we will look at specificity and sensitivity analysis first. </td>
</tr>
<tr>
<td>average reference is safe, so you don't need to write it</td>
<td>Reference is the premise of the result, so write both raw and rereference. </td>
</tr>
<tr>
<td>It is enough to write only cutoff in filter</td>
<td>Order, type, and causal/acausal are required. </td>
</tr>
<tr>
<td>High beta/gamma increase would be neural</td>
<td>Since the myoelectric overlap is strong, I cannot write strongly without an EMG audit. </td>
</tr>
<tr>
<td>Reproducible using automatic pipeline</td>
<td>Automation and reproducibility are two different things and require disclosure of inputs, thresholds, removal amounts, and retention rates. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>BIDS Specification: Electroencephalography. <a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">official docs</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M, Robbins KA. The PREP pipeline: standardized preprocessing for large-scale EEG analysis. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2015.06.014" target="_blank">doi:10.1016/j.jneumeth.2015.06.014</a></li>
<li>Widmann A, Schröger E, Maess B. Digital filter design for electrophysiological data: a practical approach. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2014.08.002" target="_blank">doi:10.1016/j.jneumeth.2014.08.002</a></li>
<li>Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. <em>Frontiers in Human Neuroscience</em>. 2013. <a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">doi:10.3389/fnhum.2013.00138</a></li>
<li>Cao Y, et al. How Different EEG References Influence Sensor Level Functional Connectivity Graphs. <em>Frontiers in Neuroscience</em>. 2017. <a href="https://doi.org/10.3389/fnins.2017.00368" target="_blank">doi:10.3389/fnins.2017.00368</a></li>
<li>Jas M, Engemann DA, Bekhti Y, Raimondo F, Gramfort A. Autoreject: automated artifact rejection for MEG and EEG data. <em>NeuroImage</em>. 2017. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.030" target="_blank">doi:10.1016/j.neuroimage.2017.08.030</a></li>
<li>Pion-Tonachini L, Kreutz-Delgado K, Makeig S. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. <em>NeuroImage</em>. 2019. <a href="https://doi.org/10.1016/j.neuroimage.2019.05.026" target="_blank">doi:10.1016/j.neuroimage.2019.05.026</a></li>
<li>Kessler V, et al. How EEG preprocessing shapes decoding performance. <em>Communications Biology</em>. 2025. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">doi:10.1038/s42003-025-08464-3</a></li>
<li>Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. <em>Frontiers in Human Neuroscience</em>. 2020;14:103. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Dong C, Jia T, Wang S, et al. Benchmarking of different channel locations for motor imagery based BCI. <em>Brain Research Bulletin</em>. 2024;210:110906. <a href="https://doi.org/10.1016/j.brainresbull.2024.110906" target="_blank">doi:10.1016/j.brainresbull.2024.110906</a></li>
<li>Chang C-Y, Hsu S-H, Pion-Tonachini L, Jung T-P. Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. <em>Proc IEEE EMBC</em>. 2018. <a href="https://doi.org/10.1109/EMBC.2018.8512547" target="_blank">doi:10.1109/EMBC.2018.8512547</a></li>
<li>de Cheveigné A. ZapLine: A simple and effective method to remove power line artifacts. <em>NeuroImage</em>. 2020;207:116356. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356" target="_blank">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li>Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CMA. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>. 2011;55(4):1548-1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. <em>NeuroImage</em>. 2013;64:120-133. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <em>NeuroImage</em>. 2018;173:632-643. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Miljevic A, Murphy OW, Fitzgerald PB, Bailey NW. Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. <em>Clinical Neurophysiology</em>. 2025;174:73-83. <a href="https://doi.org/10.1016/j.clinph.2025.03.043" target="_blank">doi:10.1016/j.clinph.2025.03.043</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-basics.html">EEG basics →</a></li>
<li><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">Uncertainty/proofreading/abstention →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html">EEG 101 →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Reference</h4>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS EEG Specification</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">COBIDAS-MEEG</a></li>
<li><a href="https://doi.org/10.1016/j.jneumeth.2015.06.014" target="_blank">PREP Pipeline</a></li>
<li><a href="https://doi.org/10.1016/j.jneumeth.2014.08.002" target="_blank">Widmann et al. (2015)</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">Muthukumaraswamy (2013)</a></li>
<li><a href="https://doi.org/10.3389/fnins.2017.00368" target="_blank">Reference and Connectivity</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2017.08.030" target="_blank">Autoreject</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2019.05.026" target="_blank">ICLabel</a></li>
<li><a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">Kessler et al. (2025)</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">Haufe et al. (2013)</a></li>
</ul>
</div>
</aside>
</main>
