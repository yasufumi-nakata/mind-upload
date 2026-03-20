# Site Deepening Audit (2026-03-21, Myelin Route Card)

## Target

- Primary: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Propagated rule changes: `verification.md`, `wbe_101.md`, `index.md`

## Why this topic was selected

- The site already treated `myelin / oligodendrocyte support` as a real hidden-state family, but the operational rule was still weaker than for sleep replay, phospho-signaling, or multimodal fusion.
- In practice, a reader could still compress at least five different inferential objects into one bucket called `myelin evidence`:
  - activity-dependent oligodendrogenesis for learning
  - node / internode / periaxonal timing-state control
  - developmental myelination as a brake on adult plasticity
  - remyelination-to-function recovery
  - human macro-myelin proxy routes
- That compression is scientifically unsafe because the cited literature does not show that these objects share one claim ceiling.

## Evidence-backed critique

### 1. Learning-dependent myelination and timing-state control are not the same inferential object

- Problem:
  - The site already said that myelin matters, but it still risked reading that family mainly as `delay / support`.
- Evidence:
  - Gibson et al. (2014) showed activity-dependent oligodendrogenesis and adaptive myelination.
  - McKenzie et al. (2014) showed that active central myelination is required for motor-skill learning.
  - Seidl et al. (2015), Dutta et al. (2018), Cohen et al. (2020), Micheva et al. (2021), and Dubey et al. (2022) instead focused on conduction timing, nodal / periaxonal structure, and synchronization.
- Critique:
  - Therefore `myelin matters for learning` and `myelin fixes timing-state` cannot be treated as one evidence class.

### 2. Myelin is not only a speed variable; it can also be a plasticity gate

- Problem:
  - The earlier wording let `more myelin = faster timing` dominate the interpretation.
- Evidence:
  - Xin et al. (2024) showed that blocking adolescent oligodendrogenesis preserved adult visual-cortex plasticity that is normally restricted, supporting developmental myelination as a functional brake on neuronal plasticity.
- Critique:
  - Therefore myelin evidence cannot be reduced to `conduction speed`. It also changes which plastic transitions remain available.

### 3. Functional recovery after remyelination is not the same thing as complete restoration of healthy myelin-state

- Problem:
  - Without a route-card field for recovery boundary, functional rescue can be overread as `state restoration completed`.
- Evidence:
  - Della-Flora Nunes et al. (2025) showed that visual neuronal function can recover even when oligodendrocyte and myelin restoration to healthy levels remains incomplete.
- Critique:
  - Therefore `function came back` and `healthy myelin-state was fully reconstructed` are different claims and must be logged separately.

### 4. Human myelin observability is still proxy-limited

- Problem:
  - The site already labeled human myelin routes as macro proxies, but it did not yet force the reader to say which human proxy class they were using.
- Evidence:
  - van Blooijs et al. (2023) provided tract-scale transmission-speed evidence in humans, not per-axon ground truth.
  - Baadsvik et al. (2024) demonstrated in vivo myelin-bilayer mapping, but in two healthy volunteers on specialized hardware.
  - Genc et al. (2025) aligned cortical microstructure MRI with oligodendrocyte cell-type expression trajectories and explicitly kept histopathological confirmation as future work.
- Critique:
  - Therefore current human myelin evidence remains a macro timing or MRI proxy class, not direct whole-brain timing-state recovery.

## Changes executed

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - Updated `last_updated` to `2026-03-21`.
  - Expanded the myelin section so it now separates learning, timing-state, plasticity-brake, remyelination, and human-proxy logic.
  - Added `#myelin-route-card` with explicit fields:
    - claim family
    - biological regime
    - direct observable / structural unit
    - functional target
    - recovery / completeness boundary
    - human route / measurement model
    - abstention boundary
  - Added new primary references for Xin et al. (2024), Della-Flora Nunes et al. (2025), Genc et al. (2025), and the timing-state literature cluster.
- `verification.md`
  - Added a page-highlight bullet making the myelin route card a public verification rule.
  - Added a maintenance-state addendum that points readers to the new route card and blocks claim compression at submission time.
- `wbe_101.md`
  - Added a page-highlight bullet clarifying that `myelin evidence` is not one row.
  - Added a front-door note so entry-level readers do not silently promote human myelin maps or remyelination papers to timing-complete claims.
- `index.md`
  - Added a landing-page stop rule that blocks reading myelin as one solved timing variable.

## External dependency kept separate

- Same-subject benchmark for human myelin route calibration
  - Owner: external MRI / electrophysiology benchmark designers
  - Preconditions: same-subject acquisition combining human tract-speed or timing-sensitive physiology with macro-myelin MRI and an externally validated timing target
  - Done when: the site can point to a public benchmark that calibrates which human myelin proxy actually reduces which timing or plasticity error term

## References

1. Gibson EM, Purger D, Mount CW, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. *Science*. 2014;344(6183):1252304.
   - https://doi.org/10.1126/science.1252304
2. McKenzie IA, Ohayon D, Li H, et al. Motor skill learning requires active central myelination. *Science*. 2014;346(6207):318-322.
   - https://doi.org/10.1126/science.1254960
3. Seidl AH, Rubel EW, Barría A. Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. *Nature Communications*. 2015;6:8073.
   - https://doi.org/10.1038/ncomms9073
4. Dutta DJ, Woo DH, Lee PR, et al. Regulation of myelin structure and conduction velocity by perinodal astrocytes. *Proceedings of the National Academy of Sciences USA*. 2018;115(46):11832-11837.
   - https://doi.org/10.1073/pnas.1811013115
5. Cohen CCH, Popovic MA, Klooster J, et al. Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. *Cell*. 2020;180(2):311-322.e15.
   - https://doi.org/10.1016/j.cell.2019.11.039
6. Micheva KD, Kiraly M, Perez MM, Madison DV. Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. *Cerebral Cortex*. 2021;31(7):3374-3392.
   - https://doi.org/10.1093/cercor/bhab018
7. Dubey S, Kuschmitz S, Mezey SE, et al. Myelination synchronizes cortical oscillations by consolidating parvalbumin-mediated phasic inhibition. *eLife*. 2022;11:e73827.
   - https://doi.org/10.7554/eLife.73827
8. van Blooijs D, de Haan AM, Renaud S, et al. Developmental trajectory of transmission speed in the human brain. *Nature Neuroscience*. 2023;26:828-838.
   - https://doi.org/10.1038/s41593-023-01272-0
9. Xin W, Kaneko M, Roth RH, et al. Oligodendrocytes and myelin limit neuronal plasticity in visual cortex. *Nature*. 2024;633:856-863.
   - https://doi.org/10.1038/s41586-024-07853-8
10. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
11. Della-Flora Nunes G, Osso LA, Haynes JA, et al. Incomplete remyelination via therapeutically enhanced oligodendrogenesis is sufficient to recover visual cortical function. *Nature Communications*. 2025;16:732.
   - https://doi.org/10.1038/s41467-025-56092-6
12. Genc S, Ball G, Chamberland M, et al. MRI signatures of cortical microstructure in human development align with oligodendrocyte cell-type expression. *Nature Communications*. 2025;16:3317.
   - https://doi.org/10.1038/s41467-025-58604-w
