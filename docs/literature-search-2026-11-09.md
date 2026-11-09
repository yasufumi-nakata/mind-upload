# Literature expansion method / 文献探索方法（2026-11-09）

This is a documented, scoped expansion of the existing technical guide, not an exhaustive systematic review. The search date is 9 November 2026. The evidence library starts from 61 adopted records and ends at 67: 57 literature sources and 10 official/historical web resources. Six sources were added after reading the full-text sections supporting the new claims. Existing records were checked for identifiers, DOI duplicates and citation coverage, but the 51 earlier literature sources were not all reread.

既存の技術ガイドを対象とする範囲限定の追補です。網羅的なシステマティックレビューではありません。2026年11月9日に探索し、既存61件へ本文の関連箇所を確認した6件を追加しました。公開目録は文献57件、公式・歴史的ウェブ資料10件の計67件です。既存資料はID・DOI重複・引用箇所を点検しましたが、既存の51文献すべてを再読したわけではありません。

## Domains / 探索領域

| Domain / 領域 | Question / 確認する問い | Outcome / 今回の反映 |
|---|---|---|
| Structural acquisition / 構造取得 | What is measured, omitted or corrected? / 計測・省略・校正の範囲は何か | CAVE versioning; sequencing and X-ray methods require further review / CAVEの版管理を採用、配列・X線方式は追加精読が必要 |
| Activity and latent states / 活動・潜在状態 | Spatial coverage, sampling, missing cells and spikes? / 空間被覆・時間間隔・欠測は何か | 2026 zebrafish voltage study / 2026年ゼブラフィッシュ電位計測 |
| Molecular state and memory / 分子状態・記憶 | Which information is necessary beyond wiring? / 接続以外に何が必要か | Prior evidence retained; molecular/engram candidates remain unreviewed / 既存根拠を維持、追加候補は未読 |
| Preservation / 保存 | Morphology, metabolism, physiology, plasticity or retained learned memory? / 何を保存後に検証したか | Mouse hippocampal vitrification, with selection and inference limits / 海馬ガラス化と選択・推論の限界 |
| System identification / 同定 | Can unseen interventions separate equivalent models? / 未見介入でモデルを区別できるか | Proposed held-out intervention and added-state experiments / 未見介入・追加状態の実験案 |
| Computing and embodiment / 計算・身体 | Measured resources and genuine closed-loop behavior? / 実測資源と閉ループ行動は何か | NeuroMechFly v2; no whole-individual reconstruction claim / 身体モデルを採用、個体再現とは区別 |
| Reproducibility / 再現可能性 | Can another implementation reconstruct inputs and versions? / 別実装で入力・版を再現できるか | NWB, SONATA, CAVE; interoperable formats do not prove model correctness / 標準形式とモデルの妥当性を区別 |
| Whole-brain integration / 全脳統合 | Do studies support original-individual memory across the complete chain? / 元個体の記憶を工程全体で検証したか | Prior whole-brain-emulation roadmap and rubric retained / 既存計画・配点を維持 |

## Search and screening / 検索と選別

Thirty-five targeted English/Japanese web queries were run, followed by publisher, PubMed/PMC, preprint and institutional-source checks and reference-list discovery. Search hits were discovery aids, not evidence. Article pages, full-text HTML and an author-hosted publication PDF were used where available. An abstract, metadata entry, news story or download alone did not qualify a source for publication.

英日35検索式から、出版社、PubMed/PMC、プレプリント、研究機関の情報へ進み、参考文献も探索しました。検索結果は候補発見の手段です。公開引用への採用には、本文の関連箇所と主張の照合を必要としました。抄録・書誌・ニュース・ダウンロードのみでは採用していません。

### Queries actually used / 実行した検索式

1. whole brain emulation 2025 2026 research roadmap connectome function memory preservation
2. MICrONS 2025 functional connectomics mouse visual cortex Nature synapses
3. Drosophila whole brain connectome 2024 2025 computational model behavior Nature
4. brain tissue vitrification electrophysiological function recovery 2025 2026 PNAS cryopreservation
5. PATHFINDER automated proofreading connectomics 2025 paper
6. C elegans neuropeptide connectome 2023 2024 functional atlas Nature
7. virtual rodent embodied digital twin neural activity 2024 Nature
8. "whole brain" "emulation" "2026" research preprint -site:reddit.com
9. "whole-brain" "recording" "2025" "2026" voltage imaging
10. "brain" "vitrification" "2026" "synaptic" memory
11. "memory" "engram" "2025" "2026" synaptic molecular connectome
12. "brain simulation" "2025" "2026" "NEST" GPU
13. "SONATA" "Neurodata Without Borders" simulation model reproducibility
14. "connectomics" "2026" "2025" "expansion" "protein" synapse
15. "whole brain emulation" "identifiability" "2025" "2026"
16. "Synaptic connectomics by sequencing"
17. "NeuroMechFly v2" embodied sensorimotor 2024
18. "Neurodata Without Borders" 2022 eLife 78362
19. "Accelerating neuron reconstruction with PATHFINDER" 2026
20. "Connectome-seq" "2026" single synapse
21. "whole brain" "non-destructive" connectomics resolution magnetic resonance
22. "neural system identification" "2025" "2026" intervention identifiability
23. "human brain" "connectome" "2026" electron microscopy
24. "Reconstruction and Simulation of Neocortical Microcircuitry" Markram 2015
25. "A connectome is not enough" Scheffer Meinertzhagen
26. "whole-brain" simulation "memory bandwidth" "2026"
27. "connectome" "error" "functional" "perturbation" model 2025 2026
28. "MICrONS" "data" "2026" functional connectomics
29. "brain preservation" "memory retention" "2025" "2026"
30. "whole brain emulation" "benchmark" "2026" "model"
31. "mind uploading" "review" "2026" "research" -site:reddit.com
32. 全脳エミュレーション 全脳シミュレーション 2025 2026 理研
33. マインドアップロード 神経回路 記憶 復元 研究 論文
34. 脳 デジタルツイン 2026 シミュレーション Fugaku
35. brain preservation engram memory recovery vitrification 2026 review

## Adoption and version rules / 採用・版管理の規則

- Prefer primary experimental/method papers for scientific claims; retain official sources for project descriptions. Distinguish peer-reviewed publications, preprints, reviews and our own experimental designs.
- Match title, authors, publication year, DOI and venue against the publisher or article header. DOI year strings do not necessarily equal publication years.
- Normalize DOI case, URL prefixes and percent-encoding before duplicate detection. Different DOI records still need human work-level comparison: a preprint, publication, dataset and commentary are not interchangeable.
- Record organisms, sample scope, measured variables and limitations. Do not infer whole-organism memory, original-individual reconstruction or consciousness from local structural, electrophysiological or behavioral results.
- Public entries specify the reviewed sections. Figure captions, visual inspection, supplements, raw-data reanalysis and code reproduction are different review operations. This update did not independently inspect figure pixels or supplementary files, reproduce code or reanalyse raw datasets.
- Keep unreviewed discovery candidates separate from published evidence. No full texts, private inventories or acquisition logs are committed.

一次論文と公式資料を役割に応じて使い分け、題名・著者・年・DOI・掲載先を原典と照合しました。DOIの正規化だけでプレプリントと出版版の同一性が判定できるわけではありません。解説・データセットも原著と区別します。本文の確認範囲は各レコードに記録し、図説明と図像、別添補足、元データ、コードの再現を同一視しません。未読候補や本文ファイルは公開リポジトリに追加しません。

## Six adopted sources / 採用6資料

| Stable ID | Canonical source | Contribution / 使い方 |
|---|---|---|
| WANG2026_VOLTAGE | [Wang et al., Nature Methods (2026)](https://doi.org/10.1038/s41592-026-03179-7) | Spatial coverage versus neuron/spike completeness / 空間被覆と細胞・スパイクの網羅性を分ける |
| GERMAN2026_VITRIFICATION | [German et al., PNAS (2026)](https://doi.org/10.1073/pnas.2516848123) | Local physiological recovery versus remembered information / 局所機能と記憶の保持を分ける |
| DORKENWALD2025_CAVE | [Dorkenwald et al., Nature Methods (2025)](https://doi.org/10.1038/s41592-024-02426-z) | Versioned reconstruction and annotations / 校正・注釈の版を固定する |
| DAI2020_SONATA | [Dai et al., PLOS Computational Biology (2020)](https://doi.org/10.1371/journal.pcbi.1007696) | Portable model descriptions and simulation conditions / モデル記述と計算条件を渡す |
| RUBEL2022_NWB | [Rübel et al., eLife (2022)](https://doi.org/10.7554/eLife.78362) | Aligned multimodal measurements / 複数の計測と時刻を対応させる |
| WANGCHEN2024_NMF2 | [Wang-Chen et al., Nature Methods (2024)](https://doi.org/10.1038/s41592-024-02497-y) | Closed-loop embodied testing / 身体・環境との閉ループ評価を組む |

The [machine-readable index](../data/literature-index.json) is generated from the adopted references and actual bilingual page-section citations. The build rejects duplicate DOI records, inconsistent IDs and missing bilingual review scopes. Source records, JSON and BibTeX remain synchronized.

[機械可読索引](../data/literature-index.json)は採用資料と英日各ページの実際の引用から生成します。ID、DOI重複、英日の確認範囲をビルドで検査し、書誌JSON・BibTeXとの対応を保ちます。

## Limits and continuation / 限界と次の探索

This round did not export or screen all records from Scopus, Web of Science, PubMed or other specialist databases. Search ranking, access and English/Japanese language selection create bias. Neither a complete search-result denominator nor formal saturation was established, so no PRISMA-style completeness claim or recall percentage is reported. Citation chasing can discover adjacent methods without establishing their relevance or validating their claims.

Next review priorities are sequencing and X-ray connectomics, molecular/engram measurements, automated proofreading, optimal perturbation design and large-scale simulations. Each requires legitimate full text, work/version matching and explicit claim-level review before adoption. The new research designs do not change achievement scores or establish a completed mind upload.

専門データベースの全件抽出・スクリーニングは行っていません。順位・アクセス・英日中心の言語選択による偏りが残ります。検索結果全体の母数や正式な飽和は確立していないため、PRISMAに相当する完全性や再現率を主張しません。次の優先精読は配列・X線コネクトミクス、分子・エングラム計測、自動校正、最適介入、大規模モデルです。正規の本文、版の対応、主張単位の照合を経て採用します。追加した実験案は未実施であり、達成率を変更していません。
