---
title: "2026-04-02 site deepening audit: glossary support-state route-role split"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was not a missing citation block somewhere deep in the wiki. It was a **glossary-level compression bug**. By 2026-04-01, many core pages had already learned to separate human astrocyte-related PET routes and human clearance / transport routes by **target**, **quantity type**, **transport regime**, and **route role**. However, the glossary still lagged behind that site-wide rule. Because the glossary is the shortest path by which new readers normalize the site's vocabulary, that lag mattered disproportionately.

In practical terms, the glossary still made it too easy to overread three different things as one:

1. `astrocyte PET exists in humans` -> one generic human astrocyte-state meter
2. `glymphatic / clearance evidence exists in humans` -> one generic human clearance-state meter
3. `support-state proxy` -> one route-free category that no longer needs quantity-type or route-role typing

# Why This Needed Correction

## 1. The glossary still underdescribed the site's own route-discipline

Other core pages had already converged on the rule that living-human support-state evidence must be typed more narrowly than a family label. The glossary is where those labels are stabilized for reuse across the site. If the glossary remains coarser than the central rule pages, then the site silently reintroduces the same collapse it has already worked to eliminate elsewhere.

## 2. Human astrocyte-related PET does not support one interchangeable glossary entry

The primary literature does not define one route-free `astrocyte PET` object.

- Villemagne et al. (2022, DOI `10.2967/jnumed.121.263254`) provide **first-in-human SMBT-1 MAO-B target validation**.
- Hiraoka et al. (2025, DOI `10.1007/s12149-025-02083-y`) provide a **brain quantification** route with explicit kinetic-model burden.
- Mesfin et al. (2026, DOI `10.1007/s12149-025-02144-2`) provide **whole-body biodistribution / dosimetry** burden, not regional brain astrogliosis ground truth.
- Tyacke et al. (2018, DOI `10.2967/jnumed.118.208009`) establish an **I2BS** route rather than the same molecular target as MAO-B PET.
- Livingston et al. (2022, DOI `10.1038/s41380-021-01429-y`) show disease-stage and region-dependent BU99008 behavior.
- Best et al. (2026, DOI `10.1038/s41380-025-03355-9`) show cohort- and smoking-conditioned MAO-B PET interpretation even within one tracer-target family.

Therefore, the glossary had to stop naming `astrocyte / glial-state` as if one generic human astrocyte row existed. The safe site-wide label is a **target-defined astrocyte-related proxy** whose reading still depends on route role.

## 3. Human clearance / transport evidence also does not support one generic glossary row

The human literature already spans different observables, different crossed boundaries, different intervention regimes, and different model burdens.

- Fultz et al. (2019, DOI `10.1126/science.aax5440`) show **macroscopic CSF oscillation** during sleep.
- Kim, Huang, and Liu (2025, DOI `10.1016/j.neuroimage.2025.121142`) measure **parenchyma-CSF water exchange**.
- Eide et al. (2023, DOI `10.1038/s41467-023-37685-5`) combine **intrathecal tracer retention** with **CSF-to-blood clearance-capacity modeling**.
- Hirschler et al. (2025, DOI `10.1038/s41593-025-02073-3`) measure **CSF mobility**, not generic route-free clearance.
- Lim et al. (2025, DOI `10.1038/s41467-025-66548-4`) measure **respiration-enhanced net flow**.
- Yoo et al. (2025, DOI `10.1038/s41467-025-58726-1`) provide an **exercise-conditioned contrast-influx / meningeal-lymphatic-flow** route.
- Dagum et al. (2026, DOI `10.1038/s41467-026-68374-8`) infer **model-based overnight biomarker efflux**.
- Kim et al. (2025, DOI `10.1016/j.cell.2025.02.022`) add mechanistic relevance for the meningeal-lymphatic / microglia axis, but not a route-free human clearance scalar.

Therefore, the glossary needed an explicit **macro clearance-transport proxy family** term and a tighter `clearance / immune support` definition so readers would not overread one family label into one human glymphatic meter or one local immune-controller readout.

## 4. `Support-state proxy` had become too coarse without quantity type or route role

As the site added BBB water exchange, tracer-specific transport, astrocyte PET family splits, and multiple clearance / transport rows, the old `support-state proxy` definition no longer protected against category mistakes. It had to be rewritten so that the label itself reminds the reader that meaning still depends on:

- quantity type
- target class
- transport regime
- direct observable
- route role

# Changes Executed In This Session

- Updated [`glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md) front matter so the page highlights and known points now explicitly name `route role`, `target-defined astrocyte-related proxy`, and `macro clearance-transport proxy family`.
- Rewrote the `When human-evidence terms start sounding like one thing` note so it now lists BBB water exchange, MAO-B / I2BS astrocyte PET, CSF mobility, respiration-conditioned net-flow MRI, exercise-conditioned contrast-influx, and model-based biomarker efflux as distinct rows that should not collapse into one human-visibility impression.
- Added a new glossary term, `Route role`, to stop one family name from sounding like one interchangeable paper row.
- Rewrote `Astrocyte / glial-state` so the human side is framed only through **target-defined astrocyte-related proxies** rather than one generic astrocyte-state meter.
- Added a new glossary term, `Target-defined astrocyte-related proxy`, to encode the site-wide rule that current human astrocyte evidence must still be typed by target and route role.
- Rewrote `Clearance / immune support` so the human side now explicitly separates macroscopic CSF oscillation, parenchyma-CSF water exchange, respiration-conditioned net-flow, exercise-conditioned contrast influx / meningeal-lymphatic flow, intrathecal tracer / CSF-to-blood clearance, CSF mobility, and model-based biomarker efflux.
- Added a new glossary term, `Macro clearance-transport proxy family`, so those routes are no longer forced back into one coarse `glymphatic` word.
- Rewrote `Support-state proxy` so it now states directly that the meaning remains dependent on quantity type or route role.
- Added the missing primary references needed to support those glossary-level distinctions directly on the page.

# Verification

- Ran `git diff --check` with no whitespace or patch-format errors.
- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Confirmed the new glossary terms and route-role language appear in the generated `_site/glossary.html`.

# External Dependency Tasks

- None.
  - This session required only repository inspection, literature review, local editing, site build verification, and Git operations executable in the current environment.

# References

1. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of ^18F-SMBT-1, a Novel ^18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
   - https://doi.org/10.2967/jnumed.121.263254
2. Hiraoka K, Mesfin B, Wu Y, et al. Kinetic and quantitative analysis of [^18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
3. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [^18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
4. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of ^11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
   - https://doi.org/10.2967/jnumed.118.208009
5. Livingston NR, Calsolaro V, Hinz R, et al. Relationship between astrocyte reactivity, using novel ^11C-BU99008 PET, and glucose metabolism, grey matter volume and amyloid load in cognitively impaired individuals. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-021-01429-y
6. Best LM, Truong J, McCluskey T, et al. MAO-B status in alcohol use disorder: a [^11C]SL25.1188 PET imaging study of putative astrogliosis. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
7. Fultz NE, Bonmassar G, Setsompop K, et al. Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. *Science*. 2019.
   - https://doi.org/10.1126/science.aax5440
8. Kim D, Huang Y, Liu J. Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121142
9. Eide PK, Pripp AH, Valnes LM, et al. Intrathecal cerebrospinal fluid tracer clearance to blood is associated with CSF-to-blood clearance capacity and plasma biomarkers. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-37685-5
10. Hirschler L, et al. Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
    - https://doi.org/10.1038/s41593-025-02073-3
11. Lim C, Chen C, Zhang C, et al. Human cerebrospinal fluid net flow enhanced by respiration during the awake state. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-66548-4
12. Yoo R-E, Kim J-H, Moon HY, et al. Long-term physical exercise facilitates putative glymphatic and meningeal lymphatic vessel flow in humans. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-58726-1
13. Dagum P, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
    - https://doi.org/10.1038/s41467-026-68374-8
14. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
    - https://doi.org/10.1016/j.cell.2025.02.022
