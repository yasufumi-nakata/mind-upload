# Wiki: Terminology guide from measurement to modeling

> Don't memorize words by dots, connect them by flow.
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-27 / 位置づけ: Learning guide

## このページの役割
This page is a wiki for understanding measurement terms such as EEG, model terms such as ESI and DCM, and operational terms such as BIDS and QC by connecting them in the flow of ``observation → organization → estimation → verification.'' Rather than memorizing individual words, the aim is to first distinguish which words to use and where to stop making an argument.

## 正確さの前提
The flow shown here is organized for understanding. Although there are back-and-forths and exceptions in actual research, it is important not to confuse observation and estimation, and estimation and verification.

## 公開ページへ戻る
- [Glossary](https://mind-upload.com/glossary.html)
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Verification platform](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - As an entry point to measurements, you can see what EEG measures.
- [Wiki: EEG pretreatment and QC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - Compensate on what changes the outcome during the organizing stage.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Make up for what to fix in the final validation step.

## いま分かっていること
- Measurement, preprocessing, estimation, and verification have different roles and different words are used for each.
- The observed signal is not the brain state as it is, and estimation involves uncertainty and candidate model dependence.
- BIDS and QC are not an added bonus; they are the backbone of comparability.
- Solver names do not determine claim strength; validation ladders and route cards do.
- For inverse problems, field visibility, conductivity sensitivity, solver uncertainty, and validation class are different questions; progress in one does not erase the others.
- Same-session multimodal and same-brain language do not by themselves solve fusion validity or state continuity.

## まだ分かっていないこと
- The extent to which non-invasive measurements alone can restore sufficient internal state for WBE remains an open question.
- Which modeling combinations will ultimately be most effective is still being studied.
- The extent to which causality can be identified using observational data alone varies greatly depending on the intervention design.
- Which inverse-problem route or validation ladder generalizes beyond focal or clinical benchmark regimes remains unresolved.

---

<h2>The shortest map</h2>
<p>
The words on this site can be roughly divided into four levels. These are to <strong>observe</strong>, <strong>arrange</strong>, <strong>estimate</strong>, and <strong>confirm</strong>. Even if the words seem difficult, confusion will be reduced if you first explain what stage the story is in.
</p>

<strong>2026-03 correction to the beginner route</strong>
<p>
The older beginner route on this site grouped ESI, DCM, and SCM together too loosely as "modeling words." That was too weak. On this site, <strong>ESI is read through a validation ladder</strong>, <strong>DCM through candidate-model disclosure and model recovery</strong>, and <strong>SCM through intervention conditions and equivalence-class narrowing</strong>.
</p>

<strong>2026-03-26 correction to the beginner route</strong>
<p>
A second beginner overread also remained: more sensors, same-brain linkage, or a connectome prior can sound as if the candidate set were almost closed. On this site, that is still too strong. Same-session multimodal work needs a <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/multimodal-integration-basics">Fusion Card</a>, sequential same-brain or cross-day claims need a <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge">State-Continuity Bridge Card</a>, and connectome-constrained predictors still need an <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation#identifiability-card">Identifiability Card</a>. The detailed rule lives in <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">Wiki: From observation to estimation</a>.
</p>

<strong>2026-03-27 correction to the inverse-problem route</strong>
<p>
One more beginner overread still remained: <strong>inverse-problem progress</strong> could still sound like one continuous bar. The primary literature does not support that shortcut. <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a>, <a href="https://doi.org/10.1002/hbm.20571" target="_blank">Goldenholz et al. (2009)</a>, and <a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al. (2021)</a> show that <strong>field formation and head-model detail</strong> already limit what reaches the sensors. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> and <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026)</a> show that <strong>conductivity uncertainty and estimation</strong> still materially move the result. <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>, <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025)</a>, and <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> improve how <strong>candidate sets and uncertainty</strong> are exposed inside a stated inverse family. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">Pascarella et al. (2023)</a>, <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>, and <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> then validate different <strong>source regimes and error questions</strong>. Therefore, on this site, inverse papers are no longer read as one ladder.
</p>

<h2>View in 4 levels</h2>
<table>
<thead>
<tr>
<th>stage</th>
<th>Words that are easy to appear here</th>
<th>What are you doing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Observation</strong></td>
<td>EEG, MEG, fMRI, ECoG</td>
<td>We first measure the signals coming out from the brain and body. </td>
</tr>
<tr>
<td><strong>2. Organize</strong></td>
<td>QC, pretreatment, BIDS</td>
<td>Check for noise and defects and arrange it into a shape that others can follow. </td>
</tr>
<tr>
<td><strong>3. Estimation</strong></td>
<td>Inverse problem, ESI, DCM, SCM</td>
<td>Think about how far you can estimate the state and causal structure in the brain from observations, and which route card fixes the ceiling. </td>
</tr>
<tr>
<td><strong>4. Verification</strong></td>
<td>Benchmark, baseline, pre-registration, model card</td>
<td>Check whether the estimation or model really holds true in a comparable manner. </td>
</tr>
</tbody>
</table>

<h2>1. Observation: First get the signal</h2>
<p>
EEG and MEG do not directly look inside the brain, but rather measure signals that can be observed from outside. The important point here is that<strong>what you observe is not the same as what is really happening in</strong>the brain.
</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>In one word</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>This is a method to quickly measure the potential difference on the scalp. While it is resistant to changes over time, it is easily blurred spatially. </td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>This is a method of measuring magnetic fields. Although it is complementary to EEG, it is expensive and has significant equipment limitations. </td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>This is a method to measure changes in blood flow. It is strong in position, but slow in time resolution. </td>
</tr>
<tr>
<td><strong>ECoG</strong></td>
<td>This is an invasive measurement that measures near the brain surface. Although it is highly accurate, there are strong restrictions on the applicable range. </td>
</tr>
</tbody>
</table>

<h2>2. Organize: Don't believe the signal as it is</h2>
<p>
The observed signals include blinks, myoelectricity, body movements, equipment noise, etc. Therefore, the next step is QC and pre-treatment. This is not a matter of improving the appearance, but of <strong>recording what information has been kept and what has been removed</strong>.
</p>

<h4>Words used here</h4>
<ul>
<li><strong>QC:</strong>Leave missing, noise, artifact, and exclusion reasons in numerical form. </li>
<li><strong>Preprocessing:</strong> Set up reference methods, filters, artifact removal, etc. </li>
<li><strong>BIDS:</strong>A standard for aligning data and metadata in a way that others can track them. </li>
</ul>

<p>
If you skip this step, even if a high-performance model comes out later, it will not provide comparable evidence.
</p>

<h2>3. Estimation: How much can we tell from observations</h2>
<p>
We want to estimate brain activity and causal structure based on the organized signals. This is where inverse problems, ESI, DCM, and SCM come into play. However, it must be remembered at this stage that<strong>the estimate is an estimate, and uncertainty and candidate model dependence remain</strong>.
</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>What it adds</th>
<th>What still has to be disclosed</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Inverse problem</strong></td>
<td>This is the general family of routes that estimate hidden causes from externally observed signals. </td>
<td>The solution is not unique by default, so <strong>field visibility</strong>, <strong>forward-model or conductivity burden</strong>, <strong>solver uncertainty</strong>, and <strong>validation class</strong> remain part of the result. </td>
</tr>
<tr>
<td><strong>ESI</strong></td>
<td>A concrete inverse workflow that combines a head model, source prior, and estimation rule to produce candidate source configurations. </td>
<td>One polished map is not enough; disclose <strong>field visibility</strong>, <strong>forward-model burden</strong>, <strong>cross-solver or posterior spread</strong>, and the <strong>validation class or source regime</strong> that was actually tested. </td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>A framework for comparing candidate generative circuit models and asking which one better explains the observation. </td>
<td>The result still depends on the candidate model space, priors, family comparison, recovery, and external validation. </td>
</tr>
<tr>
<td><strong>SCM</strong></td>
<td>A language for making interventions and counterfactuals explicit. </td>
<td>With observational data alone, equivalence classes often remain, so intervention design still determines how strong the causal claim can become. </td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th>Inverse-problem gate</th>
<th>What question it answers</th>
<th>Representative primary literature</th>
<th>What it still does not close</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1: Field-formation visibility</strong></td>
<td>Does the target source class generate a usable scalp field under the actual orientation, extent, anatomy, and head-model detail?</td>
<td><a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a>; <a href="https://doi.org/10.1002/hbm.20571" target="_blank">Goldenholz et al. (2009)</a>; <a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al. (2021)</a></td>
<td>A visible source class can still remain poorly localized, poorly identified, or weakly validated.</td>
</tr>
<tr>
<td><strong>Gate 2: Forward-model / conductivity burden</strong></td>
<td>How much do skull or tissue conductivity and geometry assumptions move localization, depth, magnitude, or orientation?</td>
<td><a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a>; <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026)</a></td>
<td>Reducing conductivity-driven spread does not by itself collapse solver degeneracy or prove source recovery in every regime.</td>
</tr>
<tr>
<td><strong>Gate 3: Solver-family / posterior uncertainty</strong></td>
<td>Does the method expose alternative source configurations, intervals, or extended-source uncertainty instead of one polished point map?</td>
<td><a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>; <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025)</a>; <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a></td>
<td>Better uncertainty exposure does not repair missing observability, wrong head models, or unmatched validation classes.</td>
</tr>
<tr>
<td><strong>Gate 4: Validation class / source regime</strong></td>
<td>Which error question was actually tested: known stimulation site, focal-source board, simultaneous invasive concordance, or clinical ictal localization?</td>
<td><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a>; <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">Pascarella et al. (2023)</a>; <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>; <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a></td>
<td>Validation success in one regime is not a universal winner for focal, extended, spontaneous, and deep-source recovery together.</td>
</tr>
</tbody>
</table>

<strong>Changes that are likely to occur here</strong>
<p>
Observing an EEG is not the same as uniquely reconstructing brain states. Furthermore, being correct in a correlational prediction is not the same as knowing the causal structure.
</p>

<strong>Supplementary information for 2026-03</strong>
<p>
DCM is a comparison of candidate generative models, and SCM is a language that facilitates describing interventions and counterfactuals. Causal equivalence classes often remain from observational data alone, so it is necessary to read the candidate model space, family comparison, external validation, and the presence or absence of intervention data separately. For more information, see <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">Wiki: From observation to estimation</a>.
</p>

<strong>Read ESI by four gates, not solver name</strong>
<p>
Michel &amp; Brunet (2019) summarize ESI as a multi-step pipeline rather than a one-word method. On top of that, <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a>, <a href="https://doi.org/10.1002/hbm.20571" target="_blank">Goldenholz et al. (2009)</a>, and <a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al. (2021)</a> show that field formation is already selective before inversion begins, <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> and <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026)</a> show that conductivity assumptions still move the result, and <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>, <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong et al. (2025)</a>, and <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> show why uncertainty has to be exposed rather than hidden. Finally, <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">Pascarella et al. (2023)</a>, <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>, and <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> validate different source regimes. On this site, a claim that says only "we used ESI" still does not say enough.
</p>

<strong>Read DCM by candidate-model rule, not causal wording</strong>
<p>
Penny et al. (2004) fixed that DCM inference is relative to the compared model set, Rosa et al. (2012) showed how post-hoc model-space search can be expanded, and Frässle et al. (2021) plus Wu et al. (2024) pushed whole-brain and faster estimation. Those are advances in <strong>tractability</strong>, not automatic solutions to identifiability. On this site, DCM therefore remains a <strong>model-conditioned causal hypothesis</strong> unless candidate space, recovery, reliability, and validation are disclosed.
</p>

<h2>4. Verification: How to trust estimates</h2>
<p>
The final question is, "Can other people confirm this estimation or model under the same conditions?" This is where words like Benchmark, Baseline, Preregistration, and Model Card come into play.
</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>What is it needed for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Benchmark</strong></td>
<td>Fix what will be compared and what indicators will be used to score. </td>
</tr>
<tr>
<td><strong>Baseline</strong></td>
<td>Places a starting point for advocating for improvements. </td>
</tr>
<tr>
<td><strong>Pre-registration</strong></td>
<td>Avoid changing the conditions later. </td>
</tr>
<tr>
<td><strong>Model card</strong></td>
<td>In addition to the score, we will also publish weaknesses, failure examples, leak countermeasures, and calculation conditions. </td>
</tr>
<tr>
<td><strong>Route card</strong></td>
<td>When ESI, connectivity, or DCM is used, we disclose the assumptions, validation class, abstention boundary, and what the result still does not identify. </td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review of the analysis steps. <em>Frontiers in Neurology</em>, 10, 325. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Ahlfors, S. P., Han, J., Belliveau, J. W., &amp; H&auml;m&auml;l&auml;inen, M. S. (2010). Sensitivity of MEG and EEG to source orientation. <em>Brain Topography</em>, 23(3), 227-232. <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">doi:10.1007/s10548-010-0154-x</a></li>
<li>Goldenholz, D. M., Ahlfors, S. P., H&auml;m&auml;l&auml;inen, M. S., Sharon, D., Ishitobi, M., Vaina, L. M., &amp; Stufflebeam, S. M. (2009). Mapping the signal-to-noise-ratios of cortical sources in magnetoencephalography and electroencephalography. <em>Human Brain Mapping</em>, 30(4), 1077-1086. <a href="https://doi.org/10.1002/hbm.20571" target="_blank">doi:10.1002/hbm.20571</a></li>
<li>Piastra, M. C., N&uuml;&szlig;ing, A., Vorwerk, J., Clerc, M., Engwer, C., &amp; Wolters, C. H. (2021). A comprehensive study on electroencephalography and magnetoencephalography sensitivity to cortical and subcortical sources. <em>Human Brain Mapping</em>, 42(4), 978-992. <a href="https://doi.org/10.1002/hbm.25272" target="_blank">doi:10.1002/hbm.25272</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Pascarella, A., Mikulan, E., Sciacchitano, F., et al. (2023). An in-vivo validation of ESI methods with focal sources. <em>NeuroImage</em>, 277, 120219. <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">doi:10.1016/j.neuroimage.2023.120219</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Vorwerk, J., Wolters, C. H., &amp; Baumgarten, D. (2024). Global sensitivity of EEG source analysis to tissue conductivity uncertainties. <em>Frontiers in Human Neuroscience</em>, 18, 1335212. <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">doi:10.3389/fnhum.2024.1335212</a></li>
<li>Luria, G., Viani, S., Pascarella, A., et al. (2024). The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. <em>Frontiers in Human Neuroscience</em>, 18, 1359753. <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">doi:10.3389/fnhum.2024.1359753</a></li>
<li>Tong, P. F., Yang, H., Ding, X., et al. (2025). Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">doi:10.1109/TMI.2024.3506596</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging extended E/MEG source activation with empirical Bayesian uncertainty quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Vorwerk, J., K&ouml;hler, T., G&uuml;llmar, D., et al. (2026). Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy. <em>Journal of Neural Engineering</em>, 23(1), 016007. <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">doi:10.1088/1741-2552/ae2f01</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <em>Journal of Neuroscience Methods</em>, 208(1), 66-78. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Frässle, S., Paulus, F. M., Krach, S., &amp; Jansen, A. (2016). Test-retest reliability of effective connectivity in the face perception network. <em>Human Brain Mapping</em>, 37(2), 730-744. <a href="https://doi.org/10.1002/hbm.23061" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle, S., Manjaly, Z. M., Do, C. T., Kasper, L., Pruessmann, K. P., &amp; Stephan, K. E. (2021). Whole-brain estimates of directed connectivity for human connectomics. <em>NeuroImage</em>, 225, 117491. <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Wu, H., Hu, X., &amp; Zeng, Y. (2024). A fast dynamic causal modeling regression method for fMRI. <em>NeuroImage</em>, 304, 120954. <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">doi:10.1016/j.neuroimage.2024.120954</a></li>
</ol>

<h2>What has been learned from this process and what is still unknown</h2>
<table>
<thead>
<tr>
<th>What we know</th>
<th>What we still don't know</th>
</tr>
</thead>
<tbody>
<tr>
<td>Which stage of work does the term belong to? </td>
<td>Which model ultimately adequately explains consciousness and identity? </td>
</tr>
<tr>
<td>How to read without confusing observation, estimation, and verification. </td>
<td>Is it possible to obtain sufficient information for WBE with non-invasive measurements alone? </td>
</tr>
<tr>
<td>Why are BIDS and QC part of the technology rather than the outside? </td>
<td>Which multimodal integration is ultimately best? </td>
</tr>
<tr>
<td>Why inverse-problem papers must be separated into visibility, forward-model burden, solver uncertainty, and validation class. </td>
<td>Which inverse route or validation ladder generalizes beyond focal or clinical benchmark regimes. </td>
</tr>
</tbody>
</table>

<h2>Where to go back next</h2>
<p>
Please use <a href="https://mind-upload.com/glossary.html">Glossary</a> to return to a short definition, <a href="https://mind-upload.com/eeg_101.html">Introduction to EEG</a> to read the role of EEG again, and <a href="https://mind-upload.com/verification.html">Verification infrastructure</a> to proceed to comparable verification.
</p>
