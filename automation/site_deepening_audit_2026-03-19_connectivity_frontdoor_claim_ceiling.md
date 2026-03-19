# Site Deepening Audit (2026-03-19, Connectivity Front Door Claim Ceiling)

## 対象

- 主対象: `faq.md`
- 副対象: `glossary.md`
- 副対象: `index.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、`DCM / effective connectivity`、`tractography connectome`、`thermodynamic claims`、`body / environment boundary` については、front door でもかなり明示的に guardrail を置けておりました。
- その一方で、`EEG / MEG functional connectivity`、`source-space connectivity`、`wPLI`、`STE`、`information flow` といった語は、主に `eeg_101.md` と `perspective.md` で厳密化されており、`FAQ` と `Glossary` の入口ではまだ独立した誤読防止ルールになっておりませんでした。
- この弱点は技術・自然科学の観点で重要です。なぜなら、front door で `connectivity graph が出た = communication channel を見た = causality にかなり近い` という連続的な誤読が残ると、せっかく site-wide に分離した `observation / estimation / intervention` の境界が再び崩れるからです。

## 根拠付き批判

### 1. `cleanup` と `leakage / causality` が front door で独立した誤差項になっていませんでした

- 問題:
  - `eeg_101.md` では、ASR / ZapLine のような cleanup と、volume conduction / source leakage / directional identifiability を別問題として明確に分離できておりました。
  - しかし `FAQ` の入口には、`EEG / MEG connectivity` そのものに対する独立の誤読防止項目がなく、読者が method 名や graph の見た目だけで一段強い claim に読める余地が残っておりました。
- 根拠:
  - Vinck et al. (2011) は wPLI を zero-lag mixing や noise に対してより保守的な指標として導入しましたが、 leak-proof connectivity meter とは述べておりません。
  - Haufe et al. (2013) は、sensor-space EEG connectivity の神経生理学的解釈が volume conduction により強く制限されることを simulation で示しました。
- 批判:
  - したがって `より良い preprocessing` や `より保守的な metric` を、そのまま `communication route を見た` へ引き上げるのは誤りです。
  - front door 側でも、`cleanup improved`、`dependence estimated`、`causality validated` を別レベルとして固定する必要がありました。

### 2. `source-space` や `information flow` という語が、なお causal overread を誘発しうる状態でした

- 問題:
  - 既存サイトは `DCM` の誤読は止めていましたが、`source-space connectivity` や `information flow` という語自体の overread は front door で明文化しておりませんでした。
- 根拠:
  - Palva et al. (2018) は、leakage-insensitive な source-space measures でも `ghost interactions` が生じうると示しました。
  - Ye et al. (2020) は STE を TMS で評価しており、観測データだけでは causality 同定が難しいことを前提にしております。
- 批判:
  - つまり `source-space` は `leakage-free` を意味せず、`information flow` も `causal proof` を意味しません。
  - DCM だけでなく、directed functional-connectivity family 全体に対しても、front door で claim ceiling を固定する必要がありました。

### 3. `Glossary` に functional connectivity / effective connectivity / causal wiring の境界が欠けていました

- 問題:
  - `Glossary` は `DCM` を持っていましたが、`functional connectivity` と `effective connectivity` の差、さらにそこから `causal wiring` へ飛ばない規律が term-level に固定されておりませんでした。
- 根拠:
  - Penny et al. (2004) と Rosa et al. (2012) は、effective-connectivity claim が candidate model space に依存することを示しております。
  - Miljevic et al. (2025) は、sensor-space connectivity estimate が rereferencing, epoch length, epoch number, metric choice に依存することを示しました。
- 批判:
  - 語の境界が曖昧なままだと、`functional connectivity < effective connectivity < causal truth` という滑らかな誤読が入口で生じます。
  - 用語集は単なる言い換え集ではなく、ここでは claim ceiling を固定する装置であるべきでした。

## 今回実行した変更

- `faq.md`
  - front matter と front-door note を `six` から `seven` technical guardrails へ更新しました。
  - 新規 Q&A `If a paper shows EEG / MEG connectivity or information flow...` を追加し、wPLI / source-space / STE / pipeline dependence の ceiling を明文化しました。
  - 参考文献に Vinck (2011), Haufe (2013), Palva (2018), Ye (2020), Miljevic (2025) を追加しました。
- `glossary.md`
  - `functional connectivity / effective connectivity / causal wiring` の easy-confusion row を追加しました。
  - modeling section に `Functional connectivity`, `Effective connectivity`, `wPLI`, `STE` を追加し、`DCM` 定義を route-card 前提へ改稿しました。
  - 参考文献に Penny (2004), Rosa (2012), Haufe (2013), Palva (2018), Ye (2020), Miljevic (2025) を追加しました。
- `index.md`
  - landing-page highlights / known points に connectivity claim ceiling を追加しました。
  - `If You Read EEG / MEG Connectivity As Communication Or Causality Too Quickly` の note-box を追加し、FAQ と EEG 101 への最短導線を張りました。

## 外部依存で保留

- なし
  - 今回の作業は公開本文・用語境界・参考文献導線の改稿で完結しております。

## 参考文献

1. Vinck M, Oostenveld R, van Wingerden M, Battaglia F, Pennartz CMA. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. *NeuroImage*. 2011;55(4):1548-1565.
   - https://doi.org/10.1016/j.neuroimage.2011.01.055
2. Haufe S, Nikulin VV, Müller K-R, Nolte G. A critical assessment of connectivity measures for EEG data: A simulation study. *NeuroImage*. 2013;64:120-133.
   - https://doi.org/10.1016/j.neuroimage.2012.09.036
3. Palva JM, Wang SH, Palva S, Zhigalov A, Monto S, Brookes MJ, Schoffelen J-M, Jerbi K. Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. *NeuroImage*. 2018;173:632-643.
   - https://doi.org/10.1016/j.neuroimage.2018.02.032
4. Staniek M, Lehnertz K. Symbolic Transfer Entropy. *Physical Review Letters*. 2008;100(15):158101.
   - https://doi.org/10.1103/PhysRevLett.100.158101
5. Ye S, Kitajo K, Kitano K. Information-theoretic approach to detect directional information flow in EEG signals induced by TMS. *Neuroscience Research*. 2020;154:87-96.
   - https://doi.org/10.1016/j.neures.2019.09.003
6. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004;22(3):1157-1172.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
7. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *Journal of Neuroscience Methods*. 2012;208(1):66-78.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
8. Miljevic A, Murphy OW, Fitzgerald PB, Bailey NW. Estimating sensor-space EEG connectivity PART 1: Identifying best performing methods for functional connectivity in simulated data. *Clinical Neurophysiology*. 2025;174:73-83.
   - https://doi.org/10.1016/j.clinph.2025.03.043
