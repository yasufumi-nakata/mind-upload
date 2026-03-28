# Site Deepening Audit (2026-03-15, Perspective / Consciousness Metrics Reference Integrity and Construct Validity)

## Scope

- Main target: `perspective.md`
- Secondary target: `automation/site_deepening_audit_2026-03-14_perspective_consciousness_markers.md`

## Why This Page Was Selected

- Although consciousness metrics on the `tech_roadmap.md` side were pretty well organized as of 2026-03-15, two types of weaknesses still remained in the `Measuring consciousness with EEG` section of `perspective.md`.
- First, the DOI/bibliographic information for references 103-105 did not match the actual primary literature. This is not just a typographical error; it also destroys verifiability because a third party cannot trace the evidence.
- Second, while the main text repositioned no-report as confound control, it still failed to bring to the fore the problem of `construct validity` that the 2025 criterion placement paper showed.
- Therefore, this time, I decided that it would be most effective to do ``rigorize content'' and ``restore consistency of bibliography'' at the same time.

## How to check

- Checked whether references 103-105 of `perspective.md` match actual primary document titles using DOI content negotiation and Crossref metadata.
- We then reviewed the correspondence between the strength of the main text's claims and the references based on primary literature metadata from Current Biology, European Journal of Neuroscience, Brain, eLife, and Nature.

## Main Critiques

### 1. Misidentification of references 103-105 compromised verifiability prior to the main text

- Issue:
- The old `perspective.md` ref-103 referred to `10.1016/j.cub.2025.03.031` as `Neural correlates of auditory awareness under no-report conditions`, but this DOI was not that paper.
- `10.1093/brain/awaf332` in ref-104 and `10.1093/brain/awaf287` in ref-105 also did not match the consciousness / DoC paper mentioned in the main text.
- Why it's important:
- This section is often referenced as a site-wide position statement. If the DOI is off here, the reader will not be able to see ``Which paper is really the basis?''.
- For scientific pages, `Being able to follow the reference' is the minimum requirement before strength of argument.
- Revision:
- Replaced ref-103 with Dellert et al. (2025) `Neural correlates of consciousness in an auditory no-report fMRI study`.
- Replaced ref-104 with Casarotto et al. (2024) `Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state`.
- Replaced ref-105 with Manasova et al. (2026) `Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness`.

### 2. Writing no-report is not enough; construct validity will be broken if criterion placement is not audited separately.

- Issue:
- In the old version, it was possible to write up to `no-report = confound control`, but the point where the fluctuation of the response criterion broke the interpretation of the neural marker was not fixed as an independent condition.
- Basis:
- Fahrenfort et al. (2025) showed that the construct validity of conscious content markers is threatened simply by differences in criterion placement.
- Therefore, `Do not report` alone is not sufficient, and `What criteria did you use to decide yes/no` must also be recorded in a separate log.
- Revision:
- Extended `4 conditions fixed first in this section` to `5 conditions` and added criterion placement as an independent condition.
- Site rule has also been updated to `no-report / criterion placement = confound control`.

### 3. The evidence of auditory no-report is the basis of confound-control, not the basis of EEG benchmark

- Issue:
- The structure of the previous edition was such that some readers could read the auditory no-report paper as if it were the direct basis for a `measuring consciousness with EEG` claim.
- Basis:
- The paper by Dellert et al. (2025) is an auditory no-report **fMRI** study.
- This paper supports the point that a no-report design separates post-perceptual confounds even in the auditory domain, not the bedside deployability of EEG alone.
- Revision:
- Added note-box `construct validity as a separate audit` and specified no-report evidence across modalities as `confound control`.

### 4. Unless you specify the contents of multimodal validation, the word "multimodal" will take on a life of its own.

- Issue:
- The `multimodal clinical panel` line in the old version was generally in the correct direction, but it was unclear which modality was effective for what.
- Basis:
- Manasova et al. (2026) reinforced the need to evaluate the diagnosis/prognosis of DoC in a multimodal/multisite manner and read it as a bundle of behavioral evaluation, HD-EEG, MRI, PET, and clinical variables rather than a single indicator.
- Revision:
- Changed the expression to `multisite panel that bundles behavioral evaluation, HD-EEG, MRI, PET, and clinical variables` to make multimodal more concrete.

## Changes Made This Round

- `perspective.md`
- Updated the opening sentence of the `Measuring consciousness with EEG` section to read `no-report + criterion placement + resting-state calibration + multisite validation`
- Updated site rule to `no-report / criterion placement = confound control`
- Added note-box for `construct validity as a separate audit`
- Update `4 conditions fixed first in this section` to `5 conditions`
- Added criterion placement audit to phase 0 / ToDo
- Corrected phase 2 spontaneous-vs-evoked dissociation literature to Casarotto et al. (2024)
- Corrected multimodal panel and concluding paragraph to Manasova et al. (2026)
- Modified ref-103 / ref-104 / ref-105 to match primary literature metadata
- Added Fahrenfort et al. (2025) as ref-113
- `automation/site_deepening_audit_2026-03-14_perspective_consciousness_markers.md`
- Corrected incorrect bibliographic information in audit memo

## Deferred External-Dependency Tasks

- Public bench implementation of no-report / criterion placement / perturbation / multimodal validation in the same cohort
- Person in charge: AI / maintainer / experimental joint researcher
- Prerequisites: task implementation, clinical collaboration, TMS-EEG or alternative perturbation, simultaneous measurement with behavioral assessment
- Completion condition: There must be a public log that allows comparison of no-report conditions, criterion placement, PCI-based indicators, and outcome predictions using the same schema.

## References

- Ferrante O, et al. Adversarial testing of global neuronal workspace and integrated information theories of consciousness. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08888-1
- Tsuchiya N, et al. No-Report Paradigms: Extracting the True Neural Correlates of Consciousness. *Trends Cogn Sci*. 2015.
  - https://doi.org/10.1016/j.tics.2015.10.002
- Cohen MA, et al. Neural signatures of visual awareness independent of postperceptual processing. *Cereb Cortex*. 2024.
  - https://doi.org/10.1093/cercor/bhae415
- Dellert T, et al. Neural correlates of consciousness in an auditory no-report fMRI study. *Curr Biol*. 2025.
  - https://doi.org/10.1016/j.cub.2025.10.026
- Fahrenfort JJ, et al. Criterion placement threatens the construct validity of neural measures of consciousness. *eLife*. 2025.
  - https://doi.org/10.7554/eLife.102335
- Casali AG, et al. A theoretically based index of consciousness independent of sensory processing and behavior. *Sci Transl Med*. 2013.
  - https://doi.org/10.1126/scitranslmed.3006294
- Comolatti R, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. *Brain Stimul*. 2019.
  - https://doi.org/10.1016/j.brs.2019.05.013
- Hernandez-Pavon JC, et al. TMS combined with EEG: Recommendations and open issues. *Brain Stimul*. 2023.
  - https://doi.org/10.1016/j.brs.2023.02.009
- Maschke C, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. *Commun Biol*. 2024.
  - https://doi.org/10.1038/s42003-024-06613-8
- Casarotto S, et al. Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. *Eur J Neurosci*. 2024.
  - https://doi.org/10.1111/ejn.16299
- Manasova D, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026.
  - https://doi.org/10.1093/brain/awaf412
