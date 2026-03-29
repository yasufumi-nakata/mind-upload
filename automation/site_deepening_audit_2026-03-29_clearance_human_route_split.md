# Site Deepening Audit (2026-03-29, human clearance-route split)

## 対象

- 主対象:
  - `index.md`
  - `wbe_101.md`
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- site の front door 側では `clearance / immune support` を route-family 単位で読む規則がかなり整っておりました。
- しかし文献ハブと一部表ではなお
  - `support-state mobility / efflux`
  - `CSF mobility and sleep-linked clearance`
  - `CSF-mobility or sleep-linked clearance physiology`
  のような圧縮が残っておりました。
- これは科学的に危険でございます。human clearance 系は少なくとも
  - macroscopic CSF oscillation
  - parenchyma-CSF water exchange
  - intrathecal tracer retention / CSF-to-blood clearance capacity
  - CSF-mobility MRI
  - model-based biomarker efflux
  に分けて読まなければ、direct observable と claim ceiling が混線いたします。

## 主要結論

- `human clearance evidence` は一つの測定対象ではございません。
- [Fultz et al. (2019)](https://doi.org/10.1126/science.aax5440) は sleep-linked macroscopic CSF oscillation を示す route であり、net molecular flux の ground truth ではございません。
- [Kim, Huang, & Liu (2025)](https://doi.org/10.1016/j.neuroimage.2025.121142) は parenchyma-CSF water exchange の route であり、protein-clearance capacity そのものではございません。
- [Eide et al. (2023)](https://doi.org/10.1038/s41467-023-37685-5) は intrathecal gadobutrol retention と PK-based CSF-to-blood clearance variables を扱う route であり、natural-sleep whole-brain clearance truth ではございません。
- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) は CSF mobility を扱う route であり、direct flux ground truth ではございません。
- [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) は model-based overnight biomarker efflux の route であり、local immune-controller identification ではございません。

## 根拠付き批判

### 1. `CSF mobility` と `biomarker efflux` は同じ観測量ではございません

- [Hirschler et al. (2025)](https://doi.org/10.1038/s41593-025-02073-3) の direct observable は region-specific CSF mobility MRI でございます。
- [Dagum et al. (2026)](https://doi.org/10.1038/s41467-026-68374-8) の direct observable は randomized crossover 睡眠実験を multicompartment model で解釈した overnight Aβ / tau efflux でございます。

批判:

- `mobility map exists` を `clearance truth exists` に変換してはいけません。
- 同じ `glymphatic` 周辺語彙でも、quantity type, model burden, time window, biological abstention boundary が違います。

### 2. `parenchyma-CSF water exchange` と `intrathecal tracer clearance` も同一ではございません

- [Kim, Huang, & Liu (2025)](https://doi.org/10.1016/j.neuroimage.2025.121142) は MT spin labeling による water-exchange route でございます。
- [Eide et al. (2023)](https://doi.org/10.1038/s41467-023-37685-5) は intrathecal gadobutrol retention と CSF-to-blood clearance variables の route でございます。

批判:

- 一方は water-exchange proxy、他方は exogenous tracer と PK model を含む clearance-capacity proxy でございます。
- したがって `human clearance route` の一語でまとめると、route burden と external-assumption burden を隠してしまいます。

### 3. `macroscopic CSF oscillation` はさらに別の route でございます

- [Fultz et al. (2019)](https://doi.org/10.1126/science.aax5440) は human NREM sleep 中の electrophysiology, hemodynamics, CSF oscillation の coupling を示しました。

批判:

- これは sleep-state coupled macro oscillation の route であり、protein efflux や segment-specific drainage assignment の direct measurement ではございません。
- にもかかわらず `sleep-linked clearance physiology` とだけ書くと、oscillation, transport, efflux が同じ row に潰れます。

### 4. 文献ハブでの再圧縮は front door の厳密化を打ち消します

- `index.md` と `wbe_101.md` で route split を入れても、`mind_uploading_papers.md` や `research_harvest_50.md` の表で再び compressed wording を使うと、読者は archive 側で旧来の誤読へ戻ります。

批判:

- literature hub は taxonomy を粗くしてよい場所ではございません。
- むしろ archive / evidence bank こそ `どの inferential object の論文を読んでいるのか` を最初に固定すべきでございます。

## 今回実行した変更

- `index.md`
  - clearance front-door note の `Eide et al. (2023)` を、説明内容に整合する [Nature Communications 論文](https://doi.org/10.1038/s41467-023-37685-5) に修正しました。

- `wbe_101.md`
  - human clearance proxy row を 1 行から 5 行へ分解しました。
  - `Fultz 2019`, `Kim, Huang, & Liu 2025`, `Eide 2023`, `Hirschler 2025`, `Dagum 2026` を別 row として記載しました。
  - entry-point note と composition-failure note の DOI を同期しました。
  - references に 3 本追加し、`Eide et al. (2023)` を Nature Communications 側へ修正しました。

- `mind_uploading_papers.md`
  - known-points、2026 technical addendum、human in vivo observability rows、destructive-vs-in-vivo note、route-name warning、quick-start rowを更新しました。
  - `support-state mobility / efflux` を route-family 名へ分解しました。

- `research_harvest_50.md`
  - human-measurement note を更新し、clearance-support calibrator を 1 行ではなく 5 route に分解しました。
  - anchor table に `Fultz`, `Kim, Huang, & Liu`, `Eide`, `Hirschler`, `Dagum` の個別 rows を追加しました。

## 今回止めた誤読

- `CSF mobility MRI` = direct flux ground truth
- `intrathecal tracer retention` = natural-sleep whole-brain clearance truth
- `model-based plasma efflux` = local immune-controller identification
- `sleep-linked clearance physiology` = one common measurable object
- `archive page だから route naming は粗くてよい`

## 外部依存タスク

- なし
  - 今回の変更は一次文献確認、repo 内改稿、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Fultz NE, Bonmassar G, Setsompop K, et al. Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. *Science*. 2019.
   - https://doi.org/10.1126/science.aax5440
2. Kim D, Huang Y, Liu J. Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121142
3. Eide PK, Lashkarivand A, Pripp A, et al. Plasma neurodegeneration biomarker concentrations associate with glymphatic and meningeal lymphatic measures in neurological disorders. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-37685-5
4. Eide PK, Ringstad G. Sleep deprivation impairs molecular clearance from the human brain. *Brain*. 2021.
   - https://doi.org/10.1093/brain/awaa443
5. Hirschler L, Runderkamp BA, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
6. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
