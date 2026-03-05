---
layout: default
title: "Wiki：本人性評価と連続性テスト"
description: "L4 の本人性主張で、何をどうテストしたいのかを、記憶・価値観・学習・分岐・縦断の観点から初歩的に整理します。"
article_type: Wiki
subtitle: "哲学の話を、保留条件つきのテスト設計へ戻す"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Learning guide"
audience: "本人性の話を工学へ戻したい人、L4 の読み方で止まりやすい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload における L4『本人性主張』を、哲学用語の紹介ではなく『何をどうテストしたいのか』の観点から整理する wiki です。記憶、価値観、学習、縦断安定性、分岐時の扱いを、事前登録された連続性テストへどう落とすかを初歩から説明します。"
accuracy_note: "ここで述べるのは評価設計の入口です。どの条件で『同じ本人』と最終判定できるかは未解決であり、このページもその結論を与えるものではありません。"
page_highlights:
  - "本人性は『似ているか』だけではなく、どこで保留にするかが重要です。"
  - "記憶、価値観、学習、分岐、縦断ドリフトを別々に見ます。"
  - "L4 では、事前登録と失敗条件が特に重要になります。"
known_points:
  - "本人性の主張は、L0〜L3 より強く、単なる出力一致だけでは足りません。"
  - "記憶、価値観、学習履歴、条件変更への反応を分けて見る必要があります。"
  - "分岐や長期ドリフトがあると、本人性の主張はさらに難しくなります。"
unknown_points:
  - "どの組み合わせのテストを満たせば十分条件になるかは未解決です。"
  - "連続的移行が本人性を十分に守るかも、まだ証明されていません。"
wiki_links:
  - label: "Wiki: 本人性とコピー問題"
    url: "/wiki/personhood-and-copy-problem.html"
    description: "まず哲学的な土台へ戻りたい人向けです。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "L4 がどれだけ強い主張かを補います。"
  - label: "Wiki: 反事実・介入・摂動"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "条件変更への反応まで見たい理由を補います。"
  - label: "Wiki: state・trait・ドリフト"
    url: "/wiki/state-trait-and-drift.html"
    description: "縦断評価で短期状態と長期特徴をどう分けるかを補います。"
recommended_pages:
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い考え方</h2>
<p>
本人性を問うときに必要なのは、「同じように話すか」だけではありません。<strong>何が続いていて、何が崩れたら保留にするか</strong>を先に決めることが重要です。
</p>
</div>

<section class="section" id="why-l4-is-hard">
<h2 class="section-title">なぜ L4 は急に難しくなるのか</h2>
<p>
L1 や L2 では、精度や予測一致のように比較的はっきりした指標を置けます。しかし L4 では、「この記憶の一致だけで十分か」「価値観が少し変わったら別人か」「学習による変化はどこまで許容するか」といった問題が入ってきます。つまり、測定だけでなく<strong>判定ルール</strong>そのものが難しくなります。
</p>
</section>

<section class="section" id="what-to-separate">
<h2 class="section-title">まず分けて考えたい 5 項目</h2>
<table class="data-table">
<thead>
<tr>
<th>項目</th>
<th>何を見たいか</th>
<th>それだけでは足りない理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>記憶</strong></td>
<td>自伝的記憶やエピソードの整合性。</td>
<td>記憶再生だけで、主観的連続性まで言えるとは限りません。</td>
</tr>
<tr>
<td><strong>価値観・選好</strong></td>
<td>判断傾向や優先順位の一貫性。</td>
<td>短期の気分変動と長期の人格傾向を分ける必要があります。</td>
</tr>
<tr>
<td><strong>学習履歴</strong></td>
<td>新しい経験をどう取り込み、以前の傾向とどうつながるか。</td>
<td>学習すると変化するのは自然で、変化そのものを即不一致とは言えません。</td>
</tr>
<tr>
<td><strong>条件変更への反応</strong></td>
<td>未学習条件や介入で、どのように応答が分岐するか。</td>
<td>平常時だけ似ていても、分岐で大きく崩れる可能性があります。</td>
</tr>
<tr>
<td><strong>縦断安定性</strong></td>
<td>日内・日間・長期で、何が安定し何が揺れるか。</td>
<td>一度の測定だけでは、本人性の持続は見えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="example-tests">
<h2 class="section-title">どんな連続性テストを考えたいのか</h2>
<div class="key-points">
<h4>例として置きたいテスト群</h4>
<ul>
<li><strong>自伝的記憶整合：</strong>出来事の内容だけでなく、関連づけや優先度も追います。</li>
<li><strong>選好安定性：</strong>価値判断や選択傾向が、短期ノイズを超えて続いているかを見ます。</li>
<li><strong>学習連続性：</strong>新しい情報を与えたあと、更新の仕方がもとの傾向とつながるかを見ます。</li>
<li><strong>分岐検証：</strong>条件を変えたときに、どの時点から別個体として扱うべきかを記録します。</li>
<li><strong>長期ドリフト監視：</strong>数日から数週間で、変わる特徴と変わらない特徴を分けて追います。</li>
</ul>
</div>
<p>特に縦断評価の入口だけ先に整理したい場合は、<a href="state-trait-and-drift.html">Wiki: state・trait・ドリフト</a> が補講になります。</p>
</section>

<section class="section" id="prereg">
<h2 class="section-title">なぜ事前登録が特に重要なのか</h2>
<p>
本人性の評価は、あとから見ればいくらでも都合よく解釈できてしまいます。だからこそ、「何を一致とみなすか」「どの程度のズレで保留にするか」「どの分岐を別個体として扱うか」を、<strong>事前登録</strong>しておく必要があります。
</p>
<div class="note-box">
<strong>先に決めておきたいこと</strong>
<p>
テスト項目、採点ルール、観察期間、失敗条件、停止条件、分岐時の扱い、でございます。L4 ではこの部分が曖昧だと、結論全体が揺らぎます。
</p>
</div>
</section>

<section class="section" id="branching">
<h2 class="section-title">分岐が起きると何が難しいか</h2>
<p>
もし途中から 2 つの系が別々に学習し始めたら、最初はほぼ同じでも、時間とともに別の履歴を持ちます。このとき問題になるのは、「どの時点まで同じ評価単位として扱うか」「どこで別個体として分けるか」です。
</p>
<p>
したがって、L4 の評価では、単に似ているかだけでなく、<strong>分岐ログ</strong>と<strong>バージョン管理</strong>が重要になります。
</p>
</section>

<section class="section" id="what-not-claim">
<h2 class="section-title">この段階でまだ言わない方がよいこと</h2>
<table class="data-table">
<thead>
<tr>
<th>言いすぎやすい表現</th>
<th>より安全な読み替え</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>本人性が証明された</strong></td>
<td>事前登録した連続性テスト群で、いまのところ重大な不一致が出ていない。</td>
</tr>
<tr>
<td><strong>同じ人が完全に保存された</strong></td>
<td>記憶・価値観・学習・分岐に関する暫定評価が成立した。</td>
</tr>
<tr>
<td><strong>長期的にも同一である</strong></td>
<td>観測期間内では、定義した指標に大きなドリフトが見られなかった。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">L4 の話を読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>何を続いているとみなすか：</strong>記憶、価値観、学習、分岐、縦断のどれを見ているか。</li>
<li><strong>事前登録があるか：</strong>あと出しで基準を変えていないか。</li>
<li><strong>失敗条件があるか：</strong>どんなズレなら保留にするかが明示されているか。</li>
<li><strong>観測期間が足りているか：</strong>一回の一致で長期本人性を言っていないか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
哲学寄りの入口へ戻るなら <a href="personhood-and-copy-problem.html">本人性とコピー問題</a>、L4 の位置づけへ戻るなら <a href="../wbe_101.html">WBE入門</a>、検証設計へ戻るなら <a href="../verification.html">検証基盤</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="personhood-and-copy-problem.html">本人性とコピー問題 →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
<li><a href="counterfactual-and-perturbation-verification.html">反事実・介入・摂動 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../wbe_101.html">WBE入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../tech_roadmap.html">技術ロードマップ →</a></li>
</ul>
</div>
</aside>
</main>
