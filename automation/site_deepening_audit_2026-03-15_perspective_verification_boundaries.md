# Site Deepening Audit (2026-03-15, Perspective / Verification Boundaries)

## Scope

- Main target: `perspective.md`

## Why This Page Was Selected

- `perspective.md` is a long page that is most easily referenced as a position statement on the site.
- As of 2026-03-15, each theory has been updated, but in the `Decoding → Emulation` section, there still remained a structure where `local connectomics`, `non-invasive source imaging`, `sleep-dependent maintenance-state`, `closed-loop intervention`, and `thermodynamic readout` were seen easily as one "difficulty".
- This is a high priority improvement from a technical/natural science perspective. This is because if we read different types of advances in the same way, we tend to overestimate `local digital twin` to `human whole-brain state-complete`, `good decode / localization` to `unique restoration`, and `local causal gain` to `WBE validation`.

## Main Critiques

### 1. Observability and identifiability were mixed

- Issue:
- In the previous version, the boundary between `Measurement advancement` and `Unique restoration of internal state` was not fixed as a table even though it was indicated in bullet points.
-Therefore, there was room to misread improvements in local connectomics and source imaging as `whole brain status was much more visible`.
- Basis:
- Dorkenwald et al. (2024) showed a wiring diagram of the adult Drosophila whole brain.
- MICrONS Consortium et al. (2025) advanced same-brain function / connectomics correspondence in a single mouse 1 mm³ cortex, but not in a human whole-brain.
- Michel & Brunet (2019) and Aydin et al. (2019) clarify that the EEG inverse problem still depends on the head model and conductivity assumption.
- Frässle et al. (2021) advanced model-family comparison, but did not guarantee general uniqueness recovery.
- Revision:
- Added a table with `observability` and `identifiability` on separate lines.
- Added a site rule to the text that does not allow `local digital twin / ESI / whole-brain WBE` to be written in the same line.

### 2. The maintenance-state wall was too compressed with the word `connectome is missing`

- Issue:
- Hidden state was mentioned in the previous version, but sleep/wake, myelin sheath, and glial/metabolic support were not fixed as `an independent wall to stop cross-day claims`.
- This left room for the same-day activity match and decode results to appear more like evidence of overnight maintenance and timing-sensitive stability.
- Basis:
- Hengen et al. (2016), Torrado Pacheco et al. (2021), and Xu et al. (2024) showed sleep/wake-dependent homeostatic recovery.
- Looser et al. (2024) demonstrated oligodendrocyte-axon metabolic coupling.
- Cahill et al. (2024) and Lee et al. (2022) strengthened glial / active maintenance.
- Revision:
- Added `maintenance-state wall` as a separate line.
- Added `cross-day claim requires maintenance-state longitudinal log` to the text.

### 3. The locality of the intervention evidence was weak, and the structure made it easy to interpret closed-loop success as a higher-level claim.

- Issue:
- The previous version emphasized the importance of causal evidence, but it was not fixed in the table which interventions were `local subsystem evidence` and which were unsupported.
- Basis:
- Hernandez-Pavon et al. (2023) organized the stimulus conditions, masking, and artifact management necessary for TMS-EEG comparability.
- Flesher et al. (2021) showed local causal gain with bidirectional BCI.
- Oehrn et al. (2024) advanced the clinical feasibility of adaptive DBS, but in a local loop with disease conditions.
- Revision:
- Added `intervention wall` as a separate line.
- Changed the policy to read `passive observation / held-out perturbation / online loop / long-term adaptive operation` as separately staged evidence.

### 4. It was written that the thermodynamic readout was an auxiliary log, but its relative position to other walls was ambiguous.

- Issue:
- In the previous version, although thermodynamic caution itself was correct, its relative position alongside observability/intervention was weak, and the structure made it easy for readers to feel that it was ``stronger due to exposure to physical constraints.''
- Basis:
- What Lynn et al. (2021) and de la Fuente et al. (2022) showed is the irreversibility signature of coarse-grained neural dynamics.
- Ishihara & Shimazaki (2025) remains difficult to stably estimate arrow of time from spiking.
- Revision:
- `thermodynamic readout wall` has been clearly displayed in the table, and its position as an auxiliary log has been fixed alongside other walls.

## Changes Made This Round

- `perspective.md`
- `last_updated` updated to 2026-03-15
- Updated `page_highlights` / `known_points` / `wiki_links` to make the verification boundary easier to read.
- Added `5 walls` table to `Decoding → Emulation` section
- Added `Replacement prohibited in this section` in note-box
- Add `maintenance-state logs including cross-day` to `minimum evidence chain`
- Reorganized the engineering limits of `Limitations` into the four pillars of `observability / identifiability / maintenance-state / intervention scope`

## Deferred External-Dependency Tasks

- Public data preparation for cross-day maintenance-state benchmark
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisite: Public data that can track sleep state, recovery, myelin / glial proxy, and intervention log in the same individual
- Completion condition: same-day fit, cross-day stability, and online perturbation can be compared using the same schema.

## References

- Dorkenwald S, et al. Neuronal wiring diagram of an adult brain. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Michel CM, Brunet D. EEG source imaging: a practical review of the methodology. *Front Neurol*. 2019.
  - https://doi.org/10.3389/fneur.2019.00325
- Aydin U, Vorwerk J, Küpper P, et al. Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. *Front Neurosci*. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Frässle S, et al. Regression DCMs for fMRI. *NeuroImage*. 2021.
  - https://doi.org/10.1016/j.neuroimage.2020.117566
- Hengen KB, et al. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. *Neuron*. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nat Commun*. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nat Neurosci*. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *PNAS*. 2022.
  - https://doi.org/10.1073/pnas.2211572119
- Hernandez-Pavon JC, et al. TMS combined with EEG: Recommendations and open issues. *Brain Stimul*. 2023.
  - https://doi.org/10.1016/j.brs.2023.02.009
- Flesher SN, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021.
  - https://doi.org/10.1126/science.abd0380
- Oehrn CR, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson’s disease: a blinded randomized feasibility trial. *Nat Med*. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Lynn CW, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021.
  - https://doi.org/10.1073/pnas.2109889118
- de la Fuente LA, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. *Cereb Cortex*. 2022.
  - https://doi.org/10.1093/cercor/bhac177
- Ishihara K, Shimazaki H. Entropy flow reveals the arrow of time from neuronal spiking activity. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-66669-w
