# Site Deepening Audit (2026-03-15, Entry Pages / Maintenance-State Propagation)

## Scope

- Main target: `index.md`
- Secondary target: `wbe_101.md`
- Secondary target: `faq.md`

## Why This Page Was Selected

- In the individual wiki and `verification.md`, it became quite clear that the connectome alone was not enough and the spread of the maintenance-state.
- However, in the public entry pages, the points of discussion were too compressed into `Links to related wikis`, and the structure remained that readers who read it for the first time could easily misread it as `Once you get the wiring diagram + cell type, the rest is fine-tuning`.
- The entrance page determines how the site-wide is read, so if it is rough, the careful position of `connectome-complete is scaffold` that follows will not be fully conveyed.

## Main Critiques

### 1. The entry page showed maintenance-state as "additional information that seems to exist"

- Issue:
- `index.md` and `wbe_101.md` touched on connectome deficiency, but they did not fix at the entrance what sleep/wake-dependent renormalization, myelin sheath/oligodendrocyte support, and glial/metabolic support destroy.
- As a result, it was not brought to the foreground that `same-day activity matching` and `cross-day maintenance mechanism matching` are different issues.
- Basis:
- Hengen et al. (2016), Torrado Pacheco et al. (2021), and Xu et al. (2024) showed that sleep/wake cycles are involved in firing-rate homeostasis and network regime recovery.
- Gibson et al. (2014), McKenzie et al. (2014), and Looser et al. (2024) showed that myelin/oligodendrocyte support is involved in timing and axonal health.
- Suzuki et al. (2011), Cahill et al. (2024), and Lee et al. (2022) showed that glial/metabolic support and active maintenance under turnover are involved in memory consolidation and slow state.
- Revision:
- `connectome-complete ≠ emulation-complete` was specified as `connectome-complete ≠ emulation-complete` to prevent misreading at the entrance.
- Added `hidden state that cannot be removed at the entrance` section to `wbe_101.md` and summarized it into 4 classes.

### 2. The entrance page lacked boundaries for "how much you can say"

- Issue:
- The existing conductor was useful in guiding deep into the wiki, but the entrance itself did not keep short and fixed.
- This left room for readers to confuse `connectome-complete` and `digital twin` with state-complete reconstruction.
- Basis:
- Gouwens et al. (2021) showed that continuity of morpho-electric phenotype remains even within the same transcriptomic type.
- All of the above sleep/myelin/glia primary literature indicates that the state variables that support long-term dynamics remain outside the wiring diagram.
- Revision:
- `wbe_101.md` has been specified as `connectome-complete is an advance of the structural scaffold, not a declaration of emulation-complete`.
- The text also states that this judgment is an **inference** based on the fact that the above primary literature leaves maintenance-state as a separate variable.

### 3. There was no section in the FAQ that directly answered this misconception

- Issue:
- The FAQ is an excellent starting point, but there was no section that directly answered the natural question ``Is it enough to know the connectome and cell type?''
- Therefore, even though it was an important issue, the reader had to go deeper into the wiki to reach the answer.
- Revision:
- Added `Q. If we know the connectome and cell type, will most of the rest be filled in? ` to `faq.md`.
- Added a short list of sleep / myelin / glia early in the entrance and a link back to the details page.

## Changes Made This Round

- `index.md`
- `last_updated` updated to 2026-03-15
- Added missing maintenance-state to `page_highlights` / `known_points`
- Added a new note for `Prevent misreading at the entrance`
- `wbe_101.md`
- `last_updated` updated to 2026-03-15
- Added `hidden state that cannot be removed at the entrance` section
- Add primary literature on sleep / myelin / glia / maintenance-state to references
- `faq.md`
- `last_updated` updated to 2026-03-15
- Added `Q2c`
- Updated entrance information table and references

## Deferred External-Dependency Tasks

- Common schema for maintenance-state artifact pack
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisite: be able to compare sleep history, overnight recovery, conduction / myelin proxy, and glial / metabolic proxy using the same benchmark
- Completion condition: `same-day fit`, `cross-day recovery`, `timing-sensitive stability`, `active maintenance` can be submitted in the same schema.

## References

- Gouwens NW, et al. Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. Nature. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. Cell. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. Neuron. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. Nat Commun. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. Science. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. Science. 2014.
  - https://doi.org/10.1126/science.1254960
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. Nat Neurosci. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. Cell. 2011.
  - https://doi.org/10.1016/j.cell.2011.02.018
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. Proc Natl Acad Sci U S A. 2022.
  - https://doi.org/10.1073/pnas.2211572119
