# Mind-upload RQ60 Application Playbook (RQ unit fixed)

> Fix submission decisions based on RQ, not general abstracts
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-30 / Role: Per-RQ Grant and Dataset Playbook

## Role Of This Page
This page is a practical playbook that targets each of mind-upload's 60 research questions and fixes the primary application destination/preliminary application destination, main EEG-DATA, reason for hiring, and submitted deliverables.

## Accuracy Notes
A/B/C judgment uses the same criteria as `mind-upload-eeg-rq60-feasibility-and-funds.md`.

## Back To Public Pages
- [Literature map](https://mind-upload.com/research_harvest_50.html)
- [Data & Bench](https://mind-upload.com/datasets.html)

## Related Wiki Pages
- [Wiki: RQ60 EEG verification availability and subsidy theme](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds) - Original copy of judgment basis, U-specific background, and RQ table.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Criteria for converting artifacts into verification specifications.

---

## How to use

1. Select one `RQ` and fix the `first application destination` and `main EEG-DATA`.
2. Create only the `minimum deliverables` first (expand after completion).
3. `C` judgments do not make performance claims and are submitted in the system/audit design track.
4. Numeric `ID` in this page is for search guidance only. Submission/reproducibility logs must use `DOI + dataset name + access class` in the canonical map `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.

## Fixed map (first application destination/preliminary application destination)

- `U0: G2/G3`, `U1: G1/G4`, `U3: G2/G6`, `U4: G1/G4`
- `U7: G1/G3`, `U8: G2/G5`, `U10: G2/G6`, `U11: G2/G4`
- `U12: G2/G6`, `U13: G1/G4`, `U14: G1/G3`, `U15: G2/G6`

## Current funding reality (2026-03-30 01:08 JST)

- `G1/G2` are routing keys used to keep the RQ-level application lanes stable. They are not current grant-card files.
- Current grant-card entities are `G3-G6`, and the practical shortlist is now fixed in [AoyamaLab/auto-research-funds wiki: Mind-Upload-Current-Funding-Shortlist](https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md).
- The six currently revalidated deep-focus RQs are `U13-2`, `U13-5`, `U14-4`, `U0-2`, `U0-3`, and `U14-2`.
- The public route is now intentionally concentrated on `inner-speech decoding + identity drift + reproducibility auditing`, with `D10/D03/D01/D02` used as the conservative anchor family.
- Inside that anchor family, `D10/D02` are the strongest current primary anchors. `D03/D01` stay useful for the public route, but they should be read as bounded route-setting anchors until the first artifacts and logs are denser.
- The practical funding bridge for this batch is led by `Nakatani Foundation graduate scholarship` and `Kura Fund`; the `Kashinome Scholarship` stays only as a student-runway side route, and the `Nakatani Foundation research grant` remains a watch-mode route rather than a current open call.
- Relevant Todoist tasks for the practical shortlist already existed before this run, so no new task was created in this run.
- For submission-ready references, prefer `Dxx + DOI + dataset name + access class` over numeric search IDs.
- The six current public rows below are now synchronized to `Dxx + DOI + dataset name + access class`, so the playbook no longer needs numeric search IDs for `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2`.
- `tech_roadmap.md` also contains `U2/U5/U6/U9`, but those roadmap families are not yet translated into this playbook's current `RQ60` practical layer.

## Anchor-strength recheck (2026-03-30 05:07 JST)

This run keeps the same public six-RQ batch and the same practical submission routes. What changed is the reading discipline for the current anchors after a post-pull `EEG-DATA` reread, a live-site check, an official-window recheck, and a read-only Todoist recheck. `D10` and `D02` remain the stronger primary anchors for first artifacts. `D03` and `D01` remain useful, but they should still be treated as bounded support anchors until a richer speech-side or benchmark-style adjunct is added.

| RQ | Current anchor class | Funding route to keep now | Why this route still fits | Adjunct before stronger proposal wording |
|---|---|---|---|---|
| `U13-2` | Strong primary (`D10 3M-CPSEED`) | `Kura Fund` / `Nakatani Foundation graduate scholarship` | Public BIDS speech phases make it the shortest route to a `brain-minus-prior` control story. | Add an external language-evaluation layer and a broader control family. |
| `U13-5` | Bounded support (`D03`) | `Kura Fund` / `Nakatani Foundation graduate scholarship` | The immediate EEG + eye-tracking release is still enough for a narrow perception-to-transfer branch note. | Add `CuBiAAD` or another speech-richer adjunct before stronger mechanism language. |
| `U0-2` | Strong primary (`D02 CSTE`) | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship` | Cross-session and cross-task biometric structure still makes it the cleanest current identity-drift floor. | Add a longer-horizon adjunct with more explicit timing and synchronization logs. |
| `U0-3` | Strong primary (`D02 CSTE`) | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship` | The same cross-session floor keeps threshold stability and overfit exclusion on the same bounded identity route. | Add a session-external rerun pack and a larger cohort extension. |
| `U14-4` | Bounded support (`D01`) | `Kura Fund` / `Nakatani Foundation research grant (watch)` | A latency-first wireless-delay dataset is still enough to force concrete disclosure fields into the rerun contract. | Add `A New Benchmark Dataset Towards Ubiquitous P300 ERP-based BCI Applications` for richer rerun examples. |
| `U14-2` | Bounded support (`D01`) | `Kura Fund` / `Nakatani Foundation research grant (watch)` | The same narrow latency route still supports an operational exploration/confirmation split. | Add the same public benchmark-style rerun adjunct plus split-violation examples. |

- No new Todoist task was needed in this run because the current practical routes were already covered by existing tasks.
- `高齢社会課題解決研究(AI)` still remains outside this EEG-first, one-RQ-at-a-time route and therefore stays deferred.

## Current public six after the March 30 official-window and Todoist recheck

This run keeps the same public batch and the same funding routes. The only new layer is execution wording: one submission-ready theme, one anchor reason, and one task-status sentence per current row.

| RQ | Submission-ready theme | Why the current funder still fits | Main anchor and first deliverable | Task status |
|---|---|---|---|---|
| `U13-2` | `Neural-contribution audit for imagined speech with a brain-minus-prior control` | `Kura Fund` still fits the bounded young-researcher benchmark route, and `Nakatani Foundation graduate scholarship` still fits the doctoral-track continuity route. | `D10 3M-CPSEED` because the current mirror still preserves an immediate speech-decoding package with overt / silent-intended / imagined speech across `20 participants x 4 sessions`; first deliverable: `brain-minus-prior control table`. | Existing `Kura` and `Nakatani graduate scholarship` start/deadline tasks were rechecked in this run; no new Todoist item was needed. |
| `U13-5` | `Perception-to-recall transfer-gap benchmark for mimic separation` | `Kura Fund` still fits the bounded benchmark framing, and `Nakatani Foundation graduate scholarship` still fits the doctoral-track extension because the row remains a narrow mechanism-separation test rather than a solved theory claim. | `D03 Multimodal Fusion EEG + Eye-Tracking` because the current mirror still keeps an immediate paired EEG + gaze route; first deliverable: `perception-to-recall degradation note`. | Existing `Kura` and `Nakatani graduate scholarship` tasks already cover this route; no duplicate task was added. |
| `U0-2` | `Temporal-validity-aware identity drift audit with offset, jitter, and state-feature collapse` | `Nakatani Foundation graduate scholarship` still fits the student-facing continuity / biometrics route, while `Kashinome Scholarship` still fits only as a runway-support layer. | `D02 CSTE` because the current mirror still preserves an immediate `cross-session / cross-task` biometric benchmark with `10 participants`; first deliverable: `offset/jitter distribution audit`. | Existing `Nakatani graduate scholarship` and `Kashinome` tasks were rechecked; no new task was needed. |
| `U0-3` | `Task-specific threshold stability and overfit-exclusion benchmark for identity drift` | The same `Nakatani graduate scholarship` plus `Kashinome` route still fits because this row remains a bounded doctoral-track threshold-governance problem rather than a broader personhood claim. | `D02 CSTE` on the same identity-drift floor as `U0-2`; first deliverable: `threshold-stability note and selection rationale`. | Existing `Nakatani graduate scholarship` and `Kashinome` tasks already cover the row; no new task was needed. |
| `U14-4` | `Card-integrated reproducibility contract for the current public batch` | `Kura Fund` still fits the immediate young-researcher reproducibility package, while `Nakatani Foundation research grant` remains watch-only because the current cycle is closed. | `D01 Acquisition delay of wireless EEG` because the current mirror still gives an immediate latency-first measurement route; first deliverable: `filled Model Card / Dataset Card examples`. | Existing `Kura` tasks and existing `Nakatani research grant` watch tasks were rechecked; no new task was needed. |
| `U14-2` | `Exploration-vs-confirmation split contract for reruns` | `Kura Fund` still fits the immediate bounded reproducibility route, while `Nakatani Foundation research grant` remains a next-cycle watch route only. | `D01 Acquisition delay of wireless EEG` on the same latency-first rerun floor as `U14-4`; first deliverable: `fixed-split rerun contract and negative-case trail`. | Existing `Kura` and `Nakatani research grant` watch tasks already cover the row; no new task was needed. |

## Fixed table by RQ (60 items)

| RQ | Judgment | First applicant | Preliminary applicant | Main EEG-DATA | Reason for selecting main data | Minimum deliverables |
|---|---|---|---|---:|---|---|
| U0-1 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | It is easy to track identity changes across sessions in the same framework. | Intervention protocol and rebuttal condition definition |
| U0-2 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | D02 CSTE (10.21227/j162-nh61 / immediate) | Repeated sessions, cross-task identity labels, and timestamp/QC metadata make it the cleanest current anchor for `clock offset + jitter + state-feature collapse` auditing. | Time synchronization audit report (offset/jitter distribution) |
| U0-3 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | D02 CSTE (10.21227/j162-nh61 / immediate) | Repeated sessions and cross-task splits let the threshold-stability and overfit-exclusion route stay on the same identity-drift anchor as `U0-2`. | Threshold search notebook and selection rationale table |
| U0-4 | B | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | It is easy to track identity changes across sessions in the same framework. | Identity determination two-axis report (observation match/intervention match) |
| U1-1 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | Easy to measure errors and uncertainties of inverse problems under known intervention/high density conditions. | Inverse solution comparison table and uncertainty distribution chart |
| U1-2 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | Easy to measure errors and uncertainties of inverse problems under known intervention/high density conditions. | Inverse problem reproduction report (error/uncertainty) |
| U1-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | Easy to measure errors and uncertainties of inverse problems under known intervention/high density conditions. | Inverse problem reproduction report (error/uncertainty) |
| U1-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | Easy to measure errors and uncertainties of inverse problems under known intervention/high density conditions. | Inverse solution comparison table and uncertainty distribution chart |
| U3-1 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG alone and multimodal condition differences can be easily compared using the same evaluation axis. | Boundary expansion evaluation report (single/integrated comparison) |
| U3-2 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG alone and multimodal condition differences can be easily compared using the same evaluation axis. | Boundary expansion evaluation report (single/integrated comparison) |
| U3-3 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG alone and multimodal condition differences can be easily compared using the same evaluation axis. | Boundary expansion evaluation report (single/integrated comparison) |
| U3-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG alone and multimodal condition differences can be easily compared using the same evaluation axis. | Boundary expansion evaluation report (single/integrated comparison) |
| U3-5 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG alone and multimodal condition differences can be easily compared using the same evaluation axis. | Boundary expansion evaluation report (single/integrated comparison) |
| U3-6 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | EEG alone and multimodal condition differences can be easily compared using the same evaluation axis. | Boundary expansion evaluation report (single/integrated comparison) |
| U4-1 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | It is easy to separate the difference between correlation and causation by clearly indicating the presence or absence of intervention. | Intervention protocol and rebuttal condition definition |
| U4-2 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | It is easy to separate the difference between correlation and causation by clearly indicating the presence or absence of intervention. | Intervention protocol and rebuttal condition definition |
| U4-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | It is easy to separate the difference between correlation and causation by clearly indicating the presence or absence of intervention. | Intervention protocol and rebuttal condition definition |
| U4-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | It is easy to separate the difference between correlation and causation by clearly indicating the presence or absence of intervention. | Causal verification report (minimum intervention claim) |
| U7-1 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | Synchronization, QC, and reproducibility audits can be easily linked directly to operational indicators. | Time synchronization audit report (offset/jitter distribution) |
| U7-2 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | Synchronization, QC, and reproducibility audits can be easily linked directly to operational indicators. | Time synchronization audit report (offset/jitter distribution) |
| U7-3 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | Easy to connect synchronization, QC, and reproducibility audits directly to operational indicators. | Reproducibility audit report (synchronization/QC/preprocessing difference) |
| U7-4 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | Synchronization, QC, and reproducibility audits can be easily linked directly to operational indicators. | Reproducibility audit report (synchronization/QC/preprocessing difference) |
| U7-5 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | Synchronization, QC, and reproducibility audits can be easily linked directly to operational indicators. | Threshold search notebook and selection rationale table |
| U7-6 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | Synchronization, QC, and reproducibility audits can be easily linked directly to operational indicators. | Reproducibility audit report (synchronization/QC/preprocessing difference) |
| U8-1 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | Closed-loop KPIs for delay/relearning/safety stop are easy to measure. | Closed loop safety KPI dashboard |
| U8-2 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | Closed-loop KPIs for delay/relearning/safety stop are easy to measure. | Closed loop safety KPI dashboard |
| U8-3 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | Closed-loop KPIs for delay/relearning/safety stop are easy to measure. | Operational stability report (safety shutdown/recovery time) |
| U8-4 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 2412 | Closed-loop abnormal-detection latency, fail-safe trigger, and recovery can be measured in the same contract. | Operational stability report (safety shutdown/recovery time) |
| U8-5 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | Closed-loop KPIs for delay/relearning/safety stop are easy to measure. | Closed loop safety KPI dashboard |
| U8-6 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | Closed-loop KPIs for delay/relearning/safety stop are easy to measure. | Closed loop safety KPI dashboard |
| U10-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | It is easy to verify the difference between theoretical consistency and physiological proxy step by step. | Theory consistency memo and proxy correlation analysis |
| U10-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | It is easy to verify the difference between theoretical consistency and physiological proxy step by step. | Theory consistency memo and proxy correlation analysis |
| U10-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | It is easy to verify the difference between theoretical consistency and physiological proxy step by step. | Theory consistency report (thermodynamic proxy) |
| U10-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | It is easy to verify the difference between theoretical consistency and physiological proxy step by step. | Theory consistency memo and proxy correlation analysis |
| U11-1 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | It is easy to preserve the ranking of theoretical indicators and verify failure conditions using state difference data. | Awareness index comparison report (with failure condition) |
| U11-2 | C | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | It is easy to verify the ranking preservation and failure conditions of theoretical indicators using state difference data. | Theoretical comparison I/O specifications and calculation budget |
| U11-3 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | It is easy to preserve the ranking of theoretical indicators and verify failure conditions using state difference data. | Awareness index comparison report (with failure condition) |
| U11-4 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | It is easy to preserve the ranking of theoretical indicators and verify failure conditions using state difference data. | Theoretical comparison I/O specifications and calculation budget |
| U12-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | It is technically easy to maintain audit logs to be passed to system issues. | Branch-based audit log design document |
| U12-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | It is technically easy to maintain audit logs to be passed to system issues. | System audit requirements table (technical log compatible) |
| U12-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | It is technically easy to maintain audit logs to be passed to system issues. | System audit requirements table (technical log compatible) |
| U12-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | It is technically easy to maintain audit logs to be passed to system issues. | Branch-based audit log design document |
| U12-5 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | It is technically easy to maintain audit logs that support branch relinking and subject-ID reorganization decisions. | Branch-based audit log design document |
| U12-6 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | It is technically easy to maintain audit logs to be passed to system issues. | System audit requirements table (technical log compatible) |
| U13-1 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | It is easy to separate semantic restoration and mechanistic difference using control conditions. | Intervention protocol and rebuttal condition definition |
| U13-2 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | D10 3M-CPSEED (10.18112/openneuro.ds006465.v2.0.0 / immediate) | Overt/silent/imagined speech plus transcript-aligned phases make it the strongest current `brain-minus-prior` anchor for hallucination and neural-inconsistency auditing. | Mimic separation evaluation script and control condition table |
| U13-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | It is easy to separate semantic restoration and mechanistic difference using control conditions. | Imitation separation evaluation report (meaning/mechanism) |
| U13-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | Semantic restoration and mechanistic difference are easy to separate under control conditions. | Intervention protocol and rebuttal condition definition |
| U13-5 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | D03 Multimodal Fusion EEG + Eye-Tracking (10.21227/6106-6120 / immediate) | Shared EEG plus gaze streams keep the perception-to-recall branch analysis bounded and make decoder-transfer failure easier to interpret without overstating mechanism preservation. | Mimic separation evaluation script and control condition table |
| U13-6 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | It is easy to separate semantic restoration and mechanistic difference using control conditions. | Leak audit results and repartition trail |
| U14-1 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | It is easy to fix the operation of supplementary exam contracts, leak audits, and disclosure of negative cases. | Supplementary test operation report (including negative cases) |
| U14-2 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | D01 Acquisition delay of wireless EEG (10.21227/dv1p-vq18 / immediate) | A latency-first measurement package is sufficient to keep the exploration/confirmation split and rerun contract narrow, measurable, and public-safe. | Supplementary test operation report (including negative cases) |
| U14-3 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | It is easy to fix the operation of supplementary exam contracts, leak audits, and disclosure of negative cases. | Leak audit results and repartition trail |
| U14-4 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | D01 Acquisition delay of wireless EEG (10.21227/dv1p-vq18 / immediate) | The same latency/measurement anchor is enough to wire Model Card and Dataset Card fields into the rerun contract without claiming field-wide standardization. | Model/Dataset Card template and filled-in examples |
| U14-5 | B | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | It is easy to fix the operation of supplementary exam contracts, leak audits, and disclosure of negative cases. | Negative Example Registry First Edition (CSV+Operating Rules) |
| U14-6 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | It is easy to fix the operation of supplementary exam contracts, leak audits, and disclosure of negative cases. | Fixed container reproduction procedure manual and cost measurement |
| U15-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | Easy to connect to system audit indicators for safe shutdown and authority management. | System integrated audit report (suspension/renewal conditions) |
| U15-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | Easy to connect to system audit indicators for safe shutdown and authority management. | System audit requirements table (technical log compatible) |
| U15-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | Easy to connect to system audit indicators for safe shutdown and authority management. | System audit requirements table (technical log compatible) |
| U15-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | Easy to connect to system audit indicators for safe shutdown and authority management. | System audit requirements table (technical log compatible) |

## Additional information

- This page is a quick guide for "fixing submission operations." Please refer to `mind-upload-eeg-rq60-feasibility-and-funds` for details on the reasons for the decision.
- `C` In judgment RQ, limit claims to institutional requirements and audit requirements and avoid excessive performance claims.

## 2026-03-14 19:12 JST Added

- Re-scanned 60 RQs and fixed ``first application destination/preliminary application destination/main EEG-DATA/minimum deliverables'' for each RQ.
- The number of A/B/C (`17/25/18`) matches the original page.
- The purpose of this page is to avoid general summaries and make it possible to immediately execute `1RQ=1 submission decision`.

## 2026-03-15 10:02 JST revalidation log (after main run/pull)

- Re-verify in `main` after running `git pull --rebase --autostash` and re-check `RQ_TOTAL=60`.
- Compare this page with `mind-upload-rq60-deep-focus-notes.md` and confirm that the breakdown of `A/B/C=17/25/18` matches.
- `First application destination/preliminary application destination/main EEG-DATA/minimum deliverables'' of each RQ line is missing `0`, blank `0`.
- Grant real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is `auto-research-funds` Can be referenced on the side.
- Continuing the policy: fix `1RQ=1 submission judgment` instead of a general summary, and transfer directly to the application text in RQ units.

## 2026-03-15 12:02 JST re-verification log (fixed confirmation of this run/RQ unit submission decision)

- Double-checked `RQ_TOTAL=60` and `A/B/C=17/25/18`, which exactly match `mind-upload-eeg-rq60-feasibility-and-funds.md`.
- ``First applicant/Preliminary applicant/Main EEG-DATA/Minimum deliverable'' in all `RQ` lines is missing `0`, blank `0`.
- The reference ID of `main EEG-DATA` is `EEG-DATA/eeg_dataset_summary_ja.csv`, and all items exist (missing `0`).
- Grant real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is `auto-research-funds` / All items can be re-referenced with `grant_queue`.

</article>
</main>

## 2026-03-15 13:03 JST revalidation log (main run / application playbook consistency check)

- After re-inspecting this page after `main` pull, we confirmed that `1st applicant/Preliminary applicant/main EEG-DATA/Minimum deliverables' were missing `0` and blank `0` in all `60RQ` lines.
- `A/B/C=17/25/18` remains consistent with `mind-upload-eeg-rq60-feasibility-and-funds.md`.
- Grant key `G1-G6` Real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) Confirmed that it can be re-referenced in `auto-research-funds`.
- Leave the practical application unchanged: Instead of making it into a general theme, we will maintain the granularity that allows direct transcription to the application text with `1RQ=1 submission judgment`.

## 2026-03-15 16:03 JST revalidation log (after main run/submodule pull)

- After `main` pull, check the `RQ=60` line again and check the missing `0` of `First applicant/Preliminary applicant/Main EEG-DATA/Minimum deliverables`.
- Judgment breakdown `A/B/C=17/25/18` remains consistent with `mind-upload-eeg-rq60-feasibility-and-funds.md`.
- Continue to operate this page: `1RQ=1 submission judgment` is fixed, and the application text is posted in RQ units instead of general summaries.

## 2026-03-18 11:20 JST revalidation log (main run / playbook consistency refresh)

- Pulled latest `main` and fixed base commits to `mind-upload=d0a06cf30f2d`, `EEG-DATA=357cd9af4962`, `auto-research-funds=a6ffdb0898e8`.
- Re-checked this playbook with unique `Ux-y` keys and reconfirmed `60RQ` coverage (missing `0`, duplicate `0`).
- Reconfirmed `A/B/C=17/25/18` consistency against `mind-upload-eeg-rq60-feasibility-and-funds.md`.
- Re-verified grant keys `G1-G6` and confirmed each ID is still resolvable from `grant_queue` or `auto-research-funds` sources.
- Continued the same rule for execution and writing: keep `1RQ=1 submission decision` and transfer to applications in RQ units, not generic themes.

## 2026-03-18 12:08 JST revalidation log (main run / one-RQ execution guard)

- Rechecked this playbook row-by-row and reconfirmed `60RQ` coverage with no missing `Ux-RQy` line.
- Revalidated consistency with feasibility page: `A/B/C=17/25/18` unchanged.
- Revalidated grant IDs `G1-G6` in `grant_queue` and `auto-research-funds` sources.
- Because current `EEG-DATA/eeg_dataset_summary_ja.csv` has remapped numeric IDs, this page's numeric IDs are handled as search aids only.
- Submission-ready references are fixed to `DOI + dataset name + access class` from `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.
