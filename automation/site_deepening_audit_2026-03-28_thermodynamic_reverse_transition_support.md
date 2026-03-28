# Site Deepening Audit (2026-03-28, thermodynamic reverse-transition support / null-control split)

## 対象

- 主対象: `wiki/thermodynamic-grounding-basics.md`
- 同期対象:
  - `github-wiki-export/thermodynamic-grounding-basics.md`
  - `verification.md`
  - `faq.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1073/pnas.2109889118`
- `https://doi.org/10.1038/s41467-025-66669-w`
- `https://doi.org/10.1038/s42005-024-01742-2`
- `https://doi.org/10.1073/pnas.2318333121`

## 今回この箇所を選んだ理由

- 公開サイトはすでに thermodynamic / irreversibility claim を `estimator family`、`coarse-graining`、`closure audit` でかなり厳密に止められておりました。
- しかしなお一つ、実務上重要な混線が残っておりました。現行文面では `null / surrogate control` と `finite-data handling` が同じ欄に入りやすく、読者が
  - surrogate が通った
  - だから entropy production は十分推定できた
  と読める余地が残っておりました。
- これは一次文献の整理として弱いです。artifact rejection と estimator support coverage は別問題だからでございます。

## 根拠付き批判

### 1. clean surrogate は nuisance rejection を示しても、support coverage を保証しません

- [Lynn et al. (2021)](https://doi.org/10.1073/pnas.2109889118) は coarse-grained BOLD transition から entropy-production lower bound を推定し、finite-data 由来の confidence interval を明示しました。
- [Ishihara & Shimazaki (2025)](https://doi.org/10.1038/s41467-025-66669-w) は trial-shuffled data を使って coupling-related entropy flow を firing-rate dynamics と sampling error から切り分けました。

批判:

- これは `surrogate が通ったか` と `estimate が十分 supported か` が別の監査軸であることを示します。
- したがって route card の現行欄が両者を一体化しているのは、読解規則としてまだ甘い状態でした。

### 2. reverse transition が見えていないと、direct estimate 自体が崩れえます

- [Baiesi et al. (2024)](https://doi.org/10.1038/s42005-024-01742-2) は、lacking-data regime では backward transition が十分に観測されないため、direct entropy-production estimate が破綻しうることを示しました。
- 同論文は、その条件では lower-bound strategy の方が安定な場合があることも示しています。

批判:

- したがって `rare-transition treatment` は単なる implementation detail ではございません。
- これは estimator choice と claim ceiling を変える independent stop line であり、null control の後ろに埋めるべきではありませんでした。

### 3. partial observation と coarse lumping は finite-data problem をさらに悪化させます

- [Blom et al. (2024)](https://doi.org/10.1073/pnas.2318333121) は、coarse resolution で観測した trajectory を naive に Markov と読むと dissipation estimate が大きく過小評価されうることを示しました。

批判:

- したがって `support coverage` は単に sample size の話ではなく、
  - observed transition support
  - memory order misspecification
  - coarse-lumping artifact
  の交点で評価すべきです。
- 現行ページがこれを `null / surrogate` と同じ欄に置くのは、site-wide の verification grammar として不十分でした。

## 今回実行した変更

- `wiki/thermodynamic-grounding-basics.md`
  - `last_updated` を `2026-03-28` に更新しました。
  - front matter の `page_highlights` / `known_points` に、`null / surrogate control` と `reverse-transition support` は別監査である旨を追加しました。
  - `Main weakness` 節に fourth weakness を追加し、
    - Lynn 2021 の finite-data confidence interval
    - Ishihara & Shimazaki 2025 の trial-shuffled control
    - Baiesi 2024 の lacking-data regime
    を使って、support coverage を独立 stop line として明文化しました。
  - `Irreversibility route card` の表で、
    - `Null / surrogate control`
    - `Reverse-transition support / finite-data support`
    を別 field に分離しました。
  - `What would actually strengthen the claim` の finite-data row を support-coverage 중심に更新しました。
  - `Operation rules` に `null controls` と `reverse-transition support` を分ける規則を追加しました。
  - `6 questions` を `7 questions` に更新し、`Were the relevant reverse transitions actually supported by the data?` を追加しました。

- `verification.md`
  - `Irreversibility / Thermodynamic Route Card` の概要要件に
    - coarse-graining / closure assumptions
    - reverse-transition support / finite-data handling
    を追加しました。
  - thermodynamic section の addendum を `2026-03-28` に更新し、Baiesi 2024 を加えて
    - surrogate success
    - reverse-transition support
    が別問題であることを明文化しました。
  - minimum reporting rule を
    - `Nulls and surrogate controls`
    - `Reverse-transition support and finite-data handling`
    に分離しました。

- `faq.md`
  - `Q1f` を更新し、Baiesi 2024 と Ishihara & Shimazaki 2025 を使って
    - clean surrogate
    - sparse reverse-transition regime
    を別監査として説明しました。

## 今回止めた誤読

- `shuffle / surrogate を通過 = entropy production は十分に推定できた`
- `reverse transition がほぼ見えていない estimate` でも、clean null があれば強く読める
- `finite-data handling` は estimator 実装の細部にすぎない
- `thermodynamic result` の fragile point は coarse-graining だけで、support coverage は別に要らない

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、wiki export、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. *PNAS*. 2021;118(47):e2109889118.
   - https://doi.org/10.1073/pnas.2109889118
2. Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. *Nature Communications*. 2025;16:10852.
   - https://doi.org/10.1038/s41467-025-66669-w
3. Baiesi M, Nishiyama T, Falasco G. Effective estimation of entropy production with lacking data. *Communications Physics*. 2024;7:264.
   - https://doi.org/10.1038/s42005-024-01742-2
4. Blom K, Song K, Vouga E, Godec A, Makarov DE. Milestoning estimators of dissipation in systems observed at a coarse resolution. *PNAS*. 2024;121(23):e2318333121.
   - https://doi.org/10.1073/pnas.2318333121
