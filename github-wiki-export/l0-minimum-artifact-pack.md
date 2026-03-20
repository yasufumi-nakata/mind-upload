# Wiki: Minimum artifact pack for L0

> Do not call it reproducible until version, observability, evaluation, lineage, and replay are fixed together
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-20 / 位置づけ: Operational guide

## このページの役割
This page is an auxiliary page that fixes what must be bundled together before an L0 result can be called reproducible analysis on this site. It is not a procedure manual; it is a submission-shape check that asks whether a third party can reconstruct not only the score, but also what was actually observed, held out, harmonized, and omitted.

## 正確さの前提
This page defines the current minimum for L0. It does not by itself justify causal or identity claims, but without these fields even L0 comparability remains too weak.

## 公開ページへ戻る
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Verification base](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - You can see from the beginning why artifacts are fixed first.
- [Wiki: Data partitioning and leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Supplements the reason why splitting rules go into artifacts.
- [Wiki: Baseline/Pre-registration/Model Card](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Compensates for the role differences between baseline and failure examples.

## いま分かっていること
- For L0, it is more important than high accuracy that a third party can rerun under the same conditions and still understand what the score is allowed to mean.
- BIDS / EEG-BIDS makes data traceable, but it does not by itself fix event fidelity, label provenance, or leak-free evaluation.
- The same score changes meaning across within-session, cross-session, cross-subject, and adaptation settings.
- Preloaded or modified recordings should be written as derivatives with explicit lineage rather than silently overwriting raw.
- Examples of failures, setup shortcuts, and stopping claims belong in the artifact pack, not only in side notes.

## まだ分かっていないこと
- Which QC metrics, nuisance-only baselines, and harmonization transforms should become defaults still depends on the task and dataset.
- How the L0 pack should expand into standard L1/L2 cards will depend on future benchmark design.
- The best reusable format for acquisition-distribution summaries across multi-site datasets is still evolving.

---

<h2>Think in terms of one pack</h2>
<p>
The L0 artifact is not a single file or a single score. Only when <strong>dataset identity</strong>, <strong>what was actually observed</strong>, <strong>how train/test was separated</strong>, <strong>how derivatives were produced</strong>, and <strong>how to replay the run</strong> are fixed together can a third party track the result honestly.
</p>

<strong>2026-03-20 addendum: the old 8-point pack was too weak</strong>
<p>
This site's practical pages now require more than <strong>version + BIDS + QC + split + baseline</strong>. The reason is simple: EEG-BIDS, MOABB, official dataset pages, and MNE-BIDS docs together make clear that <strong>event fidelity</strong>, <strong>label provenance</strong>, <strong>evaluation family</strong>, <strong>acquisition-distribution summary</strong>, and <strong>derivative lineage</strong> materially change what a later score means. This page is now synchronized with that stricter rule.
</p>

<h2>Minimum 11 items now required in the L0 pack</h2>
<table>
<thead>
<tr>
<th>Deliverables</th>
<th>Minimum desired contents</th>
<th>What is the problem if it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Dataset identity</strong></td>
<td>Snapshot / version / DOI / retrieval date / license / persistent URL.</td>
<td>Even with the same dataset name, different versions or releases get mixed and reproduction breaks.</td>
</tr>
<tr>
<td><strong>2. BIDS / EEG-BIDS skeleton</strong></td>
<td><code>dataset_description.json</code>, <code>README</code>, participant/session/run structure, <code>*_eeg.json</code>, <code>*_channels.tsv</code>, <code>*_electrodes.tsv</code>, and <code>*_coordsystem.json</code> when positions exist.</td>
<td>Third parties cannot reconstruct the same raw input or its measurement condition.</td>
</tr>
<tr>
<td><strong>3. Event Fidelity Card</strong></td>
<td>Onset / duration / sample, clock domain, delay / jitter evidence, event semantics, and any HED or scoring rule used to interpret them.</td>
<td>The result may look aligned to behavior while event meaning and timing remain ambiguous.</td>
</tr>
<tr>
<td><strong>4. Label provenance</strong></td>
<td>Whether the target comes from annotation channels, manual scoring, clinician reports, keyword rules, or another derived source, plus a report-usage flag when relevant.</td>
<td>A signal-only benchmark and a report-assisted benchmark get silently mixed.</td>
</tr>
<tr>
<td><strong>5. Standards confirmation</strong></td>
<td>Validator output together with any remaining warnings and why they are acceptable.</td>
<td>Non-shareable structural violations remain hidden behind a seemingly clean dataset name.</td>
</tr>
<tr>
<td><strong>6. Split family + hold-out ancestry</strong></td>
<td>Within-session / cross-session / cross-subject / adaptation family, the independent hold-out unit, and whether windows from the same raw recording can cross the boundary.</td>
<td>The score becomes uninterpretable because train/test independence is unclear.</td>
</tr>
<tr>
<td><strong>7. Acquisition-distribution summary</strong></td>
<td>Site / device / reference / channel map / electrode layout / protocol distribution, plus the harmonization policy and any metadata-only baseline.</td>
<td>Signal differences and setup differences get collapsed into one accuracy number.</td>
</tr>
<tr>
<td><strong>8. QC / exclusion log</strong></td>
<td>Missingness, bad channels, bad segments, artifacts, exclusions, and thresholds in numerical form.</td>
<td>No one can tell which recordings were removed or why.</td>
</tr>
<tr>
<td><strong>9. Baseline + shortcut checks</strong></td>
<td>At least one simple baseline, plus any nuisance-only or metadata-only comparison needed to keep shortcut routes visible.</td>
<td>Apparent improvement may come from identity, setup, or label shortcuts rather than the intended signal.</td>
</tr>
<tr>
<td><strong>10. Derivative lineage + replay steps</strong></td>
<td>Commands, environment, random seeds, preprocessing boundaries, and explicit raw-to-derivative lineage.</td>
<td>Preprocessed data can be mistaken for raw, and other people cannot rerun the same flow.</td>
</tr>
<tr>
<td><strong>11. Failure examples + stopping claim</strong></td>
<td>Known failure modes, exclusions, pending conditions, and the strongest claim the result is still allowed to stop at.</td>
<td>Only successes remain and later readers overread L0 as if it already implied stronger evidence.</td>
</tr>
</tbody>
</table>

<h2>Why the old 8-point pack is now too weak</h2>
<table>
<thead>
<tr>
<th>Weak point</th>
<th>Why it fails now</th>
<th>What the pack must add</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDS shape without annotation depth</strong></td>
<td>BIDS and EEG-BIDS make the dataset traceable, but they do not by themselves tell you whether an outcome came from cue markers, manual stage scoring, clinician reports, or a derived rule.</td>
<td>Add <strong>Event Fidelity Card</strong> plus <strong>label provenance</strong> to the pack itself.</td>
</tr>
<tr>
<td><strong>Split rule without evaluation family</strong></td>
<td>Within-session, cross-session, cross-subject, and adaptation all answer different questions, and the same accuracy number does not transfer across them.</td>
<td>Add <strong>evaluation family</strong>, <strong>independent hold-out unit</strong>, and <strong>window ancestry</strong>.</td>
</tr>
<tr>
<td><strong>Replay steps without lineage or setup summary</strong></td>
<td>Preloaded / modified data can silently become derivatives, and setup differences such as site, device, reference, and electrode layout can still dominate the result.</td>
<td>Add <strong>acquisition-distribution summary</strong>, <strong>harmonization log</strong>, and <strong>derivative lineage</strong>.</td>
</tr>
</tbody>
</table>

<h2>Five bundles to keep together</h2>

<h4>Bundles</h4>
<ul>
<li><strong>Identity:</strong> freeze snapshot, version, DOI, retrieval date, and license.</li>
<li><strong>Observability:</strong> fix BIDS / EEG-BIDS shape, event fidelity, and label provenance.</li>
<li><strong>Evaluation:</strong> fix evaluation family, hold-out ancestry, setup distribution, harmonization, and baselines.</li>
<li><strong>Lineage:</strong> keep raw-to-derivative boundaries explicit instead of silently rewriting modified data as raw.</li>
<li><strong>Replay:</strong> keep commands, environment, failures, and the stopping claim together.</li>
</ul>

<h2>Common omissions</h2>
<table>
<thead>
<tr>
<th>Common conditions</th>
<th>What is still missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>dataset name exists</strong></td>
<td>Snapshot, version, DOI, retrieval date, and license may not remain.</td>
</tr>
<tr>
<td><strong>Waveform file is available</strong></td>
<td>Events, synchronization, label provenance, event semantics, and bad segments may still be missing.</td>
</tr>
<tr>
<td><strong>Accuracy is there</strong></td>
<td>Evaluation family, independent hold-out unit, leak check, harmonization log, or baseline may still be absent.</td>
</tr>
<tr>
<td><strong>There is a code</strong></td>
<td>Environment, random numbers, derivative lineage, execution order, and known failure conditions may not be written.</td>
</tr>
<tr>
<td><strong>I thought I did QC</strong></td>
<td>Numeric logs, exclusion reasons, and the stopping claim may not remain.</td>
</tr>
</tbody>
</table>

<h2>A stricter L0 completion check</h2>
<table>
<thead>
<tr>
<th>Question</th>
<th>If yes, move forward</th>
<th>If no, what to do next</th>
</tr>
</thead>
<tbody>
<tr>
<td>Can other people recover the same input identity?</td>
<td>Snapshot / version / DOI / retrieval date / license and BIDS skeleton are complete.</td>
<td>Freeze the dataset identity and the BIDS skeleton first.</td>
</tr>
<tr>
<td>Can they tell what was actually annotated and by whom?</td>
<td>Event fidelity and label provenance are written, including any report-usage flag.</td>
<td>Fix events, annotation rules, and label provenance before trusting the score.</td>
</tr>
<tr>
<td>Can they explain what the score means?</td>
<td>Evaluation family, hold-out ancestry, setup summary, harmonization policy, and baselines are fixed.</td>
<td>Fix train/test logic, metadata shortcuts, and baselines first.</td>
</tr>
<tr>
<td>Can someone else replay the same derivatives?</td>
<td>Command, environment, preprocessing boundaries, and raw-to-derivative lineage remain.</td>
<td>Create a short runbook and make derivative lineage explicit.</td>
</tr>
<tr>
<td>Can the claim stop at the right ceiling?</td>
<td>Failure examples and the stopping claim are written next to the result.</td>
<td>State explicitly what the current pack does <strong>not</strong> justify.</td>
</tr>
</tbody>
</table>

<strong>What this page still does not do</strong>
<p>
Here we do not decide which model is strongest or which metric is ultimately best. The first objective of L0 is still to create a comparable starting point. The change on this page is only that the starting point is now defined more strictly.
</p>

<h2>References</h2>
<ul>
<li><a href="https://bids.neuroimaging.io/getting_started/tutorials/annotation.html" target="_blank">BIDS Website: Annotating a BIDS dataset</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS Specification 1.11.1: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS Docs: write_raw_bids</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018), MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/generated/moabb.evaluations.WithinSessionEvaluation.html" target="_blank">MOABB Docs: WithinSessionEvaluation</a></li>
<li><a href="https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSessionEvaluation.html" target="_blank">MOABB Docs: CrossSessionEvaluation</a></li>
<li><a href="https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSubjectEvaluation.html" target="_blank">MOABB Docs: CrossSubjectEvaluation</a></li>
<li><a href="https://doi.org/10.1038/s41597-022-01647-1" target="_blank">Ma et al. (2022), A large EEG dataset for studying cross-session variability in motor imagery BCI</a></li>
<li><a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019), identity confounding in machine learning-based disease diagnosis</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017), Systems, subjects, sessions</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020), Cross-dataset deep learning for EEG</a></li>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), TUH EEG Corpus</a></li>
</ul>

<h2>Where to return next</h2>
<p>
Return to <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-On</a> if you want to follow the actual steps, <a href="https://mind-upload.com/datasets.html">Data & Bench</a> if you want to reselect the input data, or return to <a href="https://mind-upload.com/verification.html">Verification Infrastructure</a> if you want to see how this product stacks up as a public good.
</p>
