# Wiki: Basics of multimodal integration

> Rather than adding everything, it is designed to increase synchronization, geometry, and external validation.
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Technical / natural science only

## このページの役割
This page is a wiki that organizes what really improves when combining EEG, MEG, fMRI, invasive recording, and MRI based on primary literature. Rather than focusing on philosophy or legal systems, we focus only on synchronization, coordinate alignment, forward models, external validation, and state coverage.

## 正確さの前提
What I'm trying to show here is not that ``if you integrate everything, you can figure it out.'' It's about sorting out what can be said a little more strongly when certain conditions are met, and what can't be said yet.

## 公開ページへ戻る
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Verification base](https://mind-upload.com/verification.html)
- [Technology Roadmap](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - Click here if you want to return to the limits of EEG alone.
- [Wiki: Event synchronization and observation log](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Introduces the basics of shared clocks, delays, jitter, and drift.
- [Wiki: Uncertainty, proofreading, abstaining](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - Compensates for why uncertainty persists with integration.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - An entry point to avoid confusing observed values and estimated values.

## いま分かっていること
- By combining multiple modalities, some aspects of time, space, and locality can be complemented.
- However, the amount of improvement is highly dependent on the shared clock, individual anatomy, electrode/sensor location, conductivity assumptions, and the presence or absence of an external reference.
- Invasive recording is a strong calibration route, but suffers from coverage bias and patient bias.

## まだ分かっていないこと
- It is not yet certain which integration set is most effective for which stage of WBE.
- Even with the integration of multiple modalities, the sufficiency of cells, synapses, neuromodifications, and glial states remain unresolved.
- How to propagate and report post-integration uncertainties remains a research topic.

---

<h2>Conclusion</h2>
<p>
Multimodal integration can compensate for some of the weaknesses of EEG. However, it can also simply replace <strong>one inverse problem with multiple problems involving synchronization, geometry, noise, and external validation</strong>. Therefore, on this site, we do not evaluate only by the fact that ``modalities were added'', but by <strong>which audit gate was passed</strong>.
</p>

<strong>Scope of this page</strong>
<p>
Here we will only deal with the technical and natural science aspects. It does not include issues of identity, consciousness, or the legal system. The question to ask is not ``what could be observed?'' but <strong>what and to what extent could it be audited?
</p>

<h2>Five audit gates to fix first</h2>
<table>
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

<h2>What is currently proven for each major route</h2>
<table>
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
<td>Artifact and safety control tend to deteriorate with magnetic field strength, leaving asymmetry in time resolution and poor EEG quality. </td>
</tr>
<tr>
<td><strong>EEG + invasive recording (ECoG/SEEG/DBS)</strong></td>
<td>Zhang et al. (2006) showed cortical potential reconstruction with simultaneous scalp EEG/ECoG, and Seeber et al. (2019) showed subcortical detectability with 256ch scalp EEG and simultaneous DBS recording. </td>
<td>Coverage is biased toward areas of clinical need, and patient group bias is also unavoidable. There is no whole-brain ground truth. </td>
</tr>
<tr>
<td><strong>OPM-MEG system</strong></td>
<td>Boto et al. (2018) demonstrated the feasibility of MEG measurement under conditions including natural movement using wearable OPM-MEG. </td>
<td>It relies on background field nulling and motion-aware correction, and is not a simple mobile replacement device. </td>
</tr>
</tbody>
</table>

<h2>What each route actually adds</h2>

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
Simultaneous EEG-fMRI is attractive, but as the magnetic field strength increases, artifacts and setup dependence also increase, as shown in two 2015 papers by Jorge et al. Wirsich et al. (2021) showed reproducible connectome analysis over 1.5T to 7T, but this also means that this can only be achieved by incorporating appropriate hardware, cabling, and artifact control. Therefore, it is not just a matter of adding spatial resolution.
</p>

<h3>4. EEG + invasive recording is strong as a calibration route, but coverage is narrow</h3>
<p>
Zhang et al. (2006) used simultaneous scalp EEG/ECoG to show that the main spatial patterns of cortical potential reconstructions can be preserved with realistic FEM and co-registered MRI/CT. Seeber et al. (2019) also showed that deep signals are conditionally detectable using 256ch scalp EEG and simultaneous DBS recording. However, these only strengthen the area visible in the invasion record, and do not guarantee unmeasured areas.
</p>

<h2>Reading rules adopted on this site</h2>

<h4>Rule</h4>
<ul>
<li><strong>multimodal:</strong>Read as "which audit gate was passed through" instead of "multiple modalities were added." </li>
<li><strong>EEG + MRI:</strong>Even if individual anatomy is included, if there is no external validation, the source claim will be limited. </li>
<li><strong>EEG + fMRI:</strong>It is useful as a complement to spatial information, but requires auditing of artifacts, safety, and time series alignment. </li>
<li><strong>EEG + invasive recording: Treated as a coverage-limited calibration/validation route, not a gold standard. </li>
<li><strong>state coverage:</strong>If the synapse, neuromodification, glial, or cell type label is unobserved, it will be marked as unobserved. </li>
</ul>

<h2>References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C., Garrido, M. I., Gramfort, A., et al. (2020). Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>, 23, 1473-1483. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Jorge, J., Grouiller, F., Ipek, O., et al. (2015). Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. <em>NeuroImage</em>, 105, 132-144. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Jorge, J., Grouiller, F., Gruetter, R., et al. (2015). Towards high-quality simultaneous EEG-fMRI at 7 T: Detection and reduction of EEG artifacts due to head motion. <em>NeuroImage</em>, 120, 143-153. <a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">doi:10.1016/j.neuroimage.2015.07.020</a></li>
<li>Wirsich, J., Jorge, J., Iannotti, G. R., et al. (2021). The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. <em>NeuroImage</em>, 231, 117864. <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2014). Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. <em>PLoS ONE</em>, 9(3), e93154. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Zhang, Y., Ding, L., van Drongelen, W., et al. (2006). A cortical potential imaging study from simultaneous extra- and intracranial electrical recordings by means of the finite element method. <em>NeuroImage</em>, 31(4), 1517-1528. <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">doi:10.1016/j.neuroimage.2006.02.027</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657-661. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
</ol>
