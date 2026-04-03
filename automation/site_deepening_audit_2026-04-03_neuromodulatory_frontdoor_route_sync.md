---
title: "2026-04-03 site deepening audit: neuromodulatory front-door route sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **public front-door lag in the site's neuromodulatory taxonomy**.

The wiki-side composition rules had already separated four non-equivalent human evidence families:

- mixed arousal proxy
- receptor / transporter atlas prior
- occupancy PET
- challenge-linked release-sensitive PET

But key public pages still relied mainly on older example sets or broader labels. In practice, that left two overreads too easy:

- `occupancy PET ~= endogenous release`
- `atlas prior / arousal proxy / occupancy / release proxy ~= one current neuromodulatory state row`

I therefore chose the public front door itself as the next update target and synced the newer 2025 primary literature into the central public pages.

# Why This Needed Correction

## 1. The central synthesis page still compressed neuromodulation too early

[`/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md`](/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md) still had a top-level row named `neuromodulator / glia imaging`.

That was scientifically too coarse, because the current primary literature already splits at least four human neuromodulatory route families:

- [Carro-Domínguez et al. (2025)](https://doi.org/10.1038/s41467-025-57289-5): mixed arousal proxy in human sleep
- [Hansen et al. (2022)](https://doi.org/10.1038/s41593-022-01186-3) and [Nakuci & Bansal (2025)](https://doi.org/10.1038/s42003-025-08492-z): receptor / transporter atlas prior and modeling scaffold
- [Wong et al. (2013)](https://doi.org/10.1007/s00213-013-3103-z) and [Schlosser et al. (2025)](https://doi.org/10.3389/fnins.2025.1651016): administered-drug occupancy routes, including informative null occupancy
- [Koepp et al. (1998)](https://doi.org/10.1038/30498), [Erritzoe et al. (2020)](https://doi.org/10.1038/s41386-019-0567-5), and [Miederer et al. (2025)](https://doi.org/10.2967/jnumed.124.268317): challenge-linked release-sensitive routes

Those papers do not observe one shared object.

## 2. The public human-observability ladder was still missing one important human row

[`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md) already told readers not to compress neuromodulatory evidence.

But the ladder itself still moved directly from synaptic-density PET to receptor / transporter atlas priors and PET routes, without a dedicated human `mixed arousal proxy` row.

That mattered because [Carro-Domínguez et al. (2025)](https://doi.org/10.1038/s41467-025-57289-5) show a real human route that still remains upstream of transmitter-specific interpretation. If that rung is missing, the reader can silently promote `human sleep arousal evidence` into `human transmitter-state evidence`.

## 3. The older public wording underused the newest 2025 counterexamples

Two newer papers were especially important for stopping overread:

- [Schlosser et al. (2025)](https://doi.org/10.3389/fnins.2025.1651016) show that a higher ketamine dose still yielded SERT occupancy that did **not significantly differ from zero**.
- [Miederer et al. (2025)](https://doi.org/10.2967/jnumed.124.268317) show a task-switching dopamine-release proxy in a named region and bounded design.

Together, they sharpen the difference between:

- `did the administered compound occupy the target?`
- `did the named task / challenge alter binding enough to support a bounded release proxy?`

If the public pages do not name that split explicitly, the current ceiling becomes easier to overread than the primary literature allows.

# Root Critique

The criticism is straightforward:

1. `pupil-size arousal proxy` is not `transmitter-specific measurement`.
2. `receptor / transporter atlas prior` is not `same-subject current state`.
3. `occupancy PET` is not `endogenous release`.
4. `challenge-linked release proxy` is not `continuous whole-brain transmitter field`.
5. `astrocyte-state causality` is not the same row as any of the above neuromodulatory routes.

Therefore, a central public page must not re-compress those objects after the wiki has already separated them.

# Other Improvement Candidates Observed

These also remain worth future work, but they were secondary to the front-door neuromodulatory lag:

- `faq.md` still uses an older public example mix for neuromodulatory routes and could be refreshed next.
- `summary_booklet.md` is safe on truncation now, but it still inherits whichever front-matter stop lines are strongest on the source pages, so further front-matter tightening may still improve booklet emphasis.

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - added a dedicated human `mixed arousal proxy in sleep` row
  - updated the receptor / transporter atlas row with the 2025 modeling-scaffold paper
  - updated the occupancy PET row with the 2025 informative-null occupancy paper
  - updated the release-sensitive PET row with the 2025 task-switching dopamine proxy paper
  - tightened the public note boxes so occupancy-versus-release and atlas-versus-current-state are explicit at the entry layer
- [`/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md`](/Users/yasufumi/Documents/GitHub/mind-upload/perspective.md)
  - split the old `neuromodulator / glia imaging` row into separate `human neuromodulatory proxy family` and `astrocyte / glia state routes`
  - updated the human-route table so receptor-prior, occupancy, and release-sensitive rows reflect the newer 2025 examples
  - tightened the central synthesis notes so current public reading rules match the wiki-side composition rules
  - extended the references list with the new primary sources
- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_neuromodulatory_frontdoor_route_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_neuromodulatory_frontdoor_route_sync.md)
  - added this audit note to preserve the criticism, rationale, and reference trail

# Verification

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "Carro-Dom|Nakuci|Schlosser|Miederer|mixed arousal proxy in sleep|informative null occupancy" wbe_101.md perspective.md automation/site_deepening_audit_2026-04-03_neuromodulatory_frontdoor_route_sync.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown edits, local build verification, and Git publication.

# References

1. Carro-Domínguez M, Huwiler S, Oberlin S, et al. Pupil size reveals arousal level fluctuations in human sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57289-5
2. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022. https://doi.org/10.1038/s41593-022-01186-3
3. Nakuci J, Bansal K. The neuroreceptors and transporters underlying spontaneous brain activity. *Communications Biology*. 2025. https://doi.org/10.1038/s42003-025-08492-z
4. Wong DF, Kuwabara H, Hsu DJ, et al. Determination of dopamine D2 receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. *Psychopharmacology*. 2013. https://doi.org/10.1007/s00213-013-3103-z
5. Schlosser G, Murgaš M, Godbersen GM, et al. Human in vivo assessment of ketamine binding of the serotonin transporter-follow up at a higher dose. *Frontiers in Neuroscience*. 2025. https://doi.org/10.3389/fnins.2025.1651016
6. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998. https://doi.org/10.1038/30498
7. Erritzoe D, Ashok AH, Searle GE, et al. Serotonin release measured in the human brain: a PET study with [11C]CIMBI-36 and d-amphetamine challenge. *Neuropsychopharmacology*. 2020. https://doi.org/10.1038/s41386-019-0567-5
8. Miederer I, Buchholz H-G, Rademacher L, et al. Dopaminergic Mechanisms of Cognitive Flexibility: An [18F]Fallypride PET Study. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268317
