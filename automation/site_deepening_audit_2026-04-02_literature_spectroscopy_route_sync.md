# Site Deepening Audit (2026-04-02, literature front-door spectroscopy route sync)

## Target

- Main public pages:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- Scope:
  - Technology
  - Natural science
- Explicitly excluded:
  - Philosophy
  - Law

## Why This Topic Was Chosen

- The site-wide rule had already become strict about human observability route families:
  - `1H-MRSI similarity scaffold`
  - `high-resolution 1H-MRSI metabolite-distribution mapping`
  - `31P metabolite / pH balance`
  - `31P MT exchange-flux`
  - `31P NAD-content mapping`
  - `localized functional 31P NAD-dynamics`
  - `deuterium absolute metabolite mapping / quantification`
  - `deuterium kinetic-rate imaging`
- However, the literature front door still lagged behind that rule in two concrete ways:
  - `mind_uploading_papers.md` still omitted the `Guo et al. (2025)` high-resolution `1H-MRSI metabolite-distribution` route from multiple front-door tables and route summaries.
  - `research_harvest_50.md` still lacked both a dedicated `Guo et al. (2025)` anchor row and a front-door sentence that explicitly stops readers from collapsing `Lucchetti 2025` and `Guo 2025` into one spectroscopy row.
- This was not a cosmetic omission. The affected sections are precisely the parts that new readers use first to decide what current living-human observability means.

## Main Conclusion

- `Lucchetti et al. (2025)` and `Guo et al. (2025)` are not one interchangeable `1H-MRSI` route.
- `Lucchetti et al. (2025)` is a `five-metabolite parcel-similarity / connectome` route.
- `Guo et al. (2025)` is a `high-resolution metabolite-distribution` route with an explicit acquisition / reconstruction burden.
- Therefore, literature front doors must expose both rows separately, or they silently teach the wrong inferential object.
- The same front door should also keep visible that the deuterium family still carries route-local `dose`, `time-point`, and `repeatability` burdens.

## Evidence-Based Critique

### 1. The site's own front-door taxonomy had an internal contradiction

- `mind_uploading_papers.md` already stated in summary-level sections that `1H-MRSI similarity` and `high-resolution 1H-MRSI metabolite-distribution mapping` are different route families.
- But the same page's high-traffic evidence-class table, living-human ladder summary, and quick-start route still dropped the high-resolution row.
- `research_harvest_50.md` likewise already enforced multi-row spectroscopy discipline in prose, but still lacked a dedicated `Guo et al. (2025)` anchor row.

Critique:

- This is a front-door compression bug.
- When the first-reading tables omit a route that the deeper pages already treat as distinct, readers are pushed back toward a false `one spectroscopy row` interpretation.

### 2. `Lucchetti et al. (2025)` and `Guo et al. (2025)` constrain different inferential objects

- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) used fast, high-resolution 3D whole-brain `1H-MRSI` in `51 healthy subjects` and defined a metabolic connectome as `pairwise correlations among five metabolites (tCr, tNAA, Glx, Ins, Cho) across gray-matter parcels`, with validation in an independent sample of `13` at another site.
- [Guo et al. (2025)](https://doi.org/10.1109/TBME.2025.3572448) instead addressed `high-resolution brain metabolic imaging at ultrahigh field` using `extended spatiospectral encoding and subspace modeling`, explicitly tackling `spectral ghosting`, `aliasing`, and `low-SNR` burdens to recover metabolite-distribution maps.

Critique:

- `Lucchetti 2025` is a `macro biochemical similarity scaffold`.
- `Guo 2025` is a `high-resolution metabolite-distribution route`.
- The first does not automatically give the second, and the second does not automatically give the first.
- Therefore, any literature front door that names only `Lucchetti 2025` still underdescribes what the current `1H-MRSI` family actually contains.

### 3. The spectroscopy lane is already multi-row even before deuterium enters the picture

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) constrain `resting 31P metabolite / pH balance`.
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) constrain `31P MT exchange-flux`.
- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) constrain `whole-brain intracellular NAD-content mapping`.
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) constrain `functionally localized 31P NAD+ dynamics` in a visually localized occipital voxel at `7 T` across `25 healthy volunteers`.

Critique:

- Once `1H-MRSI` already splits into at least `similarity` and `distribution`, and `31P` already splits into at least `balance`, `exchange-flux`, `NAD content`, and `task-evoked NAD dynamics`, the literature front door cannot safely present spectroscopy as a short undifferentiated lane.
- The omission of the high-resolution `1H-MRSI` row was therefore not an isolated missing citation. It weakened the route-family logic of the entire spectroscopy block.

### 4. Deuterium work also needs operating-point disclosure, not just family labels

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) constrain `absolute deuterated metabolite distributions` under an explicit quantification pipeline.
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) constrain `dynamic DMRSI kinetic-rate imaging` with `0.7 cc nominal voxel`, `2.5 min/image`, whole-brain coverage, blood-input measurement, and explicit kinetic modeling.
- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) showed in `six healthy participants` at `7 T` that brain `2H-Glc` and `2H-Glx` are dose dependent and that `0.50 g/kg` and `0.75 g/kg` behaved similarly from `60-100 min`, whereas `0.25 g/kg` was lower.
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) showed that deuterium-route repeatability depends on the acquisition / time-point regime rather than being route-free by default.

Critique:

- Even after the absolute-versus-kinetic split is named, the route burden is still not fully specified unless dose and repeatability windows remain visible.
- That is why the front-door anchor table needed an explicit `operating-point burden` row rather than only prose elsewhere on the site.

## Changes Executed In This Session

- `mind_uploading_papers.md`
  - Added `last_updated: "2026-04-02"` to reflect the material public-page revision.
  - Updated the human-observability note and table rows so `1H-MRSI similarity` and `high-resolution metabolite-distribution mapping` are named separately.
  - Updated the `observability-class advance / human in vivo proxy ladder` table so the spectroscopy lane now includes `Guo 2025` and explicit deuterium operating burdens.
  - Rewrote the quick-start row `I want to see what humans can actually observe now` so readers now separate:
    - `1H-MRSI similarity`
    - `high-resolution 1H-MRSI metabolite distribution`
    - `31P route families`
    - `deuterium absolute vs kinetic plus operating burden`

- `research_harvest_50.md`
  - Updated the front-matter note to reflect the spectroscopy-route sync.
  - Added a dedicated U7 stop line so `Lucchetti 2025` and `Guo 2025` are no longer allowed to collapse into one spectroscopy row.
  - Added a new anchor-table row for `Guo et al. (2025)`.
  - Added a new anchor-table row for `Ahmadian et al. (2025) / Bøgh et al. (2024)` so deuterium operating burdens are visible in the U7 front door itself.

## Misreadings Stopped By This Change

- `1H-MRSI paper exists` = one spectroscopy row
- `Lucchetti 2025` = high-resolution metabolite-distribution mapping
- `high-resolution metabolite map` = parcel-similarity connectome
- `deuterium route exists` = dose-free and timing-free portability
- `human metabolic imaging` = one living-human maintenance-state meter

## Verification

- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `git diff --check`
- `rg -n "10.1109/TBME.2025.3572448|high-resolution 1H-MRSI metabolite-distribution mapping|operating-point burden calibration" _site/mind_uploading_papers.html _site/research_harvest_50.html`

## External Dependency Tasks

- None.
  - This session required only web verification of primary literature, repository edits, local build / diff validation, and Git operations executable in the current environment.

## References

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66124-w
2. Guo G, Chen H, Peng X, et al. High-Resolution Brain Metabolic Imaging at Ultrahigh Field Using Extended Spatiospectral Encoding and Subspace Modeling. *IEEE Transactions on Biomedical Engineering*. 2025.
   - https://doi.org/10.1109/TBME.2025.3572448
3. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
4. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
5. Guo R, Yang S, Wiesner HM, et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024.
   - https://doi.org/10.3389/fnins.2024.1389111
6. Kaiser A, Vind FA, Duarte JMN, et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
7. Karkouri J, Novoselova M, Miller S, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7 T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
8. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
9. Ahmadian N, Konig MM, Otto S, et al. Human Brain Deuterium Metabolic Imaging at 7 T: Impact of Different [6,6'-2H2]Glucose Doses. *Journal of Magnetic Resonance Imaging*. 2025.
   - https://doi.org/10.1002/jmri.29532
10. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024.
    - https://doi.org/10.1186/s41747-024-00426-4
