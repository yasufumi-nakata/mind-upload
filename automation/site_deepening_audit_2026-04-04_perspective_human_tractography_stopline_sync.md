# Site Deepening Audit (2026-04-04, Perspective Human Tractography Stop-Line Sync)

## 対象

- 主対象: `perspective.md`

## 今回の選定理由

- 2026-04-04 時点の公開サイトでは、`index.md`、`wbe_101.md`、`verification.md`、`research_harvest_50.md`、`mind_uploading_papers.md` で、`living-human diffusion MRI tractography` を `finished connectome` と読ませない停止条件が既にかなり整っておりました。
- しかし長文の統合ノート `perspective.md` では、`structural scaffold` と `human connectome` の間にあるはずの `route-conditioned macro pathway prior` がまだ十分に前景化されておらず、ここが central page として相対的に弱くなっていました。
- この差は技術・自然科学の観点で重要でございます。なぜなら、`Perspective` は site-wide の長文統合ページであり、ここで `human connectome` の停止条件が弱いと、他ページで止めている過読がこのページだけで再発するからです。

## 主要な批判点

### 1. `Perspective` は structural scaffold の内部で `living-human tractography` をまだ十分に分離していませんでした

- 問題:
  - 現行ページは `volume EM / same-brain connectomics` と `living-human proxy families` を精密に分けていました。
  - しかし `living-human diffusion MRI tractography` 自体の ceiling は central table と central narrative に明示されておらず、`human connectome` という語が route-conditioned graph object を越えて読まれる余地が残っていました。
- 批判:
  - `structural scaffold` の中でも、
    - local destructive ultrastructure
    - sequential same-brain EM bridge
    - living-human diffusion-MRI tractography
    は別々の inferential object でございます。
  - この三者を分けないと、`human structural evidence advanced` が `human connectome is getting close to completion` へ不正に滑ります。

### 2. 一次文献は tractography graph が one stable object ではないことを明示しています

- 根拠:
  - Thomas et al. (2014) は、voxel-averaged local orientations のみから構成される tractography の anatomical accuracy が inherently limited であることを示しました。
  - Gajwani et al. (2023) は `1,760 group connectomes` を比較し、hub location / strength が tractography algorithm、parcellation、group reconstruction choice によって大きく動くことを示しました。
  - McMaster et al. (2025) は HCP-YA scan/rescan data を用い、voxel resolution を変えるだけで connectome graph measures が有意に動くことを示し、robust comparison のために `1 mm isotropic` への resampling を推奨しました。
  - Bramati et al. (2026) は same 3 T scanner と fixed preprocessing のもとでも、common diffusion-sampling schemes が tractography outputs を動かすことを示しました。
- 批判:
  - よって `human tractography connectome` を route-free graph truth と読むのは不正確でございます。
  - 強く言えるのは `acquisition-conditioned macro pathway prior`、よくて `targeted bundle-hypothesis route` または `calibrated bundle comparison` までです。

### 3. MRI-only tractography の改善は calibration route の改善であり、finished connectome の達成ではありません

- 根拠:
  - Zhu et al. (2025) は microscopy-informed hybrid MRI-microscopy tractography によって reconstruction を改善しました。
  - これは `MRI tractography alone became sufficient` ではなく、むしろ `explicit microscopy calibration shrinks one tractography error term` を示しております。
- 批判:
  - したがって、hybrid improvement を `living-human connectome is now close` と読むのも過読でございます。
  - 正しい読みに直すと、`external calibration matters because MRI-only tractography remains insufficiently constrained` です。

## 今回実行した変更

- `perspective.md`
  - front matter の `note` に `2026-04-04 human-tractography stop-line sync` を追加
  - `page_highlights` に `living-human tractography` の ceiling を追加
  - `known_points` に `current living-human tractography evidence is route-conditioned` を追加
  - measurement-stack table に `Human diffusion-MRI tractography connectome` の新規行を追加
  - central note-box を追加し、`Thomas 2014 -> Gajwani 2023 -> McMaster 2025 -> Bramati 2026 -> Zhu 2025` という一次文献列から
    - endpoint / graph-construction dependence
    - voxel-resolution dependence
    - q-space sampling dependence
    - calibration dependence
    を明示
  - `Key Technical Challenges` の `Gap between connectome and dynamics` に tractography paragraph を追加し、`human connectome` 語の停止条件を central narrative でも明示
  - 参考文献に tractography 関連 5 文献を追加

## この修正で防げる過読

- `human tractography graph exists -> the human connectome is becoming complete`
- `hub map exists -> hub organization is stable across pipelines`
- `higher resolution MRI exists -> connectome graph is invariant enough for strong structural claims`
- `same scanner / same preprocessing -> tractography output is route-free`
- `hybrid MRI-microscopy improved reconstruction -> MRI-only tractography is nearly sufficient`

## 外部依存で保留

- なし
  - 今回の作業は、このセッション内で文献確認・ページ改稿・ビルド検証・Git 反映まで完結可能でございます。

## Web で確認した一次文献

1. Thomas C, Ye FQ, Irfanoglu MO, et al. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *PNAS*. 2014.
   - https://doi.org/10.1073/pnas.1405672111
2. Gajwani M, Oldham S, Pang JC, et al. Can hubs of the human connectome be identified consistently with diffusion MRI? *Network Neuroscience*. 2023.
   - https://doi.org/10.1162/netn_a_00324
3. McMaster EM, Newlin NR, Rudravaram G, et al. Harmonized connectome resampling for variance in voxel sizes. *Magnetic Resonance Imaging*. 2025.
   - https://doi.org/10.1016/j.mri.2025.110424
4. Bramati IB, Szczupak D, Monteiro MC, et al. Diffusion MRI sampling schemes bias diffusion metrics and tractography. *Frontiers in Neuroimaging*. 2026.
   - https://doi.org/10.3389/fnimg.2026.1670604
5. Zhu S, Huszar IN, Cottaar M, et al. Imaging the structural connectome with hybrid MRI-microscopy tractography. *Medical Image Analysis*. 2025.
   - https://doi.org/10.1016/j.media.2025.103498

## 実施した検証

- `git diff --check`
  - pass
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - pass
- `rg -n "human tractography|macro pathway prior|targeted bundle-hypothesis|calibrated bundle comparison" perspective.md`
  - pass
