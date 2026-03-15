# Site Deepening Audit (2026-03-15, Decode / Emulate Evidence Gate)

## 対象

- 主対象: `wiki/decode-vs-emulate.md`
- 副対象: `faq.md`

## 今回の選定理由

- `Wiki: Decode と Emulate` はサイトの核となる境界ページですが、2026-03-15 時点では 2023 年中心の例示で止まっており、2025 年の一次文献が押し上げた `open-vocabulary non-invasive decode`、`streaming / voice-synthesis neuroprosthesis`、`long-term recalibration burden`、`connectome-constrained prediction` を site rule に落とし切れていませんでした。
- これは技術・自然科学の観点で改善優先度が高いです。なぜなら、現状の strongest evidence は「decode がどこまで進んだか」「local subsystem の closed loop がどこまで進んだか」「connectome 制約でどこまで predictive gain が出るか」に分かれており、それらを一括で `emulation に近い` と読むと evidence gate が崩れるからです。

## 主要な批判点

### 1. 旧ページは 2025 年の decode frontier を取り込めておらず、非侵襲 decode の ceiling を古い粒度でしか止められていませんでした

- 問題:
  - 旧版は Tang (2023) を中心に non-invasive decode を説明していましたが、d'Ascoli et al. (2025) の 723 人規模 single-word decoding を踏まえた `open-vocabulary progress と boundary` を明示していませんでした。
  - そのため、読者が `単語 decode が進んだ` を `自由思考の一般的読解` や `内部状態 reconstruction` へ読み替えやすい構造が残っていました。
- 根拠:
  - Tang et al. (2023) は semantic reconstruction の大きな前進ですが、participant cooperation を必要とする participant-specific system です。
  - d'Ascoli et al. (2025) は open-vocabulary non-invasive word decoding の前進を示す一方、モダリティ、課題、データ量で性能が大きく変わることも示しました。
- 修正:
  - `wiki/decode-vs-emulate.md` に d'Ascoli (2025) を追加し、`language prior / candidate set / participant cooperation` を decode/emulate 境界の必須監査項目へ昇格しました。
  - `faq.md` の `brain-to-text` 節も、`LM-only / no-brain / shuffle baseline` を最低確認項目へ追加しました。

### 2. 旧ページは streaming speech neuroprosthesis を `高性能 decode` としか扱っておらず、deployment burden を十分に切り出せていませんでした

- 問題:
  - 旧版の `decode vs emulate` 境界は、offline accuracy と局所 closed loop を主に見ていました。
  - しかし 2025 年の strongest evidence は `どれだけ速いか` だけでなく、`tail latency`、`silence / abstention`、`recalibration burden`、`cross-day deployment` を別ログとして残すべきことを示しています。
- 根拠:
  - Littlejohn et al. (2025) は 80 ms ごとの streaming brain-to-voice を示しました。
  - Wairagkar et al. (2025) は 10 ms 未満の neural-to-voice synthesis と silence fallback を示しました。
  - Wilson et al. (2025) は long-term unsupervised recalibration を扱い、daily supervised recalibration 自体が実運用の壁であることを明示しました。
- 修正:
  - `wiki/decode-vs-emulate.md` の evidence ladder を更新し、speech neuroprosthesis を `communication subsystem の L2〜L3` と明示しました。
  - `5 つのゲート` に `閉ループと長期運用で安定か` を追加し、`P50/P95/P99 latency`、`silence / abstention`、`recalibration burden`、`recovery time` を必須ログへ加えました。
  - `faq.md` でも、within-session の速さと deployable closed loop を分けて読むよう改稿しました。

### 3. 旧ページは connectome-constrained model を `emulate に近い方向の基盤` と述べるに留まり、縮退の壁を 2025 年水準で具体化していませんでした

- 問題:
  - 旧版は MICrONS と Billeh を使って `digital twin に近い` 方向を示していましたが、connectome 制約を入れてもなぜ唯一解にならないかを、2025 年の一次文献で具体化できていませんでした。
- 根拠:
  - MICrONS Consortium et al. (2025) は same-brain function + connectomics の貴重な足場を与えました。
  - Beiran & Litwin-Kumar (2025) は connectome-constrained recurrent networks でも、unrecorded neurons や未測定 biophysical parameter が残ると teacher dynamics の回復が一意にならないことを示しました。
  - Prinz et al. (2004) は古典的に、似た network activity が異なる circuit parameter から出ることを示しています。
- 修正:
  - `wiki/decode-vs-emulate.md` に `connectome-constrained prediction → unique internal mechanism` を禁止する表を追加しました。
  - 併せて、`connectome-only baseline と augmentation 比較`、`family comparison`、`latent state 監査` を G5 として固定しました。

### 4. FAQ の短い答えが、最新の evidence gate を十分に圧縮できていませんでした

- 問題:
  - FAQ は入口として有用ですが、`brain-to-text のデモを見るとき` と `decode / emulate の違い` の答えは、2025 年の strongest evidence を読むには少し短すぎました。
- 修正:
  - `faq.md` の Q1b、Q2、Q5b を更新し、prior baseline、silence / abstention、recalibration burden、cross-day 劣化を短い形で追加しました。

## 今回実行した変更

- `wiki/decode-vs-emulate.md`
  - `last_updated` を 2026-03-15 に更新
  - 2025 年文献を反映して front matter を更新
  - evidence ladder を `d'Ascoli / Tang / Willett / Littlejohn / Wairagkar / Flesher / MICrONS / Beiran` ベースへ改稿
  - `2026-03 文献監査：ここで禁止する 3 つの読み替え` を追加
  - `decode を emulate と読み替える前の 5 つのゲート` へ更新
  - site rule を `prior 超過 / cross-day / intervention / deployment / state completeness` の 5 軸へ改めた
- `faq.md`
  - Q1b に `LM-only / no-brain / shuffle baseline`、`silence / abstention`、`長期運用` を追加
  - Q2 を、2025 年 decode / subsystem closed-loop を踏まえた読み替え禁止へ更新
  - Q5b を、Littlejohn / Wairagkar / Wilson ベースの long-term closed-loop 読みへ更新

## 外部依存で保留

- decode / emulate を横断する公開 benchmark の実データ整備
  - 担当者: AI / maintainer / 実験系 collaborators
  - 前提条件: `LM-only`、`no-brain`、`shuffle`、`OOD`、`cross-day`、`silence / abstention`、`recalibration burden`、`state-variable augmentation` を同一 schema で比較できる公開ログがあること
  - 完了条件: `見た目の出力が良い`、`communication subsystem が良い`、`state-complete emulate に近い` を同じ score に潰さず、別の評価軸として公開比較できること

## 参考文献

- Tang J, LeBel A, Jain S, et al. Semantic reconstruction of continuous language from non-invasive brain recordings. *Nat Neurosci*. 2023.
  - https://doi.org/10.1038/s41593-023-01304-9
- d'Ascoli S, Bel C, Rapin J, et al. Towards decoding individual words from non-invasive brain recordings. *Nat Commun*. 2025.
  - https://doi.org/10.1038/s41467-025-65499-0
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. *Nature*. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nat Biomed Eng*. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. *Science*. 2021.
  - https://doi.org/10.1126/science.abd0380
- MICrONS Consortium, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
  - https://doi.org/10.1038/s41586-025-08790-w
- Beiran M, Litwin-Kumar A. Prediction of neural activity in connectome-constrained recurrent networks. *Nat Neurosci*. 2025.
  - https://doi.org/10.1038/s41593-025-02080-4
- Billeh YN, Cai B, Gratiy SL, et al. Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex. *Neuron*. 2020.
  - https://doi.org/10.1016/j.neuron.2020.01.040
- Prinz AA, Bucher D, Marder E. Similar network activity from disparate circuit parameters. *Nat Neurosci*. 2004.
  - https://doi.org/10.1038/nn1352
