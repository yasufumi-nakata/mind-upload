# Site Deepening Audit (2026-03-19, EEG Connectivity Claim Ceiling)

## 対象

- 主対象: `perspective.md`
- 副対象: `eeg_101.md`

## 今回の選定理由

- 公開サイトの 2026-03 時点の主流方針は、`観測`、`推定`、`因果` を分離し、modality ごとの claim ceiling を厳密に書く方向でかなり整理できております。
- しかし `perspective.md` の proposal 47 には、`ASR + ZapLine` を `wPLI / STE` の volume conduction / directionality 問題へほぼ直結させて読める文面が残っていました。
- この残存表現は技術・自然科学の観点で弱点です。なぜなら、artifact suppression、line-noise suppression、source leakage、directional identifiability、causal validity は同じ誤差項ではないからです。

## 根拠付き批判

### 1. ASR と ZapLine は cleanup 手法であって、connectivity identifiability 手法ではありませんでした

- 問題:
  - 旧 `perspective.md` proposal 47 は、`Combining automatic ASR removal with ZapLine's line noise suppression to address volume conduction and directionality issues in wPLI/STE` と書いていました。
  - しかし ASR と ZapLine が主に扱うのは artifact / line noise であり、source mixing や causal direction の識別そのものではありません。
- 根拠:
  - Chang et al. (2018) は ASR を `automatic EEG artifact removal` として評価しています。
  - de Cheveigné (2020) は ZapLine を `power line artifacts` の除去法として提示しています。
- 批判:
  - したがって、cleanup を強くしたことをもって `volume conduction` や `directionality` が解けたかのように書くのは、誤差項のすり替えです。

### 2. wPLI は safer metric ではあっても leak-proof metric ではありませんでした

- 問題:
  - 旧文面だと、読者が `wPLI を使えば volume conduction 問題はかなり処理済み` と読める余地がありました。
- 根拠:
  - Vinck et al. (2011) は wPLI を、volume-conduction・noise・sample-size bias に対して PLI より改善した phase-lag metric として導入しました。
  - しかし Haufe et al. (2013) は、realistic volume conduction 下では sensor-space connectivity の神経生理学的解釈が severe に制限され、Granger-causal measures は source reconstruction 後でも spurious connectivity を出しうると示しました。
  - Palva et al. (2018) は、zero-lag を無視する leakage-insensitive measures でも source space で `ghost interactions` が生じうると示しました。
  - Miljevic et al. (2025) は、sensor-space EEG functional connectivity 推定が rereferencing、epoch length、epoch number、metric choice に強く依存すると示しました。
- 批判:
  - したがって安全な書き方は、`wPLI は一部の zero-lag mixing に対してより保守的` であって、`inter-areal coupling の leak-proof readout` ではない、です。

### 3. STE は directed-dependence estimator ではあっても、observational EEG からの causal proof ではありませんでした

- 問題:
  - 旧文面は `STE is effective for estimating directional information flow` とだけ書いており、観測データだけでの causal overread を十分に止めていませんでした。
- 根拠:
  - Staniek & Lehnertz (2008) は Symbolic Transfer Entropy を提案しましたが、それ自体は observational EEG を causal ground truth 化する論文ではありません。
  - Ye et al. (2020) は、`the validity of the derived connectivity has not yet been fully determined`、`it is generally difficult to identify causality in the usual experimental framework based on observations alone` と明示した上で、TMS perturbation を使って STE を評価しました。
- 批判:
  - つまり STE の安全な読解は `directed statistical dependence under assumptions` であり、因果方向の確定には perturbation / external validation が別途必要です。

## 今回実行した変更

- `perspective.md`
  - proposal 47 の題名を `Enhanced preprocessing reproducibility and connectivity ceilings` に変更しました。
  - ASR / ZapLine の役割を cleanup に限定し、volume conduction・source leakage・directional identifiability は別監査であることを明文化しました。
  - wPLI の safe reading、STE の safe reading、recent benchmarking に基づく pipeline-dependence を追記しました。
  - Haufe (2013), Palva (2018), Ye (2020), Miljevic (2025) を参考文献へ追加しました。
- `eeg_101.md`
  - `page_highlights` と `known_points` に、artifact suppression が leakage / causality を自動解決しないことを追加しました。
  - preprocessing acceptance gate 直下に `Connectivity metrics are not leak-proof or causal just by name` という note を追加しました。
  - サイドバー参考文献へ Vinck (2011), Haufe (2013), Palva (2018), Ye (2020), Miljevic (2025) を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文と参考文献導線の修正で完結しております。

## 参考文献

1. Chang C-Y, Hsu S-H, Pion-Tonachini L, Jung T-P. Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. *Proc IEEE EMBC*. 2018.
   - https://doi.org/10.1109/EMBC.2018.8512547
2. de Cheveigné A. ZapLine: A simple and effective method to remove power line artifacts. *NeuroImage*. 2020;207:116356.
   - https://doi.org/10.1016/j.neuroimage.2019.116356
3. Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CMA. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage*. 2011;55(4):1548-1565.
   - https://doi.org/10.1016/j.neuroimage.2011.01.055
4. Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. *NeuroImage*. 2013;64:120-133.
   - https://doi.org/10.1016/j.neuroimage.2012.09.036
5. Palva JM, Wang SH, Palva S, Zhigalov A, Monto S, Brookes MJ, Schoffelen J-M, Jerbi K. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018;173:632-643.
   - https://doi.org/10.1016/j.neuroimage.2018.02.032
6. Staniek M, Lehnertz K. Symbolic Transfer Entropy. *Physical Review Letters*. 2008;100(15):158101.
   - https://doi.org/10.1103/PhysRevLett.100.158101
7. Ye S, Kitajo K, Kitano K. Information-theoretic approach to detect directional information flow in EEG signals induced by TMS. *Neuroscience Research*. 2020;154:87-96.
   - https://doi.org/10.1016/j.neures.2019.09.003
8. Miljevic A, Murphy OW, Fitzgerald PB, Bailey NW. Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. *Clinical Neurophysiology*. 2025;174:73-83.
   - https://doi.org/10.1016/j.clinph.2025.03.043
