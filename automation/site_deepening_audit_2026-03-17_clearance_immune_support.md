# Site Deepening Audit (2026-03-17, Clearance / Immune Support as a Distinct Maintenance-State)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-17 時点で、公開サイトは `connectome-complete ≠ emulation-complete`、`same-day fit ≠ cross-day maintenance`、`human proxy ≠ local ground truth` をかなり強く整理できていました。
- その一方で、`clearance / immune support` はなお `glial / metabolic support` の中へ半ば吸収されており、`meningeal lymphatics / CSF-interstitial exchange / microglia-mediated support` が独立の maintenance-state としては十分に前面化されていませんでした。
- この弱点は技術・自然科学の観点で優先度が高いです。なぜなら、現在の一次文献が比較的強く示しているのは、`clearance` が単なる掃除の比喩ではなく、`multiday support-state` として synaptic physiology や recovery ceiling に関わるという点であり、同時に human 側では `macro support proxy` に留まるという二重の境界だからです。

## 根拠付き批判

### 1. 旧サイトは `glial / metabolic support` と `clearance / immune support` を十分に分けていませんでした

- 問題:
  - astrocyte ensemble、lactate transport、metabolic support は厚く記述されていましたが、meningeal lymphatics、CSF mobility、glymphatic route、microglia-mediated support が独立の state class としては薄く、読者が `glia を書いていれば clearance もほぼ含まれる` と誤読しうる構造が残っていました。
- 根拠:
  - Louveau et al. (2015) は CNS lymphatic vessels の構造と機能を示しました。
  - Kim et al. (2025) は meningeal lymphatics-microglia axis が synaptic physiology を調整することを示しました。
- 批判:
  - したがって、`astrocyte / metabolic support` と `clearance / immune support` は同一行へ畳み込まず、少なくとも site rule 上は別軸として扱う必要があります。

### 2. 旧 human observability 導線は `CSF / glymphatic proxy` を明示しておらず、support-state の観測層差が見えにくかった

- 問題:
  - human 側では EM、MRSI、myelin、TMS-state proxy は見え始めていましたが、CSF mobility や glymphatic clearance がどの層を押し上げるのかが本文導線に固定されていませんでした。
  - このままでは、読者が `human では clearance はまだ全く見えていない` か、逆に `human で glymphatic が見えたので local immune controller もかなり見えた` と両方向に誤読しやすい状態でした。
- 根拠:
  - Eide & Ringstad (2021) は sleep deprivation が molecular clearance を阻害することを示しました。
  - Hirschler et al. (2025) は MRI で region-specific な CSF mobility driver を示しました。
  - Dagum et al. (2026) は human で glymphatic route に沿った amyloid-beta / tau clearance を示しました。
- 批判:
  - これらが直接押し上げるのは `macro support-state proxy` であって、`moment-to-moment neural truth` や `cell-specific immune controller` ではありません。したがって、proxy class を独立に明示する必要があります。

### 3. Verification 側に `clearance / immune support` の独立行が無く、棄権条件が曖昧でした

- 問題:
  - `latent-state error budget` には glial / slow-state support はありましたが、clearance / immune support の欄がなく、multiday recovery や protein-clearance を含む claim をどこで止めるかが曖昧でした。
- 批判:
  - 提出物仕様に独立行が無いままでは、`sleep / wake annotation`、`CSF mobility proxy`、`immune / meningeal covariate` を出していない結果でも、multiday support-state claim を曖昧に延長できてしまいます。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `7つの maintenance-state` へ改稿し、`clearance / immune support` を追加
  - `clearance / immune support は passive cleanup ではありません` 節を新設
  - human observability table に `human CSF / glymphatic proxy` 行を追加
  - site rules と提出物 table に `clearance / immune support` を追加
- `wbe_101.md`
  - hidden-state evidence table に `clearance / immune support` 行を追加
  - `human direct observability ceiling` 行を `CSF-glymphatic support proxy` まで拡張
  - hidden state table に `clearance / immune support` 行を追加
- `wiki/connectome-is-not-enough.md`
  - `7つの状態クラス` へ改稿し、bottom-line table と timescale matrix に `clearance / immune support` 行を追加
  - abstract / known points / note を support-state 読みへ同期
- `verification.md`
  - `latent-state error budget` に `clearance / immune support` 行を追加
  - `clearance / immune proxy は momentary neural truth ではありません` note を追加

## 外部依存で保留

- なし
  - 今回の修正は、公開本文と提出物仕様の改稿で完結しています。

## 参考文献

1. Louveau A, Smirnov I, Keyes TJ, et al. Structural and functional features of central nervous system lymphatic vessels. *Nature*. 2015.
   - https://doi.org/10.1038/nature14432
2. Kim J, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
   - https://doi.org/10.1016/j.cell.2025.02.022
3. Eide PK, Ringstad G. Sleep deprivation impairs molecular clearance from the human brain. *Brain*. 2021.
   - https://doi.org/10.1093/brain/awab285
4. Hirschler L, et al. Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
5. Dagum P, et al. The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
