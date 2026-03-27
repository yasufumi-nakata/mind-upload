# Site Deepening Audit (2026-03-28, front-door tractography route-card sync)

## 対象

- 主対象: `faq.md`
- 副対象: `glossary.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1162/netn_a_00324`
- `https://doi.org/10.1016/j.neuroimage.2024.120904`
- `https://doi.org/10.1016/j.mri.2025.110424`
- `https://doi.org/10.3389/fnimg.2026.1670604`
- `https://doi.org/10.1016/j.media.2025.103580`
- `https://doi.org/10.1016/j.media.2025.103498`

## 今回この箇所を選んだ理由

- `wiki/connectome-is-not-enough.md` と `verification.md` はすでに
  - `tractography route card`
  - `macro pathway prior`
  - `acquisition / endpoint / graph / uncertainty` の分離
  をかなり強く入れていました。
- その一方で、読者の入口になりやすい `faq.md` と `glossary.md` はなお
  - `tractography-derived connectome = coarse`
  までは止めていたものの、
  - `その coarse object 自体が一つの安定 graph ではない`
  という 2023-2026 文献の更新を front door で十分に固定していませんでした。
- このズレは技術・自然科学の観点で重要です。中核ページで止めた過読を FAQ と用語集が再導入すると、読者は `human connectome` という語だけで stable graph を想像しやすくなるからです。

## 根拠付き批判

### 1. `macro pathway prior` だけでは、graph-conditioning の中身がまだ見えません

- [Gajwani et al. (2023)](https://doi.org/10.1162/netn_a_00324) は、`40 pipelines` と `44` の group-representative reconstructions で hub location の不一致を示し、node strength が regional surface area と強く結びつく条件が多いことを示しました。
- [He et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120904) は tractogram filtering により structural-connectome laterality が有意に動くことを示しました。

批判:

- したがって `tractography connectome is a macro pathway prior` という一文だけでは、読者はなお `coarse だが stable graph` と読めてしまいます。
- front door 側でも `hubness / laterality / graph metric 自体が pipeline-conditioned` であることを明示すべきでした。

### 2. acquisition scheme と voxel size は単なる implementation detail ではありません

- [McMaster et al. (2025)](https://doi.org/10.1016/j.mri.2025.110424) は voxel-size variance が connectome に影響し、比較時の resampling rule を要することを示しました。
- [Bramati et al. (2026)](https://doi.org/10.3389/fnimg.2026.1670604) は、同じ `3 T` scanner・同じ preprocessing でも、HARDI / multi-shell / DSI / HCP-style multi-shell の sampling scheme の違いだけで voxel metrics と tractography output が動くことを示しました。

批判:

- `tractography result` を modality name だけで読むのは粗すぎます。
- FAQ と glossary でも `q-space sampling` と `voxel-size harmonization` を route meaning の一部として固定する必要がありました。

### 3. uncertainty と hybrid calibration を front door で無視すると、MRI-alone overread が戻ります

- [Manzano-Patrón et al. (2025)](https://doi.org/10.1016/j.media.2025.103580) は fibre-orientation uncertainty を tractography へ明示的に伝播させました。
- [Zhu et al. (2025)](https://doi.org/10.1016/j.media.2025.103498) は MRI に microscopy を足した hybrid route で tractography を改善しました。

批判:

- これは逆に言えば、`MRI alone already fixed the graph` ではないことを意味します。
- glossary に `tractography route card` がないままだと、読者は uncertainty / external calibration を optional detail と見なしやすいです。

## 今回実行した変更

- `faq.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `page_highlights` と `known_points` に、human tractography graph が `acquisition / endpoint / graph / uncertainty-conditioned` であることを追加しました。
  - Q2c の tractography paragraph を改稿し、従来の `macro pathway prior` 説明に加えて
    - hub instability
    - laterality shift
    - voxel-size dependence
    - q-space sampling bias
    - explicit uncertainty propagation
    - MRI-microscopy hybrid calibration
    を追加しました。
  - 参考文献に 2023-2026 tractography papers を追記しました。

- `glossary.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter に tractography-specific stop-line の追加を明記しました。
  - 用語として
    - `Macro pathway prior`
    - `Tractography route card`
    - `Human tractography connectome`
    を追加しました。
  - `Connectome` の定義も、human diffusion-MRI route では safe reading が lower ceiling になると分かるよう改稿しました。
  - 参考文献に tractography route-card の主要文献を追加しました。

## 今回止めた過読

- `human tractography connectome = coarse だが stable graph`
- `hub map` や `laterality` を connectome 本体の性質としてそのまま読む
- `voxel size` や `q-space sampling` を実装詳細として無視する
- `uncertainty` を表示しなくても connectome claim は同じ重みで読める
- `hybrid MRI-microscopy improvement` を MRI-alone tractography の完成と取り違える

## 外部依存タスク

- なし
  - 今回の変更は公開文書・監査メモ・参考文献更新で repo 内完結できます。

## 参考文献

1. Thomas C, Ye FQ, Irfanoglu MO, et al. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *PNAS*. 2014.
   - https://doi.org/10.1073/pnas.1405672111
2. Reveley C, Seth AK, Pierpaoli C, et al. Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. *PNAS*. 2015.
   - https://doi.org/10.1073/pnas.1418198112
3. Donahue CJ, Sotiropoulos SN, Jbabdi S, et al. Using diffusion tractography to predict cortical connection strength and distance: a quantitative comparison with tracers in the monkey. *J Neurosci*. 2016.
   - https://doi.org/10.1523/JNEUROSCI.0493-16.2016
4. Schilling KG, Petit L, Rheault F, et al. Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. *Brain Struct Funct*. 2020.
   - https://doi.org/10.1007/s00429-020-02129-z
5. Grisot G, Haber SN, Hawrylycz M, Yendiki A, et al. Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. *NeuroImage*. 2021.
   - https://doi.org/10.1016/j.neuroimage.2021.118300
6. Gajwani M, Oldham S, Pang JC, Arnatkevičiūtė A, Tiego J, Bellgrove MA, Fornito A. Can hubs of the human connectome be identified consistently with diffusion MRI? *Network Neuroscience*. 2023.
   - https://doi.org/10.1162/netn_a_00324
7. Sarwar T, Ramamohanarao K, Daducci A, Schiavi S, Smith RE, Zalesky A. Evaluation of tractogram filtering methods using human-like connectome phantoms. *NeuroImage*. 2023.
   - https://doi.org/10.1016/j.neuroimage.2023.120376
8. He Y, Hong Y, Wu Y, et al. Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. *NeuroImage*. 2024.
   - https://doi.org/10.1016/j.neuroimage.2024.120904
9. McMaster EM, Newlin NR, Rudravaram G, et al. Harmonized connectome resampling for variance in voxel sizes. *Magn Reson Imaging*. 2025.
   - https://doi.org/10.1016/j.mri.2025.110424
10. Manzano-Patrón JP, Deistler M, Schröder C, et al. Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. *Med Image Anal*. 2025.
   - https://doi.org/10.1016/j.media.2025.103580
11. Zhu S, Huszar IN, Cottaar M, et al. Imaging the structural connectome with hybrid MRI-microscopy tractography. *Med Image Anal*. 2025.
   - https://doi.org/10.1016/j.media.2025.103498
12. Bramati IB, Szczupak D, Carneiro Monteiro M, Meireles F, Menezes Guimarães D, Dean RJ, Paul LK, Tovar-Moll F. Diffusion MRI sampling schemes bias diffusion metrics and tractography. *Front Neuroimaging*. 2026.
   - https://doi.org/10.3389/fnimg.2026.1670604
