# Site Deepening Audit (2026-04-01, literature tractography route sync)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 同期先として確認したページ:
  - `index.md`
  - `wbe_101.md`
  - `verification.md`
  - `wiki/connectome-is-not-enough.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.1073/pnas.1405672111`
- `https://doi.org/10.1002/hbm.23936`
- `https://doi.org/10.1007/s00429-020-02129-z`
- `https://doi.org/10.1162/netn_a_00324`
- `https://doi.org/10.1016/j.mri.2025.110424`
- `https://doi.org/10.3389/fnimg.2026.1670604`
- `https://doi.org/10.1016/j.media.2025.103498`

## 今回この箇所を選んだ理由

- front door 側ではすでに
  - `tractography-derived human connectome`
  - `macro pathway prior`
  - `endpoint / graph-construction / calibration burden`
  の停止線がかなり明示されておりました。
- しかし文献アーカイブである
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
  では、`same-brain functional connectomics` や `living-human proxy routes` は精密に split されていた一方で、
  - `human tractography connectome`
  - `bundle dissection under strong priors`
  - `graph instability across plausible pipelines`
  - `protocol dependence`
  - `hybrid calibration`
  を独立ルートとして止める front-door 文言が不足しておりました。

## 主要結論

- 文献アーカイブ側でも、`human tractography connectome` は少なくとも次の 5 分割で止める必要がございました。
  - `endpoint access / gyral-endpoint bias`
  - `targeted bundle dissection under strong priors`
  - `graph-construction instability`
  - `protocol / voxel / sampling dependence`
  - `external / hybrid calibration`
- よって archive / evidence-bank の safe ceiling は
  - `acquisition-, endpoint-, graph-construction-, and calibration-conditioned macro pathway prior`
  - `targeted bundle-hypothesis route`
  に留めるのが妥当でございます。

## 根拠付き批判

### 1. tractography は「connectome」という単語だけで一つの安定した object にはなりません

- [Thomas et al. (2014)](https://doi.org/10.1073/pnas.1405672111) は，voxel-averaged local orientation に基づく tractography には本質的限界があることを示しました。
- [Schilling et al. (2018)](https://doi.org/10.1002/hbm.23936) は，deterministic / probabilistic algorithm，複数 diffusion model，高解像度条件でも gyral-endpoint bias が残ることを示しました。

批判:

- したがって `tractography connectome` を無条件で `cortical edge list` と読むのは不正確でございます。
- 少なくとも
  - cortical endpoint access
  - endpoint bias
  は明示的に別 burden として残ります。

### 2. 強い anatomical prior で精度が上がることは，「一般 connectome recovery」が解けたことを意味しません

- [Schilling et al. (2020)](https://doi.org/10.1007/s00429-020-02129-z) は，start / end / exclusion の強い prior があると tractography の anatomical accuracy が大きく改善しうることを示しました。

批判:

- これは重要な前進ですが，
  - targeted bundle dissection
  - strong-prior virtual dissection
  の前進であり，
  - unconstrained whole-brain edge-complete recovery
  の別名ではございません。
- よって archive 側でも `tractography success` を generic `connectome truth` へ昇格させるべきではございません。

### 3. graph metric 自体が pipeline で動くため，hubness や topography を one stable anatomy と読むことはできません

- [Gajwani et al. (2023)](https://doi.org/10.1162/netn_a_00324) は，`1,760` group connectomes（`40 pipelines` × `44 group-reconstruction schemes`）を比較し，hub location と hubness が processing choice に強く依存することを示しました。

批判:

- したがって
  - hub map
  - laterality
  - degree ranking
  は tractography graph の自然な副産物ではなく，
  - graph-construction choice
  - tractography workflow
  - parcellation
  の関数でございます。

### 4. protocol dependence は scanner 外の混線ではなく，同系条件でも残ります

- [McMaster et al. (2025)](https://doi.org/10.1016/j.mri.2025.110424) は，voxel-size variance が connectome comparison を動かし，harmonized resampling の必要性を示しました。
- [Bramati et al. (2026)](https://doi.org/10.3389/fnimg.2026.1670604) は，同一 `3 T` scanner・uniform processing 条件でも sampling scheme が diffusion metrics と tractography を動かすことを示しました。

批判:

- したがって `different scanner` だから揺れるのではなく，
  - voxel size
  - q-space / sampling scheme
  自体が route burden でございます。

### 5. hybrid calibration は improvement であって，living-human finished connectome ではありません

- [Zhu et al. (2025)](https://doi.org/10.1016/j.media.2025.103498) は，MRI と microscopy を組み合わせた hybrid tractography により reconstruction 改善を示しました。

批判:

- これは
  - calibration-enhanced reconstruction
  - hybrid ex vivo support route
  の前進であり，
  - living-human tractography alone yields finished connectome
  を意味しません。

## 今回実行した変更

### `mind_uploading_papers.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `known_points` と `page_highlights` に tractography route-conditioned reading を追加しました。
- technology / natural-science front door に tractography note-box を追加しました。
- 読み分け table に，tractography paper の安全な入口 row を追加しました。

### `research_harvest_50.md`

- front matter の `page_highlights` と `known_points` に tractography route split を追加しました。
- priority-route table の U1/U7 row を修正し，tractography route burden を first-pass 読解条件に加えました。
- tractography note-box を追加し，文献マップ側でも同停止線が visible になるようにしました。

## 今回止めた誤読

- `tractography graph = the connectome itself`
- `connectome paper = stable human structural truth`
- `improved bundle dissection under priors = general edge-complete recovery`
- `hub map = anatomy rather than pipeline choice`
- `hybrid MRI-microscopy improvement = living-human connectome nearly solved`

## 検証予定

- `bundle exec jekyll build`
- `git diff --check`
- `git diff --stat`

## external dependency tasks

- なし
  - 今回の主作業は、web 上の一次文献確認、公開ページ改稿、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Thomas C, Ye FQ, Irfanoglu MO, et al. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *PNAS*. 2014. https://doi.org/10.1073/pnas.1405672111
2. Schilling KG, Gao Y, Janve V, Stepniewska I, Landman BA, Anderson AW. Confirmation of a gyral bias in diffusion MRI fiber tractography. *Human Brain Mapping*. 2018. https://doi.org/10.1002/hbm.23936
3. Schilling KG, Petit L, Rheault F, et al. Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. *Brain Structure and Function*. 2020. https://doi.org/10.1007/s00429-020-02129-z
4. Gajwani M, Oldham S, Pang JC, et al. Can hubs of the human connectome be identified consistently with diffusion MRI? *Network Neuroscience*. 2023. https://doi.org/10.1162/netn_a_00324
5. McMaster EM, Newlin NR, Rudravaram G, et al. Harmonized connectome resampling for variance in voxel sizes. *Magnetic Resonance Imaging*. 2025. https://doi.org/10.1016/j.mri.2025.110424
6. Bramati IB, Szczupak D, Carneiro Monteiro M, et al. Diffusion MRI sampling schemes bias diffusion metrics and tractography. *Frontiers in Neuroimaging*. 2026. https://doi.org/10.3389/fnimg.2026.1670604
7. Zhu S, Huszar IN, Cottaar M, et al. Imaging the structural connectome with hybrid MRI-microscopy tractography. *Medical Image Analysis*. 2025. https://doi.org/10.1016/j.media.2025.103498
