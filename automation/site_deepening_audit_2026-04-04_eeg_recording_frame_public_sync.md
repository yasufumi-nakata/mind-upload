---
title: "2026-04-04 site deepening audit: EEG recording-frame public sync"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **public-page under-specification of EEG recording-frame comparability**.

By 2026-04-04, the deeper wiki page [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-preprocessing-and-qc.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-preprocessing-and-qc.md) had already become stricter:

- setup metadata were part of the observation model
- harmonization was a recording-frame contract
- `common-channel intersection`
- `interpolation to a target montage`
- `REST-based transformation`

were no longer treated as one interchangeable `harmonized EEG` object

However, several public / front-door pages were still scientifically weaker:

- [`/Users/yasufumi/Documents/GitHub/mind-upload/eeg_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/eeg_101.md)
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
- [`/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md`](/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md)
- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)

That gap mattered because the site's public front door still risked leaving readers with two false impressions:

1. preprocessing is mainly waveform cleanup
2. `harmonized` means one comparable or raw-equivalent EEG object

# Why This Needed Correction

## 1. The official measurement standard already treats setup metadata as part of the measurement condition

The official EEG-BIDS specification does not compress EEG acquisition into one raw waveform file.

It explicitly separates:

- `*_channels.tsv`
- `*_electrodes.tsv`
- `*_coordsystem.json`
- reference and ground disclosure
- filter disclosure

That means the current community standard already treats channel identity, electrode identity, coordinate system, and reference scheme as part of the recording definition rather than as cosmetic metadata.

Therefore, a public page that still lets readers read setup differences as one background nuisance is weaker than the formal measurement standard.

## 2. Primary literature does not support one generic `harmonized EEG` label

- [Hu et al. (2018)](https://pubmed.ncbi.nlm.nih.gov/29368697/) showed that measured scalp potentials depend on both **reference montage** and **electrode setup**.
- [Melnik et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/28424600/) quantified variance contributions from **systems**, **subjects**, and **sessions**, showing that the recording system itself is not negligible.
- [Xu et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/32372929/) showed that **cross-dataset variability** weakens deep-learning EEG generalization.
- [Dong et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39232993/) did not claim generic harmonization; they validated one explicit **REST-based transformation** route for channel-location harmonization and reported high correlation rather than raw identity by default.
- [Kessler et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/40640472/) showed that preprocessing choices can materially change decoding performance and that artifact handling can improve interpretability while reducing classification performance.

Critique:

- `common-channel intersection` is not the same object as `interpolation to a target montage`
- `interpolation` is not the same object as `REST-based transformation`
- a validated REST route is not evidence that every unnamed harmonization branch is equivalent
- a paper that says only `harmonized across setups` still leaves the measurement object under-specified

The stronger rule is therefore an inference from the sources:

- setup diversity must be read through a **recording-frame contract**
- `harmonized EEG` is not one self-interpreting object

## 3. The public pages also contained stale / incorrect citation links

The public-side pages above still pointed to:

- `10.1088/1741-2552/aacfe4` for the Hu EEG setup paper
- `10.1016/j.brainresbull.2024.110906` for the Dong REST harmonization paper

Those were not the correct source identifiers for the claims being made.

The verified public-source corrections are:

- Hu et al. (2018): `10.1088/1741-2552/aaa13f`
- Dong et al. (2024): `10.1016/j.brainresbull.2024.111064`

This was not a cosmetic bibliography fix. It weakened the site's evidence trail exactly where the site asks readers to inspect measurement conditions carefully.

# Root Critique

The scientific criticism is therefore:

1. The deeper EEG wiki already had the stricter measurement rule.
2. Several public pages still presented a weaker front door.
3. Current official standards and primary literature do not support one generic `harmonized EEG` object.
4. Some of the public citation links for that exact claim were stale or incorrect.
5. Therefore the site needed a public-side sync that:
   - corrected the source trail
   - promoted `recording-frame contract` language into the front door
   - explicitly split `common-channel intersection`, `interpolation`, and `REST-based transformation`

# Web-Verified Primary Sources Checked On 2026-04-04

- EEG-BIDS specification: https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- EEG-BIDS paper: https://www.nature.com/articles/s41597-019-0104-8
- Hu et al. (2018) PubMed: https://pubmed.ncbi.nlm.nih.gov/29368697/
- Melnik et al. (2017) PubMed: https://pubmed.ncbi.nlm.nih.gov/28424600/
- Xu et al. (2020) PubMed: https://pubmed.ncbi.nlm.nih.gov/32372929/
- Dong et al. (2024) PubMed: https://pubmed.ncbi.nlm.nih.gov/39232993/
- Kessler et al. (2025) PubMed: https://pubmed.ncbi.nlm.nih.gov/40640472/

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/eeg_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/eeg_101.md)
  - updated `last_updated` to `2026-04-04`
  - promoted recording-frame contract language to the public primer
  - corrected the Hu and Dong source links
  - added the explicit split among `common-channel intersection`, `interpolation`, and `REST-based transformation`
  - tightened the entry-level reading rule and preprocessing stage wording

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - added a front-door highlight that `harmonized EEG` is not one checkbox
  - strengthened the EEG foundation-model FAQ answer so `works across setups` must still disclose the recording-frame branch
  - required `harmonization branch` in the short stop rule

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md`](/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md)
  - updated `last_updated` to `2026-04-04`
  - replaced the weaker acquisition-distribution note with a recording-frame contract correction
  - corrected the Hu and Dong source links
  - made the dataset-card rule require named harmonization branches

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - synchronized the core verification page to the stricter recording-frame rule
  - corrected the Hu and Dong source links
  - strengthened the `harmonization policy` row so it now requires naming the branch, not only generic harmonization disclosure

- Added [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_eeg_recording_frame_public_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_eeg_recording_frame_public_sync.md)
  - records the critique, source trail, and public-page synchronization logic

# Verification

The following checks were planned for this run after editing:

- `git diff --check`
- `ruby scripts/build_summary_booklet.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "recording-frame contract|common-channel intersection|REST-based transformation|aaa13f|111064|harmonization branch" eeg_101.md faq.md datasets.md verification.md summary_booklet.md automation/site_deepening_audit_2026-04-04_eeg_recording_frame_public_sync.md`

# External Dependency Tasks

- None.
  - This run stays inside executable repository work: source verification, markdown revision, static-site regeneration, verification, and Git publication.

# References

1. Brain Imaging Data Structure. Electroencephalography. BIDS Specification. https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
2. Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Scientific Data*. 2019. https://www.nature.com/articles/s41597-019-0104-8
3. Hu S, Lai Y, Valdes-Sosa PA, Bringas-Vega ML, Yao D. How do reference montage and electrodes setup affect the measured scalp EEG potentials? *Journal of Neural Engineering*. 2018. https://pubmed.ncbi.nlm.nih.gov/29368697/
4. Melnik A, Legkov P, Izdebski K, et al. Systems, Subjects, Sessions: To What Extent Do These Factors Influence EEG Data? *Frontiers in Human Neuroscience*. 2017. https://pubmed.ncbi.nlm.nih.gov/28424600/
5. Xu L, Xu M, Ke Y, An X, Liu S, Ming D. Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. *Frontiers in Human Neuroscience*. 2020. https://pubmed.ncbi.nlm.nih.gov/32372929/
6. Dong L, Yang R, Xie A, et al. Transforming of scalp EEGs with different channel locations by REST for comparative study. *Brain Research Bulletin*. 2024. https://pubmed.ncbi.nlm.nih.gov/39232993/
7. Kessler R, Enge A, Skeide MA. How EEG preprocessing shapes decoding performance. *Communications Biology*. 2025. https://pubmed.ncbi.nlm.nih.gov/40640472/
