---
title: "2026-04-03 site deepening audit: astrocyte PET SL25 route sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **site-wide overcompression inside human astrocyte-related PET**.

By 2026-04-03, `tech_roadmap.md` already preserved a stricter split:

- `SMBT-1` first-in-human target validation
- `SMBT-1` AD-spectrum disease context
- `SMBT-1` brain quantification
- `SMBT-1` whole-body biodistribution
- `SL25.1188` simplified / arterial-free AD quantification
- `SL25.1188` severity- and smoking-conditioned AUD interpretation
- `I2BS` as a different target class

However, several front-door and route-rule pages were still weaker than that internal standard, and one FAQ table still misclassified `Best et al. (2026)` under `I2BS`.

# Why This Needed Correction

## 1. `Best et al. (2026)` is not an `I2BS` paper

- [Best et al. (2026)](https://doi.org/10.1038/s41380-025-03355-9) used **[11C]SL25.1188**, which is an **MAO-B tracer**.
- Therefore, placing it under an `I2BS` row was a taxonomy error, not merely a wording preference.
- That error matters because the site's public logic depends on readers keeping **target class**, **tracer family**, and **route role** separate.

## 2. `MAO-B PET` had become too coarse even after the older split

- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) established **SMBT-1 first-in-human target validation**.
- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) established **SMBT-1 AD-spectrum disease context**.
- [Hiraoka et al. (2025)](https://doi.org/10.1007/s12149-025-02083-y) established **SMBT-1 brain quantification burden**.
- [Mesfin et al. (2026)](https://doi.org/10.1007/s12149-025-02144-2) established **SMBT-1 whole-body biodistribution / tracer-burden burden**.
- [Matsuoka et al. (2026)](https://doi.org/10.1007/s00259-025-07542-2) established a distinct **[11C]SL25.1188 simplified / arterial-free quantification route in AD**, rather than a simple reuse of SMBT-1 assumptions.
- [Best et al. (2026)](https://doi.org/10.1038/s41380-025-03355-9) established that **SL25.1188 MAO-B interpretation in AUD is severity- and cigarette-use-conditioned**, and not one monotone scalar.

Therefore, saying only `MAO-B PET` was still overcompressed. The site needed one more split: **inside the MAO-B family itself**.

## 3. The public front door had drifted away from the stricter internal rule

Before this run:

- `tech_roadmap.md` already carried the newer `SL25.1188` split
- several public pages still omitted `Matsuoka et al. (2026)`
- some pages still let readers infer that `SMBT-1`, `SL25.1188`, and `I2BS` were one ladder with only minor wording differences

That was technically unstable because the site's stop rules were already stricter than some of its most visible pages.

# Changes Executed In This Session

## Front-door pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - fixed the misclassification of `Best et al. (2026)` from `I2BS` to `SL25.1188 MAO-B`
  - added a new explicit `SL25.1188 MAO-B disease / severity routes` row
  - expanded the FAQ stop line so `MAO-B PET` now splits by tracer family as well as route role
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - upgraded the beginner astrocyte-PET explanation from `MAO-B vs I2BS` to `SMBT-1 vs SL25.1188 vs I2BS`
  - rewrote the human astrocyte PET row as a family of route types rather than one generic human PET row
- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - synchronized the landing-page astrocyte notes to include `Mesfin` and `Matsuoka`
  - made explicit that `SL25.1188` has its own quantification and covariate ceiling

## Literature and route-rule pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md)
  - updated the 2025-2026 technical reading lane so astrocyte PET is no longer a single `target-defined` line
  - added `Matsuoka et al. (2026)` to the human observability ladder
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/human-proxy-composition.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/human-proxy-composition.md)
  - added a dedicated `Human SL25.1188 MAO-B disease / severity route`
  - removed `Best et al. (2026)` from the `SMBT-1 AD-spectrum` row
  - updated the composition note and references so the family-internal split is explicit
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md)
  - updated the astrocyte route card so human astrocyte PET is now explicitly `target-defined`, `tracer-family-separated`, and `route-role-separated`
  - added `Matsuoka et al. (2026)` to both the argument and the references
- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - updated the astrocyte evidence addendum so the verification rule now names `tracer family` explicitly

# Verification

- Ran `ruby scripts/build_summary_booklet.rb`.
- Ran `git diff --check`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified the repository now contains `SL25.1188 MAO-B disease / severity routes` and `Matsuoka et al. (2026)` on the corrected public pages.

# External Dependency Tasks

- None.
  - This run stayed fully inside executable repository work: literature verification, markdown updates, generated summary rebuild, local site build, and Git operations.

# References

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
6. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
7. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
8. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel 11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
9. Jaisa-Aad M, Muñoz-Castro C, Healey MA, Hyman BT, Serrano-Pozo A. Characterization of monoamine oxidase-B (MAO-B) as a biomarker of reactive astrogliosis in Alzheimer's disease and related dementias. *Acta Neuropathologica*. 2024.
   - https://doi.org/10.1007/s00401-024-02712-2
