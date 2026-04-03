---
title: "2026-04-03 site deepening audit: glossary thermodynamic route-card sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **front-door synchronization bug inside the site's thermodynamic terminology**.

The repository already had a much stricter thermodynamic reading rule on deeper pages:

- route family is not enough
- coarse-graining and state definition matter
- partial observation and memory order matter
- reverse-transition support is separate from null controls
- operational stability is separate from mathematical interpretability
- physiology-side grounding is separate from signal-side irreversibility

However, [`glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md) still described thermodynamic language too briefly for the site's current scientific standard. That made the glossary a new entry point for an old misreading:

- `irreversibility result` = direct physical dissipation
- `named estimator family` = enough to compare papers strongly
- `paired physiology language` = enough to discuss metabolic cost

# Why This Needed Correction

## 1. Estimator-family naming was still too close to claim-ready interpretation

- [Lynn et al. (2021)](https://doi.org/10.1073/pnas.2109889118) estimate entropy-production lower bounds from coarse-grained BOLD state transitions.
- [de la Fuente et al. (2023)](https://doi.org/10.1093/cercor/bhac177) estimate temporal irreversibility from inversion decoding on ECoG.
- [Nartallo-Kaluarachchi et al. (2025)](https://doi.org/10.1073/pnas.2408791122) use directed visibility graphs on MEG.
- [Ishihara & Shimazaki (2025)](https://doi.org/10.1038/s41467-025-66669-w) estimate model-based entropy flow in a nonstationary kinetic-Ising framework.

Critique:

- These papers do not compute one shared quantity.
- But even after separating estimator families, the front door still has to say what remains unresolved:
  - coarse-graining
  - hidden-degree risk
  - finite-data support
  - operational stability
  - physiology-side grounding

Without that extra step, the glossary still teaches a weaker scientific reading than the FAQ and wiki already require.

## 2. Partial observation and memory are not minor technical footnotes

- [Martínez et al. (2019)](https://doi.org/10.1038/s41467-019-11051-w) showed that waiting-time asymmetry can reveal hidden dissipation even when observable current vanishes.
- [Blom et al. (2024)](https://doi.org/10.1073/pnas.2318333121) showed that coarse lumping can hide dissipative cycles and induce memory, which can make naive Markov-style estimates far too small.
- [Baiesi et al. (2024)](https://doi.org/10.1038/s42005-024-01742-2) showed that sparse or missing reverse transitions can break direct entropy-production estimation and motivate lower-bound strategies.

Critique:

- `thermodynamic result` is still too coarse if the glossary does not name hidden-degree risk and reverse-transition support explicitly.
- Otherwise a reader can mistake a neat-looking number for a well-supported near-equilibrium or cost estimate.

## 3. Operational stability and physiology bridges are separate scientific burdens

- [Poudel et al. (2024)](https://doi.org/10.1007/s12021-024-09652-y) showed that small motion materially alters visibility-graph structure and that only selected low-motion metrics reach moderate-to-high test-retest reliability.
- [Metzen et al. (2024)](https://doi.org/10.1002/hbm.26778) showed that BOLD variability and complexity measures have sharply different reliability profiles.
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) showed that simultaneous EEG-PET-MRI can be temporally coupled while still remaining spatially non-identical across modalities.
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) showed that BOLD changes can oppose oxygen-metabolism changes across the cortex.

Critique:

- A mathematically interpretable estimator is not yet a reusable operational metric.
- A paired physiology phrase is not yet an energetic bridge.
- Therefore the glossary needed explicit terms for `stability / nuisance sensitivity`, `cross-estimator concordance`, and `physiology-side grounding / bridge quality`.

# Root Critique

The scientific criticism is precise:

1. The site's deep pages had already become strict.
2. The glossary had not caught up.
3. Because the glossary is a front-door page, that mismatch mattered.
4. If the glossary keeps thermodynamic language too short, the site silently reopens exactly the overread that the FAQ and verification rules were built to stop.

Therefore the correct fix was not a new theory section. The correct fix was to make the glossary itself carry the current route-card stop line.

# Web-Verified Primary Sources Checked On 2026-04-03

- Lynn et al. (2021), PNAS: https://doi.org/10.1073/pnas.2109889118
- de la Fuente et al. (2023), Cerebral Cortex: https://doi.org/10.1093/cercor/bhac177
- Nartallo-Kaluarachchi et al. (2025), PNAS: https://doi.org/10.1073/pnas.2408791122
- Ishihara & Shimazaki (2025), Nature Communications: https://doi.org/10.1038/s41467-025-66669-w
- Martínez et al. (2019), Nature Communications: https://doi.org/10.1038/s41467-019-11051-w
- Blom et al. (2024), PNAS: https://doi.org/10.1073/pnas.2318333121
- Baiesi et al. (2024), Communications Physics: https://doi.org/10.1038/s42005-024-01742-2
- Poudel et al. (2024), Neuroinformatics: https://doi.org/10.1007/s12021-024-09652-y
- Metzen et al. (2024), Human Brain Mapping: https://doi.org/10.1002/hbm.26778
- Chen et al. (2025), Nature Communications: https://doi.org/10.1038/s41467-025-64414-x
- Epp et al. (2025), Nature Neuroscience: https://doi.org/10.1038/s41593-025-02132-9

# Changes Executed In This Session

## Public-facing changes executed

- [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md)
  - updated the page header note, highlights, and known-points so the glossary now explicitly states that the thermodynamic stop line is part of the front-door reading model
  - added a new front-door note box clarifying that thermodynamic words are not promoted to measured cost without route-card disclosure
  - strengthened the `Irreversibility / EPR proxy` and `Irreversibility / Thermodynamic Route Card` entries
  - added glossary rows for:
    - coarse-graining / timescale
    - observed-state closure / hidden-degree risk
    - reverse-transition support / finite-data handling
    - stability / nuisance sensitivity
    - cross-estimator concordance
    - physiology-side grounding / bridge quality
  - rewrote the thermodynamic note box so the front door now names partial-observation, finite-data, stability, and physiology-bridge burdens explicitly
  - expanded the reference list with the newer thermodynamic-support sources needed to justify those entry-level terms

## Non-public or support changes executed

- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_glossary_thermodynamic_route_card_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_glossary_thermodynamic_route_card_sync.md)
  - added this audit note to preserve the criticism, rationale, and source trail

# Misreadings Blocked By This Update

- `thermodynamic result` = direct physical dissipation
- `named estimator family` = enough to compare papers strongly
- `clean null` = adequate reverse-transition support
- `interesting metric` = reusable operational signal
- `paired physiology wording` = metabolism-side grounding solved
- `arrow-of-time` = WBE-ready energetic gate

# Verification

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "When thermodynamic words start sounding too close to measured cost|Reverse-transition support / finite-data handling|Cross-estimator concordance|Physiology-side grounding / bridge quality" glossary.md _site/glossary.html`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: web literature verification, glossary edits, local static-site build, and Git publication.

# References

1. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021. https://doi.org/10.1073/pnas.2109889118
2. de la Fuente LA, Zamberlan F, Bocaccio H, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cerebral Cortex*. 2023. https://doi.org/10.1093/cercor/bhac177
3. Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. *PNAS*. 2025. https://doi.org/10.1073/pnas.2408791122
4. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-66669-w
5. Martínez IA, Bisker G, Horowitz JM, Parrondo JMR. Inferring broken detailed balance in the absence of observable currents. *Nature Communications*. 2019. https://doi.org/10.1038/s41467-019-11051-w
6. Blom K, Song K, Vouga E, Godec A, Makarov DE. Milestoning estimators of dissipation in systems observed at a coarse resolution. *PNAS*. 2024. https://doi.org/10.1073/pnas.2318333121
7. Baiesi M, Falasco G, Moghimi-Araghi S. Effective estimation of entropy production with lacking data. *Communications Physics*. 2024. https://doi.org/10.1038/s42005-024-01742-2
8. Poudel R, et al. Network representation of fMRI data using visibility graphs: the impact of motion and test-retest reliability. *Neuroinformatics*. 2024. https://doi.org/10.1007/s12021-024-09652-y
9. Metzen D, et al. Reliability of variability and complexity measures for task and task-free BOLD fMRI. *Human Brain Mapping*. 2024. https://doi.org/10.1002/hbm.26778
10. Chen Y, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-64414-x
11. Epp SM, Castrillon G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02132-9
