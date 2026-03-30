# Site Deepening Audit (2026-03-31, uncertainty / source-imaging uncertainty-object split)

## 対象

- 主対象: `wiki/uncertainty-confidence-and-abstention.md`
- 同期対象:
  - `github-wiki-export/uncertainty-confidence-and-abstention.md`
  - `github-wiki-export/verification-basics.md` （export 再生成で既存 source との差分が同期されたため）
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- サイト本体では 2026-03-30 から 2026-03-31 にかけて、
  - inverse family
  - target object
  - uncertainty object
  - validation board
  を分離する site-wide rule がかなり整備されていました。
- しかし `wiki/uncertainty-confidence-and-abstention.md` はなお、
  - `posterior / interval width`
  - `solver comparison`
  - `conductivity sensitivity`
  - `external validator`
  を、読者が実質的に一つの `width` や `confidence` として読める余地を残していました。
- これは技術的に弱いです。source imaging の不確実性は一個ではなく、少なくとも
  - cross-pipeline spread
  - forward-model / conductivity sensitivity
  - focal posterior support
  - sparse debiased interval / hypothesis-test uncertainty
  - extent-aware uncertainty
  に分かれるからです。
- ここが曖昧なままですと、他ページで route card を厳密化していても、不確実性の入口ページで `better width = stronger truth` と再圧縮されます。

## web確認対象

- `https://doi.org/10.1016/j.neuroimage.2017.02.076`
- `https://doi.org/10.3389/fnhum.2024.1335212`
- `https://doi.org/10.3389/fnhum.2024.1359753`
- `https://doi.org/10.1109/TMI.2024.3506596`
- `https://doi.org/10.1109/TMI.2025.3642620`
- `https://doi.org/10.1038/s41597-020-0467-x`
- `https://doi.org/10.1111/epi.18552`

## 根拠付き批判

### 1. 「width を出した」だけでは、何の不確実性かが決まりません

- [Mahjoory et al. (2017)](https://doi.org/10.1016/j.neuroimage.2017.02.076) は、forward model / inverse method / template / toolbox の違いだけで source localization と connectivity がかなり動くことを示しました。
- [Luria et al. (2024)](https://doi.org/10.3389/fnhum.2024.1359753) は focal-source configuration に対する probabilistic posterior support を返します。
- [Tong et al. (2025)](https://doi.org/10.1109/TMI.2024.3506596) は sparse source activity に対する debiased estimator の variance と hypothesis testing を返します。
- [Feng et al. (2025)](https://doi.org/10.1109/TMI.2025.3642620) は extended source の location と extent を対象に empirical-Bayesian uncertainty を返します。

批判:

- これらは同じ `width` ではありません。
- 旧ページは point estimate 批判としては正しかった一方で、読者が `posterior / interval / spread` を一続きの uncertainty ladder と誤読できる構図を残していました。

### 2. solver-internal uncertainty と forward-model uncertainty は別監査です

- [Vorwerk et al. (2024)](https://doi.org/10.3389/fnhum.2024.1335212) は tissue conductivity uncertainty が localization error と source-depth error を強く動かし、特に sulcal wall の quasi-tangential sources で大きいことを示しました。
- [Rimpiläinen et al. (2019)](https://doi.org/10.1016/j.neuroimage.2018.11.058) は unknown skull conductivity を Bayesian に扱うことで upstream physics の不確実性を source localization に持ち込む route を示しました。

批判:

- したがって `posterior-aware solver` があることと `upstream conductivity / geometry uncertainty が十分に監査された` ことは同じではありません。
- 旧ページはこの分離が弱く、solver 内の uncertainty と forward-model 側の uncertainty が近すぎる読み口になっていました。

### 3. external validation も一つの coverage ではありません

- [Mikulan et al. (2020)](https://doi.org/10.1038/s41597-020-0467-x) は simultaneous intracerebral stimulation and HD-EEG による precisely known stimulation-site board です。
- [Hao et al. (2025)](https://doi.org/10.1111/epi.18552) は simultaneous HD-EEG and SEEG in drug-resistant epilepsy で、source depth と spike power に依存する regime-conditioned accuracy を報告しています。

批判:

- これらは同じ validation ではありません。前者は focal stimulation-site board、後者は epilepsy-specific simultaneous-reference board です。
- 旧ページは `external validator` を一欄で処理しており、`which board for which error question` の区別が弱い状態でした。

## 今回実行した変更

### `wiki/uncertainty-confidence-and-abstention.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `description` / `page_intro` / `page_highlights` / `known_points` を更新し、source imaging では uncertainty object を typed に読む必要があることを明示しました。
- 冒頭に `2026-03-31 correction: source-imaging uncertainty is not one generic width` を追加しました。
- Conclusion に `untyped source-imaging widths` を入れ、入口の停止線を強めました。
- `Gate 2: Proofreading` を更新し、`named uncertainty object` を必須 disclosure にしました。
- `Task-specific reporting` の `EEG source imaging` 行を更新し、
  - inverse family / target object
  - uncertainty object
  - forward-model uncertainty route
  - cross-family comparison rule
  - named validation board / operating regime
  - abstention boundary
  を要求するようにしました。
- source-imaging 文献節を全面改稿し、
  - `width without a typed uncertainty object is still too much reading`
  という節へ変更しました。
- その直下に `Uncertainty object` table を追加し、
  - cross-pipeline spread
  - forward-model / conductivity sensitivity
  - posterior support over focal-source configurations
  - debiased interval / test uncertainty for sparse activity
  - extent-aware empirical-Bayesian uncertainty
  を分離しました。
- `External validation is also not one generic coverage claim` note を追加しました。
- site rules の source-imaging bullet を `typed uncertainty objects` ベースに更新しました。
- references に
  - Mahjoory 2017
  - Vorwerk 2024
  - Luria 2024
  - Tong 2025
  - Mikulan 2020
  - Hao 2025
  を追加しました。

### export 同期

- `ruby scripts/export_github_wiki.rb` を実行し、`github-wiki-export/uncertainty-confidence-and-abstention.md` を再生成しました。
- その際、既存 source と export がずれていた `github-wiki-export/verification-basics.md` も同期されました。

## 今回止めた誤読

- `posterior / interval / solver spread` を一つの confidence scale として読む
- `solver-internal uncertainty` と `forward-model uncertainty` を同じ欄で済ませる
- `probabilistic focal support` と `debiased sparse interval` と `extended-source extent uncertainty` を同じ object とみなす
- `external validator がある` を `どの error question でも validation 済み` と読む
- `better width` を `better truth` と読み替える

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功
- `bundle exec jekyll build`
  - 成功
- `ruby scripts/check_github_wiki_export.rb`
  - 未 commit の export drift を検知して停止
  - これは内容破綻ではなく、validator が export 差分の未 commit 状態を検出したもの

## external dependency tasks

- なし
  - 今回の修正は repo 内の公開文面、export 同期、検証、commit、push までこのセッションで完結可能です。

## 参考文献

1. Mahjoory K, Nikulin VV, Botrel L, Linkenkaer-Hansen K, Fato MM, Haufe S. Consistency of EEG source localization and connectivity estimates. *NeuroImage*. 2017;152:590-601. https://doi.org/10.1016/j.neuroimage.2017.02.076
2. Vorwerk J, Wolters CH, Baumgarten D. Global sensitivity of EEG source analysis to tissue conductivity uncertainties. *Front Hum Neurosci*. 2024;18:1335212. https://doi.org/10.3389/fnhum.2024.1335212
3. Rimpiläinen I, Solis-Lemus JA, Särkkä S. Improved EEG source localization with Bayesian uncertainty modelling of unknown skull conductivity. *NeuroImage*. 2019;184:52-60. https://doi.org/10.1016/j.neuroimage.2018.11.058
4. Luria G, Viani A, Pascarella A, Bornfleth H, Sommariva S, Sorrentino A. The SESAMEEG package: a probabilistic tool for source localization and uncertainty quantification in M/EEG. *Front Hum Neurosci*. 2024;18:1359753. https://doi.org/10.3389/fnhum.2024.1359753
5. Tong PF, Yang H, Ding X, Ding Y, Geng X, An S, Wang G, Chen SX. Debiased Estimation and Inference for Spatial-Temporal EEG/MEG Source Imaging. *IEEE Trans Med Imaging*. 2025;44(3):1480-1493. https://doi.org/10.1109/TMI.2024.3506596
6. Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. *IEEE Trans Med Imaging*. 2025. https://doi.org/10.1109/TMI.2025.3642620
7. Mikulan E, Russo S, Parmigiani S, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Sci Data*. 2020;7:127. https://doi.org/10.1038/s41597-020-0467-x
8. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464. https://doi.org/10.1111/epi.18552
