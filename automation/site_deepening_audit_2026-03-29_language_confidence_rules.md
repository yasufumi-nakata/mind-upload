# Site Deepening Audit (2026-03-29, Language Confidence Rules)

## Scope

- Main public targets:
  - `faq.md`
  - `wiki/uncertainty-confidence-and-abstention.md`
  - `github-wiki-export/uncertainty-confidence-and-abstention.md`

## Why This Topic Was Selected

- The site had already separated language prior, shortcut auditing, and communication-subsystem evidence in several places.
- However, the public uncertainty page still explicitly said that task-specific pass/fail rules for candidate-conditioned language confidence were not finalized.
- That gap mattered because several 2023-2025 papers now produce fluent language-like outputs under very different scaffolds:
  - subject-cooperative semantic reconstruction
  - fixed-bank segment retrieval
  - known-onset word decoding
  - prompt-conditioned generation
  - viewed/recalled content captioning
  - invasive streaming speech synthesis

## Main Critiques

### 1. The site still had a structural gap between route split and pass/fail rules

- Issue:
  - The route split existed across `faq.md`, `verification.md`, `perspective.md`, and `wiki/decode-vs-emulate.md`.
  - But the uncertainty page still left readers without a reusable rule for when a language-facing score could pass as valid within its own scaffold.
- Why this matters:
  - Without a structural pass rule, readers can still compare unlike uncertainty objects as if they were one probability scale.
  - That is exactly how fixed-bank retrieval, known-onset word decoding, prompt-conditioned generation, and streaming speech BCIs get over-read.
- Executed change:
  - Added a route-by-route structural pass/fail bundle to the uncertainty page and its GitHub wiki export.

### 2. Cue-supported semantic BCIs can be over-read as self-generated communication

- Issue:
  - Many readers still jump from “semantic categories were decoded” to “free semantic communication is close.”
- Primary-literature basis:
  - Rybár et al. (2024) showed that EEG semantic-category decoding could look strong during cue presentation but fail during the later cue-separated mental-task period.
  - Therefore, cue-period performance and self-generated semantic operation are not the same evidence class.
- Executed change:
  - Added cue-regime disclosure to the public FAQ checklist.
  - Added cue-policy disclosure and cue-separated comparison to the language-confidence pass/fail bundle.

### 3. Language-like output was still too easy to compare on one axis

- Issue:
  - A fluent sentence can now come from very different neural-to-text pathways, but the front door still risked making them sound like one `brain-to-text` ladder.
- Primary-literature basis:
  - Tang et al. (2023) remained subject-cooperative semantic reconstruction from fMRI.
  - d'Ascoli et al. (2025) remained known-onset top-10 retrieval over a fixed 250-word vocabulary.
  - Ye et al. (2025) remained prompt-conditioned generation with explicit prompt/LLM scaffold.
  - Horikawa (2025) added viewed/recalled content captioning from decoded semantic features and iterative text optimization, which is a distinct route again.
- Executed change:
  - Added `output family` as a first-pass FAQ audit item.
  - Added a captioning-specific row to the uncertainty-page pass/fail bundle.

### 4. Streaming speech neuroprosthesis still needs confidence and durability rules, not only speed

- Issue:
  - A fast or natural-sounding output can still be over-read as stable general communication.
- Primary-literature basis:
  - Littlejohn et al. (2025) achieved streaming neural decoding in 80-ms increments.
  - Wairagkar et al. (2025) achieved sub-10-ms voice synthesis with silence fallback, but fixed-decoder performance still declined over time.
  - Wilson et al. (2025) showed that long-term unsupervised recalibration is a separate operational axis.
- Executed change:
  - Added latency-quantile, silence/abstention, fixed-decoder interval, recalibration-burden, and durability-slice disclosure to the route-specific pass bundle.

## Changes Executed In This Session

- `faq.md`
  - Added a new critique paragraph to Q1 explaining cue-period overestimation and the separate captioning route.
  - Expanded the `minimum you should check` list from 9 to 11 items by adding `cue regime` and `output family`.
  - Added a route-splitting paragraph so readers do not compare cue-supported semantic decode, captioning, prompt-conditioned generation, and speech BCIs on one axis.
  - Added FAQ references for Rybár et al. (2024) and Horikawa (2025).
- `wiki/uncertainty-confidence-and-abstention.md`
  - Updated page metadata and known/unknown statements.
  - Upgraded the language-decoding row in the task-specific reporting table to include cue regime and output family.
  - Added a new structural pass/fail bundle for fixed-bank retrieval, known-onset word decoding, prompt-conditioned generation, viewed/recalled content captioning, and streaming speech neuroprosthesis.
  - Added references for Rybár et al. (2024), Horikawa (2025), and Littlejohn et al. (2025).
- `github-wiki-export/uncertainty-confidence-and-abstention.md`
  - Synced the same substantive changes for the GitHub Wiki mirror.

## Verification

- Executed:
  - `bundle exec jekyll build` -> passed
  - `git diff --stat` -> confirmed the intended public files and wiki-export mirror changed together

## External Dependency Tasks

- Numeric thresholds for route-specific coverage / abstention remain an external benchmarking task.
- Owner:
  - AI / maintainer / future benchmark author
- Prerequisites:
  - Public benchmark logs with fixed candidate scaffold, calibration split, abstention policy, and temporal-shift slices
- Completion condition:
  - A public threshold table that fixes route-specific numeric pass/fail values without mixing different uncertainty objects

## References

- Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Ye X, Liu X, Wang Y, et al. Generative language reconstruction from brain recordings. Commun Biol. 2025.
  - https://doi.org/10.1038/s42003-025-07731-7
- Rybár M, Poli R, Daly I. Using data from cue presentations results in grossly overestimating semantic BCI performance. Sci Rep. 2024.
  - https://doi.org/10.1038/s41598-024-79309-y
- Horikawa T. Mind captioning: Evolving descriptive text of mental content from human brain activity. Sci Adv. 2025.
  - https://doi.org/10.1126/sciadv.adw1464
- Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
