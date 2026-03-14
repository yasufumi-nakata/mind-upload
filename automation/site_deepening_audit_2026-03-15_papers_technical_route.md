# Site Deepening Audit (2026-03-15, Paper Collection / Technical Reading Route)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `wiki/literature-and-evidence-reading.md`

## 今回の選定理由

- `mind_uploading_papers.md` は broad archive としては有用ですが、2026-03-15 時点では技術・自然科学の一次証拠へ最短到達する構造が不足していました。
- 実際、2025 年の先頭表示には法学・形而上学・VR 作品論が並び、non-invasive language decode、侵襲 speech neuroprosthesis、ESI direct validation、maintenance-state といった実験フロンティアが埋もれやすい状態でした。
- これは技術・自然科学の観点で弱点です。なぜなら、年順アーカイブの先頭を「いま最も強い証拠」と誤読すると、サイト全体の evidence gate が崩れるからです。

## 主要な批判点

### 1. 旧ページは broad archive と evidence-ranked reading route を分離していませんでした

- 問題:
  - `mind_uploading_papers.md` は年別整理としては整っていましたが、`何を先に読むと技術フロンティアへ最短で届くか` が固定されていませんでした。
  - そのため、最新年の先頭にある非実験系文献を、実験 frontier の代表と誤読しうる構造が残っていました。
- 根拠:
  - Tang et al. (2023)、D&eacute;fossez et al. (2023)、d'Ascoli et al. (2025) は、非侵襲 language decode の一次文献として直接の到達点を与えます。
  - Willett et al. (2023)、Littlejohn et al. (2025)、Wairagkar et al. (2025) は、侵襲 speech neuroprosthesis の closed-loop / streaming front を押し上げています。
  - Mikulan et al. (2020)、Unnwongse et al. (2023)、Hao et al. (2025) は、ESI を direct validation で監査する系です。
  - Xu et al. (2024)、Looser et al. (2024)、Lee et al. (2022) は、connectome 外の maintenance-state を示します。
- 修正:
  - `mind_uploading_papers.md` に `技術・自然科学の優先ルート` を新設しました。
  - 年順アーカイブは維持しつつ、技術読者は年順の先頭から入らない site rule を本文へ明記しました。

### 2. 旧ページは「技術系で何を先に読むべきか」の単位が粗すぎました

- 問題:
  - 旧版のテーマ案内は `技術や計測に近い論文を見たい` 程度の粒度で、decode、closed loop、ESI、maintenance-state の区別が弱い状態でした。
  - これでは、decode 成功と emulation claim、local communication subsystem と whole-brain route、structural scaffold と hidden state を混同しやすくなります。
- 根拠:
  - d'Ascoli et al. (2025) は word decoding の前進を示しますが、subject-independent open-ended thought reading ではありません。
  - Wairagkar et al. (2025) は超低遅延 voice synthesis を示しますが、全脳 WBE ではありません。
  - Hao et al. (2025) は simultaneous HD-EEG/SEEG で ictal/interictal ESI の誤差監査を与えますが、一般的一意復元を与えません。
  - Xu et al. (2024) と Looser et al. (2024) は sleep-dependent renormalization と myelin/metabolic coupling を示し、connectome-complete を emulation-complete と読めないことを補強します。
- 修正:
  - `mind_uploading_papers.md` の案内表を、`非侵襲 language decode`、`侵襲 speech neuroprosthesis`、`直接妥当化つき ESI`、`maintenance-state / hidden variable` の 4 ルートへ再編しました。

### 3. 旧 wiki は「論文集は broad archive」という説明に留まり、技術読者の入り口を指定していませんでした

- 問題:
  - `wiki/literature-and-evidence-reading.md` は文献系ページの役割差を正しく説明していましたが、技術・自然科学の一次証拠だけを追いたい読者に対して、論文集内のどこから入るべきかを具体化していませんでした。
- 修正:
  - `wiki/literature-and-evidence-reading.md` に、技術読者は論文集の `技術・自然科学の優先ルート` から入るべきことを追記しました。

## 今回実行した変更

- `mind_uploading_papers.md`
  - `last_updated` を 2026-03-15 に更新
  - `年順 ≠ 証拠強度順` を front matter へ明記
  - `技術・自然科学の優先ルート` を追加
  - テーマ別の案内表を、decode / neuroprosthesis / ESI / maintenance-state の 4 ルートへ差し替え
- `wiki/literature-and-evidence-reading.md`
  - `last_updated` を 2026-03-15 に更新
  - 技術読者向けの読み方注記を追加
  - 論文集の役割説明へ `優先ルートから入る` ことを追記

## 外部依存で保留

- broad archive 全カードへの系統タグ付け
  - 担当者: AI / maintainer
  - 前提条件: 既存カード 100 件を `tech-primary / review / philosophy-law / culture-media` などへ再分類する運用基準を決めること
  - 完了条件: 年別カード全件が evidence-track と source-type の両方で絞り込めること

## 参考文献

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- D&eacute;fossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. *Nat Mach Intell*. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Sci Data*. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Elger CE, Pawley AD, Surges R, Avigdor T. Validating EEG source imaging using intracranial electrical stimulation in stereotyped seizure-onset patients. *Brain Commun*. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao Y, et al. Direct validation of HD-EEG source imaging with simultaneous stereoelectroencephalography in focal epilepsy. *Epilepsia*. 2025.
  - https://doi.org/10.1111/epi.18552
- Xu W, et al. Sleep restores an optimal computational regime in cortical networks. *Nat Commun*. 2024.
  - https://doi.org/10.1038/s41467-024-47838-5
- Looser ZJ, et al. Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health. *Nat Neurosci*. 2024.
  - https://doi.org/10.1038/s41593-023-01517-y
- Lee J-C, Wang C-Y, Lin C-L, Lu H-C. Synaptic memory survives molecular turnover. *Proc Natl Acad Sci U S A*. 2022.
  - https://doi.org/10.1073/pnas.2211572119
