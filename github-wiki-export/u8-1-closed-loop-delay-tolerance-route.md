# Wiki: U8-1 closed-loop delay-tolerance route packet

> A next-watch closed-loop packet outside the current public six
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-04-04 / Role: U8-1 route packet (updated with phase-targeting estimability sync)

## Role Of This Page
This page records one narrow next-watch route outside the current public six at the level of one question, one public-open closed-loop anchor, one bounded first artifact, and one funding bridge.

## Accuracy Notes
This page does not change the active public six-question batch. It only records what the present U8-1 closed-loop route can honestly close first.

## Back To Public Pages
- [Issue page](https://mind-upload.com/issue.html)
- [Data & Bench](https://mind-upload.com/datasets.html)

## Related Wiki Pages
- [Wiki: Current public six route brief](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-current-public-six-rq-brief) - The compact six-row public route that still stays unchanged.
- [Wiki: Closed loop, delay, jitter, safe stop](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - The timing, safety-stop, and co-adaptation page that now makes this row readable more narrowly.
- [Wiki: Deep focus notes](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-rq60-deep-focus-notes) - The wider working note for all current practical rows.
- [Wiki: Grant and dataset playbook](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook) - The fixed funding and anchor map.

---

# U8-1 closed-loop delay-tolerance route packet

This page does not change the current public six-question batch. It records one narrow route just outside that batch, so readers can see why `U8-1` is the next bounded closed-loop route to deepen, why `D20` stays the cleanest public-open first anchor for that row, and what the first public-safe artifact can honestly close.

## What was rechecked for this row

- `D20 Closed-loop auditory stimulation targeting REM oscillations` still remains the cleanest public-open first anchor for `U8-1`, because it is already a real REM phase-targeting family with explicit estimability, targeting, and stop-intervention failure modes rather than a generic offline benchmark.
- `D21 NeuroSimo: closed-loop EEG/EMG-guided TMS` remains the strongest support family once the row needs an explicit trigger / stop / recovery cross-check in a second intervention setting.
- `D12 Longitudinal MI-BCI training with transcutaneous spinal stimulation` remains a useful support family for durability and retraining burden, but it still fits `U8-6` more directly than the first `U8-1` packet.
- The refreshed `closed-loop latency / jitter / safe stop` page now keeps timing, phase-targeting estimability, co-adaptation, rescue-mode recalibration, and body/environment incompleteness separate, which makes `U8-1` readable as a bounded operations packet rather than as a universal latency claim.
- The current public six-question batch still stays unchanged: `U13-2 / U13-5 / U0-2 / U0-3 / U14-4 / U14-2`.
- The practical funding bridge for this row is still watch-only rather than a current public-six route: `Japan Industrial Science Research Institute research grant` and `Nakatani Foundation research grant` remain the cleanest fits, and existing Todoist watch tasks already cover both lanes.

## Why `U8-1` is the next bounded closed-loop route outside the current six

- It is a `B` row: the useful first claim is still real, but it must stay explicitly bounded and must keep external dependencies visible.
- It is control-and-safety-first: the first artifact is a `closed-loop safety KPI dashboard`, not a claim that one timing number already solves closed-loop stability.
- It extends the outside-current-six route without widening the public claim surface. `U7-1` fixes synchronization discipline, `U1-2` fixes inverse-estimation uncertainty, `U4-2` fixes a narrow intervention rule, and `U8-1` fixes the delay-tolerance and safety-stop boundary for one named loop family.

## Why `D20` stays the main public-open anchor

| Candidate | What it helps with | Why it is not the first public anchor |
|---|---|---|
| `D20 Closed-loop auditory stimulation targeting REM oscillations` (`10.5281/zenodo.10663994`, immediate) | It is already a named REM phase-targeting family, so it is the shortest route to a bounded `stability rate / stop-intervention rate / recovery time` dashboard plus a disclosed `phase-targeting log` instead of a generic timing story. | None in this run. It is the cleanest public-open first anchor for `U8-1`. |
| `D21 NeuroSimo: closed-loop EEG/EMG-guided TMS` (`10.5281/zenodo.14398633`, immediate) | It is the strongest nearby support family when the row needs an explicit trigger / intervention / recovery cross-check in a second closed-loop setting. | It is more protocol-specific and intervention-heavy than the first delay-tolerance packet needs. |
| `D12 Longitudinal MI-BCI training with transcutaneous spinal stimulation` (`10.5281/zenodo.15454354`, immediate) | It is useful once the row has to connect delay tolerance to fixed-decoder durability and retraining burden. | It fits `U8-6` more directly than the first `U8-1` packet, so it stays support rather than primary. |

<strong>Why `D20` cannot stay a delay-only anchor</strong>
<p>
`D20` is not merely a generic fast-loop dataset. The linked REM paper, <a href="https://doi.org/10.1093/sleep/zsae193" target="_blank">Jaramillo et al. (2024)</a>, delivered auditory stimulation phase-locked to alpha or theta oscillations during REM sleep and reported <strong>phase-dependent power and frequency changes</strong>. That makes the route scientifically narrower and stricter than a generic latency packet. <a href="https://doi.org/10.1016/j.neuroimage.2020.116761" target="_blank">Zrenner et al. (2020)</a> showed that meaningful real-time phase estimation itself degrades when oscillatory amplitude and SNR are low. <a href="https://doi.org/10.3389/fnhum.2021.691821" target="_blank">Gordon et al. (2021)</a> showed that prefrontal theta-triggered stimulation needed additional constraints to avoid low-amplitude and phase-reset epochs. <a href="https://doi.org/10.1111/ejn.14931" target="_blank">Vigu&eacute;-Guix et al. (2022)</a> showed that reliable trial-to-trial alpha phase locking still did not yield a consistent behavioral gain. <a href="https://doi.org/10.1523/ENEURO.0050-23.2023" target="_blank">Kim et al. (2023)</a> showed across public datasets that prediction quality improves primarily with higher power and SNR and with waiting for eligible epochs. <a href="https://doi.org/10.1016/j.brs.2025.09.019" target="_blank">Hougland et al. (2025)</a> then showed within-session fluctuation and low test-retest reliability of the optimal mu-phase. Therefore, the first public-safe artifact for `U8-1` cannot remain a <strong>delay-only dashboard</strong>. It also needs a <strong>phase-targeting log</strong> that keeps estimability, targeting accuracy, downstream effect, and phase-stability separate.
</p>

| `Phase-targeting field` | What the packet now has to say explicitly | What goes wrong if omitted |
|---|---|---|
| `Oscillation gate` | Which band, channel / spatial filter, power / SNR threshold, phase-reset rejection, and no-stim or missed-trigger rate defined an eligible REM epoch. | A fast trigger is overread as if the target oscillation had actually been estimable throughout the session. |
| `Targeting metric` | Which circular phase-error metric, off-target comparator, and causal-versus-post-hoc benchmark were used under the disclosed REM protocol. | Low mean latency is mistaken for correct phase targeting. |
| `Downstream effect` | Which outcome changed: power, frequency, physiology, behavior, or none, and on what time window. | Targeting success is silently promoted to physiological or behavioral efficacy. |
| `Stability policy` | Whether the preferred phase stayed fixed, drifted, or was updated within or across sessions, and how abstention was handled when the target weakened. | One locally useful phase is overread as a stable controller across the whole route. |

## What the first artifact can honestly close now

| Artifact piece | What it closes now | What still stays outside the claim |
|---|---|---|
| `Closed-loop safety KPI dashboard` | A bounded dashboard that fixes `stability rate`, `stop-intervention rate`, `recovery time`, and declared end-to-end timing percentiles for one named loop family under one disclosed protocol. | Any statement that one dashboard already gives a universal closed-loop threshold across loop types. |
| `Phase-targeting log` | A bounded log that fixes `oscillation gate`, `no-stim / missed-trigger rate`, `circular phase error`, `off-target comparator`, and `effect readout` for the present REM targeting protocol. | Any statement that a fast loop or a low average phase error already proves reliable phase-specific control or stable downstream benefit. |
| `Delay-tolerance band note` | A narrow rule for which timing deterioration begins to break the present loop class under the present protocol, oscillation gate, and stop logic. | Any statement that a single ms threshold generalizes across neurofeedback, P300 control, speech BCI, phase-targeting, and chronic adaptive stimulation. |
| `Downgrade-rule note` | A public-safe rule that keeps the row at a local-controller result whenever stability drops below the predeclared floor or recovery time drifts beyond the operating band. | Any interpretation that a fast or stable local loop is automatically boundary-complete, fixed-decoder durable, chronically deployable, or identity-relevant. |

## Funding wording that still fits

| Route | Submission wording that stays honest | Why it still fits this row |
|---|---|---|
| `Japan Industrial Science Research Institute research grant` (`watch`) | `Operational delay-tolerance and safety-stop dashboard for closed-loop EEG control in the mind-upload route` | The row reads naturally as an engineering-style operations and safety package rather than as a stronger neuroscience or mind-preservation claim. |
| `Nakatani Foundation research grant` (`next-cycle watch`) | `Control-theoretic delay-tolerance benchmark for closed-loop EEG safety and retraining boundaries` | It still fits as a bounded BME-facing validation package, but only as a watch route because the current cycle is closed. |

## External dependency tasks that stay outside this session

- Generalization across loop classes still remains outside the present packet.
- Phase-targeting estimability, downstream effect, and preferred-phase stability still remain separate evidence objects even inside the current REM family.
- Fixed-decoder durability, rescue-mode recalibration burden, and clinic/home transfer still remain separate evidence objects rather than completed claims of this row.
- Any interpretation that one closed-loop timing result proves a boundary-complete controller, a stable preserved self, or a deployable WBE loop remains outside the present route.

## What changed in this run

- The public batch did not change.
- The main change is that `U8-1` now has a public packet that records the cleanest public-open anchor, the first safety artifact, and the watch-level funding bridge after the closed-loop timing page was strengthened.
- This remains a route-setting update, not a solved-claim update.
