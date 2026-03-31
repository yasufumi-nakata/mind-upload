---
layout: default
title: "Mind-upload RQ60 Deep focus notes (EEG-DATA × Grant)"
description: "A deep-dive note that fixes each of the 60 RQs, including the core, external requirements, and application themes that will be directly verified with EEG."
article_type: Wiki
subtitle: "Fix the issues for each RQ instead of a general summary"
author: Mind Uploading Research Project
last_updated: "2026-03-31"
note: "RQ-by-RQ Deep Focus"
audience: "People who want to translate each RQ directly into application statements and experimental procedures"
reading_time: "20-35 minutes"
page_intro: "This page is a practical note that fixes the core of mind-upload's 60 RQs, which can be confirmed directly with EEG-DATA, application themes for auto-research-funds, and necessary requirements outside of EEG."
accuracy_note: "A/B/C judgment is the same as mind-upload-eeg-rq60-feasibility-and-funds. C means 'not complete with EEG alone' rather than 'not important'."
wiki_links:
  - label: "Wiki: RQ60 EEG verification availability and subsidy theme"
    url: "/wiki/mind-upload-eeg-rq60-feasibility-and-funds.html"
    description: "The original version of the judgment and data candidates."
  - label: "Wiki: RQ60 Application Playbook"
    url: "/wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html"
    description: "Fixed table of applicant ID and minimum deliverables."
recommended_pages:
  - label: "Literature map"
    url: "/research_harvest_50.html"
  - label: "Data & Bench"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

## How to use

1. Select only one `RQ` and implement only the `core to be directly verified with EEG` in the table below first.
2. Copy the `application theme (grant key)` directly to the proposed application title.
3. Don't expand your claim unless you can satisfy the ``required outside the EEG''.
4. Numeric `ID` in this page is for search guidance only. Submission/reproducibility logs must use `DOI + dataset name + access class` in the canonical map `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.

## Meaning of judgment

- `A`: Main claims can be verified with EEG-DATA only.
- `B`: EEG main analysis is possible. Requires additional external modality/design.
- `C`: Mainly system/legal/theoretical integration. EEG is an audit log or supporting evidence.

## Latest post-pull hold (2026-03-31 16:05 JST)

- A latest pull reread after `mind-upload@a11240d38415`, `EEG-DATA@f318ac8ce42d`, and `auto-research-funds@c95cc61fdfc9` still leaves the current public six-question batch and the solve-first order unchanged.
- The newest deltas widen the support map, not the current practical batch: `mind-upload` tightened the connectome / timing-state route cards, `EEG-DATA` added an `OSF eucqf` deep-dive refresh, and `auto-research-funds` added new `Takeda / Nohken` funding-card material, but none of those changes replace the current `D10 / D03 / D02 / D01` family or the outside-current-six order `U7-1 -> U1-2 -> U4-2 -> U8-1`.
- Browser-level live checks still returned `200` for `issue.html`, `mind-upload-current-public-six-rq-brief.html`, and `u8-1-closed-loop-delay-tolerance-route.html`, so this run does not add new public prose.
- The Todoist full-item audit still showed enough family coverage (`items=205`, `Kura=2`, `Nakatani family=11`, `Kashinome=2`, `Secom family=3`, `AI for Aging-Society Problem Solving=0`), so no new task was added.

## Overnight revalidation hold (2026-03-31 00:04 JST)

- This run rechecked the live public route, the current official funding windows, and a Todoist full-item audit after the latest `EEG-DATA` upstream additions.
- The current public six-question batch still stays `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2`, and the solve-first order still stays `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`.
- The newest upstream `EEG-DATA` additions remain outside the current speech / identity / reproducibility anchor family, so they do not replace `D10` as the only clearly public-open primary anchor and do not turn `D03/D02/D01` into immediate public routes.
- Funding-window recheck in this run still supports the same narrow route: `Kura Fund` remains open through `2026-04-17 17:00`, the `Nakatani Foundation graduate scholarship` still runs `2026-04-01 - 2026-05-25 15:00`, the `Kashinome Scholarship` remains open through `2026-04-09`, and `Secom General Research Grant` remains a watch route through `2026-03-31 12:00`.
- A March 31 access audit at `2026-03-31 00:20 JST` also means earlier March 30 notes that called `D03/D02/D01` immediate public anchors should now be read as superseded. Those three stay only as subscription-gated support anchors on the public route.
- Todoist still did not need a new item in this run. The full-item audit continues to show the relevant family coverage already present (`Kura=2`, `Nakatani family=11`, `Kashinome=2`, `Secom family=3`, `AI for Aging-Society Problem Solving=0`).

## Dawn revalidation note (2026-03-31 05:05 JST)

- A fresh `pull --ff-only` recheck still leaves `mind-upload`, `auto-research-funds`, and the active `EEG-DATA` workspace aligned with `origin/main`, so this run adds no hidden upstream batch switch.
- A live reread of `https://mind-upload.com/issue.html` still shows the same public six, the same execution order, and the same route-hold framing, so the public source page itself did not need new prose in this run.
- Direct access rechecks now reconfirm the anchor split more concretely: `D10 3M-CPSEED` remains public-open on OpenNeuro, while the current IEEE DataPort pages for `D03`, `D02`, and `D01` still show `LOGIN TO ACCESS DATASET FILES` plus `Subscription Required`, so those three remain subscription-gated support anchors rather than immediate public anchors.
- A same-run official-window reread still supports the same narrow funding bridge: `Kura Fund = 2026-04-17 17:00`, `Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`, `Kashinome = 2026-04-09`, and `Secom General Research Grant = 2026-03-31 12:00`.
- A same-run Todoist sync audit still finds the practical route already covered (`Kura=2`, `Nakatani graduate=5`, `Nakatani research=3`, `Kashinome=2`, `Secom=3`), so no new task was added.

## Post-pull revalidation hold (2026-03-30 00:11 JST)

- This run pulled `mind-upload@836d4db`, `EEG-DATA@25f065735da`, and `auto-research-funds@7619c14a2`, then rechecked the live public page plus the current official funding windows.
- The current public six-question batch still stays `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2`, and the solve-first order still stays `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`.
- The practical reason for holding the batch is unchanged: the narrowest current bridge from `mind-upload.com` RQs to bounded EEG-ready and fundable work still runs through `inner-speech decoding + identity drift + reproducibility auditing`, not through a broader thematic spread.
- Anchor strength also stays conservative after the pull. `D10 3M-CPSEED` and `D02 CSTE` remain the strong primary anchors, while `D03 Multimodal Fusion EEG + Eye-Tracking` and `D01 Acquisition delay of wireless EEG` remain bounded-support anchors with lower claim ceilings.
- Funding-window recheck in this run: `Kura Fund` remains open through `2026-04-17 17:00`, the `Nakatani Foundation graduate scholarship` opens `2026-04-01` and closes `2026-05-25 15:00`, the `Kashinome Scholarship` remains open through `2026-04-09`, the `Secom General Research Grant` remains an urgency watch route through `2026-03-31 12:00`, and the `Nakatani Foundation research grant` remains `next-cycle watch`.
- Large social-deployment programs such as `AI for Aging-Society Problem Solving` remain outside this current EEG-first route, because their required output is a scaled public deployment program rather than a `one-RQ / one-anchor / one-first-artifact` EEG result.

## Public-safe closure gates for the current batch (2026-03-30 02:05 JST)

- This run rechecked the live public page, the current official funding windows, and Todoist in read-only mode. The batch itself still does not change.
- What does change here is the wording of `what counts as real progress right now`: not a stronger claim, but a narrower `first artifact` for each of the six current public RQs.

| RQ | What can honestly move forward now | Why the current anchor is enough for that next step | First artifact to close next | Keep outside the public claim |
|---|---|---|---|---|
| `U13-2` | Fix the `brain-minus-prior` control family before any stronger decoder wording. | `D10 3M-CPSEED` already gives overt / silent-intended / imagined speech, repeated sessions, and transcript-aligned phases, so it is sufficient for a bounded hallucination / inconsistency audit. | `Brain-minus-prior control table and mimic-separation note` | Do not treat decoder success as preserved internal state or mind preservation. |
| `U13-5` | Freeze only the perception-to-recall branch point, not a general mechanism claim. | `D03 Multimodal Fusion EEG + Eye-Tracking` is enough to keep the transfer-gap interpretation bounded because the shared EEG + gaze streams let the branch stay tied to a concrete perception/recall shift. | `Perception-to-recall degradation note and transfer-gap table` | Do not present a shared decoder as evidence of preserved internal mechanism. |
| `U0-2` | Close the timing budget that prevents identity-like wording from absorbing measurement error. | `D02 CSTE` already has repeated sessions, cross-task labels, and timestamp/QC structure, so it is enough to lock `clock offset + jitter + state-feature collapse` into one narrow audit. | `Offset/jitter distribution and state-feature collapse audit` | Do not elevate synchronization stability into legal or philosophical identity continuity. |
| `U0-3` | Fix the threshold-selection rule only after the timing route is bounded. | The same `D02 CSTE` anchor lets threshold stability and overfit exclusion stay on the same cross-session / cross-task identity-drift floor as `U0-2`. | `Threshold-stability note and overfit-exclusion rule` | Do not treat a stable biometric threshold as a sufficient condition for personhood continuity. |
| `U14-4` | Freeze the disclosure fields that the current batch actually needs for reruns. | `D01 Acquisition delay of wireless EEG` is narrow enough to turn Model Card / Dataset Card items into a rerun checklist without overclaiming field-wide standardization. | `Filled Model Card / Dataset Card examples for the current public batch` | Do not claim organizational adoption or community-wide standardization yet. |
| `U14-2` | Make the exploration/confirmation split operational rather than aspirational. | The same `D01` latency-first route is enough to define a fixed split plus rerun boundary, even though it is still too narrow for broader reproducibility claims. | `Fixed-split rerun contract and negative-case trail` | Do not present exploratory outputs as confirmatory evidence after the split boundary is crossed. |

- Official-window recheck in this run stayed conservative: `Kura Fund` remains open through `2026-04-17 17:00`, the `Nakatani Foundation graduate scholarship` detail page still shows `2026-04-01 - 2026-05-25 15:00`, the `Kashinome Scholarship` remains open through `2026-04-09`, and `Secom General Research Grant` remains a watch route through `2026-03-31 12:00`.
- Todoist read-only recheck found the current route already covered by existing tasks, including `Kura Fund`, `Nakatani Foundation graduate scholarship`, `Kashinome Scholarship`, `Nakatani Foundation research grant`, and `Secom`. No new task was added in this run.

## Current public six-question batch (2026-03-29 10:09 JST)

This run changes the active public batch to `U13-2`, `U13-5`, `U14-4`, `U0-2`, `U0-3`, and `U14-2`.

This is a route-setting update, not a solved-claim update. The public batch is now intentionally concentrated on `inner-speech decoding + identity drift + reproducibility auditing`, because these six RQs are the cleanest current bridge from `mind-upload.com` research questions to bounded EEG-ready and fundable work packages.

| RQ | What is fixed first | Main `Dxx + DOI` anchor | Practical first / backup route | First-pass KPI | Keep outside the EEG claim |
|---|---|---|---|---|---|
| `U13-2` | A `brain-minus-prior` hallucination audit for overt/silent/imagined speech. | `D10` / `10.18112/openneuro.ds006465.v2.0.0` | `Kura Fund` / `Nakatani Foundation graduate scholarship` | `semantic alignment` `brain-minus-prior gap` `misalignment rate` | Do not treat language-decoder success as a mind-preservation claim. |
| `U13-5` | A perception-to-recall branch analysis for mimicry/mechanism separation. | `D03` / `10.21227/6106-6120` | `Kura Fund` / `Nakatani Foundation graduate scholarship` | `perception-to-recall degradation point` `transfer gap` `control-condition stability` | Do not treat a shared decoder as evidence of preserved internal mechanism. |
| `U14-4` | Model Card / Dataset Card fields are wired into the reproducibility contract. | `D01` / `10.21227/dv1p-vq18` | `Kura Fund` / `Nakatani Foundation research grant (watch)` | `required-card fill rate` `rerun success rate` `leak-audit coverage` | Do not claim organizational adoption or field-wide standardization yet. |
| `U0-2` | The identity route is limited to `clock offset + jitter + state-feature collapse` auditing. | `D02` / `10.21227/j162-nh61` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` | `clock-offset p95` `state-feature collapse rate` `resync recovery rate` | Do not elevate technical synchronization stability to legal or philosophical identity. |
| `U0-3` | Task-specific threshold stability and overfit exclusion are fixed before any stronger identity reading. | `D02` / `10.21227/j162-nh61` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` | `session-out AUC` `threshold stability` `overfit exclusion rate` | Do not treat a stable biometric threshold as a sufficient condition for personhood continuity. |
| `U14-2` | Exploratory and confirmatory tracks are separated inside the rerun contract. | `D01` / `10.21227/dv1p-vq18` | `Kura Fund` / `Nakatani Foundation research grant (watch)` | `fixed-split rate` `rerun success rate` `explore-to-confirm carryover gap` | Do not present exploration outputs as confirmatory evidence after the split boundary is crossed. |

- Practical funding alignment in this run is intentionally narrow: `Nakatani Foundation graduate scholarship`, `Kura Fund`, `Kashinome Scholarship (student-runway only)`, and `Nakatani Foundation research grant` already provide active routes or watch routes for this cluster.
- Relevant Todoist tasks already existed before this run, so no new task was needed for the current practical shortlist.
- Funding-window spot check (2026-03-29): `Kura Fund` remains open in the current cycle, the `Nakatani Foundation graduate scholarship` remains the main student-facing bridge for this batch, the `Kashinome Scholarship` stays only as a student-runway side route rather than a core EEG research-funding anchor, and the `Nakatani Foundation research grant` plus broader neuroscience routes stay in watch mode.

## Anchor strength and uncovered roadmap families (2026-03-29 15:15 JST)

- The current six-question batch does not change here. What changes is the explicit reading order for the anchors: `D10` and `D02` are the strongest current primary anchors, while `D03` and `D01` stay in the batch as bounded route-setting anchors with narrower claim ceilings.
- Practical consequence: `U13-2/U0-2/U0-3` can carry stronger first-pass artifacts inside EEG-DATA alone, while `U13-5/U14-4/U14-2` should remain attached to narrower artifacts until either the DOI-based source package is exercised more deeply or an adjunct benchmark is added.
- Submission and reproducibility references remain fixed to `Dxx + DOI + dataset name + access class`. Numeric IDs stay search-only because the local mirror keeps re-ranking and remapping those IDs.
- There is also a structural backlog outside this six-question batch: `U2/U5/U6/U9` exist in `tech_roadmap.md`, but they are not yet translated into the current `RQ60` practical pages. They should be treated as the next internal translation queue rather than as an already-covered part of the public six.

## Solve-first order after the post-pull revalidation (2026-03-29 14:06 JST)

This run does not change the public six-question batch. It only fixes the execution order more explicitly, so the work can proceed as `one-RQ / one-anchor / one-first-artifact` instead of drifting back into a broad summary.

The order below is intentionally sequential. Each row closes a blocker for the next row rather than treating the six questions as one blended benchmark.

| Order | RQ | Why this comes before the next one | Main anchor / access | First artifact to finish | Practical route now |
|---|---|---|---|---|---|
| `1` | `U13-2` | It is the shortest route to test whether the neural signal adds anything beyond the language prior. If this fails, stronger speech-decoder wording stays blocked. | `D10` / `10.18112/openneuro.ds006465.v2.0.0` / `immediate` | `Mimic separation evaluation script and brain-minus-prior control table` | `Kura Fund` / `Nakatani Foundation graduate scholarship` |
| `2` | `U13-5` | It becomes meaningful only after `U13-2` fixes the control family. Then the perception-to-recall branch point can be read as a bounded mechanism split rather than a generic decoder score. | `D03` / `10.21227/6106-6120` / `subscription-gated support` | `Perception-to-recall degradation note and transfer-gap table` | `Kura Fund` / `Nakatani Foundation graduate scholarship` |
| `3` | `U0-2` | Identity-like wording remains unsafe until synchronization drift is audited at the millisecond level. This is the first hard ceiling for the continuity route. | `D02` / `10.21227/j162-nh61` / `subscription-gated support` | `Offset/jitter distribution and state-feature collapse audit` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` |
| `4` | `U0-3` | Threshold stability only becomes interpretable after `U0-2` fixes the timing budget. Otherwise the threshold can absorb synchronization error. | `D02` / `10.21227/j162-nh61` / `subscription-gated support` | `Threshold search notebook and overfit-exclusion rule` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` |
| `5` | `U14-4` | Card requirements should be frozen only after the speech and identity rows stabilize what must actually be disclosed. | `D01` / `10.21227/dv1p-vq18` / `subscription-gated support` | `Filled Model Card / Dataset Card examples for the current public batch` | `Kura Fund` / `Nakatani Foundation research grant (watch)` |
| `6` | `U14-2` | The exploration/confirmation split is the last step because it depends on the artifact family above being stable enough to rerun without ad hoc reinterpretation. | `D01` / `10.21227/dv1p-vq18` / `subscription-gated support` | `Fixed-split rerun contract and negative-case trail` | `Kura Fund` / `Nakatani Foundation research grant (watch)` |

- Live public check in this run: `mind-upload.com/issue.html` still presents the same six RQs and still labels them as a `route-setting update`, so the public source page itself does not need a new batch switch.
- Anchor reality recheck in this run: `D10 = 3M-CPSEED` (`10.18112/openneuro.ds006465.v2.0.0`, `immediate`), while `D03 = Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments: An EEG and Eye-Tracking Study` (`10.21227/6106-6120`, `subscription-gated support`), `D01 = Acquisition delay of wireless EEG` (`10.21227/dv1p-vq18`, `subscription-gated support`), and `D02 = CSTE` (`10.21227/j162-nh61`, `subscription-gated support`) remain in the current route only as gated support anchors. These four anchors still define the current execution floor for the batch, but only `D10` currently counts as a clearly public-open primary anchor.
- Funding-window recheck in this run: `Kura Fund` stayed open, the `Nakatani Foundation graduate scholarship` stayed the main student-facing bridge, the `Kashinome Scholarship` stayed a runway-only side route, and the `Nakatani Foundation research grant` stayed in watch mode.
- Todoist recheck in this run: the start/deadline tasks for these routes already existed, so no duplicate task was added.

## Post-pull hold after the route-taxonomy update (2026-03-29 17:10 JST)

- This run pulled the latest upstream route-taxonomy update and rechecked whether it changes the current public six-question batch. It does not. The public route remains `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2`, and the solve-first order remains `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`.
- The practical reason for holding the batch is unchanged: the cleanest current bridge from `mind-upload.com` questions to bounded EEG-ready work still runs through `inner-speech decoding + identity drift + reproducibility auditing`, not through a broader thematic spread.
- Anchor strength also remains unchanged after the pull. `D10` and `D02` stay the strong primary anchors for first-pass artifacts, while `D03` and `D01` remain bounded-support anchors whose outputs should keep a narrower claim ceiling.
- The upstream route-taxonomy tightening is still useful, but its immediate effect is internal rather than public-facing. It sharpens backlog translation and claim ceilings around uncovered roadmap families; it does not justify a new public batch switch or stronger solved-claim wording.
- Funding and task routing also stay conservative in this run. `Kura Fund` and the `Nakatani Foundation graduate scholarship` remain the practical first routes, `Kashinome Scholarship` stays runway-only support, `Nakatani Foundation research grant` stays next-cycle watch, and no new Todoist task is needed because the current practical routes are already covered by existing tasks.

## Next internal six-question queue (2026-03-29 11:10 JST)

The public batch above does not change in this run. This section only records the next bounded queue once the current public six have stable audit artifacts.

The rule stays the same: no broad thematic expansion, and no solved-claim wording. Each row below is a `one-RQ / one-anchor / one-minimum-deliverable` continuation that stays close to the current `inner-speech decoding + identity drift + reproducibility auditing` bundle.

| RQ | Why it is next | Main `Dxx + DOI` anchor | Minimum deliverable | Keep outside the EEG claim |
|---|---|---|---|---|
| `U13-1` | It is the nearest unresolved split after `U13-2/U13-5`: `semantic restoration` must be separated from `causal restoration`. | `D10` / `10.18112/openneuro.ds006465.v2.0.0` | `Intervention protocol and rebuttal condition definition` | Do not read semantic-match success as preserved internal mechanism. |
| `U13-3` | It extends the same inner-speech cluster to the `same output / different mechanism` failure mode. | `D10` / `10.18112/openneuro.ds006465.v2.0.0` | `Imitation separation evaluation report (meaning/mechanism)` | Do not treat output equivalence as causal equivalence. |
| `U14-3` | It is the cleanest next reproducibility step after `U14-2/U14-4`: leaderboard leak and report-bias auditing. | `D719` / leaderboard leak benchmark anchor used in the RQ dossier | `Leak audit results and repartition trail` | Do not present internal leaderboard robustness as field-wide validation. |
| `U7-3` | It fixes when preprocessing drift becomes release-block relevant instead of a mere implementation detail. | `D11` / `10.18112/openneuro.ds007216.v1.0.0` | `Reproducibility audit report (synchronization/QC/preprocessing difference)` | Do not generalize one preprocessing audit rule beyond its tested protocol family. |
| `U1-2` | It is the next strongest `A` candidate near the same verification stack: uncertainty calibration for inverse estimates. | `D08` / `10.21227/7may-9q56` | `Inverse problem reproduction report (error/uncertainty)` | Do not promote interval coverage stability into a blanket guarantee across all head models. |
| `U14-1` | It turns rerun requirements into an executable contract before broader standardization claims. | `D01` / `10.21227/dv1p-vq18` | `Supplementary test operation report (including negative cases)` | Do not claim community-wide agreement on the required rerun pack. |

- Funding-wise, the next internal queue splits into two states on purpose: `U7/U14` already have concrete reproducibility-facing watch routes, while `U13/U1` still lean on `G4`-style neuroscience watch routes where the near-term public call signal is weaker.
- Todoist-wise, no new task is required just because a row appears here. A task is only added when an actual `watch / start-date / deadline` route is concrete enough to avoid duplication.

## U0 (identity)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U0-1 | A | Two-axis ROC that separates observation matching and intervention response matching | Necessary/sufficient condition design for identity KPI (G2/G3) | 11, 29, 696 | Normative definition of personality identity |
| U0-2 | A | Correspondence coefficient between ms synchronization deviation and state representation collapse | Standardization of time synchronization audit criteria (G2/G3) | D02 CSTE (`10.21227/j162-nh61`, subscription-gated support); adjunct: ds004148, ds007216 | Inter-sensor clock calibration regular agreement |
| U0-3 | A | External verification difference between task-specific thresholds and overfitting exclusion | Individual identification method with generalized threshold (G2/G3) | D02 CSTE (`10.21227/j162-nh61`, subscription-gated support); adjunct: ds004148, ds007216 | Screening rules for threshold selection |
| U0-4 | B | Lower limit evaluation of technical ID stability after branching | Procedure for determining identity of branching entity (G2/G3) | 11, 29, 696 | Legal entity definition/responsibility allocation |

## U1 (inverse problem)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U1-1 | A | Position error and recall for each prior distribution | Inverse problem prior distribution bench (G1/G4) | 56, 676, 1839 | Model selection rules |
| U1-2 | A | Uncertainty propagation of conductivity/electrode defects/noise injection | Inverse estimation with uncertainty calibration (G1/G4) | 56, 676, 1839 | Head model identification conditions |
| U1-3 | B | Deviation rate distribution of MNE/beamformer/Champagne | Decision rule that allows method deviation (G1/G4) | 56, 676, 1839 | Inter-method agreement protocol |
| U1-4 | B | Estimated values and reanalysis concordance rate when releasing backward distribution | Establishment of standards for publishing backward distribution (G1/G4) | 56, 676, 1839 | Scope of disclosure and anonymization decision |

## U3 (boundary extension)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U3-1 | B | Predictive improvement of EEG alone vs. integrated model | Estimated effect size of boundary expansion (G2/G6) | 13, 16, 39 | Additional modality collection |
| U3-2 | B | Lower bound of correlation between connectome proxy and functional prediction | Cross-species comparison design study (G2/G6) | 13, 16, 39 | Cross-species connectome data |
| U3-3 | B | Performance deterioration when removing the body/environment loop | Verification of necessity of body connection (G2/G6) | 13, 16, 39 | Real environment intervention log |
| U3-4 | C | Fixed only the proxy KPI for the required minimum configuration | System design for determining the minimum configuration (G2/G6) | 13, 16, 39 | Agreement on theory adoption criteria |
| U3-5 | C | Search for alternative indicators under unobserved glymphatic conditions | Preparatory research on body fluid system integration (G2/G6) | 13, 16, 39 | Metabolic/body fluid measurement data |
| U3-6 | C | Extraction of short-term failure signs of immune surveillance exclusion model | Design of long-term failure monitoring (G2/G6) | 13, 16, 39 | Longitudinal data on inflammation and immunity |

## U4 (causal)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U4-1 | B | Sign discrepancy rate between correlation estimation and intervention effect | Formulation of correlation → causal transfer conditions (G1/G4) | 19, 56, 1839 | Ethical review of intervention design |
| U4-2 | A | Reproducibility of minimal intervention claim | Ground-truth causal verification (G1/G4) | 19, 56, 1839 | Stopping rule when intervention fails |
| U4-3 | B | Counterfactual error comparison of DCM/active inference | Single design comparison of theoretical predictions (G1/G4) | 19, 56, 676 | Common I/O specifications between theories |
| U4-4 | B | Falsification threshold (ΔAUC/sign reversal rate) | Evaluation contract with falsification precedent (G1/G4) | 19, 56, 1839 | Operating rules for failure declaration |

## U7 (Standardization/Reproducibility)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U7-1 | A | Missing rate of synchronization/QC/stimulation log required items | BIDS extended audit infrastructure (G1/G3) | 676, 783, 4878 | Organizational adoption of standard specifications |
| U7-2 | A | LSL synchronization error jitter distribution and threshold | Synchronization error automatic warning operation (G1/G3) | 676, 783, 4878 | Inter-device calibration SOP |
| U7-3 | A | Results drift due to preprocessing setting differences | Establishment of preprocessing audit CI (G1/G3) | 676, 783, 4878 | CI operation governance |
| U7-4 | A | Re-measurement judgment tree in case of alignment failure | Operational criteria for re-measurement/exclusion (G1/G3) | 676, 783, 4878 | Measurement re-execution cost plan |
| U7-5 | A | False block rate against release block threshold | Stopping rule for decreasing recall rate (G1/G3) | 676, 783, 4878 | Release responsibility system |
| U7-6 | A | Conclusion preservation rate under missing modality | Minimum observation set design (G1/G3) | 676, 783, 4878 | Clinical operational standards when missing |

## U8 (closed loop operation)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U8-1 | B | Stability rate/recovery time against delay changes | Identification of closed-loop delay tolerance range (G2/G5) | 6, 1972, 2412, 696 | Design of mounted system controller |
| U8-2 | B | Online calibration frequency and performance maintenance rate | Optimization of concept drift countermeasures (G2/G5) | 6, 1972, 2412, 696 | Continuous operation infrastructure |
| U8-3 | B | Variance decomposition of individual differences and diurnal variation | Long-term stability KPI design (G2/G5) | 6, 1972, 2412, 696 | Long-term tracking protocol |
| U8-4 | B | Abnormality detection delay and failsafe activation rate | Safe shutdown evaluation contract (G2/G5) | 6, 1972, 2412, 696 | Safety procedures at operational sites |
| U8-5 | B | Malfunction rate and recovery time during override | Human-in-the-loop evaluation (G2/G5) | 6, 1972, 2412, 696 | Operator training and demarcation of responsibility |
| U8-6 | B | Trade-off curve between relearning interval and safety margin | Relearning scheduling (G2/G5) | 6, 1972, 2412, 696 | MLOps update control |

## U10 (Information Thermodynamics)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U10-1 | C | Audit consistency with theoretical formula using proxy | Neural calculation and Landauer consistency (G2/G6) | 735, 783, 1011 | Direct measurement of heat dissipation |
| U10-2 | C | Weak correlation between nonequilibrium index and information efficiency proxy | Verification design of nonequilibrium index definition (G2/G6) | 735, 783, 1011 | Simultaneous measurement with metabolic measurement |
| U10-3 | C | Observation design validity of neural activity + metabolic proxy | Observation design template construction (G2/G6) | 735, 783, 1011 | Metabolic/temperature sensor integration |
| U10-4 | C | Theoretical consistency check for calculation cost evaluation | WBE cost evaluation with thermal constraints (G2/G6) | 735, 783, 1011 | Actual measurement data on WBE implementation side |

## U11 (awareness index)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U11-1 | B | PCI approximation/LZ/wSMI rank preservation rate | Unification of theoretical cross-sectional I/O specifications (G2/G4) | 735, 842, 859 | Clinical operation acceptance criteria |
| U11-2 | C | Comparison of approximation indicators within calculation budget | Evaluation of calculation amount constraints for IIT approximation (G2/G4) | 735, 842, 859 | Exact IIT calculation platform |
| U11-3 | B | Single-condition comparison of theoretical conflicting points | Single experimentalization of theoretical conflicting points (G2/G4) | 735, 842, 859 | Joint experimental design agreement |
| U11-4 | B | Advance declaration of failure conditions including false positives/false negatives | Definition of failure conditions for awareness indicators (G2/G4) | 735, 842, 859 | Clinical responsibility division and accountability |

## U12 (principal/responsibility)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U12-1 | C | Technical stability log of post-branch ID | Audit design of branch ID (G2/G6) | 11, 509, 696 | Legal ID granting criteria |
| U12-2 | C | Technical Event Log for Succession Points | Responsibility/Rights/Consent Succession Rules (G2/G6) | 11, 509, 696 | Institutional Branching Rules |
| U12-3 | C | Change audit of psychological continuity proxy | Connection of psychological standards and legal standards (G2/G6) | 11, 509, 696 | Normative judgment frame |
| U12-4 | C | Correspondence log between performance KPI and attribution KPI | Connection between performance evaluation and personality evaluation (G2/G6) | 11, 509, 696 | Judicial/Ethical Review |
| U12-5 | C | Extracting ID reorganization candidates during resynchronization events | ID reorganization criteria during memory editing (G2/G6) | 11, 509, 696 | Personal consent and legal validity |
| U12-6 | C | Delayed audit of authority reflection after consent withdrawal | Consent withdrawal and authority revocation audit (G2/G6) | 11, 509, 696 | Access control system design |

## U13 (Decoding and imitation separation)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U13-1 | B | Discrepancy between semantic matching rate and causal matching rate | Separate evaluation of meaning restoration/causal reproduction (G1/G4) | 509, 13, 65 | External behavior/language evaluation system |
| U13-2 | B | Correlation between hallucination test results and neural state differences | Neural decoding connections for hallucination tests (G1/G4) | D10 3M-CPSEED (`10.18112/openneuro.ds006465.v2.0.0`, immediate); adjunct: D03, D09 | LLM evaluation platform collaboration |
| U13-3 | B | Identification rate of the same output and different internal mechanisms | Shortcut detection bench (G1/G4) | 509, 13, 65 | Model internal visualization platform |
| U13-4 | B | Effect of prohibiting passing based on imitation score alone | Imitation evaluation with causal consistency (G1/G4) | 509, 13, 65 | Causal intervention design |
| U13-5 | B | Degradation branch point estimation from perception to recall | Perception/recall decoder branch analysis (G1/G4) | D03 Multimodal Fusion EEG + Eye-Tracking (`10.21227/6106-6120`, subscription-gated support); adjunct: D10, D09 | Unification of task design |
| U13-6 | B | Prompt induction/leak/shortcut separation rate | Leak audit with controlled experiment (G1/G4) | 509, 13, 65 | Data management governance |

## U14 (Operation/Audit)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U14-1 | A | Follow-up success rate for each fixed granularity | Minimum granularity definition for reproduction contract (G1/G3) | 6, 56, 719 | Contract document template |
| U14-2 | A | Recall rate difference when separating exploration/verification | Operational separation of exploration and verification (G1/G3) | D01 Acquisition delay of wireless EEG (`10.21227/dv1p-vq18`, subscription-gated support); adjunct: D08, D13 | Research management process |
| U14-3 | A | Subject/time series leak detection rate | leaderboard audit operation (G1/G3) | 6, 56, 719 | Enforcement of publication rules |
| U14-4 | A | Differences in ease of auditing with and without Card description | Model/Dataset Card contracting (G1/G3) | D01 Acquisition delay of wireless EEG (`10.21227/dv1p-vq18`, subscription-gated support); adjunct: D08, D13 | Legal preparation for evaluation contracts |
| U14-5 | B | Retry improvement rate with negative example registry | Negative example disclosure and retry cycle (G1/G3) | 6, 56, 719 | Disclosure consent/anonymization operation |
| U14-6 | A | Cost increase due to container fixation | Setting the maximum allowable reproduction cost (G1/G3) | 6, 56, 719 | Computing resource procurement plan |

## U15 (Regulations/neurorights)

| RQ | Judgment | Core to be directly verified with EEG | Application theme (grant key) | Main EEG-DATA | Required outside of EEG |
|---|---|---|---|---|---|
| U15-1 | C | Technical logging of neural data sensitivity | Neural data law concept mapping (G2/G6) | 49, 2412, 3419 | Official definition of legal concepts |
| U15-2 | C | Correspondence between neurorights items and technical audit logs | Neurorights audit itemization (G2/G6) | 49, 2412, 3419 | Consistency with regulatory agency requirements |
| U15-3 | C | Differences in technical items for requirements by jurisdiction | EU/US/JP minimum common operational definition (G2/G6) | 49, 2412, 3419 | Legal review of each jurisdiction |
| U15-4 | C | Risk indicator candidates linked to suspension/renewal conditions | Governance of suspension conditions/renewal conditions (G2/G6) | 49, 2412, 3419 | Design of operation supervision system |

## Practical notes (things fixed on this page)

- For all `60RQ`, `core to be verified directly with EEG` and `required outside of EEG` are listed separately.
- `Application theme` is unified to the existing grant key of `G1-G6`.
- The operating rule is `1RQ = 1 verification proposition = 1 application theme = 1 main data`.

## 2026-03-15 13:18 JST revalidation log (main run)

- Re-verify `mind-upload/research_harvest_50.md` as the original and check the number of lines in `Ux-RQy` is `60`, duplicate `0`, and missing `0`.
- Recalculated the judgment breakdown `A/B/C=17/25/18` and confirmed that it is consistent with each line on this page.
- The referenced EEG data ID (`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`) is `EEG-DATA/eeg_dataset_summary_ja.csv` All cases above exist (missing `0`).
- The real ID of subsidy key `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is All items can be viewed on the `auto-research-funds` side.
- The policy continues: Instead of a general overview, we maintain a deep-dive operation of `1 RQ = 1 verification proposition = 1 application theme = 1 main data`.

## 2026-03-15 09:03 JST revalidation log (after main run/pull)

- `main` Recounted after updating and reconfirmed `RQ_TOTAL=60`, `A/B/C=17/25/18` (matched both on this page and `mind-upload-eeg-rq60-feasibility-and-funds.md`).
- Re-extracted the `research question decomposition` section of `research_harvest_50.md` as the original, `RQ_COUNT=60`, missing `0`.
- The EEG data ID (`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`) referenced on this page is `EEG-DATA/eeg_dataset_summary_ja.csv` All cases exist (missing `0`).
- Grant ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) All can be viewed at `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`, `grant_queue/*.yaml`, and `auto-research-funds/grant_eeg_dataset_match.csv`.

### Latest 6 questions to dig deeper into one question at a time (fixed order of execution)

1. `U8-1` Closed loop delay tolerance range identification: `Main data = 6`, application destination `G2` (preliminary `G5`)
2. `U8-2` Online calibration and drift countermeasures: `Main data = 696`, application destination `G2` (preliminary `G5`)
3. `U14-1` Fixed granularity and supplementary exam success rate: `Main data = 56`, application destination `G1` (preliminary `G3`)
4. `U14-3` Leak audit operation: `Main data = 719`, application destination `G1` (preliminary `G3`)
5. `U7-2` Time synchronization error audit: `Main data = 6`, application destination `G1` (preliminary `G3`)
6. `U13-1` Separation of semantic agreement and causal agreement: `Main data = 509`, applicant `G1` (preliminary `G4`)

Reasons for proceeding in this order:
- It is easy to reach "actual KPI + failure conditions + application draft" within 4 weeks with `A/B` judgment.
- It will be easier to pass the `C` judgment (system-driven) if you submit it at a later stage based on these 6 actual measurement logs.

## 2026-03-15 12:02 JST re-verification log (main run / deep digging target fixed)

- Reconfirmed `RQ_TOTAL=60` and `A/B/C=17/25/18` and confirmed that they match the number of `RQ` lines on this page.
- All IDs referenced in the `main EEG-DATA` column exist in `EEG-DATA/eeg_dataset_summary_ja.csv` (missing `0`).
- All real IDs of grant keys `G1-G6` can be viewed on the `auto-research-funds` side.
- Continue to operate this page: Dig deeper into each case and clarify the ``key things that need to be verified directly with EEG'' and ``required things outside of EEG,'' and avoid general summaries.

</article>
</main>

## 2026-03-15 13:03 JST re-verification log (main run / continued deep digging operation)

- After `main` pull, we reconfirmed `RQ_TOTAL=60` and `A/B/C=17/25/18` and confirmed that they are consistent with the `RQ` line on this page.
- We reconfirmed that all EEG data IDs referenced on this page exist (missing `0`) in `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Grant real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is `auto-research-funds` I reconfirmed that all items can be viewed on the side.
- The policy will continue: Instead of a general overview, we will maintain ``1 RQ = 1 verification proposition = 1 application theme = 1 main data'' and give priority to in-depth description of each RQ.

## 2026-03-15 14:03 JST Re-verification log (main run / re-confirmation of all RQ deep digging fixed)

- We re-counted the `RQ` line in `mind-upload/wiki/mind-upload-rq60-deep-focus-notes.md` and confirmed `60` (`A/B/C=17/25/18`).
- In all `RQ` lines, `Application theme (grant key)` has been assigned to one of `G1-G6`, and we confirmed that there is a blank `0`.
- There are 24 types of data IDs referenced in the `main EEG-DATA` column (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`), we confirmed the missing `0` on `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Grant real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is `auto-research-funds` I confirmed that it can be re-referenced under it.
- The policy remains unchanged. Rather than general summaries, we will continue to deeply dig into ``1 RQ = 1 verification proposition = 1 application theme = 1 main data.''

## 2026-03-15 16:22 JST Deep implementation card (execute 6RQ one by one)

- Policy: We did not comprehensively update all RQs, but fixed the 6 RQs that are most likely to be implemented "in depth one by one" to the execution plan.
- Target: `U8-1`, `U8-2`, `U14-1`, `U14-3`, `U7-2`, `U13-1` (maintains the previously fixed priority order).

| RQ | Nucleus that can be solved with EEG-DATA (fixed for this time) | Two-week initial experiment (one experiment each) | Application theme (grant key) | EEG-DATA to be used (main/preliminary) | Pass/fail gate (conditions for proceeding to the next) |
|---|---|---|---|---|---|
| U8-1 | Identify the relationship between stability rate and recovery time when closed-loop delay is manipulated. | The same preprocessing pipeline was fixed with a delay of 0/50/100/150ms in the first week. In the second week, we remeasured the stability rate, recovery time, and abnormal stoppage rate and created a threshold table. | Identification of closed-loop delay tolerance range (`G2` main / `G5` spare) | `6` / `1972` | Relative decrease in stability rate is within 20% and abnormal stop rate is within the prior upper limit. |
| U8-2 | Quantify the impact of online calibration intervals on performance retention. | Three conditions of calibration interval (every trial/every block/no fixation) were set in the first week. In the second week, we simultaneously evaluate the amount of drift and recalibration cost and determine the upper limit of operation. | Optimization of concept drift countermeasures (`G2` main / `G5` spare) | `696` / `2412` | Improvement in performance maintenance rate is statistically significant with respect to increase in calibration cost. |
| U14-1 | Measure the correspondence between the fixed granularity (data/code/environment) of supplementary trial contracts and the reproduction success rate. | In the first week, re-execute at three granularity: "Fixed data only", "Fixed data + code", "Fixed data + code + environment". Quantify the recall rate difference and the man-hour difference in the second week. | Minimum granularity definition of reproduction contract (`G1` main / `G3` reserve) | `56` / `719` | Recall rate meets target value and man-hour increment is within acceptable upper limit. |
| U14-3 | Automatically detect subject leaks and time series leaks, and enable auditing of leaderboard evaluations. | Implemented leak detection rules (subject/session/time-window) in the first week. Apply it to the existing partition in the second week and create an audit report of the performance difference after re-partitioning. | leaderboard audit operation (`G1` main / `G3` spare) | `719` / `56` | Zero leak detection, performance deterioration after repartition can be explained. |
| U7-2 | Estimate the jitter distribution of LSL synchronization error and determine the operational warning threshold. | Fixed offset/jitter extraction processing in the first week. Calculate the event rate exceeding the threshold in the second week and set the remeasurement trigger conditions as rules. | Synchronization error automatic warning operation (`G1` main / `G3` spare) | `6` / `696` | Reproducibility of threshold exceeded events and false alarm rate of remeasurement rules are within tolerance. |
| U13-1 | Separately evaluate the discrepancy between semantic matching and causal matching using the same decoder. | In the first week, compute semantic match score and intervention-response match score with separate metrics. In the second week, register deviation cases as failure conditions and prohibit pass decisions based only on imitation score. | Separate evaluation of semantic restoration/causal reproduction (`G1` main / `G4` preliminary) | `509` / `13` | Cases where only semantic matching is high can be identified and cases where there is no causal matching can be avoided. |

### Execution order (fixed)

1. `U8-1` (delay tolerance area)
2. `U8-2` (Calibration interval and drift)
3. `U14-1` (Reproduction contract granularity)
4. `U14-3` (Leak Audit)
5. `U7-2` (Synchronization error audit)
6. `U13-1` (Separation of semantic matching/causal matching)

### Operation rules fixed in this run

- Re-fix `1RQ=1 verification proposition=1 application theme=1 main data` as 6RQ.
- RQs that do not reach "first experiment results + pass/fail gate" within two weeks will not be carried over to the next run, but will be switched to another RQ with a clear reason for failure.
- `C` Judgment RQ is not subject to this time (the policy is to accumulate technology demonstration first).

## 2026-03-15 16:03 JST revalidation log (after main run/submodule pull)

- After reflecting the latest `main` of `mind-upload` / `EEG-DATA` / `auto-research-funds`, re-inspect the `RQ` line of the deep digging note.
- Reconfirmed `RQ_TOTAL=60`, `A/B/C=17/25/18`, `Application theme (grant key)` missing `0`, `Main EEG-DATA` missing `0`.
- The policy remains the same: `1RQ = 1 verification proposition = 1 application theme = 1 main data`, and each issue will be treated individually and in depth.

## 2026-03-18 12:08 JST revalidation log (main run / deep-by-RQ enforcement)

- Revalidated deep-focus operation with the same policy: avoid generic summaries and keep `1RQ = 1 verification proposition = 1 application theme = 1 main data`.

## 2026-03-22 11:03 JST revalidation log (main run / one-by-one deep pack refresh)

- Reconfirmed `RQ_TOTAL=60` and `A/B/C=17/25/18` against `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`.
- Refreshed the fixed deep pack to a non-overlapping 6RQ set for this run:
  `U0-1`, `U3-3`, `U4-2`, `U7-5`, `U11-3`, `U14-2`.
- Re-fixed the operational policy: avoid broad summaries and enforce `1RQ = 1 verification proposition = 1 application theme = 1 main data`.
- Updated synchronized map pages:
  `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` and
  `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.
- Rechecked RQ coverage on this page against `research_harvest_50.md` and related RQ60 pages (coverage maintained).
- Revalidated grant keys `G1-G6` and source resolvability in `grant_queue`/`auto-research-funds`.
- Confirmed EEG numeric IDs are present in latest `EEG-DATA` CSV but no longer reliable as fixed dataset identifiers after reindex/remap.
- Fixed submission rule for this run: canonical references must be written using `DOI + dataset name + access class` in `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.

## 2026-03-18 16:28 JST revalidation log (main run / pull-after deep sync)

- Pulled latest `main` before this run and revalidated this page in deep-by-RQ mode (`1RQ = 1 verification proposition = 1 application theme = 1 main data`).
- Recounted unique RQ keys on this page and reconfirmed `RQ_TOTAL=60` with no missing key.
- Recalculated judgment split from `mind-upload-eeg-rq60-feasibility-and-funds.md` and reconfirmed `A/B/C=17/25/18`.
- Revalidated referenced EEG IDs (`24` IDs: `6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) exist in latest `EEG-DATA/eeg_dataset_summary_ja.csv` (`missing=0`).
- Revalidated grant real IDs `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) remain resolvable in `grant_queue` and `auto-research-funds` mapping docs.

## 2026-03-18 08:04 JST revalidation log (main run / deep-by-RQ execution lock)

- Pulled latest `main` in `auto-startup`, `mind-upload`, `auto-research-funds`, and `EEG-DATA` before this run.
- Recounted unique `Ux-RQy` keys on this page and reconfirmed `RQ_TOTAL=60` (`missing=0`, `duplicate=0`).
- Rechecked judgment split against `mind-upload-eeg-rq60-feasibility-and-funds.md` and reconfirmed `A/B/C=17/25/18`.
- Revalidated the 24 referenced EEG IDs (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) in latest `EEG-DATA/eeg_dataset_summary_ja.csv` (`missing=0`).
- Revalidated grant real IDs `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) in `grant_queue` and `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.
- Execution policy is unchanged: no generic sweep, only deep one-by-one operation with `1RQ = 1 verification proposition = 1 application theme = 1 main data`.

## 2026-03-18 09:04 JST revalidation log (main run / deep-by-RQ consistency refresh)

- Pulled latest `main` in `auto-startup`, `mind-upload`, `auto-research-funds`, and `EEG-DATA` before this run.
- Rechecked deep-by-RQ operation (`1RQ = 1 verification proposition = 1 application theme = 1 main data`) and reconfirmed `RQ_TOTAL=60` with `A/B/C=17/25/18`.
- Revalidated the 24 referenced EEG IDs (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) in latest `EEG-DATA/eeg_dataset_summary_ja.csv` (`missing=0`).
- Revalidated grant real IDs `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) in `grant_queue` and `auto-research-funds` map docs.
- Refreshed EEG inventory baseline from current CSV: `TOTAL=28,152`, `immediate=23,871`, `uncertain_public=3,692`, `account_required=585`, `restricted=4`.
- Execution rule is unchanged: avoid generic sweep and maintain one-by-one deep operation for every RQ.

## 2026-03-18 10:18 JST 再検証ログ（本run / 1件ずつ深掘りの固定）

- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- `main EEG-DATA` 参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` で全件実在（欠落 `0`）を確認しました。
- 助成実ID `G1-G6` は `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能でした。
- 継続方針: 汎用要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を維持します。

### 直近で深掘りする6RQ（本run固定）

1. `U4-2`（主データ `56` / `G1`）
2. `U7-5`（主データ `676` / `G1`）
3. `U8-4`（主データ `2412` / `G2`）
4. `U11-1`（主データ `859` / `G2`）
5. `U13-3`（主データ `509` / `G1`）
6. `U14-6`（主データ `719` / `G1`）

## 2026-03-18 19:02 JST 再検証ログ（本run / 総合確認）

- `main` pull 後に `mind-upload/wiki/mind-upload-rq60-deep-focus-notes.md` を再検証し、`research_harvest_50.md` 由来の `RQ_TOTAL=60`（`missing=0`, `duplicate=0`）を再確認しました。
- 判定内訳は `A/B/C=17/25/18` を再計数で確認しました。
- 60RQの全行で `Application theme (grant key)` と `Main EEG-DATA` が埋まっていることを確認しました。
- `Main EEG-DATA` の参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` 上で全件実在（`missing=0`）を再確認しました。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds` 側マップで再参照可能でした。
- 方針は継続: 汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を固定し、1件ずつ深掘りします。

### 本runで優先して深掘りする6RQ（1件ずつ実行）

1. `U0-1`（同一性KPI二軸ROC、主データ `11`、応募 `G2`）
2. `U1-2`（不確実性伝播校正、主データ `56`、応募 `G1`）
3. `U4-2`（最小介入因果主張、主データ `56`、応募 `G1`）
4. `U8-1`（閉ループ遅延許容域、主データ `6`、応募 `G2`）
5. `U13-1`（意味一致/因果一致の分離、主データ `509`、応募 `G1`）
6. `U14-3`（リーク監査運用、主データ `719`、応募 `G1`）

## 2026-03-20 09:35 JST 実行カード更新ログ（本run / 1件ずつ深掘りの固定）

- `mind-upload` / `EEG-DATA` / `auto-research-funds` を再突合し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を維持したまま、2週間で初回結果まで到達しやすい `6RQ` を実行カード化しました。
- 汎用横断ではなく、`1RQ=1検証命題=1応募テーマ=1主データ` で、各RQに `KPI` `失敗条件` `提出最低成果物` を明示しました。
- このrunでは `C` 判定RQを拡張せず、まず `A/B` の実測ログを積む順序に固定しました。

### 本run固定: 2週間実行パック（深掘り6RQ）

| RQ | 最初の実験KPI | 失敗条件 | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|
| `U14-1` | `追試成功率` `再現率差` `追加工数` | 最厳格固定条件でも追試成功率が目標未達 | Supplementary test operation report (including negative cases) | `G1 / G3` |
| `U7-2` | `clock offset` `jitter p95` `閾値超過率` | 閾値超過イベントの再現性不足、または誤警報率過大 | Time synchronization audit report (offset/jitter distribution) | `G1 / G3` |
| `U14-3` | `被験者リーク検出率` `時系列リーク検出率` `再分割後性能差` | 再分割後もリーク0件を達成できない | Leak audit results and repartition trail | `G1 / G3` |
| `U8-1` | `安定率` `回復時間` `異常停止率` | 遅延増加で安定率低下が大きく許容域未確定 | Closed loop safety KPI dashboard | `G2 / G5` |
| `U8-2` | `性能維持率` `ドリフト量` `再較正コスト` | 再較正コスト増に対して性能維持率改善が有意でない | Closed loop safety KPI dashboard | `G2 / G5` |
| `U13-1` | `意味一致率` `因果一致率` `乖離ケース率` | 意味一致高・因果一致低ケースを分離できない | Intervention protocol and rebuttal condition definition | `G1 / G4` |

## 2026-03-20 12:03 JST 再検証ログ（本run / 深掘り運用の継続固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を基準に `RQ_TOTAL=60`、`A/B/C=17/25/18` を再計数し、整合を確認しました。
- 本ページの方針（汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で1件ずつ深掘り）を継続固定しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の実在を再確認しました。

## 2026-03-20 13:02 JST 再検証ログ（本run / ユーザー依頼: 全RQを1件ずつ深掘りでwiki再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、全60RQで `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 3ページ（`mind-upload` 側2ページ + `auto-research-funds` 側1ページ）で参照されるEEG ID一意集合（`6, 11, 13, 16, 19, 29, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1972, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を `grant_queue` と `auto-research-funds` 側で再照合し、全件実在を確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」運用を継続します。

## 2026-03-22 15:40 JST 実行カード更新ログ（本run / 6RQ追加バッチ）

- `RQ_TOTAL=60`、`A/B/C=17/25/18` を維持したまま、既存6RQバッチとは重複しない新規6RQを追加し、実行順を固定しました。
- 追加した6RQは `U0-2` `U1-3` `U4-4` `U11-1` `U14-5` `U15-4` で、`KPI` `失敗条件` `提出最低成果物` を明示しました。
- `U15-4`（C判定）を含め、制度系RQでも技術監査ログとして2週間で到達できる入口を固定しました。
- 運用ルールは継続して `1RQ=1検証命題=1応募テーマ=1主データ` を適用します。

## 2026-03-22 09:01 JST revalidation log (main run / one-by-one deepening)

- Updated the fixed deep-dive batch without broad summary expansion; selected only `U0-3/U1-2/U7-3/U8-4/U13-2/U15-2`.
- Kept `RQ_TOTAL=60`, `A/B/C=17/25/18`, and the same `G1-G6` operating keys.
- Locked the submission rule as `Dxx + DOI + dataset name + access class` (numeric ID is search-only legacy guidance).
- Focused deliverable style remains: `1RQ = 1 verification proposition = 1 application theme = 1 primary dataset`.

## 2026-03-27 07:02 JST 再検証ログ（本run / 6RQ深掘り固定）

- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を正本として再突合し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 本runは汎用横断の追加を行わず、非重複6RQ（`U1-3/U3-5/U7-4/U8-5/U11-3/U15-1`）を `1RQ=1検証命題=1応募テーマ=1主データ` で固定しました。
- 参照主データID（`56,13,676,6,735,49`）は `EEG-DATA/eeg_dataset_summary_ja.csv` で実在（欠落 `0`）を確認しました。
- 助成接続は `G1-G6` 実ID系（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を維持しました。

### 本runで優先して深掘りする6RQ

1. `U7-4`（再計測/除外判定木を固定）
2. `U1-3`（逆解法乖離の採択規則）
3. `U8-5`（オーバーライド安全KPI）
4. `U11-3`（理論比較I/O仕様）
5. `U3-5`（境界拡張proxyと外部依存境界）
6. `U15-1`（神経データ機微性の制度接続）

## 2026-03-27 13:02 JST 再検証ログ（本run / 6RQ深掘り固定）

- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を正本として再突合し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 本runは汎用横断の追加を行わず、非重複6RQ（`U0-1/U1-1/U4-3/U8-6/U12-3/U14-4`）を `1RQ=1検証命題=1応募テーマ=1主データ` で固定しました。
- 参照主データID（`11,56,19,6`）は `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` で実在（欠落 `0`）を確認しました。
- 助成接続は `G1-G6` 実ID系（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を維持しました。

### 本runで優先して深掘りする6RQ

1. `U1-1`（逆問題の事前分布比較と採択規則）
2. `U0-1`（同一性KPIの観測一致/介入一致二軸化）
3. `U14-4`（Model Card / Dataset Card の契約要件化）
4. `U4-3`（反事実誤差による理論比較固定）
5. `U8-6`（再学習頻度と安全余裕のトレードオフ固定）
6. `U12-3`（心理的連続性監査ログの制度接続準備）

## 2026-03-29 01:37 JST correction log (main run / anchor and deliverable drift fix)

- Pulled the latest `main` in `auto-startup`, `mind-upload`, `EEG-DATA`, and `auto-research-funds` before editing (`0 0`, `Already up to date` in every repo).
- Recounted `### Ux-y` headings in `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` and reconfirmed `RQ_TOTAL=60` (`missing=0`, `duplicate=0`).
- Recomputed the judgment split from `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` and reconfirmed `A/B/C=17/25/18`.
- Rechecked the referenced legacy ID set (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) in `EEG-DATA/eeg_dataset_summary_ja.csv` (`旧ID`, `missing=0`).
- Corrected the `U11-1` anchor drift: the stale `D12=10.21227/qqj2-r702` reference was invalid and is now aligned to `D14 (10.6084/m9.figshare.1485719)` with `D16/D17` as support anchors.
- Corrected the `U12-5` minimum deliverable drift: this RQ now consistently points to `Branch-based audit log design document` instead of a synchronization-only report.
- This correction pass did not replace the solve-first execution pack. The active 2026-03-29 pack remains the synced six-RQ set below.

## 2026-03-29 01:44 JST revalidation log (main run / solve-first six-RQ sync)

- Synced this note to the existing 2026-03-29 solve-first pack already fixed in `docs/wiki/mind-upload_eeg_funding_verification_2026-03-29_0137-jst.md`, `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`, and `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.
- Kept the same evidence rule: no broad sweep, no claim expansion, and no numeric-ID-only citation in submission documents.
- Reconfirmed the execution criterion for this sync: prioritize RQs that are easiest to turn into both an initial EEG experiment and a grant-ready problem statement without relaxing the `1RQ = 1 verification proposition = 1 application theme = 1 primary dataset` rule.

### Solve-first six-RQ pack synced in this run

1. `U1-1` - prior-family benchmark with known stimulation ground truth
2. `U4-2` - minimum causal claim fixed before analysis
3. `U7-1` - BIDS extension contract for synchronization/QC/stimulus logs
4. `U11-1` - rank-preserving theory comparison across anesthesia/sleep/DoC
5. `U13-5` - perception-to-recall branch point for mimicry/mechanism separation
6. `U14-4` - Model Card / Dataset Card wired into the reproducibility contract

## 2026-03-29 07:18 JST revalidation log (main run / mind-upload public six-RQ batch)

- Pulled the latest `main` in `auto-startup`, `mind-upload`, `EEG-DATA`, and `auto-research-funds` before editing and reconfirmed `Already up to date`.
- Kept `RQ_TOTAL=60`, `A/B/C=17/25/18`, and the submission evidence rule `Dxx + DOI + dataset name + access class`.
- Chose only six RQs that directly tighten the public mind-upload program instead of widening the summary surface again.
- Synchronized the public batch in `issue.html` to the same six RQs, while keeping the stronger dataset/KPI/stopping-rule details inside the wiki.

### Current public deepening batch

| RQ | Why this is solve-first now | Primary D anchor | Grant lane | First KPI to lock now | External dependency kept separate |
|---|---|---|---|---|---|
| `U0-1` | identity claims drift upward too easily unless observation-match and intervention-response match are forced into the same public pass/fail gate. | `D02` + support `D11/D23` | `G2 / G3` | `observation-match AUC / intervention-response match rate` | Legal/philosophical identity criteria |
| `U1-2` | inverse-problem claims are not credible unless uncertainty propagation survives repeated conductivity, missing-electrode, and noise perturbations. | `D08` + support `D11/D19` | `G1 / G4` | `interval coverage` | Head-model identification conditions |
| `U4-4` | causal-equivalence claims should fail fast, so falsification thresholds must be locked before reading any result. | `D05` + support `D08/D19` | `G1 / G4` | `PEHE + sign-reversal rate` | Common I/O specification and intervention protocol |
| `U7-1` | synchronization/QC/stimulus logs are the shortest path to a public reproducibility claim that still stays conservative. | `D11` + support `D15/D23` | `G1 / G3` | `required-field fill rate` | Institutional adoption and governance |
| `U8-4` | a closed-loop program without explicit fail-safe latency metrics is not ready for a public safety claim. | `D20` + support `D01/D21` | `G2 / G5` | `abnormal-detection latency p95` | Site shutdown ownership and operational safety SOP |
| `U11-1` | awareness-index comparison is publicly safer when it is reduced to rank preservation across shared I/O rather than theory-winning language. | `D14` + support `D16/D17` | `G2 / G4` | `rank-preservation rate` | Theory adoption and clinical responsibility split |

### Execution order fixed in this run

1. `U7-1`
2. `U1-2`
3. `U4-4`
4. `U0-1`
5. `U8-4`
6. `U11-1`

## 2026-03-29 09:06 JST revalidation log (main run / repo-level anchor audit)

- Pulled the latest `main` in `auto-startup`, `mind-upload`, `EEG-DATA`, and `auto-research-funds`, plus `master` in `auto-startup.wiki`, and reconfirmed `Already up to date` in every target repo.
- Rechecked the active public six-RQ anchors against the local `EEG-DATA/wiki/datasets` cards instead of relying only on routing tables.
- `D11` is currently the strongest anchor in the local mirror because its card exposes `BIDS 1.7.0`, `CC0`, `47 sessions`, `186 EEG runs`, `31 EEG + 5 misc`, `5000 Hz`, and even the `README=24 / participants.tsv=25` mismatch that still has to stay visible in any serious audit.
- `D02` remains a valid cross-session identity anchor, but the current local card only fixes a conservative minimum set (`10 participants`, `BrainVision / BrainAmp / actiCHamp`, motor-imagery framing, cross-session transfer route). It is not yet a substitute for a richer intervention log or a theory-level identity dossier.
- `D05`, `D08`, `D14`, and `D20` remain valid route anchors in the current mirror, but their autogenerated local cards are still sparse enough that public claims should stay at the level of `what family of test this anchor supports` plus `which logs are still required`, not at the level of a complete protocol/QC dossier.
- Practical consequence for the public batch: keep the current six-RQ selection unchanged, but treat `required logs` as first-class deliverables before strengthening the claim language around causal equivalence, inverse-problem coverage, closed-loop safety, or awareness-index comparison.

## 2026-03-29 12:06 JST revalidation log (main run / current public batch re-check)

- Rechecked the same six public RQs directly against the local dataset cards and the still-stale live `https://mind-upload.com/issue.html` output before changing the public source page.
- `D08` and `D11` remain the strongest current repository anchors: `D08` because it exposes a ground-truth source-localization route with intervention, and `D11` because it exposes the richest synchronization/BIDS/session-run audit surface in the local mirror.
- `D02` and `D20` remain usable conservative route anchors, but only when the public claim is kept at the level of cross-session identity drift or closed-loop latency/safety auditing rather than a stronger intervention or deployment claim.
- `D05` works as the minimum perturbation anchor for `U4-4`, but the stronger causal-equivalence reading should stay tied to `D08`-class ground truth or equivalent intervention detail.
- `D14` works as the minimum anesthesia-side anchor for `U11-1`, but the cross-state wording should stay paired with sleep / DoC support anchors such as `D16/D17` rather than being read as a standalone winner.
- Practical consequence for this run: keep the public six-RQ batch unchanged, strengthen the wording around `support anchors + required logs`, and do not widen the claim ceiling.

## 2026-03-29 15:32 JST revalidation log (main run / public-six anchor proof)

- Rechecked the same six public RQs against the live `https://mind-upload.com/issue.html` wording, the local `EEG-DATA` dataset cards, the official funding pages, and the live Todoist task inventory before changing any public-facing text.
- The public six-RQ batch stays unchanged: `U13-2`, `U13-5`, `U14-4`, `U0-2`, `U0-3`, and `U14-2` still form the narrow `inner-speech decoding + identity drift + reproducibility auditing` route, and the public page still presents them as a `route-setting update` rather than a solved-claim update.
- The current conservative anchor proof in the local mirror is now fixed more explicitly as `D10 -> 000016 3M-CPSEED (OpenNeuro ds006465 v2.0.0, immediate)`, `D03 -> 011012 Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments: An EEG and Eye-Tracking Study (DOI route, subscription-gated support)`, `D01 -> 016105 Acquisition delay of wireless EEG (DOI route, subscription-gated support)`, and `D02 -> 005558 CSTE (DOI route, subscription-gated support)`.
- `D03`, `D01`, and `D02` still have IEEE DataPort-backed routes in the local mirror that now need to be read as `subscription-gated support`, so the public route no longer treats them as immediate public anchors.
- Funding and task handling also stay conservative in this run: `Kura Fund` remains the practical first route for `U13/U14`, the `Nakatani Foundation graduate scholarship` remains the main student-facing bridge for `U13/U0`, the `Kashinome Scholarship` stays a runway-only side route, the `Nakatani Foundation research grant` stays in watch mode, and no new Todoist task is added because the required start/deadline tasks already exist.
- Practical consequence for this run: keep the batch unchanged, keep the current solve-first order, and treat the next public-facing progress threshold as `finished minimum artifacts + required logs`, not as a stronger claim ceiling.
