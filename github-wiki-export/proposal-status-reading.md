# Wiki: 提案とステータス ラベルの見方

> 「採用」と「採用」は別物
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-14 / Role: 読書ガイド

## このページの役割
このページは、Mind-Upload の提案ページと問題ページに表示されるステータス ラベルの読み間違いを防ぐための補助ページです。提案が受理されて実装されることと、外部合意が完了することには違いがありますので、その違いを日常用語で説明します。

## 正確性に関する注記
ここでの説明は読みやすくするためのものです。必ず提案ページに戻って発行履歴を確認し、個々の提案の最新ステータスを確認してください。

## 公開ページへ戻る
- [技術提案](https://mind-upload.com/issue.html#proposal-integration)
- [貢献ガイド](https://mind-upload.com/issue.html)
- [検証ベース](https://mind-upload.com/verification.html)

## 関連 Wiki ページ
- [Wiki: 文献と証拠のページの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - 提案書ページと文献ページの違いを補います。
- [Wiki: 社内および外部の依存関係について最初に行うべきこと](https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies) - この本は、外部依存関係を今すぐに実行できる準備作業に分解したい人向けです。
- [Wiki: 検証インフラストラクチャの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 達成条件と不確認条件が最初に配置される理由がわかります。
- [ウィキホーム](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基本ページに戻ることができます。

## 現在わかっていること
- 提案の受け入れや文書の反映は、自動的にコードや共同研究の完了を意味するものではありません。
- 外部に依存するタスクについては、自分側の準備と相手側の契約を別々に読む必要があります。
- ステータスラベルは、実装および出版の場所を示すものであり、科学的確実性自体を示すものではありません。

## まだわかっていないこと
- 各提案が最終的にどの程度実施されるかは、作業が進むにつれて変わる可能性があります。
- 外部依存タスクの完了タイミングや完了条件はラベルだけでは保証できません。

---

<h2>まず区別したいのは</h2>
<p>
提案書のページでは、さまざまな段階が「`accepted as a good idea,'' ``written in the main text,'' ``worked into code,'' and `『外部の同意を得て完了』となっている。」この区別があいまいであると、進行中の作業とまだ保留中の作業が混同されます。
</p>

<h2>日常の言葉で状態ラベルを作成する</h2>
<table>
<thead>
<tr>
<th>ラベルタイプ</th>
<th>日常用語</th>
<th>残り</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>提案書を公開</strong></td>
<td> 提案として提出されており、議論が行われています。 </td>
<td>有効性と優先度の検証は残ります。 </td>
</tr>
<tr>
<td><strong>提案受理・方針反映</strong></td>
方向性としては<td>を取る価値があると判断しました。 </td>
<td>の実施方法、検証条件、公表資料が残っています。 </td>
</tr>
<tr>
<td><strong>ドキュメントの反射</strong></td>
<td>状態は本文記載の通りです。 </td>
<td>コード、データ、ログが不完全な可能性があります。 </td>
</tr>
<tr>
<td><strong>実装済み</strong></td>
<td>実際に動くものがある状態です。 </td>
<td>別途第三者による追加検査や監査が必要となる場合があります。 </td>
</tr>
<tr>
<td><strong>外部依存関係</strong></td>
<td>一人では完結できませんのでご了承ください。パートナーとシステムが必要です。 </td>
<td>協定、契約、実験、資金などが残っています。 </td>
</tr>
</tbody>
</table>

<h2>ラベルの意味しない</h2>

<h4>意味がない</h4>
<ul>
<li><strong>提案受諾:</strong> これは、提案が科学的に完全に正しいことを意味するものではありません。 </li>
<li><strong>文書反映:</strong> これで実施・共同研究が終了したわけではありません。 </li>
<li><strong>実装済み:</strong> 社会実装やシステム開発が完了しているわけではありません。 </li>
</ul>

<h2>どこに戻ればいいですか</h2>
<table>
<thead>
<tr>
<th>知りたい</th>
<th>戻る</th>
</tr>
</thead>
<tbody>
<tr>
<td>提案内容と根拠</td>
<td><a href="https://mind-upload.com/issue.html#proposal-integration">技術提案</a></td>
</tr>
<tr>
<td>今誰が何を助けることができますか?</td>
<td><a href="https://mind-upload.com/issue.html">貢献ガイド</a></td>
</tr>
<tr>
<td>達成条件と反証条件の仮定</td>
<td><a href="https://mind-upload.com/verification.html">検証インフラストラクチャ</a></td>
</tr>
</tbody>
</table>

<strong>外部依存関係が「待ちボックス」になるのを避けるため </strong>
<p>
このページではステージの違いについて説明します。外部依存関係になった後に最初に作成できるものを整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">Wiki: 社内で最初に行うことと外部依存関係の分離</a> を参照してください。
</p>
