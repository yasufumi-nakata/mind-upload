# Mind-upload RQ60 × EEG-DATA 検証可否と助成テーマ（深掘り版）

> RQごとに検証設計と応募テーマまで接続する
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-19 / 位置づけ: RQ-by-RQ Deep Dive

---

# Mind-upload RQ60 × EEG-DATA 検証可否と助成テーマ（深掘り版）

> 1問ずつ深掘りして、検証設計と応募テーマまで接続する
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-19 / 位置づけ: RQ-by-RQ Deep Dive

## このページの役割
このページは research_harvest_50 の60 RQを対象に、EEG-DATAで解ける範囲をA/B/Cで判定し、各RQごとの検証設計・応募テーマ・使うデータセットIDをまとめた実務版です。

## 正確さの前提
U10/U12/U15の一部RQはEEG単独で解決できないため、不可と判定し、必要な外部要件を明記します。

## 公開ページへ戻る
- [文献地図](https://mind-upload.com/research_harvest_50.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [RQ60 申請プレイブック](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook)
- [Issue](https://mind-upload.com/issue.html)

## 関連 Wiki
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 判定を実験仕様に落とすときの基準。
- [Wiki: 反事実・介入検証](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - U4/U13の因果評価に直結。
- [Wiki: データ分割とリーク](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - U14の再現性監査に必要。

---

## 判定ルール

- `A` = EEG-DATAのみで主要仮説まで直接検証可能
- `B` = EEG-DATAで中核の一部は検証可能。ただし外部データ/制度情報の併用が必要
- `C` = EEG-DATA単独では解けない（制度設計・法規・代謝/熱計測などが主対象）

## 先に結論（60RQの内訳）

- `A`: 17件
- `B`: 25件
- `C`: 18件

## 今回の再検証ログ（2026-03-18）

本ページは、`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の60行を1行ずつ読み、各RQについて下記4点が埋まっていることを再確認した上で更新しています。

1. `検証可否`（`A/B/C` 判定と境界条件）
2. `auto-research-funds向け応募テーマ`
3. `推奨EEG-DATA`（主データセットID）
4. `提出成果物`（最低限の実装/監査アウトプット）

再検証時の固定ルール:

- 汎用横断の要約は作らず、`1RQ=1検証命題=1応募テーマ=1主データ` を優先
- `C` 判定RQは「EEG単独で不可」の理由（法務/制度/他モダリティ）を明記
- データセット参照はID再採番の影響を避けるため、提出時は `DOI + dataset名 + access区分` を必ず併記

## auto-research-fundsで使う応募レーン（本ページで参照した根拠）

- `若手研究助成` / `研究奨励金` / `一般研究助成` / `共同研究助成` / `博士課程研究助成`
- 根拠ファイル: `auto-research-funds/data/docs/research_funding_manual_additions_2026-03-14_run132.md`
- 根拠ファイル: `auto-research-funds/data/docs/research_funding_keio_grad_underfilled_2026-02-17.md`
- 根拠ファイル: `auto-research-funds/data/docs/research_funding_daily_codex_2026-03-07.md`

### 実務で使う助成キー（IDつき）

- `G1`: `GR-2026-013`（`grant_queue` 上の応募トラックID / 技術実証・再現性中心）
- `G2`: `GR-2026-014`（`grant_queue` 上の応募トラックID / 統合検証・社会実装中心）
- `G3`: `9Lx4dPK6a4k2gOb7`（研究助成（国内））
- `G4`: `Drbm6vBRDJkn0NGJ`（研究助成）
- `G5`: `871pw3rLjNPKgqA0`（研究助成金）
- `G6`: `46z9VPE4wnkrvEJR`（学術・研究助成）

### 助成キー実体（根拠系統を分離）

| Key | 制度名 | 締切窓（根拠種別） | RQ60での使いどころ |
|---|---|---|---|
| G1 | `GR-2026-013`（応募トラックID。名称は `grant_queue/GR-2026-013.yaml` を正本） | `grant_queue` 管理値（都度更新） | `U1/U4/U7/U13/U14` の技術検証を、再現性パッケージ付きで短中期成果として出す。 |
| G2 | `GR-2026-014`（応募トラックID。名称は `grant_queue/GR-2026-014.yaml` を正本） | `grant_queue` 管理値（都度更新） | `U0/U3/U8/U10/U11/U12/U15` の統合設計・長期テーマを博士計画として束ねる。 |
| G3 | 大川情報通信基金 研究助成 (`9Lx4dPK6a4k2gOb7`) | 2025年度実績ベースの想定窓（2026年は要再確認） | 再現基盤・データ標準化寄りの `A` 判定RQ（U7/U14）を補助応募として出す。 |
| G4 | 成茂神経科学研究助成基金 (`Drbm6vBRDJkn0NGJ`) | 2022/11/18〜2023/02/17実績ベース（制度継続状況は不明） | 方法論高度化（因果・逆問題・デコード監査）として `U1/U4/U11/U13/U14` を中心に出す。 |
| G5 | 日本産業科学研究所 研究助成金 (`871pw3rLjNPKgqA0`) | 2025年度実績ベースの想定窓（2026年は要再確認） | `U8` の閉ループ運用・ドリフト対策の運用研究を小中規模実装として出す。 |
| G6 | 住友電工グループ社会貢献基金 学術・研究助成 (`46z9VPE4wnkrvEJR`) | 2025年度実績ベースの想定窓（2026年は要再確認） | `C` 判定RQ（U3/U10/U12/U15）で必要な制度・多モーダル連携の準備研究に使う。 |

- 参照ルール: `G1-G2` は `grant_queue/*.yaml`、`G3-G6` は `auto-research-funds/wiki/cards` と `grant_eeg_dataset_match.csv` を正本として扱います。

### U別の第一応募先/予備応募先（運用固定）

| U | 第一応募先 | 予備応募先 |
|---|---|---|
| U0 | G2 | G3 |
| U1 | G1 | G4 |
| U3 | G2 | G6 |
| U4 | G1 | G4 |
| U7 | G1 | G3 |
| U8 | G2 | G5 |
| U10 | G2 | G6 |
| U11 | G2 | G4 |
| U12 | G2 | G6 |
| U13 | G1 | G4 |
| U14 | G1 | G3 |
| U15 | G2 | G6 |

### A/B/C判定別の提出戦略

- `A`: EEG-DATAだけで主解析まで完結。`G1/G3` 優先で「再現性・実装速度」を前面化する。
- `B`: EEG主解析 + 外部要件が必要。`G2/G4/G5` を使い「統合検証計画」を明記する。
- `C`: EEGは監査ログ/補助証拠として利用。`G2/G6` で制度・理論連携トラックとして出す。

### RQタイプ別のEEG-DATA選定テンプレ（1問ずつ深掘りするための固定入口）

| RQタイプ（該当U） | 優先するEEG資源軸 | 入口レポート（EEG-DATA） | まず使うデータ例 |
|---|---|---|---|
| 思考/運動意図の安定デコード（`U0/U8/U13`） | `motor imagery` `cross-session` `cross-subject` | `TARGET_TASK_REPORT.md` `BENCHMARK_SETUP_REPORT.md` | ID `6, 11, 696, 719` |
| 言語/意味復元と模倣分離（`U13`） | `reading-RSVP` `naturalistic stimulus` `reconstruction/decoding` | `LANGUAGE_PARADIGM_REPORT.md` `TASK_FORMULATION_REPORT.md` | ID `509, 13, 65` |
| 意識状態・睡眠・失敗条件（`U11/U15`） | `resting-state` `sleep` `EEG-fMRI` | `PARADIGM_FAMILY_REPORT.md` `MULTIMODAL_SETUP_REPORT.md` | ID `735, 842, 859` |
| 高解像度・逆問題・因果介入（`U1/U4`） | `high-density channel` `stimulation` `ground-truth` | `RECORDING_MODALITY_REPORT.md` `EXPERIMENT_REUSE_READINESS.md` | ID `56, 676, 1839` |
| 多モーダル整合と再現性運用（`U7/U14`） | `multimodal alignment` `access` `benchmark` | `MULTIMODAL_SETUP_REPORT.md` `EXPERIMENT_SHORTLISTS.md` | ID `6, 56, 783, 4878` |

### auto-research-funds向けテーマレーン拡張（G1-G6に加える候補）

| レーン | 追加候補ID（auto-research-funds） | このページでの使い方 |
|---|---|---|
| 神経・認知・臨床EEG | `1geD73ZENwB8yaor`, `lEYmRP97ng3perjO` | `U11/U15` で「臨床評価補助バイオマーカー化」を前面に出す。 |
| 医工学・AI・信号処理 | `1geD73Z9K2B8yaor` | `U1/U7/U13/U14` で「EEG分類・異常検知・再現性基盤」を強調。 |
| 高齢社会・リハビリ | `QKYgNPxZxN38bO1Z` | `U8/U11/U15` の睡眠・覚醒・注意維持介入の実装テーマに接続。 |
| 社会実装・防災・地域ヘルス | `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor` | `U15` の制度統合・現場運用監査トラックとして提出。 |

### RQを1問ずつ深掘りするときの提出フォーマット（本ページ運用ルール）

各RQで下記4点を必ず埋めてから応募文章へ転記します（汎用要約ではなくRQ単位運用）。

1. `主張単位`:
`このRQで検証する最小主張` を1文で固定（例: 「U4-2は最小介入因果主張まで」）。
2. `EEG-DATA単独で言える範囲`:
`A/B/C` の判定理由を、データID付きで1文で固定（例: `ID 56` が ground-truth を提供）。
3. `外部依存`:
不足モダリティ、制度判断、法務判断のどれが不足かを明記し、境界を曖昧にしない。
4. `提出成果物`:
応募時点で必ず提出できる実物を固定（`解析スクリプト`、`分割規則`、`失敗条件定義`、`再現ログ`）。

## EEG-DATA 参照データセット（本ページで使用）

> 重要（2026-03-15 08:00 JST 追記）:
> `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID` は再採番で変動するため、`ID -> データセット名` を固定参照として扱わないでください。応募書類・再現ログでは、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `D1-D16（DOI固定）` を正とし、`DOI + データセット名 + access区分` を併記します。

| ID | データセット |
|---|---|
| 6 | Acquisition delay of wireless EEG |
| 11 | CSTE (cross-session/task EEG biometrics) |
| 13 | Multimodal Fusion EEG + Eye-tracking |
| 16 | Deep Nonparametric Bayesian Multimodal Sensor Fusion |
| 19 | HiPi pinprick stimulation EEG |
| 29 | Longitudinal dyslexia ERP |
| 39 | MAD multimodal affective dataset |
| 49 | Physiological Indicators of Driver Sleepiness |
| 56 | Intracerebral stimulation + HD-EEG (ground-truth) |
| 65 | VICODEV driving distraction multimodal |
| 509 | 3M-CPSEED overt/silent/imagined speech EEG |
| 676 | Simultaneous EEG-fMRI XP1 |
| 696 | Longitudinal MI-BCI + spinal stimulation |
| 719 | Ubiquitous P300 benchmark |
| 735 | PK-NMM propofol anesthesia EEG simulation |
| 783 | Simultaneous EEG-fNIRS working memory |
| 842 | AAUWSS wearable sleep study |
| 859 | DoC EEG biomarker pilot |
| 1011 | AlphaDirection1 EEG+ECG+PPG |
| 1839 | CerebellarTMSEEGData |
| 1972 | Closed-loop auditory stimulation (REM) |
| 2412 | NeuroSimo closed-loop EEG/EMG-guided TMS |
| 3419 | rTMS responder/non-responder EEG |
| 4878 | EEG+PPG+GSR rehabilitation fatigue |

## RQ深掘り根拠メモ（U単位）

| U | 対象RQ数 | 主に使うEEG-DATA | この組み合わせにした理由 | この時点の限界 |
|---|---:|---|---|---|
| U0 | 4 | ID 11 / 29 / 696 | セッション横断・縦断・訓練後変化を同時に見られるため、操作的同一性の閾値設計を進めやすい。 | 生体同定の技術同一性が中心で、人格同一性の規範判断までは扱えない。 |
| U1 | 4 | ID 56 / 676 / 1839 | 既知刺激位置や同時計測を使って、逆問題の誤差・不確実性伝播を実測しやすい。 | 臨床・特定課題条件のデータに寄るため、一般化可能性は追加検証が必要。 |
| U3 | 6 | ID 13 / 16 / 39 | EEG単独とマルチモーダル拡張の性能差を比較し、主体境界拡張の必要量を推定できる。 | グリンパ系・免疫監視の直接計測がなく、境界最終判定はEEG単独で完結しない。 |
| U4 | 4 | ID 19 / 56 / 1839 | 制御刺激と応答差を使って、観測一致ではなく介入一致の反証可能な試験を組める。 | 高次認知までの因果同値を単独で保証するには、追加モダリティ・追加介入が要る。 |
| U7 | 6 | ID 6 / 676 / 783 / 4878 | 時刻同期・前処理差分・モダリティ欠損を同じ枠で監査でき、再現性運用に直結する。 | タスクが限定的なため、全領域共通の標準契約にするには運用拡張が必要。 |
| U8 | 6 | ID 6 / 1972 / 2412 / 696 | 遅延・位相・再較正・ドリフトの閉ループ課題が揃い、安全域KPIを実測で定義できる。 | 睡眠・TMS・運動イメージに偏るため、日常運用一般への外挿には追加試験が必要。 |
| U10 | 4 | ID 735 / 783 / 1011 | 神経活動と代謝proxyを結び、情報熱力学の理論整合を段階的に検証しやすい。 | 熱散逸の直接計測がないため、Landauer下限の主張は理論・proxyレベルに留まる。 |
| U11 | 4 | ID 735 / 842 / 859 | 麻酔・睡眠・DoCの状態差で、意識指標近似の順位保存と失敗条件を比較しやすい。 | IIT厳密計算や理論間の最終裁定は、計算量・外部設計制約が残る。 |
| U12 | 6 | ID 11 / 509 / 696 | 分岐条件や表現ドリフトを技術IDとして追跡し、制度議論に渡す監査ログを作れる。 | 責任・権利・同意の規範判断は制度設計が主で、EEG単独で決定できない。 |
| U13 | 6 | ID 509 / 13 / 65 | overt/imagined差と行動・生理差を併用し、模倣成功と内部機構差を分離しやすい。 | 言語・運転など特定文脈が中心で、一般模倣分離ベンチ化には追加タスクが必要。 |
| U14 | 6 | ID 6 / 56 / 719 | 遅延再現・ground-truth・benchmarkを組み合わせ、追試可能性を契約化しやすい。 | 公開同意や否定例公開フローなど、制度運用面は別途実装が必要。 |
| U15 | 4 | ID 49 / 2412 / 3419 | 安全停止・治療継続判断に近い技術ログを作れ、制度KPIの実装土台にしやすい。 | neurorights・法域差の最終運用は法務設計が主で、データ単独では完了しない。 |

## U0 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U0-1<br>同一性判定を『観測一致』と『介入応答一致』に分離したとき、どちらを必要条件・十分条件に置くか。 | A（直接検証可能） | 観測一致（EEG特徴量）と介入一致（刺激/課題変更時の応答）を分離して二軸ROCを作る。 | 若手研究助成（同一性KPI） | ID 11, 29, 696 |
| U0-2<br>時間同期（ms単位）と状態表現（行動・神経活動・生理）の対応をどう固定するか。 | A（直接検証可能） | ID 676/4878で時刻同期ずれと状態特徴量の崩れを同時に計測し、固定ルールを定義する。 | 研究奨励金（縦断同一性） | ID 11, 29, 696 |
| U0-3<br>同一性判定の閾値をタスク別にどう設定し、過学習モデルをどう除外するか。 | A（直接検証可能） | ID 11/696でタスク別に同一性閾値を推定し、過学習モデルはセッション外性能で除外する。 | 博士課程研究助成（個体同定） | ID 11, 29, 696 |
| U0-4<br>分岐/複製ケースでの『同一個体』定義をどの評価軸に帰着させるか。 | B（部分検証（外部データ併用で成立）） | ID 11/509で「同一個体判定」指標を生体同定精度に限定して運用限界を明記する。 | 共同研究助成（同一性×責任） | ID 11, 29, 696 |

## U1 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U1-1<br>EEG/MEG逆問題での不良設定性を、どの事前分布で制御するか。 | A（直接検証可能） | ID 56の既知刺激位置を使って、事前分布ごとの逆解誤差を比較する。 | 研究助成（逆問題ベンチ） | ID 56, 676, 1839 |
| U1-2<br>頭蓋導電率・電極配置・ノイズ構造の不確実性を、推定不確実性へどう伝播させるか。 | A（直接検証可能） | ID 56/1839で電極欠損・ノイズ注入を行い、不確実性伝播の校正曲線を作る。 | 若手研究助成（不確実性推定） | ID 56, 676, 1839 |
| U1-3<br>同じデータで異なる逆解法（MNE, beamformer, Champagne 等）が乖離した場合の判定規則をどう置くか。 | B（部分検証（外部データ併用で成立）） | ID 56/676でMNE/beamformer/Champagneの乖離率をタスク別に比較する。 | 研究奨励金（手法比較） | ID 56, 676, 1839 |
| U1-4<br>推定値だけでなく、信頼区間/後方分布を公開基準に含めるか。 | B（部分検証（外部データ併用で成立）） | 逆問題の信頼区間公開可否を、ID 56での後方分布再現性で評価する。 | 博士課程研究助成（後方分布公開） | ID 56, 676, 1839 |

## U3 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U3-1<br>ニューロン中心モデルに対して、グリア/体液性調節を追加した際の予測改善量をどう測るか。 | B（部分検証（外部データ併用で成立）） | ID 13/39でEEG単独 vs マルチモーダルの性能差を測り、境界拡張の必要量を推定する。 | 探索的若手研究助成（境界 proxy） | ID 13, 16, 39 |
| U3-2<br>connectome完全性と機能予測性能の関係を、種横断でどう比較するか。 | B（部分検証（外部データ併用で成立）） | EEG-DATA単独ではconnectome完全性を直接検証できないため、補助指標としての再現性評価に限定する。 | 探索的若手研究助成（境界 proxy） | ID 13, 16, 39 |
| U3-3<br>身体・環境結合を除去したモデルで失われる機能をどう定量化するか。 | B（部分検証（外部データ併用で成立）） | ID 16/39で身体・環境ループを含む条件差を比較し、除去時の性能低下を測る。 | 探索的若手研究助成（境界 proxy） | ID 13, 16, 39 |
| U3-4<br>『必要最小構成』の判定を理論的主張ではなくデータでどう固定するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 必要最小構成の最終判定はEEG単独では不可。まずID 13/39で代理KPIを固定する。 | 探索的若手研究助成（境界 proxy） | ID 13, 16, 39 |
| U3-5<br>glymphatic/meningeal lymphatic 系を含むとき、予測精度と説明可能性はどの程度改善するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | glymphatic/meningeal系はEEG-DATAに直接計測がなく、同時代謝データ併用前提の探索扱い。 | 探索的若手研究助成（境界 proxy） | ID 13, 16, 39 |
| U3-6<br>免疫監視（髄膜免疫・炎症性シグナル）を除外したモデルは、どの時点で長期予測が破綻するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 免疫監視除外モデルの長期破綻はEEG-DATAだけでは不可。縦断臨床データの外部連携が必要。 | 探索的若手研究助成（境界 proxy） | ID 13, 16, 39 |

## U4 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U4-1<br>観測データ由来の相関を因果グラフへ持ち上げる識別条件は何か。 | B（部分検証（外部データ併用で成立）） | ID 19/1839で入力操作に対する応答差を計測し、観測相関との差を分離する。 | 研究助成（介入同値） | ID 19, 56, 1839 |
| U4-2<br>介入実験（刺激・抑制・入力撹乱）で検証可能な最小因果主張は何か。 | A（直接検証可能） | ID 56の既知介入で最小因果主張を事前登録し、再現可否で判定する。 | 若手研究助成（ground-truth介入） | ID 19, 56, 1839 |
| U4-3<br>active inferenceやDCMの理論予測を、反事実評価にどう接続するか。 | B（部分検証（外部データ併用で成立）） | ID 676を主に、介入あり/なしで反事実誤差（PEHE）と予測尤度差を比較し、理論順位を固定する。 | 研究奨励金（反事実評価） | ID 19, 56, 676 |
| U4-4<br>同値判定の失敗条件（falsification）をどの水準で宣言するか。 | B（部分検証（外部データ併用で成立）） | ID 19/56で `ΔAUC > 0.03` または `介入応答の符号反転率 > 10%` を失敗宣言閾値として事前登録する。 | 共同研究助成（反証設計） | ID 19, 56, 1839 |

## U7 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U7-1<br>BIDS拡張で同期・QC・刺激ログをどこまで必須化するか。 | A（直接検証可能） | ID 676/783で `clock offset` `sampling drift` `stimulus onset` `QC fail code` の4項目を必須化し、欠落時は不採択にする。 | 研究助成（マルチモーダル標準化） | ID 676, 783, 4878 |
| U7-2<br>LSL等の時刻同期誤差を検証可能な指標に落とせるか。 | A（直接検証可能） | ID 6/676でジッタ/遅延の基準値を算出し、閾値超過を自動警告する。 | 若手研究助成（同期監査） | ID 676, 783, 4878 |
| U7-3<br>アーチファクト除去（ASR, ZapLine等）の設定差が結果へ与える影響をどう監査するか。 | A（直接検証可能） | ID 676/4878で前処理設定差分を再実行し、結果ドリフトを定量化する。 | 研究奨励金（前処理差分） | ID 676, 783, 4878 |
| U7-4<br>モダリティ間アライメント失敗時の再計測/除外基準をどう固定するか。 | A（直接検証可能） | ID 676/783でアライメント失敗時の再計測/除外条件を判定木化する。 | 共同研究助成（再計測基準） | ID 676, 783, 4878 |
| U7-5<br>前処理差分をCIで自動比較する場合、どの再現率低下をリリースブロック閾値にするか。 | A（直接検証可能） | ID 676で前処理CIを回し、基準パイプライン比で `再現率 -5pt` 以上低下を release block 閾値に固定する。 | 研究助成（CI再現性） | ID 676, 783, 4878 |
| U7-6<br>モダリティ欠損（EEG欠損・fMRI欠損）条件でも同等結論を保てる最小観測セットは何か。 | A（直接検証可能） | ID 676/783でEEG欠損・fMRI/fNIRS欠損をシミュレートし最小観測セットを求める。 | 研究助成（欠損ロバスト性） | ID 676, 783, 4878 |

## U8 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U8-1<br>閉ループBCIの遅延許容域を制御理論的にどう同定するか。 | B（部分検証（外部データ併用で成立）） | ID 6/1972で遅延・位相ずれに対する `安定率` `停止介入率` `回復時間` を測り、許容域を3指標で定義する。 | 若手研究助成（閉ループ安定化） | ID 6, 1972, 2412, 696 |
| U8-2<br>オンライン較正と概念ドリフト対策をどう組み込むか。 | B（部分検証（外部データ併用で成立）） | ID 2412/696でオンライン再較正の頻度と性能安定性を比較する。 | 研究奨励金（再較正） | ID 6, 1972, 2412, 696 |
| U8-3<br>個体差と日内変動をまたぐ安定性をどの指標で評価するか。 | B（部分検証（外部データ併用で成立）） | ID 696で個体内・個体間分散を分けて長期安定性KPIを設計する。 | 博士課程研究助成（長期ドリフト） | ID 6, 1972, 2412, 696 |
| U8-4<br>異常検知とフェイルセーフを評価契約へどう組み込むか。 | B（部分検証（外部データ併用で成立）） | ID 2412/1972で異常検知遅延とフェイルセーフ発動時間を測る。 | 共同研究助成（フェイルセーフ） | ID 6, 1972, 2412, 696 |
| U8-5<br>ヒューマンオーバーライドを導入したとき、誤作動率と回復時間をどうKPI化するか。 | B（部分検証（外部データ併用で成立）） | ID 2412で手動オーバーライド時の誤作動率と回復時間をKPI化する。 | 研究奨励金（オーバーライド） | ID 6, 1972, 2412, 696 |
| U8-6<br>週〜月スケール運用での再学習頻度を、性能劣化と安全余裕のトレードオフでどう最適化するか。 | B（部分検証（外部データ併用で成立）） | ID 696/2412で再学習間隔を変え、性能劣化と安全余裕のトレードオフを推定する。 | 研究助成（再学習最適化） | ID 6, 1972, 2412, 696 |

## U10 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U10-1<br>Landauer下限を神経計算でどう適用/解釈するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | Landauer下限の直接検証はEEG-DATA単独では不可。ID 735を理論整合の事前検証に使う。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |
| U10-2<br>非平衡熱力学指標と神経情報処理効率の対応をどう定義するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 非平衡熱力学指標の主評価は不可。ID 783/1011で代謝proxyとの弱い相関を探索する。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |
| U10-3<br>理論式を実データ（神経活動・代謝）へ落とし込む観測設計をどう作るか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 神経活動+代謝同時計測はID 783で部分検証可能だが、熱散逸実測は外部計測が必要。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |
| U10-4<br>WBE計算コスト評価に熱力学制約をどう統合するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | WBE計算コストへ熱制約を統合する実証はEEG-DATA外。ID 735でモデル妥当性確認まで。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |

## U11 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U11-1<br>理論間で比較可能な入出力仕様をどう定義するか。 | B（部分検証（外部データ併用で成立）） | ID 842/859で PCI近似・LZ複雑性・摂動応答の3指標を同一I/O仕様に揃え、順位保存率80%以上を採択条件にする。 | 研究助成（意識指標比較） | ID 735, 842, 859 |
| U11-2<br>PCIやIIT近似計算の計算量制約をどう扱うか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | IIT厳密計算は除外し、ID 735/842で `PCI近似` `LZ` `wSMI` を計算予算（1症例あたりGPU 2時間以内）付きで比較する。 | 理論研究奨励（IIT近似） | ID 735, 842, 859 |
| U11-3<br>理論予測の対立点を単一実験計画へどう落とすか。 | B（部分検証（外部データ併用で成立）） | ID 735/859で理論対立点を同一入力条件へ寄せる試験計画を作る。 | 共同研究助成（理論対立検証） | ID 735, 842, 859 |
| U11-4<br>意識指標を臨床/研究で運用する際の失敗条件をどう明示するか。 | B（部分検証（外部データ併用で成立）） | ID 859で偽陽性/偽陰性を含む臨床失敗条件の閾値を先に定義する。 | 臨床系若手助成（失敗条件定義） | ID 735, 842, 859 |

## U12 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U12-1<br>分岐後主体の識別子を何に基づいて付与するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 分岐後識別子の法的定義はEEG-DATA単独では不可。ID 11を技術IDの安定性評価に限定利用。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-2<br>責任・権利・同意の継承ルールをどの時点で分岐させるか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 責任・権利・同意の継承規則は制度設計課題であり、EEG-DATAは検証補助のみ。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-3<br>心理的連続性基準と法的個体基準の不一致をどう扱うか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 心理的連続性と法的個体の不一致はデータだけでは裁定できず、規範設計が主対象。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-4<br>技術評価（性能）と人格評価（帰属）をどう接続するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 性能KPIと人格帰属KPIの接続は法務要件が主で、EEGは監査ログ項目の補助。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-5<br>分岐主体間で記憶編集・再同期が起きた場合、法的主体IDを再編する基準は何か。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 記憶編集・再同期時のID再編ルールはEEGデータでは直接検証不可。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-6<br>同意撤回が発生したとき、複数分岐主体への権限剥奪を技術的にどう実装・監査するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 同意撤回の権限剥奪監査はシステム設計課題で、EEG-DATAは模擬ログ検証まで。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |

## U13 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U13-1<br>brain-to-text成功を『意味復元』と『因果再現』へ分解できるか。 | B（部分検証（外部データ併用で成立）） | ID 509でovert/imaginedを比較し、意味一致と因果一致の乖離を測る。 | 研究助成（模倣分離） | ID 509, 13, 65 |
| U13-2<br>LLMの幻覚・整合性検査を神経デコード評価へどう接続するか。 | B（部分検証（外部データ併用で成立）） | ID 13/65で行動整合と内部状態差を分離し、幻覚検査の接続点を作る。 | 若手研究助成（幻覚/内部状態差） | ID 509, 13, 65 |
| U13-3<br>同一出力でも内部機構が異なるケースをどう検出するか。 | B（部分検証（外部データ併用で成立）） | ID 65/509で同一出力・異内部状態ケースを抽出する判定器を設計する。 | 研究奨励金（shortcut検出） | ID 509, 13, 65 |
| U13-4<br>模倣性能の上限を因果評価でどこまで抑制できるか。 | B（部分検証（外部データ併用で成立）） | ID 509で模倣スコア単独合格を禁止し、因果整合指標との二重閾値を運用する。 | 研究助成（因果整合KPI） | ID 509, 13, 65 |
| U13-5<br>視覚知覚と視覚想起で同一デコーダを使ったとき、意味復元精度の劣化パターンはどこで分岐するか。 | B（部分検証（外部データ併用で成立）） | ID 13を主に、知覚条件と想起条件で同一デコーダを適用し、精度低下の分岐点を推定する。 | 博士課程研究助成（知覚/想起分岐） | ID 13, 509, 65 |
| U13-6<br>プロンプト誘導・データリーク・shortcut学習を分離検出する対照実験をどう設計するか。 | B（部分検証（外部データ併用で成立）） | ID 65/13でリーク対照実験を設計し、shortcut検出率を評価する。 | 研究助成（リーク分離実験） | ID 509, 13, 65 |

## U14 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U14-1<br>データ/コード/評価環境の固定粒度をどこまで要求するか。 | A（直接検証可能） | ID 6で測定遅延再現試験を自動化し、最小追試パックの基礎にする。 | 研究助成（再現性運用） | ID 6, 56, 719 |
| U14-2<br>探索研究と検証研究を運用上どう分離するか。 | A（直接検証可能） | ID 56で探索/検証の分離運用を行い、同一条件再実行の再現率を示す。 | 研究奨励金（探索/検証分離） | ID 6, 56, 719 |
| U14-3<br>leaderboardでのリーク・過適合・報告バイアスをどう監査するか。 | A（直接検証可能） | ID 719でleaderboardリーク監査（被験者分割・時系列リーク）を定期化する。 | 若手研究助成（リーク監査） | ID 6, 56, 719 |
| U14-4<br>Model Card / Dataset Card を評価契約へどう統合するか。 | A（直接検証可能） | ID 719/56にModel Card・Dataset Card必須化を接続し監査項目化する。 | 研究助成（カード統合） | ID 6, 56, 719 |
| U14-5<br>再現失敗ケースを否定例レジストリとして公開し、再試行サイクルをどう運用するか。 | B（部分検証（外部データ併用で成立）） | `failure_id` `dataset_id` `split_hash` `failure_type` `rerun_status` を必須項目にした否定例レジストリを運用し、公開同意フローを併設する。 | 研究奨励金（否定例レジストリ） | ID 6, 56, 719 |
| U14-6<br>コンテナ固定（OS・依存ライブラリ・乱数種）を必須化した場合、再現コスト増分をどこまで許容するか。 | A（直接検証可能） | ID 719でコンテナ固定時の計算コスト増分を測定し、許容上限を設定する。 | 研究助成（再現コスト上限） | ID 6, 56, 719 |

## U15 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨EEG-DATA |
|---|---|---|---|---|
| U15-1<br>神経データの機微性をどの法概念で扱うか（個人情報・生体情報・人格情報）。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 神経データ機微性の法概念マッピングは法務課題で、EEG-DATA単独検証は不可。 | 制度設計助成（神経データ法制） | ID 49, 2412, 3419 |
| U15-2<br>neurorightsを技術監査項目へどう写像するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | neurorights監査項目化は制度設計が主で、ID 2412は技術ログ項目定義にのみ有効。 | 制度設計助成（神経データ法制） | ID 49, 2412, 3419 |
| U15-3<br>法域差（EU/US/JP等）を跨ぐ最小共通運用をどう定義するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 法域差を跨ぐ最小運用はデータでは確定できず、規制比較テーブル整備が必要。 | 制度設計助成（神経データ法制） | ID 49, 2412, 3419 |
| U15-4<br>技術進展に応じた停止条件・更新条件をどうガバナンス化するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 停止/更新条件のガバナンス化は制度KPIが主で、ID 49/3419はリスク閾値の補助根拠。 | 制度設計助成（神経データ法制） | ID 49, 2412, 3419 |

## 実行優先順（助成応募に直結する順）

1. `U7/U14` を先行（Aが多く、短期間で再現可能成果を作りやすい）
2. `U0/U1/U4/U8/U13` を第2波（B中心だが実験系としては組める）
3. `U10/U12/U15` は制度・理論連携枠で別トラック化（EEG単独完結は不可）

## RQ別提出固定表（新規）

- `1RQ=1提出判断` を固定した運用版は `mind-upload-eeg-rq60-grant-dataset-playbook` を参照。
- 各 `Ux-RQy` について、`第一応募先/予備応募先/主EEG-DATA/最小成果物` を1行で固定済み。
- 本ページは判定根拠、プレイブック側は提出運用という役割分担で使う。

## 注意点

- 本ページの`C`判定は「重要でない」意味ではなく、「EEG-DATA単独では実証不十分」の意味です。
- `U12/U15`は制度設計（法務・倫理・監査要件）を先に定義し、EEG側は監査ログ要件の裏取りに使うのが安全です。
- `U10`は熱力学の直接計測が未整備なので、まずは理論整合とproxy検証に限定する方が過剰主張を避けられます。

## 2026-03-18 12:02 JST 再検証ログ（本run / 依頼反映）

- 作業前に `auto-startup` の `main` で `git pull --ff-only` を実行し、最新状態を確認しました。
- `mind-upload/research_harvest_50.md` を正本として再照合し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、各RQに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が埋まっていることを再確認しました。
- 助成テーマは `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を正本キーとして維持しました。
- EEG参照は引き続き `D1-D16 + DOI + データセット名 + access区分` を申請正本とし、数値IDは探索補助として扱います。
- 依頼方針どおり、汎用的な浅い横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の粒度で、各課題を個別に深掘りする運用をwiki正本に固定しました。

## 2026-03-18 13:01 JST 再検証ログ（本run / 深掘り方針の再固定）

- 作業前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、fast-forward不要（Already up to date）を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` を正本に、`60RQ` すべてに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が1行ずつ埋まっている構造を再確認しました。
- 依頼方針どおり、横断的な一般論ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で扱う運用を維持し、各RQの「EEG-DATA単独で言える範囲」と「外部依存境界」を分離して提示する方針を固定しました。
- 応募先は `G1-G6` のキー運用を維持し、`A/B/C` 判定ごとに `A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を使い分ける設計を継続しました。
- wiki反映先は `mind-upload/wiki` と `mind-upload/github-wiki-export`、および `auto-research-funds/wiki` の3面同期を維持し、同一内容で更新しました。

## 2026-03-18 14:02 JST 再検証ログ（本run / 3リポ同期確認）

- 作業前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull origin main` を実行し、先に最新化したうえで検証を開始しました。
- `RQ60` の1問ずつ深掘り構造を再確認し、`検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` の4列が全行で埋まっていることを確認しました。
- 再計数結果は `RQ_TOTAL=60`、`A/B/C=17/25/18` で前回と一致しました（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）。
- 応募テーマの運用は `G1-G6` を維持し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を継続しました。
- 方針は引き続き `1RQ=1検証命題=1応募テーマ=1主データ` を固定し、汎用横断要約ではなくRQ単位での深掘りを正本運用としました。
- wiki反映先は `mind-upload/wiki` / `mind-upload/github-wiki-export` / `auto-research-funds/wiki` の3面同期を維持しました。

## 2026-03-18 15:12 JST 再検証ログ（本run / 依頼の再実行）

- 作業開始前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、最新化済み（Already up to date）を確認しました。
- `mind-upload/research_harvest_50.md` を正本として、`RQ_TOTAL=60` と `U別内訳（4/4/6/4/6/6/4/4/6/6/6/4）` を再照合しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` を比較し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り構造が維持されていることを確認しました。
- 判定内訳 `A/B/C=17/25/18`、および `G1-G6` の助成キー運用を継続し、EEG-DATAは各RQに対して主データを明示したまま維持しました。
- wiki反映は `mind-upload/wiki` / `mind-upload/github-wiki-export` / `auto-research-funds/wiki` の3面同期で更新しました。

## 2026-03-18 17:03 JST 再検証ログ（本run / 深掘り方針で再実行）

- 作業開始前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、最新化済み（Already up to date）を確認しました。
- `mind-upload/research_harvest_50.md` を正本として、`RQ_TOTAL=60` と `U別内訳（U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4）` を再照合しました。
- `A/B/C=17/25/18` を再計数し、全RQに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA`（Deep Evaluation Cards では `主張単位` `応募先` `最低成果物` を追加）が埋まっていることを確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 応募先は `G1-G6` を継続利用し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を維持しました。
- wiki反映先は `mind-upload/wiki` と `auto-research-funds/wiki` の両方に同期しました。

## 2026-03-18 17:18 JST 再検証ログ（本run / 依頼に対する最終固定）

- 作業開始前に `auto-startup` ルートで `git pull --ff-only origin main` を実行し、`Already up to date` を確認した上で検証を開始しました。
- `mind-upload/research_harvest_50.md` のRQ分解を正本として再照合し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 本ページの全RQ行について、`検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略区分を維持しました。
- 助成キーは `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を継続利用し、RQごとの応募テーマを固定しました。
- 依頼方針どおり、汎用的な全体要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用をwiki正本として維持しました。

## 2026-03-18 21:02 JST 再検証ログ（本run / EEG-DATA突合まで再確認）

- 作業開始前に `auto-startup` ルートで `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` を再解析し、`RQ_TOTAL=60` と `U別内訳（U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4）` を再確認しました。
- `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- 本ページで参照するEEGデータID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、欠損IDが `0` 件であることを確認しました。
- 助成テーマは `G1-G6` のキー運用を継続し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略区分を維持しました。
- 依頼方針どおり、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を再固定しました。

## 2026-03-18 22:02 JST 再検証ログ（本run / 依頼再実行）

- 作業開始前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を再検算し、`RQ行数=60` を確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り構造を維持していることを再確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、欠損 `0` 件を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の実在を `grant_queue` / `auto-research-funds` 側で再確認しました。

## 2026-03-18 23:03 JST 再検証ログ（本run / 3リポ pull 後の再固定）

- 作業前に `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only` を実行し、最新更新を取り込んだ状態で検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` の `RQ` 行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と再突合し、欠損 `0` 件を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能でした。
- 運用方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り固定を維持しました。

## 2026-03-19 13:40 JST 再検証ログ（本run / 依頼再実行）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/research_harvest_50.md` を正本として `RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再照合しました。
- 本ページのRQ行を再計数し、`A/B/C=17/25/18` を再確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照整合を `grant_queue` / `auto-research-funds/wiki` で再確認しました。
- 依頼方針どおり、汎用要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-19 14:02 JST 再検証ログ（本run / RQ単位深掘り監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本ページの `RQ` 行を再計数し `60`（`A/B/C=17/25/18`）を再確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` と突合し、`1RQ=1検証命題=1応募テーマ=1主データ` の欠損がないことを確認しました。
- 本ページで参照する EEG 主要ID群（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と再照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側の `RQ行数=60` も再確認し、wiki間整合を維持しました。

## 2026-03-19 06:03 JST 再検証ログ（本run / 1RQ深掘り運用の再確認）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60` を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と突合し、`1RQ=1検証命題=1応募テーマ=1主データ` の整合を維持しました。
- EEG参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、未解決ID `0` を確認しました。

## 2026-03-19 09:05 JST 再検証ログ（本run / 3リポ最新化後の深掘り固定）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化した状態で検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` の `RQ` 行を再計数し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- 主要EEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）は、最新 `EEG-DATA/eeg_dataset_summary_ja.csv` 上で17件すべて存在することを再確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 10:02 JST 再検証ログ（本run / EEG-DATA更新後の深掘り監査）

- 作業開始前に `auto-startup` 親リポジトリで `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新差分を取り込んだ状態で検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` の `RQ` 行を再計数し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と突合し、`1RQ=1検証命題=1応募テーマ=1主データ` の整合を維持しました。
- 主要EEG参照ID（`6, 11, 13, 19, 49, 56, 509, 676, 735`）は、最新 `EEG-DATA/eeg_dataset_summary_ja.csv` で欠損 `0` を確認しました。

## 2026-03-19 11:01 JST 再検証ログ（本run / 要求対応）

- 作業開始前に `auto-startup` 親リポジトリの `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/research_harvest_50.md` を正本として、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再照合しました。
- 本ページのRQ行を再計数し、判定内訳 `A/B/C=17/25/18` を再確認しました。
- 依頼方針に合わせて、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持したまま、各RQの `EEG-DATAで言える範囲` と `外部依存境界` を再確認しました。
- 助成テーマは `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）で維持し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を継続しました。
- wiki反映先として `auto-research-funds/wiki`, `mind-upload/wiki`, `mind-upload/github-wiki-export` の3面へ同内容の再検証ログを追記しました。

## 2026-03-19 12:02 JST 再検証ログ（本run / deep-by-RQ更新後の再監査）

- 作業開始時に `auto-startup` 親リポジトリの `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に検証しました。
- `mind-upload` と `auto-research-funds` の対象wikiページで `RQ` 行を再計数し、いずれも `60` 件で一致することを確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持していることを確認しました。
- 主要EEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。

## 2026-03-19 13:02 JST 再検証ログ（本run / EEG-DATA更新後の深掘り再監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新差分（`mind-upload: f4965c8 -> ee2238d`、`auto-research-funds: 50d3928d8 -> 54f03a5cd`、`EEG-DATA: f09217e902a -> cbb11c31e42`）を取り込んだ状態で検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を `Ux-y` 行で再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認しました。
- RQカードの `主データ/補助データ` から抽出したEEG参照ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側も `Ux-y` 行で `RQ_TOTAL=60` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り同期を維持しました。

## 2026-03-19 14:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで再固定）

- 作業開始前に `auto-startup` 親リポジトリで `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に再検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` も同様に `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、両正本の整合を確認しました。
- 深掘り運用は `1RQ=1検証命題=1応募テーマ=1主データ` を維持し、汎用横断要約ではなく各RQを個別に固定した運用を継続しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。

## 2026-03-19 16:02 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りを再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化後に検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`、`mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` を突合し、`RQ_TOTAL=60` と `A/B/C=17/25/18` の一致を再確認しました。
- RQ運用で参照するEEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 運用方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で、各課題を個別に深掘りして記述する形を維持しました。
## 2026-03-19 18:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りの再監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新差分（`mind-upload: 66e2f8a -> 2b43943`、`auto-research-funds: 382a5f90e -> 5a6eda781`、`EEG-DATA: 88c625b0b6f -> 76b2c83256b`）を取り込んだ状態で再検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18` の一致を再確認しました。
- RQカードの `主データ/補助データ` から抽出したEEG参照ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 運用方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で各課題を個別に深掘りする形を維持しました。

## 2026-03-19 20:02 JST 再検証ログ（本run / ユーザー依頼: 1RQ深掘り固定でWiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` と `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の `Ux-y` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り構造を維持しました。
- 本runで参照したEEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 同内容は `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` にも同期済みです。

## 2026-03-19 21:01 JST 再検証ログ（本run / RQ60可否×助成テーマ再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only` を実行し、最新化済み（Already up to date）を確認しました。
- 本ページの `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）と `A/B/C=17/25/18` を再確認しました。
- 本ページ中の `ID nnn` を抽出して `EEG-DATA/eeg_dataset_summary_ja.csv` と再突合し、参照ID集合（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）の未解決 `0` 件を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と件数・判定内訳が一致することを再確認し、deep-by-RQ同期を維持しました。
