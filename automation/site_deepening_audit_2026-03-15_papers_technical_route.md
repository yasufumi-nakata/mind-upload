# Site Deepening Audit (2026-03-15, Paper Collection / Technical Reading Route)

## Scope

- Main target: `mind_uploading_papers.md`
- Secondary target: `wiki/literature-and-evidence-reading.md`

## Why This Page Was Selected

- `mind_uploading_papers.md` is useful as a broad archive, but as of 2026-03-15, it lacked a structure to reach primary evidence in technology and natural science in the shortest possible time.
- In fact, law, metaphysics, and VR works were listed at the top of the list in 2025, and experimental frontiers such as non-invasive language decoding, invasive speech neuroprosthesis, ESI direct validation, and maintenance-state were easily obscured.
- This is a weakness from a technical/natural science perspective. This is because if you misread the beginning of the chronological archive as "currently the strongest evidence," the evidence gate for the entire site will collapse.

## Main Critiques

### 1. The old page did not separate broad archive and evidence-ranked reading route

- Issue:
- `mind_uploading_papers.md` was organized by year, but `What should I read first to reach the technological frontier in the shortest time?` was not fixed.
- As a result, there remained a structure in which the non-experimental literature at the beginning of the latest year could be mistakenly interpreted as representative of the experimental frontier.
- Basis:
- Tang et al. (2023), Défossez et al. (2023), d'Ascoli et al. (2025) provide direct access as the primary literature on non-invasive language decoding.
- Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025) push the closed-loop/streaming front of invasive speech neuroprosthesis.
- Mikulan et al. (2020), Unnwongse et al. (2023), and Hao et al. (2025) are systems that audit ESI using direct validation.
- Xu et al. (2024), Looser et al. (2024), Lee et al. (2022) indicate maintenance-state outside the connectome.
- Revision:
- Added `Technology/Natural Science Priority Route` to `mind_uploading_papers.md`.
- While maintaining the chronological archive, we have clearly stated in the main text the site rule that technical readers cannot enter from the beginning of the chronological order.

### 2. The old page had too coarse units of information on "What to read first in technology"

- Issue:
- The previous version of the theme guide had a granularity of ``I want to see papers that are close to technology and measurement,'' and the distinction between decode, closed loop, ESI, and maintenance-state was weak.
- This makes it easy to confuse decode success with emulation claims, local communication subsystems with whole-brain routes, and structural scaffolds with hidden state.
- Basis:
- d'Ascoli et al. (2025) represents an advance in word decoding, but not subject-independent open-ended thought reading.
- Wairagkar et al. (2025) shows ultra-low latency voice synthesis but not whole-brain WBE.
- Hao et al. (2025) gives an error audit of ictal/interictal ESI in simultaneous HD-EEG/SEEG, but does not give a general unique recovery.
- Xu et al. (2024) and Looser et al. (2024) demonstrate sleep-dependent renormalization and myelin/metabolic coupling, reinforcing that connectome-complete cannot be read as emulation-complete.
- Revision:
- The `mind_uploading_papers.md` guide table has been reorganized into four routes: `non-invasive language decode`, `invasive speech neuroprosthesis`, `ESI with direct validation`, and `maintenance-state / hidden variable`.

### 3. The old wiki only explained that "a collection of papers is a broad archive" and did not specify the entry point for technical readers.

- Issue:
- `wiki/literature-and-evidence-reading.md` correctly explained the different roles of bibliographic pages, but did not specify where in the collection of papers they should enter for readers who only want to follow primary evidence in technology and natural sciences.
- Revision:
- Added information to `wiki/literature-and-evidence-reading.md` that technical readers should access from `Technology and Natural Sciences Preferred Route` in the collection of papers.

## Changes Made This Round

- `mind_uploading_papers.md`
- `last_updated` updated to 2026-03-15
- Specify `By year ≠ By strength of evidence` in front matter
- Added `Technology/Natural Science Priority Route`
- Replaced the theme-based information table with 4 routes: decode / neuroprosthesis / ESI / maintenance-state
- `wiki/literature-and-evidence-reading.md`
- `last_updated` updated to 2026-03-15
- Added reading notes for technical readers
- Added `Enter from the priority route` to the role explanation of the collection of papers

## Deferred External-Dependency Tasks

- Broad archive Lineage tagging for all cards
- Person in charge: AI / maintainer
- Prerequisite: Determine the operational criteria for reclassifying 100 existing cards to `tech-primary / review / philosophy-law / culture-media` etc.
- Completion condition: All yearly cards can be filtered by both evidence-track and source-type.

## References

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- D&eacute;fossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. *Nat Mach Intell*. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Sci Data*. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Elger CE, Pawley AD, Surges R, Avigdor T. Validating EEG source imaging using intracranial electrical stimulation in stereotyped seizure-onset patients. *Brain Commun*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, et al. Direct validation of HD-EEG source imaging with simultaneous stereoelectroencephalography in focal epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nat Commun*. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nat Neurosci*. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *Proc Natl Acad Sci U S A*. 2022.
  - https://doi.org/10.1073/pnas.2211572119
