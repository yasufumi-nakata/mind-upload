# Site Deepening Audit (2026-03-14, Uncertainty / Calibration / Abstention)

## 対象

- 主対象: `wiki/uncertainty-confidence-and-abstention.md`

## 今回の選定理由

- このページは `eeg_101.md`、`verification.md`、`wiki/observation-to-estimation.md`、`wiki/closed-loop-latency-jitter-and-safety-stops.md` から参照される補助ページであり、サイト全体の主張強度を下支えします。
- しかし 2026-03-14 時点の旧版は、`点推定より区間が大事` という一般論には触れていた一方で、`confidence ≠ calibration`、`棄権は coverage との交換条件`、`source imaging / EEG分類 / online BCI で必要な不確実性会計が違う` という実務上の核心が固定されていませんでした。
- この弱さは公開サイト全体の読み方を甘くします。なぜなら、source imaging の事後幅、EEG 分類の校正誤差、closed-loop BCI の再較正負荷は、同じ「不確実性」という語でまとめられないにもかかわらず、旧版ではほぼ同列に読めてしまったからです。

## 主要な批判点

### 1. 旧版は `confidence` と `calibration` を分けていませんでした

- 問題:
  - 旧版は `信頼区間 / 信用区間` の初歩説明としては有用でしたが、classification score や posterior の 1 数字を、どこまで実用上の信頼度として読めるかを固定していませんでした。
  - そのため、softmax や decoder score を、そのまま `当たる確率` のように誤読する余地が残っていました。
- 根拠:
  - Duan et al. (2023) は motor imagery EEG decoding で uncertainty estimation と confidence calibration を分けて扱っています。
  - Hu et al. (2024) と Shafiezadeh et al. (2024) も、EEG seizure classification / forecasting で calibration 改善そのものを評価対象にしています。
- 修正:
  - `confidence、区間、校正、棄権を混ぜない` 節を新設し、点推定、区間、confidence、校正、棄権の役割差を表で固定しました。
  - `softmax や posterior をそのまま校正済み確率とみなさない` という site rule を明記しました。

### 2. 旧版の `棄権` は安全論に寄りすぎており、coverage との交換が見えませんでした

- 問題:
  - 旧版は `自信が低いときに無理に答えない方が安全` という説明で止まっていました。
  - しかし実務では、棄権は `どれだけ誤りを減らしたか` と同時に `どれだけ出力を諦めたか` を伴います。
- 根拠:
  - Ganeshkumar et al. (2017) は EEG motor imagery BCI に reject option を入れることで false prediction rate を下げていますが、同時に coverage 低下を伴います。
  - Segal et al. (2023) は seizure prediction で risk-controlling prediction calibration により false alarm rate を抑えています。これは、安全論ではなく threshold と誤警報コストの設計問題です。
- 修正:
  - `棄権は「安全そうだから」ではなく、coverage と risk の公開` という節に差し替えました。
  - `accuracy だけ` でも `棄権率だけ` でもなく、coverage-risk curve を一緒に出すことを site rule に入れました。

### 3. 旧版は source imaging、EEG分類、closed-loop BCI を同じ不確実性概念で読ませていました

- 問題:
  - source imaging の不確実性は頭部幾何、導電率、solver family、外部妥当化に強く依存します。
  - 一方で EEG 分類は subject shift や calibration error、online BCI は drift や recalibration burden が支配します。
  - 旧版はこの差を十分に分離していませんでした。
- 根拠:
  - Vorwerk et al. (2019)、Rimpiläinen et al. (2019)、Feng et al. (2025) は source imaging 側で、頭部モデルや conductivity uncertainty を本体として扱っています。
  - Wilson et al. (2025) は long-term intracortical BCI の実用性を、再較正負荷込みで示しています。
  - Wairagkar et al. (2025) は low-latency voice neuroprosthesis でも non-speech では silence を返す設計を前提にしています。
- 修正:
  - `課題ごとに公開すべき指標を変えます` 節を新設し、source imaging、offline EEG分類、希少イベント予測、online BCI ごとに必要指標を分けました。
  - `不確実性は4つの層で生まれる` として、観測ノイズ、モデル・幾何、分布ずれ、運用ドリフトを切り分けました。

### 4. 旧版は一次文献ベースのページとしては根拠が薄すぎました

- 問題:
  - 旧版に参考文献節がなく、読者が「この整理は何に支えられているのか」を追いにくい構造でした。
- 修正:
  - source imaging、EEG calibration、seizure forecasting、reject option、online BCI recalibration を直接扱う一次文献を 10 本追加しました。

## 今回実行した変更

- `wiki/uncertainty-confidence-and-abstention.md`
  - front matter を技術・自然科学中心へ更新
  - `4つの監査ゲート`、`confidence / calibration / abstention の役割差`、`課題別の必要指標`、`一次文献が示す現実`、`site rule`、`参考文献` を新設
  - タイトルを `不確実性・信頼区間・棄権` から `不確実性・校正・棄権` へ更新

## 外部依存で保留

- site-wide での calibration metric 統一
  - 担当者: AI / maintainer
  - 前提条件: `ECE / Brier / NLL / interval coverage / coverage-risk curve` のうち、課題別の標準提出物を決めること
  - 完了条件: `verification.md` と関連 wiki 全体で、L0 / L1 / L3 ごとの標準指標が揃うこと
- source imaging 系ページでの citation consistency 監査
  - 担当者: AI / maintainer
  - 前提条件: source imaging 関連ページの reference 表記を棚卸しすること
  - 完了条件: author 表記・DOI・年の不整合が site-wide で解消されること

## 参考文献

- Vorwerk J, Aydin U, Wolters CH, Butson CR. Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. Front Neurosci. 2019.
  - https://doi.org/10.3389/fnins.2019.00531
- Rimpiläinen I, Solis-Lemus JA, Särkkä S. Improved EEG source localization with Bayesian uncertainty modelling of unknown skull conductivity. NeuroImage. 2019.
  - https://doi.org/10.1016/j.neuroimage.2018.11.058
- Feng Z, Guan C, Sun Y. Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. IEEE Trans Med Imaging. 2025.
  - https://doi.org/10.1109/TMI.2025.3642620
- Duan T, Wang Z, Liu S, Yin Y, Srihari SN. UNCER: A framework for uncertainty estimation and reduction in neural decoding of EEG signals. Neurocomputing. 2023.
  - https://doi.org/10.1016/j.neucom.2023.03.071
- Hu J, Ur Rahman MM, Al-Naffouri T, Laleg-Kirati T-M. Uncertainty Estimation and Model Calibration in EEG Signal Classification for Epileptic Seizures Detection. EMBC. 2024.
  - https://doi.org/10.1109/EMBC53108.2024.10782858
- Shafiezadeh S, Duma GM, Mento G, et al. Calibrating Deep Learning Classifiers for Patient-Independent Electroencephalogram Seizure Forecasting. Sensors. 2024.
  - https://doi.org/10.3390/s24092863
- Segal G, Keidar N, Lotan RM, et al. Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. Front Neurosci. 2023.
  - https://doi.org/10.3389/fnins.2023.1184990
- Ganeshkumar P, Maheswari U, Vasant P. Reject Option to Reduce False Prediction Rates for EEG-Motor Imagery Based BCI. ICACCI. 2017.
  - https://doi.org/10.1109/ICACCI.2017.8125908
- Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
