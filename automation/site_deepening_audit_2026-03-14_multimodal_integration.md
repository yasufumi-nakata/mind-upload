# Site Deepening Audit (2026-03-14, EEG Multimodal Integration)

## Scope

- Main target: `wiki/multimodal-integration-basics.md`
- Reference page: `eeg_101.md`

## Why This Page Was Selected

- `eeg_101.md` itself was quite specific as of 2026-03-14, but the `wiki/multimodal-integration-basics.md` that follows from there remained a general explanation as of 2026-03-06.
- The current wiki has written about ``which combination complements what,'' but it lacks primary literature, conditions for success, conditions for failure, and external validation.
- Therefore, the `EEG alone is not enough → So what should we add?` direction on the public site looked a little optimistic from a scientific perspective.

## Main Critiques

### 1. The current page stopped at the explanation of "complementary relationships" and did not audit the conditions for the integration to take place.

- Issue:
- I listed `EEG + fMRI`, `EEG + MEG`, `EEG + MRI`, `EEG + ECoG`, but I did not write which one of the shared clock, coordinate alignment, forward model, conductivity assumption, or artifact management is required.
- As a result, the structure was easy to read as ``increasing the number of modalities will make it stronger.''
- Basis:
- COBIDAS-MEEG (Pernet et al., 2020) organizes that reusability will be lost if acquisition, analysis, reporting, and sharing are not specified in MEEG research.
- EEG-BIDS (Pernet et al., 2019) also shows that keeping raw data and metadata structured is itself a prerequisite for reproducibility.
- Revision:
- The public page was reconfigured with `5 audit gates` and synchronization, geometry, noise/field, external validation, and state coverage were fixed first.

### 2. EEG+fMRI explanation was less strict on artifact and safety

- Issue:
- The current page was limited to the general theory of `temporal variation and spatial distribution complement each other` and overlooked the practical difficulties of simultaneous measurement.
- Basis:
- Jorge et al. (2015, doi:10.1016/j.neuroimage.2014.10.055) showed that artifacts and safety issues become larger at temperatures above 3T.
- Jorge et al. (2015, doi:10.1016/j.neuroimage.2015.07.020) showed that detecting and reducing head motion artifacts is a central challenge at 7T.
- Wirsich et al. (2021) demonstrated the reproducibility of a simultaneous EEG-fMRI connectome over 1.5T to 7T, which is based on proper setup and cleaning.
- Revision:
- `EEG + fMRI` has been rewritten as "route where artifacts and safety controls increase as the magnetic field increases" instead of "spatiotemporal complementation".

### 3. EEG+MEG improvement was written without physical model

- Issue:
- The current page only wrote `Complement the sensitivity distribution`, but I missed the point that the gain depends on skull conductivity calibration and realistic head model.
- Basis:
- Aydin et al. (2014) showed that EEG/MEG integration with a calibrated realistic volume conductor model can improve source reconstruction.
- Conversely, it is not possible to make an equivalent claim just by using modality stacking.
- Revision:
- Redefined `EEG + MEG` as a route that works with improvements to the physical model.

### 4. Integration with invasive records was only described as ``high SNR can be obtained,'' and its position as a validation route was weak.

- Issue:
- The current page introduced ECoG/invasive measurement as a local measurement with high SNR, but in the context of the public site, the role of `external validation and calibration` is more important.
- Basis:
- Zhang et al. (2006) verified cortical potential imaging using simultaneous scalp EEG/ECoG.
- Seeber et al. (2019) showed subcortical detectability with simultaneous DBS + 256ch scalp EEG.
- However, both are coverage-limited and do not provide whole-brain ground truth.
- Revision:
- Rewritten `EEG + invasive record` as `coverage-limited validation route` instead of gold standard.

### 5. Even if OPM-MEG could be written as a promising device for the future, the current prerequisites were missing.

- Issue:
- While the current page reads OPM-MEG as a positive extension, it misses the point that system engineering with background field nulling and motion correction is essential.
- Basis:
- Boto et al. (2018) demonstrated the potential of wearable OPM-MEG, but also the importance of a shielded environment and system-level engineering.
- Revision:
- Clarified `Not a simple mobile replacement device`.

## Changes Made This Round

- `wiki/multimodal-integration-basics.md`
- Updated front matter to focus on technology and natural sciences
- Deleted general explanations and reorganized to `Five Audit Gates` based on primary literature
- Evidence-based comparison of `EEG + MRI`, `EEG + MEG`, `EEG + fMRI`, `EEG + Invasive Recording`, `OPM-MEG`
- Specify the rules for rereading on public sites
- Newly established reference bibliography centered on primary documents

## Deferred External-Dependency Tasks

- Continuous monitoring of 2024-2026 validation literature of simultaneous scalp EEG + intracranial recording
- Person in charge: AI / maintainer
- Prerequisite: Continuous publication of new peer-reviewed validation papers
- Completion condition: The generalization limitations of scalp-to-intracranial mapping are additionally organized in peer-reviewed literature rather than preprints.

## References

- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Jorge J, Grouiller F, Ipek O, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. NeuroImage. 2015.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Jorge J, Grouiller F, Gruetter R, et al. Towards high-quality simultaneous EEG-fMRI at 7 T: Detection and reduction of EEG artifacts due to head motion. NeuroImage. 2015.
  - https://doi.org/10.1016/j.neuroimage.2015.07.020
- Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. NeuroImage. 2021.
  - https://doi.org/10.1016/j.neuroimage.2021.117864
- Aydin U, Vorwerk J, Kupper P, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. PLoS ONE. 2014.
  - https://doi.org/10.1371/journal.pone.0093154
- Zhang Y, Ding L, van Drongelen W, et al. A cortical potential imaging study from simultaneous extra- and intracranial electrical recordings by means of the finite element method. NeuroImage. 2006.
  - https://doi.org/10.1016/j.neuroimage.2006.02.027
- Seeber M, Cantonas LM, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nat Commun. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Boto E, Holmes N, Leggett J, et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature. 2018.
  - https://doi.org/10.1038/nature26147
