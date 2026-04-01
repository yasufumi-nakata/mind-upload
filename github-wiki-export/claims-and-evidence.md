# Wiki: How to read claims and evidence

> Strong language is cheap. Strong evidence is not.
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-04-01 / Role: Reading guide

## Role Of This Page
This page turns flashy neuroscience and WBE wording back into claim strength, evidence class, and the minimum route cards needed before the claim can be read strongly. The goal is not to dampen progress, but to stop score inflation and evidence-class collapse at the entrance.

## Accuracy Notes
This page stays on the technology and natural-science side. It does not treat a headline, a high score, or one modeling framework as a substitute for disclosed measurement conditions, external validation, or abstention.

## Back To Public Pages
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [FAQ](https://mind-upload.com/faq.html)

## Related Wiki Pages
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - Sets the overall technical picture before claim reading.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Explains why route cards, audits, and preregistration matter operationally.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Explains why ESI, DCM, and SCM do not all support the same kind of claim.
- [Wiki: Measurement-stack observability and claim ceilings](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling) - Shows what each modality directly observes and where the claim ceiling appears.

## What Is Currently Known
- Reproducible analysis, decoding, intervention prediction, and identity claims require different evidence floors.
- The same score can arise from different causal stories, so direct observables and shortcut routes must be separated.
- Same-subject or same-session human proxy bundles can still leave quantity-type mismatch, cohort-regime mismatch, and common-driver ambiguity unresolved.
- Recent primary literature supports stricter beginner reading rules for decode, human proxy composition, tractography, effective connectivity, thermodynamic claims, and closed loops.

## What Is Still Unknown
- It remains unsettled which measurement stack would be sufficient for WBE-level internal-state capture.
- It remains unresolved how far any future L4 continuity test would justify identity claims.

---

<h2>Basic rule</h2>
<p>
When a neuroscience or WBE headline sounds strong, do not ask first whether it sounds impressive. Ask <strong>what was directly observed</strong>, <strong>what was only inferred through a model or prior</strong>, and <strong>what the result still does not identify</strong>. This page is the shortest beginner route for doing that.
</p>

<strong>2026-03-26 deepening: why this beginner page needed another rewrite</strong>
<p>
The 2026-03-19 rewrite fixed several major overreads, but one important beginner shortcut still remained: it was still too easy to read <strong>same-subject multimodal</strong> or <strong>living-human whole-brain measurement</strong> as if they already meant near-complete state access. The recent public updates across this site now require a <strong>Human Proxy Composition Card</strong> and a <strong>Fusion Card</strong> in addition to route cards for tractography, effective connectivity, thermodynamic irreversibility, neural contribution, and body/environment boundary. This page now exposes that human-proxy distinction at the entrance instead of leaving it to later technical pages.
</p>

<strong>2026-03-29 deepening: a causal-graph headline still needs closure and sampling audits</strong>
<p>
This page also had one remaining effective-connectivity shortcut. It still sounded too easy to read <strong>"found causal wiring"</strong> as if candidate-model comparison already covered the main failure modes. The current literature does not support that. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a> showed that lag-based fMRI methods perform poorly and that <strong>functionally inaccurate ROIs</strong> are especially damaging to network estimation. <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">Barnett &amp; Seth (2017)</a> showed that subsampling can create <strong>detectability black spots</strong>. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">Vink et al. (2020)</a> showed that resting-state EEG functional connectivity explains <strong>less than 10%</strong> of TMS-evoked propagation variance. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde et al. (2019)</a> showed why observability of states, inputs, and parameters is its own problem, <a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025)</a> showed that <strong>slow BOLD sampling</strong> can still induce spurious Granger-causal inference, <a href="https://doi.org/10.1002/hbm.26782" target="_blank">Jafarian et al. (2024)</a> showed that reliability itself is conditional on a tight acquisition regime, and <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">Yan et al. (2026)</a> showed that latent confounders remain an active reconstruction problem. Therefore, on this site, a causal-graph headline still has to disclose <strong>observed-subsystem closure / latent-confound audit</strong>, <strong>node-definition policy</strong>, <strong>sampling / transformation sensitivity</strong>, <strong>validation</strong>, <strong>reliability window</strong>, and <strong>abstention</strong> before it rises above a model-conditioned causal hypothesis.
</p>

<h2>Rephrasing L0-L5 in everyday language, without losing the technical floor</h2>
<table>
<thead>
<tr>
<th>Level</th>
<th>Safe everyday reading</th>
<th>Minimum evidence floor</th>
<th>Fastest overread to block</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>Someone else can rerun the same result.</td>
<td>Public data or artifact pack, code, environment, split rules, and logs are complete enough for third-party rerun.</td>
<td>Do not read <strong>rerunnable</strong> as <strong>generalizable</strong>.</td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>A signal can be decoded or classified under stated conditions.</td>
<td>Participant-/session-disjoint evaluation, measurement-condition disclosure, relevant baselines, shortcut audit, and abstention when confidence collapses.</td>
<td>Do not read <strong>high score</strong> as <strong>target-specific neural evidence</strong> or <strong>correct internal mechanism</strong>.</td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>The model still predicts or controls something after conditions are changed.</td>
<td>Held-out perturbation or counterfactual evaluation, preregistered success/failure rules, and evidence that the effect survives beyond a fixed dataset regime.</td>
<td>Do not read <strong>fit on observed data</strong> as <strong>causal robustness</strong>.</td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>A closed loop runs stably under a disclosed boundary.</td>
<td>Latency/jitter/safe-stop logs, recalibration burden, and a body/environment boundary card naming preserved, substituted, and omitted sensory, motor, and interoceptive loops.</td>
<td>Do not read <strong>real-time demo</strong> as <strong>solved embodiment</strong> or <strong>state-complete closed loop</strong>.</td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>Continuity or identity is being tested explicitly.</td>
<td>Pre-registered continuity tests, branch handling, memory/value/learning criteria, and explicit alternative explanations.</td>
<td>Do not read <strong>functional similarity</strong> as <strong>identity preserved</strong>.</td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>A system is being considered for durable operation in the world.</td>
<td>Operational, safety, and governance conditions must exist in public form.</td>
<td>Do not read <strong>works in a lab</strong> as <strong>ready for deployment</strong>.</td>
</tr>
</tbody>
</table>

<h2>Translating common headline phrases into safer first readings</h2>
<table>
<thead>
<tr>
<th>Headline-style phrase</th>
<th>Safest default reading</th>
<th>What you must ask before reading stronger</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>"Recovered sentences from the brain"</strong></td>
<td>Usually an L1 decode or assistive BCI result under task- and participant-specific conditions.</td>
<td>What were the task constraint, language prior, candidate set, subject cooperation requirement, calibration burden, and no-brain / no-LM / shuffle baselines?</td>
</tr>
<tr>
<td><strong>"Found a biomarker with 95% accuracy"</strong></td>
<td>Usually an L1 classifier under a specific acquisition and split regime.</td>
<td>Were subjects and sessions disjoint, could metadata or subject fingerprint explain the score, and was performance checked across sites/devices/datasets?</td>
</tr>
<tr>
<td><strong>"Measured the whole-brain state in living humans"</strong></td>
<td>Usually a proxy-rich human or simultaneous multimodal result that constrains several bounded quantities under specific cohort, hardware, and model burdens.</td>
<td>What did each row directly observe, were rows actually same-subject / same-session / same-perturbation, did shared-vs-specific decomposition and common-driver audit survive, and what calibrator role plus residual hidden-state ceiling remained?</td>
</tr>
<tr>
<td><strong>"Mapped the connectome in living humans"</strong></td>
<td>Usually a tractography-conditioned macro pathway estimate, not an edge-complete connectome.</td>
<td>What were the direct observables, tractography priors/filtering choices, uncertainty handling, and same-brain or external validation route?</td>
</tr>
<tr>
<td><strong>"Found causal wiring / effective connectivity"</strong></td>
<td>Usually a model-conditioned causal hypothesis.</td>
<td>What candidate model space competed, how was the observed subsystem or latent-confound boundary audited, how were nodes defined, what observation and sampling assumptions were imposed, how was model recovery checked, and what validation or reliability window exists?</td>
</tr>
<tr>
<td><strong>"Measured entropy production / irreversibility in brain data"</strong></td>
<td>Usually a modality- and estimator-conditioned auxiliary nonequilibrium analysis.</td>
<td>What were the signal route, coarse-graining, estimator family, null control, quantity type, and abstention boundary?</td>
</tr>
<tr>
<td><strong>"Ran a stable real-time closed loop"</strong></td>
<td>Usually a local closed-loop success under a specific sensory/motor contract.</td>
<td>Which loops were preserved, which were substituted, what recalibration was needed, and which body/environment channels remained omitted?</td>
</tr>
</tbody>
</table>

<h2>Why the beginner rules had to become stricter</h2>

<strong>1. High accuracy does not become target-specific evidence by default</strong>
<p>
This is the first place beginners are most often misled. <a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">Chaibub Neto et al. (2019)</a> showed that record-wise splits can inflate performance because the model learns who the participant is, not only the target label. <a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">Di et al. (2021)</a> showed that resting-state EEG can support time-robust individual identification. <a href="https://www.frontiersin.org/articles/10.3389/fnhum.2020.00103/full" target="_blank">Xu et al. (2020)</a> showed that cross-dataset variability weakens EEG-decoding generalization. Meanwhile, <a href="https://www.nature.com/articles/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a> showed that non-invasive semantic reconstruction requires subject cooperation, and <a href="https://www.nature.com/articles/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a> achieved strong speech-BCI performance under implanted, participant-specific conditions. Therefore, on this site, a decode headline is not read strongly until split unit, measurement condition, task/language prior, and shortcut routes are disclosed.
</p>

<strong>2. Proxy-rich human multimodal evidence does not automatically become same-subject state closure</strong>
<p>
The beginner route also needed tightening because current human proxy papers are easy to list rhetorically as if they were already converging on one state-complete meter. The primary literature does not support that shortcut. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> provided a 33-participant SV2A atlas, <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> defined a five-metabolite parcel-similarity graph in 51 adolescents with 13-person replication, <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> reported 7 T dynamic DMRSI kinetic maps in five healthy participants, <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> reported a specialized 7 T CSF-mobility route in healthy younger adults whose sequence does not determine net-flow direction, and <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> inferred model-based overnight biomarker efflux in a randomized crossover trial with 39 participants using an investigational device and a multicompartment model. These are real advances, but they are not one shared inferential object. In parallel, <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a> showed both common and divergent structure across simultaneous modalities, <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a> showed coupled global progression plus two distinct network patterns in simultaneous EEG-PET-MRI, <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">Bolt et al. (2025)</a> showed substantial autonomic coupling of a major global fMRI mode, and <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> showed that approximately 40% of significant cortical ΔBOLD voxels can oppose oxygen-metabolism changes. Therefore, on this site, <strong>same-subject</strong>, <strong>multimodal</strong>, and <strong>proxy-rich</strong> do not by themselves justify whole-brain state language. They instead trigger proxy-class, calibrator-role, and common-driver audits.
</p>

<strong>3. "Connectome" still names different evidence classes</strong>
<p>
The beginner route also needed tightening because the word <strong>connectome</strong> hides a large spread in evidence class. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">Thomas et al. (2014)</a> showed inherent limits in anatomical accuracy for diffusion-MRI tractography, <a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">Maier-Hein et al. (2017)</a> exposed fundamental ambiguities and many invalid bundles in a community challenge, <a href="https://pubmed.ncbi.nlm.nih.gov/32816112/" target="_blank">Schilling et al. (2020)</a> showed that high anatomical accuracy depends on strong start/end/exclusion priors, and <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8475636/" target="_blank">Grisot et al. (2021)</a> localized recurring failure modes in the same brain. Therefore, a living-human tractography graph is not read here as connectome-complete by default. It stays at <strong>macro pathway prior</strong> unless the tractography route card is shown.
</p>

<strong>4. Model-conditioned graphs are not discovered causal wiring</strong>
<p>
For effective connectivity, the problem is not that DCM or related models are useless. The problem is overreading them. <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">Penny et al. (2004)</a> made explicit that DCM inferences are contingent on model structure, and <a href="https://pubmed.ncbi.nlm.nih.gov/22561579/" target="_blank">Rosa et al. (2012)</a> showed that larger candidate spaces can be searched more efficiently. But that is still not enough to read a directed graph as discovered causal wiring. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">Smith et al. (2011)</a> showed that lag-based fMRI methods perform poorly and that <strong>functionally inaccurate ROIs</strong> are especially damaging to network estimation. <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">Barnett &amp; Seth (2017)</a> showed that subsampling can create <strong>detectability black spots</strong> and <strong>sweet spots</strong>. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">Vink et al. (2020)</a> showed that resting-state EEG functional connectivity explains <strong>less than 10%</strong> of TMS-evoked propagation variance. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">Villaverde et al. (2019)</a> showed why <strong>observability</strong> of the full input-state-parameter system is its own question. <a href="https://doi.org/10.1002/hbm.70285" target="_blank">Novelli et al. (2025)</a> showed that realistic HRF variability alone need not force false positives while <strong>slow BOLD sampling</strong> can still induce spurious Granger-causal inference. <a href="https://doi.org/10.1002/hbm.26782" target="_blank">Jafarian et al. (2024)</a> showed that reliability can be high under tightly matched MEG sessions, and <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">Yan et al. (2026)</a> showed that latent confounders remain an active reconstruction problem. Therefore, on this site, a dense effective-connectivity graph without <strong>model-space disclosure</strong>, <strong>observed-subsystem closure / latent-confound audit</strong>, <strong>node-definition policy</strong>, <strong>sampling / transformation sensitivity</strong>, <strong>recovery</strong>, <strong>validation</strong>, <strong>reliability window</strong>, and <strong>abstention</strong> remains a <strong>model-conditioned causal hypothesis</strong>.
</p>

<strong>5. Thermodynamic keywords still hide different measured objects</strong>
<p>
The older beginner wording was also too weak for thermodynamic claims. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">Lynn et al. (2021)</a> estimated entropy-production lower bounds from coarse-grained BOLD state transitions, <a href="https://academic.oup.com/cercor/article/33/5/1856/6577164" target="_blank">de la Fuente et al. (2023)</a> used temporal irreversibility decoding on ECoG, and <a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">Ishihara &amp; Shimazaki (2025)</a> estimated model-based entropy flow in a nonstationary state-space kinetic Ising model. Those are related, but not identical, objects. Therefore this site no longer allows the beginner reading that <strong>"thermodynamic paper"</strong> automatically means a common measurement of physical dissipation or WBE-relevant cost.
</p>

<strong>6. Real-time loop success still needs a disclosed body/environment boundary</strong>
<p>
Finally, closed-loop headlines needed a stricter beginner rule. <a href="https://pubmed.ncbi.nlm.nih.gov/31551604/" target="_blank">Musall et al. (2019)</a> showed that richly varied movements dominate cortex-wide activity, <a href="https://www.nature.com/articles/nn.3567" target="_blank">Saleem et al. (2013)</a> showed that locomotion changes visual-cortex coding, and <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">Flesher et al. (2021)</a> showed that restoring tactile feedback improves robotic-arm control. The safe reading is therefore not <strong>"closed loop solved"</strong> but <strong>"a specific local loop worked under a specific retained/substituted boundary."</strong>
</p>

<h2>Seven questions before you believe the strong version of a headline</h2>

<h4>Checklist</h4>
<ul>
<li><strong>What was directly observed?</strong> Separate sensor output from inferred internal state.</li>
<li><strong>What model space or prior was imposed?</strong> Candidate models, language priors, tractography filters, and neural-mass assumptions all matter.</li>
<li><strong>Which shortcut could reproduce the score?</strong> Subject/session fingerprint, metadata leakage, device differences, and candidate-set structure must be checked explicitly.</li>
<li><strong>If this is a human or multimodal bundle, what does each row directly observe?</strong> Proxy class, operational maturity, calibrator role, and possible common-driver routes must be named separately.</li>
<li><strong>What external or held-out validation exists?</strong> Same-dataset fit is weaker than perturbation, stimulation, same-brain tracing, or external benchmark prediction.</li>
<li><strong>What loops or state variables remain outside the measurement?</strong> Boundary and hidden-state omissions still set the claim ceiling.</li>
<li><strong>Where does the paper abstain?</strong> A strong paper says which interpretations it does <em>not</em> support.</li>
</ul>

<h2>Where to go next after this beginner page</h2>
<table>
<thead>
<tr>
<th>If the headline is mostly about...</th>
<th>Read this next</th>
<th>Why</th>
</tr>
</thead>
<tbody>
<tr>
<td>Decode / biomarker / speech / EEG score</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling">Measurement-stack observability and claim ceilings</a></td>
<td>It fixes what was directly observed and which shortcut routes remain open.</td>
</tr>
<tr>
<td>Living-human multimodal / proxy-rich whole-brain claim</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition">Human Proxy Composition and Route Maturity</a></td>
<td>It separates direct observable by row, proxy class, calibrator role, and common-driver audit before same-subject language is allowed.</td>
</tr>
<tr>
<td>Connectome / tractography / structural prior</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/connectome-is-not-enough">Why wiring diagrams alone are not enough</a></td>
<td>It separates scaffold progress from hidden-state completeness.</td>
</tr>
<tr>
<td>DCM / effective connectivity / causal graph</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation#effective-connectivity-route-card">Effective-connectivity route card</a></td>
<td>It shows why candidate-model dependence is only the start, and why closure, node definition, sampling, and validation still have to be disclosed.</td>
</tr>
<tr>
<td>Entropy production / irreversibility / time arrow</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/thermodynamic-grounding-basics#irreversibility-route-card">Irreversibility route card</a></td>
<td>It separates estimator families and null controls.</td>
</tr>
<tr>
<td>Closed loop / BCI / embodiment</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">Closed loops, latency, jitter, and safety stops</a></td>
<td>It explains why latency logs and boundary disclosure are separate requirements.</td>
</tr>
</tbody>
</table>

<h2>References</h2>
<ol>
<li>Chaibub Neto, E., Pratap, A., Perumal, T. M., et al. (2019). Detecting the impact of subject characteristics on machine learning-based diagnostic applications. <em>npj Digital Medicine</em>, 2, 99. <a href="https://www.nature.com/articles/s41746-019-0178-x" target="_blank">doi:10.1038/s41746-019-0178-x</a></li>
<li>Xu, M., Yao, S., Wei, Z., et al. (2020). Cross-dataset variability problem in EEG decoding with deep learning. <em>Frontiers in Human Neuroscience</em>, 14, 103. <a href="https://www.frontiersin.org/articles/10.3389/fnhum.2020.00103/full" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Di, Y., An, X., Zhong, W., Liu, S., &amp; Ming, D. (2021). The time-robustness analysis of individual identification based on resting-state EEG. <em>Frontiers in Human Neuroscience</em>, 15, 672946. <a href="https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.672946/full" target="_blank">doi:10.3389/fnhum.2021.672946</a></li>
<li>Tang, J., LeBel, A., Jain, S., &amp; Huth, A. G. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. <em>Nature Neuroscience</em>, 26, 858-866. <a href="https://www.nature.com/articles/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <em>Nature</em>, 620, 1031-1036. <a href="https://www.nature.com/articles/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Johansen, A., Bzdok, D., Veronese, M., et al. (2024). An in vivo high-resolution human brain atlas of synaptic density. <em>Journal of Neuroscience</em>. <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1750-23.2024</a></li>
<li>Vafaii, H., Mandino, F., Desrosiers-Grégoire, G., et al. (2024). Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Li, X., Zhu, X.-H., Li, Y., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. <em>PNAS Nexus</em>. <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>Hirschler, L., Runderkamp, B. A. R., Decker, A., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Chen, J. E., Lewis, L. D., Coursey, S. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T., Wang, S., Nomi, J. S., et al. (2025). Autonomic physiological coupling of the global fMRI signal. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Epp, S. M., Castrillon, G., Yuan, B., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Dagum, P., Elbert, D. L., Giovangrandi, L., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. <em>Nature Communications</em>. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Thomas, C., Ye, F. Q., Irfanoglu, M. O., et al. (2014). Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. <em>PNAS</em>, 111(46), 16574-16579. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4246325/" target="_blank">doi:10.1073/pnas.1405672111</a></li>
<li>Maier-Hein, K. H., Neher, P. F., Houde, J.-C., et al. (2017). The challenge of mapping the human connectome based on diffusion tractography. <em>Nature Communications</em>, 8, 1349. <a href="https://www.nature.com/articles/s41467-017-01285-x" target="_blank">doi:10.1038/s41467-017-01285-x</a></li>
<li>Schilling, K. G., Petit, L., Rheault, F., et al. (2020). Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. <em>Brain Structure and Function</em>, 225, 2387-2402. <a href="https://pubmed.ncbi.nlm.nih.gov/32816112/" target="_blank">doi:10.1007/s00429-020-02129-z</a></li>
<li>Grisot, G., Haber, S. N., Hawrylycz, M., Yendiki, A., et al. (2021). Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. <em>NeuroImage</em>, 239, 118300. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8475636/" target="_blank">doi:10.1016/j.neuroimage.2021.118300</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://www.sciencedirect.com/science/article/abs/pii/S1053811904001648" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa, M. J., Friston, K., &amp; Penny, W. (2012). Post-hoc selection of dynamic causal models. <em>Journal of Neuroscience Methods</em>, 208(1), 66-78. <a href="https://pubmed.ncbi.nlm.nih.gov/22561579/" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Frässle, S., Paulus, F. M., Krach, S., &amp; Jansen, A. (2016). Test-retest reliability of effective connectivity in the face perception network. <em>Human Brain Mapping</em>, 37(2), 730-744. <a href="https://pubmed.ncbi.nlm.nih.gov/26611397/" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle, S., Manjaly, Z. M., Do, C. T., et al. (2021). Whole-brain estimates of directed connectivity for human connectomics. <em>NeuroImage</em>, 225, 117491. <a href="https://pubmed.ncbi.nlm.nih.gov/33115664/" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Smith, S. M., Miller, K. L., Salimi-Khorshidi, G., Webster, M., Beckmann, C. F., Nichols, T. E., Ramsey, J. D., &amp; Woolrich, M. W. (2011). Network modelling methods for FMRI. <em>NeuroImage</em>, 54(2), 875-891. <a href="https://doi.org/10.1016/j.neuroimage.2010.08.063" target="_blank">doi:10.1016/j.neuroimage.2010.08.063</a></li>
<li>Barnett, L., &amp; Seth, A. K. (2017). Detectability of Granger causality for subsampled continuous-time neurophysiological processes. <em>Journal of Neuroscience Methods</em>, 275, 93-121. <a href="https://doi.org/10.1016/j.jneumeth.2016.10.016" target="_blank">doi:10.1016/j.jneumeth.2016.10.016</a></li>
<li>Villaverde, A. F., Tsiantis, N., &amp; Banga, J. R. (2019). Full observability and estimation of unknown inputs, states and parameters of nonlinear biological models. <em>Journal of the Royal Society Interface</em>, 16(156), 20190043. <a href="https://doi.org/10.1098/rsif.2019.0043" target="_blank">doi:10.1098/rsif.2019.0043</a></li>
<li>Vink, J. J. T., Klooster, D. C. W., Ozdemir, R. A., Westover, M. B., Pascual-Leone, A., &amp; Shafi, M. M. (2020). EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. <em>Brain Topography</em>, 33(2), 221-237. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>Jafarian, A., Karadag Assem, M., Kocagoncu, E., et al. (2024). Reliability of dynamic causal modelling of resting-state magnetoencephalography. <em>Human Brain Mapping</em>, 45(10), e26782. <a href="https://doi.org/10.1002/hbm.26782" target="_blank">doi:10.1002/hbm.26782</a></li>
<li>Novelli, L., Barnett, L., Seth, A. K., &amp; Razi, A. (2025). Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. <em>Human Brain Mapping</em>, 46(10), e70285. <a href="https://doi.org/10.1002/hbm.70285" target="_blank">doi:10.1002/hbm.70285</a></li>
<li>Yan, J., Zhang, S.-W., Zhang, C., Huang, W., Shi, J., &amp; Chen, L. (2026). Dynamical Causality under Latent Confounders for Biological Network Reconstruction. <em>IEEE Transactions on Pattern Analysis and Machine Intelligence</em>. <a href="https://doi.org/10.1109/TPAMI.2026.3658839" target="_blank">doi:10.1109/TPAMI.2026.3658839</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., et al. (2021). Broken detailed balance and entropy production in the human brain. <em>PNAS</em>, 118(47), e2109889118. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8617485/" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>de la Fuente, L. A., Zamberlan, F., Bocaccio, H., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <em>Cerebral Cortex</em>, 33(5), 1856-1865. <a href="https://academic.oup.com/cercor/article/33/5/1856/6577164" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <em>Nature Communications</em>, 16, 10852. <a href="https://www.nature.com/articles/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <em>Nature Neuroscience</em>, 22, 1677-1686. <a href="https://www.nature.com/articles/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Saleem, A. B., Ayaz, A., Jeffery, K. J., Harris, K. D., &amp; Carandini, M. (2013). Integration of visual motion and locomotion in mouse visual cortex. <em>Nature Neuroscience</em>, 16, 1864-1869. <a href="https://www.nature.com/articles/nn.3567" target="_blank">doi:10.1038/nn.3567</a></li>
<li>Flesher, S. N., Downey, J. E., Weiss, J. M., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science</em>, 372(6544), 831-836. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8715714/" target="_blank">doi:10.1126/science.abd0380</a></li>
</ol>
