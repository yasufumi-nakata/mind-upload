---
layout: default
title: "Wiki: Thermodynamic Grounding Basics"
description: "Explains how Mind-Upload separates Landauer limits, tissue energy budgets, neural irreversibility metrics, model-based entropy-flow estimates, and implementation-side power accounting."
article_type: Wiki
subtitle: "Arrow-of-time evidence is informative, but it is not direct physical dissipation by default"
author: Mind Uploading Research Project
last_updated: "2026-03-30"
note: "Technical / natural science only"
audience: "Readers who want a rigorous way to read thermodynamic, irreversibility, or entropy-production language without overpromoting it"
reading_time: "12-18 minutes"
page_intro: "This page explains why thermodynamic language appears on Mind-Upload, what current neural-data papers actually compute, and where the interpretation ceiling still sits."
accuracy_note: "This page treats thermodynamic indicators as auxiliary scientific evidence. It does not treat them as sufficient conditions for identity, consciousness, or WBE success."
page_highlights:
  - "Landauer lower bounds, tissue energy budgets, neural irreversibility metrics, model-based entropy-flow estimates, and implementation-side power accounting are different layers and are not read as one measurement."
  - "The main scientific risk is silent translation: state-space construction, partial observation, reverse-transition sparsity, and physiology-side grounding all change what a thermodynamic number can mean."
  - "Arrow-of-time results remain auxiliary on this site unless the route card names coarse-graining, hidden-degree risk, estimator family, support coverage, and quantity type."
  - "Energetic or metabolic language now requires a separate physiology-side route such as calibrated CMRO2, FDG-PET, or 31P-MRS rather than being inferred from signal asymmetry alone."
  - "A clean null or shuffle control is not the same thing as adequate reverse-transition support."
  - "Implementation-side FLOPs, wall-power, and communication cost stay separate from observation-side nonequilibrium metrics."
known_points:
  - "The biological brain is a continuously driven physical system rather than a static stored object."
  - "Current neural irreversibility papers do report informative nonequilibrium signatures, but they do not all compute the same quantity."
  - "State-space construction, coarse graining, and dynamical assumptions are part of the claim rather than implementation footnotes."
  - "Partial observation can hide dissipative cycles and induce memory, so weak observable currents do not by themselves imply near-equilibrium."
  - "Physiology-side grounding is a separate requirement from observation-side arrow-of-time analysis."
unknown_points:
  - "There is still no field-standard route from neural irreversibility metrics to a stable whole-brain entropy-production estimate."
  - "It remains unresolved which thermodynamic indicators, if any, will prove decision-relevant for stronger WBE claims."
  - "Cross-estimator convergence and physiology-side calibration for energetic interpretations remain open problems."
wiki_links:
  - label: "Wiki: Verification Basics"
    url: "/wiki/verification-basics.html"
    description: "Places thermodynamic indicators inside the wider verification stack."
  - label: "Wiki: Claims and Evidence"
    url: "/wiki/claims-and-evidence.html"
    description: "Explains how auxiliary evidence is kept from silently becoming a stronger claim."
  - label: "Wiki: From Observation to Estimation"
    url: "/wiki/observation-to-estimation.html"
    description: "Explains why observability and model-based inference are separate burdens."
recommended_pages:
  - label: "Verification"
    url: "/verification.html"
  - label: "FAQ"
    url: "/faq.html#q1f"
  - label: "Perspective"
    url: "/perspective.html#design-principles"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Shortest conclusion</h2>
<p>
On this site, thermodynamic language is useful only after it is typed correctly. A paper can show <strong>temporal asymmetry</strong>, a <strong>coarse-grained nonequilibrium lower bound</strong>, or a <strong>model-conditioned entropy-flow estimate</strong> without yet measuring <strong>microscopic physical dissipation</strong>, <strong>brain-wide metabolic cost</strong>, or a <strong>WBE acceptance criterion</strong>.
</p>
</div>

<div class="key-points">
<h4>Three Overreads To Stop Early</h4>
<ul>
<li><strong>Arrow of time is not direct heat dissipation:</strong> observation-side irreversibility and physiology-side energetic cost are different routes.</li>
<li><strong>A clean surrogate is not enough:</strong> reverse-transition support and sparse-data handling are separate burdens.</li>
<li><strong>One thermodynamic word is not one measurement object:</strong> lower bounds, asymmetry scores, graph indices, and model-based entropy-flow estimates answer different questions.</li>
</ul>
</div>

<div class="note-box">
<strong>How this page fits the site</strong>
<p>
This is the background page for the <a href="../verification.html#thermodynamic-verification">Verification: thermodynamic indicators</a> rule and the <a href="#irreversibility-route-card">irreversibility route card</a>. The operational policy lives in Verification; this page explains why that policy is strict.
</p>
</div>

<div class="note-box">
<strong>Scope</strong>
<p>
This page stays on the technology and natural-science side only. It does not use thermodynamic language to settle identity, consciousness, law, or ethics. The narrower question is: <strong>what did the paper actually compute, what assumptions were required, and what ceiling still remains?</strong>
</p>
</div>

<div class="note-box">
<strong>2026-03-30 correction: the real danger is silent translation</strong>
<p>
The main weakness of the older page was not that it mentioned the wrong literature. The weakness was that it still let readers move too quickly across four translations: from <strong>signal asymmetry</strong> to <strong>nonequilibrium inference</strong>, from <strong>coarse-grained inference</strong> to <strong>energetic interpretation</strong>, from <strong>observed trajectory</strong> to <strong>thermodynamic closure</strong>, and from <strong>auxiliary physics signal</strong> to <strong>WBE relevance</strong>. The current primary literature does not support those jumps unless each one is disclosed separately.
</p>
</div>

<section class="section" id="why-thermodynamics">
<h2 class="section-title">Why thermodynamics appears on Mind-Upload at all</h2>
<p>
Mind-Upload does not treat WBE as a static data-storage problem alone. The brain is a continuously driven physical system whose information processing is maintained under non-equilibrium conditions. That is why thermodynamic language appears here. But the site's use is deliberately narrow: thermodynamic indicators are treated as <strong>auxiliary constraints on ongoing physical process</strong>, not as a shortcut to identity, consciousness, or final success conditions.
</p>
</section>

<section class="section" id="layers">
<h2 class="section-title">Five layers that must stay separate</h2>
<table class="data-table">
<thead>
<tr>
<th>Layer</th>
<th>Representative literature</th>
<th>What it can support</th>
<th>What it still cannot support</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Landauer lower bound</strong></td>
<td><a href="https://doi.org/10.1038/nature10872" target="_blank">B&eacute;rut et al. (2012)</a></td>
<td>A lower bound for logically irreversible operations such as bit erasure.</td>
<td>Actual brain power draw, actual emulator wall-power, or a WBE pass condition.</td>
</tr>
<tr>
<td><strong>Tissue-level energy budget</strong></td>
<td><a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">Attwell &amp; Laughlin (2001)</a></td>
<td>A descriptive decomposition of signaling-related energy use in biological tissue.</td>
<td>A universal KPI for digital emulation or a thermodynamic success threshold.</td>
</tr>
<tr>
<td><strong>Observation-side irreversibility metric</strong></td>
<td><a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a>; <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">Deco et al. (2022)</a>; <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a>; <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">Nartallo-Kaluarachchi et al. (2025)</a></td>
<td>Time asymmetry or broken detailed balance under a declared signal route, state-space construction, and estimator family.</td>
<td>Direct microscopic dissipation, direct metabolic cost, or implementation-side efficiency.</td>
</tr>
<tr>
<td><strong>Model-conditioned entropy-flow estimate</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a></td>
<td>A time-varying entropy-flow estimate inside a declared state-space kinetic-Ising model.</td>
<td>Whole-brain direct EPR measurement without model burden.</td>
</tr>
<tr>
<td><strong>Implementation-side cost accounting</strong></td>
<td>Project-specific engineering audit</td>
<td>Wall-power, FLOPs, communication cost, cooling burden, and hardware throughput of the implementation itself.</td>
<td>Observation-side neural irreversibility by itself, unless the bridge is disclosed explicitly.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="translation-gaps">
<h2 class="section-title">Three translation gaps the site now blocks</h2>
<table class="data-table">
<thead>
<tr>
<th>Translation gap</th>
<th>What the primary literature shows</th>
<th>Safe reading on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Estimator label -&gt; thermodynamic meaning</strong></td>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/34789565/" target="_blank">Lynn et al. (2021)</a> estimated entropy production only after coarse-graining BOLD dynamics into clustered macrostates and showed sensitivity to the number of clusters. <a href="https://academic.oup.com/cercor/article/33/5/1856/6577164" target="_blank">de la Fuente et al. (2023)</a> showed that reversibility detection depends on retained principal components, feature family, and classifier complexity. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> added a nonstationary state-space kinetic Ising model precisely because steady-state assumptions fail for neural activity. <a href="https://doi.org/10.1103/PhysRevLett.125.110601" target="_blank">Teza &amp; Stella (2020)</a> and <a href="https://doi.org/10.1103/PhysRevE.105.L042601" target="_blank">Cocconi et al. (2022)</a> showed that coarse graining can preserve or rescale entropy production depending on process class and scale.</td>
<td>An estimator family name alone is too coarse. State-space construction, timescale, and dynamical assumptions belong in the claim.</td>
</tr>
<tr>
<td><strong>Signal irreversibility -&gt; metabolic or energetic interpretation</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> found that about <strong>40%</strong> of voxels with significant task-evoked BOLD changes showed oxygen-metabolism changes in the opposite direction. Observation-side asymmetry therefore does not by itself determine energetic demand.</td>
<td>If the text uses words such as <strong>energy</strong>, <strong>metabolism</strong>, or <strong>dissipation cost</strong>, it must name a physiology-side route such as calibrated CMRO<sub>2</sub>, FDG-PET, or <sup>31</sup>P-MRS, or else abstain.</td>
</tr>
<tr>
<td><strong>Observed trajectory -&gt; thermodynamic closure</strong></td>
<td><a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">Mart&iacute;nez et al. (2019)</a> showed that waiting-time asymmetry can reveal hidden dissipation even when observable current vanishes. <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">Hartich &amp; Godec (2024)</a> showed that this can fail when coarse-graining and time reversal do not commute, and <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">Mart&iacute;nez et al. (2024)</a> limited the earlier claim to local-in-time coarse grainings and, where needed, semi-Markov constructions. <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">Blom et al. (2024)</a> showed that coarse lumping can hide dissipative cycles and induce memory. <a href="https://doi.org/10.1038/s42005-024-01742-2" target="_blank">Baiesi et al. (2024)</a> showed that sparse or unobserved reverse transitions can make direct estimation fail.</td>
<td>Low current or a small irreversibility estimate is not read as near-equilibrium unless hidden-degree risk, memory order, and reverse-transition support are disclosed explicitly.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="claim-ladder">
<h2 class="section-title">The thermodynamic claim ladder on this site</h2>
<p>
The safe way to read thermodynamic papers is not to ask whether they are <strong>important</strong> or <strong>unimportant</strong>. The better question is <strong>which rung they actually reached</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Claim rung</th>
<th>Minimum evidence required</th>
<th>What it still does not license</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Rung 1: signal-side arrow of time</strong></td>
<td>A declared observation route plus a reproducible forward-versus-reversed asymmetry or inversion-detection result.</td>
<td>Direct entropy production, direct metabolic cost, or implementation-side efficiency.</td>
</tr>
<tr>
<td><strong>Rung 2: coarse-grained nonequilibrium lower bound</strong></td>
<td>A transition-based or equivalent lower-bound estimate with explicit state-space construction, coarse-graining policy, and finite-data uncertainty.</td>
<td>Microscopic dissipation or thermodynamic closure of the full underlying process.</td>
</tr>
<tr>
<td><strong>Rung 3: model-conditioned entropy-flow estimate</strong></td>
<td>An explicit dynamical model, its assumptions, parameter-identifiability limits, and controls separating coupling-related effects from firing-rate or sampling artifacts.</td>
<td>Model-free direct EPR measurement or a unique mechanistic explanation.</td>
</tr>
<tr>
<td><strong>Rung 4: physiology-grounded energetic interpretation</strong></td>
<td>A separate physiology-side route linking the observed signal-side effect to metabolism, transport, or energetics under a declared bridge.</td>
<td>A universal thermodynamic success criterion or identity-relevant sameness.</td>
</tr>
<tr>
<td><strong>Rung 5: implementation-side cost accounting</strong></td>
<td>Separate measurement of hardware power, wall-clock energy, FLOPs, communication cost, and cooling burden for the implementation itself.</td>
<td>Equivalence to the brain's nonequilibrium statistics unless the bridge is argued and tested separately.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="estimator-families">
<h2 class="section-title">Irreversibility is not one estimator family</h2>
<p>
The same thermodynamic vocabulary still hides materially different mathematical objects.
</p>
<table class="data-table">
<thead>
<tr>
<th>Estimator family</th>
<th>Representative literature</th>
<th>What is actually computed</th>
<th>Safe ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Coarse-grained transition-flux lower bound</strong></td>
<td><a href="https://pubmed.ncbi.nlm.nih.gov/34789565/" target="_blank">Lynn et al. (2021)</a></td>
<td>Entropy-production lower bound from clustered BOLD-state transitions.</td>
<td>Broken detailed balance in a declared coarse-grained macrostate system, not direct microscopic heat dissipation.</td>
</tr>
<tr>
<td><strong>Time-shifted asymmetry / inversion family</strong></td>
<td><a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">Deco et al. (2022)</a>; <a href="https://academic.oup.com/cercor/article/33/5/1856/6577164" target="_blank">de la Fuente et al. (2023)</a></td>
<td>Forward-versus-reversed asymmetry from time-shifted correlations or inversion classification.</td>
<td>Temporal-asymmetry signature under the stated preprocessing and features, not direct EPR.</td>
</tr>
<tr>
<td><strong>Directed visibility-graph irreversibility</strong></td>
<td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11912438/" target="_blank">Nartallo-Kaluarachchi et al. (2025)</a></td>
<td>Graph divergence between in/out degree structure of directed visibility graphs built from MEG-derived dynamics.</td>
<td>Ordering of nonequilibrium organization across interaction scales, not direct causal wiring or microscopic dissipation.</td>
</tr>
<tr>
<td><strong>State-space kinetic Ising entropy flow</strong></td>
<td><a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a></td>
<td>Time-varying entropy flow in a nonstationary, sparsely active spike-ensemble model.</td>
<td>A model-conditioned entropy-flow estimate in recorded ensembles, not whole-brain direct EPR measurement.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="irreversibility-route-card">
<h2 class="section-title">Irreversibility route card</h2>
<p>
The purpose of the route card is simple: thermodynamic language alone does not tell the reader what quantity was computed, how fragile it is, or how far the interpretation may safely rise.
</p>
<table class="data-table">
<thead>
<tr>
<th>Route-card field</th>
<th>What must be disclosed</th>
<th>What misreading it blocks</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Signal route and state definition</strong></td>
<td>Modality, sensor / source / spike level, preprocessing summary, source reconstruction or parcelization if used, and task / state segmentation rule.</td>
<td>It blocks fMRI, ECoG, MEG, EEG, and spike-train results from sounding like the same observation route.</td>
</tr>
<tr>
<td><strong>Coarse-graining geometry and timescale</strong></td>
<td>Parcel count, clustering rule, retained principal components, source model, window length, temporal bin width, sampling rate, and frequency range.</td>
<td>It blocks the same paper title from sounding like the same quantity after state-space construction changes.</td>
</tr>
<tr>
<td><strong>Observed-state closure / hidden-degree risk</strong></td>
<td>Whether hidden states, hidden cycles, latent variables, or nonlocal coarse-graining could still carry dissipation that is invisible in the reported trajectory.</td>
<td>It blocks weak observable current from being misread as near-equilibrium.</td>
</tr>
<tr>
<td><strong>Dynamical assumptions and memory order</strong></td>
<td>Whether the process is treated as Markov, semi-Markov, or another memory-bearing system, and whether coarse-graining and time reversal commute under the adopted construction.</td>
<td>It blocks a Markov-style estimator from being overread when the observed process acquires memory under coarse graining.</td>
</tr>
<tr>
<td><strong>Estimator family and quantity type</strong></td>
<td>State explicitly whether the result is a lower bound, asymmetry score, graph divergence, model-based entropy-flow component, or fuller entropy-production estimate.</td>
<td>It blocks asymmetry scores or lower bounds from being misread as direct microscopic dissipation.</td>
</tr>
<tr>
<td><strong>Null / surrogate control</strong></td>
<td>State what shuffle, time reversal, label randomization, or surrogate was used and what failure it was designed to catch.</td>
<td>It blocks a clean null test from sounding like a full thermodynamic validation.</td>
</tr>
<tr>
<td><strong>Reverse-transition support / finite-data handling</strong></td>
<td>Transition-count support, whether reverse transitions were observed for the reported state pairs, and how zero or rare counts were handled.</td>
<td>It blocks a clean surrogate test from being mistaken for adequate support coverage.</td>
</tr>
<tr>
<td><strong>Physiology-side grounding</strong></td>
<td>If energetic or metabolic language is used, state whether a direct route such as calibrated CMRO<sub>2</sub>, FDG-PET, or <sup>31</sup>P-MRS was actually measured, or explicitly state that it was not.</td>
<td>It blocks signal-side irreversibility from being silently upgraded to metabolic cost or physical dissipation.</td>
</tr>
<tr>
<td><strong>Cost isolation</strong></td>
<td>Report hardware power, wall-clock energy, FLOPs, communication cost, and cooling burden separately from the neural irreversibility metric.</td>
<td>It blocks implementation-side engineering cost from being merged with observation-side nonequilibrium evidence.</td>
</tr>
<tr>
<td><strong>Abstention boundary</strong></td>
<td>Declare what the analysis does not identify, such as microscopic dissipation, direct metabolic cost, direct causal wiring, or identity-relevant sameness.</td>
<td>It blocks auxiliary analysis from being promoted to a thermodynamic gate for WBE.</td>
</tr>
</tbody>
</table>
<p>
If this card is missing, this site keeps the result at <strong>exploratory auxiliary evidence</strong>. It is not promoted here to a common thermodynamic gate, direct microscopic dissipation, direct metabolic-cost readout, or WBE-relevant identity evidence.
</p>
</section>

<section class="section" id="strengthening-conditions">
<h2 class="section-title">What would actually strengthen the claim</h2>
<table class="data-table">
<thead>
<tr>
<th>What to add</th>
<th>Why it matters</th>
<th>What it still does not prove</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Robustness across reasonable coarse-graining choices</strong></td>
<td>Shows that the sign or ordering of the result is not a one-pipeline artifact of parcelization, clustering, PCA rank, or temporal binning.</td>
<td>It still does not turn a lower bound or asymmetry score into direct physical dissipation.</td>
</tr>
<tr>
<td><strong>Explicit model-sensitivity audit</strong></td>
<td>Shows what changes when stationarity, pairwise couplings, conditional independence, source-model assumptions, or memory order are altered.</td>
<td>It still does not identify a unique neural mechanism.</td>
</tr>
<tr>
<td><strong>Observed-state closure / hidden-degree audit</strong></td>
<td>Shows whether hidden cycles, latent variables, or nonlocal coarse graining could still carry the dissipation that the observed path misses.</td>
<td>It still does not recover total microscopic entropy production by itself.</td>
</tr>
<tr>
<td><strong>Reverse-transition support / sparse-data disclosure</strong></td>
<td>Shows whether the relevant forward and reverse transitions were actually seen often enough for the chosen estimator.</td>
<td>It still does not remove hidden-variable bias by itself.</td>
</tr>
<tr>
<td><strong>Physiology-side calibration when energetic language is used</strong></td>
<td>Separates observation-side arrow-of-time analysis from actual metabolism-side measurement.</td>
<td>It still does not establish identity, consciousness, or a universal thermodynamic acceptance criterion.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">Seven questions when reading thermodynamic claims</h2>
<ol>
<li><strong>Are we looking at a lower bound, an asymmetry score, a graph index, or a model-based entropy-flow estimate?</strong></li>
<li><strong>How was the state space built?</strong> Check parcelization, clustering, PCA rank, source model, temporal bins, and frequency range.</li>
<li><strong>What hidden-state or memory risk remains?</strong> Ask whether the observed trajectory is plausibly Markov, semi-Markov, or under-closed.</li>
<li><strong>Did the paper separate null controls from support coverage?</strong> A clean shuffle does not guarantee adequate reverse-transition counts.</li>
<li><strong>If the paper says "energy" or "metabolism," where is the physiology-side route?</strong></li>
<li><strong>Are logical and physical costs still separated?</strong> Do not merge FLOPs, wall-power, and signal-side nonequilibrium into one scalar.</li>
<li><strong>What does the metric explicitly abstain from claiming?</strong> If that line is missing, the ceiling should be read conservatively.</li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>B&eacute;rut, A., Arakelyan, A., Petrosyan, A., et al. (2012). Experimental verification of Landauer&rsquo;s principle linking information and thermodynamics. <em>Nature</em>, 483, 187-189. <a href="https://doi.org/10.1038/nature10872" target="_blank">doi:10.1038/nature10872</a></li>
<li>Attwell, D., &amp; Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>, 21(10), 1133-1145. <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">doi:10.1097/00004647-200110000-00001</a></li>
<li>Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001" target="_blank">doi:10.1088/0034-4885/75/12/126001</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., Bertolero, M. A., Bassett, D. S., &amp; Daniels, K. E. (2021). Broken detailed balance and entropy production in the human brain. <em>Proceedings of the National Academy of Sciences</em>, 118(47), e2109889118. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>Mart&iacute;nez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2019). Inferring broken detailed balance in the absence of observable currents. <em>Nature Communications</em>, 10, 3542. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">doi:10.1038/s41467-019-11051-w</a></li>
<li>Hartich, D., &amp; Godec, A. (2024). Comment on “Inferring broken detailed balance in the absence of observable currents”. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">doi:10.1038/s41467-024-52602-0</a></li>
<li>Mart&iacute;nez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2024). Reply to: Comment on “Inferring broken detailed balance in the absence of observable currents”. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">doi:10.1038/s41467-024-52603-z</a></li>
<li>Deco, G., Sanz Perl, Y., Bocaccio, H., Tagliazucchi, E., &amp; Kringelbach, M. L. (2022). The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. <em>Communications Biology</em>, 5, 572. <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">doi:10.1038/s42003-022-03505-7</a></li>
<li>de la Fuente, L. A., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <em>Cerebral Cortex</em>, 33(5), 1856-1865. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <em>Proceedings of the National Academy of Sciences</em>, 122(10), e2408791122. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Blom, K., Song, K., Vouga, E., Godec, A., &amp; Makarov, D. E. (2024). Milestoning estimators of dissipation in systems observed at a coarse resolution. <em>Proceedings of the National Academy of Sciences</em>, 121(17), e2318333121. <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">doi:10.1073/pnas.2318333121</a></li>
<li>Teza, G., &amp; Stella, A. L. (2020). Exact coarse graining preserves entropy production out of equilibrium. <em>Physical Review Letters</em>, 125(11), 110601. <a href="https://doi.org/10.1103/PhysRevLett.125.110601" target="_blank">doi:10.1103/PhysRevLett.125.110601</a></li>
<li>Cocconi, L., Salbreux, G., &amp; Pruessner, G. (2022). Scaling of entropy production under coarse graining in active disordered media. <em>Physical Review E</em>, 105(4), L042601. <a href="https://doi.org/10.1103/PhysRevE.105.L042601" target="_blank">doi:10.1103/PhysRevE.105.L042601</a></li>
<li>Baiesi, M., Nishiyama, T., &amp; Falasco, G. (2024). Effective estimation of entropy production with lacking data. <em>Communications Physics</em>, 7, 264. <a href="https://doi.org/10.1038/s42005-024-01742-2" target="_blank">doi:10.1038/s42005-024-01742-2</a></li>
<li>Epp, S. M., Castrill&oacute;n, G., Yuan, B., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">Verification basics →</a></li>
<li><a href="claims-and-evidence.html">Claims and evidence →</a></li>
<li><a href="observation-to-estimation.html">From observation to estimation →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../faq.html#q1f">FAQ: thermodynamic claims →</a></li>
<li><a href="../verification.html#thermodynamic-verification">Verification: thermodynamic indicators →</a></li>
<li><a href="../perspective.html#design-principles">Perspective: design principles →</a></li>
</ul>
</div>
</aside>
</main>
