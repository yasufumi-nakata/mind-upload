# Site Deepening Audit (2026-04-02, front-door release-machinery sync)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
  - `wiki/mind-upload-basics.md`
- 派生同期:
  - `summary_booklet.md`
  - `github-wiki-export/mind-upload-basics.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.1038/s41467-022-30199-6`
- `https://doi.org/10.1038/s41586-025-08790-w`
- `https://doi.org/10.1038/s41593-025-02080-4`
- `https://doi.org/10.7554/eLife.18167`
- `https://doi.org/10.1038/s41593-017-0041-9`
- `https://doi.org/10.1038/s41467-022-33565-6`
- `https://doi.org/10.1038/s41593-024-01720-5`
- `https://doi.org/10.1038/s41586-020-03134-2`
- `https://doi.org/10.1523/JNEUROSCI.1750-23.2024`
- `https://doi.org/10.1177/0271678X20946198`
- `https://doi.org/10.1038/s41380-022-01465-2`

## 今回この箇所を選んだ理由

- 2026-04-02 時点で、deep page 群ではすでに
  - `regional SV2A density`
  - `same-brain structure-function scaffold`
  - `release-site number / docked-vesicle architecture / active-zone nanostructure / current release competence`
  を別 object として扱う stop line が導入済みでした。
- しかし front door である
  - `index.md`
  - `faq.md`
  - `wiki/mind-upload-basics.md`
  には、なお `current synaptic-state` という粗い表現が残っており、読者が
  - `same-brain functional connectomics`
  - `SV2A PET`
  - `human observability progress`
  を presynaptic release machinery の近接 readout と過読する余地がございました。
- この不整合は入口で起きるため、修正レバレッジが大きく、深いページの strict rule が front door で失われる compression bug を生んでおりました。

## 主要結論

- `same-brain local scaffold` は `presynaptic release-machinery truth` ではございません。
- `regional SV2A density` は `release-site number` ではございません。
- `current synaptic state` という語は front door では粗すぎ、少なくとも
  - `release-site number`
  - `docked-vesicle architecture`
  - `active-zone nanostructure / priming-site assembly`
  - `current release competence`
  を別 row に分ける必要がございます。
- よって今回もっとも改善価値が高かったのは、新 topic の追加ではなく、既存 front-door wording を deep page の stop line に同期することでございました。

## 根拠付き批判

### 1. Same-brain functional connectomics は structure-function scaffold を強めますが、release-machinery truth には到達いたしません

- 根拠:
  - [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6)
  - [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w)
  - [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4)
- 批判:
  - same-brain bridge 自体が sequential landmark route であり、さらに connectome-constrained dynamics は追加記録がない限り依然として degenerate でございます。
  - したがって `same brain` というだけで local twin や presynaptic machinery まで読むことはできません。

### 2. Human synapse / active zone 文献は、`one synapse` や `one strength scalar` では presynaptic object を尽くさないことを示しております

- 根拠:
  - [Molnár et al. (2016)](https://doi.org/10.7554/eLife.18167)
  - [Sakamoto et al. (2018)](https://doi.org/10.1038/s41593-017-0041-9)
  - [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6)
  - [Emperador-Melero et al. (2024)](https://doi.org/10.1038/s41593-024-01720-5)
  - [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2)
- 批判:
  - human synapses can contain multiple docked vesicles and multivesicular release.
  - independent release sites are set by Munc13 assemblies.
  - release probability matters, but it still does not exhaust active-zone nanostructure.
  - CaV2 clustering and vesicle priming are themselves distinct machineries.
  - よって `current synaptic state` を front door で one row のまま残すと、deep page 側がすでに止めている mechanistic split を入口で消してしまいます。

### 3. SV2A PET は release-machinery readout ではなく bounded regional-density proxy でございます

- 根拠:
  - [Johansen et al. (2024)](https://doi.org/10.1523/JNEUROSCI.1750-23.2024)
  - [Smart et al. (2021)](https://doi.org/10.1177/0271678X20946198)
  - [Holmes et al. (2022)](https://doi.org/10.1038/s41380-022-01465-2)
- 批判:
  - healthy-human atlas は重要な advance ですが、activation-null と intervention-null の文献が示すとおり、SV2A PET は momentary release competence meter ではございません。
  - したがって front door が `current synaptic state` で止まると、SV2A を active-zone truth に過剰昇格させる余地が残ります。

## 今回実行した変更

- `index.md`
  - `last_updated` を更新しました。
  - front-matter の `page_highlights` と `known_points` を tightening し、same-brain / SV2A 側の `presynaptic release-machinery ceiling` を追加しました。
  - same-brain note-box と SV2A note-box を更新し、release-site number / docked-vesicle architecture / active-zone nanostructure / current release competence を front door に同期しました。
  - human observability note-box に `presynaptic release-machinery / active-zone nanostructure state` の still-missing row を追加しました。

- `faq.md`
  - `last_updated` を更新しました。
  - front matter と `Eleven technical guards` の本文に `presynaptic release-machinery ceiling` を追加しました。
  - Q2c1 の入口要約と本文を更新し、same-brain scaffold と release-machinery truth を切り分けました。
  - Q2d 本文と SV2A row を更新し、healthy atlas / activation-null / intervention-null と release-machinery ceiling の関係を明示しました。

- `wiki/mind-upload-basics.md`
  - `page_highlights` と `known_points` を tightening しました。
  - 新しい note-box `2026-04-02 correction: synaptic-density is not presynaptic release machinery` を追加しました。
  - human observability ladder の `Regional synaptic-density PET atlas` 行を更新しました。
  - 2026-03-30 beginner correction の same-brain paragraph を更新し、release-machinery ceiling を beginner front door に同期しました。

- `summary_booklet.md`
  - `index.md` / `faq.md` / `wiki/mind-upload-basics.md` の front matter tightening を自動要約へ同期するため、`ruby scripts/build_summary_booklet.rb` で再生成しました。

- `github-wiki-export/*.md`
  - `github-wiki-export/mind-upload-basics.md` を edited source に合わせて再生成しました。
  - 併せて `ruby scripts/export_github_wiki.rb` により、source 側がすでに export snapshot より先行していた
    - `github-wiki-export/measurement-stack-and-claim-ceiling.md`
    - `github-wiki-export/mind-upload-current-public-six-rq-brief.md`
    - `github-wiki-export/mind-upload-eeg-rq60-feasibility-and-funds.md`
    - `github-wiki-export/mind-upload-rq-solvability-bridge.md`
    も同期されました。

## 今回止めた誤読

- `same-brain local scaffold` = `release-site number`
- `same-brain digital twin` = `active-zone nanostructure truth`
- `SV2A atlas` = `current release competence meter`
- `current synaptic state` = `one presynaptic scalar`
- `human observability progress` = `release-machinery observability progress`

## 検証結果

- `ruby scripts/export_github_wiki.rb`
  - 成功しました。
- `ruby scripts/build_summary_booklet.rb`
  - 成功しました。
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功しました。
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功しました。
- `git diff --check`
  - 成功しました。
- `rg -n "presynaptic release-machinery|release-site number|docked-vesicle architecture|current release competence" summary_booklet.md github-wiki-export/mind-upload-basics.md _site/index.html _site/faq.html _site/wiki/mind-upload-basics.html`
  - `summary_booklet.md`、GitHub Wiki export、公開 HTML `_site` のすべてに新しい stop line が反映されていることを確認しました。

## 外部依存タスク

- なし
  - 今回の作業は、web 上の一次文献確認、repo 内改稿、derived artifact 再生成、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Bosch C, et al. Functional and multiscale 3D structural investigation of brain circuits in anesthetized rodents by combining two-photon imaging and sample expansion. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
2. MICrONS Consortium, Bae JA, Buchanan EK, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
3. Beiran M, Litwin-Kumar A. Identifiability of neural activity from a brain's connectome. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02080-4
4. Molnár G, Rózsa M, Baka J, Holderith N, Barzó P, Nusser Z, Tamás G. Human pyramidal to interneuron synapses are mediated by multi-vesicular release and multiple docked vesicles. *eLife*. 2016;5:e18167.
   - https://doi.org/10.7554/eLife.18167
5. Sakamoto H, Ariyoshi T, Kimpara N, Sugao K, Taiko I, Takikawa K, Asanuma D, Namiki S, Hirose K. Synaptic weight set by Munc13-1 supramolecular assemblies. *Nature Neuroscience*. 2018;21(1):41-49.
   - https://doi.org/10.1038/s41593-017-0041-9
6. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022;13:6126.
   - https://doi.org/10.1038/s41467-022-33565-6
7. Emperador-Melero J, Andersen JW, Metzbower SR, et al. Distinct active zone protein machineries mediate Ca<sup>2+</sup> channel clustering and vesicle priming at hippocampal synapses. *Nature Neuroscience*. 2024;27:1680-1694.
   - https://doi.org/10.1038/s41593-024-01720-5
8. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021;591:111-116.
   - https://doi.org/10.1038/s41586-020-03134-2
9. Johansen A, et al. Regional synaptic density mapped in vivo in the healthy human brain. *Journal of Neuroscience*. 2024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
10. Smart K, Liu H, Matuskey D, et al. Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
11. Holmes SE, Finnema SJ, Naganawa M, et al. Imaging the effect of ketamine on synaptic density (SV2A) in the living brain. *Molecular Psychiatry*. 2022.
   - https://doi.org/10.1038/s41380-022-01465-2
