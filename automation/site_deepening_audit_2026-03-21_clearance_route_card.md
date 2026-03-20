# Site Deepening Audit (2026-03-21, Clearance / Immune Route Card)

## Target

- Primary: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Propagated rule changes: `verification.md`, `wbe_101.md`, `index.md`

## Why this topic was selected

- The site already treated `clearance / immune support` as a real maintenance-state family, and it already blocked the simplistic reading that this is mere `cleanup`.
- However, compared with myelin, sleep replay, phospho-signaling, or multimodal fusion, the site still lacked an explicit route card for this topic.
- In practice, a reader could still compress at least five different inferential objects into one bucket:
  - meningeal-lymphatic anatomy / drainage route
  - disease or ageing-linked lymphatic dysfunction
  - microglia-mediated synaptic-physiology mechanism
  - human CSF-mobility MRI
  - model-based human biomarker efflux
- That compression is scientifically unsafe because the cited primary literature does not show that these objects share one claim ceiling.

## Evidence-backed critique

### 1. Drainage anatomy is not the same claim as immune-effector control

- Problem:
  - The current site correctly cited lymphatic anatomy papers, but could still let readers overread anatomy as if the responsible immune controller had been identified.
- Evidence:
  - Louveau et al. (2015) established structural and functional CNS lymphatic vessels.
  - Ahn et al. (2019) localized skull-base meningeal lymphatic vessels as key CSF-drainage routes.
- Critique:
  - Therefore `a drainage route exists` is not yet `the synapse- or cell-specific maintenance controller is known`.

### 2. Disease-modulation papers are not the same object as healthy support-state measurement

- Problem:
  - Without an explicit route-card field, lymphatic dysfunction in ageing / AD-like contexts can be overread as if it already supplied a general observability route.
- Evidence:
  - Da Mesquita et al. (2021) showed that impaired meningeal lymphatics worsen microglial inflammatory response and anti-Aβ immunotherapy outcome in AD-model mice.
- Critique:
  - Therefore disease-modulation evidence strengthens causal relevance, but it is not the same as a direct healthy-human state readout.

### 3. Microglia-related synaptic control is not the same object as CSF mobility or protein efflux

- Problem:
  - The existing text grouped microglia and clearance together, but it still did not force the reader to say whether the paper was about synaptic physiology, mobility, or biomarker transport.
- Evidence:
  - Kim et al. (2025) showed that the meningeal-lymphatics-microglia axis regulates synaptic physiology.
  - Hirschler et al. (2025) measured region-specific CSF mobility with MRI in humans.
  - Dagum et al. (2026) inferred glymphatic-route amyloid-beta / tau transport from brain to plasma using a wearable plus compartment modeling.
- Critique:
  - Therefore `microglia-synapse mechanism`, `CSF mobility`, and `brain-to-plasma biomarker efflux` cannot be merged into one generic `clearance signal`.

### 4. Physiology-linked clearance dynamics are not direct controller identification

- Problem:
  - Sleep-linked or physiology-linked clearance results can be overread as if they had already localized the responsible maintenance controller.
- Evidence:
  - Hablitz et al. (2019) showed that glymphatic influx correlates with delta power and heart rate in mice under anesthesia.
  - Eide & Ringstad (2021) showed that one night of sleep deprivation impairs molecular clearance from the human brain.
- Critique:
  - Therefore state dependence and causal support for clearance dynamics are important, but they are still different from direct measurement of a local immune or synaptic controller.

## Changes executed

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - Added a new highlight and unknown-point entry so the route-card need is visible in the header.
  - Added `#clearance-route-card` with explicit fields:
    - claim family
    - biological regime
    - direct observable / route object
    - driver / perturbation route
    - human measurement / model burden
    - functional target
    - abstention boundary
  - Added primary references for Hablitz et al. (2019) and Da Mesquita et al. (2021).
- `verification.md`
  - Added a page-highlight bullet making the clearance / immune route card part of the public verification rule.
  - Added a maintenance-state addendum that blocks compression of anatomy, synaptic mechanism, mobility MRI, and biomarker-efflux modeling into one evidence class.
- `wbe_101.md`
  - Added an entry-level highlight clarifying that `clearance evidence` is not one row.
  - Rewrote the front-door note so readers do not silently promote CSF mobility or biomarker-efflux papers to local immune-controller readout.
- `index.md`
  - Added a landing-page highlight separating clearance evidence families.
  - Updated the clearance note to point directly to the new route card.

## External dependency kept separate

- Same-subject benchmark for human clearance-route calibration
  - Owner: external MRI / sleep / neuroimmune benchmark designers
  - Preconditions: same-subject acquisition linking human CSF-mobility MRI, biomarker-efflux modeling, sleep / physiology logs, and an external biological target
  - Done when: the site can point to a public benchmark that calibrates which human clearance proxy actually reduces which maintenance-state error term

## References

1. Louveau A, Smirnov I, Keyes TJ, et al. Structural and functional features of central nervous system lymphatic vessels. *Nature*. 2015;523:337-341.
   - https://doi.org/10.1038/nature14432
2. Ahn JH, Cho H, Kim J-H, et al. Meningeal lymphatic vessels at the skull base drain cerebrospinal fluid. *Nature*. 2019;572:62-66.
   - https://doi.org/10.1038/s41586-019-1419-5
3. Hablitz LM, Vinitsky HS, Sun Q, et al. Increased glymphatic influx is correlated with high EEG delta power and low heart rate in mice under anesthesia. *Science Advances*. 2019;5(2):eaav5447.
   - https://doi.org/10.1126/sciadv.aav5447
4. Eide PK, Ringstad G. Sleep deprivation impairs molecular clearance from the human brain. *Brain*. 2021;144(3):863-874.
   - https://doi.org/10.1093/brain/awaa443
5. Da Mesquita S, Papadopoulos Z, Dykstra T, et al. Meningeal lymphatics affect microglia responses and anti-Aβ immunotherapy. *Nature*. 2021;593:255-260.
   - https://doi.org/10.1038/s41586-021-03489-0
6. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025;188(8):2129-2148.e21.
   - https://doi.org/10.1016/j.cell.2025.02.022
7. Hirschler L, Runderkamp BA, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28(11):2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
8. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
