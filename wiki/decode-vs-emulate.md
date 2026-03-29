---
layout: default
title: "Wiki: Decode and Emulate"
description: "Explains the difference between decoding, which translates observations, and emulation, which reproduces internal causality, using primary literature and the evidence required for each claim."
article_type: Wiki
subtitle: "Output matching is only the entrance; intervention matching and closed-loop stability are another wall."
author: Mind Uploading Research Project
last_updated: "2026-03-30"
note: "Technical / natural science only"
audience: "People who want to distinguish decode from emulate using only technical and natural-science evidence."
reading_time: "10-15 minutes"
page_intro: >
  This page is an auxiliary guide that organizes the difference between decode and emulate,
  one of the key distinctions in Mind-Upload, on the basis of primary literature. It separates
  a high-performance translator from a system that moves internal states by using observation,
  intervention, and closed-loop evidence.
accuracy_note: >
  What is presented here are technical boundary conditions. This page does not provide a final
  agreement on sufficient conditions, nor a sole determination of success, for WBE as a whole.
page_highlights:
  - "Decode assigns a label or sentence from an observation; emulate includes the temporal evolution of internal states and their responses to interventions."
  - "d'Ascoli 2025 and Tang 2023 pushed the frontier of non-invasive decoding, but they do not establish unrestricted thought reading or state reconstruction."
  - "Littlejohn 2025 and Wairagkar 2025 are major advances in streaming and voice-synthesis neuroprostheses, but they are L2-L3 evidence for the communication subsystem, not whole-brain emulation."
  - "As Chen 2024 showed, offline gain mixed with non-causal decoders and post-onset auditory feedback should not be interpreted as real-time deployability."
  - "Same-session streaming success and chronic deployability are separate evidence classes, and they require separate logging of fixed decoder intervals, recalibration burden, and same-neuron audits."
  - "Connectome-constrained prediction is important, but as Beiran & Litwin-Kumar 2025 shows, parameter degeneracy and unmeasured conditions remain."
  - "Same-brain functional connectomics and digital-twin language are now split into sequential local scaffolds, stimulus-conditioned predictors, and dynamical-degeneracy audits rather than one solved local twin."
known_points:
  - "Decode is mainly an L1 claim, while local closed-loop performance and intervention responses are closer to L2-L3."
  - "Output matching alone does not establish internal causal structure or the sufficiency of state variables."
  - "Non-invasive decoding is easy to overestimate unless language priors, candidate sets, and subject cooperation are separated."
  - "With speech decoding, if causal versus non-causal paths, look-ahead windows, and auditory-feedback contamination are not separated, offline scores are easy to misread as deployable loops."
  - "Tail latency, silence/abstention, and recalibration burden are separate axes from offline accuracy and are required logs for closed-loop claims."
  - "In microelectrode systems, the same neuron across days is not an observed fact, but an estimate built from motion correction, sorting, and probabilistic matching."
unknown_points:
  - "It is unclear how much intervention matching and state-variable completeness is required to count as sufficiently emulated."
  - "There is still no public benchmark for extrapolating from local-circuit successes to whole-brain emulation."
  - "It is unclear how much same-brain function and maintenance-state must be added to connectome-constrained models to constrain degeneracy sufficiently."
wiki_links:
  - label: "Wiki: How to read claims and evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "Return to L0-L5 claim strength and the evidence required for each level."
  - label: "Wiki: Why wiring diagrams alone are not enough"
    url: "/wiki/connectome-is-not-enough.html"
    description: "Clarifies what remains missing at the level of state completeness."
  - label: "Wiki: Closed loop, delay, jitter, safe stop"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Adds the end-to-end conditions required for L3 claims."
  - label: "Wiki: state / trait / drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Explains how to read drift and recalibration burden in cross-day and chronic claims."
recommended_pages:
  - label: "WBE 101"
    url: "/wbe_101.html"
  - label: "Verification"
    url: "/verification.html"
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>First of all, the conclusion in one word</h2>
<p>
Decode means ``to infer something from an observed signal,'' and emulate means ``the internal state evolves over time and responds consistently to changes in conditions or interventions.'' Even if the visual outputs are similar, it does not necessarily mean that they are<strong>operating by the same causal mechanism</strong>.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. From only the aspects of technology and natural science, we will clarify the conditions under which decode can be read as emulate.
</p>
</div>

<div class="note-box">
<strong>2026-03 Points revised in literature audit</strong>
<p>
The weakness of the previous version is that while the principle difference between decode and emulate was correct, it did not reach the level of <strong>site rule</strong> to stop <strong>open-vocabulary non-invasive decode</strong>, <strong>streaming / voice-synthesis neuroprosthesis</strong>, and <strong>connectome-constrained prediction</strong>, which were promoted in the primary literature of 2025. This update promotes <strong>language prior</strong>, <strong>tail latency / silence / recalibration burden</strong>, <strong>fixed decoder interval</strong>, <strong>same-neuron tracking audit</strong>, and <strong>parameter degeneracy</strong> to mandatory audit items at the decode/emulate boundary.
</p>
</div>

<section class="section" id="simple-table">
<h2 class="section-title">The shortest difference</h2>
<table class="data-table">
<thead>
<tr>
<th>Viewing Points</th>
<th>Decode</th>
<th>Emulate</th>
<th>Minimum required verification</th>
</tr>
</thead>
<tbody>
<tr>
<td>What to reproduce</td>
<td>Infer states, stimuli, meanings, motor intentions, etc. from observations. </td>
<td>Internal states evolve over time and produce future outputs and intervention responses. </td>
<td>Evaluate not only supervised prediction accuracy but also time evolution and condition changes. </td>
</tr>
<tr>
<td>Strengths</td>
<td>It is easy to achieve high performance under the observed conditions, and it is easy to connect directly to practical BCI. </td>
<td>A stronger case can be made for intervention, counterfactuals, and closed-loop control. </td>
<td>OOD generalization, perturbation matching, and closed-loop stability are evaluated separately. </td>
</tr>
<tr>
<td>Misreadings that will increase in 2025</td>
<td>It is easy to read open-vocabulary word decode and streaming voice output as "free thinking mind reading" or "internal reproduction". </td>
<td>It is easy to read connectome-constrained prediction and local closed loop as evidence of whole-brain emulation. </td>
<td>LM-only / no-brain / shuffle baseline, subsystem scope, and state completeness are issued at the same time. </td>
</tr>
<tr>
<td>Misreading when insufficient</td>
<td>It is easy to translate correlative translation into "internal reproduction". </td>
<td>It is easy to misread it as "faithful reproduction" just by matching the output. </td>
<td>Separately audits the completeness and identifiability of state variables. </td>
</tr>
<tr>
<td>Typical failure modes</td>
<td>Even if the accuracy is high within a subject or within a task, it will collapse under unlearning conditions or on a different day. </td>
<td>Even if the behavior seems to match, different internal parameters may produce the same output. </td>
<td>Disclose the division unit, number of recalibrations, post-intervention error, and abstention conditions. </td>
</tr>
<tr>
<td>Minimum log to keep</td>
<td>candidate set, presence or absence of LM, subject cooperation, proofreading and abstention rate, and cross-day degradation. </td>
<td>Perturbation log, P50/P95/P99 latency, silence/abstention, recalibration burden, residuals of latent state. </td>
<td>Leave speed, accuracy, stability, and hidden state as separate columns. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="paper-normalization">
<h2 class="section-title">2026-03-17 Addendum: Arrange representative papers in the same coordinate system</h2>
<p>
One area where there was a lot of room for improvement with the current site was that representative papers showing natural text/voice output could easily be compared on the same axis. However, looking at the primary literature, semantic reconstruction of perceived / imagined content, known-onset word decoding, prompt-conditioned language continuation, attempted speech communication, and streaming voice synthesis are all different in training depth, subject route, prior scaffold, and time axis. Therefore, on this page we normalize the main papers into a single comparison table, fixing what is directly shown and what is not yet shown.
</p>
<table class="data-table">
<thead>
<tr>
<th>Representative paper</th>
<th>Signals and issues</th>
<th>Limitations directly shown by primary literature</th>
<th>ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tang et al. (2023)</strong><br>semantic reconstruction</td>
<td>Reconstruct the semantic representation of perceived speech / imagined speech / silent video from fMRI. </td>
<td>Within-subject, the recovered time-points reached 65-82%, but with cross-subject, it remained at 1-5%, and the learning gain also plateaued at about 7.5 hours. Countermeasures like counting by sevens and naming animals reduced recovery to 0-50%. </td>
<td>Subject-cooperative task-limited semantic reconstruction. It will not be promoted to subject-free thought reader or unrestricted mental-state readout. </td>
</tr>
<tr>
<td><strong>Défossez et al. (2023)</strong><br>speech-segment retrieval from M/EEG</td>
<td>Identify the correct 3 s speech segment from non-invasive M/EEG recorded while participants passively listened to natural speech. </td>
<td>The route decoded perceived speech segments from more than 1,000 possibilities with much stronger performance in MEG than EEG, and the model predictions primarily tracked lexical and contextual semantic representations. It still depended on a fixed candidate bank of speech segments at test time. </td>
<td>Candidate-bank segment retrieval for perceived speech. It will not be promoted to free-form generation, production decode, or unrestricted thought reading. </td>
</tr>
<tr>
<td><strong>d'Ascoli et al. (2025)</strong><br>open-vocabulary word decoding</td>
<td>Estimating word identity under known word onset from M/EEG of 723 people and 5 million words. </td>
<td>With the design using sentence-level context, performance was strongly dependent on additional training data, test averaging, MEG &gt; EEG, and reading &gt; listening. Therefore, even with "open-vocabulary", task structure and modality advantage remain. </td>
<td>Open-vocabulary word decode with known-onset and perception-heavy conditions. I will not promote it to free thought reading or unrestricted language generation. </td>
</tr>
<tr>
<td><strong>Ye et al. (2025)</strong><br>generative language reconstruction + LLM</td>
<td>Feed fMRI-derived representations and a text prompt into an autoregressive LLM to generate a continuation rather than rerank a fixed candidate list. </td>
<td>BrainLLM beat a permuted-brain control across three fMRI datasets, but performance still depended on prompt length, LLM size, and data volume; no-prompt generation remained harder by language-similarity metrics even when brain input helped relative to the control. </td>
<td>prompt-conditioned generative language reconstruction. It does not advance to brain-only text generation or hidden-state recovery. </td>
</tr>
<tr>
<td><strong>Willett et al. (2023)</strong><br>high-performance speech neuroprosthesis</td>
<td>Decodes attempted speech from intracortical array and returns large vocabulary text output. </td>
<td>With a vocabulary of 125,000 words, we achieved 62 words/min and 23.8% WER for attempted speech decoding of a participant-specific invasive route. </td>
<td>It is a high-bandwidth communication subsystem. It does not promote semantic autonomy or whole-brain state reconstruction. </td>
</tr>
<tr>
<td><strong>Littlejohn et al. (2025)<br>Wairagkar et al. (2025)</strong><br>streaming brain-to-voice / instantaneous voice synthesis</td>
<td>Synthesize a voice similar to own-voice from the invasive signal using streaming / low-latency. </td>
<td>Littlejohn showed streaming brain-to-voice every 80 ms, and Wairagkar showed less than 10 ms inference and silence fallback. On the other hand, in Wairagkar, the decoder fixed on post-implant day 165 deteriorated significantly after about 15 days. </td>
<td>Invasive communication route from same-session to short-horizon. Chronic deployability or long-term stability of a fixed decoder is not claimed without a Temporal Validity Card. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Why do we need this table</strong>
<p>
Even if the "natural language output" looks the same, <strong>semantic reconstruction</strong>, <strong>candidate-bank segment retrieval</strong>, <strong>known-onset word decode</strong>, <strong>prompt-conditioned continuation</strong>, <strong>attempted speech communication</strong>, and <strong>streaming voice synthesis</strong> are different routes. If we do a side-by-side comparison without separating these areas, it is easy to misinterpret deep single-subject fMRI, broad multi-subject M/EEG, participant-specific invasive BCI, and generation systems with LLM scaffold as evidence of the same strength. Therefore, on this site, when looking at natural sentence output, we first return <strong>task regime</strong>, <strong>training depth / subject route</strong>, <strong>prior scaffold</strong>, and <strong>fixed decoder horizon</strong>, and read it based on the type of evidence rather than the flashiness of the medium.
</p>
</div>
</section>

<section class="section" id="chronic-communication-ceiling">
<h2 class="section-title">2026-03-17 Addendum: chronic ceiling of invasive communication route</h2>
<table class="data-table">
<thead>
<tr>
<th>Wall</th>
<th>What the primary literature now supports</th>
<th>How to read this page</th>
<th>Claims not raised yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>same-session streaming ceiling</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> is streaming brain-to-voice, <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> advances instantaneous voice synthesis and silence fallback. </td>
<td>Read as evidence of strong L2-L3 communication subsystem. </td>
<td>We do not claim long-term retention or chronic deployability of fixed decoders. </td>
</tr>
<tr>
<td><strong>recalibration ceiling</strong></td>
<td><a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> tested one-month unsupervised recalibration and <a href="https://doi.org/10.1038/s42003-024-06784-4" target="_blank">Pun et al. (2024)</a> showed that chronic human intracortical recording instability is strongly associated with decreased BCI performance. </td>
<td>As long as <code>time since last supervised calibration</code>, recovery time, and recalibration burden are recorded in separate logs, it can be read as a preliminary step toward long-term operation. </td>
<td>We do not write that "it worked on that day" as "it held true over a long period of time without recalibration." </td>
</tr>
<tr>
<td><strong>same-neuron tracking ceiling</strong></td>
<td><a href="https://doi.org/10.1126/science.abf4588" target="_blank">Steinmetz et al. (2021)</a> is stable recording with motion correction, <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">Pachitariu et al. al. (2024)</a> advanced sorting centered on drift / split / merge, and <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">van Beest et al. (2025)</a> advanced probabilistic cross-day neural tracking. </td>
<td>In the microelectrode system, the same-neuron claim is read as an estimate with <code>sorting version + drift correction + unit-match probability</code>. </td>
<td>Successful chronic decoding cannot be written as direct reading of a stable single-neuron mechanism. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Practical rules for this section</strong>
<p>
When promoting invasive speech BCI to a higher level, we will not only consider same-day streaming performance, but also <strong>how many days the fixed decoder lasts</strong>, <strong>how much it relies on manual recalibration</strong>, <strong>how did we estimate same-neuron tracking for microelectrode systems</strong>, and <strong>how did we audit the implant age / material / geometry / tissue-response proxy</strong>. For a long background, see <a href="state-trait-and-drift.html">Wiki: state, trait, drift</a>.
</p>
</div>
</section>

<section class="section" id="speech-decode-scaffolds">
<h2 class="section-title">2026-03-17 Addendum: 4 scaffolds that make it easy to expand speech decode</h2>
<table class="data-table">
<thead>
<tr>
<th>Scaffold</th>
<th>What the primary literature now supports</th>
<th>How to read this page</th>
<th>Claims not raised yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>task / vocabulary scaffold</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> advanced open-vocabulary word decoding, but also showed that performance changes significantly depending on word onset, task structure, modality, amount of training data, and test averaging. </td>
<td>Read as an advance in conditional language/communication decoding. </td>
<td>I will not post it as free thought reading or state-complete reconstruction. </td>
</tr>
<tr>
<td><strong>causal / non-causal scaffold</strong></td>
<td><a href="https://doi.org/10.1038/s42256-024-00837-5" target="_blank">Chen et al. (2024)</a> showed that in 48-participant EEG speech decoding, an offline non-causal model can boost performance using post-onset auditory feedback, while a real-time causal model can boost performance. We have shown that model has stricter constraints. </td>
<td>Read offline retrospective decode and causal real-time route separately. </td>
<td>Offline gain with look-ahead cannot be directly written as deployable streaming loop. </td>
</tr>
<tr>
<td><strong>transfer / adaptation scaffold</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a> advanced transfer learning of phonemic speech decoding with a group-derived decoder with distributed minimally invasive recordings, but shared task structure and speech network coverage are still prerequisites. </td>
<td>Read as decode engineering to boost clinical scalability. </td>
<td>I will not promote zero-shot as a general thought decoder or subject-free universal reader. </td>
</tr>
<tr>
<td><strong>LLM / prompt scaffold</strong></td>
<td><a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">Ye et al. (2025)</a> generated text continuations by inputting fMRI-derived expressions into a prompt and large language model. </td>
<td>Read as prompt-conditioned generative language reconstruction. </td>
<td>Do not directly equate output fluency with brain-only reconstruction or hidden-state recovery. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Critiques of this section</strong>
<p>
A common misinterpretation of current news and demonstrations is to interpret the four advances of <strong>natural output</strong>, <strong>large vocabulary</strong>, <strong>effective transfer learning</strong>, and<strong>LLM documentation</strong> as ``we were able to read the internal state of the brain fairly directly.'' However, what primary literature directly supports is the advancement of decode engineering to the extent that task scaffolding, causal deployment conditions, adaptation routes, and language prior are clearly specified, not the state completeness itself required for WBE.
</p>
</div>
</section>

<section class="section" id="paper-ladder">
<h2 class="section-title">Boundary cases seen in primary literature</h2>
<table class="data-table">
<thead>
<tr>
<th>Example</th>
<th>What we have achieved now</th>
<th>Why not just emulate</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tang et al. (2023)</strong><br>non-invasive semantic decoding</td>
<td>We showed semantic recovery of continuous language from fMRI and demonstrated decoding across perceived speech, imagined speech, and silent video. </td>
<td>Subject cooperation is required for both learning and application, and translation of the observed semantic representation. We do not demonstrate internal causal structure or replication of intervention responses. </td>
</tr>
<tr>
<td><strong>Défossez et al. (2023)</strong><br>non-invasive speech-segment retrieval</td>
<td>Three-second speech segments were identified from non-invasive MEG/EEG while participants passively listened to natural speech, with much stronger performance in MEG than EEG. </td>
<td>This is evidence for candidate-bank retrieval of perceived speech segments, not for unrestricted word-level or sentence-level generation without a fixed comparison bank. </td>
</tr>
<tr>
<td><strong>d'Ascoli et al. (2025)</strong><br>open-vocabulary non-invasive word decoding</td>
<td>We advanced individual word decoding from non-invasive recordings with 723 people and showed that the amount of training data, test averaging, modality, and task dependence greatly affect performance. </td>
<td>Although this is an advance in open-vocabulary, dependence on word onset, task structure, and participant conditions remains. The progress here is in decoding the communication route, not in state-complete reconstruction. </td>
</tr>
<tr>
<td><strong>Chen et al. (2024)</strong><br>EEG speech decoding with causal / non-causal comparison</td>
<td>We compared speech decoding using EEG of 48 participants and clarified the difference in the apparent gain of the acausal model and the constraints of the causal path for real-time. </td>
<td>This is primary evidence for separating offline retrospective score and deployable real-time route, but it does not indicate general thought reading. </td>
</tr>
<tr>
<td><strong>Singh et al. (2025)</strong><br>transfer learning with distributed brain recordings</td>
<td>Using distributed minimally invasive recordings, they show that a group-derived decoder improves the reliability of phonemic speech decoding. </td>
<td>It is an advance in transfer learning that assumes a shared task structure and calibration route, rather than a subject-free universal decoder. It does not directly lead to WBE internal state identification or unrestricted decoding. </td>
</tr>
<tr>
<td><strong>Willett et al. (2023)</strong><br>invasive speech BCI</td>
<td>Large-vocabulary speech decoding of 62 words/min was demonstrated with a vocabulary of 125,000 words from the intracortical array. </td>
<td>Even at high bandwidth, the main focus is on decoding attempted speech. It does not show autonomous internal generation or causal agreement with changing conditions. </td>
</tr>
<tr>
<td><strong>Littlejohn et al. (2025) / Wairagkar et al. (2025)</strong><br>streaming brain-to-voice / voice synthesis</td>
<td>Littlejohn et al. showed streaming brain-to-voice every 80 ms, and Wairagkar et al. showed sub-10 ms inference, silence fallback, and short horizon of a fixed decoder for a neural-to-voice algorithm. </td>
<td>This is strong L2-L3 evidence of a communication subsystem, but not whole-brain emulation. In addition to speed, long-term deployability cannot be determined unless it also provides tail latency, dropout, silence/false speech, recalibration burden, and fixed decoder horizon. </td>
</tr>
<tr>
<td><strong>Ye et al. (2025)</strong><br>generative language reconstruction + LLM</td>
<td>fMRI-derived brain representations and text prompts were combined inside an autoregressive LLM to generate language continuations. </td>
<td>This is an advance in generative language interfaces, but the fluency of the output still depends strongly on prompt and LLM scaffold, and no-prompt generation remains harder. From here, you cannot immediately proceed to brain-only reconstruction or emulation. </td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong><br>bidirectional closed-loop BCI</td>
<td>By returning tactile feedback to motor decode, the time required for the robot grasp task was reduced from 20.9 seconds to 10.2 seconds. </td>
<td>This is a locally closed loop demonstration that is even stronger than decode, but it targets the sensorimotor subsystem. Rather than whole-brain emulation, it is appropriate to read this as <strong>evidence close to L3 in local circuits</strong>. </td>
</tr>
<tr>
<td><strong>MICrONS (2025) / Billeh et al. (2020) / Beiran &amp; Litwin-Kumar (2025)</strong><br>stimulus-conditioned digital twin / connectome-constrained model</td>
<td>Sequential same-brain connectomics datasets, multiscale models, and connectome-constrained recurrent networks have advanced local conditional prediction under named tasks and recordings. </td>
<td>This is an important foundation in a direction similar to emulate, but the scope remains local and regime-bounded. Furthermore, as MICrONS (2025), Beiran &amp; Litwin-Kumar (2025), and Prinz et al. (2004) show, output matching alone cannot be said to be faithful reproduction or the only solution because degeneracy remains, including unmeasured parameters, unrecorded neurons, and omitted state families. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="audit-2026-03">
<h2 class="section-title">2026-03 Literature audit: 4 alternative readings prohibited here</h2>
<table class="data-table">
<thead>
<tr>
<th>Dangerous transliteration</th>
<th>Why is it dangerous</th>
<th>Boundaries currently supported by primary literature</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>open-vocabulary non-invasive decode → unrestricted thought reading</strong></td>
<td>The word decoding in 2025 is certainly a step forward, but it is strongly influenced by task structure, candidate sets, participant cooperation, and modality differences. </td>
<td>What can be said relatively strongly from Tang (2023) and d'Ascoli (2025) is that <strong>conditional language / communication decoding</strong> has progressed. From there, it is not possible to go directly to general unique restoration of internal states or retrieval of WBE-required states. </td>
</tr>
<tr>
<td><strong>streaming speech neuroprosthesis → emulate / WBE</strong></td>
<td>Streaming and voice synthesis are great achievements of the communication subsystem, but being able to speak quickly and having internal causality are two different things. </td>
<td>Littlejohn (2025) and Wairagkar (2025) pushed the <strong>L2-L3 of the invasive communication route</strong>, and as Wilson (2025) shows, long-term recalibration burden is another barrier. </td>
</tr>
<tr>
<td><strong>non-causal offline gain → deployable real-time loop</strong></td>
<td>Decoders that can use future context or post-onset auditory feedback can have an advantage over causal decoders that can be used in closed loops. </td>
<td>What we can say relatively strongly from Chen (2024) is that <strong>real-time claims cannot be made unless the causal path is reported separately.</strong> </td>
</tr>
<tr>
<td><strong>connectome-constrained prediction → unique internal mechanism</strong></td>
<td>Even if a connectome or same-brain function is included, internal dynamics can degenerate if unmeasured biophysical parameters and hidden states remain. </td>
<td>What can be said relatively strongly from MICrONS (2025), Billeh (2020), and Beiran &amp; Litwin-Kumar (2025) is that <strong>structural constraints help prediction</strong>. From there, you cannot proceed directly to state-complete reconstruction or a unique internal model. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="gates">
<h2 class="section-title">Six gates before replacing decode with emulate</h2>
<table class="data-table">
<thead>
<tr>
<th>Gate</th>
<th>Why is it necessary</th>
<th>Minimum evidence you want</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>G1: Does brain-derived information exceed prior</strong></td>
<td>If the language prior or candidate set is strong, the neural contribution can be mistaken based on the fluency of the output alone. </td>
<td><code>LM-only</code>, <code>no-brain</code>, time-shuffle, trial-shuffle, candidate set size, participant cooperation disclosure. </td>
</tr>
<tr>
<td><strong>G2: Are you following the causal deployment path?</strong></td>
<td>When using future frames, teacher forcing, post-onset auditory feedback, and acausal windows, offline scores overestimate the real-time ceiling. </td>
<td>Disclosure of causal/non-causal, look-ahead window, feedback contamination guard, and online inference path. </td>
</tr>
<tr>
<td><strong>G3: Should it be kept on a different day from the unlearned condition?</strong></td>
<td>Even if the accuracy is high based on the same subject, same day, and same task, the mechanism does not necessarily match. </td>
<td>OOD conditions, cross-day, separate stimulus set, out-of-subject evaluation, fixed decoder deterioration curve, abstention rate. </td>
</tr>
<tr>
<td><strong>G4: Respond to intervention</strong></td>
<td>If you call yourself emulate, you need to guess not only the observation but also the branch after perturbation. </td>
<td>Predictive matching for stimulus changes, ICMS/TMS, pharmacology, and task rule changes. </td>
</tr>
<tr>
<td><strong>G5: Is it stable with closed loop and long-term operation?</strong></td>
<td>If the output changes the next input, offline accuracy no longer applies. Furthermore, within-session speed and long-term deployability are another issue. </td>
<td>end-to-end latency at <code>P50/P95/P99</code>, tail latency, silence / abstention, dropout, <strong>fixed decoder interval</strong>, <code>time since last supervised calibration</code>, recalibration burden, and recovery time.</td>
</tr>
<tr>
<td><strong>G6: Are there enough state variables and have you audited degeneracy?</strong></td>
<td>The same output can have different sets of internal parameters. If we hide the state deficit and the degeneracy of the model family, it becomes an overstatement. </td>
<td>In addition to auditing connectome-only baseline and augmentation comparison, family comparison, uncertainty, cell type / synaptic state / delay / neuromodulation / glia, we also record <strong>sorting version</strong>, <strong>drift correction</strong>, and <strong>unit-match probability</strong> for chronic microelectrode systems. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Operation rules for this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li>Conditions for writing <strong>decode:</strong>This is when the demonstration focuses on predicting meanings, stimuli, actions, and sentences from observed signals, and even if a neural contribution that exceeds <code>LM-only</code> or shuffle baseline is shown, intervention matching or causal real-time path is not shown. </li>
<li><strong>Conditions written as L2 to L3 of communication subsystem: Even if a local loop is established such as speech BCI or tactile BCI, clearly state that the target is a limited subsystem, include causal decoder path, latency / silence / <strong>fixed decoder interval</strong> / recalibration burden, and if it is a microelectrode system, also include unit identity audit. </li>
<li><strong>Conditions for writing local emulation:</strong>When a local circuit shows both a closed loop and a causal intervention, and what is replaced is specified in a limited manner. </li>
<li><strong>Conditions for writing close to WBE:</strong>Only when six points are met: exceedance of prior, causal deployment guard, OOD/cross-day generalization, perturbation matching, closed-loop long-term stability, and integrity audit of state variables. </li>
<li><strong>When only matching output:</strong> Use expressions such as avatar, behavioral clone, decoder, and language interface, not emulate. </li>
<li><strong>Treatment of connectome-constrained success: Predictive gain, stimulus-conditioned digital-twin models, and connectome-constrained success are positioned as advancements in structural/functional scaffolds, and are not described as the only solution or state-complete reconstruction. </li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Tang, J., LeBel, A., Jain, S., et al. (2023). Semantic reconstruction from non-invasive brain recordings. <em>Nature Neuroscience</em>, 26, 858–866. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Défossez, A., Caucheteux, C., Rapin, J., et al. (2023). Decoding speech perception from non-invasive brain recordings. <em>Nature Machine Intelligence</em>, 5, 1097–1107. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">doi:10.1038/s42256-023-00714-5</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <em>Nature Communications</em>, 16, 10521. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Chen, Z., Yao, D., Wang, M., et al. (2024). A neural speech decoding framework leveraging deep learning and speech synthesis. <em>Nature Machine Intelligence</em>, 6, 1816–1827. <a href="https://doi.org/10.1038/s42256-024-00837-5" target="_blank">doi:10.1038/s42256-024-00837-5</a></li>
<li>Singh, V., Papangelou, A., Sharma, M., et al. (2025). Transfer learning via distributed brain recordings enables reliable speech decoding. <em>Nature Communications</em>, 16, 5364. <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">doi:10.1038/s41467-025-63825-0</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <em>Nature</em>, 620, 1031–1036. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>, 28, 902–912. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644, 145–152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Ye, Z., Ai, Q., Liu, Y., de Rijke, M., Zhang, M., Lioma, C., &amp; Ruotsalo, T. (2025). Generative language reconstruction from brain recordings. <em>Communications Biology</em>, 8, 346. <a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">doi:10.1038/s42003-025-07731-7</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Pun, T. K., Khoshnevis, M., Hosman, T., et al. (2024). Measuring instability in chronic human intracortical neural recordings towards stable, long-term brain-computer interfaces. <em>Communications Biology</em>, 7, 1363. <a href="https://doi.org/10.1038/s42003-024-06784-4" target="_blank">doi:10.1038/s42003-024-06784-4</a></li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <em>Science</em>, 372(6539), eabf4588. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>Pachitariu, M., Sridhar, S., Pennington, J., &amp; Stringer, C. (2024). Spike sorting with Kilosort4. <em>Nature Methods</em>, 21, 914–921. <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">doi:10.1038/s41592-024-02595-5</a></li>
<li>van Beest, E. H., Bimbard, C., Fabre, J. M. J., et al. (2025). Tracking neurons across days with high-density probes. <em>Nature Methods</em>, 22, 778–787. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
<li>Flesher, S. N., Downey, J. E., Weiss, J. M., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science</em>, 372(6544), 831–836. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 1323–1334. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Billeh, Y. N., Cai, B., Gratiy, S. L., et al. (2020). Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex. <em>Neuron</em>, 106(3), 388–403.e18. <a href="https://doi.org/10.1016/j.neuron.2020.01.040" target="_blank">doi:10.1016/j.neuron.2020.01.040</a></li>
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <em>Nature Neuroscience</em>, 7, 1345–1352. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
</ol>
</section>

<section class="section" id="why-matters">
<h2 class="section-title">Why is this distinction important</h2>
<p>
Without this distinction, individual advances such as ``we were able to produce sentences from brain signals,'' ``a little bit better with closed loop,'' and ``the stimulus-conditioned digital twin worked'' would be mistakenly interpreted as an overall achievement of WBE. At Mind-Upload, in order to avoid this leap forward, we put the complaint ladder and verification foundation first.
</p>
<div class="cta-box">
<h4>Next</h4>
<p>Click here if you would like to see the level of assertion and the strength of required evidence. </p>
<a href="claims-and-evidence.html">How to read claims and evidence →</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
<li><a href="eeg-basics.html">EEG basics →</a></li>
<li><a href="state-trait-and-drift.html">state / trait / drift →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
<li><a href="../faq.html">FAQ →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
</aside>
</main>
