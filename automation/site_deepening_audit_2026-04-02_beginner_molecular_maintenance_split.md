# Site Deepening Audit (2026-04-02, beginner molecular-maintenance family split)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
- 同期対象:
  - `github-wiki-export/mind-upload-basics.md`
- web確認対象:
  - `https://mind-upload.com/wiki/mind-upload-basics.html`
  - `https://mind-upload.com/wiki/homeostatic-plasticity-and-maintenance-state.html`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- beginner front door である `wiki/mind-upload-basics.md` は、2026-04-01 までに
  - human observability の three-axis reading
  - spectroscopy / myelin / BBB / astrocyte / clearance の quantity-type split
  - glial substrate-routing と astrocyte-state の分離
  をかなり前面化できておりました。
- しかし live page を web で再確認すると、`What still remains outside these human routes` の総括はなお
  - `transcription / chromatin state`
  - `glial substrate-routing`
  - `astrocyte-network state`
  - `related maintenance controllers`
  という書き方で止まっておりました。
- これは front-door compression bug でございます。深いページ `wiki/homeostatic-plasticity-and-maintenance-state.md` ではすでに
  - `post-transcriptional RNA-state`
  - `phospho-signaling / second-messenger state`
  - `local proteostasis / synaptic-tagging state`
  - `cargo-transport / cytoskeletal trafficking state`
  が独立 family として運用されているのに、入口だけがまだ `related controllers` へ圧縮しておりました。

## 主要結論

- 今回もっとも改善優先度が高かったのは、新しい molecular paper を単に足すことではなく、`beginner page でも molecular maintenance families を独立 family として止めること` でございました。
- 一次文献に照らすと、`molecular maintenance` は beginner level でも少なくとも
  - `object family`
  - `direct observable`
  - `compartment / integration unit`
  - `timescale`
  - `human observability ceiling`
  を分けて読ませなければなりません。
- よって今回の更新対象は、site の入口として最もレバレッジが大きい `wiki/mind-upload-basics.md` が最適でございました。

## 根拠付き批判

### 1. beginner page は `transcription` を書いていても、molecular maintenance family split をまだ十分に可視化しておりませんでした

- live `mind-upload-basics.html` は 2026-04-02 JST 時点で、molecular side を `transcription / chromatin state ... and related maintenance controllers` と総括しておりました。
- 一方、deep page 側はすでに
  - post-transcriptional RNA
  - phospho-signaling
  - proteostasis / synaptic tagging
  - cargo-routing
  を別 route card で扱っております。

批判:

- 入口でこの split が visible でないと、読者は `molecular maintenance` を `transcription plus some details` と誤読します。
- その誤読は、current site-wide rule と整合いたしません。

### 2. 一次文献は transcription, RNA, phospho, proteostasis, cargo を同じ object として扱っておりません

- [Santoni et al. (2024, `10.1126/science.adg9982`)](https://doi.org/10.1126/science.adg9982) は、memory-trace allocation の前段にある `chromatin plasticity / neuronal eligibility` route でございます。
- [Terceros et al. (2026, `10.1038/s41586-025-09774-6`)](https://doi.org/10.1038/s41586-025-09774-6) は、`thalamocortical transcriptional gate` による memory stabilization route でございます。
- [Wang et al. (2015, `10.1038/nn.4069`)](https://doi.org/10.1038/nn.4069) は、`LSD1n splice-isoform / transcription-elongation control` route であり、gene-level abundance ではなく isoform-defined controller を示しました。
- [Peterson et al. (2025, `10.1126/scisignal.adr1442`)](https://doi.org/10.1126/scisignal.adr1442) は、`ADAR2-mediated GluA2 RNA editing` が homeostatic synaptic plasticity に関与する RNA-editing route でございます。
- [Vierra et al. (2023, `10.1038/s41467-023-40930-6`)](https://doi.org/10.1038/s41467-023-40930-6) は、`neuronal ER-plasma membrane junction` における `Ca2+-activated PKA signaling` の compartmentalized phospho-signaling route でございます。
- [Thomas et al. (2025, `10.1038/s42003-025-08459-0`)](https://doi.org/10.1038/s42003-025-08459-0) は、`actin dynamics / spine geometry` が synaptic-tag timescale に persist しうる proteostasis / tag-capture side の stop line を与えます。
- [Aiken & Holzbaur (2024, `10.1016/j.cub.2024.03.010`)](https://doi.org/10.1016/j.cub.2024.03.010) は、human iPSC-derived axons における `presynaptic cargo pausing / retention` と local microtubule dynamics を結びつける cargo-routing route でございます。

批判:

- これらはすべて `molecular maintenance` に属しえますが、direct observable も integration unit も timescale も異なります。
- したがって beginner page で `transcription ... and related maintenance controllers` に戻すと、
  - chromatin eligibility
  - transcriptional gate
  - RNA isoform / editing control
  - phospho nanodomain signaling
  - tag-timescale stabilization
  - cargo pausing / retention
  の非同一性を入口で消してしまいます。

### 3. human observability ceiling も family ごとに別であり、generic molecular row ではございません

- 上記 routes の多くは rodent causal route、ex vivo route、or human-derived preparation route でございます。
- [Aiken & Holzbaur (2024)](https://doi.org/10.1016/j.cub.2024.03.010) は human iPSC-derived neurons を使っておりますが、living-human whole-brain cargo-state readout ではございません。
- [Vierra et al. (2023)](https://doi.org/10.1038/s41467-023-40930-6) も local signaling nanodomain route であり、comparable living-human whole-brain phospho-state route ではございません。

批判:

- beginner page に dedicated stop rule がないと、読者は `molecular mechanism exists` を `human-compatible current-state readout is emerging` と短絡しえます。
- その short cut は current primary literature では支持されておりません。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - `last_updated` を `2026-04-02` に更新しました。
  - `page_highlights` に、transcription が molecular maintenance の全体ではないことを明示する bullet を追加しました。
  - `known_points` に、molecular maintenance が `transcription / chromatin`, `post-transcriptional RNA`, `phospho-signaling`, `proteostasis`, `cargo-routing` に split することを明示しました。
  - 新しい note-box `2026-04-02 correction: transcription is not the whole molecular maintenance layer` を追加しました。
  - `What still remains outside these human routes` を更新し、molecular maintenance family split を beginner front door でも visible にしました。
  - bibliography に `Wang / Peterson / Vierra / Thomas / Aiken` を追加しました。

## 今回止めた誤読

- `transcription / chromatin` = molecular maintenance の代表行
- `molecular maintenance` = one generic controller family
- `RNA / phospho / proteostasis / cargo` = transcription の詳細
- `human-derived preparation` = living-human whole-brain observability progress

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

1. Santoni G, Astori S, Leleu M, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024;385(6707):eadg9982.
   - https://doi.org/10.1126/science.adg9982
2. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;649(8099):1254-1263.
   - https://doi.org/10.1038/s41586-025-09774-6
3. Wang J, Telese F, Tan Y, et al. LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. *Nature Neuroscience*. 2015;18(9):1256-1264.
   - https://doi.org/10.1038/nn.4069
4. Peterson L, Kasper JM, Allgaier JA, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025;18(886):eadr1442.
   - https://doi.org/10.1126/scisignal.adr1442
5. Vierra NC, et al. Neuronal ER-plasma membrane junctions couple excitation to Ca2+-activated PKA signaling. *Nature Communications*. 2023;14:5231.
   - https://doi.org/10.1038/s41467-023-40930-6
6. Thomas M, Bogaciu C-A, Rizzoli SO, et al. Long-term potentiation-induced changes in actin dynamics and spine geometry persist on the timescale of the synaptic tag. *Communications Biology*. 2025;8:1065.
   - https://doi.org/10.1038/s42003-025-08459-0
7. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024;34(8):1687-1704.e8.
   - https://doi.org/10.1016/j.cub.2024.03.010
