# Site Deepening Audit (2026-03-28, measurement/modeling beginner route minimum-sufficiency sync)

## 対象

- 主対象: `wiki/measurement-and-modeling-terms.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1049/iet-syb.2010.0061`
- `https://doi.org/10.1016/j.mbs.2016.10.009`
- `https://doi.org/10.1371/journal.pcbi.1005227`
- `https://doi.org/10.1038/s41540-023-00325-1`
- `https://doi.org/10.1038/s41593-025-02080-4`
- `https://doi.org/10.1038/s41593-025-01869-7`
- `https://doi.org/10.1016/j.csbj.2025.10.058`

## 今回この箇所を選んだ理由

- `wiki/measurement-and-modeling-terms.md` は、初学者が `observation -> organization -> estimation -> verification` を最初に学ぶ technical front door です。
- しかし 2026-03-28 時点では、詳細ページで既に導入済みの
  - `identifiability objective`
  - `omitted-mechanism stress`
  - `minimum-sufficiency stop rule`
  がこの入口ページには入っておらず、読者がなお
  - 曖昧性が残ったら追加データを増やせばよい
  - 検証は fit 後の reporting layer であり、次の測定条件の選び方までは含まない
  と読める余地が残っていました。
- これは技術・自然科学の観点で弱点です。なぜなら、WBE 周辺の modeling 議論で本当に難しいのは「データが少ないこと」そのものではなく、「残った曖昧性をどの条件で崩すか」を設計できているかだからでございます。

## 根拠付き批判

### 1. non-identifiability は generic な `more data` ではなく、条件付き設計か model reduction で解く問題です

- [Raue et al. (2011)](https://doi.org/10.1049/iet-syb.2010.0061) は、structural / practical non-identifiability を検出した後は、`suitable conditions` での追加測定か、データの情報量に合わせた model reduction によって解くべきだと整理しました。

批判:

- beginner route が `estimate -> verify` の順だけを教えると、何を追加すべきかが generic な data collection に見えます。
- しかし一次文献の水準では、次に要るのは `more samples` ではなく `which condition changes the information content` でございます。

### 2. sloppiness は identifiability の代用指標ではありません

- [Chis et al. (2016)](https://doi.org/10.1016/j.mbs.2016.10.009) は、sloppiness は structural / practical identifiability と同値ではなく、optimal design でも identifiability criteria を直接最適化する方が informative だと示しました。

批判:

- よって、入口ページが `uncertainty が減る方向に設計する` 程度で止まるのは弱いです。
- この段階で `何の identifiability criterion を改善する設計か` を書かないと、site-wide rule が入口で再び曖昧になります。

### 3. complementary experiment は強化だけでなく omitted mechanism の露出にもなります

- [White et al. (2016)](https://doi.org/10.1371/journal.pcbi.1005227) は、complementary experiment を足すことで model discrepancy が大きくなり、推定精度が上がっても予測力がむしろ下がりうることを示しました。

批判:

- したがって `追加条件を入れた = より informative になった` とは限りません。
- beginner route に `new condition may expose omitted-mechanism error` を書かないと、stronger design を単調増加の bar と誤読させます。

### 4. 実際には `minimum-sufficient schedule` と停止条件が設計対象です

- [Gevertz & Kareva (2024)](https://doi.org/10.1038/s41540-023-00325-1) は、practical identifiability を保ちながら時間点数とコストを最小化する `minimally sufficient experimental design` を定式化しました。
- [Liu et al. (2025)](https://doi.org/10.1016/j.csbj.2025.10.058) は、active learning により practical identifiability を達成するのに必要な観測数を大きく減らせることを示しました。

批判:

- 入口ページが `verification = benchmark / baseline / preregistration / model card` に留まると、停止条件の設計が visibility を失います。
- 現在の一次文献では、`what is enough to stop` も設計変数であり、afterthought ではありません。

### 5. neuroscience でも重要なのは modality count ではなく ambiguity-breaking design です

- [Beiran & Litwin-Kumar (2025)](https://doi.org/10.1038/s41593-025-02080-4) は、connectome-constrained network でも dynamics の縮退が残る一方、small targeted recording set でそれを崩せることを示しました。
- [Langdon & Engel (2025)](https://doi.org/10.1038/s41593-025-01869-7) は、task-variable 間の causal interaction を latent circuit として保持すると、correlation-only reduction では取り逃がす behaviorally relevant computation を取り戻せることを示しました。

批判:

- したがって、beginner route でまだ `more sensors / more data / more modality` の語感が強いのは不十分です。
- neuroscience の一次文献も、`which neurons / which interaction / which perturbation` を選ぶ設計の方が決定的であることを支持しています。

## 今回実行した変更

- `wiki/measurement-and-modeling-terms.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `page_highlights` / `known_points` に、
    - identifiability objective
    - omitted-mechanism stress
    - minimum-sufficiency stop rule
    を beginner route の必須読解対象として追加しました。
  - 新しい note-box `2026-03-28 correction to the beginner route` を追加し、
    - Raue 2011
    - Chis 2016
    - White 2016
    - Gevertz & Kareva 2024
    - Beiran & Litwin-Kumar 2025
    - Langdon & Engel 2025
    - Liu et al. 2025
    を使って、`more data` ではなく `ambiguity-breaking design` を beginner rule に同期しました。
  - verification table に `Experiment-design leverage` row を追加しました。
  - verification section に補足 note を追加し、verification が reporting だけでなく `why this next condition` を説明する層であることを明文化しました。
  - 参考文献を追加しました。

## 今回止めた誤読

- `曖昧性が残る = とりあえず追加データを増やす`
- `uncertainty が少し減った = identifiability が改善した`
- `complementary experiment = つねにより良い設計`
- `verification = fit 後に benchmark を並べるだけ`
- `neuroscience では modality を増やせば candidate set が自然に閉じる`

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査記録、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Raue A, Kreutz C, Maiwald T, Klingmüller U, Timmer J. Addressing parameter identifiability by model-based experimentation. *IET Systems Biology*. 2011;5(2):120-130.
   - https://doi.org/10.1049/iet-syb.2010.0061
2. Chis OT, Villaverde AF, Banga JR, Balsa-Canto E. On the relationship between sloppiness and identifiability. *Mathematical Biosciences*. 2016;282:147-161.
   - https://doi.org/10.1016/j.mbs.2016.10.009
3. White A, Tolman M, Thames HD, Withers HR, Mason KA, Transtrum MK. The Limitations of Model-Based Experimental Design and Parameter Estimation in Sloppy Systems. *PLoS Computational Biology*. 2016;12(12):e1005227.
   - https://doi.org/10.1371/journal.pcbi.1005227
4. Gevertz JL, Kareva I. Minimally sufficient experimental design using identifiability analysis. *npj Systems Biology and Applications*. 2024;10(1):2.
   - https://doi.org/10.1038/s41540-023-00325-1
5. Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nature Neuroscience*. 2025;28:2561-2574.
   - https://doi.org/10.1038/s41593-025-02080-4
6. Langdon C, Engel TA. Latent circuit inference from heterogeneous neural responses during cognitive tasks. *Nature Neuroscience*. 2025;28:665-675.
   - https://doi.org/10.1038/s41593-025-01869-7
7. Liu X, Wanika L, Chappell MJ, Branke J. Efficient data collection for establishing practical identifiability via active learning. *Computational and Structural Biotechnology Journal*. 2025;27:4992-5006.
   - https://doi.org/10.1016/j.csbj.2025.10.058
