---
layout: default
title: "Wiki: EEG foundation models and pretraining"
description: "This page organizes how to read EEG foundation / self-supervised models using primary sources, the site's Pretraining Card workflow, and shortcut-resistance checks."
article_type: Wiki
subtitle: "Read advances in representation learning separately from claims that still need to be stopped"
author: Mind Uploading Research Project
last_updated: "2026-03-28"
note: "Technical / natural science only"
audience: "Readers who want to assess EEG foundation models such as LaBraM, BIOT, EEGPT, and BENDR without overclaiming"
reading_time: "10-15 min"
page_intro: "This page is a learning wiki that organizes how to read EEG foundation / self-supervised models. Recent large-scale pretraining is clearly an advance, but to avoid jumping from that advance to claims such as 'generalization is solved' or 'we are one step closer to WBE,' we separate pretraining corpus, channel mismatch, adaptation regime, benchmark object / supervision unit, and evaluation family."
accuracy_note: "This page covers only how to read the technical and natural-science evidence. It does not address overall WBE completion criteria or philosophical questions."
page_highlights:
  - "Foundation models can improve EEG decoding, but they do not solve observability, identifiability, and deployability all at once."
  - "Recent primary papers themselves treat electrode mismatch, sampling-rate differences, missing channels, low SNR, and inter-subject variability as major open problems."
  - "Accepted papers, official challenge rules, and arXiv preprints / under-review manuscripts are not treated as the same evidence tier."
  - "Challenge and benchmark papers from 2025-2026 show that standardized cross-task / cross-subject evaluation is itself still unfinished."
  - "Foundation-model benchmarks are not one object: window / trial classification, event detection, sequence labeling, subject-level regression, and retrieval-style tasks still need separate benchmark-object disclosure."
  - "The official EEG Challenge leaderboard later disclosed a split-construction error in Challenge 2, so benchmark provenance here includes sample randomization, hidden grouping, and inference-stage constraints rather than only benchmark name."
  - "A setup-agnostic foundation model or a very large pretraining corpus is not yet shortcut-resistant transfer; subject / site / reference / protocol shortcuts still need an explicit specificity audit."
  - "Larger models do not automatically win; rankings move with parameter efficiency, training time, and benchmark design."
  - "To preserve comparability, a standard model card is not enough; a Pretraining Card is also required."
  - "A pretraining corpus is also a dataset, so results without an overlap audit cannot be read safely."
known_points:
  - "Self-supervised / foundation models show promising gains under limited-label conditions and across mixed-task downstream settings."
  - "EEG has severe format heterogeneity, and differences in channel count, reference, sample rate, and window length easily break comparison."
  - "The meaning of a downstream score changes across frozen, linear-probe, and fine-tuning regimes."
  - "Papers from 2025-2026 are beginning to show that model rankings can change even with benchmark split construction and preprocessing alone."
  - "Recent 2025-2026 model and benchmark papers show that 'works with any setup', 'wins under linear probing', and 'transfers under fine-tuning' are different claims that can reverse across evaluation regimes."
  - "Benchmark name alone is still too coarse; the supervision unit can shift from windows or trials to epochs, events, or subjects, which changes what transfer means."
  - "Official challenge operations can themselves expose hidden subject-order shortcuts or score-definition changes, so benchmark postmortems are treated here as primary evidence about comparability rather than as afterthoughts."
  - "A successful foundation model cannot be read directly as source identifiability or WBE state-completeness."
unknown_points:
  - "It is still unsettled which pretraining objective is the most stable across broad downstream families."
  - "There is still no default path that simultaneously satisfies cross-day, cross-device, cross-task, and longitudinal deployability."
  - "There is also no fixed common standard for auditing benchmark version, split rules, and checkpoint selection together."
  - "There is still no fixed common standard for reporting benchmark object / supervision unit alongside benchmark provenance."
  - "It is not yet a settled law when targeted diversity beats indiscriminate scale."
  - "It also remains unresolved how to show that a pretrained EEG representation is resisting identity / setup shortcuts rather than merely tolerating them on one benchmark."
wiki_links:
  - label: "Wiki: Baselines, preregistration, and model cards"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Use this page to connect the Pretraining Card to the standard model-card workflow."
  - label: "Wiki: Dataset splits and leakage"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "This page explains why an overlap audit is necessary."
  - label: "Wiki: State, trait, and drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Use this page to return to the basics when separating cross-day and longitudinal claims."
recommended_pages:
  - label: "EEG Basics"
    url: "/eeg_101.html"
  - label: "Data and Benchmarks"
    url: "/datasets.html"
  - label: "Verification Stack"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Bottom line in one sentence</h2>
<p>
EEG foundation models are an important advance for <strong>representation learning</strong> and <strong>low-label downstream tasks</strong>. However, that advance is readable only after separating <strong>what data the model was pretrained on</strong>, <strong>how formats were harmonized</strong>, and <strong>how far adaptation went downstream</strong>. A large model name alone does not determine either the strength of generalization or which claims still need to be stopped.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
This page does not cover philosophy or legal institutions. It covers only how to read EEG foundation / self-supervised models from technical and natural-science evidence.
</p>
</div>

<div class="note-box">
<strong>What the 2026-03 literature audit identified as missing</strong>
<p>
The previous site had already strengthened QC, splits, multimodality, and drift, but it was missing <strong>how to read foundation models themselves</strong>. Without that layer, recent large-scale pretraining can still be misread too quickly as "dataset shift is solved," "a general decoder exists," or "we are closer to WBE." This page therefore separates what the primary literature actually advances from what it still leaves unresolved.
</p>
</div>

<div class="note-box">
<strong>Source types fixed in advance as of 2026-03-25</strong>
<p>
The sources on this page mix <strong>peer-reviewed journal / accepted conference papers</strong>, <strong>accepted posters / workshops</strong>, <strong>official challenge websites / rules</strong>, <strong>arXiv preprints</strong>, and <strong>under-review manuscripts</strong>. These are not evidence of the same strength. For example, the official EEG Foundation Challenge site states in its 2025-11-17 update that the <strong>proposal preprint does not reflect changes made during the execution phase and that the current website and starter kit should be used instead</strong>. The final leaderboard then disclosed that Challenge 2 had not randomized samples, which allowed teams to exploit the fact that contiguous trials likely came from the same subjects. Accordingly, this page does not place model-capability comparisons, benchmark-governance warnings, and moving-target competition rules into the same single frontier ranking.
</p>
</div>

<div class="note-box">
<strong>"Adapting to any setup" is not yet shortcut-resistant transfer</strong>
<p>
This was the next weak point on this page. <a href="https://arxiv.org/abs/2510.21585" target="_blank">El Ouahidi et al. (2025)</a> is important because it explicitly targets arbitrary length and electrode arrangement with pretraining on more than <strong>60,000 hours</strong> from <strong>92 datasets</strong>. But that is still not the same as proving that the learned representation stopped reading <strong>subject identity</strong>, <strong>reference / device / protocol structure</strong>, or other recording-distribution cues. <a href="https://arxiv.org/abs/2603.02268" target="_blank">Lahiri et al. (2026)</a> then showed that narrow-source versus diverse-source pretraining can trade places depending on whether the downstream regime is <strong>linear-probe</strong> or <strong>fine-tuning</strong>, while <a href="https://arxiv.org/abs/2601.17883" target="_blank">Liu et al. (2026)</a> showed across <strong>12 open-source foundation models</strong> and <strong>13 datasets</strong> that linear probing is often insufficient, specialist models trained from scratch remain competitive, and larger models do not automatically generalize better. Those benchmark-side warnings line up with the shortcut literature already used elsewhere on this site: <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a>, <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a>, and <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> show why identity confounding, acquisition variability, and time-robust fingerprints must be audited separately from headline transfer. Therefore, on this site, <strong>setup-agnostic pretraining</strong> is not read as <strong>shortcut-resistant neural representation</strong> unless the downstream claim also passes the <a href="../verification.html#specificity-shortcut-card">Specificity &amp; Shortcut Card</a>.
</p>
</div>

<div class="note-box">
<strong>Benchmark object and supervision unit are not one box either</strong>
<p>
This was the next remaining weakness on this page. The official <a href="https://eeg2025.github.io/data/" target="_blank">EEG Challenge data page</a> bundles <strong>six distinct cognitive tasks</strong> and also reports <strong>four psychopathology dimensions</strong> derived from parent-reported CBCL, so even one official benchmark family already mixes <strong>window / trial-level task decoding</strong> with <strong>subject-level factor prediction</strong>. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">Lee et al. (2025)</a> then fine-tuned large brainwave foundation models across <strong>memory tasks</strong> and <strong>sleep stage classification</strong>, while <a href="https://arxiv.org/abs/2508.17742" target="_blank">Xiong et al. (2025)</a> integrated <strong>14 datasets across 10 paradigms</strong>. Those are not one benchmark object, one supervision unit, or one metric family. Therefore, on this site, benchmark name and split rule are still insufficient unless the paper also states whether the downstream object is <strong>window / trial classification</strong>, <strong>event detection</strong>, <strong>sequence labeling</strong>, <strong>subject-level regression / diagnosis</strong>, or another family, together with what counts as one independent prediction.
</p>
</div>

<section class="section" id="paper-boundaries">
<h2 class="section-title">Read primary sources by evidence tier</h2>
<p>
The biggest weakness that needed correction here was that <strong>accepted model papers</strong>, <strong>official challenge documentation</strong>, <strong>benchmark-warning preprints</strong>, and <strong>under-review manuscripts</strong> were too easy to read as equally strong "latest research." Technically, that matters because accepted model papers support <strong>advances in representation learning / transfer under specific settings</strong>, official rules support <strong>the exposure conditions of the benchmark</strong>, and benchmark-audit preprints support <strong>warnings about instability in comparison</strong>. A table that hides source type therefore becomes a source of misreading by itself.
</p>
<table class="data-table">
<thead>
<tr>
<th>Example</th>
<th>Source type / as of 2026-03-25</th>
<th>What can be said relatively strongly</th>
<th>What barrier the paper itself leaves unresolved</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Kostas et al. (2021)</strong><br>BENDR</td>
<td>Peer-reviewed journal paper</td>
<td>It showed that self-supervised pretraining can provide breadth across novel subjects, hardware, and tasks.</td>
<td>Downstream applicability remained unsettled; pretraining alone did not guarantee universal transfer.</td>
</tr>
<tr>
<td><strong>Wang et al. (2023)</strong><br>BIOT</td>
<td>Accepted conference paper</td>
<td>It provided a concrete strategy for bringing heterogeneous biosignals with different sampling rates, channels, recording durations, and missing values into cross-dataset learning.</td>
<td>Conversely, any result that does not report format harmonization is not meaningfully comparable.</td>
</tr>
<tr>
<td><strong>Jiang et al. (2024)</strong><br>LaBraM</td>
<td>Accepted conference paper</td>
<td>It performed cross-dataset pretraining on about 20 datasets and roughly 2,500 hours of EEG, and showed strong performance across multiple downstream tasks.</td>
<td>It explicitly leaves electrode mismatch, unequal length, varied task design, and low SNR as central EEG-side challenges.</td>
</tr>
<tr>
<td><strong>Wang et al. (2024)</strong><br>EEGPT</td>
<td>Accepted conference presentation</td>
<td>It reported strong downstream performance with a pretrained transformer and linear probing under low SNR, inter-subject variability, and channel mismatch.</td>
<td>A high score there does not automatically imply cross-day deployability or source identifiability.</td>
</tr>
<tr>
<td><strong>Lee et al. (2025)</strong><br>ICML fine-tuning audit</td>
<td>Accepted conference poster</td>
<td>It showed that current large brainwave foundation models only slightly outperform conventional deep baselines, while PEFT methods such as LoRA can greatly reduce the number of trainable parameters.</td>
<td>The gain is small, around 0.5% even at the abstract level, so the result does not support the claim that "larger models win by default."</td>
</tr>
<tr>
<td><strong>EEG Foundation Challenge (2025)</strong><br>NeurIPS competition</td>
<td>Official competition website / rules</td>
<td>It attempts to standardize measurement of cross-task transfer and subject-invariant representation over more than 3,000 HBN-EEG participants.</td>
<td>What it provides directly is current benchmark governance, not a final verdict on model capability. The official site also states that the proposal preprint is outdated, so operational conditions should be read from the current rules and starter kit.</td>
</tr>
<tr>
<td><strong>EEG Foundation Challenge final leaderboard (2025)</strong><br>Governance postmortem</td>
<td>Official leaderboard / postmortem</td>
<td>It shows that benchmark operations themselves can expose hidden subject-order shortcuts: the organizers reported that Challenge 2 samples had not been randomized, so contiguous trials could reveal same-subject structure and the final prize logic had to be changed.</td>
<td>This is strong evidence about benchmark fragility, not a stable capability ranking of the submitted models. It tells us the measurement changed, not which architecture is universally best.</td>
</tr>
<tr>
<td><strong>Xiong et al. (2025)</strong><br>EEG-FM-Bench</td>
<td>arXiv benchmark preprint</td>
<td>It states explicitly that the rapid proliferation of foundation models has outpaced standardized evaluation and that fragmented comparison is slowing scientific progress.</td>
<td>Unharmonized comparisons do create scientific inefficiency, but this is safest to read as a benchmark warning rather than as a final frontier ranking.</td>
</tr>
<tr>
<td><strong>El Ouahidi et al. (2025)</strong><br>REVE</td>
<td>Accepted poster / arXiv manuscript</td>
<td>It introduced a 4D positional encoding that can handle arbitrary length and electrode arrangement, pointing toward better transfer across diverse setups.</td>
<td>What can be read relatively strongly here is a direction for handling heterogeneity, not a stable universal ranking across accepted benchmarks.</td>
</tr>
<tr>
<td><strong>Han et al. (2025)</strong><br>DIVER-1</td>
<td>Under-review / arXiv manuscript</td>
<td>It presented a largest-scale corpus and a systematic scaling-law analysis, arguing that electrophysiology raises a data-constrained scaling question.</td>
<td>The warning that smaller models trained longer can outperform larger models trained briefly under fixed data / compute is important, but an under-review source alone is not enough to fix the field's default scaling-law interpretation.</td>
</tr>
<tr>
<td><strong>Wang et al. (2025)</strong><br>NeuroTTT</td>
<td>arXiv method preprint</td>
<td>It showed that domain-tuned self-supervision and test-time training can help with pretraining-downstream misalignment and cross-subject shift.</td>
<td>Conversely, the results do not support the assumption that a foundation model alone is sufficient without downstream adaptation. Results that include TTT are also not read here as evidence of deployment simplicity.</td>
</tr>
<tr>
<td><strong>Lahiri et al. (2026)</strong><br>PRISM</td>
<td>arXiv clinical-transfer preprint</td>
<td>It reported that pretraining with targeted diversity can become advantageous under fine-tuning and can improve performance on a clinical mimicker task.</td>
<td>The warning that benchmark inconsistency alone can strongly reverse rankings on the same dataset is important, but it still should not be fixed as a shared conclusion of accepted clinical benchmarks.</td>
</tr>
<tr>
<td><strong>Liu et al. (2026)</strong><br>EEG FM benchmarking</td>
<td>arXiv benchmark / review preprint</td>
<td>It compared 12 open-source foundation models and specialist baselines across 13 EEG datasets, and argued that linear probing is often insufficient, scratch specialists remain competitive, and larger models do not automatically generalize better.</td>
<td>Because it is still a preprint and a benchmark study, it does not by itself prove shortcut resistance, deployment readiness, or a settled ranking across future accepted evaluations.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="nine-gates">
<h2 class="section-title">The 10 gates before reading a foundation model</h2>
<table class="data-table">
<thead>
<tr>
<th>Gate</th>
<th>Why it is needed</th>
<th>Minimum evidence we want</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>G0: source type / maturity</strong></td>
<td>Accepted papers, accepted posters, official rules, arXiv preprints, and under-review manuscripts support claims of different strength.</td>
<td>The source type, whether it is accepted / preprint / under review, and for moving-target rules pages, the last verified date.</td>
</tr>
<tr>
<td><strong>G1: corpus identity / overlap</strong></td>
<td>A pretraining corpus is also a dataset. If closely related data leak into the downstream side, the split no longer means what it appears to mean.</td>
<td>Corpus name, version / snapshot, total hours, and an overlap audit against downstream datasets / subjects / sessions.</td>
</tr>
<tr>
<td><strong>G2: population / setup diversity</strong></td>
<td>The number of datasets or total hours is not enough. If population, device, or electrode layout are biased, pretraining may simply learn recording-distribution artifacts.</td>
<td>The covered population, device types, clinical vs. lab setting, electrode schema, and the distribution of reference systems.</td>
</tr>
<tr>
<td><strong>G3: harmonization</strong></td>
<td>EEG differs greatly in channel count, reference, sample rate, and window length, and performance can move purely because of formatting choices.</td>
<td>Channel map, reference, resampling, token length, and the policy for missing channels / missing segments.</td>
</tr>
<tr>
<td><strong>G4: adaptation regime</strong></td>
<td>Frozen feature extraction, full fine-tuning, and test-time training do not mean the same thing when one asks what actually transferred.</td>
<td>Whether the regime is frozen, linear-probe, PEFT, full fine-tune, or TTT, plus target-data usage, label budget, and recalibration amount.</td>
</tr>
<tr>
<td><strong>G5: benchmark object / supervision unit</strong></td>
<td>Per-window classification, event detection, sequence labeling, subject-level regression, and retrieval / ranking do not test the same scientific object. Official foundation-model benchmarks already mix these families.</td>
<td>The supervision unit, label provenance, output family, metric bundle, and what counts as one independent prediction.</td>
</tr>
<tr>
<td><strong>G6: benchmark provenance</strong></td>
<td>Benchmark papers from 2025-2026 show that rankings can move with split construction, checkpoint selection, segment length, and even hidden sample ordering. The official EEG Challenge postmortem made that point operationally explicit.</td>
<td>Benchmark name, version, split rule, sample-randomization / hidden-grouping policy, checkpoint selection, segment length, normalization, how the external hold-out was built, and any inference-stage compute / training restrictions.</td>
</tr>
<tr>
<td><strong>G7: shortcut-resistance / specificity bridge</strong></td>
<td>A good transfer score can still come from subject identity, site / device / reference structure, or protocol distribution rather than the intended neural variable. Foundation-model headlines do not remove that risk.</td>
<td>A task-matched nuisance audit, including participant / site / device / reference disjointness, metadata-only or identity baselines where applicable, shortcut slices, and the linked <a href="../verification.html#specificity-shortcut-card">Specificity &amp; Shortcut Card</a>.</td>
</tr>
<tr>
<td><strong>G8: scale / efficiency</strong></td>
<td>In EEG, "bigger is stronger" does not always hold. It is easy to misread results unless parameter count, data, compute, and trainable fraction are read together.</td>
<td>Total parameter count, trainable parameter count, pretraining epochs / steps, corpus size, training time, and adapter size.</td>
</tr>
<tr>
<td><strong>G9: claim ceiling</strong></td>
<td>Success for a foundation model is still an advance in macro decoding / representation learning.</td>
<td>An explicit statement of what remains latent, and an explicit stop against source identifiability, direct validation, and WBE state-completeness claims.</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>Official challenge postmortems count as benchmark evidence</strong>
<p>
The EEG Challenge submission page defines an <strong>inference-only code submission</strong> setting, while the final leaderboard discloses that Challenge 2 accidentally preserved same-subject trial contiguity. Those facts are not side notes. They directly change what a reported ranking means, because one result was obtained under a fixed inference budget and another could exploit an unintended grouping cue. On this site, benchmark provenance therefore includes <strong>operational constraints</strong> and <strong>postmortem disclosures</strong>, not only the benchmark title.
</p>
</div>

<section class="section" id="pretraining-card">
<h2 class="section-title">The Pretraining Card required on this site</h2>
<p>
For foundation / self-supervised results, this site requires a <strong>Pretraining Card</strong> in addition to the standard model card. This is not an external publication standard; it is <strong>an operating rule of this site</strong> for keeping heterogeneous-corpus pretraining comparable.
</p>

<table class="data-table">
<thead>
<tr>
<th>Item</th>
<th>Minimum required content</th>
<th>Dangerous misreading if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Corpus</strong></td>
<td>Pretraining corpus name, version, total hours, exclusion criteria, and overlap audit.</td>
<td>You may miss the possibility that what looked like generalization was actually reuse of closely related data.</td>
</tr>
<tr>
<td><strong>Population / Setup</strong></td>
<td>Population, device, electrode layout, reference system, and whether the setting is clinical or lab-based.</td>
<td>You may misread the number of datasets as recording diversity itself.</td>
</tr>
<tr>
<td><strong>Harmonization</strong></td>
<td>Channel schema, reference, sample rate, tokenization, normalization, and missing-value policy.</td>
<td>You may misread preprocessing differences as model-capability differences.</td>
</tr>
<tr>
<td><strong>Objective</strong></td>
<td>The pretraining objective, such as masked, autoregressive, or contrastive.</td>
<td>You cannot compare which inductive bias actually mattered.</td>
</tr>
<tr>
<td><strong>Source Type / Maturity</strong></td>
<td>Whether the source is an accepted journal / conference paper, accepted poster / workshop, official rules page, arXiv preprint, or under-review manuscript, and for a rules page, the last verified date.</td>
<td>You may misread under-review warnings or operational documentation as frontier evidence of the same strength as accepted model papers.</td>
</tr>
<tr>
<td><strong>Adaptation</strong></td>
<td>Frozen / linear-probe / PEFT / full fine-tune / TTT, target-data usage, label budget, and whether recalibration is used.</td>
<td>You may conflate "a general representation transferred well" with "the model was strongly adapted to the target."</td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Benchmark name, version, split rule, checkpoint selection, segment length, and normalization.</td>
<td>You may misread ranking changes caused by benchmark design as differences in the model itself.</td>
</tr>
<tr>
<td><strong>Benchmark Object / Supervision Unit</strong></td>
<td>Whether the downstream object is window / trial classification, event detection, sequence labeling, subject-level regression / diagnosis, retrieval / ranking, or another family, together with label provenance, output family, metric bundle, and the independent prediction unit.</td>
<td>You may collapse heterogeneous wins into one story about portable EEG generalization even though the model solved different objects with different error surfaces.</td>
</tr>
<tr>
<td><strong>Shortcut-resistance / Specificity Bridge</strong></td>
<td>For any downstream decode / biomarker / clinical claim, report participant / site / device / reference disjointness, metadata-only or subject-ID baselines where relevant, nuisance-route checks, shortcut slices, and the linked <a href="../verification.html#specificity-shortcut-card">Specificity &amp; Shortcut Card</a>.</td>
<td>You may misread a representation that mainly preserves identity or recording-distribution cues as if it had become invariant to those shortcuts.</td>
</tr>
<tr>
<td><strong>Scale / Efficiency</strong></td>
<td>Total parameter count, trainable parameter count, pretraining steps / epochs, training time, adapter size, and inference cost.</td>
<td>You may read "the foundation model won because it is large" when the real driver was compute allocation or PEFT.</td>
</tr>
<tr>
<td><strong>Evaluation</strong></td>
<td>Evaluation family, hold-out unit, device hold-out, cross-day evaluation, abstention policy, and failure conditions.</td>
<td>You may mistake a high same-day score for deployability.</td>
</tr>
<tr>
<td><strong>Stopped claim</strong></td>
<td>A one-line statement of what still cannot be claimed.</td>
<td>You may over-extrapolate foundation-model success to source truth or WBE.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Operating rules on this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>We do not hide source type:</strong> accepted papers, official rules, and preprints / under-review manuscripts are not listed as evidence of the same strength.</li>
<li><strong>Foundation-model results are not exempt from split auditing:</strong> independence must be checked including the pretraining corpus.</li>
<li><strong>We do not hide population / setup diversity:</strong> we report not just the number of datasets, but which recording distributions were actually included.</li>
<li><strong>We do not hide format harmonization:</strong> channel / reference / sampling harmonization must always be reported.</li>
<li><strong>We do not hide the amount of adaptation:</strong> linear probing, full fine-tuning, and TTT are not all listed as the same kind of "transfer success."</li>
<li><strong>We do not hide benchmark object:</strong> window classification, event detection, sequence labeling, subject-level regression, and retrieval-like tasks are not compressed into one frontier score.</li>
<li><strong>We do not hide benchmark provenance:</strong> because rankings move with split / checkpoint / preprocessing differences, benchmark specification is part of the result.</li>
<li><strong>We do not treat "any setup" as shortcut-resistant by title alone:</strong> foundation-model transfer claims also need a shortcut-resistance bridge to the <a href="../verification.html#specificity-shortcut-card">Specificity &amp; Shortcut Card</a>.</li>
<li><strong>Current competition rules are checked on the official site:</strong> proposal papers or companion preprints are background material; current rules / submission instructions / starter kits take priority for operations.</li>
<li><strong>We do not hide benchmark postmortems:</strong> if organizers later disclose split flaws, sample-order shortcuts, or scoring changes, that disclosure changes how we read the leaderboard.</li>
<li><strong>Benchmark-warning preprints are not treated as frontier verdicts:</strong> ranking reversals and scaling-law claims remain exploratory until reinforced by accepted papers or independent reruns.</li>
<li><strong>We do not hide scale / efficiency:</strong> we do not write that a foundation model won without reporting parameter count, trainable fraction, and training time.</li>
<li><strong>Even at high scores, the claim ceiling is kept in place:</strong> source identifiability, direct validation, closed-loop deployability, and WBE state-completeness are separate gates.</li>
<li><strong>Results without a Pretraining Card are treated only as qualified decoding evidence:</strong> they are not automatically promoted to L2 or above.</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Kostas, D., Aroca-Ouellette, S., &amp; Rudzicz, F. (2021). BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. <em>Frontiers in Human Neuroscience</em>, 15, 653659. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">doi:10.3389/fnhum.2021.653659</a></li>
<li>Wang, H., Lu, C., Xie, B., et al. (2023). BIOT: Biosignal Transformer for Cross-data Learning in the Wild. <em>NeurIPS 2023</em>. <a href="https://papers.nips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf" target="_blank">paper</a></li>
<li>Jiang, W.-B., Zhao, L., &amp; Lu, B.-L. (2024). Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. <em>ICLR 2024</em>. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">proceedings</a></li>
<li>Wang, G., Liu, W., He, Y., Xu, C., Ma, L., &amp; Li, H. (2024). EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. <em>NeurIPS 2024</em>. <a href="https://neurips.cc/virtual/2024/poster/93793" target="_blank">poster / abstract</a></li>
<li>Lee, N., Barmpas, K., Panagakis, Y., Adamos, D., Laskaris, N., &amp; Zafeiriou, S. (2025). Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. <em>ICML 2025 poster</em>. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">OpenReview</a></li>
<li>EEG Foundation Challenge (2025). From Cross-Task to Cross-Subject EEG Decoding. <em>NeurIPS 2025 competition</em>. <a href="https://eeg2025.github.io/" target="_blank">official website</a></li>
<li>EEG Foundation Challenge (2025). Data. <a href="https://eeg2025.github.io/data/" target="_blank">official data page</a></li>
<li>EEG Foundation Challenge (2025). Rules. <a href="https://eeg2025.github.io/rules/" target="_blank">official rules</a></li>
<li>EEG Foundation Challenge (2025). Submission. <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a></li>
<li>EEG Foundation Challenge (2025). Leaderboard. <a href="https://eeg2025.github.io/leaderboard/" target="_blank">official leaderboard / postmortem</a></li>
<li>Xiong, W., Li, J., Li, J., &amp; Zhu, K. (2025). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <em>arXiv</em>. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>El Ouahidi, Y., Lys, J., Thölke, P., Farrugia, N., Pasdeloup, B., Gripon, V., Jerbi, K., &amp; Lioi, G. (2025). REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. <em>accepted poster / arXiv manuscript</em>. <a href="https://arxiv.org/abs/2510.21585" target="_blank">arXiv:2510.21585</a></li>
<li>Han, D. D., Gwon, Y., Lee, A. L., et al. (2025). DIVER-1: Deep Integration of Vast Electrophysiological Recordings at Scale. <em>under-review / arXiv manuscript</em>. <a href="https://arxiv.org/abs/2512.19097" target="_blank">arXiv:2512.19097</a></li>
<li>Wang, S., Deng, Y., Bao, Z., Zhan, X., &amp; Duan, Y. (2025). NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training. <em>arXiv preprint</em>. <a href="https://arxiv.org/abs/2509.26301" target="_blank">arXiv:2509.26301</a></li>
<li>Lahiri, J. B., Runwal, P., Kulkarni, A., Jain, M., Mishra, A. R., Panwar, S., &amp; Singh, S. (2026). PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. <em>arXiv preprint</em>. <a href="https://arxiv.org/abs/2603.02268" target="_blank">arXiv:2603.02268</a></li>
<li>Liu, D., Chen, Y., Chen, Z., Cui, Z., Wen, Y., An, J., Luo, J., &amp; Wu, D. (2026). EEG Foundation Models: Progresses, Benchmarking, and Open Problems. <em>arXiv preprint</em>. <a href="https://arxiv.org/abs/2601.17883" target="_blank">arXiv:2601.17883</a></li>
<li>Chaibub Neto, E., Pratap, A., Perumal, T. M., et al. (2019). Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <em>npj Digital Medicine</em>, 2, 99. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu, M., Yao, S., Wei, Z., et al. (2020). Cross-dataset variability problem in EEG decoding with deep learning. <em>Frontiers in Human Neuroscience</em>, 14, 103. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Di, Y., An, X., Zhong, W., Liu, S., &amp; Ming, D. (2021). The time-robustness analysis of individual identification based on resting-state EEG. <em>Frontiers in Human Neuroscience</em>, 15, 672946. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="baselines-prereg-and-model-cards.html">Baselines, preregistration, and model cards →</a></li>
<li><a href="dataset-splits-and-leakage.html">Dataset splits and leakage →</a></li>
<li><a href="state-trait-and-drift.html">State, trait, and drift →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public Pages</h4>
<ul>
<li><a href="../eeg_101.html">EEG Basics →</a></li>
<li><a href="../datasets.html">Data and Benchmarks →</a></li>
<li><a href="../verification.html">Verification Stack →</a></li>
</ul>
</div>
</aside>
</main>
