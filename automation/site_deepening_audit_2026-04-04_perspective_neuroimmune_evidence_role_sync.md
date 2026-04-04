---
title: "2026-04-04 site deepening audit: perspective-layer neuroimmune evidence-role sync"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **perspective-layer compression bug inside human neuroimmune support evidence**.

The site had already become stricter elsewhere about the split between:

- `transport-side clearance`
- `TSPO disease-context / validation-bounded PET`
- `CSF1R route-setting PET`
- `COX-2 enzyme-defined PET`

However, [`/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md`](/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md) still under-exposed that split in the one page meant to hold the whole technical argument together. That mattered because `perspective.md` is the longest synthesis page on the site. If that page still allows readers to compress these routes back into one broad `immune support` or `immune PET` lane, the stricter route-card logic on other pages becomes easier to miss.

# Why This Needed Correction

## 1. The current human literature does not support one reusable neuroimmune PET row

- [Biechele et al. (2023)](https://doi.org/10.1038/s41467-023-40937-z) showed that `TSPO` is not a species-invariant activation-state meter across fibrillar tauopathies, so it cannot be treated as a route-free human microglia-state scalar.
- [Wijesinghe et al. (2025)](https://doi.org/10.1093/brain/awaf078) then constrained a narrower `TSPO` lane by aligning in vivo PET with post-mortem pathology in PSP.
- [Horti et al. (2022)](https://doi.org/10.1186/s13550-022-00929-4) and [Ogata et al. (2025)](https://doi.org/10.2967/jnumed.124.268699) constrain a different lane: `CSF1R` first-in-human / arterial-input / route-setting PET in healthy volunteers.
- [Yan et al. (2025)](https://doi.org/10.2967/jnumed.124.268525) constrain another lane: `COX-2` enzyme-defined PET with celecoxib blockade and route-local test-retest characterization in healthy humans.

Therefore, the safest criticism is not merely that these papers use different targets. They also differ by **validation regime**, **healthy-versus-disease context**, **quantification burden**, and **safe extrapolation ceiling**.

## 2. Perspective had to show the same stop rule as the stricter route-card pages

The site had already corrected this logic in verification and composition pages, but `perspective.md` still made the split less visible than it should have been in three places:

1. top-level highlights,
2. known-points summary language,
3. the main living-human support-state table.

That mismatch was technically important because the page is designed to prevent readers from overpromoting scaffold progress into state-complete language. A synthesis page cannot demand route-role precision in principle while compressing the same distinction in its summary-facing layer.

## 3. The compression was scientifically costly, not stylistically costly

Leaving the page as-is kept three false equivalences too close together:

1. `TSPO pathology-aligned disease-context validation` versus `CSF1R route-setting in healthy volunteers`
2. `CSF1R route-setting` versus `COX-2 pharmacologic specificity plus repeatability`
3. `target-defined neuroimmune PET` versus `transport-side clearance`

Those are different inferential objects. They do not identify one common latent variable, one common controller, or one common deployment maturity class. If they are not separated, the page can accidentally overstate how close current human evidence is to identifying local immune support state.

# Root Critique

The technical criticism is therefore:

1. `TSPO`, `CSF1R`, and `COX-2` are not interchangeable neuroimmune PET rows.
2. `transport-side clearance` is not the same object as `target-defined neuroimmune PET`.
3. None of those human rows, alone or together, yet directly identifies a route-free local immune controller or synapse-support mechanism.

The page had to say that explicitly where readers actually scan first: the summary bullets and the living-human support-state table.

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md`](/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md)
  - extended the top-level `note` and `page_highlights` to name the neuroimmune evidence-role split explicitly
  - added a `known_points` bullet that blocks silent exchange among `TSPO`, `CSF1R`, and `COX-2`
  - inserted three separate support-state rows for `TSPO`, `CSF1R`, and `COX-2`
  - added a dedicated note box explaining why `human neuroimmune PET` is not one reusable support-state row
  - rewrote the maintenance-state summary row so `clearance / immune support` now names transport-side versus PET-side family splitting instead of compressing them

# Verification

- `ruby scripts/build_summary_booklet.rb`
- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- confirmed that [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md) was regenerated cleanly from the updated public-page front matter without introducing build errors

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature check, markdown edits, generated-content rebuild, static-site verification, and Git operations.

# References

1. Biechele G, Wind K, Blume T, et al. Translocator protein is a marker of activated microglia in rodent models but not human neurodegenerative diseases. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-40937-z
2. Wijesinghe P, Edison P, Passamonti L, et al. Post-mortem validation of in vivo TSPO PET as a microglial biomarker in progressive supranuclear palsy. *Brain*. 2025. https://doi.org/10.1093/brain/awaf078
3. Horti AG, Naik R, Foss CA, et al. First-in-human use of 11C-CPPC with positron emission tomography for imaging the macrophage colony-stimulating factor 1 receptor. *EJNMMI Research*. 2022. https://doi.org/10.1186/s13550-022-00929-4
4. Ogata A, Ikenuma H, Yasuno F, et al. First-in-human study of [11C]NCGG401 for imaging colony-stimulating factor-1 receptors in the brain. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268699
5. Yan X, Mori W, Yasuno F, et al. PET quantification in healthy humans of cyclooxygenase-2, a potential biomarker of neuroinflammation. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268525
