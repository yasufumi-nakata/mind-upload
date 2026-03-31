# Site Deepening Audit (2026-03-31, FAQ post-transcriptional RNA front-door split)

## Scope

- Primary target: `faq.md`
- Secondary target: `summary_booklet.md` via regeneration from updated front matter

## Why This Topic Was Chosen

- The site already had a strong `post-transcriptional RNA route card` in the wiki and a stronger front-door split on `index.md`.
- However, the central FAQ answer `Q2c` still opened the RNA section with a sentence that was easy to skim as one generic `RNA layer`.
- That wording was technically weaker than the rest of the site because the cited primary literature does not support treating
  - splice-isoform control
  - splice-dependent transsynaptic receptor-balance control
  - m6A-dependent translation
  - m6A-dependent degradation
  - RNA editing
  - atlas / observability ceiling
  as one interchangeable inferential object.

## Evidence-Based Critique

### 1. The FAQ front door still compressed several RNA controllers into one short clause

- Problem:
  - `faq.md` already told readers that post-transcriptional RNA-state remained another layer.
  - But the first sentence still grouped the cited papers mainly under `alternative splicing, m6A-dependent translation / degradation, and RNA-editing ratio`.
- Why this is technically weak:
  - At the FAQ front door, many readers skim only the first sentence of each family.
  - If that first sentence is too coarse, later caveats about human ceiling are easy to miss.
  - The site's own rule is to stop route compression early, not only in the deeper wiki pages.

### 2. The cited splice papers do not constrain the same downstream object

- Primary evidence:
  - Wang et al. (2015, DOI `10.1038/nn.4069`) is a neuron-specific LSD1 splice-isoform route whose downstream object is transcriptional elongation control.
  - Dai et al. (2019, DOI `10.1016/j.neuron.2019.03.032`) is a presynaptic neurexin splice route whose downstream object is postsynaptic NMDA versus AMPA receptor balance and contextual memory.
- Critique:
  - Therefore `alternative splicing` is still too coarse unless the route says which controller and which downstream target changed.
  - One splice paper is not a generic readout of the current whole-brain RNA controller.

### 3. The m6A papers support opposite RNA-fate roles, not one common m6A knob

- Primary evidence:
  - Shi et al. (2018, DOI `10.1038/s41586-018-0666-1`) supports stimulus-dependent translation through YTHDF1.
  - Li et al. (2025, DOI `10.1002/advs.202514926`) supports YTHDF2-mediated m6A degradation as a different controller whose inhibition enhances protein synthesis and hippocampus-dependent memory.
  - Peterson et al. (2025, DOI `10.1126/scisignal.adr1442`) is different again because it is an ADAR2-mediated RNA-editing route for homeostatic AMPAR composition.
- Critique:
  - `m6A-dependent translation / degradation` is directionally correct, but still too compressed for a front-door sentence.
  - Translation, degradation, and editing are different controller families with different direct observables and different claim ceilings.

### 4. The human ceiling remains an atlas ceiling, not a living-human whole-brain route

- Primary evidence:
  - Joglekar et al. (2024, DOI `10.1038/s41593-024-01616-4`) provides a single-cell long-read atlas showing specialized splicing patterns across mouse and human brain.
- Inference from sources and search:
  - I checked the current primary-literature landscape on the web on 2026-03-31 and did not find a comparable living-human in vivo whole-brain route that directly reads isoform choice, m6A-reader engagement, or RNA-editing ratios.
- Critique:
  - That means the FAQ front door should already warn readers that the cited RNA papers are route-family evidence plus an atlas ceiling, not a current human whole-brain observability solution.

## Changes Executed In This Session

- `faq.md`
  - Added a new `page_highlights` bullet that states explicitly that post-transcriptional RNA evidence is not one class at the FAQ front door.
  - Rewrote the opening RNA clause in `Q2c` so it now separates
    - Wang as a splice-isoform route for chromatin / transcriptional control
    - Dai as a splice-dependent transsynaptic receptor-balance route
    - Shi versus Li as different m6A translation-versus-degradation routes
    - Peterson as an RNA-editing route for homeostatic AMPAR composition
  - Tightened the stop line so gene-level abundance is no longer the only contrast; the route-family split is now visible in the first sentence.
- `summary_booklet.md`
  - Regenerated from the updated FAQ front matter so the booklet reflects the new front-door stop line.

## External Dependency Tasks

- None.
  - This session only required repository inspection, literature review, local file edits, regeneration, verification, and Git operations.

## References

1. Wang J, Telese F, Tan Y, et al. LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. *Nature Neuroscience*. 2015.
   - https://doi.org/10.1038/nn.4069
2. Dai J, Aoto J, Südhof TC. Alternative splicing of presynaptic neurexins differentially controls postsynaptic NMDA and AMPA receptor responses. *Neuron*. 2019.
   - https://doi.org/10.1016/j.neuron.2019.03.032
3. Shi H, Zhang X, Weng Y-L, et al. m6A facilitates hippocampus-dependent learning and memory through YTHDF1. *Nature*. 2018.
   - https://doi.org/10.1038/s41586-018-0666-1
4. Li Y, Zhu M, Li X, et al. Enhanced Protein Synthesis and Hippocampus-Dependent Memory via Inhibition of YTHDF2-Mediated m6A mRNA Degradation. *Advanced Science*. 2025.
   - https://doi.org/10.1002/advs.202514926
5. Peterson LN, Kasper JM, Allgaier JA, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025.
   - https://doi.org/10.1126/scisignal.adr1442
6. Joglekar A, Prjibelski A, Mahfouz A, et al. Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-024-01616-4
