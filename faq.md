---
layout: default
title: "FAQ: Common Questions and Common Failure Modes"
description: "Short, precise answers to the questions that come up most often when reading Mind-Upload."
article_type: FAQ
subtitle: "Prefer verifiable progress to flashy conclusions"
author: Mind Uploading Research Project
last_updated: "2026-03-20"
note: "Human-first"
audience: "Readers who want to sort out questions and misconceptions first, and readers who want a quick overview through short Q&A"
reading_time: "8-15 minutes"
page_intro: "This page is a Q&A for the questions many readers hit first when reading Mind-Upload. It stays short as an entry point, but every strong claim is tied back to a page with evidence."
accuracy_note: "This page gives short answers. Please do not quote the conclusion alone; return to the linked pages and references when you need the full basis."
page_highlights:
  - "It quickly clears up first-order questions such as what this site is for and what EEG or brain-to-text work can and cannot support."
  - "It now front-loads seven technical guardrails: connectome-complete is not state-complete, a high score is not automatically a target-specific neural readout, EEG / MEG connectivity labels are not automatically leak-proof communication maps or causal circuits, BOLD / fNIRS differences need vascular-state / CVR audit, DCM / effective-connectivity labels do not by themselves identify true causal wiring, thermodynamic / irreversibility labels do not by themselves measure physical dissipation or WBE-ready cost, and low latency does not by itself solve the body / environment boundary."
  - "It avoids dramatic overstatement and states what remains unresolved at the same time."
  - "It is structured so readers can tell when the FAQ is enough and when they should move on to the full page."
known_points:
  - "Even short Q&A becomes much safer when strong claims are decomposed into weaker, more testable claims."
  - "The impressive appearance of EEG or LLM outputs must be separated from strong WBE claims, and the contributions of language priors, nuisance routes, and brain-derived information must also be separated."
  - "Because wiring diagrams and cell types still leave excitability, timing-state, thermal-state, transcription/chromatin, proteostasis, cargo-transport / cytoskeletal trafficking state, ECM / PNN, ionic-homeostasis, bioenergetic / mitochondrial state, and maintenance-support variables unresolved, long-term dynamical claims require separate auditing."
  - "An EEG / MEG connectivity label does not by itself show leak-free inter-areal communication or causality; volume conduction, source leakage, ghost interactions, and pipeline dependence still matter."
  - "A BOLD or fNIRS amplitude difference without vascular-state / CVR or short-separation auditing is still not a clean neural difference."
  - "A DCM or effective-connectivity label does not by itself discover the one true causal circuit; candidate model space, validation, and reliability still matter."
  - "An irreversibility / entropy-production label does not by itself tell you the coarse-graining, timescale, estimator family, or dynamical assumptions behind the number, and it is not automatically a metabolic-cost readout."
  - "A closed-loop demo without a disclosed body / environment boundary remains a local controller or subsystem-loop result rather than evidence that embodiment is solved."
  - "FAQ works well as an entry point for avoiding the wrong direction."
unknown_points:
  - "Short answers alone cannot settle theory choice or identity questions."
  - "How far any individual research result generalizes depends on the original paper and its verification conditions."
wiki_links:
  - label: "Wiki: How to read claims and evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "For readers who want a more careful explanation of the short answers in the FAQ."
  - label: "Wiki: How to read the public-page header blocks"
    url: "/wiki/page-header-reading-guide.html"
    description: "Explains how to use the guidance, known/unknown lists, and wiki links at the top of the FAQ."
  - label: "Wiki: Reading routes for L0-L5"
    url: "/wiki/claim-level-reading-routes.html"
    description: "Shows which page to go to next based on the level of claim discussed in the FAQ."
  - label: "Wiki: Guide to the public pages"
    url: "/wiki/public-page-reading-guide.html"
    description: "Helps you decide where to return after the FAQ."
  - label: "Wiki: Decode vs. Emulate"
    url: "/wiki/decode-vs-emulate.html"
    description: "Gives a more intuitive explanation of the distinction used in Q2."
  - label: "Wiki: Consciousness theory map"
    url: "/wiki/consciousness-theory-map.html"
    description: "Organizes the positions of IIT and GNWT from Q8 in table form."
  - label: "Wiki: Counterfactuals, interventions, and perturbations"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "Explains the entry point for causal verification behind Q1-Q3."
  - label: "Wiki: From observation to estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Organizes why ESI, DCM, and SCM remain model-conditioned unless validation and abstention are disclosed."
  - label: "Wiki: Standards, repositories, validators, and benchmarks"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "Clarifies the standardization issues behind Q4 by role."
  - label: "Wiki: Closed loop, latency, jitter, and safe stops"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "Explains the difference between offline accuracy and L3 from a real-time systems perspective."
  - label: "Wiki: Why a Connectome Is Not Enough"
    url: "/wiki/connectome-is-not-enough.html"
    description: "Explains which state classes remain outside wiring diagram plus cell type."
  - label: "Wiki: Observability and Claim Ceiling by Measurement Stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Explains why hemodynamic differences and shortcut-prone scores still have strict reading ceilings."
  - label: "Wiki: Thermodynamic grounding basics"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Explains Landauer, dissipation, NESS, irreversibility, and route cards from the beginning."
recommended_pages:
  - label: "Verification"
    url: "/verification.html"
  - label: "WBE 101"
    url: "/wbe_101.html"
  - label: "Glossary"
    url: "/glossary.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Read</h2>
<p>
This page is designed to block common misunderstandings early. The stronger the claim, the more carefully you should check, in order, (1) the definition of terms, (2) the measurement scale, (3) the condition that would count as failure, and (4) the reproduction procedure.
</p>
</div>

<div class="note-box">
<strong>Limits of the FAQ</strong>
<p>
The FAQ gives short answers so you do not head in the wrong direction first. It is meant to establish orientation; once you need evidence or detail, move on to the linked pages.
</p>
</div>
<div class="note-box">
<strong>When you are not sure where to return after a short answer</strong>
<p>
The FAQ is only an entry point, so after reading it you still need to decide whether to go next to Verification, WBE 101, Datasets, or the Glossary. If you want the role differences among the public pages first, see <a href="wiki/public-page-reading-guide.html">Wiki: Guide to the public pages</a>.
</p>
</div>
<div class="note-box">
<strong>When you are unsure how to use the site as a whole</strong>
<p>
If you want to use the FAQ as the front door and then decide whether to get the overview, study in the wiki, or turn a question into an Issue, see <a href="wiki/site-usage-modes.html">Wiki: The three ways to use this site</a>.
</p>
</div>
<div class="note-box">
<strong>When you are unsure how to read the header guidance and the known/unknown blocks</strong>
<p>
The blocks at the top of this page, such as how to read the page, the accuracy note, what is known now, and the wiki routes, are there to prevent short Q&amp;A answers from being misread. If you want the shared rules in one place, see <a href="wiki/page-header-reading-guide.html">Wiki: How to read the public-page header blocks</a>.
</p>
</div>
<div class="note-box">
<strong>When your question is stuck somewhere between L0 and L5</strong>
<p>
The questions in this FAQ span everything from L0 practical work to L5 social deployment. If you want the next pages organized by claim level, see <a href="wiki/claim-level-reading-routes.html">Wiki: Reading routes for L0-L5</a>.
</p>
</div>
<div class="note-box">
<strong>When you are unsure whether to follow theory pages or practical pages next</strong>
<p>
If you want to continue only into theory pages after the FAQ, see <a href="wiki/theory-pages-reading-guide.html">Wiki: Guide to the theory pages</a>. If you want to continue into practical pages such as Verification or Datasets, see <a href="wiki/practical-pages-reading-guide.html">Wiki: Guide to the practical pages</a>.
</p>
</div>
<div class="note-box">
<strong>When you are unsure which page to open after Verification</strong>
<p>
If you move from the FAQ into Verification and then are unsure whether to return to L0 implementation or jump first to L2, L3, or L4, see <a href="wiki/verification-next-routes.html">Wiki: Four paths after Verification</a>.
</p>
</div>
<div class="note-box">
<strong>When you want to turn the question itself into an Issue</strong>
<p>
If reading the FAQ makes you think “this is unclear” or “this condition is missing,” and you want to turn that directly into a useful Issue, see <a href="wiki/issue-writing-basics.html">Wiki: Writing your first Issue</a>.
</p>
</div>
<div class="note-box">
<strong>When you understand the meaning but not the next action</strong>
<p>
If the FAQ helped you understand the topic but you still do not know what to verify next before making a correction or judgment, see <a href="wiki/understanding-vs-action-readiness.html">Wiki: The difference between understanding and being ready to act</a>.
</p>
</div>

<div class="note-box">
<strong>Seven technical guards now fixed at the front door</strong>
<p>
This FAQ now blocks seven fast overreads before they spread through the site: <strong>connectome-complete is not state-complete</strong>, <strong>high score is not automatically target-specific neural evidence</strong>, <strong>sensor- or source-space connectivity is not automatically a leak-proof communication map or causal circuit</strong>, <strong>BOLD / fNIRS amplitude difference is not automatically a neural difference without vascular-state / CVR audit</strong>, <strong>DCM / effective-connectivity output is not automatically the brain's true causal wiring</strong>, <strong>thermodynamic / irreversibility labels are not automatically direct physical-dissipation measurements or WBE gates</strong>, and <strong>low latency is not automatically a solved body / environment boundary</strong>. If you need the full rule set behind them, go next to <a href="eeg_101.html">EEG 101</a>, <a href="verification.html#observability-budget">Verification: Observability Budget</a>, <a href="verification.html#body-environment-boundary-card">Verification: Body / Environment Boundary Card</a>, <a href="wiki/connectome-is-not-enough.html">Wiki: Why a Connectome Is Not Enough</a>, <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: Observability and Claim Ceiling by Measurement Stack</a>, <a href="wiki/observation-to-estimation.html#effective-connectivity-route-card">Wiki: effective-connectivity route card</a>, and <a href="wiki/thermodynamic-grounding-basics.html#irreversibility-route-card">Wiki: irreversibility route card</a>.
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>If you want to...</th>
<th>Read this question first</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Know only what this site is for</strong></td>
<td>Start with Q0, “What does Mind-Upload actually do?” for the fastest overview.</td>
</tr>
<tr>
<td><strong>Avoid misreading flashy claims in news coverage</strong></td>
<td>Read the Q1 series first to separate task-limited decode, shortcut routes, connectivity-ceiling issues, hemodynamic proxy limits, model-conditioned causal claims, and thermodynamic overreads before moving on to Q2.</td>
</tr>
<tr>
<td><strong>Know only what counts as progress</strong></td>
<td>Q3, “Then what should we build to count as progress?” shows the minimum deliverables for L0-L2.</td>
</tr>
<tr>
<td><strong>Know whether the connectome alone is enough</strong></td>
<td>Q2c, “If we know the connectome and cell type, is the rest mostly filled in?” clarifies which hidden-state families remain outside connectome plus cell type.</td>
</tr>
<tr>
<td><strong>Know the conditions for real-time or closed-loop work</strong></td>
<td>Start with Q5b, “If offline accuracy is high, is that enough for closed loop?” to see what L3 adds.</td>
</tr>
<tr>
<td><strong>Know the philosophical or ethical positions involved</strong></td>
<td>Read Q6 on the hard problem and Q9 on ethics to see what the site does and does not claim there.</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Four checks for strong claims</strong>
<ol>
<li><strong>What was actually achieved?</strong> Check which level from L0 to L5 the claim belongs to.</li>
<li><strong>What was actually measured?</strong> Separate output matching from intervention or counterfactual testing.</li>
<li><strong>What would count as being wrong?</strong> Look for an explicit falsification condition.</li>
<li><strong>Can other people follow it?</strong> Check whether the data, code, logs, and procedure are public.</li>
</ol>
</div>

<section class="section" id="q0">
<h2 class="section-title">Q. What does Mind-Upload actually do?</h2>
<p>
A. It is a site for building a <strong>Verification Commons</strong> that turns mind uploading and WBE into a verifiable research program. It fixes the data inputs, evaluation outputs, rules for success and failure, and operational procedures first.
</p>
<div class="cta-box">
<h4>Start</h4>
<p>The overall picture starts here.</p>
<a href="verification.html">Open Verification →</a>
</div>
</section>

<section class="section" id="q1">
<h2 class="section-title">Q. Can EEG read “thoughts”?</h2>
<p>
A. It is fair to say that some aspects can be read under constrained conditions, but it is not yet fair to say that free thought can be read as such. Tang et al. (2023) demonstrated semantic reconstruction of continuous language from non-invasive brain recordings, but this was an individual-subject reconstruction setup using fMRI. d'Ascoli et al. (2025) showed progress in word decoding from non-invasive M/EEG across 723 people and roughly five million words, but the result depended on known word onsets and task structure, and MEG with reading performed better than EEG with listening.
</p>
<p>
It is also not the case that scalp signals uniquely determine the internal state. In Unnwongse et al. (2023), which used intracranial stimulation for direct validation, the mean ESI localization error ranged from 10.3 to 26.0 mm depending on source depth and skull conductivity. In Hao et al. (2025), using simultaneous HD-EEG and SEEG, ictal ESI outperformed interictal ESI, but the figures were still 14.07 ± 4.62 mm versus 17.38 ± 4.16 mm, and accuracy depended strongly on source depth and spike power.
</p>
<p>
On this site, we therefore do not treat “externally validated ESI” as one checkbox. Intracranial-stimulation ground truth, simultaneous HD-EEG/SEEG, and postsurgical outcome answer different error questions, so the benchmark class has to be named before the claim ceiling is raised. The shortest route is <a href="eeg_101.html#esi-uncertainty">EEG 101: what must now be stated rigorously about ESI</a> and <a href="datasets.html#validation-ladder">Datasets: the source-imaging validation ladder</a>.
</p>
<p>
Another weak reading is to publish only the cleanest inverse map and silently ignore how much the answer moves across reasonable pipelines. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.076" target="_blank">Mahjoory et al. (2017)</a> showed that inverse-method and software-package choice can materially change source localization and even more strongly change downstream connectivity estimates. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a> then showed on a ground-truth intracranial-stimulation benchmark that many tested parameter combinations miss the session-wise optimum by a wide margin. So at Mind-Upload, one pretty ESI map without <strong>cross-solver / cross-parameter spread</strong> or an <strong>uncertainty display</strong> is still read as <strong>method-sensitive evidence</strong>, not as a stable source fact.
</p>
<p>
The Mind-Upload position is not to deny ambitious readout work. It is to separate the claim first into <strong>task-dependent decoding</strong> and <strong>internal-state identification</strong>, then make explicit the language prior, calibration, abstention conditions, and whether direct validation exists. If you skip those distinctions, you end up misreading “a string was produced” as if it were WBE-relevant state reconstruction.
</p>
</section>

<div class="note-box">
<strong>Do not collapse Q1 into one sentence</strong>
<p>
<code>A string came out</code>, <code>it came out from brain-derived information alone</code>, <code>the score followed the target variable rather than shortcut routes</code>, and <code>the internal state was identified</code> are different claims. When reading brain-to-text work, separate (1) the measurement method, (2) the task constraints, (3) the language prior, (4) the presence or absence of direct validation, (5) shortcut and nuisance-route auditing, and (6) calibration and abstention conditions.
</p>
</div>

<section class="section" id="q1b">
<h2 class="section-title" id="brain-to-text">Q. What is the minimum you should check in a brain-to-text demo?</h2>
<p>
A. At minimum, check the following six things.
</p>
<ul>
<li><strong>Measurement method:</strong> scalp EEG, MEG, fMRI, ECoG, or intracortical array. Representative high-performance speech neuroprostheses are invasive.</li>
<li><strong>Task:</strong> heard words, read words, speech articulation, recall, or free conversation. A constrained perceptual task is not the same as free thought.</li>
<li><strong>Priors and baselines:</strong> fixed vocabulary, beam search, external corpora, LLMs, prompts, and how far <code>LM-only</code>, <code>no-brain</code>, or shuffle baselines were used. Fluency does not automatically reflect brain signal alone.</li>
<li><strong>Validation:</strong> held-out conditions, counterfactual tests, adversarial controls, and whether failure cases are shown. Evaluation that stays too close to the training setup is not strong evidence.</li>
<li><strong>Confidence handling:</strong> whether confidence is calibrated, and whether silence or abstention is returned at low confidence. A high-probability display alone is not safe interpretation.</li>
<li><strong>Long-term operation:</strong> not just within-session speed, but also tail latency, cross-day stability, and recalibration burden. A fast demo is not the same as a deployable loop.</li>
</ul>
<p>
Littlejohn et al. (2025) showed streaming brain-to-voice output every 80 ms, and Wairagkar et al. (2025) showed neural-to-voice synthesis under 10 ms with silence fallback, but both are invasive communication routes. Wilson et al. (2025) further showed the importance of long-term unsupervised recalibration, making it clear that daily supervised recalibration is itself another barrier. For that reason, general scalp EEG or ordinary non-invasive BCI cannot claim the same level without the same conditions.
</p>
</section>

<section class="section" id="q1c">
<h2 class="section-title">Q. If the score is high or cross-day stable, did we read the target neural variable?</h2>
<p>
A. Not necessarily. A score can stay high because the model is using <strong>shortcut routes</strong> rather than the intended neural variable. In EEG/BCI work, those routes can include eye position, facial/jaw/neck EMG, uninstructed movement, auditory feedback, subject / session fingerprint, and acquisition-distribution cues such as site, device, reference system, electrode layout, and protocol.
</p>
<p>
<a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> showed that trial-by-trial neural dynamics can be dominated by richly varied movements, <a href="https://doi.org/10.1523/ENEURO.0401-17.2018" target="_blank">Mostert et al. (2018)</a> showed that visual-working-memory decode can retain an eye-movement confound, <a href="https://doi.org/10.1088/1741-2560/2/4/014" target="_blank">McFarland et al. (2005)</a> showed that EMG can contribute to early BCI performance, <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> showed that repeated-measure record-wise splits can massively underestimate error through identity confounding, and <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">Xu et al. (2020)</a> showed that cross-dataset variability weakens EEG-decoding generalization.
</p>
<p>
At Mind-Upload, a result is not read as <strong>target-specific neural evidence</strong> unless the paper also fixes the target variable, nuisance-only baselines, slice-wise hold-out, and independence units for subject / session / acquisition distribution. The shortest follow-up is <a href="verification.html#specificity-shortcut-card">Verification: Specificity &amp; Shortcut Card</a>.
</p>
</section>

<section class="section" id="q1d">
<h2 class="section-title">Q. If BOLD or fNIRS changes, does that mean neural state changed?</h2>
<p>
A. Not automatically. Hemodynamic modalities carry both neural-side uncertainty and a <strong>vascular transfer state</strong>. So a group difference or longitudinal BOLD / HbO / HbR change can partly reflect baseline vascular state, cerebrovascular reactivity, or superficial/systemic contamination rather than a clean neural difference.
</p>
<p>
<a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a> showed that accounting for individual vascular reactivity improves group-level BOLD analyses, <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a> showed that task BOLD magnitude is strongly predicted by CVR across the cortex, <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yücel et al. (2015)</a> showed that short-separation regression is needed to reduce superficial confounds in fNIRS, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can coexist with opposite oxygen-metabolism changes in many voxels.
</p>
<p>
At Mind-Upload, a BOLD or fNIRS difference without <strong>vascular-state / CVR</strong> or <strong>short-separation</strong> audit stays a <strong>hemodynamic-limited difference</strong> rather than a clean neural difference. The shortest follow-up is <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: Observability and Claim Ceiling by Measurement Stack</a> plus <a href="verification.html#observability-budget">Verification: Observability Budget</a>.
</p>
</section>

<section class="section" id="q1d2">
<h2 class="section-title">Q. If a paper shows EEG / MEG connectivity or information flow, did it identify communication channels or causality?</h2>
<p>
A. Not by default. On this site, sensor-space or source-space connectivity results are first read as <strong>dependence patterns under a named pipeline</strong>, not as leak-proof inter-areal communication maps or causal wiring. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">Vinck et al. (2011)</a> made wPLI more conservative against some zero-lag mixing than older phase-synchrony measures, but that is not the same as eliminating leakage or proving directional influence.
</p>
<p>
The deeper problem is that the remaining failure modes are different from ordinary cleanup. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">Haufe et al. (2013)</a> showed that sensor-space EEG connectivity remains strongly limited by volume conduction, <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">Palva et al. (2018)</a> showed that even leakage-insensitive source-space measures can generate ghost interactions, <a href="https://doi.org/10.1016/j.neures.2019.09.003" target="_blank">Ye et al. (2020)</a> evaluated symbolic transfer entropy with TMS precisely because observational data alone make causality difficult to identify, and <a href="https://doi.org/10.1016/j.clinph.2025.03.043" target="_blank">Miljevic et al. (2025)</a> showed that sensor-space functional-connectivity estimates still change materially with rereferencing, epoch length, epoch count, and metric choice.
</p>
<p>
At Mind-Upload, a connectivity paper must therefore still disclose <strong>reference scheme and preprocessing route</strong>, <strong>leakage / volume-conduction countermeasures</strong>, <strong>source-model assumptions if used</strong>, <strong>perturbation or external validation route for directional claims</strong>, <strong>pipeline-sensitivity checks</strong>, and <strong>residual claim ceiling</strong>. If those are missing, we read the result as a <strong>pipeline-conditioned dependence map</strong>, not as a communication graph or causal circuit. The shortest follow-up is <a href="eeg_101.html">EEG 101</a>, especially the connectivity-ceiling note, then <a href="wiki/observation-to-estimation.html">Wiki: From observation to estimation</a>.
</p>
</section>

<section class="section" id="q1e">
<h2 class="section-title">Q. If a paper reports DCM or effective connectivity, did it find the brain's true causal wiring?</h2>
<p>
A. Not by default. On this site, DCM / effective-connectivity output is read as a <strong>model-conditioned causal hypothesis</strong>, not as automatic discovery of the one true circuit. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">Penny et al. (2004)</a> showed that DCM conclusions are relative to the models being compared, and <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">Rosa et al. (2012)</a> showed that later workflows can search very large model spaces efficiently from one full model rather than make the true model unique. More recent scaling work such as <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">Frässle et al. (2021)</a> and <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Wu et al. (2024)</a> pushes effective-connectivity estimation toward whole-brain or faster settings, but it still remains inside an explicitly chosen generative model and observation model.
</p>
<p>
That does not make effective-connectivity work useless. It means the safe claim is narrower: under a disclosed node set, omitted alternatives, prior family, and observation assumptions, one model family explained the data better than named competitors. Even reproducibility is conditional. <a href="https://doi.org/10.1002/hbm.23061" target="_blank">Frässle et al. (2016)</a> and <a href="https://doi.org/10.1002/hbm.26782" target="_blank">Jafarian et al. (2024)</a> show that effective-connectivity reliability can be good when the task, session interval, and acquisition conditions are tightly controlled, but that is still not the same as proving a unique causal circuit in the wild.
</p>
<p>
At Mind-Upload, a paper that says “effective connectivity” must still disclose <strong>candidate model space</strong>, <strong>omitted alternatives</strong>, <strong>family comparison or model recovery</strong>, <strong>held-out perturbation / external validation</strong>, <strong>reliability window</strong>, and <strong>abstention boundary</strong>. If those are missing, we read it as a <strong>candidate-model result</strong>, not as causal-wiring discovery. The shortest follow-up is <a href="wiki/observation-to-estimation.html#effective-connectivity-route-card">Wiki: effective-connectivity route card</a> and <a href="tech_roadmap.html#qa-r4">Roadmap R4</a>.
</p>
</section>

<section class="section" id="q1f">
<h2 class="section-title">Q. If a paper reports entropy production, irreversibility, or arrow-of-time in brain data, did it measure the brain's physical dissipation or WBE-ready thermodynamic cost?</h2>
<p>
A. Not by default. On this site, thermodynamic language is split before interpretation. <a href="https://doi.org/10.1038/nature10872" target="_blank">B&eacute;rut et al. (2012)</a> tested the Landauer lower bound for bit erasure, <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">Attwell &amp; Laughlin (2001)</a> summarized tissue-side signaling costs, and papers such as <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> estimate nonequilibrium quantities from neural data. Those objects are related, but they are not the same measurement.
</p>
<p>
In the current primary literature, the same thermodynamic vocabulary still hides different estimator families. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> estimated entropy-production lower bounds from coarse-grained BOLD state transitions, <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">Deco et al. (2022)</a> used time-shifted correlation asymmetry, <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a> used inversion decoding on ECoG, <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">Nartallo-Kaluarachchi et al. (2025)</a> used directed visibility graphs on MEG, and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> estimated model-based entropy flow under a state-space kinetic Ising model. So the phrase <strong>thermodynamic result</strong> does not by itself tell you whether the paper reported a lower bound, an asymmetry score, a graph index, or a model-based flow estimate.
</p>
<p>
Just naming the estimator family is still too weak. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> showed that the estimate depends on how macrostates are coarse-grained, <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a> showed that reversibility detection depends on principal-component choice, input features, and model complexity, and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> explicitly notes that pairwise and conditional-independence assumptions limit interpretation. At Mind-Upload, such a paper must therefore disclose <strong>signal route and state definition</strong>, <strong>coarse-graining / timescale</strong>, <strong>estimator family and dynamical assumptions</strong>, <strong>null / surrogate control</strong>, <strong>quantity type</strong>, <strong>physiology-side grounding if energetic language is used</strong>, <strong>cost isolation</strong>, and <strong>abstention boundary</strong>. If those are missing, we keep the result at the level of an <strong>exploratory auxiliary analysis</strong>, not a direct readout of microscopic dissipation, metabolic cost, or WBE-relevant validity. The shortest follow-up is <a href="wiki/thermodynamic-grounding-basics.html#irreversibility-route-card">Wiki: irreversibility route card</a> plus <a href="verification.html#thermodynamic-verification">Verification: thermodynamic indicators</a>.
</p>
</section>

<section class="section" id="q2">
<h2 class="section-title">Q. What is the difference between decode and emulate?</h2>
<p>
A. Decode means <em>translating observations</em>. Emulate means <em>having an internal state that evolves over time, responds to intervention, and generates outputs</em>. To move closer to WBE, the benchmark has to evaluate the second kind of claim, not only the first.
</p>
<p>
Recent non-invasive word decoding and streaming speech neuroprostheses are major advances as communication routes. But at Mind-Upload, we do not read them as emulation, let alone as WBE evidence, unless the work also establishes <strong>neural contribution beyond language prior</strong>, <strong>OOD and cross-day generalization</strong>, <strong>matching after intervention</strong>, <strong>tail latency, silence, and recalibration burden</strong>, and <strong>auditing of hidden state</strong>. What has advanced first is decode, or at most local subsystem closed loop.
</p>
<p><a href="wbe_101.html">WBE 101</a>, the <a href="glossary.html">Glossary</a>, and <a href="wiki/decode-vs-emulate.html">Wiki: Decode vs. Emulate</a> are the shortest follow-up route.</p>
</section>

<section class="section" id="q2b">
<h2 class="section-title">Q. If an LLM or digital twin talks like a person, is that Mind-Upload?</h2>
<p>
A. Not by itself. Natural conversation could reflect <strong>imitation of outward behavior</strong>, or it could reflect <strong>continuity of internal state and causal structure</strong>. Those are different questions.
</p>
<p>
Mind-Upload cares not only about whether something looks human-like, but whether the responses under changed conditions, the continuity of memory and learning, and the response to falsification conditions are all disclosed. Natural appearance matters as a clue, but it is not enough to move to an L4 identity claim.
</p>
<p><a href="wiki/counterfactual-and-perturbation-verification.html">Wiki: Counterfactual, intervention, and perturbation verification</a> explains in stages why “it can talk naturally” is not enough.</p>
</section>

<section class="section" id="q2c">
<h2 class="section-title">Q. If we know the connectome and cell type, is the rest mostly filled in?</h2>
<p>
A. Not yet. Wiring and cell type still leave broad families of state latent. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> showed morpho-electric spread even within the same transcriptomic type, <a href="https://doi.org/10.1038/nature09160" target="_blank">Grubb &amp; Burrone (2010)</a> showed activity-dependent AIS relocation that retunes excitability, <a href="https://doi.org/10.1126/science.adg9982" target="_blank">Santoni et al. (2024)</a> showed that chromatin plasticity can predetermine neuronal eligibility for memory trace formation, <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">Govindarajan et al. (2011)</a> showed branch-level protein-synthesis-dependent LTP integration, <a href="https://doi.org/10.1016/j.neuron.2006.09.040" target="_blank">Park et al. (2006)</a>, <a href="https://doi.org/10.7554/eLife.53456" target="_blank">Zhao et al. (2020)</a>, and <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">Swarnkar et al. (2021)</a> showed that compartment-specific cargo delivery is another state layer for spine growth, synaptic plasticity, and memory, <a href="https://doi.org/10.1038/nn.2338" target="_blank">Frischknecht et al. (2009)</a> showed that ECM constrains AMPA-receptor mobility and short-term plasticity, <a href="https://doi.org/10.1126/science.1245423" target="_blank">Glykys et al. (2014)</a> showed that local impermeant anions constrain neuronal chloride concentration, and <a href="https://doi.org/10.1038/ncomms9073" target="_blank">Seidl et al. (2015)</a> showed that node and internode geometry can tune conduction timing.
</p>
<p>
If by “connectome” one means a human diffusion-MRI tractography connectome, the object is even coarser than the word suggests. <a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">Thomas et al. (2014)</a> found no high-anatomical-accuracy solution across tractography methods even with exceptional ex vivo macaque diffusion data, <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">Reveley et al. (2015)</a> showed that superficial white matter can block long-range tracking from large parts of cortex, <a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">Donahue et al. (2016)</a> found useful but incomplete prediction of tracer-weighted corticocortical connectivity, <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">Schilling et al. (2020)</a> showed that high accuracy mainly appears when strong anatomical start / end / exclusion priors are supplied, and <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">Grisot et al. (2021)</a> localized recurring same-brain errors at branching and turning configurations. At Mind-Upload, a tractography-derived human connectome is therefore read as a <strong>macro pathway prior</strong> or <strong>bundle-level hypothesis</strong>, not as an edge-complete human connectome.
</p>
<p>
Likewise, <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>, and <a href="https://doi.org/10.1038/s41467-024-47838-5" target="_blank">Xu et al. (2024)</a> show that sleep-dependent homeostasis and network recovery remain additional variables. <a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a>, <a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. (2014)</a>, and <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> show that myelin and oligodendrocyte support affect timing and axonal health. Separately, <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">Hardingham &amp; Larkman (1998)</a>, <a href="https://doi.org/10.1111/j.1469-7793.2000.00059.x" target="_blank">Volgushev et al. (2000)</a>, <a href="https://doi.org/10.1126/science.8446900" target="_blank">Moser et al. (1993)</a>, and <a href="https://doi.org/10.1038/nature07448" target="_blank">Long &amp; Fee (2008)</a> show that local thermal-state can change synaptic reliability, spike generation, field-potential amplitude, and sequence timing even without rewiring, while healthy-human <a href="https://doi.org/10.1093/brain/awab466" target="_blank">MRS thermometry (Rzechorzek et al., 2022)</a> remains a macro thermal proxy rather than cell-specific ground truth. Separately, <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">Rangaraju et al. (2014)</a>, <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">Rangaraju et al. (2019)</a>, <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">Divakaruni et al. (2018)</a>, <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">Bapat et al. (2024)</a>, and <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">Hu et al. (2025)</a> show that local ATP supply, mitochondrial positioning, fission/fusion, and synaptic ATP-synthase organization remain additional hidden state for repeated-burst reliability and dendritic plasticity. Current human energetic routes such as <a href="https://doi.org/10.1002/nbm.3384" target="_blank">31P-MRS (Ren et al., 2015)</a> and <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">dynamic DMRSI (Li et al., 2025)</a> are important advances, but they are still macro energetic proxies rather than branch-local mitochondrial readouts. The same human ceiling applies to cargo routing: current in vivo routes do not directly reveal branch-specific motor engagement, cargo pausing, or bouton-level retention. Likewise, human sodium MRI routes such as <a href="https://doi.org/10.1002/mrm.23225" target="_blank">Qian et al. (2012)</a> and <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">Qian et al. (2025)</a> are important macro ionic proxies, but they still do not directly reveal cell-specific chloride concentration, KCC2 / NKCC1 balance, or local E<sub>GABA</sub>. Meanwhile, <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a>, <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a>, and <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Lee et al. (2022)</a> show that glial and metabolic support, plus active maintenance under molecular turnover, matter for memory consolidation and slow state.
</p>
<p>
At Mind-Upload, this means we treat <strong>connectome-complete as progress on the structural scaffold</strong>, not as <strong>emulation-complete</strong>. Current excitability, timing-state, thermal-state, transcription/chromatin, local proteostasis, cargo-transport / cytoskeletal trafficking state, ECM / PNN gate, ionic milieu, bioenergetic / mitochondrial state, sleep/controller state, and glial/metabolic support still need to be disclosed or left explicitly latent. So <strong>same-day activity matching</strong>, <strong>cross-day stability</strong>, and <strong>maintenance-consistent dynamics</strong> remain separate claims. The shortest follow-up is <a href="wiki/connectome-is-not-enough.html">Wiki: Why wiring diagrams alone are not enough</a> plus <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: Homeostatic plasticity and maintenance state</a>.
</p>
<p>
Human evidence should also be read as a <strong>ladder</strong>, not as one direct route. Local human nanoscale ultrastructure, diffusion-MRI tractography-based macro pathway priors, regional synaptic-density PET, receptor / transporter atlas priors, ligand- / challenge-limited occupancy or displacement PET, <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">sleep-homeostasis / TMS-EEG plasticity proxies (Huber et al., 2013)</a>, <a href="https://doi.org/10.1038/ncomms12455" target="_blank">Kuhn et al. (2016)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">Fehér et al. (2026)</a>, <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">EEG-state-gated perturbation routes (Zrenner et al., 2018)</a>, and whole-brain biochemical / energetic / ionic / thermal / myelin / clearance proxies are all real advances, but they reduce different error terms and do not auto-fill current transcription / chromatin state, ECM / PNN gate state, current chloride homeostasis, branch-local proteostasis, branch- or bouton-specific cargo delivery, branch-local mitochondrial positioning, AIS geometry, or the cell-specific recovery controller. Several of the newer human routes are also still <strong>specialized, small-cohort, or model-dependent</strong>, and tractography remains <strong>ceiling-limited by validation constraints</strong> rather than by deployment alone, so proxy class and operational maturity should not be collapsed into one impression. The shortest front-door table is <a href="wbe_101.html#human-observability-ladder">WBE 101: what human evidence currently looks like</a>.
</p>
<p>
Even within the PET rows, the measurement model still matters. On this site, SV2A PET is read as a tracer-defined synaptic-density proxy rather than a readout of momentary synaptic efficacy, receptor atlases are read as normative group maps rather than current individual state, and occupancy / displacement PET is read as ligand- and challenge-limited evidence over bounded scan windows. If tracer, quantification model, or scan window is missing, the PET result is still too coarse to read as current internal state.
</p>
</section>

<section class="section" id="q3">
<h2 class="section-title">Q. Then what should we build to count as progress?</h2>
<p>
A. For now, L0-L2 is the realistic target: reproducible analyses, comparable benchmarks, and models that can be tested through intervention prediction. Mind-Upload turns those into operating templates, logs, and rules that the site can actually use.
</p>
<div class="key-points">
<h4>Concrete deliverables</h4>
<ul>
<li><strong>Input:</strong> BIDS or EEG-BIDS, metadata, and QC logs</li>
<li><strong>Procedure:</strong> a fixed pipeline, execution logs, and documented failure cases</li>
<li><strong>Output:</strong> metrics, baseline deltas, and the result of falsification conditions</li>
</ul>
</div>
<p>If you want to see how those three parts connect in a single EEG example, the shortest route is <a href="wiki/verification-example-walkthrough.html">Wiki: Verification example walkthrough</a>.</p>
</section>

<section class="section" id="q4">
<h2 class="section-title">Q. Why is standardization so important?</h2>
<p>
A. Without standards, people appear to be talking about the same thing while actually comparing different inputs, different procedures, and different metrics. Once that happens, progress becomes unreadable.
</p>
<p>
Examples such as the PDB and the BIDS + OpenNeuro ecosystem differ in field, but they share the same crucial property: they turned progress into something different groups could measure in comparable ways. The <a href="verification.html#casework">casework collection</a> summarizes the design pattern, and if you want the role differences among BIDS, OpenNeuro, validators, and benchmarks first, the shortest path is <a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: Standards, repositories, validators, and benchmarks</a>.
</p>
</section>

<section class="section" id="q5">
<h2 class="section-title">Q. What is the “benchmark trap”?</h2>
<p>
A. It is the phenomenon where winning on a metric drifts away from the real goal, a version of Goodhart's law. For example, the score may go up because of data leakage or overfitting, or the system may be too costly to deploy in practice. Mind-Upload treats failure cases, leakage checks, and model cards as part of the benchmark design itself.
</p>
<p><a href="wiki/dataset-splits-and-leakage.html">Wiki: Dataset splits and data leakage</a> collects typical ways the numbers break when train/test separation is poorly designed.</p>
</section>

<section class="section" id="q5b">
<h2 class="section-title">Q. If offline accuracy is high, is that enough for closed loop?</h2>
<p>
A. No. In a closed loop, the output changes the next input and often the environment as well, so end-to-end latency, jitter, drift, and safe-stop behavior all matter. A method can work well on recorded data and still fail to operate stably in real time.
</p>
<p>
Recent speech neuroprosthesis work made major progress in real-time text, audio, and voice output. Littlejohn et al. (2025) showed streaming brain-to-voice output every 80 ms, and Wairagkar et al. (2025) showed neural-to-voice synthesis under 10 ms. But those are within-session achievements in invasive communication subsystems, not general evidence for WBE. As Wilson et al. (2025) shows, whether such systems can be maintained long-term while reducing daily supervised recalibration is a separate question.
</p>
<p>
At Mind-Upload, offline accuracy and L3 closed-loop stability are read separately. In particular, if the work does not report <strong>P50/P95/P99 latency</strong>, <strong>silence or abstention behavior</strong>, <strong>recalibration burden</strong>, and <strong>cross-day degradation</strong> apart from accuracy, we do not read it as a deployable closed loop. For a beginner-friendly version of that distinction, see <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: Closed loop, latency, jitter, and safe stops</a>.
</p>
</section>

<section class="section" id="q5c">
<h2 class="section-title">Q. If latency is low, does that mean the body/environment problem is solved?</h2>
<p>
A. No. Low latency only tells you that one loop is fast enough; it does not tell you that the relevant <strong>subject boundary</strong> has been reproduced. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> and <a href="https://doi.org/10.1126/science.aav7893" target="_blank">Stringer et al. (2019)</a> showed that ongoing behavior shapes a large fraction of cortical activity, <a href="https://doi.org/10.1038/nn.3567" target="_blank">Saleem et al. (2013)</a> and <a href="https://doi.org/10.1126/science.1232655" target="_blank">Ravassard et al. (2013)</a> showed that locomotion, optic flow, vestibular, and other sensory cues reshape cortical and hippocampal codes, <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">Zelano et al. (2016)</a> showed that nasal respiration entrains human limbic activity and modulates memory, and <a href="https://doi.org/10.1126/science.abd0380" target="_blank">Flesher et al. (2021)</a> showed that adding tactile feedback improves a local bidirectional BCI loop.
</p>
<p>
At Mind-Upload, a closed-loop paper that does not disclose <strong>which sensory, motor, and interoceptive channels were preserved, substituted, or omitted</strong>, plus what happened when those loops were removed or altered, stays a <strong>local controller</strong> or <strong>local subsystem-loop</strong> result. The shortest follow-up is <a href="verification.html#body-environment-boundary-card">Verification: Body / Environment Boundary Card</a> together with <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html#boundary-before-latency">Wiki: before milliseconds, fix which loop boundary was actually preserved</a>, <a href="tech_roadmap.html#qa-m4">Roadmap M4</a>, and <a href="tech_roadmap.html#qa-i6">Roadmap I6</a>.
</p>
</section>

<section class="section" id="q6">
<h2 class="section-title">Q. What is the site's stance on the hard problem of consciousness?</h2>
<p>
A. Mind-Upload does not assume any specific philosophical stance on the hard problem of consciousness (Chalmers, 1995). It uses a functionalist approach as an implementation basis, but it does not claim that functional equivalence is sufficient for phenomenal consciousness. Instead, it evaluates <strong>verifiable operational indicators</strong> such as PCI-ST, counterfactual tests, and agreement under intervention, and leaves philosophical consequences to the interpretation stage once there is enough empirical data.
</p>
<div class="note-box">
<strong>Transparency</strong>
<p>
This is a serious limitation. Even if functional equivalence is confirmed, the identity of phenomenal consciousness is not guaranteed. The site states that limit explicitly and then accumulates only the progress that can still be measured.
</p>
</div>
</section>

<section class="section" id="q7">
<h2 class="section-title">Q. How do you handle the copy problem?</h2>
<p>
A. In a scan-and-copy route, the original and the copy branch immediately after the copy is made, so there is no principled way to decide which one is “the person” in the strong sense associated with identity debates. Mind-Upload therefore centers <strong>slow continuous mind uploading</strong> as a design strategy, treating continuity of process without abrupt rupture as an engineering requirement.
</p>
<p>
Even then, the strategy still needs a pre-fixed criterion for when the transfer is complete. Mind-Upload treats that as part of the L4 claim ladder rather than as something already solved.
</p>
</section>

<section class="section" id="q8">
<h2 class="section-title">Q. What happened with experimental tests of IIT and GNWT?</h2>
<p>
A. The 2025 Cogitate Consortium adversarial collaboration tested predictions from IIT and GNWT at large scale. The result was that <strong>neither theory received full support</strong>: IIT's posterior cortical sustained activity received only partial support, while GNWT's prefrontal ignition remained difficult to separate from report-related activity. In response, Mind-Upload avoids overcommitting to any one theory and instead emphasizes theory-light empirical indicators such as PCI.
</p>
<p>If you want the theory map itself first, <a href="wiki/consciousness-theory-map.html">Wiki: Consciousness theory map</a> is the shortest route.</p>
</section>

<section class="section" id="q9">
<h2 class="section-title">Q. How does the site treat ethical issues?</h2>
<p>
A. WBE brings its own ethical issues, including (1) the legal status and rights of emulated beings, (2) whether consent can be withdrawn, including the right to stop, (3) the ethics of multiple copies, and (4) access inequality and social justice. Mind-Upload places the design of <strong>ethical review and governance</strong> as a prerequisite for L5 social deployment while focusing current effort on the technical foundation in L0-L2.
</p>
</section>

<section class="section" id="q10">
<h2 class="section-title">Q. How is this different from other WBE-related projects?</h2>
<p>
A. Relative to several major existing efforts, the rough distinction is:
</p>
<ul>
<li><strong>Blue Brain / Human Brain Project:</strong> more focused on large-scale simulation. Mind-Upload differs by prioritizing the verification framework first.</li>
<li><strong>Whole Brain Architecture Initiative (WBAI):</strong> more focused on constructive architecture and roadmap work. Mind-Upload is complementary in that it fixes benchmarks and falsification conditions early.</li>
<li><strong>OpenWorm:</strong> focused on full-connectome implementation for <em>C. elegans</em>. Mind-Upload instead starts from non-invasive human-brain measurement, especially EEG.</li>
</ul>
<p>
The distinguishing strategy of Mind-Upload is <strong>to build the Verification Commons first</strong>.
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">References (FAQ)</h2>
<ol>
<li>Tang, J., et al. (2023). Semantic reconstruction from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Mahjoory, K., Nikulin, V. V., Botrel, L., et al. (2017). Consistency of EEG source localization and connectivity estimates. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.076" target="_blank">doi:10.1016/j.neuroimage.2017.02.076</a></li>
<li>Mikulan, E., Russo, S., Parmigiani, S., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Frässle, S., Paulus, F. M., Krach, S., &amp; Jansen, A. (2016). Test-retest reliability of effective connectivity in the face perception network. <a href="https://doi.org/10.1002/hbm.23061" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle, S., Manjaly, Z. M., Do, C. T., Kasper, L., Pruessmann, K. P., &amp; Stephan, K. E. (2021). Whole-brain estimates of directed connectivity for human connectomics. <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Wu, H., Hu, X., &amp; Zeng, Y. (2024). A fast dynamic causal modeling regression method for fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">doi:10.1016/j.neuroimage.2024.120954</a></li>
<li>Jafarian, A., Assem, M. K., Kocagoncu, E., et al. (2024). Reliability of dynamic causal modelling of resting-state magnetoencephalography. <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Gouwens, N. W., et al. (2021). Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <a href="https://doi.org/10.1038/s41467-024-47838-5" target="_blank">doi:10.1038/s41467-024-47838-5</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">doi:10.1038/s41593-023-01558-3</a></li>
<li>Hardingham, N. R., &amp; Larkman, A. U. (1998). The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. <a href="https://doi.org/10.1111/j.1469-7793.1998.249bu.x" target="_blank">doi:10.1111/j.1469-7793.1998.249bu.x</a></li>
<li>Volgushev, M., Vidyasagar, T. R., Chistiakova, M., Yousef, T., &amp; Eysel, U. T. (2000). Membrane properties and spike generation in rat visual cortical cells during reversible cooling. <a href="https://doi.org/10.1111/j.1469-7793.2000.00059.x" target="_blank">doi:10.1111/j.1469-7793.2000.00059.x</a></li>
<li>Moser, E., Mathiesen, I., &amp; Andersen, P. (1993). Association between brain temperature and dentate field potentials in exploring and swimming rats. <a href="https://doi.org/10.1126/science.8446900" target="_blank">doi:10.1126/science.8446900</a></li>
<li>Long, M. A., &amp; Fee, M. S. (2008). Using temperature to analyse temporal dynamics in the songbird motor pathway. <a href="https://doi.org/10.1038/nature07448" target="_blank">doi:10.1038/nature07448</a></li>
<li>Rangaraju, V., Calloway, N., &amp; Ryan, T. A. (2014). Activity-driven local ATP synthesis is required for synaptic function. <a href="https://doi.org/10.1016/j.cell.2013.12.042" target="_blank">doi:10.1016/j.cell.2013.12.042</a></li>
<li>Rangaraju, V., Lauterbach, M., &amp; Schuman, E. M. (2019). Spatially stable mitochondrial compartments fuel local translation during plasticity. <a href="https://doi.org/10.1016/j.cell.2018.12.013" target="_blank">doi:10.1016/j.cell.2018.12.013</a></li>
<li>Divakaruni, S. S., Van Dyke, A. M., Chandra, R., et al. (2018). Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. <a href="https://doi.org/10.1016/j.neuron.2018.09.025" target="_blank">doi:10.1016/j.neuron.2018.09.025</a></li>
<li>Bapat, P., Nirschl, J. J., Wilkerson, J. R., et al. (2024). VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. <a href="https://doi.org/10.1038/s41467-023-44233-8" target="_blank">doi:10.1038/s41467-023-44233-8</a></li>
<li>Hu, H., Tang, J., Wu, Y., et al. (2025). Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. <a href="https://doi.org/10.1038/s42003-025-08963-3" target="_blank">doi:10.1038/s42003-025-08963-3</a></li>
<li>Park, M., Salgado, J. M., Ostroff, L., Helton, T. D., Robinson, C. G., Harris, K. M., &amp; Ehlers, M. D. (2006). Plasticity-induced growth of dendritic spines by exocytic trafficking from recycling endosomes. <a href="https://doi.org/10.1016/j.neuron.2006.09.040" target="_blank">doi:10.1016/j.neuron.2006.09.040</a></li>
<li>Zhao, J., Fok, A. H. K., Fan, R., Kwan, P.-Y., Chan, H.-L., Lo, L. H.-Y., Chan, Y.-S., Yung, W.-H., Huang, J., Lai, C. S. W., &amp; Lai, K.-O. (2020). Specific depletion of the motor protein KIF5B leads to deficits in dendritic transport, synaptic plasticity and memory. <a href="https://doi.org/10.7554/eLife.53456" target="_blank">doi:10.7554/eLife.53456</a></li>
<li>Swarnkar, S., Avchalumov, Y., Espadas, I., Grinman, E., Liu, X.-A., Raveendra, B. L., Zucca, A., Mediouni, S., Sadhu, A., Valente, S., Page, D., Miller, K., &amp; Puthanveettil, S. V. (2021). Molecular motor protein KIF5C mediates structural plasticity and long-term memory by constraining local translation. <a href="https://doi.org/10.1016/j.celrep.2021.109369" target="_blank">doi:10.1016/j.celrep.2021.109369</a></li>
<li>Rzechorzek, N. M., Thrippleton, M. J., Chappell, F. M., et al. (2022). A daily temperature rhythm in the human brain predicts survival after brain injury. <a href="https://doi.org/10.1093/brain/awab466" target="_blank">doi:10.1093/brain/awab466</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Qian, Y., Zhao, T., Zheng, H., Weimer, J., &amp; Boada, F. E. (2012). High-resolution sodium imaging of human brain at 7 T. <a href="https://doi.org/10.1002/mrm.23225" target="_blank">doi:10.1002/mrm.23225</a></li>
<li>Qian, Y., Lin, Y.-C., Chen, X., et al. (2025). Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. <a href="https://doi.org/10.1038/s41598-025-07800-1" target="_blank">doi:10.1038/s41598-025-07800-1</a></li>
<li>Suzuki, A., et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">doi:10.1016/j.cell.2011.02.018</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Lee, J.-C., Wang, C.-Y., Lin, C.-L., &amp; Lu, H.-C. (2022). Synaptic memory survives molecular turnover. <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">doi:10.1073/pnas.2211572119</a></li>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Mostert, P., Albers, A. M., Brinkman, L., Todorova, L., &amp; de Lange, F. P. (2018). Eye Movement-Related Confounds in Neural Decoding of Visual Working Memory Representations. <a href="https://doi.org/10.1523/ENEURO.0401-17.2018" target="_blank">doi:10.1523/ENEURO.0401-17.2018</a></li>
<li>McFarland, D. J., McCane, L. M., David, S. V., &amp; Wolpaw, J. R. (2005). Brain-computer interface operation: signal and noise during early training sessions. <a href="https://doi.org/10.1088/1741-2560/2/4/014" target="_blank">doi:10.1088/1741-2560/2/4/014</a></li>
<li>Chaibub Neto, E., Pratap, A., Perumal, T. M., et al. (2019). Identity confounding in machine learning can be controlled by design. <a href="https://doi.org/10.1038/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu, M., Fanton, S., Jahanbekam, A., et al. (2020). The Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. <a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., et al. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Yücel, M. A., Selb, J., Huppert, T. J., Franceschini, M. A., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>Epp, S. M., Halani, S., Paquette, M., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., &amp; Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: A simulation study. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva, J. M., Wang, S. H., Palva, S., Zhigalov, A., Monto, S., Brookes, M. J., Schoffelen, J.-M., &amp; Jerbi, K. (2018). Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Ye, S., Kitajo, K., &amp; Kitano, K. (2020). Information-theoretic approach to detect directional information flow in EEG signals induced by TMS. <a href="https://doi.org/10.1016/j.neures.2019.09.003" target="_blank">doi:10.1016/j.neures.2019.09.003</a></li>
<li>Miljevic, A., Murphy, O. W., Fitzgerald, P. B., &amp; Bailey, N. W. (2025). Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. <a href="https://doi.org/10.1016/j.clinph.2025.03.043" target="_blank">doi:10.1016/j.clinph.2025.03.043</a></li>
<li>Bérut, A., Arakelyan, A., Petrosyan, A., et al. (2012). Experimental verification of Landauer&rsquo;s principle linking information and thermodynamics. <a href="https://doi.org/10.1038/nature10872" target="_blank">doi:10.1038/nature10872</a></li>
<li>Attwell, D., &amp; Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">doi:10.1097/00004647-200110000-00001</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., et al. (2021). Broken detailed balance and entropy production in the human brain. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>Deco, G., Sanz Perl, Y., Bocaccio, H., Tagliazucchi, E., &amp; Kringelbach, M. L. (2022). The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">doi:10.1038/s42003-022-03505-7</a></li>
<li>de la Fuente, L. A., Zamberlan, F., Bocaccio, H., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., Bonetti, L., Fernández-Rubio, G., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Grubb, M. S., &amp; Burrone, J. (2010). Activity-dependent relocation of the axon initial segment fine-tunes neuronal excitability. <a href="https://doi.org/10.1038/nature09160" target="_blank">doi:10.1038/nature09160</a></li>
<li>Thomas, C., Ye, F. Q., Irfanoglu, M. O., Modi, P., Saleem, K. S., Leopold, D. A., &amp; Pierpaoli, C. (2014). Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. <a href="https://doi.org/10.1073/pnas.1405672111" target="_blank">doi:10.1073/pnas.1405672111</a></li>
<li>Reveley, C., Seth, A. K., Pierpaoli, C., Silva, A. C., Yu, D., Saunders, R. C., Leopold, D. A., &amp; Ye, F. Q. (2015). Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. <a href="https://doi.org/10.1073/pnas.1418198112" target="_blank">doi:10.1073/pnas.1418198112</a></li>
<li>Donahue, C. J., Sotiropoulos, S. N., Jbabdi, S., Hernandez-Fernandez, M., Behrens, T. E., Dyrby, T. B., Coalson, T., Kennedy, H., Knoblauch, K., Van Essen, D. C., &amp; Glasser, M. F. (2016). Using diffusion tractography to predict cortical connection strength and distance: A quantitative comparison with tracers in the monkey. <a href="https://doi.org/10.1523/JNEUROSCI.0493-16.2016" target="_blank">doi:10.1523/JNEUROSCI.0493-16.2016</a></li>
<li>Schilling, K. G., Petit, L., Rheault, F., Remedios, S., Pierpaoli, C., Anderson, A. W., Landman, B. A., &amp; Descoteaux, M. (2020). Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. <a href="https://doi.org/10.1007/s00429-020-02129-z" target="_blank">doi:10.1007/s00429-020-02129-z</a></li>
<li>Grisot, G., Haber, S. N., Hawrylycz, M., Yendiki, A., et al. (2021). Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. <a href="https://doi.org/10.1016/j.neuroimage.2021.118300" target="_blank">doi:10.1016/j.neuroimage.2021.118300</a></li>
<li>Huber, R., Mäki, H., Rosanova, M., Casarotto, S., Canali, P., Casali, A. G., Tononi, G., &amp; Massimini, M. (2013). Human cortical excitability increases with time awake. <a href="https://doi.org/10.1093/cercor/bhs014" target="_blank">doi:10.1093/cercor/bhs014</a></li>
<li>Kuhn, M., Wolf, E., Maier, J. G., Mainberger, F., Feige, B., Schmid, H., et al. (2016). Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. <a href="https://doi.org/10.1038/ncomms12455" target="_blank">doi:10.1038/ncomms12455</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Fehér, K. D., Henckaerts, P., Hirsch, V., Bucsenez, U., Kuhn, M., Maier, J. G., et al. (2026). A nap can recalibrate homeostatic and associative synaptic plasticity in the human cortex. <a href="https://doi.org/10.1016/j.neuroimage.2026.121723" target="_blank">doi:10.1016/j.neuroimage.2026.121723</a></li>
<li>Santoni, G., et al. (2024). Chromatin plasticity predetermines neuronal eligibility for memory trace formation. <a href="https://doi.org/10.1126/science.adg9982" target="_blank">doi:10.1126/science.adg9982</a></li>
<li>Govindarajan, A., Israely, I., Huang, S.-Y., &amp; Tonegawa, S. (2011). The dendritic branch is the preferred integrative unit for protein synthesis-dependent LTP. <a href="https://doi.org/10.1016/j.neuron.2010.12.008" target="_blank">doi:10.1016/j.neuron.2010.12.008</a></li>
<li>Frischknecht, R., Heine, M., Perrais, D., Seidenbecher, C. I., Choquet, D., &amp; Gundelfinger, E. D. (2009). Brain extracellular matrix affects AMPA receptor lateral mobility and short-term synaptic plasticity. <a href="https://doi.org/10.1038/nn.2338" target="_blank">doi:10.1038/nn.2338</a></li>
<li>Glykys, J., Dzhala, V., Egawa, K., et al. (2014). Local impermeant anions establish the neuronal chloride concentration. <a href="https://doi.org/10.1126/science.1245423" target="_blank">doi:10.1126/science.1245423</a></li>
<li>Seidl, A. H., Rubel, E. W., &amp; Barria, A. (2015). Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. <a href="https://doi.org/10.1038/ncomms9073" target="_blank">doi:10.1038/ncomms9073</a></li>
<li>Stringer, C., Pachitariu, M., Steinmetz, N., et al. (2019). Spontaneous behaviors drive multidimensional, brainwide activity. <a href="https://doi.org/10.1126/science.aav7893" target="_blank">doi:10.1126/science.aav7893</a></li>
<li>Saleem, A. B., Ayaz, A., Jeffery, K. J., Harris, K. D., &amp; Carandini, M. (2013). Integration of visual motion and locomotion in mouse visual cortex. <a href="https://doi.org/10.1038/nn.3567" target="_blank">doi:10.1038/nn.3567</a></li>
<li>Ravassard, P., Kees, A., Willers, B., et al. (2013). Multisensory control of hippocampal spatiotemporal selectivity. <a href="https://doi.org/10.1126/science.1232655" target="_blank">doi:10.1126/science.1232655</a></li>
<li>Zelano, C., Jiang, H., Zhou, G., et al. (2016). Nasal respiration entrains human limbic oscillations and modulates cognitive function. <a href="https://doi.org/10.1523/JNEUROSCI.2586-16.2016" target="_blank">doi:10.1523/JNEUROSCI.2586-16.2016</a></li>
<li>Flesher, S. N., Downey, J. E., Weiss, J. M., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Raut, R. V., Rosenthal, Z. P., Wang, X., et al. (2025). Arousal as a universal embedding for spatiotemporal brain dynamics. <a href="https://doi.org/10.1038/s41586-025-09544-4" target="_blank">doi:10.1038/s41586-025-09544-4</a></li>
<li>Guo, C., Pleiss, G., Sun, Y., &amp; Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. <a href="https://proceedings.mlr.press/v70/guo17a.html" target="_blank">PMLR 70:1321-1330</a></li>
<li>Geifman, Y., &amp; El-Yaniv, R. (2017). Selective Classification for Deep Neural Networks. <a href="https://papers.neurips.cc/paper/7073-selective-classification-for-deep-neural-networks" target="_blank">NeurIPS 2017</a></li>
<li>Ji, Z., et al. (2023). Survey of Hallucination in NLG. <a href="https://doi.org/10.1145/3571730" target="_blank">doi:10.1145/3571730</a></li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested Counterfactual Identification. <a href="https://arxiv.org/abs/2107.03190" target="_blank">arXiv:2107.03190</a></li>
<li>Gorgolewski, K. J., et al. (2016). BIDS. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Casali, A. G., et al. (2013). PCI. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Chalmers, D. J. (1995). Facing up to the problem of consciousness. <em>Journal of Consciousness Studies</em>, 2(3), 200-219.</li>
<li>Parfit, D. (1984). <em>Reasons and Persons</em>. Oxford University Press.</li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Shortcuts</h4>
<ul>
<li><a href="index.html">Start →</a></li>
<li><a href="verification.html">Verification →</a></li>
<li><a href="wbe_101.html">WBE 101 →</a></li>
<li><a href="eeg_101.html">EEG 101 →</a></li>
<li><a href="datasets.html">Datasets →</a></li>
<li><a href="glossary.html">Glossary →</a></li>
</ul>
</div>

</aside>
</main>
