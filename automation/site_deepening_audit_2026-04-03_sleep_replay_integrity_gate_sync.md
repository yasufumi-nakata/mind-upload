---
title: "2026-04-03 site deepening audit: sleep replay integrity and physiology-gate sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **remaining audit gap inside the site's sleep replay route family**.

Earlier passes had already done important work:

- separating `sleep / wake history` from `sleep architecture / replay-coupling`
- separating phase-locked stimulation, scalp decoding, intracranial synchrony intervention, ripple-linked evidence, and item-selective TMR

However, the public pages still did not force three additional checks strongly enough:

- **sleep-integrity / disturbance burden**
- **NREM substate / physiology gate**
- **oscillation gain versus memory gain, plus memory-age / selection dependence**

That gap mattered because the current primary literature does not support reading `sleep happened`, `oscillations increased`, `a cue was delivered`, and `memory improved` as one mechanistic ladder.

# Why This Needed Correction

## 1. The newer sleep literature does not support one generic `sleep replay worked` sentence

- [Whitmore et al. (2022)](https://doi.org/10.1038/s41539-021-00119-2) showed that targeted memory reactivation benefit depended on **ample and undisturbed slow-wave sleep**, not merely cue delivery.
- [Baxter et al. (2023)](https://doi.org/10.1093/sleep/zsad206) showed that **closed-loop auditory stimulation can modify SO / spindle dynamics without yielding extra motor-memory benefit** when sleep continuity is compromised.
- [Schreiner et al. (2023)](https://doi.org/10.1038/s41467-023-43450-5) showed that **respiration-linked coupling** is relevant to human sleep oscillations and reactivation strength.
- [Whitmore et al. (2024)](https://doi.org/10.1038/s41539-024-00276-0) showed that **sleep-disruption effects are not identical across memory ages**.
- [Deng et al. (2025)](https://doi.org/10.1016/j.neuron.2025.03.020) showed that even within NREM, consolidation depends on a **time-structured physiological window**.

Therefore, current evidence requires a stricter reading rule:

- `a cue was presented` is not yet `the relevant consolidation window was matched`
- `oscillations changed` is not yet `memory improved for the relevant reason`
- `overnight memory changed` is not yet `replay-coupling was identified`

## 2. The site had already split route families, but the public wording still under-specified the audit burden

Before this run, the repository already had:

- a sleep architecture / replay-coupling row
- a dedicated sleep replay route card
- front-door warnings against treating all sleep evidence as one class

But the public wording still left too much room for an overread in which a reader could move from:

- stage label
- cue timing
- overnight score change

to a stronger mechanistic interpretation without having to state:

- whether sleep continuity was preserved
- whether the claim depended on a finer NREM physiology gate
- whether the effect generalized across item types or memory ages

That was inconsistent with the site's general scientific policy, which is to keep route family, direct observable, and claim ceiling explicit.

# Web-Verified Primary Sources Checked On 2026-04-03

1. Ngo HVV, Martinetz T, Born J, Mölle M. *Neuron*. 2013. https://doi.org/10.1016/j.neuron.2013.03.006
2. Whitmore NW, Bassard AM, Paller KA. *npj Science of Learning*. 2022. https://doi.org/10.1038/s41539-021-00119-2
3. Baxter BS, Mylonas D, Kwok KS, et al. *Sleep*. 2023. https://doi.org/10.1093/sleep/zsad206
4. Schreiner T, Petzka M, Staudigl T, Staresina BP. *Nature Communications*. 2021. https://doi.org/10.1038/s41467-021-23520-2
5. Schreiner T, Petzka M, Staudigl T, et al. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-43450-5
6. Geva-Sagiv M, Mankin EA, Eliashiv D, et al. *Nature Neuroscience*. 2023. https://doi.org/10.1038/s41593-023-01324-5
7. Schreiner T, Griffiths BJ, Kutlu M, et al. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-024-49572-8
8. Whitmore NW, Yamazaki EM, Paller KA. *npj Science of Learning*. 2024. https://doi.org/10.1038/s41539-024-00276-0
9. Jourde N, Fattinger S, Teague M, et al. *NeuroImage*. 2025. https://doi.org/10.1016/j.neuroimage.2025.121530
10. Deng Z, Fei X, Zhang S, Xu M. *Neuron*. 2025. https://doi.org/10.1016/j.neuron.2025.03.020
11. Duan W, Xu Z, Chen D, et al. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57766-x
12. Shin G-H, Kweon Y-S, Oh S, et al. *npj Science of Learning*. 2025. https://doi.org/10.1038/s41539-025-00340-3

# Changes Executed In This Session

## Public pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - tightened the landing-page stop rule so `sleep happened`, `oscillations increased`, `cue delivered`, and `memory changed` are no longer readable as one claim
  - added explicit front-door language for `sleep-integrity / disturbance burden`, `NREM substate / physiology gate`, and `memory subset / age`
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - upgraded the entry-layer sleep replay note and route summary so oscillation gain is not overread as replay-mechanism evidence
  - tightened the hidden-state row to require sleep-integrity and physiology-gate disclosure
- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - strengthened the maintenance-state error budget so sleep replay claims must report stage composition, physiology gate, disturbance burden, cue timing / dose, and memory-age or selection regime
  - updated the evidence-driven rationale and shorter summary rows to match the stricter rule
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - rewrote the front-door sleep replay explanation so recent primary sources block mechanistic overread at the FAQ layer
  - extended the bibliography with the newly used sleep-continuity and physiology-gate sources
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md)
  - expanded the route card itself with explicit fields for `Sleep-integrity / disturbance burden` and `NREM substate / physiology gate`
  - separated `oscillation gain` from `memory gain` and broadened the selection field to include `memory-age regime`

## Generated output check

- [`/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md)
  - regenerated after the source edits as a synchronization check; this run produced no additional tracked diff in the generated booklet

# Main Critique

The site was no longer making the old mistake of treating all sleep replay evidence as one undifferentiated class. That correction had already happened. The remaining problem was subtler and, scientifically, still important: the public wording had not yet made the **minimum audit burden** explicit enough.

In the current literature, a sleep replay claim has to answer at least four separable questions:

1. **Was the relevant event timed correctly?**
2. **Did the intervention preserve sleep integrity rather than merely alter oscillations?**
3. **Which physiological NREM substate or gate actually mattered?**
4. **Which memory subset, difficulty regime, or memory age carried the reported effect?**

Without those fields, even a technically literate reader can still overread a heterogeneous literature into a single `sleep replay success` row. That was the main scientific weakness corrected in this run.

# Verification

- Ran `git diff --check`.
- Ran `ruby scripts/build_summary_booklet.rb`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Reviewed the resulting diffs to confirm that the new wording appears on the landing page, FAQ layer, WBE entry page, verification rules, and sleep replay route card.

# External Dependency Tasks

- None.
  - This run stayed within executable repository work: literature verification, public-page revision, generated-summary refresh, local build validation, and Git operations.

# References

1. Ngo HVV, Martinetz T, Born J, Mölle M. Auditory closed-loop stimulation of the sleep slow oscillation enhances memory. *Neuron*. 2013. https://doi.org/10.1016/j.neuron.2013.03.006
2. Whitmore NW, Bassard AM, Paller KA. Targeted memory reactivation of face-name learning depends on ample and undisturbed slow-wave sleep. *npj Science of Learning*. 2022. https://doi.org/10.1038/s41539-021-00119-2
3. Baxter BS, Mylonas D, Kwok KS, et al. The effects of closed-loop auditory stimulation on sleep oscillatory dynamics in relation to motor procedural memory consolidation. *Sleep*. 2023. https://doi.org/10.1093/sleep/zsad206
4. Schreiner T, Petzka M, Staudigl T, Staresina BP. Endogenous memory reactivation during sleep in humans is clocked by slow oscillation-spindle complexes. *Nature Communications*. 2021. https://doi.org/10.1038/s41467-021-23520-2
5. Schreiner T, Petzka M, Staudigl T, et al. Respiration modulates sleep oscillations and memory reactivation in humans. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-43450-5
6. Geva-Sagiv M, Mankin EA, Eliashiv D, et al. Augmenting hippocampal-prefrontal neuronal synchrony during sleep enhances memory consolidation in humans. *Nature Neuroscience*. 2023. https://doi.org/10.1038/s41593-023-01324-5
7. Schreiner T, Griffiths BJ, Kutlu M, et al. Spindle-locked ripples mediate memory reactivation during human NREM sleep. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-024-49572-8
8. Whitmore NW, Yamazaki EM, Paller KA. Targeted memory reactivation with sleep disruption does not weaken week-old memories. *npj Science of Learning*. 2024. https://doi.org/10.1038/s41539-024-00276-0
9. Jourde N, Fattinger S, Teague M, et al. The effectiveness of auditory stimulation in sleep varies with thalamocortical spindle phase. *NeuroImage*. 2025. https://doi.org/10.1016/j.neuroimage.2025.121530
10. Deng Z, Fei X, Zhang S, Xu M. A time window for memory consolidation during NREM sleep revealed by cAMP oscillation. *Neuron*. 2025. https://doi.org/10.1016/j.neuron.2025.03.020
11. Duan W, Xu Z, Chen D, et al. Electrophysiological signatures underlying variability in human memory consolidation. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-57766-x
12. Shin G-H, Kweon Y-S, Oh S, et al. Personalized targeted memory reactivation enhances consolidation of challenging memories via slow wave and spindle dynamics. *npj Science of Learning*. 2025. https://doi.org/10.1038/s41539-025-00340-3
