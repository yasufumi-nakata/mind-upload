---
layout: default
title: "Wiki：新しい情報の置き場所を決める基本"
description: "新しく見つけた説明、文献、修正案、外部依存タスクを、公開ページ、wiki、Issue、Collaborations、運用領域のどこへ置くべきかを初歩から整理するガイドです。"
article_type: Wiki
subtitle: "『何を書くか』の前に、『どこへ置くか』を決めるための基本"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Content placement basics"
audience: "新しい情報の統合先で迷う人、公開ページと wiki の役割差を初歩から知りたい人"
reading_time: "8〜12分"
page_intro: "このページは、Mind-Upload に新しい情報を足すときに、どこへ置くべきかを初歩から整理する補助教材です。公開ページは情報ポータル、wiki は学習用の詳説、Issue は実行する変更、Collaborations は外部依存の整理、運用領域は中間成果という役割差を、例と一緒に確認できます。"
accuracy_note: "ここで示すのは置き場所の基本です。個別の主張の正しさや採否は、必ず元ページの本文と根拠へ戻って判断してください。"
page_highlights:
  - "公開ページ、wiki、Issue、Collaborations、運用領域の役割差を初歩から整理します。"
  - "『とりあえず新規ページを作る』前に、既存の統合先を判断しやすくします。"
  - "公開ページをポータルとして保ちつつ、学習用の厚みは wiki へ寄せる方針を具体化します。"
known_points:
  - "置き場所を先に決めると、情報の重複や導線の散逸が減ります。"
  - "公開ページと wiki を分けると、入口の見やすさと説明の厚みを両立しやすいです。"
  - "外部依存タスクは、今この場で実行する変更とは分けて管理する必要があります。"
unknown_points:
  - "どの論点が将来独立ページになるかは、蓄積量と読者需要で変わります。"
  - "一部の話題は複数ページにまたがるため、最終的な統合先は今後も調整されます。"
wiki_links:
  - label: "Wiki: 公開ページの読み分けガイド"
    url: "/wiki/public-page-reading-guide.html"
    description: "公開ページどうしの役割差を先に見たい人向けです。"
  - label: "Wiki: 参加・協業ページのあとに進む5つの道"
    url: "/wiki/participation-next-routes.html"
    description: "置き場所の判断後に、次の作業へ進みたい人向けです。"
  - label: "Wiki: はじめての Issue の書き方"
    url: "/wiki/issue-writing-basics.html"
    description: "置き場所が Issue になったときの書き方を補います。"
recommended_pages:
  - label: "公開コンテンツ統合ハブ"
    url: "/content_hub.html"
  - label: "貢献ガイド"
    url: "/issue.html"
  - label: "協業候補"
    url: "/issue.html#external-collaboration"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>最初に決めるのは「内容」より「置き場所」です</h2>
<p>
新しい情報を見つけたとき、すぐ本文を書き始めると重複や迷子が増えます。先に<strong>その情報の役割</strong>を決めると、公開ページをポータルとして保ちつつ、必要な詳説を wiki へ増やしやすくなります。
</p>
</div>

<section class="section" id="five-places">
<h2 class="section-title">まずは 5 つの置き場所を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>置き場所</th>
<th>何を置くか</th>
<th>置かない方がよいもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>公開ページ</strong></td>
<td>いま分かっていること、まだ分かっていないこと、次に読む場所、判断表。</td>
<td>背景知識を最初から最後まで教える長い教材。</td>
</tr>
<tr>
<td><strong>wiki</strong></td>
<td>初歩の説明、似た言葉の違い、ページの読み方、学習用の補助教材。</td>
<td>最新の運用判断や実装状況の一次置き場。</td>
</tr>
<tr>
<td><strong>Issue</strong></td>
<td>今このリポジトリで実行する変更、修正位置、前進条件、反証条件。</td>
<td>外部依存を含む大きな計画を、完了済みのように書くこと。</td>
</tr>
<tr>
<td><strong>Collaborations</strong></td>
<td>共同研究、標準化提案、制度連携など、相手先や外部条件が必要な話。</td>
<td>こちらだけで完了できる小さな修正の記録。</td>
</tr>
<tr>
<td><strong>運用領域</strong></td>
<td>未整理メモ、中間成果、CSV、機械処理結果、監査ログ。</td>
<td>そのまま読者向け本文として見せること。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="by-question">
<h2 class="section-title">その情報が何に答えるかで置き場所を決める</h2>
<table class="data-table">
<thead>
<tr>
<th>その情報が答える問い</th>
<th>まず置く先</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>この分野で、いま何が分かっていて何が未解決か</strong></td>
<td><a href="../verification.html">Verification</a>、<a href="../tech_roadmap.html">Roadmap</a> などの公開ページ</td>
<td>公開ページは、判断の入口として既知/未知を示す役割だからです。</td>
</tr>
<tr>
<td><strong>用語や背景知識を初歩から説明したい</strong></td>
<td><a href="../wiki/">wiki</a></td>
<td>学習用の厚みは wiki に寄せた方が、入口ページが見やすく保てるからです。</td>
</tr>
<tr>
<td><strong>今すぐ直せる修正を切りたい</strong></td>
<td><a href="../issue.html">Issue</a></td>
<td>実行可能な変更として、完了条件まで含めて管理できるからです。</td>
</tr>
<tr>
<td><strong>共同研究や標準化の候補を整理したい</strong></td>
<td><a href="../issue.html#external-collaboration">Collaborations</a></td>
<td>外部依存の話を、内製変更と混ぜないためです。</td>
</tr>
<tr>
<td><strong>まだ整理し切れていない生データやメモを残したい</strong></td>
<td>運用領域</td>
<td>統合先が決まる前の断片を、公開本文へ直接流し込まないためです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-cases">
<h2 class="section-title">よくあるケースの置き方</h2>
<table class="data-table">
<thead>
<tr>
<th>見つけたもの</th>
<th>まず置く先</th>
<th>補助で見るページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>中学生向けに噛み砕いた説明</strong></td>
<td><a href="../wiki/">wiki</a></td>
<td><a href="../content_hub.html">Content Hub</a> / <a href="public-page-reading-guide.html">公開ページの読み分けガイド</a></td>
</tr>
<tr>
<td><strong>既存の主張に足りない条件や注意書き</strong></td>
<td><a href="../issue.html">Issue</a> から対象公開ページへ</td>
<td><a href="../verification.html">Verification</a> / <a href="issue-writing-basics.html">はじめての Issue の書き方</a></td>
</tr>
<tr>
<td><strong>新しい論文やデータセット</strong></td>
<td><a href="../research_harvest_50.html">Research Harvest</a> か <a href="../datasets.html">Datasets</a></td>
<td><a href="literature-to-action-route.html">文献から実装・参加へ戻る一本道</a></td>
</tr>
<tr>
<td><strong>共同研究先へ渡す 1 ページ要約</strong></td>
<td><a href="../issue.html#external-collaboration">Collaborations</a> に接続する準備物</td>
<td><a href="internal-prework-and-external-dependencies.html">内製で先にやることと外部依存</a></td>
</tr>
<tr>
<td><strong>まだ真偽や置き場が決まっていない断片メモ</strong></td>
<td>運用領域</td>
<td><a href="../content_hub.html">Content Hub</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="mistakes">
<h2 class="section-title">よくある失敗</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>とりあえず新規ページを作る：</strong> まず既存ページに統合できるかを確認してください。</li>
<li><strong>公開ページを教科書化する：</strong> 詳説は wiki へ寄せた方が入口が見やすくなります。</li>
<li><strong>Issue と Collaborations を混ぜる：</strong> 今できる変更と外部依存を分けてください。</li>
<li><strong>未整理メモをそのまま公開する：</strong> まず運用領域で整理してから統合先を決める方が安全です。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
統合先の一覧へ戻るなら <a href="../content_hub.html">公開コンテンツ統合ハブ</a>、参加導線へ戻るなら <a href="participation-next-routes.html">参加・協業ページのあとに進む5つの道</a>、Issue に落とし込む書き方へ戻るなら <a href="issue-writing-basics.html">はじめての Issue の書き方</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="public-page-reading-guide.html">公開ページの読み分けガイド →</a></li>
<li><a href="participation-next-routes.html">参加・協業ページのあとに進む5つの道 →</a></li>
<li><a href="issue-writing-basics.html">はじめての Issue の書き方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../content_hub.html">公開コンテンツ統合ハブ →</a></li>
<li><a href="../issue.html">貢献ガイド →</a></li>
<li><a href="../issue.html#external-collaboration">協業候補 →</a></li>
</ul>
</div>
</aside>
</main>
