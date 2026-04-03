---
title: "2026-04-04 site deepening audit: summary booklet EEG foundation-model stop-line sync"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **front-door compression bug in the auto-generated summary artifact**.

The scientific correction on EEG foundation-model reading already existed in deeper public pages:

- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-foundation-models.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-foundation-models.md)

However, the derived briefing layer in [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md) still surfaced that rule mostly as one long generic clause inside the FAQ card:

- `a foundation-model or leaderboard result is not automatically a general neural decoder`

That wording was directionally correct.

But it was no longer strong enough for the current technical literature, because the key scientific split had become **which object a paper directly advances**:

- `representation learning / efficiency`
- `recording-frame compatibility`
- `label-limited adaptation rescue`
- `benchmark governance / postmortem`

Without that split, the booklet still allowed a fast reader to carry away a weaker mental model than the site's actual public standard.

# Why This Needed Correction

## 1. Current EEG foundation-model papers do not support one monotonic capability ladder

- [Lee et al. (2025)](https://proceedings.mlr.press/v267/lee25a.html) constrain a `representation learning / efficiency` lane and reported only marginal gains over conventional deep baselines under their fine-tuning study.
- [Han et al. (2025)](https://arxiv.org/abs/2507.14141), [Chen et al. (2025)](https://arxiv.org/abs/2510.12515), and [El Ouahidi et al. (2025)](https://arxiv.org/abs/2510.21585) constrain a `recording-frame compatibility` lane.
- [Ma et al. (2026)](https://arxiv.org/abs/2602.17251) constrain a `label-limited adaptation rescue` lane.
- [Lahiri et al. (2026)](https://arxiv.org/abs/2603.02268) explicitly show that narrow-source pretraining can win `linear probes` while more diverse pretraining can win under `fine-tuning`, and they report ranking reversals of up to `24 pp` under benchmark inconsistencies.
- [Liu et al. (2026)](https://arxiv.org/abs/2601.17883) explicitly frame EEG foundation-model benchmarking as an unresolved comparison problem rather than a settled leaderboard ladder.

Critique:

- these papers do not all strengthen the same object
- some strengthen representation efficiency
- some strengthen heterogeneous setup support
- some strengthen adaptation under label scarcity
- some mainly strengthen benchmark criticism

Therefore one short phrase such as `foundation-model progress` is scientifically too coarse at the briefing layer.

## 2. Official benchmark governance is part of the claim, not an appendix

The official EEG Challenge pages also support the stricter split:

- the [homepage](https://eeg2025.github.io/) states that the original proposal preprint became outdated during execution and that the website should be treated as current
- the [rules](https://eeg2025.github.io/rules/) fix downsampling, disclosure obligations, and the inference-stage compute rule
- the [submission page](https://eeg2025.github.io/submission/) fixes that this is an inference-only code-submission competition
- the [leaderboard](https://eeg2025.github.io/leaderboard/) reports a Challenge 2 randomization problem and separates awards accordingly

Critique:

- this is not administrative noise
- it changes benchmark object, operating budget, and leakage risk
- therefore `leaderboard rank` is not a route-free capability statement

## 3. The summary booklet had become weaker than the public pages it summarizes

This mattered because the booklet is not an internal scratch file.

It is a public-facing entry layer generated from page front matter and lead summaries.

If that layer keeps only the generic sentence

- `not automatically a general neural decoder`

while hiding the route-family split that already exists in the FAQ body and wiki, then the booklet silently reopens the exact overread the site was built to stop.

# Root Critique

The criticism is precise:

1. The site's deeper public pages already moved to a route-split reading of EEG foundation-model evidence.
2. The auto-generated booklet still surfaced a weaker, compressed version of that rule.
3. Current primary sources and official benchmark pages do not support that compression.
4. Therefore the booklet and its generator needed to preserve the four-way split explicitly.

# Changes Executed In This Session

## Public-facing source content

- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - added a new front-matter highlight that names the four-way split directly
  - added a new known-point line stating the regime-dependent trade-off between narrow-source linear-probe wins and diverse-pretraining fine-tuning wins

## Generation logic

- [`/Users/yasufumi/Documents/GitHub/mind-upload/scripts/build_summary_booklet.rb`](/Users/yasufumi/Documents/GitHub/mind-upload/scripts/build_summary_booklet.rb)
  - taught the booklet selector to score `foundation-model / leaderboard / benchmark governance / recording-frame / adaptation` stop lines explicitly
  - rejected the overcompressed `eleven technical guardrails` mega-bullet from booklet selection so concise scientific stop lines can surface instead
  - added an FAQ-specific priority so the booklet cannot bury the EEG foundation-model split behind unrelated bridge or proxy bullets
  - added a compact replacement for the generic foundation-model stop line when the booklet needs a short form

## Regenerated output

- [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md)
  - regenerated so the FAQ card now surfaces the EEG foundation-model split instead of only the long generic guardrail clause
  - regenerated so the `Datasets` and `EEG 101` cards also surface foundation-model disclosure obligations more clearly

# Verification

- Ran `ruby scripts/build_summary_booklet.rb`.
- Re-read [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md) to confirm the FAQ card now exposes the specific EEG foundation-model stop line.
- Planned local site verification after regeneration with `git diff --check` and `bundle exec jekyll build`.

# External Dependency Tasks

- None.
  - This session stayed inside repository work: source verification, summary-layer correction, build-script adjustment, generated-output refresh, validation, and Git operations.

# References

1. Lee N, Barmpas K, Panagakis Y, et al. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *Proceedings of the 42nd International Conference on Machine Learning*. 2025. https://proceedings.mlr.press/v267/lee25a.html
2. Han DD, Lee AL, Lee T, et al. DIVER-0: A Fully Channel Equivariant EEG Foundation Model. *arXiv*. 2025. https://arxiv.org/abs/2507.14141
3. Chen Z, Qin C, You W, et al. HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Representation. *arXiv*. 2025. https://arxiv.org/abs/2510.12515
4. El Ouahidi Y, Lys J, Thölke P, et al. REVE: A Foundation Model for EEG: Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025. https://arxiv.org/abs/2510.21585
5. Ma J, Wu F, Xing Y, et al. Structured Prototype-Guided Adaptation for EEG Foundation Models. *arXiv*. 2026. https://arxiv.org/abs/2602.17251
6. Lahiri JB, Runwal P, Kulkarni A, et al. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026. https://arxiv.org/abs/2603.02268
7. Liu D, Chen Y, Chen Z, et al. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026. https://arxiv.org/abs/2601.17883
8. EEG Challenge (2025). Official homepage. https://eeg2025.github.io/
9. EEG Challenge (2025). Rules. https://eeg2025.github.io/rules/
10. EEG Challenge (2025). Submission. https://eeg2025.github.io/submission/
11. EEG Challenge (2025). Leaderboard. https://eeg2025.github.io/leaderboard/
