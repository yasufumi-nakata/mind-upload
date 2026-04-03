---
title: "2026-04-04 site deepening audit: EEG preprocessing recording-frame contract"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **scientifically under-specified harmonization story** on the EEG preprocessing page.

[`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-preprocessing-and-qc.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-preprocessing-and-qc.md) already separated:

- filtering
- artifact handling
- leakage control
- dataset splitting
- derivative logging

That was directionally correct.

But one important compression still remained:

- the page still risked sounding as if `harmonization` were one background cleanup step
- rather than a **recording-frame contract** that changes what kind of cross-dataset comparison is being claimed

That simplification is no longer defensible under current technical and natural-science literature.

# Why This Needed Correction

## 1. EEG comparison depends on the recording frame, not only on cleanup quality

EEG-BIDS already requires researchers to separate:

- electrode positions
- channel definitions
- coordinate systems
- reference description

This is not bookkeeping noise.

It is part of the measurement condition itself.

Once different datasets use different:

- channel layouts
- coordinate routes
- reference families
- omission policies

the comparison target is no longer fixed by saying only that preprocessing was `standardized`.

Therefore the page needed to state explicitly that preprocessing is partly a **claim contract about measurement comparability**.

## 2. Common-channel reduction, interpolation, and REST-based transformation are not the same operation

The earlier page language compressed harmonization into a single bucket.

That was too weak.

These branches solve different problems and preserve different objects:

- `common-channel intersection` preserves only the shared observed subset and often discards spatial coverage
- `interpolation to a target montage` restores a denser display space but introduces a model-based estimate
- `REST / coordinate transformation` aims at cross-layout comparability in a transformed frame, not raw identity of measurements

Current literature supports treating these as separate methodological choices rather than interchangeable cleanup details.

## 3. Cross-dataset decoding sensitivity is now an explicit warning sign

Recent benchmarking work shows that preprocessing decisions can materially reshape downstream decoding behavior.

That means the site should not let readers carry away the weaker intuition that once artifacts are reduced, the remaining representation is effectively stable across datasets.

The scientific stop line is stronger:

- preprocessing changes benchmark objects
- harmonization changes comparison objects
- therefore both must be disclosed as part of the claim

# Root Critique

The criticism is precise:

1. The page already treated preprocessing as more than cosmetic cleanup.
2. But it still under-described the measurement consequences of montage / coordinate / reference mismatch.
3. Current literature does not support collapsing all harmonization routes into one generic `aligned dataset` label.
4. Therefore the page had to distinguish the recording-frame contract explicitly and force disclosure of the harmonization branch.

The corrected rule is now:

`artifact control` does not by itself establish `cross-dataset comparability`

and

`harmonized` does not by itself mean `same measurement object`

# Web-Verified Primary Sources Checked On 2026-04-04

- EEG-BIDS specification: https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- BIDS Derivatives specification: https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html
- COBIDAS-MEEG reporting recommendations: https://www.biorxiv.org/content/10.1101/2024.11.06.622359v1.full.pdf
- Kessler et al. (2025), *Communications Biology*: https://doi.org/10.1038/s42003-025-08464-3
- Brookshire et al. (2024), *Frontiers in Neuroscience*: https://doi.org/10.3389/fnins.2024.1373515
- Del Pup et al. (2025), *Computers in Biology and Medicine*: https://doi.org/10.1016/j.compbiomed.2025.110608
- Hu et al. (2018), *Journal of Neural Engineering*: https://doi.org/10.1088/1741-2552/aaa13f
- Melnik et al. (2017), *Frontiers in Human Neuroscience*: https://doi.org/10.3389/fnhum.2017.00150
- Xu et al. (2020), *Frontiers in Human Neuroscience*: https://doi.org/10.3389/fnhum.2020.00103
- Dong et al. (2024), *Brain Research Bulletin*: https://doi.org/10.1016/j.brainresbull.2024.111064

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-preprocessing-and-qc.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-preprocessing-and-qc.md)
  - rewrote the page framing so preprocessing is defined as part of a `claim contract`
  - added a `2026-04-04 correction` box making the recording-frame problem explicit
  - replaced the old harmonization wording with a recording-frame contract / harmonization gate
  - rewrote the harmonization section so it now distinguishes:
    - common-channel intersection
    - interpolation to a target montage
    - REST / coordinate transformation
  - tightened the minimum evidence requirements so authors must log:
    - original channel map
    - coordinate system
    - raw reference and rereference family
    - omitted / interpolated channel policy
    - harmonization route
  - added a new misreading row clarifying that `harmonized` does not imply raw equivalence
  - corrected reference metadata, including the Dong 2024 DOI and the Huang et al. author line

- [`/Users/yasufumi/Documents/GitHub/mind-upload/github-wiki-export/eeg-preprocessing-and-qc.md`](/Users/yasufumi/Documents/GitHub/mind-upload/github-wiki-export/eeg-preprocessing-and-qc.md)
  - mirrored the substantive wiki changes in the GitHub wiki export copy

- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_eeg_preprocessing_recording_frame_contract.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_eeg_preprocessing_recording_frame_contract.md)
  - added this audit note so the critique, source trail, and executed corrections remain inspectable

# Verification

The following checks were executed in this run:

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "recording-frame contract|common-channel intersection|REST / coordinate transformation|111064|Huang Y" wiki/eeg-preprocessing-and-qc.md github-wiki-export/eeg-preprocessing-and-qc.md automation/site_deepening_audit_2026-04-04_eeg_preprocessing_recording_frame_contract.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown revision, static-site build, and Git publication.

# References

1. Brain Imaging Data Structure. Electroencephalography. BIDS Specification. https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
2. Brain Imaging Data Structure. Derivatives. BIDS Specification. https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html
3. Pernet C, Appelhoff S, Gorgolewski KJ, et al. COBIDAS report for MEEG: Methodological reporting recommendations for reproducible electroencephalography and magnetoencephalography research. *bioRxiv*. 2024. https://www.biorxiv.org/content/10.1101/2024.11.06.622359v1
4. Kessler M, Mints M, Castaño-Candamil S, et al. Preprocessing choices shape EEG decoding. *Communications Biology*. 2025. https://doi.org/10.1038/s42003-025-08464-3
5. Brookshire G, Bowers M, Hansen N, et al. Focusing on neural activity can misrepresent electrophysiological signals. *Frontiers in Neuroscience*. 2024. https://doi.org/10.3389/fnins.2024.1373515
6. Del Pup L, Alschuler A, Dauwels J, et al. Large-scale benchmarking of EEG preprocessing for machine learning: a systematic review and practical guide. *Computers in Biology and Medicine*. 2025. https://doi.org/10.1016/j.compbiomed.2025.110608
7. Hu S, Stead M, Dai Q, Worrell GA. On the recording reference contribution to EEG correlation, phase synchronization, and causality measures. *Journal of Neural Engineering*. 2018. https://doi.org/10.1088/1741-2552/aaa13f
8. Melnik A, Legkov P, Izdebski K, et al. Systems, subjects, sessions: To what extent do these factors influence EEG data? *Frontiers in Human Neuroscience*. 2017. https://doi.org/10.3389/fnhum.2017.00150
9. Xu H, Plataniotis KN, Brown MSA. Intra-subject and inter-subject diagnostic tests for cross-subject and cross-dataset seizure prediction. *Frontiers in Human Neuroscience*. 2020. https://doi.org/10.3389/fnhum.2020.00103
10. Dong L, Yang R, Xie A, et al. Transforming of scalp EEGs with different channel locations by REST for comparative study. *Brain Research Bulletin*. 2024;217:111064. https://doi.org/10.1016/j.brainresbull.2024.111064
