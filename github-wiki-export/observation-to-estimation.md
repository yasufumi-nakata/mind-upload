# Wiki: From observation to estimation

> Being consistent with observation, understanding internal states, and understanding cause and effect are different things.
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-14 / Role: Technical / natural science only

## Role Of This Page
This page is a wiki that organizes where to stop making claims and what to add to make them even stronger when estimating brain states and causal structures from observational signals such as EEG. Connect forward problems, inverse problems, ESI, DCM, SCM, and causal equivalence classes in the order of ``observation → estimation → intervention → validation.''

## Accuracy Notes
This is not a fixed recipe for which method to use. This page first fixes audit items that cannot be avoided no matter what method you use.

## Back To Public Pages
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [technology roadmap](https://mind-upload.com/tech_roadmap.html)

## Related Wiki Pages
- [Wiki: From measurement to modeling](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-and-modeling-terms) - You can return to the overall map of measurement, organization, estimation, and verification.
- [Wiki: EEG pretreatment and QC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - In the first stage of estimation, we compensate for what changes the results.
- [Wiki: Uncertainty, proofreading, abstaining](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - Instead of point estimation, we supplement the width and how to leave conditions for abstention.
- [Wiki: Counterfactuals/Interventions/Perturbations](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - It supplements the conditions for proceeding from observational adaptation to intervention validation.

## What Is Currently Known
- In principle, it is difficult to uniquely determine brain activity from scalp EEG, and estimation requires assumptions.
- High-density EEG, individualized MRI, FEM/BEM, and empirical Bayesian estimation can improve conditions, but alone do not guarantee unique recovery.
- The causal structure cannot be determined by observational fit alone; a set of candidate models and an intervention design are required.

## What Is Still Unknown
- It remains unclear which measurement/modeling combination is most effective for validating WBE.
- Research is currently underway to determine how detailed the causal structure and state variables can be stably restored using non-invasive measurements alone.
- Which external validation ladders will be pinned to the site-wide benchmark is still being worked out.

---

<h2>Conclusion</h2>
<p>
Even if a model that matches the observed signal is found, it cannot be said that the internal state has been uniquely determined or that the causal structure has been identified. Therefore, on this site, we audit four points, <strong>geometry, uncertainty, candidate model set, and external validation</strong>, before looking at the solver name or theory name.
</p>

<strong>Scope of this page</strong>
<p>
I am not going to deal with philosophy or legal systems here. We will organize the boundaries between observation, estimation, and causal claims based on primary literature from only the aspects of technology and natural science.
</p>

<h2>Four audit gates to be fixed first</h2>
<table>
<thead>
<tr>
<th>Audit gate</th>
<th>What I want at least</th>
<th>Claim that it stops when there is not enough</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1: Geometry and forward model</strong></td>
<td>Electrode coordinates, head model, conductivity assumption, presence or absence of individual MRI, sensitivity analysis. </td>
<td>I cannot make strong anatomical source claims. </td>
</tr>
<tr>
<td><strong>Gate 2: Visualizing uncertainty</strong></td>
<td>Posterior distribution, confidence interval, bootstrap/ensemble width, or solver/preprocessing sensitivity analysis. </td>
<td>It is not possible to write it as the only solution using only point estimation. </td>
</tr>
<tr>
<td><strong>Gate 3: Specifying candidate model set</strong></td>
<td>Compared model spaces, family comparisons, remaining equivalence classes, abstention conditions. </td>
<td>Even if we use DCM or SCM, we cannot say that we have uniquely discovered cause and effect. </td>
</tr>
<tr>
<td><strong>Gate 4: External validation/intervention</strong></td>
<td>Simulation, phantom, simultaneous invasive recording, intracranial stimulation, held-out prediction of stimulus/lesion/task perturbations. </td>
<td> Observed fit cannot be promoted to causal validity or generalization performance. </td>
</tr>
</tbody>
</table>

<h2>Do not mix observation, estimation, and causal verification</h2>
<table>
<thead>
<tr>
<th>stage</th>
<th>What we're doing here</th>
<th>Things that cannot be said at this stage yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Observation</strong></td>
<td>Measures signals visible on the scalp and outside. </td>
<td>It cannot be said that the brain state has been uniquely restored. </td>
</tr>
<tr>
<td><strong>Estimation</strong></td>
<td>Place a head model or generative model to infer activity sources and connections. </td>
<td>It cannot be said that it is true even outside the candidate model. </td>
</tr>
<tr>
<td><strong>Intervention/validation</strong></td>
<td>Calibrate predictions with stimuli, lesions, task changes, intracranial stimulation, and concurrent invasive recordings. </td>
<td>Even with this, the branch-equivalence of whole-brain WBE cannot be said. </td>
</tr>
</tbody>
</table>

<h2>Forward and inverse problems</h2>
<table>
<thead>
<tr>
<th>Term</th>
<th>Meaning</th>
<th>Effective points in auditing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Order questions</strong></td>
<td>If there is this activity in the brain, calculate what it looks like in the scalp. </td>
<td>Head model, conductivity, and electrode placement assumptions come to the fore. </td>
</tr>
<tr>
<td><strong>Inverse problem</strong></td>
<td>We estimate the brain activity that can explain the signals seen on the scalp. </td>
<td>Uncertainty and sensitivity analysis is essential because multiple solutions can produce the same observation. </td>
</tr>
</tbody>
</table>
<p>
The inverse problem is difficult because<strong>multiple internal states can produce the same observation</strong>. Therefore, the important thing here is not to strongly insist on the "best one point" but to reveal what assumptions made and how far the results were narrowed down.
</p>

<h2>Read ESI in the validation ladder first, rather than the solver name</h2>
<p>
ESI is a framework for estimating source from scalp signals. However, as shown by direct validation studies by Mikulan et al. and Unnwongse et al., the error varies greatly depending on source depth, cranial conductivity, head model, electrode geometry, and solver selection. Therefore, it is not possible to make a strong argument just by saying<strong>Because it is a high-density EEG or because it is a Bayesian solver</strong>.
</p>
<table>
<thead>
<tr>
<th>Check with ESI first</th>
<th>Why is it important</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Geometry</strong></td>
<td>The source error will change if the electrode position, individual MRI, FEM/BEM, and conductivity assumptions are different. </td>
</tr>
<tr>
<td><strong>Uncertainty</strong></td>
<td>Empirical Bayes and ensemble are powerful, but what is essential is visualization of the width, not the solver name. </td>
</tr>
<tr>
<td><strong>Withholding deep/micro sources</strong></td>
<td>Detectable and general reconstruction are different, and deep generalization requires a suspension condition. </td>
</tr>
<tr>
<td><strong>External validation</strong></td>
<td>It is necessary to know where the simulation, phantom, simultaneous invasive recording, and intracranial stimulation were calibrated. </td>
</tr>
</tbody>
</table>

<strong>Replacement on this site</strong>
<p>
Bayesian / empirical Bayes / sparse Bayesian learning is a good candidate for<strong>estimation with uncertainty</strong>. However, on this site, rather than ``accepting a proposal because it is Bayesian'', the criteria for acceptance or rejection are <strong>how uncertainty is disclosed and what external standards were used for calibration</strong>.
</p>

<h2>DCM is not "a device that automatically discovers true cause and effect"</h2>
<p>
DCM is a framework that specifies candidate generative models and compares them to see which one is easier to explain observations. As shown in Friston et al.'s original paper and Penny et al.'s model comparison study, DCM conclusions depend on the candidate model space entered into the comparison. Therefore, winning in a model comparison means that it is ``good among the candidate set'' and does not mean that it is<strong>the only correct one in</strong>the world.
</p>

<h4>Four points when reading DCM</h4>
<ul>
<li><strong>Candidate model space:</strong> Which nodes and join candidates were initially included in the comparison. </li>
<li><strong>Family comparison:</strong>Is the upper family stable, not the details? </li>
<li><strong>model recovery:</strong>Can the correct model be recovered through simulation? </li>
<li><strong>Intervention Calibration:</strong>Is the held-out prediction correct with the stimulus or perturbation? </li>
</ul>

<h2>SCM and causal discovery only become stronger with intervention</h2>
<p>
SCM is a framework that makes it easy to write down interventions and counterfactuals explicitly. However, when we learn only from observational data, we are often left with a<strong>Markov equivalence class</strong>. As shown by Hauser and Buhlmann, intervention data are important for narrowing this class of equivalences. Even in brain data, Vink et al. showed that resting-state functional connectivity remains a weak predictor of causal interaction, and it is dangerous to determine direction and mechanism based on correlation alone.
</p>

<strong>Difference in role between SCM and DCM</strong>
<p>
DCM is useful for comparing neural circuit candidate generation models, and SCM is useful as a language for expressing interventions and counterfactuals. Both are important, but adding one does not automatically establish cause and effect.
</p>

<h2>External validation ladder for progressing to stronger claims</h2>
<table>
<thead>
<tr>
<th>Validation ladder</th>
<th>What do we know</th>
<th>Limits that still remain</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Simulation</strong></td>
<td>You can see the lower limit performance of solver and model recovery. </td>
<td>It does not completely reproduce the real head geometry and biological noise. </td>
</tr>
<tr>
<td><strong>Phantom</strong></td>
<td>You can calibrate the geometry and validity of the forward model. </td>
<td>There is no biological plasticity or state dependence. </td>
</tr>
<tr>
<td><strong>Simultaneous invasive/non-invasive record</strong></td>
<td>Comparisons can be made close to the local ground truth. </td>
<td>coverage-limited, not whole-brain ground truth. </td>
</tr>
<tr>
<td><strong>Intracranial stimulation/perturbation</strong></td>
<td>Enables validation of intervention responses and time order. </td>
<td>Highly dependent on stimulus conditions and observation window design. </td>
</tr>
</tbody>
</table>

<h2>Operation rules adopted by this site</h2>

<h4>Rule</h4>
<ul>
<li><strong>Don't write solver names as standard:</strong>Bayesian solver, minimum norm, DCM, and SCM are candidates, and acceptance or rejection is determined by audit items. </li>
<li><strong>Don't raise causal claims based on observed fit alone:</strong>In the absence of intervention or external validation, stay at the equivalence class or candidate model level. </li>
<li><strong>Write with reservations for deep and fine-grained information:</strong>Do not confuse detectable with robust reconstruction. </li>
<li><strong>Abstain when there is wide uncertainty:</strong>If the solutions overlap, do not force them to collapse into one, but make your reservations clear. </li>
</ul>

<h2>References</h2>
<ol>
<li>Wipf, D., &amp; Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging. <em>NeuroImage</em>, 44(3), 947-966. <a href="https://doi.org/10.1016/j.neuroimage.2008.02.059" target="_blank">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(1), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, Y., Alhilani, M., Asano, E., et al. (2025). High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. <em>Epilepsia</em>. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging extended E/MEG source activation with empirical Bayesian uncertainty quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <em>NeuroImage</em>, 19(4), 1273-1302. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Lee, H.-L., Zahneisen, B., Hugger, T., et al. (2017). Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. <em>NeuroImage</em>, 149, 441-451. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.012" target="_blank">doi:10.1016/j.neuroimage.2017.02.012</a></li>
<li>Hauser, A., &amp; Buhlmann, P. (2012). Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. <em>Journal of Machine Learning Research</em>, 13, 2409-2464. <a href="https://jmlr.org/papers/v13/hauser12a.html" target="_blank">JMLR</a></li>
<li>Vink, J. J., Ramos-Nuñez, A. I., Bellesi, A., et al. (2020). The brain's functional connectome is a poor predictor of the brain's causal activity flow. <em>PLOS Computational Biology</em>, 16(1), e1007866. <a href="https://doi.org/10.1371/journal.pcbi.1007866" target="_blank">doi:10.1371/journal.pcbi.1007866</a></li>
</ol>
