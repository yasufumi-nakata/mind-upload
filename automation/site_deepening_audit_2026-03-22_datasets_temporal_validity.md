# Site Deepening Audit (2026-03-22, datasets temporal-validity stop line)

## Target

- Primary: `datasets.md`

## Why this topic was selected

- The core public pages already separated `state / trait / drift`, `Temporal Validity Card`, and `recalibration burden`.
- The practical entry page for data and L0 work, however, still stopped mostly at `evaluation family` labels such as `within-session`, `cross-session`, and `adaptation`.
- That left a real scientific weakness: a reader could still overread `cross-session` or `adaptation` as if those tags already captured longitudinal validity.

## Evidence-backed critique

### 1. Split labels alone do not tell us what changed across time

- Problem:
  - `within-session`, `cross-session`, and `adaptation` are useful evaluation families, but they do not by themselves disclose whether the score moved because of state fluctuation, interface change, or genuine backbone instability.
- Evidence:
  - Musall et al. (2019) showed that task-related neural activity can be strongly dominated by uninstructed movements.
  - Egger et al. (2024) showed over a 10-hour EEG day that chrono-EEG dynamics materially influence hand-gesture decoding and motivate adaptive decoders.
- Critique:
  - Therefore, a cross-session score without `state annotation` is still underdetermined.
  - The practical page needed to say explicitly that split family and temporal validity are different audit layers.

### 2. Adaptation success is not fixed-decoder durability

- Problem:
  - The old page named adaptation, but it did not force the reader to separate `the system remained usable` from `the original decoder remained valid`.
- Evidence:
  - Karpowicz et al. (2025) stabilized BCI performance through alignment of latent dynamics, which is an explicit rescue route.
  - Wilson et al. (2025) maintained online cursor iBCI use for up to one month with unsupervised recalibration, which makes recalibration burden part of the result rather than a hidden detail.
- Critique:
  - Therefore, adaptation should not be summarized as generic robustness.
  - A practical page that omits `fixed decoder interval` and `recalibration burden` still leaves the main longitudinal ambiguity intact.

### 3. Fast online communication demos are not yet generic temporal-validity benchmarks

- Problem:
  - Practical readers can still move too quickly from `real-time online use exists` to `long-term temporal validity is demonstrated`.
- Evidence:
  - Wairagkar et al. (2025) showed a major speech-neuroprosthesis advance with instantaneous voice synthesis from chronic intracortical recordings.
- Critique:
  - This is strong communication-route evidence, but it is still participant-specific and does not, by itself, settle transfer ceiling, generic deployment, or low-burden durability.
  - The datasets page therefore needed a stop line that prevents `online use` from replacing a named temporal-validity audit.

## Changes executed

- `datasets.md`
  - Updated `last_updated` to `2026-03-22`.
  - Added front-matter bullets stating that `cross-session` and `adaptation` are not yet temporal-validity claims by themselves.
  - Added a new note box in `#generalization-families` that ties practical reading to:
    - state annotation
    - fixed decoder interval
    - recalibration burden
    - transfer ceiling
  - Added a compact table showing which extra disclosures are still required for:
    - cross-session
    - cross-session adaptation
    - longitudinal / chronic use
  - Strengthened the practical site rule so cross-session-or-longer claims now explicitly stack the site's `Temporal Validity` fields on top of ordinary dataset-card metadata.
  - Added primary references for Egger et al. (2024), Karpowicz et al. (2025), and Wairagkar et al. (2025).

## Why this is better

- The practical data page now matches the stricter scientific stop lines already used on the theory and verification pages.
- A reader can no longer treat `cross-session` as a shortcut for `durable`.
- A reader can no longer treat `adaptation worked` as if it proved `drift disappeared`.

## External dependency kept separate

- Unified public temporal-validity benchmark for EEG-style datasets
  - Owner: external benchmark designers and dataset maintainers
  - Preconditions: public schema that logs state annotation, fixed decoder interval, recalibration burden, and transfer ceiling under shared evaluation tasks
  - Done when: a public benchmark board makes these four fields comparable across practical EEG datasets

## References

1. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
2. Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
3. Karpowicz BM, Ali YH, Wimalasena LN, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
4. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
5. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
