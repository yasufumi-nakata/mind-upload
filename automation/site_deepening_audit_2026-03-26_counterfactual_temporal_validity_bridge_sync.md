# Site Deepening Audit (2026-03-26, counterfactual wiki temporal-validity / bridge / maintenance sync)

## 対象

- 主対象: `wiki/counterfactual-and-perturbation-verification.md`
- 同期対象: `github-wiki-export/counterfactual-and-perturbation-verification.md`
- 参照整合先: `verification.md`, `wiki/state-continuity-bridge.md`, `wiki/state-trait-and-drift.md`, `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- 調査方法: 公開中の `https://mind-upload.com/wiki/counterfactual-and-perturbation-verification.html` を web で確認し、ローカル原稿と site-wide rule を突き合わせ
- 範囲: 技術 / 自然科学のみ

## 今回このページを選んだ理由

- `wiki/counterfactual-and-perturbation-verification.md` は 2026-03-14 更新のままで、最近 site 全体に追加された
  - `Temporal Validity Card`
  - `State-Continuity Bridge Card`
  - `Maintenance-State Error Budget`
  - `Body / Environment Boundary Card`
  との接続が本文レベルで弱い状態でした。
- その結果、読者は依然として
  - `online で動いた`
  - `局所介入で行動が変わった`
  - `cross-day でも何とか動いた`
  - `same-subject だった`
  を、一段階ずつ別の監査対象としてではなく、一本の「因果検証ラダー」として読めてしまいます。
- これは自然科学的に弱いです。現在の一次文献が示しているのは、局所 causal gain、低遅延 closed loop、unsupervised recalibration、在宅 deployment、same-state bridge validity がそれぞれ別問題だということだからです。

## 主批判

### 1. 同ページは `same-session causal gain` と `cross-day durability` を十分に分離しておりませんでした

- [Wairagkar et al. (2025)](https://doi.org/10.1038/s41586-025-09127-3) は、raw neural activity から voice synthesis までを 10 ms 未満で回し、non-speech では silence を返す closed-loop 実装を示しました。
- しかし同論文の Extended Data では、固定 decoder の性能が約 15 日後から目立って低下することも報告されています。
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) は、one-month の unsupervised closed-loop を示しつつ、5 年分の iBCI 記録を用いて、`pairwise recalibration` と `iterative longer-term use` が別問題であることを明示しました。

批判:

- したがって `closed-loop で動いた` を一つの causal-evidence bucket として読むのは弱いです。
- `same-session low latency`、`fixed-decoder durability`、`unsupervised recalibration burden`、`home-use viability` は別々に監査しなければなりません。

### 2. `same-subject` を `same-state` へ近似する停止線がこのページでは弱いままでした

- [Lu et al. (2023)](https://doi.org/10.1016/j.crmeth.2023.100520) は preservation route と fixation time course が extracellular-space retention を変えることを示しました。
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) は same-brain function + EM を大きく前進させましたが、simultaneous capture ではなく sequential local pipeline です。
- [Attardo et al. (2015)](https://doi.org/10.1038/nature14467) は adult CA1 spine の lifetime が週スケールで動くことを示しました。

批判:

- したがって `same-subject` や `same-brain` のラベルだけでは、一つの latent-state sample を保証できません。
- 因果検証 wiki 自体が `State-Continuity Bridge Card` に接続していないと、bridge-validity の site-wide rule がここだけ落ちます。

### 3. `persistence / forgetting / recovery after perturbation` を maintenance-state disclosure なしで読める構造が残っていました

- [Hengen et al. (2016)](https://doi.org/10.1016/j.cell.2016.01.046) は firing-rate homeostasis が sleep / wake で制御されることを示しました。
- [Schreiner et al. (2024)](https://doi.org/10.1038/s41467-024-49572-8) は spindle-locked ripple と memory reactivation の関係を示しました。
- [Deng et al. (2025)](https://doi.org/10.1016/j.neuron.2025.03.020) は NREM memory consolidation に特定の intracellular time window があることを示しました。

批判:

- よって intervention 後の retention や recovery を読むときに、`maintenance-state families` を伏せたまま causal story を作るのは過大です。
- counterfactual / perturbation wiki でも `Maintenance-State Error Budget` へ接続しないと、same-day perturbation response が long-horizon causal equivalence のように誤読されます。

### 4. deployability は timing だけでなく eligibility / programming burden でも止まります

- [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z) は chronic aDBS を blinded randomized blocks で home life まで持ち込みました。
- [Cascino et al. (2026)](https://doi.org/10.1038/s41531-026-01269-z) は 20 連続 Parkinson 症例へ dual-threshold aDBS を提示し、eligibility と programming constraints が continue 可能性を左右することを示しました。
- [Dixon et al. (2026)](https://doi.org/10.1038/s41551-025-01438-0) も remote optimization を前景化しました。

批判:

- したがって `state-dependent intervention` を読んだとき、lab success と deployable controller を同一視するのは不適切です。
- このページは `Temporal Validity` だけでなく `deployment burden` も causal-verification ladder の独立段として見せる必要がありました。

## 今回実行した変更

- `wiki/counterfactual-and-perturbation-verification.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter に
    - `Temporal Validity`
    - `State-Continuity Bridge`
    - `Maintenance-State Error Budget`
    - `Body / Environment Boundary`
    との接続を追加
  - 本文の因果ラダーを `5段階` から `6段階` へ改稿
    - held-out decode
    - online human-in-the-loop
    - bidirectional / local intervention
    - state-dependent intervention
    - temporal durability / deployment
    - perturbation-structure / branch test
  - `Recent literature forces four extra stop lines` 節を新設
  - `counterfactual` と呼ぶ条件を 4 条件から 6 条件へ拡張
    - temporal scope
    - bridge status
    を追加
  - `Minimum log bundle now required` 節を新設し、timing, temporal validity, bridge, maintenance, boundary を分離
  - `Boundary cases` table を更新し、Littlejohn 2025, Wilson 2025, Cascino 2026 を追加
  - 参考文献を更新し、bridge / maintenance / deployment 系を補強

## 今回実行する変更

- `github-wiki-export/counterfactual-and-perturbation-verification.md`
  - export script で再生成し、GitHub Wiki 側の読書導線も同期

## 外部依存で保留

- same-branch / whole-brain perturbation benchmark の実装
  - 担当者: maintainer / 実験系共同研究者
  - 前提条件: 介入プロトコル、IRB、長期閉ループ運用ログ、公開可能データ
  - 完了条件: perturbation, temporal validity, bridge validity, maintenance-state disclosure を同時に検証できる公開 benchmark の実装

- chronic deployment benchmark の実データ整備
  - 担当者: maintainer / 実験系共同研究者
  - 前提条件: home-use / clinic-use の公開 longitudinal controller log
  - 完了条件: eligibility, continuation, programming burden, recalibration burden を比較可能な schema で公開
