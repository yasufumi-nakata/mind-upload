# Site Deepening Audit (2026-03-16, fMRI / BOLD Proxy Ceiling)

## 対象

- 主対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `wiki/multimodal-integration-basics.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-16 時点で、サイトは `fMRI は blood-flow proxy である` という大枠は既に正しく押さえていました。
- しかし、技術・自然科学の観点で見ると、その表現はまだ粗く、`何が proxy ceiling を作るのか` が failure mode 単位で十分に分解されていませんでした。
- 特に不足していたのは、以下の 4 点でございます。
  - BOLD が local spiking の単純な代理ではなく、population input / neurovascular coupling に強く依存すること
  - task-related / anticipatory hemodynamics が local neuronal activity と乖離しうること
  - HRF の個体差・領域差・局所差が latency / spectral interpretation を崩しうること
  - venous geometry や non-neural factor が spatial map の振幅と laminar 読みを歪めうること

## 主要な批判点

### 1. 旧記述は `fMRI = 遅い proxy` とだけ書き、proxy の壊れ方を十分に明示していませんでした

- 問題:
  - 旧版は fMRI を `血行動態 proxy` として正しく位置付けていました。
  - ただし、その一語だけでは、読者が `高い BOLD = 高い neuronal activity`、`BOLD onset 差 = neural latency 差`、`sub-mm BOLD map = 細い neural truth` と読み替える余地が残ります。
- 根拠:
  - Logothetis et al. (2001) は、BOLD が単純な multiunit output よりも LFP に強く結びつくことを示しました。
  - Lee et al. (2010) は、cell type / wiring に依存して global / local fMRI signal が変わることを示しました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` の fMRI row を、`BOLD を中心とする neurovascular proxy` として言い換えました。
  - 同ページに `fMRI / BOLD を別扱いにする理由` 節を追加し、coupling target・HRF・venous bias を表形式で固定しました。

### 2. 旧記述は task-locked haemodynamics を neuronal computation と混同しうる余地を残していました

- 問題:
  - 旧版は fMRI の遅さは書いていましたが、`task に同期した血行動態成分のすべてが stimulus-driven neural computation ではない` という点は前面に出ていませんでした。
- 根拠:
  - Sirotin & Das (2009) は、sensory cortex で local neuronal activity によって予測されない anticipatory haemodynamic signal を報告しました。
  - Cardoso et al. (2012) は、neuroimaging signal が neurally distinct な stimulus-related component と task-related component の線形和として振る舞うことを示しました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` と `wiki/multimodal-integration-basics.md` に、task / anticipatory haemodynamics を独立 failure mode として追加しました。
  - `verification.md` の Fusion Card に `hemodynamic proxy audit` 行を追加し、fMRI / fNIRS を含む統合では task-related component を別監査する仕様へ更新しました。

### 3. 旧記述は HRF の heterogeneity を提出物仕様にまで落とせていませんでした

- 問題:
  - 旧版でも `fMRI は遅い` とは書けていましたが、`遅い` だけでは不十分です。問題は遅いだけでなく、HRF の形とタイミングが subject / region / voxel で動くことです。
- 根拠:
  - Handwerker et al. (2004) は、BOLD response が被験者間・脳領域間で大きく変動し、統計解析へ影響することを示しました。
  - Bailes et al. (2023) は、resting-state fMRI signal に local hemodynamic response timing の spectral signature が残ることを示しました。
- 修正:
  - `wiki/multimodal-integration-basics.md` に `hemodynamic proxy gate` を追加し、EEG-fMRI 統合では shared clock に加えて HRF model granularity を別提出物へしました。
  - `tech_roadmap.md` の M1 と M5 に、canonical HRF だけでは latency / mechanism claim を支えない旨を追記しました。

### 4. 旧記述は venous / non-neural factor を spatial truth と分離しきれていませんでした

- 問題:
  - 旧版は multimodal と high-resolution fMRI の価値を正しく認めていましたが、読者が `細かい voxel map = 細かい neural map` と読み替える余地が残っていました。
- 根拠:
  - Kay et al. (2019) は、sub-millimeter fMRI において venous effect が data quality と interpretation を大きく左右することを示しました。
  - Kurzawski et al. (2022) は、同一被験者内でも non-neural factor が BOLD magnitude を左右することを示しました。
- 修正:
  - `wiki/measurement-stack-and-claim-ceiling.md` と `wiki/multimodal-integration-basics.md` に、venous / depth diagnostic を明示的な gate として追加しました。
  - `tech_roadmap.md` の fMRI row も、`spatial map = neural truth` と読めないように書き換えました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - fMRI row を `BOLD / neurovascular proxy` として再定義
  - `fMRI / BOLD を別扱いにする理由` 節を追加
  - coupling target / task component / HRF heterogeneity / venous bias の 4 failure mode を表形式で追加
  - fMRI を使う claim で必要な提出物を `Hemodynamic Proxy Audit` として明文化
  - 一次文献の参考文献を追加
- `wiki/multimodal-integration-basics.md`
  - simultaneous EEG-fMRI row の残る制約を拡充
  - `EEG-fMRI で追加する hemodynamic proxy gate` 節を追加
  - Fusion Card に `hemodynamic proxy audit (when fMRI / fNIRS is included)` 行を追加
  - site rule に fMRI-specific ceiling を追加
  - 一次文献の参考文献を追加
- `verification.md`
  - Fusion Card に `hemodynamic proxy audit` 行を追加
  - fMRI / fNIRS を含む multimodal result は、この監査が無ければ macro concordance までに留めるルールを追記
- `tech_roadmap.md`
  - `last_updated` を 2026-03-16 に更新
  - M1 の fMRI row を proxy ceiling ベースに改稿
  - `fMRI の proxy ceiling を 1 段厳しく読む` 補足を追加
  - M5 に EEG-fMRI / MRI 統合時の `hemodynamic proxy audit` 要件を追記
  - 参考文献を追加

## 外部依存で保留

- fMRI / fNIRS を含む dataset card の site-wide schema 統一
  - 担当者: AI / maintainer
  - 前提条件: Verification / Datasets / Wiki で card 名称と欄の語彙を揃えること
  - 完了条件: fMRI / fNIRS を使う全ページで `hemodynamic proxy audit` を同じ欄名で再利用できること
- 実データつき mechanistic validator benchmark の追加
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: simultaneous electrophysiology, calibrated BOLD, fPET, depth-specific validation のいずれかを含む公開データまたは再配布可能 metadata があること
  - 完了条件: `shared clock はあるが mechanistic validator は無い` 族と `validator あり` 族を分けて benchmark 化できること

## 参考文献

- Logothetis NK, Pauls J, Augath M, Trinath T, Oeltermann A. Neurophysiological investigation of the basis of the fMRI signal. *Nature*. 2001;412:150-157.
  - https://doi.org/10.1038/35084005
- Lee JH, Durand R, Gradinaru V, et al. Global and local fMRI signals driven by neurons defined optogenetically by type and wiring. *Nature*. 2010;465:788-792.
  - https://doi.org/10.1038/nature09108
- Sirotin YB, Das A. Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity. *Nature*. 2009;457:475-479.
  - https://doi.org/10.1038/nature07664
- Cardoso MMBM, Sirotin YB, Lima B, Glushenkova E, Das A. The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components. *Nat Neurosci*. 2012;15:1298-1306.
  - https://doi.org/10.1038/nn.3170
- Handwerker DA, Ollinger JM, D'Esposito M. Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. *NeuroImage*. 2004;21:1639-1651.
  - https://doi.org/10.1016/j.neuroimage.2003.11.029
- Bailes J, Millman R, Franklin C, et al. Resting-state fMRI signals contain spectral signatures of local hemodynamic response timing. *eLife*. 2023.
  - https://doi.org/10.7554/eLife.86453
- Kay KN, Jamison KW, Zhang RY, Uğurbil K. A critical assessment of data quality and venous effects in sub-millimeter fMRI. *NeuroImage*. 2019;189:847-869.
  - https://doi.org/10.1016/j.neuroimage.2019.02.006
- Kurzawski JW, Yablonskiy DA, Pointer R, et al. Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects. *J Neurosci*. 2022;42:7256-7266.
  - https://doi.org/10.1523/JNEUROSCI.2532-21.2022
