# Site Deepening Audit (2026-03-14, Observation / Estimation / Identifiability)

## Scope

- Main target: `wiki/observation-to-estimation.md`
- Secondary target: `tech_roadmap.md`
- Secondary target: `wiki/measurement-and-modeling-terms.md`

## Why This Page Was Selected

- As of 2026-03-14, `closed loop`, `causal perturbation`, `multimodal integration`, and `decode vs emulate` on the public site were quite specific.
- On the other hand, although the conceptual arrangement around `From observation to inference` is correct, `Where does the argument stop?' and `What can we add to make it even stronger?' were not audited items based on primary literature.
- This weakness is not limited to local pages. R1 / R4 / R7 of `tech_roadmap.md` is a reference point that determines "how far you can say" for the entire site, and if you are lenient here, the readings of ESI, DCM, SCM, and causal equivalence classes will become optimistic on all pages.

## Main Critiques

### 1. The old `R1` was written in a way that could be read as "Bayesian standard solution", and the solver name appeared before the audit item.

- Issue:
- R1 of the old `tech_roadmap.md` wrote correctly that the inverse problem was a bad setting.
- However, the conclusion was closed with `Bayesian approach in principle`, a structure that could give the reader the impression that ``the problem can be solved to a large extent by determining the solver family.''
- Basis:
- Wipf & Nagarajan (2009) presented a unified Bayesian framework, but this is a study that shows the power of Bayesian routes, and is not a study that guarantees unique restoration on its own.
- Aydin et al. (2019) showed that uncertainty in head tissue conductivity greatly affects dipole reconstruction.
- Unnwongse et al. (2023) and Hao et al. (2025) show that source depth, geometry, forward model, and solver have a strong effect on errors in direct validation using intracranial stimulation and simultaneous SEEG as ground truth.
- Revision:
- `Bayesian Principles` has been withdrawn and `Uncertainty Representation + Geometric/Conductivity Sensitivity Analysis + External Validation` has been brought forward as an acceptance condition.
- Bayesian / empirical Bayes has been repositioned as a "promising candidate".

### 2. The old `R4` read Active Inference and multiscale simulation as if they were the default route.

- Issue:
- The previous version emphasized `Active Inference` and `Multi-scale causal modeling such as Blue Brain Project` as strong policies.
- However, as of 2026-03, primary literature strongly supports the following points: `Causality cannot be identified by observational fit alone`, `Candidate model space and intervention data are required`, `Theories should be competitive`.
- Basis:
- Friston et al. (2003) and Penny et al. (2004) make it clear that DCM is a candidate model comparison.
- Hauser & Buhlmann (2012) showed that intervention data narrows the Markov equivalence class.
- Vink et al. (2020) show that the functional connectome remains a weak predictor of causal activity flow.
- Lee et al. (2017) demonstrate DCM validation using anesthesia-induced changes, showing that intervention-like conditional differences are important, not just observational fit.
- Revision:
- Rewritten `Active Inference / DCM / SCM / state-space / mechanistic circuit` as a competitive candidate set.
- Fixed `explicit candidate model space`, `family comparison`, `model recovery`, `held-out perturbation` as mandatory requirements.
- multiscale route has been lowered to `potential extension route` and removed from the default route.

### 3. The old `wiki/observation-to-estimation.md` was only a conceptual explanation and did not have an audit gate.

- Issue:
- There were definitions for forward problems, inverse problems, ESI, DCM, SCM, and causal equivalence classes, but there was no table showing which conditions would have to be met to stop the assertion.
- As a result, there was room for the step between `fits the observation` → `we know the internal state` → `we know the cause and effect` to be read weakly.
- Basis:
- Mikulan et al. (2020), Unnwongse et al. (2023), and Hao et al. (2025) show that the strength of source imaging depends on the external validation route.
- Feng et al. (2025) presented empirical Bayesian uncertainty quantification, but the body is `how to express uncertainty` instead of `solver name`.
- Hauser & Buhlmann (2012) clearly show that the strength of causal information obtained changes between observation only and intervention.
- Revision:
- The new version has been completely reorganized to `4 audit gates` (geometry, width visualization, candidate model set, external validation/intervention).
- Replaced with three pillars: `Audit by solver name`, `DCM is not an automatic discoverer`, `SCM is a language of intervention and equivalence classes remain only by observation`.

### 4. `measurement-and-modeling-terms.md` was also sufficient as an auxiliary page, but the discussion of equivalence classes and candidate set was missing.

- Issue:
- The previous version was useful for understanding the flow of `Observation→Organization→Estimation→Verification`.
- However, there were no supplements such as `candidate model dependence at the estimation stage` and `causal direction remains with observation alone`, and the explanation was a little weaker than `observation-to-estimation`.
- Revision:
- Rewritten to `Estimates are estimates and uncertainty and candidate model dependence remain`.
- Added DCM/SCM/equivalence class role difference as `2026-03 supplement`.

## Changes Made This Round

- `wiki/observation-to-estimation.md`
- Updated front matter with focus on technology and natural sciences
- Newly added `Four Audit Gates`, `ESI Validation Ladder`, `DCM Candidate Model Dependency`, `SCM and the Role of Interventions`, `site rule`, `References`
- `tech_roadmap.md`
- Withdraw `Bayesian Principles` in R1 and change to `Uncertainty + Sensitivity Analysis + External Validation`
- Changed R4 from `adoption of specific theory` to `model competition + intervention benchmark`
- Added `family / sensitivity / calibration / abstention` to R7
- Added source validation and causal identifiability documents to the bibliography.
- `wiki/measurement-and-modeling-terms.md`
- Added minimal synchronization fixes to compensate for `candidate model dependence` and `causal equivalence class`

## Deferred External-Dependency Tasks

- Site-wide re-audit of theory-heavy citations remaining in `perspective.md` and `tech_roadmap.md`
- Person in charge: AI / maintainer
- Prerequisite: inventory future-looking / theory-specific citations on all pages
- Completion condition: Theory-dependent descriptions that can be read as `default route` are organized according to the strength of published primary literature.

## References

- Wipf D, Nagarajan S. A unified Bayesian framework for MEG/EEG source imaging. NeuroImage. 2009.
  - https://doi.org/10.1016/j.neuroimage.2008.02.059
- Aydin U, Vorwerk J, Kupper P, et al. Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. Front Neurosci. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. Sci Data. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, Alhilani M, Asano E, et al. High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Feng Z, Mishne G, Hashemi A, et al. Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. IEEE Trans Med Imaging. 2025.
  - https://doi.org/10.1109/TMI.2025.3642620
- Friston KJ, Harrison L, Penny W. Dynamic causal modelling. NeuroImage. 2003.
  - https://doi.org/10.1016/S1053-8119(03)00202-7
- Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. NeuroImage. 2004.
  - https://doi.org/10.1016/j.neuroimage.2004.03.026
- Lee HL, Zahneisen B, Hugger T, et al. Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. NeuroImage. 2017.
  - https://doi.org/10.1016/j.neuroimage.2017.02.012
- Hauser A, Buhlmann P. Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. JMLR. 2012.
  - https://jmlr.org/papers/v13/hauser12a.html
- Vink JJ, Ramos-Nunez AI, Bellesi A, et al. The brain's functional connectome is a poor predictor of the brain's causal activity flow. PLoS Comput Biol. 2020.
  - https://doi.org/10.1371/journal.pcbi.1007866
