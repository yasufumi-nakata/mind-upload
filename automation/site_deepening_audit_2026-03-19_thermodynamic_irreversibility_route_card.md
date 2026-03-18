# Site Deepening Audit (2026-03-19, Thermodynamic Irreversibility Route Card)

## 対象

- 主対象: `wiki/thermodynamic-grounding-basics.md`
- 副対象: `verification.md`
- 追従対象: `tech_roadmap.md`
- 同期対象: `github-wiki-export/thermodynamic-grounding-basics.md`

## 今回の選定理由

- 2026-03-15 の更新で、`Landauer 下限`・`組織レベル energy budget`・`粗視化 neural dynamics の irreversibility`・`model-based entropy flow` を混同しない最低線は既に入りました。
- しかし、その後も `irreversibility / EPR` という 1 語のまま読める箇所が残っており、一次文献上は別物である estimator family が、ひとつの共通測定量であるかのように見える弱点が残っていました。
- これはサイト全体に効く弱点でございます。`Verification` では thermodynamics を補助ログに下げていても、入門 wiki が estimator family と null control を明示しなければ、読者はなお「thermodynamic paper = 直接 EPR を測った paper」と誤読できます。

## 主要な批判点

### 1. `irreversibility` が 1 種類の計測量として見えていました

- 問題:
  - 旧版は `粗視化 neural dynamics の不可逆性` と `model-based entropy flow` の違いは書いていましたが、その中でさらに異なる estimator family が分かれていませんでした。
  - そのため、`BOLD の coarse-grained transition flux`、`ECoG の time-shifted asymmetry / inversion decoding`、`MEG visibility graph`、`spike train の state-space kinetic Ising entropy flow` が 1 個の熱力学量の variant のように読めました。
- 根拠:
  - Lynn et al. (2021) は、clustered BOLD state transition から entropy-production の lower bound を見積もっています。さらに temporal shuffling で flux が消えることを確認しています。
  - Deco et al. (2022) は、forward / reversed time series の time-shifted correlation matrix の距離で non-reversibility を定義しています。
  - de la Fuente et al. (2023) は、ECoG の temporal inversion を deep learning で decode しています。
  - Nartallo-Kaluarachchi et al. (2025) は、MEG の directed multiplex visibility graph の in/out-degree distribution の Jensen-Shannon divergence を multilevel irreversibility として使っています。
  - Ishihara & Shimazaki (2025) は、state-space kinetic Ising model と mean-field approximation の上で time-varying entropy flow を推定しています。
- 修正:
  - `wiki/thermodynamic-grounding-basics.md` に `\"Irreversibility\" is not one estimator family` 節を追加しました。
  - 各 estimator family について、`何を計算しているか` と `このサイトで許す safe ceiling` を表で分離しました。

### 2. `Verification` 側の thermodynamic log が、まだ開示不足でした

- 問題:
  - 旧 `Supplementary thermodynamic log` は `coarse-graining` `modality` `sampling` `estimator` `lower bound or main body estimation` `hardware power isolation` までは要求していました。
  - しかし、一次文献の差はそこだけではありません。`signal route`、`state definition`、`null / surrogate control`、`quantity type`、`abstention boundary` がなければ、過大読みを十分に止められません。
- 根拠:
  - Lynn et al. (2021) は temporal shuffling を用いて flux が artifact ではないことを検証しています。
  - Ishihara & Shimazaki (2025) は trial-shuffled data を用い、firing-rate dynamics と sampling error の寄与を切り分けています。
  - したがって、thermodynamic claim の読解では estimator だけでなく control の開示が必要です。
- 修正:
  - `verification.md` の `Supplementary thermodynamic log` を `Irreversibility / Thermodynamic Route Card` に置き換えました。
  - 必須開示項目として `signal route and state definition` `estimator family` `null / surrogate control` `quantity type` `cost isolation` `abstention boundary` を明記しました。
  - `thermodynamic-verification` 節に 2026-03-19 addendum を追加し、どの一次文献がどの estimator family を代表するかを明記しました。

### 3. `tech_roadmap.md` の I9 が、読者の次アクションとしてはまだ粗かったです

- 問題:
  - 旧 I9 は caution 自体は正しかったものの、`次に何を publish すべきか` が route-card 単位まで落ちていませんでした。
- 根拠:
  - 今回確認した一次文献群は、thermodynamic result が 1 つの通貨ではないことを示しています。
  - したがって、読者の次アクションは `thermodynamic benchmark` という抽象語ではなく、`irreversibility route card` を公開することに落とすべきです。
- 修正:
  - `tech_roadmap.md` の I9 に `estimator family and null control` を追加しました。
  - `Next` を route-card 公開へ言い換え、`wiki/thermodynamic-grounding-basics.html#irreversibility-route-card` へ直接つなげました。

## 今回実行した変更

- `wiki/thermodynamic-grounding-basics.md`
  - `last_updated` を 2026-03-19 に更新
  - estimator family を分解する節を追加
  - `irreversibility route card` を追加
  - 過大読み例に `EPR を brain activity から直接測った` を追加
  - 参照文献に Deco et al. (2022) を追加
- `verification.md`
  - thermodynamic log を `Irreversibility / Thermodynamic Route Card` に更新
  - thermodynamic section に 2026-03-19 addendum を追加
  - `de la Fuente et al.` の年表記を 2023 に統一
  - 参照文献に Deco et al. (2022) と Nartallo-Kaluarachchi et al. (2025) を追加
- `tech_roadmap.md`
  - I9 の運用規則に `estimator family and null control` を追加
  - `Next` を route-card 公開へ更新

## 外部依存で保留

- 同一タスク・同一前処理条件での cross-modality irreversibility benchmark
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: fMRI / MEG / ECoG / spike train の比較可能な公開データと、各 modality で再現可能な preprocessing chain があること
  - 完了条件: `signal route` `estimator family` `null control` `quantity type` `cost isolation` を同一 schema で比較できる公開 benchmark が整うこと

## 参考文献

- Bérut A, Arakelyan A, Petrosyan A, et al. Experimental verification of Landauer’s principle linking information and thermodynamics. Nature. 2012.
  - https://doi.org/10.1038/nature10872
- Attwell D, Laughlin SB. An energy budget for signaling in the grey matter of the brain. J Cereb Blood Flow Metab. 2001.
  - https://doi.org/10.1097/00004647-200110000-00001
- Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. Proc Natl Acad Sci U S A. 2021.
  - https://doi.org/10.1073/pnas.2109889118
- Deco G, Sanz Perl Y, Bocaccio H, Tagliazucchi E, Kringelbach ML. The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states. Commun Biol. 2022.
  - https://doi.org/10.1038/s42003-022-03505-7
- de la Fuente LA, Zamberlan F, Bocaccio H, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. Cereb Cortex. 2023.
  - https://doi.org/10.1093/cercor/bhac177
- Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. Proc Natl Acad Sci U S A. 2025.
  - https://doi.org/10.1073/pnas.2408791122
- Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-66669-w
