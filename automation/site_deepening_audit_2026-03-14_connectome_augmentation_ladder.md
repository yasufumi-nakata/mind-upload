# Site Deepening Audit (2026-03-14, Connectome / Augmentation Ladder)

## Scope

- Main target: `wiki/connectome-is-not-enough.md`
- Secondary target: `verification.md`

## Why This Page Was Selected

- On the public site as of 2026-03-14, the `connectome-complete ≠ emulation-complete` criticism itself was pretty well organized.
- However, the current explanation still leans toward `enumeration of missing state variables`, making it difficult for readers to understand in a way that they can compare and understand, ``What should I add to advance to a predicted stronger claim?''
- This lack is a weakness in the technical and natural science aspects. This is because simply enumerating an infinite number of state variables will make the research design look like ``Not enough of anything'' instead of ``What to take'', reducing demonstrability.

## Main Critiques

### 1. The current site could say ``What's missing?'', but ``What should we add to see it as an improvement?'' was not in the foreground.

- Issue:
- `wiki/connectome-is-not-enough.md` was shown in the primary literature to lack cell types, intrinsic excitability, synapses, delays, neuromodification, and glia.
- However, there was no table to compare the incremental value of state variables as `augmentation / ablation`, and the structure made it difficult for readers to follow "which additional measurement reduces which error term."
- Basis:
- Lappalainen et al. (2024) showed broad activity predictions in connectome-constrained networks, but excluded electrical synapses, nonlinear chemical synapses, neuromodulation, etc.
- Beiran & Litwin-Kumar (2025) showed that even if a connectome is given, recurrent dynamics can be significantly degenerate if unmeasured biophysical parameters are different.
- MICrONS Consortium et al. (2025) connected dense neural activity, EM connectome, pupil diameter, and locomotion in the same individual, embodying the incremental value of `same-brain structure + function + behavior`.
- Revision:
- Added `augmentation / ablation` clause to `wiki/connectome-is-not-enough.md`.
- Fixed `connectome-only baseline`, `+ same-brain function / behavior`, `+ transcriptomic / cell-type label`, `+ local transmitter dynamics`, `+ glial / slow-state`, `+ perturbation / recovery of excitability-homeostasis` in the stage table.

### 2. Regarding neuromodulation and glia, the operational rules above were weak.

- Issue:
- The existing site could say up to `pupil / HRV is coarse proxy` and `glia is not support tissue`.
- However, it was unclear under what conditions to promote from `covariate` to `state variable that gave predictive gain`.
- Basis:
- Neyhart et al. (2024) showed that while cortical ACh dynamics can be fairly predicted from cholinergic axon activity and behavioral state, locality remains dependent on distance and clearance kinetics.
- Cahill et al. (2024) showed that local, transient neurotransmitter inputs are encoded minute-long into the broad cortical astrocyte network.
- Vadisiute et al. (2024) showed that astrocytes, microglia, and synaptic density rapidly change after acute chemogenetic manipulation.
- Revision:
- Added site rule `Do not write that the added state variable was effective without placing a connectome-only baseline`.
- Updated to include `proxy specificity`, `family / uncertainty`, and `abstention` in simultaneous submissions.

### 3. The state variable integrity gate was still closer to `missing list` on the Verification side.

- Issue:
- `State Variable Integrity Gate` in `verification.md` was useful as a table showing what was missing, but the structure made it difficult for researchers to list the next submissions.
-Therefore, even if the reader understood `missing state variables`, it was difficult to read `what to compare to the baseline`.
- Basis:
- Primary literature from MICrONS, Gamlin, Neyhart, Cahill, Hadzibegovic et al. indicates the value of additional information should be read apart from ``Under what state change/recovery/task conditions does it work?''.
- Revision:
- Added comparison table for `augmentation claim` to `verification.md`.
- For `+ same-brain function / behavior`, `+ transcriptomic / cell-type label`, `+ neuromodulatory proxy`, `+ glial / slow-state`, `+ excitability / homeostatic recovery log`, we have fixed the minimum desired comparison and the replacement in case of failure.

## Changes Made This Round

- `wiki/connectome-is-not-enough.md`
- Added `augmentation / ablation` clause
- Explicit `connectome-only baseline`
- Added `state-variable augmentation claim` minimum submissions to table
- Added Vadisiute (2024) and Hadzibegovic (2026) to references
- `verification.md`
- Added comparison table of augmentation claims to `state variable integrity gate`
- Convert connectome / same-brain function / transcriptomic label / neuromodulatory proxy / glial state / recovery log into comparable submissions
- Add related primary papers to references

## Deferred External-Dependency Tasks

- Preparation of real data for same-brain augmentation benchmark
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisite: Public data that allows you to compare connectome-only baseline and augmentation conditions using the same split.
- Completion condition: Publish predictive gains including cross-state / cross-day / perturbation / recovery in a schema that can be reused site-wide.

## References

- Lappalainen JK, Tschopp FD, Prakhya S, et al. Connectome-constrained networks predict neural activity across the fly visual system. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07939-3
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. Nature Neuroscience. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. Cell Reports. 2024.
  - https://doi.org/10.1016/j.celrep.2024.114808
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Vadisiute A, Meijer E, Therpurakal RN, et al. Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. Communications Biology. 2024.
  - https://doi.org/10.1038/s42003-024-06994-w
- Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. Nature Communications. 2026.
  - https://doi.org/10.1038/s41467-025-66975-3
