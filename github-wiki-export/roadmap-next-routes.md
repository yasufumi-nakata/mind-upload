# Wiki: ロードマップ後にたどるべき 5 つの道

> 依存関係マップを見て次のページを決定するためのガイド
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: ロードマップのルート

## このページの役割
このページは、技術ロードマップを読んだ後にどのような点を議論すべきかを整理するための補助的なガイドです。測定に戻るか、再構築と因果推定に行くか、実装に戻るか、検証条件に戻るか、システムと連携に戻るかによって、次のページが変わります。

## 正確性に関する注記
ここに示されているのは、ロードマップを読んだ後のエントリーポイントです。各ノードの公式ポイントや達成条件はロードマップ本文で必ずご確認ください。

## 公開ページへ戻る
- [テクノロジーロードマップ](https://mind-upload.com/tech_roadmap.html)
- [検証ベース](https://mind-upload.com/verification.html)
- [脳波検査の概要](https://mind-upload.com/eeg_101.html)

## 関連 Wiki ページ
- [Wiki: ロードマップの見方](https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide) - ロードマップそのものをもう一度読みたい人向け。
- [Wiki: L0～L5の各読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes) - 主張レベルからリードを見たい人向け。
- [Wiki: 検証後の 4 つのパス](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes) - Vシリーズに移行してさらにスキルを磨きたい人向けです。

## 現在わかっていること
- 技術ロードマップは全体図なので、このままでは次のページが広すぎます。
- 計測、再構成、実装、検証、社会実装で戻るページが異なります。
- ロードマップを読んだ後、ルートを1つに絞ると分かりやすく進みやすくなります。

## まだわかっていないこと
- どのルートが最短で最も効果的かは、今後のデータやベンチの開発によって変わる可能性があります。
- VとDの最終条件にはまだ未解決の部分が多い。

---

<h2>地図を見てルートを決める</h2>
<p>
テクノロジーロードマップは「全体像」を把握するのには役立ちますが、次にどこに進むべきかという点では広すぎます。ここでは、今掘り下げたい内容に応じて5つのパスに分け、次のページを固定します。
</p>

<h2>ロードマップ後にたどるべき 5 つの道</h2>
<table>
<thead>
<tr>
<th>次に知りたいこと</th>
<th>次のページ</th>
<th>わかること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>測定限界を下げたい</strong></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a> / <a href="https://mind-upload.com/datasets.html">データセット</a></td>
<td>Mシリーズの前提である、単体で測定できるものと測定できないものを確認できます。 </td>
</tr>
<tr>
<td><strong>I再構成と因果推定をさらに掘り下げたい</strong></td>
<td><a href="https://mind-upload.com/verification.html">検証</a> / <a href="https://mind-upload.com/perspective.html">視点</a></td>
<td>Rシリーズが評価や因果関係検証につながるところがわかります。 </td>
</tr>
<tr>
<td><strong>I 実装と L0 の作業に取り掛かりたい</strong></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">ハンズオン</a> / <a href="https://mind-upload.com/datasets.html">データセット</a></td>
<td>I シリーズや入力データの選択に進む前に、最小ループを指定できます。 </td>
</tr>
<tr>
<td><strong>検証条件を重視したい</strong></td>
<td><a href="https://mind-upload.com/verification.html">検証</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">検証後の4つのパス</a></td>
<td>V シリーズのアサーション レベルと、実践、クローズド ループ、アイデンティティの次のブランチを確認できます。 </td>
</tr>
<tr>
<td><strong>システムと外部連携を確認したい</strong></td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">コラボレーション</a> / <a href="https://mind-upload.com/issue.html">発行</a></td>
<td>今できる準備とは別に、Dシリーズと外部依存関係を確認できます。 </td>
</tr>
</tbody>
</table>

<h2>なぜこの部門なのか</h2>
<table>
<thead>
<tr>
<th>way</th>
<th>ロードマップの後にそのページにアクセスする理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>測定</strong></td>
<td>Mシリーズでは入力限界が決められているため、測定の基礎は別ページで確認しておくと読み間違いが少なくなります。 </td>
</tr>
<tr>
<td><strong>再構成</strong></td>
<td>Rシリーズは評価と因果関係の検証につながるため、検証と視点を補う必要があります。 </td>
</tr>
<tr>
<td><strong>実装</strong></td>
<td>Iシリーズは紙の上だけでなく、ハンズオンやデータセットなども含めて整理しないと先に進むことが難しいためです。 </td>
</tr>
<tr>
<td><strong>検証</strong></td>
<td>Vシリーズでは全体のデザインと主張レベルを合わせて見る必要があるため、検証側を深掘りする方が自然です。 </td>
</tr>
<tr>
<td><strong>社会実装</strong></td>
<td>Dシリーズはシステムや外部依存が大きいため、課題や連携を具体化すると実践しやすくなります。 </td>
</tr>
</tbody>
</table>

<h2>途中でやめるときのサポートwiki</h2>
<table>
<thead>
<tr>
<th>停車場所</th>
<th>ウィキに戻る</th>
</tr>
</thead>
<tbody>
<tr>
<td>P/M/R/I/V/D自体の読み込みで停止</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide">ロードマップの読み方</a></td>
</tr>
<tr>
<td>主張レベルから見てみたい</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">各L0～L5の見方</a></td>
</tr>
<tr>
<td>実用側に降順で停止</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">EEG から L0 までの 1 つの直線パス</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">検証後にたどる 4 つのパス</a></td>
</tr>
<tr>
<td>理論面に戻る順に停止</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/wbe-to-theory-route">WBE を開始し、理論をさらに深く掘り下げるための 4 つのルート</a></td>
</tr>
<tr>
<td>外部依存および参加パスにより停止</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">社内生産と外部依存関係</a></td>
</tr>
</tbody>
</table>

<h2>よくある迷い方</h2>

<h4>間違い</h4>
<ul>
<li><strong>ロードマップを読むだけで、次の行動が決まったような気分になります：</strong>実際には、ルートを1つに絞る必要があります。 </li>
<li><strong>SM と R をスキップして I と V に進む:</strong> これにより、入力と推定の制限内に留まりながら、より強力な議論に進むことが容易になります。 </li>
<li><strong>D シリーズの要約はそのままにします:</strong> 準備を課題とコラボレーションに切り戻す方が現実的です。 </li>
<li><strong>検証に行けばすべてわかります:</strong>Vシリーズ以降、L0、L3、L4に以下の分岐があります。 </li>
</ul>

<h2>次に戻る場所</h2>
<p>
ロードマップ本文に戻るには<a href="https://mind-upload.com/tech_roadmap.html">テクノロジーロードマップ</a>、検証側に戻るには<a href="https://mind-upload.com/verification.html">Verification Platform</a>、理論サイドブランチに戻るにはWBE入門からの<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/wbe-to-theory-route">4ルート</a>を使用してください。
</p>
