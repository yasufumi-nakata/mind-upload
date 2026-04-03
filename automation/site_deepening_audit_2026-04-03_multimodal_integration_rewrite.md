# Site Deepening Audit: Multimodal Integration Rewrite

- Date: 2026-04-03
- Target page: `wiki/multimodal-integration-basics.md`
- Scope: Technical and natural-science content only

## Why this page was selected

This page was selected because it sits at a high-traffic conceptual junction in the site while still carrying three avoidable scientific risks:

1. It still allowed readers to slide from `same-session` to `same temporal object`.
2. It still allowed readers to slide from `shared cross-modal factor` to `target biological variable` or `quantity bridge`.
3. It still allowed readers to slide from `multimodal gain` to `robust bundle`.

The page also had weaker English than nearby core pages, which made several stop rules harder to read precisely.

## Scientific weaknesses identified

### 1. Temporal-object conflation

The previous page stated the temporal-kernel problem, but not forcefully enough. A simultaneous acquisition can still combine event-locked electrophysiology, hemodynamic response windows, scan-window averages, and kinetic PET quantities. That means shared timestamps do not yet define one shared state sample.

### 2. Shared-factor overread

The previous page correctly warned against overreading common factors, but it still did not sharply separate:

- shared statistical structure
- physiology-linked common drivers
- modality-specific residual structure
- externally grounded quantity bridges

That distinction matters because current multimodal literature repeatedly shows convergence and divergence together.

### 3. Robustness overread

The previous page acknowledged missingness and transfer burdens, but it still needed a cleaner operational stop rule. Bundle-level gains can coexist with:

- restricted complete-case slices
- explicit missing-modality substitution
- higher disagreement in hard subgroups
- cross-centre dependence

### 4. Overcorrection on physiology-linked factors

One subtle weakness remained: physiology-linked common factors could still be read as if they were only nuisance. The literature does not support that simplification either. The correct rule is to label them as physiology-linked or mixed when specificity is unresolved, not to collapse them into either `pure artifact` or `pure neural target`.

### 5. English precision gap

The prior page had multiple sentences whose wording was weaker than the scientific logic being defended. Because this page is a route-setting page, wording quality was not cosmetic; it affected claim boundaries.

## Primary literature basis used in this rewrite

- Kothe et al. (2025), [doi:10.1162/IMAG.a.136](https://doi.org/10.1162/IMAG.a.136): synchronization infrastructure is not the same as device-side delay truth.
- Nguyen et al. (2016), [doi:10.1155/2016/4182483](https://doi.org/10.1155/2016/4182483): EEG-fMRI source imaging still retains temporal mismatch.
- Ripp et al. (2021), [doi:10.1016/j.neuroimage.2021.118131](https://doi.org/10.1016/j.neuroimage.2021.118131): simultaneous PET/fMRI still relies on scan-window PET interpretation.
- Vafaii et al. (2024), [doi:10.1038/s41467-023-44363-z](https://doi.org/10.1038/s41467-023-44363-z): multimodal spontaneous activity contains both common and divergent organization.
- Chen et al. (2025), [doi:10.1038/s41467-025-64414-x](https://doi.org/10.1038/s41467-025-64414-x): simultaneous EEG-PET-MRI shows tightly coupled global dynamics together with distinct network structure.
- Bolt et al. (2025), [doi:10.1038/s41593-025-01945-y](https://doi.org/10.1038/s41593-025-01945-y): a major global fMRI mode is coupled to autonomic physiology as well as EEG.
- Özbay et al. (2019), [doi:10.1038/s42003-019-0659-0](https://doi.org/10.1038/s42003-019-0659-0): sympathetic activity contributes to the fMRI signal during EEG-marked arousal change.
- Epp et al. (2025), [doi:10.1038/s41593-025-02132-9](https://doi.org/10.1038/s41593-025-02132-9): BOLD changes can oppose oxygen-metabolism changes, so covariance is not an automatic quantity bridge.
- Rohaut et al. (2024), [doi:10.1038/s41591-024-03019-1](https://doi.org/10.1038/s41591-024-03019-1): multimodal assessment can improve prognostic performance.
- Amiri et al. (2023), [doi:10.1093/brain/awac335](https://doi.org/10.1093/brain/awac335): direct same-sample multimodal comparison can shrink to a restricted complete-feature subset.
- Manasova et al. (2026), [doi:10.1093/brain/awaf412](https://doi.org/10.1093/brain/awaf412): multimodal models can still face missing-modality handling, transfer burden, and higher disagreement in harder groups.
- Yucel et al. (2015), [doi:10.1117/1.NPh.2.3.035005](https://doi.org/10.1117/1.NPh.2.3.035005): short-separation regression matters for fNIRS when autonomic responses differ.
- An et al. (2025), [doi:10.1117/1.NPh.12.3.035009](https://doi.org/10.1117/1.NPh.12.3.035009): short-channel regression improves cortical activation estimates in a working-memory fNIRS task.

## Changes executed in this session

### Public-facing changes executed

- Rewrote `wiki/multimodal-integration-basics.md` in clearer English.
- Updated the page header fields, highlights, known points, and unknown points to match current Fusion Card logic.
- Rebuilt the eleven audit gates so each gate now names both what it supports and what it still does not license.
- Added an explicit `EEG + fNIRS` route to the route table.
- Added a stronger note that physiology-linked common factors are neither automatically nuisance nor automatically the target neural variable.
- Tightened the operational stop rule for multimodal bundle robustness.
- Reworked the reading rules so they are usable as front-door guardrails instead of only descriptive prose.
- Expanded the reference list with `An et al. (2025)` to support the fNIRS-specific correction.

### Non-public or support changes executed

- Synced `github-wiki-export/multimodal-integration-basics.md` to the rewritten wiki page.

## External dependency tasks

- None for this rewrite.

## Remaining open items after the rewrite

- No same-session multimodal standard yet collapses electrophysiological, hemodynamic, metabolic, and autonomic quantities into one externally validated biological variable.
- Bundle robustness across centres, scanners, and hard clinical or physiological regimes remains an open scientific issue, not a documentation issue.
- State completeness for WBE-relevant hidden variables still remains unresolved even after stronger multimodal framing.

## Verification results

- `cmp -s wiki/multimodal-integration-basics.md github-wiki-export/multimodal-integration-basics.md` -> passed (`synced`)
- `bundle exec jekyll build` -> passed
- `git diff --check` -> passed
- `_site/wiki/multimodal-integration-basics.html` contains the rewritten shared-factor section -> confirmed
