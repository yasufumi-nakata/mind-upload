# 2026-03-31 site deepening audit: tech roadmap identifiability stop rule

## 対象として選んだ箇所

- `tech_roadmap.md`
- 参照して整合性を確認した箇所:
  - `verification.md`
  - `wiki/observation-to-estimation.md`

## 今回ここを優先した理由

- 2026-03-31 時点の公開サイトは、`index.md`、`verification.md`、`wiki/observation-to-estimation.md` ではすでに
  - `ambiguity class`
  - `experiment-design leverage`
  - `minimum-sufficiency stop rule`
  をかなり明示的に扱っておりました。
- しかし、公開サイトの中心的 dependency map である `tech_roadmap.md` の `R7` は、
  - `observability`
  - `structural identifiability`
  - `practical identifiability`
  の三層化までは強かった一方で、
  - 何の ambiguity が残っているのか
  - どの設計目的で次の条件を選んだのか
  - どこでデータ取得を止めてよいのか
  が本文としてはまだ弱く、`more modalities`, `more tasks`, `more data` を generic identifiability gain と読み替える余地が残っておりました。

## 根拠付き批判

### 1. 現状の `R7` は「一意解ではない」を言えていましたが、「なぜ一意解でないのか」の型分けが core page で不足しておりました

- 既存 `R7` は five-step audit を示しており、方向性は正確でございました。
- ただし、そのままでは読者が
  - `same fit but different parameters`
  - `same fit but omitted mechanism`
  - `same fit but narrow-regime degeneracy`
  - `same fit but wrong representation`
  を全部ひとまとめに `need more data`
  と読めてしまいます。
- 一次文献はその読み方を支持しておりません。
  - [Massonis & Villaverde (2020)](https://doi.org/10.3390/sym12030469): structural unidentifiability can come from symmetry and may require symmetry-breaking observables or reformulation
  - [White et al. (2016)](https://doi.org/10.1371/journal.pcbi.1005227): complementary experiments can expose omitted mechanisms and increase model discrepancy
  - [Langdon & Engel (2025)](https://doi.org/10.1038/s41593-025-01869-7): preserving causal interactions among task variables matters; correlation-only reduction can miss behaviorally relevant computation

### 2. `more measurements` と `more informative measurements` は別であり，Roadmap の主導線でも stop rule を持つべきでした

- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は、connectome-constrained recurrent networks の degeneracy が `small targeted recording set` で崩せることを示しました。
- これは `record more` ではなく `record the right subset for the surviving ambiguity` でございます。
- [Gevertz & Kareva (2024)](https://doi.org/10.1038/s41540-023-00325-1) は `minimally sufficient experimental design` を明示し、[Liu et al. (2025)](https://doi.org/10.1016/j.csbj.2025.10.058) は active learning により practical identifiability に達するまでの観測数を減らせることを示しました。
- したがって `R7` で止めるべき誤読は
  - `more data = more identification`
  - `multimodal = automatically informative`
  - `naturalistic = automatically broader regime coverage`
  でございます。

### 3. Roadmap がここで弱いと，verification 側の厳密さを入口で受け止めきれません

- `verification.md` と `wiki/observation-to-estimation.md` は submission rule と explanatory rule としてかなり厳密でした。
- しかし `tech_roadmap.md` は site-wide dependency map であり、ここで ambiguity typing と stop rule が薄いと、
  - 読者は roadmap で generic improvement と読んでから
  - verification page で初めて厳しい disclosure を知る
  という順序になります。
- この順序はよくありません。Roadmap の時点で
  - ambiguity class
  - design objective
  - minimum-sufficiency stop rule
  を visible にしておく方が、サイト全体の読解が安定いたします。

## web で確認した主な一次文献

- [Langdon & Engel (2025)](https://doi.org/10.1038/s41593-025-01869-7)
  - heterogeneous neural responses から latent circuit inference を行い、task-variable interaction を保持した低次元回路表現を提示
- [Gevertz & Kareva (2024)](https://doi.org/10.1038/s41540-023-00325-1)
  - practical identifiability を保ちながら `how much data` と `when to collect it` を最小化する minimally sufficient design を定式化
- [Liu et al. (2025)](https://doi.org/10.1016/j.csbj.2025.10.058)
  - active learning / profile-likelihood based design により、practical identifiability 到達に必要な観測数を削減

## 今回実行した変更

### `tech_roadmap.md`

- `page_highlights` を更新し、`R7` を
  - `observability`
  - `structural identifiability`
  - `practical identifiability`
  - `ambiguity class`
  - `minimum-sufficiency stop rule`
  の 5 要素で読むことを front matter に反映しました。
- `known_points` を更新し、`Richer observability and better fit` の停止条件に
  - `ambiguity class`
  - `experiment-design leverage`
  - `minimum-sufficiency stop rules`
  を追加しました。
- `R7` 本文に `Ambiguity class` table を追加し、少なくとも
  - `symmetry / reparameterization ambiguity`
  - `regime-restricted degeneracy`
  - `model-family / omitted-mechanism ambiguity`
  - `task-variable interaction / representation ambiguity`
  の 4 類型で読むよう固定しました。
- `R7` 本文に `2026-03-31 supplement` を追加し、informative protocol の条件を
  - named ambiguity
  - identifiability objective
  - orthogonal regime / targeted recording leverage
  - model-discrepancy stress
  - minimum-sufficiency stop rule
  の 5 項目で table 化しました。
- 参考文献欄に今回 `R7` で直接使った識別可能性・設計文献を追加しました。

## 今回止めた誤読

- `more measurements = more informative measurements`
- `multimodal = automatically ambiguity-breaking`
- `naturalistic = automatically broad enough regime coverage`
- `more data until performance looks stable = practical identifiability achieved`
- `one good fit after a richer protocol = unique mechanism`

## 検証

- `bundle exec jekyll build` を実行して、サイトがビルドできることを確認します。
- `git diff --stat` と要点 diff で、今回の修正が `tech_roadmap.md` と監査メモに限定されていることを確認します。

## external dependency tasks

- なし
  - 今回の主作業は、web 上の一次文献確認、repo 内の公開本文修正、監査メモ追加、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Massonis G, Villaverde AF. Finding and breaking Lie symmetries: implications for structural identifiability and observability in biological modelling. *Symmetry*. 2020;12(3):469. https://doi.org/10.3390/sym12030469
2. White A, Tolman M, Thames HD, Withers HR, Mason KA, Transtrum MK. The limitations of model-based experimental design and parameter estimation in sloppy systems. *PLOS Computational Biology*. 2016;12(12):e1005227. https://doi.org/10.1371/journal.pcbi.1005227
3. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574. https://doi.org/10.1038/s41593-025-02080-4
4. Langdon C, Engel TA. Latent circuit inference from heterogeneous neural responses during cognitive tasks. *Nature Neuroscience*. 2025;28:665-675. https://doi.org/10.1038/s41593-025-01869-7
5. Gevertz JL, Kareva I. Minimally sufficient experimental design using identifiability analysis. *npj Systems Biology and Applications*. 2024;10:2. https://doi.org/10.1038/s41540-023-00325-1
6. Liu X, Wanika L, Chappell MJ, Branke J. Efficient data collection for establishing practical identifiability via active learning. *Computational and Structural Biotechnology Journal*. 2025;27:4992-5006. https://doi.org/10.1016/j.csbj.2025.10.058
