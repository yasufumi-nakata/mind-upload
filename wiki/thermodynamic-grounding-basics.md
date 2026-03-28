---
layout: default
title: "Wiki: Basics of thermodynamic grounding"
description: "We will explain from the beginning why Landauer, dissipation, NESS, and EPR appear in Mind-Upload."
article_type: Wiki
subtitle: "It's an entry point to see not only how information circulates, but also what kind of physical cost it takes to circulate information."
author: Mind Uploading Research Project
last_updated: "2026-03-28"
note: "Learning guide"
audience: "Landauer, NESS, EPR, people who are easy to stop in the sense of dissipative structure"
reading_time: "10-15 minutes"
page_intro: "This page is a wiki that explains why topics on thermodynamics come up in Mind-Upload from the perspective of Landauer, dissipation, non-equilibrium steady state (NESS), and entropy production rate (EPR). It is used as an entry point for people who stop reading on the theory page when they suddenly see the topic of physics."
accuracy_note: "What we show here is the beginning of thermodynamic grounding. It has not been determined that thermodynamic indicators are a sufficient condition for consciousness or identity, and this is treated as an unresolved problem on this site."
page_highlights:
  - "The Landauer lower bound and the energy consumption of the real brain or emulation are not the same story."
  - "Landauer lower bounds, tissue-level energy budgets, and irreversibility of neural time series are another layer of measurement."
  - "Irreversibility results are not one estimator family; coarse-grained transition lower bounds, time-shifted asymmetry scores, visibility-graph indices, and model-based spike-train entropy flow answer different questions."
  - "Coarse-graining, time binning, source reconstruction, and dynamical assumptions can materially change an irreversibility estimate, so the route card now names them explicitly."
  - "Passing null / surrogate controls is not the same as having enough reverse-transition support; nuisance rejection and estimator support-coverage are now audited separately."
  - "Partial observation can hide dissipative cycles and generate non-Markov memory, so a low or zero observable current is not enough to infer near-equilibrium."
  - "NESS and EPR are words used to describe a system that continues to move."
  - "The thermodynamics story is an auxiliary line that strengthens the hypothesis, not a magical indicator that alone can lead to a conclusion."
known_points:
  - "The biological brain is a system that has a continuous flow of energy, not static data."
  - "Logical calculation costs and physical dissipation costs must be considered separately."
  - "There are ideas for incorporating thermodynamic indicators into the validation process, but measurement and interpretation remain difficult."
  - "Thermodynamic route cards are needed because signal route, coarse-graining, estimator family, dynamical assumptions, and quantity type change what a result can mean."
  - "A clean null or shuffle control does not by itself show that entropy production was estimable; sparse or unobserved reverse transitions remain a separate support-coverage problem."
  - "Partial observation can hide dissipative cycles and introduce memory, so a weak estimate is not automatically evidence that dissipation is absent."
unknown_points:
  - "It is unclear which thermodynamic indicators affect which aspects of consciousness and identity."
  - "The extent to which EPR and dissipation proxy indicators can be stably estimated from neural data remains an open question."
  - "Cross-estimator convergence and physiology-side calibration for energetic interpretations are still unresolved."
wiki_links:
  - label: "Wiki: Theory of Consciousness Map"
    url: "/wiki/consciousness-theory-map.html"
    description: "Go back to the theory of role differences."
  - label: "Wiki: Basics of verification infrastructure"
    url: "/wiki/verification-basics.html"
    description: "Complements the positioning of thermodynamic indicators in evaluation."
  - label: "Wiki Home"
    url: "/wiki/"
    description: "You can return to other auxiliary pages."
recommended_pages:
  - label: "Theoretical Frame"
    url: "/perspective.html#design-principles"
  - label: "Research Notes"
    url: "/perspective.html"
  - label: "Verification base"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>The shortest answer</h2>
<p>
The reason we talk about thermodynamics in Mind-Upload is because we want to see not only whether the information is similar, but also the physical cost of maintaining that information processing. If we are concerned with moving processes rather than stationary data storage, it becomes difficult to ignore dissipation and non-equilibrium.
</p>
</div>

<section class="section" id="why-thermodynamics">
<h2 class="section-title">Why thermodynamics comes into play here</h2>
<p>
This site treats WBE as a ``continuing process of inheritance'' rather than a ``static copy.'' In this case, the issue becomes not only ``what was calculated,'' but also ``the physical flow in which the calculation is maintained.''
</p>
<div class="note-box">
<strong>Safe reading</strong>
<p>
This does not mean that if you understand thermodynamics, you can understand consciousness. Rather, it is treated as an unresolved problem that ``there may be physical constraints that are overlooked by information indicators alone.''
</p>
</div>
</section>

<section class="section" id="terms">
<h2 class="section-title">First, separate the four words</h2>
<table class="data-table">
<thead>
<tr>
<th>Term</th>
<th>Rough meaning</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Landauer lower bound</strong></td>
<td>This is the minimum cost required for logically irreversible calculations, such as erasing information. </td>
<td>Actual brains and computers do not operate exactly at that lower limit. </td>
</tr>
<tr>
<td><strong>dissipation</strong></td>
<td>Irreversible loss of energy. </td>
<td>Logical cost and physical dissipation cost are looked at separately. </td>
</tr>
<tr>
<td><strong>NESS</strong></td>
<td>None-equilibrium steady state. A system that maintains a constant state while receiving energy from the outside. </td>
<td>This often comes up when considering systems that keep moving, such as the brain. </td>
</tr>
<tr>
<td><strong>EPR</strong></td>
<td>Entropy generation rate. This is an indicator of how irreversible the flow is. </td>
<td>It is difficult to directly measure it, and there are many discussions about proxy indicators and lower bound estimation. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="measurement-layers">
<h2 class="section-title">Do not mix 4 more measurement layers</h2>
<table class="data-table">
<thead>
<tr>
<th>Measurement layer</th>
<th>Representative literature</th>
<th>What you'll learn here</th>
<th>What I can't say from here yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Landauer lower bound</strong></td>
<td>B&eacute;rut et al. (2012)</td>
<td>There is a minimum dissipation lower bound for logically irreversible operations like bit erasure. </td>
<td>It directly determines the success or failure of wall-power, NESS, and WBE of the entire digital brain. </td>
</tr>
<tr>
<td><strong>Organizational-level energy budget</strong></td>
<td>Attwell &amp; Laughlin (2001)</td>
<td>This is a descriptive budget on the biological tissue side, which determines how to decompose the signaling cost in rodent gray matter. </td>
<td>The idea is to use that ratio as it is as the acceptance KPI for digital emulation. </td>
</tr>
<tr>
<td><strong>Irreversibility of coarse-grained neural dynamics</strong></td>
<td>Lynn et al. (2021), de la Fuente et al. (2023), Nartallo-Kaluarachchi et al. (2025)</td>
<td>Time series such as fMRI / ECoG / MEG have state-dependent broken detailed balance and time asymmetry. </td>
<td>This means that we were able to directly measure microscopic physical dissipation and individuality. </td>
</tr>
<tr>
<td><strong>model-based entropy flow</strong></td>
<td>Ishihara &amp; Shimazaki (2025)</td>
<td>It is possible to estimate the task-dependent entropy flow of a spiking population under the state-space kinetic ising model. </td>
<td>This means that we were able to directly and stably measure EPR in the whole brain without making any model assumptions. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="main-weakness">
<h2 class="section-title">Main weakness this pass had to fix</h2>
<p>
The earlier version already separated Landauer, tissue-level energy budgets, and irreversibility metrics. That part was correct. The weak point was elsewhere: it still let the reader learn the <strong>estimator label</strong> while skipping <strong>how the state space itself was constructed</strong> and <strong>what assumptions were needed to connect the result to physiology</strong>. The current primary literature does not support that shortcut.
</p>
<p>
<a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> estimated entropy production only after coarse-graining 100-parcel BOLD dynamics into clustered macrostates, proved that the estimate rises as the clustering becomes finer, and reported robustness only across a bounded range of coarse-graining choices. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a> then showed that reversibility detection in ECoG depends on the number of retained principal components, whether frequency or phase features are used, and the complexity of the classifier. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> introduced a nonstationary state-space kinetic Ising model because neuronal activity violates steady-state assumptions, but they also state that pairwise couplings and conditional independence limit interpretability and that fitted couplings are statistical summaries rather than direct synaptic mechanisms. Meanwhile, stochastic-thermodynamics work such as <a href="https://doi.org/10.1103/PhysRevLett.125.110601" target="_blank">Teza &amp; Stella (2020)</a> and <a href="https://doi.org/10.1103/PhysRevE.105.L042601" target="_blank">Cocconi et al. (2022)</a> shows that entropy production can be preserved or rescaled under coarse graining depending on the process class and scale of description. Therefore, on this site, the route card now has to expose <strong>coarse-graining geometry, timescale, and dynamical assumptions</strong>, not only the family name of the estimator.
</p>
<p>
A second shortcut also had to be blocked. If an article uses irreversibility language and then casually switches to <strong>energy cost</strong> or <strong>metabolic demand</strong>, the burden of proof changes. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that about 40% of voxels with significant task-evoked BOLD changes displayed oxygen-metabolism changes in the opposite direction. Observation-side time asymmetry therefore cannot be upgraded to metabolic dissipation unless a physiology-side route such as calibrated CMRO<sub>2</sub>, FDG-PET, or <sup>31</sup>P-MRS is disclosed separately.
</p>
<p>
A third weakness remained even after that fix: the page still let the reader treat the observed trajectory as if it were thermodynamically sufficient by default. The current thermodynamics literature does not support that shortcut. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">Martínez et al. (2019)</a> showed that waiting-time asymmetry can reveal hidden dissipation even when observable current vanishes. <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">Hartich &amp; Godec (2024)</a> then showed that this reading can fail when coarse-graining and time reversal do not commute, and <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">Martínez et al. (2024)</a> replied by limiting the original claim to coarse-grainings that are local in time and, where needed, second-order semi-Markov constructions. <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">Blom et al. (2024)</a> further showed that lumped observations can hide dissipative cycles, acquire memory, and strongly underestimate entropy production when the coarse trajectory is naively treated as Markov. Therefore, on this site, the route card now has to expose <strong>observed-state closure, hidden-degree risk, and memory order</strong>, not only coarse-graining geometry and estimator family.
</p>
<p>
A fourth weakness remained after adding closure and estimator-family audits. The page still let readers treat <strong>surrogate success</strong> and <strong>estimator support coverage</strong> as if they were one checkmark. The current primary literature does not support that shortcut either. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> already displayed finite-data confidence intervals around flux estimates, <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> used trial-shuffled controls to separate coupling-related entropy flow from firing-rate dynamics and sampling error, and <a href="https://doi.org/10.1038/s42005-024-01742-2" target="_blank">Baiesi et al. (2024)</a> showed that when backward transitions are rare or unobserved, direct entropy-production estimation can fail and lower-bound strategies become preferable. Therefore, on this site, <strong>null / surrogate control</strong> and <strong>reverse-transition support / finite-data support</strong> now have to be logged as separate route-card fields rather than one merged note.
</p>
</section>

<section class="section" id="estimator-families">
<h2 class="section-title">"Irreversibility" is not one estimator family</h2>
<p>
One remaining weak point in thermodynamic discussions is that papers using similar words often compute different quantities. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> estimated entropy-production lower bounds from coarse-grained BOLD state transitions, <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">Deco et al. (2022)</a> and <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a> measured time asymmetry from forward / reversed ECoG through time-shifted correlations or inversion decoding, <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">Nartallo-Kaluarachchi et al. (2025)</a> measured multilevel irreversibility from directed visibility-graph degree distributions on MEG, and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> estimated time-varying entropy flow from spike trains under a state-space kinetic Ising model. Therefore, on this site, the phrase <strong>irreversibility result</strong> is not read as one common measurement object.
</p>
<table class="data-table">
<thead>
<tr>
<th>Estimator family</th>
<th>Representative paper</th>
<th>What is computed</th>
<th>Safe ceiling on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Coarse-grained state-transition lower bound</strong></td>
<td>Lynn et al. (2021)</td>
<td>Entropy-production lower bound from clustered BOLD state transitions.</td>
<td>State-dependent broken detailed balance in coarse-grained macrostates, not direct heat dissipation.</td>
</tr>
<tr>
<td><strong>Time-shifted correlation / inversion family</strong></td>
<td>Deco et al. (2022), de la Fuente et al. (2023)</td>
<td>Distance between forward / reversed time-shifted correlation matrices or inversion-classification accuracy on ECoG.</td>
<td>Temporal-asymmetry signature under the stated preprocessing and state comparison, not direct EPR.</td>
</tr>
<tr>
<td><strong>Multilevel visibility-graph irreversibility</strong></td>
<td>Nartallo-Kaluarachchi et al. (2025)</td>
<td>Jensen-Shannon divergence between in/out degree distributions of directed multiplex visibility graphs built from source-reconstructed MEG.</td>
<td>Ordering of interaction-level nonequilibrium across tuples, not direct causal wiring or microscopic dissipation.</td>
</tr>
<tr>
<td><strong>State-space kinetic Ising entropy flow</strong></td>
<td>Ishihara &amp; Shimazaki (2025)</td>
<td>Model-based time-varying entropy flow from binarized spike ensembles under nonstationary kinetic-Ising assumptions.</td>
<td>Coupling-conditioned entropy-flow estimate in recorded ensembles, not whole-brain direct EPR measurement.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-is-not-being-claimed">
<h2 class="section-title">What I'm not saying here</h2>
<table class="data-table">
<thead>
<tr>
<th>Expressions that are easy to overstate</th>
<th>Safer reading</th>
</tr>
</thead>
<tbody>
<tr>
<td>"Consciousness is preserved if Landauer is satisfied"</td>
<td>Landauer is talking about a lower bound, not a sufficient condition for identity or consciousness. </td>
</tr>
<tr>
<td>"If the EPR is the same, it's the same person"</td>
<td>EPR is one of the candidate indicators and does not alone determine L4. </td>
</tr>
<tr>
<td>"The brain uses 20W, so the same power is enough"</td>
<td>Not only the total power consumption, but also the ratio of communication and calculation and how it is dissipated are other issues. </td>
</tr>
<tr>
<td>"It's enough if the signaling budget ratio is the same"</td>
<td>The tissue energy budget paper is a descriptive budget of biological tissue, not a pass/fail gate for WBE. </td>
</tr>
<tr>
<td>"This paper measured EPR directly from brain activity"</td>
<td>Often the paper measured a lower bound, asymmetry score, graph index, or model-conditioned entropy-flow estimate rather than direct microscopic dissipation. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-logical-vs-physical">
<h2 class="section-title">Separate logical and physical costs</h2>
<p>
Logical computational complexity, such as FLOPs, is an indicator of how much computation was performed. On the other hand, thermodynamic dissipation looks at the physical cost of performing the calculation. One or the other alone cannot fully express the difficulty of a constantly moving implementation.
</p>
</section>

<section class="section" id="what-can-be-said-now">
<h2 class="section-title">What can be said relatively strongly now / What is still weak</h2>
<table class="data-table">
<thead>
<tr>
<th>Something that can be said relatively strongly</th>
<th>Still weak</th>
</tr>
</thead>
<tbody>
<tr>
<td>If information processing and physical costs are recorded separately, implementation comparisons will be less likely to be misinterpreted. </td>
<td>It is unclear which thermodynamic index is directly linked to the quality of consciousness and identity. </td>
</tr>
<tr>
<td>When considering dynamic systems such as the brain, it is safer not to ignore non-equilibrium and dissipation. </td>
<td>A standard method for estimating EPR and NESS from neural data has not yet been established. </td>
</tr>
<tr>
<td>It is useful to look at the ratio of communication to computation, not just the total power. </td>
<td>The extent to which this ratio affects the conditions for WBE is still unresolved. </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="measurement-boundary">
<h2 class="section-title">How much can we tell from observations</h2>
<table class="data-table">
<thead>
<tr>
<th>Observation/Estimation</th>
<th>I can say this so far</th>
<th>It's still too much to say</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>time irreversibility of fMRI / EEG / ECoG</strong></td>
<td>We can show that there may be state-dependent time asymmetry in brain dynamics. </td>
<td>It cannot be said that microscopic physical dissipation or "sameness" can be directly measured. </td>
</tr>
<tr>
<td><strong>Lower bound estimation of entropy production</strong></td>
<td>Non-equilibrium informational signals can be extracted from coarse-grained time series. </td>
<td>There is no one-to-one correspondence with hardware power or metabolic costs. </td>
</tr>
<tr>
<td><strong>Entropy flow estimation with spiking model</strong></td>
<td>Progress is being made in the design of nonequilibrium indicators for non-stationary firing sequences. </td>
<td>At this point, it is too early to generalize that ``EPR can be stably and directly measured from neural firing.'' </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="irreversibility-route-card">
<h2 class="section-title">Irreversibility route card</h2>
<p>
The reason this site now asks for a route card is simple: thermodynamic language alone does not tell you what quantity was computed or how fragile it is. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> checked that fluxes vanish after temporal shuffling and reported finite-data confidence intervals, <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> used trial-shuffled data to isolate coupling-related contributions from firing-rate dynamics and sampling error, and <a href="https://doi.org/10.1038/s42005-024-01742-2" target="_blank">Baiesi et al. (2024)</a> showed that rare or unobserved reverse transitions materially affect entropy-production estimation in data-poor regimes. Therefore, a modality label alone is not enough, and a clean surrogate does not by itself guarantee that reverse-transition support was adequate.
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
<td>Write modality, sensor / source / spike level, source reconstruction or parcelization if used, preprocessing summary, and the task / state contrast or segmentation window.</td>
<td>It blocks BOLD, ECoG, MEG, and spike-train results from sounding as if they were the same observation route.</td>
</tr>
<tr>
<td><strong>Coarse-graining geometry and timescale</strong></td>
<td>Write parcel count, clustering rule and k if used, retained principal components, source model, temporal bin width, window length, sampling rate, and frequency range.</td>
<td>It blocks the same paper title from sounding like the same quantity after state-space construction or temporal resolution has changed.</td>
</tr>
<tr>
<td><strong>Observed-state closure / hidden-degree risk</strong></td>
<td>State whether the observed process is treated as Markov, 1st/2nd-order semi-Markov, or another memory-bearing process, whether coarse-graining and time reversal commute under the adopted construction, which hidden states or cycles were collapsed, and whether waiting-time or memory diagnostics were checked.</td>
<td>It blocks zero current or a small irreversibility score from being misread as near-equilibrium when dissipation may simply be hidden in unobserved degrees of freedom or in neglected memory.</td>
</tr>
<tr>
<td><strong>Estimator family and dynamical assumptions</strong></td>
<td>Name whether the result comes from transition-flux lower bounds, time-shifted correlations, inversion classifiers, visibility graphs, state-space kinetic Ising models, or another explicit family, and state whether steady-state, Markov, pairwise, conditional-independence, or source-model assumptions are imposed.</td>
<td>It blocks all irreversibility papers from being collapsed into one common "EPR measurement," and blocks model-conditioned summaries from sounding like model-free physiology.</td>
</tr>
<tr>
<td><strong>Null / surrogate control</strong></td>
<td>Write time-reversal baseline, temporal shuffle, label shuffle, trial shuffle, and motion or nuisance controls used to test whether the apparent effect survives artifact-sensitive or rate-only alternatives.</td>
<td>It blocks pipeline artifacts, nuisance structure, and firing-rate-only changes from being silently rephrased as nonequilibrium structure.</td>
</tr>
<tr>
<td><strong>Reverse-transition support / finite-data support</strong></td>
<td>Write transition-count support, whether reverse transitions were observed for the reported state pairs, how zero or rare reverse counts were handled, and the noise-floor, bootstrap, Bayesian prior, or lower-bound strategy used in sparse-data regimes.</td>
<td>It blocks a clean surrogate test from being misread as proof that entropy production was estimable when the relevant reverse transitions were too sparse or absent.</td>
</tr>
<tr>
<td><strong>Quantity type</strong></td>
<td>State explicitly whether the reported number is an entropy-production lower bound, asymmetry score, graph divergence, entropy-flow component, or a fuller entropy-production estimate.</td>
<td>It blocks asymmetry scores or lower bounds from being misread as direct microscopic dissipation.</td>
</tr>
<tr>
<td><strong>Physiology-side grounding</strong></td>
<td>If the text interprets the result as energetic or metabolic, state whether there is a direct physiology-side route such as calibrated CMRO<sub>2</sub>, FDG-PET, or <sup>31</sup>P-MRS, or explicitly mark that no such route is present.</td>
<td>It blocks brain-signal irreversibility from being silently upgraded to metabolic cost or physical dissipation.</td>
</tr>
<tr>
<td><strong>Cost isolation</strong></td>
<td>Report hardware power, wall-clock energy, FLOPs, and communication cost separately from the brain-signal irreversibility metric.</td>
<td>It blocks observation-side nonequilibrium from being merged with implementation-side power accounting.</td>
</tr>
<tr>
<td><strong>Abstention boundary</strong></td>
<td>Declare what the analysis does not identify, such as microscopic dissipation, direct metabolic cost, direct causal wiring, or identity-relevant sameness.</td>
<td>It blocks exploratory auxiliary analysis from being promoted to a thermodynamic gate for WBE.</td>
</tr>
</tbody>
</table>
<p>
If this card is missing, this site keeps the result at <strong>exploratory auxiliary log</strong>. It is not promoted here to a common thermodynamic gate, direct microscopic dissipation, direct metabolic-cost readout, or WBE-relevant identity evidence.
</p>
</section>

<section class="section" id="strengthening-conditions">
<h2 class="section-title">What would actually strengthen the claim</h2>
<p>
On this site, strengthening a thermodynamic interpretation does <strong>not</strong> mean promoting it to a WBE gate. It means making the auxiliary result harder to misread inside its own modality.
</p>
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
<td>Shows what changes when stationarity, pairwise couplings, conditional independence, or source-model assumptions are relaxed, rather than hiding those assumptions inside one fitted summary.</td>
<td>It still does not identify the unique neural mechanism or synaptic circuit.</td>
</tr>
<tr>
<td><strong>Observed-state closure / memory-order audit</strong></td>
<td>Shows whether zero current or a small estimate could be an artifact of hidden cycles, hidden variables, or a too-low Markov order rather than evidence that dissipation is genuinely weak.</td>
<td>It still does not recover the total microscopic entropy production by itself.</td>
</tr>
<tr>
<td><strong>Reverse-transition support / finite-data disclosure</strong></td>
<td>Shows whether the key forward and reverse transitions were actually observed often enough, whether zero-count handling or lower-bound substitution was needed, and whether the claimed irreversibility survives a realistic support-coverage audit.</td>
<td>It still does not solve hidden-variable bias by itself.</td>
</tr>
<tr>
<td><strong>Physiology-side calibration when energetic language is used</strong></td>
<td>Separates observation-side arrow-of-time from direct energy-side measurements by naming the metabolic route or abstaining clearly.</td>
<td>It still does not establish identity, consciousness, or a universal thermodynamic acceptance criterion.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rule-2026-03">
<h2 class="section-title">Operation rules fixed in 2026-03 audit</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>Separate Landauer and implemented power:</strong>Do not confuse lower bound theory and measured power. </li>
<li><strong>Separate the organization's budget and acceptance gate:</strong>20W and signaling partition are background values and should not be made into site-wide KPIs. </li>
<li><strong>Distinguish information entropy production and physical dissipation:</strong>Do not write the lower bound estimation from coarse-grained neural data as physical dissipation itself. </li>
<li><strong>Name coarse-graining and timescale explicitly:</strong>Parcelization, clustering, PCA rank, source model, window length, and temporal binning are part of the claim, not implementation footnotes. </li>
<li><strong>Do not assume the observed trajectory is thermodynamically closed:</strong>Write hidden-degree risk, local-in-time coarse-graining assumption, and effective memory order explicitly when waiting-time or semi-Markov arguments are used. </li>
<li><strong>Separate null controls from reverse-transition support:</strong>Shuffle or surrogate success and adequate forward/reverse transition support are different checks; both must be disclosed. </li>
<li><strong>Name estimator family, dynamical assumptions, and finite-data treatment:</strong>Transition-based lower bounds, time-shifted correlations, inversion classifiers, visibility graphs, and state-space Ising models are not interchangeable, and steady-state / pairwise / rare-transition assumptions are part of the claim. </li>
<li><strong>Do not infer metabolism without a physiology-side route:</strong>If the text uses energetic or metabolic language, disclose calibrated CMRO<sub>2</sub>, FDG-PET, <sup>31</sup>P-MRS, or abstain. </li>
<li><strong>Thermodynamic indicators are not used in place of auxiliary logs:</strong>OOD generalization, perturbation, validation, uncertainty, and abstention conditions. </li>
<li><strong>Clarify modality dependence:</strong> Do not interchange fMRI, ECoG, EEG, and spiking with the same meaning. </li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">7 questions when reading thermodynamic claims</h2>
<ol>
<li><strong>Are we talking about lower bounds or actual measurements?</strong>It is important not to confuse theoretical lower bounds such as Landauer's with actual consumption or dissipation. </li>
<li><strong>How was the state space built, and what hidden-state / memory risk remains?</strong>Check parcelization, clustering, PCA rank, source reconstruction, window length, temporal binning, whether the observed process is treated as Markov or semi-Markov, and whether hidden cycles or nonlocal coarse-graining could still carry the dissipation. </li>
<li><strong>Which estimator family, dynamical assumptions, and null control were used?</strong>Check whether this is a transition-flux lower bound, time-shifted asymmetry score, visibility-graph index, or model-based spike-train estimate, together with steady-state / pairwise assumptions and shuffle / surrogate tests. </li>
<li><strong>Were the relevant reverse transitions actually supported by the data?</strong>Check whether reverse transitions were observed often enough, whether zero-count handling or lower-bound substitution was needed, and whether the reported result survives a finite-data audit rather than only a surrogate test. </li>
<li><strong>If the paper says "energy" or "metabolism," where is the physiology-side route?</strong>Check whether CMRO<sub>2</sub>, FDG-PET, <sup>31</sup>P-MRS, or another direct route was actually measured, rather than inferred from the irreversibility metric alone. </li>
<li><strong>Are you separating logical and physical costs?</strong>Are you combining FLOPs and dissipation into one number? </li>
<li><strong>What do you mean by this metric alone?</strong>Check whether EPR or NESS is being used alone to prove identity or consciousness. </li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">Where to go back next</h2>
<p>
To return to the theory frame, please use <a href="../perspective.html#design-principles">Theoretical frame</a>. To return to the long research note, please use <a href="../perspective.html">Research note</a>. To return to the verification requirements, please use <a href="../verification.html">Verification platform</a>.
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>B&eacute;rut, A., Arakelyan, A., Petrosyan, A., et al. (2012). Experimental verification of Landauer&rsquo;s principle linking information and thermodynamics. <em>Nature</em>, 483, 187-189. <a href="https://doi.org/10.1038/nature10872" target="_blank">doi:10.1038/nature10872</a></li>
<li>Attwell, D., &amp; Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>, 21(10), 1133-1145. <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">doi:10.1097/00004647-200110000-00001</a></li>
<li>Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001" target="_blank">doi:10.1088/0034-4885/75/12/126001</a></li>
<li>Lynn, C. W., et al. (2021). Broken detailed balance and entropy production in the human brain. <em>PNAS</em>, 118(47), e2109889118. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>Martínez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2019). Inferring broken detailed balance in the absence of observable currents. <em>Nature Communications</em>, 10, 3542. <a href="https://doi.org/10.1038/s41467-019-11051-w" target="_blank">doi:10.1038/s41467-019-11051-w</a></li>
<li>Hartich, D., &amp; Godec, A. (2024). Comment on “Inferring broken detailed balance in the absence of observable currents”. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-024-52602-0" target="_blank">doi:10.1038/s41467-024-52602-0</a></li>
<li>Martínez, I. A., Bisker, G., Horowitz, J. M., &amp; Parrondo, J. M. R. (2024). Reply to: Comment on “Inferring broken detailed balance in the absence of observable currents”. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-024-52603-z" target="_blank">doi:10.1038/s41467-024-52603-z</a></li>
<li>Deco, G., Sanz Perl, Y., Bocaccio, H., Tagliazucchi, E., &amp; Kringelbach, M. L. (2022). The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. <em>Communications Biology</em>, 5, 572. <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">doi:10.1038/s42003-022-03505-7</a></li>
<li>de la Fuente, L. A., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <em>Cerebral Cortex</em>, 33(5), 1856–1865. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <em>PNAS</em>, 122(10), e2408791122. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Blom, K., Song, K., Vouga, E., Godec, A., &amp; Makarov, D. E. (2024). Milestoning estimators of dissipation in systems observed at a coarse resolution. <em>PNAS</em>, 121(17), e2318333121. <a href="https://doi.org/10.1073/pnas.2318333121" target="_blank">doi:10.1073/pnas.2318333121</a></li>
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
<li><a href="consciousness-theory-map.html">Consciousness theory map →</a></li>
<li><a href="verification-basics.html">Basics of verification infrastructure →</a></li>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../perspective.html#design-principles">Theoretical frame →</a></li>
<li><a href="../perspective.html">Research notes →</a></li>
<li><a href="../verification.html">Verification infrastructure →</a></li>
</ul>
</div>
</aside>
</main>
