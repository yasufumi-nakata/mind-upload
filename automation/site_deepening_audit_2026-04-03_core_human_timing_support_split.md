---
title: "2026-04-03 site deepening audit: core human timing-support split"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **core front-door inconsistency in the human timing-support lane**.

By 2026-04-03, the site already had the correct scientific stop line in some deeper prose:

- `human tract-scale transmission-speed estimation`
- `myelin-water / calibrated T1w:T2w comparison`
- `relaxometry / MTsat comparison`
- `bilayer-sensitive mapping`
- `qT1 remyelination-sensitive pathology`
- `T1w/FLAIR tissue-health-sensitive ratio`

were already treated as different inferential objects in the stronger route-card pages.

However, the public entry tables and glossary still lagged behind that rule in several places:

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md) still compressed human timing-support into one `myelin MRI / tissue-health-sensitive ratio family` row.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md) still presented only `myelin-bilayer mapping` in the main human-observability table.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md) still listed `human myelin bilayer mapping` without a separate tract-speed row.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md`](/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md) still let the roadmap table collapse tract-speed and myelin-sensitive MRI into one row family.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md) still defined `Timing-state` without explicitly separating tract-speed estimation from myelin-sensitive or tissue-health-sensitive MRI quantities.

That mismatch mattered because the front door was weaker than the deeper methodological rule.

# Why This Needed Correction

## 1. Tract-speed estimation and myelin-sensitive MRI are not the same observable

The primary literature does not support a single reusable `human timing-support` row.

- [van Blooijs et al. (2023)](https://doi.org/10.1038/s41593-023-01272-0) constrain a **tract-scale transmission-speed estimation** route in living humans.
- [Arshad et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/) compare **MWF** with calibrated **T1w/T2w** and show that reliability does not by itself give strong criterion validity.
- [Hagiwara et al. (2018)](https://doi.org/10.1038/s41598-018-28852-6) show that **SyMRI**, **MTsat**, and **T1w/T2w** do not behave as one interchangeable myelin measure.
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) provide a **bilayer-sensitive** route, but only as a specialized proof-of-principle in two healthy volunteers.
- [Galbusera et al. (2025)](https://doi.org/10.1111/bpa.70010) show that **qT1** can be remyelination-sensitive in a pathology-linked postmortem design while **MWF** and **MTR** do not separate the same lesion classes.
- [Colaes et al. (2026)](https://doi.org/10.1007/s00234-025-03875-9) show that **T1w/FLAIR** is safer to read as a broader tissue-health-sensitive ratio rather than a myelin-specific readout.

These routes differ in direct observable, calibration target, cohort/pathology dependence, and safe claim ceiling.

## 2. The front door was still reintroducing a shortcut that the route-card pages already reject

The scientific criticism is not that the site lacked literature. The problem was **cross-page inferential drift**.

- Deep pages already rejected `human timing-support` as one generic quantity.
- Core entry tables still left room for readers to silently move from:
  - `tract-scale speed estimate exists`
  - `a myelin-sensitive MRI contrast exists`
  - `a bilayer-sensitive proof-of-principle exists`
  - `a tissue-health-sensitive ratio exists`
- to:
  - `human timing-state is nearly directly readable`

That rephrasing is not defensible from the current primary literature.

## 3. The glossary also needed the same stop line

The glossary is one of the first places where readers stabilize the site's vocabulary.

If `Timing-state` is defined only as `myelin` plus a few MRI-family examples, readers can still miss that:

- tract-speed estimation is a **route family**
- myelin-sensitive MRI is a **quantity family**
- tissue-health-sensitive ratios are a **broader family**

Those are not interchangeable.

# Changes Executed In This Session

## [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)

- Updated the front-door `Human evidence is layered` highlight so it now separates:
  - `quantity-defined ionic proxy families`
  - `tract-scale transmission-speed routes`
  - `myelin-sensitive / tissue-health-sensitive MRI ratio families`

## [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)

- Updated the myelin highlight so it now names `human tract-speed estimation` separately.
- Updated the human-evidence ladder highlight so it no longer compresses timing-support and myelin-sensitive MRI into one family label.
- Split the human-observability table into:
  - `Human tract-scale transmission-speed estimation`
  - `Human myelin MRI / tissue-health-sensitive ratio family`
- Rewrote the timing-support note box so the route split is explicit at the entry point.
- Added a reference entry for van Blooijs et al. (2023).

## [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)

- Updated the front-door proxy summary so `tract-scale transmission-speed estimation` is a visible human route.
- Updated the long Q2d human-observability paragraph to add van Blooijs et al. (2023) before the bilayer route.
- Added a dedicated `Human tract-scale transmission-speed estimation` row to the main human route table.
- Updated the `Route name alone is too coarse` note so it now includes `tract-scale transmission-speed estimation`.
- Added a reference entry for van Blooijs et al. (2023).

## [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md)

- Updated the human-maintenance ladder overview so it now distinguishes `tract-scale transmission-speed estimation` from `macro myelin mapping`.
- Added a dedicated tract-speed row to the ladder table.
- Updated the operational-maturity note so it now states that van Blooijs et al. (2023) and Baadsvik et al. (2024) calibrate different bounded timing-support proxies.
- Updated the human proxy-class rule so `tract-scale transmission-speed proxy` is explicit as its own proxy class.
- Added a reference entry for van Blooijs et al. (2023).

## [`/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md`](/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md)

- Updated the roadmap highlights so `tract-scale transmission-speed estimation` is separate from `quantity-defined myelin MRI / tissue-health-sensitive ratios`.
- Updated the M3 addendum prose so the route-family split is explicit in the roadmap narrative.
- Split the roadmap table into:
  - `Human tract-scale transmission-speed estimation`
  - `Quantity-defined myelin MRI / tissue-health-sensitive ratio family`
- Added a reference entry for van Blooijs et al. (2023).

## [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md)

- Rewrote the `Timing-state` definition so it now explicitly separates:
  - `tract-scale transmission-speed estimation`
  - `myelin-water / MT-family / bilayer / qT1 remyelination-sensitive`
  - `T1w/FLAIR tissue-health-sensitive`

# Verification

- Ran `git diff --check` to confirm the patch is clean.
- Rebuilt the site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Confirmed generated output contains the new tract-speed split in:
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/wbe_101.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/wbe_101.html)
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/faq.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/faq.html)
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/wiki/measurement-stack-and-claim-ceiling.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/wiki/measurement-stack-and-claim-ceiling.html)
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/tech_roadmap.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/tech_roadmap.html)
  - [`/Users/yasufumi/Documents/GitHub/mind-upload/_site/glossary.html`](/Users/yasufumi/Documents/GitHub/mind-upload/_site/glossary.html)

# External Dependency Tasks

- None.
  - This session's work was fully executable inside the repository: literature-backed content edits, local verification, and Git operations.

# References

1. van Blooijs D, Nunes A, van den Boom MA, et al. Developmental trajectory of transmission speed in the human brain. *Nature Neuroscience*. 2023.
   - https://doi.org/10.1038/s41593-023-01272-0
2. Arshad M, Stanley JA, Raz N. Test-retest reliability and concurrent validity of in vivo myelin content indices: Myelin water fraction and calibrated T1w/T2w image ratio. *Human Brain Mapping*. 2017.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5342928/
3. Hagiwara A, Hori M, Kamagata K, et al. Myelin Measurement: Comparison Between Simultaneous Tissue Relaxometry, Magnetization Transfer Saturation Index, and T1w/T2w Ratio Methods. *Scientific Reports*. 2018.
   - https://doi.org/10.1038/s41598-018-28852-6
4. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024.
   - https://doi.org/10.1002/mrm.29998
5. Galbusera R, Weigel M, Bahn E, et al. Quantitative T1 is sensitive to cortical remyelination in multiple sclerosis: A postmortem MRI study. *Brain Pathology*. 2025.
   - https://doi.org/10.1111/bpa.70010
6. Colaes R, Radwan A, Billiet T, et al. Evaluating the T1w/FLAIR ratio as a proxy for myelin: Associations with myelin water imaging, diffusion metrics, and cognition. *Neuroradiology*. 2026.
   - https://doi.org/10.1007/s00234-025-03875-9
