---
title: "2026-04-03 site deepening audit: datasets temporal-validity slow-milieu sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **practical-rule lag in the site's temporal-validity layer**.

By 2026-04-03, the site already treated `slow internal milieu` as a real scientific boundary in:

- `verification.md`
- `wiki/state-trait-and-drift.md`
- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- `tech_roadmap.md`

However, the main practical page for starter data and benchmark cards still left a softer rule in place:

- `datasets.md`

and the two L0 helper pages still inherited that softer practical wording:

- `wiki/eeg-to-l0-route.md`
- `wiki/l0-minimum-artifact-pack.md`

The result was that `state annotation` could still be read too loosely in the exact place where the site tells readers what a dataset card or L0 artifact must actually contain.

# Why This Needed Correction

## 1. Fast labels are not the whole state story

- [Musall et al. (2019)](https://doi.org/10.1038/s41593-019-0502-4) showed that task activity can be strongly shaped by uninstructed movement.
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) showed over a **10-hour EEG day** that movement-related decoding conditions vary enough to motivate adaptive decoders.

Those papers justify logging `movement`, `arousal`, and related fast labels, but they do **not** justify stopping there.

## 2. Slower internal milieu can move the operating regime without changing the visible task

- [de Quervain et al. (1998)](https://doi.org/10.1038/29542) showed glucocorticoid-dependent retrieval impairment.
- [Oei et al. (2007)](https://doi.org/10.1007/s11682-007-9003-2) showed hydrocortisone-linked decreases in human hippocampal and prefrontal retrieval activity.
- [Barone et al. (2023)](https://doi.org/10.1126/sciadv.adj1010) showed circadian control of hippocampal plasticity through synaptic BMAL1 phosphorylation.
- [Birnie et al. (2023)](https://doi.org/10.1073/pnas.2211996120) showed that corticosteroid treatment disrupts circadian regulation of hippocampal function.
- [Sherman et al. (2015)](https://doi.org/10.1016/j.neuropsychologia.2015.07.020) showed that hippocampal activity mediates the relationship between circadian-rhythm consistency and associative memory.

Therefore a result can keep the same task, subject, and nominal decoder while still running under a different biological operating regime.

## 3. Fast online success, fixed-decoder survival, and rescue burden are different evidence objects

- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) showed that long-term cursor iBCI use can be maintained with unsupervised recalibration, which is useful but still a distinct operating burden.
- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) showed an impressive low-latency speech route, but that does not convert same-day throughput into a generic temporal-validity benchmark.

Therefore the practical dataset page should not let `same-day online use`, `cross-session`, `cross-session adaptation`, and `longitudinal/chronic use` share an underspecified `state annotation` field.

# Root Critique

The central criticism is simple:

1. `state annotation` is too weak if it means only movement, arousal, or session ID.
2. `same task` is not `same operating regime`.
3. `cross-session` is not `fixed-decoder durability`.
4. `adaptive rescue` is not `training-free survival`.
5. `fast online output` is not `longitudinal deployability`.

Because `datasets.md` is the public page that tells readers what to log in practice, leaving this page softer than the rest of the site was a real scientific error. It reopened a shortcut that the theory and verification pages had already closed.

# Changes Executed In This Session

- [`/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md`](/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md)
  - updated front matter so the page summary layer now states that `state annotation` is split into `fast labels` and `slow internal-milieu disclosure`
  - rewrote the temporal-validity scientific rationale so movement-related, glucocorticoid, circadian, and recalibration evidence are all visible in one practical rule
  - added a new practical note that blocks `state annotation` from being treated as one free-text field
  - added a `same-day online / streaming use` row to the temporal-validity table
  - strengthened the `cross-session`, `cross-session adaptation`, and `longitudinal / chronic use` rows so slow internal-milieu disclosure is now explicit
  - updated the page-level site rule so dataset cards must split fast labels from slow internal-milieu disclosure
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-to-l0-route.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/eeg-to-l0-route.md)
  - synchronized the beginner route with the new temporal-validity rule
  - updated the `same-session score` warning and `Temporal-validity note` artifact description
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/l0-minimum-artifact-pack.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/l0-minimum-artifact-pack.md)
  - synchronized the L0 pack with the same fast-label / slow-milieu split
  - added a short addendum explaining why item 9 cannot remain a vague temporal note
  - updated the item-9 description and the condensed checklist language
- [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_datasets_temporal_validity_slow_milieu_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-03_datasets_temporal_validity_slow_milieu_sync.md)
  - added this audit record to preserve the criticism, rationale, and source trail

# Verification

- `git diff --check`
- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "slow internal-milieu|fast labels|same-day online / streaming use|Temporal-Validity addendum" datasets.md wiki/eeg-to-l0-route.md wiki/l0-minimum-artifact-pack.md github-wiki-export/eeg-to-l0-route.md github-wiki-export/l0-minimum-artifact-pack.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature reread, public-page edits, wiki export synchronization, local build validation, and Git publication.

# References

1. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019. https://doi.org/10.1038/s41593-019-0502-4
2. Egger F, Vuckovic A, Min B-K, et al. Adaptive decoders for movement-related EEG in extended day-night recording. *Scientific Reports*. 2024. https://doi.org/10.1038/s41598-024-70609-x
3. de Quervain DJF, Roozendaal B, McGaugh JL. Stress and glucocorticoids impair retrieval of long-term spatial memory. *Nature*. 1998. https://doi.org/10.1038/29542
4. Oei NYL, Elzinga BM, Wolf OT, et al. Glucocorticoids decrease hippocampal and prefrontal activation during declarative memory retrieval in young men. *Brain Imaging and Behavior*. 2007. https://doi.org/10.1007/s11682-007-9003-2
5. Barone I, Gillette NM, Hawks-Mayer H, et al. Synaptic BMAL1 phosphorylation controls circadian hippocampal plasticity. *Science Advances*. 2023. https://doi.org/10.1126/sciadv.adj1010
6. Birnie MT, Begum G, Sugden D, et al. Circadian regulation of hippocampal function is disrupted with corticosteroid treatment. *Proceedings of the National Academy of Sciences of the United States of America*. 2023. https://doi.org/10.1073/pnas.2211996120
7. Sherman SM, Mumford JA, Schnyer DM. Hippocampal activity mediates the relationship between circadian activity rhythms and memory in older adults. *Neuropsychologia*. 2015. https://doi.org/10.1016/j.neuropsychologia.2015.07.020
8. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025. https://doi.org/10.1038/s41551-025-01536-z
9. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025. https://doi.org/10.1038/s41586-025-09127-3
