# Site Deepening Audit (2026-03-15, EEG Generalization Ladder / Recalibration Burden)

## Scope

- Main target: `datasets.md`
- Secondary target: `eeg_101.md`

## Why This Page Was Selected

- As of 2026-03-15, the public site was quite organized with annotation provenance, split unit, QC, and observability ceiling.
- On the other hand, at the entrance to the public page, there was still a weak guideline to distinguish `high score` from `under what generalization conditions did the score come out`, and there was still room for `within-session success` to appear as `cross-day robustness` or `deployable loop`.
- This weakness is significant from a technical/natural science perspective. This is because the real barrier to EEG/BCI is not just simple classification ability, but also the separate effects of state fluctuation, session drift, subject variability, and recalibration burden.

## Main Critiques

### 1. The old `datasets.md` explained split unit, but failed to bring evaluation family to the forefront as a reading rule.

- Issue:
- The previous version had the word `within-session / cross-session / cross-subject`.
- However, the fact that each is `a different scientific question` and cannot be placed side by side with the same accuracy was not fixed as the main clause of the text.
- Basis:
- MOABB's official docs implements `WithinSessionEvaluation`, `CrossSessionEvaluation`, and `CrossSubjectEvaluation` as separate classes.
- `WithinSessionEvaluation` is k-fold within the same session.
- `CrossSessionEvaluation` is an evaluation across different sessions of the same subject.
- `CrossSubjectEvaluation` is an assessment that holds-out one subject and learns from the remaining subjects.
- Revision:
- Added `2.5) Even if the score is the same, the meaning changes if the generalization steps are different` to `datasets.md`.
- Created a new table with 4 columns of `evaluation family / hold-out unit / what to say / stop misreading` to prevent misreading of score alone.

### 2. The old site did not show the same-day score and cross-day degradation distance using numbers from the primary literature.

- Issue:
- In the previous version, there was a direction of `cross-session is difficult`, but the extent of the drop was not quantified on the entrance page.
- Basis:
- Ma et al. (2022) showed that the average subject-specific accuracy drops from `within-session 68.8%` to `cross-session 53.7%` in a 5-day, 25-subject motor imagery dataset.
- The same paper also shows that cross-session adaptation using a small amount of target-session data can recover up to `78.9%`.
- What we can say directly from this is that `same-day separation`, `separate-day tolerance`, and `operation with recalibration` are different evaluations.
- Revision:
- Added the above values ​​to `datasets.md` and `eeg_101.md`, and clarified the site rule to read `hold-out condition` and `adaptation presence` at the same time when viewing `high score`.

### 3. The old `eeg_101.md` handled artifacts and inverse problems carefully, but only weakly handled state confound and long-term nonstationarity at the entrance.

- Issue:
- The previous version dealt with source imaging ceiling and preprocessing gate quite strictly.
- However, the possibility that the same-day score picks up the state and movement of that day, or the possibility that it collapses on a different day, was not brought to the fore as an independent clause.
- Basis:
- Musall et al. (2019) showed that cortex-wide activity can be strongly controlled by uninstructed movements.
- Wilson et al. (2025) showed that intracortical BCI requires frequent recalibration due to accumulated neural nonstationarity.
- Even though the modalities are different, `same-day decoding success` and `long-term operational stability` are different issues, which is an important lesson for EEG readers.
- Revision:
- Added `Even if the decoding score is the same, the range that can be read is different` clause to `eeg_101.md`.
- Fixed `within-session / cross-session / cross-subject / longitudinal closed-loop` in a 4-row table, with `What we are mainly looking at here` and `What we cannot say yet` clearly marked in each row.

### 4. The old publication page indicated recalibration as an "improvement", but it was not fixed enough as a "part of performance"

- Issue:
- In the previous version, drift and recalibration burden were discussed in the wiki and FAQ, but they remained in a supporting role on the EEG entry page and the datasets entry page.
- Basis:
- Wilson et al. (2025) showed that the need for frequent recalibration is itself an operational barrier.
- So while `returning with adaptation` is good news, `it was stable from the beginning` does not mean.
- Revision:
- `datasets.md` added `cross-session adaptation` as an independent line and promoted `target session` to the lowest reporting item.
- For `eeg_101.md`, `How many days did you hold the fixed decoder` and `recalibration burden` have been added to the confirmation items.

## Changes Made This Round

- `datasets.md`
- Updated front matter highlights / known points / wiki links
- Added note for `Even if the score is the same, the meaning will change if the generalization conditions are different`
- Added `2.5) The same score has different meanings if the generalization steps are different` section
- Added MOABB docs, Ma et al. (2022), Musall et al. (2019), Wilson et al. (2025) to references
- `eeg_101.md`
- Updated front matter highlights / known / unknown / wiki links
- Added note for `When you see a high score, you want to see what you hold-out first`
- Added `Even if the decoding score is the same, the range that can be read is different` section
- Add `Since the accuracy was high, it is enough to use another day or another person` to `Common misconception`
- Added MOABB docs, Ma et al. (2022), Musall et al. (2019), Wilson et al. (2025) to references

## Deferred External-Dependency Tasks

- Unification of site-wide score card schema
- Person in charge: AI / maintainer
- Prerequisite: `evaluation family`, `hold-out unit`, `adaptation budget`, `recalibration burden` must be common attributes in datasets / verification / papers / FAQ
- Completion condition: At least the above four attributes must be included on all pages where the score is published.

## References

- Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. *Journal of Neural Engineering*. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- MOABB Docs: WithinSessionEvaluation
  - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.WithinSessionEvaluation.html
- MOABB Docs: CrossSessionEvaluation
  - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSessionEvaluation.html
- MOABB Docs: CrossSubjectEvaluation
  - https://moabb.neurotechx.com/docs/generated/moabb.evaluations.CrossSubjectEvaluation.html
- Ma J, Yang B, Qiu W, et al. A large EEG dataset for studying cross-session variability in motor imagery brain-computer interface. *Scientific Data*. 2022.
  - https://doi.org/10.1038/s41597-022-01647-1
- Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
  - https://doi.org/10.1038/s41593-019-0502-4
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
