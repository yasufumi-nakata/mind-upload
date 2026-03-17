# Site Deepening Audit (2026-03-18, Activity-Dependent Transcription / Chromatin / Epigenetic State)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-18 時点で公開サイトは、`connectome-complete ≠ emulation-complete`、`cell type ≠ intrinsic excitability`、`synapse ≠ plasticity gate`、`same-day fit ≠ cross-day maintenance` をかなり強く分離できておりました。
- その一方で、`activity-dependent transcription / chromatin / epigenetic state` はなお `cell-type label` や `molecular turnover` の陰に入り、`現在の可塑性可能状態` と `静的な細胞アイデンティティ` がやや近く読める構造が残っておりました。
- この弱点は技術・自然科学の観点で重要です。なぜなら、同じ connectome と同じ cell type が与えられても、`どの細胞が engram allocation に乗りやすいか`、`どの遅延転写プログラムが memory stabilization を支えるか`、`どの locus-specific plasticity rule が開いているか` はなお別変数だからです。

## 主要な批判点

### 1. 旧サイトは `cell identity` と `current plasticity program` を十分に分けていませんでした

- 問題:
  - 既存サイトは `transcriptomic type` の重要性自体は正しく書けていました。
  - しかし、読者が `cell atlas があれば、記憶割り当てや stabilization に必要な転写状態もかなり見えた` と誤読しうる余地が残っていました。
- 根拠:
  - Santoni et al. (2024) は、memory-trace formation への neuronal eligibility が chromatin plasticity により事前規定されることを示しました。
  - Traunmüller et al. (2025) は、新奇環境曝露後に hippocampus で時間依存かつ領域依存の chromatin accessibility / gene-expression 変化が起こることを示しました。
  - Terceros et al. (2026) は、thalamocortical circuit で異なる post-learning window に異なる transcriptional gate が必要であることを示しました。
- 批判:
  - したがって、`cell type が分かった` と `現在の memory-stabilization controller が分かった` は同じではございません。
  - `static atlas` を `current plasticity-competent state` に読み替えるのは強すぎます。

### 2. 旧サイトは `transcriptomic clue` と `causal epigenetic control` を同列に置きうる構造でした

- 問題:
  - 既存ページ群では spatial transcriptomics の進展は触れられていましたが、`time-stamped clue`、`locus-specific perturbation`、`longitudinal stabilization gate` の差が site-wide rule になっていませんでした。
- 根拠:
  - Coda et al. (2025) は、cell-type- and locus-specific epigenetic editing により memory expression を双方向に制御できることを示しました。
  - Sun et al. (2024) は spatial transcriptomics から long-term memory 候補を提案しましたが、Mukamel & Yu (2025) は DEG 解釈が animal-level dependence の扱いに敏感であると批判し、Sun et al. (2025) は解析意図の差を理由に反論しました。
- 批判:
  - したがって、`memory-related DEG が見えた` と `causal controller を掴んだ` は同じではありません。
  - transcriptomic evidence には、`hypothesis-generating` と `causal / gate-setting` を分けるルールが必要でした。

### 3. 旧 Verification には `transcriptional / chromatin state audit` の提出物がありませんでした

- 問題:
  - `cell-type label`、`ECM / PNN`、`timing-state`、`glial state` は提出物へ落ちていましたが、`current transcriptional / chromatin state` を独立欄として要求していませんでした。
- 批判:
  - これでは `cell atlas を足した`、`memory-related transcript を見た`、`epigenetic intervention で effect が出た` の三者を、同じ「state が見えた」に潰してしまいます。
  - site-wide には、`何を直接測ったのか`、`時間窓はどこか`、`causal perturbation があるか`、`どこから先を latent に残すか` を明示する必要がありました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `activity-dependent transcription / chromatin state` を front matter、highlights、known/unknown points に追加
  - `9 maintenance-states` を `10 maintenance-states` に更新
  - 新しい state row と本文節を追加し、`cell identity ≠ current plasticity program` を一次文献つきで明文化
  - transcriptomic clue と causal epigenetic evidence の読み分け規則を追加
  - long-horizon memory claim の最低提出物へ `time-stamped transcription / chromatin route or omission log` を追加
- `wiki/connectome-is-not-enough.md`
  - `7 state classes` を `8 state classes` に更新
  - `activity-dependent transcription / chromatin state` を独立 state class として追加
  - augmentation / ablation table に `+ activity-dependent transcription / chromatin audit` を追加
  - site rule に `transcriptomic atlas is not current chromatin state` を追加
- `verification.md`
  - `state variable integrity gate` を `at least eight loose state classes` へ更新
  - `Activity-dependent transcription / chromatin / epigenetic state` row を追加
  - `cell-type atlas is not current transcriptional state` addendum を追加
  - augmentation table に `+ transcriptional / chromatin state audit` を追加
- `wbe_101.md`
  - 入口の hidden-state 説明へ `activity-dependent transcription / chromatin state` を追加
  - entry table に同 state row を追加
  - 導入参考文献へ Santoni / Coda / Terceros を追加

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と site-wide 判定ルールの改稿で完結しております。

## 参考文献

1. Santoni G, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024;385(6716):eadg9982.
   - https://doi.org/10.1126/science.adg9982
2. Traunmüller L, et al. Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. *Nature Communications*. 2025;16:2613.
   - https://doi.org/10.1038/s41467-025-63029-6
3. Coda B, et al. Cell-type- and locus-specific epigenetic editing of memory expression. *Nature Genetics*. 2025;57:1211-1222.
   - https://doi.org/10.1038/s41588-025-02195-z
4. Terceros Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;642:489-498.
   - https://doi.org/10.1038/s41586-025-09334-w
5. Sun X, et al. Spatial transcriptomics reveal neuron-astrocyte synergy in long-term memory. *Nature*. 2024;627:374-381.
   - https://doi.org/10.1038/s41586-023-07011-6
6. Mukamel EA, Yu X. False positives in study of memory-related gene expression. *Nature*. 2025;642:E1-E3.
   - https://doi.org/10.1038/s41586-025-08988-y
7. Sun X, et al. Reply to: False positives in study of memory-related gene expression. *Nature*. 2025;642:E4-E6.
   - https://doi.org/10.1038/s41586-025-08989-x
