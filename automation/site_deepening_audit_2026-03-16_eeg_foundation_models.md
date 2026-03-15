# Site Deepening Audit (2026-03-16, EEG Foundation Models / Self-Supervised Pretraining)

## 対象

- 主対象: `eeg_101.md`
- 主対象: `datasets.md`
- 副対象: `wiki/eeg-foundation-models.md`
- 関連対象: `wiki/baselines-prereg-and-model-cards.md`
- 関連対象: `wiki/index.md`

## 今回の選定理由

- 2026-03-16 時点で、サイトは QC、split、multimodal、closed-loop、maintenance-state をかなり深く整理できていました。
- その一方で、`EEG foundation model / self-supervised pretraining` の読み方だけが公開導線で抜けていました。
- これは技術・自然科学の観点で弱点です。なぜなら、最近の大規模事前学習は実際に前進している一方で、その論文群自身が `electrode mismatch`、`sample-rate 差`、`missing channel`、`low SNR`、`inter-subject variability` を主要課題として置いており、そこを見ずに score だけ読むと evidence gate が壊れるからです。

## 主要な批判点

### 1. 旧サイトは foundation model の前進を、既存の generalization gate へ接続できていませんでした

- 問題:
  - `eeg_101.md` と `datasets.md` は within / cross-session / cross-subject / drift の読み分けをかなり整備していました。
  - しかし、LaBraM、BIOT、EEGPT、BENDR のような foundation / self-supervised 系をどこへ位置づけるかが明示されていませんでした。
  - そのため、読者が `大規模 pretraining = generalization solved`、`大規模 pretraining = WBE に一段近づいた` と誤読しうる余地が残っていました。
- 根拠:
  - Kostas et al. (2021) は breadth を示しつつ、downstream applicability remains to be seen と述べています。
  - Wang et al. (2023) は sampling rate、channel、duration、missing segment の mismatch 自体を cross-data 学習の中心問題として置いています。
  - Jiang et al. (2024) と Wang et al. (2024) は、foundation model の abstract 自体で electrode mismatch、varied task design、low SNR、inter-subject variability を主要課題として挙げています。
- 修正:
  - `eeg_101.md` に `EEG foundation model は一般化ゲートを飛び越えません` 節を追加しました。
  - foundation / self-supervised 結果も `observability / identifiability / deployability` の 3 gate をそのまま通す、と site rule を明記しました。

### 2. 旧 Datasets ページは、foundation model 時代の dataset 監査項目をまだ固定していませんでした

- 問題:
  - 旧 `datasets.md` は dataset card と event fidelity をかなり明確にしていました。
  - しかし、pretraining corpus 自体を dataset としてどう監査するかが未定義でした。
  - そのため、pretraining corpus overlap、channel harmonization、adaptation regime を hidden にしたまま score 比較する余地が残っていました。
- 根拠:
  - BIOT は heterogeneous biosignal に対して resampling、normalization、tokenization、missing data handling を前面に出しています。
  - LaBraM は unequal length、electrode mismatch、varied task design、low SNR を foundation model 側の課題として明示しています。
  - EEGPT は low SNR、inter-subject variability、channel mismatch を主要課題とし、linear probing を使った downstream 評価を報告しています。
- 修正:
  - `datasets.md` に `foundation / self-supervised EEG model を使うときの追加監査` 節を追加しました。
  - `Pretraining Card` を定義し、corpus identity / overlap audit、harmonization、objective / adaptation regime、evaluation family、stopped claim を最低限の提出項目へ昇格しました。

### 3. 旧サイトには、この論点を支える学習用 wiki がありませんでした

- 問題:
  - foundation model の読み方を、EEG 入口ページや dataset 実務ページだけで完結させると、説明が過密になります。
  - しかし wiki 側にも対応ページが無かったため、公開ページから deeper explanation へ飛べませんでした。
- 修正:
  - `wiki/eeg-foundation-models.md` を新設しました。
  - 一次文献の境界、5 つの gate、Pretraining Card、本サイトでの運用ルールを 1 ページに集約しました。
  - `wiki/index.md` に導線を追加し、`wiki/baselines-prereg-and-model-cards.md` に Pretraining Card を接続しました。

### 4. 旧 model-card 運用は multimodal には対応済みでしたが、pretraining 特有の追加カードがありませんでした

- 問題:
  - `wiki/baselines-prereg-and-model-cards.md` は Observability Budget と Fusion Card をかなり明確に説明していました。
  - その一方で、foundation / self-supervised 結果に何を追加提出すべきかが空欄でした。
- 修正:
  - `wiki/baselines-prereg-and-model-cards.md` に Pretraining Card を追記しました。
  - foundation / self-supervised EEG 結果では、通常の model card に加えて Pretraining Card が必要だと明記しました。

## 今回実行した変更

- `eeg_101.md`
  - foundation model の boundary と site rule を追加
  - `Wiki: EEG foundation model と事前学習` への導線を追加
  - 参考文献リンクに BENDR / BIOT / LaBraM / EEGPT / CDRC を追加
- `datasets.md`
  - `last_updated` を 2026-03-16 に更新
  - `2.6) foundation / self-supervised EEG model を使うときの追加監査` を追加
  - `Pretraining Card` を定義
  - 参考文献に foundation / self-supervised 系を追加
- `wiki/eeg-foundation-models.md`
  - 新規作成
  - 一次文献の境界、5 つの gate、Pretraining Card、site rule を整理
- `wiki/baselines-prereg-and-model-cards.md`
  - Pretraining Card を model-card 運用へ接続
- `wiki/index.md`
  - 新規 wiki への導線を追加

## 外部依存で保留

- なし
  - 今回の変更はすべてこのリポジトリ内で完結しています。

## 参考文献

- Kostas D, Aroca-Ouellette S, Rudzicz F. BENDR: Using Transformers and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. *Front Hum Neurosci*. 2021;15:653659.
  - https://doi.org/10.3389/fnhum.2021.653659
- Wang H, Lu C, Xie B, et al. BIOT: Biosignal Transformer for Cross-data Learning in the Wild. *NeurIPS*. 2023.
  - https://papers.nips.cc/paper_files/paper/2023/file/f6b30f3e2dd9cb53bbf2024402d02295-Paper-Conference.pdf
- Jiang W-B, Zhao L, Lu B-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. *ICLR*. 2024.
  - https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html
- Wang G, Liu W, He Y, Xu C, Ma L, Li H. EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals. *NeurIPS*. 2024.
  - https://neurips.cc/virtual/2024/poster/93793
- Zhang M, Zhao S, Xie L, Liu T, Yao D, Yin E. Self-Supervised Contrastive Pre-Training for EEG-Based Recognition via Cross Device Representation Consistency. *IEEE Trans Biomed Eng*. 2025.
  - https://doi.org/10.1109/TBME.2025.3613730
