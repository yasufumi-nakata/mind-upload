---
layout: default
title: "Wiki：L0で最低限そろえる成果物パック"
description: "BIDS、Validator、QCログ、分割ルール、ベースライン、実行手順、失敗例など、L0 の再現可能解析で最低限そろえたい成果物を 1 枚で整理します。"
article_type: Wiki
subtitle: "『最小ループ』を、提出物の形で確認するための補助ページ"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Operational guide"
audience: "L0 を作り始めた人、どこまでそろえば再現可能解析と呼べるかを確認したい人"
reading_time: "8〜12分"
page_intro: "このページは、L0 の再現可能解析を作るときに、最終的に何を一式としてそろえるべきかを整理する補助ページです。手順書ではなく、提出物の形に注目して『何があれば第三者が追えるか』を確認するために使います。"
accuracy_note: "ここで扱うのは L0 の最低限です。これだけで因果主張や本人性の議論に進めるわけではありませんが、比較可能な出発点としては重要です。"
page_highlights:
  - "BIDS、Validator、QC、分割、ベースライン、実行手順、失敗例を 1 パックとして整理します。"
  - "『手順はあるがログがない』『精度はあるが分割規則がない』といった抜けを見つけやすくします。"
  - "hands_on の作業手順と、verification の成果物設計を橋渡しします。"
known_points:
  - "L0 では高精度より、第三者が同じ条件で再実行できることが重要です。"
  - "BIDS の形、QC ログ、分割規則、ベースラインがそろうだけで、比較可能性は大きく上がります。"
  - "失敗例や既知のつまずきどころも成果物の一部として残すべきです。"
unknown_points:
  - "どのベースラインやどの QC 指標が最終的に最も有効かは、課題ごとに変わります。"
  - "L0 の先で、どこまで L1/L2 の標準成果物へ広げるかは今後の整備次第です。"
wiki_links:
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "なぜ成果物を先に固定するのかを初歩から確認できます。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "分割規則が成果物に入る理由を補います。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "ベースラインや失敗例の役割差を補います。"
recommended_pages:
  - label: "ハンズオン"
    url: "/hands_on.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず 1 パックで考える</h2>
<p>
L0 の成果物は、1 つのファイルや 1 つのスコアではありません。<strong>入力の形</strong>、<strong>品質の証跡</strong>、<strong>評価のルール</strong>、<strong>再実行手順</strong>がそろって、初めて第三者が追える状態になります。
</p>
</div>

<section class="section" id="artifact-pack">
<h2 class="section-title">L0 で最低限そろえたい 7 点</h2>
<table class="data-table">
<thead>
<tr>
<th>成果物</th>
<th>最低限ほしい中身</th>
<th>欠けると何が困るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. データ骨格</strong></td>
<td>BIDS の骨格、最低限のメタデータ、課題名、電極情報。</td>
<td>同じ入力を別の人が持てず、比較の出発点が揃いません。</td>
</tr>
<tr>
<td><strong>2. 規格確認結果</strong></td>
<td>BIDS Validator の結果、残した警告の理由。</td>
<td>共有不能な規格違反を見落としやすくなります。</td>
</tr>
<tr>
<td><strong>3. QC ログ</strong></td>
<td>欠損、ノイズ、アーティファクト、除外理由の数値記録。</td>
<td>どのデータが悪かったかが人依存になり、再現性が壊れます。</td>
</tr>
<tr>
<td><strong>4. 分割ルール</strong></td>
<td>train/test の単位、リーク防止ルール、test を触らない約束。</td>
<td>数字の上振れを見抜けず、評価全体が崩れます。</td>
</tr>
<tr>
<td><strong>5. ベースライン結果</strong></td>
<td>単純な 1 本の指標、設定、結果表。</td>
<td>改善を主張する出発点が無くなります。</td>
</tr>
<tr>
<td><strong>6. 実行手順</strong></td>
<td>コマンド、環境、乱数、前処理条件、既知のつまずきどころ。</td>
<td>他の人が同じ流れを再実行できません。</td>
</tr>
<tr>
<td><strong>7. 失敗例</strong></td>
<td>除外した条件、うまくいかなかった設定、注意点。</td>
<td>成功だけが残り、次の人が同じ失敗を繰り返します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="minimum-shape">
<h2 class="section-title">もっと短く言うと</h2>
<div class="key-points">
<h4>Pack</h4>
<ul>
<li><strong>Input:</strong> BIDS の形</li>
<li><strong>Quality:</strong> QC と Validator</li>
<li><strong>Evaluation:</strong> 分割ルールとベースライン</li>
<li><strong>Replay:</strong> 実行手順と失敗例</li>
</ul>
</div>
</section>

<section class="section" id="common-gaps">
<h2 class="section-title">よくある抜け</h2>
<table class="data-table">
<thead>
<tr>
<th>ありがちな状態</th>
<th>まだ足りないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>波形ファイルはある</strong></td>
<td>イベント、同期、bad segment、課題定義が足りないことがあります。</td>
</tr>
<tr>
<td><strong>精度はある</strong></td>
<td>分割規則、リーク検査、ベースラインとの差が無いことがあります。</td>
</tr>
<tr>
<td><strong>コードはある</strong></td>
<td>環境、乱数、実行順、既知の失敗条件が書かれていないことがあります。</td>
</tr>
<tr>
<td><strong>QC したつもり</strong></td>
<td>数値ログや除外理由が残っていないことがあります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="exit-criteria">
<h2 class="section-title">L0 完了の簡易判定</h2>
<table class="data-table">
<thead>
<tr>
<th>質問</th>
<th>はいなら前進</th>
<th>いいえなら次にやること</th>
</tr>
</thead>
<tbody>
<tr>
<td>他の人が同じ入力を持てますか</td>
<td>BIDS 骨格とメタデータが揃っています。</td>
<td>データ骨格を先に固定します。</td>
</tr>
<tr>
<td>どのデータを除外したか分かりますか</td>
<td>QC ログと除外理由が残っています。</td>
<td>数値ログへ落とします。</td>
</tr>
<tr>
<td>数字の作り方を説明できますか</td>
<td>分割規則とベースラインが固定されています。</td>
<td>train/test と比較相手を先に固定します。</td>
</tr>
<tr>
<td>他の人が再実行できますか</td>
<td>コマンド、環境、既知の失敗条件が残っています。</td>
<td>短い runbook を作ります。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>このページがしないこと</strong>
<p>
ここでは、どのモデルが最強か、どの指標が最終的に正しいかは決めません。L0 では、まず比較可能な出発点を作ることが目的です。
</p>
</div>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
実際の手順を追いたい場合は <a href="../hands_on.html">ハンズオン</a>、入口データを選び直したい場合は <a href="../datasets.html">データ&ベンチ</a>、この成果物が公共財としてどう積み上がるかを見たい場合は <a href="../verification.html">検証基盤</a> に戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="dataset-splits-and-leakage.html">データ分割とデータリーク →</a></li>
<li><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">ベースライン・事前登録・モデルカード →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../hands_on.html">ハンズオン →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
