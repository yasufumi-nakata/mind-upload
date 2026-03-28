# Site Deepening Audit (2026-03-14, Closed-Loop Timing / Safety)

## Scope

- Main target: `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- Secondary target: `tech_roadmap.md`

## Why This Page Was Selected

- In the previous audit, EEG, decode/emulate, and multimodal integration were made quite concrete, but there was still a mixture of generalizations and strong threshold claims around `closed loop`.
- In particular, the M2 clause of `tech_roadmap.md` has a structure that allows `1 ms or less` and `microsecond class synchronization` to be read as almost common requirements from gamma synchronization.
- However, the primary literature as of 2026-03 supports the `Closed-loop time requirements vary by loop type` arrangement, not site-wide application of a single threshold.

## Main Critiques

### 1. The current Roadmap talks about the entire closed loop with a “single timing threshold”

- Issue:
- `tech_roadmap.md` strongly promoted `jitter tolerance below 1 ms` and `microsecond measurement synchronization` due to the difficulty of phase synchronization.
- However, while it is important as part of a phase-targeted loop, it cannot be directly generalized to slow neurofeedback or adaptive DBS.
- Basis:
- Wilson et al. (2010) showed the need to measure BCI timing by dividing it into input/processing/output hardware.
- Belinskaia et al. (2020) showed that an additional 250/500 ms delay in alpha neurofeedback worsens learning. The important thing here is `shorter is better`, not requiring `1 ms` site-wide.
- Mansouri et al. (2018) and Zrenner et al. (2018) showed that in a phase-targeting system, delay should be evaluated by mapping it to `phase error`.
- In the adaptive DBS context of Little et al. (2013) and Tinkhauser et al. (2017), the dominant time constant is beta burst, a slower band than phase-locked stimulation.
- Revision:
- Completely replaced the M2 note and changed it to `leave end-to-end measurements for each loop class` form.
- I1 has also been modified to read in four sections: `state feedback / ERP-command / phase-locked / burst-driven`.

### 2. The current wiki is correct in explaining the concept, but lacks primary literature and audit items

- Issue:
- The old `wiki/closed-loop-latency-jitter-and-safety-stops.md` was useful for organizing terms such as "delay," "jitter," "drift," and "safety stop."
- However, `Why fixed thresholds are dangerous`, `Which loop class should measure what`, and `How to distinguish between marker and end-to-end` were not supported by primary literature.
- Basis:
- Thompson et al. (2013) and Mowla et al. (2017) showed that latency jitter is effective for performance in ERP-based BCI.
- Appelhoff & Stenner (2021) showed sub-ms event marking with USB markers, but this is the accuracy of the marker path and not the guarantee of the entire loop.
- Kothe et al. (2025) organized LSL's synchronized multimodal recording, but software-based synchronization and physical actuation onset need to be treated separately.
- Revision:
- Completely revised the wiki with `4 loop classes` and `4 audit layers` (end-to-end, marker/sync, phase/burst indicators, stopping rules).
- Added references, mainly primary documents.

### 3. The current description mixed "synchronization", "actual output measurement", and "safety stop"

- Issue:
- LSL, TTL marker, photodiode, phase estimator, and safety stop look similar but are separate layers.
- This difference was not made clear enough on the old page, and there was room for it to be misread as `timing is sufficient because of LSL`.
- Basis:
- Kothe et al. (2025) describes LSL as software-based synchronization.
- Wilson et al. (2010) indicates the need to measure output path separately.
- Appelhoff & Stenner (2021) shows that marker paths are faster, but display/stimulator paths are a different matter.
- Revision:
- Separated `What LSL guarantees/does not guarantee` into an independent clause.
- Fixed `abstain / freeze / safety stop` as a table to the difference between trigger and log.

## Changes Made This Round

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- Completely revised the general explanation of the 2026-03-06 version to an evidence refresh version based on primary literature.
- Added `Why fixed thresholds are dangerous`, `Four loop classes`, `Difference in role between LSL and marker`, `Minimum logs to leave`, `References`
- `tech_roadmap.md`
- Withdraw M2's `1 ms / microsecond` assumption and replace it with auditing for each loop class.
- Redefine `closed loop` in I1 with loop class and end-to-end indicator
- Updated timing/synchronization literature reference set.

## Deferred External-Dependency Tasks

- Establishment of a common evaluation system that combines phase-specific stimulation and adaptive DBS in humans on the same bench
- Person in charge: AI / maintainer / experimental collaborators
- Prerequisites: IRB, stimulation equipment, closed-loop experimental environment
- Completion condition: An experimental system that can be compared using a common end-to-end latency / phase error / stop-rule schema is in place.

## References

- Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. IEEE Trans Biomed Eng. 2010.
  - https://doi.org/10.1109/TBME.2010.2047259
- Thompson DE, Warschausky SA, Huggins JE. Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. J Neural Eng. 2013.
  - https://doi.org/10.1088/1741-2560/10/1/016006
- Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. Brain Comput Interfaces. 2017.
  - https://doi.org/10.1080/2326263X.2017.1338010
- Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. J Neural Eng. 2020.
  - https://doi.org/10.1088/1741-2552/abc8d7
- Mansouri F, Fettes P, Schulze L, et al. A real-time phase-locking system for non-invasive brain stimulation. Front Neurosci. 2018.
  - https://doi.org/10.3389/fnins.2018.00877
- Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. Brain Stimul. 2018.
  - https://doi.org/10.1016/j.brs.2017.11.016
- Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. Ann Neurol. 2013.
  - https://doi.org/10.1002/ana.23951
- Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. Brain. 2017.
  - https://doi.org/10.1093/brain/awx010
- Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. Behav Res Methods. 2021.
  - https://doi.org/10.3758/s13428-021-01571-z
- Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. Imaging Neurosci. 2025.
  - https://doi.org/10.1162/IMAG.a.136
