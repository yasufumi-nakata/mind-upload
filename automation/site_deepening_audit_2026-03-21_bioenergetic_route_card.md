# Site Deepening Audit (2026-03-21, Bioenergetic / Mitochondrial Route Card)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 運用ルール反映: `verification.md`
- 入口反映: `wbe_101.md`, `index.md`

## 今回の選定理由

- サイトはすでに `bioenergetic / mitochondrial state` を hidden-state として明示しており、`glial support` や `human metabolic connectome` と別物であることもかなり整理できていました。
- しかし 2026-03-21 時点でも、`energetic evidence` がなお一つの証拠クラスとして読める余地が残っていました。
- このままでは、技術・自然科学の観点で読者が `presynaptic ATP-linked respiration`、`dendritic mitochondrial positioning / fission`、`synaptic ATP synthase nano-organization`、`mitochondrial Ca2+ efflux tuning`、`human macro energetic imaging` を同じ inferential object として圧縮しやすい状態でした。

## 根拠付き批判

### 1. Presynaptic energetic support と dendritic plasticity support は同じ claim family ではありません

- 問題:
  - 既存サイトは `local ATP reserve` と `mitochondrial positioning` を同じ hidden-state family に入れていましたが、`どの compartment の何を直接見たのか` の開示がまだ弱く、presynaptic と dendritic の差が route-card 化されていませんでした。
- 根拠:
  - Rangaraju et al. (2014) は activity-driven local ATP synthesis が presynaptic function に必要であることを示しました。
  - Underwood et al. (2023) は contextual fear training により CA1 presynaptic terminal の mitochondrial respiration が上がり、Drp1 関連介入で memory が落ちることを示しました。
  - Rangaraju et al. (2019), Divakaruni et al. (2018), Bapat et al. (2024) は、dendritic compartment 側で local translation, LTP induction, mitochondria stabilization を扱っています。
- 批判:
  - したがって `energetics matters` だけでは粗すぎます。presynaptic energetic support と dendritic plasticity support は別の inferential object であり、同じ 1 行に圧縮すべきではありません。

### 2. Organelle micro-organization と bulk energetic rate は同じ quantity type ではありません

- 問題:
  - 既存サイトは human energetic imaging を macro proxy として demote できていましたが、`nano-organization`, `respiration`, `metabolic rate map` の quantity type の差は route-card として固定されていませんでした。
- 根拠:
  - Hu et al. (2025) は synaptic mitochondria 内 ATP synthase の polarized reorganization を MINFLUX ベースで示しました。
  - Li et al. (2025) は dynamic DMRSI と kinetic model により whole-brain glucose transport と metabolic rates を推定しました。
  - Ren et al. (2015) は 31P-MRS により ATP synthesis, metabolite concentration, pH を示しました。
- 批判:
  - したがって `mitochondrial ATP-related evidence` という一語で、nanostructure, respiration, and model-based macro rate imaging を同列に扱うのは不適切です。

### 3. Metabolic tuning intervention と local state readout は別です

- 問題:
  - 近年文献は mitochondrial metabolism を操作して memory を変える方向へ進んでいますが、それは `local state was fully read out` とは別の claim です。
- 根拠:
  - Vishwanath et al. (2026) は Letm1-mediated mitochondrial Ca2+ efflux を操作し、neuronal metabolism と long-term memory across species を変えました。
- 批判:
  - したがって `controller manipulation works` を `the relevant mitochondrial state was measured and identified` に昇格させてはなりません。
  - route card なしでは intervention claim と observability claim が混ざります。

### 4. Human energetic imaging は依然として macro proxy class です

- 問題:
  - 既存サイトはこの点を説明していましたが、front door ではなお `human energetic imaging exists` から `human local mitochondrial state is partly solved` へ飛ぶ誤読余地が残っていました。
- 根拠:
  - Ren et al. (2015) は healthy human brain における 31P-MRS の ATP synthesis / metabolite concentrations / pH を示しました。
  - Li et al. (2025) は 7T dynamic DMRSI で whole-brain CMRGlc, CMRLac, VTCA, Tmax を示しました。
- 批判:
  - しかし、これらは branch-specific ATP reserve, synapse-neighbor mitochondrial residence, fission/fusion controller, or cell-specific Ca2+ efflux control を直接は示しません。
  - したがって human energetic imaging は route card 上 `macro energetic proxy` として明示しない限り危険です。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights`, `known_points`, `unknown_points` を route-card 方針へ更新しました。
  - bioenergetic section 本文に Underwood et al. (2023) と Vishwanath et al. (2026) を追加しました。
  - `#bioenergetic-route-card` を新設し、以下の field を固定しました。
    - claim family
    - biological regime / compartment
    - direct energetic observable
    - controller / perturbation route
    - quantity type / model burden
    - functional target
    - human observability / external calibration
    - abstention boundary
  - references に Underwood et al. (2023), Vishwanath et al. (2026) を追加しました。
- `verification.md`
  - `page_highlights` に bioenergetic route-card rule を追加しました。
  - maintenance-state error budget の `Bioenergetic / mitochondrial support` 行を route-card 粒度へ拡張しました。
  - `bioenergetic evidence also needs a route card` note を追加しました。
  - references に Underwood et al. (2023), Vishwanath et al. (2026) を追加しました。
- `wbe_101.md`
  - `page_highlights` に bioenergetic evidence is not one class を追加しました。
  - entry-level note `Bioenergetic evidence now gets its own route card` を追加しました。
  - references に Underwood et al. (2023), Vishwanath et al. (2026) を追加しました。
- `index.md`
  - landing-page highlight を更新しました。
  - `If You Are Treating Energetic Evidence As One Solved Row` note を追加し、front door で energetic evidence の圧縮誤読を止めました。

## 外部依存で保留

- same-subject benchmark for calibrating human energetic proxies against local mitochondrial controllers
  - 担当者: external human neuroimaging / cellular-calibration researchers
  - 前提条件: same-subject design linking macro energetic imaging with externally validated local energetic targets or perturbation-calibrated controller variables
  - 完了条件: the site can point to a public benchmark showing which human energetic proxy reduces which local mitochondrial uncertainty term

## 参考文献

1. Rangaraju V, Calloway N, Ryan TA. Activity-driven local ATP synthesis is required for synaptic function. *Cell*. 2014;156(4):825-835.
   - https://doi.org/10.1016/j.cell.2013.12.042
2. Rangaraju V, Lauterbach M, Schuman EM. Spatially stable mitochondrial compartments fuel local translation during plasticity. *Cell*. 2019;176(1-2):73-84.e15.
   - https://doi.org/10.1016/j.cell.2018.12.013
3. Divakaruni SS, Van Dyke AM, Chandra R, et al. Long-term potentiation requires a rapid burst of dendritic mitochondrial fission during induction. *Neuron*. 2018;100(4):860-875.e7.
   - https://doi.org/10.1016/j.neuron.2018.09.025
4. Underwood EL, Redell JB, Hood KN, et al. Enhanced presynaptic mitochondrial energy production is required for memory formation. *Scientific Reports*. 2023;13:14431.
   - https://doi.org/10.1038/s41598-023-40877-0
5. Bapat P, Nirschl JJ, Wilkerson JR, et al. VAP stabilizes dendritic mitochondria to locally support synaptic plasticity. *Nature Communications*. 2024;15:742.
   - https://doi.org/10.1038/s41467-023-44233-8
6. Hu H, Tang J, Wu Y, et al. Polarized ATP synthase in synaptic mitochondria induced by learning and plasticity signals. *Communications Biology*. 2025;8:166.
   - https://doi.org/10.1038/s42003-025-08963-3
7. Vishwanath AA, Comyn T, Mira RG, et al. Mitochondrial Ca2+ efflux controls neuronal metabolism and long-term memory across species. *Nature Metabolism*. 2026;8:467-488.
   - https://doi.org/10.1038/s42255-026-01451-w
8. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015;28(11):1455-1462.
   - https://doi.org/10.1002/nbm.3384
9. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025;4(3):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
