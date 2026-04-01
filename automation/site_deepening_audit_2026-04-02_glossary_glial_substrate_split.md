---
title: "2026-04-02 site deepening audit: glossary glial-substrate split"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was a **glossary-level category collapse**. By 2026-04-02, the site's core theory and verification pages already treated **glial substrate-routing**, **astrocyte-state**, and **human astrocyte-related proxy routes** as different inferential objects. The glossary still lagged behind that rule.

In practice, the glossary still allowed the following unsafe shortcut:

`astrocyte / glial-state` -> one mixed bucket containing both astrocyte ensembles and glia-to-neuron fuel-routing

That was technically unstable because the rest of the site had already made the opposite distinction explicit.

# Why This Needed Correction

## 1. The glossary contradicted the site's own maintenance-state taxonomy

Core pages already state that:

- `glial substrate-routing` is separate from neuronal mitochondrial control
- `glial substrate-routing` is separate from `astrocyte-state`
- current human energetic imaging and astrocyte-related PET do not directly read out living-human glia-to-neuron fuel-routing

If the glossary keeps those categories fused, new readers relearn exactly the compression that the core pages are trying to block.

## 2. Glial substrate-routing is already a split family in the primary literature

The primary literature does not support one generic `glial support` object.

- Suzuki et al. (2011, DOI `10.1016/j.cell.2011.02.018`) showed that **astrocyte-neuron lactate transport** is required for long-term memory formation.
- Silva et al. (2022, DOI `10.1038/s42255-022-00528-6`) showed a **glial ketogenesis / ketone-body** route during starvation.
- Pavlowsky et al. (2025, DOI `10.1038/s42255-025-01416-5`) showed an **intensive-learning glia-to-neuron fatty-acid** route.
- Greda et al. (2025, DOI `10.1038/s42255-025-01389-5`) showed an **apoE / sortilin-dependent lipid-delivery and fuel-choice** route.

Those papers do not share one fuel class, one supplier-sink relation, one regime trigger, or one claim ceiling.

## 3. Astrocyte-state is a different causal family from fuel-routing

The current astrocyte literature also does not support folding astrocyte ensembles into fuel-routing.

- Cahill et al. (2024, DOI `10.1038/s41586-024-07311-5`) sharpened **minute-scale cortical astrocyte network encoding**.
- Williamson et al. (2025, DOI `10.1038/s41586-024-08170-w`) sharpened **learning-associated astrocyte ensembles** and recall.
- Dewa et al. (2025, DOI `10.1038/s41586-025-09619-2`) sharpened a **multiday astrocytic stabilization trace**.
- Bukalo et al. (2026, DOI `10.1038/s41586-025-10068-0`) sharpened **amygdala astrocyte-supported memory representations**.

These are not the same inferential object as lactate routing, ketone routing, fatty-acid transfer, or apoE / sortilin-dependent lipid uptake.

## 4. Current human routes still stop below direct glial substrate-routing identification

The site already uses a stricter rule elsewhere: current human evidence is limited to macro energetic proxies or target-defined astrocyte-related proxies, not direct living-human glia-to-neuron fuel-routing identity.

Therefore, the glossary needed to stop implying that human astrocyte PET or human energetic imaging already names the active supplier cell, fuel object, transport route, or neuronal sink.

# Changes Executed In This Session

- Updated [`glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md) front matter so glossary-level highlights and known-points now explicitly include `glial substrate-routing`.
- Expanded the `When human-evidence terms start sounding like one thing` note so the route-splitting vocabulary now also names `glial substrate-routing`.
- Added a new glossary note, `When astrocyte-state and glial fuel support start sounding identical`, to stop the specific front-door confusion between astrocyte ensembles, glia-to-neuron fuel-routing, and human proxy classes.
- Rewrote `Maintenance-state` so it now lists `glial substrate-routing` and `astrocyte-state` as separate maintenance-side families.
- Added a new glossary term, `Glial substrate-routing`, to define supplier cell, fuel object, transport route, and human observability ceiling as a distinct concept.
- Replaced the old `Astrocyte / glial-state` row with a narrower `Astrocyte-state` definition that no longer absorbs lactate / ketone / fatty-acid / lipid-routing claims.
- Tightened `Support-state proxy` so a coarse human proxy is not silently overread as direct glial substrate-routing identity.
- Added the missing glial substrate-routing references directly to the glossary bibliography.

# Verification

- Ran `git diff --check` with no whitespace or patch-format errors.
- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Confirmed the generated `_site/glossary.html` contains the new `Glial substrate-routing` row, the renamed `Astrocyte-state` row, and the new glossary note box.

# External Dependency Tasks

- None.
  - This session required only repository inspection, literature verification, local editing, local build verification, and Git operations executable in the current environment.

# References

1. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011.
   - https://doi.org/10.1016/j.cell.2011.02.018
2. Silva B, et al. Glial ketogenesis regulates memory maintenance during starvation. *Nature Metabolism*. 2022.
   - https://doi.org/10.1038/s42255-022-00528-6
3. Pavlowsky A, et al. Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila. *Nature Metabolism*. 2025.
   - https://doi.org/10.1038/s42255-025-01416-5
4. Greda AK, et al. Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel. *Nature Metabolism*. 2025.
   - https://doi.org/10.1038/s42255-025-01389-5
5. Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
   - https://doi.org/10.1038/s41586-024-07311-5
6. Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-024-08170-w
7. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
8. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
