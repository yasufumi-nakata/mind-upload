# RQ60 EEG-Funds Revalidation (2026-03-17 04:04 JST)

## Scope
- Revalidate whether all 60 `mind-upload` research questions remain solvable with EEG evidence tiers (`A/B/C`).
- Reconfirm `auto-research-funds` submission themes and fixed EEG dataset assignment.
- Preserve deep-dive policy: `1RQ=1 verification claim=1 submission theme=1 primary dataset`.

## Checks
- Pulled latest `main` before work.
- Recounted RQ rows from `research_harvest_50.md`: total `60`.
- Rechecked U breakdown: `U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`.
- Reconfirmed `A/B/C = 17/25/18` in `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`.
- Compared with `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`.

## Findings
- No missing RQ lines and no numbering gaps.
- `G1-G6` definitions and priority queue are consistent between repos.
- A representation mismatch remains for 6 focused RQs (`U1-2`, `U7-2`, `U8-2`, `U13-1`, `U14-1`, `U15-2`):
  - `mind-upload` RQ table uses numeric `ID` sets (feasibility-side candidate pool).
  - `auto-research-funds` map uses fixed `D` keys (submission-side canonical keys).

## Decision
- Keep submission canonical source as `D1-D16 + DOI + dataset name`.
- Treat numeric `ID` references in RQ table as auxiliary feasibility references.
- Added explicit run logs to both wiki pages to avoid ambiguity.

## Fixed submission mapping (this run)
- `U1-2`: `D7/D12` -> `G4`
- `U7-2`: `D7/D4` -> `G3`
- `U8-2`: `D10/D8` -> `G2`
- `U13-1`: `D2/D1` -> `G1`
- `U14-1`: `D12/D8` -> `G1`
- `U15-2`: `D4/D5` -> `G6`
