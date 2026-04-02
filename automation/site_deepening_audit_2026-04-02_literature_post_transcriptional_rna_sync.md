# Site Deepening Audit (2026-04-02, literature front-door post-transcriptional-RNA sync)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.1038/nn.4069`
- `https://doi.org/10.1016/j.neuron.2019.03.032`
- `https://doi.org/10.1038/s41586-018-0666-1`
- `https://doi.org/10.1038/s41380-023-01953-z`
- `https://doi.org/10.1002/advs.202514926`
- `https://doi.org/10.1126/scisignal.adr1442`
- `https://doi.org/10.1038/s41593-024-01616-4`

## 今回この箇所を選んだ理由

- 2026-04-02 JST 時点で、core page 側ではすでに
  - `post-transcriptional RNA route card`
  - `gene-level abundance ≠ RNA-state`
  - `atlas ceiling ≠ living-human in vivo route`
  が整備済みでございました。
- しかし literature front door である
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
  には、その stop line がまだ十分に前面化されておらず、読者が
  - `post-transcriptional RNA control`
  - `m6A evidence`
  - `splicing evidence`
  を一つの maintenance row として過読する余地が残っておりました。
- 特に m6A lane では、`Shi et al. (2018)` の `YTHDF1-mediated translation` と、`Zhuang et al. (2023)` / `Li et al. (2025)` の `YTHDF2-mediated decay / stability` が、front door ではまだ十分に分離されておりませんでした。
- したがって今回の correction value は、新 topic の追加ではなく、既存の文献入口に `post-transcriptional RNA family split` を site-wide rule として同期することにございました。

## 主要結論

- `post-transcriptional RNA evidence` は一つの object ではございません。
- `splicing evidence` 自体も一つの route ではございません。
- `m6A evidence` も一つの universal hippocampal reader assignment ではございません。
- `long-read atlas` は重要ですが、`living-human whole-brain in vivo readout` ではございません。
- よって literature front door でも
  - `splice-isoform control`
  - `transsynaptic splice-dependent receptor balance`
  - `m6A translation`
  - `dentate-gyrus-scale YTHDF2-mediated decay / stability`
  - `forebrain-scale YTHDF2-mediated decay / stability`
  - `RNA editing`
  - `atlas / observability ceiling`
  を別 route として明示する必要がございました。

## 根拠付き批判

### 1. Literature front door だけがまだ `post-transcriptional RNA control` を一段粗く見せておりました

- 根拠:
  - `verification.md` と `wbe_101.md` では、すでに
    - splice-isoform
    - m6A translation
    - m6A degradation
    - RNA editing
    - atlas ceiling
    の route split が導入済みでございました。
- 批判:
  - その一方で `mind_uploading_papers.md` と `research_harvest_50.md` では、front-door note と highlights にまだ dedicated stop line がなく、`post-transcriptional RNA control` が generic maintenance vocabulary に埋もれておりました。
  - これでは core page の厳密さを archive / evidence-bank の入口で静かに取り崩してしまいます。

### 2. `splicing evidence` 自体が一つの downstream object を指しておりません

- 根拠:
  - [Wang et al. (2015)](https://doi.org/10.1038/nn.4069) は neuron-specific LSD1 splice isoform による `chromatin / transcriptional elongation control` でございます。
  - [Dai et al. (2019)](https://doi.org/10.1016/j.neuron.2019.03.032) は presynaptic neurexin splice による `postsynaptic NMDA-versus-AMPA receptor balance` でございます。
- 批判:
  - よって `splicing evidence exists` という一文では scientific stop line として不十分でございます。
  - 同じ splicing でも downstream object が違えば、何が latent か、どこまで claim できるか、何を human route がまだ観測できていないかが変わります。

### 3. `m6A evidence` を一つの reader/controller として扱うことは一次文献に反します

- 根拠:
  - [Shi et al. (2018)](https://doi.org/10.1038/s41586-018-0666-1) は `YTHDF1-mediated translation` を learning / memory route として示しました。
  - [Zhuang et al. (2023)](https://doi.org/10.1038/s41380-023-01953-z) は `only the DG-specific Ythdf2 cKO mice displayed impaired memory formation` であり、先行 YTHDF1 report と整合しない dentate-gyrus-specific reader assignment を示しました。
  - [Li et al. (2025)](https://doi.org/10.1002/advs.202514926) は forebrain cKO で `YTHDF2-mediated mRNA degradation` が activity-dependent protein synthesis と hippocampus-dependent memory を抑えていることを示しました。
- 批判:
  - したがって `m6A reader route` を一つの reusable row として front door に置くのは不正確でございます。
  - 少なくとも
    - translation vs decay
    - dentate gyrus vs broader forebrain scope
    - reader assignment
    を分けなければ、読者は `m6A evidence exists` を `the relevant reader/controller is fixed` と誤読しやすくなります。

### 4. Atlas ceiling と causal controller paper を同列に読ませる余地が残っておりました

- 根拠:
  - [Peterson et al. (2025)](https://doi.org/10.1126/scisignal.adr1442) は ADAR2 / GluA2 editing を homeostatic plasticity に結びつける causal route でございます。
  - [Joglekar et al. (2024)](https://doi.org/10.1038/s41593-024-01616-4) は long-read atlas として extensive isoform variability を示しますが、living-human whole-brain in vivo route ではございません。
- 批判:
  - それにもかかわらず front door で dedicated RNA note がないと、atlas route の存在が `current human RNA-state observability is close` という誤読に繋がります。
  - literature front door でも `atlas / observability ceiling` を mechanistic controller route から明確に切り離す必要がございました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter の `note` を更新しました。
  - `page_highlights` と `known_points` に、post-transcriptional RNA family split を追加しました。
  - `Read maintenance-state papers as route-changing evidence` の直後に、新しい note-box を追加しました。
  - 新 note-box では
    - Wang
    - Dai
    - Shi
    - Zhuang
    - Li
    - Peterson
    - Joglekar
    を並べ、`splicing / m6A / editing / atlas ceiling` を別 route として front door に明示しました。

- `research_harvest_50.md`
  - front matter の `note` を更新しました。
  - `page_highlights` と `known_points` に、U3 post-transcriptional RNA family split を追加しました。
  - `Read maintenance-state papers as more than support background` の直後に、新しい note-box を追加しました。
  - 新 note-box では、U3 側の reading rule として
    - splice-isoform control
    - transsynaptic receptor-balance route
    - YTHDF1 translation
    - dentate-gyrus-scale YTHDF2 decay / stability
    - forebrain-scale YTHDF2 decay / stability
    - RNA editing
    - atlas ceiling
    を separate claim family として固定しました。

## 今回止めた誤読

- `post-transcriptional RNA evidence` = `one maintenance row`
- `splicing evidence` = `one downstream object`
- `m6A evidence` = `one universal hippocampal reader assignment`
- `one RNA paper` = `current whole-brain RNA-controller state`
- `long-read atlas` = `living-human in vivo RNA-state readout`

## 検証計画

- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - サイト全体が静的ビルドできることを確認
- `git diff --check`
  - 余計な空白差分やパッチ破損がないことを確認
- `rg -n "post-transcriptional RNA papers through an explicit route-family split|U3 post-transcriptional RNA papers as route-family claims|universal hippocampal m6A-reader assignment" _site/mind_uploading_papers.html _site/research_harvest_50.html`
  - `_site` 側へ新しい stop line が反映されていることを確認

## 外部依存タスク

- なし
  - 今回の作業は、web 上の一次文献確認、本文修正、build / diff / generated HTML 確認、commit、push までこのセッションで完結できます。

## 参考文献

1. Wang J, Telese F, Tan Y, et al. LSD1n is an H4K20 demethylase regulating memory formation via transcriptional elongation control. *Nature Neuroscience*. 2015;18(9):1256-1264.
   - https://doi.org/10.1038/nn.4069
2. Dai J, Aoto J, Südhof TC. Alternative splicing of presynaptic neurexins differentially controls postsynaptic NMDA and AMPA receptor responses. *Neuron*. 2019;102(5):993-1008.e5.
   - https://doi.org/10.1016/j.neuron.2019.03.032
3. Shi H, Zhang X, Weng Y-L, et al. m6A facilitates hippocampus-dependent learning and memory through YTHDF1. *Nature*. 2018;563(7730):249-253.
   - https://doi.org/10.1038/s41586-018-0666-1
4. Zhuang M, Geng X, Han P, et al. YTHDF2 in dentate gyrus is the m6A reader mediating m6A modification in hippocampus-dependent learning and memory. *Molecular Psychiatry*. 2023;28(4):1679-1691.
   - https://doi.org/10.1038/s41380-023-01953-z
5. Li K, Guo C, Wu X, et al. Enhanced Protein Synthesis and Hippocampus-Dependent Memory via Inhibition of YTHDF2-Mediated m6A mRNA Degradation. *Advanced Science*. 2025;12:e14926.
   - https://doi.org/10.1002/advs.202514926
6. Peterson LN, Kasper JM, Allgaier JA, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025;18(886):adr1442.
   - https://doi.org/10.1126/scisignal.adr1442
7. Joglekar A, Prjibelski A, Mahfouz A, et al. Single-cell long-read sequencing-based mapping reveals specialized splicing patterns in developing and adult mouse and human brain. *Nature Neuroscience*. 2024;27(6):1073-1088.
   - https://doi.org/10.1038/s41593-024-01616-4
