# Wiki: Why wiring diagrams alone are not enough

> connectome-complete is not emulation-complete
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-19 / 位置づけ: Technical / natural science only

## このページの役割
This page is a page to analyze the intuition that ``If we can obtain the connectome, it would be sufficient to reproduce the brain'' based on primary literature. Rather than focusing on philosophy or legal systems, I will focus on what state variables can't be said if they are missing, and what putative barriers remain even in connectome-constrained.

## 正確さの前提
What I'm showing here is an arrangement of ``at least removing this will weaken the argument'' and ``degeneracy that remains even if wiring constraints are included'', and does not mean that the final sufficient condition has been determined.

## 公開ページへ戻る
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [technology roadmap](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - Let's organize the overall picture that forms the premise of this argument from the beginning.
- [Wiki: Homeostatic plasticity and maintenance state](https://github.com/yasufumi-nakata/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state) - We take a deep dive into why intrinsic excitability, sleep-homeostasis, and myelin/metabolic maintenance are separate variables.
- [Wiki: Decode and Emulate](https://github.com/yasufumi-nakata/mind-upload/wiki/decode-vs-emulate) - Sort out the differences between output translation and internal generation.
- [Wiki: How to read claims and evidence](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - You can check how much evidence and how strong a claim is allowed.

## いま分かっていること
- Great progress has been made in creating a whole-brain connectome, but this alone does not mean that dynamic reproduction is complete.
- Synaptic efficiency, activity-dependent transcription / chromatin state, latency, ionic milieu / chloride homeostasis, shared extracellular / electrical state, neuromodification, glia, cell type labels, intrinsic excitability/homeostasis set points, and local proteostasis / synaptic-tagging state are pieces of information that are likely to fall off a static edge list, and perisynaptic ECM / PNN state is another.
- Confusing coarse physiological proxies with ground truths makes it easy to overstate claims about internal states.
- Even in a connectome-constrained model, dynamics can degenerate if unmeasured cell/synapse/modification parameters remain.
- Dorkenwald et al. (2024), MICrONS Consortium et al. (2025), Thomas et al. (2014), Donahue et al. (2016), Schilling et al. (2020), Grisot et al. (2021), Lappalainen et al. (2024), and Beiran & Litwin-Kumar (2025) support different kinds of progress and should not be collapsed into one story that connectome is "almost enough."
- Conditional predictions can be improved by adding same-brain function, transcriptomics, neuromodulatory dynamics, and glial slow state, but the improvement depends on the task, time constant, and external validation conditions.
- Device latency audit and biological timing-state audit are different requirements; passing one does not automatically pass the other.

## まだ分かっていないこと
- It is unclear which state class and resolution should be taken to approach the sufficient condition for WBE.
- The extent to which missing state variables can be compensated for by estimation or coarse-graining is an issue for future verification.
- It is not yet fixed which animal/invasive system should be used to calibrate conditions that cannot be directly obtained in humans, including cell-specific timing-state.
- It has not yet been systematically determined to what extent degeneracy can be resolved when adding same-brain functions.
- Which order of augmentations most efficiently reduces which error terms still varies from dataset to dataset.

---

<h2>Conclusion</h2>
<p>
Although wiring diagrams are an important foundation for WBE,<strong>alone are not the minimum requirement for dynamic reproduction</strong>. Even within the same adjacency relationship, differences in cell type labeling, activity-dependent transcription / chromatin program, intrinsic excitability, synaptic efficiency, local proteostasis / synaptic-tagging route, perisynaptic ECM / PNN organization, ionic milieu / chloride homeostasis, shared extracellular / electrical state, conduction delay, neuronal modification, and glial connectivity state can significantly alter learning, phase synchronization, arousal-dependent responses, inhibitory sign, and long-term stability. Furthermore, connectome-constrained modeling research in 2024-2025 showed that even with the inclusion of wiring constraints, degeneracy in dynamics remains due to unmeasured parameters and omitted mechanisms. Therefore, this site treats<strong>connectome-complete as a structural atlas/scaffold achievement</strong> and not as<strong>emulation-complete</strong>. Similarly, the fact that a<strong>connectome-constrained model reproduced some activities</strong> cannot be read as state-complete reconstruction. This warning becomes even stronger when the word <strong>connectome</strong> refers only to a diffusion-MRI-derived human tractography product, because current validation literature supports that object as a macro pathway prior rather than a synapse-resolved edge list.
</p>

<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. From only the aspects of technology and natural science, we will clarify ``what state variables are missing and what cannot be claimed?'' and ``what cannot be uniquely determined even if wiring constraints are included.''
</p>

<h2>11 state classes and 1 putative wall to fix first</h2>
<table>
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
<td>Even with the same graph and cell-type label, allocation eligibility, late memory-stabilization programs, and locus-specific plasticity rules can still change over hours to weeks. </td>
<td>A cell atlas or one-shot DEG list means that the current plasticity-competent program is already fixed. </td>
<td>Treat static transcriptomic labels as identity priors; keep memory-stabilization controller explicit as latent unless temporal or causal evidence is shown. </td>
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
<td><strong>Local proteostasis / synaptic-tagging state</strong></td>
<td>Even with the same graph and current weights, tagged spines and branches can still differ in PRP capture, translation/degradation balance, and late-stabilization persistence. </td>
<td>If the current weight is estimated, the late-stabilization route is also basically fixed. </td>
<td>Unless the tag/capture/proteostasis route is measured, perturbed, or externally calibrated, keep late stabilization and reconsolidation claims as latent state. </td>
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

<strong>Missing variables added this time</strong>
<p>
The March 2026 re-audits first split <strong>intrinsic excitability / homeostasis set point</strong> from cell-type labels and <strong>perisynaptic ECM / PNN state</strong> from synaptic state. This pass adds not only <strong>activity-dependent transcription / chromatin state</strong>, <strong>local proteostasis / synaptic-tagging state</strong>, but also <strong>ionic milieu / chloride homeostasis</strong> as independent classes. The reason is that even if we have cell-type labels, synapse counts, connectomes, and a weight estimate, allocation eligibility, late memory-stabilization programs, branch-local capture routes, and even inhibitory sign can still vary. A more detailed arrangement of these maintenance-side variables is collected in <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state">Wiki: Homeostatic plasticity and maintenance state</a>.
</p>

<h2>Wiring diagram research has made great progress, but it is not the end in itself</h2>
<p>
Dorkenwald et al. (2024), MICrONS Consortium et al. (2025), the tractography-validation literature from Thomas et al. (2014), Reveley et al. (2015), Donahue et al. (2016), Maier-Hein et al. (2017), Schilling et al. (2020), and Grisot et al. (2021), Lappalainen et al. (2024), and Beiran &amp; Litwin-Kumar (2025) changed the connectome discussion qualitatively. However, they did not all solve the same problem. The first gave a whole-adult-brain wiring atlas in fly, the second co-registered function and ultrastructure within one awake mouse visual-cortex volume, the tractography papers showed what can and cannot be inferred about long-range pathways from diffusion-MRI orientation data, the next showed that a connectome-constrained and task-optimized model can predict rich activity in a fly visual subsystem, and the last showed theoretically that a connectome often still does not uniquely determine recurrent dynamics when biophysical parameters remain uncertain. Therefore, the correct reading is not “the connectome is nearly enough,” but rather that <strong>different papers remove different uncertainties while leaving other uncertainties intact</strong>.
</p>

<strong>How this site now reads “connectome progress”</strong>
<p>
On this site, connectome-related progress is now separated into five evidence classes before any WBE claim is read: <strong>(1) wiring atlas</strong>, <strong>(2) same-brain local structure-function scaffold</strong>, <strong>(3) human macro pathway prior / tractography connectome</strong>, <strong>(4) connectome-constrained conditional predictor</strong>, and <strong>(5) identifiability / degeneracy audit</strong>. Collapsing these into one slogan such as “the connectome is almost enough” is too weak, because each class answers a different question and leaves a different ceiling in place.
</p>

<table>
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
<td>MICrONS Consortium et al. (2025)</td>
<td>Dense calcium imaging of about 75,000 neurons in multiple mouse visual areas co-registered with an EM reconstruction of more than 200,000 cells and 0.5 billion synapses in the same awake mouse.</td>
<td>Whole-brain or all-state coverage, general human observability, or proof that local co-registration exhausts hidden-state variables.</td>
<td>Read as a <strong>same-brain local digital-twin scaffold</strong> for visual-cortex questions, not as a state-complete whole-brain template.</td>
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

<strong>Operational rule added here</strong>
<p>
When a paper says that “connectome progress” moves WBE forward, this site now asks <strong>which of the five evidence classes improved</strong>. A stronger claim requires not just more structure, but a narrower remaining latent-state family under the same held-out or perturbed condition.
</p>

<h2>Human diffusion-MRI connectome is still a macro pathway prior</h2>
<p>
The earlier version of this site was already strong at saying that a connectome is not state-complete, but it still left one practical ambiguity too open: <strong>what if the “connectome” itself is a diffusion-MRI tractography product from a living human brain?</strong> Primary validation literature does not support reading that object as a synapse-resolved or edge-complete graph. <a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">Thomas et al. (2014)</a> showed that even exceptional ex vivo macaque diffusion data did not yield high anatomical accuracy across tractography methods, with sensitivity/specificity trade-offs that changed by pathway. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">Reveley et al. (2015)</a> showed that superficial white matter can block long-range tracking from roughly half of the cortical surface. <a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">Donahue et al. (2016)</a> found useful but clearly incomplete predictive power for corticocortical connection strength relative to tracer data. <a href="https://doi.org/10.1038/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017)</a> showed in an open tractography challenge that most submissions recovered many invalid bundles, with 64% of systematically recovered bundles absent from the ground truth. <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">Schilling et al. (2020)</a> then showed that high anatomical accuracy is possible mainly when strong start / end / exclusion priors are supplied, and <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">Grisot et al. (2021)</a> localized recurring same-brain errors at branching and turning configurations that are not fixed simply by higher q-space sampling.
</p>

<strong>Site rule for tractography-derived connectomes</strong>
<p>
On this site, a diffusion-MRI-derived human connectome is read as an <strong>algorithm- and resolution-conditioned macro pathway prior</strong> or <strong>targeted bundle hypothesis route</strong>. It can strengthen statements about major white-matter organization, parcel-level pathway likelihood, or bundle-specific anatomical hypotheses. It does <strong>not</strong> become a synapse-resolved edge list, a direction-complete cortical graph, or proof that the living human connectome is already close to WBE-ready capture.
</p>

<h3>Tractography connectomes need a route card</h3>
<p>
The earlier wording on this site said "macro pathway prior," which was directionally correct, but still too permissive in practice. It left room for readers to treat any tractography-derived connectome as a stable graph once a modern pipeline had been applied. The newer primary literature argues against that shortcut. <a href="https://doi.org/10.1016/j.neuroimage.2023.120376" target="_blank">Sarwar et al. (2023)</a> showed that filtering improves simple tubular bundles much more than complex brain-like architectures, <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">He et al. (2024)</a> showed that tractography filtering can significantly change laterality indices for more than 10% of connections, <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">McMaster et al. (2025)</a> showed that voxel resolution changes the resulting connectome and recommended resampling to 1 mm isotropic for robust comparisons, <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">Manzano-Patrón et al. (2025)</a> showed that fibre-orientation uncertainty can be propagated into tractography rather than hidden, and <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">Zhu et al. (2025)</a> improved whole-brain reconstruction by fusing MRI with microscopy. That combination of results means that on this site the phrase <strong>human tractography connectome</strong> is not one object. It is an <strong>acquisition- and reconstruction-conditioned estimate</strong>.
</p>
<table>
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
<td>Write voxel size, shell / b-value scheme, orientation model, and state explicitly that the direct observable is diffusion signal / local fibre-orientation estimate rather than synapse identity, direction, or weight.</td>
<td>Otherwise a streamline graph is misread as if the edges themselves had been directly observed.</td>
</tr>
<tr>
<td><strong>Priors and post-processing</strong></td>
<td>Write seeding rule, deterministic / probabilistic mode, start / end / exclusion ROIs, atlas constraints, stopping rules, and filtering / weighting method.</td>
<td>Otherwise prior-driven bundle recovery is silently rephrased as unbiased graph discovery.</td>
</tr>
<tr>
<td><strong>Instability and uncertainty</strong></td>
<td>Report scan-rescan or ensemble stability, posterior / bootstrap uncertainty, and sensitivity to voxel size or filtering for the headline graph metric.</td>
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

<strong>Operational rule added in this pass</strong>
<p>
If a tractography-derived connectome claim lacks this route card, this site does not read it as a connectome-complete result. The default ceiling stays at <strong>macro pathway prior / targeted bundle hypothesis</strong>. The burden of proof is on the paper to show which part of the pipeline created the claim and which part has been externally calibrated.
</p>

<h2>Easy to overlook problem 0: Even if the wiring is known, the dynamics are still degenerate</h2>
<p>
Previous versions of this page primarily explained "what state variables fall off the edge list." However, a theoretical study by Beiran and Litwin-Kumar in 2025 showed that even if a connectome is provided, recurrent dynamics often become highly degenerate if unmeasured cell and synaptic properties remain. Even if the student model and teacher model share the same synaptic weights, the dynamics of unobserved neurons can deviate significantly if the biophysical parameters are different. In other words, the missing variable is not ``auxiliary information that can be added later'', but is the main body that determines how uniquely it can be estimated.
</p>

<strong>What this criticism means</strong>
<p>
Even if there is only a wiring diagram, the only solution for the internal state is still far away. Adding same-brain function or perturbation will reduce degeneracy, but unless the remaining family is made public, it cannot be said that ``this internal state is correct.'' Therefore, on this site, <strong>there is a graph</strong>, <strong>activity is partially correct</strong>, and <strong>the internal state is nearly unique</strong> are treated as different claims.
</p>

<h2>Why are these 11 classes easy to skip</h2>

<h3>1. Cell type labels are not decorations for node IDs</h3>
<p>
Gamlin et al. showed that connectivity motifs, synaptic properties, and myelination differ systematically among predicted Sst transcriptomic types in mouse visual cortex. Furthermore, the MICrONS Consortium emphasized that in the mammalian cortex, cells of different cell types may contain neurons with different tuning preferences, so it is necessary to read same-brain connectivity and same-brain function together. In other words, even if the graph structure is the same, the physical meaning of the circuit changes if the node label and same-brain physiology are different. An unlabeled graph with a reduced cell type may be convenient for compression, but it loses a lot of the information required to reproduce the function.
</p>

<h3>2. Activity-dependent transcription / chromatin state is not reducible to node label</h3>
<p>
The weak point that became clearer in this pass was that the site was already separating <strong>cell identity</strong> from <strong>intrinsic excitability</strong>, while still leaving <strong>the current transcriptional / chromatin program for allocation and stabilization</strong> too close to the cell-type bucket. That is too weak. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">Santoni et al. (2024)</a> showed that chromatin plasticity predetermines neuronal eligibility for memory-trace formation, <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">Traunmüller et al. (2025)</a> showed region-specific and time-defined chromatin / gene-expression changes after novel-environment exposure, <a href="https://doi.org/10.1038/s41586-025-09334-w" target="_blank">Terceros et al. (2026)</a> showed thalamocortical transcriptional gates that coordinate memory stabilization across distinct post-learning windows, and <a href="https://doi.org/10.1038/s41588-025-02195-z" target="_blank">Coda et al. (2025)</a> showed cell-type- and locus-specific epigenetic editing of memory expression. In other words, even if the graph and cell-type label are fixed, <strong>which neurons are allocation-ready and which late programs stabilize memory</strong> can still remain as latent state.
</p>

<strong>Reading rule for transcriptomic evidence</strong>
<p>
On this site, a static atlas or one-shot memory-related DEG list is treated as <strong>identity prior or time-stamped clue</strong>, not as a ground truth of the current plasticity-competent state. Unless temporal calibration, locus specificity, or causal perturbation is shown, transcriptomic evidence stays below current-state completion.
</p>

<h3>3. Intrinsic excitability and homeostasis set point is not a byproduct of node label</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> showed that the morpho-electric phenotype spreads continuously even within the same transcriptomic type. Furthermore, <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> showed that even among identified neurons, there are large individual differences in ion channel mRNA and current amount, and <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> modeled how activity-dependent channel expressions can yield activity set points. Furthermore, <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> have shown that a firing-rate set point exists for each single neuron in vivo. In other words,<strong>even if the cell-type label and graph are known, the return destination after threshold, gain, rebound, and perturbation can still remain as latent state</strong>.
</p>

<h3>4. Synapses are not binary edges</h3>
<p>
Holler et al. analyzed the ultrastructure and release properties of neocortical synapses, and showed that transmission properties cannot be expressed simply by "connected/not connected." Matsuzaki et al. demonstrated that spine enlargement and AMPA current increases are linked in LTP induction in a single dendritic spine. Furthermore, Vardalaki et al. showed that even in the adult neocortex, approximately 25% of filopodia can serve as the structural basis for silent synapse lacking AMPA receptors. Therefore, <strong>edge list alone will reduce the weight of the current state, plastic history, and whether it is functionally active in the first place</strong>.
</p>

<strong>Current weight is not the same as the late-stabilization route</strong>
<p>
<a href="https://doi.org/10.1038/385533a0" target="_blank">Frey &amp; Morris (1997)</a> proposed synaptic tagging as the condition that allows late LTP to capture plasticity-related proteins, <a href="https://doi.org/10.1038/ncomms2250" target="_blank">Shires et al. (2012)</a> demonstrated synaptic tagging and capture in the living rat, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a> showed branch-level integration of protein-synthesis-dependent LTP, and <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">Fonseca et al. (2006)</a> showed that late-LTP maintenance depends on a balance between protein synthesis and proteasome-dependent degradation. More recently, <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">Pandey et al. (2021)</a> linked local autophagy-coupled translation to long-term memory formation and <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">Thomas et al. (2025)</a> showed that actin/spine geometry can persist on the timescale of the synaptic tag. Therefore, even if the connectome and a weight estimate are given, the branch-local capture and stabilization route can still remain latent.
</p>

<h3>5. Perisynaptic ECM / PNN state is not just packaging around synapses</h3>
<p>
The current site used to separate synapses, timing, neuromodulation, and glia, while still leaving <strong>the extracellular matrix around synapses and inhibitory cells</strong> too implicit. That was too weak. <a href="https://doi.org/10.1126/science.1072699" target="_blank">Pizzorusso et al. (2002)</a> showed that digesting chondroitin-sulfate proteoglycans can reopen ocular-dominance plasticity in adult visual cortex. <a href="https://doi.org/10.1038/nn.2338" target="_blank">Frischknecht et al. (2009)</a> showed that brain extracellular matrix constrains AMPA-receptor lateral mobility and short-term synaptic plasticity. <a href="https://doi.org/10.1126/science.1174146" target="_blank">Gogolla et al. (2009)</a> showed that perineuronal nets protect fear memories from erasure, and <a href="https://doi.org/10.1016/j.matbio.2024.11.001" target="_blank">Jabłońska et al. (2024)</a> showed that extracellular-matrix integrity regulates hippocampal GABAergic plasticity. In other words, the missing variable is not only "how strong the synapse is now," but also <strong>which plasticity transitions and stabilization regimes are still available on that same graph</strong>.
</p>

<strong>Human observability ceiling for ECM / PNN state</strong>
<p>
Human evidence is moving, but it is still not an in vivo whole-brain ground truth of current ECM state. <a href="https://doi.org/10.3390/ijms23158197" target="_blank">Boonen et al. (2022)</a> showed extracellular-matrix reorganization in human hippocampal sclerosis tissue, which is useful evidence that the matrix layer is biologically real in human disease tissue. But this remains <strong>ex vivo pathology</strong>, not a direct readout of moment-to-moment perisynaptic matrix state in a living human brain. On this site, ECM / PNN is therefore treated as a latent state unless it is externally calibrated or locally perturbed.
</p>

<h3>6. Ionic milieu / chloride homeostasis is not background chemistry</h3>
<p>
The current site had become good at separating <strong>intrinsic excitability</strong>, <strong>ECM / PNN</strong>, <strong>timing-state</strong>, and <strong>glia</strong>, while still leaving <strong>chloride set point and interstitial ion composition</strong> too implicit. That was too weak. <a href="https://doi.org/10.1126/science.1245423" target="_blank">Glykys et al. (2014)</a> showed that local impermeant anions help establish neuronal chloride concentration, <a href="https://doi.org/10.1038/s41467-017-01749-0" target="_blank">Heubl et al. (2017)</a> showed that GABA<sub>A</sub>-receptor-mediated synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase, <a href="https://doi.org/10.1126/science.aad4821" target="_blank">Ding et al. (2016)</a> showed that changing interstitial K<sup>+</sup>, Ca<sup>2+</sup>, Mg<sup>2+</sup>, and H<sup>+</sup> is sufficient to shift cortical activity and sleep/wake state, and <a href="https://doi.org/10.1523/JNEUROSCI.2761-07.2007" target="_blank">Huberfeld et al. (2007)</a> showed perturbed chloride homeostasis with depolarizing GABAergic signaling in human temporal-lobe epilepsy. More recently, <a href="https://doi.org/10.1038/s41386-022-01480-5" target="_blank">Simonnet et al. (2023)</a> linked KCC2 silencing to impaired hippocampal memory and altered rhythmogenesis, and <a href="https://doi.org/10.1007/s12576-018-00654-5" target="_blank">Nakamura et al. (2019)</a> showed that KCC2 overexpression enhances dendritic-spine plasticity and motor learning. In other words, the missing variable is not only <strong>how excitable a neuron is in general</strong>, but also <strong>what sign and gain inhibition has on that local circuit right now</strong>.
</p>

<strong>Human observability ceiling for ionic state</strong>
<p>
Human ionic evidence is still a coarse observability class. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> demonstrated high-resolution sodium imaging of healthy human brain at 7 T, which is useful evidence that some ionic layer is becoming visible in vivo. But this remains a mm-class tissue sodium map, not a direct readout of <strong>cell-specific chloride concentration</strong>, <strong>KCC2 / NKCC1 balance</strong>, <strong>extracellular K<sup>+</sup> or Ca<sup>2+</sup> microdomains</strong>, or <strong>local E<sub>GABA</sub></strong>. On this site, human sodium imaging is therefore treated as a <strong>macro ionic proxy</strong>, not as ground truth of current chloride homeostasis.
</p>

<h3>7. Shared extracellular / electrical state is not reducible to chemical wiring</h3>
<p>
The remaining weakness was that the site had become much better at separating <strong>ionic / chloride state</strong>, <strong>timing-state</strong>, and <strong>glia</strong>, while still leaving <strong>gap-junction coupling, endogenous field effects, and local inhibitory driving force</strong> too close to the chemical-synapse bucket. That was too weak. <a href="https://doi.org/10.1038/99496" target="_blank">Galarreta &amp; Hestrin (1999)</a> showed that fast-spiking interneurons in neocortex form electrical-synapse networks, <a href="https://doi.org/10.1038/nn.2727" target="_blank">Anastassiou et al. (2011)</a> showed that endogenous extracellular fields can causally entrain cortical spike timing under physiological conditions, <a href="https://doi.org/10.1073/pnas.2313042121" target="_blank">Yang et al. (2024)</a> showed that dynamic electrical synapses can rewire brain networks for persistent oscillations, and <a href="https://doi.org/10.1038/s41467-024-53074-y" target="_blank">Selfe et al. (2024)</a> showed with ORCHID that inhibitory driving force can now be measured directly, but only with specialized local optical methods. In other words, the missing variable is not only <strong>how strong chemical inhibition is</strong>, but also <strong>how electrical coupling and local field state coordinate spikes and oscillations on that same chemical graph</strong>.
</p>

<strong>Human observability ceiling for electrical-state</strong>
<p>
Human evidence for this layer is still indirect. <a href="https://doi.org/10.1111/ejn.70401" target="_blank">Feld et al. (2026)</a> reported that mefloquine before sleep impaired declarative-memory retention and disrupted spindle-to-slow-oscillation coupling in healthy participants, which is useful perturbation evidence that electrical coupling can matter for systems-memory coordination. But the same paper also leaves off-target effects as a caveat, and it is not a direct readout of <strong>which cells were electrically coupled</strong> or <strong>what the local inhibitory driving force was</strong>. On this site, human evidence for shared electrical state is therefore read first as a <strong>perturbation-conditioned clue</strong>, not as ground truth of local electrical coupling in vivo.
</p>

<h3>8. Delay and myelin are part of timing</h3>
<p>
<a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a> showed that neuronal activity promotes oligodendrogenesis and adaptive myelination, and <a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. (2014)</a> showed that active central myelination is required for motor-skill learning. But the weakness of the earlier page was that it still allowed the reader to compress this into the slogan "more myelin, faster signal." Primary literature now supports a stronger statement: <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a> showed that node and internode geometry is tuned along auditory axons to adjust action-potential timing, <a href="https://doi.org/10.1073/pnas.1811013115" target="_blank">Dutta et al. (2018)</a> showed that perinodal astrocytes can reversibly alter nodal gap length and myelin structure to change conduction velocity and spike arrival, and <a href="https://doi.org/10.1016/j.cell.2019.11.039" target="_blank">Cohen et al. (2020)</a> showed that saltatory conduction depends on a conductive periaxonal nanocircuit rather than on a single scalar delay term.
</p>
<p>
This matters for WBE because timing-sensitive circuits do not only depend on "who connects to whom," but also on <strong>when inhibition, synchrony, and phase-locked drive arrive</strong>. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">Micheva et al. (2021)</a> showed that even locally projecting PV interneurons gain physiologically relevant conduction-speed differences with axonal myelination, and <a href="https://doi.org/10.7554/eLife.73827" target="_blank">Dubey et al. (2022)</a> linked loss of PV-axon myelination to weakened fast inhibition and failure of gamma synchronization. Therefore, if timing matters, the missing variable is better described as <strong>timing-state</strong> rather than simply "delay."
</p>

<strong>Human observability ceiling for timing-state</strong>
<p>
<a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">van Blooijs et al. (2023)</a> showed that transmission speed in the human brain follows a developmental trajectory, which is useful evidence that conduction timing is biologically variable at the tract scale. But this is still a macro timing proxy, not a cell-specific readout of node length, periaxonal space, oligodendrocyte state, or local inhibitory arrival time. On this site, human myelin or tract-speed readouts are therefore treated as macro support for timing-state, not as ground truth of per-axon conduction state.
</p>

<h3>9. Neuromodulation is not “one mood scalar”</h3>
<p>
Reimer et al. showed that pupil fluctuations track both adrenergic and cholinergic activity within the cortex. Conversely, this also means that<strong>pupil diameter does not uniquely represent one transmitter state or the other</strong>. Additionally, Neyhart et al. showed that while cortical ACh is highly predictable from cholinergic axon activity and behavioral state, it also has locality that depends on distance from neighboring axons and clearance kinetics. Therefore, although it is useful to use pupil diameter or HRV in humans, it is an overstatement to consider it as the ground truth of transmitter-specific and region-specific internal states. What is necessary is not only to say whether it is a good proxy or not, but also to specify what it is and what it is not.
</p>

<h3>10. Glia is not an afterthought auxiliary variable</h3>
<p>
Adamsky et al. showed that astrocytic activation can produce de novo neuronal potentiation and memory enhancement. Cahill et al. reported that local, instantaneous neurotransmitter inputs are encoded into responses of a broad astrocyte network over minutes. Therefore, a model that ignores glia should be treated as a model that partially lacks plasticity and slow network state. What is important here is not to generalize that glia are also involved, but to clarify in the model specifications <strong>Which time constants and which state variables were discarded</strong>.
</p>

<h2>Don't end with enumeration, compare with augmentation / ablation</h2>
<p>
The weakness of the current site was that even if it was possible to enumerate the missing state variables, it did not bring to the fore what additional information and which error terms could be reduced to advance to a stronger claim. Primary literature from 2024-2026 shows that when you add same-brain function, transcriptomic label, activity-dependent transcription / chromatin audit, ECM / PNN state, ionic milieu / chloride-homeostasis audit, shared extracellular / electrical-state audit, local transmitter dynamics, glial slow state, and recovery log from the connectome-only baseline, the improvement is different. Therefore, on this site, instead of counting state variables as "present/absent," we will compare held-out predictive gain using augmentation/ablation.
</p>
<table>
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
<td>Compare a chemical-connectome or synapse-aware baseline against the same model with gap-junction measurements or perturbation, local field calibration, or direct inhibitory-driving-force measurement under the same held-out synchrony, sleep-oscillation, or state-switch condition.</td>
<td>Galarreta, Anastassiou, Yang, Selfe, and Feld together support that fast synchrony, oscillatory coordination, and electrical-state regime can be read more narrowly once electrical coupling and local driving-force state are treated explicitly.</td>
<td>Human perturbation or macro field evidence alone remains indirect and does not become ground truth of local electrical coupling or cell-specific inhibitory driving force in vivo.</td>
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

<strong>Conditions for passing on this site</strong>
<p>
An added state variable can be described as ``effective'' if it shows a predictive gain in any of the cross-state / cross-day / perturbation / recovery conditions when comparing <strong>(a) connectome-only baseline</strong> and <strong>(b) model with additional variables under the same split / same held-out conditions</strong>, and at the same time shows <strong>proxy specificity</strong>, <strong>family / uncertainty</strong>, <strong>abstention</strong>, and the <strong>time scale at which the added variable was observed or calibrated</strong>. If it does not go that far, this site treats it as an annotation, stratification covariate, or post hoc explanation.
</p>

<h2>Reading rules and minimum submissions adopted on this site</h2>

<h4>Rule</h4>
<ul>
<li><strong>connectome-complete:</strong> Treat as a structural atlas, candidate scaffold, and starting point for compaction. It is not written as achieving L2/L3 emulation. </li>
<li><strong>connectome-constrained model:</strong> First of all, it is treated as a hypothesis engine / conditional model. It is not written as the unique solution of the internal state. </li>
<li><strong>augmentation / ablation:</strong>You can't write that "the added state variable worked" without putting a connectome-only baseline. </li>
<li><strong>transcriptomic atlas is not current chromatin state:</strong>Do not auto-complete memory-stabilization controller from cell identity or one-shot DEG evidence. </li>
<li><strong>intrinsic excitability / homeostatic set point:</strong>Do not automatically infer from cell-type label or short-term activity matching. If not measured, write latent state. </li>
<li><strong>local proteostasis / synaptic tagging:</strong>Do not auto-complete late stabilization from current weight alone. If not measured, write latent state. </li>
<li><strong>ECM / PNN state:</strong>Do not collapse plasticity gate, receptor mobility, or memory-stabilization resistance into synapse count or glial support. If not measured, write latent state. </li>
<li><strong>ionic milieu / chloride homeostasis:</strong>Do not collapse inhibitory sign or state-transition regime into cell type, weight snapshot, or generic excitability. If not measured, write latent state. </li>
<li><strong>shared extracellular / electrical state:</strong>Do not collapse gap junctions, endogenous field effects, or inhibitory driving force into the chemical connectome or a generic ionic proxy. If not measured, write latent state.</li>
<li><strong>Delay is not one scalar:</strong>If timing matters, separate device latency, biological timing-state, and phase error; if the biological side is not measured, write timing-state as latent. </li>
<li><strong>pupil / HRV:</strong> A useful state covariate for human data, but not a transmitter-specific ground truth. </li>
<li><strong>When state variable is missing:</strong>If estimated, specify the error and abstention condition; if not, specify absent. </li>
<li>When there are no weights / timing-state: phase, timing, intervention response, and closed-loop stability claims are demoted. </li>
<li><strong>When dropping glia / neuromodulation:</strong>Write in the text what behavior was discarded in the approximation as the scope of application. </li>
<li>When multiple <strong>families remain:</strong>Rather than just confidence, expose family comparison, uncertainty, and abstention. </li>
</ul>

<table>
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
<td>Include same-brain function or perturbation, list of missing state variables, proxy limits, family/uncertainty, and absence of intrinsic excitability/homeostatic set point plus ionic / chloride state if not measured. </td>
</tr>
<tr>
<td><strong>Intervention/Closed Loop claim</strong></td>
<td>In addition to the above, we will also publish calibration routes for weights / timing-state / neuromodulation / excitability-homeostasis / ionic milieu, external validation, and abstention / stop conditions. </td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <em>Nature</em>, 634, 1132–1140. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 2561–2574. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Thomas, C., Ye, F. Q., Irfanoglu, M. O., Modi, P., Saleem, K. S., Leopold, D. A., &amp; Pierpaoli, C. (2014). Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 111(46), 16574–16579. <a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">doi:10.1073/pnas.1405672111</a></li>
<li>Reveley, C., Seth, A. K., Pierpaoli, C., Silva, A. C., Yu, D., Saunders, R. C., Leopold, D. A., &amp; Ye, F. Q. (2015). Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 112(21), E2820–E2828. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">doi:10.1073/pnas.1418198112</a></li>
<li>Donahue, C. J., Sotiropoulos, S. N., Jbabdi, S., Hernandez-Fernandez, M., Behrens, T. E., Dyrby, T. B., Coalson, T., Kennedy, H., Knoblauch, K., Van Essen, D. C., &amp; Glasser, M. F. (2016). Using diffusion tractography to predict cortical connection strength and distance: A quantitative comparison with tracers in the monkey. <em>Journal of Neuroscience</em>, 36(25), 6758–6770. <a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">doi:10.1523/JNEUROSCI.0493-16.2016</a></li>
<li>Maier-Hein, K. H., Neher, P. F., Houde, J.-C., Côté, M.-A., Garyfallidis, E., Zhong, J., Chamberland, M., et al. (2017). The challenge of mapping the human connectome based on diffusion tractography. <em>Nature Communications</em>, 8, 1349. <a href="https://doi.org/10.1038/s41467-017-01285-x" target="_blank">doi:10.1038/s41467-017-01285-x</a></li>
<li>Schilling, K. G., Petit, L., Rheault, F., Remedios, S., Pierpaoli, C., Anderson, A. W., Landman, B. A., &amp; Descoteaux, M. (2020). Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. <em>Brain Structure and Function</em>, 225(8), 2387–2402. <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">doi:10.1007/s00429-020-02129-z</a></li>
<li>Grisot, G., Haber, S. N., Hawrylycz, M., Yendiki, A., et al. (2021). Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. <em>NeuroImage</em>, 239, 118300. <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">doi:10.1016/j.neuroimage.2021.118300</a></li>
<li>Sarwar, T., Ramamohanarao, K., Daducci, A., Schiavi, S., Smith, R. E., &amp; Zalesky, A. (2023). Evaluation of tractogram filtering methods using human-like connectome phantoms. <em>NeuroImage</em>, 282, 120376. <a href="https://doi.org/10.1016/j.neuroimage.2023.120376" target="_blank">doi:10.1016/j.neuroimage.2023.120376</a></li>
<li>He, Y., Hong, Y., Wu, Y., et al. (2024). Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. <em>NeuroImage</em>, 303, 120904. <a href="https://doi.org/10.1016/j.neuroimage.2024.120904" target="_blank">doi:10.1016/j.neuroimage.2024.120904</a></li>
<li>McMaster, E. M., Newlin, N. R., Rudravaram, G., et al. (2025). Harmonized connectome resampling for variance in voxel sizes. <em>Magnetic Resonance Imaging</em>, 121, 110424. <a href="https://doi.org/10.1016/j.mri.2025.110424" target="_blank">doi:10.1016/j.mri.2025.110424</a></li>
<li>Manzano-Patrón, J. P., Deistler, M., Schröder, C., et al. (2025). Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. <em>Medical Image Analysis</em>, 103, 103580. <a href="https://doi.org/10.1016/j.media.2025.103580" target="_blank">doi:10.1016/j.media.2025.103580</a></li>
<li>Zhu, S., Huszar, I. N., Cottaar, M., et al. (2025). Imaging the structural connectome with hybrid MRI-microscopy tractography. <em>Medical Image Analysis</em>, 102, 103498. <a href="https://doi.org/10.1016/j.media.2025.103498" target="_blank">doi:10.1016/j.media.2025.103498</a></li>
<li>Galarreta, M., &amp; Hestrin, S. (1999). A network of fast-spiking cells in the neocortex connected by electrical synapses. <em>Nature</em>, 402, 72–75. <a href="https://doi.org/10.1038/99496" target="_blank">doi:10.1038/99496</a></li>
<li>Anastassiou, C. A., Perin, R., Markram, H., &amp; Koch, C. (2011). Ephaptic coupling of cortical neurons. <em>Nature Neuroscience</em>, 14(2), 217–223. <a href="https://doi.org/10.1038/nn.2727" target="_blank">doi:10.1038/nn.2727</a></li>
<li>Yang, Y.-C., Wang, G.-H., Chou, P., Hsueh, S.-W., Lai, Y.-C., &amp; Kuo, C.-C. (2024). Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 121(8), e2313042121. <a href="https://doi.org/10.1073/pnas.2313042121" target="_blank">doi:10.1073/pnas.2313042121</a></li>
<li>Selfe, J. S., et al. (2024). All-optical reporting of inhibitory receptor driving force in the nervous system. <em>Nature Communications</em>, 15(1), 8913. <a href="https://doi.org/10.1038/s41467-024-53074-y" target="_blank">doi:10.1038/s41467-024-53074-y</a></li>
<li>Feld, G. B., Niethard, N., Liu, J., et al. (2026). Electrical synapses contribute to sleep-dependent declarative memory retention. <em>European Journal of Neuroscience</em>, 63(2), e70401. <a href="https://doi.org/10.1111/ejn.70401" target="_blank">doi:10.1111/ejn.70401</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497–505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Santoni, G., et al. (2024). Chromatin plasticity predetermines neuronal eligibility for memory trace formation. <em>Science</em>, 385(6716), eadg9982. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">doi:10.1126/science.adg9982</a></li>
<li>Traunmüller, L., et al. (2025). Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. <em>Nature Communications</em>, 16, 2613. <a href="https://doi.org/10.1038/s41467-025-63029-6" target="_blank">doi:10.1038/s41467-025-63029-6</a></li>
<li>Coda, B., et al. (2025). Cell-type- and locus-specific epigenetic editing of memory expression. <em>Nature Genetics</em>, 57, 1211–1222. <a href="https://doi.org/10.1038/s41588-025-02195-z" target="_blank">doi:10.1038/s41588-025-02195-z</a></li>
<li>Terceros, Y., et al. (2026). Thalamocortical transcriptional gates coordinate memory stabilization. <em>Nature</em>, 642, 489–498. <a href="https://doi.org/10.1038/s41586-025-09334-w" target="_blank">doi:10.1038/s41586-025-09334-w</a></li>
<li>Frey, U., &amp; Morris, R. G. M. (1997). Synaptic tagging and long-term potentiation. <em>Nature</em>, 385(6616), 533–536. <a href="https://doi.org/10.1038/385533a0" target="_blank">doi:10.1038/385533a0</a></li>
<li>Fonseca, R., Vabulas, R. M., Hartl, F. U., Bonhoeffer, T., &amp; Nägerl, U. V. (2006). A balance of protein synthesis and proteasome-dependent degradation determines the maintenance of LTP. <em>Neuron</em>, 52(2), 239–245. <a href="https://doi.org/10.1016/j.neuron.2006.08.015" target="_blank">doi:10.1016/j.neuron.2006.08.015</a></li>
<li>Govindarajan, A., Israely, I., Huang, S.-Y., &amp; Tonegawa, S. (2011). The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. <em>Neuron</em>, 69(1), 132–146. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">doi:10.1016/j.neuron.2010.12.008</a></li>
<li>Shires, K. L., Da Silva, B. M., Hawthorne, J. P., Morris, R. G. M., &amp; Martin, S. J. (2012). Synaptic tagging and capture in the living rat. <em>Nature Communications</em>, 3, 1246. <a href="https://doi.org/10.1038/ncomms2250" target="_blank">doi:10.1038/ncomms2250</a></li>
<li>Pandey, K., Yu, X.-W., Steinmetz, A., &amp; Alberini, C. M. (2021). Autophagy coupled to translation is required for long-term memory formation. <em>Autophagy</em>, 17(9), 2489–2505. <a href="https://doi.org/10.1080/15548627.2020.1775393" target="_blank">doi:10.1080/15548627.2020.1775393</a></li>
<li>Thomas, M., Bogaciu, C.-A., Rizzoli, S. O., et al. (2025). Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. <em>Communications Biology</em>, 8, 756. <a href="https://doi.org/10.1038/s42003-025-08459-0" target="_blank">doi:10.1038/s42003-025-08459-0</a></li>
<li>Holler, S., et al. (2021). Structure and function of a neocortical synapse. <em>Nature</em>, 591, 111–116. <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">doi:10.1038/s41586-020-03134-2</a></li>
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
<li>van Blooijs, D., de Haan, A. M., Renaud, S., et al. (2023). Developmental trajectory of transmission speed in the human brain. <em>Nature Neuroscience</em>, 26, 828–838. <a href="https://doi.org/10.1038/s41593-023-01272-0" target="_blank">doi:10.1038/s41593-023-01272-0</a></li>
<li>Qian, Y., Zhao, T., Zheng, H., Weimer, J., &amp; Boada, F. E. (2012). High-resolution sodium imaging of human brain at 7 T. <em>Magnetic Resonance in Medicine</em>, 68(1), 227–233. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">doi:10.1002/mrm.23225</a></li>
<li>Reimer, J., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Adamsky, A., et al. (2018). Astrocytic activation generates de novo neuronal potentiation and memory enhancement. <em>Nature Neuroscience</em>, 21, 1725–1733. <a href="https://doi.org/10.1038/s41593-018-0253-6" target="_blank">doi:10.1038/s41593-018-0253-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <em>Communications Biology</em>, 7, 1498. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
</ol>
