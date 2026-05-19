---
layout: default
title: "逆問題とESI"
description: "順問題、逆問題、EEG Source Imaging、同定可能性、不確実性定量化を初歩から整理します。"
article_type: Wiki
subtitle: "『見えた脳』ではなく『推定した脳』であることを忘れない"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Concept Deep Dive"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>TL;DR</h2>
<p>
EEG の頭皮電位から脳内ソースを推定する作業は、<strong>逆問題</strong>です。逆問題は一般に一意に解けません。だから ESI の結果は「真実そのもの」ではなく、<strong>仮定つきの推定</strong>として扱う必要があります。
</p>
</div>

<section class="section" id="forward-inverse">
<h2 class="section-title">順問題と逆問題</h2>
<table class="data-table">
<thead>
<tr>
<th>問題</th>
<th>意味</th>
<th>典型例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>順問題</strong></td>
<td>脳内にこのソースがあるとき、頭皮ではどう見えるか。</td>
<td>頭部モデルと導電率から電位分布を計算する。</td>
</tr>
<tr>
<td><strong>逆問題</strong></td>
<td>頭皮でこの信号が見えたとき、脳内で何が起きていたか。</td>
<td>EEG から皮質上の活動分布を推定する。</td>
</tr>
</tbody>
</table>
<p>
順問題は、仮定が定まれば比較的よく定義できます。逆問題は、複数の脳内配置が同じ頭皮パターンを作れるため、不良設定になりやすいです。
</p>
</section>

<section class="section" id="esi">
<h2 class="section-title">ESI で何をしているか</h2>
<div class="key-points">
<h4>ESI Workflow</h4>
<ul>
<li><strong>頭部モデルを置く：</strong>MRI やテンプレートから形状を決める。</li>
<li><strong>ソース空間を置く：</strong>皮質上に候補点や領域を置く。</li>
<li><strong>事前仮定を置く：</strong>滑らかさ、疎性、ベイズ事前分布など。</li>
<li><strong>不確実性を評価する：</strong>信用区間、事後分布、感度分析を出す。</li>
</ul>
</div>
</section>

<section class="section" id="uncertainty">
<h2 class="section-title">どこから不確実性が入るか</h2>
<table class="data-table">
<thead>
<tr>
<th>不確実性の源</th>
<th>何が揺れるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>導電率</strong></td>
<td>頭蓋骨や組織の伝導特性が変わり、順モデル自体が揺れます。</td>
</tr>
<tr>
<td><strong>頭部形状</strong></td>
<td>テンプレート使用やセグメンテーション誤差で、ソース位置がずれます。</td>
</tr>
<tr>
<td><strong>ノイズモデル</strong></td>
<td>眼球運動、筋電、ラインノイズで事後分布が広がります。</td>
</tr>
<tr>
<td><strong>事前仮定</strong></td>
<td>疎な解を好むか、滑らかな解を好むかで結果が変わります。</td>
</tr>
</tbody>
</table>
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
<td><strong>どこまで一意化できるか</strong><br>どの条件なら逆問題を強く制約できるか。</td>
<td>観測数より潜在変数の方が多くなりやすいからです。</td>
<td>ESI の解釈を強く言えません。</td>
<td>どんな追加モダリティが必要か判断できます。</td>
</tr>
<tr>
<td><strong>不確実性の伝播</strong><br>ESI の曖昧さを後段モデルへどう渡すか。</td>
<td>多くの解析が点推定前提で組まれているからです。</td>
<td>因果モデルや生成モデルに誤差が埋め込まれます。</td>
<td>より誠実な downstream 解析ができます。</td>
</tr>
<tr>
<td><strong>個人差の扱い</strong><br>頭部形状や導電率の差をどう吸収するか。</td>
<td>個人ごとに十分な追加計測を取れないことが多いからです。</td>
<td>クロス個体比較が難しいです。</td>
<td>長期追跡や群比較の精度が上がります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>ESI の結果を、観測と推定に分けて読めます。</li>
<li>不確実性つき報告が必要な理由を説明できます。</li>
<li>計測だけでなく、モデリングと監査の設計にもつながります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u1-inverse-identifiability.html' | relative_url }}">U1 逆問題の同定可能性 →</a></li>
<li><a href="{{ '/wiki/u2-resolution-limits.html' | relative_url }}">U2 時空間解像度 →</a></li>
<li><a href="{{ '/wiki/u7-multimodal-alignment.html' | relative_url }}">U7 マルチモーダル整合 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/eeg_101.html#esi-uncertainty' | relative_url }}">EEG入門: ESI不確実性 →</a></li>
<li><a href="{{ '/perspective.html#technical-framework' | relative_url }}">Perspective: Technical Framework →</a></li>
<li><a href="{{ '/verification.html#verification-rigor' | relative_url }}">Verification: 厳密性要件 →</a></li>
</ul>
</div>

</aside>
</main>
