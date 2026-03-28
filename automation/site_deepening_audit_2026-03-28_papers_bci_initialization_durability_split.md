# Site Deepening Audit (2026-03-28, papers/research-harvest invasive speech BCI initialization-durability split)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1038/s41586-023-06377-x`
- `https://doi.org/10.1038/s41593-025-01905-6`
- `https://doi.org/10.1038/s41586-025-09127-3`
- `https://doi.org/10.1056/NEJMoa2314132`
- `https://doi.org/10.1038/s41467-025-63825-0`
- `https://doi.org/10.1038/s42003-024-06784-4`
- `https://doi.org/10.1038/s41467-025-59652-y`
- `https://doi.org/10.1038/s41551-025-01536-z`

## 今回この箇所を選んだ理由

- `mind_uploading_papers.md` と `research_harvest_50.md` は、技術系読者がまず触る文献入口でございます。
- しかし 2026-03-28 時点でも、この入口は侵襲型 speech BCI をなお粗く束ねており、
  - communication throughput / expressivity
  - decoder initialization
  - fixed-decoder durability
  - adaptive rescue
  を十分に別 object として固定できておりませんでした。
- 入口でこの圧縮が残ると、他ページで止めている誤読が再注入されます。

## 根拠付き批判

### 1. fluent output は initialization の改善と同じ成果ではありません

- [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x)、[Littlejohn et al. (2025)](https://doi.org/10.1038/s41593-025-01905-6)、[Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は、same-session の communication throughput / expressivity を強く押し上げました。
- 一方で [Card et al. (2024)](https://doi.org/10.1056/NEJMoa2314132) は rapid same-subject calibration を、[Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) は cross-subject transfer-assisted initialization を強めています。

批判:

- `話せた / 速かった` を、そのまま `短時間で立ち上がった` や `subject-general に初期化できた` と読むのは技術的に誤りでございます。
- communication route と initialization route は別に監査すべきでございます。

### 2. initialization が良くても、fixed-decoder durability は別問題でございます

- [Pun et al. (2024)](https://doi.org/10.1038/s42003-024-06784-4) は、chronic human iBCI で instability / model drift が performance degradation と強く結びつくことを示しました。
- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) も、expressive voice synthesis を示しつつ fixed-decoder slice の低下を別に報告しています。

批判:

- `短く calibrate できた`、`transfer で初期性能が出た` は、`fixed decoder が日単位・週単位で持続した` を意味しません。
- したがって入口ページが initialization と durability を同列に束ねるのは弱いです。

### 3. adaptive rescue は fixed-decoder validity の証拠ではありません

- [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) は latent-dynamics alignment による stabilization を示しました。
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は one-month unsupervised recalibration と five-year offline characterization を示しました。

批判:

- これらが強めるのは rescue route であって、元の decoder が drift しなかったという主張ではございません。
- `rescue succeeded` を `fixed decoder remained valid` と読むのは主張のすり替えでございます。

### 4. 文献入口ページこそ、この split を最初に持つ必要がございます

- `faq.md`、`wbe_101.md`、`tech_roadmap.md`、`verification.md` は、すでに invasive language BCI を圧縮読解しない方向へ更新済みでございます。
- それにもかかわらず、paper/archive 側で `invasive communication` を大きく一塊に残すと、詳細ページの stop line が入口で弱まります。

批判:

- 文献入口ページが `何を直接強めた論文か` を先に分けない構造は、site-wide governance として不整合でございました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `known_points` / `page_highlights` を、侵襲型 BCI の four-way split に更新しました。
  - technical addendum の invasive BCI correction を改稿し、
    - communication throughput / expressivity
    - decoder initialization
    - fixed-decoder durability
    - adaptive rescue
    を別 route として明文化しました。
  - `technical-fast-lane` の導入文を更新し、initialization と fixed-decoder horizon を分離しました。
  - shortlist table を再編し、
    - `Invasive speech neuroprosthesis / communication throughput`
    - `Decoder initialization / transfer-assisted route`
    - `Fixed-decoder durability / instability audit`
    - `Adaptive stabilization / recalibration route`
    を独立 row として追加しました。
  - invasive BCI note-box を `durability split` から `operational-route split` に改稿し、Card 2024 と Pun 2024 を加えました。
  - `technical-evidence-classes` を更新し、`decoder initialization / transfer` と `fixed-decoder durability / instability audit` を独立 class として追加しました。
  - 読み始め案内表に `decoder initialization / transfer safely` の row を追加しました。

- `research_harvest_50.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `page_highlights` / `known_points` に invasive language BCI の four-way split を追加しました。
  - priority route table に `BCI initialization route` を追加し、long-horizon closed-loop stability row を durability / instability まで読む形へ更新しました。
  - `U13: Mimic separation` の traction bullet、代表文献、technical note を更新し、communication / initialization / durability / rescue を分離しました。

## 今回止めた誤読

- `speech BCI demo が速い` = `decoder initialization も solved`
- `rapid calibration` = `fixed decoder が durable`
- `cross-subject transfer が効く` = `subject-general everyday speech が solved`
- `instability を測れた` = `rescue も autonomy も solved`
- `adaptive recalibration が効く` = `元 decoder は十分 stable`

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
   - https://doi.org/10.1038/s41586-023-06377-x
2. Card NS, et al. An accurate and rapidly calibrating speech neuroprosthesis. *New England Journal of Medicine*. 2024.
   - https://doi.org/10.1056/NEJMoa2314132
3. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01905-6
4. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
5. Singh A, Wu E, Ramsey NF, et al. Transfer learning via distributed brain recordings enables reliable speech decoding. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-63825-0
6. Pun TK, Khoshnevis M, Hosman T, et al. Measuring instability in chronic human intracortical neural recordings towards stable, long-term brain-computer interfaces. *Communications Biology*. 2024.
   - https://doi.org/10.1038/s42003-024-06784-4
7. Karpowicz BM, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
8. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
