---
title: "2026-04-04 site deepening audit: U8-1 phase-targeting estimability sync"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **route-packet overcompression inside [`wiki/u8-1-closed-loop-delay-tolerance-route.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/u8-1-closed-loop-delay-tolerance-route.md)**.

The packet was already correct about the broad operational claim:

- `U8-1` should stay bounded
- the first artifact should be a safety-facing dashboard
- one timing number should not generalize across loop classes

But it still treated the main public-open anchor, `D20 Closed-loop auditory stimulation targeting REM oscillations`, too much like a **generic delay-tolerance row**.

That was scientifically weaker than the rest of the site.

The deeper page [`wiki/closed-loop-latency-jitter-and-safety-stops.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops.md) had already moved to the stricter rule:

- `low latency` is not `oscillation estimability`
- `correct phase targeting` is not `downstream physiological or behavioral effect`
- `one useful phase this session` is not `stable preferred phase across sessions`

`U8-1` had not yet absorbed that rule into the packet itself.

# Why This Needed Correction

## 1. `D20` is a phase-targeting family, not a generic timing family

[Jaramillo et al. (2024)](https://doi.org/10.1093/sleep/zsae193) delivered auditory stimulation phase-locked to alpha or theta oscillations during REM sleep and reported phase-dependent changes in oscillatory power and frequency.

Critique:

- this is not only a timing route
- it is a **phase-targeting** route
- therefore it inherits a stricter stop line than a generic latency dashboard

If the route packet says only `delay tolerance` and `safety KPI dashboard`, it quietly erases the scientific object that makes `D20` worth selecting in the first place.

## 2. Phase-targeted loops have an estimability wall before they have a control claim

- [Zrenner et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116761) showed that real-time phase estimation degrades when oscillatory amplitude and SNR are low.
- [Gordon et al. (2021)](https://doi.org/10.3389/fnhum.2021.691821) showed that prefrontal theta-triggered stimulation required additional rules to reject low-amplitude and phase-reset epochs.
- [Kim et al. (2023)](https://doi.org/10.1523/ENEURO.0050-23.2023) showed across multiple public datasets that prediction accuracy improves mainly with higher power / SNR and with waiting for eligible epochs.

Critique:

- a fast event marker is not enough
- even a low average delay is not enough
- the packet must also disclose whether the target oscillation was actually estimable when stimulation was attempted

Without that disclosure, the row overreads hardware speed as biological target visibility.

## 3. Targeting success is not the same object as effect

- [Vigué-Guix et al. (2022)](https://doi.org/10.1111/ejn.14931) achieved reliable trial-to-trial alpha phase locking without a consistent behavioral benefit.

Critique:

- `phase was hit` is not `function changed`
- a packet that tracks only timing and trigger success still leaves the effect question unresolved

Therefore `U8-1` needed a separate `effect readout` field, not only a timing artifact.

## 4. A useful phase in one session is not a stable controller

- [Hougland et al. (2025)](https://doi.org/10.1016/j.brs.2025.09.019) showed within-session fluctuation and low test-retest reliability of the optimal mu-phase.

Critique:

- a packet that stops at one session-level phase estimate can still be scientifically too weak
- phase stability and abstention policy need to remain visible even in a bounded public packet

Otherwise the route silently upgrades from `local timing artifact` to `stable controller claim`.

# Root Critique

The criticism is precise:

1. `U8-1` correctly aimed to keep the route bounded.
2. But it still compressed a **phase-targeting REM loop** into a mostly **delay-tolerance** framing.
3. The primary literature does not support that compression.
4. `estimability`, `targeting accuracy`, `downstream effect`, and `phase stability` are distinct evidence objects.
5. Therefore the packet had to be rewritten so the first artifact is not just a delay dashboard, but a delay dashboard plus a phase-targeting log.

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/u8-1-closed-loop-delay-tolerance-route.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/u8-1-closed-loop-delay-tolerance-route.md)
  - updated `last_updated` to `2026-04-04`
  - updated the front-matter note to disclose the phase-targeting sync
  - tightened the `D20` anchor description so it is read as a REM phase-targeting family rather than a generic delay row
  - tightened the recheck bullet that points to the deeper closed-loop page so `phase-targeting estimability` is visible at packet level
  - added a new note box explaining why `D20` cannot stay a delay-only anchor
  - added a compact `phase-targeting field` table so oscillation gate, targeting metric, downstream effect, and stability policy stay explicit
  - expanded the `What the first artifact can honestly close now` table so the packet now requires a `Phase-targeting log`
  - added an external-dependency reminder that estimability, effect, and phase stability remain separate evidence objects even within the current REM family

- Added [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_u8_1_phase_targeting_estimability_sync.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_u8_1_phase_targeting_estimability_sync.md)
  - records the critique, rationale, and source trail for this correction

# Verification

- `git diff --check`
- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "phase-targeting log|oscillation gate|D20 Closed-loop auditory stimulation targeting REM oscillations|delay-only anchor" wiki/u8-1-closed-loop-delay-tolerance-route.md github-wiki-export/u8-1-closed-loop-delay-tolerance-route.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: source verification, public-content edits, wiki export, local build validation, and Git publication.

# References

1. Jaramillo V, Garside P, de Mello G, et al. Closed-loop auditory stimulation targeting REM oscillations. *Sleep*. 2024. https://doi.org/10.1093/sleep/zsae193
2. Zrenner C, Galevska D, Nieminen JO, et al. The shaky ground truth of real-time phase estimation. *NeuroImage*. 2020. https://doi.org/10.1016/j.neuroimage.2020.116761
3. Gordon PC, Desideri D, Belardinelli P, et al. Prefrontal theta-phase synchronized brain stimulation with real-time EEG-triggered TMS. *Frontiers in Human Neuroscience*. 2021. https://doi.org/10.3389/fnhum.2021.691821
4. Vigué-Guix I, Morís Fernández L, Torralba Cuello M, et al. Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain-computer interface (BCI)? *European Journal of Neuroscience*. 2022. https://doi.org/10.1111/ejn.14931
5. Kim CS, Leveille E, Kharbouch A, et al. Closed-loop phase prediction across public datasets reveals power- and SNR-dependent timing limits. *eNeuro*. 2023. https://doi.org/10.1523/ENEURO.0050-23.2023
6. Hougland B, et al. Within-session drift and low test-retest reliability of optimal mu-phase for stimulation. *Brain Stimulation*. 2025. https://doi.org/10.1016/j.brs.2025.09.019
