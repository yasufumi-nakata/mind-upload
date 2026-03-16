# Site Deepening Audit (2026-03-16, Neural Contribution Card / Brain-to-Text Evidence Separation)

## 対象

- 主対象: `verification.md`
- 副対象: `index.md`
- 副対象: `faq.md`
- 副対象: `glossary.md`

## 今回の選定理由

- 2026-03-16 時点で、公開サイトは `Observability Budget`、`Fusion Card`、`Temporal Validity Card`、`Calibration & Abstention Card`、`Benchmark Governance Card`、`Intervention Card` をかなり整理できていました。
- しかし、`brain-to-text / speech decode の出力のうち何が本当に脳由来で、何が task constraint・language prior・prompt・candidate set・decoder scaffold から来たか` は、まだ site-wide の提出物として固定できていませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、同じ「文字列が出た」「音声が出た」でも、subject-specific calibration、LM-only baseline、beam search、prompt、vocoder、candidate pruning、online fallback の露出条件が違えば、証拠の意味がまったく変わるからです。

## 主要な批判点

### 1. 旧サイトは language prior の危険を narrative では説明していましたが、Verification Commons の標準提出物には落とせていませんでした

- 問題:
  - `faq.md`、`perspective.md`、`wiki/decode-vs-emulate.md` では、language prior と neural contribution を分ける必要性を説明していました。
  - しかし `verification.md` には、それを `Model Card` や `Calibration & Abstention Card` のように別提出物として固定する節がありませんでした。
- 根拠:
  - Tang et al. (2023) は non-invasive semantic reconstruction を示しましたが、decoder の学習と適用の双方で参加者の協力が必要でした。
  - Défossez et al. (2023) は non-invasive speech decoding を示しましたが、self-supervised speech representation と retrieval setting に支えられていました。
  - d'Ascoli et al. (2025) は 723 人規模の単語デコードを示しましたが、surrounding context、モダリティ、課題が性能を強く動かしました。
  - Wang et al. (2025) は fMRI 由来表現を prompt とともに LLM へ入力して text continuation を生成しました。
  - Littlejohn et al. (2025) と Wairagkar et al. (2025) は streaming / voice synthesis を大きく前進させましたが、acoustic model、beam search、vocoder、silence fallback、participant-specific calibration が結果の意味を左右しました。
- 修正:
  - `verification.md` に `Neural Contribution Card` 節を追加しました。
  - `Leaderboard & Model Cards` の説明に同 card を統合し、`Verification Commons` の提出物仕様へ昇格しました。

### 2. 旧サイトは decode の成功を「何が脳由来か」で比較する共通欄が不足していました

- 問題:
  - 旧版では `LM-only`、`no-brain`、`shuffle` の必要性は散発的に言及されていました。
  - しかし、各研究で最低限何を開示すべきかが card 化されていなかったため、比較時に毎回読み手が独自に監査する必要がありました。
- 根拠:
  - Tang et al. (2023) は participant cooperation を必要としました。
  - d'Ascoli et al. (2025) は surrounding context を活用し、MEG / reading が EEG / listening より有利でした。
  - Littlejohn et al. (2025) は HuBERT、byte-pair encoding model、beam search を使い、electrode shuffle による chance control を示しました。
  - Wairagkar et al. (2025) は open-ended vocalization を押し上げましたが、silence fallback と participant-specific synthesis が重要でした。
- 修正:
  - `Neural Contribution Card` に `target / task regime`、`prior scaffold`、`brain-versus-prior baselines`、`subject adaptation / cooperation`、`generalization surface`、`online semantics / fallback`、`claim ceiling` を定義しました。

### 3. 既存カードとの責任分界が弱く、Pretraining / Calibration / Temporal Validity と混ざる余地がありました

- 問題:
  - 現状でも `Pretraining Card`、`Calibration & Abstention Card`、`Temporal Validity Card` はありましたが、decode 系ではそれぞれが何を固定し、何を固定しないかが明示されていませんでした。
- 根拠:
  - Wilson et al. (2025) は長期運用で recalibration policy が中心問題になることを示しましたが、これは `何が脳由来か` とは別軸です。
  - d'Ascoli et al. (2025) や Wang et al. (2025) が示す context / prompt / task scaffold の寄与は、calibration や temporal drift とは別軸です。
- 修正:
  - `verification.md` に `既存カードとの役割差` を追加しました。
  - `faq.md` と `index.md` に導線を加え、読者が `Neural Contribution Card` を独立カードとして参照できるようにしました。

### 4. 用語側に `Neural Contribution Card` が無く、入口読者が decode 系の提出物名を追いにくい状態でした

- 問題:
  - `glossary.md` には `Language Prior` はありましたが、card 名としての整理はありませんでした。
- 修正:
  - `glossary.md` に `Neural Contribution Card` を追加し、`brain signal / language prior / card` の 3 層を分けました。

## 今回実行した変更

- `verification.md`
  - `page_highlights` に `Neural Contribution Card` を追加
  - `Leaderboard & Model Cards` の説明へ統合
  - `2026-03 追補：brain-to-text / speech decode 結果には Neural Contribution Card を添付する` 節を新設
  - 参考文献へ Tang (2023)、Défossez (2023)、Wang (2025)、d'Ascoli (2025) を追加
- `index.md`
  - `page_highlights` に `Neural Contribution Card` を追加
  - 入口ノートとして `何が脳由来か先に見たいとき` 節を追加
- `faq.md`
  - `page_highlights` に `Neural Contribution Card` を追加
  - `Q. brain-to-text のデモを見るとき...` に Verification への導線を追加
- `glossary.md`
  - `last_updated` を 2026-03-16 に更新
  - `Neural Contribution Card` の用語項目を追加

## 外部依存で保留

- なし
  - 今回の変更は、このリポジトリ内の公開ルール整備と導線更新で完結しています。

## 参考文献

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- Défossez A, Caucheteux C, Rapin J, Kabeli O, King J-R. Decoding speech perception from non-invasive brain recordings. *Nat Mach Intell*. 2023.
  - https://doi.org/10.1038/s42256-023-00714-5
- Wang Z, Huo Y, Zhang M, Li Y, Ma Y, Qu D, Hu X. Generative language reconstruction from brain recordings. *Commun Biol*. 2025.
  - https://doi.org/10.1038/s42003-025-07751-z
- d'Ascoli S, Bel C, Rapin J, Dubarry A-S, King J-R, Ferrante O. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
