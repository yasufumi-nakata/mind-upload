# Site Deepening Audit (2026-03-14, Homeostatic Maintenance States)

## Scope

- Main target: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Secondary target: `wiki/connectome-is-not-enough.md`
- Secondary target: `verification.md`
- Secondary target: `wbe_101.md`
- Secondary target: `tech_roadmap.md`
- Secondary target: `perspective.md`
- Secondary target: `wiki/index.md`

## Why This Page Was Selected

- In today's automatic deep digging, the general framework `connectome is scaffold, not state-complete` has already been strengthened.
- However, the main state-completeness discussion on the current site is centered around `Cell type / synapse / delay / neuromodification / glia`, and `Intrinsic excitability / firing-rate set point / maintenance mechanism under molecular turnover` has not come to the fore as an independent class.
- This omission allows for the misreading as `The same connectome + the same cell type will determine the long-term dynamics to a large extent.' From a technical and natural science perspective, this is still an exaggeration.

## Main Critiques

### 1. The old version underestimated `intrinsic excitability` after setting `cell type`

- Issue:
- The previous version emphasized transcriptomic type and same-brain function, but did not treat the fact that even within the same type there was a range of morpho-electric phenotype and ion-channel expression as independent missing variables.
-Therefore, the mispronunciation of `cell-type labeling roughly determines threshold / gain / recovery` remained.
- Basis:
- Gouwens et al. (2021) showed that the transcriptomic type of mouse cortex has continuous fluctuations in morpho-electric space.
- Schulz et al. (2006) showed that there are large individual differences in ion-channel mRNA and current levels even among identified neurons.
- Revision:
- Updated the state-completeness description for `wiki/connectome-is-not-enough.md` and `verification.md` from `5 class` to `6 class`.
- Added a new `Intrinsic excitability/homeostasis set point` line.

### 2. The old version did not separate `Current activity value` and `Where to go back`

- Issue:
- Previous editions discussed short-term state and synaptic state, but did not treat homeostatic controllers and firing-rate set points as separate technical issues.
- As a result, `short-term activity matching` and `long-term stability` were read as being close.
- Basis:
- Turrigiano et al. (1998) demonstrated homeostatic synaptic scaling.
- O'Leary et al. (2014) showed that set points and compensations are generated from activity-dependent channel expressions.
- Hengen et al. (2016) demonstrated precise firing-rate set points for individual neurons in vivo.
- Revision:
- Organized `firing rate set point / homeostatic controller` as an independent maintenance-state in the newly created wiki.
- Also reflected in `verification.md`, `tech_roadmap.md`, `perspective.md` as a condition to weaken the long-term claim.

### 3. The old version had a structure where `memory remains` could be misread as `static storage is sufficient`

- Issue:
- The previous edition dealt with plasticity and synaptic states, but did not clearly point out that when memory is maintained across molecular turnover, this means active maintenance.
- Basis:
- Yiu et al. (2014) showed that relative excitability affects memory allocation.
- Lee et al. (2022) showed that synaptic memory can be maintained by active state transfer even under molecular turnover.
- Revision:
- Added `Maintenance mechanism under molecular turnover` as a third maintenance-state in the new wiki.
- Clarified the rule not to read it as `memory persistence = static molecular storage`.

## Changes Made This Round

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
- New addition
- Organize `intrinsic excitability / ion-channel configuration`, `firing rate set point / homeostatic controller`, `maintenance mechanism under molecular turnover` into three maintenance-states.
- Includes 8 primary sources and clearly states dangerous misreadings and site rules.
- `wiki/connectome-is-not-enough.md`
- Update `5 class` to `6 class`
- Add `Intrinsic excitability/homeostasis set point` as a separate line
- Added detailed explanation and link to new wiki
- `verification.md`
- Updated state variable integrity gate to `6 class`
- Added lead to new wiki
- `wbe_101.md`
- Added a link from the introductory page to the new wiki
- `tech_roadmap.md`
- Added `intrinsic excitability / homeostatic set point` to R series and M3
- `perspective.md`
- Updated `5 State Class` to `6 State Class` in core description
- `wiki/index.md`
- Added new wiki leads

## Deferred External-Dependency Tasks

- Direct human excitability-homeostasis benchmark
- Person in charge: Experimental collaborators / maintainer
- Prerequisites: long-term repeated measurements, perturbation, intracellular or invasive ground truth, cross-day tracking
- Completion condition: A benchmark that can compare connectome / cell type / excitability / recovery with the same schema will be published.

## References

- Gouwens NW, et al. Phenotypic variation of transcriptomic cell types in mouse motor cortex. Nature. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Schulz DJ, Goaillard J-M, Marder E. Variable channel expression in identified single and electrically coupled neurons in different animals. Nat Neurosci. 2006.
  - https://doi.org/10.1038/nn1639
- Turrigiano GG, Leslie KR, Desai NS, Rutherford LC, Nelson SB. Activity-dependent scaling of quantal amplitude in neocortical neurons. Nature. 1998.
  - https://doi.org/10.1038/36103
- O'Leary T, Williams AH, Franci A, Marder E. Cell types, network homeostasis, and pathological compensation from a biologically plausible ion channel expression model. Neuron. 2014.
  - https://doi.org/10.1016/j.neuron.2014.04.002
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. Cell. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Yiu AP, et al. Neurons are recruited to a memory trace based on relative neuronal excitability immediately before training. Neuron. 2014.
  - https://doi.org/10.1016/j.neuron.2014.07.017
- Hadzibegovic N, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. Nat Commun. 2026.
  - https://doi.org/10.1038/s41467-025-66975-3
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. Proc Natl Acad Sci U S A. 2022.
  - https://doi.org/10.1073/pnas.2211572119
