# Site Deepening Audit (2026-03-30, effective-connectivity processing-policy split)

## Target

- Primary target:
  - `wiki/observation-to-estimation.md`
- Consistency targets:
  - `verification.md`
  - `faq.md`
  - `mind_uploading_papers.md`
- Scope:
  - technology / natural science only

## Why This Area Was Chosen

- The site already had a strong stop rule for `effective connectivity / DCM`: it separated
  - candidate model space
  - observed-subsystem closure / latent confounds
  - node-definition policy
  - sampling / transform sensitivity
  - validation
  - reliability
- However, one compression still remained.
- The public text still made it too easy to read `whole-brain`, `fast`, or `reproducible` directed-connectivity results as if the remaining main issue were only `candidate model comparison`.
- Current primary literature shows a stronger claim ceiling:
  - reasonable `processing / first-level design policy` can itself move the inferred edges and the associated parameter certainty
  - reliability is still conditional on `scan duration` and `sample size`
- Therefore the public route card needed one more split before the site's criticism became fully operational.

## Evidence-Based Critique

### 1. Candidate-model disclosure alone was still too narrow

- The site already cited
  - Penny et al. (2004)
  - Rosa et al. (2012)
  - Frässle et al. (2021)
  - Jafarian et al. (2024)
  - Novelli et al. (2025)
  - Yan et al. (2026)
- Those sources already support the claim that
  - model comparison is conditional
  - scaling is not automatic causal discovery
  - latent confounders and sampling remain open
- But that still left a missing operational question:
  - what happens when the same paper family changes the `reasonable analysis recipe` rather than the model family?

### 2. Primary literature now shows that preprocessing / first-level design is not mere housekeeping

- [Almgren et al. (2020)](https://doi.org/10.1016/j.neuroimage.2019.116435) directly studied the effect of global signal regression on DCM noise and effective-connectivity estimates from resting-state fMRI.
- [Zhang et al. (2024)](https://doi.org/10.1002/hbm.26751) showed that for task-fMRI DCM, reasonable choices such as
  - GLM design
  - activation contrast
  - GSR policy
  - significance-thresholding approach
  can materially change group-averaged effective-connectivity patterns and parameter certainty.

Critique:

- Without a separate `processing / first-level design policy` field, the site still allowed a subtle overread:
  - a graph that survives one named DCM family could be mistaken for a graph that is robust across reasonable analysis recipes
- The primary literature does not support that shortcut.

### 3. Conditional reproducibility also needed a more exact reading

- [Frässle et al. (2016)](https://doi.org/10.1002/hbm.23061) and [Jafarian et al. (2024)](https://doi.org/10.1002/hbm.26782) already supported the idea that effective-connectivity reliability can be nontrivial under tightly controlled settings.
- [Ma et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120604) sharpened that point by showing that reliability still depends on
  - scan duration
  - sample size
  under explicit resting-state fMRI DCM analyses.

Critique:

- Therefore `reliable` must still be read as
  - reliability within a named acquisition / duration / sample-size regime
  rather than
  - general portability of a causal graph.

## Main Conclusion

- The safer 2026-03-30 site rule is:
  - separate `tractability`
  - separate `processing-policy sensitivity`
  - separate `conditional reliability`
  - separate `causal validity`
- A dense, scalable, or reproducible DCM graph is still not discovered wiring unless those axes are disclosed independently.

## Changes Executed In This Session

- `wiki/observation-to-estimation.md`
  - updated `last_updated`
  - added a new deepening note on processing / first-level design policy
  - added `Processing / first-level design policy` to the effective-connectivity route card
  - tightened the final stop rule so `one preprocessing recipe` is not overread as robustness
  - added references for Almgren 2020, Zhang 2024, and Ma 2024
- `verification.md`
  - synchronized the top-level stop rule and route-card summary with the new processing-policy split
  - revised the note-box so effective-connectivity claims now require partial-observation, processing-policy, and sampling audits
  - added inline support from Zhang 2024 and Ma 2024
  - added the new references
- `faq.md`
  - revised the DCM / effective-connectivity answer so it now names processing / first-level design policy as a separate disclosure field
  - added Zhang 2024 and Ma 2024 to the criticism and references
- `mind_uploading_papers.md`
  - tightened the technical fast-lane row for effective connectivity / DCM
  - rewrote the route-card note so readers now separate tractability, processing-policy sensitivity, conditional reliability, and causal validity

## Misreadings Now Stopped More Explicitly

- `whole-brain DCM` = discovered causal wiring
- `fast regression DCM` = solved identifiability
- `one reasonable preprocessing recipe` = preprocessing-robust edge direction
- `good test-retest under matched conditions` = condition-general portability
- `candidate-model comparison` = the only remaining uncertainty layer

## Verification

- Planned verification for this session:
  - `git diff --check`
  - `env VERIFY_GITHUB_WIKI_BUILD=1 ./scripts/verify_github_wiki_toolchain.sh`
  - follow-up diff inspection before commit / push

## External Dependency Tasks

- None
  - This change is fully executable inside the current session: literature confirmation, public text revision, verification, commit, and push.

## References

1. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
2. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
3. Almgren H, Van de Steen F, Razi A, Friston K, Marinazzo D. The effect of global signal regression on DCM estimates of noise and effective connectivity from resting state fMRI. *NeuroImage*. 2020;208:116435.
   - https://doi.org/10.1016/j.neuroimage.2019.116435
4. Frässle S, Manjaly ZM, Do CT, Kasper L, Pruessmann KP, Stephan KE. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021;225:117491.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
5. Zhang S, Jung K, Langner R, Florin E, Eickhoff SB, Popovych OV. Impact of data processing varieties on DCM estimates of effective connectivity from task-fMRI. *Human Brain Mapping*. 2024;45(8):e26751.
   - https://doi.org/10.1002/hbm.26751
6. Jafarian A, Assem MK, Kocagoncu E, et al. Reliability of dynamic causal modelling of resting-state magnetoencephalography. *Human Brain Mapping*. 2024.
   - https://doi.org/10.1002/hbm.26782
7. Ma L, Braun SE, Steinberg JL, Bjork JM, Martin CE, Keen LD II, Moeller FG. Effect of scanning duration and sample size on reliability in resting state fMRI dynamic causal modeling analysis. *NeuroImage*. 2024;292:120604.
   - https://doi.org/10.1016/j.neuroimage.2024.120604
8. Wu H, Hu X, Zeng Y. A fast dynamic causal modeling regression method for fMRI. *NeuroImage*. 2024;304:120954.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
9. Novelli L, Barnett L, Seth AK, Razi A. Minimum-Phase Property of the Hemodynamic Response Function, and Implications for Granger Causality in fMRI. *Human Brain Mapping*. 2025;46(10):e70285.
   - https://doi.org/10.1002/hbm.70285
10. Yan J, Zhang S-W, Zhang C, Huang W, Shi J, Chen L. Dynamical Causality under Latent Confounders for Biological Network Reconstruction. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. 2026.
   - https://doi.org/10.1109/TPAMI.2026.3658839
