---
title: "2026-04-04 site deepening audit: barrier-side human proxy role split"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **remaining compression bug around barrier-side human proxy roles**.

By 2026-04-04, the public site already did a substantial amount of correct work:

- it separated **BBB water exchange** from **tracer-specific BBB transport**
- it separated **choroid-plexus perfusion** from **blood-to-CSF water transport**
- it separated **DCE water cycling**, **apparent BCSFB exchange**, and **simultaneous BBB-versus-BCSFB exchange**

However, one important compression still remained on key reading pages:

- route-family separation was present
- but **route-role / evidence-role separation inside the barrier-side human lane was still incomplete**

That matters because the site's own composition rule says that:

- a **normative / reference route**
- a **cross-sectional disease-burden contrast**
- a **method-comparison warning**
- a **repeatability anchor**
- and a **boundary-separation / model-comparison route**

are not interchangeable bundle jobs.

# Why This Needed Correction

## 1. BBB water-exchange papers already answer different questions

- [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) are not a healthy-reference paper or a disease-burden paper first. Their main result is a **method-family non-equivalence warning**: diffusion-prepared ASL and multi-echo ASL produced materially different BBB water-exchange estimates and inconsistent age dependence.
- [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) are not a method-comparison paper. Their main role is a **healthy-adult lifespan reference route** with a specific ceiling: the apparent gray-matter age effect disappears after **CBF / ATT** correction.
- [Padrela et al. (2026)](https://doi.org/10.1016/j.nicl.2025.103926) are not a healthy-reference paper. Their main role is a **cross-sectional disease-burden route**: lower `Tex` appears in **SCD / MCI** and moderate **WMH** burden, while amyloid-group differences do not survive age / sex adjustment.
- [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) are a different class again: a **tracer-specific PET transport-model route**, not a water-exchange MRI row.

Therefore, even inside `human BBB evidence`, the papers do not share one direct observable, one method burden, or one evidence role.

## 2. BCSFB / choroid-plexus papers also answer different questions

- [Zhao et al. (2020)](https://doi.org/10.1186/s12987-020-00218-z) are an **early route-setting perfusion study** in a small healthy cohort using dynamic ASL modeling.
- [Sun et al. (2024)](https://doi.org/10.1186/s12987-024-00603-y) are a **large healthy-aging extension** using the HCP-Aging cohort to relate choroid-plexus perfusion, volume, and diffusion across adulthood.
- [Petitclerc et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118755) are a **blood-to-CSF water-transport route**, not a perfusion route.
- [Anderson et al. (2022)](https://doi.org/10.1080/21688370.2021.1963143) are a **DCE water-cycling route** that explicitly separates `k_co` from `K^trans`.
- [Wu et al. (2026)](https://doi.org/10.1177/0271678X251369218) are primarily a **repeatability anchor** for apparent `k_BCSFB` under a REXI route.
- [Petitclerc et al. (2026)](https://doi.org/10.1177/0271678X261429042) are primarily a **boundary-separation / model-comparison route** that estimates both `K_bl→GM` and `K_bl→CSF` in one acquisition.

Therefore, the current literature already requires not just `route family`, but also **route role**.

## 3. This compression matters most on the pages that teach bundle reading

The pages most affected by this bug were:

- `wbe_101.md`
- `wiki/human-proxy-composition.md`

That is technically serious because these are the pages that teach readers how to move from:

- route family
- to human proxy role
- to proxy class / maturity / calibrator role
- to composition

If barrier-side papers are kept too coarse here, the site silently reintroduces the shortcut that a growing set of human barrier papers is already one interchangeable `support-state` row.

# Changes Executed In This Session

## `wbe_101.md`

- Updated the front-door highlights so the page now states that barrier-side human evidence is split not only by route family but also by **proxy role**.
- Updated the human observability ladder rows so the BBB row now makes visible:
  - method-comparison
  - healthy-lifespan reference
  - disease-burden contrast
  - tracer-specific transport modeling
- Updated the BCSFB / choroid-plexus row so it now makes visible:
  - early route-setting perfusion
  - healthy-aging extension
  - blood-to-CSF transport
  - DCE water cycling
  - repeatability anchor
  - simultaneous boundary separation
- Updated the neurovascular / BBB note so the human barrier-side examples are no longer listed as if they were one interchangeable human row.

## `wiki/human-proxy-composition.md`

- Updated front matter so the page now records the `2026-04-04 barrier-side route-role split`.
- Added a new correction note explaining why **barrier-side route-role typing** belongs inside composition, not only on front-door pages.
- Added a new page-level highlight so the reader sees the Morgan / Padrela / Zhao / Sun / Wu / Petitclerc role differences before the route matrix.
- Split the old combined rows into separate route-role rows for:
  - BBB water-exchange method-comparison
  - BBB water-exchange healthy-lifespan reference
  - BBB water-exchange disease-burden contrast
  - choroid-plexus perfusion route-setting
  - choroid-plexus perfusion healthy-aging extension
  - apparent BCSFB exchange repeatability
  - simultaneous BBB-versus-BCSFB boundary separation

# Main Critique

The scientific problem here was not a lack of references. It was **role compression inside an already route-split family**.

The site had already learned that:

- BBB water exchange is not tracer-specific PET transport
- choroid-plexus perfusion is not blood-to-CSF transport
- apparent BCSFB exchange is not simultaneous BBB-versus-BCSFB separation

But that still leaves another level of ambiguity unless the **bundle job** is named too.

The barrier-side human papers do not all contribute the same kind of evidence:

- some tell us that two methods disagree
- some provide a healthy-reference surface
- some provide disease-burden contrast
- some provide repeatability
- some provide better model-based boundary separation

Without this split, the site remains vulnerable to a specific overread:

> several barrier-side human papers exist, therefore one general human barrier-support meter is emerging

The primary literature does not justify that move.

# Verification

- Ran `git diff --check`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Reviewed the updated wording in:
  - `wbe_101.md`
  - `wiki/human-proxy-composition.md`
  - the generated `_site` outputs after the build

# External Dependency Tasks

- None.
  - This run stayed within executable repository work: source review, markdown edits, local build verification, and Git operations.

# References

1. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024. https://doi.org/10.1002/nbm.5256
2. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: a multi-echo ASL study. *Neurobiology of Aging*. 2025. https://doi.org/10.1016/j.neurobiolaging.2024.12.012
3. Padrela BE, Tecelão S, Kirsebom B-E, et al. Blood-brain barrier water exchange in relation to amyloid, cognition and cerebrovascular burden. *NeuroImage: Clinical*. 2026. https://doi.org/10.1016/j.nicl.2025.103926
4. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-58356-7
5. Zhao L, Taso M, Dai W, Press DZ, Alsop DC. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids Barriers CNS*. 2020. https://doi.org/10.1186/s12987-020-00218-z
6. Sun Z, Li C, Zhang J, Wisniewski T, Ge Y. Choroid plexus aging: structural and vascular insights from the HCP-aging dataset. *Fluids Barriers CNS*. 2024. https://doi.org/10.1186/s12987-024-00603-y
7. Petitclerc L, Hirschler L, Wells JA, et al. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.118755
8. Anderson VC, Tagge IJ, Doud A, et al. DCE-MRI of Brain Fluid Barriers: In Vivo Water Cycling at the Human Choroid Plexus. *Tissue Barriers*. 2022. https://doi.org/10.1080/21688370.2021.1963143
9. Wu X, Tan S, Zhang Y, et al. Feasibility of relaxation-exchange magnetic resonance imaging (REXI) for measuring water exchange across the blood-CSF barrier in the human choroid plexus. *J Cereb Blood Flow Metab*. 2026. https://doi.org/10.1177/0271678X251369218
10. Petitclerc L, Durrant H, Hirschler L, Václavů L, van Osch MJP. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *J Cereb Blood Flow Metab*. 2026. https://doi.org/10.1177/0271678X261429042
