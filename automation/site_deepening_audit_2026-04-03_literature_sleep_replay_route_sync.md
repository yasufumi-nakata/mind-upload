---
title: "2026-04-03 site deepening audit: literature sleep replay route sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **remaining literature-hub compression inside the site's sleep replay / replay-coupling lane**.

By 2026-04-03, the front-door and verification-side pages had already been tightened:

- `index.md`
- `wbe_101.md`
- `faq.md`
- `verification.md`
- `wiki/homeostatic-plasticity-and-maintenance-state.md`

Those pages already blocked the shortcut that:

- `a cue was delivered`
- `an oscillation changed`
- `overnight memory changed`

could be read as one generic `sleep replay worked` sentence.

However, the two literature hubs that decide how readers group evidence still lagged behind that stricter rule:

- `mind_uploading_papers.md`
- `research_harvest_50.md`

# Why This Needed Correction

## 1. The current literature does not support one generic sleep replay row

- [Ngo et al. (2013)](https://doi.org/10.1016/j.neuron.2013.03.006) established a **phase-locked slow-oscillation stimulation route**.
- [Whitmore et al. (2022)](https://doi.org/10.1038/s41539-021-00119-2) showed that **TMR benefit depends on ample and undisturbed slow-wave sleep**.
- [Baxter et al. (2023)](https://doi.org/10.1093/sleep/zsad206) showed that **oscillation gains can occur without extra motor-memory gain**.
- [Geva-Sagiv et al. (2023)](https://doi.org/10.1038/s41593-023-01324-5) showed an **intracranial hippocampal-prefrontal synchrony intervention route**.
- [Schreiner et al. (2024)](https://doi.org/10.1038/s41467-024-49572-8) showed a **spindle-locked ripple route**.
- [Whitmore et al. (2024)](https://doi.org/10.1038/s41539-024-00276-0) showed **memory-age dependence under sleep disruption**.
- [Jourde et al. (2025)](https://doi.org/10.1093/sleepadvances/zpaf007) showed that **spindle-targeted auditory stimulation can either amplify sigma or truncate the spindle depending on timing**.
- [Duan et al. (2025)](https://doi.org/10.1038/s41467-025-57766-x) showed **item-level electrophysiological variability in human consolidation**.
- [Deng et al. (2025)](https://doi.org/10.1016/j.neuron.2025.03.020) showed a **time-windowed NREM physiology gate**.
- [Shin et al. (2025)](https://doi.org/10.1038/s41539-025-00340-3) showed a **difficulty-conditioned personalized TMR route**.

Therefore, the safe reading is not `sleep replay worked`, but a route-typed statement about:

- cueing or intervention route
- sleep-integrity / disturbance burden
- NREM physiology gate
- oscillation-versus-memory effect split
- memory-selection / difficulty / age regime

## 2. The site had already fixed this on the front door, but not in the literature grouping layer

That mismatch was technically serious because these two pages decide how readers classify papers before they reach deeper route cards.

If the front door is strict but the literature map is coarse, the shortcut re-enters through the archive layer:

- a spindle paper sounds like a replay paper
- a replay paper sounds like a memory-gain paper
- a memory-gain paper sounds like a mechanistic controller readout

The current primary literature does not justify that collapse.

# Changes Executed In This Session

## `mind_uploading_papers.md`

- updated the front-matter `note`, `known_points`, and `page_highlights` so the archive front door now names the sleep replay route-family split explicitly
- expanded the `technical-fast-lane` framing so maintenance-state reading now includes `sleep replay / replay-coupling route families`
- added a new front-door note:
  - `Read sleep replay papers as route-family claims, not as one overnight-memory row`
- added a dedicated row to the `technical evidence class` table:
  - `sleep replay / replay-coupling route family`

## `research_harvest_50.md`

- updated the front-matter `note`, `page_highlights`, and `known_points` so U3 now explicitly includes a sleep replay route-family split
- strengthened the `technical-priority-route` table so U3 verification now requires:
  - sleep replay / replay-coupling route family
  - sleep-integrity / disturbance burden
  - NREM substate / physiology gate
  - oscillation gain versus memory gain
  - item / difficulty / memory-age regime
- added a new literature-route note:
  - `Read U3 sleep replay papers as route-family claims, not as one overnight-memory row`
- updated the U3 `What has some traction now` section so sleep replay is treated as a route-split maintenance family
- updated the U3 unresolved section so the remaining gap is now stated as:
  - no living-human whole-brain route that directly identifies which replay event or physiology gate preserved a given item
- expanded the U3 representative references with the sleep replay route-family anchors
- updated the literature-hub cross-link note so paper-level anchors now explicitly include `sleep replay / replay-coupling route-family splits`

# Main Critique

The scientific problem was **not** that the site still treated all sleep evidence as one class. That mistake had already been corrected on the main public pages.

The remaining weakness was subtler:

- the archive page still let readers group sleep replay papers too coarsely
- the evidence bank still let U3 hide sleep replay inside a generic maintenance bucket

That was a real taxonomy problem. In the current literature, the key question is no longer just whether memory changed after sleep. It is whether the paper isolated:

1. the intervention or cueing route
2. the sleep-integrity burden
3. the NREM physiology gate
4. the oscillation-versus-memory relation
5. the memory subset that carried the effect

Without those fields, the literature layer silently overpromotes heterogeneous results into one mechanistic row. The site's deeper policy was already stricter than that; this run made the literature hubs obey the same rule.

# Verification

- Ran `git diff --check`.
- Ran `ruby scripts/build_summary_booklet.rb`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Verified the new sleep replay route-family language in:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`

# External Dependency Tasks

- None.
  - This run stayed within executable repository work: primary-source verification, literature-hub revision, local build validation, and Git operations.

# References

1. Ngo HVV, Martinetz T, Born J, Mölle M. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. *Neuron*. 2013. https://doi.org/10.1016/j.neuron.2013.03.006
2. Whitmore NW, Bassard AM, Paller KA. Targeted memory reactivation of face-name learning depends on ample and undisturbed slow-wave sleep. *npj Science of Learning*. 2022. https://doi.org/10.1038/s41539-021-00119-2
3. Baxter BS, Mylonas D, Kwok KS, et al. The effects of closed-loop auditory stimulation on sleep oscillatory dynamics in relation to motor procedural memory consolidation. *Sleep*. 2023. https://doi.org/10.1093/sleep/zsad206
4. Geva-Sagiv M, Mankin EA, Eliashiv D, et al. Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans. *Nature Neuroscience*. 2023. https://doi.org/10.1038/s41593-023-01324-5
5. Schreiner T, Griffiths BJ, Kutlu M, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-024-49572-8
6. Whitmore NW, Yamazaki EM, Paller KA. Targeted memory reactivation with sleep disruption does not weaken week-old memories. *npj Science of Learning*. 2024. https://doi.org/10.1038/s41539-024-00276-0
7. Jourde HR, Sobral M, Beltrame G, Coffey EBJ. Neurophysiological effects of targeting sleep spindles with closed-loop auditory stimulation. *Sleep Advances*. 2025. https://doi.org/10.1093/sleepadvances/zpaf007
8. Duan W, Xu Z, Chen D, et al. Electrophysiological signatures underlying variability in human memory consolidation. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57766-x
9. Deng Z, Fei X, Zhang S, Xu M. A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. *Neuron*. 2025. https://doi.org/10.1016/j.neuron.2025.03.020
10. Shin G-H, Kweon Y-S, Oh S, et al. Personalized targeted memory reactivation enhances consolidation of challenging memories via slow wave and spindle dynamics. *npj Science of Learning*. 2025. https://doi.org/10.1038/s41539-025-00340-3
