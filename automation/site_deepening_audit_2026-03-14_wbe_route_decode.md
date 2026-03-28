# Site Deepening Audit (2026-03-14, WBE Route / Decode-Emulate)

## Scope

- Main target: `wbe_101.md`
- Secondary target: `wiki/decode-vs-emulate.md`

## Why This Page Was Selected

- `wbe_101.md` is the entrance to the public site, and if the comparison axis here is not easy, the reading of the entire lower page will be distorted.
- The existing "comparison with alternative approaches" has a structure that can be read as a comparison of position preferences and future visions rather than a comparison of evidence from technology and natural science.
- `wiki/decode-vs-emulate.md` is a frequently referenced auxiliary page, but it only serves as a conceptual explanation and lacks borderline cases based on primary literature.

## Main Critiques

### 1. The `wbe_101.md` comparison table looked like "position preference" rather than "technology route comparison"

- Issue:
- The existing table clearly states `Gradual replacement (adopted by Mind-Upload)`, and the route preference was fixed first on the entrance page.
- However, as of March 2026, primary literature strongly supports non-invasive decoding, invasive speech BCI, local closed-loop Yoshitsugu, connectomics + function, and local digital twin.
- At the stage when the neuron-by-neuron whole-brain replacement benchmark could not be confirmed as a published primary document, calling a specific route ``adopted'' was a way of writing that placed the conclusion before the strength of the evidence.
- Basis:
- Tang et al. (2023) demonstrated semantic recovery of continuous language using non-invasive fMRI, but decoding is required and subject cooperation is required.
- Willett et al. (2023) demonstrated a vocabulary of 125,000 words at 62 words/min with invasive speech BCI, which also focuses on attempted speech decoding.
- Flesher et al. (2021) improved the grasping task with a bidirectional BCI that returns tactile feedback, but this is a closed loop demonstration of the sensorimotor subsystem rather than the whole brain.
- Berger et al. (2011) showed a local connection in the hippocampus, but it is task-specific and local.
- Revision:
- The comparison table for `wbe_101.md` has been reorganized into four columns for `Root / Currently published proof / What can be said so far / What is still missing`.
- Changed the axis of comparison to `measurement density / intervention possibility / closed-loop demonstration / state completeness` instead of philosophical continuity.

### 2. The existing comparison table describes the limits of connectomics and simulation too roughly

- Issue:
- `Whole Brain Simulation` was written as "the most faithful reproduction possible", but this was an expression that ignored the difficulty of parameter identifiability.
- `Scan & Copy` also only says "required resolution is unrealistic", so I couldn't see which state variables were missing.
- Basis:
- Dorkenwald et al. (2024) and MICrONS Consortium et al. (2025) demonstrate that the coupling of connectome and functional measurements is finally at a major step forward.
- Billeh et al. (2020) built a data-driven multi-scale V1 model, but it is a domain- and issue-limited model.
- Prinz et al. (2004) show that nearly identical network activities can result from widely different sets of internal parameters, and output matching alone does not guarantee faithful simulation.
- Revision:
- Repositioned connectomics as `structural atlas / scaffold / hypothesis engine`.
- Changed simulation to `testing mechanistic hypotheses and local digital twin` and specified it as `output match is not sufficient unless identifiability is solved`.

### 3. `wiki/decode-vs-emulate.md` was only a conceptual explanation, and borderline cases were not supported by literature.

- Issue:
- The existing pages mainly contained everyday examples, and did not include strong decode examples such as Tang 2023 and Willett 2023, or local closed-loop Yoshitsugu examples such as Flesher 2021 and Berger 2011.
- As a result, it was difficult for readers to understand ``what is the upper limit of decode'' and ``what is close to local emulate''.
- Basis:
- Tang 2023 is a high-end example of non-invasive decoding.
- Willett 2023 is an upper bound example of invasive decoding.
- Flesher 2021 and Berger 2011 are local evidences that move towards the causal/closed-loop side.
- Revision:
- Added a new `Boundary cases seen in primary literature` clause and arranged the four routes with a gradient of decode → local emulate.
- Fixed OOD generalization, intervention matching, closed-loop stability, and state completeness as `four gates`.

### 4. The reference set on the entry page did not match the current technology comparison.

- Issue:
- The existing `wbe_101.md` bibliography contains philosophical literature and was not consistent with the basis of the updated `Technology route comparison` section.
- Revision:
- Replaced the references with a focus on Tang / Willett / Flesher / Berger / Dorkenwald / MICrONS / Billeh / Prinz and organized them into sets that directly support this comparison table.

## Changes Made This Round

- `wbe_101.md`
- Completely revised `Comparison with alternative approaches` section to `Comparison of technology routes (observable evidence base)`
- Removed route preference and changed to evidence profile comparison of published primary literature
- Replaced references with focus on technology and natural sciences
- `wiki/decode-vs-emulate.md`
- Updated front matter for technology and natural sciences
- Expanded the text that was just a concept explanation to a boundary case page with primary references
- Added `Four Gates` and `Rules for operation on this site`

## Deferred External-Dependency Tasks

- Continuous monitoring of public benchmarks for whole-brain scale hybrid replacement/gradual replacement
- Person in charge: AI / maintainer
- Prerequisite: emergence of new primary literature or public datasets
- Completion condition: Identify a reproducible benchmark that evaluates neuron-by-neuron or multi-area replacement and add it to the `wbe_101.md` comparison table.

## References

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021.
  - https://doi.org/10.1126/science.abd0380
- Berger TW, Hampson RE, Song D, et al. A cortical neural prosthesis for restoring and enhancing memory. J Neural Eng. 2011.
  - https://doi.org/10.1088/1741-2560/8/4/046017
- Dorkenwald S, McKellar CE, Macrina T, et al. Neuronal wiring diagram of an adult brain. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Billeh YN, Cai B, Gratiy SL, et al. Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex. Neuron. 2020.
  - https://doi.org/10.1016/j.neuron.2020.01.040
- Prinz AA, Bucher D, Marder E. Similar network activity from disparate circuit parameters. Nat Neurosci. 2004.
  - https://doi.org/10.1038/nn1352
