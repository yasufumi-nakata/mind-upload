---
layout: default
title: "Wiki：熱力学的接地の基本"
description: "Landauer、散逸、NESS、EPR がなぜ Mind-Upload で出てくるのかを初歩から整理します。"
article_type: Wiki
subtitle: "情報が回るだけでなく、どういう物理的コストで回るかを見る入口です"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Learning guide"
audience: "Landauer、NESS、EPR、散逸構造の意味で止まりやすい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload で熱力学の話がなぜ出てくるのかを、Landauer、散逸、非平衡定常状態（NESS）、エントロピー生成速度（EPR）の観点から初歩から整理する wiki です。理論ページで急に物理の話に見えて止まる人のための入口として使います。"
accuracy_note: "ここで示すのは熱力学的接地の入口です。熱力学指標が意識や本人性の十分条件になると確定したわけではなく、サイト内でも未解決問題として扱っています。"
page_highlights:
  - "Landauer 下限と、実際の脳やエミュレーションのエネルギー消費は同じ話ではありません。"
  - "NESS と EPR は『動き続ける系』を見るための言葉です。"
  - "熱力学の話は、仮説を強める補助線であって、単独で結論を出す魔法の指標ではありません。"
known_points:
  - "生物学的脳は、静止したデータではなくエネルギーを流し続ける系です。"
  - "論理的な計算コストと、物理的な散逸コストは分けて考える必要があります。"
  - "熱力学指標を検証へ入れる発想はありますが、計測と解釈はまだ難しいままです。"
unknown_points:
  - "どの熱力学指標が意識や本人性のどの側面に効くかは未確定です。"
  - "EPR や散逸の代理指標を、どこまで神経データから安定に推定できるかは未解決です。"
wiki_links:
  - label: "Wiki: 意識理論マップ"
    url: "/wiki/consciousness-theory-map.html"
    description: "理論の役割差へ戻れます。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "熱力学指標を評価へ入れる位置づけを補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の補助ページへ戻れます。"
recommended_pages:
  - label: "理論フレーム"
    url: "/perspective.html#design-principles"
  - label: "研究ノート"
    url: "/perspective.html"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い答え</h2>
<p>
Mind-Upload で熱力学の話が出るのは、「情報が似ているか」だけでなく、<strong>その情報処理がどういう物理的コストで維持されるか</strong>も見たいからです。静止したデータの保存ではなく、動き続けるプロセスを問題にするなら、散逸や非平衡性を無視しにくくなります。
</p>
</div>

<section class="section" id="why-thermodynamics">
<h2 class="section-title">なぜここで熱力学が出てくるのか</h2>
<p>
このサイトでは、WBE を「静的なコピー」より「動き続ける過程の引き継ぎ」として扱います。そうすると、「何を計算したか」だけでなく、「その計算がどのような物理的流れの上で維持されるか」も論点に入ります。
</p>
<div class="note-box">
<strong>安全な読み方</strong>
<p>
これは「熱力学が分かれば意識が分かる」という意味ではありません。むしろ、「情報指標だけでは見落とす物理的制約があるかもしれない」という未解決問題として扱っています。
</p>
</div>
</section>

<section class="section" id="terms">
<h2 class="section-title">まず 4 つの言葉を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ざっくり意味</th>
<th>注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Landauer 下限</strong></td>
<td>情報の消去など、論理的に不可逆な計算に必要な最小コストの話です。</td>
<td>実際の脳や計算機が、その下限ぴったりで動くわけではありません。</td>
</tr>
<tr>
<td><strong>散逸（dissipation）</strong></td>
<td>エネルギーが不可逆に失われることです。</td>
<td>論理コストと物理的散逸コストは分けて見ます。</td>
</tr>
<tr>
<td><strong>NESS</strong></td>
<td>非平衡定常状態です。外からエネルギーを受けつつ、一定の状態を保つ系を指します。</td>
<td>脳のような動き続ける系を考えるときによく出ます。</td>
</tr>
<tr>
<td><strong>EPR</strong></td>
<td>エントロピー生成速度です。どれだけ不可逆な流れが起きているかの指標です。</td>
<td>直接測るのは難しく、代理指標や下界推定の議論が多いです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-is-not-being-claimed">
<h2 class="section-title">ここで言っていないこと</h2>
<table class="data-table">
<thead>
<tr>
<th>言いすぎやすい表現</th>
<th>より安全な読み替え</th>
</tr>
</thead>
<tbody>
<tr>
<td>「Landauer を満たせば意識も保存される」</td>
<td>Landauer は下限の話であり、本人性や意識の十分条件ではありません。</td>
</tr>
<tr>
<td>「EPR が同じなら同じ本人だ」</td>
<td>EPR は候補指標の 1 つであり、単独で L4 を決めるものではありません。</td>
</tr>
<tr>
<td>「脳は 20W だから、同じ電力なら十分だ」</td>
<td>総消費電力だけでなく、通信と計算の比率や散逸の仕方も別問題です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-logical-vs-physical">
<h2 class="section-title">論理コストと物理コストを分ける</h2>
<p>
FLOPs のような論理的計算量は、「どれくらい計算したか」を見る指標です。一方で熱力学的散逸は、「その計算をどんな物理的コストで回したか」を見ます。どちらか一方だけでは、動き続ける実装の難しさを十分に表せません。
</p>
</section>

<section class="section" id="what-can-be-said-now">
<h2 class="section-title">いま比較的強く言えること / まだ弱いこと</h2>
<table class="data-table">
<thead>
<tr>
<th>比較的強く言えること</th>
<th>まだ弱いこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>情報処理と物理コストを分けて記録した方が、実装比較は誤読しにくくなります。</td>
<td>どの熱力学指標が意識の質や本人性に直結するかは未確定です。</td>
</tr>
<tr>
<td>脳のような動的系を考えるなら、非平衡性や散逸を無視しない方が安全です。</td>
<td>EPR や NESS を神経データから標準的に推定する方法はまだ確立していません。</td>
</tr>
<tr>
<td>総電力だけでなく、通信対計算の比率を見る発想は有用です。</td>
<td>その比率がどこまで WBE の成立条件に効くかは未解決です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">熱力学の主張を読むときの 3 問</h2>
<ol>
<li><strong>これは下限の話か、実測の話か：</strong>Landauer のような理論下限と、実際の消費や散逸を混同しないことが重要です。</li>
<li><strong>論理コストと物理コストを分けているか：</strong>FLOPs と散逸を 1 つの数字にまとめていないかを見ます。</li>
<li><strong>この指標だけで何を言おうとしているか：</strong>EPR や NESS を、単独で本人性や意識の証明に使っていないかを確認します。</li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
理論フレームへ戻るなら <a href="../perspective.html#design-principles">理論フレーム</a>、長文の研究ノートへ戻るなら <a href="../perspective.html">研究ノート</a>、検証要件へ戻るなら <a href="../verification.html">検証基盤</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="consciousness-theory-map.html">意識理論マップ →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../perspective.html#design-principles">理論フレーム →</a></li>
<li><a href="../perspective.html">研究ノート →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
