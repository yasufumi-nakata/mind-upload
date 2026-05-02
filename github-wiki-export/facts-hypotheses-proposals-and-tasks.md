# Wiki: 事実、仮説、提案、実行タスクの違い

> ページの役割を事実、仮説、提案、タスクごとに整理する
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: クレームの役割の読み取り

## このページの役割
このページは、Mind-Upload の各ページが同じタイプの議論ではないことを理解するのに役立つ補助ガイドです。観察、文献の整理、理論的な作業仮説、提案、このリポジトリで実行されるタスク、および外部依存関係の調整にはすべて、異なる役割と証拠の重みがあります。このページを使用して、これらの違いをまとめて読んでください。

## 正確性に関する注記
ここで扱っているのは、ページの役割の違いです。必ず各ページの本文と証拠に戻って、個々の理論や提案の妥当性を確認してください。

## 公開ページへ戻る
- [研究ノート](https://mind-upload.com/perspective.html)
- [理論的フレーム](https://mind-upload.com/perspective.html#design-principles)
- [技術提案](https://mind-upload.com/issue.html#proposal-integration)

## 関連 Wiki ページ
- [Wiki: 公開ページを読むためのガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - これは、最初にページ間の役割の違いを確認したい人向けです。
- [Wiki: 提案と状態ラベルの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading) - さらに詳しく知りたい人は、提案ページのステータス ラベルを確認してください。
- [Wiki: 最初の問題の書き方](https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics) - 実行タスクへの記述方法を補足します。

## 現在わかっていること
- 各ページは、観察、理論的仮説、提案、実装タスク、および外部依存関係に分かれています。
- 提案の受諾または文書の反映は、自動的に実装の完了または外部合意の完了を意味するものではありません。
- 実行可能な変化は、問題を解決するか実践して初めて具体的になります。

## まだわかっていないこと
- 最終的にどの仮説や提案が中心線として残るかは、今後の検証によって変わってくる。
- 対外依存の話がどこまで実際の協力に進むかは相手や状況次第だ。

---

<h2>「主張」は同じように見えても、その役割は同じではない</h2>
<p>
文献の整理、理論的メモ、設計原則、技術提案、問題点、およびコラボレーションの候補は、すべて同じ種類のテキストではありません。まず、<strong>どのページが記録されているか</strong>を分けることで、肯定の強さや次の行動を読み間違えにくくなります。
</p>

<h2>まずは5種類に分ける</h2>
<table>
<thead>
<tr>
<th>タイプ</th>
<th>何してるの</th>
<th>メインページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察・組織</strong></td>
<td>既知のことと未解決のことを記録します。 </td>
<td><a href="https://mind-upload.com/research_harvest_50.html">リサーチハーベスト</a> / <a href="https://mind-upload.com/mind_uploading_papers.html">論文</a> / <a href="https://mind-upload.com/verification.html#casework">ケースワーク</a></td>
</tr>
<tr>
<td><strong>仮説・理論フレーム</strong></td>
<td>Iでは、設計条件に適用しやすい考え方をご紹介します。 </td>
<td><a href="https://mind-upload.com/perspective.html">パースペクティブ</a> / <a href="https://mind-upload.com/perspective.html#design-principles">アイデア</a></td>
</tr>
<tr>
<td><strong>提案・方針</strong></td>
<td>どの方向に進み、どのストリームに編成するかを示します。 </td>
<td><a href="https://mind-upload.com/issue.html#proposal-integration">提案</a></td>
</tr>
<tr>
<td><strong>タスクの実行</strong></td>
<td>このリポジトリで行う変更、完了条件、および反証条件をカットします。 </td>
<td><a href="https://mind-upload.com/issue.html">問題</a> / <a href="https://mind-upload.com/datasets.html#l0-practice">実践</a></td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td>共同研究、標準化、治験審査委員会、設備、法務等の外部条件を必要とする業務を整理します。
<td><a href="https://mind-upload.com/issue.html#external-collaboration">コラボレーション</a></td>
</tr>
</tbody>
</table>

<h2>似ているページ間の違い</h2>
<table>
<thead>
<tr>
<th>ページ</th>
<th>主役</th>
<th>読み間違えやすい</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>遠近感</strong></td>
<td>A 文献と限界を整理することで、理論の裏付けとなる点と弱点を追跡する研究ノート。 </td>
<td>長い記事ですが、最終的な理論を宣言するものではありません。 </td>
</tr>
<tr>
<td><strong>アイデア</strong></td>
<td>採用する設計原則や作業仮説を絞り込むための理論フレームです。 </td>
<td>これは見解を要約したものであり、実験的に証明されたことを意味するものではありません。 </td>
</tr>
<tr>
<td><strong>提案</strong></td>
<td>これは、提案のステータス、流れ、根拠を追跡する組織図です。 </td>
<td>提案の受諾は、コードの実装や共同研究を意味するものではありません。 </td>
</tr>
<tr>
<td><strong>問題</strong></td>
<td>これは、今ここで実行される変更を完了条件付きで管理するためのエントリ ポイントです。 </td>
<td>大きな理論と外部依存関係を同じ箱で扱うと混乱を招きます。 </td>
</tr>
<tr>
<td><strong>コラボレーション</strong></td>
<td>外部依存関係の候補と連携前に必要な準備をまとめた実践的なページです。 </td>
<td>これは候補リストであり、合意されたリストではありません。 </td>
</tr>
</tbody>
</table>

<h2>自然な動き方</h2>
<table>
<thead>
<tr>
<th>今どこにいる</th>
<th>次の自然な目的地</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察・組織</strong></td>
<td><a href="https://mind-upload.com/perspective.html">パース</a> / <a href="https://mind-upload.com/issue.html#proposal-integration">提案</a></td>
<td>次のステップは、文献を整理し、それをどのように読み、どのような政策に使用するかを決定することです。 </td>
</tr>
<tr>
<td><strong>仮説/理論フレーム</strong></td>
<td><a href="https://mind-upload.com/verification.html">検証</a> / <a href="https://mind-upload.com/tech_roadmap.html">ロードマップ</a></td>
<td>仮説をそのまま設計条件や検証条件に落とし込む必要があるためです。 </td>
</tr>
<tr>
<td><strong>提案・方針</strong></td>
<td><a href="https://mind-upload.com/issue.html">問題</a> / <a href="https://mind-upload.com/datasets.html#l0-practice">実践</a></td>
<td>提案を実際の変更と最小限のループに変換します。 </td>
</tr>
<tr>
<td><strong>タスクの実行</strong></td>
<td><a href="https://mind-upload.com/content_hub.html">コンテンツハブ</a> / <a href="https://mind-upload.com/verification.html">検証</a></td>
<td>場所や完成条件を再確認しながら進めていきます。 </td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">社内生産と外部依存関係</a></td>
<td>まず社内でできる準備に分解する必要があるからです。 </td>
</tr>
</tbody>
</table>

<h2>よくある混乱</h2>

<h4>間違い</h4>
<ul>
<li><strong>理論フレームを事実のリストとして読む:</strong> アイデアには作業仮説が含まれています。 </li>
<li><strong>実装完了として提案ページを読む:</strong> 提案は概要表であり、完了レポートではありません。 </li>
<li><strong>問題を大きなアイデアに変える note:</strong> このリポジトリで有効期限が切れる変更に問題をドロップする方が安全です。 </li>
<li><strong>コラボレーションを TODO リストとして読む:</strong> すぐに実行できるリストではなく、潜在的な外部依存関係と準備をまとめたもの。 </li>
</ul>

<h2>次に戻る場所</h2>
<p>
公開ページ全体の役割の違いに戻りたい場合は<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide">公開ページの読み方</a>、提案ページのステータスに戻りたい場合は<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading">提案とステータスラベルの読み方</a>、実行タスクに変換したい場合は<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">最初の課題の書き方</a>をご利用ください。
</p>
