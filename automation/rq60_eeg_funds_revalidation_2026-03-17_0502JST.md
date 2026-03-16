# RQ60 EEG-Funds Revalidation (2026-03-17 05:02 JST)

## Scope
- Revalidate whether all 60 `mind-upload` research questions remain solvable with EEG evidence tiers (`A/B/C`).
- Reconfirm `auto-research-funds` submission themes and fixed EEG dataset assignment.
- Keep deep-dive policy: `1RQ=1 verification claim=1 submission theme=1 primary dataset`.

## Pull baseline
- `mind-upload`: `eb20d32b7877`
- `EEG-DATA`: `48261b83b1de`
- `auto-research-funds`: `05a5d3664abb`

## Checks
- Recounted RQ rows from `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`: `RQ_TOTAL=60`.
- Reconfirmed U breakdown: `U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`.
- Reconfirmed `A/B/C=17/25/18`.
- Rechecked numeric dataset IDs used in the RQ table: `17 IDs` (`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`), missing `0` in `EEG-DATA/eeg_dataset_summary_ja.csv`.
- Rechecked canonical submission keys `D1-D16` DOI presence in `EEG-DATA/eeg_dataset_summary_ja.csv`: missing `0`.
- Rechecked grant keys `G1-G6` (`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`): missing `0`.

## Decision
- Keep canonical submission references as `D-key + DOI + dataset name`.
- Keep numeric `ID` in `mind-upload` RQ table as auxiliary feasibility-side references.
- Keep queue priority unchanged because no feasibility or grant-key breakage was found.

## Priority queue (unchanged)
1. `G1`: `U14-RQ1` (`D12/D8`)
2. `G3`: `U7-RQ2` (`D7/D4`)
3. `G2`: `U8-RQ2` (`D10/D8`)
4. `G4`: `U1-RQ2` (`D7/D12`)
5. `G1`: `U13-RQ1` (`D2/D1`)
6. `G6`: `U15-RQ2` (`D4/D5`)
