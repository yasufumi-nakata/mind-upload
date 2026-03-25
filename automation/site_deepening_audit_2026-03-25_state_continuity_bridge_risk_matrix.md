# Site Deepening Audit: State-Continuity Bridge Risk Matrix

- Date: 2026-03-25
- Main target: `wiki/state-continuity-bridge.md`
- Synchronized targets: `verification.md`, `research_harvest_50.md`
- Scope: technical / natural science only

## Why this was the next page to deepen

The public site had already established the correct high-level rule:

- `same-subject != same-state`
- `same-brain != simultaneous whole-state capture`
- sequential bridges need a `State-Continuity Bridge Card`

However, one research-critical weakness remained.

The bridge rule still read too much like a **single generic time penalty**. That is not what the primary literature supports. Different bridge classes fail for different reasons:

- `live -> fixation -> ex vivo` bridges are dominated by **preparation change / transformation**
- `same-day repeated live` bridges are dominated by **behavioral and regime drift**
- `sleep-crossing / overnight` bridges are dominated by **homeostatic and computational-regime change**
- `multi-day proxy bundles` are dominated by **trait/state mixing plus proxy-composition mismatch**

Without that split, a reader can still under-audit bridge claims even while repeating the slogan `same-subject is not same-state`.

## Primary-literature basis for the criticism

### 1. Live-to-fix bridges are transformation-dominated, not just delayed

- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) showed that preservation route and fixation time course change extracellular-space retention and downstream ultrastructure quality.
- [Idziak et al. (2023)](https://doi.org/10.1523/ENEURO.0104-23.2023) compared live and PFA-fixed hippocampal slices and reported subtle dendritic-spine morphology changes plus substantial membrane damage.

Criticism:

- A bridge from live physiology to fixed tissue cannot be summarized as `same specimen with some elapsed time`.
- The bridge itself changes what is observable.

### 2. Same-brain structure/function pipelines remain local, deformation-heavy bridges

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) required a multistage workflow linking in vivo 2-photon data to SXRT and targeted SBEM through landmarks, warping, and targeted subvolumes.
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) provided a landmark dataset, but still as a sequential local pipeline; the paper explicitly reports day-to-day tissue deformation across a wide field of view.

Criticism:

- `same-brain` does not license cell-precise, deformation-free, whole-state language.
- The correct reading is local bridge strength plus residual deformation burden.

### 3. Same-day repeated live measurements can drift within hours

- [Musall et al. (2019)](https://doi.org/10.1038/s41593-019-0502-4) showed that richly varied movements dominate single-trial cortical dynamics.
- [Benisty et al. (2024)](https://doi.org/10.1038/s41593-023-01498-y) showed rapid fluctuations in functional connectivity that encode spontaneous behavior.
- [Egger et al. (2024)](https://doi.org/10.1038/s41598-024-70609-x) showed decoder-relevant chrono-EEG dynamics over a 10-hour window.

Criticism:

- A repeated live measurement can fail same-state continuity even without any destructive stage.
- The first exposed bridge risks here are not fixation artifacts but behavioral, arousal, connectivity, and decoder-statistics drift.

### 4. Sleep-crossing bridges are regime changes, not just longer same-day bridges

- [Hengen et al. (2016)](https://doi.org/10.1016/j.cell.2016.01.046) showed that firing-rate homeostasis is gated by wake and inhibited during sleep.
- [Xu et al. (2024)](https://doi.org/10.1038/s41593-023-01536-9) showed that wake progressively disrupts cortical criticality and sleep restores it.

Criticism:

- Overnight reacquisition crosses a homeostatic / computational regime boundary.
- If a claim ignores sleep/wake crossing, the bridge audit is under-specified even when elapsed time is reported.

### 5. Multi-day bridges can cross genuine structural turnover windows

- [Attardo et al. (2015)](https://doi.org/10.1038/nature14467) reported CA1 spine lifetimes on the order of 1-2 weeks, implying near-complete turnover over a few multiples of that interval.

Criticism:

- Multi-day or week-scale bridges cannot be read as biologically silent by default.
- Structural continuity and maintenance-state continuity should be treated as explicit burdens, not background assumptions.

## What I changed on the site

### 1. `wiki/state-continuity-bridge.md`

Added a new section:

- `Bridge risk is family-specific, not one scalar`

This section now:

- distinguishes transformation-dominated bridges from drift-dominated bridges
- maps bridge classes to the first hidden-state families that become exposed
- names the default stacked cards for each bridge class
- keeps this as a site-level inference rather than falsely attributing the table to the source papers

### 2. `verification.md`

Strengthened the `State-Continuity Bridge Card` by adding:

- an explicit 2026-03-25 addendum
- a bridge-class table that forces authors to name both:
  - the bridge type
  - the first exposed hidden-state families

This closes the loophole where users could report only elapsed time and still leave the real bridge burden underspecified.

### 3. `research_harvest_50.md`

Strengthened the evidence-bank reading rule so technical readers now see, at the literature-map level, that:

- bridge risk is not one scalar
- live-to-fix, waking-state drift, and sleep-crossing should be read differently
- the operational matrix lives in the bridge wiki and the verification card

## Resulting site-level rule

The revised public rule is now:

1. Ask what kind of bridge it is.
2. Ask which hidden-state families that bridge exposes first.
3. Ask which extra cards must be stacked because of that bridge class.
4. Demote the claim to the strongest directly supported stage if those fields are absent.

That is a stricter and more scientifically defensible reading rule than `same-subject but with some delay`.
