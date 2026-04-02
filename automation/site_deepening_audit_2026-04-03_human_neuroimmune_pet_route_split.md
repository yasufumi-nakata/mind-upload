---
title: "2026-04-03 site deepening audit: human neuroimmune PET route split"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **site-wide overcompression inside human neuroimmune PET**.

Several public pages already treated transport-side human clearance routes more carefully, but they still left too much room for readers to read `immune PET` as one reusable human observability row. The current primary literature does not support that shortcut. By 2026-04-03, the safest human-facing split was already at least:

- `TSPO disease-context / validation-bounded PET`
- `CSF1R route-setting PET`
- `COX-2 enzyme-defined PET`

Those routes do not share one target class, one validation regime, one model burden, or one safe calibrator role.

# Why This Needed Correction

## 1. `immune PET` was still too coarse for the human lane

- [Biechele et al. (2023)](https://doi.org/10.1038/s41467-023-40937-z) showed that `TSPO` interpretation is not species-invariant and cannot be read as a universal human activation-state meter.
- [Wijesinghe et al. (2025)](https://doi.org/10.1093/brain/awaf078) then fixed a narrower `TSPO disease-context / validation-bounded` route in PSP by aligning PET with post-mortem pathology.
- [Horti et al. (2022)](https://doi.org/10.1186/s13550-022-00929-4) and [Ogata et al. (2025)](https://doi.org/10.2967/jnumed.124.268699) constrained `CSF1R` first-in-human / arterial-input / tracer-model burdens rather than a route-free microglia-state meter.
- [Yan et al. (2025)](https://doi.org/10.2967/jnumed.124.268525) constrained a distinct `COX-2 enzyme-defined` route with celecoxib blockade.

Therefore, the human literature does not justify the row `immune PET` without target class and route role.

## 2. Human neuroimmune PET is not the same object as transport-side clearance

The site had already become stricter about human clearance transport:

- `macroscopic CSF oscillation`
- `parenchyma-CSF water exchange`
- `respiration-conditioned net flow`
- `exercise-conditioned contrast influx / meningeal-lymphatic flow`
- `intrathecal tracer / CSF-to-blood clearance`
- `CSF mobility`
- `model-based biomarker efflux`

However, that stricter transport-side split created a second problem if the PET side remained generic. A reader could still misread the site as if all human immune-support evidence now formed one broader lane. That is technically false. Transport-side clearance proxies and target-defined neuroimmune PET proxies are already different inferential objects, and even within neuroimmune PET the literature still splits again into `TSPO`, `CSF1R`, and `COX-2` bounded routes.

## 3. The front door and route-rule pages had to agree

Before this run, some core pages had already started separating transport-side human clearance routes from immune interpretation more carefully, but the front door, composition language, and route-card language were not yet synchronized all the way through the site.

That mattered because the public-facing stop rules are only reliable if the landing page, FAQ, beginner page, literature front door, composition page, route-card page, and verification page all block the same category error.

# Root Critique

The scientific criticism is straightforward:

1. A paper about `TSPO` does not automatically calibrate `CSF1R`.
2. A paper about `CSF1R` does not automatically calibrate `COX-2`.
3. A target-defined neuroimmune PET paper does not automatically calibrate transport-side clearance.
4. None of these human routes, by themselves, directly identify a local immune controller or synapse-support mechanism.

Therefore, the site's stronger rule now has to be:

- first name whether the human evidence is `transport-side clearance` or `target-defined neuroimmune PET`
- then, if it is neuroimmune PET, type it as `TSPO`, `CSF1R`, or `COX-2`
- only then assign any safe claim ceiling or calibrator role

# Changes Executed In This Session

## Front-door and summary pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - added the neuroimmune PET split to the landing-page highlights and human-lane wording
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - expanded the beginner human observability ladder with `TSPO`, `CSF1R`, and `COX-2` rows
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - rewrote the human clearance / immune explanation into transport-side versus target-defined neuroimmune PET lanes

## Literature, composition, and route-rule pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md)
  - added a dedicated note box for `human neuroimmune PET` route-family splitting
  - expanded the observability ladder and front-door summary text with `TSPO / CSF1R / COX-2`
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/human-proxy-composition.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/human-proxy-composition.md)
  - added explicit composition language that keeps `TSPO`, `CSF1R`, and `COX-2` separate
  - corrected the causal-bridge table so target-defined neuroimmune PET is no longer hidden inside astrocyte / clearance wording
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md)
  - upgraded the human clearance / immune route card into a transport-side versus target-defined PET split, then subdivided the PET side into `TSPO / CSF1R / COX-2`
- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - updated the observability and composition rule so verification now blocks both `transport-versus-PET` collapse and `TSPO-versus-CSF1R-versus-COX-2` collapse

# Verification

- Ran `git diff --check`.
- Ran `ruby scripts/build_summary_booklet.rb`.
- Ran `ruby scripts/export_github_wiki.rb`.
- Ran `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified the edited pages now contain `TSPO`, `CSF1R`, and `COX-2` route labels instead of a single reusable `immune PET` row.

# External Dependency Tasks

- None.
  - This run stayed fully inside executable repository work: literature verification, markdown edits, generated export checks, local static-site build, and Git operations.

# References

1. Biechele G, Wind K, Blume T, et al. Microglial activation in fibrillar tauopathies. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-40937-z
2. Wijesinghe P, Edison P, Passamonti L, et al. Postmortem validation of neuroinflammation in progressive supranuclear palsy. *Brain*. 2025.
   - https://doi.org/10.1093/brain/awaf078
3. Horti AG, Naik R, Foss CA, et al. PET imaging of microglia by targeting macrophage colony-stimulating factor 1 receptor (CSF1R). *EJNMMI Research*. 2022.
   - https://doi.org/10.1186/s13550-022-00929-4
4. Ogata H, Ni R, Naka S, et al. First-in-human PET study of a CSF1R radioligand in healthy participants. *Journal of Nuclear Medicine*. 2025.
   - https://doi.org/10.2967/jnumed.124.268699
5. Yan X, Mori W, Yasuno F, et al. First-in-human PET imaging of cyclooxygenase-2 with celecoxib blockade in healthy brain. *Journal of Nuclear Medicine*. 2025.
   - https://doi.org/10.2967/jnumed.124.268525
