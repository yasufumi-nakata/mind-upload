---
layout: default
title: "Wiki：文献のソース種別と状態ラベルの読み方"
description: "Scopus、arXiv、Review、Media、source_logged、curated などが何を意味し、何を意味しないかを初歩から整理します。"
article_type: Wiki
subtitle: "Badge・掲載元・状態を混同しないための補助ページ"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Reading guide"
audience: "論文集や文献地図のラベルを読み違えたくない人、どこで原文へ戻るべきかを知りたい人"
reading_time: "8〜12分"
page_intro: "このページは、論文集や文献地図に出てくる『Scopus』『arXiv』『Review』『Media』『source_logged』『curated』などのラベルを、初学者向けに整理する補助ページです。ここで大事なのは、ラベルが何の情報なのかを分けて読むことです。"
accuracy_note: "ラベルは読み方の補助であり、論文内容の正しさを自動的に保証するものではありません。根拠として使うときは、必ず DOI、本文、一次研究へ戻ってください。"
page_highlights:
  - "掲載元、文献種別、サイト内状態を別の軸として分けて説明します。"
  - "Scopus や arXiv を、そのまま証拠の強さと誤読しないための基準を示します。"
  - "どこで止めてよいか、どこから原文へ戻るべきかを表で確認できます。"
known_points:
  - "同じ文献でも、掲載元、文献種別、サイト内状態は別々に見る必要があります。"
  - "Scopus は索引、arXiv はプレプリント置き場、Review は文献種別であり、互いに同じ意味ではありません。"
  - "source_logged と curated は、このサイト内での整理状態を示すラベルです。"
unknown_points:
  - "個々の論文が最終的にどこまで中心的根拠として残るかは、後続の精査で変わります。"
  - "レビューやニュースから辿った話題が、一次研究へ戻ると弱まる場合もあります。"
wiki_links:
  - label: "Wiki: 文献と証拠ページの読み方"
    url: "/wiki/literature-and-evidence-reading.html"
    description: "論文集、文献地図、提案ページの役割差を先に整理します。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "ラベルの先にある『主張の強さ』をどう読むかを補います。"
  - label: "Wiki: U番号ガイド"
    url: "/wiki/u-number-guide.html"
    description: "文献地図で、どの未解決問題に関係するかを見る補助ページです。"
recommended_pages:
  - label: "論文集"
    url: "/mind_uploading_papers.html"
  - label: "文献地図"
    url: "/research_harvest_50.html"
  - label: "ケースワーク"
    url: "/casework.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず3つに分ける</h2>
<p>
文献ページで混乱しやすいのは、<strong>どこに載っているか</strong>、<strong>どんな種別の文献か</strong>、<strong>このサイト内で今どの状態か</strong>を同じものとして読んでしまうことです。まずこの3つを分けるだけで、かなり誤読が減ります。
</p>
</div>

<section class="section" id="three-axes">
<h2 class="section-title">ラベルには3つの軸があります</h2>
<table class="data-table">
<thead>
<tr>
<th>軸</th>
<th>何を表すか</th>
<th>例</th>
<th>それだけでは言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>掲載元・Badge</strong></td>
<td>どこから辿れる文献か、どの入口で拾ったかです。</td>
<td>Scopus / arXiv / 学術誌ページ / DOI</td>
<td>内容が強い、正しい、中心的根拠であるとは決まりません。</td>
</tr>
<tr>
<td><strong>文献種別</strong></td>
<td>その文書が一次研究なのか、レビューなのか、ニュースなのかです。</td>
<td>Primary / Review / Media</td>
<td>新規データの有無や、検証に直接使える強さは別途確認が必要です。</td>
</tr>
<tr>
<td><strong>サイト内状態</strong></td>
<td>このサイトで、入力受理済みか、整理済みか、除外済みかを示します。</td>
<td>source_logged / curated / noise_excluded</td>
<td>論文内容が真である、または価値が低い、とまでは決まりません。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>同じ文献に複数の属性が重なります</strong>
<p>
たとえば、ある文献が <strong>Scopus に載っているレビュー論文</strong> であることもあれば、<strong>arXiv にある一次研究のプレプリント</strong> であることもあります。ひとつのラベルだけで全体を決めないでください。
</p>
</div>

<section class="section" id="source-kinds">
<h2 class="section-title">掲載元や種別の読み方</h2>
<table class="data-table">
<thead>
<tr>
<th>表示</th>
<th>日常語で言うと</th>
<th>役に立つ点</th>
<th>注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scopus</strong></td>
<td>学術文献の索引データベース経由で見つかる文献です。</td>
<td>書誌情報を整理しやすく、学術文献を広く拾う入口になります。</td>
<td>Scopus は索引であり、査読の強さや論点への直結度を自動で保証しません。</td>
</tr>
<tr>
<td><strong>arXiv</strong></td>
<td>プレプリントの公開置き場です。</td>
<td>新しい研究を早く見つけられます。</td>
<td>投稿時点では査読前のことが多く、方法と限界を自分で確認する必要があります。</td>
</tr>
<tr>
<td><strong>Review</strong></td>
<td>複数研究をまとめる総説です。</td>
<td>分野全体の地図や主要論点を掴むのに向いています。</td>
<td>自前の新規実験が主役とは限らないため、強い根拠に使うときは一次研究へ戻ります。</td>
</tr>
<tr>
<td><strong>Media</strong></td>
<td>ニュース記事、解説記事、一般向け紹介です。</td>
<td>話題の入口や一次文献探索の手掛かりになります。</td>
<td>そのままでは学術的根拠として弱く、必ず元の論文や発表へ辿る必要があります。</td>
</tr>
<tr>
<td><strong>Primary</strong></td>
<td>新しいデータ、実験、解析を直接出している一次研究です。</td>
<td>方法、評価、限界を確認すれば、最も直接に根拠を追えます。</td>
<td>一次研究でもサンプル条件、統計、再現性の弱さはあり得るため、無条件では使えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-labels">
<h2 class="section-title">サイト内状態ラベルの読み方</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベル</th>
<th>日常語で言うと</th>
<th>次に必要なこと</th>
<th>誤読しやすい点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>source_logged</strong></td>
<td>入口として URL や DOI を受け付け、追跡対象に入れた段階です。</td>
<td>関連性確認、一次文献追跡、U番号割当、要約の精査が必要です。</td>
<td>「採用確定」や「高品質確定」を意味しません。</td>
</tr>
<tr>
<td><strong>curated</strong></td>
<td>このサイトの論点に沿って整理し、配置済みの段階です。</td>
<td>重複整理、強い根拠との差し替え、更新追跡は今後も必要です。</td>
<td>「内容が真である」と保証するラベルではありません。</td>
</tr>
<tr>
<td><strong>noise_excluded</strong></td>
<td>関係が薄い、混入が大きい、現時点では使わないと判断した段階です。</td>
<td>除外理由を残し、同種の混入を防ぐことが重要です。</td>
<td>論文自体の価値がゼロという意味ではなく、このサイトの論点とずれた可能性もあります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="when-to-return">
<h2 class="section-title">どこで止まり、どこで原文へ戻るか</h2>
<table class="data-table">
<thead>
<tr>
<th>いまの目的</th>
<th>ここで止めてよい</th>
<th>原文へ戻るべき</th>
</tr>
</thead>
<tbody>
<tr>
<td>広く話題を拾いたい</td>
<td>Badge、要約、5ポイント整理で関心の有無が分かった時点。</td>
<td>その論文を引用して強い主張を支えたいとき。</td>
</tr>
<tr>
<td>source_logged の項目を見ている</td>
<td>「まだ入口段階だ」と理解できた時点。</td>
<td>一次研究へ追えそうか、U番号に入るかを判断したいとき。</td>
</tr>
<tr>
<td>Review や Media を見ている</td>
<td>論点の地図や関連キーワードを掴めた時点。</td>
<td>評価、方法、数値を根拠として使いたいとき。</td>
</tr>
<tr>
<td>Scopus や arXiv の文献を比較している</td>
<td>どの入口から拾われたかを把握できた時点。</td>
<td>査読状況、実験条件、限界、追試可能性を確認したいとき。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある誤読</h2>
<div class="key-points">
<h4>Misread</h4>
<ul>
<li><strong>「Scopus だから強い」：</strong> Scopus は索引です。論点への効き方は、本文と方法で確認します。</li>
<li><strong>「arXiv だから全部弱い」：</strong> 査読前でも重要な入口はあります。弱いかどうかは内容で見ます。</li>
<li><strong>「Review だから十分」：</strong> 総説は地図として有用ですが、直接の根拠は一次研究へ戻る必要があります。</li>
<li><strong>「source_logged だから採用済み」：</strong> まだ受理ログであり、統合や除外の判断は後続作業です。</li>
<li><strong>「curated だから真である」：</strong> 整理済みであることと、最終的に正しいことは別です。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
論文を広く眺めたい場合は <a href="../mind_uploading_papers.html">論文集</a>、未解決問題との対応を見たい場合は <a href="../research_harvest_50.html">文献地図</a>、そもそもの役割差から整理したい場合は <a href="literature-and-evidence-reading.html">文献と証拠ページの読み方</a> に戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="literature-and-evidence-reading.html">文献と証拠ページの読み方 →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
<li><a href="u-number-guide.html">U番号ガイド →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../mind_uploading_papers.html">論文集 →</a></li>
<li><a href="../research_harvest_50.html">文献地図 →</a></li>
<li><a href="../casework.html">ケースワーク →</a></li>
</ul>
</div>
</aside>
</main>
