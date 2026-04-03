---
title: "2026-04-03 site deepening audit: measurement-stack human proxy route sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **central rule-page lag inside the human maintenance-state ladder**.

Several other public pages had already split living-human support-state evidence into narrower route families, but [`wiki/measurement-stack-and-claim-ceiling.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md) still underrepresented three critical internal splits:

- `blood-CSF barrier / choroid-plexus` routes
- `SL25.1188` as a distinct MAO-B astrocyte-PET route
- `TSPO / CSF1R / COX-2` as separate human neuroimmune PET routes

Because this page is the site's claim-ceiling rule sheet, that lag mattered more than another front-door rewrite. If the rule page stays compressed, later summaries can silently inherit an overbroad ceiling.

# Why This Needed Correction

## 1. The rule page still compressed distinct human barrier routes

- [Zhao et al. (2020)](https://doi.org/10.1186/s12987-020-00218-z) constrain `choroid-plexus perfusion`.
- [Petitclerc et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118755) constrain `blood-to-CSF water transport`.
- [Anderson et al. (2022)](https://doi.org/10.1080/21688370.2021.1963143) constrain `choroid-plexus water cycling`.
- [Wu et al. (2026)](https://doi.org/10.1177/0271678X251369218) constrain `apparent BCSFB exchange`.
- [Petitclerc et al. (2026)](https://doi.org/10.1177/0271678X261429042) constrain `simultaneous BBB-versus-BCSFB exchange`.

Those papers do not observe one shared boundary object. They differ in crossed boundary, carrier definition, model burden, and safe calibrator role.

## 2. Astrocyte PET still needed an explicit `SL25.1188` rung

- [Villemagne et al. (2022a)](https://doi.org/10.2967/jnumed.121.263254), [Villemagne et al. (2022b)](https://doi.org/10.2967/jnumed.121.263255), [Hiraoka et al. (2025)](https://doi.org/10.1007/s12149-025-02083-y), and [Mesfin et al. (2026)](https://doi.org/10.1007/s12149-025-02144-2) already split `SMBT-1` into target-validation, disease-context, brain-quantification, and whole-body-biodistribution roles.
- [Matsuoka et al. (2026)](https://doi.org/10.1007/s00259-025-07542-2) then constrain a separate `SL25.1188 simplified-quantification` route.
- [Best et al. (2026)](https://doi.org/10.1038/s41380-025-03355-9) show `SL25.1188` remains cohort-severity- and smoking-conditioned.
- [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) and [Livingston et al. (2022)](https://doi.org/10.1038/s41380-021-01429-y) constrain `I2BS`.

Therefore `astrocyte PET` is still not one route family even after SMBT-1 has been split.

## 3. Human neuroimmune PET still could not be left as one broad lane

- [Biechele et al. (2023)](https://doi.org/10.1038/s41467-023-40937-z) show that `TSPO` is not a universal human activation-state meter.
- [Wijesinghe et al. (2025)](https://doi.org/10.1093/brain/awaf078) constrain a narrower `TSPO disease-context / validation-bounded` route.
- [Horti et al. (2022)](https://doi.org/10.1186/s13550-022-00929-4) and [Ogata et al. (2025)](https://doi.org/10.2967/jnumed.124.268699) constrain `CSF1R route-setting`.
- [Yan et al. (2025)](https://doi.org/10.2967/jnumed.124.268525) constrain a separate `COX-2 enzyme-defined` route.

These are different target classes with different validation burdens. The central claim-ceiling page therefore had to block `immune PET` as a reusable umbrella row.

# Root Critique

The scientific criticism is straightforward:

1. `BBB water exchange` is not `blood-CSF barrier / choroid-plexus transport`.
2. `Choroid-plexus perfusion` is not `blood-to-CSF transport`.
3. `SMBT-1` is not `SL25.1188`, and neither is `I2BS`.
4. `TSPO` is not `CSF1R`, and neither is `COX-2`.
5. None of those living-human rows, by itself, directly identifies a local maintenance controller or synapse-support mechanism.

Therefore the rule page must force a reader to name the route family before interpreting the claim ceiling.

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md)
  - updated front matter, highlights, and known-points text so BCSFB, `SL25.1188`, and neuroimmune PET route splits are visible at the page-summary layer
  - expanded the human maintenance-state ladder with five `blood-CSF barrier / choroid-plexus` rows
  - added a dedicated `SL25.1188 MAO-B` row
  - added `TSPO`, `CSF1R`, and `COX-2` human neuroimmune PET rows
  - updated the surrounding rule text so the page now logs proxy class, operational maturity, and calibrator role at the same granularity
  - extended the on-page references list with the new primary sources
- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_measurement_stack_human_proxy_route_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_measurement_stack_human_proxy_route_sync.md)
  - added this audit note to preserve the criticism, rationale, and reference trail

# Verification

- `git diff --check`
- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "choroid-plexus|blood-to-CSF|BCSFB|SL25.1188|TSPO|CSF1R|COX-2" wiki/measurement-stack-and-claim-ceiling.md github-wiki-export/measurement-stack-and-claim-ceiling.md`

# External Dependency Tasks

- None.
  - This run stayed fully inside executable repository work: literature checking, markdown edits, export verification, local static-site build, and Git publication.

# References

1. Zhao L, Taso M, Dai W, Press DZ, Alsop DC. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids and Barriers of the CNS*. 2020. https://doi.org/10.1186/s12987-020-00218-z
2. Petitclerc L, Hirschler L, Wells JA, et al. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.118755
3. Anderson VC, Tagge IJ, Doud A, et al. DCE-MRI of brain fluid barriers: in vivo water cycling at the human choroid plexus. *Tissue Barriers*. 2022. https://doi.org/10.1080/21688370.2021.1963143
4. Wu X, Tan S, Zhang Y, et al. Feasibility of relaxation-exchange magnetic resonance imaging (REXI) for measuring water exchange across the blood-CSF barrier in the human choroid plexus. *Journal of Cerebral Blood Flow & Metabolism*. 2026. https://doi.org/10.1177/0271678X251369218
5. Petitclerc L, Durrant H, Hirschler L, Václavů L, van Osch MJP. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *Journal of Cerebral Blood Flow & Metabolism*. 2026. https://doi.org/10.1177/0271678X261429042
6. Villemagne VL, Harada R, Dore V, et al. First-in-humans evaluation of 18F-SMBT-1, a novel monoamine oxidase-B PET tracer for imaging reactive astrogliosis. *Journal of Nuclear Medicine*. 2022. https://doi.org/10.2967/jnumed.121.263254
7. Villemagne VL, Harada R, Dore V, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022. https://doi.org/10.2967/jnumed.121.263255
8. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025. https://doi.org/10.1007/s12149-025-02083-y
9. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [18F]SMBT-1 in healthy humans. *Annals of Nuclear Medicine*. 2026. https://doi.org/10.1007/s12149-025-02144-2
10. Matsuoka K, Matsuura K, Kikuchi T, et al. Quantification of monoamine oxidase B expression with 11C-SL25.1188 for imaging reactive astrocytes in patients with Alzheimer disease. *European Journal of Nuclear Medicine and Molecular Imaging*. 2026. https://doi.org/10.1007/s00259-025-07542-2
11. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026. https://doi.org/10.1038/s41380-025-03355-9
12. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018. https://doi.org/10.2967/jnumed.118.208009
13. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, glucose metabolism, grey matter volume and amyloid load using 11C-BU99008 PET. *Molecular Psychiatry*. 2022. https://doi.org/10.1038/s41380-021-01429-y
14. Biechele G, Wind K, Blume T, et al. Translocator protein is a marker of activated microglia in rodent models but not human neurodegenerative diseases. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-40937-z
15. Wijesinghe SS, Edison P, Passamonti L, et al. Post-mortem validation of in vivo TSPO PET as a microglial biomarker. *Brain*. 2025. https://doi.org/10.1093/brain/awaf078
16. Horti AG, Naik R, Foss CA, et al. PET imaging of microglia by targeting macrophage colony-stimulating factor 1 receptor (CSF1R). *EJNMMI Research*. 2022. https://doi.org/10.1186/s13550-022-00929-4
17. Ogata A, Ikenuma H, Yasuno F, et al. First-in-Human Study of [11C]NCGG401 for Imaging Colony-Stimulating Factor 1 Receptors in the Brain. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268699
18. Yan X, Noergaard M, Morse CL, et al. PET Quantification in Healthy Humans of Cyclooxygenase-2, a Potential Biomarker of Neuroinflammation. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268525
