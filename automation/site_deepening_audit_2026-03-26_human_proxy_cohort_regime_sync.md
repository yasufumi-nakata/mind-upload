# 2026-03-26 サイト深掘り監査: human proxy composition に残っていた cohort / regime collapse を停止線へ昇格

- 対象ページ:
  - `wiki/human-proxy-composition.md`
  - `faq.md`
- 同期生成物:
  - `summary_booklet.md`
- web 確認対象:
  - `https://www.nature.com/articles/s41467-025-66124-w`
  - `https://www.nature.com/articles/s41593-025-02073-3`
  - `https://www.nature.com/articles/s41467-026-68374-8`
  - `https://pubmed.ncbi.nlm.nih.gov/35086892/`
- 調査範囲: 技術 / 自然科学のみ

## 1. 今回この論点を選んだ理由

- 直近の site-wide rule では human proxy を
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  の三軸で読む構造はかなり整っております。
- しかし、それでもなお `どの cohort / physiological regime から得られた route なのか` が composition stop line としては弱い状態でした。
- これは自然科学的に重要です。developmental stage、aging regime、disease enrichment が違えば、同じ `human proxy` でも baseline physiology と transfer 可能性が変わるからです。
- とくに `wiki/human-proxy-composition.md` は composition 専用ページであるにもかかわらず、`quantity type / spatial unit / timescale / burden` までは見えていても、`mixed cohort を一つの human baseline と読んでよいか` を table-level で止め切れていませんでした。

## 2. 主批判

### 2-1. cohort / regime は measurement object の外側ではありません

- <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> の main cohort は Mindfulteen study の adolescents `13-15 years` であり、independent replication cohort は `15-35 years` の healthy controls です。
- <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> の main mobility maps は `healthy, younger individuals (33 ± 12 years)` で得られ、さらに CAA を別 cohort で扱っています。
- <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> は `49-66 years` の healthy older participants を対象にした randomized crossover sleep-deprivation study です。
- <a href="https://doi.org/10.2967/jnumed.121.263255" target="_blank">Villemagne et al. (2022)</a> は `76 ± 5.5 years` の volunteers を AD continuum で並べた reactive-astrogliosis PET です。

- したがって、これらを単に `human routes` と一括するだけでは弱いです。
- development、healthy younger adulthood、healthy older adulthood、AD-continuum pathology は同じ baseline ではありません。

### 2-2. 既存の三軸だけでは cross-cohort transfer を十分に固定できません

- `proxy class` が同定されても、それは route の quantity type を言うだけです。
- `operational maturity` が分かっても、それは hardware / burden / deployability の話です。
- `calibrator role` が分かっても、それは `何 family をどこまで較正できるか` の話であり、`別 cohort にどこまで持ち込めるか` とは別です。

- つまり、
  - `real proxy`
  - `specialized but meaningful route`
  - `bounded calibrator`
  を満たしていても、
  - `cross-cohort same-baseline`
  は自動では得られません。

### 2-3. FAQ front door にこの停止線がないと、読者は最後に混ぜてしまいます

- FAQ は `proxy-rich is not state-complete` をかなり前面化しています。
- しかし初心者は、最後に表だけ見て
  - `SV2A`
  - `MRSI similarity`
  - `CSF mobility`
  - `sleep-linked efflux`
  を `human evidence is converging` と一文でまとめがちです。
- そのとき cohort / regime の不一致が見えていないと、site-wide の stricter rule より先に誤読が固定されます。

## 3. 今回実行した変更

- `wiki/human-proxy-composition.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter の `description`, `page_intro`, `page_highlights`, `known_points` に `cohort / regime` 軸を追加
  - route-matrix に cohort 情報を補い、
    - Johansen = 33 healthy adults
    - Lucchetti = 51 adolescents + 13 healthy-control replication
    - Dagum = 49-66-year-old healthy older participants
    を明記
  - `Seven collapse errors` を `Eight collapse errors` に拡張し、`Cohort-regime collapse` 行を追加
  - 新規 note-box `Cohort and physiological regime are part of the measurement object` を追加
  - `three-axes` 節に、三軸は `per route` であり、composition では別途 `cohort / regime compatibility audit` が必要であることを追加

- `faq.md`
  - `last_updated` を `2026-03-26` に更新
  - `known_points` に mixed cohort を一つの baseline と読まない rule を追加
  - `Q2d` の note-box を `Four extra checks for proxy bundles` に更新
  - `Same cohort / regime?` の bullet を追加
  - FAQ 本文に `transfer argument` を要求する一文を追加

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` で再生成

## 4. 今回の修正で止めた誤読

- `human in vivo route が複数ある = one matched human baseline`
- `adolescent metabolic scaffold + healthy younger mobility + healthy older clearance = same maintenance ladder`
- `proxy class / maturity / calibrator role が揃えば cross-cohort transfer もほぼ自明`
- `reactive-astrogliosis PET` を healthy-memory proxy として混ぜる

## 5. 外部依存タスク

- なし。今回の修正は repo 内の公開本文・生成物・監査記録のみで完結しました。

## 6. 参考文献

1. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-66124-w
2. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02073-3
3. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026. https://doi.org/10.1038/s41467-026-68374-8
4. Villemagne VL, Rowe CC, Burnham S, et al. Assessing reactive astrogliosis with 18F-SMBT-1 across the Alzheimer disease spectrum. *Journal of Nuclear Medicine*. 2022. https://doi.org/10.2967/jnumed.121.263255
5. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024. https://doi.org/10.1523/JNEUROSCI.1750-23.2024
