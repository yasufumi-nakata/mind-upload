---
layout: default
title: 'Wiki: 最初に行うべき社内依存関係と外部依存関係の区別'
description: これは、このリポジトリ内で実行できることと、パートナーやシステムが必要なものを区別するための、問題、共同研究、実験、標準化提案の補助ページです。
article_type: ウィキ
subtitle: 「相手を待つ」ように見える作業を準備作業に分解する
author: マインドアップロード研究プロジェクト
last_updated: '2026-03-14'
note: 操作ガイド
audience: 課題を書いたり、共同研究候補を検討したり、今何が変えられるかを整理したい人。
reading_time: 8～12分
page_intro: このページは、Mind-Upload の運用で何度も出てくる「外部依存関係」を、停止理由ではなく分解対象として読むための補助ページです。ここでの焦点は、このリポジトリで最初に作成できるものと、パートナーやシステムが必要なものとを区別することです。
accuracy_note: このページは、作業を分離するのに役立ちます。このページだけでは、実際の契約、契約、治験審査委員会、または機器の使用が確立されることを保証するものではありません。
page_highlights:
- 外部の依存関係を何もできない箱として放置せず、社内での準備に分割してください。
- 課題、共同研究、実験、標準化提案に共通する最低限の準備を整理します。
- このリポジトリで今すぐ完了できる変更と、別のトラックで管理する必要がある作業を分けてください。
known_points:
- 外部に依存する業務であっても、要件仕様書や判定条件、公開ログフォーマット、比較表などをまず社内で作成することが可能です。
- 相手にアプローチする前に、最低限の成果物と依頼内容を1ページに整理しておくとスムーズに進みます。
- 課題でも共同研究でも、今何ができるかを明確にすることが大切です。
unknown_points:
- どの外部候補者が実際に合意するか、またどのような条件で合意するかは、相手側の要因によって決まります。
- IRB、契約、資金調達、および機器の入手可能時期は、このページの外で決定されます。
wiki_links:
- label: 'Wiki: 提案と状態ラベルの読み方'
  url: /wiki/proposal-status-reading.html
  description: まずは提案、文書反映、外部依存などの段階での違いを整理していきます。
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: 要件仕様書と判定条件を最初に作成する理由を説明します。
- label: ウィキホーム
  url: /wiki/
  description: 他の補助ページに戻ることができます。
recommended_pages:
- label: 貢献ガイド
  url: /issue.html
- label: 連携候補者
  url: /issue.html#external-collaboration
- label: 検証ベース
  url: /verification.html
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>最初に共有したいこと</h2>
<p>
外部に依存するタスクは、<strong> だけでは完了できない作業です。ただし、<strong> が私たちのために何もできないというわけではありません。リクエスト前の準備や判定条件、公開ログ形式、比較表などを事前に準備できます。
</p>
</div>

<div class="note-box">
<strong>参加ページの次のページを決めたい場合</strong>
<p>
「問題とコラボレーション」を読んだ後、小さな変更、条件設計、文献からの作業、または L0 実装の準備に進むべきかどうかを 1 ページで確認したい場合は、<a href="participation-next-routes.html"> 参加/コラボレーション後にたどるべき 5 つのパス ページ</a> を参照してください。
</p>
</div>

<section class="section" id="two-columns">
<h2 class="section-title">社内プロダクションと外部の依存関係を 2 列で読み取ります</h2>
<table class="data-table">
<thead>
<tr>
<th>タイプ</th>
<th>このリポジトリでできること</th>
<th>外部依存になる</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>実験</strong></td>
<td>要求仕様書、評価指標、停止条件、公開ログフォーマット、事前登録案を作成できます。 </td>
<td>IRB、被験者の募集、機器の使用、測定データの取得は外部関係者に依存しています。 </td>
</tr>
<tr>
<td><strong>共同研究</strong></td>
<td>1ページのサマリー、最低限の成果物、リクエスト範囲、比較表、再分析計画を作成できます。 </td>
<td>共著者契約、契約、パートナーの承認、およびデータ共有条件は外部に依存します。 </td>
</tr>
<tr>
<td><strong>標準化提案</strong></td>
<td>仕様案、差分表、サンプルログ、想定ユースケースを作成できます。 </td>
<td>コミュニティの採用、公式仕様の反映、外部レビューは外部に依存します。 </td>
</tr>
<tr>
<td><strong>資金/制度</strong></td>
<td>目的、最低限の範囲、成果物、必要な予算を整理できます。 </td>
<td>採用、予算配分、法的決定、およびシステム設計に関する正式な決定は外部に依存します。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="prework-pack">
<h2 class="section-title">外部依存関係がある場合でも最初に行う必要がある最小限の準備</h2>
<table class="data-table">
<thead>
<tr>
<th>準備</th>
<th>最低限の内容</th>
<th>なぜ必要なのか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1 ページの概要</strong></td>
<td>目的、相手に求めるもの、すでに持っているもの。 </td>
<td>相手が何を言っているのかをすぐに判断できるようにするためです。 </td>
</tr>
<tr>
<td><strong>最小納品物</strong></td>
<td>この定義では、最小範囲が 1 つに絞り込まれます。 </td>
<td>ご要望が大きすぎる場合、初期合意に達することが困難になります。 </td>
</tr>
<tr>
<td><strong>判定条件</strong></td>
<td>前に進むにはどうすればいいですか？何を保留すべきでしょうか？失敗するにはどうすればいいでしょうか？ </td>
<td>ストーリーの進行に伴って目的が移動するのを防ぐためです。 </td>
</tr>
<tr>
<td><strong>出版準備</strong></td>
<td>仕様案、QCログ例、比較表、BIDSテンプレート、チェックリスト。 </td>
<td>本気度や具体性が伝わりやすいからです。 </td>
</tr>
<tr>
<td><strong>外部依存関係の境界</strong></td>
<td>治験審査委員会、設備、契約、法的事項、相手方の承認などの意思決定は誰が行う必要がありますか？ </td>
<td>これは、即時作業と待機中の作業を混同しないようにするためです。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="issue-vs-collab">
<h2 class="section-title">課題と共同研究のわずかな違い</h2>
<table class="data-table">
<thead>
<tr>
<th>シーン</th>
<th>まず直したいところ</th>
<th>外部依存関係となるもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>問題を作成するとき</strong></td>
<td>どこで止まったのか、何が足りなかったのか、進歩の条件、そして反証の条件。 </td>
<td>実験や法務が必要な場合は別トラックとして切り出します。 </td>
</tr>
<tr>
<td><strong>共同研究候補を見る場合</strong></td>
<td>相手にお願いしたいことの範囲と、最初に制作できる成果物。 </td>
<td>契約、共著、データ使用条件、機器使用条件はそのまま残ります。 </td>
</tr>
<tr>
<td><strong>標準化提案提出時</strong></td>
<td> の差異表、サンプル、現行規格に不足している点。 </td>
<td> は引き続きコミュニティのレビューと正式な採用の対象となります。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある混乱</h2>
<div class="key-points">
<h4>誤読</h4>
<ul>
<li><strong>「外部ソースに依存するため、今は何もしない」:</strong> 仕様、比較表、ログ形式、最小限の成果物を最初に作成できます。 </li>
<li><strong>「書面だから進んでいる」：</strong> 相手に引き渡すための下準備と、実際に合意が得られることは別のことです。 </li>
<li><strong>「計画は大きければ大きいほど良い」:</strong> 最初に最低限の範囲を切り詰めないと、要望も課題もうまくいきません。 </li>
<li><strong>「本文では外部依存関係を完全なものとして扱う」:</strong> これは特に避けるべきであり、証跡のある社内変更とは別に記述する必要があります。 </li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
課題の書き方に戻るには<a href="../issue.html">貢献ガイド</a>に、共同研究候補者をまとめるには<a href="../issue.html#external-collaboration">連携候補</a>に、要件仕様や判断条件を固めるには<a href="../verification.html">検証プラットフォーム</a>に戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="proposal-status-reading.html">提案書とステータスラベルの見方→</a></li>
<li><a href="verification-basics.html">検証基盤の基礎→</a></li>
<li><a href="roadmap-reading-guide.html">ロードマップの見方→</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../issue.html">投稿ガイド→</a></li>
<li><a href="../issue.html#external-collaboration">連携候補→</a></li>
<li><a href="../verification.html">検証インフラ→</a></li>
</ul>
</div>
</aside>
</main>
