# Site Deepening Audit (2026-03-14, Tech Roadmap / Brain-to-Text Evidence Gate)

## 対象

- 主対象: `tech_roadmap.md`

## 今回の選定理由

- `tech_roadmap.md` は公開サイトの主要導線であり、ここでの比較軸が甘いと `Perspective` や `Verification` で整えた厳密さが入口で薄まります。
- 2026-03-14 時点の `V8` は抽象度が高く、`LLM/模倣との区別` を述べながら、実際には何を baseline として並べるべきかが十分に固定されていませんでした。
- さらに `先行研究マップ` と `参考文献 E` は、generic LLM 論文を含む古い束ね方のままで、brain-to-text / speech BCI の一次文献ベースの読み方に追いついていませんでした。

## 主要な批判点

### 1. `V8` は「模倣との区別」を抽象的に述べるだけで、一次文献が示す証拠階層を分けていませんでした

- 問題:
  - 旧版は「介入応答・閉ループ・内部状態の整合が必要」と書いていましたが、非侵襲 semantic decode、非侵襲 word / speech decode、侵襲 streaming speech BCI が別々の達成であることが見えませんでした。
  - そのため、読者が `brain-to-text` の前進をそのまま `WBE` や `emulation` の前進として読める余地が残っていました。
- 根拠:
  - Tang et al. (2023) は、non-invasive fMRI から連続言語の意味再構成を示しつつ、subject cooperation が学習時にも適用時にも必要であると示しました。
  - D&eacute;fossez et al. (2023) は、MEG/EEG から speech perception の decode を示しましたが、healthy volunteers の受動聴取課題であり、speech production や open-ended generation ではありません。
  - d'Ascoli et al. (2025) は、MEG と reading task が EEG と listening より有利で、データ量が decode 性能を大きく左右すると示しました。
  - Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025) は、speech neuroprosthesis の性能上限を押し上げましたが、communication subsystem の局所的前進です。
- 修正:
  - `V8` を evidence gate として再設計し、`非侵襲 semantic / caption decoding`、`非侵襲 word / speech decoding`、`侵襲 streaming speech neuroprosthesis` を表で分離しました。
  - 各トラックに対して「今言えること」と「まだ言えないこと」を固定しました。

### 2. 言語事前分布の混入を監査する評価パックが Roadmap 側に不足していました

- 問題:
  - 旧版には `LM-only`、`no-LM`、`time-shuffle`、`trial-shuffle`、candidate set size、cross-day、latency、abstention、recalibration burden といった監査項目が明示されていませんでした。
  - そのため、language prior の寄与と neural contribution を分ける site rule が、長文ノート側にしか存在しない状態でした。
- 根拠:
  - Tang et al. (2023) は subject cooperation requirement を明示し、decode 成功が計測条件に強く依存することを示しました。
  - d'Ascoli et al. (2025) は device、task、training data amount が decode 性能を強く動かすことを示しました。
  - Littlejohn et al. (2025) は 80 ms increments の streaming synthesis を示し、Wairagkar et al. (2025) は instantaneous closed-loop audio feedback を示しました。ここでは accuracy だけでなく latency / silence / abstention が中心指標になります。
  - Wilson et al. (2025) は、long-term unsupervised recalibration を別問題として切り出し、drift を無視した fixed-decoder 主張が危ういことを示しました。
- 修正:
  - `V8` に `最低限ほしい評価パック` を追加し、neural contribution、generalization boundary、streaming metrics、claim downgrade rule を明文化しました。

### 3. `先行研究マップ` と `参考文献 E` が、公開サイトの現在の厳密さに比べて弱い文献束のままでした

- 問題:
  - 旧版は `Ji et al. (2023)` や `Manakul et al. (2023)` のような generic LLM reliability 論文を、brain decoding の主要先行研究と同列に置いていました。
  - 一方で、D&eacute;fossez et al. (2023)、d'Ascoli et al. (2025)、Littlejohn et al. (2025)、Wairagkar et al. (2025)、Wilson et al. (2025) など、今回の技術論点を直接支える一次文献が抜けていました。
  - また d'Ascoli らの 2025 論文は、公開サイト内の別監査メモでは DOI が `10.1038/s41467-025-56165-8` と記録されていましたが、Nature Communications の正式記事は `10.1038/s41467-025-65499-0` でした。
- 修正:
  - `先行研究マップ` のデコーディング行を、`Huth / Tang / D&eacute;fossez / Horikawa / d'Ascoli / Willett / Littlejohn / Wairagkar / Wilson` の一次文献セットへ更新しました。
  - `参考文献 E` を、generic LLM 論文ではなく、brain-to-text / speech BCI の primary papers と DOI へ全面差し替えました。
  - d'Ascoli らの DOI は `10.1038/s41467-025-65499-0` で統一しました。

## 今回実行した変更

- `tech_roadmap.md`
  - `V8` を abstract な模倣論から、brain-to-text の evidence gate へ改稿
  - `最低限ほしい評価パック` を追加
  - `先行研究マップ` のデコーディング行を一次文献ベースへ更新
  - `参考文献 E` を primary papers + DOI へ全面更新

## 外部依存で保留

- `LM-only / shuffle / OOD / cross-day / latency / abstention / recalibration` を同一 schema で比較できる公開 benchmark の整備
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 公開可能な brain-to-text / speech BCI ログ、または同等の再現用ベンチ
  - 完了条件: communication route の前進と WBE 主張を同じ評価表で切り分けられること

## 参考文献

- Huth AG, de Heer WA, Griffiths TL, Theunissen FE, Gallant JL. Natural speech reveals the semantic maps that tile human cerebral cortex. Nature. 2016.
  - https://doi.org/10.1038/nature17637
- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- D&eacute;fossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. Nat Mach Intell. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- Horikawa T. Mind captioning: Evolving descriptive text of mental content from human brain activity. Sci Adv. 2025.
  - https://doi.org/10.1126/sciadv.adw1464
- d'Ascoli S, Ferrante O, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain&ndash;computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
