# Site Deepening Audit (2026-03-16, Multimodal Integration / Alignment and Validation)

## 対象

- 主対象: `wiki/multimodal-integration-basics.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 2026-03-16 時点で、サイトは `multimodal` が有用であること自体は正しく説明できていました。
- しかし、技術・自然科学の観点で見ると、`multimodal` の中に少なくとも 4 種類のまったく異なる前進が混ざっていました。
  - 同時取得 + 共有時計
  - 同一個体だが非同時の幾何統合
  - coverage-limited な侵襲校正
  - atlas / Patch-seq / same-brain local twin による prior 付与
- これは重大です。なぜなら、これらは全部「複数モダリティ」ですが、直接追加される証拠が違い、したがって許される主張の強さも違うからです。

## 主要な批判点

### 1. 旧ページは `multimodal` を一つの種類として扱いすぎていました

- 問題:
  - 旧版は EEG+fMRI、EEG+MEG、EEG+侵襲記録を並べていましたが、`何が直接増えたか` を acquisition relation 単位で切れていませんでした。
  - そのため、読者が `atlas を足した`、`同一個体 MRI を足した`、`同時計測した`、`侵襲校正した` を、同じ種類の前進として読める余地が残っていました。
- 根拠:
  - Pernet et al. (2019) は EEG-BIDS が modality-specific metadata を必要とすることを示しました。
  - Kothe et al. (2025) は LSL が synchronized multimodal recording に有効でも、device-side delay や display latency の真値までは自動で与えないことを示しました。
  - Burns et al. (2024) は Motion-BIDS により、motion 系 metadata を別 schema で保持しないと multimodal reuse が崩れることを示しました。
- 修正:
  - `wiki/multimodal-integration-basics.md` を、`同時取得`、`幾何統合`、`侵襲校正`、`atlas / bridge / prior` の 4 系統へ再編しました。
  - `eeg_101.md` の統合節も同じ分類へ更新し、入口段階で誤読を止めるよう改稿しました。

### 2. 旧ページは fused map を「直接見えた情報」に近く読ませる危険が残っていました

- 問題:
  - 旧版は multimodal の有効性を述べていましたが、fusion output が `raw truth` ではなく `モデル + prior + co-registration を通した推定` であることを十分に前面化できていませんでした。
- 根拠:
  - Wei et al. (2020) は Bayesian fusion / multimodal DCM が共有 latent model を明示して初めて EEG と fMRI を結び付けることを示しました。
  - Aydin et al. (2014) は EEG+MEG の改善が calibrated realistic volume conductor model に依存することを示しました。
- 修正:
  - `wiki/multimodal-integration-basics.md` に `融合後の地図は、直接観測ではなく推定です` 節を追加しました。
  - `Fusion Card` を新設し、fusion model、registration error、不確実性、raw retention を必須項目へ格上げしました。

### 3. 旧ページは侵襲校正を強い validation route と述べつつ、coverage boundary を十分に固定していませんでした

- 問題:
  - 旧版は EEG+侵襲記録を calibration route として正しく紹介していましたが、読者がそれを `whole-brain ground truth` に近いものとして読む余地が残っていました。
- 根拠:
  - Mikulan et al. (2020) は intracerebral stimulation + HD-EEG の ground-truth dataset を公開しました。
  - Unnwongse et al. (2023) は intracranial electric stimulation による direct validation を示しました。
  - しかし、どちらも implanted / stimulated site 周辺での妥当化であり、全脳の一般的一意復元を与えるものではありません。
- 修正:
  - `wiki/multimodal-integration-basics.md` の route table と site rule に、`coverage-limited validation` であることを明記しました。
  - `eeg_101.md` でも、侵襲校正を `局所妥当化` として短く固定しました。

### 4. 旧ページは atlas / same-brain local twin / transcriptomic bridge を、同じ強さの「統合」として並べていました

- 問題:
  - 旧版は atlas や same-brain structure-function link の価値を説明していましたが、`current state を直接観測したことにはならない` 境界をまだ十分に強く打ち出せていませんでした。
- 根拠:
  - Yao et al. (2023) は whole-mouse-brain の transcriptomic / spatial atlas を提示しましたが、これは identity prior と spatial prior を強くする前進です。
  - MICrONS Consortium et al. (2025) は same-brain local structure-function link を押し上げましたが、human whole-brain state-complete ではありません。
  - Gamlin et al. (2025) は predicted transcriptomic type と connectomics の橋渡しを示しましたが、これも current synaptic state そのものではありません。
- 修正:
  - `wiki/multimodal-integration-basics.md` に `atlas / bridge / prior 付与` を独立行として新設しました。
  - site rule を `atlas / Patch-seq / transcriptomics は prior と書く` へ更新しました。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - `last_updated` を 2026-03-16 に更新
  - `multimodal` を 4 種類の acquisition relation へ分解
  - `6 つの監査ゲート` を新設
  - `Fusion Card` を追加し、取得関係、共有時計、幾何、fusion model、不確実性、external validator、coverage boundary を提出物化
  - 参考文献を EEG-BIDS / LSL / Motion-BIDS / Bayesian fusion / direct validation / MICrONS / atlas 系へ更新
- `eeg_101.md`
  - `last_updated` を 2026-03-16 に更新
  - multimodal 節を acquisition relation ベースに改稿
  - `Fusion Card` の短い説明を追加
  - 参照リンクに LSL / Motion-BIDS / Wei / Mikulan / Wirsich / Yao / MICrONS / Gamlin を追加

## 外部依存で保留

- Fusion Card を site-wide schema として全ページへ展開
  - 担当者: AI / maintainer
  - 前提条件: `verification.md` の提出物テンプレ群と整合する共通見出しを決めること
  - 完了条件: Datasets / Verification / Wiki の関連ページで、multimodal 結果に同じ card schema を使えること
- 実データつき multimodal benchmark の追加
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: raw per modality、clock validation、registration error、external validator を含む公開データまたは再配布可能な metadata があること
  - 完了条件: same-subject geometry prior、simultaneous recording、coverage-limited validation、atlas prior を別 benchmark family として比較できること

## 参考文献

- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Sci Data*. 2019;6:103.
  - https://doi.org/10.1038/s41597-019-0104-8
- Kothe C, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neurosci*. 2025;3:IMAG.a.136.
  - https://doi.org/10.1162/imag.a.136
- Burns M, Nii L, Williams AN, et al. Motion-BIDS: extending BIDS to support standardized storage of motion data. *Sci Data*. 2024;11:857.
  - https://doi.org/10.1038/s41597-024-03559-8
- Wei H, Jafarian A, Zeidman P, et al. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
  - https://doi.org/10.1016/j.neuroimage.2019.116595
- Jorge J, Grouiller F, Ipek O, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. *NeuroImage*. 2015;105:132-144.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021;231:117864.
  - https://doi.org/10.1016/j.neuroimage.2021.117864
- Aydin U, Vorwerk J, Kupper P, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. *PLoS One*. 2014;9(3):e93154.
  - https://doi.org/10.1371/journal.pone.0093154
- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Sci Data*. 2020;7:127.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Commun*. 2023;5(2):fcad023.
  - https://doi.org/10.1093/braincomms/fcad023
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;638:425-435.
  - https://doi.org/10.1038/s41586-025-08790-w
- Yao Z, van Velthoven CTJ, Nguyen TN, et al. A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. *Nature*. 2023;624:317-332.
  - https://doi.org/10.1038/s41586-023-06812-z
- Gamlin CR, et al. Connectomics of predicted Sst transcriptomic types in mouse visual cortex. *Nature*. 2025;638:316-324.
  - https://doi.org/10.1038/s41586-025-08805-6
