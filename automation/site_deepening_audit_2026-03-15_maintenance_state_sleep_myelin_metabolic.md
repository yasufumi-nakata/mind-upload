# Site Deepening Audit (2026-03-15, Maintenance State / Sleep / Myelin / Metabolic Support)

## Scope

- Main target: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Secondary target: `verification.md`

## Why This Page Was Selected

- As of 2026-03-14, the public site was pretty clear that connectome and cell type are not enough.
- However, `Wiki: Homeostatic plasticity and the maintenance state` still had its center of gravity at three points, `intrinsic excitability/firing rate set point/molecular turnover`, and did not sufficiently fix sleep-dependent renormalization, myelin sheath/oligodendrocytes, and glial metabolic support as the main body of the maintenance-state.
- This is a weakness from a technical/natural science perspective. This is because when reading long-term dynamics, cross-day stability, rebalance after learning, and timing-sensitive closed loop, it was easy to misread as ``the maintenance mechanisms are similar.''

## Main Critiques

### 1. The current page defined maintenance-state too narrowly and could not treat sleep as the controller's time axis.

- Issue:
- The previous version covered the firing-rate set point and molecular turnover, but did not emphasize that the sleep / wake cycle itself is the execution phase of synaptic scaling and homeostatic recovery.
- Therefore, there remained room for same-day activity matching and short-term decoding results to be interpreted as evidence of cross-day stability or long-term maintenance.
- Basis:
- Hengen et al. (2016) showed that firing-rate homeostasis progresses asymmetrically during sleep/wake.
- Torrado Pacheco et al. (2021) showed that sleep promotes downward downward-rate homeostasis.
- de Vivo et al. (2017), Diering et al. (2017), Noya et al. (2019), and Xu et al. (2024) showed that ultrastructure, synaptic modeling, proteome, and network regime are systematically updated during sleep.
- Revision:
- Reorganized `wiki/homeostatic-plasticity-and-maintenance-state.md` from `3` to `6` maintenance-state.
- Added `sleep / wake dependent renormalization` as an independent class to separate same-day fit and overnight maintenance.

### 2. Previous version did not include myelin / oligodendrocyte state sufficiently in maintenance-state

- Issue:
- In the old version, the story about delay and myelin sheath was moved to another page, and `Keep State` looked neuro-centric on this page alone.
- But in timing-sensitive claims, myelin is not just a fixed delay, but an activity-dependent variable of state.
- Basis:
- Gibson et al. (2014) showed that neuronal activity promotes oligodendrogenesis and adaptive myelination.
- McKenzie et al. (2014) showed that active central myelination is necessary for motor skill learning.
- Looser et al. (2024) showed that oligodendrocyte-axon metabolic coupling is involved in maintaining axonal health.
- Revision:
- Added `myelin sheath / oligodendrocyte support` as an independent class.
- Updated the operation rule to record what was discarded in the main text when delay is absorbed with a fixed constant.

### 3. The old version treated glial / metabolic support close to `molecular turnover background` and was weak as a main variable for memory consolidation.

- Issue:
- The previous version described active maintenance as the persistence of a molecular state, but did not sufficiently separate support mechanisms such as astrocyte-neuron lactate transport and astrocyte network state.
- As a result, there remained a structure where memory persistence could be read as a problem with `only the internal state on the neural side`.
- Basis:
- Suzuki et al. (2011) showed that astrocyte-neuron lactate transport is required for long-term memory formation.
- Cahill et al. (2024) showed that local neurotransmitter input is encoded into astrocyte network state minute-long.
- Lee et al. (2022) showed that memory can remain through active maintenance even under molecular turnover.
- Revision:
- Separated `glial metabolism / substrate routing` and `reimmobilization under molecular turnover`.
- Revised text to read memory maintenance as `renormalization and resolidification chain` instead of `static storage`.

### 4. The state-completeness gate on the verification side also did not sufficiently reflect the spread of maintenance-state.

- Issue:
- The table for `verification.md` is useful, but the explanation for `Intrinsic excitability/homeostasis set point` was too focused on excitability and did not explicitly mention sleep-dependent renormalization or recovery controller.
- Revision:
- Updated the relevant line of `verification.md` to include renormalization and recovery controller depending on sleep/wake.
- Notes on practical rules have also been rephrased as `homeostasis/maintenance state`.

## Changes Made This Round

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Updated front matter and summary
- `6 maintenance-state` Completely revised table
- Added sections on sleep-dependent renormalization, adaptive myelination, oligodendrocyte metabolic coupling, and astrocyte metabolic support.
- Updated misreading table and practical rules to accommodate cross-day / overnight / timing-sensitive claims.
- Expanded references to 18 books
- `verification.md`
- Update `Intrinsic excitability/homeostasis set point` line in `State variable integrity gate`
- Sync to `homeostasis/maintenance state` representation of notes

## Deferred External-Dependency Tasks

- Maintenance of public benchmarks including sleep / myelin / glial maintenance
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisite: Public data that can track sleep state, cross-day recovery, myelin proxy, and glial/metabolic proxy in the same individual.
- Completion condition: A benchmark that can compare `same-day fit`, `overnight recovery`, and `timing-sensitive stability` with the same schema can be reused site-wide.

## References

- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. Cell. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. Neuron. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- de Vivo L, et al. Ultrastructural evidence for synaptic scaling across the wake/sleep cycle. Science. 2017.
  - https://doi.org/10.1126/science.aah5982
- Diering GH, et al. Homer1a drives homeostatic scaling-down of excitatory synapses during sleep. Science. 2017.
  - https://doi.org/10.1126/science.aai8355
- Noya SB, et al. The forebrain synaptic transcriptome is organized by clocks but its proteome is driven by sleep. Science. 2019.
  - https://doi.org/10.1126/science.aav2642
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. Nature Communications. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. Science. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. Science. 2014.
  - https://doi.org/10.1126/science.1254960
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. Nature Neuroscience. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. Cell. 2011.
  - https://doi.org/10.1016/j.cell.2011.02.018
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. PNAS. 2022.
  - https://doi.org/10.1073/pnas.2211572119
