# Wiki: Baseline/Pre-registration/Model Card

> Thinking about 'what to compare, how to fix, and what to keep'
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-20 / 位置づけ: Learning guide

## このページの役割
This page is a wiki that organizes from the beginning the differences in the roles of ``baseline,'' ``benchmark,'' ``pre-registration,'' ``model card,'' and ``failure example,'' which appear repeatedly in Mind-Upload. Use it as a scaffold to understand the difference between getting a high score and making comparable progress.

## 正確さの前提
Here we will explain the differences in operational roles in an easy-to-understand manner. Please check the actual template and specifications on the public page.

## 公開ページへ戻る
- [Verification base](https://mind-upload.com/verification.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Casework](https://mind-upload.com/verification.html#casework)

## 関連 Wiki
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - First, let's go back to the big picture of Verification Commons.
- [Wiki: Data partitioning and leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Compensate for particularly dangerous leaks in benchmark operations.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other basic pages.

## いま分かっていること
- Comparable progress requires a starting point, scoring criteria, a priori rules, and a record of results.
- Without a baseline, it's harder to claim improvement.
- Lack of pre-registration and model cards makes it easier to conveniently interpret later.
- For multimodal or atlas-prior claims, acquisition relation, lag audit, co-registration, and fusion baseline are part of the result itself.
- For heterogeneous-corpus pretraining, corpus identity, harmonization, adaptation regime, and benchmark provenance are part of the result itself.

## まだ分かっていないこと
- Which templates will be standardized across WBE is still in the operational design stage.
- The extent to which failure cases and negative results will be required to be disclosed is subject to future development.

---

<h2>The shortest map</h2>
<p>
A baseline is a starting point, a benchmark is a ``scoring standard,'' pre-registration is a ``promise made before starting,'' a model card is a ``results report'', and failure examples are a ``record of where things went wrong.'' Any one alone is not comparable progress.
</p>

<strong>2026-03 Addendum</strong>
<p>
For L1 and higher results, in addition to the usual model card, we have attached an <a href="https://mind-upload.com/verification.html#observability-budget">Observability Budget</a> to make it operationally clear the measurement stack, direct observables, remaining latent state, claim ceiling, and abstention conditions.
</p>

<strong>2026-03-19 Addendum: foundation / self-supervised EEG results also need a Pretraining Card</strong>
<p>
The previous version still made it sound as if one generic model card could cover all EEG results once scores and weaknesses were listed. That is too weak for large-scale EEG pretraining. Recent source papers and benchmark operations show that <strong>corpus identity</strong>, <strong>setup diversity</strong>, <strong>harmonization policy</strong>, <strong>adaptation regime</strong>, and <strong>benchmark provenance</strong> materially change what a transfer result means. Therefore, this site now treats the <a href="https://mind-upload.com/verification.html#pretraining-card">Pretraining Card</a> as a separate artifact on top of the usual model card for foundation / self-supervised EEG results.
</p>

<strong>2026-03-20 Addendum: multimodal / atlas-prior results also need a Fusion Card</strong>
<p>
The remaining weakness was to let the words <strong>simultaneous</strong>, <strong>multimodal</strong>, or <strong>atlas-informed</strong> stand in for a validated fusion step. That is too weak. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> showed that synchronization middleware aligns streams but does not by itself certify device-side delay truth, <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">Wei et al. (2020)</a> showed that EEG-fMRI fusion remains model-conditioned, and <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> plus <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed that simultaneous multimodal recordings can reveal both common and divergent structure across modalities. Therefore, this site now treats the <a href="https://mind-upload.com/verification.html#fusion-card">Fusion Card</a> as a separate artifact on top of the usual model card and <a href="https://mind-upload.com/verification.html#observability-budget">Observability Budget</a> for multimodal or atlas-prior results.
</p>

<h2>First, separate roles</h2>
<table>
<thead>
<tr>
<th>Term</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Baseline</strong></td>
<td>This is the minimum comparison partner. This will be the starting point for making improvements. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Fix what, which data, and which indicators to compare. </td>
</tr>
<tr>
<td><strong>Pre-registration</strong></td>
<td>Before proceeding, fix the indicators, stopping conditions, and analysis policy. </td>
</tr>
<tr>
<td><strong>Model card</strong></td>
<td>Scores, weaknesses, leak countermeasures, failure examples, calculation conditions, and Observability Budget for L1 and above. </td>
</tr>
<tr>
<td><strong>Fusion Card</strong></td>
<td>For multimodal or atlas-prior results, fix acquisition relation, synchronization / lag audit, co-registration scope, fusion model, unimodal baseline, external calibration, and abstention boundary.</td>
</tr>
<tr>
<td><strong>Pretraining Card</strong></td>
<td>For foundation / self-supervised EEG results, fix corpus identity, overlap audit, harmonization, adaptation regime, benchmark provenance, and scale / efficiency.</td>
</tr>
<tr>
<td><strong>Failure examples/negative results</strong></td>
<td>Leave what didn't work and where it broke. </td>
</tr>
</tbody>
</table>

<h2>When a normal model card is not enough</h2>
<table>
<thead>
<tr>
<th>Artifact</th>
<th>What it fixes</th>
<th>What goes wrong if you stop there</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Model card</strong></td>
<td>Scores, baselines, failure examples, compute usage, and practical weaknesses of one trained system.</td>
<td>For foundation-model results, it can still hide what part of the gain came from pretraining corpus composition, harmonization choices, or downstream adaptation.</td>
</tr>
<tr>
<td><strong>Observability Budget</strong></td>
<td>What the measurement stack directly observed, what remained latent, and which claim ceiling still applies.</td>
<td>It does not say whether a transfer claim changed because of corpus overlap, benchmark design, or fine-tuning amount.</td>
</tr>
<tr>
<td><strong>Fusion Card</strong></td>
<td>Acquisition relation, lag audit, co-registration scope, fusion model, unimodal / prior-only baseline, and external calibration for multimodal or atlas-prior claims.</td>
<td>If it is missing, the fusion step can be overread as self-validating and a same-session combination can be misread as same-subject state identification.</td>
</tr>
<tr>
<td><strong>Pretraining Card</strong></td>
<td>Corpus identity / overlap, population and setup diversity, harmonization policy, adaptation regime, benchmark provenance, and scale / efficiency.</td>
<td>If it is missing, a same-benchmark win can be overread as generic transfer or portable robustness.</td>
</tr>
</tbody>
</table>

<h2>Why do we need them all</h2>
<table>
<thead>
<tr>
<th>What is missing</th>
<th>Common problems</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No baseline</strong></td>
<td>It becomes difficult to judge whether the numbers are good or bad, an improvement or a coincidence. </td>
</tr>
<tr>
<td><strong>No benchmark</strong></td>
<td>Each person will score differently, which will break the comparison. </td>
</tr>
<tr>
<td><strong>No pre-registration</strong></td>
<td>It will be easier to select only convenient conditions later. </td>
</tr>
<tr>
<td><strong>No model card</strong></td>
<td>Only the points remain, and weaknesses and reproduction steps are no longer visible. </td>
</tr>
<tr>
<td><strong>No failure cases</strong></td>
<td>It is easy to repeat the same mistakes because the failure point is not shared. </td>
</tr>
</tbody>
</table>

<h2>View with minimal flow</h2>

01

<h4>Put a baseline</h4>
<p>First of all, it may be simple, so let's use one as a starting point for comparison. </p>

02

<h4>Fix the benchmark</h4>
<p>Align data, divisions, indicators, and prohibitions. </p>

03

<h4>Pre-register</h4>
<p>Decide first which conditions will be considered success/failure. </p>

04

<h4>Leave model cards and failure examples</h4>
<p>Not only the score, but also the weaknesses and ways of collapse will be disclosed. </p>

<h2>Why are failure examples important?</h2>
<p>
If you collect only successful cases, only the conditions that happened to be successful will remain. In a field as big as Mind-Upload, keeping track of<strong>under what conditions it failed</strong> is just as important as keeping track of success stories.
</p>

<strong>Minimum requirements for failure examples</strong>
<p>
Under what conditions, which indicators collapsed, and by how much? It is necessary to isolate whether it was a leak or partition problem, whether it collapsed due to OOD, or whether there was insufficient computational resources.
</p>

<h2>Minimum checks when reading public pages</h2>

<h4>Checklist</h4>
<ul>
<li><strong>Is there a baseline?</strong>Is it clear what it is compared to? </li>
<li><strong>Are the benchmarks fixed:</strong>Are the data, splits, and metrics written? </li>
<li><strong>Are there any pre-registrations?</strong>Have the conditions been changed afterwards? </li>
<li><strong>Are there model cards or examples of failure?</strong>In addition to weaknesses and ways of collapse, is the Observability Budget visible at L1 and above? </li>
<li><strong>If it is a multimodal or atlas-prior result, is a Fusion Card visible?</strong>Are acquisition relation, lag audit, co-registration, fusion baseline, and external calibration written? </li>
<li><strong>If it is a foundation / self-supervised EEG result, is a Pretraining Card visible?</strong>Are corpus overlap, harmonization, adaptation, and benchmark version written? </li>
</ul>

<h2>References</h2>
<ol>
<li>Kostas, D., Aroca-Ouellette, S., &amp; Rudzicz, F. (2021). BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. <a href="https://doi.org/10.3389/fnhum.2021.653659" target="_blank">doi:10.3389/fnhum.2021.653659</a></li>
<li>Jiang, W.-B., Zhao, L., &amp; Lu, B.-L. (2024). Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. <a href="https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html" target="_blank">ICLR 2024 proceedings</a></li>
<li>Lee, N., Barmpas, K., Panagakis, Y., Adamos, D., Laskaris, N., &amp; Zafeiriou, S. (2025). Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. <a href="https://openreview.net/forum?id=J5SbLoq7Uv" target="_blank">ICML 2025 poster / OpenReview</a></li>
<li>EEG Challenge (2025). Rules. <a href="https://eeg2025.github.io/rules/" target="_blank">official rules</a></li>
<li>Xiong, W., Li, J., Li, J., Zhu, K., &amp; Jiang, C. (2025). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., Medine, D., Boulay, C., Grivich, M. I., Artoni, F., Mullen, T., Delorme, A., &amp; Makeig, S. (2025). The lab streaming layer for synchronized multimodal recording. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H., Jafarian, A., Zeidman, P., Litvak, V., Razi, A., Garrido, M., Friston, K., &amp; Daunizeau, J. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., Catana, C., Polimeni, J. R., Fan, J., Droppa, K. S., Patel, R., Wey, H.-Y., Chang, C., Manoach, D. S., Price, J. C., Sander, C. Y., &amp; Rosen, B. R. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
</ol>

<h2>Where to go back next</h2>
<p>
If you want to go back to the drawing board, use <a href="https://mind-upload.com/verification.html">Verification platform</a>, if you want to go back to practice, use <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a>, and if you want to go back to precedents in other fields, use <a href="https://mind-upload.com/verification.html#casework">Casework</a>.
</p>
