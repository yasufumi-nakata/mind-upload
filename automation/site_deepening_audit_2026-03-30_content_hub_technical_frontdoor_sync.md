# Site Deepening Audit (2026-03-30, Content Hub Technical Frontdoor Sync)

## Scope

- Primary target: `content_hub.md`
- Secondary target: `summary_booklet.md` (auto-generated after the content-hub update)

## Why This Topic Was Chosen

- The core scientific pages had already become much stricter in March 2026 about three distinct technical reading problems:
  - local causal maintenance-state dependence,
  - bounded living-human observability / proxy classes,
  - bridge-limited same-subject / same-brain evidence.
- However, the public routing hub still reflected the older site structure from `2026-03-14` and did not operationalize those newer distinctions for readers who enter through the literature side.
- That mismatch matters because the hub page is the place where new content gets routed. If the routing layer is stale, later readers can reintroduce the exact compression that the core technical pages already blocked.

## Evidence-Based Critique

### 1. The integration hub under-specified the difference between `research_harvest_50` and `mind_uploading_papers`

- Problem:
  - `content_hub.md` routed "paper summaries and literature organization by open problem" to `research_harvest_50.html`, but it did not state clearly when to use `mind_uploading_papers.html` instead.
  - The public inventory listed both pages, but without a role split that matched the newer technical workflow.
- Why this is technically weak:
  - `mind_uploading_papers.md` is now the paper-level technical fast lane with chronology policy and route-family entry.
  - `research_harvest_50.md` is now the unresolved-question evidence map keyed to U-numbers.
  - If the hub does not state that distinction, technical readers can still enter through mixed year order or merge paper-level anchors directly into the wrong evidence bucket.
- Site evidence:
  - `mind_uploading_papers.md` explicitly says that law, metaphysics, and other non-technical material share the year cards, and that technical readers should first use the technical fast lane.
  - `research_harvest_50.md` explicitly says it is the unresolved-question map rather than a paper-card archive.

### 2. The routing layer did not expose the now-critical split between local causal maintenance papers and bounded living-human observability papers

- Problem:
  - The integration hub still described literature placement generically, even though the core technical pages now treat several 2025-2026 papers as belonging to different inferential ladders.
- Why this is technically weak:
  - Primary literature in late 2025 through early 2026 does not justify one homogeneous "frontier" lane.
  - Local causal maintenance-state papers move a controller-side ladder; living-human proxy papers move a bounded observability ladder; same-subject / same-brain papers can instead move only a bridge-validation ladder.
- Primary evidence:
  - Terceros et al. (2026), Dewa et al. (2025), and Bukalo et al. (2026) sharpen local causal maintenance-state dependence.
  - Hirschler et al. (2025) and Dagum et al. (2026) sharpen bounded living-human observability classes.
  - Those papers differ in species, direct observable, spatial unit, and model burden.

### 3. The hub did not tell maintainers where bridge-limited same-subject / same-brain results should be integrated

- Problem:
  - The site already had dedicated bridge logic in Verification and the State-Continuity Bridge wiki page.
  - But the integration hub did not identify bridge-limited carry-over evidence as its own routing case.
- Why this is technically weak:
  - Same-subject or same-brain wording is one of the easiest places for a reader to overread identity of specimen as identity of state.
  - If the hub fails to route bridge papers through the bridge card first, those papers can be misfiled as stronger human observability evidence than they warrant.
- Site evidence:
  - `verification.md` already has a `State-Continuity Bridge Card`.
  - `wiki/state-continuity-bridge.md` already explains preservation route, elapsed time, regime continuity, and bridge validation as distinct burdens.

## Changes Executed In This Session

- `content_hub.md`
  - Updated page metadata and highlights to reflect the March 2026 technical routing logic.
  - Added a technical / natural-science note that explicitly routes readers first to `mind_uploading_papers` for paper-level anchors, then to `research_harvest_50` for unresolved-question placement.
  - Added an explicit note that same-subject / same-brain papers must first pass the bridge route through Verification and the State-Continuity Bridge wiki page.
  - Added a technical fast-path table separating:
    - paper-level frontier anchors,
    - unresolved-question mapping,
    - bounded human observability,
    - bridge-limited same-subject / same-brain evidence,
    - multi-row human proxy composition.
  - Expanded the integration map so `mind_uploading_papers`, bridge-limited evidence, and human proxy composition now have fixed public destinations.
  - Added an anti-sprawl rule that blocks chronology from fusing local causal maintenance papers, bounded living-human observability papers, and bridge-limited same-subject / same-brain papers into one lane.
  - Added `summary_booklet.html`, `wiki/human-proxy-composition.html`, and `wiki/state-continuity-bridge.html` to the public inventory so the routing layer matches the current site topology.
- `summary_booklet.md`
  - Regenerated after the content-hub update so the public booklet reflects the refreshed hub metadata and newest summary date.

## External Dependency Tasks

- None.
  - This session only required literature verification, public routing edits, auto-generated booklet refresh, and repository updates that were executable locally.

## References

1. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;649:1254-1263.
   - https://doi.org/10.1038/s41586-025-09774-6
2. Dewa AM, Williamson E, Eldridge A, et al. Emotional memory consolidation is supported by astrocytic ensembles. *Nature*. 2025;648:643-651.
   - https://doi.org/10.1038/s41586-025-09619-2
3. Bukalo O, O'Sullivan R, Tanisumi Y, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
4. Hirschler L, Ding J, Smith AJ, et al. Mobility tensor imaging uncovers in vivo cerebrospinal fluid dynamics in the human brain. *Nature Neuroscience*. 2025;28:70-80.
   - https://doi.org/10.1038/s41593-025-02073-3
5. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026;17:715.
   - https://doi.org/10.1038/s41467-026-68374-8
6. Lu T, Schwarz C, Tardiff K, et al. Preservation quality and extracellular-space retention shape correlative microscopy outcomes. *Cell Reports Methods*. 2023;3(7):100520.
   - https://doi.org/10.1016/j.crmeth.2023.100520
7. Bosch C, Martínez-Martínez Á, Castaño-Prat P, et al. Correlating in vivo functional imaging and electron microscopy of single neurons in mouse visual cortex. *Nature Communications*. 2022;13:2500.
   - https://doi.org/10.1038/s41467-022-30199-6
8. Egger M, Iljazi A, Rebsamen M, et al. Non-stationarity of resting EEG over 10 hours motivates adaptive decoding. *Scientific Reports*. 2024;14:70609.
   - https://doi.org/10.1038/s41598-024-70609-x
