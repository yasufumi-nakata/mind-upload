# Site Deepening Audit (2026-03-14, Language Prior / Brain-to-Text)

## Scope

- Main target: `perspective.md`

## Why This Page Was Selected

- `perspective.md` is the longest page on the site and is often referred to as a position statement.
- On the other hand, the previous version's placed `LLM Research Update` section brain-to-text primary literature and general-purpose LLM operational theory at the same level.
- This is a weakness from a technical/natural science perspective. This is because the main constraint on brain decoding lies not in the presence or absence of RLHF or RAG, but in `isolation of neural contribution`, `task dependence`, `tail latency of streaming operation`, `drift / recalibration`, `subject cooperation`.

## Main Critiques

### 1. The previous version confused "evidence of brain decoding" with "useful functions of general-purpose LLM"

- Issue:
- The previous version listed RLHF, DPO, QLoRA, RAG, ReAct, Toolformer, and SelfCheckGPT, but these are not the main primary evidence for brain-to-text.
- Therefore, there was room for readers to misread the paper by thinking, ``If you add LLM peripheral technology, you can overcome the barrier of brain decoding.''
- Basis:
- Tang et al. (2023) demonstrated non-invasive semantic reconstruction, but required participants' cooperation in both learning and applying the decoder.
- Défossez et al. (2023) demonstrated the identification of 3-second speech intervals from non-invasive brain recordings, but the setting is closer to retrieval/identification rather than open-ended generation.
- d'Ascoli et al. (2025) demonstrated word decoding in 723 participants, but modality, task, and amount of data greatly influenced performance.
- Therefore, the central question is not ``how to use LM conveniently'', but ``to what extent does neural data exceed language prior''?
- Revision:
- The relevant section of `perspective.md` has been completely revised from the generic LLM theory to the primary literature review of `brain-to-text / speech neuroprosthesis / neural encoding`.
- As a site rule, it has been clearly stated in the text that ``general-purpose LLM papers should not be used as main evidence.''

### 2. Non-invasive decoding, invasive speech BCI, and encoding by LLM embedding were not separated.

- Issue:
- In the previous edition, research on ``generating sentences from brain activity'' was treated as one, and differences in modality and strength of evidence were not visible.
- In particular, it was dangerous that the encoding model and decoder could be read with the same weight.
- Basis:
- Horikawa et al. (2025) and Tang et al. (2023) are advances in semantic/caption reconstruction using non-invasive measurements.
- Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025) are streaming/low-latency demonstrations of invasive speech neuroprosthesis.
- Zada ​​et al. (2024) and Goldstein et al. (2025) provide encoding evidence that LLM embeddings and semantic relationship representations predict brain activity well, but they are not decoder truth.
- Revision:
- Added `Dividing the evidence hierarchy into four parts` table to `perspective.md`.
- Separated `non-invasive semantic / caption decoding`, `non-invasive word / speech decoding`, `invasive streaming speech neuroprosthesis`, `neural encoding with LLM embedding`.
- "What can be said now" and "What can't be said yet" have been fixed for each track.

### 3. Evaluation pack to audit language prior contamination was missing

- Issue:
- The old version only described `LLM-derived noise` conceptually, and was not clear on what should be listed as the baseline.
- This will overestimate high apparent performance in tasks with a small candidate set or in conditions where a strong language prior is effective.
- Basis:
- Tang et al. (2023) required participant cooperation and showed that the data acquisition conditions themselves are directly linked to performance.
- d'Ascoli et al. (2025) showed that decoding performance varies greatly depending on modality, task, and amount of data.
- Littlejohn et al. (2025) and Wairagkar et al. (2025) showed that latency and silence/abstention are core metrics in streaming communication.
- Revision:
- Added `no brain`, `time-shuffle`, `trial-shuffle`, `LM-only`, `no-LM`, candidate set size, held-out / OOD, cross-day, latency, abstention, recalibration burden to the text as `minimum evaluation pack`.
- Phase 1 of the research program table was also rewritten from a generic "causal consistency check" to an evaluation pack with specific audit items.

### 4. Successful decoding left a structure that could be read directly to WBE/emulate

- Issue:
- The previous edition also mentioned the difference between decode and emulate, but the brain-to-text section itself still had a structure that could be read optimistically.
- Basis:
- The best example of invasive speech BCI is the closed-loop improvement of the communication subsystem.
- The success of neural encoding using LLM embedding indicates that the brain is partially reflected in the representation space of the language model, but it does not indicate that it has reproduced the causal dynamics of the brain.
- Revision:
- Added `Operation rules on Mind-Upload side` and fixed L1 / L2 / L3 assertion conditions.
- Clarified `decode success, embedding resemblance, and naturalness of conversation should not be interpreted as emulate/WBE/preservation of identity`.

## Changes Made This Round

- `perspective.md`
- Completely revised `LLM Research Update` section to `Brain-to-Text Update: Language Priors, Streaming, Evidence Gate`
- `Divide the evidence hierarchy into four parts` New table added
- Added `Minimum required evaluation pack` and `Operation rules on Mind-Upload side`
- Revised Phase 1 of the research program table to focus on brain-to-text evaluation packs.
- Added primary papers from 2023-2025 to references

## Deferred External-Dependency Tasks

- Brain-to-text L3 benchmark implementation
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisites: Publishable streaming BCI logs, evaluation data including latency/abstention/recalibration
- Completion condition: `No brain / No LM / shuffle / OOD / drift / latency` can be reproduced on the same bench.

## References

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- Horikawa T, et al. Mind captioning: Evolving descriptive text of mental content from human brain activity. Sci Adv. 2025.
  - https://doi.org/10.1126/sciadv.adw1464
- Défossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. Nat Mach Intell. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Zada Z, Goldstein A, et al. Contextual embeddings from deep language models predict fMRI responses to naturalistic language. Neuron. 2024.
  - https://doi.org/10.1016/j.neuron.2024.09.018
- Goldstein A, Bar A, et al. Connecting concepts in the brain by mapping cortical representations of semantic relations. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01903-8
