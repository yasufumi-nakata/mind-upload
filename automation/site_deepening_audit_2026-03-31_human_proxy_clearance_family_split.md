# Site Deepening Audit (2026-03-31, human proxy clearance family-internal split)

## 対象

- 主対象:
  - `wiki/human-proxy-composition.md`
- 同期対象:
  - `verification.md`
  - `github-wiki-export/human-proxy-composition.md`
- 調査範囲:
  - 技術
  - 自然科学

## web確認対象

- `https://doi.org/10.1126/science.aax5440`
- `https://doi.org/10.1016/j.neuroimage.2025.121142`
- `https://doi.org/10.1038/s41467-023-37685-5`
- `https://doi.org/10.1038/s41593-025-02073-3`
- `https://doi.org/10.1038/s41467-025-66548-4`
- `https://doi.org/10.1038/s41467-025-58726-1`
- `https://doi.org/10.1038/s41467-026-68374-8`

## 今回この箇所を選んだ理由

- front door 側の `index.md` と `wbe_101.md`、および route-card 側の `wiki/homeostatic-plasticity-and-maintenance-state.md` では、clearance / immune support をすでに family 内部で分解しておりました。
- しかし central bundle rule である `wiki/human-proxy-composition.md` では、なお clearance family が実質的に
  - `CSF mobility`
  - `model-based biomarker efflux`
  の二行に近い形で読める構造が残っておりました。
- この状態では、site 全体では `macroscopic CSF oscillation / parenchyma-CSF water exchange / respiration-conditioned net-flow / exercise-conditioned contrast influx / intrathecal tracer retention / CSF-to-blood clearance / CSF mobility / biomarker efflux` を別 object として扱っているのに、bundle composition の中核規則だけがそれを十分に要求していないことになります。

## 主要結論

- `human clearance evidence` は一つの reusable bundle row ではございません。
- 少なくとも
  - `macroscopic CSF oscillation`
  - `parenchyma-CSF water exchange`
  - `respiration-conditioned net-flow`
  - `exercise-conditioned contrast influx / parasagittal meningeal-lymphatic flow`
  - `intrathecal tracer / CSF-to-blood clearance capacity`
  - `CSF mobility`
  - `model-based biomarker efflux`
  を別 row として扱う必要がございます。
- したがって `Human Proxy Composition Card` でも、`clearance proxy` とだけ書くことは不十分であり、family-internal comparison family を固定しなければなりません。

## 根拠付き批判

### 1. `CSF oscillation` と `water exchange` と `net flow` は同じ観測量ではございません

- 根拠:
  - [Fultz et al. (2019)](https://doi.org/10.1126/science.aax5440) は human NREM sleep における coupled electrophysiology / hemodynamics / CSF oscillation を扱う route でございます。
  - [Kim, Huang, & Liu (2025)](https://doi.org/10.1016/j.neuroimage.2025.121142) は MT spin labeling による `parenchyma-CSF water exchange` route でございます。
  - [Lim et al. (2025)](https://doi.org/10.1038/s41467-025-66548-4) は awake-state 2D PC-MRI による `respiration-conditioned net flow` route であり、論文自体が plane-specific net flow は whole-brain bulk circulation の真値ではないと明記しております。
- 批判:
  - これらを一行の `clearance proxy` に圧縮すると、motion / exchange / flow という別 object が消えます。
  - その結果、carrier, crossed boundary, time window, intervention regime が見えなくなります。

### 2. `contrast influx` と `intrathecal tracer retention` と `biomarker efflux` も同じ route ではございません

- 根拠:
  - [Yoo et al. (2025)](https://doi.org/10.1038/s41467-025-58726-1) は exercise-conditioned intravenous-contrast route と parasagittal meningeal-lymphatic flow を扱う small healthy-young study でございます。
  - [Eide et al. (2023)](https://doi.org/10.1038/s41467-023-37685-5) は intrathecal gadobutrol retention と PK-based CSF-to-blood clearance variables を plasma biomarkers と関係づける clinical route でございます。
  - [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は randomized crossover と multicompartment model による overnight brain-to-plasma biomarker efflux route でございます。
- 批判:
  - contrast-influx, intrathecal clearance-capacity, biomarker efflux は同じ carrier class でも same-boundary でもございません。
  - したがって `human glymphatic evidence exists` の一語へ潰すと、model burden と intervention dependence が隠れます。

### 3. central composition rule がこの split を要求しないと、site 全体の taxonomy が back door で崩れます

- 根拠:
  - `wbe_101.md` と `wiki/homeostatic-plasticity-and-maintenance-state.md` はすでに clearance family を 7 以上の route へ分けております。
  - しかし central composition rule が `CSF mobility + biomarker efflux` 程度の reading で止まると、bundle 側では依然として `clearance row exists` と読めてしまいます。
- 批判:
  - これは `family-internal split` を मुख्य public rule に入れるという recent site policy と衝突いたします。
  - 結果として、front door で止めた誤読を central rule が再導入してしまいます。

## 今回実行した変更

- `wiki/human-proxy-composition.md`
  - front matter の `description`、`page_highlights`、`known_points` を、clearance family 内部の split を central rule に反映する文言へ更新しました。
  - `What this page fixes` に clearance family 圧縮を追加しました。
  - `2026-03-31 correction: clearance-route family-internal split also belongs inside bundle composition` note-box を追加しました。
  - central table の clearance rows を
    - `Sleep-state CSF-oscillation route`
    - `Human parenchyma-CSF water-exchange route`
    - `Human respiration-conditioned CSF net-flow route`
    - `Human exercise-conditioned contrast-influx route`
    - `Human intrathecal tracer / CSF-to-blood clearance route`
    - `CSF mobility MRI`
    - `Sleep-linked glymphatic efflux to plasma`
    の 7 行へ分解しました。
  - `Family-internal route collapse` を clearance family まで拡張しました。
  - `CSF mobility is not net clearance flux` note を `Human clearance is not one reusable bundle row` に改稿しました。
  - three-axes table でも clearance family を同じ 7 行へ分解しました。
  - references に `Fultz 2019`, `Kim/Huang/Liu 2025`, `Eide 2023`, `Lim 2025`, `Yoo 2025` を追加しました。

- `verification.md`
  - `Human Proxy Composition Card` に clearance family-internal split paragraph を追加しました。
  - `Proxy-row inventory and direct observables` に clearance family の typing rule を追加しました。
  - `Clearance / immune support` row と `Human evidence class / observability ceiling` row を、clearance route object の明示を要求する文言へ更新しました。

- 生成物
  - `ruby scripts/export_github_wiki.rb` を実行し、`github-wiki-export/human-proxy-composition.md` を同期しました。

## 今回止めた誤読

- `human clearance evidence` = one reusable bundle row
- `CSF oscillation` = `water exchange` = `net flow` = `contrast influx` = `intrathecal clearance` = `CSF mobility` = `biomarker efflux`
- `clearance proxy exists` = `local immune-controller state is partly measured`
- `bundle composition では clearance family 名だけで十分`

## 検証結果

- `git diff --check`
  - pass
- `ruby scripts/build_summary_booklet.rb`
  - pass
- `ruby scripts/export_github_wiki.rb`
  - pass
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - pass
- `bundle exec jekyll build`
  - pass

## 外部依存タスク

- なし
  - 今回の作業は一次文献確認、repo 内改稿、生成物同期、検証、commit、push までこのセッションで完結できます。
