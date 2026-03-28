# Site Deepening Audit (2026-03-14, Connectome / State Completeness)

## Scope

- Main target: `wiki/connectome-is-not-enough.md`

## Why This Page Was Selected

- The public site already had the correct direction `connectome-complete is not emulation-complete`, but as of 2026-03-14, the main text was still `enumeration of missing state variables`.
- However, there are two important points that the primary literature for 2024-2025 shows.
1. There are multiple state variables missing from the wiring diagram.
2. Even if connectome-constrained, the dynamics itself can degenerate if unmeasured cell/synapse/modification parameters remain.
- The former version was correct in the previous version, but the `identifiability wall` was weak, and there was latter room for readers to misread it as `connectome + a little activity = the internal state was pretty clear`.

## Main Critiques

### 1. The previous version explained "missing state variables" but did not treat "degeneracy that remains even in connectome-constrained" as an independent issue.

- Issue:
- The previous version correctly listed `Cell type / Synapse / Delay / Neuromodification / Glial`.
- However, the main text did not clearly state that the internal dynamics are often not unique even if the connectome is known.
- Basis:
- Beiran & Litwin-Kumar (2025) showed that even in connectome-constrained recurrent networks, the dynamics of unobserved neurons can change significantly due to differences in biophysical parameters.
- Lappalainen et al. (2024) advanced the connectome-constrained model with a fly visual system, but the authors themselves put electrical synapses, nonlinear chemical synapses, and neuromodulation outside the explanation of the reductionist model.
- Revision:
- Added `1 putative wall (parameter degeneracy)` in addition to `5 state classes`.
- Specified site rule to read `connectome-constrained model` as `hypothesis engine / conditional model` instead of unique internal state.

### 2. The old version did not fix "dangerous misreading" and "claim downgrade" for each state class

- Issue:
- The previous version introduced each state class, but `What should be considered an overstatement` and `Which claims should be stopped if they remain missing` were not fixed in the table.
- For this reason, the structure was such that readers could misread unlabeled graph, edge count, pupil/HRV, etc. as functionally sufficient conditions or transmitter ground truth.
- Basis:
- MICrONS Consortium (2025) showed that in the mammalian cortex, there are neurons with different tuning preferences even within the same cell type, and it is necessary to connect same-brain connectivity and function.
- Gamlin et al. (2025) showed that different predicted Sst transcriptomic types have different binding, synaptic properties, and myelination.
- Holler et al. (2021) and Matsuzaki et al. (2004) showed that synapses have ultrastructure / weight / plastic history rather than binary edges.
- Vardalaki et al. (2022) showed that filopodia can serve as the structural basis for silent synapse even in the adult neocortex.
- Reimer et al. (2016) and Neyhart et al. (2024) showed that even though pupils and behavioral states reflect cholinergic/adrenergic dynamics, they do not replace local release/clearance or transmitter specificity.
- Revision:
- Reorganized the opening table into 4 columns of `What's missing / Dangerous misreading / Current treatment`.
- Clarified operation rules that can be used site-wide, such as `demote phase/intervention/closed-loop claims in the absence of weights/delays`.

### 3. The previous version was weak in ``what to request as a submission from this discussion'' and was difficult to put into practical use.

- Issue:
- The previous version was conceptually sound, but the structure made it difficult for readers and future editors to determine ``So what should I make to make a claim close to L1 / L2 / L3?''.
- Basis:
- A discussion of state completeness will not be effective if it ends up as a mere caution note.
- Actually, the required submissions are different for structural atlas, conditional dynamical claim, and intervention/closed loop claim.
- Revision:
- Added `Replacement rules and minimum submissions adopted by this site` section.
- The minimum submissions are listed in three columns: `structural atlas / scaffold`, `conditional dynamical claim`, `intervention/closed-loop claim`.

## Changes Made This Round

- `wiki/connectome-is-not-enough.md`
- Updated front matter to `missing state variable + limit of connectome-constrained estimation`
- Expand opening table to `5 state classes + 1 inferential wall`
- Added `0th problem that is easy to overlook: Even if the wiring is known, the dynamics are still degenerate` clause
- Fixed `dangerous misreading` and `Currently handling` as tables
- Added `Minimum submissions` table
- Added primary literature from 2022-2025

## Deferred External-Dependency Tasks

- Implementation of `state completeness benchmark` using same-brain multimodal / perturbation
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisites: publicly available connectomics + same-brain physiology + perturbation data or equivalent benchmark
- Completion condition: A public evaluation system is in place that allows comparison of `missing state variable` and `remaining family` using the same schema.

## References

- Dorkenwald S, McKellar CE, Macrina T, et al. Neuronal wiring diagram of an adult brain. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Lappalainen JK, Tschopp FD, Prakhya S, et al. Connectome-constrained networks predict neural activity across the fly visual system. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07939-3
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Holler S, et al. Structure and function of a neocortical synapse. Nature. 2021.
  - https://doi.org/10.1038/s41586-020-03134-2
- Matsuzaki M, Honkura N, Ellis-Davies GCR, Kasai H. Structural basis of long-term potentiation in single dendritic spines. Nature. 2004.
  - https://doi.org/10.1038/nature02617
- Vardalaki D, Chung K, Harnett MT. Filopodia are a structural substrate for silent synapses in adult neocortex. Nature. 2022.
  - https://doi.org/10.1038/s41586-022-05483-6
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. Science. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. Science. 2014.
  - https://doi.org/10.1126/science.1254960
- Micheva KD, Kiraly M, Perez MM, Madison DV. Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. Cereb Cortex. 2021.
  - https://doi.org/10.1093/cercor/bhab018
- Reimer J, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. Nat Commun. 2016.
  - https://doi.org/10.1038/ncomms13289
- Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. Cell Reports. 2024.
  - https://doi.org/10.1016/j.celrep.2024.114808
- Adamsky A, et al. Astrocytic activation generates de novo neuronal potentiation and memory enhancement. Nat Neurosci. 2018.
  - https://doi.org/10.1038/s41593-018-0253-6
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
