# Site Deepening Audit (2026-03-14, FAQ / Glossary / Decoding Boundary)

## 対象

- 主対象: `faq.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-14 の既存監査で、`verification`、`tech_roadmap`、`wbe_101`、`perspective`、各種 wiki はかなり深く更新されていました。
- 一方で、公開サイトの入口層である `faq.md` と用語層である `glossary.md` は、2025 年までの non-invasive language decoding と ESI 直接妥当化の進展を十分に反映していませんでした。
- 入口層が弱いままだと、深いページで丁寧に分けた `decode` / `identifiability` / `direct validation` の境界が、最初の数ページで再び混ざります。

## 主要な批判点

### 1. `faq.md` の Q1 は、fMRI ベースの semantic reconstruction と EEG の話を近接させることで、cross-modal のすり替えを起こしやすかった

- 問題:
  - 既存の Q1 は「EEGで“思考”は読める？」という問いに対し、方向性としては正しかった一方、どの成果が scalp EEG の話で、どの成果が fMRI や侵襲系の話かを本文中で十分に分けていませんでした。
  - そのため、Tang et al. (2023) の non-invasive semantic reconstruction を、そのまま scalp EEG の一般到達点として誤読する余地が残っていました。
  - 2025 年の d'Ascoli et al. は large-scale M/EEG から単語 decoding の前進を示しましたが、既知の word onset、reading/listening 課題、MEG 優位、学習データ量依存という条件が明確にあります。ここを入口で固定しないと、「任意の思考が自由に読める」という読み替えが起きます。
- 修正:
  - Q1 を `限定条件つき decoding` と `内部状態の同定` に明示的に分離しました。
  - Tang (2023) は fMRI 系、d'Ascoli (2025) は M/EEG の constrained decoding 系と書き分けました。

### 2. `faq.md` は、brain-to-text の見た目の強さと ground truth の強さを分ける入口が不足していた

- 問題:
  - 現行 FAQ には、「どのデモでも最低限どこを見るべきか」を固定する短いチェックリストがありませんでした。
  - その結果、侵襲 speech neuroprosthesis の高性能値が、scalp EEG や一般的 non-invasive BCI にそのまま継承できるかのように読まれる余地がありました。
  - Metzger et al. (2023) と Card et al. (2024) は確かに大きな前進ですが、いずれも cortical surface electrodes または intracortical arrays を用いた侵襲系です。
- 修正:
  - 新設した Q1b に、`計測法 / 課題 / prior / 検証 / 信頼度運用` の 5 点チェックを追加しました。
  - Q5b にも、閉ループ性能を読むときは侵襲性・再校正時間・日跨ぎ安定性を分けるべきだと追記しました。

### 3. `glossary.md` は、2026-03 時点で最も危ない用語対をまだ持っていなかった

- 問題:
  - 既存 glossary は `decode / emulate`、`相関 / 因果` までは置けていましたが、`observability / identifiability`、`モデル適合 / direct validation`、`brain signal / language prior` が欠落していました。
  - これは site-wide で最も危険な欠落です。なぜなら、decoder が文字列を出した瞬間に「内部状態が分かった」と読まれ、source imaging が source を出した瞬間に「十分に localize できた」と読まれるからです。
  - Unnwongse et al. (2023) の direct validation では mean localization error が 10.3-26.0 mm に達し、Hao et al. (2025) でも 14.07 ± 4.62 mm 対 17.38 ± 4.16 mm の誤差が残り、source depth と spike power に依存しました。これは `detectable` と `uniquely identified` が別だと示す十分な根拠です。
- 修正:
  - `よく混同する言葉` に 3 組の用語対を追加しました。
  - `モデル化` 節に `観測可能性 / 同定可能性 / 直接妥当化 / Language Prior / 校正 / 棄権` を追加しました。

## 今回実行した変更

- `faq.md`
  - Q1 を quantitative な ceiling 付きの説明へ更新
  - `Q1の読み替え禁止` 注記を追加
  - 新設 Q1b で brain-to-text 読解の 5 点チェックを追加
  - Q5b に侵襲系 closed-loop 実績と non-invasive への読み替え禁止を追加
  - 参考文献に d'Ascoli (2025)、Unnwongse (2023)、Hao (2025)、Metzger (2023)、Card (2024)、Guo (2017)、Geifman & El-Yaniv (2017) を追加
- `glossary.md`
  - `observability / identifiability` ほか混同しやすい用語対を追加
  - `モデル化` 節に `直接妥当化`、`Language Prior`、`校正`、`棄権` を追加
  - `2026-03 の補足` 注記で、non-invasive decoding の読み方を固定
  - 参考文献に Seeber (2019)、Unnwongse (2023)、Hao (2025)、Tang (2023)、d'Ascoli (2025)、Pernet (2020)、Guo (2017)、Geifman & El-Yaniv (2017) を追加

## 外部依存で保留

- public benchmarks を用いた site-wide `language prior` 表示の統一
  - 担当者: AI / maintainer
  - 前提条件: brain-to-text / source imaging 関連ページすべての prior 表示棚卸し
  - 完了条件: public page 上の decoder 系主張すべてに、モダリティ・課題・prior・validation の4要素が明示されること

## 参考文献

- Tang J, LeBel A, Jain S, Huth AG. Semantic reconstruction of continuous language from non-invasive brain recordings. Nat Neurosci. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nat Commun. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, Achakulvisut T, Wu JY, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Metzger SL, Littlejohn KT, Silva AB, et al. A high-performance neuroprosthesis for speech decoding and avatar control. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06443-4
- Card NS, Glasser MF, et al. An accurate and rapidly calibrating speech neuroprosthesis. N Engl J Med. 2024.
  - https://doi.org/10.1056/NEJMoa2314132
- Pernet CR, et al. Best practices in data analysis and sharing in neuroimaging using MEEG. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Guo C, Pleiss G, Sun Y, Weinberger KQ. On Calibration of Modern Neural Networks. ICML/PMLR. 2017.
  - https://proceedings.mlr.press/v70/guo17a.html
- Geifman Y, El-Yaniv R. Selective Classification for Deep Neural Networks. NeurIPS. 2017.
  - https://papers.neurips.cc/paper/7073-selective-classification-for-deep-neural-networks
