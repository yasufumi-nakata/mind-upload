# Site Deepening Audit (2026-03-14)

## Scope

- Main target: `eeg_101.md`
- Secondary target: `datasets.md`

## Why This Page Was Selected

- These two pages are reference points when reading "How much can EEG contribute to WBE" on the public site.
- If this is ambiguous, the claims of `decode vs emulate`, `verification`, and `roadmap` on other pages will also be easily misunderstood.
- While the existing explanation is generally correct, there was a mix of ``essential requirements,'' ``promising candidate methods,'' and ``future extensions,'' and a structure remained that made it easy to overestimate source imaging.

## Main Critiques

### 1. `eeg_101.md` put the method name too early

- Issue:
- In the existing ESI sections, there were places where Champagne, HBM, ASR, ZapLine-plus, etc. could be read as if they were the current standard solutions.
- However, Michel & Brunet (2019) emphasizes individual MRI, measured electrode positions, conductivity assumptions, and visual inspection, and does not standardize fixed recipes.
- COBIDAS-MEEG also emphasizes transparent reporting and reproducible records, not the adoption of a specific algorithm itself.
- Revision:
- Reorganized into a three-tier evidence chain: `Reporting floor / Geometry floor / Validation floor`.
- Separated `required` and `promising but candidate`, and changed the structure to put the benchmark and error report before the method name.

### 2. The explanation regarding the deep source should have made the conditions for establishment more explicit.

- Issue:
- The existing page correctly added that "the deep part is not impossible at all," but on the other hand, the description of how task-specific it is and how much error remains was weak.
- Seeber et al. (2019) showed potential for deep detection with 256ch HD-EEG and simultaneous DBS recording, but not a study that showed general unique recovery.
- Unnwongse et al. (2023) showed that in direct validation using intracranial stimulation as ground truth, the average localization error reached 14.4–23.4 mm and was strongly dependent on source depth and skull conductivity.
- Even in the systematic review by Mouthaan et al. (2019), source imaging for presurgical epilepsy had a summary sensitivity of 82% and specificity of 53%, and bias remained in all studies.
- Revision:
- Added `Upper limit indicated by actual measurement evidence` section to clarify that "detectable" and "general reconstruction" are different.
- The results of clinical/direct validation were introduced as the upper limit of the benchmark, and the expression was changed to not directly link to WBE.

### 3. `datasets.md` wrote about the "limitations of starter data," but the next step was weak.

- Issue:
- The existing page appropriately positioned EEGMMI / CHB-MIT / Sleep-EDF / TUH EEG as a practice platform for L0-L1.
- However, the question of ``what data should I go to when I want to dig deeper into source imaging?'' was not sufficiently fixed.
- As a result, there was room for readers to misread the data as if they could claim ESI improvement by extending the A-stage starter data.
- Revision:
- Added 3-level data staircase for `A: practice bench / B: reconstruction with anatomical constraints / C: direct validation`.
- Specific examples of stage C include Localize-MI, intracranial stimulation, simultaneous HD-EEG/SEEG, and cohort with postoperative outcomes.

## Changes Made This Round

- `eeg_101.md`
- Completely rewritten ESI section
- Modified the multimodal integration section from focusing on "benefits" to "benefits + additional audit load"
- Added COBIDAS-MEEG, Mouthaan et al. (2019), Jorge et al. (2015), Aydin et al. (2014), Boto et al. (2018) to references.
- `datasets.md`
- Added `If you want to dig deeper into source imaging, divide the data into three stages` section
- Localize-MI, Hao et al. (2025), Mouthaan et al. (2019) added to references

## Deferred External-Dependency Tasks

- Re-auditing future-looking references across public sites
- Person in charge: AI / maintainer
- Prerequisite: Inventory of all page reference links
- Completion condition: zero site-wide citations with unconfirmed DOI or primary source

## References

- Michel CM, Brunet D. EEG source imaging: a practical review of the analysis steps. Front Neurol. 2019.
  - https://doi.org/10.3389/fneur.2019.00325
- Pernet CR, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet CR, et al. Best practices in data analysis and sharing in neuroimaging using MEEG. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Hämäläinen MS, Ilmoniemi RJ. Interpreting magnetic fields of the brain: minimum norm estimates. NeuroImage. 1994.
  - https://doi.org/10.1016/1053-8119(94)90016-7
- Seeber M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nat Commun. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Mouthaan BE, et al. Diagnostic accuracy of interictal source imaging in presurgical epilepsy evaluation: a systematic review from the E-PILEPSY consortium. Clin Neurophysiol. 2019.
  - https://doi.org/10.1016/j.clinph.2018.12.016
- Mikulan E, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. Sci Data. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Hao Y, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Jorge J, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. NeuroImage. 2015.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Aydin U, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. PLoS One. 2014.
  - https://doi.org/10.1371/journal.pone.0093154
- Boto E, et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature. 2018.
  - https://doi.org/10.1038/nature26147
