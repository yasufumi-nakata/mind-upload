# Site Deepening Audit (2026-03-14, Dataset Toolchain / Benchmark Reproducibility)

## Scope

- Main target: `datasets.md`
- Secondary target: `wiki/standards-repositories-validators-and-benchmarks.md`
- Secondary target: `wiki/l0-minimum-artifact-pack.md`

## Why This Page Was Selected

- The public site has already been organized to the general outline of ``BIDS is the standard, OpenNeuro is the place to be, Benchmark is the comparison rule``.
- However, as of 2026-03-14, it was not sufficiently established in the practical guidance that `Even if the dataset name is the same, different snapshots/versions are different inputs`, `loader/transformer like MNE-BIDS` and `benchmark harness like MOABB` are different things.
- This lack is a weakness from a technical/natural science perspective. This is because in reproducible analysis of L0, comparability itself does not hold unless `which version of the input was compared with which evaluation family` is fixed before the high-performance model.

## Main Critiques

### 1. The current site conceptually separated `Standard / Place / benchmark`, but `Version fixed` was missing.

- Issue:
- The previous version introduced `OpenNeuro` and `PhysioNet` as locations, but there was room for it to be read as if the same input was specified just by the dataset name.
- However, the snapshot / version can change even with the same dataset name on a public repository.
- Basis:
- OpenNeuro's official docs clearly states that snapshots are treated as semantic version git tags.
- PhysioNet's project pages and citation guidance indicate the version for each resource and cite that version.
- Revision:
- Added site rule to `datasets.md` and `wiki/l0-minimum-artifact-pack.md` to include `snapshot / version / DOI / retrieved date` instead of the dataset name in the minimum deliverables.
- Version fixation has been made an independent issue as `Input ID` in `wiki/standards-repositories-validators-and-benchmarks.md`.

### 2. The current site did not separate `readable` and `fairly comparable` enough

- Issue:
- In the old version, `Align to BIDS`, `Pass through Validator`, `Compare with Benchmark` were written, but `I/O path like MNE-BIDS` and `evaluation engine like MOABB` in between were missing.
- As a result, a structure remained that could be misread by readers as `Readable by MNE-BIDS = reached benchmark`.
- Basis:
- MNE-BIDS by Appelhoff et al. (2019) is software that provides a path for organizing BIDS datasets, extracting metadata, and loading them into MNE.
- The current docs of MNE-BIDS notes `BIDS was originally designed for unprocessed or minimally processed data` about `write_raw_bids()`, and treats writing back modified/preloaded data as an exception.
- MOABB by Jayaram & Barachant (2018) is a framework that fixes paradigm and evaluation for the purpose of trustworthy algorithm benchmarking for EEG-based BCI.
- MOABB's official docs also organizes within-session / cross-session / cross-subject as a separate evaluation family.
- Revision:
- Added `5 layers` table to `wiki/standards-repositories-validators-and-benchmarks.md` and separated standards, public version, conversion/reading, benchmark harness, and learning device.
- Added `Execution chain to be fixed after storage` and `Step 2.5: Fix loader and benchmark separately` to `datasets.md`.

### 3. `evaluation family` and `dataset version` were not explicitly specified in the current L0 artifact pack

- Issue:
- The old `wiki/l0-minimum-artifact-pack.md` listed BIDS, QC, splits, baselines, execution steps, and failure examples, but did not treat `Which edition of the data` and `Within-session / cross-session / cross-subject` as independent artifacts.
- This cannot prevent cases where the same score has different meanings.
- Basis:
- MOABB docs defines paradigm and evaluation family independently, and even if the same pipeline has a different evaluation family, the comparison meaning will change.
- OpenNeuro / PhysioNet makes dataset versioning explicit, and the dataset name alone is not sufficient.
- Revision:
- Updated `wiki/l0-minimum-artifact-pack.md` from `7 points` to `8 points` and added `data version` at the beginning.
- Clarified evaluation family in the split rule and changed `Can others have the same version of input` to the first completion judgment.

## Changes Made This Round

- `datasets.md`
- Added repository / BIDS / loader / benchmark practical chain
- Added `version pin` and `evaluation family` to L0 checklist and confirmation table.
- Added primary sources for OpenNeuro, PhysioNet, MNE-BIDS, MOABB to bibliography
- `wiki/standards-repositories-validators-and-benchmarks.md`
- Expanded the concept explanation of `4 layers` to the operation table of `5 layers`
- Clarify `dataset name alone is not enough`, `MNE-BIDS ≠ benchmark`, `MOABB score depends on evaluation family`
- Added `4 IDs` and `5 questions`
- `wiki/l0-minimum-artifact-pack.md`
- Updated `7 points` to `8 points` and added `Data version`
- Updated completion judgment to `same version input` standard

## Deferred External-Dependency Tasks

- Unification of site-wide benchmark schema
- Person in charge: AI / maintainer
- Prerequisite: Decide how much `within-session / cross-session / cross-subject` should be used as standard language throughout the public page.
- Completion condition: `datasets.md`, `verification.md`, evaluation family name and minimum submissions must be consistent between related wikis.

## References

- BIDS Specification: Electroencephalography
  - https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Scientific Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- OpenNeuro Docs: Git access and snapshots
  - https://docs.openneuro.org/git.html
- OpenNeuro Docs: User guide
  - https://docs.openneuro.org/user_guide.html
- PhysioNet: About
  - https://physionet.org/about/
- PhysioNet: Resources
  - https://physionet.org/about/content/
- Appelhoff S, Sanderson M, Brooks TL, et al. MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. J Open Source Softw. 2019.
  - https://doi.org/10.21105/joss.01896
- MNE-BIDS Docs: write_raw_bids
  - https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html
- Jayaram V, Barachant A. MOABB: trustworthy algorithm benchmarking for BCIs. Journal of Neural Engineering. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- MOABB Docs
  - https://moabb.neurotechx.com/docs/index.html
- MOABB Docs: paradigm and evaluation examples
  - https://moabb.neurotechx.com/docs/auto_examples/paradigm_examples/index.html
