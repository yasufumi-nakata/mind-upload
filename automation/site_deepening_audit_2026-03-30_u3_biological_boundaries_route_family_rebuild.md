# Site Deepening Audit (2026-03-30, U3 biological-boundary route-family rebuild)

## Scope

- Primary target: `research_harvest_50.md`
- Investigation scope: technical and natural-science claims only
- Explicitly excluded: philosophy, law, institutional strategy

## Why This Topic Was Chosen

- The site had already accumulated stronger route-splitting rules in several front-door pages, especially for measurement ceilings and human proxy classes.
- However, the `U3: Biological boundaries` section in the research harvest still compressed too many non-neuronal mechanisms into one broad `support` framing.
- That compression is technically dangerous because it makes distinct controller objects sound exchangeable:
  - astrocytic state
  - pericyte / BBB / neurovascular control
  - clearance / immune support
  - bounded living-human macro proxies for those support layers

## Main Conclusion

- `Biological boundary evidence` is not one common bucket.
- The current primary literature requires at least a route-family reading:
  - astrocyte ensemble / representation routes
  - pericyte-neurovascular-BBB controller routes
  - clearance / immune support routes
  - living-human macro proxy routes
- The previous U3 wording was too permissive because it let those families inherit one another's inferential strength.

## Evidence-Based Critique

### 1. Astrocyte papers do not define one common maintenance controller

- Problem:
  - The earlier U3 framing let astrocyte-related results read like one accumulating line of evidence for a generic glial maintenance requirement.
- Why this is technically weak:
  - The primary papers now constrain different controller objects and time scales.
  - They do not justify a single interchangeable `astrocyte support` row.
- Primary evidence:
  - Dewa et al. (2025) showed an astrocytic ensemble acting as a multiday trace that stabilizes memory.
  - Bukalo et al. (2026) showed astrocyte-dependent amygdala representations supporting memory.
  - Xin et al. (2025) showed neuron-astrocyte coupling in lateral habenula linked to depressive-like behavior.
- Criticism:
  - These are not the same direct observable.
  - They differ in anatomical locus, task class, and implied controller identity.
  - Therefore `astrocyte evidence exists` is too coarse to support a minimum biological-subject requirement without route naming.

### 2. Pericyte / neurovascular / BBB papers do not collapse to one vascular scalar

- Problem:
  - The earlier wording grouped neurovascular coupling, BBB modulation, and pericyte findings as if they were one maintenance-side variable.
- Why this is technically weak:
  - The literature constrains separable mechanisms:
    - neuronal phenotype support and capillary regulation
    - acute neurovascular coupling failure after pericyte ablation
    - pericyte-derived memory-support signaling
    - activity-linked BBB modulation
    - capillary-diameter control with behavioral consequences
- Primary evidence:
  - Bell et al. (2010)
  - Kisler et al. (2020)
  - Pandey et al. (2023)
  - Swissa et al. (2024)
  - Mai-Morente et al. (2025)
- Criticism:
  - A reader must now ask which controller object is being claimed:
    - perfusion support
    - barrier state
    - capillary control
    - pericyte-derived molecular memory support
  - Without that split, the evidence bank overstates how close current measurements are to a same-subject biological equivalence test.

### 3. Clearance / immune support must be separated from living-human proxy routes

- Problem:
  - The older U3 section let animal clearance findings and human macro imaging or model-based evidence sit too near each other.
- Why this is technically weak:
  - Those papers do not share the same direct observable or claim ceiling.
  - Animal manipulations can identify controller-side causal roles that current human routes cannot yet resolve locally.
- Primary evidence:
  - Kim et al. (2025) identified a meningeal-lymphatics / microglia axis regulating synaptic physiology.
  - Jiang-Xie et al. (2024) linked neuronal dynamics to CSF perfusion and brain clearance.
  - Murdock et al. (2024) showed multisensory gamma stimulation promoting glymphatic amyloid clearance.
  - Padrela et al. (2025) measured BBB water permeability across the adult lifespan.
  - Chung et al. (2025) quantified tracer-specific molecular BBB permeability with PET modeling.
  - Hirschler et al. (2025) measured region-specific CSF mobility in humans.
  - Dagum et al. (2026) reported model-based overnight amyloid-beta and tau efflux from brain to plasma in humans.
- Criticism:
  - `human support-state proxy exists` must not be read as `human local controller readout exists`.
  - The route families differ in model burden, spatial scale, perturbation dependence, and biological abstention boundary.

### 4. Archive pages must preserve route discipline, not undo it

- Problem:
  - Even if front-door pages become more rigorous, archive or harvest pages can silently reintroduce compression by using broad umbrella wording.
- Why this matters:
  - Readers often use evidence-bank pages to infer what counts as already established.
  - If the archive collapses route families, the site's more careful front-door distinctions lose force.
- Criticism:
  - `research_harvest_50.md` should therefore be stricter than overview pages, not looser.
  - The evidence bank must force naming of:
    - route family
    - direct observable
    - human ceiling

## Changes Executed In This Session

- `research_harvest_50.md`
  - Rewrote `What has some traction now` so U3 is organized by route families rather than by a generic support bucket.
  - Replaced mixed placeholder-style references with controller-side primary studies and bounded human proxy studies.
  - Added a `2026-03-30 deepening` note that explains why astrocyte, pericyte / BBB, clearance / immune, and human macro proxies must not be compressed.
  - Rewrote `What still needs research` so the unresolved section names the missing living-human routes explicitly.
  - Rebuilt the prior-study list into `17 route-family anchors` rather than a mixed list of heterogeneous entries.

## Misreadings This Change Intentionally Stops

- `astrocyte evidence exists` = one common controller object
- `vascular support evidence exists` = one scalar maintenance variable
- `clearance evidence exists` = same-subject human local controller observability exists
- `human BBB / CSF proxy exists` = synapse-resolved support-state readout exists
- `archive page can use rough wording because the front door is already careful`

## External Dependency Tasks

- None.
  - This session only required literature verification, repo edits, build validation, commit, and push.

## References

1. Dewa Y, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
2. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
3. Xin et al. Neuron-astrocyte coupling in lateral habenula mediates depressive-like behaviors. *Cell*. 2025.
   - https://doi.org/10.1016/j.cell.2025.04.010
4. Bell RD, Winkler EA, Sagare AP, et al. Pericytes control key neurovascular functions and neuronal phenotype in the adult brain and during brain aging. *Neuron*. 2010;68(3):409-427.
   - https://doi.org/10.1016/j.neuron.2010.09.043
5. Kisler K, Nikolakopoulou AM, Sweeney MD, et al. Acute ablation of cortical pericytes leads to rapid neurovascular uncoupling. *Frontiers in Cellular Neuroscience*. 2020;14:27.
   - https://doi.org/10.3389/fncel.2020.00027
6. Pandey R, et al. Neuronal activity drives IGF2 expression from pericytes to form long-term memory. *Neuron*. 2023.
   - https://doi.org/10.1016/j.neuron.2023.08.030
7. Swissa E, et al. Cortical plasticity is associated with blood-brain barrier modulation. *eLife*. 2024;12:RP89611.
   - https://doi.org/10.7554/eLife.89611
8. Mai-Morente N, et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nature Communications*. 2025;16:61312.
   - https://doi.org/10.1038/s41467-025-61312-0
9. Jiang-Xie LF, et al. Neuronal dynamics direct cerebrospinal fluid perfusion and brain clearance. *Nature*. 2024.
   - https://doi.org/10.1038/s41586-024-07108-6
10. Murdock MH, et al. Multisensory gamma stimulation promotes glymphatic clearance of amyloid. *Nature*. 2024.
    - https://doi.org/10.1038/s41586-024-07132-6
11. Kim et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
    - https://doi.org/10.1016/j.cell.2025.02.022
12. Padrela N, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025;148:112-121.
    - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
13. Chung et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:58356.
    - https://doi.org/10.1038/s41467-025-58356-7
14. Hirschler L, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
    - https://doi.org/10.1038/s41593-025-02073-3
15. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:68374.
    - https://doi.org/10.1038/s41467-026-68374-8
