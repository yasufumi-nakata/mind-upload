---
layout: default
title: "Wiki: Uncertainty, Calibration, and Abstention"
description: "Organizes uncertainty, calibration, and abstention in EEG source imaging, EEG classification, language decoding, and closed-loop BCI on the basis of primary literature."
article_type: Wiki
subtitle: "Confidence is not the same thing as reliability. Calibration and coverage must be read separately."
author: Mind Uploading Research Project
last_updated: "2026-03-29"
note: "Technical / natural science only"
audience: "People who want to avoid point-estimate-only claims, and people who want to understand calibration and abstention as practical indicators."
reading_time: "12-18 minutes"
page_intro: >
  This page organizes uncertainty, confidence intervals, calibration, and abstention in EEG source
  imaging, EEG classification, language decoding, and closed-loop BCI using primary literature. It
  is not only about how much to trust a number when it appears, but also about which output space
  was fixed in advance and when output should stop.
accuracy_note: >
  This page prioritizes technical and natural-science audit items over textbook completeness in statistics.
  Some strict definitions are compressed, but the core points remain explicit: confidence and calibration are
  different, risk can be lowered by lowering coverage, and recalibration burden is itself a performance metric
  in online systems.
page_highlights:
  - "Confidence and calibration are different, and safety cannot be determined from a single number such as softmax or a posterior score."
  - "The same ECE and coverage mean different things within-session, cross-session, cross-subject, and temporal-shift settings."
  - "In brain-to-text or speech decoding, confidence is conditional on the declared candidate bank, onset regime, prompt scaffold, and language prior."
  - "Cue-supported semantic BCI, viewed/recalled content captioning, known-onset word decode, prompt-conditioned generation, and streaming speech synthesis do not share one confidence object."
  - "The uncertainty indicators that should be disclosed differ across source imaging, EEG classification, language decoding, and closed-loop BCI."
  - "Abstention is not weakness; it is an operation that exposes the terms of exchange between coverage and risk."
known_points:
  - "Head geometry, conductivity, subject shift, session drift, and decoder drift all strongly affect estimated width and real-world performance."
  - "If fit / calibration / test separation is ambiguous, the meaning of confidence and thresholds collapses."
  - "Even with high accuracy, poor calibration can still produce overconfident wrong answers under low-confidence conditions."
  - "In language-facing outputs, top-k success or confidence from a fixed candidate bank, known-onset protocol, or prompt scaffold should not be read as open-world uncertainty."
  - "Structural pass/fail rules for language-facing confidence are route-specific even when the numeric thresholds remain task-dependent."
  - "Online BCI requires not only latency, but also abstention rate, dropout, recalibration burden, and recovery time."
unknown_points:
  - "The Calibration & Abstention Card is fixed as a minimum site-wide submission, but numeric pass/fail thresholds for each task are not finalized yet."
  - "It is not yet fixed which coverage / abstention thresholds should become the common pass/fail rule for L2 and L3."
  - "The structural pass/fail bundle for candidate-conditioned confidence in language-facing decode is fixed here, but the numeric threshold values remain route-dependent."
  - "A unified uncertainty-accounting scheme across source imaging, language decoding, and online BCI is still in progress."
wiki_links:
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Returns to the point where an argument stops by using inverse problems and causal inference."
  - label: "Wiki: Baselines / pre-registration / model cards"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Places Calibration & Abstention Cards alongside the rest of the submission set."
  - label: "Wiki: state / trait / drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Separates day-scale variation, longitudinal change, and decoder drift."
  - label: "Wiki: Counterfactuals / interventions / perturbations"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "Explains how to incorporate uncertainty into interventions and held-out conditions."
  - label: "Wiki: Closed loop, delay, jitter, safe stop"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Adds guidance for separating abstention, freeze, and stop behavior in online systems."
recommended_pages:
  - label: "EEG Basics"
    url: "/eeg_101.html"
  - label: "Verification"
    url: "/verification.html"
  - label: "Technology Roadmap"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Conclusion</h2>
<p>
This site does not treat <strong>point estimates only</strong>, <strong>uncalibrated confidence only</strong>, or <strong>output without abstention conditions</strong> as strong evidence. The four points to be audited first are <strong>where does the uncertainty come from</strong>, <strong>which split and evaluation family was used to calibrate the probability/interval/prediction set</strong>, <strong>where to stop when reliability is low</strong>, and <strong>how to record the recalibration load in the case of an online system</strong>. In the re-audit in March 2026, we did not end this with an auxiliary explanation, but connected it to <a href="../verification.html#calibration-abstention-card">Verification's Calibration &amp; Abstention Card</a>.
</p>
</div>

<div class="note-box">
<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. We sort out uncertainties, calibrations, and abstentions from only the technical and natural science aspects of EEG source imaging, EEG classification, language decoding, and closed-loop BCI.
</p>
</div>

<div class="note-box">
<strong>2026-03 Weaknesses revealed in re-audit</strong>
<p>
The previous version was useful as a support page for teaching <strong>confidence ≠ calibration</strong>, but it had not yet become a <strong>reusable submission specification</strong> like the Observability Budget or Temporal Validity Card. Looking at the primary literature, it is dangerous to directly extrapolate within-session calibration to cross-day / cross-subject / temporal shift, and if you touch the threshold without separating fit / calibration / test, the evidence gate itself will collapse. In addition, the earlier page still let language-facing outputs sound too generic: a retrieval score from a fixed bank, a top-k score at known word onsets, and a prompt-conditioned LLM output were still too easy to misread as if they all expressed the same kind of uncertainty. Therefore, on this page, split, slice, candidate scaffold, coverage-risk, and fallback policy are fixed together as <strong>Calibration &amp; Abstention Card</strong>, and language-facing outputs are explicitly stacked with the <a href="../verification.html#neural-contribution-card">Neural Contribution Card</a>.
</p>
</div>

<section class="section" id="audit-gates">
<h2 class="section-title">Four audit gates to be fixed first</h2>
<table class="data-table">
<thead>
<tr>
<th>Audit gate</th>
<th>What I want at least</th>
<th>Claim that it stops when there is not enough</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1: Isolating the source</strong></td>
<td>Breakdown of observation noise, preprocessing difference, head geometry, conductivity, subject shift, session drift, and decoder drift. </td>
<td>It cannot be said that ``the cause of the error is known'' or ``the improvement measures were effective.'' </td>
</tr>
<tr>
<td><strong>Gate 2: Proofreading</strong></td>
<td>Separation of fit/calibration/test, coverage of intervals and sets, ECE/Brier/NLL, posterior width, slice-wise calibration audit, and declared output scaffold when the task is language-facing. </td>
<td>confidence and posterior cannot be read as usable probabilities or confidence levels. </td>
</tr>
<tr>
<td><strong>Gate 3: Abstain</strong></td>
<td>Reject/abstain conditions when low reliability, exchange of coverage reduction and risk reduction, prediction-set size, false alarm ceiling, branching of remeasurement and reanalysis, and disclosure of candidate bank / prompt dependence where relevant. </td>
<td>We cannot claim to suppress incorrect answers or operate on the safe side under low reliability conditions. </td>
</tr>
<tr>
<td><strong>Gate 4: online load</strong></td>
<td>Distinction between recalibration frequency, recalibration trigger, dropout, recovery time, hold-last-output / silence / freeze / hard stop. </td>
<td>Operation stability in a closed loop cannot be expressed only in terms of average accuracy. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="terms">
<h2 class="section-title">Do not mix confidence, intervals, proofreading, and abstention</h2>
<table class="data-table">
<thead>
<tr>
<th>Concept</th>
<th>What do we know</th>
<th>What we still don't know</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Point Presumption</strong></td>
<td>You can see the current representative value. </td>
<td>We don't know how unstable it is or whether it will collapse if conditions are changed. </td>
</tr>
<tr>
<td><strong>Interval / posterior band</strong></td>
<td>You can see how much width there is around the estimated value. </td>
<td>It is necessary to separately check whether the width actually has a reasonable coverage and where it comes from. </td>
</tr>
<tr>
<td><strong>Prediction set</strong></td>
<td>You can see how many candidates can be narrowed down under these conditions. </td>
<td>It is necessary to separately check under what assumptions the set guarantees coverage and how much the set size has increased. </td>
</tr>
<tr>
<td><strong>confidence</strong></td>
<td>You can see the ordering of scores and confidence inside the model. </td>
<td>I don't know if that number matches the actual probability of hitting the mark. </td>
</tr>
<tr>
<td><strong>Calibration</strong></td>
<td>When you get 0.8, you can see whether it really hits about 80% or whether the interval is covered as expected. </td>
<td>Even if proofreading is good, lack of expressiveness and lack of OOD generalization remain separate issues. </td>
</tr>
<tr>
<td><strong>Abstain</strong></td>
<td>Output can be stopped under low reliability conditions and exchange conditions between coverage and risk can be specified. </td>
<td>It is necessary to determine whether the threshold setting is appropriate and whether there is a remeasurement/recalibration flow after abstention. </td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Replacement on this site</strong>
<p>
Softmax, posterior probability, decoder class score, and prediction set are not considered as <strong>calibrated probabilities</strong> or <strong>safe sets</strong> as they are. Calibration error, coverage-risk, interval/set coverage, and separation of fit/calibration/test must be presented together before they can be considered reliable for actual operation.
</p>
</div>
<div class="note-box">
<strong>Additional replacement for language-facing outputs</strong>
<p>
If the output is a word, sentence, or speech candidate, the score must also disclose whether it was conditioned on a <strong>fixed retrieval bank</strong>, a <strong>known-onset protocol</strong>, or a <strong>prompt / language-model scaffold</strong>. On this site, that score is not read as open-world uncertainty until the scaffold itself has been fixed and audited.
</p>
</div>
</section>

<section class="section" id="calibration-split">
<h2 class="section-title">Calibration is managed separately for fit / calibration / test</h2>
<table class="data-table">
<thead>
<tr>
<th>Stage</th>
<th>Put it here</th>
<th>What breaks when you mix</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>fit</strong></td>
<td>Learn the model parameter, feature extractor, and decoder body. </td>
<td>If you mix this stage with calibration, you will lose track of the contribution of model improvement and threshold adjustment. </td>
</tr>
<tr>
<td><strong>calibration</strong></td>
<td>Adjust temperature scaling, threshold tuning, conformal score, and prediction-set size to the frozen model. </td>
<td>If you move the threshold while looking at the test, you cannot claim calibrated probabilities or coverage. </td>
</tr>
<tr>
<td><strong>test</strong></td>
<td>Fix final ECE/Brier/NLL, empirical coverage, false alarm rate, coverage-risk. </td>
<td>When retuning with test, held-out evidence and local tuning are indistinguishable. </td>
</tr>
<tr>
<td><strong>deployment / temporal audit</strong></td>
<td>Fix the handling of cross-day, cross-subject, temporal shift, recalibration trigger, and human intervention. </td>
<td>The same-day calibration is mistakenly read as deployable threshold. </td>
</tr>
</tbody>
</table>
<p>
<a href="https://doi.org/10.1080/01621459.2017.1307116" target="_blank">Lei et al. (2018)</a> specified the calibration split necessary for split conformal, and <a href="https://doi.org/10.1073/pnas.2107794118" target="_blank">Chernozhukov et al. (2021)</a> extended the distributional conformal route. Therefore, on this site, we do not refer to proofreading as ``setting a threshold value after the fact,'' but treat it as a submission that requires an independent split.
</p>
</section>

<section class="section" id="shift-slices">
<h2 class="section-title">The same calibration has different meanings if the evaluation family is different</h2>
<table class="data-table">
<thead>
<tr>
<th>evaluation family</th>
<th>Minimum desired slice</th>
<th>Stop misreading here</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>within-session</strong></td>
<td>Calibration per trial / block / state / artifact burden. </td>
<td>The same-day confidence should not be translated into another day or person. </td>
</tr>
<tr>
<td><strong>cross-session</strong></td>
<td>Calibration per recording day, electrode replacement, state annotation. </td>
<td>Do not write stable decoder while leaving the day shift within the same subject as hidden. </td>
</tr>
<tr>
<td><strong>cross-subject / cross-site / cross-device</strong></td>
<td>Calibration by cohort, site, device, reference scheme, and population subgroup. </td>
<td>Confidence provided by mixed validation is not misinterpreted as patient-independent reliability. </td>
</tr>
<tr>
<td><strong>temporal / longitudinal / OOD</strong></td>
<td>Calibration per time-since-fit, time-since-calibration, novel task, drug/vigilance state, and covariate shift. </td>
<td>We do not increase the short-term success of a fixed model to long-term deployability or OOD safety. </td>
</tr>
</tbody>
</table>
<p>
<a href="https://www.mdpi.com/2227-7390/11/7/1650" target="_blank">Shafiezadeh et al. (2023)</a> showed that the split design itself greatly influenced the results in patient-independent seizure prediction, and <a href="https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html" target="_blank">Ovadia et al. (2019)</a> showed that predictive uncertainty can widely collapse under dataset shift. Furthermore, <a href="https://proceedings.mlr.press/v235/han24b.html" target="_blank">Han et al. (2024)</a> showed that in temporal distribution shift, assessment and selection themselves need to be aligned with the time axis. Therefore, on this site, we do not read <strong>global 1-digit ECE</strong> as final proof of reliability.
</p>
</section>

<section class="section" id="output-objects">
<h2 class="section-title">Probability, interval, prediction set, and abstention are separate outputs</h2>
<table class="data-table">
<thead>
<tr>
<th>Output type</th>
<th>Minimum guarantee you want</th>
<th>Things that should be brought together</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>scalar probability / confidence</strong></td>
<td>ECE, Brier, NLL, reliability diagram, and slice-wise calibration.</td>
<td>Fit/calibration/test separation, evaluation family, and the claim being stopped.</td>
</tr>
<tr>
<td><strong>interval / posterior band</strong></td>
<td>Alignment with empirical coverage, interval width, sensitivity analysis, and external validation. </td>
<td>Whether the coverage is marginal or local, increase or decrease the width, and for which variable. </td>
</tr>
<tr>
<td><strong>prediction set / conformal output</strong></td>
<td>Set coverage, average set size, the validity assumption, and the exchangeability / time-order rule.</td>
<td>Calibration split, set-size cost, marginal vs conditional validity, arguments that stop at OOD. </td>
</tr>
<tr>
<td><strong>abstention / selective prediction</strong></td>
<td>Coverage-risk curve, false-alarm ceiling, fallback path, and human-review trigger.</td>
<td>Threshold, coverage drop, silence/freeze/stop distinction, recovery rule. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="candidate-scaffold">
<h2 class="section-title">Candidate-bank and prompt-conditioned confidence are not open-world uncertainty</h2>
<table class="data-table">
<thead>
<tr>
<th>Route type</th>
<th>What the reported score is conditional on</th>
<th>What it must not be overread as</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fixed-bank retrieval</strong></td>
<td>Bank contents, segment definition, retrieval metric, and top-k cutoff.</td>
<td>Uncertainty over unrestricted language or free-form generation.</td>
</tr>
<tr>
<td><strong>Known-onset word decoding</strong></td>
<td>Declared word boundaries, retrieval-set size, averaging rule, and vocabulary family.</td>
<td>Confidence for free-running segmentation plus decoding in natural conversation.</td>
</tr>
<tr>
<td><strong>Prompt-conditioned generation</strong></td>
<td>Prompt tokens, LLM prior, vocabulary, and beam / decoding strategy.</td>
<td>Brain-only generative likelihood over the full space of possible continuations.</td>
</tr>
<tr>
<td><strong>Autoregressive semantic reconstruction</strong></td>
<td>Subject-specific fit, previous decoded context, and the evaluation candidate regime.</td>
<td>Subject-independent or prior-free semantic access.</td>
</tr>
</tbody>
</table>
<p>
<a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a> explicitly separated encoding-model and language-model contributions by ranking the actual word against distractors, while also showing that the decoder relies on both autoregressive context and fMRI. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">Défossez et al. (2023)</a> reported segment-level top-k retrieval for 3 s speech segments rather than open-vocabulary decoding. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> explicitly framed prior M/EEG retrieval work as requiring access to the ground-truth speech segments at test time, and their own word-level results still report top-k accuracy under a fixed retrieval set with known word onsets. <a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">Ye et al. (2025)</a> concatenated brain and text embeddings into the LLM prompt itself. Therefore, on this site, language-facing confidence is read only after the scaffold is disclosed through the <a href="../verification.html#neural-contribution-card">Neural Contribution Card</a>, and any cross-day or deployment claim must still pass the <a href="../verification.html#temporal-validity-card">Temporal Validity Card</a>.
</p>
</section>

<section class="section" id="sources">
<h2 class="section-title">Uncertainty comes in four layers</h2>
<table class="data-table">
<thead>
<tr>
<th>Layer</th>
<th>Representative examples</th>
<th>Mainly effective pages/issues</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observation noise</strong></td>
<td>Electrode contact, synchronization, myoelectricity/blinks, defects, stimulation artifacts. </td>
<td>Introduction to EEG, event sync, closed-loop implementation. </td>
</tr>
<tr>
<td><strong>Model/geometry uncertainties</strong></td>
<td>Head model, cranial conductivity, source depth, solver dependence. </td>
<td>Source imaging, multimodal integration, and observation-to-estimation.</td>
</tr>
<tr>
<td><strong>Distribution shift</strong></td>
<td>Subject differences, different days, pharmacological conditions, anesthesia, task changes, OOD conditions. </td>
<td>Decode, forecasting, and counterfactual / perturbation.</td>
</tr>
<tr>
<td><strong>Operation Drift</strong></td>
<td>decoder drift, electrode reseating, learning, fatigue, recalibration loads. </td>
<td>Closed-loop BCI, state-trait-drift, and longitudinal evaluation.</td>
</tr>
</tbody>
</table>
<p>
The important thing is not to talk about uncertainty in one box. Source imaging width strongly depends on geometry and conductivity, EEG classification overconfidence strongly depends on calibration error and subject shift, and closed-loop failure strongly depends on drift and recalibration load. <strong>Even though the word "uncertainty" is the same, accounting methods differ depending on the issue</strong>.
</p>
</section>

<section class="section" id="task-specific-reporting">
<h2 class="section-title">Change the indicators to be published for each issue</h2>
<table class="data-table">
<thead>
<tr>
<th>Task</th>
<th>Minimum desired indicators</th>
<th>Why point estimation alone is dangerous</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG source imaging</strong></td>
<td>Posterior / interval width, cranial conductivity sensitivity, solver comparison, empirical coverage for external validator. </td>
<td>This is because multiple source configurations can explain the same scalp signal. </td>
</tr>
<tr>
<td><strong>Offline EEG classification</strong></td>
<td>ECE, Brier score, NLL, fit/calibration/test separation, out-of-subject evaluation, coverage-risk curve. </td>
<td>Even if the accuracy is high, the confidence created by mixed validation is dangerous during operation. </td>
</tr>
<tr>
<td><strong>Speech / brain-to-text decode</strong></td>
<td>Neural Contribution Card fields, cue regime, output family, candidate bank or retrieval-set size, prompt / LM scaffold, onset regime or caption scaffold, no-brain / no-LM / shuffle controls, calibration / abstention slices, and Temporal Validity Card when the claim leaves same-session.</td>
<td>Fluent output or top-k success can be carried by the scaffold more than by the neural contribution if the task constraints are left implicit.</td>
</tr>
<tr>
<td><strong>Rare event prediction</strong></td>
<td>False alarm rate, sensitivity, calibration curve, risk-controlling threshold, and coverage for each alarm horizon.</td>
<td>In low-frequency tasks such as seizure prediction, even a small amount of overconfidence can greatly impair practicality. </td>
</tr>
<tr>
<td><strong>online / closed-loop BCI</strong></td>
<td>abstention rate, dropout, recalibration burden, recovery time, time-since-calibration, number of silence / freeze / hard stops. </td>
<td>Average accuracy alone hides breakdowns in continuous operation and time when intervention is unavailable. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="papers">
<h2 class="section-title">What the primary literature actually shows</h2>

<h3>1. For source imaging, estimation without width is too much reading</h3>
<p>
Vorwerk et al. showed that uncertainty in head tissue conductivity greatly affects dipole reconstruction, and Rimpiläinen et al. included uncertainty in source localization itself in estimation by treating unknown skull conductivity in a Bayesian manner. In Feng et al.'s Block-Champagne, the important thing is not the solver name itself, but the fact that it is accompanied by empirical Bayesian uncertainty quantification. Therefore, on this site, we first check ``which width and external validation was shown'' rather than ``which solver''.
</p>

<h3>2. In EEG classification, calibration without fixing split and shift is reading too much</h3>
<p>
<a href="https://www.mdpi.com/2227-7390/11/7/1650" target="_blank">Shafiezadeh et al. (2023)</a> showed that random cross-validation and leave-one-patient-out give different estimates in patient-independent seizure prediction, and <a href="https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html" target="_blank">Ovadia et al. (2019)</a> showed that predictive uncertainty methods can be widely degraded under dataset shifts. Furthermore, <a href="https://proceedings.mlr.press/v235/han24b.html" target="_blank">Han et al. (2024)</a> showed that model assessment and selection should be designed according to the temporal order with temporal distribution shift. Duan et al.'s UNCER, Hu et al., and Shafiezadeh et al. (2024) showed that calibration itself is important, but the inference that can be drawn from this is that even if the ECE is the same, different split and shift families are different evidence. Therefore, this site does not equate within-session calibration with cross-day / cross-subject reliability.
</p>

<h3>3. In language decoding, confidence must be read through the scaffold</h3>
<p>
Language-decoding papers make the same lesson concrete in a different form: the uncertainty object changes when the output scaffold changes. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a> used subject-specific fMRI together with autoregressive context, and their ablations show that removing fMRI drops performance while isolated scoring still compares the actual word to distractors. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">Défossez et al. (2023)</a> reported top-10 segment retrieval for fixed 3 s speech windows. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> scaled known-word-onset decoding to 723 participants, but still reported top-10 accuracy with a retrieval set of 250 words and found strong protocol effects such as <strong>MEG &gt; EEG</strong> and <strong>reading &gt; listening</strong>. <a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">Ye et al. (2025)</a> directly concatenated brain and text prompt embeddings for LLM generation and outperformed prompt-only or permuted-brain controls. Therefore, on this site, apparently fluent text output is not accepted as a generic uncertainty object: it must declare the candidate bank, prompt scaffold, onset rule, and neural-contribution controls first.
</p>

<h3>3A. 2026-03-29 addendum: structural pass/fail bundle for language-facing confidence</h3>
<table class="data-table">
<thead>
<tr>
<th>Route family</th>
<th>Minimum disclosure before the score is read</th>
<th>Minimum pass condition on this site</th>
<th>Claim still blocked</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Fixed-bank retrieval</strong></td>
<td>Bank contents, segment definition, bank size, cue policy, and whether cue-presentation data entered train / validation / test.</td>
<td>It can count only as retrieval-conditioned evidence if calibration and accuracy are reported on held-out trials under the same bank and cue policy, with no-brain, time-shuffle, or cue-separated comparison.</td>
<td>Open-world semantic access or free-choice communication.</td>
</tr>
<tr>
<td><strong>Known-onset word decoding</strong></td>
<td>Word-onset source, retrieval-set size, vocabulary policy, averaging rule, and whether the decoder uses only causal information around the onset.</td>
<td>It can count only as onset-conditioned word-decoding evidence if top-k or calibration is reported within the declared retrieval set and onset regime together with Neural Contribution Card controls.</td>
<td>Free-running continuous speech or unrestricted language readout.</td>
</tr>
<tr>
<td><strong>Prompt-conditioned generation</strong></td>
<td>Prompt tokens, prompt length, prompt-only and permuted-brain controls, LLM family, decoding strategy, and output-length rule.</td>
<td>It can count only as prompt-conditioned generative evidence if the paper shows what changes when the brain input is removed or permuted under the same prompt scaffold.</td>
<td>Brain-only generative likelihood or prior-free semantic reconstruction.</td>
</tr>
<tr>
<td><strong>Viewed/recalled content captioning</strong></td>
<td>Stimulus family, semantic feature extractor, candidate-initialization policy, cue or recall prompt route, and whether caption optimization started from noninformative or content-bearing seeds.</td>
<td>It can count only as captioning of bounded viewed/recalled content if identification or discriminability and caption quality are reported under the declared caption scaffold and compared against scaffold-preserving controls such as word-order shuffle or feature-mismatch baselines.</td>
<td>General inner-speech decoding or unrestricted thought reading.</td>
</tr>
<tr>
<td><strong>Streaming speech neuroprosthesis</strong></td>
<td>Latency quantiles, silence or abstention rule, same-day training versus fixed-decoder interval, recalibration burden, and durability slice.</td>
<td>It can count only as communication-subsystem evidence if online performance is reported together with abstention or silence behavior and the time window over which the decoder was kept fixed.</td>
<td>Long-term general communication ability, emulate, or WBE-relevant state recovery.</td>
</tr>
</tbody>
</table>
<p>
The point of this bundle is not to assign one universal numeric threshold. It is to stop readers from comparing unlike uncertainty objects as if they were one probability scale. <a href="https://doi.org/10.1038/s41598-024-79309-y" target="_blank">Ryb&aacute;r et al. (2024)</a> showed that cue-presentation data can grossly overestimate semantic BCI performance. <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">Horikawa (2025)</a> added a viewed/recalled content-captioning route built from decoded semantic features and iterative text optimization. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a> remained subject-cooperative autoregressive semantic reconstruction. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> remained known-onset top-10 retrieval over a fixed vocabulary. <a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">Ye et al. (2025)</a> remained prompt-conditioned LLM generation. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> remained invasive communication-subsystem routes. The confidence object changes before the score changes.
</p>

<h3>4. Conformal / risk-controlling routes are effective, but the assumptions and set size need to be stated separately</h3>
<p>
<a href="https://doi.org/10.1080/01621459.2017.1307116" target="_blank">Lei et al. (2018)</a> gives finite-sample marginal coverage by split conformal, and <a href="https://doi.org/10.1073/pnas.2107794118" target="_blank">Chernozhukov et al. (2021)</a> presented distributional conformal prediction using a conditional distribution model. <a href="https://papers.nips.cc/paper/8522-conformal-prediction-under-covariate-shift" target="_blank">Tibshirani et al. (2019)</a> then made explicit that once exchangeability breaks under covariate shift, the conformal procedure itself must be modified rather than rhetorically extended. Furthermore, <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">Segal et al. (2023)</a> showed a direction to suppress false alarm rate by risk-controlling prediction calibration in seizure prediction, and <a href="https://proceedings.mlr.press/v105/eliades19a.html" target="_blank">Eliades &amp; Papadopoulos (2019)</a> applied conformal prediction to BCI / exoskeleton control. Therefore, set-valued output and risk-controlled threshold are effective, but it is necessary to separately state <strong>which split was used for calibration</strong>, <strong>how coverage and set size were exchanged</strong>, and which of <strong>marginal / conditional / temporal validity</strong> is claimed.
</p>

<h3>5. Abstaining is not "because it seems safe", but disclosure of coverage and risk</h3>
<p>
Ganeshkumar et al. showed that the false prediction rate can be reduced by including a reject option in the EEG motor imagery BCI. What is important here is to show <strong>how much coverage has been reduced</strong> in exchange for reducing errors. Therefore, it is not enough to show only abstention rate or accuracy alone, and it is necessary to disclose coverage-risk exchange conditions together.
</p>

<h3>6. With online BCI, recalibration and silence are also performance features</h3>
<p>
Wairagkar et al.'s instantaneous voice-synthesis neuroprosthesis showed a low-latency loop, but at the same time it was important to design it to return silence in non-speech sections. Wilson et al. demonstrated long-term unsupervised recalibration of intracortical BCIs and showed that not only accuracy but also <strong>how much recalibration is required</strong> is the bottleneck for continued operation. Therefore, in the closed-loop system, in addition to latency and accuracy, <strong>abstention / silence / recalibration burden / recovery time</strong> are kept as separate indicators.
</p>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">Operation rules adopted by this site</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>Do not read confidence as just probability:</strong>If there is no calibration error or interval / set coverage, treat it as an internal score. </li>
<li><strong>Separate fit/calibration/test:</strong>Temperature scaling, threshold tuning, and conformal score are managed as independent splits, and they are not readjusted by looking at the test. </li>
<li><strong>Calibration is issued for each evaluation family:</strong>Do not read within-session ECE or coverage as cross-day / cross-subject / temporal shift reliability. </li>
<li><strong>Language-facing scores must disclose their scaffold:</strong>Fixed candidate banks, known onsets, prompt tokens, beam search, and language-model priors are reported before score or fluency is read as neural uncertainty. </li>
<li><strong>Source imaging requires breadth and sensitivity analysis:</strong>If the solutions overlap due to differences in cranial conductivity, head model, and solver family, do not force them to collapse into one point. </li>
<li><strong>EEG classification gives coverage-risk:</strong>Do not pass with accuracy alone, include ECE/Brier/NLL, slice-wise calibration, and coverage after abstention. </li>
<li><strong>Set-valued / conformal results also reveal assumptions:</strong>Do not hide marginal / conditional / temporal validity, set size, or exchangeability / time-order rule. </li>
<li><strong>Manage false alarms separately for seizure prediction and rare events:</strong>In addition to sensitivity, include false alarm cost and threshold control as key metrics. </li>
<li><strong>Online BCI publishes the recalibration load as performance:</strong>Publishes the breakdown of the number of recalibrations, required time, recovery time, silence / freeze / hard stop. </li>
<li><strong>Make it possible to choose to abstain when reliability is low:</strong>Rather than forcefully returning a single answer, branch to the options that require remeasurement, reanalysis, or stoppage that requires intervention. </li>
<li><strong>Attach a Calibration &amp; Abstention Card to results that highlight probabilities, intervals, prediction sets, and abstentions:</strong> Fix split, slice, coverage-risk, and fallback policy in the common submission on the <a href="../verification.html#calibration-abstention-card">Verification</a> side. </li>
<li><strong>Stack the Neural Contribution Card when the output is language-like:</strong>For text / speech / brain-to-text outputs, calibrate the score only together with candidate-set, prompt, and no-brain / no-LM / shuffle disclosure on the <a href="../verification.html#neural-contribution-card">Verification</a> side. </li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Vorwerk, J., Aydin, U., Wolters, C. H., &amp; Butson, C. R. (2019). Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Rimpiläinen, I., Solis-Lemus, J. A., &amp; Särkkä, S. (2019). Improved EEG source localization with Bayesian uncertainty modelling of unknown skull conductivity. <em>NeuroImage</em>, 184, 52-60. <a href="https://doi.org/10.1016/j.neuroimage.2018.11.058" target="_blank">doi:10.1016/j.neuroimage.2018.11.058</a></li>
<li>Feng, Z., Guan, C., &amp; Sun, Y. (2025). Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Ovadia, Y., Fertig, E., Ren, J., Nado, Z., Sculley, D., Nowozin, S., Dillon, J. V., Lakshminarayanan, B., &amp; Snoek, J. (2019). Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift. <a href="https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html" target="_blank">NeurIPS 2019</a></li>
<li>Han, E., Huang, C., &amp; Wang, K. (2024). Model Assessment and Selection under Temporal Distribution Shift. <em>Proceedings of Machine Learning Research</em>, 235. <a href="https://proceedings.mlr.press/v235/han24b.html" target="_blank">PMLR 235</a></li>
<li>Tang, J., LeBel, A., Jain, S., &amp; Huth, A. G. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. <em>Nature Neuroscience</em>, 26, 858-866. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Défossez, A., Caucheteux, C., Rapin, J., Kabeli, O., &amp; King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. <em>Nature Machine Intelligence</em>, 5, 1097-1107. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">doi:10.1038/s42256-023-00714-5</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., Banville, H., Benchetrit, Y., Pallier, C., &amp; King, J.-R. (2025). Towards decoding individual words from non-invasive brain recordings. <em>Nature Communications</em>, 16, 10521. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Ye, X., Liu, X., Wang, Y., Jiang, F., Geng, J., Ye, Q., &amp; Wang, J. (2025). Generative language reconstruction from brain recordings. <em>Communications Biology</em>, 8, 285. <a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">doi:10.1038/s42003-025-07731-7</a></li>
<li>Ryb&aacute;r, M., Poli, R., &amp; Daly, I. (2024). Using data from cue presentations results in grossly overestimating semantic BCI performance. <em>Scientific Reports</em>, 14, 28003. <a href="https://doi.org/10.1038/s41598-024-79309-y" target="_blank">doi:10.1038/s41598-024-79309-y</a></li>
<li>Horikawa, T. (2025). Mind captioning: Evolving descriptive text of mental content from human brain activity. <em>Science Advances</em>, 11(45), eadw1464. <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">doi:10.1126/sciadv.adw1464</a></li>
<li>Littlejohn, K. T., Cho, C. J., Liu, J. R., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>, 28, 902-912. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Duan, T., Wang, Z., Liu, S., Yin, Y., &amp; Srihari, S. N. (2023). UNCER: A framework for uncertainty estimation and reduction in neural decoding of EEG signals. <em>Neurocomputing</em>, 538, 126210. <a href="https://doi.org/10.1016/j.neucom.2023.03.071" target="_blank">doi:10.1016/j.neucom.2023.03.071</a></li>
<li>Hu, J., Ur Rahman, M. M., Al-Naffouri, T., &amp; Laleg-Kirati, T.-M. (2024). Uncertainty Estimation and Model Calibration in EEG Signal Classification for Epileptic Seizures Detection. In <em>2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)</em> (pp. 1-5). <a href="https://doi.org/10.1109/EMBC53108.2024.10782858" target="_blank">doi:10.1109/EMBC53108.2024.10782858</a></li>
<li>Shafiezadeh, S., Mento, G., &amp; Testolin, A. (2023). Methodological Issues in Evaluating Machine Learning Models for Patient-Independent Epileptic Seizure Prediction. <em>Mathematics</em>, 11(7), 1650. <a href="https://doi.org/10.3390/math11071650" target="_blank">doi:10.3390/math11071650</a></li>
<li>Shafiezadeh, S., Duma, G. M., Mento, G., Danieli, A., Antoniazzi, L., Del Popolo Cristaldi, F., Bonanni, P., &amp; Testolin, A. (2024). Calibrating Deep Learning Classifiers for Patient-Independent Electroencephalogram Seizure Forecasting. <em>Sensors</em>, 24(9), 2863. <a href="https://doi.org/10.3390/s24092863" target="_blank">doi:10.3390/s24092863</a></li>
<li>Lei, J., G'Sell, M., Rinaldo, A., Tibshirani, R. J., &amp; Wasserman, L. (2018). Distribution-Free Predictive Inference for Regression. <em>Journal of the American Statistical Association</em>, 113(523), 1094-1111. <a href="https://doi.org/10.1080/01621459.2017.1307116" target="_blank">doi:10.1080/01621459.2017.1307116</a></li>
<li>Chernozhukov, V., Wüthrich, K., &amp; Zhu, Y. (2021). Distributional conformal prediction. <em>Proceedings of the National Academy of Sciences</em>, 118(48), e2107794118. <a href="https://doi.org/10.1073/pnas.2107794118" target="_blank">doi:10.1073/pnas.2107794118</a></li>
<li>Tibshirani, R. J., Barber, R. F., Candès, E. J., &amp; Ramdas, A. (2019). Conformal Prediction Under Covariate Shift. <em>Advances in Neural Information Processing Systems</em>, 32. <a href="https://papers.nips.cc/paper/8522-conformal-prediction-under-covariate-shift" target="_blank">NeurIPS 2019</a></li>
<li>Segal, G., Keidar, N., Lotan, R. M., Romano, Y., Herskovitz, M., &amp; Yaniv, Y. (2023). Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. <em>Frontiers in Neuroscience</em>, 17, 1184990. <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">doi:10.3389/fnins.2023.1184990</a></li>
<li>Ganeshkumar, P., Maheswari, U., &amp; Vasant, P. (2017). Reject Option to Reduce False Prediction Rates for EEG-Motor Imagery Based BCI. In <em>2017 International Conference on Advances in Computing, Communications and Informatics (ICACCI)</em>. <a href="https://doi.org/10.1109/ICACCI.2017.8125908" target="_blank">doi:10.1109/ICACCI.2017.8125908</a></li>
<li>Eliades, G., &amp; Papadopoulos, H. (2019). Applying conformal prediction to control an exoskeleton. <em>Proceedings of Machine Learning Research</em>, 105, 44-51. <a href="https://proceedings.mlr.press/v105/eliades19a.html" target="_blank">PMLR 105</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., Avansino, D. T., Pun, T. K., Gross, R., Hosman, T., Singer-Clark, T., Kapitonava, A., Hochberg, L. R., Simeral, J. D., Shenoy, K. V., Druckmann, S., Henderson, J. M., &amp; Willett, F. R. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., Hochberg, L. R., Brandman, D. M., &amp; Stavisky, S. D. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644(8075), 145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
To return to the source imaging side, please use <a href="observation-to-estimation.html">From observation to estimation</a>. To return to the closed-loop side, please use <a href="closed-loop-latency-jitter-and-safety-stops.html">Closed-loop, delay, jitter, and safety stops</a>. To return to the entire public rule, please use <a href="../verification.html">Verification platform</a>.
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="observation-to-estimation.html">From observation to estimation →</a></li>
<li><a href="state-trait-and-drift.html">state / trait / drift →</a></li>
<li><a href="closed-loop-latency-jitter-and-safety-stops.html">Closed-loop/delay/jitter/safety stops →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../eeg_101.html">EEG Basics -></a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
<li><a href="../tech_roadmap.html">Technology roadmap →</a></li>
</ul>
</div>
</aside>
</main>
