# Site Deepening Audit (2026-03-16, Neuromodulatory PET / Occupancy / Release Proxy Routes)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-16 時点で、公開サイトは neuromodulation を `mixed arousal proxy / axon activity / local transmitter sensor / receptor atlas / pharmacology` の階段としてかなり明確に扱えていました。
- ただし、人で使える receptor-related route の中でも
  - `receptor atlas / autoradiography`
  - `drug occupancy PET`
  - `release-sensitive displacement PET`
  が、まだ 1 本の `receptor atlas / PET / autoradiography` に束ねられていました。
- この粗さは技術・自然科学の観点で重要でございます。なぜなら、これらはどれも receptor を見る経路ですが、直接増える情報が違い、許される claim ceiling も違うからです。

## 主要な批判点

### 1. 旧記述は `static receptor prior` と `dynamic PET proxy` を同じ段に置いていました

- 問題:
  - 旧 `measurement-stack` では `receptor atlas / PET / autoradiography` が 1 行でした。
  - しかし、atlas / autoradiography が与えるのは主として `どこで receptor density が高いか` という地域・層の prior であり、occupancy / displacement PET が与えるのは `選んだ ligand / challenge 下での target engagement または release proxy` です。
- 根拠:
  - Hansen et al. (2022) は human neocortex における複数 neurotransmitter system map を統合し、構造・機能軸との対応を示しました。
  - Goulas et al. (2021) は human cortex の receptor distribution に自然軸があることを示しました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` で `receptor atlas / autoradiography` を独立行へ分け、PET 行を別に新設しました。

### 2. 旧記述は `PET = current neuromodulatory state` と誤読される余地を残していました

- 問題:
  - 旧版には PET の route がありましたが、PET が `ligand-specific`、`receptor-family-specific`、`challenge-dependent` な proxy であることが十分に前面化されていませんでした。
- 根拠:
  - Wong et al. (2013) は healthy subject で lurasidone の D2 receptor occupancy を dose-dependent target engagement として測定しました。
  - Koepp et al. (1998) は raclopride displacement による striatal dopamine release proxy を示しました。
  - Lippert et al. (2019) は dynamic PET により stimulus-evoked regional dopamine release を time-dependent に評価しました。
- 批判:
  - したがって PET は `momentary whole-brain transmitter field` ではなく、`選んだ receptor 系と kinetic / displacement model の下での regional occupancy / release proxy` として読む必要があります。

### 3. 既存の latent-state error budget では PET 系の必須欄が足りませんでした

- 問題:
  - `verification.md` の neuromodulatory 行は `compartment / spatial scope / receptor family` を要求していましたが、PET 系でさらに必要な `ligand / challenge / temporal window` がありませんでした。
- 修正:
  - `verification.md` に `ligand / challenge` と `temporal window` を追加し、PET 系結果を `occupancy PET` と `displacement PET` に分けて監査する運用へ更新しました。

### 4. 書誌情報に誤りがありました

- 問題:
  - 旧 `measurement-stack` は Goulas 論文を `2023 / Neuron / 10.1016/j.neuron.2023.02.013` として引用していました。
  - しかし、`The natural axis of transmitter receptor distribution in the human cerebral cortex` の正しい書誌は `2021 / PNAS / 10.1073/pnas.2020574118` です。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` と対応する export / audit を訂正しました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - neuromodulatory ladder を `receptor atlas / autoradiography` と `occupancy / release-sensitive PET` に分割
  - human PET が何を直接与え、何をまだ与えないかを明文化
  - site rule に `occupancy PET / displacement PET` を明記
  - Goulas citation を訂正
  - Wong (2013), Koepp (1998), Lippert (2019) を追加
- `verification.md`
  - neuromodulatory specificity 行へ `ligand / challenge` と `temporal window` を追加
  - explanatory note を atlas / occupancy / displacement の三分法へ更新
  - 参考文献を追加
- `tech_roadmap.md`
  - R10 を 6 段ラダーへ更新
  - human 側で `atlas / occupancy PET / release-sensitive PET` を分ける運用へ同期

## 外部依存で保留

- なし
  - 今回の修正は、このリポジトリ内の本文更新と書誌整合性修正で完結しています。

## 参考文献

1. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01186-3
2. Goulas A, Changeux J-P, Wagstyl K, Amunts K, Palomero-Gallagher N, Hilgetag CC. The natural axis of transmitter receptor distribution in the human cerebral cortex. *PNAS*. 2021.
   - https://doi.org/10.1073/pnas.2020574118
3. Wong DF, Kuwabara H, Hsu DJ, et al. D2 receptor occupancy in the brains of healthy subjects by the novel atypical antipsychotic lurasidone. *J Clin Psychiatry*. 2013.
   - https://doi.org/10.4088/JCP.12m08042
4. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998.
   - https://doi.org/10.1038/28364
5. Lippert RN, Bolding KA, Abbott LF, et al. Time-dependent assessment of stimulus-evoked regional dopamine release. *Nature Communications*. 2019.
   - https://doi.org/10.1038/s41467-019-09897-z
6. Reimer J, McGinley MJ, Liu Y, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. *Nature Communications*. 2016.
   - https://doi.org/10.1038/ncomms13289
7. Lohani S, Moberly AH, Benisty H, et al. Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. *Nature Neuroscience*. 2022.
   - https://doi.org/10.1038/s41593-022-01202-6
8. Collins L, Reddy CB, Neal S, et al. Cholinergic and noradrenergic axonal activity contains a behavioral-state signal that is coordinated across the dorsal cortex. *eLife*. 2023.
   - https://doi.org/10.7554/eLife.86800.2
9. Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. *Cell Reports*. 2024.
   - https://doi.org/10.1016/j.celrep.2024.114808
