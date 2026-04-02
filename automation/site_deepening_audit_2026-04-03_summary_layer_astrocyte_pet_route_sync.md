---
title: "2026-04-03 site deepening audit: summary-layer astrocyte PET route sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **summary-layer compression bug inside human astrocyte-related PET**.

By 2026-04-03, the body text and deep route-rule pages already separated:

- `SMBT-1` first-in-human MAO-B target validation
- `SMBT-1` Alzheimer-spectrum disease-context contrast
- `SMBT-1` brain-side quantification burden
- `SMBT-1` whole-body biodistribution burden
- `SL25.1188` simplified / arterial-free MAO-B quantification in AD
- `SL25.1188` severity- and smoking-conditioned MAO-B interpretation in AUD
- `I2BS` as a different target class

However, the summary-facing front matter still allowed those routes to collapse back into phrases such as `target-defined astrocyte PET` or `MAO-B or I2BS`, and the auto-generated booklet inherited that weaker language.

# Why This Needed Correction

## 1. The current primary literature does not support one generic `human astrocyte PET` row

- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254) is a **first-in-human SMBT-1 MAO-B target-validation** paper.
- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) is an **SMBT-1 AD-spectrum disease-context** paper.
- [Hiraoka et al. (2025)](https://doi.org/10.1007/s12149-025-02083-y) is an **SMBT-1 brain-quantification** paper.
- [Mesfin et al. (2026)](https://doi.org/10.1007/s12149-025-02144-2) is an **SMBT-1 whole-body biodistribution / tracer-burden** paper.
- [Matsuoka et al. (2026)](https://doi.org/10.1007/s00259-025-07542-2) is an **SL25.1188 simplified / arterial-free MAO-B quantification** paper in AD.
- [Best et al. (2026)](https://doi.org/10.1038/s41380-025-03355-9) is an **SL25.1188 severity- and smoking-conditioned MAO-B interpretation** paper in AUD.
- [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) and [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) define an **I2BS** route, which is a different target class from MAO-B.
- [Jaisa-Aad et al. (2024)](https://doi.org/10.1007/s00401-024-02712-2) further shows that even MAO-B itself is a promising but bounded reactive-astrogliosis biomarker rather than a route-free astrocyte-state scalar.

Therefore, a summary phrase that compresses these into one `target-defined astrocyte PET` line is weaker than the evidence standard already enforced elsewhere on the site.

## 2. The summary layer had drifted away from the route-card logic

Before this run:

- `FAQ`, `WBE 101`, the route-rule wiki, and parts of `tech_roadmap.md` already distinguished tracer families and route roles
- the front-matter summary bullets in `index.md`, `wbe_101.md`, and `tech_roadmap.md` still used weaker family labels
- `summary_booklet.md` inherited that weaker language because it is auto-generated from front matter

That drift mattered because the summary booklet is a front-door artifact. If the summary layer is weaker than the route-card layer, a reader can re-import the very shortcut that deeper pages already block.

# Changes Executed In This Session

## Summary-source pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - replaced the compressed `target-defined astrocyte PET` summary line with explicit `SMBT-1`, `SL25.1188`, and `I2BS` route families
  - tightened the astrocyte summary bullets so `route role` remains visible at the landing-page layer
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - updated summary-facing bullets so the human observability ladder now keeps `SMBT-1`, `SL25.1188`, and `I2BS` distinct in the high-level layer
  - corrected the front-door sentence that still treated human astrocyte PET as a single target-defined row
- [`/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md`](/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md)
  - updated the roadmap front matter so `astrocyte PET` is no longer summarized as one interchangeable family
  - advanced `last_updated` to `2026-04-03` and synced the note text to this summary-layer pass

## Generated output

- [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md)
  - regenerated from source pages so the public booklet now inherits the stricter tracer-family and route-role split

# Main Critique

The site's deep logic was already correct, but the summary layer was not yet carrying its own scientific burden. In a project whose central claim is that **route-family and claim-ceiling discipline matter**, letting the booklet collapse `SMBT-1`, `SL25.1188`, and `I2BS` back into one summary noun reintroduced a scientifically important shortcut. The fix was therefore not to add a brand-new deep page; it was to restore **consistency between the summary layer and the verified route-card layer**.

# Verification

- Ran `ruby scripts/build_summary_booklet.rb`.
- Ran `git diff --check`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified the generated booklet and built HTML now contain `SL25.1188` and no longer depend on the compressed `target-defined astrocyte PET` wording at the summary layer.

# External Dependency Tasks

- None.
  - This session stayed inside executable repository work: literature verification, front-matter edits, summary regeneration, local build validation, and Git operations.

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
