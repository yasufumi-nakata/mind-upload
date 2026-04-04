# Site Deepening Audit: Human Support-State Front Door

Date: 2026-04-04

## Scope

- Technical and natural-science content only.
- `issue.md` was intentionally not read, per operator instruction.
- Focus selected for this run: the public front door for human support-state evidence on [`index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md) and [`wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md).

## Why this area was selected

- It sits directly on the main reading path, so a coarse reading here propagates into the rest of the site.
- The repository already had strong route-family discipline, but the compressed public entry points still left a specific overreading risk: recent human support-state rows could still look like one convergent `maintenance-controller meter`.
- Recent primary literature sharpens a stricter split. The rows differ in direct observable, crossed boundary, target class, scan/model burden, and validation ceiling.

## Critical findings

1. The public front door already warned that human evidence is layered, but it still lacked a compact four-lane decomposition of support-state human rows.
Evidence: barrier-side transport papers, clearance-transport papers, astrocyte-related PET papers, and target-defined neuroimmune PET papers were all nearby in the entry narrative, but not yet typed side by side as different lanes with different stop lines.

2. Barrier-side human routes are not one generic `BBB meter`.
Evidence: Petitclerc et al. (2026) separates BBB-versus-BCSFB water transport in a small MRI study, while Chung et al. (2025) quantifies tracer-specific molecular BBB permeability and explicitly points to missing human ground truth and future test-retest work.

3. Astrocyte-related human PET is not one interchangeable controller readout.
Evidence: SMBT-1 target validation and quantification routes differ from I2BS routes; scan window, reference region, and kinetic-model choice materially affect quantification; tracer-family equivalence is not licensed by the current literature.

4. Target-defined neuroimmune PET is not one reusable inflammation scalar.
Evidence: TSPO, CSF1R, and COX-2 are different targets with different biological meaning and different validation status. The strongest current literature does not support silently switching among them inside one bundle claim.

5. Clearance-side human routes remain transport-side routes.
Evidence: CSF mobility MRI and model-based brain-to-plasma biomarker-efflux studies constrain macroscopic transport behavior, but they still do not identify the local immune effector, astrocyte ensemble, or synapse-specific maintenance controller.

6. Operational burden remains part of the claim ceiling.
Evidence: several front-rank rows still depend on small cohorts, arterial sampling, 7 T hardware, explicit compartmental models, investigational devices, or other route-specific burdens. These constraints should stay visible at the entry point instead of being hidden behind the phrase `human evidence exists`.

## Executed changes in this session

- Added a new four-lane support-state note and comparison table to [`index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md).
- Expanded the human-observability section in [`wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md) so that `BBB / BCSFB transport`, `astrocyte-related PET`, `target-defined neuroimmune PET`, and `clearance-transport` rows are explicitly separated.
- Updated page notes on both entry pages so the change is visible in public metadata.

## Why these edits are scientifically justified

- They reduce a concrete front-door overreading risk without changing the site's core position.
- They are conservative: the edits do not claim that current human routes are weak or irrelevant, only that they measure different objects and therefore must not inherit each other's claim ceiling.
- They align the most compressed public pages with the stricter route-card logic already present deeper in the repository.

## Verification run

- Verified local diff for [`index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md) and [`wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md).
- Built the site locally with Jekyll after the edits.

## External dependency tasks

- None for this run.

## Primary literature used for the critique

1. Petitclerc, L., Durrant, H., Hirschler, L., Václavů, L., & van Osch, M. J. P. (2026). Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *Journal of Cerebral Blood Flow & Metabolism*. https://doi.org/10.1177/0271678X261429042
2. Petitclerc, L., Hirschler, L., Wells, J. A., Thomas, D. L., van Walderveen, M. A. A., van Buchem, M. A., & van Osch, M. J. P. (2021). Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage, 245*, 118755. https://doi.org/10.1016/j.neuroimage.2021.118755
3. Chung, K. J., Abdelhafez, Y. G., Spencer, B. A., et al. (2025). Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications, 16*, 3076. https://doi.org/10.1038/s41467-025-58356-7
4. Villemagne, V. L., Harada, R., Dore, V., et al. (2022). First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine, 63*(10), 1551-1559. https://doi.org/10.2967/jnumed.121.263254
5. Hiraoka, K., Mesfin, B., Wu, Y., et al. (2025). Kinetic and quantitative analysis of [18F]SMBT-1 PET imaging for monoamine oxidase B. *Annals of Nuclear Medicine, 39*, 1249-1257. https://doi.org/10.1007/s12149-025-02083-y
6. Tyacke, R. J., Myers, J. F. M., Venkataraman, A., et al. (2018). Evaluation of 11C-BU99008, a PET Ligand for the Imidazoline2 Binding Site in Human Brain. *Journal of Nuclear Medicine, 59*(10), 1597-1602. https://doi.org/10.2967/jnumed.118.208009
7. Nutma, E., Fancy, N., Weinert, M., et al. (2023). Translocator protein is a marker of activated microglia in rodent models but not human neurodegenerative diseases. *Nature Communications, 14*, 4917. https://doi.org/10.1038/s41467-023-40937-z
8. Ogata, A., Ikenuma, H., Yasuno, F., et al. (2025). First-in-Human Study of [11C]NCGG401 for Imaging Colony-Stimulating Factor 1 Receptors in the Brain. *Journal of Nuclear Medicine, 66*(2), 302-308. https://doi.org/10.2967/jnumed.124.268699
9. Yan, X., Noergaard, M., Morse, C. L., et al. (2025). PET Quantification in Healthy Humans of Cyclooxygenase-2, a Potential Biomarker of Neuroinflammation. *Journal of Nuclear Medicine, 66*(3), 398-404. https://doi.org/10.2967/jnumed.124.268525
10. Hirschler, L., Petitclerc, L., Duits, F. H., et al. (2025). Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. https://doi.org/10.1038/s41593-025-02073-3
11. Dagum, A., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications, 17*. https://doi.org/10.1038/s41467-026-68374-8
