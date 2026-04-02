# Site Deepening Audit (2026-04-02, literature phospho route sync)

## 対象

- 主対象:
  - `research_harvest_50.md`
  - `mind_uploading_papers.md`
- 参照した深い整合先:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `wbe_101.md`
- web確認対象:
  - `https://mind-upload.com/research_harvest_50.html`
  - `https://mind-upload.com/mind_uploading_papers.html`
  - DOI / PubMed landing pages for the cited primary papers
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- `wiki/homeostatic-plasticity-and-maintenance-state.md` と `wbe_101.md` では，phospho-signaling / second-messenger state はすでに
  - phosphosite-specific plasticity gates
  - learning-linked local phosphorylation
  - compartmentalized second-messenger / signalosome routing
  - circadian phospho-timing gate
  - region-specific phosphorylation / synapse relocalization
  - phospho-mutant causal intervention
  - human ex vivo phosphoproteome atlas ceiling
  へ分割されておりました。
- しかし，公開サイトの文献入口である `research_harvest_50.md` と `mind_uploading_papers.md` では，front door の visible stop line がまだ弱く，`phospho-signaling` が generic U3 row として読めてしまう状態でございました。
- これは front-door compression bug でございます。深いページでは禁止している圧縮が，入口ページで再発しておりました。

## 主要結論

- 今回もっとも改善優先度が高かったのは，新しい phospho paper を単に追加することではなく，`文献の入口でも phospho evidence を route-family claim として止めること` でございました。
- 一次文献に照らすと，phospho-signaling / second-messenger state は少なくとも
  - claim family
  - direct observable
  - spatial / compartment scope
  - timescale
  - causal leverage
  - human observability ceiling
  を分けて読ませなければなりません。
- よって今回の主修正は，`research_harvest_50.md` と `mind_uploading_papers.md` に phospho route-family split を明示し，core pages と front door の読解規則を同期させることでございました。

## 根拠付き批判

### 1. 入口ページの `phospho-signaling` 表記は，deep page 側の route-card rule を十分に可視化しておりませんでした

- `research_harvest_50.md` と `mind_uploading_papers.md` の front matter には phospho-signaling への言及自体はございました。
- しかし，読者の最初の停止規則としては
  - phosphosite-specific gate
  - compartmentalized signalosome
  - circadian phospho-timing
  - region-structured localization change
  - phospho-mutant causal intervention
  - ex vivo atlas ceiling
  の非同一性が十分に visible ではございませんでした。

批判:

- その結果，読者は `phospho-signaling evidence exists` を `one molecular controller row is getting covered` と誤読しえます。
- しかし site-wide の core rule は，まさにその圧縮を禁止しております。

### 2. 一次文献は phospho-signaling を単一 object として扱っておりません

- [Lee et al. (2003, `10.1016/S0092-8674(03)00122-3`)](https://doi.org/10.1016/S0092-8674(03)00122-3) は，AMPA receptor phosphosite による `bidirectional synaptic-plasticity gate` でございます。
- [Rodrigues et al. (2004, `10.1523/JNEUROSCI.5303-03.2004`)](https://doi.org/10.1523/JNEUROSCI.5303-03.2004) は，fear conditioning に伴う `learning-linked local CaMKII Thr286 phosphorylation route` でございます。
- [Havekes et al. (2016, `10.1523/JNEUROSCI.0248-16.2016`)](https://doi.org/10.1523/JNEUROSCI.0248-16.2016) は，`compartmentalized PDE4A5 signaling` による hippocampal plasticity / memory route でございます。
- [Vierra et al. (2023, `10.1038/s41467-023-40930-6`)](https://doi.org/10.1038/s41467-023-40930-6) は，neuronal ER-plasma membrane junction における `Ca2+-activated PKA signaling nanodomain` route でございます。
- [Barone et al. (2023, `10.1126/sciadv.adj1010`)](https://doi.org/10.1126/sciadv.adj1010) は，`synaptic BMAL1 phosphorylation` による circadian hippocampal plasticity gate でございます。
- [Altas et al. (2024, `10.1016/j.biopsych.2023.12.020`)](https://doi.org/10.1016/j.biopsych.2023.12.020) は，`region-specific phosphorylation` による Neuroligin-3 localization switch を mouse / human samples で示した route でございます。
- [Rodriguez et al. (2025, `10.1523/JNEUROSCI.1619-24.2025`)](https://doi.org/10.1523/JNEUROSCI.1619-24.2025) は，`single-site HDAC3 phospho-mimic / phospho-null` による causal memory intervention でございます。
- [Biswas et al. (2023, `10.1021/acs.jproteome.2c00244`)](https://doi.org/10.1021/acs.jproteome.2c00244) は，`human brain phosphoproteome atlas` による region-structured ex vivo observability route でございます。

批判:

- これらはすべて phospho-signaling に属しえますが，direct observable も causal leverage も scope も timescale も異なります。
- したがって，front door で `phospho-signaling` を generic maintenance label に戻すことは，一次文献が区別している inferential object を入口で再度潰すことになります。

### 3. human observability ceiling も phospho family ごとに別であり，generic molecular row ではございません

- [Biswas et al. (2023)](https://doi.org/10.1021/acs.jproteome.2c00244) は human brain phosphoproteome の region structure を示しますが，living-human in vivo whole-brain phosphosite occupancy readout ではございません。
- [Altas et al. (2024)](https://doi.org/10.1016/j.biopsych.2023.12.020) は mouse / human samples を使った region-specific phospho-localization route であり，current living-human phospho-state meter ではございません。
- [Vierra et al. (2023)](https://doi.org/10.1038/s41467-023-40930-6) と [Havekes et al. (2016)](https://doi.org/10.1523/JNEUROSCI.0248-16.2016) も local signaling nanodomain / compartmentalized controller route であり，whole-brain in vivo observability ではございません。

批判:

- front door に dedicated stop rule がないと，読者は `mechanistic phospho causality exists` を `human-compatible current-state observability is rising` と短絡しえます。
- 現在の primary literature はその short cut を支持しておりません。

## 今回実行した変更

- `research_harvest_50.md`
  - front matter の `note` を更新しました。
  - `page_highlights` に phospho route-family split を追加しました。
  - `known_points` に phospho route-card split の bullet を追加しました。
  - 新しい note-box `Read U3 phospho-signaling papers as route-family claims, not as one controller row` を追加しました。
- `mind_uploading_papers.md`
  - front matter の `note` を更新しました。
  - `known_points` と `page_highlights` に phospho route-family split を追加しました。
  - 新しい note-box `Read phospho-signaling papers through an explicit route-family split` を追加しました。
  - technical fast-lane table に `phospho-signaling / second-messenger route-card split` 行を追加しました。

## 今回止めた誤読

- `phospho-signaling` = one generic maintenance controller
- `learning-linked phosphosite change` = `compartmentalized second-messenger routing`
- `circadian phospho timing gate` = `closed-loop drift disclosure`
- `human ex vivo phosphoproteome atlas` = `living-human current phospho-state observability`
- `one phospho paper` = `one universal memory controller`

## 検証結果

- `git diff --check`
  - 問題なく通過いたしました。
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功いたしました。
  - 出力先は `_site/` でございます。
  - `faraday-retry` に関する警告は出ましたが，build failure ではなく，site generation 自体は完了いたしました。

## 外部依存タスク

- なし
  - 今回の作業は，repo 内調査，文献確認，ページ改稿，ローカル build 検証，commit，push までこのセッションで完結できます。

## 参考文献

1. Lee HK, Barbarosie M, Kameyama K, Bear MF, Huganir RL. Regulation of distinct AMPA receptor phosphorylation sites during bidirectional synaptic plasticity. *Cell*. 2003;112(5):631-643.
   - https://doi.org/10.1016/S0092-8674(03)00122-3
2. Rodrigues SM, Farb CR, Bauer EP, LeDoux JE, Schafe GE. Pavlovian fear conditioning regulates Thr286 autophosphorylation of Ca2+/calmodulin-dependent protein kinase II at lateral amygdala synapses. *Journal of Neuroscience*. 2004;24(13):3281-3288.
   - https://doi.org/10.1523/JNEUROSCI.5303-03.2004
3. Havekes R, Park AJ, Tolentino RE, et al. Compartmentalized PDE4A5 signaling impairs hippocampal synaptic plasticity and long-term memory. *Journal of Neuroscience*. 2016;36(34):8936-8946.
   - https://doi.org/10.1523/JNEUROSCI.0248-16.2016
4. Vierra NC, et al. Neuronal ER-plasma membrane junctions couple excitation to Ca2+-activated PKA signaling. *Nature Communications*. 2023;14:5231.
   - https://doi.org/10.1038/s41467-023-40930-6
5. Barone I, et al. Synaptic BMAL1 phosphorylation controls circadian hippocampal plasticity. *Science Advances*. 2023.
   - https://doi.org/10.1126/sciadv.adj1010
6. Altas B, Tuffy LP, Patrizi A, et al. Region-specific phosphorylation determines Neuroligin-3 localization to excitatory versus inhibitory synapses. *Biological Psychiatry*. 2024;96(10):815-828.
   - https://doi.org/10.1016/j.biopsych.2023.12.020
7. Rodriguez AC, Kramár EA, Augustynski AS, et al. HDAC3 Serine 424 phospho-mimic and phospho-null mutants bidirectionally modulate long-term memory formation and synaptic plasticity in the adult and aging mouse brain. *Journal of Neuroscience*. 2025;45(29):e1619242025.
   - https://doi.org/10.1523/JNEUROSCI.1619-24.2025
8. Biswas D, et al. The landscape of the human brain phosphoproteome reveals region-specific phosphorylation events. *Journal of Proteome Research*. 2023;22(4):1390-1404.
   - https://doi.org/10.1021/acs.jproteome.2c00244
