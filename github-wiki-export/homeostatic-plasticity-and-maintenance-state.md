# Wiki: Homeostatic Plasticity And Maintenance-State

> Even with a wiring diagram and cell type labels, long-term dynamics are still not determined.
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-17 / Role: Technical / natural science only

## Role Of This Page
This page responds to the intuition that if we know the wiring diagram and cell type, most of the rest will fall into place. Against that intuition, it organizes the maintenance mechanisms that remain separate variables in primary literature: intrinsic excitability, AIS and ion-channel landscapes, firing-rate set points, sleep-dependent renormalization, myelin / oligodendrocyte coupling, local ATP supply and mitochondrial arrangement, synaptic-density proxies including human SV2A PET, glial metabolism, clearance / immune support, and molecular turnover. It focuses only on technology and natural science, not philosophy or legal systems.


## Accuracy Notes
What is shown here is the minimum list of hidden states that must be accounted for when reading long-term dynamics and memory maintenance. This does not mean sufficient conditions have been established.


## Back To Public Pages
- [Verification](https://mind-upload.com/verification.html)
- [Technology Roadmap](https://mind-upload.com/tech_roadmap.html)
- [WBE Basics](https://mind-upload.com/wbe_101.html)

## Related Wiki Pages
- [Wiki: Why wiring diagrams alone are not enough](https://github.com/yasufumi-nakata/mind-upload/wiki/connectome-is-not-enough) - Starts with the broader state variables that remain missing from the connectome.
- [Wiki: state / trait / drift](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - Adds guidance for separating maintenance-state from drift in longitudinal evaluation.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Clarifies how far latent states can be raised from observation alone.

## What Is Currently Known
- Continuity and variability in morpho-electric phenotype remain even within the same transcriptomic type.
- Firing rates and synaptic strengths are regulated by homeostatic plasticity across sleep / wake cycles.
- Myelin, oligodendrocytes, local ATP supply and mitochondrial positioning, astrocytes, and the microglia / meningeal-lymphatic system all contribute to timing, metabolism, memory retrieval, long-term recovery, and clearance support.
- Even in humans, macro scaffolds and support-state proxies are starting to become visible through SV2A PET, MRSI-based metabolic connectomes, 31P-MRS, dynamic deuterium metabolic imaging, myelin bilayer mapping, TMS / EEG / sleep plasticity proxies, and CSF / glymphatic proxies, although cell-specific maintenance-states still remain coarse.

## What Is Still Unknown
- It is unclear at what granularity excitability, sleep homeostasis, bioenergetic support, metabolic support, and clearance support must be measured to approach sufficient conditions for WBE.
- It has not been fixed which external standards among SV2A PET, MRSI, 31P-MRS, dynamic DMI, myelin bilayers, TMS-EEG, sleep-plasticity proxies, and CSF-glymphatic proxies should calibrate maintenance-states that cannot be measured directly in humans.
- It is not yet fixed which sleep, myelin, bioenergetic, metabolic, and clearance indicators will become standard submissions for long-term closed-loop claims.
- It is also unclear how strongly parcel-level metabolic similarity and CSF-mobility proxies constrain cell-specific glial, immune, transmitter, and synaptic maintenance-states.

---

<h2>The shortest conclusion</h2>
<p>
Even if<strong>the connectome and cell type are known, the long-term dynamics are not yet determined</strong>. Current primary literature shows relatively consistently that at least eight types of maintenance-states remain. First, even within the same transcriptomic type, the morpho-electric phenotype and ion-channel expression vary widely, and AIS geometry and Na+ channel distribution can vary over a span of hours to days. Second, neural circuits homeostatically adjust their firing rate and synaptic strength, not only maintaining <strong>current activity</strong> but also having a set point of <strong>where to return</strong>. Third, sleep/wake cycles create a temporal division of labor between synaptic scaling and firing-rate homeostasis. Fourth, the myelin sheath and oligodendrocyte connections are involved not only in timing but also in axonal support. Fifth, local ATP supply, mitochondrial parking position, fission/fusion, and redox reserve constrain synaptic vesicle recycling, dendritic plasticity, and local translation. Sixth, astrocytes and glial metabolism are not the background of memory consolidation, but are also involved in<strong>memory retrieval, stabilization over a multi-day span, and fear memory expression</strong>. Seventh, clearance/immune support including meningeal lymphatic drainage, CSF-interstitial exchange, and microglia support synaptic physiology and multiday recovery. Eighth, even if memory remains under molecular turnover, this does not mean permanent preservation of stationary molecules, but active maintenance. Therefore, this site treats the reconsolidation mechanism, including relative excitability, AIS / channel state, homeostatic set point, sleep-dependent renormalization, myelin support, bioenergetic / mitochondrial state, astrocyte ensemble, clearance / immune support, as a hidden state that remains outside the connectome.
</p>

<strong>Scope of this page</strong>
<p>
Philosophy, legal systems, and copying issues are not discussed here. It addresses why wiring diagrams, cell types, and short-term activity matching alone are still an underspecification when reading WBE and long-term BCI.
</p>

<h2>8 maintenance-states to fix first</h2>
<table>
<thead>
<tr>
<th>maintenance-state</th>
<th>What's missing</th>
<th>Dangerous misreading</th>
<th>Currently handling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Intrinsic excitability / AIS / ion-channel configuration</strong></td>
<td>Response laws of the cell to input, such as threshold, gain, afterhyperpolarization, burstiness, rebound, AIS length/position, and Na+ channel distribution. </td>
<td>If you have a cell-type label or a short activity record, you can almost determine the same input-output rules. </td>
<td>Leave as latent state unless accompanied by morpho-electric or patch/perturbation. </td>
</tr>
<tr>
<td><strong>Firing rate set point / recovery controller</strong></td>
<td>Where the circuit returns after perturbation, with what time constant, and which compensatory path to use. </td>
<td>If the current average firing rates are similar, then the maintenance mechanism is also the same. </td>
<td>Longitudinal claims will be demoted if there is no fixed-model degradation and recovery log or set point indicator. </td>
</tr>
<tr>
<td><strong>Renormalization of sleep / wake dependencies</strong></td>
<td>When synaptic modeling, phosphoproteome, and network regimes are reset and accumulated. </td>
<td>If the activities during wakefulness and same-day decoding are similar, then the maintenance mechanism for the next day is also the same. </td>
<td>If sleep state or overnight recovery is lacking, cross-day stability is limited. </td>
</tr>
<tr>
<td><strong>Myelin / oligodendrocyte support</strong></td>
<td>Changes in conduction velocity, activity-dependent myelination, and axonal metabolic support. </td>
<td>If you set delay as a constant, timing and energy support are sufficient. </td>
<td>The absence of myelin/oligodendroglial state weakens timing-sensitive claims and long-term recovery claims. </td>
</tr>
<tr>
<td><strong>bioenergetic / mitochondrial state</strong></td>
<td>Local ATP supply, mitochondrial parking position, fission/fusion, ATP synthase relocation, and redox reserve. </td>
<td>If you look at glial/metabolic support, you can read that it can almost represent the local energy constraints of neurons. </td>
<td>If there is no bioenergetic/mitochondrial state, reliability during repeated stimulation, dendritic plasticity, and energetic mechanism of local translation will remain as a latent state. </td>
</tr>
<tr>
<td><strong>Glial metabolism / substrate routing</strong></td>
<td>Astrocyte-neuron lactate shuttle, reactivation of astrocyte ensemble, astrocyte network response to local transmitter, and slow metabolic support. </td>
<td>I read that if you track just the engram on the neuron side, you can almost determine recall and stabilization after a few days. </td>
<td>If you reduce the glial/metabolic state, limit the scope of plasticity, memory retrieval, restabilization, and slow state. </td>
</tr>
<tr>
<td><strong>clearance / immune support</strong></td>
<td>meningeal lymphatic drainage, CSF-interstitial exchange, microglia-mediated surveillance, protein/metabolite clearance and immune support during recovery. </td>
<td>Clearance is passive housekeeping, so it has little to do with momentary neural fit or next-day stability. </td>
<td>If you reduce clearance / immune support, weaken multiday recovery, protein-clearance, and support-state claims, and specify human proxy as support-state proxy. </td>
</tr>
<tr>
<td><strong>Reimmobilization under molecular turnover</strong></td>
<td>Even if receptors, kinases, and scaffolding proteins are replaced, what maintains the memory trace? </td>
<td>I read that if the memory is to remain, it is sufficient to save only a static molecule snapshot. </td>
<td>If molecular retention is not claimed and the maintenance mechanism is not measured, it will be clearly stated as not measured. </td>
</tr>
</tbody>
</table>

<h2>Why cell type and short-term activity matching alone are not enough</h2>

<h3>1. Transcriptomic type does not completely fix morpho-electric phenotype</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> showed that transcriptomic cell types in the mouse motor cortex have continuous fluctuations within the morpho-electric space. This means that<strong>even if the cell-type label is known, the electrophysiological parameters of the field are not uniquely determined</strong>. Furthermore, <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> showed that although there are large individual differences in ion channel mRNA and current levels among identified neurons, some function can be maintained. Therefore, even if you overlay cell-type labels on the connectome, the<strong>threshold and gain layers</strong> still remain.
</p>

<h3>2. Sometimes what is maintained is not the “current value” but the “return destination”</h3>
<p>
<a href="https://doi.org/10.1038/36103" target="_blank">Turrigiano et al. (1998)</a> showed that neocortical neurons bidirectionally scale their quantitative amplitude in response to chronic activity blockade or activity increase. Furthermore, <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> showed that the relationship between activity set point, cell type, and compensation can be explained from a simple biophysical model of activity-dependent ion-channel expression. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> show that individual neurons return to a precise firing-rate set point in the visual cortex in vivo. What is important here is that not only the activity value as a snapshot, but also the state of the controller, which is where to return after perturbation, is a separate variable.
</p>

<h3>3. Intrinsic excitability is not in one line, but is split into AIS and ion-channel landscape</h3>
<p>
The weakness that we should have investigated most deeply this time was that if we write <strong>intrinsic excitability</strong> as one latent state, <strong>memory allocation by relative excitability</strong>, <strong>gain adjustment by AIS geometry / Na+ channel distribution</strong>, and <strong>homeostatic recovery controller</strong> appear to be in the same evidence layer. <a href="https://doi.org/10.1038/nature09160" target="_blank">Grubb &amp; Burrone (2010)</a> showed that AIS relocation according to activity fine-tune neural excitability, and <a href="https://doi.org/10.1038/nature09087" target="_blank">Kuba et al. (2010)</a> showed that presynaptic activity can regulate Na+ channel distribution in AIS. Furthermore, <a href="https://doi.org/10.1038/s41467-020-20232-x" target="_blank">Jamann et al. (2021)</a> demonstrated rapid homeostatic AIS scaling in response to sensory input in the mouse barrel cortex. target="_blank">Fréal et al. (2023)</a> showed that sodium channel endocytosis drives AIS plasticity, and <a href="https://doi.org/10.1038/s41593-025-02152-5" target="_blank">Benoit et al. (2025)</a> showed that AIS dynamics during associative fear learning. showed that it changes. Therefore, even if <strong>the same connectome and the same cell type</strong> are known, <strong>threshold / gain / spike-initiation rules with a span of hours to days</strong> will still remain latent.
</p>

<strong>What can be said directly from this verse</strong>
<p>
What we can say directly from this is that when reading the input-output rules for WBE and long-term BCI, one should not collapse<strong>intrinsic excitability into one number or one row of missing columns. Allocation, AIS/channel state, and recovery controller should be measured separately, or at least written with separate reasons for abstention.
</p>

<h3>4. sleep / wake cycles rewire synapse and network regimes</h3>
<p>
The weakness of the current site is that it focuses maintenance-state too much on excitability and molecular turnover, and fails to emphasize that sleep is responsible for the time axis of renormalization itself. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a> showed that the firing rate that increases during wake returns to downward homeostasis during sleep. <a href="https://doi.org/10.1126/science.aah5982" target="_blank">de Vivo et al. (2017)</a> showed ultrastructural synaptic scaling across the wake/sleep cycle, and <a href="https://doi.org/10.1126/science.aai8355" target="_blank">Diering et al. (2017) showed excitatory synapse scaling-down during sleep via Homer1a. Furthermore, <a href="https://doi.org/10.1126/science.aav2642" target="_blank">Noya et al. (2019)</a> showed that the forebrain synaptic proteome is driven by sleep, and <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a> reported that sleep returns the cortical network to a better computational regime. In addition, <a href="https://doi.org/10.1016/j.cub.2024.07.032" target="_blank">Koukaroudi et al. (2024)</a> showed that sleep deprivation reduces excitatory synapse diversity in the cortex and hippocampus, and maintenance-state is not just a recalibration of the mean value, but also includes maintaining the distribution of the synaptic repertoire. Therefore,<strong>same-day activity matching alone cannot be read as maintenance-state matching</strong>. Without sleep history and overnight recovery log, next-day stability and post-learning re-equilibration are another matter.
</p>

<h3>5. Myelin and oligodendrocytes are timing and support variables</h3>
<p>
Although the current page mentions intrinsic excitability, it did not sufficiently fix <strong>myelin plasticity, which is the basis of delay, as a maintenance-state. <a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a> showed that neuronal activity promotes oligodendrogenesis and adaptive myelination, and <a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. al. (2014) showed that active central myelination is necessary for motor skill learning. Furthermore, <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> showed that oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and is involved in maintaining axonal health. Therefore,<strong>even with the same wiring and the same cell type, timing and recoverability can vary if the myelin/oligodendroglial state is different</strong>. A model in which delay is set as a fixed constant is convenient, but it is necessary to specify what is discarded in the approximation.
</p>

<h3>6. bioenergetic / mitochondrial state is not another name for glial support</h3>
<p>
The weakness that I discovered after digging deeper this time is that while I wrote <strong>myelin / oligodendroglial support</strong> and <strong>astrocyte / metabolic support</strong>, I did not isolate <strong>neuron local ATP supply and mitochondrial arrangement</strong> as independent maintenance-states. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">Rangaraju et al. (2014)</a> showed that activity-driven local ATP synthesis is required for presynaptic function, and <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">Rangaraju et al. (2019)</a> showed that spatially stable mitochondrial compartments support local translation during plasticity. Furthermore, <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">Divakaruni et al. (2018)</a> showed that rapid dendritic mitochondrial fission is required for LTP induction. href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">Bapat et al. (2024) showed that mitochondria stabilized on dendrites support local plasticity. href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">Hu et al. (2025)</a> showed polarization of ATP synthase in synaptic mitochondria in response to learning/plasticity signals. What we can directly say from this is that even with the same connectome, the same cell type, and the same astrocyte support, repeated-burst reliability and dendritic plasticity can still change if the local bioenergetic state of the neuron is different.
</p>

<strong>What you can currently see in human is the macro energetic proxy</strong>
<p>
<a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a> measured ATP synthesis, metabolite concentration, and pH using 31P-MRS in healthy human brains, and <a href="https://doi.org/10.1093/pnasnexus/pgaf079" target="_blank">Li et al. (2025)</a> visualized whole-brain glucose turnover using dynamic deuterium metabolic imaging. However, these are just <strong>macro energetic proxies</strong> and do not directly tell us <strong>which synapse neighborhood mitochondria are staying at and which dendritic branch lacks ATP reserve</strong>. Therefore, on this site, while acknowledging energetic imaging in humans as an important advance, we do not refer to direct readout of cell-specific bioenergetic / mitochondrial state.
</p>

<h3>7. Astrocytes are state variables for memory retrieval, stabilization, and expression</h3>
<p>
Reading maintenance-state too neuron-centric makes it easy to misread energy supply and local transmitter integration as "background noise." <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a> showed that astrocyte-neuron lactate transport is required for long-term memory formation. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> showed that local, instantaneous neurotransmitter inputs are encoded into broad astrocyte network states over the order of minutes. Furthermore, <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a> showed that in hippocampus, a learning-associated astrocyte ensemble is formed near engram neurons, ensemble reactivation causes memory recall, and astrocyte-specific NFIA deletion causes recall. has been shown to suppress. <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> showed that astrocyte ensemble associated with emotional memory contributes to stabilization over a span of several days across repeated recall, and integrates noradrenergic input and local engram signal to improve memory stability and precision. It was shown that it affects Furthermore, <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> showed that basolateral amygdala astrocytes reorganize in response to fear retrieval/extinction, and astrocyte Ca<sup>2+</sup> signaling We showed that it supports the neural representation of the amygdala-prefrontal circuit. What we can say directly from this is that it is dangerous to consider <strong>glial / metabolic background as an afterthought correction, and that the astrocyte ensemble itself remains as a state variable in long-term memory. However, these strong causal evidences center around rodent's hippocampus/amygdala issues, and do not directly translate into direct readout of human arbitrary content or whole-brain maintenance-state. When discussing memory consolidation and slow network state, it is necessary to at least distinguish between the extent to which astrocyte/metabolic support was measured and the point at which proxy was substituted.
</p>

<strong>How to read the strength of evidence</strong>
<p>
On the other hand, <a href="https://doi.org/10.1038/s41586-023-07011-6" target="_blank">Sun et al. (2024)</a>'s spatial transcriptomics suggested interaction between peri-engram neurons and astrocytes, and <em>Igfbp2</em> as a long-term memory candidate; href="https://doi.org/10.1038/s41586-025-08988-y" target="_blank">Mukamel &amp; Yu (2025)</a> criticized that no significant DEGs remain after correcting for the dependence of cells derived from the same animal as multiple-comparison, and <a href="https://doi.org/10.1038/s41586-025-08989-x" target="_blank">Sun et al. (2025)</a> objected on the basis of the difference in analysis intent. Therefore, on this site, we treat this system as <strong>transcriptomic clue / hypothesis-generating evidence</strong>, and the causal weight of glia is <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a>, <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a>, <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">Bukalo et al. (2026)</a> I would like to focus on intervention research such as reactivation, inhibition, and circuit expression.
</p>

<h3>8. clearance / immune support is not passive cleanup</h3>
<p>
The weak point that I discovered after digging deeper this time is that while I wrote about <strong>astrocyte / metabolic support</strong> in detail, I did not sufficiently isolate <strong>meningeal lymphatics, CSF-interstitial exchange, clearance / immune support, including microglia, as an independent maintenance-state. <a href="https://doi.org/10.1038/nature14432" target="_blank">Louveau et al. (2015)</a> demonstrated the structure and function of CNS lymphatic vessels, and <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025) showed that the meningeal lymphatics-microglia axis regulates synaptic physiology. On the human side, <a href="https://doi.org/10.1093/brain/awab285" target="_blank">Eide &amp; Ringstad (2021)</a> has shown that sleep deprivation inhibits molecular clearance. target="_blank">Hirschler et al. (2025)</a> demonstrated that MRI can measure region-specific CSF mobility drivers, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> demonstrated that glymphatic routes can be measured in humans. showed amyloid-beta/tau clearance in line with What we can directly say from this is that<strong>clearance / immune support is not just a metaphor for cleaning, but is becoming measurable as a multiday support-state. At the same time, however, these human data are not a direct readout of <strong>local synaptic weight</strong> or <strong>moment-to-moment neural truth</strong>. Therefore, on this site, clearance / immune support is treated independently as <strong>slow support-state</strong>, while in human it is first read as <strong>macro support proxy</strong>.
</p>

<strong>How to read human clearance proxy</strong>
<p>
<a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> is a 7T MRI technical report that measures <strong>CSF mobility</strong> and is not a direct readout of clearance flux itself. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> is an important advance in combining randomized crossover and plasma biomarkers, but it relies on an <strong>investigational device</strong> and <strong>compartment model</strong>, and the paper itself requires multiple-comparison adjustment in some analyses. leaving a shortage of Therefore, this site treats both as <strong>provisional human support-state proxies</strong> and does not raise them to the ground truth of cell-specific immune controller or local synaptic maintenance.
</p>

<h3>9. Memory under molecular turnover should be read as reconsolidation rather than static storage</h3>
<p>
<a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Lee et al. (2022)</a> showed through simulation and analysis that synaptic memory can be maintained by active CaMKII state transfer even under molecular turnover. What we can say directly from this is that it is possible for memories to remain even if molecules are replaced. However, conversely, it is safer to read that<strong>memory persistence does not mean the sufficiency of static molecular snapshots, but means that a maintenance mechanism is working</strong>. When synaptic scaling and glial-metabolic support during sleep are read together, memory maintenance is treated as a chain of renormalization and refixation, rather than cryopreservation of a single molecule, which is closer to the primary literature.
</p>

<h3>10. Relative excitability influences future memory allocation</h3>
<p>
<a href="https://doi.org/10.1016/j.neuron.2014.07.017" target="_blank">Yiu et al. (2014)</a> showed that relative neuronal excitability before learning influences which neurons are more likely to be incorporated into a memory trace. Additionally, <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> show that early intrinsic excitability plasticity of neocortical engram neurons regulates memory formation and precision. Therefore, even if the connectome is the same, future learning paths and memory allocation can change if the excitability landscape is different.
</p>

<h2>2026-03 Addendum: Direct observation of human maintenance-state is still rough</h2>
<p>
This time, we dug deeper and discovered that the human observability section is not as good as <strong>EM fragment</strong>, <strong>SV2A PET</strong>, <strong>whole-brain MRSI</strong>, <strong>31P-MRS / dynamic DMI</strong>, <strong>myelin bilayer imaging</strong>, <strong>TMS-EEG / sleep plasticity proxy</strong>, <strong>CSF / glymphatic proxy</strong>. My point is that I was lumping these together as the same "evidence that started to appear in humans." If we look at the primary literature, each is pushing a separate layer: a structural scaffold, a regional synaptic-density proxy, a macro-biochemical scaffold, a macro energetic proxy, a macro-myelin proxy, a perturbation-conditioned plasticity proxy, and a macro support-state proxy. In particular, <a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">Finnema et al. (2016)</a>, <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Regional SV2A binding and synaptic-density atlas are directly visible in Johansen et al. What is directly visible in Lucchetti et al. (2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf079" target="_blank">Li et al. (2025)</a>, it is a macro proxy for ATP/glucose turnover. All are important but do not directly confer<strong>current synaptic efficacy</strong>,<strong>release probability</strong>,<strong>postsynaptic receptor occupancy</strong>,<strong>local transmitter specificity</strong>,<strong>astrocyte ensemble</strong>,<strong>sleep-dependent recovery controller</strong>,<strong>cell-specific immune controller</strong>, or<strong>branch-specific mitochondrial positioning</strong>. Therefore, even on the human side, maintenance-state remains divided into <strong>macro scaffold / macro proxy / local hidden state</strong>.
</p>
<table>
<thead>
<tr>
<th>What I began to see in human</th>
<th>Directly visible layer</th>
<th>Still latent layer</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>human nanoscale ultrastructure</strong><br>Shapson-Coe et al.</td>
<td>Ultrastructure, cell/synapse arrangement, and local structure scaffold of fixed human cortex fragments. </td>
<td>Current weight, sleep history, recovery controller, neuromodulatory context, and glial slow-state.</td>
</tr>
<tr>
<td><strong>human synaptic-density PET</strong><br>Finnema et al., Naganawa et al., Johansen et al.</td>
<td>Regional presynaptic vesicle density based on SV2A binding and atlas-level synaptic-density distribution. </td>
<td>Current synaptic efficacy, release probability, postsynaptic receptor occupancy, silent-synapse recruitment, excitatory / inhibitory composition, and trial-level fluctuation.</td>
</tr>
<tr>
<td><strong>human metabolic connectome</strong><br>Lucchetti et al.</td>
<td>Parcel-level biochemical organization based on Glx / Ins / Cho / tCr / tNAA and its reproducibility. </td>
<td>Cell-specific metabolic routing, astrocyte ensemble, local transmitter state, and synapse-specific maintenance.</td>
</tr>
<tr>
<td><strong>human energetic imaging</strong><br>Ren et al., Li et al.</td>
<td>A macro energetic proxy for ATP/PCr/pH by 31P-MRS and whole-brain glucose turnover by dynamic DMI. </td>
<td>Cell-specific ATP reserves, branch-specific mitochondrial positioning, synapse-specific fatigue risk, and energetic mechanisms of dendritic plasticity.</td>
</tr>
<tr>
<td><strong>human myelin bilayer map</strong><br>Baadsvik et al.</td>
<td>In vivo 1.4 mm class myelin bilayer contrast and regional myelin distribution. </td>
<td>Single-axon conduction delay, activity-dependent myelination, oligodendrocyte-axon metabolic support, and a cell-specific timing controller.</td>
</tr>
<tr>
<td><strong>human sleep-homeostasis / plasticity proxy</strong><br>Huber et al., Kuhn et al., Fehér et al.</td>
<td>A macro perturbational proxy that changes TMS-EEG excitability and PAS induction plasticity depending on wake / sleep / nap. </td>
<td>Which cell type, synapse, glia, or controller was responsible for the change. </td>
</tr>
<tr>
<td><strong>human state-gated perturbation proxy</strong><br>Zrenner et al.</td>
<td>A state-conditioned causal proxy that the EEG-defined excitability state influences TMS-induced plasticity efficacy. </td>
<td>AIS geometry, channel distribution, cell-specific allocation state, and long-horizon recovery controllers.</td>
</tr>
<tr>
<td><strong>human CSF / glymphatic proxy</strong><br>Hirschler et al., Dagum et al.</td>
<td>Macro support-state proxy using region-specific CSF mobility and device/model-based protein-biomarker transport. </td>
<td>Which synapse, which astrocyte, which microglia, and which meningeal lymphatic controller are responsible for the difference? </td>
</tr>
</tbody>
</table>
<p>
This difference is important in practice. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> investigated local ultrastructure of fixed tissue, and <a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">Finnema et al. (2016)</a>, <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">Naganawa et al. (2021)</a>, <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> analyzed the regional synaptic-density proxy using SV2A PET in humans, and <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">Shatalina et al. href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf079" target="_blank">Li et al. et al. (2024)</a> have an in vivo map of myelin bilayer, <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">Huber et al. al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">Fehér et al. (2026)</a>, <a href="https://doi.org/10.1016/j.brs.2017.11.016" <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> independently pushed the CSF/glymphatic support-state to become measurable in humans. The important point is that <strong>these are not the same type of direct measurement</strong>, and one human proxy should not be interpreted as the ground truth of a cell-specific maintenance-state.
</p>

<strong>Practical interpretation in this addendum</strong>
<p>
Therefore, on this site, we will introduce <strong>human metabolic connectome</strong> to <strong>macro-biochemical scaffold</strong>, <strong>31P-MRS / dynamic DMI</strong> to <strong>macro energetic proxy</strong>, <strong>human myelin bilayer map</strong> to <strong>macro-myelin proxy</strong>, and <strong>TMS-EEG / sleep plasticity</strong> to <strong>perturbational proxy</strong>, treat<strong>CSF mobility / glymphatic clearance</strong> as a<strong>macro support-state proxy</strong>. All of them are promising, but they are not written as<strong>glial / transmitter maintenance-state ground truth</strong>,<strong>cell-specific recovery controller</strong>,<strong>local immune controller</strong>, or<strong>local mitochondrial state</strong>. Similarly, human EM fragments are treated as <strong>structural scaffold enhancements</strong> rather than <strong>state-complete snapshots</strong>. It is safe to support the existence of layers that are not directly visible to humans with animal causal evidence, while clearly stating the observability ceiling and abstinence on the human side.
</p>

<h2>Common misreadings and demotion rules on this site</h2>
<table>
<thead>
<tr>
<th>Dangerous Reading</th>
<th>Why is it dangerous</th>
<th>Handling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>If you know the cell-type label, the input-output rule is almost determined</strong></td>
<td>Morpho-electric variability and channel-expression variability remain within the same type. </td>
<td>Do not write excitability fixed in cell-type alone, leave it as latent state. </td>
</tr>
<tr>
<td><strong>If the connectome / cell type is the same, AIS and channel-state are also almost the same</strong></td>
<td>AIS length / position and Na+ channel distribution change according to activity, sensory input, and learning. </td>
<td>If there is no patch, perturbation, or AIS proxy, the gain / allocation / spike-initiation rule will remain in latent state. </td>
</tr>
<tr>
<td><strong>Since the average firing rate returned, the internal state also returned to the same</strong></td>
<td>The same rate may be achieved with a different conductance combination or a different controller. </td>
<td>rate only recovery, does not claim internal identity, requests perturbation and recovery logs. </td>
</tr>
<tr>
<td><strong>If the daytime activity and decoder performance are similar, the overnight maintenance is also the same</strong></td>
<td>Synaptic scaling during sleep, firing-rate homeostasis, and network regime recovery remain separately. </td>
<td>The cross-day stability claim is demoted if no sleep / wake annotations or next day recovery are issued. </td>
</tr>
<tr>
<td><strong>With the human metabolic connectome, the glial / transmitter maintenance-state was also directly visible</strong></td>
<td>Parcel-level metabolic similarity is useful, but it does not directly provide cell-specific astrocyte ensemble or transmitter state. </td>
<td>Human MRSI is treated as a macro-biochemical scaffold and is not written as the ground truth of local maintenance-state. </td>
</tr>
<tr>
<td><strong>With human myelin bilayer map and nap / TMS proxy, cell-specific maintenance controller could also be seen</strong></td>
<td>Myelin bilayer map is a mm-class tissue proxy, and TMS-EEG/PAS is a perturbational readout. The question remains which axon, oligodendrocyte, astrocyte, or synapse was responsible for the change. </td>
<td>Human myelin / sleep / excitability data is specified as macro or perturbational proxy and is not uploaded to the ground truth of cell-specific controller. </td>
</tr>
<tr>
<td><strong>Since human CSF mobility and glymphatic clearance were visible, local immune / clearance controllers were also identified</strong></td>
<td>Human CSF/glymphatic data is a macro support-state proxy, and it remains independent of which microglia, meningeal lymphatic segment, astrocyte endfoot, or local synapse is responsible for the difference. </td>
<td>Human clearance proxy is written as support-state proxy and does not increase to moment-to-moment neural truth or cell-specific immune controller. </td>
</tr>
<tr>
<td><strong>If the delay is set as a constant, the myelin sheath and oligodendrocytes can be postponed</strong></td>
<td>Adaptive myelination and axon-glia coupling are concerned with timing and long-term support. </td>
<td>In the timing-sensitive claim, the fact that myelin / conduction is not measured is clearly stated in the text. </td>
</tr>
<tr>
<td><strong>With human energetic imaging, we could directly see the local mitochondrial status</strong></td>
<td>31P-MRS and dynamic DMI are macro proxies for ATP/glucose turnover, but they do not tell in which branch or synapse the ATP reserve is insufficient or where the mitochondria are stopped. </td>
<td>Human energetic imaging is written as a macro energetic proxy and is not elevated to the ground truth of cell-specific bioenergetic / mitochondrial state. </td>
</tr>
<tr>
<td><strong>If the engrams and spike trains on the neuron side are similar, recall and stabilization after several days will be the same.</strong></td>
<td>Astrocyte ensemble, lactate transport, and local transmitter integration are involved in memory recall, restabilization, and fear-state representation. </td>
<td>When dropping glial/metabolic support, limit the scope of application of plasticity, memory consolidation, recall, restabilization, and slow state. </td>
</tr>
<tr>
<td><strong>If memory is to last long, the molecular state that must be preserved is static</strong></td>
<td>Persistence is often the result of active maintenance and reconsolidation across turnover. </td>
<td>We do not claim the sufficiency of the molecular snapshot, but specify that the maintenance mechanism has not been determined. </td>
</tr>
</tbody>
</table>

<h2>Practical rules adopted on this site</h2>

<h4>Rule</h4>
<ul>
<li><strong>In long-term claims, put maintenance-state in a separate column:</strong>Do not mix connectome / cell type / synapse with intrinsic excitability, sleep-homeostasis, myelin / oligodendroglial support, bioenergetic / mitochondrial state, glial / metabolic support, clearance / immune support. </li>
<li><strong>Don't collapse intrinsic excitability into one line:</strong>Make relative excitability, AIS / channel state, and recovery controller separate columns. </li>
<li><strong>If sleep / wake history is not measured, write it as not measured:</strong>Do not auto-complete overnight maintenance from same-day fit. </li>
<li><strong>Do not reduce sleep to mean correction:</strong>Leaves the possibility of dropping down to synapse diversity or network regime. </li>
<li>If we absorb <strong>delay with a constant, we write it as absorbed:</strong>Do not silently push timing state and axonal support into the model. </li>
<li><strong>Don't replace memory persistence with static storage: Leave open the possibility of reconsolidation and support mechanisms across</strong>turnovers. </li>
<li><strong>Focus on post-perturbation recovery:</strong>Keep a log of not only what happened, but also where you return and how you return across sleep. </li>
<li><strong>Write the limitations of proxy first:</strong>Do not write that maintenance-state is uniquely determined only by EEG / pupil / behavior. </li>
<li><strong>Do not mix human proxy classes:</strong>Do not collapse EM fragments, whole-brain MRSI, 31P-MRS / dynamic DMI, myelin bilayer map, sleep / TMS proxy into the same "human-seen" word. </li>
<li><strong>Do not misinterpret human MRSI as local ground truth:</strong>Write macro-biochemical scaffold and cell-specific maintenance-state separately. </li>
<li><strong>Do not misread human CSF / glymphatic proxy as local controller:</strong>Write macro support-state proxy and cell-specific immune / clearance state separately. </li>
<li><strong>Does not complement glia omission from neuron-only success:</strong>Recall, restabilization, and fear-state representation leave the astrocyte state separate. </li>
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
<td><strong>cross-day stability</strong></td>
<td> Fixed model degradation curve, recovery time, sleep / wake annotations, state / trait / drift separation, firing-rate distribution and excitability proxy if possible. </td>
</tr>
<tr>
<td><strong>gain / excitability claim</strong></td>
<td>relative excitability or perturbation proxy, AIS / channel proxy if possible, within-day / cross-day gain drift, omission log of unmeasured allocation / recovery controller. </td>
</tr>
<tr>
<td><strong>Long-horizon memory / learning claim</strong></td>
<td>Perturbation responses before and after learning, relative excitability or allocation proxy, presence or absence of overnight renormalization, glial / astrocyte covariate or omission log, clearance / immune covariate if possible, and list of unmeasured maintenance-states. </td>
</tr>
<tr>
<td><strong>timing-sensitive claim</strong></td>
<td>delay / phase error, myelin or conduction proxy, timing support approximated by a fixed constant, unmeasured oligodendroglial state. </td>
</tr>
<tr>
<td><strong>energetic-mechanism claim</strong></td>
<td>Energetic proxy such as 31P-MRS / dynamic DMI, fatigue / repeated-burst failure log if possible, bioenergetic state set to fixed background, unmeasured mitochondrial positioning / redox reserve. </td>
</tr>
<tr>
<td><strong>Claim close to state-complete reconstruction</strong></td>
<td>To what extent did you acquire connectome, cell type, synapse, delay / myelin, bioenergetic / mitochondrial state, neuromodulation, glia / metabolic support, clearance / immune support, sleep-homeostasis, intrinsic excitability / homeostasis, or did you abstain as a latent? </td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>Schulz, D. J., Goaillard, J.-M., &amp; Marder, E. (2006). Variable channel expression in identified single and electrically coupled neurons in different animals. <em>Nature Neuroscience</em>, 9(3), 356-362. <a href="https://doi.org/10.1038/nn1639" target="_blank">doi:10.1038/nn1639</a></li>
<li>Grubb, M. S., &amp; Burrone, J. (2010). Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. <em>Nature</em>, 465(7301), 1070-1074. <a href="https://doi.org/10.1038/nature09160" target="_blank">doi:10.1038/nature09160</a></li>
<li>Kuba, H., Oichi, Y., &amp; Ohmori, H. (2010). Presynaptic activity regulates Na+ channel distribution at the axon initial segment. <em>Nature</em>, 465(7301), 1075-1078. <a href="https://doi.org/10.1038/nature09087" target="_blank">doi:10.1038/nature09087</a></li>
<li>Jamann, N., Dannehl, D., Lehmann, N., et al. (2021). Sensory input drives rapid homeostatic scaling of the axon initial segment in mouse barrel cortex. <em>Nature Communications</em>, 12, 23. <a href="https://doi.org/10.1038/s41467-020-20232-x" target="_blank">doi:10.1038/s41467-020-20232-x</a></li>
<li>Fréal, A., Jamann, N., Ten Bos, J., et al. (2023). Sodium channel endocytosis drives axon initial segment plasticity. <em>Science Advances</em>, 9(37). <a href="https://doi.org/10.1126/sciadv.adf3885" target="_blank">doi:10.1126/sciadv.adf3885</a></li>
<li>Benoit, C. M., Ganea, D. A., Paricio-Montesinos, R., et al. (2025). Axon initial segment dynamics during associative fear learning. <em>Nature Neuroscience</em>, 29(3), 535-542. <a href="https://doi.org/10.1038/s41593-025-02152-5" target="_blank">doi:10.1038/s41593-025-02152-5</a></li>
<li>Turrigiano, G. G., Leslie, K. R., Desai, N. S., Rutherford, L. C., &amp; Nelson, S. B. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. <em>Nature</em>, 391, 892-896. <a href="https://doi.org/10.1038/36103" target="_blank">doi:10.1038/36103</a></li>
<li>O'Leary, T., Williams, A. H., Franci, A., &amp; Marder, E. (2014). Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. <em>Neuron</em>, 82(4), 809-821. <a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">doi:10.1016/j.neuron.2014.04.002</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>, 165(1), 180-191. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <em>Neuron</em>, 109(3), 530-544.e6. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Diering, G. H., et al. (2017). Homer1a drives homeostatic scaling-down of excitatory synapses during sleep. <em>Science</em>, 355(6324), 511-515. <a href="https://doi.org/10.1126/science.aai8355" target="_blank">doi:10.1126/science.aai8355</a></li>
<li>de Vivo, L., et al. (2017). Ultrastructural evidence for synaptic scaling across the wake/sleep cycle. <em>Science</em>, 355(6324), 507-510. <a href="https://doi.org/10.1126/science.aah5982" target="_blank">doi:10.1126/science.aah5982</a></li>
<li>Noya, S. B., et al. (2019). The forebrain synaptic transcriptome is organized by clocks but its proteome is driven by sleep. <em>Science</em>, 366(6462), eaav2642. <a href="https://doi.org/10.1126/science.aav2642" target="_blank">doi:10.1126/science.aav2642</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Neuroscience</em>, 27, 972-980. <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">doi:10.1038/s41593-023-01536-9</a></li>
<li>Koukaroudi, D., Qiu, Z., Fransén, E., et al. (2024). Sleep maintains excitatory synapse diversity in the cortex and hippocampus. <em>Current Biology</em>, 34(16), 3836-3843.e5. <a href="https://doi.org/10.1016/j.cub.2024.07.032" target="_blank">doi:10.1016/j.cub.2024.07.032</a></li>
<li>Yiu, A. P., et al. (2014). Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. <em>Neuron</em>, 83(3), 722-735. <a href="https://doi.org/10.1016/j.neuron.2014.07.017" target="_blank">doi:10.1016/j.neuron.2014.07.017</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <em>Brain Stimulation</em>, 11(2), 374-389. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Huber, R., Mäki, H., Rosanova, M., Casarotto, S., Canali, P., Casali, A. G., Tononi, G., &amp; Massimini, M. (2013). Human cortical excitability increases with time awake. <em>Cerebral Cortex</em>, 23(2), 332-338. <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">doi:10.1093/cercor/bhs014</a></li>
<li>Kuhn, M., Wolf, E., Maier, J. G., Mainberger, F., Feige, B., Schmid, H., et al. (2016). Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. <em>Nature Communications</em>, 7, 12455. <a href="https://doi.org/10.1038/ncomms12455" target="_blank">doi:10.1038/ncomms12455</a></li>
<li>Fehér, K. D., Henckaerts, P., Hirsch, V., Bucsenez, U., Kuhn, M., Maier, J. G., et al. (2026). A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. <em>NeuroImage</em>, 327, 121723. <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">doi:10.1016/j.neuroimage.2026.121723</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318-322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <em>Nature Neuroscience</em>, 27, 1598-1609. <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">doi:10.1038/s41593-023-01558-3</a></li>
<li>Rangaraju, V., Calloway, N., &amp; Ryan, T. A. (2014). Activity-driven local ATP synthesis is required for synaptic function. <em>Cell</em>, 156(4), 825-835. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">doi:10.1016/j.cell.2013.12.042</a></li>
<li>Rangaraju, V., Lauterbach, M., &amp; Schuman, E. M. (2019). Spatially stable mitochondrial compartments fuel local translation during plasticity. <em>Cell</em>, 176(1-2), 73-84.e15. <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">doi:10.1016/j.cell.2018.12.013</a></li>
<li>Divakaruni, S. S., Van Dyke, A. M., Chandra, R., et al. (2018). Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. <em>Neuron</em>, 100(4), 860-875.e7. <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">doi:10.1016/j.neuron.2018.09.025</a></li>
<li>Bapat, P., Nirschl, J. J., Wilkerson, J. R., et al. (2024). VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. <em>Nature Communications</em>, 15, 742. <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">doi:10.1038/s41467-023-44233-8</a></li>
<li>Hu, H., Tang, J., Wu, Y., et al. (2025). Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. <em>Communications Biology</em>, 8, 166. <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">doi:10.1038/s42003-025-08963-3</a></li>
<li>Suzuki, A., et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. <em>Cell</em>, 144(5), 810-823. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">doi:10.1016/j.cell.2011.02.018</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Sun, X., et al. (2024). Spatial transcriptomics reveal neuron-astrocyte synergy in long-term memory. <em>Nature</em>, 627, 374-381. <a href="https://doi.org/10.1038/s41586-023-07011-6" target="_blank">doi:10.1038/s41586-023-07011-6</a></li>
<li>Mukamel, E. A., &amp; Yu, X. (2025). False positives in study of memory-related gene expression. <em>Nature</em>, 642, E1-E3. <a href="https://doi.org/10.1038/s41586-025-08988-y" target="_blank">doi:10.1038/s41586-025-08988-y</a></li>
<li>Sun, X., et al. (2025). Reply to: False positives in study of memory-related gene expression. <em>Nature</em>, 642, E4-E6. <a href="https://doi.org/10.1038/s41586-025-08989-x" target="_blank">doi:10.1038/s41586-025-08989-x</a></li>
<li>Williamson, N. R., et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. <em>Nature</em>, 636, 445-454. <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">doi:10.1038/s41586-024-08170-w</a></li>
<li>Dewa, K., et al. (2025). The astrocytic ensemble acts as a multiday trace to stabilize memory. <em>Nature</em>, 648, 99-107. <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">doi:10.1038/s41586-025-09619-2</a></li>
<li>Bukalo, O., et al. (2026). Astrocytes enable amygdala neural representations supporting memory. <em>Nature</em>. <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">doi:10.1038/s41586-025-10068-0</a></li>
<li>Louveau, A., Smirnov, I., Keyes, T. J., et al. (2015). Structural and functional features of central nervous system lymphatic vessels. <em>Nature</em>, 523, 337-341. <a href="https://doi.org/10.1038/nature14432" target="_blank">doi:10.1038/nature14432</a></li>
<li>Kim, J., et al. (2025). Meningeal lymphatics-microglia axis regulates synaptic physiology. <em>Cell</em>, 188(8), 2129-2148.e21. <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">doi:10.1016/j.cell.2025.02.022</a></li>
<li>Eide, P. K., &amp; Ringstad, G. (2021). Sleep deprivation impairs molecular clearance from the human brain. <em>Brain</em>, 144(3), 863-874. <a href="https://doi.org/10.1093/brain/awab285" target="_blank">doi:10.1093/brain/awab285</a></li>
<li>Lee, J.-C., Wang, C.-Y., Lin, C.-L., &amp; Lu, H.-C. (2022). Synaptic memory survives molecular turnover. <em>Proceedings of the National Academy of Sciences of the United States of America</em>, 119(42), e2211572119. <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">doi:10.1073/pnas.2211572119</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <em>Science</em>, 384(6696), eadk4858. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Finnema, S. J., Nabulsi, N. B., Eid, T., et al. (2016). Imaging synaptic density in the living human brain. <em>Science Translational Medicine</em>, 8(348), 348ra96. <a href="https://doi.org/10.1126/scitranslmed.aaf6667" target="_blank">doi:10.1126/scitranslmed.aaf6667</a></li>
<li>Naganawa, M., Nabulsi, N., Lin, S.-F., et al. (2021). First-in-human evaluation of 18F-SynVesT-1, a radioligand for PET imaging of synaptic vesicle glycoprotein 2A. <em>Journal of Nuclear Medicine</em>, 62(4), 561-567. <a href="https://doi.org/10.2967/jnumed.120.249144" target="_blank">doi:10.2967/jnumed.120.249144</a></li>
<li>Johansen, A., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <em>Journal of Neuroscience</em>. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Shatalina, E., et al. (2024). The relationship between SV2A levels, neural activity, and cognitive function in healthy humans. <em>Imaging Neuroscience</em>. <a href="https://doi.org/10.1162/imag_a_00190" target="_blank">doi:10.1162/imag_a_00190</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>, 16, 11344. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <em>NMR in Biomedicine</em>, 28(11), 1455-1462. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Li, J., Xu, H. N., Yuan, J., et al. (2025). Dynamic deuterium metabolic imaging reveals whole-brain glucose metabolic turnover and neuronal function in humans. <em>PNAS Nexus</em>, 4(3), pgaf079. <a href="https://doi.org/10.1093/pnasnexus/pgaf079" target="_blank">doi:10.1093/pnasnexus/pgaf079</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., Schildknecht, C. M., Ineichen, B. V., &amp; Pruessmann, K. P. (2024). Myelin bilayer mapping in the human brain in vivo. <em>Magnetic Resonance in Medicine</em>, 91(6), 2332-2344. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Hirschler, L., et al. (2025). Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. <em>Nature Neuroscience</em>, 28, 1115-1126. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., et al. (2026). The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. <em>Nature Communications</em>, 17, 7800. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
</ol>
