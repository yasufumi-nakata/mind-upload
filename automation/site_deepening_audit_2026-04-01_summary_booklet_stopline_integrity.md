# Site Deepening Audit (2026-04-01, summary booklet stop-line integrity)

## 対象

- 主対象:
  - `summary_booklet.md`
- 実装対象:
  - `scripts/build_summary_booklet.rb`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://mind-upload.com/summary_booklet.html`
- `https://mind-upload.com/verification.html`
- `https://mind-upload.com/wiki/human-proxy-composition.html`
- `https://mind-upload.com/wiki/state-continuity-bridge.html`
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC5075629/`
- `https://pubmed.ncbi.nlm.nih.gov/38997157/`
- `https://www.nature.com/articles/s41467-025-66124-w`
- `https://www.nature.com/articles/s41467-026-68374-8`

## 今回この箇所を選んだ理由

- 2026-03-25 以降の深掘りで、公開ページ本体の stop line はかなり精密になっておりました。
- しかし 2026-04-01 時点の live `summary_booklet.html` では、最上段の要約がなお
  - `Current Focus Connectome-complete does not mean emulation-complete; mis…`
  - `Primary Entry Mind-Upload / Verification: Mind Uploading Verification C…`
  - `What It Does Not Claim Yet ... Human evidence is layered: local ultrastructure, synaptic-d…`
  のように、**科学的に最も落としてはいけない語** を途中で切っておりました。
- これは単なる見た目の問題ではございません。`verification.html` は live site 上でも
  - Human Proxy Composition Card による `effective time window / state axis`
  - `agreement / disagreement topology`
  - `proxy class / operational maturity / calibrator role`
  を要求しており、
  `wiki/human-proxy-composition.html` は
  - `same-session acquisition does not erase effective-window mismatch`
  を明記し、
  `wiki/state-continuity-bridge.html` は
  - `Same-subject solves specimen identity, not same-state continuity`
  を front door で固定しております。
- つまり site 本体が維持している科学的 stop line を、summary booklet 側の blind truncation が再圧縮して再流入させていた、というのが今回の主要欠陥でございました。

## 主要結論

- もっと深掘りして更新すべき箇所として、今回は **`summary_booklet` の stop-line 保全** を選ぶのが最も合理的でございました。
- 理由は、ここが public front door の一枚要約であり、技術ページで分けた inferential objects を、文字数都合で再結合してしまうと、読者が最初に受け取る情報が再び
  - `connectome ~= state completeness`
  - `human evidence ~= near-direct readout`
  - `same-subject ~= same-state`
  - `proxy-rich ~= state closure`
  に傾くためでございます。
- したがって必要だったのは、新しい topic を増やすことよりも、**既に site 全体で確立済みの stop line を summary surface で壊さないこと** でございました。

## 根拠付き批判

### 1. live booklet は stop line を「短くする」のではなく「壊して」おりました

- web 上の live `summary_booklet.html` では、
  - `Current Focus` が `Connectome-complete does not mean emulation-complete; mis…`
  - `What It Does Not Claim Yet` が `Human evidence is layered: local ultrastructure, synaptic-d…`
  のように切れておりました。
- これでは短縮ではなく、**どの latent family / proxy family / bridge rule を止めているのか** が失われます。

批判:

- 科学ページの summary で mid-sentence ellipsis が危険なのは、ここで削れるのが冗長説明ではなく、判定境界だからでございます。
- `synaptic-density PET` の後ろに続く quantity / role split、`same-subject` の後ろに続く bridge validation rule、`proxy-rich` の後ろに続く compatibility / disagreement rule が落ちると、残るのはただの progress slogan でございます。

### 2. human proxy の stop line は、いまや quantity / time window / model burden まで分離しないと意味をなしません

- [Johansen et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/38997157/) は、healthy humans で `SV2A` を用いた high-resolution atlas を構築した atlas route でございます。
- [Lucchetti et al. (2025)](https://www.nature.com/articles/s41467-025-66124-w) は、`51 healthy subjects` と `independent sample (N = 13)` で `five metabolites` による parcel-level metabolic similarity object を定義しております。
- [Dagum et al. (2026)](https://www.nature.com/articles/s41467-026-68374-8) は、`clinical randomized crossover study` と `compartmental pharmacokinetic model` と `investigational device` を併用して overnight biomarker efflux を推定しております。

批判:

- これらは同じ `human evidence` ではございません。
- direct observable, time window, spatial unit, model burden, and safe bundle role が違うため、public summary で `human evidence is layered` を途中で切ることは、現在の一次文献が要求する technical distinction をそのまま破壊いたします。

### 3. same-session / same-subject の stop line は temporal object を保持して初めて意味を持ちます

- [Nguyen et al. (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5075629/) は本文で `the issue of temporal mismatch between EEG-fMRI still persists` と明記しております。
- live `verification.html` でも `Fusion Card` は `effective-window / temporal-kernel relation` を要求しております。
- live `wiki/human-proxy-composition.html` でも `same-session acquisition does not erase effective-window mismatch` が front matter の要点として前景化されております。
- live `wiki/state-continuity-bridge.html` でも `Same-subject solves specimen identity, not same-state continuity` が最初に固定されております。

批判:

- したがって `same-subject wording does not make one state sample` や `effective-window mismatch` は、現在の site では mere nuance ではなく front-door rule でございます。
- それにもかかわらず booklet 表紙でこの rule が落ちると、最初の一枚要約が本体ページの verification policy に逆行してしまいます。

### 4. blind truncation は technical prioritization を無視します

- `scripts/build_summary_booklet.rb` の旧実装は、cover band と cover card に対して固定文字数 `shorten(...)` を適用しておりました。
- そのため、technical stop line の重要度に関係なく、文頭から文字数で切るだけの振る舞いになっておりました。

批判:

- 技術・自然科学の観点では、summary generation でも
  - 何を全文保持すべきか
  - どの stop line を compact paraphrase に置き換えるか
  - どこまで sentence boundary を守るか
  は意味論に属します。
- よって blind truncation は formatting ではなく **epistemic bug** でございました。

## 今回実行した変更

### `scripts/build_summary_booklet.rb`

- `COMPACT_STOPLINE_RULES` を追加し、次の高優先 stop line は mid-sentence truncation せず、短くても意味を壊さない完全文へ変換するようにしました。
  - `Connectome-complete is not emulation-complete.`
  - `Human evidence remains layered and proxy-based.`
  - `Same-subject wording does not make one state sample.`
  - `Proxy bundles need compatibility, repeatability, and disagreement audits.`
  - `High decode scores can still be shortcut-driven.`
  - `Same-day success is not a cross-day or long-term claim.`
- `COMPACT_TITLE_MAP` を追加し、cover band の `Primary Entry` が `Verification Commons` まで見えるようにしました。
- `cover_band_html` を修正し、`Current Focus` と `Primary Entry` を compact full-form に差し替えました。
- `cover_cards_html` を修正し、`What It Does Not Claim Yet` を blind-truncated paragraph から、stop line を保持する bullet list へ変更しました。
- `render_cards` を修正し、list HTML を card 内にそのまま出せるようにしました。
- `shorten` を修正し、一般短縮でも
  - sentence boundary を優先し、
  - それが無理でも word boundary で切る
  ようにして、`what this site is try…` のような mid-word truncation を止めました。

### `summary_booklet.md`

- 表紙 `Current Focus` を `Connectome-complete is not emulation-complete.` に更新しました。
- 表紙 `Primary Entry` を `Mind-Upload -> Verification Commons` に更新しました。
- `What It Does Not Claim Yet` を次の 4 行の stop-line list に更新しました。
  - `Connectome-complete is not emulation-complete.`
  - `Human evidence remains layered and proxy-based.`
  - `Same-subject wording does not make one state sample.`
  - `Proxy bundles need compatibility, repeatability, and disagreement audits.`
- Contents / overview / page tablesでも、文章が単語途中で切れないよう再生成しました。

## 今回止めた誤読

- `connectome-complete` の後ろに残る hidden-state ceiling が略記で消えても問題ない
- `human evidence` は generic human progress label として短縮してよい
- `same-subject` の stop line は booklet 表紙では落としてよい
- `proxy-rich` の stop line は booklet 冒頭では不要
- summary layer の truncation は purely visual issue であり、scientific reading rule には影響しない

## 検証

- `ruby scripts/build_summary_booklet.rb`
  - 成功
- `sed -n '20,90p' summary_booklet.md`
  - cover band / cover card の stop line が完全文で出力されることを確認
- `git diff -- scripts/build_summary_booklet.rb summary_booklet.md`
  - 修正が generator と generated output の双方に限定されていることを確認
- 次段の build 検証:
  - `bundle exec jekyll build`
  - `git diff --check`
  - `_site/summary_booklet.html` 上で ellipsis の置換確認

## external dependency tasks

- なし
  - 今回の主作業は、live site の web 確認、generator 修正、summary regeneration、build / diff 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Johansen A, Beliveau V, Colliander E, et al. An In Vivo High-Resolution Human Brain Atlas of Synaptic Density. *Journal of Neuroscience*. 2024.
   - https://pubmed.ncbi.nlm.nih.gov/38997157/
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025.
   - https://www.nature.com/articles/s41467-025-66124-w
3. Nguyen T, Potter T, Nguyen T, Karmonik C, Grossman R, Zhang Y. EEG Source Imaging Guided by Spatiotemporal Specific fMRI: Toward an Understanding of Dynamic Cognitive Processes. *Neural Plasticity*. 2016.
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC5075629/
   - https://doi.org/10.1155/2016/4182483
4. Dagum A, Ellingson B, Aran A, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://www.nature.com/articles/s41467-026-68374-8
