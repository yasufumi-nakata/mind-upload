# Site Deepening Audit (2026-03-15, Closed-Loop Longitudinal Deployment / Recalibration Burden)

## Scope

- Main target: `wiki/closed-loop-latency-jitter-and-safety-stops.md`

## Why This Page Was Selected

- The current `Closed Loop, Delay, Jitter, and Safety Stop` was a useful introduction to organizing the timing / synchronization / phase-locking literature from 2010-2021.
- However, as of 2026-03-15, the `long-term operation` `speech streaming` `home-based deployability` wall shown in the primary literature for 2024-2026 was not sufficiently reflected.
- In particular, the public page still had a structure that read the closed loop as a `loop moves once fast` problem, and `tail latency` `recalibration burden` `programming burden` could not be treated as a main variable separate from timing.
- This is a weakness from a technical/natural science perspective. This is because the current strong primary evidence is for `which loop class`, `what is the rate limit`, `how many days does it require manual recalibration`, and `can it be taken from clinic to home` rather than `fixed threshold`.

## Main Critiques

### 1. The old page did not treat `speech neuroprosthesis` as an independent loop type.

- Issue:
- The 4 types in the previous version were `state feedback` `ERP/command` `phase-locked stimulation` `adaptive DBS`.
- However, streaming brain-to-voice / voice-synthesis BCI is not a phase loop or a burst loop, but is a different system whose main indicators are `tail latency` `audio output path` `silence fallback` `false speech suppression`.
- Basis:
- Littlejohn et al. (2025) demonstrated streaming brain-to-voice with 80 ms increments and separately calculated the distribution from go cue to speech production.
- Wairagkar et al. (2025) showed a design that showed neural-to-voice synthesis of less than 10 ms, that closed-loop feedback could be rate-limited by the audio driver, and that returned silence for non-speech / overlapping speech.
- Revision:
- Added `streaming communication / speech neuroprosthesis` to `wiki/closed-loop-latency-jitter-and-safety-stops.md` as a third loop class.
- At the same time, `per-step inference latency` `cue-to-output latency` `audio driver latency` `silence / false-speech rate` `recalibration event` was added to the main log.

### 2. The old page embedded `recalibration burden` too much in the general theory of drift

- Issue:
- While the explanation of `drift` and `freeze` in the previous version was conceptually correct, it did not bring `daily supervised recalibration to the forefront at the empirical level.
- As a result, there was still room for the within-session low-latency loop to be extended to daily use.
- Basis:
- Wilson et al. (2025) identified frequent daily supervised recalibration as a major barrier to daily use, and evaluated unsupervised recalibration to handle the drift of multiple timescales in a 1-month closed-loop.
- Revision:
- Added a new `2026-03 Literature audit: Three walls that increase with long-term operation` section and cut out `recalibration burden / drift` as an independent wall.
- `time since last supervised calibration` `unsupervised adaptation` `performance decay curve` `recovery time` `human intervention time` has been promoted to main log.

### 3. The old page mixed `deployability` with loop quality

- Issue:
- The previous version organized adaptive DBS as burst detection delay and stopping rules, but did not treat `clinic / home transfer` and `programming burden` as separate review axes.
- This makes it easier to interpret the establishment of control in a lab or hospital as the establishment of chronic deployment.
- Basis:
- Oehrn et al. (2024) evaluated chronic aDBS both in-clinic and at-home.
- Cascino et al. (2026) reported that 9 out of 20 consecutive cases of chronic cDBS were eligible for aDBS, with 5 continuing as of July 2025, indicating that technical/programming constraints limit adoption.
- Revision:
- Added `naturalistic deployment / programming burden` as a third separate wall.
- `clinic/home performance gap` `eligibility` `continuation` `programming change` `stimulation duty cycle` was requested as the deployment side log.

### 4. The old page did not separate `silence / hold-last-output` from abstention/suspension.

- Issue:
- There were three types of outage tables in the old version: `abstain` `freeze` `safety stop`.
- However, in the speech/streaming system, the operational purpose of the `return short uncertainties and non-speech intervals with silence` action is different from that of abstention and hard stop.
- Basis:
- Wairagkar et al. (2025) specified a design that returns silence in non-speech / overlapping speech sections.
- Revision:
- Added `hold-last-output / silence fallback` as a separate line.
- Added `Trigger rate` `Maximum duration` `false speech suppression` `Cancellation delay` to the lowest log.

## Changes Made This Round

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- `last_updated` updated to 2026-03-15
- Updated front matter highlights / known / unknown to match 2024-2026 literature.
- Add `streaming communication / speech neuroprosthesis` to loop class table
- Added `2026-03 Literature audit: Three walls that increase with long-term operation` section
- Add `hold-last-output / silence fallback` to outage table
- Extend checklist to `module-wise latency` `speech-specific logs` `recalibration burden` `naturalistic deployment`
- updated to `6 questions when reading L3 claims`
- Add Littlejohn (2025), Wairagkar (2025), Wilson (2025), Oehrn (2024), Cascino (2026) to references

## Deferred External-Dependency Tasks

- Common deployment benchmark across speech BCI and chronic aDBS
- Person in charge: AI / maintainer / experimental collaborators
- Prerequisite: There is a public operation log that records `tail latency` `silence fallback` `recalibration burden` `clinic/home transfer` `programming burden` in a common schema.
- Completion condition: `Closed loop is fast` and `Closed loop can be used for a long time` can be publicly compared as different scores.

## References

- Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. *IEEE Trans Biomed Eng*. 2010.
  - https://doi.org/10.1109/TBME.2010.2047259
- Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. *Brain Comput Interfaces*. 2017.
  - https://doi.org/10.1080/2326263X.2017.1338010
- Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. *J Neural Eng*. 2020.
  - https://doi.org/10.1088/1741-2552/abc8d7
- Mansouri F, Fettes P, Schulze L, et al. A Real-Time Phase-Locking System for Non-invasive Brain Stimulation. *Front Neurosci*. 2018.
  - https://doi.org/10.3389/fnins.2018.00877
- Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. *Brain Stimul*. 2018.
  - https://doi.org/10.1016/j.brs.2017.11.016
- Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. *Ann Neurol*. 2013.
  - https://doi.org/10.1002/ana.23951
- Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. *Brain*. 2017.
  - https://doi.org/10.1093/brain/awx010
- Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. *Behav Res Methods*. 2021.
  - https://doi.org/10.3758/s13428-021-01571-z
- Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neurosci*. 2025.
  - https://doi.org/10.1162/IMAG.a.136
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. *Nat Med*. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. *npj Parkinsons Dis*. 2026.
  - https://doi.org/10.1038/s41531-026-01269-z
