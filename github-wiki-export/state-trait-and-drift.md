# Wiki: state, trait, and drift

> Do not turn same-day success, algorithmic rescue, and long-term stability into the same claim
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-21 / 位置づけ: Technical / natural science only

## このページの役割
This page explains how Mind-Upload reads state, trait, and drift when a result spans hours, days, weeks, or months. The point is not only that signals change over time, but that several different time problems coexist: state fluctuation, trait-like backbone, biological drift, interface / decoder drift, and the operational burden of keeping a system usable.

## 正確さの前提
This page treats state / trait / drift only as technology and natural-science audit items. It does not address philosophical identity or legal rights.

## 公開ページへ戻る
- [Verification: Temporal Validity Card](https://mind-upload.com/verification.html#temporal-validity-card)
- [Datasets: generalization families](https://mind-upload.com/datasets.html#generalization-families)
- [EEG 101](https://mind-upload.com/eeg_101.html)

## 関連 Wiki
- [Wiki: Uncertainty, calibration, and abstention](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - Use this page when temporal claims also need confidence, coverage, and fallback logic.
- [Wiki: Closed loops, latency, jitter, and safe stops](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - Use this page when temporal validity intersects with online operation.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Use this page when state or backbone claims depend on latent inference rather than direct observation.

## いま分かっていること
- Behavioral state, arousal, uninstructed movement, and spontaneous behavior can dominate apparent same-day neural variance.
- Population-level structure can remain more stable than individual units, so unit drift and backbone stability must not be collapsed.
- Fixed-decoder horizon, recalibration burden, and stabilization strategy answer different questions.
- Current speech and cursor BCI papers support important communication and control advances, but they still need an explicit transfer ceiling.

## まだ分かっていないこと
- There is still no site-wide default benchmark that compares state annotation, fixed-decoder durability, recalibration burden, and transfer ceiling across EEG and invasive BCI under one schema.
- It remains unsettled which backbone object should be the default trait target for WBE-relevant longitudinal claims.
- It is also unsettled how far algorithmic stabilization can be extended before changing the claim from fixed-decoder durability to adaptive operation.

---

<h2>Bottom line in one sentence</h2>
<p>
On this site, <strong>state</strong>, <strong>trait</strong>, and <strong>drift</strong> are not treated as three loose labels. They are unpacked into <strong>state annotation</strong>, <strong>trait-like backbone</strong>, <strong>biological drift</strong>, <strong>interface / decoder drift</strong>, <strong>recalibration burden</strong>, and <strong>transfer ceiling</strong> so a same-day fit or a rescued decoder is not silently promoted to long-term stability.
</p>

<h4>Three Misreadings To Stop Early</h4>
<ul>
<li><strong>Same-day success is not trait evidence:</strong> without state annotation, it may only reflect today's behavior, arousal, or setup.</li>
<li><strong>Adaptive rescue is not fixed-decoder durability:</strong> if alignment or recalibration was needed, that burden belongs in the result.</li>
<li><strong>One-person longitudinal success is not generic transfer:</strong> transfer ceiling must be stated explicitly.</li>
</ul>

<strong>How this page fits the site</strong>
<p>
The core public rule is the <a href="https://mind-upload.com/verification.html#temporal-validity-card">Verification: Temporal Validity Card</a>. This wiki is the technical background page for that card. If you want the operational submission fields, read Verification; if you want the underlying logic for why those fields are separated, read this page.
</p>

<strong>When a score looks good but you do not know what time claim it supports</strong>
<p>
Use <a href="https://mind-upload.com/datasets.html#generalization-families">Datasets: generalization families</a> first to separate within-session, cross-session, cross-subject, and adaptation results. Then return here to decide whether the paper actually showed <strong>state robustness</strong>, <strong>trait-like backbone</strong>, <strong>stabilized operation</strong>, or only a short fixed-decoder interval.
</p>

<h2>The five fields this site now audits for time validity</h2>
<p>
The main weakness of the older page was that it separated <strong>state</strong>, <strong>trait</strong>, and <strong>drift</strong> conceptually, but it still left too much room to read <strong>same-day success</strong>, <strong>algorithmic stabilization</strong>, and <strong>longitudinal deployability</strong> as one continuous story. The newer literature does not support that shortcut. The site therefore now fixes five separate fields.
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>What must be named</th>
<th>What not to overread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>fixed decoder interval</strong></td>
<td>How long the decoder or readout was held without retraining, realignment, or hidden operator adjustment.</td>
<td>Do not treat adaptive maintenance or periodic alignment as if the original decoder had simply remained valid.</td>
</tr>
<tr>
<td><strong>state annotation</strong></td>
<td>Arousal, spontaneous behavior, movement, task mode, day/night or within-day context, medication or stimulation state, and any other state labels that can move performance.</td>
<td>Do not read uncontrolled day-to-day variation as trait instability if the state itself was left unlogged.</td>
</tr>
<tr>
<td><strong>interface / decoder drift</strong></td>
<td>Electrode reattachment, impedance change, channel loss, preprocessing shift, feature-distribution shift, and software / decoder mismatch.</td>
<td>Do not collapse a failing fixed decoder into proof that the biological representation itself collapsed.</td>
</tr>
<tr>
<td><strong>recalibration burden</strong></td>
<td>How often recalibration occurred, how much labeled or inferred target data it used, how long it took, and what happened when it failed.</td>
<td>Do not say “drift is solved” when the result actually shows that drift can be absorbed at a named operational cost.</td>
</tr>
<tr>
<td><strong>transfer ceiling</strong></td>
<td>Whether the result stayed within one participant, one implant, one site, one task family, or one behavioral regime, and what it still does not establish.</td>
<td>Do not promote one-participant longitudinal success to generic transfer, broad deployment, or WBE-relevant longitudinal equivalence.</td>
</tr>
</tbody>
</table>

<h2>Why the old three-way split is not enough</h2>
<p>
If we say only “state is short-term, trait is stable, drift is change over time,” we still hide the crucial difference between <strong>what changed in the organism</strong> and <strong>what changed in the interface or decoder</strong>. We also hide the difference between a <strong>fixed decoder surviving</strong> and a <strong>system being kept alive by adaptation</strong>. The site therefore reads longitudinal results through four layers first, and then attaches the five temporal-validity fields above.
</p>
<table>
<thead>
<tr>
<th>Layer</th>
<th>What it means here</th>
<th>Typical timescale</th>
<th>Minimum evidence we want</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state fluctuation</strong></td>
<td>The momentary condition: arousal, spontaneous behavior, movement, task engagement, sleep pressure, pharmacological state, or time-of-day effects.</td>
<td>Seconds to hours, sometimes within one day.</td>
<td>State labels plus performance or neural-structure differences by state.</td>
</tr>
<tr>
<td><strong>trait-like backbone</strong></td>
<td>A relatively stable skeleton such as latent dynamics, representational geometry, or functional fingerprint.</td>
<td>Days to months, depending on the preparation.</td>
<td>Cross-session stability of a named backbone object, not only one feature or channel.</td>
</tr>
<tr>
<td><strong>biological drift</strong></td>
<td>Plasticity, learning, unit turnover, remapping, and other changes in the living system itself.</td>
<td>Days to months.</td>
<td>Evidence that separates unit-level volatility from population-level preservation or recovery.</td>
</tr>
<tr>
<td><strong>interface / decoder drift</strong></td>
<td>Changes caused by the recording interface, preprocessing chain, feature extractor, or decoder mismatch.</td>
<td>Within session to months.</td>
<td>A record of channel / interface change plus fixed-decoder degradation and recalibration burden.</td>
</tr>
</tbody>
</table>

<h2>What the primary literature now supports</h2>

<h3>1. State annotation is not optional</h3>
<p>
It is too weak to treat same-day fluctuation as mere nuisance. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> showed that cortex-wide neural activity during task performance is strongly shaped by uninstructed movements, and <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a> showed that spontaneous behavior rapidly changes not only activity magnitude but also functional-connectivity structure. More specifically for EEG control, <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> showed that movement-related EEG dynamics vary across a 10-hour day/night window and that robust decoding therefore requires adaptive decoders. On this site, that means <strong>state annotation</strong> is an independent field, not background prose.
</p>

<h3>2. Trait-like backbone sits above unit-level immutability</h3>
<p>
The safer reading is not “a trait means one neuron stays fixed.” <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a> showed that aligned low-dimensional cortical dynamics can remain stable over long periods even when recorded neurons turn over. <a href="https://doi.org/10.1038/nn.4135" target="_blank">Finn et al. (2015)</a> showed that functional-connectivity patterns can identify individuals across scan sessions. At the same time, <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">Roth &amp; Merriam (2023)</a> showed cumulative representational drift in human V1 over months while relative dissimilarity structure remained more stable, and <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">Noda et al. (2025)</a> showed that a population-level representational map can recover within days after selective neuron loss. Therefore, this site now reads <strong>trait</strong> as a named backbone object, not as single-feature immutability.
</p>

<h3>3. Stabilization and recalibration are not the same thing as fixed-decoder durability</h3>
<p>
Recent BCI papers sharpen this distinction. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a> showed that aligning latent dynamics can stabilize BCI decoding across long recordings, but that is still an <strong>alignment-based rescue strategy</strong>, not evidence that no drift occurred. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> then showed that long-term cursor BCI control can be maintained with unsupervised hidden-Markov-model recalibration, while also showing that the burden of recalibration and the choice of stabilization strategy matter. The site therefore now separates <strong>fixed decoder interval</strong> from <strong>recalibration burden</strong> and refuses to let “the system stayed usable” silently replace “the original decoder stayed valid.”
</p>

<h3>4. Speech and communication BCIs still need an explicit transfer ceiling</h3>
<p>
Communication-route papers are important, but their time claims still need a stop line. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> showed a streaming brain-to-voice neuroprosthesis with implicit speech detection and low-latency synthesis, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> showed an instantaneous voice-synthesis neuroprosthesis that kept silence during non-speech and quantified degradation of a fixed decoder over time. These are strong advances in online communication. But on this site they still do <strong>not</strong> establish broad cross-person transfer, multi-site portability, or indefinite fixed-decoder validity. That remaining ceiling must be written explicitly.
</p>

<h2>Minimum submission this site now expects for longitudinal claims</h2>
<table>
<thead>
<tr>
<th>Item</th>
<th>What must be reported at minimum</th>
<th>Stopped claim if missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state annotation</strong></td>
<td>Arousal / behavior / movement / task-mode labels, and when relevant, time-of-day or sleep-pressure context.</td>
<td>Same-day or cross-day differences cannot be read cleanly as trait or drift.</td>
</tr>
<tr>
<td><strong>fixed decoder interval</strong></td>
<td>The exact days or sessions over which the same decoder was held without retraining.</td>
<td>No claim of fixed-decoder durability or stable backbone may be made.</td>
</tr>
<tr>
<td><strong>stabilization / rescue mode</strong></td>
<td>Whether latent alignment, unsupervised recalibration, supervised recalibration, or human operator intervention was used.</td>
<td>Adaptive operation cannot be rephrased as fixed-decoder stability.</td>
</tr>
<tr>
<td><strong>recalibration burden</strong></td>
<td>Frequency, duration, amount of target data, and failure / fallback behavior.</td>
<td>Operational drift remains hidden and deployability cannot be claimed.</td>
</tr>
<tr>
<td><strong>transfer ceiling</strong></td>
<td>One line stating whether the result is still limited to one participant, one implant, one site, one task family, or one behavioral regime.</td>
<td>The result stays as participant-specific longitudinal evidence only.</td>
</tr>
</tbody>
</table>

<h2>Common misreadings and demotion rules on this site</h2>
<table>
<thead>
<tr>
<th>Dangerous reading</th>
<th>Why it is too strong</th>
<th>How this site demotes it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>"The score matched on the same day, so the trait is stable."</strong></td>
<td>Without state annotation, same-day success can still ride on momentary behavior, arousal, or setup conditions.</td>
<td>Read as state-level evidence only.</td>
</tr>
<tr>
<td><strong>"Latent alignment or recalibration kept performance high, so drift is solved."</strong></td>
<td>The result may show that drift can be compensated, not that it vanished.</td>
<td>Report stabilization strategy and recalibration burden as separate outputs.</td>
</tr>
<tr>
<td><strong>"The fixed decoder failed, so the biological representation collapsed."</strong></td>
<td>Interface / decoder drift can break performance even when a backbone remains.</td>
<td>Require separation of biological drift from interface / decoder drift.</td>
</tr>
<tr>
<td><strong>"Low latency plus several days of use means long-term deployability."</strong></td>
<td>Latency, fixed-decoder durability, and recalibration burden are different audits.</td>
<td>Do not promote to long-term deployability without all three fields.</td>
</tr>
<tr>
<td><strong>"Participant-specific longitudinal success means generic transfer."</strong></td>
<td>One-participant success does not close cross-person, cross-site, or cross-task transfer.</td>
<td>Attach an explicit transfer ceiling.</td>
</tr>
<tr>
<td><strong>"A stable population map means every unit is stable."</strong></td>
<td>Population-level homeostasis can coexist with unit-level volatility.</td>
<td>Keep unit drift and backbone stability in separate columns.</td>
</tr>
</tbody>
</table>

<h2>Operating rules adopted by this site</h2>

<h4>Rule</h4>
<ul>
<li><strong>Do not report time validity in one number:</strong> fixed decoder interval, state annotation, recalibration burden, and transfer ceiling stay separate.</li>
<li><strong>Trait must name its backbone:</strong> latent dynamics, representational geometry, functional fingerprint, or another explicit object.</li>
<li><strong>Adaptive rescue must be visible:</strong> if alignment or recalibration was used, say so and report the cost.</li>
<li><strong>Biological drift and interface drift are different failure modes:</strong> do not collapse them into one “nonstationarity” line.</li>
<li><strong>Session dates and intervals are required:</strong> intraday, daily, weekly, and monthly claims must be distinguishable.</li>
<li><strong>Every longitudinal result needs a stop line:</strong> say what still cannot be inferred from the reported horizon.</li>
</ul>

<h2>References</h2>
<ol>
<li>Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. <em>Nature Neuroscience</em>. 2019;22:1677-1686. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <em>Nature Neuroscience</em>. 2024;27:148-158. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Scientific Reports</em>. 2024;14:21209. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Gallego JA, Perich MG, Chowdhury RH, Solla SA, Miller LE. Long-term stability of cortical population dynamics underlying consistent behavior. <em>Nature Neuroscience</em>. 2020;23:260-270. <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">doi:10.1038/s41593-019-0555-4</a></li>
<li>Finn ES, Shen X, Scheinost D, et al. Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. <em>Nature Neuroscience</em>. 2015;18:1664-1671. <a href="https://doi.org/10.1038/nn.4135" target="_blank">doi:10.1038/nn.4135</a></li>
<li>Roth ZN, Merriam EP. Representations in human primary visual cortex drift over time. <em>Nature Communications</em>. 2023;14:4422. <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">doi:10.1038/s41467-023-40144-w</a></li>
<li>Noda T, Kienle E, Eppler J-B, et al. Homeostasis of a representational map in the neocortex. <em>Nature Neuroscience</em>. 2025;28:1533-1545. <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">doi:10.1038/s41593-025-01982-7</a></li>
<li>Karpowicz BM, O'Shea DJ, Wyche S, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. <em>Nature Communications</em>. 2025;16:3500. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">doi:10.1038/s41467-025-59652-y</a></li>
<li>Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>. 2025;28:1318-1328. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>. 2025;644:145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
</ol>
