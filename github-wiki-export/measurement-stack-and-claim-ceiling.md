# Wiki: observability and claim ceiling by measurement stack

> multimodal is not a synonym for ``seen everything''
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-15 / Role: Technical / natural science only

## Role Of This Page
This page is a wiki that fixes the ``upper claim limit for each measurement stack,'' which is often overlooked in WBE discussions. It's not enough to say that hidden state is important. Based on primary literature, we will explain what each of EEG/MEG/fMRI, spatial transcriptomics, Patch-seq, volume EM, same-brain functional connectomics, and local transmitter/glia imaging directly observes and what remains latent.

## Accuracy Notes
The ``claim ceiling'' column below is not the conclusion declared by each paper. This is an operational inference drawn by this site from variables directly observed in primary literature and state variables that are still unobserved.

## Back To Public Pages
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [technology roadmap](https://mind-upload.com/tech_roadmap.html)

## Related Wiki Pages
- [Wiki: Why wiring diagrams alone are not enough](https://github.com/yasufumi-nakata/mind-upload/wiki/connectome-is-not-enough) - This is a page that first organizes which state variables will be omitted.
- [Wiki: Homeostatic plasticity and maintenance state](https://github.com/yasufumi-nakata/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state) - Dig deeper into missing variables from the long-term maintenance-state side.
- [Wiki: Multimodal integration basics](https://github.com/yasufumi-nakata/mind-upload/wiki/multimodal-integration-basics) - Click here if you would like to take a closer look at the integrated audit of EEG/MEG/fMRI/invasive records.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - This is an entry point to avoid confusing observed values ​​and latent state estimates.

## What Is Currently Known
- EEG/MEG/fMRI provides macroscopic proxies, but not directly for cell types, synaptic efficiency, neuromodulatory fields, and glial status.
- Whole-brain spatial transcriptomics provides a major advance in cell-type taxonomy and spatial location, but the sufficiency of dynamic states is another matter.
- Patch-seq and same-brain connectomics reduce degeneracy, but the sufficiency of whole-brain coverage and long-term maintenance-state remains.
- Local transmitter / glia imaging is effective for calibrating coarse proxies, but it does not directly provide whole-brain ground truth.

## What Is Still Unknown
- It cannot yet be determined which stack combination will most efficiently reduce degeneracy for WBE.
- The sufficient conditions for which latent state should be obtained in the same brain, whole brain, and long-term longitudinal study are not yet determined.
- How to optimize the augmentation order between stacks can also vary depending on the task, species, and time constant.

---

<h2>The shortest conclusion</h2>
<p>
The weakness of the current site is that even though it was possible to enumerate important hidden states, it did not highlight which measurement stack directly observes what and where it hits the claim limit. Based on the primary literature, EEG/MEG/fMRI strengthens macro state tracking, whole-brain spatial atlas strengthens cell-type and spatial arrangement, Patch-seq bridges cell-type and morpho-electric phenotype, volume EM strengthens structural scaffolding, same-brain functional connectomics strengthens local conditional prediction, and local transmitter/astrocyte imaging strengthens coarse proxy calibration. However,<strong>no stack alone provides state-complete reconstruction</strong>. Therefore, on this site, we clearly specify the claim ceiling for each measurement stack, and prohibit expressions that exceed that.
</p>

<strong>Scope of this page</strong>
<p>
Philosophy, legal systems, and individuality are not covered here. What we are dealing with is the question of ``what can be seen directly through observation, and what is still latent'' from the perspective of technology and natural science only.
</p>

<h2>Weaknesses to be explored in depth</h2>
<p>
Conventional public pages already knew that connectome alone was not enough, maintenance-state remained, and comparisons should be made using augmentation/ablation. However, this alone leaves room for readers to overinterpret when they see the words <strong>multimodal</strong>, <strong>atlas</strong>, and <strong>same-brain</strong>, saying, ``I see pretty much everything.'' The weakness is that the discussion of<strong>state variables</strong> and<strong>measurement stack</strong>s have not yet been fully integrated.
</p>
<p>
Therefore, on this page, we will integrate the direct observables of each stack, what can be said a little more strongly, what will still remain in latent state, and the <strong>claim ceiling</strong> allowed by this site into one table.
</p>

<h2>Observability and claim ceiling per measurement stack</h2>

<strong>How to read</strong>
<p>
The last column of the table below is not a summary of each paper, but the operating rules for this site. In other words, it is a well-founded upper bound subtracted from <strong>the stack's directly observed variables</strong> and <strong>still unobserved state variables</strong>.
</p>

<table>
<thead>
<tr>
<th>measurement stack</th>
<th>What is directly observed</th>
<th>Something that can be said relatively strongly</th>
<th>What remains latent</th>
<th>Claim ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG</strong></td>
<td>Globally synchronized current field and its time change. </td>
You can audit some of the <td>ms-scale global state transitions, frequency band dynamics, and closed-loop timing constraints. </td>
<td>The uniqueness of the deep source, cell type, current synaptic efficiency, neuromodulatory field, and glial/metabolic state are not directly determined. </td>
<td><strong>Macro state tracking and weak L2</strong>. It does not raise to cell/synapse granularity or state-complete claims. </td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>Hemodynamic proxy and slow regional scale network state. </td>
<td>Wide coverage, recruitment patterns, and relatively slow state occupancy can be tracked within the same individual. </td>
<td>ms timing, excitation/inhibition separation, local transmitter dynamics, and current synaptic efficacy are not directly visible. </td>
<td><strong>Wide-area state atlas and coarse dynamical constraints</strong>. We do not claim the sufficiency of fast causal mechanisms or microstates. </td>
</tr>
<tr>
<td><strong>whole-brain spatial transcriptomics / cell atlas</strong></td>
<td>Ex vivo transcriptomic cell type and spatial arrangement. </td>
<td>Like Yao et al.'s whole-mouse-brain atlas, it can greatly advance cell-type taxonomy, regional distribution, and molecular maps. </td>
<td>The current firing rules, synaptic efficiency, neuromodulatory/glial state, sleep-history, and destination after perturbation remain. </td>
<td><strong>Up to molecular atlas / cell-type prior</strong>. It does not increase dynamic completeness or current state sufficiency. </td>
</tr>
<tr>
<td><strong>Patch-seq / morpho-electric-transcriptomic bridge</strong></td>
<td>Compatible with single cell transcriptome, morphology, and electrophysiology. </td>
<td>Like the systems of Gouwens et al. and Gamlin et al., it is possible to strengthen the bridge between cell-type labels, morpho-electric phenotypes, and some connectivity motifs. </td>
<td>Whole-brain coverage, same-brain circuit context, current network state, and longitudinal plastic history remain. </td>
<td><strong>Up to cell-type-specific prior and local parameter constraints</strong>. It is not used for whole-brain state completeness. </td>
</tr>
<tr>
<td><strong>volume EM connectomics</strong></td>
<td>This is a structural snapshot of hyperfine morphology and chemical synapse. </td>
<td>You can strengthen the structural scaffold, projectome, and candidate circuits like Dorkenwald et al.'s whole-brain fly wiring diagram. </td>
<td>Current synaptic weight, intrinsic excitability, neuromodulatory context, glial slow state, and sleep-dependent maintenance are not directly included. </td>
<td><strong>Structural atlas / scaffold</strong>. Do not replace connectome-complete with emulation-complete. </td>
</tr>
<tr>
<td><strong>same-brain functional connectomics</strong></td>
<td>Correspondence between co-registered dense activity and EM connectome in the same brain. </td>
<td>Like MICrONS, local circuits can further strengthen structure-function links, state-dependent response prediction, and cell-type dependent wiring rules. </td>
<td>Whole-brain coverage, whole-state generalization, sufficiency of current synaptic efficacy, homeostatic controller, and glial/metabolic maintenance-state remain. </td>
<td><strong>Up to local conditional prediction and local functional twin</strong>. We do not promote whole-brain WBE or state-complete reconstruction. </td>
</tr>
<tr>
<td><strong>local transmitter imaging / behavior-linked proxy</strong></td>
<td>Local transmitter dynamics and its relationship with axon activity / pupil / locomotion. </td>
<td>Like Neyhart et al., you can calibrate what and how representative the coarse arousal proxy is and make the transmitter-linked covariate a little stronger. </td>
<td>The whole brain transmitter field, receptor state, region-generalizable ground truth, and long-timescale maintenance-state remain. </td>
<td><strong>Up to limited covariate / proxy calibration</strong>. We do not write single-transmitter ground truth or whole-brain internal state. </td>
</tr>
<tr>
<td><strong>astrocyte / glial imaging</strong></td>
<td>Astrocyte network response and slow-state dynamics to local neurotransmitter input. </td>
<td>Like Cahill et al., we can visualize minute-long glial network states and further strengthen slow-state/recovery modeling. </td>
<td>Full integration of whole-brain coverage, cell-type-specific generalization, fast synaptic state, sleep-history, and other stacks remains. </td>
<td><strong>As far as banning slow-state calibration and glia omission</strong>. This alone does not claim whole-brain completeness. </td>
</tr>
</tbody>
</table>

<h2>Why ceiling is so different</h2>

<h3>1. atlas strengthens identity but does not directly provide current state</h3>
<p>
Yao et al. combined scRNA-seq and MERFISH on whole mouse brain and presented a high-resolution atlas consisting of 34 classes, 338 subclasses, 1,201 supertypes, and 5,322 clusters. This is a major step forward in terms of cell-type taxonomy and spatial location. However, what we can say directly from this is <strong>which molecular class the cell belongs to and where it is located</strong>, but does not include<strong>the current moment's threshold, gain, synaptic efficacy, sleep-dependent renormalization, or transmitter occupancy</strong>. So while atlas is very important, it is safe to read it first as <strong>identity prior</strong>.
</p>

<h3>2. Patch-seq is a bridge but does not erase the coverage wall</h3>
<p>
Gouwens et al. showed that morpho-electric variation remains continuously within the transcriptomic family, and Gamlin et al. mapped MET-types defined by Patch-seq to large-scale EM and showed differences in myelination and synaptic output for each Sst MET-type. This means that <strong>cell-type label alone is not enough; adding electrophysiology and morphology is of great value</strong>. On the other hand, Patch-seq is sparse and destructive sampling and does not provide the whole brain current state or longitudinal history of the same individual. Therefore, it is a<strong>bridge</strong> and not<strong>whole-brain completeness</strong>.
</p>

<h3>3. EM connectome is a scaffold but does not freeze dynamic state</h3>
<p>
Dorkenwald et al.'s adult fly whole-brain connectome is a huge step forward, reorganizing approximately 5 × 10<sup>7</sup> chemical synapses and 139,255 neurons. However, EM is strong because it is a structural scaffold, and it is not a method that directly measures current weight, release probability, neuromodulatory context, and glial/metabolic background. The criticism that follows from this is simple: we must not equate knowing the wiring with knowing the generative state of the moment.
</p>

<h3>4. Adding same-brain function reduces degeneration, but does not reach whole-brain state-complete</h3>
<p>
MICrONS combines dense calcium imaging, behavioral states, and the EM connectome in the same brain, presenting multi-area functional connectomics of the mouse visual cortex. This is even stronger than connectome-only, and provides a basis for discussing <strong>structure-function links in the same brain. However, the paper itself deals with specific regions, specific tasks, and specific states of the visual cortex, and it is not possible to make a leap from there to the human whole-brain or all-state completeness. Therefore, the ceiling of this stack is <strong>local functional twin</strong>.
</p>

<h3>5. Neuromodulator / glia imaging reduces misreading of coarse proxies, but does not provide whole-brain ground truth</h3>
<p>
Neyhart et al. showed that cortical ACh dynamics are highly predictable from cholinergic axon activity and behavioral state, and also depend on distance from local axons and clearance kinetics. Cahill et al. showed that local neurotransmitter inputs are minute-long encoded into broad astrocyte networks. These teach us that just because ``pupil has increased'' or ``behavioral state has changed'' does not mean that the transmitter state or glial state can be simplified. Therefore, these stacks are very effective for <strong>proxy calibration</strong> and <strong>banning glia omission</strong>, but they do not directly become the ground truth of the whole brain's internal state.
</p>

<h2>Practical rules arising from this criticism</h2>

<h4>Rule</h4>
<ul>
<li><strong>Write the measurement stack in the augmentation claim:</strong>Instead of saying "added transcriptomic label", distinguish between whole-brain atlas, patch-seq bridge, or same-brain link. </li>
<li><strong>Don't mix atlas / bridge / scaffold / local twin / proxy calibration:</strong>Fix which kind of advance is the same "advance". </li>
<li><strong>Don't make multimodal a synonym for state-complete:</strong>Include in the text what latent state still remains. </li>
<li><strong>When filling in unobserved states, write ``estimated'': </strong>If threshold / gain / set point is auto-completed from cell type, write ``latent inference''. </li>
<li><strong>Prohibit expressions that exceed the claim ceiling:</strong>For example, do not write EM alone as emulation-complete, Patch-seq as whole-brain state-complete, or pupil as transmitter ground truth. </li>
</ul>

<table>
<thead>
<tr>
<th>Current stack</th>
<th>What to add next</th>
<th>Stronger argument</th>
<th>Claim to stop</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG / fMRI</strong></td>
<td>External ground truth, invasion record, structure/function correspondence of the same individual, and intervention response. </td>
<td>The rationale for moving from macro decode to weak L2 is a little stronger. </td>
<td>Stop cell/synapse state sufficiency, whole-brain WBE, and state-complete claims. </td>
</tr>
<tr>
<td><strong>whole-brain atlas</strong></td>
<td>Patch-seq, same-brain physiology, perturbation/recovery log. </td>
<td>Easier to connect cell-type prior and spatial prior to local parameter prior. </td>
<td>Turn off the sufficiency of current network state and longitudinal maintenance-state. </td>
</tr>
<tr>
<td><strong>volume EM</strong></td>
<td>Same-brain function, cell-type bridge, perturbation, uncertainty are public. </td>
<td>It is easier to proceed from structural scaffold to local conditional prediction. </td>
<td>Stop rephrasing connectome-complete as emulation-complete. </td>
</tr>
<tr>
<td><strong>local transmitter / glia imaging</strong></td>
<td>coverage, cross-stack calibration, cross-state / cross-day validation. </td>
<td>Coarse proxy validity and slow-state modeling can be strengthened. </td>
<td>Stop ground truth of single-transmitter global field and whole-brain internal state. </td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124-138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <em>Nature</em>, 624, 317-332. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435-447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497-505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Communications</em>, 15, 3820. <a href="https://doi.org/10.1038/s41467-024-47838-5" target="_blank">doi:10.1038/s41467-024-47838-5</a></li>
</ol>
