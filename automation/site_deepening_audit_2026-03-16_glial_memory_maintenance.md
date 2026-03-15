# Site Deepening Audit (2026-03-16, Glial Memory Maintenance / Astrocyte Ensembles)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wbe_101.md`
- 関連対象: `verification.md`

## 今回の選定理由

- 2026-03-16 時点でサイトは、sleep/homeostasis、myelin、glial metabolism を maintenance-state としてかなり明確に扱えていました。
- ただし glia の扱いはまだ `memory consolidation の背景` に寄り、2024-2026 の一次文献が示した `astrocyte ensemble が recall・multiday stabilization・fear-memory representation に関わる` という段階までは本文の中心導線に出せていませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、読者が `neuron-side engram を押さえれば、長期想起や再安定化もだいたい決まる` と誤読しうるからです。

## 主要な批判点

### 1. 現行サイトは glia を support variable としては扱えていましたが、memory-state variable としては弱かった

- 問題:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` は Suzuki et al. (2011)、Cahill et al. (2024)、Lee et al. (2022) により、astrocyte-neuron lactate transport、astrocyte network state、active maintenance を押さえていました。
  - しかし、astrocyte ensemble そのものが memory recall や数日スパンの stabilization に関わることは前面化できていませんでした。
  - そのため `glia omission` が `多少の背景近似` に見えやすく、`neuron-only 成功` を長期 claim へ延長しやすい構造でした。
- 根拠:
  - Williamson et al. (2025) は、learning-associated astrocyte ensemble の再活性化が hippocampal memory recall を誘発し、astrocyte 特異的 NFIA deletion が recall を抑えることを示しました。
  - Dewa et al. (2025) は、astrocytic ensemble が multiday trace として emotional memory の stability / precision を支えることを示しました。
  - Bukalo et al. (2026) は、amygdala astrocytes が fear retrieval / extinction に応じて再編成され、astrocyte Ca2+ signaling が memory-supporting neural representations を支えることを示しました。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` の glia 節を、`代謝支援` から `記憶想起・安定化・表現の state variable` へ改稿しました。
  - `wbe_101.md` の hidden-state 入口も同期し、primer 段階で `neuron-only = long-term memory-complete` と読ませない表現へ更新しました。

### 2. glia 関連の新しい transcriptomics 論文を、そのまま決定打扱いすると evidence ladder を壊します

- 問題:
  - 2024 年の `Spatial transcriptomics reveal neuron-astrocyte synergy in long-term memory` は重要ですが、そのまま `astrocyte causal proof` と書くのは強すぎます。
- 根拠:
  - Sun et al. (2024) は peri-engram neuron / astrocyte synergy と `Igfbp2` を long-term memory candidate として提案しました。
  - しかし Mukamel & Yu (2025) は、multiple-comparison と同一動物由来細胞の依存性を補正すると有意な DEG は残らないと批判しました。
  - Sun et al. (2025) は同日 Reply を返しており、現時点では `解釈に争いがある transcriptomic clue` と読むのが安全です。
- 修正:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` に `証拠強度の読み方` ボックスを追加しました。
  - transcriptomics は `hypothesis-generating`、causal weight は Williamson / Dewa / Bukalo の介入研究へ置く、と site rule を明文化しました。

### 3. Verification 側の latent-state error budget は glia 行がまだ recall / restabilization を十分に監査していませんでした

- 問題:
  - `verification.md` の `glial / slow-state support` 行は slow-state と long-term recovery を押さえていましたが、`再想起後の restabilization` や `astrocyte ensemble state` がまだ提出物へ落ちていませんでした。
- 根拠:
  - Dewa et al. (2025) が示したのは、単なる slow background ではなく、repeated recall をまたぐ memory stabilization の段階です。
  - Bukalo et al. (2026) が示したのは、fear retrieval / extinction に応じた circuit representation support であり、`long-term memory claim` を neuron-only fit で済ませるのは危険です。
- 修正:
  - `verification.md` の glia 行を更新し、`restabilization window` と `astrocyte ensemble state` を最低限の監査ログへ追加しました。

### 4. 既存ページに引用整合性の小さな破綻がありました

- 問題:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` の sleep 節で、de Vivo et al. (2017) と Diering et al. (2017) の DOI が本文中で入れ替わっていました。
- 修正:
  - de Vivo et al. (2017) を `doi:10.1126/science.aah5982`、Diering et al. (2017) を `doi:10.1126/science.aai8355` へ修正しました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を 2026-03-16 に更新
  - glia 行を `astrocyte ensemble` を含む形へ更新
  - astrocyte 節を `想起・安定化・表現` の state variable として全面改稿
  - Sun et al. (2024) / Mukamel & Yu (2025) / Sun et al. (2025) を使った evidence-strength note を追加
  - Williamson et al. (2025)、Dewa et al. (2025)、Bukalo et al. (2026) を参考文献へ追加
  - sleep 節の DOI 整合性を修正
- `wbe_101.md`
  - `last_updated` を 2026-03-16 に更新
  - hidden-state 段落を glia / astrocyte の 2025-2026 causal evidence に同期
  - glial row を `recall / stabilization` まで読める表現へ更新
  - glia 関連参考文献を追加
- `verification.md`
  - `glial / slow-state support` 行に `restabilization window` と `astrocyte ensemble state` を追加
  - glia 関連一次文献を参考文献へ追加

## 外部依存で保留

- なし
  - 今回の作業は、このリポジトリ内の本文更新と引用整合性修正で完結しています。

## 参考文献

- Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011.
  - https://doi.org/10.1016/j.cell.2011.02.018
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Sun X, et al. Spatial transcriptomics reveal neuron-astrocyte synergy in long-term memory. *Nature*. 2024.
  - https://doi.org/10.1038/s41586-023-07011-6
- Mukamel EA, Yu X. False positives in study of memory-related gene expression. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08988-y
- Sun X, et al. Reply to: False positives in study of memory-related gene expression. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08989-x
- Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-024-08170-w
- Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09619-2
- Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
  - https://doi.org/10.1038/s41586-025-10068-0
- de Vivo L, et al. Ultrastructural evidence for synaptic scaling across the wake/sleep cycle. *Science*. 2017.
  - https://doi.org/10.1126/science.aah5982
- Diering GH, et al. Homer1a drives homeostatic scaling-down of excitatory synapses during sleep. *Science*. 2017.
  - https://doi.org/10.1126/science.aai8355
