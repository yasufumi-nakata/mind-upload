# Wiki: Thermodynamic Grounding Basics

> Arrow-of-time evidence is informative, but it is not direct physical dissipation by default
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-04-02 / Role: Technical / natural science only

## Role Of This Page
This page explains why thermodynamic language appears on Mind-Upload, what current neural-data papers actually compute, and where the interpretation ceiling still sits.

## Accuracy Notes
This page treats thermodynamic indicators as auxiliary scientific evidence. It does not treat them as sufficient conditions for identity, consciousness, or WBE success.

## Back To Public Pages
- [Verification](https://mind-upload.com/verification.html)
- [FAQ](https://mind-upload.com/faq.html#q1f)
- [Perspective](https://mind-upload.com/perspective.html#design-principles)

## Related Wiki Pages
- [Wiki: Verification Basics](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Places thermodynamic indicators inside the wider verification stack.
- [Wiki: Claims and Evidence](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - Explains how auxiliary evidence is kept from silently becoming a stronger claim.
- [Wiki: From Observation to Estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Explains why observability and model-based inference are separate burdens.

## What Is Currently Known
- The biological brain is a continuously driven physical system rather than a static stored object.
- Current neural irreversibility papers do report informative nonequilibrium signatures, but they do not all compute the same quantity.
- State-space construction, coarse graining, and dynamical assumptions are part of the claim rather than implementation footnotes.
- Partial observation can hide dissipative cycles and induce memory, so weak observable currents do not by themselves imply near-equilibrium.
- Physiology-side grounding is a separate requirement from observation-side arrow-of-time analysis.

## What Is Still Unknown
- There is still no field-standard route from neural irreversibility metrics to a stable whole-brain entropy-production estimate.
- It remains unresolved which thermodynamic indicators, if any, will prove decision-relevant for stronger WBE claims.
- Cross-estimator convergence and physiology-side calibration for energetic interpretations remain open problems.

---

<h2>Shortest conclusion</h2>
<p>
On this site, thermodynamic language is useful only after it is typed correctly. A paper can show <strong>temporal asymmetry</strong>, a <strong>coarse-grained nonequilibrium lower bound</strong>, or a <strong>model-conditioned entropy-flow estimate</strong> without yet measuring <strong>microscopic physical dissipation</strong>, <strong>brain-wide metabolic cost</strong>, or a <strong>WBE acceptance criterion</strong>.
</p>

<h4>Three Overreads To Stop Early</h4>
<ul>
<li><strong>Arrow of time is not direct heat dissipation:</strong> observation-side irreversibility and physiology-side energetic cost are different routes.</li>
<li><strong>A clean surrogate is not enough:</strong> reverse-transition support and sparse-data handling are separate burdens.</li>
<li><strong>One thermodynamic word is not one measurement object:</strong> lower bounds, asymmetry scores, graph indices, and model-based entropy-flow estimates answer different questions.</li>
</ul>

<strong>How this page fits the site</strong>
<p>
This is the background page for the <a href="https://mind-upload.com/verification.html#thermodynamic-verification">Verification: thermodynamic indicators</a> rule and the <a href="#irreversibility-route-card">irreversibility route card</a>. The operational policy lives in Verification; this page explains why that policy is strict.
</p>

<strong>Scope</strong>
<p>
This page stays on the technology and natural-science side only. It does not use thermodynamic language to settle identity, consciousness, law, or ethics. The narrower question is: <strong>what did the paper actually compute, what assumptions were required, and what ceiling still remains?</strong>
</p>

<strong>2026-03-30 correction: the real danger is silent translation</strong>
<p>
The main weakness of the older page was not that it mentioned the wrong literature. The weakness was that it still let readers move too quickly across four translations: from <strong>signal asymmetry</strong> to <strong>nonequilibrium inference</strong>, from <strong>coarse-grained inference</strong> to <strong>energetic interpretation</strong>, from <strong>observed trajectory</strong> to <strong>thermodynamic closure</strong>, and from <strong>auxiliary physics signal</strong> to <strong>WBE relevance</strong>. The current primary literature does not support those jumps unless each one is disclosed separately.
</p>

<strong>2026-04-02 correction: estimator meaning is not the same as operational stability</strong>
<p>
The next weakness was subtler. Even after separating estimator family, hidden-degree risk, and physiology-side grounding, the page still let one more shortcut survive: it was still too easy to read a mathematically interpretable metric as if it were already <strong>operationally stable</strong> or <strong>bridge-ready</strong>. The current primary literature does not support that shortcut either. <a href="https://doi.org/10.1007/s12021-024-09652-y" target="_blank">Poudel et al. (2024)</a> showed that small motion can materially alter visibility-graph structure and that only a low-motion subset reached moderate-to-high test-retest reliability for selected graph metrics. <a href="https://doi.org/10.1002/hbm.26778" target="_blank">Metzen et al. (2024)</a> showed that variability and complexity measures in BOLD fMRI have markedly different reliability profiles, with some functional-connectivity complexity measures remaining in the unacceptable-to-moderate range. <a href="https://doi.org/10.1016/j.neuroimage.2021.117760" target="_blank">Omidvarnia et al. (2021)</a> showed reproducible multiscale-entropy structure for resting-state fMRI, but that result is specific to that estimator family and acquisition setting rather than a blanket license for all irreversibility metrics. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> then showed with simultaneous EEG-PET-MRI that temporal coupling across electrophysiology, hemodynamics, and metabolism can be strong while the spatial organization and state trajectories remain distinct rather than interchangeable. Therefore, on this site, <strong>stability / nuisance sensitivity</strong>, <strong>cross-estimator concordance</strong>, and <strong>physiology-bridge quality</strong> are now treated as separate reporting burdens rather than as footnotes under the estimator label.
</p>

<h2>Why thermodynamics appears on Mind-Upload at all</h2>
<p>
Mind-Upload does not treat WBE as a static data-storage problem alone. The brain is a continuously driven physical system whose information processing is maintained under non-equilibrium conditions. That is why thermodynamic language appears here. But the site's use is deliberately narrow: thermodynamic indicators are treated as <strong>auxiliary constraints on ongoing physical process</strong>, not as a shortcut to identity, consciousness, or final success conditions.
</p>

<h2>Five layers that must stay separate</h2>
<table>
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

<h2>Three translation gaps the site now blocks</h2>
<table>
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

<h2>The thermodynamic claim ladder on this site</h2>
<p>
The safe way to read thermodynamic papers is not to ask whether they are <strong>important</strong> or <strong>unimportant</strong>. The better question is <strong>which rung they actually reached</strong>.
</p>
<table>
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

<h2>Irreversibility is not one estimator family</h2>
<p>
The same thermodynamic vocabulary still hides materially different mathematical objects.
</p>
<table>
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

<h2>Irreversibility route card</h2>
<p>
The purpose of the route card is simple: thermodynamic language alone does not tell the reader what quantity was computed, how fragile it is, or how far the interpretation may safely rise.
</p>
<table>
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
<td><strong>Cross-estimator concordance</strong></td>
<td>State whether the qualitative conclusion survives more than one reasonable estimator family, feature construction, or state-space definition, or whether it remains explicitly estimator-specific.</td>
<td>It blocks one metric family from sounding like a universal thermodynamic structure of the brain.</td>
</tr>
<tr>
<td><strong>Null / surrogate control</strong></td>
<td>State what shuffle, time reversal, label randomization, or surrogate was used and what failure it was designed to catch.</td>
<td>It blocks a clean null test from sounding like a full thermodynamic validation.</td>
</tr>
<tr>
<td><strong>Stability / nuisance sensitivity</strong></td>
<td>Report motion sensitivity, denoising / preprocessing sensitivity, split-half or test-retest reliability, session interval, and whether the result is single-site or protocol-scoped.</td>
<td>It blocks one clean run from sounding like a stable operational signal.</td>
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
<td><strong>Physiology-bridge quality</strong></td>
<td>If a physiology-side route is invoked, state whether it was same-session, same-state-window, spatially coregistered, lag-aware, and whether agreement or disagreement across modalities was quantified explicitly.</td>
<td>It blocks “paired modalities exist” from sounding like energetic grounding has already been solved.</td>
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

<h2>What would actually strengthen the claim</h2>
<table>
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
<td><strong>Cross-estimator concordance audit</strong></td>
<td>Shows whether the sign, ordering, or state separation survives more than one reasonable estimator family instead of depending on one mathematical construction.</td>
<td>It still does not make different estimators equivalent or erase hidden-state risk.</td>
</tr>
<tr>
<td><strong>Observed-state closure / hidden-degree audit</strong></td>
<td>Shows whether hidden cycles, latent variables, or nonlocal coarse graining could still carry the dissipation that the observed path misses.</td>
<td>It still does not recover total microscopic entropy production by itself.</td>
</tr>
<tr>
<td><strong>Within-modality stability / nuisance audit</strong></td>
<td>Shows whether the effect survives motion handling, denoising choices, split-half or test-retest checks, and declared protocol changes.</td>
<td>It still does not convert an observation-side metric into a universal gate or a cross-site standard.</td>
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
<tr>
<td><strong>Same-session physiology bridge with disagreement handling</strong></td>
<td>Shows whether electrophysiology, hemodynamics, and metabolism were aligned in the same acquisition window and whether partial agreement or spatial dissociation was reported rather than hidden.</td>
<td>It still does not prove that a neural irreversibility metric is a direct energetic readout.</td>
</tr>
</tbody>
</table>

<h2>Nine questions when reading thermodynamic claims</h2>
<ol>
<li><strong>Are we looking at a lower bound, an asymmetry score, a graph index, or a model-based entropy-flow estimate?</strong></li>
<li><strong>How was the state space built?</strong> Check parcelization, clustering, PCA rank, source model, temporal bins, and frequency range.</li>
<li><strong>What hidden-state or memory risk remains?</strong> Ask whether the observed trajectory is plausibly Markov, semi-Markov, or under-closed.</li>
<li><strong>Did the paper separate null controls from support coverage?</strong> A clean shuffle does not guarantee adequate reverse-transition counts.</li>
<li><strong>Does the qualitative result survive reasonable estimator changes?</strong> If not, read it as estimator-specific rather than as a general thermodynamic fact.</li>
<li><strong>Does it survive motion, denoising, and scan-rescan checks?</strong></li>
<li><strong>If the paper says "energy" or "metabolism," where is the physiology-side route, and was it aligned in the same session / state window?</strong></li>
<li><strong>Are logical and physical costs still separated?</strong> Do not merge FLOPs, wall-power, and signal-side nonequilibrium into one scalar.</li>
<li><strong>What does the metric explicitly abstain from claiming?</strong> If that line is missing, the ceiling should be read conservatively.</li>
</ol>

<h2>References</h2>
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
<li>Poudel, G. R., Egan, G. F., &amp; McIntosh, A. R. (2024). Network representation of fMRI data using visibility graphs: The impact of motion and test-retest reliability. <em>Neuroinformatics</em>, 22, 265-284. <a href="https://doi.org/10.1007/s12021-024-09652-y" target="_blank">doi:10.1007/s12021-024-09652-y</a></li>
<li>Metzen, D., Fellner, M.-C., Labrenz, F., &amp; Waschke, L. (2024). Reliability of variability and complexity measures for task and task-free BOLD fMRI. <em>Human Brain Mapping</em>, 45(10), e26778. <a href="https://doi.org/10.1002/hbm.26778" target="_blank">doi:10.1002/hbm.26778</a></li>
<li>Omidvarnia, A., Pedersen, M., Walz, J. M., et al. (2021). Temporal complexity of fMRI is reproducible and correlates with higher order cognition. <em>NeuroImage</em>, 230, 117760. <a href="https://doi.org/10.1016/j.neuroimage.2021.117760" target="_blank">doi:10.1016/j.neuroimage.2021.117760</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>, 16, 8887. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
</ol>
