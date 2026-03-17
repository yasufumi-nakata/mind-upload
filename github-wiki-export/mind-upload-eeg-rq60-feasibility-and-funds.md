# Mind-upload RQ60 × EEG-DATA verifiability and subsidy themes (in-depth version)

> Deeply digging into each question and connecting it to the verification design and application theme
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: RQ-by-RQ Deep Dive

## このページの役割
This page is a practical version of research_harvest_50's 60 RQs, which uses A/B/C to determine the range that can be solved with EEG-DATA, and summarizes the verification design, application theme, and dataset ID to be used for each RQ.

## 正確さの前提
Some RQs for U10/U12/U15 cannot be solved by EEG alone, so we judge that it is not possible and specify the necessary external requirements.

## 公開ページへ戻る
- [Literature map](https://mind-upload.com/research_harvest_50.html)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [RQ60 Application Playbook](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook)
- [Issue](https://mind-upload.com/issue.html)

## 関連 Wiki
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Criteria for reducing judgment to experimental specifications.
- [Wiki: Counterfactual/Intervention Verification](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - Directly linked to causal evaluation of U4/U13.
- [Wiki: Data partitioning and leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Required for U14 reproducibility audits.

---

## Judgment rules

- `A` = Main hypothesis can be directly verified with only EEG-DATA
- `B` = Part of the core can be verified with EEG-DATA. However, external data/system information must be used together.
- `C` = Cannot be solved by EEG-DATA alone (mainly targets system design, regulations, metabolism/thermal measurement, etc.)

## Conclusion first (breakdown of 60 RQ)

- `A`: 17 items
- `B`: 25 items
- `C`: 18 items

## Application lane used in auto-research-funds (grounds referenced on this page)

- `Grant for Young Researchers` / `Research Scholarships` / `General Research Grants` / `Joint Research Grants` / `Doctoral Program Research Grants`
- Basis file: `auto-research-funds/data/docs/research_funding_manual_additions_2026-03-14_run132.md`
- Basis file: `auto-research-funds/data/docs/research_funding_keio_grad_underfilled_2026-02-17.md`
- Evidence file: `auto-research-funds/data/docs/research_funding_daily_codex_2026-03-07.md`

### Subsidy key for practical use (with ID)

- `G1`: `GR-2026-013` (centered on technology verification and reproducibility)
- `G2`: `GR-2026-014` (centered on integrated verification and social implementation)
- `G3`: `9Lx4dPK6a4k2gOb7` (Research Grant (Domestic))
- `G4`: `Drbm6vBRDJkn0NGJ` (research grant)
- `G5`: `871pw3rLjNPKgqA0` (research grant)
- `G6`: `46z9VPE4wnkrvEJR` (Academic/Research Grant)

### Grant key entity (from auto-research-funds / grant_queue)

| Key | System name | Main deadline windows expected in 2026 | Where to use it in RQ60 |
|---|---|---|---|
| G1 | JST ACT-X 2026 (`GR-2026-013`) | Early April to early June 2026 | Technical verification of `U1/U4/U7/U13/U14` will be submitted as short- and medium-term results with a reproducibility package. |
| G2 | JSPS DC1 2027 adoption (`GR-2026-014`) | 2026-06-03 17:00 JST (engine deadline brought forward) | `U0/U3/U8/U10/U11/U12/U15` integrated design and long-term themes will be bundled as a doctoral plan. |
| G3 | Okawa Information and Communication Fund Research Grant (`9Lx4dPK6a4k2gOb7`) | 2026-04-21 - 2026-07-10 | Submit an `A` judgment RQ (U7/U14) that is closer to reproduction infrastructure/data standardization as a supplementary application. |
| G4 | Narishige Neuroscience Research Grant Fund (`Drbm6vBRDJkn0NGJ`) | 2022/11/18 to 2023/02/17 Performance-based (system continuation status is unknown) | Focus on `U1/U4/U11/U13/U14` for methodological advancement (causal/inverse problem/decoding audit). |
| G5 | Japan Institute of Industrial Science Research Grant (`871pw3rLjNPKgqA0`) | 2026-08-01 - 2026-09-01 | Submit operational research on closed-loop operation and drift countermeasures for `U8` as a small to medium-scale implementation. |
| G6 | Sumitomo Electric Group Social Contribution Fund Academic/Research Grant (`46z9VPE4wnkrvEJR`) | 2026-04-03 - 2026-06-06 | `C` Used for preparatory research on systems and multimodal collaboration required for judgment RQ (U3/U10/U12/U15). |

### Primary application destination/preliminary application destination by U (Fixed operation)

| U | First application destination | Preliminary application destination |
|---|---|---|
| U0 | G2 | G3 |
| U1 | G1 | G4 |
| U3 | G2 | G6 |
| U4 | G1 | G4 |
| U7 | G1 | G3 |
| U8 | G2 | G5 |
| U10 | G2 | G6 |
| U11 | G2 | G4 |
| U12 | G2 | G6 |
| U13 | G1 | G4 |
| U14 | G1 | G3 |
| U15 | G2 | G6 |

### Submission strategy by A/B/C judgment

- `A`: Complete the main analysis with just EEG-DATA. `G1/G3` Prioritize "reproducibility and implementation speed".
- `B`: EEG main analysis + external requirements required. Specify the “integrated verification plan” using `G2/G4/G5`.
- `C`: EEG is used as audit log/supporting evidence. It will be published as a system/theory collaboration track at `G2/G6`.

### EEG-DATA selection template by RQ type (fixed entrance for digging deeper into each question)

| RQ type (applicable U) | Priority EEG resource axis | Entrance report (EEG-DATA) | Example of data to use first |
|---|---|---|---|
| Stable decoding of thoughts/motor intentions (`U0/U8/U13`) | `motor imagery` `cross-session` `cross-subject` | `TARGET_TASK_REPORT.md` `BENCHMARK_SETUP_REPORT.md` | ID `6, 11, 696, 719` |
| Language/semantic restoration and imitation separation (`U13`) | `reading-RSVP` `naturalistic stimulus` `reconstruction/decoding` | `LANGUAGE_PARADIGM_REPORT.md` `TASK_FORMULATION_REPORT.md` | ID `509, 13, 65` |
| Consciousness state/sleep/failure condition (`U11/U15`) | `resting-state` `sleep` `EEG-fMRI` | `PARADIGM_FAMILY_REPORT.md` `MULTIMODAL_SETUP_REPORT.md` | ID `735, 842, 859` |
| High resolution/inverse problems/causal intervention (`U1/U4`) | `high-density channel` `stimulation` `ground-truth` | `RECORDING_MODALITY_REPORT.md` `EXPERIMENT_REUSE_READINESS.md` | ID `56, 676, 1839` |
| Multimodal alignment and reproducibility operation (`U7/U14`) | `multimodal alignment` `access` `benchmark` | `MULTIMODAL_SETUP_REPORT.md` `EXPERIMENT_SHORTLISTS.md` | ID `6, 56, 783, 4878` |

### Theme lane expansion for auto-research-funds (candidate to add to G1-G6)

| Lane | Additional candidate ID (auto-research-funds) | How to use on this page |
|---|---|---|
| Neurology/Cognition/Clinical EEG | `1geD73ZENwB8yaor`, `lEYmRP97ng3perjO` | `U11/U15` brings "biomarkerization to assist clinical evaluation" to the forefront. |
| Medical Engineering/AI/Signal Processing | `1geD73Z9K2B8yaor` | `U1/U7/U13/U14` emphasizes "EEG classification, abnormality detection, and reproducibility foundations." |
| Aging society/rehabilitation | `QKYgNPxZxN38bO1Z` | Connected to the implementation theme of `U8/U11/U15` sleep/wakefulness/attention maintenance intervention. |
| Social implementation/disaster prevention/local health | `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor` | Submitted as the system integration/field operation audit track of `U15`. |

### Submission format when digging deeper into RQ one question at a time (rules for operating this page)

Be sure to fill in the following four points for each RQ before transferring it to the application text (use by RQ unit, not a general summary).

1. `Assertion unit`:
Fixed the `minimum claim to be verified in this RQ` to one sentence (e.g. "U4-2 is up to the minimum intervention causal claim").
2. `Range that can be determined by EEG-DATA alone`:
Fixed the decision reason for `A/B/C` to be one sentence with data ID (e.g. `ID 56` provides ground-truth).
3. `External dependencies`:
Specify which modality, institutional judgment, or legal judgment is lacking, and do not blur the boundaries.
4. `Submitted deliverables`:
Fixed actual items that can be submitted at the time of application (`analysis script`, `splitting rule`, `failure condition definition`, `reproduction log`).

## EEG-DATA reference dataset (used on this page)

> Important (Added on 2026-03-15 08:00 JST):
> Since the `ID` of `EEG-DATA/eeg_dataset_summary_ja.csv` changes due to renumbering, do not treat `ID -> Dataset name` as a fixed reference. In the application documents/reproduction log, `D1-D16 (DOI fixed)` of `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` is correct, and `DOI + dataset name + access classification` is also written.

| ID | Dataset |
|---|---|
| 6 | Acquisition delay of wireless EEG |
| 11 | CSTE (cross-session/task EEG biometrics) |
| 13 | Multimodal Fusion EEG + Eye-tracking |
| 16 | Deep Nonparametric Bayesian Multimodal Sensor Fusion |
| 19 | HiPi pinprick stimulation EEG |
| 29 | Longitudinal dyslexia ERP |
| 39 | MAD multimodal affective dataset |
| 49 | Physiological Indicators of Driver Sleepiness |
| 56 | Intracerebral stimulation + HD-EEG (ground-truth) |
| 65 | VICODEV driving distraction multimodal |
| 509 | 3M-CPSEED overt/silent/imagined speech EEG |
| 676 | Simultaneous EEG-fMRI XP1 |
| 696 | Longitudinal MI-BCI + spinal stimulation |
| 719 | Ubiquitous P300 benchmark |
| 735 | PK-NMM propofol anesthesia EEG simulation |
| 783 | Simultaneous EEG-fNIRS working memory |
| 842 | AAUWSS wearable sleep study |
| 859 | DoC EEG biomarker pilot |
| 1011 | AlphaDirection1 EEG+ECG+PPG |
| 1839 | CerebellarTMSEEGData |
| 1972 | Closed-loop auditory stimulation (REM) |
| 2412 | NeuroSimo closed-loop EEG/EMG-guided TMS |
| 3419 | rTMS responder/non-responder EEG |
| 4878 | EEG+PPG+GSR rehabilitation fatigue |

## RQ deep grounding memo (U unit)

| U | Number of target RQs | Mainly used EEG-DATA | Reason for choosing this combination | Limitations at this point |
|---|---:|---|---|---|
| U0 | 4 | ID 11 / 29 / 696 | Since cross-session, longitudinal, and post-training changes can be observed at the same time, it is easy to proceed with threshold design for operational identity. | It focuses on the technical identity of biometric identification, and cannot cover the normative judgment of personality identity. |
| U1 | 4 | ID 56 / 676 / 1839 | It is easy to actually measure error and uncertainty propagation in inverse problems using known stimulus positions and simultaneous measurements. | Generalizability requires additional verification as it relies on data from clinical and specific task conditions. |
| U3 | 6 | ID 13 / 16 / 39 | The required amount of subject boundary expansion can be estimated by comparing the performance difference between EEG alone and multimodal expansion. | There is no direct measurement of the glymphatic system or immune surveillance, and the final determination of boundaries cannot be completed with EEG alone. |
| U4 | 4 | ID 19 / 56 / 1839 | Control stimuli and response differences can be used to construct falsifiable tests of intervention matching rather than observation matching. |Additional modalities and additional interventions are required to guarantee causal equivalence up to higher-order cognition on its own. |
| U7 | 6 | ID 6 / 676 / 783 / 4878 | Time synchronization, preprocessing differences, and modality defects can be audited in the same frame, which directly leads to reproducible operation. | Because the tasks are limited, operational expansion is required to create a standard contract common to all areas. |
| U8 | 6 | ID 6 / 1972 / 2412 / 696 | Closed-loop issues such as delay, phase, recalibration, and drift are complete, and safety margin KPIs can be defined by actual measurements. | Additional tests are required for extrapolation to general daily operations as it is biased toward sleep, TMS, and motor imagery. |
| U10 | 4 | ID 735 / 783 / 1011 | Connecting neural activity and metabolic proxy makes it easy to verify the theoretical consistency of information thermodynamics step by step. | Since there is no direct measurement of heat dissipation, the claim of Landauer's lower limit remains at the theoretical/proxy level. |
| U11 | 4 | ID 735 / 842 / 859 | It is easy to compare the rank preservation and failure conditions of consciousness index approximation based on the state differences of anesthesia, sleep, and DoC. | IIT exact calculations and final decisions between theories are subject to computational complexity and external design constraints. |
| U12 | 6 | ID 11 / 509 / 696 | Branch conditions and expression drift can be tracked as technical IDs and an audit log can be created to be passed on to institutional discussions. | Normative judgments about responsibility, rights, and consent are mainly determined by system design and cannot be determined by EEG alone. |
| U13 | 6 | ID 509 / 13 / 65 | By combining overt/imagined differences and behavioral/physiological differences, it is easy to separate successful imitation and internal mechanism differences. | Focusing on specific contexts such as language and driving, additional tasks are required to create a general imitation separation bench. |
| U14 | 6 | ID 6 / 56 / 719 | By combining delayed reproduction, ground-truth, and benchmark, it is easy to contract out the possibility of additional testing. | System operational aspects, such as disclosure consent and negative case disclosure flow, require separate implementation. |
| U15 | 4 | ID 49 / 2412 / 3419 | It is possible to create a technical log similar to the decision to safely stop and continue treatment, making it easy to use as the basis for implementing system KPIs. | The final implementation of neurorights/jurisdictional differences mainly involves legal design, and cannot be completed with data alone. |

## U0 Research question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application themes for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U0-1<br>When identity judgment is separated into "observation matching" and "intervention response matching", which one should be regarded as a necessary or sufficient condition? | A (directly verifiable) | Create a two-axis ROC by separating observation matching (EEG features) and intervention matching (responses when changing stimuli/tasks). | Young Researcher Grant (Identity KPI) | ID 11, 29, 696 |
| U0-2<br>How to fix the correspondence between time synchronization (in ms) and state expression (behavior, neural activity, physiology). | A (direct verification possible) | Simultaneously measure time synchronization deviation and state feature collapse using ID 676/4878 and define fixed rules. | Research grant (longitudinal identity) | ID 11, 29, 696 |
| U0-3<br>How to set the threshold for identity judgment for each task and how to exclude overfitting models. | A (directly verifiable) | Estimate the identity threshold for each task using ID 11/696, and exclude overfitted models based on out-of-session performance. | Doctoral Program Research Grant (Individual Identification) | ID 11, 29, 696 |
| U0-4<br>Which evaluation axis should we attribute to the definition of "same individual" in the case of divergence/duplication? | B (Partial verification (confirmed using external data)) | In ID 11/509, limit the "identical individual determination" index to biological identification accuracy and specify the operational limits. | Joint research grant (identity x responsibility) | ID 11, 29, 696 |

## U1 Research question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U1-1<br>Which prior distribution should be used to control ill-posedness in EEG/MEG inverse problems? | A (directly verifiable) | Compare the inverse error for each prior distribution using the known stimulus location with ID 56. | Research Grant (Inverse Problem Bench) | ID 56, 676, 1839 |
| U1-2<br>How to propagate uncertainties in cranial conductivity, electrode placement, and noise structure to estimated uncertainties. | A (direct verification possible) | Perform electrode loss and noise injection using ID 56/1839 to create a calibration curve for uncertainty propagation. | Young Researcher Grant (Uncertainty Estimation) | ID 56, 676, 1839 |
| U1-3<br>How to set the decision rule when different inverse solutions (MNE, beamformer, Champagne, etc.) differ for the same data. | B (Partial verification (confirmed using external data)) | Compare the deviation rate of MNE/beamformer/Champagne by task using ID 56/676. | Research grant (method comparison) | ID 56, 676, 1839 |
| U1-4<br>In addition to estimated values, should confidence intervals/backward distributions be included in the publication criteria? | B (partial verification (satisfied with external data)) | Evaluate whether or not the confidence interval of the inverse problem can be published using the backward distribution reproducibility with ID 56. | Doctoral research grant (backward distribution disclosure) | ID 56, 676, 1839 |

## U3 Research question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U3-1<br>How to measure the predicted improvement when adding glial/humoral regulation to the neuron-centered model? | B (partial verification (confirmed with external data)) | Measure the performance difference between EEG alone and multimodal using ID 13/39 and estimate the required amount of boundary expansion. | Exploratory Young Research Grant (Border Proxy) | ID 13, 16, 39 |
| U3-2<br>How to compare the relationship between connectome completeness and functional prediction performance across species. | B (Partial verification (satisfied with external data)) | EEG-DATA alone cannot directly verify connectome completeness, so it is limited to reproducibility evaluation as a supplementary indicator. | Exploratory Young Research Grant (Border Proxy) | ID 13, 16, 39 |
| U3-3<br>How to quantify the functions lost in a model in which the body-environment coupling is removed. | B (Partial verification (confirmed with external data)) | Compare the difference in conditions including the body/environment loop using ID 16/39 and measure the performance decline upon removal. | Exploratory Young Research Grant (Border Proxy) | ID 13, 16, 39 |
| U3-4<br>How to fix the judgment of ``minimum required configuration'' based on data rather than theoretical assertions. | C (Not possible with EEG-DATA alone (system/other modalities required)) | Final determination of the required minimum configuration cannot be made with EEG alone. First, fix the proxy KPI with ID 13/39. | Exploratory Young Research Grant (Border Proxy) | ID 13, 16, 39 |
| U3-5<br>To what extent do prediction accuracy and explainability improve when including the glymphatic/meningeal lymphatic system? | C (Not possible with EEG-DATA alone (requires system/other modalities)) | Glymphatic/meningeal systems do not have direct measurement in EEG-DATA, and are treated as exploration based on simultaneous metabolic data. | Exploratory Young Research Grant (Border Proxy) | ID 13, 16, 39 |
| U3-6<br>At what point does a model that excludes immune surveillance (meningeal immunity/inflammatory signals) fail in long-term prediction? | C (Not possible with EEG-DATA alone (requires system/other modalities)) | Long-term failure of the immune surveillance exclusion model cannot be achieved with EEG-DATA alone. External linkage of longitudinal clinical data is required. | Exploratory Young Research Grant (Border Proxy) | ID 13, 16, 39 |

## U4 Research question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U4-1<br>What are the identification conditions that bring the correlation derived from observational data into a causal graph? | B (Partial verification (established using external data)) | Measure the response difference to the input operation with ID 19/1839 and separate the difference from the observed correlation. | Research Grant (Intervention Equivalent) | ID 19, 56, 1839 |
| U4-2<br>What is the minimum causal claim that can be verified in intervention experiments (stimulation, inhibition, input disturbance)? | A (directly verifiable) | Pre-register a minimum causal claim using a known intervention with ID 56 and judge whether it can be reproduced. | Young Researcher Grant (Ground-truth Intervention) | ID 19, 56, 1839 |
| U4-3<br>How to connect the theoretical predictions of active inference and DCM to counterfactual evaluation. | B (Partial verification (established with external data)) | Mainly ID 676, compare counterfactual error (PEHE) and predicted likelihood difference with and without intervention, and fix the theoretical ranking. | Research grant (counterfactual evaluation) | ID 19, 56, 676 |
| U4-4<br>At what level should you declare the failure condition (falsification) for equivalence determination? | B (Partial verification (satisfied with external data)) | Pre-register `ΔAUC > 0.03` or `Intervention response sign reversal rate > 10%` as the failure declaration threshold with ID 19/56. | Joint research grant (falsification design) | ID 19, 56, 1839 |

## U7 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U7-1<br>To what extent should synchronization, QC, and stimulation logs be required with BIDS expansion? | A (directly verifiable) | ID 676/783 will require the following four items: `clock offset`, `sampling drift`, `stimulus onset`, and `QC fail code`, and will be rejected if they are missing. | Research Grant (Multimodal Standardization) | ID 676, 783, 4878 |
| U7-2<br>Can time synchronization errors such as LSL be reduced to verifiable indicators? | A (Direct verification possible) | ID 6/676 calculates the jitter/delay reference value and automatically warns when the threshold is exceeded. | Young Researcher Grant (Synchronous Audit) | ID 676, 783, 4878 |
| U7-3<br>How to audit the influence of setting differences in artifact removal (ASR, ZapLine, etc.) on results? | A (directly verifiable) | Rerun the preprocessing settings difference with ID 676/4878 and quantify the result drift. | Research grant (preprocessing difference) | ID 676, 783, 4878 |
| U7-4<br>How to fix remeasurement/exclusion criteria when inter-modality alignment fails. | A (directly verifiable) | Create a decision tree for remeasurement/exclusion conditions when alignment fails with ID 676/783. | Joint research grant (remeasurement criteria) | ID 676, 783, 4878 |
| U7-5<br>When automatically comparing preprocessing differences using CI, which recall rate drop should be used as the release block threshold? | A (Direct verification possible) | Run the preprocessing CI with ID 676, and set the release block threshold when the recall rate decreases by -5pt or more using the standard pipeline ratio. | Research Grant (CI Reproducibility) | ID 676, 783, 4878 |
| U7-6<br>What is the minimum observation set that can maintain equivalent conclusions even under modality deficit (EEG deficit/fMRI deficit) conditions? | A (directly verifiable) | Simulate EEG deficit/fMRI/fNIRS deficit with ID 676/783 and find the minimum observation set. | Research Grant (Defect Robustness) | ID 676, 783, 4878 |

## U8 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U8-1<br>How to identify the delay tolerance range of closed-loop BCI from a control theory perspective. | B (partial verification (confirmed with external data)) | Measure the ``stability rate'', ``stop intervention rate'', and ``recovery time'' against delay and phase shift using ID 6/1972, and define the tolerance range using three indicators. | Young Researcher Grant (Closed Loop Stabilization) | ID 6, 1972, 2412, 696 |
| U8-2<br>How to incorporate online calibration and concept drift countermeasures. | B (Partial verification (confirmed with external data)) | Compare the frequency of online recalibration and performance stability with ID 2412/696. | Research Grant (Recalibration) | ID 6, 1972, 2412, 696 |
| U8-3<br>Which index should be used to evaluate stability across individual differences and diurnal fluctuations? | B (Partial verification (confirmed using external data)) | Design a long-term stability KPI by separating intra-individual and inter-individual variance using ID 696. | Doctoral Program Research Grant (Long-term Drift) | ID 6, 1972, 2412, 696 |
| U8-4<br>How to incorporate anomaly detection and failsafe into the evaluation contract. | B (Partial verification (confirmed with external data)) | Measure the anomaly detection delay and failsafe activation time with ID 2412/1972. | Joint Research Grant (Failsafe) | ID 6, 1972, 2412, 696 |
| U8-5<br>When introducing human override, how to convert malfunction rate and recovery time into KPIs. | B (Partial verification (confirmed using external data)) | With ID 2412, make the malfunction rate and recovery time during manual override into KPIs. | Research Grant (Override) | ID 6, 1972, 2412, 696 |
| U8-6<br>How to optimize the relearning frequency in weekly to monthly scale operations by making a trade-off between performance degradation and safety margin. | B (Partial verification (satisfied with external data)) | Change the relearning interval with ID 696/2412 and estimate the trade-off between performance degradation and safety margin. | Research Grant (Relearning Optimization) | ID 6, 1972, 2412, 696 |

## U10 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U10-1<br>How to apply/interpret the Landauer lower bound in neural computation. | C (Not possible with EEG-DATA alone (system/other modalities required)) Direct verification of Landauer lower limit is not possible with EEG-DATA alone. ID 735 is used for preliminary verification of theory consistency. | Theoretical research encouragement (information thermodynamics) | ID 735, 783, 1011 |
| U10-2<br>How to define the correspondence between nonequilibrium thermodynamic index and neural information processing efficiency. | C (Not possible with EEG-DATA alone (system/other modalities required)) | Main evaluation of non-equilibrium thermodynamic index is not possible. Search for weak correlation with metabolic proxy with ID 783/1011. | Theoretical research encouragement (information thermodynamics) | ID 735, 783, 1011 |
| U10-3<br>How to create an observation design that translates theoretical formulas into actual data (neural activity/metabolism). | C (Not possible with EEG-DATA alone (system/other modalities required)) Simultaneous measurement of neural activity + metabolism can be partially verified with ID 783, but actual measurement of heat dissipation requires external measurement. | Theoretical research encouragement (information thermodynamics) | ID 735, 783, 1011 |
| U10-4<br>How to integrate thermodynamic constraints into WBE calculation cost evaluation. | C (Not possible with EEG-DATA alone (system/other modalities required)) | Demonstration of integrating thermal constraints into WBE calculation cost is outside of EEG-DATA. Up to model validation with ID 735. | Theoretical research encouragement (information thermodynamics) | ID 735, 783, 1011 |

## U11 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U11-1<br>How to define input/output specifications that can be compared between theories. | B (Partial verification (satisfied with external data)) | With ID 842/859, align the three indicators of PCI approximation, LZ complexity, and perturbation response to the same I/O specification, and make a rank preservation rate of 80% or higher a selection condition. | Research grants (awareness index comparison) | ID 735, 842, 859 |
| U11-2<br>How to deal with computational complexity constraints for PCI and IIT approximate calculations. | C (Not possible with EEG-DATA alone (system/other modalities required)) | Excluding IIT exact calculation, compare `PCI approximation` `LZ` `wSMI` with ID 735/842 with calculation budget (GPU within 2 hours per case). | Theoretical research encouragement (IIT approximation) | ID 735, 842, 859 |
| U11-3<br>How to reduce the conflicting points of theoretical predictions to a single experimental design. | B (Partial verification (successful with external data)) Create a test plan using ID 735/859 to bring the opposing points of theory to the same input conditions. | Joint research grant (theory comparison verification) | ID 735, 842, 859 |
| U11-4<br>How to clarify failure conditions when using awareness indicators in clinical/research settings. | B (Partial validation (successful with external data)) | ID 859 first defines the threshold for clinical failure conditions including false positives/false negatives. | Grant for young clinical researchers (definition of failure conditions) | ID 735, 842, 859 |

## U12 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U12-1<br>On what basis should the identifier of the post-branch subject be assigned? | C (Not possible with EEG-DATA alone (system/other modality required)) | Legal definition of post-branch identifier is not possible with EEG-DATA alone. Limited use of ID 11 for stability evaluation of technical ID. | System/Ethics Research Grant (Technical Audit Connection) | ID 11, 509, 696 |
| U12-2<br>At what point should inheritance rules for responsibilities, rights, and consent diverge? | C (Not possible with EEG-DATA alone (requires system/other modalities)) | Rules for inheritance of responsibilities, rights, and consent are system design issues, and EEG-DATA is only a verification aid. | System/Ethics Research Grant (Technical Audit Connection) | ID 11, 509, 696 |
| U12-3<br>How to handle the discrepancy between the psychological continuity standard and the legal individual standard. | C (Not possible with EEG-DATA alone (system/other modalities required)) | Discrepancies between psychological continuity and legal individuals cannot be determined based on data alone; normative design is the main target. | System/Ethics Research Grant (Technical Audit Connection) | ID 11, 509, 696 |
| U12-4<br>How to connect technical evaluation (performance) and personality evaluation (attribution). | C (EEG-DATA alone is not possible (system/other modalities are required)) | The connection between performance KPI and personality attribution KPI is mainly due to legal requirements, and EEG is a supplement to audit log items. | System/Ethics Research Grant (Technical Audit Connection) | ID 11, 509, 696 |
| U12-5<br>If memory editing/resynchronization occurs between branching entities, what are the criteria for reorganizing legal entity IDs? | C (Not possible with EEG-DATA alone (system/other modalities required)) | ID reorganization rules during memory editing and resynchronization cannot be directly verified with EEG data. | System/Ethics Research Grant (Technical Audit Connection) | ID 11, 509, 696 |
| U12-6<br>When consent is withdrawn, how to technically implement and audit the deprivation of authority to multiple branching entities. | C (EEG-DATA alone is not possible (system/other modalities are required)) | Auditing to remove authority to withdraw consent is a system design issue, and EEG-DATA can be used up to mock log verification. | System/Ethics Research Grant (Technical Audit Connection) | ID 11, 509, 696 |

## U13 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U13-1<br>Can brain-to-text success be broken down into "meaning restoration" and "causal reproduction"? | B (Partial verification (established using external data)) | Compare overt/imagined with ID 509 and measure the discrepancy between semantic agreement and causal agreement. | Research Grant (Imitation Separation) | ID 509, 13, 65 |
| U13-2<br>How to connect LLM's hallucination/consistency test to neural decoding evaluation. | B (partial verification (confirmed with external data)) | ID 13/65 separates behavior consistency and internal state difference and creates a connection point for hallucination testing. | Young Researcher Grant (Hallucination/Internal State Difference) | ID 509, 13, 65 |
| U13-3<br>How to detect cases where the internal mechanism is different even though the output is the same. | B (partial verification (satisfied with external data)) | Design a determiner that extracts cases with the same output and different internal states using ID 65/509. | Research grant (shortcut detection) | ID 509, 13, 65 |
| U13-4<br>To what extent can the upper limit of imitation performance be suppressed by causal evaluation? | B (partial verification (successful with external data)) | Prohibits ID 509 from passing with the imitation score alone, and operates a double threshold with the causal consistency index. | Research Grant (Causal Consistency KPI) | ID 509, 13, 65 |
| U13-5<br>When the same decoder is used for visual perception and visual recall, where does the pattern of deterioration in semantic restoration accuracy diverge? | B (partial verification (satisfied with external data)) | Apply the same decoder to ID 13 under the perceptual condition and the recall condition, and estimate the branching point at which accuracy decreases. | Doctoral Program Research Grant (Perception/Recall Branch) | ID 13, 509, 65 |
| U13-6<br>How to design a control experiment to separately detect prompt induction, data leaks, and shortcut learning. | B (Partial verification (successful with external data)) | Design a leak control experiment with ID 65/13 and evaluate the shortcut detection rate. | Research Grant (Leak Separation Experiment) | ID 509, 13, 65 |

## U14 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U14-1<br>To what extent do you require fixed granularity of data/code/evaluation environment? | A (direct verification possible) | Automate the measurement delay reproduction test with ID 6 and use it as the basis for the minimum follow-up test pack. | Research Grant (Reproducibility Operation) | ID 6, 56, 719 |
| U14-2<br>How to separate exploratory research and verification research operationally. | A (direct verification possible) | Perform separate operation of exploration/verification with ID 56 and show the reproducibility rate of re-execution under the same conditions. | Research grant (exploration/verification separation) | ID 6, 56, 719 |
| U14-3<br>How to audit leaks, overfitting, and reporting bias on the leaderboard. | A (directly verifiable) | Regularize leaderboard leak audits (subject splitting/time series leaks) with ID 719. | Young Researcher Grant (Leak Audit) | ID 6, 56, 719 |
| U14-4<br>How to integrate the Model Card / Dataset Card into the evaluation contract. | A (direct verification possible) | Connect Model Card/Dataset Card mandatory to ID 719/56 and make it an audit item. | Research Grant (Card Integration) | ID 6, 56, 719 |
| U14-5<br>How to publish failed reproduction cases as a negative example registry and operate the retry cycle. | B (partial verification (achieved with external data)) | Operate a negative example registry with `failure_id` `dataset_id` `split_hash` `failure_type` `rerun_status` as required items, and add a public consent flow. | Research Grant (Negative Case Registry) | ID 6, 56, 719 |
| U14-6<br>If container fixation (OS, dependent libraries, random number seeds) is made mandatory, how much increase in reproduction cost can be tolerated? | A (directly verifiable) | Measure the incremental calculation cost when fixing the container with ID 719 and set the allowable upper limit. | Research grant (reproduction cost limit) | ID 6, 56, 719 |

## U15 Research Question (RQ unit)

| RQ | Can it be solved with EEG-DATA | In-depth verification design (one question at a time) | Application theme for auto-research-funds | Recommended EEG-DATA |
|---|---|---|---|---|
| U15-1<br>Which legal concept should be used to handle the sensitivity of neural data (personal information, biological information, personality information)? | C (Not possible with EEG-DATA alone (requires system/other modalities)) | Legal concept mapping of neural data sensitivity is a legal issue, and EEG-DATA alone cannot be verified. | System Design Grant (Neurodata Legislation) | ID 49, 2412, 3419 |
| U15-2<br>How to map neurorights to technical audit items. | C (Not possible with EEG-DATA alone (requires system/other modalities)) | Neurorights audit itemization is mainly for system design, and ID 2412 is only valid for defining technical log items. | System Design Grant (Neurodata Legislation) | ID 49, 2412, 3419 |
| U15-3<br>How to define the minimum common operation across jurisdictional differences (EU/US/JP, etc.)? | C (Not possible with EEG-DATA alone (requires systems/other modalities)) | The minimum operation across jurisdictions cannot be determined from data, and a regulatory comparison table needs to be prepared. | System Design Grant (Neurodata Legislation) | ID 49, 2412, 3419 |
| U15-4<br>How to governance the suspension conditions and renewal conditions according to technological progress. | C (Not possible with EEG-DATA alone (requires system/other modalities)) | Governance of suspension/update conditions is mainly based on system KPI, and ID 49/3419 is a supporting basis for risk threshold. | System Design Grant (Neurodata Legislation) | ID 49, 2412, 3419 |

## Implementation priority order (order directly related to grant application)

1. `U7/U14` first (many A's, easy to create reproducible results in a short period of time)
2. 2nd wave of `U0/U1/U4/U8/U13` (mainly B, but can be assembled as an experimental system)
3. `U10/U12/U15` is a separate track for institutional/theoretical collaboration (EEG cannot be completed alone)

## Submission fixed table by RQ (new)

- For the operational version with fixed `1RQ=1 submission judgment`, refer to `mind-upload-eeg-rq60-grant-dataset-playbook`.
- For each `Ux-RQy`, `first application destination/preliminary application destination/main EEG-DATA/minimum deliverables'' are fixed in one line.
- This page is used as the basis for judgment, and the playbook side is used for submission management.

## Points to note

- The `C` rating on this page does not mean ``unimportant'', but rather ``EEG-DATA alone is insufficient proof''.
- It is safe to use `U12/U15` to define the system design (legal, ethical, audit requirements) first, and then use the EEG side to back up the audit log requirements.
- Direct measurement of thermodynamics is not yet available for `U10`, so it is better to limit it to theory consistency and proxy verification first to avoid over-claiming.

## 2026-03-14 11:02 JST re-verification log (main run)

- Reconfirmed that there are 60 `Ux-RQy` lines from `research_harvest_50.md` (`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`).
- EEG-DATA referenced in this page is `24 ID` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`), the missing `0` on `EEG-DATA/eeg_dataset_summary_ja.csv` was confirmed.
- Grant keys `G1-G6` match the real IDs of `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`).
- The operational policy continues to be `1 RQ = 1 verification proposition = 1 application theme`. `A/B` is given for experimental design, and `C` is given for system/audit design.
- The discrepancy in the number of EEG reference IDs (`17`) in the previous version of the log has been corrected to `24` to match the main body of the table.

## 2026-03-14 12:03 JST re-verification log (main run)

- Reconfirmed that the number of RQ lines in `mind-upload-eeg-rq60-feasibility-and-funds.md` is `60` (`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`).
- `24 ID` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) were found to be missing `0` on `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Real ID of subsidy key `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) was reconfirmed at `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.
- Audit trail is saved in `mind-upload/automation/rq60_eeg_funds_revalidation_2026-03-14_1203JST.md`.

## 2026-03-14 13:06 JST re-verification log (main run)

- Reconfirmed `RQ=60`, breakdown by U (`4/4/6/4/6/6/4/4/6/6/6/4`), and `A/B/C=17/25/18`.
- EEG-DATA `24 ID` referenced on this page is missing `0` in `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Added `TARGET_TASK_REPORT.md`, `LANGUAGE_PARADIGM_REPORT.md`, `PARADIGM_FAMILY_REPORT.md`, `RECORDING_MODALITY_REPORT.md`, `MULTIMODAL_SETUP_REPORT.md` as entry points for EEG resource selection.
- In addition to the existing `G1-G6`, auxiliary lanes include `1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, Specify `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor` as candidate IDs.

## 2026-03-14 14:03 JST re-verification log (main run)

- `Ux-RQy` of `research_harvest_50.md` continues to be `60`, and the number of RQ table rows on this page is also `60`.
- `A/B/C=17/25/18` is maintained. Since `C` judgment mainly depends on the system and legal affairs, `G2/G6` is fixed as the first candidate for submission.
- All EEG references `24 ID` exist on `EEG-DATA/eeg_dataset_summary_ja.csv`, and reconfirmed the missing `0`.
- Grant ID is `G1-G6` and additional candidate ID (`1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, Reconfirm the existence of `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor`) using `auto-research-funds` data.
- Operational policy remains unchanged. `1RQ = 1 verification proposition = 1 application theme`, and create an application statement for each RQ instead of a general summary.

## 2026-03-14 15:02 JST re-verification log (main run)

- Reconfirmed `60RQ` one by one for each `RQ` rather than for each `U`, and confirmed that the `deep-dive verification design` of each line was of a granularity that could be reduced to the "first experimental procedure".
- `A/B/C=17/25/18`, `EEG reference 24 ID`, `Support key G1-G6` (including real ID) are unchanged from the previous log. No loss of consistency.
- We maintain a policy of directly linking `A/B` to the application for actual operation, and submitting `C` in the system/audit design track.
- This page has been synchronized with `mind-upload/wiki` and `mind-upload/github-wiki-export` so that the same content can be referenced when updating the Wiki.

## 2026-03-14 16:02 JST re-verification log (main run)

- Re-checked `research_harvest_50.md` and the `RQ` of this page by `U`, and confirmed `60 matches` (`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`).
- `A/B/C` judgment was re-counted from `17/25/18`, and there was no difference from the previous run.
- Reference `EEG-DATA 24 ID` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) were found to be missing `0` in `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Grant ID `G1-G6` and additional candidate ID (`1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor`) reconfirmed actual hits in `auto-research-funds`.
- The policy for this run is to maintain `1RQ = 1 verification proposition = 1 application theme`, and use a granularity that allows each line to be directly translated into the experimental procedure, rather than a general summary.

## 2026-03-14 17:01 JST re-verification log (main run)

- Reread `mind-upload/automation/rq_reading_path_timed_round19_2026-03-01.csv` in `Ux-RQy` units and reconfirm that the 60 lines on this page have a one-to-one correspondence with the original RQ statement.
- Check all rows of `3-point set of each RQ (A/B/C judgment, application theme, recommended EEG-DATA ID)` and check for missing columns `0` and blank `0`.
- `A/B/C=17/25/18`, `Reference EEG-DATA=24 ID` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) are unchanged from the previous run.
- Grant recipients will maintain the `G1-G6 + additional candidate IDs` on the `auto-research-funds` side, with a fixed policy of using `A/B` as the technology demonstration track and `C` as the system/legal collaboration track.

## 2026-03-14 18:10 JST Addendum (by RQ/beginner experiment card)

In order to make all 60 RQs ``possible to execute one question at a time'', we added initial experiment procedures and failure actions to each RQ without breaking the existing judgments/themes/data.

| RQ | Main indicators (2) | First experimental procedure (main data) | Next action in case of failure |
|---|---|---|---|
| U0-1 | `Intervention matching rate` / `Counterfactual matching rate` | `11` is fixed as the main data, and the baseline of `Intervention matching rate` and `Counterfactual matching rate` is measured first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U0-2 | `Intervention matching rate` / `Counterfactual matching rate` | `11` is fixed as the main data, and the baseline of `Intervention matching rate` and `Counterfactual matching rate` is measured first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U0-3 | `Intervention matching rate` / `Counterfactual matching rate` | `11` is fixed as the main data, and the baseline of `Intervention matching rate` and `Counterfactual matching rate` is measured first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U0-4 | `Intervention match rate` / `Counterfactual match rate` | Fix `11` as the main data and measure the baseline of `Intervention match rate` and `Counterfactual match rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U1-1 | `Position error (mm)` / `Posterior distribution width` | Fix `56` as the main data and measure the baseline of `Position error (mm)` and `Posterior distribution width` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U1-2 | `Position error (mm)` / `Posterior distribution width` | Fix `56` as the main data and measure the baseline of `Position error (mm)` and `Posterior distribution width` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U1-3 | `Position error (mm)` / `Posterior distribution width` | Fix `56` as the main data and measure the baseline of `Position error (mm)` and `Posterior distribution width` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U1-4 | `Position error (mm)` / `Posterior distribution width` | Fix `56` as the main data and measure the baseline of `Position error (mm)` and `Posterior distribution width` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U3-1 | `Predicted improvement rate (∆R2)` / `Extrapolation performance` | `13` is fixed as the main data, and the baseline of `Predicted improvement rate (∆R2)` and `Extrapolation performance` is measured first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U3-2 | `Predicted improvement rate (ΔR2)` / `Extrapolation performance` | Fix `13` as the main data and measure the baseline of `Predicted improvement rate (ΔR2)` and `Extrapolation performance` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U3-3 | `Predicted improvement rate (ΔR2)` / ``Extrapolation performance` | Fix `13` as the main data and measure the baseline of `Predicted improvement rate (ΔR2)` and `Extrapolation performance` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U3-4 | `Predicted improvement rate (∆R2)` / `Extrapolation performance` | Fix `13` as the main data and measure the baseline of `Predicted improvement rate (∆R2)` and `Extrapolation performance` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U3-5 | `Predicted improvement rate (ΔR2)` / ``Extrapolation performance` | Fix `13` as the main data and measure the baseline of `Predicted improvement rate (ΔR2)` and `Extrapolation performance` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U3-6 | `Predicted improvement rate (∆R2)` / `Extrapolation performance` | Fix `13` as the main data and measure the baseline of `Predicted improvement rate (∆R2)` and `Extrapolation performance` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U4-1 | `Intervention effect concordance rate` / `causal edge recall rate` | `19` is fixed as the main data, and the baseline of ``intervention effect concordance rate'' and ``causal edge recall rate'' is measured first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U4-2 | `Intervention effect concordance rate` / `causal recall rate` | `19` is fixed as the main data, and the baseline of `intervention effect concordance rate` and `causal edge recall rate` is measured first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U4-3 | `Intervention effect concordance rate` / `causal recall rate` | `19` is fixed as the main data, and the baseline of `intervention effect concordance rate` and `causal edge recall rate` is measured first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U4-4 | `Intervention effect concordance rate` / `causal recall rate` | `19` is fixed as the main data, and the baseline of `intervention effect concordance rate` and `causal edge recall rate` is measured first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U7-1 | `Synchronization error (ms)` / `Decrease in recall (pt)` | Fix `676` as the main data and measure the baseline of `Synchronization error (ms)` and `Decrease in recall (pt)` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U7-2 | `Synchronization error (ms)` / `Decrease in recall (pt)` | Fix `676` as the main data and measure the baseline of `Synchronization error (ms)` and `Decrease in recall (pt)` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U7-3 | `Synchronization error (ms)` / `Decrease in recall (pt)` | Fix `676` as the main data and measure the baseline of `Synchronization error (ms)` and `Decrease in recall (pt)` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U7-4 | `Synchronization error (ms)` / `Decrease in recall (pt)` | Fix `676` as the main data and measure the baseline of `Synchronization error (ms)` and `Decrease in recall (pt)` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U7-5 | `Synchronization error (ms)` / `Decrease in recall (pt)` | Fix `676` as the main data and measure the baseline of `Synchronization error (ms)` and `Decrease in recall (pt)` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U7-6 | `Synchronization error (ms)` / `Decrease in recall (pt)` | Fix `676` as the main data and measure the baseline of `Synchronization error (ms)` and `Decrease in recall (pt)` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U8-1 | `Stability rate` / `Recovery time (s)` | Fix `6` as the main data and measure the baseline of `Stability rate` and `Recovery time (s)` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U8-2 | `Stability rate` / `Recovery time (s)` | Fix `6` as the main data and measure the baseline of `Stability rate` and `Recovery time (s)` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U8-3 | `Stability rate` / `Recovery time (s)` | Fix `6` as the main data and measure the baseline of `Stability rate` and `Recovery time (s)` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U8-4 | `Stability rate` / `Recovery time (s)` | Fix `6` as the main data and measure the baseline of `Stability rate` and `Recovery time (s)` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U8-5 | `Stability rate` / `Recovery time (s)` | Fix `6` as the main data and measure the baseline of `Stability rate` and `Recovery time (s)` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U8-6 | `Stability rate` / `Recovery time (s)` | Fix `6` as the main data and measure the baseline of `Stability rate` and `Recovery time (s)` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U10-1 | `Theoretical consistency score` / `proxy correlation (ρ)` | Fix `735` as the main data and measure the baseline of `theoretical consistency score` and `proxy correlation (ρ)` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U10-2 | `Theoretical consistency score` / `proxy correlation (ρ)` | Fix `735` as the main data and measure the baseline of `theoretical consistency score` and `proxy correlation (ρ)` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U10-3 | `Theoretical consistency score` / `proxy correlation (ρ)` | Fix `735` as the main data and measure the baseline of `theoretical consistency score` and `proxy correlation (ρ)` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U10-4 | `Theoretical consistency score` / `proxy correlation (ρ)` | Fix `735` as the main data and measure the baseline of `theoretical consistency score` and `proxy correlation (ρ)` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U11-1 | `Inter-theoretical ranking agreement rate` / `False positive rate` | Fix `735` as the main data and measure the baseline of `Inter-theoretical ranking agreement rate` and `False positive rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U11-2 | `Inter-theoretical ranking agreement rate` / `false positive rate` | Fix `735` as the main data and measure the baseline of `inter-theoretical ranking agreement rate` and `false positive rate` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U11-3 | `Inter-theoretical ranking agreement rate` / `false positive rate` | Fix `735` as the main data and measure the baseline of `inter-theoretical ranking agreement rate` and `false positive rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U11-4 | `Inter-theoretical ranking agreement rate` / `false positive rate` | Fix `735` as the main data and measure the baseline of `inter-theoretical ranking agreement rate` and `false positive rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U12-1 | `Audit log completeness` / `Consent withdrawal reflection time` | Fix `11` as the main data and measure the baseline of `Audit log completeness` and `Consent withdrawal reflection time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U12-2 | `Audit log completeness` / `consent withdrawal reflection time` | Fix `11` as the main data and measure the baseline of `audit log completeness` and `consent withdrawal reflection time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U12-3 | `Audit log completeness` / `Consent withdrawal reflection time` | Fix `11` as the main data and measure the baseline of `Audit log completeness` and `Consent withdrawal reflection time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U12-4 | `Audit log completeness` / `Consent withdrawal reflection time` | Fix `11` as the main data and measure the baseline of `Audit log completeness` and `Consent withdrawal reflection time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U12-5 | `Audit log completeness` / `Consent withdrawal reflection time` | Fix `11` as the main data and measure the baseline of `Audit log completeness` and `Consent withdrawal reflection time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U12-6 | `Audit log completeness` / `Consent withdrawal reflection time` | Fix `11` as the main data and measure the baseline of `Audit log completeness` and `Consent withdrawal reflection time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U13-1 | `Semantic matching rate` / `mechanism identification rate` | Fix `509` as the main data and measure the baseline of `semantic matching rate` and `mechanism identification rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U13-2 | `Semantic matching rate` / `mechanism identification rate` | Fix `509` as the main data and measure the baseline of `semantic matching rate` and `mechanism identification rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U13-3 | `Semantic matching rate` / `mechanism identification rate` | Fix `509` as the main data and measure the baseline of `semantic matching rate` and `mechanism identification rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U13-4 | `Semantic matching rate` / `mechanism identification rate` | Fix `509` as the main data and measure the baseline of `semantic matching rate` and `mechanism identification rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U13-5 | `Semantic matching rate` / `mechanism identification rate` | `13` is fixed as the main data, and the baseline of `semantic matching rate` and `mechanism identification rate` is measured first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U13-6 | `Semantic matching rate` / `mechanism identification rate` | Fix `509` as the main data and measure the baseline of `semantic matching rate` and `mechanism identification rate` first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U14-1 | `Make-up success rate` / `Increment in reproduction cost` | `6` is fixed as the main data, and the baseline of `Make-up success rate` and `Increment in reproduction cost` is measured first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U14-2 | `Make-up success rate` / `Increase in reproduction cost` | Fix `6` as the main data and measure the baseline of `Make-up success rate` and `Increment in reproduction cost` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U14-3 | `Make-up success rate` / `Increase in reproduction cost` | Fix `6` as the main data and measure the baseline of `Make-up success rate` and `Increment in reproduction cost` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U14-4 | `Make-up success rate` / `Increase in reproduction cost` | Fix `6` as the main data and measure the baseline of `Make-up success rate` and `Increment in reproduction cost` first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U14-5 | `Make-up success rate` / `Increment in reproduction cost` | `6` is fixed as the main data, and the baseline of `Make-up success rate` and `Increment in reproduction cost` is measured first. | Clarify external requirements (additional modalities/institutional requirements) and switch to staged proposal (technical demonstration → integrated verification). |
| U14-6 | `Make-up success rate` / `Increment in reproduction cost` | `6` is fixed as the main data, and the baseline of `Make-up success rate` and `Increment in reproduction cost` is measured first. | Re-execute preprocessing and split fixing with the same main data, and record the difference in recall rate in the audit log. |
| U15-1 | `Regulatory requirements satisfaction rate` / `Stop criteria activation time` | Fix `49` as the main data, and measure the baseline of `Regulatory requirements fulfillment rate` and `Stop criteria activation time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U15-2 | `Regulatory requirements satisfaction rate` / `Stopping criteria activation time` | Fix `49` as the main data, and measure the baseline of `Regulatory requirements fulfillment rate` and `Stopping criteria activation time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U15-3 | `Regulatory requirements satisfaction rate` / `Stopping criteria activation time` | Fix `49` as the main data, and measure the baseline of `Regulatory requirements fulfillment rate` and `Stopping criteria activation time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |
| U15-4 | `Regulatory requirements satisfaction rate` / `Stopping criteria activation time` | Fix `49` as the main data, and measure the baseline of `Regulatory requirements fulfillment rate` and `Stopping criteria activation time` first. | No performance claims will be made; it will be submitted as a system/audit design track, and EEG will be used only as an auxiliary log. |

Operational rules: Prioritize `A/B` and link directly to the application, and `C` should be submitted in the system/audit design frame.

## 2026-03-14 22:18 JST Re-verification log (deep reading audit by RQ / main run)

- I re-read `60RQ` in `research_harvest_50.md` one by one and reconfirmed that `RQ text -> In-depth verification design of this page -> Application theme -> Recommended EEG-DATA` has a one-to-one correspondence in all lines.
- We checked all 60 lines of `mind-upload-eeg-rq60-grant-dataset-playbook.md` for ``First application destination/Preliminary application destination/Main EEG-DATA/Minimum deliverables'' and confirmed missing columns `0` and broken references `0`.
- `G1-G6` real ID on `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is re-verified and remains visible in all lines.
- In this run as well, we maintained the operational policy of `1RQ = 1 verification proposition = 1 application theme = 1 main data`, and fixed the granularity so that it could be directly transferred to the application statement in units of RQs rather than general summaries.

## 2026-03-15 02:45 JST Re-verification log (main run/RQ unit deep-dive update)

- Re-check `60RQ` using `research_harvest_50.md` as the original, and it matches `Ux-RQy` on this page on a `1:1` basis (`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`).
- Maintain the operating rules of this page: `1RQ = 1 verification proposition = 1 application theme = 1 main data`.
- For the `EEG-DATA` side, priority categories are fixed for each RQ type (see table below), instead of "using anything".
- The `auto-research-funds` side will limit the `grant_eeg_dataset_match.csv` to the primary screening, and the final application will be determined by reconfirming the card itself (deadline, application qualifications, official guidelines URL).

### EEG-DATA selection category (Fixed entry for RQ unit execution)

| Category | First use case (compatible U) | Priority filter (EEG-DATA) | Precautions when using |
|---|---|---|---|
| Resting-state / baseline / connectivity | Identification limit/state boundary (`U1/U11`) | `Stimulus type = rest` `Experimental condition = resting/eyes open/closed` | The task label is thin, so it should not be used too much to claim ``content restoration.'' |
| ERP / oddball / evoked | Event tasks that are easy to disprove (`U4/U14`) | `Experimental conditions = ERP/P300/Oddball` | Due to strong event dependence, extrapolation claims are suppressed. |
| Motor imagery / active BCI | Decoding/closed loop evaluation (`U0/U8/U13`) | `Experimental conditions=motor imagery` `target-task=BCI` | Be sure to audit cross-session deterioration using a separate index. |
| Sleep / consciousness-state | Conscious state/failure condition (`U11/U15`) | `Stimulus type=Sleep` `subject-state=Sleep/Anesthesia` | Since there are few sets with sleep stage labels, check the number of data first. |
| Multimodal (EEG-fMRI/fNIRS/PSG) | Consistency audit/integrated verification (`U7/U14`) | `multimodal-setup=EEG-fMRI/EEG-fNIRS/EEG-PSG` | Rejected when synchronization log is missing (re-measurement given priority). |
| Closed-loop / neurofeedback | Delay, safe stop, relearning (`U8`) | `paradigm-family=Closed-loop` | Data whose controller specifications are unknown should be treated as "exploration". |
| Clinical / intracranial | Ground-truth supplementary/pathological boundary (`U1/U11`) | `recording-modality=iEEG/ECoG/sEEG` | Separate verification is required for generalization of healthy conditions. |

### Grant theming rules (auto-research-funds operation fixed)

1. Don't use ``philosophy words'' directly in the title, but convert them into implementation words for ``evaluation/design/audit/protocols.''
2. `A/B` judgment RQs should be sent to the ``Technology Demonstration'' lane (`G1/G3/G4/G5`), and `C` judgment RQs should be sent to the ``Audit/System Design'' lane (`G2/G6`).
3. `grant_eeg_dataset_match.csv` is only for candidate extraction. Be sure to double-check the ``application qualifications, recruitment period, and official URL'' on ``wiki/cards'' before final submission.
4. Do not use local aliases like `D1-D16` alone. Enable auditing by writing `DOI + dataset name + access category` together.

### Constraints reconfirmed in this run

- The recommendation for `grant_eeg_dataset_match.csv` focuses on vocabulary matching and does not guarantee the possibility of adoption itself.
- Since activity grants, awards, and loans are mixed even in the ``High Relevance'' judgment, refiltering is necessary for the ``Research Grant'' system type.
- Due to the small number of candidates for neuro-specialized recruitment, we will maintain a policy of specifying the topic and submitting it in the broad lane of ``engineering/information/medicine'' for actual operation.

## 2026-03-15 03:03 JST revalidation log (verification of latest version after main run/pull)

- With `mind-upload` updated to `f24ca95`, re-check `60RQ` of `research_harvest_50.md` in `Ux-RQy` units, and reconfirm the number, order, and correspondence of question sentences in the table (missing `0`, duplicate `0`).
- Updated `EEG-DATA` to `b3fb0aabe3` and maintained the policy of ``fixing one main data for each RQ and adding auxiliary data'' for dataset selection (no general-purpose brute force search).
- Updated `auto-research-funds` to `6571303ca`, and reconfirmed the operation of clearly separating and allocating `technology demonstration` and `system/audit design` according to the `A/B/C` determination of the grant theme.
- This time as well, we will maintain the fixed rule of `1RQ = 1 verification proposition = 1 application theme = 1 main data` and continue with the policy of ``deeply understanding and describing each issue one by one''.

## 2026-03-15 04:02 JST re-verification log (main run/entity verification after latest pull)

- Re-run with the latest state of `main` and fixed `mind-upload=4607efe7fd`, `EEG-DATA=b3fb0aabe3`, `auto-research-funds=6571303caf` as the base commit.
- `research_harvest_50` original and `Ux-RQy` of this page Re-match `RQ line count=60`, `duplicate=0`, `missing=0`, `Breakdown by U=U0(4)/U1(4)/U3(6)/U4(4)/U7(6)/U8(6)/U10(4)/U11(4)/U12(6)/U13(6)/U14(6)/U15(4)` I have confirmed.
- `A/B/C` judgment remains unchanged at `17/25/18`. We maintained the policy of applying for `A/B` as a technology demonstration and submitting `C` for the system/audit design track.
- `24 ID` of `EEG-DATA reference dataset` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) was confirmed to exist (missing `0`) on `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Subsidy key `G1-G6` and extension candidate ID (`1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor`) have been reconfirmed with `auto-research-funds/wiki` and `grant_eeg_dataset_match.csv`.
- We will not perform a general summary in this run, but will continue to deeply dig into `1RQ = 1 verification proposition = 1 application theme = 1 main data`.

## 2026-03-15 06:02 JST revalidation log (main run/automation addition)

- Re-verified with the latest state after running `git pull origin main` and updated the base commit to `mind-upload=8e75f7833c`, `EEG-DATA=b3fb0aabe3`, `auto-research-funds=6571303caf`.
- `mind-upload/automation/rq_reading_path_timed_round19_2026-03-01.csv` We compared this with the RQ table on this page and reconfirmed that `Number of RQ lines = 60` and `Breakdown by U = U0(4)/U1(4)/U3(6)/U4(4)/U7(6)/U8(6)/U10(4)/U11(4)/U12(6)/U13(6)/U14(6)/U15(4)`.
- Judgment breakdown remains as `A/B/C=17/25/18`. We will continue to allocate `A/B` to the technology demonstration system and `C` to the system/audit design system.
- Reference EEG data `24 ID` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) reconfirmed the existence of all items (missing `0`) in `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Grant key `G1-G6` Real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) We reconfirmed the existence of all items at `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.
- The policy remains fixed: `1RQ = 1 verification proposition = 1 application theme = 1 main data`. Rather than looking at a general overview, we will continue to dig deep into each RQ one by one and post them into the application text.

## 2026-03-15 08:02 JST revalidation log (this run / ID renumbering correction policy)

- Re-checked `mind-upload/research_harvest_50.md` and `Ux-RQy` on this page, and maintained the correspondence of `60RQ` (`missing 0/duplicate 0`).
- `A/B/C` confirmed `17/25/18` by re-counting. No change in judgment policy.
- `24 ID` of `EEG-DATA/eeg_dataset_summary_ja.csv` is maintained (missing `0`), but `ID -> Dataset name` has been renumbered in the current CSV, and the operation has been changed to not assume a fixed match with the old label.
- Clarify the original copy of the practical application:
  - Deep dive into RQ units: `mind-upload/wiki/mind-upload-rq60-deep-focus-notes.md`
  - Grant x original dataset: `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` (`D1-D16 + DOI`)
- From now on, do not submit using `numeric ID only`. Be sure to fix `DOI + dataset name + access category + application theme` as one set.

## 2026-03-15 12:02 JST Re-verification log (continuation of deep digging operation per main run/1RQ)

- Re-extracted the `Ux-RQy` line from the original `research_harvest_50.md` and checked `RQ_TOTAL=60`, `duplicate=0`, `missing=0`.
- Recounted the judgment column on this page and reconfirmed `A/B/C=17/25/18`.
- EEG data ID referenced in RQ line (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) are all present in `EEG-DATA/eeg_dataset_summary_ja.csv` (missing `0`).
- Grant real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) is `auto-research-funds` / All items can be viewed with `grant_queue`.
- The policy is fixed: we will not return to a general overview, but will continue to operate in depth using `1 RQ = 1 verification proposition = 1 application theme = 1 main data`.

</article>
</main>

## 2026-03-15 13:03 JST Re-verification log (reflects this run/latest pull)

- Before starting work, I `pull --ff-only` the `main` and 3 submodules and updated the base commits to `mind-upload=7e4833b0e3`, `EEG-DATA=1bd4c93316`, `auto-research-funds=a8d32a90bc`.
- Recount the `RQ` line on this page, `RQ_TOTAL=60`, `Breakdown by U=U0(4)/U1(4)/U3(6)/U4(4)/U7(6)/U8(6)/U10(4)/U11(4)/U12(6)/U13(6)/U14(6)/U15(4)` I reconfirmed.
- We reconfirmed the judgment breakdown `A/B/C=17/25/18` and maintained the deep operation of `1RQ=1 Verification Proposition=1 Application Theme=1 Main Data`.
- Reference EEG data ID (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) confirmed the existence of all items (missing `0`) in `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Grant key `G1-G6` Real ID (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) I reconfirmed that it can be referenced in `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` and `grant_eeg_dataset_match.csv`.

## 2026-03-15 16:03 JST revalidation log (after main run/submodule pull)

- Re-inspected `main` of `mind-upload` / `EEG-DATA` / `auto-research-funds` after pulling and confirmed the consistency of `RQ_TOTAL=60` and `A/B/C=17/25/18`.
- Continue the operational rule of `1RQ = 1 verification proposition = 1 application theme = 1 main data` and maintain a policy of not returning to a general-purpose overview.
- Reference EEG data is `24 ID` (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) and no missing parts.
- Grant real IDs (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) can still be referenced.

## 2026-03-18 11:20 JST revalidation log (main run / per-RQ deep-audit refresh)

- Before work, pulled all three repositories and fixed base commits to `mind-upload=d0a06cf30f2d`, `EEG-DATA=357cd9af4962`, `auto-research-funds=a6ffdb0898e8`.
- Recounted `research_harvest_50.md` by U section and reconfirmed `RQ_TOTAL=60` (`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`).
- Re-checked this page with unique `Ux-y` keys and reconfirmed `60 RQ` coverage with judgment split `A/B/C=17/25/18`.
- Verified all EEG IDs referenced on this page (`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`) exist in `EEG-DATA/eeg_dataset_summary_ja.csv` (missing `0`).
- Re-verified grant IDs `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`) against `grant_queue` and `auto-research-funds/grant_eeg_dataset_match.csv`.
- The operating rule remains fixed: avoid generic summary and keep `1RQ = 1 verification claim = 1 grant theme = 1 primary EEG dataset`.
