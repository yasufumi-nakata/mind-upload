---
layout: default
title: "Wiki：閉ループ・遅延・ジッタ・安全停止"
description: "閉ループ評価で重要になる遅延、ジッタ、ドリフト、安全停止を、ループ種別ごとの一次文献に沿って整理します。"
article_type: Wiki
subtitle: "閉ループの時間要件は 1 つの数値ではなく、ループ種別ごとに変わります"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Learning guide / evidence refresh"
audience: "L3 の閉ループ評価やリアルタイム運用を、一般論ではなく文献ベースで読みたい人"
reading_time: "12〜18分"
page_intro: "このページは、Mind-Upload の L3『閉ループ』で重要になる遅延、ジッタ、ドリフト、安全停止の違いを、一次文献に沿って整理する wiki です。オフライン精度が高いモデルでも、ループの帯域とアクチュエータの種類が違えば必要な timing budget も変わることを明確にするのが目的です。"
accuracy_note: "ここでは『全ループに共通の固定閾値』は置きません。課題、対象周波数、出力機構、安全要求に応じて、実測した end-to-end 指標で判断する前提で書いています。"
page_highlights:
  - "閉ループの時間要件は 1 つの ms 値ではなく、ループ種別ごとに変わります。"
  - "event marker が 1 ms 未満でも、系全体の end-to-end 保証とは別問題です。"
  - "phase-targeting では ms より位相誤差、adaptive DBS では burst 検出遅延と停止規則が重要です。"
known_points:
  - "オフライン精度と閉ループ安定性は別の主張であり、同じスコアでは監査できません。"
  - "遅延とジッタの許容範囲は、state feedback、ERP/command BCI、phase-locked stimulation、burst-driven neuromodulation で異なります。"
  - "入力、処理、出力、戻りを end-to-end で実測しないと、実運用の timing は分かりません。"
unknown_points:
  - "WBE に必要な閉ループ帯域が、どのループ種別にどこまで跨るかは未確定です。"
  - "phase-specific な制御で必要な精度を、非侵襲ヒト実験の全タスクへ一般化できるとはまだ言えません。"
  - "長期運用での drift と再較正頻度が、どの時点で『不安定』判定になるかは課題依存です。"
wiki_links:
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "遅延、ジッタ、ドリフトを何として残すかを補います。"
  - label: "Wiki: 不確実性・信頼区間・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "低信頼時に『出さない』設計の考え方を補います。"
  - label: "Wiki: 更新・分岐・停止規則"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "freeze と停止規則を運用としてどう切り分けるかを補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の補助ページへ戻れます。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い結論</h2>
<p>
<strong>閉ループ</strong>は「出力が次の入力を変える系」です。ただし、そこで要求される timing は 1 つではありません。<strong>alpha neurofeedback</strong>、<strong>P300/ERP BCI</strong>、<strong>phase-locked stimulation</strong>、<strong>adaptive DBS</strong> では、支配的な時間スケールが違います。したがって、<strong>共通の 1 ms 閾値</strong>や<strong>共通の 10 ms 閾値</strong>をサイト全体の正解として置くのは危険です。
</p>
</div>

<div class="note-box">
<strong>今回の整理で先に固定したこと</strong>
<p>
このページでは、「どれくらい速ければ十分か」を抽象論で語るのではなく、<strong>どのループ型を扱っているのか</strong>、<strong>そのループで何を壊す遅延なのか</strong>、<strong>何を hardware で実測したのか</strong>を先に固定します。event marker の高速化、LSL の同期、phase 追跡、停止規則は、それぞれ別の層の話です。
</p>
</div>

<section class="section" id="why-fixed-threshold-is-dangerous">
<h2 class="section-title">なぜ固定閾値が危険なのか</h2>
<p>
Wilson ら (2010) は、mu rhythm 振幅のような比較的ゆっくりした BCI 指標では、<strong>10 ms 程度の小さな遅れ</strong>が直ちに本質を壊すとは限らない一方、系全体の latency/jitter を測らないと出力経路や表示器が律速になることを示しました。逆に、Belinskaia ら (2020) は parietal alpha neurofeedback で、<strong>追加 250 ms / 500 ms 遅延</strong>が学習効果を悪化させることを示しました。さらに、Mansouri ら (2018) と Zrenner ら (2018) のような phase-targeting 系では、遅延は単なる ms 値ではなく、<strong>対象周波数に対する位相誤差</strong>として評価すべきです。
</p>
<div class="note-box">
<strong>読み方の原則</strong>
<p>
「低遅延が良い」は一般論として正しいですが、そこから直ちに「全ループで microsecond 級が必須」「全ループで 1 ms 以下が必須」とは言えません。正しい問いは、<strong>どのループ帯域で、どの誤差が、何を壊すのか</strong>です。
</p>
</div>
</section>

<section class="section" id="loop-classes">
<h2 class="section-title">まず 4 つのループ型に分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>ループ型</th>
<th>典型例</th>
<th>文献が示すこと</th>
<th>このサイトで先に残すべきログ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state feedback / neurofeedback</strong></td>
<td>alpha パワーを見て視覚フィードバックを返す系です。</td>
<td>Belinskaia ら (2020) は、追加 250 / 500 ms 遅延が alpha neurofeedback 学習を悪化させると示しました。短い遅延ほど学習に有利でした。</td>
<td>中央値/P95/P99 の feedback latency、表示経路、追加遅延に対する性能劣化曲線です。</td>
</tr>
<tr>
<td><strong>ERP / command BCI</strong></td>
<td>P300 speller や event-related control です。</td>
<td>Wilson ら (2010) は timing を分解して hardware 実測する必要を示し、Mowla ら (2017) は latency jitter が classification を下げるため、補正しても悪影響は完全には消えないと示しました。</td>
<td>block jitter、刺激 onset 実測、trial-to-trial latency variance、分類性能との対応です。</td>
</tr>
<tr>
<td><strong>phase-locked stimulation</strong></td>
<td>EEG 位相に合わせて TMS/tES を打つ系です。</td>
<td>Mansouri ら (2018) は位相遅れを theta/alpha で評価し、Zrenner ら (2018) は millisecond-resolution EEG-triggered TMS で brain state 依存性を実証しました。ここでは ms より位相誤差が中心です。</td>
<td>対象周波数、位相誤差分布、推定位相の信頼度、missed trigger、phase ずれ時の fallback 条件です。</td>
</tr>
<tr>
<td><strong>burst/state-triggered neuromodulation</strong></td>
<td>beta burst を使う adaptive DBS です。</td>
<td>Little ら (2013) は pathological beta を feedback に使う proof-of-principle を示し、Tinkhauser ら (2017) は adaptive DBS が <strong>100–600 ms</strong> の短い burst と <strong>600 ms 超</strong>の長い burst の分布を変えることを示しました。支配時間は phase-locking より遅いです。</td>
<td>biomarker 検出遅延、burst false positive/false negative、ramp-up/ramp-down、停止回数です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="end-to-end">
<h2 class="section-title">何を end-to-end で測るのか</h2>
<p>
Wilson ら (2010) の重要点は、<strong>signal processing latency だけを測っても不十分</strong>だということです。閉ループで効くのは、入力から出力までの全経路です。表示器、OS、ドライバ、音声系、刺激器が別の律速になることがあります。
</p>
<table class="data-table">
<thead>
<tr>
<th>区間</th>
<th>最低限知りたいこと</th>
<th>典型的な実測法</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力</strong></td>
<td>センサーが実際にいつ変化を取り込んだかです。</td>
<td>TTL、既知パルス、DAQ 入力、刺激器の marker 出力です。</td>
</tr>
<tr>
<td><strong>処理</strong></td>
<td>前処理、推定、意思決定にどれだけ時間がかかったかです。</td>
<td>software timestamp、block duration、CPU/GPU ログです。</td>
</tr>
<tr>
<td><strong>出力</strong></td>
<td>表示、音、刺激、制御信号がいつ本当に出たかです。</td>
<td>フォトダイオード、マイク、loopback、刺激アーチファクト onset です。</td>
</tr>
<tr>
<td><strong>戻り</strong></td>
<td>出力の影響がいつ次の入力へ返ってきたかです。</td>
<td>closed-loop task 内での再検出、環境センサー、身体応答ログです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>平均だけでは足りません</strong>
<p>
閉ループでは、平均遅延よりも <strong>P95/P99/worst-case</strong> や <strong>trial-to-trial jitter</strong> が壊しやすいことがあります。特に phase-targeting や safety-critical loop では、平均値だけ出しても安心材料になりません。
</p>
</div>
</section>

<section class="section" id="synchronization">
<h2 class="section-title">LSL と event marker は何を保証し、何を保証しないか</h2>
<p>
Kothe ら (2025) の LSL 論文は、LSL が <strong>millisecond-scale で十分な neurobehavioral research</strong> の同期に有用で、offset correction や jitter compensation を提供することを示しています。一方で、これは <strong>LAN 上の software-based synchronization</strong> の話であり、刺激器や表示器の物理出力がいつ起きたかを自動で保証するわけではありません。
</p>
<p>
Appelhoff と Stenner (2021) は、USB microcontroller による event marking が <strong>1 ms 未満の latency</strong> を出せることを示しました。ただし、これも主に <strong>marker path</strong> の精度です。marker が速くても、表示器、音声経路、刺激器、推定器まで含めた end-to-end loop が同じ精度とは限りません。
</p>
<div class="key-points">
<h4>ここで分けるべきこと</h4>
<ul>
<li><strong>LSL：</strong>複数 stream の共通時刻系と offset 補正を助けます。</li>
<li><strong>TTL / MCU marker：</strong>イベントを acquisition 側へ刻む精度を上げます。</li>
<li><strong>photodiode / microphone / loopback：</strong>実際の output onset を外部から検証します。</li>
<li><strong>phase 追跡器：</strong>対象周波数に対して、どれだけ位相ずれが残るかを別に監査します。</li>
</ul>
</div>
</section>

<section class="section" id="stops">
<h2 class="section-title">棄権と freeze と安全停止は別物です</h2>
<table class="data-table">
<thead>
<tr>
<th>仕組み</th>
<th>主目的</th>
<th>典型トリガー</th>
<th>最低限残すこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>棄権</strong></td>
<td>低信頼時に無理な出力を避けるためです。</td>
<td>分類確率不足、phase 推定信頼度不足、OOD 検出です。</td>
<td>棄権率、棄権時の信頼度閾値、棄権後の状態です。</td>
</tr>
<tr>
<td><strong>freeze / 一時停止</strong></td>
<td>再較正や原因確認のためです。</td>
<td>clock offset 増大、packet loss、drift 逸脱、再同期要求です。</td>
<td>発動理由、継続時間、再開条件、再較正内容です。</td>
</tr>
<tr>
<td><strong>安全停止 / containment</strong></td>
<td>危険な actuation を止めるためです。</td>
<td>P99 latency budget 超過、異常振幅、刺激禁止位相、出力飽和です。</td>
<td>停止条件、停止回数、直前の latency/phase/error、手動復帰条件です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>性能問題と安全問題を混ぜない</strong>
<p>
「うまく出せなかったので出さない」のか、「系が壊れていそうなので保留する」のか、「危険なので止める」のかは、運用上まったく別です。全部を 1 つの『停止』にまとめると、レビュー時に原因が追えなくなります。
</p>
</div>
</section>

<section class="section" id="logs">
<h2 class="section-title">最低限残したいログ</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>loop class：</strong>state feedback、ERP/command、phase-locked、burst-triggered のどれか。</li>
<li><strong>end-to-end latency：</strong>中央値、P95、P99、worst-case を別々に残します。</li>
<li><strong>jitter の定義：</strong>SD、IQR、peak-to-peak のどれかを明記します。</li>
<li><strong>clock offset / drift：</strong>LSL や hardware marker の補正前後を残します。</li>
<li><strong>marker 検証法：</strong>TTL、MCU、photodiode、microphone、loopback のどれで実測したかを書きます。</li>
<li><strong>phase/burst 系の追加指標：</strong>位相誤差分布、missed trigger、burst 検出遅延、false positive/negative です。</li>
<li><strong>棄権 / freeze / 安全停止：</strong>発動回数、直前状態、復帰条件を残します。</li>
<li><strong>性能劣化曲線：</strong>人工的に遅延を足したとき、どこで崩れるかを残します。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">L3 の主張を読むときの 4 問</h2>
<ol>
<li><strong>どの loop class を扱っているか書いてあるか：</strong> slow feedback と phase-locked を同じ表で語っていないかを見ます。</li>
<li><strong>end-to-end 実測があるか：</strong> software timestamp だけで済ませていないかを確認します。</li>
<li><strong>delay を位相誤差や burst 時間へ写像しているか：</strong> ただの ms 値で済ませていないかを見ます。</li>
<li><strong>棄権・freeze・安全停止が分離されているか：</strong> 危険時の運用が曖昧でないかを確認します。</li>
</ol>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. <em>IEEE Trans Biomed Eng.</em> 2010;57(7):1785-1797. <a href="https://doi.org/10.1109/TBME.2010.2047259" target="_blank">doi:10.1109/TBME.2010.2047259</a></li>
<li>Thompson DE, Warschausky SA, Huggins JE. Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. <em>J Neural Eng.</em> 2013;10(1):016006. <a href="https://doi.org/10.1088/1741-2560/10/1/016006" target="_blank">doi:10.1088/1741-2560/10/1/016006</a></li>
<li>Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. <em>Brain Comput Interfaces.</em> 2017;4(3):137-145. <a href="https://doi.org/10.1080/2326263X.2017.1338010" target="_blank">doi:10.1080/2326263X.2017.1338010</a></li>
<li>Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. <em>J Neural Eng.</em> 2020;17(6):066012. <a href="https://doi.org/10.1088/1741-2552/abc8d7" target="_blank">doi:10.1088/1741-2552/abc8d7</a></li>
<li>Mansouri F, Fettes P, Schulze L, et al. A Real-Time Phase-Locking System for Non-invasive Brain Stimulation. <em>Front Neurosci.</em> 2018;12:877. <a href="https://doi.org/10.3389/fnins.2018.00877" target="_blank">doi:10.3389/fnins.2018.00877</a></li>
<li>Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <em>Brain Stimul.</em> 2018;11(2):374-389. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. <em>Ann Neurol.</em> 2013;74(3):449-457. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <em>Brain.</em> 2017;140(4):1053-1067. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. <em>Behav Res Methods.</em> 2021;53(6):2450-2455. <a href="https://doi.org/10.3758/s13428-021-01571-z" target="_blank">doi:10.3758/s13428-021-01571-z</a></li>
<li>Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. <em>Imaging Neurosci.</em> 2025;3:IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
L3 の全体設計へ戻るなら <a href="../verification.html">検証基盤</a>、EEG と同期の実務へ戻るなら <a href="../eeg_101.html">EEG入門</a>、Roadmap の I1 / I8 へ戻るなら <a href="../tech_roadmap.html">技術ロードマップ</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">不確実性・信頼区間・棄権 →</a></li>
<li><a href="update-branching-and-stop-rules.html">更新・分岐・停止規則 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../tech_roadmap.html">技術ロードマップ →</a></li>
</ul>
</div>
</aside>
</main>
