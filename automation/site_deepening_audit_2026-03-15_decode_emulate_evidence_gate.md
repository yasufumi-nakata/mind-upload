# Site Deepening Audit (2026-03-15, Decode / Emulate Evidence Gate)

## Scope

- Main target: `wiki/decode-vs-emulate.md`
- Secondary target: `faq.md`

## Why This Page Was Selected

- `Wiki: Decode and Emulate` is the core boundary page of the site, but as of 2026-03-15, it was stuck with examples centered on 2023, and `open-vocabulary non-invasive decode`, `streaming / voice-synthesis neuroprosthesis`, `long-term recalibration burden`, and `connectome-constrained prediction`, which were pushed up by primary literature in 2025, had not been included in the site rules.
- This is a high priority improvement from a technical/natural science perspective. This is because the current strongest evidence is divided into "how far decoding has progressed," "how far the local subsystem's closed loop has progressed," and "how far the predictive gain can be achieved with the connectome constraint." If you read them all together as `close to emulation`, the evidence gate will collapse.

## Main Critiques

### 1. The old page did not incorporate the 2025 decode frontier, and the non-invasive decode ceiling could only be stopped at the old granularity.

- Issue:
- The previous edition mainly explained non-invasive decoding based on Tang (2023), but did not explicitly mention `open-vocabulary progress and boundary` based on d'Ascoli et al.'s (2025) 723-person single-word decoding.
-Therefore, there remained a structure that made it easy for readers to read `word decoding advanced` as `free thinking general reading` or `internal state reconstruction`.
- Basis:
- Tang et al. (2023) is a major step forward in semantic reconstruction, but it is a participant-specific system that requires participant cooperation.
- d'Ascoli et al. (2025) showed progress in open-vocabulary non-invasive word decoding, but also showed that performance varies greatly depending on modality, task, and amount of data.
- Revision:
- Added d'Ascoli (2025) to `wiki/decode-vs-emulate.md` and promoted `language prior / candidate set / participant cooperation` to mandatory audit item in decode/emulate boundary.
- Added `LM-only / no-brain / shuffle baseline` to the `brain-to-text` section of `faq.md` to the minimum confirmation items.

### 2. The old page only dealt with streaming speech neuroprosthesis as `high-performance decode` and did not sufficiently isolate the deployment burden.

- Issue:
- The `decode vs emulate` bound in the previous version mainly looked at offline accuracy and local closed loops.
- However, the strongest evidence in 2025 indicates that not only `how fast` but also `tail latency`, `silence / abstention`, `recalibration burden`, and `cross-day deployment` should be logged separately.
- Basis:
- Littlejohn et al. (2025) showed streaming brain-to-voice every 80 ms.
- Wairagkar et al. (2025) demonstrated neural-to-voice synthesis and silence fallback of less than 10 ms.
- Wilson et al. (2025) dealt with long-term unsupervised recalibration and clarified that daily supervised recalibration itself is a barrier to actual operation.
- Revision:
- Updated evidence ladder for `wiki/decode-vs-emulate.md` to clarify speech neuroprosthesis as `communication subsystem L2~L3`.
- Added `Stable in closed loop and long term operation` to `5 gates`, and added `P50/P95/P99 latency`, `silence / abstention`, `recalibration burden`, `recovery time` to required logs.
- `faq.md` has also been revised to read within-session speed and deployable closed loop separately.

### 3. The old page only stated the connectome-constrained model as `emulate near-base` and did not specify the wall of degeneration at the 2025 level.

- Issue:
- The previous version used MICrONS and Billeh to indicate the `close to digital twin` direction, but the primary literature in 2025 did not specify why it was not the only solution even with the connectome constraint.
- Basis:
- MICrONS Consortium et al. (2025) provided valuable scaffolding for same-brain function + connectomics.
- Beiran & Litwin-Kumar (2025) showed that even with connectome-constrained recurrent networks, the recovery of teacher dynamics is not unique if unrecorded neurons and unmeasured biophysical parameters remain.
- Prinz et al. (2004) classically shows that similar network activities arise from different circuit parameters.
- Revision:
- Added a table that prohibits `connectome-constrained prediction → unique internal mechanism` to `wiki/decode-vs-emulate.md`.
- In addition, `connectome-only baseline and augmentation comparison`, `family comparison`, and `latent state audit` have been fixed as G5.

### 4. Short answer in FAQ didn't compress the latest evidence gate enough

- Issue:
- The FAQ is a useful starting point, but the answers for `When watching the brain-to-text demo` and `The difference between decode / emulate` were a little too short to read the strongest evidence in 2025.
- Revision:
- Updated Q1b, Q2, Q5b of `faq.md` and added prior baseline, silence/abstention, recalibration burden, and cross-day degradation in short form.

## Changes Made This Round

- `wiki/decode-vs-emulate.md`
- `last_updated` updated to 2026-03-15
- Updated front matter to reflect 2025 literature.
- Revised evidence ladder to `d'Ascoli / Tang / Willett / Littlejohn / Wairagkar / Flesher / MICrONS / Beiran` base
- Added `2026-03 Literature Audit: Three Replacements Prohibited Here`
- Updated to `5 gates before replacing decode with emulate`
- Changed site rule to 5 axes of `prior excess / cross-day / intervention / deployment / state completeness`
- `faq.md`
- Added `LM-only / no-brain / shuffle baseline`, `silence / abstention`, `long-term operation` to Q1b.
- Updated Q2 to prohibit replacement based on 2025 decode / subsystem closed-loop
- Updated Q5b to long-term closed-loop reading based on Littlejohn / Wairagkar / Wilson

## Deferred External-Dependency Tasks

- Real data preparation of public benchmarks that cross decode / emulate
- Person in charge: AI / maintainer / experimental collaborators
- Prerequisite: There is a public log that can compare `LM-only`, `no-brain`, `shuffle`, `OOD`, `cross-day`, `silence / abstention`, `recalibration burden`, `state-variable augmentation` with the same schema.
- Completion condition: `good visual output`, `good communication subsystem`, `close to state-complete emulate` can be compared publicly as separate evaluation axes without collapsing them into the same score.

## References

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021.
  - https://doi.org/10.1126/science.abd0380
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Billeh YN, Cai B, Gratiy SL, et al. Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex. *Neuron*. 2020.
  - https://doi.org/10.1016/j.neuron.2020.01.040
- Prinz AA, Bucher D, Marder E. Similar network activity from disparate circuit parameters. *Nat Neurosci*. 2004.
  - https://doi.org/10.1038/nn1352
