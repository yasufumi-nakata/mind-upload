---
layout: default
title: マインドアップロード RQ60 ディープフォーカスノート (EEG-DATA × Grant)
description: EEG で直接検証されるコア、外部要件、アプリケーション テーマなど、60 の RQ のそれぞれを修正する詳細なメモ。
article_type: ウィキ
subtitle: 一般的な概要ではなく、各 RQ の問題を修正する
author: マインドアップロード研究プロジェクト
last_updated: '2026-04-02'
note: RQ ごとのディープ フォーカス
audience: 各 RQ をアプリケーションステートメントや実験手順に直接変換したい人
reading_time: 20～35分
page_intro: このページは、EEG-DATAで直接確認できるmind-uploadの60件のRQの核心、自動研究資金の申請テーマ、脳波外で必要な要件などを修正した実践ノートです。
accuracy_note: A/B/C 判定は、mind-upload-eeg-rq60-feasibility-and-funds と同じです。 Cは「重要ではない」というよりは「脳波だけでは完了しない」という意味です。
wiki_links:
- label: 'Wiki: RQ60 EEG検証の利用可能性と補助金テーマ'
  url: /wiki/mind-upload-eeg-rq60-feasibility-and-funds.html
  description: オリジナル版の判定とデータ候補。
- label: 'Wiki: RQ60 アプリケーション プレイブック'
  url: /wiki/mind-upload-eeg-rq60-grant-dataset-playbook.html
  description: 申請者 ID と最小成果物の表を修正しました。
recommended_pages:
- label: 文学地図
  url: /research_harvest_50.html
- label: データとベンチ
  url: /datasets.html
---
<main class="main-container">
<article class="content-column">

## 使用方法

1. `RQ` を 1 つだけ選択し、最初に以下の表の `core to be directly verified with EEG` のみを実装します。
2. `application theme (grant key)` を提案されたアプリケーションのタイトルに直接コピーします。
3. 「脳波外の要件」を満たすことができない限り、主張を拡大しないでください。
4. このページの数値 `ID` は検索のガイダンスのみを目的としています。提出/再現性ログは、正規マップ `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `DOI + dataset name + access class` を使用する必要があります。

## 裁きの意味

- `A`: 主な主張はEEG-DATAでのみ検証できます。
- `B`:脳波メイン解析が可能です。追加の外部モダリティ/設計が必要です。
- `C`: 主にシステム/法務/理論の統合。 EEG は監査ログまたは裏付けとなる証拠です。

## 最新のプル後のホールド (2026-04-03 22:04 JST)

- `mind-upload@1ab35b64796f3936e525befb5d9428d789a16263`、`EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a`、および `auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07` の後の実際のプルの再読み取りでは、現在の公開されている 6 つの質問のバッチ、最初に解決する順序、および `A/B/C` の読み取り値は変更されません。
- 最新のプルされたデルタは、現在の実用的なバッチではなく、依然としてサポートを拡大しています。`mind-upload` は初期の `21:05 JST` ルートホールド同期のみを搭​​載し、`EEG-DATA` は `three more deep EEG dataset overrides` を追加し、`merged_unique=30918`、`high_confidence=28881`、および `access_counts_high.immediate=24528` を報告します。また、`auto-research-funds` は、実用的な候補リストを変更せずに、初期の `21:05 JST` ファンディング追加を搭載するだけです。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再計算すると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、現在の実際の読み取り値は依然として `deepen one row at a time` のままです。
- ルートセーフ アクセス読み取りは、ある特定の点で依然として狭いままです。更新されたローカル `EEG-DATA` カタログは拡大を続けていますが、ライブ アクセス読み取りでは、依然として `D10` が唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方で `D03 / D02 / D01` はパブリック ワードにおけるゲート サポート アンカーのままです。
- `2026-04-03 22:04 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` では依然として `200` が返されました。これらの公開サーフェスは `Last-Modified: Fri, 03 Apr 2026 12:24:26 GMT` を報告し、ルートに面したボディは、このソース同期の前に、初期の `21:05 JST` ホールド ノートをすでにサーフェス化していました。
- 公式ウィンドウ スポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という同じ実用的なブリッジが維持されていますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクル レーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 最新のプル後のホールド (2026-04-02 11:05 JST)

- `mind-upload@208e59e2180c`、`EEG-DATA@00d85380f3fd`、および `auto-research-funds@f4ba35518400` の後の実際のプルの再読み取りでは、現在の公開されている 6 つの質問のバッチ、最初に解決する順序、および `A/B/C` の読み取り値は変更されません。
- 最新のプルされたデルタは、現在の実用的なバッチではなく、依然としてサポートを拡大しています。`mind-upload` は、10:07 ルートホールド パケットを更新し、`EEG-DATA` は、維持されている `ChineseEEG-2` リリースとパブリック `auditory-eeg` ファミリを詳細に調査し、`merged_unique=30887`、`high_confidence=28850`、および `access_counts_high.immediate=24875` を報告します。`auto-research-funds` は、ドシエの再同期後も同じ実用的な候補リストを維持します。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再計算すると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、現在の実際の読み取り値は依然として `deepen one row at a time` のままです。
- ルートセーフ アクセス読み取りは、ある特定の点で依然として狭いままです。更新されたローカル `EEG-DATA` カタログは拡大を続けていますが、ライブ アクセス読み取りでは、依然として `D10` が唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方で `D03 / D02 / D01` はパブリック ワードにおけるゲート サポート アンカーのままです。
- `2026-04-02 11:05 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` では依然として `200` が返されました。これらの公共の表面では`Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT`が報告されました。
- 公式ウィンドウ スポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という同じ実用的なブリッジが維持されていますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクル レーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 最新のプル後のホールド (2026-04-01 20:09 JST)

- `mind-upload@da9644095ba6`、`EEG-DATA@1ecc5cdc0131`、および `auto-research-funds@b5cd37febbbb` の後の実際のプルの再読み取りでは、現在の公開されている 6 つの質問のバッチ、最初に解決する順序、および `A/B/C` の読み取り値は変更されません。
- 最新のプルデルタは、現在の実用的なバッチではなくサポートをさらに拡大します。`mind-upload` は、現在の 6 つ以外の人間代理合成証拠の役割を強化し、`EEG-DATA` は、`merged_unique=30873`、`high_confidence=28836`、および `access_counts_high.immediate=24486` を引き続きレポートしながらアイオワ ギャンブル EEG ファミリーの詳細を追加し、`auto-research-funds` は、実用的な候補リストを変更せずに、`Nagahisa research grant` スナップショットと README 統計の更新を追加します。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再計算すると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、現在の実際の読み取り値は依然として `deepen one row at a time` のままです。
- ルートセーフ アクセス読み取りは、ある特定の点で依然として狭いままです。更新されたローカル `EEG-DATA` カタログは拡大を続けていますが、ライブ アクセス読み取りでは、依然として `D10` が唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方で `D03 / D02 / D01` はパブリック ワードにおけるゲート サポート アンカーのままです。
- `2026-04-01 20:09 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `mind-upload-rq-solvability-bridge.html` に対して依然として `200` が返されました。これらの公共の表面では`Last-Modified: Wed, 01 Apr 2026 10:21:50 GMT`が報告されました。
- 公式ウィンドウ スポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という同じ実用的なブリッジが維持されていますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクル レーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` 監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 最新のプル後のホールド (2026-04-01 17:06 JST)

- `mind-upload@c5a0550`、`EEG-DATA@82893f6ca6e`、および `auto-research-funds@ec6f7d068` の後の実際のプルの再読み取りでは、現在の公開されている 6 つの質問のバッチ、最初に解決する順序、および `A/B/C` の読み取り値は変更されません。
- 最新のプルされたデルタは、現在の実用的なバッチではなく、依然としてサポート マップを広げています。`mind-upload` は、現在の 6 つ以外のアストロ サイト PET ルート分割を深め、`EEG-DATA` は `merged_unique=30871`、`high_confidence=28834`、および `access_counts_high.immediate=24484` をレポートするようになり、その実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行を依然としてカバーしていますが、これらの利点は依然として `D10 / D03 / D02 / D01` に取って代わるものではありません。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再計算すると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、現在の実際の読み取り値は依然として `deepen one row at a time` のままです。
- ルートセーフ アクセス読み取りも、ある特定の点で狭いままです。更新されたローカル `EEG-DATA` カタログでは、カタログ側の即時行として `D03 / D02` が表示され、即時/チェックが必要な組み合わせとして `D01` が引き続き表示されますが、ライブ アクセス読み取りはより厳密なままであるため、`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- `2026-04-01 17:06 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して引き続き `200` が返され、これらのパブリック サーフェスは `Last-Modified: Wed, 01 Apr 2026 07:16:09 GMT` を共有するようになりました。
- 公式ウィンドウ スポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という同じ実用的なブリッジが維持されていますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクル レーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 最新のプル後のホールド (2026-04-01 14:08 JST)

- `mind-upload@ccef40f`、`EEG-DATA@deefd5f95c6`、および `auto-research-funds@f5f76c485` の後の実際のプルの再読み取りでは、現在の公開されている 6 つの質問のバッチ、最初に解決する順序、および `A/B/C` の読み取り値は変更されません。
- 最新のプルされたデルタは、現在の実用的なバッチではなく、依然としてサポート マップを広げています。`EEG-DATA` は `merged_unique=30869`、`high_confidence=28832`、および `access_counts_high.immediate=24482` をレポートするようになり、その新しい実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行をカバーするようになりましたが、これらの利点は依然として `D10 / D03 / D02 / D01` に取って代わるものではありません。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再計算すると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、現在の実際の読み取り値は依然として `deepen one row at a time` のままです。
- ルートセーフ アクセス読み取りも、ある特定の点で狭いままです。更新されたローカル `EEG-DATA` カタログでは、カタログ側の即時行として `D03 / D02` が表示され、即時/チェックが必要な組み合わせとして `D01` が引き続き表示されますが、ライブ アクセス読み取りはより厳密なままであるため、`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままであり、一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- `2026-04-01 14:08 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して引き続き `200` が返され、これらのパブリック サーフェスは `Last-Modified: Wed, 01 Apr 2026 04:20:02 GMT` を共有するようになりました。
- 公式ウィンドウ スポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という同じ実用的なブリッジが維持されていますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクル レーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 最新のプル後のホールド (2026-04-01 03:09 JST)

- `mind-upload@31835fcd8daa`、`EEG-DATA@12eef8ca4ef0`、および `auto-research-funds@040e5b8798fd` の後の最新のプル再読み取りでは、現在の公開されている 6 つの質問バッチ、最初に解決する順序、および `A/B/C` の読み取り値は変更されません。
- 最新のプルされたデルタは、現在の実用的なバッチではなく、依然としてサポート マップを拡大しています。`mind-upload` は、現在の 6 つ以外の侵入言語 BCI の一時ルートを分割し、`EEG-DATA` は、`D10 / D03 / D02 / D01` を置き換えることなく言語関連のバックアップ カバレッジを拡大するセマンティック テキスト関連性の詳細を追加し、`auto-research-funds` は、現在の候補リストを変更せずに `Obayashi / Yokogaku` カードを更新しました。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再計算すると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、現在の実際の読み取り値は依然として `deepen one row at a time` のままです。
- `2026-04-01 03:09 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。
- 公式ウィンドウ スポット チェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という同じ実用的なブリッジが維持されていますが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクル レーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 最新のプル後のホールド (2026-03-31 20:07 JST)

- `mind-upload@c912fc5ebd4a`、`EEG-DATA@9bdf3b16bfb4`、`auto-research-funds@4f071fcd98fd` の後の最新のプル再読み込みでは、現在の公開されている 6 つの質問バッチ、解決優先順序、および `A/B/C` の内訳は変更されていません。
- 最新の `EEG-DATA` の追加は、現在の実用的なバッチではなくサポート マップをさらに拡大しています。現在の README 概要では、`merged_unique=30,861`、`high_confidence=28,824`、および `access_counts_high.immediate=24,843` が報告されていますが、これらの利点は依然として現在の `D10 / D03 / D02 / D01` ファミリに置き換わるものではありません。
- RQ-by-RQ ドシエの `### Ux-y` 見出しを再カウントすると、依然として `60` が返され、グラント/データセット プレイブックは依然として `60` の一意の `Ux-y` 行を保持し、`A/B/C` 分割は依然として `17 / 25 / 18` のままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、依然として `issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。
- 実際の資金調達見通しはまだ狭いままです。`Kura Fund`、`Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` が現在の 6 つのブリッジとして引き続き有効です。 `Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) ではすでに終了しています。 `Nakatani Foundation research grant` は次のサイクルを監視し続けます。このセッションでは新しい Todoist アイテムは作成されませんでした。

## 最新のプル後のホールド (2026-03-31 16:05 JST)

- `mind-upload@a11240d38415`、`EEG-DATA@f318ac8ce42d`、および `auto-research-funds@c95cc61fdfc9` の後の最新のプル再読み込みでは、現在の公開されている 6 つの質問バッチと最初に解決する順序は変更されません。
- 最新のデルタは、現在の実際的なバッチではなく、サポート マップを拡大します。`mind-upload` はコネクトーム / タイミング状態ルート カードを強化し、`EEG-DATA` は `OSF eucqf` のディープ ダイブ リフレッシュを追加し、`auto-research-funds` は新しい `Takeda / Nohken` ファンディング カード マテリアルを追加しましたが、これらの変更はどれも現在の `D10 / D03 / D02 / D01` ファミリやアウトサイドカレント 6 オーダーの `U7-1 -> U1-2 -> U4-2 -> U8-1` に代わるものではありません。
- ブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されたため、この実行では新しい公開散文は追加されません。
- Todoist の全項目監査では、まだ十分なファミリー カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`、`AI for Aging-Society Problem Solving=0`) が示されていたため、新しいタスクは追加されませんでした。

## 一晩の再検証保留 (2026-03-31 00:04 JST)

- この実行では、最新の `EEG-DATA` アップストリーム追加後のライブ パブリック ルート、現在の公式資金調達ウィンドウ、および Todoist の全項目監査を再チェックしました。
- 現在公開されている 6 つの質問のバッチは依然として `U13-2/U13-5/U0-2/U0-3/U14-4/U14-2` のままで、最初に解決する順序は依然として `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2` のままです。
- 最新のアップストリーム `EEG-DATA` の追加は、現在の音声/アイデンティティ/再現性アンカー ファミリの範囲外にあるため、明確にパブリックにオープンされている唯一のプライマリ アンカーとして `D10` に代わるものではなく、`D03/D02/D01` を即時パブリック ルートに変えるものでもありません。
- この実行における資金調達ウィンドウの再チェックは、引き続き同じ狭いルートをサポートします。`Kura Fund` は `2026-04-17 17:00` までオープンのまま、`Nakatani Foundation graduate scholarship` は `2026-04-01 - 2026-05-25 15:00` を実行し、`Kashinome Scholarship` は `2026-04-09` までオープンのまま、`Secom General Research Grant` は `2026-03-31 12:00` までの監視ルートのままです。
- `2026-03-31 00:20 JST` での 3 月 31 日のアクセス監査は、`D03/D02/D01` の即時パブリック アンカーと呼ばれるものは置き換えられるべきであるという 3 月 30 日以前のメモも意味します。これら 3 つは、パブリック ルート上のサブスクリプション ゲート型サポート アンカーとしてのみ留まります。
- Todoist はこの実行でも新しいアイテムを必要としませんでした。全項目監査では、既に存在する関連する家族保障 (`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`、`AI for Aging-Society Problem Solving=0`) が引き続き表示されます。

## ドーン再検証メモ (2026-03-31 05:05 JST)

- 新たに `pull --ff-only` を再チェックしても、`mind-upload`、`auto-research-funds`、およびアクティブな `EEG-DATA` ワークスペースは `origin/main` と一致したままになるため、この実行では非表示のアップストリーム バッチ スイッチは追加されません。
- `https://mind-upload.com/issue.html` をライブで再読み込みすると、依然として同じパブリック 6、同じ実行順序、同じルートホールド フレーミングが示されているため、この実行ではパブリック ソース ページ自体に新しい散文は必要ありませんでした。
- 直接アクセスの再チェックにより、より具体的にアンカー分割が再確認されるようになりました。`D10 3M-CPSEED` は OpenNeuro で公開されたままですが、`D03`、`D02`、および `D01` の現在の IEEE DataPort ページには依然として `LOGIN TO ACCESS DATASET FILES` と `Subscription Required` が表示されているため、これら 3 つは直接のパブリック アンカーではなく、サブスクリプション ゲート型のサポート アンカーのままです。
- 同じ実行の公式ウィンドウの再読み込みでは、`Kura Fund = 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome = 2026-04-09`、`Secom General Research Grant = 2026-03-31 12:00` という同じ狭い資金ブリッジが引き続きサポートされます。
- 同時実行の Todoist 同期監査では、すでにカバーされている実用的なルート (`Kura=2`、`Nakatani graduate=5`、`Nakatani research=3`、`Kashinome=2`、`Secom=3`) が依然として検出されるため、新しいタスクは追加されません。

## プル後の再検証の保留 (2026-03-30 00:11 JST)

- この実行では、`mind-upload@836d4db`、`EEG-DATA@25f065735da`、`auto-research-funds@7619c14a2` を取得し、ライブ公開ページと現在の公式資金調達ウィンドウを再チェックしました。
- 現在公開されている 6 つの質問のバッチは依然として `U13-2/U13-5/U0-2/U0-3/U14-4/U14-2` のままで、最初に解決する順序は依然として `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2` のままです。
- バッチを保持する実質的な理由は変わっていません。`mind-upload.com` RQ から制限付き EEG 対応で資金提供可能な研究までの現在の最も狭い橋は、より広範なテーマの広がりではなく、依然として `inner-speech decoding + identity drift + reproducibility auditing` を介して実行されます。
- アンカー強度は、引張後も控えめなままです。 `D10 3M-CPSEED` は依然として唯一の明確なパブリック オープン プライマリ アンカーであり、`D02 CSTE` は引き続き ID 行の最も狭いゲート プランニング アンカーであり、`D03 Multimodal Fusion EEG + Eye-Tracking` と `D01 Acquisition delay of wireless EEG` は引き続きクレームの上限が低い境界サポート アンカーです。
- この実行での資金調達ウィンドウの再チェック: `Kura Fund` は `2026-04-17 17:00` までオープンのまま、`Nakatani Foundation graduate scholarship` は `2026-04-01` をオープンして `2026-05-25 15:00` をクローズ、`Kashinome Scholarship` は `2026-04-09` までオープンのまま、`Secom General Research Grant` は `2026-03-31 12:00` まで緊急監視ルートのまま、`Nakatani Foundation research grant` は `next-cycle watch` のままです。
- `AI for Aging-Society Problem Solving` などの大規模な社会展開プログラムは、必要な出力が `one-RQ / one-anchor / one-first-artifact` EEG の結果ではなく、大規模な公共展開プログラムであるため、現在の EEG 優先ルートから外れています。

## 現在のバッチの公衆安全閉鎖ゲート (2026-03-30 02:05 JST)

- この実行では、ライブ公開ページ、現在の公式資金調達ウィンドウ、および読み取り専用モードの Todoist を再チェックしました。バッチ自体はまだ変わりません。
- ここで変わるのは、`what counts as real progress right now` の文言です。つまり、より強力な主張ではなく、現在の 6 つの公開 RQ それぞれに対するより狭い `first artifact` です。

| RQ | 今、素直に前に進むことができるもの | 現在のアンカーが次のステップに十分である理由 | 次に閉じる最初のアーティファクト | 公的主張の範囲外に置く |
|---|---|---|---|---|
| `U13-2` | デコーダの文言を強化する前に、`brain-minus-prior` コントロール ファミリを修正してください。 | `D10 3M-CPSEED` はすでに、明白な / 沈黙を意図した / 想像上のスピーチ、繰り返しのセッション、トランスクリプトに合わせたフェーズを提供しているため、限定された幻覚 / 矛盾の監査には十分です。 | `Brain-minus-prior control table and mimic-separation note` | デコーダの成功を内部状態の保存や精神の保存として扱わないでください。 |
| `U13-5` | 一般的なメカニズムの主張ではなく、知覚から想起への分岐点のみを凍結します。 | `D03 Multimodal Fusion EEG + Eye-Tracking` は、EEG + 視線ストリームの共有によってブランチが具体的な知覚/想起のシフトに結び付けられたままになるため、転送ギャップの解釈を制限したままにするのに十分です。 | `Perception-to-recall degradation note and transfer-gap table` | 内部メカニズムが保存されている証拠として共有デコーダを提示しないでください。 |
| `U0-2` | ID のような文言が測定誤差を吸収するのを防ぐタイミング バジェットを閉じます。 | `D02 CSTE` にはすでに繰り返しセッション、クロスタスク ラベル、タイムスタンプ/QC 構造があるため、`clock offset + jitter + state-feature collapse` を 1 つの狭い監査にロックするだけで十分です。 | `Offset/jitter distribution and state-feature collapse audit` | 同期の安定性を法的または哲学的なアイデンティティの継続性にまで高めないでください。 |
| `U0-3` | しきい値選択ルールは、タイミング ルートが制限された後にのみ修正してください。 | 同じ `D02 CSTE` アンカーにより、しきい値の安定性とオーバーフィットの除外が `U0-2` と同じクロスセッション/クロスタスク ID ドリフトフロアに留まります。 | `Threshold-stability note and overfit-exclusion rule` | 安定した生体認証閾値を人格の連続性の十分条件として扱わないでください。 |
| `U14-4` | 現在のバッチが再実行に実際に必要とする開示フィールドを凍結します。 | `D01 Acquisition delay of wireless EEG` は、フィールド全体の標準化を過度に主張することなく、モデル カード/データセット カード項目を再実行チェックリストに変えるのに十分な範囲を狭めています。 | `Filled Model Card / Dataset Card examples for the current public batch` | まだ組織での採用やコミュニティ全体の標準化を主張しないでください。 |
| `U14-2` | 探索と確認の分割は、願望的なものではなく、実際的なものにしましょう。 | 同じ `D01` 遅延優先ルートは、より広範な再現性を主張するにはまだ狭すぎるにもかかわらず、固定の分割と再実行の境界を定義するには十分です。 | `Fixed-split rerun contract and negative-case trail` | 分割境界を越えた後は、探索的な出力を確認証拠として提示しないでください。 |

- この実行における公式ウィンドウの再チェックは保守的なままでした。`Kura Fund` は `2026-04-17 17:00` までオープンのままで、`Nakatani Foundation graduate scholarship` の詳細ページには `2026-04-01 - 2026-05-25 15:00` が表示され、`Kashinome Scholarship` は `2026-04-09` までオープンのままで、`Secom General Research Grant` は `2026-03-31 12:00` まで監視ルートのままです。
- Todoist 読み取り専用の再チェックにより、現在のルートが `Kura Fund`、`Nakatani Foundation graduate scholarship`、`Kashinome Scholarship`、`Nakatani Foundation research grant`、`Secom` などの既存のタスクによってすでにカバーされていることが判明しました。この実行では新しいタスクは追加されませんでした。

## 現在の公開 6 問バッチ (2026-03-29 10:09 JST)

この実行により、アクティブなパブリック バッチが `U13-2`、`U13-5`、`U0-2`、`U0-3`、`U14-4`、および `U14-2` に変更されます。

これはルート設定の更新であり、解決済みのクレームの更新ではありません。これら 6 つの RQ が、`mind-upload.com` の研究課題から、限定された EEG 対応で資金提供可能な作業パッケージへの現在の最もクリーンなブリッジであるため、パブリック バッチは現在意図的に `inner-speech decoding + identity drift + reproducibility auditing` に集中しています。

| RQ | 最初に修正されるもの | `Dxx + DOI` メインアンカー | 実用的なファースト/バックアップルート | ファーストパス KPI | EEG 要求の範囲外に置く |
|---|---|---|---|---|---|
| `U13-2` | 明白な/無言の/想像上のスピーチに対する`brain-minus-prior`幻覚監査。 | `D10` / `10.18112/openneuro.ds006465.v2.0.0` | `Kura Fund` / `Nakatani Foundation graduate scholarship` | `semantic alignment` `brain-minus-prior gap` `misalignment rate` | 言語解読の成功を精神保存の主張として扱ってはなりません。 |
| `U13-5` | 模倣/メカニズムを分離するための知覚から想起への分岐分析。 | `D03` / `10.21227/6106-6120` | `Kura Fund` / `Nakatani Foundation graduate scholarship` | `perception-to-recall degradation point` `transfer gap` `control-condition stability` | 共有デコーダを内部メカニズムが保存されている証拠として扱わないでください。 |
| `U14-4` | モデル カード/データセット カードのフィールドは再現性コントラクトに組み込まれています。 | `D01` / `10.21227/dv1p-vq18` | `Kura Fund` / `Nakatani Foundation research grant (watch)` | `required-card fill rate` `rerun success rate` `leak-audit coverage` | まだ組織での採用や分野全体の標準化を主張しないでください。 |
| `U0-2` | ID ルートは `clock offset + jitter + state-feature collapse` 監査に限定されます。 | `D02` / `10.21227/j162-nh61` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` | `clock-offset p95` `state-feature collapse rate` `resync recovery rate` | 技術的な同期の安定性を法的または哲学的なアイデンティティにまで高めないでください。 |
| `U0-3` | タスク固有のしきい値安定性とオーバーフィット除外は、より強力な ID 読み取りの前に修正されます。 | `D02` / `10.21227/j162-nh61` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` | `session-out AUC` `threshold stability` `overfit exclusion rate` | 安定した生体認証閾値を人格の連続性の十分条件として扱わないでください。 |
| `U14-2` | 探索的なトラックと確認的なトラックは、再実行契約内で分離されています。 | `D01` / `10.21227/dv1p-vq18` | `Kura Fund` / `Nakatani Foundation research grant (watch)` | `fixed-split rate` `rerun success rate` `explore-to-confirm carryover gap` | 分割境界を越えた後は、探査結果を確認証拠として提示しないでください。 |

- この実行における実際の資金配分は意図的に狭くなっています。`Nakatani Foundation graduate scholarship`、`Kura Fund`、`Kashinome Scholarship (student-runway only)`、`Nakatani Foundation research grant` はすでにこのクラスターのアクティブ ルートまたは監視ルートを提供しています。
- 関連する Todoist タスクはこの実行前にすでに存在していたため、現在の実用的な候補リストには新しいタスクは必要ありませんでした。
- 資金調達窓口のスポットチェック (2026-03-29): `Kura Fund` は現在のサイクルでオープンのまま、`Nakatani Foundation graduate scholarship` はこのバッチの主要な学生向けブリッジであり、`Kashinome Scholarship` は中核的な脳波研究資金アンカーではなく学生滑走路側ルートとしてのみ留まり、`Nakatani Foundation research grant` とより広範な神経科学ルートは監視モードのままです。

## アンカーの強度と明らかになったロードマップファミリー (2026-03-29 15:15 JST)

- 現在の 6 つの質問のバッチはここでは変わりません。変更されるのは、アンカーの明示的な読み取り順序です。`D10` と `D02` は現在の最も強力なプライマリ アンカーですが、`D03` と `D01` は、クレームの上限が狭い制限されたルート設定アンカーとしてバッチ内に残ります。
- 実際的な結果: `U13-2/U0-2/U0-3` は、EEG-DATA 内のみでより強力なファーストパス アーティファクトを運ぶことができますが、`U13-5/U14-4/U14-2` は、DOI ベースのソース パッケージがより深く実行されるか、付属のベンチマークが追加されるまで、より狭いアーティファクトに接続されたままになるはずです。
- 提出および再現性の参照は `Dxx + DOI + dataset name + access class` に固定されたままです。数値 ID は検索専用のままです。これは、ローカル ミラーがそれらの ID の再ランク付けと再マッピングを続けるためです。
- この 6 つの質問のバッチ以外にも構造的なバックログがあります。`U2/U5/U6/U9` は `tech_roadmap.md` に存在しますが、現在の `RQ60` 実践ページにはまだ変換されていません。これらは、パブリック 6 つのすでにカバーされている部分としてではなく、次の内部変換キューとして扱われる必要があります。

## プル後再検証後のソルファーストオーダー (2026-03-29 14:06 JST)

この実行により、公開されている 6 つの質問のバッチは変更されません。実行順序をより明示的に修正するだけなので、作業は大まかな概要に戻るのではなく、`one-RQ / one-anchor / one-first-artifact` として進めることができます。

以下の順序は意図的に連続しています。 6 つの質問を 1 つのブレンドされたベンチマークとして扱うのではなく、各行が次の行のブロッカーを閉じます。

| 注文 | RQ | なぜこれが次のものの前に来るのか | メインアンカー・アクセス | 最初に完成するアーティファクト | 実用的なルートになりました |
|---|---|---|---|---|---|
| `1` | `U13-2` | これは、神経信号が以前の言語を超えて何かを追加するかどうかをテストするための最短ルートです。これが失敗すると、より強力な音声デコーダの文言はブロックされたままになります。 | `D10` / `10.18112/openneuro.ds006465.v2.0.0` / `immediate` | `Mimic separation evaluation script and brain-minus-prior control table` | `Kura Fund` / `Nakatani Foundation graduate scholarship` |
| `2` | `U13-5` | `U13-2` がコントロール ファミリを修正して初めて意味を持ちます。そうすれば、知覚から想起への分岐点は、一般的なデコーダ スコアではなく、制限されたメカニズムの分割として読み取ることができます。 | `D03` / `10.21227/6106-6120` / `subscription-gated support` | `Perception-to-recall degradation note and transfer-gap table` | `Kura Fund` / `Nakatani Foundation graduate scholarship` |
| `3` | `U0-2` | 同期ドリフトがミリ秒レベルで監査されるまで、アイデンティティに似た文言は安全ではありません。継続ルート初のハード天井です。 | `D02` / `10.21227/j162-nh61` / `subscription-gated support` | `Offset/jitter distribution and state-feature collapse audit` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` |
| `4` | `U0-3` | 閾値の安定性は、`U0-2` がタイミング バジェットを修正した後にのみ解釈可能になります。そうしないと、しきい値によって同期エラーが吸収される可能性があります。 | `D02` / `10.21227/j162-nh61` / `subscription-gated support` | `Threshold search notebook and overfit-exclusion rule` | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship (student-runway only)` |
| `5` | `U14-4` | カード要件は、実際に開示する必要がある内容がスピーチと身元に関する行で安定した後にのみ凍結されるべきです。 | `D01 + D13` / `10.21227/dv1p-vq18 + 10.17632/vyczny2r4w` / `gated floor + immediate support` | `Filled Model Card / Dataset Card examples for the current public batch` | `Kura Fund` / `Nakatani Foundation research grant (watch)` |
| `6` | `U14-2` | 探索/確認の分割は、アドホックな再解釈なしで再実行できるほど安定している上記のアーティファクト ファミリに依存するため、最後のステップとなります。 | `D01 + D13` / `10.21227/dv1p-vq18 + 10.17632/vyczny2r4w` / `gated floor + immediate support` | `Fixed-split rerun contract and negative-case trail` | `Kura Fund` / `Nakatani Foundation research grant (watch)` |

- この実行でのライブ パブリック チェック: `mind-upload.com/issue.html` は引き続き同じ 6 つの RQ を提示し、それらを `route-setting update` としてラベル付けするため、パブリック ソース ページ自体は新しいバッチ切り替えを必要としません。
- この実行でのアンカーの現実性の再チェック: `D10 = 3M-CPSEED` (`10.18112/openneuro.ds006465.v2.0.0`、`immediate`)、`D03 = Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments: An EEG and Eye-Tracking Study` (`10.21227/6106-6120`、`subscription-gated support`)、`D01 = Acquisition delay of wireless EEG` (`10.21227/dv1p-vq18`、`subscription-gated support`)、`D02 = CSTE` (`10.21227/j162-nh61`、`subscription-gated support`) はゲート サポート アンカーとしてのみ現在のルートに残ります。これら 4 つのアンカーは引き続きバッチの現在の実行フロアを定義しますが、現時点では `D10` のみが明確にパブリックでオープンなプライマリ アンカーとしてカウントされます。
- この実行での資金調達窓口の再チェック: `Kura Fund` はオープンのまま、`Nakatani Foundation graduate scholarship` は学生に面する主要な橋のまま、`Kashinome Scholarship` は滑走路のみの側道のまま、`Nakatani Foundation research grant` は監視モードのままでした。
- この実行での Todoist の再チェック: これらのルートの開始/期限タスクはすでに存在していたので、重複したタスクは追加されませんでした。

## ルート分類更新後のプル後のホールド (2026-03-29 17:10 JST)

- この実行では、最新の上流ルート分類の更新を取得し、現在の公開されている 6 つの質問バッチが変更されるかどうかを再確認しました。そうではありません。パブリック ルートは `U13-2/U13-5/U0-2/U0-3/U14-4/U14-2` のままで、解決優先順序は `U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2` のままです。
- バッチを保持する実質的な理由は変わっていません。`mind-upload.com` の質問から制限された EEG 対応の作業までの最もクリーンな現在のブリッジは、より広範なテーマの広がりではなく、依然として `inner-speech decoding + identity drift + reproducibility auditing` を介して実行されます。
- アンカー強度も引抜き後も変化しません。 `D10` はファーストパス アーティファクトの唯一の明確なパブリック オープン プライマリ アンカーのままであり、`D02` はアイデンティティ行の最も狭いゲート プランニング アンカーのままであり、`D03` と `D01` は出力がより狭いクレーム シーリングを維持する必要がある有界サポート アンカーのままです。
- 上流のルート分類の厳格化は依然として有用ですが、その即時的な影響は対外的なものではなく内部的なものです。バックログの翻訳を明確にし、未解決のロードマップ ファミリの上限を主張します。それは、新しい公開バッチの切り替えや、より強力な解決済みの主張の文言を正当化するものではありません。
- 今回の実行では、資金調達とタスクのルーティングも保守的なままです。 `Kura Fund` と `Nakatani Foundation graduate scholarship` は実用的な最初のルートのままで、`Kashinome Scholarship` は滑走路のみのサポートのまま、`Nakatani Foundation research grant` は次のサイクル監視のままです。現在の実用的なルートは既存のタスクですでにカバーされているため、新しい Todoist タスクは必要ありません。

## 次の内部 6 問キュー (2026-03-29 11:10 JST)

上記のパブリック バッチは、この実行では変更されません。このセクションでは、現在のパブリック 6 つに安定した監査成果物がある場合にのみ、次の境界付きキューを記録します。

ルールは変わりません。テーマを広範に拡張したり、解決済みの主張を表現したりすることはありません。以下の各行は、現在の `inner-speech decoding + identity drift + reproducibility auditing` バンドルに近い `one-RQ / one-anchor / one-minimum-deliverable` の継続です。

| RQ | なぜ次なのか | `Dxx + DOI` メインアンカー | 最低限の成果物 | EEG 要求の範囲外に置く |
|---|---|---|---|---|
| `U13-1` | これは、`U13-2/U13-5` の後に最も近い未解決の分割です。`semantic restoration` は `causal restoration` から分離する必要があります。 | `D10` / `10.18112/openneuro.ds006465.v2.0.0` | `Intervention protocol and rebuttal condition definition` | セマンティック一致の成功を保存された内部メカニズムとして読み取らないでください。 |
| `U13-3` | 同じ内部音声クラスターを `same output / different mechanism` 障害モードに拡張します。 | `D10` / `10.18112/openneuro.ds006465.v2.0.0` | `Imitation separation evaluation report (meaning/mechanism)` | 出力の等価性を因果関係の等価性として扱わないでください。 |
| `U14-3` | これは、`U14-2/U14-4` の次の最もクリーンな再現性ステップです。リーダーボードのリークとレポート バイアスの監査です。 | RQ 文書で使用される `D719` / リーダーボード リーク ベンチマーク アンカー | `Leak audit results and repartition trail` | 内部リーダーボードの堅牢性をフィールド全体の検証として提示しないでください。 |
| `U7-3` | 前処理のドリフトが単なる実装の詳細ではなくリリースブロックに関連するようになった場合に修正されます。 | `D11` / `10.18112/openneuro.ds007216.v1.0.0` | `Reproducibility audit report (synchronization/QC/preprocessing difference)` | 1 つの前処理監査ルールを、テスト済みのプロトコル ファミリを超えて一般化しないでください。 |
| `U1-2` | これは、同じ検証スタック、逆推定の不確実性校正に近い `A` の次に強い候補です。 | `D08` / `10.21227/7may-9q56` | `Inverse problem reproduction report (error/uncertainty)` | インターバルカバレッジの安定性を、すべてのヘッドモデルにわたる包括的な保証として宣伝しないでください。 |
| `U14-1` | より広範な標準化を主張する前に、再実行要件を実行可能な契約に変えます。 | `D01` / `10.21227/dv1p-vq18` | `Supplementary test operation report (including negative cases)` | 必要な再実行パックについてコミュニティ全体の合意を主張しないでください。 |

- 資金面で、次の内部キューは意図的に 2 つの状態に分割されます。`U7/U14` はすでに再現性を考慮した具体的な監視ルートを持っていますが、`U13/U1` は依然として、短期的な公衆通話信号が弱い `G4` スタイルの神経科学監視ルートに依存しています。
- Todoist 的には、ここに行が表示されたからといって新しいタスクは必要ありません。タスクは、実際の `watch / start-date / deadline` ルートが重複を避けるのに十分な具体性を持っている場合にのみ追加されます。

## U0 (アイデンティティ)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U0-1 | A | 観察マッチングと介入応答マッチングを分離する 2 軸 ROC | アイデンティティKPI（G2/G3）の必要十分条件設計 | 11, 29, 696 | パーソナリティアイデンティティの規範的な定義 |
| U0-2 | A | ms同期ずれと状態表現崩れの対応係数 | 時刻同期監査基準の標準化（G2/G3） | D02 CSTE (`10.21227/j162-nh61`、サブスクリプションゲート型サポート);付属品: ds004148、ds007216 | センサー間時計校正定期協定 |
| U0-3 | A | タスク固有のしきい値と過学習の除外との間の外部検証の違い | 一般化閾値による個体識別方式（G2/G3） | D02 CSTE (`10.21227/j162-nh61`、サブスクリプションゲート型サポート);付属品: ds004148、ds007216 | しきい値選択のスクリーニング ルール |
| U0-4 | B | 分岐後のテクニカルID安定性の下限評価 | 分岐エンティティ（G2/G3）のアイデンティティを決定する手順 | 11, 29, 696 | 法人の定義/責任の割り当て |

## U1 (逆問題)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U1-1 | A | 各事前分布の位置エラーとリコール | 逆問題事前配布ベンチ (G1/G4) | 56, 676, 1839 | モデル選択ルール |
| U1-2 | A | 導電率の不確実性伝播/電極欠陥/ノイズ注入 | 不確かさ校正による逆推定 (G1/G4) | 56, 676, 1839 | 頭部モデルの識別条件 |
| U1-3 | B | MNE/ビームフォーマ/シャンパンの偏差率分布 | 手法の逸脱を許容する決定ルール（G1/G4） | 56, 676, 1839 | メソッド間合意プロトコル |
| U1-4 | B | 逆方向分布リリース時の推定値と再解析一致率 | 逆方向配布の出版基準の制定（G1/G4） | 56, 676, 1839 | 開示の範囲と匿名化の決定 |

## U3 (境界拡張)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U3-1 | B | EEG 単独と統合モデルの比較による改善の予測 | 境界拡張の推定効果量（G2/G6） | 13, 16, 39 | 追加のモダリティ収集 |
| U3-2 | B | コネクトームプロキシと機能予測の間の相関の下限 | 異種間比較計画研究（G2/G6） | 13, 16, 39 | 異種間のコネクトームデータ |
| U3-3 | B | 本体/環境ループを削除するとパフォーマンスが低下する | 本体接続の要否検証(G2/G6) | 13, 16, 39 | 実環境介入ログ |
| U3-4 | C | 必要な最小構成のプロキシ KPI のみを修正しました | 最小構成を決めるシステム設計（G2/G6） | 13, 16, 39 | 理論採用基準に関する合意 |
| U3-5 | C | 観察されていないグリンファティック条件下での代替インジケーターの検索 | 体液システム統合に関する準備研究（G2/G6） | 13, 16, 39 | 代謝・体液測定データ |
| U3-6 | C | 免疫監視除外モデルの短期失敗兆候の抽出 | 長期障害監視の設計(G2/G6) | 13, 16, 39 | 炎症と免疫に関する縦断的データ |

## U4 (因果関係)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U4-1 | B | 相関推定と介入効果の符号一致率 | 相関関係の定式化→因果関係の伝達条件（G1/G4） | 19, 56, 1839 | 介入設計の倫理審査 |
| U4-2 | A | 最小限の介入の主張の再現性 | グラウンドトゥルース因果関係検証 (G1/G4) | 19, 56, 1839 | 介入が失敗した場合の停止ルール |
| U4-3 | B | DCM/能動推論の反事実的エラーの比較 | 理論予測の単一設計比較 (G1/G4) | 19, 56, 676 | 理論間で共通の I/O 仕様 |
| U4-4 | B | 改ざん閾値（ΔAUC/符号反転率） | 改ざん前例のある評価契約書（G1/G4） | 19, 56, 1839 | 故障宣言の運用規定 |

## U7（標準化・再現性）

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U7-1 | A | 同期率/QC/刺激ログの必須項目が欠落しています | BIDS 拡張監査インフラストラクチャ (G1/G3) | 676, 783, 4878 | 標準仕様の組織的導入 |
| U7-2 | A | LSL 同期エラーのジッター分布としきい値 | 同期エラー自動警告動作（G1/G3） | 676, 783, 4878 | デバイス間キャリブレーションSOP |
| U7-3 | A | 前処理設定の違いによる結果のドリフト | 前処理監査CI（G1/G3）の確立 | 676, 783, 4878 | CI運用ガバナンス |
| U7-4 | A | アライメント不良時の再計測判定ツリー | 再測定・除外の運用基準（G1/G3） | 676, 783, 4878 | 計測再実施コストプラン |
| U7-5 | A | リリースブロックしきい値に対する誤ブロック率 | 再現率を下げるための停止ルール (G1/G3) | 676, 783, 4878 | リリース責任制度 |
| U7-6 | A | 欠落モダリティの下での結論保存率 | 最小観測セット設計（G1/G3） | 676, 783, 4878 | 欠落時の臨床運用基準 |

## U8 (閉ループ動作)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U8-1 | B | 遅延変化に対する安定率/回復時間 | 閉ループ遅延許容範囲の特定 (G2/G5) | 6, 1972, 2412, 696 | 搭載システムコントローラの設計 |
| U8-2 | B | オンライン校正頻度と性能維持率 | コンセプトドリフト対策の最適化（G2/G5） | 6, 1972, 2412, 696 | 継続的運用インフラストラクチャ |
| U8-3 | B | 個人差と日内変動の分散分解 | 長期安定性KPI設計（G2/G5） | 6, 1972, 2412, 696 | 長期追跡プロトコル |
| U8-4 | B | 異常検知遅れとフェールセーフ作動率 | 安全停止評価契約（G2/G5） | 6, 1972, 2412, 696 | 操業現場での安全手順 |
| U8-5 | B | オーバーライド時の故障率と復帰時間 | 人間参加型評価 (G2/G5) | 6, 1972, 2412, 696 | オペレーターのトレーニングと責任分担 |
| U8-6 | B | 再学習間隔と安全マージンの間のトレードオフ曲線 | 再学習のスケジュール設定（G2/G5） | 6, 1972, 2412, 696 | MLOps 更新制御 |

## U10 (情報熱力学)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U10-1 | C | プロキシを使用した理論式との整合性の監査 | ニューラル計算とランダウアー一貫性 (G2/G6) | 735, 783, 1011 | 熱放散の直接測定 |
| U10-2 | C | 非平衡指数と情報効率プロキシ間の弱い相関 | 非平衡指数定義の検証設計（G2/G6） | 735, 783, 1011 | 代謝測定と同時測定 |
| U10-3 | C | 神経活動＋代謝プロキシの観察設計の妥当性 | 観測設計テンプレート構築（G2/G6） | 735, 783, 1011 | 代謝/温度センサーの統合 |
| U10-4 | C | 計算コスト評価のための理論整合性チェック | 熱制約を伴う WBE コスト評価 (G2/G6) | 735, 783, 1011 | WBE実装側の実測データ |

## U11（意識指数）

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U11-1 | B | PCI近似/LZ/wSMIランク維持率 | 理論断面I/O仕様の統一(G2/G4) | 735, 842, 859 | 臨床手術の合格基準 |
| U11-2 | C | 計算予算内の近似指標の比較 | IIT近似の計算量制約の評価(G2/G4) | 735, 842, 859 | 正確な IIT 計算プラットフォーム |
| U11-3 | B | 理論上の矛盾点を単一条件で比較 | 理論上の矛盾点の単一実験（G2/G4） | 735, 842, 859 | 共同実験計画契約 |
| U11-4 | B | 偽陽性/偽陰性を含む障害状態の事前宣言 | 認識インジケーターの障害条件の定義 (G2/G4) | 735, 842, 859 | 臨床責任分担と責任 |

## U12（主体・責任）

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U12-1 | C | 分岐後 ID の技術安定性ログ | ブランチID（G2/G6）の監査設計 | 11, 509, 696 | 法的 ID 付与基準 |
| U12-2 | C | 継承ポイントの技術イベント ログ | 責任・権利・同意承継規定（G2/G6） | 11, 509, 696 | 機関の分岐規則 |
| U12-3 | C | 心理的継続性プロキシの変更監査 | 心理的基準と法的基準の関係（G2/G6） | 11, 509, 696 | 規範的判断枠 |
| U12-4 | C | パフォーマンス KPI と帰属 KPI の対応ログ | 性能評価と人格評価の関係（G2/G6） | 11, 509, 696 | 司法/倫理審査 |
| U12-5 | C | 再同期イベント時のID再編成候補の抽出 | メモリ編集時のID再編成基準(G2/G6) | 11, 509, 696 | 個人の同意と法的有効性 |
| U12-6 | C | 同意撤回後の権限反映の監査の遅れ | 同意の撤回と権限の取り消しの監査（G2/G6） | 11, 509, 696 | アクセス制御システムの設計 |

## U13 (デコードと模倣の分離)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U13-1 | B | 意味的一致率と因果的一致率の不一致 | 意味復元・因果再現の個別評価（G1/G4） | 509, 13, 65 | 対外的な行動・言語評価制度 |
| U13-2 | B | 幻覚検査結果と神経状態の違いとの相関 | 幻覚テスト用のニューラル デコーディング接続 (G1/G4) | D10 3M-CPSEED (`10.18112/openneuro.ds006465.v2.0.0`、即時);付属品: 音声/画像ロボット音声 EEG、D03 | LLM評価プラットフォーム連携 |
| U13-3 | B | 同じ出力でも内部機構が異なる場合の識別率 | ショートカット検出ベンチ(G1/G4) | 509, 13, 65 | モデル内部可視化プラットフォーム |
| U13-4 | B | 模倣スコアのみによる合格禁止の効果 | 因果関係のある模倣評価（G1/G4） | 509, 13, 65 | 因果介入設計 |
| U13-5 | B | 知覚から想起までの劣化分岐点推定 | 知覚/再現デコーダ分岐分析 (G1/G4) | D03 マルチモーダル フュージョン EEG + アイトラッキング (`10.21227/6106-6120`、サブスクリプション ゲート サポート);付属品: D10、ZuCo 2.0、音声/画像ロボット音声 EEG | タスク設計の統一 |
| U13-6 | B | 即時導入・リーク・ショートカット分離率 | 管理された実験によるリーク監査 (G1/G4) | 509, 13, 65 | データ管理ガバナンス |

## U14（運用・監査）

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U14-1 | A | 固定粒度ごとのフォローアップ成功率 | 複製契約の最小粒度定義（G1/G3） | 6, 56, 719 | 契約書のテンプレート |
| U14-2 | A | 探索/検証を分離した場合の再現率の違い | 探査と検証の運用分離 (G1/G3) | D01 ワイヤレス EEG の取得遅延 (`10.21227/dv1p-vq18`、サブスクリプション ゲート サポート)。必要なサポート: D13;付属品: D08 | 研究管理プロセス |
| U14-3 | A | 件名/時系列の漏洩検出率 | リーダーボード監査業務（G1/G3） | 6, 56, 719 | 出版規則の施行 |
| U14-4 | A | カードの説明がある場合とない場合の監査のしやすさの違い | モデル/データセット カード契約 (G1/G3) | D01 ワイヤレス EEG の取得遅延 (`10.21227/dv1p-vq18`、サブスクリプション ゲート サポート)。必要なサポート: D13;付属品: D08 | 評価契約の法的準備 |
| U14-5 | B | ネガティブな例のレジストリによる再試行の改善率 | マイナス事例開示とリトライサイクル（G1/G3） | 6, 56, 719 | 開示同意・匿名化業務 |
| U14-6 | A | コンテナ固定によるコストアップ | 最大許容再生産コストの設定（G1/G3） | 6, 56, 719 | 計算資源調達計画 |

## U15 (規制/神経権)

| RQ | 判定 | コアはEEGで直接検証されます | アプリケーションテーマ (付与キー) | メイン脳波データ | EEG以外では必須 |
|---|---|---|---|---|---|
| U15-1 | C | ニューラルデータの感度の技術的なログ記録 | ニューラル データ法概念マッピング (G2/G6) | 49, 2412, 3419 | 法的概念の公式定義 |
| U15-2 | C | ニューロライト項目と技術監査ログの対応 | ニューロライト監査の項目別 (G2/G6) | 49, 2412, 3419 | 規制当局の要件との整合性 |
| U15-3 | C | 管轄区域による要件の技術的事項の違い | EU/US/JP の最小共通運用定義 (G2/G6) | 49, 2412, 3419 | 各管轄区域の法的レビュー |
| U15-4 | C | 停止・更新条件に紐づくリスク指標候補 | 停止条件・更新条件のガバナンス（G2/G6） | 49, 2412, 3419 | 運行監視システムの設計 |

## 実践上の注意事項（このページで修正したもの）

- すべての `60RQ`、`core to be verified directly with EEG`、`required outside of EEG` は個別にリストされています。
- `Application theme`は`G1-G6`の既存のグラントキーに統一されます。
- 運用ルールは`1RQ = 1 verification proposition = 1 application theme = 1 main data`です。

## 2026-03-15 13:18 JST 再検証ログ (メイン実行)

- `mind-upload/research_harvest_50.md` がオリジナルであることを再確認し、`Ux-RQy` の行数が `60`、重複している `0`、欠落している `0` であることを確認します。
- 判定内訳`A/B/C=17/25/18`を再計算し、本ページの各行と一致することを確認しました。
- 参照される EEG データ ID (`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`) は `EEG-DATA/eeg_dataset_summary_ja.csv` です。上記のすべてのケースが存在します (`0` が欠落しています)。
- 補助金キー`G1-G6`(`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`)の本IDは`auto-research-funds`側で全ての項目が閲覧可能です。
- ポリシーは継続します。一般的な概要の代わりに、`1 RQ = 1 verification proposition = 1 application theme = 1 main data` の詳細な運用を維持します。

## 2026-03-15 09:03 JST 再検証ログ (メイン実行/プル後)

- `main` アップデート後に再集計し、`RQ_TOTAL=60`、`A/B/C=17/25/18`を再確認（このページと`mind-upload-eeg-rq60-feasibility-and-funds.md`の両方で一致）。
- `research_harvest_50.md` の `research question decomposition` セクションをオリジナルの `RQ_COUNT=60` として再抽出し、`0` を削除しました。
- このページで参照されている脳波データ ID (`6, 11, 13, 16, 19, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 2412`) は `EEG-DATA/eeg_dataset_summary_ja.csv` です。すべてのケースが存在します (`0` が欠落しています)。
- Grant ID (`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`) `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`、`grant_queue/*.yaml`、`auto-research-funds/grant_eeg_dataset_match.csv` ですべて参照できます。

### 最新6問を1問ずつ掘り下げていきます（出題順は固定）

1. `U8-1` 閉ループ遅延許容範囲識別: `Main data = 6`、適用先 `G2` (暫定 `G5`)
2. `U8-2` オンライン校正・ドリフト対策：`Main data = 696`、適用先`G2`（暫定`G5`）
3. `U14-1` 固定粒度と追試験合格率：`Main data = 56`、出願先`G1`（予備`G3`）
4. `U14-3` 漏洩監査運用：`Main data = 719`、申請先`G1`（予備`G3`）
5. `U7-2` 時刻同期エラー監査：`Main data = 6`、申請先`G1`（予備`G3`）
6. `U13-1` 意味的一致と因果的一致の分離：`Main data = 509`、出願人`G1`（暫定`G4`）

この順序で進める理由:
- `A/B`判定であれば4週間以内に「実際のKPI＋失敗条件＋申請書案」に到達することも容易です。
- この6つの実測ログをもとに`C`判定（システム主導）を後から提出すると通りやすくなります。

## 2026-03-15 12:02 JST 再検証ログ（メイン実行/深掘り対象修正）

- `RQ_TOTAL=60`、`A/B/C=17/25/18`を再確認し、このページの`RQ`の行数と一致することを確認しました。
- `main EEG-DATA` 列で参照されるすべての ID は `EEG-DATA/eeg_dataset_summary_ja.csv` に存在します (`0` はありません)。
- 許可キー `G1-G6` のすべての実際の ID は、`auto-research-funds` 側で表示できます。
- このページの運営を継続します。各ケースをより深く掘り下げ、「`key things that need to be verified directly with EEG'' and `「EEG 以外で必要なこと」」を明確にし、一般的な要約を避けます。

</article>
</main>

## 2026-03-15 13:03 JST 再検証ログ（メイン実行/継続深掘り操作）

- `main` のプル後、`RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、このページの `RQ` の行と一致していることを確認しました。
- このページで参照されているすべての脳波データ ID (`0` が欠落) が `EEG-DATA/eeg_dataset_summary_ja.csv` に存在することを再確認しました。
- 付与リアルID(`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`)は`auto-research-funds` 全ての項目が横から閲覧できることを再確認しました。
- 今後も方針としては、総括ではなく「1 RQ = 1 検証提案 = 1 申請テーマ = 1 主要データ」を維持し、各 RQ の詳細な説明を優先する。

## 2026-03-15 14:03 JST 再検証ログ（メイン実行/全RQ深掘り再確認修正）

- `mind-upload/wiki/mind-upload-rq60-deep-focus-notes.md` で `RQ` ラインを再カウントし、`60` (`A/B/C=17/25/18`) を確認しました。
- `RQ` の全行において、`G1-G6` のいずれかに `Application theme (grant key)` が割り当てられており、空の `0` があることを確認しました。
- `main EEG-DATA`列(`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`)で参照されるデータIDは24種類ありますが、`EEG-DATA/eeg_dataset_summary_ja.csv`では`0`が欠落していることを確認しました。
- 付与本ID(`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`)は`auto-research-funds`以下で再参照できることを確認しました。
- 方針は変わりません。総括ではなく、「1RQ＝1検証提案＝1申請テーマ＝1本体データ」を深掘りしていきます。

## 2026-03-15 16:22 JST ディープ実装カード（6RQを1つずつ実行）

- 方針: すべての RQ を包括的に更新するのではなく、実装される可能性が高い 6 つの RQ を「1 つずつ詳細に」実行計画に修正しました。
- 対象：`U8-1`、`U8-2`、`U14-1`、`U14-3`、`U7-2`、`U13-1`（以前に固定された優先順位を維持）。

| RQ | EEG-DATAで解ける核（今回修正） | 2 週間の初期実験 (それぞれ 1 回の実験) | アプリケーションテーマ (付与キー) | 使用するEEG-DATA（メイン/予備） | 合否ゲート（次に進むための条件） |
|---|---|---|---|---|---|
| U8-1 | 閉ループ遅延を操作した場合の安定率と回復時間の関係を特定します。 | 同じ前処理パイプラインは、最初の週に 0/50/100/150 ミリ秒の遅延で修正されました。 2週目は安定率、復帰時間、異常停止率を再測定し、閾値テーブルを作成しました。 | 閉ループ遅延許容範囲の特定 (`G2` メイン / `G5` スペア) | `6` / `1972` | 安定率の相対低下は20％以内、異常停止率は従来の上限値以内です。 |
| U8-2 | オンライン校正間隔がパフォーマンスの維持に及ぼす影響を定量化します。 | 最初の週はキャリブレーション間隔の 3 つの条件 (トライアルごと/ブロックごと/固定なし) を設定しました。 2週目ではドリフト量と再校正コストを同時に評価し、動作の上限を決定します。 | コンセプトドリフト対策の最適化（`G2`メイン/`G5`スペア） | `696` / `2412` | 性能維持率の向上は、校正コストの増加に対して統計的に有意です。 |
| U14-1 | 追加トライアル契約の固定粒度（データ/コード/環境）と再現成功率の対応を測定します。 | 最初の 1 週間は、「固定データのみ」、「固定データ + コード」、「固定データ + コード + 環境」の 3 つの粒度で再実行します。 2週目の再現率の差と工数の差を数値化します。 | 複製契約の最小粒度定義（`G1`メイン/`G3`リザーブ） | `56` / `719` | 回収率は目標値を満たしており、工数の増分は許容上限内にあります。 |
| U14-3 | 件名リークと時系列リークを自動的に検出し、リーダーボード評価の監査を有効にします。 | 最初の週にリーク検出ルール (件名/セッション/時間枠) を実装しました。 2 週目に既存のパーティションに適用し、再パーティション化後のパフォーマンスの違いの監査レポートを作成します。 | リーダーボード監査操作 (`G1` メイン / `G3` スペア) | `719` / `56` | ゼロリーク検出、再分割後のパフォーマンス低下を説明できます。 |
| U7-2 | LSL 同期エラーのジッター分布を推定し、動作上の警告しきい値を決定します。 | 最初の週のオフセット/ジッター抽出処理を修正しました。 2週目に閾値を超えるイベント発生率を計算し、再計測のトリガー条件をルールとして設定します。 | 同期エラー自動警告動作（`G1`メイン/`G3`スペア） | `6` / `696` | しきい値超過イベントの再現性と再測定ルールの誤報率は許容範囲内です。 |
| U13-1 | 同じデコーダを使用して、意味的一致と因果的一致の間の不一致を個別に評価します。 | 最初の週では、セマンティック一致スコアと介入応答一致スコアを別のメトリクスで計算します。 2週目では逸脱事例を不合格条件として登録し、模倣スコアのみによる合格判定を禁止します。 | 意味復元・因果再現の個別評価（`G1`メイン/`G4`予備） | `509` / `13` | 意味的一致のみが高いケースを識別でき、因果的一致が存在しないケースを回避できます。 |

### 実行順序（固定）

1. `U8-1`（遅延許容領域）
2. `U8-2` (校正間隔とドリフト)
3. `U14-1` (複製契約の粒度)
4. `U14-3` (漏洩監査)
5. `U7-2` (同期エラー監査)
6. `U13-1` (意味一致/因果一致の分離)

### 今回の実行で修正された操作ルール

- `1RQ=1 verification proposition=1 application theme=1 main data` を 6RQ として再修正します。
- 2 週間以内に「最初の実験結果 + 合否ゲート」に達しなかった RQ は、次回の実行には持ち越されませんが、明確な不合格理由を持つ別の RQ に切り替えられます。
- `C`判定RQは今回の対象外（まずは技術実証を積み上げる方針）。

## 2026-03-15 16:03 JST 再検証ログ (メイン実行/サブモジュールのプル後)

- `mind-upload`/`EEG-DATA`/`auto-research-funds`の最新`main`を反映した上で、深掘りノートの`RQ`ラインを再検証。
- `RQ_TOTAL=60`、`A/B/C=17/25/18`、`Application theme (grant key)` 欠落 `0`、`Main EEG-DATA` 欠落 `0` を再確認しました。
- ポリシーは `1RQ = 1 verification proposition = 1 application theme = 1 main data` のままであり、各問題は個別に詳細に扱われます。

## 2026-03-18 12:08 JST 再検証ログ (メイン実行 / deep-by-RQ 強制)

- 同じポリシーでディープフォーカス操作を再検証しました: 一般的な概要を避け、`1RQ = 1 verification proposition = 1 application theme = 1 main data` を維持します。

## 2026-03-22 11:03 JST 再検証ログ (メイン実行 / 1 つずつのディープ パック更新)

- `RQ_TOTAL=60`と`A/B/C=17/25/18`を`mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`に対して再確認。
- この実行のために、固定ディープ パックを重複しない 6RQ セットに更新しました。
  `U0-1`、`U3-3`、`U4-2`、`U7-5`、`U11-3`、`U14-2`。
- 運用ポリシーを再修正しました。大まかな概要を避け、`1RQ = 1 verification proposition = 1 application theme = 1 main data` を強制します。
- 更新された同期マップ ページ:
  `mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`と
  `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`。
- このページの RQ カバレッジを `research_harvest_50.md` および関連する RQ60 ページに対して再チェックしました (カバレッジは維持されています)。
- 認可キー `G1-G6` と `grant_queue`/`auto-research-funds` のソース解決可能性を再検証しました。
- 確認された EEG 数値 ID は最新の `EEG-DATA` CSV に存在しますが、再インデックス/再マップ後の固定データセット識別子としては信頼できなくなりました。
- この実行の送信ルールを修正しました: 正規参照は `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `DOI + dataset name + access class` を使用して書き込む必要があります。

## 2026-03-18 16:28 JST 再検証ログ (メイン実行 / ディープ同期後のプル)

- この実行前に最新の `main` を取得し、このページを deep-by-RQ モード (`1RQ = 1 verification proposition = 1 application theme = 1 main data`) で再検証しました。
- このページで一意の RQ キーを再カウントし、欠落キーがない `RQ_TOTAL=60` を再確認しました。
- `mind-upload-eeg-rq60-feasibility-and-funds.md`から判断分岐を再計算し、`A/B/C=17/25/18`を再確認しました。
- 最新の `EEG-DATA/eeg_dataset_summary_ja.csv` (`missing=0`) には、再検証された参照 EEG ID (`24` ID: `6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) が存在します。
- 再検証された付与実 ID `G1-G6` (`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`) は、`grant_queue` および `auto-research-funds` マッピング ドキュメントで引き続き解決可能です。

## 2026-03-18 08:04 JST 再検証ログ (メイン実行 / deep-by-RQ 実行ロック)

- この実行の前に、`auto-startup`、`mind-upload`、`auto-research-funds`、`EEG-DATA` の最新の `main` をプルしました。
- このページの一意の `Ux-RQy` キーを再カウントし、`RQ_TOTAL=60` (`missing=0`、`duplicate=0`) を再確認しました。
- `mind-upload-eeg-rq60-feasibility-and-funds.md`に対する判定スプリットを再確認し、`A/B/C=17/25/18`を再確認しました。
- 最新の `EEG-DATA/eeg_dataset_summary_ja.csv` (`missing=0`) で参照される 24 個の EEG ID (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) を再検証しました。
- `grant_queue` および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` での付与実 ID `G1-G6` (`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`) が再検証されました。
- 実行ポリシーは変更されていません。汎用スイープはなく、`1RQ = 1 verification proposition = 1 application theme = 1 main data` を使用した深い 1 つずつの操作のみです。

## 2026-03-18 09:04 JST 再検証ログ (メイン実行 / RQ によるディープ整合性リフレッシュ)

- この実行の前に、`auto-startup`、`mind-upload`、`auto-research-funds`、`EEG-DATA` の最新の `main` をプルしました。
- deep-by-RQの動作(`1RQ = 1 verification proposition = 1 application theme = 1 main data`)を再確認し、`RQ_TOTAL=60`を`A/B/C=17/25/18`で再確認しました。
- 最新の `EEG-DATA/eeg_dataset_summary_ja.csv` (`missing=0`) で参照される 24 個の EEG ID (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) を再検証しました。
- `grant_queue` および `auto-research-funds` マップ ドキュメント内の付与実 ID `G1-G6` (`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`) を再検証しました。
- 現在の CSV から更新された EEG インベントリ ベースライン: `TOTAL=28,152`、`immediate=23,871`、`uncertain_public=3,692`、`account_required=585`、`restricted=4`。
- 実行ルールは変更されていません。一般的なスイープを回避し、RQ ごとに 1 つずつ深い操作を維持します。

## 2026-03-18 10:18 JST 再検証ログ（本run / 1件ずつ深掘りの固定）

- 本ページの `RQ` 行を再計数し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- `main EEG-DATA` 参照IDは`EEG-DATA/eeg_dataset_summary_ja.csv`で全件存在（欠落`0`）を確認しました。
- 助成実ID `G1-G6` は `grant_queue` と `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` で再参照可能でした。
- 継続方針: 汎用要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を維持します。

### とりあえずで深掘りする6RQ（本実行固定）

1. `U4-2`（主データ`56` / `G1`）
2. `U7-5`（主データ`676` / `G1`）
3. `U8-4`（主データ`2412` / `G2`）
4. `U11-1`（主データ`859` / `G2`）
5. `U13-3`（主データ`509` / `G1`）
6. `U14-6`（主データ`719` / `G1`）

## 2026-03-18 19:02 JST 再検証ログ（本実行 / 総合確認）

- `main`プル後に`mind-upload/wiki/mind-upload-rq60-deep-focus-notes.md`を再検証し、`research_harvest_50.md`由来の`RQ_TOTAL=60`（`missing=0`、`duplicate=0`）を再確認しました。
- 判定内訳は `A/B/C=17/25/18` を再計数で確認しました。
- 60RQの全行程で`Application theme (grant key)`と`Main EEG-DATA`が埋まって注目を確認しました。
- `Main EEG-DATA` の参照IDは `EEG-DATA/eeg_dataset_summary_ja.csv` 上で全ファイル存在（`missing=0`）を再確認しました。
- 助成実ID `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）は `grant_queue` と `auto-research-funds` 側マップで再参照可能でした。
- 方針は継続: 汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` を固定し、1件ずつ深掘りします。

### 本runで優先して深掘りする6RQ（1件ずつ実行）

1. `U0-1`（同性KPI二軸ROC、主データ`11`、応募`G2`）
2. `U1-2`（不確実性伝播校正、主データ `56`、応募 `G1`）
3. `U4-2`（最小介入因果主張、主データ `56`、応募 `G1`）
4. `U8-1`（閉ループ遅延許容域、主データ `6`、応募 `G2`）
5. `U13-1`（意味一致/因果一致の分離、主データ `509`、応募 `G1`）
6. `U14-3`（リーク監査運用、主データ `719`、応募 `G1`）

## 2026-03-20 09:35 JST 実行カード更新ログ（本run / 1件ずつ深掘りの固定）

- `mind-upload` / `EEG-DATA` / `auto-research-funds` を再突合し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を維持したまま、2週間で初回結果まで到達しやすい `6RQ` を実行カード化しました。
- 汎用横断ではなく、`1RQ=1検証命題=1応募テーマ=1主データ` で、各RQに `KPI` `失敗条件` `提出最低成果物` を明示しました。
- このrunでは `C` 判定RQを拡張せず、まず `A/B` の実測ログを積む順序に固定しました。

### 本run固定: 2週間実行パック（深掘り6RQ）

| RQ | 最初の実験KPI | 失敗条件 | 提出最低成果物 | 応募先（第一/予備） |
|---|---|---|---|---|
| `U14-1` | `追試成功率` `再現率差` `追加工数` | 最厳格固定条件でも追試成功率が目標未達 | 試験運用補足報告書（陰性例も含む） | `G1 / G3` |
| `U7-2` | `clock offset` `jitter p95` `閾値超過率` | 閾値超過イベントの再現性不足、または誤警報率過大 | 時刻同期監査レポート（オフセット/ジッタ分布） | `G1 / G3` |
| `U14-3` | `被験者リーク検出率` `時系列リーク検出率` `再分割後性能差` | 再分割後もリーク0件を達成できない | 漏洩監査結果と再パーティション証跡 | `G1 / G3` |
| `U8-1` | `安定率` `回復時間` `異常停止率` | 遅延増加で安定率低下が大きく許容域未確定 | クローズドループ安全性 KPI ダッシュボード | `G2 / G5` |
| `U8-2` | `性能維持率` `ドリフト量` `再較正コスト` | 再較正コスト増に対して性能維持率改善が有意でない | クローズドループ安全性 KPI ダッシュボード | `G2 / G5` |
| `U13-1` | `意味一致率` `因果一致率` `乖離ケース率` | 意味一致高・因果一致低ケースを分離できない | 介入プロトコルと反論条件の定義 | `G1 / G4` |

## 2026-03-20 12:03 JST 再検証ログ（本run / 深掘り運用の継続固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull --ff-only origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を基準に `RQ_TOTAL=60`、`A/B/C=17/25/18` を再計数し、整合を確認しました。
- 本ページの方針（汎用横断要約ではなく `1RQ=1検証命題=1応募テーマ=1主データ` で1件ずつ深掘り）を継続固定しました。
- 参照EEG ID（`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`）を `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` と照合し、未解決ID `0` を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）の実在を再確認しました。

## 2026-03-20 13:02 JST 再検証ログ（本run / ユーザー依頼: 全RQを1件ずつ深掘りでwiki再固定）

- 作業開始前に親リポジトリ `auto-startup` の `main` で `git pull origin main` を実行し、`Already up to date` を確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`の`| Ux-yPH0X`行を再計数し、`RQ_TOTAL=60`（欠損・重複`0`）を再確認しました。
- 判定内訳 `A/B/C=17/25/18` を再確認し、全60RQで `1RQ=1検証命題=1応募テーマ=1主データ` の深掘り運用を維持しました。
- 3ページ（`mind-upload`側2ページ + `auto-research-funds`側1ページ）で参照されるEEG ID一意セット（`6, 11, 13, 16, 19, 29, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1972, 2412`）を`EEG-DATA/eeg_dataset_summary_ja.csv`の`ID/旧ID`と照合し、未解決ID `0`を確認しました。
- 助成キー `G1-G6`（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を `grant_queue` と `auto-research-funds` 側で再照合し、全ファイル存在を確認しました。
- 方針は不変で、汎用横断要約ではなく「1件ずつ深く理解して書く」運用を継続します。

## 2026-03-22 15:40 JST 実行カード更新ログ（本run / 6RQ追加バッチ）

- `RQ_TOTAL=60`、`A/B/C=17/25/18` を維持したまま、既存6RQバッチとは重複しない新規6RQを追加し、実行順を固定しました。
- 追加した6RQは `U0-2` `U1-3` `U4-4` `U11-1` `U14-5` `U15-4` で、`KPI` `失敗条件` `提出最低成果物` を知りました。
- `U15-4`（C判定）を含め、制度系RQでも技術監査ログとして2週間で到達できる入口を固定しました。
- 運用ルールは継続して `1RQ=1検証命題=1応募テーマ=1主データ` を適用します。

## 2026-03-22 09:01 JST 再検証ログ (メイン実行/1つずつ深化)

- 広範な概要の拡張を行わずに修正された詳細バッチを更新しました。 `U0-3/U1-2/U7-3/U8-4/U13-2/U15-2`のみを選択しました。
- `RQ_TOTAL=60`、`A/B/C=17/25/18`、および同じ`G1-G6`の操作キーを維持します。
- 送信ルールを `Dxx + DOI + dataset name + access class` としてロックしました (数値 ID は検索専用の従来のガイダンスです)。
- 焦点を絞った成果物のスタイルは引き続き `1RQ = 1 verification proposition = 1 application theme = 1 primary dataset` です。

## 2026-03-27 07:02 JST 再検証ログ（本実行 / 6RQ深掘り固定）

- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を正本として再突合し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 本実行は汎用の追加を行わず、非重複6RQ（`U1-3/U3-5/U7-4/U8-5/U11-3/U15-1`）を`1RQ=1検証命題=1応募テーマ=1主データ`で固定しました。
- 参照主データID（`56,13,676,6,735,49`）は `EEG-DATA/eeg_dataset_summary_ja.csv` で実在（欠落 `0`）を確認しました。
- 助成接続は`G1-G6`実ID系（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を維持しました。

### 本走で優先して深掘りする6RQ

1. `U7-4`（再計測/賞判定木を固定）
2. `U1-3`（逆解法乖離の規則）
3. `U8-5`（オーバーライド安全KPI）
4. `U11-3`（理論比較I/O仕様）
5. `U3-5`（境界拡張プロキシと外部依存境界）
6. `U15-1`（神経データ機微性の制度接続）

## 2026-03-27 13:02 JST 再検証ログ（本実行 / 6RQ深掘り固定）

- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md` を正本として再突合し、`RQ_TOTAL=60`、`A/B/C=17/25/18` を再確認しました。
- 本実行は汎用の追加を行わず、非重複6RQ（`U0-1/U1-1/U4-3/U8-6/U12-3/U14-4`）を`1RQ=1検証命題=1応募テーマ=1主データ`で固定しました。
- 参照主データID（`11,56,19,6`）は `EEG-DATA/eeg_dataset_summary_ja.csv` の `ID/旧ID` で実在（欠落 `0`）を確認しました。
- 助成接続は`G1-G6`実ID系（`GR-2026-013`, `GR-2026-014`, `9Lx4dPK6a4k2gOb7`, `Drbm6vBRDJkn0NGJ`, `871pw3rLjNPKgqA0`, `46z9VPE4wnkrvEJR`）を維持しました。

### 本走で優先して深掘りする6RQ

1. `U1-1`（逆問題の事前分布比較と採択規則）
2. `U0-1`（同一性KPIの観測一致/介入一致二軸化）
3. `U14-4`（モデルカード/データセットカードの契約要件化）
4. `U4-3`（反事実誤差による理論比較固定）
5. `U8-6`（再学習頻度と安全余裕のトレードオフ固定）
6. `U12-3`（心理的連続性監査ログの制度接続準備）

## 2026-03-29 01:37 JST 修正ログ (メインラン/アンカーおよび成果物のドリフト修正)

- 編集前に、`auto-startup`、`mind-upload`、`EEG-DATA`、`auto-research-funds` の最新の `main` をプルしました (すべてのリポジトリの `0 0`、`Already up to date`)。
- `mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers.md` で `### Ux-y` の見出しを再カウントし、`RQ_TOTAL=60` (`missing=0`、`duplicate=0`) を再確認しました。
- `mind-upload/wiki/mind-upload-rq60-deep-evaluation-cards.md`から判定分岐を再計算し、`A/B/C=17/25/18`を再確認しました。
- `EEG-DATA/eeg_dataset_summary_ja.csv` (`旧ID`、`missing=0`) で参照されているレガシー ID セット (`6, 11, 13, 16, 19, 29, 39, 49, 56, 65, 509, 676, 696, 719, 735, 783, 842, 859, 1011, 1839, 1972, 2412, 3419, 4878`) を再確認しました。
- `U11-1` アンカーのドリフトを修正しました。古い `D12=10.21227/qqj2-r702` 参照は無効であり、サポート アンカーとして `D16/D17` を使用して `D14 (10.6084/m9.figshare.1485719)` に調整されました。
- `U12-5` の最小成果物のドリフトを修正しました。この RQ は、同期のみのレポートではなく、一貫して `Branch-based audit log design document` を指すようになりました。
- この修正パスは、solve-first 実行パックを置き換えるものではありません。アクティブな 2026-03-29 パックは、以下の同期された 6 つの RQ セットのままです。

## 2026-03-29 01:44 JST 再検証ログ (メイン実行 / ソルブファースト 6-RQ 同期)

- このメモを、`docs/wiki/mind-upload_eeg_funding_verification_2026-03-29_0137-jst.md`、`mind-upload/wiki/mind-upload-eeg-rq60-feasibility-and-funds.md`、および `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` ですでに修正されている既存の 2026-03-29solve-first パックに同期しました。
- 同じ証拠ルールを維持しました。提出書類では広範な調査、請求の拡張、および数値 ID のみの引用を禁止しました。
- この同期の実行基準を再確認しました。`1RQ = 1 verification proposition = 1 application theme = 1 primary dataset` ルールを緩和せずに、最初の EEG 実験と認可準備済みの問題ステートメントの両方に変換するのが最も簡単な RQ を優先します。

### この実行で同期された最初の 6 RQ パックの解決

1. `U1-1` - 既知の刺激グラウンドトゥルースを備えた従来のベンチマーク
2. `U4-2` - 分析前に修正された最小因果関係主張
3. `U7-1` - 同期/QC/刺激ログの BIDS 拡張契約
4. `U11-1` - 麻酔/睡眠/DoC にわたるランク維持理論の比較
5. `U13-5` - 模倣/メカニズムを分離するための知覚から想起への分岐点
6. `U14-4` - 再現性契約に組み込まれたモデルカード/データセットカード

## 2026-03-29 07:18 JST 再検証ログ (メイン実行 / マインドアップロード公開 6-RQ バッチ)

- 編集前に`auto-startup`、`mind-upload`、`EEG-DATA`、`auto-research-funds`の最新`main`を引っ張ってきて`Already up to date`を再確認。
- `RQ_TOTAL=60`、`A/B/C=17/25/18`、提出証拠ルール `Dxx + DOI + dataset name + access class` を保持しました。
- 概要の範囲を再び広げるのではなく、国民の意識アップロード プログラムを直接強化する RQ を 6 つだけ選択しました。
- `issue.html` のパブリック バッチを同じ 6 つの RQ に同期し、より強力なデータセット/KPI/停止ルールの詳細を Wiki 内に保持しました。

### 現在の公開深化バッチ

| RQ | なぜこれが解決優先なのか | プライマリー D アンカー | グラントレーン | 今ロックする最初の KPI | 外部依存関係を分離して維持する |
|---|---|---|---|---|---|
| `U0-1` | 観察との一致と介入と応答の一致が同じ公的合格/不合格ゲートに強制的に入力されない限り、同一性の主張は簡単に上向きに上昇します。 | `D02` + `D11/D23` をサポート | `G2 / G3` | `observation-match AUC / intervention-response match rate` | 法的/哲学的アイデンティティ基準 |
| `U1-2` | 逆問題の主張は、不確実性の伝播が繰り返しの導電率、電極の欠落、およびノイズの摂動に耐えられない限り、信頼できません。 | `D08` + `D11/D19` をサポート | `G1 / G4` | `interval coverage` | 頭部モデルの識別条件 |
| `U4-4` | 因果関係の同等性の主張はすぐに失敗する必要があるため、結果を読み取る前に改ざんのしきい値をロックする必要があります。 | `D05` + `D08/D19` をサポート | `G1 / G4` | `PEHE + sign-reversal rate` | 共通の I/O 仕様と介入プロトコル |
| `U7-1` | 同期/QC/刺激ログは、依然として保守的なままである公的再現性の主張への最短距離です。 | `D11` + `D15/D23` をサポート | `G1 / G3` | `required-field fill rate` | 機関による導入とガバナンス |
| `U8-4` | 明示的なフェールセーフ遅延メトリクスのない閉ループ プログラムは、公衆の安全を主張する準備ができていません。 | `D20` + `D01/D21` をサポート | `G2 / G5` | `abnormal-detection latency p95` | サイト閉鎖の所有権と運用上の安全性に関する SOP |
| `U11-1` | 認知度インデックスの比較は、理論が勝利した言語ではなく、共有 I/O 全体でのランクの保存に帰着した場合に、公的に安全になります。 | `D14` + `D16/D17` をサポート | `G2 / G4` | `rank-preservation rate` | 理論の採用と臨床責任の分割 |

### この実行では実行順序が固定されました

1. `U7-1`
2. `U1-2`
3. `U4-4`
4. `U0-1`
5. `U8-4`
6. `U11-1`

## 2026-03-29 09:06 JST 再検証ログ (メイン実行 / リポレベルのアンカー監査)

- `auto-startup`、`mind-upload`、`EEG-DATA`、`auto-research-funds` の最新の `main`、さらに `auto-startup.wiki` の `master` をプルし、すべてのターゲット リポジトリで `Already up to date` を再確認しました。
- ルーティング テーブルのみに依存するのではなく、アクティブなパブリック 6-RQ アンカーをローカル `EEG-DATA/wiki/datasets` カードに対して再チェックしました。
- `D11` は、現時点ではローカル ミラー内で最も強力なアンカーです。そのカードは、`BIDS 1.7.0`、`CC0`、`47 sessions`、`186 EEG runs`、`31 EEG + 5 misc`、`5000 Hz`、さらには深刻な監査で引き続き表示される必要がある `README=24 / participants.tsv=25` の不一致さえも公開しているためです。
- `D02` は引き続き有効なクロスセッション ID アンカーですが、現在のローカル カードは控えめな最小セット (`10 participants`、`BrainVision / BrainAmp / actiCHamp`、モーター画像フレーミング、クロスセッション転送ルート) のみを固定します。これはまだ、より充実した介入ログや理論レベルのアイデンティティ文書に代わるものではありません。
- `D05`、`D08`、`D14`、および `D20` は現在のミラー内で有効なルート アンカーのままですが、それらの自動生成されたローカル カードはまだ十分にまばらであるため、公的主張は完全なプロトコル/QC 書類のレベルではなく、`what family of test this anchor supports` と `which logs are still required` のレベルにとどまる必要があります。
- パブリックバッチの実際的な結果: 現在の 6 つの RQ の選択を変更せずに維持しますが、因果関係の同等性、逆問題の適用範囲、閉ループの安全性、または認識指数の比較に関する主張の文言を強化する前に、`required logs` を第一級の成果物として扱います。

## 2026-03-29 12:06 JST 再検証ログ (メイン実行 / 現在の公開バッチの再チェック)

- パブリック ソース ページを変更する前に、同じ 6 つのパブリック RQ をローカル データセット カードとまだ古いライブ `https://mind-upload.com/issue.html` 出力に対して直接再チェックしました。
- `D08` と `D11` は、現在でも最も強力なリポジトリ アンカーであり続けます。`D08` は、介入によるグラウンド トゥルースのソース位置特定ルートを公開するため、`D11` は、ローカル ミラー内の最も豊富な同期/BIDS/セッション実行監査サーフェスを公開するためです。
- `D02` および `D20` は引き続き使用可能な保守的なルート アンカーですが、これはパブリック クレームが、より強力な介入や展開のクレームではなく、セッション間の ID ドリフトまたは閉ループの遅延/安全性監査のレベルに保たれている場合に限られます。
- `D05` は `U4-4` の最小摂動アンカーとして機能しますが、より強力な因果同等性の読み取りは、`D08` クラスのグラウンド トゥルースまたは同等の介入の詳細に関連付けられたままである必要があります。
- `D14` は `U11-1` の最小の麻酔側アンカーとして機能しますが、州をまたぐ文言は、単独の勝者として解釈されるのではなく、`D16/D17` などの睡眠/DoC サポート アンカーと組み合わせたままにする必要があります。
- この実行の実際的な結果: 公開されている 6 つの RQ バッチを変更せずに維持し、`support anchors + required logs` に関する文言を強化し、請求の上限を拡大しないこと。

## 2026-03-29 15:32 JST 再検証ログ (メイン実行 / 公開-6 アンカー証明)

- 公開テキストを変更する前に、同じ 6 つの公開 RQ をライブ `https://mind-upload.com/issue.html` 文言、ローカル `EEG-DATA` データセット カード、公式ファンディング ページ、ライブ Todoist タスク インベントリと照らし合わせて再チェックしました。
- 公開されている 6 つの RQ バッチは変更されていません。`U13-2`、`U13-5`、`U0-2`、`U0-3`、`U14-4`、および `U14-2` は依然として狭い `inner-speech decoding + identity drift + reproducibility auditing` ルートを形成しており、公開ページでは依然として解決済みの請求の更新ではなく `route-setting update` として表示されます。
- ローカル ミラーの現在の保守的なアンカー プルーフは、`D10 -> 000016 3M-CPSEED (OpenNeuro ds006465 v2.0.0, immediate)`、`D03 -> 011012 Data of Multimodal Fusion System for Cognitive Load Assessment in Psychological Experiments: An EEG and Eye-Tracking Study (DOI route, subscription-gated support)`、`D01 -> 016105 Acquisition delay of wireless EEG (DOI route, subscription-gated support)`、`D02 -> 005558 CSTE (DOI route, subscription-gated support)` としてより明示的に修正されました。
- `D03`、`D01`、および `D02` には、ローカル ミラー内に IEEE DataPort でバックアップされたルートがまだあり、`subscription-gated support` として読み取る必要があるため、パブリック ルートはそれらを直接のパブリック アンカーとして扱いません。
- この実行では、資金調達とタスク処理も保守的なままです。`Kura Fund` は `U13/U14` の実質的な最初のルートのまま、`Nakatani Foundation graduate scholarship` は `U13/U0` の生徒向けの主要なブリッジのまま、`Kashinome Scholarship` は滑走路のみの側道のまま、`Nakatani Foundation research grant` は監視モードのままで、必要な開始/期限タスクがすでに存在するため、新しい Todoist タスクは追加されません。
- この実行の実際的な結果: バッチを変更せず、現在の解決優先順序を維持し、次に公開される進行状況しきい値をより強力な要求上限としてではなく `finished minimum artifacts + required logs` として扱います。
