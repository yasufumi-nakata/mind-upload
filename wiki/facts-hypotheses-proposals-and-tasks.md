---
layout: default
title: "Wiki：事実・仮説・提案・実行タスクの違い"
description: "Research、Perspective、Idea、Proposals、Issue、Collaborations を、『何が観察で、何が仮説で、何が提案で、何が今やる作業か』で読み分けるためのガイドです。"
article_type: Wiki
subtitle: "ページの役割差を、事実・仮説・提案・タスクで整理する"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Reading roles of claims"
audience: "理論ページ、提案ページ、Issue ページの違いを整理したい人"
reading_time: "8〜12分"
page_intro: "このページは、Mind-Upload の各ページが『同じ種類の主張』ではないことを整理する補助ガイドです。観察や文献整理、理論的な作業仮説、提案、今このリポジトリで実行するタスク、外部依存の調整は、役割も証拠の重さも違います。その違いをそろえて読むために使います。"
accuracy_note: "ここで扱うのはページの役割差です。個別の理論や提案の妥当性は、必ず各ページ本文と根拠へ戻って確認してください。"
page_highlights:
  - "観察、仮説、提案、実行タスク、外部依存を同じ重さで読まないための基本を整理します。"
  - "Perspective、Idea、Proposals、Issue、Collaborations の違いを一枚で確認できます。"
  - "『文書に書いてある』ことと『今すぐ実行する変更』を混同しないためのガイドです。"
known_points:
  - "各ページは、観察、理論仮説、提案、実装タスク、外部依存で役割分担されています。"
  - "提案受理や文書反映は、実装完了や外部合意完了を自動では意味しません。"
  - "実行可能な変更は、Issue や Hands-on に落ちて初めて具体的に動きます。"
unknown_points:
  - "どの仮説や提案が最終的に中心線として残るかは、今後の検証で変わります。"
  - "外部依存の話がどこまで実際の連携へ進むかは、相手先や条件に依存します。"
wiki_links:
  - label: "Wiki: 公開ページの読み分けガイド"
    url: "/wiki/public-page-reading-guide.html"
    description: "ページ全体の役割差を先に見たい人向けです。"
  - label: "Wiki: 提案と状態ラベルの読み方"
    url: "/wiki/proposal-status-reading.html"
    description: "提案ページの状態ラベルをさらに詳しく見たい人向けです。"
  - label: "Wiki: はじめての Issue の書き方"
    url: "/wiki/issue-writing-basics.html"
    description: "実行タスクへ落とす書き方を補います。"
recommended_pages:
  - label: "研究ノート"
    url: "/perspective.html"
  - label: "理論フレーム"
    url: "/idea.html"
  - label: "技術提案"
    url: "/proposals.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>同じ「主張」に見えても、役割は同じではありません</h2>
<p>
文献整理、理論ノート、設計原理、技術提案、Issue、協業候補は、全部が同じ種類の文章ではありません。まず <strong>何を記録しているページか</strong> を分けると、断言の強さと次の行動を読み違えにくくなります。
</p>
</div>

<section class="section" id="five-types">
<h2 class="section-title">まず 5 種類に分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>種類</th>
<th>何をしているか</th>
<th>主なページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察 / 整理</strong></td>
<td>何が知られていて、どこが未解決かを記録します。</td>
<td><a href="../research_harvest_50.html">Research Harvest</a> / <a href="../mind_uploading_papers.html">Papers</a> / <a href="../casework.html">Casework</a></td>
</tr>
<tr>
<td><strong>仮説 / 理論フレーム</strong></td>
<td>どう考えると設計条件へ落としやすいかを示します。</td>
<td><a href="../perspective.html">Perspective</a> / <a href="../idea.html">Idea</a></td>
</tr>
<tr>
<td><strong>提案 / 方針</strong></td>
<td>どの方向で進めるか、どのストリームで整理するかを示します。</td>
<td><a href="../proposals.html">Proposals</a></td>
</tr>
<tr>
<td><strong>実行タスク</strong></td>
<td>今このリポジトリで直す変更、完了条件、反証条件を切ります。</td>
<td><a href="../issue.html">Issue</a> / <a href="../hands_on.html">Hands-on</a></td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td>共同研究、標準化、IRB、機材、法務など、外部条件が必要な作業を整理します。</td>
<td><a href="../collaborations.html">Collaborations</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="page-differences">
<h2 class="section-title">似て見えるページの違い</h2>
<table class="data-table">
<thead>
<tr>
<th>ページ</th>
<th>主な役割</th>
<th>誤読しやすい点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Perspective</strong></td>
<td>文献と限界を並べて、理論の支持点と弱点を追う研究ノートです。</td>
<td>長文でも、最終確定理論の宣言ではありません。</td>
</tr>
<tr>
<td><strong>Idea</strong></td>
<td>採用する設計原理や作業仮説を絞って示す理論フレームです。</td>
<td>立場の整理であり、実験的に証明済みという意味ではありません。</td>
</tr>
<tr>
<td><strong>Proposals</strong></td>
<td>提案の状態、ストリーム、根拠節を追う整理表です。</td>
<td>提案受理は、コード実装や共同研究成立を意味しません。</td>
</tr>
<tr>
<td><strong>Issue</strong></td>
<td>今この場で実行する変更を、完了条件つきで管理する入口です。</td>
<td>大きな理論や外部依存まで同じ箱で扱うと混乱します。</td>
</tr>
<tr>
<td><strong>Collaborations</strong></td>
<td>外部依存の候補と、連携前に必要な準備物を整理する実務ページです。</td>
<td>候補一覧であり、合意済みリストではありません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-move">
<h2 class="section-title">どう移ると自然か</h2>
<table class="data-table">
<thead>
<tr>
<th>いまいる場所</th>
<th>次に移る自然な先</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察 / 整理</strong></td>
<td><a href="../perspective.html">Perspective</a> / <a href="../proposals.html">Proposals</a></td>
<td>文献整理の次に、どう読むか、どの方針へ使うかを決めるためです。</td>
</tr>
<tr>
<td><strong>仮説 / 理論フレーム</strong></td>
<td><a href="../verification.html">Verification</a> / <a href="../tech_roadmap.html">Roadmap</a></td>
<td>仮説を、そのまま設計条件や検証条件へ落とす必要があるためです。</td>
</tr>
<tr>
<td><strong>提案 / 方針</strong></td>
<td><a href="../issue.html">Issue</a> / <a href="../hands_on.html">Hands-on</a></td>
<td>提案を実際の変更や最小ループへ落とし込むためです。</td>
</tr>
<tr>
<td><strong>実行タスク</strong></td>
<td><a href="../content_hub.html">Content Hub</a> / <a href="../verification.html">Verification</a></td>
<td>置き場所や完了条件を再確認しながら進めるためです。</td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td><a href="internal-prework-and-external-dependencies.html">内製で先にやることと外部依存</a></td>
<td>まず内製できる準備物へ分解する必要があるためです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある混同</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>理論フレームを事実一覧として読む：</strong> Idea は作業仮説を含みます。</li>
<li><strong>提案ページを実装完了と読む：</strong> Proposals は整理表であり、完了報告ではありません。</li>
<li><strong>Issue を大きな構想メモにする：</strong> 今このリポジトリで切れる変更へ落とす方が安全です。</li>
<li><strong>Collaborations を TODO 一覧と読む：</strong> 外部依存の候補と準備物の整理であり、即実行リストではありません。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
公開ページ全体の役割差へ戻るなら <a href="public-page-reading-guide.html">公開ページの読み分けガイド</a>、提案ページの状態へ戻るなら <a href="proposal-status-reading.html">提案と状態ラベルの読み方</a>、実行タスクへ落とし込むなら <a href="issue-writing-basics.html">はじめての Issue の書き方</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="public-page-reading-guide.html">公開ページの読み分けガイド →</a></li>
<li><a href="proposal-status-reading.html">提案と状態ラベルの読み方 →</a></li>
<li><a href="issue-writing-basics.html">はじめての Issue の書き方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../perspective.html">研究ノート →</a></li>
<li><a href="../idea.html">理論フレーム →</a></li>
<li><a href="../proposals.html">技術提案 →</a></li>
</ul>
</div>
</aside>
</main>
