---
title: "2026-04-02 site deepening audit: literature myelin route sync"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was a **literature-front-door compression around myelin / oligodendrocyte timing evidence**.

By 2026-04-02, the site's core verification and wiki pages already treated:

- `activity-dependent oligodendrogenesis / learning`
- `node / internode / periaxonal timing control`
- `plasticity-brake function`
- `recovery-boundary / incomplete-remyelination evidence`
- `human tract-speed estimation`
- `human myelin-proxy comparison families`

as different inferential objects.

However, the two public literature entry pages still lagged behind that rule:

- [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md) still used compressed labels such as `quantity-defined myelin routes`.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md`](/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md) still contained the stronger error `specialized macro myelin / thermal papers`, which fused myelin and thermal evidence into one row.

That was technically unstable because the public front door was quietly reintroducing exactly the compression that the site's route cards had already forbidden.

# Why This Needed Correction

## 1. The literature front door was still flattening distinct mechanistic families

The primary literature does not support one generic `myelin support` object.

- Gibson et al. (2014, DOI `10.1126/science.1252304`) and McKenzie et al. (2014, DOI `10.1126/science.1254960`) are about **activity-dependent oligodendrogenesis / learning**.
- Seidl et al. (2015, DOI `10.1038/ncomms9073`) and Cohen et al. (2020, DOI `10.1016/j.cell.2019.11.039`) are about **node / internode / periaxonal timing control**.
- Xin et al. (2024, DOI `10.1038/s41586-024-07853-8`) is about **myelination as a brake on adult cortical plasticity**.
- Della-Flora Nunes et al. (2025, DOI `10.1038/s41467-025-56092-6`) is about a **recovery boundary**, explicitly showing that functional recovery can occur without complete remyelination.

These are not one causal family, one structural unit, or one claim ceiling.

## 2. The human myelin lane was still being overread as one observability row

The current human literature also does not support one generic `myelin MRI` row.

- van Blooijs et al. (2023, DOI `10.1038/s41593-023-01272-0`) are a **tract-scale transmission-speed** route.
- Arshad et al. (2017, PMC `PMC5342928`) are an **MWF versus calibrated T1w/T2w comparison** route.
- Hagiwara et al. (2018, DOI `10.1038/s41598-018-28852-6`) are a **relaxometry / MTsat comparison** route.
- Baadsvik et al. (2024, DOI `10.1002/mrm.29998`) are a **bilayer-sensitive proof-of-principle** route with specialized burden.
- Genc et al. (2025, DOI `10.1038/s41467-025-58604-w`) are a **developmental diffusion-microstructure route with ex vivo oligodendrocyte-expression alignment**.
- Chen et al. (2025, DOI `10.1016/j.neuroimage.2025.121456`) show that **orientation dependence remains an internal MT-family burden**.
- Galbusera et al. (2025, DOI `10.1111/bpa.70010`) are a **qT1 remyelination-sensitive pathology** route.
- Colaes et al. (2026, DOI `10.1007/s00234-025-03875-9`) show that **T1w/FLAIR may stay a general tissue-health marker rather than a myelin-specific readout**.

Those routes differ in direct observable, calibration target, pathology dependence, hardware burden, and safe inference.

## 3. The archive was mixing myelin and thermal evidence into one proxy row

This was the most concrete technical error in the literature map.

Before this run, [`/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md`](/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md) still had a single table row equivalent to:

- `Baadsvik et al. (2024) / Rzechorzek et al. (2022)`
- `Specialized macro myelin bilayer / thermal physiology proxies`
- `Bounded support-state proxy calibration for myelin or thermal class`

That merge was not defensible.

- Baadsvik et al. (2024) is a **myelin bilayer-sensitive imaging** route.
- Rzechorzek et al. (2022, DOI `10.1093/brain/awab466`) is a **macro thermal-rhythm / brain-temperature physiology** route.

Myelin timing support and thermal physiology are different inferential objects. They should not share one evidence row.

## 4. The U3 summary language was still too coarse

The U3 maintenance-state summary still used compressed phrases such as:

- `myelin/metabolic support`
- `sleep / myelin / glia / metabolic support / neurovascular-unit / BBB / pericyte support`

Those phrases were weaker than the rest of the site's current taxonomy.

They silently fused:

- myelin / oligodendrocyte timing support
- glial substrate-routing
- astrocyte-state
- bioenergetic / mitochondrial support

into a single background bucket.

# Changes Executed In This Session

## [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md)

- Updated front matter so the literature archive no longer names only `quantity-defined myelin routes`.
- Added a new public front-door note, `Read myelin / oligodendrocyte timing papers through an explicit route-family split`.
- Rewrote the human observability lane so it now distinguishes `tract-speed` from a broader `myelin / oligodendrocyte proxy family`.
- Added myelin-route anchors directly to the human observability table.
- Updated the maintenance-state boundary note so myelin / oligodendrocyte timing support is explicit in the hidden-state list.
- Replaced the compressed `myelin/metabolic support` wording in the route summary table.

## [`/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md`](/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md)

- Updated front matter so the literature map now advertises the myelin / oligodendrocyte route split at the front door.
- Rewrote the U3 maintenance-state summary row to separate `myelin / oligodendrocyte timing support` from `glial substrate-routing`.
- Added a dedicated U3 note, `Read U3 myelin / oligodendrocyte timing evidence as route-family claims, not as one delay row`.
- Rewrote the human observability paragraph so myelin timing-support routes and thermal routes are no longer fused.
- Split the old combined `myelin / thermal` table row into:
  - one row for tract-speed plus macro myelin / oligodendrocyte-linked proxy routes
  - one separate row for macro thermal physiology
- Tightened the quick-entry U3 sentence so it now points readers to the current maintenance-state taxonomy rather than the old mixed bucket.

# Verification

- Ran `git diff --check` with no whitespace or patch-format errors.
- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Confirmed generated output contains the new front-door language in:
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/mind_uploading_papers.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/mind_uploading_papers.html)
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/research_harvest_50.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/research_harvest_50.html)
- Confirmed generated HTML now includes:
  - the new `Read myelin / oligodendrocyte timing papers through an explicit route-family split` note
  - the new `Read U3 myelin / oligodendrocyte timing evidence as route-family claims, not as one delay row` note
  - separate myelin and thermal calibration rows in the literature map

# External Dependency Tasks

- None.
  - This session's work was fully executable in-repo: literature verification, content edits, local build verification, and Git operations.

# References

1. Gibson EM, Purger D, Mount CW, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. *Science*. 2014.
   - https://doi.org/10.1126/science.1252304
2. McKenzie IA, Ohayon D, Li H, et al. Motor skill learning requires active central myelination. *Science*. 2014.
   - https://doi.org/10.1126/science.1254960
3. Seidl AH, Rubel EW, Harris DM. Mechanisms for adjusting interaural time differences to achieve binaural coincidence detection. *Nature Communications*. 2015.
   - https://doi.org/10.1038/ncomms9073
4. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
5. Hagiwara A, Hori M, Kamagata K, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018.
   - https://doi.org/10.1038/s41598-018-28852-6
6. Cohen CC, Popovic MA, Klooster J, et al. Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. *Cell*. 2020.
   - https://doi.org/10.1016/j.cell.2019.11.039
7. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022.
   - https://doi.org/10.1093/brain/awab466
8. van Blooijs D, Nunes A, van den Boom MA, et al. Developmental trajectory of transmission speed in the human brain. *Nature Neuroscience*. 2023.
   - https://doi.org/10.1038/s41593-023-01272-0
9. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
10. Xin W, et al. Oligodendrocytes and myelin limit neuronal plasticity in visual cortex. *Nature*. 2024.
    - https://doi.org/10.1038/s41586-024-07853-8
11. Genc S, Ball G, Chamberland M, et al. MRI signatures of cortical microstructure in human development align with oligodendrocyte cell-type expression. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-58604-w
12. Chen HS, et al. Orientation-independent magnetization transfer imaging of white matter. *NeuroImage*. 2025.
    - https://doi.org/10.1016/j.neuroimage.2025.121456
13. Della-Flora Nunes G, et al. Incomplete remyelination via therapeutically enhanced oligodendrogenesis is sufficient to recover visual cortical function. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-56092-6
14. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025.
    - https://doi.org/10.1111/bpa.70010
15. Colaes R, Radwan A, Billiet T, et al. Evaluating the T1w/FLAIR ratio as a proxy for myelin: Associations with myelin water Imaging, diffusion metrics, and cognition. *Neuroradiology*. 2026.
    - https://doi.org/10.1007/s00234-025-03875-9
