---
layout: default
title: 'Wiki: Terminology guide from measurement to modeling'
description: We will explain EEG, QC, BIDS, inverse problems, ESI, DCM, SCM, etc.
  by linking them with the flow from observation to verification and audit items.
article_type: Wiki
subtitle: Don't memorize words by dots, connect them by flow.
author: Mind Uploading Research Project
last_updated: '2026-03-26'
note: Learning guide
audience: People who see a mix of measurement words and model words, and people who
  want to understand a glossary in a flow.
reading_time: 10-15 minutes
page_intro: This page is a wiki for understanding measurement terms such as EEG, model
  terms such as ESI and DCM, and operational terms such as BIDS and QC by connecting
  them in the flow of ``observation → organization → estimation → verification.''
  Rather than memorizing individual words, the aim is to first distinguish which words
  to use and where to stop making an argument.
accuracy_note: The flow shown here is organized for understanding. Although there
  are back-and-forths and exceptions in actual research, it is important not to confuse
  observation and estimation, and estimation and verification.
page_highlights:
- You can understand EEG, QC, BIDS, ESI, DCM, and SCM in one flow.
- We will use audit items to isolate the reason why observation alone does not equate
  to reconstruction.
- ESI, DCM, and SCM do not fail in the same way; each one needs a different stop rule.
- More modalities, same-brain linkage, and connectome constraints do not bypass route
  cards; fusion, bridge, and identifiability remain separate audits.
- Reorder definitions in the glossary by working order and strength of evidence.
known_points:
- Measurement, preprocessing, estimation, and verification have different roles and
  different words are used for each.
- The observed signal is not the brain state as it is, and estimation involves uncertainty
  and candidate model dependence.
- BIDS and QC are not an added bonus; they are the backbone of comparability.
- Solver names do not determine claim strength; validation ladders and route cards do.
- Same-session multimodal and same-brain language do not by themselves solve fusion
  validity or state continuity.
unknown_points:
- The extent to which non-invasive measurements alone can restore sufficient internal
  state for WBE remains an open question.
- Which modeling combinations will ultimately be most effective is still being studied.
- The extent to which causality can be identified using observational data alone varies
  greatly depending on the intervention design.
wiki_links:
- label: 'Wiki: Basics of EEG'
  url: /wiki/eeg-basics.html
  description: As an entry point to measurements, you can see what EEG measures.
- label: 'Wiki: EEG pretreatment and QC'
  url: /wiki/eeg-preprocessing-and-qc.html
  description: Compensate on what changes the outcome during the organizing stage.
- label: 'Wiki: Basics of verification infrastructure'
  url: /wiki/verification-basics.html
  description: Make up for what to fix in the final validation step.
recommended_pages:
- label: Glossary
  url: /glossary.html
- label: Introduction to EEG
  url: /eeg_101.html
- label: Verification platform
  url: /verification.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest map</h2>
<p>
The words on this site can be roughly divided into four levels. These are to <strong>observe</strong>, <strong>arrange</strong>, <strong>estimate</strong>, and <strong>confirm</strong>. Even if the words seem difficult, confusion will be reduced if you first explain what stage the story is in.
</p>
</div>

<div class="note-box">
<strong>2026-03 correction to the beginner route</strong>
<p>
The older beginner route on this site grouped ESI, DCM, and SCM together too loosely as "modeling words." That was too weak. On this site, <strong>ESI is read through a validation ladder</strong>, <strong>DCM through candidate-model disclosure and model recovery</strong>, and <strong>SCM through intervention conditions and equivalence-class narrowing</strong>.
</p>
</div>

<div class="note-box">
<strong>2026-03-26 correction to the beginner route</strong>
<p>
A second beginner overread also remained: more sensors, same-brain linkage, or a connectome prior can sound as if the candidate set were almost closed. On this site, that is still too strong. Same-session multimodal work needs a <a href="multimodal-integration-basics.html">Fusion Card</a>, sequential same-brain or cross-day claims need a <a href="state-continuity-bridge.html">State-Continuity Bridge Card</a>, and connectome-constrained predictors still need an <a href="observation-to-estimation.html#identifiability-card">Identifiability Card</a>. The detailed rule lives in <a href="observation-to-estimation.html">Wiki: From observation to estimation</a>.
</p>
</div>

<section class="section" id="four-steps">
<h2 class="section-title">View in 4 levels</h2>
<table class="data-table">
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
</section>

<section class="section" id="observation">
<h2 class="section-title">1. Observation: First get the signal</h2>
<p>
EEG and MEG do not directly look inside the brain, but rather measure signals that can be observed from outside. The important point here is that<strong>what you observe is not the same as what is really happening in</strong>the brain.
</p>
<table class="data-table">
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
</section>

<section class="section" id="cleanup">
<h2 class="section-title">2. Organize: Don't believe the signal as it is</h2>
<p>
The observed signals include blinks, myoelectricity, body movements, equipment noise, etc. Therefore, the next step is QC and pre-treatment. This is not a matter of improving the appearance, but of <strong>recording what information has been kept and what has been removed</strong>.
</p>
<div class="key-points">
<h4>Words used here</h4>
<ul>
<li><strong>QC:</strong>Leave missing, noise, artifact, and exclusion reasons in numerical form. </li>
<li><strong>Preprocessing:</strong> Set up reference methods, filters, artifact removal, etc. </li>
<li><strong>BIDS:</strong>A standard for aligning data and metadata in a way that others can track them. </li>
</ul>
</div>
<p>
If you skip this step, even if a high-performance model comes out later, it will not provide comparable evidence.
</p>
</section>

<section class="section" id="estimation">
<h2 class="section-title">3. Estimation: How much can we tell from observations</h2>
<p>
We want to estimate brain activity and causal structure based on the organized signals. This is where inverse problems, ESI, DCM, and SCM come into play. However, it must be remembered at this stage that<strong>the estimate is an estimate, and uncertainty and candidate model dependence remain</strong>.
</p>
<table class="data-table">
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
<td>This is the general problem of estimating hidden causes from externally observed signals. </td>
<td>The solution is not unique by default, so geometry, regularization, and uncertainty remain part of the result. </td>
</tr>
<tr>
<td><strong>ESI</strong></td>
<td>A framework for estimating brain sources from EEG using a forward model, anatomy, and explicit assumptions. </td>
<td>Not only the point estimate but also the uncertainty and <strong>which validation class was passed</strong> must be reported. </td>
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
<div class="note-box">
<strong>Changes that are likely to occur here</strong>
<p>
Observing an EEG is not the same as uniquely reconstructing brain states. Furthermore, being correct in a correlational prediction is not the same as knowing the causal structure.
</p>
</div>
<div class="note-box">
<strong>Supplementary information for 2026-03</strong>
<p>
DCM is a comparison of candidate generative models, and SCM is a language that facilitates describing interventions and counterfactuals. Causal equivalence classes often remain from observational data alone, so it is necessary to read the candidate model space, family comparison, external validation, and the presence or absence of intervention data separately. For more information, see <a href="observation-to-estimation.html">Wiki: From observation to estimation</a>.
</p>
</div>

<div class="note-box">
<strong>Read ESI by validation class, not solver name</strong>
<p>
Michel &amp; Brunet (2019) summarize ESI as a multi-step pipeline rather than a one-word method. More importantly, Mikulan et al. (2020), Unnwongse et al. (2023), and Hao et al. (2025) show that intracranial stimulation, simultaneous SEEG/ECoG, and related direct-validation routes answer different error questions. On this site, a claim that says only "we used ESI" does not say enough. It has to disclose <strong>which validation ladder was passed</strong>.
</p>
</div>

<div class="note-box">
<strong>Read DCM by candidate-model rule, not causal wording</strong>
<p>
Penny et al. (2004) fixed that DCM inference is relative to the compared model set, Rosa et al. (2012) showed how post-hoc model-space search can be expanded, and Frässle et al. (2021) plus Wu et al. (2024) pushed whole-brain and faster estimation. Those are advances in <strong>tractability</strong>, not automatic solutions to identifiability. On this site, DCM therefore remains a <strong>model-conditioned causal hypothesis</strong> unless candidate space, recovery, reliability, and validation are disclosed.
</p>
</div>
</section>

<section class="section" id="verification">
<h2 class="section-title">4. Verification: How to trust estimates</h2>
<p>
The final question is, "Can other people confirm this estimation or model under the same conditions?" This is where words like Benchmark, Baseline, Preregistration, and Model Card come into play.
</p>
<table class="data-table">
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
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review of the analysis steps. <em>Frontiers in Neurology</em>, 10, 325. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <em>Journal of Neuroscience Methods</em>, 208(1), 66-78. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Frässle, S., Paulus, F. M., Krach, S., &amp; Jansen, A. (2016). Test-retest reliability of effective connectivity in the face perception network. <em>Human Brain Mapping</em>, 37(2), 730-744. <a href="https://doi.org/10.1002/hbm.23061" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle, S., Manjaly, Z. M., Do, C. T., Kasper, L., Pruessmann, K. P., &amp; Stephan, K. E. (2021). Whole-brain estimates of directed connectivity for human connectomics. <em>NeuroImage</em>, 225, 117491. <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Wu, H., Hu, X., &amp; Zeng, Y. (2024). A fast dynamic causal modeling regression method for fMRI. <em>NeuroImage</em>, 304, 120954. <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">doi:10.1016/j.neuroimage.2024.120954</a></li>
</ol>
</section>

<section class="section" id="boundary">
<h2 class="section-title">What has been learned from this process and what is still unknown</h2>
<table class="data-table">
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
</tbody>
</table>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
Please use <a href="../glossary.html">Glossary</a> to return to a short definition, <a href="../eeg_101.html">Introduction to EEG</a> to read the role of EEG again, and <a href="../verification.html">Verification infrastructure</a> to proceed to comparable verification.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-basics.html">EEG basics →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG preprocessing and QC →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../glossary.html">Glossary →</a></li>
<li><a href="../eeg_101.html">Introduction to EEG →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
</aside>
</main>
