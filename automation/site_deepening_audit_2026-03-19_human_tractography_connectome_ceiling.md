# Site Deepening Audit (2026-03-19, Human Tractography Connectome Ceiling)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `wbe_101.md`
- 副対象: `faq.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、`connectome-complete != emulation-complete`、hidden-state class、connectome-constrained degeneracy についてはかなり強く整理できておりました。
- その一方で、`human in vivo connectome` という読者の最短誤読に対して、`diffusion-MRI tractography` を独立した evidence class として十分に固定していませんでした。
- この不備は技術・自然科学の観点で重要です。なぜなら、EM connectome・same-brain local scaffold・connectome-constrained model の議論が強くなるほど、読者が `human tractography connectome` まで同じ語のまま引き上げて読みやすくなるからです。

## 根拠付き批判

### 1. `connectome progress` の evidence-class split が human tractography route を独立扱いしていませんでした

- 問題:
  - 旧 `wiki/connectome-is-not-enough.md` と `wbe_101.md` は、`wiring atlas / same-brain local scaffold / connectome-constrained conditional predictor / identifiability audit` の 4 分類を採用していました。
  - しかし、living human brain で多くの読者が最初に想起する `tractography-derived connectome` が、その 4 分類のどこに入るのかが曖昧でした。
- 根拠:
  - Thomas et al. (2014) は、例外的に高品質な ex vivo macaque diffusion data でも tractography の anatomical accuracy に本質限界があると示しました。
  - Reveley et al. (2015) は、superficial white matter が long-range cortical tracking を大きく阻害すると示しました。
  - Donahue et al. (2016) は、tracer との比較で tractography が useful predictive power を持つ一方で、接続強度の代理としては依然不完全であると示しました。
- 批判:
  - したがって `connectome` を 1 語で扱うだけでは、`synapse-resolved structural atlas` と `macro pathway prior` の差が消えます。
  - 公開サイト側では、human tractography route を独立 class として front door に置く必要がありました。

### 2. 旧 front door は `human tractography` の safe reading を固定していませんでした

- 問題:
  - 旧 `wbe_101.md` の human observability ladder は、nanoscale ultrastructure, PET, MRSI, ionic, thermal, myelin, perturbation proxies を並べていました。
  - しかし、human tractography-derived connectome が `macro pathway prior` であり `edge-complete graph` ではないことを、同じ ladder 上で示していませんでした。
- 根拠:
  - Maier-Hein et al. (2017) の open challenge では、ground-truth bundles の多くをある程度回収できても、systematic false-positive bundles が多数残り、その 64% は ground truth に存在しませんでした。
  - Schilling et al. (2020) は、high accuracy が出るのは start/end/exclusion の強い anatomical priors を与えた場合であると示しました。
  - Grisot et al. (2021) は、same-brain validation でも branching / turning geometry に recurring failure modes があると示しました。
- 批判:
  - つまり tractography は `completely useless` でも `nearly complete human connectome` でもありません。
  - 最も安全な読解は、`bundle-level hypothesis / macro pathway prior` として扱うことでした。

### 3. FAQ の `If we know the connectome and cell type...` が human tractography 誤読を十分に止めていませんでした

- 問題:
  - 旧 FAQ は hidden-state classes を強く説明していましたが、`そもそもその connectome が tractography-based なら何段階下がるのか` を明文化していませんでした。
- 根拠:
  - Thomas et al. (2014), Reveley et al. (2015), Donahue et al. (2016), Schilling et al. (2020), Grisot et al. (2021) は、tractography route の到達点をかなり具体的に限定しています。
- 批判:
  - FAQ 入口でこの clause がないと、読者は `connectome + hidden states` の話に入る前に、tractography product を `graph itself` として誤認する余地が残ります。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `connectome progress` を 4 class から 5 class に改稿し、`human macro pathway prior / tractography connectome` を追加しました。
  - `Human diffusion-MRI connectome is still a macro pathway prior` 節を新設し、tractography validation literature に基づく safe reading rule を明文化しました。
  - 結論・page highlights・known points も同じ読解に揃えました。
  - 参考文献へ Thomas (2014), Reveley (2015), Donahue (2016), Maier-Hein (2017), Schilling (2020), Grisot (2021) を追加しました。
- `wbe_101.md`
  - hidden-state 導入部へ `tractography-derived human connectome` の ceiling paragraph を追加しました。
  - human observability ladder に `Human diffusion-MRI tractography / macro connectome prior` の行を追加しました。
  - `Do not collapse connectome progress into one rung` を 5 class に更新しました。
  - 参考文献へ tractography validation papers を追加しました。
- `faq.md`
  - Q2c に `If by connectome one means human diffusion-MRI tractography...` の paragraph を追加しました。
  - human evidence ladder の短答にも `diffusion-MRI tractography-based macro pathway priors` を加え、safe reading を front door 側へ同期しました。
  - 参考文献へ tractography validation papers を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・根拠・引用整合の改稿で完結しています。

## 参考文献

1. Thomas C, Ye FQ, Irfanoglu MO, Modi P, Saleem KS, Leopold DA, Pierpaoli C. Anatomical accuracy of brain connections derived from diffusion MRI tractography is inherently limited. *PNAS*. 2014;111(46):16574-16579.
   - https://doi.org/10.1073/pnas.1405672111
2. Reveley C, Seth AK, Pierpaoli C, Silva AC, Yu D, Saunders RC, Leopold DA, Ye FQ. Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion MR tractography. *PNAS*. 2015;112(21):E2820-E2828.
   - https://doi.org/10.1073/pnas.1418198112
3. Donahue CJ, Sotiropoulos SN, Jbabdi S, Hernandez-Fernandez M, Behrens TE, Dyrby TB, Coalson T, Kennedy H, Knoblauch K, Van Essen DC, Glasser MF. Using diffusion tractography to predict cortical connection strength and distance: A quantitative comparison with tracers in the monkey. *Journal of Neuroscience*. 2016;36(25):6758-6770.
   - https://doi.org/10.1523/JNEUROSCI.0493-16.2016
4. Maier-Hein KH, Neher PF, Houde JC, Côté MA, Garyfallidis E, Zhong J, Chamberland M, et al. The challenge of mapping the human connectome based on diffusion tractography. *Nature Communications*. 2017;8:1349.
   - https://doi.org/10.1038/s41467-017-01285-x
5. Schilling KG, Petit L, Rheault F, Remedios S, Pierpaoli C, Anderson AW, Landman BA, Descoteaux M. Brain connections derived from diffusion MRI tractography can be highly anatomically accurate if we know where white matter pathways start, where they end, and where they do not go. *Brain Structure and Function*. 2020;225(8):2387-2402.
   - https://doi.org/10.1007/s00429-020-02129-z
6. Grisot G, Haber SN, Hawrylycz M, Yendiki A, et al. Diffusion MRI and anatomic tracing in the same brain reveal common failure modes of tractography. *NeuroImage*. 2021;239:118300.
   - https://doi.org/10.1016/j.neuroimage.2021.118300
