# Site Deepening Audit (2026-03-17, Synaptic State Ceiling / Connectome ≠ Current Weight)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-17 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`multimodal ≠ state-complete`、`same-day fit ≠ cross-day maintenance` をかなり強く区別できていました。
- その一方で、`current synaptic efficacy / plastic history` については、なお `EM / synapse count / PSD / spine / same-brain connectomics` を見たときに、読者が「かなり current weight まで見えた」と誤読しうる余地が残っていました。
- これは技術・自然科学の観点で優先度が高い弱点です。WBE の議論では `配線がある`、`構造と機能が同一脳で対応する`、`その瞬間の effective weight / release state が分かる` が、似て見えても別の主張だからです。

## 主要な批判点

### 1. 旧サイトは `構造シナプス指標` と `その瞬間の有効結合` の境界を、まだ十分 operational にしていませんでした

- 問題:
  - `wiki/connectome-is-not-enough.md` などは、edge list だけでは `current synaptic efficacy` が落ちること自体は正しく書いていました。
  - しかし、EM synapse count、PSD 面積、spine size、same-brain connectomics が「どこまで prior を強くし、どこから先は current weight ではないか」の区切りが、まだ明示的ではありませんでした。
- 根拠:
  - Holler et al. (2021) は identified neocortical synapse で PSD 面積と平均 EPSP の関係を前進させましたが、同研究は size-strength 対応が trial-to-trial では弱いことも示しています。
  - Dürst et al. (2022) は bouton potency が主として vesicular release probability に依存することを示しました。
  - Vardalaki et al. (2022) は、成体新皮質でも filopodia が silent synapse の構造基盤になりうることを示しました。
- 批判:
  - したがって、`構造が近い`、`同一脳で対応が付いた`、`現在の有効結合が直接読めた` は同じではありません。
  - とくに `synapse count / PSD / spine` は useful ではあっても、まず `structural prior / state-averaged constraint` として扱うべきです。

### 2. 旧サイトは `same-brain function` を synaptic-state line の前進として少し強く読みすぎていました

- 問題:
  - `wiki/measurement-stack-and-claim-ceiling.md` の短い結論では、MICrONS が局所的に `synaptic efficacy / plastic history` 行を押し上げたように読める表現が残っていました。
- 根拠:
  - MICrONS Consortium et al. (2025) が直接前進させたのは、同一脳内の structure-function link と local conditional prediction です。
  - しかし、それは momentary synaptic weight や release state の direct readout ではありません。
  - Holler et al. (2021)、Dürst et al. (2022)、Vardalaki et al. (2022) を合わせると、synaptic-state line で直接強いのは依然として local paired physiology や state manipulation に近いルートです。
- 修正:
  - MICrONS は `same-brain structure-function link / local functional twin` を押し上げると書き換え、`current synaptic efficacy` 行そのものは Holler / Dürst / Mittermaier 側へ寄せました。

### 3. 旧サイトは `human でも state が短時間で synaptic efficacy を動かす` ことを、この論点に十分接続していませんでした

- 問題:
  - 既存本文は animal local causal evidence と human structural / metabolic scaffold の gap をうまく整理していました。
  - ただし、human neocortical tissue においても membrane state が unitary synapse の transmission と consolidation を短時間で動かすことを、このページ群の実務ルールへはまだ十分落とし込めていませんでした。
- 根拠:
  - Mittermaier et al. (2024) は human neocortical tissue で、sleep-like membrane-state sequence が EPSP 振幅と synaptic consolidation を短時間で変えることを示しました。
- 批判:
  - したがって、human でも `connectome-complete` や `same-brain connectomics` を `synaptic-state-complete` と読み替えることはできません。

### 4. Verification 側で `structural synapse metric は current weight claim を支えない` という禁止則が弱かった

- 問題:
  - `verification.md` の latent-state error budget には `synaptic efficacy / plastic history` 行がありましたが、そこでは主に connectome-only baseline と weight / plasticity 項の比較が書かれていました。
  - `EM synapse / PSD / spine / same-brain connectomics だけでは current weight claim を受理しない` という site rule が、まだ明文化されていませんでした。
- 修正:
  - `verification.md` の該当行を更新し、paired physiology・presynaptic-state manipulation・held-out perturbation を direct route 側に寄せました。
  - さらに `structural synapse metric は current weight ではありません` という注記を追加しました。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `last_updated` を `2026-03-17` に更新
  - known points に `EM / PSD / same-brain connectomics は synaptic-state prior だが current weight ではない` という site rule を追加
  - 「シナプスは binary edge ではありません」を Holler / Dürst / Matsuzaki / Vardalaki / Mittermaier を用いた構造対状態の切り分けへ改稿
  - site rules に `PSD / spine / synapse count を current weight と書かない` ルールを追加
  - 参考文献へ Dürst (2022), Mittermaier (2024) を追加
- `wiki/measurement-stack-and-claim-ceiling.md`
  - `last_updated` を `2026-03-17` に更新
  - same-brain connectomics の row を `synaptic-state prior の絞り込み` として位置づけ直し
  - `current synaptic efficacy / plastic history` 行で `EM / PSD / spine / same-brain connectomics` を proxy / bridge 側へ移し、paired physiology / state manipulation を direct route 側へ更新
  - 短い結論の対応表を `MICrONS = structure-function link`、`Holler / Dürst / Mittermaier = local synaptic-state line` へ修正
  - site rules に `EM / PSD / spine / same-brain connectomics を current weight と書かない` を追加
  - 参考文献へ Holler (2021), Dürst (2022), Matsuzaki (2004), Vardalaki (2022), Mittermaier (2024) を追加
- `verification.md`
  - `last_updated` を `2026-03-17` に更新
  - latent-state error budget の `synaptic efficacy / plastic history` 行を、paired physiology / presynaptic-state manipulation / structure-only prior の区別つきへ更新
  - `structural synapse metric は current weight ではありません` という site rule note を追加
  - 参考文献へ Holler (2021), Matsuzaki (2004), Vardalaki (2022), Dürst (2022), Mittermaier (2024) を追加

## 外部依存で保留

- なし
  - 今回の修正は、既存公開ページと検証ルールの改稿で完結しています。

## 参考文献

1. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021;591:111-116.
   - https://doi.org/10.1038/s41586-020-03134-2
2. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022;13:6126.
   - https://doi.org/10.1038/s41467-022-33565-6
3. Matsuzaki M, Honkura N, Ellis-Davies GCR, Kasai H. Structural basis of long-term potentiation in single dendritic spines. *Nature*. 2004;429:761-766.
   - https://doi.org/10.1038/nature02617
4. Vardalaki D, Chung K, Harnett MT. Filopodia are a structural substrate for silent synapses in adult neocortex. *Nature*. 2022;612:323-327.
   - https://doi.org/10.1038/s41586-022-05483-6
5. Mittermaier V, Kononenko NL, Jin Y, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
6. MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025;640:435-447.
   - https://doi.org/10.1038/s41586-025-08790-w
