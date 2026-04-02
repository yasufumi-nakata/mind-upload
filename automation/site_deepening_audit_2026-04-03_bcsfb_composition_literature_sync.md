---
title: "2026-04-03 site deepening audit: BCSFB composition and literature sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **remaining compression bug around human blood-CSF-barrier / choroid-plexus evidence**.

By 2026-04-03, the core public pages already separated:

- choroid-plexus perfusion
- blood-to-CSF water transport
- choroid-plexus water cycling
- apparent BCSFB exchange
- simultaneous BBB-versus-BCSFB ASL exchange

However, two central route-organizing pages still lagged behind that stricter rule:

- `research_harvest_50.md`
- `wiki/human-proxy-composition.md`

That mattered because both pages are entry points that decide how readers compose evidence. If they keep `blood-CSF barrier` too coarse, a reader can still inherit the shortcut that:

- `BBB` and `BCSFB` are near-interchangeable
- `choroid-plexus perfusion` and `blood-to-CSF transport` are almost the same row
- `water cycling` or `apparent exchange` is already close to one generic clearance or barrier-function meter

# Why This Needed Correction

## 1. BCSFB is not just a softer spelling of BBB

- [Zhao et al. (2020)](https://doi.org/10.1186/s12987-020-00218-z) measured **apparent choroid-plexus blood flow**.
- [Petitclerc et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118755) measured **blood-to-CSF water transport** with ultra-long-TE ASL.
- [Anderson et al. (2022)](https://doi.org/10.1080/21688370.2021.1963143) measured **choroid-plexus water cycling** with DCE-MRI and explicitly separated `k_co` from `K^trans`.
- [Wu et al. (2026)](https://doi.org/10.1177/0271678X251369218) measured apparent **k_BCSFB** with a REXI route.
- [Petitclerc et al. (2026)](https://doi.org/10.1177/0271678X261429042) explicitly estimated **K_bl→GM** and **K_bl→CSF** in one human ASL acquisition.

These are not one boundary, one direct observable, or one model family.

## 2. Composition rules fail if BCSFB rows are hidden inside BBB or clearance

- `BBB water exchange`
- `tracer-specific BBB transport`
- `BCSFB / choroid-plexus perfusion`
- `blood-to-CSF transport`
- `DCE water cycling`
- `apparent BCSFB exchange`
- `clearance-side macroscopic or model-based routes`

do not answer the same question.

If those rows are collapsed, the bundle looks closer to a route-free support-state meter than the primary literature justifies.

## 3. The literature map and the composition page are exactly where this compression is most damaging

- `research_harvest_50.md` is the public evidence bank that teaches readers how to group literature by unresolved problem.
- `wiki/human-proxy-composition.md` is the central page that decides whether several human proxy rows may be promoted together.

If those pages are weaker than `index.md`, `wbe_101.md`, `faq.md`, or `perspective.md`, then the front-door shortcut re-enters through the literature and bundle layers.

# Changes Executed In This Session

## `wiki/human-proxy-composition.md`

- Updated front matter so the page now names **blood-CSF-barrier / choroid-plexus family-internal rows** explicitly.
- Expanded `page_highlights`, `known_points`, and `What this page fixes` so BCSFB is no longer compressed into BBB or clearance language.
- Added a new correction note:
  - `2026-04-03 correction: blood-CSF barrier / choroid-plexus family split also belongs inside composition`
- Added dedicated route rows for:
  - choroid-plexus perfusion
  - blood-to-CSF transport
  - choroid-plexus DCE water cycling
  - apparent BCSFB exchange
  - simultaneous BBB-versus-BCSFB ASL exchange
- Updated the composition-failure tables so `quantity / target / transport collapse` and `family-internal route collapse` now explicitly include BCSFB.

## `research_harvest_50.md`

- Updated front matter so the literature map now records the `2026-04-03 BCSFB route-family sync`.
- Added a new technical stop-line note:
  - `Read U3 blood-CSF-barrier papers as route-family claims, not as one BBB-adjacent support row`
- Updated the long `Read human measurement papers as their own evidence class` section so BCSFB routes now appear as their own human observability family rather than being absorbed by BBB or clearance.
- Split the old barrier row into explicit route anchors for:
  - BBB water exchange
  - tracer-specific BBB transport
  - choroid-plexus perfusion
  - blood-to-CSF transport
  - choroid-plexus DCE water cycling
  - apparent BCSFB exchange / simultaneous BBB-versus-BCSFB exchange
- Updated the U3 traction / unresolved summaries so current human evidence is no longer described as merely `beyond one BBB row`.

# Main Critique

The scientific problem was not lack of literature. It was **taxonomy drift**.

The site's deeper and newer public pages had already learned that BCSFB evidence is not one row. But the literature-map and bundle-composition layers had not fully inherited that rule. That drift is technically serious because the project's public logic depends on readers keeping **boundary**, **direct observable**, **carrier / transport object**, and **validation ceiling** separate. If those distinctions disappear precisely on the pages that organize evidence, the site silently reintroduces the shortcut it is trying to block.

# Verification

- Ran `git diff --check`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified the new BCSFB family language in:
  - `research_harvest_50.md`
  - `wiki/human-proxy-composition.md`
  - generated `_site` outputs

# External Dependency Tasks

- None.
  - This run stayed within executable repository work: source verification, markdown edits, local build validation, and Git operations.

# References

1. Zhao L, Taso M, Dai W, Press DZ, Alsop DC. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids Barriers CNS*. 2020. https://doi.org/10.1186/s12987-020-00218-z
2. Sun Z, Li C, Zhang J, Wisniewski T, Ge Y. Choroid plexus aging: structural and vascular insights from the HCP-aging dataset. *Fluids Barriers CNS*. 2024. https://doi.org/10.1186/s12987-024-00603-y
3. Petitclerc L, Hirschler L, Wells JA, et al. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.118755
4. Anderson VC, Tagge IJ, Doud A, et al. DCE-MRI of Brain Fluid Barriers: In Vivo Water Cycling at the Human Choroid Plexus. *Tissue Barriers*. 2022. https://doi.org/10.1080/21688370.2021.1963143
5. Wu X, Tan S, Zhang Y, et al. Feasibility of relaxation-exchange magnetic resonance imaging (REXI) for measuring water exchange across the blood-CSF barrier in the human choroid plexus. *J Cereb Blood Flow Metab*. 2026. https://doi.org/10.1177/0271678X251369218
6. Petitclerc L, Durrant H, Hirschler L, Václavů L, van Osch MJP. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *J Cereb Blood Flow Metab*. 2026. https://doi.org/10.1177/0271678X261429042
7. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024. https://doi.org/10.1002/nbm.5256
8. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025. https://doi.org/10.1016/j.neurobiolaging.2024.12.012
9. Padrela BE, Tecelão S, Kirsebom B-E, et al. Blood-brain barrier water exchange in relation to amyloid, cognition and cerebrovascular burden. *NeuroImage: Clinical*. 2026. https://doi.org/10.1016/j.nicl.2025.103926
10. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-58356-7
