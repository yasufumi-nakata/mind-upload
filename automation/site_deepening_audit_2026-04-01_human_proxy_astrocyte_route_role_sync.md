# Site Deepening Audit (2026-04-01, Human Proxy Astrocyte Route-Role Sync)

## Scope

- Primary target: `wiki/human-proxy-composition.md`
- Secondary target: `wiki/measurement-stack-and-claim-ceiling.md`

## Why This Topic Was Chosen

- The site had already improved its astrocyte PET wording on several front-door pages on 2026-03-31.
- However, the two central rule pages still underdescribed the same route family.
- That inconsistency mattered because these two pages define how readers are allowed to compose human proxy evidence across the whole site.
- As long as they still compressed astrocyte PET to `MAO-B versus I2BS` or to one generic `target-defined astrocyte PET` row, the site's stricter front-door wording remained technically unstable.

## Evidence-Based Critique

### 1. The central rule pages still collapsed route roles inside the SMBT-1 / MAO-B family

- Problem:
  - The public site had already started to separate astrocyte PET by target class and route role elsewhere.
  - But the central composition and claim-ceiling pages still allowed readers to treat `SMBT-1 first-in-human target validation`, `SMBT-1 AD-spectrum disease contrast`, `SMBT-1 brain quantification`, and `SMBT-1 whole-body biodistribution` as one common MAO-B line.
- Why this is technically weak:
  - These papers do not answer the same question.
  - One paper establishes that a tracer binds the intended target in humans.
  - Another tests disease-context contrast.
  - Another tests brain-side quantification choices.
  - Another fixes whole-body biodistribution burden.
  - Treating them as one line silently promotes the route beyond what the literature supports.
- Primary evidence:
  - Villemagne et al. (2022, DOI `10.2967/jnumed.121.263254`) establish first-in-human SMBT-1 MAO-B target validation.
  - Villemagne et al. (2022, DOI `10.2967/jnumed.121.263255`) establish Alzheimer-spectrum disease-context contrast.
  - Hiraoka et al. (2025, DOI `10.1007/s12149-025-02083-y`) establish the brain-quantification problem.
  - Mesfin et al. (2026, DOI `10.1007/s12149-025-02144-2`) establish the separate whole-body biodistribution burden.

### 2. The site's central tables were still too coarse for family-internal comparison logic

- Problem:
  - The `human-proxy-composition` route matrix and the `measurement-stack-and-claim-ceiling` ladder still contained one generic astrocyte row.
  - That row was inconsistent with the site's stricter treatment of `SV2A`, `myelin`, and `clearance` families.
- Why this is technically weak:
  - The whole point of the central pages is to prevent family-label collapse.
  - Leaving astrocyte PET unsplit in those tables made the rule look optional exactly where it needed to be strongest.
- Required correction:
  - The family-internal logic had to be promoted into the tables themselves, not only into supporting prose.

### 3. Cross-target separation was still necessary, but not sufficient

- Problem:
  - `MAO-B` versus `I2BS` separation was already an improvement.
  - But it still left the false impression that everything inside the MAO-B family was one reusable proxy row.
- Why this is technically weak:
  - `I2BS` is a different target class from `MAO-B`.
  - But even inside `MAO-B`, disease regime, quantification route, and dosimetry remain non-interchangeable.
- Primary evidence:
  - Tyacke et al. (2018, DOI `10.2967/jnumed.118.208009`) establish first-in-human I2BS pharmacology.
  - Livingston et al. (2022, DOI `10.1038/s41380-021-01429-y`) extend I2BS-related imaging into cognitively impaired humans.

### 4. Cohort and covariate dependence inside MAO-B routes still had to remain explicit

- Problem:
  - Once `MAO-B astrocyte PET` is named, readers can still overread it as one generic astrocyte-burden meter.
- Why this is technically weak:
  - The literature still shows cohort- and pathology-conditioned ceilings even inside the same target class.
- Primary evidence:
  - Best et al. (2026, DOI `10.1038/s41380-025-03355-9`) show severity- and smoking-dependent interpretation in MAO-B PET for alcohol use disorder.
  - Jaisa-Aad et al. (2024, DOI `10.1007/s00401-024-02712-2`) show that MAO-B is a bounded biomarker of reactive astrogliosis rather than a route-free astrocyte-state scalar.

## Changes Executed In This Session

- `wiki/human-proxy-composition.md`
  - Updated front matter and summary bullets so astrocyte PET is treated as a `target / route-role split` rather than one family label.
  - Added a new 2026-04-01 correction note explaining why first-in-human validation, AD-context contrast, brain quantification, whole-body biodistribution, and I2BS imaging cannot share one bundle row.
  - Replaced the old single astrocyte row in the route matrix with five rows:
    - SMBT-1 first-in-human MAO-B target validation
    - SMBT-1 AD-spectrum disease context
    - SMBT-1 brain quantification
    - SMBT-1 whole-body biodistribution
    - I2BS astrocyte PET
  - Expanded the family-internal-collapse rule so astrocyte PET is treated in the same way as SV2A, myelin, and clearance families.
  - Updated the three-axis table and causal-bridge paragraph so the same route-role split survives into calibrator-role and bridge logic.
- `wiki/measurement-stack-and-claim-ceiling.md`
  - Updated `last_updated` and page highlights so astrocyte PET is explicitly named as a non-collapsible audit family.
  - Rewrote the section-7 maintenance-state paragraph so SMBT-1 target validation, disease-context contrast, brain quantification, and whole-body biodistribution are no longer compressed into one MAO-B row.
  - Replaced the old two-row astrocyte block with five rows at the claim-ceiling table.
  - Updated the proxy-class / operational-maturity / calibrator-role note and the site rule so `MAO-B target-validation / disease-context / brain-quantification / whole-body-biodistribution` now remain distinct proxy classes.

## External Dependency Tasks

- None.
  - This session only required literature review, repository edits, local export/build verification, and Git operations executable in the current environment.

## References

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of ^18F-SMBT-1, a Novel ^18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
2. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with ^18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
3. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [^18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
4. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [^18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
5. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of ^11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
6. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel ^11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
7. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [^11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
8. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
