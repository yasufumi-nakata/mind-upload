# 2026-03-31 site deepening audit: observation-to-estimation inverse-family route card

## 対象として選んだ箇所

- `wiki/observation-to-estimation.md`
- `verification.md`

今回ここを優先した理由は、公開サイト全体の中でこの 2 ページが `inverse problem` / `ESI` の停止条件を定義しており、ここが粗いままだと他ページでどれだけ慎重な記述をしていても、読者が `better solver = better truth` と再解釈しやすいためです。

## 根拠付き批判

### 1. 現状の公開記述は「単一ソルバを真理扱いしない」まではできていましたが、「inverse family ごとに推定対象が違う」点の切り分けがまだ弱いです

- 既存文面は、`cross-solver / cross-parameter spread` を出すことまでは要求していました。
- しかし、この書き方だけでは `different inverse families are all estimating the same object, so disagreement is just one more variance term` という誤読が残ります。
- これは一次文献の読み方として粗いです。少なくとも以下は別物です。
  - [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753): posterior support と alternative configurations を返す probabilistic route
  - [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596): sparse spatial-temporal source imaging に対する debiased estimation / inference
  - [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620): extended source reconstruction に対する empirical-Bayesian uncertainty quantification
- したがって、`inverse-family disagreement` を 1 個の generic spread として扱うのは不正確です。

### 2. forward-model uncertainty と inverse-family progress は独立監査であるべきです

- [Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212) は、tissue conductivity uncertainty が depth と location を動かすことを示しています。
- つまり `posterior-aware solver` があることと、`conductivity/head-model uncertainty を十分に処理した` ことは別です。
- この区別が弱いと、見栄えの良い posterior map が upstream physics の未監査部分まで代表しているかのように見えてしまいます。

### 3. validation は solver 名ではなく operating regime に紐づきます

- [Mikulan et al. (2020)](https://doi.org/10.1038/s41597-020-0467-x) は precisely known stimulation site を使う board です。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は simultaneous HD-EEG/SEEG concordance を見る board です。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は extended-source reconstruction の board を扱っています。
- これらは同じ誤差対象ではありません。よって `validation passed` ではなく、`which board for which source regime` を公開文面側で固定する必要があります。

### 4. この弱点は front door より core policy ページで直すのが合理的です

- 既に周辺ページでは近い論点が整備されています。
- それでも `observation-to-estimation` と `verification` が generic wording のままだと、公開サイトの中心規範が緩いまま残ります。
- したがって今回の最優先修正は、「どの family が強いか」ではなく、「family ごとに何を推定し、どの不確実性を返し、どの board で読まれるのか」を core page に固定することでした。

## 今回実行した変更

### `wiki/observation-to-estimation.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `page_highlights` / `known_points` を、`probabilistic / debiased / extent-aware` family が同じ claim object を返すわけではないと明示する文言へ修正しました。
- ESI セクションに `2026-03-31 deepening: inverse-family labels still hide different source regimes and uncertainty objects` を追加しました。
- その直下に `Inverse-family route-card` table を追加し、最低限必要な監査項目を
  - `source regime and target object`
  - `uncertainty object`
  - `forward-model uncertainty route`
  - `validation board / operating regime`
  - `cross-family comparison rule`
  - `abstention boundary`
  の 6 項目で固定しました。
- references に `Luria 2024` と `Tong 2025` を追加しました。

### `verification.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `known_points` に、inverse family によって uncertainty object も変わることを反映しました。
- ESI 節に `2026-03-31 addendum: solver disagreement is not one generic number` を追加しました。
- `Inverse-Solver Agreement Log` の必須項目を拡張し、
  - `source regime / target object`
  - `uncertainty object`
  - `forward-model uncertainty route or fixed conductivity policy`
  - `named validation board / operating regime`
  を明示的に要求するよう更新しました。

## 今回止めた誤読

- `solver disagreement を出した = inverse family difference の本質も十分公開した`
- `probabilistic / debiased / extent-aware` を 1 本の進歩バーとして読める
- `better uncertainty map = forward-model uncertainty もほぼ監査済み`
- `ある validation board で強い = source regime を超えて強い`

## 検証

- `bundle exec jekyll build` を実行して、ビルドが通ることを確認します。
- 差分は `git diff --stat` と要点 diff で確認します。

## external dependency tasks

- 今回の主作業に関して、外部依存で止めた項目はありません。

## 参考文献

1. Mahjoory K, Nikulin VV, Botrel L, et al. Consistency of EEG source localization and connectivity estimates. *NeuroImage*. 2017. [https://doi.org/10.1016/j.neuroimage.2017.02.076](https://doi.org/10.1016/j.neuroimage.2017.02.076)
2. Mikulan E, Russo S, Bares M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020. [https://doi.org/10.1038/s41597-020-0467-x](https://doi.org/10.1038/s41597-020-0467-x)
3. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024. [https://doi.org/10.3389/fnhum.2024.1335212](https://doi.org/10.3389/fnhum.2024.1335212)
4. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024. [https://doi.org/10.3389/fnhum.2024.1359753](https://doi.org/10.3389/fnhum.2024.1359753)
5. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025. [https://doi.org/10.1109/TMI.2024.3506596](https://doi.org/10.1109/TMI.2024.3506596)
6. Feng Z, Mishne G, Hashemi A, et al. Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. *IEEE Transactions on Medical Imaging*. 2025. [https://doi.org/10.1109/TMI.2025.3642620](https://doi.org/10.1109/TMI.2025.3642620)
7. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025. [https://doi.org/10.1111/epi.18552](https://doi.org/10.1111/epi.18552)
