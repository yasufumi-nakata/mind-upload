# Mind-upload 現在のパブリック 6: EEG ルートの概要

> 解決済みのクレームの最新情報ではなく、狭いルートの概要
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-04-04 / Role: 現在の公立6名

## このページの役割
このページは、1 つの RQ、1 つの境界アンカー、1 つの最初のアーティファクト、および 1 つのファンディング センテンスのレベルで、現在の公開されている 6 つの質問のルートを修正します。

## 公開ページへ戻る
- [発行ページ](https://mind-upload.com/issue.html)
- [ディープフォーカスノート](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-rq60-deep-focus-notes)

## 関連 Wiki ページ
- [Wiki: RQ 可解決性ブリッジ](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-rq-solvability-bridge) - EEG が現在クローズできるもの、まだ外部のサポートが必要なもの、そしてどの資金レーンがまだ適合しているのかを 1 ページにまとめました。
- [Wiki: RQ ごとの詳細な資料](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-rq60-rq-by-rq-deep-dossiers) - 現在のパブリック 6 とより広い 60RQ マップの長期間にわたる作業書類。
- [Wiki: 助成金とデータセットのプレイブック](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-eeg-rq60-grant-dataset-playbook) - 各 RQ から現在の制限付き資金レーンおよび EEG アンカーまでのルート。
- [Wiki: U13-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u13-2-brain-minus-prior-route) - なぜ D10 が U13-2 の 1 位に留まるのか、なぜ他のスピーチ候補が 2 番目に留まるのか、そして最初のアーティファクトが正直に解決できるものは何なのか。
- [Wiki: U13-5 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u13-5-perception-to-recall-route) - D03 が U13-5 の意図されたゲート サポート アンカーであり続ける理由、サポート アンカーが二次的なままである理由、およびトランスファー ギャップ アーティファクトが正直に埋めることができるもの。
- [Wiki: U0-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u0-2-temporal-validity-route) - D02 が U0-2 の意図されたゲート サポート アンカーであり続ける理由、サポート アンカーが二次的なままである理由、タイミング フロア アーティファクトが正直に閉じることができるもの。
- [Wiki: U0-3 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u0-3-threshold-stability-route) - D02 が U0-3 の意図されたゲート サポート アンカーであり続ける理由、サポート アンカーが二次的なままである理由、およびしきい値ガバナンス アーティファクトが正直に閉じることができるもの。
- [Wiki: U14-4 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u14-4-card-contract-route) - D01 が U14-4 の意図されたゲート サポート アンカーであり続ける理由、よりリッチな再実行ベンチマークが二次的なままである理由、カード契約アーティファクトが正直に解決できるもの。
- [Wiki: U14-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u14-2-fixed-split-route) - D01 が U14-2 の意図されたゲート サポート アンカーであり続ける理由、よりリッチな再実行ベンチマークが二次的なままである理由、固定分割アーティファクトが正直に解決できるもの。
- [Wiki: U7-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u7-2-timing-metric-route) - 現在のパブリック 6 を変更せずに、同じ D11 同期ファミリーを読み取り可能に保つ隣接するタイミング メトリック パケット。

---

# Mind-upload 現在のパブリック 6: EEG ルートの概要

このページでは、現在の公開されている 6 つの質問のバッチを `one RQ -> one bounded EEG anchor -> one first artifact -> one funding bridge` レベルで読めるようにしておきます。

解決された申し立てを発表するものではありません**。 `mind-upload`、`EEG-DATA`、`auto-research-funds`、ライブ公開ページ、現在の公式資金調達ウィンドウ、読み取り専用の Todoist 再チェックのプル後のレビューを経て、現在のパブリック ルートがサポートできるほど狭いものだけが記載されています。

## 2026 年 4 月 4 日の 22:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@39248d59caaa`、`EEG-DATA@7ba2201e2b5`、および `auto-research-funds@f90279417a9f` の後の `2026-04-04 22:06 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、ルート置換ではなく引き続き引き継がれます。`mind-upload` は、ルートを広げることなく、現在の 6 つの外側にペア流体バリア ルート ガイダンスを追加します。`EEG-DATA` は、`30,935` マージされた一意の行、`28,898` 高信頼行、`24,910` すぐに使用可能な行、`24,540` 高信頼即時行を維持しながら、`IEEE DataPort EEG records` 監査を強化します。`auto-research-funds` は、移動ヘッド参照のみを緩和します。現実的な候補リストを置き換えます。
- したがって、ルート セーフ アクセスの文言は、より明確な方法で狭いままになります。`D03 / D02 / D01` は、実際の IEEE DataPort ランディング ページよりも DOI/DataCite/カタログ側の読み取りで依然としてオープンに見えるため、`D10` が唯一の明確なパブリック オープン プライマリ アンカーのままであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- 3 つのスタックの読み取りも、一般的ではなく明示的なままです。`U13-2 / U13-5` は音声側制御と転送ギャップのペアのまま、`U0-2 / U0-3` はアイデンティティ ドリフト フロアとしきい値ガバナンスのペアのまま、`U14-4 / U14-2` はカード契約と固定分割再実行ガバナンスのペアのままです。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、および `u13-5-perception-to-recall-route.html` に対して `HTTP/2 200` が返されました。このソース同期の前に、チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 12:16:08 GMT` を返し、チェックされたボディはフロント ドアに `2026-04-04 17:07 JST` の文言と `U13-2` が表示され、`U13-5` に `2026-04-04 19:09 JST` の文言が表示されました。
- 公式窓口のスポットチェックでは、実際的な橋は依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として `2026-04-09` 到着必須の側道、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` として表示されます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=207`、`projects=2`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。 DOI/カタログ ビュー自体が `D03 / D02 / D01` を促進しない理由を明確にしながら、一度に 1 つずつ同じ RQ バッチを最新のプルされたヘッドに運ぶだけです。

## 2026 年 4 月 4 日の 17:07 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@dc8ec5dc5e62`、`EEG-DATA@f115f11c2da4`、および `auto-research-funds@8d0f5128fcdc` の後の `2026-04-04 17:07 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- プルされた最新のデルタは、ルート置換ではなく引き続き引き継がれます。`mind-upload` は、ルートを拡大することなく、現在の 6 つの外側でバリア側の人間プロキシの役割を分割します。`EEG-DATA` は、`30,930` マージされた一意の行、`28,893` 高信頼行、および `24,909` すぐに使用できる行を現在の README スナップショットに保持しながら、`EEGIS imagined speech` メタデータを深めます。`auto-research-funds` は、レポートを作成しながら `Uehiro ethics foundation` レガシー同期を追加します。実際の候補リストを置き換えることなく、`8,616` 援助 ID、`4,319` 行、および `3,971` 公式ソース行。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- 3 つのスタックの読み取りも、一般的ではなく明示的なままです。`U13-2 / U13-5` は音声側制御と転送ギャップのペアのまま、`U0-2 / U0-3` はアイデンティティ ドリフト フロアとしきい値ガバナンスのペアのまま、`U14-4 / U14-2` はカード契約と固定分割再実行ガバナンスのペアのままです。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。このソース同期の前に、チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 07:12:56 GMT` を返し、チェックされた本文には依然として `2026-04-04 14:10 JST` の文言がチェックされた 5 ページすべてにわたって表示されていました。
- 公式窓口のスポットチェックでは、実際的な橋は依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として `2026-04-09` 到着必須の側道、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` として表示されます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`JSM=0`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。フロント ドアと `U13-2` 行パケットを同じ境界付き `17:07 JST` ベースに合わせて調整しながら、一度に 1 つの RQ ずつ同じバッチを最新のプルされたヘッドに搬送するだけです。

## 2026 年 4 月 4 日の 14:10 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@cafeab4bc2a5`、`EEG-DATA@e0695bcac83d`、および `auto-research-funds@a4852d89376c` の後の `2026-04-04 14:10 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- プルされた最新のデルタは、ルート置換ではなく引き続き引き継がれます。`mind-upload` は、ルートを広げることなく、初期の EEG 基礎モデルのソースステータス分割に加えて、用語集の興奮性とイオン用語を強化します。`EEG-DATA` は、`30,930` マージされた一意の行、`28,893` 高信頼行、`24,909` 即時行を維持しながら、`neuroTUM Cybathlon`、`Zenodo TSA v7.8`、`poetry EEG` メタデータを深めます。 `24,539` は信頼性の高い即時行、`auto-research-funds` は実際の候補リストを置き換えることなく `JELA Diakonia` 奨学金カードを追加します。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- 3 つのスタックの読み取りも、一般的ではなく明示的なままです。`U13-2 / U13-5` は音声側制御と転送ギャップのペアのまま、`U0-2 / U0-3` はアイデンティティ ドリフト フロアとしきい値ガバナンスのペアのまま、`U14-4 / U14-2` はカード契約と固定分割再実行ガバナンスのペアのままです。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および現在の 6 行パケットに対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 04:18:04 GMT` を返し、チェックされたボディは `issue / brief / bridge / playbook` で `2026-04-04 12:02 JST` の文言を表示しますが、古い現在の 6 行パケットはこのソース同期の前に `2026-04-04 09:05 JST` の文言を表示します。
- 公式の窓口スポットチェックは依然として実際の橋の幅を狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 必ず到着する側ルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。フロント ドア、プレイブック、および現在の 6 行パケット全体を同じ境界付き `14:10 JST` ベースに調整しながら、一度に 1 つの RQ バッチを最新のプルされたヘッドに搬送するだけです。

## 2026 年 4 月 4 日の 12:02 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@f84f6e53753b`、`EEG-DATA@017ae806c4dd`、および `auto-research-funds@d4024a5b8a1a` の後の `2026-04-04 12:02 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、ルート置換ではなく引き続き繰り越しされます。`mind-upload` は、ルートを拡大することなくパブリック ページ全体で EEG 記録フレーム コントラクトを同期し、`EEG-DATA` は、マージされた固有の行、`28,892` 高信頼性の行、`24,908` 即時行、および `24,538` の高信頼性即時行を維持しながら、EEG データセットの移動容量を詳細に調べます。 `auto-research-funds` は、実質的な最終候補リストを置き換えることなく、以前の `11:04 JST` 資金調達に関する追加条項を引き続き継承しているだけです。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 02:19:09 GMT` を返し、チェックされたボディは、このソース同期の前に `issue / brief / bridge / playbook` で `2026-04-04 11:04 JST` の文言がすでに表示されていましたが、`u13-2-brain-minus-prior-route.html` ではまだ `2026-04-04 09:05 JST` の文言が表示されていました。
- 公式の窓口スポットチェックは依然として実際の橋の幅を狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 必ず到着する側ルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。フロント ドア、プレイブック、および最初の行パケットを同じ境界付き `12:02 JST` ベースに調整しながら、一度に 1 つの RQ バッチを最新のプルされたヘッドに搬送するだけです。

## 2026 年 4 月 4 日の 11:04 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@812e1650bae1`、`EEG-DATA@1deac45c75a2`、および `auto-research-funds@9741ee45a025` の後の `2026-04-04 11:04 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 取得された最新のデルタは、ルート置換ではなく引き続き引き継がれます。`mind-upload` は、ルートを広げることなく、用語集のブリッジ監視の用語を厳格化します。`EEG-DATA` は、重複する EEG-fMRI オーバーライド行を縮小し、`30,929` マージされた一意の行、`28,892` 高信頼行、`24,908` 即時行、および `24,538` 高信頼即時行を保持する一方で、現在の `D10 / D03 / D02 / D01` ファミリは変更されません。 `auto-research-funds` は、実用的な候補リストを置き換えることなく、現在のサイクルのファンディング カードに従来の補償範囲を追加します。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および `u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Sat, 04 Apr 2026 01:14:45 GMT` を返すようになりましたが、チェックされたボディには、このソース同期の前に `2026-04-04 09:05 JST` の文言が依然として表示されていました。
- 公式の窓口スポットチェックは依然として実際の橋の幅を狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 必ず到着する側ルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。制限された `11:04 JST` フロントドアとプレイブックの同期を追加しながら、一度に 1 つの RQ ずつ同じバッチを最新のプルされたヘッドに伝送するだけです。

## 2026 年 4 月 4 日の 09:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@e571567f017d`、`EEG-DATA@fbbb0d8c01e0`、および `auto-research-funds@d7f6fb9bc158` の後の `2026-04-04 09:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 取得された最新のデルタは、ルート置換ではなく、依然として引き継がれます。`mind-upload` は、最近の事前トレーニング オーバーラップ監査に加えて以前の `08:07 JST` ルートホールド同期を保持するだけです。`EEG-DATA` は、`30,929` マージされた一意の行、`28,892` 高信頼行、`24,909` 即時行、および `24,539` 高信頼即時行を引き続き保持しますが、`OpenNeuro ds007020` を制限された残りの側のサポート ノートとして扱い、保持します。 `HeartBEAM` に加えて、バックアップ ファミリーとしてのみ `EEG at rest and with TMS` を共有し、`auto-research-funds` は、実質的な候補リストを置き換えることなく、`JGC-S` を隣接する滑走路としてのみ維持しながら、徹底的に検討された 4 月 4 日の奨学金の更新を追加します。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および現在の 6 行パケットに対して `HTTP/2 200` が返されました。チェックされたフロントドアのヘッダーは `Last-Modified: Fri, 03 Apr 2026 23:18:55 GMT` を返し、チェックされたボディにはすでに `2026-04-04 08:07 JST` の文言が表示されています。現在の 6 行のパケットは `Last-Modified: Sat, 04 Apr 2026 00:11:41 GMT` を返しましたが、このソース同期の前に `2026-04-04 01:04 JST` の文言が依然として表面化していました。
- 公式の窓口スポットチェックは依然として実際の橋の幅を狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 必ず到着する側ルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。現在の 6 行パケットをすでにパブリッシュされたフロント ドアに位置合わせしながら、一度に 1 つの RQ ずつ同じバッチを最新のプルされたヘッドに搬送するだけです。

## 2026 年 4 月 4 日の 08:07 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@418c8f5d0ef9`、`EEG-DATA@dc6d833b83e9`、および `auto-research-funds@58d8738be5d5` の後の `2026-04-04 08:07 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- プルされた最新のデルタは、ルート置換ではなく引き続き引き継がれます。`mind-upload` は、フロントドアの人間プロキシ比較を強化し、`EEG-DATA` は、`30,929` マージされた一意の行、`28,892` 高信頼行、`24,909` 即時行、および `24,539` 高信頼即時行を維持しながら、`HeartBEAM` と figshare `EEG at rest and with TMS` をバックアップ ファミリとしてのみ昇格し、`auto-research-funds` は、`JGC-S` 留学生を追加します。実際の最終候補者リストを置き換えることなく、隣接する滑走路としてのみ奨学金が与えられます。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、`u13-5-perception-to-recall-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Fri, 03 Apr 2026 22:10:18 GMT` を返すようになり、チェックされたボディにはこのソース同期の前に `2026-04-04 01:04 JST` の文言が表示され続けました。
- 公式の窓口スポットチェックは依然として実際の橋の幅を狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` は依然として毎年恒例の `mid-January to early-April` 窓口として読み取られ、引き続き `2026-04-09` 必ず到着する側ルート、`Nakatani Foundation research grant = closed / next-cycle watch`、および `Secom General Research Grant = closed (2026-03-31 12:00 JST)` として扱われます。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`、`Doumei=0`、`Kenkyu no Susume=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。それは、一度に 1 つの同じ RQ バッチを、最新のプルされたヘッド、新しく強化された `HeartBEAM` / TMS バックアップ ノート、隣接する滑走路の `JGC-S` ノーオペ判定、および新しいライブ パブリック ヘッダーにのみ搬送します。

## 2026 年 4 月 4 日の 01:04 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@9b6a8b971ba0`、`EEG-DATA@56d765da60b`、および `auto-research-funds@3c8569e28` の後の `2026-04-04 01:04 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- プルされた最新のデルタは、ルート置換ではなく引き続き繰り越されます。`mind-upload` は、初期の `00:06 JST` ルート再読み取りとフィールド レベルのアーティファクト スタック開示の厳格化を実行するようになり、`EEG-DATA` は、`30,921` マージされた一意の行、`28,884` 高信頼性行、`24,900` 即時行、および `24,530` 高信頼性即時行を維持しながら、`Numbers` および `PRIOS` のパブリック OpenNeuro メタデータを強化します。 `auto-research-funds` は、実用的な候補リストを変更することなく、`同盟育成会` および `研究のすゝめ奨学金` の現在のカバレッジを追加します。
- したがって、ルートセーフ アクセスの文言は依然として変更されていません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、`u13-5-perception-to-recall-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Fri, 03 Apr 2026 15:13:06 GMT` を返し、チェックされたボディにはこのソース同期の前に `2026-04-04 00:06 JST` の文言が依然として表示されていました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`、`同盟会=0`、`研究のすゝめ=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。実際に最新にプルされたヘッド、現在のライブボディ、公式ウィンドウ、および Todoist の十分性チェックに同じ 1 つの RQ を一度に実行するだけです。

## 2026 年 4 月 4 日の 00:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@84d84fb5a82d`、`EEG-DATA@b468ecc5f8c0`、および `auto-research-funds@eccee095a939` の後の `2026-04-04 00:06 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、ルート置換ではなく引き続きキャリーフォワードです。`mind-upload` は以前の `23:06 JST` ルート再読み込み追加を保持するだけで、`EEG-DATA` は `fast mapping semantic integration EEG dataset` を追加する一方、`summary.json` は `30,921` マージされた一意の行、`28,884` 高信頼行、`24,900` 即時行、および `24,530` 高信頼即時行を報告し、`auto-research-funds` は実質的な候補リストを置き換えることなく `Iizuka current card and Korean legacy sync` を追加します。
- したがって、ルートセーフ アクセスの文言は依然として変更されません。`D10` は現在の 6 つの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は引き続きゲート サポート プランニング アンカーであり、次のウォッチ ファミリは依然として `D11 / D08 / D05 / D20` のままです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、`u13-2-brain-minus-prior-route.html`、`u13-5-perception-to-recall-route.html` に対して `HTTP/2 200` が返されました。チェックされたボディは、新しいキューやクレームではなく、依然として `brief / bridge / U13-2` 上で `22:04 JST`、`issue` 上で `22:04/22:05 JST` として浮上しました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。一度に 1 つの RQ バッチを実際の最新のプルヘッド、ライブの公共団体、公式ウィンドウ、および Todoist の十分性チェックに運ぶだけです。

## 2026 年 4 月 3 日の 23:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@ec7a7dd713e9`、`EEG-DATA@46f6b56c693c`、および `auto-research-funds@b3d3c531729a` の後の `2026-04-03 23:06 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- プルされた最新のデルタは、ルート置換ではなく引き続き転送されます。`mind-upload` は以前の `22:04 JST` ルート ホールド同期をそのまま保持し、`EEG-DATA` は `motion sickness` および `swallowing EEG` データセットを追加します。一方、`summary.json` は、`30,920` マージされた一意の行、`28,883` 高信頼性行、`24,899` 即時行、および `24,529` 高信頼性即時行を報告し、`auto-research-funds` は深化されます。 `KIRII / Pigeon / Nakato / Takashima` 奨学金の対象範囲に加えて、実質的な最終候補リストを置き換えることなく、`22:04 JST` 資金に関する追加条項を追加します。
- したがって、ルート セーフ アクセスの文言は依然として変更されていません。`D10` は現在の 6 つのルートの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないためです。
- このソース同期の前のブラウザ レベルのライブ チェックでは、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`mind-upload-eeg-rq60-grant-dataset-playbook.html`、および現在の 6 行パケットに対して `HTTP/2 200` が返されました。これらのチェックされたページは `Last-Modified: Fri, 03 Apr 2026 13:18:48 GMT` を返し、フロントドア ページと `U13-2` はすでに `22:04 JST` を表しており、他の 5 行のパケットはまだこのソース同期の前の初期の `2026-04-02 / 23:08 JST` ホールド ノートを表しています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Nakatani Foundation research grant = closed / next-cycle watch`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=206`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 3 日の 22:04 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@1ab35b64796f3936e525befb5d9428d789a16263`、`EEG-DATA@be3d03d1c286dcd37fb056317a693e47c39f7f3a`、および `auto-research-funds@845e6849a6c36e6e83394e32cf8dc4b5fe6fdc07` の後の `2026-04-03 22:04 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは現在、`EEG-DATA` に集中しています。`summary.json` は、最新の完全リフレッシュ後に、`30,918` マージされた固有行、`28,881` 高信頼性行、`24,898` 即時行、および `24,528` 高信頼性即時行を報告します。一方、`mind-upload` と `auto-research-funds` は、実質的な候補リストを置き換えることなく、以前の `21:05 JST` 追加をそのまま引き継ぎます。
- したがって、ルート セーフ アクセスの文言は依然として変更されていません。`D10` は現在の 6 つのルートの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないためです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらのチェックされたページは `Last-Modified: Fri, 03 Apr 2026 12:24:26 GMT` を返し、ルートに面した本文の文言はすでに `21:05 JST` として `issue / brief / bridge` に表示されていますが、`U13-2` は依然として `21:05 JST` および `11:07 JST` に表示されています。
- 公式のウィンドウスポットチェックは依然として実用的なブリッジを狭めています：`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、および残りの時計/閉じた読み取り値は`21:05 JST`の再読み取りから変更されていません。
- 新しい読み取り専用 Todoist 監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`Keio graduate scholarship=2`、`G-7=1`、`ENEOS=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 3 日の 21:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@3db1aa653b74d164c3a57b75677e345ea10356e0`、`EEG-DATA@c10c95274ecf1397768eb28de48aac8ce925c22d`、および `auto-research-funds@4a67e06b530bc742521f80fa5b13ccbe1115ebb9` の後の `2026-04-03 21:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- プルされた最新のデルタは、ルート置換ではなく引き続きキャリーフォワードです。`mind-upload` は `20:05 JST` ルートホールドの追加のみを保持し、`EEG-DATA` は、不足している EEG データセットに対する BDSP 手動ディープ ダイブを追加すると同時に、`30,914` マージされた一意の行、`28,877` 高信頼行、`24,896` 即時行、および `24,526` 高信頼即時行をレポートし、`auto-research-funds` は `20:05 JST` のみを保持するようになりました。実質的な最終候補リストを置き換えることなく、追加の資金調達を行うことができます。
- ルート セーフ アクセスの文言も変更されません。`D10` は現在の 6 つのルートの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないためです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらのチェックされたページは `Last-Modified: Fri, 03 Apr 2026 11:17:44 GMT` を返し、そのルートに面した本文の文言は、`20:05 JST` の以前の `issue / brief / bridge` の保留メモをすでに表面化していますが、`U13-2` は依然として `11:07 JST` を表面化しています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)`、`Nakatani Foundation research grant = closed / next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Nakatani family=11`、`G-7=1`、`ENEOS=0`、`Keio graduate scholarship=2`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 3 日の 20:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@b4fd73d9e98301c918b57541704a95246d69ae09`、`EEG-DATA@649ff098ab577f11065562379150acea1aa07002`、および `auto-research-funds@7c1b835d1d138214f282dc85d2f06d9faa522310` の後の `2026-04-03 20:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、アクティブなバッチを広げるのではなく、依然としてサポートスペースを深めています。`mind-upload` は、現在の 6 つ以外の人体熱証拠を `passive / task-linked macro thermometry` と `perturbation-conditioned thermal routes` に分割し、`EEG-DATA` は、制限付きの `Transcranial Magnetic Stimulation in Alzheimer's disease-Data` BDSP の詳細を追加すると同時に、`30,912` マージされた固有行、`28,875` 高信頼行、および `24,894` 直接使用可能な行を報告します。また、`auto-research-funds` は、`ENEOS` と `ENEOS` の現在のカードのカバレッジを完了します。 `G-7` 奨学金は、実用的な最終候補リストを置き換えることなく、`8,600` 援助 ID、`4,308` 行、および `3,959` 公式ソース行を報告するようになりました。
- ルート セーフ アクセスの文言も変更されません。`D10` は現在の 6 つのルートの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないためです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらのチェックされたページは `Last-Modified: Fri, 03 Apr 2026 10:19:46 GMT` を返しましたが、ルートに面した本文の文言には、以前の `11:05/11:07 JST` 保留メモが依然として現れていました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)`、`Nakatani Foundation research grant = closed / next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 3 日の 11:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@f70432e4a6c8a52afafbc57b98c8f0e360c85d4e`、`EEG-DATA@1981d34c5f71deceb2549684db9173b6f54d2b89`、および `auto-research-funds@bfebe94da875d709756746285f133ef30905fd38` の後の `2026-04-03 11:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、アクティブなバッチを広げるのではなく、依然としてサポートスペースを狭めています。`mind-upload` は、現在の 6 つ以外の `sleep replay integrity / physiology-gate` の文言を強化し、`EEG-DATA` はインベントリを更新して `COG-BCI` ファミリを詳細に調べながら、`30,904` マージされた一意の行、`28,867` 高信頼行、および `24,890` 直接使用可能な行を報告します。また、`auto-research-funds` は、`10:06 JST mind-upload funding addendum` を引き継ぎながら、`8,596` 支援 ID を報告します。実質的な候補リストを置き換えることなく、`4,308` 行と `3,958` 公式ソース行。
- ルート セーフ アクセスの文言も変更されません。`D10` は現在の 6 つのルートの中で唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` はゲート サポート プランニング アンカーのままです。これは、これら 3 つのルートを直接のパブリック アンカーに変える最新のプル ヘッドがないためです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。これらのチェックされたページは `Last-Modified: Fri, 03 Apr 2026 01:31:28 GMT` を返しましたが、ルートに面した本文の文言には、以前の `05:12 JST` 保留メモが依然として現れていました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Secom General Research Grant = closed (2026-03-31 12:00 JST)`、`Nakatani Foundation research grant = closed / next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 3 日の 05:12 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@a9fc5d1cb691f3669c40803604e78cf87fab4eed`、`EEG-DATA@8c3ace28bad0b3bac259caa440994e5d05bfc7d1`、および `auto-research-funds@35756f8381c47daa24bb70bb7a1ff88d1dcf76bc` の後の `2026-04-03 05:12 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、アクティブなバッチを広げるのではなく、依然としてサポート スペースを狭めています。`mind-upload` は現在、アクティブ キューを変更せずにエクスポートされたルート ミラーの位置合わせを維持する `docs: sync github wiki export` ヘッドにあり、`EEG-DATA` は、`30,900` マージされた一意の行、`28,863` の高信頼行、および `24,885` 直接使用可能な行を維持しながら、最近の `EESM17` メタデータの深化に加えて `VR navigation dataset` 出力の更新を繰り越し、`auto-research-funds` は追加します。最近の `JSSF research publication` リフレッシュに加えて、`JSPS overseas fellow` の現在のカードのスナップショットが追加され、実際の候補リストを置き換えることなく、`8,594` 補助 ID、`4,307` 行、および `3,957` 公式ソース行がレポートされるようになりました。
- したがって、ルートセーフアクセスの読み取り値は依然として狭いままです。最新のプルヘッドが`D03 / D02 / D01`を即時パブリックアンカーに変えることはないため、パブリックセーフの文言は依然として`D10`を唯一の明確なパブリックオープンプライマリアンカーとして維持し、`D03 / D02 / D01`をゲートサポートプランニングアンカーとして維持します。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Thu, 02 Apr 2026 19:17:56 GMT` を返すようになりましたが、チェックされたボディは、このソース同期前の以前の `04:05/04:06 JST` ホールド ノートを依然として表示しています。
- この実行での公式ウィンドウスポットチェックでは、実際のブリッジは依然として狭いままです。`Kura Fund` は開いたまま (`2026-02-02 - 2026-04-17 17:00`)、`Nakatani Foundation graduate scholarship` は開いたまま (`2026-04-01 - 2026-05-25 15:00`)、`Kashinome Scholarship` は学生滑走路側ルートのまま (`2026-01-14 - 2026-04-09 must arrive`)、`Nakatani Foundation research grant` は閉じたまま/次サイクル監視 (現在の公開ページの `募集を終了しました`)、`Secom General Research Grant` は現在のサイクルでは閉じたままです (`2026-03-31 12:00 JST`)。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 3 日の 04:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@f5e13ebdc4748ce683d905c37cabfdb3c53036bb`、`EEG-DATA@53f5c8166faf0d5fcebfb5c39741d4992eb82a39`、および `auto-research-funds@1f190fec93a9180a27443b1fe2b31f9488dfbf74` の後の `2026-04-03 04:06 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、アクティブなバッチを広げるのではなく、依然としてサポート スペースを狭めています。`mind-upload` は、現在の 6 つ以外の `BCSFB / human-proxy composition` 文献同期を引き継ぎ、`EEG-DATA` は、現在のアンカー ファミリを置き換えないカタログ更新後に `30,900` マージされた一意の行、`28,863` の信頼性の高い行、および `24,885` 直接使用可能な行を保持し、`auto-research-funds` は、`8,593` 支援を報告しながら、`Itoh domestic scholarship` の周りの現在のカードおよびレジストリ レイヤーを更新します。実際の候補リストを置き換えることなく、ID、`4,306` 行、および `3,956` 公式ソース行。
- したがって、ルートセーフアクセスの読み取り値は依然として狭いままです。最新のプルヘッドが`D03 / D02 / D01`を即時パブリックアンカーに変えることはないため、パブリックセーフの文言は依然として`D10`を唯一の明確なパブリックオープンプライマリアンカーとして維持し、`D03 / D02 / D01`をゲートサポートプランニングアンカーとして維持します。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Thu, 02 Apr 2026 18:14:39 GMT` を返すようになりました。
- この実行での公式ウィンドウスポットチェックでは、実際のブリッジは依然として狭いままです。`Kura Fund` は開いたまま (`2026-02-02 - 2026-04-17 17:00`)、`Nakatani Foundation graduate scholarship` は開いたまま (`2026-04-01 - 2026-05-25 15:00`)、`Kashinome Scholarship` は学生滑走路側ルートのまま (`2026-01-14 - 2026-04-09 must arrive`)、`Nakatani Foundation research grant` は閉じたまま/次サイクル監視 (現在の公開ページの `募集を終了しました`)、`Secom General Research Grant` は現在のサイクルでは閉じたままです (`2026-03-31 12:00 JST`)。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- したがって、行に面した最初の成果物 (`U13-2 = brain-minus-prior control table`、`U13-5 = perception-to-recall degradation note`、`U0-2 = offset/jitter + state-feature collapse audit`、`U0-3 = threshold-stability note + overfit-exclusion rule`、`U14-4 = filled Model Card / Dataset Card examples`、`U14-2 = fixed-split rerun contract + negative-case trail`) は変わりません。

## 2026 年 4 月 2 日の 23:08 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@f5d1d1dd1683`、`EEG-DATA@ee1463d28288`、および `auto-research-funds@ec24a355abbc` の後の `2026-04-02 23:08 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、アクティブなクレーム サーフェスではなく、ルート規律とサポート スペースをさらに深めています。`mind-upload` は、現在の 6 つ以外の因果対人間プロキシ ブリッジとローカル ルート/プロキシの境界を明確にし、`EEG-DATA` は EEG 候補のキュレーションを改良し、`OpenNeuro ds007615` を追加すると同時に、現在の README で `30,896` マージされた一意の行、`28,859` の高信頼行、および `24,882` の直接使用可能な行を報告します。スナップショット、`auto-research-funds` は `Geo-Kagaku` の現在のカードに加えて、実質的な候補リストを置き換えることなく README 統計を更新します。
- したがって、ルートセーフアクセスの読み取り値は依然として狭いままです。最新のプルヘッドが`D03 / D02 / D01`を即時パブリックアンカーに変えることはないため、パブリックセーフの文言は依然として`D10`を唯一の明確なパブリックオープンプライマリアンカーとして維持し、`D03 / D02 / D01`をゲートサポートプランニングアンカーとして維持します。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u13-2-brain-minus-prior-route.html` に対して `HTTP/2 200` が返されました。チェックされたヘッダーは `Last-Modified: Thu, 02 Apr 2026 13:12:21 GMT` を返すようになりました。
- この実行での公式ウィンドウ スポット チェックでは、依然として実質的なブリッジが狭いままです。`Kura Fund` はオープンのまま (`2026-02-02 - 2026-04-17 17:00`)、`Nakatani Foundation graduate scholarship` はオープンのまま (`2026-04-01 - 2026-05-25 15:00`)、`Nakatani Foundation research grant` はクローズされたまま/次のサイクル監視 (`募集期間 2025-06-01 - 2025-07-07`)、そして `Secom General Research Grant` は現在のサイクルではクローズされたままです (`2026-03-31 12:00 JST`)。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` 監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。一度に 1 つの同じ RQ バッチを、最新のプルされたヘッド、ライブ パブリック ヘッダー、公式ウィンドウ、および Todoist の十分性チェックに転送するだけです。

## 2026 年 4 月 2 日の 19:03 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@e1a7e7e2f22c`、`EEG-DATA@a7f9390492fd`、および `auto-research-funds@00cdbaa9a122` の後の `2026-04-02 19:03 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに深めます。`mind-upload` は、現在の 6 つ以外の人間の神経血管ページでの `blood-CSF barrier / choroid-plexus` ルート分割を深め、`EEG-DATA` は、現在の README スナップショットで `30,892` マージされた一意の行、`28,855` 高信頼行、および `24,880` 直接使用可能な行を引き続き報告し、`auto-research-funds` は、`8,590` エイド ID、`4,301` 行で最新の概要を維持します。実用的な候補リストを置き換えることなく、`3,951` 公式ソースの行を追加します。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。直接ライブアクセスで再読み込みすると、これら 3 つのサポート アンカーの現在の `IEEE DataPort` ページに `Subscription Required` と `LOGIN TO ACCESS DATASET FILES` が表示されます。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u7-2-timing-metric-route.html` に対して `HTTP/2 200` が返されました。チェックされたページは `Last-Modified: Thu, 02 Apr 2026 09:37:54 GMT` を返しましたが、ルートに面した本文の文言は依然として以前の `18:06 JST` 保留メモを表面化させました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Secom General Research Grant = closed (March 31, 2026 at 12:00 JST)`、`Nakatani Foundation research grant = closed / next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。ルートホールドの文言を最新のプルされたヘッドに更新しながら、一度に 1 つの RQ バッチを最新のリポジトリ ヘッド、ライブ パブリック ヘッダー、公式ウィンドウ、および Todoist 十分性チェックに転送するだけです。

## 2026 年 4 月 2 日の 18:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@85b6603b569b`、`EEG-DATA@a7f9390492fd`、および `auto-research-funds@b6c0d0f4eeb7` の後の `2026-04-02 18:06 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化します。`mind-upload` は `U7-2` パブリック ブリッジの文言のみを同期し、`EEG-DATA` は `OSF gazx2` 信頼性 EEG メタデータと `OpenNeuro ds007081` を詳細に調べ、同時に `30,892` マージされた一意の行、`28,855` 高信頼行、および `24,880` 直接使用可能な行を現在の README スナップショットに報告し、`auto-research-funds` は README の概要を次のように更新します。実際の候補リストを置き換えることなく、`8,590` 援助 ID、`4,301` 行、および `3,951` 公式ソース行。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。直接ライブアクセスで再読み込みすると、これら 3 つのサポート アンカーの現在の `IEEE DataPort` ページに `Subscription Required` と `LOGIN TO ACCESS DATASET FILES` が表示されます。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u7-2-timing-metric-route.html` に対して `HTTP/2 200` が返されました。チェックされたページは `Last-Modified: Thu, 02 Apr 2026 08:22:50 GMT` を返しました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09 (must arrive)`、`Secom General Research Grant = closed (March 31, 2026 at 12:00 JST)`、`Nakatani Foundation research grant = closed / next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、現在のパブリック 6 を**拡大することはありません**。一度に 1 つの RQ バッチを最新のリポジトリ ヘッド、ライブ パブリック ヘッダー、公式ウィンドウ、および Todoist 十分性チェックに転送するだけです。

## 2026 年 4 月 2 日の 11:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@208e59e2180c`、`EEG-DATA@00d85380f3fd`、および `auto-research-funds@f4ba35518400` の後の `2026-04-02 11:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化します。`mind-upload` は 10:07 ルートホールド パケットを更新し、`EEG-DATA` は維持されている `ChineseEEG-2` リリースとパブリック `auditory-eeg` ファミリを詳細に調べながら、`30,887` マージされた一意の行、`28,850` 高信頼行、および `24,875` すぐに使用可能な行を引き続き報告し、`auto-research-funds` は同じ実用的な候補リストを維持します。新しいスピーチ側の公開資料は、`U13-2/U13-5` のバックアップの読み取り/聴取調整チェックを強化しますが、主要なアンカーとして `D10` を置き換えたり、`U13-5` の下での再現と妥当性のギャップを修復したりするものではありません。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。直接ライブアクセスで再読み込みすると、これら 3 つのサポート アンカーの現在の `IEEE DataPort` ページに `Subscription Required` と `LOGIN TO ACCESS DATASET FILES` が表示されます。
- この実行のブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックされたページは `Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT` を返しました。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant = closed (March 31, 2026 at 12:00 JST)`、`Nakatani Foundation research grant = next-cycle watch` という実際的なブリッジは依然として狭いままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、ルートホールドの文言と音声側のサポートの読み取りのみを更新します。現在の請求対象範囲が広がるわけではありません。

## 2026 年 4 月 2 日の 11:09 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@208e59e2180c`、`EEG-DATA@00d85380f3f`、および `auto-research-funds@f4ba35518400` の後の `2026-04-02 11:09 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 現在の `mind-upload` ヘッドは、以前の 10:07 ルートホールド パケット リフレッシュ自体であり、最新のアップストリーム移動は `EEG-DATA`: `chore: deep-dive ChineseEEG-2 and PhysioNet auditory EEG` 上にあります。更新された概要では、引き続き `30,887` マージされた固有の行、`28,850` の高信頼行、および `24,875` 直接使用可能な行が報告され、`auto-research-funds` は同じ実用的な候補リストを保持しますが、リポジトリの統計には `8,585` 支援 ID、`4,293` 行、および `3,943` 公式ソース行が引き続き表示されます。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。
- 新しいパブリックオープン付属物は、バッチを拡大するのではなく、行固有のバックアップ カバレッジを強化するだけです。`ds007591` と `ds007602` は、`U13-2` の音声側バックアップ オプションを強化しますが、公開された参加者はそれぞれ 3 人だけです。`ChineseEEG-2` は、`U13-5` のパブリック リーディング/リスニング アラインメント カバレッジを強化しますが、意図したリコール ラベル付きブランチは依然として公開しません。また、PhysioNet `auditory-eeg` は明らかにパブリック オープンですが、代替ではなく 1 日 4 チャネル カバレッジのままです。 `U0-2 / U0-3`の中の`D02`。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックされたページは `Last-Modified: Thu, 02 Apr 2026 01:22:44 GMT` を返すようになりました。
- 公式のウィンドウスポットチェックは依然として現実的な橋渡しを狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` の公式ページは依然として年次 `mid-January to early-April` ウィンドウとして表示され、`Secom General Research Grant` は依然として現在のサイクルが終了した (`March 31, 2026 at 12:00 JST`) と表示されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、最新の `EEG-DATA` キャリーフォワードの後に​​、ルート ホールドの文言とバックアップ ファミリの読み取り値のみを更新します。現在の請求対象範囲が広がるわけではありません。

## 2026 年 4 月 2 日の 10:07 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@be507c810b11`、`EEG-DATA@3f20f48cca6e`、および `auto-research-funds@fb32c05163f4` の後の `2026-04-02 10:07 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化します。`mind-upload` は、現在の 6 つ以外の EEG 基礎設定と同等の境界を洗練し、`EEG-DATA` は HBN EEG リリース 11 ルートを詳細に調査し、`30,887` マージされた固有の行、`28,850` 高信頼行、および `24,871` 直接使用可能な行をレポートします。また、`auto-research-funds` は、リポジトリ統計がまだ読み込まれている間、同じ実用的な候補リストを保持します。 `8,585` 援助 ID、`4,293` 行、および `3,943` 公式ソース行。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。行レベルの読み取りは、変更されていないバッチ内でのみ強化されます。`U13-5` には、目に見える `D03` メタデータが依然としてリコール固有のラベルを公開していないため、明示的なリコール有効性の警告が依然として含まれており、`U14-4 / U14-2` は、`D13` を現在の `D01` 公開フロアを超えて最初の公開再実行サポート ファミリとして維持しています。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックしたページでも `Last-Modified: Thu, 02 Apr 2026 00:15:06 GMT` が返されました。
- このソース同期により、パブリック側の行の文言と資金提供側の `60RQ` ドシエの文言も同じ `Dxx + DOI + dataset name + access class` 標準に再調整されるため、パブリック 6 は再び資金調達リポジトリと同じ正規の行パケットを指すようになります。
- 公式のウィンドウスポットチェックは依然として現実的な橋渡しを狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` の公式ページは依然として年次 `mid-January to early-April` ウィンドウとして表示され、`Secom General Research Grant` は依然として現在のサイクルが終了した (`March 31, 2026 at 12:00 JST`) と表示されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、パブリック エントリ ページ上のルート ホールドの文言と行ごとのドシエの文言のみを更新します。現在の請求対象範囲が広がるわけではありません。

## 2026 年 4 月 2 日の 09:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@d7f30648fc40`、`EEG-DATA@ac8cc6fc8e74`、および `auto-research-funds@31ec17305f6a` の後の `2026-04-02 09:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化します。`mind-upload` は、現在の 6 つ以外の文献ミエリン ルート分割を強化し、`EEG-DATA` は `aw8sz` の詳細を追加し、`merged_unique=30886`、`high_confidence=28849`、および `access_counts_high.immediate=24500` をレポートするようになりました。`auto-research-funds` は、`Aoi graduate scholarship` / `JSSF research grant` のマージに加えて、`8,585` エイド ID、`4,293` 行、および実質的な候補リストを変更せずに、`3,943` 公式ソースの行を追加します。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。直接のライブアクセスの再読み取りでは、依然として `D03 / D02 / D01` が `IEEE DataPort` ログインおよびサブスクリプション ゲートの背後に表示されます。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックされたページも `Last-Modified: Wed, 01 Apr 2026 23:29:12 GMT` を返し、ライブ ページには、このソース更新前の以前の `04:09 JST` / `03:08 JST` 再読メモがまだ表示されていました。
- 公式のウィンドウスポットチェックは依然として現実的な橋渡しを狭めています。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship` の公式ページは依然として年次 `mid-January to early-April` ウィンドウとして表示され、`Secom General Research Grant` は依然として現在のサイクルが終了した (`March 31, 2026 at 12:00 JST`) と表示されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、パブリック エントリ ページ上のルートホールドの文言のみを更新します。現在の請求対象範囲が広がるわけではありません。

## 2026 年 4 月 2 日の 03:08 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@d391dbede29e`、`EEG-DATA@f9df9ba85a6`、および `auto-research-funds@95f804055809` の後の `2026-04-02 03:08 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在のクレームサーフェスではなくルートサポートをさらに強化しています。`mind-upload`は、現在の6つの外側にECM / PNN文献ルートを分割し、`EEG-DATA`は、現在のアンカーファミリーを置き換えることなく、2つの即時アクセスの詳細な候補（`10.48804/NV4RGL`と`10.7281/T1/B660D2`）を追加し、`auto-research-funds`は、実質的な候補リストを変更することなく、Gakusho / NII資金のマージとREADME統計の更新を追加します。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックされたページでも `Last-Modified: Wed, 01 Apr 2026 17:27:08 GMT` が返され、ライブ ルートの順序では依然として同じ順序で同じ 6 つの名前が付けられていました。
- 公式のウィンドウスポットチェックでは、実際的なブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。
- このソース同期は、パブリック エントリ ページ上のルートホールドの文言のみを更新します。現在の請求対象範囲が広がるわけではありません。

## 2026 年 4 月 2 日の 00:03 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@cff3abab58e8`、`EEG-DATA@a885ef3f029d`、および `auto-research-funds@0f60872538dc` の後の `2026-04-02 00:03 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在のクレームサーフェスではなくルートサポートをさらに強化しています。`mind-upload`は、現在の6つ以外の重水素動作点の文言を厳格化し、`EEG-DATA`は`DANDI 001187`の詳細を追加し、`merged_unique=30875`、`high_confidence=28838`、および`access_counts_high.immediate=24492`を報告するようになり、`auto-research-funds`は実質的な候補リストを変更せずに`Isono / Okabe`奨学金の更新を繰り越します。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックされたページでも `Last-Modified: Wed, 01 Apr 2026 14:17:54 GMT` が返され、ライブ ルートの順序では依然として同じ順序で同じ 6 つの名前が付けられていました。
- 公式のウィンドウスポットチェックでは、実際的なブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 22:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@84e5337`、`EEG-DATA@bbb8d6c63d7`、および `auto-research-funds@5ff33413e` の後の `2026-04-01 22:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化します。`mind-upload` は、現在の 6 つの外側の正面玄関のクリアランス ルート ラベルを明確にし、`EEG-DATA` は、`merged_unique=30873`、`high_confidence=28836`、`access_counts_high.immediate=24487`、および `18,312 / 28,832` 実験に面した行 (`63.51%` カバレッジ) を維持しながら詳細なメタデータを更新し、`auto-research-funds` は、実質的な候補リストを変更せずに、`Yamaoka graduate scholarship` スナップショットと README に面した統計を追加します。
- ルートセーフ アクセスの読み取り値は依然として狭いままです。`D10` は依然として唯一の明確なパブリック オープン プライマリ アンカーである一方、`D03 / D02 / D01` は依然としてパブリック ワードにおけるゲート サポート アンカーのままです。
- このソース同期前のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。チェックされたページでも `Last-Modified: Wed, 01 Apr 2026 12:13:54 GMT` が返され、ライブ ルートの順序では依然として同じ順序で同じ 6 つの名前が付けられていました。
- 公式のウィンドウスポットチェックでは、実際的なブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items, projects)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`projects=2`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 18:05 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@9984d0b`、`EEG-DATA@5fc1df00f07`、および `auto-research-funds@d7092c8e9` の後の `2026-04-01 18:05 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化します。`mind-upload` は、現在の 6 つ以外のウェアラブル `OPM / MEG` ルート同期と測定スタックの明確化を強化し、`EEG-DATA` は継続的追跡 EEG BCI ディープ ダイブを追加し、`merged_unique=30873`、`high_confidence=28836`、および `access_counts_high.immediate=24486` をレポートするようになりました。その実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行を引き続きカバーします。 `auto-research-funds` は、最近の繰越奨学金の更新後も、同じ実質的な候補者リストを維持しています。
- ルート セーフ アクセスの読み取り値は依然として狭いままです。更新されたローカル `EEG-DATA` カタログは拡大を続けていますが、現在のパブリック ルートでは依然として `D10` が唯一の明確なパブリック オープン プライマリ アンカーとして読み取られ、一方で `D03 / D02 / D01` は依然としてパブリックの文言ではゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 08:22:51 GMT` であり、ライブ `issue.html` 段落では、この実行の新しい付録の前に、依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、実際のブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) では閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 17:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@c5a0550`、`EEG-DATA@82893f6ca6e`、および `auto-research-funds@ec6f7d068` の後の `2026-04-01 17:06 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに深めます。`mind-upload` は、現在の 6 つ以外のアストロ サイト PET ルート分割を深め、`EEG-DATA` は KMI EEG データセットを詳細に調査し、`merged_unique=30871`、`high_confidence=28834`、`access_counts_high.immediate=24484` をレポートするようになりました。その実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行を引き続きカバーし、`auto-research-funds` は `Megachips 2026 scholarship` スナップショット プラスを追加します。実際の候補リストを変更せずに README 統計を更新します。
- ルート セーフ アクセスの読み取り値は依然として狭いままです。更新されたローカル `EEG-DATA` カタログでは、カタログ側の即時行として `D03 / D02` が表示され、即時/チェックが必要な混合ペアとして `D01` が表示されていますが、ライブ アクセスの読み取りは依然として厳格であるため、`D10` が唯一の明確なパブリック オープン プライマリ アンカーのままである一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 07:16:09 GMT` ですが、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、実際のブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) では閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 14:09 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@ccef40f2f7cf`、`EEG-DATA@deefd5f95c6d`、および `auto-research-funds@f5f76c485ccb` の後の `2026-04-01 14:09 JST` での実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに深めています。`mind-upload` は、現在の 6 つ以外のシナプス前放出機構の上限を明確にし、`EEG-DATA` はメンデレー EEG メタデータを深め、`merged_unique=30869`、`high_confidence=28832`、`access_counts_high.immediate=24482` をレポートするようになりました。新しい実験メタデータ レポートは、少なくとも 1 つの実験に面したフィールド (`63.51%` カバレッジ) を持つ `18,312 / 28,832` 行をカバーし、`auto-research-funds` はリポレベルを更新します。実際の候補リストを変更せずに統計を作成します。
- ルート セーフ アクセスの読み取り値は依然として狭いままです。更新されたローカル `EEG-DATA` カタログでは、カタログ側の即時行として `D03 / D02` が表示され、即時/チェックが必要な混合ペアとして `D01` が表示されていますが、ライブ アクセスの読み取りは依然として厳格であるため、`D10` が唯一の明確なパブリック オープン プライマリ アンカーのままである一方、`D03 / D02 / D01` は依然としてパブリックの表現におけるゲート サポート アンカーのままです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 04:20:02 GMT` ですが、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、実際のブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) では閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=5`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 12:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@9f4bc8e760b1`、`EEG-DATA@1324f9e1ae2b`、および `auto-research-funds@6548b1650535` の後の `2026-04-01 12:06 JST` での 2 回目の実際のプル再チェックでは、パブリック バッチと解決優先順序は変更されません。
- 最新のプルデルタは、現在のクレーム面ではなくルートサポートをさらに深めています。`mind-upload`はすでにルートホールドの文言を公衆安全に保ち、`EEG-DATA`は現在`merged_unique=30867`、`high_confidence=28830`、`access_counts_high.immediate=24480`を報告し、`auto-research-funds`は実質的な候補リストを変更せずに資金再読ドキュメントを更新しています。
- ルート セーフ アクセスの読み取り値は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は依然としてゲート サポート アンカーのままです。これは、ライブ アクセスの読み取り値がカタログ ラベルよりも厳しいままであるためです。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されました。現在の `Last-Modified` ヘッダーは、これらの公開サーフェスでは `Wed, 01 Apr 2026 02:26:28 GMT` ですが、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、実際的なブリッジは依然として狭いままです。`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09`、`Secom General Research Grant` は現在のサイクルでは閉鎖されたままです。
- 今回の再読では、新しい Todoist ルートは導入されませんでした。最新の正規の資金調達候補者リストの監査では、現時点での実際的な領域がすでにカバーされており、公式の再検査では新たな現行サイクルの資金提供者は明らかにされませんでした。

## 2026 年 4 月 1 日の 11:06 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@aa21ab9855c1`、`EEG-DATA@cccd137a3468`、および `auto-research-funds@3a691196cb9f` 後の `2026-04-01 11:06 JST` での最新の実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなくルート サポートをさらに強化しています。`mind-upload` はすでにルート ホールドの文言をパブリック セーフに保ち、`EEG-DATA` はリポジトリ全体のメタデータを強化し、`merged_unique=30866`、`high_confidence=28829`、`access_counts_high.immediate=24479` をレポートするようになり、`auto-research-funds` は実質的な候補リストを変更せずにリポジトリ レベルの統計を更新します。
- ルート セーフ アクセスの読み取り値は依然として狭いままです。`D10` は唯一の明確なパブリック オープン プライマリ アンカーのままですが、`D03 / D02 / D01` は依然としてゲート サポート アンカーのままです。これは、ライブ アクセスの読み取り値がカタログ ラベルよりも厳しいままであるためです。
- ブラウザレベルのライブチェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して引き続き `200` が返されました。 `Last-Modified` は `issue.html` / `u8-1` および `Wed, 01 Apr 2026 01:21:13 GMT` の 2 つのブリッジ ページで `Wed, 01 Apr 2026 01:21:12 GMT` に進み、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクルレーンの外側で監視または閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 03:09 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@31835fcd8daa`、`EEG-DATA@12eef8ca4ef0`、および `auto-research-funds@040e5b8798fd` 後の `2026-04-01 03:09 JST` での最新の実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルされたデルタは、現在のクレーム サーフェスではなく、依然としてルート サポートを拡大しています。`mind-upload` は、現在のパブリック 6 パケットの外側に侵入する言語 BCI の一時ルートを分割し、`EEG-DATA` は、`D10 / D03 / D02 / D01` を置き換えることなく言語関連のバックアップ カバレッジを拡大するセマンティック テキスト関連性の詳細を追加し、`auto-research-funds` は、実質的な現在の候補リストを変更せずに `Obayashi / Yokogaku` カードを更新しました。
- `2026-04-01 03:09 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`mind-upload-rq-solvability-bridge.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ 6 つの名前が同じ順序で付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant` と `Secom General Research Grant` は閉鎖されたままであり、現在のサイクルレーンの外側で監視されています。
- 新しい読み取り専用 Todoist `api/v1/sync(items)` の全項目監査では、まだ十分なルート カバレッジ (`items=203`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`、`AI for Aging-Society Problem Solving=0`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 01:06 JST のライブソースの再チェック後も修正されていないもの

- ネストされた `mind-upload@8da02e2e48e0`、`EEG-DATA@e6013384fa01`、および `auto-research-funds@c6a383f07a7b` の後の `2026-04-01 01:06 JST` での 2 回目の no-op 実プル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 現在の `EEG-DATA` ヘッドは、置き換えるのではなく、同じ制限されたルートを引き続きサポートしています。現在の 6 ファミリ `D10 / D03 / D02 / D01` と外部の現在の 6 ファミリ `D11 / D08 / D05 / D20` はすべてリポジトリにまだ存在しており、ライブ アクセスの読み取りがカタログ ラベルよりも厳格であるため、パブリック セーフの文言では `D10` が唯一の明確なパブリック オープン プライマリとして維持されていますが、`D03 / D02 / D01` はゲート サポート アンカーのままです。
- `2026-04-01 01:06 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`u8-1-closed-loop-delay-tolerance-route.html`、および `mind-upload-rq-solvability-bridge.html` に対して依然として `200` が返されたため、この実行によりパブリック バッチは修正されたままになります。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクルレーンの外側で監視または閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync` の全項目監査では、まだ十分なルート カバレッジ (`items=204`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 4 月 1 日の 00:12 JST の実際のプルの再読み込み後もまだ修正されている点

- `mind-upload@e53a50b1256d`、`EEG-DATA@48f4814db5da`、および `auto-research-funds@76145d0e3f4c` 後の `2026-04-01 00:12 JST` での最新の実際のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 現在の `EEG-DATA` ヘッドは、置き換えるのではなく、同じ制限されたルートを引き続きサポートしています。現在の 6 ファミリ `D10 / D03 / D02 / D01` と外部の現在の 6 ファミリ `D11 / D08 / D05 / D20` はすべてリポジトリにまだ存在しますが、パブリック セーフの文言では、`D10` が唯一の明確なパブリック オープン プライマリとして維持され続けますが、`D03 / D02 / D01` はゲート サポート アンカーのままです。これは、ライブ アクセスの読み取りが依然としてカタログ ラベルより厳格であるためです。
- `2026-04-01 00:15 JST` でのブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されたため、この実行によりパブリック バッチは修正されたままとなり、サポートするルート ページに短い再読メモのみが追加されます。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現在のサイクルレーンの外側で監視または閉鎖されたままです。
- 新しい読み取り専用 Todoist `api/v1/sync` の全項目監査では、まだ十分なルート カバレッジ (`items=204`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 3 月 31 日の 21:09 JST ポストプル再読み込み後も修正されたままのもの

- `mind-upload@ed6f8203e46d`、`EEG-DATA@20fbbad9959f`、および `auto-research-funds@77f189662745` 後の `2026-03-31 21:09 JST` での最新のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在のパブリッククレームサーフェイスではなく、依然としてサポートを拡大しています。`mind-upload`はデータセットベンチマークオブジェクトルールを厳格化し、FAQ RNAルート分割を明確にし、`EEG-DATA`はリクエストゲート型`HBUED`感情認識カバレッジと継続的追跡オンラインBCIメタデータの詳細を追加し、`auto-research-funds`は`Teraura Sayoko outbound scholarship`、`Gakusho scholarship`、およびREADME統計の更新を追加しましたが、これらの変更はいずれも現在の`D10 / D03 / D02 / D01`ファミリーに代わるものではありません。または外部電流6次`U7-1 -> U1-2 -> U4-2 -> U8-1`。
- `2026-03-31 21:09 JST` でのブラウザレベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、`u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ順序で現在の 6 つの名前が付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実際のブリッジは依然として狭いままですが、`Nakatani Foundation research grant`、`Secom General Research Grant`、および `Brain Science Foundation research grant` は現行サイクルレーンの外側のままです。
- 新しい読み取り専用 Todoist `api/v1/sync` の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 3 月 31 日の 19:07 JST ポストプル再読み込み後も修正されたままのもの

- `mind-upload@b7b6c0498ae1`、`EEG-DATA@24e85cc20f09`、および `auto-research-funds@0fddd53bd03c` 後の `2026-03-31 19:07 JST` での最新のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在の公的な請求面よりも支持を依然として拡大しています。`mind-upload`はフロントドアの人間代理分割を強化し、`EEG-DATA`はカタログを`merged_unique=30860`、`high_confidence=28823`、`access_counts_high.immediate=24471`に更新し、`auto-research-funds`はキオクシア/高柳の資金調達記録を更新しましたが、これらの変更はいずれも、現在の`D10 / D03 / D02 / D01`ファミリーやアウトサイドカレント6オーダーの`U7-1 -> U1-2 -> U4-2 -> U8-1`に代わるものではありません。
- `2026-03-31 19:09 JST` でのブラウザレベルのライブ チェックでは、`issue.html` と `mind-upload-current-public-six-rq-brief.html` に対して依然として `200` が返され、ライブ `issue.html` 段落では依然として同じ順序で現在の 6 つの名前が付けられています。
- 公式のウィンドウスポットチェックでは、`Kura Fund = 2026-02-02 - 2026-04-17 17:00`、`Nakatani Foundation graduate scholarship = 2026-04-01 - 2026-05-25 15:00`、`Kashinome Scholarship = 2026-01-14 - 2026-04-09` という実質的なブリッジがまだ狭いままですが、`Nakatani Foundation research grant` と `Secom General Research Grant` は現在のサイクルですでに閉鎖されています。
- 新しい読み取り専用 Todoist の全項目監査では、まだ十分なルート カバレッジ (`items=205`、`Kura=2`、`Nakatani family=11`、`Nakatani graduate scholarship=7`、`Kashinome=2`、`Secom=3`、`Brain Science Foundation=8`、`Okawa=2`、`Japan Industrial Science Research Institute=1`) が示されていたため、このセッションには新しいタスクは追加されませんでした。

## 2026 年 3 月 31 日の 17:06 JST ポストプル再読み込み後も修正されたままのもの

- `mind-upload@4731680627ff`、`EEG-DATA@3e7a53d9ca8`、および `auto-research-funds@ef2924014a65` 後の `2026-03-31 17:06 JST` での最新のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新の `EEG-DATA` の追加により、現在のルートではなくサポート マップが広がります。NTU Dataverse の成人から幼児の一方向性神経結合の生/前処理済みリリースはすぐにダウンロード可能で、将来の社会学習やペア観察者の行に役立ちます。一方、OpenNeuro `ds007146` は、目に見えるパブリック オブジェクト ツリーが要求された生の EEG をまだ検証していないため、`uncertain_public` のままである大規模な聴覚 MEG/EEG/Ear-EEG 記録を追加します。 / 耳脳波の範囲。
- RQ ごとのドシエ内の `### Ux-y` 見出しを再カウントしても `60` が返されるため、この実行では行をまとめて折りたたむことによってキューが広がりません。
- ブラウザ ユーザー エージェントを使用したブラウザ レベルのライブ チェックでは、依然として `issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して `200` が返されました。
- したがって、実際の読み取り値は依然として狭いままです。`Kura Fund`、`Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` は現在の 6 つのアクティブなブリッジのままであり、`Secom General Research Grant` は現在のサイクル (`March 31, 2026 at 12:00 JST`) ではすでに閉じられており、繰り越されたウォッチ レコードとしてのみ残されており、このセッションでは新しい Todoist アイテムは作成されませんでした。

## 2026 年 3 月 31 日の 16:05 JST ポストプル再読み込み後も修正されたままのもの

- `mind-upload@a11240d38415`、`EEG-DATA@f318ac8ce42d`、および `auto-research-funds@c95cc61fdfc9` 後の `2026-03-31 16:05 JST` での最新のプル再チェックでは、パブリック バッチと解決優先順序が変更されないままになります。
- 最新のプルデルタは、現在のパブリッククレームサーフェスをまだ広げていません。`mind-upload` はコネクトーム/タイミングステートルートカードを強化し、`EEG-DATA` は `OSF eucqf` ディープダイブリフレッシュを追加し、`auto-research-funds` は新しい `Takeda / Nohken` カードマテリアルを追加しましたが、これらの変更はどれも現在の `D10 / D03 / D02 / D01` ファミリやアウトサイドカレント 6 オーダー `U7-1 -> U1-2 -> U4-2 -> U8-1` に代わるものではありません。
- この実行のブラウザ レベルのライブ チェックでは、`issue.html`、`mind-upload-current-public-six-rq-brief.html`、および `u8-1-closed-loop-delay-tolerance-route.html` に対して依然として `200` が返されたため、この実行では公開サイトに新しい散文が追加されません。
- 新しい Todoist `api/v1/sync(items)` の全項目監査では、すでにカバーされているルート ファミリー (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`) が引き続き表示されるため、この実行では新しいタスクは追加されません。
- したがって、実際の読み取り値は変わりません。`Kura Fund`、`Nakatani Foundation graduate scholarship`、`Kashinome Scholarship` は現在の 6 つのアクティブなナロー ブリッジのままですが、`Secom General Research Grant` と `Nakatani Foundation research grant` は次のサイクルの監視ルートのみのままです。

## 2026 年 3 月 31 日までに修正される内容

- `mind-upload@8cc3379`、`EEG-DATA@715ecdf`、および `auto-research-funds@6166f60` の後の 3 月 31 日の `2026-03-31 09:04 JST` でのプル後の再チェックでは、パブリック バッチと解決優先順序が変更されていません。
- 最新のプルデルタはマップを広げますが、現在のパブリッククレームサーフェスは広げません。アストロサイト/SV2Aルートの改良、`U1-2`資金同期パケット、および`Zenodo HEP ERP`の詳細な追加は、`D10`を置き換えたり、`D03/D02/D01`を直接のパブリックアンカーに変えたりするものではありません。
- 4 つのアウトサイドカレント 6 ヘッドライン キューも変更されません。`U7-1` は最もクリーンで公開された `A-tier` フォローアップのまま、`U1-2` は次の狭い逆推定パケットのまま、`U4-2` は最小限の因果関係介入パケットのまま、`U8-1` は有界閉ループ遅延許容パケットのままです。 `U7-2` は、ヘッドライン キューの代替としてではなく、隣接するタイミング メトリック サポート パケットとして、明示的に `U7-1` の隣に配置されるようになりました。正確な行パケットが必要な場合は、[U7-1 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u7-1-synchronization-contract-route)、[U7-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u7-2-timing-metric-route)、[U1-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u1-2-uncertainty-calibration-route)、[U4-2 ルート] に進みます。パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u4-2-minimal-causal-route)、および [U8-1 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u8-1-closed-loop-delay-tolerance-route)。
- `2026-03-31 00:04 JST` では、夜間の再チェックでもパブリック バッチと解決優先順序が変更されないままになります。
- `2026-03-31 00:20 JST` での 3 月 31 日のアクセス監査では、バッチは変更されていませんが、アンカーの読み取り範囲が狭まっています。`D10 3M-CPSEED` は、現在の 6 つの中で唯一明らかに公開されているプラ​​イマリ アンカーのままです。
- 現在、`D03 Multimodal Fusion EEG + Eye-Tracking`、`D02 CSTE`、および `D01 Acquisition delay of wireless EEG` は、`LOGIN TO ACCESS DATASET FILES` および `Subscription Required` を表示する IEEE DataPort ページに解決されるため、パブリック文言では、これらを直接のパブリック アンカーではなく、サブスクリプション ゲート型のサポート アンカーとしてのみ保持するようになりました。
- ライブ アクセス監査とカタログの自動ラベルが一致しない場合、このページはパブリック セーフな文言についてライブ アクセス監査に従い、カタログ ラベルは計画のヒントとしてのみ保持されます。
- `Kura Fund` は 2026 年 4 月 17 日の 17:00 まで、`Nakatani Foundation graduate scholarship` は 2026 年 4 月 1 日から 2026 年 5 月 25 日の 15:00 まで、`Kashinome Scholarship` は 2026 年 4 月 9 日まで営業します。
- `2026-03-31 14:07 JST`での3月31日の公式ウィンドウの再チェックでは、実質的なレーンは変更されないままですが、時計に依存する項目が1つ変更されます。`Secom General Research Grant`は、2026年3月31日の`12:00 JST`の期限がすでに過ぎているため、今回の実行では同日の時計ではなくなりました。そのため、次のサイクルの時計の記録としてのみ残されます。
- 3 月 31 日の `api/v1/sync` 経由の `14:07 JST` Todoist の全項目監査では、既にカバーされている現在のルート (`items=205`、`Kura=2`、`Nakatani family=11`、`Kashinome=2`、`Secom family=3`) がまだ示されているため、この実行では新しいタスクは追加されませんでした。
- `D03/D02/D01` を即時のパブリック ルートとして扱っていたこのページの 3 月 30 日以前のメモは、3 月 31 日のアクセス監査によって置き換えられるものとして読まれる必要があります。
- 3 月 31 日のクロスリポジトリ統合では、現在の 6 つの一般に公開されている代替 EEG ファミリも再チェックされました。これらの代替案は引き続き二次サポートとして有用ですが、それでも現在の `D10/D03/D02/D01` ルート ファミリに取って代わるものではなく、公的請求の上限を引き上げるものでもありません。
- 現在の行パケットでは行ごとに 1 つのコンパクトな `first-pass KPI bundle + stop rule` も公開されるようになり、読者はクレームが拡大する前にルートを停止するものを確認できます。

- パブリック バッチは `U13-2 / U13-5 / U0-2 / U0-3 / U14-4 / U14-2` のままです。
- 実行順序は`U13-2 -> U13-5 -> U0-2 -> U0-3 -> U14-4 -> U14-2`のままです。
- `D10 3M-CPSEED` は依然として唯一の明確に公開されているプラ​​イマリ アンカーです。
- `D03 Multimodal Fusion EEG + Eye-Tracking`、`D02 CSTE`、および `D01 Acquisition delay of wireless EEG` は、サブスクリプション ゲート型サポート アンカーとしてのみ範囲内に残ります。
- `Kura Fund` は 2026 年 4 月 17 日までオープンのままで、`Nakatani Foundation graduate scholarship` は 2026 年 4 月 1 日から 2026 年 5 月 25 日 15:00 まで実行され、`Kashinome Scholarship` は 2026 年 4 月 9 日までオープンのままで、`Secom General Research Grant` は現在のサイクル (`deadline: March 31, 2026 at 12:00 JST`) ではすでにクローズされているため、次のサイクルの監視レコードとしてのみ残ります。

## 3 月 30 日のポストプル再読み取り後の行パケット

ルートは変更されていませんが、各アクティブ行には、提出準備ができているタイトルが 1 つ、現在の EEG アンカーが最初のアーティファクトに十分であるという明示的な理由が 1 つ、コンパクトな KPI バンドルが 1 つ、クレームを狭く保つための明示的な停止ルールが 1 つ含まれています。

| RQ | すぐに投稿できるタイトル | 現在の EEG アンカーで十分な理由 | まだ適合する資金調達の橋 | なぜ国民の主張は依然として狭いのか |
|---|---|---|---|---|
| `U13-2` | `Neural-contribution audit for imagined speech with a brain-minus-prior control` | `D10 3M-CPSEED` は依然として、1 つのリリース内で明白で沈黙を意図した想像上の音声を含むパブリック OpenNeuro ルートを提供するため、デコーダーは純粋な言語以前ではなく、制限された `brain-minus-prior` コントロール ファミリに対してテストできます。 | `Kura Fund`、次に `Nakatani Foundation graduate scholarship` | これにより、狭い解読アーチファクトを事前のみのショートカットから分離できますが、保存された内部メカニズム、保存されたアイデンティティ、または成功した心の保存は確立されません。 |
| `U13-5` | `Perception-to-recall transfer-gap benchmark for mimic separation` | `D03 Multimodal Fusion EEG + Eye-Tracking` は依然として、意図されたペアの EEG + 視線計画ルートを修正しますが、表示される IEEE DataPort メタデータは、中国語の列ガイダンスを備えた `55` 学生の認知負荷データセットであり、公開ページに公開されているリコール固有のラベルがないため、この行は、ゲート付き計画アンカーと外部のリコール有効性要件としてのみ残ります。 | `Kura Fund`、次に `Nakatani Foundation graduate scholarship` | 共有デコーダ ルートは、制限された転送ギャップ ノートをサポートできますが、それ自体では、より強力な保存メカニズムの読み取りを正当化するものではありません。 |
| `U0-2` | `Temporal-validity-aware identity drift audit with offset, jitter, and state-feature collapse` | `D02 CSTE` は引き続き、意図したクロスセッション/クロスタスクの生体認証フロアを修正しますが、現在の IEEE DataPort ページはサブスクリプションゲート型であるため、公開文言では、直接のパブリックアンカーではなくゲートサポートアンカーとして扱われます。 | `Nakatani Foundation graduate scholarship`、次に `Kashinome Scholarship` | これにより、タイミングと状態機能の障害を監査できますが、法的、哲学的、または規範的なアイデンティティの継続性は解決されません。 |
| `U0-3` | `Task-specific threshold stability and overfit-exclusion benchmark for identity drift` | 同じ `D02` アンカーは依然として意図したしきい値ガバナンスの下限を修正しますが、公開文言では、パブリック オープン アンカーではなく、サブスクリプション ゲート型サポート アンカーとしてのみ保持されています。 | `Nakatani Foundation graduate scholarship`、次に `Kashinome Scholarship` | 安定したしきい値は、依然として限界のあるベンチマーク アーティファクトにすぎず、人格の連続性やブランチアイデンティティの解決にとって十分な条件ではありません。 |
| `U14-4` | `Card-integrated reproducibility contract for the current public batch` | `D01 Acquisition delay of wireless EEG` は依然として意図したレイテンシー/開示フロアをマークしますが、表示されるパッケージはそれ自体の再実行ベンチマークではなく、レイテンシーと同期のデータセットであるため、この行はゲートされたサポート ルートとしてのみ留まり、より強力な公開再現性の文言の前に `D13` が必要です。 | `Kura Fund`; `Nakatani Foundation research grant`を次サイクルウォッチとして | カードフィールドを埋めることで開示規律を向上させることができますが、それ自体ではフィールド全体の再現性、展開の準備状況、または標準の採用を実証するものではありません。 |
| `U14-2` | `Fixed-split rerun contract for exploration versus confirmation` | 同じ `D01` ルートは依然として意図した遅延優先分割境界をマークしていますが、表示されるパッケージは遅延/同期が多いため、公開文言ではゲート サポート アンカーとしてのみ保持されており、より強力な確認文言の前に `D13` に基づく再実行サンプルが依然として必要です。 | `Kura Fund`; `Nakatani Foundation research grant`を次サイクルウォッチとして | 固定された分割とネガティブケースの証跡は、再実行の規律を制限する可能性がありますが、探索的な出力や広範な再実行の堅牢性の主張に対する確認の文言をライセンスするものではありません。 |

## 現在のパブリック 6 の概要

| RQ | 現在の質問の焦点 | 現在のアンカー | 次に閉じる最初のアーティファクト | 現在の資金調達ブリッジ | 公的主張の範囲外に置く |
|---|---|---|---|---|---|
| `U13-2` | 幻覚/矛盾チェックをニューラル デコーディング評価に結び付けます。 | `D10 3M-CPSEED` (`10.18112/openneuro.ds006465.v2.0.0`、即時) | `Brain-minus-prior`コントロールテーブルとミミック分離ノート | `Kura Fund`、次に `Nakatani Foundation graduate scholarship` | 内部メカニズムの保存、アイデンティティの保存、または心の保存の成功 |
| `U13-5` | 共有デコーダーの下で、パフォーマンスが知覚と想起の間で分岐する箇所でフリーズします。 | `D03 Multimodal Fusion EEG + Eye-Tracking` (`10.21227/6106-6120`、サブスクリプションゲート型サポート) | 知覚から想起までの劣化ノートと伝達ギャップ表 | `Kura Fund`、次に `Nakatani Foundation graduate scholarship` | より強力なメカニズム保存の読み取り |
| `U0-2` | ID のような文言が測定誤差を吸収する前に、タイミング バジェットを修正します。 | `D02 CSTE` (`10.21227/j162-nh61`、サブスクリプションゲート型サポート) | オフセット/ジッター分布と状態特徴崩壊の監査 | `Nakatani Foundation graduate scholarship`、次に `Kashinome Scholarship` | 法的、哲学的、または規範的なアイデンティティの継続性 |
| `U0-3` | タイミング フロアが制限された後のみ、しきい値の安定性を修正します。 | `D02 CSTE` (`10.21227/j162-nh61`、サブスクリプションゲート型サポート) | 閾値安定性注記とオーバーフィット除外ルール | `Nakatani Foundation graduate scholarship`、次に `Kashinome Scholarship` | 安定した閾値を人格の連続性にとって十分なものとして扱う |
| `U14-4` | カードフィールドを具体的な再実行チェックリストに変えます。 | `D01 Acquisition delay of wireless EEG` (`10.21227/dv1p-vq18`、サブスクリプションゲート型サポート) | 塗りつぶされたモデル カード/データセット カードの例 | `Kura Fund`; `Nakatani Foundation research grant`を次サイクルウォッチとして | 現場全体の再現性、展開の準備状況、または標準の採用 |
| `U14-2` | 探索/確認の分割を運用可能にします。 | `D01 Acquisition delay of wireless EEG` (`10.21227/dv1p-vq18`、サブスクリプションゲート型サポート) | 固定分割リラン契約とネガティブケーストレイル | `Kura Fund`; `Nakatani Foundation research grant`を次サイクルウォッチとして | 探索的な成果を確認証拠として提示する |

## このバッチをフラット化せずに深める方法

- `U13-2 -> U13-5` は依然として音声側の貢献スタックです。まず `D10` 上で `brain-minus-prior` を正直に保ち、次に行が知覚から想起に移るときに転送ルートがどこで途切れるかを尋ねます。
- `U0-2 -> U0-3` は依然としてアイデンティティ ドリフト フロアです。`D02` ルートで最初にバウンド タイミング エラーが発生し、次にタイミング フロアが修正された後にしきい値が存続するかどうかを尋ねます。最も歪みの少ない公開ストレス テストは `ds004148` と `ds007216` のままですが、依然としてバックアップのみです。
- `U14-4 -> U14-2` は依然として再現性契約スタックです。まず開示フィールドを `D01` フロアの埋められたカードに変え、次に探索対確認の分割を凍結します。 `D13` は、これら 2 つの行が次に必要となる最初の公開再実行ファミリーであり続けます。
- `U7-1 -> U7-2 -> U1-2` は現在、パブリック オープン インフラストラクチャ フロアとしてバッチのすぐ外にあります。`D11` は同期コントラクトをパブリックで読み取り可能な状態に保ち、隣接する `U7-2` パケットはどのタイミング エラーが同じ `D11` ファミリのリリース ブロック メトリックになるかを修正し、`D08` はバッチ切り替えを強制することなく逆不確実性ルートを接地状態に保ちます。

## ファーストパス KPI バンドルと停止ルール同期

この実行ではバッチは拡張されません。ルートが拡張されるか、より強力な表現に移行される前に、各アクティブ行に 1 つの KPI バンドルと 1 つの停止ルールが含まれるようにするだけで、現在のパブリック 6 が明示的になります。

| RQ | ファーストパス KPI バンドル | 行が広がる前にルールを停止 |
|---|---|---|
| `U13-2` | `semantic alignment`、`brain-minus-prior gap`、`misalignment rate` | `brain-minus-prior gap` が以前のみのベースラインに向かって崩壊する場合、または `misalignment rate` がセッション間で不安定なままの場合は、停止します。 |
| `U13-5` | `perception-to-recall degradation point`、`transfer gap`、`control-condition stability` | コントロールファミリーの再実行後、劣化ポイントと `transfer gap` が順序を維持できない場合は停止します。 |
| `U0-2` | `clock-offset p95`、`jitter p95`、`state-feature collapse rate` | 再同期によってドリフトフロアが縮小しない場合、または `state-feature collapse rate` がセッション間で境界上限を超えたままの場合は、停止します。 |
| `U0-3` | `session-out AUC`、`threshold stability`、`overfit-exclusion rate` | しきい値の順序がセッション間で反転する場合、またはオーバーフィット スクリーニングが適用された後も受け入れられたモデルが分割固有のままである場合は、停止します。 |
| `U14-4` | `required-card fill rate`、`rerun success rate`、`leak-audit coverage` | カードを増やしても再実行のトレーサビリティが向上しない場合、または否定的なケースの例でリーク監査フィールドが欠落したままである場合は、停止します。 |
| `U14-2` | `fixed-split compliance rate`、`rerun success rate`、`explore-to-confirm carryover gap` | 結果を保存するために分割違反がまだ必要な場合、または再実行時に `explore-to-confirm carryover gap` が崩壊する場合は停止します。 |

## 現時点で各行が EEG で解決できることと解決できないこと

| RQ | 行を実数に保つ EEG-DATA の事実 | 現在クローズできる脳波 | まだ外部のサポートが必要なもの | 正直さを保つ提出文言 |
|---|---|---|---|---|
| `U13-2` | `D10` は、`20 participants x 4 sessions`、明白な / 無言で意図された / 想像上のスピーチ、生の BIDS、およびフェーズ分割派生を 1 つの公開リリース内で提供します。 | 制限付きの `brain-minus-prior` 監査と模倣分離メモ。 | 外部言語評価層、より広範なリーク制御ファミリー、および保存されたメカニズムまたはアイデンティティに関するあらゆる主張。 | `Neural-contribution audit for imagined speech with a brain-minus-prior control` |
| `U13-5` | `D03` は依然として、意図されたペアの EEG + 視線プランニング ルートを修正しますが、表示される IEEE DataPort メタデータは、中国語の列ガイダンスを備えた `55` 学生認知負荷データセットであり、パブリック ページに公開されているリコール固有のラベルがないため、行はゲート付きプランニング アンカーとしてのみ残ります。 | 知覚から想起までの劣化ノートと伝達ギャップ表。 | 外部のリコール有効性レイヤー、公開されている EEG+ET バックアップ ファミリ、およびより強力なメカニズム保存の文言。 | `Perception-to-recall transfer-gap benchmark for mimic separation` |
| `U0-2` | `D02` は引き続き、意図したクロスセッション/クロスタスクの生体認証フロアを修正しますが、現在の IEEE DataPort ページはサブスクリプションゲートになっているため、公開文言ではゲートサポートアンカーとしてのみ維持されます。 | `offset / jitter` ディストリビューションと `state-feature collapse` 監査。 | より長い期間のタイミング ログ、より大規模なコホート、および法的または哲学的な連続性の解釈。 | `Temporal-validity-aware identity-drift audit` |
| `U0-3` | 同じ `D02` ルートは引き続き、意図したしきい値ガバナンスの下限を修正しますが、現在の IEEE DataPort ページはサブスクリプション ゲートであるため、公開文言ではゲート サポート アンカーとしてのみ維持されます。 | 閾値安定性に関する注記とオーバーフィット除外ルール。 | セッション外部の再実行パック、コホート拡張、および人格継続性の読み取り。 | `Task-specific identity-threshold stability study` |
| `U14-4` | `D01` は依然として意図したレイテンシ/開示フロアをマークしますが、表示されるパッケージはそれ自体の再実行ベンチマークではなくレイテンシと同期のデータセットであるため、この行はゲートされたサポート ルートとしてのみ残ります。 | 現在のバッチの入力されたモデル カード/データセット カードの例。 | `D13` に裏付けられた再実行例、リーク監査の例、および分野全体の再現性または標準採用の文言。 | `Disclosure-first reproducibility contract package` |
| `U14-2` | 同じ `D01` レイテンシ優先ルートは引き続き意図された分割境界をマークしますが、表示されるパッケージはスタンドアロンの再実行ファミリではなく遅延/同期が多いため、この行はゲート サポート ルートとしてのみ残ります。 | 固定分割再実行契約とネガティブケーストレイル。 | `D13` に裏付けられた、より豊富な公開ベンチマークにわたる分割違反の例と、より強力な確認準備の主張。 | `Exploration-confirmation split contract for reruns` |

## メインアンカーがゲートされている場合に最適なパブリックオープンサポートファミリー

これらのサポート ファミリは、現在のゲート サポート プランニング アンカーを置き換えるものではありません。アクセスゲートされたデータセットなしでストレステストできるものを検査したい読者のために、最もクリーンで公開されているバックアップファミリーのみを示しています。

| RQ | 最優秀一般公開サポートファミリー | なぜ役立つのか | 現在の計画アンカーを置き換えない理由 |
|---|---|---|---|
| `U13-5` | `D10 3M-CPSEED`、`ChineseEEG-2`、`ZuCo 2.0`、`SparrKULee`、`spoken + imagined robot-speech EEG` | `D10` は音声側コントロール ファミリを公開し続け、`ChineseEEG-2` は維持された読み取り/聴取セマンティック アラインメント ファミリを追加し、`ZuCo 2.0` はパブリック EEG+ET ペア ストリーム ファミリを復元し、`SparrKULee` はより大きな聴覚のみのデコード ベンチマークを追加し、ロボット音声ルートはゲート付きページなしで顕性/想像ストレス テストを検査可能に保ちます。 | これらはいずれも、パブリック ルート上にクリーンなリコール ラベルの付いた分岐ポイントを公開していないため、リコールの有効性が修正されるまでバックアップのみのままです。 |
| `U0-2` | `A test-retest resting and cognitive state EEG dataset`、次に `A multi-session simultaneous EEG-fMRI dataset with online experience sampling` | これらは、最も強力なパブリックオープン再テストラダーと、最も強力なパブリックオープンマルチセッション来歴ラダーを提供します。 | これらは強力なストレステスト ファミリですが、計画において `D02` を優先し続ける直接的な `cross-session / cross-task biometrics` フレームワークに代わるものではありません。 |
| `U0-3` | `A test-retest resting and cognitive state EEG dataset`、次に `A multi-session simultaneous EEG-fMRI dataset with online experience sampling` | これらは、しきい値ルールが 1 つのセッションまたは 1 つの前処理パスの外で存続するかどうかをチェックするための、最もクリーンな公開再実行ラダーを提供します。 | これらは依然として、`D02` ほど意図されたアイデンティティ ドリフト フロアに直接一致していないため、置き換えではなくサポートのままです。 |
| `U14-4` | `D13 A New Benchmark Dataset Towards Ubiquitous P300 ERP-based BCI Applications`、次に `D08 Simultaneous human intracerebral stimulation and HD-EEG` | `D13` は、より強力な開示文言が導入される前に最初に必要とされた公開再実行ファミリーであり、`D08` はその後、最も明確な根拠のある検証フィールド ファミリです。 | これらは、最初の待ち時間/開示フロアが修正された後にのみ役立ちます。どちらも `D01` に代わるものではありませんが、`D13` はその行が次に必要とするサポート ファミリです。 |
| `U14-2` | `D13 A New Benchmark Dataset Towards Ubiquitous P300 ERP-based BCI Applications`、次に `D08 Simultaneous human intracerebral stimulation and HD-EEG` | `D13` は、最初に必要なパブリックオープンの分割違反サンプル ファミリであり、`D08` はその後、より強力な検証スタイルの障害ファミリを提供します。 | これらは、後で再実行するサンプルの範囲を広げるのに役立ちますが、`D01` をプライマリとして計画しておくためのレイテンシ優先分割境界に代わるものではありません。 |

## 行ごとの概要

### `U13-2`

- 質問の焦点: デコーダの成功を精神保存の結果として扱うことなく、幻覚と一貫性チェックを神経復号評価に結びつけることができるかどうか。
- `D10` が最強のアンカーであり続ける理由: ローカル ミラーは依然として、`20 participants x 4 sessions` によるパブリック OpenNeuro ルート、同じリリース内の明白でサイレント意図された想像上の音声、さらに生の BIDS とフェーズ分割派生を公開します。
- このアンカーが今すぐ閉じるのに十分強力なものは、`brain-minus-prior` コントロール ファミリ、狭い模倣分離メモ、および限定された不整合監査です。
- 正直さを保つ提出文言: `Neural-contribution audit for imagined speech with a brain-minus-prior control`。
- 外部からのサポートがまだ必要なのは、より強力なメカニズムの文言が許可される前に、外部言語評価層とより広範なリーク制御ファミリーです。
- まだ主張の外に残っているもの、つまり、保存された内部メカニズム、保存されたアイデンティティ、そしてより強力なマインドアップロードの文言です。
- 行固有のアンカー選択の根拠が必要な場合は、[U13-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u13-2-brain-minus-prior-route) を読んでください。

### `U13-5`

- 質問の焦点: ルートが知覚から想起に移行するときに、共有デコーダがどこで失敗し始めるか。
- `D03` がゲート付きサポート ルートのみに留まる理由: 意図したペアの EEG + 視線追跡ターゲットはその行にとって依然として有用ですが、表示される IEEE DataPort メタデータは、中国語の列ガイダンスを備えた `55` 学生の認知負荷データセットであり、公開ページに公開されているリコール固有のラベルがないため、公開の文言は即時公開アンカーの読み取り値よりも狭いままでなければなりません。
- このアンカーが現在閉じるのに十分な強度を持っているもの: 知覚から想起までの劣化ノートと、明らかに狭いままである転送ギャップ表。
- 正直さを保つ提出文言: `Perception-to-recall transfer-gap benchmark for mimic separation`。
- 依然として外部のサポートが必要なのは、外部の想起妥当性レイヤーと、共有メカニズムの読み取りを試みる前の公開音声/EEG+ET バックアップファミリーです。
- まだ主張の範囲外にあるもの: 共有デコーダが共有された保存された内部メカニズムを実証するというあらゆる記述。
- 行固有のアンカー選択の根拠が必要な場合は、[U13-5 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u13-5-perception-to-recall-route) を読んでください。

### `U0-2`

- 質問の焦点: アイデンティティのような文言が無制限の測定誤差に崩壊するのを防ぐ方法。
- `D02` がゲート付きサポート フロアのみのままである理由: 対象のデータセットは依然として明示的にクロスセッションおよびクロスタスクであり、`10 participants` に関連付けられたままですが、現在の IEEE DataPort ページはサブスクリプションゲート型であるため、パブリックな表現ではそれを直接のパブリック アンカーとして扱うことができません。
- このアンカーが今すぐ閉じるのに十分強力なものは、`offset / jitter` ディストリビューションと `state-feature collapse` 監査です。
- 正直さを保つ提出文言: `Temporal-validity-aware identity-drift audit`。
- 依然として外部サポートが必要なのは、より長い期間のタイミング ログと、行が制限されたドリフト ベンチマーク以上のものとして読み取られる前のより大きなコホートです。
- まだ主張の範囲外にあるもの: 法的、哲学的、または規範的な継続性の主張。
- 行固有のアンカー選択の根拠が必要な場合は、[U0-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u0-2-temporal-validity-route) を読んでください。

### `U0-3`

- 質問の焦点: タイミング ルートがすでに制限されている場合にのみ、しきい値の安定性を解釈可能にする方法。
- 同じ `D02` アンカーがゲート サポートとしてのみ範囲内に留まる理由: しきい値の安定性は、`U0-2` と同じ意図されたクロスセッション/クロスタスク フロアにある場合にのみ意味を持ちますが、現在の IEEE DataPort ページはサブスクリプション ゲートされているため、パブリックの文言は即時アクセスの読み取り値よりも狭い範囲にとどまる必要があります。
- このアンカーが現在閉じるのに十分な強度を持っているものは、ベンチマークのような狭い範囲を維持するしきい値安定性メモとオーバーフィット除外ルールです。
- 正直さを保つ提出文言: `Task-specific identity-threshold stability study`。
- まだ外部のサポートが必要なのは、この行の前のセッション外部再実行パックとコホート拡張で、制限された生体認証しきい値の主張よりも強力なものを運ぶことができます。
- まだ主張の範囲外にあること: 安定した閾値を人格の連続性または分岐アイデンティティの解決に十分なものとして扱うこと。
- 行固有のアンカー選択の根拠が必要な場合は、[U0-3 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u0-3-threshold-stability-route) を読んでください。

### `U14-4`

- 質問の焦点は、開示フィールドを再実行に十分なほど具体的にする方法です。
- `D01` が依然として制限されたエントリ ポイントとしてのみ有用である理由: 目に見えるパッケージは、それ自体の再実行ベンチマークではなく、ワイヤレス遅延と同期のデータセットですが、フィールド全体の標準化を主張することなく、レイテンシーと測定フィールドを実際のモデル カード/データセット カードの例に強制的に組み込むには十分です。
- このアンカーが今すぐ閉じるのに十分な強度を持っているもの: 現在のパブリック バッチの埋め込まれたカードの例。
- 正直さを保つ提出文言: `Disclosure-first reproducibility contract package`。
- 外部のサポートがまだ必要なもの: より広範な再現性が主張される前に、`D13` に裏付けられた再実行ベンチマークとリーク監査のサンプル。
- 依然として主張の範囲外にあるもの: 組織での採用、分野全体の標準の採用、または広範な再現性の勝利宣言。
- 行固有のアンカー選択の根拠が必要な場合は、[U14-4 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u14-4-card-contract-route) を読んでください。

### `U14-2`

- 質問の焦点: 探索と確認の分割を願望的なものではなく実際に実行できるようにする方法。
- 同じ `D01` アンカーが依然として機能する理由: レイテンシー優先の測定ルートは、固定分割と再実行境界を凍結するのに十分ですが、より強力な確認文言を試みる前に、最初の公開再実行ファミリーとして `D13` が依然として必要です。
- このアンカーが今すぐ閉じるのに十分強力なもの、つまり、固定分割再実行契約と、明示的に狭いままであるネガティブケースのトレイルです。
- 正直さを保つ提出文言: `Exploration-confirmation split contract for reruns`。
- まだ外部のサポートが必要なもの: 行がより広範な確認準備として読み取れるようになる前に、`D13` に裏付けられた、より豊富な公開ベンチマークにわたる分割違反の例。
- まだ主張の範囲外にあるもの: より広範な再実行堅牢性の主張、または探索的な出力に対する確認的な文言。
- 行固有のアンカー選択の根拠が必要な場合は、[U14-2 ルート パケット](https://github.com/yasufumi-nakata/mind-upload/wiki/u14-2-fixed-split-route) を読んでください。

## このページで実行できないこと

- これは、より広い `60RQ` マップを置き換えるものではありません。
- 現在の 6 つを超えてパブリック バッチを拡張することはありません。
- それは、理論、法律、神経権利、または完全なアイデンティティの問題を脳波のみで解決できる状態に移行させるものではありません。
