# Site Deepening Audit (2026-03-14, Verification Causality / Closed Loop)

## Scope

- Main target: `verification.md`
- Secondary target: `wiki/counterfactual-and-perturbation-verification.md`
- Secondary target: `wiki/closed-loop-latency-jitter-and-safety-stops.md`

## Why This Page Was Selected

- The core claim of the public site is `Verification Commons`, but as of 2026-03-14, the main text states that `Causal perturbation` and `Closed loop` are important, but does not sufficiently distinguish which primary literature has reached how far.
- This left room for `High accuracy in offline`, `Works in online`, `Behavior changes with external intervention`, `Long-term stable operation` to be read as evidence of equal strength.
- This is important from a technical and natural science perspective. This is because the current BCI/adaptive stimulation literature primarily provides causal evidence limited to local subsystems and tasks, rather than branch-equivalence of whole-brain WBE.

## Main Critiques

### 1. `verification.md` advocated "causal perturbation" but did not separate the stages of evidence.

- Issue:
- The old version showed `Stage A/B/C`, but the differences between `online human-in-the-loop`, `bidirectional feedback`, `state-dependent intervention`, `longitudinal stability` were not fixed in the form of a table.
- Therefore, there remained a structure in which the improvement in offline performance could be interpreted as an overstatement of progress closer to L2/L3.
- Basis:
- Forenzo et al. (2024) showed online continuous tracking of non-invasive BCI, but this is a demonstration of online decoding and is not a counterfactual equivalence.
- Flesher et al. (2021) showed that a bidirectional loop with tactile feedback improves behavior, but it remains a local causal gain in the sensorimotor subsystem.
- Oehrn et al. (2024) and Dixon et al. (2026) presented at-home/real-life block evaluations of adaptive DBS, showing an additional barrier between short lab demos and deployable controllers.
- Wairagkar et al. (2025) and Wilson et al. (2025) showed that even if a low-latency loop is implemented, decoder drift / recalibration burden remains another problem.
- Revision:
- Reorganized `causal perturbation suite` of `verification.md` to `4-gated`.
- `online decode`, `bidirectional perturbation`, `state-dependent intervention`, `longitudinal stability` are clearly indicated on separate lines, and representative primary literature and "things that cannot be said yet" are attached to each.
- The pass/fail index has been raised not only to `effect size` but also to `P50/P95/P99 latency`, `jitter`, `dropout`, `recalibration burden`, `recovery time`.

### 2. `wiki/counterfactual-and-perturbation-verification.md` was biased toward conceptual organization and borderline cases were too weak.

- Issue:
- The previous edition explained `intervention`, `counterfactual`, and `perturbation` in everyday language, but the structure made it difficult for readers to determine what and to what extent it had been proven in actual primary literature.
- In particular, the weakness was that the word `counterfactual` could be read as being usable without prefixing branch variables or comparison rules.
- Basis:
- Wairagkar et al. (2025) demonstrated a low-latency voice loop, but the performance of the fixed decoder deteriorated after about 15 days, so long-term stability must be treated as a separate issue.
- Casali et al. (2013) and Comolatti et al. (2019) made it possible to implement perturbation-based metrics, but they are not comparable without fixing stimulus conditions and artifact handling.
- Willett et al. (2023) and Littlejohn et al. (2025) advanced speech neuroprosthesis, but demonstrated online decode/control of communication subsystems, not branch-equivalence.
- Revision:
- Reorganized the text into `Five-step causal evidence ladder` and `Borderline cases in primary literature`.
- The following four conditions have been fixed as the usage conditions for `counterfactual`: `branching variable`, `comparison rule`, `artifact window`, and `failure condition`.
- Introduced `Intervention Response Test` and `Perturbation Generalization Test` as weaker but less misleading expressions.

### 3. `wiki/closed-loop-latency-jitter-and-safety-stops.md` had a delay definition but lacked operational indicators

- Issue:
- While the old version was correct in distinguishing between `delay/jitter/drift/abandon/safety stop`, it was abstract about what should actually be logged.
- This does not stop the misunderstanding of showing only the average latency and reading it as `L3 achievement`.
- Basis:
- Littlejohn et al. (2025) clearly demonstrated that a delay of several seconds can be a cause for failure in naturalistic communication, and showed that tail latency is important in speech systems.
- Wairagkar et al. (2025) returned silence in the non-speech section while running raw-to-speech in less than 10 ms. This shows that not only latency but also abstention implementation is required.
- Wilson et al. (2025) stated that frequent recalibration itself is a major obstacle to neural bypass, and showed that recalibration burden cannot be separated from performance.
- Cascino et al. (2026), published on February 25, 2026, reported that 9 out of 20 consecutive cases were aDBS candidates, and 5 cases continued as of July 2025, indicating that deployability and programming burden cannot be separated from implementation results.
- Revision:
- Added a new `Reality shown by primary literature` section and listed the literature on speech BCI, bidirectional BCI, adaptive DBS, and long-term recalibration.
- Clarified `P50/P95/P99 latency`, `jitter`, `dropout`, `recalibration burden`, `abstention / hold-last-output`, `recovery time`, `stimulation duty cycle` as `minimum desired indicators if you insist on L3`.
- Added a rule to separate `abstain`, `hold-last-output`, `freeze`, `hard stop` and treat the number of stops itself as a performance indicator.

## Changes Made This Round

- `verification.md`
- Revised `Causal Perturbation Suite` to `4-Gated`
- Explicit conditions for using `counterfactual`
- Added BCI / adaptive stimulation primary literature from 2023-2026 to the bibliography
- Corrected the year notation of `Unnwongse et al.` to 2023.
- `wiki/counterfactual-and-perturbation-verification.md`
- Updated the front matter and redesigned the page to be based on primary literature.
- Added `5-step ladder`, `boundary case`, `conditions for use of counterfactuals`, `minimum log`
- New reference bibliography centered on primary papers
- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- Updated front matter and redesigned `Practical indicators` centered page
- Added primary literature for speech neuroprosthesis / tactile BCI / adaptive DBS / recalibration
- Added `L3 minimum deliverables pack` and `Separation of stop types`

## Deferred External-Dependency Tasks

- Implementation of `Stage C` benchmark including real subject intervention
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisites: IRB, equipment, subject operations, stimulation safety protocols
- Completion condition: The experiment is run with stimulus conditions, artifact windows, stopping conditions, and failure conditions fixed in advance, and with a public log that can be peer reviewed.
- Long-term closed loop site-wide benchmark
- Person in charge: AI / maintainer
- Prerequisite: Securing publicly available longitudinal BCI / adaptive stimulation datasets or operational logs
- Completion condition: be able to reproduce and implement `Gate 4` of `verification.md` as a public bench.

## References

- Forenzo D, Zhu H, Shanahan J, Lim J, He B. Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. PNAS Nexus. 2024.
  - https://doi.org/10.1093/pnasnexus/pgae145
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Moses DA, Metzger SL, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021.
  - https://doi.org/10.1126/science.abd0380
- Wilson GH, Bray N, Franken M, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. Nat Med. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Dixon S, Oehrn C, Remple M, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. Nat Biomed Eng. 2026.
  - https://doi.org/10.1038/s41551-025-01592-5
- Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson’s disease: ADAPT-START findings and programming principles. npj Parkinsons Dis. 2026.
  - https://doi.org/10.1038/s41531-026-01269-z
- Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med. 2013.
  - https://doi.org/10.1126/scitranslmed.3006294
- Comolatti R, Pigorini A, Casarotto S, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. Brain Stimul. 2019.
  - https://doi.org/10.1016/j.brs.2019.05.013
