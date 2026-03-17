# Wiki: EEG foundation models and pretraining

> Read advances in representation learning separately from claims that still need to be stopped
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-17 / 位置づけ: Technical / natural science only

## このページの役割
This page is a learning wiki that organizes how to read EEG foundation / self-supervised models. Recent large-scale pretraining is clearly an advance, but to avoid jumping from that advance to claims such as 'generalization is solved' or 'we are one step closer to WBE,' we separate pretraining corpus, channel mismatch, adaptation regime, and evaluation family.

## 正確さの前提
This page covers only how to read the technical and natural-science evidence. It does not address overall WBE completion criteria or philosophical questions.

## 公開ページへ戻る
- [EEG Basics](https://mind-upload.com/eeg_101.html)
- [Data and Benchmarks](https://mind-upload.com/datasets.html)
- [Verification Stack](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: Baselines, preregistration, and model cards](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Use this page to connect the Pretraining Card to the standard model-card workflow.
- [Wiki: Dataset splits and leakage](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - This page explains why an overlap audit is necessary.
- [Wiki: State, trait, and drift](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - Use this page to return to the basics when separating cross-day and longitudinal claims.

## いま分かっていること
- Self-supervised / foundation models show promising gains under limited-label conditions and across mixed-task downstream settings.
- EEG has severe format heterogeneity, and differences in channel count, reference, sample rate, and window length easily break comparison.
- The meaning of a downstream score changes across frozen, linear-probe, and fine-tuning regimes.
- Papers from 2025-2026 are beginning to show that model rankings can change even with benchmark split construction and preprocessing alone.
- A successful foundation model cannot be read directly as source identifiability or WBE state-completeness.

## まだ分かっていないこと
- It is still unsettled which pretraining objective is the most stable across broad downstream families.
- There is still no default path that simultaneously satisfies cross-day, cross-device, cross-task, and longitudinal deployability.
- There is also no fixed common standard for auditing benchmark version, split rules, and checkpoint selection together.
- It is not yet a settled law when targeted diversity beats indiscriminate scale.

---

<h2>Bottom line in one sentence</h2>
<p>
EEG foundation models are an important advance for <strong>representation learning</strong> and <strong>low-label downstream tasks</strong>. However, that advance is readable only after separating <strong>what data the model was pretrained on</strong>, <strong>how formats were harmonized</strong>, and <strong>how far adaptation went downstream</strong>. A large model name alone does not determine either the strength of generalization or which claims still need to be stopped.
</p>

<strong>Scope of this page</strong>
<p>
This page does not cover philosophy or legal institutions. It covers only how to read EEG foundation / self-supervised models from technical and natural-science evidence.
</p>

<strong>What the 2026-03 literature audit identified as missing</strong>
<p>
The previous site had already strengthened QC, splits, multimodality, and drift, but it was missing <strong>how to read foundation models themselves</strong>. Without that layer, recent large-scale pretraining can still be misread too quickly as "dataset shift is solved," "a general decoder exists," or "we are closer to WBE." This page therefore separates what the primary literature actually advances from what it still leaves unresolved.
</p>

<strong>Source types fixed in advance as of 2026-03-17</strong>
<p>
The sources on this page mix <strong>peer-reviewed journal / accepted conference papers</strong>, <strong>accepted posters / workshops</strong>, <strong>official challenge websites / rules</strong>, <strong>arXiv preprints</strong>, and <strong>under-review manuscripts</strong>. These are not evidence of the same strength. For example, the official EEG Foundation Challenge site states in its 2025-11-17 update that the <strong>proposal preprint does not reflect changes made during the execution phase and that the current website and starter kit should be used instead</strong>. Accordingly, this page does not place model-capability comparisons, benchmark-governance warnings, and moving-target competition rules into the same single frontier ranking.
</p>

<h2>Read primary sources by evidence tier</h2>
<p>
The biggest weakness that needed correction here was that <strong>accepted model papers</strong>, <strong>official challenge documentation</strong>, <strong>benchmark-warning preprints</strong>, and <strong>under-review manuscripts</strong> were too easy to read as equally strong "latest research." Technically, that matters because accepted model papers support <strong>advances in representation learning / transfer under specific settings</strong>, official rules support <strong>the exposure conditions of the benchmark</strong>, and benchmark-audit preprints support <strong>warnings about instability in comparison</strong>. A table that hides source type therefore becomes a source of misreading by itself.
</p>
<table>
<thead>
<tr>
<th>Example</th>
<th>Source type / as of 2026-03-17</th>
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
</tbody>
</table>

<h2>The 8 gates before reading a foundation model</h2>
<table>
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
<td><strong>G5: benchmark provenance</strong></td>
<td>Benchmark papers from 2025-2026 show that rankings can move with split construction, checkpoint selection, and segment length alone.</td>
<td>Benchmark name, version, split rule, checkpoint selection, segment length, normalization, and how the external hold-out was built.</td>
</tr>
<tr>
<td><strong>G6: scale / efficiency</strong></td>
<td>In EEG, "bigger is stronger" does not always hold. It is easy to misread results unless parameter count, data, compute, and trainable fraction are read together.</td>
<td>Total parameter count, trainable parameter count, pretraining epochs / steps, corpus size, training time, and adapter size.</td>
</tr>
<tr>
<td><strong>G7: claim ceiling</strong></td>
<td>Success for a foundation model is still an advance in macro decoding / representation learning.</td>
<td>An explicit statement of what remains latent, and an explicit stop against source identifiability, direct validation, and WBE state-completeness claims.</td>
</tr>
</tbody>
</table>

<h2>The Pretraining Card required on this site</h2>
<p>
For foundation / self-supervised results, this site requires a <strong>Pretraining Card</strong> in addition to the standard model card. This is not an external publication standard; it is <strong>an operating rule of this site</strong> for keeping heterogeneous-corpus pretraining comparable.
</p>

<table>
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

<h2>Operating rules on this site</h2>

<h4>Rule</h4>
<ul>
<li><strong>We do not hide source type:</strong> accepted papers, official rules, and preprints / under-review manuscripts are not listed as evidence of the same strength.</li>
<li><strong>Foundation-model results are not exempt from split auditing:</strong> independence must be checked including the pretraining corpus.</li>
<li><strong>We do not hide population / setup diversity:</strong> we report not just the number of datasets, but which recording distributions were actually included.</li>
<li><strong>We do not hide format harmonization:</strong> channel / reference / sampling harmonization must always be reported.</li>
<li><strong>We do not hide the amount of adaptation:</strong> linear probing, full fine-tuning, and TTT are not all listed as the same kind of "transfer success."</li>
<li><strong>We do not hide benchmark provenance:</strong> because rankings move with split / checkpoint / preprocessing differences, benchmark specification is part of the result.</li>
<li><strong>Current competition rules are checked on the official site:</strong> proposal papers or companion preprints are background material; current rules / submission instructions / starter kits take priority for operations.</li>
<li><strong>Benchmark-warning preprints are not treated as frontier verdicts:</strong> ranking reversals and scaling-law claims remain exploratory until reinforced by accepted papers or independent reruns.</li>
<li><strong>We do not hide scale / efficiency:</strong> we do not write that a foundation model won without reporting parameter count, trainable fraction, and training time.</li>
<li><strong>Even at high scores, the claim ceiling is kept in place:</strong> source identifiability, direct validation, closed-loop deployability, and WBE state-completeness are separate gates.</li>
<li><strong>Results without a Pretraining Card are treated only as qualified decoding evidence:</strong> they are not automatically promoted to L2 or above.</li>
</ul>

<h2>References</h2>
<ol>
<li>Kostas, D., Aroca-Ouellette, S., &amp; Rudzicz, F. (2021). BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. <em>Frontiers in Human Neuroscience</em>, 15, 653659. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">doi:10.3389/fnhum.2021.653659</a></li>
<li>Wang, H., Lu, C., Xie, B., et al. (2023). BIOT: Biosignal Transformer for Cross-data Learning in the Wild. <em>NeurIPS 2023</em>. <a href="https://papers.nips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf" target="_blank">paper</a></li>
<li>Jiang, W.-B., Zhao, L., &amp; Lu, B.-L. (2024). Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. <em>ICLR 2024</em>. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">proceedings</a></li>
<li>Wang, G., Liu, W., He, Y., Xu, C., Ma, L., &amp; Li, H. (2024). EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. <em>NeurIPS 2024</em>. <a href="https://neurips.cc/virtual/2024/poster/93793" target="_blank">poster / abstract</a></li>
<li>Lee, N., Barmpas, K., Panagakis, Y., Adamos, D., Laskaris, N., &amp; Zafeiriou, S. (2025). Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. <em>ICML 2025 poster</em>. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">OpenReview</a></li>
<li>EEG Foundation Challenge (2025). From Cross-Task to Cross-Subject EEG Decoding. <em>NeurIPS 2025 competition</em>. <a href="https://eeg2025.github.io/" target="_blank">official website</a></li>
<li>EEG Foundation Challenge (2025). Rules. <a href="https://eeg2025.github.io/rules/" target="_blank">official rules</a></li>
<li>EEG Foundation Challenge (2025). Submission. <a href="https://eeg2025.github.io/submission/" target="_blank">submission page</a></li>
<li>Xiong, W., Li, J., Li, J., &amp; Zhu, K. (2025). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <em>arXiv</em>. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>El Ouahidi, Y., Lys, J., Thölke, P., Farrugia, N., Pasdeloup, B., Gripon, V., Jerbi, K., &amp; Lioi, G. (2025). REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. <em>accepted poster / arXiv manuscript</em>. <a href="https://arxiv.org/abs/2510.21585" target="_blank">arXiv:2510.21585</a></li>
<li>Han, D. D., Gwon, Y., Lee, A. L., et al. (2025). DIVER-1: Deep Integration of Vast Electrophysiological Recordings at Scale. <em>under-review / arXiv manuscript</em>. <a href="https://arxiv.org/abs/2512.19097" target="_blank">arXiv:2512.19097</a></li>
<li>Wang, S., Deng, Y., Bao, Z., Zhan, X., &amp; Duan, Y. (2025). NeuroTTT: Bridging Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training. <em>arXiv preprint</em>. <a href="https://arxiv.org/abs/2509.26301" target="_blank">arXiv:2509.26301</a></li>
<li>Lahiri, J. B., Runwal, P., Kulkarni, A., Jain, M., Mishra, A. R., Panwar, S., &amp; Singh, S. (2026). PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. <em>arXiv preprint</em>. <a href="https://arxiv.org/abs/2603.02268" target="_blank">arXiv:2603.02268</a></li>
</ol>
