---
title: "2026-04-03 site deepening audit: beginner neuromodulatory route-family split"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **remaining beginner-level compression inside human neuromodulatory evidence**.

The repository had already become stricter on:

- human proxy composition
- measurement-stack claim ceilings
- literature-facing route-family splits

However, the beginner technical front door in [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/mind-upload-basics.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/mind-upload-basics.md) still made it too easy to jump from:

- `human neuromodulatory evidence exists`

to:

- `human neuromodulatory state is now fairly directly observed`

That shortcut is not supported by the current primary literature.

# Why This Needed Correction

## 1. Mixed arousal proxy is not a transmitter-specific route

- [Carro-Domínguez et al. (2025)](https://doi.org/10.1038/s41467-025-57289-5) used pupil size during human sleep as an arousal-linked proxy coupled to spindle clusters and stimulation responses.

Critique:

- This is a scientifically useful route, but it is still a **mixed arousal proxy**.
- It is not a direct readout of one named transmitter field, receptor occupancy, or endogenous release state.

## 2. Receptor / transporter atlases are normative priors, not same-subject current-state readouts

- [Hansen et al. (2022)](https://doi.org/10.1038/s41593-022-01186-3) built cortical receptor / transporter maps from more than 1,200 healthy individuals.
- [Nakuci & Bansal (2025)](https://doi.org/10.1038/s42003-025-08492-z) used those maps as a PET-informed modeling scaffold for spontaneous BOLD activity.

Critique:

- These are important advances in **normative chemoarchitectural prior** and **modeling scaffold**.
- They are not same-subject current occupancy or same-subject moment-to-moment transmitter dynamics.

## 3. Occupancy PET is not the same route as release-sensitive PET

- [Wong et al. (2013)](https://doi.org/10.1007/s00213-013-3103-z) constrained dopamine D2 occupancy under administered lurasidone.
- [Erritzoe et al. (2020)](https://doi.org/10.1038/s41386-019-0567-5) constrained serotonin release under d-amphetamine challenge with [11C]CIMBI-36.
- [Miederer et al. (2025)](https://doi.org/10.2967/jnumed.124.268317) constrained task-linked dopamine release proxy with [18F]fallypride during cognitive flexibility.

Critique:

- **Occupancy PET** asks whether a named ligand engaged a named target under an administered compound.
- **Release-sensitive PET** asks whether a named challenge displaced binding strongly enough to support a bounded endogenous-release interpretation.
- They are not the same evidence row and should not be allowed to merge at the beginner layer.

## 4. This mattered because the beginner page is a real front door

The site's stronger route-family logic already existed elsewhere. But a beginner page that still starts too high on the abstraction ladder weakens the whole reading order.

The correct beginner order is now:

1. family-internal comparison family
2. proxy class / quantity type / route role
3. operational maturity
4. safe calibrator role

Without that order, the page still permits the false reading that `mixed arousal proxy`, `atlas prior`, `occupancy PET`, and `challenge-linked release PET` are four versions of one nearly direct human neuromodulatory meter.

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/mind-upload-basics.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/mind-upload-basics.md)
  - updated the beginner rule from `three axes only` to `family-internal comparison family first`
  - added a new correction note explaining why neuromodulatory evidence must split before the three axes are read
  - added four new rows to the human observability ladder:
    - mixed-arousal proxy in sleep
    - receptor / transporter atlas prior
    - occupancy PET
    - challenge-linked displacement / release-sensitive PET
  - expanded front-matter highlights and known points to block neuromodulatory overcompression
  - extended the references list with the primary literature used in the correction

# Misreads Blocked By This Update

- `human neuromodulatory evidence exists` = `human neuromodulatory state is fairly directly observed`
- `mixed arousal proxy = receptor / transporter atlas prior = occupancy PET = release-sensitive PET`
- `occupancy PET = endogenous release`
- `atlas prior = same-subject current transmitter state`
- `challenge-linked release proxy = route-free whole-brain current neuromodulatory state`

# Verification

- `git diff --check`
- `ruby scripts/build_summary_booklet.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "family-internal comparison family|mixed-arousal proxy|receptor / transporter atlas prior|Human occupancy PET|release-sensitive PET" wiki/mind-upload-basics.md`

# External Dependency Tasks

- None.
  - This run stayed within executable repository work: primary-literature verification, repo edits, local build validation, and Git operations.

# References

1. Carro-Domínguez M, Huwiler S, Oberlin S, et al. Pupil size reveals arousal level fluctuations in human sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57289-5
2. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022. https://doi.org/10.1038/s41593-022-01186-3
3. Nakuci J, Bansal K. The neuroreceptors and transporters underlying spontaneous brain activity. *Communications Biology*. 2025. https://doi.org/10.1038/s42003-025-08492-z
4. Wong DF, Kuwabara H, Brašić JR, et al. Determination of dopamine D2 receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. *Psychopharmacology*. 2013. https://doi.org/10.1007/s00213-013-3103-z
5. Erritzoe D, Ashok AH, Searle GE, et al. Serotonin release measured in the human brain: a PET study with [11C]CIMBI-36 and d-amphetamine challenge. *Neuropsychopharmacology*. 2020. https://doi.org/10.1038/s41386-019-0567-5
6. Miederer I, Buchholz H-G, Rademacher L, et al. Dopaminergic Mechanisms of Cognitive Flexibility: An [18F]Fallypride PET Study. *Journal of Nuclear Medicine*. 2025. https://doi.org/10.2967/jnumed.124.268317
