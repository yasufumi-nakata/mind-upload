---
title: "2026-04-04 site deepening audit: EEG foundation-model front-door route split"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **front-door compression bug inside the EEG foundation-model lane**.

By 2026-04-04, the deeper pages already separated at least four different evidence objects:

- `representation learning / efficiency`
- `recording-frame compatibility`
- `label-limited adaptation rescue`
- `benchmark governance / postmortem fragility`

However, the literature-entry table in `mind_uploading_papers.md` still compressed these into one row, and the FAQ answer still carried most of the split only in dense prose. That made it too easy for a reader to treat one setup paper, one adaptation result, or one leaderboard as if all of them already described one common `general EEG decoder` frontier.

# Why This Needed Correction

## 1. The current literature does not support one generic `EEG foundation model progress` row

- [Kostas et al. (2021)](https://doi.org/10.3389/fnhum.2021.653659), [Jiang et al. (2024)](https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf), and [Lee et al. (2025)](https://proceedings.mlr.press/v267/lee25a.html) constrain a **representation-learning / efficiency** lane.
- [Han et al. (2025)](https://arxiv.org/abs/2507.14141), [Chen et al. (2025)](https://arxiv.org/abs/2510.12515), and [El Ouahidi et al. (2025)](https://arxiv.org/abs/2510.21585) constrain a **recording-frame compatibility** lane.
- [Ma et al. (2026)](https://arxiv.org/abs/2602.17251) supports a **label-limited adaptation rescue** lane.
- The official [EEG Challenge (2025) homepage](https://eeg2025.github.io/), [rules](https://eeg2025.github.io/rules/), [submission page](https://eeg2025.github.io/submission/), and [leaderboard](https://eeg2025.github.io/leaderboard/), together with [Xiong et al. (2025)](https://arxiv.org/abs/2508.17742), [Liu et al. (2026)](https://arxiv.org/abs/2601.17883), and [Lahiri et al. (2026)](https://arxiv.org/abs/2603.02268), constrain a **benchmark-governance / postmortem fragility** lane.

These are not interchangeable advances. A paper that improves arbitrary-layout compatibility does not by itself show that benchmark governance is fixed. A paper that rescues transfer under limited labels does not by itself show that the pretrained representation transferred without rescue. A leaderboard postmortem does not by itself show a stronger model representation.

## 2. The front door had drifted away from the site's own deeper route-card logic

Before this run:

- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-foundation-models.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-foundation-models.md) already distinguished setup compatibility, adaptation regime, benchmark object, and benchmark governance.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md) already required the `Pretraining Card`.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md) already mentioned several of these distinctions, but mainly through dense prose.
- [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md) still exposed the literature-entry table as one merged `EEG foundation models / pretraining governance` row.

That drift mattered because the paper-collection table is a true front-door artifact. If it stays more compressed than the route-card layer, the reader can re-import exactly the shortcut that the deeper pages already block.

# Changes Executed In This Session

## Public pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md)
  - updated `last_updated` to `2026-04-04`
  - replaced the old single EEG foundation-model summary bullet with a four-lane statement in `known_points`
  - added a new note box explaining why the lane must be split into `representation learning / efficiency`, `recording-frame compatibility`, `label-limited adaptation rescue`, and `benchmark governance / postmortem`
  - replaced the single technical-frontier row with four route-specific rows
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - updated `last_updated` to `2026-04-04`
  - tightened the `Q1c2` answer so the four-way split is visible at a glance
  - added a compact table mapping each route family to what it directly advances and what still must stop there

## Audit trail

- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_eeg_foundation_frontdoor_route_split.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_eeg_foundation_frontdoor_route_split.md)
  - recorded the critique, executed changes, verification, and references for this run

# Main Critique

The site's deep EEG foundation-model logic was already stricter than many public summaries. The remaining weakness was therefore not lack of research depth, but **inconsistency between the route-card layer and the literature-entry layer**. In a project that explicitly argues that benchmark object, coordinate route, adaptation regime, and governance must remain separate, keeping one front-door row for all EEG foundation-model progress was scientifically weaker than the standard already enforced elsewhere on the site.

The correction was to make the front door carry the same burden as the deeper pages. That change is modest in file count, but it matters because it changes the reader's very first decomposition of the literature.

# Verification

- Ran `git diff --check`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Re-read the modified `faq.md` and `mind_uploading_papers.md` sections to confirm that the four-lane split now appears both in the paper-entry table and in the short FAQ answer.

# External Dependency Tasks

- None.
  - This session stayed inside executable repository work: source verification, public-content edits, local build validation, and Git operations.

# References

1. Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Frontiers in Human Neuroscience*. 2021.
   - https://doi.org/10.3389/fnhum.2021.653659
2. Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR 2024*.
   - https://proceedings.iclr.cc/paper_files/paper/2024/file/47393e8594c82ce8fd83adc672cf9872-Paper-Conference.pdf
3. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *ICML / PMLR*. 2025.
   - https://proceedings.mlr.press/v267/lee25a.html
4. EEG Challenge (2025). Homepage.
   - https://eeg2025.github.io/
5. EEG Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
6. EEG Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
7. EEG Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
8. Xiong W, Li J, Li J, Zhu K, Jiang C. EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. *arXiv*. 2025.
   - https://arxiv.org/abs/2508.17742
9. Han DD, Lee AL, Lee T, et al. DIVER-0: A Fully Channel Equivariant EEG Foundation Model. *arXiv*. 2025.
   - https://arxiv.org/abs/2507.14141
10. Chen Z, Qin C, You W, et al. HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Representation. *arXiv*. 2025.
    - https://arxiv.org/abs/2510.12515
11. El Ouahidi Y, Lys J, Thölke P, et al. REVE: A Foundation Model for EEG - Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025.
    - https://arxiv.org/abs/2510.21585
12. Ma J, Wu F, Xing Y, et al. Structured Prototype-Guided Adaptation for EEG Foundation Models. *arXiv*. 2026.
    - https://arxiv.org/abs/2602.17251
13. Liu D, Chen Y, Chen Z, et al. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
    - https://arxiv.org/abs/2601.17883
14. Lahiri JB, Runwal P, Kulkarni A, et al. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
    - https://arxiv.org/abs/2603.02268
