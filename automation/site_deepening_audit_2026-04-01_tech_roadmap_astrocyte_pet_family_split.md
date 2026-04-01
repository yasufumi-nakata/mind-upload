# Site Deepening Audit (2026-04-01, tech roadmap astrocyte PET family split)

## Scope

- Primary target:
  - `tech_roadmap.md`
- Secondary generated target:
  - `summary_booklet.md`
- Research scope:
  - technology
  - natural science
- Explicitly excluded:
  - philosophy
  - law

## Why This Topic Was Chosen

- `tech_roadmap.md` is one of the central public orientation pages on the site.
- On 2026-04-01, the site already had stricter wording in other places about not collapsing human proxy families.
- However, `tech_roadmap.md` still left a comparatively coarse `human astrocyte-related PET` row in two core tables.
- That was technically weak because the roadmap is where readers learn the site's dependency structure. If the roadmap compresses route families, later stop-rules look optional.

## Evidence-Based Critique

### 1. `astrocyte PET` was still too coarse for a central roadmap page

- Problem:
  - The roadmap still let a single family label stand for several distinct inferential objects.
- Why this is technically weak:
  - The relevant literature does not answer one shared question.
  - It answers at least:
    - first-in-human target validation
    - disease-context contrast
    - tracer-family quantification
    - whole-body biodistribution / operational burden
    - target-class separation
    - cohort / smoking / severity ceiling

### 2. MAO-B target validation is not the same thing as MAO-B disease contrast

- Primary evidence:
  - Villemagne et al. (2022, DOI `10.2967/jnumed.121.263254`) showed first-in-human SMBT-1 brain entry, reversible kinetics, and strong selegiline blockade, which is a tracer-family target-validation result.
  - Villemagne et al. (2022, DOI `10.2967/jnumed.121.263255`) then studied 77 participants across the AD continuum and showed higher cortical SMBT-1 binding in Aβ-positive cognitively normal and AD groups, which is a disease-context result.
- Critique:
  - A target-validation paper and an AD-spectrum contrast paper do not carry the same claim.
  - Treating them as one row quietly promotes a route-specific tracer family into a generic astrocyte-state meter.

### 3. Quantification and biodistribution are separate burdens inside the same MAO-B family

- Primary evidence:
  - Hiraoka et al. (2025, DOI `10.1007/s12149-025-02083-y`) showed that SMBT-1 quantification depends on time window and reference-region choices relative to kinetic modeling.
  - Mesfin et al. (2026, DOI `10.1007/s12149-025-02144-2`) showed that whole-body SMBT-1 distribution has its own operational burden, including strong early uptake in multiple organs and late gallbladder accumulation.
- Critique:
  - These are not disease-evidence papers.
  - They answer how the tracer family must be quantified and what acquisition burden it carries.
  - A roadmap that compresses these into one disease-facing row hides the route burden exactly where readers need to see it.

### 4. Even inside MAO-B, tracer families and covariate ceilings differ

- Primary evidence:
  - Matsuoka et al. (2026, DOI `10.1007/s00259-025-07542-2`) developed a simplified no-arterial-blood quantification route for 11C-SL25.1188 in AD and MCI due to AD, which is not the same route as SMBT-1.
  - Best et al. (2026, DOI `10.1038/s41380-025-03355-9`) showed in AUD that 11C-SL25.1188 binding is highly variable and strongly conditioned by smoking and severity.
  - Jaisa-Aad et al. (2024, DOI `10.1007/s00401-024-02712-2`) showed in postmortem tissue that MAO-B is a promising but bounded biomarker of reactive astrogliosis rather than a route-free astrocyte scalar.
- Critique:
  - `MAO-B PET` is not one portable readout.
  - Tracer family, cohort, and covariates materially change what can be claimed.

### 5. I2BS is a different target class, not a substitute row for MAO-B

- Primary evidence:
  - Tyacke et al. (2018, DOI `10.2967/jnumed.118.208009`) established first-in-human 11C-BU99008 behavior with idazoxan blockade and no block by isocarboxazid, supporting I2BS-specific interpretation rather than MAO-B equivalence.
  - Livingston et al. (2022, DOI `10.1038/s41380-021-01429-y`) showed that 11C-BU99008 patterns in cognitively impaired individuals vary by region and disease stage.
- Critique:
  - I2BS is not a drop-in `second astrocyte tracer`.
  - If the roadmap leaves MAO-B and I2BS inside one shared row, readers can incorrectly infer target-class interchangeability.

## Changes Executed In This Session

### `tech_roadmap.md`

- Updated `last_updated` to `2026-04-01`.
- Added front-matter stop-lines so the public summary now says astrocyte-related PET must be split by target class, tracer family, route role, and covariate ceiling.
- Replaced the old single `human astrocyte-related PET` row in the M1 comparison table with four rows:
  - MAO-B target-validation route
  - MAO-B disease-context route
  - MAO-B quantification / covariate route
  - I2BS route
- Added a new `2026-04-01 addendum` explaining why `astrocyte PET` cannot remain one roadmap row.
- Updated the existing M1 addendum so it now names Mesfin (2026), Matsuoka (2026), and Jaisa-Aad (2024) alongside the earlier astrocyte-PET references.
- Updated the M3 multimodal paragraph so the human proxy list now reflects the internal split of the astrocyte-PET family.
- Replaced the old single `Human astrocyte-related PET` row in the M3 human-observability table with five rows:
  - SMBT-1 first-in-human target validation
  - SMBT-1 AD-spectrum contrast
  - SMBT-1 quantification / biodistribution burden
  - SL25.1188 disease / severity route
  - I2BS astrocyte-related PET
- Added references for Mesfin et al. (2026) and Matsuoka et al. (2026).

## External Dependency Tasks

- None.
  - This session only required literature verification, local file edits, generated-file refresh, validation, and Git operations that are executable in the current environment.

## References

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
2. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263255
3. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
4. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
5. Matsuoka K, Takado Y, Kimura Y, et al. Quantification of monoamine oxidase B expression with 11C-SL25.1188 for imaging reactive astrocytes in patients with Alzheimer's disease. *European Journal of Nuclear Medicine and Molecular Imaging*. 2026.
   - https://doi.org/10.1007/s00259-025-07542-2
6. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
7. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
8. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
9. Jaisa-Aad M, Munoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
