---
title: "2026-04-04 site deepening audit: summary-layer neuroimmune evidence-role sync"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **summary-layer evidence-role compression bug inside human neuroimmune PET**.

The site had already audited the route-family split between:

- `TSPO disease-context / validation-bounded PET`
- `CSF1R route-setting PET`
- `COX-2 enzyme-defined PET`

However, the summary-facing layer still left room for readers to treat these rows as one generic `target-defined neuroimmune PET` bundle. That wording was too weak for the current primary literature. The relevant papers do not differ only by molecular target. They also differ by **evidence role**, **validation strategy**, **healthy-versus-disease regime**, and **quantification burden**.

# Why This Needed Correction

## 1. The strongest current papers do not support one reusable `neuroimmune PET` row

- [Biechele et al. (2023)](https://doi.org/10.1038/s41467-023-40937-z) showed that `TSPO` readout is not species-invariant across fibrillar tauopathies, so `TSPO` cannot be treated as a route-free human microglia-state scalar.
- [Wijesinghe et al. (2025)](https://doi.org/10.1093/brain/awaf078) did not merely add another target. It provided a **disease-context / post-mortem-validated** `TSPO` route in PSP.
- [Horti et al. (2022)](https://doi.org/10.1186/s13550-022-00929-4) and [Ogata et al. (2025)](https://doi.org/10.2967/jnumed.124.268699) define a different lane: **first-in-human `CSF1R` route-setting PET** in healthy volunteers.
- [Yan et al. (2025)](https://doi.org/10.2967/jnumed.124.268525) define another distinct lane: **enzyme-defined `COX-2` PET** with celecoxib blockade and explicit test-retest characterization in healthy humans.

Therefore, the safer summary rule is not merely `TSPO / CSF1R / COX-2 are different targets`, but `TSPO / CSF1R / COX-2 currently play different evidence roles and cannot be summarized as one human neuroimmune PET maturity step`.

## 2. The summary layer was lagging behind the stricter route-card layer

The route-card and verification pages had already become stricter. They already blocked:

1. `transport-side clearance` versus `target-defined neuroimmune PET`
2. `TSPO` versus `CSF1R` versus `COX-2`

But the summary layer still allowed a weaker sentence structure:

- `astrocyte-related PET, target-defined neuroimmune PET, and clearance routes`

That wording reintroduced the same shortcut the deeper pages had already removed. It kept the target names visible, but it still blurred the distinction between:

- a **pathology-validated disease-context route** (`TSPO` in PSP),
- a **healthy-volunteer first-in-human route-setting study** (`CSF1R`),
- and a **blockade-validated low-density enzyme-imaging route with reliability characterization** (`COX-2`).

For a project whose core public claim is that readers must separate **route family**, **route role**, and **claim ceiling**, that summary-layer compression was a real scientific inconsistency.

## 3. Why this matters technically

The overcompression was not a wording preference. It directly weakens the site's logic in three ways.

1. It hides that `TSPO` currently owes its strongest human claim to **disease-specific pathology alignment**, not universal target semantics.
2. It hides that `CSF1R` is still a **route-setting / deployment-burden** story rather than a disease-validated microglial-state meter.
3. It hides that `COX-2` currently depends on **pharmacologic specificity and reliability bounds** in healthy volunteers rather than disease-grounded controller identification.

Once those roles are separated, the criticism becomes clearer: none of the three rows, alone or together, yet identifies a local immune controller, a synapse-specific maintenance mechanism, or a route-free human neuroimmune state variable.

# Root Critique

The summary-layer criticism is therefore:

1. `TSPO`, `CSF1R`, and `COX-2` are not just different target labels.
2. They are different **evidence-role families** with different safe extrapolation limits.
3. A site that already teaches readers to split `route family -> route role -> proxy class` cannot keep a summary phrase that blurs those evidence roles back into one row.

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - rewrote the summary-layer neuroimmune bullet so it now names the evidence-role split: `TSPO disease-context / pathology-validated`, `CSF1R first-in-human route-setting`, and `COX-2 celecoxib-blockade / test-retest-bounded enzyme imaging`
  - replaced the compressed `target-defined neuroimmune PET` wording in the unknown-points layer with `target families` and route-role-conscious phrasing
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - synchronized the FAQ front-door bullet with the same evidence-role split
  - corrected FAQ summary bullets so `astrocyte / neuroimmune / clearance` are no longer compressed as if they answered the same type of human question

# Verification

- Ran `ruby scripts/build_summary_booklet.rb` after the source-page edits so the generated booklet inherits the stricter wording.
- Ran `git diff --check`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified that [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md) now contains `TSPO disease-context / pathology-validated PET`, `CSF1R first-in-human route-setting PET`, and `COX-2 celecoxib-blockade / test-retest-bounded enzyme PET` instead of the weaker compressed wording.

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature check, markdown edits, generated-page rebuild, local static-site verification, and Git operations.

# References

1. Biechele G, Wind K, Blume T, et al. Microglial activation in fibrillar tauopathies. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-40937-z
2. Wijesinghe P, Edison P, Passamonti L, et al. Post-mortem validation of in vivo TSPO PET as a microglial biomarker. *Brain*. 2025. https://doi.org/10.1093/brain/awaf078
3. Horti AG, Naik R, Foss CA, et al. PET imaging of microglia by targeting macrophage colony-stimulating factor 1 receptor (CSF1R). *EJNMMI Research*. 2022. https://doi.org/10.1186/s13550-022-00929-4
4. Ogata A, Ikenuma H, Yasuno F, et al. First-in-human study of [11C]NCGG401 for imaging colony-stimulating factor-1 receptors in the brain. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268699
5. Yan X, Mori W, Yasuno F, et al. PET quantification in healthy humans of cyclooxygenase-2, a potential biomarker of neuroinflammation. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268525
