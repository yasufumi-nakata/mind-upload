---
title: "2026-04-03 site deepening audit: thermodynamic route-family versus operability split"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **literature-front-door overcompression inside thermodynamic / irreversibility reading**.

The repository already had a strong route-card treatment on the stricter verification pages:

- route family
- coarse-graining / state definition
- physiology-side grounding

However, the literature-facing entry pages still made it too easy to stop one step too early. In practice, the public reading model could still become:

- `route family identified` = enough to compare papers
- `irreversibility number reported` = enough to discuss energetic meaning

That was too weak, because the current primary literature already supports a second split:

- `reverse-transition / finite-data support`
- `memory order / observed-state closure`
- `operational stability / nuisance sensitivity`
- `physiology-bridge quality`

# Why This Needed Correction

## 1. Route-family labels were still too close to operational comparability

- [Lynn et al. (2021)](https://doi.org/10.1073/pnas.2109889118) is a **coarse-grained lower-bound route** from BOLD state transitions.
- [de la Fuente et al. (2023)](https://doi.org/10.1093/cercor/bhac177) is an **inversion-decoding asymmetry route** on ECoG.
- [Nartallo-Kaluarachchi et al. (2025)](https://doi.org/10.1073/pnas.2408791122) is a **visibility-graph irreversibility route** on MEG.
- [Ishihara & Shimazaki (2025)](https://doi.org/10.1038/s41467-025-66669-w) is a **model-based entropy-flow route** under an explicit kinetic-Ising assumption set.
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) is not another irreversibility estimator at all, but a **physiology-side grounding warning** showing that BOLD changes can oppose oxygen metabolism.

Critique:

- These are not one measurement object.
- But even after this split, they are still not automatically one **comparable operating lane**.
- A literature front door that stops at route-family taxonomy still leaves readers one step short of the real caution.

## 2. Partial observation and reverse-transition support are separate scientific burdens

- [Martínez et al. (2019)](https://doi.org/10.1038/s41467-019-11051-w) showed that waiting-time asymmetry can expose hidden dissipation even when observable current vanishes.
- [Hartich & Godec (2024)](https://doi.org/10.1038/s41467-024-52602-0) showed that this reading can fail when coarse-graining and time reversal do not commute.
- [Martínez et al. (2024)](https://doi.org/10.1038/s41467-024-52603-z) replied by restricting the earlier claim to local-in-time coarse-grainings and, where needed, second-order semi-Markov constructions.
- [Blom et al. (2024)](https://doi.org/10.1073/pnas.2318333121) showed that coarse lumping can hide dissipative cycles and induce memory, making naive Markov reading underestimate dissipation.
- [Baiesi et al. (2024)](https://doi.org/10.1038/s42005-024-01742-2) showed that sparse or missing reverse transitions can force lower-bound strategies instead of direct estimation.

Critique:

- `thermodynamic route family` is still not enough.
- The observed process may be too partially seen, too non-Markov, or too reverse-sparse for the reported number to mean what a quick reader assumes.
- Therefore, reverse-transition support and memory-order disclosure are not technical footnotes; they are part of the claim ceiling.

## 3. Operational stability is another distinct ceiling

- [Poudel et al. (2024)](https://doi.org/10.1007/s12021-024-09652-y) showed that small motion materially alters visibility-graph structure and that only selected low-motion metrics reach moderate-to-high reliability.
- [Metzen et al. (2024)](https://doi.org/10.1002/hbm.26778) showed that BOLD variability and complexity measures do not share one reliability profile; some complexity measures fall into an unacceptable range.
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) showed that simultaneous EEG-PET-MRI can be tightly temporally coupled while still preserving non-identical spatial organization.

Critique:

- A mathematically meaningful metric is not yet a reusable metric.
- Motion sensitivity, denoising dependence, and cross-modal bridge disagreement remain separate burdens.
- If the archive front door does not say this explicitly, readers can silently upgrade `interesting auxiliary signal` into `portable operational metric`.

## 4. This matters for the site's central anti-shortcut rule

The central claim of the site is not only that WBE evidence is incomplete, but that incompleteness persists through **different failure modes** that must not be silently merged.

If the site itself lets thermodynamic route-family labels stand in for operational readiness, it weakens its own strongest methodological point:

- `a route family != a validated comparison lane`
- `an irreversibility number != direct dissipation`
- `a physiology-related phrase != a proven physiology bridge`

# Web-Verified Primary Sources Checked On 2026-04-03

- Lynn et al. (2021), PNAS: https://doi.org/10.1073/pnas.2109889118
- de la Fuente et al. (2023), Cerebral Cortex: https://doi.org/10.1093/cercor/bhac177
- Nartallo-Kaluarachchi et al. (2025), PNAS: https://doi.org/10.1073/pnas.2408791122
- Ishihara & Shimazaki (2025), Nature Communications: https://doi.org/10.1038/s41467-025-66669-w
- Epp et al. (2025), Nature Neuroscience: https://doi.org/10.1038/s41593-025-02132-9
- Martínez et al. (2019), Nature Communications: https://doi.org/10.1038/s41467-019-11051-w
- Hartich & Godec (2024), Nature Communications: https://doi.org/10.1038/s41467-024-52602-0
- Martínez et al. (2024), Nature Communications: https://doi.org/10.1038/s41467-024-52603-z
- Blom et al. (2024), PNAS: https://doi.org/10.1073/pnas.2318333121
- Baiesi et al. (2024), Communications Physics: https://doi.org/10.1038/s42005-024-01742-2
- Poudel et al. (2024), Neuroinformatics: https://doi.org/10.1007/s12021-024-09652-y
- Metzen et al. (2024), Human Brain Mapping: https://doi.org/10.1002/hbm.26778
- Chen et al. (2025), Nature Communications: https://doi.org/10.1038/s41467-025-64414-x

# Changes Executed In This Session

## Literature-facing public pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md)
  - filled the previously empty 2026 technical addendum note box
  - upgraded the thermodynamic front-door note from `route family only` to `route family + reverse-transition / memory-order / stability / physiology-bridge`
  - tightened the thermodynamic row in the priority table
  - tightened the thermodynamic row in the 2025-2026 shortlist
  - tightened the auxiliary thermodynamic evidence-class row so it no longer sounds like a reusable metric by default
- [`/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md`](/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md)
  - strengthened the U10 entry-row criteria in the technical priority route
  - added a new U10 addendum for reverse-transition, memory-order, stability, and physiology-bridge audits
  - expanded the U10 traction and unresolved bullets
  - extended the representative-reference bundles to include the partial-observation and stability literature

# Misreads Blocked By This Update

- `thermodynamic route family identified = papers are now operationally comparable`
- `irreversibility estimate = direct dissipation`
- `clean estimator = stable metric`
- `temporal multimodal coupling = shared physiological object`
- `energetic wording = metabolism was actually measured`

# Verification

- `git diff --check`
- `ruby scripts/build_summary_booklet.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "reverse-transition support|memory order / observed-state closure|stability / nuisance sensitivity|physiology-side bridge quality" mind_uploading_papers.md research_harvest_50.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: web literature verification, markdown edits, local verification, commit, and push.

# References

1. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021.
   - https://doi.org/10.1073/pnas.2109889118
2. de la Fuente LA, Perl YS, Zamberlan F, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cerebral Cortex*. 2023.
   - https://doi.org/10.1093/cercor/bhac177
3. Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. *PNAS*. 2025.
   - https://doi.org/10.1073/pnas.2408791122
4. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66669-w
5. Epp SM, Castrillon G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
6. Martínez IA, Bisker G, Horowitz JM, Parrondo JMR. Inferring broken detailed balance in the absence of observable currents. *Nature Communications*. 2019.
   - https://doi.org/10.1038/s41467-019-11051-w
7. Hartich D, Godec A. Comment on “Inferring broken detailed balance in the absence of observable currents”. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-52602-0
8. Martínez IA, Bisker G, Horowitz JM, Parrondo JMR. Reply to: Comment on “Inferring broken detailed balance in the absence of observable currents”. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-024-52603-z
9. Blom K, Song K, Vouga E, Godec A, Makarov DE. Milestoning estimators of dissipation in systems observed at a coarse resolution. *PNAS*. 2024.
   - https://doi.org/10.1073/pnas.2318333121
10. Baiesi M, Falasco G, Moghimi-Araghi S. Effective estimation of entropy production with lacking data. *Communications Physics*. 2024.
    - https://doi.org/10.1038/s42005-024-01742-2
11. Poudel R, et al. Network Representation of fMRI Data Using Visibility Graphs: The Impact of Motion and Test-Retest Reliability. *Neuroinformatics*. 2024.
    - https://doi.org/10.1007/s12021-024-09652-y
12. Metzen D, et al. Reliability of variability and complexity measures for task and task-free BOLD fMRI. *Human Brain Mapping*. 2024.
    - https://doi.org/10.1002/hbm.26778
13. Chen Y, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-64414-x
