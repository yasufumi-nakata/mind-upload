---
layout: default
title: "Wiki：文献と証拠ページの読み方"
description: "論文集、文献地図、提案ページの違いと、どこまで深読みすべきかを整理する補助ページです。"
article_type: Wiki
subtitle: "『論文が多い』と『結論が強い』を混同しないために"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Reading guide"
audience: "論文集と文献地図の違いが分かりにくい人、どのページから入るか迷う人"
reading_time: "8〜12分"
page_intro: "このページは、Mind-Upload にある文献系ページの役割分担を整理する補助ページです。論文が多いページほど、役割を取り違えると読み方が崩れるため、『何をするページか』『どこまで確定扱いしないか』を先に説明します。"
accuracy_note: "このページは読み方の補助です。個別論文や個別提案の評価は、必ず元ページと元論文へ戻って確認してください。"
page_highlights:
  - "論文集は広く拾う入口、文献地図は未解決問題ごとの整理、提案ページは実装方針の統合です。"
  - "論文数、引用数、状態ラベルを、そのまま結論の強さと読まないための補助です。"
  - "技術・自然科学では、Badge や source_logged だけでなく evidence class を分け、demo と mechanistic boundary を混同しない必要があります。"
  - "どこで止めてよいか、どこまで原文へ戻るべきかを示します。"
  - "技術・自然科学の一次証拠を追うときは、年順ではなく論文集内の優先ルートから入る方が安全です。"
known_points:
  - "役割の違うページを分けると、量の多さと結論の強さを混同しにくくなります。"
  - "論文集、文献地図、提案ページは、それぞれ読む目的が異なります。"
  - "技術・自然科学では、source type と evidence class を分け、task demo の直後に mechanistic boundary paper を挟んだ方が読み違えを減らせます。"
  - "重要な判断は、要約ではなく元論文や元ページへ戻って行う必要があります。"
unknown_points:
  - "どの論文が最終的に中心的根拠として残るかは、今後の整理で変わる可能性があります。"
  - "source_logged などの状態は、後続の精査で更新されることがあります。"
wiki_links:
  - label: "Wiki: 文献のソース種別と状態ラベル"
    url: "/wiki/paper-source-types-and-evidence-status.html"
    description: "Scopus、arXiv、Review、Media、source_logged などの意味を整理します。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "証拠の強さを、何で見るべきかの前提を補います。"
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "各論文や提案が、全体のどの論点に当たるかを補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "文献地図"
    url: "/research_harvest_50.html"
  - label: "論文集"
    url: "/mind_uploading_papers.html"
  - label: "技術提案"
    url: "/issue.html#proposal-integration"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず役割を分ける</h2>
<p>
文献系ページは、全部が同じ役割ではありません。広く拾うページ、未解決問題ごとに整理するページ、提案として統合するページを分けることで、読者が「いま何を見ているのか」を見失いにくくしています。
</p>
</div>

<div class="note-box">
<strong>文献を読んだあとに次の1ページを決めたいとき</strong>
<p>
役割差だけでなく、論文や文献地図を読んだあとに未解決問題、提案、Issue、協業候補のどこへ戻るかを一本道で見たい場合は <a href="literature-to-action-route.html">文献から実装・参加へ戻る一本道</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>技術・自然科学の一次証拠だけ先に追いたいとき</strong>
<p>
<a href="../mind_uploading_papers.html">論文集</a> は broad archive なので、年順の先頭がそのまま技術フロンティア順とは限りません。decode、speech neuroprosthesis、ESI direct validation、maintenance-state のような技術ルートを先に見たい場合は、論文集内の <strong>技術・自然科学の優先ルート</strong> から入ってください。
</p>
</div>
<div class="note-box">
<strong>Badge と証拠クラスを分けたいとき</strong>
<p>
Scopus、arXiv、source_logged は入口や状態を示しますが、<strong>その論文が何を直接増やすか</strong>までは示しません。技術・自然科学の主導線では、direct validation、task-limited demo、mechanistic boundary / hidden-state evidence、dataset / benchmark / standard、review / context を別クラスとして読む必要があります。使い分けは <a href="paper-source-types-and-evidence-status.html">Wiki: 文献のソース種別・状態・証拠クラスの読み方</a> にまとめました。
</p>
</div>

<section class="section" id="which-page">
<h2 class="section-title">3つのページの違い</h2>
<table class="data-table">
<thead>
<tr>
<th>ページ</th>
<th>役割</th>
<th>ここでやること</th>
<th>ここだけではしないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>論文集</strong></td>
<td>広く拾う入口</td>
<td>年別の流れ、関連論文の存在、要約からの当たり付け。技術読者は優先ルートに加え、demo / validator / mechanistic boundary のどれかを見て主要一次文献へ入ります。</td>
<td>各論文の最終評価をここだけで確定すること。</td>
</tr>
<tr>
<td><strong>文献地図</strong></td>
<td>未解決問題ごとの整理</td>
<td>U番号ごとに、何が解けていて何が未解決かを見ます。技術読者は U ごとに evidence class を見分け、demo と ceiling-setting paper を混ぜないようにします。</td>
<td>引用数だけで結論の強さを決めること。</td>
</tr>
<tr>
<td><strong>技術提案</strong></td>
<td>実装方針の統合</td>
<td>どの提案があり、どの状態で、どこへ影響するかを追うこと。</td>
<td>提案受理を、そのまま実装完了と読むこと。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-deep">
<h2 class="section-title">どこまで深読みするか</h2>
<table class="data-table">
<thead>
<tr>
<th>見ているもの</th>
<th>その場で止めてよい</th>
<th>原文へ戻るべき</th>
</tr>
</thead>
<tbody>
<tr>
<td>論文カード</td>
<td>自分の論点と遠いと分かった時点。</td>
<td>方法、評価、限界を根拠として使いたいとき。</td>
</tr>
<tr>
<td>U番号の現状マップ</td>
<td>どの U が自分に関係するか分かった時点。</td>
<td>本当にその U にその文献が効くか確認したいとき。</td>
</tr>
<tr>
<td>提案の要約表</td>
<td>関係するストリームと状態が分かった時点。</td>
<td>採否や妥当性を判断したいとき。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="three-rules">
<h2 class="section-title">読み違えを防ぐ4つのルール</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>量と強さを混同しない：</strong> 論文数や引用数は、結論の確定とは別です。</li>
<li><strong>Badge と証拠クラスを混同しない：</strong> Scopus / arXiv / source_logged は入口や状態であり、direct validation、system demo、mechanistic boundary は別軸です。</li>
<li><strong>要約で止めすぎない：</strong> 根拠として使うときは、必ず DOI や原文へ戻ります。</li>
<li><strong>状態ラベルを読み違えない：</strong> source_logged、提案受理、文書反映は、それぞれ意味が違います。</li>
</ul>
</div>
</section>

<div class="note-box">
<strong>Scopus / arXiv / source_logged の意味だけ先に確認したいとき</strong>
<p>
このページは役割差を説明する補助ページです。掲載元、文献種別、サイト内状態、evidence class の違いを 1 枚で整理したい場合は、<a href="paper-source-types-and-evidence-status.html">Wiki: 文献のソース種別・状態・証拠クラスの読み方</a> を先に見ると、論文集や文献地図の見え方が安定します。
</p>
</div>

<section class="section" id="next-step">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
広く論文を眺めたい場合は <a href="../mind_uploading_papers.html">論文集</a>、未解決問題から入りたい場合は <a href="../research_harvest_50.html">文献地図</a>、提案と実装方針を追いたい場合は <a href="../issue.html#proposal-integration">技術提案</a> へ戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="paper-source-types-and-evidence-status.html">文献のソース種別・状態・証拠クラス →</a></li>
<li><a href="proposal-status-reading.html">提案と状態ラベルの読み方 →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="mind-upload-basics.html">WBEの基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../research_harvest_50.html">文献地図 →</a></li>
<li><a href="../mind_uploading_papers.html">論文集 →</a></li>
<li><a href="../issue.html#proposal-integration">技術提案 →</a></li>
</ul>
</div>
</aside>
</main>
