# Site Deepening Audit (2026-03-31, paper archive inverse-family front door)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
- 調査範囲:
  - 技術 / 自然科学のみ
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- `verification.md`、`tech_roadmap.md`、`index.md`、`wiki/observation-to-estimation.md`、`datasets.md` では、2026-03-31 時点で `inverse family` ごとの差をかなり厳密に止められておりました。
- しかし文献入口である `mind_uploading_papers.md` では、なお
  - `validated ESI`
  - `better source imaging`
  - `direct validation`
  が比較的ひとまとまりの前進として読める余地が残っておりました。
- このズレは技術・自然科学の観点で重要でございます。文献入口で粗い分類が残ると、コア規範ページで止めている
  - `inverse family ごとに target object が違う`
  - `forward-model uncertainty は別監査`
  - `validation board は source regime ごとに違う`
  という規律が、年順アーカイブの読み方で再び崩れるからでございます。

## 根拠付き批判

### 1. 現状の文献入口は `direct validation` を強く見せる一方で、inverse-family ごとの object difference を前景化できておりませんでした

- [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753) は、M/EEG source localization において Bayesian posterior support と uncertainty quantification を返す focal-source family を提示しております。
- [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596) は、sparse spatial-temporal EEG/MEG source imaging に対して debiased estimation と inference を提示しております。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は、extended-source extent を主要対象とする Bayesian framework を提示しております。

批判:

- これらは同じ `better ESI` ではございません。
- 返している object は少なくとも
  - focal posterior support
  - sparse debiased inference
  - extended-source uncertainty / extent reconstruction
  に分かれております。
- したがって文献入口で `source imaging with direct validation` を主ラベルにし続けると、reader が family difference を単なる implementation variance に読み落とします。

### 2. forward-model / conductivity sensitivity は inverse-family progress と別の route です

- [Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212) は、tissue conductivity uncertainty が EEG inverse solution を動かし、とくに quasi-tangential source で reconstructed depth と localization が変わることを示しております。
- これは `posterior-aware` や `debiased` な inverse family が存在することと、upstream physics の不確実性が十分監査されたことが別問題であることを意味します。

批判:

- 文献入口でこの軸を独立させないと、
  - `uncertainty-aware solver`
  - `physics-aware source analysis`
  が同じ進歩線のように見えてしまいます。
- その結果、見栄えの良い posterior map が未監査の head-model burden まで代表しているかのような過読が残ります。

### 3. validation board は source regime ごとに違い、万能 board はまだありません

- [Mikulan et al. (2020)](https://doi.org/10.1038/s41597-020-0467-x) は、known stimulation locations を使う ground-truth board を提供しております。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は、simultaneous HD-EEG / SEEG により ictal / interictal localization accuracy を比較しつつ、source depth と spike power 依存性を明示しております。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) も abstract 上で simulation と deep brain stimulation EEG / epilepsy data による validation を提示しておりますが、これは extended-source reconstruction を主対象とする board です。

批判:

- したがって
  - focal stimulation board
  - simultaneous SEEG clinical board
  - extended-source simulation / DBS board
  は同じ benchmark ではございません。
- `validated` という一語でまとめると、どの source regime に対して強いのかが消えます。

### 4. この修正は文献入口そのものに必要でした

- `research_harvest_50.md` の U1 はすでに三分割で書かれております。
- しかし `mind_uploading_papers.md` は、年順アーカイブとして読者が最初に「今どこが進んだのか」を掴む場所でございます。
- ここがなお粗いと、厳密な route-card rule が site-wide default になりません。

## 今回実行した変更

### `mind_uploading_papers.md`

- `last_updated` を `2026-03-31` に更新しました。
- `note` に inverse-family split 更新を追記しました。
- front matter の `known_points` / `page_highlights` に、source-imaging route が
  - focal posterior support
  - sparse debiased inference
  - extended-source uncertainty
  - forward-model / conductivity sensitivity
  - named validation boards
  へ分かれることを追加しました。
- 技術導入段落の source-imaging 説明を、`direct validation` 中心ではなく
  - field formation
  - inverse-family target object
  - forward-model sensitivity
  - named validation boards
  の split が見える文面へ修正しました。
- technical evidence-class table の `Direct source-validation anchors` 行を
  - `Source-imaging route split: family / physics / validation board`
  に差し替えました。
- 新規 note box
  - `Read inverse-family source-imaging papers as different objects, not one better ESI line`
  を追加しました。
- paper-reading rule の長文段落に、
  - `Luria / Tong / Feng = inverse-family object split`
  - `Vorwerk = forward-model / conductivity route`
  - `Mikulan / Hao = named validation boards`
  を埋め込みました。
- priority-route table の source-imaging 行を、
  - `source regime / target object`
  - `uncertainty object`
  - `forward-model / conductivity route`
  - `named validation board`
  を読む導線へ更新しました。

## 今回止めた誤読

- `validated ESI` = one generic truth upgrade
- `posterior-aware solver` = physics burden もだいたい解決
- `debiased sparse inference` = extended-source reconstruction にも同じ強さで効く
- `clinical simultaneous SEEG board` = focal / sparse / extended / spontaneous regime の万能 benchmark
- `source-imaging progress` = one common inferential object

## 検証

- 実行予定:
  - `git diff --check`
  - `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - `git diff --stat`

## external dependency tasks

- なし
  - 今回の作業は、web 上の一次文献確認、公開ページ改稿、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024.
   - https://doi.org/10.3389/fnhum.2024.1359753
2. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2024.3506596
3. Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. *IEEE Transactions on Medical Imaging*. 2025.
   - https://doi.org/10.1109/TMI.2025.3642620
4. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024.
   - https://doi.org/10.3389/fnhum.2024.1335212
5. Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Scientific Data*. 2020.
   - https://doi.org/10.1038/s41597-020-0467-x
6. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025.
   - https://doi.org/10.1111/epi.18552
