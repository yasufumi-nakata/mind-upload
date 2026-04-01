# Site Deepening Audit (2026-04-01, Perspective Clearance Route-Role Split)

## Scope

- Primary target:
  - `perspective.md`
- Research scope:
  - technology
  - natural science
- Explicitly excluded:
  - philosophy
  - law

## Why This Topic Was Chosen

- `perspective.md` is the site's longest public synthesis page, and it is where readers can most easily carry an overcompressed family label into later reasoning.
- By 2026-04-01, the central rule pages had already split human clearance-support evidence into multiple route families.
- However, `perspective.md` still retained a comparatively coarse `Human CSF mobility / sleep-linked clearance proxy` row and several summary passages that compressed distinct transport objects into one support-state rung.
- That mismatch mattered because the page already claimed to separate proxy class, operational maturity, and calibrator role. Leaving the clearance family compressed made the page internally inconsistent with its own method.

## Evidence-Based Critique

### 1. `clearance / glymphatic evidence` was still too coarse on the Perspective page

- Problem:
  - The page still allowed readers to treat CSF mobility, glymphatic exchange, meningeal-lymphatic transport, and brain-to-plasma biomarker efflux as if they were one route family with one direct observable.
- Why this is technically weak:
  - The primary literature does not report one shared object.
  - It reports at least:
    - macroscopic CSF oscillation during sleep
    - parenchyma-CSF water exchange
    - respiration-conditioned net flow
    - exercise-conditioned contrast influx / parasagittal meningeal-lymphatic flow
    - intrathecal tracer retention / CSF-to-blood clearance capacity
    - CSF mobility around perivascular spaces
    - model-based brain-to-plasma biomarker efflux
- Consequence:
  - If these rows are left compressed, readers can silently overread `clearance evidence exists` into `the relevant local maintenance controller has nearly been observed`.

### 2. The compressed row hid different carrier classes, crossed boundaries, and intervention regimes

- Problem:
  - The older Perspective wording did not keep visible whether the route involved endogenous oscillation, water exchange, respiration training, exercise-conditioned contrast dynamics, intrathecal tracer pharmacokinetics, or a multicompartment model for plasma biomarkers.
- Why this is technically weak:
  - These factors materially change what the route means.
  - They are not metadata details; they are part of the inferential object.
- Primary evidence:
  - Fultz et al. (2019) constrain coupled electrophysiological, hemodynamic, and CSF oscillations during sleep rather than protein-specific efflux.
  - Kim, Huang, & Liu (2025) constrain parenchyma-CSF water exchange, not meningeal-lymphatic egress or protein clearance.
  - Lim et al. (2025) constrain respiration-conditioned CSF net flow in awake humans, not route-free whole-brain bulk clearance.
  - Yoo et al. (2025) constrain exercise-conditioned putative glymphatic / meningeal-lymphatic contrast flow, not a natural-sleep baseline.
  - Eide et al. (2023) constrain intrathecal gadobutrol retention and CSF-to-blood clearance variables in neurological patients, not a healthy route-free controller readout.
  - Dagum et al. (2026) constrain model-based overnight Aβ / tau efflux to plasma under sleep manipulation, not local immune-controller identity.

### 3. The page's own three-axis rule required a family-internal split

- Problem:
  - `perspective.md` already tells readers to separate `proxy class`, `operational maturity`, and `calibrator role`.
  - But the clearance family itself was still under-specified.
- Why this is technically weak:
  - A family-internal collapse prevents all three axes from being read correctly.
  - A CSF mobility MRI route, an intrathecal tracer route, and a model-based biomarker-efflux route do not share one operational burden or one calibrator role.
- Required correction:
  - The clearance family had to be split directly in the main human-evidence table and in the surrounding prose, not only elsewhere on the site.

## Changes Executed In This Session

### `perspective.md`

- Updated the page note to record a `2026-04-01 clearance-route-role split`.
- Added a page-highlight bullet stating that clearance-support routes are not one row.
- Replaced the old single clearance row in the human-evidence table with seven route-role rows:
  - macroscopic CSF oscillation
  - parenchyma-CSF water exchange
  - respiration-conditioned net flow
  - exercise-conditioned contrast influx / meningeal-lymphatic flow
  - intrathecal tracer / CSF-to-blood clearance
  - CSF mobility
  - model-based biomarker efflux
- Added a new note box explaining why `clearance evidence exists` is too coarse a reading category.
- Updated the `proxy class / operational maturity / calibrator role` note so the clearance family is split inside the prose, not only in the table.
- Updated the composition-failure table so the quantity-type and operational-maturity examples now reflect the internal split of the clearance family.
- Updated the `Gap between connectome and dynamics` section so the long-form synthesis no longer compresses the clearance family into one support-state proxy row.
- Added the relevant clearance-route references to the Perspective bibliography.

## Verification

- `ruby scripts/build_summary_booklet.rb`
  - Result:
    - succeeded
    - regenerated `summary_booklet.md` without leaving a tracked diff
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - Result:
    - succeeded
    - rendered the updated Perspective page into `_site/`
- Generated-page spot check:
  - confirmed that the built Perspective output contains the new clearance-family split and note-box text

## External Dependency Tasks

- None.
  - The work only required literature review, repository edits, local build verification, and Git operations executable in this session.

## References

1. Fultz NE, Bonmassar G, Setsompop K, et al. Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. *Science*. 2019.
   - https://doi.org/10.1126/science.aax5440
2. Eide PK, Lashkarivand A, Pripp AH, et al. Plasma neurodegeneration biomarker concentrations associate with glymphatic and meningeal lymphatic measures in neurological disorders. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-37685-5
3. Kim D, Huang Y, Liu J. Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121142
4. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
5. Lim C, Chen C, Zhang C, et al. Human cerebrospinal fluid net flow enhanced by respiration during the awake state. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66548-4
6. Yoo R-E, Kim J-H, Moon HY, et al. Long-term physical exercise facilitates putative glymphatic and meningeal lymphatic vessel flow in humans. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-58726-1
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
