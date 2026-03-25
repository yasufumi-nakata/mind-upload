---
layout: default
title: "Wiki: State-Continuity Bridge"
description: "Explains why same-subject or same-brain sequential workflows do not automatically become same-state evidence, and how Mind-Upload audits acquisition order, bridge delay, regime continuity, deformation, validation, and residual drift."
article_type: Wiki
subtitle: "Same-subject solves specimen identity, not same-state continuity"
author: Mind Uploading Research Project
last_updated: "2026-03-25"
note: "Technical / natural science only"
audience: "Readers who want to read live-to-fix, same-brain plus EM, and cross-day reacquisition claims without overpromoting specimen identity into state continuity"
reading_time: "12-18 min"
page_intro: "This page explains why a result can be same-subject or same-brain and still fail to be one state sample. The bridge problem appears whenever a claim depends on linking measurements acquired at different times, under different regimes, or after tissue transformation."
accuracy_note: "The bridge ceilings on this page are site-level inferences drawn from primary literature about preservation, correlative registration, spontaneous state fluctuation, and biological turnover."
page_highlights:
  - "Specimen identity, time continuity, regime continuity, and coordinate continuity are different claims."
  - "Preservation and fixation are not neutral storage steps; they can change geometry, membrane integrity, and downstream observability."
  - "Correlative same-brain pipelines are scientifically valuable local workflows, but they are still sequential bridges rather than simultaneous whole-state capture."
  - "Cross-day reacquisition also needs a bridge audit, because spontaneous behavior, arousal, and day-night variation can move the observed state before long-term drift is even discussed."
  - "Bridge burden is not one scalar: live-to-fix bridges are transformation-dominated, whereas same-day or overnight live bridges are drift-dominated and expose different hidden-state families."
  - "On this site, the State-Continuity Bridge Card is stacked with the Destructive-Structure Route Card, Human Proxy Composition Card, or Temporal Validity Card depending on the bridge."
known_points:
  - "Preservation route and fixation protocol materially affect ultrastructural geometry and downstream staining or registration."
  - "Correlative live-to-EM workflows need explicit landmarks, targeted subvolumes, and bridge validation rather than a simple same-brain label."
  - "Adult synaptic structures and ongoing behavioral state can change over bridge windows that are relaxed or left implicit."
  - "Same-subject wording can support specimen identity while still failing same-state continuity."
  - "Different bridge classes threaten different state families first, so elapsed time alone is not a sufficient bridge summary."
unknown_points:
  - "There is still no general bridge protocol that yields field-ready same-state evidence across live, ex vivo, and destructive stages at whole-brain scale."
  - "Which hidden-state families are tolerable to bridge by calibration rather than direct measurement remains unresolved."
  - "The strongest bridge-validation rung achievable in living humans is still limited and route-dependent."
wiki_links:
  - label: "Wiki: Human Proxy Composition and Route Maturity"
    url: "/wiki/human-proxy-composition.html"
    description: "Use this when several living-human proxy rows are combined and the bridge problem is one part of a larger composition problem."
  - label: "Wiki: State, Trait, And Drift"
    url: "/wiki/state-trait-and-drift.html"
    description: "Use this when the bridge crosses hours to days and temporal validity rather than specimen transformation becomes the main problem."
  - label: "Wiki: Observability And Claim Ceiling By Measurement Stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Places bridge-limited claims inside the broader modality ceiling table."
  - label: "Wiki: Homeostatic Plasticity And Maintenance State"
    url: "/wiki/homeostatic-plasticity-and-maintenance-state.html"
    description: "Lists the hidden-state families that can drift across a bridge window."
recommended_pages:
  - label: "Verification"
    url: "/verification.html"
  - label: "WBE 101"
    url: "/wbe_101.html"
  - label: "Technical Roadmap"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Shortest conclusion</h2>
<p>
On this site, <strong>same-subject</strong> or <strong>same-brain</strong> never means <strong>same-state</strong> by default. A bridge must separately justify <strong>time continuity</strong>, <strong>physiological-regime continuity</strong>, <strong>coordinate continuity</strong>, and <strong>bridge validation</strong>; otherwise the result stays at the ceiling of the strongest directly supported stage plus, at most, an unvalidated bridge hypothesis.
</p>
</div>

<div class="key-points">
<h4>Four Bridge Failures To Stop Early</h4>
<ul>
<li><strong>Specimen identity is not time identity:</strong> the same brain can be sampled at different states.</li>
<li><strong>Fixation is not neutral storage:</strong> preservation can alter geometry and observability.</li>
<li><strong>Same-brain registration is not deformation-free correspondence:</strong> landmarks and warping matter.</li>
<li><strong>A careful correlative workflow is not yet validated same-state evidence:</strong> bridge validation itself needs a rung.</li>
</ul>
</div>

<div class="note-box">
<strong>How this page fits the site</strong>
<p>
The operational submission rule lives in <a href="../verification.html#state-continuity-bridge-card">Verification: State-Continuity Bridge Card</a>. This wiki is the background page for that card. If your main problem is several human proxy rows moving together, go next to <a href="../wiki/human-proxy-composition.html">Wiki: Human Proxy Composition and Route Maturity</a>. If your main problem is longitudinal performance across hours or days, add <a href="../wiki/state-trait-and-drift.html">Wiki: State, Trait, and Drift</a>.
</p>
</div>

<div class="note-box">
<strong>What this page does not do</strong>
<p>
This page does not discuss personal identity, law, or ethics. The question here is narrower: <strong>when is a sequential bridge scientifically strong enough to support same-state language, and when is it not?</strong>
</p>
</div>

<section class="section" id="continuity-dimensions">
<h2 class="section-title">One bridge, four different continuity claims</h2>
<p>
The core overread is to collapse several continuity questions into one label such as <strong>same-subject</strong> or <strong>same-brain</strong>. The site now separates them explicitly.
</p>
<table class="data-table">
<thead>
<tr>
<th>Continuity claim</th>
<th>What must actually be true</th>
<th>What fails if it is only assumed</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Specimen continuity</strong></td>
<td>The later sample really came from the same subject or the same brain volume lineage.</td>
<td>You know which specimen it is, but not whether it remained in the same state.</td>
</tr>
<tr>
<td><strong>Time continuity</strong></td>
<td>The acquisitions were close enough in time, with a named window and named hidden-state risks.</td>
<td>Cross-day or live-to-fix gaps can silently cross synaptic, excitability, sleep, or support-state change windows.</td>
</tr>
<tr>
<td><strong>Regime continuity</strong></td>
<td>Task, arousal, sleep pressure, anesthesia, pharmacology, recovery status, and perturbation regime were matched or explicitly shifted.</td>
<td>The same specimen may still be measured under biologically different states.</td>
</tr>
<tr>
<td><strong>Coordinate continuity</strong></td>
<td>The mapping from live to later space is disclosed through landmarks, deformation model, and residual mismatch.</td>
<td><strong>Same-brain</strong> language overstates correspondence precision and can hide shrinkage or registration error.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="literature">
<h2 class="section-title">What the primary literature now supports</h2>

<h3>1. Preservation is an intervention, not a neutral storage step</h3>
<p>
The first reason the bridge needs its own audit is that preservation itself can change the object being measured. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> did not treat fixation as a transparent handoff; they explicitly showed that conventional fixation causes extracellular-space loss and proposed a different transcardial strategy because preservation route changes downstream ultrastructure and staining quality. <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">Idziak et al. (2023)</a> then used a live-versus-fixed comparison in hippocampal slices and found subtle spine-morphology changes plus substantial membrane damage after chemical fixation. On this site, that means a bridge from live to fixed tissue is not merely a time stamp. It is a change of preparation that can alter geometry and observability.
</p>

<h3>2. Correlative same-brain workflows are multistage local bridges</h3>
<p>
The second reason is that powerful same-brain pipelines are still sequential. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a> linked in vivo two-photon physiology to synchrotron microtomography and serial block-face EM through a multistage landmark-based workflow with targeted subvolumes. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> reconstructed a remarkable human cortical fragment, but still from a rapidly preserved local surgical sample rather than a living whole-brain in vivo measurement. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> likewise made the bridge stronger, not magical: same-brain function plus EM remained a sequential local pipeline from in vivo measurements to later ex vivo reconstruction. Therefore, same-brain wording can justify local specimen linkage without justifying same-state language.
</p>

<h3>3. Relaxed bridge windows can cross real biological turnover windows</h3>
<p>
The third reason is biological turnover. <a href="https://doi.org/10.1038/nature14467" target="_blank">Attardo et al. (2015)</a> showed that adult CA1 spine dynamics are compatible with mean lifetimes on the order of <strong>1-2 weeks</strong>, implying near-complete turnover over a few multiples of that interval. The exact numbers are not the point here; the point is that a bridge window cannot be treated as biologically silent unless the relevant state family is named and bounded. A live measurement plus a later fixation, or one session plus a later reacquisition, can cross windows in which structure or support-state has genuinely changed.
</p>

<h3>4. Cross-day reacquisition is also a bridge problem</h3>
<p>
The bridge problem is not limited to destructive follow-up. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> showed that richly varied movements dominate much of single-trial cortical variance during task performance. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a> showed that spontaneous behavior changes not only signal magnitude but also functional-connectivity structure. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> then showed 10-hour EEG dynamics that materially affect decoding and motivate adaptive decoders. Therefore, even when the measurement stack itself stays live and non-destructive, a cross-day or within-day bridge still needs state annotation and regime disclosure before it is promoted to trait or same-state language.
</p>
</section>

<section class="section" id="validation-rungs">
<h2 class="section-title">Bridge validation is a rung, not a checkbox</h2>
<p>
The site now reads bridge validation as graded rather than binary. These rungs are operational inferences from the primary literature above; they are not labels used by the original papers themselves.
</p>
<table class="data-table">
<thead>
<tr>
<th>Validation rung</th>
<th>What is actually shown</th>
<th>Remaining ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Rung 0: specimen identity only</strong></td>
<td>The later sample is from the same subject or same brain, but the bridge itself is not independently validated.</td>
<td><strong>Strongest directly supported stage</strong> plus, at most, an <strong>unvalidated bridge hypothesis</strong>.</td>
</tr>
<tr>
<td><strong>Rung 1: repeated live continuity under one regime</strong></td>
<td>A repeated live measurement narrows one source of time drift under a matched task or arousal regime.</td>
<td>Same-regime live continuity only; not live-to-fix or cross-regime same-state evidence.</td>
</tr>
<tr>
<td><strong>Rung 2: coarse landmark recovery</strong></td>
<td>Vessels, anatomy, probe location, or gross landmarks are recovered across stages.</td>
<td>Region-level or subvolume-level bridge, not cell-precise or deformation-free correspondence.</td>
</tr>
<tr>
<td><strong>Rung 3: targeted local correspondence</strong></td>
<td>Specific cells, stimulation sites, or targeted subvolumes are linked across stages with explicit correspondence rules.</td>
<td>Local bridge evidence only; still sequential and not whole-state capture.</td>
</tr>
<tr>
<td><strong>Rung 4: correspondence plus matched perturbation or repeated validation</strong></td>
<td>The bridge is checked not only anatomically but also against a repeated or perturbation-linked relation that would fail if the bridge drifted too far.</td>
<td>Strongest currently plausible <strong>local</strong> same-bridge evidence, still below whole-brain or maintenance-complete continuity.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="risk-matrix">
<h2 class="section-title">Bridge risk is family-specific, not one scalar</h2>
<p>
One remaining weakness in the public bridge rule was that <strong>bridge burden</strong> could still sound like one generic time penalty. The primary literature does not support that shortcut. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> and <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">Idziak et al. (2023)</a> show that live-to-fix bridges are already <strong>transformation-dominated</strong>, because preservation route, fixation duration, and membrane integrity can change geometry and observability before a long delay even appears. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a> and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> then show that same-brain function-plus-structure pipelines are landmark- and deformation-heavy <strong>local bridges</strong>. By contrast, <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a>, <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a>, and <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> show that repeated live measurements can drift through movement, arousal, connectivity structure, and decoder-relevant EEG dynamics within hours. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> and <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a> further show that sleep/wake crossing changes homeostatic and computational regime rather than merely adding more elapsed time. Therefore, on this site, bridge audit starts by asking <strong>what kind of bridge this is</strong> and <strong>which hidden-state families it exposes first</strong>.
</p>
<div class="note-box">
<strong>Site-level inference</strong>
<p>
The matrix below is an operational inference from the primary literature above plus the site's maintenance-state taxonomy. It is not a label used by the original papers themselves.
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>Bridge class</th>
<th>What changes first</th>
<th>Hidden-state families to name first</th>
<th>Cards this site stacks by default</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Live -&gt; fixation -&gt; ex vivo / EM</strong></td>
<td>Preservation route, extracellular-space retention, membrane integrity, staining compatibility, deformation, and registration precision.</td>
<td>Structural observability itself, omitted live physiology, and whatever state family the paper wants to carry across fixation.</td>
<td><strong>State-Continuity Bridge Card</strong> plus <strong>Destructive-Structure Route Card</strong>.</td>
</tr>
<tr>
<td><strong>Same-day repeated live measurement within waking</strong></td>
<td>Movement pattern, arousal / neuromodulatory context, functional-connectivity structure, and decoder-relevant signal statistics.</td>
<td>Behavior-linked state, neuromodulatory context, functional-coupling state, and task / decoder dependence.</td>
<td><strong>State-Continuity Bridge Card</strong> plus <strong>Temporal Validity Card</strong>.</td>
</tr>
<tr>
<td><strong>Sleep-crossing or overnight reacquisition</strong></td>
<td>Firing-rate recovery controller, sleep-dependent renormalization, replay-coupling opportunity, and support-state restoration.</td>
<td>Firing-rate set point, sleep / wake renormalization, sleep architecture / replay-coupling, and support-state families cited by the claim.</td>
<td><strong>State-Continuity Bridge Card</strong> plus <strong>Temporal Validity Card</strong> plus <strong>Maintenance-State Error Budget</strong>.</td>
</tr>
<tr>
<td><strong>Multi-day same-subject proxy bundle</strong></td>
<td>Trait / state mixing, slow structural turnover, support-state drift, and cross-row quantity mismatch.</td>
<td>Structural turnover, maintenance-state families named by the proxy bundle, and human proxy composition ceiling.</td>
<td><strong>State-Continuity Bridge Card</strong> plus <strong>Human Proxy Composition Card</strong> plus <strong>Maintenance-State Error Budget</strong>.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="card-stacking">
<h2 class="section-title">Which other cards stack with the bridge card</h2>
<table class="data-table">
<thead>
<tr>
<th>Scenario</th>
<th>What the bridge problem is</th>
<th>Cards this site stacks together</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Live measurement -&gt; fixation -&gt; ex vivo EM</strong></td>
<td>Time gap, regime shift, tissue transformation, and registration all matter.</td>
<td><strong>State-Continuity Bridge Card</strong> plus <strong>Destructive-Structure Route Card</strong>.</td>
</tr>
<tr>
<td><strong>Several living-human proxy rows acquired on different days or under different regimes</strong></td>
<td>Cross-row composition and bridge validity are both unresolved.</td>
<td><strong>Human Proxy Composition Card</strong> plus <strong>State-Continuity Bridge Card</strong>.</td>
</tr>
<tr>
<td><strong>Cross-day or day-night reacquisition with the same live stack</strong></td>
<td>Behavioral state and decoder or interface drift can move the observed object before any destructive step appears.</td>
<td><strong>State-Continuity Bridge Card</strong> plus <strong>Temporal Validity Card</strong>.</td>
</tr>
<tr>
<td><strong>Same-session multimodal acquisition</strong></td>
<td>The main issue is shared-versus-specific component disclosure rather than a long sequential bridge.</td>
<td><strong>Fusion Card</strong>, and when several human proxy rows are combined, also the <strong>Human Proxy Composition Card</strong>.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="misreadings">
<h2 class="section-title">Common misreadings and demotion rules on this site</h2>
<table class="data-table">
<thead>
<tr>
<th>Dangerous reading</th>
<th>Why it is too strong</th>
<th>How this site demotes it</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>"Same subject" means the same state was sampled twice.</strong></td>
<td>Specimen identity does not bound elapsed time, regime shift, or tissue transformation.</td>
<td>Read as specimen linkage only unless the bridge fields are disclosed.</td>
</tr>
<tr>
<td><strong>"Same brain plus EM" means native state was preserved.</strong></td>
<td>Fixation, staining, sectioning, and registration are all extra interventions.</td>
<td>Read as a sequential local scaffold unless preservation and bridge validation are shown.</td>
</tr>
<tr>
<td><strong>A correlative workflow is automatically a validated bridge.</strong></td>
<td>A workflow can be carefully engineered and still remain unvalidated for the specific state claim being made.</td>
<td>Name the validation rung and keep the ceiling local if the bridge itself is not independently checked.</td>
</tr>
<tr>
<td><strong>A cross-day reacquisition that still decodes well means the same state persisted.</strong></td>
<td>Behavior, arousal, day-night context, and adaptive decoding can hide regime change or rescue drift.</td>
<td>Route through the <a href="../verification.html#temporal-validity-card">Temporal Validity Card</a> as well as the bridge audit.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">References (main)</h2>
<ol>
<li>Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <em>Cell Reports Methods</em>. 2023. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Idziak A, Inavalli VVGK, Bancelin S, Arizono M, Nagerl UV. The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. <em>eNeuro</em>. 2023. <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">doi:10.1523/ENEURO.0104-23.2023</a></li>
<li>Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. <em>Nature Communications</em>. 2022. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <em>Science</em>. 2024. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>. 2025. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Attardo A, Fitzgerald JE, Schnitzer MJ. Impermanence of dendritic spines in live adult CA1 hippocampus. <em>Nature</em>. 2015. <a href="https://doi.org/10.1038/nature14467" target="_blank">doi:10.1038/nature14467</a></li>
<li>Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. <em>Nature Neuroscience</em>. 2019. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <em>Nature Neuroscience</em>. 2024. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Scientific Reports</em>. 2024. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>. 2016. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Xu Y, Schneider A, Wessel R, Hengen KB. Sleep restores an optimal computational regime in cortical networks. <em>Nature Neuroscience</em>. 2024. <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">doi:10.1038/s41593-023-01536-9</a></li>
</ol>
</section>

</article>
</main>
