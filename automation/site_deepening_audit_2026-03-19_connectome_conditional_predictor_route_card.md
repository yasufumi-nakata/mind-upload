# Site Deepening Audit (2026-03-19, Connectome-Constrained Conditional Predictor Route Card)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、`connectome-complete != emulation-complete`、hidden-state class、tractography ceiling、effective-connectivity route card まではかなり強く整理できておりました。
- その一方で、`connectome-constrained model` だけは、`conditional predictor / hypothesis engine` としての位置づけ自体は書かれていても、`では何を開示しない限り強い claim に昇格させないか` が route-card 形式で固定されておりませんでした。
- この欠落は技術・自然科学の観点で重要です。なぜなら、近年の connectomics 論文で最も誤読されやすいのは `配線制約つきでよく当たる` ことを `hidden state がほぼ回収された` と読み替える点だからです。

## 根拠付き批判

### 1. `connectome-constrained predictor` は structural scaffold と internal-state recovery の中間物であり、提出物なしでは過大読みに耐えません

- 問題:
  - 既存サイトは `connectome-constrained conditional predictor` という evidence class を導入していました。
  - しかし、その class をどう読むべきかは本文説明に留まり、tractography / DCM / thermodynamic claim のような route-card にはなっていませんでした。
- 根拠:
  - Lappalainen et al. (2024) は、fly visual system の partial connectome, periodic tiling, simplified single-compartment neurons, threshold-linear synapses, 734 free parameters, 50 local optima という条件で activity prediction を前進させました。
  - つまり前進は real ですが、`全部を直接見た` でも `一意復元した` でもございません。
- 批判:
  - よって `connectome-constrained` というラベルだけでは不足です。
  - 少なくとも `どの structural prior を使ったか`, `何が未観測のまま学習されたか`, `どの task/state regime で検証したか` を出さない限り、強い読みは止めるべきでした。

### 2. recent flagship papers 自体が「条件付き成功」であることを明示しています

- 問題:
  - 読者は high-profile paper の成功を、そのまま一般的な mechanistic recovery と読みやすい構造にあります。
- 根拠:
  - Shiu et al. (2024) は、whole-fly connectome と neurotransmitter identity から feeding / grooming の sensorimotor transformation を予測しましたが、結果は coarse-level の circuit description として書かれています。
  - Pospisil et al. (2024) は、connectome を prior に使った perturbation-based effectome を提案しましたが、recover しているのは nonlinear dynamics そのものではなく linear approximation です。
  - Beiran & Litwin-Kumar (2025) は、同じ synaptic weights でも biophysical parameters が違えば recurrent dynamics が大きくずれうること、少数 recording でその degeneracy を減らせることを示しました。
  - Prinz et al. (2004) は、かなり異なる parameter set から virtually indistinguishable network activity が生じうることを示しました。
- 批判:
  - したがって、`予測が当たった` は `隠れ状態がほぼ決まった` ことを意味しません。
  - 正しい読解は、`ある structural prior とある task family の下で、候補空間をかなり絞った conditional model が得られた` です。

### 3. Verification 側に route-card がないと、front door の厳密さが submission rule に落ちません

- 問題:
  - `verification.md` は tractography, DCM, thermodynamic claims には route card を持っていました。
  - しかし connectome-constrained predictor には対応する提出物がありませんでした。
- 根拠:
  - 同ページは Observability Budget を `what was directly observed` の提出物に変換しており、ここで conditional predictor だけ exempt にすると、最も強く見える recent connectomics success が例外になります。
- 批判:
  - 技術・自然科学の側面だけで読むなら、ここを例外扱いする理由はございません。
  - `structural prior`, `fitted degrees of freedom`, `task/state regime`, `omitted mechanisms`, `validation class`, `abstention boundary` を route-card 化して初めて、サイト内の claim ceiling が一貫します。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `page_highlights` に `conditional-model route card` を追加
  - 新規節 `Connectome-constrained predictors need a conditional-model route card` を追加
  - route-card table を追加し、`structural prior`, `fitted degrees of freedom`, `task/state regime`, `omitted mechanisms`, `validation class`, `equivalence class / abstention` を必須開示項目として固定
  - 参考文献に Shiu (2024), Pospisil (2024), Prinz (2004) を追加
- `verification.md`
  - front matter の `page_highlights` / `known_points` に `conditional-model route card` を追加
  - Observability Budget に `connectome-constrained predictors need a conditional-model route card` addendum と table を追加
  - `Minimum operating rules` に `conditional-model route card` 不在時の claim ceiling を追加
  - `Additional audit logs` に `Connectome-Constrained Model Card` を追加
  - 参考文献に Shiu (2024), Pospisil (2024) を追加
- `wbe_101.md`
  - 入口節に `Connectome-constrained predictors need a route card` note を追加
  - 詳細 rule への導線を `wiki/connectome-is-not-enough.html#conditional-predictor-route-card` と `verification.html#observability-budget` に接続

## 外部依存で保留

- なし
  - 今回の作業は公開本文・Verification rule・Wiki export の改稿で完結しております。

## 参考文献

1. Lappalainen JK, Tschopp FD, Prakhya S, et al. Connectome-constrained networks predict neural activity across the fly visual system. *Nature*. 2024;634:1132-1140.
   - https://doi.org/10.1038/s41586-024-07939-3
2. Shiu P-K, Bates AS, et al. A Drosophila computational brain model reveals sensorimotor processing. *Nature*. 2024;634:210-219.
   - https://doi.org/10.1038/s41586-024-07763-9
3. Pospisil DA, Aragon MJ, Dorkenwald S, et al. The fly connectome reveals a path to the effectome. *Nature*. 2024;634:201-209.
   - https://doi.org/10.1038/s41586-024-07982-0
4. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
5. Prinz AA, Bucher D, Marder E. Similar network activity from disparate circuit parameters. *Nature Neuroscience*. 2004;7:1345-1352.
   - https://doi.org/10.1038/nn1352
