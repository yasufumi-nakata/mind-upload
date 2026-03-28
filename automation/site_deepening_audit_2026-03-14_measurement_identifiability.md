# Site Deepening Audit (2026-03-14, Measurement / Identifiability)

## Scope

- Main target: `tech_roadmap.md`
- Secondary target: `wiki/eeg-basics.md`

## Why This Page Was Selected

- As of 2026-03-14, public sites `verification` and `wbe_101` were significantly updated on the same day. On the other hand, `tech_roadmap` and `wiki/eeg-basics` still had weaknesses in terms of technology and natural science.
- The weak point is that the main text does not sufficiently distinguish between EEG/multimodal measurements, which are ``observable,'' ``correlations and predictions can be made,'' and ``internal states can be sufficiently identified.''
- This ambiguity is critical in the WBE debate. This is because improved source imaging and successful simultaneous measurements often confuse `seen` and `uniquely seen`.

## Main Critiques

### 1. In the measurement clause of `tech_roadmap.md`, the boundary between observability and identifiability was still loose.

- Issue:
- M1 correctly stated that ``different observed variables change what is restored,'' but the table did not fix which modality directly observes what and what remains latent.
- Therefore, when reading EEG/MEG/fMRI/ECoG/SEEG/connectomics side by side, a structure remained that made it easy to overinterpret multimodal integration as "resolution of missing state variables."
- Basis:
- Mikulan et al. (2020) provided a ground-truth dataset of intracranial stimulation + HD-EEG and indicated that source localization is an issue that should be audited with external standards.
- Seeber et al. (2019) showed that subcortical activity can be conditionally detected in 256ch scalp EEG, but they do not claim general unique restoration.
- Unnwongse et al. (2023) showed in direct validation using intracranial stimulation that localization error depends on conductivity assumption and source depth.
- Hao et al. (2025) reported in 29 cases of simultaneous HD-EEG/SEEG that source power and source depth greatly affect ESI accuracy.
- Dorkenwald et al. (2024), MICrONS Consortium et al. (2025), Gamlin et al. (2025), and Cahill et al. (2024) reinforce that even when structure and local function are linked in the same brain, cell-type / neuromodulatory / glial state still remains as a separate variable.
- Revision:
- Added observability matrix of `Observation route / Direct observation / What can be said strongly / Remaining latent state` to M1 of `tech_roadmap.md`.
- As a note in M1, we clarified that ``multimodal is not the achievement of state completeness'' with the name of the primary literature.

### 2. R7 of `tech_roadmap.md` stated identifiability in general terms, but the implications of direct validation literature were weak.

- Issue:
- R7 mentioned the need for sensitivity analysis, family comparison, and abstention conditions, but the structure was difficult for readers to directly connect with the validation study as to why they were writing so harshly.
- As a result, there was room to misinterpret cross-modal correlations and held-out predictions as identifications that were close to the unique solution.
- Basis:
- Seeber et al. (2019) showed detectability, but it is not a general solution for source identifiability.
- Unnwongse et al. (2023) showed that even under direct validation conditions, localization errors remain on the order of cm.
- Hao et al. (2025) reported that the error strongly depends on source depth and source power in simultaneous HD-EEG/SEEG.
- Revision:
- Added a note to R7 of `tech_roadmap.md` that "correlation, prediction, and identification are not treated with the same strength".
- An operational rule to read `Increasing predictability` and `Unique solution to internal state` separately has been embedded into the main text.

### 3. `wiki/eeg-basics.md` is easy to read as an introduction, but it did not reflect the validation literature as of 2026-03.

- Issue:
- While it is concise for beginners, when I moved on from the explanation that ``EEG is a mixed signal,'' I couldn't see where it started with observation, where it started with conditional estimation, and where it became a question of external validation.
- There was no references section, and the link back to more rigorous discussion on the public site was weak.
- Basis:
- Mikulan et al. (2020) published a public benchmark, and the minimum line for auditing source localization with ground-truth has become quite concrete.
- According to Unnwongse et al. (2023) and Hao et al. (2025), we have reached the stage where the results of direct validation and simultaneous HD-EEG/SEEG should at least be reflected on the beginner page.
- Revision:
- Added `Observation, estimation, and identification are separate` section to `wiki/eeg-basics.md` and divided the EEG explanation into three stages.
- `2026-03 actual measurement evidence` Added notes and simplified Seeber / Unnwongse / Hao implications for beginners.
- Added a bibliography section and related links to return to `measurement-and-modeling-terms`.

## Changes Made This Round

- `tech_roadmap.md`
- Added observability matrix to M1
- Added `multimodal ≠ state completeness` note to M1
- Added `predictability ≠ identifiability` note to R7
- Added Seeber (2019), Dorkenwald (2024), MICrONS (2025), Gamlin (2025), Cahill (2024) to references
- `wiki/eeg-basics.md`
- Added `Observation, estimation, and identification are different` section
- Direct validation Based on literature 2026-03 Added notes
- Added references section and related links

## Deferred External-Dependency Tasks

- Implementation and continuous monitoring of source imaging benchmark
- Person in charge: AI / maintainer
- Prerequisite: Localize-MI, simultaneous HD-EEG/SEEG, continuous acquisition and maintenance of intracranial stimulation data
- Completion condition: Translate the `direct validation` points on the site to a public bench that can be reproduced with real data.

## References

- Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. Scientific Data. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nature Communications. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. Brain Communications. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, Alhilani M, Asano E, et al. High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Dorkenwald S, McKellar CE, Macrina T, et al. Neuronal wiring diagram of an adult brain. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
