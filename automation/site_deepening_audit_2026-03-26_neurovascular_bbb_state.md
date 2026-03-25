# Site Deepening Audit (2026-03-26, Neurovascular-Unit / BBB / Pericyte State)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `index.md`
- 副対象: `faq.md`
- 副対象: `wbe_101.md`
- 副対象: `glossary.md`
- 副対象: `perspective.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-26 時点の公開サイトは、measurement-side の `vascular-state / CVR audit` をかなり強く整理できていました。
- 一方で maintenance-side では、`clearance / immune support`、`astrocyte-state`、`bioenergetic state` などは明示されていても、`neurovascular-unit / BBB / pericyte state` が独立 family としてはまだ弱く、読者が `vascular confound を監査した = relevant vascular biology も押さえた` と誤読しうる余地が残っていました。
- これは技術・自然科学の観点で優先度が高いです。なぜなら、一次文献が示しているのは、pericyte / endothelial / BBB biology が単なる hemodynamic nuisance ではなく、capillary support、plasticity、long-term memory、および human BBB permeability proxy の ceiling を別々に規定するという点だからです。

## 根拠付き批判

### 1. `vascular-state / CVR audit` と `neurovascular-unit / BBB / pericyte state` は同じ問いではありません

- 問題:
  - 旧サイトは BOLD / fNIRS などの hemodynamic modality について、measurement-side の transfer audit をかなり丁寧に整理していました。
  - しかし、その強さの反面で、読者が `vascular audit を通したなら neurovascular biology も十分扱った` と短絡できる余地が残っていました。
- 根拠:
  - [Bell et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.043) は adult brain において pericyte deficiency が cerebral blood flow、blood-brain barrier integrity、secondary neuronal change に関わることを示しました。
  - [Kisler et al. (2020)](https://doi.org/10.3389/fncel.2020.00027) は cortical pericyte ablation が rapid neurovascular uncoupling を起こすことを示しました。
  - [Mai-Morente et al. (2025)](https://doi.org/10.1038/s41467-025-61312-0) は pericyte Panx1 route が capillary diameter control と memory function に関与することを示しました。
- 批判:
  - したがって、`vascular-state / CVR audit` は measurement transfer の監査であり、`neurovascular-unit / BBB / pericyte state` は maintenance-side controller family です。両者を同じ欄で済ませるのは科学的に粗いです。

### 2. Pericyte / BBB biology は clearance や generic support に吸収してはいけません

- 問題:
  - 旧サイトには `clearance / immune support` と `astrocyte-state` があり、vascular-support biology をそこへ吸収して読めてしまう構造が一部残っていました。
- 根拠:
  - [Pandey et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.030) は neuronal activity に応答した pericyte-derived IGF2 signal が long-term memory formation に関わることを示しました。
  - [Swissa et al. (2024)](https://doi.org/10.7554/eLife.89611) は cortical plasticity と blood-brain barrier modulation の連動を示しました。
- 批判:
  - これらは `clearance がある`、`astrocyte がある` という一般論では代替できません。pericyte / endothelial / BBB route は、それ自体が別の hidden-state family です。

### 3. Human evidence でも観測 ceiling は独立です

- 問題:
  - 旧サイトは human support-state proxy を拡張していましたが、BBB permeability / water exchange route が `macro support evidence` に吸収されやすいままでした。
- 根拠:
  - [Padrela et al. (2025)](https://doi.org/10.1016/j.neurobiolaging.2024.12.012) は multi-echo ASL により adult lifespan にわたる BBB water permeability を扱いました。
  - [Chung et al. (2025)](https://doi.org/10.1038/s41467-025-58356-7) は quantitative PET imaging と kinetic modeling による molecular BBB permeability route を示しました。
- 批判:
  - これらは important な human observability advance ですが、なお macro permeability / exchange proxy です。cell-specific pericyte controller や full neurovascular maintenance state の direct readout ではありません。したがって、human proxy table に独立 row と calibrator-role 記述が必要でした。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - maintenance-state family count を 17 から 18 へ更新
  - `neurovascular-unit / BBB / pericyte state` を独立 family として front matter、summary table、human proxy table に追加
  - `vascular-state / CVR audit` とは別物であることを明示する新規 section と route card を追加
  - human observability の ceiling を `macro BBB permeability / water-exchange proxy` として明記
  - Bell / Kisler / Pandey / Swissa / Mai-Morente / Padrela / Chung を参考文献へ追加
- `index.md`
  - front-door summary に `neurovascular-unit / BBB / pericyte state` を追加
  - `vascular audit を通した = maintenance-side vascular biology も解決した` という誤読を止める note を追加
- `faq.md`
  - Q2c に neurovascular / BBB / pericyte family の独立性を追加
- `wbe_101.md`
  - human observability ladder に BBB permeability / water-exchange proxy row を追加
  - `human proxy composition` ではなく `maintenance-state family split` の話でもあることを補強
- `glossary.md`
  - `Vascular-state / CVR audit` を measurement-side と明記
  - `Neurovascular-unit / BBB / pericyte state` の独立項目を新設
- `perspective.md`
  - perspective page の hidden-state family count と human ceiling discussion を更新
- `verification.md`
  - state-completeness gate に neurovascular / BBB / pericyte state を追加
  - `vascular transfer audit is not neurovascular support-state audit` という addendum を追加

## 外部依存で保留

- なし
  - 今回の変更は、公開本文・要約・検証ページ・用語集の改稿で完結しています。

## 参考文献

1. Bell RD, Winkler EA, Sagare AP, et al. Pericytes control key neurovascular functions and neuronal phenotype in the adult brain and during brain aging. *Neuron*. 2010;68(3):409-427.
   - https://doi.org/10.1016/j.neuron.2010.09.043
2. Kisler K, Nikolakopoulou AM, Sweeney MD, et al. Acute ablation of cortical pericytes leads to rapid neurovascular uncoupling. *Frontiers in Cellular Neuroscience*. 2020;14:27.
   - https://doi.org/10.3389/fncel.2020.00027
3. Pandey K, Bessières B, Sheng SL, et al. Neuronal activity drives IGF2 expression from pericytes to form long-term memory. *Neuron*. 2023;111(23):3819-3836.e8.
   - https://doi.org/10.1016/j.neuron.2023.08.030
4. Swissa E, Monsonego U, Yang LT, et al. Cortical plasticity is associated with blood-brain barrier modulation. *eLife*. 2024.
   - https://doi.org/10.7554/eLife.89611
5. Mai-Morente S, Razvan M, Lechuga-Sancho AM, et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nature Communications*. 2025;16:5912.
   - https://doi.org/10.1038/s41467-025-61312-0
6. Padrela BE, Slivka M, Sneve MH, et al. Blood-brain barrier water permeability across the adult lifespan: A multi-echo ASL study. *Neurobiology of Aging*. 2025;147:176-186.
   - https://doi.org/10.1016/j.neurobiolaging.2024.12.012
7. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025;16:3076.
   - https://doi.org/10.1038/s41467-025-58356-7
