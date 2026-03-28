# Site Deepening Audit (2026-03-14, State / Trait / Drift)

## Scope

- Main target: `wiki/state-trait-and-drift.md`
- Secondary target: `wiki/index.md`
- Secondary target: `verification.md`
- Secondary target: `eeg_101.md`

## Why This Page Was Selected

- As of today, the areas surrounding `uncertainty`, `closed-loop`, `verification`, and `decode/emulate` have been updated considerably, but the auxiliary page for `state・trait・drift`, which is the premise for them, remained at the 2026-03-06 version.
- The current page was useful as a conceptual introduction, but from a technical/natural science perspective, it put `in-situ state fluctuations', `relatively stable skeletons', `representational drift on the biological side', and `interface / decoder drift` into the same box.
- This crosstalk weakens the discussion of recently added `recalibration burden`, `abstention/silence`, `population-level stability`. In particular, there remained room to misread fixed decoder deterioration as an essential change in the brain.

## Main Critiques

### 1. The old version treated drift too much as one type.

- Issue:
- In the previous version, drift was only explained as ``changes that occur over time,'' and expression drift on the biological side and nonstationarity of electrodes, preprocessing, and decoders were not separated.
- However, in long-term BCI operation, if these two are mixed, the cause cannot be identified.
- Basis:
- Wilson et al. (2025) showed that intracortical cursor BCI requires frequent recalibration due to accumulating neural nonstationarities.
- Wairagkar et al. (2025) showed that the fixed operational performance of a brain-to-voice decoder noticeably deteriorates after about 15 days.
- Revision:
- Added `biological drift` and `interface / decoder drift` as separate lines.
- Added fixed decoder interval, recalibration burden, and recovery time to minimum submission.

### 2. The old version only described trait as a verbal "characteristic that is stable for a long time," and was too weak in defining what was considered a stable skeleton.

- Issue:
- The previous version explained trait, but it was a structure that could be misinterpreted as the immutability of a single neuron/voxel.
- However, primary literature shows that while individual units often move, latent dynamics and representational geometry are more stable.
- Basis:
- Gallego et al. (2020) showed that low-dimensional latent dynamics are stable even in the presence of neuron turnover, and decoding based on aligned latent dynamics can be maintained for a long period of time.
- Finn et al. (2015) showed that functional connectivity profiles can be used to identify individuals across cross-sessions and tasks/rests.
- Noda et al. (2025) showed that the population-level representational map is maintained even in the presence of single-neuron tuning volatility.
- Revision:
- Redefined trait as `trait-like backbone` to illustrate latent dynamics, representational geometry, and functional fingerprint.
- The site rule `trait is not a still image of a single unit` has been clarified.

### 3. The previous version only referred to state fluctuations as "short-term fluctuations" and did not actually indicate what was effective and how much.

- Issue:
- The previous version only gave examples of fatigue and concentration, but did not show that state fluctuation could be the main source of neural variance.
- Basis:
- Musall et al. (2019) showed that uninstructed movements strongly regulate cortex-wide activity.
- Benisty et al. (2024) showed that spontaneous behavior rapidly changes not only the magnitude but also the correlational structure of functional connectivity.
- Revision:
- Made `state fluctuation` not just noise, but an independent layer that should be audited within-session.
- Simultaneous measurement of behavior and physiology and performance differences by state have been included in the minimum evaluation.

### 4. Previous edition had no primary literature or longitudinal benchmark

- Issue:
- There was no bibliography section, so I couldn't follow the basis on which readers differentiate between state/trait/drift.
- Also, it was not fixed what kind of logs were needed to read the longitudinal evaluation.
- Revision:
- Added 8 primary documents supporting state fluctuation, trait-like backbone, representational drift, and decoder drift.
- Fixed the 4 audit items of `state sensitivity / fixed-model stability / population backbone / recalibration burden` as a table.

## Changes Made This Round

- `wiki/state-trait-and-drift.md`
- Updated front matter to focus on technology and natural sciences
- Newly added `Four layers`, `Why the traditional three classifications are not enough`, `Reality shown by primary documents`, `At least what should be kept separate`, `Demotion rules`, `References`
- Redefine trait as `trait-like backbone`
- Explicit fixed decoder interval and recalibration burden
- site-wide label consistency
- Updated the old link text for `Uncertainty, Confidence Intervals and Abstentions` to match the retitled `Uncertainty, Calibration and Abstentions`

## Deferred External-Dependency Tasks

- Implementation of cross-modal longitudinal benchmark
- Person in charge: AI / maintainer / experimental collaborators
- Prerequisites: Public data including state manipulation, long-term remeasurement, fixed decoder hold, and recalibration log for the same subject
- Completion condition: `state sensitivity / trait backbone / drift / recalibration burden` comparison of the same schema is possible in at least two EEG/invasive BCI/fMRI systems.

## References

- Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. Nat Neurosci. 2019.
  - https://doi.org/10.1038/s41593-019-0502-4
- Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. Nat Neurosci. 2024.
  - https://doi.org/10.1038/s41593-023-01498-y
- Gallego JA, Perich MG, Chowdhury RH, Solla SA, Miller LE. Long-term stability of cortical population dynamics underlying consistent behavior. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-019-0555-4
- Finn ES, Shen X, Scheinost D, et al. Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. Nat Neurosci. 2015.
  - https://doi.org/10.1038/nn.4135
- Roth ZN, Merriam EP. Representations in human primary visual cortex drift over time. Nat Commun. 2023.
  - https://doi.org/10.1038/s41467-023-40144-w
- Noda T, Kienle E, Eppler J-B, et al. Homeostasis of a representational map in the neocortex. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01982-7
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
