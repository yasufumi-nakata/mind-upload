---
layout: default
title: "Wiki：配線図だけでは足りない理由"
description: "WBE で connectome だけを保存しても足りない理由を、状態変数の欠落と connectome-constrained 推定の限界まで含めて一次文献から整理します。"
article_type: Wiki
subtitle: "connectome-complete は emulation-complete ではありません"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Technical / natural science only"
audience: "配線図が取れたら WBE に近いのかを、技術と自然科学だけで判断したい人"
reading_time: "15〜20分"
page_intro: "このページは、『コネクトームが取れれば脳の再現に十分ではないか』という直感を、一次文献に基づいて分解するためのページです。哲学や法制度ではなく、どの状態変数が欠けると何が言えなくなるか、さらに connectome-constrained でもどの推定上の壁が残るかに絞って整理します。"
accuracy_note: "ここで示すのは『最低限これを外すと主張が弱くなる』という整理と、『配線制約を入れてもなお残る縮退』の整理であり、最終的な十分条件が確定したという意味ではありません。"
page_highlights:
  - "配線図だけでは落ちる論点を、6つの状態クラスと1つの推定上の壁に分けて整理します。"
  - "一次文献だけを使い、state variable の欠落と parameter degeneracy を切り分けます。"
  - "このサイトで connectome-complete と connectome-constrained model をどう読み替えるかの運用ルールも固定します。"
known_points:
  - "全脳 connectome の作成は大きく前進していますが、それだけで動的再現が完了したとは言えません。"
  - "シナプス効率、遅延、神経修飾、グリア、細胞型ラベル、内在興奮性 / 恒常性 set point は、静的な edge list からは落ちやすい情報です。"
  - "粗い生理 proxy を ground truth と混同すると、内部状態の主張を過大化しやすくなります。"
  - "connectome-constrained なモデルでも、未測定の細胞・シナプス・修飾パラメータが残ると dynamics は縮退しえます。"
unknown_points:
  - "どの状態クラスをどの解像度まで取れば WBE の十分条件に近づくかは未確定です。"
  - "欠落した状態変数をどこまで推定や coarse-graining で補えるかは、今後の検証課題です。"
  - "人で直接取得できない状態を、どの動物・侵襲系で較正すべきかはまだ固定されていません。"
  - "same-brain function を足したとき、どの程度まで縮退が解けるかもまだ系統的には定まっていません。"
wiki_links:
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "この論点の前提になる全体像を初歩から整理します。"
  - label: "Wiki: 恒常性可塑性と維持状態"
    url: "/wiki/homeostatic-plasticity-and-maintenance-state.html"
    description: "内在興奮性や発火 set point がなぜ別変数かを深掘りします。"
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
配線図は WBE の重要な土台ですが、<strong>それだけでは動的再現の下限要件になりません</strong>。同じ隣接関係でも、細胞型ラベル、内在興奮性、シナプス効率、伝導遅延、神経修飾、グリア結合状態が違えば、学習、位相同期、覚醒度依存の応答、長期安定性は大きく変わります。さらに、2024-2025 年の connectome-constrained modelling 研究は、<strong>配線制約を入れても未測定パラメータと省略機構のために dynamics の縮退が残る</strong>ことを示しました。したがって、このサイトでは <strong>connectome-complete を structural atlas / scaffold の達成</strong>として扱い、<strong>emulation-complete と言い換えません</strong>。同様に、<strong>connectome-constrained model が一部の活動を再現した</strong>ことも、そのまま state-complete reconstruction とは読みません。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。技術と自然科学の側面だけから、「何の状態変数が欠けると何が主張できなくなるか」と、「配線制約を入れても何がまだ一意に決まらないか」を整理します。
</p>
</div>

<section class="section" id="bottom-line">
<h2 class="section-title">先に固定する 6 つの状態クラスと 1 つの推定上の壁</h2>
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
従来の 5 クラスに加えて、2026-03 の再監査では <strong>内在興奮性・恒常性 set point</strong> を独立クラスとして切り出しました。理由は、cell-type ラベルや connectome を持っていても、threshold、gain、発火率の戻り先、分子ターンオーバー下の維持機構が違えば、長期予測と摂動回復がまだ定まらないためです。一次文献のまとまった整理は <a href="homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> に分けております。
</p>
</div>
</section>

<section class="section" id="connectome-progress">
<h2 class="section-title">配線図研究は大きく進んだが、それ自体は終点ではない</h2>
<p>
Dorkenwald らは成体ショウジョウバエ全脳の wiring diagram を示し、約 13 万ニューロン規模で全脳 connectome を提示しました。一方で MICrONS Consortium は、マウス視覚皮質の立方ミリメートル規模で、同一個体の機能計測と connectomics を結びつけるデータセットと局所 functional digital twin を公開しました。さらに Lappalainen らは、ショウジョウバエ視覚系で connectome-constrained network を task-optimized に学習させ、広い範囲の活動予測を可能にしました。これは非常に大きな前進ですが、逆に言えば、<strong>現在ようやく「配線＋一部機能＋追加仮定」を結び始めた段階</strong>であり、全脳・全状態の動的再現とはまだ別問題であることも示しています。
</p>
<div class="note-box">
<strong>ここでの読み替え</strong>
<p>
connectome-complete は「何がつながっているか」がかなり分かったという意味では重要です。しかし、それだけでは「どの強さで」「どの遅延で」「どの neuromodulatory context で」「どの glial coupling の下で」動くかまでは固定されません。さらに Lappalainen らの reductionist model でも、著者自身が electrical synapses、nonlinear chemical synapses、neuromodulation を説明外に置いています。したがって、本サイトでは connectome-complete を <strong>structural atlas / scaffold</strong> の達成として扱い、L2/L3 の emulation claim へは自動的に昇格させません。<strong>connectome-constrained による activity prediction</strong> も、まずは hypothesis engine と conditional model として読みます。
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
<h2 class="section-title">なぜこの 6 クラスが抜けやすいのか</h2>

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
Holler らは新皮質シナプスで、超微細構造と release property を結びつけて解析し、単純な「つながっている/いない」では伝達特性を表せないことを示しました。Matsuzaki らは単一 dendritic spine における LTP 誘導で、spine enlargement と AMPA 電流増加が結びつくことを示しています。さらに Vardalaki らは、成体新皮質でもおよそ 25% の filopodia が AMPA 受容体を欠く silent synapse の構造基盤になりうることを示しました。したがって、<strong>edge list だけでは current state の weight も plastic history も、そもそも機能的に active かどうかも落ちます</strong>。
</p>

<h3>4. 遅延と髄鞘は timing の一部です</h3>
<p>
Gibson らは神経活動が oligodendrogenesis と adaptive myelination を促進することを示し、McKenzie らは motor skill learning に active central myelination が必要であることを報告しました。さらに Micheva らは、PV interneuron の局所軸索でも髄鞘化の程度が伝導速度と相関することを示しました。つまり、<strong>同じ配線でも timing state が違えば、局所抑制回路や学習のダイナミクスが変わる</strong>ため、delay を graph の外へ追い出すことはできません。
</p>

<h3>5. 神経修飾は「1つの気分スカラー」ではありません</h3>
<p>
Reimer らは、瞳孔変動が皮質内の adrenergic と cholinergic activity の両方を追うことを示しました。これは逆に、<strong>瞳孔径がどちらか一方の transmitter state を一意に表すわけではない</strong>ことも意味します。さらに Neyhart らは、皮質 ACh が cholinergic axon activity と行動状態からかなり予測できる一方で、<strong>近傍軸索からの距離と clearance kinetics に依存する局所性</strong>も持つことを示しました。したがって、人で瞳孔径や HRV を使うのは有用でも、それをトランスミッタ特異的・領域特異的な内部状態の ground truth と見なすのは過大主張です。必要なのは「良い proxy かどうか」だけではなく、<strong>何の proxy で何の proxy ではないか</strong>を明記することでございます。
</p>

<h3>6. グリアは後付けの補助変数ではありません</h3>
<p>
Adamsky らは astrocytic activation が de novo neuronal potentiation と memory enhancement を生みうることを示しました。Cahill らは、局所的で瞬間的な neurotransmitter input が、分単位にわたる広い astrocyte network の応答へ符号化されることを報告しています。したがって、<strong>グリアを無視したモデルは、可塑性や slow network state を部分的に欠いたモデル</strong>として扱うべきです。ここで重要なのは、「グリアも関わるらしい」という一般論ではなく、<strong>どの時定数のどの状態変数を捨てたか</strong>をモデル仕様として明示することでございます。
</p>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">このサイトで採用する読み替えルールと最低提出物</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>connectome-complete：</strong>構造アトラス、候補 scaffold、圧縮の出発点として扱います。L2/L3 の emulation 達成とは書きません。</li>
<li><strong>connectome-constrained model：</strong>まずは hypothesis engine / conditional model として扱います。内部状態の唯一解とは書きません。</li>
<li><strong>intrinsic excitability / homeostatic set point：</strong>cell-type ラベルや短時間の活動一致から自動推定されたことにはしません。測っていなければ latent state と書きます。</li>
<li><strong>pupil / HRV：</strong>人データでは有用な state covariate ですが、トランスミッタ特異的 ground truth としては扱いません。</li>
<li><strong>state variable が無いとき：</strong>推定したなら誤差と棄権条件を、推定していないなら absent と明記します。</li>
<li><strong>weights / delays が無いとき：</strong>phase、timing、介入応答、閉ループ安定性の主張は降格します。</li>
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
<td><strong>条件付き dynamical claim</strong></td>
<td>same-brain function または perturbation、欠測 state variable 一覧、proxy の限界、family / uncertainty、さらに intrinsic excitability / homeostatic set point を測っていない場合はその不在を添えます。</td>
</tr>
<tr>
<td><strong>介入・閉ループ claim</strong></td>
<td>上記に加え、weights / delays / neuromodulation / excitability-homeostasis の較正ルート、外部妥当化、abstention / stop 条件まで公開します。</td>
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
<li>Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. <em>Nature</em>, 429, 761–766. <a href="https://doi.org/10.1038/nature02617" target="_blank">doi:10.1038/nature02617</a></li>
<li>Vardalaki, D., Chung, K., &amp; Harnett, M. T. (2022). Filopodia are a structural substrate for silent synapses in adult neocortex. <em>Nature</em>, 612, 323–327. <a href="https://doi.org/10.1038/s41586-022-05483-6" target="_blank">doi:10.1038/s41586-022-05483-6</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318–322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Micheva, K. D., Kiraly, M., Perez, M. M., & Madison, D. V. (2021). Conduction Velocity Along the Local Axons of Parvalbumin Interneurons Correlates With the Degree of Axonal Myelination. <em>Cerebral Cortex</em>, 31(7), 3374–3392. <a href="https://doi.org/10.1093/cercor/bhab018" target="_blank">doi:10.1093/cercor/bhab018</a></li>
<li>Reimer, J., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Adamsky, A., et al. (2018). Astrocytic activation generates de novo neuronal potentiation and memory enhancement. <em>Nature Neuroscience</em>, 21, 1725–1733. <a href="https://doi.org/10.1038/s41593-018-0253-6" target="_blank">doi:10.1038/s41593-018-0253-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146–153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
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
