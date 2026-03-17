# Wiki: Verification of counterfactuals, interventions, and perturbations

> High accuracy is one thing, correct response to changing conditions is another.
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Learning guide

## このページの役割
This page is a wiki that separates the verification of held-out accuracy, online human-in-the-loop, external intervention, and perturbation complexity along the lines of primary literature. In addition to the concept words, list what papers actually change and what they don't show yet.

## 正確さの前提
The primary literature as of March 2026 strongly supports local subsystem and task-specific causal evidence. This does not mean that the counterfactual equivalence of whole-brain WBE has been demonstrated.

## 公開ページへ戻る
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [FAQ](https://mind-upload.com/faq.html)

## 関連 Wiki
- [Wiki: Decode and Emulate](https://github.com/yasufumi-nakata/mind-upload/wiki/decode-vs-emulate) - First, it is for those who want to go back to the difference between translation and generation.
- [Wiki: From observation to estimation](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - It compensates for the difference between inferential models and causal models.
- [Wiki: Closed loop, delay, jitter, safe stop](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - Supplements practical indicators when reading causal verification online.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - It complements the role of Benchmark, Registry, and Model Card.

## いま分かっていること
- High held-out precision alone does not guarantee agreement in causal structure.
- Bidirectional feedback and state-dependent stimulation strengthen causal evidence, but their scope of application tends to be localized.
- Logs of latency, recalibration, and abstention are essential in closed-loop systems.

## まだ分かっていないこと
- It is an open question which set of perturbations is sufficient to satisfy the generative equivalence of WBE.
- The extent to which counterfactual bifurcations can be benchmarked is still under research in terms of both theory and engineering.
- No public infrastructure exists yet to directly test branch-equivalence on a whole-brain scale.

---

<h2>Shortest conclusion</h2>
<p>
High held-out accuracy is important, but it alone does not mean that the mechanisms inside are the same. Primary literature as of March 2026 shows that<strong>offline decode</strong>, <strong>online human-in-the-loop</strong>, <strong>external intervention</strong>, and <strong>long-term closed loop</strong> are separate walls.
</p>

<strong>Points fixed in this reorganization</strong>
<p>
The previous edition had a heavy emphasis on explaining intervention, counterfactual, and perturbation as conceptual terms, making it difficult to see which papers demonstrated what level of proof. On this page, we list <strong>what has actually changed</strong>, <strong>what has improved</strong>, and <strong>what cannot be said</strong> for each primary source.
</p>

<h2>First, classify the strength of causal evidence into five levels</h2>
<table>
<thead>
<tr>
<th>stage</th>
<th>What is actually changing</th>
<th>Minimum desired log</th>
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. held-out decode</strong></td>
<td>See if it hits with untrained data. </td>
<td>Division unit, leak test, calibration error, and uncertainty. </td>
<td>It is not yet possible to say whether the response to condition changes or the causal structure matches. </td>
</tr>
<tr>
<td><strong>2. online human-in-the-loop</strong></td>
<td>The subject performs continuous operations and conversations while viewing the output. </td>
<td>End-to-end latency, jitter, dropout, and recalibration events. </td>
<td>Even if it works online, it still cannot be said that it is compatible with external intervention. </td>
</tr>
<tr>
<td><strong>3. Bidirectional feedback / local intervention</strong></td>
<td>With haptic feedback or stimulation, create a loop where the output changes the next input. </td>
<td>Stimulus timing, intensity, artifact window, and amount of behavioral change. </td>
<td>Even if we can show local causal gain, we cannot show whole-brain generative equivalence. </td>
</tr>
<tr>
<td><strong>4. state-dependent intervention</strong></td>
<td>Switches stimulation and control depending on the detected state. </td>
<td>State estimation error, stimulus duty cycle, stop conditions, home operation log. </td>
<td>Task-specific controller effectiveness, state completeness is another matter. </td>
</tr>
<tr>
<td><strong>5. perturbation-structure test</strong></td>
<td>Compare multiple condition branches and perturbation response structures. </td>
<td>A set of branching conditions, comparison rules, failure conditions, and repeatable perturbations. </td>
<td>Here too, identity and social implementation cannot be automatically determined. </td>
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
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Forenzo et al. (2024)</strong></td>
<td>We evaluated the non-invasive EEG continuous tracking task online and compared the behavior of the deep learning decoder within the human loop. </td>
<td>It is important to point out the online metric rather than the offline accuracy. Even though it is non-invasive, it can be read that there is a human-in-the-loop wall. </td>
<td>This is a demonstration of continuous control, not counterfactual equivalence or whole-brain generation. </td>
</tr>
<tr>
<td><strong>Wairagkar et al. (2025)</strong></td>
<td>We showed a voice loop that went from raw neural activity to speech synthesis within 10 ms, and returned silence in the non-speech section. </td>
<td>It turns out that implementing low latency and abstention is an essential part of closed-loop evaluation. </td>
<td>Fixed decoders show performance degradation after about 15 days, long-term stability is another issue. </td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong></td>
<td>Adding ICMS haptic feedback to the sensory cortex improved the trial time and grasp time of robotic arm control. </td>
<td>This is a classic example of causal evidence that bidirectional feedback changes behavior. </td>
<td>It is a local loop in the sensorimotor subsystem and is not a sufficient condition for whole-brain WBE. </td>
</tr>
<tr>
<td><strong>Oehrn et al. (2024)</strong></td>
<td>We compared chronic adaptive DBS and conventional DBS for Parkinson's disease in a blinded randomized block, and evaluated the results including the home environment. </td>
<td>It turns out that if you insist on state-dependent intervention, you'll need real-life block comparisons. </td>
<td>Controller demonstration of symptom control, not complete reconfiguration of internal state. </td>
</tr>
<tr>
<td><strong>Casali et al. (2013), Comolatti et al. (2019)</strong></td>
<td>We demonstrated a method to quantify response complexity to TMS/intracranial stimulation. </td>
<td>Although perturbation-based verification can be implemented, it can be read that comparisons cannot be made unless the stimulus conditions and artifact handling are fixed. </td>
<td>A single indicator alone is not enough to determine pass/fail of WBE. </td>
</tr>
</tbody>
</table>

<strong>Increasing the speed of communication BCI is not directly causally equivalent</strong>
<p>
Willett et al. (2023) and Littlejohn et al. (2025) showed that speech neuroprosthesis can be fast and streaming. However, what was demonstrated here is<strong>online decoding / control</strong> of the communication subsystem, not branch-equivalence or whole-brain WBE.
</p>

<h2>What is called a "counterfactual" when it is satisfied</h2>
<p>
On this site, we do not call something a <strong>counterfactual</strong> simply by ``changing the conditions.'' If at least the following four conditions are not met, it is called an <strong>intervention response test</strong> or <strong>perturbation generalization test</strong>, which are weaker expressions.
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
<td>If it is unclear what was changed, it is impossible to distinguish between comparing different conditions or just a noise difference. </td>
</tr>
<tr>
<td><strong>Comparison rules are pre-registered</strong></td>
<td>If you choose only convenient branches later, it will look like a counterfactual. </td>
</tr>
<tr>
<td><strong>Artifact windows and safety conditions are published</strong></td>
<td>It is necessary to determine whether the signal change after stimulation is a neural response or a device-induced change. </td>
</tr>
<tr>
<td><strong>Fixed failure conditions</strong></td>
<td>You must first decide how far the deviation should be before it is determined that the same branch cannot be reproduced. </td>
</tr>
</tbody>
</table>

<h2>The minimum log you want to keep</h2>

<h4>Checklist</h4>
<ul>
<li><strong>Definition of intervention:</strong>Stimulation site, intensity, timing, duration, trial conditions. </li>
<li><strong>Artifact processing:</strong>Exclusion window immediately after stimulus, interpolation, masking, trials not included. </li>
<li><strong>online metrics:</strong>end-to-end latency distribution, dropout, recalibration events, abstention rate. </li>
<li><strong>Effect size:</strong>Not only average improvement but also trial-level variation, failure cases, and recovery time. </li>
<li><strong>Comparison rules:</strong>Which condition should be the main comparison and which result should be considered a fail. </li>
</ul>

<h2>5 questions when reading causal verification papers</h2>
<ol>
<li><strong>Do you have online metrics instead of offline accuracy?</strong>For human-in-the-loop issues, offline alone is not enough. </li>
<li><strong>Does it say what actually changed?</strong>Distinguish between stimulus, feedback, decoder updates, and task conditions. </li>
<li><strong>Is artifact processing made clear?</strong>Especially in the stimulus system, if this is omitted, causal evidence will collapse. </li>
<li><strong>Are there any hidden recalibrations and abandonments?</strong>Look for loops that aren't just about successful trials. </li>
<li><strong>Aren't we making a leap from proving local subsystems to whole-brain equivalence?</strong>This is the most important point. </li>
</ol>

<h2>References</h2>
<ol>
<li>Forenzo D, Zhu H, Shanahan J, Lim J, He B. Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. PNAS Nexus. 2024. <a href="https://doi.org/10.1093/pnasnexus/pgae145" target="_blank">doi:10.1093/pnasnexus/pgae145</a></li>
<li>Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Moses DA, Metzger SL, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. Nat Med. 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Wilson GH, Bray N, Franken M, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med. 2013. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti R, Pigorini A, Casarotto S, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. Brain Stimul. 2019. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
</ol>

<h2>Where to go back next</h2>
<p>
To return to the difference between translation and generation, please use <a href="https://mind-upload.com/wbe_101.html">Introduction to WBE</a>, to return to verification design <a href="https://mind-upload.com/verification.html">Verification infrastructure</a>, and to return to closed-loop practice please use <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">Wiki: Closed-loop, delay, jitter, and safety stops</a>.
</p>
