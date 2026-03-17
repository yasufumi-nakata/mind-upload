---
layout: default
title: "Wiki: Basics of thermodynamic grounding"
description: "We will explain from the beginning why Landauer, dissipation, NESS, and EPR appear in Mind-Upload."
article_type: Wiki
subtitle: "It's an entry point to see not only how information circulates, but also what kind of physical cost it takes to circulate information."
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Learning guide"
audience: "Landauer, NESS, EPR, people who are easy to stop in the sense of dissipative structure"
reading_time: "10-15 minutes"
page_intro: "This page is a wiki that explains why topics on thermodynamics come up in Mind-Upload from the perspective of Landauer, dissipation, non-equilibrium steady state (NESS), and entropy production rate (EPR). It is used as an entry point for people who stop reading on the theory page when they suddenly see the topic of physics."
accuracy_note: "What we show here is the beginning of thermodynamic grounding. It has not been determined that thermodynamic indicators are a sufficient condition for consciousness or identity, and this is treated as an unresolved problem on this site."
page_highlights:
  - "The Landauer lower bound and the energy consumption of the real brain or emulation are not the same story."
  - "Landauer lower bounds, tissue-level energy budgets, and irreversibility of neural time series are another layer of measurement."
  - "NESS and EPR are words used to describe a system that continues to move."
  - "The thermodynamics story is an auxiliary line that strengthens the hypothesis, not a magical indicator that alone can lead to a conclusion."
known_points:
  - "The biological brain is a system that has a continuous flow of energy, not static data."
  - "Logical calculation costs and physical dissipation costs must be considered separately."
  - "There are ideas for incorporating thermodynamic indicators into the validation process, but measurement and interpretation remain difficult."
unknown_points:
  - "It is unclear which thermodynamic indicators affect which aspects of consciousness and identity."
  - "The extent to which EPR and dissipation proxy indicators can be stably estimated from neural data remains an open question."
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

<section class="section" id="site-rule-2026-03">
<h2 class="section-title">Operation rules fixed in 2026-03 audit</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>Separate Landauer and implemented power:</strong>Do not confuse lower bound theory and measured power. </li>
<li><strong>Separate the organization's budget and acceptance gate:</strong>20W and signaling partition are background values and should not be made into site-wide KPIs. </li>
<li><strong>Distinguish information entropy production and physical dissipation:</strong>Do not write the lower bound estimation from coarse-grained neural data as physical dissipation itself. </li>
<li><strong>Thermodynamic indicators are not used in place of auxiliary logs:</strong>OOD generalization, perturbation, validation, uncertainty, and abstention conditions. </li>
<li><strong>Clarify modality dependence:</strong> Do not interchange fMRI, ECoG, EEG, and spiking with the same meaning. </li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">3 questions when reading thermodynamic claims</h2>
<ol>
<li><strong>Are we talking about lower bounds or actual measurements?</strong>It is important not to confuse theoretical lower bounds such as Landauer's with actual consumption or dissipation. </li>
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
<li>de la Fuente, L. A., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <em>Cerebral Cortex</em>, 33(5), 1856–1865. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <em>PNAS</em>, 122(10), e2408791122. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
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
