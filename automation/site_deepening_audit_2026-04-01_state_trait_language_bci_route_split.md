# Site Deepening Audit (2026-04-01, State-Trait Language-BCI Route Split)

## 対象として選んだ箇所

- `wiki/state-trait-and-drift.md`
- `verification.md`

## 今回ここを優先した理由

- サイト全体では 2026-03-31 に `perspective.md` と `wbe_101.md` 側で侵襲的 language BCI を
  - `throughput / expressivity`
  - `transfer initialization`
  - `bounded fixed-decoder slice`
  - `adaptive rescue`
  に分ける方向へ進んでいました。
- しかし、時間的主張の上限を決める中核ページ `wiki/state-trait-and-drift.md` は、依然として
  - `fixed-decoder durability`
  - `recalibration burden`
  の分離まではしていても、
  - `transfer initialization`
  を独立した route としては十分に明示していませんでした。
- そのままだと、読者が `cross-subject transfer` を `participant-invariant backbone` や `long-horizon durability` の証拠として過大読解しやすい状態が残ります。
- この弱点は周辺ページではなく、`temporal validity` の規範ページで直すのが合理的でした。

## 根拠付き批判

### 1. 現状の state-trait page は `speech BCI` の時間的成功をまだ1本の進歩バーとして読ませうる

- 既存文面は、
  - throughput 系
  - fixed-decoder durability
  - recalibration
  の違いをある程度は示していました。
- しかし、これだけでは `transfer learning` による初期化成功まで `decoder stayed stable` や `trait-like invariant object was found` と同じ列に置かれかねません。
- 一次文献はその読みを支持しません。
  - [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x) は高 throughput な speech neuroprosthesis と bounded な no-new-day-training slice を示しました。
  - [Littlejohn et al. (2025)](https://doi.org/10.1038/s41593-025-01905-6) は streaming brain-to-voice による throughput / expressivity を示しました。
  - [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は instantaneous voice synthesis と silence fallback、さらに fixed-decoder degradation の可視化を示しました。
  - [Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) は distributed recordings による transfer initialization を示しましたが、これは long-horizon no-update durability とは別物です。
  - [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) と [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は alignment / unsupervised recalibration による adaptive rescue を示しました。

### 2. `transfer initialization` を独立 row にしないと、temporal-validity 議論が歪む

- `transfer initialization` は
  - 初期化コストを下げる
  - 学習開始点を改善する
  ことを示しうる一方で、
  - 長期固定デコーダの妥当性
  - participant-invariant latent manifold
  - cross-site portability
  をそのまま保証しません。
- したがって、`state-trait-and-drift` でこれを独立 route にしないと、
  - `cross-subject transfer`
  - `fixed-decoder durability`
  - `adaptive rescue`
  がひとまとまりの longitudinal success に見えてしまいます。

### 3. Verification 側にも最小限の route-typing が必要だった

- `verification.md` はサイト全体の card/log 規範です。
- ここに `communication route type / temporal claim` がないままだと、
  - `state-trait-and-drift` だけが厳しく
  - `verification` 側の提出欄は粗い
  という整合性問題が残ります。
- したがって今回の修正は、
  - 背景ロジックを `wiki/state-trait-and-drift.md`
  - 提出項目を `verification.md`
  の両方で揃える必要がありました。

## 今回実行した変更

### `wiki/state-trait-and-drift.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` と `known_points` に、侵襲的 language BCI の temporal route split を明記しました。
- `2026-04-01 correction: invasive language BCIs are not one temporal-validity route` を追加し、
  - throughput / expressivity
  - transfer initialization
  - bounded fixed-decoder slice
  - adaptive rescue
  を分ける必要を、一次文献付きで説明しました。
- 旧 `Speech and communication BCIs still need an explicit transfer ceiling` 節を、
  - `Invasive language BCIs split into four temporal routes`
  へ更新しました。
- その直下に 4 route の table を追加し、各 route について
  - representative literature
  - what it supports
  - what it still does not support
  を明示しました。
- `Minimum submission` table に `communication route type` を追加し、最低限必要な申告事項として
  - route class
  - no-new-day-training comparator
  - open-loop comparator
  - subject-specific fine-tuning
  - time since last supervised calibration
  を要求する形へ寄せました。
- `Common misreadings` に
  - `Cross-subject transfer initialization means the decoder is participant-invariant or already durable`
  という誤読と、その降格規則を追加しました。
- `Operating rules` にも route-typing rule を追加しました。
- references に
  - Willett et al. (2023)
  - Singh et al. (2025)
  を追加しました。

### `verification.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` に、侵襲的 language BCI の route typing を明記しました。
- language decode の table に `communication route type / temporal claim` 行を追加しました。
- `Invasive language BCIs are not one temporal-validity route either` note を追加し、同じ split が verification policy 側でも必要であることを明文化しました。
- `Co-Adaptation Log` の要求項目に、侵襲的 language / speech BCI では
  - throughput / expressivity
  - transfer initialization
  - bounded fixed-decoder slice
  - adaptive rescue
  のどれとして読んでいるのかを明示する rule を追加しました。
- references に
  - Singh et al. (2025)
  - Karpowicz et al. (2025)
  を追加しました。

## 今回止めた誤読

- `cross-subject transfer` がそのまま `participant-invariant decoding` を意味する
- `streaming voice output` がそのまま `fixed-decoder durability` を意味する
- `adaptive rescue` がそのまま `drift disappeared` を意味する
- `speech BCI` 文献群が 1 本の monotonic ladder を構成している

## external dependency tasks

- なし。
  - 今回の主作業は一次文献確認、repo 内文書更新、ローカル build 検証、Git 操作で完結できます。

## 参考文献

1. Willett FR, Avansino DT, Hochberg LR, Henderson JM, Shenoy KV. A high-performance speech neuroprosthesis. *Nature*. 2023.
   - https://doi.org/10.1038/s41586-023-06377-x
2. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
3. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
4. Singh A, Thomas T, Li J, et al. Transfer learning via distributed brain recordings enables reliable speech decoding. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-63825-0
5. Karpowicz BM, O'Shea DJ, Wyche S, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
6. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
