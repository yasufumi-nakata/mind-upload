# Wiki: Basics of thermodynamic grounding

> It's an entry point to see not only how information circulates, but also what kind of physical cost it takes to circulate information.
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-19 / 位置づけ: Learning guide

## このページの役割
This page is a wiki that explains why topics on thermodynamics come up in Mind-Upload from the perspective of Landauer, dissipation, non-equilibrium steady state (NESS), and entropy production rate (EPR). It is used as an entry point for people who stop reading on the theory page when they suddenly see the topic of physics.

## 正確さの前提
What we show here is the beginning of thermodynamic grounding. It has not been determined that thermodynamic indicators are a sufficient condition for consciousness or identity, and this is treated as an unresolved problem on this site.

## 公開ページへ戻る
- [Theoretical Frame](https://mind-upload.com/perspective.html#design-principles)
- [Research Notes](https://mind-upload.com/perspective.html)
- [Verification base](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: Theory of Consciousness Map](https://github.com/yasufumi-nakata/mind-upload/wiki/consciousness-theory-map) - Go back to the theory of role differences.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Complements the positioning of thermodynamic indicators in evaluation.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other auxiliary pages.

## いま分かっていること
- The biological brain is a system that has a continuous flow of energy, not static data.
- Logical calculation costs and physical dissipation costs must be considered separately.
- There are ideas for incorporating thermodynamic indicators into the validation process, but measurement and interpretation remain difficult.
- Thermodynamic route cards are needed because signal route, estimator family, and quantity type change what a result can mean.

## まだ分かっていないこと
- It is unclear which thermodynamic indicators affect which aspects of consciousness and identity.
- The extent to which EPR and dissipation proxy indicators can be stably estimated from neural data remains an open question.

---

<h2>The shortest answer</h2>
<p>
The reason we talk about thermodynamics in Mind-Upload is because we want to see not only whether the information is similar, but also the physical cost of maintaining that information processing. If we are concerned with moving processes rather than stationary data storage, it becomes difficult to ignore dissipation and non-equilibrium.
</p>

<h2>Why thermodynamics comes into play here</h2>
<p>
This site treats WBE as a ``continuing process of inheritance'' rather than a ``static copy.'' In this case, the issue becomes not only ``what was calculated,'' but also ``the physical flow in which the calculation is maintained.''
</p>

<strong>Safe reading</strong>
<p>
This does not mean that if you understand thermodynamics, you can understand consciousness. Rather, it is treated as an unresolved problem that ``there may be physical constraints that are overlooked by information indicators alone.''
</p>

<h2>First, separate the four words</h2>
<table>
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

<h2>Do not mix 4 more measurement layers</h2>
<table>
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

<h2>"Irreversibility" is not one estimator family</h2>
<p>
One remaining weak point in thermodynamic discussions is that papers using similar words often compute different quantities. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> estimated entropy-production lower bounds from coarse-grained BOLD state transitions, <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">Deco et al. (2022)</a> and <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">de la Fuente et al. (2023)</a> measured time asymmetry from forward / reversed ECoG through time-shifted correlations or inversion decoding, <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">Nartallo-Kaluarachchi et al. (2025)</a> measured multilevel irreversibility from directed visibility-graph degree distributions on MEG, and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> estimated time-varying entropy flow from spike trains under a state-space kinetic Ising model. Therefore, on this site, the phrase <strong>irreversibility result</strong> is not read as one common measurement object.
</p>
<table>
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

<h2>What I'm not saying here</h2>
<table>
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

<h2>Separate logical and physical costs</h2>
<p>
Logical computational complexity, such as FLOPs, is an indicator of how much computation was performed. On the other hand, thermodynamic dissipation looks at the physical cost of performing the calculation. One or the other alone cannot fully express the difficulty of a constantly moving implementation.
</p>

<h2>What can be said relatively strongly now / What is still weak</h2>
<table>
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

<h2>How much can we tell from observations</h2>
<table>
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

<h2>Irreversibility route card</h2>
<p>
The reason this site now asks for a route card is simple: thermodynamic language alone does not tell you what quantity was computed or how fragile it is. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">Lynn et al. (2021)</a> checked that fluxes vanish after temporal shuffling, and <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> used trial-shuffled data to isolate coupling-related contributions from firing-rate dynamics and sampling error. Therefore, a modality label alone is not enough.
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
<td>Write modality, sensor / source / spike level, source reconstruction or parcelization if used, preprocessing summary, and the task / state contrast or segmentation window.</td>
<td>It blocks BOLD, ECoG, MEG, and spike-train results from sounding as if they were the same observation route.</td>
</tr>
<tr>
<td><strong>Estimator family</strong></td>
<td>Name whether the result comes from transition-flux lower bounds, time-shifted correlations, inversion classifiers, visibility graphs, state-space kinetic Ising models, or another explicit family.</td>
<td>It blocks all irreversibility papers from being collapsed into one common "EPR measurement."</td>
</tr>
<tr>
<td><strong>Null / surrogate control</strong></td>
<td>Write time-reversal baseline, temporal shuffle, trial shuffle, noise-floor estimate, motion control, or other surrogate that tests whether the headline asymmetry survives.</td>
<td>It blocks pipeline artifacts or firing-rate changes from being silently rephrased as nonequilibrium structure.</td>
</tr>
<tr>
<td><strong>Quantity type</strong></td>
<td>State explicitly whether the reported number is an entropy-production lower bound, asymmetry score, graph divergence, entropy-flow component, or a fuller entropy-production estimate.</td>
<td>It blocks asymmetry scores or lower bounds from being misread as direct microscopic dissipation.</td>
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

<h2>Operation rules fixed in 2026-03 audit</h2>

<h4>Rule</h4>
<ul>
<li><strong>Separate Landauer and implemented power:</strong>Do not confuse lower bound theory and measured power. </li>
<li><strong>Separate the organization's budget and acceptance gate:</strong>20W and signaling partition are background values and should not be made into site-wide KPIs. </li>
<li><strong>Distinguish information entropy production and physical dissipation:</strong>Do not write the lower bound estimation from coarse-grained neural data as physical dissipation itself. </li>
<li><strong>Name estimator family and null control:</strong>Transition-based lower bounds, time-shifted correlations, inversion classifiers, visibility graphs, and state-space Ising models are not interchangeable, and shuffle / surrogate controls are part of the claim. </li>
<li><strong>Thermodynamic indicators are not used in place of auxiliary logs:</strong>OOD generalization, perturbation, validation, uncertainty, and abstention conditions. </li>
<li><strong>Clarify modality dependence:</strong> Do not interchange fMRI, ECoG, EEG, and spiking with the same meaning. </li>
</ul>

<h2>4 questions when reading thermodynamic claims</h2>
<ol>
<li><strong>Are we talking about lower bounds or actual measurements?</strong>It is important not to confuse theoretical lower bounds such as Landauer's with actual consumption or dissipation. </li>
<li><strong>Which estimator family and null control were used?</strong>Check whether this is a transition-flux lower bound, time-shifted asymmetry score, visibility-graph index, or model-based spike-train estimate, and what shuffle / surrogate test was applied. </li>
<li><strong>Are you separating logical and physical costs?</strong>Are you combining FLOPs and dissipation into one number? </li>
<li><strong>What do you mean by this metric alone?</strong>Check whether EPR or NESS is being used alone to prove identity or consciousness. </li>
</ol>

<h2>Where to go back next</h2>
<p>
To return to the theory frame, please use <a href="https://mind-upload.com/perspective.html#design-principles">Theoretical frame</a>. To return to the long research note, please use <a href="https://mind-upload.com/perspective.html">Research note</a>. To return to the verification requirements, please use <a href="https://mind-upload.com/verification.html">Verification platform</a>.
</p>

<h2>References</h2>
<ol>
<li>B&eacute;rut, A., Arakelyan, A., Petrosyan, A., et al. (2012). Experimental verification of Landauer&rsquo;s principle linking information and thermodynamics. <em>Nature</em>, 483, 187-189. <a href="https://doi.org/10.1038/nature10872" target="_blank">doi:10.1038/nature10872</a></li>
<li>Attwell, D., &amp; Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>, 21(10), 1133-1145. <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">doi:10.1097/00004647-200110000-00001</a></li>
<li>Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001" target="_blank">doi:10.1088/0034-4885/75/12/126001</a></li>
<li>Lynn, C. W., et al. (2021). Broken detailed balance and entropy production in the human brain. <em>PNAS</em>, 118(47), e2109889118. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>Deco, G., Sanz Perl, Y., Bocaccio, H., Tagliazucchi, E., &amp; Kringelbach, M. L. (2022). The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. <em>Communications Biology</em>, 5, 572. <a href="https://doi.org/10.1038/s42003-022-03505-7" target="_blank">doi:10.1038/s42003-022-03505-7</a></li>
<li>de la Fuente, L. A., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <em>Cerebral Cortex</em>, 33(5), 1856–1865. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <em>PNAS</em>, 122(10), e2408791122. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
</ol>
