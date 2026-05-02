# Wiki: 更新/分岐/停止ルール

> 変化に応じて変化するシステムを監査するための基本
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: 学習ガイド

## このページの役割
このページは、Mind-Uploadに頻繁に登場する「`updates,'' ``versions,'' ``branches,'' ``stopping rules,'' and ``キルスイッチ」を序盤から解説するwikiです。スコアが上がったからといって、それが同じシステムの自然な経過であると単純に考えないでください。これを履歴とともに変更を監査するための基礎として使用します。

## 正確性に関する注記
ここに示すのは、動作と検証の基本的な配置です。どの程度の変化を維持する必要があるか、どの停止ルールが十分であるかについての最終的な基準は、問題や理論に応じてまだ決定されていません。

## 公開ページへ戻る
- [テクノロジーロードマップ](https://mind-upload.com/tech_roadmap.html)
- [検証ベース](https://mind-upload.com/verification.html)
- [実践](https://mind-upload.com/datasets.html#l0-practice)

## 関連 Wiki ページ
- [Wiki: アイデンティティ評価と連続性テスト](https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests) - 完全な L4 導通テストに戻ります。
- [Wiki: 状態/特性/ドリフト](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - 更新と長期的な変更を区別する方法を完了します。
- [Wiki: ベースライン/事前登録/モデルカード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - 事前登録と結果記録の役割の違いを補います。
- [Wiki: 閉ループ、遅延、ジッター、安全停止](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - リアルタイムで安全な停止を考える方法を補完します。
- [ウィキホーム](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページに戻ることができます。

## 現在わかっていること
- 学習やモデルの更新を許可する場合は、履歴管理や差分記録が必要になります。
- 分岐が起こると、それを一つの「同じ個人」として扱うことが難しくなります。
- 停止ルールは、結果を確認した後ではなく、事前に修正した方が強力です。

## まだわかっていないこと
- どの程度のドリフトまたは発散が同一性の範囲内であるとみなされるかは不明です。
- L4/L5分岐後の責任と権利の扱いは制度面も含めて未解決である。

---

<h2>最短の区別</h2>
<p>
<strong>Update</strong>は同じ履歴を継承する変更、<strong>Branch</strong>は同じ開始点から複数の履歴を実行する場合、<strong>Stopルール</strong>はどのような結果をキャンセルまたは一時停止するかの事前ルール、<strong>Kill switch</strong>は危険時の緊急停止方法です。似ていますが、役割が異なります。
</p>

<h2>なぜこの区別が必要ですか?</h2>
<p>
WBE とアイデンティティに関しては、システムは固定されていません。学べば変わり、真似すれば離れ、使えばやめるかどうか。ここを曖昧にしておくと、「`It's better than the previous version, so it's a healthy progression of the same system,'' or `『分岐しても同一人物』」などと強く読まれがちだ。
</p>

<h2>最初に個別の条件</h2>
<table>
<thead>
<tr>
<th>期間</th>
<th>大まかな意味</th>
<th>ここが重要ポイント</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>更新</strong></td>
<td>同じシステムに新しい学習や設定の変更を導入します。 </td>
<td>差分で何が変わったのかを記載しておかないと評価の意味が曖昧になってしまいます。 </td>
</tr>
<tr>
<td><strong>バージョン</strong></td>
<td>その時点での固定状態に割り当てられたID。 </td>
<td>以前のバージョンを上書きせずに戻って比較できることが重要です。 </td>
</tr>
<tr>
<td><strong>支店</strong></td>
<td>別々の更新履歴が同じ開始点から実行されます。 </td>
<td>は分岐後の履歴が異なるため、同じ評価ユニット内に混在させないほうが無難です。 </td>
</tr>
<tr>
<td><strong>ストップルール</strong></td>
<td>これらは、どの結果をキャンセル、一時停止、または取り消しに使用するかを決定する事前ルールです。 </td>
<td>結果を見て決めるより先に直した方が検証としては強いです。 </td>
</tr>
<tr>
<td><strong>キルスイッチ/アイソレーション</strong></td>
<td>安全上の問題が発生した場合に、動作を停止または遮断する機構です。 </td>
<td>停止ルールとは異なり、統計的な判断ではなく安全性の確保を主な目的としています。 </td>
</tr>
</tbody>
</table>

<h2>更新しても問題ないかどうかの最低限のチェック</h2>
<table>
<thead>
<tr>
<th>チェック項目</th>
<th>最低限やりたいこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>変更点の明確化</strong></td>
<td>データ、前処理、モデル、評価メトリクスに加えられた変更を書き留めます。 </td>
</tr>
<tr>
<td><strong>前のバージョンを保存</strong></td>
<td> は以前のバージョンを上書きせず、同じ入力で再実行できる状態を残します。 </td>
</tr>
<tr>
<td><strong>比較条件固定</strong></td>
<td>同じテスト、同じ評価指標、同じベースラインを使用して以前のバージョンと比較します。 </td>
</tr>
<tr>
<td><strong>漏れがないか再チェック</strong></td>
<td>トレーニング/テストの境界と正規化手順が更新によって破損していないことを再確認します。 </td>
</tr>
<tr>
<td><strong>故障時の対応</strong></td>
<td>パフォーマンスの低下や不安定性が発生した場合に、どこでアップデートを一時停止またはキャンセルするかを最初に決定します。 </td>
</tr>
</tbody>
</table>

<strong>重要</strong>
<p>
スコアが上がったからといって、それが安全なアップデートであるとは限りません。リーク、評価の変更、または便利なサブセット選択により数値が増加する可能性があるため、一連の <strong> 相違点 </strong> および <strong> 比較条件 </strong> を保持する必要があります。
</p>

<h2>分岐が発生した場合の修正方法</h2>
<table>
<thead>
<tr>
<th>直したいところ</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>分岐点</strong></td>
<td>これは、ブランチがどのバージョンとデータポイントから作成されたかを明確にするためです。 </td>
</tr>
<tr>
<td><strong>親子関係</strong></td>
<td>どのブランチがどの親バージョンを継承したかの監査を有効にします。 </td>
</tr>
<tr>
<td><strong>個別ID / インスタンスID</strong></td>
<td>これは、複数の履歴を同一人物として混同することを避けるためです。 </td>
</tr>
<tr>
<td><strong>評価期間</strong></td>
<td>分岐直後が似ているのか、ずっと似ているのかを区別するためです。 </td>
</tr>
<tr>
<td><strong>帰属ルール</strong></td>
<td>どのブランチの達成/失敗としてどの結果が記録されるかを修正するためです。 </td>
</tr>
</tbody>
</table>
<p>
特にアイデンティティに関する議論では、分岐後のすべての結果を総称して「プリンシパル」と呼ぶのは危険です。少なくとも、<strong> を </strong> 評価の同じ単位として扱う時点までを記録する必要があります。
</p>

<h2>停止ルールとキルスイッチは異なります</h2>
<table>
<thead>
<tr>
<th>仕組み</th>
<th>いつ決めるか</th>
<th>主目的</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ストップルール</strong></td>
<td>実験・評価前。 </td>
<td>失敗判定や撤退ラインを取り残さないためです。 </td>
</tr>
<tr>
<td><strong>ホールド/フリーズ</strong></td>
<td>今回問題が発覚しました。 </td>
<td>原因が判明するまで、更新・公開を一時的に停止させていただくためです。 </td>
</tr>
<tr>
<td><strong>キルスイッチ/アイソレーション</strong></td>
<td>安全上の問題に備えて事前に実装してください。 </td>
<td>危険な行為や逸脱を速やかに中止するためのものです。 </td>
</tr>
</tbody>
</table>

<strong>よくある混乱</strong>
<p>
「`I stopped because the results were bad'' is about stopping rules, and ``I stopped immediately because it was dangerous'' is about safety. The same word `「停止」」は、証拠の処理と安全対策に関しては異なる意味を持ちます。
</p>

<p>
特に閉ループの実装では、遅延や異常な動作に対する安全な停止がさらに重要になります。最初にリアルタイム システムの入口だけを整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">Wiki: 閉ループ、遅延、ジッター、および安全停止</a> を参照してください。
</p>

<h2>保持したい最小限のログ</h2>

<h4>チェックリスト</h4>
<ul>
<li><strong>バージョン ID:</strong>今評価したのはどのバージョンですか? </li>
<li><strong>親 / ブランチ ID:</strong>どこから分岐したか。 </li>
<li><strong>差分の変更:</strong>データ、前処理、モデル、評価の何が変更されましたか? </li>
<li><strong>比較結果：前バージョンとの相違点、改善点、劣化点、不明点。 </li>
<li><strong>中止の決定:</strong>どのルールが触れられましたか、または触れられませんでしたか? </li>
<li><strong>障害の例:</strong>機能しないか崩壊した状態。 </li>
</ul>

<h2>3 強力な議論を読むときの質問</h2>
<ol>
<li><strong>アップデート前後で違いはありますか?</strong>何が変わったのか不明な場合は、改善の意味を深読みしないほうが無難です。 </li>
<li><strong>ブランチIDと観測期間はありますか?</strong>複数の履歴を1つにまとめていないか確認してください。 </li>
<li><strong>停止ルールは事前に決められていますか?</strong>不良結果が出た場合の処理を後から書き換えていないか確認してください。 </li>
</ol>

<h2>次に戻る場所</h2>
<p>
ロードマップのI5 / I8 / V7に戻りたい場合は<a href="https://mind-upload.com/tech_roadmap.html">Technology Roadmap</a>を、検証プラットフォームのレジストリ/監査に戻りたい場合は<a href="https://mind-upload.com/verification.html">Verification Platform</a>を、L0プラクティスに戻りたい場合は<a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a>をご利用ください。
</p>
