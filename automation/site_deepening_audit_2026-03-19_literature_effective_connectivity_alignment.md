# Site Deepening Audit (2026-03-19, Literature Route / Effective-Connectivity Alignment)

## 対象

- 主対象: `mind_uploading_papers.md`
- 主対象: `research_harvest_50.md`
- 副対象: `wiki/u-number-guide.md`

## 今回の選定理由

- 2026-03-19 時点で、core pages 側では effective connectivity / DCM を `model-conditioned causal hypothesis` として読む route-card 方針が既に導入済みでした。
- しかし、文献導線ページ側ではその方針がまだ十分に前面化されておらず、`chronological archive` や `U4/U13` の混合導線の中で、effective connectivity の誤読停止条件が埋もれていました。
- このギャップは技術・自然科学の観点で重要です。なぜなら、front door で directed graph を見た読者が `true causal wiring` と誤読すれば、後段の identifiability / validation / abstention の規律が再び崩れるからです。

## 既存監査との関係

- 2026-03-15 の監査で、`mind_uploading_papers.md` と `research_harvest_50.md` には技術・自然科学の優先ルートが導入済みでした。
- 2026-03-19 の監査で、`wiki/observation-to-estimation.md`、`faq.md`、`verification.md`、`tech_roadmap.md` には effective-connectivity route card が導入済みでした。
- 今回の仕事はその続きであり、**core pages で固定された scientific rule を literature route に波及させること**が目的です。

## 根拠付き批判

### 1. 文献導線だけが `U4` を広く書きすぎていました

- 問題:
  - `research_harvest_50.md` の技術優先ルートは `U4 / U13` を一括で置いていました。
  - そのため、`effective connectivity の route-card 問題` と `decode / imitation separation` が同じ入口で読まれ、読者が U4 の前提審査を飛ばしやすい構造でした。
- 根拠:
  - Penny et al. (2004) は DCM 結論が比較した候補モデル集合に依存することを固定しました。
  - Rosa et al. (2012) は large model space search を tractable にしましたが、それは `true model の一意化` ではありません。
  - Jafarian et al. (2020) は neurovascular coupling の observation-model choice 自体が推定対象の一部であることを示しました。
- 批判:
  - したがって、U4 は `decode が emulation ではない` という話より一段手前で、まず `directed graph が discovered wiring ではない` ことを止める必要があります。
  - 文献地図でも U4 を独立ルートとして見せるべきでした。

### 2. 論文アーカイブは effective-connectivity の evidence class を独立させていませんでした

- 問題:
  - `mind_uploading_papers.md` は demo / observability / benchmark / hidden-state を分けていましたが、effective connectivity が demo や一般的な `causal` 語に吸収されやすい構造でした。
- 根拠:
  - Frässle et al. (2021) は whole-brain directed-connectivity 推定を可能にしましたが、これは tractability の前進です。
  - Jafarian et al. (2024) は reliability を close-in-time, similar-circumstance 条件で示しましたが、general portability ではありません。
  - Wu et al. (2024) は computational complexity を主問題として高速化を報告しており、identifiability solved を報告しているわけではありません。
- 批判:
  - つまり、effective connectivity の文献は `task-limited demo` でも `benchmark/toolchain` でもなく、**candidate-model dependence と observation-model dependence を伴う model-conditioned causal claim** という独自クラスで読む必要があります。

### 3. U4 の代表文献が route-card の scientific core より広く散っていました

- 問題:
  - `research_harvest_50.md` の U4 には review, arXiv, tool docs が混ざっており、route-card の中心となる一次文献が相対的に見えにくい状態でした。
- 根拠:
  - Penny (2004), Rosa (2012), Jafarian (2020), Frässle (2021), Jafarian (2024), Wu (2024) の並びだけで、
    1. candidate model dependence
    2. large model-space tractability
    3. observation-model dependence
    4. whole-brain scaling
    5. reliability under matched conditions
    6. faster inversion
    を順序立てて示せます。
- 批判:
  - U4 の front door では、まずこの scientific spine を出す方が合理的です。review や周辺手法はその後で十分です。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `last_updated` を 2026-03-19 に更新
  - 技術・自然科学の優先ルートへ `effective connectivity / DCM route card` を追加
  - evidence class に `model-conditioned causal hypothesis / effective connectivity` を追加
  - route-card 読みを明示する note-box を追加
  - テーマ別導線に `effective connectivity / DCM safely` を追加
- `research_harvest_50.md`
  - `last_updated` を 2026-03-19 に更新
  - 技術優先ルートを `U1/U7 -> U4 -> U13 -> U8 -> U3 -> U10` へ更新
  - `Why U4 now sits on its own rung` を追加
  - U4 section を一次文献中心に再編
  - U4 の unresolved point を `node set / priors / hemodynamics / omitted competitors / held-out validation` まで明文化
- `wiki/u-number-guide.md`
  - `last_updated` を 2026-03-19 に更新
  - default route を `U1/U7 -> U4 -> U13 -> U8 -> U3 -> U10` に更新
  - U4 を decode/WBE 誤読より先に読む理由を note-box で明記

## 今回実行する変更と外部依存の切り分け

- 今回実行した変更:
  - 公開本文の導線改稿
  - U4 の代表文献の再編
  - 技術・自然科学向け読解ルールの site-wide 整合
- 外部依存で保留:
  - なし
  - 今回の作業は repo 内の公開文面修正だけで完結しています。

## 参考文献

1. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
2. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
3. Jafarian A, Litvak V, Cagnan H, Friston KJ, Zeidman P. Comparing dynamic causal models of neurovascular coupling with fMRI and EEG/MEG. *NeuroImage*. 2020;216:116734.
   - https://doi.org/10.1016/j.neuroimage.2020.116734
4. Frässle S, Paulus FM, Krach S, Jansen A. Test-retest reliability of effective connectivity in the face perception network. *Human Brain Mapping*. 2016;37(2):730-744.
   - https://doi.org/10.1002/hbm.23061
5. Frässle S, Manjaly ZM, Do CT, Kasper L, Pruessmann KP, Stephan KE. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021;225:117491.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
6. Vink JJ, Ramos-Nuñez AI, Bellesi A, et al. The brain's functional connectome is a poor predictor of the brain's causal activity flow. *PLOS Computational Biology*. 2020;16(1):e1007866.
   - https://doi.org/10.1371/journal.pcbi.1007866
7. Jafarian A, Assem MK, Kocagoncu E, et al. Reliability of dynamic causal modelling of resting-state magnetoencephalography. *Human Brain Mapping*. 2024.
   - https://doi.org/10.1002/hbm.26782
8. Wu H, Hu X, Zeng Y. A fast dynamic causal modeling regression method for fMRI. *NeuroImage*. 2024;304:120954.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
9. Hauser A, Bühlmann P. Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. *Journal of Machine Learning Research*. 2012;13:2409-2464.
   - https://jmlr.org/papers/v13/hauser12a.html
