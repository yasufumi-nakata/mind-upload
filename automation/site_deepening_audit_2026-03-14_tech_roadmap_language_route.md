# Site Deepening Audit (2026-03-14, Tech Roadmap / Brain-to-Text Evidence Gate)

## Scope

- Main target: `tech_roadmap.md`

## Why This Page Was Selected

- `tech_roadmap.md` is the main conductor of the public site, and if the comparison axis here is lax, the rigor established by `Perspective` and `Verification` will be weakened at the entrance.
- `V8` as of 2026-03-14 has a high level of abstraction, and while it states `LLM/imitation distinction`, what should actually be arranged as baseline was not sufficiently fixed.
- In addition, `Previous research map` and `References E` were still in the old bundling style, including generic LLM papers, and had not kept up with the primary literature-based reading style of brain-to-text/speech BCI.

## Main Critiques

### 1. `V8` only abstractly stated the "distinction from imitation" and did not separate the layers of evidence shown by the primary literature

- Issue:
- The previous version wrote that "intervention response, closed loop, and internal state alignment are required," but it did not seem that non-invasive semantic decoding, non-invasive word/speech decoding, and invasive streaming speech BCI were separate achievements.
- Therefore, there was still room for readers to read the progress of `brain-to-text` as the progress of `WBE` or `emulation`.
- Basis:
- Tang et al. (2023) demonstrated semantic reconstruction of continuous language using non-invasive fMRI, and showed that subject cooperation is necessary both during learning and application.
- Défossez et al. (2023) showed decoding of speech perception from MEG/EEG, but in a passive listening task with healthy volunteers, not speech production or open-ended generation.
- d'Ascoli et al. (2025) showed that MEG and reading tasks are more advantageous than EEG and listening, and that the amount of data greatly affects decoding performance.
- Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025) have pushed the performance limits of speech neuroprosthesis, but are local advances in the communication subsystem.
- Revision:
- Redesigned `V8` as an evidence gate and separated `non-invasive semantic / caption decoding`, `non-invasive word / speech decoding`, and `invasive streaming speech neuroprosthesis` in a table.
- Fixed "What can be said now" and "What can't be said yet" for each track.

### 2. Roadmap was missing an evaluation pack to audit language prior contamination

- Issue:
- The previous version did not clearly specify audit items such as `LM-only`, `no-LM`, `time-shuffle`, `trial-shuffle`, candidate set size, cross-day, latency, abstention, and recalibration burden.
- As a result, the site rule that separates the language prior contribution from the neural contribution only existed on the long note side.
- Basis:
- Tang et al. (2023) clarified the subject cooperation requirement and showed that decoding success strongly depends on measurement conditions.
- d'Ascoli et al. (2025) showed that device, task, and training data amount strongly influence decoding performance.
- Littlejohn et al. (2025) demonstrated streaming synthesis with 80 ms increments, and Wairagkar et al. (2025) demonstrated instantaneous closed-loop audio feedback. Here, not only accuracy but also latency / silence / abstention are the central metrics.
- Wilson et al. (2025) treated long-term unsupervised recalibration as a separate issue and showed that the fixed-decoder argument that ignores drift is dangerous.
- Revision:
- Added `minimum evaluation pack` to `V8` and clarified neural contribution, generalization boundary, streaming metrics, and claim downgrade rule.

### 3. `Previous research map` and `References E` remained weak literature bundles compared to the current rigor of the public site

- Issue:
- Previous editions placed generic LLM reliability papers such as `Ji et al. (2023)` and `Manakul et al. (2023)` on the same level as major previous research in brain decoding.
- On the other hand, primary literature that directly supports this technical issue was missing, such as Défossez et al. (2023), d'Ascoli et al. (2025), Littlejohn et al. (2025), Wairagkar et al. (2025), and Wilson et al. (2025).
- Also, the DOI of d'Ascoli et al.'s 2025 paper was recorded as `10.1038/s41467-025-56165-8` in a separate audit memo on the public site, but the official article in Nature Communications was `10.1038/s41467-025-65499-0`.
- Revision:
- Updated the decoding line for `Previous research map` to the primary literature set for `Huth / Tang / Défossez / Horikawa / d'Ascoli / Willett / Littlejohn / Wairagkar / Wilson`.
- Completely replaced `Reference E` with brain-to-text / speech BCI primary papers and DOI instead of generic LLM papers.
- The DOI of d'Ascoli et al. has been unified as `10.1038/s41467-025-65499-0`.

## Changes Made This Round

- `tech_roadmap.md`
- Rewritten `V8` from abstract imitation theory to brain-to-text evidence gate.
- Added `Minimum desired evaluation pack`
- Updated the decoding line of `Previous research map` to the primary literature base.
- Full update of `References E` to primary papers + DOI

## Deferred External-Dependency Tasks

- Develop a public benchmark that allows you to compare `LM-only / shuffle / OOD / cross-day / latency / abstention / recalibration` with the same schema.
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisite: Publishable brain-to-text / speech BCI logs or equivalent reproduction bench
- Completion condition: Communication route progress and WBE claims can be separated using the same evaluation table.

## References

- Huth AG, de Heer WA, Griffiths TL, Theunissen FE, Gallant JL. Natural speech reveals the semantic maps that tile human cerebral cortex. Nature. 2016.
  - https://doi.org/10.1038/nature17637
- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- D&eacute;fossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. Nat Mach Intell. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- Horikawa T. Mind captioning: Evolving descriptive text of mental content from human brain activity. Sci Adv. 2025.
  - https://doi.org/10.1126/sciadv.adw1464
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain&ndash;computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
