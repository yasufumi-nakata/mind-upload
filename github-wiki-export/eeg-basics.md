# Wiki: Basics of EEG

> Basic knowledge to prevent EEG from becoming a magical mind-reading technique
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-14 / Role: Beginner guide

## Role Of This Page
This page is a wiki that explains from the basics what EEG measures. Beyond complicated formulas, the goal is to understand ``what kind of signals are mixed together and where'' and ``why preprocessing and QC are important.''

## Accuracy Notes
We highlight the limitations of EEG so as not to overestimate it, but that doesn't mean it's useless.

## Back To Public Pages
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)

## Related Wiki Pages
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - If you want to see first where EEG fits into the overall WBE, click here.
- [Wiki: EEG pretreatment and QC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - We will organize preprocessing and logging methods in a practical manner.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Understand why EEG also requires standards and QC.

## What Is Currently Known
- EEG is good at looking at time changes in milliseconds.
- The observed signal is the result of a mixture of many activities, and interpretation requires assumptions.
- Including individualized MRI and external references improves source imaging, but uncertainty remains for deep and weak sources.
- Public data provides plenty of practice with preprocessing and baseline comparisons.

## What Is Still Unknown
- It remains unresolved whether non-invasive EEG alone is sufficient to reconstruct detailed causal structures within the brain.
- The choice of preprocessing does not uniformly change the conclusion for each task.
- It is not yet fixed which external benchmark will be the standard validation set for source imaging.

---

<h2>What does the EEG see?</h2>
<p>
EEG is a method that measures electrical potential differences using electrodes placed on the scalp. In other words, we are not looking directly into the brain with a camera, but are reading the mixed signals that are transmitted to the outside as a result of many overlapping activities.
</p>

<strong>Switch to stop on this page first</strong>
<p>
With EEG, it is different to<strong>observe scalp signals, conditionally estimate the brain source, and<strong>uniquely identify internal states. If these three are confused, beginners will read "seen" and "estimated" to mean the same thing.
</p>

<h2>What EEG is good at</h2>
<table>
<thead>
<tr>
<th>What I'm good at</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td>Seeing changes over time</td>
<td>Because EEG can capture signals in milliseconds, it is easy to track when changes occur. </td>
</tr>
<tr>
<td>State transition and event detection</td>
<td>It is suitable for observing conditions that change over time, such as sleep stages and seizure events. </td>
</tr>
<tr>
<td>Reproduction practice with public data</td>
<td>PhysioNet has standard data and it is easy to start practicing L0. </td>
</tr>
</tbody>
</table>

<h2>Things that EEG is bad at</h2>
<table>
<thead>
<tr>
<th>Things I'm not good at</th>
<th>Why is it difficult</th>
</tr>
</thead>
<tbody>
<tr>
<td>Accurately stating "somewhere in the brain"</td>
<td>This is because the signal becomes blurred while passing through the skull and scalp, and the inverse problem cannot be solved uniquely. </td>
</tr>
<tr>
<td>Knowing the deep structure in detail</td>
<td>Activities far from the scalp and weak signals are difficult to observe. </td>
</tr>
<tr>
<td>Making a strong claim of identity using EEG alone</td>
<td>EEG is an important clue, but it alone cannot confirm memories, values, or causal continuity. </td>
</tr>
</tbody>
</table>

<h2>Observation, estimation, and identification are different</h2>
<table>
<thead>
<tr>
<th>stage</th>
<th>What can be said with EEG</th>
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observation</strong></td>
<td>The mixed potential on the scalp can be taken on the ms scale. It is good at tracking state transitions and event times. </td>
<td>We cannot say that we have directly seen which deep source is the sole cause, including cell types and neuronal modifications. </td>
</tr>
<tr>
<td><strong>Conditional estimation</strong></td>
<td>Including individual MRI, electrode coordinates, and forward model will improve the estimation of near-cortical and some deep activities. </td>
<td>Being able to detect when the conditions are severe is different from being able to restore uniqueness in general. </td>
</tr>
<tr>
<td><strong>Identification</strong></td>
<td>External criteria such as intracranial stimulation, simultaneous SEEG/ECoG, phantoms, and postoperative outcomes allow for error auditing. </td>
<td>Without an external standard, it is impossible to say ``I have found the source'' or ``I have achieved a sufficient state for WBE.'' </td>
</tr>
</tbody>
</table>

<strong>2026-03 actual measurement evidence</strong>
<p>
Seeber et al. (2019) demonstrated detectability of subcortical signals with 256ch scalp EEG and simultaneous DBS recordings, but did not claim general unique reconstruction. Unnwongse et al. (2023) reported that localization error depends on cranial conductivity and source depth in direct validation for intracranial stimulation, and Hao et al. (2025) showed that source power and source depth strongly influence error in 29 cases of simultaneous HD-EEG/SEEG. Therefore, the correct way to read it is ``partially auditable if the conditions are strictly fixed'', not ``the brain source can be uniquely read using EEG alone''.
</p>

<h2>Why QC and pretreatment are important</h2>
<p>
EEG is a measurement that is susceptible to noise. Results vary depending on eye blinks, myoelectricity, body movements, power supply noise, reference electrode placement, filter settings, etc. Therefore, it is not enough just to have a diagram that looks good, it is necessary to record how it was processed.
</p>

<h4>What you want to keep as a minimum</h4>
<ul>
<li><strong>Reference method:</strong>What standard was used to measure the potential difference? </li>
<li><strong>Filter:</strong>Which frequency band is passed through? </li>
<li><strong>Artifact processing:</strong>Which noise was removed and how? </li>
<li><strong>Exclusion criteria:</strong>Which data were excluded and why? </li>
</ul>

<h2>How to connect with WBE</h2>
<p>
EEG is not a device that suddenly completes WBE. However, it is important for providing time information on state changes, baseline comparison, and reproducibility with public data. At Mind-Upload, we treat EEG not as a device that reads everything, but as an observation tool that provides macroscopic constraints.
</p>

<h4>Next</h4>
<p>Click here to read research involving EEG based on the strength of claims and evidence. </p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence">How to read claims and evidence →</a>

<h4>Practical Next</h4>
<p>Click here if you want to see what changes with reference methods, filters, and artifact processing from a practical perspective. </p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc">To EEG preprocessing and QC →</a>

<h4>Technical Next</h4>
<p>Click here if you would like to see the boundaries between observation and estimation, and the connections between ESI, DCM, and SCM. </p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-and-modeling-terms">From measurement to modeling →</a>

<h2>References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review of the analysis steps. <em>Frontiers in Neurology</em>, 10, 325. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, Y., Alhilani, M., Asano, E., et al. (2025). High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. <em>Epilepsia</em>. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
</ol>
