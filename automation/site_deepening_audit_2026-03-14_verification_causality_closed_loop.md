# Site Deepening Audit (2026-03-14, Verification Causality / Closed Loop)

## 対象

- 主対象: `verification.md`
- 副対象: `wiki/counterfactual-and-perturbation-verification.md`
- 副対象: `wiki/closed-loop-latency-jitter-and-safety-stops.md`

## 今回の選定理由

- 公開サイトの中核主張は `Verification Commons` にありますが、2026-03-14 時点の本文は、`因果摂動` と `閉ループ` を重要だと述べる一方で、どの一次文献がどこまで到達しているかを十分に切り分けていませんでした。
- その結果、`offline で高精度`、`online で動く`、`外部介入で挙動が変わる`、`長期に安定運用できる` が、同じ強さの証拠として読まれる余地が残っていました。
- これは技術・自然科学の観点では重大です。なぜなら、現在の BCI / adaptive stimulation 文献が示しているのは主として局所サブシステム・課題限定の causal evidence であり、全脳WBEの branch-equivalence ではないからです。

## 主要な批判点

### 1. `verification.md` は「因果摂動」を掲げつつ、証拠段階を分け切れていませんでした

- 問題:
  - 旧版は `Stage A/B/C` を示していましたが、`online human-in-the-loop`、`bidirectional feedback`、`state-dependent intervention`、`longitudinal stability` の差が表の形で固定されていませんでした。
  - そのため、offline 成績の改善を、L2/L3 に近い進歩として過大に読める構造が残っていました。
- 根拠:
  - Forenzo et al. (2024) は non-invasive BCI の online continuous tracking を示しましたが、これは online decode の実証であり、反事実同値ではありません。
  - Flesher et al. (2021) は tactile feedback による双方向 loop が行動を改善することを示しましたが、感覚運動サブシステムの局所 causal gain に留まります。
  - Oehrn et al. (2024) と Dixon et al. (2026) は adaptive DBS の在宅・実生活 block 評価を示し、短いラボデモと deployable controller の間に追加の壁があることを示しました。
  - Wairagkar et al. (2025) と Wilson et al. (2025) は、低遅延 loop を実装しても decoder drift / recalibration burden が別問題として残ることを示しました。
- 修正:
  - `verification.md` の `因果的摂動スイート` を `4ゲート制` へ再編しました。
  - `online decode`、`bidirectional perturbation`、`state-dependent intervention`、`longitudinal stability` を別行で明示し、それぞれに代表的な一次文献と「まだ言えないこと」を付けました。
  - 合否指標も `effect size` だけでなく、`P50/P95/P99 latency`、`jitter`、`dropout`、`recalibration burden`、`recovery time` まで引き上げました。

### 2. `wiki/counterfactual-and-perturbation-verification.md` は概念整理に偏り、境界事例が弱すぎました

- 問題:
  - 旧版は `介入`、`反事実`、`摂動` を日常語で説明していましたが、読者が「では現実の一次文献では何がどこまで実証されたのか」を判断しにくい構造でした。
  - 特に `反事実` という語を、branch variable や比較規則の事前固定なしで使えるように読めてしまう点が弱点でした。
- 根拠:
  - Wairagkar et al. (2025) は low-latency voice loop を示しましたが、約 15 日で fixed decoder の性能が落ちており、長期安定性を別問題として扱う必要があります。
  - Casali et al. (2013) と Comolatti et al. (2019) は perturbation-based metric を実装可能にしましたが、刺激条件とアーチファクト処理を固定しなければ比較不能です。
  - Willett et al. (2023) と Littlejohn et al. (2025) は speech neuroprosthesis を前進させましたが、通信サブシステムの online decode / control を示したのであって、branch-equivalence ではありません。
- 修正:
  - 本文を `5段階の因果証拠ラダー` と `一次文献で見る境界事例` に再構成しました。
  - `反事実` の使用条件として、`分岐変数`、`比較規則`、`アーチファクト窓`、`失敗条件` の 4 条件を固定しました。
  - `介入応答テスト` と `摂動一般化テスト` を、より弱いが誤解の少ない表現として導入しました。

### 3. `wiki/closed-loop-latency-jitter-and-safety-stops.md` は、遅延の定義はあっても運用指標が足りませんでした

- 問題:
  - 旧版は `遅延 / ジッタ / ドリフト / 棄権 / 安全停止` の区別としては正しかった一方、実際に何をログとして残すべきかが抽象的でした。
  - これでは、平均 latency だけ示して `L3 達成` と読む誤解を止めきれません。
- 根拠:
  - Littlejohn et al. (2025) は naturalistic communication で数秒単位の遅れが破綻要因になることを明示し、speech 系では tail latency が重要であることを示しました。
  - Wairagkar et al. (2025) は raw-to-speech を 10 ms 未満で回しつつ non-speech 区間で silence を返しました。これは latency だけでなく abstention 実装が必須だと示しています。
  - Wilson et al. (2025) は frequent recalibration 自体が neural bypass の大きな障害だと述べ、recalibration burden を性能から切り離せないことを示しました。
  - 2026年2月25日公開の Cascino et al. (2026) は、20 連続症例中 9 例が aDBS 候補、2025年7月時点で 5 例継続と報告し、deployability と programming burden を実装成績から分離できないことを示しました。
- 修正:
  - `一次文献が示す現実` 節を新設し、speech BCI、bidirectional BCI、adaptive DBS、長期 recalibration の文献を並べました。
  - `L3 を主張するなら最低限ほしい指標` として、`P50/P95/P99 latency`、`jitter`、`dropout`、`recalibration burden`、`abstention / hold-last-output`、`recovery time`、`stimulation duty cycle` を明示しました。
  - `棄権`、`hold-last-output`、`freeze`、`hard stop` を分離し、停止回数そのものを性能指標として扱うルールを追加しました。

## 今回実行した変更

- `verification.md`
  - `因果的摂動スイート` を `4ゲート制` へ改稿
  - `反事実` を使う条件を明示
  - 2023-2026 の BCI / adaptive stimulation 一次文献を参考文献へ追加
  - `Unnwongse et al.` の年表記を 2023 に修正
- `wiki/counterfactual-and-perturbation-verification.md`
  - front matter を更新し、一次文献ベースのページへ再設計
  - `5段階ラダー`、`境界事例`、`反事実の使用条件`、`最低限ログ` を追加
  - 参考文献を primary papers 中心で新設
- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - front matter を更新し、`実務指標` 中心のページへ再設計
  - speech neuroprosthesis / tactile BCI / adaptive DBS / recalibration の一次文献を追加
  - `L3 最低提出物パック` と `停止種別の分離` を追加

## 外部依存で保留

- 実被験者介入を含む `Stage C` benchmark の実装
  - 担当者: AI / maintainer / 実験系共同研究者
  - 前提条件: IRB、機材、被験者運用、刺激安全プロトコル
  - 完了条件: 刺激条件、アーチファクト窓、停止条件、失敗条件を事前固定したうえで、査読可能な公開ログを伴う実験が走ること
- 長期閉ループの site-wide benchmark 化
  - 担当者: AI / maintainer
  - 前提条件: 公開可能な longitudinal BCI / adaptive stimulation データセットまたは運用ログの確保
  - 完了条件: `verification.md` の `Gate 4` を公開ベンチとして再現実装できること

## 参考文献

- Forenzo D, Zhu H, Shanahan J, Lim J, He B. Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. PNAS Nexus. 2024.
  - https://doi.org/10.1093/pnasnexus/pgae145
- Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023.
  - https://doi.org/10.1038/s41586-023-06377-x
- Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025.
  - https://doi.org/10.1038/s41593-025-01905-6
- Wairagkar M, Moses DA, Metzger SL, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025.
  - https://doi.org/10.1038/s41586-025-09127-3
- Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021.
  - https://doi.org/10.1126/science.abd0380
- Wilson GH, Bray N, Franken M, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025.
  - https://doi.org/10.1038/s41551-025-01536-z
- Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. Nat Med. 2024.
  - https://doi.org/10.1038/s41591-024-03196-z
- Dixon S, Oehrn C, Remple M, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. Nat Biomed Eng. 2026.
  - https://doi.org/10.1038/s41551-025-01592-5
- Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson’s disease: ADAPT-START findings and programming principles. npj Parkinsons Dis. 2026.
  - https://doi.org/10.1038/s41531-026-01269-z
- Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med. 2013.
  - https://doi.org/10.1126/scitranslmed.3006294
- Comolatti R, Pigorini A, Casarotto S, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. Brain Stimul. 2019.
  - https://doi.org/10.1016/j.brs.2019.05.013
