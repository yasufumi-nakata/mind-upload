---
layout: default
title: 'Wiki: Basics of verification infrastructure'
description: A beginner explanation of why standards, benchmarks, preregistration, route cards, and audits are needed before strong WBE claims can be compared.
article_type: Wiki
subtitle: Before celebrating a score, fix the ruler, the route card, and the failure log.
author: Mind Uploading Research Project
last_updated: '2026-03-19'
note: Beginner guide
audience: People who want to understand the logic of the Verification Commons from the beginning
reading_time: 12-15 minutes
page_intro: This page explains from the beginning why Mind-Upload focuses on standards, benchmarks, preregistration, route cards, and audits. The goal is to show why technical progress becomes comparable only when the evidence pathway itself is disclosed.
accuracy_note: The analogies here are for orientation only. Always return to the public specification pages to see the actual operational rules.
page_highlights:
- Data alone does not become comparable progress.
- Standards, benchmarks, preregistration, route cards, and audits each solve a different failure mode.
- Modern neuroscience results often need claim-specific route cards, not only a generic score sheet.
- The stricter the claim, the more explicit the measurement path and abstention boundary must be.
known_points:
- Comparable progress requires aligned inputs, evaluation, rules, and records.
- Without preregistration and auditing, it becomes too easy to promote only favorable conditions.
- Recent primary literature shows that decode, tractography, effective-connectivity, thermodynamic, and closed-loop claims fail in different ways and therefore need different cards.
unknown_points:
- A complete WBE benchmark stack does not yet exist in finished public form.
- Which additional requirements would be sufficient for future L4 or L5 claims remains unresolved.
wiki_links:
- label: 'Wiki: How to read claims and evidence'
  url: /wiki/claims-and-evidence.html
  description: Shows why the same headline can still hide different evidence classes.
- label: 'Wiki: Basics of WBE'
  url: /wiki/mind-upload-basics.html
  description: Gives the broader technical picture before the operational details.
- label: 'Wiki: Baselines, preregistration, and model cards'
  url: /wiki/baselines-prereg-and-model-cards.html
  description: Separates the operational roles of these commonly mixed terms.
- label: 'Wiki: Measurement-stack observability and claim ceilings'
  url: /wiki/measurement-stack-and-claim-ceiling.html
  description: Shows why route-card logic is needed for different measurement classes.
recommended_pages:
- label: Verification platform
  url: /verification.html
- label: Casework
  url: /verification.html#casework
- label: Datasets and Hands-On Work
  url: /datasets.html
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Why the ruler comes first</h2>
<p>
If two groups use different inputs, different split rules, different hidden assumptions, and different failure criteria, comparing their scores does not tell you who made more progress. The Verification Commons exists so that progress claims can survive comparison rather than only presentation.
</p>
</div>

<div class="note-box">
<strong>2026-03-19 beginner update: generic audits were no longer enough</strong>
<p>
The older beginner explanation correctly said that standards and audits matter, but it still sounded as if one generic score sheet could cover every kind of neuroscience result. That is no longer safe enough. Different claim families now need different route cards because they fail for different scientific reasons.
</p>
</div>

<section class="section" id="five-parts">
<h2 class="section-title">The five parts of comparable progress</h2>
<table class="data-table">
<thead>
<tr>
<th>Part</th>
<th>Role</th>
<th>Simple analogy</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data standard</strong></td>
<td>Aligns the structure and metadata of the input.</td>
<td>The same answer sheet format.</td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Aligns the task, split rules, and evaluation family.</td>
<td>The same exam and scoring rubric.</td>
</tr>
<tr>
<td><strong>Preregistration / registry</strong></td>
<td>Locks success/failure conditions before the result is known.</td>
<td>The rules announced before the exam starts.</td>
</tr>
<tr>
<td><strong>Route card</strong></td>
<td>Discloses the evidence pathway, assumptions, omitted alternatives, and abstention boundary for a specific claim family.</td>
<td>The answer key that says which reasoning steps were allowed.</td>
</tr>
<tr>
<td><strong>Audit / model card / log</strong></td>
<td>Records weaknesses, drift, failures, recalibration, and unresolved limits.</td>
<td>The report card plus the error log.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="missing">
<h2 class="section-title">What goes wrong when one part is missing</h2>
<table class="data-table">
<thead>
<tr>
<th>What is missing</th>
<th>What goes wrong</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard</td>
<td>You cannot be sure that people are even talking about the same input.</td>
</tr>
<tr>
<td>Benchmark</td>
<td>Different groups can claim victory on different tasks and different split regimes.</td>
</tr>
<tr>
<td>Preregistration</td>
<td>It becomes too easy to keep only the convenient conditions and present them as the intended target all along.</td>
</tr>
<tr>
<td>Route card</td>
<td>A result is overread beyond the evidence class that produced it.</td>
</tr>
<tr>
<td>Audit</td>
<td>Weaknesses, drift, shortcuts, recalibration burden, and abstentions disappear behind one score.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="claim-specific-cards">
<h2 class="section-title">Why modern neuroscience needs claim-specific route cards</h2>
<table class="data-table">
<thead>
<tr>
<th>Claim family</th>
<th>Why a generic score sheet is too weak</th>
<th>Card this site now asks for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Decode / biomarker / speech</strong></td>
<td>High scores can come from subject/session fingerprint, task priors, metadata leakage, or language-model support rather than the target neural variable alone.</td>
<td>Neural Contribution Card plus Specificity &amp; Shortcut Card.</td>
</tr>
<tr>
<td><strong>Tractography / connectome</strong></td>
<td>The graph depends on acquisition, reconstruction, filtering, and external calibration; it is not one fixed object by default.</td>
<td>Tractography route card.</td>
</tr>
<tr>
<td><strong>Effective connectivity / DCM</strong></td>
<td>The output depends on candidate model space, priors, recovery, validation, and reliability.</td>
<td>Effective-connectivity route card.</td>
</tr>
<tr>
<td><strong>Thermodynamic irreversibility</strong></td>
<td>Different papers compute different quantities from different signal routes and coarse-grainings.</td>
<td>Irreversibility / thermodynamic route card.</td>
</tr>
<tr>
<td><strong>Closed loop / BCI</strong></td>
<td>Latency alone does not tell you which sensory, motor, and interoceptive loops were preserved or omitted.</td>
<td>Intervention Card plus Body / Environment Boundary Card.</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-wbe-needs-this">
<h2 class="section-title">Why this matters especially for WBE</h2>
<p>
WBE is especially vulnerable to level substitution. It is easy to describe an L1 decoding result as if it were approaching L4 continuity, or to describe one route-conditioned measurement as if it had solved a whole class of hidden states. Verification infrastructure is therefore not administrative overhead. It is part of the scientific content because it prevents the evidence class from changing silently after the result is known.
</p>

<div class="note-box">
<strong>Representative primary-literature reasons</strong>
<p>
<a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> and <a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">Di et al. (2021)</a> show why decode scores need shortcut audits. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">Thomas et al. (2014)</a> and <a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017)</a> show why tractography claims need route disclosure. <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">Penny et al. (2004)</a> and <a href="https://pubmed.ncbi.nlm.nih.gov/22561579/" target="_blank">Rosa et al. (2012)</a> show why effective-connectivity claims need candidate-model disclosure. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">Lynn et al. (2021)</a> and <a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> show why thermodynamic language hides multiple estimator families. <a href="https://pubmed.ncbi.nlm.nih.gov/31551604/" target="_blank">Musall et al. (2019)</a> and <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">Flesher et al. (2021)</a> show why closed-loop results need a boundary card rather than latency alone.
</p>
</div>
</section>

<section class="section" id="site-link">
<h2 class="section-title">How this beginner page connects to the site</h2>
<p>
On Mind-Upload, the public <a href="../verification.html">Verification</a> page is the operational blueprint. <a href="../datasets.html">Datasets and Hands-On Work</a> supplies the entry datasets and minimum implementation loop. The route-card and audit logic explained here is expanded in the public specification and in the topic-specific wiki pages.
</p>

<table class="data-table">
<thead>
<tr>
<th>If you want to understand...</th>
<th>Go here next</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>How to translate headlines into safer claim levels</td>
<td><a href="claims-and-evidence.html">How to read claims and evidence</a></td>
<td>It gives the shortest claim-reading workflow.</td>
</tr>
<tr>
<td>Why route cards differ by measurement class</td>
<td><a href="measurement-stack-and-claim-ceiling.html">Measurement-stack observability and claim ceilings</a></td>
<td>It shows what is directly observed and where each stack stops.</td>
</tr>
<tr>
<td>The full operational blueprint</td>
<td><a href="../verification.html">Verification</a></td>
<td>It defines the public rules, cards, and logs in full.</td>
</tr>
</tbody>
</table>

<div class="cta-box">
<h4>Next</h4>
<p>If you want to see how strong-looking headlines are translated into safer first readings, continue here.</p>
<a href="claims-and-evidence.html">How to read claims and evidence →</a>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">References</h2>
<ol>
<li>Chaibub Neto, E., Pratap, A., Perumal, T. M., et al. (2019). Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <em>npj Digital Medicine</em>, 2, 99. <a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Di, Y., An, X., Zhong, W., Liu, S., &amp; Ming, D. (2021). The time-robustness analysis of individual identification based on resting-state EEG. <em>Frontiers in Human Neuroscience</em>, 15, 672946. <a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>Thomas, C., Ye, F. Q., Irfanoglu, M. O., et al. (2014). Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. <em>PNAS</em>, 111(46), 16574-16579. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">doi:10.1073/pnas.1405672111</a></li>
<li>Maier-Hein, K. H., Neher, P. F., Houde, J.-C., et al. (2017). The challenge of mapping the human connectome based on diffusion tractography. <em>Nature Communications</em>, 8, 1349. <a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">doi:10.1038/s41467-017-01285-x</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <em>Journal of Neuroscience Methods</em>, 208(1), 66-78. <a href="https://pubmed.ncbi.nlm.nih.gov/22561579/" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., et al. (2021). Broken detailed balance and entropy production in the human brain. <em>PNAS</em>, 118(47), e2109889118. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <em>Nature Neuroscience</em>, 22, 1677-1686. <a href="https://pubmed.ncbi.nlm.nih.gov/31551604/" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Flesher, S. N., Downey, J. E., Weiss, J. M., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science</em>, 372(6544), 831-836. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">doi:10.1126/science.abd0380</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE basics →</a></li>
<li><a href="claims-and-evidence.html">How to read claims and evidence →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">Baselines, preregistration, and model cards →</a></li>
<li><a href="measurement-stack-and-claim-ceiling.html">Observability and claim ceilings →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Public page</h4>
<ul>
<li><a href="../verification.html">Verification →</a></li>
<li><a href="../datasets.html">Datasets and Hands-On Work →</a></li>
<li><a href="../verification.html#casework">Casework →</a></li>
</ul>
</div>
</aside>
</main>
