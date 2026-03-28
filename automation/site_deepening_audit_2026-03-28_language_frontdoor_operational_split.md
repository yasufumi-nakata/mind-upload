# Site Deepening Audit (2026-03-28, language front door / invasive BCI operational split)

## 対象

- 主対象:
  - `faq.md`
  - `wbe_101.md`
  - `tech_roadmap.md`
- 派生同期:
  - `summary_booklet.md`

## web確認対象

- `https://mind-upload.com/faq.html`
- `https://mind-upload.com/wbe_101.html`
- `https://mind-upload.com/tech_roadmap.html`
- `https://doi.org/10.1038/s41586-023-06377-x`
- `https://doi.org/10.1038/s41593-025-01905-6`
- `https://doi.org/10.1038/s41586-025-09127-3`
- `https://doi.org/10.1038/s41467-025-63825-0`
- `https://doi.org/10.1038/s41467-025-59652-y`
- `https://doi.org/10.1038/s41551-025-01536-z`

## 今回この箇所を選んだ理由

- 文献ハブの `mind_uploading_papers.md` では、侵襲型言語BCIを
  - same-session throughput / expressivity
  - transfer-assisted initialization
  - fixed-decoder durability
  - adaptive stabilization / rescue
  に分ける reading rule がすでに導入されていました。
- しかし 2026-03-28 時点の front door である `faq.md`、`wbe_101.md`、`tech_roadmap.md` は、なお `speech BCI` をほぼ一つの成功列として読める構造を残していました。
- この圧縮は技術・自然科学の観点では弱いです。入口ページで圧縮すると、詳細ページで止めている誤読を再注入するからです。

## 根拠付き批判

### 1. throughput / expressivity は transfer-assisted initialization と同じ成果ではありません

- 根拠:
  - [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x) は large-vocabulary speech BCI と高い same-session throughput を示しました。
  - [Littlejohn et al. (2025)](https://doi.org/10.1038/s41593-025-01905-6) は streaming brain-to-voice を前進させました。
  - [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は near-instant voice synthesis と silence fallback を示しました。
  - 一方で [Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) は、distributed intracranial recordings を使った cross-subject transfer learning により、group-derived decoder が individual-only training を上回る初期化ルートを示しました。
- 批判:
  - したがって `speech BCI が速い` と `個別被験者への初期化が改善した` は別の operational claim です。
  - 前者を後者へ読み替えるのは、subject-generalization の過大読解です。

### 2. fixed-decoder durability は adaptive rescue と同じ成果ではありません

- 根拠:
  - [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x) は、new-day retraining を入れない offline slice でも一定性能が残ることを示しましたが、同時に multi-day adaptation が未解決であることを明記しています。
  - [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) は latent-dynamics alignment による stabilization を示しました。
  - [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は unsupervised recalibration を使った long-term rescue route を示しました。
- 批判:
  - これは `固定デコーダが十分持続した` と `適応で救済できた` が同じ主張でないことを意味します。
  - 入口ページでこの二つを分けないと、救済成功が no-drift の証拠に見えてしまいます。

### 3. Wairagkar 2025 の強さも、fast synthesis と long-horizon stability を自動では接続しません

- 根拠:
  - [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は、instantaneous voice synthesis、silence fallback、chronically implanted participant での表情的出力を前進させました。
  - しかし同論文の session 1 例は same-day training を明示しており、また chronic usage video があること自体は fixed-decoder durability の独立監査を置き換えません。
- 批判:
  - `chronically implanted and expressive` を `fixed decoder solved` と読むのは過剰です。
  - ここでも route の型名を front door で固定する必要があります。

### 4. 入口ページが粗いと、詳細ページの stop line が無効化されます

- 根拠:
  - `verification.md` と `wiki/closed-loop-latency-jitter-and-safety-stops.md` はすでに
    - co-adaptation / credit assignment
    - fixed-decoder durability
    - rescue-mode recalibration
    を別 object に分けています。
  - `mind_uploading_papers.md` も 2026-03-27 時点で、侵襲型BCIを durability split で読ませる構造へ更新済みです。
- 批判:
  - それにもかかわらず FAQ と WBE 101 と Roadmap が `speech BCI progress` を一段で出すと、読者は入口で再び圧縮読解に戻ります。
  - これは site-wide governance として不整合でした。

## 今回実行した変更

- `faq.md`
  - `last_updated` は維持したまま front matter の `page_highlights` / `known_points` に invasive language BCI の four-way split を追加しました。
  - `Q. What is the minimum you should check in a brain-to-text demo?` を更新し、
    - seven things という誤記を修正
    - `operational route` を独立チェック項目として追加
    - Willett 2023, Littlejohn 2025, Wairagkar 2025, Singh 2025, Karpowicz 2025, Wilson 2025 を使って front-door explanation を改稿
  - 参考文献に Singh 2025 と Karpowicz 2025 を追加しました。

- `wbe_101.md`
  - front matter の `page_highlights` / `known_points` に同じ four-way split を追加しました。
  - `Technology-route comparison` の `Invasive / hybrid neuroprosthesis` row を改稿し、
    - same-session throughput
    - transfer-assisted initialization
    - causal closed-loop improvement
    を混同しない形に更新しました。
  - `2026-03-28 addendum: invasive language BCIs are not one operational route either` を追加しました。
  - 参考文献に Littlejohn 2025, Wairagkar 2025, Singh 2025, Karpowicz 2025, Wilson 2025 を追加しました。

- `tech_roadmap.md`
  - front matter の `page_highlights` / `known_points` に V8 front-door split を追加しました。
  - `V8` table を 3 行から 6 行へ再編し、
    - non-invasive semantic / caption
    - non-invasive word / speech
    - invasive throughput / expressivity
    - transfer-assisted initialization
    - fixed-decoder durability slice
    - adaptive stabilization / rescue
    の区別が読める形に更新しました。
  - `Minimum evaluation pack` に `Operational route label` を追加しました。
  - 参考文献リストに Singh 2025 を追加しました。

- `summary_booklet.md`
  - front matter 更新を反映するため再生成対象にしました。

## 今回止めた誤読

- `speech BCI paper` = one monotonic invasive-BCI progress bar
- `throughput improved` = `cross-subject initialization improved`
- `adaptive rescue worked` = `fixed decoder stayed stable`
- `chronically implanted expressive output exists` = `long-horizon fixed-decoder durability is solved`
- `invasive language result` = `subject-general robust deployment`

## 外部依存タスク

- なし
  - 今回の変更は repo 内本文、監査記録、派生再生成、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
   - https://doi.org/10.1038/s41586-023-06377-x
2. Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
3. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
4. Singh A, Wu E, Ramsey NF, et al. Transfer learning via distributed brain recordings enables reliable speech decoding. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-63825-0
5. Karpowicz BM, Ali YH, Wimalasena LN, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
6. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
