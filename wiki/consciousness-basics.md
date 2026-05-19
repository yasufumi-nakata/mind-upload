---
layout: default
title: "意識理論"
description: "IIT、GNWT、FEP、Active Inference、PCI など、Mind-Uploadで頻出する意識理論と指標を初歩から整理します。"
article_type: Wiki
subtitle: "何を保存すれば『意識がある』と言えるのか"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Beginner-first"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>TL;DR</h2>
<p>
意識理論は、WBE で<strong>何を再現対象に含めるべきか</strong>を左右します。ただし、現時点では単一理論への決着はついていません。Mind-Upload は理論争いを避けるのではなく、<strong>理論ごとに何を要求するか</strong>と<strong>何がまだ未検証か</strong>を分けて扱います。
</p>
</div>

<section class="section" id="theories">
<h2 class="section-title">よく出る理論をざっくり区別する</h2>
<table class="data-table">
<thead>
<tr>
<th>理論</th>
<th>初歩的な説明</th>
<th>WBEで気になる点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT</strong></td>
<td>意識は統合された因果構造に対応する、という立場です。</td>
<td>正しい入出力だけでなく、因果構造の保存が必要になります。</td>
</tr>
<tr>
<td><strong>GNWT</strong></td>
<td>情報が広域ネットワークで共有されると意識化する、という立場です。</td>
<td>前頭-頭頂ネットワークやイグニッションの再現が重要になります。</td>
</tr>
<tr>
<td><strong>FEP / Active Inference</strong></td>
<td>生体は予測誤差を減らしながら環境へ能動的に関わる、という枠組みです。</td>
<td>閉ループ、自律性、自己維持の設計へつながります。</td>
</tr>
<tr>
<td><strong>HOT</strong></td>
<td>一次表象をさらに捉える高次表象が意識に関わる、という理論群です。</td>
<td>自己参照やメタ認知の実装要件に関係します。</td>
</tr>
<tr>
<td><strong>PCI / PCI-ST</strong></td>
<td>摂動に対する脳応答の複雑さを測る経験的指標です。</td>
<td>理論非依存の検証指標として使いやすいです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-theory">
<h2 class="section-title">なぜ理論を避けて通れないか</h2>
<p>
「行動が似ている」「応答が自然である」だけでは、どこまでを意識の再現と呼ぶかが決まりません。理論は、<strong>どの性質を保存すべきか</strong>を決める地図の役割を持ちます。
</p>
<div class="note-box">
<strong>Mind-Upload の立場</strong>
<p>
特定理論を最終解答として採用しません。その代わり、PCI のような経験的指標や、理論ごとに異なる予測を比較できるテスト設計を優先します。
</p>
</div>
<div class="cta-box">
<h4>Deep Dive</h4>
<p><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較</a>、<a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答</a>、<a href="{{ '/wiki/fep-active-inference.html' | relative_url }}">FEP / 能動的推論 / マルコフブランケット</a> に詳細を分けています。</p>
</div>
</section>

<section class="section" id="unknowns">
<h2 class="section-title">まだ分かっていないこと</h2>
<table class="data-table">
<thead>
<tr>
<th>何が分かっていないか</th>
<th>なぜ分からないか</th>
<th>今どこで詰まるか</th>
<th>分かると何が嬉しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どの理論が正しいか</strong><br>IIT, GNWT, FEP などの優劣。</td>
<td>理論ごとに前提も指標も異なり、同じ土俵で比較しにくいからです。</td>
<td>何を保存すべきかが揺れます。</td>
<td>WBE の成功条件を絞り込めます。</td>
</tr>
<tr>
<td><strong>意識指標と主観経験の関係</strong><br>PCI などが何をどこまで表すか。</td>
<td>主観経験を第三者が直接観測できません。</td>
<td>指標が高いことを、経験の同一性に直結しにくいです。</td>
<td>理論非依存な合否テストを作りやすくなります。</td>
</tr>
<tr>
<td><strong>報告課題の混入</strong><br>被験者の報告行動が理論検証を汚していないか。</td>
<td>意識研究では「報告する」こと自体が脳活動を変えるからです。</td>
<td>理論同士の比較実験が解釈しにくいです。</td>
<td>より純粋な意識指標に近づけます。</td>
</tr>
<tr>
<td><strong>スケール問題</strong><br>ミクロ・マクロのどの因果構造が重要か。</td>
<td>脳は多階層系で、どの空間・時間スケールが本質か不明です。</td>
<td>実装粒度と理論要件が一致しません。</td>
<td>必要な計測解像度や実装基盤を絞れます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>意識理論の名前を、単なる哲学用語でなく設計条件として読めます。</li>
<li>なぜ Mind-Upload が PCI や反事実テストを重視するか理解できます。</li>
<li>理論の未決着を理由に停止するのでなく、比較可能な実験へ分解できます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較 →</a></li>
<li><a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答 →</a></li>
<li><a href="{{ '/wiki/fep-active-inference.html' | relative_url }}">FEPと能動的推論 →</a></li>
<li><a href="{{ '/wiki/wbe-basics.html' | relative_url }}">WBEの基礎 →</a></li>
<li><a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/glossary.html#consciousness-theories' | relative_url }}">Glossary: 意識理論 →</a></li>
<li><a href="{{ '/faq.html#q8' | relative_url }}">FAQ: IIT と GNWT →</a></li>
<li><a href="{{ '/perspective.html#eeg-consciousness-roadmap' | relative_url }}">Perspective: EEGで意識を測る →</a></li>
</ul>
</div>

</aside>
</main>
