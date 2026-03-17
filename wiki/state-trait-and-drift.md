---
layout: default
title: "Wiki: state/trait/drift"
description: "We will organize state fluctuations, trait-like stability, expression drift on the biological side, and non-stationarity on the measurement/decoder side based on primary literature."
article_type: Wiki
subtitle: "'Today's status,' 'relatively stable framework,' and 'operational drift' will be audited separately."
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Technical / natural science only"
audience: "People who want to distinguish state/trait/drift based on actual measurement rather than intuition when reading longitudinal evaluation, cross-day decoding, and closed-loop BCI."
reading_time: "12-18 minutes"
page_intro: "This page is a wiki that organizes state (in-situ state), trait (relatively stable skeleton), and drift (changes that occur over time), which frequently appear in Mind-Upload's longitudinal evaluation, along with EEG, fMRI, chronic recording, and BCI primary literature. Rather than just distinguishing between short-term fluctuations and long-term changes, we aim to fix what time constant, mechanism, and evaluation system they are used for."
accuracy_note: "We do not deal with philosophy or legal systems here. We treat state / trait / drift as audit items of technology and natural science. We do not call traits 'immutable' and we do not treat any type of drift."
page_highlights:
  - "In the same signal, state fluctuations, trait-like skeletons, drift on the biological side, and drift on the measurement/decoder side coexist."
  - "It is safer to read traits as relatively stable skeletons, such as latent dynamics, representational geometry, and connectome fingerprints, rather than as single-neuron invariants."
  - "In closed-loop and speech BCI, fixed decoder degradation and recalibration burden are also part of drift."
known_points:
  - "Behavioral state, arousal, unintentional movement, and spontaneous behavior greatly influence trial-to-trial neural variance."
  - "The population-level structure and latent dynamics may remain more stable even with changes in a single unit or voxel."
  - "Long-term stability cannot be assessed without cross-day degradation and recalibration burden of the fixed decoder."
unknown_points:
  - "A site-wide standard for determining which task and which skeleton should be called a trait has not yet been fixed."
  - "A standard format for cross-sectionally comparing the accounting of biological drift and interface/decoder drift between EEG and invasive BCI has not yet been established."
  - "It is unclear up to which timescale the same trait backbone is considered as a long-term benchmark for WBE."
wiki_links:
  - label: "Wiki: Uncertainty, proofreading, abstaining"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "How to connect drift with margin of error, calibration, and coverage-risk."
  - label: "Wiki: Closed loop, delay, jitter, safe stop"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Corrects how to read drift and recalibration load in online systems."
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Compensates for the extent to which observed fluctuations can be lifted into latent states and structures."
recommended_pages:
  - label: "Verification base"
    url: "/verification.html"
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest conclusion</h2>
<p>
<strong>state</strong>, <strong>trait</strong>, and <strong>drift</strong> are more than just sorting data into three boxes. In reality, <strong>fluctuations in local behavior and arousal</strong>, <strong>relatively stable population backbone</strong>, <strong>representational drift on the biological side</strong>, and<strong>nonstationarity</strong> on the electrode/preprocessing/decoder side are all mixed together in the same recording. Therefore, this site separately audits <strong>timescale</strong>, <strong>origin</strong>, <strong>held-out degradation in fixed decoder</strong>, and <strong>recalibration load</strong>.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
We cannot proceed to a final determination of identity or rights here. We deal with longitudinal neuroscience and BCI technology and natural science. First, make sure that state is not misinterpreted as trait, trait is not rephrased as "a single neuron is unchanging", and drift is not reduced to one type.
</p>
</div>

<section class="section" id="four-buckets">
<h2 class="section-title">Read it in four parts first</h2>
<table class="data-table">
<thead>
<tr>
<th>layer</th>
<th>What does it refer to</th>
<th>Typical timescale</th>
<th>Minimum desired rating</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state fluctuation</strong></td>
<td>It is the state of the moment, such as alertness, fatigue, unintentional movement, spontaneous action, and task engagement. </td>
<td>Seconds to minutes, at most within the same day. </td>
<td>within-session Conditional differences, simultaneous measurement with behavioral and physiological indicators, and performance differences by state. </td>
</tr>
<tr>
<td><strong>trait-like backbone</strong></td>
<td>A relatively stable skeleton with latent dynamics, representational geometry, and functional fingerprints. </td>
<td>Day to month, depending on the assignment, yearly. </td>
<td>Cross-session identification, latent manifold alignment, and representational similarity stability. </td>
</tr>
<tr>
<td><strong>biological drift</strong></td>
<td>Changes in the living body, such as learning, plasticity, relocation of tuning, and replacement of responsive neurons. </td>
<td>Day to week to month. </td>
<td> Fixed readout aging, single-unit / voxel tuning changes, and population geometry retention. </td>
</tr>
<tr>
<td><strong>interface / decoder drift</strong></td>
<td>Depends on electrode reattachment, impedance change, feature distribution shift, decoder mismatch, and recalibration. </td>
<td>From between sessions to long-term operation. </td>
<td>Fixed decoder degradation, recalibration frequency, recovery time, and success or failure of unsupervised adaptation. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-old-three-way-split-is-not-enough">
<h2 class="section-title">Why the three traditional classifications are not enough</h2>
<p>
If we just say ``state is now, traits are stable for a long time, and drift is changes over time,'' we cannot see what originates from the brain and what originates from devices and decoders. Furthermore, traits can be read as if they were the invariance of a single neuron or a single feature. However, the primary literature repeatedly shows that, while<strong>individual units can move a lot,<strong>population-level relational structures can last longer.
</p>
<div class="note-box">
<strong>Safe reading on this site</strong>
<p>
A trait does not mean that one electrode, one neuron, or one voxel remains unchanged, but rather it is treated as a skeleton that remains relatively stable even across state fluctuations and some unit replacements. Conversely, a claim that does not look at fixed decoder degradation or recalibration dependence does not sufficiently demonstrate trait stability.
</p>
</div>
</section>

<section class="section" id="papers">
<h2 class="section-title">What the primary literature actually shows</h2>

<h3>1. State fluctuation is often the body, not “noise”</h3>
<p>
Musall et al. (2019) showed that cortex-wide activity during task performance is strongly controlled not only by task variables but also by<strong>uninstructed movements</strong>. Benisty et al. (2024) also show that spontaneous behavior is rapidly imprinted not only on the magnitude of cortical network activity but also on the correlational structure of functional connectivity. Therefore, even for the same subject and on the same day, a "match" or "mismatch" obtained without specifying the state does not directly serve as evidence of a trait or drift.
</p>

<h3>2. Trait-like backbone must be read above unit-level immutability</h3>
<p>
Gallego et al. (2020) tracked the sensorimotor cortex of monkeys for up to two years and showed that even when recorded neurons are replaced, low-dimensional latent dynamics remain stable, and decoding based on aligned latent dynamics can be maintained over a long period of time, while fixed decoders that directly depend on recorded activity deteriorate significantly. Finn et al. (2015) also show that functional connectivity profiles can be used to identify individuals across scan sessions, tasks, and rests. What we can say from this is that even if a trait exists, it is often visible at the level of a relation or manifold, and not as a still image of a single feature.
</p>

<h3>3. Representational drift is a change that an organism can make even in a stable environment</h3>
<p>
Roth and Merriam (2023) showed in longitudinal fMRI of human V1 that the cvR² of model fit decreases as the time between sessions increases, and they reported that representational drift accumulates on a monthly basis. On the other hand, representational dissimilarity itself is relatively stable, indicating that a relational structure that can be read downstream may remain. In addition, Noda et al. (2025) showed that in the mouse auditory cortex, the population-level representational map can be maintained even with individual neuron tuning volatility, and that it can recover within a few days even after selected neuron loss. In other words, even if biological drift exists, all levels do not collapse at the same speed.
</p>

<h3>4. Decoder drift and recalibration burden are two separate barriers in BCI operation</h3>
<p>
Wilson et al. (2025) showed that intracortical cursor BCI requires <strong>frequent recalibration</strong> due to accumulating neural nonstationarities and is difficult to maintain long-term without unsupervised target-inference recalibration. Wairagkar et al. (2025) also show that it is important to <strong>return silence during non-speech in instantaneous voice-synthesis neuroprosthesis, and that the performance of a decoder fixed at post-implant day 165 drops noticeably after about 15 days. Therefore, in an online system, it is not enough just to say that it worked on that day; it is also necessary to evaluate drift, including how many days the fixed decoder lasts, how much it depends on recalibration, and how it uses silence/abstention.
</p>
</section>

<section class="section" id="what-to-measure">
<h2 class="section-title">Minimum things to keep separate in longitudinal evaluation</h2>
<table class="data-table">
<thead>
<tr>
<th>Audit items</th>
<th>What I want at least</th>
<th>Claim that it stops when there is not enough</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state sensitivity</strong></td>
<td> Simultaneous measurement of arousal, amount of activity, unintentional movement, task engagement, pharmacological state, etc., and performance differences depending on conditions. </td>
<td>It cannot be said that it is stable with the same subject or that short-term discrepancies are errors. </td>
</tr>
<tr>
<td><strong>fixed-model stability</strong></td>
<td>No relearning How many days/weeks the decoder/readout was held and the deterioration curve for each interval. </td>
<td>It cannot be said that ``it has a trait backbone'' or ``it can be operated for a long period of time.'' </td>
</tr>
<tr>
<td><strong>population backbone</strong></td>
<td>Stability of relationship structures, including latent dynamics, representational similarity, and cross-session identification. </td>
<td>It cannot be shown what is conserved even within a single unit change. </td>
</tr>
<tr>
<td><strong>recalibration burden</strong></td>
<td>Recalibration frequency, time required, supervised/unsupervised, recovery time, fallback in case of failure. </td>
<td>online We talk about stability only in terms of accuracy and WER. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="misreadings">
<h2 class="section-title">Common misreadings and demotion rules on this site</h2>
<table class="data-table">
<thead>
<tr>
<th>Dangerous Reading</th>
<th>Why is it dangerous</th>
<th>Handling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>There is a trait because the reactions were similar on the same day</strong></td>
<td>It is possible that the state fluctuation is not suppressed sufficiently. </td>
<td>Same-day matches will be treated as state-level evidence and will not be raised as a trait claim. </td>
</tr>
<tr>
<td><strong>There is no trait because a single neuron/voxel has changed</strong></td>
<td>Population-level geometry and latent dynamics may be maintained. </td>
<td>Let unit-level drift and population backbone be reported separately. </td>
</tr>
<tr>
<td><strong>Performance returned after recalibration, so drift is not a problem</strong></td>
<td>This is not proof that there is no drift, but it may just be that the operation has absorbed the drift. </td>
<td>The number of recalibrations, time, and failure rate are separately calculated as part of the performance. </td>
</tr>
<tr>
<td><strong>Because the fixed decoder collapsed, the brain representation itself collapsed</strong></td>
<td>It may be an interface, feature extraction, or channel turnover issue. </td>
<td>Requires separation of biological drift and interface/decoder drift. </td>
</tr>
<tr>
<td><strong>Performance is low because there is a lot of silence / abstention</strong></td>
<td>It may be safer in actual operation to not forcefully output the low-confidence condition. </td>
<td>Coverage, risk, silence rate, and false output rate are output as a set. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Operation rules adopted by this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>Don't report state and traits in the same metric:</strong>Keep short-term fluctuations and long-term skeleton in separate columns. </li>
<li><strong>Trait is indicated as a skeleton: </strong>Specifies one of latent dynamics, similarity matrix, fingerprint, or stable subspace. </li>
<li><strong>Drift is divided into two systems:</strong>Representational drift on the biological side and interface/decoder drift are logged separately. </li>
<li><strong>Make fixed decoder interval:</strong>Do not hide how many days go by without recalibration. </li>
<li><strong>Recalibration burden is also about performance:</strong> Break down recalibration frequency, time required, and fallback separately from accuracy. </li>
<li><strong>Include session dates for longitudinal comparisons:</strong> Specify intraday, daily, weekly, or monthly. </li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <em>Nature Neuroscience</em>, 22, 1677-1686. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Benisty, H., Barson, D., Moberly, A. H., Lohani, S., Tang, L., Coifman, R. R., Crair, M. C., Cardin, J. A., &amp; Higley, M. J. (2024). Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <em>Nature Neuroscience</em>, 27, 148-158. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Gallego, J. A., Perich, M. G., Chowdhury, R. H., Solla, S. A., &amp; Miller, L. E. (2020). Long-term stability of cortical population dynamics underlying consistent behavior. <em>Nature Neuroscience</em>, 23, 260-270. <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">doi:10.1038/s41593-019-0555-4</a></li>
<li>Finn, E. S., Shen, X., Scheinost, D., Rosenberg, M. D., Huang, J., Chun, M. M., Papademetris, X., &amp; Constable, R. T. (2015). Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. <em>Nature Neuroscience</em>, 18(11), 1664-1671. <a href="https://doi.org/10.1038/nn.4135" target="_blank">doi:10.1038/nn.4135</a></li>
<li>Roth, Z. N., &amp; Merriam, E. P. (2023). Representations in human primary visual cortex drift over time. <em>Nature Communications</em>, 14, 4422. <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">doi:10.1038/s41467-023-40144-w</a></li>
<li>Noda, T., Kienle, E., Eppler, J.-B., Aschauer, D. F., Kaschube, M., Loewenstein, Y., &amp; Rumpel, S. (2025). Homeostasis of a representational map in the neocortex. <em>Nature Neuroscience</em>, 28, 1533-1545. <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">doi:10.1038/s41593-025-01982-7</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., Avansino, D. T., Pun, T. K., Gross, R., Hosman, T., Singer-Clark, T., Kapitonava, A., Hochberg, L. R., Simeral, J. D., Shenoy, K. V., Druckmann, S., Henderson, J. M., &amp; Willett, F. R. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., Hochberg, L. R., Brandman, D. M., &amp; Stavisky, S. D. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644, 145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
To go back to uncertainty and coverage-risk, go back to <a href="uncertainty-confidence-and-abstention.html">Uncertainty, calibration, abstention</a>, go back to log design for online operations go back to <a href="closed-loop-latency-jitter-and-safety-stops.html">closed-loop, delay, jitter, safety stops</a>, go back to overall pass/fail rules <a Please use href="../verification.html">Verification infrastructure</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="uncertainty-confidence-and-abstention.html">Uncertainty/proofreading/abstention →</a></li>
<li><a href="closed-loop-latency-jitter-and-safety-stops.html">Closed-loop/delay/jitter/safety stops →</a></li>
<li><a href="observation-to-estimation.html">From observation to estimation →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../tech_roadmap.html">Technology roadmap →</a></li>
<li><a href="../eeg_101.html">Introduction to EEG →</a></li>
</ul>
</div>
</aside>
</main>
