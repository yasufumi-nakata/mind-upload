# Wiki: Closed Loop, Delay, Jitter, Safe Stop

> Closed-loop time requirements are not a single number; they vary by loop type
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-15 / Role: Learning guide / evidence refresh

## Role Of This Page
This page is a wiki that organizes the differences between delay, jitter, drift, and safety stop, which are important in Mind-Upload's L3 'closed loop', according to primary literature. The purpose is to clarify that even in models with high offline accuracy, the required timing budget will change depending on the loop band and type of actuator.

## Accuracy Notes
Here, we do not set a ``fixed threshold common to all loops.'' We write on the premise that judgments are made based on actually measured end-to-end indicators according to the issue, target frequency, output mechanism, and safety requirements.

## Back To Public Pages
- [Verification base](https://mind-upload.com/verification.html)
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Technology Roadmap](https://mind-upload.com/tech_roadmap.html)

## Related Wiki Pages
- [Wiki: Event synchronization and observation log](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Compensates for delay, jitter, and drift.
- [Wiki: Uncertainty, proofreading, abstaining](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - Complements the design concept of 'not releasing' when reliability is low.
- [Wiki: Update/branch/stop rules](https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules) - Complements how to separate freeze and stop rules as operations.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other auxiliary pages.

## What Is Currently Known
- Offline accuracy and closed-loop stability are separate claims and cannot be audited with the same score.
- Latency and jitter tolerances vary for state feedback, ERP/command BCI, streaming communication, phase-locked stimulation, and burst-driven neuromodulation.
- Unless you actually measure input, processing, output, and return end-to-end, you won't know the timing of actual operation.
- Speed-up within-session alone is not enough; it also leaves recalibration burden, clinic/home transition, and programming burden.

## What Is Still Unknown
- It is unclear how far the closed-loop bandwidth required for WBE spans which loop types.
- It is not yet possible to generalize the precision required for phase-specific control to all tasks in non-invasive human experiments.
- What is considered 'unstable' or 'impractical' in terms of drift, recalibration frequency, and programming burden during long-term operation depends on the task.

---

<h2>The shortest conclusion</h2>
<p>
A <strong>closed loop</strong> is a system in which the output changes the next input. However, there is more than one timing required. The dominant time scales and breakdown methods are different for<strong>alpha neurofeedback</strong>,<strong>P300/ERP BCI</strong>,<strong>streaming speech neuroprosthesis</strong>,<strong>phase-locked stimulation</strong>, and<strong>adaptive DBS</strong>. Therefore, it is dangerous to place a <strong>common 1 ms threshold</strong> or <strong>common 10 ms threshold</strong> as the correct answer for the whole site.
</p>

<strong>What was fixed first in this organization</strong>
<p>
On this page, instead of talking about "how fast is enough" in an abstract way, we first fix <strong>which loop type we are dealing with</strong>, <strong>what is the delay that breaks in the loop</strong>, and <strong>what was actually measured with hardware</strong>. Event marker acceleration, LSL synchronization, phase tracking, and stopping rules are separate layers.
</p>

<h2>Why fixed thresholds are dangerous</h2>
<p>
Wilson et al. (2010) showed that for relatively slow BCI indicators such as mu rhythm amplitude, a small delay of about 10 ms does not necessarily destroy the essence, but if the latency/jitter of the entire system is not measured, the output path and display become rate-limiting. Conversely, Belinskaia et al. (2020) showed that with parietal alpha neurofeedback, an<strong>additional 250 ms / 500 ms delay</strong> worsened the learning effect. Furthermore, in phase-targeting systems such as Mansouri et al. (2018) and Zrenner et al. (2018), the delay should be evaluated as<strong>the phase error relative to the frequency of interest</strong>and not simply as a ms value.
</p>

<strong>Reading principles</strong>
<p>
"Low latency is good" is generally correct, but it cannot immediately be said that "microsecond-level delay is required for all loops" or "1 ms or less is required for all loops." The correct question is<strong>in what loop band, what error breaks what</strong>.
</p>

<h2>First, divide into 5 loop types</h2>
<table>
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

<h2>2026-03 Literature audit: Three barriers that increase with long-term operation</h2>
<p>
The weakness of the previous version was that it too often categorized the closed loop as a <strong>same-session timing problem</strong>. Looking at the primary literature for 2024-2026, in addition to normal latency/jitter, speech BCI and chronic aDBS have other barriers such as tail latency and output path, recalibration burden, and natural deployment / programming burden. Therefore, this site does not raise L3 just because the loop "moves", but requests the following three axes in separate logs.
</p>
<table>
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
<td>Littlejohn et al. (2025) showed streaming speech in 80 ms increments and separately published the delay distribution from go cue to actual speech. Wairagkar et al. (2025) demonstrated neural-to-voice synthesis of less than 10 ms, but also demonstrated that the audio driver is speed-dependent in closed-loop feedback. </td>
<td>The average latency of the reasoner is not enough, and we leave the behavior of module-wise latency, cue-to-output tail, audio playback path, and silence/abstention separately. </td>
</tr>
<tr>
<td><strong>recalibration burden / drift</strong></td>
<td>Wilson et al. (2025) found that frequent daily supervised recalibration is a major obstacle to daily use, and evaluated unsupervised recalibration that handles the drift of multiple timescales in a one-month closed-loop. </td>
<td><code>time since last supervised calibration</code>, presence or absence of unsupervised adaptation, performance degradation curve, recovery time, and manual intervention time are raised to the main log. </td>
</tr>
<tr>
<td><strong>naturalistic deployment / programming burden</strong></td>
<td>Oehrn et al. (2024) evaluated chronic aDBS in both in-clinic and at-home settings, and compared them even in a natural environment. Cascino et al. (2026) reported that 9 out of 20 consecutive cases of chronic cDBS were eligible for aDBS, with 5 continuing as of July 2025, indicating that technical/programming constraints affect deployability. </td>
<td>Not only successes in the lab, but also clinic/home transition, eligibility, continuation, programming changes, and stimulation duty cycle are recorded as required logs on the deployment side. </td>
</tr>
</tbody>
</table>

<strong>Points of criticism here</strong>
<p>
Therefore, just because "the fast loop worked once" or "the adaptive controller reduced the symptoms a little" does not mean that it can be used for a long time. Only after <strong>tail latency</strong>, <strong>manual recalibration</strong>, and <strong>establishment at home</strong> are passed separately can we read that we are approaching a deployable closed loop.
</p>

<h2>What is measured end-to-end</h2>
<p>
Wilson et al.'s (2010) key point is that it is insufficient to measure signal processing latency alone. A closed loop is the entire path from the input to the output. The display, OS, driver, audio system, and stimulator may be different rate-limiting factors.
</p>
<table>
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

<strong>Average is not enough</strong>
<p>
In a closed loop, <strong>P95/P99/worst-case</strong> and <strong>trial-to-trial jitter</strong> can be more destructive than average delay. Especially in phase-targeting and safety-critical loops, just showing the average value does not provide any reassurance.
</p>

<h2>What LSL and event markers do and don't guarantee</h2>
<p>
Kothe et al.'s (2025) LSL paper shows that LSL is useful for <strong>millisecond-scale synchronization in sufficient neurobehavioral research</strong> to provide offset correction and jitter compensation. On the other hand, this is <strong>software-based synchronization on LAN</strong> and does not automatically guarantee when the physical output of the stimulator or indicator occurs.
</p>
<p>
Appelhoff and Stenner (2021) showed that event marking with a USB microcontroller can produce <strong>latencies of less than 1 ms. However, this is also primarily a <strong>marker path</strong> accuracy. Even if the marker is fast, the end-to-end loop that includes the display, audio path, stimulator, and estimator does not necessarily have the same accuracy.
</p>

<h4>Things to be divided here</h4>
<ul>
<li><strong>LSL: Helps with common time system and offset correction for multiple streams. </li>
<li><strong>TTL / MCU marker:</strong>Improve the accuracy of marking events to the acquisition side. </li>
<li><strong>Photodiode / microphone / loopback: Externally verify the actual output onset. </li>
<li><strong>Phase tracker:</strong>Separately audits how much phase shift remains for the target frequency. </li>
</ul>

<h2>Abstain, freeze and safety stop are different things</h2>
<table>
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

<strong>Do not mix performance and safety issues</strong>
<p>
Whether it's ``I didn't get it right so I won't output it'', ``I'm going to use silence to connect short spaces'', ``I'm going to put it on hold because the system seems to be broken'', or ``I'm going to stop it because it's dangerous'' are completely different in operational terms. If you combine everything into one "outage", you will not be able to trace the cause during review.
</p>

<h2>The minimum log you want to keep</h2>

<h4>Checklist</h4>
<ul>
<li><strong>loop class: One of</strong>state feedback, ERP/command, speech/streaming, phase-locked, burst-triggered. </li>
<li><strong>end-to-end latency:</strong>Leave median, P95, P99, worst-case separate. </li>
<li><strong>Module-wise latency:</strong> Separate input, inference, output, and recursive input, leaving what is rate-limiting. </li>
<li><strong>Definition of jitter:</strong>Specify SD, IQR, or peak-to-peak. </li>
<li><strong>clock offset / drift: Leave before and after the LSL and hardware marker correction. </li>
<li><strong>Marker verification method:</strong>Write which of TTL, MCU, photodiode, microphone, or loopback was used for actual measurement. </li>
<li><strong>Additional metrics for speech / streaming: </strong>Leave cue-to-output tail latency, audio driver latency, silence / hold-last-output rate, and false speech rate. </li>
<li><strong>Additional metrics for phase/burst systems:</strong>Phase error distribution, missed trigger, burst detection delay, false positive/negative. </li>
<li><strong>Abstain/freeze/safety stop:</strong>Leave the number of activations, previous state, and return conditions. </li>
<li><strong>Longitudinal burden: Record the elapsed time since the last supervised recalibration, presence or absence of unsupervised adaptation, and manpower/time required for recalibration. </li>
<li><strong>naturalistic deployment: leave clinic/home performance difference, eligibility, continuation, programming change, duty cycle. </li>
<li><strong>Performance degradation curve:</strong> Leaves the point at which it collapses when artificially adding delay. </li>
</ul>

<h2>6 questions when reading L3 arguments</h2>
<ol>
<li><strong>Does it say which loop class it deals with?</strong> Check whether slow feedback, speech streaming, phase-locked, and aDBS are mentioned in the same table. </li>
<li><strong>Are there module-wise measurements, not just end-to-end?</strong> Don't just rely on software timestamps, check which of the input, inference, and output paths are rate-limiting. </li>
<li><strong>For speech / streaming, check whether silence and output path are displayed:</strong> Check whether false speech, audio driver, or hold-last-output are hidden. </li>
<li><strong>Is delay mapped to phase error or burst time?</strong> Check to see if it's just a ms value. </li>
<li><strong>Are there recalibration burden and clinic/home metastases?</strong> Check to see if it reads deployable only with within-session success. </li>
<li><strong>Are abstentions, silence fallbacks, freezes, and safety stops separated?</strong> Confirm whether operations in times of danger and times of low reliability are not ambiguous. </li>
</ol>

<h2>References</h2>
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
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nat Neurosci.</em> 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. <em>Nature.</em> 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. <em>Nat Biomed Eng.</em> 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <em>Nat Med.</em> 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. <em>npj Parkinsons Dis.</em> 2026. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
</ol>

<h2>Where to go back next</h2>
<p>
If you want to go back to the overall design of L3, please use <a href="https://mind-upload.com/verification.html">Verification Platform</a>, if you want to go back to EEG and synchronization practices, please use <a href="https://mind-upload.com/eeg_101.html">Introduction to EEG</a>, and if you want to go back to Roadmap I1/I8, please use <a href="https://mind-upload.com/tech_roadmap.html">Technology Roadmap</a>.
</p>
