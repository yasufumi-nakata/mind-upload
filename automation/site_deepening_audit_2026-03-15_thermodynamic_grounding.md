# Site Deepening Audit (2026-03-15, Thermodynamic Grounding)

## Scope

- Main target: `tech_roadmap.md`
- Secondary target: `wiki/thermodynamic-grounding-basics.md`

## Why This Page Was Selected

- Thermodynamics on the public site was written very carefully in `verification.md` and `wiki/thermodynamic-grounding-basics.md`, but `I9` in `tech_roadmap.md` was still written too strongly.
- In particular, the old `I9` bundled `Landauer lower bound`, `metabolic budget of the living brain`, `time irreversibility of coarse-grained neural dynamics`, and `model-based entropy flow` into one essential book, making it readable beyond the reach of primary literature.
- This is a site-wide issue. `tech_roadmap.md` is a standard page where learners read ``Which problems must be solved to move forward?'' If the exploratory support log is made to look like a required gate here, even the careful descriptions on other pages will be weakly read.

## Main Critiques

### 1. Old `I9` mixed different measurement layers into one engineering requirement

- Issue:
- The previous version presented `Landauer`, `EPR > 0`, `20W`, `Communication: Computation Ratio`, `Virtual Dissipation Protocol` as a series of design conditions.
- But these are not the same amount of layers.
- Basis:
- Bérut et al. (2012) demonstrated a minimum dissipation lower bound for `logically irreversible` 1-bit erasure, not wall-power or NESS reproduction conditions for the entire digital brain.
- Lynn et al. (2021) estimated broken detailed balance and entropy production from coarse-grained fMRI state dynamics, but the paper itself clearly states that coarse graining can average out nonequilibrium degrees of freedom.
- Nartallo-Kaluarachchi et al. (2025) also clearly states that the irreversibility of observed multivariate time-series is the lower bound of EPR.
- Ishihara & Shimazaki (2025) show that entropy flow estimation is a model-based quantity that depends on the state-space kinetic ising model, pairwise coupling, and mean-field approximation.
- Revision:
- Added `4 measurement layers` to `wiki/thermodynamic-grounding-basics.md`.
- `Landauer lower bound`, `organizational-level energy budget`, `irreversibility of coarse-grained neural dynamics`, `model-based entropy flow` were separated into tables as separate items.

### 2. Old `I9` placed mandatory gates that primary literature does not yet support

- Issue:
- `Formulation of an algorithm that performs logical calculations while maintaining EPR > 0`
  - `Virtual Dissipation Protocol`
- `Equivalent to biological brain 20W`
- `Communication: Calculation energy consumption ratio is the same`
- These were listed as if they were the current acceptance conditions.
- Basis:
- None of Bérut et al. (2012), Lynn et al. (2021), de la Fuente et al. (2022), Nartallo-Kaluarachchi et al. (2025), and Ishihara & Shimazaki (2025) derive the above conditions as an acceptance gate for WBE.
- Attwell & Laughlin (2001) give a decomposition of the signaling budget in rodent gray matter, but this is a descriptive budget for biological tissue and is not a pass/fail criterion for digital emulation.
- Revision:
- The old `I9` requirement has been withdrawn, and the thermodynamic index has been specified as `auxiliary log`.
- The following judgment is **inference** based on the fact that the above primary literature does not derive the essential gates of WBE:
- `EPR > 0` Do not make maintenance a condition for acceptance.
- Do not make `20W` or `Communication:Calculation ratio` site-wide KPIs.
- Do not make `Virtual Dissipation Protocol` the design default route

### 3. The old `I9` brought too many theory-dependent claims into the engineering requirements of thermodynamics.

- Issue:
- The previous version had a structure that put `IIT 4.0` and `Unfolding Argument` at the forefront and derived substrate requirement and thermodynamic guarantee from there.
- However, only `lower bound of logical irreversibility` and `time asymmetry of coarse-grained neural dynamics` are directly supported by the primary literature on thermodynamics.
- Revision:
- Replaced `I9` in `tech_roadmap.md` with the `How far should we treat it as a measurement / logging question?` clause instead of the theory adoption clause.
- From an engineering standpoint, I have limited what I am doing now to the separate logs of `wall-plug power`, `FLOPs`, `time irreversibility`, and `model-based entropy flow`.

## Changes Made This Round

- `tech_roadmap.md`
- `last_updated` updated to 2026-03-15
- Completely revised `I9` and withdrawn `Virtual Dissipation Protocol` / `EPR > 0` / `20W KPI` / `Communication: Calculation ratio KPI`
- Set the thermodynamic index to `auxiliary log` and add the minimum log schema that should be kept.
- Replaced the thermodynamics section of the bibliography with the existing primary literature base.
- `wiki/thermodynamic-grounding-basics.md`
- `last_updated` updated to 2026-03-15
- Added `4 measurement layers`
- `Do not make 20W or signaling budget mandatory thresholds` clearly stated in the text
- Added Bérut et al. (2012) and Attwell & Laughlin (2001) to references

## Deferred External-Dependency Tasks

- Establishment of cross-modal irreversibility benchmark
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisites: Comparable public data on at least some EEG/ECoG/fMRI/MEG for the same task and shared pre-processing conditions.
- Completion condition: A public benchmark is in place to compare `coarse-grained condition` `estimator` `lower bound / model-based quantity` `wall-power / FLOPs` with the same schema.

## References

- Bérut A, Arakelyan A, Petrosyan A, et al. Experimental verification of Landauer’s principle linking information and thermodynamics. Nature. 2012.
  - https://doi.org/10.1038/nature10872
- Attwell D, Laughlin SB. An energy budget for signaling in the grey matter of the brain. J Cereb Blood Flow Metab. 2001.
  - https://doi.org/10.1097/00004647-200110000-00001
- Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. Proc Natl Acad Sci U S A. 2021.
  - https://doi.org/10.1073/pnas.2109889118
- de la Fuente LA, Perl YS, Zamberlan F, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. Cereb Cortex. 2023.
  - https://doi.org/10.1093/cercor/bhac177
- Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. Proc Natl Acad Sci U S A. 2025.
  - https://doi.org/10.1073/pnas.2408791122
- Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-66669-w
