# Site Deepening Audit (2026-03-27, Human BBB Quantity-Type Split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `index.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 現行サイトはすでに `neurovascular-unit / BBB / pericyte state` を独立 family として扱い、measurement-side の `vascular-state / CVR audit` と切り分けていました。
- しかし、その次の段階でまだ弱い点が残っていました。`human BBB route` がなお `macro BBB permeability proxy` という一括語で読めてしまい、`water-exchange ASL` と `tracer-specific PET permeability-surface-area` が同じ quantity type であるかのように見える余地がありました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、human observability ceiling を議論する際には、`何を測ったか` の family split だけでなく、`その human row がどの transport quantity をどの measurement model で推定したのか` を固定しないと、proxy ceiling を過大評価しやすいからです。

## 根拠付き批判

### 1. `human BBB proxy` は一つの permeability meter ではありません

- 問題:
  - 旧サイトは `Padrela et al. (2025)` と `Chung et al. (2025)` を並べて human BBB route として扱っていました。
  - しかし、この表現だけでは `human BBB MRI / PET = one macro permeability proxy` と読めてしまいます。
- 根拠:
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は multi-echo ASL で BBB `water-exchange time` を扱っています。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は dynamic PET と kinetic modeling により `tracer-specific BBB permeability-surface-area product` を推定しています。
  - Chung 論文本文は、既存 BBB imaging が主に structural barrier を見てきたのに対し、自分たちの方法は `molecule-specific transport mechanism` を扱うと明記しています。
- 批判:
  - したがって、両者を単に `BBB permeability` と一括するのは粗いです。
  - ここで違うのは装置だけではなく、quantity type と transport object です。`water exchange` と `tracer-specific molecular transport` は同じ inferential object ではありません。

### 2. ASL 側ですら method dependence が残っています

- 問題:
  - 旧サイトでは `Padrela et al. (2025)` の existence によって、human BBB water route が一つの安定した quantity family であるかのように見える余地がありました。
- 根拠:
  - [Morgan et al. (2024)](https://doi.org/10.1002/nbm.5256) は同一 cohort で DP-ASL と ME-ASL を比較し、`Kw` が `106.6 ± 19.7 min^-1` と `306.8 ± 71.7 min^-1` で大きく異なり、年齢依存も一致しないことを示しました。
  - 同論文は、ASL-based BBB water-exchange quantification について standardization、bias/sensitivity analysis、independent validation が必要だと述べています。
- 批判:
  - したがって、`ASL-derived BBB water measure exists` を `BBB permeability can now be read generically in humans` へ昇格させるのは不適切です。
  - 少なくとも `DP-ASL vs ME-ASL` と fitting/model route は disclosure 項目にしなければなりません。

### 3. PET 側も generic leakiness meter ではありません

- 問題:
  - 旧サイトは `Chung et al. (2025)` を強い human BBB advance として正しく位置づけていましたが、そのまま読むと `PET now measures BBB permeability` という general statement に流れやすい状態でした。
- 根拠:
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は、three radiotracers の BBB permeability を tracer-specific transport mechanism として扱っています。
  - 同論文は human PS measurements について `lack of ground truth values in humans` を major limitation として明記しています。
- 批判:
  - つまり、ここで得られているのは `generic BBB leakiness scalar` ではなく、`named tracer under named kinetic model` の PS estimate です。
  - よって `human BBB proxy` を読むときは、少なくとも `quantity type`, `transport regime`, `model burden`, `validation status` を別欄で固定する必要があります。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を `2026-03-27` に更新
  - human BBB note-box を改稿し、`Padrela = water-exchange`, `Morgan = ASL method dependence`, `Chung = tracer-specific PET PS` を明記
  - `neurovascular-bbb-route-card` addendum を `human BBB quantity type` 問題へ更新
  - route-card table に `Human quantity type / transport regime` 行を追加
  - `Human measurement / model burden` 行を強化し、ASL/PET の validation / repeatability ceiling を明記
  - proxy table の `human BBB permeability / water-exchange proxy` を `human BBB water-exchange / tracer-specific transport proxy` へ改稿
  - references に `Morgan et al. (2024)` を追加

- `verification.md`
  - `last_updated` を `2026-03-27` に更新
  - page highlight を `human quantity type / transport regime` に更新
  - known point に `quantity-type disclosure` を追加
  - state-family table の human ceiling を `macro BBB water-exchange or tracer-specific transport-model proxy` に更新
  - neurovascular addendum を改稿し、`Padrela / Morgan / Chung` を用いて quantity-type split と validation ceiling を前面化

- `index.md`
  - `last_updated` を `2026-03-27` に更新
  - front-door highlight を `human BBB water-exchange MRI` と `tracer-specific BBB PET transport routes` に更新
  - known point を `macro water-exchange or tracer-specific transport proxy` に更新
  - neurovascular note-box に `Morgan et al. (2024)` を追加し、human BBB proxy でも quantity type disclosure が必要と明記

- `glossary.md`
  - `last_updated` を `2026-03-27` に更新
  - `Neurovascular-unit / BBB / pericyte state` の定義に `water exchange`, `tracer-specific transport`, `leakage-related state` を追記
  - `Support-state proxy` の BBB 例を `water-exchange or tracer-specific transport state` に更新

## 今回の修正で止めた誤読

- `human BBB MRI / PET = one macro permeability meter`
- `Padrela et al. (2025) と Chung et al. (2025) は measurement object がほぼ同じ`
- `ASL-derived Kw が出ている = BBB permeability can now be read generically in humans`
- `human BBB proxy exists = local pericyte / endothelial controller state is near-directly visible`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文と監査記録の更新のみで完結しています。

## 参考文献

1. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
2. Morgan CA, Thomas DL, Shao X, et al. Measurement of blood-brain barrier water exchange rate using diffusion-prepared and multi-echo arterial spin labelling: Comparison of quantitative values and age dependence. *NMR in Biomedicine*. 2024;37(12):e5256.
   - https://doi.org/10.1002/nbm.5256
3. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
4. Bell RD, Winkler EA, Sagare AP, et al. Pericytes control key neurovascular functions and neuronal phenotype in the adult brain and during brain aging. *Neuron*. 2010;68(3):409-427.
   - https://doi.org/10.1016/j.neuron.2010.09.043
5. Kisler K, Nikolakopoulou AM, Sweeney MD, et al. Acute ablation of cortical pericytes leads to rapid neurovascular uncoupling. *Frontiers in Cellular Neuroscience*. 2020;14:27.
   - https://doi.org/10.3389/fncel.2020.00027
6. Pandey K, Bessières B, Sheng SL, et al. Neuronal activity drives IGF2 expression from pericytes to form long-term memory. *Neuron*. 2023;111(23):3819-3836.e8.
   - https://doi.org/10.1016/j.neuron.2023.08.030
7. Swissa E, Monsonego U, Yang LT, et al. Cortical plasticity is associated with blood-brain barrier modulation. *eLife*. 2024;12:RP89611.
   - https://doi.org/10.7554/eLife.89611
8. Mai-Morente S, Razvan M, Lechuga-Sancho AM, et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nature Communications*. 2025;16:5912.
   - https://doi.org/10.1038/s41467-025-61312-0
