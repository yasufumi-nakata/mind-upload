# Site Deepening Audit (2026-03-16, Literature Evidence Class Axis)

## 対象

- 主対象: `mind_uploading_papers.md`
- 主対象: `research_harvest_50.md`
- 副対象: `wiki/paper-source-types-and-evidence-status.md`
- 副対象: `wiki/literature-and-evidence-reading.md`

## 今回の選定理由

- 2026-03-16 時点で、公開サイトは `技術・自然科学の優先ルート` をかなり明確に持てていました。
- ただし、文献ページの入口ではまだ `Scopus / arXiv / source_logged / curated` といった **掲載元・状態ラベル** が前景化されており、`その論文が技術的に何を直接増やすか` という **証拠クラス** は別軸として十分に固定されていませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、同じ一次研究でも
  - `local direct validation`
  - `task-limited system demonstration`
  - `dataset / benchmark / standard / toolchain`
  - `review / synthesis`
  - `philosophy / law / culture`
  は、WBE 議論の中で直接増やすものが根本的に違うからです。

## 主要な批判点

### 1. 旧サイトは `掲載元` と `証拠の効き方` を十分に分離できていませんでした

- 問題:
  - `mind_uploading_papers.md` と `research_harvest_50.md` は、Badge や `source_logged / curated` の説明は持っていました。
  - しかし、`Scopus から拾われた direct validator` と `Scopus から拾われた review`、`curated な benchmark paper` と `curated な task-limited demo` の違いを、入口仕様としては明示できていませんでした。
- 根拠:
  - <https://doi.org/10.1038/s41597-020-0467-x> の Mikulan et al. (2020)、<https://doi.org/10.1093/braincomms/fcad023> の Unnwongse et al. (2023)、<https://doi.org/10.1111/epi.18552> の Hao et al. (2025) は、EEG source imaging の **local direct validation** を与えます。
  - 一方、<https://doi.org/10.1038/s41593-023-01304-9> の Tang et al. (2023)、<https://doi.org/10.1038/s41467-025-65499-0> の d'Ascoli et al. (2025)、<https://doi.org/10.1038/s41586-023-06377-x> の Willett et al. (2023)、<https://doi.org/10.1038/s41593-025-01905-6> の Littlejohn et al. (2025)、<https://doi.org/10.1038/s41586-025-09127-3> の Wairagkar et al. (2025) が押し上げるのは、課題限定の decode / neuroprosthesis 性能です。
- 修正:
  - 4 ページすべてで `掲載元 / 文献種別 / サイト内状態 / evidence class` を分離しました。
  - `mind_uploading_papers.md` と `research_harvest_50.md` に、技術・自然科学向けの `evidence class` 表を追加しました。

### 2. 旧サイトは `dataset / benchmark / standard` 系の文献を、技術実証に近く読み替える余地を残していました

- 問題:
  - 文献ページでは、BIDS、LSL、MOABB、leaderboard governance の論文が技術 front の近くに置かれていました。
  - しかし、それらが直接増やすのは `reproducibility / comparability / governance` であって、`biological sufficiency` や `mechanistic truth` ではありません。
- 根拠:
  - <https://doi.org/10.1038/s41597-019-0104-8> の Pernet et al. (2019)、<https://doi.org/10.1038/s41597-024-03559-8> の Burns et al. (2024)、<https://doi.org/10.1162/imag.a.136> の Kothe et al. (2025) は、規格・同期・再利用条件を押し上げます。
  - <https://doi.org/10.1088/1741-2552/aadea0> の Jayaram & Barachant (2018)、<https://proceedings.mlr.press/v37/blum15.html> の Blum & Hardt (2015)、<https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html> の Roelofs et al. (2019) は、benchmark surface と leaderboard governance が score の意味を変えることを示しました。
- 修正:
  - `dataset / benchmark / standard / toolchain` を独立した evidence class として定義しました。
  - 文献地図では「curated でも benchmark class なら hidden state を解いたことにはならない」と site rule を明記しました。

### 3. 旧サイトは `review / context` を技術主導線から外すルールを入口で十分に固定していませんでした

- 問題:
  - これまでも本文中では broad archive だと書けていましたが、技術読者向けに `review は地図、philosophy / law / culture は context` と明示的に分類していませんでした。
- 修正:
  - `mind_uploading_papers.md` の新 table で `review / synthesis` と `context / philosophy / law / culture` を別行で切り分けました。
  - `research_harvest_50.md` では、技術・自然科学の既定ルートにおいて `review / synthesis / context` を「単独では U の解決証拠にしない」と明示しました。

### 4. 旧 wiki は `source type` と `evidence class` を同じページで十分に説明していませんでした

- 問題:
  - `wiki/paper-source-types-and-evidence-status.md` は source type と site state の読み方としては有用でした。
  - しかし、技術・自然科学の読者に最も必要な `何を直接増やす文献か` の軸がありませんでした。
- 修正:
  - タイトルを `文献のソース種別・状態・証拠クラスの読み方` へ更新しました。
  - 4 軸 table、evidence class table、よくある誤読の追加を行いました。
  - `wiki/literature-and-evidence-reading.md` 側も、この新しい軸を読むガイドへ更新しました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `evidence class` を明示する新節を追加
  - `Badge` と `evidence class` の違いを upfront に追加
  - 読み方 table に `evidence class` 行を追加
- `research_harvest_50.md`
  - `source_logged / curated` と `evidence class` を分ける共通 rule を追加
  - `dataset / benchmark class` を solved evidence と誤読しない運用を追加
- `wiki/paper-source-types-and-evidence-status.md`
  - 4 軸化
  - 技術・自然科学向け `evidence class` table を追加
  - 誤読パターンを増補
- `wiki/literature-and-evidence-reading.md`
  - `evidence class` 導線を追加
  - 4 rules 化
  - 関連 wiki の表記を更新

## 外部依存で保留

- 論文カード全件への `evidence class` タグ付与
  - 担当者: AI / maintainer
  - 前提条件: 全カードで `direct validator / system demo / standard-benchmark / review / context` を安定に付与する規約を確定すること
  - 完了条件: `mind_uploading_papers.md` と `research_harvest_50.md` の各カードを evidence class で絞り込めること

## 参考文献

- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Sci Data*. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Commun*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, et al. Direct validation of HD-EEG source imaging with simultaneous stereoelectroencephalography in focal epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS. *Sci Data*. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Burns M, Nii L, Williams AN, et al. Motion-BIDS. *Sci Data*. 2024.
  - https://doi.org/10.1038/s41597-024-03559-8
- Kothe C, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neurosci*. 2025.
  - https://doi.org/10.1162/imag.a.136
- Jayaram V, Barachant A. MOABB. *J Neural Eng*. 2018.
  - https://doi.org/10.1088/1741-2552/aadea0
- Blum A, Hardt M. The Ladder: A Reliable Leaderboard for Machine Learning Competitions. *PMLR*. 2015.
  - https://proceedings.mlr.press/v37/blum15.html
- Roelofs R, Shankar V, Recht B, et al. A Meta-Analysis of Overfitting in Machine Learning. *NeurIPS*. 2019.
  - https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html
