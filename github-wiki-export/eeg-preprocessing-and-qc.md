# Wiki: EEG pretreatment and QC

> Pre-processing is not a pretense, it is a condition for acceptance of a claim
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-26 / Role: Technical / practical guide

## Role Of This Page
This page is a wiki that organizes EEG preprocessing and QC not as ``the process of adjusting the waveform at the end,'' but as ``an auditing process that determines which signals should be kept, which derived files can be reused, and which claims should be accepted.''

## Accuracy Notes
We do not provide a one-size-fits-all procedure. From the primary literature and official specifications, we sort out what should be fixed at the bare minimum and what should not be stated yet.

## Back To Public Pages
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Data & Bench](https://mind-upload.com/datasets.html)

## Related Wiki Pages
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - Click here if you want to return from the nature of the signal itself.
- [Wiki: Event synchronization and observation log](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Supplements the time synchronization, event, and bad segment recording required before preprocessing.
- [Wiki: Dataset splits and leakage](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Use this when you need the split unit and hold-out ancestry itself clarified.
- [Wiki: Uncertainty, proofreading, abstaining](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - It supplements the idea of estimation width and abstention using preprocessing differences.
- [Wiki: Standards/Location/Validator/Benchmark](https://github.com/yasufumi-nakata/mind-upload/wiki/standards-repositories-validators-and-benchmarks) - Compensates for the role differences between BIDS, derivatives, public version, loader, and benchmark.

## What Is Currently Known
- Preprocessing is not a small implementation difference, but a choice that determines which signals are considered neural.
- Preprocessing and split design are coupled; fitting ICA, autoreject, normalization, feature selection, or learned denoisers before hold-out can leak test information.
- EEG-BIDS, COBIDAS-MEEG, and BIDS Derivatives provide a concrete floor for reproducible EEG reporting and derivative reuse.
- Cross-dataset scores can move with amplifier, cap, channel layout, reference system, and protocol differences.
- Subject- and session-specific EEG structure is strong enough that sample-based holdouts can overestimate generalization.
- Artifact suppression and signal preservation are different; accuracy alone does not determine the quality of preprocessing.
- A cleaner waveform does not automatically justify a stronger connectivity or causality claim.

## What Is Still Unknown
- It has not yet been decided which split-locked preprocessing bundle is optimal for each EEG problem.
- To determine how much of the high-frequency components can be treated as neural, it is necessary to audit myoelectricity, body movement, and task dependence.
- Which sensitivity-analysis and transform-lineage bundle should become the site-wide standard is still a bench-governance issue.

---

<h2>Shortest conclusion</h2>
<p>
EEG preprocessing is not a process to clean up the diagram. <strong>It is an auditing process that determines which signals are considered neural, which derived files remain reusable, and which claims to withhold.</strong> Therefore, this site treats split-locked transforms, reference methods, filters, artifact treatments, retention rates, setup logs, derivative lineage, and sensitivity analyses as <strong>acceptance conditions</strong> rather than supplements attached to results.
</p>

<strong>Scope of this page</strong>
<p>
Only the technical and natural science aspects will be dealt with here. Philosophy, legal systems, and individuality are not covered. The question to ask is not ``which preprocessing is just?'' but rather ``Which conditions must be fixed to avoid exaggerating EEG-derived claims?''
</p>

<strong>2026-03 correction for the beginner route</strong>
<p>
The older beginner route on this site treated preprocessing mostly as cleanup. That was too weak. For EEG, <strong>site / device / reference system / electrode layout / protocol</strong> are part of the measurement condition, and cleanup tools do not by themselves solve <strong>source leakage</strong>, <strong>ghost interactions</strong>, or <strong>directional identifiability</strong>.
</p>

<strong>2026-03-26 correction: preprocessing is also part of split design</strong>
<p>
One more stop line had to be promoted. The older page still let readers imagine that preprocessing ends before train/test design starts. The recent literature does not support that shortcut. If a step <strong>learns parameters from data</strong>, such as ICA components, autoreject thresholds, ASR calibration, z-score statistics, PCA bases, or learned denoisers, it belongs to the <strong>training split</strong> rather than the pooled dataset. Otherwise the clean derivative has already seen the hold-out distribution.
</p>

<h2>Weaknesses to be explored in depth</h2>
<p>
The older page correctly treated reference methods, filters, artifact handling, and exclusion criteria as major issues. The remaining weakness was subtler: it still let readers imagine preprocessing as if it were only <strong>waveform cleanup</strong>, rather than part of <strong>split design</strong>, <strong>derivative provenance</strong>, and <strong>shortcut control</strong>. COBIDAS-MEEG and EEG-BIDS already provide a concrete reporting floor, the PREP pipeline shows the interdependence of bad-channel detection and rereference, and Widmann et al. established that the filter design itself can drive waveform and latency. Recent work forces three more corrections. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">Kessler et al. (2025)</a> explicitly discuss latent leakage in preprocessing operations such as ICA and autoreject, <a href="https://doi.org/10.3389/fnins.2024.1373515" target="_blank">Brookshire et al. (2024)</a> show that segment-based holdout leaks subject-specific information in translational EEG, and <a href="https://doi.org/10.1016/j.compbiomed.2025.110608" target="_blank">Del Pup et al. (2025)</a> show that sample-based cross-validation overestimates performance and that nested subject-based strategies are more realistic. At the same time, BIDS Derivatives now make source lineage and processing labels part of reusability rather than optional bookkeeping. Therefore, this issue is not a practical trick, but part of the core ceiling of EEG-derived claims.
</p>

<h2>Ten audit gates to fix first</h2>
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
<td>EEG-BIDS and COBIDAS-MEEG require minimal recording of references, ground, sampling rate, filters, bad channels, electrode coordinates, events, and exclusion rules.</td>
<td>Write it as ``reproducible EEG analysis'' or ``comparable clean EEG.''</td>
</tr>
<tr>
<td><strong>split-locked transform gate</strong></td>
<td>Generic ML guidance and EEG-specific studies now support the stricter rule that any transform fitted from data must be learned on the training split, not the pooled dataset.</td>
<td>Reading a cross-session or cross-subject score as if the hold-out data were genuinely unseen.</td>
</tr>
<tr>
<td><strong>derivative-lineage / ancestry gate</strong></td>
<td>BIDS Derivatives require explicit source lineage, processing labels, and derivative naming to make cleaned data critically reusable in later processing.</td>
<td>Reading a clean derivative as reusable or comparable when the source files and processing branch are not recoverable.</td>
</tr>
<tr>
<td><strong>reference gate</strong></td>
<td>PREP pipeline and reference comparison studies show that bad-channel processing and rereference drive waveform and network metrics.</td>
<td>Reading topology, connectivity, or topography in sensor space without reference dependence disclosure.</td>
</tr>
<tr>
<td><strong>setup-distribution / harmonization gate</strong></td>
<td>Cross-dataset studies and channel-location benchmarks show that amplifier, cap, channel map, reference, sampling rate, and protocol differences can change the result even before the model changes.</td>
<td>Reading a cross-dataset or cross-site score as if it reflected only the target neural variable.</td>
</tr>
<tr>
<td><strong>filter gate</strong></td>
<td>Widmann et al. explained that cutoff, transition band, filter order, and causal/acausal application can distort waveform and latency.</td>
<td>Emphasizing ERP onset, slow components, or high-frequency gain without knowing the filter design.</td>
</tr>
<tr>
<td><strong>artifact gate</strong></td>
<td>ICA, ICLabel, Autoreject, PREP, ASR, and ZapLine are promising cleanup tools, but research in 2025 showed that artifact correction does not necessarily improve decoding accuracy.</td>
<td>Reading ``the preprocessing that produces the highest accuracy'' as automatically the best preprocessing.</td>
</tr>
<tr>
<td><strong>shortcut / fingerprint gate</strong></td>
<td>Subject-specific and session-specific EEG structure can dominate the score if split design, nuisance channels, and residual acquisition fingerprints are not audited separately.</td>
<td>Reading a diagnostic or decoding score as target-specific neural evidence before ruling out subject/session shortcut routes.</td>
</tr>
<tr>
<td><strong>connectivity ceiling gate</strong></td>
<td>wPLI can reduce some zero-lag mixing, but simulation and source-space studies show that source leakage, ghost interactions, and pipeline dependence remain separate limits.</td>
<td>Reading artifact-cleaned connectivity or directed metrics as leak-proof or causal by metric name alone.</td>
</tr>
<tr>
<td><strong>retention / high-frequency audit gate</strong></td>
<td>Myoelectricity overlaps with high beta/gamma, and aggressive cleaning can also reduce neural signals. Therefore retained trials, interpolation rate, exclusion rate, and raw-clean differences must remain numeric.</td>
<td>Reading high beta/gamma claims or heavily cleaned data as sufficient by default.</td>
</tr>
</tbody>
</table>

<h2>1. The reporting floor is the metadata, not the algorithm name</h2>
<p>
What EEG-BIDS and its official specifications first fix is not the flashy pipeline name, but what is measured, how it is measured, and in what state it is stored. You can write sampling frequency, low / high cutoff, notch, and channel status in <code>channels.tsv</code>, while <code>electrodes.tsv</code> and <code>coordsystem.json</code> fix the electrode position and coordinate system. COBIDAS-MEEG similarly requires detailed reporting of reference methods, filters, bad-channel handling, exclusion rules, and artifact handling. The simple conclusion here is that <strong>clean EEG without metadata cannot be treated as a reproducible artifact</strong>.
</p>

<strong>Rules on this site</strong>
<p>
At a minimum, leave the <strong>raw reference</strong>, <strong>rereference method</strong>, <strong>filters</strong>, <strong>bad channel / bad segment criteria</strong>, <strong>electrode coordinates</strong>, <strong>event timing</strong>, and <strong>exclusion rules</strong>. Even if you only post processed data, it will not be accepted unless you can track the difference from raw to clean.
</p>

<h2>2. If preprocessing learns from data, it belongs inside the training split</h2>
<p>
This is the correction that needed to become explicit on this page. The general ML rule is already simple: split first, then fit preprocessing on the training data and apply it to the hold-out data. EEG-specific work now shows why that generic rule matters here. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">Kessler et al. (2025)</a> explicitly discuss latent leakage from operations such as high-pass filtering, ocular ICA, and autoreject, and consider temporally separated segments or fold-wise preprocessing as countermeasures. <a href="https://doi.org/10.3389/fnins.2024.1373515" target="_blank">Brookshire et al. (2024)</a> show that random segment-based holdout can leak subject-specific patterns, and <a href="https://doi.org/10.1016/j.compbiomed.2025.110608" target="_blank">Del Pup et al. (2025)</a> show that sample-based cross-validation overestimates performance and that nested subject-based cross-validation is more realistic. Therefore, on this site, <strong>any preprocessing step that estimates parameters from data is part of split design, not a pre-split background routine</strong>.
</p>
<table>
<thead>
<tr>
<th>Transform family</th>
<th>What is learned from data</th>
<th>Site rule</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fixed preregistered transforms</strong></td>
<td>Nothing is estimated from the specific dataset once coefficients are fixed in advance.</td>
<td>These may be applied consistently across the dataset, but their parameters still have to be disclosed and sensitivity checked.</td>
</tr>
<tr>
<td><strong>ICA / ASR / Autoreject / bad-channel models</strong></td>
<td>Components, thresholds, subspaces, or channel / epoch decisions are learned from the data.</td>
<td>Fit on the training subset or train-only raw segment within each fold, then apply the learned transform to the hold-out data.</td>
</tr>
<tr>
<td><strong>Normalization / PCA / feature selection / learned denoising</strong></td>
<td>Means, variances, bases, selected features, or denoiser weights are learned from the data.</td>
<td>Never estimate these on pooled train+test data if the claim is cross-session, cross-subject, or otherwise hold-out based.</td>
</tr>
</tbody>
</table>

<strong>Rules on this site</strong>
<p>
Do not write ``hold-out performance'' unless the transform-fit boundary is explicit. For every data-fitted step, leave <strong>what was fitted</strong>, <strong>on which split unit</strong>, <strong>using which data subset</strong>, and <strong>which learned object was applied to the test fold</strong>.
</p>

<h2>3. Clean EEG is reusable only when derivative lineage and ancestry remain explicit</h2>
<p>
The next weakness was provenance. BIDS Derivatives now makes the rule concrete: derivatives are outputs of common processing pipelines that must capture enough data and metadata for a researcher to understand and <strong>critically reuse</strong> them. The specification explicitly provides <strong><code>Sources</code></strong>, <strong><code>source_entities</code></strong>, <strong><code>desc-&lt;label&gt;</code></strong>, and <strong><code>descriptions.tsv</code></strong> so later users can tell which raw or prior derivative files directly generated the cleaned EEG branch. This matters even more in EEG decoding, because windows, epochs, or averaged segments can inherit strong similarity from the same raw recording, the same session, or the same subject. If raw-window ancestry is lost, a clean derivative can look portable even when nearby windows from the same run crossed the hold-out boundary.
</p>
<table>
<thead>
<tr>
<th>What to keep</th>
<th>Why it matters</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Direct source files</strong></td>
<td>It shows which raw run or prior derivative directly generated the cleaned file.</td>
</tr>
<tr>
<td><strong><code>desc-&lt;label&gt;</code> processing branch</strong></td>
<td>It distinguishes filtered, downsampled, rereferenced, or otherwise different clean versions of the same raw input.</td>
</tr>
<tr>
<td><strong>Window / epoch ancestry</strong></td>
<td>It prevents adjacent or overlapping segments from being mistaken for independent evidence.</td>
</tr>
<tr>
<td><strong>Split unit and hold-out ancestry</strong></td>
<td>It shows whether train and test were disjoint by subject, session, run, or continuous raw recording.</td>
</tr>
</tbody>
</table>

<strong>Rules on this site</strong>
<p>
If you publish a cleaned EEG derivative, leave enough information to reconstruct the branch: <strong>source files</strong>, <strong>processing labels</strong>, <strong>software / version</strong>, <strong>split unit</strong>, and <strong>raw-window ancestry</strong>. A pretty cleaned file name is not enough provenance.
</p>

<h2>4. The reference method is not a small implementation difference; it is part of the observation model</h2>
<p>
EEG is a potential-difference measurement, so changing the reference changes the waveform, topography, and sensor-space connectivity. What the PREP pipeline emphasized is that <strong>taking the average reference while overlooking bad channels contaminates the rereference itself</strong>. Furthermore, reference comparison studies show that functional-connectivity graphs and task-related network metrics change depending on the reference. Therefore, on this site, references are treated as <strong>premises that determine the meaning of results</strong>, rather than as ``implementation notes.''
</p>
<table>
<thead>
<tr>
<th>Minimum things to write</th>
<th>Why it is necessary</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Recording reference / ground</strong></td>
<td>The assumption behind the raw potential difference changes with it.</td>
</tr>
<tr>
<td><strong>Rereference method</strong></td>
<td>The meaning of a sensor-space metric changes with average, linked mastoid, REST, and other schemes.</td>
</tr>
<tr>
<td><strong>Bad-channel handling before rereference</strong></td>
<td>Broken channels contaminate the rereference itself if they are included.</td>
</tr>
<tr>
<td><strong>Number of interpolated channels</strong></td>
<td>It separates what was truly measured from what was spatially reconstructed.</td>
</tr>
</tbody>
</table>

<h2>5. Setup distribution and harmonization are not background noise</h2>
<p>
Two EEG datasets can use the same task name and still represent different measurement conditions. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a> showed that deep-learning EEG decoding changes across datasets when amplifier, cap, sampling rate, and filtering change, and <a href="https://doi.org/10.1016/j.brainresbull.2024.110906" target="_blank">Dong et al. (2024)</a> showed that even motor-imagery BCI comparisons require explicit harmonization across channel-location schemes. Therefore, this site does not treat <strong>site / device / reference system / electrode layout / protocol</strong> as background nuisance. They are part of the observation model.
</p>

<strong>Rules on this site</strong>
<p>
If the claim spans more than one site, dataset, or recording setup, disclose the setup distribution and how harmonization was performed. Without that, a score is not read here as clean evidence of neural generalization.
</p>

<h2>6. A filter is not only a "pass-through band" but also a distortion design</h2>
<p>
As explained by Widmann et al., it is not enough to write only the cutoff frequency of a filter. Transition band, filter order, passband / stopband ripple, causal / acausal application, and forward-backward usage can all move latency and waveform shape. Therefore, claims such as seeing a <strong>slow wave</strong>, an <strong>earlier onset</strong>, or an <strong>increase in gamma</strong> cannot be accepted without a record of the filter design.
</p>

<strong>Rules on this site</strong>
<p>
Regarding filters, leave not only the cutoff of <strong>high-pass</strong>, <strong>low-pass</strong>, and <strong>notch</strong>, but also <strong>filter type</strong>, <strong>order</strong>, <strong>causal / acausal</strong>, and the presence of <strong>forward-backward</strong>. When claiming ERP or latency, check conclusion drift in at least one alternative setting.
</p>

<h2>7. Artifact suppression is not always an improvement</h2>
<p>
ICA, ICLabel, Autoreject, PREP, ASR, and ZapLine are strong practical candidates. However, the important point here is not ``which one was used,'' but whether it is possible to audit what was cut, what was left, and where each step was fitted. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">Kessler et al. (2025)</a> showed that artifact correction does not necessarily improve decoding performance and can reduce accuracy when artifact-related confounds are removed. This does not mean that cleaning is meaningless, but rather that maximizing accuracy and maximizing neural specificity are not synonymous.
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
<td>Clean the floor for line noise, bad channels, and robust reference.</td>
<td>Task-specific artifacts and signal preservation still require a separate audit.</td>
</tr>
<tr>
<td><strong>Autoreject</strong></td>
<td>Automate threshold adjustment and interpolation in trial/sensor units.</td>
<td>Retention, signal preservation, and split-aware fitting still have to be checked separately.</td>
</tr>
<tr>
<td><strong>ICA + ICLabel</strong></td>
<td>Flag candidate ocular, myoelectric, and cardiac components.</td>
<td>Component removal can also reduce neural signal, and pooled fitting can leak structure across folds.</td>
</tr>
<tr>
<td><strong>ASR / ZapLine</strong></td>
<td>Suppress large-amplitude artifacts and line-noise contamination in a reproducible way.</td>
<td>They are cleanup tools; they do not by themselves solve source leakage, directional identifiability, or shortcut risk.</td>
</tr>
</tbody>
</table>

<strong>Rules on this site</strong>
<p>
When reporting artifact processing, the <strong>method name</strong> is not sufficient. Include <strong>number of components / epochs / channels removed</strong>, <strong>interpolation rate</strong>, <strong>minutes / trials retained</strong>, <strong>raw-clean key metric differences</strong>, and, where possible, <strong>comparison with one alternative pipeline</strong>. If the method was fitted from data, also state <strong>where it was fitted</strong>.
</p>

<h2>8. Shortcut and fingerprint audit starts before the classifier</h2>
<p>
One more weakness on the older page was to leave shortcut auditing to later decoding pages. That is too weak. <a href="https://doi.org/10.3389/fnins.2024.1373515" target="_blank">Brookshire et al. (2024)</a> show that segments from the same subject are more similar to each other than to segments from different subjects, which is exactly why segment-based holdout can look deceptively strong. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> show how subject characteristics can confound machine-learning performance, and <a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">Gibson et al. (2022)</a> show that EEG variability can track stable subject identity more strongly than dynamic task state. Therefore, preprocessing review must already ask which residual patterns could still carry <strong>subject identity</strong>, <strong>session identity</strong>, or <strong>acquisition-distribution identity</strong>.
</p>
<table>
<thead>
<tr>
<th>Residual pattern to audit</th>
<th>Why preprocessing has to log it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Subject-specific spectrum / noise floor</strong></td>
<td>It can travel through normalization and windowing into the classifier as a stable identity cue.</td>
</tr>
<tr>
<td><strong>Bad-channel map / interpolation pattern</strong></td>
<td>It can act as a recording signature rather than a neural variable of interest.</td>
</tr>
<tr>
<td><strong>Reference / montage / device chain</strong></td>
<td>It can create acquisition fingerprints that survive cleanup and inflate apparent transfer.</td>
</tr>
<tr>
<td><strong>EOG / EMG / motion residuals</strong></td>
<td>They can correlate with task labels and raise accuracy while reducing neural specificity.</td>
</tr>
<tr>
<td><strong>Temporal adjacency of windows</strong></td>
<td>Neighboring windows from one run can look independent while still carrying nearly identical nuisance structure.</td>
</tr>
</tbody>
</table>

<strong>Rules on this site</strong>
<p>
Before promoting a score, log at least one <strong>nuisance-only or shortcut-aware baseline</strong>, the <strong>hold-out unit</strong>, and which <strong>residual fingerprint routes</strong> remain unresolved after preprocessing.
</p>

<h2>9. Cleanup is not connectivity validation</h2>
<p>
It is tempting to think that once artifacts and line noise are suppressed, network metrics can be read more strongly. That is still too aggressive. Vinck et al. (2011) made wPLI safer against some zero-lag mixing, but Haufe et al. (2013) showed severe limits of sensor-space connectivity under volume conduction, Palva et al. (2018) showed ghost interactions even in source space, and Miljevic et al. (2025) showed strong dependence on rereference and epoch design. Therefore, this site does not promote a connectivity or directed-connectivity result only because the cleanup pipeline looks stronger.
</p>

<strong>Rules on this site</strong>
<p>
If a paper or result outputs connectivity, directed connectivity, STE, Granger, or source-space graph measures, add a separate note stating what leakage control, external validation, and abstention boundary are still missing. Cleanup logs and connectivity validation logs are not interchangeable.
</p>

<h2>10. High beta/gamma does not write strongly without electromyographic audit</h2>
<p>
As outlined by Muthukumaraswamy, muscle artifacts overlap widely around 20-300 Hz and can be difficult to distinguish from high beta/gamma neural components. Therefore, if you claim increased <strong>high-frequency power</strong> in a task that tends to recruit forehead, jaw, or temporalis muscles, at least check <strong>topography</strong>, <strong>EOG / EMG auxiliary channels</strong>, and <strong>residual jaw / brow activity before and after cleaning</strong>. On this site, gamma is not read as neural gain without passing that audit.
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
<td>Reference, ground, device chain, sampling rate, line frequency, electrode coordinates, and event timing.</td>
</tr>
<tr>
<td><strong>split / evaluation manifest</strong></td>
<td>Evaluation family, hold-out unit, and whether train and test were disjoint by subject, session, run, and raw-recording ancestry.</td>
</tr>
<tr>
<td><strong>transform-fit ledger</strong></td>
<td>For each step, state whether it was fixed in advance or learned from data, what was fitted, and on which split subset it was fitted.</td>
</tr>
<tr>
<td><strong>derivative-lineage manifest</strong></td>
<td>Leave source files, processing labels, software version, and raw-to-clean ancestry so the clean branch remains auditable.</td>
</tr>
<tr>
<td><strong>bad channel / bad segment ledger</strong></td>
<td>Leave the criteria used to judge what was bad and what was interpolated or removed.</td>
</tr>
<tr>
<td><strong>filter design report</strong></td>
<td>Leave cutoff, order, type, causal / acausal choice, and notch.</td>
</tr>
<tr>
<td><strong>artifact model report</strong></td>
<td>Leave the presence of PREP / ICA / ICLabel / Autoreject / ASR / ZapLine, their thresholds, removal counts, and interpolation rate.</td>
</tr>
<tr>
<td><strong>setup / harmonization log</strong></td>
<td>Disclose site, device, channel map, reference system, protocol differences, and the harmonization rule across them.</td>
</tr>
<tr>
<td><strong>raw-clean delta</strong></td>
<td>Compare the amount of change in power spectrum, trial count, channel count, and major features between raw and clean.</td>
</tr>
<tr>
<td><strong>retention summary</strong></td>
<td>Display the number of minutes, number of trials, and number of channels remaining as numeric values.</td>
</tr>
<tr>
<td><strong>sensitivity analysis</strong></td>
<td>Check conclusion drift with at least one alternative reference, artifact, or transform-fit configuration.</td>
</tr>
<tr>
<td><strong>high-frequency exception note</strong></td>
<td>If you claim beta/gamma, explain separately how you passed the EMG audit.</td>
</tr>
<tr>
<td><strong>connectivity-ceiling note</strong></td>
<td>If connectivity or directionality is reported, state separately what leakage control, external validation, and abstention boundary remain.</td>
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
<td>I got a clean waveform, so that is enough</td>
<td>No. Metadata, transform-fit boundary, retention, and raw-clean diffs are all part of the acceptance condition.</td>
</tr>
<tr>
<td>I split after ICA / normalization, so the hold-out is still fair</td>
<td>No. Once the transform has seen pooled data, the test distribution has already influenced the clean derivative.</td>
</tr>
<tr>
<td>Balanced random windows are enough for evaluation</td>
<td>No. Subject identity and temporal adjacency can still leak across train and test.</td>
</tr>
<tr>
<td>The pipeline with the highest decoding accuracy is the best</td>
<td>Artifact confounds and shortcut routes may be driving the score, so specificity and sensitivity analysis come first.</td>
</tr>
<tr>
<td>Average reference is safe, so you do not need to write it</td>
<td>Reference is part of the observation model, so write both raw and rereference.</td>
</tr>
<tr>
<td>It is enough to write only cutoff in the filter</td>
<td>Order, type, and causal / acausal application are also required.</td>
</tr>
<tr>
<td>High beta/gamma increase would be neural</td>
<td>The myoelectric overlap is strong, so do not write it strongly without an EMG audit.</td>
</tr>
<tr>
<td>An automatic pipeline is automatically reproducible</td>
<td>Automation and reproducibility are different; you still need source lineage, fitted-transform logs, removal amounts, and retention rates.</td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>BIDS Specification: Electroencephalography. <a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">official docs</a></li>
<li>BIDS Derivatives: Common data types and metadata. <a href="https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html" target="_blank">official docs</a></li>
<li>Scikit-learn: Common pitfalls and recommended practices. <a href="https://scikit-learn.org/stable/common_pitfalls.html" target="_blank">official docs</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M, Robbins KA. The PREP pipeline: standardized preprocessing for large-scale EEG analysis. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2015.06.014" target="_blank">doi:10.1016/j.jneumeth.2015.06.014</a></li>
<li>Widmann A, Schröger E, Maess B. Digital filter design for electrophysiological data: a practical approach. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2014.08.002" target="_blank">doi:10.1016/j.jneumeth.2014.08.002</a></li>
<li>Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. <em>Frontiers in Human Neuroscience</em>. 2013. <a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">doi:10.3389/fnhum.2013.00138</a></li>
<li>Cao Y, et al. How Different EEG References Influence Sensor Level Functional Connectivity Graphs. <em>Frontiers in Neuroscience</em>. 2017. <a href="https://doi.org/10.3389/fnins.2017.00368" target="_blank">doi:10.3389/fnins.2017.00368</a></li>
<li>Jas M, Engemann DA, Bekhti Y, Raimondo F, Gramfort A. Autoreject: automated artifact rejection for MEG and EEG data. <em>NeuroImage</em>. 2017. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.030" target="_blank">doi:10.1016/j.neuroimage.2017.08.030</a></li>
<li>Pion-Tonachini L, Kreutz-Delgado K, Makeig S. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. <em>NeuroImage</em>. 2019. <a href="https://doi.org/10.1016/j.neuroimage.2019.05.026" target="_blank">doi:10.1016/j.neuroimage.2019.05.026</a></li>
<li>Chang C-Y, Hsu S-H, Pion-Tonachini L, Jung T-P. Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. <em>Proc IEEE EMBC</em>. 2018. <a href="https://doi.org/10.1109/EMBC.2018.8512547" target="_blank">doi:10.1109/EMBC.2018.8512547</a></li>
<li>de Cheveigné A. ZapLine: A simple and effective method to remove power line artifacts. <em>NeuroImage</em>. 2020;207:116356. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356" target="_blank">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li>Kessler V, et al. How EEG preprocessing shapes decoding performance. <em>Communications Biology</em>. 2025. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">doi:10.1038/s42003-025-08464-3</a></li>
<li>Brookshire G, Kasper J, Blauch NM, et al. Data leakage in deep learning studies of translational EEG. <em>Frontiers in Neuroscience</em>. 2024;18:1373515. <a href="https://doi.org/10.3389/fnins.2024.1373515" target="_blank">doi:10.3389/fnins.2024.1373515</a></li>
<li>Del Pup F, Zanola A, Tshimanga LF, et al. The role of data partitioning on the performance of EEG-based deep learning models in supervised cross-subject analysis: A preliminary study. <em>Computers in Biology and Medicine</em>. 2025;196(Pt A):110608. <a href="https://doi.org/10.1016/j.compbiomed.2025.110608" target="_blank">doi:10.1016/j.compbiomed.2025.110608</a></li>
<li>Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <em>npj Digital Medicine</em>. 2019;2:99. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Gibson E, Lobaugh NJ, Joordens S, McIntosh AR. EEG variability: Task-driven or subject-driven signal of interest? <em>NeuroImage</em>. 2022;252:119034. <a href="https://doi.org/10.1016/j.neuroimage.2022.119034" target="_blank">doi:10.1016/j.neuroimage.2022.119034</a></li>
<li>Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. <em>Frontiers in Human Neuroscience</em>. 2020;14:103. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Dong C, Jia T, Wang S, et al. Benchmarking of different channel locations for motor imagery based BCI. <em>Brain Research Bulletin</em>. 2024;210:110906. <a href="https://doi.org/10.1016/j.brainresbull.2024.110906" target="_blank">doi:10.1016/j.brainresbull.2024.110906</a></li>
<li>Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CMA. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>. 2011;55(4):1548-1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. <em>NeuroImage</em>. 2013;64:120-133. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva JM, Wang SH, Palva S, et al. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <em>NeuroImage</em>. 2018;173:632-643. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Miljevic A, Murphy OW, Fitzgerald PB, Bailey NW. Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. <em>Clinical Neurophysiology</em>. 2025;174:73-83. <a href="https://doi.org/10.1016/j.clinph.2025.03.043" target="_blank">doi:10.1016/j.clinph.2025.03.043</a></li>
</ol>
