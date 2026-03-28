# Site Deepening Audit (2026-03-15, EEG Preprocessing / QC Acceptance Gates)

## Scope

- Main target: `wiki/eeg-preprocessing-and-qc.md`
- Secondary target: `eeg_101.md`

## Why This Page Was Selected

- As of 2026-03-15, the public site was pretty well-organized, including the fact that EEG is not a magical mind-reading technique, the ceiling of source imaging, and the limits of multimodal integration.
- On the other hand, the area surrounding `EEG preprocessing and QC` still relied on the general idea that it was "important," and `Which processing differences stop which kinds of claims` was not an audit gate based on primary literature.
- This weakness is not limited to local pages. L0, L1, consciousness indicators, source imaging, and closed-loop using EEG can all be overstated if the preprocessing and QC floors are vague, even upstream careful discussions.

## Main Critiques

### 1. The old `EEG pretreatment and QC` only enumerated 4 points and was not a condition for acceptance.

- Issue:
- The previous version listed `Reference method`, `Filter`, `Artifact processing`, `Exclusion criteria`.
- However, ``What is the gate to stop the claim?'' and ``What must be left behind in order for the product to be reproducible?'' were not listed.
- Basis:
- EEG-BIDS and BIDS The EEG specification requires specific metadata such as reference, ground, filters, bad channels, electrode coordinates, and event information.
- COBIDAS-MEEG requires transparent reporting of acquisition conditions, filters, artifact handling, bad channel/epoch handling, and exclusion rules.
- Revision:
- Completely revised `wiki/eeg-preprocessing-and-qc.md` and reconfigured it with 5 audit gates: `metadata`, `reference`, `filter`, `artifact`, `retention rate/high frequency`.
- Fixed `What the primary literature now supports` and `Claims to stop when they don't pass` in the table for each.

### 2. Previous version did not separate `Reporting floor` and `Algorithm selection` enough

- Issue:
- In the previous version, there was a description of ``did you use ICA or something like that'', but the floor required by BIDS / COBIDAS and candidate methods such as PREP / Autoreject / ICLabel were mixed.
- As a result, a structure remained that could be misread by readers as `Wrote the famous pipeline name = ensured reproducibility`.
- Basis:
- The PREP pipeline demonstrated the need to handle bad channels before robust rereference, but this is not `all-purpose completion pipeline` nor is it a replacement for reporting floor.
- Autoreject and ICLabel are useful automations, but neither automatically guarantees signal preservation.
- Revision:
- Added a new section called `Reporting floor is metadata, not algorithm name`.
- Added a table for `Candidate methods`, positioned PREP / Autoreject / ICA+ICLabel as `Possible tools`, and listed `Reason for not automatically promoting to standard solution` in parallel.

### 3. The old version had room to read `Deleted many artifacts = good preprocessing`

- Issue:
- The previous version mentioned the necessity of removing artifacts, but was weak in ``If you remove something, you can also remove the signal.'' and ``Reducing accuracy is not necessarily a bad thing.''
- This is especially dangerous on decoding pages. This is because it is easy to misinterpret the high accuracy of artifact-related confounds as improved neural information.
- Basis:
- Kessler et al. (2025) showed that the choice of preprocessing greatly affects decoding performance.
- The 2025 NeuroImage paper `Assessing the impact of artifact correction and artifact rejection on the performance of SVM- and LDA-based decoding of EEG signals` showed that artifact correction does not necessarily improve decoding accuracy.
- Revision:
- Added a new section called `artifact suppression is not always an improvement`.
- Clarified `The pipeline with the highest decoding accuracy is not unconditionally considered the best` as a site rule, and added `raw-clean delta`, `retention rate`, and `sensitivity analysis with alternative pipelines` to the minimum submissions.

### 4. The previous version only weakly dealt with myoelectric pollution in high frequency bands

- Issue:
- The previous version only cited myoelectricity as an example of an artifact, and it was not clear under what conditions high beta/gamma claims should be stopped.
-Therefore, there was room to read it as `high frequency power increased = neural gain`.
- Basis:
- Muthukumaraswamy (2013) summarizes that muscle artifacts overlap widely in the 20-300 Hz range, making neural interpretation of high frequency bands difficult.
- Revision:
- Added independent clause `High beta / gamma is not strongly written without myoelectric audit`.
- Added `high-frequency exception note` to the minimum submission requirements and changed the operation to not raise gamma claim unless it passes EMG / topography / residual check.

### 5. The old `eeg_101.md` mentioned the importance of preprocessing, but it was weak as an acceptance condition.

- Issue:
- Although it was described as `Preprocessing and references change the result` on the public introductory page, it was only heavy enough that readers could read it as `Minor implementation differences`.
- Revision:
- Added `2026-03 Literature Audit: Preprocessing is an acceptance condition, not appearance` to `eeg_101.md`.
- On the public page side, without going into too much detail, we condensed the five acceptance gates and site rules and sent the details to the wiki.

## Changes Made This Round

- `wiki/eeg-preprocessing-and-qc.md`
- Updated front matter
- Completely revised the previous version and added 5 audit gates, positioning of candidate methods, minimum submissions, misreadings to avoid, and references.
- `eeg_101.md`
- `last_updated` updated to 2026-03-15
- Updated front matter highlights / known / unknown
- Added `Preprocessing is not about appearance but acceptance condition` section
- Added PREP, Widmann, Muthukumaraswamy, Kessler to reference links
- `github-wiki-export/eeg-preprocessing-and-qc.md`
- Synchronize public wiki HTML with export regeneration

## Deferred External-Dependency Tasks

- site-wide maintenance of raw / clean paired benchmarks
- Person in charge: AI / maintainer
- Prerequisites: A public benchmark that allows comparison of multiple preprocessing families for the same raw EEG and agreement on task-relevant signal preservation metrics.
- Completion condition: It is possible to compare not only `accuracy` but also `artifact suppression`, `retention`, and `signal preservation` with the same schema.

## References

- BIDS Specification: Electroencephalography
  - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Scientific Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. Nature Neuroscience. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M, Robbins KA. The PREP pipeline: standardized preprocessing for large-scale EEG analysis. Journal of Neuroscience Methods. 2015.
  - https://doi.org/10.1016/j.jneumeth.2015.06.014
- Widmann A, Schröger E, Maess B. Digital filter design for electrophysiological data: a practical approach. Journal of Neuroscience Methods. 2015.
  - https://doi.org/10.1016/j.jneumeth.2014.08.002
- Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. Frontiers in Human Neuroscience. 2013.
  - https://doi.org/10.3389/fnhum.2013.00138
- Cao Y, et al. How Different EEG References Influence Sensor Level Functional Connectivity Graphs. Frontiers in Neuroscience. 2017.
  - https://doi.org/10.3389/fnins.2017.00368
- Jas M, Engemann DA, Bekhti Y, Raimondo F, Gramfort A. Autoreject: automated artifact rejection for MEG and EEG data. NeuroImage. 2017.
  - https://doi.org/10.1016/j.neuroimage.2017.08.030
- Pion-Tonachini L, Kreutz-Delgado K, Makeig S. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. NeuroImage. 2019.
  - https://doi.org/10.1016/j.neuroimage.2019.05.026
- Kessler V, et al. How EEG preprocessing shapes decoding performance. Communications Biology. 2025.
  - https://doi.org/10.1038/s42003-025-08464-3
- Assessing the impact of artifact correction and artifact rejection on the performance of SVM- and LDA-based decoding of EEG signals. NeuroImage. 2025.
  - https://www.sciencedirect.com/science/article/pii/S1053811925003076
