---
layout: default
title: "観測量と代理指標"
description: "Mind-Upload で何を直接見ていて、何を代理指標として使っているのかを初歩から整理します。"
article_type: Wiki
subtitle: "『測れた』と『分かった』を混同しないための入口"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Cross-cutting guide"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>TL;DR</h2>
<p>
Mind-Upload では、脳そのものを丸ごと直接読んでいるわけではありません。実際には、<strong>観測量</strong>、<strong>代理指標</strong>、<strong>潜在変数</strong>を混ぜながら推定しています。この区別が曖昧なままだと、強い主張ほど崩れやすくなります。
</p>
</div>

<section class="section" id="basics">
<h2 class="section-title">まず区別するべき5語</h2>
<table class="data-table">
<thead>
<tr>
<th>語</th>
<th>初歩的な意味</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測量</strong></td>
<td>装置や手順を通して実際に記録した量です。</td>
<td>EEG 電位、反応時間、心拍、エネルギー消費</td>
</tr>
<tr>
<td><strong>代理指標</strong></td>
<td>本当に知りたいものの代わりとして使う量です。</td>
<td>PCI を意識状態の代理として使う、再認成績を記憶の代理として使う</td>
</tr>
<tr>
<td><strong>潜在変数</strong></td>
<td>直接は見えないが、モデル内で仮定する内部状態です。</td>
<td>内部信念、潜在表現、結合強度、ネットワーク状態</td>
</tr>
<tr>
<td><strong>交絡</strong></td>
<td>本命以外なのに結果を動かしてしまう要因です。</td>
<td>疲労、装着ずれ、薬理、課題難易度、言語モデルの事前知識</td>
</tr>
<tr>
<td><strong>終点</strong></td>
<td>最終的に合格か不合格かを判定する量です。</td>
<td>反事実一致率、閉ループ安定性、本人性ベンチの保持率</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="layers">
<h2 class="section-title">観測量は層ごとに役割が違います</h2>
<table class="data-table">
<thead>
<tr>
<th>層</th>
<th>何を測るか</th>
<th>何に使えるか</th>
<th>それだけでは足りない理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>センサー層</strong></td>
<td>EEG, MEG, fMRI, ECoG, 生理指標</td>
<td>状態推定の入力、QC、同期監査</td>
<td>計測限界とノイズが大きく、内部原因が一意に決まりません。</td>
</tr>
<tr>
<td><strong>ソース推定層</strong></td>
<td>ESI, 逆問題解、潜在状態</td>
<td>回路仮説の候補作り</td>
<td>前向きモデルと正則化に強く依存します。</td>
</tr>
<tr>
<td><strong>行動層</strong></td>
<td>選択、反応時間、誤答、自己報告</td>
<td>機能評価、本人性ベンチの一部</td>
<td>模倣でも近い結果が出るため、因果保存の証拠としては弱いです。</td>
</tr>
<tr>
<td><strong>介入応答層</strong></td>
<td>刺激変更、局所介入、閉ループ制御への応答</td>
<td>因果同値や安定性の検証</td>
<td>反事実の正解を作る設計が難しく、負荷も高いです。</td>
</tr>
<tr>
<td><strong>運用層</strong></td>
<td>再現コスト、監査ログ、失敗率、消費電力</td>
<td>公共財としての比較、社会実装判断</td>
<td>性能スコアほど標準化されていません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="unknowns">
<h2 class="section-title">まだ分かっていないこと</h2>
<table class="data-table">
<thead>
<tr>
<th>何が未解決か</th>
<th>なぜ未解決か</th>
<th>何が分かると嬉しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>代理指標の妥当性</strong><br>その指標が本当に狙った概念を表しているか。</td>
<td>意識、本人性、内部信念のように、直接測れない対象が多いからです。</td>
<td>強い主張を、弱い観測から言い過ぎる事故を減らせます。</td>
</tr>
<tr>
<td><strong>指標間の不一致</strong><br>行動、脳活動、主観報告が食い違うとき何を優先するか。</td>
<td>層ごとにノイズ源も時間スケールも違うためです。</td>
<td>U0, U4, U11 の判定を一貫した規則で行えます。</td>
</tr>
<tr>
<td><strong>縦断安定性</strong><br>日をまたいでも残る観測量は何か。</td>
<td>覚醒、疲労、薬理、装着状態で観測が大きく変わるためです。</td>
<td>本人性や個人化の議論を、単発セッション依存にしなくて済みます。</td>
</tr>
<tr>
<td><strong>観測量の最小集合</strong><br>何を測れば十分で、何は省略できるか。</td>
<td>課題別に必要情報が異なり、共通物差しが未熟だからです。</td>
<td>高コスト計測を乱発せず、現実的なロードマップを引けます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="u-links">
<h2 class="section-title">U0〜U15 とどうつながるか</h2>
<div class="key-points">
<h4>Examples</h4>
<ul>
<li><strong>U0 操作的同一性：</strong>どの観測量を同一性判定に使うかが土台です。</li>
<li><strong>U2 時空間解像度：</strong>必要な観測量を取るのに十分な分解能があるかを問います。</li>
<li><strong>U7 マルチモーダル整合：</strong>異なる観測量同士を時刻と座標で合わせる必要があります。</li>
<li><strong>U10 熱力学的一貫性：</strong>性能だけでなく散逸や効率も観測量に入れる必要があります。</li>
<li><strong>U13 模倣分離：</strong>行動スコアだけでなく介入応答も見る必要があります。</li>
</ul>
</div>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>「観測した量」と「主張したい概念」の距離を明示できます。</li>
<li>ベンチ設計で、何が入力で何が終点かを混同しにくくなります。</li>
<li>未解決問題ごとに、本当に必要な測定を絞りやすくなります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></li>
<li><a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI →</a></li>
<li><a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答 →</a></li>
<li><a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計 →</a></li>
<li><a href="{{ '/wiki/unsolved-questions.html' | relative_url }}">未解決問題カタログ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/datasets.html' | relative_url }}">データ&ベンチ →</a></li>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
<li><a href="{{ '/tech_roadmap.html#measurement' | relative_url }}">Roadmap: 計測 →</a></li>
</ul>
</div>

</aside>
</main>
