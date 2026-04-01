# Site Deepening Audit (2026-04-01, therapeutic invasive decoding route split)

## 対象

- 主対象:
  - `wbe_101.md`
  - `wiki/decode-vs-emulate.md`
- 同期対象:
  - `github-wiki-export/decode-vs-emulate.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://mind-upload.com/wbe_101.html`
- `https://mind-upload.com/wiki/decode-vs-emulate.html`
- `https://doi.org/10.1038/s41551-025-01467-9`
- `https://doi.org/10.1038/s41591-024-03196-z`
- `https://doi.org/10.1038/s41531-026-01273-3`

## 今回この箇所を選んだ理由

- 2026-04-01 時点の site は、侵襲的 language / speech BCI の
  - same-session throughput
  - transfer-assisted initialization
  - fixed-decoder durability
  - adaptive rescue
  をかなり良く分離できておりました。
- しかしその一方で、2025 に明確化した **connectomics-informed across-patient therapeutic decoding** が、入口ページではまだ独立ルートとして前面化されておりませんでした。
- この欠落は技術的に重要でございます。理由は、
  - 患者個別学習なしの invasive decoding
  - 症状リンク型 adaptive stimulation
  - 生理状態ガード付き feedback decoding
  が、communication BCI とも emulation とも異なる route class だからでございます。

## 主要結論

- `generalizable invasive decoder` は一語では読めません。
- 少なくとも次を分離する必要がございました。
  - communication throughput
  - transfer-assisted initialization
  - connectomics-informed across-patient therapeutic decoding
  - personalized controller / biomarker selection
  - physiological-state guard
  - adaptive rescue
- よって site の safe ceiling は、
  - `symptom-/state-conditioned therapeutic-control route`
  - `connectomics-informed across-patient decoder family`
  に留めるべきであり、`subject-free universal decoder` や `emulation-adjacent internal-state readout` に昇格させるべきではございません。

## 根拠付き批判

### 1. across-patient decoding without individual training は重要ですが、対象は universal decode ではありません

- [Merk et al. (2025)](https://doi.org/10.1038/s41551-025-01467-9) は、
  - `56` implanted patients
  - `1,480` ECoG channels
  - four cohorts
  を用いた movement decoding で、patient individual training なしの across-patient route を示しました。
- 同論文はさらに、
  - subgenual cingulate emotion decoding
  - seizure-related connectomic network discovery
  へ同じ platform を拡張しております。

批判:

- これは **symptom-linked therapeutic decoding** の強い前進であり、communication BCI の単純延長でも、WBE 的 internal-state readout でもございません。
- implant target、task label、disease context、network prior が変われば意味も変わるため、`generalizable invasive decode` を一つの成功列として front door に出すのは粗すぎました。

### 2. adaptive neurostimulation は generic controller success ではなく personalized biomarker selection を含みます

- [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z) は、4 人の Parkinson's disease 患者で stimulation-entrained gamma を高/低 dopaminergic state の marker として選び、personalized adaptive neurostimulation を実装しました。

批判:

- したがって adaptive DBS の成功は、
  - signal exists
  - controller is fixed
  - same control law generalizes
  の 1 本線ではございません。
- biomarker selection 自体が route burden であるため、therapeutic decoding を `adaptive BCI success` と一語で束ねるのは技術的に甘いです。

### 3. physiological context は同じ feedback band を benign にも動かします

- [Zhu et al. (2026)](https://doi.org/10.1038/s41531-026-01273-3) は、
  - `18` Parkinson's disease
  - `18` dystonia
  患者で eyes-open / eyes-closed state が basal ganglia theta/alpha dynamics を動かし、fixed threshold が benign physiological change を pathology と取り違えうることを示しました。

批判:

- したがって therapeutic decoder は `band threshold` だけでは読めません。
- 少なくとも
  - physiological-state guard
  - contextual validation
  - trigger abstention / withholding rule
  が別提出物であることを入口ページに visible にする必要がございました。

## 今回実行した変更

### `wbe_101.md`

- front matter の `page_highlights` / `known_points` を更新し、invasive route を
  - throughput
  - transfer-assisted initialization
  - connectomics-informed across-patient symptom decoding
  - fixed-decoder durability
  - adaptive rescue
  に分ける rule を明記しました。
- `Technology-route comparison` table の invasive / hybrid neuroprosthesis row に `Merk et al. (2025)` を追加しました。
- safe reading と missing 条件に
  - symptom decoding
  - physiological-state guard
  を追加しました。
- `2026-04-01 addendum: therapeutic invasive decoders are not one universal route` note-box を新設しました。
- references に
  - Merk et al. (2025)
  - Oehrn et al. (2024)
  - Zhu et al. (2026)
  を追加しました。

### `wiki/decode-vs-emulate.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` / `known_points` / `unknown_points` に、therapeutic invasive decoding の独立 route rule を追加しました。
- 冒頭に `2026-04-01 correction: therapeutic invasive decoding is not the communication route` note-box を追加しました。
- 新しい `therapeutic invasive decoding has a different ceiling` section を追加し、
  - across-patient network prior
  - personalized controller
  - physiological-state guard
  の 3 ceiling を table で固定しました。
- `Boundary cases seen in primary literature` table に `Merk et al. (2025) / Zhu et al. (2026)` row を追加しました。
- `G5` を更新し、therapeutic decoding では `controller family` と `physiological-state guard` が別ログであることを追加しました。
- site rule に `therapeutic invasive decoding` 専用 bullet を追加しました。
- references に
  - Merk et al. (2025)
  - Oehrn et al. (2024)
  - Zhu et al. (2026)
  を追加しました。

### `github-wiki-export/decode-vs-emulate.md`

- `ruby scripts/export_github_wiki.rb` により、同じ修正を GitHub Wiki export 側へ同期する想定でございます。

## 今回止めた誤読

- `generalizable invasive decoder` = `subject-free universal decoder`
- `connectomics-informed decoding` = `WBE-relevant state readout`
- `adaptive DBS success` = `one generic controller law`
- `one oscillatory biomarker threshold` = `stable disease-state meter`
- `therapeutic invasive decoding` = `speech neuroprosthesis` と同じ route

## 検証予定

- `ruby scripts/export_github_wiki.rb`
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `bundle exec jekyll build`
- `git diff --check`
- `rg -n "therapeutic invasive decoding|connectomics-informed across-patient|physiological-state guard|patient individual training" ...`

## external dependency tasks

- なし
  - 今回の作業は、一次文献確認、repo 内公開文面修正、wiki export 同期、ローカル build 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Merk T, Li N-F, Butenko K, et al. Invasive neurophysiology and whole brain connectomics for neural decoding in patients with brain implants. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01467-9
2. Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. *Nature Medicine*. 2024.
   - https://doi.org/10.1038/s41591-024-03196-z
3. Zhu G-Y, Merk T, Butenko K, et al. Decoding the impact of visual states on adaptive deep brain stimulation feedback signals in movement disorders. *npj Parkinson's Disease*. 2026.
   - https://doi.org/10.1038/s41531-026-01273-3
