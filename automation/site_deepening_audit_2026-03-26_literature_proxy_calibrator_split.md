# 2026-03-26 サイト深掘り監査: literature pages に残っていた human-proxy の二軸読解を三軸へ補正

- 対象ページ:
  - `research_harvest_50.md`
  - `mind_uploading_papers.md`
- 同期参照:
  - `wbe_101.md`
  - `verification.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `wiki/human-proxy-composition.md`
- web 確認対象:
  - `https://mind-upload.com/research_harvest_50.html`
  - `https://mind-upload.com/mind_uploading_papers.html`
- 調査範囲: 技術 / 自然科学のみ

## 1. 今回このページ群を選んだ理由

- 直近の site-wide ルールでは、living-human route は
  - `proxy class`
  - `operational maturity`
  - `calibrator role`
  の三軸で読む規則に更新されています。
- しかし literature 側のハブである `research_harvest_50.md` にはまだ
  - `proxy class is now read separately from route maturity`
  - `the in vivo papers are read on two axes at once`
  という旧説明が残っていました。
- `mind_uploading_papers.md` も shortlist の human in vivo row で `operational maturities` までは明示していた一方、`その route が何を較正できるのか` が独立項目になっていませんでした。
- これは自然科学的に弱いです。現在の一次文献が押し上げているのは「human in vivo measurement が一つ増えた」という事実ではなく、「どの family の proxy を、どこまで、どの burden で較正できるか」が route ごとに違うという点だからです。

## 2. 主批判

### 2-1. `proxy class + maturity` だけでは、route が何を較正できるかが固定されません

- <a href="https://doi.org/10.1523/JNEUROSCI.1750-23.2024" target="_blank">Johansen et al. (2024)</a> は 33 人健常者の in vivo SV2A atlas であり、較正できるのは `regional synaptic-density proxy comparison` です。現在の `synaptic efficacy` や branch-local weight を直接固定する論文ではありません。
- <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> は 51 人健常者と 13 人独立 site replication による five-metabolite parcel-similarity graph であり、較正できるのは `macro biochemical scaffold / similarity family` です。kinetic flux や cell-specific metabolic controller を直接与えません。
- <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li et al. (2025)</a> は dynamic deuterium MR spectroscopic imaging による whole-brain glucose transport / metabolism route であり、較正できるのは `macro energetic-rate family under a kinetic model` です。branch-local ATP reserve や mitochondrial positioning ではありません。
- <a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> と <a href="https://doi.org/10.1093/brain/awab466" target="_blank">Rzechorzek et al. (2022)</a> は specialized macro proxy class を押し上げますが、per-axon timing controller や local thermal controller の ground truth ではありません。
- <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a> と <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> は clearance-support physiology を押し上げますが、cell-specific immune-controller state や synapse-resolved clearance logic の readout ではありません。

### 2-2. calibrator role を欠くと、proxy-rich をそのまま state-rich に読み替えやすくなります

- `SV2A atlas`
- `five-metabolite MRSI graph`
- `dynamic deuterium energetic imaging`
- `macro myelin / thermal proxy`
- `CSF mobility / sleep-linked efflux`

これらはすべて real route ですが、同じ object を測っているわけではありません。

- したがって literature page が `route maturity` だけで整理すると、読者は `specialized but real` を `state-complete or broadly calibrating` と誤読できます。
- 現在の一次文献から安全に言えるのは、これらの route はそれぞれ別 family の calibrator であり、<strong>current transcription / chromatin</strong>, <strong>post-transcriptional RNA-state</strong>, <strong>phospho-signaling / second-messenger state</strong>, <strong>local proteostasis / synaptic-tag capture</strong>, <strong>cargo-routing</strong>, <strong>chloride set point</strong>, <strong>branch-local mitochondrial positioning</strong> などをまとめて閉じるわけではない、ということです。

### 2-3. literature pages は mixed archive の入口なので、旧ルール放置の害が大きいです

- `research_harvest_50.md` と `mind_uploading_papers.md` は、core page ではなく literature hub です。
- したがってここに旧ルールが残ると、reader は front-door 側の stricter rule を見落とし、mixed archive 側で再び `human proxy が増えた = hidden-state closure が進んだ` と読んでしまいます。
- 特に `research_harvest_50.md` の `two axes at once` は、現在の site-wide rule と明確に矛盾していました。

## 3. 今回実行した変更

- `research_harvest_50.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter の `page_highlights` を `proxy class / operational maturity / safe calibrator role` の三軸へ更新
  - `known_points` に「bounded calibrator は state-complete readout ではない」を追加
  - `Read human measurement papers as their own evidence class` の note-box を全面改稿
  - 同 note-box に
    - anchor route
    - direct observable
    - safe calibrator role
    - still not closed
    を並べた table を追加

- `mind_uploading_papers.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter の `known_points` / `page_highlights` に calibrator-role 軸を追加
  - 2025-2026 technical shortlist の `human in vivo observability / proxy ladder` 行を書き換え
    - what I can say now に `safe calibrator role` を明示
    - things I can't say yet に `calibrator-role logging` と `shared-driver audit` を追加
  - `technical-evidence-classes` 節の human-measurement lane を改稿し、Johansen / Lucchetti / Li / Baadsvik-Rzechorzek / Hirschler-Dagum がそれぞれ別 calibrator role を持つことを明記

## 4. 今回の修正で止めた誤読

- `proxy-rich = state-rich`
- `mature route = broadly calibrating route`
- `living-human observability = one common state meter`
- `human in vivo route が増えた = hidden-state family がまとめて閉じた`

## 5. 外部依存タスク

- なし。今回の修正はこのセッションで repo 内完結で実行可能でした。

## 6. 参考文献

1. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *J Neurosci*. 2024. https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Lucchetti F, Céléreau E, Steullet P, et al. Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-66124-w
3. Li Y, et al. Whole-brain glucose transport and metabolism with dynamic deuterium MR spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
4. Baadsvik EL, Weiger M, Froidevaux R, et al. Myelin bilayer mapping in the human brain in vivo. *Magn Reson Med*. 2024. https://doi.org/10.1002/mrm.29998
5. Rzechorzek NM, et al. Daily brain temperature rhythms and mortality after brain injury. *Brain*. 2022. https://doi.org/10.1093/brain/awab466
6. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nat Neurosci*. 2025. https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nat Commun*. 2026. https://doi.org/10.1038/s41467-026-68374-8
8. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023. https://doi.org/10.1016/j.crmeth.2023.100520
9. MICrONS Consortium, Bae JA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025. https://doi.org/10.1038/s41586-025-08790-w
