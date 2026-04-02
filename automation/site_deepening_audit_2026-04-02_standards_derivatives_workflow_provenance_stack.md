# Site Deepening Audit (2026-04-02, standards / derivatives / workflow-provenance stack)

## 対象

- 主対象:
  - `wiki/standards-repositories-validators-and-benchmarks.md`
- 同期対象:
  - `datasets.md`
  - `wiki/l0-minimum-artifact-pack.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## 今回この箇所を選んだ理由

- 2026-04-02 時点で、このサイトはすでに
  - benchmark provenance / governance
  - derivative lineage
  - event fidelity
  - benchmark object
  をかなり厳密に分けておりました。
- しかし `wiki/standards-repositories-validators-and-benchmarks.md` だけは、なお
  - `raw-data standard`
  - `processed derivative specification`
  - `workflow / model recipe`
  - `execution / result provenance`
  を十分に別層として固定しておらず、読者が
  - `BIDS + OpenNeuro + benchmark`
  で reproducibility stack がほぼ閉じたかのように読める余地が残っておりました。
- これは practical page 群にも波及いたします。`datasets.md` と `wiki/l0-minimum-artifact-pack.md` は実務入口ですので、ここで `dataset name + pipeline name` が粗く読めると、L0 artifact の意味づけが弱くなります。

## 主要結論

- `BIDS raw layout` は `processed-output lineage` ではございません。
- `processed-output lineage` は `workflow / model recipe` ではございません。
- `workflow / model recipe` は `benchmark harness` でもございません。
- `containerized execution` は重要ですが、それだけで `benchmark meaning` や `result provenance` は閉じません。
- よって standards page では少なくとも
  - raw standard
  - repository snapshot
  - derivative specification / lineage
  - workflow / model recipe
  - execution / result provenance
  - benchmark harness
  - benchmark provenance / governance
  を別 object として読ませる必要がございました。

## 根拠付き批判

### 1. OpenNeuro + BIDS は raw input sharing と version fixing を支えますが、processing recipe までは自動で固定いたしません

- 根拠:
  - [Gorgolewski et al. (2016)](https://doi.org/10.1038/sdata.2016.44)
  - [Markiewicz et al. (2021)](https://doi.org/10.7554/eLife.71774)
- 批判:
  - OpenNeuro は BIDS validation と snapshot/versioning に強い infrastructure ですが、それは `which raw input version was shared` を強める層であり、`which processed branch / config / result bundle produced the figure` までを自動で閉じるわけではございません。
  - したがって `OpenNeuro + BIDS` を `full reproducibility` と読むのは過剰でございます。

### 2. BIDS specification 自体が、raw と derivatives を別 dataset layer として扱っております

- 根拠:
  - [BIDS Specification: dataset description](https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html)
  - [BIDS Derivatives: common data types and metadata](https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html)
- 批判:
  - stable specification は derived dataset に `GeneratedBy` を必須化し、`SourceDatasets` を明示し、さらに derivative file ごとの `Sources` lineage を定義しております。
  - これは仕様レベルで `raw BIDS` と `processed derivatives` が別 object だと述べているに等しいです。
  - よって standards page に derivative layer が見えないのは、仕様の読み方として弱いです。

### 3. Workflow portability と workflow provenance も別でございます

- 根拠:
  - [Gorgolewski et al. (2017)](https://doi.org/10.1371/journal.pcbi.1005209)
  - [Zhao et al. (2024)](https://doi.org/10.1162/imag_a_00074)
  - [MNE-BIDS-Pipeline Docs](https://mne.tools/mne-bids-pipeline/stable/)
- 批判:
  - BIDS Apps は containerized deployment と standardized CLI を強めましたが、Zhao et al. (2024) が明示するように、BIDS Apps だけでは full audit trail は自動では残りません。
  - MNE-BIDS-Pipeline も `configuration via a simple text file`、cached steps、summary reports を明示しており、同じ raw 入力でも config 差分が output を動かしうる構造です。
  - したがって `pipeline name` と `workflow recipe / run provenance` を同一視するのは不正確でございます。

### 4. Model recipe も benchmark とは別 object でございます

- 根拠:
  - [BIDS Stats Models Specification](https://bids-standard.github.io/stats-models/index.html)
  - [Representing multi-stage neuroimaging models](https://bids-standard.github.io/stats-models/walkthrough-1.html)
- 批判:
  - BIDS Stats Models は statistical model を machine-readable JSON として定義し、その目的を `recipe` と明示しております。
  - しかも analysis graph, node, edge, groupby, contrast を別に持ちます。
  - これは `benchmark harness` や `runtime container` では代替できない情報であり、site の terminology 上も separate layer として見せる方が正確でございます。

### 5. Result provenance 自体も標準化対象であり、score table の後ろに隠してよい補助情報ではございません

- 根拠:
  - [Maumet et al. (2016)](https://doi.org/10.1038/sdata.2016.102)
- 批判:
  - NIDM-Results は machine-readable description of statistical results と key image data plus provenance を package 化します。
  - つまり result provenance は単なる supplementary note ではなく、independent standardized object です。
  - したがって site の standards page でも `execution / result provenance` を benchmark から切り離す必要がございました。

## 今回実行した変更

### `wiki/standards-repositories-validators-and-benchmarks.md`

- front matter の `description` / `subtitle` / `audience` / `page_highlights` / `known_points` / `unknown_points` を更新しました。
- 新しい note-box `2026-04-02 correction: BIDS plus a benchmark name still do not fix derivatives, workflow recipe, or result provenance` を追加しました。
- `First, separate terms` table を拡張し、
  - derivative specification / lineage
  - loader / converter
  - workflow / model recipe
  - execution / result provenance
  を独立 row として追加しました。
- `In practice ... layers` を `11 layers` に拡張し、
  - raw standard
  - repository snapshot
  - derivative lineage
  - workflow / model recipe
  - execution / result provenance
  - benchmark harness
  - benchmark governance
  の分離を site rule に固定しました。
- `2026-03 site rule` note を更新し、
  - BIDS
  - BIDS Derivatives
  - MNE-BIDS
  - MNE-BIDS-Pipeline / BIDS Apps
  - BIDS Stats Models
  - NIDM-Results
  - MOABB
  の役割差を明示しました。
- EEG example, missing-piece table, common-confusion table, minimum IDs, reading questions, reference listを更新し、実務入口でもこの layering が見えるようにしました。

### `datasets.md`

- front matter の `page_highlights` / `known_points` に、`BIDS raw layout`、`BIDS derivatives / lineage`、`workflow recipe`、`benchmark harness`、`benchmark governance`、`runtime pin` が別層であることを追加しました。
- note-box `BIDS, OpenNeuro and Benchmark are not the same` を `BIDS, Derivatives, Pipeline, OpenNeuro, and Benchmark are not the same` に更新し、MNE-BIDS / MNE-BIDS-Pipeline の役割差も前面化しました。

### `wiki/l0-minimum-artifact-pack.md`

- front matter の `description` / `page_highlights` / `known_points` を更新し、derivative lineage と workflow provenance の分離を明示しました。
- 新しい note-box `2026-04-02 addendum: derivative lineage is not yet workflow provenance` を追加しました。
- item 13 を `Derivative lineage + workflow provenance + replay steps` に更新し、
  - `GeneratedBy`
  - `SourceDatasets`
  - config / model recipe
  - container or lockfile
  を minimum pack に含める形へ tightening しました。

## 今回止めた誤読

- `BIDS dataset exists` = `processed outputs are already traceable`
- `pipeline name is written` = `workflow recipe is frozen`
- `containerized run exists` = `benchmark meaning is fixed`
- `benchmark harness is known` = `result provenance is sufficient`
- `derivative lineage` = `workflow provenance`

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功しました。
- `ruby scripts/build_summary_booklet.rb`
  - 成功しました。
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功しました。
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - 成功しました。
- `git diff --check`
  - 成功しました。
- `rg -n "workflow recipe|execution / result provenance|Derivative lineage \\+ workflow provenance|BIDS, Derivatives, Pipeline, OpenNeuro, and Benchmark" _site/datasets.html _site/wiki/standards-repositories-validators-and-benchmarks.html _site/wiki/l0-minimum-artifact-pack.html github-wiki-export/standards-repositories-validators-and-benchmarks.md github-wiki-export/l0-minimum-artifact-pack.md`
  - 主要 stop line が公開 HTML と GitHub Wiki export に反映されていることを確認しました。

## 外部依存タスク

- なし
  - 今回の作業は、一次文献 / 公式仕様確認、repo 内改稿、derived artifact 再生成、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Gorgolewski KJ, Auer T, Calhoun VD, et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. *Scientific Data*. 2016.
   - https://doi.org/10.1038/sdata.2016.44
2. Markiewicz CJ, Gorgolewski KJ, Feingold F, et al. The OpenNeuro resource for sharing of neuroscience data. *eLife*. 2021.
   - https://doi.org/10.7554/eLife.71774
3. BIDS Specification: dataset description.
   - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html
4. BIDS Derivatives: common data types and metadata.
   - https://bids-specification.readthedocs.io/en/stable/derivatives/common-data-types.html
5. Appelhoff S, Sanderson M, Brooks TL, et al. MNE-BIDS: Organizing electrophysiological data into the BIDS format and facilitating their analysis. *Journal of Open Source Software*. 2019.
   - https://doi.org/10.21105/joss.01896
6. MNE-BIDS-Pipeline documentation.
   - https://mne.tools/mne-bids-pipeline/stable/
7. Gorgolewski KJ, Alfaro-Almagro F, Auer T, et al. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. *PLOS Computational Biology*. 2017.
   - https://doi.org/10.1371/journal.pcbi.1005209
8. Zhao C, Jarecka D, Covitz S, et al. A reproducible and generalizable software workflow for analysis of large-scale neuroimaging data collections using BIDS Apps. *Imaging Neuroscience*. 2024.
   - https://doi.org/10.1162/imag_a_00074
9. BIDS Stats Models Specification.
   - https://bids-standard.github.io/stats-models/index.html
10. BIDS Stats Models walkthrough: representing multi-stage neuroimaging models.
   - https://bids-standard.github.io/stats-models/walkthrough-1.html
11. Maumet C, Auer T, Bowring A, et al. Sharing brain mapping statistical results with the neuroimaging data model. *Scientific Data*. 2016.
    - https://doi.org/10.1038/sdata.2016.102
