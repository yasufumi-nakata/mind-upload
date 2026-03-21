# Site Deepening Audit (2026-03-22, living-human proxy composition front door)

## Why this topic was chosen

- The site already stated that `proxy-rich != state-complete`, but on the public front door that warning was still mostly rhetorical.
- In practice, a reader could still scan `index.md` and `wbe_101.md`, see several strong living-human papers listed together, and come away with the wrong operational impression: `human observability is now close because many modalities moved forward`.
- The technical weakness was not a missing slogan. It was a missing comparison layer. The public pages were not yet forcing the reader to compare:
  - direct observable,
  - quantity type,
  - cohort size,
  - acquisition burden,
  - model burden,
  - and the exact composition failure each row still carries.

## Critical assessment

### 1. The front door still allowed `row count` to masquerade as `state closure`

- The public pages correctly named many modern human routes, but the comparison was still distributed across separate paragraphs and downstream wiki pages.
- That structure made it too easy to compress distinct advances into one impression of progress.
- The primary literature does not support that compression.

### 2. The cited human papers do not constrain the same inferential object

- `Johansen et al. (2024)` is a cohort-level `regional synaptic-density atlas`, not a momentary synaptic-function readout.
- `Lucchetti et al. (2025)` is a `five-metabolite similarity graph`, not kinetic metabolic flux imaging.
- `Li et al. (2025)` is a `7 T dynamic kinetic glucose-rate route`, not a density or similarity route.
- `Baadsvik et al. (2024)` is a `macro myelin-bilayer proof-of-principle`, not per-axon timing-state ground truth.
- `Hirschler et al. (2025)` is `CSF mobility`, not direct net clearance flux.
- `Dagum et al. (2026)` is `model-based sleep-linked efflux`, not a direct local immune-controller readout.

The scientific criticism is straightforward: if the quantity types differ this much, then simply listing the rows side by side does not justify reading them as one validated latent coordinate.

### 3. Operational maturity also differs sharply across rows

- Some rows are atlas-level cohort summaries.
- Some are high-field specialized acquisitions.
- Some are proof-of-principle studies with very small healthy cohorts.
- Some are model-heavy intervention studies.

That means `human route exists` and `human route is ready to compose into same-subject state identification` are different claims. The site already said this in prose, but the front door was still weaker than the literature warranted because it did not show the mismatch in a compact comparative form.

### 4. Same-session fusion still does not erase the composition problem

- `Chen et al. (2025)` shows that simultaneous EEG-PET-MRI can recover tightly coupled global progression and also `two distinct network patterns`.
- `Bolt et al. (2025)` shows that a major low-dimensional fMRI mode is substantially coupled to autonomic physiology.
- `Epp et al. (2025)` shows that significant task BOLD changes can coexist with opposite oxygen-metabolism changes across many cortical voxels.

Therefore, even when rows move together in the same session, the literature does not license the shortcut from `agreement` to `one solved biological state axis`.

## What I changed

### Public pages

- `index.md`
  - Strengthened the living-human proxy composition warning with explicit primary-paper operating details.
  - Added a compact comparison table so the front page shows, at a glance, why representative rows still fail to compose automatically.
- `wbe_101.md`
  - Added a route-by-route comparison table under the human-proxy composition rule.
  - Added a note-box that names the three exact overreads the site now blocks at the entry point:
    - `quantity-type collapse`
    - `deployment-maturity collapse`
    - `fusion collapse`

### Why this is better

- The site now criticizes the overclaim in a more falsifiable way.
- A reader can see the mismatch between `what is directly observed` and `what is being inferred` without leaving the main explanatory path.
- The change is still conservative: it does not add new speculative claims; it only makes the already-cited literature harder to overread.

## Primary sources used for this pass

1. Johansen, K. K., et al. (2024). Human SV2A / synaptic-density atlas paper. `doi:10.1523/JNEUROSCI.1750-23.2024`
2. Lucchetti, F., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. `doi:10.1038/s41467-025-66124-w`
3. Li, X., et al. (2025). Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. `doi:10.1093/pnasnexus/pgaf072`
4. Baadsvik, E. L., et al. (2024). Myelin bilayer mapping in the human brain in vivo. `doi:10.1002/mrm.29998`
5. Hirschler, L., et al. (2025). Human CSF-mobility MRI paper. `doi:10.1038/s41593-025-02073-3`
6. Dagum, P., et al. (2026). The glymphatic system clears amyloid beta and tau from brain to plasma in humans. `doi:10.1038/s41467-026-68374-8`
7. Chen, J. E., et al. (2025). Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. `doi:10.1038/s41467-025-64414-x`
8. Bolt, T., et al. (2025). Autonomic physiological coupling of the global fMRI signal. `doi:10.1038/s41593-025-01945-y`
9. Epp, S., et al. (2025). BOLD / oxygen-metabolism divergence paper used on this site for the hemodynamic common-axis warning. `doi:10.1038/s41593-025-02132-9`

## Remaining external dependencies

- None for this pass. The required work was entirely within the site's public content and evidence framing.
