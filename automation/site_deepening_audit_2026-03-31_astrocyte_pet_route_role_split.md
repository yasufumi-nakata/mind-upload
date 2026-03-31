# Site Deepening Audit (2026-03-31, Astrocyte PET Route-Role Split)

## Scope

- Primary target: `faq.md`
- Secondary targets: `wiki/homeostatic-plasticity-and-maintenance-state.md`, `verification.md`, `wbe_101.md`, `mind_uploading_papers.md`

## Why This Topic Was Chosen

- The site was already stronger than average at separating destructive ultrastructure from living-human proxy routes and at splitting astrocyte PET by target class (`MAO-B` versus `I2BS`).
- However, the public wording still remained too coarse inside the human `SMBT-1 / MAO-B` family itself.
- That gap matters technically because the current literature does not support treating `first-in-human target validation`, `AD-spectrum disease contrast`, `brain quantification`, and `whole-body biodistribution` as one interchangeable line of evidence.
- The resulting compression risk was visible on the public pages: readers could still overread one astrocyte PET citation as if it simultaneously settled target validity, disease-context relevance, quantification regime, and tracer-burden burden.

## Evidence-Based Critique

### 1. The route family was split by target class, but not yet by route role inside SMBT-1

- Problem:
  - The site already separated `MAO-B` and `I2BS`.
  - But the human `SMBT-1` line could still be read as one common route.
- Why this is technically weak:
  - `first-in-human tracer validation` answers a different question from `disease-context contrast`.
  - `brain quantification` answers a different question from `whole-body biodistribution`.
  - Without this split, a reader can silently move from `target binds in humans` to `therefore the route is ready as a stable disease or maintenance-state calibrator`, which the literature does not justify.
- Primary evidence:
  - Villemagne et al. (2022, DOI `10.2967/jnumed.121.263254`) validated the first-in-human SMBT-1 MAO-B route.
  - Villemagne et al. (2022, DOI `10.2967/jnumed.121.263255`) studied reactive astrogliosis along the Alzheimer disease continuum.
  - Hiraoka et al. (2025) showed that SMBT-1 still requires explicit brain-side quantification choices.
  - Mesfin et al. (2026) added the separate whole-body biodistribution burden in healthy humans.

### 2. One factual public citation mapping was wrong

- Problem:
  - The FAQ used DOI `10.2967/jnumed.121.263254` where the argument actually required the Alzheimer-continuum disease-context paper.
- Why this is technically weak:
  - This was not merely a wording issue.
  - It attached the wrong paper to the wrong inferential role and made the site's own route logic internally inconsistent.
- Correction:
  - The disease-context slot now cites DOI `10.2967/jnumed.121.263255`.
  - DOI `10.2967/jnumed.121.263254` is retained, but only for the first-in-human target-validation role.

### 3. The public pages undernamed whole-body biodistribution / tracer burden as its own route burden

- Problem:
  - The public pages already named brain-side proxy families carefully.
  - But they did not yet make `whole-body biodistribution` explicit inside the astrocyte PET lane.
- Why this is technically weak:
  - Human PET routes are constrained not only by target and disease contrast, but also by scan regime, tissue distribution, and excretion profile.
  - If the whole-body biodistribution role is left implicit, the route can look more deployment-ready than the evidence supports.
- Primary evidence:
  - Mesfin et al. (2026) reported six healthy participants under a 5.5-hour dynamic whole-body PET protocol and identified strong hepatobiliary / intestinal burden, which is a different evidential object from brain quantification or AD-context contrast.

### 4. Cohort and covariate dependence needed to remain explicit

- Problem:
  - Once an astrocyte PET route is named, readers can easily overread it as a generic human astrocyte burden meter.
- Why this is technically weak:
  - The literature does not support one common ceiling.
  - Cohort composition and covariates can materially move the interpretation even within the same target class.
- Primary evidence:
  - Best et al. (2026) reported that MAO-B binding in alcohol use disorder was not elevated overall and varied with severity and daily cigarette use.

## Changes Executed In This Session

- `faq.md`
  - Split the old astrocyte PET row into `Brain astrocyte-related PET routes` and `Whole-body SMBT-1 biodistribution`.
  - Corrected the disease-context citation from DOI `10.2967/jnumed.121.263254` to DOI `10.2967/jnumed.121.263255`.
  - Updated the front-door notes so `route name alone is too coarse` now explicitly includes first-in-human validation, AD-context, brain quantification, and whole-body biodistribution as separate route roles.
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - Updated the astrocyte-related route card so human evidence is read by `target`, `route role`, `quantity type`, `brain quantification regime`, and `whole-body tracer-burden regime`.
  - Added a separate `Whole-body SMBT-1 biodistribution` calibrator-role row.
- `verification.md`
  - Rewrote the astrocyte route-card addendum so it now states explicitly which paper occupies the first-in-human, AD-spectrum, brain-quantification, and whole-body-biodistribution roles.
- `wbe_101.md`
  - Strengthened the front-door human observability wording so astrocyte PET is no longer read as one generic proxy row.
- `mind_uploading_papers.md`
  - Updated the 2026 addendum, the destructive-versus-in-vivo separation note, the observability ladder tables, and the recommended reading row so the archive no longer re-compresses the astrocyte PET lane.

## External Dependency Tasks

- None.
  - This session only required literature review, repository edits, local verification, and Git operations that were executable in the current environment.

## References

1. Villemagne VL, Furumoto S, Fodero-Tavoletti MT, et al. In Vivo Evaluation of ^18F-SMBT-1, a Novel MAO-B PET Tracer for Imaging Reactive Astrogliosis in the Human Brain. *Journal of Nuclear Medicine*. 2022;63(11):1746-1752.
   - https://doi.org/10.2967/jnumed.121.263254
2. Villemagne VL, Furumoto S, Fodero-Tavoletti MT, et al. Assessing Reactive Astrogliosis with ^18F-SMBT-1 Across the Alzheimer Disease Continuum. *Journal of Nuclear Medicine*. 2022;63(12):1900-1906.
   - https://doi.org/10.2967/jnumed.121.263255
3. Hiraoka K, Furumoto S, Fodero-Tavoletti MT, et al. Quantification of 18F-SMBT-1 PET in the Human Brain. *Annals of Nuclear Medicine*. 2025.
   - https://doi.org/10.1007/s12149-025-02083-y
4. Mesfin B, Ishioka Y, Ichinose Y, et al. Whole-body biodistribution of [^18F]SMBT-1: a novel PET tracer for monoamine oxidase B imaging in healthy humans. *Annals of Nuclear Medicine*. 2026.
   - https://doi.org/10.1007/s12149-025-02144-2
5. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of ^11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine*. 2018;59(10):1597-1602.
   - https://doi.org/10.2967/jnumed.118.208009
6. Livingston NR, Vasdev N, Gao Y, et al. PET Imaging of Monoamine Oxidase B in Alcohol Use Disorder. *Molecular Psychiatry*. 2022;27:1664-1672.
   - https://doi.org/10.1038/s41380-021-01429-y
7. Best LM, Rusjan P, Mizrahi R, et al. Monoamine Oxidase-B PET in Alcohol Use Disorder: Severity and Cigarette Exposure Dependence. *Molecular Psychiatry*. 2026.
   - https://doi.org/10.1038/s41380-025-03355-9
8. Jaisa-Aad MM, Gao F, Chatterjee S, et al. Reactive Astrocyte Biomarkers Across Human Neurodegenerative Disease Tissue. *Acta Neuropathologica*. 2025.
   - https://doi.org/10.1007/s00401-024-02712-2
