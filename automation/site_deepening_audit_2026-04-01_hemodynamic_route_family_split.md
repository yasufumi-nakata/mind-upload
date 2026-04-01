# Site Deepening Audit (2026-04-01, Hemodynamic Route-Family Split)

## Scope

- Primary target: `wiki/measurement-stack-and-claim-ceiling.md`
- Secondary target: `verification.md`

## Why This Topic Was Chosen

- The site already had the right high-level caution that `BOLD / fNIRS amplitude is not automatically a neural difference`.
- However, the central rule pages still compressed several technically different hemodynamic routes into one practical row.
- That compression mattered because those pages set the claim ceiling for the whole site.
- As long as the central table still treated hemodynamic work as one family, readers could still slide from:
  - uncalibrated amplitude
  - transfer-side calibration
  - model-conditioned oxygen-metabolism estimation
  into one imagined `stronger hemodynamic truth meter`.

## Evidence-Based Critique

### 1. The central table still treated hemodynamic work as one stack even though the literature no longer supports one row

- Problem:
  - `wiki/measurement-stack-and-claim-ceiling.md` still had one row for `fMRI / hemodynamic modalities`.
  - That row underdescribed the difference between plain amplitude, transfer-side correction, and metabolic-quantity estimation.
- Why this is technically weak:
  - Those routes do not answer the same question.
  - An amplitude result can remain dominated by vascular transfer.
  - A transfer-audited result can reduce one confound without becoming a neural-quantity readout.
  - A qBOLD / OEF / CMRO2 result is already a model-conditioned quantity route rather than a model-free truth layer.
- Primary evidence:
  - Murphy et al. (2011, DOI `10.1016/j.neuroimage.2010.07.059`) showed that inter-subject vascular reactivity differences materially shape BOLD interpretation.
  - Williams et al. (2023, DOI `10.3389/fphys.2023.1167148`) showed strong correspondence between task BOLD magnitude and CVR across cortex.
  - Epp et al. (2025, DOI `10.1038/s41593-025-02132-9`) showed that significant task BOLD changes can oppose oxygen-metabolism changes.
  - Jaroszynski et al. (2025, DOI `10.1002/nbm.70120`) showed that constrained qBOLD reaches OEF / CMRO2 through an explicit model stack with separate pCASL-based CBF input.

### 2. The old wording still left fNIRS too easy to overread after only a superficial cleanup

- Problem:
  - The site already warned that fNIRS has superficial/systemic confounds.
  - But the central rule pages still did not clearly say that short-channel-corrected fNIRS is a stronger transfer audit, not a promotion to direct neural readout.
- Why this is technically weak:
  - `noise reduced` and `neural quantity identified` are not the same result.
  - A reader could still mistakenly promote `short-separation used` into `the hemodynamic route is now mostly neural`.
- Primary evidence:
  - Yucel et al. (2015, DOI `10.1117/1.NPh.2.3.035005`) showed that short-separation regression improves significance and localization under differing autonomic responses.
  - An et al. (2025, DOI `10.1117/1.NPh.12.3.035009`) showed that short-channel regression still improves validity and sensitivity even in a working-memory paradigm with minimal motor burden.

### 3. Transfer-side calibration and quantity-bridge estimation still needed to be separated explicitly

- Problem:
  - Even after the existing vascular-state addendum, the site still left room to read `CVR-corrected amplitude` and `oxygen-metabolism estimate` as one upward step.
- Why this is technically weak:
  - A transfer-side calibration route narrows one nuisance family.
  - A quantity-bridge route introduces a named physiological model and quantity definition.
  - Those are different inferential objects and should not share one ceiling.
- Primary evidence:
  - Jaroszynski et al. (2025, DOI `10.1002/nbm.70120`) explicitly estimate OEF / CMRO2 from constrained qBOLD plus pCASL.
  - Epp et al. (2025, DOI `10.1038/s41593-025-02132-9`) show why plain BOLD sign cannot stand in for oxygen-metabolism sign.

### 4. Measurement-side vascular cleanup and maintenance-side neurovascular support still needed clearer separation

- Problem:
  - Without a sharper route-family split, a reader can still move from `vascular nuisance handled` to `support-state matched`.
- Why this is technically weak:
  - The first is a measurement-side audit.
  - The second concerns biological controller state in neurovascular-unit / BBB / pericyte systems.
  - Those are distinct inferential ladders throughout this project.
- Existing site evidence that required synchronization:
  - `verification.md` already warned that vascular transfer audit is not neurovascular support-state audit.
  - The measurement-stack table needed to match that stricter rule rather than lag behind it.

## Changes Executed In This Session

- `wiki/measurement-stack-and-claim-ceiling.md`
  - Rewrote the hemodynamic summary bullets so the page no longer describes hemodynamic work as one caution family.
  - Replaced the old single `fMRI / hemodynamic modalities` row with three rows:
    - uncalibrated amplitude
    - transfer-audited amplitude
    - model-conditioned oxygen-metabolism route
  - Rewrote the section-5 critique so it no longer stops at `BOLD is indirect`.
  - Added an explicit rule that CVR audit is not the same as a quantity bridge.
  - Added a hemodynamic route-family table separating amplitude, transfer audit, autonomic/global mode, and oxygen-metabolism routes.
  - Added two new primary references:
    - An et al. (2025)
    - Jaroszynski et al. (2025)
- `verification.md`
  - Updated the page highlight for the Fusion Card so hemodynamic route family is part of the required disclosure.
  - Added a new `known_points` rule that vascular-state / CVR audit does not itself create oxygen-metabolism or neurovascular-support readout.
  - Added a new Observability Budget row:
    - `hemodynamic route family / quantity type`
  - Tightened the Fusion Card so hemodynamic contribution must be declared as:
    - uncalibrated amplitude
    - transfer-side calibration
    - named OEF / CMRO2 quantity bridge
  - Rewrote the 2026-03-18 hemodynamic addendum so it now separates:
    - uncalibrated amplitude
    - transfer-audited amplitude
    - model-conditioned oxygen-metabolism route
  - Added the same two new primary references to the reference list.

## Verification Executed In This Session

- Ran `bundle exec jekyll build`
  - Result: success
- Ran `ruby -c scripts/export_github_wiki.rb`
  - Result: `Syntax OK`
- Ran `git diff --check`
  - Result: no whitespace or patch-format issues
- Confirmed the generated HTML contains the new route-family wording in:
  - `_site/wiki/measurement-stack-and-claim-ceiling.html`
  - `_site/verification.html`

## External Dependency Tasks

- None.
  - This session required only repository edits, literature-based critique, local verification, and Git operations executable in the current environment.

## References

1. Murphy K, Harris AD, Wise RG. Robustly measuring vascular reactivity differences with breath-hold: normalising stimulus-evoked and resting state BOLD fMRI data. *NeuroImage*. 2011.
   - https://doi.org/10.1016/j.neuroimage.2010.07.059
2. Williams RJ, Specht JL, Mazerolle EL, Lebel RM, MacDonald ME, Pike GB. Correspondence between BOLD fMRI task response and cerebrovascular reactivity across the cerebral cortex. *Frontiers in Physiology*. 2023.
   - https://doi.org/10.3389/fphys.2023.1167148
3. Wu S, Tyler LK, Henson RNA, Rowe JB, Cam-CAN, Tsvetanov KA. Cerebral blood flow predicts multiple demand network activity and fluid intelligence across the adult lifespan. *Neurobiology of Aging*. 2023.
   - https://doi.org/10.1016/j.neurobiolaging.2022.09.006
4. Yucel MAY, Selb J, Aasted CMA, Petkov MP, Becerra L, Borsook D, Boas DA. Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared spectroscopy for tasks with differing autonomic responses. *Neurophotonics*. 2015.
   - https://doi.org/10.1117/1.NPh.2.3.035005
5. An J, Goyal P, Luft AR, Schönhammer JG. Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load. *Neurophotonics*. 2025.
   - https://doi.org/10.1117/1.NPh.12.3.035009
6. Özbay PS, Chang C, Picchioni D, et al. Sympathetic activity contributes to the fMRI signal. *Communications Biology*. 2019.
   - https://doi.org/10.1038/s42003-019-0659-0
7. Bolt T, Wang S, Nomi JS, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01945-y
8. Epp SM, Castrillon G, Yuan B, Andrews-Hanna J, Preibisch C, Riedl V. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
9. Jaroszynski KM, Lee H, Langham MC, Wehrli FW. Comparison of brain oxygen metabolic parameters between constrained qBOLD and whole-brain oximetric methods at baseline and in response to a physiologic stimulus. *NMR in Biomedicine*. 2025.
   - https://doi.org/10.1002/nbm.70120
