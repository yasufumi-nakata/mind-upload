---
layout: default
title: "Wiki：反事実・介入・摂動の検証"
description: "held-out 精度、オンライン操作、外部介入、反事実に近い摂動検証の差を、一次文献ベースで整理します。"
article_type: Wiki
subtitle: "高精度と、条件変更への正しい応答は別です"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Learning guide"
audience: "decode と emulate の差をもう一段ていねいに理解したい人、因果検証の入口で止まりやすい人"
reading_time: "12〜18分"
page_intro: "このページは、held-out 精度、online human-in-the-loop、外部介入、摂動複雑性の検証を、一次文献に沿って切り分ける wiki です。概念語だけでなく、どの論文が何を実際に変え、何をまだ示していないかを並べます。"
accuracy_note: "2026年3月時点の一次文献が強く支えているのは、局所サブシステムや課題限定の causal evidence です。全脳WBEの反事実同値が実証されたという意味ではありません。"
page_highlights:
  - "offline decode、online control、外部介入、長期閉ループは別々の壁です。"
  - "反事実を名乗るには、分岐条件、比較対象、失敗条件を事前固定する必要があります。"
  - "一次文献で強いのは局所系・課題限定の実証であり、全脳同値の証明ではありません。"
  - "L2 以上の介入・閉ループ結果では、Intervention Card で trigger・timing・control/sham・再較正負荷を固定します。"
known_points:
  - "高い held-out 精度だけでは、因果構造の一致は言えません。"
  - "双方向 feedback や state-dependent stimulation は causal evidence を強めますが、適用範囲は局所に限られやすいです。"
  - "閉ループ系では latency、recalibration、abstention のログが必須です。"
unknown_points:
  - "どの摂動セットを満たせば WBE の生成的同値に十分かは未解決です。"
  - "反事実分岐のどこまでを benchmark 化できるかは、理論と工学の両面で研究途中です。"
  - "全脳スケールで branch-equivalence を直接検証する公開基盤は、まだ存在しません。"
wiki_links:
  - label: "Wiki: Decode と Emulate"
    url: "/wiki/decode-vs-emulate.html"
    description: "まず翻訳と生成の違いへ戻りたい人向けです。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "推定モデルと因果モデルの違いを補います。"
  - label: "Wiki: 閉ループ・遅延・ジッタ・安全停止"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "因果検証を online 系で読むときの実務指標を補います。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "Benchmark、Registry、Model Card の役割を補います。"
recommended_pages:
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "FAQ"
    url: "/faq.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>最短の結論</h2>
<p>
高い held-out 精度は重要ですが、それだけでは「中の仕組みも同じ」とは言えません。2026年3月時点の一次文献が示しているのは、<strong>offline decode</strong>、<strong>online human-in-the-loop</strong>、<strong>外部介入</strong>、<strong>長期閉ループ</strong>が別々の壁である、ということです。
</p>
</div>

<div class="note-box">
<strong>今回の再整理で直した点</strong>
<p>
旧版は、介入・反事実・摂動を概念語として説明する比重が高く、どの論文がどの段階まで実証しているかが見えにくい構成でした。本ページでは、一次文献ごとに<strong>何を実際に変えたのか</strong>、<strong>何が改善したのか</strong>、<strong>まだ言えないことは何か</strong>を並べます。
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">まず因果証拠の強さを 5 段階で分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>実際に変えているもの</th>
<th>最低限ほしいログ</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. held-out decode</strong></td>
<td>学習していないデータで当たるかを見ます。</td>
<td>分割単位、リーク検査、校正誤差、不確実性です。</td>
<td>条件変更への応答や因果構造の一致はまだ言えません。</td>
</tr>
<tr>
<td><strong>2. online human-in-the-loop</strong></td>
<td>被験者が出力を見ながら、連続操作や会話を行います。</td>
<td>end-to-end latency、jitter、dropout、再較正イベントです。</td>
<td>online で動いても、まだ外部介入への一致までは言えません。</td>
</tr>
<tr>
<td><strong>3. 双方向 feedback / 局所介入</strong></td>
<td>触覚 feedback や刺激で、出力が次の入力を変える loop を作ります。</td>
<td>刺激タイミング、強度、アーチファクト窓、行動変化量です。</td>
<td>局所 causal gain は示せても、全脳の生成的同値は示しません。</td>
</tr>
<tr>
<td><strong>4. state-dependent intervention</strong></td>
<td>検出した状態に応じて刺激や制御を切り替えます。</td>
<td>状態推定誤差、刺激 duty cycle、停止条件、在宅運用ログです。</td>
<td>課題特異的 controller の有効性であり、state completeness は別問題です。</td>
</tr>
<tr>
<td><strong>5. perturbation-structure test</strong></td>
<td>複数条件の分岐と摂動応答構造まで比較します。</td>
<td>分岐条件、比較規則、失敗条件、反復可能な摂動セットです。</td>
<td>ここでも本人性や社会実装までは自動的には言えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="intervention-card">
<h2 class="section-title">比較可能性のために Intervention Card を付ける</h2>
<p>
2026年3月の再監査で残っていた弱点は、<strong>因果証拠の段階表はあっても、各研究が何をどの条件で実際に変えたかを同じ書式で比べるカードが無かった</strong>ことです。<a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> は millisecond-resolution の EEG-triggered TMS で、同じ rTMS でも trigger する brain state により結果が変わることを示しました。<a href="https://doi.org/10.1113/JP283986" target="_blank">Gordon et al. (2023)</a> は optimized sham を使わないと TMS 由来応答と sensory input 由来応答の切り分けが難しいことを示しました。<a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a> は adaptive DBS の comparator と blinded block を、<a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> は streaming speech の timing を、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> は long-term recalibration を、それぞれ主結果の中心へ置いています。したがって本サイトでは、因果・閉ループ結果を読むときに <a href="../verification.html#intervention-card">Verification の Intervention Card</a> を併記し、研究どうしを同じ軸で監査します。
</p>
<table class="data-table">
<thead>
<tr>
<th>Intervention Card の欄</th>
<th>なぜ要るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>target / comparator</strong></td>
<td>何を刺激・制御し、何と比較したかが見えないと、`adaptive` の意味が研究ごとに変わってしまいます。</td>
</tr>
<tr>
<td><strong>trigger / timing</strong></td>
<td>state-dependent claim は biomarker、threshold、latency、jitter がずれるだけで意味が変わります。</td>
</tr>
<tr>
<td><strong>control / sham / artifact</strong></td>
<td>刺激系では sensory confound と cleaning artifact を切り分けないと、因果証拠を過大評価しやすくなります。</td>
</tr>
<tr>
<td><strong>safety / stop rule</strong></td>
<td>実験室で一度動いたことと、停止条件つきで安全に運用できることは別です。</td>
</tr>
<tr>
<td><strong>stability / recalibration</strong></td>
<td>短時間の成功と、cross-day / home use をまたぐ持続性は別問題だからです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>このサイトでの最低運用ルール</strong>
<p>
Intervention Card が無い場合、本サイトでは結果を <strong>online demo</strong>、<strong>exploratory intervention</strong>、または <strong>limited subsystem evidence</strong> として扱います。とくに comparator、timing audit、recalibration burden のどれかが欠ける場合、state-dependent / deployable / longitudinal の読替えを止めます。
</p>
</div>
</section>

<section class="section" id="boundary-cases">
<h2 class="section-title">一次文献で見る境界事例</h2>
<table class="data-table">
<thead>
<tr>
<th>論文</th>
<th>実際にできたこと</th>
<th>このサイトでどう読むか</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Forenzo et al. (2024)</strong></td>
<td>非侵襲 EEG の連続追従課題を online で評価し、deep learning decoder の挙動を人間ループ内で比較しました。</td>
<td>offline 精度ではなく online 指標を出した点が重要です。non-invasive でも human-in-the-loop の壁は別にあると読めます。</td>
<td>これは continuous control の実証であり、反事実同値や全脳生成ではありません。</td>
</tr>
<tr>
<td><strong>Wairagkar et al. (2025)</strong></td>
<td>raw neural activity から音声合成までを 10 ms 以内で回し、non-speech 区間では silence を返す voice loop を示しました。</td>
<td>low latency と abstention の実装が、閉ループ評価の必須要素だと分かります。</td>
<td>固定 decoder は約 15 日で性能低下が見え、長期安定性は別課題です。</td>
</tr>
<tr>
<td><strong>Flesher et al. (2021)</strong></td>
<td>感覚皮質への ICMS 触覚 feedback を加えると、robotic arm control の trial time と grasp time が改善しました。</td>
<td>双方向 feedback が行動を変える、という causal evidence の典型例です。</td>
<td>感覚運動サブシステムの局所 loop であり、全脳WBEの十分条件ではありません。</td>
</tr>
<tr>
<td><strong>Oehrn et al. (2024)</strong></td>
<td>Parkinson 病で chronic adaptive DBS と conventional DBS を blinded randomized block で比較し、在宅環境を含む評価を行いました。</td>
<td>state-dependent intervention を主張するなら、実生活ブロック比較まで要ることが分かります。</td>
<td>症状制御の controller 実証であり、内部状態の完全再構成ではありません。</td>
</tr>
<tr>
<td><strong>Casali et al. (2013), Comolatti et al. (2019)</strong></td>
<td>TMS / intracranial stimulation への応答複雑性を定量化する手法を示しました。</td>
<td>摂動ベースの検証は実装可能ですが、刺激条件とアーチファクト処理を固定しないと比較できないと読めます。</td>
<td>単一指標だけで WBE の pass/fail を決める根拠にはまだなりません。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>通信系 BCI の高速化は、そのまま因果同値ではありません</strong>
<p>
Willett et al. (2023) と Littlejohn et al. (2025) は、speech neuroprosthesis が高速かつ streaming になりうることを示しました。しかし、ここで実証されたのは<strong>コミュニケーション・サブシステムの online decode / control</strong>であり、branch-equivalence や全脳WBEではありません。
</p>
</div>

<section class="section" id="counterfactual-label">
<h2 class="section-title">何を満たしたときに「反事実」と呼ぶか</h2>
<p>
このサイトでは、単に「条件を変えた」だけでは <strong>反事実</strong> と呼びません。少なくとも次の 4 条件を満たさない場合は、より弱い表現である <strong>介入応答テスト</strong> または <strong>摂動一般化テスト</strong> と呼びます。
</p>
<table class="data-table">
<thead>
<tr>
<th>条件</th>
<th>必要な理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>分岐変数が明示されている</strong></td>
<td>何を変えたのかが曖昧だと、別条件を比べたのか単なるノイズ差か区別できません。</td>
</tr>
<tr>
<td><strong>比較規則が事前登録されている</strong></td>
<td>あとから都合のよい分岐だけ選ぶと、反事実らしく見せられてしまいます。</td>
</tr>
<tr>
<td><strong>アーチファクト窓と安全条件が公開されている</strong></td>
<td>刺激後の信号変化が、神経応答なのか装置由来なのかを切り分ける必要があります。</td>
</tr>
<tr>
<td><strong>失敗条件が固定されている</strong></td>
<td>どこまでずれたら「同じ分岐を再現できていない」と判定するかを先に決める必要があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="logs">
<h2 class="section-title">最低限残したいログ</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>介入の定義：</strong>刺激部位、強度、タイミング、継続時間、試行条件。</li>
<li><strong>アーチファクト処理：</strong>刺激直後の除外窓、補間、masking、採用しなかった試行。</li>
<li><strong>online 指標：</strong>end-to-end latency の分布、dropout、再較正イベント、棄権率。</li>
<li><strong>効果量：</strong>平均改善だけでなく trial-level のばらつき、失敗例、回復時間。</li>
<li><strong>比較規則：</strong>どの条件を主比較にし、どの結果なら fail とみなすか。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">因果検証の論文を読むときの 5 問</h2>
<ol>
<li><strong>offline 精度ではなく online 指標が出ているか：</strong>human-in-the-loop の課題なら、offline だけでは足りません。</li>
<li><strong>何を実際に変えたのかが書かれているか：</strong>刺激、feedback、decoder 更新、課題条件を区別します。</li>
<li><strong>アーチファクト処理が明示されているか：</strong>特に刺激系はここが抜けると因果証拠が崩れます。</li>
<li><strong>再較正と棄権が隠れていないか：</strong>うまくいった試行だけで loop を語っていないかを見ます。</li>
<li><strong>局所サブシステムの実証を、全脳同値へ飛躍させていないか：</strong>ここが最重要です。</li>
</ol>
</section>

<section class="section" id="sources">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Forenzo D, Zhu H, Shanahan J, Lim J, He B. Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. PNAS Nexus. 2024. <a href="https://doi.org/10.1093/pnasnexus/pgae145" target="_blank">doi:10.1093/pnasnexus/pgae145</a></li>
<li>Willett FR, Kunz EM, Fan C, et al. A high-performance speech neuroprosthesis. Nature. 2023. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. Nat Neurosci. 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Moses DA, Metzger SL, et al. An instantaneous voice-synthesis neuroprosthesis. Nature. 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Flesher SN, Downey JE, Weiss JM, et al. A brain-computer interface that evokes tactile sensations improves robotic arm control. Science. 2021. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. Brain Stimul. 2018. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Gordon PC, Song YF, Jovellar DB, Rostami M, Belardinelli P, Ziemann U. Untangling TMS-EEG responses caused by TMS versus sensory input using optimized sham control and GABAergic challenge. J Physiol. 2023. <a href="https://doi.org/10.1113/JP283986" target="_blank">doi:10.1113/JP283986</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. Nat Med. 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Wilson GH, Bray N, Franken M, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. Nat Biomed Eng. 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Casali AG, Gosseries O, Rosanova M, et al. A theoretically based index of consciousness independent of sensory processing and behavior. Sci Transl Med. 2013. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti R, Pigorini A, Casarotto S, et al. A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. Brain Stimul. 2019. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
翻訳と生成の違いへ戻るなら <a href="../wbe_101.html">WBE入門</a>、検証設計へ戻るなら <a href="../verification.html">検証基盤</a>、閉ループ実務へ戻るなら <a href="closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="decode-vs-emulate.html">Decode と Emulate →</a></li>
<li><a href="observation-to-estimation.html">観測から推定へ →</a></li>
<li><a href="closed-loop-latency-jitter-and-safety-stops.html">閉ループ・遅延・ジッタ・安全停止 →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../wbe_101.html">WBE入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../faq.html">FAQ →</a></li>
</ul>
</div>
</aside>
</main>
