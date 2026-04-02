# Site Deepening Audit (2026-04-02, Perspective technical front-door reset)

## Scope

- Primary target:
  - `perspective.md`
- Secondary target:
  - `content_hub.md`
- Research scope:
  - technology
  - natural science
- Explicitly excluded:
  - philosophy
  - law
- Explicitly skipped by request:
  - `issue.md`

## Why This Topic Was Chosen

- `perspective.md` is the site's longest public synthesis page and the place where readers decide what the project thinks the real bottleneck is.
- The page had already become strong at splitting route families inside later sections, but its top-level framing still foregrounded `identity`, `copy`, and theory-routing language before the empirical bottlenecks of:
  - observability
  - identifiability
  - maintenance-state dependence
  - bounded living-human proxy composition
- That ordering was scientifically weak because it encouraged readers to start from labels rather than from the quantities that are actually measured, perturbed, or left latent.
- `content_hub.md` still routed `Perspective` as the place for `theory comparison, criticisms, and philosophical assumptions`, which reinforced the same misread at the site-navigation level.

## Evidence-Based Critique

### 1. The old top-level framing over-privileged theory labels relative to the current empirical bottleneck

- Problem:
  - The old `Perspective` front matter and opening design section started from theories and copy-language rather than from hidden-state closure.
- Why this is technically weak:
  - Current primary literature does not justify reading the field's main bottleneck as `which theory wins` first.
  - It justifies reading the bottleneck as `which state variables are observed directly, which remain latent, and which are causally required for stability and adaptation`.
- Primary evidence:
  - `Yao et al. (2023)` built a high-resolution whole-mouse transcriptomic and spatial atlas with millions of cells, which is a major scaffold gain rather than a route-free current-state meter.
  - `Shapson-Coe et al. (2024)` reconstructed a cubic millimeter of human cortex at nanoscale resolution, which is a local human structural breakthrough but still not whole-brain state closure.
  - `Gamlin et al. (2025)` linked connectomics to predicted transcriptomic types, which strengthens label transfer and scaffold quality rather than direct transcriptomic truth in vivo.
- Conclusion:
  - Structural progress is real and important, but it still belongs on the `scaffold` side of the site's claim ladder.

### 2. The strongest recent causal papers point to dynamic maintenance state, not structure alone

- Problem:
  - The old design section still let readers start from `copy / continuity / theory` language before seeing why dynamic state variables are scientifically first-order.
- Why this is technically weak:
  - Recent causal studies show that long-timescale stabilization and adaptive neural representations depend on transcriptional and glial state, not only on wiring.
- Primary evidence:
  - `Terceros et al. (2026)` identified distinct waves of thalamocortical transcriptional programs that were causally required for memory stabilization across days to weeks.
  - `Ito et al. (2025)` showed that an astrocytic ensemble acts as a multiday trace that stabilizes labile memories.
  - `Bukalo et al. (2026)` showed that astrocyte calcium signaling enables amygdala neural representations supporting fear memory retrieval and extinction.
- Conclusion:
  - A public front door that starts from structure and theory labels but delays dynamic maintenance-state burden is no longer aligned with the strongest causal literature.

### 3. Living-human observability is getting richer, but it remains bounded and route-specific

- Problem:
  - The older top framing did not make it explicit enough that living-human advances still constrain bounded proxy objects rather than route-free controller identity.
- Why this is technically weak:
  - If the top of the page does not force that distinction early, later route-family splits can still be overread as near-complete state access.
- Primary evidence:
  - `Hirschler et al. (2025)` introduced a non-invasive MRI method for CSF mobility down to perivascular spaces and showed region-specific drivers, while explicitly positioning the result as a CSF-mobility measurement rather than a full clearance-controller identity readout.
  - `Dagum et al. (2026)` linked sleep-active glymphatic processes to overnight plasma biomarker changes using a randomized crossover study and a multicompartment model, which sharpened a bounded human clearance route rather than a route-free maintenance-state meter.
- Conclusion:
  - The top of the page must tell readers that richer human evidence is still proxy-bounded and composition-limited.

### 4. The site's own navigation layer was still routing Perspective too philosophically

- Problem:
  - `content_hub.md` described `Perspective` as the page for `theory comparison, criticisms, and philosophical assumptions`.
- Why this is technically weak:
  - That routing statement contradicted the rest of the site's 2026 shift toward observability ceilings, maintenance-state families, and route-specific inference.
  - It also made technical readers more likely to misfile state-space-closure material.
- Required correction:
  - The hub needed to describe `Perspective` as the synthesis page for measurement-model-implementation limits and scientific objections, not as the philosophy bucket.

## Changes Executed In This Session

### `perspective.md`

- Updated `last_updated` to `2026-04-02`.
- Updated the public note to record a `technical-front-door framing reset`.
- Rewrote the page description, audience, intro, and accuracy note so the page now starts from:
  - observability
  - identifiability
  - maintenance-state burden
  - implementation ceilings
- Replaced the top-level highlights so the new first framing is `state-space closure`.
- Rewrote the `known_points`, `unknown_points`, and top wiki-link set to emphasize technical / natural-science routes and remove philosophy-first routing from the top summary block.
- Rewrote the opening abstract to use four technical questions:
  - what is directly observable
  - what remains latent
  - what can be perturbed or calibrated
  - what must stay stable in implementation
- Rewrote the early note boxes so readers are sent first to:
  - measurement-stack limits
  - observation-to-estimation
  - maintenance-state background
  - human-proxy composition
  - drift / closed-loop / thermodynamic pages
- Rewrote the early reading table so the first entry now asks which technical bottleneck bites first rather than which theory fails first.
- Replaced the `Design Principles: Design as a migration, not a copy` frame with `Design Principles: Start from state-space closure` while preserving the `#design-principles` anchor.
- Replaced the old identity / theory / thermodynamics table with a new four-row design table:
  - structural scaffold
  - maintenance controllers
  - human observability
  - implementation gates
- Added a new evidence-backed note box explaining why the page now starts from state-space closure, with direct DOI links to the primary literature behind the reset.

### `content_hub.md`

- Updated `last_updated` to `2026-04-02`.
- Updated the note to record the `Perspective technical-front-door sync`.
- Rewrote the guide note so `Perspective` is described as the long technical synthesis page, not a theory-first page.
- Rewrote the routing table entry for `Perspective` so it now receives:
  - measurement-model-implementation synthesis
  - scientific objections
  - state-space-closure limits

## Verification

- `bundle exec jekyll build`
  - Result:
    - succeeded
    - rendered the updated pages into `_site/`
- Generated-page spot checks:
  - confirmed the new `Perspective` header block renders the updated technical framing
  - confirmed the `#design-principles` section title and body now use the state-space-closure framing
  - confirmed `content_hub` now routes `Perspective` as a technical synthesis page

## External Dependency Tasks

- None.
  - This round was fully executable inside the session through literature checking, repository edits, local build verification, and Git operations.

## References

1. Yao Z, van Velthoven C, Kunst M, et al. A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. *Nature*. 2023;624:317-332.
   - https://doi.org/10.1038/s41586-023-06812-z
2. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024;384:eADK4858.
   - https://doi.org/10.1126/science.adk4858
3. Gamlin CR, Bae JA, Dorkenwald S, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08805-6
4. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;649:1254-1263.
   - https://doi.org/10.1038/s41586-025-09774-6
5. Ito M, Sakamoto M, Masuda T, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
6. Bukalo O, O'Sullivan R, Tanisumi Y, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
7. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025;28:2392-2401.
   - https://doi.org/10.1038/s41593-025-02073-3
8. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
