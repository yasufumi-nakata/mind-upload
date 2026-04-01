---
layout: default
title: "Wiki: Basics of multimodal integration"
description: "We will organize based on primary literature how EEG, MEG, fMRI, invasive recording, and MRI can be combined to improve what can be improved, what remains unresolved, and where multimodal bundle gains still depend on availability, transfer, and disagreement audits."
article_type: Wiki
subtitle: "Rather than adding everything, it is designed to increase synchronization, geometry, and external validation."
author: Mind Uploading Research Project
last_updated: "2026-04-01"
note: "Technical / natural science only (updated with the 2026-04-01 effective-window addendum)"
audience: "People who want to judge how to compensate for the limitations of EEG alone from only the technical and natural science aspects"
reading_time: "12-18 minutes"
page_intro: "This page is a wiki that organizes what really improves when combining EEG, MEG, fMRI, invasive recording, and MRI based on primary literature. Rather than focusing on philosophy or legal systems, we focus only on synchronization, coordinate alignment, forward models, external validation, state coverage, and bundle robustness."
accuracy_note: "What I'm trying to show here is not that ``if you integrate everything, you can figure it out.'' It's about sorting out what can be said a little more strongly when certain conditions are met, and what can't be said yet."
page_highlights:
  - "Read multimodal integration with 11 audit gates."
  - "Compare the differences between EEG+fMRI, EEG+MEG, and EEG+invasive recordings with primary literature."
  - "Same-session multimodal acquisition is not treated as self-validating fusion; a Fusion Card is required before the claim ceiling rises above the strongest unimodal route."
  - "Same-session acquisition does not erase temporal-kernel mismatch; event-locked EEG, hemodynamic response windows, and minute-scale PET routes still need an effective-window audit."
  - "Shared timestamps, shared cross-modal components, and the target biological variable are audited as separate objects rather than one shortcut."
  - "Shared-vs-specific decomposition and quantity bridge / physiology grounding are separate audits, so a coupled trajectory is not automatically one solved biological quantity."
  - "More modalities can improve bundle performance without making the bundle availability-agnostic; complete-case subset, missing-modality handling, and cross-centre transfer remain separate audits."
  - "Hemodynamic routes now separate neural interpretation from vascular-state / CVR and superficial/systemic confounds."
  - "Recent tri-modal EEG-PET-MRI work strengthens sleep/wake physiology reading, but still as model-bearing fusion rather than state-complete ground truth."
  - "When multimodal fusion also mixes living-human proxy classes, the Fusion Card and Human Proxy Composition Card solve different failure modes."
  - "Wearable OPM-MEG is read here as movement-tolerant electrophysiology only when magnetic-field control, calibration, and anatomy choice are disclosed."
  - "Fix that inverse problem and state completeness will remain even after integration."
known_points:
  - "By combining multiple modalities, some aspects of time, space, and locality can be complemented."
  - "However, the amount of improvement is highly dependent on the shared clock, individual anatomy, electrode/sensor location, conductivity assumptions, and the presence or absence of an external reference."
  - "Simultaneous acquisition, atlas-informed interpretation, and externally calibrated fusion are different claim levels."
  - "Same-session acquisition can still mix event-locked electrophysiology, hemodynamic response windows, and scan-window or kinetic metabolic measures, so synchronized clocks do not yet define one temporal object."
  - "A shared low-frequency or global multimodal factor can still mix neural, autonomic, and vascular contributions, so common structure is not yet target-variable specificity."
  - "A coupled multimodal trajectory can still sit on a mismatched biological axis, so shared time courses are not yet a quantity bridge by default."
  - "A multimodal gain can still depend on which subjects or trials actually carried all modalities, how missing rows were handled, and whether the bundle survives site transfer."
  - "For EEG+fMRI or EEG+fNIRS, alignment alone is not enough; vascular transfer state must be audited separately from neural interpretation."
  - "OPM-MEG can tolerate much more movement than SQUID-MEG, but it still depends on shielding, active field control, sensor calibration, and source-model disclosure."
  - "Invasive recording is a strong calibration route, but suffers from coverage bias and patient bias."
unknown_points:
  - "It is not yet certain which integration set is most effective for which stage of WBE."
  - "Even with the integration of multiple modalities, the sufficiency of cells, synapses, neuromodifications, and glial states remain unresolved."
  - "How to propagate and report post-integration uncertainties remains a research topic."
  - "How shared-vs-specific decompositions should be benchmarked across human multimodal stacks remains unsettled."
  - "How effective-window / temporal-kernel compatibility should be benchmarked across simultaneous human multimodal stacks remains unsettled."
  - "Which quantity bridges can be externally calibrated across electrophysiological, hemodynamic, metabolic, and autonomic stacks remains unsettled."
  - "How to compare multimodal bundles fairly when modality availability, centre mix, or hard-subgroup disagreement differ remains unsettled."
wiki_links:
  - label: "Wiki: Basics of EEG"
    url: "/wiki/eeg-basics.html"
    description: "Click here if you want to return to the limits of EEG alone."
  - label: "Wiki: observability and claim ceiling by measurement stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Use this page when you want the cross-stack ceiling table next."
  - label: "Wiki: Human Proxy Composition and Route Maturity"
    url: "/wiki/human-proxy-composition.html"
    description: "Use this when the multimodal bundle also mixes living-human proxy classes such as PET, MRSI, or support-state routes."
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Introduces the basics of shared clocks, delays, jitter, and drift."
  - label: "Wiki: Uncertainty, proofreading, abstaining"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "Compensates for why uncertainty persists with integration."
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "An entry point to avoid confusing observed values and estimated values."
  - label: "Wiki: Baselines, preregistration, and model cards"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Use this page when multimodal results need the Fusion Card workflow."
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
<strong>Even same-session multimodal acquisition still needs a Fusion Card</strong>
<p>
The remaining weakness on this page was that <strong>simultaneous</strong>, <strong>multimodal</strong>, or <strong>atlas-informed</strong> could still be overread as if fusion validity were already built in. The primary literature does not support that shortcut. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> describe LSL as synchronization infrastructure rather than device-side delay truth, <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a> show that EEG-fMRI fusion remains a model-conditioned inference problem, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> show that simultaneous multimodal recordings can retain both common and divergent network organization, and <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> show that simultaneous EEG-PET-MRI can reveal coupled global dynamics together with modality- and network-specific structure across wakefulness and NREM sleep. Therefore, on this site, even same-session multimodal claims still need a <a href="../verification.html#fusion-card">Fusion Card</a> before they are read above the strongest unimodal or prior-conditioned ceiling.
</p>
</div>

<div class="note-box">
<strong>Same session is not yet the same effective window</strong>
<p>
One remaining shortcut is to treat <strong>simultaneous acquisition</strong> as if it had already aligned the temporal object itself. The primary literature does not support that shortcut. <a href="https://doi.org/10.1155/2016/4182483" target="_blank">Nguyen et al. (2016)</a> explicitly noted that the <strong>temporal mismatch between EEG and fMRI still persists</strong> even in spatiotemporally constrained EEG-fMRI source imaging. <a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">Ripp et al. (2021)</a> then showed that simultaneous FDG-PET/fMRI working-memory data still rely on PET <strong>scan-window averages</strong>, reconstructing baseline uptake from <strong>44-60 min</strong> and task uptake from <strong>63-71 min</strong> post-injection under an assumed steady state. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> finally made the multi-timescale point concrete by linking sleep-stage electrophysiology to hemodynamic and metabolic progression in the same EEG-PET-MRI session. Therefore, on this site, a same-session multimodal paper must disclose the <strong>effective-window / temporal-kernel relation</strong> of each stack and say whether the claim is about one matched state sample, one shared transition, or only coordinated dynamics across different temporal kernels.
</p>
</div>

<div class="note-box">
<strong>A shared multimodal factor is not automatically the target biological variable</strong>
<p>
The next shortcut to block is subtler. A paper may show <strong>shared</strong> or <strong>coupled</strong> dynamics across modalities without showing that the shared factor already equals the biological variable you care about. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> explicitly separated common and divergent cortical organization across modalities, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> reported coupled global dynamics together with modality- and network-specific structure, <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that low-frequency global fMRI fluctuations covary with EEG and autonomic signals as part of an arousal response, and <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al. (2019)</a> showed that sympathetic activity can contribute to the fMRI signal during EEG-marked arousal changes. Therefore, on this site, a common factor still has to be labeled as <strong>shared neural candidate</strong>, <strong>modality-specific residual</strong>, <strong>physiology-linked global factor</strong>, or <strong>mixed / unresolved</strong> rather than being promoted automatically to one solved state variable.
</p>
</div>

<div class="note-box">
<strong>A coupled trajectory is not yet a quantity bridge</strong>
<p>
One more gap remained after separating <strong>shared</strong> and <strong>specific</strong> components. The page still left too much room to slide from "these modalities covary" to "these modalities now read the same biological quantity." The primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed tightly coupled global hemodynamic and metabolic progression during the descent into NREM sleep while also identifying <strong>two distinct network patterns</strong>. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that a major low-frequency global fMRI mode is substantially coupled to <strong>autonomic physiology</strong> as well as EEG. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> then showed that significant task BOLD changes can coexist with <strong>opposite oxygen-metabolism changes</strong> across many cortical voxels. Therefore, on this site, a multimodal paper must say whether it established only a <strong>shared trajectory</strong>, a <strong>physiology-linked common driver</strong>, or an explicit <strong>quantity bridge on a named biological axis</strong>. Without that bridge, coupled dynamics do not yet define one solved neural quantity.
</p>
</div>

<div class="note-box">
<strong>More modalities do not make the bundle availability-agnostic</strong>
<p>
One more shortcut remained after tightening synchronization and shared-vs-specific logic. A paper can honestly show that using more modalities improves prediction, yet that still does not mean the multimodal bundle is already acquisition-complete, transfer-stable, or coherent in the hardest regimes. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a> showed that adding modalities in acute brain injury decreased prognostic uncertainty and improved accuracy, which is a real bundle-performance gain. But <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> showed that direct same-sample multimodal comparison relied on <strong>48 complete-feature patients</strong>, while <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> used missing-value substitution, tested generalization across <strong>different centres and acquisition parameters</strong>, and found higher <strong>inter-modality disagreement</strong> in minimally conscious or improving patients. Therefore, on this site, a multimodal gain is read first as <strong>bundle-performance evidence under a declared availability and transfer regime</strong>, not as automatic proof that the bundle is already robust, complete, or state-identified.
</p>
</div>

<div class="note-box">
<strong>A Fusion Card does not replace the Human Proxy Composition Card</strong>
<p>
The Fusion Card answers whether streams were aligned, co-registered, and combined transparently. It does not answer whether EEG, PET, fMRI, MRSI, or other living-human proxy rows constrain the <strong>same latent family</strong>, live in the <strong>same cohort / physiological regime</strong>, or add more than the <strong>strongest single row</strong>. Therefore, if a multimodal argument also mixes living-human proxy classes to raise a human claim ceiling, this page now routes it to the <a href="../verification.html#human-proxy-composition-card">Human Proxy Composition Card</a> in addition to the <a href="../verification.html#fusion-card">Fusion Card</a>.
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
Here we will only deal with the technical and natural science aspects. It does not include issues of identity, consciousness, or the legal system. The question to ask is not ``what could be observed?'' but <strong>what and to what extent could it be audited</strong>.
</p>
</div>

<section class="section" id="gates">
<h2 class="section-title">Eleven audit gates to fix first</h2>
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
<td><strong>Fusion Card gate</strong></td>
<td>Acquisition relation, lag audit, co-registration scope, fusion model, and gain over unimodal / prior-only baselines are visible, so the result can be read as bounded cross-stack evidence rather than a loose stack collage.</td>
<td>It is too strong to read same-session, atlas-informed, or tri-modal wording as if one biological state variable had already been jointly identified.</td>
</tr>
<tr>
<td><strong>Effective-window / temporal-kernel gate</strong></td>
<td>The paper names whether each stack contributes event-locked activity, a hemodynamic response window, a scan-window average, or a minutes-long kinetic route, and says whether the claim concerns one matched state sample, one shared transition, or only coordinated multi-timescale dynamics.</td>
<td>Same-session acquisition is not promoted to one synchronous latent-state object when the modalities still average over different temporal windows or kernels.</td>
</tr>
<tr>
<td><strong>Shared-vs-specific component gate</strong></td>
<td>The paper says whether the claimed effect lives in a shared cross-modal component, a modality-specific residual, or a physiology-linked/global factor, and which decomposition or comparison supports that reading.</td>
<td>A synchronized common factor is not promoted to the target biological variable when shared physiology, residual mismatch, or modality-specific structure remain unresolved.</td>
</tr>
<tr>
<td><strong>Quantity-bridge / physiology-grounding gate</strong></td>
<td>The paper names the biological axis on which modalities are being compared and shows why the quantities are commensurate, for example by disclosing whether the bridge is electrophysiology-linked arousal, vascular transfer, metabolic rate, or another explicitly bounded physiology route.</td>
<td>A coupled trajectory or positive cross-modal correlation is not promoted to one solved neural quantity when the bridge between electrophysiological, hemodynamic, metabolic, or autonomic quantities remains unresolved.</td>
</tr>
<tr>
<td><strong>Bundle robustness gate</strong></td>
<td>The paper discloses which samples actually carried all required modalities, how missing modalities were handled, whether the gain survives cross-centre / cross-scanner transfer, and whether disagreement concentrates in hard subgroups or nuisance regimes.</td>
<td>It is too strong to read ``more modalities improved performance'' as if the bundle were already acquisition-complete, centre-robust, or equally coherent in the hardest cases.</td>
</tr>
<tr>
<td><strong>State coverage gate</strong></td>
<td>This integration can limit which of time, space, and locality will be compensated for and which state variables will still be missing. </td>
<td>It can be read that just by integrating it, it became sufficient observation for WBE. </td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Minimum fusion package on this site</strong>
<p>
For multimodal or atlas-prior routes, this page now follows the same disclosure bundle used in <a href="../verification.html#fusion-card">Verification: Fusion Card</a>: <strong>acquisition relation</strong>, <strong>clock / lag audit</strong>, <strong>effective-window / temporal-kernel relation</strong>, <strong>geometry / co-registration scope</strong>, <strong>fusion object and model burden</strong>, <strong>shared-vs-specific component disclosure</strong>, <strong>quantity bridge / physiology grounding</strong>, <strong>incremental evidence over unimodal / prior-only baselines</strong>, <strong>availability / complete-case slice</strong>, <strong>missing-modality policy</strong>, <strong>cross-centre / cross-scanner transfer window</strong>, and <strong>external calibration plus abstention boundary</strong>. If those fields are missing, the result stays at the ceiling of the strongest individually supported stack rather than becoming same-subject cross-stack state identification. If the bundle also mixes living-human proxy classes, this site adds the <a href="../verification.html#human-proxy-composition-card">Human Proxy Composition Card</a> instead of treating the Fusion Card as sufficient.
</p>
</div>

<div class="note-box">
<strong>Three different things that often get collapsed into one word</strong>
<p>
On this site, <strong>synchronized streams</strong>, <strong>a shared cross-modal component</strong>, and <strong>one externally calibrated biological variable</strong> are three different achievements. The first is an acquisition property, the second is a statistical result, and the third is a biological interpretation that still needs calibration and abstention boundaries. Multimodal papers are demoted when those three levels are compressed into one sentence.
</p>
</div>
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
<td>Artifact and safety control tend to deteriorate with magnetic field strength, leaving asymmetry in time resolution, poor EEG quality, and a remaining vascular-state / CVR interpretation ceiling on the hemodynamic side. Same-session acquisition also still needs a disclosed fusion model, <strong>effective-window relation between event-locked EEG and hemodynamic response windows</strong>, shared-vs-specific decomposition, and unimodal / prior-only baselines. </td>
</tr>
<tr>
<td><strong>Simultaneous EEG + PET + MRI</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed temporally coupled global hemodynamic and metabolic progression across wakefulness and NREM sleep while resolving distinct network patterns inside the same tri-modal session.</td>
<td>The route still depends on PET quantification model, hemodynamic / metabolic interpretation, an explicit quantity bridge / physiology-grounding rule, <strong>effective-window disclosure across second-scale electrophysiology, hemodynamic response windows, and minute-scale PET routes</strong>, co-registration, physiology-side interpretation of low-frequency shared factors, a disclosed fusion baseline, and, when reused as a predictive bundle, explicit disclosure of modality availability / complete-case slices and transfer across centres or protocol shifts; it does not by itself identify one externally validated latent brain state or solve hidden-state completeness.</td>
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
<p>
The temporal object also remains split. <a href="https://doi.org/10.1155/2016/4182483" target="_blank">Nguyen et al. (2016)</a> explicitly stated that temporal mismatch persists in EEG-fMRI source imaging even when fMRI priors are made time-variant. On this site, simultaneous EEG-fMRI is therefore read as <strong>shared acquisition plus a declared cross-kernel relation</strong>, not as automatic alignment between event-scale electrophysiology and the hemodynamic response itself.
</p>
<div class="note-box">
<strong>Apply the same rule to fNIRS</strong>
<p>
If the hemodynamic side is fNIRS rather than fMRI, the same caution remains. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015)</a> showed that short-separation regression improves statistical significance and localization for tasks with differing autonomic responses. On this site, an fNIRS branch without <strong>short-separation / superficial diagnostic</strong> is therefore not treated as a direct neural-difference readout either.
</p>
</div>

<h3>4. EEG + PET + MRI adds arousal-state fusion, not fused ground truth</h3>
<p>
The newest route that needed to be fixed here is tri-modal EEG-PET-MRI. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed that simultaneous EEG-PET-MRI can reveal tightly coupled global hemodynamic and metabolic progression together with distinct network structure across wakefulness and NREM sleep. That is a real advance because one protocol can now compare electrophysiological arousal, hemodynamic fluctuations, and metabolic decline under the same experimental window. But the safe reading still stops well short of fused ground truth: PET quantification remains model-bearing, the hemodynamic side still carries vascular interpretation, and the fusion step itself still needs a disclosed baseline over each unimodal route. On this site, tri-modal results therefore still require a <a href="../verification.html#fusion-card">Fusion Card</a> rather than being treated as automatic cross-stack state identification.
</p>
<p>
The temporal object is also split inside the same session. <a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">Ripp et al. (2021)</a> showed in simultaneous FDG-PET/fMRI working-memory data that PET still had to be interpreted through <strong>scan-window averages</strong> rather than event-scale timing, and <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> used EEG-PET-MRI to follow sleep-stage electrophysiology together with slower hemodynamic and metabolic progression. Therefore, on this site, tri-modal synchrony is read as <strong>coordinated multi-timescale evidence</strong> unless the paper explicitly shows how second-scale electrophysiology, hemodynamic response windows, and PET kernels are being compared.
</p>
<p>
The deeper correction added in this pass is that even a <strong>shared</strong> tri-modal factor is not automatically the target neural variable, and not yet a quantity bridge. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that low-frequency global fMRI fluctuations covary with EEG and multiple autonomic signals as part of a distributed arousal response, <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al. (2019)</a> showed that sympathetic activity can contribute to fMRI signal changes during EEG-marked arousal events, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can oppose oxygen-metabolism changes across many cortical voxels. Therefore, when a multimodal paper reports a coupled global trajectory, this site now asks whether the claimed factor is <strong>shared neural candidate</strong>, <strong>mixed arousal physiology</strong>, or only a <strong>common low-frequency mode with unresolved specificity</strong>, and whether the paper has actually exposed a named <strong>quantity bridge / physiology-grounding rule</strong> rather than only a correlation.
</p>

<h3>5. More modalities can help without making the bundle stable by default</h3>
<p>
The next correction is operational rather than geometric. A multimodal paper can improve prediction or uncertainty while still leaving the bundle fragile to missing modalities, site shifts, or hard-subgroup disagreement. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a> showed in acute brain injury that increasing the number of assessment modalities decreased uncertainty and improved prognostic accuracy. That is a genuine bundle-level advance. But <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> showed that direct same-sample multimodal model comparisons used <strong>48 patients with all available features</strong>, and also noted that the combined EEG-feature same-sample model improved positive predictive value and sensitivity only alongside a <strong>markedly decreased sample size</strong>. In other words, a multimodal gain can depend materially on which cases actually carry the full bundle.
</p>
<p>
<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> then showed the second half of the problem. Their second-level multimodal classifiers explicitly substitute <strong>missing values with -1</strong>, test diagnostic generalization from France to datasets from <strong>Germany and Italy</strong>, and report that pairwise disagreements across unimodal predictions are higher in <strong>minimally conscious</strong> and <strong>improving</strong> patients than in simpler groups. Therefore, on this site, a multimodal result is not upgraded from ``bundle performance improved'' to ``robust same-subject cross-stack evidence'' unless it discloses <strong>availability slice</strong>, <strong>missing-modality policy</strong>, <strong>transfer window</strong>, and <strong>hard-regime disagreement</strong>.
</p>

<h3>6. EEG + invasive recording is strong as a calibration route, but coverage is narrow</h3>
<p>
Zhang et al. (2006) used simultaneous scalp EEG/ECoG to show that the main spatial patterns of cortical potential reconstructions can be preserved with realistic FEM and co-registered MRI/CT. Seeber et al. (2019) also showed that deep signals are conditionally detectable using 256ch scalp EEG and simultaneous DBS recording. However, these only strengthen the area visible in the invasion record, and do not guarantee unmeasured areas.
</p>

<h3>7. OPM-MEG expands movement tolerance, but not without magnetic-field and source-model audits</h3>
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
<li><strong>same-session / atlas-informed:</strong>Do not read this as one validated biological state variable unless a <a href="../verification.html#fusion-card">Fusion Card</a> discloses acquisition relation, lag audit, <strong>effective-window / temporal-kernel relation</strong>, co-registration scope, shared-vs-specific component logic, unimodal / prior-only baselines, availability / complete-case slice, and external calibration.</li>
<li><strong>multimodal gain:</strong>Do not read ``more modalities improved performance'' as availability-agnostic or centre-robust unless the page discloses missing-modality handling, transfer across sites / scanners / protocol shifts, and whether disagreement rises in the hardest subgroups.</li>
<li><strong>EEG + MRI:</strong>Even if individual anatomy is included, if there is no external validation, the source claim will be limited. </li>
<li><strong>EEG + fMRI:</strong>It is useful as a complement to spatial information, but requires auditing of artifacts, safety, time series alignment, and vascular-state / CVR limits before a BOLD difference is read as a neural difference. </li>
<li><strong>EEG + PET + MRI:</strong>Read as a stronger shared acquisition window for electrophysiology, hemodynamics, and metabolism, not as fused latent-state truth; also state whether the comparison is across <strong>event-scale electrophysiology</strong>, a <strong>hemodynamic response window</strong>, or a <strong>scan-window / kinetic PET route</strong>. If a shared factor is claimed, write whether it is shared neural candidate, modality-specific residual, or physiology-linked global factor, and if the argument raises a living-human claim ceiling also attach a <a href="../verification.html#human-proxy-composition-card">Human Proxy Composition Card</a>.</li>
<li><strong>EEG + fNIRS:</strong>Short-separation / superficial diagnostic is required before HbO / HbR differences are treated as neural differences. </li>
<li><strong>EEG + invasive recording:</strong>Treated as a coverage-limited calibration/validation route, not a gold standard. </li>
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
<li>Kothe, C., Shirazi, S. Y., Stenner, T., Medine, D., Boulay, C., Grivich, M. I., Artoni, F., Mullen, T., Delorme, A., &amp; Makeig, S. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H., Jafarian, A., Zeidman, P., Litvak, V., Razi, A., Garrido, M., Friston, K., &amp; Daunizeau, J. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <em>NeuroImage</em>, 211, 116595. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Nguyen, T., Potter, T., Nguyen, T., Karmonik, C., Grossman, R., &amp; Zhang, Y. (2016). EEG Source Imaging Guided by Spatiotemporal Specific fMRI: Toward an Understanding of Dynamic Cognitive Processes. <em>Neural Plasticity</em>, 2016, 4182483. <a href="https://doi.org/10.1155/2016/4182483" target="_blank">doi:10.1155/2016/4182483</a></li>
<li>Ripp, I., Wallenwein, L. A., Wu, Q., Emch, M., Koch, K., Cumming, P., &amp; Yakushev, I. (2021). Working memory task induced neural activation: A simultaneous PET/fMRI study. <em>NeuroImage</em>, 237, 118131. <a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">doi:10.1016/j.neuroimage.2021.118131</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., O'Connor, D., Markicevic, M., Shen, X., Ge, X., Herman, P., Hyder, F., Papademetris, X., Chakravarty, M., Crair, M. C., Constable, R. T., Lake, E. M. R., &amp; Pessoa, L. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>, 15, 229. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., Catana, C., Polimeni, J. R., Fan, J., Droppa, K. S., Patel, R., Wey, H.-Y., Chang, C., Manoach, D. S., Price, J. C., Sander, C. Y., &amp; Rosen, B. R. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>, 16, 8887. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T. S., van den Brink, R. L., Song, C., et al. (2025). Autonomic physiological coupling of the global fMRI signal. <em>Nature Neuroscience</em>, 28, 1266-1278. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Özbay, P. S., Chang, C., Picchioni, D., et al. (2019). Sympathetic activity contributes to the fMRI signal. <em>Communications Biology</em>, 2, 421. <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Rohaut, B., Calligaris, C., Hermann, B., et al. (2024). Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. <em>Nature Medicine</em>, 30, 2349-2355. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Amiri, M., Andelic, N., Westhall, E., et al. (2023). Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. <em>Brain</em>, 146(1), 50-69. <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/brain/awac335</a></li>
<li>Manasova, D., Hermann, B., Calligaris, C., et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <em>Brain</em>. <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/brain/awaf412</a></li>
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
