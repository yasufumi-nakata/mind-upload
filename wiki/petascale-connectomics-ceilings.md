---
layout: default
title: "Wiki: Why petascale connectomics still stops early"
description: "A primary-literature audit of why petascale, nanoscale, and same-brain connectomics remain limited by preservation kinetics, sequential bridging, proofreading scope, and dynamical underdetermination."
article_type: Wiki
subtitle: "Resolution and data volume are real advances, but they do not erase preservation, completeness, or dynamics ceilings"
author: Mind Uploading Research Project
last_updated: "2026-04-04"
note: "Technical / natural science only"
audience: "Readers who want to know why petascale connectomics is a real structural advance but still not a state-complete route to WBE"
reading_time: "12-18 min"
page_intro: "This page concentrates one technical critique that was still too scattered across the site: why petascale connectomics and same-brain structure-function pipelines remain scientifically important but still stop well before native-state-complete or dynamics-complete WBE claims."
accuracy_note: "The ceilings on this page are site-level inferences from primary literature about what is directly preserved, what is reconstructed only sequentially, what still requires selective proofreading, and what remains dynamically underdetermined even when wiring is known."
wiki_links:
  - label: "Wiki: Why A Connectome Is Not Enough"
    url: "/wiki/connectome-is-not-enough.html"
    description: "Broader page on missing state variables and connectome-constrained degeneracy."
  - label: "Wiki: State-Continuity Bridge"
    url: "/wiki/state-continuity-bridge.html"
    description: "Background rule for why same-brain or same-subject does not automatically mean same-state."
  - label: "Wiki: Observability And Claim Ceiling By Measurement Stack"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "Places volume EM and same-brain functional connectomics inside the larger stack-by-stack ceiling table."
recommended_pages:
  - label: "WBE 101"
    url: "/wbe_101.html"
  - label: "Verification"
    url: "/verification.html"
  - label: "Perspective"
    url: "/perspective.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Shortest conclusion</h2>
<p>
Petascale connectomics is a major <strong>structural-scaffold achievement</strong>. It is not yet a license to say <strong>native live state was preserved</strong>, <strong>same-brain means same-state</strong>, <strong>the reconstruction is globally complete by default</strong>, or <strong>wiring alone now fixes dynamics</strong>. The primary literature supports four separate stop rules: <strong>preservation kinetics</strong>, <strong>sequential bridge scope</strong>, <strong>proofreading / completeness burden</strong>, and <strong>dynamical underdetermination beyond wiring</strong>.
</p>
</div>

<div class="key-points">
<h4>Four walls to stop early</h4>
<ul>
<li><strong>Preservation wall:</strong> fixation is an intervention with its own time course and geometry effects.</li>
<li><strong>Sequential-bridge wall:</strong> same-brain structure-function workflows are multistage local bridges, not simultaneous whole-state capture.</li>
<li><strong>Completeness wall:</strong> petascale acquisition still coexists with section loss, merge errors, false positives, and selective proofreading.</li>
<li><strong>Dynamics wall:</strong> even a known connectome does not uniquely determine recurrent dynamics once biophysical parameters remain uncertain.</li>
</ul>
</div>

<div class="note-box">
<strong>Why this page was added</strong>
<p>
The site already warned that <strong>connectome-complete</strong> is not <strong>emulation-complete</strong>. What was still too diffuse was the narrower technical critique of current flagship connectomics. The problem was not lack of caution words, but lack of one concentrated, quantitative page showing exactly <strong>which engineering and natural-science ceilings remain after petascale imaging succeeds</strong>. This page closes that gap.
</p>
</div>

<div class="note-box">
<strong>What this page does not do</strong>
<p>
This page does not argue that connectomics is unimportant. It argues something narrower and more testable: <strong>what connectomics directly buys</strong>, <strong>what it does not yet buy</strong>, and <strong>which additional disclosures must appear before stronger WBE language is allowed</strong>.
</p>
</div>

<section class="section" id="four-walls">
<h2 class="section-title">The four current walls</h2>
<table class="data-table">
<thead>
<tr>
<th>Wall</th>
<th>What the flagship papers directly advance</th>
<th>Why the claim still stops early on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Preservation kinetics</strong></td>
<td><a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> improve whole-brain extracellular-space preservation for rodent brains, and <a href="https://doi.org/10.1038/s41598-018-36112-w" target="_blank">Huebinger et al. (2018)</a> quantify how slowly common chemical fixation can lock intracellular protein patterns.</td>
<td>Preservation route, fixative speed, and sample-thickness limits still matter. Resolution after fixation is not the same thing as native-state completeness before fixation.</td>
</tr>
<tr>
<td><strong>Sequential bridge scope</strong></td>
<td><a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a>, <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a>, and <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> show powerful cross-scale bridges from live measurements to later ultrastructure.</td>
<td>The bridge is still ordered in time, local in scope, and transformation-heavy. Same-brain linkage is not simultaneous same-state capture.</td>
</tr>
<tr>
<td><strong>Proofreading and completeness</strong></td>
<td><a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a>, <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> push acquisition, segmentation, and proofreading to unprecedented scales.</td>
<td>Petascale does not mean scrutiny-complete. Large datasets still carry section loss, merge errors, false positives, threshold choices, and open-ended correction effort.</td>
</tr>
<tr>
<td><strong>Dynamics beyond wiring</strong></td>
<td><a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">Lappalainen et al. (2024)</a> show that connectome constraints plus task optimization can predict rich activity, and <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> show when extra recordings collapse dynamical degeneracy.</td>
<td>Wiring can narrow the hypothesis space strongly without uniquely fixing the correct dynamics. Omitted mechanisms and uncertain biophysical parameters still matter.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="preservation-wall">
<h2 class="section-title">1. Preservation is an intervention, not a transparent handoff</h2>
<p>
The first technical wall is upstream of reconstruction. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> do not treat fixation as neutral storage. They show that conventional fixation causes extracellular-space loss and report that high-pressure freezing preserves extracellular space only in samples thinner than about <strong>200 μm</strong>. That is already enough to block the shortcut from <strong>nanoscale image quality</strong> to <strong>native-state completeness</strong>.
</p>
<p>
<a href="https://doi.org/10.1038/s41598-018-36112-w" target="_blank">Huebinger et al. (2018)</a> sharpen the same point from a different side. In cultured cells, they report that formaldehyde fixation of cytosolic proteins takes <strong>more than one hour</strong>, whereas glutaraldehyde-based fixation is faster than <strong>four minutes</strong>, and they explicitly conclude that even the fastest tested chemical fixations still act on the timescale of minutes rather than as instantaneous snapshots. On this site, that means a high-resolution post-fix reconstruction does <strong>not</strong> automatically certify that fast or fragile living patterns survived the transition into the reconstructed object.
</p>
<div class="note-box">
<strong>Safe reading added here</strong>
<p>
If a connectomics result does not disclose <strong>preservation route</strong>, <strong>live-to-fix timing</strong>, and <strong>thickness-limited preservation ceiling</strong>, this site keeps the claim at <strong>post-fix structural scaffold</strong>, not <strong>native-state-complete readout</strong>.
</p>
</div>
</section>

<section class="section" id="bridge-wall">
<h2 class="section-title">2. Same-brain workflows are still sequential local bridges</h2>
<p>
The second wall is the bridge itself. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">Bosch et al. (2022)</a> present exactly the kind of result that can be overread if the bridge problem is not kept visible: a correlative pipeline from in vivo two-photon physiology to synchrotron microtomography and then targeted serial block-face EM. The achievement is real, but so is the lesson. Their own description is multistage, landmark-based, and subvolume-targeted rather than one simultaneous state capture.
</p>
<p>
The two flagship large datasets reinforce the same lesson at much larger scale. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> reconstruct a rapidly preserved human cortical slab that becomes a volume of about <strong>1.05 mm<sup>3</sup></strong> after correction for sectioning compression, assembled from <strong>5,019</strong> sections at <strong>33.9 nm</strong> mean thickness and roughly <strong>1.4 petabytes</strong> of aligned EM data. But the paper is explicit that this is a <strong>local surgical specimen</strong>, and it explicitly notes the pathology-side caveat that subtle effects of epilepsy or its treatment cannot be excluded.
</p>
<p>
<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> take the bridge further by linking in vivo calcium imaging of about <strong>75,000 neurons</strong> to a later EM reconstruction with more than <strong>200,000 cells</strong> and <strong>0.5 billion synapses</strong>. But the paper also makes the sequence visible: functional imaging first, then fixation, histology, sectioning, imaging, automated reconstruction, and proofreading. The EM branch alone required <strong>26,652</strong> imaged sections, <strong>5</strong> customized autoTEMs, about <strong>6 months</strong> of acquisition, and about <strong>2 Pb</strong> of raw data. On this site, that remains a <strong>sequential same-brain local scaffold</strong>, not same-time whole-state capture.
</p>
<div class="note-box">
<strong>Why the bridge language matters</strong>
<p>
The phrase <strong>same-brain</strong> can support specimen linkage. It does not by itself support <strong>same-state</strong>. Once the route includes live measurement, later fixation, sectioning, alignment, and targeted correspondence, the argument must be read as a bridge with its own failure modes rather than as one latent-state sample.
</p>
</div>
</section>

<section class="section" id="completeness-wall">
<h2 class="section-title">3. Petascale does not mean scrutiny-complete</h2>
<p>
The third wall is reconstruction completeness. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">Shapson-Coe et al. (2024)</a> explicitly state that the dataset is <strong>large and incompletely scrutinized</strong> and provide public tools for analysis and proofreading. They also warn that path queries need <strong>manual verification</strong> because agglomeration merge errors and synapse false positives remain. That is not a criticism of the paper. It is the correct reading of what petascale automation currently looks like.
</p>
<p>
The same lesson appears in the other flagship resources. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> write that complete segmentation for datasets at this scale still requires an <strong>extensive amount of proofreading</strong>. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> estimate that the adult-fly whole-brain reconstruction required about <strong>33 person-years</strong> of manual proofreading and explicitly state that the resource remains <strong>open for future corrections</strong>. Therefore the safe reading is not <strong>petascale means complete</strong>, but <strong>petascale means a new operating range with remaining correction burden exposed rather than hidden</strong>.
</p>
<table class="data-table">
<thead>
<tr>
<th>Representative resource</th>
<th>What the paper makes visible</th>
<th>Why the site still stops the claim</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>H01 human cortex</strong></td>
<td>Large local human EM resource with public tools plus explicit warning that some paths require manual verification because of merge errors and synapse false positives.</td>
<td>Large-scale sharing is not equivalent to globally verified reconstruction.</td>
</tr>
<tr>
<td><strong>MICrONS mouse cortex</strong></td>
<td>Massive same-brain structure-function resource with selective proofreading and low but nonzero section loss in the retained region.</td>
<td>Proofread subsets and retained subvolumes are not the same thing as fully uniform completeness.</td>
</tr>
<tr>
<td><strong>FlyWire adult fly brain</strong></td>
<td>Whole-brain connectome with huge annotation and proofreading effort, still open to later correction.</td>
<td>Even mature wiring atlases remain versioned resources rather than final, error-free objects.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dynamics-wall">
<h2 class="section-title">4. Even a known connectome does not uniquely fix dynamics</h2>
<p>
The fourth wall is not about missing pixels but about missing dynamical constraints. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">Lappalainen et al. (2024)</a> show a strong positive result: connectome-constrained and task-optimized models can predict rich activity across the fly visual system. But their own analysis also shows that both <strong>task optimization</strong> and <strong>detailed connectome constraints</strong> were critical, and that models with only <strong>cell-type connectivity</strong> predicted neural activity poorly. They also state plainly that their reduced model omits electrical synapses, nonlinear chemical synapses, and neuromodulation.
</p>
<p>
<a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> then make the ceiling explicit in theory: even when two recurrent networks share the <strong>same synaptic weights</strong>, uncertainty in neuronal and synaptic biophysical parameters can leave the dynamics strongly non-unique. Small subsets of activity recordings can reduce that degeneracy, but the connectome alone often does not substantially constrain the correct dynamics. On this site, that means petascale wiring is best read as a powerful <strong>constraint on the hypothesis space</strong>, not as automatic <strong>dynamics-complete recovery</strong>.
</p>
<div class="note-box">
<strong>Safe reading added here</strong>
<p>
If a connectome paper also includes an activity model, the result is promoted here at most to a <strong>task-bounded conditional predictor</strong> unless the authors also disclose remaining fitted degrees of freedom, omitted mechanisms, validation class, and surviving equivalence families.
</p>
</div>
</section>

<section class="section" id="operating-rule">
<h2 class="section-title">Operating rule for petascale connectomics claims</h2>
<p>
When a paper is introduced on this site with words such as <strong>petascale</strong>, <strong>nanoscale</strong>, <strong>same-brain</strong>, or <strong>digital twin</strong>, four questions now come first:
</p>
<table class="data-table">
<thead>
<tr>
<th>Question</th>
<th>If the answer is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>What was the preservation route and live-to-fix ceiling?</strong></td>
<td>Keep the result at <strong>post-fix structural scaffold</strong>.</td>
</tr>
<tr>
<td><strong>What exact bridge linked live and ex vivo stages?</strong></td>
<td>Keep the result at <strong>sequential local scaffold</strong>, not same-state evidence.</td>
</tr>
<tr>
<td><strong>How much of the reconstruction was actually proofread or otherwise independently validated?</strong></td>
<td>Keep the result at <strong>versioned large-scale resource</strong>, not silently complete ground truth.</td>
</tr>
<tr>
<td><strong>Which dynamical degrees of freedom still remained fitted or uncertain?</strong></td>
<td>Keep the result at <strong>conditional predictor / narrowed hypothesis space</strong>, not unique mechanistic recovery.</td>
</tr>
</tbody>
</table>
<p>
Operationally, that means this page is intended to be read together with <a href="../verification.html#destructive-structure-card">Verification: Destructive-Structure Route Card</a>, <a href="../verification.html#state-continuity-bridge-card">Verification: State-Continuity Bridge Card</a>, and the <a href="../wiki/connectome-is-not-enough.html#conditional-predictor-route-card">conditional-model route card</a> inside <a href="../wiki/connectome-is-not-enough.html">Wiki: Why A Connectome Is Not Enough</a>.
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ul>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). <em>Prediction of neural activity in connectome-constrained recurrent networks</em>. <em>Nature Neuroscience</em>, 28, 2561-2574. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Bosch, C., Ackels, T., Pacureanu, A., et al. (2022). <em>Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy</em>. <em>Nature Communications</em>, 13, 2923. <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>Dorkenwald, S., McKellar, C. E., Macrina, T., et al. (2024). <em>Neuronal wiring diagram of an adult brain</em>. <em>Nature</em>, 634, 124-138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Huebinger, J., Spindler, J., Holl, K. J., &amp; Koos, B. (2018). <em>Quantification of protein mobility and associated reshuffling of cytoplasm during chemical fixation</em>. <em>Scientific Reports</em>, 8, 17756. <a href="https://doi.org/10.1038/s41598-018-36112-w" target="_blank">doi:10.1038/s41598-018-36112-w</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). <em>Connectome-constrained networks predict neural activity across the fly visual system</em>. <em>Nature</em>, 634, 1132-1140. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>Lu, X., Huang, X., Shen, R. L., &amp; Lichtman, J. W. (2023). <em>Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains</em>. <em>Cell Reports Methods</em>, 3, 100520. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>MICrONS Consortium, Bae, J. A., Collman, F., et al. (2025). <em>Functional connectomics spanning multiple areas of mouse visual cortex</em>. <em>Nature</em>, 640, 435-447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). <em>A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution</em>. <em>Science</em>, 384, eadk4858. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
</ul>
</section>

</article>
</main>
