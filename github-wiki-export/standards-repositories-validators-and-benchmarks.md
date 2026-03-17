# Wiki: Standards/Location/Validator/Benchmark

> Divides similar-looking infrastructure groups, including version fixing and evaluation fixing
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: Operational guide

## このページの役割
This page is a wiki that organizes the roles of ``Standards,'' ``Stores,'' ``Validators,'' and ``Benchmarks,'' which appear many times in Mind-Upload, as well as ``version fixing,'' ``event semantics,'' ``synchronization middleware,'' ``loaders/converters,'' and ``benchmark harnesses,'' which are important in practice. The goal is not to memorize just the names, but to understand ``where reproducibility is most likely to break down.''

## 正確さの前提
What I will explain here is a basic organization of roles. BIDS vessels, HED semantics, and LSL synchronization are complementary, and the final validity of any one is not guaranteed.

## 公開ページへ戻る
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Verification base](https://mind-upload.com/verification.html)
- [Casework](https://mind-upload.com/verification.html#casework)

## 関連 Wiki
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Return to the larger map of Standards, Bench, Registration, and Audit.
- [Wiki: Baseline/Pre-registration/Model Card](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Compensates for differences in operational language beyond Benchmark.
- [Wiki: Event synchronization and observation log](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Add specific examples of log information you want to include in the standard.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other auxiliary pages.

## いま分かっていること
- To make research comparable, it is necessary to separate the data format, publication destination, testing methods, and evaluation rules.
- BIDS and EEG-BIDS are standards for 'how to place' them, not scoring rules themselves.
- Event semantics like HED have the role of supplementing the meaning of events listed in BIDS in a machine-readable manner.
- LSL helps with clock alignment between streams, but is not the ground truth for hardware delays.
- OpenNeuro and PhysioNet are public platforms, but they do not automatically guarantee all input formats and evaluation procedures.
- Even if the dataset name is the same, it cannot be compared if the snapshot / version and evaluation family are different.

## まだ分かっていないこと
- It is unclear what granularity the final common benchmark for WBE should be.
- Which validators and audit items will become the final standard will depend on future operational design.

---

<h2>The shortest distinction</h2>
<p>
<strong>Standards</strong> are the rules for ``how to arrange them,'' <strong>location</strong> is for ``where to publish them,'' <strong>Validator</strong> is a ``tool to mechanically check that the standards are met,'' and <strong>benchmarks</strong> are rules for ``what to compare.'' Even though they are the same ``research infrastructure,'' their roles are different.
</p>

<h2>Why consider separately</h2>
<p>
If you confuse these four things, you'll get the wrong impression, such as, ``There's a benchmark because you uploaded it to OpenNeuro,'' or ``Because it's BIDS, you've already done the comparison.'' In reality, the task of aligning data and the task of creating comparison rules are two different things.
</p>

<h2>First, separate terms</h2>
<table>
<thead>
<tr>
<th>Term</th>
<th>What it does</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>standard</strong></td>
<td>The way to place the file, name it, and write the metadata will be the same. </td>
<td>BIDS, EEG-BIDS. </td>
</tr>
<tr>
<td><strong>Storage/shared infrastructure (repository)</strong></td>
<td>Publish your data so others can retrieve it. </td>
<td>OpenNeuro, PhysioNet, PDB, etc. </td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>Mechanically inspects for standard violations and missing metadata. </td>
<td>BIDS Validator. </td>
</tr>
<tr>
<td><strong>benchmark</strong></td>
<td>Fix issues, divisions, indicators, and prohibitions to make them comparable. </td>
<td>MOABB, MLPerf, ImageNet type operation. </td>
</tr>
</tbody>
</table>

<h2>In practice, 4 layers are not enough, so we look at 7 layers</h2>
<table>
<thead>
<tr>
<th>layer</th>
<th>Representative examples</th>
<th>What to fix here</th>
<th>No guarantees yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Standards</strong></td>
<td>BIDS, EEG-BIDS</td>
<td>File name, required metadata, coordinate system, events/channels/electrodes format. </td>
<td>train/test Splits and indicators are not determined. </td>
</tr>
<tr>
<td><strong>2. Public version</strong></td>
<td>OpenNeuro snapshot, PhysioNet version</td>
<td>A third party can return to the same input to know which version was obtained. </td>
<td>The version does not necessarily fix the benchmark split or preprocessing conditions. </td>
</tr>
<tr>
<td><strong>3. Event semantics/extension schema</strong></td>
<td>HED, Motion-BIDS</td>
<td><code>trial_type</code> meaning, event tag, additional sensor metadata, and coordinate frame. </td>
<td>Clock alignment and benchmark split are not determined automatically. </td>
</tr>
<tr>
<td><strong>4. Synchronization middleware</strong></td>
<td>LSL</td>
<td>Time alignment of multiple streams, clock offset estimation, and stream metadata. </td>
<td>We do not guarantee the true value of device-side delay or stimulus presentation delay. </td>
</tr>
<tr>
<td><strong>5. Conversion/Reading</strong></td>
<td>MNE-BIDS</td>
<td>BIDSPath, metadata extraction, reading path to MNE, format conversion when necessary. </td>
<td>Comparison indicators and evaluation families are not fixed. </td>
</tr>
<tr>
<td><strong>6. Benchmark harness</strong></td>
<td>MOABB</td>
<td>paradigm, evaluation family, statistical comparison, cross-sectional evaluation of the same pipeline. </td>
<td>We do not guarantee the true value of source imaging or the safety of actual operation. </td>
</tr>
<tr>
<td><strong>7. Learner</strong></td>
<td>Linear classifier, Riemannian pipeline, deep model</td>
<td>Which model was run with which preprocessing, random numbers, and hyperparameters. </td>
<td>If 1-6 above are not fixed, it will not be a fair comparison. </td>
</tr>
</tbody>
</table>

<strong>2026-03 site rule</strong>
<p>
OpenNeuro treats the snapshot as a git tag of the semantic version, and PhysioNet also explicitly cites the version for each project. Therefore, on this site, we include not only the dataset name but also the <strong>snapshot / version / DOI or persistent URL</strong> in the artifact. Additionally, BIDS is a container, HED/Motion-BIDS is semantics and additional metadata, LSL is synchronization, MNE-BIDS is an input/output path, and MOABB is a comparison rule. Please don't mix these up and read that ``Since I used BIDS, I was able to get past the benchmark'' or ``Since I installed LSL, I was able to solve the hardware delay.''
</p>

<h2>Looking at the example of EEG</h2>
<table>
<thead>
<tr>
<th>stage</th>
<th>What to do there</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Align to standards</strong></td>
<td>Align EEG files, events.tsv, channels.tsv, and metadata to BIDS format. </td>
</tr>
<tr>
<td><strong>2. Add event semantics</strong></td>
Specify <td><code>trial_type</code>, condition description, HED tags, manual scoring rule, and report usage flag. </td>
</tr>
<tr>
<td><strong>3. Audit synchronization</strong></td>
<td>How to measure clock domain, LSL / TTL / photodiode, delay / jitter / drift will be left. </td>
</tr>
<tr>
<td><strong>4. Check with Validator</strong></td>
<td>Mechanically identifies violations of standards and missing items. </td>
</tr>
<tr>
<td><strong>5. Publish to storage</strong></td>
<td>Put it on a shared platform like OpenNeuro or PhysioNet so it can be retrieved by third parties. </td>
</tr>
<tr>
<td><strong>6. Compare with benchmarks</strong></td>
<td>Compare models with the same train/test split, the same metrics, and the same baseline. </td>
</tr>
</tbody>
</table>

<strong>This is important</strong>
<p>
Just by aligning to the standard, there is still no "rule for comparison." On the other hand, even if there is a benchmark, if the input shapes are different, the comparison will be broken. Both are required.
</p>

<h2>What is missing?</h2>
<table>
<thead>
<tr>
<th>What is missing</th>
<th>Problems that are likely to occur</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Standards</strong></td>
<td>The file name and metadata are different for each person, and it stops at the entrance to the supplementary exam. </td>
</tr>
<tr>
<td><strong>Storage place</strong></td>
<td>Even if you know about its existence, you will not be able to obtain it or reuse it, and the circle of comparison will not expand. </td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>Notice of violation of standards is delayed, and accidents occur immediately before sharing or during reanalysis. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Each person evaluates using different divisions and indicators, and the meaning of "winning" fluctuates. </td>
</tr>
</tbody>
</table>

<h2>Why raw files alone are not enough</h2>
<p>
Just having a waveform file is not enough for standards or benchmarks. At the very least, without event definitions, stimulus logs, synchronization information, QC logs, and reasons for exclusion, it will be difficult to repeat the same challenge.
</p>

<strong>Safe reading</strong>
<p>
Being "publicly available" and being "comparable" are two different things. Publication is the first step, comparability is the next step in design.
</p>

<h2>Common confusion</h2>
<table>
<thead>
<tr>
<th>Things I tend to say</th>
<th>More accurate paraphrase</th>
</tr>
</thead>
<tbody>
<tr>
<td>“Since we chose BIDS, there is a benchmark”</td>
<td>BIDS is an input format standard, not a comparison rule itself. </td>
</tr>
<tr>
<td>“It was standardized because it was placed in OpenNeuro”</td>
<td>Even if it is posted in the storage area, the standards and metadata are not necessarily sufficient. </td>
</tr>
<tr>
<td>"We used the same input because the dataset name is the same"</td>
<td>Unless you fix OpenNeuro snapshot or PhysioNet version, it cannot be said that it is the same input. </td>
</tr>
<tr>
<td>"Validator passed, so it's enough for research"</td>
<td>Validator is a formal check and does not guarantee the validity of the research or the strength of the benchmark. </td>
</tr>
<tr>
<td>"It became a benchmark because I could read it with MNE-BIDS"</td>
<td>MNE-BIDS is a reading/conversion aid; fixing evaluation families and comparison statistics is a separate task. </td>
</tr>
<tr>
<td>“Event semantics are fixed because there is `events.tsv`”</td>
<td><code>events.tsv</code> is a container for time and columns, and condition meanings and scorer rules must be fixed separately in <code>events.json</code>, HED, and auxiliary logs. </td>
</tr>
<tr>
<td>"Using LSL even solved the hardware delay"</td>
<td>LSL helps with stream synchronization, but device-side delay for display/audio/amplifier requires separate measurement. </td>
</tr>
<tr>
<td>“MOABB scores can be directly compared across tasks”</td>
<td>Within-session, cross-session, and cross-subject are different evaluation families and cannot be treated equally. </td>
</tr>
<tr>
<td>"It's safe to convert preprocessed files back to raw BIDS"</td>
<td>BIDS and MNE-BIDS basically assume unprocessed or minimally processed data, and it is safer to treat modified data as derivatives by specifying the lineage. </td>
</tr>
<tr>
<td>"We won the benchmark, so it's good enough for actual operation"</td>
<td>Benchmark is a yardstick for comparison and does not automatically guarantee actual operation or the establishment of L4/L5. </td>
</tr>
</tbody>
</table>

<h2>Minimum 4 IDs that you want to fix</h2>
<table>
<thead>
<tr>
<th>ID</th>
<th>What I want at least</th>
<th>What happens when it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Input ID</strong></td>
<td>OpenNeuro snapshot tag, PhysioNet version, DOI, acquisition date. </td>
<td>If you mix different versions with the same dataset name, you will not be able to try again. </td>
</tr>
<tr>
<td><strong>Schema ID</strong></td>
<td>The version of BIDS/EEG-BIDS, the version of Validator, and the reason for the warning left. </td>
<td>It is not possible to distinguish between standard differences and implementation differences. </td>
</tr>
<tr>
<td><strong>Evaluation ID</strong></td>
<td>Within-session / cross-session / cross-subject, indicators, split seed, and prohibitions. </td>
<td>The meaning of score will be different and fair comparison will be broken. </td>
</tr>
<tr>
<td><strong>Pipeline ID</strong></td>
<td>MNE-BIDS / MOABB / learning device / environment version, commit, and settings. </td>
<td>Even if you input the same version, you will get different results when you rerun it. </td>
</tr>
</tbody>
</table>

<h2>6 questions when reading strong arguments</h2>
<ol>
<li><strong>What is the input standard?</strong> Check to see if the format is consistent using BIDS, etc. </li>
<li><strong>What version was used:</strong>See if the snapshot, version, DOI, and acquisition date are fixed. </li>
<li><strong>What are the event semantics and clock domain: </strong>Look at <code>trial_type</code>, HED, scorer rule, LSL/TTL/photodiode, delay/jitter audits. </li>
<li><strong>What was used to read/write:</strong>Look at the loader/transformer and see if its version is specified. </li>
<li><strong>What are you comparing?</strong>See if benchmarks, evaluation families, splits, indicators, and prohibitions are fixed. </li>
<li><strong>Did you separate raw and derivative?</strong>See if you can follow the lineage of preprocessed data. </li>
</ol>

<h2>References and official pages</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS Specification: Task events</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS Specification: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021), HED for FAIR event annotation</a></li>
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025), HED library schema for EEG data annotation</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00136" target="_blank">Kothe et al. (2025), Lab Streaming Layer</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024), Motion-BIDS</a></li>
<li><a href="https://docs.openneuro.org/git.html" target="_blank">OpenNeuro Docs: Git access and snapshots</a></li>
<li><a href="https://docs.openneuro.org/user_guide.html" target="_blank">OpenNeuro Docs: Dataset landing page and snapshot metadata</a></li>
<li><a href="https://physionet.org/about/" target="_blank">PhysioNet: About and citation policy</a></li>
<li><a href="https://physionet.org/about/content/" target="_blank">PhysioNet: Resources and citation guidance</a></li>
<li><a href="https://doi.org/10.21105/joss.01896" target="_blank">Appelhoff et al. (2019), MNE-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS Docs: write_raw_bids</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018), MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB Docs</a></li>
<li><a href="https://moabb.neurotechx.com/docs/auto_examples/paradigm_examples/index.html" target="_blank">MOABB Docs: paradigm and evaluation examples</a></li>
</ul>

<h2>Where to go back next</h2>
<p>
Please use <a href="https://mind-upload.com/datasets.html">Data & Bench</a> to return to the practical entry point, <a href="https://mind-upload.com/verification.html">Verification Platform</a> to return to overall design, and <a href="https://mind-upload.com/verification.html#casework">Casework</a> to return to examples from other fields.
</p>
