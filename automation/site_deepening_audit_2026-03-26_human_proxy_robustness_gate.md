# 2026-03-26 サイト深掘り監査: human proxy composition に残っていた robustness gate 不足

- 対象ページ:
  - `verification.md`
  - `wiki/human-proxy-composition.md`
  - `wbe_101.md`
- web 確認対象:
  - `https://pubmed.ncbi.nlm.nih.gov/28792356/`
  - `https://pubmed.ncbi.nlm.nih.gov/30408072/`
  - `https://pubmed.ncbi.nlm.nih.gov/33592241/`
  - `https://doi.org/10.1093/brain/awac335`
  - `https://pubmed.ncbi.nlm.nih.gov/41499248/`
- 調査範囲: 技術 / 自然科学のみ

## 1. 今回この論点を選んだ理由

- `Human Proxy Composition Card` はすでに
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  - `common-driver audit`
  - `increment over the strongest single row`
  を要求しておりました。
- しかし、それでもなお `bundle 自体が本当に頑健か` を止める定量 stop line が弱い状態でした。
- 具体的には、
  - 各 row が同じ acquisition route で繰り返して安定か
  - 別施設 / 別 scanner / 別 setup でも残るか
  - full bundle が complete-case subset にしか成立していないのではないか
  がカード本文に入っておりませんでした。
- これは自然科学的に重要です。`何を測っているか` が整理されていても、`その row が不安定`、`一施設依存`、`一部 subject にしか取得できない` のであれば、bundle を state-identification 側へ押し上げる根拠としては弱いままだからです。

## 2. 主批判

### 2-1. 良い taxonomy だけでは、良い measurement になりません

- <a href="https://doi.org/10.1177/0271678X17724947" target="_blank">Finnema et al. (2018)</a> は [<sup>11</sup>C]UCB-J SV2A PET の kinetic modeling と test-retest reproducibility を評価し、regional V<sub>T</sub> の mean absolute test-retest reproducibility が `3-9%` であることを示しました。
- 重要なのは、この論文が `SV2A PET は reproducible` と一般化していない点です。reproducibility は tracer / kinetic route / quantification 条件に結びついています。
- したがって、proxy row は `density proxy` と分類されるだけでは不十分であり、`その route でどの程度安定か` を別項目で持つ必要があります。

### 2-2. MRI / fMRI 系は特に `one reliability level` ではありません

- <a href="https://doi.org/10.1371/journal.pone.0206583" target="_blank">Holiga et al. (2018)</a> は 8 個の tb-fMRI task、6 個の rs-fMRI metric、CBF を比較し、test-retest reliability が `poor to excellent` まで大きく分散することを示しました。
- これは bundle 読解に直接効きます。bundle の一部に fMRI / rs-fMRI 系 row が入っていても、その row の repeatability は自動では高くありません。
- したがって `multimodal` や `same-session` というラベルだけでは、bundle の科学的強度を上げられません。

### 2-3. cross-centre robustness は実証できるが、前提にはできません

- <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a> は 4 centres、1.5T から 7T、64 / 256 electrode の simultaneous EEG-fMRI で、crossmodal correlation が再現的に抽出できることを示しました。
- この含意は二重です。
  - 良い側面として、cross-centre reproducibility は実際に検証可能です。
  - 悪い側面として、検証されていない bundle にそれを黙って仮定してはいけません。
- したがって card は `same-lab success` と `portable / field-ready` を分ける必要があります。

### 2-4. 完全な bundle は臨床・実運用ではしばしば subset です

- <a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> の CONNECT-ME study では 87 acute DoC patients のうち、EEG は 86、fMRI は 64、両方は 63 でした。さらに full-feature same-sample comparison は 48 patients に基づいています。
- これは `multimodal bundle` がしばしば complete-case subset に依存することを示します。
- <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> も multimodal multicentre validation を行い、modality 数が増えると性能は上がる一方で、minimally conscious state や improving patients では inter-modality disagreement が高いことを示しました。
- したがって `full bundle wins` だけでは不十分であり、
  - complete-case sample size
  - one-row-missing / degraded-row slice
  - disagreement profile
  を開示しないと、bundle の一般性を過大評価します。

## 3. 今回実行した変更

- `verification.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - `page_highlights` と `known_points` を更新し、Human Proxy Composition Card に `repeatability / transfer window` を含めることを front matter に反映しました。
  - `human-proxy-composition-card` の addendum に、Finnema / Holiga / Wirsich / Amiri / Manasova を用いた robustness critique を追加しました。
  - card table に以下の 3 行を追加しました。
    - `Per-row repeatability / reproducibility window`
    - `Cross-center / cross-scanner / protocol transfer`
    - `Acquisition completeness / missing-row slice`
  - `Promotion rule beyond row diversity` と `Additional audit logs` の Human Proxy Composition Card bullet を新ルールに合わせて更新しました。

- `wiki/human-proxy-composition.md`
  - front matter の `description`, `page_intro`, `page_highlights`, `known_points` を更新し、robustness gate を page-level rule に引き上げました。
  - 新規 note-box `Why robustness belongs inside the composition rule` を追加しました。
  - `What must be fixed before a proxy bundle is promoted` の table に
    - row-level repeatability
    - cross-centre transfer
    - partial-availability / missing-row slice
    を追加しました。
  - `Operational rule on this site` を更新し、row diversity だけでは state closure を認めないことを明確化しました。
  - references に Finnema / Holiga / Wirsich / Amiri / Manasova を追加しました。

- `wbe_101.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - `human-proxy-composition-rule` の front-door 要約を更新し、bundle promotion 条件を 8 項目から 11 項目へ拡張しました。
  - front-door でも `repeatability`, `cross-centre transfer`, `missing-row robustness` を明示しました。

## 4. 今回の修正で止めた誤読

- `proxy class / maturity / calibrator role が整っていれば bundle は十分に強い`
- `同じ session で複数 row が動いた = その bundle は安定`
- `同じ lab で multimodal relation が出た = portable`
- `full bundle の性能 = 実運用で一般に得られる性能`
- `multimodal improvement = disagreement や missing-row sensitivity を無視してよい`

## 5. 外部依存タスク

- なし。今回の修正は repo 内の公開本文と監査記録の更新のみで完結しております。

## 6. 参考文献

1. Finnema SJ, Nabulsi NB, Mercier J, et al. Kinetic evaluation and test-retest reproducibility of [<sup>11</sup>C]UCB-J, a novel radioligand for positron emission tomography imaging of synaptic vesicle glycoprotein 2A in humans. *J Cereb Blood Flow Metab*. 2018. https://doi.org/10.1177/0271678X17724947
2. Holiga Š, Sambataro F, Luzy C, et al. Test-retest reliability of task-based and resting-state blood oxygen level dependence and cerebral blood flow measures. *PLoS One*. 2018. https://doi.org/10.1371/journal.pone.0206583
3. Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.117864
4. Amiri M, Fisher PM, Raimondo F, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023. https://doi.org/10.1093/brain/awac335
5. Manasova D, Belloli LML, Rosenfelder MJ, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
