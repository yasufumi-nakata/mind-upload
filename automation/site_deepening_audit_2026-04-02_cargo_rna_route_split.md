# Site Deepening Audit (2026-04-02, cargo RNA route split)

## 対象

- 主対象:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `verification.md`
  - `wbe_101.md`
  - `index.md`
- 同期対象:
  - `github-wiki-export/homeostatic-plasticity-and-maintenance-state.md`
- web確認対象:
  - `https://mind-upload.com/`
  - `https://mind-upload.com/wbe_101.html`
  - `https://mind-upload.com/verification.html`
  - `https://mind-upload.com/wiki/homeostatic-plasticity-and-maintenance-state.html`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- 既存サイトは `cargo-transport / cytoskeletal trafficking` を独立 hidden-state family として立てるところまでは到達しておりました。
- しかし `cargo` family の RNA 側はまだ
  - `RNA cargo localization / local translation support`
  - `axonal RNA localization`
  という粗い書き方に留まり、`dendritic / synaptic RNA-granule organization` と `axonal RNA localization / presynaptic mRNA targeting` の区別が前面では十分に見えておりませんでした。
- この圧縮は技術・自然科学の観点で危険でございます。なぜなら、
  - object
  - compartment
  - transport phase
  - functional target
  - observability ceiling
  が別だからでございます。

## 主要結論

- 今回もっとも改善優先度が高かったのは、新しい cargo paper を足すことではなく、`cargo RNA routes を dendritic / synaptic side と axonal side に分けること` でございました。
- 一次文献に照らすと、少なくとも以下は同じ row として読んではいけません。
  - dendritic mRNA localization required for long-term memory
  - synaptic RNA-granule trafficking / clustering
  - dendritic lncRNA transport and spine recruitment
  - axonal RNA localization in a mature in vivo memory circuit
- よって front door (`index.md`, `wbe_101.md`) と route card (`wiki/homeostatic-plasticity-and-maintenance-state.md`, `verification.md`) の双方で、この split を visible にする必要がございました。

## 根拠付き批判

### 1. 現行記述は RNA cargo route を still too coarse にまとめておりました

- `index.md`、`wbe_101.md`、`verification.md`、`wiki/homeostatic-plasticity-and-maintenance-state.md` はいずれも cargo family をかなり良く整理できておりました。
- しかし RNA 側は主として
  - `RNA cargo localization / local translation support`
  - `axonal RNA localization`
  のように読みうる書き方でございました。

批判:

- このままでは、読者が
  - dendritic / synaptic RNA condensate organization
  - axonal presynaptic mRNA targeting
  を同じ inferential object と誤読します。
- それは cargo route card の目的、すなわち `what exactly moved, where, and in which phase` を固定する運用と整合いたしません。

### 2. 一次文献は dendritic / synaptic RNA route と axonal RNA route を別 object として扱っております

- [Nakayama et al. (2017)](https://doi.org/10.7554/eLife.29677) は、`RNG105 / Caprin1-dependent dendritic mRNA localization` が long-term memory formation に必須であることを示しました。
- [Liau et al. (2023)](https://doi.org/10.1038/s41467-023-43535-1) は、synaptic Gas5 isoform が `activity-dependent trafficking and clustering of RNA granules` を制御し、fear-extinction memory に必要であることを示しました。
- [Espadas et al. (2024)](https://doi.org/10.1038/s41467-024-46972-8) は、SLAMR が `KIF5C-dependent dendritic transport` と `synaptic recruitment upon stimulation` を受け、translation / CaMKII activity / contextual-fear consolidation に関与することを示しました。
- [de Queiroz et al. (2025)](https://doi.org/10.1038/s41467-025-57651-7) は、`axonal RNA localization` が mature in vivo memory circuit で long-term memory に必要だが short-term memory には不要であることを示しました。

批判:

- これらは全て `RNA cargo` に属しえますが、
  - dendrite or synapse versus axon
  - granule trafficking / clustering versus localization to presynaptic terminals
  - spine-targeted recruitment versus axonal compartment targeting
  が異なります。
- したがって `RNA cargo localization` を一行で止めると、compartment と transport phase の差が消えます。

### 3. この圧縮を放置すると、postsynaptic-local route が presynaptic route へ誤昇格します

- Gas5 / SLAMR side の文献が直接示すのは
  - synaptic compartment
  - dendritic transport
  - granule mobility / clustering
  - spine recruitment
  でございます。
- de Queiroz side の文献が直接示すのは
  - presynaptic terminals of memory neurons
  - axonal targeting
  - transport-factor-dependent localization
  - long-term memory consolidation
  でございます。

批判:

- よって `synaptic RNA granule paper exists` を `axonal presynaptic mRNA targeting is partly fixed` と読むのは過剰主張でございます。
- 逆に `axonal RNA localization` を見て `dendritic / synaptic RNA condensate organization` まで閉じたと読むのも誤りでございます。

### 4. verification 側で claim family にこの split がなければ、実務上また圧縮されます

- `verification.md` の state-variable gate は site-wide 運用ルールでございます。
- claim family の列に
  - dendritic / synaptic RNA-granule organization
  - axonal RNA localization / presynaptic mRNA targeting
  の両方が出ていなければ、投稿物の監査で再び `RNA transport` へ圧縮されやすくなります。

批判:

- したがって front door だけでなく verification row も同期的に直す必要がございました。

## 今回実行した変更

- `index.md`
  - cargo evidence bullet を `dendritic / synaptic RNA-granule organization` と `axonal RNA localization` に分割しました。
  - cargo note-box に `Nakayama / Liau / Espadas / de Queiroz` を加え、RNA route の compartment split を明示しました。
- `wbe_101.md`
  - `last_updated` を `2026-04-02` に更新しました。
  - cargo note-box を同じ split に合わせて改稿しました。
  - bibliography に `Nakayama / Liau / Espadas` を追加しました。
- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `last_updated` を `2026-04-02` に更新しました。
  - page highlights と route-family summary を `dendritic / synaptic RNA-granule organization` と `axonal RNA localization` の二分法へ更新しました。
  - cargo section 本文、route-card intro、claim-family row、why-this-route-card note を改稿しました。
  - bibliography に `Nakayama / Liau / Espadas` を追加しました。
- `verification.md`
  - cargo route row の claim family を同じ split へ更新しました。
  - cargo addendum の critique を更新しました。
  - bibliography に `Nakayama / Liau / Espadas` を追加しました。

## 今回止めた誤読

- `RNA cargo localization` = one cargo-RNA row
- `synaptic RNA granule trafficking` = `axonal RNA localization`
- `dendritic lncRNA transport` = `presynaptic mRNA targeting`
- `local translation support paper` = compartment-complete RNA delivery evidence

## 検証予定

- `ruby scripts/export_github_wiki.rb`
  - wiki export を同期
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 公開静的サイトを再生成
- `git diff --check`
  - パッチ破損や余計な空白がないことを確認

## 外部依存タスク

- なし
  - 今回の作業は、一次資料確認、repo 内ページ改稿、export 同期、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Nakayama K, Ohashi R, Shinoda Y, et al. RNG105/caprin1, an RNA granule protein for dendritic mRNA localization, is essential for long-term memory formation. *eLife*. 2017;6:e29677.
   - https://doi.org/10.7554/eLife.29677
2. Liau W-S, Zhao Q, Bademosi A, et al. Fear extinction is regulated by the activity of long noncoding RNAs at the synapse. *Nature Communications*. 2023;14:7616.
   - https://doi.org/10.1038/s41467-023-43535-1
3. Espadas I, Wingfield JL, Nakahata Y, et al. Synaptically-targeted long non-coding RNA SLAMR promotes structural plasticity by increasing translation and CaMKII activity. *Nature Communications*. 2024;15:2694.
   - https://doi.org/10.1038/s41467-024-46972-8
4. de Queiroz BR, Laghrissi H, Rajeev S, Blot L, De Graeve F, Dehecq M, Keleman K, Ule J, Hubstenberger A, Besse F. Axonal RNA localization is essential for long-term memory. *Nature Communications*. 2025;16:2560.
   - https://doi.org/10.1038/s41467-025-57651-7
