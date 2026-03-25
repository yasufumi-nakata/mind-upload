# Site Deepening Audit - 2026-03-25 - Technical Roadmap proxy-ladder split

## Selected target

- Public page: `tech_roadmap.md`
- Focused nodes: `M1` (measurement-stack table) and `M3` (human in vivo observability ladder)

## Why this page was chosen

This repository's newer public pages already enforce a strict distinction among `proxy class`, `operational maturity`, and `calibrator role`. However, `tech_roadmap.md` still contained one compressed `local transmitter / astrocyte imaging` row and still described human in vivo evidence as a `two-axis ladder`. That lagged behind the current site-wide standard and created a real risk of overreading.

The scientific problem was not a missing slogan. It was a mismatch between:

1. the current public rule elsewhere on the site, which already separates route families and proxy ceilings; and
2. the roadmap page, which is often the first place where readers form the dependency map for measurement claims.

Because `tech_roadmap.md` is a navigation page, any compression error there propagates to the rest of the site as a reading error.

## Evidence-backed critique

### 1. `local transmitter / astrocyte imaging` was too coarse as one measurement-stack row

The row collapsed at least four inferentially different objects:

- mixed arousal proxy and pupil-linked transmitter covariation
- local transmitter sensing with explicit clearance kinetics
- astrocyte-network or ensemble-state readout
- human astrocyte / clearance support proxies

The primary literature does not support reading those as one stack.

- [Reimer et al. (2016)](https://doi.org/10.1038/ncomms13289) showed that pupil fluctuations track both adrenergic and cholinergic cortical activity rather than one transmitter-specific state variable.
- [Neyhart et al. (2024)](https://doi.org/10.1016/j.celrep.2024.114808) showed that local cortical acetylcholine depends on both cholinergic axon activity and local clearance kinetics.
- [Cahill et al. (2024)](https://doi.org/10.1038/s41586-024-07311-5) showed minute-scale cortical astrocyte-network encoding of local neurotransmitter input, which is not the same inferential object as transmitter occupancy or release.
- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263255) characterized `18F-SMBT-1` as a human reactive-astrogliosis PET proxy, not a readout of learning-associated astrocyte ensembles.
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) measured CSF mobility in humans, which the paper itself distinguishes from direct clearance flux.
- [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) infer brain-to-plasma clearance through a device-assisted, multicompartment-model route, again a different inferential object from local astrocyte or microglial controller state.

Therefore, a single row was no longer defensible on scientific grounds.

### 2. The roadmap's `two-axis ladder` language underfit the current evidence structure

The older wording separated:

- what hidden-state family a route constrains
- how specialized or deployment-limited the route is

That was already better than a one-axis progress bar, but it still omitted a third question that matters operationally:

- what the route safely calibrates on this site

That third question is necessary because a route can be:

- technically real
- somewhat mature
- yet still only calibrate one bounded hidden-state family

The primary literature supports that additional distinction.

- [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024) is a regional synaptic-density atlas route, not a generic readout of current synaptic efficacy.
- [Hansen et al. (2022)](https://doi.org/10.1038/s41593-022-01186-3) is a receptor / transporter atlas route, that is, a regional chemoarchitectural prior.
- [Wong et al. (2013)](https://doi.org/10.1007/s00213-013-3103-z) is a ligand-specific occupancy route.
- [Koepp et al. (1998)](https://doi.org/10.1038/30498) is a challenge-linked displacement / release route.
- [Lucchetti et al. (2025)](https://doi.org/10.1038/s41467-025-66124-w) is a parcel-level biochemical-similarity route, not kinetic flux imaging.
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) is a small-cohort, high-burden energetic-rate route.
- [Baadsvik et al. (2024)](https://doi.org/10.1002/mrm.29998) is a proof-of-principle myelin-bilayer route in two healthy volunteers.

These routes do not merely differ in maturity. They safely calibrate different hidden-state families and stop at different ceilings.

### 3. The roadmap needed to block additive overreading when several human rows are listed together

The risk was that readers could still treat `more human rows listed` as `closer to state-complete readout`.

That shortcut is not supported by multimodal primary literature.

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) showed that simultaneous calcium and BOLD reveal both common and divergent network organization.
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) showed tightly coupled global progression plus distinct network patterns in simultaneous EEG-PET-MRI during sleep descent.
- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) showed that a major global fMRI mode is substantially coupled to autonomic physiology.
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) showed that significant task BOLD changes can coexist with opposite oxygen-metabolism changes across many cortical voxels.

Therefore, the roadmap needed to route readers more explicitly toward `Human Proxy Composition Card` logic, not just `same-subject` and `external calibration` language.

## Executed changes

### Public page changes made now

- Updated `tech_roadmap.md` front matter so the page now describes human evidence as a `three-axis ladder` rather than a `two-axis ladder`.
- Added a `known_points` statement that `proxy class`, `operational maturity`, and `calibrator role` are different questions.
- Replaced the compressed `local transmitter / astrocyte imaging` row in `M1` with four narrower rows:
  - local transmitter sensor / axon imaging
  - local astrocyte imaging / ensemble readout
  - human receptor / transporter atlas + occupancy / displacement PET
  - human astrocyte PET / clearance-support proxy
- Added a new `M1` note box that explains, with primary-literature support, why those rows cannot be merged.
- Rewrote the `M3` human-ladder addendum from `two-axis` to `three-axis`.
- Expanded the `M3` human route table so each row now exposes:
  - proxy class
  - operational maturity / burden
  - safe calibrator role
  - residual ceiling
- Added an explicit route from `M3` to the `Human Proxy Composition Card` and [Wiki: Human Proxy Composition and Route Maturity](https://mind-upload.com/wiki/human-proxy-composition.html).

## Resulting site-level improvement

The roadmap now matches the stricter reading rules already enforced elsewhere on the site:

- `proxy-rich` no longer reads as one progress bar
- local transmitter, astrocyte, receptor-PET, and clearance routes no longer share one stack label
- readers are pushed earlier toward the correct ceiling logic before they overread later sections

## External dependency tasks

- None for this run.

## Files changed in this run

- `tech_roadmap.md`
- `automation/site_deepening_audit_2026-03-25_tech_roadmap_proxy_ladder_split.md`

