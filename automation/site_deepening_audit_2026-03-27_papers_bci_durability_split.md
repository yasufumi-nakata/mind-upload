# Site Deepening Audit (2026-03-27, Papers BCI Durability Split)

## 対象

- 主対象: `mind_uploading_papers.md`
- 派生同期: `summary_booklet.md`

## web確認対象

- `https://mind-upload.com/mind_uploading_papers.html`
- `https://www.nature.com/articles/s41586-023-06377-x`
- `https://www.nature.com/articles/s41593-025-01905-6`
- `https://www.nature.com/articles/s41586-025-09127-3`
- `https://www.nature.com/articles/s41467-025-63825-0`
- `https://www.nature.com/articles/s41467-025-59652-y`
- `https://www.nature.com/articles/s41551-025-01536-z`

## 今回この箇所を選んだ理由

- `mind_uploading_papers.md` は site 全体の文献入口であり、ここでの圧縮表現が読者の最初の claim ceiling を決めます。
- 2026-03-27 時点の本文は、language-facing papers の分解はかなり進んでいましたが、侵襲型BCIだけはなお `closed-loop communication success` に寄りすぎていました。
- 技術・自然科学の観点では、この圧縮は弱いです。理由は、`same-session throughput / expressivity` と `fixed-decoder durability` と `adaptive stabilization / recalibration` は、同じ operational achievement ではないからです。

## 根拠付き批判

### 1. 高速な speech neuroprosthesis は、そのまま長期 durability を意味しません

- 根拠:
  - [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x) は高性能な speech decoding / communication を示しましたが、主に `communication throughput under a trained interface` を強める論文です。
  - [Littlejohn et al. (2025)](https://doi.org/10.1038/s41593-025-01905-6) は streaming brain-to-voice の front を押し上げていますが、これも主張の中心は `expressive online communication` です。
  - [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は near-instant voice synthesis と silence fallback を示す一方で、固定デコーダ性能が約 `15 days` で低下しうることを明示しています。
- 批判:
  - したがって、`speech became fast and natural` を `decoder stayed stable` と読んではいけません。
  - 高速化と自然化は重要ですが、それだけでは `long-horizon deployability` を支持しません。

### 2. Recalibration による救済は、no-drift の証拠ではありません

- 根拠:
  - [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) は latent-dynamics alignment によって cross-day 変動を緩和する route を示しています。
  - [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は unsupervised recalibration が closed loop で `one month` 維持できること、また `five years` 分の cursor-control data から drift と recalibration burden を評価できることを示しました。
  - これらの papers が強めるのは `adaptive rescue route` であり、元の decoder が自律的に不変だったという主張ではありません。
- 批判:
  - `month-scale use after recalibration` を `stable decoder solved` と読むのは、主張のすり替えです。
  - 実運用評価では、`fixed-decoder interval`, `recovery burden`, `how often rescue is needed` を独立に読む必要があります。

### 3. 文献入口でこの split を明示しないと、site の他ページで止めている誤読が再注入されます

- 根拠:
  - 同じ site では、すでに `Neural Contribution Card`、`state / trait / drift`、`closed-loop latency / jitter / safety stops` のように、claim を component-wise に止める読み方を導入しています。
  - それにもかかわらず papers front door が `invasive BCI = closed-loop success` に見えるままだと、詳細ページ側の停止線が入口で崩れます。
  - [Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) も、cross-subject transfer learning による decoder initialization を強めるのであって、長期固定安定性を直接示す論文ではありません。
- 批判:
  - front door で `throughput`, `initialization`, `durability`, `adaptive rescue` を分けない構造は、技術フロンティアの読み分けとして不十分です。
  - このままでは、`online voice exists` という事実が `durable invasive BCI exists` へ過大に読み替えられます。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter の `known_points` と `page_highlights` に、侵襲型BCIを `communication throughput / expressivity`、`fixed-decoder durability`、`adaptive stabilization / recalibration` に分ける reading rule を追加
  - 2026 technical addendum に、侵襲型BCIを 3 operational routes として読むべき理由を追記
  - `technical-fast-lane` の優先質問に `fixed-decoder horizon と adaptive rescue の区別` を追加
  - `Invasive speech decoding / communication subsystem` row を same-session communication と decoder-initialization の主張へ限定
  - `Long-horizon BCI durability / recalibration route` row を新設
  - `Read invasive BCI papers through a durability split as well` note box を追加
  - `technical-evidence-classes` に `temporal durability / adaptive stabilization` row を追加
  - evidence-class 導入段落も、`task-limited system performance` と `temporal durability / adaptive stabilization` の分離に同期
  - 最下部の読書テーマ表に、long-horizon durability / recalibration の読書入口を追加

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象として同期

## 今回の修正で止めた誤読

- `streaming or naturalistic voice output exists` = `fixed decoder is durable`
- `recalibrated long-term control exists` = `neural drift is solved`
- `cross-subject transfer helps initialization` = `subject-general robust deployment exists`
- `invasive BCI works online` = `identity-relevant internal state is stably recoverable`

## 外部依存タスク

- なし
  - 今回の変更は、公開本文・派生要約・監査記録の更新で完結しています。

## 参考文献

1. Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023;620:1031-1036.
   - https://doi.org/10.1038/s41586-023-06377-x
2. Littlejohn KT, Shuvro S, Wang P, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
3. Wairagkar M, Khare A, Vaidya M, et al. An instantaneous voice-synthesis neuroprosthesis for communication. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
4. Singh A, Wu E, Ramsey NF, et al. Transfer learning via distributed brain recordings enables reliable speech decoding. *Nature Communications*. 2025;16:9034.
   - https://doi.org/10.1038/s41467-025-63825-0
5. Karpowicz BM, Zhao Y, Fan JM, et al. Stable intracortical brain-computer interface control via alignment of low-dimensional dynamics. *Nature Communications*. 2025;16:5821.
   - https://doi.org/10.1038/s41467-025-59652-y
6. Wilson GH, So RQ, Wang P, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
