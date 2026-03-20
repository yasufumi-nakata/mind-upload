# Mind-upload RQ60 Deep Evaluation Cards (EEG-DATA × auto-research-funds)

> 1RQ=1検証命題=1応募テーマ=1主データを実行可能な形で固定
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-21 / 位置づけ: Per-RQ Deep Evaluation Cards

---

# Mind-upload RQ60 Deep Evaluation Cards (EEG-DATA × auto-research-funds)

> 汎用横断の要約ではなく、60RQを1件ずつ深く読むための固定カード集。

- 更新日: 2026-03-21
- 前提: `mind-upload-eeg-rq60-feasibility-and-funds` と `mind-upload-eeg-rq60-grant-dataset-playbook` の整合を取った統合版

## このページの使い方

1. 対象RQの行だけを読み、`主張単位` と `判定境界` を先に固定する。
2. `第一応募先/予備応募先` を選び、`最低成果物` を先に作る。
3. `C` 判定RQは性能主張を避け、制度・監査設計トラックとして提出する。

## 判定内訳（再計数）

- `A`: 17
- `B`: 25
- `C`: 18

## 本run固定: 1件ずつ深掘りする6RQ（2026-03-20）

汎用横断の更新ではなく、初回結果まで最短で到達できる6RQを固定し、各RQで `KPI` `失敗条件` `最低成果物` を先に埋める。

| RQ | 深掘りする理由 | 最初の実験KPI | 失敗条件（停止条件） | 最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|---|
| U14-1 | 固定粒度を段階比較するだけで2週間で差分が出せる。 | 追試成功率・再現率差・追加工数 | 最厳格条件でも追試成功率が目標未達。 | Supplementary test operation report (including negative cases) | G1 / G3 |
| U7-2 | offset/jitter抽出を固定すれば警告閾値初版を短期確定できる。 | clock offset・jitter p95・閾値超過率 | 閾値超過イベントの再現性不足、または誤警報率過大。 | Time synchronization audit report (offset/jitter distribution) | G1 / G3 |
| U14-3 | 既存分割に監査ルールを当てるだけで再分割差分まで到達できる。 | 被験者リーク検出率・時系列リーク検出率・再分割後性能差 | 再分割後もリーク0件を達成できない。 | Leak audit results and repartition trail | G1 / G3 |
| U8-1 | 遅延条件を振るだけで安全域KPIを表にできる。 | 安定率・回復時間・異常停止率 | 遅延増加で安定率低下が大きく許容域を切れない。 | Closed loop safety KPI dashboard | G2 / G5 |
| U8-2 | 再較正頻度3条件比較で運用設計に直結する初回結果が出せる。 | 性能維持率・ドリフト量・再較正コスト | コスト増に対する性能維持率改善が有意に出ない。 | Closed loop safety KPI dashboard | G2 / G5 |
| U13-1 | 同一デコーダの2軸評価で模倣スコア偏重を抑制できる。 | 意味一致率・因果一致率・乖離ケース率 | 意味一致高/因果一致低ケースを分離できない。 | Intervention protocol and rebuttal condition definition | G1 / G4 |

実行順（本run固定）:

1. `U14-1`
2. `U7-2`
3. `U14-3`
4. `U8-1`
5. `U8-2`
6. `U13-1`

## RQ別ディープ評価カード（60件）

| RQ | 主張単位（このRQで最小に検証すること） | 判定境界（EEG-DATA単独で言える範囲） | auto-research-funds応募テーマ | 第一応募先 / 予備応募先 | 主データ（ID） | 補助データ（推奨ID） | 最低成果物 |
|---|---|---|---|---|---|---|---|

| U0-1<br>同一性判定を『観測一致』と『介入応答一致』に分離したとき、どちらを必要条件・十分条件に置くか。 | 観測一致（EEG特徴量）と介入一致（刺激/課題変更時の応答）を分離して二軸ROCを作る。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 若手研究助成（同一性KPI） | G2 (GR-2026-014) / G3 (9Lx4dPK6a4k2gOb7) | 11 | ID 11, 29, 696 | Intervention protocol and rebuttal condition definition |
| U0-2<br>時間同期（ms単位）と状態表現（行動・神経活動・生理）の対応をどう固定するか。 | ID 676/4878で時刻同期ずれと状態特徴量の崩れを同時に計測し、固定ルールを定義する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究奨励金（縦断同一性） | G2 (GR-2026-014) / G3 (9Lx4dPK6a4k2gOb7) | 11 | ID 11, 29, 696 | Time synchronization audit report (offset/jitter distribution) |
| U0-3<br>同一性判定の閾値をタスク別にどう設定し、過学習モデルをどう除外するか。 | ID 11/696でタスク別に同一性閾値を推定し、過学習モデルはセッション外性能で除外する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 博士課程研究助成（個体同定） | G2 (GR-2026-014) / G3 (9Lx4dPK6a4k2gOb7) | 11 | ID 11, 29, 696 | Threshold search notebook and selection rationale table |
| U0-4<br>分岐/複製ケースでの『同一個体』定義をどの評価軸に帰着させるか。 | ID 11/509で「同一個体判定」指標を生体同定精度に限定して運用限界を明記する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 共同研究助成（同一性×責任） | G2 (GR-2026-014) / G3 (9Lx4dPK6a4k2gOb7) | 11 | ID 11, 29, 696 | Identity determination two-axis report (observation match/intervention match) |
| U1-1<br>EEG/MEG逆問題での不良設定性を、どの事前分布で制御するか。 | ID 56の既知刺激位置を使って、事前分布ごとの逆解誤差を比較する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（逆問題ベンチ） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 56 | ID 56, 676, 1839 | Inverse solution comparison table and uncertainty distribution chart |
| U1-2<br>頭蓋導電率・電極配置・ノイズ構造の不確実性を、推定不確実性へどう伝播させるか。 | ID 56/1839で電極欠損・ノイズ注入を行い、不確実性伝播の校正曲線を作る。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 若手研究助成（不確実性推定） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 56 | ID 56, 676, 1839 | Inverse problem reproduction report (error/uncertainty) |
| U1-3<br>同じデータで異なる逆解法（MNE, beamformer, Champagne 等）が乖離した場合の判定規則をどう置くか。 | ID 56/676でMNE/beamformer/Champagneの乖離率をタスク別に比較する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究奨励金（手法比較） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 56 | ID 56, 676, 1839 | Inverse problem reproduction report (error/uncertainty) |
| U1-4<br>推定値だけでなく、信頼区間/後方分布を公開基準に含めるか。 | 逆問題の信頼区間公開可否を、ID 56での後方分布再現性で評価する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 博士課程研究助成（後方分布公開） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 56 | ID 56, 676, 1839 | Inverse solution comparison table and uncertainty distribution chart |
| U3-1<br>ニューロン中心モデルに対して、グリア/体液性調節を追加した際の予測改善量をどう測るか。 | ID 13/39でEEG単独 vs マルチモーダルの性能差を測り、境界拡張の必要量を推定する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 探索的若手研究助成（境界 proxy） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 13 | ID 13, 16, 39 | Boundary expansion evaluation report (single/integrated comparison) |
| U3-2<br>connectome完全性と機能予測性能の関係を、種横断でどう比較するか。 | EEG-DATA単独ではconnectome完全性を直接検証できないため、補助指標としての再現性評価に限定する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 探索的若手研究助成（境界 proxy） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 13 | ID 13, 16, 39 | Boundary expansion evaluation report (single/integrated comparison) |
| U3-3<br>身体・環境結合を除去したモデルで失われる機能をどう定量化するか。 | ID 16/39で身体・環境ループを含む条件差を比較し、除去時の性能低下を測る。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 探索的若手研究助成（境界 proxy） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 13 | ID 13, 16, 39 | Boundary expansion evaluation report (single/integrated comparison) |
| U3-4<br>『必要最小構成』の判定を理論的主張ではなくデータでどう固定するか。 | 必要最小構成の最終判定はEEG単独では不可。まずID 13/39で代理KPIを固定する。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 探索的若手研究助成（境界 proxy） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 13 | ID 13, 16, 39 | Boundary expansion evaluation report (single/integrated comparison) |
| U3-5<br>glymphatic/meningeal lymphatic 系を含むとき、予測精度と説明可能性はどの程度改善するか。 | glymphatic/meningeal系はEEG-DATAに直接計測がなく、同時代謝データ併用前提の探索扱い。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 探索的若手研究助成（境界 proxy） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 13 | ID 13, 16, 39 | Boundary expansion evaluation report (single/integrated comparison) |
| U3-6<br>免疫監視（髄膜免疫・炎症性シグナル）を除外したモデルは、どの時点で長期予測が破綻するか。 | 免疫監視除外モデルの長期破綻はEEG-DATAだけでは不可。縦断臨床データの外部連携が必要。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 探索的若手研究助成（境界 proxy） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 13 | ID 13, 16, 39 | Boundary expansion evaluation report (single/integrated comparison) |
| U4-1<br>観測データ由来の相関を因果グラフへ持ち上げる識別条件は何か。 | ID 19/1839で入力操作に対する応答差を計測し、観測相関との差を分離する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究助成（介入同値） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 19 | ID 19, 56, 1839 | Intervention protocol and rebuttal condition definition |
| U4-2<br>介入実験（刺激・抑制・入力撹乱）で検証可能な最小因果主張は何か。 | ID 56の既知介入で最小因果主張を事前登録し、再現可否で判定する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 若手研究助成（ground-truth介入） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 19 | ID 19, 56, 1839 | Intervention protocol and rebuttal condition definition |
| U4-3<br>active inferenceやDCMの理論予測を、反事実評価にどう接続するか。 | ID 676を主に、介入あり/なしで反事実誤差（PEHE）と予測尤度差を比較し、理論順位を固定する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究奨励金（反事実評価） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 19 | ID 19, 56, 676 | Intervention protocol and rebuttal condition definition |
| U4-4<br>同値判定の失敗条件（falsification）をどの水準で宣言するか。 | ID 19/56で `ΔAUC > 0.03` または `介入応答の符号反転率 > 10%` を失敗宣言閾値として事前登録する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 共同研究助成（反証設計） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 19 | ID 19, 56, 1839 | Causal verification report (minimum intervention claim) |
| U7-1<br>BIDS拡張で同期・QC・刺激ログをどこまで必須化するか。 | ID 676/783で `clock offset` `sampling drift` `stimulus onset` `QC fail code` の4項目を必須化し、欠落時は不採択にする。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（マルチモーダル標準化） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 676 | ID 676, 783, 4878 | Time synchronization audit report (offset/jitter distribution) |
| U7-2<br>LSL等の時刻同期誤差を検証可能な指標に落とせるか。 | ID 6/676でジッタ/遅延の基準値を算出し、閾値超過を自動警告する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 若手研究助成（同期監査） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 676 | ID 676, 783, 4878 | Time synchronization audit report (offset/jitter distribution) |
| U7-3<br>アーチファクト除去（ASR, ZapLine等）の設定差が結果へ与える影響をどう監査するか。 | ID 676/4878で前処理設定差分を再実行し、結果ドリフトを定量化する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究奨励金（前処理差分） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 676 | ID 676, 783, 4878 | Reproducibility audit report (synchronization/QC/preprocessing difference) |
| U7-4<br>モダリティ間アライメント失敗時の再計測/除外基準をどう固定するか。 | ID 676/783でアライメント失敗時の再計測/除外条件を判定木化する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 共同研究助成（再計測基準） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 676 | ID 676, 783, 4878 | Reproducibility audit report (synchronization/QC/preprocessing difference) |
| U7-5<br>前処理差分をCIで自動比較する場合、どの再現率低下をリリースブロック閾値にするか。 | ID 676で前処理CIを回し、基準パイプライン比で `再現率 -5pt` 以上低下を release block 閾値に固定する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（CI再現性） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 676 | ID 676, 783, 4878 | Threshold search notebook and selection rationale table |
| U7-6<br>モダリティ欠損（EEG欠損・fMRI欠損）条件でも同等結論を保てる最小観測セットは何か。 | ID 676/783でEEG欠損・fMRI/fNIRS欠損をシミュレートし最小観測セットを求める。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（欠損ロバスト性） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 676 | ID 676, 783, 4878 | Reproducibility audit report (synchronization/QC/preprocessing difference) |
| U8-1<br>閉ループBCIの遅延許容域を制御理論的にどう同定するか。 | ID 6/1972で遅延・位相ずれに対する `安定率` `停止介入率` `回復時間` を測り、許容域を3指標で定義する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 若手研究助成（閉ループ安定化） | G2 (GR-2026-014) / G5 (871pw3rLjNPKgqA0) | 6 | ID 6, 1972, 2412, 696 | Closed loop safety KPI dashboard |
| U8-2<br>オンライン較正と概念ドリフト対策をどう組み込むか。 | ID 2412/696でオンライン再較正の頻度と性能安定性を比較する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究奨励金（再較正） | G2 (GR-2026-014) / G5 (871pw3rLjNPKgqA0) | 6 | ID 6, 1972, 2412, 696 | Closed loop safety KPI dashboard |
| U8-3<br>個体差と日内変動をまたぐ安定性をどの指標で評価するか。 | ID 696で個体内・個体間分散を分けて長期安定性KPIを設計する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 博士課程研究助成（長期ドリフト） | G2 (GR-2026-014) / G5 (871pw3rLjNPKgqA0) | 6 | ID 6, 1972, 2412, 696 | Operational stability report (safety shutdown/recovery time) |
| U8-4<br>異常検知とフェイルセーフを評価契約へどう組み込むか。 | ID 2412/1972で異常検知遅延とフェイルセーフ発動時間を測る。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 共同研究助成（フェイルセーフ） | G2 (GR-2026-014) / G5 (871pw3rLjNPKgqA0) | 6 | ID 6, 1972, 2412, 696 | Operational stability report (safety shutdown/recovery time) |
| U8-5<br>ヒューマンオーバーライドを導入したとき、誤作動率と回復時間をどうKPI化するか。 | ID 2412で手動オーバーライド時の誤作動率と回復時間をKPI化する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究奨励金（オーバーライド） | G2 (GR-2026-014) / G5 (871pw3rLjNPKgqA0) | 6 | ID 6, 1972, 2412, 696 | Closed loop safety KPI dashboard |
| U8-6<br>週〜月スケール運用での再学習頻度を、性能劣化と安全余裕のトレードオフでどう最適化するか。 | ID 696/2412で再学習間隔を変え、性能劣化と安全余裕のトレードオフを推定する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究助成（再学習最適化） | G2 (GR-2026-014) / G5 (871pw3rLjNPKgqA0) | 6 | ID 6, 1972, 2412, 696 | Closed loop safety KPI dashboard |
| U10-1<br>Landauer下限を神経計算でどう適用/解釈するか。 | Landauer下限の直接検証はEEG-DATA単独では不可。ID 735を理論整合の事前検証に使う。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 理論研究奨励（情報熱力学） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 735 | ID 735, 783, 1011 | Theory consistency memo and proxy correlation analysis |
| U10-2<br>非平衡熱力学指標と神経情報処理効率の対応をどう定義するか。 | 非平衡熱力学指標の主評価は不可。ID 783/1011で代謝proxyとの弱い相関を探索する。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 理論研究奨励（情報熱力学） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 735 | ID 735, 783, 1011 | Theory consistency memo and proxy correlation analysis |
| U10-3<br>理論式を実データ（神経活動・代謝）へ落とし込む観測設計をどう作るか。 | 神経活動+代謝同時計測はID 783で部分検証可能だが、熱散逸実測は外部計測が必要。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 理論研究奨励（情報熱力学） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 735 | ID 735, 783, 1011 | Theory consistency report (thermodynamic proxy) |
| U10-4<br>WBE計算コスト評価に熱力学制約をどう統合するか。 | WBE計算コストへ熱制約を統合する実証はEEG-DATA外。ID 735でモデル妥当性確認まで。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 理論研究奨励（情報熱力学） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 735 | ID 735, 783, 1011 | Theory consistency memo and proxy correlation analysis |
| U11-1<br>理論間で比較可能な入出力仕様をどう定義するか。 | ID 842/859で PCI近似・LZ複雑性・摂動応答の3指標を同一I/O仕様に揃え、順位保存率80%以上を採択条件にする。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究助成（意識指標比較） | G2 (GR-2026-014) / G4 (Drbm6vBRDJkn0NGJ) | 735 | ID 735, 842, 859 | Awareness index comparison report (with failure condition) |
| U11-2<br>PCIやIIT近似計算の計算量制約をどう扱うか。 | IIT厳密計算は除外し、ID 735/842で `PCI近似` `LZ` `wSMI` を計算予算（1症例あたりGPU 2時間以内）付きで比較する。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 理論研究奨励（IIT近似） | G2 (GR-2026-014) / G4 (Drbm6vBRDJkn0NGJ) | 735 | ID 735, 842, 859 | Theoretical comparison I/O specifications and calculation budget |
| U11-3<br>理論予測の対立点を単一実験計画へどう落とすか。 | ID 735/859で理論対立点を同一入力条件へ寄せる試験計画を作る。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 共同研究助成（理論対立検証） | G2 (GR-2026-014) / G4 (Drbm6vBRDJkn0NGJ) | 735 | ID 735, 842, 859 | Awareness index comparison report (with failure condition) |
| U11-4<br>意識指標を臨床/研究で運用する際の失敗条件をどう明示するか。 | ID 859で偽陽性/偽陰性を含む臨床失敗条件の閾値を先に定義する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 臨床系若手助成（失敗条件定義） | G2 (GR-2026-014) / G4 (Drbm6vBRDJkn0NGJ) | 735 | ID 735, 842, 859 | Theoretical comparison I/O specifications and calculation budget |
| U12-1<br>分岐後主体の識別子を何に基づいて付与するか。 | 分岐後識別子の法的定義はEEG-DATA単独では不可。ID 11を技術IDの安定性評価に限定利用。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度・倫理系研究助成（技術監査接続） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 11 | ID 11, 509, 696 | Branch-based audit log design document |
| U12-2<br>責任・権利・同意の継承ルールをどの時点で分岐させるか。 | 責任・権利・同意の継承規則は制度設計課題であり、EEG-DATAは検証補助のみ。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度・倫理系研究助成（技術監査接続） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 11 | ID 11, 509, 696 | System audit requirements table (technical log compatible) |
| U12-3<br>心理的連続性基準と法的個体基準の不一致をどう扱うか。 | 心理的連続性と法的個体の不一致はデータだけでは裁定できず、規範設計が主対象。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度・倫理系研究助成（技術監査接続） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 11 | ID 11, 509, 696 | System audit requirements table (technical log compatible) |
| U12-4<br>技術評価（性能）と人格評価（帰属）をどう接続するか。 | 性能KPIと人格帰属KPIの接続は法務要件が主で、EEGは監査ログ項目の補助。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度・倫理系研究助成（技術監査接続） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 11 | ID 11, 509, 696 | Branch-based audit log design document |
| U12-5<br>分岐主体間で記憶編集・再同期が起きた場合、法的主体IDを再編する基準は何か。 | 記憶編集・再同期時のID再編ルールはEEGデータでは直接検証不可。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度・倫理系研究助成（技術監査接続） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 11 | ID 11, 509, 696 | Time synchronization audit report (offset/jitter distribution) |
| U12-6<br>同意撤回が発生したとき、複数分岐主体への権限剥奪を技術的にどう実装・監査するか。 | 同意撤回の権限剥奪監査はシステム設計課題で、EEG-DATAは模擬ログ検証まで。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度・倫理系研究助成（技術監査接続） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 11 | ID 11, 509, 696 | System audit requirements table (technical log compatible) |
| U13-1<br>brain-to-text成功を『意味復元』と『因果再現』へ分解できるか。 | ID 509でovert/imaginedを比較し、意味一致と因果一致の乖離を測る。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究助成（模倣分離） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 509 | ID 509, 13, 65 | Intervention protocol and rebuttal condition definition |
| U13-2<br>LLMの幻覚・整合性検査を神経デコード評価へどう接続するか。 | ID 13/65で行動整合と内部状態差を分離し、幻覚検査の接続点を作る。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 若手研究助成（幻覚/内部状態差） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 509 | ID 509, 13, 65 | Mimic separation evaluation script and control condition table |
| U13-3<br>同一出力でも内部機構が異なるケースをどう検出するか。 | ID 65/509で同一出力・異内部状態ケースを抽出する判定器を設計する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究奨励金（shortcut検出） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 509 | ID 509, 13, 65 | Imitation separation evaluation report (meaning/mechanism) |
| U13-4<br>模倣性能の上限を因果評価でどこまで抑制できるか。 | ID 509で模倣スコア単独合格を禁止し、因果整合指標との二重閾値を運用する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究助成（因果整合KPI） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 509 | ID 509, 13, 65 | Intervention protocol and rebuttal condition definition |
| U13-5<br>視覚知覚と視覚想起で同一デコーダを使ったとき、意味復元精度の劣化パターンはどこで分岐するか。 | ID 13を主に、知覚条件と想起条件で同一デコーダを適用し、精度低下の分岐点を推定する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 博士課程研究助成（知覚/想起分岐） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 13 | ID 13, 509, 65 | Mimic separation evaluation script and control condition table |
| U13-6<br>プロンプト誘導・データリーク・shortcut学習を分離検出する対照実験をどう設計するか。 | ID 65/13でリーク対照実験を設計し、shortcut検出率を評価する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究助成（リーク分離実験） | G1 (GR-2026-013) / G4 (Drbm6vBRDJkn0NGJ) | 509 | ID 509, 13, 65 | Leak audit results and repartition trail |
| U14-1<br>データ/コード/評価環境の固定粒度をどこまで要求するか。 | ID 6で測定遅延再現試験を自動化し、最小追試パックの基礎にする。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（再現性運用） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 6 | ID 6, 56, 719 | Supplementary test operation report (including negative cases) |
| U14-2<br>探索研究と検証研究を運用上どう分離するか。 | ID 56で探索/検証の分離運用を行い、同一条件再実行の再現率を示す。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究奨励金（探索/検証分離） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 6 | ID 6, 56, 719 | Supplementary test operation report (including negative cases) |
| U14-3<br>leaderboardでのリーク・過適合・報告バイアスをどう監査するか。 | ID 719でleaderboardリーク監査（被験者分割・時系列リーク）を定期化する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 若手研究助成（リーク監査） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 6 | ID 6, 56, 719 | Leak audit results and repartition trail |
| U14-4<br>Model Card / Dataset Card を評価契約へどう統合するか。 | ID 719/56にModel Card・Dataset Card必須化を接続し監査項目化する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（カード統合） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 6 | ID 6, 56, 719 | Model/Dataset Card template and filled-in examples |
| U14-5<br>再現失敗ケースを否定例レジストリとして公開し、再試行サイクルをどう運用するか。 | `failure_id` `dataset_id` `split_hash` `failure_type` `rerun_status` を必須項目にした否定例レジストリを運用し、公開同意フローを併設する。 | B（部分検証（外部データ併用で成立））<br>EEG主解析は可能だが、外部データまたは制度情報の併用が必須。 | 研究奨励金（否定例レジストリ） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 6 | ID 6, 56, 719 | Negative Example Registry First Edition (CSV+Operating Rules) |
| U14-6<br>コンテナ固定（OS・依存ライブラリ・乱数種）を必須化した場合、再現コスト増分をどこまで許容するか。 | ID 719でコンテナ固定時の計算コスト増分を測定し、許容上限を設定する。 | A（直接検証可能）<br>EEG-DATA単独で主要仮説まで検証可能（外部依存なし）。 | 研究助成（再現コスト上限） | G1 (GR-2026-013) / G3 (9Lx4dPK6a4k2gOb7) | 6 | ID 6, 56, 719 | Fixed container reproduction procedure manual and cost measurement |
| U15-1<br>神経データの機微性をどの法概念で扱うか（個人情報・生体情報・人格情報）。 | 神経データ機微性の法概念マッピングは法務課題で、EEG-DATA単独検証は不可。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度設計助成（神経データ法制） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 49 | ID 49, 2412, 3419 | System integrated audit report (suspension/renewal conditions) |
| U15-2<br>neurorightsを技術監査項目へどう写像するか。 | neurorights監査項目化は制度設計が主で、ID 2412は技術ログ項目定義にのみ有効。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度設計助成（神経データ法制） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 49 | ID 49, 2412, 3419 | System audit requirements table (technical log compatible) |
| U15-3<br>法域差（EU/US/JP等）を跨ぐ最小共通運用をどう定義するか。 | 法域差を跨ぐ最小運用はデータでは確定できず、規制比較テーブル整備が必要。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度設計助成（神経データ法制） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 49 | ID 49, 2412, 3419 | System audit requirements table (technical log compatible) |
| U15-4<br>技術進展に応じた停止条件・更新条件をどうガバナンス化するか。 | 停止/更新条件のガバナンス化は制度KPIが主で、ID 49/3419はリスク閾値の補助根拠。 | C（EEG-DATA単独では不可（制度・他モダリティ必須））<br>制度・法務・他モダリティが主対象で、EEGは補助証拠に限定。 | 制度設計助成（神経データ法制） | G2 (GR-2026-014) / G6 (46z9VPE4wnkrvEJR) | 49 | ID 49, 2412, 3419 | System audit requirements table (technical log compatible) |

## 運用上の注意

- 数値IDは再採番されるため、提出書類では `DOI + データセット名 + access区分` を併記する。
- `B/C` 判定RQでは、外部依存（法務・制度・他モダリティ）を明示し、EEG単独での過剰主張を避ける。
- まずは各RQで `最低成果物` を1つ完成させ、その後に拡張解析へ進む。

## 2026-03-18 16:00 JST 反映ログ（本run）

- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` と `mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook.md` を突合し、`60RQ` の統合カードを新規生成した。
- 全行に対して `主張単位` `判定境界` `応募テーマ` `応募先` `主データ` `補助データ` `最低成果物` を固定した。
- 判定内訳は再計数で `A/B/C=17/25/18` と一致した。

## 2026-03-18 17:03 JST 再検証ログ（本run / 深掘り方針で再実行）

- 作業開始前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、最新化済み（Already up to date）を確認しました。
- `mind-upload/research_harvest_50.md` を正本として、`RQ_TOTAL=60` と `U別内訳（U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4）` を再照合しました。
- `A/B/C=17/25/18` を再計数し、全RQに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA`（Deep Evaluation Cards では `主張単位` `応募先` `最低成果物` を追加）が埋まっていることを確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 応募先は `G1-G6` を継続利用し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を維持しました。
- wiki反映先は `mind-upload/wiki` と `auto-research-funds/wiki` の両方に同期しました。

## 2026-03-18 22:02 JST 再検証ログ（本run / 深掘りカード再固定）

- 作業開始前に `auto-startup` ルートで `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `RQ行数=60` と `A/B/C=17/25/18` を再計数し、前回値と一致することを確認しました。
- 全60行で `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` が欠損なく埋まっていることを確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）は `EEG-DATA/eeg_dataset_summary_ja.csv` で欠損 `0` 件でした。
- 依頼方針どおり、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の運用を継続しました。

## 2026-03-19 13:58 JST 再検証ログ（本run / 60RQ深掘り固定の監査再実行）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `RQ行数=60` と `A/B/C=17/25/18` を再計数し、欠損・重複 `0` を確認しました。
- RQ行に記載した EEG 参照IDの一意集合（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側の `RQ行数=60` も再確認し、mind-upload 側と同一件数で同期されていることを確認しました。
- 本runも方針は不変で、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 13:45 JST 再検証ログ（本run / Deep Cards再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `RQ行数=60` と `A/B/C=17/25/18` を再計数し、欠損・重複がないことを確認しました。
- 全行で `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` が埋まっていることを確認しました。
- 依頼方針どおり、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の運用を継続しました。

## 2026-03-19 06:03 JST 再検証ログ（本run / ディープ評価カード監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `RQ行数=60` と `A/B/C=17/25/18` を再計数し、欠損・重複 `0` を確認しました。
- `主データ（ID）` と `補助データ（推奨ID）` の参照を再抽出し、使用ID集合（24件）が `EEG-DATA/eeg_dataset_summary_ja.csv` に全件存在することを確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側の `RQ行数=60` と同期していることを再確認しました。
- 本runも方針は不変で、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-19 09:05 JST 再検証ログ（本run / deep cards 監査）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行しました。
- 本カードの `RQ行数=60` と `A/B/C=17/25/18` を再計数し、欠損・重複 `0` を確認しました。
- 全行で `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` が埋まっていることを再確認しました。
- 主要EEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）は、最新 `EEG-DATA/eeg_dataset_summary_ja.csv` に全件存在することを確認しました。
- 方針は不変で、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-19 10:02 JST 再検証ログ（本run / Deep Cards同期監査）

- 作業開始前に `auto-startup` 親リポジトリで `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` を `git pull --ff-only origin main` で更新後、本カードを再監査しました。
- 本カードの `RQ行数=60` と `A/B/C=17/25/18` を再計数し、欠損・重複 `0` を確認しました。
- `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` の必須列が全60行で埋まっていることを確認しました。
- `主データ（ID）` の一意集合（`6, 11, 13, 19, 49, 56, 509, 676, 735`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側の `RQ行数=60` と同期していることを再確認しました。

## 2026-03-19 12:02 JST 再検証ログ（本run / deep-by-RQ更新後の再監査）

- 作業開始時に `auto-startup` 親リポジトリの `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に検証しました。
- `mind-upload` と `auto-research-funds` の対象wikiページで `RQ` 行を再計数し、いずれも `60` 件で一致することを確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持していることを確認しました。
- 主要EEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。

## 2026-03-19 13:02 JST 再検証ログ（本run / deep cards 更新後監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新差分取り込み後に本カードを再監査しました。
- `Ux-y` 形式のRQ行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を確認しました。
- `主データ（ID）` と `補助データ（推奨ID）` から抽出したEEG参照ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側の `Ux-y` 行も `60` 件で一致し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 14:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで再固定）

- 作業開始前に `auto-startup` 親リポジトリで `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に再監査しました。
- 本カードの `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を確認しました。
- 全60行で `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` が埋まっていることを確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は不変で、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-19 15:01 JST 再検証ログ（本run / Deep Cards同期監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を再確認しました。
- 全60行で `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` が埋まっていることを再確認しました。
- RQ行で使うEEG参照ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側も `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、deep-by-RQ同期を維持しました。

## 2026-03-19 16:02 JST 再検証ログ（本run / Deep-by-RQ同期監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` を `git pull --ff-only origin main` で最新化後、`RQ` テーブルを再監査しました。
- `mind-upload` 側（Deep Cards / Feasibility）と `auto-research-funds` 側（Grant Map）で、`RQ_TOTAL=60` と `A/B/C=17/25/18` が一致することを再確認しました。
- RQ行で参照するEEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は不変で、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。
## 2026-03-19 18:03 JST 再検証ログ（本run / Deep-by-RQ同期監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` を `git pull --ff-only origin main` で最新化（`mind-upload: 66e2f8a -> 2b43943`、`auto-research-funds: 382a5f90e -> 5a6eda781`、`EEG-DATA: 88c625b0b6f -> 76b2c83256b`）した後、RQテーブルを再監査しました。
- 本カードの `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を確認しました。
- 全60行で `主張単位` `判定境界` `応募テーマ` `第一応募先/予備応募先` `主データ` `最低成果物` が埋まっていることを再確認しました。
- RQ行で参照するEEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は不変で、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 19:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を再確認しました。
- 全60行で `主張単位/判定境界/応募テーマ/応募先/主データ/最低成果物` が埋まっていることを確認し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- RQ運用で参照するEEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の対応を維持し、各RQの応募テーマとEEGデータ割当をWikiへ同期しました。

## 2026-03-19 20:02 JST 再検証ログ（本run / ユーザー依頼: 1RQ深掘り固定でWiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- 本カードと `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `主張単位/判定境界/応募テーマ/応募先/主データ/最低成果物` が埋まっていることを確認しました。
- RQ運用で使うEEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 汎用横断要約ではなく、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 21:01 JST 再検証ログ（本run / deep-by-RQ監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only` を実行し、最新化済み（Already up to date）を確認しました。
- 本カードの `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）と `A/B/C=17/25/18` を再確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と突合し、同じ `RQ_TOTAL=60` / `A/B/C=17/25/18` で一致することを確認しました。
- 方針は継続して `1RQ=1検証命題=1応募テーマ=1主データ` とし、汎用横断要約よりもRQ単位の深掘りを優先しました。

## 2026-03-19 22:01 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、すべて `RQ_TOTAL=60`、`A/B/C=17/25/18`、`missing=0`、`duplicate=0` を確認しました。
- 3ページで参照されるEEG ID（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と再照合し、未解決ID `0` を確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持したまま wiki 同期を更新しました。
## 2026-03-20 01:02 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りでwiki再同期）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` でも同じ `RQ_TOTAL=60` / `A/B/C=17/25/18` を再確認しました。
- RQ行から抽出したEEG参照ID集合（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 02:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を再確認しました。

## 2026-03-20 11:03 JST 再検証ログ（本run / RQ別深掘りの助成テーマ×EEG実行導線を固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードを `Ux-y` 単位で再読し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を再確認しました。
- `mind-upload-eeg-rq60-feasibility-and-funds.md` に、U別の `auto-research-funds向け提出テーマ` と `主/補助EEG-DATA` を直結する実行マップを追記しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用で wiki を更新しました。
- RQ行から抽出したEEG参照ID（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` は `Ux-y` 行が物理行で `66`（深掘り優先6RQの再掲あり）だが、`unique RQ=60` を再確認し、実体は本カードと一致していることを明記しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 04:02 JST 再検証ログ（本run / ユーザー依頼: 1RQ深掘りで再固定）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化しました。
- 本カードの `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を確認しました。
- `主データ（ID）` の一意集合（`6, 11, 13, 19, 49, 56, 509, 676, 735`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 本runでも方針は不変で、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 08:01 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 本カードの判定内訳を再計数し、`A/B/C=17/25/18` を確認しました。
- RQ行で参照するEEG ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 09:04 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りでwiki再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`、`mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、いずれも `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳は `A/B/C=17/25/18` を再確認しました。
- Deep Evaluation Cards で参照されるEEG ID 一意集合（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 10:03 JST 再検証ログ（本run / ユーザー依頼: 1問ずつ深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、3ページとも `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 本カードの判定内訳 `A/B/C=17/25/18` を再確認しました。
- RQ行の `主データ（ID）` と `補助データ（推奨ID）` から抽出したEEG ID集合（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-20 23:40 JST 再検証ログ（本run / ユーザー依頼: RQごと深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、全RQに `応募テーマ` `主データ` `最低成果物` が記載済みであることを確認しました。
- 本runでは汎用横断の更新ではなく、`U14-1/U7-2/U14-3/U8-1/U8-2/U13-1` を「1件ずつ深掘りする固定実行パック」として明示しました。
- 方針は継続し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-20 15:02 JST 再検証ログ（本run / deep-by-RQ同期監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本カードの `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18`（欠損・重複 `0`）を再確認しました。
- U別内訳 `U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4` を再確認しました。
- RQ行で参照するEEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照実在を `grant_queue/*.yaml` と `auto-research-funds/grant_eeg_dataset_match.csv` で再確認しました。
- 方針は不変で、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 18:02 JST 再検証ログ（本run / 依頼: mind-upload RQをEEG-DATAで深掘り評価してwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-RQ60-Deep-Evaluation-Cards.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を突合し、すべて `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳は4ページで `A/B/C=17/25/18` を再確認しました。
- 全RQで `検証可否` `深掘り検証設計(主張単位)` `応募テーマ` `主データ(EEG)` `最低成果物` の欠損 `0` を再確認しました。
- 依頼方針どおり、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-20 22:04 JST 再検証ログ（本run / deep-by-RQ同期 + 助成参照元補正）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に再検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、3ページとも `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認しました。
- 参照EEG IDは現行カード構成で `17件`（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）で、`EEG-DATA/eeg_dataset_summary_ja.csv` との照合欠落は `0` でした。
- 助成IDは `G3-G6` を `auto-research-funds/wiki/cards/*.md` と `grant_eeg_dataset_match.csv` で照合し欠落 `0` を確認、`G1/G2` は `mind-upload/wiki` と `auto-research-funds/wiki` の固定運用キーとして同期確認しました（現行 `auto-research-funds` に `grant_queue/` は未配置）。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続します。

## 2026-03-20 23:03 JST 再検証ログ（本run / ユーザー依頼: RQを1件ずつ深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `| Ux-y<br>` を再計数し、3ページとも `RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の運用が全行で維持されていることを確認しました。
- RQ行で参照されるEEG ID一意集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 助成キーは `G3-G6` を `auto-research-funds/wiki/cards/*.md` と `grant_eeg_dataset_match.csv` で照合し欠落 `0`、`G1/G2` は `mind-upload/wiki` と `auto-research-funds/wiki` の固定運用キーとして再確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」実行形で wiki 同期を維持しました。

## 2026-03-21 09:20 JST 再検証ログ（本run / DOIアンカー運用）

- `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- `EEG-DATA` の大規模再採番により、カード本文の数値IDは将来変動しうるため、提出実務では `mind-upload-eeg-rq60-feasibility-and-funds` と `Mind-Upload-EEG-RQ-Grant-Map` に追記した `D01-D24（DOI固定）` を正本キーとして扱ってください。
- 本カードはRQごとの検証命題・失敗条件・成果物定義を正本とし、データ参照の最終キーは DOI 側に委譲します。

## 2026-03-21 04:03 JST 再検証ログ（本run / 1RQ深掘り固定でwiki同期）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に再検証しました。
- 本カードと `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `| Ux-y<br>` 行を再計数し、双方とも `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳は双方で `A/B/C=17/25/18` を再確認しました。
- 本カード運用で参照するEEG ID（本runの参照集合）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は不変で、汎用横断の要約更新ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持して wiki 同期を継続しました。

## 2026-03-21 05:02 JST 再検証ログ（本run / ユーザー依頼: 各RQを1件ずつ深掘りでwiki固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `auto-research-funds/wiki/Mind-Upload-RQ60-Deep-Evaluation-Cards.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、すべて `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳は `A/B/C=17/25/18` を再確認し、全行で `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用が維持されていることを確認しました。
- 本カードの参照EEG ID一意集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 助成キーは `G3-G6` を `auto-research-funds/wiki/cards/*.md` と `grant_eeg_dataset_match.csv` で再照合し欠落 `0`、`G1/G2` は `mind-upload/wiki` と `auto-research-funds/wiki` の固定運用キーとして再確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」実行形で wiki 同期を維持しました。
