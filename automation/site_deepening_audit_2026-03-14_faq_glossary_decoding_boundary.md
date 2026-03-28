# Site Deepening Audit (2026-03-14, FAQ / Glossary / Decoding Boundary)

## Scope

- Main target: `faq.md`
- Secondary target: `glossary.md`

## Why This Page Was Selected

- In the existing audit on 2026-03-14, `verification`, `tech_roadmap`, `wbe_101`, `perspective`, and various wikis were updated quite deeply.
- On the other hand, the entrance layer `faq.md` and the terminology layer `glossary.md` of the public site did not fully reflect the progress of non-invasive language decoding and ESI direct validation until 2025.
- If the entrance layer remains weak, the `decode` / `identifiability` / `direct validation` boundaries that were carefully separated on deep pages will mix again in the first few pages.

## Main Critiques

### 1. Q1 of `faq.md` was likely to cause cross-modal switching due to the proximity of fMRI-based semantic reconstruction and EEG.

- Issue:
- While the existing Q1 was correct in terms of direction in response to the question "Can EEG read 'thoughts'?", it did not sufficiently separate in the text which results were about scalp EEG and which were about fMRI and invasive systems.
- Therefore, there was still room to misinterpret Tang et al.'s (2023) non-invasive semantic reconstruction as the general goal of scalp EEG.
- d'Ascoli et al. in 2025 showed progress in word decoding from large-scale M/EEG, but there are clear conditions such as known word onset, reading/listening tasks, MEG dominance, and dependence on the amount of training data. If this is not fixed at the entrance, it will be read as ``any thought can be read freely.''
- Revision:
- Explicitly separated Q1 into `qualified decoding` and `identification of internal state`.
- Tang (2023) called it the fMRI system, and d'Ascoli (2025) called it the M/EEG constrained decoding system.

### 2. `faq.md` lacked an entry point to separate the apparent strength of brain-to-text from the strength of ground truth.

- Issue:
- The current FAQ didn't have a short checklist fixing "at least what you should look at in every demo."
- As a result, the high performance values ​​of invasive speech neuroprosthesis could be read as if they could be inherited directly from scalp EEG or general non-invasive BCI.
- Metzger et al. (2023) and Card et al. (2024) are certainly great advances, but both are invasive systems using cortical surface electrodes or intracortical arrays.
- Revision:
- Added `Measurement method / Issues / Prior / Verification / Reliability operation` 5-point check to newly created Q1b.
- Also added to Q5b that when reading closed-loop performance, invasiveness, recalibration time, and daily stability should be separated.

### 3. `glossary.md` did not yet have the most dangerous term pair as of 2026-03

- Issue:
- The existing glossary had up to `decode / emulate` and `correlation / causation`, but `observability / identifiability`, `model fit / direct validation`, and `brain signal / language prior` were missing.
- This is the most dangerous omission in site-wide. This is because the moment the decoder outputs a string, it is read as ``the internal state is known,'' and the moment source imaging outputs the source, it is read as ``We were able to sufficiently localize.''
- In the direct validation of Unnwongse et al. (2023), the mean localization error reached 10.3-26.0 mm, and in Hao et al. (2025), the error remained 14.07 ± 4.62 mm vs. 17.38 ± 4.16 mm, depending on source depth and spike power. This is sufficient evidence to show that `detectable` and `uniquely identified` are different.
- Revision:
- Added three term pairs to `words that are often confused`.
- Added `Observability / Identifiability / Direct Validation / Language Prior / Calibration / Abstention` to `Modeling` clause.

## Changes Made This Round

- `faq.md`
- Updated Q1 to quantitative ceiling description
- `No replacement of Q1` Added note
- Added 5-point brain-to-text comprehension check in new Q1b
- Added invasive closed-loop achievement and prohibition of conversion to non-invasive to Q5b
- Added d'Ascoli (2025), Unnwongse (2023), Hao (2025), Metzger (2023), Card (2024), Guo (2017), Geifman & El-Yaniv (2017) to references.
- `glossary.md`
- Added `observability / identifiability` and other pairs of terms that are easy to confuse.
- Added `direct validation`, `Language Prior`, `proofreading`, `abstention` to `modeling` clause.
- Fixed reading of non-invasive decoding in `2026-03 supplement` note.
- Added Seeber (2019), Unnwongse (2023), Hao (2025), Tang (2023), d'Ascoli (2025), Pernet (2020), Guo (2017), Geifman & El-Yaniv (2017) to references.

## Deferred External-Dependency Tasks

- Unified site-wide `language prior` display using public benchmarks
- Person in charge: AI / maintainer
- Prerequisite: prior display inventory of all brain-to-text / source imaging related pages
- Completion condition: The four elements of modality, issue, priority, and validation must be clearly stated in all decoder-related claims on the public page.

## References

- Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nat Commun. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Metzger SL, Littlejohn KT, Silva AB, et al. A high-performance neuroprosthesis for speech decoding and avatar control. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06443-4
- Card NS, Glasser MF, et al. An accurate and rapidly calibrating speech neuroprosthesis. N Engl J Med. 2024.
  - https://doi.org/10.1056/NEJMoa2314132
- Pernet CR, et al. Best practices in data analysis and sharing in neuroimaging using MEEG. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Guo C, Pleiss G, Sun Y, Weinberger KQ. On Calibration of Modern Neural Networks. ICML/PMLR. 2017.
  - https://proceedings.mlr.press/v70/guo17a.html
- Geifman Y, El-Yaniv R. Selective Classification for Deep Neural Networks. NeurIPS. 2017.
  - https://papers.neurips.cc/paper/7073-selective-classification-for-deep-neural-networks
