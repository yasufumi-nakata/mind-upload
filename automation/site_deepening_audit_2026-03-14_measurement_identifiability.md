# Site Deepening Audit (2026-03-14, Measurement / Identifiability)

## 対象

- 主対象: `tech_roadmap.md`
- 副対象: `wiki/eeg-basics.md`

## 今回の選定理由

- 2026-03-14 時点で、公開サイトの `verification` と `wbe_101` は同日にかなり深く更新されていました。一方で、`tech_roadmap` と `wiki/eeg-basics` には、技術・自然科学の観点でまだ弱い箇所が残っていました。
- 弱点は、EEG/マルチモーダル計測について「観測できる」「相関や予測が出る」「内部状態が十分に同定できる」が、本文上はまだ十分に切り分けられていなかった点です。
- この曖昧さは WBE 議論では重大です。なぜなら、source imaging の改良や同時計測の成功は、しばしば `見えた` と `一意に分かった` を混同させるからです。

## 主要な批判点

### 1. `tech_roadmap.md` の計測節は、observability と identifiability の境界がまだ甘かった

- 問題:
  - M1 は「観測変数が違えば復元対象が変わる」と正しく述べていましたが、どのモダリティが何を直接観測し、何を依然として latent のまま残すかが表で固定されていませんでした。
  - そのため、EEG/MEG/fMRI/ECoG/SEEG/connectomics を並べて読んだときに、マルチモーダル統合を「欠けた状態変数の解消」と過大解釈しやすい構造が残っていました。
- 根拠:
  - Mikulan et al. (2020) は intracranial stimulation + HD-EEG の ground-truth dataset を提供し、source localization は外部基準つきで監査すべき問題だと示しました。
  - Seeber et al. (2019) は 256ch scalp EEG で subcortical activity が条件付きで detect できることを示しましたが、一般的一意復元は主張していません。
  - Unnwongse et al. (2023) は intracranial stimulation を用いた直接妥当化で、localization error が conductivity 仮定と source depth に依存することを示しました。
  - Hao et al. (2025) は simultaneous HD-EEG/SEEG の 29 例で、source power と source depth が ESI 精度を大きく左右すると報告しました。
  - Dorkenwald et al. (2024)、MICrONS Consortium et al. (2025)、Gamlin et al. (2025)、Cahill et al. (2024) は、構造と局所機能を同じ脳で結びつけても、cell-type / neuromodulatory / glial state がなお別変数として残ることを補強しています。
- 修正:
  - `tech_roadmap.md` の M1 に、`観測路線 / 直接観測 / 強く言えること / 残る潜在状態` の観測可能性マトリクスを追加しました。
  - M1 の注記として、「multimodal は state completeness の達成ではない」ことを一次文献名つきで明示しました。

### 2. `tech_roadmap.md` の R7 は同定可能性を一般論で述べていたが、直接妥当化文献の含意が薄かった

- 問題:
  - R7 は感度分析、family comparison、棄権条件の必要性を述べていましたが、読者が「なぜそこまで厳しく書くのか」を、直接妥当化研究から結びつけにくい構造でした。
  - その結果、cross-modal 相関や held-out 予測を、そのまま唯一解に近い同定として誤読する余地がありました。
- 根拠:
  - Seeber et al. (2019) は detectability を示しましたが、source identifiability の一般解ではありません。
  - Unnwongse et al. (2023) は direct validation の条件でも localization error が cm オーダーで残ることを示しました。
  - Hao et al. (2025) は simultaneous HD-EEG/SEEG で、誤差が source depth と source power に強く依存することを報告しました。
- 修正:
  - `tech_roadmap.md` の R7 に、「相関・予測・同定を同じ強さで扱わない」注記を追加しました。
  - `predictability の上昇` と `内部状態の唯一解` を分けて読む運用ルールを本文へ埋め込みました。

### 3. `wiki/eeg-basics.md` は入門としては読みやすいが、2026-03 時点の妥当化文献を反映できていなかった

- 問題:
  - 初学者向けに簡潔である一方、「EEG は混ざった信号」という説明から先に進んだときに、どこまでが観測で、どこからが条件付き推定で、どこからが外部妥当化の問題なのかが見えませんでした。
  - 参考文献節もなく、公開サイト内のより厳密な議論へ戻る導線が弱い状態でした。
- 根拠:
  - Mikulan et al. (2020) が public benchmark を出したことで、source localization を ground-truth 付きで監査する最小線がかなり具体化しました。
  - Unnwongse et al. (2023) と Hao et al. (2025) により、direct validation と simultaneous HD-EEG/SEEG の結果を beginner page にも最低限反映すべき段階へ来ています。
- 修正:
  - `wiki/eeg-basics.md` に `観測・推定・同定は別です` 節を追加し、EEG の説明を 3 段階に分けました。
  - `2026-03 の実測エビデンス` 注記を追加し、Seeber / Unnwongse / Hao の含意を初心者向けに簡潔化しました。
  - 参考文献節と関連導線を追加し、`measurement-and-modeling-terms` へ戻れるようにしました。

## 今回実行した変更

- `tech_roadmap.md`
  - M1 に観測可能性マトリクスを追加
  - M1 に `multimodal ≠ state completeness` の注記を追加
  - R7 に `predictability ≠ identifiability` の注記を追加
  - 参考文献に Seeber (2019)、Dorkenwald (2024)、MICrONS (2025)、Gamlin (2025)、Cahill (2024) を追加
- `wiki/eeg-basics.md`
  - `観測・推定・同定は別です` 節を新設
  - direct validation 文献に基づく 2026-03 注記を追加
  - 参考文献節と関連リンクを追加

## 外部依存で保留

- source imaging benchmark の実装・継続監視
  - 担当者: AI / maintainer
  - 前提条件: Localize-MI、同時 HD-EEG/SEEG、intracranial stimulation 系データの継続的な取得・整備
  - 完了条件: site 上の `direct validation` 論点を、実データで再現できる公開ベンチへ落とし込むこと

## 参考文献

- Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. Scientific Data. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nature Communications. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. Brain Communications. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, Alhilani M, Asano E, et al. High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Dorkenwald S, McKellar CE, Macrina T, et al. Neuronal wiring diagram of an adult brain. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07558-y
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-08805-6
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
