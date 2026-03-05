---
layout: default
title: "Wiki：意識理論マップ"
description: "IIT、GNWT、FEP、PCI がそれぞれ何を説明したいのか、どう違い、どこまで言えるかを整理する補助ページです。"
article_type: Wiki
subtitle: "理論名を覚えるより、役割の違いを先に分ける"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Theory guide"
audience: "IIT、GNWT、FEP、PCI の違いで止まりやすい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload でよく出る意識理論や意識指標を、初学者向けに役割ごとへ整理する補助ページです。どれが正しいと決めるためではなく、『何を説明したい理論か』『何をまだ説明しきれていないか』を先に分けることを目標にします。"
accuracy_note: "ここでは理論を噛み砕いて説明しますが、どの理論も最終決着したとは扱いません。支持点と限界を分けて読みます。"
page_highlights:
  - "IIT、GNWT、FEP、PCI は、同じものを同じ仕方で説明するわけではありません。"
  - "理論と指標を分けるだけで、議論の混線はかなり減ります。"
  - "Mind-Upload では、理論を教条的に採るのではなく、設計条件や評価指標へ落とす立場です。"
known_points:
  - "IIT と GNWT は意識をどう説明するかの理論、PCI は測定指標、FEP は実装原理寄りの枠組みです。"
  - "どの理論も単独で決定打になったとは言えません。"
  - "理論どうしの違いを分けて読むと、何が検証対象で何が作業仮説かが見えやすくなります。"
unknown_points:
  - "どの理論の組み合わせが、最終的に WBE の十分条件へつながるかは未確定です。"
  - "機能的等価性と現象的意識の関係を、どの理論がどこまで説明できるかは未解決です。"
wiki_links:
  - label: "Wiki: 本人性とコピー問題"
    url: "/wiki/personhood-and-copy-problem.html"
    description: "理論から本人性問題へ進むときの補助です。"
  - label: "Wiki: 文献と証拠ページの読み方"
    url: "/wiki/literature-and-evidence-reading.html"
    description: "理論論文をどこまで深読みするかの補助になります。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "研究ノート"
    url: "/perspective.html"
  - label: "理論フレーム"
    url: "/idea.html"
  - label: "用語集"
    url: "/glossary.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず大ざっぱに分ける</h2>
<p>
IIT、GNWT、FEP、PCI は、全部が同じ種類のものではありません。理論、実装原理、測定指標が混ざっているので、まず役割を分けるだけでかなり読みやすくなります。
</p>
</div>

<section class="section" id="roles">
<h2 class="section-title">まずは役割で分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>名前</th>
<th>ざっくり何か</th>
<th>主に説明したいこと</th>
<th>Mind-Upload での使い方</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT</strong></td>
<td>意識理論</td>
<td>意識の質や統合された因果構造を説明したい。</td>
<td>因果構造保存のものさし候補として参照します。</td>
</tr>
<tr>
<td><strong>GNWT</strong></td>
<td>意識理論</td>
<td>情報の広域共有と報告可能性を説明したい。</td>
<td>広域共有やアクセスの作業仮説として参照します。</td>
</tr>
<tr>
<td><strong>FEP</strong></td>
<td>包括的な枠組み / 実装原理寄り</td>
<td>システムが環境に適応しながら安定に推論することを説明したい。</td>
<td>閉ループで動く実装原理として使います。</td>
</tr>
<tr>
<td><strong>PCI</strong></td>
<td>測定指標</td>
<td>摂動に対する複雑な応答を定量化したい。</td>
<td>理論に依存しすぎない経験的な評価指標として使います。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="limits">
<h2 class="section-title">それぞれの強みと弱み</h2>
<table class="data-table">
<thead>
<tr>
<th>名前</th>
<th>強み</th>
<th>弱み / 注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT</strong></td>
<td>因果構造や統合性を強く意識させる。</td>
<td>計算量が重く、Unfolding Argument などの批判がある。</td>
</tr>
<tr>
<td><strong>GNWT</strong></td>
<td>広域共有や報告可能性との関係を考えやすい。</td>
<td>報告動作と意識そのものの区別が難しいことがある。</td>
</tr>
<tr>
<td><strong>FEP</strong></td>
<td>動き続けるシステムの実装原理として読みやすい。</td>
<td>抽象度が高く、何でも説明したように見えやすい。</td>
</tr>
<tr>
<td><strong>PCI</strong></td>
<td>理論を一つに決めなくても測定しやすい。</td>
<td>指標そのものが、意識の全体像を説明するわけではない。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-site-uses">
<h2 class="section-title">Mind-Upload ではどう使い分けるか</h2>
<p>
このサイトは、どれか1つを「唯一の正解」として採る立場ではありません。むしろ、IIT や GNWT を理論的なものさしとして見つつ、FEP を実装原理の候補として参照し、PCI のような経験的指標で検証を進める、という役割分担を取ります。
</p>
<div class="note-box">
<strong>大事なこと</strong>
<p>
理論を採ることと、理論がすでに証明されたとみなすことは別です。Mind-Upload では、理論を検証設計へ落とすために使います。
</p>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
理論全体を長文で追いたい場合は <a href="../perspective.html">研究ノート</a>、設計原理として見たい場合は <a href="../idea.html">理論フレーム</a>、単語を短く確認したい場合は <a href="../glossary.html">用語集</a> に戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="personhood-and-copy-problem.html">本人性とコピー問題 →</a></li>
<li><a href="decode-vs-emulate.html">Decode と Emulate →</a></li>
<li><a href="mind-upload-basics.html">WBEの基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../perspective.html">研究ノート →</a></li>
<li><a href="../idea.html">理論フレーム →</a></li>
<li><a href="../glossary.html">用語集 →</a></li>
</ul>
</div>
</aside>
</main>
