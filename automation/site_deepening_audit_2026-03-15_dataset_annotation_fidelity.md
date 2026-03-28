# Site Deepening Audit (2026-03-15, Dataset Annotation Fidelity / Leakage Units)

## Scope

- Main target: `datasets.md`
- Secondary target: `wiki/event-sync-and-measurement-logs.md`
- Secondary target: `wiki/dataset-splits-and-leakage.md`

## Why This Page Was Selected

- `datasets.md` was pretty well organized as of 2026-03-14 until the version pin, BIDS, loader, and benchmark harness were separated.
- However, the explanations for the four starter data items still had the center of gravity at `ease of use` and `general notes`, and `where the labels came from`, `at what time granularity', and `what should be considered independent split units` were not sufficiently fixed.
- This weakness is significant from a technical/natural science perspective. This is because even though they are all the same `EEG dataset`, cue-locked event, expert interval annotation, manual hypnogram, and report-derived label are different information-based things, and if you compare scores while leaving this ambiguous, the meaning of benchmark will be lost.

## Main Critiques

### 1. The old `datasets.md` listed dataset names, but did not focus on annotation provenance.

- Issue:
- The old version explained the suitability of `EEG Motor Movement/Imagery`, `CHB-MIT`, `Sleep-EDF`, and `TUH EEG`.
- However, the difference between `cue-locked annotation channel`, `expert seizure interval`, `manual hypnogram`, and `report-derived clinical label` was not fixed in the table.
- Basis:
- EEG Motor Movement/Imagery is a cue-locked task with T0/T1/T2 in annotation channel / `.event`.
- CHB-MIT has a long-recording seizure annotation with summary / `.seizure`, and `chb21` is the same subject as `chb01`.
- Sleep-EDF Expanded has Rechtschaffen & Kales hypnogram and 1 Hz event marker by well-trained technicians.
- TUH EEG Corpus has patient / session hierarchy and de-identified clinician report `.txt`, and TUSZ includes report keyword search and selection using algorithmic triage.
- Revision:
- Added a table with `Label/Event Origin` and `Temporal Fidelity` as independent columns to `datasets.md`.
- In addition, we added `Claim that stops here` and `Minimum operating rules` to each line to fix the claim ceiling of this site.

### 2. The old site placed `observation log` too much in event marker and timing, and did not treat label provenance as log.

- Issue:
- `wiki/event-sync-and-measurement-logs.md` explained that raw EEG alone is not enough, but was mainly talking about marker / sync / bad segment.
- Therefore, `manual scoring` and `report-derived label` could not be treated as observation logs that could not be restored later.
- Basis:
- In Sleep-EDF, the sleep stage itself is a manual hypnogram, and when the scoring manual is lost, the meaning of the label changes.
- TUH / TUSZ comes with report text and report-derived triage, and there will be a leakage risk if the signal-only benchmark and multimodal benchmark are not separated.
- Revision:
- Added `Read the source of the label in four different ways` clause to `wiki/event-sync-and-measurement-logs.md`.
- `annotation channel / expert interval / manual hypnogram / report-derived label` are arranged and the necessary auxiliary logs are associated with each one.

### 3. The old `dataset-splits-and-leakage` was correct in general terms, but it did not fix the dataset-specific independent unit.

- Issue:
- The old version explained the principle of subject / session / time split, but did not specify what `true independent units` was in each starter data.
- This left room to read, for example, `CHB-MIT is sufficient for file units`, `Sleep-EDF may shuffle epochs`, `TUH may be segment split`.
- Basis:
- CHB-MIT includes the exception that `chb21` = `chb01` same subject.
- Sleep-EDF has a subject-night structure and has strong information about same-night hypnogram continuity.
- TUH EEG / TUSZ has patient / session hierarchy and report text can be session-level covariate.
- Revision:
- Added 4 datasets `Independent unit`, `Common mis-splits`, `Why are they leaked`, `Safe way of splitting` to `wiki/dataset-splits-and-leakage.md`.
- In addition, `Independent ID`, `report usage`, and `label manual` have been added to the minimum reporting items.

### 4. There was room to read Sleep-EDF's manual scoring on the same level as modern sleep benchmarks.

- Issue:
- The previous version introduced Sleep-EDF as a good gateway to state transition learning, but did not use the difference between R&K scoring and AASM scoring as an operational gate.
- Basis:
- Sleep-EDF Expanded is manual scoring based on R&K.
- Moser et al. (2009) showed the areas where AASM and R&K sleep classification do not match.
- Revision:
- Added `R&K -> Do not compare cross-datasets without writing AASM mapping rule` site rule to `datasets.md` and two wikis.

## Changes Made This Round

- `datasets.md`
- `last_updated` updated to 2026-03-15
- Add `annotation provenance` to front matter and body
- Added tables for `Label/Event Origin`, `Time Fidelity`, `Stopping Claims`, `Minimum Operational Rules`
- Added `Annotation provenance` to checklist
- `wiki/event-sync-and-measurement-logs.md`
- Updated `last_updated` and front matter
- Revised the policy to treat `label provenance` on the same level as event log.
- Added logging rules for 4 label types and starter data
- Added references section
- `wiki/dataset-splits-and-leakage.md`
- Updated `last_updated` and front matter
- Add dataset-specific independent unit table
- Added `report usage` and `label manual` to minimum reporting items.
- Added references section

## Deferred External-Dependency Tasks

- Unification of site-wide dataset card schema
- Person in charge: AI / maintainer
- Prerequisite: Other dataset/benchmark pages also treat `annotation provenance` `time fidelity` `split unit` `claim ceiling` as a common attribute.
- Completion condition: On the public data introduction page, not only the dataset name but also the above four attributes are always displayed at the front.

## References

- PhysioNet: EEG Motor Movement/Imagery Dataset
  - https://physionet.org/content/eegmmidb/1.0.0/
- PhysioNet: CHB-MIT Scalp EEG Database
  - https://physionet.org/content/chbmit/1.0.0/
- PhysioNet: Sleep-EDF Database Expanded
  - https://physionet.org/content/sleep-edfx/1.0.0/
- Obeid I, Picone J. The Temple University Hospital EEG Data Corpus. *Front Neurosci*. 2016.
  - https://doi.org/10.3389/fnins.2016.00196
- Shah V, von Weltin E, Lopez S, et al. The Temple University Hospital Seizure Detection Corpus. *Front Neuroinform*. 2018.
  - https://doi.org/10.3389/fninf.2018.00083
- Moser D, Anderer P, Gruber G, et al. Sleep classification according to AASM and Rechtschaffen & Kales: effects on sleep scoring parameters. *Sleep*. 2009.
  - https://pubmed.ncbi.nlm.nih.gov/19238800/
