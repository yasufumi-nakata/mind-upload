# Wiki: Basics of verification infrastructure

> Before celebrating a score, fix the ruler, the route card, and the failure log.
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-27 / 位置づけ: Beginner guide

## このページの役割
This page explains from the beginning why Mind-Upload focuses on standards, benchmarks, preregistration, route cards, and audits. The goal is to show why technical progress becomes comparable only when the benchmark object, evidence pathway, and any human proxy bundle or sequential bridge are disclosed rather than left implicit.

## 正確さの前提
The analogies here are for orientation only. Always return to the public specification pages to see the actual operational rules.

## 公開ページへ戻る
- [Verification platform](https://mind-upload.com/verification.html)
- [Casework](https://mind-upload.com/verification.html#casework)
- [Datasets and Hands-On Work](https://mind-upload.com/datasets.html)

## 関連 Wiki
- [Wiki: How to read claims and evidence](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - Shows why the same headline can still hide different evidence classes.
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - Gives the broader technical picture before the operational details.
- [Wiki: Baselines, preregistration, and model cards](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Separates the operational roles of these commonly mixed terms.
- [Wiki: Measurement-stack observability and claim ceilings](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling) - Shows why route-card logic is needed for different measurement classes.
- [Wiki: Human Proxy Composition and Route Maturity](https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition) - Explains why current human proxy rows do not automatically compose into same-subject state closure.
- [Wiki: State-Continuity Bridge](https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge) - Explains why same-subject or same-brain sequential workflows still need bridge validation before same-state language is allowed.

## いま分かっていること
- Comparable progress requires aligned inputs, evaluation, rules, and records.
- Without preregistration and auditing, it becomes too easy to promote only favorable conditions.
- Recent primary literature shows that decode, tractography, effective-connectivity, thermodynamic, closed-loop, human-proxy-composition, and bridge claims fail in different ways and therefore need different cards.
- Proxy class, operational maturity, and calibrator role are different questions; a real human route may still calibrate only one bounded hidden-state family.
- A proxy bundle still needs repeatability / transfer, shared-driver / quantity-bridge, and increment disclosure before it rises above the strongest single row.
- Same-subject or same-brain wording can secure specimen identity while still leaving state continuity unresolved.

## まだ分かっていないこと
- A complete WBE benchmark stack does not yet exist in finished public form.
- Which combination of human proxy rows and bridge validations could ever support stronger same-subject continuity claims remains unresolved.
- Which additional requirements would be sufficient for future L4 or L5 claims remains unresolved.

---

<h2>Why the ruler comes first</h2>
<p>
If two groups use different inputs, different split rules, different metric bundles, different hidden assumptions, different human proxy combinations, and different bridge assumptions, comparing their scores does not tell you who made more progress. The Verification Commons exists so that progress claims can survive comparison rather than only presentation.
</p>

<strong>2026-03-19 beginner update: generic audits were no longer enough</strong>
<p>
The older beginner explanation correctly said that standards and audits matter, but it still sounded as if one generic score sheet could cover every kind of neuroscience result. That is no longer safe enough. Different claim families now need different route cards because they fail for different scientific reasons.
</p>

<strong>2026-03-25 beginner tightening: proxy bundles and bridges are not side details</strong>
<p>
The current site had also become stricter in two ways that this beginner page still underplayed. First, several living-human proxy rows can all be real while still measuring different quantity types, spatial units, timescales, and model burdens. Second, <strong>same-subject</strong> or <strong>same-brain</strong> wording can still hide a sequential bridge across fixation, deformation, behavior, sleep/wake regime, or elapsed time. Those are scientific stop lines, not administrative add-ons.
</p>

<strong>2026-03-26 beginner tightening: proxy bundles now need three axes and three gates</strong>
<p>
The remaining weakness was subtler. Even after telling readers that proxy bundles matter, this page still left too much room to think that listing several human rows side by side was already most of the work. The current site rule is stricter: a bundle must first disclose <strong>proxy class</strong>, <strong>operational maturity</strong>, and <strong>calibrator role</strong>, and then show that it passes <strong>robustness</strong>, <strong>common-driver / quantity-bridge</strong>, and <strong>increment</strong> gates. Without that, proxy-rich evidence remains scientifically meaningful but still below same-subject state closure.
</p>

<strong>2026-03-27 correction: route-family names were still too coarse</strong>
<p>
This beginner page also had to become stricter inside the human-bundle example itself. On the current site, <strong>1H-MRSI similarity</strong>, <strong>31P energetic balance</strong>, and <strong>deuterium metabolite / rate imaging</strong> are different spectroscopy rows; <strong>myelin-water / MT-family / bilayer / qT1 remyelination-sensitive</strong> routes are not one myelin meter; <strong>BBB water-exchange MRI</strong> is not <strong>tracer-specific BBB PET transport</strong>; and <strong>MAO-B</strong> astrocyte PET is not <strong>I<sub>2</sub>BS</strong> astrocyte PET. If those splits are hidden, the bundle looks much closer to one state meter than the primary literature allows.
</p>

<h2>The five parts of comparable progress</h2>
<table>
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
<td>Aligns the task, split rules, metric bundle, and benchmark governance.</td>
<td>The same exam and scoring rubric.</td>
</tr>
<tr>
<td><strong>Preregistration / registry</strong></td>
<td>Locks success/failure conditions before the result is known.</td>
<td>The rules announced before the exam starts.</td>
</tr>
<tr>
<td><strong>Route card</strong></td>
<td>Discloses the evidence pathway, assumptions, omitted alternatives, and abstention boundary for a specific claim family or bridge class.</td>
<td>The answer key that says which reasoning steps were allowed.</td>
</tr>
<tr>
<td><strong>Audit / model card / log</strong></td>
<td>Records weaknesses, drift, failures, recalibration, benchmark postmortems, and unresolved limits.</td>
<td>The report card plus the error log.</td>
</tr>
</tbody>
</table>

<h2>What goes wrong when one part is missing</h2>
<table>
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
<td>Different groups can claim victory on different tasks, split regimes, metric bundles, or organizer-conditioned benchmark versions.</td>
</tr>
<tr>
<td>Preregistration</td>
<td>It becomes too easy to keep only the convenient conditions and present them as the intended target all along.</td>
</tr>
<tr>
<td>Route card</td>
<td>A result is overread beyond the evidence class or bridge class that produced it.</td>
</tr>
<tr>
<td>Audit</td>
<td>Weaknesses, drift, shortcuts, recalibration burden, benchmark revisions, and abstentions disappear behind one score.</td>
</tr>
</tbody>
</table>

<strong>Two newer beginner stop lines this page now has to carry</strong>
<p>
The current site can no longer leave two failure modes to the deep pages only. One is <strong>composition failure</strong>: several living-human proxy rows can all be valid yet still fail to compose into one same-subject latent-state estimate. The other is <strong>bridge failure</strong>: the same subject or same brain can still be sampled under a changed preparation, coordinate frame, or physiological regime. A beginner page that omits those stop lines now understates the scientific uncertainty.
</p>

<h2>Human proxy bundles now need three axes and three gates</h2>
<p>
The remaining beginner weakness was that saying <strong>proxy bundles matter</strong> still left too much room for readers to imagine that listing several living-human rows side by side was already most of the work. The current site rule is stricter. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a>, <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a>, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a>, <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">Padrela et al. (2025)</a>, <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a>, <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a>, <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a>, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> do not all measure the same quantity, do not run at the same burden, and do not safely calibrate the same hidden-state family. Therefore, a beginner page now has to separate <strong>what class of proxy the row is</strong>, <strong>how operationally mature the route is</strong>, and <strong>what bounded calibrator role it can safely play</strong>.
</p>
<table>
<thead>
<tr>
<th>Axis</th>
<th>What it asks</th>
<th>What goes wrong if omitted</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Proxy class</strong></td>
<td>What is directly observed: density proxy, biochemical similarity scaffold, energetic-balance route, deuterium metabolite / rate route, quantity-defined myelin route, BBB water-exchange route, tracer-specific BBB transport route, target-defined astrocyte PET, support-state / mobility proxy, model-based efflux route, or destructive local scaffold?</td>
<td>Different quantity types are silently compressed into one progress bar.</td>
</tr>
<tr>
<td><strong>Operational maturity</strong></td>
<td>How specialized, small-cohort, model-heavy, or centre-bound is the route at its actual operating point?</td>
<td>A proof-of-principle route can be mistaken for portable whole-brain measurement.</td>
</tr>
<tr>
<td><strong>Calibrator role</strong></td>
<td>Which hidden-state family does the route safely constrain, and what still remains latent?</td>
<td>A real route can be overread as broadly calibrating maintenance-state completeness.</td>
</tr>
</tbody>
</table>
<p>
Even that three-axis typing is still not enough. <a href="https://doi.org/10.1177/0271678X17724947" target="_blank">Finnema et al. (2018)</a> showed route-specific SV2A PET test-retest reproducibility of <strong>3-9%</strong> for regional V<sub>T</sub>, <a href="https://doi.org/10.1371/journal.pone.0206583" target="_blank">Holiga et al. (2018)</a> showed fMRI reliability ranging from <strong>poor to excellent</strong>, and <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a> showed that some simultaneous EEG-fMRI connectome relationships can reproduce across <strong>72 subjects from four centres</strong> spanning <strong>1.5T to 7T</strong>. <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> then showed that a multimodal acute-DoC dataset can shrink from <strong>87 enrolled patients</strong> to <strong>63 with both EEG and fMRI</strong> and <strong>48</strong> for direct same-feature comparison, while <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> showed that adding modalities can improve prediction while still increasing <strong>inter-modality disagreement</strong> in clinically important groups. Finally, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed both <strong>common and divergent</strong> cross-modal organization, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can coexist with <strong>opposite oxygen-metabolism changes</strong>. Therefore, a human proxy bundle now rises only if it passes three separate gates.
</p>
<table>
<thead>
<tr>
<th>Gate</th>
<th>What must be shown</th>
<th>Ceiling if it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Robustness</strong></td>
<td>Show row-level repeatability at the actual operating point, distinguish route-local repeatability from cross-centre transfer, and disclose the real complete-case slice.</td>
<td>The bundle remains setup-bound, centre-bound, or complete-case-bound evidence.</td>
</tr>
<tr>
<td><strong>Common-driver / quantity-bridge</strong></td>
<td>Show that the rows are not only synchronized, but interpretable on an explicitly named biological axis after shared-driver audit.</td>
<td>Cross-row agreement remains proxy-rich correlation or shared-factor evidence rather than one validated state variable.</td>
</tr>
<tr>
<td><strong>Increment over the strongest single row</strong></td>
<td>Show what the bundle adds beyond the best individual row under matched cohort, condition, and reading rule.</td>
<td>Row diversity remains richer description, not same-subject state closure.</td>
</tr>
</tbody>
</table>
<p>
If the bundle is sequential rather than same-session, the <a href="https://mind-upload.com/verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> is added on top. <strong>Same-subject</strong> still solves specimen identity, not state continuity.
</p>

<h2>Why modern neuroscience needs claim-specific route cards</h2>
<table>
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
<tr>
<td><strong>Living-human proxy bundle</strong></td>
<td>SV2A PET, 1H-MRSI similarity, 31P energetic balance, deuterium metabolite / rate imaging, quantity-defined myelin MRI, BBB water-exchange MRI, tracer-specific BBB PET, target-defined astrocyte PET, and clearance routes measure different quantity / target / transport types, spatial units, timescales, model burdens, and safe calibrator roles; even a well-typed bundle still needs robustness, shared-driver / quantity-bridge, and increment disclosure.</td>
<td>Human Proxy Composition Card.</td>
</tr>
<tr>
<td><strong>Sequential same-subject / same-brain bridge</strong></td>
<td>Specimen identity does not by itself fix state continuity across fixation, deformation, behavior, sleep/wake regime, or elapsed time.</td>
<td>State-Continuity Bridge Card, plus Temporal Validity Card when the bridge crosses hours to days.</td>
</tr>
</tbody>
</table>

<h2>Why this matters especially for WBE</h2>
<p>
WBE is especially vulnerable to level substitution. It is easy to describe an L1 decoding result as if it were approaching L4 continuity, or to describe one route-conditioned measurement as if it had solved a whole class of hidden states. Verification infrastructure is therefore not administrative overhead. It is part of the scientific content because it prevents the evidence class from changing silently after the result is known.
</p>

<strong>Representative primary-literature reasons</strong>
<p>
<a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> and <a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">Di et al. (2021)</a> show why decode scores need shortcut audits. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">Thomas et al. (2014)</a> and <a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017)</a> show why tractography claims need route disclosure. <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">Penny et al. (2004)</a> and <a href="https://pubmed.ncbi.nlm.nih.gov/22561579/" target="_blank">Rosa et al. (2012)</a> show why effective-connectivity claims need candidate-model disclosure. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">Lynn et al. (2021)</a> and <a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> show why thermodynamic language hides multiple estimator families. <a href="https://pubmed.ncbi.nlm.nih.gov/31551604/" target="_blank">Musall et al. (2019)</a> and <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">Flesher et al. (2021)</a> show why closed-loop results need a boundary card rather than latency alone. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a>, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a>, <a href="https://doi.org/10.1002/nbm.3384" target="_blank">Ren et al. (2015)</a>, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a>, <a href="https://doi.org/10.1002/mrm.70308" target="_blank">Karkouri et al. (2026)</a>, <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">Padrela et al. (2025)</a>, <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">Chung et al. (2025)</a>, <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a>, <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">Tyacke et al. (2018)</a>, <a href="https://doi.org/10.1177/0271678X17724947" target="_blank">Finnema et al. (2018)</a>, <a href="https://doi.org/10.1371/journal.pone.0206583" target="_blank">Holiga et al. (2018)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a>, <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a>, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a>, <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a>, and <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> show why current living-human proxy rows do not all measure the same object, do not share one robustness level, and do not automatically add up to same-subject state closure. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a>, <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">Idziak et al. (2023)</a>, <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a>, and <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">Egger et al. (2024)</a> show why same-subject or same-brain sequencing still needs bridge validation.
</p>

<h2>How this beginner page connects to the site</h2>
<p>
On Mind-Upload, the public <a href="https://mind-upload.com/verification.html">Verification</a> page is the operational blueprint. <a href="https://mind-upload.com/datasets.html">Datasets and Hands-On Work</a> supplies the entry datasets and minimum implementation loop. The route-card and audit logic explained here is expanded in the public specification and in the topic-specific wiki pages.
</p>

<table>
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
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence">How to read claims and evidence</a></td>
<td>It gives the shortest claim-reading workflow.</td>
</tr>
<tr>
<td>Why route cards differ by measurement class</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling">Measurement-stack observability and claim ceilings</a></td>
<td>It shows what is directly observed and where each stack stops.</td>
</tr>
<tr>
<td>Why proxy-rich human evidence still stops below same-subject state closure</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition">Human Proxy Composition and Route Maturity</a></td>
<td>It separates quantity type, route maturity, calibrator role, and residual hidden-state ceiling.</td>
</tr>
<tr>
<td>Why same-subject or same-brain wording still needs a bridge audit</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge">State-Continuity Bridge</a></td>
<td>It separates specimen identity from state continuity, coordinate continuity, and bridge validation.</td>
</tr>
<tr>
<td>The full operational blueprint</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td>It defines the public rules, cards, and logs in full.</td>
</tr>
</tbody>
</table>

<h4>Next</h4>
<p>If you want to see how strong-looking headlines are translated into safer first readings, continue here.</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence">How to read claims and evidence →</a>

<h2>References</h2>
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
<li>Lu, X., Han, X., Meirovitch, Y., et al. (2023). Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. <em>Cell Reports Methods</em>. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>Idziak, A., Inavalli, V. V. G. K., Bancelin, S., Arizono, M., &amp; Nagerl, U. V. (2023). The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. <em>eNeuro</em>. <a href="https://doi.org/10.1523/ENEURO.0104-23.2023" target="_blank">doi:10.1523/ENEURO.0104-23.2023</a></li>
<li>Johansen, A., Beliveau, V., Colliander, E., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <em>Journal of Neuroscience</em>. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Ren, J., Sherry, A. D., &amp; Malloy, C. R. (2015). <sup>31</sup>P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. <em>NMR in Biomedicine</em>. <a href="https://doi.org/10.1002/nbm.3384" target="_blank">doi:10.1002/nbm.3384</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <em>PNAS Nexus</em>. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Karkouri, J., Novoselova, M., Rodgers, C. T., et al. (2026). Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. <em>Magnetic Resonance in Medicine</em>. <a href="https://doi.org/10.1002/mrm.70308" target="_blank">doi:10.1002/mrm.70308</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., et al. (2024). Myelin bilayer mapping in the human brain in vivo. <em>Magnetic Resonance in Medicine</em>. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Padrela, B. E., Slivka, M., Sneve, M. H., et al. (2025). Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. <em>Neurobiology of Aging</em>. <a href="https://doi.org/10.1016/j.neurobiolaging.2024.12.012" target="_blank">doi:10.1016/j.neurobiolaging.2024.12.012</a></li>
<li>Chung, K. J., Abdelhafez, Y. G., Spencer, B. A., et al. (2025). Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-025-58356-7" target="_blank">doi:10.1038/s41467-025-58356-7</a></li>
<li>Villemagne, V. L., Harada, R., Dore, V., et al. (2022). Assessing reactive astrogliosis with <sup>18</sup>F-SMBT-1 across the Alzheimer disease spectrum. <em>Journal of Nuclear Medicine</em>. <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">doi:10.2967/jnumed.121.263255</a></li>
<li>Tyacke, R. J., Myers, J. F. M., Venkataraman, A., et al. (2018). Evaluation of <sup>11</sup>C-BU99008, a PET Ligand for the Imidazoline<sub>2</sub> Binding Site in Human Brain. <em>Journal of Nuclear Medicine</em>. <a href="https://doi.org/10.2967/jnumed.118.208009" target="_blank">doi:10.2967/jnumed.118.208009</a></li>
<li>Hirschler, L., Runderkamp, B. A., Decker, A., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Benisty, H., Barson, D., Moberly, A. H., et al. (2024). Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Egger, A., Bayon, C., d'Almeida, J., et al. (2024). Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. <em>Scientific Reports</em>, 14, 20247. <a href="https://doi.org/10.1038/s41598-024-70609-x" target="_blank">doi:10.1038/s41598-024-70609-x</a></li>
<li>Dagum, P., Elbert, D. L., Giovangrandi, L., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Finnema, S. J., Nabulsi, N. B., Mercier, J., et al. (2018). Kinetic evaluation and test-retest reproducibility of [<sup>11</sup>C]UCB-J, a novel radioligand for positron emission tomography imaging of synaptic vesicle glycoprotein 2A in humans. <em>Journal of Cerebral Blood Flow &amp; Metabolism</em>, 38(11), 2041-2052. <a href="https://doi.org/10.1177/0271678X17724947" target="_blank">doi:10.1177/0271678X17724947</a></li>
<li>Holiga, S., Sambataro, F., Luzy, C., et al. (2018). Test-retest reliability of task-based and resting-state blood oxygen level dependence and cerebral blood flow measures. <em>PLOS ONE</em>, 13(11), e0206583. <a href="https://doi.org/10.1371/journal.pone.0206583" target="_blank">doi:10.1371/journal.pone.0206583</a></li>
<li>Wirsich, J., Jorge, J., Iannotti, G. R., et al. (2021). The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. <em>NeuroImage</em>, 231, 117864. <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>Amiri, M., Fisher, P. M., Raimondo, F., et al. (2023). Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. <em>Brain</em>, 146(1), 50-64. <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/brain/awac335</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>, 15, 229. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Epp, S. M., Halani, S., Paquette, M., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Manasova, V., et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <em>Brain</em>. <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/brain/awaf412</a></li>
</ol>
