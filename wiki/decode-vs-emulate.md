---
layout: default
title: "Wiki：Decode と Emulate"
description: "観測の翻訳としての decode と、内部因果を再現する emulate の違いを、一次文献と必要証拠で整理します。"
article_type: Wiki
subtitle: "出力一致は入口、介入一致と閉ループ安定性は別の壁です"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Technical / natural science only"
audience: "decode と emulate を、技術と自然科学の根拠だけで区別したい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload で重要な区別である decode と emulate の違いを、一次文献ベースで整理する補助ページです。何が '高性能な翻訳機' で、何が '内部状態を動かす系' に近いのかを、観測・介入・閉ループの証拠で見分けるために使います。"
accuracy_note: "ここで示すのは技術的な境界条件です。十分条件の最終合意や、WBE 全体の達成判定を単独で与えるページではありません。"
page_highlights:
  - "decode は観測からラベルや文を当てる主張で、emulate は内部状態の時間発展と介入応答を含む主張です。"
  - "Tang 2023 や Willett 2023 は decode の強い前進ですが、そのまま emulate ではありません。"
  - "Flesher 2021 や Berger 2011 のような局所閉ループ義継は、decode より一段強いが、なお全脳 emulation ではありません。"
known_points:
  - "decode は主に L1、局所的な閉ループ義継や介入応答は L2〜L3 に近い主張です。"
  - "出力一致だけでは、内部因果構造や状態変数の十分性を示せません。"
  - "OOD 一般化、摂動一致、閉ループ安定性を分けるだけで、誇大な読み替えはかなり減ります。"
unknown_points:
  - "どの程度の介入一致と状態変数の完全性があれば '十分に emulate した' と言えるかは未確定です。"
  - "局所回路の義継から全脳 emulation へどう外挿できるかは、まだ公開 benchmark がありません。"
wiki_links:
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "L0〜L5 の強さと必要な証拠へ戻せます。"
  - label: "Wiki: 配線図だけでは足りない理由"
    url: "/wiki/connectome-is-not-enough.html"
    description: "state completeness の欠損を整理します。"
  - label: "Wiki: 閉ループ・遅延・ジッタ・安全停止"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "L3 で必要な end-to-end 条件を補います。"
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
<h2>まず結論を一言でいうと</h2>
<p>
decode は「観測された信号から何かを当てること」、emulate は「内部状態が時間発展し、条件変更や介入にも整合的に応答すること」です。見た目の出力が似ていても、<strong>同じ因果機構で動いている</strong>とは限りません。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。技術と自然科学の側面だけから、decode を emulate と読み替えてよい条件が何かを整理します。
</p>
</div>

<section class="section" id="simple-table">
<h2 class="section-title">いちばん短い違い</h2>
<table class="data-table">
<thead>
<tr>
<th>観点</th>
<th>Decode</th>
<th>Emulate</th>
<th>最低限ほしい検証</th>
</tr>
</thead>
<tbody>
<tr>
<td>何を再現するか</td>
<td>観測から状態、刺激、意味、運動意図などを推定します。</td>
<td>内部状態が時間発展し、将来の出力や介入応答を生みます。</td>
<td>教師あり予測精度だけでなく、時間発展と条件変更を評価します。</td>
</tr>
<tr>
<td>強み</td>
<td>観測された条件で高性能になりやすく、実用 BCI へ直結しやすいです。</td>
<td>介入、反事実、閉ループ制御に対してより強い主張ができます。</td>
<td>OOD 一般化、摂動一致、閉ループ安定性を分けて評価します。</td>
</tr>
<tr>
<td>不足時の誤読</td>
<td>相関的翻訳を「内部再現」と言い換えやすいです。</td>
<td>出力一致だけで「忠実再現」と誤読しやすいです。</td>
<td>状態変数の完全性と同定可能性を別に監査します。</td>
</tr>
<tr>
<td>典型的な失敗モード</td>
<td>被験者内・課題内では高精度でも、未学習条件や別日で崩れます。</td>
<td>挙動が合って見えても、異なる内部パラメータで同じ出力が出ることがあります。</td>
<td>分割単位、再較正回数、介入後誤差、棄権条件を開示します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="paper-ladder">
<h2 class="section-title">一次文献で見る境界事例</h2>
<table class="data-table">
<thead>
<tr>
<th>実例</th>
<th>いま達成していること</th>
<th>なぜそのまま emulate ではないか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tang et al. (2023)</strong><br>非侵襲 semantic decoding</td>
<td>fMRI から連続言語の意味復元を示し、perceived speech、imagined speech、silent video にまたがる decode を実証しました。</td>
<td>被験者協力が学習・適用の双方で必要であり、観測された semantic representation の翻訳です。内部因果構造や介入応答の再現は示していません。</td>
</tr>
<tr>
<td><strong>Willett et al. (2023)</strong><br>侵襲 speech BCI</td>
<td>intracortical array から 125,000 語語彙で 62 words/min の large-vocabulary speech decoding を示しました。</td>
<td>高帯域であっても、主張の中心は attempted speech の decode です。自律的な内部生成や、条件変更への因果的一致までは示していません。</td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong><br>双方向 closed-loop BCI</td>
<td>motor decode に tactile feedback を返すことで、ロボット把持課題の所要時間を 20.9 秒から 10.2 秒へ短縮しました。</td>
<td>decode より一段強い局所閉ループ実証ですが、対象は感覚運動サブシステムです。全脳 emulation ではなく、<strong>局所回路での L3 に近い証拠</strong>として読むのが妥当です。</td>
</tr>
<tr>
<td><strong>Berger et al. (2011)</strong><br>海馬義継</td>
<td>CA3-CA1 の MIMO モデルから得た刺激パターンを real-time closed loop で用い、記憶課題の成績回復を示しました。</td>
<td>局所的な回路置換・補助として重要ですが、状態空間は課題特異的で、全脳・長期・多領域の一般化は未実証です。</td>
</tr>
<tr>
<td><strong>MICrONS (2025) / Billeh et al. (2020)</strong><br>digital twin / multi-scale model</td>
<td>function + connectomics を結んだ mouse visual cortex dataset と、data-driven な V1 multi-scale model が公開されました。</td>
<td>これは emulate に近い方向の基盤ですが、領域・個体・課題が限定されています。さらに Prinz et al. (2004) が示すように、似た出力が異なる内部パラメータから生じうるため、出力一致だけでは忠実再現とは言えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="gates">
<h2 class="section-title">decode を emulate と読み替える前の 4 つのゲート</h2>
<table class="data-table">
<thead>
<tr>
<th>ゲート</th>
<th>なぜ必要か</th>
<th>最低限ほしい証拠</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>G1: 未学習条件で保つか</strong></td>
<td>学習済み条件だけで高精度でも、機構が合っているとは限りません。</td>
<td>OOD 条件、別日、別刺激集合、被験者外評価での誤差分布と棄権率。</td>
</tr>
<tr>
<td><strong>G2: 介入に応答するか</strong></td>
<td>emulate を名乗るなら、観測だけでなく摂動後の分岐も当てる必要があります。</td>
<td>刺激変更、ICMS/TMS、薬理、課題ルール変更に対する予測一致。</td>
</tr>
<tr>
<td><strong>G3: 閉ループで安定か</strong></td>
<td>出力が次の入力を変えると、オフライン精度はそのまま通用しません。</td>
<td>end-to-end 遅延、ジッタ、再較正頻度、freeze / safety stop 条件。</td>
</tr>
<tr>
<td><strong>G4: 状態変数が足りているか</strong></td>
<td>同じ出力でも異なる内部パラメータ集合がありえます。状態欠損を伏せると過大主張になります。</td>
<td>cell type、synaptic state、delay、neuromodulation、glia をどう取得・推定・棄権したかの監査。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">このサイトでの運用ルール</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>decode と書く条件：</strong>観測信号から意味、刺激、行動、文章を予測する実証が中心で、介入一致までは示していないときです。</li>
<li><strong>局所 emulation と書ける条件：</strong>局所回路で、closed loop と因果介入の双方が示され、何を置換したかが限定的に明示されているときです。</li>
<li><strong>WBE に近いと書く条件：</strong>OOD 一般化、摂動一致、閉ループ安定性、状態変数の完全性監査の 4 点がそろったときだけです。</li>
<li><strong>出力一致だけのとき：</strong>avatar、behavioral clone、decoder、language interface といった表現に留め、emulate と言い換えません。</li>
<li><strong>局所義継の扱い：</strong>Berger や Flesher のような研究は非常に重要ですが、全脳 claim へ外挿せず、サブシステムの証拠として位置づけます。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Tang, J., LeBel, A., Jain, S., et al. (2023). Semantic reconstruction from non-invasive brain recordings. <em>Nature Neuroscience</em>, 26, 858–866. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <em>Nature</em>, 620, 1031–1036. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Flesher, S. N., Downey, J. E., Weiss, J. M., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science</em>, 372(6544), 831–836. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Berger, T. W., Hampson, R. E., Song, D., et al. (2011). A cortical neural prosthesis for restoring and enhancing memory. <em>Journal of Neural Engineering</em>, 8(4), 046017. <a href="https://doi.org/10.1088/1741-2560/8/4/046017" target="_blank">doi:10.1088/1741-2560/8/4/046017</a></li>
<li>Dorkenwald, S., McKellar, C. E., Macrina, T., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Billeh, Y. N., Cai, B., Gratiy, S. L., et al. (2020). Systematic Integration of Structural and Functional Data into Multi-scale Models of Mouse Primary Visual Cortex. <em>Neuron</em>, 106(3), 388–403.e18. <a href="https://doi.org/10.1016/j.neuron.2020.01.040" target="_blank">doi:10.1016/j.neuron.2020.01.040</a></li>
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <em>Nature Neuroscience</em>, 7, 1345–1352. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
</ol>
</section>

<section class="section" id="why-matters">
<h2 class="section-title">なぜこの区別が重要か</h2>
<p>
この区別がないと、「脳信号から文章を出せた」「closed loop で少し良くなった」「digital twin が動いた」という個別の前進を、そのまま WBE 全体の達成と誤読してしまいます。Mind-Upload では、この飛躍を避けるためにクレーム階段と検証基盤を先に置いています。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>主張レベルと必要な証拠の強さを合わせて見たい場合はこちらです。</p>
<a href="claims-and-evidence.html">主張と証拠の読み方へ →</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
<li><a href="eeg-basics.html">EEGの基本 →</a></li>
<li><a href="consciousness-theory-map.html">意識理論マップ →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
<li><a href="../faq.html">FAQ →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
