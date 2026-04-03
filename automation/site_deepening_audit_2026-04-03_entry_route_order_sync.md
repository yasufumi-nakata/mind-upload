---
title: "2026-04-03 site deepening audit: entry route-order sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was an **entry-page lag in the order used to read living-human evidence**.

The stronger technical pages had already converged on a narrower rule:

`route family -> route role / human-proxy role -> proxy class / operational maturity / calibrator role -> composition / bridge stop lines`

However, [`/Users/yasufumi/Documents/GitHub/mind-upload/content_hub.md`](/Users/yasufumi/Documents/GitHub/mind-upload/content_hub.md) still summarized the human side mainly as `route family / route burden / calibrator role`, and [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md) still listed many route families without turning that ordering rule into one explicit entrance instruction. That left too much room for a reader to begin from an overbroad category such as `human proxy evidence`, `same-subject evidence`, or `human spectroscopy`, and only later discover that the compared rows did not even constrain the same inferential object.

# Why This Needed Correction

## 1. Route family now has to be fixed before any three-axis reading

- [Lucchetti et al. (2025)](https://www.nature.com/articles/s41467-025-66124-w) define a **five-metabolite 1H-MRSI parcel-similarity scaffold**.
- [Li et al. (2025)](https://academic.oup.com/pnasnexus/article/4/4/pgaf072/8090200) define a **7 T dynamic deuterium MRSI route with blood-input kinetic modeling** for glucose-metabolic rates.
- [Petitclerc et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118755), [Zhao et al. (2020)](https://doi.org/10.1186/s12987-020-00218-z), and [Petitclerc et al. (2026)](https://doi.org/10.1177/0271678X261429042) constrain **blood-to-CSF transport**, **choroid-plexus perfusion**, and **joint BBB-versus-BCSFB exchange** as different route families.
- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254), [Hiraoka et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12559039/), and [Tyacke et al. (2018)](https://jnm.snmjournals.org/content/59/8/1262) constrain **SMBT-1 target-validation / quantification** and **I2BS PET** as different astrocyte-related families.
- [Biechele et al. (2023)](https://www.nature.com/articles/s41467-023-40937-z), [Ogata et al. (2025)](https://jnm.snmjournals.org/content/66/1/87), and [Yan et al. (2025)](https://jnm.snmjournals.org/content/66/1/81) constrain **TSPO**, **CSF1R**, and **COX-2** as different neuroimmune PET families.

Critique:

- `human spectroscopy` is not one route family.
- `human barrier imaging` is not one route family.
- `human astrocyte-related PET` is not one route family.
- `human immune PET` is not one route family.

Therefore a public entry page should not let a reader start from a generic `human proxy` label and only later ask how mature or useful it is.

## 2. Route role / human-proxy role also has to be fixed before bundle promotion

Even after the route family is fixed, the paper still plays different roles:

- healthy atlas / cohort prior
- cross-sectional contrast
- same-subject baseline
- within-subject change witness
- perturbation-response witness

The site's stricter pages already use that distinction, but the entry pages still left it too implicit. That matters because the same route family can still support different public claims depending on which role is actually evidenced.

## 3. Same-subject wording still arrives too early if the proxy role is not typed

`same-subject` or `same-brain` language can still name:

- a repeatability baseline
- a within-subject response witness
- a bridge-limited carry-over claim

Those are not interchangeable. Therefore, entry pages should not let `same-subject` act as a shortcut that hides route family, route role, or bridge burden.

# Root Critique

The scientific criticism is precise:

1. The home page and content hub still let a new reader begin one step too late.
2. `proxy class / operational maturity / calibrator role` are informative only after the route family is already fixed.
3. `same-subject` is not itself a route family and not itself a free promotion.
4. Without that order, the site still leaves room for category mistakes such as:
   - `1H-MRSI similarity` versus `dynamic deuterium kinetic imaging`
   - `choroid-plexus perfusion` versus `blood-to-CSF transport`
   - `SMBT-1 quantification` versus `I2BS PET`
   - `TSPO` versus `CSF1R` versus `COX-2`
5. That matters because later bundle reading, calibrator reading, and bridge reading all become weaker if the entrance typing is wrong.

Therefore the corrected entry rule is:

`route family first -> route role / human-proxy role second -> proxy class / maturity / calibrator role third -> composition / bridge fourth`

# Web-Verified Primary Sources Checked On 2026-04-03

- Lucchetti et al. (2025), *Nature Communications*: https://www.nature.com/articles/s41467-025-66124-w
- Li et al. (2025), *PNAS Nexus*: https://academic.oup.com/pnasnexus/article/4/4/pgaf072/8090200
- Zhao et al. (2020), *Fluids and Barriers of the CNS*: https://doi.org/10.1186/s12987-020-00218-z
- Petitclerc et al. (2021), *NeuroImage*: https://doi.org/10.1016/j.neuroimage.2021.118755
- Petitclerc et al. (2026), *Journal of Cerebral Blood Flow & Metabolism*: https://doi.org/10.1177/0271678X261429042
- Villemagne et al. (2022), *Journal of Nuclear Medicine*: https://doi.org/10.2967/jnumed.121.263254
- Hiraoka et al. (2025), *EJNMMI Physics* / PMC article for quantification route: https://pmc.ncbi.nlm.nih.gov/articles/PMC12559039/
- Tyacke et al. (2018), *Journal of Nuclear Medicine*: https://jnm.snmjournals.org/content/59/8/1262
- Biechele et al. (2023), *Nature Communications*: https://www.nature.com/articles/s41467-023-40937-z
- Ogata et al. (2025), *Journal of Nuclear Medicine*: https://jnm.snmjournals.org/content/66/1/87
- Yan et al. (2025), *Journal of Nuclear Medicine*: https://jnm.snmjournals.org/content/66/1/81

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/content_hub.md`](/Users/yasufumi/Documents/GitHub/mind-upload/content_hub.md)
  - updated the page header so the hub now states the stricter entry order for living-human evidence
  - added a new route-order note explaining why spectroscopy, barrier, astrocyte-related PET, and neuroimmune PET must be split before proxy-strength reading
  - tightened the `same-subject / same-brain` note so that `same-subject` is treated as one proxy role, not a route-family substitute
  - updated the technical fast path table so readers are sent first to route-family pages and then to the human-proxy role pages
- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - added an explicit entry-order rule to the front matter
  - rewrote the main human-observability entrance note so it now states `route family -> route role -> three-axis reading -> composition / bridge`
  - added paper-backed examples showing why `human spectroscopy`, `human barrier imaging`, `astrocyte PET`, and `immune PET` are too coarse as entrance labels
- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_entry_route_order_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_entry_route_order_sync.md)
  - added this audit note so the criticism, rationale, and source trail remain inspectable

# Verification

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "route role / human-proxy role|Why Route Family Now Comes Before Proxy Strength|cohort prior|same-subject baseline" content_hub.md index.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown edits, site build, and Git publication.

# References

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025. https://www.nature.com/articles/s41467-025-66124-w
2. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://academic.oup.com/pnasnexus/article/4/4/pgaf072/8090200
3. Zhao L, Taso M, Dai W, Press DZ, Alsop DC. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids and Barriers of the CNS*. 2020. https://doi.org/10.1186/s12987-020-00218-z
4. Petitclerc L, Hirschler L, Wells JA, et al. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.118755
5. Petitclerc L, Durrant H, Hirschler L, Václavů L, van Osch MJP. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *Journal of Cerebral Blood Flow & Metabolism*. 2026. https://doi.org/10.1177/0271678X261429042
6. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022. https://doi.org/10.2967/jnumed.121.263254
7. Hiraoka K, Matsuura K, Kikuchi T, et al. Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12559039/
8. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018. https://jnm.snmjournals.org/content/59/8/1262
9. Nutma E, Fancy N, Weinert M, et al. Translocator protein is a marker of activated microglia in rodent models but not human neurodegenerative diseases. *Nature Communications*. 2023. https://www.nature.com/articles/s41467-023-40937-z
10. Ogata A, Ikenuma H, Yasuno F, et al. First-in-Human Study of [11C]NCGG401 for Imaging Colony-Stimulating Factor 1 Receptors in the Brain. *Journal of Nuclear Medicine*. 2025. https://jnm.snmjournals.org/content/66/1/87
11. Yan X, Noergaard M, Morse CL, et al. PET Quantification in Healthy Humans of Cyclooxygenase-2, a Potential Biomarker of Neuroinflammation. *Journal of Nuclear Medicine*. 2025. https://jnm.snmjournals.org/content/66/1/81
