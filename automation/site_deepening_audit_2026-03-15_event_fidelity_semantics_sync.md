# Site Deepening Audit (2026-03-15, Event Fidelity / Semantics / Synchronization)

## Scope

- Main target: `wiki/event-sync-and-measurement-logs.md`
- Secondary target: `datasets.md`
- Subsidy target: `wiki/standards-repositories-validators-and-benchmarks.md`

## Why This Page Was Selected

- From a technical/natural science perspective, we have determined that the next weakness of the current site is `event sync / annotation fidelity`.
- The reason is that even though the current text correctly states that "events and synchronization are important," it has not yet sufficiently separated `timestamp tables`, `event semantics`, `clock alignment`, and `device-side delay`.
- This weakness is directly related to entrance practices. Even if the waveforms and labels are made public, if the event semantics and clock system are ambiguous, the time fidelity that is the strength of EEG will collapse.

## Main Critiques

### 1. The old page had room to read `events.tsv` as something close to the whole event fidelity

- Issue:
- The current `wiki/event-sync-and-measurement-logs.md` correctly stated the importance of event markers and label provenance, but it did not fully emphasize that `BIDS task events` mainly provides time and column instruments, and not the semantics itself necessary for cross-study comparisons.
- Therefore, there was still room for misinterpretation that the event semantics were fixed just by having `events.tsv`.
- Basis:
- The BIDS task events specification provides a description frame with `events.tsv` and sidecar JSON.
- Robbins et al. (2021) showed that existing time series data standards tend to lack important details in event descriptions, and HED supplements FAIR event annotation.
- Hermes et al. (2025) showed that EEG data annotation can be organized in a machine-actionable manner using the HED library schema.
- Revision:
- Added `Event fidelity audits in three layers` clause to `wiki/event-sync-and-measurement-logs.md` and separated `Temporal Anchors / Event Semantics / Synchronization and Transport`.
- Added `events.json and HED` to the EEG-BIDS section on the same page.

### 2. The old page did not sufficiently isolate the scope of LSL

- Issue:
- The current page explained latency, jitter, and drift, but it didn't say enough about what synchronization middleware like LSL does and doesn't solve.
- Therefore, there remained a structure that could be read as if the hardware delay had been converted into ground-truth just by having LSL and trigger.
- Basis:
- Kothe et al. (2025) clearly stated that while LSL handles network delay and jitter and supports recording with millisecond precision, input device throughput delay and on-device processing delay cannot be estimated and corrected using software timestamps alone.
- Revision:
- Added `LSL is valid, but not hardware ground truth` clause to `wiki/event-sync-and-measurement-logs.md`.
- Specified site rule to leave `timestamp domain`, `device-side delay`, `drift / resync policy`, and `validation method` as separate logs.
- Also added to `wiki/standards-repositories-validators-and-benchmarks.md` that LSL is a synchronization middleware and not a replacement for BIDS or benchmark.

### 3. The old datasets path emphasized annotation provenance, but did not fix event semantics and sync evidence as required fields in the dataset card.

- Issue:
- `datasets.md` made the label provenance and time granularity fairly clear, but did not yet make `clock domain`, `delay / jitter audit`, and `event semantics` required fields as the minimum submission for the dataset card.
- In this case, even if only the dataset name and label origin were aligned, there was a possibility that the time fidelity audit could be missed.
- Basis:
- BIDS EEG and EEG-BIDS provide a floor of shareable metadata, but are insufficient for time-aligned benchmarks without adding event semantics and clock audit.
- Motion-BIDS (Jeung et al., 2024) showed that in additional modalities, metadata and coordinate frame are the core of interpretation.
- Revision:
- Added `Event Fidelity Card` note to `datasets.md`.
- Expanded the site rule of dataset card to 6 items of `provenance / time grain / clock domain and sync evidence / event semantics / split unit / stop claim`.

### 4. The old standards page was able to distinguish between BIDS, repository, validator, and benchmark, but the `event semantics` and `synchronization middleware` layers were missing.

- Issue:
- `wiki/standards-repositories-validators-and-benchmarks.md` was useful as a five-layer arrangement, but in practice as of 2026-03, it is necessary to treat BIDS vessels, HED / Motion-BIDS semantics, and LSL synchronization as separate layers.
- Revision:
- The operational stack on the same page has been updated to 7 layers.
- Added `HED/Motion-BIDS` as `Event Semantics/Extension schema` and `LSL` as `Synchronization Middleware`.
- Added ``Events.tsv'' has fixed semantics and ``Since LSL was used, hardware delay has been resolved.'' to the ``Common confusions'' table.

## Changes Made This Round

- `wiki/event-sync-and-measurement-logs.md`
- Added a section that divides event fidelity into three tiers.
- Added section explaining scope and limitations of LSL
- Added `events.json + HED`, `clock / sync log`, `*_coordsystem.json` to EEG-BIDS clause.
- Added `Event Fidelity Card` as site rule
- Expanded references to BIDS / HED / LSL / Motion-BIDS
- `datasets.md`
- Updated `Just having raw EEG is not enough` section
- `Event Fidelity Card` Added note
- Expanded required fields of dataset card to 6 items
- Added BIDS task events, HED, LSL, Motion-BIDS to references
- `wiki/standards-repositories-validators-and-benchmarks.md`
- Updated 5-layer organization to 7-layer organization
- Added HED / Motion-BIDS / LSL as separate layer
- Added 2 rows to common confusion table

## Deferred External-Dependency Tasks

- Actual measurement of site-wide event fidelity template including hardware delay
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisite: Ability to operate measurement paths such as photodiode, loopback, and TTL on actual equipment.
- Completion condition: Clock domain, device-side delay, and validation method must be the same template for each EEG + stimulus + motion experiment run.

## References

- BIDS Specification. Task events.
  - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html
- BIDS Specification. Electroencephalography.
  - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Sci Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Robbins KA, Truong D, Jones P, et al. Building FAIR functionality: annotating events in time series data using Hierarchical Event Descriptors (HED). *Neuroinformatics*. 2021.
  - https://doi.org/10.1007/s12021-021-09513-7
- Hermes D, et al. HED library schema for EEG data annotation. *Sci Data*. 2025.
  - https://doi.org/10.1038/s41597-025-05791-2
- Kothe CA, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
  - https://doi.org/10.1162/imag_a_00136
- Jeung S, et al. Motion-BIDS, an extension to the brain imaging data structure for motion data. *Sci Data*. 2024.
  - https://doi.org/10.1038/s41597-024-03559-8
