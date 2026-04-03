---
title: "2026-04-03 site deepening audit: beginner verification human proxy family-internal split"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **beginner-rule lag inside the verification front door**.

[`wiki/verification-basics.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/verification-basics.md) already taught that living-human proxy bundles need:

- `proxy class`
- `operational maturity`
- `calibrator role`
- `robustness / common-driver / increment` gates

However, after the 2026-04-01 to 2026-04-03 site-wide tightening, that beginner page still let readers start from family labels that were already too broad. That was no longer scientifically safe.

The deeper site pages had already become stricter about:

- deuterium `absolute-quantification` versus `kinetic-rate imaging`
- BBB versus blood-CSF-barrier / choroid-plexus routes
- astrocyte PET `target + route-role` families
- neuroimmune PET `target-defined` families

The beginner verification page still under-taught that first split.

# Why This Needed Correction

## 1. The three axes are not meaningful if the route family is still internally collapsed

If a reader starts from `deuterium imaging`, `barrier MRI`, `astrocyte PET`, or `immune PET`, the three-axis framework becomes weaker than the rest of the site now permits.

That is because the bundle can appear to begin from one reusable human row when the literature actually supports several different comparison families with different quantity types, targets, transport objects, and model burdens.

## 2. Deuterium is already more than one beginner row

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) constrain an `absolute-quantification` route at `7 T`.
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) constrain a `kinetic-rate imaging` route under blood-input and kinetic modeling.
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) show that repeatability is still protocol- and time-point-conditioned.

Critique:

- `deuterium imaging` is not one beginner object.
- Quantity type and operating burden have to be fixed before `operational maturity` is judged.

## 3. Blood-fluid routes are already split before bundle composition begins

- [Zhao et al. (2020)](https://doi.org/10.1186/s12987-020-00218-z) constrain `choroid-plexus perfusion`.
- [Petitclerc et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118755) constrain `blood-to-CSF transport`.
- [Petitclerc et al. (2026)](https://doi.org/10.1177/0271678X261429042) constrain `simultaneous BBB-versus-BCSFB exchange`.

Critique:

- `barrier MRI` is not one crossed boundary.
- `BBB water-exchange`, `blood-to-CSF transport`, and `simultaneous BBB-vs-BCSFB exchange` do not share one transport object or one interpretation burden.

## 4. Astrocyte and neuroimmune PET also split before the three axes

- [Matsuoka et al. (2026)](https://doi.org/10.1007/s00259-025-07542-2) constrain a simplified `SL25.1188` MAO-B route in AD.
- [Biechele et al. (2023)](https://doi.org/10.1038/s41467-023-40937-z) show that TSPO is not a species-invariant human activation-state marker.
- [Ogata et al. (2025)](https://doi.org/10.2967/jnumed.124.268699) constrain a `CSF1R route-setting` PET route.
- [Yan et al. (2025)](https://doi.org/10.2967/jnumed.124.268525) constrain a `COX-2 enzyme-defined` PET route.

Critique:

- `astrocyte PET` is not one reusable target row.
- `immune PET` is not one reusable target row either.
- Therefore a beginner verification page that teaches bundle logic must also teach family-internal split at the front door.

# Root Critique

The scientific criticism is precise:

1. The beginner verification page already had the right bundle framework.
2. But it still let the reader enter that framework one step too late.
3. On the human side, `family-internal comparison family` now has to be fixed before `proxy class / operational maturity / calibrator role`.
4. Without that order, the beginner page teaches a weaker inferential model than the rest of the site now enforces.

Therefore the corrected beginner rule is:

`family-internal comparison family first -> three axes second -> bundle gates third`

# Web-Verified Primary Sources Checked On 2026-04-03

- Karkouri et al. (2026), *Magnetic Resonance in Medicine*: https://doi.org/10.1002/mrm.70308
- Li et al. (2025), *PNAS Nexus*: https://doi.org/10.1093/pnasnexus/pgaf072
- Bøgh et al. (2024), *European Radiology Experimental*: https://doi.org/10.1186/s41747-024-00426-4
- Zhao et al. (2020), *Fluids and Barriers of the CNS*: https://doi.org/10.1186/s12987-020-00218-z
- Petitclerc et al. (2021), *NeuroImage*: https://doi.org/10.1016/j.neuroimage.2021.118755
- Petitclerc et al. (2026), *Journal of Cerebral Blood Flow & Metabolism*: https://doi.org/10.1177/0271678X261429042
- Matsuoka et al. (2026), *European Journal of Nuclear Medicine and Molecular Imaging*: https://doi.org/10.1007/s00259-025-07542-2
- Biechele et al. (2023), *Nature Communications*: https://doi.org/10.1038/s41467-023-40937-z
- Ogata et al. (2025), *Journal of Nuclear Medicine*: https://doi.org/10.2967/jnumed.124.268699
- Yan et al. (2025), *Journal of Nuclear Medicine*: https://doi.org/10.2967/jnumed.124.268525

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/verification-basics.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/verification-basics.md)
  - updated front matter so the page summary now states that family-internal comparison family is fixed before the three-axis human-proxy reading
  - added a new 2026-04-03 beginner note-box that makes the deuterium / BCSFB / astrocyte PET / neuroimmune PET split explicit
  - tightened the `Human proxy bundles now need three axes and three gates` section so the ordering now reads `family-internal comparison family -> three axes -> bundle gates`
  - tightened the `Proxy class` row and the `Living-human proxy bundle` row so family-internal split is visible at table level
- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_verification_basics_human_proxy_family_split.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_verification_basics_human_proxy_family_split.md)
  - added this audit note to preserve the critique, rationale, and source trail

# Verification

- `git diff --check`
- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "family-internal comparison family|SL25.1188|TSPO|CSF1R|COX-2|blood-CSF-barrier / choroid-plexus" wiki/verification-basics.md github-wiki-export/verification-basics.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: web literature verification, markdown edits, wiki export, static-site build, and Git publication.

# References

1. Karkouri J, Novoselova M, Rodgers CT, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. *Magnetic Resonance in Medicine*. 2026. https://doi.org/10.1002/mrm.70308
2. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
3. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024. https://doi.org/10.1186/s41747-024-00426-4
4. Zhao L, Taso M, Dai W, Press DZ, Alsop DC. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids and Barriers of the CNS*. 2020. https://doi.org/10.1186/s12987-020-00218-z
5. Petitclerc L, Hirschler L, Wells JA, et al. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.118755
6. Petitclerc L, Durrant H, Hirschler L, Václavů L, van Osch MJP. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *Journal of Cerebral Blood Flow & Metabolism*. 2026. https://doi.org/10.1177/0271678X261429042
7. Matsuoka K, Matsuura K, Kikuchi T, et al. Quantification of monoamine oxidase B expression with 11C-SL25.1188 for imaging reactive astrocytes in patients with Alzheimer's disease. *European Journal of Nuclear Medicine and Molecular Imaging*. 2026. https://doi.org/10.1007/s00259-025-07542-2
8. Biechele G, Wind K, Blume T, et al. Translocator protein is a marker of activated microglia in rodent models but not human neurodegenerative diseases. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-40937-z
9. Ogata A, Ikenuma H, Yasuno F, et al. First-in-Human Study of [11C]NCGG401 for Imaging Colony-Stimulating Factor 1 Receptors in the Brain. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268699
10. Yan X, Noergaard M, Morse CL, et al. PET Quantification in Healthy Humans of Cyclooxygenase-2, a Potential Biomarker of Neuroinflammation. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268525
