# Wiki: state, trait, and drift

> Do not turn same-day success, algorithmic rescue, and long-term stability into the same claim
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-04-01 / Role: Technical / natural science only

## Role Of This Page
This page explains how Mind-Upload reads state, trait, and drift when a result spans hours, days, weeks, or months. The point is not only that signals change over time, but that several different time problems coexist: state fluctuation, trait-like backbone, biological drift, interface / decoder drift, and the operational burden of keeping a system usable.

## Accuracy Notes
This page treats state / trait / drift only as technology and natural-science audit items. It does not address philosophical identity or legal rights.

## Back To Public Pages
- [Verification: Temporal Validity Card](https://mind-upload.com/verification.html#temporal-validity-card)
- [Datasets: generalization families](https://mind-upload.com/datasets.html#generalization-families)
- [EEG 101](https://mind-upload.com/eeg_101.html)

## Related Wiki Pages
- [Wiki: Uncertainty, calibration, and abstention](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - Use this page when temporal claims also need confidence, coverage, and fallback logic.
- [Wiki: Closed loops, latency, jitter, and safe stops](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - Use this page when temporal validity intersects with online operation.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Use this page when state or backbone claims depend on latent inference rather than direct observation.

## What Is Currently Known
- Behavioral state, arousal, uninstructed movement, and spontaneous behavior can dominate apparent same-day neural variance.
- Circadian phase, glucocorticoid exposure, and insulin / metabolic regime can also move memory or hippocampal plasticity without any change in the recording interface.
- Population-level structure can remain more stable than individual units, so unit drift and backbone stability must not be collapsed.
- Longitudinal identifiability can be carried by different objects such as dynamic functional-connectivity windows, EEG spectral profiles, aperiodic components, or nonlinear avalanche dynamics.
- Fixed-decoder horizon, recalibration burden, and stabilization strategy answer different questions.
- In invasive language BCIs, cross-subject transfer initialization, bounded fixed-decoder use, and adaptive rescue are different achievements rather than one longitudinal ladder.
- Current speech and cursor BCI papers support important communication and control advances, but they still need an explicit transfer ceiling.

## What Is Still Unknown
- There is still no site-wide default benchmark that compares state annotation, fixed-decoder durability, recalibration burden, and transfer ceiling across EEG and invasive BCI under one schema.
- It remains unsettled which backbone object should be the default trait target for WBE-relevant longitudinal claims.
- It also remains unsettled which fingerprint carriers survive cross-state transfer rather than only same-regime reacquisition.
- It is also unsettled how far algorithmic stabilization can be extended before changing the claim from fixed-decoder durability to adaptive operation.
- A shared default logging schema for slow internal-milieu variables across EEG, invasive BCI, and human memory studies is still incomplete.

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

<strong>2026-04-01 correction: invasive language BCIs are not one temporal-validity route</strong>
<p>
The remaining weakness on this page was that it already separated <strong>fixed-decoder durability</strong> from <strong>recalibration burden</strong>, but it still left too much room to read modern invasive language BCI papers as if they formed one monotonic time-stability ladder. The current primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>, <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> support different <strong>communication throughput / expressivity</strong> routes. <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a> supports a separate <strong>cross-subject transfer-initialization</strong> route. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a> and <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> support <strong>alignment-based rescue / unsupervised recalibration</strong> routes. On this site, those are no longer read as one interchangeable story about drift, stability, and deployability.
</p>

<strong>2026-03-28 addendum: fingerprint success is not yet one backbone object</strong>
<p>
The remaining weakness on this page was subtler than simple drift. It already said that <strong>trait</strong> must name a backbone object, but it still left readers too much room to treat any strong person-identification result as if it had measured one universal, state-invariant trait. The newer primary literature does not support that shortcut. <a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">Van De Ville et al. (2021)</a> showed that functional-connectivity fingerprints depend on timescale and that different network families dominate at different windows. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> showed that resting-state EEG individuality can stay robust over runs separated by weeks, but that result is still tied to a named PSD/coherence feature family and recording regime. <a href="https://doi.org/10.1016/j.neuroimage.2023.120260" target="_blank">Sorrentino et al. (2023)</a> then showed that the non-linear, intermittent part of MEG activity can carry more subject-specific information than stationary correlation structure. Finally, <a href="https://doi.org/10.1038/s41598-025-34509-y" target="_blank">Kyllönen et al. (2026)</a> showed across two-night sleep EEG from two sites that robust individual signatures can persist even when across-participant insomnia classification drops to chance. Therefore, on this site, <strong>trait-like backbone</strong> claims now need not only a temporal horizon but also an explicit <strong>backbone / fingerprint object</strong> and the <strong>state regime</strong> in which that object stayed stable.
</p>

<strong>2026-03-30 addendum: slow internal milieu is part of state annotation, not background noise</strong>
<p>
The remaining weakness after the fingerprint update was that this page could still make <strong>state annotation</strong> sound too close to movement, arousal, and day-night labels alone. The primary literature does not support that shortcut. <a href="https://doi.org/10.1038/29542" target="_blank">de Quervain et al. (1998)</a> showed glucocorticoid-dependent retrieval impairment, <a href="https://doi.org/10.1007/s11682-007-9003-2" target="_blank">Oei et al. (2007)</a> showed hydrocortisone-linked decreases in human hippocampal and prefrontal retrieval activity, <a href="https://doi.org/10.1016/j.celrep.2020.108255" target="_blank">McCauley et al. (2020)</a>, <a href="https://doi.org/10.1126/sciadv.adj1010" target="_blank">Barone et al. (2023)</a>, and <a href="https://doi.org/10.1073/pnas.2211996120" target="_blank">Birnie et al. (2023)</a> showed circadian and corticosteroid-rhythm control of hippocampal plasticity, and <a href="https://doi.org/10.1016/j.psyneuen.2004.04.003" target="_blank">Benedict et al. (2004)</a>, <a href="https://doi.org/10.3233/JAD-2008-13309" target="_blank">Reger et al. (2008)</a>, and <a href="https://doi.org/10.1016/j.neuropsychologia.2015.07.020" target="_blank">Sherman et al. (2015)</a> showed that insulin delivery or circadian-rhythm consistency can shift human memory or hippocampal activity. Therefore, on this site, the same task, same latency, or same decoder window does not imply the same hippocampal operating regime unless <strong>fast labels</strong> and <strong>slow internal-milieu labels</strong> were both disclosed.
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
<td>Arousal, spontaneous behavior, movement, task mode, day/night or within-day context, circadian phase, recent sleep-wake schedule, glucocorticoid or steroid exposure, feeding / fasting or glucose-insulin regime, medication or stimulation state, and any other state labels that can move performance.</td>
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

<strong>Extra disclosure when the paper uses trait / backbone / fingerprint language</strong>
<p>
The five temporal-validity fields remain necessary, but they are not sufficient when a result is described as a <strong>trait</strong>, <strong>backbone</strong>, or <strong>fingerprint</strong>. In those cases, this site additionally asks which feature family actually carries the longitudinal identity signal, such as dynamic functional connectivity, spectral profile, aperiodic component, avalanche-transition dynamics, or representational geometry, and whether that object was tested only within one regime or across a declared state change.
</p>

<strong>Fast labels and slow internal milieu are different audits</strong>
<p>
Movement, arousal, task mode, and setup explain one family of temporal failures. Circadian phase, steroid exposure, and feeding / insulin-metabolic regime explain another. On this site, both have to be logged when a result is promoted beyond a narrow same-task timing claim.
</p>

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
<td>The momentary or short-horizon condition: arousal, spontaneous behavior, movement, task engagement, sleep pressure, circadian phase, glucocorticoid or steroid exposure, feeding / insulin-metabolic state, pharmacological state, or time-of-day effects.</td>
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
It is too weak to treat same-day fluctuation as mere nuisance or to reduce state annotation to movement and arousal alone. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> showed that cortex-wide neural activity during task performance is strongly shaped by uninstructed movements, and <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a> showed that spontaneous behavior rapidly changes not only activity magnitude but also functional-connectivity structure. More specifically for EEG control, <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> showed that movement-related EEG dynamics vary across a 10-hour day/night window and that robust decoding therefore requires adaptive decoders.
</p>
<p>
But the same visible fast loop can also cross a slower body-state regime. <a href="https://doi.org/10.1038/29542" target="_blank">de Quervain et al. (1998)</a> showed glucocorticoid-dependent retrieval impairment, <a href="https://doi.org/10.1007/s11682-007-9003-2" target="_blank">Oei et al. (2007)</a> showed hydrocortisone-linked decreases in human hippocampal and prefrontal retrieval activity, <a href="https://doi.org/10.1016/j.celrep.2020.108255" target="_blank">McCauley et al. (2020)</a>, <a href="https://doi.org/10.1126/sciadv.adj1010" target="_blank">Barone et al. (2023)</a>, and <a href="https://doi.org/10.1073/pnas.2211996120" target="_blank">Birnie et al. (2023)</a> showed circadian and corticosteroid-rhythm control of hippocampal plasticity, and <a href="https://doi.org/10.1016/j.psyneuen.2004.04.003" target="_blank">Benedict et al. (2004)</a>, <a href="https://doi.org/10.3233/JAD-2008-13309" target="_blank">Reger et al. (2008)</a>, and <a href="https://doi.org/10.1016/j.neuropsychologia.2015.07.020" target="_blank">Sherman et al. (2015)</a> showed that insulin delivery or circadian-rhythm consistency can shift human memory or hippocampal activity. On this site, that means <strong>state annotation</strong> has to split <strong>fast labels</strong> from <strong>slow internal-milieu disclosure</strong>; otherwise a same-task result can still hide a different operating regime.
</p>

<h3>2. Trait-like backbone sits above unit-level immutability</h3>
<p>
The safer reading is not “a trait means one neuron stays fixed.” <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a> showed that aligned low-dimensional cortical dynamics can remain stable over long periods even when recorded neurons turn over. <a href="https://doi.org/10.1038/nn.4135" target="_blank">Finn et al. (2015)</a> showed that functional-connectivity patterns can identify individuals across scan sessions. At the same time, <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">Roth &amp; Merriam (2023)</a> showed cumulative representational drift in human V1 over months while relative dissimilarity structure remained more stable, and <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">Noda et al. (2025)</a> showed that a population-level representational map can recover within days after selective neuron loss. Therefore, this site now reads <strong>trait</strong> as a named backbone object, not as single-feature immutability.
</p>
<p>
However, the phrase <strong>functional fingerprint</strong> still hides an important remaining ambiguity: it does not yet say <strong>which object</strong> carried the identification. <a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">Van De Ville et al. (2021)</a> showed that the best functional-connectivity fingerprints emerge over longer windows while shorter windows can still contain highly identifiable snapshots, and that the dominant networks change across timescales. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">Di et al. (2021)</a> showed that resting-state EEG identity can remain robust over intervals of at least two weeks using spectral and coherence features. <a href="https://doi.org/10.1016/j.neuroimage.2023.120260" target="_blank">Sorrentino et al. (2023)</a> then showed in source-reconstructed MEG that subject differentiation can be driven mainly by fast, intermittent avalanche dynamics rather than the stationary component usually summarized by correlation structure. <a href="https://doi.org/10.1038/s41598-025-34509-y" target="_blank">Kyllönen et al. (2026)</a> finally showed that sleep EEG can preserve strong two-night individual signatures even when the nominal disorder label fails to generalize across participants, with high-frequency activity dominating the identity signal. Therefore, on this site, a <strong>trait-like backbone</strong> claim must name the <strong>backbone / fingerprint object</strong>, the <strong>timescale</strong>, and the <strong>state regime</strong> in which that object remained stable, rather than stopping at person-identification accuracy alone.
</p>

<h3>3. Stabilization and recalibration are not the same thing as fixed-decoder durability</h3>
<p>
Recent BCI papers sharpen this distinction. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a> showed that aligning latent dynamics can stabilize BCI decoding across long recordings, but that is still an <strong>alignment-based rescue strategy</strong>, not evidence that no drift occurred. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> then showed that long-term cursor BCI control can be maintained with unsupervised hidden-Markov-model recalibration, while also showing that the burden of recalibration and the choice of stabilization strategy matter. The site therefore now separates <strong>fixed decoder interval</strong> from <strong>recalibration burden</strong> and refuses to let “the system stayed usable” silently replace “the original decoder stayed valid.”
</p>

<h3>4. Invasive language BCIs split into four temporal routes</h3>
<p>
Communication-route papers are important, but their temporal claims are no longer one object. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>, <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> strengthen <strong>same-session throughput / expressivity</strong> under different output contracts. <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a> strengthens <strong>cross-subject transfer initialization</strong> from distributed brain recordings, which is useful for bootstrapping but still different from proving participant-invariant decoding or long-horizon no-update use. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a> and <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> instead strengthen <strong>adaptive rescue</strong> and <strong>unsupervised recalibration</strong> under accumulating neural change. On this site, a temporal-validity claim for invasive language BCIs therefore has to say which route it belongs to before the reader can decide whether the result supports throughput, initialization, bounded fixed-decoder use, or adaptive operation.
</p>
<table>
<thead>
<tr>
<th>Route type</th>
<th>Representative literature</th>
<th>What it supports</th>
<th>What it still does not support</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Throughput / expressivity</strong></td>
<td><a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>; <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a>; <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a></td>
<td>High-rate or low-latency communication under a declared output contract, vocabulary, and abstention / silence policy.</td>
<td>Cross-person portability, indefinite fixed-decoder validity, or participant-invariant language manifolds.</td>
</tr>
<tr>
<td><strong>Transfer initialization</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a></td>
<td>Bootstrapping a subject-specific decoder from distributed recordings rather than training from scratch on one participant alone.</td>
<td>Longitudinal durability without later updates, zero-calibration use, or a state-invariant backbone proven across participants.</td>
</tr>
<tr>
<td><strong>Bounded fixed-decoder slice</strong></td>
<td><a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>; <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a></td>
<td>A declared interval over which performance can be checked without new supervised retraining.</td>
<td>Indefinite decoder durability, cross-site portability, or solved neural drift.</td>
</tr>
<tr>
<td><strong>Adaptive rescue / recalibration</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz et al. (2025)</a>; <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a></td>
<td>Maintaining usable control by latent alignment or unsupervised updates under named drift conditions.</td>
<td>Evidence that the original decoder remained valid or that drift disappeared biologically.</td>
</tr>
</tbody>
</table>

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
<td>Arousal / behavior / movement / task-mode labels, and when relevant, time-of-day or sleep-pressure context plus circadian phase, recent sleep-wake schedule, glucocorticoid or steroid exposure, and feeding / fasting or glucose-insulin regime.</td>
<td>Same-day or cross-day differences cannot be read cleanly as trait or drift.</td>
</tr>
<tr>
<td><strong>backbone / fingerprint object</strong></td>
<td>Name whether the longitudinal object is latent dynamics, functional-connectivity fingerprint, EEG spectral profile, aperiodic component, avalanche-transition dynamics, representational geometry, or another explicit feature family, and state whether it was tested only within one regime or across a declared state change.</td>
<td>Identification success cannot be promoted to a stable, state-invariant trait or backbone.</td>
</tr>
<tr>
<td><strong>fixed decoder interval</strong></td>
<td>The exact days or sessions over which the same decoder was held without retraining.</td>
<td>No claim of fixed-decoder durability or stable backbone may be made.</td>
</tr>
<tr>
<td><strong>communication route type</strong></td>
<td>For invasive language or speech BCIs, state whether the result is same-session throughput / expressivity, transfer initialization, a bounded fixed-decoder slice, or adaptive rescue, and name any no-new-day-training, open-loop, or baseline-from-scratch comparator that defines that route.</td>
<td>A communication result cannot be promoted to generic transfer or long-horizon durability by default.</td>
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
<td>Without state annotation, same-day success can still ride on momentary behavior, arousal, setup conditions, or a different circadian / endocrine-metabolic regime.</td>
<td>Read as state-level evidence only.</td>
</tr>
<tr>
<td><strong>"High person-identification accuracy means one state-invariant trait was measured."</strong></td>
<td>Different timescales, feature families, and aperiodic or high-arousal components can carry strong identification without proving one universal backbone object.</td>
<td>Name the fingerprint object and regime first; otherwise read it as same-regime identifiability only.</td>
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
<td><strong>"Cross-subject transfer initialization means the decoder is participant-invariant or already durable."</strong></td>
<td>Initialization from other participants' data can lower the startup burden while still requiring subject-specific adaptation, later recalibration, or a bounded fixed-decoder interval.</td>
<td>Read as initialization evidence only unless later fixed-decoder or rescue evidence is shown explicitly.</td>
</tr>
<tr>
<td><strong>"The task and fast loop matched, so the biological regime matched."</strong></td>
<td>Circadian phase, glucocorticoid exposure, and insulin / metabolic regime can shift hippocampal retrieval or plasticity even when the visible loop looks unchanged.</td>
<td>Read as fast-loop or same-task evidence only unless slow internal-milieu disclosure is present.</td>
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
<li><strong>State annotation must split fast labels from slow internal milieu:</strong> movement, arousal, and task mode do not cover circadian phase, glucocorticoid exposure, or insulin-metabolic regime.</li>
<li><strong>Trait must name its backbone and fingerprint object:</strong> latent dynamics, representational geometry, functional-connectivity fingerprint, spectral profile, aperiodic component, avalanche-transition dynamics, or another explicit object.</li>
<li><strong>Person-identification is not enough by itself:</strong> say which object carried the identity signal, over which timescale, and whether it survived a declared state change or only same-regime repeats.</li>
<li><strong>Adaptive rescue must be visible:</strong> if alignment or recalibration was used, say so and report the cost.</li>
<li><strong>For invasive language BCIs, temporal route type must be named:</strong> throughput / expressivity, transfer initialization, bounded fixed-decoder slices, and adaptive rescue do not license the same claim.</li>
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
<li>Van De Ville D, Amico E, Abbas K, et al. When makes you unique: Temporality of the human brain fingerprint. <em>Science Advances</em>. 2021;7:eabj0751. <a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">doi:10.1126/sciadv.abj0751</a></li>
<li>Di X, Guo Z, Meng X, et al. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. <em>Frontiers in Human Neuroscience</em>. 2021;15:672946. <a href="https://doi.org/10.3389/fnhum.2021.672946" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>Sorrentino P, Troisi Lopez E, Romano A, et al. Brain fingerprint is based on the aperiodic, scale-free, neuronal activity. <em>NeuroImage</em>. 2023;277:120260. <a href="https://doi.org/10.1016/j.neuroimage.2023.120260" target="_blank">doi:10.1016/j.neuroimage.2023.120260</a></li>
<li>Roth ZN, Merriam EP. Representations in human primary visual cortex drift over time. <em>Nature Communications</em>. 2023;14:4422. <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">doi:10.1038/s41467-023-40144-w</a></li>
<li>Noda T, Kienle E, Eppler J-B, et al. Homeostasis of a representational map in the neocortex. <em>Nature Neuroscience</em>. 2025;28:1533-1545. <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">doi:10.1038/s41593-025-01982-7</a></li>
<li>Kyllönen M, Cox R, Makkonen T, et al. Trait-like individual signatures dominate sleep EEG over insomnia-specific features. <em>Scientific Reports</em>. 2026;16:4408. <a href="https://doi.org/10.1038/s41598-025-34509-y" target="_blank">doi:10.1038/s41598-025-34509-y</a></li>
<li>Karpowicz BM, O'Shea DJ, Wyche S, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. <em>Nature Communications</em>. 2025;16:3500. <a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">doi:10.1038/s41467-025-59652-y</a></li>
<li>Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Willett FR, Avansino DT, Hochberg LR, Henderson JM, Shenoy KV. A high-performance speech neuroprosthesis. <em>Nature</em>. 2023;620:1031-1036. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>. 2025;28:1318-1328. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>. 2025;644:145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Singh A, Thomas T, Li J, et al. Transfer learning via distributed brain recordings enables reliable speech decoding. <em>Nature Communications</em>. 2025;16:8749. <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">doi:10.1038/s41467-025-63825-0</a></li>
<li>de Quervain DJF, Roozendaal B, McGaugh JL. Stress and glucocorticoids impair retrieval of long-term spatial memory. <em>Nature</em>. 1998;394:787-790. <a href="https://doi.org/10.1038/29542" target="_blank">doi:10.1038/29542</a></li>
<li>Oei NYL, Elzinga BM, Wolf OT, de Ruiter MB, Damoiseaux JS, Kuijer JPA, Veltman DJ, Scheltens P, Rombouts SARB. Glucocorticoids decrease hippocampal and prefrontal activation during declarative memory retrieval in young men. <em>Brain Imaging and Behavior</em>. 2007;1:31-41. <a href="https://doi.org/10.1007/s11682-007-9003-2" target="_blank">doi:10.1007/s11682-007-9003-2</a></li>
<li>McCauley JP, Petroccione MA, D'Brant LY, et al. Circadian modulation of neurons and astrocytes controls synaptic plasticity in hippocampal area CA1. <em>Cell Reports</em>. 2020;33:108255. <a href="https://doi.org/10.1016/j.celrep.2020.108255" target="_blank">doi:10.1016/j.celrep.2020.108255</a></li>
<li>Barone I, Gillette NM, Hawks-Mayer H, et al. Synaptic BMAL1 phosphorylation controls circadian hippocampal plasticity. <em>Science Advances</em>. 2023;9:eadj1010. <a href="https://doi.org/10.1126/sciadv.adj1010" target="_blank">doi:10.1126/sciadv.adj1010</a></li>
<li>Birnie MT, Begum G, Sugden D, et al. Circadian regulation of hippocampal function is disrupted with corticosteroid treatment. <em>Proceedings of the National Academy of Sciences of the United States of America</em>. 2023;120:e2211996120. <a href="https://doi.org/10.1073/pnas.2211996120" target="_blank">doi:10.1073/pnas.2211996120</a></li>
<li>Benedict C, Hallschmid M, Hatke A, et al. Intranasal insulin improves memory in humans. <em>Psychoneuroendocrinology</em>. 2004;29:1326-1334. <a href="https://doi.org/10.1016/j.psyneuen.2004.04.003" target="_blank">doi:10.1016/j.psyneuen.2004.04.003</a></li>
<li>Reger MA, Watson GS, Green PS, et al. Intranasal insulin administration dose-dependently modulates verbal memory and plasma amyloid-beta in memory-impaired older adults. <em>Journal of Alzheimer's Disease</em>. 2008;13:323-331. <a href="https://doi.org/10.3233/JAD-2008-13309" target="_blank">doi:10.3233/JAD-2008-13309</a></li>
<li>Sherman SM, Mumford JA, Schnyer DM. Hippocampal activity mediates the relationship between circadian activity rhythms and memory in older adults. <em>Neuropsychologia</em>. 2015;75:617-625. <a href="https://doi.org/10.1016/j.neuropsychologia.2015.07.020" target="_blank">doi:10.1016/j.neuropsychologia.2015.07.020</a></li>
</ol>
