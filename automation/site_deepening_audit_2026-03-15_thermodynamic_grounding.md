# Site Deepening Audit (2026-03-15, Thermodynamic Grounding)

## 対象

- 主対象: `tech_roadmap.md`
- 副対象: `wiki/thermodynamic-grounding-basics.md`

## 今回の選定理由

- 公開サイトの熱力学まわりは、`verification.md` と `wiki/thermodynamic-grounding-basics.md` ではかなり慎重に書かれていましたが、`tech_roadmap.md` の `I9` は依然として強すぎる記述が残っていました。
- とくに旧 `I9` は、`Landauer 下限`、`生体脳の代謝予算`、`粗視化 neural dynamics の time irreversibility`、`model-based entropy flow` を 1 本の必須条件として束ねており、一次文献の到達点を越えて読める状態でした。
- これはサイト全体に効く問題でございます。`tech_roadmap.md` は学習者が「どの問題を解けたら前進か」を読む基準ページであり、ここで探索的補助ログを必須ゲートのように見せると、他ページの慎重な記述まで弱く読まれてしまいます。

## 主要な批判点

### 1. 旧 `I9` は、異なる測定層を 1 つの工学要件に混ぜていました

- 問題:
  - 旧版は `Landauer`、`EPR > 0`、`20W`、`通信:計算比`、`Virtual Dissipation Protocol` を一続きの設計条件として提示していました。
  - しかし、これらは同じ層の量ではありません。
- 根拠:
  - Bérut et al. (2012) が実証したのは、`logically irreversible` な 1-bit erasure に対する最小散逸下限であり、デジタル脳全体の wall-power や NESS 再現条件ではありません。
  - Lynn et al. (2021) は、coarse-grained fMRI state dynamics から broken detailed balance と entropy production を推定しましたが、同論文自体が coarse graining により nonequilibrium degrees of freedom を平均化しうることを明示しています。
  - Nartallo-Kaluarachchi et al. (2025) も、観測 multivariate time-series の irreversibility は EPR の lower bound であると明示しています。
  - Ishihara & Shimazaki (2025) は、entropy flow 推定が state-space kinetic Ising model、pairwise coupling、mean-field approximation に依存する model-based quantity であることを示しています。
- 修正:
  - `wiki/thermodynamic-grounding-basics.md` に `4つの測定層` を追加しました。
  - `Landauer 下限`、`組織レベルのエネルギー予算`、`粗視化 neural dynamics の不可逆性`、`model-based entropy flow` を別物として表に分解しました。

### 2. 旧 `I9` は、一次文献がまだ支持していない必須ゲートを置いていました

- 問題:
  - `EPR > 0 を維持しつつ論理計算を行うアルゴリズムの定式化`
  - `Virtual Dissipation Protocol`
  - `生体脳 20W と同等`
  - `通信:計算のエネルギー消費比率が同等`
  - これらが、あたかも現時点の受理条件のように並んでいました。
- 根拠:
  - Bérut et al. (2012)、Lynn et al. (2021)、de la Fuente et al. (2022)、Nartallo-Kaluarachchi et al. (2025)、Ishihara & Shimazaki (2025) のいずれも、WBE の acceptance gate として上記条件を導出していません。
  - Attwell & Laughlin (2001) は rodent gray matter における signaling budget の分解を与えていますが、これは biological tissue の descriptive budget であり、digital emulation の合否基準ではありません。
- 修正:
  - 旧 `I9` の必須条件を撤回し、熱力学指標は `補助ログ` と明記しました。
  - 以下の判断は、上記一次文献が WBE の必須ゲートを導出していない点からの **推論** です:
    - `EPR > 0` 維持を受理条件にしない
    - `20W` や `通信:計算比` を site-wide KPI にしない
    - `Virtual Dissipation Protocol` を設計既定路線にしない

### 3. 旧 `I9` は、理論依存の主張を熱力学の工学要件へ持ち込みすぎていました

- 問題:
  - 旧版は `IIT 4.0` や `Unfolding Argument` を前面に出しつつ、そこから substrate requirement や thermodynamic guarantee を導く構造でした。
  - しかし、熱力学の一次文献が直接支えているのは、`論理的不可逆性の下限` と `粗視化 neural dynamics の time asymmetry` までです。
- 修正:
  - `tech_roadmap.md` の `I9` を、理論採択の節ではなく `どこまでを measurement / logging question として扱うか` の節に差し替えました。
  - 工学的に今やることを、`wall-plug power`、`FLOPs`、`time irreversibility`、`model-based entropy flow` の分離ログへ限定しました。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を 2026-03-15 に更新
  - `I9` を全面改稿し、`Virtual Dissipation Protocol` / `EPR > 0` / `20W KPI` / `通信:計算比 KPI` を撤回
  - 熱力学指標を `補助ログ` とし、最低限残すべきログ schema を追加
  - 参考文献の thermodynamics 節を、実在する一次文献ベースへ差し替え
- `wiki/thermodynamic-grounding-basics.md`
  - `last_updated` を 2026-03-15 に更新
  - `4つの測定層` を追加
  - `20W や signaling budget を必須閾値にしない` ことを本文へ明記
  - 参考文献へ Bérut et al. (2012) と Attwell & Laughlin (2001) を追加

## 外部依存で保留

- cross-modal irreversibility benchmark の整備
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: 同一タスクについて、EEG / ECoG / fMRI / MEG の少なくとも一部で比較可能な公開データと、共有前処理条件があること
  - 完了条件: `粗視化条件` `推定器` `lower bound / model-based quantity` `wall-power / FLOPs` を同一 schema で比較できる公開 benchmark が整うこと

## 参考文献

- Bérut A, Arakelyan A, Petrosyan A, et al. Experimental verification of Landauer’s principle linking information and thermodynamics. Nature. 2012.
  - https://doi.org/10.1038/nature10872
- Attwell D, Laughlin SB. An energy budget for signaling in the grey matter of the brain. J Cereb Blood Flow Metab. 2001.
  - https://doi.org/10.1097/00004647-200110000-00001
- Lynn CW, Cornblath EJ, Papadopoulos L, et al. Broken detailed balance and entropy production in the human brain. Proc Natl Acad Sci U S A. 2021.
  - https://doi.org/10.1073/pnas.2109889118
- de la Fuente LA, Perl YS, Zamberlan F, et al. Temporal irreversibility of neural dynamics as a signature of consciousness. Cereb Cortex. 2023.
  - https://doi.org/10.1093/cercor/bhac177
- Nartallo-Kaluarachchi R, Bonetti L, Fernández-Rubio G, et al. Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. Proc Natl Acad Sci U S A. 2025.
  - https://doi.org/10.1073/pnas.2408791122
- Ishihara K, Shimazaki H. State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. Nat Commun. 2025.
  - https://doi.org/10.1038/s41467-025-66669-w
