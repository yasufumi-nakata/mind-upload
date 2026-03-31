# Wiki: Verification of counterfactuals, interventions, and perturbations

> A fast loop, a causal gain, and a durable same-state result are different claims.
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-31 / Role: Learning guide / evidence refresh

## Role Of This Page
This page is a wiki that separates held-out accuracy, online human-in-the-loop control, bidirectional or local intervention, state-dependent intervention, temporal durability, and perturbation-structure tests using primary literature. It also connects those evidence classes to the site's newer operating rules: the Temporal Validity Card, Burst-Controller Log, State-Continuity Bridge Card, Maintenance-State Error Budget, and Body / Environment Boundary Card.

## Accuracy Notes
The primary literature as of March 2026 strongly supports local subsystem- and task-limited causal evidence plus real engineering progress in online control and deployment. It still does not demonstrate whole-brain counterfactual equivalence or state-complete WBE, and it also does not support reading burst-driven neuromodulation as one generic controller family.

## Back To Public Pages
- [Verification platform](https://mind-upload.com/verification.html)
- [Technology roadmap](https://mind-upload.com/tech_roadmap.html)
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)

## Related Wiki Pages
- [Wiki: Decode and Emulate](https://github.com/yasufumi-nakata/mind-upload/wiki/decode-vs-emulate) - Return here first if translation and generation are still being mixed together.
- [Wiki: From Observation to Estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - Explains why observational fit and causal validation are different steps.
- [Wiki: State, Trait, and Drift](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - Background for cross-day durability, recalibration burden, and transfer ceilings.
- [Wiki: State-Continuity Bridge](https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge) - Explains why same-subject or same-brain wording does not automatically give one same-state sample.
- [Wiki: Closed Loop, Delay, Jitter, Safe Stop](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - Detailed timing-side companion for online control and deployment logs.

## What Is Currently Known
- High held-out accuracy alone does not guarantee agreement in causal structure.
- Bidirectional feedback and state-dependent stimulation strengthen causal evidence, but their scope of application remains localized unless the omitted boundary is disclosed.
- Recent speech BCI and adaptive DBS papers show that tail latency, recalibration burden, biomarker/controller family, eligibility or programming burden, and clinic-to-home deployment are separate audit items.
- Same-subject or same-brain wording can solve specimen identity while still leaving state continuity unresolved across days, regimes, or live-to-fix bridges.
- When a claim extends to persistence, forgetting, or recovery after perturbation, intervention logs alone are insufficient without maintenance-state disclosure.

## What Is Still Unknown
- It remains open which perturbation set would be sufficient for whole-brain branch-equivalence.
- The extent to which counterfactual branch structure can be benchmarked in a shareable public infrastructure is still unresolved.
- No public benchmark yet joins perturbation response, temporal durability, bridge validity, and maintenance-state disclosure under one whole-brain standard.
- Which biomarker/controller pairing best generalizes across bradykinesia, gait impairment, dyskinesia control, and chronic home use in adaptive DBS remains unresolved.

---

<h2>Shortest conclusion</h2>
<p>
High held-out accuracy is important, but it alone does not mean that the mechanisms inside are the same. The current primary literature supports at least six separate walls: <strong>held-out decode</strong>, <strong>online human-in-the-loop control</strong>, <strong>bidirectional or local intervention</strong>, <strong>state-dependent intervention</strong>, <strong>temporal durability and deployment</strong>, and <strong>branch-structure or perturbation-pattern testing</strong>.
</p>

<strong>Main weakness this pass had to fix</strong>
<p>
The older version correctly separated held-out accuracy from intervention, but it still let readers learn causal verification as if it were one monotonic ladder. The recent primary literature does not support that shortcut. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> demonstrated raw-neural closed-loop voice synthesis in less than <strong>10 ms</strong> with explicit silence outside speech, yet the same paper reported a noticeable decline in fixed-decoder performance after about <strong>15 days</strong>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> then achieved <strong>one month</strong> of unsupervised closed-loop cursor control while showing, with recordings spanning <strong>five years</strong>, that pairwise recalibration and chained long-term use are different questions. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a> pushed adaptive DBS into blinded randomized blocks in home life over <strong>one month per condition</strong>, while <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a> showed that even after offering chronic adaptive DBS to <strong>20 consecutive</strong> Parkinson's disease patients, eligibility and programming constraints still narrowed who could actually continue. A second remaining weakness was subtler: this page still let readers treat adaptive DBS as one generic state-dependent intervention. <a href="https://pubmed.ncbi.nlm.nih.gov/38580641/" target="_blank">Mathiopoulou et al. (2024)</a>, <a href="https://pubmed.ncbi.nlm.nih.gov/39289373/" target="_blank">Stanslaski et al. (2024)</a>, <a href="https://pubmed.ncbi.nlm.nih.gov/41741462/" target="_blank">Cascino et al. (2026)</a>, and the newer biomarker papers cited below show that <strong>biomarker family</strong>, <strong>controller mode</strong>, <strong>state dependence</strong>, <strong>sensing viability</strong>, and <strong>programming burden</strong> are different causal-verification burdens. Therefore this page now separates <strong>same-session causal gain</strong>, <strong>state-dependent controller family</strong>, <strong>temporal durability</strong>, <strong>bridge validity</strong>, and <strong>deployment burden</strong> instead of hiding them inside one phrase such as <strong>closed-loop success</strong>.
</p>

<strong>2026-03-31 deepening: burst-driven neuromodulation is controller-limited, not one state-dependent intervention</strong>
<p>
This page now blocks one more shortcut. <a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">Mathiopoulou et al. (2024)</a> showed that subthalamic beta changes with <strong>movement</strong>, <strong>dopamine</strong>, and <strong>DBS</strong> state; <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> showed that adaptive-DBS already splits across <strong>single-threshold</strong>, <strong>dual-threshold</strong>, and different onset-duration policies; <a href="https://doi.org/10.1093/brain/awae004" target="_blank">Olaru et al. (2024)</a> and <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">Mathiopoulou et al. (2025)</a> pushed up different <strong>gamma-linked</strong> biomarker families; <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Dixon et al. (2026)</a> added a remotely optimized neural-decoder route; and <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a> showed that <strong>eligibility</strong> and <strong>programming constraints</strong> can still block chronic use. Therefore, on this site, a state-dependent neuromodulation paper is not read only by <strong>trigger timing</strong> or <strong>symptom change</strong>. It must also disclose <strong>which biomarker family</strong>, <strong>which controller policy</strong>, <strong>which operating regime</strong>, <strong>which sensing exclusions</strong>, and <strong>which comparator</strong> made the result possible.
</p>

<h2>First, classify causal evidence into six levels</h2>
<table>
<thead>
<tr>
<th>Stage</th>
<th>What is actually changing</th>
<th>Minimum log wanted on this site</th>
<th>What still cannot be said</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Held-out decode</strong></td>
<td>Check whether the model still predicts on unused data.</td>
<td>Split unit, leakage audit, calibration error, uncertainty, and abstention if probabilities are output.</td>
<td>It still does not show agreement under changed conditions or agreement in causal structure.</td>
</tr>
<tr>
<td><strong>2. Online human-in-the-loop control</strong></td>
<td>A participant continuously operates while seeing or hearing the output.</td>
<td>End-to-end latency distribution, jitter, dropout, abstention or silence policy, and recalibration events.</td>
<td>Even if it works online, it still does not show compatibility with explicit perturbation, long-term durability, or same-state continuity.</td>
</tr>
<tr>
<td><strong>3. Bidirectional feedback / local intervention</strong></td>
<td>Feedback or stimulation changes the next biological input or behavior.</td>
<td>Stimulus timing, intensity, artifact window, effect size, failure cases, and local safety conditions.</td>
<td>Local causal gain still does not show whole-brain generative equivalence.</td>
</tr>
<tr>
<td><strong>4. State-dependent intervention</strong></td>
<td>Stimulation or control policy switches as a function of the detected state.</td>
<td>State-estimation error, biomarker family / symptom axis, controller family, comparator policy, duty cycle, stop conditions, abstention or fallback policy, and real-life block structure when relevant.</td>
<td>A symptom-linked controller or personalized biomarker route is still different from state completeness or branch-equivalence.</td>
</tr>
<tr>
<td><strong>5. Temporal durability / deployment</strong></td>
<td>The controller is expected to survive days, weeks, or home deployment rather than a single research session.</td>
<td>Fixed-decoder interval, supervised versus unsupervised recalibration route, performance-decay curve, recovery time, clinic versus home context, continuation or eligibility counts, signal-availability exclusions, and manual programming burden.</td>
<td>Cross-day operation still does not by itself show same-state continuity or maintenance-consistent causal equivalence.</td>
</tr>
<tr>
<td><strong>6. Perturbation-structure / branch test</strong></td>
<td>Compare multiple branches or perturbation-response patterns under fixed comparison rules.</td>
<td>Explicit branch variables, preregistered comparison rule, fixed failure criterion, repeatable perturbation set, temporal scope, and bridge status.</td>
<td>Even here, whole-brain identity, complete maintenance-state coverage, and social deployment are not automatically determined.</td>
</tr>
</tbody>
</table>

<h2>Recent literature forces five extra stop lines</h2>
<p>
The site's newer cards are not editorial decoration. They are forced by concrete gaps that recent primary literature leaves visible. This page now treats them as part of causal-verification reading rather than as optional follow-up bureaucracy.
</p>
<table>
<thead>
<tr>
<th>Stop line</th>
<th>Why recent literature forces it</th>
<th>What this site now requires</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Temporal Validity</strong></td>
<td><a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> shows that an impressive same-session voice loop can still lose fixed-decoder performance after about 15 days, while <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> shows that one month of unsupervised use must be read separately from pairwise recalibration.</td>
<td>Attach the <a href="https://mind-upload.com/verification.html#temporal-validity-card">Temporal Validity Card</a> whenever the claim reaches beyond same-session performance.</td>
</tr>
<tr>
<td><strong>Burst-Controller Log</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">Mathiopoulou et al. (2024)</a> shows that beta feedback is state-dependent, <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> shows that controller law and onset-duration policy are part of the object, <a href="https://doi.org/10.1093/brain/awae004" target="_blank">Olaru et al. (2024)</a> plus <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">Mathiopoulou et al. (2025)</a> show that gamma-linked routes are not the same biomarker family as beta-guided bradykinesia control, and <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a> shows that eligibility and programming constraints remain part of the result.</td>
<td>Attach the <a href="https://mind-upload.com/verification.html#additional-audit-logs">Burst-Controller Log</a> whenever burst-driven neuromodulation or adaptive DBS is promoted above exploratory timing or personalized-controller feasibility.</td>
</tr>
<tr>
<td><strong>State-Continuity Bridge</strong></td>
<td><a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">Lu et al. (2023)</a> shows that preservation route and fixation schedule alter extracellular-space retention, <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> remains a sequential in vivo-to-EM local pipeline rather than simultaneous same-state capture, and <a href="https://doi.org/10.1038/nature14467" target="_blank">Attardo et al. (2015)</a> shows that adult CA1 spines themselves turn over on the scale of weeks.</td>
<td>Attach the <a href="https://mind-upload.com/verification.html#state-continuity-bridge-card">State-Continuity Bridge Card</a> whenever a result is read as one same-state sample across days, regimes, or live-to-fix bridges.</td>
</tr>
<tr>
<td><strong>Maintenance-State Error Budget</strong></td>
<td><a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>, <a href="https://doi.org/10.1038/s41467-024-49572-8" target="_blank">Schreiner et al. (2024)</a>, and <a href="https://doi.org/10.1016/j.neuron.2025.03.020" target="_blank">Deng et al. (2025)</a> show that sleep history, replay coupling, and intracellular timing windows remain active controllers of persistence and recovery rather than background context.</td>
<td>Attach the <a href="https://mind-upload.com/verification.html#maintenance-state-error-budget">Maintenance-State Error Budget</a> whenever the claim concerns persistence, forgetting, reconsolidation, or recovery after perturbation.</td>
</tr>
<tr>
<td><strong>Body / Environment Boundary</strong></td>
<td><a href="https://doi.org/10.1126/science.abd0380" target="_blank">Flesher et al. (2021)</a> strengthens local bidirectional feedback, but the closed-loop literature more broadly still depends on retained or omitted tactile, proprioceptive, respiratory, arousal, and other organism-level routes.</td>
<td>Attach the <a href="https://mind-upload.com/verification.html#body-environment-boundary-card">Body / Environment Boundary Card</a> whenever a fast loop is being promoted toward naturalistic or embodied equivalence rather than local controller performance.</td>
</tr>
</tbody>
</table>

<h2>Boundary cases seen in primary literature</h2>
<table>
<thead>
<tr>
<th>Papers</th>
<th>What actually happened</th>
<th>How to read on this site</th>
<th>What still cannot be said</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Forenzo et al. (2024)</strong></td>
<td>A non-invasive EEG continuous-tracking task was run online with a deep-learning decoder inside the human loop.</td>
<td>This is an online-control result. It is stronger than offline accuracy and should be read through online metrics.</td>
<td>It is not counterfactual equivalence or whole-brain generative equivalence.</td>
</tr>
<tr>
<td><strong>Littlejohn et al. (2025)</strong></td>
<td>A speech neuroprosthesis streamed brain-to-voice updates in <strong>80-ms</strong> increments for naturalistic communication.</td>
<td>This is a communication-subsystem online-control advance. It raises the bar for tail-latency and output-path logging.</td>
<td>It still does not show same-state continuity, long-term fixed-decoder durability, or branch-equivalence.</td>
</tr>
<tr>
<td><strong>Wairagkar et al. (2025)</strong></td>
<td>Raw neural activity was converted into synthesized voice in less than <strong>10 ms</strong>, with silence returned in non-speech segments.</td>
<td>This is a strong same-session loop result and a strong abstention example.</td>
<td>The same paper still leaves long-term durability open because fixed-decoder performance declines after about 15 days.</td>
</tr>
<tr>
<td><strong>Wilson et al. (2025)</strong></td>
<td>One month of unsupervised closed-loop cursor control was obtained, with offline characterization of neural nonstationarity across five years.</td>
<td>This is the right reading model for <strong>Temporal Validity</strong> and recalibration burden.</td>
<td>Cross-day usability still does not by itself show same-state continuity or maintenance-complete control.</td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong></td>
<td>ICMS tactile feedback improved robotic-arm control behavior in a bidirectional BCI.</td>
<td>This is a classic example that bidirectional feedback can causally improve a local sensorimotor loop.</td>
<td>It remains a subsystem-limited causal gain rather than whole-brain WBE evidence.</td>
</tr>
<tr>
<td><strong>Oehrn et al. (2024), Cascino et al. (2026)</strong></td>
<td>Adaptive DBS was pushed into blinded randomized home-life blocks, and later chronic programming-principle work showed that <strong>eligibility</strong>, <strong>signal quality</strong>, and <strong>continuation</strong> remain practical constraints.</td>
<td>This is the correct reading model for <strong>deployment burden</strong> and <strong>controller-feasibility screening</strong> rather than laboratory-only success.</td>
<td>Symptom-control benefit still does not equal complete state reconfiguration, same-state equivalence, or one universally valid biomarker/controller pair.</td>
</tr>
<tr>
<td><strong>Mathiopoulou et al. (2024), Stanslaski et al. (2024), Olaru et al. (2024), Mathiopoulou et al. (2025), Dixon et al. (2026)</strong></td>
<td>Adaptive neuromodulation split across beta-guided bradykinesia control, multi-timescale threshold policies, dyskinesia-linked gamma, DBS-entrained prokinetic gamma, and movement-responsive decoder control.</td>
<td>This is the correct reading model for <strong>state-dependent controller family</strong>, not one generic `adaptive DBS` result.</td>
<td>It still does not show that one trigger family, one controller law, or one operating regime solves symptom-linked control across tasks, medication cycles, or home use.</td>
</tr>
<tr>
<td><strong>Casali et al. (2013), Comolatti et al. (2019)</strong></td>
<td>Perturbation-complexity metrics were formalized for TMS or intracranial stimulation responses.</td>
<td>Perturbation-based verification can be implemented, but only if stimulation conditions and artifact handling are fixed explicitly.</td>
<td>A single complexity index is still not enough for WBE pass or fail.</td>
</tr>
</tbody>
</table>

<h2>State-dependent neuromodulation is controller-limited, not just state-triggered</h2>
<p>
One more split is needed for causal-verification reading. The older version of this page already separated online control from temporal durability, which was necessary. It still remained too weak for burst-driven neuromodulation, because it let readers learn adaptive DBS as if the main question were only whether stimulation responded to a detected signal. The current primary literature does not support that shortcut. On this site, a burst-driven or adaptive-neuromodulation result now has to separate the <strong>biomarker family</strong>, the <strong>symptom axis</strong>, the <strong>controller mode and timescale</strong>, the <strong>sensing-compatibility burden</strong>, the <strong>comparator policy</strong>, and the <strong>programming / continuation burden</strong>.
</p>
<table>
<thead>
<tr>
<th>Layer to separate</th>
<th>What recent literature now supports</th>
<th>What must be logged on this site</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Biomarker family / symptom axis</strong></td>
<td><a href="https://doi.org/10.1002/ana.23951" target="_blank">Little et al. (2013)</a> and <a href="https://doi.org/10.1093/brain/awx010" target="_blank">Tinkhauser et al. (2017)</a> support beta-guided antikinetic control, <a href="https://doi.org/10.1093/brain/awae004" target="_blank">Olaru et al. (2024)</a> supports dyskinesia-linked narrowband gamma, <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">Mathiopoulou et al. (2025)</a> supports DBS-entrained prokinetic gamma, and <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Dixon et al. (2026)</a> supports a movement-responsive neural-decoder route.</td>
<td>Name the biomarker family, symptom target, and why that pairing is being read as the relevant controller object.</td>
</tr>
<tr>
<td><strong>State dependence / controllability</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">Mathiopoulou et al. (2024)</a> showed that subthalamic beta changes with movement, dopamine, and DBS itself, and <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12397205/" target="_blank">Busch et al. (2025)</a> showed that chronic thresholds and controllability can drift across real-life use.</td>
<td>Name the operating regime: rest versus movement, medication state, stimulation state, and any state slices where the controller stopped being reliable.</td>
</tr>
<tr>
<td><strong>Controller mode / timescale</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> showed that adaptive DBS already splits across single-threshold, dual-threshold, and different onset-duration policies rather than one universal timing law.</td>
<td>Name the controller family, update interval, onset duration, ramp or smoothing policy, floor / ceiling amplitude, and fallback rule.</td>
</tr>
<tr>
<td><strong>Sensing compatibility / artifact burden</strong></td>
<td><a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">Stanslaski et al. (2024)</a> and <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a> show that inadequate signal, artifacts, absent peaks, and incompatible settings remain major bottlenecks rather than background implementation detail.</td>
<td>Name sensing contacts, signal-to-noise or peak criteria, excluded hemispheres or participants, artifact resets, and any unilateral or surrogate sensing policy.</td>
</tr>
<tr>
<td><strong>Comparator and deployability burden</strong></td>
<td><a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a> showed blinded randomized symptom benefit for a personalized signal-selection route, while <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">Cascino et al. (2026)</a> showed that chronic continuation still depends on eligibility and repeated optimization.</td>
<td>Name the comparator condition, any matching rule for duty cycle or energy when relevant, the programming workflow, continuation counts, and whether the benefit survives outside the tuning context.</td>
</tr>
</tbody>
</table>

<strong>Fast communication BCI is still not counterfactual equivalence</strong>
<p>
<a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>, <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> all move speech neuroprosthetics forward. However, what they establish is <strong>online decoding and closed-loop communication in a subsystem</strong>. On this site that is not upgraded to <strong>branch-equivalence</strong>, <strong>whole-brain causal equivalence</strong>, or <strong>same-state continuity</strong> without the extra card bundle above.
</p>

<h2>What this site calls a counterfactual test</h2>
<p>
On this site, we do not call something a <strong>counterfactual</strong> merely because conditions were changed. If the bundle below is incomplete, the result stays at a weaker label such as <strong>intervention response test</strong>, <strong>state-dependent controller result</strong>, or <strong>perturbation generalization test</strong>.
</p>
<table>
<thead>
<tr>
<th>Condition</th>
<th>Why it is necessary</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Branch variables are explicit</strong></td>
<td>If it is unclear what was changed, it is impossible to distinguish branch comparison from noise or drift.</td>
</tr>
<tr>
<td><strong>Comparison rules are pre-registered</strong></td>
<td>If convenient branches are chosen after seeing the result, the test only looks counterfactual in retrospect.</td>
</tr>
<tr>
<td><strong>Artifact windows and safety conditions are published</strong></td>
<td>Without this, stimulation-induced artifacts can be misread as neural response.</td>
</tr>
<tr>
<td><strong>Temporal scope is fixed explicitly</strong></td>
<td>Readers need to know whether the test is same-trial, same-session, same-day, or cross-day, and whether the decoder was fixed or recalibrated.</td>
</tr>
<tr>
<td><strong>Controller family is disclosed for state-dependent neuromodulation</strong></td>
<td>Without biomarker family, controller law, sensing exclusions, and comparator policy, a burst-trigger result can be overread as generic adaptive control.</td>
</tr>
<tr>
<td><strong>Bridge status is disclosed when same-subject language is used</strong></td>
<td>A same-subject claim still needs acquisition order, elapsed time, regime continuity, and omitted drift processes before it can be read as one same-state sample.</td>
</tr>
<tr>
<td><strong>Failure conditions are fixed in advance</strong></td>
<td>The result is only falsifiable when the threshold for branch mismatch is declared before the outcome is known.</td>
</tr>
</tbody>
</table>

<h2>Minimum log bundle now required</h2>
<table>
<thead>
<tr>
<th>Log family</th>
<th>What to keep</th>
<th>What overread it blocks</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Intervention definition</strong></td>
<td>Site, intensity, timing, duration, branch variable, task condition, and explicit control or sham policy.</td>
<td>Blocks vague claims that "something was perturbed" without a reproducible branch definition.</td>
</tr>
<tr>
<td><strong>Artifact and safety handling</strong></td>
<td>Artifact window, interpolation or masking policy, excluded trials, stop conditions, and hard-stop versus soft-fallback behavior.</td>
<td>Blocks device-induced changes from being misread as neural response.</td>
</tr>
<tr>
<td><strong>Online timing and abstention</strong></td>
<td>P50/P95/P99 latency, jitter, dropout, output-path delay, and abstention, silence, or hold-last-output policy.</td>
<td>Blocks average latency alone from standing in for actual loop behavior.</td>
</tr>
<tr>
<td><strong>Temporal validity</strong></td>
<td>Fixed-decoder interval, supervised versus unsupervised recalibration route, performance-decay curve, recovery time, and clinic-versus-home block structure.</td>
<td>Blocks same-session success from being silently promoted to cross-day durability.</td>
</tr>
<tr>
<td><strong>Burst-controller disclosure</strong></td>
<td>Biomarker family / symptom axis, controller family, state slice, sensing exclusions, comparator policy, and programming or rescue burden.</td>
<td>Blocks exploratory trigger timing from being promoted to validated symptom-linked control.</td>
</tr>
<tr>
<td><strong>Bridge status</strong></td>
<td>Same-session or cross-day status, live-to-fix or live-to-live ordering, elapsed time, regime change, and coordinate-transfer burden.</td>
<td>Blocks same-subject wording from being misread as one same-state sample.</td>
</tr>
<tr>
<td><strong>Maintenance-state disclosure</strong></td>
<td>If persistence, forgetting, reconsolidation, or recovery is claimed, name the relevant maintenance families or attach the Maintenance-State Error Budget.</td>
<td>Blocks intervention response from being upgraded to long-horizon maintenance evidence.</td>
</tr>
<tr>
<td><strong>Boundary disclosure</strong></td>
<td>Retained, substituted, and omitted sensory, motor, interoceptive, and feedback routes.</td>
<td>Blocks a fast local controller from being promoted to naturalistic or embodied equivalence.</td>
</tr>
</tbody>
</table>

<h2>Eight questions when reading causal-verification papers</h2>
<ol>
<li><strong>What was changed physically or computationally?</strong> Distinguish branch variable, decoder update, feedback path, and task manipulation.</li>
<li><strong>Is the result same-session, cross-day, or home-life?</strong> Online success in one session is different from temporal durability.</li>
<li><strong>Was the decoder fixed, supervised, or unsupervised?</strong> Hidden recalibration changes what the claimed causal evidence means.</li>
<li><strong>If the result is state-dependent neuromodulation, which biomarker family and controller law were actually used?</strong> `Adaptive` is too coarse unless biomarker, timescale, comparator, and sensing exclusions are explicit.</li>
<li><strong>Was the result compared against a named controller or only against a weak baseline?</strong> Symptom benefit and controller feasibility are different readings.</li>
<li><strong>If the paper says same-subject or same-brain, is it really one same-state sample?</strong> Check bridge order, elapsed time, and regime continuity.</li>
<li><strong>If persistence or recovery is claimed, where is the maintenance-state disclosure?</strong> Intervention logs alone are not enough for long-horizon claims.</li>
<li><strong>Are we jumping from subsystem-limited causal gain to whole-brain equivalence?</strong> This remains the main overread to block.</li>
</ol>

<h2>References</h2>
<ol>
<li>Forenzo D, Zhu H, Shanahan J, Lim J, He B. Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. <em>PNAS Nexus</em>. 2024. <a href="https://doi.org/10.1093/pnasnexus/pgae145" target="_blank">doi:10.1093/pnasnexus/pgae145</a></li>
<li>Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. <em>Nature</em>. 2023. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>. 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Moses DA, Metzger SL, et al. An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>. 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science</em>. 2021. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Wilson GH, Bray N, Franken M, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. <em>Annals of Neurology</em>. 2013. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <em>Brain</em>. 2017. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Mathiopoulou V, Lofredi R, Feldmann LK, et al. Modulation of subthalamic beta oscillations by movement, dopamine, and deep brain stimulation in Parkinson's disease. <em>npj Parkinson's Disease</em>. 2024. <a href="https://doi.org/10.1038/s41531-024-00693-3" target="_blank">doi:10.1038/s41531-024-00693-3</a></li>
<li>Stanslaski S, Summers RLS, Tonder L, et al. Sensing data and methodology from the Adaptive DBS Algorithm for Personalized Therapy in Parkinson's Disease (ADAPT-PD) clinical trial. <em>npj Parkinson's Disease</em>. 2024. <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">doi:10.1038/s41531-024-00772-5</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <em>Nature Medicine</em>. 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Olaru M, Cernera S, Hahn A, et al. Motor network gamma oscillations in chronic home recordings predict dyskinesia in Parkinson's disease. <em>Brain</em>. 2024. <a href="https://doi.org/10.1093/brain/awae004" target="_blank">doi:10.1093/brain/awae004</a></li>
<li>Busch JL, Kaplan J, Behnke JK, et al. Chronic adaptive deep brain stimulation for Parkinson's disease: clinical outcomes and programming strategies. <em>npj Parkinson's Disease</em>. 2025. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12397205/" target="_blank">PMC:PMC12397205</a></li>
<li>Mathiopoulou V, Habets J, Feldmann LK, et al. Gamma entrainment induced by deep brain stimulation as a biomarker for motor improvement with neuromodulation. <em>Nature Communications</em>. 2025. <a href="https://doi.org/10.1038/s41467-025-58132-7" target="_blank">doi:10.1038/s41467-025-58132-7</a></li>
<li>Dixon S, Oehrn C, Remple M, et al. Movement-responsive deep brain stimulation for Parkinson's disease using a remotely optimized neural decoder. <em>Nature Biomedical Engineering</em>. 2026. <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">doi:10.1038/s41551-025-01438-0</a></li>
<li>Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. <em>npj Parkinson's Disease</em>. 2026. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
<li>Wilkins KB, Melbourne JA, Akella P, et al. Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease. <em>Brain Communications</em>. 2025. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/" target="_blank">PMC:PMC12268161</a></li>
<li>Lu Z, Chmielowiec J, Himes B, et al. Fixation-dependent changes in the preservation of extracellular space in the neuro-glio-vascular unit. <em>Cell Reports Methods</em>. 2023. <a href="https://doi.org/10.1016/j.crmeth.2023.100520" target="_blank">doi:10.1016/j.crmeth.2023.100520</a></li>
<li>MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>. 2025. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Attardo A, Fitzgerald JE, Schnitzer MJ. Impermanence of dendritic spines in live adult CA1 hippocampus. <em>Nature</em>. 2015. <a href="https://doi.org/10.1038/nature14467" target="_blank">doi:10.1038/nature14467</a></li>
<li>Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>. 2016. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Schreiner T, Petzka M, Staudigl T, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. <em>Nature Communications</em>. 2024. <a href="https://doi.org/10.1038/s41467-024-49572-8" target="_blank">doi:10.1038/s41467-024-49572-8</a></li>
<li>Deng Z, Fei X, Zhang S, Xu M. A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. <em>Neuron</em>. 2025. <a href="https://doi.org/10.1016/j.neuron.2025.03.020" target="_blank">doi:10.1016/j.neuron.2025.03.020</a></li>
<li>Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. <em>Science Translational Medicine</em>. 2013. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti R, Pigorini A, Casarotto S, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. <em>Brain Stimulation</em>. 2019. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
</ol>

<h2>Where to go back next</h2>
<p>
To return to the difference between translation and generation, use <a href="https://mind-upload.com/wbe_101.html">Introduction to WBE</a>. To return to the site-wide rule bundle, use <a href="https://mind-upload.com/verification.html">Verification platform</a>. To return to timing-side deployment detail, use <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">Wiki: Closed Loop, Delay, Jitter, Safe Stop</a>. To return to bridge validity itself, use <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge">Wiki: State-Continuity Bridge</a>.
</p>
