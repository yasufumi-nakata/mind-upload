---
layout: default
title: "学習Wiki"
description: "Mind-Uploadで頻出する概念を、初歩から未解決点までつなげて読むためのWiki。"
article_type: Wiki
subtitle: "まず意味をそろえ、その後で未解決点を追う"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Beginner-first"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>このWikiの役割</h2>
<p>
このWikiは、Mind-Upload の各ページで前提になっている概念を、<strong>本当に初歩的なところから</strong>読み直すための補助線です。各ページでは、<strong>何の話か</strong>だけでなく、<strong>何がまだ分かっていないか</strong>、<strong>なぜ分からないか</strong>、<strong>分かると何が前進するか</strong>までまとめます。
</p>
</div>

<section class="section" id="map">
<h2 class="section-title">ページ一覧（どこから読むか）</h2>
<table class="data-table">
<thead>
<tr>
<th>テーマ</th>
<th>最初に押さえること</th>
<th>未解決点の軸</th>
<th>ページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>WBEの基礎</strong></td>
<td>マインドアップロード / WBE / クレーム階段 / decode と emulate の違い</td>
<td>何を再現すれば「前進」か</td>
<td><a href="{{ '/wiki/wbe-basics.html' | relative_url }}">WBEの基礎 →</a></td>
</tr>
<tr>
<td><strong>計測とデータ</strong></td>
<td>EEG / MEG / fMRI / ECoG / 逆問題 / QC / BIDS</td>
<td>何をどこまで測れるか</td>
<td><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></td>
</tr>
<tr>
<td><strong>モデルと因果</strong></td>
<td>デコーディング / 生成モデル / 反事実 / 介入 / 閉ループ</td>
<td>相関から因果へどう進むか</td>
<td><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></td>
</tr>
<tr>
<td><strong>意識理論</strong></td>
<td>IIT / GNWT / FEP / Active Inference / PCI</td>
<td>何を保存すれば意識と言えるか</td>
<td><a href="{{ '/wiki/consciousness-basics.html' | relative_url }}">意識理論 →</a></td>
</tr>
<tr>
<td><strong>再現性とベンチ</strong></td>
<td>Verification Commons / ベンチマーク / 事前登録 / モデルカード</td>
<td>どうすれば比較可能な進歩になるか</td>
<td><a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ →</a></td>
</tr>
<tr>
<td><strong>本人性と倫理</strong></td>
<td>コピー問題 / 連続性 / 権利 / 同意 / ガバナンス</td>
<td>誰を本人と扱うか、どう守るか</td>
<td><a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理 →</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="paths">
<h2 class="section-title">おすすめの読み順</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">10m</div>
<div class="stage-body">
<h4>最短ルート</h4>
<p><a href="{{ '/wbe_101.html' | relative_url }}">WBE入門</a> → <a href="{{ '/eeg_101.html' | relative_url }}">EEG入門</a> → <a href="{{ '/wiki/' | relative_url }}">学習Wiki</a> の順で読むと、長文ページに入りやすくなります。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">30m</div>
<div class="stage-body">
<h4>研究の全体像を掴む</h4>
<p><a href="{{ '/wiki/wbe-basics.html' | relative_url }}">WBEの基礎</a> → <a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ</a> → <a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ</a> の順が基礎固め向きです。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">60m</div>
<div class="stage-body">
<h4>未解決問題まで追う</h4>
<p><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果</a>、<a href="{{ '/wiki/consciousness-basics.html' | relative_url }}">意識理論</a>、<a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理</a> を続けて読むと、どこで議論が難しくなるかが見えます。</p>
</div>
</div>
</div>
</section>

<section class="section" id="deep-dives">
<h2 class="section-title">概念別の詳細ページ</h2>
<table class="data-table">
<thead>
<tr>
<th>領域</th>
<th>詳細ページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>主張の強さ</strong></td>
<td><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段</a> / <a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate</a></td>
</tr>
<tr>
<td><strong>標準化と再現性</strong></td>
<td><a href="{{ '/wiki/bids-and-eeg-bids.html' | relative_url }}">BIDS / EEG-BIDS</a> / <a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証</a></td>
</tr>
<tr>
<td><strong>計測と推定</strong></td>
<td><a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI</a> / <a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答</a></td>
</tr>
<tr>
<td><strong>理論比較</strong></td>
<td><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較</a> / <a href="{{ '/wiki/fep-active-inference.html' | relative_url }}">FEP / 能動的推論 / マルコフブランケット</a></td>
</tr>
<tr>
<td><strong>本人性・運用</strong></td>
<td><a href="{{ '/wiki/copy-problem-and-continuity.html' | relative_url }}">コピー問題と連続性</a> / <a href="{{ '/wiki/benchmark-pitfalls.html' | relative_url }}">ベンチマークの罠</a></td>
</tr>
<tr>
<td><strong>構造・基盤・物理</strong></td>
<td><a href="{{ '/wiki/dcm-and-scm.html' | relative_url }}">DCM / SCM</a> / <a href="{{ '/wiki/connectome-and-dynamics.html' | relative_url }}">コネクトームとダイナミクス</a> / <a href="{{ '/wiki/neuromorphic-hardware.html' | relative_url }}">ニューロモルフィック基盤</a> / <a href="{{ '/wiki/thermodynamics-and-ness.html' | relative_url }}">熱力学とNESS</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="cross-guides">
<h2 class="section-title">横断ガイド</h2>
<table class="data-table">
<thead>
<tr>
<th>ガイド</th>
<th>何を補うか</th>
<th>ページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測量の整理</strong></td>
<td>何を直接見ていて、何を代理指標として使っているかを分けます。</td>
<td><a href="{{ '/wiki/observables-and-proxies.html' | relative_url }}">観測量と代理指標 →</a></td>
</tr>
<tr>
<td><strong>実験設計の整理</strong></td>
<td>各主張を、どの最小比較へ落とすべきかをまとめます。</td>
<td><a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計 →</a></td>
</tr>
<tr>
<td><strong>反証と停止の整理</strong></td>
<td>どこで主張を退け、どこで一旦止めるかを分けます。</td>
<td><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></td>
</tr>
<tr>
<td><strong>文献の整理</strong></td>
<td>文献が答える問いと、まだ答えていない問いを分けます。</td>
<td><a href="{{ '/wiki/literature-and-evidence-map.html' | relative_url }}">文献導線と証拠地図 →</a></td>
</tr>
<tr>
<td><strong>失敗の整理</strong></td>
<td>同じ「失敗」を型に分け、再発防止に接続します。</td>
<td><a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ →</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="unknowns">
<h2 class="section-title">このプロジェクトで大きい未解決点</h2>
<table class="data-table">
<thead>
<tr>
<th>何が未解決か</th>
<th>なぜ未解決か</th>
<th>分かると何が嬉しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>復元対象の定義</strong><br>何をどこまで再現すれば「WBEに近づいた」と言えるか。</td>
<td>機能、因果構造、記憶、本人性、意識を同時に満たす定義がまだ合意されていません。</td>
<td>強い主張と弱い主張を分けられ、達成条件と停止条件を先に書けます。</td>
</tr>
<tr>
<td><strong>必要な計測解像度</strong><br>どの粒度まで脳を測れば十分か。</td>
<td>非侵襲計測には物理限界があり、どの情報が本質かも確定していません。</td>
<td>過剰な計測を避けつつ、足りない情報を特定できます。</td>
</tr>
<tr>
<td><strong>因果モデルの妥当性</strong><br>予測できるだけでなく、介入に耐えるモデルをどう作るか。</td>
<td>脳データは高次元・ノイズ大・個体差大で、反事実の正解が取りにくいからです。</td>
<td>decode 止まりの成果を、emulate に近い成果へ段階的に押し上げられます。</td>
</tr>
<tr>
<td><strong>本人性と権利</strong><br>コピー、段階的移行、停止権をどう扱うか。</td>
<td>科学だけで決められず、哲学・法・制度設計が必要だからです。</td>
<td>L4〜L5 の議論を空論でなく、テスト可能な社会設計に接続できます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u-catalog">
<h2 class="section-title">U0〜U15 未解決問題カタログ</h2>
<p>Roadmap 上の未解決問題を個別ページ化しました。総覧は <a href="{{ '/wiki/unsolved-questions.html' | relative_url }}">未解決問題カタログ</a> から辿れます。</p>
<div class="key-points">
<h4>Start Points</h4>
<ul>
<li><a href="{{ '/wiki/u0-operational-identity.html' | relative_url }}">U0 操作的同一性</a></li>
<li><a href="{{ '/wiki/u4-counterfactual-equivalence.html' | relative_url }}">U4 因果同値</a></li>
<li><a href="{{ '/wiki/u10-thermodynamic-consistency.html' | relative_url }}">U10 熱力学的一貫性</a></li>
<li><a href="{{ '/wiki/u12-branching-identity.html' | relative_url }}">U12 分岐本人性</a></li>
</ul>
</div>
</section>

<section class="section" id="root-links">
<h2 class="section-title">元ページへ戻る導線</h2>
<div class="key-points">
<h4>Core Pages</h4>
<ul>
<li><a href="{{ '/index.html' | relative_url }}">Start</a>：入口ページ</li>
<li><a href="{{ '/verification.html' | relative_url }}">Verification</a>：何を作るサイトか</li>
<li><a href="{{ '/tech_roadmap.html' | relative_url }}">Roadmap</a>：問いの木</li>
<li><a href="{{ '/glossary.html' | relative_url }}">Glossary</a>：最短の辞書</li>
<li><a href="{{ '/faq.html' | relative_url }}">FAQ</a>：よくある誤解</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Wiki Pages</h4>
<ul>
<li><a href="{{ '/wiki/wbe-basics.html' | relative_url }}">WBEの基礎 →</a></li>
<li><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></li>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
<li><a href="{{ '/wiki/consciousness-basics.html' | relative_url }}">意識理論 →</a></li>
<li><a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ →</a></li>
<li><a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Deep Dives</h4>
<ul>
<li><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段 →</a></li>
<li><a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate →</a></li>
<li><a href="{{ '/wiki/bids-and-eeg-bids.html' | relative_url }}">BIDS / EEG-BIDS →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI →</a></li>
<li><a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答 →</a></li>
<li><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較 →</a></li>
<li><a href="{{ '/wiki/fep-active-inference.html' | relative_url }}">FEPと能動的推論 →</a></li>
<li><a href="{{ '/wiki/copy-problem-and-continuity.html' | relative_url }}">コピー問題と連続性 →</a></li>
<li><a href="{{ '/wiki/benchmark-pitfalls.html' | relative_url }}">ベンチマークの罠 →</a></li>
<li><a href="{{ '/wiki/dcm-and-scm.html' | relative_url }}">DCM / SCM →</a></li>
<li><a href="{{ '/wiki/connectome-and-dynamics.html' | relative_url }}">コネクトームとダイナミクス →</a></li>
<li><a href="{{ '/wiki/neuromorphic-hardware.html' | relative_url }}">ニューロモルフィック基盤 →</a></li>
<li><a href="{{ '/wiki/thermodynamics-and-ness.html' | relative_url }}">熱力学とNESS →</a></li>
<li><a href="{{ '/wiki/observables-and-proxies.html' | relative_url }}">観測量と代理指標 →</a></li>
<li><a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計 →</a></li>
<li><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></li>
<li><a href="{{ '/wiki/literature-and-evidence-map.html' | relative_url }}">文献導線と証拠地図 →</a></li>
<li><a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ →</a></li>
<li><a href="{{ '/wiki/unsolved-questions.html' | relative_url }}">未解決問題カタログ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="{{ '/wbe_101.html' | relative_url }}">WBE入門 →</a></li>
<li><a href="{{ '/eeg_101.html' | relative_url }}">EEG入門 →</a></li>
<li><a href="{{ '/glossary.html' | relative_url }}">用語集 →</a></li>
<li><a href="{{ '/verification.html' | relative_url }}">検証基盤 →</a></li>
</ul>
</div>

<div class="note-box">
<strong>運用方針</strong>
<p>
このWikiは独立した主張集ではなく、既存ページの補足導線です。強い主張を増やすより、既存の論点を初学者が追える形に分解することを優先します。
</p>
</div>

</aside>
</main>
