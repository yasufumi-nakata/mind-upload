# Wiki: Straight path from EEG to L0

> Freeze benchmark object, temporal regime, and observation logs before touching the model
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-04-03 / Role: Practical route / temporal-validity sync

## Role Of This Page
This page is a practical route from EEG basics to a reproducible L0 artifact pack. The 2026-03 rebuild fixes one weakness in the old route: choosing a dataset and running a model still sounded too simple because benchmark object, temporal regime, event semantics, and verification gates were not kept separate enough.

## Accuracy Notes
This page does not claim that passing L0 solves identity, WBE, or higher-level state recovery. It is an entry point for reproducible analysis only. The stronger public rules still live on Verification.

## Back To Public Pages
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Verification](https://mind-upload.com/verification.html)

## Related Wiki Pages
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - Return here when the measurement ceiling of EEG itself is still unclear.
- [Wiki: Data partitioning and data leakage](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Use this when split hygiene, benchmark provenance, or acquisition shortcuts become the main issue.
- [Wiki: Basics of event synchronization and observation logs](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Use this when events, semantics, timestamps, and clock domains start to blur together.
- [Wiki: State, trait, and drift](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - Use this when same-session and cross-day claims start to blur together.
- [Wiki: Baseline / Benchmark / Pre-registration / Model Card](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Use this when a dataset name and one score start to sound like the whole benchmark object.

## What Is Currently Known
- L0 is about reproducible input, logs, preprocessing, baselines, and failure disclosure rather than high headline accuracy.
- A starter dataset is not enough by itself; the independent hold-out unit, metric bundle, and benchmark-governance status also change what the score means.
- Observation logs, derivative lineage, and temporal-validity fields are separate artifacts.
- Current literature supports careful separation of subject/session shortcuts, acquisition-distribution shortcuts, clock-domain logs, and cross-day validity.

## What Is Still Unknown
- Which starter route best prepares later L1-L2 work still depends on task family and target variable.
- The field still lacks one universally accepted default card bundle for all EEG benchmarks.
- How much temporal-validity disclosure will become standard across EEG benchmarks remains unsettled.

---

<h2>What this route now fixes first</h2>
<p>
The short path from EEG to L0 still exists, but it now starts with a stricter question: <strong>what exactly will your score mean</strong>? Current primary literature and official standards do not support the shortcut that says "pick a public dataset, run preprocessing, train a model, report accuracy." Before a score matters, this site now fixes <strong>benchmark object</strong>, <strong>temporal regime</strong>, <strong>event semantics and clock domain</strong>, <strong>artifact lineage</strong>, and the <strong>stopped claim</strong>.
</p>

<strong>Why this page needed a 2026-03 rebuild</strong>
<p>
The old route was too permissive. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a>, the current <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">BIDS specification</a>, and <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">Pernet et al. (2020)</a> show why raw identity, derivatives, and reporting provenance must be explicit. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025)</a> and <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> show why event semantics and synchronization still need separate audits. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>, <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017)</a>, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a>, and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> show why subject and acquisition shortcuts can survive loose evaluation. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> show that even within roughly half a day, EEG decoding conditions can shift enough to matter for robustness. The official <a href="https://eeg2025.github.io/" target="_blank">EEG Challenge (2025)</a> pages then show that benchmark governance itself can change what a leaderboard means. Therefore, this page no longer treats "dataset -> preprocessing -> score" as a sufficient beginner route.
</p>

<strong>Scope of this page</strong>
<p>
This page stays on the technical and natural science side. It does not argue about philosophy, law, or identity. It only fixes what must be observable, logged, and audited before an EEG result can count as reproducible L0 work on this site.
</p>

<h2>Six gates from EEG to L0</h2>
<table>
<thead>
<tr>
<th>Order</th>
<th>Page to open</th>
<th>What is fixed here</th>
<th>What must exist before moving on</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a></td>
<td>Fix the measurement ceiling: what EEG directly observes, what remains latent, and what kind of claim it cannot support on its own.</td>
<td>A one-line stopped claim such as "this route aims at reproducible macro-state analysis, not source-complete or WBE-complete recovery."</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a> and <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards">Baseline / Benchmark / Pre-registration / Model Card</a></td>
<td>Choose a <strong>benchmark object</strong>, not just a file bundle: task, target, independent hold-out unit, metric bundle, version, extra-data policy, and benchmark-governance status.</td>
<td>A short benchmark card naming dataset/version, task, target, split unit, main metric bundle, and whether official rules or postmortems changed the benchmark meaning.</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage">Dataset splits and data leakage</a> and <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift">State, trait, and drift</a></td>
<td>Freeze the <strong>temporal regime</strong>: subject, session, and time disjointness; same-session versus cross-day scope; fixed versus recalibrated decoder interval.</td>
<td>A split manifest plus a temporal-validity note stating whether the result is same-session, same-day, cross-day, or longer-horizon, and whether the decoder stays fixed.</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs">Event synchronization and observation logs</a></td>
<td>Freeze the <strong>observation contract</strong>: event times, event semantics, label provenance, clock domain, delay/jitter/drift notes, and report-usage flags.</td>
<td>An observation log that separates time anchor, semantics, and synchronization layer instead of mixing them into one generic metadata note.</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a> and <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack">L0 minimum artifact pack</a></td>
<td>Produce the first reproducible artifact bundle: <strong>raw identity</strong>, <strong>derivative identity</strong>, <strong>run identity</strong>, QC, baseline output, and failure registry.</td>
<td>A rerunnable derivative package with dataset provenance, command or pipeline provenance, environment pin, QC report, baseline output, and at least one named failure mode.</td>
</tr>
<tr>
<td><strong>6</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td>Convert the artifact bundle into a bounded claim: L0 ceiling, observability ceiling, shortcut ceiling, and temporal-validity ceiling.</td>
<td>A submission-ready stopped claim plus the required companion cards if the result starts to imply target specificity or temporal durability.</td>
</tr>
</tbody>
</table>

<h2>Why these gates must stay separate</h2>
<table>
<thead>
<tr>
<th>What older beginner routes tended to compress</th>
<th>What current sources actually support</th>
<th>How this site now reads the route</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>"Dataset choice" as only a file download step</strong></td>
<td><a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">Saito &amp; Rehmsmeier (2015)</a> show why metric choice changes what a binary score means, and the official <a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge (2025) rules</a> plus <a href="https://eeg2025.github.io/leaderboard/" target="_blank">final leaderboard</a> show that governance changes can alter benchmark meaning after launch.</td>
<td>Choosing data now means choosing the benchmark object: task, target, split/randomization rule, metric bundle, version, and governance status.</td>
</tr>
<tr>
<td><strong>"Clean split" as the whole leakage solution</strong></td>
<td><a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>, <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">Melnik et al. (2017)</a>, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a>, and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> show that subject/session and acquisition-distribution structure can remain highly predictive.</td>
<td>The route now fixes both split hygiene and shortcut resistance. A clean split is necessary, but it is not treated as proof that the target neural variable was isolated.</td>
</tr>
<tr>
<td><strong>"Same-session score" as temporal generalization</strong></td>
<td><a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> show that EEG decoding conditions can change materially across a day-night window, and this site's <a href="https://mind-upload.com/verification.html#temporal-validity-card">Temporal Validity Card</a> plus <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift">state-trait-drift rule</a> now separate fixed-decoder interval, <strong>fast labels</strong>, <strong>slow internal-milieu disclosure</strong>, and recalibration burden.</td>
<td>The route now asks the reader to decide same-session, same-day, cross-day, or longer-horizon scope before training, and to log whether the regime changed through movement / arousal alone or through slower circadian / endocrine-metabolic state as well.</td>
</tr>
<tr>
<td><strong>"Events are in BIDS" as if semantics and timing were solved together</strong></td>
<td>The current <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">BIDS specification</a> and <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025)</a> support structured events and machine-readable semantics, while <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> makes clear that synchronization middleware does not by itself measure device-side delay.</td>
<td>This route now separates <strong>time anchor</strong>, <strong>event semantics</strong>, and <strong>clock/synchronization audit</strong> into distinct observation artifacts.</td>
</tr>
<tr>
<td><strong>"Pipeline ran" as if provenance were sufficient</strong></td>
<td><a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">Gorgolewski et al. (2016)</a>, <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a>, <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">Pernet et al. (2020)</a>, and the current <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">BIDS specification</a> separate raw datasets, derivatives, and generated-by provenance.</td>
<td>The route now requires raw identity, derivative identity, and run identity to be visible as different objects before L0 is called complete.</td>
</tr>
</tbody>
</table>

<h2>Minimum artifact bundle before one score matters</h2>
<table>
<thead>
<tr>
<th>Artifact</th>
<th>What it must disclose</th>
<th>What goes wrong if it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Benchmark object</strong></td>
<td>Dataset/version, task, target, independent hold-out unit, metric bundle, extra-data policy, and benchmark-governance status.</td>
<td>A score can be overread as if it applied to a different task, split regime, or official rule set.</td>
</tr>
<tr>
<td><strong>Split manifest</strong></td>
<td>Which subject/session/time units are disjoint, how folds were frozen, and which grouping variables were respected.</td>
<td>The evaluation can drift silently as folds or grouping assumptions change.</td>
</tr>
<tr>
<td><strong>Temporal-validity note</strong></td>
<td>Same-session versus cross-day scope, fixed versus recalibrated decoder, fast state labels, and any relevant slow internal-milieu disclosure.</td>
<td>Same-day success can be silently promoted to longitudinal stability or deployability.</td>
</tr>
<tr>
<td><strong>Observation log</strong></td>
<td>Event times, semantics, scorer or report provenance, clock domain, delay/jitter/drift notes, and bad-segment annotations.</td>
<td>The route cannot distinguish a signal problem from a label or timing problem.</td>
</tr>
<tr>
<td><strong>Derivative lineage</strong></td>
<td>Source dataset, generated-by pipeline, version or commit, environment pin, command provenance, and output locations.</td>
<td>Reanalysis and audit become impossible even if the main score is reproducible once.</td>
</tr>
<tr>
<td><strong>Stopped claim</strong></td>
<td>What the result supports and what it still does not support, in one or two sentences.</td>
<td>L0 can be overread as source localization truth, stable biomarker evidence, or WBE-relevant state capture.</td>
</tr>
</tbody>
</table>

<strong>Operational inference used on this site</strong>
<p>
Not every field above is a single mandatory key in one external standard. The stronger requirement on this site is an <strong>operational inference</strong> from current standards, primary literature, and challenge practice: if a result is to count as comparable L0 progress, the benchmark object, temporal regime, observation contract, and derivative lineage all need their own artifacts rather than one mixed prose paragraph.
</p>

<h2>Five accidents this route now tries to stop early</h2>
<table>
<thead>
<tr>
<th>Common accident</th>
<th>Why it is scientifically weak</th>
<th>Where to return</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Choosing a starter dataset without naming the benchmark object</strong></td>
<td>The data may be fine, but the score will still be uninterpretable if task, metric bundle, and governance status are missing.</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards">Baseline / Benchmark / Pre-registration / Model Card</a></td>
</tr>
<tr>
<td><strong>Using a subject/session split but not naming temporal scope</strong></td>
<td>The result can still be same-session or same-day only, even if the split sounds clean.</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift">State, trait, and drift</a></td>
</tr>
<tr>
<td><strong>Treating `events.tsv` as if it fully solved label meaning</strong></td>
<td>Time anchors, condition semantics, and report-derived labels are different objects and can fail independently.</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs">Event synchronization and observation logs</a></td>
</tr>
<tr>
<td><strong>Treating LSL or trigger lines as hardware ground truth</strong></td>
<td>Network synchronization does not automatically measure display, audio, amplifier, or device-internal delays.</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs">Event synchronization and observation logs</a></td>
</tr>
<tr>
<td><strong>Reporting one score without lineage and failure disclosure</strong></td>
<td>The route becomes impossible to audit, extend, or compare even if the run once looked successful.</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack">L0 minimum artifact pack</a> and <a href="https://mind-upload.com/verification.html">Verification</a></td>
</tr>
</tbody>
</table>

<h2>Where to go next</h2>
<p>
If the measurement ceiling of EEG is still not clear, return to <a href="https://mind-upload.com/eeg_101.html">EEG 101</a>. If the main uncertainty is split hygiene or benchmark provenance, go to <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage">Dataset splits and data leakage</a>. If time anchors, label provenance, or synchronization are the problem, go to <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs">Event synchronization and observation logs</a>. Once the first artifact bundle exists, route it through <a href="https://mind-upload.com/verification.html">Verification</a> and attach the <a href="https://mind-upload.com/verification.html#temporal-validity-card">Temporal Validity Card</a> or <a href="https://mind-upload.com/verification.html#specificity-shortcut-card">Specificity &amp; Shortcut Card</a> whenever the claim starts to reach beyond plain reproducible analysis.
</p>

<h2>References</h2>
<ul>
<li>Gorgolewski KJ, Auer T, Calhoun VD, et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. <em>Sci Data</em>. 2016. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">https://doi.org/10.1038/sdata.2016.44</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Sci Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">https://doi.org/10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nat Neurosci</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">https://doi.org/10.1038/s41593-020-00709-0</a></li>
<li>Brain Imaging Data Structure (stable): dataset_description.json, derived dataset and pipeline description. <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html</a></li>
<li>Hermes D, Bigdely-Shamlo N, Niso G, et al. HED library schema for EEG data annotation. <em>Sci Data</em>. 2025. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">https://doi.org/10.1038/s41597-025-05791-2</a></li>
<li>Kothe C, Grivich M, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. <em>Imaging Neurosci</em>. 2025. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">https://doi.org/10.1162/IMAG.a.136</a></li>
<li>Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <em>npj Digit Med</em>. 2019. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">https://doi.org/10.1038/s41746-019-0178-x</a></li>
<li>Melnik A, Legkov P, Izdebski K, et al. Systems, subjects, sessions: to what extent do these factors influence EEG data? <em>Front Hum Neurosci</em>. 2017. <a href="https://doi.org/10.3389/fnhum.2017.00150" target="_blank">https://doi.org/10.3389/fnhum.2017.00150</a></li>
<li>Xu M, Han J, Wang Y, et al. Cross-dataset variability problem in EEG decoding with deep learning. <em>Front Hum Neurosci</em>. 2020. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">https://doi.org/10.3389/fnhum.2020.00103</a></li>
<li>Di M, Han J, Wang Y, et al. The time-robustness analysis of individual identification based on resting-state EEG. <em>Front Hum Neurosci</em>. 2021. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">https://doi.org/10.3389/fnhum.2021.672946</a></li>
<li>Egger M, Haden B, Bernarding J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Sci Rep</em>. 2024. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">https://doi.org/10.1038/s41598-024-70609-x</a></li>
<li>Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. <em>PLoS One</em>. 2015. <a href="https://doi.org/10.1371/journal.pone.0118432" target="_blank">https://doi.org/10.1371/journal.pone.0118432</a></li>
<li>EEG Challenge (2025) official website. <a href="https://eeg2025.github.io/" target="_blank">https://eeg2025.github.io/</a></li>
<li>EEG Challenge (2025) official rules. <a href="https://eeg2025.github.io/rules/" target="_blank">https://eeg2025.github.io/rules/</a></li>
<li>EEG Challenge (2025) final leaderboard and organizer postmortem. <a href="https://eeg2025.github.io/leaderboard/" target="_blank">https://eeg2025.github.io/leaderboard/</a></li>
</ul>
