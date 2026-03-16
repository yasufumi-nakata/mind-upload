---
layout: default
title: "Wiki：Decode と Emulate"
description: "観測の翻訳としての decode と、内部因果を再現する emulate の違いを、一次文献と必要証拠で整理します。"
article_type: Wiki
subtitle: "出力一致は入口、介入一致と閉ループ安定性は別の壁です"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Technical / natural science only"
audience: "decode と emulate を、技術と自然科学の根拠だけで区別したい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload で重要な区別である decode と emulate の違いを、一次文献ベースで整理する補助ページです。何が '高性能な翻訳機' で、何が '内部状態を動かす系' に近いのかを、観測・介入・閉ループの証拠で見分けるために使います。"
accuracy_note: "ここで示すのは技術的な境界条件です。十分条件の最終合意や、WBE 全体の達成判定を単独で与えるページではありません。"
page_highlights:
  - "decode は観測からラベルや文を当てる主張で、emulate は内部状態の時間発展と介入応答を含む主張です。"
  - "d'Ascoli 2025 や Tang 2023 は non-invasive decode の前線を押し上げましたが、そのまま unrestricted thought reading や state reconstruction ではありません。"
  - "Littlejohn 2025 と Wairagkar 2025 は streaming / voice-synthesis neuroprosthesis を大きく前進させましたが、communication subsystem の L2〜L3 証拠であって全脳 emulation ではありません。"
  - "same-session streaming success と chronic deployability は別の evidence class であり、fixed decoder interval・recalibration burden・same-neuron audit を分けて出します。"
  - "connectome-constrained prediction は重要ですが、Beiran & Litwin-Kumar 2025 が示すように parameter degeneracy と未測定状態の壁は残ります。"
known_points:
  - "decode は主に L1、局所的な閉ループ義継や介入応答は L2〜L3 に近い主張です。"
  - "出力一致だけでは、内部因果構造や状態変数の十分性を示せません。"
  - "language prior、candidate set、subject cooperation を分けて出さない限り、非侵襲 decode を過大評価しやすくなります。"
  - "tail latency、silence / abstention、recalibration burden は offline accuracy と別の軸であり、closed-loop claim の必須ログです。"
  - "microelectrode 系では same neuron across days は観測事実ではなく、motion correction・sorting・probabilistic matching を介した推定です。"
unknown_points:
  - "どの程度の介入一致と状態変数の完全性があれば '十分に emulate した' と言えるかは未確定です。"
  - "局所回路の義継から全脳 emulation へどう外挿できるかは、まだ公開 benchmark がありません。"
  - "connectome-constrained model に same-brain function や maintenance-state をどこまで足せば縮退が十分にほどけるかも未確定です。"
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
  - label: "Wiki: state・trait・ドリフト"
    url: "/wiki/state-trait-and-drift.html"
    description: "cross-day / chronic claim で drift と recalibration burden をどう読むかを補います。"
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

<div class="note-box">
<strong>2026-03 文献監査で改めた点</strong>
<p>
旧版の弱点は、decode と emulate の原理差自体は正しかった一方で、2025 年の一次文献が押し上げた <strong>open-vocabulary non-invasive decode</strong>、<strong>streaming / voice-synthesis neuroprosthesis</strong>、<strong>connectome-constrained prediction</strong> を、どの水準で止めるべきかの <strong>site rule</strong> まで落とし切れていなかった点でございます。今回の更新では、<strong>language prior</strong>、<strong>tail latency / silence / recalibration burden</strong>、<strong>fixed decoder interval</strong>、<strong>same-neuron tracking audit</strong>、<strong>parameter degeneracy</strong> を decode/emulate 境界の必須監査項目へ昇格させました。
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
<td>2025年に増えた誤読</td>
<td>open-vocabulary word decode や streaming voice 出力を、そのまま「自由思考の読心術」や「内部再現」と読み替えやすいです。</td>
<td>connectome-constrained prediction や局所 closed loop を、そのまま全脳 emulation の証拠と読み替えやすいです。</td>
<td>LM-only / no-brain / shuffle baseline、subsystem scope、state completeness を同時に出します。</td>
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
<tr>
<td>最低限残すログ</td>
<td>candidate set、LM の有無、subject cooperation、校正と棄権率、cross-day 劣化です。</td>
<td>摂動ログ、P50/P95/P99 latency、silence / abstention、recalibration burden、latent state の残差です。</td>
<td>速さ、精度、安定性、hidden state を別の列として残します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="chronic-communication-ceiling">
<h2 class="section-title">2026-03-17 追補：侵襲 communication route の chronic ceiling</h2>
<table class="data-table">
<thead>
<tr>
<th>壁</th>
<th>一次文献が今支持すること</th>
<th>このページで許す読み方</th>
<th>まだ上げない主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>same-session streaming ceiling</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> は streaming brain-to-voice、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> は instantaneous voice synthesis と silence fallback を前進させました。</td>
<td>communication subsystem の強い L2〜L3 証拠として読みます。</td>
<td>fixed decoder の長期保持や chronic deployability を、そのまま主張しません。</td>
</tr>
<tr>
<td><strong>recalibration ceiling</strong></td>
<td><a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> は one-month の unsupervised recalibration を検証し、<a href="https://doi.org/10.1038/s42003-024-06784-4" target="_blank">Pun et al. (2024)</a> は chronic human intracortical recording の instability が BCI performance 低下と強く結びつくことを示しました。</td>
<td><code>time since last supervised calibration</code>、recovery time、recalibration burden を別ログに出す限りで、長期運用の前段として読みます。</td>
<td>「その日に動いた」ことを「再較正なしで長期に成立した」とは書きません。</td>
</tr>
<tr>
<td><strong>same-neuron tracking ceiling</strong></td>
<td><a href="https://doi.org/10.1126/science.abf4588" target="_blank">Steinmetz et al. (2021)</a> は motion correction 付き stable recording、<a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">Pachitariu et al. (2024)</a> は drift / split / merge を中心に据えた sorting、<a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">van Beest et al. (2025)</a> は probabilistic cross-day neuron tracking を前進させました。</td>
<td>microelectrode 系では、same-neuron claim を <code>sorting version + drift correction + unit-match probability</code> 付きの推定として読みます。</td>
<td>chronic decode 成功を、そのまま stable single-neuron mechanism の直読とは書きません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>この節での実務ルール</strong>
<p>
侵襲 speech BCI を上位主張へ進めるときは、同日内の streaming 性能だけでなく、<strong>固定 decoder が何日持つか</strong>、<strong>どれだけ人手再較正に依存したか</strong>、<strong>microelectrode 系なら same-neuron tracking をどう推定したか</strong>、<strong>implant age / material / geometry / tissue-response proxy をどう監査したか</strong>を同時に出します。背景の長い整理は <a href="state-trait-and-drift.html">Wiki: state・trait・ドリフト</a> を参照してください。
</p>
</div>
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
<td><strong>d'Ascoli et al. (2025)</strong><br>open-vocabulary non-invasive word decoding</td>
<td>723 人規模の non-invasive recordings から individual word decoding を進め、モダリティ・課題・データ量で性能が大きく動くことも示しました。</td>
<td>open-vocabulary の前進ではありますが、word onset や課題構造、参加者条件への依存が残ります。ここで前進したのは communication route の decode であり、state-complete reconstruction ではありません。</td>
</tr>
<tr>
<td><strong>Willett et al. (2023)</strong><br>侵襲 speech BCI</td>
<td>intracortical array から 125,000 語語彙で 62 words/min の large-vocabulary speech decoding を示しました。</td>
<td>高帯域であっても、主張の中心は attempted speech の decode です。自律的な内部生成や、条件変更への因果的一致までは示していません。</td>
</tr>
<tr>
<td><strong>Littlejohn et al. (2025) / Wairagkar et al. (2025)</strong><br>streaming brain-to-voice / voice synthesis</td>
<td>Littlejohn らは 80 ms ごとの streaming brain-to-voice、Wairagkar らは neural-to-voice algorithm の 10 ms 未満推論と silence fallback を示しました。</td>
<td>これは communication subsystem の強い L2〜L3 証拠ですが、全脳 emulation ではありません。さらに速さだけでなく tail latency、dropout、silence / false speech、recalibration burden を出さない限り、長期 deployability も読めません。</td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong><br>双方向 closed-loop BCI</td>
<td>motor decode に tactile feedback を返すことで、ロボット把持課題の所要時間を 20.9 秒から 10.2 秒へ短縮しました。</td>
<td>decode より一段強い局所閉ループ実証ですが、対象は感覚運動サブシステムです。全脳 emulation ではなく、<strong>局所回路での L3 に近い証拠</strong>として読むのが妥当です。</td>
</tr>
<tr>
<td><strong>MICrONS (2025) / Billeh et al. (2020) / Beiran &amp; Litwin-Kumar (2025)</strong><br>digital twin / connectome-constrained model</td>
<td>same-brain function + connectomics dataset と multi-scale model が公開され、connectome-constrained recurrent network の予測力も前進しました。</td>
<td>これは emulate に近い方向の重要基盤ですが、領域・個体・課題は限定的です。さらに Beiran &amp; Litwin-Kumar (2025) と Prinz et al. (2004) が示すように、未測定パラメータや unrecorded neurons を含む縮退が残るため、出力一致だけでは忠実再現とも唯一解とも言えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="audit-2026-03">
<h2 class="section-title">2026-03 文献監査：ここで禁止する 3 つの読み替え</h2>
<table class="data-table">
<thead>
<tr>
<th>危険な読み替え</th>
<th>なぜ危険か</th>
<th>一次文献が今支持する境界</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>open-vocabulary non-invasive decode → unrestricted thought reading</strong></td>
<td>2025 年の単語 decode は確かに前進ですが、課題構造、candidate set、participant cooperation、モダリティ差の影響を強く受けます。</td>
<td>Tang (2023) と d'Ascoli (2025) から比較的強く言えるのは、<strong>条件付きの language / communication decode</strong>が進んだことです。そこから直接、内部状態の一般的一意復元や WBE 必須状態の取得までは言えません。</td>
</tr>
<tr>
<td><strong>streaming speech neuroprosthesis → emulate / WBE</strong></td>
<td>streaming や voice synthesis は communication subsystem の大きな達成ですが、速く話せることと内部因果の十分性は別です。</td>
<td>Littlejohn (2025) と Wairagkar (2025) が押し上げたのは <strong>侵襲系 communication route の L2〜L3</strong>であり、Wilson (2025) が示すように long-term recalibration burden も別の壁です。</td>
</tr>
<tr>
<td><strong>connectome-constrained prediction → unique internal mechanism</strong></td>
<td>connectome や same-brain function を入れても、未測定 biophysical parameter と hidden state が残ると内部 dynamics は縮退しえます。</td>
<td>MICrONS (2025)、Billeh (2020)、Beiran &amp; Litwin-Kumar (2025) から比較的強く言えるのは、<strong>構造制約が予測を助ける</strong>ことです。そこから直接、state-complete reconstruction や唯一の internal model へは進めません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="gates">
<h2 class="section-title">decode を emulate と読み替える前の 5 つのゲート</h2>
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
<td><strong>G1: 脳由来情報が prior を上回るか</strong></td>
<td>language prior や candidate set が強いと、出力の流暢さだけでは neural contribution を見誤ります。</td>
<td><code>LM-only</code>、<code>no-brain</code>、time-shuffle、trial-shuffle、candidate set size、participant cooperation の開示。</td>
</tr>
<tr>
<td><strong>G2: 未学習条件と別日で保つか</strong></td>
<td>同じ被験者・同じ日・同じ課題だけで高精度でも、機構が合っているとは限りません。</td>
<td>OOD 条件、cross-day、別刺激集合、被験者外評価、固定 decoder の劣化曲線、棄権率。</td>
</tr>
<tr>
<td><strong>G3: 介入に応答するか</strong></td>
<td>emulate を名乗るなら、観測だけでなく摂動後の分岐も当てる必要があります。</td>
<td>刺激変更、ICMS/TMS、薬理、課題ルール変更に対する予測一致。</td>
</tr>
<tr>
<td><strong>G4: 閉ループと長期運用で安定か</strong></td>
<td>出力が次の入力を変えると、offline accuracy はそのまま通用しません。さらに within-session の速さと long-term deployability も別問題です。</td>
<td>end-to-end latency の <code>P50/P95/P99</code>、tail latency、silence / abstention、dropout、<strong>fixed decoder interval</strong>、<code>time since last supervised calibration</code>、recalibration burden、recovery time。</td>
</tr>
<tr>
<td><strong>G5: 状態変数が足りており、縮退を監査したか</strong></td>
<td>同じ出力でも異なる内部パラメータ集合がありえます。状態欠損と model family の縮退を伏せると過大主張になります。</td>
<td>connectome-only baseline と augmentation 比較、family comparison、不確実性、cell type / synaptic state / delay / neuromodulation / glia の監査に加え、chronic microelectrode 系では <strong>sorting version</strong>、<strong>drift correction</strong>、<strong>unit-match probability</strong> も併記します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">このサイトでの運用ルール</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>decode と書く条件：</strong>観測信号から意味、刺激、行動、文章を予測する実証が中心で、<code>LM-only</code> や shuffle baseline を上回る neural contribution が示されていても、介入一致までは出ていないときです。</li>
<li><strong>communication subsystem の L2〜L3 と書く条件：</strong>speech BCI や tactile BCI のように局所 loop が成立していても、対象が限定サブシステムであること、latency / silence / <strong>fixed decoder interval</strong> / recalibration burden を含むことを明示し、microelectrode 系なら unit identity audit も添えます。</li>
<li><strong>局所 emulation と書ける条件：</strong>局所回路で、closed loop と因果介入の双方が示され、何を置換したかが限定的に明示されているときです。</li>
<li><strong>WBE に近いと書く条件：</strong>prior 超過、OOD / cross-day 一般化、摂動一致、閉ループ長期安定性、状態変数の完全性監査の 5 点がそろったときだけです。</li>
<li><strong>出力一致だけのとき：</strong>avatar、behavioral clone、decoder、language interface といった表現に留め、emulate と言い換えません。</li>
<li><strong>connectome-constrained 成功の扱い：</strong>predictive gain や digital twin を structural / functional scaffold の前進として位置づけ、唯一解や state-complete reconstruction とは書きません。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Tang, J., LeBel, A., Jain, S., et al. (2023). Semantic reconstruction from non-invasive brain recordings. <em>Nature Neuroscience</em>, 26, 858–866. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <em>Nature Communications</em>, 16, 5606. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <em>Nature</em>, 620, 1031–1036. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>, 28, 1711–1719. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644, 145–152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Pun, T. K., Khoshnevis, M., Hosman, T., et al. (2024). Measuring instability in chronic human intracortical neural recordings towards stable, long-term brain-computer interfaces. <em>Communications Biology</em>, 7, 1363. <a href="https://doi.org/10.1038/s42003-024-06784-4" target="_blank">doi:10.1038/s42003-024-06784-4</a></li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <em>Science</em>, 372(6539), eabf4588. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>Pachitariu, M., Sridhar, S., Pennington, J., &amp; Stringer, C. (2024). Spike sorting with Kilosort4. <em>Nature Methods</em>, 21, 914–921. <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">doi:10.1038/s41592-024-02595-5</a></li>
<li>van Beest, E. H., Bimbard, C., Fabre, J. M. J., et al. (2025). Tracking neurons across days with high-density probes. <em>Nature Methods</em>, 22, 778–787. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
<li>Flesher, S. N., Downey, J. E., Weiss, J. M., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <em>Science</em>, 372(6544), 831–836. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 1323–1334. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
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
<li><a href="state-trait-and-drift.html">state・trait・ドリフト →</a></li>
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
