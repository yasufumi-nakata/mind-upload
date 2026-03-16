---
layout: default
title: "50-Worker Research Harvest: 未解決問題を分解した文献地図"
description: "50分解クエスチョンで収集した先行研究を、解決済み領域と未解決領域に切り分けて公開。"
article_type: "Evidence Bank"
subtitle: "U0-U15 の分解、現状評価、先行研究（大量引用）"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Compiled from 50 worker tasks (curated for relevance)"
audience: "大量の文献を『何が未解決か』ごとに見たい人、論点別に引用を探したい人"
reading_time: "20〜35分（統計とU別マップだけなら7分）"
page_intro: "このページは、ばらばらに集めた文献を『未解決問題ごと』に並べ直したエビデンスバンクです。論文数の多さで圧倒するのではなく、『どこまで解けていて、どこから先が未解決か』を先に見えるようにしています。"
accuracy_note: "引用数の多さは、そのまま結論の強さを意味しません。関連度・質・未解決性を分けて読む必要があります。"
page_highlights:
  - "U0〜U15ごとに、解決済みの部分と未解決の部分を分けて示しています。"
  - "入力受理ログと学術統合済みの部分を分け、混入防止の手順も明示しています。"
  - "大量引用ページですが、統計と現状マップだけでも全体像を先に把握できます。"
  - "技術・自然科学の既定入口は、U1/U7→U4/U13→U8→U3→U10 の順に固定しました。"
  - "技術・自然科学では、source_logged / curated とは別に evidence class も分けて読みます。"
known_points:
  - "U0〜U15 ごとに論点を分けると、文献の量と結論の強さを混同しにくくなります。"
  - "source_logged / curated / noise_excluded を分けることで、入力受理と学術統合を混ぜない運用ができます。"
  - "引用数の多さは、結論の確定ではなく関心や関連度の厚みとして読む必要があります。"
  - "技術・自然科学の入口では、受理ログや制度論より先に、計測・直接妥当化・閉ループ安定性・maintenance-state を優先して読む方が安全です。"
  - "技術・自然科学では、Uごとに『何を直接増やす文献か』も別軸で見た方が誤読しにくくなります。"
unknown_points:
  - "各 U に十分な証拠が揃っているわけではなく、探索段階の領域も残っています。"
  - "source_logged の項目は、今後の精査で統合先や除外判断が変わる可能性があります。"
  - "U マップそのものも、今後の文献追加で更新され得ます。"
  - "どの優先ルートが将来の WBE 検証基盤へ最も強く効くかは、direct validation と長期縦断ベンチの整備状況で変わり得ます。"
wiki_links:
  - label: "Wiki: U番号ガイド"
    url: "/wiki/u-number-guide.html"
    description: "U番号を日常語で読み替え、どの塊から見ればよいかを整理します。"
  - label: "Wiki: 部分解決・探索段階・未整備の読み方"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "部分解決、探索段階、未標準化、不足などの意味を整理します。"
  - label: "Wiki: 文献と証拠ページの読み方"
    url: "/wiki/literature-and-evidence-reading.html"
    description: "論文アーカイブ、文献地図、提案ページの違いを初歩から整理します。"
  - label: "Wiki: 文献のソース種別と状態ラベル"
    url: "/wiki/paper-source-types-and-evidence-status.html"
    description: "Scopus、arXiv、Review、Media、source_logged などの意味を整理します。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "なぜ文献の数だけでなく、評価軸と未解決問題が重要かを補います。"
  - label: "Wiki: 熱力学的接地の基本"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "U10 で出る Landauer、散逸、NESS、EPR の入口を初歩から整理します。"
recommended_pages:
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "論文集"
    url: "/mind_uploading_papers.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>要旨</h2>
<p>本ページは、1つの大きな問いを50個の調査タスクへ分解して集めた先行研究を、未解決問題（U0-U15）に再配置したエビデンスバンクです。単なる提案ではなく、URL付き引用をベースに『今どこまで解けているか』と『何が未解決か』を分離して示します。</p>
</div>

<div class="key-points">
<h4>先に見れば十分な場所</h4>
<ul>
<li><strong>まず全体像だけ知りたい：</strong>「収集と選別の統計」と「U別の現状マップ」を見てください。</li>
<li><strong>個別論点を追いたい：</strong>自分が気になるU番号から入り、そこで引用されている文献へ進んでください。</li>
<li><strong>このページでしないこと：</strong>引用を並べただけで、各理論の正しさを自動的に保証することはしません。</li>
</ul>
</div>

<div class="note-box">
<strong>迷ったときの読み順</strong>
<p>
最初に統計と品質ゲートで「どうやって混入を防いだか」を確認し、その次に U 別の現状マップで未解決の中心を掴んでください。個別引用を精読するのは、そのあとで十分です。
</p>
</div>

<div class="note-box">
<strong>文献ページに慣れていないとき</strong>
<p>
このページは「論文の山」ではなく「未解決問題ごとの地図」です。論文アーカイブとの違いや、どこまでを確定扱いしないかを先に知りたい場合は、<a href="wiki/literature-and-evidence-reading.html">Wiki: 文献と証拠ページの読み方</a> から入ると迷いにくくなります。
</p>
</div>
<div class="note-box">
<strong>文献を読んだあとにどこへ戻すか迷ったとき</strong>
<p>
この文献地図で論文を見つけたあとに、提案へつなぐのか、Issue に落とすのか、外部依存・協業節の準備物へ変えるのかを一本道で見たい場合は <a href="wiki/literature-to-action-route.html">Wiki: 文献から実装・参加へ戻る一本道</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>文献から提案・Issue・外部依存整理までの全体フローを見たいとき</strong>
<p>
文献整理、理論整理、提案、実行タスク、外部依存の流れを 1 枚で見たい場合は <a href="wiki/reading-to-change-workflow.html">Wiki: 読んだ内容を変更へつなぐ流れ</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>要約で止めてよい場面と、原文へ戻る場面を分けたいとき</strong>
<p>
このページの U 別整理や根拠例は入口として有効ですが、実際に根拠として使うときは DOI や元論文へ戻る必要があります。要約・原文・Issue 履歴の使い分けを 1 枚で見たい場合は <a href="wiki/summary-vs-source-reading.html">Wiki: 要約・原文・Issue履歴の使い分け</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>Scopus / Review / source_logged の意味で止まったとき</strong>
<p>
このページでは、掲載元、文献種別、サイト内状態に加えて、evidence class も混ざって見えやすいです。それぞれが何を示し、何をまだ保証しないかを先に整理したい場合は、<a href="wiki/paper-source-types-and-evidence-status.html">Wiki: 文献のソース種別・状態・証拠クラスの読み方</a> をご覧ください。
</p>
</div>

<div class="note-box">
<strong>U番号で身構えたとき</strong>
<p>
U番号は難しい理論名ではなく、「未解決問題の名前札」です。どの U がどんな塊かを日常語で掴みたい場合は、<a href="wiki/u-number-guide.html">Wiki: U番号ガイド</a> を先に見てください。
</p>
</div>
<div class="note-box">
<strong>部分解決や探索段階の意味で止まったとき</strong>
<p>
このページの「現状」は、合否ではなく不足箇所の種類を短く示すラベルです。<a href="wiki/progress-labels-and-open-problem-status.html">Wiki: 部分解決・探索段階・未整備の読み方</a> を先に見ると、「何がまだ足りないのか」を落ち着いて読めます。
</p>
</div>

<section class="section" id="technical-priority-route-20260315">
<h2 class="section-title">2026-03 技術・自然科学の優先ルート</h2>
<p>
このページの弱点は、<strong>入力受理ログ</strong>と<strong>実験フロンティア</strong>が近い位置に並ぶため、技術・自然科学の読者が「いま最も強い一次証拠はどこか」を入口で取り違えやすいことでした。そこで既定の読む順序を、<strong>計測と同定</strong>、<strong>直接妥当化と模倣分離</strong>、<strong>長期閉ループ安定性</strong>、<strong>connectome 外の maintenance-state</strong>、<strong>物理的接地</strong>の順に固定します。ここでの優先順位は、Tang ら (2023)、d'Ascoli ら (2025)、Willett ら (2023)、Littlejohn ら (2025)、Wairagkar ら (2025)、Unnwongse ら (2023)、Hao ら (2025)、Xu ら (2024)、Looser ら (2024)、Lee ら (2022) が示す現在の一次証拠の厚みに基づくものでございます。
</p>
<table class="data-table">
<thead>
<tr>
<th>優先ルート</th>
<th>先に見る U</th>
<th>ここでまず確かめること</th>
<th>まだ言ってはいけないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 計測と同定</strong></td>
<td><strong>U1 / U7</strong></td>
<td>逆問題の不確実性、取得関係、共有時計、侵襲校正、hemodynamic proxy ceiling を分けて読めるかです。</td>
<td>観測量が増えたことを、そのまま state-complete reconstruction と読むことです。</td>
</tr>
<tr>
<td><strong>2. 直接妥当化と模倣分離</strong></td>
<td><strong>U4 / U13</strong></td>
<td>decode 成功が、介入での因果保存や whole-brain emulation を意味しないことです。</td>
<td>brain-to-text や speech neuroprosthesis を、そのまま WBE 実証と呼ぶことです。</td>
</tr>
<tr>
<td><strong>3. 長期閉ループ安定性</strong></td>
<td><strong>U8</strong></td>
<td>latency、jitter、dropout、recalibration burden、recovery time を別指標で残せているかです。</td>
<td>within-session の成功だけで、週〜月スケールの運用可能性を断言することです。</td>
</tr>
<tr>
<td><strong>4. maintenance-state</strong></td>
<td><strong>U3</strong></td>
<td>sleep-dependent homeostasis、myelin/metabolic support、active maintenance を落としていないかです。</td>
<td>connectome と cell type だけで長期ダイナミクスが閉じたとみなすことです。</td>
</tr>
<tr>
<td><strong>5. 物理的接地</strong></td>
<td><strong>U10</strong></td>
<td>散逸、エネルギー制約、実効コストを後付けでなく反証条件として置けるかです。</td>
<td>計算可能性の議論だけで、物理実装の成立を済ませたことにすることです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>今回の主導線から外す群</strong>
<p>
<strong>U0 / U12 / U15</strong> は重要ですが、既定の技術・自然科学ルートには置きません。理由は、ここで先に必要なのが形而上学や法学ではなく、<strong>いま何が測れて、どこまで直接妥当化できて、どこで閉ループが壊れ、どの hidden state が残るか</strong>を固定することだからです。これらの群は、実験 front を読んだあとに戻る方が誤読しにくくなります。
</p>
</div>
</section>

<section class="section" id="evidence-class-rule-20260316">
<h2 class="section-title">2026-03 文献地図の共通 rule：state label と evidence class は別です</h2>
<p>
今回さらに深掘りして見えた弱点は、<strong>source_logged / curated</strong> のような <strong>サイト内状態</strong> と、<strong>その引用が U のどの部分を直接押し上げるか</strong> が、まだ十分に分離されていなかった点でございます。たとえば <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> は <strong>local direct validation</strong> を押し上げますが、<a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a>、<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>、<a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> は <strong>task-limited subsystem performance</strong> を押し上げる論文です。さらに <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns et al. (2024)</a>、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018)</a>、<a href="https://proceedings.mlr.press/v37/blum15.html" target="_blank">Blum &amp; Hardt (2015)</a>、<a href="https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html" target="_blank">Roelofs et al. (2019)</a> は <strong>再現・benchmark governance</strong> を押し上げます。したがって文献地図では、状態ラベルとは別に evidence class を見ます。
</p>
<table class="data-table">
<thead>
<tr>
<th>evidence class</th>
<th>Uマップでの役割</th>
<th>代表例</th>
<th>まだ解いたとみなさないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>direct validator / causal calibration</strong></td>
<td>U1/U7/U13 で、妥当化、誤差源、coverage boundary を直接押し上げます。</td>
<td><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan 2020</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse 2023</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao 2025</a></td>
<td>whole-brain truth や一般的一意復元は残ります。</td>
</tr>
<tr>
<td><strong>task-limited system demonstration</strong></td>
<td>U4/U8/U13 で、decode、speech neuroprosthesis、closed-loop subsystem を押し上げます。</td>
<td><a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang 2023</a>、<a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett 2023</a>、<a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn 2025</a></td>
<td>WBE 実証、本人性、state-complete reconstruction は残ります。</td>
</tr>
<tr>
<td><strong>dataset / benchmark / standard / toolchain</strong></td>
<td>U1/U7/U8 の比較可能性、同期、split、benchmark governance を押し上げます。</td>
<td><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet 2019</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns 2024</a>、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe 2025</a>、<a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant 2018</a></td>
<td>hidden state や mechanistic sufficiency を直接は解きません。</td>
</tr>
<tr>
<td><strong>review / synthesis / context</strong></td>
<td>論点の地図、周辺文脈、次に追う一次文献の当たり付けを与えます。</td>
<td>review、survey、総説、context 文献</td>
<td>単独では U の解決証拠にしません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>文献地図での読み方</strong>
<p>
もし引用が <strong>curated</strong> でも、その evidence class が <strong>dataset / benchmark</strong> なら、「比較条件が整った」とは読めますが、「hidden state が解けた」とは読みません。逆に <strong>task-limited demo</strong> が増えても、それだけで U4/U13 が閉じたとは書きません。状態ラベルは運用、evidence class は技術的効き方でございます。
</p>
</div>
</section>

<section class="section" id="u7-evidence-classes-20260316">
<h2 class="section-title">2026-03 U7 再監査：multimodal を 4 つの証拠クラスへ分けます</h2>
<p>
今回もっとも深掘りすべきだった弱点は、この文献地図の U7 が <strong>BIDS/LSL の器</strong>、<strong>同時計測の cross-modal concordance</strong>、<strong>coverage-limited な侵襲校正</strong>、<strong>fMRI 側の hemodynamic proxy ceiling</strong> を、まだ十分に別クラスとして見せ切れていなかった点でございます。これを混ぜると、技術読者は <strong>metadata が整っている</strong>ことを <strong>neural truth が強くなった</strong>ことと誤読しやすくなります。したがって U7 では、まず以下の 4 クラスに分けて証拠の直接性を見ます。
</p>
<table class="data-table">
<thead>
<tr>
<th>証拠クラス</th>
<th>代表一次文献</th>
<th>ここで直接強くなること</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 器と時計系</strong></td>
<td><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns et al. (2024)</a>、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe et al. (2025)</a></td>
<td>EEG-BIDS / Motion-BIDS / LSL により、metadata、座標系、共有時計、再解析可能なログを固定できます。</td>
<td>device-side delay の真値、融合後の不確実性、neural truth そのものは自動では増えません。</td>
</tr>
<tr>
<td><strong>2. 同時計測の cross-modal concordance</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">Jorge et al. (2015)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">Wirsich et al. (2021)</a></td>
<td>同一時点の macro-scale concordance、safety / artifact 管理の前提、shared clock 下での再現可能な相関構造が強くなります。</td>
<td>shared clock だけで trial-level causal order や mechanistic interpretation が閉じたとは言えません。</td>
</tr>
<tr>
<td><strong>3. coverage-limited な侵襲校正</strong></td>
<td><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a></td>
<td>既知刺激位置や同時 SEEG に対する local source validation、depth / power / conductivity 依存の誤差監査ができます。</td>
<td>whole-brain ground truth や一般的一意復元までは支えません。</td>
</tr>
<tr>
<td><strong>4. hemodynamic proxy ceiling</strong></td>
<td><a href="https://doi.org/10.1038/35084005" target="_blank">Logothetis et al. (2001)</a>、<a href="https://doi.org/10.1038/nature09108" target="_blank">Lee et al. (2010)</a>、<a href="https://doi.org/10.1038/nature07664" target="_blank">Sirotin &amp; Das (2009)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">Handwerker et al. (2004)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">Kay et al. (2019)</a>、<a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">Kurzawski et al. (2022)</a></td>
<td>BOLD が neurovascular proxy であり、HRF 変動、task-related haemodynamics、venous / non-neural bias が ceiling を作ることを固定できます。</td>
<td>EEG-fMRI を direct neural truth や fine-grained mechanism の証拠とは書けません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>U7 を読むときの site rule</strong>
<p>
U7 の文献は、<strong>器と時計系</strong>、<strong>同時計測の concordance</strong>、<strong>侵襲校正</strong>、<strong>proxy ceiling</strong> のどれに属するかを先にラベルしてください。もし 1 の証拠しか無いなら、それはまず <strong>再解析可能な基盤</strong>であって、multimodal gain の実証ではございません。逆に 2 と 3 があっても、4 の監査が欠ければ fMRI を neural truth と読み上げません。
</p>
</div>
</section>

<section class="section" id="stats">
<h2 class="section-title">収集と選別の統計</h2>
<ul>
<li><strong>Worker tasks:</strong> 50</li>
<li><strong>Raw citations:</strong> 499</li>
<li><strong>Curated citations:</strong> 302</li>
<li><strong>Dropped as noise/low-relevance:</strong> 97</li>
<li><strong>Unique citation keys:</strong> 292</li>
</ul>
</section>

<section class="section" id="quality-gate">
<h2 class="section-title">品質ゲート（混入防止）</h2>
<ol>
<li>U別キーワード一致 + 神経科学アンカー語を満たす文献のみ採用</li>
<li>無関係領域（宇宙論・腫瘍画像など）の混入を自動除外</li>
<li>重複（DOI/URL/タイトル）を統合し、スコア上位のみ残す</li>
<li>各Uに対して「解かれている範囲」と「未解決」を明示</li>
</ol>
</section>

<section class="section" id="intake-minimum">
<h2 class="section-title">文献を足すときの最低メモ</h2>
<table class="data-table">
<thead>
<tr>
<th>最低限残すこと</th>
<th>例</th>
<th>なぜ必要か</th>
</tr>
</thead>
<tbody>
<tr>
<td>どの U に関係するか</td>
<td>U4: 因果同値 / U11: 意識指標近似</td>
<td>関連先が決まらないまま文献を積むと、あとで未解決問題ごとの地図に戻せなくなるためです。</td>
</tr>
<tr>
<td>一次研究か、レビューか、ニュースか</td>
<td>Primary / Review / Media</td>
<td>同じ「参考文献」でも、結論の重みと追跡の仕方が違うためです。</td>
</tr>
<tr>
<td>一文での関係説明</td>
<td>「逆問題の不確実性定量を扱うため、U1 の根拠候補」</td>
<td>タイトルだけでは、なぜこのページに入るのか後から分からなくなるためです。</td>
</tr>
<tr>
<td>いまの状態</td>
<td>source_logged / curated / noise_excluded</td>
<td>受理済みログと、学術統合済みの根拠を混同しないためです。</td>
</tr>
<tr>
<td>元URLか DOI</td>
<td>DOI: 10.xxxx / arXiv: xxxx.xxxxx</td>
<td>第三者が同じソースへ戻れないと、引用の監査ができないためです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-meaning">
<h2 class="section-title">状態ラベルの意味</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベル</th>
<th>日常語で言うと</th>
<th>まだ残っている作業</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>source_logged</strong></td>
<td>入口として URL や DOI を受け付けた状態です。</td>
<td>関連性確認、一次研究追跡、U への割り当てがまだ残っています。</td>
</tr>
<tr>
<td><strong>curated</strong></td>
<td>このエビデンスバンクの論点に沿って整理済みの状態です。</td>
<td>他の U との重複や、より強い根拠との入れ替え余地は残ります。</td>
</tr>
<tr>
<td><strong>noise_excluded</strong></td>
<td>関連性が薄い、または混入と判断して除外した状態です。</td>
<td>除外理由を保持し、同じ種の混入を再発させないことが重要です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>状態ラベルを強さと混同しないために</strong>
<p>
<code>source_logged</code> は入力受理、<code>curated</code> は整理済み、<code>noise_excluded</code> は除外判断を意味します。Scopus や arXiv のような掲載元表示や、Review / Media のような文献種別とは別軸です。混ざって見える場合は <a href="wiki/paper-source-types-and-evidence-status.html">Wiki: 文献のソース種別と状態ラベルの読み方</a> に戻ってください。
</p>
</div>
</section>

<section class="section" id="recent-intake-2026-02">
<h2 class="section-title">最新追加入力（Issue #261–#263）</h2>
<p>
2026年2月23日に受領した内容追加Issue（#261–#263）に基づき、一次参照URLをエビデンスバンクへ登録しました。ここでは「受理済みリンク」と「学術統合前（要査読確認）」を分離して管理します。
</p>
<ol>
<li><strong>[Media]</strong> <a href="https://nazology.kusuguru.co.jp/archives/189938" target="_blank">AIに意識を宿すには「正しいコード」だけでは足りないかもしれない</a>（Issue #261）<br><span class="small">status=source_logged / 学術一次文献へのトレースを継続</span></li>
<li><strong>[Review]</strong> <a href="https://www.sciencedirect.com/science/article/pii/S0149763425005251?via%3Dihub" target="_blank">On biological and artificial consciousness: A case for biological computationalism</a>（Issue #262）<br><span class="small">status=source_logged / レビュー本文の精読要約は次回更新で実施</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2512.01591" target="_blank">Scaling and context steer LLMs along the same computational path as the human brain</a>（Issue #262）<br><span class="small">status=source_logged / WBE同一性検証への接続可能性を評価予定</span></li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2305.19798" target="_blank">Primal-Attention: Self-attention through Asymmetric Kernel SVD in Primal Representation</a>（Issue #263）<br><span class="small">status=source_logged / 直接関連性（U0-U15）の再スクリーニング対象</span></li>
</ol>
<div class="note-box">
<strong>運用メモ</strong>
<p>
本節は「入力受理ログ」です。採否判定（Uマップ反映、引用優先度、ノイズ除外）は品質ゲート手順に従い、後続の定期更新で確定します。
</p>
</div>
<div class="note-box">
<strong>技術・自然科学の既定入口ではありません</strong>
<p>
本節は frontier ranking ではなく intake queue です。したがって、技術・自然科学の一次証拠を追う場合は、この節からではなく上の <a href="#technical-priority-route-20260315">技術・自然科学の優先ルート</a>、または本文中の <strong>U1 / U7 / U4 / U13 / U8 / U3 / U10</strong> から入ってください。
</p>
</div>
</section>

<section class="section" id="u-overview">
<h2 class="section-title">U別の現状マップ</h2>
<div class="note-box">
<strong>この表の読み方</strong>
<p>
ここでの <strong>ID</strong> は問題の名前札、<strong>現状</strong> はどこまで解けているか、<strong>引用数</strong> は関連証拠の量です。引用数が多いことは、そのまま結論が確定していることを意味しません。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>自分の関心</th>
<th>先に見る U</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td>EEG推定、source imaging、時刻同期の限界を知りたい</td>
<td><strong>U1 / U7</strong></td>
<td>観測からどこまで推定できるか、direct validation・同期規約・hemodynamic gate がどう効くかが集まるためです。</td>
</tr>
<tr>
<td>decode 成功と WBE 主張を切り分けたい</td>
<td><strong>U4 / U13</strong></td>
<td>観測一致と因果保存、local communication と whole-brain emulation を分けて読めるためです。</td>
</tr>
<tr>
<td>長期 closed-loop の壊れ方を知りたい</td>
<td><strong>U8</strong></td>
<td>遅延、ジッタ、recalibration burden、長期 drift の論点がここに集まるためです。</td>
</tr>
<tr>
<td>connectome 外の hidden state を知りたい</td>
<td><strong>U3</strong></td>
<td>sleep / myelin / glia / metabolic support を含む maintenance-state の不足がここへ集まるためです。</td>
</tr>
<tr>
<td>物理コストや散逸まで含めて見たい</td>
<td><strong>U10</strong></td>
<td>計算量だけでなく、実装時の散逸とエネルギー制約を読む入口になるためです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>この表の既定読順</strong>
<p>
技術・自然科学の読者は、<strong>U1 / U7 → U4 / U13 → U8 → U3 → U10</strong> の順を既定にしてください。U11 は実験比較の二次ルート、U0 / U12 / U15 は主導線のあとに戻る補助ルートとして扱います。
</p>
</div>
<table class="data-table">
<thead><tr><th>大きな問題群</th><th>含まれるU</th><th>ざっくり何を見る群か</th></tr></thead><tbody>
<tr><td><strong>定義と評価</strong></td><td>U0 / U11 / U13 / U14</td><td>何を「同じ」と呼ぶか、模倣と検証をどう分けるか、追試をどう成立させるか。</td></tr>
<tr><td><strong>計測と推定</strong></td><td>U1 / U7</td><td>観測データからどこまで分かるか、複数モダリティをどう揃えるか。</td></tr>
<tr><td><strong>因果と実装安定性</strong></td><td>U4 / U8 / U10</td><td>介入で同じと言えるか、閉ループで壊れないか、物理的コストが破綻しないか。</td></tr>
<tr><td><strong>境界と本人性</strong></td><td>U3 / U12</td><td>どこまで含めれば主体と言えるか、分岐後の本人性をどう扱うか。</td></tr>
<tr><td><strong>制度と公開運用</strong></td><td>U15</td><td>技術だけでなく、停止基準・公開基準・責任の置き方まで含めて運用できるか。</td></tr>
</tbody></table>
<table class="data-table">
<thead><tr><th>ID</th><th>問題名</th><th>現状</th><th>引用数</th><th>未解決の中心</th></tr></thead><tbody>
<tr><td>U0</td><td>操作的同一性</td><td>部分解決</td><td>23</td><td>介入実験を含む同一性評価ベンチは未標準化。</td></tr>
<tr><td>U1</td><td>逆問題同定可能性</td><td>部分解決</td><td>26</td><td>被験者間・装置間の不確実性を横断した一般化誤差境界が不足。</td></tr>
<tr><td>U3</td><td>生物学的境界</td><td>部分解決</td><td>26</td><td>sleep/homeostasis・髄鞘/代謝支持・glia/clearance support の omission test と human proxy bridge が未標準化。</td></tr>
<tr><td>U4</td><td>因果同値</td><td>部分解決</td><td>26</td><td>高次元時系列での因果識別可能性がデータ条件に強く依存。</td></tr>
<tr><td>U7</td><td>マルチモーダル整合</td><td>部分解決</td><td>26</td><td>同期誤差の許容域をタスク別に定義した共通規約が不足。</td></tr>
<tr><td>U8</td><td>閉ループ安定性</td><td>部分解決</td><td>26</td><td>長期運用でのドリフト耐性と再現性評価が不足。</td></tr>
<tr><td>U10</td><td>熱力学的一貫性</td><td>探索段階</td><td>26</td><td>神経回路実装における実効下限の実測研究が限定的。</td></tr>
<tr><td>U11</td><td>意識指標近似の妥当性</td><td>部分解決</td><td>26</td><td>理論間を同条件で比較する公開ベンチが不足。</td></tr>
<tr><td>U12</td><td>分岐本人性</td><td>探索段階</td><td>19</td><td>技術システムに直結する運用規約（監査・責任追跡）が未整備。</td></tr>
<tr><td>U13</td><td>模倣分離</td><td>部分解決</td><td>26</td><td>模倣と因果保存を同時評価する統一ベンチが不足。</td></tr>
<tr><td>U14</td><td>追試可能性</td><td>部分解決</td><td>26</td><td>神経科学×機械学習を跨ぐ共通監査規約が不十分。</td></tr>
<tr><td>U15</td><td>制度統合</td><td>探索段階</td><td>26</td><td>技術指標と法的停止基準を結びつけた実装規格が不足。</td></tr>
</tbody></table>
<div class="note-box">
<strong>番号で身構えなくてよい理由</strong>
<p>
U番号は内部管理用のコードであり、暗記するためのものではありません。まずは上の「大きな問題群」で自分に近い塊を見つけ、その後に個別の U へ降りていけば十分です。
</p>
</div>
<div class="note-box">
<strong>現状ラベルを強弱ランキングとして読まないために</strong>
<p>
<strong>部分解決</strong> は一部の土台があること、<strong>探索段階</strong> は比較基盤がまだ弱いことを示します。<strong>未標準化</strong>、<strong>不足</strong>、<strong>未整備</strong> は、何が欠けているかの種類が違います。違いを 1 枚で見たい場合は <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: 部分解決・探索段階・未整備の読み方</a> を参照してください。
</p>
</div>
</section>

<section class="section" id="definitions">
<h2 class="section-title">未解決問題の厳密定義（U0-U15）</h2>
<table class="data-table">
<thead><tr><th>ID</th><th>厳密定義</th></tr></thead><tbody>
<tr><td>U0</td><td>介入集合 I と時間窓 T を固定したとき、生体系とモデル系の条件付き分布差 D(P_bio, P_model | I, T) をしきい値以下で規定できるか。</td></tr>
<tr><td>U1</td><td>観測 y から潜在源 x を推定する際、事後分布 p(x|y) の集中度・同定誤差境界・条件数を同時に報告できるか。</td></tr>
<tr><td>U3</td><td>主体モデルに含める最小構成要素を、connectome / cell type に加えて sleep-homeostasis、axon-myelin metabolic support、glial ensemble、clearance / immune support の omission / augmentation で境界決定できるか。</td></tr>
<tr><td>U4</td><td>観測一致ではなく介入分岐（counterfactual / do-intervention）で、生体系とモデル系の因果機構一致を判定できるか。</td></tr>
<tr><td>U7</td><td>EEG/fMRI/行動/生理の時刻系・空間系・前処理ログを監査可能に固定し、再解析で同一結論へ到達できるか。</td></tr>
<tr><td>U8</td><td>遅延・ジッタ・ノイズ・ドリフト下で、閉ループ神経制御が安全制約を破らず安定に動作するか。</td></tr>
<tr><td>U10</td><td>情報処理の不可逆性・散逸・エネルギー下限を神経計算モデルへ写像し、測定可能な反証条件を置けるか。</td></tr>
<tr><td>U11</td><td>IIT/PCI/GWT等の指標が、どの条件で一致し、どの条件で乖離するかをデータ駆動で比較可能にする。</td></tr>
<tr><td>U12</td><td>複製・分岐後に発生する複数主体の同一性・責任・権利帰属を、技術評価と整合する形式で規定できるか。</td></tr>
<tr><td>U13</td><td>高性能模倣（言語/行動出力）と、内部因果構造保存を識別する評価軸を実験的に分離できるか。</td></tr>
<tr><td>U14</td><td>第三者が同一データ・同一手順・同一評価契約で同等結論に到達できる公開運用を常時維持できるか。</td></tr>
<tr><td>U15</td><td>技術評価KPIと法/倫理KPIを連動させ、停止基準と公開基準を運用レベルで定義できるか。</td></tr>
</tbody></table>
</section>

<section class="section" id="issue-rq-audit-20260224">
<h2 class="section-title">Issue反映とRQ監査（2026-02-24）</h2>
<p>GitHub Issue #264/#265 を取り込み、各Uセクションのリサーチクエスチョン件数と多様性を点検しました。重複が出やすい領域（U3/U7/U8/U12/U13/U14）は、評価軸を分離してクエスチョンを増補しています。</p>

<h3>Issue取り込み（完了）</h3>
<table class="data-table">
<thead><tr><th>Issue</th><th>入力ソース</th><th>反映先</th><th>状態</th></tr></thead><tbody>
<tr><td>#264</td><td>Neuron URL (PII: S0896-6273(25)00843-8)</td><td>U3 主要先行研究（DOI: 10.1016/j.neuron.2025.10.036）</td><td>反映済み</td></tr>
<tr><td>#265</td><td>Neuroscience News URL</td><td>U13 主要先行研究（一次研究 DOI: 10.1126/sciadv.adw1464 を併記）</td><td>反映済み</td></tr>
</tbody></table>

<h3>RQ件数と多様性評価</h3>
<table class="data-table">
<thead><tr><th>U</th><th>更新前RQ数</th><th>更新後RQ数</th><th>多様性評価</th></tr></thead><tbody>
<tr><td>U0</td><td>4</td><td>4</td><td>高（定義・閾値・分岐を分離）</td></tr>
<tr><td>U1</td><td>4</td><td>4</td><td>中（推定不確実性中心）</td></tr>
<tr><td>U3</td><td>4</td><td>6</td><td>中（構造/体液/免疫へ軸拡張）</td></tr>
<tr><td>U4</td><td>4</td><td>4</td><td>高（識別・介入・反証を分離）</td></tr>
<tr><td>U7</td><td>4</td><td>6</td><td>中（同期・QC・欠損耐性へ拡張）</td></tr>
<tr><td>U8</td><td>4</td><td>6</td><td>高（安定性・安全性・運用回復を分離）</td></tr>
<tr><td>U10</td><td>4</td><td>4</td><td>高（理論・観測・コストを分離）</td></tr>
<tr><td>U11</td><td>4</td><td>4</td><td>高（理論比較・計算量・失敗条件を分離）</td></tr>
<tr><td>U12</td><td>4</td><td>6</td><td>高（法的帰属・同意運用を追加）</td></tr>
<tr><td>U13</td><td>4</td><td>6</td><td>中（復元精度・リーク検出軸を追加）</td></tr>
<tr><td>U14</td><td>4</td><td>6</td><td>中（否定例公開・再現コスト軸を追加）</td></tr>
<tr><td>U15</td><td>4</td><td>4</td><td>高（法概念・監査・停止基準を分離）</td></tr>
<tr><td><strong>合計</strong></td><td><strong>48</strong></td><td><strong>60</strong></td><td>重複クラスタを分散済み</td></tr>
</tbody></table>

<div class="note-box">
<strong>重複処理ルール（今回適用）</strong>
<ul>
<li>同一テーマでも「測定」「因果」「運用」の評価軸を分離して別クエスチョン化。</li>
<li>文献は一次研究を優先し、ニュース記事は一次研究リンク付きの補助参照として保持。</li>
<li>低関連・重複傾向の文献を差し替え、各Uの文献件数は維持。</li>
</ul>
</div>
</section>

<section class="section" id="literature-refresh-20260224b">
<h2 class="section-title">追加文献探索（2026-02-24 第2便）</h2>
<p>2024-2026の一次文献を再探索し、関連性が高い DOI を各Uの根拠例へ追補しました。今回の追補は「理論更新」「実装更新」「監査規約更新」の3軸で選定しています。</p>
<table class="data-table">
<thead><tr><th>U</th><th>追補DOI</th><th>要点</th></tr></thead><tbody>
<tr><td>U1</td><td><a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">10.1109/JSEN.2024.3502917</a></td><td>M/EEG逆問題の2025レビュー</td></tr>
<tr><td>U4</td><td><a href="https://doi.org/10.1109/TBME.2024.3423803" target="_blank">10.1109/TBME.2024.3423803</a></td><td>発達過程の動的有効結合を因果モデル化</td></tr>
<tr><td>U7</td><td><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">10.1038/s41597-024-03559-8</a></td><td>Motion-BIDSによる再現可能な運動データ整理</td></tr>
<tr><td>U8</td><td><a href="https://doi.org/10.1088/1741-2552/adbb20" target="_blank">10.1088/1741-2552/adbb20</a></td><td>閉ループBCI実験基盤のモジュール化</td></tr>
<tr><td>U10</td><td><a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">10.1016/j.tics.2024.03.009</a></td><td>心的過程と熱力学の接続レビュー</td></tr>
<tr><td>U11</td><td><a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">10.1038/s41586-025-08888-1</a></td><td>GNWとIITの敵対的検証</td></tr>
<tr><td>U12</td><td><a href="https://doi.org/10.20318/universitas.2025.9574" target="_blank">10.20318/universitas.2025.9574</a></td><td>神経権利の欧州・中南米比較規制</td></tr>
<tr><td>U13</td><td><a href="https://doi.org/10.1088/1741-2552/adfab1" target="_blank">10.1088/1741-2552/adfab1</a></td><td>LLM併用のbrain-to-text最新報告</td></tr>
<tr><td>U14</td><td><a href="https://doi.org/10.1098/rsos.242057" target="_blank">10.1098/rsos.242057</a></td><td>再現性向上介入のスコーピングレビュー</td></tr>
<tr><td>U15</td><td><a href="https://doi.org/10.1007/s11673-025-10440-9" target="_blank">10.1007/s11673-025-10440-9</a></td><td>神経技術の責任ある倫理ガバナンス戦略</td></tr>
</tbody></table>
</section>

<section class="section" id="deepening-integration-20260301">
<h2 class="section-title">深掘り統合反映（2026-03-01）</h2>
<p>
旧 <code>research_deepening_*.md</code> 群は、この節へ統合しました。公開ページとしては分割せず、<strong>本文に何を吸収したか</strong>と<strong>raw artifact がどこに残っているか</strong>をここでまとめて追えるようにしております。
</p>
<div class="note-box">
<strong>今回の整理方針</strong>
<p>
Round 1〜114 の情報は消しておらず、公開本文と <code>automation/</code> の役割を分け直しました。読む人には要約と判断材料を本文で示し、機械処理結果や運用ログは CSV / audit memo 側へ残します。
</p>
</div>
<table class="data-table">
<thead><tr><th>U</th><th>RQ総数</th><th>深掘り完了</th><th>今回本文に残した要点</th></tr></thead><tbody>
<tr><td>U0</td><td>4</td><td>4</td><td>操作的同一性は理論整理が進む一方、介入応答を含むベンチ仕様が未整備であることを固定しました。</td></tr>
<tr><td>U1</td><td>4</td><td>4</td><td>逆問題では点推定だけでなく、不確実性伝播と区間公開を要件化すべき段階に来ています。</td></tr>
<tr><td>U3</td><td>6</td><td>6</td><td>構造 scaffold、sleep/homeostasis、髄鞘/代謝支持、glia/clearance support を別の evidence axis として分けて読む必要を固定しました。</td></tr>
<tr><td>U4 / U7 / U8</td><td>16</td><td>16</td><td>因果同値、BIDS/同期、閉ループ遅延の条件を、観測・再現・安全停止の観点で具体化しました。</td></tr>
<tr><td>U10 / U11</td><td>8</td><td>8</td><td>熱力学的一貫性と意識指標近似は、理論主張より先に KPI と失敗条件を固定する必要があると整理しました。</td></tr>
<tr><td>U12 / U15</td><td>10</td><td>10</td><td>規制トラックでは、本文更新前の証跡ゲート、再監視、再開台帳を標準化しました。</td></tr>
<tr><td>U13 / U14</td><td>12</td><td>12</td><td>模倣分離と追試可能性について、最小コア文献と補助文献の読み分けを強化しました。</td></tr>
<tr><td><strong>合計</strong></td><td><strong>60</strong></td><td><strong>60</strong></td><td><strong>旧 Round 1–114 の公開追補は本節へ集約済みです。</strong></td></tr>
</tbody></table>

<h3>今回本文へ吸収した内容</h3>
<table class="data-table">
<thead>
<tr>
<th>ラウンド群</th>
<th>本文へ残したこと</th>
<th>代表的な証跡</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Round 1–12</strong></td>
<td>U別の平易化追補、追加根拠、必須2本＋補助1本の最小コア文献セットを反映しました。</td>
<td><a href="automation/rq_core_reference_minset_round10_2026-03-01.csv" target="_blank">Round 10 core set</a></td>
</tr>
<tr>
<td><strong>Round 13–18</strong></td>
<td>補助文献の品質点検、タグ再分類、必須/補助の二層化、3ステップ読了順と時間目安を整えました。</td>
<td><a href="automation/rq_reference_layering_round17_2026-03-01.csv" target="_blank">Round 17 layering</a> / <a href="automation/rq_reading_path_timed_round18_2026-03-01.csv" target="_blank">Round 18 timed path</a></td>
</tr>
<tr>
<td><strong>Round 19–39</strong></td>
<td>U12/U15 の規制トラックを整合させ、法域ラベル、監査優先キュー、本文更新テンプレを固定しました。</td>
<td><a href="automation/rq_u12_regulation_alignment_round19_2026-03-01.csv" target="_blank">Round 19 alignment</a> / <a href="automation/rq_regulation_external_dependency_tasks_round28_2026-03-01.csv" target="_blank">Round 28 external dependency split</a></td>
</tr>
<tr>
<td><strong>Round 40–61</strong></td>
<td>公開反映前の証跡完全性、publish gate、未解消エスカレーション、クローズ条件を標準化しました。</td>
<td><a href="automation/rq_regulation_publish_gate_round57_2026-03-01.csv" target="_blank">Round 57 publish gate</a></td>
</tr>
<tr>
<td><strong>Round 62–114</strong></td>
<td>reopen / reentry / follow-up の再監視と安定化確認を、問い別台帳として運用できる形にしました。</td>
<td><a href="automation/rq_regulation_reentry_execution_packet_round70_2026-03-01.csv" target="_blank">Round 70 reentry packet</a> / <a href="automation/rq_regulation_reentry_followup_reconnect_followup_reevaluation_followup_stability_confirmation_ledger_round100_2026-03-01.csv" target="_blank">Round 100 stability ledger</a></td>
</tr>
</tbody>
</table>

<h3>深掘りから本文へ残した要点</h3>
<div class="key-points">
<h4>Representative Findings</h4>
<ul>
<li><strong>U0:</strong> 操作的同一性は理論蓄積がある一方で、介入応答を含むベンチ仕様が依然不足しております。</li>
<li><strong>U1:</strong> 逆問題では、点推定だけでなく不確実性伝播と信頼区間公開を最低要件として扱うべきです。</li>
<li><strong>U3:</strong> connectome 外の境界は、sleep/homeostasis、髄鞘/代謝支持、astrocyte ensemble、clearance/immune support を時定数別に分けて読まないと誤読します。</li>
<li><strong>U7 / U8:</strong> BIDS、同期誤差、閉ループ遅延の許容域は、再現可能性と安全停止の双方に直結します。</li>
<li><strong>U10 / U11:</strong> 熱力学的一貫性と意識指標近似は、理論対立より先に KPI と失敗条件を固定すべき論点です。</li>
<li><strong>U12 / U15:</strong> 制度・規制系は外部依存が大きいため、本文更新前の証跡ゲートと再監視運用が不可欠です。</li>
</ul>
</div>

<h3>raw artifact と監査の置き場</h3>
<p class="small">
全60問いのカバレッジ監査は <a href="automation/rq_deepening_consistency_audit_2026-03-01.md" target="_blank">rq_deepening_consistency_audit_2026-03-01.md</a>、U別集計は <a href="automation/rq_deepening_coverage_summary_2026-03-01.csv" target="_blank">rq_deepening_coverage_summary_2026-03-01.csv</a>、引用関連性の点検は <a href="automation/rq_reference_relevance_audit_2026-03-01.md" target="_blank">rq_reference_relevance_audit_2026-03-01.md</a> に残しています。
</p>
<p class="small">
運用ガイドとしての役割が強かった旧 <code>research_deepening_continue_guide_2026-03-01.md</code> は公開ページから外し、公開導線では本節の要約と <code>automation/</code> の raw artifact を対応付ける方針へ変更しました。
</p>
</section>


<section class="section" id="u0">
<h2 class="section-title">U0: 操作的同一性</h2>
<p><strong>厳密定義:</strong> 介入集合 I と時間窓 T を固定したとき、生体系とモデル系の条件付き分布差 D(P_bio, P_model | I, T) をしきい値以下で規定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>同一性判定を『観測一致』と『介入応答一致』に分離したとき、どちらを必要条件・十分条件に置くか。</li>
<li>時間同期（ms単位）と状態表現（行動・神経活動・生理）の対応をどう固定するか。</li>
<li>同一性判定の閾値をタスク別にどう設定し、過学習モデルをどう除外するか。</li>
<li>分岐/複製ケースでの『同一個体』定義をどの評価軸に帰着させるか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>心理的連続性・情報的連続性・機能的同値を区別する議論枠組みは文献上で整理済み。</li>
<li>段階置換とscan-and-copyの比較で、手続き差が同一性の十分条件にならないという反論は蓄積済み。</li>
<li>同一性を単一の形而上学命題でなく、操作的判定問題に変換する方向性は共有されている。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.7551/mitpress/10366.003.0009" target="_blank">Continuity: Kinks Not Breaks</a>、<a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a>、<a href="https://doi.org/10.31219/osf.io/zw3v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>介入実験を含む同一性評価ベンチは未標準化。</li>
<li>長期ドリフトを含む同一性維持（週〜月スケール）の定量指標が未確立。</li>
<li>分岐後主体の責任帰属と評価帰属を技術評価へ接続する規約が不足。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.7551/mitpress/10058.003.0005" target="_blank">Whole Brain Emulation</a>、<a href="https://arxiv.org/abs/2510.15745v3" target="_blank">State of Brain Emulation Report 2025</a>、<a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a>。</p>
<h3>主要先行研究（再精査 12 件）</h3>
<ol>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a> (2026)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31219/osf.io/sr7cf" target="_blank">Nondestructive Mind Uploading and the Stream of Consciousness</a> (2023)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2510.15745" target="_blank">State of Brain Emulation Report 2025</a> (2025)</li>
<li><strong>[Oxford]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a> (2016)</li>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781009367059.009" target="_blank">Personal Ontology and Life after Death, Part 2: Mind Uploading</a> (2024)</li>
<li><strong>[Synthese]</strong> <a href="https://doi.org/10.1007/s11229-024-04744-3" target="_blank">I am no abstract object</a> (2024)</li>
<li><strong>[SSRN]</strong> <a href="https://doi.org/10.2139/ssrn.2596460" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2015)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31219/osf.io/zw3v4" target="_blank">The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy</a> (2023)</li>
<li><strong>[MIT Press]</strong> <a href="https://doi.org/10.7551/mitpress/10366.003.0009" target="_blank">Continuity: Kinks Not Breaks</a> (2017)</li>
<li><strong>[MIT Press]</strong> <a href="https://doi.org/10.7551/mitpress/10058.003.0005" target="_blank">Whole Brain Emulation</a> (2015)</li>
<li><strong>[Patterns]</strong> <a href="https://doi.org/10.1016/j.patter.2023.100861" target="_blank">No legal personhood for AI</a> (2023)</li>
<li><strong>[Minds and Machines]</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a> (2014)</li>
</ol>
</section>

<section class="section" id="u1">
<h2 class="section-title">U1: 逆問題同定可能性</h2>
<p><strong>厳密定義:</strong> 観測 y から潜在源 x を推定する際、事後分布 p(x|y) の集中度・同定誤差境界・条件数を同時に報告できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>EEG/MEG逆問題での不良設定性を、どの事前分布で制御するか。</li>
<li>頭蓋導電率・電極配置・ノイズ構造の不確実性を、推定不確実性へどう伝播させるか。</li>
<li>同じデータで異なる逆解法（MNE, beamformer, Champagne 等）が乖離した場合の判定規則をどう置くか。</li>
<li>推定値だけでなく、信頼区間/後方分布を公開基準に含めるか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>Bayesian EEG/MEG source imaging と sparse prior による逆問題安定化は方法論として確立。</li>
<li>頭部導電率不確実性が逆解精度を大きく左右する点は多数研究で再現。</li>
<li>Champagne系のspatio-temporal SBLは実データ評価を含む報告が蓄積。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-3-319-14947-9_4" target="_blank">Sparse Bayesian (Champagne) Algorithm</a>、<a href="https://doi.org/10.1109/sampta64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE</a>、<a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">Inverse Problem for M/EEG Source Localization: A Review</a>、<a href="https://arxiv.org/abs/1810.04410v2" target="_blank">Fast Approximation of EEG Forward Problem and Application to Tissue Conductivity Estimation</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>被験者間・装置間の不確実性を横断した一般化誤差境界が不足。</li>
<li>逆問題の識別可能性をタスク依存で比較する統一ベンチが不足。</li>
<li>因果介入評価に接続できる逆問題の品質指標が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1137/1.9781611977844.ch7" target="_blank">Parameter Identifiability and Influence</a>、<a href="https://doi.org/10.1007/978-3-030-74918-7" target="_blank">EEG/MEG Source Reconstruction</a>、<a href="https://arxiv.org/abs/2209.11233v2" target="_blank">Evaluating Latent Space Robustness and Uncertainty of EEG-ML Models</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[IEEE Sensors Journal]</strong> <a href="https://doi.org/10.1109/JSEN.2024.3502917" target="_blank">Inverse Problem for M/EEG Source Localization: A Review</a> (2025)</li>
<li><strong>[SampTA]</strong> <a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">Revisiting CHAMPAGNE: Sparse Bayesian Learning as Reweighted Sparse Coding</a> (2025)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-319-14947-9_4" target="_blank">Sparse Bayesian (Champagne) Algorithm</a> (2015)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38545514/" target="_blank">SESAMEEG: probabilistic source localization</a> (PMID:38545514, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38532791/" target="_blank">Global sensitivity of EEG source analysis to tissue conductivity uncertainties</a> (PMID:38532791, 2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/41308490/" target="_blank">Global sensitivity of MEG source analysis to tissue conductivity uncertainties</a> (PMID:41308490, 2025)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/39423516/" target="_blank">Standardized Kalman filtering for dynamical source localization</a> (PMID:39423516, 2024)</li>
<li><strong>[Physiological Measurement]</strong> <a href="https://doi.org/10.1088/2057-1976/aca20b" target="_blank">Neural SDE as uncertainty quantification for EEG source localization</a> (2023)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/41411682/" target="_blank">Potential of EEG and EEG/MEG skull conductivity estimation</a> (PMID:41411682, 2026)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-030-74918-7_4" target="_blank">Source Models</a> (2022)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-030-74918-7" target="_blank">EEG/MEG Source Reconstruction</a> (2022)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/1810.04410v2" target="_blank">Fast Approximation of EEG Forward Problem and Application to Tissue Conductivity Estimation</a> (2018)</li>
<li><strong>[SIAM]</strong> <a href="https://doi.org/10.1137/1.9781611977844.ch7" target="_blank">Parameter Identifiability and Influence</a> (2024)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W2903531101" target="_blank">Improving EEG Source Localization Through Spatio-Temporal Sparse Bayesian Learning</a> (2018)</li>
</ol>
</section>

<section class="section" id="u3">
<h2 class="section-title">U3: 生物学的境界</h2>
<p><strong>厳密定義:</strong> 主体モデルに含める最小構成要素を、connectome / cell type に加えて <strong>sleep-homeostasis</strong>、<strong>axon-myelin metabolic support</strong>、<strong>glial ensemble state</strong>、<strong>clearance / immune support</strong> の omission / augmentation で境界決定できるか。</p>
<h3>2026-03 U3 再監査：生物学的境界を 4 つの evidence axis に分けます</h3>
<p>
今回もっとも改善すべきだった弱点は、旧 U3 が <strong>connectome の前進</strong>、<strong>sleep / homeostasis</strong>、<strong>髄鞘 / 代謝支持</strong>、<strong>astrocyte / clearance / immune support</strong>、<strong>身体・環境ループ</strong> を近い強さで並べ、しかも一部で <strong>直接性の弱い章論文や一般論</strong> を根拠例に混ぜていた点でございます。これでは読者が「ニューロン外のものは全部同じくらい必要」あるいは「全部まだ speculative」と両方向に誤読しやすくなります。一次文献を見直すと、現在の front はむしろ <strong>何が structural scaffold で、何が same-day から cross-day を左右する maintenance-state で、何がさらに遅い support-state か</strong> の分離にあります。したがって U3 では、以下の 4 軸に分けて evidence を読みます。
</p>
<table class="data-table">
<thead>
<tr>
<th>evidence axis</th>
<th>今の一次文献が直接押し上げること</th>
<th>まだそのままは言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>構造 scaffold / cell-type bridge</strong></td>
<td>whole-brain connectome、same-brain functional connectomics、Patch-seq-to-EM bridge により、どの配線と cell-type variation が構造側の床かをかなり強く固定できます。</td>
<td>current synaptic efficacy、intrinsic excitability、sleep-history、glial / metabolic state までは直接入りません。</td>
</tr>
<tr>
<td><strong>sleep / homeostatic regime</strong></td>
<td>sleep / wake に依存した firing-rate homeostasis と cortical regime recovery により、静的 wiring だけでは cross-day の戻り先が決まらないことを直接示せます。</td>
<td>human whole-brain でどの sleep / state 変数まで測れば十分かの閾値は未確定です。</td>
</tr>
<tr>
<td><strong>axon-myelin / glial support</strong></td>
<td>oligodendrocyte-axon metabolic coupling、astrocyte transmitter encoding、learning-associated astrocyte ensembles は、非神経細胞支持系が背景条件ではなく performance variable であることを示します。</td>
<td>whole-brain direct route や universal omission threshold はまだありません。</td>
</tr>
<tr>
<td><strong>clearance / immune support</strong></td>
<td>meningeal lymphatic dysfunction が synaptic physiology と memory を動かし、human CSF / glymphatic measurement も support-state として測定可能になりつつあります。</td>
<td>moment-to-moment neural truth や universal minimal core をそのまま与えるわけではありません。</td>
</tr>
</tbody>
</table>
<p class="small"><strong>site rule:</strong> 身体・環境ループは重要候補でございますが、現時点では task-specific omission study が中心であり、上の 4 軸と同じ強さの primary evidence class にはまだ置きません。U3 ではまず <strong>brain-internal support-state</strong> を時定数別に監査し、その後に body / environment coupling を追加軸として扱います。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>connectome / cell-type bridge 単独モデルと maintenance-state augmentation model の held-out prediction gap を、同じ split でどう測るか。</li>
<li>sleep-history / homeostatic set point の omission が、cross-day predictability と recovery route をいつ壊すか。</li>
<li>delay / myelin / axonal metabolic support の omission が、timing-sensitive task と long-horizon recovery をどれだけ落とすか。</li>
<li>astrocyte / glial 変数を causal contributor と slow proxy にどう分けて評価するか。</li>
<li>clearance / immune support を momentary neural truth と混同せず、人でどこまで measurable support-state として扱えるか。</li>
<li>身体・環境ループを universal core と読む前に、どの same-task ablation / transfer test を要求するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>whole-brain connectome、same-brain functional connectomics、Patch-seq-to-EM bridge により、<strong>構造 scaffold</strong> と <strong>cell-type bridge</strong> の前進は明確です。ただし connectome-constrained recurrent network でも dynamics の縮退は残ります。</li>
<li>sleep / wake 依存の firing-rate homeostasis と、sleep による cortical regime recovery は、<strong>静的 wiring だけでは cross-day の戻り先が決まらない</strong>ことを直接示しています。</li>
<li>oligodendrocyte-axon metabolic coupling、astrocyte network encoding、learning-associated astrocyte ensembles は、<strong>非神経細胞支持系が背景条件ではなく performance variable</strong> であることを強く示します。</li>
<li>meningeal lymphatics-microglia axis と human CSF / glymphatic 測定は、clearance / immune support が観測可能な support-state 軸になりつつあることを示しますが、moment-to-moment neural completeness までは与えません。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1038/s41586-024-07686-5" target="_blank">Whole-brain annotation and multi-connectome cell typing of Drosophila</a>、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">Functional connectomics spanning multiple areas of mouse visual cortex</a>、<a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Prediction of neural activity in connectome-constrained recurrent networks</a>、<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Neuronal Firing Rate Homeostasis Is Inhibited by Sleep and Promoted by Wake</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Sleep restores an optimal computational regime in cortical networks</a>、<a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health</a>、<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Network-level encoding of local neurotransmitters in cortical astrocytes</a>、<a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Meningeal lymphatics-microglia axis regulates synaptic physiology</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>どの omission / augmentation test を通れば、sleep/homeostasis、myelin/metabolic support、glial ensemble、clearance support を「必要最小構成」と呼べるかの共通ベンチが未標準化です。</li>
<li>human で直接取れる support-state は依然として coarse proxy が中心で、glial / metabolic / clearance から momentary neural state への bridge は弱いままです。</li>
<li>身体・環境ループは重要候補ですが、現時点の一次証拠は task-specific であり、U3 の既定 core を決める direct omission study はまだ薄いです。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans</a>、<a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">The glymphatic system clears amyloid-beta and tau from brain to plasma in humans</a>、<a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Synaptic memory survives molecular turnover</a>。</p>
<h3>主要先行研究（再精査 15 件）</h3>
<ol>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-024-07686-5" target="_blank">Whole-brain annotation and multi-connectome cell typing of Drosophila</a> (2024)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">Functional connectomics spanning multiple areas of mouse visual cortex</a> (2025)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Prediction of neural activity in connectome-constrained recurrent networks</a> (2025)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">Connectomics of predicted Sst transcriptomic types in mouse visual cortex</a> (2025)</li>
<li><strong>[Cell]</strong> <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Neuronal Firing Rate Homeostasis Is Inhibited by Sleep and Promoted by Wake</a> (2016)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Sleep restores an optimal computational regime in cortical networks</a> (2024)</li>
<li><strong>[Science]</strong> <a href="https://doi.org/10.1126/science.1252304" target="_blank">Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain</a> (2014)</li>
<li><strong>[Science]</strong> <a href="https://doi.org/10.1126/science.1254960" target="_blank">Motor skill learning requires active central myelination</a> (2014)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Oligodendrocyte-axon metabolic coupling is mediated by extracellular K+ and maintains axonal health</a> (2024)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Network-level encoding of local neurotransmitters in cortical astrocytes</a> (2024)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Learning-associated astrocyte ensembles regulate memory recall</a> (2025)</li>
<li><strong>[PNAS]</strong> <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">Synaptic memory survives molecular turnover</a> (2022)</li>
<li><strong>[Cell]</strong> <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Meningeal lymphatics-microglia axis regulates synaptic physiology</a> (2025)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans</a> (2025)</li>
<li><strong>[Nature Communications]</strong> <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">The glymphatic system clears amyloid-beta and tau from brain to plasma in humans</a> (2026)</li>
</ol>
</section>

<section class="section" id="u4">
<h2 class="section-title">U4: 因果同値</h2>
<p><strong>厳密定義:</strong> 観測一致ではなく介入分岐（counterfactual / do-intervention）で、生体系とモデル系の因果機構一致を判定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>観測データ由来の相関を因果グラフへ持ち上げる識別条件は何か。</li>
<li>介入実験（刺激・抑制・入力撹乱）で検証可能な最小因果主張は何か。</li>
<li>active inferenceやDCMの理論予測を、反事実評価にどう接続するか。</li>
<li>同値判定の失敗条件（falsification）をどの水準で宣言するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>do-calculus/SCM に基づく因果識別理論は成熟。</li>
<li>神経科学でDCMや介入実験を使った因果方向推定の実践知は存在。</li>
<li>反事実推論を含む評価設計の必要性は理論的にほぼ合意。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-1-4614-7320-6_57-1" target="_blank">Dynamic Causal Modeling with Neural Population Models</a>、<a href="https://doi.org/10.1101/2021.06.01.446526" target="_blank">Test-retest reliability of regression dynamic causal modeling</a>、<a href="https://doi.org/10.1109/TBME.2024.3423803" target="_blank">A Deep Dynamic Causal Learning Model</a>、<a href="https://arxiv.org/abs/2010.09429v2" target="_blank">Neural Additive VAR for Causal Discovery in Time Series</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>高次元時系列での因果識別可能性がデータ条件に強く依存。</li>
<li>観測ノイズ・遅延・未観測交絡を含む現実設定での頑健評価が不足。</li>
<li>WBE水準の介入同値判定に使える公開ベンチが未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://arxiv.org/abs/2209.03427v1" target="_blank">Causal discovery for time series with latent confounders</a>、<a href="https://arxiv.org/abs/2306.08946v2" target="_blank">Bootstrap aggregation and confidence measures for time-series causal discovery</a>、<a href="https://doi.org/10.32614/cran.package.cfid" target="_blank">cfid: Identification of Counterfactual Queries in Causal Models</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Nature Reviews Neuroscience]</strong> <a href="https://doi.org/10.1038/s41583-024-00881-3" target="_blank">Structural constraints in effective connectivity analyses</a> (2025)</li>
<li><strong>[NeuroImage]</strong> <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Fast dynamic causal modeling regression for fMRI</a> (2024)</li>
<li><strong>[IEEE TMI]</strong> <a href="https://doi.org/10.1109/TMI.2024.3381670" target="_blank">MCAN: Causal adversarial networks for dynamic effective connectivity</a> (2024)</li>
<li><strong>[JAMA Network Open]</strong> <a href="https://doi.org/10.1001/jamanetworkopen.2024.9220" target="_blank">Personalized hippocampal network-targeted stimulation trial</a> (2024)</li>
<li><strong>[PubMed]</strong> <a href="https://pubmed.ncbi.nlm.nih.gov/38826672/" target="_blank">Dynamic causal modeling in multisensory speech perception</a> (PMID:38826672, 2024)</li>
<li><strong>[IEEE TNSRE]</strong> <a href="https://doi.org/10.1109/TNSRE.2021.3123964" target="_blank">Systematic review of DCM in psychiatric disorders</a> (2021)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-1-4614-7320-6_57-1" target="_blank">Dynamic Causal Modeling with Neural Population Models</a> (2013)</li>
<li><strong>[bioRxiv]</strong> <a href="https://doi.org/10.1101/2021.06.01.446526" target="_blank">Test-retest reliability of regression dynamic causal modeling</a> (2021)</li>
<li><strong>[IEEE TBME]</strong> <a href="https://doi.org/10.1109/TBME.2024.3423803" target="_blank">A Deep Dynamic Causal Learning Model</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2010.09429v2" target="_blank">Neural Additive VAR for Causal Discovery in Time Series</a> (2020)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2209.03427v1" target="_blank">Causal discovery for time series with latent confounders</a> (2022)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2306.08946v2" target="_blank">Bootstrap aggregation and confidence measures for time-series causal discovery</a> (2023)</li>
<li><strong>[CRAN]</strong> <a href="https://doi.org/10.32614/cran.package.cfid" target="_blank">cfid: Identification of Counterfactual Queries in Causal Models</a> (2021)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2308.08307v1" target="_blank">Integrating cognitive map learning and active inference for planning in ambiguous environments</a> (2023)</li>
</ol>
</section>

<section class="section" id="u7">
<h2 class="section-title">U7: マルチモーダル整合</h2>
<p><strong>厳密定義:</strong> EEG/fMRI/行動/生理の時刻系・空間系・前処理ログを監査可能に固定し、再解析で同一結論へ到達できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>BIDS拡張で同期・QC・刺激ログをどこまで必須化するか。</li>
<li>同時計測、同一個体の非同時計測、coverage-limited な侵襲校正、atlas prior を、取得関係としてどう区別して残すか。</li>
<li>LSL 等の時刻同期誤差を、device-side delay と分けて検証可能な指標へ落とせるか。</li>
<li>EEG-fMRI で HRF、task-related haemodynamics、venous bias を別監査し、BOLD proxy ceiling を提出物にできるか。</li>
<li>モダリティ間アライメント失敗時の再計測 / 除外基準と missing-modality baseline をどう固定するか。</li>
<li>前処理差分や融合モデル差分を CI で自動比較する場合、どの再現率低下をリリースブロック閾値にするか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>EEG-BIDS、Motion-BIDS、LSL により、multimodal の metadata、座標系、共有時計、再解析ログを比較可能な形で残せるようになりました。</li>
<li>simultaneous EEG-fMRI では、setup と cleaning を厳しく固定すれば cross-modal connectome 関係の再現可能性を示せます。</li>
<li>intracerebral stimulation や simultaneous HD-EEG / SEEG により、coverage-limited ですが direct validation route が成立しました。</li>
<li>BOLD 側では、LFP 寄り coupling、task-related haemodynamics、HRF 変動、venous / non-neural bias が比較的一貫して再確認されており、proxy ceiling 自体はかなり明確です。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">EEG-BIDS</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS</a>、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">The lab streaming layer for synchronized multimodal recording</a>、<a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">simultaneous EEG-fMRI connectome reproducibility</a>、<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Localize-MI</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">direct validation by intracranial stimulation</a>、<a href="https://doi.org/10.1038/35084005" target="_blank">basis of the fMRI signal</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>取得関係のラベル付け、hardware delay 監査、missing-modality baseline を 1 枚で出す site-wide 規約がまだ不足しています。</li>
<li>同時計測の concordance、侵襲校正、hemodynamic proxy audit を同一提出物で束ねた benchmark が不足しています。</li>
<li>異なる前処理 / 融合モデル間での出力差分監査と、失敗例まで含めた公開 QC 運用がまだ限定的です。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1162/imag.a.136" target="_blank">LSL</a>、<a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">simultaneous EEG-fMRI at ultra-high field</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">simultaneous HD-EEG / SEEG</a>、<a href="https://doi.org/10.1038/nature07664" target="_blank">anticipatory haemodynamic signals</a>、<a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">non-neural BOLD factors</a>。</p>
<h3>主要先行研究（再精査 16 件）</h3>
<ol>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">EEG-BIDS, an extension to the brain imaging data structure for electroencephalography</a> (2019)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS: extending BIDS to support standardized storage of motion data</a> (2024)</li>
<li><strong>[Imaging Neuroscience]</strong> <a href="https://doi.org/10.1162/imag.a.136" target="_blank">The lab streaming layer for synchronized multimodal recording</a> (2025)</li>
<li><strong>[NeuroImage]</strong> <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment</a> (2015)</li>
<li><strong>[NeuroImage]</strong> <a href="https://doi.org/10.1016/j.neuroimage.2021.117864" target="_blank">The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T</a> (2021)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods</a> (2020)</li>
<li><strong>[Brain Communications]</strong> <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Direct validation of EEG source imaging by intracranial electric stimulation in human patients</a> (2023)</li>
<li><strong>[Epilepsia]</strong> <a href="https://doi.org/10.1111/epi.18552" target="_blank">HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy</a> (2025)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/35084005" target="_blank">Neurophysiological investigation of the basis of the fMRI signal</a> (2001)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/nature09108" target="_blank">Global and local fMRI signals driven by neurons defined optogenetically by type and wiring</a> (2010)</li>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/nature07664" target="_blank">Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity</a> (2009)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/nn.3170" target="_blank">The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components</a> (2012)</li>
<li><strong>[NeuroImage]</strong> <a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses</a> (2004)</li>
<li><strong>[NeuroImage]</strong> <a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">A critical assessment of data quality and venous effects in sub-millimeter fMRI</a> (2019)</li>
<li><strong>[Journal of Neuroscience]</strong> <a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects</a> (2022)</li>
<li><strong>[Computer Methods and Programs in Biomedicine]</strong> <a href="https://doi.org/10.1016/j.cmpb.2024.108298" target="_blank">Haemosync: synchronisation algorithm for multimodal hemodynamic signals</a> (2024)</li>
</ol>
</section>

<section class="section" id="u8">
<h2 class="section-title">U8: 閉ループ安定性</h2>
<p><strong>厳密定義:</strong> 遅延・ジッタ・ノイズ・ドリフト下で、閉ループ神経制御が安全制約を破らず安定に動作するか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>閉ループBCIの遅延許容域を制御理論的にどう同定するか。</li>
<li>オンライン較正と概念ドリフト対策をどう組み込むか。</li>
<li>個体差と日内変動をまたぐ安定性をどの指標で評価するか。</li>
<li>異常検知とフェイルセーフを評価契約へどう組み込むか。</li>
<li>ヒューマンオーバーライドを導入したとき、誤作動率と回復時間をどうKPI化するか。</li>
<li>週〜月スケール運用での再学習頻度を、性能劣化と安全余裕のトレードオフでどう最適化するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>閉ループBCIにおける遅延・適応制御の重要性は多数報告で一貫。</li>
<li>オンライン再学習や適応フィルタにより短期安定性を改善できることは確認済み。</li>
<li>リアルタイム神経フィードバック系の基本アーキテクチャは確立。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.31224/4555" target="_blank">Closed-Loop Mu-Rhythm BCI for Neuroadaptive Control</a>、<a href="https://doi.org/10.1088/1741-2552/adbb20" target="_blank">Dareplane: a modular open-source software platform for BCI research</a>、<a href="https://doi.org/10.1016/j.bspc.2022.104183" target="_blank">Self-adaptive multiple-kernel ELM for MI-BCI</a>、<a href="https://arxiv.org/abs/2508.10474v1" target="_blank">EDAPT: Calibration-Free BCIs with Continual Online Adaptation</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>長期運用でのドリフト耐性と再現性評価が不足。</li>
<li>安全制約違反を事前検出する統一検証手順が不足。</li>
<li>閉ループ破綻時の責任境界と運用基準が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://arxiv.org/abs/2011.12362v1" target="_blank">Fixed-Time Stable Adaptation Law for Safety-Critical Control</a>、<a href="https://arxiv.org/abs/2508.08153v2" target="_blank">Robust Adaptive Discrete-Time Control Barrier Certificate</a>、<a href="https://doi.org/10.1109/bci60775.2024.10480468" target="_blank">Calibration-free online test-time adaptation for EEG MI decoding</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Nature Medicine]</strong> <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Chronic adaptive DBS versus conventional DBS in Parkinson's disease</a> (2024)</li>
<li><strong>[Brain]</strong> <a href="https://doi.org/10.1093/brain/awad429" target="_blank">At-home adaptive dual-target DBS with proportional control</a> (2024)</li>
<li><strong>[npj Parkinson's Disease]</strong> <a href="https://doi.org/10.1038/s41531-025-01124-7" target="_blank">Clinical outcomes and programming strategies in chronic adaptive DBS</a> (2025)</li>
<li><strong>[npj Parkinson's Disease]</strong> <a href="https://doi.org/10.1038/s41531-024-00772-5" target="_blank">ADAPT-PD sensing data and methodology</a> (2024)</li>
<li><strong>[JAMA Neurology]</strong> <a href="https://doi.org/10.1001/jamaneurol.2025.2781" target="_blank">Long-term personalized adaptive DBS</a> (2025)</li>
<li><strong>[Nature Reviews Neurology]</strong> <a href="https://doi.org/10.1038/s41582-025-01131-5" target="_blank">From adaptive DBS to adaptive circuit targeting</a> (2025)</li>
<li><strong>[Nature Biomedical Engineering]</strong> <a href="https://doi.org/10.1038/s41551-025-01438-0" target="_blank">Movement-responsive DBS with remotely optimized decoder</a> (2026 issue)</li>
<li><strong>[Expert Review of Medical Devices]</strong> <a href="https://doi.org/10.1080/17434440.2024.2438309" target="_blank">Closed-loop DBS systems for neuropsychiatric disorders</a> (2024)</li>
<li><strong>[medRxiv]</strong> <a href="https://doi.org/10.1101/2024.08.26.24312580" target="_blank">Adaptive DBS in Parkinson's disease: Delphi consensus</a> (2024 preprint)</li>
<li><strong>[IEEE BCI]</strong> <a href="https://doi.org/10.1109/bci60775.2024.10480468" target="_blank">Calibration-free online test-time adaptation for EEG motor imagery decoding</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2508.10474v1" target="_blank">EDAPT: Calibration-Free BCIs with Continual Online Adaptation</a> (2025)</li>
<li><strong>[Crossref]</strong> <a href="https://doi.org/10.31224/4555" target="_blank">Closed-Loop Mu-Rhythm BCI for Neuroadaptive Control</a> (2025)</li>
<li><strong>[Biomedical Signal Processing and Control]</strong> <a href="https://doi.org/10.1016/j.bspc.2022.104183" target="_blank">Self-adaptive multiple-kernel ELM for MI-BCI</a> (2023)</li>
<li><strong>[IEEE BCI Workshop]</strong> <a href="https://doi.org/10.1109/iww-bci.2016.7457451" target="_blank">Brain-controlled devices: the perception-action closed loop</a> (2016)</li>
</ol>
</section>

<section class="section" id="u10">
<h2 class="section-title">U10: 熱力学的一貫性</h2>
<p><strong>厳密定義:</strong> 情報処理の不可逆性・散逸・エネルギー下限を神経計算モデルへ写像し、測定可能な反証条件を置けるか。</p>
<div class="note-box">
<strong>U10 の入口で止まったとき</strong>
<p>
この節は文献地図なので、Landauer、NESS、EPR の説明は圧縮しています。まず意味の入口だけ整理したい場合は <a href="wiki/thermodynamic-grounding-basics.html">Wiki: 熱力学的接地の基本</a> を先に見ると追いやすくなります。
</p>
</div>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>Landauer下限を神経計算でどう適用/解釈するか。</li>
<li>非平衡熱力学指標と神経情報処理効率の対応をどう定義するか。</li>
<li>理論式を実データ（神経活動・代謝）へ落とし込む観測設計をどう作るか。</li>
<li>WBE計算コスト評価に熱力学制約をどう統合するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>Landauer原理・情報熱力学の理論枠組み自体は確立。</li>
<li>神経科学へ情報熱力学を接続するレビュー/視点論文が増加。</li>
<li>計算効率とエネルギー制約を同時評価する問題設定は明確化。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://arxiv.org/abs/2003.07436v1" target="_blank">Landauer Principle and General Relativity</a>、<a href="https://doi.org/10.3390/e26090779" target="_blank">Information Thermodynamics: From Physics to Neuroscience</a>、<a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">The Thermodynamics of Mind</a>、<a href="https://doi.org/10.1017/9781316650394.024" target="_blank">Information and Thermodynamics</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>神経回路実装における実効下限の実測研究が限定的。</li>
<li>熱散逸推定の標準化された計測パイプラインが不足。</li>
<li>WBEスケール推定で使える合意済みコストモデルが未成立。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-3-319-93458-7_2" target="_blank">Conditional Erasure and the Landauer Limit</a>、<a href="https://doi.org/10.3390/books978-3-7258-4142-4" target="_blank">The Landauer Principle and Its Implementations in Physics, Chemistry and Biology</a>、<a href="https://doi.org/10.1016/b978-0-444-59557-7.00011-4" target="_blank">Thermodynamics and Biological Systems</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Entropy]</strong> <a href="https://doi.org/10.3390/e26090779" target="_blank">Information Thermodynamics: From Physics to Neuroscience</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2502.03603" target="_blank">Dynamical Landauer principle and thermodynamic cost of entropy production</a> (2025)</li>
<li><strong>[Physical Review E]</strong> <a href="https://doi.org/10.1103/PhysRevE.107.024121" target="_blank">Entropy production correlates with consciousness levels</a> (2023)</li>
<li><strong>[Trends in Cognitive Sciences]</strong> <a href="https://doi.org/10.1016/j.tics.2024.03.009" target="_blank">The Thermodynamics of Mind</a> (2024)</li>
<li><strong>[Neuroscience and Biobehavioral Reviews]</strong> <a href="https://doi.org/10.1016/j.neubiorev.2023.105070" target="_blank">A primer on entropy in neuroscience</a> (2023)</li>
<li><strong>[Springer]</strong> <a href="https://doi.org/10.1007/978-3-319-93458-7_2" target="_blank">Conditional Erasure and the Landauer Limit</a> (2018)</li>
<li><strong>[MDPI Books]</strong> <a href="https://doi.org/10.3390/books978-3-7258-4142-4" target="_blank">The Landauer Principle and Its Implementations in Physics, Chemistry and Biology</a> (2025)</li>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781316650394.024" target="_blank">Information and Thermodynamics</a> (book chapter)</li>
<li><strong>[Elsevier]</strong> <a href="https://doi.org/10.1016/b978-0-444-59557-7.00011-4" target="_blank">Thermodynamics and Biological Systems</a> (2014)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2003.07436v1" target="_blank">Landauer Principle and General Relativity</a> (2020)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2409.17599v1" target="_blank">Information thermodynamics: from physics to neuroscience</a> (2024)</li>
<li><strong>[JPCL supporting information]</strong> <a href="https://doi.org/10.1021/acs.jpclett.4c03156.s001" target="_blank">Deriving the Landauer Principle from the Quantum Shannon Entropy</a> (supporting material)</li>
<li><strong>[CRC Press]</strong> <a href="https://doi.org/10.1201/b10962-10" target="_blank">Chemical Thermodynamics, Information, and Horizons</a> (2011)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3023669232" target="_blank">Nonequilibrium Thermodynamics in Cell Biology</a> (2020)</li>
</ol>
</section>

<section class="section" id="u11">
<h2 class="section-title">U11: 意識指標近似の妥当性</h2>
<p><strong>厳密定義:</strong> IIT/PCI/GWT等の指標が、どの条件で一致し、どの条件で乖離するかをデータ駆動で比較可能にする。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>理論間で比較可能な入出力仕様をどう定義するか。</li>
<li>PCIやIIT近似計算の計算量制約をどう扱うか。</li>
<li>理論予測の対立点を単一実験計画へどう落とすか。</li>
<li>意識指標を臨床/研究で運用する際の失敗条件をどう明示するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>IIT 4.0、GWT、PCI系の理論・実証双方で比較対象が明確化。</li>
<li>adversarial collaboration型の理論比較アプローチが提案され、対立点の明示が進展。</li>
<li>PCIは臨床・意識状態研究で一定の有用性が示されている。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1093/nc/niad016" target="_blank">PCI と GWT の整合可能性検討</a>、<a href="https://doi.org/10.31234/osf.io/rdq52" target="_blank">Structured Adversarial Collaboration Process</a>、<a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">Adversarial testing of global neuronal workspace and integrated information theories of consciousness</a>、<a href="https://arxiv.org/abs/2212.14787v1" target="_blank">Integrated Information Theory (IIT) 4.0</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>理論間を同条件で比較する公開ベンチが不足。</li>
<li>IIT計算量問題を回避した近似指標の妥当域が未確定。</li>
<li>複数理論を統合した実務的判定規約が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.31234/osf.io/gauqm_v1" target="_blank">IIT の実験予測可能性に関する検討</a>、<a href="https://doi.org/10.31234/osf.io/kxywt" target="_blank">弱い IIT の分解と評価</a>、<a href="https://doi.org/10.1101/2020.01.08.898775" target="_blank">PCI の再現性評価（TMS-EEG）</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Nature]</strong> <a href="https://doi.org/10.1038/s41586-025-08888-1" target="_blank">Adversarial testing of global neuronal workspace and integrated information theories</a> (2025)</li>
<li><strong>[PLOS ONE]</strong> <a href="https://doi.org/10.1371/journal.pone.0268577" target="_blank">Adversarial collaboration protocol for consciousness theory testing</a> (2023)</li>
<li><strong>[Neuroscience of Consciousness]</strong> <a href="https://doi.org/10.1093/nc/niad016" target="_blank">Compatibility between PCI and global neuronal workspace theory</a> (2023)</li>
<li><strong>[Entropy]</strong> <a href="https://doi.org/10.3390/e25020334" target="_blank">System Integrated Information</a> (2023)</li>
<li><strong>[Journal of NeuroEngineering and Rehabilitation]</strong> <a href="https://doi.org/10.1186/s12984-024-01455-1" target="_blank">PCI in rTMS treatment responsiveness study</a> (2024)</li>
<li><strong>[Neuron]</strong> <a href="https://doi.org/10.1016/j.neuron.2024.03.002" target="_blank">Anesthesia and neurobiology of consciousness</a> (2024)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/rdq52" target="_blank">Structured Adversarial Collaboration Process</a> (2024)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2212.14787v1" target="_blank">Integrated Information Theory (IIT) 4.0</a> (2022)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/gauqm_v1" target="_blank">Does IIT make experimental predictions about consciousness?</a> (2025)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/kxywt" target="_blank">Separating weak IIT into IIT-inspired and aspirational-IIT approaches</a> (2023)</li>
<li><strong>[bioRxiv]</strong> <a href="https://doi.org/10.1101/2020.01.08.898775" target="_blank">Reliability of the perturbational complexity index using TMS-EEG</a> (2020)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4382048961" target="_blank">An adversarial collaboration to critically evaluate theories of consciousness</a> (2023)</li>
<li><strong>[Oxford]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198520917.003.0012" target="_blank">The global neuronal workspace</a> (2006)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W3092295352" target="_blank">The predictive global neuronal workspace: an active inference model</a> (2020)</li>
</ol>
</section>

<section class="section" id="u12">
<h2 class="section-title">U12: 分岐本人性</h2>
<p><strong>厳密定義:</strong> 複製・分岐後に発生する複数主体の同一性・責任・権利帰属を、技術評価と整合する形式で規定できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>分岐後主体の識別子を何に基づいて付与するか。</li>
<li>責任・権利・同意の継承ルールをどの時点で分岐させるか。</li>
<li>心理的連続性基準と法的個体基準の不一致をどう扱うか。</li>
<li>技術評価（性能）と人格評価（帰属）をどう接続するか。</li>
<li>分岐主体間で記憶編集・再同期が起きた場合、法的主体IDを再編する基準は何か。</li>
<li>同意撤回が発生したとき、複数分岐主体への権限剥奪を技術的にどう実装・監査するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>哲学的には分岐問題（duplications, fission）に関する論点整理が進んでいる。</li>
<li>心理的連続性 vs 数的同一性の対立構造は明確。</li>
<li>法制度側でデジタル人格・データ主体性の議論が拡大。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a>、<a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a>、<a href="https://doi.org/10.20318/universitas.2025.9574" target="_blank">Neurotecnologías y neuroderechos</a>、<a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>技術システムに直結する運用規約（監査・責任追跡）が未整備。</li>
<li>分岐後の評価KPI（福祉・責任・所有）を定義する実務設計が不足。</li>
<li>国際法域をまたぐ整合ルールが未確定。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.52340/scai.2025.02.13" target="_blank">Digital Identity and Legal Personhood</a>、<a href="https://doi.org/10.69971/lra.3.1.2025.42" target="_blank">Legal Personhood and Identity of Human Digital Twins</a>、<a href="https://doi.org/10.1007/978-1-137-01616-4_15" target="_blank">Defining Identity IV: Personhood</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Minds and Machines]</strong> <a href="https://doi.org/10.1007/s11023-014-9352-8" target="_blank">Uploading and Branching Identity</a> (2014)</li>
<li><strong>[Oxford]</strong> <a href="https://doi.org/10.1093/acprof:oso/9780198754855.003.0013" target="_blank">Enhancement, Mind-Uploading, and Personal Identity</a> (2016)</li>
<li><strong>[Cambridge]</strong> <a href="https://doi.org/10.1017/9781009486309.002" target="_blank">The Right to Personal Identity</a> (2026)</li>
<li><strong>[Patterns]</strong> <a href="https://linkinghub.elsevier.com/retrieve/pii/S2666389923002453" target="_blank">No legal personhood for AI (DOI: 10.1016/j.patter.2023.100861)</a> (2023)</li>
<li><strong>[EU Law]</strong> <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU AI Act (Regulation (EU) 2024/1689)</a> (2024)</li>
<li><strong>[Council of Europe]</strong> <a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">Framework Convention on AI (CETS No.225)</a> (2024)</li>
<li><strong>[Bioethics]</strong> <a href="https://doi.org/10.1111/bioe.70045" target="_blank">Digitizing Dignity: Digital Twins and Human Dignity</a> (2025)</li>
<li><strong>[AI and Society]</strong> <a href="https://doi.org/10.1007/s00146-025-02796-8" target="_blank">What makes a digital human twin more than a simulation?</a> (2025)</li>
<li><strong>[ISO]</strong> <a href="https://www.iso.org/standard/42001" target="_blank">ISO/IEC 42001 AI management systems</a> (2023)</li>
<li><strong>[OECD]</strong> <a href="https://oecd.ai/en/ai-principles/" target="_blank">OECD AI Principles</a> (運用中)</li>
<li><strong>[NIST]</strong> <a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">NIST AI RMF: Generative AI Profile</a> (2024)</li>
<li><strong>[Science and Innovation]</strong> <a href="https://doi.org/10.52340/scai.2025.02.13" target="_blank">Digital Identity and Legal Personhood</a> (2025)</li>
<li><strong>[Legal Research and Analysis]</strong> <a href="https://doi.org/10.69971/lra.3.1.2025.42" target="_blank">Legal Personhood and Identity of Human Digital Twins</a> (2025)</li>
<li><strong>[Palgrave]</strong> <a href="https://doi.org/10.1007/978-1-137-01616-4_15" target="_blank">Defining Identity IV: Personhood</a> (2014)</li>
</ol>
<h3>監査導線（Round 23 追加）</h3>
<ul>
<li>EU AI Act 手続き履歴: <a href="https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=CELEX:32024R1689" target="_blank">EUR-Lex Procedure timeline</a></li>
<li>EU 手続番号ページ: <a href="https://eur-lex.europa.eu/procedure/EN/2021_106" target="_blank">Procedure 2021_106</a></li>
<li>CoE 条約詳細（CETS 225）: <a href="https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=225" target="_blank">Treaty Office detail</a></li>
<li>CoE 最近の更新: <a href="https://www.coe.int/en/web/conventions/recent-changes" target="_blank">Treaty Office recent changes</a></li>
</ul>
</section>

<section class="section" id="u13">
<h2 class="section-title">U13: 模倣分離</h2>
<p><strong>厳密定義:</strong> 高性能模倣（言語/行動出力）と、内部因果構造保存を識別する評価軸を実験的に分離できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>brain-to-text成功を『意味復元』と『因果再現』へ分解できるか。</li>
<li>LLMの幻覚・整合性検査を神経デコード評価へどう接続するか。</li>
<li>同一出力でも内部機構が異なるケースをどう検出するか。</li>
<li>模倣性能の上限を因果評価でどこまで抑制できるか。</li>
<li>視覚知覚と視覚想起で同一デコーダを使ったとき、意味復元精度の劣化パターンはどこで分岐するか。</li>
<li>プロンプト誘導・データリーク・shortcut学習を分離検出する対照実験をどう設計するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>非侵襲脳活動からのsemantic decoding/brain-to-textは急速に進展。</li>
<li>LLM幻覚検出・自己整合性評価の方法論は拡張中。</li>
<li>『出力一致だけでは内部同一性を保証しない』点は広く共有。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">Mind captioning</a>、<a href="https://doi.org/10.1088/1741-2552/adfab1" target="_blank">Brain-to-text decoding with context-aware neural representations and large language models</a>、<a href="https://doi.org/10.1101/2022.09.29.509744" target="_blank">Semantic reconstruction of continuous language from non-invasive brain recordings</a>、<a href="https://doi.org/10.1002/brx2.37" target="_blank">Advancements and implications of semantic reconstruction</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>模倣と因果保存を同時評価する統一ベンチが不足。</li>
<li>神経デコードでのデータリーク・shortcut学習検出が不十分。</li>
<li>介入実験を含む因果評価の標準手順が未整備。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.18653/v1/2025.emnlp-industry.139" target="_blank">Zero-knowledge LLM hallucination detection and mitigation</a>、<a href="https://doi.org/10.18653/v1/2025.findings-emnlp.527" target="_blank">Factuality Hallucination Type Detection via Belief State</a>、<a href="https://doi.org/10.1101/2024.03.19.585656" target="_blank">Decoding Continuous Character-based Language from Non-invasive Brain Recordings</a>。</p>
<h3>主要先行研究（再精査 14 件）</h3>
<ol>
<li><strong>[Science Advances]</strong> <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">Mind captioning: Evolving descriptive text of mental content from human brain activity</a> (2025)</li>
<li><strong>[Nature Neuroscience]</strong> <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Semantic reconstruction of continuous language from non-invasive brain recordings</a> (2023)</li>
<li><strong>[Cell Reports]</strong> <a href="https://doi.org/10.1016/j.celrep.2024.114924" target="_blank">A brain-to-text framework for decoding natural tonal sentences</a> (2024)</li>
<li><strong>[Journal of Neural Engineering]</strong> <a href="https://doi.org/10.1088/1741-2552/adfab1" target="_blank">Brain-to-text decoding with context-aware neural representations and large language models</a> (2025)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2506.22486" target="_blank">Hallucination Detection with Small Language Models</a> (2025)</li>
<li><strong>[EMNLP Industry]</strong> <a href="https://doi.org/10.18653/v1/2025.emnlp-industry.139" target="_blank">Zero-knowledge LLM hallucination detection and mitigation</a> (2025)</li>
<li><strong>[Findings of EMNLP]</strong> <a href="https://doi.org/10.18653/v1/2025.findings-emnlp.527" target="_blank">Factuality hallucination type detection via belief state</a> (2025)</li>
<li><strong>[AAAI]</strong> <a href="https://doi.org/10.1609/aaai.v39i27.35124" target="_blank">Representation Learning: A Causal Perspective</a> (2025)</li>
<li><strong>[AAAI]</strong> <a href="https://doi.org/10.1609/aaai.v39i17.33998" target="_blank">Learning strategy representation for imitation learning in multi-agent games</a> (2025)</li>
<li><strong>[Knowledge-Based Systems]</strong> <a href="https://doi.org/10.1016/j.knosys.2025.113565" target="_blank">Causal representation learning in offline visual reinforcement learning</a> (2025)</li>
<li><strong>[Nature Machine Intelligence]</strong> <a href="https://doi.org/10.1038/s42256-020-00257-z" target="_blank">Shortcut learning in deep neural networks</a> (2020)</li>
<li><strong>[IEEE EMBC]</strong> <a href="https://doi.org/10.1109/EMBC58623.2025.11251641" target="_blank">Decoding visual imagination and perception from EEG via topomap sequences</a> (2025)</li>
<li><strong>[IEEE EMBC]</strong> <a href="https://doi.org/10.1109/EMBC53108.2024.10782730" target="_blank">Decoding visual perception from EEG using explainable graph neural networks</a> (2024)</li>
<li><strong>[bioRxiv]</strong> <a href="https://doi.org/10.1101/2024.03.19.585656" target="_blank">Decoding continuous character-based language from non-invasive brain recordings</a> (2024)</li>
</ol>
</section>

<section class="section" id="u14">
<h2 class="section-title">U14: 追試可能性</h2>
<p><strong>厳密定義:</strong> 第三者が同一データ・同一手順・同一評価契約で同等結論に到達できる公開運用を常時維持できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>データ/コード/評価環境の固定粒度をどこまで要求するか。</li>
<li>探索研究と検証研究を運用上どう分離するか。</li>
<li>leaderboardでのリーク・過適合・報告バイアスをどう監査するか。</li>
<li>Model Card / Dataset Card を評価契約へどう統合するか。</li>
<li>再現失敗ケースを否定例レジストリとして公開し、再試行サイクルをどう運用するか。</li>
<li>コンテナ固定（OS・依存ライブラリ・乱数種）を必須化した場合、再現コスト増分をどこまで許容するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>再現性危機を受け、preregistration・open science実践は拡大。</li>
<li>Model Card / Dataset Card の実務フレームは利用可能。</li>
<li>ベンチ運用の落とし穴（リーク、データ重複）に関する知見は豊富。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1098/rsos.210155" target="_blank">Preregistration template for cognitive models</a>、<a href="https://doi.org/10.31219/osf.io/xsfam" target="_blank">Preregistration and increased transparency will benefit science</a>、<a href="https://doi.org/10.1038/s41746-022-00592-y" target="_blank">Methodological failures in medical imaging ML and recommendations</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>神経科学×機械学習を跨ぐ共通監査規約が不十分。</li>
<li>失敗例を継続公開する文化・実装が限定的。</li>
<li>長期運用での評価劣化を追跡する仕組みが不足。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1093/oso/9780190881481.003.0007" target="_blank">The Reproducibility Crisis</a>、<a href="https://doi.org/10.1098/rsos.242057" target="_blank">Open science interventions to improve reproducibility and replicability of research</a>、<a href="https://doi.org/10.31234/osf.io/dzsh4" target="_blank">Barriers and solutions for early career researchers in tackling reproducibility</a>、<a href="https://doi.org/10.37473/dac/10.1002/jrsm.1540" target="_blank">PreregRS guides preregistration for research syntheses</a>。</p>
<h3>主要先行研究（再精査 16 件）</h3>
<ol>
<li><strong>[Royal Society Open Science]</strong> <a href="https://doi.org/10.1098/rsos.210155" target="_blank">Preregistration template for the application of cognitive models</a> (2021)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31219/osf.io/xsfam" target="_blank">Preregistration and increased transparency will benefit science</a> (2017)</li>
<li><strong>[npj Digital Medicine]</strong> <a href="https://doi.org/10.1038/s41746-022-00592-y" target="_blank">Methodological failures in medical imaging ML and recommendations</a> (2022)</li>
<li><strong>[Book Chapter]</strong> <a href="https://doi.org/10.1093/oso/9780190881481.003.0007" target="_blank">The Reproducibility Crisis</a> (2019)</li>
<li><strong>[Royal Society Open Science]</strong> <a href="https://doi.org/10.1098/rsos.242057" target="_blank">Open science interventions to improve reproducibility and replicability</a> (2024)</li>
<li><strong>[OSF]</strong> <a href="https://doi.org/10.31234/osf.io/dzsh4" target="_blank">Barriers and solutions for early career researchers in reproducibility</a> (2018)</li>
<li><strong>[PreregRS]</strong> <a href="https://doi.org/10.37473/dac/10.1002/jrsm.1540" target="_blank">PreregRS guides preregistration for research syntheses</a> (2022)</li>
<li><strong>[Journal of Neuroscience Methods]</strong> <a href="https://doi.org/10.1016/j.jneumeth.2023.109931" target="_blank">Methodical advances in reproducibility research</a> (2023)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Motion-BIDS extension for reproducible motion data</a> (2024)</li>
<li><strong>[Scientific Data]</strong> <a href="https://doi.org/10.1038/s41597-023-02614-0" target="_blank">A comparison of neuroelectrophysiology databases</a> (2023)</li>
<li><strong>[Epilepsia Open]</strong> <a href="https://doi.org/10.1002/epi4.12704" target="_blank">EEG datasets for seizure detection and prediction: a review</a> (2023)</li>
<li><strong>[eLife]</strong> <a href="https://doi.org/10.7554/eLife.85980" target="_blank">Enhancing precision in human neuroscience</a> (2023)</li>
<li><strong>[JAMA]</strong> <a href="https://doi.org/10.1001/jama.2025.13350" target="_blank">TARGET statement for transparent reporting</a> (2025)</li>
<li><strong>[BIDS]</strong> <a href="https://bids-specification.readthedocs.io/en/stable/" target="_blank">BIDS Specification 1.10.1</a> (2025更新版)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2311.04912" target="_blank">ezBIDS for curation and validation workflow</a> (2023)</li>
<li><strong>[Zenodo]</strong> <a href="https://zenodo.org/records/18201723" target="_blank">BEP036 draft metadata extension</a> (2025)</li>
</ol>
</section>

<section class="section" id="u15">
<h2 class="section-title">U15: 制度統合</h2>
<p><strong>厳密定義:</strong> 技術評価KPIと法/倫理KPIを連動させ、停止基準と公開基準を運用レベルで定義できるか。</p>
<h3>リサーチクエスチョン分解</h3>
<ol>
<li>神経データの機微性をどの法概念で扱うか（個人情報・生体情報・人格情報）。</li>
<li>neurorightsを技術監査項目へどう写像するか。</li>
<li>法域差（EU/US/JP等）を跨ぐ最小共通運用をどう定義するか。</li>
<li>技術進展に応じた停止条件・更新条件をどうガバナンス化するか。</li>
</ol>
<h3>今、解かれているもの（文献で積み上がっている領域）</h3>
<ul>
<li>neurorights・神経データ保護に関する政策議論と法案提案は拡大。</li>
<li>BCIプライバシー・安全性のリスク領域は比較的明確化。</li>
<li>AIガバナンス枠組みを神経技術へ接続する試みが増加。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1007/978-3-030-72254-8_19" target="_blank">Privacy and Security in Brain-Computer Interfaces</a>、<a href="https://doi.org/10.1201/9781351231954-34" target="_blank">Privacy and Ethics in Brain-Computer Interface Research</a>、<a href="https://doi.org/10.1007/s11673-025-10440-9" target="_blank">Ethical Governance Strategies for the Responsible Innovation of Neurotechnologies</a>、<a href="https://doi.org/10.2196/56665" target="_blank">Ethics and Governance of Neurotechnology in Africa</a>。</p>
<h3>これから研究が必要なもの（未解決）</h3>
<ul>
<li>技術指標と法的停止基準を結びつけた実装規格が不足。</li>
<li>国際相互運用可能な監査テンプレートが未整備。</li>
<li>研究用途と商用用途の境界で運用ルールが分断。</li>
</ul>
<p class="small"><strong>根拠例:</strong> <a href="https://doi.org/10.1017/9781009207898.029" target="_blank">Responsible AI Healthcare and Neurotechnology Governance</a>、<a href="https://doi.org/10.4337/9781786438515.00015" target="_blank">Social values and privacy law and policy</a>、<a href="https://api.openalex.org/W4200185524" target="_blank">On Neurorights</a>。</p>
<h3>主要先行研究（再精査 16 件）</h3>
<ol>
<li><strong>[EU Law]</strong> <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank">EU AI Act (Regulation (EU) 2024/1689)</a> (2024)</li>
<li><strong>[Lancet Neurology]</strong> <a href="https://doi.org/10.1016/S1474-4422(25)00124-3" target="_blank">Neurorights in neurology</a> (2025)</li>
<li><strong>[Journal of Human Rights Practice]</strong> <a href="https://doi.org/10.1093/jhuman/huae042" target="_blank">Establishing Neurorights: New Rights versus Derived Rights</a> (2024)</li>
<li><strong>[NIST]</strong> <a href="https://doi.org/10.6028/NIST.AI.600-1" target="_blank">NIST AI RMF: Generative AI Profile</a> (2024)</li>
<li><strong>[OECD]</strong> <a href="https://oecd.ai/en/ai-principles/" target="_blank">OECD AI Principles</a> (運用中)</li>
<li><strong>[Council of Europe]</strong> <a href="https://book.coe.int/en/texts-of-council-of-europe-treaties/12225-council-of-europe-framework-convention-on-artificial-intelligence-and-human-rights-democracy-and-the-rule-of-law-cets-no-225.html" target="_blank">Framework Convention on AI (CETS No.225)</a> (2024)</li>
<li><strong>[ISO]</strong> <a href="https://www.iso.org/standard/42001" target="_blank">ISO/IEC 42001 AI management systems</a> (2023)</li>
<li><strong>[AISC]</strong> <a href="https://doi.org/10.1007/978-3-030-72254-8_19" target="_blank">Privacy and Security in Brain-Computer Interfaces</a> (2021)</li>
<li><strong>[Handbook Chapter]</strong> <a href="https://doi.org/10.1201/9781351231954-34" target="_blank">Privacy and Ethics in Brain-Computer Interface Research</a> (2018)</li>
<li><strong>[Bioethics]</strong> <a href="https://doi.org/10.1007/s11673-025-10440-9" target="_blank">Ethical Governance Strategies for Responsible Neurotechnology</a> (2025)</li>
<li><strong>[JMIR Neurotechnology]</strong> <a href="https://doi.org/10.2196/56665" target="_blank">Ethics and Governance of Neurotechnology in Africa: Lessons from AI</a> (2024)</li>
<li><strong>[Cambridge Handbook]</strong> <a href="https://doi.org/10.1017/9781009207898.029" target="_blank">Responsible AI Healthcare and Neurotechnology Governance</a> (2022)</li>
<li><strong>[Research Handbook]</strong> <a href="https://doi.org/10.4337/9781786438515.00015" target="_blank">Social values and privacy law and policy</a> (2022)</li>
<li><strong>[Frontiers]</strong> <a href="https://api.openalex.org/W4200185524" target="_blank">On Neurorights</a> (2021)</li>
<li><strong>[arXiv]</strong> <a href="https://arxiv.org/abs/2407.14390v1" target="_blank">Honest Computing: demonstrable data lineage and provenance</a> (2024)</li>
<li><strong>[OpenAlex]</strong> <a href="https://api.openalex.org/W4379053109" target="_blank">Equal access to mental augmentation</a> (2023)</li>
</ol>
<h3>監査導線（Round 23 追加）</h3>
<ul>
<li>EU AI Act 手続き履歴: <a href="https://eur-lex.europa.eu/legal-content/EN/HIS/?uri=CELEX:32024R1689" target="_blank">EUR-Lex Procedure timeline</a></li>
<li>NIST AI RMF 開発履歴: <a href="https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-development" target="_blank">NIST AI RMF Development</a></li>
<li>OECD 法的本文: <a href="https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449" target="_blank">OECD-LEGAL-0449</a></li>
<li>OECD 2024 改訂公表: <a href="https://www.oecd.org/en/about/news/press-releases/2024/05/oecd-updates-ai-principles-to-stay-abreast-of-rapid-technological-developments.html" target="_blank">OECD press release (2024 update)</a></li>
</ul>
</section>

</article>
<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連ページ</h4>
<ul>
<li><a href="verification.html">Verification Commons →</a></li>
<li><a href="tech_roadmap.html#unsolved">Roadmap: Unsolved Questions →</a></li>
<li><a href="mind_uploading_papers.html">Paper Archive →</a></li>
<li><a href="issue.html#proposal-integration">Technical Proposals →</a></li>
</ul>
</div>
<div class="note-box">
<strong>運用方針</strong>
<p>このページは『実体のある引用と未解決定義』を更新する場所です。実行不能な主提案ではなく、検証可能な差分と証跡を残します。</p>
</div>
</aside>
</main>
