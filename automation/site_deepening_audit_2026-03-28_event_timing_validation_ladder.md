# Site Deepening Audit (2026-03-28, event timing validation ladder)

## 対象

- 主対象: `wiki/event-sync-and-measurement-logs.md`
- 同期対象: `datasets.md`
- 派生同期: `summary_booklet.md`

## web確認対象

- `https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html`
- `https://doi.org/10.1038/s41597-025-05791-2`
- `https://doi.org/10.1162/imag.a.136`
- `https://doi.org/10.3758/s13428-024-02508-y`
- `https://doi.org/10.7717/peerj.9414`

## 今回この箇所を選んだ理由

- `datasets.md` は 2026-03-28 時点でも実践入口として強い一方、そこから参照される `wiki/event-sync-and-measurement-logs.md` は `last_updated: 2026-03-15` のままでした。
- 技術・自然科学の観点では、ここは誤読コストが大きいです。L0/L1 実践で最初に起こる失敗は、しばしば「event がある」「LSL を使った」「trigger を入れた」を同じ timing evidence と読んでしまうことだからです。
- 現行サイトは `LSL は hardware ground truth ではない` までは既に書けていましたが、`stored-data anchor`、`stream alignment`、`digital marker capture`、`physical output onset`、`uncontrolled-response timing` をまだ site-wide card として十分に分離していませんでした。

## 根拠付き批判

### 1. BIDS の `onset` は physical onset そのものではありません

- 根拠:
  - [BIDS Specification: Events](https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html) は `onset` / `duration` / `sample` を保存データ上の event anchor として定義します。
  - これは比較可能な container として重要ですが、表示装置・音声装置・ボタン応答の physical onset truth まで自動で固定する仕様ではありません。
- 批判:
  - したがって `events.tsv がある = stimulus timing が physical world で保証された` と読むのは弱いです。
  - BIDS は `stored-data anchor` の床であって、timing validation ladder の最終段ではありません。

### 2. HED は event semantics を強めますが、hardware latency truth までは与えません

- 根拠:
  - [Hermes et al. (2025)](https://doi.org/10.1038/s41597-025-05791-2) は HED library schema により EEG annotation を machine-actionable に整理できることを示しました。
  - これは `trial_type` や SCORE 系 annotation の意味論を固定する重要な前進です。
- 批判:
  - しかし、semantics が machine-readable になったことと、timing が physical truth に較正されたことは別問題です。
  - `meaning is fixed` と `latency is validated` を同じ欄に入れる構造は、科学的には粗すぎます。

### 3. LSL は stream alignment を強めますが、device-side delay を自動で消しません

- 根拠:
  - [Kothe et al. (2025)](https://doi.org/10.1162/imag.a.136) は、LSL が cross-device offset / drift / jitter 補償を含む synchronized multimodal recording infrastructure として有効である一方、残余の setup offset は実機での testing が必要であることを明記しました。
  - 同論文は display/input latency について photodiode や high-frame-rate camera など外部計測の必要性も述べています。
- 批判:
  - したがって `LSL を使った = timing は十分` という読みは誤りです。
  - LSL が強めるのは `stream alignment` であり、`physical onset truth` や `response timing truth` ではありません。

### 4. 物理刺激時刻と応答時刻は、外部実測クラスで別々に監査しなければなりません

- 根拠:
  - [Lepauvre et al. (2024)](https://doi.org/10.3758/s13428-024-02508-y) は、event-based experiment の timing を photodiode と microphone で検証し、log file timestamps と actual physical events を比較して平均ズレと標準偏差を報告する標準化枠組みを提示しました。
  - [Bridges et al. (2020)](https://doi.org/10.7717/peerj.9414) は、popular experiment generators でも package / OS / browser により visual, audio, response timing precision が変動することを示し、各自の環境で timing validation を行う必要性を強調しました。
- 批判:
  - `TTL marker がある` と `screen 上の actual onset を photodiode で測った` は同じ証拠ではありません。
  - 同様に `button timestamp が記録された` と `actual button press timing を microphone / loopback で検証した` も別問題です。
  - 現行ページの `LSL / TTL / photodiode / loopback` を同じ `sync evidence` 欄に置く構造は、今の一次文献の切り分けに追いついていませんでした。

## 今回実行した変更

- `wiki/event-sync-and-measurement-logs.md`
  - `last_updated` を `2026-03-28` に更新
  - front matter の `accuracy_note` / `page_highlights` / `known_points` を、timing validation class の分離に同期
  - `2026-03-28 re-audit: timing evidence still needed a ladder` note を追加
  - `Timing validation is a ladder, not one box` 節を新設し、
    - stored-data anchor
    - stream alignment
    - acquisition-side digital marker capture
    - physical output onset
    - uncontrolled-response timing
    の 5 段を分離
  - `Event Fidelity Card` を 6 項目へ拡張し、`clock domain and stream alignment` と `timing validation class` を分離
  - `Information that is difficult to restore later` に `timing validation class` を追加
  - 参考文献に Lepauvre et al. (2024) と Bridges et al. (2020) を追加

- `datasets.md`
  - `last_updated` を `2026-03-28` に更新
  - `page_highlights` / `known_points` に timing validation class の split を追加
  - `Event Fidelity Card now required` の要件を 7 項目へ更新し、
    - clock domain plus stream-alignment rule
    - timing-validation class
    を別 field として要求
  - `The most important site rule to add now` の dataset card 要件を 8 項目へ更新
  - checklist と L0 loop の `Event fidelity` / `Metadata` を timing validation ladder に同期

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成し、`datasets.md` の更新を冊子に反映

## 今回の修正で止めた誤読

- `events.tsv がある` = `physical stimulus onset が検証済み`
- `HED で semantics が固定された` = `hardware latency まで監査済み`
- `LSL を使った` = `display / audio / response timing まで ground-truth 化された`
- `TTL marker がある` = `screen/audio/button の actual onset が分かった`
- `response timestamp がある` = `actual response timing precision が分かった`

## 外部依存タスク

- なし
  - 今回の変更は、公開本文・派生要約・監査記録の更新で完結しています。

## 参考文献

1. Brain Imaging Data Structure. BIDS Specification: Events.
   - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html
2. Hermes D, Pal Attia T, Beniczky S, et al. Hierarchical Event Descriptor library schema for EEG data annotation. *Scientific Data*. 2025.
   - https://doi.org/10.1038/s41597-025-05791-2
3. Kothe C, Medine D, Grivich M, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
   - https://doi.org/10.1162/imag.a.136
4. Lepauvre A, Hirschhorn R, Bendtz K, Mudrik L, Melloni L. A standardized framework to test event-based experiments. *Behavior Research Methods*. 2024;56(8):8852-8868.
   - https://doi.org/10.3758/s13428-024-02508-y
5. Bridges D, Pitiot A, MacAskill MR, Peirce JW. The timing mega-study: comparing a range of experiment generators, both lab-based and online. *PeerJ*. 2020;8:e9414.
   - https://doi.org/10.7717/peerj.9414
