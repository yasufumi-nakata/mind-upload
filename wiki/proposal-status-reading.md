---
layout: default
title: 'Wiki: 提案とステータス ラベルの見方'
description: これは、提案、承認、文書反映、実装、外部依存関係の違いを整理し、提案ページと論点の誤読を避けるための補助ページです。
article_type: ウィキ
subtitle: 「採用」と「採用」は別物
author: マインドアップロード研究プロジェクト
last_updated: '2026-03-14'
note: 読書ガイド
audience: 提案ページや課題ステータスラベルを理解するのが難しい人
reading_time: 8～12分
page_intro: このページは、Mind-Upload の提案ページと問題ページに表示されるステータス ラベルの読み間違いを防ぐための補助ページです。提案が受理されて実装されることと、外部合意が完了することには違いがありますので、その違いを日常用語で説明します。
accuracy_note: ここでの説明は読みやすくするためのものです。必ず提案ページに戻って発行履歴を確認し、個々の提案の最新ステータスを確認してください。
page_highlights:
- 提案、承認、ドキュメントの反映、実装、および外部依存関係が別の段階として説明されます。
- どのラベルを見れば、次にどこに戻ればよいかがわかります。
- これは、本文にあるから完結していると思わないための補助です。
known_points:
- 提案の受け入れや文書の反映は、自動的にコードや共同研究の完了を意味するものではありません。
- 外部に依存するタスクについては、自分側の準備と相手側の契約を別々に読む必要があります。
- ステータスラベルは、実装および出版の場所を示すものであり、科学的確実性自体を示すものではありません。
unknown_points:
- 各提案が最終的にどの程度実施されるかは、作業が進むにつれて変わる可能性があります。
- 外部依存タスクの完了タイミングや完了条件はラベルだけでは保証できません。
wiki_links:
- label: 'Wiki: 文献と証拠のページの読み方'
  url: /wiki/literature-and-evidence-reading.html
  description: 提案書ページと文献ページの違いを補います。
- label: 'Wiki: 社内および外部の依存関係について最初に行うべきこと'
  url: /wiki/internal-prework-and-external-dependencies.html
  description: この本は、外部依存関係を今すぐに実行できる準備作業に分解したい人向けです。
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: 達成条件と不確認条件が最初に配置される理由がわかります。
- label: ウィキホーム
  url: /wiki/
  description: 他の基本ページに戻ることができます。
recommended_pages:
- label: 技術提案
  url: /issue.html#proposal-integration
- label: 貢献ガイド
  url: /issue.html
- label: 検証ベース
  url: /verification.html
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず区別したいのは</h2>
<p>
提案書のページでは、さまざまな段階が「`accepted as a good idea,'' ``written in the main text,'' ``worked into code,'' and `『外部の同意を得て完了』となっている。」この区別があいまいであると、進行中の作業とまだ保留中の作業が混同されます。
</p>
</div>

<section class="section" id="labels">
<h2 class="section-title">日常の言葉で状態ラベルを作成する</h2>
<table class="data-table">
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
</section>

<section class="section" id="what-not-mean">
<h2 class="section-title">ラベルの意味しない</h2>
<div class="key-points">
<h4>意味がない</h4>
<ul>
<li><strong>提案受諾:</strong> これは、提案が科学的に完全に正しいことを意味するものではありません。 </li>
<li><strong>文書反映:</strong> これで実施・共同研究が終了したわけではありません。 </li>
<li><strong>実装済み:</strong> 社会実装やシステム開発が完了しているわけではありません。 </li>
</ul>
</div>
</section>

<section class="section" id="where-to-return">
<h2 class="section-title">どこに戻ればいいですか</h2>
<table class="data-table">
<thead>
<tr>
<th>知りたい</th>
<th>戻る</th>
</tr>
</thead>
<tbody>
<tr>
<td>提案内容と根拠</td>
<td><a href="../issue.html#proposal-integration">技術提案</a></td>
</tr>
<tr>
<td>今誰が何を助けることができますか?</td>
<td><a href="../issue.html">貢献ガイド</a></td>
</tr>
<tr>
<td>達成条件と反証条件の仮定</td>
<td><a href="../verification.html">検証インフラストラクチャ</a></td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>外部依存関係が「待ちボックス」になるのを避けるため </strong>
<p>
このページではステージの違いについて説明します。外部依存関係になった後に最初に作成できるものを整理したい場合は、<a href="internal-prework-and-external-dependencies.html">Wiki: 社内で最初に行うことと外部依存関係の分離</a> を参照してください。
</p>
</div>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="literature-and-evidence-reading.html">文献・エビデンスページの見方→</a></li>
<li><a href="verification-basics.html">検証基盤の基礎→</a></li>
<li><a href="roadmap-reading-guide.html">ロードマップの見方→</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../issue.html#proposal-integration">技術提案→</a></li>
<li><a href="../issue.html">投稿ガイド→</a></li>
<li><a href="../verification.html">検証インフラ→</a></li>
</ul>
</div>
</aside>
</main>
