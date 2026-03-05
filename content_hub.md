---
layout: default
title: "公開コンテンツ統合ハブ"
description: "公開ページの役割・統合先・更新先を1ページに集約した運用ハブ。"
article_type: "Navigation"
subtitle: "散逸防止のための単一導線"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Single source of truth for public pages"
audience: "公開ページの置き場所を確認したい人、新規追記の統合先を迷いたくない人"
reading_time: "5〜10分"
page_intro: "このページは、公開コンテンツが散らばらないように『どの話題をどのページへ足すべきか』を固定するための運用ハブです。新しい情報を書く前に、まず既存ページの統合先を確認する場所として使います。"
accuracy_note: "ここは運用ハブであり、新しい主張を増やす本文ページではありません。どこへ統合すべきかを判断するためのページです。"
page_highlights:
  - "領域ごとに主ページと補助ページを分け、追記先を固定しています。"
  - "新規ページを増やす前に、既存ページへ統合できるかを確認する前提です。"
  - "公開導線と運用資料を一箇所で見渡せるようにしています。"
recommended_pages:
  - label: "スタートページ"
    url: "/index.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "貢献ガイド"
    url: "/issue.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>このページの役割</h2>
<p>
このページは、公開コンテンツの<strong>統合先</strong>と<strong>更新先</strong>を固定するハブです。新しい情報を追加するときは、まず本ページの対応表で既存ページを確認し、既存ページへ統合する運用を優先します。
</p>
</div>

<div class="note-box">
<strong>このページで決めること</strong>
<p>
ここで決めたいのは「何を書くか」よりも「どこへ書くか」でございます。内容の重複や導線の散逸を防ぐため、公開ページの入口と統合先をこのページで先に固定します。
</p>
</div>

<section class="section" id="quick-routing">
<h2 class="section-title">追加したい内容から統合先を決める</h2>
<table class="data-table">
<thead>
<tr>
<th>追加したい内容</th>
<th>まず足す先</th>
<th>そのページに置く理由</th>
</tr>
</thead>
<tbody>
<tr>
<td>「何を満たせば前進か」「何が出たら失敗か」の説明</td>
<td><a href="verification.html">verification.html</a></td>
<td>このサイトの合格条件と反証条件を一番厳密に置く主ページだからです。</td>
</tr>
<tr>
<td>技術的な順番、どこから解くべきか、未解決問題の整理</td>
<td><a href="tech_roadmap.html">tech_roadmap.html</a></td>
<td>問題分解と到達条件を固定する場所であり、順序の話を散らさないためです。</td>
</tr>
<tr>
<td>理論比較、批判点、哲学的前提の整理</td>
<td><a href="perspective.html">perspective.html</a></td>
<td>理論ごとの立場の違いを、検証可能性と結び付けて読むためです。</td>
</tr>
<tr>
<td>論文の要約、未解決問題ごとの文献整理</td>
<td><a href="research_harvest_50.html">research_harvest_50.html</a></td>
<td>論点別の受け皿があり、既存の問題番号と結び付けて蓄積できるからです。</td>
</tr>
<tr>
<td>「まず何を読むか」という入口の説明</td>
<td><a href="index.html">index.html</a></td>
<td>最初の導線を一本化し、同じ案内を複数ページに重複させないためです。</td>
</tr>
<tr>
<td>用語の意味や、似た言葉の違い</td>
<td><a href="glossary.html">glossary.html</a></td>
<td>本文ページを重くしすぎず、言葉の足場を共通化できるからです。</td>
</tr>
<tr>
<td>参加方法、Issueの状態、外部依存タスクの切り分け</td>
<td><a href="issue.html">issue.html</a></td>
<td>実行可能な変更と保留事項を分けて記録する専用ページだからです。</td>
</tr>
<tr>
<td>実務手順、最小ループ、手を動かす順番</td>
<td><a href="hands_on.html">hands_on.html</a></td>
<td>読むだけでなく、実際に再現可能な作業へ落とすためのページだからです。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>新規ページを作る前の確認</strong>
<p>
新しいページを増やす前に、その内容が既存ページの1節として自然に入らないかを確認してください。ページが増えるほど、読む順番と責任範囲が分散し、初学者ほど迷いやすくなります。内容が既存ページの目的に収まるなら、分割より統合を優先します。
</p>
</div>

<section class="section" id="integration-map">
<h2 class="section-title">統合マップ（公開ページ）</h2>
<table class="data-table">
<thead><tr><th>領域</th><th>統合先（主ページ）</th><th>含める内容</th><th>補助ページ</th></tr></thead><tbody>
<tr><td>検証基盤</td><td><a href="verification.html">verification.html</a></td><td>勝利条件、反証条件、監査契約、再現性基準</td><td><a href="hands_on.html">hands_on.html</a></td></tr>
<tr><td>技術ロードマップ</td><td><a href="tech_roadmap.html">tech_roadmap.html</a></td><td>問題分解、到達条件、実装順序</td><td><a href="proposals.html">proposals.html</a></td></tr>
<tr><td>研究論点</td><td><a href="perspective.html">perspective.html</a></td><td>理論整理、批判点、文献根拠</td><td><a href="idea.html">idea.html</a></td></tr>
<tr><td>未解決問題×文献</td><td><a href="research_harvest_50.html">research_harvest_50.html</a></td><td>U別のリサーチクエスチョン、文献監査、重複整理</td><td><a href="datasets.html">datasets.html</a></td></tr>
<tr><td>参加導線</td><td><a href="issue.html">issue.html</a></td><td>Issue運用、対応状況、外部依存タスクの分離</td><td><a href="collaborations.html">collaborations.html</a></td></tr>
<tr><td>入門導線</td><td><a href="index.html">index.html</a></td><td>読む順番、主要ページへの入口</td><td><a href="wbe_101.html">wbe_101.html</a> / <a href="eeg_101.html">eeg_101.html</a></td></tr>
</tbody></table>
</section>

<section class="section" id="rules">
<h2 class="section-title">散逸防止ルール</h2>
<ol>
<li>新規ファイルを作る前に、既存の統合先へ追記できるかを先に確認する。</li>
<li>一時的な下書き・中間成果は公開ページへ直結させず、運用ディレクトリ（`automation/` 等）で管理する。</li>
<li>公開導線は `index.html` と本ページに集約し、重複導線を増やさない。</li>
<li>Issue対応で追加した内容は、対応先ページと根拠リンクを必ず明記する。</li>
</ol>
</section>

<section class="section" id="public-pages">
<h2 class="section-title">公開ページ一覧</h2>
<div class="key-points">
<h4>Core</h4>
<ul>
<li><a href="index.html">index.html</a></li>
<li><a href="verification.html">verification.html</a></li>
<li><a href="tech_roadmap.html">tech_roadmap.html</a></li>
<li><a href="perspective.html">perspective.html</a></li>
<li><a href="proposals.html">proposals.html</a></li>
<li><a href="issue.html">issue.html</a></li>
</ul>
</div>
<div class="key-points">
<h4>Reference</h4>
<ul>
<li><a href="research_harvest_50.html">research_harvest_50.html</a></li>
<li><a href="mind_uploading_papers.html">mind_uploading_papers.html</a></li>
<li><a href="datasets.html">datasets.html</a></li>
<li><a href="glossary.html">glossary.html</a></li>
<li><a href="faq.html">faq.html</a></li>
<li><a href="casework.html">casework.html</a></li>
</ul>
</div>
</section>

</article>
<aside class="sidebar-column">
<div class="sidebar-box">
<h4>運用資料（GitHub）</h4>
<ul>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/blob/main/README.md" target="_blank">README.md ↗</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/blob/main/AGENTS.md" target="_blank">AGENTS.md ↗</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/tree/main/.agent" target="_blank">.agent/ ↗</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/tree/main/automation" target="_blank">automation/ ↗</a></li>
</ul>
</div>
</aside>
</main>
