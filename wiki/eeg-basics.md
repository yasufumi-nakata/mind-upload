---
layout: default
title: "Wiki: Basics of EEG"
description: "We'll explain from the beginning what EEG measures and why it's good at it and what it's bad at."
article_type: Wiki
subtitle: "Basic knowledge to prevent EEG from becoming a magical mind-reading technique"
author: Mind Uploading Research Project
last_updated: "2026-03-26"
note: "Beginner guide"
audience: "People learning EEG for the first time, people who want to create a premise for public data and introductory pages"
reading_time: "10-15 minutes"
page_intro: "This page is a wiki that explains from the basics what EEG measures. Beyond complicated formulas, the goal is to understand ``what kind of signals are mixed together and where'' and ``why preprocessing and QC are important.''"
accuracy_note: "We highlight the limitations of EEG so as not to overestimate it, but that doesn't mean it's useless."
page_highlights:
  - "EEG is a mixed electrical signal observed at the scalp."
  - "While strong against temporal changes, it has limitations in spatial identification and deep estimation."
  - "Reference system, electrode layout, device chain, and protocol are part of the observation model rather than background implementation details."
  - "Being able to predict something with your scalp is different from being able to uniquely determine the source in your brain."
  - "Source-space connectivity and directed connectivity are even stronger claims than source localization and need separate stopping rules."
  - "Same-session multimodal EEG acquisition is not self-validating; synchronized streams, shared cross-modal components, and target biological variables remain different achievements."
  - "A shared EEG-fMRI or EEG-PET-MRI factor can still mix neural, autonomic, and vascular contributions."
  - "QC and pretreatment records greatly determine the reliability and ceiling of the result."
known_points:
  - "EEG is good at looking at time changes in milliseconds."
  - "The observed signal is the result of a mixture of many activities, and interpretation requires assumptions."
  - "Including individualized MRI and external references improves source imaging, but uncertainty remains for deep and weak sources."
  - "Reference choice, recording setup, and channel layout can materially change ERP, connectivity, and decoding conclusions."
  - "Artifact cleanup does not by itself solve source leakage or turn directed connectivity into causal proof."
  - "Adding fMRI, PET, or other modalities can strengthen one audit layer while still leaving fusion validity, shared-factor specificity, and bundle robustness unresolved."
  - "Public data provides plenty of practice with preprocessing and baseline comparisons."
unknown_points:
  - "It remains unresolved whether non-invasive EEG alone is sufficient to reconstruct detailed causal structures within the brain."
  - "The choice of preprocessing does not uniformly change the conclusion for each task."
  - "It is not yet fixed which external benchmark will be the standard validation set for source imaging."
wiki_links:
  - label: "Wiki: Basics of WBE"
    url: "/wiki/mind-upload-basics.html"
    description: "If you want to see first where EEG fits into the overall WBE, click here."
  - label: "Wiki: EEG pretreatment and QC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "We will organize preprocessing and logging methods in a practical manner."
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Understand why EEG also requires standards and QC."
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Use this page when you want the limits of ESI, DCM, and SCM organized together."
  - label: "Wiki: Basics of multimodal integration"
    url: "/wiki/multimodal-integration-basics.html"
    description: "Use this page when EEG starts to be combined with fMRI, PET, MEG, or invasive recording."
recommended_pages:
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Data & Bench"
    url: "/datasets.html"
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>What does the EEG see?</h2>
<p>
EEG is a method that measures electrical potential differences using electrodes placed on the scalp. In other words, we are not looking directly into the brain with a camera, but are reading the mixed signals that are transmitted to the outside as a result of many overlapping activities.
</p>
</div>

<div class="note-box">
<strong>Switch to stop on this page first</strong>
<p>
With EEG, it is different to <strong>observe scalp signals</strong>, <strong>conditionally estimate brain sources</strong>, <strong>estimate interactions</strong>, and <strong>uniquely identify internal states</strong>. If these are confused, beginners will read "seen" and "estimated" as if they were the same thing.
</p>
</div>

<div class="note-box">
<strong>2026-03 correction for the beginner route</strong>
<p>
The older beginner route on this site stopped at "EEG is mixed and source imaging is hard." That was too weak. For EEG, <strong>measurement condition itself</strong> matters: reference system, electrode layout, device chain, and protocol can change what the scalp signal even means. It was also necessary to say more clearly that a <strong>connectivity map or directed graph</strong> is a stronger claim than a sensor trace or even a source estimate.
</p>
</div>

<div class="note-box">
<strong>Adding another modality does not make EEG a solved state meter</strong>
<p>
The next beginner shortcut to stop is the word <strong>multimodal</strong>. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> describe LSL as synchronization infrastructure rather than device-side delay truth, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> show that simultaneous multimodal recordings retain both common and divergent organization, and <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> show that simultaneous EEG-PET-MRI can contain coupled global dynamics together with modality-specific structure. Therefore, even when EEG is combined with other stacks, the site still separates <strong>synchronized acquisition</strong>, <strong>shared statistical structure</strong>, and <strong>one externally calibrated biological variable</strong> rather than treating them as one achievement.
</p>
</div>

<section class="section" id="strengths">
<h2 class="section-title">What EEG is good at</h2>
<table class="data-table">
<thead>
<tr>
<th>What I'm good at</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td>Seeing changes over time</td>
<td>Because EEG can capture signals in milliseconds, it is easy to track when changes occur. </td>
</tr>
<tr>
<td>State transition and event detection</td>
<td>It is suitable for observing conditions that change over time, such as sleep stages and seizure events. </td>
</tr>
<tr>
<td>Reproduction practice with public data</td>
<td>PhysioNet has standard data and it is easy to start practicing L0. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="limits">
<h2 class="section-title">Things that EEG is bad at</h2>
<table class="data-table">
<thead>
<tr>
<th>Things I'm not good at</th>
<th>Why is it difficult</th>
</tr>
</thead>
<tbody>
<tr>
<td>Accurately stating "somewhere in the brain"</td>
<td>This is because the signal becomes blurred while passing through the skull and scalp, and the inverse problem cannot be solved uniquely. </td>
</tr>
<tr>
<td>Knowing the deep structure in detail</td>
<td>Activities far from the scalp and weak signals are difficult to observe. </td>
</tr>
<tr>
<td>Making a strong claim of identity using EEG alone</td>
<td>EEG is an important clue, but it alone cannot confirm memories, values, or causal continuity. </td>
</tr>
<tr>
<td>Treating a connectivity map or directed graph as discovered causal wiring</td>
<td>Reference choice, sensor mixing, source leakage, parcellation, and missing external validation can all change the network result even after the waveform looks clean. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="observability">
<h2 class="section-title">Observation, estimation, and identification are different</h2>
<table class="data-table">
<thead>
<tr>
<th>stage</th>
<th>What can be said with EEG</th>
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observation</strong></td>
<td>The mixed potential on the scalp can be taken on the ms scale. It is good at tracking state transitions and event times. </td>
<td>We cannot say that we have directly seen which deep source is the sole cause, including cell types and neuronal modifications. </td>
</tr>
<tr>
<td><strong>Conditional estimation</strong></td>
<td>Including individual MRI, electrode coordinates, and forward model will improve the estimation of near-cortical and some deep activities. </td>
<td>Being able to detect when the conditions are severe is different from being able to restore uniqueness in general. </td>
</tr>
<tr>
<td><strong>Network / directed-connectivity estimate</strong></td>
<td>With source modeling, parcellation, and explicit metrics, one can estimate conditional interaction structure more strongly than at pure sensor level. </td>
<td>That still does not prove leak-free inter-areal coupling or causal direction. Connectivity and directed connectivity need their own validation and abstention rules. </td>
</tr>
<tr>
<td><strong>Identification</strong></td>
<td>External criteria such as intracranial stimulation, simultaneous SEEG/ECoG, phantoms, and postoperative outcomes allow for error auditing. </td>
<td>Without an external standard, it is impossible to say ``I have found the source'' or ``I have achieved a sufficient state for WBE.'' </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>2026-03 actual measurement evidence</strong>
<p>
Seeber et al. (2019) demonstrated detectability of subcortical signals with 256ch scalp EEG and simultaneous DBS recordings, but did not claim general unique reconstruction. Unnwongse et al. (2023) reported that localization error depends on cranial conductivity and source depth in direct validation for intracranial stimulation, and Hao et al. (2025) showed that source power and source depth strongly influence error in 29 cases of simultaneous HD-EEG/SEEG. Therefore, the correct way to read it is ``partially auditable if the conditions are strictly fixed'', not ``the brain source can be uniquely read using EEG alone''.
</p>
</div>

<div class="note-box">
<strong>Connectivity is not just one more EEG output</strong>
<p>
It is tempting to think that once a source estimate exists, a connectivity graph is just the next summary. That is too strong. Vinck et al. (2011) made wPLI safer against some zero-lag mixing, but Haufe et al. (2013) showed that sensor-space connectivity remains strongly limited by volume conduction, Palva et al. (2018) showed that even source-space measures can create ghost interactions, and Miljevic et al. (2025) showed that sensor-space network results move with rereferencing, epoch design, and metric choice. On this site, EEG connectivity is therefore read as a <strong>model- and pipeline-conditioned estimator</strong>, not as automatically discovered wiring.
</p>
</div>
</section>

<section class="section" id="pipeline">
<h2 class="section-title">Why QC and pretreatment are important</h2>
<p>
EEG is a measurement that is susceptible to noise, but the important correction is that the issue is not only noise. Results can move with eye blinks, myoelectricity, body movements, power supply noise, <strong>reference choice</strong>, <strong>electrode layout</strong>, <strong>device-side filtering</strong>, and <strong>site-specific setup</strong>. Therefore, it is not enough to keep only a clean-looking figure; one must also record the measurement condition that made that figure possible.
</p>
<div class="key-points">
<h4>What you want to keep as a minimum</h4>
<ul>
<li><strong>Reference method:</strong>What standard was used to measure the potential difference? </li>
<li><strong>Recording setup:</strong>Which device chain, sampling policy, and electrode layout were used? </li>
<li><strong>Filter:</strong>Which frequency band is passed through? </li>
<li><strong>Artifact processing:</strong>Which noise was removed and how? </li>
<li><strong>Exclusion criteria:</strong>Which data were excluded and why? </li>
</ul>
</div>

<div class="note-box">
<strong>Same task does not guarantee the same measurement condition</strong>
<p>
Xu et al. (2020) showed that cross-dataset deep-learning results move with environmental variability such as amplifier, cap, sampling rate, and filtering. That is why this site does not treat setup as a background nuisance. It is part of the observation model and has to be logged before the score is interpreted.
</p>
</div>

<div class="note-box">
<strong>Shared multimodal factors can still be mixed physiology</strong>
<p>
Even when a paper reports one common EEG-fMRI or EEG-PET-MRI factor, that factor can still mix neural and non-neural contributions. <a href="https://doi.org/10.1162/imag_a_00287" target="_blank">Gold et al. (2024)</a> show that fMRI-autonomic covariance grows as vigilance decreases in simultaneous EEG-fMRI-autonomic recordings, <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al. (2019)</a> show sympathetic contributions to the fMRI signal, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> show that BOLD changes can oppose oxygen-metabolism changes across a large fraction of cortex. On this site, a common factor is therefore not promoted automatically to the target neural variable.
</p>
</div>
</section>

<section class="section" id="wbe-link">
<h2 class="section-title">How to connect with WBE</h2>
<p>
EEG is not a device that suddenly completes WBE. However, it is important for providing time information on state changes, baseline comparison, and reproducibility with public data. At Mind-Upload, we treat EEG not as a device that reads everything, but as an observation tool that provides macroscopic constraints. The practical consequence is that <strong>measurement condition, source-estimation validation class, and connectivity ceiling</strong> all have to be disclosed separately before an EEG result is promoted.
</p>
<div class="note-box">
<strong>When multimodal bundles look stronger than they really are</strong>
<p>
More modalities can improve prediction while the bundle still remains fragile. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a> show real multimodal prognostic gains, but <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> show that same-sample analysis, missing-modality handling, cross-centre transfer, and inter-modality disagreement still matter. That is why this site routes EEG-plus-other-stack arguments through the <a href="../verification.html#fusion-card">Fusion Card</a>, and when living-human proxy rows are mixed, also the <a href="../verification.html#human-proxy-composition-card">Human Proxy Composition Card</a>.
</p>
</div>
<div class="cta-box">
<h4>Next</h4>
<p>Click here to read research involving EEG based on the strength of claims and evidence. </p>
<a href="claims-and-evidence.html">How to read claims and evidence →</a>
</div>

<div class="cta-box">
<h4>Practical Next</h4>
<p>Click here if you want to see what changes with reference methods, filters, and artifact processing from a practical perspective. </p>
<a href="eeg-preprocessing-and-qc.html">To EEG preprocessing and QC →</a>
</div>

<div class="cta-box">
<h4>Technical Next</h4>
<p>Click here if you would like to see the boundaries between observation and estimation, and the connections between ESI, DCM, and SCM. </p>
<a href="measurement-and-modeling-terms.html">From measurement to modeling →</a>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C., Garrido, M. I., Gramfort, A., et al. (2020). Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>, 23, 1473-1483. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review of the analysis steps. <em>Frontiers in Neurology</em>, 10, 325. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Xu, M., Yao, S., Wei, Z., et al. (2020). Cross-dataset variability problem in EEG decoding with deep learning. <em>Frontiers in Human Neuroscience</em>, 14, 103. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., &amp; Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>, 55(4), 1548-1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: a simulation study. <em>NeuroImage</em>, 64, 120-133. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva, J. M., Wang, S. H., Palva, S., et al. (2018). Ghost interactions in MEG/EEG source space: a note of caution on inter-areal coupling measures. <em>NeuroImage</em>, 173, 632-643. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Miljevic, A., Murphy, O. W., Fitzgerald, P. B., &amp; Bailey, N. W. (2025). Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. <em>Clinical Neurophysiology</em>, 174, 73-83. <a href="https://doi.org/10.1016/j.clinph.2025.03.043" target="_blank">doi:10.1016/j.clinph.2025.03.043</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>, 15, 581. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>, 16, 8887. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Gold, B. P., Goodale, S. E., Zhao, C., et al. (2024). Functional MRI signals exhibit stronger covariation with peripheral autonomic measures as vigilance decreases. <em>Imaging Neuroscience</em>, 2, IMAG.a.00287. <a href="https://doi.org/10.1162/imag_a_00287" target="_blank">doi:10.1162/imag_a_00287</a></li>
<li>Özbay, P. S., Chang, C., Picchioni, D., et al. (2019). Sympathetic activity contributes to the fMRI signal. <em>Communications Biology</em>, 2, 421. <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Epp, S. M., Castrillón, G., Yuan, B., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Rohaut, B., Hermann, B., Kaufmann, B. C., et al. (2024). Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. <em>Nature Medicine</em>, 30, 2482-2491. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Amiri, M., Bødker Andersen, M., Jørgensen, S. H., et al. (2023). Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. <em>Brain</em>, 146(1), 50-64. <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/brain/awac335</a></li>
<li>Manasova, D., Belloli, L. M. L., Rosenfelder, M. J., et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <em>Brain</em>. <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/brain/awaf412</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE basics →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG preprocessing and QC →</a></li>
<li><a href="measurement-and-modeling-terms.html">From measurement to modeling →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Reference</h4>
<ul>
<li><a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">Michel &amp; Brunet (2019)</a></li>
<li><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a></li>
<li><a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019)</a></li>
<li><a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a></li>
<li><a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">Haufe et al. (2013)</a></li>
<li><a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a></li>
<li><a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html">EEG 101 →</a></li>
<li><a href="../datasets.html">Data & Bench →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
</ul>
</div>
</aside>
</main>
