---
title: "2026-04-02 site deepening audit: front-door myelin specificity sync"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was a **front-door overcompression inside the human myelin route family**.

By 2026-04-02, the archive-side literature pages already preserved a stricter distinction:

- some routes remain **myelin-sensitive**
- some routes remain **route-specific comparison families**
- some routes remain **developmental oligodendrocyte-linked microstructure routes**
- and at least one newly cited route, **T1w/FLAIR**, may still be safer to read as a **general tissue-health marker** than as a myelin-specific quantity

However, several public entry pages still let readers overread `human myelin MRI` as if it were one reusable row.

# Why This Needed Correction

## 1. The current primary literature does not support one interchangeable human myelin meter

- [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) showed that calibrated `T1w/T2w` can remain reasonably reliable while still having limited criterion validity against **MWF**.
- [Hagiwara et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) showed stronger agreement between **SyMRI** and **MTsat** than with `T1w/T2w`.
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) demonstrated bilayer-sensitive mapping in only **two healthy volunteers** under a specialized acquisition burden.
- [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) showed that **qT1**, but not **MWF** or **MTR**, separated demyelinated from remyelinated cortical lesions in postmortem multiple-sclerosis cortex.
- [Colaes et al. (2026)](https://doi.org/10.1007/s00234-025-03875-9) showed only **weak correlations** between `T1w/FLAIR` and **MWF** and explicitly supported reading the ratio as a broader **tissue-health marker** rather than a specific myelin measure.

Therefore, the site could no longer safely use `human myelin MRI` as one family label without also naming the family-internal split and the `tissue-health` ceiling.

## 2. The front door and the route card had drifted apart

Before this run, the archive already carried the stricter stop line, but the public entry pages were still weaker.

That was technically unstable because:

- readers could still inherit a stronger claim from the front door than from the route card
- `T1w/FLAIR` could still be silently retyped as a myelin-specific route
- the bundle-composition rules in `Verification` and `Human Proxy Composition` were stricter than the language in some overview pages

# Changes Executed In This Session

## Front-door pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - corrected the `Hagiwara et al. (2018)` citation label
  - added the `Colaes et al. (2026)` stop line
  - clarified that `T1w/FLAIR` is not promoted to a myelin-specific meter
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - upgraded the human myelin table row into a `myelin MRI / tissue-health-sensitive ratio family`
  - added `T1w/FLAIR tissue-health-sensitive ratio` to the entry-point route split
- [`/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md`](/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md)
  - updated M3 so the human myelin family now includes the `T1w/FLAIR` ceiling
  - revised the route table so the family no longer reads as one interchangeable myelin quantity
- [`/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md`](/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md)
  - rewrote the human myelin row as `myelin MRI / tissue-health-sensitive routes`

## Verification and route-rule pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - extended the Human Proxy Composition Card and the myelin addendum
  - now requires authors to say whether a route is actually `myelin-sensitive` or only `tissue-health-sensitive`
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/human-proxy-composition.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/human-proxy-composition.md)
  - added a dedicated `T1w/FLAIR tissue-health-sensitive ratio route`
  - updated the composition note so the family now has five internal route types instead of four
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md)
  - updated the myelin route card so `T1w/FLAIR` is explicitly disclosed as broader than myelin-specific contrast

# Verification

- Ran `git diff --check`.
- Rebuilt the site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified the generated output contains the new `T1w/FLAIR tissue-health-sensitive` language and the `Colaes et al. (2026)` stop line.

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown updates, local build, and Git operations.

# References

1. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
2. Hagiwara A, Hori M, Kamagata K, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018.
   - https://doi.org/10.1038/s41598-018-28852-6
3. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
4. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025.
   - https://doi.org/10.1111/bpa.70010
5. Colaes R, Radwan A, Billiet T, et al. Evaluating the T1w/FLAIR ratio as a proxy for myelin: Associations with myelin water imaging, diffusion metrics, and cognition. *Neuroradiology*. 2026.
   - https://doi.org/10.1007/s00234-025-03875-9
