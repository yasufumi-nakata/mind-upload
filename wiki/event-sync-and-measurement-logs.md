---
layout: default
title: "Wiki: Basics of event synchronization and observation logs"
description: "Explain why raw EEG alone is not enough from the perspectives of event markers, event semantics, time synchronization, manual scoring, and report-derived labels."
article_type: Wiki
subtitle: "Comparisons break down if we don't leave behind the source of the label, not just the signal."
author: Mind Uploading Research Project
last_updated: "2026-03-28"
note: "Practical guide"
audience: "People who have started working with EEG data and want to experience the bare minimum of BIDS and QC"
reading_time: "12-18 minutes"
page_intro: "This page is a wiki that explains why raw EEG waveforms alone are not reproducible in research from the perspectives of event markers, event semantics, time synchronization, manual scoring, and report-derived labels. The purpose is to prevent not only ``waveform files are available but cannot be compared,'' but also ``labels are available but provenance is ambiguous and cannot be compared,'' and ``time is available but clock domain is ambiguous and cannot be compared.''"
accuracy_note: "What we are dealing with here is the minimum observation log and label provenance, but in the 2026-03-28 update, we also clarify the differences in the roles of BIDS event tables, HED semantics, LSL synchronization, physical timing validation, and Motion-BIDS-type metadata. Although each issue requires additional metadata, the principle of keeping events, meanings, clock systems, and timing-validation classes separate remains the same."
page_highlights:
  - "Raw EEG alone may not tell you the signal at the moment of what happened."
  - "Event markers, stimulation logs, and synchronization information may not be restored later."
  - "BIDS's `events.tsv` is a timestamp table, not event semantics by itself."
  - "LSL strengthens intra-LAN synchronization, but does not automatically provide the true value of intra-device delay or stimulus presentation delay."
  - "Stored-data anchors, stream alignment, digital trigger capture, physical output onset, and uncontrolled-response timing are different timing-validation classes."
  - "Cue onset, expert interval, hypnogram, and report-derived label are different even though they are the same labeled data."
  - "Recording bad channels and bad segments is also part of the evidence."
known_points:
  - "Waveform files alone may not be sufficient to reconstruct task and stimulus responses."
  - "If you don't record delays, jitter, and drift, your strengths in temporal resolution will be undermined."
  - "BIDS/EEG-BIDS provides a container for events and metadata, but machine-readable semantics like HED are useful for cross-study reuse."
  - "Even with LSL and trigger lines, time fidelity cannot be audited without specifying the clock domain and device-side delay."
  - "A BIDS onset or sample index does not by itself prove physical display/audio onset, and a digital trigger does not by itself prove uncontrolled response timing."
  - "If you do not write annotation provenance, you may not be able to reuse the same label name."
  - "Recording bad channels/bad segments is directly linked to transparency of exclusions."
unknown_points:
  - "We are still in the process of operational design as to how detailed metadata will be required for all assignments."
  - "How to unify the minimum synchronization log in complex multimodal simultaneous measurements is a future issue."
  - "We still need to adjust how far event semantics should be made mandatory in HED / ontology / scorer rules."
  - "The site-wide schema for how far report-derived labels should be separated from signal-only benchmarks is still being finalized."
wiki_links:
  - label: "Wiki: EEG pretreatment and QC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "Compensate for where the results change after observation."
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Learn why logs are a public good."
  - label: "Wiki: Closed loop, delay, jitter, safe stop"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Compensates for how to read delay and jitter in L3 closed-loop evaluation."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "Returns to the entire learning page."
recommended_pages:
  - label: "Introduction to EEG"
    url: "/eeg_101.html"
  - label: "Data & Bench"
    url: "/datasets.html"
  - label: "Hands-on"
    url: "/datasets.html#l0-practice"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest answer</h2>
<p>
Raw EEG is a sequence of electrical signals. However, what we often want to know in research is ``<strong>When and what signals occur</strong>''. Without that correspondence table, the meaning will be ambiguous even if you look at it later.
</p>
</div>

<div class="note-box">
<strong>Assumptions added in 2026-03 literature audit</strong>
<p>
This page treats not only event logs but also <strong>label provenance</strong> as observation logs. In other words, even if the same "correct label" is used, it will not be a comparable benchmark unless it is written whether it is an <strong>annotation channel</strong>, an <strong>expert's interval annotation</strong>, a <strong>whole-night hypnogram</strong>, or a <strong>label derived from a doctor's report</strong>.
</p>
</div>

<div class="note-box">
<strong>Main weakness this page needed to fix</strong>
<p>
Although the site already stated that events and synchronization matter, it still did not cleanly separate <strong>time anchors</strong>, <strong>event semantics</strong>, and <strong>clock alignment</strong>. BIDS task events provide a descriptive framework through <code>events.tsv</code> and JSON sidecars, but as Robbins et al. (2021) and Hermes et al. (2025) show, cross-study reuse also requires <strong>machine-readable semantics such as HED</strong>. Furthermore, as Kothe et al. (2025) show, LSL can strengthen network synchronization without automatically giving you device-internal delay or stimulus-presentation delay. That is why this site audits event fidelity in three tiers rather than treating it as a single checkbox.
</p>
</div>

<div class="note-box">
<strong>2026-03-28 re-audit: timing evidence still needed a ladder</strong>
<p>
The remaining weakness was that this page could still let a reader treat <strong>BIDS onset/sample fields</strong>, <strong>LSL alignment</strong>, <strong>TTL markers</strong>, <strong>photodiode traces</strong>, and <strong>microphone / loopback tests</strong> as if they were interchangeable proofs of timing. The current standards and primary literature do not support that compression. The BIDS specification defines <code>onset</code> relative to the <strong>first stored data point</strong>, not the physical onset at the screen or speaker. Hermes et al. (2025) shows that HED sharpens machine-actionable semantics, not hardware latency truth. Kothe et al. (2025) shows that LSL can compensate cross-device offsets and jitter, but residual setup offsets must still be tested on the actual instruments. Lepauvre et al. (2024) and Bridges et al. (2020) then show that physical stimulus onset and response timing need external validation because software package, operating system, and hardware combinations can materially shift delay and jitter. Therefore, this site now reads timing evidence as a <strong>validation ladder</strong> rather than one sync checkbox.
</p>
</div>

<section class="section" id="why-raw-is-not-enough">
<h2 class="section-title">Why raw EEG alone is not enough</h2>
<p>
For example, if we do not know how many times a stimulus appeared during a task, at what timing a button was pressed, or which sections were excluded due to noise, different people will interpret the same waveform differently. In other words, if you look only at the waveform, it may not be clear what you are comparing.
</p>
</section>

<section class="section" id="event-markers">
<h2 class="section-title">Event markers and stimulus log</h2>
<table class="data-table">
<thead>
<tr>
<th>Record</th>
<th>What is it needed for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Event marker</strong></td>
<td>Indicates where stimulus presentation, response, state change, etc. correspond to on the waveform. </td>
</tr>
<tr>
<td><strong>Stimulus log</strong></td>
<td>It records which stimuli appeared, in what order, and under what conditions. </td>
</tr>
<tr>
<td><strong>Reaction log</strong></td>
<td>Associate the subject's button presses, answers, failed trials, etc. with the waveform. </td>
</tr>
</tbody>
</table>
<p>
Even if there is only an event marker, if the content of the stimulus or the name of the condition is ambiguous, it will be difficult to reanalyze it. Conversely, just having a stimulus log is not enough unless it is linked to EEG time.
</p>
</section>

<section class="section" id="event-fidelity-layers">
<h2 class="section-title">Event fidelity is audited in three layers</h2>
<table class="data-table">
<thead>
<tr>
<th>layer</th>
<th>What to fix here</th>
<th>Misreading that is likely to occur if missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Time anchor</strong></td>
<td>Correspondence with onset/duration, sample index, clock domain, stimulus/response log. </td>
<td>``When the event happened'' becomes ambiguous, and epoching and delayed evaluation break down. </td>
</tr>
<tr>
<td><strong>2. Event semantics</strong></td>
<td><code>trial_type</code>, condition name, HED tags, manual scoring rule, report usage flag. </td>
<td>Even if the label name is the same, the meaning will be different and cross-study meta/mega analysis will be broken. </td>
</tr>
<tr>
<td><strong>3. Synchronization and transport</strong></td>
<td>Clock offset, delay, jitter, drift, transport path, presence or absence of resampling/smoothing. </td>
<td>If LSL or trigger is just a sub-ms ground truth, it will be easy to misread it. </td>
</tr>
</tbody>
</table>
<p>
BIDS task events primarily provide the <strong>first layer</strong>, HED supplements the <strong>second-layer semantics</strong>, and LSL supports <strong>third-layer network synchronization</strong>. Therefore, this site does not treat these as interchangeable tools.
</p>
</section>

<section class="section" id="timing-validation-ladder">
<h2 class="section-title">Timing validation is a ladder, not one box</h2>
<table class="data-table">
<thead>
<tr>
<th>Validation class</th>
<th>What it directly fixes</th>
<th>What it still does not prove</th>
<th>Typical artifact to keep</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Stored-data anchor</strong></td>
<td>Fixes where an event sits in the saved data file by <code>onset</code>, <code>duration</code>, and optionally <code>sample</code>.</td>
<td>Does not prove physical display/audio onset, device throughput delay, or participant response timing.</td>
<td><code>events.tsv</code>, <code>events.json</code>, acquisition start definition, discarded-sample rule.</td>
</tr>
<tr>
<td><strong>Stream alignment</strong></td>
<td>Fixes cross-device clock offset, drift, and network-jitter handling across synchronized streams.</td>
<td>Does not prove the true latency of displays, speakers, amplifiers, or buttons.</td>
<td>LSL/XDF log, clock domain, offset / RTT summary, resync policy.</td>
</tr>
<tr>
<td><strong>Acquisition-side digital marker capture</strong></td>
<td>Fixes when a trigger pulse reached the acquisition system or DAQ input.</td>
<td>Does not prove when the stimulus actually became visible/audible or when the participant actually responded.</td>
<td>TTL or marker trace, DAQ channel, trigger wiring map, marker-to-stream relation.</td>
</tr>
<tr>
<td><strong>Physical output onset</strong></td>
<td>Fixes the real-world onset and duration of a visual or auditory event at the actuator.</td>
<td>Does not prove subjective perception time, neural processing latency, or response-device timing.</td>
<td>Photodiode trace, microphone trace, audio loopback, high-speed-camera or equivalent setup note.</td>
</tr>
<tr>
<td><strong>Uncontrolled-response timing</strong></td>
<td>Fixes the gap between the logged response timestamp and the actual button / key / actuator response.</td>
<td>Does not prove stimulus onset timing or internal cognitive latency.</td>
<td>Contact microphone, force sensor, loopback, response-box validation log.</td>
</tr>
</tbody>
</table>
<p>
On this site, a submission has to name the <strong>highest rung actually tested</strong>. Saying “we used BIDS” fixes the stored-data anchor. Saying “we used LSL” fixes stream alignment. Saying “we sent TTL markers” fixes acquisition-side digital capture. Claims about <strong>physical stimulus onset</strong> or <strong>true response timing</strong> require an external measurement rung such as photodiode, microphone, or loopback.
</p>
</section>

<section class="section" id="label-provenance">
<h2 class="section-title">Read the origins of labels in four different ways</h2>
<table class="data-table">
<thead>
<tr>
<th>Label type</th>
<th>Representative examples</th>
<th>What it directly represents</th>
<th>Minimum auxiliary log that should be kept</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cue-locked annotation channel</strong></td>
<td>EEG Motor Movement/Imagery T0 / T1 / T2</td>
<td>The design timing of the issue cue and motion/imagery onset. </td>
<td>Leave run ID, task ID, subject ID, visual cue condition, and epoching rule. </td>
</tr>
<tr>
<td><strong>expert interval annotation</strong></td>
<td>CHB-MIT seizure onset / offset</td>
<td>This is the event section during long-term recording. </td>
<td>Leave file order, gap, case-to-subject support, montage changes. </td>
</tr>
<tr>
<td><strong>manual hypnogram</strong></td>
<td>Sleep-EDF's R&K sleep stage</td>
<td>This is the coarse state label of whole-night. </td>
<td>Leave scoring manual, scorer ID, night / study conditions, and label mapping. </td>
</tr>
<tr>
<td><strong>report-derived / triaged label</strong></td>
<td>TUH EEG / TUSZ report keyword search and clinician report</td>
<td>Clinical label and triage information attached to session/file. </td>
<td>Leave report usage flag, patient / session ID, signal-only or multimodal declaration. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="timing">
<h2 class="section-title">Three things to look for in time synchronization</h2>
<table class="data-table">
<thead>
<tr>
<th>Term</th>
<th>Meaning</th>
<th>What is the problem</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Delay</strong></td>
<td>How many ms is the difference between the actual event and the record? </td>
<td>The time of the post-stimulus response is shifted, leading to incorrect interpretation. </td>
</tr>
<tr>
<td><strong>Jitter</strong></td>
<td>How much does the deviation fluctuate each time? </td>
<td>Averaging will blur the peaks and make the response appear weaker. </td>
</tr>
<tr>
<td><strong>Drift</strong></td>
<td>The clock lag increases over a long period of time. </td>
<td>The later the time, the greater the synchronization error becomes. </td>
</tr>
</tbody>
</table>
<p>
This section explains the meaning of the observation log. If you want to see how these affect end-to-end stability and safe stopping in L3 closed-loop evaluation, <a href="closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed-loop, delay, jitter, and safe stopping</a> is a supplementary lesson.
</p>
</section>

<section class="section" id="lsl-scope">
<h2 class="section-title">LSL is powerful, but not hardware ground truth</h2>
<p>
The Lab Streaming Layer (LSL) is extremely useful as a foundation for synchronizing multiple streams within the same LAN and consistently handling clock offsets and stream metadata. Kothe et al. (2025) showed that LSL can achieve millisecond precision with software-based synchronization. However, the same paper also makes clear that <strong>the input device's throughput delay and on-device processing delay cannot be estimated or corrected by LSL alone</strong>. Therefore, even if LSL is used, display delay, audio delay, and amplifier buffer delay must still be measured separately.
</p>
<table class="data-table">
<thead>
<tr>
<th>Things you should leave behind even if you are using LSL</th>
<th>Reason</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>timestamp domain</strong></td>
<td>If you do not write whether it is based on the presentation PC, acquisition PC, or device clock, the meaning of the time difference will be lost. </td>
</tr>
<tr>
<td><strong>device-side delay</strong></td>
<td>The internal delays of the amplifier, display, audio output, and microcontroller cannot be determined by software timestamp alone. </td>
</tr>
<tr>
<td><strong>drift / resync policy</strong></td>
<td>In long-term recording, the alignment error in the second half changes depending on whether or not drift correction is applied. </td>
</tr>
<tr>
<td><strong>validation method</strong></td>
<td>You need to know which method you used to estimate the delay, such as photodiode, loopback, TTL, or common signal input. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="starter-dataset-logging">
<h2 class="section-title">What to log with the 4 starter datasets</h2>
<div class="note-box">
<strong>The last column is the operational reasoning for this site</strong>
<p>
The <strong>what not to overread</strong> column below marks the operational boundary that this site draws from the logging granularity directly described in official dataset documentation and primary literature.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Dataset</th>
<th>Current logging</th>
<th>Additional details to preserve</th>
<th>What not to overread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td><code>.event</code> and the annotation channel record cue-locked onset with T0 / T1 / T2 tags. </td>
<td>Keep subject, run, task block, epoching window, and EOG / EMG audit results. </td>
<td>Do not read this cue-locked motor task as spontaneous thought readout. </td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>The summary and <code>.seizure</code> annotations preserve seizure intervals, case structure, file gaps, and surrogate dates. </td>
<td>Keep case-to-subject linkage, gap length, whether recording is continuous, and montage summaries. </td>
<td>Do not treat each file as an independent sample or read the dataset as a gap-free monitoring log. </td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>The dataset includes an R&amp;K hypnogram, Fpz-Cz / Pz-Oz EEG, and a 1 Hz event marker. </td>
<td>Keep the scoring manual, scorer, study arm, night ID, and any mapping rules to AASM labels. </td>
<td>Do not claim sub-second sleep-event timing simply because the EEG itself is sampled at 100 Hz. </td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>Depending on the subset, the dataset includes patient / session hierarchy, EDF, clinician reports, and expert seizure annotation. </td>
<td>Keep report-usage flags, patient / session splits, and any report-keyword-derived triage. </td>
<td>Do not write report-assisted clinical labels as pure EEG signal-only results. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="bad-records">
<h2 class="section-title">Why leave bad channel / bad segment</h2>
<p>
It is normal to exclude channels with large noise or sections broken by body movement. However, without that record, another person cannot reproduce the same exclusion later.
</p>
<div class="key-points">
<h4>What you want to keep as a minimum</h4>
<ul>
<li><strong>bad channel:</strong>Which channel was marked bad and for what reason? </li>
<li><strong>bad segment:</strong>Which time segment did you exclude? </li>
<li><strong>Threshold:</strong>What criteria were used to exclude it? </li>
<li><strong>How to fix:</strong>Did you interpolate or discard? </li>
</ul>
</div>
</section>

<section class="section" id="bids">
<h2 class="section-title">Minimum information required for EEG-BIDS</h2>
<table class="data-table">
<thead>
<tr>
<th>Item</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>`events.tsv`</strong></td>
<td>Leaves the time and type of stimulus and response. </td>
</tr>
<tr>
<td><strong>`events.json` and HED</strong></td>
<td>Explain the meaning of <code>trial_type</code> and other columns, and optionally make event semantics machine-readable with HED tags. </td>
</tr>
<tr>
<td><strong>`channels.tsv`</strong></td>
<td>Leave the status and type of each channel. </td>
</tr>
<tr>
<td><strong>JSON metadata</strong></td>
<td>Leave the sampling frequency, reference method, measurement conditions, etc. </td>
</tr>
<tr>
<td><strong>clock / sync log</strong></td>
<td>Clock domain, delay, jitter, drift, synchronization method, and measurement method are recorded in separate logs. </td>
</tr>
<tr>
<td><strong>`*_coordsystem.json` and extended schema</strong></td>
<td>When using electrodes, motion sensors, or pose streams, leave the coordinate system and measurement arrangement as first-class metadata. </td>
</tr>
<tr>
<td><strong>QC / Exclusion Log</strong></td>
<td>Leave bad channels, bad segments, noise, and exclusion reasons in external logs and derivatives. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="event-fidelity-card">
<h2 class="section-title">Event Fidelity Card required on this site</h2>
<p>
As of the 2026-03-28 site rule, dataset cards and runbooks that contain events must include at least the following six items. The point is not to wait until everything is perfect, but to make missing pieces visible and define where claims must stop.
</p>
<table class="data-table">
<thead>
<tr>
<th>Item</th>
<th>Minimum details to include</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Event anchor</strong></td>
<td>Onset / duration / sample, source file, and the clock domain to which the time refers. </td>
</tr>
<tr>
<td><strong>2. Event semantics</strong></td>
<td><code>trial_type</code>, condition definitions, HED or an equivalent vocabulary, and whether semantics come from signal-only annotation or manual scoring / reports. </td>
</tr>
<tr>
<td><strong>3. Clock domain and stream alignment</strong></td>
<td>Name the clock domain, synchronization middleware if any, offset / drift handling, and resynchronization policy. </td>
</tr>
<tr>
<td><strong>4. Timing validation class</strong></td>
<td>Name whether timing evidence comes from stored-data anchor only, digital marker capture, physical output onset, or uncontrolled-response testing, together with measured delay / jitter summary and the measurement method. </td>
</tr>
<tr>
<td><strong>5. Provenance</strong></td>
<td>Scorer ID, scoring manual, report-usage flag, and whether the label is signal-only or multimodal. </td>
</tr>
<tr>
<td><strong>6. Geometry / multimodal metadata</strong></td>
<td>Electrode coordinates, coordinate system, and the frame plus schema of any additional motion, video, or physiology streams. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="cannot-recover">
<h2 class="section-title">Information that is difficult to restore later</h2>
<p>
If you do not record the following information, you will have to guess it later.
</p>
<ul>
<li><strong>Exact time of stimulus presentation:</strong>Rough order cannot be substituted. </li>
<li><strong>Clock domain:</strong>If you do not state which clock a timestamp belongs to, you cannot interpret differences across multiple streams. </li>
<li><strong>Timing validation class:</strong>If you do not say whether a number comes from stored-data anchor, TTL, photodiode, microphone, or loopback, sync evidence becomes impossible to interpret. </li>
<li><strong>Actual delay and jitter:</strong> Sometimes equipment and software settings are not enough. </li>
<li><strong>Device-side delay:</strong>Even if you use LSL or trigger, you need to measure the internal delay of the display, audio, and amplifier separately. </li>
<li><strong>Reason for exclusion:</strong>Even if you look back on it, you won't know why you threw it away. </li>
<li><strong>Label provenance:</strong>If you do not record whether a label came from manual scoring or a report-derived rule, you cannot compare it safely even when the label name is the same. </li>
<li><strong>Event semantics: </strong>If there is no meaning of <code>trial_type</code>, condition name, or HED tags, the same name may be different conditions. </li>
<li><strong>scoring manual / scorer:</strong>Manual hypnograms like Sleep-EDF change their meaning for reuse when they lose their reference and scorer. </li>
<li><strong>report usage flag:</strong>In TUH-style datasets, you otherwise cannot tell later whether a label depended on reports or came from signal-only processing. </li>
<li><strong>Coordinate system and sensor frame:</strong> Adding motion and pose but not leaving frame makes multimodal integration non-reusable. </li>
<li><strong>On-the-spot operational notes:</strong> Electrode troubles and synchronization errors cannot be read from the waveform alone. </li>
</ul>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS Specification: Events</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS Specification: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021), Building FAIR functionality: annotating events in time series data using HED</a></li>
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025), HED library schema for EEG data annotation</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00136" target="_blank">Kothe et al. (2025), The lab streaming layer for synchronized multimodal recording</a></li>
<li><a href="https://doi.org/10.3758/s13428-024-02508-y" target="_blank">Lepauvre et al. (2024), A standardized framework to test event-based experiments</a></li>
<li><a href="https://doi.org/10.7717/peerj.9414" target="_blank">Bridges et al. (2020), The timing mega-study: comparing a range of experiment generators, both lab-based and online</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024), Motion-BIDS</a></li>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), The Temple University Hospital EEG Data Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), The Temple University Hospital Seizure Detection Corpus</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009), Sleep classification according to AASM and Rechtschaffen &amp; Kales</a></li>
</ul>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
Please use <a href="../eeg_101.html">Introduction to EEG</a> to return to the role of EEG as a whole, <a href="../datasets.html">Data & Bench</a> to return to selecting starter data, and <a href="../datasets.html#l0-practice">Hands-on</a> to return to the minimal loop procedure.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-preprocessing-and-qc.html">EEG preprocessing and QC →</a></li>
<li><a href="measurement-and-modeling-terms.html">From measurement to modeling →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html">Introduction to EEG →</a></li>
<li><a href="../datasets.html">Data & Bench →</a></li>
<li><a href="../datasets.html#l0-practice">Hands-on →</a></li>
</ul>
</div>
</aside>
</main>
