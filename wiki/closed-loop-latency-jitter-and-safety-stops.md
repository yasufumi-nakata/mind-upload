---
layout: default
title: "Wiki: Closed Loop, Delay, Jitter, Safe Stop"
description: "Delay, jitter, biomarker/controller family, fixed-decoder durability, recalibration burden, deployment eligibility, and the body/environment boundary are organized from primary literature for each type of closed loop."
article_type: Wiki
subtitle: "Closed-loop time requirements are not a single number; they vary by loop type"
author: Mind Uploading Research Project
last_updated: "2026-03-31"
note: "Learning guide / evidence refresh"
audience: "People who want to read about L3 closed-loop evaluation and real-time operation based on literature rather than general information"
reading_time: "14-22 minutes"
page_intro: "This page is a wiki that organizes delay, jitter, drift, safety stop, body/environment boundary, and long-horizon deployability in Mind-Upload's L3 'closed loop' using primary literature. The purpose is to clarify that even when offline accuracy is high, the required timing budget depends on the loop band and actuator, and low latency alone does not tell you which sensory, motor, interoceptive, reafferent, or slow internal-milieu routes were actually preserved, whether a fixed decoder survived across time, how much rescue-mode programming was needed, or, for burst-driven neuromodulation, which biomarker and controller were actually operating."
accuracy_note: "Here, we do not set a ``fixed threshold common to all loops.'' We also do not treat a fast loop as boundary-complete, temporally durable, or chronically deployable by default. Judgments are written on the premise that end-to-end timing indicators, retained/substituted body/environment routes, slow internal-milieu routes, fixed-decoder interval, co-adaptation regime, rescue-mode adaptation burden, deployment slices, and, for phase-targeting loops, oscillation estimability plus causal-versus-post-hoc targeting benchmarks, and, for burst-driven loops, biomarker family plus controller policy are disclosed explicitly."
page_highlights:
  - "Closed-loop time requirements vary by loop type, not by a single ms value."
  - "Low latency is not the same as reproducing the relevant body/environment boundary, because the fast loop and the slow internal milieu are different audits."
  - "A same-session fast loop, a fixed decoder that survives across days, an adaptively rescued loop, and a chronically deployable loop are different achievements."
  - "Online improvement is not one object: user-side learning, decoder updates, and application-side shaping must be separated before gains are read as stability."
  - "Even if the event marker is less than 1 ms, it is a different matter from guaranteeing end-to-end for the entire system."
  - "Phase error is more important than ms for phase-targeting, and for adaptive DBS the timing story now has to be separated from fixed-decoder durability, programming burden, and eligibility."
  - "For phase-targeted stimulation, low mean latency is still not enough: oscillation presence / power / SNR gate, causal estimator benchmark, circular targeting error, and no-stim / missed-trigger rates must be separated."
  - "For burst-driven neuromodulation, the main question is no longer burst timing alone: biomarker family, controller mode, movement / medication state, sensing compatibility, and biomarker-linked comparator have to be separated."
  - "Streaming speech BCI needs to record not only average delay but also tail latency, output-path audit, silence/hold-last-output, and fixed-decoder horizon in separate logs."
  - "Adaptive-DBS papers need to log rescue-mode optimization, clinic/home transfer, eligibility, continuation, and biomarker/controller choice separately from symptom benefit."
known_points:
  - "Offline accuracy and closed-loop stability are separate claims and cannot be audited with the same score."
  - "Even a fast loop can remain boundary-incomplete if self-motion, predicted reafference, tactile feedback, respiration, arousal, circadian phase, glucocorticoid state, insulin / metabolic regime, or other subject-defining routes stay omitted or undisclosed."
  - "Latency and jitter tolerances vary for state feedback, ERP/command BCI, streaming communication, phase-locked stimulation, and burst-driven neuromodulation."
  - "Unless you actually measure input, processing, output, and return end-to-end, you won't know the timing of actual operation."
  - "Closed-loop gains can come from co-adaptation of the user, decoder, and application rather than from a stable fixed decoder alone."
  - "Fixed-decoder durability and rescue-mode recalibration are separate evidence objects; one can fail while the other still rescues behavior."
  - "Reliable phase locking is not the same as a reliable physiological or behavioral effect, and neither one fixes a stable optimal phase across sessions."
  - "Burst-driven neuromodulation is not one controller family: beta power, beta burst duration, entrained gamma, dyskinesia-linked narrowband gamma, and movement-responsive decoder policies do not constrain the same symptom axis or operate on the same timescale."
  - "Subthalamic beta is modulated by movement, dopaminergic medication, and stimulation itself, so a beta feedback signal tuned in one regime is not automatically valid in another."
  - "Speed-up within-session alone is not enough; it also leaves fixed-decoder horizon, recalibration burden, clinic/home transition, and programming burden."
  - "Chronic adaptive-DBS symptom benefit, eligibility, and long-run continuation are different axes and should not be collapsed into one deployment verdict."
unknown_points:
  - "It is unclear how far the closed-loop bandwidth required for WBE spans which loop types."
  - "It is not yet possible to generalize the precision required for phase-specific control to all tasks in non-invasive human experiments."
  - "It is not yet fixed which biomarker/controller pairing best generalizes across bradykinesia, gait impairment, dyskinesia control, and chronic home use in adaptive DBS."
  - "What counts as an acceptable fixed-decoder horizon before rescue-mode adaptation becomes a different operating regime still depends on task and modality."
  - "How fast or slow co-adaptation should be to help the user without hiding instability still depends on loop type, modality, and task."
  - "How a phase-targeting protocol should adapt when the optimal phase drifts within-session or across sessions still depends on band, task, and subject."
  - "How burst-driven loops should adapt when biomarker controllability changes with movement, medication cycle, contact choice, or artifact remains unsettled."
  - "What is considered 'unstable' or 'impractical' in terms of drift, recalibration frequency, eligibility, continuation, and programming burden during long-term operation depends on the task."
wiki_links:
  - label: "Wiki: Event synchronization and observation log"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "Compensates for delay, jitter, and drift."
  - label: "Wiki: Uncertainty, proofreading, abstaining"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "Complements the design concept of 'not releasing' when reliability is low."
  - label: "Wiki: State, trait, and drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Separates same-session success from cross-day durability and rescue-mode adaptation."
  - label: "Wiki: Update/branch/stop rules"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "Complements how to separate freeze and stop rules as operations."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "You can return to other auxiliary pages."
recommended_pages:
  - label: "Verification base"
    url: "/verification.html"
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest conclusion</h2>
<p>
A <strong>closed loop</strong> is a system in which the output changes the next input. However, there is more than one timing required. The dominant time scales and breakdown methods are different for<strong>alpha neurofeedback</strong>,<strong>P300/ERP BCI</strong>,<strong>streaming speech neuroprosthesis</strong>,<strong>phase-locked stimulation</strong>, and<strong>adaptive DBS</strong>. Therefore, it is dangerous to place a <strong>common 1 ms threshold</strong> or <strong>common 10 ms threshold</strong> as the correct answer for the whole site.
</p>
</div>

<div class="note-box">
<strong>What was fixed first in this organization</strong>
<p>
On this page, instead of talking about "how fast is enough" in an abstract way, we first fix <strong>which loop type we are dealing with</strong>, <strong>what is the delay that breaks in the loop</strong>, and <strong>what was actually measured with hardware</strong>. Event marker acceleration, LSL synchronization, phase tracking, and stopping rules are separate layers.
</p>
</div>

<div class="note-box">
<strong>Timing audit is not the whole loop audit</strong>
<p>
This page now keeps <strong>timing logs</strong> separate from <strong>body/environment boundary logs</strong>. A loop can be fast and still remain boundary-incomplete if the paper does not say which sensory, action, interoceptive, self-generated-feedback, and slow internal-milieu routes were preserved, substituted, matched, perturbed, or omitted. On this site, low latency without that disclosure does not rise above a task-specific local controller or surrogate-body result.
</p>
</div>

<div class="note-box">
<strong>Three public cards are stacked here, not one timing score</strong>
<p>
On this site, once a closed-loop claim leaves the narrow same-session timing question, it has to stack the <a href="../verification.html#temporal-validity-card">Verification: Temporal Validity Card</a> with the <a href="../verification.html#body-environment-boundary-card">Verification: Body / Environment Boundary Card</a>, and add the <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> whenever silence, abstention, or fallback behavior matters. A fast loop without those companion cards stays a bounded local-controller result.
</p>
</div>

<div class="note-box">
<strong>2026-03-28 re-audit: co-adaptation is a separate evidence wall</strong>
<p>
The remaining blind spot was that the page could still let readers treat <strong>any online improvement</strong> as if it primarily reflected timing quality or long-horizon stability. The primary literature does not support that compression. <a href="https://doi.org/10.1016/j.neuron.2014.04.048" target="_blank">Orsborn et al. (2014)</a> showed that combined neural and decoder adaptation can itself shape neural representations. <a href="https://doi.org/10.1371/journal.pbio.2003787" target="_blank">Perdikis et al. (2018)</a> and <a href="https://doi.org/10.3389/fnhum.2019.00362" target="_blank">Abu-Rmileh et al. (2019)</a> showed that user learning and classifier adaptation evolve on different timescales in longitudinal EEG BCIs, and that adaptation that is too frequent can hinder subject learning. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> and <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> then showed that modern speech and cursor loops still rely on per-session retraining, blockwise decoder updates, and explicit open-loop probes to estimate performance without closed-loop correction. Therefore, this site now treats <strong>co-adaptation / credit assignment</strong> as a separate wall rather than hiding it inside latency or recalibration.
</p>
</div>
<div class="note-box">
<strong>2026-03-28 second re-audit: phase-targeting needs an estimability wall</strong>
<p>
One more shortcut remained. The page still allowed a reader to think that once a phase-targeted loop reports <strong>low latency</strong> and some <strong>phase error distribution</strong>, the main technical burden is already satisfied. The primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">Zrenner et al. (2020)</a> showed that meaningful phase estimation itself degrades when oscillatory amplitude and SNR are low. <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">Gordon et al. (2021)</a> then showed that prefrontal theta targeting required extra constraints to avoid low-amplitude and phase-reset epochs. <a href="https://doi.org/10.1111/ejn.14931" target="_blank">Vigué-Guix et al. (2022)</a> achieved reliable trial-to-trial alpha phase locking yet did not obtain a consistent behavioral benefit, which means targeting success and functional effect must be kept separate. <a href="https://doi.org/10.1523/ENEURO.0050-23.2023" target="_blank">Kim et al. (2023)</a> showed across 11 public datasets that higher power and SNR improve prediction accuracy and that waiting for eligible epochs matters more than forcing one cognitive state. Finally, <a href="https://doi.org/10.1016/j.brs.2025.09.019" target="_blank">Hougland et al. (2025)</a> showed within-session fluctuations and low test-retest reliability of the optimal mu-phase. Therefore, phase-targeted stimulation on this site is now read through an <strong>estimability / targeting / effect / stability stack</strong>, not one timing number.
</p>
</div>
<div class="note-box">
<strong>2026-03-31 re-audit: burst-driven neuromodulation needs a controller wall too</strong>
<p>
Another shortcut remained on the adaptive-DBS side. The page still let a reader treat <strong>burst timing</strong> or <strong>beta-trigger latency</strong> as if that were the main technical burden once phase-targeting had already been split more carefully. The newer primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">Mathiopoulou et al. (2024)</a> showed that subthalamic beta is modulated differently by movement, medication, and stimulation. <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> showed that single-threshold and dual-threshold aDBS are different control modes with different timescales and therapeutic goals. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a>, <a href="https://doi.org/10.1093/brain/awae004" target="_blank">Olaru et al. (2024)</a>, and <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">Mathiopoulou et al. (2025)</a> then showed that <strong>entrained gamma</strong>, <strong>dyskinesia-linked narrowband gamma</strong>, and <strong>personalized high-versus-low dopaminergic-state markers</strong> do not constrain the same symptom axis. <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Busch et al. (2025)</a> and <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a> further showed that sensing compatibility, threshold setting, signal artifacts, and patient eligibility remain concrete bottlenecks. Therefore, burst-driven neuromodulation on this site is now read through a <strong>biomarker / controller / delivery / effect / deployability stack</strong>, not one burst-timing story.
</p>
</div>

<section class="section" id="why-fixed-threshold-is-dangerous">
<h2 class="section-title">Why fixed thresholds are dangerous</h2>
<p>
Wilson et al. (2010) showed that for relatively slow BCI indicators such as mu rhythm amplitude, a small delay of about 10 ms does not necessarily destroy the essence, but if the latency/jitter of the entire system is not measured, the output path and display become rate-limiting. Conversely, Belinskaia et al. (2020) showed that with parietal alpha neurofeedback, an<strong>additional 250 ms / 500 ms delay</strong> worsened the learning effect. Furthermore, in phase-targeting systems such as Mansouri et al. (2018) and Zrenner et al. (2018), the delay should be evaluated as<strong>the phase error relative to the frequency of interest</strong>and not simply as a ms value.
</p>
<div class="note-box">
<strong>Reading principles</strong>
<p>
"Low latency is good" is generally correct, but it cannot immediately be said that "microsecond-level delay is required for all loops" or "1 ms or less is required for all loops." The correct question is<strong>in what loop band, what error breaks what</strong>.
</p>
</div>
<div class="note-box">
<strong>If you want the row-level route</strong>
<p>
If you want the one-row operational packet that turns this principle into a public-safe route, continue with the <a href="u8-1-closed-loop-delay-tolerance-route.html">U8-1 closed-loop delay-tolerance route packet</a>. That packet keeps the question at the level of one named loop class, one KPI bundle, and one downgrade rule rather than a universal latency threshold.
</p>
</div>
</section>

<section class="section" id="boundary-before-latency">
<h2 class="section-title">Before milliseconds, fix which loop boundary was actually preserved</h2>
<p>
The weakness of the older timing-only reading was that it could still let a reader say, <strong>"the loop was fast, therefore the closed-loop problem is close to solved."</strong> That is too weak. Primary literature shows that sensory cortex and higher-order dynamics are continuously reshaped by self-motion, predicted sensory consequences, multisensory navigation cues, respiration, arousal, tactile feedback, circadian timing, glucocorticoid exposure, and metabolic state. Therefore, a low-latency controller is not automatically a boundary-complete controller.
</p>
<table class="data-table">
<thead>
<tr>
<th>Boundary component</th>
<th>What primary literature shows</th>
<th>Why timing alone is insufficient</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>self-motion / optic flow / proprioceptive coupling</strong></td>
<td><a href="https://doi.org/10.1038/nn.3567" target="_blank">Saleem et al. (2013)</a> showed that V1 neurons combine visual speed with run speed during navigation.</td>
<td>A fast visual loop still differs from the biological loop if locomotion- and proprioception-linked inputs were absent, simulated, or silently simplified.</td>
</tr>
<tr>
<td><strong>predicted reafference / sensorimotor mismatch</strong></td>
<td><a href="https://doi.org/10.1016/j.neuron.2012.03.040" target="_blank">Keller et al. (2012)</a> showed mismatch-sensitive responses in behaving-mouse V1, supporting the idea that expected sensory feedback matters beyond passive stimulation.</td>
<td>The loop is not characterized only by delay; it also depends on whether self-generated sensory consequences and mismatch signals were available at all.</td>
</tr>
<tr>
<td><strong>vestibular and multisensory navigation cues</strong></td>
<td><a href="https://doi.org/10.1126/science.1232655" target="_blank">Ravassard et al. (2013)</a> showed that removing real-world multisensory cues changes hippocampal spatiotemporal selectivity in virtual reality.</td>
<td>A low-latency virtual loop can still be a different loop class if vestibular and other navigation cues were missing or remapped.</td>
</tr>
<tr>
<td><strong>corollary discharge of self-generated sensory consequences</strong></td>
<td><a href="https://doi.org/10.1038/nature13724" target="_blank">Schneider et al. (2014)</a> showed a motor-to-auditory cortical circuit that suppresses sensory responses during movement.</td>
<td>If a system does not disclose whether corollary-discharge-like routes or self-generated sensory predictions were preserved, timing alone cannot tell you whether the sensory loop is comparable.</td>
</tr>
<tr>
<td><strong>respiration / arousal / organism-wide physiology</strong></td>
<td><a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">Zelano et al. (2016)</a> showed nasal-respiration coupling to human limbic oscillations, and <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">Raut et al. (2025)</a> showed that neural activity, physiology, and behavior share a structured arousal manifold.</td>
<td>A brain-only fast controller can still omit organism-wide state variables that co-organize the loop in vivo.</td>
</tr>
<tr>
<td><strong>slow endocrine / circadian / metabolic milieu</strong></td>
<td><a href="https://doi.org/10.1038/29542" target="_blank">de Quervain et al. (1998)</a> showed glucocorticoid-dependent memory-retrieval impairment, <a href="https://doi.org/10.1007/s11682-007-9003-2" target="_blank">Oei et al. (2007)</a> showed hydrocortisone-linked decreases in human hippocampal and prefrontal retrieval activity, <a href="https://doi.org/10.1016/j.celrep.2020.108255" target="_blank">McCauley et al. (2020)</a> plus <a href="https://doi.org/10.1126/sciadv.adj1010" target="_blank">Barone et al. (2023)</a> showed circadian gating of hippocampal plasticity, and <a href="https://doi.org/10.1073/pnas.2211996120" target="_blank">Birnie et al. (2023)</a>, <a href="https://doi.org/10.1016/j.psyneuen.2004.04.003" target="_blank">Benedict et al. (2004)</a>, <a href="https://doi.org/10.3233/JAD-2008-13309" target="_blank">Reger et al. (2008)</a>, and <a href="https://doi.org/10.1016/j.neuropsychologia.2015.07.020" target="_blank">Sherman et al. (2015)</a> showed that corticosteroid rhythm, insulin signaling, and circadian-rhythm consistency can shift hippocampal plasticity, human memory, or hippocampal activity.</td>
<td>The same visible input-output loop can still be a different biological loop class if clock phase, steroid state, or feeding / insulin regime were unmatched or left latent.</td>
</tr>
<tr>
<td><strong>tactile contact feedback</strong></td>
<td><a href="https://doi.org/10.1126/science.abd0380" target="_blank">Flesher et al. (2021)</a> showed that adding tactile feedback improves robotic-arm control in a bidirectional BCI.</td>
<td>The main issue is not only whether the loop is fast, but which feedback channels were restored and which still remained absent.</td>
</tr>
<tr>
<td><strong>movement-linked latent structure</strong></td>
<td><a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> and <a href="https://doi.org/10.1126/science.aav7893" target="_blank">Stringer et al. (2019)</a> showed that ongoing behavior explains a large fraction of cortical and brainwide neural variance.</td>
<td>Without a boundary card, a fast controller can overfit a narrow behavioral contract while still being read as a general closed-loop success.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Operating rule on this site</strong>
<p>
If the paper does not disclose which sensory, action, interoceptive, self-generated-feedback, and slow internal-milieu routes were retained, substituted, matched, perturbed, or omitted, this site does not promote the result from <strong>fast local loop</strong> to <strong>boundary-complete L3 evidence</strong>. The formal public rule is the <a href="../verification.html#body-environment-boundary-card">Verification: Body / Environment Boundary Card</a>; this wiki supplies the timing-side companion logic.
</p>
</div>
</section>

<section class="section" id="loop-classes">
<h2 class="section-title">First, divide into 5 loop types</h2>
<table class="data-table">
<thead>
<tr>
<th>Loop type</th>
<th>Typical example</th>
<th>What the literature shows</th>
<th>Logs that should be left first on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state feedback / neurofeedback</strong></td>
<td>alpha This is a system that looks at the power and gives visual feedback. </td>
<td>Belinskaia et al. (2020) showed that an additional 250/500 ms delay worsens alpha neurofeedback learning. Shorter delays were more beneficial for learning. </td>
<td>Performance degradation curves for median/P95/P99 feedback latency, display path, and additional delay. </td>
</tr>
<tr>
<td><strong>ERP / command BCI</strong></td>
<td>P300 speller or event-related control. </td>
<td>Wilson et al. (2010) showed that it is necessary to decompose timing and measure hardware, and Mowla et al. (2017) showed that latency jitter lowers classification, so even if it is corrected, the negative effects cannot be completely eliminated. </td>
<td>Correspondence with block jitter, stimulus onset measurement, trial-to-trial latency variance, and classification performance. </td>
</tr>
<tr>
<td><strong>streaming communication / speech neuroprosthesis</strong></td>
<td>It is a system that continuously returns brain-to-text or brain-to-voice as audio or text. </td>
<td>Littlejohn et al. (2025) demonstrated streaming brain-to-voice in 80 ms increments, and Wairagkar et al. (2025) demonstrated a loop that returns speech synthesis from raw neural input in less than 10 ms while returning silence for non-speech and overlapping speech. The key metrics here are not only average latency, but also tail latency, audio output path, and silence/abstention. </td>
<td>per-step inference latency, cue-to-output latency distribution, audio driver latency, silence / false-speech rate, dropout, recalibration event. </td>
</tr>
<tr>
<td><strong>phase-locked stimulation</strong></td>
<td>This is a system that delivers TMS/tES in accordance with the EEG phase. </td>
<td>Mansouri et al. (2018) and Zrenner et al. (2018) demonstrated real-time phase targeting, but Zrenner et al. (2020), Gordon et al. (2021), Kim et al. (2023), and Hougland et al. (2025) show that the real bottleneck is not latency alone but whether the oscillation is estimable now, how the causal estimate is benchmarked, and whether the optimal phase is stable. </td>
<td>Target band and spatial filter, power/SNR gate, no-stim rate, causal-versus-post-hoc benchmark, mean phase offset / circular spread, missed trigger, and any fixed-versus-adaptive phase policy. </td>
</tr>
<tr>
<td><strong>burst/state-triggered neuromodulation</strong></td>
<td>Adaptive DBS using beta burst. </td>
<td>Little et al. (2013) and Tinkhauser et al. (2017) established beta-based feedback, but Mathiopoulou et al. (2024), Stanslaski et al. (2024), Oehrn et al. (2024), Olaru et al. (2024), Busch et al. (2025), Mathiopoulou et al. (2025), and Cascino et al. (2026) show that the main burden is no longer burst timing alone but <strong>which biomarker is being controlled</strong>, <strong>which controller mode is used</strong>, and <strong>whether sensing and programming remain viable</strong>. </td>
<td>biomarker family / symptom target, sensing contacts / signal-to-noise, controller mode, update interval / onset duration / ramp policy, false positive/negative, artifact-triggered resets, comparator condition, and rescue/programming burden. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="phase-targeting-wall">
<h2 class="section-title">Phase-targeting is estimability-limited, not latency-limited</h2>
<p>
The older wording on this page already separated <strong>phase error</strong> from plain milliseconds. That was necessary, but it was not yet sufficient. Current primary literature shows that a phase-targeted loop can fail for at least five different reasons: the target oscillation may not be estimable in the current epoch, the causal estimator may not match the post-hoc benchmark, the circular targeting precision may be too weak, the loop may phase-lock without producing a reliable physiological or behavioral effect, or the best phase may drift within and across sessions. Therefore, this site now reads phase-targeted stimulation through the following stack rather than a single timing figure.
</p>
<table class="data-table">
<thead>
<tr>
<th>Layer to separate</th>
<th>What the primary literature supports</th>
<th>What must be logged</th>
<th>What it still does not prove</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>oscillation gate / estimability</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">Zrenner et al. (2020)</a> showed that phase estimability worsens when oscillatory amplitude and SNR are low, <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">Gordon et al. (2021)</a> improved prefrontal theta targeting by excluding low-theta and phase-reset epochs, and <a href="https://doi.org/10.1523/ENEURO.0050-23.2023" target="_blank">Kim et al. (2023)</a> showed across 11 public datasets that high power and SNR are the main practical conditions for better phase prediction.</td>
<td>Target band, channel or spatial filter, spectral peak criterion, amplitude/SNR threshold, no-stim or wait rate, and any phase-reset rejection rule.</td>
<td>That the loop really stimulated the intended phase in every eligible epoch, or that a functional effect followed.</td>
</tr>
<tr>
<td><strong>causal estimator benchmark</strong></td>
<td><a href="https://doi.org/10.3389/fnins.2018.00877" target="_blank">Mansouri et al. (2018)</a> and <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> made real-time phase-triggering feasible, while <a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">Zrenner et al. (2020)</a> and <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">Gordon et al. (2021)</a> showed why the causal estimate has to be benchmarked against a non-causal or post-hoc phase estimate under the same signal class.</td>
<td>Causal algorithm family, training window, forecast horizon, artifact blanking rule, post-hoc benchmark procedure, and whether the benchmark was run on non-stimulated or artifact-free matched epochs.</td>
<td>That the chosen causal estimator is uniquely best, or that the phase effect is biologically meaningful.</td>
</tr>
<tr>
<td><strong>targeting precision</strong></td>
<td><a href="https://doi.org/10.1016/j.jneumeth.2021.109288" target="_blank">Bruegger &amp; Abegg (2021)</a> compared methods using mean phase offset, circular standard deviation, and prediction latency, and <a href="https://doi.org/10.1523/JNEUROSCI.1913-18.2018" target="_blank">Holt et al. (2019)</a> showed that narrower phase bins and repeated phase-consistent pulses materially change effect size.</td>
<td>Mean phase offset, circular spread or equivalent circular error metric, phase-locking statistic at trigger, missed-trigger rate, and any phase-bin width or consecutive-cycle rule.</td>
<td>That the targeted phase is the most effective phase for the claimed physiological or behavioral endpoint.</td>
</tr>
<tr>
<td><strong>functional effect versus targeting success</strong></td>
<td><a href="https://doi.org/10.1111/ejn.14931" target="_blank">Vigué-Guix et al. (2022)</a> achieved reliable trial-to-trial alpha phase locking in a real-time BCI yet found no consistent reaction-time modulation, showing that accurate targeting and useful behavioral control are different evidence objects.</td>
<td>Off-target or random-phase comparator, sham or surrogate comparator when available, effect-size distribution for the downstream endpoint, and the stopped claim if targeting succeeded but the endpoint did not.</td>
<td>That a phase-targeted loop improves cognition, therapy, or plasticity simply because phase locking worked.</td>
</tr>
<tr>
<td><strong>phase stability and adaptation policy</strong></td>
<td><a href="https://doi.org/10.1016/j.brs.2025.09.019" target="_blank">Hougland et al. (2025)</a> showed within-session fluctuations and low test-retest reliability of the optimal mu-phase, which limits the generalizability of fixed-phase targeting across sessions.</td>
<td>Whether the preferred phase was fixed or updated, within-session drift audit, across-session reliability, retuning trigger, and whether adaptation changes the claim from fixed-policy targeting to adaptive targeting.</td>
<td>That one fixed phase generalizes across people, sessions, or task states without re-validation.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Revision rule on this site</strong>
<p>
If a phase-targeted loop reports only milliseconds or only a single average phase error, this page does not promote it to validated phase-specific control. The minimum readable object is a <strong>declared target band with an estimability gate</strong>, a <strong>causal-versus-post-hoc benchmark</strong>, <strong>circular targeting metrics</strong>, a <strong>functional comparator</strong>, and a <strong>fixed-versus-adaptive phase policy</strong>.
</p>
</div>
</section>

<section class="section" id="burst-controller-wall">
<h2 class="section-title">Burst-driven neuromodulation is controller-limited, not just burst-timed</h2>
<p>
The older wording on this page already said that burst-triggered neuromodulation is slower than phase-locking. That was directionally correct, but it was still too coarse. Current primary literature shows that an adaptive-DBS loop can fail or change meaning for at least five different reasons: the chosen biomarker may track a different symptom axis, the biomarker may be modulated by movement / medication / stimulation state, the controller law may operate on a different timescale, sensing contacts and artifacts may constrain whether the loop can even run, and a biomarker-linked control signal may still fail to show unique clinical superiority over an energy-matched comparator. Therefore, this site now reads burst-driven neuromodulation through the following stack rather than a single burst-timing figure.
</p>
<table class="data-table">
<thead>
<tr>
<th>Layer to separate</th>
<th>What the primary literature supports</th>
<th>What must be logged</th>
<th>What it still does not prove</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>biomarker family / symptom target</strong></td>
<td><a href="https://doi.org/10.1002/ana.23951" target="_blank">Little et al. (2013)</a> and <a href="https://doi.org/10.1093/brain/awx010" target="_blank">Tinkhauser et al. (2017)</a> constrain a <strong>beta-burst antikinetic route</strong>, <a href="https://doi.org/10.1093/brain/awae004" target="_blank">Olaru et al. (2024)</a> constrains a <strong>dyskinesia-linked narrowband-gamma route</strong>, <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a> used <strong>personalized high-versus-low dopaminergic-state markers</strong>, and <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">Mathiopoulou et al. (2025)</a> constrains <strong>entrained gamma as a prokinetic biomarker candidate</strong>. Those are not the same control object.</td>
<td>Signal family, frequency band, anatomical source, intended symptom axis, and whether the signal is read as antikinetic beta, dyskinesia-linked gamma, entrained prokinetic gamma, or another personalized state marker.</td>
<td>That one adaptive-DBS signal generalizes across bradykinesia, gait impairment, dyskinesia, and medication-state control.</td>
</tr>
<tr>
<td><strong>state dependence / controllability</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">Mathiopoulou et al. (2024)</a> showed that movement, dopaminergic medication, and DBS each modulate subthalamic beta differently, while <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Busch et al. (2025)</a> documented that useful beta-threshold setting depends on patient-specific long-term modulation and can be misread by in-clinic snapshots alone.</td>
<td>Medication state, rest versus movement slices, controllability test of the candidate signal, band-width or peak-selection rule, and whether thresholds were derived from clinic-only or chronic home data.</td>
<td>That a signal tuned at rest or in one medication state stays equally informative during naturalistic behavior.</td>
</tr>
<tr>
<td><strong>controller mode / timescale</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> showed that ADAPT-PD uses <strong>single-threshold</strong> control with <strong>250 ms</strong> amplitude changes and <strong>dual-threshold</strong> control with <strong>2.5 min up / 5 min down</strong> adjustment plus a programmable <strong>1.2–2 s onset</strong>, while <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/" target="_blank">Wilkins et al. (2025)</a> used a <strong>beta-burst-duration controller</strong> with a therapeutic floor, ceiling, and slow ramp policy for gait / freezing-of-gait.</td>
<td>Controller family, single- versus dual-threshold or other policy class, update interval, onset duration, floor/ceiling amplitude, ramp rate, and whether one or both hemispheres drive the control law.</td>
<td>That two aDBS papers used the same control strategy simply because both were called adaptive or beta-based.</td>
</tr>
<tr>
<td><strong>sensing compatibility / artifact burden</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> reported that participants could exit ADAPT-PD because of <strong>signal artifact</strong>, inadequate LFP signal, or no acceptable aDBS mode, and <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Busch et al. (2025)</a> showed no visible beta peak in <strong>3/16 hemispheres</strong>, unilateral sensing in <strong>4/8 patients</strong>, threshold drift, and outlier distortion during setup. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/" target="_blank">Wilkins et al. (2025)</a> likewise required sense-friendly configurations and slower ramps to reduce stimulation artefacts.</td>
<td>Sensing contacts, signal-to-noise, unilateral versus bilateral sensing, excluded hemispheres, artifact-detection rule, threshold reset events, and whether the signal remained usable during movement and stimulation.</td>
<td>That the controller would have been available under ordinary contact settings or chronic use without extra debugging and exclusions.</td>
</tr>
<tr>
<td><strong>biomarker-linked control versus clinical effect</strong></td>
<td><a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a> showed improved motor symptoms and quality of life with personalized adaptive DBS in a four-patient pilot, but <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/" target="_blank">Wilkins et al. (2025)</a> found that a <strong>randomly adapting</strong> DBS control with matched therapeutic window and TEED still performed similarly to cDBS and aDBS at group level on several acute metrics, which means biomarker linkage and clinical superiority are separate evidence objects.</td>
<td>cDBS comparator, random / inverted / surrogate comparator when available, TEED or duty-cycle matching rule, chosen symptom endpoint, and the stopped claim when the biomarker tracks a state but does not show unique clinical benefit.</td>
<td>That better biomarker tracking or a cleaner controller trace automatically produced unique symptom-level superiority.</td>
</tr>
<tr>
<td><strong>deployability / programming burden</strong></td>
<td><a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Busch et al. (2025)</a>, <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a>, and <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Dixon et al. (2026)</a> show that home use still depends on programming workflow, remote or manual rescue, eligibility, and continuation. In ADAPT-START, only <strong>9 of 20</strong> consecutive chronic cDBS patients were eligible and <strong>5</strong> remained on chronic aDBS by July 2025.</td>
<td>Screened n, exclusion reasons, programming visits, remote or manual optimization route, home slice, continuation, and the manpower / time burden of maintaining the controller.</td>
<td>That a controller with an interesting biomarker is already routine, broadly eligible, or low-burden clinical care.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Revision rule on this site</strong>
<p>
If a burst-driven loop reports only burst duration or only one average timing number, this page does not promote it to validated symptom-linked adaptive control. The minimum readable object is a <strong>named biomarker family and symptom target</strong>, a <strong>state-dependence / controllability audit</strong>, a <strong>declared controller mode with timescale</strong>, a <strong>sensing / artifact burden audit</strong>, a <strong>biomarker-linked comparator</strong>, and a <strong>deployment slice</strong>.
</p>
</div>
</section>

<section class="section" id="co-adaptation-wall">
<h2 class="section-title">Co-adaptation must be separated before online gains are interpreted</h2>
<p>
A remaining weakness at the L3 entry point was that "online performance improved" could still be read as if the same decoder had simply become more durable. Current primary literature does not support that shortcut. In closed-loop BCIs, improvement can come from <strong>user-side neural strategy learning</strong>, <strong>decoder-weight updates or pseudo-label self-training</strong>, and <strong>application / interaction redesign</strong>. If these are mixed, a fast loop is not yet evidence of a stable fixed decoder.
</p>
<table class="data-table">
<thead>
<tr>
<th>Source of apparent improvement</th>
<th>What the primary literature supports</th>
<th>What must be logged</th>
<th>What it still does not prove</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>user-side learning</strong></td>
<td><a href="https://doi.org/10.3389/fnhum.2019.00362" target="_blank">Abu-Rmileh et al. (2019)</a> compared a fixed classifier against regular adaptation over four days and showed different within-day versus between-day behaviour, while <a href="https://doi.org/10.1371/journal.pbio.2003787" target="_blank">Perdikis et al. (2018)</a> showed longitudinal subject learning and warned that frequent recalibration can hinder it.</td>
<td>Fixed versus updated decoder schedule, practice dose, instruction changes, and within-day versus between-day curves.</td>
<td>That the decoder itself was stable, or that gains will survive with no update.</td>
</tr>
<tr>
<td><strong>decoder-side adaptation</strong></td>
<td><a href="https://doi.org/10.1016/j.neuron.2014.04.048" target="_blank">Orsborn et al. (2014)</a> showed that combined neural and decoder adaptation can yield skillful control while reshaping neural representations, and <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> updated decoder weights after each closed-loop block while using open-loop probes to estimate performance without closed-loop effects.</td>
<td>Update trigger, cadence, pseudo-label or supervision route, open-loop probe blocks, and frozen-comparator performance.</td>
<td>That online gains came from a fixed decoder, or that they reflect user learning alone.</td>
</tr>
<tr>
<td><strong>application / interaction shaping</strong></td>
<td><a href="https://doi.org/10.1371/journal.pbio.2003787" target="_blank">Perdikis et al. (2018)</a> showed that control-paradigm refinement can facilitate subject learning, while <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> reported that participant engagement and enunciation influenced synthesis quality and retrained the decoder using previous-session data.</td>
<td>Feedback policy, smoothing or evidence-accumulation rules, prompt or task scaffold, session-to-session interface changes, and engagement / fatigue notes.</td>
<td>That the neural controller alone improved independent of interface or task redesign.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Revision rule on this site</strong>
<p>
A same-session online result must now name whether it is a <strong>fixed-policy loop</strong> or a <strong>co-adaptive loop</strong>. If the paper mixes user learning, decoder updates, and interface redesign without a frozen comparator or open-loop probe, this site does not promote the gain to fixed-decoder durability or portable deployment evidence.
</p>
</div>
</section>

<section class="section" id="longitudinal-bottlenecks">
<h2 class="section-title">2026-03 literature audit: five barriers that appear once a loop first works online</h2>
<p>
The remaining weakness of the previous version was that it still let readers compress long-horizon closed-loop evidence into a <strong>same-session timing problem</strong>. Looking at the primary literature for 2014-2025, the scientific bottlenecks after a loop first "moves" are not one axis. Closed-loop BCIs now force at least <strong>(1) co-adaptation / credit assignment</strong>, <strong>(2) output-path timing</strong>, <strong>(3) fixed-decoder durability</strong>, <strong>(4) rescue-mode recalibration / remote optimization burden</strong>, and <strong>(5) eligibility / continuation / clinic-home transfer</strong> to be logged separately. Therefore, this site does not raise L3 just because the loop runs online; it asks for the following five barriers as distinct evidence objects.
</p>
<table class="data-table">
<thead>
<tr>
<th>Wall</th>
<th>What the primary literature now supports</th>
<th>Revision policy on this page</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>co-adaptation / credit assignment</strong></td>
<td><a href="https://doi.org/10.1016/j.neuron.2014.04.048" target="_blank">Orsborn et al. (2014)</a>, <a href="https://doi.org/10.1371/journal.pbio.2003787" target="_blank">Perdikis et al. (2018)</a>, <a href="https://doi.org/10.3389/fnhum.2019.00362" target="_blank">Abu-Rmileh et al. (2019)</a>, <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> show that online gains can reflect mixed changes in user strategy, decoder weights, and application policy. A loop that improves online is therefore not automatically a durable fixed decoder.</td>
<td>Record whether the decoder / thresholds / interaction policy were frozen or updated, when each change occurred, what open-loop or frozen-comparator probe was kept, and what part of the gain is attributed to user learning versus decoder adaptation.</td>
</tr>
<tr>
<td><strong>tail latency / output path</strong></td>
<td>Littlejohn et al. (2025) showed streaming brain-to-voice in <strong>80 ms steps</strong> and reported cue-to-audio timing rather than just decoder timing. Wairagkar et al. (2025) demonstrated <strong>sub-10 ms</strong> neural-to-voice synthesis while returning <strong>silence for non-speech and overlapping speech</strong>, which means output-path latency and fallback policy are part of the loop rather than post-processing detail.</td>
<td>The average latency of the reasoner is not enough, and we leave the behavior of module-wise latency, cue-to-output tail, audio playback path, and silence/abstention separately. </td>
</tr>
<tr>
<td><strong>fixed-decoder durability</strong></td>
<td>Wilson et al. (2025) made explicit that accumulating neural changes create periods in which users cannot use a static intracortical BCI reliably, and evaluated one-month operation against fixed-decoder comparators rather than hiding every failure behind adaptive rescue. That means a same-session fast loop and a fixed decoder that still works days later are not the same achievement.</td>
<td>Report the <strong>fixed decoder interval</strong>, time since last supervised calibration, degradation curve under no-update conditions, and when the claim ceiling has to drop from durable fixed-decoder evidence to rescue-mode evidence.</td>
</tr>
<tr>
<td><strong>rescue-mode recalibration / remote optimization burden</strong></td>
<td>Wilson et al. (2025) also showed multi-timescale unsupervised recalibration, Dixon et al. (2026) reported a machine-learning pipeline capable of <strong>remotely optimizing</strong> movement-responsive aDBS parameters in a <strong>home setting</strong>, and Busch et al. (2025) documented biomarker-selection, threshold-definition, and artifact-related maladaptation as programming burdens. Rescue is therefore a separate operating regime, not a free extension of fixed-decoder success.</td>
<td>Log whether rescue was <strong>manual, unsupervised, or remotely optimized</strong>, what data and staff time it required, which parameters changed, how long recovery took, and whether performance after rescue is being compared fairly against the pre-rescue fixed-decoder slice.</td>
</tr>
<tr>
<td><strong>eligibility / continuation / naturalistic transfer</strong></td>
<td>Oehrn et al. (2024) evaluated chronic adaptive DBS with both <strong>in-clinic and at-home</strong> recordings. Busch et al. (2025) reported that <strong>6 of 8</strong> patients chose to remain on adaptive DBS after two-week home evaluation, while Cascino et al. (2026) reported that only <strong>9 of 20</strong> consecutive chronic cDBS patients were eligible and <strong>5</strong> remained on chronic aDBS by July 2025. Eligibility and continuation therefore remain separate bottlenecks even after technical proof-of-principle.</td>
<td>Not only lab success, but also <strong>screened n</strong>, exclusion reasons, clinic/home slice, continuation rate, programming visits, and stimulation-duty-cycle changes are recorded as required logs on the deployment side.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Points of criticism here</strong>
<p>
Therefore, just because "the fast loop worked once" or "the adaptive controller reduced the symptoms a little" does not mean that it can be used for a long time. A same-session online gain is not yet a <strong>credit-assigned fixed-policy result</strong>; a same-session fast loop is not yet a <strong>fixed decoder that still works tomorrow</strong>; a rescued loop is not yet an <strong>easy-to-program chronic controller</strong>; and a programmable chronic controller is not yet a <strong>broadly eligible and maintainable home-use route</strong>. Only after those barriers are passed separately can we read that we are approaching a deployable closed loop.
</p>
</div>
</section>

<section class="section" id="card-stack">
<h2 class="section-title">Which public card gets stacked when the loop leaves same-session</h2>
<table class="data-table">
<thead>
<tr>
<th>Evidence slice</th>
<th>What it safely supports</th>
<th>What it still does not support</th>
<th>Public card stack on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>same-session fixed-policy local loop</strong></td>
<td>That the declared subsystem can run online with measured timing under a frozen decoder / interaction policy and an explicit fallback policy.</td>
<td>Cross-day durability, boundary completeness, easy clinical deployment.</td>
<td>Timing log plus <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> when relevant.</td>
</tr>
<tr>
<td><strong>same-session co-adaptive local loop</strong></td>
<td>That the coupled human + decoder + interface package can be trained online under a declared update policy and credit-assignment log.</td>
<td>Fixed-decoder durability, user-independent stability, broad deployment.</td>
<td>Timing log plus co-adaptation log plus <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> when relevant.</td>
</tr>
<tr>
<td><strong>cross-day fixed-decoder loop</strong></td>
<td>That a decoder survives a declared no-update interval under declared state annotation and drift conditions.</td>
<td>Adaptive rescue benefit, broad home-use scalability, solved embodiment.</td>
<td><a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> plus timing log.</td>
</tr>
<tr>
<td><strong>rescued / adaptively maintained loop</strong></td>
<td>That performance can be recovered under a declared update policy.</td>
<td>That the original fixed decoder was durable, or that rescue burden is negligible.</td>
<td><a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> plus update / rescue log and <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a>.</td>
</tr>
<tr>
<td><strong>naturalistic chronic therapeutic loop</strong></td>
<td>That the loop can remain useful under declared clinic/home and continuation constraints for the screened population.</td>
<td>That the route is broadly eligible, easy to program, or body/environment complete by default.</td>
<td><a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> plus <a href="../verification.html#body-environment-boundary-card">Body / Environment Boundary Card</a> plus deployment-burden log.</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Reading rule</strong>
<p>
This page now blocks a common shortcut: <strong>same-session online</strong> is not quietly promoted to <strong>co-adaptation-aware</strong>, <strong>durable</strong>, <strong>rescued</strong>, or <strong>deployable</strong>. Those are five different evidence slices with different public cards and different failure modes.
</p>
</div>
</section>

<section class="section" id="end-to-end">
<h2 class="section-title">What is measured end-to-end</h2>
<p>
Wilson et al.'s (2010) key point is that it is insufficient to measure signal processing latency alone. A closed loop is the entire path from the input to the output. The display, OS, driver, audio system, and stimulator may be different rate-limiting factors.
</p>
<table class="data-table">
<thead>
<tr>
<th>Interval</th>
<th>What you need to know</th>
<th>Typical measurement method</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Input</strong></td>
<td>This is when the sensor actually detected a change. </td>
<td>TTL, known pulse, DAQ input, stimulator marker output. </td>
</tr>
<tr>
<td><strong>Processing</strong></td>
<td>This is how much time it took for preprocessing, estimation, and decision making. </td>
<td>software timestamp, block duration, CPU/GPU logs. </td>
</tr>
<tr>
<td><strong>Output</strong></td>
<td>It is when a display, sound, stimulus, or control signal really occurs. </td>
<td>Photodiode, microphone, loopback, stimulus artifact onset. </td>
</tr>
<tr>
<td><strong>Return</strong></td>
<td>When the influence of the output is returned to the next input. </td>
<td>Redetection, environmental sensor, and body response logs within a closed-loop task. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Average is not enough</strong>
<p>
In a closed loop, <strong>P95/P99/worst-case</strong> and <strong>trial-to-trial jitter</strong> can be more destructive than average delay. Especially in phase-targeting and safety-critical loops, just showing the average value does not provide any reassurance.
</p>
</div>
</section>

<section class="section" id="synchronization">
<h2 class="section-title">What LSL and event markers do and don't guarantee</h2>
<p>
Kothe et al.'s (2025) LSL paper shows that LSL is useful for <strong>millisecond-scale synchronization in sufficient neurobehavioral research</strong> to provide offset correction and jitter compensation. On the other hand, this is <strong>software-based synchronization on LAN</strong> and does not automatically guarantee when the physical output of the stimulator or indicator occurs.
</p>
<p>
Appelhoff and Stenner (2021) showed that event marking with a USB microcontroller can produce <strong>latencies of less than 1 ms. However, this is also primarily a <strong>marker path</strong> accuracy. Even if the marker is fast, the end-to-end loop that includes the display, audio path, stimulator, and estimator does not necessarily have the same accuracy.
</p>
<div class="key-points">
<h4>Things to be divided here</h4>
<ul>
<li><strong>LSL: Helps with common time system and offset correction for multiple streams. </li>
<li><strong>TTL / MCU marker:</strong>Improve the accuracy of marking events to the acquisition side. </li>
<li><strong>Photodiode / microphone / loopback: Externally verify the actual output onset. </li>
<li><strong>Phase tracker:</strong>Separately audits how much phase shift remains for the target frequency. </li>
</ul>
</div>
</section>

<section class="section" id="stops">
<h2 class="section-title">Abstain, freeze and safety stop are different things</h2>
<table class="data-table">
<thead>
<tr>
<th>How it works</th>
<th>Main purpose</th>
<th>Typical trigger</th>
<th>What to keep at a minimum</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Abstain</strong></td>
<td>This is to avoid unreasonable output when reliability is low. </td>
<td>Insufficient classification probability, insufficient phase estimation reliability, OOD detection. </td>
<td>Abstention rate, confidence threshold at the time of abstention, and state after abstention. </td>
</tr>
<tr>
<td><strong>hold-last-output / silence fallback</strong></td>
<td>This is to maintain continuity without increasing erroneous output during short uncertainties or non-speech intervals. </td>
<td>non-speech interval, decoder blank, short dropout, audio buffer underrun. </td>
<td>Trigger rate, maximum duration, false speech suppression rate, and release delay. </td>
</tr>
<tr>
<td><strong>freeze / pause</strong></td>
<td>This is for recalibration and confirmation of the cause. </td>
<td>Clock offset increase, packet loss, drift deviation, resynchronization request. </td>
<td>Invocation reason, duration, restart conditions, and recalibration details. </td>
</tr>
<tr>
<td><strong>Safety stop / containment</strong></td>
<td>To stop a dangerous actuation. </td>
<td>P99 latency budget exceeded, abnormal amplitude, stimulation prohibited phase, output saturation. </td>
<td>Stop conditions, number of stops, previous latency/phase/error, and manual return conditions. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Do not mix performance and safety issues</strong>
<p>
Whether it's ``I didn't get it right so I won't output it'', ``I'm going to use silence to connect short spaces'', ``I'm going to put it on hold because the system seems to be broken'', or ``I'm going to stop it because it's dangerous'' are completely different in operational terms. If you combine everything into one "outage", you will not be able to trace the cause during review.
</p>
</div>
</section>

<section class="section" id="logs">
<h2 class="section-title">The minimum log you want to keep</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>loop class: One of</strong>state feedback, ERP/command, speech/streaming, phase-locked, burst-triggered. </li>
<li><strong>co-adaptation regime:</strong>State whether the decoder, thresholds, smoothing, evidence accumulation, or interface rules were frozen or updated, and what triggered each change.</li>
<li><strong>declared boundary / target subsystem:</strong>State whether the loop is speech, grasp, navigation, memory-task, symptom-control, or another subsystem, and state the maximum claim ceiling. </li>
<li><strong>retained / substituted sensory and self-generated-feedback routes:</strong>List which visual, tactile, auditory, proprioceptive, vestibular, respiration-linked, or predicted reafferent cues were present, simulated, or omitted. </li>
<li><strong>retained / substituted action channels:</strong>Name the actual plant or actuator, such as cursor, robotic hand, speech synthesizer, avatar, or stimulator, together with its controllable degrees of freedom. </li>
<li><strong>interoceptive / arousal logs:</strong>Record whether respiration, pupil, HR / HRV, effort, fatigue, or similar organism-wide covariates were logged, manipulated, or left latent. </li>
<li><strong>slow internal-milieu logs:</strong>Record whether circadian phase or clock time, recent sleep-wake schedule, cortisol / glucocorticoid assay or steroid treatment, feeding / fasting or glucose-insulin regime, and similar slow body-state covariates were controlled, measured, perturbed, or left latent. </li>
<li><strong>end-to-end latency:</strong>Leave median, P95, P99, worst-case separate. </li>
<li><strong>Module-wise latency:</strong> Separate input, inference, output, and recursive input, leaving what is rate-limiting. </li>
<li><strong>Definition of jitter:</strong>Specify SD, IQR, or peak-to-peak. </li>
<li><strong>clock offset / drift: Leave before and after the LSL and hardware marker correction. </li>
<li><strong>Marker verification method:</strong>Write which of TTL, MCU, photodiode, microphone, or loopback was used for actual measurement. </li>
<li><strong>loop-removal / ablation test:</strong>Report what happened when tactile feedback, self-motion cues, predicted sensory consequences, or another decisive route was removed, scrambled, or delayed. </li>
<li><strong>credit-assignment probe:</strong>Keep fixed-policy or open-loop probe blocks so gains can be compared with and without closed-loop correction or online updates.</li>
<li><strong>Additional metrics for speech / streaming: </strong>Leave cue-to-output tail latency, audio driver latency, silence / hold-last-output rate, and false speech rate. </li>
<li><strong>Additional metrics for phase-targeting systems:</strong>Target band and spatial filter, power/SNR gate, no-stim rate, causal-versus-post-hoc benchmark, mean phase offset, circular spread or equivalent circular metric, trigger-time phase-locking statistic, missed trigger, and any fixed-versus-adaptive phase policy. </li>
<li><strong>Additional metrics for burst systems:</strong>Name biomarker family and symptom target, sensing contacts and signal-to-noise, controller mode, medication / movement state, floor/ceiling amplitude, update interval / onset duration / ramp policy, false positive/negative, artifact-triggered resets, comparator condition, and any TEED / duty-cycle matching rule. </li>
<li><strong>residual omitted loops / abstention boundary:</strong>State which body/environment routes remain absent and what stronger claim therefore remains forbidden. </li>
<li><strong>Abstain/freeze/safety stop:</strong>Leave the number of activations, previous state, and return conditions. </li>
<li><strong>fixed decoder interval / training-free horizon:</strong>State how long the system was required to run before any supervised or unsupervised update was allowed. </li>
<li><strong>user/application training changes:</strong>Record practice dose, instruction changes, control-paradigm refinements, prompt or task-scaffold changes, and engagement / fatigue notes across sessions.</li>
<li><strong>rescue-mode policy:</strong>Record whether unsupervised adaptation, manual reprogramming, or remote optimization was used, which parameters changed, and what manpower/time was required. </li>
<li><strong>eligibility / continuation / naturalistic deployment:</strong>Leave clinic/home performance difference, screened n, exclusion reasons, continuation, programming visits, and duty cycle. </li>
<li><strong>Performance degradation curve:</strong> Leaves the point at which it collapses when artificially adding delay. </li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">16 questions when reading L3 arguments</h2>
<ol>
<li><strong>Does it say which loop class it deals with?</strong> Check whether slow feedback, speech streaming, phase-locked, and aDBS are mentioned in the same table. </li>
<li><strong>Does it declare which body/environment boundary it actually used?</strong> Check whether the paper fixes the target subsystem and names preserved, substituted, and omitted loops instead of only saying "closed loop."</li>
<li><strong>Are sensory, action, interoceptive, and slow internal-milieu routes disclosed?</strong> Look for tactile, proprioceptive, vestibular, respiration-linked, arousal-linked, circadian, glucocorticoid, and metabolic-state channels, not only the main output stream. </li>
<li><strong>Was any decisive loop component removed or scrambled?</strong> Check whether feedback-removal or sensory-ablation tests were run, rather than assuming robustness. </li>
<li><strong>Are there module-wise measurements, not just end-to-end?</strong> Don't just rely on software timestamps; check which of the input, inference, and output paths are rate-limiting. </li>
<li><strong>For speech / streaming, are silence and output path displayed?</strong> Check whether false speech, audio driver, or hold-last-output are hidden. </li>
<li><strong>Is delay mapped to phase error, burst timing, or controller-update timescale?</strong> Check whether the paper goes beyond a single ms value when phase targeting or adaptive stimulation policy is what matters. </li>
<li><strong>For phase-targeted loops, does it show the oscillation was estimable before triggering?</strong> Check whether power/SNR thresholds, no-stim epochs, and phase-reset rejection were declared rather than assuming every band-passed epoch has meaningful phase.</li>
<li><strong>For phase-targeted loops, does it separate targeting success from functional effect and from phase stability?</strong> Check whether the paper reports circular targeting precision, off-target or random-phase comparators, and whether the preferred phase was fixed or drifted across time. </li>
<li><strong>For burst-driven loops, does it name the biomarker family and symptom target?</strong> Check whether the paper distinguishes beta, beta-burst duration, entrained gamma, dyskinesia-linked gamma, or another personalized marker rather than saying only "adaptive DBS."</li>
<li><strong>For burst-driven loops, does it disclose controller mode, state dependence, and comparator?</strong> Check whether medication / movement dependence, single versus dual threshold or other policy, artifact burden, and cDBS or random / surrogate comparators are shown rather than only burst-trigger timing. </li>
<li><strong>Does it separate user learning, decoder updates, and interface redesign?</strong> Check whether the gain could come from co-adaptation rather than from a stable fixed decoder. </li>
<li><strong>Does it separate fixed-decoder durability from adaptive rescue?</strong> Check whether the paper shows the no-update slice rather than reporting only the post-update result. </li>
<li><strong>If rescue happened, is the rescue cost shown?</strong> Check whether staff time, parameter changes, remote optimization, or unsupervised adaptation are hidden. </li>
<li><strong>Are eligibility, continuation, and clinic/home transfer shown separately from symptom benefit?</strong> Check that deployability is not inferred from a small set of successfully programmed cases alone. </li>
<li><strong>Are abstentions, silence fallbacks, freezes, and safety stops separated?</strong> Confirm that danger-handling and low-confidence handling are not collapsed into one outage label. </li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. <em>IEEE Trans Biomed Eng.</em> 2010;57(7):1785-1797. <a href="https://doi.org/10.1109/TBME.2010.2047259" target="_blank">doi:10.1109/TBME.2010.2047259</a></li>
<li>Thompson DE, Warschausky SA, Huggins JE. Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. <em>J Neural Eng.</em> 2013;10(1):016006. <a href="https://doi.org/10.1088/1741-2560/10/1/016006" target="_blank">doi:10.1088/1741-2560/10/1/016006</a></li>
<li>Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. <em>Brain Comput Interfaces.</em> 2017;4(3):137-145. <a href="https://doi.org/10.1080/2326263X.2017.1338010" target="_blank">doi:10.1080/2326263X.2017.1338010</a></li>
<li>Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. <em>J Neural Eng.</em> 2020;17(6):066012. <a href="https://doi.org/10.1088/1741-2552/abc8d7" target="_blank">doi:10.1088/1741-2552/abc8d7</a></li>
<li>Mansouri F, Fettes P, Schulze L, et al. A Real-Time Phase-Locking System for Non-invasive Brain Stimulation. <em>Front Neurosci.</em> 2018;12:877. <a href="https://doi.org/10.3389/fnins.2018.00877" target="_blank">doi:10.3389/fnins.2018.00877</a></li>
<li>Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <em>Brain Stimul.</em> 2018;11(2):374-389. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Holt AB, Kormann E, Gulberti A, et al. Phase-Dependent Suppression of Beta Oscillations in Parkinson's Disease Patients. <em>J Neurosci.</em> 2019;39(6):1119-1134. <a href="https://doi.org/10.1523/JNEUROSCI.1913-18.2018" target="_blank">doi:10.1523/JNEUROSCI.1913-18.2018</a></li>
<li>Zrenner C, Galevska D, Nieminen JO, Baur D, Stefanou MI, Ziemann U. The shaky ground truth of real-time phase estimation. <em>Neuroimage.</em> 2020;214:116761. <a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">doi:10.1016/j.neuroimage.2020.116761</a></li>
<li>Gordon PC, Dörre S, Belardinelli P, Stenroos M, Zrenner B, Ziemann U, Zrenner C. Prefrontal Theta-Phase Synchronized Brain Stimulation With Real-Time EEG-Triggered TMS. <em>Front Hum Neurosci.</em> 2021;15:691821. <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">doi:10.3389/fnhum.2021.691821</a></li>
<li>Bruegger D, Abegg M. Prediction of cortical theta oscillations in humans for phase-locked visual stimulation. <em>J Neurosci Methods.</em> 2021;361:109288. <a href="https://doi.org/10.1016/j.jneumeth.2021.109288" target="_blank">doi:10.1016/j.jneumeth.2021.109288</a></li>
<li>Vigué-Guix I, Morís Fernández L, Torralba Cuello M, Ruzzoli M, Soto-Faraco S. Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain-computer interface (BCI)? <em>Eur J Neurosci.</em> 2022;55(11-12):3224-3240. <a href="https://doi.org/10.1111/ejn.14931" target="_blank">doi:10.1111/ejn.14931</a></li>
<li>Kim B, Erickson BA, Fernandez-Nunez G, Rich R, Mentzelopoulos G, Vitale F, Medaglia JD. EEG Phase Can Be Predicted with Similar Accuracy across Cognitive States after Accounting for Power and Signal-to-Noise Ratio. <em>eNeuro.</em> 2023;10(9):ENEURO.0050-23.2023. <a href="https://doi.org/10.1523/ENEURO.0050-23.2023" target="_blank">doi:10.1523/ENEURO.0050-23.2023</a></li>
<li>Hougland JR, Kirchhoff M, Vetter DE, Ahola O, Jooß A, Humaidan D, Ziemann U. Fluctuations in the optimal sensorimotor mu-rhythm phase associated with high corticospinal excitability during TMS-EEG. <em>Brain Stimul.</em> 2025;18(6):1843-1851. <a href="https://doi.org/10.1016/j.brs.2025.09.019" target="_blank">doi:10.1016/j.brs.2025.09.019</a></li>
<li>Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. <em>Ann Neurol.</em> 2013;74(3):449-457. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <em>Brain.</em> 2017;140(4):1053-1067. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Mathiopoulou V, Lofredi R, Feldmann LK, et al. Modulation of subthalamic beta oscillations by movement, dopamine, and deep brain stimulation in Parkinson's disease. <em>npj Parkinsons Dis.</em> 2024;10:77. <a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">doi:10.1038/s41531-024-00693-3</a></li>
<li>Stanslaski S, Summers RLS, Tonder L, et al. Sensing data and methodology from the Adaptive DBS Algorithm for Personalized Therapy in Parkinson's Disease (ADAPT-PD) clinical trial. <em>npj Parkinsons Dis.</em> 2024;10:174. <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">doi:10.1038/s41531-024-00772-5</a></li>
<li>Olaru M, et al. Motor network gamma oscillations in chronic home recordings predict dyskinesia in Parkinson's disease. <em>Brain.</em> 2024;147:2038-2052. <a href="https://doi.org/10.1093/brain/awae004" target="_blank">doi:10.1093/brain/awae004</a></li>
<li>Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. <em>Behav Res Methods.</em> 2021;53(6):2450-2455. <a href="https://doi.org/10.3758/s13428-021-01571-z" target="_blank">doi:10.3758/s13428-021-01571-z</a></li>
<li>Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. <em>Imaging Neurosci.</em> 2025;3:IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Keller GB, Bonhoeffer T, Hubener M. Sensorimotor mismatch signals in primary visual cortex of the behaving mouse. <em>Neuron.</em> 2012;74(5):809-815. <a href="https://doi.org/10.1016/j.neuron.2012.03.040" target="_blank">doi:10.1016/j.neuron.2012.03.040</a></li>
<li>Saleem AB, Ayaz A, Jeffery KJ, Harris KD, Carandini M. Integration of visual motion and locomotion in mouse visual cortex. <em>Nat Neurosci.</em> 2013;16(12):1864-1869. <a href="https://doi.org/10.1038/nn.3567" target="_blank">doi:10.1038/nn.3567</a></li>
<li>Ravassard P, Kees A, Willers B, et al. Multisensory control of hippocampal spatiotemporal selectivity. <em>Science.</em> 2013;340(6138):1342-1346. <a href="https://doi.org/10.1126/science.1232655" target="_blank">doi:10.1126/science.1232655</a></li>
<li>Schneider DM, Nelson A, Mooney R. A synaptic and circuit basis for corollary discharge in the auditory cortex. <em>Nature.</em> 2014;513(7517):189-194. <a href="https://doi.org/10.1038/nature13724" target="_blank">doi:10.1038/nature13724</a></li>
<li>Zelano C, Jiang H, Zhou G, et al. Nasal respiration entrains human limbic oscillations and modulates cognitive function. <em>J Neurosci.</em> 2016;36(49):12448-12467. <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">doi:10.1523/JNEUROSCI.2586-16.2016</a></li>
<li>Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. <em>Nat Neurosci.</em> 2019;22:1677-1686. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Stringer C, Pachitariu M, Steinmetz N, et al. Spontaneous behaviors drive multidimensional, brainwide activity. <em>Science.</em> 2019;364(6437):eaav7893. <a href="https://doi.org/10.1126/science.aav7893" target="_blank">doi:10.1126/science.aav7893</a></li>
<li>Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science.</em> 2021;372(6544):831-836. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Raut RV, Rosenthal ZP, Wang X, et al. Arousal as a universal embedding for spatiotemporal brain dynamics. <em>Nature.</em> 2025;647:454-461. <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">doi:10.1038/s41586-025-09544-4</a></li>
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nat Neurosci.</em> 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. <em>Nature.</em> 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Mathiopoulou V, Habets J, Feldmann LK, et al. Gamma entrainment induced by deep brain stimulation as a biomarker for motor improvement with neuromodulation. <em>Nat Commun.</em> 2025;16:2956. <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">doi:10.1038/s41467-025-58132-7</a></li>
<li>Wilkins KB, Melbourne JA, Akella P, et al. Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease. <em>Brain Commun.</em> 2025. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/" target="_blank">PMCID: PMC12268161</a></li>
<li>Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. <em>Nat Biomed Eng.</em> 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <em>Nat Med.</em> 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. <em>npj Parkinsons Dis.</em> 2026. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
<li>Dixon TC, Strandquist G, Zeng A, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. <em>Nat Biomed Eng.</em> 2026;10:110-124. <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">doi:10.1038/s41551-025-01438-0</a></li>
<li>Busch JL, Kaplan J, Behnke JK, et al. Chronic adaptive deep brain stimulation for Parkinson’s disease: clinical outcomes and programming strategies. <em>npj Parkinsons Dis.</em> 2025;11:264. <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">doi:10.1038/s41531-025-01124-7</a></li>
<li>Orsborn AL, Moorman HG, Overduin SA, Shanechi MM, Dimitrov DF, Carmena JM. Closed-loop decoder adaptation shapes neural plasticity for skillful neuroprosthetic control. <em>Neuron.</em> 2014;82(6):1380-1393. <a href="https://doi.org/10.1016/j.neuron.2014.04.048" target="_blank">doi:10.1016/j.neuron.2014.04.048</a></li>
<li>Perdikis S, Tonin L, Saeedi S, et al. The Cybathlon BCI race: successful longitudinal mutual learning with two tetraplegic users. <em>PLoS Biol.</em> 2018;16(5):e2003787. <a href="https://doi.org/10.1371/journal.pbio.2003787" target="_blank">doi:10.1371/journal.pbio.2003787</a></li>
<li>Abu-Rmileh A, Zakkay E, Shmuelof L, Shriki O. Co-adaptive training improves efficacy of a multi-day EEG-based motor imagery BCI training. <em>Front Hum Neurosci.</em> 2019;13:362. <a href="https://doi.org/10.3389/fnhum.2019.00362" target="_blank">doi:10.3389/fnhum.2019.00362</a></li>
<li>Lin CY, Lu CF, Jao CW, Wang PS, Wu YT. Toward consistency between humans and classifiers: improved performance of a real-time brain-computer interface using a mutual learning system. <em>Expert Syst Appl.</em> 2023;226:120205. <a href="https://doi.org/10.1016/j.eswa.2023.120205" target="_blank">doi:10.1016/j.eswa.2023.120205</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
If you want to go back to the overall design of L3, please use <a href="../verification.html">Verification Platform</a>, if you want to go back to EEG and synchronization practices, please use <a href="../eeg_101.html">Introduction to EEG</a>, and if you want to go back to Roadmap I1/I8, please use <a href="../tech_roadmap.html">Technology Roadmap</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="event-sync-and-measurement-logs.html">Event synchronization and observation logs →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">Uncertainty/proofreading/abstention →</a></li>
<li><a href="update-branching-and-stop-rules.html">Update/branching/stop rules →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../eeg_101.html">Introduction to EEG →</a></li>
<li><a href="../tech_roadmap.html">Technology roadmap →</a></li>
</ul>
</div>
</aside>
</main>
