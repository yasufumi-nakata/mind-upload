# Site Deepening Audit (2026-03-18, Timing-State / Conduction Delay Is Not One Scalar)

## 対象

- 主対象: `wiki/connectome-is-not-enough.md`
- 副対象: `verification.md`
- 副対象: `tech_roadmap.md`

## 今回の選定理由

- 2026-03-18 時点の公開サイトは、`connectome-complete ≠ emulation-complete`、`delay / myelin が重要` という方向性自体は既に正しく置けていました。
- しかし、`delay / myelin` の記述はなお 1 本の潜在変数に圧縮されやすく、`node / internode geometry`、`periaxonal space`、`perinodal astrocyte control`、`human tract-scale timing proxy` が分離されていませんでした。
- この弱さは技術・自然科学の観点で重要です。なぜなら、`閉ループ機器のレイテンシが速い` ことと、`生体側の伝導タイミング状態が分かっている` ことは別であり、ここを混ぜると `hardware-fast` を `timing-complete` に誤昇格させるからです。

## 主要な批判点

### 1. 旧 site は `delay / myelin` を重要変数として挙げていたが、timing-state の内部構造を潰していました

- 問題:
  - `wiki/connectome-is-not-enough.md` と `verification.md` は、髄鞘や伝導遅延が state variable であること自体は明示していました。
  - しかし、旧文面だと読者が `delay = 1 個の定数` と読めてしまい、`node length`、`internode geometry`、`periaxonal coupling`、`astrocyte-dependent paranodal structure` が timing-state を動かす別レイヤーであることが前面に出ていませんでした。
- 根拠:
  - Gibson et al. (2014) は activity-dependent oligodendrogenesis / adaptive myelination を示しました。
  - McKenzie et al. (2014) は新規 myelination が motor-skill learning に必要であることを示しました。
  - Seidl et al. (2015) は Ranvier node / internode geometry が action-potential timing を調整することを示しました。
  - Dutta et al. (2018) は perinodal astrocyte が nodal gap length と myelin structure を可逆的に変え、conduction velocity を変えることを示しました。
  - Cohen et al. (2020) は saltatory conduction が periaxonal nanocircuit を含むことを示しました。
- 批判:
  - したがって、`delay / myelin` を 1 行で扱うだけでは、timing-sensitive circuit に必要な state decomposition が不足していました。
  - 特に phase / synchrony / spike-arrival claim では、`graph + one delay constant` という読み方を許すのは甘すぎます。

### 2. 旧 site は `hardware latency` と `biological timing-state` を十分に分離していませんでした

- 問題:
  - `tech_roadmap.md` の M2 は closed-loop latency / jitter をかなり丁寧に扱っていました。
  - しかし、そこでは主として `device-side timing audit` が中心で、`生体側の conduction timing も未測定なら latent` という site-wide rule がまだ弱い状態でした。
- 根拠:
  - Micheva et al. (2021) は local PV interneuron axon の myelination degree と conduction velocity の相関を示しました。
  - Dubey et al. (2022) は PV axon myelination loss が fast phasic inhibition と gamma oscillation を崩すことを示しました。
- 批判:
  - これらは、timing-sensitive claim の失敗が `hardware latency` だけでなく `biological timing-state` の未同定でも起きることを示しています。
  - したがって、`photodiode/TTL audit が通った` だけでは timing claim を引き上げられません。

### 3. 旧 site は human-side timing evidence の claim ceiling を明示しきれていませんでした

- 問題:
  - 人間側では myelin や transmission speed の計測が少しずつ進んでいますが、旧 site には `human timing evidence がどこまで直接で、どこから proxy か` の線引きが十分にありませんでした。
- 根拠:
  - van Blooijs et al. (2023) は human brain の transmission speed に developmental trajectory があることを示しました。
- 批判:
  - これは tract-scale で timing が biologically variable であることを支持しますが、`node length`、`periaxonal space`、`oligodendrocyte state`、`local inhibitory arrival time` の ground truth ではありません。
  - したがって、human myelin / tract-speed data は `macro timing proxy` として扱うべきであり、per-axon conduction state に昇格させるべきではありませんでした。

### 4. Verification 側には `timing-state augmentation` の提出物がありませんでした

- 問題:
  - 旧 `verification.md` は augmentation / ablation を良く整理していましたが、timing-state については専用 row がありませんでした。
- 根拠:
  - timing-sensitive prediction は `fixed-delay baseline` と `measured or externally calibrated timing-state` を同一 held-out 条件で比較しないと、何が改善したのかが読めません。
- 批判:
  - この row が無いままだと、`myelin-related evidence を足した` と `timing-sensitive claim を上げた` のあいだに site-wide comparison rule が存在しませんでした。

## 今回実行した変更

- `wiki/connectome-is-not-enough.md`
  - `last_updated` を `2026-03-18` に更新
  - `delay / myelin` を `delay / timing-state` として再定義
  - page highlights / known points に `device latency ≠ biological timing-state` を追加
  - section 4 を拡張し、Seidl / Dutta / Cohen / Micheva / Dubey / van Blooijs を用いて timing-state の内部構造と human observability ceiling を明文化
  - augmentation table に `+ timing-state / conduction audit` row を追加
  - rule table と minimum submission を `timing-state` 用語へ揃えた
- `verification.md`
  - page highlights / known points に timing-state の site-wide rule を追加
  - state-variable integrity gate の `Delay/Myelin` row を `Delay / timing-state` へ改稿
  - `delay is not one scalar` note を追加
  - augmentation table に `+ timing-state / conduction audit` row を追加
  - 既存の glial row の HTML 崩れも合わせて修正
- `tech_roadmap.md`
  - page highlights / known points に `hardware latency` と `biological timing-state` の分離を追加
  - M2 note を改稿し、closed-loop latency audit の外側に `tissue-side timing-state` が残ることを明記
  - M3 の latent-state list に `delay / timing-state` を追加

## 外部依存で保留

- なし
  - 今回の変更は、公開本文・検証ルール・ロードマップ記述の改稿で完結しています。

## 参考文献

1. Gibson EM, Purger D, Mount CW, et al. Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. *Science*. 2014.
   - https://doi.org/10.1126/science.1252304
2. McKenzie IA, Ohayon D, Li H, et al. Motor skill learning requires active central myelination. *Science*. 2014.
   - https://doi.org/10.1126/science.1254960
3. Seidl AH, Rubel EW, Barria A. Tuning of Ranvier node and internode properties in myelinated axons to adjust action potential timing. *Nature Communications*. 2015.
   - https://doi.org/10.1038/ncomms9073
4. Dutta DJ, Woo DH, Lee PR, et al. Regulation of myelin structure and conduction velocity by perinodal astrocytes. *Proceedings of the National Academy of Sciences USA*. 2018.
   - https://doi.org/10.1073/pnas.1811013115
5. Cohen CCH, Popovic MA, Klooster J, et al. Saltatory conduction along myelinated axons involves a periaxonal nanocircuit. *Cell*. 2020.
   - https://doi.org/10.1016/j.cell.2019.11.039
6. Micheva KD, Kiraly M, Perez MM, Madison DV. Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. *Cerebral Cortex*. 2021.
   - https://doi.org/10.1093/cercor/bhab018
7. Dubey S, Kuschmitz S, Mezey SE, et al. Myelination synchronizes cortical oscillations by consolidating parvalbumin-mediated phasic inhibition. *eLife*. 2022.
   - https://doi.org/10.7554/eLife.73827
8. van Blooijs D, de Haan AM, Renaud S, et al. Developmental trajectory of transmission speed in the human brain. *Nature Neuroscience*. 2023.
   - https://doi.org/10.1038/s41593-023-01272-0
