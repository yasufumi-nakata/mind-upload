# Site Deepening Audit (2026-03-16, Neuromodulatory Proxy Ceiling / Receptor-Specificity Ladder)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `verification.md`
- 補助対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-16 時点で、このサイトは `neuromodulation` を latent-state の一行としては扱えていました。
- ただし、技術・自然科学の観点で重要な分解である
  - `mixed arousal proxy (pupil / HRV / locomotion)`
  - `axon activity`
  - `local transmitter sensor`
  - `receptor atlas / receptor-specific physiology`
  が、まだ本文では 1 本に束ねられていました。
- この欠落は重大でございます。なぜなら、読者が `pupil が上がった`、`ACh sensor が上がった`、`receptor density が高い` を、いずれも「neuromodulatory state が直接見えた」と誤読しうるからです。

## 主要な批判点

### 1. 旧版は pupil / behavior proxy を厳しく扱っていましたが、mixed proxy だという根拠の段差がまだ前景化されていませんでした

- 問題:
  - 旧版は `pupil / HRV は coarse proxy` と書いていました。
  - しかし、それがなぜ coarse なのか、つまり `単に粗い` のではなく `adrenergic / cholinergic が混ざった state proxy` だという一次文献ベースの根拠が薄い状態でした。
- 根拠:
  - Reimer et al. (2016) は、瞳孔変動が皮質内の adrenergic と cholinergic activity の両方を追うことを示しました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` と `verification.md` に、pupil / HRV を `mixed arousal proxy` として明示しました。

### 2. 旧版は local transmitter imaging を強い route と述べていましたが、axon activity / local chemical signal / receptor effect を分けていませんでした

- 問題:
  - 旧版は Neyhart et al. (2024) を使って local ACh dynamics の価値を押さえていました。
  - しかし、`axon activity`、`sensor 近傍の local chemical signal`、`その downstream effect` が別問題であることを 1 枚で固定していませんでした。
- 根拠:
  - Lohani et al. (2022) と Collins et al. (2023) は、cortex-wide の共通信号と局所独立成分が共存することを示しました。
  - Neyhart et al. (2024) は、local ACh signal が近傍軸索からの距離と clearance kinetics に依存することを示しました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` に `neuromodulatory proxy ladder` を追加し、`mixed arousal proxy`、`axon activity`、`local transmitter sensor`、`receptor atlas / physiology` を別 route として分解しました。

### 3. 旧版は transmitter specificity を書いていましたが、receptor / layer / projection specificity が effect ceiling を作る点が弱かった

- 問題:
  - transmitter が同じなら effect も同じだと読める余地が残っていました。
- 根拠:
  - Hansen et al. (2022)、Goulas et al. (2021)、Zilles & Palomero-Gallagher (2017) は、human / macaque cortex の receptor / transporter density が領域ごと・層ごとに大きく異なることを示しました。
  - Verhoog et al. (2016) と Gulledge et al. (2024) は、同じ cholinergic drive でも layer や projection class によって effect が変わることを示しました。
- 修正:
  - `verification.md` の neuromodulatory row を `compartment`、`spatial scope`、`receptor family` を必須にする形へ改稿しました。
  - `tech_roadmap.md` の R10 も同じ階段構造に同期しました。

### 4. 旧版は receptor atlas を暗黙に stronger evidence として扱いがちでしたが、momentary release と current state をまだ十分に切っていませんでした

- 問題:
  - receptor atlas / PET / autoradiography は非常に重要ですが、その重要性は `どこで effect が変わりうるか` という prior にあります。
  - これを `今この瞬間の transmitter state` と読むのは強すぎます。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` の matrix と site rule を更新し、`receptor atlas = regional prior`、`local transmitter sensor = local chemical proxy`、`pupil = mixed arousal proxy` を分離しました。
  - `verification.md` の augmentation 行も同じ読み替え規則へ更新しました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - neuromodulation を `behavior proxy / axon activity / local chemical proxy / receptor prior / local causal calibration` の ladder に再編
  - state-variable matrix の `neuromodulatory specificity` 行を改稿
  - `local transmitter imaging / behavior-linked proxy` 行の claim ceiling を細分化
  - site rule に `compartment` 明記ルールを追加
  - 参考文献を Reimer / Lohani / Collins / Hansen / Goulas / Zilles / Verhoog / Gulledge まで補強
- `verification.md`
  - latent-state error budget の `neuromodulatory specificity` 行を `compartment / spatial scope / receptor family` 必須へ更新
  - `neuromodulatory proxy` に関する補足 note を追加
  - hidden-state table と augmentation table の neuromodulation 行を同期
  - 参考文献を追加
- `tech_roadmap.md`
  - R10 を `4 段の proxy ladder` で再定義
  - 詳細根拠への導線を `wiki/measurement-stack-and-claim-ceiling.html#neuromodulatory-proxy-ladder` へ更新

## 外部依存で保留

- なし
  - 今回の作業は、このリポジトリ内の本文更新と引用整合性修正で完結しています。

## 参考文献

1. Reimer J, McGinley MJ, Liu Y, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. *Nature Communications*. 2016.
   - https://doi.org/10.1038/ncomms13289
2. Lohani S, Moberly AH, Benisty H, et al. Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01202-6
3. Collins L, Reddy CB, Neal S, et al. Cholinergic and noradrenergic axonal activity contains a behavioral-state signal that is coordinated across the dorsal cortex. *eLife*. 2023.
   - https://doi.org/10.7554/eLife.86800.2
4. Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. *Cell Reports*. 2024.
   - https://doi.org/10.1016/j.celrep.2024.114808
5. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01186-3
6. Goulas A, Changeux J-P, Wagstyl K, et al. The natural axis of transmitter receptor distribution in the human cerebral cortex. *PNAS*. 2021.
   - https://doi.org/10.1073/pnas.2020574118
7. Zilles K, Palomero-Gallagher N. Multiple Transmitter Receptors in Regions and Layers of the Human Cerebral Cortex. *Frontiers in Neuroanatomy*. 2017.
   - https://doi.org/10.3389/fnana.2017.00078
8. Verhoog MB, Goriounova NA, Obermayer J, et al. Mechanisms underlying the rules for associative plasticity at adult human neocortical synapses. *Nature Communications*. 2016.
   - https://doi.org/10.1038/ncomms12826
9. Gulledge AT, et al. M1-type muscarinic receptors inhibit corticofugal pyramidal tract neurons to suppress layer 5 cortical output. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1455-23.2024
