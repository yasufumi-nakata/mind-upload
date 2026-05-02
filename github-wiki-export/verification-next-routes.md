# Wiki: 検証後に従うべき 4 つのパス

> 検証プラットフォームを読んだ後、迷わず次のページに進むためのガイド
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: 読書ルート

## このページの役割
このページは、検証を読んだ後に知りたいことに応じて、次にどのページを公開するかを決定するためのガイドです。次のページは、L0 実装、L2 介入検証、L3 閉ループ、または L4 ID のいずれに戻るかによって変わります。

## 正確性に関する注記
ここが検証への次の入り口です。各路線の実情は必ずオリジナルページの本文でご確認ください。

## 公開ページへ戻る
- [検証プラットフォーム](https://mind-upload.com/verification.html)
- [実践的な](https://mind-upload.com/datasets.html#l0-practice)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki ページ
- [Wiki: L0～L5の各読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes) - これは、レベルの全体的なパスに戻りたい人向けです。
- [Wiki: 実用的なページを読むためのガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide) - これは、検証、データセット、ハンズオンの役割の違いを最初に確認したい人向けです。
- [Wiki: EEG から L0 への直線パス](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route) - L0側の特定ルートだけをすぐに見たい人向けです。

## 現在わかっていること
- 検証は全体の設計図なので、このままでは次のページが大きすぎます。
- 戻るページは、L0 実装、L2 検証、L3 閉ループ、L4 ID によって異なります。
- 検証後にルートを修正すると、読み取りがより安定します。

## まだわかっていないこと
- 最終的にどのルートが最も重要になるかは、プロジェクトの進行に応じて変わる可能性があります。
- L4とL5の最終条件はまだ決まっていない。

---

<h2>次のページを決める</h2>
<p>
設計図として検証は重要ですが、ただ読むだけでは次の作業に向けて幅が広すぎます。ここでは<strong>・知りたいことは次</strong>をベースに4つのパスに分けて次のページを固定していきます。
</p>

<h2>検証後にたどる4つの道</h2>
<table>
<thead>
<tr>
<th>知りたい</th>
<th>次のページ</th>
<th>そこで何を決めるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I L0</strong></td> の実装を作成したい
<td><a href="https://mind-upload.com/datasets.html#l0-practice">ハンズオン</a></td>
<td>入力、QC、前処理、ベースライン、および失敗ケースを接続する手順を修正します。 </td>
</tr>
<tr>
<td><strong>L2介入/反事実検証について知りたい</strong></td>
<td><a href="https://mind-upload.com/tech_roadmap.html">ロードマップ</a></td>
<td>依存関係を利用してどの問題が因果関係検証や生成予測につながるのかを確認します。 </td>
</tr>
<tr>
<td><strong>I L3</strong></td>の閉ループ条件を知りたい
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a> または <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ/遅延/ジッター/安全停止</a></td>
<td>オフラインの精度とリアルタイムの安定性の違いを分離します。 </td>
</tr>
<tr>
<td><strong>I L4</strong></td>の正体を知りたい
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a> または <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">ID 評価および連続性テスト</a></td>
<td>記憶、価値観、学習、分岐の観点から、連続しているものとみなしたいものにチェックを入れます。 </td>
</tr>
</tbody>
</table>

<h2>なぜこの部門なのか</h2>
<table>
<thead>
<tr>
<th>way</th>
<th>確認後にそのページに移動する理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0実装</strong></td>
<td>検証で決めた合格条件をハンズオンで実際の成果物に落とし込む必要があるためです。 </td>
</tr>
<tr>
<td><strong>L2 検証</strong></td>
<td>ロードマップを見てどの点に最初に取り組む必要があるかを確認しないと、介入や反事実に飛びつくのは簡単です。 </td>
</tr>
<tr>
<td><strong>L3 閉ループ</strong></td>
<td>閉ループの場合、検証設計を評価するだけでは十分ではありません。測定とリアルタイムの制約も考慮する必要があります。 </td>
</tr>
<tr>
<td><strong>L4 パーソナリティ</strong></td>
<td>これは、スコアだけでは自分のアイデンティティを評価できないためです。まず、事前登録してテストしたいものを整理する必要があります。 </td>
</tr>
</tbody>
</table>

<h2>片道支援wiki</h2>
<table>
<thead>
<tr>
<th>way</th>
<th>一緒に見る価値のあるWiki</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0実装</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">A EEG から L0</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack">L0</a></td> の最小アーティファクト パック
</tr>
<tr>
<td><strong>L2 検証</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification">反事実、介入、摂動の検証</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">観察から推定まで</a></td>
</tr>
<tr>
<td><strong>L3 閉ループ</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ/遅延/ジッター/安全停止</a></td>
</tr>
<tr>
<td><strong>L4 パーソナリティ</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">人物像の評価と継続性テスト</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem">人物像とコピーの問題</a></td>
</tr>
</tbody>
</table>

<h2>よくある迷い方</h2>

<h4>間違い</h4>
<ul>
<li><strong>「検証」を読むだけで、次の行動が決まったような気分になります:</strong> 実は、ルートを 1 つに絞る必要があります。 </li>
<li><strong>L0 と L2 の追跡を同時に開始:</strong> 最初に再現可能な分析を確立する方が、やり直しが少なくて済むため簡単です。 </li>
<li><strong>L3 を精度の観点のみで考えてください:</strong> 閉ループには追加の遅延と安全停止が必要です。 </li>
<li><strong>L4をスコアの延長として考える：</strong>個性的に連続すると思われるものをあらかじめ別途設計する必要がある。 </li>
</ul>

<h2>次に戻る場所</h2>
<p>
検証本文に戻る場合は<a href="https://mind-upload.com/verification.html">Verificationbase</a>をご利用ください。レベル全体のルートに戻るには、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">でL0～L5</a>の各L0を読み取る方法を使用してください。実践ページ間の役割の違いに戻るには、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide">実践ページの読み方ガイド</a>を使用してください。
</p>
