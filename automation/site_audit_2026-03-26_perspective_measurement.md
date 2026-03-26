# Site Deep Audit 2026-03-26: `perspective.md` measurement and execution claims

## Selected target

This audit selected the `perspective.md` section around:

- `Substance and Reproducibility of the project`
- `Research Program`

This was chosen because it is central to the site's public framing, but it was still less rigorous than the updated standards already enforced in [`eeg_101.md`](../eeg_101.md), [`verification.md`](../verification.md), and [`tech_roadmap.md`](../tech_roadmap.md).

## Why this section needed deeper correction

### 1. The old roadmap compressed distinct evidence classes into one linear phase table

The previous `Research Program` table implicitly treated the following as one continuous engineering ladder:

- sharable measurement packages
- source-imaging validation
- multimodal fusion
- local causal perturbation
- speech neuroprosthesis
- WBE-relevant verification

That compression is not supported by the primary literature.

- Tang et al. (2023) showed non-invasive semantic reconstruction, but under participant-specific training and cooperative use rather than subject-independent or WBE-like readout.
- Willett et al. (2023), Littlejohn et al. (2025), and Wairagkar et al. (2025) demonstrated strong communication-subsystem BCIs, not whole-brain equivalence.
- Hernandez-Pavon et al. (2023), Gogulski et al. (2024), and Biabani et al. (2024) showed that TMS-EEG interpretation remains conditional on stimulation parameters, target-specific reliability, and sensory contamination control.
- Rohaut et al. (2024) and Manasova et al. (2026) showed that multimodal gains are bundle-conditioned and modality-specific, not one interchangeable consciousness meter.
- Beiran and Litwin-Kumar (2025) showed that even connectome-constrained models remain dynamically degenerate until additional recordings collapse the compatible state space.

Conclusion:
The site should not present one straight phase ladder from EEG/fMRI setup to "Neural Turing Test" language. It should separate executable repository work from external-dependency experiments and keep each at its own claim ceiling.

### 2. The old reproducibility wording over-read the current repository state

The previous wording said the project was "gradually building an analysis pipeline" and promised publication of decoding code and dummy-data pipelines, but the current repository state is still documentation-first.

Repository inspection on this run showed:

- public pages and wiki/export toolchain are present
- `dataset_description.json` exists
- the `scripts/` directory is dominated by GitHub Wiki export/validation tooling
- there is not yet a public EEG analysis package with fixed environment, named dataset snapshot, executable preprocessing/metric scripts, and expected outputs that a third party can rerun end to end

Conclusion:
The page should explicitly say that current public output is mainly documentation, schema, audit format, and publishing infrastructure, not a finished executable EEG benchmark package.

### 3. External-dependency experiments were not separated clearly enough

The site-wide operating rules already require separating what can be executed in-session from what depends on external resources. The old `Research Program` section did not do this clearly enough.

Examples of external dependencies:

- simultaneous HD-EEG/fMRI acquisition
- TMS-EEG / PCI acquisition
- intracranial stimulation or simultaneous SEEG/ECoG validation
- chronic speech-neuroprosthesis studies

These require some combination of:

- IRB / clinical approval
- participant recruitment
- specialized hardware
- clinical partnerships
- longitudinal operations

Conclusion:
The page should label these explicitly as external-dependency tasks and state the strongest safe wording until they are actually executed.

### 4. Several labels were not yet operationally defined

Terms such as:

- `personality maintenance`
- `WBA integration framework`
- `Neural Turing Test`

were still too coarse in this section. The rest of the site has already moved toward operational cards, validation classes, calibration logs, abstention boundaries, and external-validation ladders. This section needed to adopt the same style instead of reintroducing slogan-like labels.

Conclusion:
Replace those labels with concrete public outputs:

- evaluation packs
- audit cards
- validation-class registries
- missing-state ledgers
- external-dependency task lists

## Changes applied in this run

### `perspective.md`

- Rewrote the `Research Program` section into an evidence-aligned plan.
- Added a literature-backed explanation for why the old linear roadmap was too coarse.
- Split the work into:
  - repository-executable work
  - external-dependency tasks
- Rewrote the reproducibility section so it describes the current repository honestly.
- Added a table separating:
  - what is already public now
  - what is still missing before L0 third-party reproducibility

## Main references used for the correction

- Tang, J. et al. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. Nature Neuroscience. DOI: https://doi.org/10.1038/s41593-023-01304-9
- Hernandez-Pavon, J. C. et al. (2023). TMS combined with EEG: Recommendations and open issues. Brain Stimulation. DOI: https://doi.org/10.1016/j.brs.2023.02.009
- Gogulski, J. et al. (2024). Reliability of the TMS-evoked potential in dorsolateral prefrontal cortex. Cerebral Cortex. DOI: https://doi.org/10.1093/cercor/bhae130
- Biabani, M. et al. (2024). Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. Imaging Neuroscience. DOI: https://doi.org/10.1162/imag_a_00349
- Rohaut, B. et al. (2024). Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. Nature Medicine. DOI: https://doi.org/10.1038/s41591-024-03019-1
- Willett, F. R. et al. (2023). A high-performance speech neuroprosthesis. Nature. DOI: https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn, K. T. et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nature Neuroscience. DOI: https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar, M. et al. (2025). An instantaneous voice-synthesis neuroprosthesis. Nature. DOI: https://doi.org/10.1038/s41586-025-09127-3
- Beiran, M. and Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. Nature Neuroscience. DOI: https://doi.org/10.1038/s41593-025-02080-4
- Manasova, D. et al. (2026). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. Brain. DOI: https://doi.org/10.1093/brain/awaf412
