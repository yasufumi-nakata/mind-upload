# Site Deepening Audit (2026-04-01, presynaptic release machinery / active-zone split)

## 対象

- 主対象:
  - `wiki/connectome-is-not-enough.md`
- 同期対象:
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wbe_101.md`
  - `verification.md`
  - `github-wiki-export/connectome-is-not-enough.md`
  - `github-wiki-export/measurement-stack-and-claim-ceiling.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.7554/eLife.18167`
- `https://doi.org/10.1038/s41593-017-0041-9`
- `https://doi.org/10.1038/s41467-022-33565-6`
- `https://doi.org/10.1038/s41593-024-01720-5`
- `https://doi.org/10.1177/0271678X20946198`
- `https://doi.org/10.1038/s41586-020-03134-2`
- `https://doi.org/10.1038/s41467-024-53901-2`

## 今回この箇所を選んだ理由

- 2026-04-01 時点の site は、`connectome is not enough` の論点自体はかなり強く整理できておりましたが、なお
  - `synapse count`
  - `regional SV2A density`
  - `release probability`
  - `presynaptic release machinery / active-zone nanostructure`
  を読者が心中で一つの object に圧縮できる余地が残っておりました。
- この余地を残すと、connectome page で止めたつもりの誤読が、
  - same-brain functional connectomics
  - synaptic-density PET
  - front-door human observability ladder
  - verification budget
 へ再流入いたします。
- したがって、今回もっとも correction value が高いのは、新しい topic を増やすことではなく、`current synaptic-state` の内部をもう一段分解し、`active-zone / release-site architecture` を site-wide の stop line として明示することでした。

## 主要結論

- `synapse exists` は `release site is specified` を意味いたしません。
- `regional SV2A density` は `current presynaptic release machinery` を意味いたしません。
- `release probability` は重要な state variable ですが、それ自体が `release-site number` や `active-zone nanostructure / priming-site assembly` を尽くすわけではございません。
- よって本 site では、
  - `synapse count`
  - `regional synaptic-density proxy`
  - `release-site number`
  - `docked-vesicle architecture`
  - `active-zone nanostructure / priming-site assembly`
  - `current release competence`
  を別 object として扱う必要がございます。

## 根拠付き批判

### 1. Human synaptic contact は one-contact = one release-ready state ではございません

- 根拠:
  - [Molnár et al. (2016)](https://doi.org/10.7554/eLife.18167) は、human pyramidal-to-interneuron synapses において multi-vesicular release と multiple docked vesicles を示しました。
- 批判:
  - これは、同じ `one synaptic contact` でも docked-vesicle architecture と release organization が単一ではないことを意味いたします。
  - したがって `synapse count` をそのまま `current release competence` に読み替えるのは過読でございます。

### 2. Presynaptic weight は Munc13-based release-site organization を伴うため one scalar ではございません

- 根拠:
  - [Sakamoto et al. (2018)](https://doi.org/10.1038/s41593-017-0041-9) は、Munc13-1 supramolecular assemblies が独立 release site として働き、presynaptic weight を規定することを示しました。
- 批判:
  - ここで重要なのは、presynaptic strength の差が `vesicle exists / synapse exists` ではなく、active-zone-side の organization に依存する点でございます。
  - よって connectome row や synapse count だけでは、presynaptic side の operative architecture は確定いたしません。

### 3. Release probability は重要ですが、それだけで presynaptic machinery 全体を代表いたしません

- 根拠:
  - [Dürst et al. (2022)](https://doi.org/10.1038/s41467-022-33565-6) は、individual synaptic strength を vesicular release probability が強く規定することを示しました。
- 批判:
  - この結果は `release probability matters` を支持しますが、同時に `release probability` を測っただけで `release-site number` や `active-zone nanostructure` が分かったことにはなりません。
  - したがって `release probability` を `presynaptic machinery` の fully sufficient proxy として扱うのも不適切でございます。

### 4. Active zone 自体が内部で分解されており、CaV2 clustering と priming は別機構でございます

- 根拠:
  - [Emperador-Melero et al. (2024)](https://doi.org/10.1038/s41593-024-01720-5) は、CaV2 channel clustering と vesicle priming が distinct active-zone machineries により媒介されることを示しました。
- 批判:
  - これにより、`active zone` という語自体も one-piece object では読めなくなります。
  - よって `same-brain structure-function correspondence` や `regional synaptic-density proxy` を active-zone truth に拡張する余地はさらに小さくなります。

### 5. Same-brain functional connectomics は local scaffold であって current release-machinery readout ではございません

- 根拠:
  - [Holler et al. (2021)](https://doi.org/10.1038/s41586-020-03134-2) は neocortical synapse の structure/function relation を詳細化しつつ、structure から function を直に尽くせない限界を示しました。
  - [Mittermaier et al. (2024)](https://doi.org/10.1038/s41467-024-53901-2) は human neocortical tissue で membrane-potential state が synaptic consolidation を gate することを示しました。
- 批判:
  - same-brain functional connectomics は `stronger local scaffold` ではありますが、そこから active-zone architecture や membrane-state-gated synaptic readiness を自動で引き出すことはできません。
  - よって site rule には `current synaptic-state` だけでなく `presynaptic release machinery` も explicit ceiling として書く必要がございました。

### 6. SV2A PET は timescale ceiling 上、momentary release readiness meter でもございません

- 根拠:
  - [Smart et al. (2021)](https://doi.org/10.1177/0271678X20946198) は、brief visual activation によって tracer influx は変化しても [<sup>11</sup>C]UCB-J binding 自体は変化しなかったことを示しました。
- 批判:
  - これは `regional SV2A density` を `momentary synaptic efficacy` や `current release machinery` に読み替えることを止める直接根拠でございます。
  - front door と verification page の両方に stop line を置く必要がございました。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - front matter の `description` と `last_updated` を更新しました。
  - `page_highlights` と `known_points` に、`synapse count / SV2A density / release-site number / active-zone nanostructure` を切り分ける stop line を追加しました。
  - conclusion と `Synaptic efficiency/short-term state` 行を更新し、current presynaptic release machinery を latent state として明示しました。
  - `2026-04-01 addendum` note-box を追加し、Molnár / Sakamoto / Dürst / Emperador-Melero をまとめて site rule に接続しました。
  - `Current-synaptic-state wall` を更新し、release-machinery readout ではないことを明記しました。
  - references に Molnár et al. (2016), Sakamoto et al. (2018), Emperador-Melero et al. (2024) を追加しました。

- `wiki/measurement-stack-and-claim-ceiling.md`
  - `page_highlights` と `known_points` を更新し、same-brain functional connectomics と synaptic-density PET を presynaptic release-machinery readout へ昇格させない rule を明記しました。
  - `same-brain functional connectomics` 行と same-brain section を更新し、`active-zone architecture` を unresolved object として追加しました。
  - `SV2A PET / synaptic-density PET` 行を更新し、`release-site number` と `active-zone nanostructure / priming-site assembly` を ceiling 側へ追加しました。

- `wbe_101.md`
  - beginner-facing note-box を追加し、`synapse count / regional SV2A density / presynaptic release machinery` を一束に読まない rule を front door へ同期しました。
  - human observability ladder の `Regional synaptic-density PET atlas` 行を更新しました。
  - `Still lacking a comparable in vivo whole-brain human route` 行に `presynaptic release-machinery / active-zone nanostructure state` を追加しました。

- `verification.md`
  - observability / maintenance bullet を更新し、regional density の overread 先に `presynaptic release machinery` を追加しました。
  - latent-state budget と maintenance-state budget の `Current synaptic efficacy / short-term state` 行を更新しました。
  - `2026-04-01 addendum: synaptic-density is not presynaptic release-machinery evidence` を追加しました。

- generated 同期:
  - `ruby scripts/export_github_wiki.rb` により
    - `github-wiki-export/connectome-is-not-enough.md`
    - `github-wiki-export/measurement-stack-and-claim-ceiling.md`
    へ対応差分を再生成しました。

## 今回止めた誤読

- `synapse count` = `current release competence`
- `regional SV2A density` = `presynaptic release-machinery truth`
- `release probability` = `complete presynaptic state`
- `same-brain functional connectomics` = `active-zone architecture readout`
- `current synaptic-state` = `one scalar`

## 検証結果

- `ruby scripts/export_github_wiki.rb`
  - 成功しました。
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功しました。
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功しました。
- `git diff --check`
  - 成功しました。
- `rg -n "presynaptic release machinery|active-zone nanostructure|release-site number|synaptic-density is not presynaptic release-machinery evidence" ...`
  - `_site` と `github-wiki-export` の両方に、新しい stop line が反映されていることを確認しました。

## 外部依存タスク

- なし
  - 今回の作業は、web 上の一次文献確認、本文修正、export/build/diff 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Molnár G, Rózsa M, Baka J, Holderith N, Barzó P, Nusser Z, Tamás G. Human pyramidal to interneuron synapses are mediated by multi-vesicular release and multiple docked vesicles. *eLife*. 2016;5:e18167.
   - https://doi.org/10.7554/eLife.18167
2. Sakamoto H, Ariyoshi T, Kimpara N, Sugao K, Taiko I, Takikawa K, Asanuma D, Namiki S, Hirose K. Synaptic weight set by Munc13-1 supramolecular assemblies. *Nature Neuroscience*. 2018;21(1):41-49.
   - https://doi.org/10.1038/s41593-017-0041-9
3. Dürst CD, Wiegert JS, Schulze C, et al. Vesicular release probability sets the strength of individual Schaffer collateral synapses. *Nature Communications*. 2022;13:6126.
   - https://doi.org/10.1038/s41467-022-33565-6
4. Emperador-Melero J, Andersen JW, Metzbower SR, et al. Distinct active zone protein machineries mediate Ca<sup>2+</sup> channel clustering and vesicle priming at hippocampal synapses. *Nature Neuroscience*. 2024;27:1680-1694.
   - https://doi.org/10.1038/s41593-024-01720-5
5. Smart K, Liu H, Matuskey D, et al. Binding of the synaptic vesicle radiotracer [<sup>11</sup>C]UCB-J is unchanged during functional brain activation using a visual stimulation task. *Journal of Cerebral Blood Flow & Metabolism*. 2021.
   - https://doi.org/10.1177/0271678X20946198
6. Holler S, et al. Structure and function of a neocortical synapse. *Nature*. 2021;591:111-116.
   - https://doi.org/10.1038/s41586-020-03134-2
7. Mittermaier FX, Kalbhenn T, Xu R, et al. Membrane potential states gate synaptic consolidation in human neocortical tissue. *Nature Communications*. 2024;15:10340.
   - https://doi.org/10.1038/s41467-024-53901-2
