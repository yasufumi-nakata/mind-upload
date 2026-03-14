---
layout: default
title: "Wiki：EEG前処理とQC"
description: "参照法、フィルタ、アーティファクト処理、保持率、感度分析まで、EEG 前処理を受理条件として整理します。"
article_type: Wiki
subtitle: "前処理は見栄えではなく、主張の受理条件です"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Technical / practical guide"
audience: "EEG の前処理や QC が結果をどう動かすかを、根拠つきで整理したい人"
reading_time: "12〜18分"
page_intro: "このページは、EEG の前処理と QC を『最後に波形を整える作業』ではなく、『どの信号を残し、どの主張を許すかを決める監査工程』として整理する wiki です。"
accuracy_note: "万能の 1 手順は示しません。一次文献と公式仕様から、『最低限どこを固定し、何をまだ断言しないか』を整理します。"
page_highlights:
  - "参照法、フィルタ、アーティファクト処理は、ERP・connectivity・decoding の結論自体を動かしえます。"
  - "EEG-BIDS と COBIDAS-MEEG が強調するのは、アルゴリズム名より先に metadata と報告の完全性です。"
  - "アーティファクト除去は常に decoding 精度を上げるとは限らず、confound を減らした結果として精度が下がる場合もあります。"
  - "高 beta / gamma 帯は筋電汚染と重なるため、筋電監査なしに強く主張しません。"
known_points:
  - "前処理は小さな実装差ではなく、どの信号を neural とみなすかを決める選択です。"
  - "参照法、フィルタ設計、bad channel 処理、除外基準は最低限残すべき情報です。"
  - "EEG-BIDS と COBIDAS-MEEG は、再現可能な EEG 報告の床をかなり具体的に与えています。"
  - "artifact suppression と signal preservation は別であり、精度だけで前処理の良し悪しは決められません。"
unknown_points:
  - "どの課題でどの前処理族が最適かは、いまだ一律には決まりません。"
  - "高周波成分のどこまでを neural と扱えるかは、筋電・体動・課題依存性の監査を要します。"
  - "どの感度分析セットを site-wide の標準とするかも、今後のベンチ運用課題です。"
wiki_links:
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "信号そのものの性質から戻りたいときはこちらです。"
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "前処理の前段で必要な時刻同期、イベント、bad segment 記録を補います。"
  - label: "Wiki: 不確実性・校正・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "前処理差による推定幅や棄権の考え方を補います。"
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "BIDS、公開版、loader、benchmark の役割差を補います。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
  - label: "データ&ベンチ"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>最短結論</h2>
<p>
EEG の前処理は、図をきれいにする工程ではございません。<strong>どの信号を neural とみなし、どの主張を保留するかを決める監査工程</strong>でございます。したがって本サイトでは、参照法、フィルタ、アーティファクト処理、保持率、感度分析を、結果の後ろに付く補足ではなく <strong>受理条件</strong>として扱います。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここで扱うのは技術と自然科学の側面だけでございます。哲学、法制度、本人性は扱いません。問うのは「どの前処理が正義か」ではなく、<strong>どの条件を固定しないと EEG 由来の主張が過大化するか</strong>です。
</p>
</div>

<section class="section" id="why-this-matters">
<h2 class="section-title">今回深掘りする弱点</h2>
<p>
従来のページは、参照法、フィルタ、アーティファクト処理、除外基準という 4 論点を正しく挙げていました。しかし弱点は、<strong>なぜそれらが結果そのものを変えうるのか</strong>、そして <strong>何を残さないと主張レベルを上げられないのか</strong>が、一次文献ベースの監査ゲートになっていなかった点でございます。COBIDAS-MEEG と EEG-BIDS は報告の床をかなり具体的に与え、PREP pipeline は bad channel と rereference の相互依存を示し、Widmann らは filter design 自体が波形や latency を動かしうることを整理しました。さらに 2025 年の decoding 研究は、artifact correction が常に性能向上を意味しないことを示しています。したがって、この論点は実務上の小技ではなく、<strong>EEG 由来の主張の ceiling を決める本体</strong>でございます。
</p>
</section>

<section class="section" id="audit-gates">
<h2 class="section-title">先に固定する5つの監査ゲート</h2>
<table class="data-table">
<thead>
<tr>
<th>ゲート</th>
<th>一次文献・公式仕様が今支持すること</th>
<th>通っていないときに止める主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>metadata / 報告ゲート</strong></td>
<td>EEG-BIDS と COBIDAS-MEEG は、参照、ground、sampling rate、filters、bad channel、電極座標、events、除外規則を最低限の記録として要求します。</td>
<td>「再現可能な EEG 解析」「比較可能な clean EEG」と書くことです。</td>
</tr>
<tr>
<td><strong>参照ゲート</strong></td>
<td>PREP pipeline と reference comparison 研究は、bad channel 処理と rereference が波形・network 指標を動かすことを示しています。</td>
<td>sensor-space の位相・connectivity・topography を、参照依存性なしに読むことです。</td>
</tr>
<tr>
<td><strong>filter ゲート</strong></td>
<td>Widmann らは cutoff、transition band、filter order、causal / acausal が waveform と latency を歪めうることを整理しました。</td>
<td>ERP onset、slow component、high-frequency gain を、filter 設計を伏せたまま強く言うことです。</td>
</tr>
<tr>
<td><strong>artifact ゲート</strong></td>
<td>ICA、ICLabel、Autoreject、PREP などは有力ですが、2025 年の研究は artifact correction が decoding 精度を必ずしも上げないこと、むしろ confound を減らした結果として精度が下がりうることを示しました。</td>
<td>「最も高い精度を出した前処理が最良」と読むことです。</td>
</tr>
<tr>
<td><strong>保持率 / 高周波監査ゲート</strong></td>
<td>筋電は高 beta / gamma と重なり、さらに aggressive cleaning は neural signal も削りえます。したがって retained trials、補間率、除外率、raw-clean 差分を数値で残す必要があります。</td>
<td>高 beta / gamma の neural claim や、cleaning 後のデータだけで十分とすることです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="reporting-floor">
<h2 class="section-title">1. 報告の床はアルゴリズム名ではなく metadata です</h2>
<p>
EEG-BIDS とその公式仕様が先に固定するのは、派手な pipeline 名ではなく、<strong>何をどう測り、どの状態で保存したか</strong>でございます。`channels.tsv` には sampling frequency、low / high cutoff、notch、channel status を書けますし、`electrodes.tsv` と `coordsystem.json` は電極位置と座標系を固定します。COBIDAS-MEEG も同様に、参照法、フィルタ、bad channel 処理、除外規則、artifact handling の詳細報告を要求しています。ここから言えるのは単純で、<strong>metadata が無い clean EEG は再現可能成果物として扱えない</strong>ということです。
</p>
<div class="note-box">
<strong>このサイトでの rule</strong>
<p>
最低限、<strong>raw reference</strong>、<strong>rereference 後の方式</strong>、<strong>filters</strong>、<strong>bad channel / bad segment</strong>、<strong>電極座標</strong>、<strong>イベント時刻</strong>、<strong>除外規則</strong> を残してください。processed data だけを置く場合でも、raw から clean への差分が追えなければ受理しません。
</p>
</div>
</section>

<section class="section" id="reference-choice">
<h2 class="section-title">2. 参照法は小さな実装差ではなく、観測モデルの一部です</h2>
<p>
EEG は電位差計測なので、reference を変えると波形・topography・sensor-space connectivity は動きます。PREP pipeline が強調したのは、<strong>bad channel を見逃したまま平均参照を取ると rereference 自体が汚染される</strong>という点です。さらに、reference comparison 研究では functional connectivity graph や task-related network 指標が reference に依存して変化します。したがって本サイトでは、reference を「実装メモ」ではなく <strong>結果の意味を決める前提</strong>として扱います。
</p>
<table class="data-table">
<thead>
<tr>
<th>最低限書くこと</th>
<th>なぜ必要か</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>収録時 reference / ground</strong></td>
<td>raw の電位差の前提が変わるためです。</td>
</tr>
<tr>
<td><strong>rereference の方式</strong></td>
<td>average、linked mastoid、REST などで sensor-space 指標の意味が変わるためです。</td>
</tr>
<tr>
<td><strong>rereference 前の bad channel 処理</strong></td>
<td>壊れたチャンネルを混ぜると rereference 自体が汚染されるためです。</td>
</tr>
<tr>
<td><strong>補間したチャンネル数</strong></td>
<td>spatial pattern がどこまで実測でどこから補間かを区別するためです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="filter-design">
<h2 class="section-title">3. filter は「通した帯域」だけでなく、歪みの設計です</h2>
<p>
Widmann らが整理した通り、filter は cutoff 周波数だけを書けば済む話ではございません。transition band、filter order、passband / stopband ripple、causal / acausal、片方向 / 両方向適用で、latency と waveform は動きます。したがって、<strong>slow wave が見えた</strong>、<strong>onset が早まった</strong>、<strong>gamma が増えた</strong>といった主張は、filter design の記録なしには受理できません。
</p>
<div class="note-box">
<strong>このサイトでの rule</strong>
<p>
filter については、<strong>high-pass</strong>、<strong>low-pass</strong>、<strong>notch</strong> の cutoff だけでなく、<strong>filter type</strong>、<strong>order</strong>、<strong>causal / acausal</strong>、<strong>forward-backward の有無</strong> を残してください。ERP や latency を主張する場合は、少なくとも 1 つの代替設定で conclusion drift を点検します。
</p>
</div>
</section>

<section class="section" id="artifact-control">
<h2 class="section-title">4. artifact suppression は常に改善とは限りません</h2>
<p>
ICA、ICLabel、Autoreject、PREP などは有力な実務候補です。しかし、ここでの重要点は「どれを使ったか」ではなく、<strong>何を削り、何を残したかを監査できるか</strong>でございます。2025 年の decoding 研究は、artifact correction が分類性能を必ずしも上げず、むしろ artifact-related confounds を減らした結果として精度が下がりうることを示しました。これは cleaning が無意味という話ではなく、<strong>accuracy 最大化と neural specificity 最大化は同義ではない</strong>という意味です。
</p>
<table class="data-table">
<thead>
<tr>
<th>候補手法</th>
<th>役割</th>
<th>自動的に標準解へ昇格しない理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PREP</strong></td>
<td>line noise、bad channel、robust rereference の床を整えます。</td>
<td>課題特異的 artifact や signal preservation は別途監査が要るためです。</td>
</tr>
<tr>
<td><strong>Autoreject</strong></td>
<td>trial / sensor 単位のしきい値調整と補間を自動化します。</td>
<td>保持率と task-relevant signal がどう動いたかは別に確認が要るためです。</td>
</tr>
<tr>
<td><strong>ICA + ICLabel</strong></td>
<td>眼球、筋電、心電などの independent component を候補化します。</td>
<td>component 除去が neural 成分まで削る可能性があり、完全自動化は危険なためです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>このサイトでの rule</strong>
<p>
artifact 処理を報告するときは、<strong>使った手法名</strong>だけでは不十分です。<strong>除去した component / epoch / channel 数</strong>、<strong>補間率</strong>、<strong>保持した minutes / trials</strong>、<strong>raw-clean の主要指標差分</strong>、さらに可能なら <strong>代替 pipeline 1 本との比較</strong> を残してください。
</p>
</div>
</section>

<section class="section" id="high-frequency-caution">
<h2 class="section-title">5. 高 beta / gamma は筋電監査なしに強く書きません</h2>
<p>
Muthukumaraswamy が整理した通り、muscle artifact は 20-300 Hz 近辺に広く重なり、高 beta / gamma の神経成分と見分けにくい場合があります。したがって、額、顎、側頭筋の活動が入りやすい課題で <strong>high-frequency power 増加</strong> を主張するなら、少なくとも <strong>topography</strong>、<strong>EOG / EMG 補助チャネル</strong>、<strong>jaw / brow などの行動 confound</strong>、<strong>cleaning 前後の residual</strong> を点検してください。ここをやらずに gamma を neural gain と読むのは、本サイトでは止めます。
</p>
</section>

<section class="section" id="minimum-deliverables">
<h2 class="section-title">最低限の提出物</h2>
<table class="data-table">
<thead>
<tr>
<th>提出物</th>
<th>最低限ほしい内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>acquisition metadata</strong></td>
<td>reference、ground、sampling rate、line frequency、electrode coordinates、event timing です。</td>
</tr>
<tr>
<td><strong>bad channel / bad segment 台帳</strong></td>
<td>何をどの基準で bad と判定し、補間したかを残します。</td>
</tr>
<tr>
<td><strong>filter design report</strong></td>
<td>cutoff、order、type、causal / acausal、notch を残します。</td>
</tr>
<tr>
<td><strong>artifact model report</strong></td>
<td>PREP / ICA / ICLabel / Autoreject などの有無、除去数、しきい値、補間率を残します。</td>
</tr>
<tr>
<td><strong>raw-clean delta</strong></td>
<td>power spectrum、trial count、channel count、主要 feature の変化量を raw と clean で比較します。</td>
</tr>
<tr>
<td><strong>retention summary</strong></td>
<td>最終的に何分、何試行、何チャンネルが残ったかを数値で出します。</td>
</tr>
<tr>
<td><strong>sensitivity analysis</strong></td>
<td>少なくとも 1 本の代替 reference または artifact pipeline で結論 drift を点検します。</td>
</tr>
<tr>
<td><strong>high-frequency exception note</strong></td>
<td>beta / gamma を主張する場合は、EMG 監査をどう通したかを別記します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="misreadings">
<h2 class="section-title">この批判から止めるべき誤読</h2>
<table class="data-table">
<thead>
<tr>
<th>誤読</th>
<th>このサイトでの読み替え</th>
</tr>
</thead>
<tbody>
<tr>
<td>きれいな波形が出たので十分</td>
<td>metadata、保持率、raw-clean 差分がなければ十分ではありません。</td>
</tr>
<tr>
<td>最も高い decoding 精度を出した pipeline が最良</td>
<td>artifact confound を拾っている可能性があるので、specificity と感度分析を先に見ます。</td>
</tr>
<tr>
<td>average reference は無難なので書かなくてよい</td>
<td>reference は結果の前提なので、raw / rereference の両方を書きます。</td>
</tr>
<tr>
<td>filter は cutoff だけ書けば足りる</td>
<td>order、type、causal / acausal まで必要です。</td>
</tr>
<tr>
<td>高 beta / gamma の増加は neural だろう</td>
<td>筋電重なりが強いので、EMG 監査なしには強く書きません。</td>
</tr>
<tr>
<td>自動 pipeline を使ったので再現可能</td>
<td>自動化と再現可能性は別であり、入力、しきい値、除去量、保持率の公開が必要です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>BIDS Specification: Electroencephalography. <a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">official docs</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nature Neuroscience</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Bigdely-Shamlo N, Mullen T, Kothe C, Su K-M, Robbins KA. The PREP pipeline: standardized preprocessing for large-scale EEG analysis. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2015.06.014" target="_blank">doi:10.1016/j.jneumeth.2015.06.014</a></li>
<li>Widmann A, Schröger E, Maess B. Digital filter design for electrophysiological data: a practical approach. <em>Journal of Neuroscience Methods</em>. 2015. <a href="https://doi.org/10.1016/j.jneumeth.2014.08.002" target="_blank">doi:10.1016/j.jneumeth.2014.08.002</a></li>
<li>Muthukumaraswamy SD. High-frequency brain activity and muscle artifacts in MEG/EEG: a review and recommendations. <em>Frontiers in Human Neuroscience</em>. 2013. <a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">doi:10.3389/fnhum.2013.00138</a></li>
<li>Cao Y, et al. How Different EEG References Influence Sensor Level Functional Connectivity Graphs. <em>Frontiers in Neuroscience</em>. 2017. <a href="https://doi.org/10.3389/fnins.2017.00368" target="_blank">doi:10.3389/fnins.2017.00368</a></li>
<li>Jas M, Engemann DA, Bekhti Y, Raimondo F, Gramfort A. Autoreject: automated artifact rejection for MEG and EEG data. <em>NeuroImage</em>. 2017. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.030" target="_blank">doi:10.1016/j.neuroimage.2017.08.030</a></li>
<li>Pion-Tonachini L, Kreutz-Delgado K, Makeig S. ICLabel: An automated electroencephalographic independent component classifier, dataset, and website. <em>NeuroImage</em>. 2019. <a href="https://doi.org/10.1016/j.neuroimage.2019.05.026" target="_blank">doi:10.1016/j.neuroimage.2019.05.026</a></li>
<li>Kessler V, et al. How EEG preprocessing shapes decoding performance. <em>Communications Biology</em>. 2025. <a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">doi:10.1038/s42003-025-08464-3</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-basics.html">EEGの基本 →</a></li>
<li><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">不確実性・校正・棄権 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG 101 →</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>Reference</h4>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS EEG Specification</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">COBIDAS-MEEG</a></li>
<li><a href="https://doi.org/10.1016/j.jneumeth.2015.06.014" target="_blank">PREP Pipeline</a></li>
<li><a href="https://doi.org/10.1016/j.jneumeth.2014.08.002" target="_blank">Widmann et al. (2015)</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2013.00138" target="_blank">Muthukumaraswamy (2013)</a></li>
<li><a href="https://doi.org/10.3389/fnins.2017.00368" target="_blank">Reference and Connectivity</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2017.08.030" target="_blank">Autoreject</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2019.05.026" target="_blank">ICLabel</a></li>
<li><a href="https://doi.org/10.1038/s42003-025-08464-3" target="_blank">Kessler et al. (2025)</a></li>
</ul>
</div>
</aside>
</main>
