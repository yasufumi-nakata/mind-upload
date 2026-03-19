# Wiki: observability and claim ceiling by measurement stack

> multimodal is not a synonym for ``seen everything''
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-19 / 位置づけ: Technical / natural science only

## このページの役割
This page is a wiki that fixes the ``upper claim limit for each measurement stack,'' which is often overlooked in WBE discussions. It's not enough to say that hidden state is important. Based on primary literature, we will explain what each of EEG/MEG/fMRI, spatial transcriptomics, Patch-seq, volume EM, same-brain functional connectomics, synaptic-density PET, mixed arousal proxy, local transmitter sensor, receptor atlas / PET, glia imaging, and human biochemical / energetic / ionic / thermal / myelin / clearance routes directly observes and what remains latent.

## 正確さの前提
The ``claim ceiling'' column below is not the conclusion declared by each paper. This is an operational inference drawn by this site from variables directly observed in primary literature and state variables that are still unobserved.

## 公開ページへ戻る
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [technology roadmap](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: Why wiring diagrams alone are not enough](https://github.com/yasufumi-nakata/mind-upload/wiki/connectome-is-not-enough) - This is a page that first organizes which state variables will be omitted.
- [Wiki: Homeostatic plasticity and maintenance state](https://github.com/yasufumi-nakata/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state) - Dig deeper into missing variables from the long-term maintenance-state side.
- [Wiki: Multimodal integration basics](https://github.com/yasufumi-nakata/mind-upload/wiki/multimodal-integration-basics) - Click here if you would like to take a closer look at the integrated audit of EEG/MEG/fMRI/invasive records.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - This is an entry point to avoid confusing observed values ​​and latent state estimates.

## いま分かっていること
- EEG/MEG/fMRI provides macroscopic proxies, but not directly for cell types, synaptic efficiency, neuromodulatory fields, and glial status.
- In hemodynamic modalities, vascular transfer state such as baseline perfusion, CVR, and superficial/systemic contamination can also dominate amplitude differences.
- Whole-brain spatial transcriptomics provides a major advance in cell-type taxonomy and spatial location, but the sufficiency of dynamic states is another matter.
- Patch-seq and same-brain connectomics reduce degeneracy, but the sufficiency of whole-brain coverage and long-term maintenance-state remains.
- Local transmitter / glia imaging is effective for calibrating coarse proxies, but it does not directly provide whole-brain ground truth.
- Human biochemical, energetic, ionic, thermal, myelin, and clearance routes reduce different latent-state error terms and should not be summarized as one direct path to maintenance-state completeness.

## まだ分かっていないこと
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
<td>ms-scale global state transitions, frequency band dynamics, and closed-loop timing constraints can be audited. </td>
<td>The uniqueness of the deep source, cell type, current synaptic efficiency, neuromodulatory field, and glial/metabolic state are not directly determined. </td>
<td><strong>Macro state tracking and weak L2</strong>. It does not raise to cell/synapse granularity or state-complete claims. </td>
</tr>
<tr>
<td><strong>fMRI / hemodynamic modalities</strong></td>
<td>BOLD / HbO / HbR proxy and slow regional scale network state. </td>
<td>Wide coverage, recruitment patterns, relatively slow state occupancy, and coarse task-state differences can be tracked within the same individual. </td>
<td>ms timing, excitation/inhibition separation, local transmitter dynamics, current synaptic efficacy, and separation of neural state from vascular transfer state / CVR remain unresolved. </td>
<td><strong>Wide-area hemodynamic state atlas and coarse dynamical constraints</strong>. Without vascular-state / CVR audit, amplitude differences remain hemodynamic-limited rather than clean neural differences. </td>
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
<td><strong>SV2A PET / synaptic-density PET</strong></td>
<td>Tracer-defined regional SV2A binding interpreted through kinetic modeling or a validated simplified scan window. </td>
<td>You can strengthen human in vivo regional synaptic-density gradients, atlas construction, and disease-linked density comparisons. </td>
<td>Current release probability, postsynaptic receptor occupancy, task-evoked momentary synaptic efficacy, and branch-local plasticity state remain unresolved, and anatomy/partial-volume handling can still matter for interpretation. </td>
<td><strong>Up to regional synaptic-density proxy</strong>. We do not read it as current synaptic efficacy or momentary synaptic state. </td>
</tr>
<tr>
<td><strong>mixed arousal proxy (pupil / HRV / locomotion / facial motion)</strong></td>
<td>Behavior-linked arousal markers and their covariance with ongoing state. </td>
<td>You can stratify coarse arousal-like state and test whether a behavioral proxy carries useful variance for the task. </td>
<td>Transmitter identity, receptor family, regional release, cell-specific effect, and the whole-brain transmitter field remain unresolved. </td>
<td><strong>Up to coarse covariate / stratification</strong>. We do not treat it as transmitter-specific ground truth. </td>
</tr>
<tr>
<td><strong>local axon activity / transmitter sensor</strong></td>
<td>Local cholinergic / aminergic axon activity or local extracellular transmitter signal in the measured region. </td>
<td>You can calibrate local chemical dynamics, spatial heterogeneity, and where a mixed behavioral proxy fails or succeeds. </td>
<td>The whole-brain distribution, receptor occupancy / downstream effect, and cross-species generalization to human current state remain unresolved. </td>
<td><strong>Up to local transmitter-linked calibration</strong>. It is stronger than mixed proxy, but it is still not whole-brain neuromodulatory ground truth. </td>
</tr>
<tr>
<td><strong>receptor / transporter atlas or autoradiography</strong></td>
<td>Group-average regional distribution of selected receptors / transporters and laminar density priors from PET and autoradiography. </td>
<td>You can show where selected transmitter systems are likely to differ and which cortical axes they follow. </td>
<td>Current occupancy, task-evoked release, individual time-varying state, and cell-specific downstream effect remain unresolved. </td>
<td><strong>Up to regional chemoarchitectural prior</strong>. It is not read as the current neuromodulatory state. </td>
</tr>
<tr>
<td><strong>occupancy PET</strong></td>
<td>Ligand- or drug-specific target engagement within a named receptor family over bounded scan windows, interpreted through an explicit tracer and quantification model. </td>
<td>You can quantify selected exogenous target engagement for the chosen receptor family, ligand / drug, dose, and scan window. </td>
<td>Endogenous transmitter release, unsampled receptor families, laminar / cell-specific effect, and continuous state outside the dosing window remain unresolved. </td>
<td><strong>Up to ligand- and dose-limited target-engagement proxy</strong>. We do not read it as endogenous release or whole-brain current transmitter state. </td>
</tr>
<tr>
<td><strong>displacement / release-sensitive PET</strong></td>
<td>Challenge-linked change in binding potential for selected tracers / receptor families over bounded scan windows, used as a proxy for endogenous transmitter release under an explicit task or pharmacological challenge. </td>
<td>You can test whether a named challenge perturbs a selected transmitter system within the scanned window and spatial scope. </td>
<td>The complete transmitter field, unsampled receptor families, laminar / cell-specific effect, downstream consequence, and continuous state outside the challenge window remain unresolved. </td>
<td><strong>Up to receptor-, tracer-, and challenge-limited release proxy</strong>. We do not promote it to receptor-family-complete or whole-brain internal-state ground truth. </td>
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

<h3>5. Hemodynamic stacks also observe through a vascular transfer state</h3>
<p>
The weak point that needed another pass was that this page already called fMRI a <strong>hemodynamic proxy</strong>, but still left too much room for the reader to translate a BOLD amplitude difference directly into a neural difference. That was too weak. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> showed that inter-subject differences in CBF and CBV contribute to BOLD reactivity and that breath-hold-derived vascular-reactivity covariates improve group analyses. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> showed that task BOLD magnitude corresponds strongly to hypercapnia-based CVR across multiple cortical regions. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> showed that baseline CBF partly explains age-related components of multiple-demand-network BOLD responses, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that about 40% of task-responsive voxels can display oxygen-metabolism changes opposite in sign to the BOLD response. What follows directly from this is that <strong>hemodynamic stacks are limited not only by unobserved neural state, but also by unobserved vascular transfer state</strong>.
</p>

<strong>fNIRS belongs to the same caution family</strong>
<p>
The same logic applies to cortical hemodynamic modalities beyond fMRI. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015)</a> showed that short-separation regression improves both significance and localization for fNIRS tasks with differing autonomic responses. Therefore, on this site, fNIRS without <strong>short-separation / superficial diagnostic</strong> is not treated as a direct neural-difference readout either.
</p>

<h3>6. Neuromodulatory routes form a ladder, not one stack</h3>
<p>
The weakness that needed another pass was that this page still let <strong>pupil / HRV</strong>, <strong>local transmitter imaging</strong>, <strong>receptor maps</strong>, <strong>occupancy PET</strong>, and <strong>displacement / release-sensitive PET</strong> sound closer than they are. That was too weak. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> showed that pupil fluctuations track both adrenergic and cholinergic activity rather than a single transmitter. <a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">Lohani et al. (2022)</a> showed that cortical cholinergic signals are spatially heterogeneous across behavioral states, and <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> showed that local ACh depends on axon activity and local clearance kinetics. On the human side, <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> and <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">Goulas et al. (2021)</a> showed that receptor maps are structured regional priors, <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> showed selected D<sub>2</sub>-receptor target engagement by an administered drug, and <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, and <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> showed challenge- and window-limited dopamine or serotonin release proxies. What follows directly is that <strong>neuromodulation is not one measurement class</strong>.
</p>

<strong>Site rule for the ladder</strong>
<p>
On this site, <strong>mixed arousal proxy</strong> is read as a coarse covariate, <strong>local transmitter sensor</strong> as local calibration, <strong>receptor / transporter atlas</strong> as a regional prior, <strong>occupancy PET</strong> as target engagement, and <strong>displacement / release-sensitive PET</strong> as a challenge-limited release proxy. None of those rungs is promoted by default to the claim that the current whole-brain neuromodulatory state was directly measured.
</p>

<strong>Occupancy and displacement are different audit items</strong>
<p>
<a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> asked whether an administered antipsychotic occupied a selected receptor target in healthy humans. By contrast, <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, and <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> used task- or drug-challenge-linked binding changes as dopamine or serotonin release proxies within bounded windows. Those designs do not answer the same question. On this site, occupancy PET is therefore audited as <strong>target engagement</strong>, whereas displacement PET is audited as <strong>endogenous release proxy under a named challenge</strong>.
</p>

<strong>PET routes still need tracer and quantification disclosure</strong>
<p>
PET-based proxy classes are not readable from the modality label alone. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a> showed that human SV2A PET quantification depends on the tracer, arterial-versus-reference route, compartment model, and named scan window. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">Smart et al. (2021)</a> showed that [<sup>11</sup>C]UCB-J binding measures remain unchanged during brief functional activation even when tracer influx rises with blood flow, so synaptic-density PET is not a momentary synaptic-efficacy readout. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> built a receptor atlas by collating PET data from more than 1,200 healthy individuals, so the resulting map is a normative chemoarchitectural prior rather than an individual's current transmitter state. <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> quantified occupancy for an administered antipsychotic, while <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, and <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> used challenge-linked binding changes as displacement-based release proxies. Therefore, on this site, PET-based routes must name the tracer, occupancy-versus-displacement design, challenge or administered drug plus dose when applicable, quantification model or validated window, and partial-volume handling when relevant before their claim ceiling is interpreted.
</p>

<p>
The same caution extends to glia. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> showed that local neurotransmitter inputs are minute-long encoded into broad astrocyte networks. That is a real advance, but it is still a slow-state / support-state route, not an automatic shortcut to whole-brain internal-state completeness.
</p>

<h2>7. Human maintenance-state routes also form a ladder</h2>
<p>
Another weakness that remained on this page was that it separated generic measurement stacks while still leaving recent <strong>human maintenance-state evidence</strong> too easy to compress into one sentence such as ``human in vivo observability is getting close.'' That is too weak. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> pushed up <strong>local human nanoscale ultrastructure</strong>, <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> pushed up a <strong>regional synaptic-density atlas</strong>, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> pushed up a <strong>whole-brain biochemical scaffold</strong>, <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> pushed up <strong>macro energetic routes</strong>, <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> and <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">Qian et al. (2025)</a> pushed up <strong>macro ionic routes</strong>, <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a> pushed up <strong>macro thermal routes</strong>, <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> pushed up <strong>macro myelin mapping</strong>, <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">Huber et al. (2013)</a>, <a href="https://doi.org/10.1038/ncomms12455" target="_blank">Kuhn et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">Fehér et al. (2026)</a>, and <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> pushed up <strong>perturbation-conditioned human plasticity / state-gated routes</strong>, and <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> plus <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> pushed up <strong>macro CSF / glymphatic support-state routes</strong>. What follows directly is that <strong>human evidence is layered across proxy classes</strong>, not a single near-direct route to current whole-brain maintenance-state. A second correction is also required: those rows are not all equally mature, routine, or deployment-ready.
</p>
<table>
<thead>
<tr>
<th>Human route</th>
<th>What it directly advances</th>
<th>What still remains latent</th>
<th>Claim ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Local human nanoscale ultrastructure</strong><br>Shapson-Coe et al. (2024)</td>
<td>A cubic-millimeter human cortical fragment reconstructed at nanoscale resolution with dense local cell, axon, glia, vascular, and synapse structure.</td>
<td>Living whole-brain dynamics, current synaptic efficacy, ongoing maintenance-state, and cross-brain generalization.</td>
<td><strong>Local human structural scaffold</strong>. We do not promote it to living whole-brain state capture.</td>
</tr>
<tr>
<td><strong>Regional synaptic-density PET atlas</strong><br>Johansen et al. (2024)</td>
<td>Atlas-level distribution of the synaptic marker SV2A across the living human brain, estimated through tracer-specific kinetic modeling or a validated simplified window.</td>
<td>Current synaptic efficacy, release probability, task-evoked momentary state change, synaptic-tag capture, and branch-local plasticity state.</td>
<td><strong>Regional synaptic-density proxy</strong>. We do not read it as a direct measurement of current synaptic function.</td>
</tr>
<tr>
<td><strong>Whole-brain MRSI metabolic similarity scaffold</strong><br>Lucchetti et al. (2025)</td>
<td>Parcel-level biochemical organization from whole-brain <sup>1</sup>H-MRSI metabolite profiles with within-subject metabolic similarity structure.</td>
<td>Current transcriptional controller, branch-local energetic reserve, cell-specific recovery logic, and local transmitter / glial microstate.</td>
<td><strong>Macro biochemical scaffold</strong>. It is not a local maintenance-state snapshot.</td>
</tr>
<tr>
<td><strong>Human energetic imaging (31P-MRS / dynamic DMRSI)</strong><br>Ren et al. (2015); Li et al. (2025)</td>
<td>ATP synthesis / pH and whole-brain glucose transport and metabolic-rate mapping in living humans.</td>
<td>Which dendritic branch lacks ATP reserve, where mitochondria are parked, which compartment is energetically fragile right now, and which fission / fusion state is active.</td>
<td><strong>Macro energetic proxy</strong>. It does not become branch-local mitochondrial ground truth.</td>
</tr>
<tr>
<td><strong>Human sodium MRI / ionic proxy</strong><br>Qian et al. (2012); Qian et al. (2025)</td>
<td>mm-class tissue sodium mapping in vivo and emerging mono- / bi-T<sub>2</sub> sodium separation under specialized acquisition.</td>
<td>Cell-specific chloride concentration, KCC2 / NKCC1 balance, extracellular K<sup>+</sup> / Ca<sup>2+</sup> / pH microdomains, local E<sub>GABA</sub>, and routine whole-brain intra- versus extracellular sodium partition.</td>
<td><strong>Macro ionic proxy</strong>. It is not direct ground truth of current chloride homeostasis.</td>
</tr>
<tr>
<td><strong>Human brain thermometry</strong><br>Rzechorzek et al. (2022)</td>
<td>4D macro thermal maps and daily human brain-temperature rhythms.</td>
<td>Cell-specific microtemperature, synapse-level heating burden, and local thermal controller state.</td>
<td><strong>Macro thermal proxy</strong>. It is not cell-specific thermal-state ground truth.</td>
</tr>
<tr>
<td><strong>Human myelin bilayer mapping (specialized proof-of-principle)</strong><br>Baadsvik et al. (2024)</td>
<td>Direct MRI access to the myelin bilayer at macro scale in living human brain.</td>
<td>Per-axon conduction controller, node / internode microgeometry, and local timing-state recovery.</td>
<td><strong>Macro myelin proxy</strong>. It is not full timing-state recovery.</td>
</tr>
<tr>
<td><strong>Human sleep-homeostasis / plasticity proxy</strong><br>Huber et al. (2013); Kuhn et al. (2016); Fehér et al. (2026)</td>
<td>Wake / sleep / nap manipulations that measurably shift TMS-EEG cortical excitability and PAS-like plasticity efficacy in living humans.</td>
<td>Which cell type, AIS / channel change, synapse, glial controller, or recovery controller produced the effect.</td>
<td><strong>Perturbation-conditioned maintenance proxy</strong>. It is not direct readout of the responsible excitability controller.</td>
</tr>
<tr>
<td><strong>Human state-gated perturbation proxy</strong><br>Zrenner et al. (2018)</td>
<td>State-conditioned causal evidence that EEG-defined excitability state changes the efficacy of TMS-induced plasticity.</td>
<td>AIS geometry, channel distribution, cell-specific allocation state, and long-horizon recovery controller.</td>
<td><strong>State-gated perturbation proxy</strong>. It is not direct measurement of the excitability mechanism itself.</td>
</tr>
<tr>
<td><strong>Human CSF mobility / sleep-linked clearance proxy</strong><br>Hirschler et al. (2025); Dagum et al. (2026)</td>
<td>In vivo CSF mobility mapping and sleep-related clearance evidence linking brain-to-plasma transport.</td>
<td>Cell-specific immune control, local synaptic maintenance, and moment-to-moment neural state.</td>
<td><strong>Macro support-state proxy</strong>. It is not a direct readout of local maintenance control.</td>
</tr>
<tr>
<td><strong>Still lacking a comparable in vivo whole-brain human route</strong></td>
<td>Current transcription / chromatin state, ECM / PNN gate state, branch-local proteostasis / synaptic-tag capture, current chloride set point, and branch-local mitochondrial positioning remain important state classes.</td>
<td>These layers still cannot be promoted from human evidence to comparable whole-brain in vivo ground truth on the basis of the reviewed measurement classes alone.</td>
<td><strong>Keep them explicitly latent</strong> or externally calibrated; do not auto-fill them from the proxy rows above.</td>
</tr>
</tbody>
</table>

<strong>Proxy class and maturity have to be logged separately</strong>
<p>
The key operational criticism is that the presence of a human proxy class does not by itself tell you how mature the route is. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> built an atlas from <strong>33 healthy participants</strong> calibrated against postmortem autoradiography. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> derived a metabolic similarity scaffold from <strong>51 healthy adolescents</strong> with an <strong>independent replication sample of 13</strong>, using five-metabolite <sup>1</sup>H-MRSI and a correlation-based construction. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> reported whole-brain metabolic-rate mapping in <strong>five healthy participants</strong> at <strong>7 T</strong> with custom dual-frequency coils and blood-input modeling. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> showed myelin-bilayer mapping in <strong>two healthy volunteers</strong> on high-performance hardware. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> introduced a specialized 7 T CSF-mobility sequence in <strong>24 healthy adults</strong>, while <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> relied on older-adult crossover cohorts, an <strong>investigational wearable</strong>, and a <strong>compartmental model</strong> with notable QC attrition. Therefore, this page now treats <strong>proxy class</strong> and <strong>operational maturity</strong> as separate metadata that both have to be stated before claim ceilings are interpreted.
</p>

<strong>Site rule for human proxy classes</strong>
<p>
On this site, human-side summaries must name the <strong>proxy class</strong> explicitly. ``Human evidence exists'' is too coarse. The summary has to tell the reader whether the result is a <strong>local structural scaffold</strong>, <strong>regional synaptic-density proxy</strong>, <strong>macro biochemical scaffold</strong>, <strong>perturbation-conditioned maintenance / state-gated perturbation proxy</strong>, <strong>macro energetic / ionic / thermal / myelin proxy</strong>, or <strong>macro support-state proxy</strong>. When the route is still specialized, model-dependent, or small-cohort, that maturity limit must be stated alongside the proxy class rather than left implicit.
</p>

<strong>Why this ladder matters operationally</strong>
<p>
The danger is not only philosophical overreach. If these rows are compressed into one sentence, readers can silently replace ``human proxy-rich evidence'' with ``human near-direct maintenance-state observation.'' This site does not allow that rephrasing. The missing layers above stay latent until a comparable whole-brain in vivo human route or an explicit external-calibration route is shown.
</p>

<h2>8. Proxy-rich human evidence still does not become state-complete by composition</h2>
<p>
A remaining weakness after separating <strong>proxy class</strong> and <strong>operational maturity</strong> was that a reader could still mentally add the strongest human rows together and conclude that the hidden-state problem is almost solved. The primary literature does not support that shortcut. The rows above live on different spatial units, time windows, and inference layers, and several of the strongest demonstrations are still specialized or model-heavy. The safe reading on this site is therefore not ``the proxies add up to completeness,'' but ``the proxies reduce different error terms and still leave a fusion problem.''
</p>
<table>
<thead>
<tr>
<th>Compositional shortcut to block</th>
<th>Why the cited literature does not support it</th>
<th>Operational correction on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>``Atlas + proxy = current individual state''</strong></td>
<td><a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> and <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> are atlas / cohort resources. They constrain regional organization and synaptic-density distribution, but they do not directly read one individual's current task-time state.</td>
<td>Write <strong>atlas</strong> or <strong>normative prior</strong> explicitly; do not phrase these rows as current-state measurement.</td>
</tr>
<tr>
<td><strong>``Several macro proxies = one local controller''</strong></td>
<td><a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a>, <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">Qian et al. (2025)</a>, and <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> constrain different macro energetic, thermal, ionic, or myelin variables. They do not identify branch-local ATP reserve, current chloride set point, or per-axon conduction control as one merged mechanism.</td>
<td>Keep local controllers explicit in the Observability Budget; do not auto-fill them from macro proxy coexistence.</td>
</tr>
<tr>
<td><strong>``Support-state proxy = direct maintenance controller''</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> constrain CSF mobility or brain-to-plasma clearance under explicit acquisition and model assumptions, not cell-specific immune control or synaptic maintenance logic.</td>
<td>Read them as <strong>support-state evidence</strong> only; leave local maintenance control latent unless another calibrated route closes it.</td>
</tr>
<tr>
<td><strong>``Cross-stack fusion adds only observables''</strong></td>
<td><a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a>, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> each depend on explicit quantification models, validated windows, or compartment assumptions. Fusion therefore combines model burdens as well as direct observables.</td>
<td>Log the <strong>fusion model</strong>, <strong>external calibration source</strong>, and <strong>abstention boundary</strong> separately instead of treating multimodal combination as self-justifying.</td>
</tr>
<tr>
<td><strong>``Different scales acquired somewhere imply same-subject completeness''</strong></td>
<td><a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> is local ex vivo nanoscale human cortex, whereas <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> and <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> are small-cohort specialized in vivo macro routes. The cited papers do not demonstrate same-subject, same-time, whole-brain cross-stack state identification.</td>
<td>Reserve stronger wording for studies that disclose <strong>same-subject co-registration</strong>, <strong>same-regime alignment</strong>, and <strong>externally validated cross-stack fusion</strong>.</td>
</tr>
</tbody>
</table>

<strong>Composition rule on this site</strong>
<p>
This site now treats <strong>proxy-rich human evidence</strong> as a real advance over a single proxy class, but still below <strong>same-subject, cross-stack, externally calibrated state identification</strong>. To move upward, a paper or benchmark package has to disclose co-registration scope, perturbation alignment, quantification models, external calibration, and what latent states remain unmatched. That ranking is an inference from the primary literature summarized above.
</p>

<h2>Practical rules arising from this criticism</h2>

<h4>Rule</h4>
<ul>
<li><strong>Write the measurement stack in the augmentation claim:</strong>Instead of saying "added transcriptomic label", distinguish between whole-brain atlas, patch-seq bridge, or same-brain link. </li>
<li><strong>Don't mix atlas / bridge / scaffold / local twin / proxy calibration:</strong>Fix which kind of advance is the same "advance". </li>
<li><strong>Don't make multimodal a synonym for state-complete:</strong>Include in the text what latent state still remains. </li>
<li><strong>In human-side summaries, name the proxy class:</strong>Do not compress local ultrastructure, synaptic-density PET, biochemical scaffold, perturbation-conditioned plasticity/state-gated perturbation routes, energetic / ionic / thermal / myelin / clearance routes into one direct route. </li>
<li><strong>Do not read proxy accumulation as automatic state-completeness:</strong>Cross-stack fusion still needs same-subject alignment, model disclosure, external calibration, and abstention boundaries.</li>
<li><strong>When filling in unobserved states, write ``estimated'': </strong>If threshold / gain / set point is auto-completed from cell type, write ``latent inference''. </li>
<li><strong>Do not promote BOLD / fNIRS amplitude to neural difference without hemodynamic audit:</strong>Write vascular-state / CVR calibration route or abstention explicitly. </li>
<li><strong>Prohibit expressions that exceed the claim ceiling:</strong>For example, do not write EM alone as emulation-complete, Patch-seq as whole-brain state-complete, pupil as transmitter ground truth, receptor atlas as current transmitter state, occupancy PET as whole-brain transmitter-state readout, or displacement PET as whole-brain neuromodulatory ground truth. </li>
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
<td><strong>mixed proxy / transmitter sensor / receptor atlas / occupancy PET / displacement PET</strong></td>
<td>cross-stack calibration, ligand / drug / challenge / dose disclosure, cross-state validation, and abstention boundary. </td>
<td>It becomes easier to distinguish coarse arousal covariate, local calibration, regional prior, exogenous target engagement, and challenge-limited release proxy. </td>
<td>Stop whole-brain transmitter-field ground truth and receptor-family-complete internal-state claims. </td>
</tr>
<tr>
<td><strong>human maintenance-state proxies</strong></td>
<td>class-labeled submission, external calibration route, cross-stack comparison, and abstention boundary. </td>
<td>It becomes easier to separate local scaffold, synaptic-density proxy, biochemical scaffold, perturbation-conditioned plasticity proxy, energetic / ionic / thermal / myelin / clearance proxy, and still-missing human routes. </td>
<td>Stop near-direct human maintenance-state and state-complete claims. </td>
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
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <em>NeuroImage</em>, 54(1), 369-379. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <em>Frontiers in Physiology</em>, 14, 1167148. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu, S., Tyler, L. K., Henson, R. N. A., Rowe, J. B., Cam-CAN, &amp; Tsvetanov, K. A. (2023). Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. <em>Neurobiology of Aging</em>, 121, 1-14. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Yucel, M. A. Y., Selb, J., Aasted, C. M. A., Petkov, M. P., Becerra, L., Borsook, D., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <em>Neurophotonics</em>, 2(3), 035005. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>Epp, S. M., Castrillon, G., Yuan, B., Andrews-Hanna, J., Preibisch, C., &amp; Riedl, V. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Lohani, S., Moberly, A. H., Benisty, H., et al. (2022). Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. <em>Nature Neuroscience</em>, 25(12), 1706-1713. <a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">doi:10.1038/s41593-022-01202-6</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <em>Nature Neuroscience</em>, 25(11), 1569-1581. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Goulas, A., Changeux, J.-P., Wagstyl, K., Amunts, K., Palomero-Gallagher, N., &amp; Hilgetag, C. C. (2021). The natural axis of transmitter receptor distribution in the human cerebral cortex. <em>PNAS</em>, 118(3), e2020574118. <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">doi:10.1073/pnas.2020574118</a></li>
<li>Naganawa, M., Li, S., Nabulsi, N., et al. (2021). First-in-human evaluation of <sup>18</sup>F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. <em>Journal of Nuclear Medicine</em>, 62(4), 561-567. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">doi:10.2967/jnumed.120.249144</a></li>
<li>Smart, K., Liu, H., Matuskey, D., et al. (2021). Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>, 41(5), 1067-1079. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">doi:10.1177/0271678X20946198</a></li>
<li>Johansen, A., Beliveau, V., Colliander, E., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <em>Journal of Neuroscience</em>, 44(33), e1750232024. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <em>Science</em>, 384(6696), eadk4858. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Lucchetti, F., C&eacute;l&eacute;reau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>, 16, 11344. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). <sup>31</sup>P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <em>NMR in Biomedicine</em>, 28(11), 1455-1462. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <em>PNAS Nexus</em>, 4(3), pgaf072. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Qian, Y., Zhao, T., Zheng, H., Weimer, J., &amp; Boada, F. E. (2012). High-resolution sodium imaging of human brain at 7 T. <em>Magnetic Resonance in Medicine</em>, 68(1), 227-233. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">doi:10.1002/mrm.23225</a></li>
<li>Qian, Y., Lin, Y. C., Chen, X., et al. (2025). Single-quantum sodium MRI at 3 T for separation of mono- and bi-T<sub>2</sub> sodium signals. <em>Scientific Reports</em>, 15, 27427. <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">doi:10.1038/s41598-025-07800-1</a></li>
<li>Rzechorzek, N. M., Thrippleton, M. J., Chappell, F. M., et al. (2022). A daily temperature rhythm in the human brain predicts survival after brain injury. <em>Brain</em>, 145(6), 2031-2048. <a href="https://doi.org/10.1093/brain/awab466" target="_blank">doi:10.1093/brain/awab466</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., Schildknecht, C. M., Ineichen, B. V., &amp; Pruessmann, K. P. (2024). Myelin bilayer mapping in the human brain in vivo. <em>Magnetic Resonance in Medicine</em>, 91(6), 2332-2344. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Huber, R., Mäki, H., Rosanova, M., Casarotto, S., Canali, P., Casali, A. G., Tononi, G., &amp; Massimini, M. (2013). Human cortical excitability increases with time awake. <em>Cerebral Cortex</em>, 23(2), 332-338. <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">doi:10.1093/cercor/bhs014</a></li>
<li>Kuhn, M., Wolf, E., Maier, J. G., Mainberger, F., Feige, B., Schmid, H., et al. (2016). Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. <em>Nature Communications</em>, 7, 12455. <a href="https://doi.org/10.1038/ncomms12455" target="_blank">doi:10.1038/ncomms12455</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <em>Brain Stimulation</em>, 11(2), 374-389. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Fehér, K. D., Henckaerts, P., Hirsch, V., Bucsenez, U., Kuhn, M., Maier, J. G., et al. (2026). A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. <em>NeuroImage</em>, 327, 121723. <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">doi:10.1016/j.neuroimage.2026.121723</a></li>
<li>Hirschler, L., Runderkamp, B. A. R., Decker, A., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <em>Nature Neuroscience</em>, 28(11), 2392-2401. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., Elbert, D. L., Giovangrandi, L., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <em>Nature Communications</em>, 17, 715. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Wong, D. F., Kuwabara, H., Hsu, D. J., et al. (2013). Determination of dopamine D<sub>2</sub> receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. <em>Psychopharmacology</em>, 229(2), 245-252. <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">doi:10.1007/s00213-013-3103-z</a></li>
<li>Koepp, M. J., Gunn, R. N., Lawrence, A. D., et al. (1998). Evidence for striatal dopamine release during a video game. <em>Nature</em>, 393(6682), 266-268. <a href="https://doi.org/10.1038/30498" target="_blank">doi:10.1038/30498</a></li>
<li>Lippert, R. N., Cremer, A. L., Edwin Thanarajah, S., et al. (2019). Time-dependent assessment of stimulus-evoked regional dopamine release. <em>Nature Communications</em>, 10, 336. <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">doi:10.1038/s41467-018-08143-4</a></li>
<li>Erritzoe, D., Ashok, A. H., Searle, G. E., et al. (2020). Serotonin release measured in the human brain: a PET study with [<sup>11</sup>C]CIMBI-36 and d-amphetamine challenge. <em>Neuropsychopharmacology</em>, 45(5), 804-810. <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">doi:10.1038/s41386-019-0567-5</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Communications</em>, 15, 3820. <a href="https://doi.org/10.1038/s41467-024-47838-5" target="_blank">doi:10.1038/s41467-024-47838-5</a></li>
</ol>
