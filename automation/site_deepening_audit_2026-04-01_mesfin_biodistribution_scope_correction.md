# Site Deepening Audit (2026-04-01, Mesfin SMBT-1 Biodistribution Scope Correction)

## Scope

- Public targets:
  - `faq.md`
  - `wbe_101.md`
  - `verification.md`
  - `mind_uploading_papers.md`
  - `wiki/mind-upload-basics.md`
  - `wiki/human-proxy-composition.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Internal targets:
  - prior astrocyte PET route-role audit notes under `automation/`

## Why This Topic Was Chosen

- By 2026-04-01, `Mesfin et al. (2026)` had become a route-role anchor across both front-door pages and central rule pages.
- That made one narrow factual overread unusually costly: if the paper's evidential role is named too broadly, the entire `SMBT-1 / MAO-B` route-role matrix becomes internally inconsistent.
- The site's strongest recent improvement has been to separate `target`, `route role`, `quantification regime`, and `cohort / covariate regime`. A mislabeled Mesfin row re-collapses those gains.

## Evidence-Based Critique

### 1. What the primary paper directly studies

- The article title is `Whole-body biodistribution of [18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans`.
- The abstract objective is to observe `whole-body biodistribution` and evaluate `peripheral MAO-B expression` in healthy volunteers.
- The methods describe `six healthy subjects` who underwent `nine dynamic PET scans over 5.5 h`.
- The results emphasize early uptake in kidneys, liver, heart, and stomach, plus delayed gallbladder / intestinal uptake.
- The conclusion states that `[18F]SMBT-1 exhibited favorable reversible kinetics in the whole-body biodistribution assessment`.
- Therefore, the direct evidential object is a `whole-body biodistribution / tracer-burden route`.

### 2. Why calling it a dosimetry route is too strong

- The paper itself is not framed as a brain-side quantification paper. That role belongs to `Hiraoka et al. (2025)`.
- The paper itself is not framed as an AD-spectrum disease-context paper. That role belongs to `Villemagne et al. (2022, DOI 10.2967/jnumed.121.263255)`.
- Inference from the paper's own title, objective, methods, results, and conclusion:
  - the site should not promote `Mesfin et al. (2026)` to a generic `whole-body dosimetry route` label, because the paper's explicit evidential role is biodistribution and systemic tracer burden.
- That inference is narrower and better supported than the old wording.

### 3. Why this mattered for the site's broader logic

- Once `Mesfin et al. (2026)` is misnamed, the reader can silently treat one citation as if it had already settled:
  - first-in-human target validation
  - disease-context contrast
  - brain quantification
  - whole-body deployment burden
- The literature does not support that compression.
- The practical effect is that `MAO-B astrocyte PET` starts to look more route-complete and deployment-ready than it really is.

## Changes Executed In This Session

- Rewrote public-facing mentions of `Mesfin et al. (2026)` so the route is now named `whole-body biodistribution` or `whole-body biodistribution / tracer-burden`, not `whole-body dosimetry`.
- Updated central rule pages so the same correction survives into:
  - family-internal route matrices
  - claim-ceiling tables
  - calibrator-role language
  - causal-bridge language
- Corrected prior automation audit notes so they no longer preserve the same overread in the repository history.
- Standardized remaining `Mesfin et al. (2026)` links to the DOI URL where touched.

## External Dependency Tasks

- None.
  - The work only required literature review, repository edits, local generation / verification, and Git operations executable in this session.

## References

1. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [^18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
2. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of ^18F-SMBT-1, a Novel ^18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
3. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with ^18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
4. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [^18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
5. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of ^11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
6. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel ^11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
7. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [^11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
8. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
