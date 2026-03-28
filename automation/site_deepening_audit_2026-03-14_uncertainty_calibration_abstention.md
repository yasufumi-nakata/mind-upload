# Site Deepening Audit (2026-03-14, Uncertainty / Calibration / Abstention)

## Scope

- Main target: `wiki/uncertainty-confidence-and-abstention.md`

## Why This Page Was Selected

- This page is a supplementary page referenced by `eeg_101.md`, `verification.md`, `wiki/observation-to-estimation.md`, `wiki/closed-loop-latency-jitter-and-safety-stops.md`, and supports the strength of the overall site's claims.
- However, while the previous version as of 2026-03-14 touched on the general theory of `Interval is more important than point estimation`, the practical core of `confidence ≠ calibration`, `Abstention is a trade-off for coverage`, and `Uncertainty accounting required for source imaging / EEG classification / online BCI is different` was not fixed.
- This weakness makes the entire public site difficult to read. This is because the posterior width of source imaging, the calibration error of EEG classification, and the recalibration load of closed-loop BCI were read as almost the same in the previous edition, even though they cannot be summarized under the same word "uncertainty."

## Main Critiques

### 1. The old version did not separate `confidence` and `calibration`

- Issue:
- The previous version was useful as an introductory explanation of `confidence interval / confidence interval`, but it did not fix the extent to which a single number in classification score or posterior could be read as a practical reliability.
-Therefore, there was still room for misreading softmax and decoder score as `probability of winning`.
- Basis:
- Duan et al. (2023) treats uncertainty estimation and confidence calibration separately in motor imagery EEG decoding.
- Hu et al. (2024) and Shafiezadeh et al. (2024) also evaluate calibration improvement itself in EEG seizure classification/forecasting.
- Revision:
- Added a new `Do not mix confidence, interval, calibration, abstention` section and fixed the role differences of point estimation, interval, confidence, calibration, and abstention in a table.
- Specified the site rule `Do not consider softmax or posterior as calibrated probability`.

### 2. The old version of `Abstain` was too focused on safety, and I couldn't see any replacement with coverage.

- Issue:
- The old version stopped at the explanation ``It's safer not to force yourself to answer when your confidence is low.''
- But in practice, abstention involves `how much you reduced errors` as well as `how much you gave up on output`.
- Basis:
- Ganeshkumar et al. (2017) lowered the false prediction rate by adding a reject option to the EEG motor imagery BCI, but at the same time it reduced coverage.
- Segal et al. (2023) uses risk-controlling prediction calibration to suppress false alarm rates in seizure prediction. This is a threshold and false alarm cost design issue, not a safety issue.
- Revision:
- Replaced with the clause ``abstaining is not ``because it seems safe'' but disclosure of coverage and risk``.
- Added to the site rule that the coverage-risk curve should be issued together with neither `accuracy` nor `abstention rate`.

### 3. The previous version used the same uncertainty concept for source imaging, EEG classification, and closed-loop BCI.

- Issue:
- Source imaging uncertainty strongly depends on head geometry, conductivity, solver family, and external validation.
- On the other hand, EEG classification is dominated by subject shift and calibration error, and online BCI is dominated by drift and recalibration burden.
- The previous version did not separate this difference well enough.
- Basis:
- Vorwerk et al. (2019), Rimpiläinen et al. (2019), and Feng et al. (2025) treat the head model and conductivity uncertainty as the main body on the source imaging side.
- Wilson et al. (2025) demonstrate the utility of long-term intracortical BCI, including recalibration loads.
- Wairagkar et al. (2025) assumes a design that returns silence for non-speech even with low-latency voice neuroprosthesis.
- Revision:
- A new section has been added to separate the required indicators for source imaging, offline EEG classification, rare event prediction, and online BCI.
- We separated observation noise, model/geometry, distribution shift, and operational drift as `Uncertainty comes from four layers`.

### 4. The previous version had too little evidence as a page based on primary literature

- Issue:
- The previous edition did not have a bibliography section, making it difficult for readers to follow what supports this organization.
- Revision:
- Added 10 primary documents that directly address source imaging, EEG calibration, seizure forecasting, reject option, and online BCI recalibration.

## Changes Made This Round

- `wiki/uncertainty-confidence-and-abstention.md`
- Updated front matter to focus on technology and natural sciences
- Newly added `Four audit gates`, `Difference in the role of confidence / calibration / abstention`, `Required indicators for each issue`, `Reality shown by primary literature`, `site rule`, `References`
- Updated title from `Uncertainty, Confidence Intervals and Abstentions` to `Uncertainty, Calibration and Abstentions`

## Deferred External-Dependency Tasks

- Unification of site-wide calibration metrics
- Person in charge: AI / maintainer
- Prerequisite: Decide on the standard submissions for each assignment among `ECE / Brier / NLL / interval coverage / coverage-risk curve`
- Completion condition: Standard indicators for each L0 / L1 / L3 must be aligned throughout `verification.md` and related wikis.
- Citation consistency audit on source imaging pages
- Person in charge: AI / maintainer
- Prerequisite: Inventory the reference notations on source imaging related pages.
- Completion condition: Inconsistencies in author notation, DOI, and year must be resolved site-wide.

## References

- Vorwerk J, Aydin U, Wolters CH, Butson CR. Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. Front Neurosci. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Rimpiläinen I, Solis-Lemus JA, Särkkä S. Improved EEG source localization with Bayesian uncertainty modelling of unknown skull conductivity. NeuroImage. 2019.
  - https://doi.org/10.1016/j.neuroimage.2018.11.058
- Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. IEEE Trans Med Imaging. 2025.
  - https://doi.org/10.1109/TMI.2025.3642620
- Duan T, Wang Z, Liu S, Yin Y, Srihari SN. UNCER: A framework for uncertainty estimation and reduction in neural decoding of EEG signals. Neurocomputing. 2023.
  - https://doi.org/10.1016/j.neucom.2023.03.071
- Hu J, Ur Rahman MM, Al-Naffouri T, Laleg-Kirati T-M. Uncertainty Estimation and Model Calibration in EEG Signal Classification for Epileptic Seizures Detection. EMBC. 2024.
  - https://doi.org/10.1109/EMBC53108.2024.10782858
- Shafiezadeh S, Duma GM, Mento G, et al. Calibrating Deep Learning Classifiers for Patient-Independent Electroencephalogram Seizure Forecasting. Sensors. 2024.
  - https://doi.org/10.3390/s24092863
- Segal G, Keidar N, Lotan RM, et al. Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. Front Neurosci. 2023.
  - https://doi.org/10.3389/fnins.2023.1184990
- Ganeshkumar P, Maheswari U, Vasant P. Reject Option to Reduce False Prediction Rates for EEG-Motor Imagery Based BCI. ICACCI. 2017.
  - https://doi.org/10.1109/ICACCI.2017.8125908
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
