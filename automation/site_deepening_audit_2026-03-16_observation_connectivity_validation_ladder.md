# Site Deepening Audit (2026-03-16, Observation-to-Estimation / connectivity validation ladder)

## 対象

- 主対象: `wiki/observation-to-estimation.md`
- 補助対象: `eeg_101.md`

## 今回の選定理由

- 2026-03-16 時点で、このサイトは source localization の限界、ghost interaction、directed metric の限界をかなり明確に書けていました。
- その一方で、`source localization の直接妥当化` と `source-space connectivity / directed connectivity の妥当化` の間にある **段差** が、まだ十分に構造化されていませんでした。
- この欠落は技術・自然科学の観点で優先度が高いです。なぜなら、いまの一次文献が示しているのは「局在がある程度合うこと」と「network claim が安定で causal であること」が別問題だという点だからです。

## 主要な批判点

### 1. 旧版は connectivity を localization より強い主張だと述べていましたが、妥当化の段差をまだ 1 枚に固定していませんでした

- 問題:
  - 旧 `wiki/observation-to-estimation.md` は `connectivity は localization の次の段` と正しく述べていました。
  - しかし、読者が Mikulan / Unnwongse / Hao のような `source localization の direct validation` を、そのまま `network validation` と誤読する余地が残っていました。
- 根拠:
  - Mahjoory et al. (2017) は、source localization より functional / effective connectivity の方が pipeline 間で一貫性が低いことを示しました。
  - Vallarino et al. (2023) は、source estimation に最適な regularization と connectivity estimation に最適な regularization が一致しないことを示しました。
- 修正:
  - `wiki/observation-to-estimation.md` に `connectivity validation ladder` 節を新設し、`pipeline stability`、`connectivity-specific tuning`、`coverage-limited local concordance`、`group-level invasive atlas consistency`、`perturbation` の 5 段に分けました。

### 2. 旧版は leakage-control と directed metric の限界を書いていましたが、zero-lag 除去の trade-off をまだ十分に前景化していませんでした

- 問題:
  - 旧版は wPLI や ghost interaction の注意点を持っていましたが、`zero-lag を減らす metric = より真の connectome` と誤読される余地が残っていました。
- 根拠:
  - Afnan et al. (2025) は、group-level の MEG resting-state connectome と iEEG atlas の比較で、AEC / PLV は中等度相関する一方、OAEC / wPLI では相関が低下することを示しました。
  - これは leakage 抑制と真の zero-lag coupling 除去が trade-off を持つことを意味します。
- 修正:
  - 同ページの `2026-03 の一次文献が切る境界` を更新し、Afnan et al. (2025) を加えて `lagged metric = leakage solved` をより明確に否定しました。

### 3. 旧版は public entry から新しい境界に辿る導線が弱く、修正しても入口から見つけにくい状態でした

- 問題:
  - `eeg_101.md` には network claim の監査節がありましたが、新たに追加した technical wiki 側の `connectivity validation ladder` への直リンクがありませんでした。
- 修正:
  - `eeg_101.md` の network claim note に、`wiki/observation-to-estimation.html#connectivity-validation-ladder` への導線を追加しました。

## 今回実行した変更

- `wiki/observation-to-estimation.md`
  - `last_updated` を `2026-03-16` に更新
  - front matter に `局在妥当化 / network 妥当化 / perturbation 妥当化は別ラダー` を追加
  - `known_points` と `unknown_points` に、connectivity-specific tuning と whole-brain ground truth 不在を追記
  - `connectivity-gates` 節の文献監査 note を更新
  - `connectivity validation ladder` 節を新設
  - `site rules` に `localization validated != network validated` と `localization-optimal setting != connectivity-optimal setting` を追記
  - 参考文献に Mahjoory et al. (2017), Vallarino et al. (2023), Afnan et al. (2025) を追加
- `eeg_101.md`
  - network claim note から新設節への導線を追加

## 外部依存で保留

- なし
  - 今回の修正はすべてこのリポジトリ内で完結しています。

## 参考文献

- Mahjoory K, Nikulin VV, Botrel L, et al. Consistency of EEG source localization and connectivity estimates. *NeuroImage*. 2017;152:590-601.
  - https://doi.org/10.1016/j.neuroimage.2017.02.076
- Vallarino E, Bartolomeo P, Bénar C, et al. Connectivity estimation results strongly depend on the choice of source reconstruction parameters. *NeuroImage*. 2023;278:120304.
  - https://doi.org/10.1016/j.neuroimage.2023.120304
- Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464.
  - https://doi.org/10.1111/epi.18552
- Papadopoulou M, Friston K, Marinazzo D. Estimating Directed Connectivity from Cortical Recordings and Reconstructed Sources. *Brain Topogr*. 2019;32(4):741-752.
  - https://doi.org/10.1007/s10548-015-0450-6
- Afnan J, Cai Z, Lina J-M, et al. Validating MEG estimated resting-state connectome with intracranial EEG. *Network Neuroscience*. 2025;9(1):421-446.
  - https://doi.org/10.1162/netn_a_00445
- Vink JJJ, Ramos-Nuñez AI, Bellesi A, et al. The brain's functional connectome is a poor predictor of the brain's causal activity flow. *PLoS Comput Biol*. 2020;16(1):e1007866.
  - https://doi.org/10.1371/journal.pcbi.1007866
