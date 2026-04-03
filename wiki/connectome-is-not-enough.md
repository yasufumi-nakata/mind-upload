---
layout: default
title: 'Wiki: Why wiring diagrams alone are not enough'
description: We will summarize the reasons why storing only the connectome in WBE
  is insufficient, including the lack of state variables such as activity-dependent
  transcription / chromatin state, post-transcriptional RNA-state, phospho-signaling / second-messenger state, local proteostasis / synaptic tagging, presynaptic
  release-machinery / active-zone nanostructure state, cargo-transport / cytoskeletal
  trafficking state, perisynaptic extracellular matrix, ionic milieu / chloride
  homeostasis, shared extracellular / electrical state, thermal-state, bioenergetic
  / mitochondrial state, neurovascular-unit / BBB / pericyte state, glial
  substrate-routing, astrocyte-state, and clearance / immune support, as well
  as the limitations of connectome-constrained estimation, based on primary
  literature.
article_type: Wiki
subtitle: connectome-complete is not emulation-complete
author: Mind Uploading Research Project
last_updated: '2026-04-04'
note: Technical / natural science only
audience: People who want to judge whether the wiring diagram is close to WBE based
  only on technology and natural science.
reading_time: 15-20 minutes
page_intro: This page is a page to analyze the intuition that ``If we can obtain the
  connectome, it would be sufficient to reproduce the brain'' based on primary literature.
  Rather than focusing on philosophy or legal systems, I will focus on what state
  variables can't be said if they are missing, and what putative barriers remain even
  in connectome-constrained.
accuracy_note: What I'm showing here is an arrangement of ``at least removing this
  will weaken the argument'' and ``degeneracy that remains even if wiring constraints
  are included'', and does not mean that the final sufficient condition has been determined.
page_highlights:
- We will organize the points that cannot be solved by wiring diagrams alone into
  19 state classes and 1 presumed wall.
- "Current synaptic-state is not treated as one scalar here: synapse count, regional synaptic-density proxy, release-site number, active-zone nanostructure / priming-site assembly, docked-vesicle architecture, and current release competence are kept separate."
- Use only primary literature to separate missing state variables from parameter degeneracy.
- We will also fix operational rules for how to read connectome-complete and connectome-constrained
  model on this site.
- "Flagship connectome results are split into five evidence classes here: wiring atlas, same-brain local scaffold, human macro pathway prior / tractography connectome, connectome-constrained conditional predictor, and identifiability audit."
- "Same-brain functional connectomics is now kept behind a sequential-bridge / label-transfer / current-synaptic-state / dynamical-identifiability split, so digital-twin wording is not read as a solved local twin."
- "Connectome-constrained predictors now need a conditional-model route card that names the structural prior, fitted degrees of freedom, task/state regime, omitted mechanisms, validation route, and abstention boundary."
- Rather than ending with enumeration, we use augmentation/ablation to fix what should
  be added from connectome-only to read the predictive gain.
- "Timing-state is treated as more than a single delay constant: activity-dependent oligodendrogenesis, node/internode/periaxonal microgeometry, plasticity-brake effects, remyelination-to-function recovery, and human quantity-defined myelin or tract-speed proxies are read separately."
- "Thermal-state is treated as another missing layer, because membrane kinetics, synaptic reliability, field-potential amplitude, perturbation timing, and heating artifacts are not implied by graph, delay, or ATP alone."
- "Post-transcriptional RNA-state is treated as another missing layer, because gene-level abundance does not by itself fix isoform choice, m6A-dependent translation / degradation, or RNA-editing ratio."
- "Phospho-signaling / second-messenger state is treated as another missing layer, because transcript or bulk protein abundance does not by itself fix phosphosite occupancy, kinase/phosphatase balance, or signaling nanodomains."
- "Cargo-transport / cytoskeletal trafficking is treated as another missing layer, because receptor, endosome, RNA, and presynaptic cargo delivery are not implied by graph, weight, or ATP alone."
- "Ionic milieu / chloride homeostasis is treated as another missing layer, because inhibition sign and sleep/wake state can still shift with local chloride set point and interstitial ion composition even on the same graph."
- "Chemical connectome is not shared extracellular / electrical-state complete: gap junctions, endogenous field effects, extracellular-space geometry / diffusion barriers / osmotic regime, and inhibitory-driving-force state remain separate variables, and route-card disclosure is now required."
- "Bioenergetic / mitochondrial evidence is treated as another missing layer, because local ATP reserve, mitochondrial positioning/fission, ATP-synthase nano-organization, and Ca2+-efflux tuning are not implied by graph or macro energetic imaging alone."
- "Neurovascular-unit / BBB / pericyte evidence is treated as another missing layer, because vascular transfer audit, human BBB water-exchange, tracer-specific BBB transport, and blood-CSF-barrier / choroid-plexus routes do not by themselves fix the local controller state."
- "Glial substrate-routing is treated as another missing layer, because lactate-shuttle support, starvation ketone-body export, intensive-learning glia-to-neuron fatty-acid flux, and apoE / sortilin-dependent lipid delivery do not answer the same supplier-fuel-sink question."
- "Astrocyte-state is treated as another missing layer, because minute-scale network encoding, recall ensembles, multiday stabilization, and target-defined human MAO-B or I2BS astrocyte-related PET routes do not all answer the same question."
- "Clearance / immune support is treated as another missing layer, because meningeal drainage anatomy, microglia-linked synaptic control, human CSF oscillation / parenchyma-CSF exchange / intrathecal-tracer / CSF-mobility / biomarker-efflux routes do not all answer the same question."
- "A diffusion-MRI-derived human connectome is treated as an algorithm- and resolution-conditioned macro pathway prior or targeted bundle hypothesis route, not as a synapse-resolved edge list."
- "Within tractography itself, cortical endpoint assignment and parcel-graph construction are separate walls, so tractography graphs and hub maps are not stable objects by default."
known_points:
- Great progress has been made in creating a whole-brain connectome, but this alone
  does not mean that dynamic reproduction is complete.
- Synapse count and regional SV2A density still do not directly fix release-site
  number, active-zone nanostructure / priming-site assembly, docked-vesicle architecture,
  or current release competence.
- Synaptic efficiency, activity-dependent transcription / chromatin state, timing-state,
  thermal-state, post-transcriptional RNA-state,
  phospho-signaling / second-messenger state,
  ionic milieu / chloride homeostasis, shared extracellular / electrical state,
  neuromodulation, bioenergetic / mitochondrial state,
  neurovascular-unit / BBB / pericyte state, glial substrate-routing, astrocyte-state,
  clearance / immune support, cell type labels, intrinsic excitability/homeostasis
  set points, and local proteostasis / synaptic-tagging state are pieces of information
  that are likely to fall off a static edge list, cargo-transport / cytoskeletal
  trafficking state is another, and perisynaptic ECM / PNN state is another.
- Confusing coarse physiological proxies with ground truths makes it easy to overstate
  claims about internal states.
- "Human support-state observability is already internally split: BBB water exchange, tracer-specific BBB transport, choroid-plexus / blood-CSF-barrier routes, CSF oscillation, parenchyma-CSF exchange, intrathecal-tracer clearance, CSF mobility, and model-based biomarker efflux are not one reusable meter."
- Even in a connectome-constrained model, dynamics can degenerate if unmeasured cell/synapse/modification
  parameters remain.
- Dorkenwald et al. (2024), MICrONS Consortium et al. (2025), Thomas et al. (2014), Donahue et al. (2016), Schilling et al. (2020), Grisot et al. (2021), Lappalainen et al. (2024), and Beiran & Litwin-Kumar (2025) support different kinds of progress and should not be collapsed into one story that connectome is "almost enough."
- Same-brain functional connectomics strengthens specimen identity and local structure-function correspondence more than atlas priors do, but it still remains a sequential bridge and local conditional-prediction route rather than direct transcriptomic truth, current synaptic-state readout, or unique local dynamics.
- A tractography-derived graph can still change at the cortical-endpoint and parcel-graph stage even when the underlying diffusion signal is the same.
- Conditional predictions can be improved by adding same-brain function, transcriptomics,
  neuromodulatory dynamics, thermal logs, energetic support, glial substrate-routing,
  astrocyte-state, neurovascular support, and clearance support, but the improvement
  depends on the task, time constant, and external validation conditions.
- Device latency audit and biological timing-state audit are different requirements; passing
  one does not automatically pass the other.
- Timing-state claims now require claim-family, structural-unit, recovery-boundary, and human quantity-type disclosure; a tract-speed or myelin MRI row still remains a macro proxy unless externally calibrated.
unknown_points:
- It is unclear which state class and resolution should be taken to approach the sufficient
  condition for WBE.
- The extent to which missing state variables can be compensated for by estimation
  or coarse-graining is an issue for future verification.
- It is not yet fixed which animal/invasive system should be used to calibrate conditions
  that cannot be directly obtained in humans, including cell-specific timing-state.
- It has not yet been systematically determined to what extent degeneracy can be resolved
  when adding same-brain functions.
- Which order of augmentations most efficiently reduces which error terms still varies
  from dataset to dataset.
wiki_links:
- label: 'Wiki: Basics of WBE'
  url: /wiki/mind-upload-basics.html
  description: Let's organize the overall picture that forms the premise of this argument
    from the beginning.
- label: 'Wiki: Homeostatic plasticity and maintenance state'
  url: /wiki/homeostatic-plasticity-and-maintenance-state.html
  description: We take a deep dive into why intrinsic excitability, sleep-homeostasis,
    and myelin/metabolic maintenance are separate variables.
- label: 'Wiki: Decode and Emulate'
  url: /wiki/decode-vs-emulate.html
  description: Sort out the differences between output translation and internal generation.
- label: 'Wiki: How to read claims and evidence'
  url: /wiki/claims-and-evidence.html
  description: You can check how much evidence and how strong a claim is allowed.
recommended_pages:
- label: Introduction to WBE
  url: /wbe_101.html
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
Although wiring diagrams are an important foundation for WBE,<strong>alone are not the minimum requirement for dynamic reproduction</strong>. Even within the same adjacency relationship, differences in cell type labeling, activity-dependent transcription / chromatin program, post-transcriptional RNA-state, phospho-signaling / second-messenger state, intrinsic excitability, synaptic efficiency, presynaptic release-machinery / active-zone nanostructure state, local proteostasis / synaptic-tagging route, cargo-transport / cytoskeletal trafficking route, perisynaptic ECM / PNN organization, ionic milieu / chloride homeostasis, shared extracellular / electrical state, timing-state / conduction support, thermal-state, neuromodulatory occupancy / release state, bioenergetic / mitochondrial support, neurovascular-unit / BBB / pericyte controller state, glial substrate-routing, astrocyte-state, and clearance / immune support can significantly alter learning, phase synchronization, arousal-dependent responses, inhibitory sign, state transitions, and long-term stability. Furthermore, connectome-constrained modeling research in 2024-2025 showed that even with the inclusion of wiring constraints, degeneracy in dynamics remains due to unmeasured parameters and omitted mechanisms. Therefore, this site treats<strong>connectome-complete as a structural atlas/scaffold achievement</strong> and not as<strong>emulation-complete</strong>. Similarly, the fact that a<strong>connectome-constrained model reproduced some activities</strong> cannot be read as state-complete reconstruction. This warning becomes even stronger when the word <strong>connectome</strong> refers only to a diffusion-MRI-derived human tractography product, because current validation literature supports that object as a macro pathway prior rather than a synapse-resolved edge list.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. From only the aspects of technology and natural science, we will clarify ``what state variables are missing and what cannot be claimed?'' and ``what cannot be uniquely determined even if wiring constraints are included.''
</p>
</div>

<section class="section" id="bottom-line">
<h2 class="section-title">19 state classes and 1 putative wall to fix first</h2>
<table class="data-table">
<thead>
<tr>
<th>State class</th>
<th>What is missing with just a wiring diagram</th>
<th>Dangerous misreading</th>
<th>Currently handling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cell type label</strong></td>
<td>Even with the same adjacency relationship, different transcript types have different binding motifs, synaptic properties, and myelination tendencies. </td>
<td>The physical meaning of the circuit is the same even if it is an unlabeled graph. </td>
<td>Stay with the structural atlas and candidate scaffold unless tied to the same-brain transcriptomics / physiology. </td>
</tr>
<tr>
<td><strong>Activity-dependent transcription / chromatin state</strong></td>
<td>Even with the same graph and cell-type label, allocation eligibility, late memory-stabilization programs, and locus-specific plasticity rules can still change over hours to weeks, and the measured object may be accessibility, histone chemistry, DNA-methylation control, higher-order looping, or locus-specific editing rather than one generic epigenetic row. </td>
<td>A cell atlas, one-shot DEG list, or one epigenetic assay means that the current plasticity-competent program is already fixed. </td>
<td>Treat static transcriptomic labels or single-object epigenetic assays as identity / object priors; keep memory-stabilization controller explicit as latent unless temporal or causal evidence is shown. </td>
</tr>
<tr>
<td><strong>Post-transcriptional RNA-state</strong></td>
<td>Even with the same graph, cell-type label, and gene-level abundance, splice isoform choice, m6A-dependent translation / degradation, and RNA-editing ratio can still differ over the relevant cells and compartments.</td>
<td>If transcript counts look similar, the operative RNA controller is already fixed too.</td>
<td>Treat gene-level abundance as insufficient; keep isoform / m6A / editing controller explicit as latent unless directly measured, causally perturbed, or externally calibrated.</td>
</tr>
<tr>
<td><strong>Phospho-signaling / second-messenger state</strong></td>
<td>Even with the same graph, transcript state, and bulk protein abundance, phosphosite occupancy, kinase/phosphatase balance, and compartment-specific second-messenger nanodomains can still differ over the relevant cells and compartments.</td>
<td>If transcript or protein abundance looks similar, the active phospho-controller is already fixed too.</td>
<td>Treat abundance-only evidence as insufficient; keep phospho-signaling explicit as latent unless directly measured, causally perturbed, or externally calibrated.</td>
</tr>
<tr>
<td><strong>Intrinsic excitability/homeostasis set point</strong></td>
<td>Even with the same cell type and graph, if the target values ​​for ion channel expression, threshold, gain, and firing rate are different, the response and recovery method to the same input will change. </td>
<td>The long-term dynamics are largely determined by cell-type labels and short activity matches. </td>
<td>Unless you're measuring threshold / gain / recovery / homeostatic controller, keep claims about long-term stability or memory allocation with latent state. </td>
</tr>
<tr>
<td><strong>Synaptic efficiency/short-term state</strong></td>
<td>The presence or absence of edges alone cannot determine weights, release probability, release-site number, active-zone nanostructure / priming-site assembly, short-term plasticity, and LTP/LTD history. </td>
<td>Edge count, synapse count, or a regional synaptic-density proxy can be read as current release competence. </td>
<td>Although it is possible to describe static wiring, it does not claim current presynaptic release machinery, L2 intervention prediction, or L3 closed-loop stability. </td>
</tr>
<tr>
<td><strong>Local proteostasis / synaptic-tagging state</strong></td>
<td>Even with the same graph and current weights, tagged spines and branches can still differ in PRP capture, translation/degradation balance, and late-stabilization persistence. </td>
<td>If the current weight is estimated, the late-stabilization route is also basically fixed. </td>
<td>Unless the tag/capture/proteostasis route is measured, perturbed, or externally calibrated, keep late stabilization and reconsolidation claims as latent state. </td>
</tr>
<tr>
<td><strong>Cargo-transport / cytoskeletal trafficking state</strong></td>
<td>Even with the same graph, current weights, and local translation capacity, receptors, endosomes, RNA cargoes, mitochondria, and presynaptic components can still be delivered, paused, or retained at different branches, spines, and boutons.</td>
<td>If local translation or ATP supply is discussed, then the right cargo will also have reached the right compartment.</td>
<td>Unless cargo-delivery route is measured, perturbed, or externally calibrated, keep compartment-specific stabilization, receptor localization, and synaptogenesis claims as latent state.</td>
</tr>
<tr>
<td><strong>Perisynaptic ECM / PNN state</strong></td>
<td>Extracellular matrix organization can change receptor mobility, inhibitory plasticity, memory-update resistance, and adult plasticity even on the same synapse graph. </td>
<td>Once synapses and weights are listed, the plasticity gate and stabilization state are basically fixed too. </td>
<td>Unless ECM / PNN state is measured, perturbed, or externally calibrated, keep adult plasticity and stabilization claims as latent state. </td>
</tr>
<tr>
<td><strong>Ionic milieu / chloride homeostasis</strong></td>
<td>Even with the same graph, cell type, and nominal synaptic weights, local chloride set point, transporter state, and extracellular K<sup>+</sup> / Ca<sup>2+</sup> / pH composition can still change inhibitory sign, network gain, and state transitions.</td>
<td>If the graph and synapses are the same, the sign of inhibition and the local brain-state regime are also basically fixed.</td>
<td>Demote inhibitory-polarity, rhythm-stability, and state-transition claims unless ionic / chloride state is measured, perturbed, externally calibrated, or explicitly left latent.</td>
</tr>
<tr>
<td><strong>Shared extracellular / electrical state</strong></td>
<td>Even with the same chemical graph, gap-junction coupling, endogenous electric fields, and local inhibitory driving force can still alter fast synchrony, spike timing, oscillatory coordination, and state-switch thresholds.</td>
<td>Once chemical synapses and nominal weights are listed, electrical coupling and electrotonic regime are basically fixed too.</td>
<td>Demote fast-synchrony, oscillatory-coordination, and electrical-state claims unless electrical coupling / field state is measured, perturbed, externally calibrated, or explicitly left latent.</td>
</tr>
<tr>
<td><strong>Timing-state / conduction support</strong></td>
<td>Even with the same graph, differences in activity-dependent oligodendrogenesis, node/internode geometry, periaxonal nanocircuit state, plasticity-brake state, or remyelination state can change conduction speed, spike-arrival timing, synchrony, and recovery. </td>
<td>If the graph is the same, timing can be absorbed into one scalar delay, and any human myelin or tract-speed paper is already close to per-axon timing ground truth. </td>
<td>Demote phase, synchrony, plasticity-window, and recovery-sensitive claims unless timing-state is typed, measured, externally calibrated, or explicitly left latent. </td>
</tr>
<tr>
<td><strong>Thermal-state</strong></td>
<td>Even with the same graph, timing-state, and ATP support, local tissue temperature can still change membrane kinetics, release probability, field-potential amplitude, and perturbation burden.</td>
<td>If delay, ATP, or a generic heating note is present, the thermal operating point is already fixed.</td>
<td>Demote operating-point, sequence-timing, and thermal-confound claims unless local temperature, heating burden, or thermal perturbation route is measured, externally calibrated, or explicitly left latent.</td>
</tr>
<tr>
<td><strong>Neuromodulatory occupancy / release state</strong></td>
<td>Arousal level, learning rate, and gain adjustment cannot be restored with static wiring alone, and pupil diameter and HRV remain as rough proxies. </td>
<td>pupil / HRV or global arousal can be read as a single transmitter ground truth. </td>
<td>It can be used for covariates and stratification in human data, but it is not written as transmitter-specific or region-specific ground truth. </td>
</tr>
<tr>
<td><strong>Bioenergetic / mitochondrial state</strong></td>
<td>Even with the same graph and nominal activity fit, branch/bouton ATP reserve, mitochondrial positioning / fission, ATP-synthase nano-organization, and Ca<sup>2+</sup>-efflux tuning can still differ.</td>
<td>If a macro energetic proxy or ATP-related sentence is present, the local energetic controller is already fixed.</td>
<td>Demote high-demand plasticity, fatigue-resilience, and local metabolic-support claims unless energetic route, controller manipulation, or external calibration is measured and disclosed.</td>
</tr>
<tr>
<td><strong>Neurovascular-unit / BBB / pericyte state</strong></td>
<td>Even with the same graph and nominal neural state, capillary-diameter control, BBB permeability, neurovascular coupling, and pericyte / endothelial support logic can still differ.</td>
<td>If vascular confounds are audited or one human BBB / BCSFB proxy exists, the relevant controller state is almost solved.</td>
<td>Demote neurovascular-maintenance and barrier-controller claims unless controller-side biology, barrier route family, macro proxy class, and calibration ceiling are named separately.</td>
</tr>
<tr>
<td><strong>Glial substrate-routing</strong></td>
<td>Even with the same graph, energetic proxy, and astrocyte label, supplier cell, neuronal sink, fuel object / carrier, and regime trigger can still differ across lactate, ketone-body, fatty-acid, and apoE / sortilin-linked lipid routes.</td>
<td>If a macro energetic proxy, astrocyte-related PET signal, or generic glial-support sentence exists, the operative glial fuel route is already fixed.</td>
<td>Keep supplier-fuel-sink routing explicit as latent unless the route family, supplier cell, neuronal sink, fuel object / carrier, regime trigger, and observability ceiling are directly measured, perturbed, externally calibrated, or openly left latent.</td>
</tr>
<tr>
<td><strong>Astrocyte-state</strong></td>
<td>Even with the same graph, minute-scale network encoding, recall ensembles, fear-state representations, and multiday stabilization ensembles can still differ.</td>
<td>Generic glial support or a human MAO-B / I<sub>2</sub>BS astrocyte-related PET route means the operative astrocyte state is already fixed.</td>
<td>Demote astrocyte-dependent plasticity, recall, and slow-state claims unless the astrocyte observable, perturbation route, or proxy ceiling is disclosed.</td>
</tr>
<tr>
<td><strong>Clearance / immune support</strong></td>
<td>Even with the same graph and astrocyte support, meningeal drainage, CSF-interstitial exchange, and microglia-linked synaptic maintenance can still differ over multiday windows.</td>
<td>Clearance is passive cleanup, or one human CSF / glymphatic route already fixes the local immune controller.</td>
<td>Demote multiday maintenance, recovery, and local immune-controller claims unless clearance / immune route family, transport object or target class, proxy class, and calibration ceiling are disclosed separately.</td>
</tr>
<tr>
<td><strong>Parameter degeneracy (estimated wall)</strong></td>
<td>Even models with the same connectome or similar outputs can have multiple internal dynamics if the unknown parameters of cells and synapses are different. </td>
<td>Connectome-constrained means that the internal state is almost unique. </td>
<td>We do not write that it is close to the unique solution unless it involves family comparison, uncertainty, held-out perturbation, and abstention. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Missing variables added this time</strong>
<p>
The March 2026 re-audits first split <strong>intrinsic excitability / homeostasis set point</strong> from cell-type labels and <strong>perisynaptic ECM / PNN state</strong> from synaptic state. The later passes added <strong>activity-dependent transcription / chromatin state</strong>, <strong>post-transcriptional RNA-state</strong>, <strong>phospho-signaling / second-messenger state</strong>, <strong>local proteostasis / synaptic-tagging state</strong>, <strong>cargo-transport / cytoskeletal trafficking state</strong>, and <strong>ionic milieu / chloride homeostasis</strong>. This pass completes the maintenance-side family list on this page by adding <strong>thermal-state</strong>, <strong>bioenergetic / mitochondrial state</strong>, <strong>neurovascular-unit / BBB / pericyte state</strong>, <strong>glial substrate-routing</strong>, <strong>astrocyte-state</strong>, and <strong>clearance / immune support</strong> as independent rows instead of letting them hide inside generic glia, vascular nuisance, or slow-support language. The reason is that even if we have cell-type labels, synapse counts, connectomes, and a weight estimate, membrane operating point, local ATP reserve, supplier-fuel-sink routing, pericyte / BBB control, astrocyte ensemble state, and multiday clearance support can still vary. A more detailed arrangement of these maintenance-side variables is collected in <a href="homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>.
</p>
</div>
</section>

<section class="section" id="connectome-progress">
<h2 class="section-title">Wiring diagram research has made great progress, but it is not the end in itself</h2>
<p>
Dorkenwald et al. (2024), MICrONS Consortium et al. (2025), the tractography-validation literature from Thomas et al. (2014), Reveley et al. (2015), Donahue et al. (2016), Maier-Hein et al. (2017), Schilling et al. (2020), and Grisot et al. (2021), Lappalainen et al. (2024), and Beiran &amp; Litwin-Kumar (2025) changed the connectome discussion qualitatively. However, they did not all solve the same problem. The first gave a whole-adult-brain wiring atlas in fly, the second co-registered function and ultrastructure within one awake mouse visual-cortex volume, the tractography papers showed what can and cannot be inferred about long-range pathways from diffusion-MRI orientation data, the next showed that a connectome-constrained and task-optimized model can predict rich activity in a fly visual subsystem, and the last showed theoretically that a connectome often still does not uniquely determine recurrent dynamics when biophysical parameters remain uncertain. Therefore, the correct reading is not “the connectome is nearly enough,” but rather that <strong>different papers remove different uncertainties while leaving other uncertainties intact</strong>.
</p>
<p>
The missing split is even narrower than that. <a href="https://doi.org/10.1523/JNEUROSCI.4493-13.2014" target="_blank">Graydon et al. (2014)</a> showed that synapse-adjacent postsynaptic morphology changes extracellular dilution and transmitter signaling, while <a href="https://doi.org/10.1002/jnr.20871" target="_blank">Kilb et al. (2006)</a> and <a href="https://doi.org/10.1177/1759091415605115" target="_blank">Lauderdale et al. (2015)</a> showed that osmotic ECS contraction / edema can rapidly shift excitability. Therefore the missing variable is not only <strong>electrical coupling</strong>, but also <strong>extracellular-space width / diffusion constraint / osmotic regime</strong>. A chemical connectome can stay fixed while local spillover, dilution, and state-switch threshold still move.
</p>
<div class="note-box">
<strong>How this site now reads “connectome progress”</strong>
<p>
On this site, connectome-related progress is now separated into five evidence classes before any WBE claim is read: <strong>(1) wiring atlas</strong>, <strong>(2) same-brain local structure-function scaffold</strong>, <strong>(3) human macro pathway prior / tractography connectome</strong>, <strong>(4) connectome-constrained conditional predictor</strong>, and <strong>(5) identifiability / degeneracy audit</strong>. Collapsing these into one slogan such as “the connectome is almost enough” is too weak, because each class answers a different question and leaves a different ceiling in place.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Evidence class</th>
<th>Representative result</th>
<th>What primary literature directly advances</th>
<th>What it still does not support</th>
<th>How this site reads it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Wiring atlas</strong></td>
<td>Dorkenwald et al. (2024)</td>
<td>A whole-adult-brain fly connectome with about 130,000 neurons, about 5 x 10<sup>7</sup> chemical synapses, and linked annotations for cell classes, types, and neurotransmitter predictions.</td>
<td>Current synaptic efficacy, timing-state, ionic regime, neuromodulation, glial coupling, or whole-state dynamics.</td>
<td>Read as a <strong>structural atlas / scaffold achievement</strong>, not as emulation-complete state capture.</td>
</tr>
<tr>
<td><strong>Same-brain local structure-function scaffold</strong></td>
<td>Bosch et al. (2022); MICrONS Consortium et al. (2025); Ding et al. (2025)</td>
<td>Sequential same-brain bridges between in vivo activity and later ultrastructure, local structure-function correspondences, and validated stimulus-conditioned response models within the measured region / task.</td>
<td>Same-time whole-brain or all-state capture, direct transcriptomic truth inside the EM volume, current synaptic efficacy / release state, unique dynamical parameterization, or general human observability.</td>
<td>Read as a <strong>sequential same-brain local scaffold plus task-bounded conditional predictor</strong>, not as a solved local twin or state-complete template.</td>
</tr>
<tr>
<td><strong>Human macro pathway prior / tractography connectome</strong></td>
<td>Thomas et al. (2014); Donahue et al. (2016); Schilling et al. (2020); Grisot et al. (2021)</td>
<td>Macro white-matter pathway priors, parcel-level connectivity clues, and targeted bundle reconstructions when strong anatomical start / end / exclusion constraints are supplied and the tractography route is disclosed.</td>
<td>Synapse-resolved edge completeness, cortical endpoint completeness across the whole brain, directionality, current weights, stable graph metrics independent of filtering / voxel size, or unbiased discovery of all long-range pathways without strong priors.</td>
<td>Read as an <strong>algorithm-conditioned macro pathway prior / bundle-level hypothesis route</strong>, not as an edge-complete human connectome.</td>
</tr>
<tr>
<td><strong>Connectome-constrained conditional predictor</strong></td>
<td>Lappalainen et al. (2024)</td>
<td>Detailed neural-activity predictions across the fly visual system when connectome structure is combined with task optimization, strongly reducing free parameters and yielding single-neuron-scale hypotheses.</td>
<td>Unique recovery of internal state, arbitrary tasks, or omitted mechanisms such as electrical synapses, nonlinear chemical synapses, and neuromodulation that the authors explicitly leave out.</td>
<td>Read as a <strong>conditional model / hypothesis engine</strong>, not as proof that connectome plus fitting recovers all missing state.</td>
</tr>
<tr>
<td><strong>Identifiability / degeneracy audit</strong></td>
<td>Beiran &amp; Litwin-Kumar (2025)</td>
<td>A formal result that even networks sharing the same synaptic weights can diverge strongly in dynamics when biophysical parameters differ, while a small subset of activity recordings can reduce the degeneracy.</td>
<td>A claim that connectome-only is sufficient, or conversely that connectome is useless once recordings are added.</td>
<td>Read as the reason <strong>connectome-constrained is not unique by default</strong>; additional recordings, family comparison, and abstention rules remain necessary.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03-30 addendum: same-brain functional connectomics is a sequential scaffold, not a solved local twin</strong>
<p>
This page still left one practical shortcut too open. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a> showed that bridging in vivo physiology to targeted volume EM requires a correlative multistage workflow that links scales rather than freezing one simultaneous state object. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> then advanced that route with dense calcium imaging of about <strong>75,000 neurons</strong> co-registered to a later EM reconstruction containing more than <strong>200,000 cells</strong> and <strong>0.5 billion synapses</strong> in one awake mouse. <a href="https://doi.org/10.1038/s41586-025-08840-3" target="_blank">Ding et al. (2025)</a> built on the same dataset with a validated stimulus-conditioned response model, but explicitly warned that model internals still need cautious interpretation. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">Gamlin et al. (2025)</a> further improved the cell-type bridge, yet did so through morphology-based prediction of transcriptomic Sst types rather than by direct transcriptomic assay inside the EM volume. On the synaptic side, <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">Holler et al. (2021)</a> described unresolved synaptic-strength structure as a key limitation for inferring brain function from wiring diagrams, <a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">Dürst et al. (2022)</a> showed that vesicular release probability strongly determines synaptic strength, and <a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">Mittermaier et al. (2024)</a> showed that membrane-potential state gates synaptic consolidation in human neocortical tissue. Finally, <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> showed that connectome-constrained recurrent networks can remain dynamically degenerate until extra activity recordings reduce the compatible family. Therefore, the safe ceiling here is <strong>sequential same-brain scaffold plus task-bounded conditional prediction</strong>, not direct transcriptomic truth, current synaptic-state readout, or a unique local twin.
</p>
</div>
<div class="note-box">
<strong>2026-04-01 addendum: presynaptic release machinery is not reducible to synapse count or one release-probability scalar</strong>
<p>
Another practical shortcut still remained: readers could mentally collapse <strong>synapse count</strong>, <strong>regional SV2A density</strong>, <strong>release probability</strong>, and <strong>presynaptic release machinery</strong> into one interchangeable object. That is too weak. <a href="https://doi.org/10.7554/eLife.18167" target="_blank">Moln&aacute;r et al. (2016)</a> showed in human pyramidal-to-interneuron synapses that multi-vesicular release and multiple docked vesicles can coexist at one synaptic contact. <a href="https://doi.org/10.1038/s41593-017-0041-9" target="_blank">Sakamoto et al. (2018)</a> showed that presynaptic weight can be set by multiple Munc13-1 supramolecular assemblies that act as independent release sites. <a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">D&uuml;rst et al. (2022)</a> showed that vesicular release probability sets the strength of individual synapses, and <a href="https://doi.org/10.1038/s41593-024-01720-5" target="_blank">Emperador-Melero et al. (2024)</a> showed that CaV2 channel clustering and vesicle priming are mediated by distinct active-zone machineries. Therefore, a connectome row, a synapse count, or a regional synaptic-density PET value does <strong>not</strong> directly reveal <strong>release-site number</strong>, <strong>docked-vesicle architecture</strong>, <strong>active-zone nanostructure / priming-site assembly</strong>, or <strong>current release competence</strong>. On this site, those variables remain explicit latent state unless a route directly assays them.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Wall</th>
<th>What the primary literature now supports</th>
<th>Safe reading on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Sequential bridge wall</strong></td>
<td>Bosch and MICrONS support a powerful same-brain bridge from live physiology to later ultrastructure, but that bridge still carries landmarks, targeted subvolumes, and ordered transformations.</td>
<td>A <strong>sequential same-brain scaffold</strong>, not a simultaneous whole-state sample.</td>
</tr>
<tr>
<td><strong>Label-transfer wall</strong></td>
<td>Gamlin supports morphology-linked prediction of transcriptomic Sst types inside a large EM volume.</td>
<td>A <strong>cell-type bridge with predicted labels</strong>, not direct transcriptomic truth by default.</td>
</tr>
<tr>
<td><strong>Current-synaptic-state wall</strong></td>
<td>Holler, Moln&aacute;r, Sakamoto, D&uuml;rst, Emperador-Melero, and Mittermaier together show that structure-function correspondence still leaves release-site architecture, release probability, and membrane-state-gated consolidation unresolved.</td>
<td>A <strong>structure-function correspondence route</strong>, not current efficacy, release-machinery, or release-state readout.</td>
</tr>
<tr>
<td><strong>Dynamical-identifiability wall</strong></td>
<td>Ding supports validated stimulus-conditioned prediction, while Beiran &amp; Litwin-Kumar show that connectome-constrained dynamics can still remain non-unique.</td>
<td>A <strong>task-bounded conditional predictor</strong>, not one solved local dynamic twin.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Operational rule added here</strong>
<p>
When a paper says that “connectome progress” moves WBE forward, this site now asks <strong>which of the five evidence classes improved</strong>. A stronger claim requires not just more structure, but a narrower remaining latent-state family under the same held-out or perturbed condition.
</p>
</div>
<div class="note-box">
<strong>2026-03-21 addendum: even the graph and node labels need robustness audits</strong>
<p>
Another weakness in older summaries was to treat edge existence and cell labels as if they had already become binary facts once a large EM resource appeared. The primary literature is narrower. <a href="https://doi.org/10.1038/s41586-024-07686-5" target="_blank">Schlegel et al. (2024)</a> showed across three fly hemispheres that edges stronger than ten synapses or at least 0.9% of a target cell type's total inputs persist more than 90% of the time, whereas weaker edges are less reliable and cell types should be treated as predictions or hypotheses to be validated across brains. In mammalian cortex, <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">Gamlin et al. (2025)</a> linked EM connectivity to transcriptomic Sst subtypes through morphology-based prediction from Patch-seq rather than by directly reading transcriptomes out of the connectome itself, and those predicted subtypes differed in axon myelination and synaptic output patterns. Therefore, this site now separates <strong>edge robustness</strong>, <strong>cell-type bridge quality</strong>, and <strong>dynamical sufficiency</strong> instead of treating them as one package.
</p>
</div>
</section>

<section class="section" id="tractography-ceiling">
<h2 class="section-title">Human diffusion-MRI connectome is still a macro pathway prior</h2>
<p>
The earlier version of this site was already strong at saying that a connectome is not state-complete, but it still left one practical ambiguity too open: <strong>what if the “connectome” itself is a diffusion-MRI tractography product from a living human brain?</strong> Primary validation literature does not support reading that object as a synapse-resolved or edge-complete graph. <a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">Thomas et al. (2014)</a> showed that even exceptional ex vivo macaque diffusion data did not yield high anatomical accuracy across tractography methods, with sensitivity/specificity trade-offs that changed by pathway. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">Reveley et al. (2015)</a> showed that superficial white matter can block long-range tracking from roughly half of the cortical surface. <a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">Donahue et al. (2016)</a> found useful but clearly incomplete predictive power for corticocortical connection strength relative to tracer data. <a href="https://doi.org/10.1038/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017)</a> showed in an open tractography challenge that most submissions recovered many invalid bundles, with 64% of systematically recovered bundles absent from the ground truth. <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">Schilling et al. (2020)</a> then showed that high anatomical accuracy is possible mainly when strong start / end / exclusion priors are supplied, and <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">Grisot et al. (2021)</a> localized recurring same-brain errors at branching and turning configurations that are not fixed simply by higher q-space sampling.
</p>
<div class="note-box">
<strong>Site rule for tractography-derived connectomes</strong>
<p>
On this site, a diffusion-MRI-derived human connectome is read as an <strong>algorithm- and resolution-conditioned macro pathway prior</strong> or <strong>targeted bundle hypothesis route</strong>. It can strengthen statements about major white-matter organization, parcel-level pathway likelihood, or bundle-specific anatomical hypotheses. It does <strong>not</strong> become a synapse-resolved edge list, a direction-complete cortical graph, or proof that the living human connectome is already close to WBE-ready capture.
</p>
</div>
<h3 id="tractography-route-card">Tractography connectomes need a route card</h3>
<p>
The earlier wording on this site said "macro pathway prior," which was directionally correct, but still too permissive in practice. It left room for readers to treat any tractography-derived connectome as a stable graph once a modern pipeline had been applied. The newer primary literature argues against that shortcut at multiple stages. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">Reveley et al. (2015)</a> showed that superficial white matter can block long-range tracking from roughly half of the cortical surface, and <a href="https://doi.org/10.1002/hbm.23936" target="_blank">Schilling et al. (2018)</a> showed that tractography endpoints are biased toward gyral crowns across deterministic and probabilistic algorithms, multiple diffusion models, and even very high-resolution data. <a href="https://doi.org/10.1016/j.neuroimage.2023.120376" target="_blank">Sarwar et al. (2023)</a> showed that filtering improves simple tubular bundles much more than complex brain-like architectures, <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">He et al. (2024)</a> showed that tractography filtering can significantly change laterality indices for more than 10% of connections, <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">Gajwani et al. (2023)</a> showed across <strong>40 pipelines</strong> and <strong>44</strong> group-representative reconstructions that hub location is highly variable and that hub connectivity correlates with regional surface area in <strong>69%</strong> of assessed pipelines, <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">McMaster et al. (2025)</a> showed that voxel resolution changes the resulting connectome and recommended resampling to <strong>1 mm isotropic</strong> for robust comparisons, <a href="https://doi.org/10.3389/fnimg.2026.1670604" target="_blank">Bramati et al. (2026)</a> showed on a single <strong>3 T</strong> scanner with uniform processing that common diffusion-sampling schemes can still shift both voxel-wise metrics and tractography outputs, <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">Manzano-Patrón et al. (2025)</a> showed that fibre-orientation uncertainty can be propagated into tractography rather than hidden, and <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">Zhu et al. (2025)</a> improved whole-brain reconstruction by fusing MRI with microscopy. That combination of results means that on this site the phrase <strong>human tractography connectome</strong> is not one object. It is an <strong>acquisition-, endpoint-, graph-construction-, and calibration-conditioned estimate</strong>.
</p>
<div class="note-box">
<strong>What the earlier wording still hid</strong>
<p>
The phrase <strong>macro pathway prior</strong> was correct, but it still compressed three different transformations into one label: <strong>(1) diffusion signal to local orientation estimate</strong>, <strong>(2) orientation estimate to cortical endpoint assignment</strong>, and <strong>(3) endpoints to parcel graph / hub map</strong>. The signal does not directly reveal synapses or direction, the endpoint assignment can still be biased by superficial-white-matter and gyral-entry effects, and the final graph can still move when parcellation, weighting, or thresholding changes. Therefore, two papers that both say <strong>tractography connectome</strong> may still be reporting different inferential objects.
</p>
</div>
<div class="note-box">
<strong>2026-03-26 addendum: acquisition-scheme variance is a separate failure mode</strong>
<p>
One remaining weakness in the older route card was that it mentioned shell / b-value scheme under <strong>direct observables</strong> but still did not make protocol harmonization a separate stop-rule. <a href="https://doi.org/10.3389/fnimg.2026.1670604" target="_blank">Bramati et al. (2026)</a> compared <strong>HARDI</strong>, <strong>clinical multi-shell</strong>, <strong>DSI</strong>, and <strong>HCP-style multi-shell</strong> acquisitions on the <strong>same 3 T scanner</strong> with uniform processing and still found systematic differences in both voxel-wise metrics and tractography outputs. Together with <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">McMaster et al. (2025)</a>, that means a tractography connectome can move not only because endpoints or graph construction changed, but because the <strong>q-space sampling scheme itself</strong> changed. Therefore, this site now treats <strong>acquisition / harmonization audit</strong> as a separate route-card item rather than a footnote under the modality label.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Stage</th>
<th>What is added after the sensor</th>
<th>Why this site still stops the claim</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Signal -&gt; orientation field</strong></td>
<td>Shell / b-value choice, reconstruction model, and local fibre-orientation estimation.</td>
<td>The direct observable remains diffusion signal, not synapse identity, direction, or weight.</td>
</tr>
<tr>
<td><strong>Orientation field -&gt; cortical endpoints</strong></td>
<td>Tracking rule, stopping rule, and white-matter / gray-matter boundary or surface-assignment procedure.</td>
<td>Long-range cortical endpoints can still be hidden or over-assigned to gyral crowns.</td>
</tr>
<tr>
<td><strong>Endpoints -&gt; parcel graph</strong></td>
<td>Parcellation, edge definition, weighting, thresholding, and group-reconstruction scheme.</td>
<td>Hub maps and graph metrics can still move across plausible graph-construction choices.</td>
</tr>
</tbody>
</table>
<table class="data-table">
<thead>
<tr>
<th>Failure mode</th>
<th>What the primary literature shows</th>
<th>Safe claim that survives</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Ground-truth gap</strong></td>
<td><a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">Thomas et al. (2014)</a> and <a href="https://doi.org/10.1038/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017)</a> show that tractography faces intrinsic ambiguity and many invalid bundles even under favorable conditions.</td>
<td>At most a <strong>macro pathway prior</strong>, not an edge-complete connectome.</td>
</tr>
<tr>
<td><strong>Endpoint invisibility / gyral bias</strong></td>
<td><a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">Reveley et al. (2015)</a> and <a href="https://doi.org/10.1002/hbm.23936" target="_blank">Schilling et al. (2018)</a> show that long-range cortical endpoints can be hidden or biased toward gyral crowns.</td>
<td>An <strong>endpoint-limited bundle hypothesis</strong>, not cortical edge completeness.</td>
</tr>
<tr>
<td><strong>Recovery depends on strong priors and still misses error classes</strong></td>
<td><a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">Donahue et al. (2016)</a>, <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">Schilling et al. (2020)</a>, and <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">Grisot et al. (2021)</a> show useful tracer correspondence and better recovery only with strong start / end / exclusion priors, while same-brain failures at branching and turning remain.</td>
<td>A <strong>prior-assisted bundle recovery</strong> or named error-term audit, not unbiased whole-brain discovery.</td>
</tr>
<tr>
<td><strong>Graph metrics are pipeline-conditioned</strong></td>
<td><a href="https://doi.org/10.1162/netn_a_00324" target="_blank">Gajwani et al. (2023)</a> and <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">He et al. (2024)</a> show that hub topology and laterality can shift across plausible processing choices.</td>
<td>A <strong>pipeline-conditioned graph metric</strong>, not anatomy by default.</td>
</tr>
<tr>
<td><strong>Acquisition / harmonization instability</strong></td>
<td><a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">McMaster et al. (2025)</a> and <a href="https://doi.org/10.3389/fnimg.2026.1670604" target="_blank">Bramati et al. (2026)</a> show that resolution and q-space protocol can systematically move connectome estimates even before endpoint and graph choices are interpreted.</td>
<td>A <strong>protocol-scoped connectome estimate</strong>; cross-protocol comparison needs explicit harmonization.</td>
</tr>
<tr>
<td><strong>Uncertainty and ex vivo calibration improve only part of the chain</strong></td>
<td><a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">Manzano-Patrón et al. (2025)</a> show that posterior uncertainty can be mapped rather than hidden, and <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">Zhu et al. (2025)</a> show that MRI plus microscopy can improve reconstruction in an ex vivo calibration setting.</td>
<td>A <strong>calibrated bundle comparison</strong>, not living-human connectome completion.</td>
</tr>
</tbody>
</table>
<table class="data-table">
<thead>
<tr>
<th>Route-card item</th>
<th>What must be disclosed</th>
<th>Why this site asks for it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Direct observables</strong></td>
<td>Write voxel size, shell / b-value scheme, direction count, orientation model, and state explicitly that the direct observable is diffusion signal / local fibre-orientation estimate rather than synapse identity, direction, or weight.</td>
<td>Otherwise a streamline graph is misread as if the edges themselves had been directly observed.</td>
</tr>
<tr>
<td><strong>Acquisition / harmonization audit</strong></td>
<td>Name whether the comparison spans different scanners, resolutions, or q-space schemes; disclose any resampling / harmonization route; and say whether the headline result survives protocol variation or remains protocol-scoped.</td>
<td>Otherwise a connectome change can be caused by acquisition design rather than anatomy.</td>
</tr>
<tr>
<td><strong>Cortical endpoint / surface-bias audit</strong></td>
<td>Name the white-matter / gray-matter boundary or surface-assignment route, whether superficial-white-matter or gyral-bias checks were performed, and which cortical territory remained endpoint-limited.</td>
<td>Otherwise cortical endpoint differences are misread as anatomical absence or edge specificity.</td>
</tr>
<tr>
<td><strong>Priors and post-processing</strong></td>
<td>Write seeding rule, deterministic / probabilistic mode, start / end / exclusion ROIs, atlas constraints, stopping rules, and filtering / weighting method.</td>
<td>Otherwise prior-driven bundle recovery is silently rephrased as unbiased graph discovery.</td>
</tr>
<tr>
<td><strong>Graph construction choices</strong></td>
<td>Name the parcellation / surface atlas, edge definition and weighting, density or threshold rule, and whether the headline metric survives reasonable alternative graph constructions.</td>
<td>Otherwise hub maps and graph metrics are read as anatomy when they may still be graph-construction artifacts.</td>
</tr>
<tr>
<td><strong>Instability and uncertainty</strong></td>
<td>Report scan-rescan or ensemble stability, posterior / bootstrap uncertainty, and sensitivity to voxel size, q-space scheme, or filtering for the headline graph metric.</td>
<td>Otherwise a connectome difference may only reflect pipeline choice rather than anatomy.</td>
</tr>
<tr>
<td><strong>External calibration route</strong></td>
<td>Name any tracer, same-brain histology, microscopy, or phantom route and say which error term it audits.</td>
<td>Otherwise "biologically plausible" is confused with validated.</td>
</tr>
<tr>
<td><strong>Ceiling and abstention</strong></td>
<td>Declare whether the claim stops at macro pathway prior, targeted bundle hypothesis, or calibrated bundle comparison, and write what would trigger abstention.</td>
<td>Otherwise tractography is rolled up to edge-complete or WBE-ready language.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Operational rule added in this pass</strong>
<p>
If a tractography-derived connectome claim lacks this route card, this site does not read it as a connectome-complete result. The default ceiling stays at <strong>macro pathway prior / targeted bundle hypothesis</strong>. The burden of proof is on the paper to show which part of the pipeline created the claim and which part has been externally calibrated.
</p>
</div>
</section>

<section class="section" id="degeneracy">
<h2 class="section-title">Easy to overlook problem 0: Even if the wiring is known, the dynamics are still degenerate</h2>
<p>
Previous versions of this page primarily explained "what state variables fall off the edge list." However, a theoretical study by Beiran and Litwin-Kumar in 2025 showed that even if a connectome is provided, recurrent dynamics often become highly degenerate if unmeasured cell and synaptic properties remain. Even if the student model and teacher model share the same synaptic weights, the dynamics of unobserved neurons can deviate significantly if the biophysical parameters are different. In other words, the missing variable is not ``auxiliary information that can be added later'', but is the main body that determines how uniquely it can be estimated.
</p>
<div class="note-box">
<strong>What this criticism means</strong>
<p>
Even if there is only a wiring diagram, the only solution for the internal state is still far away. Adding same-brain function or perturbation will reduce degeneracy, but unless the remaining family is made public, it cannot be said that ``this internal state is correct.'' Therefore, on this site, <strong>there is a graph</strong>, <strong>activity is partially correct</strong>, and <strong>the internal state is nearly unique</strong> are treated as different claims.
</p>
</div>
</section>

<section class="section" id="conditional-predictor-route-card">
<h2 class="section-title">Connectome-constrained predictors need a conditional-model route card</h2>
<p>
The remaining weak point after splitting connectome evidence classes was that the site still did not fully fix <strong>what must be disclosed before a connectome-constrained activity predictor can be read as more than a local conditional model</strong>. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">Lappalainen et al. (2024)</a> showed that a connectome-constrained and task-optimized fly visual-system model can make rich cell-type-level activity predictions while still relying on a partial motion-pathway connectome, periodic tiling, simplified single-compartment neurons, threshold-linear synapses, and an ensemble of <strong>50 local optima</strong>. <a href="https://doi.org/10.1038/s41586-024-07763-9" target="_blank">Shiu et al. (2024)</a> showed that a fly-brain model built from synapse-level connectivity and neurotransmitter identity can predict named feeding and grooming circuits, but the authors also describe that success as a <strong>coarse-level</strong> description of specific sensorimotor transformations. <a href="https://doi.org/10.1038/s41586-024-07982-0" target="_blank">Pospisil et al. (2024)</a> then used the connectome as a prior for a perturbation-based effectome and explicitly recovered a <strong>linear approximation</strong> to more realistic nonlinear dynamics rather than the full nonlinear state. Together with <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> and <a href="https://doi.org/10.1038/nn1352" target="_blank">Prinz et al. (2004)</a>, the operational lesson is now stronger: a successful connectome-constrained predictor is evidence of a useful <strong>conditional hypothesis engine</strong>, but not yet of unique internal-state recovery.
</p>
<table class="data-table">
<thead>
<tr>
<th>Conditional-model route-card field</th>
<th>What must be disclosed</th>
<th>Why this site asks for it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Structural prior actually used</strong></td>
<td>Name whether the model used EM edges, synapse counts, neurotransmitter-sign predictions, same-brain recordings, tractography priors, periodic tiling, or atlas-level averages, and state the exact spatial and cell-type coverage.</td>
<td>Otherwise a local or partially reconstructed scaffold is overread as if the whole relevant circuit had been directly observed.</td>
</tr>
<tr>
<td><strong>Fitted degrees of freedom</strong></td>
<td>List which quantities were still learned or tuned, such as neuron time constants, resting potentials, unitary synapse scales, decoder weights, gain functions, or Jacobian entries around the operating point.</td>
<td>Otherwise “connectome-constrained” is misread as if the fitted dynamics were directly measured rather than inferred from many remaining free parameters.</td>
</tr>
<tr>
<td><strong>Task / state regime and training distribution</strong></td>
<td>Name the stimulus family, behaviour, operating state, species, local circuit window, held-out/OOD splits, and whether validation stayed inside the same task family.</td>
<td>Otherwise success on one visual, sensorimotor, or state-limited regime is silently promoted to arbitrary-task or whole-brain competence.</td>
</tr>
<tr>
<td><strong>Omitted mechanisms and adaptation boundary</strong></td>
<td>State whether electrical synapses, nonlinear chemical synapses, neuromodulation, glia, plasticity, body/environment loops, or long-timescale maintenance controllers were omitted, frozen, or externally calibrated.</td>
<td>Otherwise the reader cannot tell whether good prediction came from the connectome route itself or from a boundary where important mechanisms were removed from the question.</td>
</tr>
<tr>
<td><strong>Validation and perturbation class</strong></td>
<td>Name whether the model was checked against held-out activity, same-brain physiology, optogenetic perturbation, behavioural intervention, or only task loss, and say whether the claim is local-linear / Jacobian-like or long-horizon nonlinear.</td>
<td>Otherwise “validated” blurs together offline task fit, local causal support, and true recovery of intervention response.</td>
</tr>
<tr>
<td><strong>Equivalence classes, uncertainty, and abstention</strong></td>
<td>Expose ensemble spread, alternative families, local optima, parameter non-uniqueness, and the point where the claim stops at hypothesis engine / conditional predictor / local effectome.</td>
<td>Otherwise a single successful fit is overread as if competing internal explanations had disappeared.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Operational rule added in this pass</strong>
<p>
If a connectome-constrained predictor lacks this route card, this site keeps the result at <strong>conditional model / hypothesis engine</strong>, <strong>task-bounded local predictor</strong>, or at most <strong>locally validated perturbation model</strong>. It is not promoted to state-complete recovery, unique internal-state identification, or a whole-brain mechanistic solution.
</p>
</div>
</section>

<section class="section" id="state-classes">
<h2 class="section-title">Why these classes are easy to skip</h2>

<h3>1. Cell type labels are not decorations for node IDs</h3>
<p>
Gamlin et al. (2025) did not obtain transcriptomic labels directly from the connectome itself; they used Patch-seq morphology to predict transcriptomic Sst types inside a large EM volume and then showed that those predicted Sst subtypes differed in axon myelination and synaptic output patterns. Furthermore, the MICrONS Consortium emphasized that in mammalian cortex, cells of different cell types can still contain neurons with different tuning preferences, so same-brain connectivity and same-brain function must be read together. In other words, even if the graph structure is the same, the physical meaning of the circuit changes if the node label and same-brain physiology are different. An unlabeled graph with a reduced cell type may be convenient for compression, but it loses a large fraction of the information required to reproduce function.
</p>

<h3>2. Activity-dependent transcription / chromatin state is not reducible to node label</h3>
<p>
The weak point that became clearer in this pass was that the site was already separating <strong>cell identity</strong> from <strong>intrinsic excitability</strong>, while still leaving <strong>the current transcriptional / chromatin program for allocation and stabilization</strong> too close to the cell-type bucket. That is too weak. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">Santoni et al. (2024)</a> showed that chromatin plasticity predetermines neuronal eligibility for memory-trace formation, <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">Traunmüller et al. (2025)</a> showed region-specific and time-defined chromatin / gene-expression changes after novel-environment exposure, <a href="https://doi.org/10.1038/s41586-025-09774-6" target="_blank">Terceros et al. (2026)</a> showed thalamocortical transcriptional gates that coordinate memory stabilization across distinct post-learning windows, and <a href="https://doi.org/10.1038/s41588-025-02368-y" target="_blank">Coda et al. (2025)</a> showed cell-type- and locus-specific epigenetic editing of memory expression. In other words, even if the graph and cell-type label are fixed, <strong>which neurons are allocation-ready and which late programs stabilize memory</strong> can still remain as latent state.
</p>
<div class="note-box">
<strong>Reading rule for transcriptomic evidence</strong>
<p>
On this site, a static atlas, one-shot memory-related DEG list, or one epigenetic assay is treated as an <strong>identity prior, object-specific clue, or time-stamped clue</strong>, not as a ground truth of the current plasticity-competent state. Unless temporal calibration, locus specificity, molecular-object disclosure, or causal perturbation is shown, transcriptomic evidence stays below current-state completion. The detailed operating rule is now collected in <a href="homeostatic-plasticity-and-maintenance-state.html#transcription-route-card">Wiki: transcription / chromatin route card</a>.
</p>
</div>

<h3>3. Post-transcriptional RNA-state is not recoverable from gene-level abundance alone</h3>
<p>
The remaining weakness after separating <strong>cell identity</strong> from <strong>current transcription / chromatin state</strong> was that the site still left <strong>post-transcriptional RNA-state</strong> too close to DEG lists or transcript counts. That was too weak. <a href="https://doi.org/10.1038/nn.4069" target="_blank">Wang et al. (2015)</a> showed that a neuron-specific LSD1 splice isoform regulates memory formation, <a href="https://doi.org/10.1016/j.neuron.2019.03.032" target="_blank">Dai et al. (2019)</a> showed that presynaptic neurexin alternative splicing changes postsynaptic receptor balance and contextual memory, <a href="https://doi.org/10.1038/s41586-018-0666-1" target="_blank">Shi et al. (2018)</a> and <a href="https://doi.org/10.1002/advs.202514926" target="_blank">Li et al. (2025)</a> showed that m6A-reader routes can alter hippocampus-dependent learning and memory, and <a href="https://doi.org/10.1126/scisignal.adr1442" target="_blank">Peterson et al. (2025)</a> showed that ADAR2-mediated GluA2 RNA editing contributes to homeostatic synaptic plasticity. In other words, even if the graph, cell-type label, and gene-level abundance are held fixed, <strong>the operative RNA controller that helps set receptor composition, plasticity route, and stabilization can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for post-transcriptional RNA-state</strong>
<p>
Current human in vivo routes on this site do not directly reveal whole-brain <strong>isoform choice</strong>, <strong>m6A-reader engagement</strong>, or <strong>RNA-editing ratio</strong>. Specialized long-read atlas work such as <a href="https://doi.org/10.1038/s41593-024-01616-4" target="_blank">Joglekar et al. (2024)</a> is important evidence that splicing programs are rich and cell-type-specific in mouse and human brain, but it is still an atlas-building / ex vivo route rather than a comparable in vivo whole-brain human measurement. On this site, post-transcriptional RNA-state therefore remains latent unless it is externally calibrated or causally perturbed in a narrower preparation. The maintenance-side treatment is developed further in <a href="homeostatic-plasticity-and-maintenance-state.html#post-transcriptional-rna-state">Wiki: post-transcriptional RNA-state</a>.
</p>
</div>
<h3 id="phospho-signaling-state">4. Phospho-signaling / second-messenger state is not recoverable from transcript or protein abundance alone</h3>
<p>
The remaining weakness after separating <strong>post-transcriptional RNA-state</strong> from <strong>gene-level abundance</strong> was that the site still left <strong>phospho-signaling / second-messenger state</strong> too close to transcriptomics, proteomics, or nominal weights. That was too weak. <a href="https://doi.org/10.1126/science.279.5352.870" target="_blank">Giese et al. (1998)</a> showed that CaMKII Thr286 autophosphorylation is required for LTP and spatial learning, <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">Lee et al. (2003)</a> showed that distinct AMPA-receptor phosphorylation sites regulate bidirectional synaptic plasticity, <a href="https://doi.org/10.1523/JNEUROSCI.5303-03.2004" target="_blank">Rodrigues et al. (2004)</a> showed learning-linked CaMKII phospho-state changes at lateral amygdala synapses, <a href="https://doi.org/10.1016/j.neuron.2005.01.009" target="_blank">Tomita et al. (2005)</a> showed phosphorylation-dependent control of TARP-mediated AMPAR plasticity, and <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">Vierra et al. (2023)</a> showed that ER-plasma membrane junctions create Ca<sup>2+</sup>-activated PKA signaling nanodomains in neurons. In other words, even if graph, cell-type label, transcript counts, and bulk protein abundance are held fixed, <strong>the active phospho-controller and second-messenger routing can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for phospho-signaling state</strong>
<p>
Current human in vivo routes on this site do not directly reveal whole-brain <strong>phosphosite occupancy</strong>, <strong>kinase/phosphatase balance</strong>, or <strong>compartment-specific signaling nanodomains</strong>. Ex vivo atlas work such as <a href="https://doi.org/10.1021/acs.jproteome.2c00244" target="_blank">Biswas et al. (2023)</a> is important evidence that the human brain phosphoproteome is region-structured, but it is still an atlas-building / ex vivo route rather than a comparable in vivo whole-brain human measurement. On this site, phospho-signaling / second-messenger state therefore remains latent unless it is externally calibrated or causally perturbed in a narrower preparation. The maintenance-side treatment is developed further in <a href="homeostatic-plasticity-and-maintenance-state.html#phospho-signaling-state">Wiki: phospho-signaling / second-messenger state</a>.
</p>
</div>

<h3>5. Intrinsic excitability and homeostasis set point is not a byproduct of node label</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> showed that the morpho-electric phenotype spreads continuously even within the same transcriptomic type. Furthermore, <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> showed that even among identified neurons, there are large individual differences in ion channel mRNA and current amount, and <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> modeled how activity-dependent channel expressions can yield activity set points. Furthermore, <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> have shown that a firing-rate set point exists for each single neuron in vivo. In other words,<strong>even if the cell-type label and graph are known, the return destination after threshold, gain, rebound, and perturbation can still remain as latent state</strong>.
</p>

<h3>6. Synapses are not binary edges</h3>
<p>
Holler et al. analyzed the ultrastructure and release properties of neocortical synapses, and showed that transmission properties cannot be expressed simply by "connected/not connected." Matsuzaki et al. demonstrated that spine enlargement and AMPA current increases are linked in LTP induction in a single dendritic spine. Furthermore, Vardalaki et al. showed that even in the adult neocortex, approximately 25% of filopodia can serve as the structural basis for silent synapse lacking AMPA receptors. Therefore, <strong>edge list alone will reduce the weight of the current state, plastic history, and whether it is functionally active in the first place</strong>.
</p>
<div class="note-box">
<strong>Current weight is not the same as the late-stabilization route</strong>
<p>
<a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a> proposed synaptic tagging as the condition that allows late LTP to capture plasticity-related proteins, <a href="https://doi.org/10.1038/ncomms2250" target="_blank">Shires et al. (2012)</a> demonstrated synaptic tagging and capture in the living rat, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a> showed branch-level integration of protein-synthesis-dependent LTP, and <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">Fonseca et al. (2006)</a> showed that late-LTP maintenance depends on a balance between protein synthesis and proteasome-dependent degradation. More recently, <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a> linked local autophagy-coupled translation to long-term memory formation and <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">Thomas et al. (2025)</a> showed that actin/spine geometry can persist on the timescale of the synaptic tag. Therefore, even if the connectome and a weight estimate are given, the branch-local capture and stabilization route can still remain latent.
</p>
</div>
<div class="note-box">
<strong>Cargo delivery is not implied by weight, proteostasis, or ATP</strong>
<p>
<a href="https://doi.org/10.1016/j.neuron.2006.09.040" target="_blank">Park et al. (2006)</a> showed that recycling-endosome exocytosis is required for LTP-associated spine growth, <a href="https://doi.org/10.1073/pnas.0902304106" target="_blank">Maas et al. (2009)</a> showed that synaptic activation rewrites microtubules that support postsynaptic cargo transport, <a href="https://doi.org/10.1016/j.neuron.2011.03.026" target="_blank">Yin et al. (2011)</a> showed that KIF17 supports synaptic NR2A/2B balance and memory, <a href="https://doi.org/10.7554/eLife.53456" target="_blank">Zhao et al. (2020)</a> showed that KIF5B depletion impairs dendritic transport, plasticity, and memory, <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">Swarnkar et al. (2021)</a> linked KIF5C-mediated transport to structural plasticity and long-term memory, and <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">Aiken &amp; Holzbaur (2024)</a> showed that axonal microtubule patterning controls presynaptic cargo delivery. Therefore, even if a site measures weight, tag state, or ATP support, <strong>which cargo reaches which compartment</strong> can still remain latent.
</p>
</div>

<h3>7. Perisynaptic ECM / PNN state is not just packaging around synapses</h3>
<p>
The current site used to separate synapses, timing, neuromodulation, and glia, while still leaving <strong>the extracellular matrix around synapses and inhibitory cells</strong> too implicit. That was too weak. <a href="https://doi.org/10.1126/science.1072699" target="_blank">Pizzorusso et al. (2002)</a> showed that digesting chondroitin-sulfate proteoglycans can reopen ocular-dominance plasticity in adult visual cortex. <a href="https://doi.org/10.1038/nn.2338" target="_blank">Frischknecht et al. (2009)</a> showed that brain extracellular matrix constrains AMPA-receptor lateral mobility and short-term synaptic plasticity. <a href="https://doi.org/10.1126/science.1174146" target="_blank">Gogolla et al. (2009)</a> showed that perineuronal nets protect fear memories from erasure, and <a href="https://doi.org/10.1016/j.matbio.2024.11.001" target="_blank">Jabłońska et al. (2024)</a> showed that extracellular-matrix integrity regulates hippocampal GABAergic plasticity. In other words, the missing variable is not only "how strong the synapse is now," but also <strong>which plasticity transitions and stabilization regimes are still available on that same graph</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for ECM / PNN state</strong>
<p>
Human evidence is moving, but it is still not an in vivo whole-brain ground truth of current ECM state. <a href="https://doi.org/10.3390/ijms23158197" target="_blank">Boonen et al. (2022)</a> showed extracellular-matrix reorganization in human hippocampal sclerosis tissue, which is useful evidence that the matrix layer is biologically real in human disease tissue. But this remains <strong>ex vivo pathology</strong>, not a direct readout of moment-to-moment perisynaptic matrix state in a living human brain. On this site, ECM / PNN is therefore treated as a latent state unless it is externally calibrated or locally perturbed.
</p>
</div>

<h3>8. Ionic milieu / chloride homeostasis is not background chemistry</h3>
<p>
The current site had become good at separating <strong>intrinsic excitability</strong>, <strong>ECM / PNN</strong>, <strong>timing-state</strong>, and <strong>glia</strong>, while still leaving <strong>chloride set point and interstitial ion composition</strong> too implicit. That was too weak. <a href="https://doi.org/10.1126/science.1245423" target="_blank">Glykys et al. (2014)</a> showed that local impermeant anions help establish neuronal chloride concentration, <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">Heubl et al. (2017)</a> showed that GABA<sub>A</sub>-receptor-mediated synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase, <a href="https://doi.org/10.1126/science.aad4821" target="_blank">Ding et al. (2016)</a> showed that changing interstitial K<sup>+</sup>, Ca<sup>2+</sup>, Mg<sup>2+</sup>, and H<sup>+</sup> is sufficient to shift cortical activity and sleep/wake state, and <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">Huberfeld et al. (2007)</a> showed perturbed chloride homeostasis with depolarizing GABAergic signaling in human temporal-lobe epilepsy. More recently, <a href="https://doi.org/10.1038/s41386-022-01480-5" target="_blank">Simonnet et al. (2023)</a> linked KCC2 silencing to impaired hippocampal memory and altered rhythmogenesis, and <a href="https://doi.org/10.1007/s12576-018-00654-5" target="_blank">Nakamura et al. (2019)</a> showed that KCC2 overexpression enhances dendritic-spine plasticity and motor learning. In other words, the missing variable is not only <strong>how excitable a neuron is in general</strong>, but also <strong>what sign and gain inhibition has on that local circuit right now</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for ionic state</strong>
<p>
Human ionic evidence is still a coarse observability class. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> demonstrated high-resolution sodium imaging of healthy human brain at 7 T, which is useful evidence that some ionic layer is becoming visible in vivo. But this remains a mm-class tissue sodium map, not a direct readout of <strong>cell-specific chloride concentration</strong>, <strong>KCC2 / NKCC1 balance</strong>, <strong>extracellular K<sup>+</sup> or Ca<sup>2+</sup> microdomains</strong>, or <strong>local E<sub>GABA</sub></strong>. On this site, human sodium imaging is therefore treated as a <strong>macro ionic proxy</strong>, not as ground truth of current chloride homeostasis.
</p>
</div>

<h3>9. Shared extracellular / electrical state is not reducible to chemical wiring</h3>
<p>
The remaining weakness was that the site had become much better at separating <strong>ionic / chloride state</strong>, <strong>timing-state</strong>, and <strong>glia</strong>, while still leaving <strong>gap-junction coupling, endogenous field effects, and local inhibitory driving force</strong> too close to the chemical-synapse bucket. That was too weak. <a href="https://doi.org/10.1038/47029" target="_blank">Galarreta &amp; Hestrin (1999)</a> showed that fast-spiking interneurons in neocortex form electrical-synapse networks, <a href="https://doi.org/10.1038/nn.2727" target="_blank">Anastassiou et al. (2011)</a> showed that endogenous extracellular fields can causally entrain cortical spike timing under physiological conditions, <a href="https://doi.org/10.1016/j.neuron.2023.08.005" target="_blank">Burman et al. (2023)</a> showed that active cortical networks can shift fast inhibition toward a predominantly shunting regime in vivo, <a href="https://doi.org/10.1073/pnas.2313042121" target="_blank">Yang et al. (2024)</a> showed that dynamic electrical synapses can rewire brain networks for persistent oscillations, and <a href="https://doi.org/10.1038/s41467-024-53074-y" target="_blank">Selfe et al. (2024)</a> showed with ORCHID that inhibitory driving force can now be measured directly, but only with specialized local optical methods. In other words, the missing variable is not only <strong>how strong chemical inhibition is</strong>, but also <strong>how electrical coupling, extracellular-field geometry, and inhibitory driving-force regime coordinate spikes and oscillations on that same chemical graph</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for electrical-state</strong>
<p>
Human evidence for this layer is still indirect. <a href="https://doi.org/10.1111/ejn.70401" target="_blank">Feld et al. (2026)</a> reported that mefloquine before sleep impaired declarative-memory retention and disrupted spindle-to-slow-oscillation coupling in healthy participants, which is useful perturbation evidence that electrical coupling can matter for systems-memory coordination. But the same paper also leaves off-target effects as a caveat, and it is not a direct readout of <strong>which cells were electrically coupled</strong> or <strong>what the local inhibitory driving force was</strong>. On this site, human evidence for shared electrical state is therefore read first as a <strong>perturbation-conditioned clue</strong>, not as ground truth of local electrical coupling in vivo.
</p>
<p>
Human evidence for extracellular geometry is also ceiling-limited and internally split. <a href="https://doi.org/10.1126/science.1241224" target="_blank">Xie et al. (2013)</a> showed sleep-linked interstitial-space expansion in mice, <a href="https://doi.org/10.1016/j.neuroimage.2020.116682" target="_blank">Voldsbekk et al. (2020)</a> provided a bounded human diffusion-MRI clue consistent with wakefulness-related extra-axonal / extracellular-volume reduction, and <a href="https://doi.org/10.1016/j.neuroimage.2023.120124" target="_blank">Örzsik et al. (2023)</a> used a within-subject wake-versus-sleep design plus higher-order diffusion modeling to derive a sleep-conditioned clue compatible with increased interstitial-fluid volume and glymphatic-like clearance. Those are useful clues, but they are still not direct local readouts of synapse-adjacent extracellular geometry in living humans, and they do not become one route merely because both use human diffusion MRI.
</p>
</div>
<h4 id="electrical-state-route-card">Electrical-state evidence now needs a route card</h4>
<p>
The critique here is not merely that <strong>electrical state exists</strong>, but that recent primary literature spans <strong>different inferential objects</strong>. Gap-junction topology, endogenous-field coupling, inhibitory-driving-force state, and activity-dependent electrical-synapse remodeling do not all answer the same question. A human wakefulness-related diffusion clue, a human sleep-conditioned higher-order diffusion clue, and a human sleep perturbation clue are different again. If a paper moves among those objects without naming the route, the reader can silently overread a local mechanistic result as if it had already fixed the broader electrical regime.
</p>
<p>
On this site, that warning now also applies to <strong>extracellular-space geometry / diffusion-barrier / osmotic-regime routes</strong>. A paper about synapse-adjacent dilution, osmotic ECS contraction, sleep-linked interstitial-space change, or a human diffusion-MRI extra-axonal proxy is not automatically a paper about the same inferential object as gap-junction topology or inhibitory driving force.
</p>
<table class="data-table">
<thead>
<tr>
<th>Route-card item</th>
<th>What must be disclosed</th>
<th>Why this site asks for it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claim family</strong></td>
<td>State whether the paper is about a <strong>gap-junction coupling network</strong>, an <strong>endogenous-field / ephaptic route</strong>, an <strong>extracellular-space geometry / diffusion-barrier route</strong>, an <strong>inhibitory-driving-force regime</strong>, an <strong>activity-dependent electrical-synapse remodeling route</strong>, a <strong>human wakefulness-related ECS proxy clue</strong>, a <strong>human sleep-conditioned diffusion / glymphatic clue</strong>, or only a <strong>human perturbation-conditioned clue</strong>.</td>
<td>Otherwise the paper's object changes silently while the headline claim stays broad.</td>
</tr>
<tr>
<td><strong>Direct extracellular / electrical observable</strong></td>
<td>Name the direct observable explicitly, such as paired-cell electrical coupling, extracellular field effect on spike timing, local extracellular volume fraction / diffusion constraint, local inhibitory driving force, oscillation-coupling statistic, or only a downstream behavioral / sleep-coupling or diffusion-MRI proxy.</td>
<td>Otherwise a downstream phenotype is misread as if the electrical state itself had been observed.</td>
</tr>
<tr>
<td><strong>Spatial regime</strong></td>
<td>State whether the route is a paired-cell microcircuit, a synapse-adjacent extracellular pocket, a local cortical population, a network oscillation preparation, a sleep/wake population regime, or a macro human perturbation / diffusion-MRI regime.</td>
<td>Otherwise a narrow local mechanism is overread as if it already fixed a broader electrical regime.</td>
</tr>
<tr>
<td><strong>Perturbation / calibration route</strong></td>
<td>Name the perturbation or calibration route, such as connexin-linked coupling measurement, extracellular-field manipulation, extracellular diffusion or tetramethylammonium-style assay, osmotic challenge, ORCHID-style optical assay, pharmacological perturbation, diffusion-MRI compartment modeling, or no direct calibration at all.</td>
<td>Otherwise causal leverage and calibration burden disappear behind the word <strong>electrical</strong>.</td>
</tr>
<tr>
<td><strong>Human evidence class</strong></td>
<td>Write whether the strongest human-facing evidence is a <strong>direct local assay</strong>, a <strong>specialized optical / invasive route</strong>, a <strong>wakefulness-related diffusion-MRI ECS proxy clue</strong>, a <strong>sleep-conditioned higher-order diffusion / glymphatic clue</strong>, a <strong>perturbation-conditioned clue</strong>, or <strong>no human route</strong>.</td>
<td>Otherwise a human perturbation result is silently promoted toward local state identification.</td>
</tr>
<tr>
<td><strong>Ceiling and abstention</strong></td>
<td>Declare whether the claim stops at <strong>local electrical mechanism</strong>, <strong>local extracellular-geometry mechanism</strong>, <strong>narrow network-regime evidence</strong>, <strong>human wakefulness-related diffusion-MRI proxy clue</strong>, <strong>human sleep-conditioned diffusion / glymphatic clue</strong>, or <strong>human perturbation clue</strong>, and write what would trigger abstention.</td>
<td>Otherwise the phrase <strong>electrical-state complete</strong> is allowed to outrun the actual evidence class.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Operational rule added in this pass</strong>
<p>
If a shared extracellular / electrical-state claim lacks this route card, this site keeps the result at <strong>local mechanism</strong>, <strong>specialized assay</strong>, <strong>human wakefulness-related diffusion-MRI proxy clue</strong>, <strong>human sleep-conditioned diffusion / glymphatic clue</strong>, or <strong>human perturbation clue</strong>. It is not promoted to chemical-connectome-complete state capture, whole-brain extracellular / electrical-regime recovery, or maintenance-complete synchrony control.
</p>
</div>

<h3>10. Timing-state is not one scalar delay term</h3>
<p>
<a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a> showed that neuronal activity promotes oligodendrogenesis and adaptive myelination, and <a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. (2014)</a> showed that active central myelination is required for motor-skill learning. But the weakness of the earlier page was that it still allowed the reader to compress this into the slogan "more myelin, faster signal." Primary literature now supports a stronger statement: <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a> showed that node and internode geometry is tuned along auditory axons to adjust action-potential timing, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a> showed that perinodal astrocytes can reversibly alter nodal gap length and myelin structure to change conduction velocity and spike arrival, and <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a> showed that saltatory conduction depends on a conductive periaxonal nanocircuit rather than on a single scalar delay term.
</p>
<p>
This matters for WBE because timing-sensitive circuits do not only depend on "who connects to whom," but also on <strong>when inhibition, synchrony, and phase-locked drive arrive</strong>. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">Micheva et al. (2021)</a> showed that even locally projecting PV interneurons gain physiologically relevant conduction-speed differences with axonal myelination, <a href="https://doi.org/10.7554/eLife.73827" target="_blank">Dubey et al. (2022)</a> linked loss of PV-axon myelination to weakened fast inhibition and failure of gamma synchronization, <a href="https://doi.org/10.1038/s41586-024-07853-8" target="_blank">Xin et al. (2024)</a> showed that adolescent oligodendrogenesis can act as a brake on adult visual-cortex plasticity, and <a href="https://doi.org/10.1038/s41467-025-56092-6" target="_blank">Della-Flora Nunes et al. (2025)</a> showed that neuronal recovery after demyelination can return before healthy myelin levels are completely restored. Therefore, if timing matters, the missing variable is better described as <strong>timing-state</strong> rather than simply "delay," and the site has to keep <strong>learning</strong>, <strong>microgeometry</strong>, <strong>plasticity brake</strong>, <strong>recovery boundary</strong>, and <strong>human proxy class</strong> on separate rows.
</p>
<div class="note-box">
<strong>Do not compress timing-state into one evidence row</strong>
<p>
On this site, timing-state evidence is no longer read as one interchangeable ladder. <strong>Activity-dependent oligodendrogenesis / learning</strong>, <strong>node-internode-periaxonal timing control</strong>, <strong>plasticity-brake function</strong>, <strong>remyelination-to-function recovery</strong>, and <strong>human tract-speed or quantity-defined myelin proxy routes</strong> answer different questions and stop at different ceilings. Therefore, a positive human myelin paper does not inherit the causal force of the animal timing-microgeometry papers, and a functional rescue result does not inherit proof that healthy myelin-state was fully restored.
</p>
</div>
<div class="note-box">
<strong>Human observability ceiling for timing-state</strong>
<p>
Human timing-side evidence is also not one route. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">van Blooijs et al. (2023)</a> showed that transmission speed in the human brain follows a developmental trajectory, which is useful evidence that conduction timing is biologically variable at the tract scale. But tract-speed estimation is still not the same inferential object as quantity-defined myelin MRI. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/" target="_blank">Arshad et al. (2017)</a> showed that reliability does not guarantee myelin validity for calibrated T<sub>1</sub>w/T<sub>2</sub>w relative to <strong>MWF</strong>, <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6043493/" target="_blank">Hagiwara et al. (2018)</a> showed stronger agreement between <strong>SyMRI</strong> and <strong>MT<sub>sat</sub></strong> than with T<sub>1</sub>w/T<sub>2</sub>w, <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> demonstrated bilayer-sensitive mapping only in <strong>two healthy volunteers</strong>, <a href="https://doi.org/10.1016/j.neuroimage.2025.121456" target="_blank">Chen et al. (2025)</a> showed that conventional quantitative MT keeps an orientation-dependent route variable, <a href="https://doi.org/10.1111/bpa.70010" target="_blank">Galbusera et al. (2025)</a> showed that <strong>qT1</strong>, but not <strong>MWF</strong> or <strong>MTR</strong>, separated cortical remyelination states in a histology-linked design, and <a href="https://doi.org/10.1038/s41467-025-58604-w" target="_blank">Genc et al. (2025)</a> still required ex vivo gene-expression alignment and histopathological confirmation when linking developmental cortical microstructure to oligodendrocyte biology. On this site, human tract-speed or myelin readouts are therefore treated as <strong>typed macro timing proxies</strong>, not as ground truth of per-axon conduction state, node length, periaxonal spacing, or local inhibitory arrival time.
</p>
</div>
<div class="note-box" id="timing-state-route-card">
<strong>2026-03-31 addendum: timing-state evidence also needs a route card on this page</strong>
<p>
The remaining weakness on this central page was that <strong>timing-state evidence</strong> could still compress <strong>activity-dependent oligodendrogenesis / learning</strong>, <strong>node / internode / periaxonal timing control</strong>, <strong>plasticity-brake function</strong>, <strong>remyelination-to-function recovery</strong>, and <strong>human tract-speed or myelin-proxy routes</strong> into one bucket. The primary literature does not support that shortcut. Therefore, this page now also requires a <strong>timing-state / myelin route card</strong> before a connectome argument is promoted beyond a narrow, explicitly named ceiling.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Route-card field</th>
<th>What must be fixed explicitly</th>
<th>What goes wrong if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Claim family</strong></td>
<td>State whether the paper is about <strong>activity-dependent oligodendrogenesis / learning</strong>, <strong>node-internode-periaxonal timing control</strong>, <strong>plasticity-brake function</strong>, <strong>remyelination-to-function recovery</strong>, or a <strong>human macro timing / myelin proxy</strong>.</td>
<td>Learning, microgeometry, recovery, and human proxy papers collapse into one phrase such as <code>myelin evidence supports timing</code>.</td>
</tr>
<tr>
<td><strong>Direct structural unit / observable</strong></td>
<td>Name the actual object: new oligodendrocyte generation, myelin sheath or bilayer contrast, nodal gap length, internode geometry, periaxonal space, PV-axon myelination, tract-scale transmission speed, or another explicitly measured unit.</td>
<td><code>Timing changed</code> replaces the actual scale of evidence, and macro proxy rows are overread as if they already measured the timing controller itself.</td>
</tr>
<tr>
<td><strong>Functional target</strong></td>
<td>Write whether the claim is about skill learning, deprived-eye or visual-cortex plasticity, phase / synchrony precision, spike-arrival timing, gamma support, VEP latency, or another named target.</td>
<td>The site silently shifts from one dependent variable to another, for example from a learning result to timing-complete reconstruction.</td>
</tr>
<tr>
<td><strong>Recovery / completeness boundary</strong></td>
<td>State whether the paper shows prevention, compensation, partial remyelination with functional rescue, or complete restoration of healthy myelin-state.</td>
<td>Any recovery result is overread as proof that the healthy timing-state or myelin-state was fully reconstructed.</td>
</tr>
<tr>
<td><strong>Human quantity type / proxy class</strong></td>
<td>For human evidence, disclose whether the route is tract-speed estimation, <strong>MWF</strong>, <strong>MT / MT<sub>sat</sub> / qMT / MPF-family contrast</strong>, <strong>bilayer-sensitive ultrashort-T<sub>2</sub> mapping</strong>, <strong>qT1 remyelination-sensitive readout</strong>, developmental diffusion-microstructure modelling with ex vivo alignment, or another named proxy class, together with hardware burden and model assumptions.</td>
<td>A human myelin paper is treated as if it had directly measured one interchangeable timing object, per-axon delay, or oligodendrocyte support state.</td>
</tr>
<tr>
<td><strong>Abstention boundary</strong></td>
<td>Fix in one line what remains latent, especially per-axon conduction delay, node / internode / periaxonal microgeometry in humans, oligodendrocyte-axon metabolic support, local plasticity gating, and same-subject whole-brain timing-controller identification.</td>
<td>Macro proxy or partial-recovery evidence is promoted to timing-complete, plasticity-complete, or maintenance-complete language.</td>
</tr>
</tbody>
</table>

<h3>11. Thermal-state is not reducible to timing or recording nuisance</h3>
<p>
The remaining weakness after separating <strong>timing-state</strong> from a single delay constant was that the page still let readers compress <strong>thermal-state</strong> into either "part of timing" or "just a recording nuisance." That was too weak. <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">Hardingham &amp; Larkman (1998)</a> showed that excitatory synaptic reliability in rat visual cortex is temperature dependent, <a href="https://doi.org/10.1371/journal.pone.0232451" target="_blank">Van Hook (2020)</a> showed that warming shifts release probability, synaptic depression, membrane conductance, and spike output in the visual thalamus, and <a href="https://doi.org/10.1126/science.8446900" target="_blank">Moser et al. (1993)</a> showed that dentate field potentials track brain temperature closely enough to mask learning-related change. Furthermore, <a href="https://doi.org/10.1038/nature07448" target="_blank">Long &amp; Fee (2008)</a> and <a href="https://doi.org/10.1152/jn.00890.2009" target="_blank">Reig et al. (2010)</a> showed that local cooling / warming can act as a perturbation of sequence timing and cortical rhythms, whereas <a href="https://doi.org/10.1038/s41593-019-0422-3" target="_blank">Owen et al. (2019)</a> showed that optogenetic manipulations can themselves inject tissue heating artifacts. In other words, even if graph, weights, timing-state, and ATP support are held fixed, <strong>the local thermal operating point and heating burden can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for thermal-state</strong>
<p>
Human thermal evidence is still a macro proxy class. <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a> showed a daily temperature rhythm across the human brain, and <a href="https://doi.org/10.1007/s00062-024-01467-3" target="_blank">Tan et al. (2025)</a> used <sup>1</sup>H-MRS thermometry to measure frontal-lobe temperature in healthy adults. Those routes are useful evidence that human brain temperature is measurable and variable, but they do not become ground truth of cell-specific microtemperature, local heating burden, or branch-specific thermal sensitivity. On this site, human thermal routes therefore remain <strong>macro thermal proxy</strong> rather than local thermal-state readout.
</p>
</div>

<h3>12. Neuromodulatory occupancy / release state is not “one mood scalar”</h3>
<p>
Reimer et al. showed that pupil fluctuations track both adrenergic and cholinergic activity within the cortex. Conversely, this also means that<strong>pupil diameter does not uniquely represent one transmitter state or the other</strong>. Additionally, Neyhart et al. showed that while cortical ACh is highly predictable from cholinergic axon activity and behavioral state, it also has locality that depends on distance from neighboring axons and clearance kinetics. Therefore, although it is useful to use pupil diameter or HRV in humans, it is an overstatement to consider it as the ground truth of transmitter-specific and region-specific internal states. What is necessary is not only to say whether it is a good proxy or not, but also to specify what it is and what it is not.
</p>

<h3>13. Bioenergetic / mitochondrial state is not implied by graph or macro energetic imaging</h3>
<p>
The current site already treated energy as important, but it still left too much room to compress <strong>presynaptic ATP-demand support</strong>, <strong>dendritic mitochondrial positioning / fission</strong>, <strong>synaptic ATP-synthase nano-organization</strong>, and <strong>human macro energetic imaging</strong> into one energetic row. Primary literature is narrower. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">Rangaraju et al. (2014)</a> showed that activity-driven local ATP synthesis is required for synaptic function, <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">Divakaruni et al. (2018)</a> showed that LTP induction requires a rapid burst of dendritic mitochondrial fission, <a href="https://doi.org/10.1038/s41598-023-40877-0" target="_blank">Underwood et al. (2023)</a> showed that enhanced presynaptic mitochondrial energy production is required for memory formation, and <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">Hu et al. (2025)</a> showed learning-linked polarized ATP-synthase organization in synaptic mitochondria. More recently, <a href="https://doi.org/10.1038/s42255-026-01451-w" target="_blank">Vishwanath et al. (2026)</a> showed that mitochondrial Ca<sup>2+</sup> efflux tuning can control neuronal metabolism and long-term memory across species. Therefore, even if graph and nominal activity fit are known, <strong>the local energetic controller and mitochondrial operating regime can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for bioenergetic / mitochondrial state</strong>
<p>
Human energetic observability is still a set of macro proxy classes rather than one meter. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> constrained <strong><sup>31</sup>P metabolite / pH balance</strong>, <a href="https://doi.org/10.1002/mrm.26560" target="_blank">Ren et al. (2017)</a> constrained <strong>model-conditioned <sup>31</sup>P MT exchange flux</strong>, <a href="https://doi.org/10.3389/fnins.2024.1389111" target="_blank">Guo et al. (2024)</a> mapped <strong>whole-brain <sup>31</sup>P NAD content</strong>, <a href="https://doi.org/10.1177/0271678X261415784" target="_blank">Kaiser et al. (2026)</a> measured <strong>localized functional <sup>31</sup>P NAD dynamics</strong>, <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a> constrained <strong>deuterium metabolite-mapping / absolute quantification</strong>, and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> constrained <strong>deuterium kinetic-rate terms</strong> under blood-input and explicit kinetic modeling. Those routes are useful evidence that human energetic burden is measurable, but they do not become ground truth of branch-specific ATP reserve, mitochondrial residence time, or local Ca<sup>2+</sup>-efflux control. On this site, human energetic routes therefore remain <strong>macro energetic proxies of different quantity types</strong>, not one solved energetic readout.
</p>
</div>

<h3>14. Neurovascular-unit / BBB / pericyte state is not just vascular transfer nuisance</h3>
<p>
Another weakness of the earlier page was that it let readers compress <strong>neurovascular support</strong> into either hemodynamic transfer audit or generic glial support. That is too weak. <a href="https://doi.org/10.1016/j.neuron.2010.09.043" target="_blank">Bell et al. (2010)</a> showed that pericytes control key neurovascular functions and neuronal phenotype, <a href="https://doi.org/10.3389/fncel.2020.00027" target="_blank">Kisler et al. (2020)</a> showed that acute cortical pericyte ablation rapidly uncouples neurovascular signaling, <a href="https://doi.org/10.1016/j.neuron.2023.08.030" target="_blank">Pandey et al. (2023)</a> showed that neuronal activity drives memory-relevant IGF2 expression from pericytes, and <a href="https://doi.org/10.1038/s41467-025-61312-0" target="_blank">Mai-Morente et al. (2025)</a> showed that pericyte pannexin1 controls capillary diameter and supports memory function. Therefore, even if graph, neural activity, and vascular confounds are audited, <strong>the neurovascular-unit / BBB / pericyte controller state can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for neurovascular-unit / barrier-side state</strong>
<p>
Human barrier-side observability is already a route-family split rather than one generic `BBB` meter. <a href="https://doi.org/10.1002/nbm.5256" target="_blank">Morgan et al. (2024)</a> and <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">Padrela et al. (2025)</a> constrain <strong>BBB water-exchange</strong> under ASL method and model choices, <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a> constrains <strong>tracer-specific BBB transport</strong> with dynamic PET and kinetic modeling, <a href="https://doi.org/10.1186/s12987-020-00218-z" target="_blank">Zhao et al. (2020)</a> constrains <strong>choroid-plexus perfusion</strong>, <a href="https://doi.org/10.1016/j.neuroimage.2021.118755" target="_blank">Petitclerc et al. (2021)</a> constrains <strong>blood-to-CSF water transport</strong>, and <a href="https://doi.org/10.1177/0271678X261429042" target="_blank">Petitclerc et al. (2026)</a> constrains a <strong>simultaneous BBB-versus-BCSFB exchange route</strong>. These papers do not share one crossed boundary, one carrier object, one model family, or one validation ceiling. On this site, human barrier routes therefore remain <strong>bounded BBB or BCSFB proxy families</strong>, not one route-free permeability scalar and not a readout of which pericyte, endothelial, or choroid-plexus epithelial controller is active.
</p>
</div>

<h3>15. Glial substrate-routing is not generic astrocyte or energetic support</h3>
<p>
The current site had already separated neuronal mitochondrial support and astrocyte ensembles elsewhere, but this central page still left too much room to compress <strong>glial fuel support</strong> into either generic astrocyte-state or one energetic row. Primary literature does not permit that shortcut. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a> showed that astrocyte-neuron lactate transport is required for long-term memory formation, <a href="https://doi.org/10.1038/s42255-022-00528-6" target="_blank">Silva et al. (2022)</a> showed that glial ketogenesis regulates memory maintenance during starvation, <a href="https://doi.org/10.1038/s42255-025-01416-5" target="_blank">Pavlowsky et al. (2025)</a> showed an intensive-learning glia-to-neuron fatty-acid route, <a href="https://doi.org/10.1038/s42255-025-01389-5" target="_blank">Greda et al. (2025)</a> showed an apoE3 / sortilin-dependent neuronal lipid-uptake and fuel-choice route, and <a href="https://doi.org/10.1016/j.celrep.2020.108572" target="_blank">Qi et al. (2021)</a> showed that even neuron-astrocyte fatty-acid coupling is genotype-sensitive. These are not one interchangeable glial-support variable: they differ in supplier cell, neuronal sink, fuel object / carrier, and regime trigger. Therefore, even if graph, nominal neural activity, astrocyte-related proxy, and macro energetic imaging are acknowledged, <strong>the operative supplier-fuel-sink route can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for glial substrate-routing</strong>
<p>
Human energetic and astrocyte-related routes are still bounded proxy classes rather than direct supplier-fuel-sink readouts. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a>, <a href="https://doi.org/10.1002/mrm.26560" target="_blank">Ren et al. (2017)</a>, <a href="https://doi.org/10.3389/fnins.2024.1389111" target="_blank">Guo et al. (2024)</a>, <a href="https://doi.org/10.1177/0271678X261415784" target="_blank">Kaiser et al. (2026)</a>, <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a>, and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> constrain macro energetic quantity types, while <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">Villemagne et al. (2022)</a>, <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">Matsuoka et al. (2026)</a>, and <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a> constrain target-defined astrocyte-related PET routes. Those human lanes can bound observability, but they do not directly identify which glial supplier delivered which fuel through which transport route to which neuronal sink. On this site, current human energetic imaging and astrocyte PET therefore remain <strong>bounded clues</strong>, not glial substrate-routing closure.
</p>
</div>

<h3>16. Astrocyte-state is not generic glial background</h3>
<p>
The earlier wording that "glia matters" was directionally correct but still too coarse. Primary literature now supports a narrower astrocyte reading. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> showed that local neurotransmitter inputs are encoded into broad cortical astrocyte-network responses over minutes, <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a> showed that learning-associated astrocyte ensembles regulate memory recall, <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> showed that the astrocytic ensemble can act as a multiday stabilization trace, and <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> showed that astrocytes enable amygdala neural representations supporting memory. Therefore, even if graph, synapses, and generic glial support are acknowledged, <strong>the operative astrocyte-state can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for astrocyte-state</strong>
<p>
Human astrocyte-related evidence is still proxy-class evidence. <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">Villemagne et al. (2022)</a> characterized <sup>18</sup>F-SMBT-1 as a first-in-human MAO-B PET tracer for reactive astrogliosis, <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">Matsuoka et al. (2026)</a> showed that <sup>11</sup>C-SL25.1188 can be quantified with a simplified MAO-B route in Alzheimer's disease, <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a> showed that <sup>11</sup>C-BU99008 is an I<sub>2</sub>BS route rather than the same molecular target, <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">Livingston et al. (2022)</a> showed BU99008 uptake varies with region and impairment stage, and <a href="https://doi.org/10.1007/s00401-024-02712-2" target="_blank">Jaisa-Aad et al. (2024)</a> showed cortical MAO-B varies across AD/ADRD classes. That is useful evidence that human astrocyte-related routes exist, but it does not become ground truth of learning-associated astrocyte ensembles, recall-state identity, or arbitrary content-related astrocyte coding. On this site, current human astrocyte PET therefore remains a <strong>target-defined astrocyte-related proxy class</strong>, not astrocyte-state closure.
</p>
</div>

<h3>17. Clearance / immune support is not passive cleanup</h3>
<p>
The current site had already become stronger on maintenance-state language, but this page still let <strong>clearance / immune support</strong> hide inside generic support biology. That was too weak. <a href="https://doi.org/10.1038/nature14432" target="_blank">Louveau et al. (2015)</a> and <a href="https://doi.org/10.1038/s41586-019-1419-5" target="_blank">Ahn et al. (2019)</a> showed that CNS lymphatic drainage is a real anatomical and functional route, and <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> showed that a meningeal-lymphatics-microglia axis regulates synaptic physiology. Therefore, even if graph and astrocyte support are known, <strong>multiday clearance / immune-controller state can still remain latent</strong>.
</p>
<div class="note-box">
<strong>Human observability ceiling for clearance / immune support</strong>
<p>
Human clearance evidence also remains a route-split proxy family rather than one glymphatic meter. <a href="https://doi.org/10.1126/science.aax5440" target="_blank">Fultz et al. (2019)</a> constrains <strong>macroscopic CSF oscillation</strong> during sleep, <a href="https://doi.org/10.1016/j.neuroimage.2025.121142" target="_blank">Kim, Huang, &amp; Liu (2025)</a> constrains <strong>parenchyma-CSF water exchange</strong>, <a href="https://doi.org/10.1038/s41467-023-37685-5" target="_blank">Eide et al. (2023)</a> constrains an <strong>intrathecal-tracer / CSF-to-blood-clearance-capacity route</strong>, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> constrains <strong>CSF mobility</strong>, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> constrains a <strong>model-based overnight biomarker-efflux route</strong>. Those routes do not share one crossed boundary, one time window, one transport object, or one model burden, and they still do not become direct readouts of local microglial controller state, synapse-specific maintenance logic, or cell-resolved clearance routing. On this site, human clearance evidence therefore remains <strong>macro support-state proxy families</strong>, not one route-free human clearance truth.
</p>
</div>
</section>

<section class="section" id="augmentation-ablation">
<h2 class="section-title">Don't end with enumeration, compare with augmentation / ablation</h2>
<p>
The weakness of the current site was that even if it was possible to enumerate the missing state variables, it did not bring to the fore what additional information and which error terms could be reduced to advance to a stronger claim. Primary literature from 2024-2026 shows that when you add same-brain function, transcriptomic label, activity-dependent transcription / chromatin audit, post-transcriptional RNA-state audit, ECM / PNN state, ionic milieu / chloride-homeostasis audit, shared extracellular / electrical-state audit, thermal-state, local transmitter dynamics, bioenergetic support, neurovascular support, glial substrate-routing, astrocyte-state, clearance / immune support, and recovery log from the connectome-only baseline, the improvement is different. Therefore, on this site, instead of counting state variables as "present/absent," we will compare held-out predictive gain using augmentation/ablation.
</p>
<table class="data-table">
<thead>
<tr>
<th>Comparison stage</th>
<th>Information to add</th>
<th>Improvements suggested by primary literature</th>
<th>Walls that still remain</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>connectome-only baseline</strong></td>
<td>Recurrent model with wiring constraints and unknown parameters to be filled in by learning. </td>
<td>Lappalainen et al. showed a wide range of activity predictions using the fly visual system, and Beiran and Litwin-Kumar showed that even if a connectome is provided, the dynamics can be largely degenerate due to differences in unmeasured biophysical parameters. </td>
<td>Successful connectome-only advances conditional activity prediction, but a unique internal state or state-complete reconstruction remains unreadable. </td>
</tr>
<tr>
<td><strong>+ same-brain function / behavior</strong></td>
<td>Co-registered functional measurements and behavioral states in the same individual. </td>
<td>Bosch and MICrONS show that same-brain activity plus later ultrastructure can build a sequential local scaffold for comparing structure and state-dependent function within one preparation, while Ding shows that validated stimulus-conditioned predictors can exploit that scaffold. </td>
<td>The bridge remains local and sequential, and it does not by itself guarantee same-time whole-state capture, current synaptic efficacy, direct transcriptomic truth, unique dynamics, or whole-brain generalization. </td>
</tr>
<tr>
<td><strong>+ transcriptomic / cell-type label</strong></td>
<td>Predicted or directly measured transcriptomic type and target specificity with same-brain or proximity conditions. </td>
<td>Gamlin et al. demonstrated that connectivity motifs, synaptic properties, and myelination differ systematically among <strong>predicted</strong> Sst transcriptomic types, embodying the incremental value of node labels while keeping the morphology-to-transcriptomics bridge explicit. </td>
<td>Within-type heterogeneity and morpho-electric variability remain, and morphology-linked predicted labels are still not the same as direct transcriptomic assay in the EM volume, so threshold / gain / set point will still be latent. </td>
</tr>
<tr>
<td><strong>+ activity-dependent transcription / chromatin audit</strong></td>
<td>Compare a connectome or cell-atlas baseline against the same model with time-stamped expression / chromatin measurements or causal epigenetic intervention under the same held-out learning or stabilization condition. </td>
<td>You can state more narrowly how much allocation eligibility, late memory stabilization, or locus-specific plasticity control improves once current transcriptional / chromatin state is treated explicitly. </td>
<td>A static atlas or one-shot DEG list remains identity/context annotation or a time-stamped clue, not a ground truth of current plasticity state. </td>
</tr>
<tr>
<td><strong>+ local proteostasis / synaptic-tagging audit</strong></td>
<td>Compare a synapse- or transcription-aware baseline against the same model with tag/PRP capture measurements, branch-local structural-tag proxy, or local translation/degradation/autophagy perturbation under the same held-out stabilization condition. </td>
<td>Frey, Shires, Govindarajan, Fonseca, Pandey, and Thomas together support that late stabilization and reconsolidation can be read more narrowly once branch-local capture routes are treated explicitly. </td>
<td>A current weight estimate or one-shot transcriptomic change remains a snapshot and does not become ground truth of the late-stabilization route. </td>
</tr>
<tr>
<td><strong>+ cargo-transport / cytoskeletal-trafficking audit</strong></td>
<td>Compare a synapse-, proteostasis-, or bioenergetics-aware baseline against the same model with recycling-endosome measurements, cargo-transport perturbation, motor-protein manipulation, or externally calibrated branch/bouton delivery route under the same held-out stabilization or synaptogenesis condition. </td>
<td>Park, Maas, Yin, Zhao, Swarnkar, and Aiken together support that branch-specific receptor delivery, local RNA/protein localization, and presynaptic cargo retention can be read more narrowly once transport state is treated explicitly. </td>
<td>A weight estimate, a transcriptomic clue, or a macro energetic proxy remains too coarse to become ground truth of compartment-specific cargo delivery in vivo. </td>
</tr>
<tr>
<td><strong>+ ECM / PNN state audit</strong></td>
<td>Compare a synapse- or connectome-based baseline against the same model with matrix markers, local matrix perturbation, or externally calibrated ECM state under the same held-out plasticity or recovery conditions. </td>
<td>Pizzorusso, Frischknecht, Gogolla, and Jabłońska together support that adult plasticity, receptor mobility, inhibitory stabilization, and memory-update resistance can be read more narrowly once matrix state is treated explicitly. </td>
<td>Histology, pathology, or generic scaffold annotation alone do not become a ground truth of current ECM / PNN state in vivo. </td>
</tr>
<tr>
<td><strong>+ ionic milieu / chloride-homeostasis audit</strong></td>
<td>Compare a synapse- or excitability-aware baseline against the same model with chloride-state measurements, ionic manipulations, transporter-state perturbation, or externally calibrated ionic proxy under the same held-out memory, rhythm, or state-transition conditions. </td>
<td>Glykys, Heubl, Ding, Huberfeld, Simonnet, and Nakamura together support that inhibitory sign, rhythm stability, state transitions, and some learning-relevant plasticity can be read more narrowly once chloride / ionic state is treated explicitly. </td>
<td>Human sodium MRI or pathology alone remains a macro or disease-linked proxy and does not become ground truth of local chloride homeostasis in vivo. </td>
</tr>
<tr>
<td><strong>+ shared extracellular / electrical-state audit</strong></td>
<td>Compare a chemical-connectome or synapse-aware baseline against the same model with gap-junction measurements or perturbation, local field calibration, extracellular-space geometry / diffusion audit, osmotic manipulation, sleep-linked interstitial-space logging, or direct inhibitory-driving-force measurement under the same held-out synchrony, sleep-oscillation, spillover, or state-switch condition.</td>
<td>Galarreta, Anastassiou, Graydon, Kilb, Lauderdale, Xie, Burman, Yang, Selfe, Voldsbekk, and Feld together support that fast synchrony, oscillatory coordination, spillover, and extracellular / electrical-state regime can be read more narrowly once coupling topology, extracellular geometry, inhibitory driving force, and human clue classes are kept on separate rows.</td>
<td>Human perturbation, macro field, or diffusion-MRI proxy evidence alone remains indirect and does not become ground truth of local electrical coupling, extracellular-space geometry, or cell-specific inhibitory driving force in vivo.</td>
</tr>
<tr>
<td><strong>+ timing-state / conduction audit</strong></td>
<td>Compare a fixed-delay baseline against the same model or analysis after naming the <strong>timing claim family</strong>, adding measured or externally calibrated node / internode / periaxonal / myelin variables, and keeping recovery boundary plus human quantity type explicit under the same held-out phase, synchrony, plasticity, or recovery condition. </td>
<td>Gibson, McKenzie, Seidl, Dutta, Cohen, Micheva, Dubey, Xin, and Della-Flora Nunes together support that timing-sensitive prediction can improve when learning-linked oligodendrogenesis, node / internode / periaxonal structure, myelination-linked local speed, plasticity-brake state, and incomplete-versus-complete remyelination are kept on separate rows. </td>
<td>Human tract-speed, MWF, MT-family, bilayer-sensitive, developmental dMRI, or qT1 remyelination-sensitive routes remain typed macro proxies; without external calibration they do not become per-axon timing ground truth or proof that healthy timing-state was fully restored. </td>
</tr>
<tr>
<td><strong>+ thermal-state audit</strong></td>
<td>Compare a timing- or activity-aware baseline against the same model with local temperature logs, heating / cooling perturbation, or externally calibrated thermometry under the same held-out operating-point, sequence-timing, or readout-confound condition.</td>
<td>Hardingham, Moser, Long, Reig, Owen, and Boorman together support that thermal-state can narrow operating-point, timing-perturbation, and heating-artifact claims when it is kept separate from timing-state and ATP support.</td>
<td>Human MRS thermometry or daily temperature maps remain macro thermal proxies and do not become cell-specific thermal-state ground truth.</td>
</tr>
<tr>
<td><strong>+ local transmitter dynamics</strong></td>
<td>Local cholinergic axon activity or behavior-linked transmitter proxy. </td>
<td>Neyhart et al. showed that while cortical ACh dynamics can be fairly predicted from cholinergic axon activity and behavioral state, locality changes with distance from neighboring axons and clearance kinetics. </td>
<td>pupil / behavior / global arousal is still a coarse proxy and cannot be automatically promoted to transmitter-specific or region-specific ground truth. </td>
</tr>
<tr>
<td><strong>+ bioenergetic / mitochondrial audit</strong></td>
<td>Compare an activity- or cargo-aware baseline against the same model with ATP-linked respiration, mitochondrial positioning / fission, ATP-synthase organization, or externally calibrated macro energetic proxy under the same held-out plasticity or fatigue condition.</td>
<td>Rangaraju, Divakaruni, Underwood, Hu, and Vishwanath together support that local energetic support can narrow high-demand plasticity and memory claims when the mitochondrial controller is treated explicitly.</td>
<td>Human 31P-MRS or dynamic DMRSI remains a macro energetic proxy and does not become branch- or bouton-specific mitochondrial-state ground truth.</td>
</tr>
<tr>
<td><strong>+ neurovascular / BBB audit</strong></td>
<td>Compare a neural-activity or vascular-transfer-aware baseline against the same model with pericyte / endothelial perturbation, BBB water-exchange, tracer-specific BBB transport, blood-CSF-barrier / choroid-plexus route, or externally calibrated support-state proxy under the same held-out coupling or memory condition.</td>
<td>Bell, Kisler, Pandey, Mai-Morente, Morgan, Chung, Zhao, and Petitclerc together support that neurovascular-unit / barrier state can narrow capillary-control and permeability claims once controller biology and barrier route family are kept separate.</td>
<td>Human BBB / BCSFB MRI or PET remains a macro barrier-support proxy family and does not become local pericyte, endothelial, or choroid-plexus-controller ground truth.</td>
</tr>
<tr>
<td><strong>+ glial substrate-routing audit</strong></td>
<td>Compare an energetic- or astrocyte-aware baseline against the same model with a named glia-to-neuron fuel-support observable or perturbation that fixes supplier cell, neuronal sink, fuel object / carrier, and nutrient or learning regime under the same held-out recall, stabilization, or metabolic-stress condition.</td>
<td>Suzuki, Silva, Pavlowsky, Greda, and Qi together support that named routing families can narrow memory-support and stress-regime claims once supplier-fuel-sink logic is kept explicit instead of compressed into generic glial support.</td>
<td>Human 31P / deuterium energetic imaging and astrocyte-related PET remain macro energetic or target-defined proxy classes and do not become direct supplier-fuel-sink ground truth.</td>
</tr>
<tr>
<td><strong>+ astrocyte-state audit</strong></td>
<td>Compare a synapse- or glial-routing-aware baseline against the same model with astrocyte-network state, ensemble perturbation, or externally calibrated human astrocyte proxy under the same held-out recall or stabilization condition.</td>
<td>Cahill, Williamson, Dewa, and Bukalo together support that astrocyte-state can narrow encoding, recall, representation, and stabilization claims once ensemble state is treated explicitly.</td>
<td>Human MAO-B or I<sub>2</sub>BS astrocyte-related PET remains a target-defined proxy route and does not become ground truth of learning-associated astrocyte ensembles.</td>
</tr>
<tr>
<td><strong>+ clearance / immune audit</strong></td>
<td>Compare an astrocyte- or neurovascular-aware baseline against the same model with lymphatic / CSF routing, microglia-linked synaptic readout, or externally calibrated human clearance proxy under the same multiday recovery or support condition.</td>
<td>Louveau, Ahn, Kim, Fultz, Kim, Huang, &amp; Liu, Eide, Hirschler, and Dagum together support that clearance / immune support can narrow multiday maintenance claims once drainage anatomy, synaptic physiology, and human transport-side proxy families are not compressed into one row.</td>
<td>Human CSF oscillation, parenchyma-CSF exchange, intrathecal-tracer clearance, CSF-mobility, or biomarker-efflux routes remain macro support-state proxies and do not become local immune-controller ground truth.</td>
</tr>
<tr>
<td><strong>+ astrocyte / clearance recovery log</strong></td>
<td>Record whether the model includes astrocyte-state, clearance / immune support, or both, and compare recovery / retention under the same elapsed-time and sleep-history condition.</td>
<td>Adding this log makes it harder to silently promote a same-day fit into multiday maintenance readiness when astrocyte and clearance families were omitted.</td>
<td>The exact contribution still depends on task, species, and external calibration; adding the log does not collapse the remaining hidden-state family.</td>
</tr>
<tr>
<td><strong>+ perturbation / recovery of excitability-homeostasis</strong></td>
<td>Intrinsic excitability, recovery time, and memory allocation metrics before and after learning or after intervention. </td>
<td>Hadzibegovic et al. showed that early intrinsic excitability plasticity of neocortical engram neurons regulates memory formation and precision, and substantiated the value of adding the recovery log. </td>
<td>This is engram-specific and early-window evidence, and cannot replace the whole-brain long-term controller. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Conditions for passing on this site</strong>
<p>
An added state variable can be described as ``effective'' if it shows a predictive gain in any of the cross-state / cross-day / perturbation / recovery conditions when comparing <strong>(a) connectome-only baseline</strong> and <strong>(b) model with additional variables under the same split / same held-out conditions</strong>, and at the same time shows <strong>proxy specificity</strong>, <strong>family / uncertainty</strong>, <strong>abstention</strong>, and the <strong>time scale at which the added variable was observed or calibrated</strong>. If it does not go that far, this site treats it as an annotation, stratification covariate, or post hoc explanation.
</p>
</div>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Reading rules and minimum submissions adopted on this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>connectome-complete:</strong> Treat as a structural atlas, candidate scaffold, and starting point for compaction. It is not written as achieving L2/L3 emulation. </li>
<li><strong>connectome-constrained model:</strong> First of all, it is treated as a hypothesis engine / conditional model. It is not written as the unique solution of the internal state. </li>
<li><strong>same-brain functional connectomics:</strong>Do not collapse sequential bridge, morphology-linked predicted labels, current synaptic-state caveats, and dynamical-identifiability burden into one local twin. If those four ceilings are not separately disclosed, keep the claim at scaffold plus task-bounded conditional prediction.</li>
<li><strong>augmentation / ablation:</strong>You can't write that "the added state variable worked" without putting a connectome-only baseline. </li>
<li><strong>transcriptomic atlas is not current chromatin state:</strong>Do not auto-complete memory-stabilization controller from cell identity or one-shot DEG evidence. </li>
<li><strong>gene-level abundance is not post-transcriptional RNA-state:</strong>Do not auto-complete isoform choice, m6A-dependent translation / degradation, or RNA-editing controller from transcript counts alone. </li>
<li><strong>intrinsic excitability / homeostatic set point:</strong>Do not automatically infer from cell-type label or short-term activity matching. If not measured, write latent state. </li>
<li><strong>local proteostasis / synaptic tagging:</strong>Do not auto-complete late stabilization from current weight alone. If not measured, write latent state. </li>
<li><strong>cargo-transport / cytoskeletal trafficking state:</strong>Do not collapse compartment-specific receptor, endosome, RNA, or presynaptic cargo delivery into weight, proteostasis, or ATP support. If not measured, write latent state. </li>
<li><strong>ECM / PNN state:</strong>Do not collapse plasticity gate, receptor mobility, or memory-stabilization resistance into synapse count or glial support. If not measured, write latent state. </li>
<li><strong>ionic milieu / chloride homeostasis:</strong>Do not collapse inhibitory sign or state-transition regime into cell type, weight snapshot, or generic excitability. If not measured, write latent state. </li>
<li><strong>shared extracellular / electrical state:</strong>Do not collapse gap junctions, endogenous field effects, extracellular-space geometry / diffusion barriers / osmotic regime, or inhibitory driving force into the chemical connectome or a generic ionic proxy. If not measured, write latent state.</li>
<li><strong>Delay is not one scalar:</strong>If timing matters, separate device latency, biological timing-state, and phase error; if the biological side is not measured, write timing-state as latent. </li>
<li><strong>thermal-state:</strong>Do not collapse local temperature, heating burden, or thermal perturbation into timing-state, bioenergetics, or generic artifact language. If not measured, write latent state.</li>
<li><strong>pupil / HRV:</strong> A useful state covariate for human data, but not a transmitter-specific ground truth. </li>
<li><strong>bioenergetic / mitochondrial state:</strong>Do not collapse ATP-demand support, mitochondrial positioning, or Ca<sup>2+</sup>-efflux control into generic activity fit or macro energetic imaging. If not measured, write latent state.</li>
<li><strong>neurovascular-unit / BBB / pericyte state:</strong>Do not collapse controller-side biology into vascular transfer audit or macro BBB permeability proxy. If not measured, write latent state.</li>
<li><strong>glial substrate-routing:</strong>Do not collapse lactate-, ketone-body-, fatty-acid-, or apoE / sortilin-linked lipid routes into bioenergetics, astrocyte-state, or human macro energetic / astrocyte-related proxy language. If not measured, write latent state.</li>
<li><strong>astrocyte-state:</strong>Do not collapse network encoding, recall ensembles, fear-state representations, multiday stabilization, or human MAO-B / I<sub>2</sub>BS astrocyte-related PET into one generic glial sentence. If not measured, write latent state.</li>
<li><strong>clearance / immune support:</strong>Do not collapse drainage anatomy, microglia-linked synaptic control, CSF mobility, or glymphatic-model routes into passive cleanup language. If not measured, write latent state.</li>
<li><strong>When state variable is missing:</strong>If estimated, specify the error and abstention condition; if not, specify absent. </li>
<li>When there are no weights / timing-state: phase, timing, intervention response, and closed-loop stability claims are demoted. </li>
<li><strong>When dropping glial substrate-routing / astrocyte / clearance / neurovascular support:</strong>Write in the text which fuel-support, plasticity, recovery, support-state, or multiday-maintenance behaviors were discarded as the scope of application. </li>
<li>When multiple <strong>families remain:</strong>Rather than just confidence, expose family comparison, uncertainty, and abstention. </li>
</ul>
</div>
<table class="data-table">
<thead>
<tr>
<th>What you want to claim</th>
<th>Minimum required submissions</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Structure atlas / scaffold</strong></td>
<td>Specify handling of coverage, segmentation caveat, synapse count, and presence/absence of cell-type label. </td>
</tr>
<tr>
<td><strong>state-variable augmentation claim</strong></td>
<td>Connectome-only baseline, predictive gain under the same split/held-out conditions, ablation results, proxy specificity, family/uncertainty, and abstention are also listed. </td>
</tr>
<tr>
<td><strong>same-brain functional-connectomics claim</strong></td>
<td>Declare bridge order, carried witness, local coverage, direct assay versus predicted label-transfer route, current-synaptic-state ceiling, and dynamical uncertainty / abstention before using digital-twin or same-state language. </td>
</tr>
<tr>
<td><strong>Conditional dynamical claim</strong></td>
<td>Include same-brain function or perturbation, list of missing state variables, proxy limits, family/uncertainty, and explicit absence of intrinsic excitability/homeostatic set point, post-transcriptional RNA-state, ionic / chloride state, thermal-state, bioenergetic / mitochondrial state, neurovascular / BBB state, glial substrate-routing, astrocyte-state, and clearance / immune support if not measured. </td>
</tr>
<tr>
<td><strong>Intervention/Closed Loop claim</strong></td>
<td>In addition to the above, we will also publish calibration routes for weights / timing-state / thermal-state / neuromodulation / excitability-homeostasis / ionic milieu / bioenergetics / neurovascular support / glial substrate-routing / astrocyte-state / clearance support, plus external validation and abstention / stop conditions. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Schlegel, P., et al. (2024). Whole-brain annotation and multi-connectome cell typing of Drosophila. <em>Nature</em>, 634, 139–150. <a href="https://doi.org/10.1038/s41586-024-07686-5" target="_blank">doi:10.1038/s41586-024-07686-5</a></li>
<li>Bosch, C., Pacureanu, A., Patino, J., et al. (2022). Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. <em>Nature Communications</em>, 13, 2923. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Ding, Z., et al. (2025). Functional connectomics reveals a general wiring rule in mouse visual cortex. <em>Nature</em>, 640, 459–469. <a href="https://doi.org/10.1038/s41586-025-08840-3" target="_blank">doi:10.1038/s41586-025-08840-3</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <em>Nature</em>, 634, 1132–1140. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 2561–2574. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Shiu, P.-K., et al. (2024). A Drosophila computational brain model reveals sensorimotor processing. <em>Nature</em>, 634, 210–219. <a href="https://doi.org/10.1038/s41586-024-07763-9" target="_blank">doi:10.1038/s41586-024-07763-9</a></li>
<li>Pospisil, D. A., et al. (2024). The fly connectome reveals a path to the effectome. <em>Nature</em>, 634, 201–209. <a href="https://doi.org/10.1038/s41586-024-07982-0" target="_blank">doi:10.1038/s41586-024-07982-0</a></li>
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <em>Nature Neuroscience</em>, 7, 1345–1352. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
<li>Thomas, C., Ye, F. Q., Irfanoglu, M. O., Modi, P., Saleem, K. S., Leopold, D. A., &amp; Pierpaoli, C. (2014). Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 111(46), 16574–16579. <a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">doi:10.1073/pnas.1405672111</a></li>
<li>Reveley, C., Seth, A. K., Pierpaoli, C., Silva, A. C., Yu, D., Saunders, R. C., Leopold, D. A., &amp; Ye, F. Q. (2015). Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 112(21), E2820–E2828. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">doi:10.1073/pnas.1418198112</a></li>
<li>Schilling, K. G., Gao, Y., Janve, V., Stepniewska, I., Landman, B. A., &amp; Anderson, A. W. (2018). Confirmation of a gyral bias in diffusion MRI fiber tractography. <em>Human Brain Mapping</em>, 39(3), 1449–1466. <a href="https://doi.org/10.1002/hbm.23936" target="_blank">doi:10.1002/hbm.23936</a></li>
<li>Donahue, C. J., Sotiropoulos, S. N., Jbabdi, S., Hernandez-Fernandez, M., Behrens, T. E., Dyrby, T. B., Coalson, T., Kennedy, H., Knoblauch, K., Van Essen, D. C., &amp; Glasser, M. F. (2016). Using diffusion tractography to predict cortical connection strength and distance: A quantitative comparison with tracers in the monkey. <em>Journal of Neuroscience</em>, 36(25), 6758–6770. <a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">doi:10.1523/JNEUROSCI.0493-16.2016</a></li>
<li>Maier-Hein, K. H., Neher, P. F., Houde, J.-C., Côté, M.-A., Garyfallidis, E., Zhong, J., Chamberland, M., et al. (2017). The challenge of mapping the human connectome based on diffusion tractography. <em>Nature Communications</em>, 8, 1349. <a href="https://doi.org/10.1038/s41467-017-01285-x" target="_blank">doi:10.1038/s41467-017-01285-x</a></li>
<li>Schilling, K. G., Petit, L., Rheault, F., Remedios, S., Pierpaoli, C., Anderson, A. W., Landman, B. A., &amp; Descoteaux, M. (2020). Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. <em>Brain Structure and Function</em>, 225(8), 2387–2402. <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">doi:10.1007/s00429-020-02129-z</a></li>
<li>Grisot, G., Haber, S. N., Hawrylycz, M., Yendiki, A., et al. (2021). Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. <em>NeuroImage</em>, 239, 118300. <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">doi:10.1016/j.neuroimage.2021.118300</a></li>
<li>Sarwar, T., Ramamohanarao, K., Daducci, A., Schiavi, S., Smith, R. E., &amp; Zalesky, A. (2023). Evaluation of tractogram filtering methods using human-like connectome phantoms. <em>NeuroImage</em>, 282, 120376. <a href="https://doi.org/10.1016/j.neuroimage.2023.120376" target="_blank">doi:10.1016/j.neuroimage.2023.120376</a></li>
<li>Gajwani, M., Oldham, S., Pang, J. C., Arnatkevičiūtė, A., Tiego, J., Bellgrove, M. A., &amp; Fornito, A. (2023). Can hubs of the human connectome be identified consistently with diffusion MRI? <em>Network Neuroscience</em>, 7(4), 1326–1350. <a href="https://doi.org/10.1162/netn_a_00324" target="_blank">doi:10.1162/netn_a_00324</a></li>
<li>He, Y., Hong, Y., Wu, Y., et al. (2024). Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. <em>NeuroImage</em>, 303, 120904. <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">doi:10.1016/j.neuroimage.2024.120904</a></li>
<li>McMaster, E. M., Newlin, N. R., Rudravaram, G., et al. (2025). Harmonized connectome resampling for variance in voxel sizes. <em>Magnetic Resonance Imaging</em>, 121, 110424. <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">doi:10.1016/j.mri.2025.110424</a></li>
<li>Bramati, I. B., Szczupak, D., Carneiro Monteiro, M., Meireles, F., Menezes Guimarães, D., Dean, R. J., Paul, L. K., &amp; Tovar-Moll, F. (2026). Diffusion MRI sampling schemes bias diffusion metrics and tractography. <em>Frontiers in Neuroimaging</em>, 5, 1670604. <a href="https://doi.org/10.3389/fnimg.2026.1670604" target="_blank">doi:10.3389/fnimg.2026.1670604</a></li>
<li>Manzano-Patrón, J. P., Deistler, M., Schröder, C., et al. (2025). Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. <em>Medical Image Analysis</em>, 103, 103580. <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">doi:10.1016/j.media.2025.103580</a></li>
<li>Zhu, S., Huszar, I. N., Cottaar, M., et al. (2025). Imaging the structural connectome with hybrid MRI-microscopy tractography. <em>Medical Image Analysis</em>, 102, 103498. <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">doi:10.1016/j.media.2025.103498</a></li>
<li>Galarreta, M., &amp; Hestrin, S. (1999). A network of fast-spiking cells in the neocortex connected by electrical synapses. <em>Nature</em>, 402, 72–75. <a href="https://doi.org/10.1038/47029" target="_blank">doi:10.1038/47029</a></li>
<li>Anastassiou, C. A., Perin, R., Markram, H., &amp; Koch, C. (2011). Ephaptic coupling of cortical neurons. <em>Nature Neuroscience</em>, 14(2), 217–223. <a href="https://doi.org/10.1038/nn.2727" target="_blank">doi:10.1038/nn.2727</a></li>
<li>Graydon, C. W., Cho, S., Diamond, J. S., Kachar, B., von Gersdorff, H., &amp; Grimes, W. N. (2014). Specialized postsynaptic morphology enhances neurotransmitter dilution and high-frequency signaling at an auditory synapse. <em>Journal of Neuroscience</em>, 34(24), 8358–8372. <a href="https://doi.org/10.1523/JNEUROSCI.4493-13.2014" target="_blank">doi:10.1523/JNEUROSCI.4493-13.2014</a></li>
<li>Kilb, W., Dierkes, P. W., Syková, E., Vargová, L., &amp; Luhmann, H. J. (2006). Hypoosmolar conditions reduce extracellular volume fraction and enhance epileptiform activity in the CA3 region of the immature rat hippocampus. <em>Journal of Neuroscience Research</em>, 84(1), 119–129. <a href="https://doi.org/10.1002/jnr.20871" target="_blank">doi:10.1002/jnr.20871</a></li>
<li>Xie, L., Kang, H., Xu, Q., Chen, M. J., Liao, Y., Thiyagarajan, M., O'Donnell, J., Christensen, D. J., Nicholson, C., Iliff, J. J., Takano, T., Deane, R., &amp; Nedergaard, M. (2013). Sleep drives metabolite clearance from the adult brain. <em>Science</em>, 342(6156), 373–377. <a href="https://doi.org/10.1126/science.1241224" target="_blank">doi:10.1126/science.1241224</a></li>
<li>Lauderdale, K., Murphy, T., Tung, T., Davila, D., Binder, D. K., &amp; Fiacco, T. A. (2015). Osmotic Edema Rapidly Increases Neuronal Excitability Through Activation of NMDA Receptor-Dependent Slow Inward Currents in Juvenile and Adult Hippocampus. <em>ASN Neuro</em>, 7(5), 1759091415605115. <a href="https://doi.org/10.1177/1759091415605115" target="_blank">doi:10.1177/1759091415605115</a></li>
<li>Burman, R. J., Brodersen, P. J. N., Raimondo, J. V., Sen, A., &amp; Akerman, C. J. (2023). Active cortical networks promote shunting fast synaptic inhibition in vivo. <em>Neuron</em>, 111(22), 3531–3540.e6. <a href="https://doi.org/10.1016/j.neuron.2023.08.005" target="_blank">doi:10.1016/j.neuron.2023.08.005</a></li>
<li>Yang, Y.-C., Wang, G.-H., Chou, P., Hsueh, S.-W., Lai, Y.-C., &amp; Kuo, C.-C. (2024). Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 121(8), e2313042121. <a href="https://doi.org/10.1073/pnas.2313042121" target="_blank">doi:10.1073/pnas.2313042121</a></li>
<li>Selfe, J. S., et al. (2024). All-optical reporting of inhibitory receptor driving force in the nervous system. <em>Nature Communications</em>, 15(1), 8913. <a href="https://doi.org/10.1038/s41467-024-53074-y" target="_blank">doi:10.1038/s41467-024-53074-y</a></li>
<li>Voldsbekk, I., Maximov, I. I., Zak, N., Roelfs, D., Geier, O., Due-Tønnessen, P., Elvsåshagen, T., Strømstad, M., Bjørnerud, A., &amp; Groote, I. (2020). Evidence for wakefulness-related changes to extracellular space in human brain white matter from diffusion-weighted MRI. <em>NeuroImage</em>, 212, 116682. <a href="https://doi.org/10.1016/j.neuroimage.2020.116682" target="_blank">doi:10.1016/j.neuroimage.2020.116682</a></li>
<li>Feld, G. B., Niethard, N., Liu, J., et al. (2026). Electrical synapses contribute to sleep-dependent declarative memory retention. <em>European Journal of Neuroscience</em>, 63(2), e70401. <a href="https://doi.org/10.1111/ejn.70401" target="_blank">doi:10.1111/ejn.70401</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497–505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Santoni, G., et al. (2024). Chromatin plasticity predetermines neuronal eligibility for memory trace formation. <em>Science</em>, 385(6716), eadg9982. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">doi:10.1126/science.adg9982</a></li>
<li>Traunmüller, L., et al. (2025). Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. <em>Nature Communications</em>, 16, 7787. <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">doi:10.1038/s41467-025-63029-6</a></li>
<li>Coda, D. M., Watt, L., Glauser, L., et al. (2025). Cell-type- and locus-specific epigenetic editing of memory expression. <em>Nature Genetics</em>, 57, 2661–2668. <a href="https://doi.org/10.1038/s41588-025-02368-y" target="_blank">doi:10.1038/s41588-025-02368-y</a></li>
<li>Terceros, A., Chen, C., Harada, Y., et al. (2026). Thalamocortical transcriptional gates coordinate memory stabilization. <em>Nature</em>, 649, 1254–1263. <a href="https://doi.org/10.1038/s41586-025-09774-6" target="_blank">doi:10.1038/s41586-025-09774-6</a></li>
<li>Wang, J., Telese, F., Tan, Y., et al. (2015). LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. <em>Nature Neuroscience</em>, 18(9), 1256–1264. <a href="https://doi.org/10.1038/nn.4069" target="_blank">doi:10.1038/nn.4069</a></li>
<li>Dai, J., Aoto, J., &amp; Südhof, T. C. (2019). Alternative splicing of presynaptic neurexins differentially controls postsynaptic NMDA and AMPA receptor responses. <em>Neuron</em>, 102(5), 993–1008.e5. <a href="https://doi.org/10.1016/j.neuron.2019.03.032" target="_blank">doi:10.1016/j.neuron.2019.03.032</a></li>
<li>Shi, H., Zhang, X., Weng, Y.-L., et al. (2018). m6A facilitates hippocampus-dependent learning and memory through YTHDF1. <em>Nature</em>, 563(7730), 249–253. <a href="https://doi.org/10.1038/s41586-018-0666-1" target="_blank">doi:10.1038/s41586-018-0666-1</a></li>
<li>Peterson, L. N., Kasper, J. M., Allgaier, J. A., et al. (2025). ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. <em>Science Signaling</em>, 18(886), eadr1442. <a href="https://doi.org/10.1126/scisignal.adr1442" target="_blank">doi:10.1126/scisignal.adr1442</a></li>
<li>Joglekar, A., Prjibelski, A., Mahfouz, A., et al. (2024). Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. <em>Nature Neuroscience</em>, 27(6), 1073–1088. <a href="https://doi.org/10.1038/s41593-024-01616-4" target="_blank">doi:10.1038/s41593-024-01616-4</a></li>
<li>Li, Y., Zhu, M., Li, X., et al. (2025). Enhanced Protein Synthesis and Hippocampus-Dependent Memory via Inhibition of YTHDF2-Mediated m6A mRNA Degradation. <em>Advanced Science</em>, 12(34), e14926. <a href="https://doi.org/10.1002/advs.202514926" target="_blank">doi:10.1002/advs.202514926</a></li>
<li>Giese, K. P., Fedorov, N. B., Filipkowski, R. K., &amp; Silva, A. J. (1998). Autophosphorylation at Thr286 of the alpha calcium-calmodulin kinase II in LTP and learning. <em>Science</em>, 279(5352), 870–873. <a href="https://doi.org/10.1126/science.279.5352.870" target="_blank">doi:10.1126/science.279.5352.870</a></li>
<li>Lee, H.-K., Barbarosie, M., Kameyama, K., Bear, M. F., &amp; Huganir, R. L. (2003). Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. <em>Cell</em>, 112(5), 631–643. <a href="https://doi.org/10.1016/S0092-8674(03)00122-3" target="_blank">doi:10.1016/S0092-8674(03)00122-3</a></li>
<li>Rodrigues, S. M., Farb, C. R., Bauer, E. P., LeDoux, J. E., &amp; Schafe, G. E. (2004). Pavlovian fear conditioning regulates Thr286 autophosphorylation of Ca2+/calmodulin-dependent protein kinase II at lateral amygdala synapses. <em>Journal of Neuroscience</em>, 24(13), 3281–3288. <a href="https://doi.org/10.1523/JNEUROSCI.5303-03.2004" target="_blank">doi:10.1523/JNEUROSCI.5303-03.2004</a></li>
<li>Tomita, S., Stein, V., Stocker, T. J., Nicoll, R. A., &amp; Bredt, D. S. (2005). Bidirectional synaptic plasticity regulated by phosphorylation of stargazin-like TARPs. <em>Neuron</em>, 45(2), 269–277. <a href="https://doi.org/10.1016/j.neuron.2005.01.009" target="_blank">doi:10.1016/j.neuron.2005.01.009</a></li>
<li>Vierra, N. C., et al. (2023). Endoplasmic reticulum-plasma membrane junctions couple electrical activity to Ca2+-activated PKA signaling in neurons. <em>Nature Communications</em>, 14, 6040. <a href="https://doi.org/10.1038/s41467-023-40930-6" target="_blank">doi:10.1038/s41467-023-40930-6</a></li>
<li>Biswas, D., et al. (2023). The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. <em>Journal of Proteome Research</em>, 22(4), 1390–1404. <a href="https://doi.org/10.1021/acs.jproteome.2c00244" target="_blank">doi:10.1021/acs.jproteome.2c00244</a></li>
<li>Frey, U., &amp; Morris, R. G. M. (1997). Synaptic tagging and long-term potentiation. <em>Nature</em>, 385(6616), 533–536. <a href="https://doi.org/10.1038/385533a0" target="_blank">doi:10.1038/385533a0</a></li>
<li>Fonseca, R., Vabulas, R. M., Hartl, F. U., Bonhoeffer, T., &amp; Nägerl, U. V. (2006). A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. <em>Neuron</em>, 52(2), 239–245. <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">doi:10.1016/j.neuron.2006.08.015</a></li>
<li>Govindarajan, A., Israely, I., Huang, S.-Y., &amp; Tonegawa, S. (2011). The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. <em>Neuron</em>, 69(1), 132–146. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">doi:10.1016/j.neuron.2010.12.008</a></li>
<li>Shires, K. L., Da Silva, B. M., Hawthorne, J. P., Morris, R. G. M., &amp; Martin, S. J. (2012). Synaptic tagging and capture in the living rat. <em>Nature Communications</em>, 3, 1246. <a href="https://doi.org/10.1038/ncomms2250" target="_blank">doi:10.1038/ncomms2250</a></li>
<li>Pandey, K., Yu, X.-W., Steinmetz, A., &amp; Alberini, C. M. (2021). Autophagy coupled to translation is required for long-term memory formation. <em>Autophagy</em>, 17(9), 2489–2505. <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">doi:10.1080/15548627.2020.1775393</a></li>
<li>Thomas, M., Bogaciu, C.-A., Rizzoli, S. O., et al. (2025). Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. <em>Communications Biology</em>, 8, 756. <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">doi:10.1038/s42003-025-08459-0</a></li>
<li>Park, M., Salgado, J. M., Ostroff, L., Helton, T. D., Robinson, C. G., Harris, K. M., &amp; Ehlers, M. D. (2006). Plasticity-induced growth of dendritic spines by exocytic trafficking from recycling endosomes. <em>Neuron</em>, 52(5), 817-830. <a href="https://doi.org/10.1016/j.neuron.2006.09.040" target="_blank">doi:10.1016/j.neuron.2006.09.040</a></li>
<li>Maas, C., Belgardt, D., Lee, H. K., Heisler, F. F., Lappe-Siefke, C., Magiera, M. M., van Dijk, J., Hausrat, T. J., Janke, C., &amp; Kneussel, M. (2009). Synaptic activation modifies microtubules underlying transport of postsynaptic cargo. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 106(21), 8731-8736. <a href="https://doi.org/10.1073/pnas.0902304106" target="_blank">doi:10.1073/pnas.0902304106</a></li>
<li>Yin, X., Takei, Y., Kido, M. A., &amp; Hirokawa, N. (2011). Molecular motor KIF17 is fundamental for memory and learning via differential support of synaptic NR2A/2B levels. <em>Neuron</em>, 70(2), 310-325. <a href="https://doi.org/10.1016/j.neuron.2011.03.026" target="_blank">doi:10.1016/j.neuron.2011.03.026</a></li>
<li>Zhao, J., Fok, A. H. K., Fan, R., Kwan, P.-Y., Chan, H.-L., Lo, L. H.-Y., Chan, Y.-S., Yung, W.-H., Huang, J., Lai, C. S. W., &amp; Lai, K.-O. (2020). Specific depletion of the motor protein KIF5B leads to deficits in dendritic transport, synaptic plasticity and memory. <em>eLife</em>, 9, e53456. <a href="https://doi.org/10.7554/eLife.53456" target="_blank">doi:10.7554/eLife.53456</a></li>
<li>Swarnkar, S., Avchalumov, Y., Espadas, I., Grinman, E., Liu, X.-A., Raveendra, B. L., Zucca, A., Mediouni, S., Sadhu, A., Valente, S., Page, D., Miller, K., &amp; Puthanveettil, S. V. (2021). Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. <em>Cell Reports</em>, 36(2), 109369. <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">doi:10.1016/j.celrep.2021.109369</a></li>
<li>Aiken, J., &amp; Holzbaur, E. L. F. (2024). Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. <em>Current Biology</em>, 34(8), 1687-1704.e8. <a href="https://doi.org/10.1016/j.cub.2024.03.010" target="_blank">doi:10.1016/j.cub.2024.03.010</a></li>
<li>Holler, S., et al. (2021). Structure and function of a neocortical synapse. <em>Nature</em>, 591, 111–116. <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">doi:10.1038/s41586-020-03134-2</a></li>
<li>Moln&aacute;r, G., R&oacute;zsa, M., Baka, J., Holderith, N., Barz&oacute;, P., Nusser, Z., &amp; Tam&aacute;s, G. (2016). Human pyramidal to interneuron synapses are mediated by multi-vesicular release and multiple docked vesicles. <em>eLife</em>, 5, e18167. <a href="https://doi.org/10.7554/eLife.18167" target="_blank">doi:10.7554/eLife.18167</a></li>
<li>Sakamoto, H., Ariyoshi, T., Kimpara, N., Sugao, K., Taiko, I., Takikawa, K., Asanuma, D., Namiki, S., &amp; Hirose, K. (2018). Synaptic weight set by Munc13-1 supramolecular assemblies. <em>Nature Neuroscience</em>, 21(1), 41–49. <a href="https://doi.org/10.1038/s41593-017-0041-9" target="_blank">doi:10.1038/s41593-017-0041-9</a></li>
<li>Dürst, C. D., Wiegert, J. S., Schulze, C., et al. (2022). Vesicular release probability sets the strength of individual Schaffer collateral synapses. <em>Nature Communications</em>, 13, 6126. <a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">doi:10.1038/s41467-022-33565-6</a></li>
<li>Emperador-Melero, J., Andersen, J. W., Metzbower, S. R., et al. (2024). Distinct active zone protein machineries mediate Ca<sup>2+</sup> channel clustering and vesicle priming at hippocampal synapses. <em>Nature Neuroscience</em>, 27, 1680–1694. <a href="https://doi.org/10.1038/s41593-024-01720-5" target="_blank">doi:10.1038/s41593-024-01720-5</a></li>
<li>Mittermaier, F. X., Kalbhenn, T., Xu, R., et al. (2024). Membrane potential states gate synaptic consolidation in human neocortical tissue. <em>Nature Communications</em>, 15, 10340. <a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">doi:10.1038/s41467-024-53901-2</a></li>
<li>Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. <em>Nature</em>, 429, 761–766. <a href="https://doi.org/10.1038/nature02617" target="_blank">doi:10.1038/nature02617</a></li>
<li>Vardalaki, D., Chung, K., &amp; Harnett, M. T. (2022). Filopodia are a structural substrate for silent synapses in adult neocortex. <em>Nature</em>, 612, 323–327. <a href="https://doi.org/10.1038/s41586-022-05483-6" target="_blank">doi:10.1038/s41586-022-05483-6</a></li>
<li>Pizzorusso, T., Medini, P., Berardi, N., Chierzi, S., Fawcett, J. W., &amp; Maffei, L. (2002). Reactivation of ocular dominance plasticity in the adult visual cortex. <em>Science</em>, 298(5596), 1248–1251. <a href="https://doi.org/10.1126/science.1072699" target="_blank">doi:10.1126/science.1072699</a></li>
<li>Frischknecht, R., Heine, M., Perrais, D., Seidenbecher, C. I., Choquet, D., &amp; Gundelfinger, E. D. (2009). Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. <em>Nature Neuroscience</em>, 12(7), 897–904. <a href="https://doi.org/10.1038/nn.2338" target="_blank">doi:10.1038/nn.2338</a></li>
<li>Gogolla, N., Caroni, P., Lüthi, A., &amp; Herry, C. (2009). Perineuronal nets protect fear memories from erasure. <em>Science</em>, 325(5945), 1258–1261. <a href="https://doi.org/10.1126/science.1174146" target="_blank">doi:10.1126/science.1174146</a></li>
<li>Jabłońska, K., Kaczor, K., Kółeczko, M., et al. (2024). Extracellular matrix integrity regulates GABAergic plasticity in the hippocampus. <em>Matrix Biology</em>, 136, 74–96. <a href="https://doi.org/10.1016/j.matbio.2024.11.001" target="_blank">doi:10.1016/j.matbio.2024.11.001</a></li>
<li>Boonen, M., Hellings, N., Hoedemaekers, T., et al. (2022). Reorganization of the brain extracellular matrix in hippocampal sclerosis. <em>International Journal of Molecular Sciences</em>, 23(15), 8197. <a href="https://doi.org/10.3390/ijms23158197" target="_blank">doi:10.3390/ijms23158197</a></li>
<li>Glykys, J., Dzhala, V., Egawa, K., Balena, T., Saponjian, Y., Kuchibhotla, K. V., Bacskai, B. J., Kahle, K. T., Zeuthen, T., &amp; Staley, K. J. (2014). Local impermeant anions establish the neuronal chloride concentration. <em>Science</em>, 343(6171), 670–675. <a href="https://doi.org/10.1126/science.1245423" target="_blank">doi:10.1126/science.1245423</a></li>
<li>Heubl, M., Zhang, J., Pressey, J. C., Al Awabdh, S., Renner, M., Gomez-Castro, F., Moutkine, I., Eugène, E., Russeau, M., Kahle, K. T., Poncer, J.-C., &amp; Lévi, S. (2017). GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. <em>Nature Communications</em>, 8, 1776. <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">doi:10.1038/s41467-017-01749-0</a></li>
<li>Ding, F., O'Donnell, J., Xu, Q., Kang, N., Goldman, N., &amp; Nedergaard, M. (2016). Changes in the composition of brain interstitial ions control the sleep-wake cycle. <em>Science</em>, 352(6285), 550–555. <a href="https://doi.org/10.1126/science.aad4821" target="_blank">doi:10.1126/science.aad4821</a></li>
<li>Huberfeld, G., Wittner, L., Clemenceau, S., Baulac, M., Kaila, K., Miles, R., &amp; Rivera, C. (2007). Perturbed chloride homeostasis and GABAergic signaling in human temporal lobe epilepsy. <em>Journal of Neuroscience</em>, 27(37), 9866–9873. <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">doi:10.1523/JNEUROSCI.2761-07.2007</a></li>
<li>Simonnet, C., Sinha, M., Goutierre, M., Moutkine, I., Daumas, S., &amp; Poncer, J.-C. (2023). Silencing KCC2 in mouse dorsal hippocampus compromises spatial and contextual memory. <em>Neuropsychopharmacology</em>, 48(7), 1067–1077. <a href="https://doi.org/10.1038/s41386-022-01480-5" target="_blank">doi:10.1038/s41386-022-01480-5</a></li>
<li>Nakamura, K., Moorhouse, A. J., Cheung, D. L., Eto, K., Takeda, I., Rozenbroek, P. W., Inada, H., Housley, G. D., Wake, H., &amp; Nabekura, J. (2019). Overexpression of neuronal K+–Cl− co-transporter enhances dendritic spine plasticity and motor learning. <em>The Journal of Physiological Sciences</em>, 69, 453–463. <a href="https://doi.org/10.1007/s12576-018-00654-5" target="_blank">doi:10.1007/s12576-018-00654-5</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318–322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Seidl, A. H., Rubel, E. W., &amp; Barría, A. (2015). Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. <em>Nature Communications</em>, 6, 8073. <a href="https://doi.org/10.1038/ncomms9073" target="_blank">doi:10.1038/ncomms9073</a></li>
<li>Dutta, D. J., Woo, D. H., Lee, P. R., et al. (2018). Regulation of myelin structure and conduction velocity by perinodal astrocytes. <em>Proceedings of the National Academy of Sciences USA</em>, 115(46), 11832–11837. <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">doi:10.1073/pnas.1811013115</a></li>
<li>Cohen, C. C. H., Popovic, M. A., Klooster, J., et al. (2020). Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. <em>Cell</em>, 180(2), 311–322.e15. <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">doi:10.1016/j.cell.2019.11.039</a></li>
<li>Micheva, K. D., Kiraly, M., Perez, M. M., & Madison, D. V. (2021). Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. <em>Cerebral Cortex</em>, 31(7), 3374–3392. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">doi:10.1093/cercor/bhab018</a></li>
<li>Dubey, S., Kuschmitz, S., Mezey, S. E., et al. (2022). Myelination synchronizes cortical oscillations by consolidating parvalbumin-mediated phasic inhibition. <em>eLife</em>, 11, e73827. <a href="https://doi.org/10.7554/eLife.73827" target="_blank">doi:10.7554/eLife.73827</a></li>
<li>Xin, W., Kaneko, M., Roth, R. H., Zhang, A., Nocera, S., Ding, J. B., Stryker, M. P., &amp; Chan, J. R. (2024). Oligodendrocytes and myelin limit neuronal plasticity in visual cortex. <em>Nature</em>, 633, 856–863. <a href="https://doi.org/10.1038/s41586-024-07853-8" target="_blank">doi:10.1038/s41586-024-07853-8</a></li>
<li>Della-Flora Nunes, G., Osso, L. A., Haynes, J. A., et al. (2025). Incomplete remyelination via therapeutically enhanced oligodendrogenesis is sufficient to recover visual cortical function. <em>Nature Communications</em>, 16, 732. <a href="https://doi.org/10.1038/s41467-025-56092-6" target="_blank">doi:10.1038/s41467-025-56092-6</a></li>
<li>van Blooijs, D., de Haan, A. M., Renaud, S., et al. (2023). Developmental trajectory of transmission speed in the human brain. <em>Nature Neuroscience</em>, 26, 828–838. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">doi:10.1038/s41593-023-01272-0</a></li>
<li>Arshad, M., Stanley, J. A., &amp; Raz, N. (2017). Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T<sub>1</sub>w/T<sub>2</sub>w image ratio. <em>Human Brain Mapping</em>, 38(4), 1780–1790. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/" target="_blank">PMC5342928</a></li>
<li>Hagiwara, A., Hori, M., Kamagata, K., Warntjes, M., Matsuyoshi, D., Nakazawa, M., Ueda, R., Andica, C., Horiuchi, K., Fujita, S., Maekawa, T., Irie, R., Kumamaru, K. K., Abe, O., Aoki, S. (2018). Myelin measurement: Comparison between simultaneous tissue relaxometry, magnetization transfer saturation index, and T1w/T2w ratio methods. <em>Scientific Reports</em>, 8, 10554. <a href="https://doi.org/10.1038/s41598-018-28852-6" target="_blank">doi:10.1038/s41598-018-28852-6</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., et al. (2024). Myelin bilayer mapping in the human brain in vivo. <em>Magnetic Resonance in Medicine</em>, 92(1), 260–273. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Chen, M., Tang, S., Chen, H., Zhou, Z., Rong, P., Lu, H., &amp; Chen, W. (2025). Orientation-independent magnetization transfer imaging of brain white matter. <em>NeuroImage</em>, 309, 121456. <a href="https://doi.org/10.1016/j.neuroimage.2025.121456" target="_blank">doi:10.1016/j.neuroimage.2025.121456</a></li>
<li>Galbusera, R., Weigel, M., Bahn, E., Schaedelin, S., Cagol, A., Lu, P.-J., et al. (2025). Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. <em>Brain Pathology</em>, 35(5), e70010. <a href="https://doi.org/10.1111/bpa.70010" target="_blank">doi:10.1111/bpa.70010</a></li>
<li>Genc, S., Ball, G., Chamberland, M., et al. (2025). MRI signatures of cortical microstructure in human development align with oligodendrocyte cell-type expression. <em>Nature Communications</em>, 16, 3317. <a href="https://doi.org/10.1038/s41467-025-58604-w" target="_blank">doi:10.1038/s41467-025-58604-w</a></li>
<li>Qian, Y., Zhao, T., Zheng, H., Weimer, J., &amp; Boada, F. E. (2012). High-resolution sodium imaging of human brain at 7 T. <em>Magnetic Resonance in Medicine</em>, 68(1), 227–233. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">doi:10.1002/mrm.23225</a></li>
<li>Reimer, J., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Adamsky, A., et al. (2018). Astrocytic activation generates de novo neuronal potentiation and memory enhancement. <em>Nature Neuroscience</em>, 21, 1725–1733. <a href="https://doi.org/10.1038/s41593-018-0253-6" target="_blank">doi:10.1038/s41593-018-0253-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <em>Communications Biology</em>, 7, 1498. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Hardingham, N. R., &amp; Larkman, A. U. (1998). The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. <em>The Journal of Physiology</em>, 507(1), 249–256. <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">doi:10.1111/j.1469-7793.1998.249bu.x</a></li>
<li>Moser, E., Mathiesen, I., &amp; Andersen, P. (1993). Association between brain temperature and dentate field potentials in exploring and swimming rats. <em>Science</em>, 259(5099), 1324–1326. <a href="https://doi.org/10.1126/science.8446900" target="_blank">doi:10.1126/science.8446900</a></li>
<li>Long, M. A., &amp; Fee, M. S. (2008). Using temperature to analyse temporal dynamics in the songbird motor pathway. <em>Nature</em>, 456, 189–194. <a href="https://doi.org/10.1038/nature07448" target="_blank">doi:10.1038/nature07448</a></li>
<li>Reig, R., Mattia, M., Compte, A., Belmonte, C., &amp; Sanchez-Vives, M. V. (2010). Temperature modulation of slow and fast cortical rhythms. <em>Journal of Neurophysiology</em>, 103(3), 1253–1261. <a href="https://doi.org/10.1152/jn.00890.2009" target="_blank">doi:10.1152/jn.00890.2009</a></li>
<li>Van Hook, M. J. (2020). Temperature effects on synaptic transmission and neuronal function in the visual thalamus. <em>PLoS One</em>, 15(4), e0232451. <a href="https://doi.org/10.1371/journal.pone.0232451" target="_blank">doi:10.1371/journal.pone.0232451</a></li>
<li>Owen, S. F., Liu, M. H., &amp; Kreitzer, A. C. (2019). Thermal constraints on in vivo optogenetic manipulations. <em>Nature Neuroscience</em>, 22, 1061–1065. <a href="https://doi.org/10.1038/s41593-019-0422-3" target="_blank">doi:10.1038/s41593-019-0422-3</a></li>
<li>Boorman, L. W., Harris, S. S., Shabir, O., et al. (2023). Bidirectional alterations in brain temperature profoundly modulate spatiotemporal neurovascular responses in-vivo. <em>Communications Biology</em>, 6, 185. <a href="https://doi.org/10.1038/s42003-023-04542-6" target="_blank">doi:10.1038/s42003-023-04542-6</a></li>
<li>Rzechorzek, N. M., Thrippleton, M. J., Chappell, F. M., et al. (2022). A daily temperature rhythm in the human brain predicts survival after brain injury. <em>Brain</em>, 145(6), 2031–2048. <a href="https://doi.org/10.1093/brain/awab466" target="_blank">doi:10.1093/brain/awab466</a></li>
<li>Tan, Y., Liu, W., Li, Y., et al. (2025). Measurement of Healthy Adult Brain Temperature Using <sup>1</sup>H Magnetic Resonance Spectroscopy Thermometry. <em>Clinical Neuroradiology</em>, 35(1), 159–164. <a href="https://doi.org/10.1007/s00062-024-01467-3" target="_blank">doi:10.1007/s00062-024-01467-3</a></li>
<li>Rangaraju, V., Calloway, N., &amp; Ryan, T. A. (2014). Activity-driven local ATP synthesis is required for synaptic function. <em>Cell</em>, 156(4), 825–835. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">doi:10.1016/j.cell.2013.12.042</a></li>
<li>Divakaruni, S. S., Van Dyke, A. M., Chandra, R., et al. (2018). Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. <em>Neuron</em>, 100(4), 860–875.e7. <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">doi:10.1016/j.neuron.2018.09.025</a></li>
<li>Underwood, E. L., Redell, J. B., Hood, K. N., et al. (2023). Enhanced presynaptic mitochondrial energy production is required for memory formation. <em>Scientific Reports</em>, 13, 14431. <a href="https://doi.org/10.1038/s41598-023-40877-0" target="_blank">doi:10.1038/s41598-023-40877-0</a></li>
<li>Hu, H., Tang, J., Wu, Y., et al. (2025). Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. <em>Communications Biology</em>, 8, 166. <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">doi:10.1038/s42003-025-08963-3</a></li>
<li>Vishwanath, A. A., Comyn, T., Mira, R. G., et al. (2026). Mitochondrial Ca<sup>2+</sup> efflux controls neuronal metabolism and long-term memory across species. <em>Nature Metabolism</em>, 8, 467–488. <a href="https://doi.org/10.1038/s42255-026-01451-w" target="_blank">doi:10.1038/s42255-026-01451-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). <sup>31</sup>P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <em>NMR in Biomedicine</em>, 28(11), 1455–1462. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2017). Efficient <sup>31</sup>P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. <em>Magnetic Resonance in Medicine</em>, 78(5), 1657–1666. <a href="https://doi.org/10.1002/mrm.26560" target="_blank">doi:10.1002/mrm.26560</a></li>
<li>Guo, R., Yang, S., Wiesner, H. M., Li, Y., Zhao, Y., Liang, Z.-P., Chen, W., &amp; Zhu, X.-H. (2024). Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. <em>Frontiers in Neuroscience</em>, 18, 1389111. <a href="https://doi.org/10.3389/fnins.2024.1389111" target="_blank">doi:10.3389/fnins.2024.1389111</a></li>
<li>Kaiser, A., Vind, F. A., Duarte, J. M. N., Jelescu, I., Lin, Y., Yu, X., Widmaier, M., Wenz, D., &amp; Xin, L. (2026). Ultra-high field <sup>31</sup>P functional magnetic resonance spectroscopy reveals NAD<sup>+</sup> dynamics in brain energy metabolism during visual stimulation. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>. <a href="https://doi.org/10.1177/0271678X261415784" target="_blank">doi:10.1177/0271678X261415784</a></li>
<li>Karkouri, J., Deelchand, D. K., Van de Moortele, P.-F., et al. (2026). Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. <em>Magnetic Resonance in Medicine</em>. <a href="https://doi.org/10.1002/mrm.70308" target="_blank">doi:10.1002/mrm.70308</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <em>PNAS Nexus</em>, 4(3), pgaf072. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Bell, R. D., Winkler, E. A., Sagare, A. P., et al. (2010). Pericytes control key neurovascular functions and neuronal phenotype in the adult brain and during brain aging. <em>Neuron</em>, 68(3), 409–427. <a href="https://doi.org/10.1016/j.neuron.2010.09.043" target="_blank">doi:10.1016/j.neuron.2010.09.043</a></li>
<li>Kisler, K., Nikolakopoulou, A. M., Sweeney, M. D., et al. (2020). Acute ablation of cortical pericytes leads to rapid neurovascular uncoupling. <em>Frontiers in Cellular Neuroscience</em>, 14, 27. <a href="https://doi.org/10.3389/fncel.2020.00027" target="_blank">doi:10.3389/fncel.2020.00027</a></li>
<li>Pandey, K., Bessières, B., Sheng, S. L., et al. (2023). Neuronal activity drives IGF2 expression from pericytes to form long-term memory. <em>Neuron</em>, 111(23), 3819–3836.e8. <a href="https://doi.org/10.1016/j.neuron.2023.08.030" target="_blank">doi:10.1016/j.neuron.2023.08.030</a></li>
<li>Mai-Morente, S., Razvan, M., Lechuga-Sancho, A. M., et al. (2025). Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. <em>Nature Communications</em>, 16, 5912. <a href="https://doi.org/10.1038/s41467-025-61312-0" target="_blank">doi:10.1038/s41467-025-61312-0</a></li>
<li>Morgan, C. A., Thomas, D. L., Shao, X., et al. (2024). Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. <em>NMR in Biomedicine</em>, 37(12), e5256. <a href="https://doi.org/10.1002/nbm.5256" target="_blank">doi:10.1002/nbm.5256</a></li>
<li>Padrela, B. E., Slivka, M., Sneve, M. H., et al. (2025). Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. <em>Neurobiology of Aging</em>, 147, 176–186. <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">doi:10.1016/j.neurobiolaging.2024.12.012</a></li>
<li>Chung, K. J., Abdelhafez, Y. G., Spencer, B. A., et al. (2025). Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. <em>Nature Communications</em>, 16, 3076. <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">doi:10.1038/s41467-025-58356-7</a></li>
<li>Zhao, L., Taso, M., Dai, W., Press, D. Z., &amp; Alsop, D. C. (2020). Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. <em>Fluids and Barriers of the CNS</em>, 17, 58. <a href="https://doi.org/10.1186/s12987-020-00218-z" target="_blank">doi:10.1186/s12987-020-00218-z</a></li>
<li>Petitclerc, L., Hirschler, L., Wells, J. A., et al. (2021). Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. <em>NeuroImage</em>, 245, 118755. <a href="https://doi.org/10.1016/j.neuroimage.2021.118755" target="_blank">doi:10.1016/j.neuroimage.2021.118755</a></li>
<li>Petitclerc, L., Durrant, H., Hirschler, L., Václavů, L., &amp; van Osch, M. J. P. (2026). Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>. <a href="https://doi.org/10.1177/0271678X261429042" target="_blank">doi:10.1177/0271678X261429042</a></li>
<li>Suzuki, A., Stern, S. A., Bozdagi, O., et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. <em>Cell</em>, 144(5), 810–823. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">doi:10.1016/j.cell.2011.02.018</a></li>
<li>Silva, B., et al. (2022). Glial ketogenesis regulates memory maintenance during starvation. <em>Nature Metabolism</em>, 4, 1534–1547. <a href="https://doi.org/10.1038/s42255-022-00528-6" target="_blank">doi:10.1038/s42255-022-00528-6</a></li>
<li>Qi, G., Mi, Y., Shi, X., Gu, H., Brinton, R. D., &amp; Yin, F. (2021). ApoE4 impairs neuron-astrocyte coupling of fatty acid metabolism. <em>Cell Reports</em>, 34(1), 108572. <a href="https://doi.org/10.1016/j.celrep.2020.108572" target="_blank">doi:10.1016/j.celrep.2020.108572</a></li>
<li>Pavlowsky, A., et al. (2025). Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila. <em>Nature Metabolism</em>, 7, 2467–2483. <a href="https://doi.org/10.1038/s42255-025-01416-5" target="_blank">doi:10.1038/s42255-025-01416-5</a></li>
<li>Greda, A. K., et al. (2025). Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel. <em>Nature Metabolism</em>, 7, 2346–2365. <a href="https://doi.org/10.1038/s42255-025-01389-5" target="_blank">doi:10.1038/s42255-025-01389-5</a></li>
<li>Villemagne, V. L., Harada, R., Dore, V., et al. (2022). First-in-Humans Evaluation of <sup>18</sup>F-SMBT-1, a Novel <sup>18</sup>F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. <em>Journal of Nuclear Medicine</em>, 63(10), 1551–1559. <a href="https://doi.org/10.2967/jnumed.121.263254" target="_blank">doi:10.2967/jnumed.121.263254</a></li>
<li>Matsuoka, K., Takado, Y., Kimura, Y., et al. (2026). Quantification of monoamine oxidase B expression with <sup>11</sup>C-SL25.1188 for imaging reactive astrocytes in patients with Alzheimer's disease. <em>European Journal of Nuclear Medicine and Molecular Imaging</em>, 53, 1142–1156. <a href="https://doi.org/10.1007/s00259-025-07542-2" target="_blank">doi:10.1007/s00259-025-07542-2</a></li>
<li>Tyacke, R. J., Myers, J. F. M., Venkataraman, A., et al. (2018). Evaluation of <sup>11</sup>C-BU99008, a PET Ligand for the Imidazoline<sub>2</sub> Binding Site in Human Brain. <em>Journal of Nuclear Medicine</em>, 59(10), 1597–1602. <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">doi:10.2967/jnumed.118.208009</a></li>
<li>Livingston, N. R., Calsolaro, V., Hinz, R., et al. (2022). Relationship between astrocyte reactivity, using novel <sup>11</sup>C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. <em>Molecular Psychiatry</em>, 27(4), 2019–2029. <a href="https://doi.org/10.1038/s41380-021-01429-y" target="_blank">doi:10.1038/s41380-021-01429-y</a></li>
<li>Jaisa-Aad, M., Muñoz-Castro, C., Healey, M. A., Hyman, B. T., &amp; Serrano-Pozo, A. (2024). Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. <em>Acta Neuropathologica</em>, 147(1), 66. <a href="https://doi.org/10.1007/s00401-024-02712-2" target="_blank">doi:10.1007/s00401-024-02712-2</a></li>
<li>Williamson, N. R., Ferreira, A. N., Watanabe, A. T., et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. <em>Nature</em>, 636, 445–454. <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">doi:10.1038/s41586-024-08170-w</a></li>
<li>Dewa, K., Kwon, O.-B., Zheng, X., et al. (2025). The astrocytic ensemble acts as a multiday trace to stabilize memory. <em>Nature</em>, 648, 99–107. <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">doi:10.1038/s41586-025-09619-2</a></li>
<li>Bukalo, O., et al. (2026). Astrocytes enable amygdala neural representations supporting memory. <em>Nature</em>. <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">doi:10.1038/s41586-025-10068-0</a></li>
<li>Louveau, A., Smirnov, I., Keyes, T. J., et al. (2015). Structural and functional features of central nervous system lymphatic vessels. <em>Nature</em>, 523, 337–341. <a href="https://doi.org/10.1038/nature14432" target="_blank">doi:10.1038/nature14432</a></li>
<li>Ahn, J. H., Cho, H., Kim, J.-H., et al. (2019). Meningeal lymphatic vessels at the skull base drain cerebrospinal fluid. <em>Nature</em>, 572, 62–66. <a href="https://doi.org/10.1038/s41586-019-1419-5" target="_blank">doi:10.1038/s41586-019-1419-5</a></li>
<li>Kim, J., et al. (2025). Meningeal lymphatics-microglia axis regulates synaptic physiology. <em>Cell</em>, 188(8), 2129–2148.e21. <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">doi:10.1016/j.cell.2025.02.022</a></li>
<li>Eide, P. K., &amp; Ringstad, G. (2021). Sleep deprivation impairs molecular clearance from the human brain. <em>Brain</em>, 144(3), 863–874. <a href="https://doi.org/10.1093/brain/awaa443" target="_blank">doi:10.1093/brain/awaa443</a></li>
<li>Fultz, N. E., Bonmassar, G., Setsompop, K., et al. (2019). Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. <em>Science</em>. <a href="https://doi.org/10.1126/science.aax5440" target="_blank">doi:10.1126/science.aax5440</a></li>
<li>Kim, D., Huang, Y., &amp; Liu, J. (2025). Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. <em>NeuroImage</em>. <a href="https://doi.org/10.1016/j.neuroimage.2025.121142" target="_blank">doi:10.1016/j.neuroimage.2025.121142</a></li>
<li>Eide, P. K., Lashkarivand, A., Pripp, A., et al. (2023). Plasma neurodegeneration biomarker concentrations associate with glymphatic and meningeal lymphatic measures in neurological disorders. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-023-37685-5" target="_blank">doi:10.1038/s41467-023-37685-5</a></li>
<li>Hirschler, L., Runderkamp, B. A., Decker, A., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., Elbert, D. L., Giovangrandi, L., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <em>Nature Communications</em>, 17, 715. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE basics →</a></li>
<li><a href="homeostatic-plasticity-and-maintenance-state.html">Homeostatic plasticity and maintenance state →</a></li>
<li><a href="decode-vs-emulate.html">Decode and Emulate →</a></li>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../wbe_101.html">Introduction to WBE →</a></li>
<li><a href="../verification.html#state-completeness-gate">State variable integrity gate →</a></li>
<li><a href="../tech_roadmap.html#qa-r10">R10 neuromodification →</a></li>
</ul>
</div>
</aside>
</main>
