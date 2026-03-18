# Site Deepening Audit (2026-03-18, Human Ionic Proxy Boundary)

## 対象

- 主対象: `wbe_101.md`
- 副対象: `index.md`
- 副対象: `faq.md`
- 副対象: `verification.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`ionic milieu / chloride homeostasis` を重要な hidden-state としてかなり強く扱えておりました。
- しかし front door の human observability 導線では、human 側の `ionic route` がまだ十分に見えていませんでした。
- これは技術・自然科学の観点で粗さが残る点でございます。なぜなら読者が
  - `human では ionic route が全く無い`
  - `human sodium MRI があるなら chloride homeostasis もかなり読める`
  の両方向へ誤読しうるからです。

## 根拠付き批判

### 1. 旧 front door は `ionic hidden state` を強調する一方、human 側の proxy class を 1 段飛ばしていました

- 問題:
  - `wbe_101.md` と `index.md` は、chloride homeostasis が inhibitory sign や state transition に効くことを正しく強調していました。
  - しかし human observability ladder では `macro ionic proxy` が欠けており、biochemical / energetic / thermal / myelin / clearance の間に `ionic` だけが落ちていました。
- 根拠:
  - Qian et al. (2012) は human brain で 7T sodium MRI による高分解能 sodium imaging を示しました。
  - Rodriguez et al. (2022) は simultaneous `1H / 23Na` MRI の repeatability を human brain で示しつつ、現行 sodium MRI が主に `total sodium concentration` や sodium density-weighted 指標を扱うことを明示しました。
  - Qian et al. (2025) は 3T single-quantum sodium MRI による mono- / bi-T2 sodium signal separation を示しましたが、同時に mono- / bi-T2 population が intra- / extracellular を一意に分けるわけではないこと、TSC がなお voxel-level proxy であることも示しました。
- 批判:
  - したがって human 側には確かに `ionic route` がございます。
  - しかしそれは `macro ionic proxy` であって、`current chloride set point` や `local E_GABA` の ground truth ではありません。

### 2. 旧 FAQ は energetic / thermal proxy を説明できていましたが、ionic proxy の位置づけだけが抜けていました

- 問題:
  - `faq.md` の Q2c は energetic proxy と thermal proxy まで丁寧に整理していました。
  - 一方で human sodium MRI の位置づけが無かったため、`ionic hidden state` の話だけが human evidence ladder から切れておりました。
- 批判:
  - FAQ は front door でございますので、ここで `ionic route は存在するが粗い` を短く固定しないと、読者は `ionic は完全に unseen` か `ionic もほぼ見えている` のどちらかへ振れやすくなります。

### 3. 旧 Verification の human evidence class は wiki と完全同期していませんでした

- 問題:
  - `verification.md` は maintenance-state error budget で `sodium / macro ionic proxy` を個別に扱っていました。
  - それにもかかわらず、human evidence class の一覧では `macro ionic proxy` が抜け、wiki 側の class list と不整合でした。
- 批判:
  - これは提出仕様の弱さでございます。
  - submission 側で ionic proxy を separate field として要求するなら、class-labeled submission の方にも `macro ionic proxy` を明示しなければなりません。

## 今回実行した変更

- `index.md`
  - landing page の human evidence summary に `ionic` を追加
  - human observability note で `current chloride set point` を still-missing route に追加
- `wbe_101.md`
  - front matter の human evidence summary を `ionic` 含みへ更新
  - known points に `current chloride homeostasis` の未達を追加
  - human observability ladder に `Human sodium MRI / ionic proxy` 行を追加
  - entry rule と measurement-stack note に `ionic proxy` の読み方を追加
  - 参考文献に Qian et al. (2012), Qian et al. (2025) を追加
- `faq.md`
  - Q2c に `human sodium MRI = macro ionic proxy` の説明を追加
  - human ladder の summary に `ionic` を追加
  - 参考文献に Qian et al. (2012), Qian et al. (2025) を追加
- `verification.md`
  - human evidence class を `macro biochemical / energetic / ionic / thermal / myelin / support proxy` へ更新
  - addendum の class list に `macro ionic proxy` と `macro thermal proxy` を追加

## 外部依存で保留

- なし
  - 今回の作業は、一次文献確認と公開本文・提出仕様の改稿で完結しております。

## 参考文献

1. Qian Y, Zhao T, Zheng H, Weimer J, Boada FE. High-resolution sodium imaging of human brain at 7 T. *Magnetic Resonance in Medicine*. 2012.
   - https://doi.org/10.1002/mrm.23225
2. Rodriguez GG, Yu Z, O'Donnell LF, et al. Repeatability of simultaneous 3D 1H MRF/23Na MRI in brain at 7 T. *Scientific Reports*. 2022.
   - https://doi.org/10.1038/s41598-022-18388-1
3. Qian Y, Lin Y-C, Chen X, et al. Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. *Scientific Reports*. 2025.
   - https://doi.org/10.1038/s41598-025-07800-1
4. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014.
   - https://doi.org/10.1126/science.1245423
5. Heubl M, Zhang J, Pressey JC, et al. GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. *Nature Communications*. 2017.
   - https://doi.org/10.1038/s41467-017-01749-0
6. Ding F, O'Donnell J, Xu Q, et al. Changes in the composition of brain interstitial ions control the sleep-wake cycle. *Science*. 2016.
   - https://doi.org/10.1126/science.aad4821
