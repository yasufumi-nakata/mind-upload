---
layout: default
title: 'Wiki: ID とコピーの問題'
description: 「`copying'' and `」転送との違い、なぜ身元特定が難しいのか、何が未解決なのかを最初から明らかにします。
article_type: ウィキ
subtitle: 見た目は同じでも、同一人物かどうかは別問題です。
author: マインドアップロード研究プロジェクト
last_updated: '2026-03-14'
note: 初心者ガイド
audience: アイデンティティ、コピーの問題、継続的な移行について話すとすぐに止められる人
reading_time: 10～15分
page_intro: このページは、Mind-Uploadの議論でよく出てくる「`copying problem'' and `の真正性」を初期から整理したWikiです。哲学の固有名詞を覚える前に、なぜこの問題がテクノロジーから逃れられないのかを理解することを目指します。
accuracy_note: このページは分かりやすく解説しておりますが、その人物の身元について最終的な結論を導くページではありません。未解決のままであることを明確にします。
page_highlights:
- 「`acting the same way'' and `」と「同一人物」を区別してください。
- 静的コピーと継続的移行が異なる扱いを受ける理由を説明します。
- エンジニアリング ページに戻ると、テスト対象が表示されます。
known_points:
- たとえ行動が似ていても、それだけではその人の同一性を確認することはできません。
- 複数のコピーが存在する状況では、どれが本人であるかは自動的には判断されません。
- したがって、Mind-Upload では、連続性をどのように検証するかは別の問題として扱います。
unknown_points:
- 2 人の人物が「同一人物」とみなされる条件については合意がありません。
- 心理的連続性を重視するか、因果的連続性を重視するか、現象的意識を重視するかによって結論は変わります。
- また、継続的な移行設計がアイデンティティを適切に保護するかどうかも証明されていません。
wiki_links:
- label: 'Wiki: WBE の基本'
  url: /wiki/mind-upload-basics.html
  description: 全体像からこの問題の位置を確認することができます。
- label: 'Wiki: 主張と証拠の読み方'
  url: /wiki/claims-and-evidence.html
  description: L4 の ID 主張の強さを補います。
- label: 'Wiki: アイデンティティ評価と連続性テスト'
  url: /wiki/identity-and-continuity-tests.html
  description: 哲学的な問題を整理して、事前に登録したテスト設計に戻します。
- label: ウィキホーム
  url: /wiki/
  description: 他の基本ページに戻ることができます。
recommended_pages:
- label: 理論フレーム
  url: /perspective.html#design-principles
- label: WBE の概要
  url: /wbe_101.html
- label: 検証プラットフォーム
  url: /verification.html
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>第一区別</h2>
<p>
たとえ他の人とまったく同じ話し方、同じ記憶、同じ反応をしたとしても、それだけで同じ人間であるとは限りません。 Mind-Upload では、この違いが曖昧になることを避けるために、<strong> パフォーマンス マッチング </strong> と <strong> アイデンティティ アサーション </strong> を異なるレベルとして扱います。
</p>
</div>

<section class="section" id="why-hard">
<h2 class="section-title">なぜ難しいのか</h2>
<table class="data-table">
<thead>
<tr>
<th>質問</th>
<th>なぜ難しいのか</th>
</tr>
</thead>
<tbody>
<tr>
<td>もし同じ思い出を共有できるとしたら、それは私でしょうか?</td>
<td>記憶の再現と経験の連続性は同じではない可能性があるからです。 </td>
</tr>
<tr>
<td>1枚のみの場合はご本人様</td>
<td>を2つ作成した場合、同じロジックではどちらが本人であるかを判断することは困難です。 </td>
</tr>
<tr>
<td>少しずつ交換した方が安全ですか？</td>
<td>連続遷移は直感的には強そうですが、十分条件かどうかはまだわかりません。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="copy-vs-transfer">
<h2 class="section-title">静的コピーと継続的移行の違い</h2>
<table class="data-table">
<thead>
<tr>
<th>考える</th>
<th>注目すべき点</th>
<th>残りの質問</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>静的コピー</strong></td>
<td>ある時点の構造や情報をコピーすること。 </td>
<td>複数枚持っているとどれが本人か分からなくなります。 </td>
</tr>
<tr>
<td><strong>継続的移行</strong></td>
<td>プロセスと対話を中断することなく引き継ぎます。 </td>
<td>連続性がアイデンティティの十分条件であるかどうかはまだ証明されていません。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-can-test">
<h2 class="section-title">エンジニアリングに戻り、何をテストしたいですか</h2>
<p>
この点を工学に戻しますと、単によく似ているかどうかだけを見るだけでは十分ではありません。事前に登録されたテストを通じて、記憶、価値観、学習履歴、状況の変化への対応の連続性を調べる必要があります。言い換えれば、哲学的な議論をそのまま放置するのではなく、</strong> のアイデンティティの主張を保留する原因となる失敗がどのようなものであるかを定義する方向に進みます。
</p>
<p>最初にテスト設計の概要を見たい場合は、<a href="identity-and-continuity-tests.html">Wiki: ID 評価と継続性テスト</a> が補足コースです。 </p>
<div class="cta-box">
<h4>次</h4>
<p>この問題を理論的なフレームとしてどのように扱うかをここで確認できます。 </p>
<a href="../perspective.html#design-principles">理論フレームへ→</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE 基本→</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方→</a></li>
<li><a href="roadmap-reading-guide.html">ロードマップの見方→</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../perspective.html#design-principles">理論フレーム→</a></li>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
<li><a href="../verification.html">検証インフラ→</a></li>
</ul>
</div>
</aside>
</main>