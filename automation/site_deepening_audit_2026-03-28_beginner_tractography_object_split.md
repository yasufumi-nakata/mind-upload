# Site Deepening Audit (2026-03-28, beginner tractography object split)

## 対象

- 主対象:
  - `wiki/mind-upload-basics.md`
  - `wiki/verification-basics.md`
- 同期対象:
  - `github-wiki-export/mind-upload-basics.md`
  - `github-wiki-export/verification-basics.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://mind-upload.com/wiki/mind-upload-basics.html`
- `https://mind-upload.com/wiki/verification-basics.html`
- `https://mind-upload.com/wiki/connectome-is-not-enough.html#tractography-route-card`
- `https://doi.org/10.1162/netn_a_00324`
- `https://doi.org/10.1016/j.neuroimage.2024.120904`
- `https://doi.org/10.1016/j.mri.2025.110424`
- `https://doi.org/10.1016/j.media.2025.103580`
- `https://doi.org/10.1016/j.media.2025.103498`
- `https://doi.org/10.3389/fnimg.2026.1670604`

## 今回この箇所を選んだ理由

- `wiki/connectome-is-not-enough.md` は、tractography route card を
  - acquisition / harmonization
  - cortical endpoint assignment
  - graph construction
  - instability / uncertainty
  - external calibration
  に分解しており、2023-2026 文献の更新を十分に反映していました。
- しかし入口ページである `wiki/mind-upload-basics.md` と `wiki/verification-basics.md` は、なお
  - `tractography = coarse structural prior`
  - `tractography claims need route disclosure`
  までは言えていても、
  - `その tractography graph 自体が一つの安定 object ではない`
  という更新を front door で固定できておりませんでした。
- このずれは技術・自然科学の観点で重要でございます。入口ページが粗いと、読者は `human tractography connectome` を `粗いが stable` と読めてしまい、深いページで止めている過読が入口で再流入するからでございます。

## 根拠付き批判

### 1. `macro pathway prior` だけでは、graph-conditioning の内訳がまだ隠れます

- [Gajwani et al. (2023)](https://doi.org/10.1162/netn_a_00324) は、`40 pipelines` と `44` の group-representative reconstructions で hub location の不一致を示しました。
- [He et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120904) は、tractogram filtering により structural-connectome laterality が有意に動くことを示しました。

批判:

- よって `tractography connectome is a macro pathway prior` だけでは、読者はなお `coarse だが stable graph` と誤読できます。
- beginner front door でも `hubness` や `laterality` 自体が pipeline-conditioned であることを明示する必要がございました。

### 2. voxel size と q-space sampling は implementation detail ではございません

- [McMaster et al. (2025)](https://doi.org/10.1016/j.mri.2025.110424) は voxel-size variance に対する harmonized resampling の必要性を示しました。
- [Bramati et al. (2026)](https://doi.org/10.3389/fnimg.2026.1670604) は、同じ `3 T` scanner・同じ processing でも diffusion sampling scheme の違いだけで voxel metrics と tractography outputs が動くことを示しました。

批判:

- これは `tractography result` を modality name だけで読むことが粗すぎることを意味します。
- 入口ページでも `acquisition / harmonization` を route meaning の一部として固定しなければ、protocol-conditioned object を anatomy と誤認させます。

### 3. uncertainty と hybrid calibration を入口で落とすと MRI-alone overread が戻ります

- [Manzano-Patrón et al. (2025)](https://doi.org/10.1016/j.media.2025.103580) は fibre-orientation uncertainty を tractography へ明示的に伝播させました。
- [Zhu et al. (2025)](https://doi.org/10.1016/j.media.2025.103498) は MRI に microscopy を加えた hybrid tractography で reconstruction を改善しました。

批判:

- 逆に言えば、`MRI-alone で graph が既に固定された` とは言えません。
- beginner page が uncertainty / external calibration を optional detail として扱う構造は、サイト全体の strict reading rule と不整合でございました。

### 4. beginner page の route-card 説明が粗いと、Verification Commons の定義自体が弱まります

- `wiki/verification-basics.md` は claim-specific route cards を教える入口ページでございます。
- ここで tractography route card を `be careful` 程度の注意喚起に留めると、route card が `object typing` ではなく `警告ラベル` に見えてしまいます。

批判:

- Verification Commons の入口では、tractography route card が `何を測ったか` だけでなく `何という inferential object を作ったか` を固定する装置だと示す必要がございました。

## 今回実行した変更

- `wiki/mind-upload-basics.md`
  - beginner front door に tractography object split を追加しました。
  - `page_highlights` / `known_points` を、human tractography connectome が `acquisition / endpoint / graph / uncertainty / calibration-conditioned` である形に更新しました。
  - 新しい note-box を追加し、hub instability, laterality shift, voxel-size / q-space dependence, uncertainty propagation, MRI-microscopy fusion を一つの route-card reason としてまとめました。
  - `Representative reasons` を改稿し、`coarse structural prior` だけでなく `not one stable graph` まで明文化しました。
  - 参考文献を追加しました。

- `wiki/verification-basics.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - `page_highlights` / `known_points` に tractography route-card の object-typing rule を追加しました。
  - 新しい note-box を追加し、tractography route card が caution ではなく object typing であることを明文化しました。
  - claim-specific route-card table の tractography row を、acquisition / endpoint / graph / uncertainty / calibration を分離した説明へ更新しました。
  - `Representative primary-literature reasons` を改稿し、2023-2026 tractography papers を反映しました。
  - 参考文献を追加しました。

- `github-wiki-export/mind-upload-basics.md`
  - 公開ページと同じ beginner tractography split を同期しました。

- `github-wiki-export/verification-basics.md`
  - 公開ページと同じ object-typing rule を同期しました。

## 今回止めた過読

- `human tractography connectome = coarse だが stable graph`
- `hub map` や `laterality` を connectome 本体の性質としてそのまま読む
- `voxel size` と `q-space sampling` を implementation detail として無視する
- `uncertainty propagation` や `hybrid MRI-microscopy calibration` を optional enhancement と読み、MRI-alone tractography の未解決誤差を忘れる
- `route card` を単なる caution label とみなし、inferential object の型付け装置として読まない

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Thomas C, Ye FQ, Irfanoglu MO, et al. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *PNAS*. 2014.
   - https://doi.org/10.1073/pnas.1405672111
2. Maier-Hein KH, Neher PF, Houde J-C, et al. The challenge of mapping the human connectome based on diffusion tractography. *Nature Communications*. 2017.
   - https://doi.org/10.1038/s41467-017-01285-x
3. Gajwani M, Oldham S, Pang JC, Arnatkevičiūtė A, Tiego J, Bellgrove MA, Fornito A. Can hubs of the human connectome be identified consistently with diffusion MRI? *Network Neuroscience*. 2023.
   - https://doi.org/10.1162/netn_a_00324
4. He Y, Hong Y, Wu Y, et al. Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. *NeuroImage*. 2024.
   - https://doi.org/10.1016/j.neuroimage.2024.120904
5. McMaster EM, Newlin NR, Rudravaram G, et al. Harmonized connectome resampling for variance in voxel sizes. *Magnetic Resonance Imaging*. 2025.
   - https://doi.org/10.1016/j.mri.2025.110424
6. Manzano-Patrón JP, Deistler M, Schröder C, et al. Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. *Medical Image Analysis*. 2025.
   - https://doi.org/10.1016/j.media.2025.103580
7. Zhu S, Huszar IN, Cottaar M, et al. Imaging the structural connectome with hybrid MRI-microscopy tractography. *Medical Image Analysis*. 2025.
   - https://doi.org/10.1016/j.media.2025.103498
8. Bramati IB, Szczupak D, Carneiro Monteiro M, Meireles F, Menezes Guimarães D, Dean RJ, Paul LK, Tovar-Moll F. Diffusion MRI sampling schemes bias diffusion metrics and tractography. *Frontiers in Neuroimaging*. 2026.
   - https://doi.org/10.3389/fnimg.2026.1670604
