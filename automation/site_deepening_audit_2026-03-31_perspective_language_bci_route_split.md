# Site Deepening Audit (2026-03-31, perspective language-BCI route split)

## 対象

- 主対象:
  - `perspective.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.1038/s41586-023-06377-x`
- `https://doi.org/10.1038/s41593-025-01905-6`
- `https://doi.org/10.1038/s41586-025-09127-3`
- `https://doi.org/10.1038/s41467-025-63825-0`
- `https://doi.org/10.1038/s41467-025-59652-y`
- `https://doi.org/10.1038/s41551-025-01536-z`

## 今回この箇所を選んだ理由

- site-wide rule としては、すでに
  - `throughput / expressivity`
  - `transfer initialization`
  - `fixed-decoder durability`
  - `adaptive rescue / recalibration`
  を別の operational slice として扱う方向が
  - `wbe_101.md`
  - `tech_roadmap.md`
  - `wiki/decode-vs-emulate.md`
  - `wiki/state-trait-and-drift.md`
  で成立しておりました。
- しかし `perspective.md` の language section では、なお `invasive streaming speech neuroprosthesis` が 1 行で処理されており、central synthesis page としては停止線が弱うございました。
- この圧縮を放置すると、読者は
  - communication throughput
  - voice expressivity
  - cross-subject transfer
  - chronic rescue
  を一つの monotonic route と読みやすくなります。

## 根拠付き批判

### 1. throughput / expressivity と transfer initialization は同じ進歩ではございません

- [Willett et al. (2023)](https://doi.org/10.1038/s41586-023-06377-x) は large-vocabulary speech-to-text を前進させました。
- [Littlejohn et al. (2025)](https://doi.org/10.1038/s41593-025-01905-6) は online large-vocabulary brain-to-voice synthesis を `80-ms increments` で前進させました。
- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は instantaneous voice synthesis と paralinguistic control、silence fallback を前進させました。
- これに対して [Singh et al. (2025)](https://doi.org/10.1038/s41467-025-63825-0) は、distributed intracranial recordings を使った `cross-subject transfer learning framework` により、shared latent manifolds と individual model initialization を扱っております。

批判:

- 前三者が主に前進させたのは `communication throughput / expressivity` でございます。
- Singh は `subject initialization under heterogeneous coverage` を前進させたのであり、同じ evidence object ではございません。
- したがって central page で 1 行に圧縮すると、何が improved communication で何が improved initialization なのかが崩れます。

### 2. transfer initialization と adaptive rescue も同じ進歩ではございません

- [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) は、latent-dynamics alignment による stabilization を示しました。
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は、hidden-Markov-model による target-inference recalibration を使い、closed loop over one month と offline five-year dataset を通じた unsupervised recalibration route を示しました。

批判:

- これらは `decoder stayed valid as-is` を示しているのではなく、`performance can be rescued or maintained under a named adaptation strategy` を示しているにすぎません。
- よって `transfer worked` と `long-term operation worked` の間には、なお `what adaptation was required` という大きな隔たりがございます。

### 3. adaptive rescue は fixed-decoder durability と同義ではございません

- Wilson の abstract 自体が、intracortical BCI は neural activity の変化により frequent recalibration を要し、そこで hidden-Markov-model による unsupervised adaptation を入れていることを明示しております。
- Karpowicz も `alignment of latent dynamics` を stabilization 手段として前景化しており、fixed decoder が drift free であるとは言っておりません。

批判:

- したがって `rescue succeeded` を `fixed decoder was durable` と読み替えるのは不正確でございます。
- public wording には少なくとも
  - `fixed decoder interval`
  - `time since last supervised calibration`
  - `stabilization / alignment strategy`
  - `recalibration burden`
  を separate field として残す必要がございます。

### 4. central synthesis page が 1 行要約のままだと、他ページで成立している厳密さを打ち消します

- `wbe_101.md` ではすでに invasive language BCI を sharper split で読んでおります。
- `wiki/decode-vs-emulate.md` と `wiki/state-trait-and-drift.md` でも、fixed-decoder horizon と recalibration burden を別物として扱っております。
- それにもかかわらず `perspective.md` が 1 行の `speech neuroprosthesis` に留まると、読者は central page で再び `speech BCI progress = one ladder` と読み得ます。

批判:

- central page は supporting wiki より緩くてはなりません。
- 今回の修正は、site-wide rule を `perspective.md` に再同期する意味を持ちます。

## 今回実行した変更

### `perspective.md`

- front matter の `note` に `2026-03-31 invasive-language-BCI route split` を追記しました。
- `page_highlights` と `known_points` に、invasive language BCI が
  - throughput / expressivity
  - transfer initialization
  - fixed-decoder durability
  - adaptive rescue
  の別 slice であることを追加しました。
- language section 冒頭の総論 paragraph を改稿し、invasive side を一つの route としてではなく、上記 split を伴う route family として書き換えました。
- evidence table の `invasive streaming speech neuroprosthesis` row を `Invasive language-BCI route family` に改稿しました。
- `2026-03-31 correction: invasive language BCIs are not one operational route on this page either` note-box を追加しました。
- 直下に 3 行の sub-route table を追加し、
  - throughput / expressivity
  - transfer initialization
  - adaptive rescue / recalibration
  を分離しました。
- `Minimum required evaluation pack` に `Longitudinal operation split` bullet を追加し、
  - fixed decoder interval
  - time since last supervised calibration
  - stabilization / alignment strategy
  - unit-identity or channel-stability audit
  を要求する形へ更新しました。
- `Operation rules on Mind-Upload side` に `Route typing for invasive language BCIs` を追加し、L3 条件にも `fixed decoder interval` と `time since last supervised calibration` を明記しました。
- reference list の `Littlejohn et al. (2025)` を official citation に合わせて
  - `Cho, Liu, et al.`
  - `Nat Neurosci 28, 902–912`
  へ修正しました。
- 新規 reference として
  - `Singh et al. (2025)`
  - `Karpowicz et al. (2025)`
  - `Wilson et al. (2025)`
  を追加しました。

## 今回止めた誤読

- `speech BCI progress` = one monotonic ladder
- `throughput / expressivity` = `generic transfer`
- `transfer initialization` = `fixed-decoder durability`
- `adaptive rescue` = `no-recalibration chronic stability`
- `one strong invasive paper exists` = `the chronic operational problem is basically solved`

## 検証予定

- `git diff --check`
- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `bundle exec jekyll build`
- `git diff --stat`

## external dependency tasks

- なし
  - 今回の作業は web 文献確認、repo 内改稿、検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023;620:1031-1036.
   - https://doi.org/10.1038/s41586-023-06377-x
2. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025;28:902-912.
   - https://doi.org/10.1038/s41593-025-01905-6
3. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025;644:145-152.
   - https://doi.org/10.1038/s41586-025-09127-3
4. Singh A, Thomas T, Li J, et al. Transfer learning via distributed brain recordings enables reliable speech decoding. *Nature Communications*. 2025;16:8749.
   - https://doi.org/10.1038/s41467-025-63825-0
5. Karpowicz BM, Ali YH, Wimalasena LN, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025;16:4662.
   - https://doi.org/10.1038/s41467-025-59652-y
6. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
