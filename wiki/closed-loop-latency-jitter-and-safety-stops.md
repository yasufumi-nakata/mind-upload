---
layout: default
title: "Wiki：閉ループ・遅延・ジッタ・安全停止"
description: "閉ループ評価で重要になる遅延、ジッタ、再較正、棄権、安全停止を、一次文献ベースで整理します。"
article_type: Wiki
subtitle: "オフライン精度が高くても、リアルタイムで安定とは限りません"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Learning guide"
audience: "L3 の閉ループ評価やリアルタイム運用の意味が曖昧な人"
reading_time: "12〜18分"
page_intro: "このページは、Mind-Upload の L3『閉ループ』で重要になる遅延、ジッタ、再較正、棄権、安全停止を、一次文献に沿って整理する wiki です。一般論ではなく、どの論文がどこまで online 運用を示したかに基づいて読みます。"
accuracy_note: "ここで固定するのは『何を測るべきか』であり、許容 ms 値そのものではありません。許容値は課題依存ですが、分布・停止条件・再較正ログを出す必要性は共通です。"
page_highlights:
  - "offline 精度、online throughput、長期安定性は別々に測る必要があります。"
  - "latency は平均値だけでなく P95/P99 や dropout を含めて記録する必要があります。"
  - "recalibration と safety stop を隠したまま L3 を主張してはなりません。"
known_points:
  - "出力が次の入力を変える系では、latency と jitter が性能そのものを変えます。"
  - "固定 decoder の性能は時間とともに落ちうるため、再較正頻度自体が重要な指標です。"
  - "棄権、hold-last-output、freeze、hard stop は別の役割です。"
unknown_points:
  - "どの課題で何 ms まで許容できるかは、対話、運動、刺激制御で異なります。"
  - "長期安定性に必要な decoder update 則の一般解はまだありません。"
  - "全脳WBE の L3 をどう operationalize するかは未解決です。"
wiki_links:
  - label: "Wiki: 反事実・介入・摂動の検証"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "なぜ causal evidence が online 指標よりさらに強いのかを補います。"
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "遅延、ジッタ、ドリフトの記録方法を補います。"
  - label: "Wiki: 不確実性・信頼区間・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "低信頼時に何もしない設計の考え方を補います。"
  - label: "Wiki: 更新・分岐・停止規則"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "停止規則やキルスイッチの運用語を補います。"
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
<h2>最短の区別</h2>
<p>
<strong>閉ループ</strong>では、出力が次の入力を変えます。したがって、<strong>平均精度</strong>だけでなく、<strong>遅延分布</strong>、<strong>ジッタ</strong>、<strong>dropout</strong>、<strong>再較正頻度</strong>、<strong>停止条件</strong>まで公開しないと、安定に動いたとは言えません。
</p>
</div>

<div class="note-box">
<strong>今回の再整理で直した点</strong>
<p>
旧版は「遅延」「ジッタ」「安全停止」の定義整理としては有用でしたが、一次文献に基づく実務指標が不足していました。本ページでは、speech neuroprosthesis、bidirectional BCI、adaptive DBS、長期 decoder 維持の文献から、<strong>何を記録しなければならないか</strong>を逆算します。
</p>
</div>

<section class="section" id="evidence">
<h2 class="section-title">一次文献が示す現実</h2>
<table class="data-table">
<thead>
<tr>
<th>論文</th>
<th>何を示したか</th>
<th>閉ループ評価にどう効くか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Littlejohn et al. (2025)</strong></td>
<td>brain-to-voice neuroprosthesis は 80 ms increment で音声を streaming し、自然な会話で数秒の遅延が破綻要因になると明示しました。</td>
<td>speech 系では平均 latency ではなく、会話可能性を壊す tail latency を見る必要があります。</td>
</tr>
<tr>
<td><strong>Wairagkar et al. (2025)</strong></td>
<td>raw neural activity から音声合成まで 10 ms 以内で回し、non-speech では silence を返しました。一方で fixed decoder は約 15 日で性能低下が見えました。</td>
<td>latency と abstention を実装しても、長期安定性と decoder drift は別途監査が必要だと分かります。</td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong></td>
<td>ICMS による tactile feedback を加えると、robotic arm control の trial time と grasp time が大きく改善しました。</td>
<td>feedback path の遅延や欠落は、単に「使い勝手」ではなく performance 本体を変えます。</td>
</tr>
<tr>
<td><strong>Wilson et al. (2025)</strong></td>
<td>頻回 recalibration が neural bypass の大きな障害であると示し、hidden Markov model による unsupervised recalibration を one-month closed loop と five-year offline data で評価しました。</td>
<td>再較正頻度そのものを、性能指標から切り離さず報告すべきだと分かります。</td>
</tr>
<tr>
<td><strong>Oehrn et al. (2024)</strong></td>
<td>chronic adaptive DBS と conventional DBS を blinded randomized block で比較し、各条件を少なくとも 1 か月、実生活環境で評価しました。</td>
<td>閉ループ controller を主張するなら、短いラボデモではなく longitudinal block comparison が必要です。</td>
</tr>
<tr>
<td><strong>Cascino et al. (2026)</strong></td>
<td>2026年2月25日公開の ADAPT-START 報告では、20 連続症例中 9 例が aDBS 候補となり、2025年7月時点で 5 例が chronic aDBS を継続していました。</td>
<td>deployability と programming burden も閉ループ系の現実であり、候補選定率そのものを隠してはいけません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="metrics">
<h2 class="section-title">L3 を主張するなら最低限ほしい指標</h2>
<table class="data-table">
<thead>
<tr>
<th>指標</th>
<th>何を残すか</th>
<th>なぜ必要か</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>end-to-end latency</strong></td>
<td>P50 / P95 / P99、試行数、どの区間を含めたか。</td>
<td>平均だけでは会話や制御を壊す tail latency が隠れるためです。</td>
</tr>
<tr>
<td><strong>jitter</strong></td>
<td>latency の分散、外れ値率、条件別の揺れ。</td>
<td>平均遅延が同じでも、揺れが大きいと制御が崩れます。</td>
</tr>
<tr>
<td><strong>dropout / missed updates</strong></td>
<td>フレーム落ち、無効更新、通信断の回数と持続時間。</td>
<td>online loop は連続性が切れた瞬間に性能が落ちるためです。</td>
</tr>
<tr>
<td><strong>recalibration burden</strong></td>
<td>何分・何試行ごとに再較正したか、手動か自動か。</td>
<td>「高性能」でも頻回再較正が必要なら、運用可能性は低いままです。</td>
</tr>
<tr>
<td><strong>abstention / hold-last-output</strong></td>
<td>何もしない率、直前出力保持率、発動条件。</td>
<td>低信頼時の挙動を隠すと、安全性も性能も正しく読めません。</td>
</tr>
<tr>
<td><strong>recovery time</strong></td>
<td>摂動後または同期失敗後に、何試行・何秒で戻ったか。</td>
<td>loop の安定性は平均成績だけでなく回復力で決まるためです。</td>
</tr>
<tr>
<td><strong>stimulation duty cycle</strong></td>
<td>刺激時間率、総刺激量、停止回数。</td>
<td>adaptive stimulation 系では efficacy と exposure を両方見る必要があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="stops">
<h2 class="section-title">棄権・保持・停止を混ぜない</h2>
<table class="data-table">
<thead>
<tr>
<th>仕組み</th>
<th>主目的</th>
<th>ログに残すもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>棄権</strong></td>
<td>低信頼時に新規出力を出さないためです。</td>
<td>信頼度閾値、棄権率、そのときの入力条件。</td>
</tr>
<tr>
<td><strong>hold-last-output</strong></td>
<td>一時的な欠損時に急変を避けるためです。</td>
<td>保持時間、保持中の性能劣化、解除条件。</td>
</tr>
<tr>
<td><strong>freeze / 再較正停止</strong></td>
<td>異常検出後に原因確認や再同期へ入るためです。</td>
<td>発動理由、所要時間、再開条件、再開後の回復時間。</td>
</tr>
<tr>
<td><strong>hard stop</strong></td>
<td>危険な挙動や上限超過を直ちに止めるためです。</td>
<td>停止トリガー、時刻、被害回避の根拠、手動介入の有無。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>重要な実務ルール</strong>
<p>
再較正や停止が多い系を、成功試行だけ切り出して「閉ループで安定」と書いてはなりません。停止そのものが性能指標です。
</p>
</div>
</section>

<section class="section" id="minimum-pack">
<h2 class="section-title">L3 最低提出物パック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>online 指標：</strong>end-to-end latency 分布、jitter、dropout、throughput。</li>
<li><strong>安定性指標：</strong>セッション内劣化、日跨ぎ劣化、再較正頻度、回復時間。</li>
<li><strong>安全指標：</strong>棄権率、hold-last-output 率、freeze 回数、hard stop 回数。</li>
<li><strong>比較設計：</strong>offline と online を分離し、conventional controller や no-feedback 条件と比較すること。</li>
<li><strong>公開ログ：</strong>失敗試行、異常時ログ、停止理由、除外理由を隠さず出すこと。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">L3 の主張を読むときの 4 問</h2>
<ol>
<li><strong>平均精度ではなく latency の分布が出ているか：</strong>P95/P99 を出していないなら、会話や制御の破綻が隠れます。</li>
<li><strong>recalibration burden が明示されているか：</strong>毎回人手で直しているなら、安定運用ではありません。</li>
<li><strong>停止・棄権が性能から除外されていないか：</strong>安全動作も loop の一部です。</li>
<li><strong>短時間デモを長期安定性へ飛躍させていないか：</strong>ここが最も多いすり替えです。</li>
</ol>
</section>

<section class="section" id="sources">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Moses DA, Metzger SL, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson GH, Bray N, Franken M, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. Nat Med. 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Dixon S, Oehrn C, Remple M, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. Nat Biomed Eng. 2026. <a href="https://doi.org/10.1038/s41551-025-01592-5" target="_blank">doi:10.1038/s41551-025-01592-5</a></li>
<li>Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson’s disease: ADAPT-START findings and programming principles. npj Parkinsons Dis. 2026. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
L3 の全体設計へ戻るなら <a href="../verification.html">検証基盤</a>、因果摂動の意味へ戻るなら <a href="counterfactual-and-perturbation-verification.html">Wiki: 反事実・介入・摂動の検証</a>、Roadmap の I1 / I8 へ戻るなら <a href="../tech_roadmap.html">技術ロードマップ</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="counterfactual-and-perturbation-verification.html">反事実・介入・摂動の検証 →</a></li>
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
