# Wiki: Multimodal Integration Basics

> Shared clocks, shared factors, and quantity bridges are different achievements
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-04-03 / Role: Technical / natural science only (rewritten on 2026-04-03 for Fusion Card consistency)

## Role Of This Page
This page organizes what current primary literature actually supports when EEG, MEG, fMRI, PET, fNIRS, invasive recordings, and MRI are combined. The purpose is not to celebrate fusion by default, but to separate synchronization, geometry, physiology, model burden, and bundle robustness into auditable pieces.

## Accuracy Notes
This page does not argue that adding modalities makes state-complete readout likely. It explains which claim ceiling rises, which one does not, and why.

## Back To Public Pages
- [EEG 101](https://mind-upload.com/eeg_101.html)
- [Verification](https://mind-upload.com/verification.html)
- [Technical Roadmap](https://mind-upload.com/tech_roadmap.html)

## Related Wiki Pages
- [Wiki: EEG Basics](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - Return here when you want the ceiling of EEG alone.
- [Wiki: Observability and Claim Ceiling by Measurement Stack](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling) - Use this next for the stack-by-stack ceiling table.
- [Wiki: Human Proxy Composition and Route Maturity](https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition) - Use this when the multimodal bundle also mixes living-human proxy classes.
- [Wiki: Event Synchronization and Measurement Logs](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Introduces shared clocks, delays, jitter, and drift.
- [Wiki: Uncertainty, Confidence, and Abstention](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - Explains why uncertainty remains even after fusion.
- [Wiki: From Observation to Estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Keeps direct observables separate from inferred latent variables.
- [Wiki: Baselines, Preregistration, and Model Cards](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Use this when a multimodal result needs the Fusion Card workflow.

## What Is Currently Known
- Combining modalities can strengthen specific questions about timing, spatial localization, calibration, or bundle-level prediction.
- The gain depends on synchronization path, subject-specific geometry, field/noise control, physiology-side interpretation, and model burden.
- Simultaneous acquisition, a shared component, and one externally calibrated biological variable are different claim levels.
- Same-session multimodal studies can still mix event-locked electrophysiology, hemodynamic windows, and scan-window or kinetic metabolic quantities, so shared clocks do not define one temporal object.
- A shared low-frequency/global factor can mix neural, autonomic, and vascular contributions, so common structure is not automatic target-variable specificity.
- A coupled trajectory is not yet a quantity bridge unless the compared biological axis is named and externally grounded.
- A multimodal gain can still depend on which samples carried the full bundle, how missing modalities were handled, and whether disagreement grows in hard regimes.
- For EEG + fMRI and EEG + fNIRS, alignment alone is insufficient; hemodynamic transfer and superficial/systemic contamination remain separate audits.
- OPM-MEG can tolerate more movement than fixed SQUID systems, but only under disclosed shielding, active field control, calibration, and anatomy assumptions.
- Invasive recordings remain valuable external calibration routes with strong spatial and cohort bias.

## What Is Still Unknown
- Which multimodal bundle is best for each WBE-relevant stage remains unsettled.
- Even richer multimodal stacks still do not settle the sufficiency of synaptic, glial, transcriptional, neuromodulatory, or maintenance-state observability.
- How to benchmark shared-vs-specific decompositions across human multimodal stacks remains unresolved.
- How to benchmark effective-window compatibility across simultaneous multimodal studies remains unresolved.
- Which quantity bridges can be externally calibrated across electrophysiological, hemodynamic, metabolic, and autonomic stacks remains unresolved.
- How to compare multimodal bundles fairly when complete-case availability, centre mix, or subgroup disagreement differ remains unresolved.

---

<h2>Conclusion</h2>
<p>
Multimodal integration can raise some claim ceilings, but it does not erase inverse problems, physiology bridges, or robustness burdens. On this site, a multimodal paper is read only after <strong>synchronization</strong>, <strong>geometry</strong>, <strong>temporal-kernel relation</strong>, <strong>hemodynamic or metabolic interpretation</strong>, <strong>shared-vs-specific structure</strong>, <strong>quantity bridge</strong>, and <strong>bundle robustness</strong> are audited separately.
</p>

<strong>How this page fits the site</strong>
<p>
This is the background page for <a href="https://mind-upload.com/verification.html#fusion-card">Verification: Fusion Card</a>. Verification gives the operating rule. This page explains why the rule has to be strict, which routes currently earn stronger readings, and where the claim ceiling still stops.
</p>

<strong>Why this page had to be rewritten</strong>
<p>
The older version pointed in the right direction, but it still left three shortcuts too easy to make. First, <strong>same-session</strong> could still be mistaken for one matched temporal object. Second, a <strong>shared factor</strong> could still be mistaken for the target biological variable or for a solved <strong>quantity bridge</strong>. Third, a <strong>multimodal gain</strong> could still be mistaken for a robust, availability-agnostic bundle. The primary literature does not support any of those jumps. The current rewrite makes those stop rules explicit and also fixes one overcorrection: a physiology-linked global factor is not automatically just "artifact"; it can be a real coupled process while still failing to equal the neural target variable of interest.
</p>

<strong>Scope</strong>
<p>
This page stays on the technical and natural-science side only. It does not use multimodal language to settle identity, consciousness, law, or ethics. The narrower question is: <strong>what did the multimodal paper actually add, and what still remains conditional?</strong>
</p>

<h2>Eleven audit gates to fix first</h2>
<table>
<thead>
<tr>
<th>Gate</th>
<th>What passing the gate can support</th>
<th>What this site still stops claiming if the gate is absent</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Synchronization gate</strong></td>
<td>Shared clocks, delays, jitter, and drift are disclosed well enough to compare streams in time.</td>
<td>Shared timestamps alone do not become temporally aligned latent-state evidence.</td>
</tr>
<tr>
<td><strong>Geometry gate</strong></td>
<td>Individual MRI, measured electrode or sensor positions, and a declared forward model strengthen spatial interpretation.</td>
<td>The result is not read as exact anatomical truth just because anatomy was added.</td>
</tr>
<tr>
<td><strong>Noise / field gate</strong></td>
<td>MR artifact, motion artifact, magnetic background field, crosstalk, and cross-talk routes are handled transparently.</td>
<td>A cleaner fused output is not treated as direct neural ground truth.</td>
</tr>
<tr>
<td><strong>Hemodynamic transfer gate</strong></td>
<td>For fMRI or fNIRS, vascular-state, CVR, and superficial/systemic burdens are either calibrated or left as abstention limits.</td>
<td>BOLD, HbO, or HbR amplitude differences are not read as clean neural differences by default.</td>
</tr>
<tr>
<td><strong>External validation gate</strong></td>
<td>Errors can be audited against invasive recordings, electrical stimulation, postoperative outcomes, phantoms, or other external references.</td>
<td>Model output alone is not read as validated localization or fused truth.</td>
</tr>
<tr>
<td><strong>Fusion Card gate</strong></td>
<td>Acquisition relation, lag audit, co-registration scope, fusion model, and gain over unimodal or prior-only baselines are made visible.</td>
<td>"Simultaneous," "multimodal," or "atlas-informed" is not treated as self-validating fusion.</td>
</tr>
<tr>
<td><strong>Effective-window / temporal-kernel gate</strong></td>
<td>Each stack's temporal object is named, such as event-locked electrophysiology, hemodynamic response window, scan-window average, or minutes-long kinetic route.</td>
<td>Same-session acquisition is not promoted to one synchronous state sample when the kernels still differ.</td>
</tr>
<tr>
<td><strong>Shared-vs-specific component gate</strong></td>
<td>The paper states whether the effect lives in a shared component, a modality-specific residual, or a physiology-linked global factor.</td>
<td>A common factor is not promoted to the target biological variable by default.</td>
</tr>
<tr>
<td><strong>Quantity-bridge / physiology-grounding gate</strong></td>
<td>The paper names the biological axis on which modalities are being compared and shows why those quantities are commensurate.</td>
<td>Cross-modal covariance is not promoted to one solved neural quantity without a declared bridge.</td>
</tr>
<tr>
<td><strong>Bundle robustness gate</strong></td>
<td>The paper discloses complete-case slice, missing-modality handling, transfer across centres or scanners, and disagreement in hard subgroups.</td>
<td>"More modalities improved performance" is not read as robust, acquisition-complete bundle evidence.</td>
</tr>
<tr>
<td><strong>State-coverage gate</strong></td>
<td>The paper states which state families were actually constrained and which ones remain unobserved.</td>
<td>Multimodal integration is not promoted to state completeness for WBE-relevant hidden variables.</td>
</tr>
</tbody>
</table>

<strong>Minimum fusion package on this site</strong>
<p>
For multimodal or atlas-prior routes, this page follows the same disclosure bundle as <a href="https://mind-upload.com/verification.html#fusion-card">Verification: Fusion Card</a>: <strong>acquisition relation</strong>, <strong>clock / lag audit</strong>, <strong>effective-window / temporal-kernel relation</strong>, <strong>geometry / co-registration scope</strong>, <strong>fusion object and model burden</strong>, <strong>shared-vs-specific component disclosure</strong>, <strong>quantity bridge / physiology grounding</strong>, <strong>incremental evidence over unimodal / prior-only baselines</strong>, <strong>availability / complete-case slice</strong>, <strong>missing-modality policy</strong>, <strong>cross-centre / cross-scanner transfer window</strong>, and <strong>external calibration plus abstention boundary</strong>. If those fields are missing, the result stays at the ceiling of the strongest individually supported stack.
</p>

<strong>Three objects that are often collapsed into one phrase</strong>
<p>
On this site, <strong>synchronized streams</strong>, <strong>a shared cross-modal factor</strong>, and <strong>one externally grounded biological quantity</strong> are three different achievements. The first is an acquisition property. The second is a statistical result. The third is a biological interpretation that still needs calibration, bridge logic, and an abstention boundary.
</p>

<h2>What current primary literature supports for each major route</h2>
<table>
<thead>
<tr>
<th>Route</th>
<th>What current primary literature really supports</th>
<th>What still remains open or conditional</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG + individual MRI / forward model</strong></td>
<td>Subject-specific anatomy, measured electrode positions, and realistic head models strengthen source-imaging conditions and can be externally checked against intracranial stimulation.</td>
<td>Depth bias, conductivity uncertainty, and non-uniqueness remain; this is improved geometry, not direct local circuit truth.</td>
</tr>
<tr>
<td><strong>EEG + MEG</strong></td>
<td>Complementary sensitivity profiles can improve source reconstruction when a calibrated realistic conductor model is used.</td>
<td>The gain depends on co-registration and conductivity modeling rather than modality count alone.</td>
</tr>
<tr>
<td><strong>EEG + fMRI</strong></td>
<td>Joint acquisition can support reproducible cross-stack analyses and model-conditioned fusion of temporal and spatial information.</td>
<td>Temporal-kernel mismatch, MR artifact burden, and vascular-state / CVR interpretation remain separate ceilings.</td>
</tr>
<tr>
<td><strong>EEG + fNIRS</strong></td>
<td>Portable hemodynamic-electrophysiological pairing can strengthen bounded task reading when superficial and systemic signals are measured and regressed explicitly.</td>
<td>Without short-separation or equivalent superficial diagnostics, HbO/HbR differences still carry extracerebral and autonomic burden.</td>
</tr>
<tr>
<td><strong>EEG + PET + MRI</strong></td>
<td>Tri-modal acquisition can reveal coordinated electrophysiological, hemodynamic, and metabolic progression within one experimental session.</td>
<td>PET quantification remains model-bearing, temporal kernels still differ, and shared trajectories do not by themselves establish one validated latent state.</td>
</tr>
<tr>
<td><strong>EEG + invasive recording</strong></td>
<td>Simultaneous scalp and invasive recordings provide strong external calibration for limited spatial domains and selected source regimes.</td>
<td>Coverage is sparse, clinically biased, and not whole-brain ground truth.</td>
</tr>
<tr>
<td><strong>OPM-MEG</strong></td>
<td>Wearable systems can extend MEG into standing, ambulatory, and interactive paradigms when field control is engineered carefully.</td>
<td>Shielding class, active nulling, sensor calibration, anatomy route, and crosstalk still define the claim ceiling.</td>
</tr>
</tbody>
</table>

<h2>What each route actually adds</h2>

<h3>1. EEG + MRI adds audited geometry, not ground truth</h3>
<p>
Individual MRI, measured electrode positions, and a realistic forward model materially improve EEG source-imaging conditions. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> then added direct stimulation-based validation in human patients. That is a real step forward. But the safe reading is still narrow: even after subject-specific geometry is added, source depth, conductivity choice, and inverse-family choice continue to matter. On this site, EEG + MRI is therefore read as <strong>better geometric auditability</strong>, not as direct local neural truth and not as solved uniqueness.
</p>

<h3>2. EEG + MEG complements sensitivity profiles only when the physical model is improved</h3>
<p>
EEG and MEG are worth combining because they respond differently to source orientation and volume conduction. But the gain does not come from bimodality in the abstract. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">Aydin et al. (2014)</a> showed that the improvement depends on a <strong>calibrated realistic volume conductor model</strong>. On this site, EEG + MEG is therefore read as a route whose ceiling rises only when the <strong>conductivity model, co-registration, and inverse assumptions</strong> are disclosed, not as a generic "more sensors solved the source problem" result.
</p>

<h3>3. EEG + fMRI adds cross-stack complementarity, but not a neural-only readout</h3>
<p>
Simultaneous EEG-fMRI remains scientifically useful because it can relate fast electrophysiology to slower hemodynamic organization under one acquisition protocol. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">Jorge et al. (2015a)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">Jorge et al. (2015b)</a>, and <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a> showed that the route is feasible and can support reproducible cross-stack analysis. But the ceiling still stops early in two different places.
</p>
<p>
The first limit is temporal. <a href="https://doi.org/10.1155/2016/4182483" target="_blank">Nguyen et al. (2016)</a> made explicit that even spatiotemporally constrained EEG-fMRI source imaging does <strong>not</strong> erase the temporal mismatch between EEG and the hemodynamic response. The second limit is interpretive. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">Murphy et al. (2011)</a>, <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">Williams et al. (2023)</a>, and <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">Wu et al. (2023)</a> show why vascular-state and CVR differences still matter for BOLD reading, while <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> show that task BOLD changes can even oppose oxygen-metabolism changes across parts of cortex. On this site, EEG + fMRI therefore remains <strong>shared acquisition plus a declared cross-kernel relation</strong>, not automatic same-state or same-quantity evidence.
</p>

<strong>The same stop rule applies to EEG + fNIRS</strong>
<p>
The portable hemodynamic route is scientifically useful, but it does not escape physiology-side burdens. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">Yucel et al. (2015)</a> showed that short-separation regression improves localization and statistical significance when autonomic responses differ across tasks, and <a href="https://doi.org/10.1117/1.NPh.12.3.035009" target="_blank">An et al. (2025)</a> showed that short-channel regression can improve sensitivity and validity even in a working-memory task with minimal motor demand. Therefore, on this site, EEG + fNIRS without <strong>short-separation or equivalent superficial/systemic disclosure</strong> is not treated as a clean neural-difference readout.
</p>

<h3>4. EEG + PET + MRI adds coordinated multi-timescale physiology, not fused ground truth</h3>
<p>
Tri-modal EEG-PET-MRI is the route that most strongly needed tightening on this page. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed that simultaneous EEG-PET-MRI can reveal tightly coupled global hemodynamic and metabolic progression together with distinct spatial network structure across wakefulness and NREM sleep. That is a real advance because one protocol can now compare electrophysiological arousal, hemodynamic fluctuation, and metabolic decline in the same session.
</p>
<p>
But the safe reading still stops well short of fused state truth. PET quantification remains model-bearing. The hemodynamic side still carries vascular interpretation. The temporal object is still split: <a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">Ripp et al. (2021)</a> showed in simultaneous FDG-PET/fMRI working-memory data that PET still had to be read through <strong>scan-window averages</strong> rather than event-scale timing. On this site, tri-modal synchrony is therefore read as <strong>coordinated multi-timescale evidence</strong> unless the paper explicitly shows how second-scale electrophysiology, hemodynamic response windows, and PET kernels are being compared.
</p>

<strong>A shared global factor is not automatically the neural target, but it is not automatically mere nuisance either</strong>
<p>
The deeper correction on this page is that shared low-frequency structure must be <strong>typed</strong>, not simply praised or dismissed. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed that multimodal spontaneous-brain measures contain both <strong>common</strong> and <strong>divergent</strong> organization. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed that a major global fMRI mode is strongly coupled to autonomic physiology as well as EEG, while <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al. (2019)</a> showed that sympathetic activity contributes to fMRI signal changes during EEG-marked arousal events. The correct reading is not "therefore it is meaningless," and not "therefore it is the target neural variable." The correct reading is that a reported common factor must be labeled as <strong>shared neural candidate</strong>, <strong>physiology-linked common driver</strong>, <strong>modality-specific residual</strong>, or <strong>mixed / unresolved</strong>.
</p>

<p>
One more stop rule is needed before a coupled trajectory becomes a <strong>quantity bridge</strong>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that significant task BOLD changes can oppose oxygen-metabolism changes across many cortical voxels. Therefore, even strong coupling across EEG, fMRI, and PET does not by itself show that all three stacks now read one solved biological quantity. On this site, a multimodal paper must say whether it established only a <strong>shared trajectory</strong>, a <strong>physiology-linked common driver</strong>, or an explicit <strong>quantity bridge on a named biological axis</strong>.
</p>

<h3>5. More modalities can help without making the bundle robust by default</h3>
<p>
The next correction is operational rather than geometric. A multimodal paper can improve prediction or uncertainty while still leaving the bundle fragile to missing modalities, site shifts, or disagreement in hard subgroups. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a> showed in acute brain injury that adding modalities can decrease prognostic uncertainty and improve accuracy. That is a genuine bundle-level gain. But the gain is not the same thing as a robust multimodal bundle.
</p>
<p>
<a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> showed that direct same-sample multimodal comparison relied on a restricted <strong>complete-feature subset</strong>, so the comparison itself depends on who actually carried the full bundle. <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> then showed that multimodal classifiers can combine missing-modality handling with cross-centre testing while still showing higher <strong>pairwise disagreement</strong> in <strong>minimally conscious</strong> or <strong>improving</strong> patients. On this site, "multimodal gain" therefore stops at <strong>bundle-performance evidence under a declared availability, transfer, and disagreement regime</strong> unless the paper proves more.
</p>

<h3>6. EEG + invasive recording is a strong calibration route, but only for bounded coverage</h3>
<p>
Simultaneous scalp and invasive recordings are among the strongest external calibration routes available to human multimodal studies. <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">Zhang et al. (2006)</a> used simultaneous scalp EEG and ECoG to show that realistic FEM and co-registered MRI/CT can preserve major cortical potential patterns, and <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019)</a> showed that subcortical electrophysiological activity can be conditionally detectable with high-density EEG source imaging. But these are <strong>coverage-limited</strong> gains. On this site, simultaneous invasive routes are treated as <strong>calibration / validation routes for the recorded territory and source regime</strong>, not as whole-brain gold standards.
</p>

<h3>7. OPM-MEG expands movement tolerance, but not without field-control and source-model audits</h3>
<p>
Wearable OPM-MEG is a real advance because the sensors move with the head and therefore support paradigms that fixed SQUID helmets do not. <a href="https://doi.org/10.1038/nature26147" target="_blank">Boto et al. (2018)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">Seymour et al. (2021)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">Holmes et al. (2023a)</a>, and <a href="https://doi.org/10.3390/s23125454" target="_blank">Holmes et al. (2023b)</a> show increasingly naturalistic use cases. But the common lesson is not "movement solved." It is that <strong>movement becomes measurable when the magnetic environment is controlled tightly enough</strong>.
</p>
<p>
The engineering ceiling still runs through field environment and source modeling. <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">Mellor et al. (2022)</a>, <a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">Rea et al. (2021)</a>, and <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">Holmes et al. (2025)</a> show why background-field control, active compensation, and shielding class still matter. <a href="https://doi.org/10.3390/s22083059" target="_blank">Iivanainen et al. (2022)</a>, <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">Rhodes et al. (2025)</a>, and <a href="https://doi.org/10.1063/5.0273491" target="_blank">Wu et al. (2025)</a> show why calibration, anatomy route, and crosstalk remain live burdens. On this site, wearable OPM-MEG therefore remains <strong>movement-tolerant macro electrophysiology under disclosed field control and source-model assumptions</strong>, not unconstrained real-world brain readout.
</p>

<strong>Do not read "wearable" as shield-free, calibration-free, or state-complete</strong>
<p>
Even when OPM-MEG looks much closer to daily behavior, the public claim still has to name <strong>shielding class</strong>, <strong>field-nulling / interference-suppression method</strong>, <strong>motion-tracking route</strong>, <strong>sensor calibration path</strong>, <strong>anatomy route</strong>, and <strong>where abstention begins</strong>. If those are missing, this site keeps the result at the feasibility or proof-of-concept ceiling.
</p>

<h2>Reading rules adopted on this site</h2>

<h4>Rules</h4>
<ul>
<li><strong>multimodal:</strong> Read it as "which audit gates were passed" rather than "multiple modalities were added."</li>
<li><strong>same-session / atlas-informed:</strong> Do not read it as one validated biological state variable unless a <a href="https://mind-upload.com/verification.html#fusion-card">Fusion Card</a> discloses acquisition relation, lag audit, temporal-kernel relation, co-registration scope, shared-vs-specific logic, unimodal / prior-only baselines, availability slice, and external calibration.</li>
<li><strong>shared factor:</strong> Do not read it as automatic target specificity. Label it as shared neural candidate, physiology-linked common driver, modality-specific residual, or unresolved.</li>
<li><strong>quantity bridge:</strong> Do not infer one from covariance alone. Name the biological axis and the physiology-grounding rule explicitly.</li>
<li><strong>multimodal gain:</strong> Do not read "more modalities improved performance" as robustness unless missing-modality handling, transfer, and hard-subgroup disagreement are also disclosed.</li>
<li><strong>EEG + fMRI / fNIRS:</strong> Hemodynamic amplitude remains a transfer-limited quantity until vascular-state / CVR or superficial-signal burdens are audited.</li>
<li><strong>EEG + invasive recording:</strong> Treat it as coverage-limited calibration or validation, not whole-brain truth.</li>
<li><strong>OPM-MEG:</strong> Wearable and motion-tolerant does not waive shielding, field control, calibration, anatomy, or crosstalk audits.</li>
<li><strong>state coverage:</strong> If synaptic, glial, transcriptional, or maintenance-support variables remain unobserved, they stay marked as unobserved even after fusion.</li>
</ul>

<h2>References</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C., Garrido, M. I., Gramfort, A., et al. (2020). Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>, 23, 1473-1483. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., Medine, D., Boulay, C., Grivich, M. I., Artoni, F., Mullen, T., Delorme, A., &amp; Makeig, S. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Wei, H., Jafarian, A., Zeidman, P., Litvak, V., Razi, A., Garrido, M., Friston, K., &amp; Daunizeau, J. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <em>NeuroImage</em>, 211, 116595. <a href="https://doi.org/10.1016/j.neuroimage.2020.116595" target="_blank">doi:10.1016/j.neuroimage.2020.116595</a></li>
<li>Nguyen, T., Potter, T., Nguyen, T., Karmonik, C., Grossman, R., &amp; Zhang, Y. (2016). EEG source imaging guided by spatiotemporal specific fMRI: toward an understanding of dynamic cognitive processes. <em>Neural Plasticity</em>, 2016, 4182483. <a href="https://doi.org/10.1155/2016/4182483" target="_blank">doi:10.1155/2016/4182483</a></li>
<li>Ripp, I., Wallenwein, L. A., Wu, Q., Emch, M., Koch, K., Cumming, P., &amp; Yakushev, I. (2021). Working memory task induced neural activation: a simultaneous PET/fMRI study. <em>NeuroImage</em>, 237, 118131. <a href="https://doi.org/10.1016/j.neuroimage.2021.118131" target="_blank">doi:10.1016/j.neuroimage.2021.118131</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., O'Connor, D., Markicevic, M., Shen, X., Ge, X., Herman, P., Hyder, F., Papademetris, X., Chakravarty, M., Crair, M. C., Constable, R. T., Lake, E. M. R., &amp; Pessoa, L. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>, 15, 229. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., Catana, C., Polimeni, J. R., Fan, J., Droppa, K. S., Patel, R., Wey, H.-Y., Chang, C., Manoach, D. S., Price, J. C., Sander, C. Y., &amp; Rosen, B. R. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>, 16, 8887. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T. S., van den Brink, R. L., Song, C., et al. (2025). Autonomic physiological coupling of the global fMRI signal. <em>Nature Neuroscience</em>, 28, 1266-1278. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Özbay, P. S., Chang, C., Picchioni, D., et al. (2019). Sympathetic activity contributes to the fMRI signal. <em>Communications Biology</em>, 2, 421. <a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Rohaut, B., Calligaris, C., Hermann, B., et al. (2024). Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. <em>Nature Medicine</em>, 30, 2349-2355. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Amiri, M., Andelic, N., Westhall, E., et al. (2023). Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. <em>Brain</em>, 146(1), 50-69. <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/brain/awac335</a></li>
<li>Manasova, D., Hermann, B., Calligaris, C., et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <em>Brain</em>. <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/brain/awaf412</a></li>
<li>Jorge, J., Grouiller, F., Ipek, O., et al. (2015). Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. <em>NeuroImage</em>, 105, 132-144. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Jorge, J., Grouiller, F., Gruetter, R., et al. (2015). Towards high-quality simultaneous EEG-fMRI at 7 T: detection and reduction of EEG artifacts due to head motion. <em>NeuroImage</em>, 120, 143-153. <a href="https://doi.org/10.1016/j.neuroimage.2015.07.020" target="_blank">doi:10.1016/j.neuroimage.2015.07.020</a></li>
<li>Wirsich, J., Jorge, J., Iannotti, G. R., et al. (2021). The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. <em>NeuroImage</em>, 231, 117864. <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">doi:10.1016/j.neuroimage.2021.117864</a></li>
<li>Murphy, K., Harris, A. D., &amp; Wise, R. G. (2011). Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. <em>NeuroImage</em>, 54(1), 369-379. <a href="https://doi.org/10.1016/j.neuroimage.2010.07.059" target="_blank">doi:10.1016/j.neuroimage.2010.07.059</a></li>
<li>Williams, R. J., Specht, J. L., Mazerolle, E. L., Lebel, R. M., MacDonald, M. E., &amp; Pike, G. B. (2023). Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. <em>Frontiers in Physiology</em>, 14, 1167148. <a href="https://doi.org/10.3389/fphys.2023.1167148" target="_blank">doi:10.3389/fphys.2023.1167148</a></li>
<li>Wu, S., Tyler, L. K., Henson, R. N. A., Rowe, J. B., Cam-CAN, &amp; Tsvetanov, K. A. (2023). Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. <em>Neurobiology of Aging</em>, 121, 1-14. <a href="https://doi.org/10.1016/j.neurobiolaging.2022.09.006" target="_blank">doi:10.1016/j.neurobiolaging.2022.09.006</a></li>
<li>Yucel, M. A. Y., Selb, J., Aasted, C. M. A., Petkov, M. P., Becerra, L., Borsook, D., &amp; Boas, D. A. (2015). Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. <em>Neurophotonics</em>, 2(3), 035005. <a href="https://doi.org/10.1117/1.NPh.2.3.035005" target="_blank">doi:10.1117/1.NPh.2.3.035005</a></li>
<li>An, J., Goyal, P., Luft, A. R., &amp; Schönhammer, J. G. (2025). Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load. <em>Neurophotonics</em>, 12(3), 035009. <a href="https://doi.org/10.1117/1.NPh.12.3.035009" target="_blank">doi:10.1117/1.NPh.12.3.035009</a></li>
<li>Epp, S. M., Castrillón, G., Yuan, B., Andrews-Hanna, J., Preibisch, C., &amp; Riedl, V. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2014). Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. <em>PLoS ONE</em>, 9(3), e93154. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Zhang, Y., Ding, L., van Drongelen, W., et al. (2006). A cortical potential imaging study from simultaneous extra- and intracranial electrical recordings by means of the finite element method. <em>NeuroImage</em>, 31(4), 1517-1528. <a href="https://doi.org/10.1016/j.neuroimage.2006.02.027" target="_blank">doi:10.1016/j.neuroimage.2006.02.027</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657-661. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
<li>Seymour, R. A., Alexander, N., Mellor, S., O'Neill, G. C., Tierney, T. M., Barnes, G. R., &amp; Maguire, E. A. (2021). Using OPMs to measure neural activity in standing, mobile participants. <em>NeuroImage</em>, 244, 118604. <a href="https://doi.org/10.1016/j.neuroimage.2021.118604" target="_blank">doi:10.1016/j.neuroimage.2021.118604</a></li>
<li>Mellor, S. J., Tierney, T. M., O'Neill, G. C., Alexander, N., Seymour, R. A., Holmes, N., Lopez, J. D., Hill, R. M., Boto, E., Rea, M., Roberts, G., Leggett, J., Bowtell, R., Brookes, M. J., Maguire, E. A., Walker, M. C., &amp; Barnes, G. R. (2022). Magnetic field mapping and correction for moving OP-MEG. <em>IEEE Transactions on Biomedical Engineering</em>, 69(2), 528-536. <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">doi:10.1109/TBME.2021.3100770</a></li>
<li>Rea, M., Holmes, N., Hill, R. M., Boto, E., Leggett, J., Edwards, L. J., Woolger, D., Dawson, E., Shah, V., Osborne, J., Bowtell, R., &amp; Brookes, M. J. (2021). Precision magnetic field modelling and control for wearable magnetoencephalography. <em>NeuroImage</em>, 241, 118401. <a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">doi:10.1016/j.neuroimage.2021.118401</a></li>
<li>Holmes, N., Rea, M., Hill, R. M., Leggett, J., Edwards, L. J., Hobson, P. J., Boto, E., Tierney, T. M., Rier, L., Reina Rivero, G., Shah, V., Osborne, J., Fromhold, T. M., Glover, P., Brookes, M. J., &amp; Bowtell, R. (2023). Enabling ambulatory movement in wearable magnetoencephalography with matrix coil active magnetic shielding. <em>NeuroImage</em>, 274, 120157. <a href="https://doi.org/10.1016/j.neuroimage.2023.120157" target="_blank">doi:10.1016/j.neuroimage.2023.120157</a></li>
<li>Holmes, N., Rea, M., Hill, R. M., Boto, E., Leggett, J., Edwards, L. J., Rhodes, N., Shah, V., Osborne, J., Fromhold, T. M., Glover, P., Montague, P. R., Brookes, M. J., &amp; Bowtell, R. (2023). Naturalistic hyperscanning with wearable magnetoencephalography. <em>Sensors</em>, 23(12), 5454. <a href="https://doi.org/10.3390/s23125454" target="_blank">doi:10.3390/s23125454</a></li>
<li>Holmes, N., Leggett, J., Hill, R. M., Rier, L., Boto, E., Schofield, H., Hayward, T., Dawson, E., Woolger, D., Shah, V., Taulu, S., Brookes, M. J., &amp; Bowtell, R. (2025). Wearable magnetoencephalography in a lightly shielded environment. <em>IEEE Transactions on Biomedical Engineering</em>, 72(2), 609-618. <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">doi:10.1109/TBME.2024.3465654</a></li>
<li>Iivanainen, J., Borna, A., Zetter, R., Carter, T. R., Stephen, J. M., McKay, J., Parkkonen, L., Taulu, S., &amp; Schwindt, P. D. D. (2022). Calibration and localization of optically pumped magnetometers using electromagnetic coils. <em>Sensors</em>, 22(8), 3059. <a href="https://doi.org/10.3390/s22083059" target="_blank">doi:10.3390/s22083059</a></li>
<li>Rhodes, N., Rier, L., Boto, E., Hill, R. M., &amp; Brookes, M. J. (2025). Source reconstruction without an MRI using optically pumped magnetometer-based magnetoencephalography. <em>Imaging Neuroscience</em>, 3, IMAG.a.8. <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">doi:10.1162/IMAG.a.8</a></li>
<li>Wu, T., Xiao, W., Peng, X., Wu, T., &amp; Guo, H. (2025). Crosstalk reduction in optically pumped magnetometers arrays for biomagnetic measurement. <em>Review of Scientific Instruments</em>, 96(8), 085004. <a href="https://doi.org/10.1063/5.0273491" target="_blank">doi:10.1063/5.0273491</a></li>
</ol>
