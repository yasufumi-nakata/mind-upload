# Site Deepening Audit (2026-04-01, research_harvest issue-lead provenance hygiene)

## 対象

- 主対象:
  - `research_harvest_50.md`
- 調査範囲:
  - 技術
  - 自然科学

## 今回この箇所を選んだ理由

- `research_harvest_50.md` は現在，technical / natural-science readers に対してかなり厳密な route-family split を要求しており，
  - review
  - primary paper
  - secondary / media lead
  - bounded human proxy
  - controller-side causality
  を混線させないことが site-wide rule になっております。
- しかし同ページの `Issue integration and RQ audit (2026-02-24)` 節だけは，
  - `Neuron URL (PII: S0896-6273(25)00843-8)`
  - `Neuroscience News URL`
  のような intake-level wording を public evidence bank 上に残しており，
  - source class
  - evidence class
  - routing metadata
  の区別が崩れておりました。
- これは technical archive として弱点でございます。理由は，現在の site 本体が `Review` と `Media` を evidence class としては別扱いにしているにもかかわらず，この節だけがなお
  - review が U3 primary anchor であるかのような印象
  - news URL が U13 integrated evidence の入り口であるかのような印象
  を残していたためでございます。

## 根拠付き批判

### 1. `Issue integration` 節は，現在の site-wide evidence policy より provenance 要求が弱うございました

- `research_harvest_50.md` 冒頭ではすでに
  - intake logs と academically integrated evidence を分ける
  - contamination を防ぐ
  という rule を掲げております。
- また `mind_uploading_papers.md` と `wiki/paper-source-types-and-evidence-status.md` でも，
  - `Review`
  - `Media`
  - `DOI`
  - `source_logged`
  は同じ意味ではないと明示しております。
- それにもかかわらず `Issue integration` 表が
  - `PII`
  - `Neuroscience News URL`
  を public-facing evidence table にそのまま残すと，
  review / media / primary の境界が弱くなります。

### 2. `10.1016/j.neuron.2025.10.036` は U3 の controller-side primary anchor そのものではなく，review / route-mapping source でございます

- web で確認したところ，
  - DOI `10.1016/j.neuron.2025.10.036`
  - title `Resolving the mysteries of brain clearance and immune surveillance`
  - Neuron review
  であり，controller-side causal paper そのものではございません。
- U3 の main section はすでに，
  - `Kim et al. (2025)` meningeal lymphatics-microglia route
  - `Dewa et al. (2025)` multiday astrocytic stabilization route
  - `Bukalo et al. (2026)` astrocyte-enabled amygdala route
  - `Mai-Morente et al. (2025)` pericyte support route
  - `Hirschler et al. (2025)` / `Dagum et al. (2026)` bounded human support-state observability
  などの primary papers を軸に組み上がっております。
- したがって public issue-intake 表が review を primary anchor のように見せるのは，現在の U3 route-family reading と整合いたしません。

### 3. `#265` の `Neuroscience News URL` 表記は，primary-source verified archive としては停止線が甘うございました

- U13 ではすでに `Horikawa (2025)` の primary paper
  - DOI `10.1126/sciadv.adw1464`
  - `Mind captioning: Evolving descriptive text of mental content from human brain activity`
  が site 内で参照されております。
- その状態で public issue-intake 表に `Neuroscience News URL` を残すと，
  - secondary coverage が evidence class の一部である
  - あるいは source typing が未完である
  かのように読めてしまいます。
- これは evidence bank としては弱く，issue lead は routing metadata に格下げし，integrated evidence は primary DOI に寄せるべきでございます。

### 4. `structure/humor/immunity` は scientific English として不正確で，U3 の current meaning を誤らせうる表現でございました

- `humor` は明らかに `humoral` か `fluid-side support` を誤っており，
  technical / natural-science page では残すべきではございません。
- U3 の current public reading は
  - structure
  - humoral / support-state
  - immune support
  の split に近いため，少なくとも public row ではそれが読み取れる表記へ直す必要がございました。

## web で確認した主な資料

- `10.1016/j.neuron.2025.10.036`
  - *Neuron* review: `Resolving the mysteries of brain clearance and immune surveillance`
- `10.1126/sciadv.adw1464`
  - *Science Advances* primary paper: `Mind captioning: Evolving descriptive text of mental content from human brain activity`

## 今回実行した変更

### `research_harvest_50.md`

- `last_updated` を `2026-04-01` に更新しました。
- `page_highlights` に，issue lead は source class を保持し，integrated evidence は verified primary source に寄せる rule を追加しました。
- `known_points` に，同じ provenance rule を加えました。
- `Issue integration and RQ audit` を `Issue-lead routing and RQ audit` に改稿しました。
- 冒頭説明を，
  - issue lead は routing metadata
  - primary DOI または review-level route map が確認できたら source class を明示する
  という方針へ更新しました。
- intake table を
  - `Issue lead`
  - `Verified source class`
  - `Evidence routing decision`
  - `Status`
  の 4 列へ差し替えました。
- `#264` は review / route-mapping source として扱い，U3 本文の primary anchors と混同しないように明記しました。
- `#265` は secondary-news lead から primary DOI へ解決したことを明記しました。
- `Why this provenance correction matters` note-box を追加し，
  - review は route map
  - media lead は lead
  - integrated evidence は verified source class
  であることを public text で固定しました。
- `U3` diversity row の `structure/humor/immunity` を `structure / humoral / immune support` に修正しました。

## 今回止めた誤読

- `review DOI` = `U3 controller-side primary anchor`
- `news URL` = `integrated evidence class`
- `issue intake` と `academic integration` は public page 上で同じ層
- `humor/immunity` は U3 の scientific split を表している

## 検証予定

- `bundle exec jekyll build`
- `git diff --stat`
- `git diff --check`

## external dependency tasks

- なし
  - 今回の作業は source-class web 確認，public page 修正，監査メモ追加，ローカル検証，commit，push までこのセッションで完結できます。

## 参考

1. Kipnis J, et al. Resolving the mysteries of brain clearance and immune surveillance. *Neuron*. 2025. https://doi.org/10.1016/j.neuron.2025.10.036
2. Horikawa T. Mind captioning: Evolving descriptive text of mental content from human brain activity. *Science Advances*. 2025. https://doi.org/10.1126/sciadv.adw1464
