---
layout: default
title: Mind-upload RQ60 アプリケーション プレイブック (RQ ユニット固定)
description: 固定アプリケーション ID、メイン EEG データ、選択理由、および 60 RQ ごとの最小成果物を含む操作ページ。
article_type: ウィキ
subtitle: 一般的な要約ではなく、RQ に基づいて提出の決定を修正する
author: マインドアップロード研究プロジェクト
last_updated: '2026-04-04'
note: RQ ごとの助成金とデータセットのハンドブック
audience: 資金申請と各RQの最初の実験を同時に決めたい人
reading_time: 20～30分
page_intro: このページは、mind-uploadの60のリサーチクエスチョンをそれぞれ対象とし、一次応募先・予備応募先、主なEEG-DATA、採用理由、提出成果物を固定化した実践的なプレイブックです。
accuracy_note: A/B/C判定は`mind-upload-eeg-rq60-feasibility-and-funds.md`と同じ基準となります。
wiki_links:
- label: 'Wiki: RQ60 EEG検証の利用可能性と補助金テーマ'
  url: /wiki/mind-upload-eeg-rq60-feasibility-and-funds.html
  description: 判断根拠、U 固有の背景、RQ 表の原本。
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: 成果物を検証仕様に変換するための基準。
recommended_pages:
- label: 文学地図
  url: /research_harvest_50.html
- label: データとベンチ
  url: /datasets.html
---
<main class="main-container">
<article class="content-column">

## 使用方法

1. `RQ` を 1 つ選択し、`first application destination` と `main EEG-DATA` を固定します。
2. 最初に`minimum deliverables`のみを作成します(完了後に展開します)。
3. `C` の判断はパフォーマンスに関する主張を行うものではなく、システム/監査設計トラックで提出されます。
4. このページの数値 `ID` は検索のガイダンスのみを目的としています。提出/再現性ログは、正規マップ `auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md` の `DOI + dataset name + access class` を使用する必要があります。

## 固定マップ（第一次申請先／予備申請先）

- `U0: G2/G3`, `U1: G1/G4`, `U3: G2/G6`, `U4: G1/G4`
- `U7: G1/G3`、`U8: G2/G5`、`U10: G2/G6`、`U11: G2/G4`
- `U12: G2/G6`、`U13: G1/G4`、`U14: G1/G3`、`U15: G2/G6`

## 現在の資金調達の現実 (2026-03-31 00:04 JST)

- `G1/G2` は、RQ レベルのアプリケーション レーンを安定に保つために使用されるルーティング キーです。これらは現在の許可カード ファイルではありません。
- 現在の補助金カードのエンティティは `G3-G6` で、実際の最終候補リストは現在 [AoyamaLab/auto-research-funds wiki: Mind-Upload-Current-Funding-Shortlist](https://github.com/AoyamaLab/auto-research-funds/blob/main/wiki/Mind-Upload-Current-Funding-Shortlist.md) で修正されています。
- 現在再検証されている 6 つのディープフォーカス RQ は、`U13-2`、`U13-5`、`U0-2`、`U0-3`、`U14-4`、および `U14-2` です。
- 現在、パブリック ルートは意図的に `inner-speech decoding + identity drift + reproducibility auditing` に集中しており、`D10/D03/D01/D02` が保守的なアンカー ファミリとして使用されています。
- `2026-03-31 00:20 JST` での 3 月 31 日のアクセス監査により、現在の判断は絞り込まれています。`D10` は、このファミリーの中で唯一明らかに公開されているプラ​​イマリ アンカーです。 `D03`、`D02`、および `D01` は現在、`LOGIN TO ACCESS DATASET FILES` および `Subscription Required` を表示する IEEE DataPort ページに解決されるため、公開文ではこれらをサブスクリプションゲート型サポート アンカーとしてのみ扱う必要があります。
- このバッチの実際的な資金提供ブリッジは、`Nakatani Foundation graduate scholarship` と `Kura Fund` によって主導されます。 `Kashinome Scholarship` は学生滑走路側ルートとしてのみ残り、`Nakatani Foundation research grant` は現在のオープンコールではなくウォッチモードルートのままです。
- 3 月 31 日の夜の再チェックでは、最新の `EEG-DATA` アップストリームの追加後もルートは変更されません。これは、これらの追加がパブリック オープン アンカーとして `D10` に代わるものではなく、`D03/D02/D01` を即時パブリック ルートに変えるものではないためです。
- 実用的な候補リストに関連する Todoist タスクはこの実行前にすでに存在しており、全項目監査ではまだ `Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3` が表示されているため、この実行では新しいタスクは作成されませんでした。
- すぐに提出できる参照の場合は、数値検索 ID よりも `Dxx + DOI + dataset name + access class` を優先します。
- 以下の 6 つの現在のパブリック行が `Dxx + DOI + dataset name + access class` に同期されるようになったため、プレイブックでは `U13-2/U13-5/U0-2/U0-3/U14-4/U14-2` の数値検索 ID が必要なくなりました。
- `tech_roadmap.md` には `U2/U5/U6/U9` も含まれていますが、これらのロードマップ ファミリは、このプレイブックの現在の `RQ60` 実践レイヤーにはまだ変換されていません。

## 最新のライブソース追記 (2026-04-04 22:06 JST)

- `mind-upload@39248d59caaa`、`EEG-DATA@7ba2201e2b5`、`auto-research-funds@f90279417a9f` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。 `mind-upload` は、ルートを広げることなく、現在の 6 行以外にペア流体バリア ルート ガイダンスを追加します。`EEG-DATA` は、`30,935` マージされた一意の行、`28,898` 高信頼行、`24,910` すぐに使用可能な行、`24,540` 高信頼即時行を維持しながら、`IEEE DataPort EEG records` 監査を強化します。`auto-research-funds` は、現在の実用的な候補リストを置き換えることなく、移動ヘッドの参照のみを緩和します。
- ルートセーフ アクセスの文言は、より明確な理由で狭いままになっています。`D03 / D02 / D01` は、実際の IEEE DataPort ランディング ページよりも DOI/DataCite/カタログ側の読み取りで依然としてオープンに見えるため、`D10` が唯一の明確なパブリック オープン プライマリ アンカーのままである一方、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。
- 行とテーマのマップも、`U13-2 -> D10 3M-CPSEED -> Kura Fund / Nakatani Foundation graduate scholarship`、`U13-5 -> D03 with public-open backups -> Kura Fund / Nakatani Foundation graduate scholarship`、`U0-2 / U0-3 -> D02 with ds004148 + ds007216 stress ladders -> Nakatani Foundation graduate scholarship / Kashinome Scholarship`、`U14-4 / U14-2 -> D01 with D13 rerun support -> Kura Fund / Nakatani Foundation research grant watch / Secom watch` のように、一度に 1 つの質問ごとに固定されます。
- `2026-04-04 22:06 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、および `u13-5-perception-to-recall-route.html` に対しては依然として `HTTP/2 200` が返されました。このソース同期の前に、チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 12:16:08 GMT` を返し、チェックされたボディにはフロント ドアに `2026-04-04 17:07 JST` の文言と `U13-2`、`U13-5` に `2026-04-04 19:09 JST` の文言が依然として表示されていました。
- この走行における公式の窓口スポットチェックでは、実際的な橋は依然として狭いままです: `Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として `2026-04-09` が必ず到着する側道、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` のままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=207`、`projects=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 17:07 JST)

- `mind-upload@dc8ec5dc5e62`、`EEG-DATA@f115f11c2da4`、`auto-research-funds@8d0f5128fcdc` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、ルートを広げることなく、現在の 6 つ以外のバリア側人間プロキシの役割を分割します。`EEG-DATA` は、`30,930` マージされた一意の行、`28,893` の信頼性の高い行、`24,909` の現在の README スナップショット内のすぐに使用できる行を維持しながら、`EEGIS imagined speech` メタデータを深めます。`auto-research-funds` は、`Uehiro ethics foundation` レガシー同期を追加し、`8,616` 補助 ID、`4,319` を報告します。現在の実用的な候補リストを置き換えることなく、`3,971` 公式ソースの行を追加できます。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- 更新されたサポート スペース ナビゲーションは引き続き便利ですが、current-six アンカー ファミリまたは external-current-six キューの行レベルの置き換えは作成されません。バリアの役割分割により現在の 6 つのルートの外側の言語が強化され、新しい想像音声メタデータの深化により `U13-2` サポート スペースの読み取りが改善され、資金提供によるレガシー同期により隣接する滑走路の衛生状態が改善されましたが、それらのいずれも現在の列の順序を変更するものではありません。
- `2026-04-04 17:07 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。このソース同期の前に、チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 07:12:56 GMT` を返し、チェックされた本文には、チェックされた 5 ページすべてにわたって `2026-04-04 14:10 JST` の文言が依然として表示されていました。
- この走行における公式の窓口スポットチェックでは、実際的な橋は依然として狭いままです: `Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として `2026-04-09` が必ず到着する側道、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` のままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`JSM=0`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 14:10 JST)

- `mind-upload@cafeab4bc2a5`、`EEG-DATA@e0695bcac83d`、`auto-research-funds@a4852d89376c` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、ルートを広げることなく、初期の EEG 基礎モデルのソースとステータスの分割に加えて、用語集の興奮性とイオン用語を強化します。`EEG-DATA` は、`30,930` マージされた一意の行、`28,893` 高信頼性の行、`24,909` 即時行、および `24,539` 高信頼性の即時行を維持しながら、`neuroTUM Cybathlon`、`Zenodo TSA v7.8`、および `poetry EEG` メタデータを深めます。 `auto-research-funds` は、現在の実用的な最終候補リストを置き換えることなく、`JELA Diakonia` 奨学金カードを追加します。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- 更新されたサポート スペース ナビゲーションは引き続き便利ですが、current-six アンカー ファミリまたは external-current-six キューの行レベルの置き換えは作成されません。用語集/ソースステータスの厳格化によりフロントドアの規律が改善され、最新のEEGディープダイブにより隣接するサポートスペースの読み取りが改善され、隣接する奨学金の拡張により滑走路のコンテキストが改善されますが、それらのいずれも現在の列の順序を変更するものではありません。
- `2026-04-04 14:10 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および現在の 6 行パケットに対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 04:18:04 GMT` を返し、チェックされたボディは、フロント ドアに `2026-04-04 12:02 JST` の文言と、このソース同期前の古い現在の 6 行パケットに `2026-04-04 09:05 JST` という文言が依然として表示されていました。
- この運行における公式の窓口スポットチェックでは、実際の橋は依然として狭いままである：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 到着必須のサイドルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われる。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 12:02 JST)

- `mind-upload@f84f6e53753b`、`EEG-DATA@017ae806c4dd`、`auto-research-funds@d4024a5b8a1a` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の`mind-upload`ヘッドは、ルートを広げることなくパブリックページ全体でEEG記録フレームコントラクトを同期し、`EEG-DATA`は`30,929`マージされた一意の行、`28,892`高信頼行、`24,908`即時行、`24,538`高信頼即時行を維持しながら、移動容量のEEGデータセットを詳細に調査し、`auto-research-funds`は以前の`11:04 JST`資金追加条項をそのまま継承します。現在の実用的な候補リストを置き換えます。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- 更新されたサポート スペース ナビゲーションは引き続き便利ですが、current-six アンカー ファミリまたは external-current-six キューの行レベルの置き換えは作成されません。記録フレームの同期により公共の技術規律が向上し、移動能力の詳細な調査により隣接するサポート スペースの読み取りが向上し、資金繰越により候補リストが読み取り可能に保たれますが、それらはいずれも現在の行順序を変更しません。
- `2026-04-04 12:02 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 02:19:09 GMT` を返し、チェックされたボディは、このソース同期の前に `issue / brief / bridge / playbook` で `2026-04-04 11:04 JST` の文言がすでに表示されていましたが、`u13-2-brain-minus-prior-route.html` ではまだ `2026-04-04 09:05 JST` の文言が表示されていました。
- この運行における公式の窓口スポットチェックでは、実際の橋は依然として狭いままである：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 到着必須のサイドルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われる。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 11:04 JST)

- `mind-upload@812e1650bae1`、`EEG-DATA@1deac45c75a2`、`auto-research-funds@9741ee45a025` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の`mind-upload`ヘッドはルートを広げることなく用語集のブリッジ証人用語を強化し、`EEG-DATA`は重複したEEG-fMRIオーバーライド行を縮小し、`30,929`マージされた固有の行、`28,892`高信頼行、`24,908`即時行、`24,538`高信頼即時行を維持しながら、現在のアンカーファミリーを変更せず、`auto-research-funds`は現在の実用的なものを置き換えることなく、現在のサイクルの資金調達カードのレガシーカバレッジを追加します。候補者リスト。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- 更新されたサポート スペース ナビゲーションは引き続き便利ですが、current-six アンカー ファミリまたは external-current-six キューの行レベルの置き換えは作成されません。用語集の厳格化により玄関先での読書規律が改善され、重複オーバーライドのクリーンアップにより在庫の衛生状態が改善され、レガシー カードの拡張により滑走路のコンテキストが改善されましたが、いずれも現在の行の順序を変更するものではありません。
- `2026-04-04 11:04 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 01:14:45 GMT` を返し、チェックされたボディにはこのソース同期の前に `2026-04-04 09:05 JST` の文言が依然として表示されていました。
- この運行における公式の窓口スポットチェックでは、実際の橋は依然として狭いままである：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 到着必須のサイドルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われる。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 09:05 JST)

- `mind-upload@e571567f017d`、`EEG-DATA@fbbb0d8c01e0`、`auto-research-funds@d7f6fb9bc158` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは以前の `08:07 JST` ルート ホールド同期を保持するだけで、`EEG-DATA` は `30,929` マージ固有行、`28,892` 高信頼行、`24,909` 即時行、および `24,539` 高信頼即時行を維持しながら、`OpenNeuro ds007020` を制限された残り側サポート ノートとして扱い、`HeartBEAM` と figshare `EEG at rest and with TMS` をバックアップ ファミリとしてのみ保持し、`auto-research-funds` は深く検討された 4 月の追加です現在の実用的な最終候補リストを置き換えることなく、`JGC-S` を隣接する滑走路としてのみ維持しながら、4 つの奨学金を更新します。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- 更新されたサポート スペース ナビゲーションは引き続き便利ですが、current-six アンカー ファミリまたは external-current-six キューの行レベルの置き換えは作成されません。 `OpenNeuro ds007020` は限定されたレストサイドノートのまま、`HeartBEAM` は強力なバックアップ/監視ノートのまま、`JGC-S` は隣接する滑走路ノートのままです。
- `2026-04-04 09:05 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および現在の 6 行パケットに対して `HTTP/2 200` が返されました。チェックされたフロントドアのヘッダーは `Last-Modified: Fri, 03 Apr 2026 23:18:55 GMT` を返し、チェックされたボディにはすでに `2026-04-04 08:07 JST` の文言が表示されていました。現在の 6 行のパケットは `Last-Modified: Sat, 04 Apr 2026 00:11:41 GMT` を返しましたが、このソース同期の前に `2026-04-04 01:04 JST` の文言が依然として表面化していました。
- この運行における公式の窓口スポットチェックでは、実際の橋は依然として狭いままである：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 到着必須のサイドルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われる。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 08:07 JST)

- `mind-upload@418c8f5d0ef9`、`EEG-DATA@dc6d833b83e9`、`auto-research-funds@58d8738be5d5` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、フロントドアの人間代理比較を強化し、`EEG-DATA` は、`30,929` マージ固有行、`28,892` 高信頼行、`24,909` 即時行、および `24,539` 高信頼即時行を維持しながら、`HeartBEAM` および figshare `EEG at rest and with TMS` をバックアップ ファミリとしてのみプロモートし、`auto-research-funds` は、現在の奨学金を置き換えることなく、隣接する滑走路としてのみ `JGC-S` 留学生奨学金を追加します。実用的な候補者リスト。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- 更新されたサポート スペース ナビゲーションは引き続き便利ですが、current-six アンカー ファミリまたは external-current-six キューの行レベルの置き換えは作成されません。 `HeartBEAM` はより強力なバックアップ/監視メモとして保持する価値があり、`JGC-S` は隣接する滑走路メモとしてのみ保持する価値があります。
- `2026-04-04 08:07 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、および `u13-5-perception-to-recall-route.html` に対しては依然として `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Fri, 03 Apr 2026 22:10:18 GMT` を返し、チェックされたボディにはこのソース同期の前に `2026-04-04 01:04 JST` の文言が依然として表示されていました。
- この運行における公式の窓口スポットチェックでは、実際の橋は依然として狭いままである：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 到着必須のサイドルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われる。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 01:04 JST)

- `mind-upload@9b6a8b971ba0`、`EEG-DATA@56d765da60b`、`auto-research-funds@3c8569e28` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドには、初期の `00:06 JST` 再読み取りとフィールド レベルのアーティファクト スタック開示の強化が含まれています。`EEG-DATA` は、`Numbers` および `PRIOS` の公開 OpenNeuro メタデータを強化しながら、`30,921` マージされた一意の行、`28,884` 高信頼行、`24,900` 即時行、および `24,530` 高信頼即時行を維持します。`auto-research-funds` は、`同盟育成会` の現在のカバレッジを追加します。現在の実用的な候補リストを置き換えることなく、`研究のすゝめ奨学金` を選択できます。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `Numbers` と `PRIOS` は、シンボリック番号と刺激応答の読み取り用のサポート スペース メモとして保存する価値がありますが、それでも現在の current-6 アンカー ファミリや外部の現在の 6 キューに代わるものではありません。
- `2026-04-04 01:04 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、および `u13-5-perception-to-recall-route.html` に対しては依然として `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Fri, 03 Apr 2026 15:13:06 GMT` を返し、チェックされたボディにはこのソース同期の前に `2026-04-04 00:06 JST` の文言が依然として表示されていました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`、`同盟会=0`、`研究のすゝめ=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-04 00:06 JST)

- `mind-upload@84d84fb5a82d`、`EEG-DATA@b468ecc5f8c0`、`auto-research-funds@eccee095a939` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、初期の `23:06 JST` ルート再読み取り追加機能を保持するだけであり、`EEG-DATA` は、`30,921` マージされた一意の行、`28,884` 高信頼行、`24,900` 即時行、および `24,530` 高信頼即時行を保持しながら、`fast mapping semantic integration EEG dataset` を追加し、`auto-research-funds` は、現在の実用的な候補リストを置き換えることなく `Iizuka current card and Korean legacy sync` を追加します。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-04 00:06 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、および `u13-5-perception-to-recall-route.html` に対しては依然として `HTTP/2 200` が返されました。このソース同期の前に、チェックされたボディは依然として `22:04 JST` 上で `brief / bridge / U13-2` 上に、`22:04/22:05 JST` 上で `issue` 上に浮上しました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 22:04 JST)

- `mind-upload@1ab35b64796f3936e525befb5d9428d789a16263`、`EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a`、`auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは以前の `21:05 JST` ルート ホールド同期のみを保持し、`EEG-DATA` は `30,918` マージ固有行、`28,881` 高信頼行、`24,898` 即時行、および `24,528` 高信頼即時行を保持しながら `three more deep EEG dataset overrides` を追加し、`auto-research-funds` は現在の実質的な候補リストを置き換えることなく、以前の `21:05 JST` 資金追加付録を保持するだけです。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 22:04 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーはこれらの公開サーフェスでは `Fri, 03 Apr 2026 12:24:26 GMT` でしたが、チェックされたボディは、このソース同期の前に `issue / brief / bridge / U13-2` 上で以前の `21:05 JST` ホールド ノートがすでに表示されていました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 23:06 JST)

- `mind-upload@ec7a7dd713e9`、`EEG-DATA@46f6b56c693c`、`auto-research-funds@b3d3c531729a` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、以前の `22:04 JST` ルート ホールド同期を継承するだけです。`EEG-DATA` は、`30,920` マージされた一意の行、`28,883` 高信頼行、`24,899` 即時行、および `24,529` 高信頼即時行を維持しながら、`motion sickness` および `swallowing EEG` データセットを追加します。`auto-research-funds` は、`KIRII / Pigeon / Nakato / Takashima` 奨学金の対象範囲を深め、さらに `22:04 JST` 資金提供の追加を追加しません。現在の実用的な候補リストを置き換えます。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 23:06 JST` でのブラウザ レベルのライブ チェックでは、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および現在の 6 行パケットに対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーはこれらの公開サーフェスでは `Fri, 03 Apr 2026 13:18:48 GMT` でしたが、フロントドア ページと `U13-2` はすでに `22:04 JST` を表しており、他の 5 行のパケットは、このソース同期の前にまだ初期の `2026-04-02 / 23:08 JST` ホールド ノートを表しています。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 21:05 JST)

- `mind-upload@3db1aa653b74d164c3a57b75677e345ea10356e0`、`EEG-DATA@c10c95274ecf1397768eb28de48aac8ce925c22d`、`auto-research-funds@4a67e06b530bc742521f80fa5b13ccbe1115ebb9` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、以前の `20:05 JST` ルートホールドの追加を保持するだけです。`EEG-DATA` は、`30,914` マージされた一意の行、`28,877` 高信頼行、`24,896` 即時行、および `24,526` 高信頼即時行を保持しながら、欠落している EEG データセットに対する BDSP 手動ディープ ダイブを追加します。また、`auto-research-funds` は、現在の実用的な機能を置き換えることなく、以前の `20:05 JST` ファンディングの追加を保持するだけです。候補者リスト。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 21:05 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーはこれらの公開サーフェスでは `Fri, 03 Apr 2026 11:17:44 GMT` でしたが、チェックされたボディは、このソース同期の前に、`issue / brief / bridge` では以前の `20:05 JST` ホールド ノート、`U13-2` では `11:07 JST` がすでに表示されていました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Nakatani family=11`、`G-7=1`、`ENEOS=0`、`Keio graduate scholarship=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 20:05 JST)

- `mind-upload@b4fd73d9e98301c918b57541704a95246d69ae09`、`EEG-DATA@649ff098ab577f11065562379150acea1aa07002`、`auto-research-funds@7c1b835d1d138214f282dc85d2f06d9faa522310` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の`mind-upload`ヘッドは、アクティブなバッチ外の人体熱証拠を`passive / task-linked macro thermometry`と`perturbation-conditioned thermal routes`に分割し、`EEG-DATA`は制限付きBDSPアルツハイマー`TMS-EEG + rsEEG`リソースを追加しながら、`30,912`マージされた一意の行、`28,875`高信頼行、`24,894`直接使用可能な行を維持し、`auto-research-funds`は、現在の実用的な候補リストを置き換えることなく、`ENEOS`と`G-7`の現在のカードのカバレッジを完了します。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 20:05 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらの公開サーフェスでは現在の `Last-Modified` ヘッダーは `Fri, 03 Apr 2026 10:19:46 GMT` でしたが、チェックされたボディには、このソース同期の前の初期の `11:05/11:07 JST` ホールド ノートが依然として表示されていました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 11:05 JST)

- `mind-upload@f70432e4a6c8a52afafbc57b98c8f0e360c85d4e`、`EEG-DATA@1981d34c5f71deceb2549684db9173b6f54d2b89`、`auto-research-funds@bfebe94da875d709756746285f133ef30905fd38` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドはアクティブなバッチ外の `sleep replay integrity / physiology-gate` の文言を強化し、`EEG-DATA` はインベントリを更新して `COG-BCI` ファミリを詳しく調べながら、`30,904` マージされた一意の行、`28,867` 高信頼行、および `24,890` 直接使用可能な行を維持します。`auto-research-funds` は `10:06 JST mind-upload funding addendum` を引き継ぎながら、`8,596` 支援 ID、`4,308` 行、および `3,958` をレポートします。現在の実用的な候補リストを置き換えることなく、公式ソースの行を追加します。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 11:05 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらの公開サーフェスでは現在の `Last-Modified` ヘッダーは `Fri, 03 Apr 2026 01:31:28 GMT` でしたが、チェックされたボディには、このソース同期の前の初期の `05:12 JST` ホールド ノートが依然として表示されていました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 05:12 JST)

- `mind-upload@a9fc5d1cb691f3669c40803604e78cf87fab4eed`、`EEG-DATA@8c3ace28bad0b3bac259caa440994e5d05bfc7d1`、`auto-research-funds@35756f8381c47daa24bb70bb7a1ff88d1dcf76bc` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、アクティブ キューを変更せずにエクスポートされたミラーの位置を調整する `docs: sync github wiki export` キャリーフォワードです。`EEG-DATA` は、`30,900` マージされた固有行、`28,863` 高信頼行、および `24,885` 直接使用可能な行を維持しながら、最近の `EESM17` メタデータの深化に基づいて `VR navigation dataset` 出力リフレッシュを繰り越します。`auto-research-funds` は、最近のカードの上に `JSPS overseas fellow` の現在のカード スナップショットを追加します。 `JSSF research publication` が更新され、現在の実用的な候補リストを置き換えることなく、`8,594` 補助 ID、`4,307` 行、および `3,957` 公式ソース行がレポートされるようになりました。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 05:12 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらの公開サーフェスでは現在の `Last-Modified` ヘッダーは `Thu, 02 Apr 2026 19:17:56 GMT` でしたが、チェックされたボディには、このソース同期の前の初期の `04:05/04:06 JST` ホールド ノートが依然として表示されていました。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-03 04:06 JST)

- `mind-upload@f5e13ebdc4748ce683d905c37cabfdb3c53036bb`、`EEG-DATA@53f5c8166faf0d5fcebfb5c39741d4992eb82a39`、`auto-research-funds@1f190fec93a9180a27443b1fe2b31f9488dfbf74` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、アクティブなバッチの外部で `BCSFB / human-proxy composition` 文献同期を転送します。`EEG-DATA` は、現在のアンカー ファミリを置き換えないカタログ更新後に、`30,900` マージされた固有行、`28,863` 高信頼行、および `24,885` 直接使用可能な行を保持します。`auto-research-funds` は、`Itoh domestic scholarship` の周囲の現在のカード層とレジストリ層を更新しながら、`8,593` 補助 ID、`4,306` 行、および現在の実用的な候補リストを置き換えることなく、`3,956` 公式ソースの行を追加します。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-03 04:06 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 18:14:39 GMT` でした。
- 今回の実行における公式ウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-02 23:08 JST)

- `mind-upload@f5d1d1dd1683`、`EEG-DATA@ee1463d28288`、`auto-research-funds@ec24a355abbc` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、アクティブなバッチの外側にある因果関係と人間によるプロキシのブリッジを明確にし、`EEG-DATA` は候補のキュレーションを改良し、`OpenNeuro ds007615` を追加すると同時に、現在の README スナップショットで `30,896` マージされた一意の行、`28,859` の信頼性の高い行、および `24,882` 直接使用可能な行を報告します。また、`auto-research-funds` は、現在の実践的な内容を置き換えることなく、`Geo-Kagaku` の現在のカードと README 統計の更新を追加します。候補者リスト。
- ルートセーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリックオープンプライマリアンカーのままですが、`D03 / D02 / D01` はゲートサポートプランニングアンカーのままです。これは、これら 3 つのルートを直接のパブリックアンカーに変える最新のプルヘッドがないためです。
- `2026-04-02 23:08 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 13:12:21 GMT` でした。
- この実行における公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Nakatani Foundation research grant = closed / next-cycle watch (募集期間 2025-06-01 - 2025-07-07)`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Okawa=2`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-02 18:06 JST)

- `mind-upload@85b6603b569b`、`EEG-DATA@a7f9390492fd`、`auto-research-funds@b6c0d0f4eeb7` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、`U7-2` パブリック ブリッジの文言、`EEG-DATA` の詳細な `OSF gazx2` 信頼性 EEG メタデータと `OpenNeuro ds007081` のみを同期し、同時に `30,892` マージされた一意の行、`28,855` 高信頼性行、および現在の README スナップショット内の `24,880` 直接使用可能な行をレポートし、`auto-research-funds` は README 概要を `8,590` 補助 ID、`4,301` に更新します。現在の実用的な候補リストを置き換えることなく、`3,951` 公式ソースの行を追加できます。
- ルートセーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、直接ライブ アクセスの再読み込みでは、これら 3 つのアンカーの現在の `IEEE DataPort` ページに `Subscription Required` と `LOGIN TO ACCESS DATASET FILES` が表示されるためです。
- `2026-04-02 18:06 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u7-2-timing-metric-route.html` に対して `HTTP/2 200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Thu, 02 Apr 2026 08:22:50 GMT` でした。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Secom General Research Grant = closed (March 31, 2026 at 12:00 JST)`、`Nakatani Foundation research grant = closed / next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Okawa=2`、`AI for Aging-Society Problem Solving=0`) が示されていたため、現在のルートと監視ルートはすでにカバーされており、高齢化社会レーンはまだ現在の EEG ファースト ルートの外側にあるため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-02 11:09 JST)

- `mind-upload@208e59e2180c`、`EEG-DATA@00d85380f3f`、`auto-research-funds@f4ba35518400` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。現在の `mind-upload` ヘッドは、初期の 10:07 ルートホールド パケット リフレッシュそのものであり、`EEG-DATA` は公開音声/聴取および聴覚生体認証の詳細な調査を追加し、`30,887` マージされた一意の行、`28,850` の高信頼行、および `24,875` 直接使用可能な行を引き続き報告します。`auto-research-funds` は、リポジトリ統計が `8,585` 支援 ID、`4,293` を読み取りながら、同じ実用的な候補リストを維持します。現在の実用的な候補リストを置き換えることなく、`3,943` 公式ソースの行を追加できます。
- ルート セーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、直接ライブ アクセスの再読み込みでは依然としてこれら 3 つのルート上で `IEEE DataPort` ログインとサブスクリプション ゲートが表示されるためです。
- 最新のパブリックオープン付属物は、現在のルート ファミリを置き換えるのではなく、行固有のバックアップ カバレッジを強化するだけです。`ds007591` と `ds007602` は、`U13-2` の音声側バックアップ オプションを強化しますが、公開された参加者はそれぞれ 3 人だけです。`ChineseEEG-2` は、`U13-5` のパブリック リーディング/リスニング アラインメント カバレッジを強化しますが、意図したリコール ラベル付きブランチは公開しません。また、PhysioNet `auditory-eeg` は明らかにパブリック オープンですが、代替ではなく 1 日の 4 チャネル カバレッジのままです。 `U0-2 / U0-3`の中の`D02`。
- `2026-04-02 11:09 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `mind-upload-rq-solvability-bridge.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、それらの公開サーフェスでは `Thu, 02 Apr 2026 01:22:44 GMT` でした。
- 公式のウィンドウスポットチェックは依然として現実的な橋渡しを狭めています：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` の公式ページは依然として毎年恒例の `mid-January to early-April` ウィンドウ、そして `Secom General Research Grant = 2026-03-13 - 2026-03-31 12:00 (closed)` と表示されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Okawa=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-02 10:07 JST)

- `mind-upload@be507c810b11`、`EEG-DATA@3f20f48cca6e`、`auto-research-funds@fb32c05163f4` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、現在の 6 つ以外の EEG 基盤セットアップと同等の境界を改良し、`EEG-DATA` は HBN EEG リリース 11 ルートを詳細に調査し、`30,887` マージされた固有行、`28,850` 高信頼行、および `24,871` 直接使用可能な行を報告するようになりました。また、`auto-research-funds` は、リポジトリ統計が `8,585` 補助 ID、`4,293` 行、および現在の実用的な候補リストを置き換えることなく、`3,943` 公式ソースの行を追加します。
- ルート セーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、直接ライブ アクセスの再読み込みでは依然としてこれら 3 つのルート上で `IEEE DataPort` ログインとサブスクリプション ゲートが表示されるためです。
- 資金調達に直面している `RQ-by-RQ` ディープドシエも、この実行ではこのページで使用されているのと同じ `Dxx + DOI + dataset name + access class` 標準に再同期されるため、プレイブックと資金調達ドシエは再び同じ正規行パケットを指すようになります。
- `2026-04-02 10:07 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `mind-upload-rq-solvability-bridge.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、それらの公開サーフェスでは `Thu, 02 Apr 2026 00:15:06 GMT` でした。
- 公式のウィンドウスポットチェックは依然として現実的な橋渡しを狭めています：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` の公式ページは依然として毎年恒例の `mid-January to early-April` ウィンドウ、そして `Secom General Research Grant = 2026-03-13 - 2026-03-31 12:00 (closed)` と表示されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Okawa=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-02 09:05 JST)

- `mind-upload@d7f30648fc40`、`EEG-DATA@ac8cc6fc8e74`、`auto-research-funds@31ec17305f6a` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` ヘッドは、現在の 6 つ以外の文献ミエリン ルート分割を強化し、`EEG-DATA` は `aw8sz` の詳細を追加し、`merged_unique=30886`、`high_confidence=28849`、`access_counts_high.immediate=24500` をレポートするようになりました。`auto-research-funds` は、`Aoi graduate scholarship` / `JSSF research grant` マージに加えて、現在の行を置き換えることなく、`8,585` 補助 ID、`4,293` 行、および `3,943` 公式ソース行への README 統計の更新を追加しました。実用的な候補者リスト。
- ルート セーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、直接ライブ アクセスの再読み込みでは依然としてこれら 3 つのルート上で `IEEE DataPort` ログインとサブスクリプション ゲートが表示されるためです。
- `2026-04-02 09:05 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `mind-upload-rq-solvability-bridge.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーはそれらの公開面では `Wed, 01 Apr 2026 23:29:12 GMT` であり、ライブ ページには、このソース更新前の以前の `04:09 JST` / `03:08 JST` 再読メモが、同じ 6 つを同じ順序で保持しながら依然として表示されていました。
- 公式のウィンドウスポットチェックは依然として現実的な橋渡しを狭めています：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` の公式ページは依然として毎年恒例の `mid-January to early-April` ウィンドウ、そして `Secom General Research Grant = 2026-03-13 - 2026-03-31 12:00 (closed)` と表示されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Okawa=2`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-01 20:09 JST)

- `mind-upload@da9644095ba6`、`EEG-DATA@1ecc5cdc0131`、`auto-research-funds@b5cd37febbbb` の後の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の`mind-upload`ヘッドは、現在の6つ以外の人間代理構成証拠の役割を強化し、`EEG-DATA`は、アイオワ・ギャンブルEEGファミリーの詳細な調査を追加しますが、引き続き`merged_unique=30873`、`high_confidence=28836`、および`access_counts_high.immediate=24486`を報告します。`auto-research-funds`は、現在の実用的な候補リストを置き換えることなく、長久研究助成金のスナップショットとリポ統計のリフレッシュを追加します。
- ルート セーフなアクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、ライブ アクセスの読み取りがカタログ側の識別子表面よりも依然として厳格であるためです。
- `2026-04-01 20:09 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `mind-upload-rq-solvability-bridge.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 10:21:50 GMT` でしたが、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant = 2026-03-13 - 2026-03-31 12:00 (closed)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` 監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-01 12:06 JST)

- `mind-upload@9f4bc8e760b1`、`EEG-DATA@1324f9e1ae2b`、`auto-research-funds@6548b1650535` の後の 2 回目の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `EEG-DATA` ヘッドは現在、`merged_unique=30867`、`high_confidence=28830`、および `access_counts_high.immediate=24480` をレポートしますが、これはアンカーの置き換えではなく、メタデータを深化させるための繰り越しのままです。
- ルート セーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、ライブ アクセスの読み取りがカタログ側の識別子の表面よりも狭いためです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 02:26:28 GMT` ですが、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、実際的なブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 今回の再読では、新しい Todoist ルートは導入されませんでした。最新の正規の資金調達候補者リストの監査では、現時点での実際的な領域がすでにカバーされており、公式の再検査では新たな現行サイクルの資金提供者は明らかにされませんでした。

## 最新のライブソース追記 (2026-04-01 11:06 JST)

- `mind-upload@aa21ab9855c1`、`EEG-DATA@cccd137a3468`、`auto-research-funds@3a691196cb9f` の後の最新の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されていません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `EEG-DATA` リポジトリ全体のメタデータの深化と最新の `auto-research-funds` リポ統計の更新によって、これらのアンカーが置き換えられたり、キューの順序が変更されたりすることはありません。
- ルート セーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、ライブ アクセスの読み取りがカタログ側の識別子の表面よりも狭いためです。
- ブラウザレベルのライブチェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して引き続き `200` が返されました。 `Last-Modified` は `issue.html` / `u8-1` および `Wed, 01 Apr 2026 01:21:13 GMT` の 2 つのブリッジ ページで `Wed, 01 Apr 2026 01:21:12 GMT` に進み、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現行サイクルレーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-01 10:19 JST)

- `mind-upload@d87b9ce`、`EEG-DATA@c05ceda146f8`、`auto-research-funds@ca65b206cf6d` の後の最新の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されていません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` 初心者グリアルート監査、最新の `EEG-DATA` `OpenNeuro ds006036` の詳細な調査、および最新の `auto-research-funds` `JCS / Takai / Korean scholarship` の現在のカードのリフレッシュでは、これらのアンカーが置き換えられたり、キューの順序が変更されたりしません。
- ルート セーフ アクセスの文言は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、ライブ アクセスの読み取りがカタログ側の識別子の表面よりも狭いためです。
- `2026-04-01 10:19 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現行サイクルレーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-01 03:09 JST)

- `mind-upload@31835fcd8daa`、`EEG-DATA@12eef8ca4ef0`、`auto-research-funds@040e5b8798fd` の後の最新の実際のプルの再読み取りでは、この Playbook の実際の読み取り値は変更されていません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の `mind-upload` 侵入言語ルート分割、最新の `EEG-DATA` セマンティック テキスト関連性の詳細、および最新の `auto-research-funds` `Obayashi / Yokogaku` カード リフレッシュは、これらのアンカーを置き換えたり、キューの順序を変更したりしません。
- `2026-04-01 03:09 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現行サイクルレーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のライブソース追記 (2026-04-01 01:06 JST)

- 入れ子になった `mind-upload@8da02e2e48e0`、`EEG-DATA@e6013384fa01`、および `auto-research-funds@c6a383f07a7b` の後の 2 回目の no-op の実際のプルの再読み込みでは、この Playbook の実際の読み取り値は変更されません。
- 現在のルートは、パブリック 6 の場合は `D10 / D03 / D02 / D01`、outside-current-6 キューの場合は `U7-1 -> U1-2 -> U4-2 -> U8-1` に固定されたままです。最新の上流デルタは、それらのアンカーを置き換えたり、そのキューの順序を変更したりしません。
- `2026-04-01 01:06 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`u8-1-closed-loop-delay-tolerance-route.html`、`mind-upload-rq-solvability-bridge.html` に対して `200` が返されました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現行サイクルレーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync` の全項目監査では、まだ十分なルート カバレッジ (`items=204`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のプル後の追記 (2026-03-31 21:09 JST)

- `mind-upload@ed6f8203e46d`、`EEG-DATA@20fbbad9959f`、`auto-research-funds@77f189662745` の後の最新のプル再読み込みでは、この Playbook の実質的な読み取り値は変更されていません。
- 最新のプルされたデルタは、現在のルートではなく依然としてサポートを拡大しています。`mind-upload` はデータセット ベンチマーク オブジェクト ルールを厳格化し、FAQ RNA ルート分割を明確にし、`EEG-DATA` はリクエスト ゲート型 `HBUED` 感情認識カバレッジと継続的追跡オンライン BCI メタデータの詳細を追加し、`auto-research-funds` は `Teraura Sayoko outbound scholarship`、`Gakusho scholarship`、および README 統計の更新を追加しましたが、これらの変更はいずれも現在の `D10 / D03 / D02 / D01` ファミリに取って代わるものではありません。外側電流6次`U7-1 -> U1-2 -> U4-2 -> U8-1`。
- `2026-03-31 21:09 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ順序で現在の 6 つの名前が付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現行サイクルレーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync` の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のプル後の追記 (2026-03-31 19:07 JST)

- `mind-upload@b7b6c0498ae1`、`EEG-DATA@24e85cc20f09`、`auto-research-funds@0fddd53bd03c` の後の最新のプル再読み込みでは、この Playbook の実質的な読み取り値は変更されていません。
- 最新のプルデルタは、現在のルートではなく依然としてサポートを拡大しています。`mind-upload`はフロントドアの人間代理分割を強化し、`EEG-DATA`はカタログを`merged_unique=30860`、`high_confidence=28823`、`access_counts_high.immediate=24471`に更新し、`auto-research-funds`はキオクシア/高柳の資金調達記録を更新しましたが、これらの変更はいずれも、現在の`D10 / D03 / D02 / D01`ファミリーやアウトサイドカレント6オーダーの`U7-1 -> U1-2 -> U4-2 -> U8-1`に取って代わるものではありません。
- `2026-03-31 19:09 JST` でのブラウザレベルのライブ チェックでは、`issue.html` と `mind-upload-current-public-six-rq-brief.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ順序で現在の 6 つの名前が付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実質的なブリッジがまだ狭いままですが、`Nakatani Foundation research grant` と `Secom General Research Grant` は現在のサイクルですでに閉鎖されています。
- 新しい Todoist の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## 最新のプル後の追記 (2026-03-31 17:06 JST)

- `mind-upload@4731680627ff`、`EEG-DATA@3e7a53d9ca8`、`auto-research-funds@ef2924014a65` の後の最新のプル再読み込みでは、この Playbook の実質的な読み取り値は変更されていません。
- 最新の `EEG-DATA` の追加により、現在のルートではなくサポート マップが拡大されます。NTU Dataverse の成人から幼児の一方向性神経結合の生/前処理済みリリースはすぐにダウンロード可能で、将来の社会学習やペア観察者の行に役立ちますが、OpenNeuro `ds007146` は、目に見えるパブリック オブジェクト ツリーが主張されている生の EEG / 耳 EEG カバレッジをまだ検証していないため、依然として `uncertain_public` のままです。
- RQ ごとのドシエ内の `### Ux-y` 見出しを再カウントしても `60` が返されるため、この実行では、一度に 1 つの RQ のルートが平坦化されてキューが拡大されることはありません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、依然として `issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。
- したがって、実際の資金調達ブリッジは依然として狭いままです。`Kura Fund`、`Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` は現在の 6 つのアクティブなブリッジのままであり、`Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) ではすでに終了しており、繰り越しウォッチ レコードとしてのみ残されており、このセッションでは新しい Todoist アイテムは作成されませんでした。

## 最新のプル後の追記 (2026-03-31 16:05 JST)

- `mind-upload@a11240d38415`、`EEG-DATA@f318ac8ce42d`、`auto-research-funds@c95cc61fdfc9` の後の最新のプル再読み込みでは、この Playbook の実質的な読み取り値は変更されていません。
- 最新のデルタは、現在のルートではなくサポート マップを拡大します。`mind-upload` はコネクトーム / タイミング ステート ルート カードを強化し、`EEG-DATA` は `OSF eucqf` の詳細な更新を追加し、`auto-research-funds` は新しい `Takeda / Nohken` ファンディング カード マテリアルを追加しましたが、これらの変更はいずれも現在の `D10 / D03 / D02 / D01` ファミリやアウトサイドカレント 6 オーダーの `U7-1 -> U1-2 -> U4-2 -> U8-1` に取って代わるものではありません。
- ブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して引き続き `200` が返されたため、この実行によってパブリック サイトに新たな散文が追加されることはありません。
- 新しい Todoist の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## メタデータ繰越に関する追記 (2026-03-31 16:32 JST)

- `EEG-DATA@3e7a53d9ca84` 後の 2 回目のプル後の再読み込みでも、この Playbook の実際の読み取り値は変更されません。
- 最新の `EEG-DATA` ヘッドは、行選択の変更ではなく、カタログ強化キャリーフォワード (`chore: deep-dive NTU and OpenNeuro EEG metadata`) です。更新されたサマリーでは `merged_unique=30858`、`high_confidence=28821`、および `access_counts_high.immediate=24469` がレポートされるようになりました。これにより、アクティブな `D10 / D03 / D02 / D01` ルート ファミリを置き換えることなく、バックアップ ファミリの検索スペースが向上します。
- アクセスのニュアンスは、提出物の文言にとって引き続き重要です。更新されたカタログでは、引き続き DOI ルートを通じて `D01` が即時として公開され、`D02` が即時/計画バケット内に保持されますが、このプレイブックのパブリック セーフな文言は引き続き厳格なライブ アクセス監査に従っており、したがって `D03 / D02 / D01` はサブスクリプション ゲート型サポート アンカーとして保持されます。
- この実行におけるブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されたため、パブリック サイトの散文を拡張する必要はまだありません。
- 新しい Todoist の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、この実行では新しいタスクは追加されませんでした。

## アンカー強度の再確認(2026-03-30 05:07 JST)

この実行では、同じパブリック 6-RQ バッチと同じ実際の送信ルートが維持されます。変更されたのは、プル後の `EEG-DATA` 再読み取り、ライブサイト チェック、公式ウィンドウの再チェック、および読み取り専用 Todoist の再チェック後の現在のアンカーのアクセス読み取りです。 `D10` は、最初のアーティファクトの唯一の明確に公開されているプラ​​イマリ アンカーのままです。 `D03`、`D02`、および `D01` は、サブスクリプション ゲート型サポート アンカーとしてのみ有用であり、これらを即時パブリック ルートと呼んだ 3 月 30 日初頭のメモは、3 月 31 日のアクセス監査によって置き換えられるべきであると解釈されます。

| RQ | 現在のアンカークラス | 今守るべき資金調達ルート | このルートが依然として適合する理由 | より強力な提案文言の前の補助文 |
|---|---|---|---|---|
| `U13-2` | 強力なプライマリ (`D10 3M-CPSEED`) | `Kura Fund` / `Nakatani Foundation graduate scholarship` | 公開 BIDS スピーチ段階は、`brain-minus-prior` 制御ストーリーへの最短ルートとなります。 | 外部言語評価レイヤーとより広範なコントロール ファミリを追加します。 |
| `U13-5` | ゲート付きサポート (`D03`) | `Kura Fund` / `Nakatani Foundation graduate scholarship` | 意図されている EEG + 視線追跡のペアのルートは依然として知覚から転送までの狭い分岐点の境界にありますが、現在の DataPort ページはサブスクリプションゲート型です。 | `D10`、`ZuCo 2.0`、またはパブリック ロボット音声 EEG ファミリを、より強力なメカニズム言語の前に追加します。 |
| `U0-2` | ゲート付きサポート (`D02 CSTE`) | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship` | クロスセッションおよびクロスタスクの生体認証構造により、意図した最もクリーンな ID ドリフトフロアになりますが、現在の DataPort ページはサブスクリプションゲート型です。 | より明示的なタイミングと同期ログを備えた、より長期的な付属物を追加します。 |
| `U0-3` | ゲート付きサポート (`D02 CSTE`) | `Nakatani Foundation graduate scholarship` / `Kashinome Scholarship` | 同じ ID ドリフト フロアにより、1 つの境界付きルートでのしきい値の安定性とオーバーフィットの除外が維持されますが、現在の DataPort ページはサブスクリプション ゲート型です。 | セッション外部再実行パックとより大きなコホート拡張を追加します。 |
| `U14-4` | ゲート付きサポート (`D01`) | `Kura Fund` / `Nakatani Foundation research grant (watch)` | 遅延優先のワイヤレス遅延データセットは、再実行契約に具体的な開示フィールドを強制的に組み込むのにまだ十分ですが、現在の DataPort ページはサブスクリプションゲート型です。 | `A New Benchmark Dataset Towards Ubiquitous P300 ERP-based BCI Applications` を追加すると、再実行のサンプルが豊富になります。 |
| `U14-2` | ゲート付きサポート (`D01`) | `Kura Fund` / `Nakatani Foundation research grant (watch)` | 同じ遅延の狭いルートは引き続き運用探索/確認分割をサポートしていますが、現在の DataPort ページはサブスクリプションゲート型です。 | 同じ公開ベンチマーク スタイルの再実行付属物と分割違反の例を追加します。 |

- 現在の実用的なルートは既存のタスクですでにカバーされているため、この実行では新しい Todoist タスクは必要ありませんでした。
- `高齢社会課題解決研究(AI)` は依然として、この EEG ファースト、一度に 1 つの RQ ルートの外側にあるため、延期されたままになります。

## 3 月 30 日の公式ウィンドウと Todoist の再チェック後の現在の公開 6

この実行では、同じ公開バッチと同じ資金調達ルートが維持されます。唯一の新しいレイヤーは実行文言です。つまり、現在の行ごとに 1 つの提出準備が整ったテーマ、1 つのアンカー理由、および 1 つのタスク ステータス文です。

| RQ | すぐに投稿できるテーマ | 現在の資金提供者が依然として適している理由 | メインアンカーと最初の成果物 | タスクのステータス |
|---|---|---|---|---|
| `U13-2` | `Neural-contribution audit for imagined speech with a brain-minus-prior control` | `Kura Fund` は依然として限定された若手研究者のベンチマーク ルートに適合し、`Nakatani Foundation graduate scholarship` は依然として博士課程の継続ルートに適合します。 | `D10 3M-CPSEED` は、現在のミラーが `20 participants x 4 sessions` 全体にわたる明白な / 沈黙を意図した / 想像上の音声を含む即時音声デコード パッケージを保持しているためです。最初の成果物: `brain-minus-prior control table`。 | この実行では、既存の `Kura` および `Nakatani graduate scholarship` 開始/期限タスクが再チェックされました。新しい Todoist アイテムは必要ありませんでした。 |
| `U13-5` | `Perception-to-recall transfer-gap benchmark for mimic separation` | `Kura Fund` は依然として境界付きベンチマークの枠組みに適合しており、`Nakatani Foundation graduate scholarship` は依然として博士課程の拡張に適合しています。これは、この行が解決された理論上の主張ではなく、狭いメカニズムの分離テストに留まっているためです。 | `D03 Multimodal Fusion EEG + Eye-Tracking` は、意図したペアの EEG + 視線ルートが依然として質問の範囲内であるためですが、現在の DataPort ページはサブスクリプションゲート型であるためです。最初の成果物: `perception-to-recall degradation note`。 | 既存の `Kura` および `Nakatani graduate scholarship` タスクはすでにこのルートをカバーしています。重複したタスクは追加されませんでした。 |
| `U0-2` | `Temporal-validity-aware identity drift audit with offset, jitter, and state-feature collapse` | `Nakatani Foundation graduate scholarship` は依然として学生向けの継続性 / 生体認証ルートに適合しますが、`Kashinome Scholarship` は依然として滑走路サポート層としてのみ適合します。 | `D02 CSTE` は、意図した `cross-session / cross-task` 生体認証ベンチマークと `10 participants` が依然としてルートを制限しているためですが、現在の DataPort ページはサブスクリプション ゲート型であるためです。最初の成果物: `offset/jitter distribution audit`。 | 既存の `Nakatani graduate scholarship` および `Kashinome` タスクが再チェックされました。新しいタスクは必要ありませんでした。 |
| `U0-3` | `Task-specific threshold stability and overfit-exclusion benchmark for identity drift` | 同じ `Nakatani graduate scholarship` と `Kashinome` のルートは依然として適合します。なぜなら、この行は、より広範な個人性の主張ではなく、限定された博士課程の閾値とガバナンスの問題にとどまっているからです。 | `D02 CSTE` は `U0-2` と同じ ID ドリフトフロアにありますが、現在の DataPort ページはサブスクリプションゲート型です。最初の成果物: `threshold-stability note and selection rationale`。 | 既存の `Nakatani graduate scholarship` および `Kashinome` タスクはすでにこの行をカバーしています。新しいタスクは必要ありませんでした。 |
| `U14-4` | `Card-integrated reproducibility contract for the current public batch` | `Kura Fund` は依然として若手研究者の即時再現性パッケージに適合していますが、`Nakatani Foundation research grant` は現在のサイクルが終了しているため監視のみのままです。 | `D01 Acquisition delay of wireless EEG` は、意図した遅延優先の測定ルートが依然として開示パッケージに制限されているためですが、現在の DataPort ページはサブスクリプションゲート型であるためです。最初の成果物: `filled Model Card / Dataset Card examples`。 | 既存の `Kura` タスクと既存の `Nakatani research grant` 監視タスクが再チェックされました。新しいタスクは必要ありませんでした。 |
| `U14-2` | `Exploration-vs-confirmation split contract for reruns` | `Kura Fund` は依然として即時限定再現ルートに適合しますが、`Nakatani Foundation research grant` は引き続き次サイクル監視ルートのみです。 | `D01 Acquisition delay of wireless EEG` は `U14-4` と同じレイテンシ優先再実行フロアにありますが、現在の DataPort ページはサブスクリプションゲート型です。最初の成果物: `fixed-split rerun contract and negative-case trail`。 | 既存の `Kura` および `Nakatani research grant` 監視タスクはすでにこの行をカバーしています。新しいタスクは必要ありませんでした。 |

## RQ別固定表（60項目）

| RQ | 判定 | 最初の申請者 | 予備申請者 | メイン脳波データ | 主要データの選定理由 | 最小限の成果物 |
|---|---|---|---|---:|---|---|
| U0-1 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | 同じフレームワーク内のセッション間での ID の変更を追跡するのは簡単です。 | 介入プロトコルと反論条件の定義 |
| U0-2 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | D02 CSTE (10.21227/j162-nh61 / サブスクリプションゲート型サポート) | 繰り返されるセッション、クロスタスク ID ラベル、タイムスタンプ/QC メタデータにより、依然として `clock offset + jitter + state-feature collapse` 監査の最もクリーンなアンカーとなっていますが、現在の DataPort ページはサブスクリプションゲート型です。 | 時刻同期監査レポート（オフセット/ジッタ分布） |
| U0-3 | A | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | D02 CSTE (10.21227/j162-nh61 / サブスクリプションゲート型サポート) | 繰り返されるセッションとクロスタスク分割では、しきい値安定性とオーバーフィット除外ルートが `U0-2` と同じ ID ドリフト アンカー上に留まりますが、現在の DataPort ページはサブスクリプション ゲート型です。 | 閾値検索ノートと選択根拠表 |
| U0-4 | B | G2 (GR-2026-014) | G3 (9Lx4dPK6a4k2gOb7) | 11 | 同じフレームワーク内のセッション間での ID の変更を追跡するのは簡単です。 | 同一性判定二軸レポート（観察一致／介入一致） |
| U1-1 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知の介入/高密度条件下での逆問題の誤差と不確実性を簡単に測定できます。 | 逆解比較表と不確かさ分布図 |
| U1-2 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知の介入/高密度条件下での逆問題の誤差と不確実性を簡単に測定できます。 | 逆問題再現レポート（エラー/不確実性） |
| U1-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知の介入/高密度条件下での逆問題の誤差と不確実性を簡単に測定できます。 | 逆問題再現レポート（エラー/不確実性） |
| U1-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 56 | 既知の介入/高密度条件下での逆問題の誤差と不確実性を簡単に測定できます。 | 逆解比較表と不確かさ分布図 |
| U3-1 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | 脳波単独と多峰性の状態の違いを同じ評価軸で簡単に比較できます。 | 境界拡張評価レポート（単体・統合比較） |
| U3-2 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | 脳波単独と多峰性の状態の違いを同じ評価軸で簡単に比較できます。 | 境界拡張評価レポート（単体・統合比較） |
| U3-3 | B | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | 脳波単独と多峰性の状態の違いを同じ評価軸で簡単に比較できます。 | 境界拡張評価レポート（単体・統合比較） |
| U3-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | 脳波単独と多峰性の状態の違いを同じ評価軸で簡単に比較できます。 | 境界拡張評価レポート（単体・統合比較） |
| U3-5 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | 脳波単独と多峰性の状態の違いを同じ評価軸で簡単に比較できます。 | 境界拡張評価レポート（単体・統合比較） |
| U3-6 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 13 | 脳波単独と多峰性の状態の違いを同じ評価軸で簡単に比較できます。 | 境界拡張評価レポート（単体・統合比較） |
| U4-1 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入の有無を明確に示すことで、相関関係と因果関係の区別が容易になります。 | 介入プロトコルと反論条件の定義 |
| U4-2 | A | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入の有無を明確に示すことで、相関関係と因果関係の区別が容易になります。 | 介入プロトコルと反論条件の定義 |
| U4-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入の有無を明確に示すことで、相関関係と因果関係の区別が容易になります。 | 介入プロトコルと反論条件の定義 |
| U4-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 19 | 介入の有無を明確に示すことで、相関関係と因果関係の区別が容易になります。 | 因果関係検証報告書（最小限介入主張） |
| U7-1 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期、QC、再現性の監査は、運用指標に簡単に直接リンクできます。 | 時刻同期監査レポート（オフセット/ジッタ分布） |
| U7-2 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期、QC、再現性の監査は、運用指標に簡単に直接リンクできます。 | 時刻同期監査レポート（オフセット/ジッタ分布） |
| U7-3 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期、QC、再現性の監査を運用指標に直接結び付けるのが簡単です。 | 再現性監査レポート（同期/QC/前処理差異） |
| U7-4 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期、QC、再現性の監査は、運用指標に簡単に直接リンクできます。 | 再現性監査レポート（同期/QC/前処理差異） |
| U7-5 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期、QC、再現性の監査は、運用指標に簡単に直接リンクできます。 | 閾値検索ノートと選択根拠表 |
| U7-6 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 676 | 同期、QC、再現性の監査は、運用指標に簡単に直接リンクできます。 | 再現性監査レポート（同期/QC/前処理差異） |
| U8-1 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループ KPI は簡単に測定できます。 | クローズドループ安全性 KPI ダッシュボード |
| U8-2 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループ KPI は簡単に測定できます。 | クローズドループ安全性 KPI ダッシュボード |
| U8-3 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループ KPI は簡単に測定できます。 | 動作安定性レポート（安全停止/復旧時間） |
| U8-4 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 2412 | 閉ループの異常検出レイテンシー、フェールセーフトリガー、リカバリーを同じ契約で測定できます。 | 動作安定性レポート（安全停止/復旧時間） |
| U8-5 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループ KPI は簡単に測定できます。 | クローズドループ安全性 KPI ダッシュボード |
| U8-6 | B | G2 (GR-2026-014) | G5 (871pw3rLjNPKgqA0) | 6 | 遅延/再学習/安全停止の閉ループ KPI は簡単に測定できます。 | クローズドループ安全性 KPI ダッシュボード |
| U10-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論的な一貫性と生理学的代理の違いを段階的に検証するのは簡単です。 | 理論整合性メモと代理相関分析 |
| U10-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論的な一貫性と生理学的代理の違いを段階的に検証するのは簡単です。 | 理論整合性メモと代理相関分析 |
| U10-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論的な一貫性と生理学的代理の違いを段階的に検証するのは簡単です。 | 理論整合性レポート (熱力学プロキシ) |
| U10-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 735 | 理論的な一貫性と生理学的代理の違いを段階的に検証するのは簡単です。 | 理論整合性メモと代理相関分析 |
| U11-1 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 理論指標のランキングを保存したり、状態差分データを使用して故障状況を検証したりすることが簡単です。 | 認知度指数比較レポート（故障条件あり） |
| U11-2 | C | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 状態差分データを利用して、理論指標の順位維持や破綻状況を簡単に検証できます。 | I/O仕様と計算予算の理論比較 |
| U11-3 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 理論指標のランキングを保存したり、状態差分データを使用して故障状況を検証したりすることが簡単です。 | 認知度指数比較レポート（故障条件あり） |
| U11-4 | B | G2 (GR-2026-014) | G4 (Drbm6vBRDJkn0NGJ) | 735 | 理論指標のランキングを保存したり、状態差分データを使用して故障状況を検証したりすることが簡単です。 | I/O仕様と計算予算の理論比較 |
| U12-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | システムの問題に渡される監査ログを維持することは技術的には簡単です。 | ブランチベースの監査ログ設計ドキュメント |
| U12-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | システムの問題に渡される監査ログを維持することは技術的には簡単です。 | システム監査要件表（テクニカルログ対応） |
| U12-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | システムの問題に渡される監査ログを維持することは技術的には簡単です。 | システム監査要件表（テクニカルログ対応） |
| U12-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | システムの問題に渡される監査ログを維持することは技術的には簡単です。 | ブランチベースの監査ログ設計ドキュメント |
| U12-5 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | ブランチの再リンクやサブジェクト ID の再編成の決定をサポートする監査ログを維持することは、技術的には簡単です。 | ブランチベースの監査ログ設計ドキュメント |
| U12-6 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 11 | システムの問題に渡される監査ログを維持することは技術的には簡単です。 | システム監査要件表（テクニカルログ対応） |
| U13-1 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 制御条件を使用することで、意味的な復元と機構的な差異を分離することが容易になります。 | 介入プロトコルと反論条件の定義 |
| U13-2 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | D10 3M-CPSEED (10.18112/openneuro.ds006465.v2.0.0 / 即時) | 明白/無言/想像上の音声とトランスクリプトに合わせたフェーズにより、幻覚や神経不一致の監査に対する現在の最強の `brain-minus-prior` アンカーになります。 | ミミック分離評価スクリプトと制御条件テーブル |
| U13-3 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 制御条件を使用することで、意味的な復元と機構的な差異を分離することが容易になります。 | 模倣品分離評価報告書（意味・仕組み） |
| U13-4 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 意味的復元とメカニズムの違いは、制御条件下で簡単に分離できます。 | 介入プロトコルと反論条件の定義 |
| U13-5 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | D03 マルチモーダル フュージョン EEG + アイトラッキング (10.21227/6106-6120 / サブスクリプションゲート型サポート) | 共有 EEG と視線ストリームは依然として知覚から想起までの分岐分析を制限し、メカニズムの保存を誇張することなくデコーダ転送の失敗を解釈しやすくしますが、現在の DataPort ページはサブスクリプションゲート型です。 | ミミック分離評価スクリプトと制御条件テーブル |
| U13-6 | B | G1 (GR-2026-013) | G4 (Drbm6vBRDJkn0NGJ) | 509 | 制御条件を使用することで、意味的な復元と機構的な差異を分離することが容易になります。 | 漏洩監査結果と再パーティション証跡 |
| U14-1 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試験契約の運用、監査の漏洩、不利な事例の開示などを修正するのは簡単です。 | 試験運用補足報告書（陰性例も含む） |
| U14-2 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | D01 ワイヤレス EEG の取得遅延 (10.21227/dv1p-vq18 / サブスクリプション ゲート サポート) | レイテンシーファーストの測定パッケージは、探索/確認の分割と再実行契約を狭く、測定可能で、公衆の安全性を維持するのに十分ですが、現在の DataPort ページはサブスクリプションゲート型です。 | 試験運用補足報告書（陰性例も含む） |
| U14-3 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試験契約の運用、監査の漏洩、不利な事例の開示などを修正するのは簡単です。 | 漏洩監査結果と再パーティション証跡 |
| U14-4 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | D01 ワイヤレス EEG の取得遅延 (10.21227/dv1p-vq18 / サブスクリプション ゲート サポート) | フィールド全体の標準化を主張することなく、モデル カードとデータセット カードのフィールドを再実行コントラクトに接続するには、同じレイテンシ/測定アンカーで十分ですが、現在の DataPort ページはサブスクリプション ゲート型です。 | モデル/データセット カードのテンプレートと記入例 |
| U14-5 | B | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試験契約の運用、監査の漏洩、不利な事例の開示などを修正するのは簡単です。 | ネガティブサンプルレジストリ初版（CSV+運用ルール） |
| U14-6 | A | G1 (GR-2026-013) | G3 (9Lx4dPK6a4k2gOb7) | 6 | 追試験契約の運用、監査の漏洩、不利な事例の開示などを修正するのは簡単です。 | コンテナ再生産手順書とコスト測定を修正 |
| U15-1 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全なシャットダウンと権限管理のためのシステム監査インジケーターに簡単に接続できます。 | システム統合監査報告書（停止・更新条件） |
| U15-2 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全なシャットダウンと権限管理のためのシステム監査インジケーターに簡単に接続できます。 | システム監査要件表（テクニカルログ対応） |
| U15-3 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全なシャットダウンと権限管理のためのシステム監査インジケーターに簡単に接続できます。 | システム監査要件表（テクニカルログ対応） |
| U15-4 | C | G2 (GR-2026-014) | G6 (46z9VPE4wnkrvEJR) | 49 | 安全なシャットダウンと権限管理のためのシステム監査インジケーターに簡単に接続できます。 | システム監査要件表（テクニカルログ対応） |


## 追加情報

- このページは「投稿操作を修正する」ためのクイックガイドです。決定理由の詳細は`mind-upload-eeg-rq60-feasibility-and-funds`をご参照ください。
- `C` 判決 RQ では、主張を組織的要件と監査要件に限定し、過剰なパフォーマンスの主張を避けてください。

## 2026-03-14 19:12 JST 追加

- 60個のRQを再スキャンし、各RQの「初回申請先/予備申請先/メインEEG-DATA/最低限の成果物」を修正。
- A/B/C（`17/25/18`）の番号は元のページと一致します。
- このページの目的は、一般的な概要を避け、`1RQ=1 submission decision` をすぐに実行できるようにすることです。

## 2026-03-15 10:02 JST 再検証ログ (メイン実行/プル後)

- `git pull --rebase --autostash` を実行した後、`main` で再検証し、`RQ_TOTAL=60` を再チェックします。
- このページと`mind-upload-rq60-deep-focus-notes.md`を比較し、`A/B/C=17/25/18`の内訳が一致していることを確認してください。
- `First application destination/preliminary application destination/main EEG-DATA/minimum deliverables'' of each RQ line is missing `0`, blank `0`。
- 付与されるリアルID（`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`）は`auto-research-funds`側で参照可能です。
- ポリシーの継続: 概要の代わりに `1RQ=1 submission judgment` を修正し、RQ 単位でアプリケーション テキストに直接転送します。

## 2026-03-15 12:02 JST 再検証ログ（今回の実行確認・RQユニット提出判定修正）

- `RQ_TOTAL=60` と `A/B/C=17/25/18` を再確認し、`mind-upload-eeg-rq60-feasibility-and-funds.md` と完全に一致します。
- 「`First applicant/Preliminary applicant/Main EEG-DATA/Minimum deliverable'' in all `RQ` lines is missing `0`, blank `0」。
- `main EEG-DATA` の参照 ID は `EEG-DATA/eeg_dataset_summary_ja.csv` であり、すべての項目が存在します (`0` が欠落しています)。
- 付与本ID(`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`)は`auto-research-funds` / `grant_queue`で全項目再参照可能。

</article>
</main>

## 2026-03-15 13:03 JST 再検証ログ (メイン実行 / アプリケーション プレイブックの整合性チェック)

- `main` プル後にこのページを再検査したところ、`1st applicant/Preliminary applicant/main EEG-DATA/Minimum deliverables' were missing `0` and blank `0` in all `60RQ` 行が確認されました。
- `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一貫性を保ちます。
- グラントキー `G1-G6` Real ID (`GR-2026-013`、`GR-2026-014`、`9Lx4dPK6a4k2gOb7`、`Drbm6vBRDJkn0NGJ`、`871pw3rLjNPKgqA0`、`46z9VPE4wnkrvEJR`) `auto-research-funds`で再参照できることを確認。
- 実際のアプリケーションはそのままにします。一般的なテーマにする代わりに、`1RQ=1 submission judgment` でアプリケーションのテキストに直接転写できる粒度を維持します。

## 2026-03-15 16:03 JST 再検証ログ (メイン実行/サブモジュールのプル後)

- `main` をプルした後、もう一度 `RQ=60` ラインを確認し、`First applicant/Preliminary applicant/Main EEG-DATA/Minimum deliverables` の欠落している `0` を確認します。
- 判定の内訳 `A/B/C=17/25/18` は `mind-upload-eeg-rq60-feasibility-and-funds.md` と一致しています。
- このページの運用を継続します: `1RQ=1 submission judgment` が修正され、申請テキストは総括ではなく RQ 単位で掲載されます。

## 2026-03-18 11:20 JST 再検証ログ (メイン実行 / プレイブックの整合性更新)

- 最新の `main` をプルし、`mind-upload=d0a06cf30f2d`、`EEG-DATA=357cd9af4962`、`auto-research-funds=a6ffdb0898e8` へのベース コミットを修正しました。
- 固有の `Ux-y` キーを使用してこのプレイブックを再確認し、`60RQ` のカバレッジ (`0` の欠落、`0` の重複) を再確認しました。
- `mind-upload-eeg-rq60-feasibility-and-funds.md` に対する `A/B/C=17/25/18` の一貫性を再確認しました。
- 認可キー `G1-G6` を再検証し、各 ID が `grant_queue` または `auto-research-funds` ソースから引き続き解決可能であることを確認しました。
- 実行と書き込みについても同じルールを継続します。`1RQ=1 submission decision` を保持し、汎用テーマではなく RQ 単位でアプリケーションに転送します。

## 2026-03-18 12:08 JST 再検証ログ (メイン実行 / 1-RQ 実行ガード)

- このプレイブックを行ごとに再チェックし、`Ux-RQy` 行の欠落がない `60RQ` カバレッジを再確認しました。
- 実現可能性ページとの整合性を再検証: `A/B/C=17/25/18` は変更なし。
- `grant_queue` および `auto-research-funds` ソースの許可 ID `G1-G6` が再検証されました。
- 現在の `EEG-DATA/eeg_dataset_summary_ja.csv` は数値 ID を再マップしているため、このページの数値 ID は検索補助としてのみ扱われます。
- 提出可能参照は`auto-research-funds/wiki/Mind-Upload-EEG-RQ-Grant-Map.md`から`DOI + dataset name + access class`に固定されます。
