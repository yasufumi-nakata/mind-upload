# Site Deepening Audit (2026-03-28, measurement-stack tractography ceiling)

## 対象

- 主対象:
  - `wiki/measurement-stack-and-claim-ceiling.md`
- 同期対象:
  - `github-wiki-export/measurement-stack-and-claim-ceiling.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://mind-upload.com/wiki/measurement-stack-and-claim-ceiling.html`
- `https://mind-upload.com/wiki/connectome-is-not-enough.html#tractography-route-card`
- `https://doi.org/10.1073/pnas.1418198112`
- `https://doi.org/10.1002/hbm.23936`
- `https://doi.org/10.1162/netn_a_00324`
- `https://doi.org/10.1016/j.neuroimage.2024.120904`
- `https://doi.org/10.1016/j.mri.2025.110424`
- `https://doi.org/10.3389/fnimg.2026.1670604`
- `https://doi.org/10.1016/j.media.2025.103580`
- `https://doi.org/10.1016/j.media.2025.103498`

## 今回この箇所を選んだ理由

- `wiki/measurement-stack-and-claim-ceiling.md` は、サイト全体で「何が直接観測され、どこで claim ceiling が止まるか」を固定する中核ページでございます。
- しかし 2026-03-28 時点の live page には、`diffusion MRI tractography / structural connectome` の行が存在しておりませんでした。
- そのため、他ページではすでに止めている
  - `human tractography connectome = one stable graph`
  - `connectome row がある = measurement-stack 上も object が確定している`
  という過読が、この中央ページだけで再流入しておりました。

## 根拠付き批判

### 1. measurement-stack table に tractography row がないと、connectome だけ modality-free に見えてしまいます

- 根拠:
  - live page `https://mind-upload.com/wiki/measurement-stack-and-claim-ceiling.html` では、EEG / MEG, fMRI, atlas, Patch-seq, volume EM, same-brain functional connectomics, PET, glia imaging までは row がある一方、human dMRI tractography row がありませんでした。
  - 一方、`https://mind-upload.com/wiki/connectome-is-not-enough.html#tractography-route-card` では既に、tractography connectome は `acquisition-, endpoint-, graph-construction-, and calibration-conditioned estimate` として厳密化されております。
- 批判:
  - これは site-wide に不整合でございます。中央の ceiling table で row が抜けると、読者は tractography だけを measurement-conditioned object ではなく、`connectome` という名の quasi-fixed object として読みやすくなります。

### 2. tractography graph 自体が pipeline-conditioned ですので、measurement-stack 側で止める必要があります

- 根拠:
  - [Gajwani et al. (2023)](https://doi.org/10.1162/netn_a_00324) は、`40 pipelines` と `44` group-representative reconstructions で hub location が高く変動することを示しました。
  - [He et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120904) は、tractogram filtering が structural-connectome laterality を有意に動かすことを示しました。
- 批判:
  - したがって `tractography connectome` を measurement stack table に無記載のまま残すと、graph construction の条件付き object であることが見えません。
  - `measurement stack` という名前を使う以上、tractography graph が `signal -> endpoint -> parcel graph` の変換を経た inferential object であることを table 自体に書く必要がございました。

### 3. acquisition / harmonization は tractography では implementation detail ではございません

- 根拠:
  - [McMaster et al. (2025)](https://doi.org/10.1016/j.mri.2025.110424) は voxel-size variance に対して harmonized connectome resampling を導入しました。
  - [Bramati et al. (2026)](https://doi.org/10.3389/fnimg.2026.1670604) は、同じ 3 T scanner・同じ processing でも q-space sampling scheme が diffusion metrics と tractography outputs を動かすことを示しました。
- 批判:
  - これは measurement-stack page が tractography を row に持たないと、読者が `dMRI connectome` を modality label だけで読んでしまうことを意味します。
  - 中央ページで `protocol-scoped object` と書かない限り、他ページで加えた protocol audit rule が抜け落ちます。

### 4. uncertainty / calibration の扱いも measurement stack の ceiling に含める必要がありました

- 根拠:
  - [Manzano-Patrón et al. (2025)](https://doi.org/10.1016/j.media.2025.103580) は tractography の uncertainty mapping を classical Bayes と比較しつつ明示化しました。
  - [Zhu et al. (2025)](https://doi.org/10.1016/j.media.2025.103498) は hybrid MRI-microscopy tractography により reconstruction 改善を示しました。
- 批判:
  - 逆に言えば、uncertainty-aware tractography や hybrid calibration は tractography chain の一部改善であって、living-human edge-complete connectome 完成ではございません。
  - この stop line は `connectome-is-not-enough` だけでなく、measurement-stack の ceiling table にも必要でございました。

## 今回実行した変更

- `wiki/measurement-stack-and-claim-ceiling.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `description` / `page_intro` / `page_highlights` / `known_points` を、tractography row が中央ページでも見える形に同期しました。
  - measurement-stack table に `diffusion MRI tractography / structural connectome` row を追加しました。
  - 新しい本文節 `4.6. Human diffusion MRI tractography is a route-conditioned macro pathway prior, not one stable graph` を追加しました。
  - endpoint / graph-construction / acquisition-harmonization / uncertainty-calibration の 4 壁を表にし、site rule を明記しました。
  - tractography route card への運用リンクを追加しました。
  - 参考文献を追加しました。

- `github-wiki-export/measurement-stack-and-claim-ceiling.md`
  - 公開ページと同じ tractography ceiling を同期しました。

## 今回止めた過読

- `measurement stack table に row がない` = tractography は measurement-conditioned object ではない
- `human tractography connectome` = one stable graph
- `hubness` や `laterality` = anatomy そのもの
- `dMRI protocol` = implementation detail で graph meaning には影響しない
- `uncertainty-aware` や `MRI-microscopy hybrid` = living-human connectome completion

## 外部依存タスク

- なし
  - 今回の作業は repo 内文書、wiki export、監査記録、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Reveley C, Seth AK, Pierpaoli C, Silva AC, Yu D, Saunders RC, Leopold DA, Ye FQ. Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. *PNAS*. 2015;112(21):E2820-E2828.
   - https://doi.org/10.1073/pnas.1418198112
2. Schilling KG, Gao Y, Janve V, Stepniewska I, Landman BA, Anderson AW. Confirmation of a gyral bias in diffusion MRI fiber tractography. *Human Brain Mapping*. 2018;39(3):1449-1466.
   - https://doi.org/10.1002/hbm.23936
3. Gajwani M, Oldham S, Pang JC, Arnatkevičiūtė A, Tiego J, Bellgrove MA, Fornito A. Can hubs of the human connectome be identified consistently with diffusion MRI? *Network Neuroscience*. 2023;7(4):1326-1350.
   - https://doi.org/10.1162/netn_a_00324
4. He Y, Hong Y, Wu Y, et al. Spherical-deconvolution informed filtering of tractograms changes laterality of structural connectome. *NeuroImage*. 2024;303:120904.
   - https://doi.org/10.1016/j.neuroimage.2024.120904
5. McMaster EM, Newlin NR, Rudravaram G, et al. Harmonized connectome resampling for variance in voxel sizes. *Magnetic Resonance Imaging*. 2025;121:110424.
   - https://doi.org/10.1016/j.mri.2025.110424
6. Bramati IB, Szczupak D, Carneiro Monteiro M, Meireles F, Menezes Guimarães D, Dean RJ, Paul LK, Tovar-Moll F. Diffusion MRI sampling schemes bias diffusion metrics and tractography. *Frontiers in Neuroimaging*. 2026;5:1670604.
   - https://doi.org/10.3389/fnimg.2026.1670604
7. Manzano-Patrón JP, Deistler M, Schröder C, et al. Uncertainty mapping and probabilistic tractography using Simulation-based Inference in diffusion MRI: A comparison with classical Bayes. *Medical Image Analysis*. 2025;103:103580.
   - https://doi.org/10.1016/j.media.2025.103580
8. Zhu S, Huszar IN, Cottaar M, et al. Imaging the structural connectome with hybrid MRI-microscopy tractography. *Medical Image Analysis*. 2025;102:103498.
   - https://doi.org/10.1016/j.media.2025.103498
