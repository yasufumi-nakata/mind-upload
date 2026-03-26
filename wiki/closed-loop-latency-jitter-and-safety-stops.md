---
layout: default
title: "Wiki: Closed Loop, Delay, Jitter, Safe Stop"
description: "Delay, jitter, tail latency, fixed-decoder durability, recalibration burden, deployment eligibility, and the body/environment boundary are organized from primary literature for each type of closed loop."
article_type: Wiki
subtitle: "Closed-loop time requirements are not a single number; they vary by loop type"
author: Mind Uploading Research Project
last_updated: "2026-03-26"
note: "Learning guide / evidence refresh"
audience: "People who want to read about L3 closed-loop evaluation and real-time operation based on literature rather than general information"
reading_time: "14-22 minutes"
page_intro: "This page is a wiki that organizes delay, jitter, drift, safety stop, body/environment boundary, and long-horizon deployability in Mind-Upload's L3 'closed loop' using primary literature. The purpose is to clarify that even when offline accuracy is high, the required timing budget depends on the loop band and actuator, and low latency alone does not tell you which sensory, motor, interoceptive, or reafferent loops were actually preserved, whether a fixed decoder survived across time, or how much rescue-mode programming was needed."
accuracy_note: "Here, we do not set a ``fixed threshold common to all loops.'' We also do not treat a fast loop as boundary-complete, temporally durable, or chronically deployable by default. Judgments are written on the premise that end-to-end timing indicators, retained/substituted body/environment routes, fixed-decoder interval, rescue-mode adaptation burden, and deployment slices are disclosed explicitly."
page_highlights:
  - "Closed-loop time requirements vary by loop type, not by a single ms value."
  - "Low latency is not the same as reproducing the relevant body/environment boundary."
  - "A same-session fast loop, a fixed decoder that survives across days, an adaptively rescued loop, and a chronically deployable loop are different achievements."
  - "Even if the event marker is less than 1 ms, it is a different matter from guaranteeing end-to-end for the entire system."
  - "Phase error is more important than ms for phase-targeting, and for adaptive DBS the timing story now has to be separated from fixed-decoder durability, programming burden, and eligibility."
  - "Streaming speech BCI needs to record not only average delay but also tail latency, output-path audit, silence/hold-last-output, and fixed-decoder horizon in separate logs."
  - "Adaptive-DBS papers need to log rescue-mode optimization, clinic/home transfer, eligibility, and continuation separately from symptom benefit."
known_points:
  - "Offline accuracy and closed-loop stability are separate claims and cannot be audited with the same score."
  - "Even a fast loop can remain boundary-incomplete if self-motion, predicted reafference, tactile feedback, respiration, arousal, or other subject-defining routes stay omitted or undisclosed."
  - "Latency and jitter tolerances vary for state feedback, ERP/command BCI, streaming communication, phase-locked stimulation, and burst-driven neuromodulation."
  - "Unless you actually measure input, processing, output, and return end-to-end, you won't know the timing of actual operation."
  - "Fixed-decoder durability and rescue-mode recalibration are separate evidence objects; one can fail while the other still rescues behavior."
  - "Speed-up within-session alone is not enough; it also leaves fixed-decoder horizon, recalibration burden, clinic/home transition, and programming burden."
  - "Chronic adaptive-DBS symptom benefit, eligibility, and long-run continuation are different axes and should not be collapsed into one deployment verdict."
unknown_points:
  - "It is unclear how far the closed-loop bandwidth required for WBE spans which loop types."
  - "It is not yet possible to generalize the precision required for phase-specific control to all tasks in non-invasive human experiments."
  - "What counts as an acceptable fixed-decoder horizon before rescue-mode adaptation becomes a different operating regime still depends on task and modality."
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
This page now keeps <strong>timing logs</strong> separate from <strong>body/environment boundary logs</strong>. A loop can be fast and still remain boundary-incomplete if the paper does not say which sensory, action, interoceptive, and self-generated-feedback routes were preserved, substituted, or omitted. On this site, low latency without that disclosure does not rise above a task-specific local controller or surrogate-body result.
</p>
</div>

<div class="note-box">
<strong>Three public cards are stacked here, not one timing score</strong>
<p>
On this site, once a closed-loop claim leaves the narrow same-session timing question, it has to stack the <a href="../verification.html#temporal-validity-card">Verification: Temporal Validity Card</a> with the <a href="../verification.html#body-environment-boundary-card">Verification: Body / Environment Boundary Card</a>, and add the <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> whenever silence, abstention, or fallback behavior matters. A fast loop without those companion cards stays a bounded local-controller result.
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
</section>

<section class="section" id="boundary-before-latency">
<h2 class="section-title">Before milliseconds, fix which loop boundary was actually preserved</h2>
<p>
The weakness of the older timing-only reading was that it could still let a reader say, <strong>"the loop was fast, therefore the closed-loop problem is close to solved."</strong> That is too weak. Primary literature shows that sensory cortex and higher-order dynamics are continuously reshaped by self-motion, predicted sensory consequences, multisensory navigation cues, respiration, arousal, and tactile feedback. Therefore, a low-latency controller is not automatically a boundary-complete controller.
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
If the paper does not disclose which sensory, action, interoceptive, and self-generated-feedback routes were retained, substituted, or omitted, this site does not promote the result from <strong>fast local loop</strong> to <strong>boundary-complete L3 evidence</strong>. The formal public rule is the <a href="../verification.html#body-environment-boundary-card">Verification: Body / Environment Boundary Card</a>; this wiki supplies the timing-side companion logic.
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
<td>Mansouri et al. (2018) evaluated phase lag in theta/alpha, and Zrenner et al. (2018) demonstrated brain state dependence in millisecond-resolution EEG-triggered TMS. Here, phase error is more important than ms. </td>
<td>Target frequency, phase error distribution, reliability of estimated phase, missed trigger, and fallback conditions in case of phase shift. </td>
</tr>
<tr>
<td><strong>burst/state-triggered neuromodulation</strong></td>
<td>Adaptive DBS using beta burst. </td>
<td>Little et al. (2013) demonstrated the proof-of-principle of using pathological beta for feedback, and Tinkhauser et al. (2017) showed that adaptive DBS changes the distribution of short bursts of <strong>100–600 ms</strong> and long bursts of >600 ms. Domination time is slower than phase-locking. </td>
<td>biomarker detection delay, burst false positive/false negative, ramp-up/ramp-down, number of stops. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="longitudinal-bottlenecks">
<h2 class="section-title">2026-03 literature audit: four barriers that appear after same-session success</h2>
<p>
The remaining weakness of the previous version was that it still let readers compress long-horizon closed-loop evidence into a <strong>same-session timing problem</strong>. Looking at the primary literature for 2024-2026, the scientific bottlenecks after a loop first "moves" are not one axis. Speech BCI and chronic aDBS now force at least <strong>(1) output-path timing</strong>, <strong>(2) fixed-decoder durability</strong>, <strong>(3) rescue-mode recalibration / remote optimization burden</strong>, and <strong>(4) eligibility / continuation / clinic-home transfer</strong> to be logged separately. Therefore, this site does not raise L3 just because the loop runs online; it asks for the following four barriers as distinct evidence objects.
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
Therefore, just because "the fast loop worked once" or "the adaptive controller reduced the symptoms a little" does not mean that it can be used for a long time. A same-session fast loop is not yet a <strong>fixed decoder that still works tomorrow</strong>; a rescued loop is not yet an <strong>easy-to-program chronic controller</strong>; and a programmable chronic controller is not yet a <strong>broadly eligible and maintainable home-use route</strong>. Only after those barriers are passed separately can we read that we are approaching a deployable closed loop.
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
<td><strong>same-session fast local loop</strong></td>
<td>That the declared subsystem can run online with measured timing and an explicit fallback policy.</td>
<td>Cross-day durability, boundary completeness, easy clinical deployment.</td>
<td>Timing log plus <a href="../verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> when relevant.</td>
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
This page now blocks a common shortcut: <strong>same-session online</strong> is not quietly promoted to <strong>durable</strong>, <strong>rescued</strong>, or <strong>deployable</strong>. Those are four different evidence slices with different public cards and different failure modes.
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
<li><strong>declared boundary / target subsystem:</strong>State whether the loop is speech, grasp, navigation, memory-task, symptom-control, or another subsystem, and state the maximum claim ceiling. </li>
<li><strong>retained / substituted sensory and self-generated-feedback routes:</strong>List which visual, tactile, auditory, proprioceptive, vestibular, respiration-linked, or predicted reafferent cues were present, simulated, or omitted. </li>
<li><strong>retained / substituted action channels:</strong>Name the actual plant or actuator, such as cursor, robotic hand, speech synthesizer, avatar, or stimulator, together with its controllable degrees of freedom. </li>
<li><strong>interoceptive / arousal logs:</strong>Record whether respiration, pupil, HR / HRV, effort, fatigue, or similar organism-wide covariates were logged, manipulated, or left latent. </li>
<li><strong>end-to-end latency:</strong>Leave median, P95, P99, worst-case separate. </li>
<li><strong>Module-wise latency:</strong> Separate input, inference, output, and recursive input, leaving what is rate-limiting. </li>
<li><strong>Definition of jitter:</strong>Specify SD, IQR, or peak-to-peak. </li>
<li><strong>clock offset / drift: Leave before and after the LSL and hardware marker correction. </li>
<li><strong>Marker verification method:</strong>Write which of TTL, MCU, photodiode, microphone, or loopback was used for actual measurement. </li>
<li><strong>loop-removal / ablation test:</strong>Report what happened when tactile feedback, self-motion cues, predicted sensory consequences, or another decisive route was removed, scrambled, or delayed. </li>
<li><strong>Additional metrics for speech / streaming: </strong>Leave cue-to-output tail latency, audio driver latency, silence / hold-last-output rate, and false speech rate. </li>
<li><strong>Additional metrics for phase/burst systems:</strong>Phase error distribution, missed trigger, burst detection delay, false positive/negative. </li>
<li><strong>residual omitted loops / abstention boundary:</strong>State which body/environment routes remain absent and what stronger claim therefore remains forbidden. </li>
<li><strong>Abstain/freeze/safety stop:</strong>Leave the number of activations, previous state, and return conditions. </li>
<li><strong>fixed decoder interval / training-free horizon:</strong>State how long the system was required to run before any supervised or unsupervised update was allowed. </li>
<li><strong>rescue-mode policy:</strong>Record whether unsupervised adaptation, manual reprogramming, or remote optimization was used, which parameters changed, and what manpower/time was required. </li>
<li><strong>eligibility / continuation / naturalistic deployment:</strong>Leave clinic/home performance difference, screened n, exclusion reasons, continuation, programming visits, and duty cycle. </li>
<li><strong>Performance degradation curve:</strong> Leaves the point at which it collapses when artificially adding delay. </li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">11 questions when reading L3 arguments</h2>
<ol>
<li><strong>Does it say which loop class it deals with?</strong> Check whether slow feedback, speech streaming, phase-locked, and aDBS are mentioned in the same table. </li>
<li><strong>Does it declare which body/environment boundary it actually used?</strong> Check whether the paper fixes the target subsystem and names preserved, substituted, and omitted loops instead of only saying "closed loop."</li>
<li><strong>Are sensory, action, and interoceptive routes disclosed?</strong> Look for tactile, proprioceptive, vestibular, respiration-linked, and arousal-linked channels, not only the main output stream. </li>
<li><strong>Was any decisive loop component removed or scrambled?</strong> Check whether feedback-removal or sensory-ablation tests were run, rather than assuming robustness. </li>
<li><strong>Are there module-wise measurements, not just end-to-end?</strong> Don't just rely on software timestamps; check which of the input, inference, and output paths are rate-limiting. </li>
<li><strong>For speech / streaming, are silence and output path displayed?</strong> Check whether false speech, audio driver, or hold-last-output are hidden. </li>
<li><strong>Is delay mapped to phase error or burst time?</strong> Check whether the paper goes beyond a single ms value when phase or burst timing is what matters. </li>
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
<li>Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. <em>Ann Neurol.</em> 2013;74(3):449-457. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <em>Brain.</em> 2017;140(4):1053-1067. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
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
<li>Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. <em>Nat Biomed Eng.</em> 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <em>Nat Med.</em> 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. <em>npj Parkinsons Dis.</em> 2026. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
<li>Dixon TC, Strandquist G, Zeng A, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. <em>Nat Biomed Eng.</em> 2026;10:110-124. <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">doi:10.1038/s41551-025-01438-0</a></li>
<li>Busch JL, Kaplan J, Behnke JK, et al. Chronic adaptive deep brain stimulation for Parkinson’s disease: clinical outcomes and programming strategies. <em>npj Parkinsons Dis.</em> 2025;11:264. <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">doi:10.1038/s41531-025-01124-7</a></li>
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
