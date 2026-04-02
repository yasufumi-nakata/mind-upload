# Site Deepening Audit: `datasets.md` starter-dataset evidence trace

Date: 2026-04-02  
Scope: `datasets.md` sections `3) Audit to avoid overestimating starter data` and `5) Checklist that does not end with just “there is data”`  
Method: repository audit + primary-source verification + public-page revision

## Why this page was selected

This page is one of the public front doors for practical work. Its core operational logic was already strong: it distinguished starter datasets, split units, timing fidelity, and claim ceilings better than most EEG starter guides.

The remaining weakness was narrower but important:

1. Several of the strongest stop-lines were correct but still looked like site policy rather than source-traceable scientific constraints.
2. The page told readers to respect provenance, yet it did not sufficiently show how official dataset descriptions, scorer-reliability studies, and benchmark postmortems force that requirement.
3. The page warned about leakage, but the reason leakage must be treated as a first-class scientific issue rather than a mere engineering mistake was not explicit enough in-body.

## Main critique

### 1. The dataset caveats were operationally right but evidentially under-anchored in-body

The page already told readers not to overread EEGMMI, CHB-MIT, Sleep-EDF, or TUH/TUSZ. The problem was not the direction of the warning. The problem was the missing trace from warning to primary source.

That gap matters because this site is trying to become a verification commons. A stop-line that cannot be traced to acquisition design, annotation design, or validation history is easy for readers to misread as house style.

### 2. Sleep-stage labels needed a clearer measurement ceiling

The page already noted that Sleep-EDF uses R&amp;K labels and coarse event timing. What it still underplayed was that even expert human sleep staging remains imperfect. Without that added ceiling, readers can still mentally upgrade a manually scored hypnogram into a frictionless target.

### 3. Benchmark provenance needed to be tied to documented failures, not only to abstract caution

The checklist already asked for benchmark provenance, but the page did not sufficiently connect that request to published failures in EEG benchmarking practice. That left the requirement looking administrative. It is not administrative. It is directly tied to whether a score means what the reader thinks it means.

## Evidence trace

### EEG Motor Movement/Imagery

- The official PhysioNet description fixes the task as cue-driven rather than open semantic intent: 109 volunteers, 64 channels, 14 runs, 160 Hz, and T0/T1/T2 onset codes in the annotation channel and `.event` files.
- Scientific consequence:
  the dataset is strong for cue-locked preprocessing, split hygiene, and baseline decoding practice, but it does not justify promoting results to open-ended semantic or free-intent readout.
- Source:
  - [EEG Motor Movement/Imagery Dataset v1.0.0](https://physionet.org/content/eegmmidb/1.0.0/)

### CHB-MIT

- The official description fixes a pediatric epilepsy monitoring context with 22 subjects organized into 23 cases, identifies `chb21` as the same subject as `chb01`, and documents gaps between consecutively numbered EDF files.
- Scientific consequence:
  randomization by file can overstate independence, and gap-free continuous-monitoring interpretations are not justified.
- Sources:
  - [Guttag (2010), CHB-MIT Scalp EEG Database](https://doi.org/10.13026/C2K01R)
  - [Ali Shoeb (2009), PhD thesis referenced by PhysioNet](https://hdl.handle.net/1721.1/54669)

### Sleep-EDF

- The official description fixes a narrow montage and mixed timing resolution: Fpz-Cz / Pz-Oz EEG, EOG, chin EMG, with event markers and some auxiliary channels at 1 Hz; hypnograms are manual R&amp;K scores.
- Rosenberg &amp; Van Hout (2013) reported about 82.6% average inter-scorer agreement in the AASM program, with lower agreement for N1 and N3.
- Scientific consequence:
  a manual hypnogram remains a bounded human annotation route, not a frictionless high-resolution target.
- Sources:
  - [Sleep-EDF Database Expanded v1.0.0](https://doi.org/10.13026/C2X676)
  - [Rosenberg & Van Hout (2013)](https://doi.org/10.5664/jcsm.2350)

### TUH / TUSZ

- Obeid & Picone (2016) describe TUEG as a clinical EEG corpus paired with clinician reports in `.txt` form.
- Shah et al. (2018) describe seizure-rich triage for TUSZ using report keyword search and automatic detectors.
- Later maintenance notes reported that an early Neureka 2020 release had non-exclusive subjects across train/dev/blind evaluation and annotation issues for high-frequency seizures.
- Scientific consequence:
  report usage, patient/session ancestry, and post-release benchmark corrections must remain visible in the result itself.
- Sources:
  - [Obeid & Picone (2016)](https://doi.org/10.3389/fnins.2016.00196)
  - [Shah et al. (2018)](https://doi.org/10.3389/fninf.2018.00083)
  - [Hamid et al. (2021) maintenance note](https://par.nsf.gov/servlets/purl/10311411)

### Leakage as a scientific, not merely engineering, failure mode

- Brookshire et al. (2024) show that segment-based cross-validation in translational EEG can leak subject information between train and test sets and inflate performance.
- Scientific consequence:
  subject exclusivity and segment/window ancestry are part of the claim ceiling, not optional hygiene.
- Source:
  - [Brookshire et al. (2024)](https://doi.org/10.3389/fnins.2024.1373515)

## Changes executed in this session

1. Added an evidence-backed note box to `datasets.md` that ties dataset stop-lines to official dataset descriptions, scorer-reliability evidence, and TUH/TUSZ maintenance records.
2. Strengthened the public checklist so `annotation provenance`, `benchmark provenance`, and `rebuttal evidence` explicitly require scorer ceilings, subject exclusivity, and segment/window ancestry.
3. Rewrote the benchmark-provenance note to connect it to documented leakage and split-repair evidence rather than abstract caution.
4. Added the newly used sources to the page reference list.

## External dependency tasks

None for this pass.

No new experiments, recruitment, IRB action, hardware acquisition, or legal review were required to execute the selected improvement.

## Verification

- `git pull --ff-only`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `git diff --stat`

## Files changed

- `/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md`
- `/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-02_datasets_starter_evidence_trace.md`
