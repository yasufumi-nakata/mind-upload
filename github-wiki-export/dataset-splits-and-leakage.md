# Wiki: Data partitioning and data leaks

> Even if the accuracy is high, the evaluation will be corrupted if the classification is lax
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-25 / 位置づけ: Practical guide

## このページの役割
This page is a wiki that explains from the beginning how to divide datasets and why data leaks are dangerous. The 2026-03 re-audit tightened one more point: a clean split is necessary, but it is still not enough if acquisition-distribution shortcuts or benchmark-governance failures remain hidden.

## 正確さの前提
These are operational rules, not one-size-fits-all formulas. The best split still depends on the task and data structure, and official challenge operations can materially change what a benchmark score means.

## 公開ページへ戻る
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Verification base](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: EEG pretreatment and QC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - Compensates for where the preprocessing itself changes the result.
- [Wiki: EEG foundation models and pretraining](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-foundation-models) - Use this page when benchmark rules, extra pretraining, and leaderboard interpretation start to blur together.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - See why leak prevention is 'part of operations'.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to the overall map of the learning page.

## いま分かっていること
- Accuracy can easily be overestimated if the train/test separation is loose.
- Apparent performance tends to improve when fragments from the same subject, same session, and near time are included on both sides.
- In clinical EEG, report text and report-derived labels can also be leakage sources.
- Preprocessing, normalization, and feature selection can also be a source of leaks if they are performed after looking at all the data.
- Even after coarse split hygiene, metadata shortcuts such as site, amplifier, reference, and electrode layout can still dominate the score if disjointness and harmonization are not disclosed.
- Leaderboard and challenge results are not stable objects unless benchmark provenance and later postmortems are carried together with the score.

## まだ分かっていないこと
- Which division is closest to future actual operation depends on the task setting and usage situation.
- A deep understanding and auditing of data structures is required to be able to claim that leaks have been completely eliminated.
- How to standardize report-derived labels from signal-only benchmarks is still in the process of operational design.
- Which benchmark-governance bundle should become the default reusable card for EEG leaderboards is still being refined.

---

<h2>The shortest explanation</h2>
<p>
Data division is the process of ``determining how far you can look before comparing the answers.'' A data leak is when that boundary is inadvertently crossed and information that cannot be used in production is mixed into learning and adjustment.
</p>

<strong>2026-03 re-audit: split hygiene is necessary, not sufficient</strong>
<p>
The older version of this page was good at explaining <strong>subject / session / time split</strong>, but it still left two practical shortcuts too implicit. First, <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>, <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017)</a>, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a>, and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> together show that <strong>identity and acquisition-distribution shortcuts</strong> can remain even when the coarse split sounds respectable. Second, the official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) homepage</a>, <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a>, <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a>, and <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> show that <strong>benchmark governance</strong> itself can move what a score means. Therefore this page now treats split hygiene, acquisition-distribution audit, and benchmark provenance as one operational bundle rather than three unrelated side notes.
</p>

<h2>Why partitioning matters so much</h2>
<p>
On school tests, if you practice the questions while looking at the answers, you will get a higher score. However, that score cannot be said to indicate the ability to solve truly new problems. The same goes for machine learning, if the information seen during learning bleeds into the test side, only the numbers will look good.
</p>

<h2>First, be aware of the unit of division</h2>
<table>
<thead>
<tr>
<th>Unit of division</th>
<th>What kind of scene is it?</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Subject unit</strong></td>
<td>When you want to see if you can generalize to new people. </td>
<td>It's easier than it looks when you have pieces of the same person in both train and test. </td>
</tr>
<tr>
<td><strong>Per session</strong></td>
<td>When you want to see if the same person will be stable on different days. </td>
<td>If you divide only by recording on the same day, you will overlook differences in daily differences and electrode conditions. </td>
</tr>
<tr>
<td><strong>Time unit</strong></td>
<td>When envisioning future predictions or continuous operation. </td>
<td>If you enter windows with similar times on both sides, you may see almost the same fragment. </td>
</tr>
</tbody>
</table>

<h2>4 starter data items, independent units are not the same</h2>

<strong>The last two columns are the operational reasoning for this site</strong>
<p>
<strong>Why leaks</strong> and <strong>Safe classification</strong> in the table below are operational rules drawn by this site based on the official explanation of each dataset and the hierarchical structure shown in primary documents.
</p>

<table>
<thead>
<tr>
<th>Dataset</th>
<th>What should be prioritized as an independent unit</th>
<th>Common misdivision</th>
<th>Why does it leak</th>
<th>How to divide on the safe side</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>subject, run if necessary</td>
<td>Random split of epoch / trial</td>
<td>Signal characteristics and cue structures of the same subject and session span train / test. </td>
<td>First of all, separate the subject unit and the run unit even if the evaluation is within the same subject. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>subject and case chronology</td>
<td>Random division by file</td>
<td><code>chb21</code> is the same subject as <code>chb01</code>, and the gap between files also has a context. </td>
<td>Check for subject correspondence instead of case, and split while preserving sequential order and gap. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>subject-night</td>
<td>Random split of epoch</td>
<td>Sequential hypnograms and subject-specific sleep structures from the same night span train / test. </td>
<td>Keep each night and declare first whether it is generalization across subjects or within-subject. </td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>patient / session</td>
<td>Random division of segment / file, signal-only evaluation with report included</td>
<td>This is because multiple sessions and de-identified reports of the same patient have information close to the label. </td>
<td>Require per patient/session split and <strong>report usage flag</strong>. </td>
</tr>
</tbody>
</table>

<h2>7 common leak patterns</h2>
<table>
<thead>
<tr>
<th>Common accidents</th>
<th>What's happening</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fragments of the same subject enter on both sides</strong></td>
<td>The individual's unique habits are memorized, and the generalization performance to new people appears to be higher. </td>
</tr>
<tr>
<td><strong>Mix adjacent time windows</strong></td>
<td>Separating almost the same waveform slices into train/test, it underestimates the difficulty of predicting the future. </td>
</tr>
<tr>
<td><strong>Normalize and select features on all data</strong></td>
<td>The statistics on the test side are used during training, and the information flows backwards. </td>
</tr>
<tr>
<td><strong>Repeat model selection with test</strong></td>
<td>test essentially takes on the role of validation, and the final score is optimistic. </td>
</tr>
<tr>
<td><strong>Miss duplicate or derived samples</strong></td>
<td>Data originally cut from the same record is included on both sides, resulting in a comparison that is not an independent sample. </td>
</tr>
<tr>
<td><strong>Hide site / device / reference / layout shortcuts</strong></td>
<td>The model learns acquisition-distribution structure such as amplifier, montage, reference system, or electrode layout instead of the target neural variable. </td>
</tr>
<tr>
<td><strong>Treat challenge operations as fixed when they changed</strong></td>
<td>The benchmark name stays the same while randomization, hidden grouping, extra-data policy, inference restrictions, or organizer postmortems change what the ranking actually measures. </td>
</tr>
</tbody>
</table>

<h2>Split hygiene still leaves four shortcut families</h2>
<table>
<thead>
<tr>
<th>Shortcut family</th>
<th>What can masquerade as progress</th>
<th>What to publish instead</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Subject / session fingerprint</strong></td>
<td>A score can look like generalization while it mostly exploits stable subject-specific or session-specific structure. </td>
<td>Disclose the independent hold-out unit, raw-window ancestry, and whether subject/session identifiers were fully disjoint. </td>
</tr>
<tr>
<td><strong>Acquisition-distribution shortcut</strong></td>
<td>A model can ride site, amplifier, cap, sampling rate, filter chain, reference system, or electrode-layout differences instead of the claimed neural variable. </td>
<td>Publish site / device / reference / layout disjointness, the harmonization log, and a metadata-only or setup-only baseline whenever possible. </td>
</tr>
<tr>
<td><strong>Report / metadata shortcut</strong></td>
<td>A signal-only claim can inherit report-derived labels, triage context, or structured metadata that already sits close to the answer. </td>
<td>State whether report text or derived metadata were used, and separate signal-only from multimodal / metadata-assisted scoreboards. </td>
</tr>
<tr>
<td><strong>Benchmark-governance shortcut</strong></td>
<td>A leaderboard can look stable even though hidden grouping, randomization, extra-data policy, checkpoint policy, or inference-stage rules changed what the benchmark measured. </td>
<td>Publish benchmark version, split / randomization rule, hidden grouping, extra-data and pretrained-checkpoint policy, inference-stage restrictions, and later postmortems together with the score. </td>
</tr>
</tbody>
</table>

<strong>Benchmark governance is part of leakage control, not administrative detail</strong>
<p>
The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) homepage</a> explicitly says the original preprint became outdated after execution-phase changes and that the website plus starter kit should be treated as current. The official <a href="https://eeg2025.github.io/rules/" target="_blank">rules</a> require disclosure of additional pretraining datasets, pretrained models and fine-tuning method, code submission during the inference stage, and a <strong>single-GPU 20 GB</strong> inference budget. The official <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a> further fixes the event as an <strong>inference-only code competition</strong>. The final <a href="https://eeg2025.github.io/leaderboard/" target="_blank">leaderboard</a> then disclosed that Challenge 2 samples had not been randomized, allowing contiguous-trial same-subject structure to affect the ranking and forcing separate awards. On this site, that means benchmark governance now belongs on the same checklist as split hygiene rather than in a footnote after the score.
</p>

<strong>Metric semantics are also part of leak-resistant reporting</strong>
<p>
Even after split hygiene and benchmark provenance are disclosed, the reported number can still mislead if the task is rare-event or class-imbalanced. <a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp; Rehmsmeier (2015)</a> showed that precision-recall views are often more informative than ROC summaries under strong imbalance. In seizure tasks, <a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">Roy et al. (2021)</a> and <a href="https://doi.org/10.1097/WNP.0000000000000709" target="_blank">Scheuer et al. (2021)</a> show that event sensitivity, overlap logic, and false alarms per hour or day matter together, while <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">Segal et al. (2023)</a> shows that false-alarm control is itself a design target in seizure prediction. In sleep staging, <a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">Sun et al. (2017)</a> and <a href="https://doi.org/10.7554/eLife.70092" target="_blank">Vallat &amp; Walker (2021)</a> show that pooled performance can still hide minority-stage failure. Therefore, this site now asks for a <strong>task-matched metric bundle</strong> in addition to split hygiene.
</p>

<h2>Leak warning specific to the dataset added this time</h2>
<table>
<thead>
<tr>
<th>dataset</th>
<th>Notes to be fixed this time</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>Since it is a cue-locked motor task, even if the split is made stricter, the visual cue/eyeball/myoelectric contributions will still be audited separately. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>Do not confuse subject numbers with case numbers. Don't shuffle files and pin gap and chronology to runbook. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>Do not silently mix R&K hypnogram as equivalent to AASM. No cross-dataset comparison without writing label mapping. </td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>Do not mix report text, triage and session metadata derived from report keyword into input of signal-only benchmark. </td>
</tr>
</tbody>
</table>

<h2>At least I would like to report this</h2>

<h4>Report Items</h4>
<ul>
<li><strong>Evaluation family:</strong>Whether the result is within-session, cross-session, cross-subject, or temporal / longitudinal. </li>
<li><strong>Split rule:</strong>How many items were placed in train / validation / calibration / test, and what was the independent hold-out unit? </li>
<li><strong>Window ancestry:</strong>Which subject / case / night / session / file / record generated each split, and were near-adjacent windows kept apart? </li>
<li><strong>Metric bundle:</strong>Was the task read through balanced / macro metrics, event sensitivity plus false alarms, or per-stage agreement rather than a single headline number? </li>
<li><strong>Report usage flag:</strong>Was the claim signal-only, or were report text / metadata / multimodal fields also used? </li>
<li><strong>Acquisition-distribution audit:</strong>Were site, device, reference system, channel map, electrode layout, and protocol distribution separated, harmonized, or left mixed? </li>
<li><strong>Preprocessing boundaries:</strong>Were normalization, feature selection, and threshold tuning fit using only the allowed split? </li>
<li><strong>Benchmark provenance:</strong>If this is a challenge or leaderboard result, what were the benchmark version, randomization rule, hidden grouping, extra-data / pretrained-checkpoint policy, inference-stage restrictions, and later postmortems? </li>
<li><strong>Baseline:</strong>What is the improvement compared with a simpler model or a metadata-only / setup-only baseline? </li>
<li><strong>Failure example + stopping claim:</strong>Under what conditions did it fail, what was excluded, and what stronger claim is explicitly not being made? </li>
</ul>

<h2>References</h2>
<ul>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), The Temple University Hospital EEG Data Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), The Temple University Hospital Seizure Detection Corpus</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009), Sleep classification according to AASM and Rechtschaffen &amp; Kales</a></li>
<li><a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019), Detecting the impact of subject characteristics on machine learning-based diagnostic applications</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017), Systems, subjects, sessions: to what extent do these factors influence EEG data?</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020), Cross-dataset variability problem in EEG decoding with deep learning</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021), The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG</a></li>
<li><a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp; Rehmsmeier (2015), The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets</a></li>
<li><a href="https://doi.org/10.1016/j.ebiom.2021.103275" target="_blank">Roy et al. (2021), Evaluation of artificial intelligence systems for assisting neurologists with fast and accurate annotations of scalp electroencephalography data</a></li>
<li><a href="https://doi.org/10.1097/WNP.0000000000000709" target="_blank">Scheuer et al. (2021), Seizure Detection: Interreader Agreement and Detection Algorithm Assessments Using a Large Dataset</a></li>
<li><a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">Segal et al. (2023), Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction</a></li>
<li><a href="https://doi.org/10.1093/sleep/zsx139" target="_blank">Sun et al. (2017), Large-Scale Automated Sleep Staging</a></li>
<li><a href="https://doi.org/10.7554/eLife.70092" target="_blank">Vallat &amp; Walker (2021), An open-source, high-performance tool for automated sleep staging</a></li>
<li><a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025) official homepage</a></li>
<li><a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge (2025) official rules</a></li>
<li><a href="https://eeg2025.github.io/submission/" target="_blank">EEG Challenge (2025) official submission page</a></li>
<li><a href="https://eeg2025.github.io/leaderboard/" target="_blank">EEG Challenge (2025) official leaderboard / organizer postmortem</a></li>
</ul>

<h2>Safety measures if you get lost in the first book</h2>
<p>
When in doubt, it is safe to follow these three points: <strong>Separate train/test for each subject</strong> <strong>Do not touch test until the end</strong><strong>For normalization and feature selection, fit only with train</strong>. Even if it seems too harsh, reliable accuracy is more valuable than fancy numbers.
</p>

<h2>Where to go back next</h2>
<p>
Go back to <a href="https://mind-upload.com/datasets.html">Data & Bench</a> if you want to review the actual starter data, <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a> if you want to go back to creating minimal loops, or go back to <a href="https://mind-upload.com/verification.html">Verification Foundation</a> if you want to see why this is part of the verification foundation.
</p>
