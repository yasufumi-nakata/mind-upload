---
layout: default
title: "Wiki：実務系ページの読み分けガイド"
description: "Verification、Datasets、Hands-on、Casework、Proposals など、実務寄りの公開ページどうしの役割差と読む順番を整理します。"
article_type: Wiki
subtitle: "勝利条件、入口データ、作業手順、参照事例、提案整理を混ぜないための地図"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Reading guide"
audience: "手を動かす側の公開ページから入りたい人、実務ページの役割差を整理したい人"
reading_time: "8〜12分"
page_intro: "このページは、Mind-Upload の実務寄り公開ページを読み分けるための補助ガイドです。Verification は勝利条件、Datasets は入口データ、Hands-on は最小ループ手順、Casework は参照事例、Proposals は提案整理であり、似て見えても役目が違います。"
accuracy_note: "ここで扱うのはページの役割差です。実際の検証条件や手順の細部は、各本文ページで確認してください。"
page_highlights:
  - "実務系ページを、設計、入口データ、作業手順、参照事例、提案整理に分けて整理します。"
  - "『手を動かしたい』という同じ目的でも、最初に読むべきページが違うことを明確にします。"
  - "提案済み、実装方針反映、外部依存を混ぜて読まないための補助線を置きます。"
known_points:
  - "Verification、Datasets、Hands-on、Casework、Proposals は、どれも実務寄りですが役割が違います。"
  - "Verification は前進の定義、Datasets は入口選定、Hands-on は手順、Casework は設計参照、Proposals は提案整理です。"
  - "ページの役割差を先に分けると、実務導線を読み違えにくくなります。"
unknown_points:
  - "どの実務ルートが将来の L2 や L3 に最も効くかは、まだ固定していません。"
  - "将来どの実務ページを独立拡張するかは、運用の蓄積に応じて変わります。"
wiki_links:
  - label: "Wiki: 公開ページの読み分けガイド"
    url: "/wiki/public-page-reading-guide.html"
    description: "公開ページ全体の役割差を見たい人向けです。"
  - label: "Wiki: L0で最低限そろえる成果物パック"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "Hands-on の提出物を 1 枚で確認したい人向けです。"
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "Casework や Verification で出る運用語の違いを補います。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "実務ページで何を残すべきかを役割ごとに整理します。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "ハンズオン"
    url: "/hands_on.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず5つに分ける</h2>
<p>
実務系ページは、全部が「作業に役立つページ」ではありますが、<strong>何を決めるページか</strong>が違います。先に <strong>勝利条件</strong>、<strong>入口データ</strong>、<strong>作業手順</strong>、<strong>参照事例</strong>、<strong>提案整理</strong> に分けると、実務導線がかなり安定します。
</p>
</div>

<div class="note-box">
<strong>EEGからL0までの順番だけを一本道で見たいとき</strong>
<p>
実務ページの役割差よりも、EEG 入門から Datasets、Hands-on、Verification までの順番をそのまま辿りたい場合は <a href="eeg-to-l0-route.html">EEGからL0までの一本道</a> をご覧ください。
</p>
</div>

<section class="section" id="role-diff">
<h2 class="section-title">実務系ページの役割差</h2>
<table class="data-table">
<thead>
<tr>
<th>ページ</th>
<th>主な役割</th>
<th>最初に向く疑問</th>
<th>ここだけでは足りないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><a href="../verification.html">Verification</a></strong></td>
<td>勝利条件と反証条件を決める設計図です。</td>
<td>「何を満たしたら前進か」を先に固定したいときです。</td>
<td>実際の入口データや作業手順は、Datasets や Hands-on で補う必要があります。</td>
</tr>
<tr>
<td><strong><a href="../datasets.html">Datasets</a></strong></td>
<td>入口データを選ぶページです。</td>
<td>最初にどの公開データで L0 を始めるかを決めたいときです。</td>
<td>何を成果物として残すかは、Hands-on や Verification で補う必要があります。</td>
</tr>
<tr>
<td><strong><a href="../hands_on.html">Hands-on</a></strong></td>
<td>最小ループを作る手順書です。</td>
<td>今この場で再現可能な解析を一周つなぎたいときです。</td>
<td>その手順がなぜ必要かという設計理由は、Verification で補う必要があります。</td>
</tr>
<tr>
<td><strong><a href="../casework.html">Casework</a></strong></td>
<td>他分野の成功事例から設計の型を学ぶ参照集です。</td>
<td>標準、置き場、ベンチ、事前登録がなぜ効いたのかを実例で見たいときです。</td>
<td>この事例だけで WBE の成立を示すことはできません。</td>
</tr>
<tr>
<td><strong><a href="../proposals.html">Proposals</a></strong></td>
<td>提案群の状態と根拠をまとめる整理表です。</td>
<td>どの提案が何を目指し、どこまで反映されたかを追いたいときです。</td>
<td>要約だけで実装完了とは言えず、Issue や原文へ戻る必要があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="which-question">
<h2 class="section-title">この疑問なら、まずこのページ</h2>
<table class="data-table">
<thead>
<tr>
<th>いま知りたいこと</th>
<th>まず開くページ</th>
<th>次に行くページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>何を満たせば前進と呼べるか知りたい</td>
<td><a href="../verification.html">Verification</a></td>
<td><a href="../tech_roadmap.html">Roadmap</a> で依存関係を見ます。</td>
</tr>
<tr>
<td>最初にどの公開データを使うか決めたい</td>
<td><a href="../datasets.html">Datasets</a></td>
<td><a href="../hands_on.html">Hands-on</a> で L0 の作業へ進みます。</td>
</tr>
<tr>
<td>実際に何を一式として残すか知りたい</td>
<td><a href="../hands_on.html">Hands-on</a></td>
<td><a href="../verification.html">Verification</a> と <a href="../datasets.html">Datasets</a> を補います。</td>
</tr>
<tr>
<td>なぜ標準やベンチが必要かを歴史事例で見たい</td>
<td><a href="../casework.html">Casework</a></td>
<td><a href="../verification.html">Verification</a> に戻って現在設計と照合します。</td>
</tr>
<tr>
<td>提案済みと実装済みを区別して追いたい</td>
<td><a href="../proposals.html">Proposals</a></td>
<td><a href="../issue.html">Issue</a> と原文節へ戻ります。</td>
</tr>
<tr>
<td>どこへ追記・更新するかを決めたい</td>
<td><a href="../content_hub.html">Content Hub</a></td>
<td><a href="../issue.html">Issue</a> で実行可能な作業へ落とします。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="similar-pages">
<h2 class="section-title">似て見えるページの違い</h2>
<table class="data-table">
<thead>
<tr>
<th>似て見える組</th>
<th>違いを一言で言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Verification / Hands-on</strong></td>
<td>Verification は合格条件、Hands-on は最小ループの作業順です。</td>
</tr>
<tr>
<td><strong>Datasets / Hands-on</strong></td>
<td>Datasets は何で始めるか、Hands-on はどう一周させるかです。</td>
</tr>
<tr>
<td><strong>Verification / Casework</strong></td>
<td>Verification は現在の設計、Casework は他分野から借りる型です。</td>
</tr>
<tr>
<td><strong>Proposals / Issue</strong></td>
<td>Proposals は提案の本文整理、Issue は今この場で切る作業と外部依存の管理です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある迷い方</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>Datasets だけ見て進めた気になる：</strong> 何を成果物として残すかは Hands-on と Verification で固定する必要があります。</li>
<li><strong>Hands-on を勝利条件の定義と誤読する：</strong> 手順書だけでは、何を前進と呼ぶかまでは決まりません。</li>
<li><strong>Casework を直接の証拠と読む：</strong> ここは設計参照であり、WBE が成立した証明ではありません。</li>
<li><strong>Proposals を実装完了一覧として読む：</strong> 提案受理や文書反映と、実装完了や外部合意は別です。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
実務の入口へ戻るなら <a href="../verification.html">検証基盤</a>、L0 の実作業へ戻るなら <a href="../hands_on.html">ハンズオン</a>、更新先を決めたい場合は <a href="../content_hub.html">公開コンテンツ統合ハブ</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="public-page-reading-guide.html">公開ページの読み分けガイド →</a></li>
<li><a href="l0-minimum-artifact-pack.html">L0で最低限そろえる成果物パック →</a></li>
<li><a href="standards-repositories-validators-and-benchmarks.html">規格・置き場・Validator・ベンチマーク →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../hands_on.html">ハンズオン →</a></li>
</ul>
</div>
</aside>
</main>
