---
title: "2026-04-04 site deepening audit: EEG foundation-model overlap axes"
date: "2026-04-04"
author: "Codex"
---

# Summary

This run selected a **remaining technical weakness in the site's EEG foundation-model guidance**:

- the site already required a `Pretraining Card`
- the direction was scientifically correct
- but the public wording still left `overlap audit` too close to a single yes/no checkbox

That compression is not supported by the current primary literature or by current official benchmark operations.

# Why This Needed Correction

## 1. Raw-window leakage is not the same failure as subject leakage

- [Brookshire et al. (2024)](https://doi.org/10.3389/fnins.2024.1373515) show that segment-based evaluation in translational EEG can leak subject information when segments from the same people appear on both sides of the split.
- Scientific consequence:
  `overlap audit` must at least name raw-recording / window ancestry and subject ancestry separately.

## 2. Subject ancestry is not the same failure as setup ancestry

- [Chaibub Neto et al. (2019)](https://doi.org/10.1038/s41746-019-0178-x) show that repeated-measure diagnostic learning can absorb subject characteristics.
- [Melnik et al. (2017)](https://doi.org/10.3389/fnhum.2017.00150) show that EEG variance comes not only from subjects but also from systems.
- [Xu et al. (2020)](https://doi.org/10.3389/fnhum.2020.00103) show that amplifier, cap, sample-rate, and filtering differences materially degrade cross-dataset EEG decoding.
- Scientific consequence:
  a model can look robust while still leaning on recording-distribution regularities rather than on portable neural structure.

## 3. Setup tolerance is not yet physiology-preserving equivalence

- [Jiang et al. (2024)](https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html) explicitly frame mismatched electrodes, unequal lengths, varied task designs, and low SNR as open EEG-side barriers.
- [El Ouahidi et al. (2025)](https://arxiv.org/abs/2510.21585) push toward setup-agnostic pretraining at large corpus scale.
- Scientific consequence:
  channel/layout tolerance is an advance, but it is still not evidence that reference-family, geometry-route, or physiology-equivalence problems are solved.

## 4. Benchmark object and benchmark operations are separate ancestry axes

- The official [EEG Challenge 2025 data page](https://eeg2025.github.io/data/) shows that one competition family already mixes six cognitive tasks with subject-level psychopathology targets.
- The official [submission page](https://eeg2025.github.io/submission/) fixes an inference-only code competition.
- The official [leaderboard / postmortem](https://eeg2025.github.io/leaderboard/) discloses that Challenge 2 samples were not randomized, so contiguous-trial same-subject structure could be exploited.
- [Xiong et al. (2025)](https://arxiv.org/abs/2508.17742) and [Liu et al. (2026)](https://arxiv.org/abs/2601.17883) both argue that protocol differences still prevent reliable cross-model EEG-FM comparison.
- Scientific consequence:
  `benchmark provenance` is not an administrative add-on. It is part of the scientific object being compared.

# Critical Conclusion

The site's prior `Pretraining Card` was **scientifically pointed in the right direction but still too compressed at one crucial field**.

The required correction was:

1. treat `overlap audit` as **multi-axis**
2. separate at least:
   - raw-recording / window ancestry
   - subject / session ancestry
   - site / device / reference / layout ancestry
   - task / benchmark-object ancestry
   - benchmark-operations ancestry
3. block the common false promotion:
   - `benchmark win` -> `portable generalization`
   - `setup tolerance` -> `physiology-preserving invariance`
   - `mixed-task transfer` -> `universal EEG decoder`

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - updated the public `Pretraining Card` summary line in front matter
  - strengthened the main addendum paragraph with evidence that overlap failure has distinct routes
  - rewrote the `corpus identity / overlap audit` row as a multi-axis requirement
  - added a new public correction table that names five ancestry axes explicitly
  - tightened the minimum operating rule so missing axis separation now blocks strong transfer language

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-foundation-models.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-foundation-models.md)
  - updated the learning page summary / known-point wording
  - strengthened Gate G1 from a generic overlap check to a multi-axis audit
  - added a correction note explaining why overlap must split by ancestry axis
  - rewrote the `Corpus` item in the page-local Pretraining Card
  - added Brookshire et al. (2024) to the references

- [`/Users/yasufumi/Documents/GitHub/mind-upload/github-wiki-export/eeg-foundation-models.md`](/Users/yasufumi/Documents/GitHub/mind-upload/github-wiki-export/eeg-foundation-models.md)
  - synchronized the same public correction into the GitHub Wiki export copy

# External Dependency Tasks

None.

This pass stayed within executable repository work: source verification, page edits, local build checks, and Git operations.

# Verification

- `git pull --rebase --autostash`
- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "multi-axis overlap audit|overlap audit is multi-axis|ancestry axis" verification.md wiki/eeg-foundation-models.md github-wiki-export/eeg-foundation-models.md`

# References

1. Brookshire G, Kasper J, Blauch NM, Wu YC, Glatt R, Merrill DA, Gerrol S, Yoder KJ, Quirk C, Lucero C. Data leakage in deep learning studies of translational EEG. *Frontiers in Neuroscience*. 2024. https://doi.org/10.3389/fnins.2024.1373515
2. Chaibub Neto E, Pratap A, Perumal TM, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019. https://doi.org/10.1038/s41746-019-0178-x
3. Melnik A, Legkov P, Izdebski K, et al. Systems, Subjects, Sessions: To What Extent Do These Factors Influence EEG Data? *Frontiers in Human Neuroscience*. 2017. https://doi.org/10.3389/fnhum.2017.00150
4. Xu M, Yao S, Wei Z, et al. Cross-dataset variability problem in EEG decoding with deep learning. *Frontiers in Human Neuroscience*. 2020. https://doi.org/10.3389/fnhum.2020.00103
5. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR 2024*. https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
6. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML 2025 / PMLR 267*. https://proceedings.mlr.press/v267/lee25a.html
7. El Ouahidi Y, Lys J, Thölke P, Farrugia N, Pasdeloup B, Gripon V, Jerbi K, Lioi G. REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025. https://arxiv.org/abs/2510.21585
8. EEG Challenge. Data. 2025. https://eeg2025.github.io/data/
9. EEG Challenge. Submission. 2025. https://eeg2025.github.io/submission/
10. EEG Challenge. Leaderboard. 2025. https://eeg2025.github.io/leaderboard/
11. Xiong W, Li J, Li J, Zhu K. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025. https://arxiv.org/abs/2508.17742
12. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026. https://arxiv.org/abs/2601.17883
