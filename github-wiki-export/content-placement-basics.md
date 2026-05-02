# Wiki: 新しい情報をどこに配置するかを決定するための基本

> 何を書くかを決める前に、配置場所を決める基本
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: コンテンツ配置の基本

## このページの役割
このページは、Mind-Uploadに新しい情報を追加する際に、どこに載せるかを最初から整理するための補足資料です。公開ページは情報ポータル、Wiki は学習のための詳細な説明、問題は行われる変更、コラボレーションは外部依存関係を整理するため、操作領域は中間結果です。役割の違いを例で確認できます。

## 正確性に関する注記
ここで示しているのは配置の基本です。個々の主張の正否を判断するには、必ず元のページの本文と根拠に戻ってください。

## 公開ページへ戻る
- [パブリック コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)
- [貢献ガイド](https://mind-upload.com/issue.html)
- [連携候補者](https://mind-upload.com/issue.html#external-collaboration)

## 関連 Wiki ページ
- [Wiki: 公開ページを読むためのガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - これは、公開ページ間の役割の違いを最初に確認したい人向けです。
- [Wiki: 参加/コラボレーション後にたどる 5 つの道筋ページ](https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes) - 場所を決めたら次の作業に移りたい人向けです。
- [Wiki: 最初の問題の書き方](https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics) - 場所が問題になる場合の書き方についての追加情報。

## 現在わかっていること
- 最初に場所を特定すると、情報の重複やリードの散逸が減少します。
- 公開ページとWikiを分離することで、入り口の視認性の向上とより詳しい説明の両方が容易になります。
- 外部に依存するタスクは、現在行われた変更とは別に管理する必要があります。

## まだわかっていないこと
- 将来的にどの号が独立したページになるかは、コンテンツの量と読者の需要に応じて変わります。
- 一部のトピックは複数のページにまたがるため、最終的な行き先は引き続き調整されます。

---

<h2>最初に決めるのは「内容」よりも「場所」</h2>
<p>
新しい情報を見つけたときにすぐに本文を書き始めると、重複や混乱が増えることになります。最初にその情報の役割を決定すると、公開ページをポータルとして維持しながら、必要な詳細を Wiki に追加することが容易になります。
</p>

<h2>まずは5つの保管場所を分ける</h2>
<table>
<thead>
<tr>
<th>場所</th>
<th>何を入れるか</th>
<th>置いてはいけないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>公開ページ</strong></td>
<td>今わかっていること、まだわかっていないこと、次に読むべきこと、そして意思決定チャート。 </td>
<td>L背景知識を最初から最後まで学べる長尺教材。 </td>
</tr>
<tr>
<td><strong>wiki</strong></td>
<td>の基本解説、類語の違い、ページの見方、学習用補助資料。 </td>
最新の運用上の決定と実装ステータスの <td>A プライマリ リポジトリ。 </td>
</tr>
<tr>
<td><strong>問題</strong></td>
<td>このリポジトリで現在実行される変更、変更場所、進行条件、反抗条件。 </td>
<td>あたかも完了したかのように外部依存関係を含む大きな計画を作成する。 </td>
</tr>
<tr>
<td><strong>コラボレーション</strong></td>
<td> 共同研究、標準化提案、機関協力などのパートナーや外部条件を必要とする協議。 </td>
<td>Aここでしか完結できない小さな修正の記録。 </td>
</tr>
<tr>
<td><strong>操作エリア</strong></td>
<td>未整理のメモ、中間結果、CSV、機械処理結果、監査ログ。 </td>
<td>読者向けにテキストをそのまま表示します。 </td>
</tr>
</tbody>
</table>

<h2>回答内容に基づいて情報を配置する場所を決定</h2>
<table>
<thead>
<tr>
<th>情報が答える質問</th>
<th>最初に置く場所</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>この分野で現在わかっていることと未解決のまま残っていること</strong></td>
<td><a href="https://mind-upload.com/verification.html">検証</a>、<a href="https://mind-upload.com/tech_roadmap.html">ロードマップ</a></td>などの公開ページ
<td>公開ページは、判断の入り口として既知・未知を示す役割を果たしているからです。 </td>
</tr>
<tr>
<td><strong>用語や予備知識を一から説明したい</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki">wiki</a></td>
<td>入り口ページを読みやすくするために、学習資料を Wiki に置いたほうがよいでしょう。 </td>
</tr>
<tr>
<td><strong>今すぐ直せるものは直したい</strong></td>
<td><a href="https://mind-upload.com/issue.html">問題</a></td>
<td>これは、完了条件を含む実行可能な変更を管理できるためです。 </td>
</tr>
<tr>
<td><strong>共同研究や標準化の候補を整理したい</strong></td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">コラボレーション</a></td>
<td>これは、外部の依存関係と社内の変更が混在することを避けるためです。 </td>
</tr>
<tr>
<td><strong>生データや未整理のメモを残しておきたい</strong></td>
<td>操作エリア</td>
<td>統合先が決まる前に公開テキストに直接フラグメントが流し込まれることを防ぐためです。 </td>
</tr>
</tbody>
</table>

<h2>一般的なケースの置き方</h2>
<table>
<thead>
<tr>
<th>見つけたもの</th>
<th>最初に置く場所</th>
<th>サポート付きで閲覧できるページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>中学生向け説明</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki">wiki</a></td>
<td><a href="https://mind-upload.com/content_hub.html">コンテンツハブ</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide">公開ページ閲覧ガイド</a></td>
</tr>
<tr>
<td><strong>既存の申し立てに条件と注記がありません</strong></td>
<td><a href="https://mind-upload.com/issue.html">公開ページをターゲットに</a>を発行</td>
<td><a href="https://mind-upload.com/verification.html">検証</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">最初の問題の書き方</a></td>
</tr>
<tr>
<td><strong>新しい論文とデータセット</strong></td>
<td><a href="https://mind-upload.com/research_harvest_50.html">リサーチハーベスト</a>または<a href="https://mind-upload.com/datasets.html">データセット</a></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装および参加までの直線的なパス</a></td>
</tr>
<tr>
<td><strong>共同研究パートナーに引き渡す1ページの概要</strong></td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">との接続準備</a></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">社内生産と外部依存関係</a></td>
</tr>
<tr>
<td><strong>信憑性と場所がまだ特定されていない断片化されたメモ</strong></td>
<td>操作エリア</td>
<td><a href="https://mind-upload.com/content_hub.html">コンテンツハブ</a></td>
</tr>
</tbody>
</table>

<h2>よくある間違い</h2>

<h4>間違い</h4>
<ul>
<li><strong>とりあえず新しいページを作成する:</strong> まず、既存のページに統合できるかどうかを確認します。 </li>
<li><strong>公開ページを教科書化する:</strong> 詳しい説明をwikiに投稿していただくと入り口が分かりやすくなります。 </li>
<li><strong>混合問題とコラボレーション:</strong> 外部依存関係から今すぐ実行できる個別の変更。 </li>
<li><strong>未整理のメモをそのまま公開する：</strong> まずは業務領域で整理してからどこに統合するかを決める方が安全です。 </li>
</ul>

<h2>次に戻る場所</h2>
<p>
統合先一覧に戻る場合は<a href="https://mind-upload.com/content_hub.html">パブリックコンテンツ統合ハブ</a>、参加ルートに戻る場合は<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes">参加・連携ページ以降に進むべき5つの道</a>、課題の書き方に戻る場合は<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">最初の課題の書き方</a>をご利用ください。
</p>
