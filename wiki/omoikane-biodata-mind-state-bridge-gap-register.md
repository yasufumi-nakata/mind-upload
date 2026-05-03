---
layout: default
title: 'Wiki: Omoikane BioData bridge ギャップ登録'
description: Omoikane BioData Transmitter から mind-upload 側の mind-state substrate へ進むために必要な研究ギャップ、評価指標、反証条件、倫理 gate を整理します。
article_type: ウィキ
subtitle: body-state surrogate input から consciousness reproduction claim へ飛ばないための bridge register
author: マインドアップロード研究プロジェクト
last_updated: '2026-05-03'
note: Issue #280 対応
audience: Omoikane の BioData bridge、QualiaBuffer surrogate、SelfModel advisory、mind-upload 側の claim ceiling を接続したい人。
reading_time: 20～30分
page_intro: このページは、BioData latent を mind-upload 側の L2/L3 substrate に渡す場合に、どこまでを入力 proxy として扱い、どこから先を未解決の研究ギャップとして止めるかを定義します。
accuracy_note: このページは semantic thought content、subjective equivalence、consciousness reproduction、identity replacement を達成済みとは主張しません。現時点の上限は body-state-surrogate-input-only です。
page_highlights:
- BioData latent は、semantic thought content や qualia equivalence の証拠ではなく、body-state surrogate input として扱います。
- 意識再現 claim へ進むには、主観報告、行動、生理応答、記憶再認、神経動態、摂動応答を分離して評価する必要があります。
- 各ギャップについて、測定対象、必要 dataset、評価指標、反証条件、negative controls、倫理 gate、downgrade rule を明示します。
- 実験、IRB、Omoikane repo 実装、長期縦断データは external dependency tasks として分離します。
known_points:
- biosignal-only input から言語的・記憶的な thought content を一般に復元できるとは主張できません。
- calibration confidence gate は、入力 proxy の信頼性 gate であり、主観等価性の gate ではありません。
- 同一対象の bridge でも、same-subject は same-state や identity continuity を自動的に意味しません。
unknown_points:
- BioData latent と QualiaBuffer surrogate の表現対応が、どのタスク・時間窓・個人内条件で安定するかは未解決です。
- consciousness reproduction の acceptance test は、予測一致、外部行動一致、主観報告一致、同一性継続主張に分解された段階でしか検討できません。
wiki_links:
- label: 'Wiki: Issue #267-#280 対応監査'
  url: /wiki/open-issues-267-280-resolution.html
  description: このページが #280 のクローズ根拠としてどの issue 群に接続されるかを確認します。
- label: 'Wiki: 状態継続ブリッジ'
  url: /wiki/state-continuity-bridge.html
  description: same-subject や same-brain の証拠を same-state と読まないための橋渡し条件を確認します。
- label: 'Wiki: 人間プロキシ構成'
  url: /wiki/human-proxy-composition.html
  description: 複数の生きている人間 proxy row を束ねる場合の上限と残留潜在状態を確認します。
recommended_pages:
- label: 検証
  url: /verification.html#human-proxy-composition-card
- label: 状態継続ブリッジ
  url: /verification.html#state-continuity-bridge-card
- label: 技術ロードマップ
  url: /tech_roadmap.html
---

# Omoikane BioData bridge ギャップ登録

Issue #280 は、Omoikane 側の BioData Transmitter が `physiology-latent-body-state-v0` と `biodata-mind-state-bridge-v1` の境界まで到達したという前提から、mind-upload 側で意識再現 claim を上げるために何が足りないかを整理するものです。

この repo 側では、まず上限を固定します。現時点で許可される読み方は **body-state-surrogate-input-only** です。次の 4 つは runtime fact として主張しません。

- semantic thought content の復元
- subjective equivalence / qualia equivalence
- consciousness reproduction
- identity replacement

## bridge input / output contract

| 項目 | このページで許可する読み方 | 禁止する読み方 |
|---|---|---|
| BioData latent | 生理特徴を圧縮した body-state proxy。 | 思考内容、記憶内容、意識内容の復元。 |
| generated biosignal / affect / thought-pressure proxy | タスク・時間窓・校正条件つきの surrogate signal。 | 本人の意味内容または内的独白の直接読み出し。 |
| calibration confidence gate | 入力 proxy が対象条件内でどれだけ信頼できるかの gate。 | 主観等価性、意識再現、本人性の合格 gate。 |
| QualiaBuffer surrogate handoff | L2/L3 評価に渡す候補特徴 bundle。 | qualia equivalence の証明。 |
| SelfModel advisory | 自己状態推定の補助入力。 | identity continuity の証明。 |
| EpisodicStream handoff | 記憶再認・行動・生理反応と照合すべき入力候補。 | episodic memory の復元。 |

## 研究ギャップ登録

| gap | 測定対象 | 必要 dataset / calibration | 評価指標 | 反証条件・negative controls | 倫理 gate / downgrade rule |
|---|---|---|---|---|---|
| BioData latent から qualia surrogate への表現論 | 生理 latent と主観報告・行動・神経応答の条件付き対応。 | 同一対象、同一セッション、日をまたぐ biosignal + 主観 rating + task events + neural proxy。 | calibration error、予測区間 coverage、subject-within vs subject-out gap、report consistency、OOD degradation。 | shuffled time windows、wrong-subject latent、LM/task-prior only、affect-only baseline が同等なら claim は body-state proxy へ downgrade。 | 主観報告は coercion なしで取得し、撤回時は該当 latent と report linkage を無効化する。 |
| biosignal-only から semantic thought content を復元できる範囲 | 言語・記憶・行動文脈なしで復元可能な成分と不可能成分。 | biosignal-only 条件、language/context 条件、memory cue 条件を分けた ablation dataset。 | brain-minus-prior delta、LM-only 差分、candidate set sensitivity、semantic specificity。 | LM-only、prompt prior、task label、個人 fingerprint で同等なら semantic claim を禁止。 | biosignal-only claim は「意味内容復元」ではなく「状態 proxy」へ戻す。 |
| longitudinal multimodal 個人内 dataset | EEG/ECG/PPG/EDA/呼吸に加え、fNIRS/fMRI/MEG/ECoG/omics/代謝/自律神経/運動/音声などの route family。 | modality ごとの有効時間窓、同期、欠損 policy、同一対象 ID、外部校正を持つ longitudinal protocol。 | complete-case slice、missing modality robustness、cross-day drift、route-local reproducibility、fusion gain over strongest single row。 | 追加 modality が最強単一行を上回らない、または不一致が hard subgroup に集中する場合は multimodal state claim を禁止。 | IRB、データ最小化、撤回可能性、センシティブ signal の別管理が必須。 |
| body-state latent / connectome / neural dynamics / causal perturbation / behavior の階層モデル | 同一 identity の状態推定を構成する階層と残留潜在状態。 | 同一対象の構造 proxy、神経動態、摂動、行動、body-state latent を時間軸付きで接続する dataset。 | posterior overlap、counterfactual prediction、perturbation response error、state-continuity bridge residual。 | 構造 prior だけ、body latent だけ、行動だけの model が同等なら階層統合 claim を downgrade。 | 同一対象リンクは identity continuity ではなく bridge-limited evidence として扱う。 |
| QualiaBuffer / SelfModel / EpisodicStream surrogate benchmark | surrogate 入力後の主観報告、行動、生理応答、記憶再認との一致。 | handoff 前後の event log、surrogate input bundle、report protocol、recognition task、physiology response。 | report agreement、recognition accuracy delta、physiology response alignment、behavioral transfer、abstention rate。 | surrogate を random / wrong-subject / delayed / report-only に置換して同等なら L2/L3 substrate claim を禁止。 | 参加者が報告を拒否・撤回でき、失敗や不一致が公開ログから消されないこと。 |
| consciousness reproduction acceptance test | 予測一致、外部行動一致、主観報告一致、同一性継続主張を分離した合格条件。 | 各 claim level に対応した preregistered benchmark と witness log。 | claim-level pass/fail、OOD robustness、temporal validity、state-continuity residual、downgrade count。 | 1 つの軸だけの成功を他軸へ昇格した場合は acceptance failure。 | consciousness reproduction は独立倫理審査、停止規則、異議申し立て、公開 claim ceiling が揃うまで禁止。 |
| identity continuity witness / consent / revocation / rollback | bridge の同意、証人、撤回、分岐、rollback の運用状態。 | consent record、witness log、branch ID、rollback log、revocation propagation。 | revocation latency、branch trace completeness、rollback test success、audit trail integrity。 | witness 不在、撤回反映不能、branch 不明、rollback 不能なら identity continuity claim を禁止。 | 法的・倫理的 owner を明記し、参加者実験前に承認された protocol を用意する。 |

## end-to-end protocol の最小案

強い claim を避けるため、最初の end-to-end protocol は 4 段階に分けます。

1. **入力固定**: BioData latent、generated biosignal bundle、calibration confidence gate、feature-window series を、時間窓と前処理 version 付きで固定する。
2. **比較固定**: same-subject baseline、wrong-subject control、time-shuffled control、LM/task-prior only、affect-only baseline を同じ分割で固定する。
3. **handoff 固定**: QualiaBuffer surrogate、SelfModel advisory、perception/affect/attention handoff に渡した入力、拒否・棄権・欠損を全て記録する。
4. **評価固定**: 主観報告、行動、記憶再認、生理応答、神経 proxy、摂動応答を別々に採点し、どれか 1 つの成功を consciousness reproduction や identity continuity へ昇格しない。

この protocol が通っても、claim ceiling は最大で **calibrated body-state-to-surrogate handoff** です。semantic thought content、qualia equivalence、consciousness reproduction、identity replacement は別の acceptance test が通るまで禁止します。

## acceptance test の分離

| claim type | 合格に必要なもの | このページでの初期扱い |
|---|---|---|
| 予測一致 | 事前登録された同一対象/日跨ぎ/OOD 評価、calibration、abstention、negative controls。 | 実行可能な L1/L2 検証対象。 |
| 外部行動一致 | 事前登録された行動課題、shortcut audit、task-prior control。 | 行動 proxy としてのみ読む。 |
| 主観報告一致 | report protocol、再検査、report refusal policy、coercion 対策。 | subjective report alignment であり、qualia equivalence ではない。 |
| 記憶再認一致 | cue、recognition、false memory control、time gap、state annotation。 | episodic proxy として読む。 |
| 同一性継続 | witness、consent、revocation、rollback、branch log、state-continuity bridge residual。 | external dependency。現時点では claim 禁止。 |
| 意識再現 | 上記すべてに加え、独立した理論依存/非依存 gate と失敗時 downgrade rule。 | external dependency。現時点では claim 禁止。 |

## downgrade rule

次のいずれかに該当した場合、claim は即座に下げます。

- wrong-subject control と同等なら、個人内 surrogate claim を禁止する。
- time-shuffled control と同等なら、時間的状態 claim を禁止する。
- LM-only / task-prior only と同等なら、semantic thought content claim を禁止する。
- affect-only baseline と同等なら、QualiaBuffer claim ではなく affect/body-state proxy に戻す。
- missing modality policy で結果が反転するなら、fusion claim を禁止する。
- report refusal / revocation を処理できないなら、subjective / identity 系 claim を禁止する。
- rollback または branch log を再現できないなら、identity continuity claim を禁止する。

## external dependency tasks

| task | owner | 前提条件 | 完了条件 |
|---|---|---|---|
| Omoikane 側 schema / docs へ claim ceiling と downgrade rule を同期する。 | Omoikane maintainer | Omoikane repo の編集権限と schema compatibility 方針。 | bridge schema または docs が `body-state-surrogate-input-only` と forbidden claims を明示する。 |
| 同一対象 longitudinal multimodal protocol を設計する。 | 研究 PI / データ管理者 | IRB、同意、機器、保管基盤、撤回手順。 | dataset card、calibration protocol、missing modality policy、negative controls が承認される。 |
| QualiaBuffer / SelfModel / EpisodicStream benchmark を実装する。 | mind-upload / Omoikane joint maintainer | handoff log format、evaluation split、baseline suite。 | benchmark runner と result card が公開され、失敗時 downgrade が自動記録される。 |
| witness / consent / revocation / rollback protocol を作る。 | 倫理・法務・研究運用責任者 | 法的レビュー、参加者説明、監査ログ、撤回運用。 | witness log、branch ID、rollback test、revocation propagation test が承認済みになる。 |
