---
layout: default
title: "Wiki：配線図だけでは足りない理由"
description: "WBE で connectome だけを保存しても足りない理由を、shared extracellular / electrical state、樹状突起統合状態を含む状態変数の欠落と connectome-constrained 推定の限界まで含めて一次文献から整理します。clearance / immune support も独立軸として扱います。"
article_type: Wiki
subtitle: "connectome-complete は emulation-complete ではありません"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Technical / natural science only"
audience: "配線図が取れたら WBE に近いのかを、技術と自然科学だけで判断したい人"
reading_time: "15〜20分"
page_intro: "このページは、『コネクトームが取れれば脳の再現に十分ではないか』という直感を、一次文献に基づいて分解するためのページです。哲学や法制度ではなく、どの状態変数が欠けると何が言えなくなるか、さらに connectome-constrained でもどの推定上の壁が残るかに絞って整理します。glial / metabolic support や clearance / immune support だけでなく、shared extracellular / electrical state と樹状突起の branch-specific な統合状態も独立に扱います。"
accuracy_note: "ここで示すのは『最低限これを外すと主張が弱くなる』という整理と、『配線制約を入れてもなお残る縮退』の整理であり、最終的な十分条件が確定したという意味ではありません。"
page_highlights:
  - "配線図だけでは落ちる論点を、9つの状態クラスと1つの推定上の壁に分けて整理します。"
  - "一次文献だけを使い、state variable の欠落と parameter degeneracy を切り分けます。"
  - "このサイトで connectome-complete と connectome-constrained model をどう読み替えるかの運用ルールも固定します。"
  - "列挙で終わらせず、connectome-only から何を足したときに predictive gain が読めるかを augmentation / ablation で固定します。"
  - "fly / mouse / human の証拠を混ぜたときの external validity ceiling も、本文で明示します。"
known_points:
  - "全脳 connectome の作成は大きく前進していますが、それだけで動的再現が完了したとは言えません。"
  - "シナプス効率、shared extracellular / electrical state、樹状突起の branch-specific 非線形統合、遅延、神経修飾、グリア、clearance / immune support、細胞型ラベル、内在興奮性 / 恒常性 set point は、静的な edge list からは落ちやすい情報です。"
  - "EM の synapse count、PSD 面積、same-brain connectomics は synaptic-state の prior を強くしえますが、その瞬間の effective weight や release state の直接読出しではありません。"
  - "粗い生理 proxy を ground truth と混同すると、内部状態の主張を過大化しやすくなります。"
  - "connectome-constrained なモデルでも、未測定の細胞・シナプス・修飾パラメータが残ると dynamics は縮退しえます。"
  - "same-brain function、transcriptomics、neuromodulatory dynamics、glial slow state を足すと条件付き予測は改善しえますが、その改善は課題・時定数・外部妥当化条件に依存します。"
  - "human での petavoxel 級 ultrastructure や MRSI-based metabolic connectome も重要な前進ですが、現時点では structural / biochemical scaffold の主張に留まります。"
unknown_points:
  - "どの状態クラスをどの解像度まで取れば WBE の十分条件に近づくかは未確定です。"
  - "欠落した状態変数をどこまで推定や coarse-graining で補えるかは、今後の検証課題です。"
  - "人で直接取得できない状態を、どの動物・侵襲系で較正すべきかはまだ固定されていません。"
  - "same-brain function を足したとき、どの程度まで縮退が解けるかもまだ系統的には定まっていません。"
  - "どの augmentation の順序が、どの誤差項をもっとも効率よく減らすかは、まだ dataset ごとに変わります。"
  - "human macro-biochemical scaffold が local transmitter / glial maintenance-state をどこまで拘束できるかも未確定です。"
wiki_links:
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "この論点の前提になる全体像を初歩から整理します。"
  - label: "Wiki: 恒常性可塑性と維持状態"
    url: "/wiki/homeostatic-plasticity-and-maintenance-state.html"
    description: "内在興奮性、sleep-homeostasis、髄鞘/代謝維持がなぜ別変数かを深掘りします。"
  - label: "Wiki: Decode と Emulate"
    url: "/wiki/decode-vs-emulate.html"
    description: "出力の翻訳と内部生成の違いを整理します。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "どこまでの証拠でどの強さの主張が許されるかを確認できます。"
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
<h2>結論</h2>
<p>
配線図は WBE の重要な土台ですが、<strong>それだけでは動的再現の下限要件になりません</strong>。同じ隣接関係でも、細胞型ラベル、内在興奮性、シナプス効率、shared extracellular / electrical state、樹状突起 branch の非線形統合、伝導遅延、神経修飾、グリア結合状態、clearance / immune support が違えば、学習、位相同期、局所計算、覚醒度依存の応答、長期安定性は大きく変わります。さらに、2024-2025 年の connectome-constrained modelling 研究は、<strong>配線制約を入れても未測定パラメータと省略機構のために dynamics の縮退が残る</strong>ことを示しました。したがって、このサイトでは <strong>connectome-complete を structural atlas / scaffold の達成</strong>として扱い、<strong>emulation-complete と言い換えません</strong>。同様に、<strong>connectome-constrained model が一部の活動を再現した</strong>ことも、そのまま state-complete reconstruction とは読みません。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。技術と自然科学の側面だけから、「何の状態変数が欠けると何が主張できなくなるか」と、「配線制約を入れても何がまだ一意に決まらないか」を整理します。
</p>
</div>

<section class="section" id="bottom-line">
<h2 class="section-title">先に固定する 9 つの状態クラスと 1 つの推定上の壁</h2>
<table class="data-table">
<thead>
<tr>
<th>状態クラス</th>
<th>配線図だけでは何が欠けるか</th>
<th>危険な誤読</th>
<th>現時点での扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>細胞型ラベル</strong></td>
<td>同じ隣接関係でも、転写型ごとに結合モチーフ、シナプス特性、髄鞘化の傾向が変わります。</td>
<td>unlabeled graph でも回路の物理的意味は同じだ、と読むことです。</td>
<td>same-brain transcriptomics / physiology と結んでいない限り、構造 atlas と候補 scaffold に留めます。</td>
</tr>
<tr>
<td><strong>内在興奮性・恒常性 set point</strong></td>
<td>同じ cell type と graph でも、ion channel expression、threshold、gain、発火率の目標値が違えば、同じ入力に対する応答と回復の仕方が変わります。</td>
<td>cell-type ラベルや短い活動一致があれば、長期ダイナミクスもほぼ決まる、と読むことです。</td>
<td>threshold / gain / recovery / homeostatic controller を測っていない限り、長期安定性や記憶配分の主張は latent state 付きに留めます。</td>
</tr>
<tr>
<td><strong>シナプス効率・短期状態</strong></td>
<td>edge の有無だけでは重み、放出確率、短期可塑性、LTP/LTD の履歴を決められません。</td>
<td>edge count や synapse count を、そのまま effective weight と読むことです。</td>
<td>静的配線の記述までは可能ですが、L2 の介入予測や L3 の閉ループ安定性は主張しません。</td>
</tr>
<tr>
<td><strong>shared extracellular / electrical state</strong></td>
<td>chemical synapse の wiring だけでは、gap junction の結合、endogenous electric field、interstitial ion / chloride state が固定されず、同じ graph でも inhibition の効き方、同期、state switching が変わります。</td>
<td>chemical connectome と cell type が分かれば、electrical coupling と inhibitory gain もほぼ固定された、と読むことです。</td>
<td>local ion / field / gap-junction state を測っていない限り、phase locking、inhibition sign / gain、state-transition threshold、plasticity gate の強い主張は latent state 付きに留めます。</td>
</tr>
<tr>
<td><strong>樹状突起統合状態</strong></td>
<td>同じ synapse set と somatic spike rule でも、branch-specific NMDA spike / plateau / dendritic sodium-calcium spike threshold、局所入力クラスタリング、compartmentalization が違えば、1 個のニューロンが実装する関数が変わります。</td>
<td>cell type、形態、平均発火率が分かれば、single-neuron transfer function もほぼ固定された、と読むことです。</td>
<td>dendritic recording / imaging / branch-specific perturbation が無い限り、point-neuron 化は近似として明示し、subcellular credit assignment や clustered-input causal claim は latent state 付きに留めます。</td>
</tr>
<tr>
<td><strong>遅延・髄鞘</strong></td>
<td>同じグラフでも伝導速度が違えば、位相、同期、抑制の到達タイミングが変わります。</td>
<td>同じ graph なら timing もほぼ同じだ、と読むことです。</td>
<td>時間整合性、位相同期、閉ループ制御の主張は降格し、delay uncertainty を残します。</td>
</tr>
<tr>
<td><strong>神経修飾場</strong></td>
<td>覚醒度、学習率、利得調整は静的 wiring だけでは復元できず、瞳孔径や HRV は粗い proxy にとどまります。</td>
<td>pupil / HRV や global arousal を、単一の transmitter ground truth と読むことです。</td>
<td>人データでは共変量や層別化に使えますが、トランスミッタ特異的・領域特異的 ground truth とは書きません。</td>
</tr>
<tr>
<td><strong>グリア・代謝結合状態</strong></td>
<td>アストロサイト等は可塑性や記憶想起に因果的に関与し、単なる支持組織ではありません。</td>
<td>glia は support tissue なので後回しにできる、と読むことです。</td>
<td>長期可塑性や slow state を含む主張は弱め、何を捨てた近似かを適用範囲として明記します。</td>
</tr>
<tr>
<td><strong>clearance / immune support</strong></td>
<td>meningeal lymphatic drainage、CSF-interstitial exchange、microglia-mediated surveillance が multiday support-state を支えます。</td>
<td>clearance は passive housekeeping なので neural fit と独立だ、と読むことです。</td>
<td>human proxy は support-state proxy に留め、multiday recovery や protein-clearance を含む主張は限定つきにします。</td>
</tr>
<tr>
<td><strong>パラメータ縮退（推定上の壁）</strong></td>
<td>同じ connectome や似た出力を満たすモデルでも、細胞・シナプスの未知パラメータが違えば内部 dynamics は複数ありえます。</td>
<td>connectome-constrained なら内部状態もほぼ一意だ、と読むことです。</td>
<td>family comparison、不確実性、held-out perturbation、abstention を伴わない限り、唯一解に近いとは書きません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>今回追加した不足変数</strong>
<p>
2026-03-17 の追加再監査では、従来の整理に加えて <strong>shared extracellular / electrical state</strong>、<strong>樹状突起統合状態</strong>、<strong>内在興奮性・恒常性 set point</strong>、<strong>clearance / immune support</strong> を独立クラスとして固定しました。理由は、cell-type ラベルや connectome を持っていても、gap junction / endogenous field / ion-state、branch-specific な非線形入力統合、threshold、gain、発火率の戻り先、CSF / glymphatic support、microglia-mediated surveillance が違えば、局所計算、長期予測、multiday recovery がまだ定まらないためです。一次文献のまとまった整理は <a href="homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> に分けております。
</p>
</div>
</section>

<section class="section" id="timescale-matrix">
<h2 class="section-title">2026-03 追補：hidden state を同じ 1 行に潰さない</h2>
<p>
今回さらに深掘りして見えた弱点は、connectome の外に残る state variable を 1 本の欠測リストとして並べると、<strong>ミリ秒スケールの実行状態</strong>、<strong>時間から日スケールの controller state</strong>、<strong>日から週スケールの maintenance state</strong> が混ざってしまう点でございました。一次文献が比較的一貫して示すのは、<strong>欠けた state class ごとに止まる主張が違う</strong>ということであり、same-day の fit から cross-day stability や long-term memory maintenance へ一足飛びには上げられません。
</p>
<table class="data-table">
<thead>
<tr>
<th>state class</th>
<th>主に止まる時間スケール</th>
<th>一次文献が直接支えること</th>
<th>human での直接性</th>
<th>欠けたときに止める主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>fast execution state</strong><br>current synaptic efficacy / release state / short-term plasticity</td>
<td>ms〜分</td>
<td><a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">Holler et al. (2021)</a>、<a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">Dürst et al. (2022)</a>、<a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">Alle et al. (2024)</a> は、ultrastructure や release-probability parameter が average potency の制約を強めても、その瞬間の release state や transmission reliability までは固定しないことを示します。</td>
<td>human では主として局所 ex vivo / 断片レベルであり、whole-brain in vivo の current state を直接は与えません。</td>
<td>phase-sensitive な介入予測、precise timing、closed-loop stability を強くは主張しません。</td>
</tr>
<tr>
<td><strong>shared extracellular / electrical state</strong><br>gap junction / ephaptic field / interstitial ion &amp; chloride state</td>
<td>ms〜時間</td>
<td><a href="https://doi.org/10.1038/99496" target="_blank">Galarreta &amp; Hestrin (1999)</a> は neocortical fast-spiking interneuron 間の electrical coupling を、<a href="https://doi.org/10.1038/nn.2727" target="_blank">Anastassiou et al. (2011)</a> は endogenous electric field が spike timing を動かしうることを、<a href="https://doi.org/10.1126/science.aaf3736" target="_blank">Ding et al. (2016)</a> は interstitial ion composition の操作だけで sleep-wake transition を切り替えうることを、<a href="https://doi.org/10.1016/j.neuron.2023.07.013" target="_blank">Burman et al. (2023)</a> は active cortical network が in vivo で fast inhibition を shunting mode へ動かすことを、<a href="https://doi.org/10.1016/j.cub.2025.01.050" target="_blank">Alfonsa et al. (2025)</a> は sleep-wake-related な intracellular chloride 変化が cortical plasticity を左右することを示しました。</td>
<td>human では local ion composition、E<sub>GABA</sub>、ephaptic microfield の routine direct readout はほぼ無く、侵襲局所計測か coarse proxy に限られます。</td>
<td>inhibition sign / gain、fast synchrony、state-switch threshold、plasticity gate を fixed parameter としては主張しません。</td>
</tr>
<tr>
<td><strong>branch-specific integration state</strong><br>dendritic spikes / plateau / local nonlinear subunits</td>
<td>ms〜時間</td>
<td><a href="https://doi.org/10.1038/35005094" target="_blank">Schiller et al. (2000)</a>、<a href="https://doi.org/10.1038/nn1253" target="_blank">Polsky et al. (2004)</a>、<a href="https://doi.org/10.1038/nature12600" target="_blank">Smith et al. (2013)</a>、<a href="https://doi.org/10.1038/nature14251" target="_blank">Cichon &amp; Gan (2015)</a>、<a href="https://doi.org/10.1126/science.aah6066" target="_blank">Takahashi et al. (2016)</a>、<a href="https://doi.org/10.1038/s41593-025-01876-8" target="_blank">Sehgal et al. (2025)</a> は、樹状突起 branch が input summation の受け皿ではなく、感覚選択性・学習・文脈リンクを左右する非線形 subunit だと示します。</td>
<td>human では <a href="https://doi.org/10.1016/j.cell.2018.08.045" target="_blank">Beaulieu-Laroche et al. (2018)</a> と <a href="https://doi.org/10.1126/science.aax6239" target="_blank">Gidon et al. (2020)</a> の ex vivo L2/3 evidence が中心で、whole-brain in vivo の branch-state direct readout はまだありません。</td>
<td>clustered-input computation、subcellular credit assignment、single-neuron transfer-function equivalence を soma-only fit からは主張しません。</td>
</tr>
<tr>
<td><strong>controller state</strong><br>intrinsic excitability / AIS / homeostatic set point</td>
<td>時間〜日</td>
<td><a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a>、<a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a>、<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>、<a href="https://doi.org/10.1038/nature09160" target="_blank">Grubb &amp; Burrone (2010)</a>、<a href="https://doi.org/10.1038/s41467-020-20232-x" target="_blank">Jamann et al. (2021)</a> は、cell type と graph だけでは threshold / gain / recovery の戻り先が定まらないことを示します。</td>
<td>human では perturbation 由来の coarse proxy が中心で、cell-specific な AIS / channel state の routine direct readout はまだありません。</td>
<td>cross-day generalization、memory allocation、perturbation 後の回復一致をそのままは主張しません。</td>
</tr>
<tr>
<td><strong>sleep-homeostatic renormalization</strong></td>
<td>overnight〜日</td>
<td><a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>、<a href="https://doi.org/10.1126/science.aah5982" target="_blank">de Vivo et al. (2017)</a>、<a href="https://doi.org/10.1126/science.aai8355" target="_blank">Diering et al. (2017)</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a>、<a href="https://doi.org/10.1016/j.cub.2024.07.032" target="_blank">Koukaroudi et al. (2024)</a> は、sleep が rate、synapse、network regime を再正規化することを示します。</td>
<td>human での direct readout はまだ粗く、sleep annotation と indirect proxy が中心です。</td>
<td>same-day の decode / fit を、そのまま overnight maintenance や multiday stability へ延長しません。</td>
</tr>
<tr>
<td><strong>timing-support state</strong><br>delay / myelin / oligodendroglial support</td>
<td>ms〜週</td>
<td><a href="https://doi.org/10.1126/science.1252304" target="_blank">Gibson et al. (2014)</a>、<a href="https://doi.org/10.1126/science.1254960" target="_blank">McKenzie et al. (2014)</a>、<a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">Micheva et al. (2021)</a>、<a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> は、myelination と oligodendrocyte-axon coupling が timing と support を左右することを示します。</td>
<td>human では local conduction / support state の direct routine readout は乏しく、構造 proxy が中心です。</td>
<td>delay-sensitive claim、phase coordination、long-term axonal support の一致は降格します。</td>
</tr>
<tr>
<td><strong>neuromodulatory context</strong></td>
<td>秒〜分</td>
<td><a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> と <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> は、pupil / behavior が役に立つ一方で、local transmitter state を一意には与えないことを示します。</td>
<td>human では pupil / HRV / behavior が主で、transmitter-specific・region-specific directness はまだ限定的です。</td>
<td>単一 transmitter mechanism、region-specific gain control、learning-rate control を直接は主張しません。</td>
</tr>
<tr>
<td><strong>slow maintenance state</strong><br>glial / metabolic ensemble</td>
<td>分〜日</td>
<td><a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">Suzuki et al. (2011)</a> と <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> は rodent の記憶・局所回路で astrocyte-metabolic support の因果性と機序を強めました。一方 <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> は human で 5 代謝物の parcel-level covariance を示したのであり、cell-specific astrocyte ensemble の direct readout ではありません。</td>
<td>human では parcel-level biochemical organization までが主で、cell-specific astrocyte ensemble の direct readout ではありません。</td>
<td>memory stabilization、slow-state、metabolic maintenance の一致を neuron-only success へ還元しません。</td>
</tr>
<tr>
<td><strong>clearance / immune support</strong><br>meningeal lymphatic / CSF / microglia axis</td>
<td>時間〜日</td>
<td><a href="https://doi.org/10.1038/nature14432" target="_blank">Louveau et al. (2015)</a> と <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> は lymphatic / microglia 軸の存在と局所 synaptic physiology への関与を強めました。human 側の <a href="https://doi.org/10.1093/brain/awab285" target="_blank">Eide &amp; Ringstad (2021)</a>、<a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">Hirschler et al. (2025)</a>、<a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> は macro support-state proxy を前進させましたが、特に Dagum らは investigational device と compartment model を含むため、現時点では provisional human evidence として読みます。</td>
<td>human では CSF mobility や glymphatic clearance の macro proxy が中心で、cell-specific immune controller の direct readout ではありません。</td>
<td>multiday recovery、protein-clearance、slow support-state を momentary neural completeness へ読み替えません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 文献監査で直した点</strong>
<p>
今回の監査では、<strong>Lucchetti et al. (2025)</strong> を glial causal evidence から外し、<strong>5 代謝物（tCr / tNAA / Glx / Ins / Cho）の parcel-level covariance</strong> に基づく human macro-biochemical scaffold として位置づけ直しました。また、<strong>Hirschler et al. (2025)</strong> は CSF mobility の 7T MRI technical report、<strong>Dagum et al. (2026)</strong> は investigational device と compartment model を含む biomarker transport study であるため、いずれも <strong>human support-state proxy</strong> として扱います。加えて、<strong>Dürst</strong> と <strong>Alle</strong> の DOI / 年次の整合性を修正し、synapse ultrastructure と momentary synaptic state の差をより厳密に書き分けました。
</p>
</div>
<div class="note-box">
<strong>この行列で何を直したか</strong>
<p>
今回の修正では、<strong>fast execution state</strong>、<strong>shared extracellular / electrical state</strong>、<strong>branch-specific integration state</strong>、<strong>controller state</strong>、<strong>slow maintenance state</strong>、<strong>clearance / immune support</strong> を本文で明示的に分けました。これにより、同じ「hidden state が残る」という一文でも、<strong>何が momentary release を止めるのか</strong>、<strong>何が inhibition sign / gain と state switching を止めるのか</strong>、<strong>何が single-neuron transfer function を止めるのか</strong>、<strong>何が cross-day claim を止めるのか</strong>、<strong>何が long-term stabilization を止めるのか</strong>、<strong>何が multiday support-state を止めるのか</strong>を別々に読めます。今後このサイトでは、これらを 1 行の latent state 欄に潰さず、timescale ごとの claim ceiling と一緒に出します。
</p>
</div>
</section>

<section class="section" id="connectome-progress">
<h2 class="section-title">配線図研究は大きく進んだが、それ自体は終点ではない</h2>
<p>
Dorkenwald らは成体ショウジョウバエ全脳の wiring diagram を示し、約 13 万ニューロン規模で全脳 connectome を提示しました。一方で MICrONS Consortium は、マウス視覚皮質の立方ミリメートル規模で、同一個体の機能計測と connectomics を結びつけるデータセットと局所 functional digital twin を公開しました。さらに Lappalainen らは、ショウジョウバエ視覚系で connectome-constrained network を task-optimized に学習させ、広い範囲の活動予測を可能にしました。human 側でも、Shapson-Coe らは petavoxel 級のヒト大脳皮質断片を nanoscale で再構成し、Lucchetti らは 3D whole-brain <sup>1</sup>H-MRSI から 5 代謝物の parcel-level covariance に基づく human metabolic connectome を提示しました。これは非常に大きな前進ですが、逆に言えば、<strong>現在ようやく「配線＋一部機能＋一部 biochemical scaffold＋追加仮定」を結び始めた段階</strong>であり、全脳・全状態の動的再現とはまだ別問題であることも示しています。
</p>
<div class="note-box">
<strong>ここでの読み替え</strong>
<p>
connectome-complete は「何がつながっているか」がかなり分かったという意味では重要です。しかし、それだけでは「どの強さで」「どの遅延で」「どの neuromodulatory context で」「どの glial coupling の下で」動くかまでは固定されません。human metabolic connectome も、parcel-level の biochemical organization を前進させますが、current synaptic efficacy、local transmitter specificity、astrocyte ensemble、sleep-history を直接は与えません。さらに Lappalainen らの reductionist model でも、著者自身が electrical synapses、nonlinear chemical synapses、neuromodulation を説明外に置いています。したがって、本サイトでは connectome-complete を <strong>structural atlas / scaffold</strong> の達成として扱い、L2/L3 の emulation claim へは自動的に昇格させません。<strong>connectome-constrained による activity prediction</strong> も、まずは hypothesis engine と conditional model として読みます。
</p>
</div>
</section>

<section class="section" id="transfer-ceiling">
<h2 class="section-title">2026-03 追補：species / scale / measurement stack の transfer ceiling を明示する</h2>
<p>
現行サイトの弱点は、fly、mouse、human の前進を同じ「connectome progress」として並べたときに、<strong>どこまで human whole-brain claim へ持ち込めるか</strong>の上限を本文で十分に固定していなかった点でした。一次文献はむしろ、<strong>種差</strong>、<strong>観測スケール</strong>、<strong>measurement stack</strong> の違いを無視すると主張が膨らみすぎることを示しています。Loomba らは、human cortex が mouse と同じ inhibitory microcircuit を単純拡大したものではなく、interneuron-to-interneuron network の拡張を持つことを示しました。したがって、「mouse で見えた局所対応」と「human whole-brain で何が言えるか」は、同じ connectomics でも別段階として扱う必要があります。
</p>
<table class="data-table">
<thead>
<tr>
<th>一次文献の前進</th>
<th>直接強くなったこと</th>
<th>そのままでは言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>fly whole-brain connectome / model</strong><br>Dorkenwald ら、Lappalainen ら</td>
<td>全脳 structural completeness と、fly visual system での task-conditioned activity prediction が前進しました。</td>
<td>mammalian cortical cell-type heterogeneity、human microcircuit 特異性、glial / metabolic maintenance-state を自動補完できません。</td>
</tr>
<tr>
<td><strong>mouse same-brain local twin</strong><br>MICrONS、Gamlin ら</td>
<td>same-brain structure-function link と、transcriptomic node label の増分価値が局所皮質で強くなりました。</td>
<td>mouse local cortex の成功を、そのまま human whole-brain の十分条件や全状態一般化へは上げられません。</td>
</tr>
<tr>
<td><strong>human nanoscale ultrastructure</strong><br>Shapson-Coe ら</td>
<td>human cortex でも nanoscale ultrastructure を petavoxel 断片で直接再構成できることが示され、human structural scaffold は大きく前進しました。</td>
<td>断片データであり、whole-brain connectome、current synaptic efficacy、neuromodulatory context、sleep-dependent maintenance-state はまだ直接与えません。</td>
</tr>
<tr>
<td><strong>human metabolic connectome</strong><br>Lucchetti ら</td>
<td>whole-brain <sup>1</sup>H-MRSI から、再現性のある parcel-level biochemical organization を human で描けるようになりました。</td>
<td>Glx / Ins / Cho / tCr / tNAA の parcel-level similarity は、cell-specific transmitter state、astrocyte ensemble、synaptic weight、local recovery controller の ground truth ではありません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>この追補で明確にした批判点</strong>
<p>
したがって、本サイトでは今後、<strong>「human でも EM が取れた」</strong>を<strong>whole-brain state-complete</strong>と読み替えず、<strong>「human で metabolic connectome が描けた」</strong>を<strong>local glial / transmitter state の直接観測</strong>と読み替えません。逆に、これらは human 側で何が見え始めたかを示す重要な前進であり、<strong>structural scaffold</strong> と <strong>macro-biochemical scaffold</strong> を分けて積み上げる方が、一次文献に整合的でございます。
</p>
</div>
</section>

<section class="section" id="degeneracy">
<h2 class="section-title">見落としやすい第0の問題：配線が分かっても dynamics はまだ縮退します</h2>
<p>
このページの旧版は、主として「何の状態変数が edge list から落ちるか」を説明していました。しかし、2025 年の Beiran と Litwin-Kumar の理論研究が示したのは、<strong>connectome が与えられても、未測定の細胞・シナプス特性が残ると recurrent dynamics はしばしば大きく縮退する</strong>という点です。学生モデルと教師モデルが同じ synaptic weights を共有していても、biophysical parameter が違えば、未観測ニューロンの dynamics は大きくずれうります。つまり、missing variable は「あとで足せばよい補助情報」ではなく、<strong>どこまで一意に推定できるかを決める本体</strong>でございます。
</p>
<div class="note-box">
<strong>この批判が意味すること</strong>
<p>
配線図があるだけでは、内部状態の唯一解はまだ遠いです。same-brain function や perturbation を足すと縮退は減りますが、それでも残った family を公開しない限り、「この内部状態が正しい」とは書けません。したがって、本サイトでは <strong>graph がある</strong>、<strong>activity が一部当たる</strong>、<strong>内部状態が一意に近い</strong>を別の主張として扱います。
</p>
</div>
</section>

<section class="section" id="state-classes">
<h2 class="section-title">なぜこれらの hidden state が抜けやすいのか</h2>

<h3>1. 細胞型ラベルは node ID の飾りではありません</h3>
<p>
Gamlin らは、マウス視覚皮質で予測された Sst transcriptomic types ごとに、接続モチーフ、シナプス特性、髄鞘化が系統的に異なることを示しました。さらに MICrONS Consortium は、哺乳類皮質では cell type の内部にも異なる tuning preference をもつニューロンが含まれうるため、same-brain connectivity と same-brain function を結んで読む必要があることを強調しました。つまり、<strong>同じグラフ構造でも node label と same-brain physiology が違えば回路の物理的意味が変わる</strong>ということです。cell type を落とした unlabeled graph は、圧縮としては便利でも、機能再現の前提情報をかなり失います。
</p>

<h3>2. 内在興奮性と恒常性 set point は node label の副産物ではありません</h3>
<p>
<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> は、同じ transcriptomic type の内部でも morpho-electric phenotype が連続的に広がることを示しました。さらに <a href="https://doi.org/10.1038/nn1639" target="_blank">Schulz et al. (2006)</a> は、同定済みニューロンでも ion channel mRNA と電流量に大きな個体差があることを示し、<a href="https://doi.org/10.1016/j.neuron.2014.04.002" target="_blank">O'Leary et al. (2014)</a> は activity-dependent な channel expression が activity set point を生みうることをモデル化しました。さらに <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a> は in vivo で単一ニューロンごとの firing-rate set point が存在することを示しています。つまり、<strong>cell-type ラベルと graph が分かっていても、threshold、gain、rebound、perturbation 後の戻り先はまだ latent state として残りえます</strong>。
</p>

<h3>3. シナプスは binary edge ではありません</h3>
<p>
Holler らは、同定した新皮質錐体細胞間シナプスで <strong>PSD 面積と平均 EPSP</strong> の関係を前進させましたが、同じ研究で <strong>trial-to-trial の size-strength 対応は弱く</strong>、multivesicular release も残ることを示しました。つまり、EM の ultrastructure は mean strength の prior を強くしえても、その瞬間の有効重みをそのまま与えるわけではございません。さらに Dürst らは、個々の bouton の potency が主として <strong>vesicular release probability</strong> に依存し、releasable vesicle number の寄与は高 <em>p</em><sub>ves</sub> 条件で強くなることを示しました。Matsuzaki らは単一 dendritic spine における LTP 誘導で、spine enlargement と AMPA 電流増加が結びつくことを示し、Vardalaki らは成体新皮質でもおよそ 25% の filopodia が AMPA 受容体を欠く silent synapse の構造基盤になりうることを示しました。したがって、<strong>edge list、synapse count、PSD / spine size だけでは current state の weight も release state も plastic history も、そもそも機能的に active かどうかも落ちます</strong>。
</p>
<div class="note-box">
<strong>今回固定する読み替え</strong>
<p>
このサイトでは今後、<strong>EM のシナプス数</strong>、<strong>PSD 面積</strong>、<strong>spine size</strong>、<strong>same-brain connectomics</strong> を、まず <strong>structural prior / state-averaged constraint</strong> として読みます。<a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">Alle et al. (2024)</a> は human neocortical tissue で、sleep-like な membrane state sequence が unitary synapse の transmission と consolidation を短時間で動かすことを示しました。したがって、paired physiology、presynaptic-state manipulation、held-out perturbation が無い限り、本サイトではそれらを <strong>current effective weight の直接読出し</strong>とは書きません。
</p>
</div>

<h3>4. shared extracellular / electrical state は edge list の外にあります</h3>
<p>
current connectomics の強みは chemical synapse の構造制約を押し上げることですが、<strong>それだけでは gap junction、endogenous electric field、interstitial ion / chloride state は固定されません</strong>。<a href="https://doi.org/10.1038/99496" target="_blank">Galarreta &amp; Hestrin (1999)</a> は neocortex の fast-spiking interneuron が electrical synapse で結ばれた network を作ることを示しました。さらに <a href="https://doi.org/10.1038/nn.2727" target="_blank">Anastassiou et al. (2011)</a> は、endogenous field が cortical neuron の発火タイミングを偏らせうることを示しました。加えて <a href="https://doi.org/10.1126/science.aaf3736" target="_blank">Ding et al. (2016)</a> は、brain interstitial ion composition を変えるだけで sleep-like / wake-like state を切り替えうることを示し、<a href="https://doi.org/10.1016/j.neuron.2023.07.013" target="_blank">Burman et al. (2023)</a> は active cortical network が in vivo で fast inhibition を shunting mode に寄せることを、<a href="https://doi.org/10.1016/j.cub.2025.01.050" target="_blank">Alfonsa et al. (2025)</a> は sleep-wake-related な intracellular chloride 変化が glutamatergic cortical synapse の plasticity を制御することを示しました。したがって、<strong>同じ chemical connectome と同じ cell type でも、field / ion / chloride state が違えば inhibition の効き方、同期、state transition、plasticity gate はまだ変わりえます</strong>。
</p>
<div class="note-box">
<strong>今回固定する読み替え</strong>
<p>
このサイトでは今後、<strong>gap junction の有無</strong>、<strong>ephaptic field</strong>、<strong>interstitial ion / chloride state</strong> を、神経修飾や glial support の注釈へ埋め込んで済ませません。local ion / field / electrical-coupling 情報が無い場合、<strong>inhibition sign / gain</strong>、<strong>fast synchrony</strong>、<strong>state-switch threshold</strong>、<strong>plasticity gate</strong> は latent state として残し、chemical wiring だけで固定されたとは書きません。
</p>
</div>

<h3>5. 樹状突起は point neuron の自動補完先ではありません</h3>
<p>
<a href="https://doi.org/10.1038/35005094" target="_blank">Schiller et al. (2000)</a> は neocortical pyramidal neuron の basal dendrite で NMDA spike を示し、<a href="https://doi.org/10.1038/nn1253" target="_blank">Polsky et al. (2004)</a> は thin dendrite が独立した computational subunit として振る舞いうることを示しました。さらに <a href="https://doi.org/10.1038/nature12600" target="_blank">Smith et al. (2013)</a> は in vivo で dendritic spike が感覚選択性を高めることを、<a href="https://doi.org/10.1038/nature14251" target="_blank">Cichon &amp; Gan (2015)</a> は branch-specific dendritic Ca<sup>2+</sup> spike が持続的 plasticity を引き起こすことを、<a href="https://doi.org/10.1126/science.aah6066" target="_blank">Takahashi et al. (2016)</a> は active dendrite の介入が perception を動かすことを示しました。加えて human でも <a href="https://doi.org/10.1016/j.cell.2018.08.045" target="_blank">Beaulieu-Laroche et al. (2018)</a> と <a href="https://doi.org/10.1126/science.aax6239" target="_blank">Gidon et al. (2020)</a> が L2/3 neuron の強い compartmentalization と dendritic action potential を示し、<a href="https://doi.org/10.1038/s41593-025-01876-8" target="_blank">Sehgal et al. (2025)</a> は branch-specific plasticity が近接時刻の contextual memory linking に関わることを示しました。したがって、<strong>同じ connectome</strong>、<strong>同じ cell type</strong>、<strong>似た somatic firing</strong> があっても、branch ごとの非線形統合状態が違えば、single-neuron transfer function と学習の配分はまだ一致しません。
</p>
<div class="note-box">
<strong>今回固定する読み替え</strong>
<p>
このサイトでは今後、<strong>樹状突起 morphology</strong>、<strong>somatic spike train</strong>、<strong>平均受容野</strong>だけから、branch-specific な NMDA spike / plateau / dendritic spike threshold が分かったとは書きません。dendritic imaging、branch-specific perturbation、あるいはそれに準じる local validation が無い限り、point-neuron 化は <strong>便宜的近似</strong>として明示し、subcellular credit assignment と dendrite-dependent causal claim は保留します。
</p>
</div>

<h3>6. 遅延と髄鞘は timing の一部です</h3>
<p>
Gibson らは神経活動が oligodendrogenesis と adaptive myelination を促進することを示し、McKenzie らは motor skill learning に active central myelination が必要であることを報告しました。さらに Micheva らは、PV interneuron の局所軸索でも髄鞘化の程度が伝導速度と相関することを示しました。つまり、<strong>同じ配線でも timing state が違えば、局所抑制回路や学習のダイナミクスが変わる</strong>ため、delay を graph の外へ追い出すことはできません。
</p>

<h3>7. 神経修飾は「1つの気分スカラー」ではありません</h3>
<p>
Reimer らは、瞳孔変動が皮質内の adrenergic と cholinergic activity の両方を追うことを示しました。これは逆に、<strong>瞳孔径がどちらか一方の transmitter state を一意に表すわけではない</strong>ことも意味します。さらに Neyhart らは、皮質 ACh が cholinergic axon activity と行動状態からかなり予測できる一方で、<strong>近傍軸索からの距離と clearance kinetics に依存する局所性</strong>も持つことを示しました。したがって、人で瞳孔径や HRV を使うのは有用でも、それをトランスミッタ特異的・領域特異的な内部状態の ground truth と見なすのは過大主張です。必要なのは「良い proxy かどうか」だけではなく、<strong>何の proxy で何の proxy ではないか</strong>を明記することでございます。
</p>

<h3>8. グリアは後付けの補助変数ではありません</h3>
<p>
Adamsky らは astrocytic activation が de novo neuronal potentiation と memory enhancement を生みうることを示しました。Cahill らは、局所的で瞬間的な neurotransmitter input が、分単位にわたる広い astrocyte network の応答へ符号化されることを報告しています。したがって、<strong>グリアを無視したモデルは、可塑性や slow network state を部分的に欠いたモデル</strong>として扱うべきです。ここで重要なのは、「グリアも関わるらしい」という一般論ではなく、<strong>どの時定数のどの状態変数を捨てたか</strong>をモデル仕様として明示することでございます。
</p>
</section>

<section class="section" id="augmentation-ablation">
<h2 class="section-title">列挙で終わらせず、augmentation / ablation で比較する</h2>
<p>
現行サイトの弱点は、欠ける state variable を列挙できても、<strong>どの追加情報がどの誤差項を減らしたときに一段強い claim へ進めるのか</strong>が前面に出ていなかった点でした。2024-2026 年の一次文献は、connectome-only baseline から same-brain function、transcriptomic label、shared extracellular / electrical state、dendritic branch state、local transmitter dynamics、glial slow state、recovery log を足すと、改善の出方が別であることを示しています。したがって、このサイトでは <strong>state variable を「ある / ない」で数えるのではなく、augmentation / ablation で held-out predictive gain を比較する</strong>方針へ寄せます。
</p>
<table class="data-table">
<thead>
<tr>
<th>比較段階</th>
<th>追加する情報</th>
<th>一次文献が示す改善</th>
<th>それでも残る壁</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>connectome-only baseline</strong></td>
<td>配線制約つき recurrent model と、学習で埋める未知パラメータです。</td>
<td>Lappalainen らは fly visual system で広い活動予測を示し、Beiran と Litwin-Kumar は connectome を与えても未測定 biophysical parameter の違いで dynamics が大きく縮退しうることを示しました。</td>
<td>connectome-only の成功は conditional activity prediction を前進させますが、内部状態の唯一解や state-complete reconstruction は依然として読めません。</td>
</tr>
<tr>
<td><strong>+ same-brain function / behavior</strong></td>
<td>同一個体で co-registered な機能計測と行動状態です。</td>
<td>MICrONS は同じマウスで dense neural activity、EM connectome、pupil diameter、locomotion を結び、構造と state-dependent function を同一脳内で比較できる足場を作りました。これは <strong>local structure-function constraint</strong> を大きく前進させますが、current synaptic efficacy の直接読出しそのものではありません。</td>
<td>mouse visual cortex の特定課題・特定状態での前進であり、全脳・全状態の一般化や hidden state の十分性、さらには momentary synaptic weight の十分性までは保証しません。</td>
</tr>
<tr>
<td><strong>+ transcriptomic / cell-type label</strong></td>
<td>same-brain か近接条件での transcriptomic type と target specificity です。</td>
<td>Gamlin らは predicted Sst transcriptomic types ごとに接続モチーフ、シナプス特性、髄鞘化が系統的に異なることを示し、node label の増分価値を具体化しました。</td>
<td>within-type heterogeneity と morpho-electric variability は残るため、cell-type label を足しても threshold / gain / set point はまだ latent のままです。</td>
</tr>
<tr>
<td><strong>+ dendritic branch readout / perturbation</strong></td>
<td>dendritic voltage / Ca imaging、branch-specific stimulation、clustered-vs-dispersed input test です。</td>
<td>Schiller、Smith、Cichon &amp; Gan、Takahashi、Sehgal らは、branch-specific な非線形統合を足すと感覚選択性、学習後の持続 plasticity、近接時刻記憶リンクの説明力が上がることを示しました。</td>
<td>coverage は sparse で local です。human whole-brain では依然として soma-only readout と ex vivo validation の gap が大きく、point-neuron 近似の ceiling も残ります。</td>
</tr>
<tr>
<td><strong>+ local transmitter dynamics</strong></td>
<td>局所 cholinergic axon activity や behavior-linked transmitter proxy です。</td>
<td>Neyhart らは cortical ACh dynamics が cholinergic axon activity と behavioral state からかなり予測できる一方、近傍軸索からの距離と clearance kinetics で局所性が変わることを示しました。</td>
<td>pupil / behavior / global arousal はなお coarse proxy であり、transmitter-specific・region-specific ground truth に自動昇格はできません。</td>
</tr>
<tr>
<td><strong>+ glial / slow-state</strong></td>
<td>astrocyte network state、microglia / synaptic-density 変化、分オーダーの slow response です。</td>
<td>Cahill らは local transient neurotransmitter inputs が broad cortical astrocyte network に minutes-long に符号化されることを示し、Vadisiute らは acute chemogenetic manipulation 後に astrocyte・microglia・synaptic density が急速に変化することを示しました。</td>
<td>slow state の寄与は cell type、課題、種差に依存し、ここを足しても即座に全脳 emulation には繋がりません。</td>
</tr>
<tr>
<td><strong>+ perturbation / recovery of excitability-homeostasis</strong></td>
<td>学習前後または介入後の intrinsic excitability、recovery time、memory allocation 指標です。</td>
<td>Hadzibegovic らは、neocortical engram neurons の early intrinsic excitability plasticity が memory formation と precision を規定することを示し、recovery log を足す価値を具体化しました。</td>
<td>engram-specific かつ early-window の証拠であり、全脳の長期 controller をこれだけで置き換えることはできません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>このサイトでの合格条件</strong>
<p>
追加した state variable を「効いた」と書けるのは、少なくとも <strong>(a) connectome-only baseline</strong> と <strong>(b) 追加変数つき model</strong> を <strong>同じ split / 同じ held-out 条件</strong>で比べ、cross-state / cross-day / perturbation / recovery のどれかで predictive gain を示し、同時に <strong>proxy specificity</strong>、<strong>family / uncertainty</strong>、<strong>abstention</strong> を公開したときだけでございます。そこまで出ていなければ、本サイトでは annotation、stratification covariate、post hoc explanation のいずれかとして扱います。
</p>
</div>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">このサイトで採用する読み替えルールと最低提出物</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>connectome-complete：</strong>構造アトラス、候補 scaffold、圧縮の出発点として扱います。L2/L3 の emulation 達成とは書きません。</li>
<li><strong>connectome-constrained model：</strong>まずは hypothesis engine / conditional model として扱います。内部状態の唯一解とは書きません。</li>
<li><strong>augmentation / ablation：</strong>connectome-only baseline を置かずに、「追加した state variable が効いた」とは書きません。</li>
<li><strong>species / stack をまたぐとき：</strong>fly / mouse / human、local / fragment / whole-brain、structural / functional / metabolic の差を本文に残し、external validity ceiling を省略しません。</li>
<li><strong>intrinsic excitability / homeostatic set point：</strong>cell-type ラベルや短時間の活動一致から自動推定されたことにはしません。測っていなければ latent state と書きます。</li>
<li><strong>PSD 面積 / spine size / synapse count：</strong>paired physiology や perturbation が無い限り、current effective weight とは書かず、structural prior と書きます。</li>
<li><strong>樹状突起 morphology / soma-only fit：</strong>branch-specific NMDA spike / plateau / dendritic action potential が直接見えたとは書かず、point-neuron 近似の適用範囲を残します。</li>
<li><strong>pupil / HRV：</strong>人データでは有用な state covariate ですが、トランスミッタ特異的 ground truth としては扱いません。</li>
<li><strong>state variable が無いとき：</strong>推定したなら誤差と棄権条件を、推定していないなら absent と明記します。</li>
<li><strong>weights / delays が無いとき：</strong>phase、timing、介入応答、閉ループ安定性の主張は降格します。</li>
<li><strong>human metabolic scaffold：</strong>parcel-level biochemical organization と、cell-specific glial / transmitter maintenance-state を混同しません。</li>
<li><strong>glia / neuromodulation を落とすとき：</strong>その近似で何の振る舞いを捨てたのかを、適用範囲として本文に書きます。</li>
<li><strong>family が複数残るとき：</strong>confidence だけで押し切らず、family comparison、不確実性、abstention を公開します。</li>
</ul>
</div>
<table class="data-table">
<thead>
<tr>
<th>主張したいこと</th>
<th>最低限ほしい提出物</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>構造 atlas / scaffold</strong></td>
<td>coverage、segmentation caveat、synapse count の扱い、cell-type ラベルの有無を明記します。</td>
</tr>
<tr>
<td><strong>state-variable augmentation claim</strong></td>
<td>connectome-only baseline、同じ split / held-out 条件での predictive gain、ablation 結果、proxy specificity、family / uncertainty、abstention を併記します。</td>
</tr>
<tr>
<td><strong>条件付き dynamical claim</strong></td>
<td>same-brain function または perturbation、欠測 state variable 一覧、proxy の限界、family / uncertainty、さらに intrinsic excitability / homeostatic set point や dendritic integration state を測っていない場合はその不在を添えます。</td>
</tr>
<tr>
<td><strong>介入・閉ループ claim</strong></td>
<td>上記に加え、weights / dendritic integration / delays / neuromodulation / excitability-homeostasis の較正ルート、外部妥当化、abstention / stop 条件まで公開します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435–447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <em>Nature</em>, 634, 1132–1140. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <em>Nature Neuroscience</em>, 28, 2561–2574. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497–505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Holler, S., et al. (2021). Structure and function of a neocortical synapse. <em>Nature</em>, 591, 111–116. <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">doi:10.1038/s41586-020-03134-2</a></li>
<li>Dürst, C. D., Wiegert, J. S., Schulze, C., et al. (2022). Vesicular release probability sets the strength of individual Schaffer collateral synapses. <em>Nature Communications</em>, 13, 6126. <a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">doi:10.1038/s41467-022-33565-6</a></li>
<li>Schiller, J., Major, G., Koester, H. J., &amp; Schiller, Y. (2000). NMDA spikes in basal dendrites of cortical pyramidal neurons. <em>Nature</em>, 404, 285–289. <a href="https://doi.org/10.1038/35005094" target="_blank">doi:10.1038/35005094</a></li>
<li>Polsky, A., Mel, B. W., &amp; Schiller, J. (2004). Computational subunits in thin dendrites of pyramidal cells. <em>Nature Neuroscience</em>, 7, 621–627. <a href="https://doi.org/10.1038/nn1253" target="_blank">doi:10.1038/nn1253</a></li>
<li>Smith, S. L., Smith, I. T., Branco, T., &amp; Häusser, M. (2013). Dendritic spikes enhance stimulus selectivity in cortical neurons in vivo. <em>Nature</em>, 503, 115–120. <a href="https://doi.org/10.1038/nature12600" target="_blank">doi:10.1038/nature12600</a></li>
<li>Cichon, J., &amp; Gan, W.-B. (2015). Branch-specific dendritic Ca<sup>2+</sup> spikes cause persistent synaptic plasticity. <em>Nature</em>, 520, 180–185. <a href="https://doi.org/10.1038/nature14251" target="_blank">doi:10.1038/nature14251</a></li>
<li>Takahashi, N., Oertner, T. G., Hegemann, P., &amp; Larkum, M. E. (2016). Active cortical dendrites modulate perception. <em>Science</em>, 354(6319), 1587–1590. <a href="https://doi.org/10.1126/science.aah6066" target="_blank">doi:10.1126/science.aah6066</a></li>
<li>Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. <em>Nature</em>, 429, 761–766. <a href="https://doi.org/10.1038/nature02617" target="_blank">doi:10.1038/nature02617</a></li>
<li>Vardalaki, D., Chung, K., &amp; Harnett, M. T. (2022). Filopodia are a structural substrate for silent synapses in adult neocortex. <em>Nature</em>, 612, 323–327. <a href="https://doi.org/10.1038/s41586-022-05483-6" target="_blank">doi:10.1038/s41586-022-05483-6</a></li>
<li>Alle, H., et al. (2024). Membrane potential states gate synaptic consolidation in human neocortical tissue. <em>Nature Communications</em>, 15, 10340. <a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">doi:10.1038/s41467-024-53901-2</a></li>
<li>Galarreta, M., &amp; Hestrin, S. (1999). A network of fast-spiking cells in the neocortex connected by electrical synapses. <em>Nature</em>, 402, 72–75. <a href="https://doi.org/10.1038/99496" target="_blank">doi:10.1038/99496</a></li>
<li>Anastassiou, C. A., Perin, R., Markram, H., &amp; Koch, C. (2011). Ephaptic coupling of cortical neurons. <em>Nature Neuroscience</em>, 14, 217–223. <a href="https://doi.org/10.1038/nn.2727" target="_blank">doi:10.1038/nn.2727</a></li>
<li>Ding, F., O'Donnell, J., Xu, Q., Kang, N., Goldman, N., &amp; Nedergaard, M. (2016). Changes in the composition of brain interstitial ions control the sleep-wake cycle. <em>Science</em>, 352(6285), 550–555. <a href="https://doi.org/10.1126/science.aaf3736" target="_blank">doi:10.1126/science.aaf3736</a></li>
<li>Burman, R. J., et al. (2023). Active cortical networks promote shunting fast synaptic inhibition in vivo. <em>Neuron</em>, 111(22), 3633–3648.e8. <a href="https://doi.org/10.1016/j.neuron.2023.07.013" target="_blank">doi:10.1016/j.neuron.2023.07.013</a></li>
<li>Alfonsa, H., et al. (2025). Sleep-wake-related changes in intracellular chloride regulate plasticity at glutamatergic cortical synapses. <em>Current Biology</em>. <a href="https://doi.org/10.1016/j.cub.2025.01.050" target="_blank">doi:10.1016/j.cub.2025.01.050</a></li>
<li>Beaulieu-Laroche, L., Toloza, E. H. S., van der Goes, M.-S., et al. (2018). Enhanced Dendritic Compartmentalization in Human Cortical Neurons. <em>Cell</em>, 175(3), 643–651.e14. <a href="https://doi.org/10.1016/j.cell.2018.08.045" target="_blank">doi:10.1016/j.cell.2018.08.045</a></li>
<li>Gidon, A., Zolnik, T. A., Fidzinski, P., et al. (2020). Dendritic action potentials and computation in human layer 2/3 cortical neurons. <em>Science</em>, 367(6473), 83–87. <a href="https://doi.org/10.1126/science.aax6239" target="_blank">doi:10.1126/science.aax6239</a></li>
<li>Sehgal, M., et al. (2025). Compartmentalized dendritic plasticity in the mouse retrosplenial cortex links contextual memories formed close in time. <em>Nature Neuroscience</em>, 28, 602–615. <a href="https://doi.org/10.1038/s41593-025-01876-8" target="_blank">doi:10.1038/s41593-025-01876-8</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318–322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Micheva, K. D., Kiraly, M., Perez, M. M., & Madison, D. V. (2021). Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. <em>Cerebral Cortex</em>, 31(7), 3374–3392. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">doi:10.1093/cercor/bhab018</a></li>
<li>Reimer, J., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Adamsky, A., et al. (2018). Astrocytic activation generates de novo neuronal potentiation and memory enhancement. <em>Nature Neuroscience</em>, 21, 1725–1733. <a href="https://doi.org/10.1038/s41593-018-0253-6" target="_blank">doi:10.1038/s41593-018-0253-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <em>Communications Biology</em>, 7, 1498. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Loomba, S., Straehle, J., Gangadharan, V., et al. (2022). Connectomic comparison of mouse and human cortex. <em>Science</em>, 377(6602), eabo0924. <a href="https://doi.org/10.1126/science.abo0924" target="_blank">doi:10.1126/science.abo0924</a></li>
<li>Shapson-Coe, A., Januszewski, M., Berger, D. R., et al. (2024). A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. <em>Science</em>, 384(6696), eadk4858. <a href="https://doi.org/10.1126/science.adk4858" target="_blank">doi:10.1126/science.adk4858</a></li>
<li>Lucchetti, F., Céléreau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <em>Nature Communications</em>, 16, 11344. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Louveau, A., Smirnov, I., Keyes, T. J., et al. (2015). Structural and functional features of central nervous system lymphatic vessels. <em>Nature</em>, 523, 337-341. <a href="https://doi.org/10.1038/nature14432" target="_blank">doi:10.1038/nature14432</a></li>
<li>Kim, J., et al. (2025). Meningeal lymphatics-microglia axis regulates synaptic physiology. <em>Cell</em>, 188(8), 2129-2148.e21. <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">doi:10.1016/j.cell.2025.02.022</a></li>
<li>Eide, P. K., &amp; Ringstad, G. (2021). Sleep deprivation impairs molecular clearance from the human brain. <em>Brain</em>, 144(3), 863-874. <a href="https://doi.org/10.1093/brain/awab285" target="_blank">doi:10.1093/brain/awab285</a></li>
<li>Hirschler, L., et al. (2025). Region-specific drivers of cerebrospinal fluid mobility measured with MRI in humans. <em>Nature Neuroscience</em>, 28, 1115-1126. <a href="https://doi.org/10.1038/s41593-025-02073-3" target="_blank">doi:10.1038/s41593-025-02073-3</a></li>
<li>Dagum, P., et al. (2026). The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. <em>Nature Communications</em>, 17, 7800. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBEの基本 →</a></li>
<li><a href="homeostatic-plasticity-and-maintenance-state.html">恒常性可塑性と維持状態 →</a></li>
<li><a href="decode-vs-emulate.html">Decode と Emulate →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../wbe_101.html">WBE入門 →</a></li>
<li><a href="../verification.html#state-completeness-gate">状態変数の完全性ゲート →</a></li>
<li><a href="../tech_roadmap.html#qa-r10">R10 神経修飾 →</a></li>
</ul>
</div>
</aside>
</main>
