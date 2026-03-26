# Wiki: observability and claim ceiling by measurement stack

> multimodal is not a synonym for ``seen everything''
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-27 / 位置づけ: Technical / natural science only

## このページの役割
This page is a wiki that fixes the ``upper claim limit for each measurement stack,'' which is often overlooked in WBE discussions. It's not enough to say that hidden state is important. Based on primary literature, we will explain what each of EEG/MEG/fMRI, spatial transcriptomics, Patch-seq, volume EM, same-brain functional connectomics, synaptic-density PET, mixed arousal proxy, local transmitter sensor, receptor atlas / PET, glia imaging, and human 1H-MRSI biochemical-similarity / 31P energetic-balance / deuterium metabolite-rate / ionic / thermal / myelin / clearance routes directly observes and what remains latent.

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
- Human 1H-MRSI biochemical similarity, 31P energetic balance, deuterium metabolite / rate, ionic, thermal, myelin, and clearance routes reduce different latent-state error terms and should not be summarized as one direct path to maintenance-state completeness.
- A real human proxy route may still calibrate only one bounded hidden-state family, so proxy class and operational maturity do not by themselves fix calibrator role.
- Same-subject or same-brain wording can solve specimen identity while still leaving state continuity unresolved across time gaps, regime changes, and tissue transformation.

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

<h3>4.5. Destructive ultrastructure still faces a preservation / registration / throughput wall</h3>
<p>
Another weakness that remained on this page was that <strong>volume EM</strong>, <strong>petascale</strong>, or <strong>same-brain</strong> could still be overread as if destructive ultrastructure had already solved native-state preservation, whole-brain scaling, and reconstruction quality in one move. That is too weak. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that conventional aldehyde fixation collapses extracellular space, that the fixation time course itself is not instantaneous, and that high-pressure freezing preserves extracellular space only in samples thinner than roughly <strong>200 μm</strong>. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> then showed that a rapidly preserved human sample can yield a remarkable nanoscale reconstruction, but still as a <strong>1.05 mm<sup>3</sup></strong> surgical fragment with <strong>1.8 PB</strong> raw data and <strong>326 days</strong> of imaging. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> showed that same-brain function plus EM is a sequential local pipeline rather than simultaneous state capture, and <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> showed that even the adult fly whole-brain frontier still depended on proofreading, thresholding, and substantial manual correction effort. What follows directly is that <strong>resolution alone does not erase preservation artifacts, local registration limits, or reconstruction burden</strong>.
</p>
<table>
<thead>
<tr>
<th>Wall</th>
<th>What the primary literature now supports</th>
<th>Site rule</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Preservation wall</strong></td>
<td>Fixation route changes what the ultrastructure looks like; preserving extracellular space and fine geometry requires an explicit preservation protocol and does not mean that live molecular or electrophysiological state was captured.</td>
<td>Do not read <strong>nanoscale</strong> or <strong>EM</strong> as automatic native-state preservation.</td>
</tr>
<tr>
<td><strong>Registration wall</strong></td>
<td>Same-brain function + EM is stronger than connectome-only, but it is still a sequential, local, and registration-limited route rather than same-time whole-brain state capture.</td>
<td>Do not read <strong>same-brain</strong> as <strong>same-time complete state</strong>.</td>
</tr>
<tr>
<td><strong>Throughput / proof wall</strong></td>
<td>Petascale imaging still implies long acquisition windows, sectioning/alignment risk, segmentation trade-offs, and nontrivial proofreading burden.</td>
<td>Do not read <strong>petascale</strong> as <strong>finished, error-free, or whole-brain-ready</strong>.</td>
</tr>
</tbody>
</table>

<strong>Operating rule for destructive ultrastructure</strong>
<p>
On this site, a destructive ultrastructure result is read first as a <strong>structural scaffold</strong> or <strong>local ex vivo scaffold</strong> unless it also discloses preservation route, live-to-fix window, registration scope, section-loss / alignment risk, segmentation / proofreading status, and omitted live-state families. That disclosure bundle is formalized in <a href="https://mind-upload.com/verification.html#destructive-structure-card">Verification: Destructive-Structure Route Card</a>.
</p>

<h3>4.6. EEG / MEG still face a visibility / inverse / validation wall</h3>
<p>
Another weakness that remained on this page was that <strong>source-localized</strong>, <strong>deep-source detectable</strong>, or <strong>intracranially validated</strong> could still be overread as if non-invasive field recordings had already crossed from macro observables into general internal-state recovery. That is too weak. Before any inverse solver runs, there is already a <strong>field-formation wall</strong>. <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a> quantified source-orientation sensitivity with realistic tissue boundaries and found that the median ratio between the least and most sensitive orientations was <strong>0.63 for EEG</strong> but only <strong>0.06 for MEG</strong>. <a href="https://doi.org/10.1002/hbm.20851" target="_blank">Ahlfors et al. (2010)</a> then showed that extended and distributed sources can cancel substantially at the surface. <a href="https://doi.org/10.1002/hbm.20571" target="_blank">Goldenholz et al. (2009)</a> showed that source extent and anatomy strongly change detectability, with mesial temporal source patches of about <strong>3 cm<sup>2</sup></strong> versus <strong>8 cm<sup>2</sup></strong> differing by roughly <strong>10 dB</strong> in SNR. <a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al. (2021)</a> further showed that ignoring the <strong>CSF compartment</strong> overestimates EEG SNR and that cortical / subcortical sensitivity depends jointly on depth and orientation. Only after that upstream filter do benchmark papers become readable. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a> created the first open human ground-truth benchmark by combining <strong>256-channel HD-EEG</strong> with precisely known intracerebral stimulation sites, but they also stated explicitly that stimulation artifacts are <strong>non-physiological</strong> and that spatial sampling remains anatomically clustered. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> then evaluated <strong>3,619</strong> known stimulation locations in <strong>11 patients</strong> with simultaneous SEEG and scalp EEG and found mean localization errors ranging from <strong>10.3 to 26 mm</strong>, worsening with source depth and lower skull conductivity. <a href="https://doi.org/10.1016/j.jneumeth.2024.110193" target="_blank">Zauli et al. (2024)</a> showed that hidden interictal discharges not visible on single-trial scalp HD-EEG can be uncovered with simultaneous SEEG-triggered averaging, but the resulting ESI still remained <strong>method- and parameter-dependent</strong> with localization accuracy of only about <strong>2 cm</strong>. <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> reported that simultaneous HD-EEG/SEEG ictal ESI localizes better than interictal ESI, yet still at <strong>14.07 ± 4.62 mm</strong> versus <strong>17.38 ± 4.16 mm</strong>, with accuracy strongly influenced by source depth and spike power. Finally, <a href="https://doi.org/10.1038/s41467-019-08665-5" target="_blank">Pizzo et al. (2019)</a> showed that MEG can detect direct hippocampal or amygdalar contributions under simultaneous intracranial validation, but only after blind source separation because the deep contribution reaching the surface was <strong>small but significant</strong> rather than dominating the sensor signal. What follows directly is that <strong>EEG / MEG can gain conditional access to some deeper generators, but they still do not collapse field formation, the inverse problem, or general deep-state observability</strong>.
</p>
<table>
<thead>
<tr>
<th>Wall</th>
<th>What the primary literature now supports</th>
<th>Site rule</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Field-formation wall</strong></td>
<td>Whether a source reaches the scalp with usable SNR already depends on its orientation, depth, cortical folding, source extent, cancellation profile, and the tissue compartments included in the head model.</td>
<td>Do not read <strong>high-density</strong>, <strong>deep detectable</strong>, or <strong>not seen at the scalp</strong> without naming the target source class, expected extent, cancellation risk, and CSF / conductivity assumptions.</td>
</tr>
<tr>
<td><strong>Visibility wall</strong></td>
<td>Deep or low-power events can be absent at the scalp in single trials and may only appear after intracranial timing information, averaging, or special source-separation steps.</td>
<td>Do not read <strong>scalp-invisible</strong> as <strong>nonexistent</strong>, but do not read <strong>recoverable under SEEG guidance</strong> as <strong>routinely visible non-invasively</strong> either.</td>
</tr>
<tr>
<td><strong>Inverse / model wall</strong></td>
<td>Localization error changes with source depth, skull conductivity, forward model, and chosen inverse method; better fit does not imply unique recovery of the underlying neural state.</td>
<td>Do not read <strong>source-localized</strong> as <strong>unique internal-state reconstruction</strong>; always disclose the head model, conductivity assumptions, and abstention conditions.</td>
</tr>
<tr>
<td><strong>Validation wall</strong></td>
<td>Current direct-validation routes mostly come from intracranial stimulation, epilepsy discharges, or simultaneous SEEG/MEG recordings, which answer conditional localization questions rather than physiological whole-brain cognition in healthy humans.</td>
<td>Do not promote <strong>intracranially validated epilepsy benchmarks</strong> to <strong>general-purpose whole-brain state readout</strong>.</td>
</tr>
</tbody>
</table>

<strong>Operating rule for EEG / MEG</strong>
<p>
On this site, EEG / MEG are read first as <strong>macro field observables</strong>. Even when deeper sources become conditionally detectable, the claim ceiling stays bounded by field formation, synchrony, source depth, head-model assumptions, and the exact validation route. To argue above macro state tracking or weak L2, a result now has to disclose whether the support comes from <strong>field-formation / sensitivity analysis</strong>, <strong>stimulation benchmark</strong>, <strong>simultaneous intracranial recording</strong>, <strong>task-only inference</strong>, or <strong>model transfer</strong>, plus what deep or cell-scale state variables remain latent.
</p>

<h3>5. Hemodynamic stacks also observe through a vascular transfer state</h3>
<p>
The weak point that needed another pass was that this page already called fMRI a <strong>hemodynamic proxy</strong>, but still left too much room for the reader to translate a BOLD amplitude difference directly into a neural difference. That was too weak. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> showed that inter-subject differences in CBF and CBV contribute to BOLD reactivity and that breath-hold-derived vascular-reactivity covariates improve group analyses. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> showed that task BOLD magnitude corresponds strongly to hypercapnia-based CVR across multiple cortical regions. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> showed that baseline CBF partly explains age-related components of multiple-demand-network BOLD responses. <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al. (2019)</a> showed that widespread fMRI changes can co-occur with EEG K-complexes and sympathetic-linked vascular-tone changes, and <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed across multiple datasets that a major low-frequency global fMRI mode cofluctuates with EEG and multiple autonomic signals. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> then showed that about <strong>40%</strong> of task-responsive voxels can display oxygen-metabolism changes opposite in sign to the BOLD response. What follows directly from this is that <strong>hemodynamic stacks are limited not only by unobserved neural state, but also by unobserved vascular transfer state and autonomic-body coupling</strong>.
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
PET-based proxy classes are not readable from the modality label alone. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a> showed that human SV2A PET quantification depends on the tracer, arterial-versus-reference route, compartment model, and named scan window. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> then built a healthy-human synaptic-density atlas, <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">Shatalina et al. (2024)</a> linked [<sup>11</sup>C]UCB-J DVRcs to task-related activity and cognition in healthy adults, <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">Smart et al. (2021)</a> showed that [<sup>11</sup>C]UCB-J binding measures remain unchanged during brief functional activation even when tracer influx rises with blood flow, and <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">Holmes et al. (2022)</a> found no measurable overall SV2A change 24 h after ketamine despite symptom improvement. Those papers do not answer the same question. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> built a receptor atlas by collating PET data from more than 1,200 healthy individuals, so the resulting map is a normative chemoarchitectural prior rather than an individual's current transmitter state. <a href="https://doi.org/10.1007/s00213-013-3103-z" target="_blank">Wong et al. (2013)</a> quantified occupancy for an administered antipsychotic, while <a href="https://doi.org/10.1038/30498" target="_blank">Koepp et al. (1998)</a>, <a href="https://doi.org/10.1038/s41467-018-08143-4" target="_blank">Lippert et al. (2019)</a>, and <a href="https://doi.org/10.1038/s41386-019-0567-5" target="_blank">Erritzoe et al. (2020)</a> used challenge-linked binding changes as displacement-based release proxies. Therefore, on this site, PET-based routes must name the tracer, occupancy-versus-displacement design, challenge or administered drug plus dose when applicable, quantification model or validated window, anatomy / partial-volume handling when relevant, and the comparison family they actually instantiate before their claim ceiling is interpreted. The full SV2A-specific checklist now lives in <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state#sv2a-route-card">Wiki: SV2A / synaptic-density PET route card</a>.
</p>

<p>
The same caution extends to glia. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> showed that local neurotransmitter inputs are minute-long encoded into broad astrocyte networks. That is a real advance, but it is still a slow-state / support-state route, not an automatic shortcut to whole-brain internal-state completeness.
</p>

<h2>7. Human maintenance-state routes also form a ladder</h2>
<p>
Another weakness that remained on this page was that it separated generic measurement stacks while still leaving recent <strong>human maintenance-state evidence</strong> too easy to compress into one sentence such as ``human in vivo observability is getting close.'' That is too weak. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> pushed up <strong>local human nanoscale ultrastructure</strong>, <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> pushed up a <strong>regional synaptic-density atlas</strong>, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> pushed up a <strong>whole-brain biochemical scaffold</strong>, <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> pushed up <strong>macro energetic routes</strong>, <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> and <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">Qian et al. (2025)</a> pushed up <strong>macro ionic routes</strong>, <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a> pushed up <strong>macro thermal routes</strong>, <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> pushed up <strong>macro myelin mapping</strong>, <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">Huber et al. (2013)</a>, <a href="https://doi.org/10.1038/ncomms12455" target="_blank">Kuhn et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">Fehér et al. (2026)</a>, and <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> pushed up <strong>perturbation-conditioned human plasticity / state-gated routes</strong>, and <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> plus <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> pushed up <strong>macro CSF / glymphatic support-state routes</strong>. What follows directly is that <strong>human evidence is layered across proxy classes</strong>, not a single near-direct route to current whole-brain maintenance-state. A second correction is also required: those rows are not all equally mature, routine, or deployment-ready, and they do not safely calibrate the same hidden-state family.
</p>
<table>
<thead>
<tr>
<th>Human route</th>
<th>Proxy class on this site</th>
<th>Operational maturity / burden</th>
<th>Safe calibrator role on this site</th>
<th>What still remains latent</th>
<th>Claim ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Local human nanoscale ultrastructure</strong><br>Shapson-Coe et al. (2024)</td>
<td><strong>Local ex vivo structural scaffold</strong></td>
<td>Destructive surgical-fragment route; not repeatable living-human acquisition.</td>
<td>Structural scaffold only.</td>
<td>Living whole-brain dynamics, current synaptic efficacy, ongoing maintenance-state, and cross-brain generalization.</td>
<td><strong>Local human structural scaffold</strong>. We do not promote it to living whole-brain state capture.</td>
</tr>
<tr>
<td><strong>Regional synaptic-density PET atlas</strong><br>Johansen et al. (2024)</td>
<td><strong>Regional synaptic-density proxy</strong></td>
<td>Healthy-cohort atlas; tracer- and quantification-dependent.</td>
<td>Bounded synaptic-density prior.</td>
<td>Current synaptic efficacy, release probability, task-evoked momentary state change, synaptic-tag capture, and branch-local plasticity state.</td>
<td><strong>Regional synaptic-density proxy</strong>. We do not read it as a direct measurement of current synaptic function.</td>
</tr>
<tr>
<td><strong>Whole-brain 1H-MRSI metabolic similarity scaffold</strong><br>Lucchetti et al. (2025)</td>
<td><strong>Parcel-level 1H-MRSI biochemical similarity scaffold</strong></td>
<td>Whole-brain cohort mapping with replication, but still a static five-metabolite similarity route.</td>
<td>Bounded 1H-MRSI biochemical-organization scaffold.</td>
<td>Current transcriptional controller, branch-local energetic reserve, cell-specific recovery logic, and local transmitter / glial microstate.</td>
<td><strong>Macro 1H-MRSI biochemical scaffold</strong>. It is not a local maintenance-state snapshot.</td>
</tr>
<tr>
<td><strong>Human 31P-MRS energetic-balance route</strong><br>Ren et al. (2015)</td>
<td><strong>Macro 31P energetic-balance proxy</strong></td>
<td>Healthy resting cohort of 12 with ATP-synthesis, phosphorus-metabolite, pH, and relaxation estimates, but not a spatially fine compartment-control readout.</td>
<td>Bounded phosphorus-energetic balance proxy.</td>
<td>Which dendritic branch lacks ATP reserve, where mitochondria are parked, which compartment is energetically fragile right now, and which fission / fusion state is active.</td>
<td><strong>Macro 31P energetic-balance proxy</strong>. It does not become branch-local mitochondrial ground truth.</td>
</tr>
<tr>
<td><strong>Human deuterium metabolite / rate imaging</strong><br>Li et al. (2025); Karkouri et al. (2026)</td>
<td><strong>Macro deuterium metabolite / kinetic-rate proxy</strong></td>
<td>Specialized 7 T deuterium imaging with custom hardware or advanced modeling; current human evidence remains small-cohort and high-burden.</td>
<td>Bounded deuterium metabolite / energetic-rate proxy.</td>
<td>Which dendritic branch lacks ATP reserve, where mitochondria are parked, which compartment is energetically fragile right now, and which fission / fusion state is active.</td>
<td><strong>Macro deuterium metabolite / rate proxy</strong>. It does not become branch-local mitochondrial ground truth.</td>
</tr>
<tr>
<td><strong>Human sodium MRI / ionic proxy</strong><br>Qian et al. (2012); Qian et al. (2025)</td>
<td><strong>Macro ionic proxy</strong></td>
<td>Specialized acquisition with emerging compartment-sensitive extensions rather than routine controller readout.</td>
<td>Bounded ionic-burden proxy.</td>
<td>Cell-specific chloride concentration, KCC2 / NKCC1 balance, extracellular K<sup>+</sup> / Ca<sup>2+</sup> / pH microdomains, local E<sub>GABA</sub>, and routine whole-brain intra- versus extracellular sodium partition.</td>
<td><strong>Macro ionic proxy</strong>. It is not direct ground truth of current chloride homeostasis.</td>
</tr>
<tr>
<td><strong>Human brain thermometry</strong><br>Rzechorzek et al. (2022)</td>
<td><strong>Macro thermal proxy</strong></td>
<td>Living-human macro mapping route, but not a local thermal-controller assay.</td>
<td>Bounded thermal-burden proxy.</td>
<td>Cell-specific microtemperature, synapse-level heating burden, and local thermal controller state.</td>
<td><strong>Macro thermal proxy</strong>. It is not cell-specific thermal-state ground truth.</td>
</tr>
<tr>
<td><strong>Human myelin bilayer mapping (specialized proof-of-principle)</strong><br>Baadsvik et al. (2024)</td>
<td><strong>Macro myelin proxy</strong></td>
<td>Proof-of-principle in two healthy volunteers on specialized high-performance hardware.</td>
<td>Bounded myelin / timing-support proxy.</td>
<td>Per-axon conduction controller, node / internode microgeometry, and local timing-state recovery.</td>
<td><strong>Macro myelin proxy</strong>. It is not full timing-state recovery.</td>
</tr>
<tr>
<td><strong>Human sleep-homeostasis / plasticity proxy</strong><br>Huber et al. (2013); Kuhn et al. (2016); Fehér et al. (2026)</td>
<td><strong>Perturbation-conditioned maintenance proxy</strong></td>
<td>Intervention-backed human route, but still controller-indirect and regime-limited.</td>
<td>Bounded excitability / plasticity-support proxy.</td>
<td>Which cell type, AIS / channel change, synapse, glial controller, or recovery controller produced the effect.</td>
<td><strong>Perturbation-conditioned maintenance proxy</strong>. It is not direct readout of the responsible excitability controller.</td>
</tr>
<tr>
<td><strong>Human state-gated perturbation proxy</strong><br>Zrenner et al. (2018)</td>
<td><strong>State-gated perturbation proxy</strong></td>
<td>Operationally real closed-loop human route, but still mechanism-indirect.</td>
<td>Bounded state-gated excitability proxy.</td>
<td>AIS geometry, channel distribution, cell-specific allocation state, and long-horizon recovery controller.</td>
<td><strong>State-gated perturbation proxy</strong>. It is not direct measurement of the excitability mechanism itself.</td>
</tr>
<tr>
<td><strong>Human CSF mobility / sleep-linked clearance proxy</strong><br>Hirschler et al. (2025); Dagum et al. (2026)</td>
<td><strong>Macro support-state proxy</strong></td>
<td>Specialized MRI or device- and model-heavy biomarker-efflux inference.</td>
<td>Bounded clearance-support proxy.</td>
<td>Cell-specific immune control, local synaptic maintenance, and moment-to-moment neural state.</td>
<td><strong>Macro support-state proxy</strong>. It is not a direct readout of local maintenance control.</td>
</tr>
<tr>
<td><strong>Still lacking a comparable in vivo whole-brain human route</strong></td>
<td><strong>Still explicitly latent</strong></td>
<td>No comparable living-human whole-brain route in the reviewed stack bundle.</td>
<td>No safe calibrator role yet.</td>
<td>These layers still cannot be promoted from human evidence to comparable whole-brain in vivo ground truth on the basis of the reviewed measurement classes alone.</td>
<td><strong>Keep them explicitly latent</strong> or externally calibrated; do not auto-fill them from the proxy rows above.</td>
</tr>
</tbody>
</table>

<strong>Proxy class, operational maturity, and calibrator role have to be logged separately</strong>
<p>
The key operational criticism is that a route can be real without being broad. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> built an atlas from <strong>33 healthy participants</strong> calibrated against postmortem autoradiography, but that still calibrates a <strong>synaptic-density prior</strong> rather than task-time synaptic efficacy. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> derived a <strong>five-metabolite similarity scaffold</strong> from <strong>51 healthy adolescents</strong> with an <strong>independent replication sample of 13</strong>, but that still calibrates a <strong>biochemical organization scaffold</strong> rather than an energetic controller. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> measured <strong>ATP synthesis, phosphorus metabolites, and pH</strong> in <strong>12 healthy participants</strong>, which calibrates only a <strong>bounded energetic-balance proxy</strong>. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> and <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a> reported deuterium metabolite / rate maps at <strong>7 T</strong> with small cohorts and high acquisition-model burden, which is real but still calibrates only a <strong>bounded deuterium energetic-rate proxy</strong>. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> showed myelin-bilayer mapping in <strong>two healthy volunteers</strong> on specialized hardware, while <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> constrain <strong>support-state</strong> rather than cell-specific maintenance control. Therefore, this page now treats <strong>proxy class</strong>, <strong>operational maturity</strong>, and <strong>safe calibrator role</strong> as separate metadata that all have to be stated before claim ceilings are interpreted.
</p>

<strong>Spectroscopy rows also split by quantity type and model burden</strong>
<p>
The spectroscopy rows cannot be read as one proxy family. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> constrained <strong>parcel-level correlation structure</strong> across five metabolites, <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> constrained <strong>ATP synthesis / phosphorus-metabolite balance / pH</strong>, and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> plus <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a> constrained <strong>deuterated metabolite concentrations and kinetic rates</strong>. Even within <sup>1</sup>H-MRSI mapping, <a href="https://doi.org/10.1002/brb3.1852" target="_blank">Bhogal et al. (2020)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2022.119574" target="_blank">Wright et al. (2022)</a>, <a href="https://doi.org/10.1148/radiol.232401" target="_blank">Baboli et al. (2024)</a>, and <a href="https://doi.org/10.1109/TBME.2025.3572448" target="_blank">Guo et al. (2025)</a> show that lipid suppression, tissue-fraction correction, water / relaxation modeling, ghosting, aliasing, and low-SNR handling materially shape the inferred maps. Therefore, this site does not allow ``human spectroscopy evidence'' as a single proxy label. The quantity type, cohort burden, hardware burden, and model burden all have to be named before the claim ceiling is read.
</p>

<strong>Site rule for human proxy classes</strong>
<p>
On this site, human-side summaries must name the <strong>proxy class</strong> explicitly. ``Human evidence exists'' is too coarse. The summary has to tell the reader whether the result is a <strong>local structural scaffold</strong>, <strong>regional synaptic-density proxy</strong>, <strong>macro 1H-MRSI biochemical similarity scaffold</strong>, <strong>macro 31P energetic-balance proxy</strong>, <strong>macro deuterium metabolite / rate proxy</strong>, <strong>perturbation-conditioned maintenance / state-gated perturbation proxy</strong>, <strong>quantity-defined macro ionic / thermal / myelin proxy family</strong>, or <strong>macro support-state proxy</strong>. When the route is still specialized, model-dependent, or small-cohort, that maturity limit must be stated alongside the proxy class. And when the route calibrates only one bounded hidden-state family, that <strong>calibrator role</strong> must be written explicitly rather than inherited from the modality label.
</p>

<strong>Same-subject still does not solve the bridge by itself</strong>
<p>
One more shortcut remained too easy on this page: to read <strong>same subject</strong> or <strong>same brain</strong> as if several human rows had already become one state sample. The primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that preservation route changes extracellular-space retention and native geometry, <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> remained a rapidly preserved local surgical fragment rather than a living whole-brain route, and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> remained a sequential same-brain pipeline rather than same-time capture. Therefore, if a human proxy bundle crosses live and ex vivo or separated physiological regimes, this site now asks for a <a href="https://mind-upload.com/verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> that names elapsed time, regime continuity, coordinate-transfer burden, and residual drift ceiling before same-state language is allowed.
</p>

<strong>Why this ladder matters operationally</strong>
<p>
The danger is not only philosophical overreach. If these rows are compressed into one sentence, readers can silently replace ``human proxy-rich evidence'' with ``human near-direct maintenance-state observation.'' This site does not allow that rephrasing. The missing layers above stay latent until a comparable whole-brain in vivo human route or an explicit external-calibration route is shown.
</p>

<h2>8. Proxy-rich human evidence still does not become state-complete by composition</h2>
<p>
A remaining weakness after separating <strong>proxy class</strong>, <strong>operational maturity</strong>, and <strong>calibrator role</strong> was that a reader could still mentally add the strongest human rows together and conclude that the hidden-state problem is almost solved. The primary literature does not support that shortcut. The rows above live on different spatial units, time windows, and inference layers, and several of the strongest demonstrations are still specialized or model-heavy. The safe reading on this site is therefore not ``the proxies add up to completeness,'' but ``the proxies reduce different error terms and still leave a fusion problem.''
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
<td><a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a> made the model burden in EEG-fMRI fusion explicit, while <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> and <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed that simultaneous multimodal recordings can carry both common and divergent structure across modalities. Fusion therefore combines model burdens and mismatch risks as well as direct observables.</td>
<td>Log the <strong>fusion model</strong>, <strong>external calibration source</strong>, and <strong>abstention boundary</strong> separately instead of treating multimodal combination as self-justifying; on this site that package is the <a href="https://mind-upload.com/verification.html#fusion-card">Fusion Card</a>.</td>
</tr>
<tr>
<td><strong>``Different scales acquired somewhere imply same-subject completeness''</strong></td>
<td><a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> is local ex vivo nanoscale human cortex, whereas <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> and <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> are small-cohort specialized in vivo macro routes. The cited papers do not demonstrate same-subject, same-time, whole-brain cross-stack state identification.</td>
<td>Reserve stronger wording for studies that disclose <strong>same-subject co-registration</strong>, <strong>same-regime alignment</strong>, and <strong>externally validated cross-stack fusion</strong>.</td>
</tr>
<tr>
<td><strong>``Same-subject sequential pipeline = same-state multistack sample''</strong></td>
<td><a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> showed that preservation route changes geometry, <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> remained a local ex vivo fragment, and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> remained a sequential same-brain workflow rather than same-time capture. The cited papers do not show that specimen identity alone closes time, regime, or registration drift.</td>
<td>Attach a <strong>State-Continuity Bridge Card</strong> that names elapsed time, regime continuity, coordinate transfer, and residual drift ceiling before promoting the bundle above proxy-rich evidence.</td>
</tr>
</tbody>
</table>

<strong>Composition rule on this site</strong>
<p>
This site now treats <strong>proxy-rich human evidence</strong> as a real advance over a single proxy class, but still below <strong>same-subject, cross-stack, externally calibrated state identification</strong>. To move upward, a paper or benchmark package has to disclose co-registration scope, perturbation alignment, clock / lag audit, quantification models, external calibration, and what latent states remain unmatched. If the bridge is sequential across live and ex vivo or across separated physiological regimes, it also has to disclose elapsed time, regime continuity, coordinate transfer, and residual drift ceiling through the <a href="https://mind-upload.com/verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a>. On this site, multimodal combination itself is formalized as the <a href="https://mind-upload.com/verification.html#fusion-card">Fusion Card</a>. That ranking is an inference from the primary literature summarized above.
</p>

<h2>Practical rules arising from this criticism</h2>

<h4>Rule</h4>
<ul>
<li><strong>Write the measurement stack in the augmentation claim:</strong>Instead of saying "added transcriptomic label", distinguish between whole-brain atlas, patch-seq bridge, or same-brain link. </li>
<li><strong>Don't mix atlas / bridge / scaffold / local twin / proxy calibration:</strong>Fix which kind of advance is the same "advance". </li>
<li><strong>Don't make multimodal a synonym for state-complete:</strong>Include in the text what latent state still remains. </li>
<li><strong>In human-side summaries, name proxy class, operational maturity, and calibrator role:</strong>Do not compress local ultrastructure, synaptic-density PET, biochemical scaffold, perturbation-conditioned plasticity/state-gated perturbation routes, energetic / ionic / thermal / myelin / clearance routes into one direct route. </li>
<li><strong>Do not read proxy accumulation as automatic state-completeness:</strong>Cross-stack fusion still needs same-subject alignment, model disclosure, external calibration, and abstention boundaries.</li>
<li><strong>Do not read same-subject wording as same-state when the bridge is sequential:</strong>Require elapsed time, regime continuity, coordinate transfer, and residual drift disclosure. </li>
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
<td>class-labeled submission, calibrator-role disclosure, external calibration route, cross-stack comparison, and bridge disclosure when acquisition is sequential. </td>
<td>It becomes easier to separate local scaffold, synaptic-density proxy, biochemical scaffold, perturbation-conditioned plasticity proxy, energetic / ionic / thermal / myelin / clearance proxy, the bounded hidden-state family each route safely calibrates, and still-missing human routes. </td>
<td>Stop near-direct human maintenance-state and state-complete claims. </td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124-138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <em>Cell Reports Methods</em>, 3(7), 100520. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <em>Nature</em>, 624, 317-332. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435-447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497-505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Ahlfors, S. P., Han, J., Belliveau, J. W., &amp; H&auml;m&auml;l&auml;inen, M. S. (2010). Sensitivity of MEG and EEG to source orientation. <em>Brain Topography</em>, 23(3), 227-232. <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">doi:10.1007/s10548-010-0154-x</a></li>
<li>Ahlfors, S. P., Han, J., Lin, F.-H., Witzel, T., Belliveau, J. W., H&auml;m&auml;l&auml;inen, M. S., &amp; Halgren, E. (2010). Cancellation of EEG and MEG signals generated by extended and distributed sources. <em>Human Brain Mapping</em>, 31(1), 140-149. <a href="https://doi.org/10.1002/hbm.20851" target="_blank">doi:10.1002/hbm.20851</a></li>
<li>Goldenholz, D. M., Ahlfors, S. P., H&auml;m&auml;l&auml;inen, M. S., Sharon, D., Ishitobi, M., Vaina, L. M., &amp; Stufflebeam, S. M. (2009). Mapping the signal-to-noise-ratios of cortical sources in magnetoencephalography and electroencephalography. <em>Human Brain Mapping</em>, 30(4), 1077-1086. <a href="https://doi.org/10.1002/hbm.20571" target="_blank">doi:10.1002/hbm.20571</a></li>
<li>Piastra, M. C., N&uuml;&szlig;ing, A., Vorwerk, J., Clerc, M., Engwer, C., &amp; Wolters, C. H. (2021). A comprehensive study on electroencephalography and magnetoencephalography sensitivity to cortical and subcortical sources. <em>Human Brain Mapping</em>, 42(4), 978-992. <a href="https://doi.org/10.1002/hbm.25272" target="_blank">doi:10.1002/hbm.25272</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Rampp, S., Wehner, T., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation. <em>Brain Communications</em>, 5(1), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Pizzo, F., Roehri, N., Medina Villalon, S., et al. (2019). Deep brain activities can be detected with magnetoencephalography. <em>Nature Communications</em>, 10, 971. <a href="https://doi.org/10.1038/s41467-019-08665-5" target="_blank">doi:10.1038/s41467-019-08665-5</a></li>
<li>Zauli, F. M., Del Vecchio, M., Pigorini, A., et al. (2024). Localizing hidden Interictal Epileptiform Discharges with simultaneous intracerebral and scalp high-density EEG recordings. <em>Journal of Neuroscience Methods</em>, 409, 110193. <a href="https://doi.org/10.1016/j.jneumeth.2024.110193" target="_blank">doi:10.1016/j.jneumeth.2024.110193</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <em>NeuroImage</em>, 54(1), 369-379. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <em>Frontiers in Physiology</em>, 14, 1167148. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu, S., Tyler, L. K., Henson, R. N. A., Rowe, J. B., Cam-CAN, &amp; Tsvetanov, K. A. (2023). Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. <em>Neurobiology of Aging</em>, 121, 1-14. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Özbay, P. S., Chang, C., Picchioni, D., et al. (2019). Sympathetic activity contributes to the fMRI signal. <em>Communications Biology</em>, 2, 421. <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Yucel, M. A. Y., Selb, J., Aasted, C. M. A., Petkov, M. P., Becerra, L., Borsook, D., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <em>Neurophotonics</em>, 2(3), 035005. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>Bolt, T., Wang, S., Nomi, J. S., et al. (2025). Autonomic physiological coupling of the global fMRI signal. <em>Nature Neuroscience</em>, 28, 1327-1335. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Epp, S. M., Castrillon, G., Yuan, B., Andrews-Hanna, J., Preibisch, C., &amp; Riedl, V. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Lohani, S., Moberly, A. H., Benisty, H., et al. (2022). Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. <em>Nature Neuroscience</em>, 25(12), 1706-1713. <a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">doi:10.1038/s41593-022-01202-6</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <em>Nature Neuroscience</em>, 25(11), 1569-1581. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Goulas, A., Changeux, J.-P., Wagstyl, K., Amunts, K., Palomero-Gallagher, N., &amp; Hilgetag, C. C. (2021). The natural axis of transmitter receptor distribution in the human cerebral cortex. <em>PNAS</em>, 118(3), e2020574118. <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">doi:10.1073/pnas.2020574118</a></li>
<li>Naganawa, M., Li, S., Nabulsi, N., et al. (2021). First-in-human evaluation of <sup>18</sup>F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. <em>Journal of Nuclear Medicine</em>, 62(4), 561-567. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">doi:10.2967/jnumed.120.249144</a></li>
<li>Smart, K., Liu, H., Matuskey, D., et al. (2021). Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>, 41(5), 1067-1079. <a href="https://doi.org/10.1177/0271678X20946198" target="_blank">doi:10.1177/0271678X20946198</a></li>
<li>Johansen, A., Beliveau, V., Colliander, E., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <em>Journal of Neuroscience</em>, 44(33), e1750232024. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Shatalina, E., Onwordi, E. C., Whitehurst, T., et al. (2024). The relationship between SV2A levels, neural activity, and cognitive function in healthy humans: A [<sup>11</sup>C]UCB-J PET and fMRI study. <em>Imaging Neuroscience</em>, 2, 1-16. <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">doi:10.1162/imag_a_00190</a></li>
<li>Holmes, S. E., Finnema, S. J., Naganawa, M., et al. (2022). Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. <em>Molecular Psychiatry</em>, 27(4), 2273-2281. <a href="https://doi.org/10.1038/s41380-022-01465-2" target="_blank">doi:10.1038/s41380-022-01465-2</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <em>Science</em>, 384(6696), eadk4858. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., Medine, D., Boulay, C., Grivich, M. I., Artoni, F., Mullen, T., Delorme, A., &amp; Makeig, S. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H., Jafarian, A., Zeidman, P., Litvak, V., Razi, A., Garrido, M., Friston, K., &amp; Daunizeau, J. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <em>NeuroImage</em>, 211, 116595. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., Catana, C., Polimeni, J. R., Fan, J., Droppa, K. S., Patel, R., Wey, H.-Y., Chang, C., Manoach, D. S., Price, J. C., Sander, C. Y., &amp; Rosen, B. R. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Lucchetti, F., C&eacute;l&eacute;reau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>, 16, 11344. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). <sup>31</sup>P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <em>NMR in Biomedicine</em>, 28(11), 1455-1462. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Bhogal, A. A., Broeders, T. A. A., Morsinkhof, L., et al. (2020). Lipid-suppressed and tissue-fraction corrected metabolic distributions in human central brain structures using 2D <sup>1</sup>H magnetic resonance spectroscopic imaging at 7 T. <em>Brain and Behavior</em>, 10(10), e01852. <a href="https://doi.org/10.1002/brb3.1852" target="_blank">doi:10.1002/brb3.1852</a></li>
<li>Wright, A. M., Murali-Manohar, S., &amp; Henning, A. (2022). Quantitative T<sub>1</sub>-relaxation corrected metabolite mapping of 12 metabolites in the human brain at 9.4 T. <em>NeuroImage</em>, 261, 119574. <a href="https://doi.org/10.1016/j.neuroimage.2022.119574" target="_blank">doi:10.1016/j.neuroimage.2022.119574</a></li>
<li>Baboli, M., Wang, F., Dong, Z., et al. (2024). Absolute Metabolite Quantification in Individuals with Glioma and Healthy Individuals Using Whole-Brain Three-dimensional MR Spectroscopic and Echo-planar Time-resolved Imaging. <em>Radiology</em>, 311(3), e232401. <a href="https://doi.org/10.1148/radiol.232401" target="_blank">doi:10.1148/radiol.232401</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <em>PNAS Nexus</em>, 4(3), pgaf072. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Guo, R., Bogner, W., Heckova, E., et al. (2025). High-resolution whole-brain metabolic imaging using accelerated free induction decay MR spectroscopic imaging and a dual-branch super-resolution network. <em>IEEE Transactions on Biomedical Engineering</em>. <a href="https://doi.org/10.1109/TBME.2025.3572448" target="_blank">doi:10.1109/TBME.2025.3572448</a></li>
<li>Karkouri, J., Deelchand, D. K., Van de Moortele, P.-F., et al. (2026). Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. <em>Magnetic Resonance in Medicine</em>. <a href="https://doi.org/10.1002/mrm.70308" target="_blank">doi:10.1002/mrm.70308</a></li>
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
