---
layout: default
title: "Wiki: Basics of multimodal integration"
description: "We will organize based on primary literature how EEG, MEG, fMRI, invasive recording, and MRI can be combined to improve what can be improved and what is still unresolved."
article_type: Wiki
subtitle: "Rather than adding everything, it is designed to increase synchronization, geometry, and external validation."
author: Mind Uploading Research Project
last_updated: "2026-03-19"
note: "Technical / natural science only"
audience: "People who want to judge how to compensate for the limitations of EEG alone from only the technical and natural science aspects"
reading_time: "12-18 minutes"
page_intro: "This page is a wiki that organizes what really improves when combining EEG, MEG, fMRI, invasive recording, and MRI based on primary literature. Rather than focusing on philosophy or legal systems, we focus only on synchronization, coordinate alignment, forward models, external validation, and state coverage."
accuracy_note: "What I'm trying to show here is not that ``if you integrate everything, you can figure it out.'' It's about sorting out what can be said a little more strongly when certain conditions are met, and what can't be said yet."
page_highlights:
  - "Read Multimodal Integration with 6 Audit Gates."
  - "Compare the differences between EEG+fMRI, EEG+MEG, and EEG+invasive recordings with primary literature."
  - "Hemodynamic routes now separate neural interpretation from vascular-state / CVR and superficial/systemic confounds."
  - "Wearable OPM-MEG is read here as movement-tolerant electrophysiology only when magnetic-field control, calibration, and anatomy choice are disclosed."
  - "Fix that inverse problem and state completeness will remain even after integration."
known_points:
  - "By combining multiple modalities, some aspects of time, space, and locality can be complemented."
  - "However, the amount of improvement is highly dependent on the shared clock, individual anatomy, electrode/sensor location, conductivity assumptions, and the presence or absence of an external reference."
  - "For EEG+fMRI or EEG+fNIRS, alignment alone is not enough; vascular transfer state must be audited separately from neural interpretation."
  - "OPM-MEG can tolerate much more movement than SQUID-MEG, but it still depends on shielding, active field control, sensor calibration, and source-model disclosure."
  - "Invasive recording is a strong calibration route, but suffers from coverage bias and patient bias."
unknown_points:
  - "It is not yet certain which integration set is most effective for which stage of WBE."
  - "Even with the integration of multiple modalities, the sufficiency of cells, synapses, neuromodifications, and glial states remain unresolved."
  - "How to propagate and report post-integration uncertainties remains a research topic."
wiki_links:
  - label: "Wiki: Basics of EEG"
    url: "/wiki/eeg-basics.html"
    description: "Click here if you want to return to the limits of EEG alone."
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Introduces the basics of shared clocks, delays, jitter, and drift."
  - label: "Wiki: Uncertainty, proofreading, abstaining"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "Compensates for why uncertainty persists with integration."
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "An entry point to avoid confusing observed values and estimated values."
recommended_pages:
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Verification base"
    url: "/verification.html"
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Conclusion</h2>
<p>
Multimodal integration can compensate for some of the weaknesses of EEG. However, it can also simply replace <strong>one inverse problem with multiple problems involving synchronization, geometry, noise, and external validation</strong>. Therefore, on this site, we do not evaluate only by the fact that ``modalities were added'', but by <strong>which audit gate was passed</strong>.
</p>
</div>

<div class="note-box">
<strong>When wearable MEG sounds like unconstrained naturalism</strong>
<p>
The current OPM-MEG literature does show standing, ambulatory, and two-person proof-of-concept. But on this site, the safe reading remains narrower: the route still depends on <strong>magnetic shielding</strong>, <strong>active field control</strong>, <strong>sensor calibration / co-registration</strong>, and <strong>source-model disclosure</strong>. Without those, ``wearable'' is not treated as a portable substitute for standard MEG.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
Here we will only deal with the technical and natural science aspects. It does not include issues of identity, consciousness, or the legal system. The question to ask is not ``what could be observed?'' but <strong>what and to what extent could it be audited?
</p>
</div>

<section class="section" id="gates">
<h2 class="section-title">Six audit gates to fix first</h2>
<table class="data-table">
<thead>
<tr>
<th>Gate</th>
<th>Things I can say a little more strongly after passing through</th>
<th>Claims to stop when not working</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Synchronization gate</strong></td>
<td>Shared clocks, delays, jitter, and drift are managed, making it easier to compare time series for each modality. </td>
<td>I strongly emphasize topological relationships, causal order, and trial-level integration. </td>
</tr>
<tr>
<td><strong>Geometric gate</strong></td>
<td>Now that we have the individual MRI, measured electrode/sensor positions, and forward model, the basis for the source claim becomes a little stronger. </td>
<td>It is to generalize and assert ``where it happened.'' </td>
</tr>
<tr>
<td><strong>Noise/field gate</strong></td>
<td>MR artifact, motion artifact, background field, and cross-talk can be handled separately. </td>
<td>The idea is to treat a clean fused map as the true value of the neural signal. </td>
</tr>
<tr>
<td><strong>Hemodynamic transfer gate</strong></td>
<td>For fMRI / fNIRS, baseline vascular state, CVR, and superficial/systemic contamination are either calibrated or explicitly left as abstention limits. </td>
<td>BOLD / HbO / HbR amplitude differences can be read as if they directly measured neural differences. </td>
</tr>
<tr>
<td><strong>External validation gate</strong></td>
<td>You can audit errors for invasive records, intracranial stimulation, postoperative outcomes, phantoms, etc. </td>
<td>It can be said that there has been an "improvement" based on the estimation results alone. </td>
</tr>
<tr>
<td><strong>state coverage gate</strong></td>
<td>This integration can limit which of time, space, and locality will be compensated for and which state variables will still be missing. </td>
<td>It can be read that just by integrating it, it became sufficient observation for WBE. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="routes">
<h2 class="section-title">What is currently proven for each major route</h2>
<table class="data-table">
<thead>
<tr>
<th>Root</th>
<th>Where primary documents support</th>
<th>Remaining constraints</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG + individual MRI / forward model</strong></td>
<td>Unnwongse et al. (2023) used intracranial electrical stimulation as the ground truth and directly verified the localization error using individual FEM and skull conductivity optimization. </td>
<td>Errors depend on source depth and conductivity assumptions, and fine-grained local circuits and deep activities cannot generally be uniquely recovered. </td>
</tr>
<tr>
<td><strong>EEG + MEG</strong></td>
<td>Aydin et al. (2014) showed that EEG/MEG integration can improve source reconstruction by using a calibrated realistic head model. </td>
<td>The benefits depend on skull conductivity calibration and co-registration and cannot be obtained by simple modality stacking alone. </td>
</tr>
<tr>
<td><strong>Simultaneous measurement EEG + fMRI</strong></td>
<td>Two 2015 papers by Jorge et al. and Wirsich et al. (2021) showed that simultaneous measurements are possible even at 1.5T to 7T, and with an appropriate setup, it is possible to proceed to reproducible connectivity analysis. </td>
<td>Artifact and safety control tend to deteriorate with magnetic field strength, leaving asymmetry in time resolution, poor EEG quality, and a remaining vascular-state / CVR interpretation ceiling on the hemodynamic side. </td>
</tr>
<tr>
<td><strong>EEG + invasive recording (ECoG/SEEG/DBS)</strong></td>
<td>Zhang et al. (2006) showed cortical potential reconstruction with simultaneous scalp EEG/ECoG, and Seeber et al. (2019) showed subcortical detectability with 256ch scalp EEG and simultaneous DBS recording. </td>
<td>Coverage is biased toward areas of clinical need, and patient group bias is also unavoidable. There is no whole-brain ground truth. </td>
</tr>
<tr>
<td><strong>OPM-MEG system</strong></td>
<td>Boto et al. (2018), Seymour et al. (2021), Holmes et al. (2023), and Holmes et al. (2023) showed wearable MEG during seated, standing/mobile, ambulatory, and two-person interactive paradigms. </td>
<td>Low dynamic range / near-zero field operation, magnetically shielded rooms, active field nulling, optical tracking / interference suppression, sensor calibration, anatomy choice, and crosstalk management remain separate engineering gates. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-each-route-adds">
<h2 class="section-title">What each route actually adds</h2>

<h3>1. EEG + MRI "adds anatomy", not true value</h3>
<p>
Individualized MRI, measured electrode positions, and a realistic forward model greatly improve the conditions for EEG source imaging. However, as shown by Unnwongse et al. (2023), even if direct validation is performed, errors remain, and the deeper the source, the more difficult it becomes</strong>, so it cannot be interpreted as ``localized because MRI was added.'' The correct reading is "Geometry auditing has gone one step further."
</p>

<h3>2. EEG + MEG complements the sensitivity distribution, but cranial conductivity calibration is effective</h3>
<p>
Integration makes sense because EEG and MEG have different sensitivities to volume conduction. However, as Aydin et al. (2014) show, the key to improvement lies in the <strong>calibrated realistic volume conductor model</strong>. Therefore, the essence of this route is not that it is "strong because it is bimodal", but is<strong>strong only when accompanied by a better physical model</strong>.
</p>

<h3>3. EEG + fMRI is complementary in time and space, but increases artifact and safety</h3>
<p>
Simultaneous EEG-fMRI is attractive, but as the magnetic field strength increases, artifacts and setup dependence also increase, as shown in two 2015 papers by Jorge et al. Wirsich et al. (2021) showed reproducible connectome analysis over 1.5T to 7T, but this also means that this can only be achieved by incorporating appropriate hardware, cabling, and artifact control. The deeper correction is that even after synchronization is solved, the hemodynamic side still carries a <strong>vascular transfer state</strong>. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> showed that inter-subject CBF / CBV differences contribute to BOLD reactivity and that breath-hold-derived vascular-reactivity covariates improve group analyses. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> showed that task BOLD magnitude corresponds strongly to CVR across multiple cortical regions, <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> showed that baseline CBF partly explains age-related components of BOLD responses, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can oppose oxygen-metabolism changes across a large fraction of cortex. Therefore, it is not just a matter of adding spatial resolution: EEG+fMRI still needs a <strong>vascular-state / CVR calibration route</strong> or explicit abstention.
</p>
<div class="note-box">
<strong>Apply the same rule to fNIRS</strong>
<p>
If the hemodynamic side is fNIRS rather than fMRI, the same caution remains. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015)</a> showed that short-separation regression improves statistical significance and localization for tasks with differing autonomic responses. On this site, an fNIRS branch without <strong>short-separation / superficial diagnostic</strong> is therefore not treated as a direct neural-difference readout either.
</p>
</div>

<h3>4. EEG + invasive recording is strong as a calibration route, but coverage is narrow</h3>
<p>
Zhang et al. (2006) used simultaneous scalp EEG/ECoG to show that the main spatial patterns of cortical potential reconstructions can be preserved with realistic FEM and co-registered MRI/CT. Seeber et al. (2019) also showed that deep signals are conditionally detectable using 256ch scalp EEG and simultaneous DBS recording. However, these only strengthen the area visible in the invasion record, and do not guarantee unmeasured areas.
</p>

<h3>5. OPM-MEG expands movement tolerance, but not without magnetic-field and source-model audits</h3>
<p>
Wearable OPM-MEG is a real advance because the sensors move with the head and can therefore support paradigms that fixed SQUID helmets cannot. <a href="https://doi.org/10.1038/nature26147" target="_blank">Boto et al. (2018)</a> established the first motion-tolerant wearable system, <a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">Seymour et al. (2021)</a> pushed this to standing/mobile participants, <a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">Holmes et al. (2023)</a> enabled ambulatory movement with matrix-coil active shielding, and <a href="https://doi.org/10.3390/s23125454" target="_blank">Holmes et al. (2023)</a> extended proof-of-concept to two-person hyperscanning. But the common lesson is not ``movement solved.'' It is that <strong>movement becomes measurable when the magnetic environment is controlled tightly enough</strong>.
</p>
<p>
The main engineering ceiling is still the field environment. OPMs operate around near-zero field and have low dynamic range, so background field drift, participant movement through a non-zero field, and coil-induced interference all matter. <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">Mellor et al. (2022)</a> and <a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">Rea et al. (2021)</a> showed why precision field modeling and control are necessary, and <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">Holmes et al. (2025)</a> showed that lighter shielded rooms become plausible only when tSSS and active compensation are added. So on this site, wearable OPM-MEG is not read as ``shield-free'' or ``ordinary-room'' measurement.
</p>
<p>
The second ceiling is source modeling. <a href="https://doi.org/10.3390/s22083059" target="_blank">Iivanainen et al. (2022)</a> showed that sensor gain, position, and orientation still need explicit calibration, <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">Rhodes et al. (2025)</a> showed that pseudo-MRI can be useful when MRI is difficult but that individual MRI remains the gold standard, and <a href="https://doi.org/10.1063/5.0273491" target="_blank">Wu et al. (2025)</a> showed that crosstalk remains a practical array-design limit. Therefore, the safe ceiling on this page is <strong>movement-tolerant macro electrophysiology under disclosed field control and source-model assumptions</strong>, not unconstrained naturalistic brain readout and not state-complete observation.
</p>

<div class="note-box">
<strong>Do not read "wearable" as shield-free, calibration-free, or state-complete</strong>
<p>
Even when OP-MEG looks much closer to daily behavior, the public claim still has to name <strong>shielding class</strong>, <strong>field-nulling / interference-suppression method</strong>, <strong>motion-tracking path</strong>, <strong>sensor calibration route</strong>, <strong>anatomy route</strong>, and <strong>where abstention begins</strong>. If those are missing, this site keeps the result at the feasibility / proof-of-concept level.
</p>
</div>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Reading rules adopted on this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>multimodal:</strong>Read as "which audit gate was passed through" instead of "multiple modalities were added." </li>
<li><strong>EEG + MRI:</strong>Even if individual anatomy is included, if there is no external validation, the source claim will be limited. </li>
<li><strong>EEG + fMRI:</strong>It is useful as a complement to spatial information, but requires auditing of artifacts, safety, time series alignment, and vascular-state / CVR limits before a BOLD difference is read as a neural difference. </li>
<li><strong>EEG + fNIRS:</strong>Short-separation / superficial diagnostic is required before HbO / HbR differences are treated as neural differences. </li>
<li><strong>EEG + invasive recording: Treated as a coverage-limited calibration/validation route, not a gold standard. </li>
<li><strong>OPM-MEG:</strong>Wearable and motion-tolerant does not waive shielding, field nulling, co-registration, anatomy, or crosstalk audit. </li>
<li><strong>state coverage:</strong>If the synapse, neuromodification, glial, or cell type label is unobserved, it will be marked as unobserved. </li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C., Garrido, M. I., Gramfort, A., et al. (2020). Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>, 23, 1473-1483. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Jorge, J., Grouiller, F., Ipek, O., et al. (2015). Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. <em>NeuroImage</em>, 105, 132-144. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Jorge, J., Grouiller, F., Gruetter, R., et al. (2015). Towards high-quality simultaneous EEG-fMRI at 7 T: Detection and reduction of EEG artifacts due to head motion. <em>NeuroImage</em>, 120, 143-153. <a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">doi:10.1016/j.neuroimage.2015.07.020</a></li>
<li>Wirsich, J., Jorge, J., Iannotti, G. R., et al. (2021). The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. <em>NeuroImage</em>, 231, 117864. <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <em>NeuroImage</em>, 54(1), 369-379. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <em>Frontiers in Physiology</em>, 14, 1167148. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu, S., Tyler, L. K., Henson, R. N. A., Rowe, J. B., Cam-CAN, &amp; Tsvetanov, K. A. (2023). Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. <em>Neurobiology of Aging</em>, 121, 1-14. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Yucel, M. A. Y., Selb, J., Aasted, C. M. A., Petkov, M. P., Becerra, L., Borsook, D., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <em>Neurophotonics</em>, 2(3), 035005. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>Epp, S. M., Castrillon, G., Yuan, B., Andrews-Hanna, J., Preibisch, C., &amp; Riedl, V. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2014). Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. <em>PLoS ONE</em>, 9(3), e93154. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Zhang, Y., Ding, L., van Drongelen, W., et al. (2006). A cortical potential imaging study from simultaneous extra- and intracranial electrical recordings by means of the finite element method. <em>NeuroImage</em>, 31(4), 1517-1528. <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">doi:10.1016/j.neuroimage.2006.02.027</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657-661. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
<li>Seymour, R. A., Alexander, N., Mellor, S., O'Neill, G. C., Tierney, T. M., Barnes, G. R., &amp; Maguire, E. A. (2021). Using OPMs to measure neural activity in standing, mobile participants. <em>NeuroImage</em>, 244, 118604. <a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">doi:10.1016/j.neuroimage.2021.118604</a></li>
<li>Mellor, S. J., Tierney, T. M., O'Neill, G. C., Alexander, N., Seymour, R. A., Holmes, N., Lopez, J. D., Hill, R. M., Boto, E., Rea, M., Roberts, G., Leggett, J., Bowtell, R., Brookes, M. J., Maguire, E. A., Walker, M. C., &amp; Barnes, G. R. (2022). Magnetic Field Mapping and Correction for Moving OP-MEG. <em>IEEE Transactions on Biomedical Engineering</em>, 69(2), 528-536. <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">doi:10.1109/TBME.2021.3100770</a></li>
<li>Rea, M., Holmes, N., Hill, R. M., Boto, E., Leggett, J., Edwards, L. J., Woolger, D., Dawson, E., Shah, V., Osborne, J., Bowtell, R., &amp; Brookes, M. J. (2021). Precision magnetic field modelling and control for wearable magnetoencephalography. <em>NeuroImage</em>, 241, 118401. <a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">doi:10.1016/j.neuroimage.2021.118401</a></li>
<li>Holmes, N., Rea, M., Hill, R. M., Leggett, J., Edwards, L. J., Hobson, P. J., Boto, E., Tierney, T. M., Rier, L., Reina Rivero, G., Shah, V., Osborne, J., Fromhold, T. M., Glover, P., Brookes, M. J., &amp; Bowtell, R. (2023). Enabling ambulatory movement in wearable magnetoencephalography with matrix coil active magnetic shielding. <em>NeuroImage</em>, 274, 120157. <a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">doi:10.1016/j.neuroimage.2023.120157</a></li>
<li>Holmes, N., Rea, M., Hill, R. M., Boto, E., Leggett, J., Edwards, L. J., Rhodes, N., Shah, V., Osborne, J., Fromhold, T. M., Glover, P., Montague, P. R., Brookes, M. J., &amp; Bowtell, R. (2023). Naturalistic hyperscanning with wearable magnetoencephalography. <em>Sensors</em>, 23(12), 5454. <a href="https://doi.org/10.3390/s23125454" target="_blank">doi:10.3390/s23125454</a></li>
<li>Holmes, N., Leggett, J., Hill, R. M., Rier, L., Boto, E., Schofield, H., Hayward, T., Dawson, E., Woolger, D., Shah, V., Taulu, S., Brookes, M. J., &amp; Bowtell, R. (2025). Wearable magnetoencephalography in a lightly shielded environment. <em>IEEE Transactions on Biomedical Engineering</em>, 72(2), 609-618. <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">doi:10.1109/TBME.2024.3465654</a></li>
<li>Iivanainen, J., Borna, A., Zetter, R., Carter, T. R., Stephen, J. M., McKay, J., Parkkonen, L., Taulu, S., &amp; Schwindt, P. D. D. (2022). Calibration and Localization of Optically Pumped Magnetometers Using Electromagnetic Coils. <em>Sensors</em>, 22(8), 3059. <a href="https://doi.org/10.3390/s22083059" target="_blank">doi:10.3390/s22083059</a></li>
<li>Rhodes, N., Rier, L., Boto, E., Hill, R. M., &amp; Brookes, M. J. (2025). Source reconstruction without an MRI using optically pumped magnetometer-based magnetoencephalography. <em>Imaging Neuroscience</em>, 3, IMAG.a.8. <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">doi:10.1162/IMAG.a.8</a></li>
<li>Wu, T., Xiao, W., Peng, X., Wu, T., &amp; Guo, H. (2025). Crosstalk reduction in optically pumped magnetometers arrays for biomagnetic measurement. <em>Review of Scientific Instruments</em>, 96(8), 085004. <a href="https://doi.org/10.1063/5.0273491" target="_blank">doi:10.1063/5.0273491</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-basics.html">EEG basics →</a></li>
<li><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs →</a></li>
<li><a href="observation-to-estimation.html">From observation to estimation →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html#multimodal-integration">Introduction to EEG Integration Section →</a></li>
<li><a href="../verification.html#verification-rigor">Verification rigor requirements →</a></li>
<li><a href="../tech_roadmap.html#qa-m5">Roadmap: M5 Multimodal Integration →</a></li>
</ul>
</div>
</aside>
</main>
