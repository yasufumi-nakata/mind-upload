---
layout: default
title: Mind-upload RQ60 × EEG-DATA 検証可否と助成テーマ（深掘り版）
description: research_harvest_50由来の60リサーチクエスチョンを1問ずつ、EEG-DATAでの検証可否・auto-research-funds向け応募テーマ・使用データを実務運用向けに整理したページ。
article_type: ウィキ
subtitle: RQごとに検証設計と応募テーマまで接続する
author: マインドアップロード研究プロジェクト
last_updated: '2026-04-03'
note: RQ ごとの詳細な説明
audience: RQを実験計画・応募書類へ落とし込む研究者/実装者
reading_time: 25-40分
---
# Mind-upload RQ60 × EEG-DATA 検証可否と助成テーマ（深掘り版）

> 1問ずつ深掘りして、検証設計と応募テーマまで接続する
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-04-02 / 連続: RQ ごとのディープダイブ

## このページの役割
このページは research_harvest_50 の60 RQを対象に、EEG-DATAで解ける範囲をA/B/Cで判定し、各RQごとの検証設計・応募テーマ・使うデータセットIDをまとめた実務版です。

## 正確さの前提
U10/U12/U15の一部RQはEEG単独で解決できないため、不可と判定し、必要な外部要件を明記します。

## 公開ページへ戻る
- [文書地図](https://mind-upload.com/research_harvest_50.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [RQ60申請プレイブック](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook)
- [現在の資金調達候補リスト](https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md)
- [問題](https://mind-upload.com/issue.html)

## 関連ウィキ
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 判定を実験仕様に迷うときの基準。
- [Wiki:反事実・介入検証](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - U4/U13の成果評価に直結。
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

## 2026 年 4 月 4 日の 22:06 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@39248d59caaa`、`EEG-DATA@7ba2201e2b5`、および `auto-research-funds@f90279417a9f` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルデルタは、現在のルートを置き換えるのではなく、依然としてサポートを強化しています。`mind-upload` は、現在の 6 つの外側にペア流体バリア ルート ガイダンスを追加し、`EEG-DATA` は、`30,935` マージされた一意の行、`28,898` 高信頼行、`24,910` 直接使用可能な行、および `24,540` 高信頼即時行を維持しながら、`IEEE DataPort EEG records` 監査を強化し、`auto-research-funds` は、実質的な候補リストを変更せずに、ムービングヘッド参照のみを緩和します。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取りも、より鋭い方法で意図的に狭いままです。つまり、`D03 / D02 / D01` は、実際の IEEE DataPort ランディング ページよりも DOI/DataCite/カタログ側の読み取りで依然としてオープンに見えるため、`D10` が唯一の明確なパブリック オープン プライマリ アンカーのままである一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- 最新のリポジトリ全体のキャリーフォワードは、依然として強力な行レベルの置換を作成していません。ペアの流体バリア ノートは外部カレント 6 ブリッジ言語を改善し、最新の IEEE DataPort 監査はアクセス ステータスの規律を改善し、資金調達の文言のクリーンアップは最終候補リストを再利用しやすくしていますが、いずれも `U13-5` の下でのリコール有効性のギャップを修復せず、`U0-2 / U0-3` の下でセッション間の ID ドリフト フロアを置き換えず、現在の `D11 / D08 / D05 / D20` を置き換えるものではありません。外カレント6人家族。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、`wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html`、`wiki/u13-2-brain-minus-prior-route.html`、および `wiki/u13-5-perception-to-recall-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーはこれらの公開面では `Sat, 04 Apr 2026 12:16:08 GMT` ですが、チェックされたボディでは、このソース同期の前に、フロント ドアに以前の `2026-04-04 17:07 JST` の文言と `U13-2`、`U13-5` に `2026-04-04 19:09 JST` の文言が依然として表示されていました。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=207`、`projects=2`) が示されていたため、現在のルートと監視ルートがすでにカバーされており、それらを置き換える新しい直接適合 EEG ファースト レーンがなかったため、このセッションでは新しいタスクは追加されませんでした。

## 2026 年 4 月 4 日の 17:07 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@dc8ec5dc5e62`、`EEG-DATA@f115f11c2da4`、および `auto-research-funds@8d0f5128fcdc` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、引き続きサポートを強化します。`mind-upload` は、ルートを拡大することなく、現在の 6 つの外側でバリア側の人間プロキシの役割を分割します。`EEG-DATA` は、`30,930` マージされた一意の行、`28,893` 高信頼行、`24,909` の直接使用可能な行を現在の README スナップショットに保持しながら、`EEGIS imagined speech` メタデータを深めます。`auto-research-funds` は、レポートを作成しながら `Uehiro ethics foundation` レガシー同期を追加します。実際の候補リストを変更せずに、`8,616` 援助 ID、`4,319` 行、および `3,971` 公式ソース行。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- 最新のリポジトリ全体の繰り越しは、依然として強力な行レベルの置換を作成していません。バリアの役割の分割は、現在の 6 ブリッジ言語の外側を強化し、最新の想像音声メタデータの深化は音声側のサポートスペースの読み取りを改善し、資金提供のレガシー同期は隣接する滑走路の衛生状態を改善しますが、それらのいずれも、`U13-5` でのリコール妥当性のギャップを修復したり、`U0-2 / U0-3` でのクロスセッション ID ドリフトフロアを置き換えたりするものではありません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、`wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `wiki/u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Sat, 04 Apr 2026 07:12:56 GMT` ですが、チェックされたボディには、このソース同期の前に以前の `2026-04-04 14:10 JST` の文言が依然として表示されています。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`JSM=0`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、現在のルートと監視ルートはすでにカバーされており、新しいダイレクト フィット EEG-first レーンがなかったため、このセッションでは新しいタスクは追加されませんでした。彼らを追い出した。

## 2026 年 4 月 4 日の 01:04 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@9b6a8b971ba0`、`EEG-DATA@56d765da60b`、および `auto-research-funds@3c8569e28` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- The newest pulled deltas still deepen support rather than replace the current route: `mind-upload` adds field-level artifact-stack disclosure tightening on top of the earlier `00:06 JST` reread addenda, `EEG-DATA` deepens the public OpenNeuro metadata for `Numbers` and `PRIOS` while still keeping `30,921` merged-unique rows, `28,884` high-confidence rows, and `24,900` directly usable rows, and `auto-research-funds` adds current coverage for実質的な候補リストは変更せずに、`同盟育成会` と `研究のすゝめ奨学金`。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- 最新のリポジトリ全体の繰り越しは、依然として強力な行レベルの置換を作成しません。`Numbers` と `PRIOS` はサポート空間の特異性を向上させますが、`U13-5` でのリコール有効性のギャップを修復したり、`U0-2 / U0-3` でセッション間の ID ドリフトフロアを置き換えたり、現在の `D11 / D08 / D05 / D20` の外側の現在の 6 ファミリーを置き換えたりすることはありません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u13-2-brain-minus-prior-route.html` に対して依然として `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Fri, 03 Apr 2026 15:13:06 GMT` ですが、チェックされたボディには、このソース同期の前に以前の `2026-04-04 00:06 JST` の文言が依然として表示されています。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`、`同盟会=0`、`研究のすゝめ=0`) が示されていたため、現在のルートと監視ルートがすでにカバーされていたため、このセッションでは新しいタスクは追加されませんでした。新たに対象となる 2 つの奨学金は、依然として現在の EEG 優先ルートから外れています。

## 2026 年 4 月 3 日の 05:12 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@a9fc5d1cb691f3669c40803604e78cf87fab4eed`、`EEG-DATA@8c3ace28bad0b3bac259caa440994e5d05bfc7d1`、および `auto-research-funds@35756f8381c47daa24bb70bb7a1ff88d1dcf76bc` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、引き続きサポートを強化します。`mind-upload` は、アクティブ キューを変更せずにエクスポートされたルート ミラーの位置合わせを維持する `docs: sync github wiki export` ヘッドにあり、`EEG-DATA` は、`30,900` マージされた一意の行、`28,863` 高信頼行、および `24,885` 直接使用可能な行を維持しながら、最近の `EESM17` メタデータの深化に加えて `VR navigation dataset` 出力更新を繰り越し、`auto-research-funds` は追加します。最近の `JSSF research publication` リフレッシュに加えて、`JSPS overseas fellow` の現在のカードのスナップショットが追加され、実質的な候補リストを変更することなく、`8,594` 補助 ID、`4,307` 行、および `3,957` 公式ソース行がレポートされるようになりました。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- 最新のリポジトリ全体のキャリーフォワードは、依然として強力な行レベルの置換を作成していません。サポート スペースは広くなっていますが、最新のプル ヘッドには、`U13-5` でのリコール有効性のギャップが修復されず、`U0-2 / U0-3` でのセッション間の ID ドリフト フロアが置き換えられるものはありません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u13-2-brain-minus-prior-route.html` に対して依然として `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 19:17:56 GMT` ですが、チェックされたボディは、このソース同期の前の初期の `04:05/04:06 JST` ホールド ノートを依然として表示しています。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、現在のルートと監視ルートはすでにカバーされており、高齢化社会レーンはまだ現在の EEG-first ルートの外側にあるため、このセッションでは新しいタスクは追加されませんでした。

## 2026 年 4 月 3 日の 04:06 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@f5e13ebdc4748ce683d905c37cabfdb3c53036bb`、`EEG-DATA@53f5c8166faf0d5fcebfb5c39741d4992eb82a39`、および `auto-research-funds@1f190fec93a9180a27443b1fe2b31f9488dfbf74` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、引き続きサポートを強化します。`mind-upload` は、現在の 6 つの外部に `BCSFB / human-proxy composition` 文献同期を引き継ぎ、`EEG-DATA` は、現在のアンカー ファミリを置き換えないカタログ更新後に `30,900` マージされた一意の行、`28,863` の信頼性の高い行、および `24,885` 直接使用可能な行を保持し、`auto-research-funds` は、`8,593` 支援を報告しながら、`Itoh domestic scholarship` の周囲の現在のカードおよびレジストリ レイヤーを更新します。実際の候補リストを変更せずに、ID、`4,306` 行、および `3,956` 公式ソース行。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- 最新のリポジトリ全体のキャリーフォワードは、依然として強力な行レベルの置換を作成していません。サポート スペースは広くなっていますが、最新のプル ヘッドには、`U13-5` でのリコール有効性のギャップが修復されず、`U0-2 / U0-3` でのセッション間の ID ドリフト フロアが置き換えられるものはありません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u13-2-brain-minus-prior-route.html` に対して依然として `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 18:14:39 GMT` です。
- 公式ウィンドウのスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、現在のルートと監視ルートはすでにカバーされており、高齢化社会レーンはまだ現在の EEG-first ルートの外側にあるため、このセッションでは新しいタスクは追加されませんでした。

## 2026 年 4 月 2 日の 18:06 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@85b6603b569b`、`EEG-DATA@a7f9390492fd`、および `auto-research-funds@b6c0d0f4eeb7` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、引き続きサポートを強化します。`mind-upload` は `U7-2` パブリック ブリッジの文言のみを同期し、`EEG-DATA` は `OSF gazx2` 信頼性 EEG メタデータと `OpenNeuro ds007081` を詳細に調査し、同時に `30,892` マージされた一意の行、`28,855` 高信頼性の行、および `24,880` 直接使用可能な行を現在の README スナップショットに報告し、`auto-research-funds` は README の概要を次のように更新します。 `8,590` 援助 ID、`4,301` 行、および `3,951` 公式ソース行。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も、意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、直接のライブ アクセスの再読み取りでは依然としてこれら 3 つのルート上の `IEEE DataPort` ログイン ゲートとサブスクリプション ゲートを示すため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- 最新のリポジトリ全体の繰り越しは、より強力な行レベルの置換を作成しません。スピーチ側のバックアップ ファミリは依然として役に立ちますが、最新のプル ヘッドには、`U13-5` でのリコール有効性のギャップが修復されず、`U0-2 / U0-3` でのセッション間の ID ドリフト フロアが置き換えられるものはありません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u7-2-timing-metric-route.html` に対して依然として `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 08:22:50 GMT` です。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、現在のルートと監視ルートはすでにカバーされており、高齢化社会レーンはまだ現在の EEG-first ルートの外側にあるため、このセッションでは新しいタスクは追加されませんでした。

## 2026 年 4 月 2 日 10:07 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@be507c810b11`、`EEG-DATA@3f20f48cca6e`、および `auto-research-funds@fb32c05163f4` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、依然としてサポートを強化しています。`mind-upload` は、現在の 6 つ以外の EEG 基盤設定と同等の境界を改良し、`EEG-DATA` は、HBN EEG リリース 11 の詳細な調査後に、`30,887` マージされた一意の行、`28,850` の高信頼行、および `24,871` 直接使用可能な行を報告するようになり、`auto-research-funds` は、リポジトリ統計が依然として `8,585` 支援と表示されている間、同じ実用的な候補リストを維持します。 ID、`4,293` 行、および `3,943` 公式ソース行。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も、意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、直接のライブ アクセスの再読み取りでは依然としてこれら 3 つのルート上の `IEEE DataPort` ログイン ゲートとサブスクリプション ゲートを示すため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- この実行では、現在の行ごとの真実の情報源もより厳密になります。公的側の詳細文書と資金提供側の詳細文書は同じ `Dxx + DOI + dataset name + access class` 文言に再同期されるため、`A/B/C` マップと助成金側の行は再び同じ正規パケットを指すようになります。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 00:15:06 GMT` です。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = annual mid-January to early-April window on the official page`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 2 日の 09:05 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@d7f30648fc40`、`EEG-DATA@ac8cc6fc8e74`、および `auto-research-funds@31ec17305f6a` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、依然としてサポートを強化しています。`mind-upload` は、現在の 6 つ以外の文献ミエリンルート分割を強化し、`EEG-DATA` は `merged_unique=30886`、`high_confidence=28849`、`access_counts_high.immediate=24500` を報告するようになり、`auto-research-funds` は、`Aoi graduate scholarship` / `JSSF research grant` マージに加えて、`8,585` エイド ID、`4,293` 行、および `3,943` 公式ソース行への README 統計の更新を引き継ぎます。現実的な候補リストを置き換えます。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も、意図的に狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は、直接のライブ アクセスの再読み取りでは依然としてこれら 3 つのルート上の `IEEE DataPort` ログイン ゲートとサブスクリプション ゲートを示すため、パブリック ワードでは依然としてゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーはこれらの公開面では `Wed, 01 Apr 2026 23:29:12 GMT` であり、ライブ ページでは、このソース更新の前に以前の `04:09 JST` / `03:08 JST` の再読メモがまだ表示されています。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = annual mid-January to early-April window on the official page`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = current cycle closed` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 2 日の 04:09 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@92d1547bfeb9`、`EEG-DATA@2e3799a174d9`、および `auto-research-funds@f5f55bcbf724` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルデルタは、現在のルートを置き換えるのではなく、依然として支持を深めています。`mind-upload`は、現在の6つ以外の初心者分子メンテナンスファミリーを分割し、`EEG-DATA`は現在、`merged_unique=30877`、`high_confidence=28840`、および`access_counts_high.immediate=24492`を報告し、`auto-research-funds`は、実質的な最終候補リストを置き換えることなく、4月2日の大規模な資金調達の更新を繰り越します。
- `rq_deepening_backlog_2026-03-01_enriched.csv` を再カウントしても `60` 行が返されるため、この実行ではマップが平坦化されるのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取り値も意図的に狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`wiki/mind-upload-current-public-six-rq-brief.html`、`wiki/mind-upload-rq-solvability-bridge.html`、および `wiki/u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 18:24:31 GMT` です。
- 公式窓口のスポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed`、`Kashinome Scholarship = support-only / repo-side current card keeps 2026-04-09` という同じ実用的なブリッジが維持されます。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 17:06 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@c5a0550`、`EEG-DATA@82893f6ca6e`、および `auto-research-funds@ec6f7d068` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新のプルされたデルタは、現在のルートを置き換えるのではなく、依然としてサポートを強化しています。`mind-upload` は、現在の 6 つ以外のアストロ サイト PET ルート分割を深め、`EEG-DATA` は KMI EEG の詳細を更新し、`merged_unique=30871`、`high_confidence=28834`、および `access_counts_high.immediate=24484` をレポートするようになり、その実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行を引き続きカバーし、`auto-research-funds` は `Megachips 2026 scholarship` スナップショットと実際の候補リストを変更せずに README-stat を更新します。
- RQ-by-RQ ドシエで `### Ux-y` 見出しを再カウントしても `60` が返され、グラント/データセット プレイブックで行パケットを再カウントしても `60` が返されるため、この実行ではマップを平坦化するのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取りも、カタログ側のラベルよりも意図的に厳密なままです。更新されたローカル `EEG-DATA` カタログでは、引き続き `D03 / D02` がカタログ側の即時行として、`D01` が即時/要チェックの混合ペアとしてレンダリングされますが、ライブ アクセスの読み取りは狭いままであるため、`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 07:16:09 GMT` です。
- 公式窓口のスポットチェックは依然として同じ実際的なルートを維持しています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 14:08 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。 `mind-upload@ccef40f`、`EEG-DATA@deefd5f95c6`、および `auto-research-funds@f5f76c485` の後の実際のプルの再読み取りでは、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` は変更されません。

- 最新の `EEG-DATA` 追加は、現在のルートを置き換えるのではなく、メタデータをさらに深めます。更新された概要では `merged_unique=30869`、`high_confidence=28832`、および `access_counts_high.immediate=24482` がレポートされるようになり、新しい実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行をカバーします。
- RQ-by-RQ ドシエで `### Ux-y` 見出しを再カウントしても `60` が返され、グラント/データセット プレイブックで行パケットを再カウントしても `60` が返されるため、この実行ではマップを平坦化するのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ルート セーフ アクセスの読み取りも、カタログ側のラベルよりも意図的に厳密なままです。更新されたローカル `EEG-DATA` カタログでは、引き続き `D03 / D02` がカタログ側の即時行として、`D01` が即時/要チェックの混合ペアとしてレンダリングされますが、ライブ アクセスの読み取りは狭いままであるため、`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 04:20:02 GMT` です。
- 公式窓口のスポットチェックは依然として同じ実際的なルートを維持しています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 12:06 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。最新のプルされたデルタは、このメモを凍結する前に再度読み取られました。`mind-upload@9f4bc8e760b1`、`EEG-DATA@1324f9e1ae2b`、および `auto-research-funds@6548b1650535` は、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` を変更せずに残しています。

- 最新の `EEG-DATA` の追加は、現在のルートを置き換えるのではなく、依然としてメタデータを強化しています。更新された概要では `merged_unique=30867`、`high_confidence=28830`、および `access_counts_high.immediate=24480` が報告されていますが、これらの利点は依然として現在の 6 行アンカー ファミリに取って代わるものではありません。
- RQ-by-RQ ドシエで `### Ux-y` 見出しを再カウントしても `60` が返され、グラント/データセット プレイブックで行パケットを再カウントしても `60` が返されるため、この実行ではマップを平坦化するのではなく、`one-RQ-at-a-time` 読み取り値が維持されます。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 02:26:28 GMT` です。
- 公式窓口のスポットチェックは依然として同じ実際的なルートを維持しています。`Kura Fund = 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome = 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 今回の再読では、新しい Todoist ルートは導入されませんでした。最新の正規の資金調達候補者リストの監査では、現時点での実際的な領域がすでにカバーされており、公式の再検査では新たな現行サイクルの資金提供者は明らかにされませんでした。

## 2026 年 4 月 1 日の 11:06 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。最新のプルされたデルタは、このメモを凍結する前に再度読み取られました。`mind-upload@aa21ab9855c1`、`EEG-DATA@cccd137a3468`、および `auto-research-funds@3a691196cb9f` は、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` を変更せずに残しています。

- 最新の `EEG-DATA` の追加は、現在のルートを置き換えるのではなく、依然としてメタデータを強化しています。更新された概要では `merged_unique=30866`、`high_confidence=28829`、および `access_counts_high.immediate=24479` が報告されていますが、これらの利点は依然として現在の 6 行アンカー ファミリに取って代わるものではありません。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再カウントしても `60` が返され、グラント/データセット プレイブックは引き続き `60` の一意の `Ux-y` 行を保持し、この実行ではマップを平坦化するのではなく、依然として `one-RQ-at-a-time` 読み取り値を保持します。
- ブラウザレベルのライブチェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して引き続き `200` が返されました。 `Last-Modified`は`issue.html`/`u8-1`、`Wed, 01 Apr 2026 01:21:13 GMT`の2つのブリッジページで`Wed, 01 Apr 2026 01:21:12 GMT`に進みました。
- 公式窓口のスポットチェックでは、`Kura Fund = 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome = 2026-04-09` という実際的なルートが引き続き維持されますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` はクローズされたままであり、現在のサイクルを監視します。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 03:09 JST 以降の最新のプル後の再検証

この実行によって、現在のパブリック バッチや `A/B/C` の読み取り値は変更されません。最新のプルされたデルタは、このメモを凍結する前に再度読み取られました。`mind-upload@31835fcd8daa`、`EEG-DATA@12eef8ca4ef0`、および `auto-research-funds@040e5b8798fd` は、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` を変更せずに残しています。

- `mind-upload` は、現在のパブリック 6 つ以外の侵入言語 BCI の時間ルートを分割し、`EEG-DATA` は、現在の 6 行のアンカー ファミリを置き換えることなく言語関連のサポート範囲を拡大するセマンティック テキスト関連性の詳細を追加し、`auto-research-funds` は、実質的な候補リストを変更せずに `Obayashi / Yokogaku` カードを更新しました。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再カウントしても `60` が返され、グラント/データセット プレイブックは引き続き `60` の一意の `Ux-y` 行を保持し、この実行ではマップを平坦化するのではなく、依然として `one-RQ-at-a-time` 読み取り値を保持します。
- `2026-04-01 03:09 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。
- 公式窓口のスポットチェックでは、`Kura Fund = 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome = 2026-04-09` という実際的なルートが引き続き維持されますが、`Nakatani Foundation research grant` と `Secom General Research Grant` はクローズされたままで、現在のサイクルを監視します。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 3 月 31 日 20:07 JST 以降の最新のプル後の再検証

この実行では、現在のパブリック バッチや `A/B/C` の内訳は変わりません。最新のプルされたデルタは、このメモを凍結する前に再度読み取られました。`mind-upload@c912fc5ebd4a`、`EEG-DATA@9bdf3b16bfb4`、および `auto-research-funds@4f071fcd98fd` は、現在の `D10 / D03 / D02 / D01` ファミリと外部電流 6 次の `U7-1 -> U1-2 -> U4-2 -> U8-1` を変更せずに残しています。

- 最新の `EEG-DATA` の追加は、現在のルートではなくサポート マップをさらに拡大します。現在の README 概要では、`merged_unique=30,861`、`high_confidence=28,824`、および `access_counts_high.immediate=24,843` が報告されていますが、これらの利点は依然として現在の 6 行アンカー ファミリに取って代わるものではありません。
- RQ ごとのドシエの `### Ux-y` 見出しを再計算すると、引き続き `60` が返され、助成金/データセット プレイブックでは依然として `60` の一意の `Ux-y` 行が保持され、`A/B/C` の内訳は依然として `17 / 25 / 18` のままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、依然として `issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。
- 実際の資金調達見通しはまだ狭いままです。`Kura Fund`、`Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` が現在の 6 つのブリッジとして引き続き有効です。 `Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) ではすでに終了しています。 `Nakatani Foundation research grant` は次のサイクルを監視し続けます。このセッションでは新しい Todoist アイテムは作成されませんでした。

## 2026 年 3 月 31 日の 16:05 JST 以降の最新のプル後の再検証

この実行では、現在のパブリック バッチや `A/B/C` の内訳は変わりません。このメモを凍結する前に、最新のプルされたデルタが再読されました。`mind-upload@a11240d38415` はコネクトーム / タイミング状態ルート カードを強化し、`EEG-DATA@f318ac8ce42d` は `OSF eucqf` の詳細な更新を追加し、`auto-research-funds@c95cc61fdfc9` は新しい `Takeda / Nohken` ファンディング カード マテリアルを追加しました。これらの変更によりサポートマップは広がりますが、それでも現在の `D10 / D03 / D02 / D01` ファミリや現行 6 次オーダーの外側の `U7-1 -> U1-2 -> U4-2 -> U8-1` に代わるものではありません。

- 現在のバッチはまだ `U13-2 / U13-5 / U0-2 / U0-3 / U14-4 / U14-2` のままです。
- この実行のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されたため、この実行では更新するパブリック サイトのテキストはありませんでした。
- Todoist の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`、`AI for Aging-Society Problem Solving=0`) が示されていたため、新しいタスクは追加されませんでした。

## 3月31日の夜の再検査後の現在の6RQルート

この実行によって、現在のパブリック バッチや解決優先順序は変更されません。変更されたのはホールドのアクセス読み取りです。最新の `EEG-DATA` アップストリームの追加は現在の 6 行アンカー ファミリの範囲外のままで、`D10` は唯一明確にパブリックにオープンされたプライマリ アンカーのままであり、`D03/D02/D01` はパブリック ルート上のサブスクリプション ゲート型サポート アンカーとしてのみ読み取る必要があります。

- バッチはまだ `U13-2 / U13-5 / U0-2 / U0-3 / U14-4 / U14-2` のままです。
- 注文はまだ`U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`のままです。
- `2026-03-31 00:04 JST` での公式窓口の再チェックは、`Kura Fund = 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome = 2026-04-09`、`Secom General Research Grant = 2026-03-31 12:00` という同じ実際的なルートを維持しています。
- フルアイテム監査ではすでにカバーされているルート ファミリー (`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`、`AI for Aging-Society Problem Solving=0`) が維持されるため、Todoist はこの実行でも新しいアイテムを必要としませんでした。
- `D03/D02/D01` 即時パブリック ルートと呼ばれるこのページの 3 月 30 日以前のメモは、3 月 31 日のアクセス監査によって置き換えられるものとして読み替えてください。

## 3 月 30 日のライブ再チェック後の現在の 6 RQ ルート

この実行によって、現在のパブリック バッチや解決優先順序は変更されません。これにより追加されるのは、アクティブな 6 行に対するより厳密な読み取りルールです。`D10` は引き続き、明確にパブリックにオープンされた唯一のプライマリ アンカーであり、`D03`、`D02`、および `D01` は引き続き有用ですが、サブスクリプション ゲート型のサポート アンカーです。したがって、公道は意図的に狭いままになっています。

| RQ | 現在のEEG-DATAアンカー | このアンカーがまだ最初の橋として機能している理由 | 即時の資金調達ルートを維持 | EEG 要求の範囲外に置く |
|---|---|---|---|---|
| `U13-2` | `D10 3M-CPSEED` | ローカル EEG-DATA ミラーは、`brain-minus-prior` 監査の最もクリーンな現在のフロアである `20 participants x 4 sessions` 全体で、明白でサイレント意図された想像上の音声を含む即時アクセス OpenNeuro ルートを保存しています。 | `Kura Fund` が最初、`Nakatani Foundation graduate scholarship` が 2 番目です。 | デコーダの成功を内部メカニズムの保存や精神の保存として扱わないでください。 |
| `U13-5` | `D03 Multimodal Fusion EEG + Eye-Tracking` | 意図されたペアの EEG と注視ルートは依然として知覚から想起までの分岐分析を制限しますが、現在の DataPort ページはサブスクリプションゲート型です。 | `Kura Fund` が最初、`Nakatani Foundation graduate scholarship` が 2 番目です。 | 認識と想起を超えて共有されたデコーダを、共有された内部メカニズムの証拠として扱わないでください。 |
| `U0-2` | `D02 CSTE` | `10 participants` を使用した意図された `cross-session / cross-task` 生体認証ベンチマークでは、依然として `offset / jitter / state-feature collapse` 監査の最も明確なフロアになりますが、現在の DataPort ページはサブスクリプションゲート型です。 | 最初は `Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` は学生滑走路サポートのみです。 | 同期の安定性を法的または哲学的なアイデンティティの継続性にまで高めないでください。 |
| `U0-3` | `D02 CSTE` | 同じ `D02` フロアは、しきい値にタイミング エラーを吸収させるのではなく、`U0-2` と同じセッション間アイデンティティ ドリフト ベッド上でしきい値の安定性とオーバーフィットの除外を維持します。 | 最初は `Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` は学生滑走路サポートのみです。 | 安定した生体認証閾値を人格の連続性の十分条件として扱わないでください。 |
| `U14-4` | `D01 Acquisition delay of wireless EEG` | 目的の遅延優先測定パッケージは、制限された開示および再実行契約のエントリ ポイントとしてはまだ十分ですが、現在の DataPort ページはサブスクリプション ゲート型です。 | `Kura Fund` が最初で、`Nakatani Foundation research grant` は次のサイクルの時計としてのみ使用されます。 | 狭いレイテンシ優先のベンチマークから、分野全体の標準化や組織への導入を主張しないでください。 |
| `U14-2` | `D01 Acquisition delay of wireless EEG` | より強力な再現性の文言が許可される前に、操作上の再実行ルールとして探索対確認の分割を定義するには、同じ `D01` アンカーで十分です。 | `Kura Fund` が最初で、`Nakatani Foundation research grant` は次のサイクルの時計としてのみ使用されます。 | 分割境界を越えた後は、探索的な出力を確認証拠として提示しないでください。 |

- この実行における公式ウィンドウの再チェックは、既存の実際のルートと一貫性を保っていました。`Kura Fund` は `2026-04-17 17:00` までオープンのまま、`Nakatani Foundation graduate scholarship` の詳細ページは `2026-04-01 - 2026-05-25 15:00` のまま、`Kashinome` は 4 月初旬の学生滑走路ルートのまま、`Secom General Research Grant` は `2026-03-31 12:00` を通るショートウィンドウ監視ルートのままです。
- Todoist はこの実行では新しいアイテムを必要としませんでした。新たに読み取り専用 API を再チェックしたところ、既存の `Kura`、`Nakatani graduate scholarship`、`Kashinome`、`Nakatani research grant`、および `Secom` タスクがすでに配置されていることが依然として判明したため、重複によりルートが実用的になるどころか、ノイズが増大した可能性があります。

## 今日の深掘り実行パック（2026-03-30 02:05 JST、1-RQ 閉鎖ゲート + 正規ソースの再チェック）

本実行では、現在のパブリック 6RQ のバッチ自体はしっかりと把握したまま、「今この 6 件でパブリック-セーフに前進とさらに最初の成果物」を `RQ` ごとに固定し直しました。

- 現在のパブリックバッチとsolve-first順は維持: `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`
- 公式ソースの再確認:
  - `くら基金`: 現在の PDF / ページで `2026-04-17 17:00` まで開く
  - `中谷財団 大学院生奨学金`: current detail page で `2026-04-01 - 2026-05-25 15:00`
  - `樫の芽会`: 現在の `recruit` ページから `2026-04-09` まで
  - `セコム一般研究助成`: current page で `2026-03-31 12:00` まで
  - `中谷財団 研究助成`:`next-cycle watch`
- Todoist 実 API の読み取り専用再確認でも、現在のルート / ウォッチ ルートを保持しているタスクは足りなかったため、本実行でも新規追加は行っておりません。

| RQ | 今回閉じる最初の成果物 | 主Dアンカー | そのアンカーで今閉じられる範囲 | EEG単独でまだ主張しないこと |
|---|---|---|---|---|
| `U13-2` | `brain-minus-prior`コントロールテーブルとミミック分離ノート | `D10` | 明白な / 無言の意図 / 想像上の音声の分離を使い、幻覚 / 矛盾監査を境界に固定する。 | デコーダの成功を心の保存または保存された内部状態の秘密へ読み替えません。 |
| `U13-5` | 知覚から想起までの劣化ノートと伝達ギャップテーブル | `D03` | EEG+視線のペアストリームを使い、知覚/想起の分岐点を狭くする固定。 | 共有デコーダを共有メカニズムの秘密へ昇格しません。 |
| `U0-2` | オフセット/ジッタ分布と状態特徴崩壊監査 | `D02` | 繰り返されるセッション/クロスタスクのラベルを使い、セキュリティ違反がアイデンティティのような文言へ混入する境界を先に切る。 | 技術的同期安定性を法的・哲学的同一性へ直結しません。 |
| `U0-3` | 閾値安定性注記と過適合除外ルール | `D02` | `U0-2`と同じクロスセッション/クロスタスク床で、閾値選択を狭いベンチマークとして閉じます。 | 安定閾値を personhood continuity の十分条件と扱いません。 |
| `U14-4` | 記入されたモデル カード / データセット カードの例 | `D01` | レイテンシーファーストな狭い再実行ルートに必要な開示フィールドをチェックリスト化する。 | card 記述だけで field-wide reproducibility や組織導入完了を主張しません。 |
| `U14-2` | 固定分割リラン契約とネガティブケーストレイル | `D01` | 探索・確認分割を運用契約として定義し、再実行境界を固定する。 | 探索的出力と確認的主張は混在しません。 |

## 今日の深掘り実行パック（2026-03-29 19:07 JST、現在のルートの充足性 / Todoist の重複監査）

本実行では、現在のパブリック 6RQ の実用的なルートを変えずに、公式ファンディング ウィンドウと Todoist の「今のルートに対して暫定」を再審査いたしました。 総論を増やすのではなく、`current 6RQ を今そのまま深く閉じられるか` だけをさらに明確化する補助です。

- 現在のパブリックバッチとsolve-first順は維持: `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`
- 公式ファンディングウィンドウの再確認:
  - `くら基金`：`2026-04-17 17:00`までオープン
  - `中谷財団 大学院生奨学金`: detail page で `2026-04-01 - 2026-05-25 15:00`
  - `樫の芽会`：`2026-04-09`までオープン
  - `中谷財団 研究助成`: `2026年度募集は終了済み（2025-06-01 - 2025-07-07）`
- Todoist 実 API では、現在のルート周辺で `11` タスクがヒットしました。これは `中谷財団 大学院生奨学金 / 大学院生奨学金給付` と `中谷財団 研究助成` に重複ウォッチがあるため、現在の 6RQ に必要なタスクが不足していることは意味しません。引き続き本実行でも新規タスクは追加しておりません。
- ブロードアーファンディングウォッチでは、`ブレインサイエンス振興財団` `島津科学技術振興財団` `精密測定技術振興財団` `服部報公会` `リカケンホールディングス` の Todoist タスクをもう一度確認できました。いっぽう `高齢社会課題解決研究(AI)` はタスク未登録で今度は、現在のパブリック 6RQ の即時ルートではなく、今回の実行では 2026 回帰を独立再確認していないため追加送りました。
- `mind-upload.com` 側は現在のパブリック 6RQ を既にパブリックセーフに案内できているため、本実行で公開本文の差し替えは行っておりません。

## 今日の深掘り実行パック（2026-03-29 15:15 JST、アンカー強度 + ロードマップギャップ監査）

本実行では、現在のパブリック 6RQ を巻き戻して、`EEG-DATA` 側のアンカー強度と `tech_roadmap.md` 側の未実用化領域だけを追加承認しました。 方針は総論拡張ではなく、引き続き `1RQ=1検証命題=1主アンカー=1第一資金ルート=1非主張境界` です。

- 現在のパブリックバッチとsolve-first順は維持: `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`
- 早速で最も強いメインアンカーは`D10 3M-CPSEED`と`D02 CSTE`です。スピーチ/アイデンティティ側の最初のアーティファクトはこの2本を基準床として扱います。
- `D03 Multimodal Fusion EEG + Eye-Tracking` と `D01 Acquisition delay of wireless EEG` は現在のルート上では有効ですが、メタデータの主張と主張の広がりやすさは `D10/D02` より弱いため、`bounded support anchor` として扱います。`U13-5/U14-4/U14-2` は公開されながらも狭い主張に留め、最小限の成果物が詰まった場合は `D10/D02` 側の補強か付属ベンチマークを優先します。
- 提出・再現ログの正本キーは今回も`Dxx + DOI + dataset name + access class`です。数値IDは探索補助に限定し、再採番ドリフトの影響を避けます。
- `tech_roadmap.md` にある `U2/U5/U6/U9` は、今回の `RQ60` 実務層にはまだ落ちないのです。これは現在の公開バッチの欠落ではなく、`research_harvest_50` 由来の RQ 実用化を次に増やす内部バックログとして扱います。

## 今回の深掘り実行パック（2026-03-29 13:03 JST、アップストリームポストプル / 公式ウィンドウ / Todoist 監査）

本実行では、`mind-upload@12d3d42` `EEG-DATA@8d3d7db889a` `auto-research-funds@eaa5633d0` までプル後に、live `mind-upload.com/issue.html`、主要認定の公式募集ページ、Todoist 実 API を再確認いたしました。 結論は巻き戻すため、現在の公開バッチは `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2` 維持いたします。

- live `mind-upload.com/issue.html`は引き続き`inner-speech decoding + identity drift + reproducibility auditing`を現在のパブリックルートとして出しており、主アンカー族も`D10/D03/D01/D02`のままでした。
- 公式募集ページの 13:03-13:08 JST スポットチェックでは、`くら基金` は `2026-04-17 17:00` まで募集中、`中谷財団 大学院生奨学金` は個別ページで `2026-04-01 - 2026-05-25 15:00` を案内しつつトップの現在オープンリストは空、`セコム一般研究助成` は `2026-03-31 12:00` までオープン、`樫の芽会` は `2026-04-09` までオープン、`中谷財団 研究助成` は `next-cycle watch` という整理を維持いたします。
- Todoist 実 API では `くら基金` `中谷財団 大学院生奨学金` `樫の芽会` `中谷財団 研究助成` の `募集開始確認/応募締切` 8 タスクを 13:03-13:05 JST に再確認できました、本実行でも新規タスクは追加しておりません。
- `mind-upload.com` の公開ソース ページは今回の制限されたルートをすでに自然な文面で保持しており、本実行では公開ページ本文の差し替えは行わず、内部 wiki 側の監査ログだけを更新いたします。

## 今回の深掘り実行パック（2026-03-29 12:06 JST、プル後の公開バッチ同期）

本実行では、プル後にライブ `mind-upload.com/issue.html` を再確認し、公開中の 6RQ を `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2` として内部 wiki 側へ同期し直しました。

| RQ | 今回固定する最小命題 | 主Dアンカー | 現行助成レーン / 実制度の置き先 | 初手KPI | EEG単独でまだ主張しないこと |
|---|---|---|---|---|---|
| U13-2 | `brain-minus-prior`を含む幻聴・神経矛盾監査 | `D10` | `G1/G4` / `くら基金 若手研究者奨励助成`, `中谷財団 大学院生奨学金` | `semantic alignment` `brain-minus-prior gap` `misalignment rate` | デコーダーの成功を精神保存の主張へ読み替えません。 |
| U13-5 | 知覚→想起の分岐点で mimicry と mechanism を切り分ける transfer bench | `D03` | `G1/G4` / `くら基金 若手研究者奨励助成`, `中谷財団 大学院生奨学金` | `perception-to-recall degradation point` `transfer gap` `control-condition stability` | 共有デコーダを共有メカニズムの秘密にしません。 |
| U14-4 | モデルカード/データセットカードを再実行する契約の必須欄へ接続する再現性監査 | `D01` | `G1/G3` / `くら基金 若手研究者奨励助成`, `中谷財団 研究助成（next-cycle watch）` | `required-card fill rate` `rerun success rate` `leak-audit coverage` | card 記述だけで field-wide reproducibility を主張しません。 |
| U0-2 | `clock offset + jitter + state-feature collapse`の本人性ドリフト監査 | `D02` | `G2/G3` / `中谷財団 大学院生奨学金`, `樫の芽会 奨学金（runway 補助のみ）` | `clock-offset p95` `state-feature collapse rate` `resync recovery rate` | 技術的同期安定性を法的・哲学的同一性へ直結しません。 |
| U0-3 | タスク別閾値安定性とオーバーフィット除外を先に固定する本人性ドリフトベンチ | `D02` | `G2/G3` / `中谷財団 大学院生奨学金`, `樫の芽会 奨学金（runway 補助のみ）` | `session-out AUC` `threshold stability` `overfit exclusion rate` | 安定閾値を personhood continuity の十分条件にしません。 |
| U14-2 | 探索・確認分割を再実行契約の運用境界へ落とす再現性分割 | `D01` | `G1/G3` / `くら基金 若手研究者奨励助成`, `中谷財団 研究助成（next-cycle watch）` | `fixed-split rate` `rerun success rate` `explore-to-confirm carryover gap` | 探索的出力と確認的主張は混在しません。 |

補足:

- live `mind-upload.com/issue.html` はこの 6RQ を既に自然なパブリックルートとして出していたため、本実行でパブリックソースページの追加差し替えは行っておりません。
- Todoist は実際の API にも存在しないタスクの存在を再確認できました、本実行では新規タスクを追加しておりません。
- 公式認証の再確認では、`中谷財団 研究助成`は`2026年度研究助成の募集を終了しました（募集期間: 2025-06-01 - 2025-07-07）`と信頼されていたため、`U14-4/U14-2`の即ルートは`くら基金`、共助成は`next-cycle watch`として扱います。
- 07:18 の `U0-1/U1-2/U4-4/U7-1/U8-4/U11-1` ブロックは以前の内部候補として残され、現在のパブリック ルートは本節の 6RQ を正本といたします。

## 今回の深掘り実行パック（2026-03-29 07:18 JST, mind-upload.com 優先6RQの再固定）

本実行では、`mind-upload.com` 側で今そのまま不自然なく案内できる公開導線を一旦固定し、その会話「今すぐ 1 件ずつ深く検討」6RQ を `EEG-DATA` 現面・現行助成面・Todoist 登録状況まで含めて再固定いたしました。公開面では結論を強めず、`1RQ=1検証命題=1主Dアンカー=1外部依存境界` の粒度に留めます。

| RQ | 今回固定する最小命題 | 主/予備Dアンカー | 現行助成レーン / 実制度の置き先 | 初手KPI | EEG単独でまだ主張しないこと |
|---|---|---|---|---|---|
| U0-1 | 観測一致 / 介入応答一致の二軸ROCで、本人性KPIの必要条件と十分条件の運用境界を切ります。 | 主：`D02` / 予備：`D11`、`D23` | `G2/G3` / `中谷財団 大学院生奨学金`, `樫の芽会 奨学金` | `session-out AUC` `observation-match rate` `intervention-response match rate` | 法的/哲学的な人格同一性の十分条件までは主張しません。 |
| U1-2 | 導電率・電極欠損・ノイズ摂動で、逆問題の区間被覆率が崩れる境界を固定します。 | 主：`D08` / 予備：`D11`、`D19` | `G1/G4` / `ブレインサイエンス振興財団 研究助成`, `中谷財団 研究助成` | `interval coverage` `perturbation stability` `rank stability` | solver 優劣や recoverability の一般論までは主張しません。 |
| U4-4 | 反証閾値（`ΔAUC` / `sign reversal rate`）を先宣言し、因果同値主張の降格条件を固定します。 | 主：`D05` / 予備：`D08`、`D19` | `G1/G4` / `ブレインサイエンス振興財団 研究助成`, `セコム科学技術振興財団 一般研究助成` | `PEHE` `ΔAUC` `sign reversal rate` | 介入系列なしの因果同値や理論勝敗までは主張しません。 |
| U7-1 | `clock offset` `sampling drift` `stimulus onset` `QC fail code` の4項目をBIDS拡張の必須欄として固定します。 | 主：`D11` / 予備：`D15`、`D23` | `G1/G3` / `中谷財団 研究助成`, `くら基金 若手研究者奨励助成` | `required-field fill rate` `reanalysis success rate` `missing-log rate` | 組織導入完了や臨床標準化までは主張しません。 |
| U8-4 | 異常検知遅延と fail-safe 発火 / 回復を単一の評価契約へ固定します。 | 主：`D20` / 予備：`D01`、`D21` | `G2/G5` / `中谷財団 研究助成`, `セコム科学技術振興財団 挑戦的研究助成` | `abnormal-detection latency p95` `fail-safe firing rate` `recovery time` | 現場運用の安全認証や chronic deployability までは主張しません。 |
| U11-1 | `PCI近似 / LZ / wSMI` の順位保存を麻酔・睡眠・DoC 横断で比較可能にします。 | 主：`D14` / 予備：`D16`、`D17` | `G2/G4` / `ブレインサイエンス振興財団 研究助成`, `セコム科学技術振興財団 一般研究助成` | `rank-preservation rate` `boundary-state agreement` `same-cohort calibration gap` | 理論勝敗や意識本体の定義確定までは主張しません。 |

補足:

- この 07:18 候補は、12:06 のライブ再確認で現在の公開バッチが `U13-2/U13-5/U14-4/U0-2/U0-3/U14-2` であることを確認したため、歴史的候補として扱います。
- 関連する主要制度の Todoist task は既に登録済みのため、本runでは新規 task 追加を行っておりません。

実行順（本実行固定）:

1. `U7-1`
2. `U1-2`
3. `U4-4`
4. `U0-1`
5. `U8-4`
6. `U11-1`

## 今回の深掘り実行パック（2026-03-29 05:55 JST, EEG-DATA実在面 + 現行助成面の再検証）

本運営では、みんなの`6RQ`深掘りパックを維持したまま、`EEG-DATA`側の現存バケットと`auto-research-funds`側の現存カード実体を再固定いたしました。

| RQ | EEG-DATAバケット（今回のメインアンカー） | 主/予備Dアンカー | 実データ条件（最低限） | 現行助成レーン | EEG単独でまだ主張しないこと |
|---|---|---|---|---|---|
| U0-2 | 生体認証 / クロスセッション転送 (`D02`) | 主：`D02` / 予備：`D11`、`D23` | 繰り返されるセッション、同じ主題のラベル、タスクのバリエーション、タイムスタンプ/QC、デバイスのメタデータ | レーン：`G2/G3` / 実カード：`G3=9Lx4dPK6a4k2gOb7` | 同一性の哲学的十分条件までは主張しない。同期妥当性つき識別KPIに限定。 |
| U1-4 | ソースローカリゼーション/直接検証 (`D08`) | 主：`D08` / 予備：`D11`、`D19` | 高密度EEG、介入グラウンドトゥルース、頭部モデルまたはiEEG開示、再実行可能なパイプライン | レーン：`G1/G4` / 実カード：`G4=Drbm6vBRDJkn0NGJ` | solver 優劣を一般脳状態の完全回復へ直結させない。 |
| U7-6 | 同時 EEG-fMRI / EEG-fNIRS / 欠落モダリティの堅牢性 (`D11`) | 主：`D11` / 予備：`D15`、`D23` | 同じトライアルの同期、BIDS サイドカーの出自、欠落モダリティ ポリシー、サブジェクト セッション数 | レーン：`G1/G3` / 実カード：`G3=9Lx4dPK6a4k2gOb7` | multimodal bundle 成功を「共通状態変数の解決」とは呼ばない。 |
| U8-6 | 縦断的/閉ループオンライン適応 (`D12`) | 主：`D12` / 予備：`D20`、`D21` | オンライン ラベル、レイテンシー ジッター ログ、修正デコーダーと再キャリブレーション デコーダーの開示、障害レジストリ | レーン：`G2/G5` / 実カード：`G5=871pw3rLjNPKgqA0` | same-session 成功だけで週〜月運用の耐久性を主張しない。 |
| U11-3 | 睡眠意識 / 麻酔鎮静 / DoC バイオマーカー (`D17`) | 主：`D17` / 予備：`D14`、`D16` | 同一コホートのキャリブレーション、連続記録、催眠計画または鎮静段階のラベル、薬理学または摂動ログ | レーン：`G2/G4` / 実カード：`G4=Drbm6vBRDJkn0NGJ` | 理論勝敗や意識の本質指標の確定までは主張しない。 |
| U13-2 | 音声生成/再構成-復号化 (`D10`) | 主：`D10` / 予備：`D03`、`D09` | 刺激/音声/転写物の調整、顕性対非顕在の制御、リークのない分割、BIDS または同等の出自 | レーン：`G1/G4` / 実カード：`G4=Drbm6vBRDJkn0NGJ` | brain-to-text 成功を模倣分離や保存成功の証拠とは呼ばない。 |

補足:

- `G1/G2` は固定レーンであり、現行の助成 card 実体ではありません。
- 現在のカード本体は`G3-G6`です。
- 現行 card の一覧正本は `auto-research-funds/wiki/Mind-Upload-Current-Funding-Shortlist.md` として固定いたしました。

## 今回の深掘り実行パック（2026-03-29 02:04 JST, 現行site audit反映パック）

本実行では、直前の「可解性優先パック」を崩さず、その上で現在 `mind-upload` のサイト深化監査が強く更新した見解を `6RQ` に限定して反映いたしました。

| RQ | 今回固定する最小命題 | 提出テーマ（そのまま応募見出しへ使う軸） | 第一/予備応募先 | 主データ（主/予備） | 反映したサイトの意見 | 初手KPI | 停止条件 |
|---|---|---|---|---|---|---|---|
| U0-2 | 同期ずれを`clock offset + jitter p95 + state-feature collapse rate`の3つの指標で固定し、同一性評価が計測誤差へ引きずられる境界を越えます。 | 時間的有効性を認識した ID 同期監査 | `G2 / G3` | 主：`D02 CSTE: A Dataset for Cross-Sessions and Cross-Tasks EEG Biometrics` / 予備：`D11 A multi-session simultaneous EEG-fMRI dataset with online experience sampling`、`D23 EEG, PPG, GSR signals for rehabilitation fatigue detection` | `Temporal Validity Card`と`state annotation`の分離 | `clock offset p95` `state-feature collapse rate` `resync recovery rate` | 再同期後も `state-feature collapse rate` が収束せず、同一性判定の改善が再現しない場合。 |
| U1-4 | 逆問題の公開基準を点推定ではなく`posterior interval + reanalysis agreement`へ固定し、ソルバー改善と不確実性公開を分離します。 | 事後を意識した逆ベンチマークと開示基準 | `G1 / G4` | 主：`D08 Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods` / 予備：`D11 A multi-session simultaneous EEG-fMRI dataset with online experience sampling`、`D19 CerebellarTMSEEGData` | 逆ルートの4ゲート読解 | `interval coverage` `posterior-width stability` `reanalysis agreement` | 区間被覆率が継続逸脱し、後方分布公開で手法順位が不安定化する場合。 |
| U7-6 | 欠損モダリティ下でも結論を維持できる最小観測セットを`conclusion agreement + warning recall + complete-case bias`で固定します。 | 欠落モダリティの堅牢なマルチモーダル監査パッケージ | `G1 / G3` | 主：`D11 A multi-session simultaneous EEG-fMRI dataset with online experience sampling` / 予備：`D15 A simultaneous EEG-fNIRS dataset for investigating working memory load`、`D23 EEG, PPG, GSR signals for rehabilitation fatigue detection` | `bundle robustness gate`と`missing-modality policy`の独立開示 | `conclusion agreement rate` `warning recall` `complete-case bias` | full-modality 基準との一致率下限を満たさず、欠損条件で安全警告の見逃しが増える場合。 |
| U8-6 | 閉ループの再学習間隔を`fixed-decoder durability`と`rescue-mode recalibration burden`に分けて固定します。 | 閉ループの安全性を確保するための縦方向の再校正スケジュール | `G2 / G5` | 主：`D12 Longitudinal MI-BCI training with transcutaneous spinal stimulation` / 予備：`D20 Closed-loop auditory stimulation targeting REM oscillations`、`D21 NeuroSimo: closed-loop EEG/EMG-guided TMS` | `same-session fast`と`deployable chronic loop`の分離 | `performance decay rate` `safety margin` `retraining cost` | 再学習コスト増に対して性能維持と安全余裕の改善が再現しない場合。 |
| U11-3 | 理論対立点を単一計画へ落とす際、`construct validity / perturbational validity / same-cohort calibration / incremental validity`の4ゲートを必須にします。 | 4 ゲート意識代理競合テスト | `G2 / G4` | 主：`D17 DoC EEG biomarker pilot (preliminary ML outcome detection)` / 予備：`D14 PK-NMM EEG simulation during propofol anesthesia`、`D16 Aalborg University Wearable Sleep Study (AAUWSS)` | 意識理論マップの4ゲートを読む | `same-cohort calibration gap` `indicator divergence width` `incremental validity` | 指標乖離が理論予測と整合せず、same-cohort calibration を固定できない場合。 |
| U13-2 | 言語デコードを一括りにせず、`brain-minus-prior baseline` を含む hallucination/整合監査へ分解して固定します。 | 模倣分離のための神経幻覚調整監査 | `G1 / G4` | 主：`D10 3M-CPSEED: EEG dataset for overt/silent/imagined speech` / 予備：`D03 Multimodal Fusion System for Cognitive Load Assessment`、`D09 VICODEV dataset` | 言語ルート分割と`Neural Contribution Card` | `semantic alignment` `brain-minus-prior gap` `misalignment rate` | prompt 依存の寄与を分離できず、神経由来の差分が再現しない場合。 |

実行順（本実行固定）:

1. `U0-2`
2. `U1-4`
3. `U7-6`
4. `U8-6`
5. `U11-3`
6. `U13-2`

## 今回の深掘り実行パック（2026-03-29 01:37 JST, 可解性優先のA/B実装パック）

今回は「全体をもう一度広く要約する」更新は行わず、`A/B` 判定の中でも EEG-DATA だけで最初の実験と応募テーマを切りやすい `6RQ` を固定いたしました。

| RQ | 今回固定する最小命題 | 提出テーマ（そのまま応募見出しへ使う軸） | 第一/予備応募先 | 主データ（主/予備） | 初手KPI | 停止条件 |
|---|---|---|---|---|---|---|
| U1-1 | 既知刺激位置に対する `prior` 別逆解誤差の序列を固定する。 | 高密度EEGグラウンドトゥルースを用いた逆問題事前選択ベンチマーク | `G1 / G4` | 主：`ID 56 Intracerebral stimulation + HD-EEG (ground-truth)` / 予備：`ID 676 Simultaneous EEG-fMRI XP1`、`ID 1839 CerebellarTMSEEGData` | `位置誤差` `被覆率` `手法順位一致率` | 誤差序列が再現せず、被覆率が継続逸脱する場合。 |
| U4-2 | 最小介入で反証可能な因果主張までに限定して固定する。 | 刺激・騒乱入り最小因果検証パッケージ | `G1 / G4` | 主：`ID 19 HiPi pinprick stimulation EEG` / 予備：`ID 56 Intracerebral stimulation + HD-EEG (ground-truth)`、`ID 1839 CerebellarTMSEEGData` | `介入あり/なし差` `符号一致率` `反事実誤差` | 介入差分が再現せず、符号一致率が基準未達のままの場合。 |
| U7-1 | 同期/QC/刺激ログの必須項目欠損率を BIDS 拡張監査として固定する。 | BIDS拡張による同期・QC・刺激ログ監査基盤 | `G1 / G3` | 主：`ID 676 Simultaneous EEG-fMRI XP1` / 予備：`ID 783 Simultaneous EEG-fNIRS working memory`、`ID 4878 EEG+PPG+GSR rehabilitation fatigue` | `必須項目充足率` `欠損ログ率` `再解析成功率` | 必須項目を再構成できず、再解析成功率が継続的に下回る場合。 |
| U11-1 | `PCI近似/LZ/wSMI` の順位保存を状態差ごとに比較し、理論横断I/Oを固定する。 | 麻酔・睡眠・DoCをまたぐ意識代理ランキング調査 | `G2 / G4` | 主：`ID 735 PK-NMM propofol anesthesia EEG simulation` / 予備：`ID 842 AAUWSS wearable sleep study`、`ID 859 DoC EEG biomarker pilot` | `順位保存率` `偽陽性率` `状態遷移境界一致率` | 状態間で順位が安定せず、失敗条件を先に定義できない場合。 |
| U13-5 | 同一デコーダで知覚条件と想起条件を比較し、分岐点だけを固定する。 | 知覚/想起分裂を使った模倣メカニズムの分離 | `G1 / G4` | 主：`ID 13 Multimodal Fusion EEG + Eye-tracking` / 予備：`ID 509 3M-CPSEED overt/silent/imagined speech EEG`、`ID 65 VICODEV driving distraction multimodal` | `意味一致率` `機構差検出率` `知覚→想起劣化点` | 分岐点が安定せず、知覚/想起の差を対照条件で固定できない場合。 |
| U14-4 | Model Card / Dataset Card を評価契約の必須項目へ統合し、追試可否を固定する。 | モデルカード/データセットカード統合再現契約 | `G1 / G3` | 主：`ID 6 Acquisition delay of wireless EEG` / 予備：`ID 56 Intracerebral stimulation + HD-EEG (ground-truth)`、`ID 719 Ubiquitous P300 benchmark` | `カード必須項目充足率` `追試成功率` `リーク監査反映率` | カード整備を入れても追試成功率が改善せず、監査項目が運用へ落ちない場合。 |

実行順（本実行固定）:

1. `U1-1`
2. `U4-2`
3. `U7-1`
4. `U11-1`
5. `U13-5`
6. `U14-4`

## U別・助成テーマ×EEG-DATA実行マップ（全RQ再点検）

`mind-upload-rq60-deep-evaluation-cards` を1行ずつ再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` で提出できるよう、U単位の入口を固定しました。

| U | RQ数 | auto-research-funds向け提出テーマ（RQ深掘り時の主軸） | 主に使うEEG-DATA（主/補助） | 可否帯 |
|---|---:|---|---|---|
| U0 | 4 | 同一性KPI（観測一致/介入一致の二軸判定） | 主: `ID 11` / 補助: `ID 29, 696` | `A中心（一部B）` |
| U1 | 4 | 逆問題不確実性・手法比較・後方分布公開 | 主: `ID 56` / 補助: `ID 676, 1839` | `A/B` |
| U3 | 6 | 境界拡張のproxy検証（EEG単独と統合条件の差分） | 主: `ID 13` / 補助: `ID 16, 39` | `B/C` |
| U4 | 4 | 介入同値・反事実評価・反証条件の固定 | 主: `ID 19` / 補助: `ID 56, 1839` | `A/B` |
| U7 | 6 | 同期監査・前処理差分監査・再現性契約化 | 主: `ID 676` / 補助: `ID 783, 4878` | `A` |
| U8 | 6 | 閉ループ安定化・再較正・フェイルセーフ運用 | 主: `ID 6` / 補助: `ID 1972, 2412, 696` | `B` |
| U10 | 4 | 情報熱力学の理論整合（proxy段階） | 主: `ID 735` / 補助: `ID 783, 1011` | `C` |
| U11 | 4 | 意識指標比較・失敗条件付き理論比較 | 主: `ID 735` / 補助: `ID 842, 859` | `B/C` |
| U12 | 6 | 分岐/複製監査ログ設計・制度接続 | 主: `ID 11` / 補助: `ID 509, 696` | `C` |
| U13 | 6 | 模倣分離（意味一致と因果一致の分離） | 主: `ID 509` / 補助: `ID 13, 65` | `B` |
| U14 | 6 | 追試契約・リーク監査・否定例公開運用 | 主: `ID 6` / 補助: `ID 56, 719` | `A中心（一部B）` |
| U15 | 4 | 制度統合・停止/更新条件の監査設計 | 主: `ID 49` / 補助: `ID 2412, 3419` | `C` |

上表は「どの助成テーマで出すか」と「そのテーマで最初に使うEEG-DATAは何か」を、RQ群ごとに即決できるようにするための実務入口です。実際の提出では、各RQ行（60行）に戻して `主張単位` と `最低成果物` を固定してください。

## 今回の深掘り実行パック（2026-03-27 09:30 JST, 2週間で初回結果まで）

汎用横断の更新ではなく、今回は直近runと重複しない `6RQ` を固定し、`1RQ=1検証命題=1応募テーマ=1主データ` で深掘りします。

| RQ | 選定理由（1件ずつ深掘りする理由） | 最初の実験KPI | 失敗条件（このrunでの停止条件） | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|---|
| U1-2 | 不確実性伝播の校正は逆問題の再現性土台なので、先に固定するとU1系の評価軸がぶれにくい。 | `被覆率` `導電率摂動時誤差` `電極欠損耐性` | 被覆率が設計区間を継続逸脱し、摂動で誤差順位が逆転する。 | 逆問題再現レポート（エラー/不確実性） | `G1 / G4` |
| U3-1 | 境界拡張はEEG単独と統合条件の差分を定量化しないと過大主張しやすく、早期に差分基準を固定する価値が高い。 | `統合時改善量` `再現率差` `外部依存残差` | 統合時改善量が再現せず、外部依存残差の説明が不能。 | 境界拡張評価レポート（単体・統合比較） | `G2 / G6` |
| U7-4 | 再計測/除外判定木は再現運用のボトルネックで、先に決めるとU7全体の監査運用が安定する。 | `再計測判定一致率` `除外誤判定率` `再実行コスト` | 判定木の一致率が低く、再計測コストが運用上限を超える。 | 再現性監査レポート（同期/QC/前処理差異） | `G1 / G3` |
| U8-5 | ヒューマンオーバーライドは現場安全に直結し、誤作動率と回復時間の同時評価が必須。 | `誤作動率` `回復時間` `手動介入率` | 介入時の回復が不安定で、誤作動率が許容帯を超過。 | 動作安定性レポート（安全停止/復旧時間） | `G2 / G5` |
| U11-4 | 意識指標は失敗条件を先に固定しないと臨床運用で過剰主張になるため、閾値と否定例を先に定義する。 | `偽陽性率` `偽陰性率` `閾値安定性` | 偽陽性/偽陰性のいずれかが上限を超え、閾値が症例群で不安定。 | 認知度指数比較レポート（故障条件あり） | `G2 / G4` |
| U14-6 | コンテナ固定のコスト上限は追試運用の可否を決めるため、性能だけでなく実行費用境界を先に決める。 | `追試成功率` `実行時間増分` `計算費増分` | 追試成功率の改善がなく、コスト増分だけが累積。 | コンテナ再生産手順書とコスト測定を修正 | `G1 / G3` |

実行順（本実行固定）:

1. `U1-2`
2. `U3-1`
3. `U7-4`
4. `U8-5`
5. `U11-4`
6. `U14-6`

## 今回の深掘り実行パック（2026-03-27 22:01 JST, 2週間で初回結果まで）

汎用横断の更新ではなく、前runと重複しない `6RQ` を固定し、`1RQ=1検証命題=1応募テーマ=1主データ` で深掘りします。

| RQ | 選定理由（1件ずつ深掘りする理由） | 最初の実験KPI | 失敗条件（このrunでの停止条件） | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|---|
| U0-1 | 観測一致と介入一致を分離しないまま同一性を語ると過大主張になりやすいため、最小判定軸を先に固定する。 | `セッション外AUC` `観測一致率` `介入応答一致率` | 二軸のどちらかが閾値未達で、同一条件再実行でも改善しない。 | 介入プロトコルと反論条件の定義 | `G2 / G3` |
| U1-3 | 逆解法間の乖離はU1全体の再現性ボトルネックなので、手法順位の安定性を先に監査する。 | `手法順位一致率` `逆解誤差` `不確実性被覆率` | 手法順位が分割条件で反転し、順位一致率が基準を下回る。 | 逆問題再現レポート（エラー/不確実性） | `G1 / G4` |
| U4-4 | 反証閾値がない因果同値は運用できないため、失敗宣言条件を先に数値化する。 | `反証閾値超過率` `介入あり/なし差` `符号反転率` | 反証閾値が条件ごとに不安定で、再現時に閾値妥当性を維持できない。 | 因果関係検証報告書（最小限介入主張） | `G1 / G4` |
| U7-5 | 前処理差分の自動監査は再現運用の中心で、release block条件を先に固定すると実装速度が落ちにくい。 | `再現率差` `release block発火率` `再実行時間` | ブロック条件が過敏/鈍感で、同一障害の検出再現性が低い。 | 閾値検索ノートと選択根拠表 | `G1 / G3` |
| U12-6 | 同意撤回時の権限剥奪は技術監査ログへの接続が必須なので、制度RQでも実装可能な最小ログ仕様を先に作る。 | `監査証跡完全性` `権限剥奪反映時間` `欠損ログ率` | 剥奪イベントが監査ログで追跡不能、または反映時間が上限超過。 | システム監査要件表（テクニカルログ対応） | `G2 / G6` |
| U15-2 | neurorightsを理念のままにせず監査項目へ写像できるかが提出可否を左右するため、技術ログとの橋渡しを先行する。 | `法令適合率` `監査項目充足率` `停止基準発動時間` | 監査項目が技術ログへ落とせず、停止/更新条件と接続できない。 | システム統合監査報告書（停止・更新条件） | `G2 / G6` |

実行順（本実行固定）:

1. `U0-1`
2. `U1-3`
3. `U4-4`
4. `U7-5`
5. `U12-6`
6. `U15-2`

## 今回の深掘り実行パック（2026-03-28 09:40 JST, 2週間で初回結果まで）

汎用横断の更新ではなく、過去runの連続実行と重複しにくい `6RQ` を固定し、`1RQ=1検証命題=1応募テーマ=1主データ` で深掘りします。

| RQ | 選定理由（1件ずつ深掘りする理由） | 最初の実験KPI | 失敗条件（このrunでの停止条件） | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|---|
| U0-3 | 同一人物内の状態ドリフトを時間遅延込みで評価しないと、同一性主張が静的一致に偏るため。 | `時系列一致率` `遅延補正後誤差` `再計測時の閾値安定性` | 遅延補正で一致率が改善せず、閾値がセッション間で反転する。 | 閾値検索ノートと選択根拠表 | `G2 / G3` |
| U3-2 | マルチモーダル統合の寄与を分解しないまま性能だけを比較すると、EEG単独境界を誤認しやすいため。 | `統合寄与率` `EEG単独差分` `外部依存残差` | 統合寄与の符号が不安定で、外部依存残差を説明できない。 | 境界拡張評価レポート（単体・統合比較） | `G2 / G6` |
| U4-1 | 介入と反事実の差分を最小主張へ接続しないと、因果主張が相関主張へ退化しやすいため。 | `介入効果量` `反事実誤差` `符号反転率` | 反事実誤差が上限を超え、符号反転が連続発生する。 | 介入プロトコルと反論条件の定義 | `G1 / G4` |
| U7-2 | 同期監査は収録-前処理-再学習で誤差伝播するため、運用KPI化しないと再現不能障害が残るため。 | `同期ずれ分布` `再実行一致率` `QC失敗率` | 同期ずれが収束せず、再実行一致率が基準未達のまま。 | 時刻同期監査レポート（オフセット/ジッタ分布） | `G1 / G3` |
| U11-2 | 指標比較を失敗条件付きで設計しないと、理論比較が事後解釈に流れやすいため。 | `順位保存率` `失敗条件再現率` `理論間乖離幅` | 順位保存率が基準未達で、失敗条件の再現ができない。 | I/O仕様と計算予算の理論比較 | `G2 / G4` |
| U15-1 | 停止/更新条件の技術ログ接続を先に固定しないと、制度提出で監査証跡が不足しやすいため。 | `停止判定遅延` `監査証跡完全性` `権限変更反映時間` | 停止判定が遅延し、監査ログ欠損が継続する。 | システム統合監査報告書（停止・更新条件） | `G2 / G6` |

実行順（本実行固定）:

1. `U0-3`
2. `U3-2`
3. `U4-1`
4. `U7-2`
5. `U11-2`
6. `U15-1`

## 今回の再検証ログ（2026-03-28 09:40 JST）

本実行では、皆様の `RQ60` マップを包括要約へ戻り一旦、RQ 単位の深掘り監査を再実行しました。 今回は `U0-3/U3-2/U4-1/U7-2/U11-2/U15-1` を固定しています。

更新したこと（RQ単位）:

- `U0-3`: 同一性判定に時間遅延補正を組み込み、静的一致のみでの合格を禁止。
- `U3-2`: 統合条件の寄与率を必須記載化し、EEG単独境界を明示する運用に更新。
- `U4-1`: 介入効果と反事実誤差を同時監査し、因果主張の最小条件を固定。
- `U7-2`: 同期ずれの分布と再実行一致率を運用KPIとして固定。
- `U11-2`: 理論比較を失敗条件付きI/O仕様へ接続し、事後解釈を抑制。
- `U15-1`: 停止/更新条件を監査ログへ写像する制度接続導線を明文化。

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` は不変。
- EEG参照運用ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）は最新 `EEG-DATA/eeg_dataset_summary_ja.csv` で旧ID列（`旧ID`）に欠損 `0`。
- 応募キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認。
- 方針は継続して `1RQ=1検証命題=1応募テーマ=1主データ` を維持。

## 今回の再検証ログ（2026-03-29 01:37 JST）

本実行では、`A/B` 判定の中でも EEG-DATA だけで最初の実験と応募テーマを切りやすい `6RQ` を優先させていただきました。

更新したこと（RQ単位）:

- `U1-1`: 既知の刺激位置つき高密度EEGを使う`prior selection benchmark`を固定し、逆問題の最初の手隙順序列へ限定しました。
- `U4-2`: 最小介入で反証可能な causal verification へ主張を絞り、相関主張への後退を防ぐ停止条件を先に書きました。
- `U7-1`: BIDS 拡張の必須ログ項目を成果物へ昇格し、再解析成功率を最小KPIに固定しました。
- `U11-1`: 麻酔・睡眠・DoC をまたぐ順位保存率を前提にし、理論比較を `失敗条件付き` に限定しました。
- `U13-5`: 知覚/想起で同一デコーダの分岐点のみを扱い、意味復元の過読を避ける運用に更新しました。
- `U14-4`: モデルカード/データセットカードを再現性契約の必須項目として扱い、カードが追試成功率へ有効かで判定する形に固定しました。

整合チェック（再実施）:

- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`RQ_TOTAL=60`、`A/B/C=17/25/18`を再確認しました。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` の `### Ux-y` 見出し `60件` を再確認しました。
- ディープ評価カードから抽出した旧ID `24件`（`6,11,13,16,19,29,39,49,56,65,509,676,696,719,735,783,842,859,1011,1839,1972,2412,3419,4878`）は、`EEG-DATA/eeg_dataset_summary_ja.csv` の `旧ID` 列で欠損 `0` でした。
- 応募キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認しました。
- 方針は継続して `1RQ=1検証命題=1応募テーマ=1主データ` を維持いたします。

## 今回の再検証ログ（2026-03-27 22:01 JST）

本runでは、皆様の`RQ60`マップを包括要約へ戻る一旦、RQ単位の深掘り監査を再実行しました。前実行と重複しないように、今回の固定6RQは`U0-1/U1-3/U4-4/U7-5/U12-6/U15-2`としています。

更新したこと（RQ単位）:

- `U0-1`: 同一性判定を `観測一致` と `介入一致` の二軸で固定し、単軸主張を禁止する運用に更新。
- `U1-3`: 逆解法間の順位反転を停止条件に追加し、分割条件依存の過大主張を抑制。
- `U4-4`: 反証閾値を先に宣言する方針を明文化し、因果同値の失敗宣言を運用仕様へ接続。
- `U7-5`: 前処理差分CIで `release block` 閾値を主成果物に昇格。
- `U12-6`: 同意撤回イベントの監査証跡設計を、制度RQの最小実装要件として固定。
- `U15-2`: neurorights監査項目を停止/更新条件の技術ログへ写像する導線を明文化。

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` を `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` から再計数して確認。
- EEG参照ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）は最新 `EEG-DATA/eeg_dataset_summary_ja.csv` で欠損 `0`（`17/17`）を確認。
- 応募キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認。
- 方針は継続して `1RQ=1検証命題=1応募テーマ=1主データ` を維持。

## 今回の再検証ログ（2026-03-27 05:12 JST）

本runでは、皆様の`RQ60`マップを包括的にまとめて一旦戻り、RQ単位の深掘り監査を再実行しました。前runと重複しないように、今回の固定6RQは`U0-2/U4-3/U7-6/U8-3/U13-6/U14-2`としています。

更新したこと（RQ単位）:

- `U0-2`: ms同期と状態表現の固定ルールを、時刻ずれと特徴崩れの同時監査として明文化。
- `U4-3`: 反事実誤差（PEHE）と予測尤度差を最小セットで比較する接続条件を固定。
- `U7-6`: モダリティ欠損（EEG欠損/補助モダリティ欠損）時の最小観測セット同定を深掘り対象に固定。
- `U8-3`: 個体内/個体間分散を分離した長期安定性KPIを、提出前提の評価軸として固定。
- `U13-6`: prompt誘導・データリーク・shortcut学習の分離検出を、対照実験必須条件として固定。
- `U14-2`: 探索研究/検証研究の運用分離を、同一条件再実行の再現率で判定する方針に固定。

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` は不変。
- EEG参照IDセット（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）は最新の`EEG-DATA/eeg_dataset_summary_ja.csv`で欠損`0`です。
- 応募キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認。
- 方針は継続して `1RQ=1検証命題=1応募テーマ=1主データ`。

## 今回の再検証ログ（2026-03-27 09:30 JST）

本runでは、前runで固定した6RQ（`U0-4/U1-1/U4-2/U8-1/U13-3/U14-3`）と重複しないように、`U1-2/U3-1/U7-4/U8-5/U11-4/U14-6`を新規深掘りキューとして固定しました。

更新したこと（RQ単位）:

- `U1-2`: 導電率・電極欠損・ノイズ注入の3系統摂動で、被覆率逸脱を停止条件に明文化。
- `U3-1`: EEG単独 vs 統合条件の改善量を主張上限に接続し、外部依存残差を必須記載に固定。
- `U7-4`: アライメント失敗時の再計測/除外判定木を成果物要件へ昇格。
- `U8-5`: 手動オーバーライド時の誤作動率と回復時間を同時KPI化し、安全境界を明示。
- `U11-4`: 偽陽性/偽陰性を先行定義し、臨床運用での失敗条件を先に宣言する方針へ固定。
- `U14-6`: コンテナ固定の実行コスト増分を追試成功率と対で評価する運用へ更新。

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` は不変。
- データ参照運用は `DOI + dataset名 + access区分` を正本とする方針を継続。
- 応募キー `G1-G6` の参照整合は維持。

## 今回の再検証ログ（2026-03-26 23:03 JST）

本runでは、前runの固定6RQ（`U4-2/U7-3/U8-2/U13-5/U14-5/U15-4`）を再読し、各RQを「提出文へ転記できる粒度」に深掘り更新しました。総合論は増やさず、RQ単位の境界と運用条件を具体化しています。

更新したこと（RQ単位）:

- `U4-2`: 介入有無比較の最小因果主張を `符号一致` として事前登録し、`PEHE/符号反転率` で停止条件を固定。
- `U7-3`: ASR/ZapLine/ICAの設定差分を監査対象化し、`再現率 -5pt`を解除ブロック条件に固定。
- `U8-2`: 再較正間隔（日次/週次）を運用コストと安全KPIで比較し、棄却条件を明文化。
- `U13-5`: 知覚学習デコーダの想起転送で分岐点を定義し、チャンス水準近傍時の主張撤回条件を追加。
- `U14-5`: 否定例レジストリの必須項目を拡張し、`rerun_window` 超過率で運用停止条件を設定。
- `U15-4`: 停止/更新/例外承認/監査責任の4点を規約化し、ログ欠落時の応募停止条件を明示。

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` は不変。
- データ参照運用は `DOI + dataset名 + access区分` を正本とする方針を継続。
- 応募キー `G1-G6` の参照整合は維持。


## 今回の再検証ログ（2026-03-26 22:03 JST）

本runは「汎用要約ではなく、1問ずつ深掘りする」を維持するため、まず `60RQ` の整合監査を実施したうえで、深掘り対象を6件に固定しました。

再検証で確認したこと:

- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md`の`RQ見出し=60件`（`### Ux-y`形式）を再確認。
- 判定内訳は既存運用値 `A/B/C=17/25/18` を維持。
- 参照EEG ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）と `EEG-DATA/eeg_dataset_summary_ja.csv` の照合方針を再固定。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `auto-research-funds` 側で継続参照可能です。

今回の深掘り固定6RQ（実装優先順）:

1. `U4-2`（最小介入因果主張の事前登録）
2. `U7-3`（前処理差分手数料）
3. `U8-2`（再較正頻度と運用コストの境界）
4. `U13-5`（知覚/想起分岐での復元劣化）
5. `U14-5`（否定例レジストリ初版）
6. `U15-4`（停止条件/更新条件ガバナンス）

深掘り固定ルール（本実行継続）:

- `1RQ=1検証命題=1応募テーマ=1主データ`
- `C` 判定RQは性能主張をしない（制度/監査設計トラックで提出）
- 提出時のデータ参照は `DOI + dataset名 + access区分` を必須化

## 今回の再検証ログ（2026-03-25 04:02 JST）


本ページは、`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の60行を1行ずつ読み、各RQについて下記4点が埋まっていることを再確認した上で更新しています。

1. `検証可否`（`A/B/C` 判定と境界条件）
2. `auto-research-funds向け応募テーマ`
3. `推奨EEG-DATA`（主データセットID）
4. `提出成果物`（最低限の実装/監査アウトプット）

再検証時の固定ルール:

- 汎用横断の要約は作らず、`1RQ=1検証命題=1応募テーマ=1主データ` を優先
- `C` 判定RQは「EEG単独で不可」の理由（法務/制度/他モダリティ）を明記
- データセット参照はID再採番の影響を避けるため、提出時は `DOI + dataset名 + access区分` を必ず併記

2026-03-25 04:02 JST の再計数結果（機械検証）:

- `RQ件数`：`60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）
- `A/B/C`: `17/25/18`
- `参照EEG ID`：`17件`（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）
- `EEG ID欠落`：`0`（照合先：`EEG-DATA/eeg_dataset_summary_ja.csv`）
- `助成ID検証`: `G3-G6` は `auto-research-funds/wiki/cards/*.md` と `grant_eeg_dataset_match.csv` で欠落 `0`、`G1/G2` は本ページと `Mind-Upload-EEG-RQ-Grant-Map.md` の固定運用キーとして再確認（現在 `auto-research-funds` に `grant_queue/` は未配置）

## auto-research-fundsで使う応募レーン（本ページで参照した根拠）

- `若手研究助成` / `研究奨励金` / `一般研究助成` / `共同研究助成` / `博士課程研究助成`
- 根拠ファイル: `auto-research-funds/data/docs/research_funding_manual_additions_2026-03-14_run132.md`
- 根拠ファイル: `auto-research-funds/data/docs/research_funding_keio_grad_underfilled_2026-02-17.md`
- 根拠ファイル: `auto-research-funds/data/docs/research_funding_daily_codex_2026-03-07.md`

### 実務で使う助成キー（IDつき）

- `G1`: `GR-2026-013`（固定運用トラックID / 技術実証・再現性中心）
- `G2`: `GR-2026-014`（固定運用トラックID / 統合検証・社会実装中心）
- `G3`: `9Lx4dPK6a4k2gOb7`（研究助成（国内））
- `G4`: `Drbm6vBRDJkn0NGJ`（研究助成）
- `G5`: `871pw3rLjNPKgqA0`（研究助成金）
- `G6`: `46z9VPE4wnkrvEJR`（学術・研究助成）

### 助成キー実体（根拠系統を分離）

| 鍵 | 制度名 | 締切窓（根拠種別） | RQ60の使いどころ |
|---|---|---|---|
| G1 | `GR-2026-013`（応募トラックID。`Mind-Upload-EEG-RQ-Grant-Map`の固定キー） | `mind-upload/wiki` と `auto-research-funds/wiki` の同期管理値（`grant_queue` は現在未構成） | `U1/U4/U7/U13/U14` の技術検証を、再現性パッケージ付きで短中期成果として出す。 |
| G2 | `GR-2026-014`（応募トラックID。`Mind-Upload-EEG-RQ-Grant-Map`の固定キー） | `mind-upload/wiki` と `auto-research-funds/wiki` の同期管理値（`grant_queue` は現在未構成） | `U0/U3/U8/U10/U11/U12/U15` の統合設計・長期テーマを博士計画として束ねる。 |
| G3 | 大川情報通信基金 研究助成 (`9Lx4dPK6a4k2gOb7`) | 2025年度実績ベースの想定窓（2026年は要再確認） | 再現基盤・データ標準化寄りの `A` 判定RQ（U7/U14）を補助応募として出す。 |
| G4 | 成茂神経科学研究助成基金 (`Drbm6vBRDJkn0NGJ`) | 2022/11/18〜2023/02/17実績ベース（制度継続状況は不明） | 方法論高度化（因果・逆問題・デコード監査）として `U1/U4/U11/U13/U14` を中心に出す。 |
| G5 | 日本産業科学研究所 研究助成金 (`871pw3rLjNPKgqA0`) | 2025年度実績ベースの想定窓（2026年は要再確認） | `U8` の閉ループ運用・ドリフト対策の運用研究を小中規模実装として出す。 |
| G6 | 住友電工グループ社会貢献基金 学術・研究助成 (`46z9VPE4wnkrvEJR`) | 2025年度実績ベースの想定窓（2026年は要再確認） | `C` 判定RQ（U3/U10/U12/U15）で必要な制度・多モーダル連携の準備研究に使う。 |

- 参照ルール: `G1-G2` は `mind-upload/wiki` と `auto-research-funds/wiki` の同期キーとして扱い、`G3-G6` は `auto-research-funds/wiki/cards` と `grant_eeg_dataset_match.csv` を正本として扱います。

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

| RQタイプ（該当U） | 優先する脳波資源軸 | エントリーレポート（EEG-DATA） | まず使うデータ例 |
|---|---|---|---|
| 思考/運動意図の安定デコード（`U0/U8/U13`） | `motor imagery` `cross-session` `cross-subject` | `TARGET_TASK_REPORT.md` `BENCHMARK_SETUP_REPORT.md` | ID `6, 11, 696, 719` |
| 言語/意味復元と模倣分離（`U13`） | `reading-RSVP` `naturalistic stimulus` `reconstruction/decoding` | `LANGUAGE_PARADIGM_REPORT.md` `TASK_FORMULATION_REPORT.md` | ID `509, 13, 65` |
| 意識状態・睡眠・失敗条件（`U11/U15`） | `resting-state` `sleep` `EEG-fMRI` | `PARADIGM_FAMILY_REPORT.md` `MULTIMODAL_SETUP_REPORT.md` | ID `735, 842, 859` |
| 高解像度・逆問題・因果介入（`U1/U4`） | `high-density channel` `stimulation` `ground-truth` | `RECORDING_MODALITY_REPORT.md` `EXPERIMENT_REUSE_READINESS.md` | ID `56, 676, 1839` |
| 多モーダル整合と再現性運用（`U7/U14`） | `multimodal alignment` `access` `benchmark` | `MULTIMODAL_SETUP_REPORT.md` `EXPERIMENT_SHORTLISTS.md` | ID `6, 56, 783, 4878` |

### auto-research-funds向けテーマレーン拡張（G1-G6に加える候補）

| レーン | 候補ID（自動研究資金）の追加 | このページでの使い方 |
|---|---|---|
| 神経・認知・臨床脳波 | `1geD73ZENwB8yaor`、`lEYmRP97ng3perjO` | `U11/U15` で「臨床評価補助バイオマーカー化」を前面に出す。 |
| 医工学・AI・信号処理 | `1geD73Z9K2B8yaor` | `U1/U7/U13/U14` で「EEG分類・異常検知・再現性基盤」を強調。 |
| 高齢社会・リハビリ | `QKYgNPxZxN38bO1Z` | `U8/U11/U15` の睡眠・覚醒・注意維持介入の実装テーマに接続。 |
| 社会実装・防災・地域ヘルス | `46z9VPE6E0BrvEJR`、`1geD73ZE54B8yaor`、`1geD73Z6yq38yaor` | `U15` の制度統合・現場運用監査トラックとして提出。 |

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

> 重要（2026-03-15 08:00 JST 留意）:
> `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID` は再採番で変動するため、`ID -> データセット名` を固定参照として扱わないでください。応募書類・再現ログでは、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `D1-D16（DOI固定）` を正し、`DOI + データセット名 + access区分` を並行記します。

| ID | データセット |
|---|---|
| 6 | ワイヤレスEEGの取得遅延 |
| 11 | CSTE (クロスセッション/タスク EEG 生体認証) |
| 13 | マルチモーダルフュージョン EEG + アイトラッキング |
| 16 | ディープ ノンパラメトリック ベイジアン マルチモーダル センサーの融合 |
| 19 | HiPi ピン刺し刺激脳波計 |
| 29 | 縦断性失読症ERP |
| 39 | MAD マルチモーダル感情データセット |
| 49 | ドライバーの眠気の生理学的指標 |
| 56 | 脳内刺激 + HD-EEG (グラウンドトゥルース) |
| 65 | VICODEV 運転気晴らしマルチモーダル |
| 509 | 3M-CPSEED 顕在/無言/想像音声脳波計 |
| 676 | 同時EEG-fMRI XP1 |
| 696 | 縦方向 MI-BCI + 脊椎刺激 |
| 719 | ユビキタス P300 ベンチマーク |
| 735 | PK-NMM プロポフォール麻酔脳波シミュレーション |
| 783 | EEG-fNIRS同時作業記憶 |
| 842 | AAUWSS ウェアラブル睡眠研究 |
| 859 | DoC EEG バイオマーカー パイロット |
| 1011 | AlphaDirection1 EEG+ECG+PPG |
| 1839 | 小脳TMSEEGデータ |
| 1972 | 閉ループ聴覚刺激 (REM) |
| 2412 | NeuroSimo 閉ループ EEG/EMG ガイド付き TMS |
| 3419 | rTMS レスポンダー/ノンレスポンダー EEG |
| 4878 | EEG+PPG+GSR リハビリ疲労 |

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

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U0-1<br>同一性判定を『観測一致』と『介入応答一致』に分離したとき、どちらを必要条件・十分条件に置くか。 | A（直接検証可能） | 観測一致（EEG特徴量）と介入一致（刺激/課題変更時の応答）を分離して二軸ROCを作る。 | 若手研究助成（同一性KPI） | ID 11, 29, 696 |
| U0-2<br>時間同期（ms単位）と状態表現（行動・神経活動・生理）の対応をどう固定するか。 | A（直接検証可能） | ID 676/4878で時刻同期ずれと状態特徴量の崩れを同時に計測し、固定ルールを定義する。 | 研究奨励金（縦断同一性） | ID 11, 29, 696 |
| U0-3<br>同一性判定の閾値をタスク別にどう設定し、過学習モデルをどう除外するか。 | A（直接検証可能） | ID 11/696でタスク別に同一性閾値を推定し、過学習モデルはセッション外性能で除外する。 | 博士課程研究助成（個体同定） | ID 11, 29, 696 |
| U0-4<br>分岐/複製ケースでの『同一個体』定義をどの評価軸に帰着させるか。 | B（部分検証（外部データ併用で成立）） | ID 11/509で「同一個体判定」指標を生体同定精度に限定して運用限界を明記する。 | 共同研究助成（同一性×責任） | ID 11, 29, 696 |

## U1 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U1-1<br>EEG/MEG逆問題での不良設定性を、どの事前分布で制御するか。 | A（直接検証可能） | ID 56の既知刺激位置を使って、事前分布ごとの逆解誤差を比較する。 | 研究助成（逆問題ベンチ） | ID 56, 676, 1839 |
| U1-2<br>頭蓋導電率・電極配置・ノイズ構造の不確実性を、推定不確実性へどう伝播させるか。 | A（直接検証可能） | ID 56/1839で電極欠損・ノイズ注入を行い、不確実性伝播の校正曲線を作る。 | 若手研究助成（不確実性推定） | ID 56, 676, 1839 |
| U1-3<br>同じデータで異なる逆解法（MNE, beamformer, Champagne 等）が乖離した場合の判定規則をどう置くか。 | B（部分検証（外部データ併用で成立）） | ID 56/676でMNE/beamformer/Champagneの乖離率をタスク別に比較する。 | 研究奨励金（手法比較） | ID 56, 676, 1839 |
| U1-4<br>推定値だけでなく、信頼区間/後方分布を公開基準に含めるか。 | B（部分検証（外部データ併用で成立）） | 逆問題の信頼区間公開可否を、ID 56での後方分布再現性で評価する。 | 博士課程研究助成（後方分布公開） | ID 56, 676, 1839 |

## U3 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U3-1<br>ニューロン中心モデルに対して、グリア/体液性調節を追加した際の予測改善量をどう測るか。 | B（部分検証（外部データ併用で成立）） | ID 13/39でEEG単独 vs マルチモーダルの性能差を測り、境界拡張の必要量を推定する。 | 探索的若手研究助成（境界プロキシ） | ID 13, 16, 39 |
| U3-2<br>connectome完全性と機能予測性能の関係を、種横断でどう比較するか。 | B（部分検証（外部データ併用で成立）） | EEG-DATA単独ではconnectome完全性を直接検証できないため、補助指標としての再現性評価に限定する。 | 探索的若手研究助成（境界プロキシ） | ID 13, 16, 39 |
| U3-3<br>身体・環境結合を除去したモデルで失われる機能をどう定量化するか。 | B（部分検証（外部データ併用で成立）） | ID 16/39で身体・環境ループを含む条件差を比較し、除去時の性能低下を測る。 | 探索的若手研究助成（境界プロキシ） | ID 13, 16, 39 |
| U3-4<br>『必要最小構成』の判定を理論的主張ではなくデータでどう固定するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 必要最小構成の最終判定はEEG単独では不可。まずID 13/39で代理KPIを固定する。 | 探索的若手研究助成（境界プロキシ） | ID 13, 16, 39 |
| U3-5<br>glymphatic/meningeal lymphatic 系を含むとき、予測精度と説明可能性はどの程度改善するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | glymphatic/meningeal系はEEG-DATAに直接計測がなく、同時代謝データ併用前提の探索扱い。 | 探索的若手研究助成（境界プロキシ） | ID 13, 16, 39 |
| U3-6<br>免疫監視（髄膜免疫・炎症性シグナル）を除外したモデルは、どの時点で長期予測が破綻するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 免疫監視除外モデルの長期破綻はEEG-DATAだけでは不可。縦断臨床データの外部連携が必要。 | 探索的若手研究助成（境界プロキシ） | ID 13, 16, 39 |

## U4 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U4-1<br>観測データ由来の相関を因果グラフへ持ち上げる識別条件は何か。 | B（部分検証（外部データ併用で成立）） | ID 19/1839で入力操作に対する応答差を計測し、観測相関との差を分離する。 | 研究助成（介入同値） | ID 19, 56, 1839 |
| U4-2<br>介入実験（刺激・抑制・入力撹乱）で検証可能な最小因果主張は何か。 | A（直接検証可能） | ID 56の既知介入で最小因果主張を事前登録し、再現可否で判定する。 | 若手研究助成（グラウンドトゥルース介入） | ID 19, 56, 1839 |
| U4-3<br>active inferenceやDCMの理論予測を、反事実評価にどう接続するか。 | B（部分検証（外部データ併用で成立）） | ID 676を主に、介入あり/なしで反事実誤差（PEHE）と予測尤度差を比較し、理論順位を固定する。 | 研究奨励金（反事実評価） | ID 19, 56, 676 |
| U4-4<br>同値判定の失敗条件（falsification）をどの水準で宣言するか。 | B（部分検証（外部データ併用で成立）） | ID 19/56で `ΔAUC > 0.03` または `介入応答の符号反転率 > 10%` を失敗宣言閾値として事前登録する。 | 共同研究助成（反証設計） | ID 19, 56, 1839 |

## U7 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U7-1<br>BIDS拡張で同期・QC・刺激ログをどこまで必須化するか。 | A（直接検証可能） | ID 676/783で`clock offset` `sampling drift` `stimulus onset` `QC fail code`の4項目を必須変更、欠落時は省略させて頂きます。 | 研究助成（マルチモーダル標準化） | ID 676, 783, 4878 |
| U7-2<br>LSL等の時刻同期誤差を検証可能な指標に落とせるか。 | A（直接検証可能） | ID 6/676でジッタ/遅延の基準値を算出し、閾値超過を自動警告する。 | 若手研究助成（同期監査） | ID 676, 783, 4878 |
| U7-3<br>アーチファクト除去（ASR, ZapLine等）の設定差が結果へ与える影響をどう監査するか。 | A（直接検証可能） | ID 676/4878で前処理設定差分を再実行し、結果ドリフトを定量化する。 | 研究奨励金（前処理差分） | ID 676, 783, 4878 |
| U7-4<br>モダリティ間アライメント失敗時の再計測/除外基準をどう固定するか。 | A（直接検証可能） | ID 676/783でアライメント失敗時の再計測/除外条件を判定木化する。 | 共同研究助成（再計測基準） | ID 676, 783, 4878 |
| U7-5<br>前処理差分をCIで自動比較する場合、どの再現率低下をリリースブロック閾値にするか。 | A（直接検証可能） | ID 676で前処理CIを回し、基準パイプライン比で `再現率 -5pt` 以上低下を release block 閾値に固定する。 | 研究助成（CI再現性） | ID 676, 783, 4878 |
| U7-6<br>モダリティ欠損（EEG欠損・fMRI欠損）条件でも同等結論を保てる最小観測セットは何か。 | A（直接検証可能） | ID 676/783でEEG欠損・fMRI/fNIRS欠損をシミュレートし最小観測セットを求める。 | 研究助成（欠損ロバスト性） | ID 676, 783, 4878 |

## U8 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U8-1<br>閉ループBCIの遅延許容域を制御理論的にどう同定するか。 | B（部分検証（外部データ併用で成立）） | ID 6/1972で遅延・位相ずれに対する `安定率` `停止介入率` `回復時間` を測り、許容域を3指標で定義する。 | 若手研究助成（閉ループ安定化） | ID 6, 1972, 2412, 696 |
| U8-2<br>オンライン較正と概念ドリフト対策をどう組み込むか。 | B（部分検証（外部データ併用で成立）） | ID 2412/696でオンライン再較正の頻度と性能安定性を比較する。 | 研究奨励金（再較正） | ID 6, 1972, 2412, 696 |
| U8-3<br>個体差と日内変動をまたぐ安定性をどの指標で評価するか。 | B（部分検証（外部データ併用で成立）） | ID 696で個体内・個体間分散を分けて長期安定性KPIを設計する。 | 博士課程研究助成（長期ドリフト） | ID 6, 1972, 2412, 696 |
| U8-4<br>異常検知とフェイルセーフを評価契約へどう組み込むか。 | B（部分検証（外部データ併用で成立）） | ID 2412/1972で異常検知遅延とフェイルセーフ発動時間を測る。 | 共同研究助成（フェイルセーフ） | ID 6, 1972, 2412, 696 |
| U8-5<br>ヒューマンオーバーライドを導入したとき、誤作動率と回復時間をどうKPI化するか。 | B（部分検証（外部データ併用で成立）） | ID 2412で手動オーバーライド時の誤作動率と回復時間をKPI化する。 | 研究奨励金（オーバーライド） | ID 6, 1972, 2412, 696 |
| U8-6<br>週〜月スケール運用での再学習頻度を、性能劣化と安全余裕のトレードオフでどう最適化するか。 | B（部分検証（外部データ併用で成立）） | ID 696/2412で再学習間隔を変え、性能劣化と安全余裕のトレードオフを推定する。 | 研究助成（再学習最適化） | ID 6, 1972, 2412, 696 |

## U10 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U10-1<br>Landauer下限を神経計算でどう適用/解釈するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | Landauer下限の直接検証はEEG-DATA単独では不可。ID 735を理論整合の事前検証に使う。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |
| U10-2<br>非平衡熱力学指標と神経情報処理効率の対応をどう定義するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 非平衡熱力学指標の主評価は不可。ID 783/1011で代謝proxyとの弱い相関を探索する。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |
| U10-3<br>理論式を実データ（神経活動・代謝）へ落とし込む観測設計をどう作るか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 神経活動+代謝同時計測はID 783で部分検証可能だが、熱散逸実測は外部計測が必要。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |
| U10-4<br>WBE計算コスト評価に熱力学制約をどう統合するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | WBE計算コストへ熱制約を統合する実証はEEG-DATA外。ID 735でモデル妥当性確認まで。 | 理論研究奨励（情報熱力学） | ID 735, 783, 1011 |

## U11 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U11-1<br>理論間で比較可能な入出力仕様をどう定義するか。 | B（部分検証（外部データ併用で成立）） | ID 842/859で PCI近似・LZ複雑性・摂動応答の3指標を同一I/O仕様に揃え、順位保存率80%以上を採択条件にする。 | 研究助成（意識指標比較） | ID 735, 842, 859 |
| U11-2<br>PCIやIIT近似計算の計算量制約をどう扱うか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | IIT厳密計算は除外し、ID 735/842で `PCI近似` `LZ` `wSMI` を計算予算（1症例あたりGPU 2時間以内）付きで比較する。 | 理論研究奨励（IIT近似） | ID 735, 842, 859 |
| U11-3<br>理論予測の対立点を単一実験計画へどう落とすか。 | B（部分検証（外部データ併用で成立）） | ID 735/859で理論対立点を同一入力条件へ寄せる試験計画を作る。 | 共同研究助成（理論対立検証） | ID 735, 842, 859 |
| U11-4<br>意識指標を臨床/研究で運用する際の失敗条件をどう明示するか。 | B（部分検証（外部データ併用で成立）） | ID 859で偽陽性/偽陰性を含む臨床失敗条件の閾値を先に定義する。 | 臨床系若手助成（失敗条件定義） | ID 735, 842, 859 |

## U12 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U12-1<br>分岐後主体の識別子を何に基づいて付与するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 分岐後識別子の法的定義はEEG-DATA単独では不可。ID 11を技術IDの安定性評価に限定利用。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-2<br>責任・権利・同意の継承ルールをどの時点で分岐させるか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 責任・権利・同意の継承規則は制度設計課題であり、EEG-DATAは検証補助のみ。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-3<br>心理的連続性基準と法的個体基準の不一致をどう扱うか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 心理的連続性と法的個体の不一致はデータだけでは裁定できず、規範設計が主対象。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-4<br>技術評価（性能）と人格評価（帰属）をどう接続するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 性能KPIと人格帰属KPIの接続は法務要件が主で、EEGは監査ログ項目の補助。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-5<br>分岐主体間で記憶編集・再同期が起きた場合、法的主体IDを再編する基準は何か。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 記憶編集・再同期時のID再編ルールはEEGデータでは直接検証不可。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |
| U12-6<br>同意撤回が発生したとき、複数分岐主体への権限剥奪を技術的にどう実装・監査するか。 | C（EEG-DATA単独では不可（制度・他モダリティ必須）） | 同意撤回の権限剥奪監査はシステム設計課題で、EEG-DATAは模擬ログ検証まで。 | 制度・倫理系研究助成（技術監査接続） | ID 11, 509, 696 |

## U13 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U13-1<br>brain-to-text成功を『意味復元』と『因果再現』へ分解できるか。 | B（部分検証（外部データ併用で成立）） | ID 509でovert/imaginedを比較し、意味一致と因果一致の乖離を測る。 | 研究助成（模倣分離） | ID 509, 13, 65 |
| U13-2<br>LLMの幻覚・整合性検査を神経デコード評価へどう接続するか。 | B（部分検証（外部データ併用で成立）） | ID 13/65で行動整合と内部状態差を分離し、幻覚検査の接続点を作る。 | 若手研究助成（幻覚/内部状態差） | ID 509, 13, 65 |
| U13-3<br>同一出力でも内部機構が異なるケースをどう検出するか。 | B（部分検証（外部データ併用で成立）） | ID 65/509で同一出力・異内部状態ケースを抽出する判定器を設計する。 | 研究奨励金（shortcut検出） | ID 509, 13, 65 |
| U13-4<br>模倣性能の上限を因果評価でどこまで抑制できるか。 | B（部分検証（外部データ併用で成立）） | ID 509で模倣スコア単独合格を禁止し、因果整合指標との二重閾値を運用する。 | 研究助成（偶然統合KPI） | ID 509, 13, 65 |
| U13-5<br>視覚知覚と視覚想起で同一デコーダを使ったとき、意味復元精度の劣化パターンはどこで分岐するか。 | B（部分検証（外部データ併用で成立）） | ID 13を主に、知覚条件と想起条件で同一デコーダを適用し、精度低下の分岐点を推定する。 | 博士課程研究助成（知覚/想起分岐） | ID 13, 509, 65 |
| U13-6<br>プロンプト誘導・データリーク・shortcut学習を分離検出する対照実験をどう設計するか。 | B（部分検証（外部データ併用で成立）） | ID 65/13でリーク対照実験を設計し、shortcut検出率を評価する。 | 研究助成（リーク分離実験） | ID 509, 13, 65 |

## U14 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
|---|---|---|---|---|
| U14-1<br>データ/コード/評価環境の固定粒度をどこまで要求するか。 | A（直接検証可能） | ID 6で測定遅延再現試験を自動化し、最小追試パックの基礎にする。 | 研究助成（再現性運用） | ID 6, 56, 719 |
| U14-2<br>探索研究と検証研究を運用上どう分離するか。 | A（直接検証可能） | ID 56で探索/検証の分離運用を行い、同一条件再実行の再現率を示す。 | 研究奨励金（探索/検証分離） | ID 6, 56, 719 |
| U14-3<br>leaderboardでのリーク・過適合・報告バイアスをどう監査するか。 | A（直接検証可能） | ID 719でleaderboardリーク監査（被験者分割・時系列リーク）を定期化する。 | 若手研究助成（リーク監査） | ID 6, 56, 719 |
| U14-4<br>Model Card / Dataset Cardを評価契約へどう統合しますか。 | A（直接検証可能） | ID 719/56にModel Card・Dataset Card必須化を接続し監査項目化する。 | 研究助成（カード統合） | ID 6, 56, 719 |
| U14-5<br>再現失敗ケースを否定例レジストリとして公開し、再試行サイクルをどう運用するか。 | B（部分検証（外部データ併用で成立）） | `failure_id` `dataset_id` `split_hash` `failure_type` `rerun_status` を必須項目とした否定例レジストリを運用し、公開同意フローを併設します。 | 研究奨励金（否定例レジストリ） | ID 6, 56, 719 |
| U14-6<br>コンテナ固定（OS・依存ライブラリ・乱数種）を必須化した場合、再現コスト増分をどこまで許容するか。 | A（直接検証可能） | ID 719でコンテナ固定時の計算コスト増分を測定し、許容上限を設定する。 | 研究助成（再現コスト上限） | ID 6, 56, 719 |

## U15 リサーチクエスチョン（RQ単位）

| RQ | EEG-DATAで解けるか | 深掘り検証設計（1問ずつ） | auto-research-funds向け応募テーマ | 推奨脳波データ |
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

## 2026-03-18 12:02 JST 再検証ログ（本実行 / 依頼反省）

- 作業前に`auto-startup`の`main`で`git pull --ff-only`を実行し、最新状態を確認しました。
- `mind-upload/research_harvest_50.md`を正規として再照合し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、各RQに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が埋まっていることを再確認しました。
- 助成テーマは`G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を正本キーとして維持しました。
- EEG参照は引き続き `D1-D16 + DOI + データセット名 + access区分` を申請正本とし、数値IDは探索補助として扱います。
- 依頼方針どおり、汎用的な浅い横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の粒度で、各課題を個別に深掘りする運用をwiki正本に固定しました。

## 2026-03-18 13:01 JST 再検証ログ（本run / 深掘り方針の再固定）

- 作業前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、早送り不要（すでに最新です）を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` を正本に、`60RQ` すべてに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が1行ずつ埋まっている構造を再確認しました。
- 依頼方針どおり、横断的な一般論ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で扱う運用を維持し、各RQの「EEG-DATA単独で言える範囲」と「外部依存境界」を分離して提示する方針を固定しました。
- 応募先は `G1-G6` のキー運用を維持し、`A/B/C` 判定ごとに `A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を使い分ける設計を継続しました。
- wiki先は`mind-upload/wiki`と`mind-upload/github-wiki-export`、および`auto-research-funds/wiki`の3面同期を維持し、同じコンテンツで更新しました。

## 2026-03-18 14:02 JST 再検証ログ（本run / 3リポ同期確認）

- 作業前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull origin main` を実行し、当面最新化した検証を開始しました。
- `RQ60` の1問ずつ深掘り構造を再確認し、`検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` の4列が全行で埋まっていることを確認しました。
- 再計数結果は `RQ_TOTAL=60`、`A/B/C=17/25/18` で前回​​と一致しました（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）。
- 応募テーマの運用は `G1-G6` を維持し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を継続しました。
- 方針は引き続き `1RQ=1検証命題=1応募テーマ=1主データ` を固定し、汎用横断要約ではなくRQ単位での深掘りを正本運用としました。
- wiki先反映は`mind-upload/wiki` / `mind-upload/github-wiki-export` / `auto-research-funds/wiki`の3面同期を維持しました。



## 2026-03-18 15:12 JST 再検証ログ（本run / 依頼の再実行）

- 作業開始前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、最新化済み（すでに最新です）を確認しました。
- `mind-upload/research_harvest_50.md` を正本として、`RQ_TOTAL=60` と `U別内訳（4/4/6/4/6/6/4/4/6/6/6/4）` を再照合しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`と`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`を比較し、`1RQ=1検証命題=1応募テーマ=1主データ`の深掘り構造が維持されている事を確認しました。
- 判定内訳 `A/B/C=17/25/18`、および `G1-G6` の助成キー運用を継続し、EEG-DATAは各RQに対して主データを明示したまま維持しました。
- wikiは`mind-upload/wiki` / `mind-upload/github-wiki-export` / `auto-research-funds/wiki`の3面同期で更新しました。

## 2026-03-18 17:03 JST 再検証ログ（本run / 深掘り方針で再実行）

- 作業開始前に `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、最新化済み（すでに最新です）を確認しました。
- `mind-upload/research_harvest_50.md`を純正として、`RQ_TOTAL=60`と`U別内訳（U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4）`を再照合しました。
- `A/B/C=17/25/18` を再計数し、全RQに `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA`（Deep Evaluation Cards では `主張単位` `応募先` `最低成果物` を追加）が埋まっていることを確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 応募先は `G1-G6` を継続利用し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略を維持しました。
- wiki は `mind-upload/wiki` と `auto-research-funds/wiki` の両方に同期しました。

## 2026-03-18 17:18 JST 再検証ログ（本run / 依頼に対する最終固定）

- 作業開始前に`auto-startup`ルートで`git pull --ff-only origin main`を実行し、`Already up to date`を確認した上で検証を開始しました。
- `mind-upload/research_harvest_50.md`のRQ分解を正本として再照合し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 本ページの全RQ行について、`検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略区分を維持しました。
- 助成キーは`G1-G6`（`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`）を継続利用し、RQごとの応募テーマを固定しました。
- 依頼方針どおり、汎用的な全体要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用をwiki正本として維持しました。

## 2026-03-18 21:02 JST 再検証ログ（本run / EEG-DATA突合まで再確認）

- 作業開始前に`auto-startup`ルートで`git pull --ff-only origin main`を実行し、`Already up to date`を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`を再解析し、`RQ_TOTAL=60`と`U別内訳（U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4）`を再確認しました。
- `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- 本ページで参照するEEGデータID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、欠損IDが `0` 件であることを確認しました。
- 助成テーマは `G1-G6` のキー運用を継続し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携` の提出戦略区分を維持しました。
- 依頼方針どおり、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を再固定しました。

## 2026-03-18 22:02 JST 再検証ログ（本実行 / 依頼再実行）

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

## 2026-03-19 13:40 JST 再検証ログ（本実行 / 依頼再実行）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/research_harvest_50.md`を正規として`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再照合しました。
- 本ページのRQ行を再計数し、`A/B/C=17/25/18` を再確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を `grant_queue` / `auto-research-funds/wiki` で再確認しました。
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
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と突合し、`1RQ=1検証命題=1応募テーマ=1主データ` の統合を維持しました。
- EEG参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、未解決ID `0` を確認しました。

## 2026-03-19 09:05 JST 再検証ログ（本run / 3リポ最新化後の深掘り固定）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化した状態で検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`の`RQ`行を再計数し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- 主要EEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）は、最新 `EEG-DATA/eeg_dataset_summary_ja.csv` 上で17件すべて存在することを再確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 10:02 JST 再検証ログ（本run / EEG-DATA更新後の深掘り監査）

- 作業開始前に`auto-startup`親リポジトリで`git pull --ff-only origin main`を実行し、`Already up to date`を確認しました。
- 続けて`mind-upload` / `auto-research-funds` / `EEG-DATA`の各`main`で`git pull --ff-only origin main`を実行し、最新の差分を取り込んだ状態で検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`の`RQ`行を再計数し、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が欠損なく埋まっていることを確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と突合し、`1RQ=1検証命題=1応募テーマ=1主データ` の統合を維持しました。
- 主要EEG参照ID（`6, 11, 13, 19, 49, 56, 509, 676, 735`）は、最新 `EEG-DATA/eeg_dataset_summary_ja.csv` で欠損 `0` を確認しました。

## 2026-03-19 11:01 JST 再検証ログ（本実行 / 要求対応）

- 作業開始前に `auto-startup` 親リポジトリの `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/research_harvest_50.md`を正規として、`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再照合しました。
- 本ページのRQ行を再計数し、判定内訳 `A/B/C=17/25/18` を再確認しました。
- 依頼方針に合わせて、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持したまま、各RQの `EEG-DATAで言える範囲` と `外部依存境界` を再確認しました。
- 助成テーマは`G1-G6`（`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`）で維持し、`A=再現性実装` `B=統合検証計画` `C=制度/理論連携`の戦略提案を継続しました。
- wiki先として`auto-research-funds/wiki`、`mind-upload/wiki`、`mind-upload/github-wiki-export`の3面へ同じ内容の再検証ログを追記しました。

## 2026-03-19 12:02 JST 再検証ログ（本run / deep-by-RQ更新後の再監査）

- 作業開始時に`auto-startup` 親リポジトリの`main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて`mind-upload` / `auto-research-funds` / `EEG-DATA`の各`main`で`git pull --ff-only origin main`を実行し、最新化後に検証しました。
- `mind-upload` と `auto-research-funds` の対象wikiページで `RQ` 行を再計数し、いずれも `60` 件で一致することを確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持していることを確認しました。
- 主要EEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。



## 2026-03-19 13:02 JST 再検証ログ（本run / EEG-DATA更新後の深掘り再監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- 続けて`mind-upload` / `auto-research-funds` / `EEG-DATA`の各`main`で`git pull --ff-only origin main`を実行し、最新の差分（`mind-upload: f4965c8 -> ee2238d`、`auto-research-funds: 50d3928d8 -> 54f03a5cd`、`EEG-DATA: f09217e902a -> cbb11c31e42`）を取り込んだ状態で検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`を`Ux-y`行で再計数し、`RQ_TOTAL=60`と`A/B/C=17/25/18`を再確認しました。
- RQカードの `主データ/補助データ` から抽出したEEG参照ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`側も`Ux-y`行で`RQ_TOTAL=60`を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ`の深掘り同期を維持しました。

## 2026-03-19 14:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで再固定）

- 作業開始前に`auto-startup`親リポジトリで`git pull --ff-only origin main`を実行し、`Already up to date`を確認しました。
- 続けて`mind-upload` / `auto-research-funds` / `EEG-DATA`の各`main`で`git pull --ff-only origin main`を実行し、最新化後に再検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`Ux-y`行を再計数し、`RQ_TOTAL=60`と`A/B/C=17/25/18`を再確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` も同様に `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、両正本の整合を確認しました。
- 深掘り運用は `1RQ=1検証命題=1応募テーマ=1主データ` を維持し、汎用横断要約ではなく各RQを個別に固定した運用を継続しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。

## 2026-03-19 15:01 JST 再検証ログ（本run / ユーザー依頼の再実行）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/research_harvest_50.md`を正規として`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再照合しました。
- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `RQ行数=60` を突合し、`1RQ=1検証命題=1応募テーマ=1主データ` の統合を再確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 運用方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘りで更新しました。

## 2026-03-19 16:02 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りを再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて`mind-upload` / `auto-research-funds` / `EEG-DATA`の各`main`で`git pull --ff-only origin main`を実行し、最新化後に検証しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`、`mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`を突き合わせ、`RQ_TOTAL=60`と`A/B/C=17/25/18`の一致を再確認しました。
- RQ運用で参照するEEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 運用方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で、各課題を個別に深掘りして記述する形を維持しました。
## 2026-03-19 18:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りの再監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- 続けて`mind-upload` / `auto-research-funds` / `EEG-DATA`の各`main`で`git pull --ff-only origin main`を実行し、最新の差分（`mind-upload: 66e2f8a -> 2b43943`、`auto-research-funds: 382a5f90e -> 5a6eda781`、`EEG-DATA: 88c625b0b6f -> 76b2c83256b`）を取り込んだ状態で再検証しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` の走行を再計数し、`RQ_TOTAL=60` と `A/B/C=17/25/18` の一致を再確認しました。
- RQカードの `主データ/補助データ` から抽出したEEG参照ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を最新 `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 運用方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で各課題を個別に深掘りする形を維持しました。

## 2026-03-19 20:02 JST 再検証ログ（本run / ユーザー依頼: 1RQ深掘り固定でWiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- このページと`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`Ux-y`行を再計数し、`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否/深掘り検証設計/応募テーマ/推奨EEG-DATA` が埋まっていることを確認しました。
- RQ運用で使うEEG参照ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 汎用横断要約ではなく、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-19 21:01 JST 再検証ログ（本run / RQ60可否×助成テーマ再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only` を実行し、最新化済み（すでに最新です）を確認しました。
- 本ページの `| Ux-y<br>` 行を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）と `A/B/C=17/25/18` を再確認しました。
- 本ページ中の `ID nnn` を抽出して `EEG-DATA/eeg_dataset_summary_ja.csv` と再突合し、参照ID集合（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）の未解決 `0` 件を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` と件数・判定内訳が一致することを再確認し、deep-by-RQ同期を維持しました。

## 2026-03-19 22:01 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、すべて `RQ_TOTAL=60`、`A/B/C=17/25/18`、`missing=0`、`duplicate=0` を確認しました。
- 3ページで参照されるEEG ID（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と再照合し、未解決ID `0` を確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持したまま wiki 同期を更新しました。

## 2026-03-19 23:02 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りをwikiへ再同期）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`と`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`の`Ux-y`行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18`（欠損・重複`0`）を再確認しました。
- 本ページ中のEEG参照ID（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と再照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認しました。
- 方針は継続し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持したままwiki同期を更新しました。
## 2026-03-20 01:02 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りでwiki再同期）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`| Ux-yPH0X`行を再計数し、`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` も同じ `RQ_TOTAL=60` / `A/B/C=17/25/18` を再確認しました。
- RQ行から抽出したEEG参照ID集合（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 02:03 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りで更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`| Ux-yPH0X`行を再計数し、`RQ_TOTAL=60`と`A/B/C=17/25/18`（欠損・重複`0`）を再確認しました。
- RQ行から抽出したEEG参照ID（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` は `Ux-y` の物理行が `66`（深掘り優先6RQ の再掲あり）ですが、`unique RQ=60` を再確認し、このページとの整合性は維持されていることを保証します。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-20 04:02 JST 再検証ログ（本run / ユーザー依頼: 1問ずつ深掘りで更新）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only origin main` を実行し、最新化しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`Ux-y`行を再計数し、`RQ_TOTAL=60`と`A/B/C=17/25/18`（欠損・重複`0`）を再確認しました。
- 60RQの `主データ（ID）`（`6, 11, 13, 19, 49, 56, 509, 676, 735`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と突合し、未解決ID `0` を確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` 側と同一方針で同期し、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

### 本runの深掘り優先6RQ（応募テーマと主EEGデータ実名）

| RQ | 応募テーマ | 主脳波データ（ID / 名前） | 第一/予備応募先 |
|---|---|---|---|
| U14-1 | 追試運用の固定粒度監査 | `6` / ワイヤレス脳波の取得遅延 | `G1 / G3` |
| U7-2 | 時刻同期セキュリティ（オフセット/ジッター値） | `676` / 同時EEG-fMRI XP1 | `G1 / G3` |
| U14-3 | リーダーボードリーク監査 | `719` / ユビキタス P300 ベンチマーク | `G1 / G3` |
| U8-1 | 閉ループ遅延許容域同定 | `1972` / 閉ループ聴覚刺激 (REM) | `G2 / G5` |
| U8-2 | 再較正頻度最適化 | `2412` / NeuroSimo 閉ループ EEG/EMG ガイド付き TMS | `G2 / G5` |
| U13-1 | 模倣と因果の分離評価 | `509` / 3M-CPSEED 顕在/無言/想像音声脳波 | `G1 / G4` |

## 2026-03-20 08:01 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`の`| Ux-yPH0X`行を再計数し、`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否/深掘り検証設計/応募テーマ/推奨EEG-DATA` が埋まっていることを再確認しました。
- 参照EEG ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 09:04 JST 再検証ログ（本run / ユーザー依頼: RQ別深掘りでwiki再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`、`mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`の`Ux-y`行を再計数し、いずれも`RQ_TOTAL=60`（欠損・重複`0`）を確認しました。
- 判定内訳は `A/B/C=17/25/18` を再確認しました。
- Deep Evaluation Cards で参照されるEEG ID 一意セット（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 依頼方針どおり、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 10:03 JST 再検証ログ（本run / ユーザー依頼: 1問ずつ深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、3ページとも`RQ_TOTAL=60`（欠損・重複`0`）を確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認しました。
- RQ行由来のEEG参照ID集合（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 方針は不変で、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 12:03 JST 再検証ログ（本run / ユーザー依頼: 全RQを1件ずつ深掘りで再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`| Ux-yPH0X`行を再計数し、`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再計数し、全60行で `検証可否 / 深掘り検証設計 / 応募テーマ / 推奨EEG-DATA` が埋まっていることを再確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を `grant_queue` と `auto-research-funds` 側で再照合し、全ファイル存在を確認しました。
- 方針は維持し、汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続しました。

## 2026-03-20 13:02 JST 再検証ログ（本run / ユーザー依頼: 全RQを1件ずつ深掘りでwiki再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`| Ux-yPH0X`行を再計数し、`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、全60RQで `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 3ページ（`mind-upload`側2ページ + `auto-research-funds`側1ページ）で参照されるEEG ID一意セット（`6, 11, 13, 16, 19, 29, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1972, 2412`）を`EEG-DATA/eeg_dataset_summary_ja.csv`の`ID/旧ID`と照合し、未解決ID `0`を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を `grant_queue` と `auto-research-funds` 側で再照合し、全ファイル存在を確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」運用を継続します。

## 2026-03-20 15:02 JST 再検証ログ（本実行 / 1RQ深掘り固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を再計数し、`RQ_TOTAL=60` を再確認しました。
- 判定内訳は両ページで `A/B/C=17/25/18`（欠損・重複 `0`）を再確認しました。
- U別内訳 `U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`を再確認しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 2412`）は `EEG-DATA/eeg_dataset_summary_ja.csv` 照合で欠損 `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照を実在を `grant_queue/*.yaml` と `auto-research-funds/grant_eeg_dataset_match.csv` で再確認しました。
- 方針は継続して、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を固定しました。

## 2026-03-20 18:02 JST 再検証ログ（本実行 / 依頼：mind-upload RQをEEG-DATAで深掘り評価してwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-RQ60-Deep-Evaluation-Cards.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `Ux-y` 行を突合し、すべて `RQ_TOTAL=60`（欠損・重複 `0`）を確認しました。
- 判定内訳は4ページで `A/B/C=17/25/18` を再確認しました。
- 全RQで `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` の欠損 `0` を再確認しました。
- 依頼方針どおり、汎用横断ではなく `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。

## 2026-03-20 23:03 JST 再検証ログ（本run / ユーザー依頼: RQを1件ずつ深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `| Ux-yPH0X` を再計数し、3ページとも`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の運用が全行で維持されていることを確認しました。
- RQ行で参照されるEEG ID一意集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 助成キーは `G3-G6` を `auto-research-funds/wiki/cards/*.md` と `grant_eeg_dataset_match.csv` で照合し欠落 `0`、`G1/G2` は `mind-upload/wiki` と `auto-research-funds/wiki` の固定運用キーとして再確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」実行形で wiki 同期を維持しました。


## 2026-03-21 09:20 JST 再検証ログ（本実行 / EEG-DATA再採番対応）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull --ff-only origin main` を実行し、最新化した上で検証しました。
- `RQ_TOTAL=60` と `A/B/C=17/25/18` は維持される一方、`EEG-DATA/eeg_dataset_summary_ja.csv` 更新により旧数値IDの多くが再採番で無効化されることを確認しました。
- そのため本実行では、運用キーを `旧ID中心` から `DOI + データセット名 + access区分` へ再固定し、`D01-D24` の DOI アンカーを正本しました。
- `RQごとの深掘り` 方針（`1RQ=1検証命題=1応募テーマ=1主データ`）は維持し、助成テーマ紐付けは据え置きでデータ参照方法のみ更新しています。

### EEG-DATA DOIアンカー（2026-03-21運用）

| 鍵 | データセット（正本名） | 土肥 | 現在ID（探索補助） | 備考 |
|---|---|---|---:|---|
| D01 | ワイヤレスEEGの取得遅延 | `10.21227/dv1p-vq18` | 15962 | 旧ID `6` から再採番。 |
| D02 | CSTE: クロスセッションおよびクロスタスク EEG バイオメトリクス用のデータセット | `10.21227/j162-nh61` | 5311 | 旧ID `11` 対応。 |
| D03 | 心理実験における認知負荷評価のためのマルチモーダル融合システムのデータ: EEG および視線追跡研究 | `10.21227/6106-6120` | 10821 | 旧ID `13` 運用先。 |
| D04 | 没入型仮想現実におけるリアルタイムの動きと感情モデリングのためのディープ ノンパラメトリック ベイジアン マルチモーダル センサー融合法 | `10.21227/4fb5-7d89` | 10824 | 旧ID `16` 運用先。 |
| D05 | HiPi 後の脳波皮質反応: 高速ロボット制御のピン刺し刺激 | `10.21227/8snc-7h06` | 10826 | 旧ID `19` 運用先。 |
| D06 | ディスレクシアのある子どもとない子どもの縦断的作業記憶タスクからの ERP データ | `10.21227/r34y-c988` | 10831 | 旧ID `29` 運用先。 |
| D07 | ドライバーの眠気の生理学的指標 | `10.21227/rnms-3h47` | 10843 | 旧ID `49` 運用先。 |
| D08 | 人間の脳内刺激と HD-EEG の同時、音源位置特定手法のグラウンドトゥルース | `10.21227/7may-9q56` | 15972 | 旧ID `56` 運用先。 |
| D09 | VICODEV データセット – ダイナミック ドライビング シミュレーターにおける視覚と認知の注意散漫 | `10.21227/r8fc-2y40` | 1369 | 旧ID `65` 運用先。 |
| D10 | 3M-CPSEED: 顕在音声/無声音声/想像音声の脳波データセット | `10.18112/openneuro.ds006465.v2.0.0` | 1370 | 旧ID `509` 運用先。 |
| D11 | オンライン体験サンプリングを備えたマルチセッション同時 EEG-fMRI データセット | `10.18112/openneuro.ds007216.v1.0.0` | 35 | 旧ID `676` の運用代替。 |
| D12 | 経皮的脊髄刺激を伴う縦方向の MI-BCI トレーニング | `10.5281/zenodo.15454354` | 33 | 旧ID `696` 運用先。 |
| D13 | ユビキタス P300 ERP ベースの BCI アプリケーションに向けた新しいベンチマーク データセット | `10.17632/vyczny2r4w` | 536 | 旧ID `719` 運用先。 |
| D14 | プロポフォール麻酔中のPK-NMM脳波シミュレーション | `10.6084/m9.figshare.1485719` | 6111 | 旧ID `735` 運用先。 |
| D15 | 作業記憶負荷を調査するためのEEG-fNIRS同時データセット | `10.21227/tswy-m550` | 16223 | 旧ID `783` 運用先。 |
| D16 | オールボー大学ウェアラブル睡眠研究 (AAUWSS) | `10.5281/zenodo.16919070` | 5344 | 旧ID `842` 運用先。 |
| D17 | DoC EEG バイオマーカー パイロット (予備的な ML 結果検出) | `10.5281/zenodo.6951439` | 6159 | 旧ID `859` 運用先。 |
| D18 | AlphaDirection1: EEG、ECG、PPG (安静時 + 作業記憶) | `10.18112/openneuro.ds006848.v1.0.0` | 1374 | 旧ID `1011` 運用先。 |
| D19 | 小脳TMSEEGデータ | `10.6084/m9.figshare.13082495` | 1531 | 旧ID `1839` 運用先。 |
| D20 | REM振動をターゲットとした閉ループ聴覚刺激 | `10.5281/zenodo.10663994` | 2723 | 旧ID `1972` 運用先。 |
| D21 | NeuroSimo: 閉ループEEG/EMGガイド付きTMS | `10.5281/zenodo.14398633` | 6852 | 旧ID `2412` 運用先。 |
| D22 | rTMS 応答者/非応答者の EEG 後遺症 | `10.17632/vgbghtzvt2` | 7244 | 旧ID `3419` 運用先。 |
| D23 | リハビリテーション疲労検出のための EEG、PPG、GSR 信号 | `10.6084/m9.figshare.31169026` | 3530 | 旧ID `4878` 運用先。 |
| D24 | LLaMAC マルチモーダル感情コンピューティング データセット（MAD運用代替） | `10.6084/m9.figshare.28748696` | 4010 | 旧ID `39` の現行代替。 |

- 実務ルール: 応募書類・再現ログでは `Dxx + DOI + データセット名 + access区分` を正とし、`現在ID` は探索補助に限定します。


## 2026-03-21 10:04 JST 再検証ログ（本run / 依頼: RQを1件ずつ深掘りしwiki固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / 本ページ / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `| Ux-yPH0X` 行を再計数し、3 ページも `RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用が全行で維持されていることを確認しました。
- 本ページの再検証で参照した主要EEG ID（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6` は `mind-upload/wiki` と `auto-research-funds/wiki` の両方で再確認し、欠落 `0` を確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」運用を継続します。

## 2026-03-21 21:02 JST 再検証ログ（本run / 依頼: RQを1件ずつ深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / 本ページ / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、3ページとも `RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、全60RQで `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用が維持されていることを確認しました。
- 本ページのRQ行由来EEG参照ID一意集合（`6,11,13,16,19,29,39,49,56,65,509,676,696,719,735,783,842,859,1011,1839,1972,2412,3419,4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` と照合し、未解決ID `0` を確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」運用を継続します。

## 2026-03-21 22:02 JST 再検証ログ（本run / 依頼: RQごと深掘りで可否×助成テーマを再固定）

- `mind-upload/research_harvest_50.md`を正規として`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再照合しました。
- `A/B/C=17/25/18` を再計数し、全RQで `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` が埋まっていることを確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`と`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`に同じコンテンツを同期し、`1RQ=1検証命題=1応募テーマ=1主データ`の運用を再固定しました。
- 提出参照はID依存を避け、`DOI + dataset名 + access区分` を正本にする運用を継続します。

## 2026-03-21 23:26 JST 再検証ログ（本run / 依頼: 全RQを1件ずつ深掘りでwiki更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / 本ページ / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、3ページも `RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- `A/B/C=17/25/18` を再確認し、全RQで `検証可否` `深掘り検証設計` `応募テーマ` `推奨EEG-DATA` の欠損 `0` を確認しました。
- RQ行由来の主要EEG参照ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を `EEG-DATA/eeg_dataset_summary_ja.csv`（`ID/旧ID`）に照合し、未解決ID `0` を確認しました。
- 助成ID `9Lx4dPK6a4k2gOb7` `Drbm6vBRDJkn0NGJ` `871pw3rLjNPKgqA0` `46z9VPE4wnkrvEJR` は `auto-research-funds/wiki/cards/*.md` で実在を再確認し、`G1/G2` は運用固定キーとして継続しました。

### 本runで深掘り固定した4RQ（汎用横断ではなく1件ずつ）

| RQ | 深掘りした検証命題 | 主データ（EEG-DATA） | 応募テーマ（自動研究資金） | 応募先（第一/予備） |
|---|---|---|---|---|
| U1-2 | 導電率/電極配置/ノイズの不確実性が逆問題の信頼区間へどう伝播するかを、校正曲線で固定する。 | ID `56`（補助: `676, 1839`） | 不確実性推定・逆問題検証 | `G1 / G4` |
| U8-2 | 再較正頻度の3条件比較で、性能維持率と運用コストのトレードオフ境界を固定する。 | ID `6`（補助: `2412, 696`） | 閉ループ運用・再較正設計 | `G2 / G5` |
| U13-1 | 意味一致と因果一致を同一デコーダで分離し、模倣成功の過大主張を抑止する。 | ID `509`（補助: `13, 65`） | 模倣分離・漏れ統合KPI | `G1 / G4` |
| U15-2 | neurorights を監査ログ要件へ写像し、EEGは制度監査の技術証跡として限定使用する。 | ID `49`（補助: `2412, 3419`） | 制度設計・監査要件定義 | `G2 / G6` |

## 2026-03-22 JST 再検証ログ（本run / pull後のID再採番監査）

- 作業開始前に `auto-startup` / `mind-upload` / `EEG-DATA` / `auto-research-funds` の各 `main` で `git pull --ff-only origin main` を実行し、最新化してから再検証しました。
- `mind-upload/research_harvest_50.md`を正本として`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- `A/B/C=17/25/18` は維持されています（注: `A/B/C` は wiki側の運用判定であり `research_harvest_50.md` 本体の埋め込み値ではありません）。
- `EEG-DATA/eeg_dataset_summary_ja.csv` の更新後、RQ運用で参照していた数値IDは `存在自体はするが意味が変わる` 状態（再採番）になっていることを確認しました。
- そのため本runでは、`数値IDを正本扱いしない` ルールを再固定し、提出・再現ログでは `D01-D24 + DOI + データセット名 + access区分` を正とします。
- 既存の `ID` 列は探索補助の legacy スナップショットとしてのみ扱い、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用は維持します。
- 助成キー `G3/G5/G6` は最新カード上で 2026年度想定窓（`G3: 2026-04-21〜2026-07-10`, `G5: 2026-08-01〜2026-09-01`, `G6: 2026-04-03〜2026-06-06`）を再確認し、`G4` は予備キーとして継続運用します。

## 2026-03-22 02:03 JST 再検証ログ（本run / ユーザー依頼: RQを1件ずつ深掘りでwiki更新）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull --ff-only origin main` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-RQ60-Deep-Evaluation-Cards.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、4ページすべて `RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を4ページで再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用が維持されていることを確認しました。
- `mind-upload`側カードで参照しているEEG ID一意セット（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）を`EEG-DATA/eeg_dataset_summary_ja.csv`と突合し、未解決ID `0`を確認しました。
- `C`判定RQ（主に`U10/U12/U15`と`U3/U11`の一部）は、EEG特異では不可能という境界を維持し、`G2/G6`を中心に制度・理論連携トラックへ接続する方針を再固定しました。
- `A/B` 判定RQは、各行の `最低成果物`（監査レポート・リーク監査・閉ループKPI等）を提出単位として使う方針を維持し、汎用横断要約ではなくRQ単位での深掘り提出を継続します。

## 2026-03-22 JST 追加: RQ個票ディープノート（第2バッチ）

`1RQ=1検証命題=1応募テーマ=1主データ` の運用を維持したまま、本runでは `U4-3` `U11-1` `U15-2` の3件だけを本文で深掘りした。

| RQ | 判定 | 第一/予備応募先 | 主データ（Dアンカー） | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U4-3 | B | `G1 / G4` | `D05`（補助`D08`） | 介入あり/なしで `PEHE + log-likelihood` の二軸比較を固定し、理論順位の反転を停止条件に設定。 |
| U11-1 | B | `G2 / G4` | `D14`（補助`D16/D17`） | PCI近似/LZ/摂動応答の順位保存率を同一I/O条件で比較し、`80%` を運用閾値化。 |
| U15-2 | C | `G2 / G6` | `D07`（補助`D20/D21`） | neurorights条項を監査ログ項目へ写像し、同意撤回時の権限剥奪ログ欠損を停止条件に設定。 |

補足:

- 本文の旧ID表記は探索用。提出時は `Dxx + DOI + データセット名 + access区分` を正本として使う。
- 既存60RQの件数、`A/B/C=17/25/18`、および `G1-G6` の運用は変更していない。

## 2026-03-22 06:02 JST 再検証ログ（本run / CSV正本照合 + 6RQディープバッチ）

- `mind-upload/automation/rq_deepening_backlog_2026-03-01_enriched.csv`を正本として`U0-1..U15-4`の`RQ_TOTAL=60`を再照合し、`mind-upload/wiki`と`auto-research-funds/wiki`の4ページすべてで`missing=0 / extra=0`を確認しました。
- 判定内訳 `A/B/C=17/25/18` は維持され、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続します。
- 本runでは汎用横断要約を増やさず、下記6RQだけを追加で深掘り固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-2 | A | `D02`（補助`D11/D23`） | `G2 / G3` | ms同期ずれと状態表現崩れを同時計測し、`clock offset + jitter p95 + 表現崩壊率` の3指標を固定。 |
| U1-3 | B | `D08`（補助`D11/D19`） | `G1 / G4` | MNE/beamformer/Champagne の乖離率を `task別` に比較し、乖離時の採択規則（手法一致率閾値）を先に定義。 |
| U8-6 | B | `D12`（補助`D20/D21`） | `G2 / G5` | 再学習間隔（週次/隔週/月次）で `性能劣化速度` と `安全余裕` のトレードオフ曲線を固定。 |
| U10-3 | C | `D15`（補助`D12/D18`） | `G2 / G6` | 理論式→観測設計の写像を `proxy限定` で明示し、熱散逸実測が無い限界を申請本文に明記。 |
| U12-4 | C | `D02`（補助`D10/D12`） | `G2 / G6` | 分岐後同意撤回のイベント連鎖を `event_id/consent_state/revocation_latency` で監査可能化。 |
| U14-5 | B | `D13`（補助`D01/D08`） | `G1 / G3` | 否定例レジストリを `failure_id/split_hash/rerun_status` の必須列で運用し、再試行サイクルを固定。 |

補足:

- 旧数値IDは探索補助としてのみ扱い、提出物では `Dxx + DOI + データセット名 + access区分` を正本参照にします。
- 既存60RQの件数、A/B/C内訳、G1-G6運用キーは変更していません。

## 2026-03-22 09:01 JST 再検証ログ（本run / 1RQ深掘り固定の継続）

- 作業開始前に `auto-startup` / `mind-upload` / `EEG-DATA` / `auto-research-funds` / `auto-startup.wiki` で `git pull --ff-only` を実行し、最新化してから更新しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`を正本として`RQ_TOTAL=60`（`U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` は維持され、欠損・重複 `0` を再確認しました。
- 本runでは汎用を増やさず、`U0-3/U1-2/U7-3/U8-4/U13-2/U15-2`の6RQだけを深掘り対象として固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-3 | A | `D02`（補助`D11/D23`） | `G2 / G3` | タスク別閾値の外部検証一致率を固定し、過学習境界を再現可能な監査項目へ分解。 |
| U1-2 | A | `D08`（補助`D11/D19`） | `G1 / G4` | 不確実性伝播の校正誤差と区間被覆率を同時監査して、逆問題主張の範囲を限定。 |
| U7-3 | A | `D11`（補助`D12/D24`） | `G1 / G3` | 前処理差分起因の順位崩れをCIで監査し、再現性契約の必須設定項目を固定。 |
| U8-4 | B | `D20`（補助`D01/D21`） | `G2 / G5` | 異常検知遅延とフェイルセーフ発火率を同時計測し、閉ループ停止条件を運用化。 |
| U13-2 | B | `D10`（補助`D03/D09`） | `G1 / G4` | 幻覚テストと神経状態差の効果量整合を検証し、模倣分離主張の過大化を抑制。 |
| U15-2 | C | `D07`（補助`D20/D21`） | `G2 / G6` | neurorights条項を監査ログ項目へ写像し、同意撤回の技術監査可能性を最低成果物化。 |

補足:

- 数値IDは探索補助のみとし、提出時は `Dxx + DOI + データセット名 + access区分` を正本参照にします。
- 既存60RQの件数、A/B/C内訳、G1-G6運用キーは変更していません。

## 2026-03-22 12:02 JST 再検証ログ（本run / 6RQディープバッチ追加）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull --ff-only origin main` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / 本ページ / `auto-research-funds/wiki/Mind-Upload-RQ60-Deep-Evaluation-Cards.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、4ページすべて `RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を4ページで再計数し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用が維持されていることを確認しました。
- 本runでは汎用横断概要を増やさず、`U3-6/U4-1/U7-5/U10-1/U12-5/U14-2`の6RQだけを追加で深掘り固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U3-6 | C | `D03`（補助`D04/D24`） | `G2 / G6` | 免疫監視除外モデルの長期破綻を `ドメイン外劣化率` と `再同期不能率` で proxy 監査し、EEG単独主張の上限を明文化。 |
| U4-1 | B | `D05`（補助`D08/D19`） | `G1 / G4` | 観測相関と介入応答の乖離を `ΔAUC` と `介入符号一致率` で分離し、因果主張の採択境界を固定。 |
| U7-5 | A | `D11`（補助`D15/D23`） | `G1 / G3` | 前処理CIで `再現率低下-5pt` の release block を実運用し、誤ブロック率を併記して閾値妥当性を監査。 |
| U10-1 | C | `D14`（補助`D15/D18`） | `G2 / G6` | Landauer下限は理論主張に限定し、EEGでは `理論整合proxy` のみを成果物化する境界を明示。 |
| U12-5 | C | `D02`（補助`D10/D12`） | `G2 / G6` | 分岐主体の記憶編集/再同期イベントを `subject_branch_id/consent_state/relink_trace` で監査し、法的ID再編は外部依存へ分離。 |
| U14-2 | A | `D01`（補助`D08/D13`） | `G1 / G3` | 探索系と検証系の実験トラックを分離し、`split固定率` と `追試成功率` を同時KPIとして運用固定。 |

補足:

- 数値IDは探索補助のみとし、提出時は `Dxx + DOI + データセット名 + access区分` を正本参照にします。
- 既存60RQの件数、A/B/C内訳、G1-G6運用キーは変更していません。

## 2026-03-25 02:03 JST 再検証ログ（本run / 6RQディープバッチ追加）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull --ff-only origin main` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` とこのページの `unique Ux-y` を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` は維持され、`1RQ=1検証命題=1応募テーマ=1主データ` の運用を継続します。
- 本実行は広範囲にわたって更新ではなく、とりあえずバッチと重複しない`U0-4/U1-4/U8-5/U11-4/U13-6/U15-3`の6RQを深掘り対象として固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-4 | B | `D02`（補助`D10/D12`） | `G2 / G3` | 分岐/複製ケースの同一個体判定を `観測一致` と `介入一致` へ分離し、技術同一性の到達上限を先に明文化。 |
| U1-4 | B | `D08`（補助`D11/D19`） | `G1 / G4` | 逆問題の推定値だけでなく `後方分布` `区間被覆率` を提出必須にし、再解析一致率を採択条件に固定。 |
| U8-5 | B | `D21`（補助`D20/D12`） | `G2 / G5` | ヒューマンオーバーライド時の `誤作動率` `回復時間` `再発率` を同時計測し、運用停止条件を監査可能化。 |
| U11-4 | B | `D15`（補助`D16/D17`） | `G2 / G4` | 意識指標の運用で `偽陽性/偽陰性` の失敗条件を先宣言し、閾値変更時の再評価手順まで固定。 |
| U13-6 | B | `D10`（補助`D03/D09`） | `G1 / G4` | prompt誘導・データリーク・shortcut学習を分離する対照実験を固定し、`リーク検出率` を最低成果物へ接続。 |
| U15-3 | C | `D07`（補助`D21/D22`） | `G2 / G6` | 法域差（EU/US/JP）を跨ぐ最小共通運用を `監査イベント項目` 単位で比較し、EEGは補助証跡に限定する境界を明示。 |

- 提出時のデータ参照は引き続き `D01-D24 + DOI + データセット名 + access区分` を正本とし、数値IDは探索補助として扱います。

## 2026-03-25 02:36 JST 再検証ログ（本run / 6RQディープバッチ追加）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull --ff-only` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` とこのページの `unique Ux-y` を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` は維持され、`1RQ=1検証命題=1応募テーマ=1主データ` の運用を継続します。
- 本runは包括的更新ではなく、`U3-5/U7-6/U10-4/U12-6/U13-5/U14-6`を深掘り対象として固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U3-5 | C | `D03`（補助`D04/D24`） | `G2 / G6` | 境界拡張proxyを「統合条件と単体条件の差分KPI」で固定し、EEG単独主張の上限を先に明文化。 |
| U7-6 | A | `D11`（補助`D15/D23`） | `G1 / G3` | モダリティ欠損時の結論一致率と安全警告再現率を同時計測し、最小観測セットを運用閾値付きで定義。 |
| U10-4 | C | `D14`（補助`D15/D18`） | `G2 / G6` | 情報熱力学制約をWBE計算コストへ写像するproxy指標を固定し、理論整合が崩れる停止条件を明示。 |
| U12-6 | C | `D02`（補助`D10/D12`） | `G2 / G6` | 分岐主体への同意撤回伝播を `branch_id/consent_state/evidence_hash` で監査可能にし、制度判断と技術監査を分離。 |
| U13-5 | B | `D03`（補助`D10/D09`） | `G1 / G4` | 知覚/想起で同一デコーダを適用し、意味復元劣化の分岐点をセッション横断で固定する手順を確定。 |
| U14-6 | A | `D01`（補助`D08/D13`） | `G1 / G3` | コンテナ固定による再現率改善と計算コスト増分を同一KPI枠で監査し、許容上限を提出条件化。 |

- 提出時のデータ参照は引き続き `Dxx + DOI + データセット名 + access区分` を正本とし、数値IDは探索補助として扱います。

## 今回の深掘り実行パック（2026-03-25 03:03 JST, 2週間で初回結果まで）

汎用横断の更新ではなく、今回は直近runと重複しない `6RQ` を固定し、`1RQ=1検証命題=1応募テーマ=1主データ` で深掘りします。

| RQ | 選定理由（1件ずつ深掘りする理由） | 最初の実験KPI | 失敗条件（このrunでの停止条件） | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|---|
| U0-1 | 同一性判定の基礎で、二軸閾値を固定するとU0全体の判定基盤を再利用できる。 | `観測一致AUC` `介入一致率` `閾値安定性` | 介入条件変更で一致率が閾値未満になり、閾値がセッション間で再現しない。 | アイデンティティ KPI 2 軸ベースライン カード | `G2 / G3` |
| U3-2 | EEG単独で言える境界を明示しつつ、外部連携が必要な理由を定量化できる。 | `統合条件対単体条件のΔAUC` `proxy再現率` | proxy差分が再現せず、外部依存境界を主張できない。 | 境界拡張評価レポート（単体・統合比較） | `G2 / G6` |
| U7-4 | 再計測/除外ルールの判定木化は、再現運用契約へ直接転記しやすい。 | `判定木一致率` `再計測成功率` `除外妥当率` | 同条件で判定が分岐し、運用契約として固定できない。 | 再現性監査レポート（同期/QC/前処理差異） | `G1 / G3` |
| U10-2 | 理論主張の過大化を防ぎ、proxy段階の提出境界を明確化できる。 | `理論proxy相関` `符号一致率` `条件間安定性` | proxy対応方向が反転し、理論整合の再現が維持できない。 | 理論整合性メモと代理相関分析 | `G2 / G6` |
| U12-1 | 分岐主体IDの監査鎖を先に作ると、U12全体の制度接続設計に再利用できる。 | `lineage追跡率` `同意状態整合率` `監査欠損率` | lineage追跡が一意化できず、同意状態との対応が監査ログで再現できない。 | システム監査要件表（テクニカルログ対応） | `G2 / G6` |
| U13-3 | 出力一致だけでは判定できない問題を、乖離ケース抽出で具体化できる。 | `意味一致率` `因果一致率` `乖離ケース再現率` | 乖離ケース抽出が不安定で、対照条件で再現しない。 | ミミック分離評価スクリプトと制御条件テーブル | `G1 / G4` |

実行順（本実行固定）:

1. `U0-1`
2. `U7-4`
3. `U3-2`
4. `U13-3`
5. `U10-2`
6. `U12-1`

## 今回の再検証ログ（2026-03-25 03:03 JST）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の各 `main` で `git pull --ff-only` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` / `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md` / `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `unique Ux-y` を再計数し、3ページとも`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 本runは汎用横断概要ではなく、`U0-1/U3-2/U7-4/U10-2/U12-1/U13-3`の6RQだけを新規ディープバッチとして追加しました。
- 提出時データ参照は引き続き `Dxx + DOI + データセット名 + access区分` を正本とし、数値IDは探索補助として扱います。

## 2026-03-26 13:26 JST 再検証ログ（本run / 6RQディープバッチ追加）

- 作業開始前に `auto-startup` の `main` で `git pull --rebase --autostash origin main` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` の `### Ux-y` を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を維持し、`1RQ=1検証命題=1応募テーマ=1主データ` の運用を継続します。
- `EEG-DATA/eeg_dataset_summary_ja.csv` で本ページ参照の24件（`6,11,13,16,19,29,39,49,56,65,509,676,696,719,735,783,842,859,1011,1839,1972,2412,3419,4878`）を再照合し、欠落 `0` を確認しました。
- `auto-research-funds`側では`G1-G6`と拡張候補ID（`1geD73ZENwB8yaor`, `lEYmRP97ng3perjO`, `1geD73Z9K2B8yaor`, `QKYgNPxZxN38bO1Z`, `46z9VPE6E0BrvEJR`, `1geD73ZE54B8yaor`, `1geD73Z6yq38yaor`）の実在参照を再確認しました。
- 追加確認として、上記24件の数値IDは `現行ID` と `旧ID` の両方に現れるため、裸の数値参照は曖昧です。提出・再現ログの主キーは引き続き `Dxx + DOI` を使用し、`ID` は探索補助に限定します。
- 本runは包括的更新ではなく、`U0-2/U1-3/U4-4/U8-2/U11-1/U14-5`を深掘り対象として固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-2 | A | `D02`（補助`D11/D23`） | `G2 / G3` | ms同期ずれを `offset/jitter` 分布で固定し、同一性判定で許容する同期誤差上限を運用条件へ接続。 |
| U1-3 | B | `D08`（補助`D11/D19`） | `G1 / G4` | 逆解法間乖離を手法順位一致率で監査し、順位反転が起きる条件を提出前に明示。 |
| U4-4 | B | `D05`（補助`D08/D19`） | `G1 / G4` | 最小介入主張を `反証条件` 先行で固定し、観測相関だけでは採択しない停止規則を明文化。 |
| U8-2 | B | `D20`（補助`D01/D21`） | `G2 / G5` | 個体差・日内変動を跨ぐ再較正負荷を `回復時間` と `停止介入率` の同時計測で管理。 |
| U11-1 | B | `D14`（補助`D16/D17`） | `G2 / G4` | 意識指標比較で `失敗条件付き理論比較` を固定し、順位保存不能ケースを否定例として先に登録。 |
| U14-5 | B | `D01`（補助`D08/D13`） | `G1 / G3` | 否定例レジストリを `split_hash` と `rerun_status` まで必須化し、追試不能ケースを公開前提で監査。 |

- 提出時データ参照は継続して `Dxx + DOI + データセット名 + access区分` を正本とし、数値IDは探索補助として扱います。

## 2026-03-25 13:03 JST 再検証ログ（本run / 6RQディープバッチ追加）

- 作業開始前に `auto-startup` / `mind-upload` / `auto-research-funds` / `EEG-DATA` の `main` で `git pull --rebase origin main` を実行し、最新化を確認しました。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` を正本として `RQ_TOTAL=60`（欠損・重複 `0`）を再計数しました。
- 判定内訳 `A/B/C=17/25/18`、U内訳 `U0=4 U1=4 U3=6 U4=4 U7=6 U8=6 U10=4 U11=4 U12=6 U13=6 U14=6 U15=4`を機械的に再確認しました。
- `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の参照キーは `D01-D24` が連番で欠落 `0`、`G1-G6` も欠落 `0` を再確認しました。
- `EEG-DATA/eeg_dataset_summary_ja.csv` に対して、本ページ掲載の24ID（探索補助）がすべて存在することを確認しました（欠落 `0`）。
- 本runは汎用的な更新ではなく、`U1-2/U4-2/U8-3/U11-3/U14-4/U15-1`の6RQだけを深掘り対象として固定しました。

| RQ | 判定 | 主データ（ID） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U1-2 | A | `56` | `G1 / G4` | 逆問題の不確実性伝播を `誤差 + 区間被覆率` で固定し、再解析で一致しない場合は主張を下方修正する停止条件を先に宣言。 |
| U4-2 | A | `19` | `G1 / G4` | 介入あり/なし比較で `反事実の符号一致率` を必須KPI化し、因果主張を観測相関から分離して提出可能化。 |
| U8-3 | B | `6` | `G2 / G5` | 日内変動・個体差を跨ぐ運用で `安全停止率 + 回復時間` を同時計測し、外部運用要件が未接続なら部分成立に止める。 |
| U11-3 | B | `735` | `G2 / G4` | 理論対立を単一実験計画へ圧縮し、指標順位が反転する条件を失敗条件として先に固定。 |
| U14-4 | A | `6` | `G1 / G3` | Model/Dataset Card を評価契約へ統合し、再現失敗時の追試ルートをカード項目単位で提出テンプレ化。 |
| U15-1 | C | `49` | `G2 / G6` | 神経データの機微性分類は制度依存であることを明示し、EEGは補助証跡として監査ログ設計に限定する境界を固定。 |

- 提出時データ参照は引き続き `Dxx + DOI + データセット名 + access区分` を正本とし、数値IDは探索補助として扱います。

## 2026-03-26 14:20 JST 再検証ログ（本run / 助成締切の具体日付更新）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --rebase --autostash origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/research_harvest_50.md`と`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`を突き合わせ、`RQ_TOTAL=60`と`A/B/C=17/25/18`の一致を再確認しました。
- 助成締切の記載を「推定」だけにしないため、確認できた具体日付を運用ログに固定しました。
  - くら基金 若手研究者奨励助成: `2026-02-02` 〜 `2026-04-17`
  - ブレインサイエンス振興財団 海外派遣研究助成: 締切 `2026-01-09`（派遣対象 `2026-04-01` 〜 `2027-03-31`）
  - 中谷財団 交流助成（直近観測）: `2025-04-30` / `2025-08-29` / `2025-09-16` / `2025-12-26`
  - SCAT研究奨励金（直近観測）: `2025-08-01` 〜 `2025-11-28`（`2026-11-29` は予測値として区別）
- 方針は継続で、汎用要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を維持し、`C` 判定RQは制度・法務依存を明示して過剰主張を避けます。


## 2026-03-26 12:03 JST 再検証ログ（本run / RQ単位深掘りの整合監査）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`と`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`の`| Ux-yPH0X`行を再計数し、両方の`RQ_TOTAL=60`（欠損・重複`0`）を確認しました。
- 判定内訳は双方で `A/B/C=17/25/18` を再確認し、`1RQ=1検証命題=1応募テーマ=1主データ` の運用を維持しました。
- 参照EEG ID（`6,11,13,16,19,29,39,49,56,65,509,676,696,719,735,783,842,859,1011,1839,1972,2412,3419,4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` と照合し、欠落 `0` を確認しました。
- 助成キー `G3-G6` のカード実体（`9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `auto-research-funds/wiki/cards/` で存在確認済みです。
- 本実行は広範囲に更新を増やさず、次の 6RQ を深掘り優先キューとして固定します: `U0-4`、`U1-1`、`U4-2`、`U8-1`、`U13-3`、`U14-3`。

## 2026-03-27 15:03 JST 再検証ログ（本run / 6RQディープバッチ追加）

- 本ランは汎用横断概要ではなく、`U0-2/U1-4/U3-4/U8-4/U12-2/U14-5`の6RQを深掘り対象として固定しました。
- 各RQで `EEGで確定できる最小境界` と `外部依存境界` を分離し、`1RQ=1検証命題=1応募テーマ=1主データ` の運用を維持しました。
- 参照ID（`6, 11, 13, 16, 29, 39, 56, 509, 676, 696, 719, 1839, 1972, 2412`）は最新 `EEG-DATA/eeg_dataset_summary_ja.csv` で欠落 `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認しました。

## 今回の再検証ログ（2026-03-27 21:03 JST）

本runでは、`60RQ` の全件マップを維持したまま、汎用横断サマリを増やさず `1RQ=1検証命題=1応募テーマ=1主データ` で非重複6RQを深掘り固定しました。

更新したこと（RQ単位）:

- `U0-3`（A）: タスク別閾値と過学習除外条件を、セッション外性能を基準に固定。
- `U1-3`（B）: MNE/beamformer/Champagne の乖離率比較を、判定規則の一次根拠として固定。
- `U3-4`（C）: 必要最小構成はEEG単独で確定しない前提を明示し、代理KPI運用へ境界固定。
- `U8-4`（B）: 異常検知遅延とフェイルセーフ発動時間を同時KPIにして評価契約へ接続。
- `U13-4`（B）: 模倣スコア単独合格を禁止し、因果整合との二重閾値を固定。
- `U14-4`（A）：モデルカード/データセットカードを監査必須項目として契約統合する運用へ固定。

本実行固定6RQ（深掘り順）:

1. `U0-3` - 博士課程研究助成（個体同定） / `G2 / G3` / 主データ `ID 11`
2. `U1-3` - 研究奨励金（手法比較） / `G1 / G4` / 主データ `ID 56`
3. `U3-4` - 探索的若手研究助成（境界 proxy） / `G2 / G6` / 主データ `ID 13`
4. `U8-4` - 共同研究助成（フェイルセーフ） / `G2 / G5` / 主データ `ID 6`
5. `U13-4` - 研究助成（因果整合KPI） / `G1 / G4` / 主データ `ID 509`
6. `U14-4` - 研究助成（カード統合） / `G1 / G3` / 主データ `ID 6`

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` は不変。
- 参照EEG IDセット（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）は欠損`0`。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を維持。

## 今回の再検証ログ（2026-03-28 02:02 JST）

- 作業開始時に`auto-startup` / `mind-upload` / `EEG-DATA` / `auto-research-funds` で `git pull --ff-only origin main` を実行し、全リポジトリを最新化しました。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` の `### Ux-y` を再計数し、`RQ_TOTAL=60`（欠損 `0` / 重複 `0`）を再確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を再計数し、判定内訳 `A/B/C=17/25/18` を維持していることを確認しました。
- 本実行は包括的横断概要を増やさず、`U0-4/U1-1/U3-3/U8-6/U12-4/U15-4`の6RQだけを深掘り対象として固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-4 | B | `D02`（補助`D10/D12`） | `G2 / G3` | 分岐/複製ケースの同一性主張を「観測一致」「介入一致」の二軸に固定し、片軸のみの合格を禁止する評価規約を明文化。 |
| U1-1 | A | `D08`（補助`D11/D19`） | `G1 / G4` | 逆問題の事前分布比較を、誤差最小だけでなく区間被覆率と手法順位一致率まで必須化し、再解析での反転を停止条件に設定。 |
| U3-3 | B | `D03`（補助`D04/D24`） | `G2 / G6` | 身体・環境結合を除いたときの性能低下を単一精度ではなく「統合条件との差分KPI」で定義し、EEG単独主張の上限を先に固定。 |
| U8-6 | B | `D20`（補助`D21/D22`） | `G2 / G5` | 週〜月運用の再学習頻度を、性能劣化率と安全余裕（停止介入率/回復時間）のトレードオフで最適化する運用手順を固定。 |
| U12-4 | C | `D02`（補助`D10/D12`） | `G2 / G6` | 技術評価KPIと人間帰属KPIの接続を`branch_id/consent_state/evidence_hash`監査鎖で実装可能、法制度判断は外部依存として分離。 |
| U15-4 | C | `D07`（補助`D20/D21`） | `G2 / G6` | 停止条件・更新条件のガバナンスを監査イベント単位で定義し、EEGはリスク閾値の補助証跡に限定する境界を固定。 |

- 参照ID（`6,11,13,16,29,39,49,56,509,676,696,1839,1972,2412,3419`）は `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` で欠落 `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認しました。
- 提出時の正本参照は継続して `Dxx + DOI + データセット名 + access区分` を使用し、数値IDは探索補助とします。

## 今回の再検証ログ（2026-03-28 07:02 JST）

- 作業開始時に `auto-startup` / `mind-upload` / `EEG-DATA` / `auto-research-funds` の各 `main` で `git pull --ff-only origin main` を実行し、最新化してから再検証しました。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` の `### Ux-y` を再計数し、`RQ_TOTAL=60`（欠損 `0` / 重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` は不変で、`1RQ=1検証命題=1応募テーマ=1主データ` の運用を継続します。
- 本実行は包括的な概要を増やるだけ、とりあえずバッチ（`U0-4/U1-1/U3-3/U8-6/U12-4/U15-4`）と重複しない `U0-2/U1-4/U4-3/U7-1/U13-2/U14-5` の6RQを深掘り対象として固定しました。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-2 | A | `D02`（補助`D11/D23`） | `G2 / G3` | ms同期ずれを `offset/jitter` 分布で固定し、同一性判定で許容する時刻誤差上限を運用条件へ接続。 |
| U1-4 | B | `D08`（補助`D11/D19`） | `G1 / G4` | 逆問題で推定値のみ合格を禁止し、`後方分布公開` と `区間被覆率` を提出必須に固定。 |
| U4-3 | B | `D05`（補助`D08/D19`） | `G1 / G4` | active inference/DCM の理論予測を反事実誤差へ接続し、理論順位の反転条件を停止条件として先に宣言。 |
| U7-1 | A | `D11`（補助`D15/D23`） | `G1 / G3` | BIDS拡張で`clock offset/sampling drift/stimulus onset/QC fail code`を必須設定、欠落時は停止する監査運用を固定。 |
| U13-2 | B | `D10`（補助`D03/D09`） | `G1 / G4` | 模倣判定を `意味一致` と `因果一致` の二軸で評価し、片軸のみ高得点の過大主張を遮断。 |
| U14-5 | B | `D01`（補助`D08/D13`） | `G1 / G3` | 否定例レジストリを`failure_id/dataset_doi/split_hash/rerun_status`で固定し、再試行SLAを提案要件に組み込む。 |

- 参照データの正本は継続して `Dxx + DOI + データセット名 + access区分` とし、数値IDは探索補助として扱います。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認しました。

## 今回の再検証ログ（2026-03-28 08:02 JST）

- 作業開始前に `auto-startup` / `mind-upload` / `EEG-DATA` / `auto-research-funds` の `main` をプルしてから再検証しました（`auto-startup` と `mind-upload` はローカル変更保護のため `--autostash` を使用）。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` の `### Ux-y` を再計数し、`RQ_TOTAL=60`（欠損 `0` / 重複 `0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` は不変で、`1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を継続します。
- 本実行は包括的な概要を増やさず、バッチと重複しにくい `U0-1/U1-2/U4-4/U8-2/U12-3/U15-4` の 6RQ を固定して深掘りします。

| RQ | 判定 | 主データ（Dアンカー） | 第一/予備応募先 | 今回固定した深掘りポイント |
|---|---|---|---|---|
| U0-1 | A | `D02`（補助`D11/D23`） | `G2 / G3` | 同一性判定を `観測一致` と `介入一致` の二軸ROCで固定し、片軸のみ成立の合格を禁止。 |
| U1-2 | A | `D08`（補助`D11/D19`） | `G1 / G4` | 導電率・電極欠損・ノイズ注入の3摂動で `区間被覆率` と `誤差増分` を同時監査し、不確実性伝播の採択条件を固定。 |
| U4-4 | B | `D05`（補助`D08/D19`） | `G1 / G4` | 反証閾値（`反事実誤差` `符号反転率`）を先に宣言し、条件別に閾値が揺れる場合は因果主張を降格する運用を固定。 |
| U8-2 | B | `D20`（補助`D01/D21`） | `G2 / G5` | 再較正頻度と安全余裕のトレードオフを `性能維持率/回復時間/停止介入率` で監査し、運用可能帯を先に明文化。 |
| U12-3 | C | `D02`（補助`D10/D12`） | `G2 / G6` | 心理的連続性proxyの監査ログ（`branch_id/continuity_score/evidence_hash`）を最低要件化し、人格判断は外部制度依存として分離。 |
| U15-4 | C | `D07`（補助`D20/D21`） | `G2 / G6` | 停止条件・更新条件・例外承認を監査イベント単位で規約化し、EEGは閾値補助証跡に限定する境界を固定。 |

- 提出時の正本参照は継続して `Dxx + DOI + データセット名 + access区分` を使用し、数値IDは探索補助として扱います。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認しました。

## 今回の再検証ログ（2026-03-28 16:02 JST）

本runでは、既存の `RQ60` マップを汎用要約へ戻さず、各課題を1件ずつ深掘りする方針を維持したまま再検証しました。

更新したこと（RQ単位の深掘り固定キュー）:

- `U0-4`: 分岐/複製ケースの同一個体判定を、生体同定精度と責任帰属の分離条件で固定。
- `U1-1`: 逆問題の事前分布比較を、既知刺激位置に対する逆解誤差と被覆率の同時監査へ固定。
- `U3-3`: 身体・環境ループ除去時の性能低下を、EEG単独境界の明示を含む比較課題として固定。
- `U8-4`: 異常検知遅延とフェイルセーフ発動時間を、運用停止判断に直結するKPIとして固定。
- `U14-1`: データ/コード/環境固定の最小追試パックを、否定例付き運用で提出可能な形へ固定。
- `U15-4`: 停止条件/更新条件のガバナンスを、技術ログ連携可能な制度監査項目へ固定。

整合チェック（機械再計数）:

- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` の `### Ux-y` を再計数し、`RQ_TOTAL=60`（欠損・重複 `0`）を確認。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` の判定行を再計数し、`A/B/C=17/25/18` を確認。
- 参照旧ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）は `EEG-DATA/eeg_dataset_summary_ja.csv` の `旧ID` 列で欠損 `0/17`。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を維持。

継続方針:

- 汎用横断の浅い要約は増やさず、`1RQ=1検証命題=1応募テーマ=1主データ` を固定運用する。

## 今回の深掘り実行パック（2026-03-28 17:04 JST, 2週間で初回結果まで）

汎用横断の更新ではなく、前runと重複しにくい `6RQ` を固定し、`1RQ=1検証命題=1応募テーマ=1主データ` で深掘りします。

| RQ | 選定理由（1件ずつ深掘りする理由） | 最初の実験KPI | 失敗条件（このrunでの停止条件） | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|---|
| U0-2 | ms同期と状態表現の対応を固定しないと、同一性判定が計測誤差に引きずられるため。 | `clock offset p95` `状態特徴崩れ率` `再同期後の一致率` | offsetが収束せず、再同期後も一致率が基準未達。 | 時刻同期監査レポート（オフセット/ジッタ分布） | `G2 / G3` |
| U1-3 | 逆解法間の乖離を先に抑えないと、後続RQの因果比較が不安定化するため。 | `手法順位一致率` `逆解誤差` `被覆率` | 手法順位の反転が継続し、被覆率が逸脱。 | 逆問題再現レポート（エラー/不確実性） | `G1 / G4` |
| U4-3 | 反事実誤差と尤度差を同時に見ないと、理論比較が事後解釈へ流れやすいため。 | `PEHE` `予測尤度差` `符号一致率` | PEHEが上限超過し、符号一致率が不安定。 | 介入プロトコルと反論条件の定義 | `G1 / G4` |
| U8-1 | 閉ループ遅延の安全域を先に定義しないと、運用KPIが固定できないため。 | `安定率` `回復時間` `停止介入率` | 安定率が許容域未満で回復時間が長期化。 | クローズドループ安全性 KPI ダッシュボード | `G2 / G5` |
| U13-4 | 模倣スコア偏重を抑えるため、因果整合との二重閾値を先に固定する必要があるため。 | `意味一致率` `因果一致率` `乖離ケース率` | 意味一致高/因果一致低の乖離を分離できない。 | 模倣品分離評価報告書（意味・仕組み） | `G1 / G4` |
| U14-5 | 否定例レジストリを更新しないと、再現失敗の再試行運用が属人化しやすいため。 | `failure再現率` `rerun完了率` `否定例公開率` | rerun未完了が滞留し、失敗分類が再現不能。 | ネガティブサンプルレジストリ初版（CSV+運用ルール） | `G1 / G3` |

実行順（本実行固定）:

1. `U0-2`
2. `U1-3`
3. `U4-3`
4. `U8-1`
5. `U13-4`
6. `U14-5`

## 今回の再検証ログ（2026-03-28 17:04 JST）

本実行では、`mind-upload`/`EEG-DATA`/`auto-research-funds`の最新の`main`を反映し、後にRQ単位の深掘り監査を再実行しました。

整合チェック（再実施）:

- `RQ見出し=60件`（`### Ux-y`）を維持します。
- 判定内訳 `A/B/C=17/25/18` は不変。
- EEG参照運用ID集合（`6,11,13,16,19,49,56,65,509,676,696,719,735,783,842,859,2412`）は最新 `EEG-DATA/eeg_dataset_summary_ja.csv` の `旧ID` 列で欠損 `0`。
- 応募キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の参照統合を再確認。
- 方針は継続して `1RQ=1検証命題=1応募テーマ=1主データ` を維持。

## 2026-03-29 06:25 JST 再検証ログ (メイン実行 / 6 RQ ファンディングおよびデータセット アンカー パス)

- このパスでは概要は拡張されません。これは、EEG 対応および助成金対応の作業パッケージに変換される場合に、パブリック マインド アップロード プログラムを最も直接的に変更する 6 つの RQ を修正します。
- 正規の証拠ルールは変更されません。提出には `Dxx + DOI + dataset name + access class` を使用し、検索専用のガイダンスとして数値のレガシー ID を保持します。

| RQ | 判定 | プライマリー D アンカー | グラントレーン | 今回の実行で修正された点 | ストップコンディション |
|---|---|---|---|---|---|
| `U13-1` | `B` | `D10` + `D03/D09` をサポート | `G1 / G4` | 意味論的復元を因果的再現から分離し、模倣のみのパス判定を禁止しました。 | リークのない分割で意味的/因果的ギャップが表示されない場合は、クレームをダウングレードします。 |
| `U7-3` | `A` | `D11` + `D12/D24` をサポート | `G1 / G3` | 前処理ドリフト監査を補足ではなく、第一級の再現性成果物として修正しました。 | 繰り返しの実行でランキングの安定性を損なう構成をすべて削除します。 |
| `U0-4` | `B` | `D02` + `D10/D12` をサポート | `G2 / G3` | 分岐アイデンティティを 2 軸の技術基準 (観察一致と介入一致) にロックしました。 | いずれかの軸に障害が発生した場合、または 1 つの軸のみが生き残った場合、結果は部分的なままになります。 |
| `U8-4` | `B` | `D20` + `D01/D21` をサポート | `G2 / G5` | 最小閉ループ安全ペアとして異常検出レイテンシとフェールセーフ起動を修正しました。 | レイテンシまたはリカバリしきい値に達しない場合は、研究専用の安全手順内で作業を続けてください。 |
| `U1-2` | `A` | `D08` + `D11/D19` をサポート | `G1 / G4` | 点推定精度のみではなく、摂動テストされた区間カバレッジへの不確かさの伝播をロックしました。 | 度重なる変動によりカバレッジの安定性が損なわれる場合は、申し立てを格下げします。 |
| `U4-3` | `B` | `D05` + `D08/D19` をサポート | `G1 / G4` | 分析前の`PEHE + log-likelihood`との反事実理論の比較を修正しました。 | 繰り返しの介入設定によって理論のランキングが反転した場合は、その主張を格下げします。 |
