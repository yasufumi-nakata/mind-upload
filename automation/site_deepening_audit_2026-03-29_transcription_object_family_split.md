# Site Deepening Audit (2026-03-29, transcription / chromatin object-family split)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 同期対象: `wbe_101.md`
- 同期対象: `verification.md`
- 同期対象: `index.md`
- 調査方法:
  - 公開中の `https://mind-upload.com/` を web で確認
  - ローカル原稿と突き合わせ
  - 一次文献を追加確認
- 範囲: 技術・自然科学のみ

## 今回この箇所を選んだ理由

- 2026-03-29 JST 時点で、公開サイトはすでに `transcription / chromatin` を
  - `allocation eligibility`
  - `time-resolved response map`
  - `persistent stabilization cascade`
  - `locus-specific causal editability`
  に分けるところまではできておりました。
- しかし、一次文献の粒度では、ここでさらに
  - `chromatin accessibility`
  - `histone-acetylation / histone-methylation route`
  - `DNA-methylation route`
  - `higher-order chromatin looping / topology route`
  - `locus-specific editing route`
  が別 object です。
- 現行サイトの route card は `assay and direct observable` を要求していましたが、ここだけではまだ `molecular object` の違いが読者に十分可視化されません。
- その結果、`epigenetic evidence` という一語が、なお
  - 開いた accessibility map
  - 持続する histone mark
  - consolidation-linked DNA methylation
  - enhancer-promoter looping
  - CRISPR/dCas9-based locus editing
  を近づけすぎます。

## 根拠付き批判

### 1. 現行サイトは `claim family` を分けていましたが、`molecular object family` はなお圧縮しておりました

- 観察:
  - `allocation eligibility`、`time-course map`、`stabilization cascade`、`locus-specific editability` の分解はすでに導入済みでした。
  - その一方で、route card の `assay / direct observable` だけでは、`chromatin accessibility` と `DNA methylation` と `loop topology` がどの程度別物かが front-door ではまだ十分に露出しておりませんでした。
- 批判:
  - これは scientific stop line として一段甘いです。
  - なぜなら、同じ `transcription / chromatin` family に属していても、`何を直接観測したのか` が違えば persistence, causal leverage, and human-readout ceiling も変わるからです。

### 2. 一次文献は accessibility, histone chemistry, DNA methylation, and looping を同じ証拠として扱っておりません

- 根拠:
  - Santoni et al. (2024) は、memory-trace formation 前の `neuronal eligibility` を `pre-encoding chromatin plasticity` と結びつけました。
  - Traunmüller et al. (2025) は、hippocampus で `single-nucleus multiomics` により region-specific な `chromatin accessibility` と `gene-expression` を追いました。
  - Guan et al. (2009) は、`histone-tail acetylation / HDAC2` の操作が memory formation と synaptic plasticity を変えることを示しました。
  - Gulmez Karaca et al. (2020) は、engram ensemble 内の `DNA methylation / Dnmt3a2` 操作が consolidation と engram stability を変えることを示しました。
  - Bharadwaj et al. (2014) は、human and mouse cortex で `higher-order chromatin loopings` が GRIN2B regulation と cognition に関わることを示しました。
  - Coda et al. (2025) は、defined engram cells で `locus-specific epigenetic editing` を因果的に用いました。
- 批判:
  - したがって `epigenetic state` は一行で終わる object ではございません。
  - `opening`, `chemical marking`, `methylome rewrite`, `loop rewiring`, and `locus editing` are different readouts and different interventions.
  - ここを site rule に反映しないと、読者は `epigenetic evidence exists` を `the relevant controller was fixed` と過読しやすくなります。

### 3. persistence claim の中身が object family によって異なります

- 根拠:
  - Traunmüller et al. (2025) は physiological stimulation 後の temporally defined accessibility / expression map を示しました。
  - Gulmez Karaca et al. (2020) は consolidation window の DNA methylation manipulation が engram stability を強めることを示しました。
  - Bharadwaj et al. (2014) は higher-order loop regulation を gene-expression and cognition に結びつけました。
- 批判:
  - よって `persistent transcription / chromatin signal` という言い方だけでは不十分です。
  - `persistent accessibility`, `persistent methylation program`, and `persistent looping` are not interchangeable.
  - 現行サイトは `persistent stabilization cascade` という claim-family language までは入っていましたが、`which molecular object persisted` をまだ十分には固定しておりませんでした。

### 4. human observability ceiling も transcription / chromatin family の内部で明示し直す価値があります

- 観察:
  - RNA-state, phospho-signaling, spectroscopy などでは `human observability ceiling` が比較的明示されていました。
  - 一方 transcription / chromatin では、site-wide には「まだ comparable in vivo whole-brain human route がない」と書かれていても、route-card section 自体には dedicated ceiling box がありませんでした。
- 批判:
  - これは入口規律として弱いです。
  - 一次文献で実際に state を押し上げている routes は、mouse in vivo, destructive single-nucleus assays, postmortem tissue, or in-vitro human neurons が中心であり、living-human whole-brain current-state readout ではありません。
  - この ceiling を route-card 直下で再掲しないと、読者は human relevance と human observability を混同しやすくなります。

## 今回実行する修正方針

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `accessibility / chemical marks / DNA methylation / loop topology / locus editing` を別 object family として明示
  - transcription / chromatin route card に `molecular object / persistence mode` を追加
  - dedicated `human observability ceiling for transcription / chromatin state` note-box を追加
- `wbe_101.md`
  - entry note-box を object-family split に合わせて更新
  - hidden-state table の stop line を、atlas/DEG だけでなく object-family overread にも対応させる
- `verification.md`
  - state-completeness gate の transcription row を `molecular object family` まで要求する文言へ更新
  - addendum を claim-family split から object-family split へ一段厳密化
- `index.md`
  - front-door note-box に `accessibility / histone / methylation / looping / editing` 非同一性を短く露出

## 今回実行した修正

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - 冒頭の hidden-state table 自体に `molecular object family` の stop line を追記
  - route-card note と参考文献の `Guan et al. (2009)` を正しい DOI に修正
- `verification.md`
  - state-completeness row の handling 文言を `single-object clue` まで明示する形へ微修正
  - transcription / chromatin addendum と参考文献の `Guan et al. (2009)` を正しい DOI に修正
- `wiki/connectome-is-not-enough.md`
  - connectome だけでは足りない table と reading rule に `single-object epigenetic assay` 非十分性を追記
- `index.md`
  - front-door highlight を object-family split に合わせて厳密化
  - transcription / chromatin note-box の `Guan et al. (2009)` DOI を修正
- `wbe_101.md`
  - primer 本文と参考文献の `Guan et al. (2009)` DOI を修正

## 今回修正しないもの

- 哲学・法学・personhood の議論
- `issue.md`
- 新規 standalone page の追加
  - 今回の問題は page multiplication ではなく rule sharpening です

## 外部依存で保留

- なし
  - 今回の作業は、このリポジトリ内の本文修正・検証・push までで完結できます

## 検証計画

- `ruby scripts/export_github_wiki.rb`
  - wiki source と `github-wiki-export/` を同期
- `bundle exec jekyll build`
  - サイト全体が静的ビルドできることを確認
- `git diff --check`
  - 余計な空白差分やパッチ破損がないことを確認

## 参考文献 / 公式ソース

1. Santoni G, Astori S, Leleu M, et al. Chromatin plasticity predetermines neuronal eligibility for memory trace formation. *Science*. 2024;385(6707):eadg9982.
   - https://doi.org/10.1126/science.adg9982
2. Traunmüller L, Duffy EE, Liu H, et al. Novel environment exposure drives temporally defined and region-specific chromatin accessibility and gene expression changes in the hippocampus. *Nature Communications*. 2025;16:7787.
   - https://doi.org/10.1038/s41467-025-63029-6
3. Guan JS, Haggarty SJ, Giacometti E, et al. HDAC2 negatively regulates memory formation and synaptic plasticity. *Nature*. 2009;459(7243):55-60.
   - https://doi.org/10.1038/nature07925
4. Gulmez Karaca K, Kupke J, Brito DVC, et al. Neuronal ensemble-specific DNA methylation strengthens engram stability. *Nature Communications*. 2020;11:639.
   - https://doi.org/10.1038/s41467-020-14498-4
5. Bharadwaj R, Peter CJ, Jiang Y, et al. Conserved higher-order chromatin regulates NMDA receptor gene expression and cognition. *Neuron*. 2014;84(5):997-1008.
   - https://doi.org/10.1016/j.neuron.2014.10.032
6. Coda DM, Watt L, Glauser L, et al. Cell-type- and locus-specific epigenetic editing of memory expression. *Nature Genetics*. 2025;57:2661-2668.
   - https://doi.org/10.1038/s41588-025-02368-y
7. Terceros A, Chen C, Harada Y, et al. Thalamocortical transcriptional gates coordinate memory stabilization. *Nature*. 2026;649(8099):1254-1263.
   - https://doi.org/10.1038/s41586-025-09774-6
