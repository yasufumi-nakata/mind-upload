# 2026-03-31 site deepening audit: frontdoor inverse-family sync

## 対象として選んだ箇所

- `index.md`
- `tech_roadmap.md`

今回ここを優先した理由は、`wiki/observation-to-estimation.md` と `verification.md` では inverse-family の停止条件がかなり明確になっている一方、入口ページと Roadmap 本体ではまだ `new inverse method = one stronger truth meter` と読める余地が残っていたためです。公開サイトの core policy が深部ページにだけある状態は、読者の最初の誤読を止めきれません。

## 根拠付き批判

### 1. 現状の入口ページは `solver sensitivity` までは言えていましたが、`inverse family ごとに推定対象そのものが違う` ことがまだ十分に前面化されていませんでした

- [Luria et al. (2024)](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1359753/full) は、SESAMEEG を focal-source hypothesis に対する posterior-support route として提示しています。
- [Tong et al. (2025)](https://www.songxichen.com/Uploads/Files/Publication/Debiased_Estimation_and_Inference_for_SpatialTemporal_EEG_MEG_Source_Imaging.pdf) は、sparse spatial-temporal source imaging に対して debiased estimation / inference を与えます。
- [Feng et al. (2025)](https://pubmed.ncbi.nlm.nih.gov/41370172/) は、extended-source extent を返す Block-Champagne を提示しています。
- したがって `better inverse method` を 1 本の進歩バーとして front door で読ませるのは不正確です。family が違う時点で target object と uncertainty object が違います。

### 2. forward-model uncertainty は inverse family の進歩と独立に残ります

- [Vorwerk et al. (2024)](https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1335212/full) は、EEG source analysis が skull / skin conductivity uncertainty に強く依存し、特に quasi-tangential sources で localization が大きく動くことを示しています。
- [Vorwerk et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/41411682/) は、skull conductivity estimation が source-analysis uncertainty を大きく下げうる一方で、brain base などでは効果が限定的であることを示しています。
- よって、posterior-aware あるいは debiased family が出たことだけで upstream physics が解決したと読ませるのは誤りです。

### 3. validation は `solver name` ではなく `board / operating regime` に紐づきます

- [Pascarella et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120219) は focal-source の in-vivo validation route です。
- [Unnwongse et al. (2023)](https://pubmed.ncbi.nlm.nih.gov/36824389/) は simultaneous intracranial stimulation / scalp EEG を使った focal clinical board です。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は simultaneous HD-EEG / SEEG concordance を見る drug-resistant-epilepsy operating regime です。
- これらは同じ board ではありません。ゆえに `validated ESI` を generic label として front door に残すと、validation transfer が過大になります。

### 4. この弱点は front door と roadmap 本体で直すべきでした

- 詳細版の wiki / verification にだけ厳密な停止条件があると、サイト全体としては「奥へ行くほど厳密」ではあっても「入口で誤読を防ぐ」構造になりません。
- このサイトの目的は verification commons であり、入口で誤読を止めること自体が core function です。
- したがって今回は、さらに深い technical page を増やすのではなく、既に成立している inverse-family policy を入口ページと Roadmap 本体に同期させる方が合理的でした。

## 今回実行した変更

### `index.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `page_highlights` / `known_points` に、ESI の進歩を one shared inverse-progress score と読まない旨を追加しました。
- `If A Better ESI Solver Sounds Like One Shared Progress Bar` という note-box を追加し、
  - focal posterior-support family
  - sparse debiased family
  - extended-source family
  - forward-model uncertainty
  - validation board / operating regime
  を front door で明示するようにしました。

### `tech_roadmap.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `page_highlights` / `known_points` に inverse-family split を追加しました。
- `R1` に 2026-03-31 addendum を追加し、minimum audit item を
  - `source regime / target object`
  - `uncertainty object`
  - `forward-model uncertainty route`
  - `validation board / operating regime`
  の 4 項目で固定しました。
- `R2` に 2026-03-31 addendum を追加し、representation family を
  - probabilistic focal-source family
  - sparse spatial-temporal family
  - extended-source family
  に分けて、各 family が何を返し、何を自動では正当化しないかを table で固定しました。

## 今回止めた誤読

- `new inverse solver = one stronger truth meter`
- `posterior-aware / debiased / extent-aware` は同じ target object を返している
- `better uncertainty map = forward-model uncertainty もほぼ解決`
- `validated in one regime = validated for all source classes`
- `front door では簡略化してよいので inverse-family difference は deep page にだけ置けばよい`

## 検証

- `bundle exec jekyll build` を実行してビルド通過を確認する
- `git diff --stat` と要点 diff で反映箇所を確認する

## external dependency tasks

- 今回の主作業に関して、外部依存で止めた項目はありません。

## 参考文献

1. Luria G, Viani S, Pascarella A, et al. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Frontiers in Human Neuroscience*. 2024. https://doi.org/10.3389/fnhum.2024.1359753
2. Tong PF, Yang H, Ding X, et al. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Transactions on Medical Imaging*. 2025. https://doi.org/10.1109/TMI.2024.3506596
3. Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. *IEEE Transactions on Medical Imaging*. 2025. https://doi.org/10.1109/TMI.2025.3642620
4. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Frontiers in Human Neuroscience*. 2024. https://doi.org/10.3389/fnhum.2024.1335212
5. Vorwerk J, Rampp S, Wolters CH, Baumgarten D. Potential of EEG and EEG/MEG skull conductivity estimation to improve source analysis in presurgical evaluation of epilepsy. *Journal of Neural Engineering*. 2026. https://doi.org/10.1088/1741-2552/ae2f01
6. Pascarella A, Rucco R, Bertino E, et al. An in-vivo validation of ESI methods with focal sources. *NeuroImage*. 2023. https://doi.org/10.1016/j.neuroimage.2023.120219
7. Unnwongse K, Rampp S, Wehner T, et al. Validating EEG source imaging using intracranial electrical stimulation. *Brain Communications*. 2023. https://doi.org/10.1093/braincomms/fcad023
8. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025. https://doi.org/10.1111/epi.18552
