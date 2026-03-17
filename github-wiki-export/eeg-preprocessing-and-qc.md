# Wiki: EEG pretreatment and QC

> Pre-processing is not a pretense, it is a condition for acceptance of a claim
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-15 / Role: Technical / practical guide

## Role Of This Page
This page is a wiki that organizes EEG preprocessing and QC not as ``the process of adjusting the waveform at the end,'' but as ``an auditing process that determines which signals should be kept and which claims should be accepted.''

## Accuracy Notes
We do not provide a one-size-fits-all procedure. From the primary literature and official specifications, we will sort out what should be fixed at the bare minimum and what should not be stated yet.

## Back To Public Pages
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Data & Bench](https://mind-upload.com/datasets.html)

## Related Wiki Pages
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - Click here if you want to return from the nature of the signal itself.
- [Wiki: Event synchronization and observation log](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Supplements the time synchronization, event, and bad segment recording required before preprocessing.
- [Wiki: Uncertainty, proofreading, abstaining](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - It supplements the idea of estimation width and abstention using preprocessing differences.
- [Wiki: Standards/Location/Validator/Benchmark](https://github.com/yasufumi-nakata/mind-upload/wiki/standards-repositories-validators-and-benchmarks) - Compensates for the role differences between BIDS, public version, loader, and benchmark.

## What Is Currently Known
- Preprocessing is not a small implementation difference, but a choice that determines which signals are considered neural.
- Reference method, filter design, bad channel processing, and exclusion criteria are the minimum information that should be kept.
- EEG-BIDS and COBIDAS-MEEG provide a fairly concrete floor for reproducible EEG reporting.
- Artifact suppression and signal preservation are different; accuracy alone does not determine the quality of preprocessing.

## What Is Still Unknown
- It has not yet been decided which preprocessing group is optimal for which problem.
- To determine how much of the high-frequency components can be treated as neural, it is necessary to audit myoelectricity, body movement, and task dependence.
- Which sensitivity analysis set should be the site-wide standard is a future bench operation issue.

---

<h2>Shortest conclusion</h2>
<p>
EEG preprocessing is not a process to clean up the diagram. <strong>This is an auditing process that determines which signals are considered neural and which claims to withhold. Therefore, this site treats reference methods, filters, artifact treatments, retention rates, and sensitivity analyzes as <strong>acceptance conditions</strong> rather than supplements attached to results.
</p>

<strong>Scope of this page</strong>
<p>
Only the technical and natural science aspects will be dealt with here. Philosophy, legal systems, and individuality are not covered. The question to ask is not ``which preprocessing is just?'' but rather ``Which conditions must be fixed to exaggerate EEG-derived claims?''
</p>

<h2>Weaknesses to be explored in depth</h2>
<p>
The previous page correctly listed four issues: reference methods, filters, artifact handling, and exclusion criteria. However, the weakness is that <strong>why they can change the results themselves</strong> and <strong>what must be left behind to raise the level of claims</strong> was not an audit gate based on primary literature. COBIDAS-MEEG and EEG-BIDS provide a fairly concrete reporting platform, the PREP pipeline shows the interdependence of bad channel and rereference, and Widmann et al. have established that the filter design itself can drive waveform and latency. Additionally, a 2025 decoding study shows that artifact correction does not always mean improved performance. Therefore, this issue is not a practical trick, but is the main body that determines the ceiling of EEG-derived claims.
</p>

<h2>Five audit gates to fix first</h2>
<table>
<thead>
<tr>
<th>Gate</th>
<th>What primary documents and official specifications currently support</th>
<th>Assertion to stop when not passing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>metadata / reporting gate</strong></td>
<td>EEG-BIDS and COBIDAS-MEEG require minimal recording of references, ground, sampling rate, filters, bad channels, electrode coordinates, events, and exclusion rules. </td>
<td>Write it as ``reproducible EEG analysis'' or ``comparable clean EEG.'' </td>
</tr>
<tr>
<td><strong>Reference gate</strong></td>
<td>PREP pipeline and reference comparison studies show that bad channel processing and rereference drive waveform and network metrics. </td>
<td>Reading the topology, connectivity, and topography of sensor-space without reference dependencies. </td>
</tr>
<tr>
<td><strong>filter gate</strong></td>
<td>Widmann et al. explained that cutoff, transition band, filter order, and causal/acausal can distort waveform and latency. </td>
<td>Emphasis on ERP onset, slow component, and high-frequency gain without knowing the filter design. </td>
</tr>
<tr>
<td><strong>artifact gate</strong></td>
<td>ICA, ICLabel, Autoreject, PREP, etc. are promising, but research in 2025 showed that artifact correction does not necessarily improve decoding accuracy, but rather can reduce accuracy as a result of reducing confound. </td>
<td>It is read as "the preprocessing that produces the highest accuracy is the best." </td>
</tr>
<tr>
<td><strong>Retention Rate / High Frequency Audit Gate</strong></td>
<td>Myoelectricity overlaps with high beta/gamma, and aggressive cleaning can also reduce neural signals. Therefore, it is necessary to keep numerical values ​​for retained trials, interpolation rate, exclusion rate, and raw-clean differences. </td>
<td>High beta/gamma neural claims and data after cleaning are sufficient. </td>
</tr>
</tbody>
</table>

<h2>1. The reporting floor is the metadata, not the algorithm name</h2>
<p>
What EEG-BIDS and its official specifications first fix is not the flashy pipeline name, but what is measured, how it is measured, and in what state it is stored. You can write sampling frequency, low / high cutoff, notch, and channel status in `channels.tsv`, and `electrodes.tsv` and `coordsystem.json` fix the electrode position and coordinate system. COBIDAS-MEEG similarly requires detailed reporting of reference methods, filters, bad channel handling, exclusion rules, and artifact handling. The simple conclusion here is that <strong>clean EEG without metadata cannot be treated as a reproducible artifact</strong>.
</p>

<strong>Rules on this site</strong>
<p>
At a minimum, please leave the <strong>raw reference</strong>, <strong>rereference method</strong>, <strong>filters</strong>, <strong>bad channel / bad segment</strong>, <strong>electrode coordinates</strong>, <strong>event time</strong>, and <strong>exclusion rules</strong>. Even if you only post processed data, it will not be accepted unless you can track the difference from raw to clean.
</p>

<h2>2. The reference method is not a small implementation difference; it is part of the observation model</h2>
<p>
EEG is a potential difference measurement, so changing the reference changes the waveform, topography, and sensor-space connectivity. What the PREP pipeline emphasized is that<strong>taking the average reference while overlooking the bad channel pollutes the rereference itself</strong>. Furthermore, in reference comparison studies, functional connectivity graphs and task-related network metrics change depending on the reference. Therefore, on this site, references are treated as <strong>premises that determine the meaning of results</strong>, rather than as ``implementation notes.''
</p>
<table>
<thead>
<tr>
<th>Minimum things to write</th>
<th>Why is it necessary</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>When recording reference / ground</strong></td>
<td>This is because the assumption of raw potential difference changes. </td>
</tr>
<tr>
<td><strong>rereference method</strong></td>
<td>This is because the meaning of the sensor-space metric changes with average, linked mastoid, REST, etc. </td>
</tr>
<tr>
<td><strong>Bad channel handling before rereference</strong></td>
<td>This is because mixing broken channels contaminates the rereference itself. </td>
</tr>
<tr>
<td><strong>Number of interpolated channels</strong></td>
<td>This is to distinguish between the actual measurement and the interpolation of the spatial pattern. </td>
</tr>
</tbody>
</table>

<h2>3. A filter is not only a "pass-through band" but also a distortion design</h2>
<p>
As explained by Widmann et al., it is not enough to just write the cutoff frequency for filter. Transition band, filter order, passband / stopband ripple, causal / acausal, unidirectional / bidirectional application, latency and waveform move. Therefore, claims such as seeing a<strong>slow wave, an earlier onset, or an increase in gamma cannot be accepted without a record of the filter design.
</p>

<strong>Rules on this site</strong>
<p>
Regarding filter, please leave not only the cutoff of<strong>high-pass</strong>,<strong>low-pass</strong>, and<strong>notch</strong>, but also<strong>filter type</strong>, <strong>order</strong>, <strong>causal / acausal</strong>, and presence of<strong>forward-backward</strong>. When claiming ERP or latency, check conclusion drift in at least one alternative setting.
</p>

<h2>4. Artifact suppression is not always an improvement</h2>
<p>
ICA, ICLabel, Autoreject, PREP, etc. are strong practical candidates. However, the important point here is not ``which one was used'', but whether it is possible to audit what was cut and what was left. A 2025 decoding study showed that artifact correction does not necessarily improve classification performance, but rather can reduce accuracy as a result of reducing artifact-related confounds. This does not mean that cleaning is meaningless, but rather that maximizing accuracy and maximizing neural specificity are not synonymous.
</p>
<table>
<thead>
<tr>
<th>Candidate method</th>
<th>Role</th>
<th>Reason why it is not automatically promoted to standard solution</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PREP</strong></td>
<td>Clean the floor for line noise, bad channel, and robust reference. </td>
<td>This is because task-specific artifacts and signal preservation require a separate audit. </td>
</tr>
<tr>
<td><strong>Autoreject</strong></td>
Automate threshold adjustment and interpolation in <td>trial/sensor units. </td>
<td>This is because it is necessary to separately check how the retention rate and task-relevant signal worked. </td>
</tr>
<tr>
<td><strong>ICA + ICLabel</strong></td>
<td>Candidate independent components such as eyeballs, myoelectrics, and electrocardiograms. </td>
<td>Component removal may reduce the neural component, so full automation is dangerous. </td>
</tr>
</tbody>
</table>

<strong>Rules on this site</strong>
<p>
When reporting artifact processing, <strong>name of method used</strong> is not sufficient. Please include <strong>number of components / epochs / channels removed</strong>, <strong>interpolation rate</strong>, <strong>minutes / trials retained</strong>, <strong>raw-clean key metric differences</strong>, and if possible <strong>comparison with one alternative pipeline</strong>.
</p>

<h2>5. High beta/gamma does not write strongly without electromyographic audit</h2>
<p>
As outlined by Muthukumaraswamy, muscle artifacts overlap widely around 20-300 Hz and can be difficult to distinguish from high beta/gamma neural components. Therefore, if you claim to increase <strong>high-frequency power</strong> in a task that tends to involve activation of the forehead, jaw, and temporalis muscles, at least check for behavioral confound</strong>s such as <strong>topography</strong>, <strong>EOG / EMG auxiliary channels</strong>, <strong>jaw / brow, and residual</strong>before and after cleaning. On this site, we will not read gamma as neural gain without doing this.
</p>

<h2>Minimum submissions</h2>
<table>
<thead>
<tr>
<th>Submission</th>
<th>Minimum desired content</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>acquisition metadata</strong></td>
<td>reference, ground, sampling rate, line frequency, electrode coordinates, event timing. </td>
</tr>
<tr>
<td><strong>bad channel / bad segment ledger</strong></td>
<td>What criteria were used to judge what was bad and what was interpolated is left. </td>
</tr>
<tr>
<td><strong>filter design report</strong></td>
<td>Leave cutoff, order, type, causal / acausal, notch. </td>
</tr>
<tr>
<td><strong>artifact model report</strong></td>
<td>Presence of PREP / ICA / ICLabel / Autoreject, etc., number of removals, threshold, and interpolation rate are left. </td>
</tr>
<tr>
<td><strong>raw-clean delta</strong></td>
<td>Compare the amount of change in power spectrum, trial count, channel count, and major features between raw and clean. </td>
</tr>
<tr>
<td><strong>retention summary</strong></td>
<td>Finally, the number of minutes, number of trials, and number of channels remaining are displayed as numerical values. </td>
</tr>
<tr>
<td><strong>sensitivity analysis</strong></td>
<td>Check the conclusion drift with at least one alternative reference or artifact pipeline. </td>
</tr>
<tr>
<td><strong>high-frequency exception note</strong></td>
<td>If you claim beta/gamma, please separately explain how you passed the EMG audit. </td>
</tr>
</tbody>
</table>

<h2>Misinterpretations that should be avoided from this criticism</h2>
<table>
<thead>
<tr>
<th>Misreading</th>
<th>Replacement on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td>I got a clean waveform, so that's enough</td>
<td>Metadata, retention, and raw-clean diffs are not enough. </td>
</tr>
<tr>
<td>The pipeline with the highest decoding accuracy is the best</td>
<td>Since we may be picking up artifact confounds, we will look at specificity and sensitivity analysis first. </td>
</tr>
<tr>
<td>average reference is safe, so you don't need to write it</td>
<td>Reference is the premise of the result, so write both raw and rereference. </td>
</tr>
<tr>
<td>It is enough to write only cutoff in filter</td>
<td>Order, type, and causal/acausal are required. </td>
</tr>
<tr>
<td>High beta/gamma increase would be neural</td>
<td>Since the myoelectric overlap is strong, I cannot write strongly without an EMG audit. </td>
</tr>
<tr>
<td>Reproducible using automatic pipeline</td>
<td>Automation and reproducibility are two different things and require disclosure of inputs, thresholds, removal amounts, and retention rates. </td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>BIDS Specification: Electroencephalography. <a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">official docs</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M, Robbins KA. The PREP pipeline: standardized preprocessing for large-scale EEG analysis. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2015.06.014" target="_blank">doi:10.1016/j.jneumeth.2015.06.014</a></li>
<li>Widmann A, Schröger E, Maess B. Digital filter design for electrophysiological data: a practical approach. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2014.08.002" target="_blank">doi:10.1016/j.jneumeth.2014.08.002</a></li>
<li>Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. <em>Frontiers in Human Neuroscience</em>. 2013. <a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">doi:10.3389/fnhum.2013.00138</a></li>
<li>Cao Y, et al. How Different EEG References Influence Sensor Level Functional Connectivity Graphs. <em>Frontiers in Neuroscience</em>. 2017. <a href="https://doi.org/10.3389/fnins.2017.00368" target="_blank">doi:10.3389/fnins.2017.00368</a></li>
<li>Jas M, Engemann DA, Bekhti Y, Raimondo F, Gramfort A. Autoreject: automated artifact rejection for MEG and EEG data. <em>NeuroImage</em>. 2017. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.030" target="_blank">doi:10.1016/j.neuroimage.2017.08.030</a></li>
<li>Pion-Tonachini L, Kreutz-Delgado K, Makeig S. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. <em>NeuroImage</em>. 2019. <a href="https://doi.org/10.1016/j.neuroimage.2019.05.026" target="_blank">doi:10.1016/j.neuroimage.2019.05.026</a></li>
<li>Kessler V, et al. How EEG preprocessing shapes decoding performance. <em>Communications Biology</em>. 2025. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">doi:10.1038/s42003-025-08464-3</a></li>
</ol>
