# Site Deepening Audit (2026-04-02, glossary effective-connectivity route-card sync)

## Target

- Main public page:
  - `glossary.md`
- Scope:
  - technology
  - natural science
- Explicitly excluded:
  - philosophy
  - law
- Explicitly skipped by request:
  - `issue.md`

## Why This Topic Was Chosen

- The site's deeper pages had already become strict about `effective connectivity / DCM`:
  - `FAQ` already required
    - candidate model space
    - observed-subsystem closure / latent-confound audit
    - node-definition policy
    - processing / first-level design policy
    - sampling / transformation sensitivity
    - validation
    - reliability window
    - abstention boundary
  - `wiki/observation-to-estimation.md` already exposed the same route-card logic.
- However, the public `glossary.md` entry point still defined:
  - `Effective connectivity`
  - `DCM`
  only in broad terms such as `candidate model space`, `validation`, and `reliability`.
- That mismatch reintroduced a front-door compression bug:
  - a beginner could read a directed graph as if the main remaining issue were only `which model family won`,
  - while the rest of the site had already moved to the stricter view that omitted nodes, ROI policy, first-level design, sampling transforms, and regime-matched reliability are separate failure modes.

## Main Conclusion

- The most important improvement opportunity in the current repo was not a brand-new route family.
- It was a front-door synchronization bug: `glossary.md` still underdescribed what the site now means by an effective-connectivity claim.
- Therefore the right fix was to make the `effective-connectivity route card` visible at the glossary level, not only in deep technical pages.

## Evidence-Based Critique

### 1. Faster or larger-scale DCM does not remove model-conditioning

- Evidence:
  - [Frässle et al. (2021)](https://pubmed.ncbi.nlm.nih.gov/33115664/)
  - [Wu et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120954)
- Critique:
  - Whole-brain and faster effective-connectivity estimation are genuine advances in tractability and scale.
  - They do **not** convert directed-connectivity output into route-free causal-wiring discovery.
  - Therefore a glossary definition that stops at `candidate model space` is too weak for the site's present scientific standard.

### 2. Node definition and first-level processing are not cosmetic choices

- Evidence:
  - [Smith et al. (2011)](https://doi.org/10.1016/j.neuroimage.2010.08.063)
  - [Zhang et al. (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11167406/)
- Critique:
  - Smith et al. showed that functionally inaccurate ROIs can seriously damage network estimation.
  - Zhang et al. showed that reasonable task-fMRI processing choices, especially GLM design and activation contrast, can materially change effective-connectivity strength and parameter certainty.
  - Therefore `node-definition policy` and `processing / first-level design policy` need their own front-door terms.

### 3. Hidden inputs, hidden nodes, and subsampling remain separate causal-audit problems

- Evidence:
  - [Barnett & Seth (2017)](https://doi.org/10.1016/j.jneumeth.2016.10.016)
  - [Villaverde et al. (2019)](https://doi.org/10.1098/rsif.2019.0043)
  - [Yan et al. (2026)](https://doi.org/10.1109/TPAMI.2026.3658839)
- Critique:
  - Barnett & Seth showed that subsampling can create detectability black spots and sweet spots.
  - Villaverde et al. showed that states, inputs, and parameters often need to be assessed jointly rather than as separable afterthoughts.
  - Yan et al. showed that latent confounders remain an active biological-network-reconstruction problem.
  - Therefore `observed-subsystem closure / latent-confound audit` and `sampling / transformation sensitivity` cannot stay implicit at the glossary level.

### 4. Reliability is regime-conditional, not a method-wide guarantee

- Evidence:
  - [Jafarian et al. (2024)](https://research.birmingham.ac.uk/en/publications/reliability-of-dynamic-causal-modelling-of-restingstate-magnetoen/)
- Critique:
  - Jafarian et al. found strong reliability for resting-state MEG DCM under tightly matched conditions and sessions acquired close in time.
  - That is important positive evidence, but it is still a named acquisition regime, not a route-free guarantee that effective connectivity is simply reliable.
  - Therefore `reliability window` needs to be a separate term, not a vague property silently attached to `DCM`.

## Changes Executed In This Session

### `glossary.md`

- Updated front-matter highlights and known-points so the page now explicitly states that the effective-connectivity stop line includes:
  - effective-connectivity route card
  - observed-subsystem closure / latent-confound audit
  - node-definition policy
  - processing / first-level design policy
  - sampling / transformation sensitivity
  - reliability window
  - model recovery / family comparison
- Added a new front-door note box:
  - `When effective-connectivity words start sounding too close to discovered wiring`
- Tightened the existing definitions for:
  - `Effective connectivity`
  - `DCM`
- Added new glossary rows for:
  - `Effective-connectivity route card`
  - `Observed-subsystem closure / latent-confound audit`
  - `Node-definition policy`
  - `Processing / first-level design policy`
  - `Sampling / transformation sensitivity`
  - `Model recovery / family comparison`
  - `Reliability window`

## Misreadings Stopped By This Change

- `effective connectivity` = discovered causal wiring
- `DCM` = true circuit finder
- `candidate model space disclosed` = main failure mode solved
- `same graph under one preprocessing policy` = robust route-independent causal result
- `reported reliability` = method-wide guarantee outside the acquisition regime used

## Verification

- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `git diff --check`
- `rg -n "Effective-connectivity route card|Observed-subsystem closure / latent-confound audit|Processing / first-level design policy|Reliability window" glossary.md _site/glossary.html`

## External Dependency Tasks

- None.
  - This session was fully executable through web verification of primary literature, repository edits, local build validation, and Git operations.

## References

1. Frässle S, Manjaly ZM, Do CT, et al. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021.
   - https://pubmed.ncbi.nlm.nih.gov/33115664/
2. Wu X, Hu X, Liu X, et al. Whole-brain effective connectivity analysis at scale. *NeuroImage*. 2024.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
3. Smith SM, Miller KL, Salimi-Khorshidi G, et al. Network modelling methods for FMRI. *NeuroImage*. 2011.
   - https://doi.org/10.1016/j.neuroimage.2010.08.063
4. Zhang S, Jung K, Langner R, et al. Impact of data processing varieties on DCM estimates of effective connectivity from task-fMRI. *Human Brain Mapping*. 2024.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC11167406/
5. Barnett L, Seth AK. Detectability of Granger causality for subsampled continuous-time neurophysiological processes. *Journal of Neuroscience Methods*. 2017.
   - https://doi.org/10.1016/j.jneumeth.2016.10.016
6. Villaverde AF, Evans ND, Chappell MJ, Banga JR. Input-dependent structural identifiability of nonlinear systems. *Journal of the Royal Society Interface*. 2019.
   - https://doi.org/10.1098/rsif.2019.0043
7. Jafarian A, Assem MK, Kocagoncu E, et al. Reliability of dynamic causal modelling of resting-state magnetoencephalography. *Human Brain Mapping*. 2024.
   - https://research.birmingham.ac.uk/en/publications/reliability-of-dynamic-causal-modelling-of-restingstate-magnetoen/
8. Yan X, et al. Latent confounders in biological network reconstruction. *IEEE Transactions on Pattern Analysis and Machine Intelligence*. 2026.
   - https://doi.org/10.1109/TPAMI.2026.3658839
