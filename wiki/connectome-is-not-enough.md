---
layout: default
title: 'Wiki: Why wiring diagrams alone are not enough'
description: We will summarize the reasons why storing only the connectome in WBE
  is insufficient, including the lack of state variables and the limitations of connectome-constrained
  estimation, based on primary literature.
article_type: Wiki
subtitle: connectome-complete is not emulation-complete
author: Mind Uploading Research Project
last_updated: '2026-03-18'
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
  6 state classes and 1 presumed wall.
- Use only primary literature to separate missing state variables from parameter degeneracy.
- We will also fix operational rules for how to read connectome-complete and connectome-constrained
  model on this site.
- Rather than ending with enumeration, we use augmentation/ablation to fix what should
  be added from connectome-only to read the predictive gain.
- "Timing-state is treated as more than a single delay constant: node/internode geometry,
  periaxonal structure, astrocyte control, and human macro timing proxies are read separately."
known_points:
- Great progress has been made in creating a whole-brain connectome, but this alone
  does not mean that dynamic reproduction is complete.
- Synaptic efficiency, latency, neuromodification, glia, cell type labels, and intrinsic
  excitability/homeostasis set points are pieces of information that are likely to
  fall off a static edge list.
- Confusing coarse physiological proxies with ground truths makes it easy to overstate
  claims about internal states.
- Even in a connectome-constrained model, dynamics can degenerate if unmeasured cell/synapse/modification
  parameters remain.
- Conditional predictions can be improved by adding same-brain function, transcriptomics,
  neuromodulatory dynamics, and glial slow state, but the improvement depends on the
  task, time constant, and external validation conditions.
- Device latency audit and biological timing-state audit are different requirements; passing
  one does not automatically pass the other.
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
Although wiring diagrams are an important foundation for WBE,<strong>alone are not the minimum requirement for dynamic reproduction</strong>. Even within the same adjacency relationship, differences in cell type labeling, intrinsic excitability, synaptic efficiency, conduction delay, neuronal modification, and glial connectivity state can significantly alter learning, phase synchronization, arousal-dependent responses, and long-term stability. Furthermore, connectome-constrained modeling research in 2024-2025 showed that even with the inclusion of wiring constraints, degeneracy in dynamics remains due to unmeasured parameters and omitted mechanisms. Therefore, this site treats<strong>connectome-complete as a structural atlas/scaffold achievement</strong> and not as<strong>emulation-complete</strong>. Similarly, the fact that a<strong>connectome-constrained model reproduced some activities</strong> cannot be read as state-complete reconstruction.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. From only the aspects of technology and natural science, we will clarify ``what state variables are missing and what cannot be claimed?'' and ``what cannot be uniquely determined even if wiring constraints are included.''
</p>
</div>

<section class="section" id="bottom-line">
<h2 class="section-title">6 state classes and 1 putative wall to fix first</h2>
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
<td><strong>Intrinsic excitability/homeostasis set point</strong></td>
<td>Even with the same cell type and graph, if the target values ​​for ion channel expression, threshold, gain, and firing rate are different, the response and recovery method to the same input will change. </td>
<td>The long-term dynamics are largely determined by cell-type labels and short activity matches. </td>
<td>Unless you're measuring threshold / gain / recovery / homeostatic controller, keep claims about long-term stability or memory allocation with latent state. </td>
</tr>
<tr>
<td><strong>Synaptic efficiency/short-term state</strong></td>
<td>The presence or absence of edges alone cannot determine weights, release probability, short-term plasticity, and LTP/LTD history. </td>
<td>Edge count and synapse count can be read as effective weight. </td>
<td>Although it is possible to describe static wiring, it does not claim L2 intervention prediction or L3 closed-loop stability. </td>
</tr>
<tr>
<td><strong>Delay / timing-state</strong></td>
<td>Even with the same graph, differences in myelin thickness, node/internode geometry, or periaxonal structure can change conduction speed and spike-arrival timing. </td>
<td>If the graph is the same, timing can be absorbed into a single constant. </td>
<td>Demote phase, synchrony, and closed-loop claims unless timing-state is measured, externally calibrated, or explicitly left latent. </td>
</tr>
<tr>
<td><strong>Neural modification field</strong></td>
<td>Arousal level, learning rate, and gain adjustment cannot be restored with static wiring alone, and pupil diameter and HRV remain as rough proxies. </td>
<td>pupil / HRV or global arousal can be read as a single transmitter ground truth. </td>
<td>It can be used for covariates and stratification in human data, but it is not written as transmitter-specific or region-specific ground truth. </td>
</tr>
<tr>
<td><strong>Glial-metabolic coupling status</strong></td>
<td>Astrocytes are causally involved in plasticity and memory retrieval, and are not just supporting tissues. </td>
<td>Glia is support tissue, so it can be postponed. </td>
<td>We weaken claims involving long-term plasticity and slow states, and clearly state what approximations should be discarded as the scope of applicability. </td>
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
In addition to the previous 5 classes, the 2026-03 re-audit included <strong>intrinsic excitability/homeostasis set point</strong> as an independent class. The reason is that even if we have cell-type labels and connectomes, long-term prediction and perturbation recovery are still unclear if the threshold, gain, return destination of firing rate, and maintenance mechanism under molecular turnover are different. A comprehensive arrangement of primary literature is divided into <a href="homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>.
</p>
</div>
</section>

<section class="section" id="connectome-progress">
<h2 class="section-title">Wiring diagram research has made great progress, but it is not the end in itself</h2>
<p>
Dorkenwald et al. showed a wiring diagram of the adult Drosophila whole brain and presented a whole brain connectome with a scale of approximately 130,000 neurons. Meanwhile, the MICrONS Consortium has released a dataset and local functional digital twin that links functional measurements and connectomics in the same individual at the cubic millimeter scale of the mouse visual cortex. Furthermore, Lappalainen et al. trained a connectome-constrained network in the Drosophila visual system to be task-optimized, making it possible to predict a wide range of activities. This is a huge step forward, but on the other hand, we are only now at the stage where we are finally starting to connect "wiring + some functions + additional assumptions", and it also shows that dynamic reproduction of the whole brain and all states is still a different problem.
</p>
<div class="note-box">
<strong>Replace here</strong>
<p>
connectome-complete is important in the sense that we have a pretty good idea of what is connected. However, this alone does not fix ``with what strength,'' ``with what delay,'' ``in which neuromodulatory context,'' and ``under which glial coupling.'' Furthermore, even in Lappalainen et al.'s reductionist model, the authors themselves exclude electrical synapses, nonlinear chemical synapses, and neuromodulation. Therefore, this site treats connectome-complete as an achievement of <strong>structural atlas / scaffold</strong> and does not automatically promote it to L2/L3 emulation claim. <strong>Activity prediction by connectome-constrained</strong> can also be read as a hypothesis engine and a conditional model.
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

<section class="section" id="state-classes">
<h2 class="section-title">Why are these 6 classes easy to skip</h2>

<h3>1. Cell type labels are not decorations for node IDs</h3>
<p>
Gamlin et al. showed that connectivity motifs, synaptic properties, and myelination differ systematically among predicted Sst transcriptomic types in mouse visual cortex. Furthermore, the MICrONS Consortium emphasized that in the mammalian cortex, cells of different cell types may contain neurons with different tuning preferences, so it is necessary to read same-brain connectivity and same-brain function together. In other words, even if the graph structure is the same, the physical meaning of the circuit changes if the node label and same-brain physiology are different. An unlabeled graph with a reduced cell type may be convenient for compression, but it loses a lot of the information required to reproduce the function.
</p>

<h3>2. Intrinsic excitability and homeostasis set point is not a byproduct of node label</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> showed that the morpho-electric phenotype spreads continuously even within the same transcriptomic type. Furthermore, <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> showed that even among identified neurons, there are large individual differences in ion channel mRNA and current amount, and <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> modeled how activity-dependent channel expressions can yield activity set points. Furthermore, <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> have shown that a firing-rate set point exists for each single neuron in vivo. In other words,<strong>even if the cell-type label and graph are known, the return destination after threshold, gain, rebound, and perturbation can still remain as latent state</strong>.
</p>

<h3>3. Synapses are not binary edges</h3>
<p>
Holler et al. analyzed the ultrastructure and release properties of neocortical synapses, and showed that transmission properties cannot be expressed simply by "connected/not connected." Matsuzaki et al. demonstrated that spine enlargement and AMPA current increases are linked in LTP induction in a single dendritic spine. Furthermore, Vardalaki et al. showed that even in the adult neocortex, approximately 25% of filopodia can serve as the structural basis for silent synapse lacking AMPA receptors. Therefore, <strong>edge list alone will reduce the weight of the current state, plastic history, and whether it is functionally active in the first place</strong>.
</p>

<h3>4. Delay and myelin are part of timing</h3>
<p>
<a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a> showed that neuronal activity promotes oligodendrogenesis and adaptive myelination, and <a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. (2014)</a> showed that active central myelination is required for motor-skill learning. But the weakness of the earlier page was that it still allowed the reader to compress this into the slogan "more myelin, faster signal." Primary literature now supports a stronger statement: <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a> showed that node and internode geometry is tuned along auditory axons to adjust action-potential timing, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a> showed that perinodal astrocytes can reversibly alter nodal gap length and myelin structure to change conduction velocity and spike arrival, and <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a> showed that saltatory conduction depends on a conductive periaxonal nanocircuit rather than on a single scalar delay term.
</p>
<p>
This matters for WBE because timing-sensitive circuits do not only depend on "who connects to whom," but also on <strong>when inhibition, synchrony, and phase-locked drive arrive</strong>. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">Micheva et al. (2021)</a> showed that even locally projecting PV interneurons gain physiologically relevant conduction-speed differences with axonal myelination, and <a href="https://doi.org/10.7554/eLife.73827" target="_blank">Dubey et al. (2022)</a> linked loss of PV-axon myelination to weakened fast inhibition and failure of gamma synchronization. Therefore, if timing matters, the missing variable is better described as <strong>timing-state</strong> rather than simply "delay."
</p>
<div class="note-box">
<strong>Human observability ceiling for timing-state</strong>
<p>
<a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">van Blooijs et al. (2023)</a> showed that transmission speed in the human brain follows a developmental trajectory, which is useful evidence that conduction timing is biologically variable at the tract scale. But this is still a macro timing proxy, not a cell-specific readout of node length, periaxonal space, oligodendrocyte state, or local inhibitory arrival time. On this site, human myelin or tract-speed readouts are therefore treated as macro support for timing-state, not as ground truth of per-axon conduction state.
</p>
</div>

<h3>5. Neuromodulation is not “one mood scalar”</h3>
<p>
Reimer et al. showed that pupil fluctuations track both adrenergic and cholinergic activity within the cortex. Conversely, this also means that<strong>pupil diameter does not uniquely represent one transmitter state or the other</strong>. Additionally, Neyhart et al. showed that while cortical ACh is highly predictable from cholinergic axon activity and behavioral state, it also has locality that depends on distance from neighboring axons and clearance kinetics. Therefore, although it is useful to use pupil diameter or HRV in humans, it is an overstatement to consider it as the ground truth of transmitter-specific and region-specific internal states. What is necessary is not only to say whether it is a good proxy or not, but also to specify what it is and what it is not.
</p>

<h3>6. Glia is not an afterthought auxiliary variable</h3>
<p>
Adamsky et al. showed that astrocytic activation can produce de novo neuronal potentiation and memory enhancement. Cahill et al. reported that local, instantaneous neurotransmitter inputs are encoded into responses of a broad astrocyte network over minutes. Therefore, a model that ignores glia should be treated as a model that partially lacks plasticity and slow network state. What is important here is not to generalize that glia are also involved, but to clarify in the model specifications <strong>Which time constants and which state variables were discarded</strong>.
</p>
</section>

<section class="section" id="augmentation-ablation">
<h2 class="section-title">Don't end with enumeration, compare with augmentation / ablation</h2>
<p>
The weakness of the current site was that even if it was possible to enumerate the missing state variables, it did not bring to the fore what additional information and which error terms could be reduced to advance to a stronger claim. Primary literature from 2024-2026 shows that when you add same-brain function, transcriptomic label, local transmitter dynamics, glial slow state, and recovery log from the connectome-only baseline, the improvement is different. Therefore, on this site, instead of counting state variables as "present/absent," we will compare held-out predictive gain using augmentation/ablation.
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
<td>MICrONS connects dense neural activity, EM connectome, pupil diameter, and locomotion in the same mouse, creating a scaffold that allows comparison of structure and state-dependent function within the same brain. </td>
<td>This is an advancement in a specific task or specific state of the mouse visual cortex, and does not guarantee generalization to the whole brain or all states or the sufficiency of the hidden state. </td>
</tr>
<tr>
<td><strong>+ transcriptomic / cell-type label</strong></td>
<td>transcriptomic type and target specificity with same-brain or proximity conditions. </td>
<td>Gamlin et al. demonstrated that connectivity motifs, synaptic properties, and myelination differ systematically among predicted Sst transcriptomic types, embodying the incremental value of node labels. </td>
<td>Within-type heterogeneity and morpho-electric variability remain, so even if you add cell-type label, threshold / gain / set point will still be latent. </td>
</tr>
<tr>
<td><strong>+ timing-state / conduction audit</strong></td>
<td>Compare a fixed-delay baseline against a model or analysis that adds measured or externally calibrated timing variables under the same held-out conditions. </td>
<td>Seidl, Dutta, Cohen, Micheva, and Dubey together support that timing-sensitive prediction can improve when node/internode structure, periaxonal coupling, or myelination-linked local speed are treated explicitly. </td>
<td>Human myelin maps or tract-scale transmission-speed estimates remain macro proxies; without external calibration they do not become per-axon timing ground truth. </td>
</tr>
<tr>
<td><strong>+ local transmitter dynamics</strong></td>
<td>Local cholinergic axon activity or behavior-linked transmitter proxy. </td>
<td>Neyhart et al. showed that while cortical ACh dynamics can be fairly predicted from cholinergic axon activity and behavioral state, locality changes with distance from neighboring axons and clearance kinetics. </td>
<td>pupil / behavior / global arousal is still a coarse proxy and cannot be automatically promoted to transmitter-specific or region-specific ground truth. </td>
</tr>
<tr>
<td><strong>+ glial / slow-state</strong></td>
<td>Astrocyte network state, microglia / synaptic-density changes, slow response on the order of minutes. </td>
<td>Cahill et al. showed that local transient neurotransmitter inputs are minute-long encoded in broad cortical astrocyte networks, and Vadisiute et al. showed that astrocyte, microglia, and synaptic densities change rapidly after acute chemogenetic manipulation. </td>
<td>The contribution of the slow state depends on cell type, task, and species differences, and adding it up will not immediately lead to whole-brain emulation. </td>
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
<li><strong>augmentation / ablation:</strong>You can't write that "the added state variable worked" without putting a connectome-only baseline. </li>
<li><strong>intrinsic excitability / homeostatic set point:</strong>Do not automatically infer from cell-type label or short-term activity matching. If not measured, write latent state. </li>
<li><strong>Delay is not one scalar:</strong>If timing matters, separate device latency, biological timing-state, and phase error; if the biological side is not measured, write timing-state as latent. </li>
<li><strong>pupil / HRV:</strong> A useful state covariate for human data, but not a transmitter-specific ground truth. </li>
<li><strong>When state variable is missing:</strong>If estimated, specify the error and abstention condition; if not, specify absent. </li>
<li>When there are no weights / timing-state: phase, timing, intervention response, and closed-loop stability claims are demoted. </li>
<li><strong>When dropping glia / neuromodulation:</strong>Write in the text what behavior was discarded in the approximation as the scope of application. </li>
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
<td><strong>Conditional dynamical claim</strong></td>
<td>Include same-brain function or perturbation, list of missing state variables, proxy limits, family/uncertainty, and absence of intrinsic excitability/homeostatic set point if not measured. </td>
</tr>
<tr>
<td><strong>Intervention/Closed Loop claim</strong></td>
<td>In addition to the above, we will also publish calibration routes for weights / timing-state / neuromodulation / excitability-homeostasis, external validation, and abstention / stop conditions. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <em>Nature</em>, 634, 1132–1140. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 2561–2574. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497–505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Holler, S., et al. (2021). Structure and function of a neocortical synapse. <em>Nature</em>, 591, 111–116. <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">doi:10.1038/s41586-020-03134-2</a></li>
<li>Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. <em>Nature</em>, 429, 761–766. <a href="https://doi.org/10.1038/nature02617" target="_blank">doi:10.1038/nature02617</a></li>
<li>Vardalaki, D., Chung, K., &amp; Harnett, M. T. (2022). Filopodia are a structural substrate for silent synapses in adult neocortex. <em>Nature</em>, 612, 323–327. <a href="https://doi.org/10.1038/s41586-022-05483-6" target="_blank">doi:10.1038/s41586-022-05483-6</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318–322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Seidl, A. H., Rubel, E. W., &amp; Barría, A. (2015). Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. <em>Nature Communications</em>, 6, 8073. <a href="https://doi.org/10.1038/ncomms9073" target="_blank">doi:10.1038/ncomms9073</a></li>
<li>Dutta, D. J., Woo, D. H., Lee, P. R., et al. (2018). Regulation of myelin structure and conduction velocity by perinodal astrocytes. <em>Proceedings of the National Academy of Sciences USA</em>, 115(46), 11832–11837. <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">doi:10.1073/pnas.1811013115</a></li>
<li>Cohen, C. C. H., Popovic, M. A., Klooster, J., et al. (2020). Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. <em>Cell</em>, 180(2), 311–322.e15. <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">doi:10.1016/j.cell.2019.11.039</a></li>
<li>Micheva, K. D., Kiraly, M., Perez, M. M., & Madison, D. V. (2021). Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. <em>Cerebral Cortex</em>, 31(7), 3374–3392. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">doi:10.1093/cercor/bhab018</a></li>
<li>Dubey, S., Kuschmitz, S., Mezey, S. E., et al. (2022). Myelination synchronizes cortical oscillations by consolidating parvalbumin-mediated phasic inhibition. <em>eLife</em>, 11, e73827. <a href="https://doi.org/10.7554/eLife.73827" target="_blank">doi:10.7554/eLife.73827</a></li>
<li>van Blooijs, D., de Haan, A. M., Renaud, S., et al. (2023). Developmental trajectory of transmission speed in the human brain. <em>Nature Neuroscience</em>, 26, 828–838. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">doi:10.1038/s41593-023-01272-0</a></li>
<li>Reimer, J., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Adamsky, A., et al. (2018). Astrocytic activation generates de novo neuronal potentiation and memory enhancement. <em>Nature Neuroscience</em>, 21, 1725–1733. <a href="https://doi.org/10.1038/s41593-018-0253-6" target="_blank">doi:10.1038/s41593-018-0253-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <em>Communications Biology</em>, 7, 1498. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
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
