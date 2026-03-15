# Site Deepening Audit (2026-03-14, Perspective / Consciousness Markers)

## 対象

- 主対象: `perspective.md`

## 今回の選定理由

- 2026-03-14 時点で、`Perspective` の `EEGで意識を測る` 節は、サイト全体の中でもっとも読者に将来像を強く印象づける箇所でした。
- しかし、`PCI / PCI-ST`、`no-report paradigms`、`安静時複雑性`、`臨界性`、`multimodal clinical validation` が、証拠強度の差を十分に見せないまま並んでいました。
- その結果、一次文献がまだ支持していない `単独の意識メータ`、`臨界性からの統一説明`、`単一路線への収束` を読者が期待しやすい構造が残っていました。

## 主要な批判点

### 1. Cogitate / adversarial collaboration の読み方が強すぎました

- 問題:
  - 旧版は、2025年の adversarial collaboration を、`IIT/GNWT 統合の撤回` と `FEP/予測符号化への転換` にほぼ直結させていました。
  - しかし Ferrante et al. (2025) が示したのは、単一理論の勝利ではなく、複数理論の主要予測が部分的に支持されつつ、鍵予測のいくつかが反証された、という結果です。
  - また同論文は、意識内容候補マーカーと task relevance / report requirement のマーカーが分かれることも示しており、理論移行より先に confound control を固定すべきことを示しています。
- 修正:
  - `理論を採択する` 書き方をやめ、`理論を事前登録された予測集合として競わせる` 立場へ改めました。
  - FEP / 予測符号化も `既定路線` ではなく `候補モデル族` へ下げました。

### 2. `no-report` と `PCI` と `resting-state metrics` が同列に見えていました

- 問題:
  - 旧版は、`行動非依存の意識指標` として PCI、no-report、臨界性をほぼ同格に読める構造でした。
  - しかし技術的には、no-report は readout ではなく confound control、PCI/PCI-ST は perturbation benchmark、安静時複雑性・臨界性は補助 proxy 候補です。
  - この差を曖昧にすると、`安静時 EEG だけで十分` という誤読を誘発します。
- 根拠:
  - Tsuchiya et al. (2015) は no-report paradigms を NCC 抽出の設計として整理しています。
  - Cohen et al. (2024) は visual awareness で、Dellert et al. (2025) は auditory no-report fMRI で、no-report 条件が post-perceptual processing の切り分けに有効であることを示しました。
  - Casali et al. (2013) と Comolatti et al. (2019) は PCI / PCI-ST を state-level benchmark として前進させましたが、Hernandez-Pavon et al. (2023) は TMS-EEG の刺激条件・マスキング・アーチファクト管理が比較可能性の前提だと明示しています。
- 修正:
  - `site rule` として、`no-report = confound control`、`PCI/PCI-ST = 主 benchmark 候補`、`安静時複雑性・臨界性 = 補助 / 探索トラック` を明記しました。
  - `証拠強度の違う4トラック` 表を追加し、読者が強さの差を表で読めるようにしました。

### 3. `臨界性からの統一説明` は、一次文献の強さより一段先へ進みすぎていました

- 問題:
  - 旧版は、安静時 EEG の臨界性指標から `侵襲なしの意識評価` や `統一説明` へ比較的滑らかにつなげていました。
  - しかし、Maschke et al. (2024) が示すのは麻酔誘導下の cohort での関連であり、広範な病態・装置・施設をまたぐ一般解ではありません。
  - さらに Casarotto et al. (2024) は、MCS で spontaneous EEG marker と evoked EEG marker が解離しうることを示しており、安静時 proxy を PCI 代替とみなすのは危険です。
- 修正:
  - フェーズ2を `安静時 proxy の較正` へ変更し、`摂動なしで十分` という読みを止めました。
  - `proxy としてどこまで使えるかを外部較正する` という目的へ縮退させました。

### 4. 終盤のインパクト記述が科学ページとして過大でした

- 問題:
  - 旧版には `ノーベル級のインパクト`、`世界標準の意識指標` という表現がありました。
  - これは研究計画の気概としては理解できても、一次文献の強さを伝える科学ページとしては過大で、読者の期待を誤誘導します。
- 根拠:
  - Ferreiro et al. (2025) は、DoC の診断 / 予後は multimodal・multicentre の統合で前進しうることを示していますが、単独で universal standard となる 1 指標を提示したわけではありません。
- 修正:
  - `単独意識メータ` の宣言を撤回し、`事前登録・外部妥当化・校正・棄権を含む公開 benchmark を積み上げる` という到達目標へ変更しました。

## 今回実行した変更

- `perspective.md`
  - `Adversarial Collaboration` の解釈を、`理論の勝敗` から `prediction competition` へ修正
  - `FEP / 予測符号化` の位置づけを `候補モデル族` へ変更
  - `EEGで意識を測る` 節を全面改稿し、`PCI / no-report / resting-state metrics / multimodal validation` の証拠強度を分離
  - `臨界性からの統一説明` と `世界標準 / ノーベル級` の誇張表現を撤回
  - 2024-2025 の一次文献 4 本を参考文献へ追加

## 外部依存で保留

- TMS-EEG / no-report / multimodal validation を同一 cohort で回す実験系の実装
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: IRB、TMS-EEG 機材、no-report 課題実装、臨床協力体制
  - 完了条件: 同一 cohort で perturbation benchmark と spontaneous proxy を比較できる公開ログがそろうこと

## 参考文献

- Ferrante O, et al. Adversarial testing of global neuronal workspace and integrated information theories of consciousness. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08888-1
- Tsuchiya N, et al. No-Report Paradigms: Extracting the True Neural Correlates of Consciousness. Trends Cogn Sci. 2015.
  - https://doi.org/10.1016/j.tics.2015.10.002
- Cohen MA, et al. Neural signatures of visual awareness independent of postperceptual processing. Cereb Cortex. 2024.
  - https://doi.org/10.1093/cercor/bhae415
- Dellert T, et al. Neural correlates of consciousness in an auditory no-report fMRI study. Curr Biol. 2025.
  - https://doi.org/10.1016/j.cub.2025.10.026
- Casali AG, et al. A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med. 2013.
  - https://doi.org/10.1126/scitranslmed.3006294
- Comolatti R, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. Brain Stimul. 2019.
  - https://doi.org/10.1016/j.brs.2019.05.013
- Hernandez-Pavon JC, et al. TMS combined with EEG: Recommendations and open issues. Brain Stimul. 2023.
  - https://doi.org/10.1016/j.brs.2023.02.009
- Schartner M, et al. Complexity of multi-dimensional spontaneous EEG decreases during propofol induced general anaesthesia. PLoS One. 2015.
  - https://doi.org/10.1371/journal.pone.0133532
- Maschke C, et al. Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity. Commun Biol. 2024.
  - https://doi.org/10.1038/s42003-024-06613-8
- Shew WL, Plenz D. The functional benefits of criticality in the cortex. Neuroscientist. 2013.
  - https://doi.org/10.1177/1073858412445487
- Casarotto S, et al. Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state. Eur J Neurosci. 2024.
  - https://doi.org/10.1111/ejn.16299
- Manasova D, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. Brain. 2026.
  - https://doi.org/10.1093/brain/awaf412
