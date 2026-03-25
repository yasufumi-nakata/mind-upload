---
layout: default
title: "Wiki: Human Proxy Composition and Route Maturity"
description: "Explains why recent human PET, MRSI, myelin, clearance, and multimodal advances do not automatically compose into same-subject state-complete readout, and how to audit quantity type, spatial unit, timescale, model burden, and deployment burden."
article_type: Wiki
subtitle: "Proxy-rich is not the same as same-subject state closure"
author: Mind Uploading Research Project
last_updated: "2026-03-25"
note: "Technical / natural science only"
audience: "Readers who want a stricter technical reading of current human in vivo advances and why they still stop below state-complete language"
reading_time: "12-18 minutes"
page_intro: "This page explains how to read current human proxy routes without collapsing them into one generic progress bar. The question is not only whether a route is impressive, but what it directly measures, on what unit and timescale, with what model burden, and what hidden-state families still remain unresolved."
accuracy_note: "The ceilings on this page are operational inferences drawn from primary literature. They are not the claims made by the original papers themselves."
page_highlights:
  - "Human proxy routes differ not only in strength, but in quantity type: structural scaffold, density proxy, similarity scaffold, kinetic rate map, mobility map, and model-based efflux route are different objects."
  - "Spatial unit and time window are part of the evidence: a cubic-millimeter surgical fragment, parcel-level similarity matrix, 0.7 cc dynamic metabolic voxel, and overnight plasma-efflux inference cannot be treated as interchangeable."
  - "Model burden is part of the object: tracer kinetics, partial-volume correction, blood input functions, multicompartment models, and synchronization choices all change what the measurement means."
  - "Same-session multimodal acquisition reduces one mismatch, but it does not erase common physiological factors or modality-specific residuals by default."
  - "Same-subject or same-brain wording solves specimen identity, not state continuity; sequential bridges still need elapsed-time, regime-continuity, and deformation disclosure."
  - "Proxy class, operational maturity, and calibrator role are different axes: a route can be real and still calibrate only one bounded hidden-state family."
  - "On this site, a proxy bundle is promoted only after a Human Proxy Composition Card discloses proxy class, direct observable, same-subject relation, operational maturity, calibrator role, model burden, and residual latent-state ceiling."
known_points:
  - "Recent human-side advances reduce different uncertainty terms and are scientifically meaningful, but they are not one common measurement class."
  - "SV2A PET, MRSI similarity graphs, dynamic DMRSI, myelin bilayer MRI, and CSF / glymphatic routes all require route-specific interpretation."
  - "Proxy class and operational maturity still do not tell you what the route safely calibrates, so calibrator role has to be stated separately."
  - "Simultaneous multimodal acquisition can reveal both common and divergent structure across modalities."
  - "Global or shared multimodal factors can still include autonomic or vascular physiology, not only the target neural variable."
  - "A same-subject bridge can still fail to preserve state continuity when acquisition order, elapsed time, or deformation correction are left implicit."
unknown_points:
  - "There is still no settled recipe for fusing current human proxy rows into same-subject, externally calibrated state identification."
  - "It remains unresolved which latent-state families must be measured directly, which can be externally calibrated, and which can remain explicit abstentions for stronger WBE claims."
  - "Current human routes do not yet provide comparable whole-brain in vivo readouts for transcription / chromatin state, post-transcriptional RNA-state, phospho-signaling nanodomains, branch-local proteostasis, current chloride set point, or branch-local mitochondrial positioning."
wiki_links:
  - label: "Wiki: Observability and claim ceiling by measurement stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Places this page inside the broader modality-by-modality ceiling table."
  - label: "Wiki: Multimodal integration basics"
    url: "/wiki/multimodal-integration-basics.html"
    description: "Explains why simultaneous acquisition still needs a fusion audit."
  - label: "Wiki: State-Continuity Bridge"
    url: "/wiki/state-continuity-bridge.html"
    description: "Explains why same-subject or same-brain sequential workflows still need a bridge audit before same-state language is allowed."
  - label: "Wiki: Homeostatic plasticity and maintenance state"
    url: "/wiki/homeostatic-plasticity-and-maintenance-state.html"
    description: "Organizes the hidden-state families that current human routes still leave unresolved."
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Explains why observability and identifiability are separate questions."
recommended_pages:
  - label: "WBE 101"
    url: "/wbe_101.html"
  - label: "Verification"
    url: "/verification.html"
  - label: "FAQ"
    url: "/faq.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Shortest conclusion</h2>
<p>
Recent human proxy advances are real, but they do not yet compose automatically into <strong>same-subject state-complete readout</strong>. The reason is not only missing modalities. It is also that current routes measure <strong>different quantity types</strong>, on <strong>different spatial and temporal units</strong>, with <strong>different model and hardware burdens</strong>.
</p>
</div>

<div class="note-box">
<strong>What this page fixes</strong>
<p>
The public pages already separate local human ultrastructure, SV2A PET, MRSI biochemical scaffolds, dynamic DMRSI, myelin bilayer MRI, and clearance routes. The remaining weakness was that readers could still treat those rows as if they were pieces of one nearly finished whole-brain state meter. The current primary literature does not support that shortcut. This page fixes the missing composition rule in one place.
</p>
</div>

<div class="note-box">
<strong>Scope</strong>
<p>
This page stays on the technology and natural-science side only. It does not discuss philosophy, law, personhood, or policy. The question here is narrower: <strong>what do current human routes directly observe, what do they infer through a model, and what do they still leave latent?</strong>
</p>
</div>

<section class="section" id="route-matrix">
<h2 class="section-title">The composition problem in one table</h2>
<table class="data-table">
<thead>
<tr>
<th>Human route</th>
<th>Direct observable</th>
<th>Spatial / temporal unit</th>
<th>Main model or acquisition burden</th>
<th>Safe ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Destructive local ultrastructure</strong><br><a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a>; <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a></td>
<td>Local ex vivo structural scaffold with nanoscale cell, axon, glia, and synapse geometry.</td>
<td>Cubic-millimeter surgical fragment; destructive one-time snapshot.</td>
<td>Preservation route, live-to-fix delay, section loss, segmentation, registration, proofreading.</td>
<td><strong>Destructive local structural scaffold</strong>, not living whole-brain state readout.</td>
</tr>
<tr>
<td><strong>SV2A PET</strong><br><a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>; <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a>; <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">Shatalina et al. (2024)</a></td>
<td>Tracer-defined regional SV2A binding interpreted as a synaptic-density proxy.</td>
<td>Regional scan-window average; atlas or task-linked interindividual comparison.</td>
<td>Tracer choice, arterial-versus-reference quantification, kinetic model, scan window, partial-volume handling.</td>
<td><strong>Regional synaptic-density proxy</strong>, not current synaptic efficacy or universal activity truth.</td>
</tr>
<tr>
<td><strong>Whole-brain <sup>1</sup>H-MRSI metabolic similarity</strong><br><a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a></td>
<td>Within-subject pairwise correlations among five metabolite profiles (tCr, tNAA, Glx, Ins, Cho) across gray-matter parcels.</td>
<td>Parcel-level static similarity matrix in 51 healthy subjects, with independent replication in 13.</td>
<td>Spectral QC, partial-volume correction, parceling choice, z-scoring, similarity definition.</td>
<td><strong>Macro biochemical similarity scaffold</strong>, not tractography, flux imaging, or controller-level state readout.</td>
</tr>
<tr>
<td><strong>Dynamic DMRSI</strong><br><a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a></td>
<td>Dynamic deuterated glucose and downstream metabolite signals with kinetic-model-derived rate maps.</td>
<td>0.7 cc nominal voxels, 2.5 min/image, whole-brain 7 T acquisition; five healthy participants.</td>
<td>7 T hardware, dual-frequency RF coils, blood input functions, kinetic model, oral tracer timing.</td>
<td><strong>Specialized macro metabolic-rate imaging</strong>, not branch-local mitochondrial or ATP-reserve ground truth.</td>
</tr>
<tr>
<td><strong>Myelin bilayer MRI</strong><br><a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a></td>
<td>Ultrashort-T<sub>2</sub>-based quantitative maps of the myelin lipid-protein bilayer in vivo.</td>
<td>1.4 mm maps at 3 T in two healthy volunteers.</td>
<td>High-performance RF and gradient hardware, HYFI sequence, three-component signal model, SNR constraints.</td>
<td><strong>Specialized macro myelin proxy</strong>, not per-axon timing or node-level control.</td>
</tr>
<tr>
<td><strong>CSF mobility MRI</strong><br><a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a></td>
<td>CSF mobility, explicitly distinguished from net flow or diffusion.</td>
<td>0.45-mm isotropic 7 T MRI with whole-brain rest maps in 20 healthy younger individuals, plus driver analyses reported in 11 of 24 total healthy participants.</td>
<td>CSF-specific sequence design, mobility-encoding tensor model, 7 T acquisition, region interpretation.</td>
<td><strong>Macro support-state / mobility proxy</strong>, not direct clearance flux or local immune-controller identification.</td>
</tr>
<tr>
<td><strong>Sleep-linked glymphatic efflux to plasma</strong><br><a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a></td>
<td>Overnight plasma biomarker changes interpreted through randomized crossover and a multicompartment brain-to-plasma model.</td>
<td>Randomized crossover trial with 39 participants; overnight sleep versus sleep deprivation.</td>
<td>Investigational device, plasma biomarker assays, multicompartment model, overnight physiology assumptions.</td>
<td><strong>Model-based human biomarker-efflux route</strong>, not local synaptic-maintenance or segment-specific lymphatic ground truth.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="collapse-errors">
<h2 class="section-title">Seven collapse errors to block</h2>
<table class="data-table">
<thead>
<tr>
<th>Shortcut that fails</th>
<th>Why it fails in primary literature</th>
<th>What must be disclosed instead</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Quantity-type collapse</strong><br><code>density + similarity + rate + mobility = same state variable</code></td>
<td>Johansen measures regional SV2A density proxy, Lucchetti measures parcel-level metabolite-profile similarity, Li measures kinetic glucose-related rates, Hirschler measures CSF mobility, and Dagum models overnight biomarker efflux. Those are different inferential objects.</td>
<td>Name the exact quantity: <strong>density</strong>, <strong>similarity</strong>, <strong>rate</strong>, <strong>mobility</strong>, or <strong>model-based efflux</strong>.</td>
</tr>
<tr>
<td><strong>Spatial-unit collapse</strong><br><code>local fragment + regional atlas + parcel graph + macro voxel = same resolution ladder</code></td>
<td>Shapson-Coe is a local surgical fragment, Johansen is regional atlas-level PET, Lucchetti is gray-matter parcel similarity, Li is 0.7 cc voxelwise kinetic imaging, and Baadsvik is 1.4 mm macro myelin mapping. These do not resolve the same biological unit.</td>
<td>Name the biological unit actually constrained: <strong>fragment</strong>, <strong>region</strong>, <strong>parcel</strong>, <strong>macro voxel</strong>, or <strong>whole-brain support-state trend</strong>.</td>
</tr>
<tr>
<td><strong>Timescale collapse</strong><br><code>static atlas + scan average + minutes-long kinetics + overnight physiology = one current state</code></td>
<td>Naganawa and Johansen operate over PET scan windows, Lucchetti is a static similarity scaffold, Li resolves minutes-long dynamics, and Dagum is an overnight sleep manipulation. They do not all answer <strong>what is true right now</strong> at the same timescale.</td>
<td>Name the time window explicitly: <strong>structural snapshot</strong>, <strong>scan-window average</strong>, <strong>minutes-long kinetics</strong>, or <strong>overnight state transition</strong>.</td>
</tr>
<tr>
<td><strong>Model-burden collapse</strong><br><code>multimodal means directly seen</code></td>
<td>PET requires tracer and kinetic interpretation, MRSI requires reconstruction and QC, dynamic DMRSI requires kinetic modeling and blood inputs, CSF mobility MRI requires mobility-tensor interpretation, and Dagum requires a multicompartment model. Model burden changes what is justified.</td>
<td>Disclose tracer, model family, correction route, input function, synchronization route, and abstention boundary.</td>
</tr>
<tr>
<td><strong>Deployment-maturity collapse</strong><br><code>if a route exists, it is already field-ready</code></td>
<td>Li used custom 7 T hardware in five participants; Baadsvik used two healthy volunteers with high-performance hardware; Hirschler used ultra-high-field MRI with a specialized sequence; Dagum used an investigational device. These are advances, but not routine whole-brain deployment.</td>
<td>Name cohort size, hardware class, scan burden, device status, and whether the route is routine, specialized, or proof-of-principle.</td>
</tr>
<tr>
<td><strong>Common-driver collapse</strong><br><code>if rows move together, they must be the same latent variable</code></td>
<td><a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> found both common and divergent cross-modal structure, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> found coupled global progression plus two distinct network patterns in simultaneous EEG-PET-MRI, and <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that a major global fMRI mode is substantially coupled to autonomic physiology. Agreement can therefore reflect shared nuisance or shared global state rather than one solved target variable.</td>
<td>Disclose shared-vs-specific decomposition, nuisance calibration, matched perturbation, and what still remains vulnerable to autonomic / vascular / motion-linked common drivers.</td>
</tr>
<tr>
<td><strong>Increment-collapse</strong><br><code>more rows listed = more state closure</code></td>
<td>Current primary papers advance different rows, but they do not by themselves show that a bundle outperforms the strongest row under matched subject, session, and condition. Diversity of rows is not yet evidence of incremental state closure.</td>
<td>Report what the bundle adds beyond the strongest single row under the same reading rule, ideally with matched-condition or held-out evaluation, and say explicitly when the gain is only rhetorical.</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>SV2A PET is not a generic activity meter</strong>
<p>
The safe reading of SV2A PET is narrower than “synapses were measured, therefore task-state was measured.” <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a> showed that quantification depends on tracer kinetics, model choice, and scan window. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> built a valuable atlas of regional synaptic density in 33 healthy participants. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">Smart et al. (2021)</a> then showed that visual stimulation increased tracer influx K<sub>1</sub> but left binding measures unchanged, while <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">Holmes et al. (2022)</a> found no detectable overall SV2A change 24 h after ketamine despite antidepressant response. <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">Shatalina et al. (2024)</a> further found that in 25 healthy adults, SV2A density related to task-switching activation and switch cost, yet not to the N-back task in the same study. On this site, that means density-activity or density-intervention relationships remain <strong>task-, timescale-, and design-conditioned</strong>, not a universal license to read SV2A PET as moment-to-moment neural activity or rapid plasticity.
</p>
</div>

<div class="note-box">
<strong>Metabolic similarity is not metabolic rate</strong>
<p>
The phrase <strong>metabolic connectome</strong> is especially easy to overread. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> define a within-subject parcel-similarity graph from five metabolites and show that it aligns only <strong>weakly</strong> with tractography-based structural connectivity. That is a biochemical-organization result, not kinetic flux imaging. By contrast, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> used dynamic deuterium MRSI plus a kinetic model to estimate glucose transport and metabolic rates. On this site, static similarity and dynamic rate imaging therefore remain separate rows and do not inherit one another's claim ceiling.
</p>
</div>

<div class="note-box">
<strong>CSF mobility is not net clearance flux</strong>
<p>
The distinction is explicit in the primary paper. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> state that their MRI observable is <strong>mobility</strong>, not simply flow or diffusion, because signal attenuation can arise from slow flow, laminar flow, back-and-forth motion, or a combination of these. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> then move to a different object: randomized overnight biomarker changes interpreted through a multicompartment brain-to-plasma model. On this site, those routes are both informative, but neither is silently promoted to direct local immune-controller or synapse-specific maintenance ground truth.
</p>
</div>

<section class="section" id="three-axes">
<h2 class="section-title">Proxy class, operational maturity, and calibrator role are different questions</h2>
<p>
The remaining weakness after separating quantity type, spatial unit, and model burden is subtler. Readers can still think that once a route has a recognizable <strong>proxy class</strong> and looks technically real, the route must already calibrate a broad hidden-state family. The current primary literature does not support that shortcut. On this site, each human route is therefore read along <strong>three separate axes</strong>: <strong>what kind of proxy it is</strong>, <strong>how operationally mature it is</strong>, and <strong>what hidden-state family it safely calibrates</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Human route</th>
<th>Proxy class on this site</th>
<th>Operational maturity on this site</th>
<th>Safe calibrator role</th>
<th>What still remains outside calibration</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>SV2A PET</strong><br><a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a>; <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">Smart et al. (2021)</a>; <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">Holmes et al. (2022)</a></td>
<td><strong>Regional synaptic-density proxy</strong></td>
<td>Useful atlas and disease-comparison route, but not a moment-to-moment state meter.</td>
<td>Constrains relatively slow regional synaptic-density contrasts and selected between-condition comparisons.</td>
<td>Current release probability, postsynaptic efficacy, rapid plasticity, and branch-local controller state.</td>
</tr>
<tr>
<td><strong>Whole-brain <sup>1</sup>H-MRSI metabolic similarity</strong><br><a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a></td>
<td><strong>Macro biochemical similarity scaffold</strong></td>
<td>Cohort-level whole-brain mapping with replication, but still a static similarity route.</td>
<td>Constrains parcel-level biochemical organization and cross-region metabolic similarity structure.</td>
<td>Kinetic metabolic rate, energetic reserve, axonal wiring, and local maintenance-controller identity.</td>
</tr>
<tr>
<td><strong>Dynamic DMRSI</strong><br><a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a></td>
<td><strong>Specialized macro metabolic-rate imaging</strong></td>
<td>High-burden proof-of-principle route with custom 7 T hardware and blood-input modeling.</td>
<td>Constrains macro glucose-transport and metabolic-rate maps under an explicit kinetic model.</td>
<td>Branch-local mitochondrial positioning, ATP nano-organization, and synapse-specific energetic reserve.</td>
</tr>
<tr>
<td><strong>CSF mobility MRI</strong><br><a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a></td>
<td><strong>Macro support-state / mobility proxy</strong></td>
<td>Specialized 7 T route with a CSF-specific sequence and region-specific driver analyses.</td>
<td>Constrains region-specific CSF mobility and its candidate physiological drivers.</td>
<td>Net clearance flux, cell-specific immune control, and synapse-level maintenance state.</td>
</tr>
<tr>
<td><strong>Sleep-linked glymphatic efflux to plasma</strong><br><a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a></td>
<td><strong>Model-based human biomarker-efflux route</strong></td>
<td>Intervention-backed crossover design, but still device-dependent and model-heavy.</td>
<td>Constrains the sleep-linked directionality of brain-to-plasma biomarker transport under a multicompartment model.</td>
<td>Spatial localization, local clearance topology, and cell-specific synaptic-maintenance controller identity.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Operational rule on this site</strong>
<p>
The safe ceiling of a proxy bundle is not set by the most impressive hardware description or by the number of rows listed. It is set by the <strong>narrowest well-supported calibrator role</strong> that survives matched-condition comparison, common-driver audit, and external calibration. Without that separation, <strong>proxy-rich</strong> is too easy to misread as <strong>broad hidden-state calibration</strong>.
</p>
</div>
</section>

<section class="section" id="multimodal">
<h2 class="section-title">Same-session multimodal does not erase the composition problem</h2>
<p>
It is tempting to think that if several modalities are acquired simultaneously, the composition problem disappears. The current primary literature does not support that shortcut. Simultaneous acquisition narrows one class of timing mismatch, but it still leaves open <strong>what is shared</strong>, <strong>what remains modality-specific</strong>, and <strong>what common factors may come from physiology rather than the target neural variable</strong>.
</p>
<p>
<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> used simultaneous wide-field Ca<sup>2+</sup> imaging and fMRI-BOLD in mice and found that the modalities reveal both <strong>common</strong> and <strong>divergent</strong> features of network organization. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> used simultaneous EEG-PET-MRI in humans and found tightly coupled global hemodynamic and metabolic progressions during descent into NREM sleep, while also identifying <strong>two distinct network patterns</strong> rather than one uniform multimodal state. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> further showed that a major low-frequency global fMRI mode is substantially coupled to <strong>autonomic arousal physiology</strong>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> then showed in same-session quantitative fMRI that approximately <strong>40%</strong> of gray-matter voxels with significant ΔBOLD exhibited <strong>opposing</strong> oxygen-metabolism changes. On this site, that means same-session multimodal acquisition still needs a <a href="../verification.html#fusion-card">Fusion Card</a> and does not auto-upgrade a result to same-subject state closure. It also means a proxy bundle still has to disclose whether the apparent agreement survives a <strong>common-driver audit</strong>, whether the quantity types remain commensurable, and whether the bundle adds anything beyond the strongest single row.
</p>
</section>

<section class="section" id="sequential-bridge">
<h2 class="section-title">Same-subject is not yet same-state when the bridge is sequential</h2>
<p>
The next shortcut to block is subtler than ordinary multimodal overreading. Even if two measurements come from the <strong>same subject</strong> or the <strong>same brain</strong>, they still do not automatically form one state sample when the bridge itself is sequential. The problem is not only that the modalities differ. The problem is that the pipeline can cross <strong>time</strong>, <strong>physiological regime</strong>, and <strong>tissue transformation</strong> before the second stage is acquired.
</p>
<p>
<a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that preservation route and fixation time course materially change extracellular-space retention and native geometry. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a> then showed that linking in vivo two-photon physiology to synchrotron microtomography and serial block-face EM requires a multistage correlative workflow with explicit landmarks and targeted subvolumes. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> showed that same-brain function plus EM remains a <strong>sequential local pipeline</strong> rather than simultaneous whole-state capture. Finally, <a href="https://doi.org/10.1038/nature14467" target="_blank">Attardo et al. (2015)</a> showed that adult CA1 dendritic spines are not static over relaxed windows, with mean lifetimes on the order of <strong>1-2 weeks</strong>. On this site, that means same-subject wording solves specimen identity only; it does <strong>not</strong> solve state continuity by itself.
</p>
<table class="data-table">
<thead>
<tr>
<th>Bridge failure mode</th>
<th>Why it matters</th>
<th>What must be disclosed instead</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Time-gap collapse</strong><br><code>same subject = same time</code></td>
<td>A live measurement and a later fixation or cross-day reacquisition can cross windows in which synaptic, excitability, sleep-related, or support-state variables drift.</td>
<td>Name the exact elapsed time and which hidden-state families could change inside that window.</td>
</tr>
<tr>
<td><strong>Regime-collapse</strong><br><code>same specimen = same physiological state</code></td>
<td>Arousal, anesthesia, sleep deprivation, task condition, pharmacology, or recovery status can differ across the bridge even when the specimen is the same.</td>
<td>Name whether the regime was matched, intentionally shifted, or left unmatched.</td>
</tr>
<tr>
<td><strong>Geometry-collapse</strong><br><code>same brain = same coordinates</code></td>
<td>Fixation, shrinkage, sectioning, and correlative registration change how points in live space are mapped to ex vivo space.</td>
<td>Name landmarks, deformation model, manual versus automated correspondence, and unresolved mismatch.</td>
</tr>
<tr>
<td><strong>Validation-collapse</strong><br><code>correlative workflow = validated bridge</code></td>
<td>A bridge can be carefully engineered and still remain unvalidated for the exact state claim being made.</td>
<td>Name the bridge validation rung: repeated live measurement, vessel / cell recovery, stimulation-site correspondence, histology check, or none.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Operational rule on this site</strong>
<p>
If the claim depends on treating a sequential bridge as one latent-state sample, this site now asks for the <a href="../verification.html#state-continuity-bridge-card">Verification: State-Continuity Bridge Card</a>. Without that card, the result stays at the <strong>strongest directly supported live or destructive stage</strong> plus, at most, an <strong>unvalidated bridge hypothesis</strong>; it is not promoted to same-state cross-regime evidence. If the bridge problem itself is your main question, the longer background is in <a href="../wiki/state-continuity-bridge.html">Wiki: State-Continuity Bridge</a>.
</p>
</div>
</section>

<section class="section" id="promotion-rule">
<h2 class="section-title">What must be fixed before a proxy bundle is promoted</h2>
<table class="data-table">
<thead>
<tr>
<th>Required disclosure</th>
<th>Why it is required here</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claimed latent variable</strong></td>
<td>Without naming the target variable, routes that constrain different objects are silently mixed.</td>
</tr>
<tr>
<td><strong>Proxy class of each row</strong></td>
<td>Prevents structural scaffold, density proxy, similarity scaffold, kinetic rate imaging, mobility proxy, and model-based efflux from being treated as the same kind of evidence.</td>
</tr>
<tr>
<td><strong>Direct observable of each stack</strong></td>
<td>Prevents density, similarity, rate, mobility, and efflux from being treated as synonyms.</td>
</tr>
<tr>
<td><strong>Same-subject / same-session / same-perturbation relation</strong></td>
<td>Stops cross-cohort or cross-paper evidence from being rephrased as if it were one joint measurement in one person.</td>
</tr>
<tr>
<td><strong>Model burden and acquisition burden</strong></td>
<td>Kinetic models, blood inputs, high-field hardware, investigational devices, and specialized sequences all change the practical meaning of the result.</td>
</tr>
<tr>
<td><strong>Operational maturity</strong></td>
<td>Stops proof-of-principle, specialized high-field, and routine clinical-style routes from being silently treated as equally deployable or equally reproducible.</td>
</tr>
<tr>
<td><strong>Calibrator role</strong></td>
<td>Stops a real human route from being overread as if it calibrated every hidden-state family, rather than one bounded family such as regional density, parcel similarity, macro energetic rate, or support-state mobility.</td>
</tr>
<tr>
<td><strong>External calibration or perturbation route</strong></td>
<td>Needed to separate a shared statistical factor from a validated biological variable.</td>
</tr>
<tr>
<td><strong>Common-driver / independence audit</strong></td>
<td>Prevents cross-row agreement from being read as one solved latent variable when the bundle may still be dominated by autonomic, vascular, motion-linked, or shared-preparation factors.</td>
</tr>
<tr>
<td><strong>Increment over the strongest single row</strong></td>
<td>Stops row diversity from being mistaken for state closure when the bundle has not been shown to add anything beyond the strongest single route under matched conditions.</td>
</tr>
<tr>
<td><strong>Residual latent-state ceiling</strong></td>
<td>Keeps transcription / chromatin state, RNA-state, phospho-signaling, proteostasis, chloride homeostasis, mitochondrial positioning, and local immune control explicit when they remain unresolved.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Operational rule on this site</strong>
<p>
If these disclosures are missing, a proxy bundle remains at <strong>proxy-rich but ceiling-limited human evidence</strong>. It is not promoted to <strong>same-subject cross-stack state identification</strong>, <strong>unique internal-state recovery</strong>, or <strong>state-complete readout</strong>. In particular, row diversity without explicit <strong>proxy class</strong>, <strong>operational maturity</strong>, <strong>calibrator role</strong>, <strong>common-driver audit</strong>, and a clear <strong>increment over the strongest single row</strong> is not treated as real state closure. The public-facing implementation of that rule is the <a href="../verification.html#human-proxy-composition-card">Verification: Human Proxy Composition Card</a>.
</p>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References (main)</h2>
<ol>
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Bosch, C., Pacureanu, A., Patiño, J., et al. (2022). Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>Naganawa, M., Li, S., Nabulsi, N., et al. (2021). First-in-human evaluation of <sup>18</sup>F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">doi:10.2967/jnumed.120.249144</a></li>
<li>Johansen, A., Beliveau, V., Colliander, E., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Smart, K., Liu, H., Matuskey, D., et al. (2021). Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">doi:10.1177/0271678X20946198</a></li>
<li>Holmes, S. E., Scheinost, D., Finnema, S. J., et al. (2022). Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">doi:10.1038/s41380-022-01465-2</a></li>
<li>Shatalina, E., Onwordi, E. C., Whitehurst, T., et al. (2024). The relationship between SV2A levels, neural activity, and cognitive function in healthy humans: A [<sup>11</sup>C]UCB-J PET and fMRI study. <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">doi:10.1162/imag_a_00190</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., et al. (2024). Myelin bilayer mapping in the human brain in vivo. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Hirschler, L., Runderkamp, B. A., Decker, A., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., Elbert, D. L., Giovangrandi, L., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T. S., et al. (2025). Autonomic physiological coupling of the global fMRI signal. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Epp, S. M., Castrillón, G., Yuan, B., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Attardo, A., Fitzgerald, J. E., &amp; Schnitzer, M. J. (2015). Impermanence of dendritic spines in live adult CA1 hippocampus. <a href="https://doi.org/10.1038/nature14467" target="_blank">doi:10.1038/nature14467</a></li>
</ol>
</section>

</article>
</main>
