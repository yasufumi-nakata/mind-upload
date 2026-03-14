# Site Deepening Audit (2026-03-15, Entry Pages / Maintenance-State Propagation)

## 対象

- 主対象: `index.md`
- 副対象: `wbe_101.md`
- 副対象: `faq.md`

## 今回の選定理由

- 個別 wiki と `verification.md` では、connectome だけでは足りないことと maintenance-state の広がりがかなり明確になっていました。
- しかし公開入口ページ群では、その論点が `関連 wiki へのリンク` に圧縮されすぎており、最初に読む読者ほど `配線図 + cell type が取れれば、残りは微調整` と誤読しやすい構造が残っていました。
- 入口ページは site-wide の読み方を決めるため、ここが粗いと、その後の `connectome-complete は scaffold である` という慎重な立場が十分に伝わりません。

## 主要な批判点

### 1. 入口ページは maintenance-state を「存在するらしい追加情報」程度に見せていました

- 問題:
  - `index.md` と `wbe_101.md` は connectome 不足へ触れていましたが、sleep / wake 依存の再正規化、髄鞘 / oligodendrocyte support、glial / metabolic support が何を壊すのかを入口で固定できていませんでした。
  - その結果、`same-day の活動一致` と `cross-day の維持機構一致` が別問題であることが前景化していませんでした。
- 根拠:
  - Hengen et al. (2016)、Torrado Pacheco et al. (2021)、Xu et al. (2024) は、sleep / wake cycle が firing-rate homeostasis と network regime recovery に関わることを示しました。
  - Gibson et al. (2014)、McKenzie et al. (2014)、Looser et al. (2024) は、髄鞘 / oligodendrocyte support が timing と axonal health に関わることを示しました。
  - Suzuki et al. (2011)、Cahill et al. (2024)、Lee et al. (2022) は、glial / metabolic support と turnover 下の active maintenance が memory consolidation や slow state に関わることを示しました。
- 修正:
  - `index.md` に、入口で先に防ぐ誤読として `connectome-complete ≠ emulation-complete` を明示しました。
  - `wbe_101.md` に `入口で外せない hidden state` 節を新設し、4 クラスへ要約しました。

### 2. 入口ページには「どこまでなら言えるか」の境界が不足していました

- 問題:
  - 既存の導線は深い wiki へ誘導する点で有用でしたが、入口自身は `何がまだ言えないか` を短く固定していませんでした。
  - これにより、読者が `connectome-complete` や `digital twin` を、そのまま state-complete reconstruction と混同する余地がありました。
- 根拠:
  - Gouwens et al. (2021) は、同じ transcriptomic type の内部にも morpho-electric phenotype の連続性が残ることを示しました。
  - 上記の sleep / myelin / glia 系一次文献はいずれも、長期ダイナミクスを支える状態変数が配線図の外に残ることを示します。
- 修正:
  - `wbe_101.md` に、`connectome-complete は structural scaffold の前進であり、emulation-complete の宣言ではない` と明記しました。
  - この判断は、上記一次文献が maintenance-state を別変数として残している点からの **推論** であることも本文に残しました。

### 3. FAQ には、この誤解へ直接答える項目がありませんでした

- 問題:
  - FAQ は入口として優秀ですが、`コネクトームと cell type が分かれば十分か` という自然な疑問へ直接答える節がありませんでした。
  - そのため、重要論点なのに読者が深い wiki へ進まないと答えに到達しない構造でした。
- 修正:
  - `faq.md` に `Q. コネクトームと cell type が分かれば、残りはほぼ埋まる？` を追加しました。
  - 入口の早い段階で、sleep / myelin / glia を短く列挙し、詳細ページへ戻る導線を追加しました。

## 今回実行した変更

- `index.md`
  - `last_updated` を 2026-03-15 に更新
  - `page_highlights` / `known_points` に maintenance-state の不足を追加
  - `入口で先に防ぐ誤読` の注記を新設
- `wbe_101.md`
  - `last_updated` を 2026-03-15 に更新
  - `入口で外せない hidden state` 節を新設
  - 参考文献へ sleep / myelin / glia / maintenance-state 系の一次文献を追加
- `faq.md`
  - `last_updated` を 2026-03-15 に更新
  - `Q2c` を追加
  - 入口案内テーブルと参考文献を更新

## 外部依存で保留

- maintenance-state artifact pack の共通 schema 化
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: sleep history、overnight recovery、conduction / myelin proxy、glial / metabolic proxy を同じ benchmark で比較できること
  - 完了条件: `same-day fit`、`cross-day recovery`、`timing-sensitive stability`、`active maintenance` を同一 schema で提出できること

## 参考文献

- Gouwens NW, et al. Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. Nature. 2021.
  - https://doi.org/10.1038/s41586-020-2907-3
- Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. Cell. 2016.
  - https://doi.org/10.1016/j.cell.2016.01.046
- Torrado Pacheco A, et al. Sleep Promotes Downward Firing Rate Homeostasis. Neuron. 2021.
  - https://doi.org/10.1016/j.neuron.2021.04.004
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. Nat Commun. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Gibson EM, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. Science. 2014.
  - https://doi.org/10.1126/science.1252304
- McKenzie IA, et al. Motor skill learning requires active central myelination. Science. 2014.
  - https://doi.org/10.1126/science.1254960
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. Nat Neurosci. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Suzuki A, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. Cell. 2011.
  - https://doi.org/10.1016/j.cell.2011.02.018
- Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. Nature. 2024.
  - https://doi.org/10.1038/s41586-024-07311-5
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. Proc Natl Acad Sci U S A. 2022.
  - https://doi.org/10.1073/pnas.2211572119
