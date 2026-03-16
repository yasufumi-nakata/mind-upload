---
layout: default
title: "Wiki：計測スタックごとの observability と claim ceiling"
description: "EEG/MEG/fMRI、高密度 extracellular probe、whole-brain spatial atlas、Patch-seq、volume EM、same-brain functional connectomics、transmitter/glia imaging が何を直接観測し、どこで主張上限に当たるかを、state variable と timescale まで含めて整理します。"
article_type: Wiki
subtitle: "multimodal は『全部見えた』の同義語ではありません"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Technical / natural science only"
audience: "どの modality で何が直接見え、どの claim までなら妥当かを、技術と自然科学だけで整理したい人"
reading_time: "16〜24分"
page_intro: "このページは、WBE の議論で見落としやすい『measurement stack ごとの主張上限』を固定する wiki です。hidden state が重要だというだけでは足りません。EEG/MEG/fMRI、高密度 extracellular probe、spatial transcriptomics、Patch-seq、volume EM、same-brain functional connectomics、local transmitter / glia imaging が、それぞれ何を直接観測し、何をまだ latent に残すのかを、state variable と timescale まで含めて一次文献ベースで整理します。"
accuracy_note: "以下の『claim ceiling』列は、各論文がそのまま宣言している結論ではありません。一次文献が直接観測した変数と、依然として未観測の状態変数から本サイトが引く運用上の推論でございます。"
page_highlights:
  - "『hidden state がある』という一般論を、『どの計測 stack で何がまだ未観測か』へ落とし直します。"
  - "multimodal / atlas / connectome の語を、そのまま state-complete と誤読しないための ceiling を固定します。"
  - "stack の表だけでなく、state variable × timescale × direct / proxy / inferred の行列も追加し、何が本当に直接見えているかを分解します。"
  - "fMRI / BOLD は neural truth ではなく、neurovascular transfer・HRF・venous geometry を介した proxy として扱います。"
  - "neuromodulation も 1 本ではなく、behavior proxy / axon activity / local transmitter sensor / receptor atlas / receptor physiology の別ラダーとして扱います。"
known_points:
  - "EEG/MEG/fMRI はマクロな proxy を与えますが、細胞型、シナプス効率、神経修飾場、グリア状態を直接は与えません。"
  - "fMRI の振幅や onset は、神経活動だけでなく HRF の変動や vascular geometry の影響も受けます。"
  - "高密度 extracellular probe は implant 近傍の local population を強く見ますが、chronic な single-unit identity は sorting と matching を介した推定です。"
  - "whole-brain spatial transcriptomics は cell-type taxonomy と空間配置を大きく前進させますが、動的状態の十分性は別問題です。"
  - "Patch-seq と same-brain connectomics は縮退を減らしますが、全脳 coverage と長期 maintenance-state の十分性は残ります。"
  - "local transmitter / glia imaging は coarse proxy の校正に有効ですが、そのまま全脳 ground truth にはなりません。"
  - "pupil や locomotion は mixed arousal proxy であり、local transmitter sensor や receptor atlas / physiology とは別の evidence class です。"
unknown_points:
  - "どの stack の組み合わせが WBE に対して最も効率よく縮退を減らすかは、まだ固定できません。"
  - "同一脳・全脳・長期縦断で、どの latent state まで取得すべきかの十分条件は未確定です。"
  - "stack 間の augmentation 順序をどう最適化するかも、課題・種・時定数ごとに変わり得ます。"
wiki_links:
  - label: "Wiki: 配線図だけでは足りない理由"
    url: "/wiki/connectome-is-not-enough.html"
    description: "何の状態変数が抜けるかを先に整理したページです。"
  - label: "Wiki: 恒常性可塑性と維持状態"
    url: "/wiki/homeostatic-plasticity-and-maintenance-state.html"
    description: "長期 maintenance-state の側から不足変数を深掘りします。"
  - label: "Wiki: マルチモーダル統合の基本"
    url: "/wiki/multimodal-integration-basics.html"
    description: "EEG/MEG/fMRI/侵襲記録の統合監査を詳しく見たいときはこちらです。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "観測値と latent state 推定を混同しないための入口です。"
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
<h2>いちばん短い結論</h2>
<p>
現行サイトの弱点は、<strong>重要な hidden state は列挙できても、どの measurement stack が何を直接観測し、どこで主張上限に当たるか</strong>が前面に出ていなかった点でございました。一次文献を並べると、EEG/MEG/fMRI はマクロ state の tracking、高密度 extracellular probe は implant 近傍の local population window、whole-brain spatial atlas は cell-type と空間配置、Patch-seq は cell-type と morpho-electric phenotype の橋渡し、volume EM は structural scaffold、same-brain functional connectomics は局所 conditional prediction、local transmitter / astrocyte imaging は coarse proxy の較正を強くします。しかし、<strong>どの stack も単独では state-complete reconstruction を与えません</strong>。したがって本サイトでは、measurement stack ごとに claim ceiling を明記し、そこを超える表現を禁止します。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学、法制度、本人性は扱いません。扱うのは、技術と自然科学の側面だけから見た「どの観測で何が直接見えて、何がまだ latent か」という問題です。
</p>
</div>

<section class="section" id="weakness">
<h2 class="section-title">今回深掘りする弱点</h2>
<p>
従来の公開ページは、connectome だけでは足りないこと、maintenance-state が残ること、augmentation / ablation で比較すべきことを既に押さえていました。しかし、それだけでは読者が <strong>multimodal</strong>、<strong>atlas</strong>、<strong>same-brain</strong> という語を見たときに、「かなり全部見えた」と過大解釈する余地が残ります。弱点は、<strong>state variable の議論</strong>と<strong>measurement stack の議論</strong>がまだ十分に一体化していなかったことでございます。
</p>
<p>
そこで本ページでは、各 stack の直接観測量、何を少し強く言えるか、何が依然として latent state として残るか、そしてこのサイトで許す <strong>claim ceiling</strong> を 1 つの表に統合します。今回の更新ではさらに、row を measurement stack から <strong>state variable</strong> へ切り替えた timescale 行列も追加し、「multimodal」という 1 語に畳み込まれやすい不足を分離します。
</p>
</section>

<section class="section" id="matrix">
<h2 class="section-title">計測スタックごとの observability と claim ceiling</h2>
<div class="note-box">
<strong>読み方</strong>
<p>
下の表の最後の列は、各論文の要約ではなく、本サイトの運用ルールです。つまり、<strong>その stack が直接観測した変数</strong>と、<strong>依然として未観測の状態変数</strong>から引く、根拠付きの主張上限でございます。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>measurement stack</th>
<th>直接観測しているもの</th>
<th>比較的強く言えること</th>
<th>まだ latent に残るもの</th>
<th>このサイトでの claim ceiling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG</strong></td>
<td>大域的に同期した電流場と、その時間変化です。</td>
<td>ms スケールの大域 state 遷移、周波数帯ダイナミクス、閉ループ timing constraint の一部を監査できます。</td>
<td>深部源の一意性、細胞型、現在のシナプス効率、neuromodulatory field、glial / metabolic state は直接は決まりません。</td>
<td><strong>マクロ state tracking と weak L2 まで</strong>です。cell / synapse 粒度や state-complete claim には上げません。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>BOLD を中心とする血行動態 proxy と、領域スケールの遅い network state です。</td>
<td>広域 coverage、recruitment pattern、比較的遅い state occupancy、同一個体内の large-scale network constraint を追えます。</td>
<td>ms timing、興奮/抑制の分離、region-specific HRF、静脈ドレナージと層方向の空間歪み、局所 transmitter dynamics、current synaptic efficacy は直接は見えません。</td>
<td><strong>広域 state atlas と coarse dynamical constraint まで</strong>です。fast causal order、laminar microcircuit、BOLD 振幅の単純な neural gain 解釈は主張しません。</td>
</tr>
<tr>
<td><strong>whole-brain spatial transcriptomics / cell atlas</strong></td>
<td>ex vivo の transcriptomic cell type と空間配置です。</td>
<td>Yao らの whole-mouse-brain atlas のように、cell-type taxonomy、領域ごとの分布、分子地図を大きく前進させられます。</td>
<td>現在の発火則、シナプス効率、neuromodulatory / glial state、sleep-history、perturbation 後の戻り先は残ります。</td>
<td><strong>molecular atlas / cell-type prior まで</strong>です。dynamic completeness や current state の十分性へは上げません。</td>
</tr>
<tr>
<td><strong>Patch-seq / morpho-electric-transcriptomic bridge</strong></td>
<td>単一細胞の transcriptome・形態・電気生理の対応です。</td>
<td>Gouwens らや Gamlin らの系のように、cell-type label と morpho-electric phenotype、さらに一部の connectivity motif の橋渡しを強くできます。</td>
<td>全脳 coverage、same-brain の回路文脈、current network state、longitudinal plastic history は残ります。</td>
<td><strong>cell-type-specific prior と局所 parameter constraint まで</strong>です。全脳 state completeness には使いません。</td>
</tr>
<tr>
<td><strong>high-density extracellular probe<br>(Neuropixels / Utah / microwire)</strong></td>
<td>implant 近傍の extracellular spike waveform、threshold crossing、multiunit / local field activity です。</td>
<td>Steinmetz らや Neuropixels 系のように、implant region の local population dynamics、online decode、比較的強い局所 readout を一段強くできます。</td>
<td>未記録 neuron、stable single-unit identity across days、sorting-dependent cluster boundary、probe drift、tissue response、synaptic / transmitter / glial state、全脳 coverage は残ります。</td>
<td><strong>implant-region の local population window と stated validity horizon まで</strong>です。stable neuron identity や whole-brain ground truth には上げません。</td>
</tr>
<tr>
<td><strong>volume EM connectomics</strong></td>
<td>超微細形態と chemical synapse の構造 snapshot です。</td>
<td>Dorkenwald らの全脳 fly wiring diagram のように、structural scaffold、projectome、候補回路を強くできます。</td>
<td>current synaptic weight、intrinsic excitability、neuromodulatory context、glial slow state、sleep-dependent maintenance は直接は入りません。</td>
<td><strong>structural atlas / scaffold まで</strong>です。connectome-complete を emulation-complete と言い換えません。</td>
</tr>
<tr>
<td><strong>same-brain functional connectomics</strong></td>
<td>同一脳で co-registered な dense activity と EM connectome の対応です。</td>
<td>MICrONS のように、局所回路で structure-function link、state-dependent response prediction、cell-type 依存 wiring rule を一段強くできます。</td>
<td>全脳 coverage、全状態一般化、current synaptic efficacy の十分性、homeostatic controller、glial / metabolic maintenance-state は残ります。</td>
<td><strong>局所 conditional prediction と local functional twin まで</strong>です。全脳 WBE や state-complete reconstructionへは上げません。</td>
</tr>
<tr>
<td><strong>local transmitter imaging / behavior-linked proxy</strong></td>
<td>局所 transmitter dynamics と、その axon activity / pupil / locomotion / receptor prior との関係です。</td>
<td>Neyhart、Lohani、Collins、Reimer らの系のように、mixed arousal proxy、axon activity、local chemical signal がどこまで一致しどこで分かれるかを較正できます。</td>
<td>全脳の transmitter field、momentary receptor occupancy、cell-type-specific effect、region-generalizable ground truth、long-timescale maintenance-state は残ります。</td>
<td><strong>mixed arousal proxy / local chemical proxy / regional receptor prior まで</strong>です。single-transmitter ground truth や全脳 internal state とは書きません。</td>
</tr>
<tr>
<td><strong>astrocyte / glial imaging</strong></td>
<td>局所 neurotransmitter input に対する astrocyte network 応答や slow-state dynamics です。</td>
<td>Cahill らのように、minutes-long の glial network state を可視化し、slow-state / recovery modeling を一段強くできます。</td>
<td>全脳 coverage、cell-type-specific generalization、fast synaptic state、sleep-history と他 stack の完全統合は残ります。</td>
<td><strong>slow-state calibration と glia omission の禁止まで</strong>です。これだけで全脳 completeness は主張しません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="fmri-proxy-audit">
<h2 class="section-title">fMRI / BOLD を別扱いにする理由</h2>
<p>
現行サイトは fMRI を `blood-flow proxy` としては正しく扱えていました。しかし、技術・自然科学の観点では、それだけでは不十分でございます。重要なのは <strong>proxy であること</strong>そのものよりも、<strong>どの failure mode が BOLD の解釈 ceiling を作るか</strong>を提出物へ落とすことです。以下では、一次文献が比較的一貫して支持する 5 つの failure mode を固定します。
</p>
<table class="data-table">
<thead>
<tr>
<th>failure mode</th>
<th>一次文献が支持すること</th>
<th>このサイトでの読み替え</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>neural coupling target</strong></td>
<td><a href="https://doi.org/10.1038/35084005" target="_blank">Logothetis et al. (2001)</a> は BOLD が単純な multiunit output よりも局所場電位に強く結びつくことを示し、<a href="https://doi.org/10.1038/nature09108" target="_blank">Lee et al. (2010)</a> は cell type / wiring に応じて global / local fMRI signal が変わることを示しました。</td>
<td>BOLD 振幅を `spike count` や `local computation amount` と 1 対 1 に読みません。まず <strong>population-input-weighted neurovascular proxy</strong> として扱います。</td>
</tr>
<tr>
<td><strong>task / anticipatory haemodynamics</strong></td>
<td><a href="https://doi.org/10.1038/nature07664" target="_blank">Sirotin &amp; Das (2009)</a> は sensory cortex で local neuronal activity によって予測されない anticipatory haemodynamic signal を報告し、<a href="https://doi.org/10.1038/nn.3170" target="_blank">Cardoso et al. (2012)</a> は neuroimaging signal が stimulus-related component と task-related component の線形和として振る舞うことを示しました。</td>
<td>task-locked BOLD を、そのまま stimulus-driven computation と同一視しません。task structure や anticipation を covariate として別監査します。</td>
</tr>
<tr>
<td><strong>HRF timing heterogeneity</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">Handwerker et al. (2004)</a> は BOLD response が被験者・脳領域で大きく変動することを示し、<a href="https://doi.org/10.7554/eLife.86453" target="_blank">Bailes et al. (2023)</a> は resting-state fMRI signal に local hemodynamic response timing の spectral signature が残ることを示しました。</td>
<td>canonical HRF だけで onset 差、latency 差、spectral difference を mechanistic difference と読みません。region / subject / voxel ごとの transfer difference を残します。</td>
</tr>
<tr>
<td><strong>venous / non-neural spatial bias</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">Kay et al. (2019)</a> は sub-millimeter fMRI の data quality と venous effect を批判的に整理し、<a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">Kurzawski et al. (2022)</a> は同一被験者内でも non-neural factor が BOLD magnitude を左右することを示しました。</td>
<td>`細かい voxel map = 細かい neural map` とは読みません。laminar / sub-mm / large-vessel-near claim では venous / depth diagnostic を別提出物にします。</td>
</tr>
<tr>
<td><strong>BOLD-CMRO<sub>2</sub> discordance</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025)</a> は human cortex の calibrated fMRI で、BOLD と酸素代謝変化が有意 voxel の約40%で逆向きになりうることを示しました。</td>
<td>BOLD の符号や振幅だけを、そのまま local metabolic demand や energetic mechanism と読みません。代謝や機序の主張をする場合は calibrated BOLD、CMRO<sub>2</sub> 関連 readout、または明示的な棄権条件を追加します。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>このサイトでの運用ルール</strong>
<p>
fMRI を含む claim では、少なくとも <strong>(1) target neural claim</strong>、<strong>(2) HRF model granularity</strong>、<strong>(3) physiology / task-related nuisance</strong>、<strong>(4) venous / depth diagnostic</strong>、<strong>(5) metabolic / calibrated validator または abstention condition</strong> をセットで残します。これが無い場合、本サイトでは fMRI を <strong>broad coverage を与える hemodynamic proxy</strong> としては受理しても、fast mechanism や fine-grained localization の根拠には上げません。
</p>
</div>
</section>

<section class="section" id="state-variable-matrix">
<h2 class="section-title">state variable × timescale × observability matrix</h2>
<div class="note-box">
<strong>今回追加した批判軸</strong>
<p>
stack 別の ceiling 表だけでは、「何が見えていないか」は分かっても、<strong>どの state variable が、どの timescale で、どの route なら direct observation なのか</strong>までは固定できません。したがってここでは row を measurement stack ではなく <strong>state variable</strong> に切り替え、各行を <strong>direct</strong>、<strong>proxy / bridge</strong>、<strong>inferred / absent</strong> に分けます。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>state variable</th>
<th>支配 timescale / なぜ効くか</th>
<th>今日もっとも direct な route</th>
<th>direct と誤読されやすい proxy / bridge</th>
<th>このサイトでの運用上の結論</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cell identity / spatial placement</strong></td>
<td>日〜生涯の比較的安定な骨格で、cell class と spatial prior を与えます。</td>
<td>whole-brain spatial transcriptomics、Patch-seq、形態再構成です。</td>
<td>in vivo activity だけからの cell-type classifier、atlas prior の投影です。</td>
<td><strong>identity prior には direct</strong>ですが、current state や maintenance-state の直接観測には数えません。</td>
</tr>
<tr>
<td><strong>current synaptic efficacy / plastic history</strong></td>
<td>ms〜日で変わり、release probability、STP/LTP/LTD、recent plastic history が予測と介入応答を左右します。</td>
<td>局所 paired physiology、same-brain function + perturbation、coverage-limited な direct validation です。</td>
<td>EM synapse count、connectome-only model、cell-type label です。</td>
<td><strong>非破壊・全脳の direct route は未整備</strong>です。held-out perturbation gain が無ければ inferred のままにします。</td>
</tr>
<tr>
<td><strong>intrinsic excitability / homeostatic set point</strong></td>
<td>秒〜日で threshold / gain / recovery target を変え、縦断安定性と memory allocation に効きます。</td>
<td>局所 intracellular / patch、longitudinal perturbation と recovery log です。</td>
<td>短時間 firing-rate snapshot、cell-type label、decoder fit です。</td>
<td><strong>cross-day / recovery 記録が無ければ latent</strong>です。same-day fit を長期 stability へ延長しません。</td>
</tr>
<tr>
<td><strong>delay / myelin / axonal support</strong></td>
<td>ms〜週で位相、伝導遅延、学習後 timing を変えます。</td>
<td>伝導測定、myelin histology、oligodendrocyte-axon physiology です。</td>
<td>tract geometry、graph path length、fixed delay parameter です。</td>
<td><strong>timing-sensitive claim では delay-aware audit を必須</strong>にします。固定遅延だけなら ceiling を下げます。</td>
</tr>
<tr>
<td><strong>neuromodulatory specificity</strong></td>
<td>subsecond〜分で state gating と gain control を変え、release・clearance・receptor distribution の差で効果が局所化します。</td>
<td>local transmitter sensor、axon activity imaging、receptor / transporter atlas、receptor-specific physiology / pharmacology です。</td>
<td>pupil、locomotion、behaviour label、HRV、single global arousal proxy です。</td>
<td><strong>compartment（pupil / axon / sensor / receptor）、spatial scope、receptor family が無ければ proxy</strong>と書き、momentary internal state ground truth へ上げません。</td>
</tr>
<tr>
<td><strong>glial / metabolic slow-state</strong></td>
<td>秒〜時間で recovery、consolidation、metabolic support を左右します。</td>
<td>astrocyte / glia imaging、metabolic assay、slow-state covariate 記録です。</td>
<td>BOLD、broadband LFP / EEG envelope、行動状態だけのラベルです。</td>
<td><strong>neuron-only fit では slow-state completeness を主張しません</strong>。memory consolidation も別扱いにします。</td>
</tr>
<tr>
<td><strong>sleep / recovery regime</strong></td>
<td>時間〜日で overnight renormalization と regime recovery を決めます。</td>
<td>polysomnography、sleep staging、overnight recovery log、cross-day perturbation です。</td>
<td>same-day task fit、coarse vigilance label、短時間 resting-state 類似度です。</td>
<td><strong>same-day agreement を翌日安定性へ延長しません</strong>。sleep history が無ければ maintenance-state claim は弱めます。</td>
</tr>
<tr>
<td><strong>chronic unit identity / tissue response</strong></td>
<td>日〜月で longitudinal decode と same-neuron claim の妥当範囲を決めます。</td>
<td>probabilistic unit matching、drift correction、implant age と tissue-response audit です。</td>
<td>channel continuity、waveform 類似、manual curation だけの継続判定です。</td>
<td><strong>matching probability、dropout、tissue log が無ければ same-neuron claim を止めます</strong>。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>短い結論</strong>
<p>
Yao らと Gouwens / Gamlin らは主に <strong>cell identity</strong> 行を、MICrONS は局所的に <strong>synaptic efficacy / plastic history</strong> 行を、Hengen / Torrado Pacheco / Xu らは <strong>sleep / recovery regime</strong> 行を、Gibson / McKenzie / Looser らは <strong>delay / myelin / axonal support</strong> 行を、Neyhart らは <strong>neuromodulatory specificity</strong> 行を、Cahill / Suzuki らは <strong>glial / metabolic slow-state</strong> 行を、van Beest / Gregory らは <strong>chronic unit identity</strong> 行を押し上げました。重要なのは、<strong>これらが別々の行を押し上げている</strong>という点であり、1 本の multimodal stack が入っただけで全行が direct になった扱いはできません。
</p>
</div>
</section>

<section class="section" id="why-ceilings-differ">
<h2 class="section-title">なぜ ceiling がこれほど違うのか</h2>

<h3>1. atlas は identity を強くするが、current state を直接は与えません</h3>
<p>
Yao らは、whole mouse brain に対して scRNA-seq と MERFISH を組み合わせ、34 classes、338 subclasses、1,201 supertypes、5,322 clusters からなる高解像度 atlas を提示しました。これは cell-type taxonomy と spatial location の面で大きな前進です。しかし、ここから直接言えるのは <strong>その細胞がどの分子 class に属し、どこにいるか</strong>であり、<strong>今この瞬間の threshold、gain、synaptic efficacy、sleep-dependent renormalization、transmitter occupancy</strong> までは含みません。したがって atlas は非常に重要ですが、まず <strong>identity prior</strong> として読むのが安全でございます。
</p>

<h3>2. Patch-seq は bridge だが、coverage の壁を消しません</h3>
<p>
Gouwens らは transcriptomic family 内に morpho-electric variation が連続的に残ることを示し、Gamlin らは Patch-seq で定義された MET-type を large-scale EM へ写像して、Sst MET-type ごとの myelination と synaptic output の差を示しました。これは <strong>cell-type label だけでは足りず、electrophysiology と morphology を足す価値が大きい</strong>ことを意味します。一方で、Patch-seq は sparse で destructive な sampling であり、同一個体の全脳 current state や longitudinal history を与えるわけではありません。したがって、これは <strong>bridge</strong> であって <strong>whole-brain completeness</strong> ではございません。
</p>

<h3>3. 高密度 extracellular probe は local population window だが、unit identity と chronic horizon は自動では固定されません</h3>
<p>
Steinmetz らの Neuropixels 2.0 は motion correction により安定な長期記録を大きく前進させ、Pachitariu らの Kilosort4 は drift、low-norm units、split / merge error を含む現実的 benchmark を前提に spike sorting を改良しました。しかし、ここから直ちに「同じ neuron を長期間そのまま見ている」とは言えません。Trautmann らは、dense array では <strong>population dynamics のかなりの部分が spike sorting を介さなくても回収できる</strong>ことを示し、van Beest らは high-density probe の cross-day matching を <strong>probabilistic unit identification</strong> として実装しました。さらに Gregory らは、埋め込み array 周辺の deep-layer pyramidal neuron に structural / functional change が起こることを示しました。したがって、この stack の強みは <strong>implant region の local population readout</strong> であり、<strong>stable single-unit identity</strong> は別監査項目でございます。
</p>

<h3>4. EM connectome は scaffold だが、dynamic state を凍結しません</h3>
<p>
Dorkenwald らの adult fly whole-brain connectome は、約 5 × 10<sup>7</sup> chemical synapses と 139,255 neurons を再構成した巨大な前進です。しかし、EM が強いのは structural scaffold であり、current weight、release probability、neuromodulatory context、glial / metabolic background を直接測る方法ではありません。ここから導かれる批判は単純で、<strong>配線が分かった</strong>ことと<strong>その瞬間の生成的状態が分かった</strong>ことを同一視してはならない、という点でございます。
</p>

<h3>5. same-brain function を足すと縮退は減るが、全脳 state-complete には届きません</h3>
<p>
MICrONS は、同一脳で dense calcium imaging、行動状態、EM connectome を結びつけ、mouse visual cortex の multi-area functional connectomics を提示しました。これは connectome-only より一段強く、<strong>同じ脳での structure-function link</strong> を論じられる土台です。しかし、論文自体が扱うのは visual cortex の特定領域、特定課題、特定状態であり、そこから human whole-brain や all-state completeness へ飛躍することはできません。従って、この stack の ceiling は <strong>local functional twin</strong> です。
</p>

<div id="neuromodulatory-proxy-ladder"></div>
<h3>6. neuromodulatory observability は 1 本ではなく、proxy ladder として監査する必要があります</h3>
<p>
ここが今回もっとも深掘りして修正すべきだった点でございます。<a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> は瞳孔変動が皮質内の adrenergic と cholinergic activity の両方を追うことを示し、瞳孔径が <strong>mixed arousal proxy</strong> であることを明確にしました。さらに <a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">Lohani et al. (2022)</a> と <a href="https://doi.org/10.7554/eLife.86800.2" target="_blank">Collins et al. (2023)</a> は、cholinergic / noradrenergic axonal activity に cortex-wide の共通 signal がある一方で、局所には独立成分も残ることを示しました。<a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> は、cortical ACh dynamics が cholinergic axon activity と behavioral state からかなり予測できても、signal が近傍軸索からの距離と clearance kinetics に依存することを示しました。したがって、<strong>pupil</strong>、<strong>axon activity</strong>、<strong>local transmitter sensor</strong> は同じものを見ているわけではございません。
</p>
<p>
さらに、chemical specificity が上がっても、そこから直ちに functional effect の ground truth にはなりません。<a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a>、<a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">Goulas et al. (2021)</a>、<a href="https://doi.org/10.3389/fnana.2017.00078" target="_blank">Zilles &amp; Palomero-Gallagher (2017)</a> は、human / macaque cortex で receptor / transporter density が領域ごと・層ごとに大きく異なることを示しました。一方、human PET が直接与えるものも 1 本ではありません。<a href="https://doi.org/10.4088/JCP.12m08042" target="_blank">Wong et al. (2013)</a> は D<sub>2</sub> receptor occupancy PET が healthy subject における dose-dependent target engagement を与えることを示し、<a href="https://doi.org/10.1038/28364" target="_blank">Koepp et al. (1998)</a> と <a href="https://doi.org/10.1038/s41467-019-09897-z" target="_blank">Lippert et al. (2019)</a> は raclopride 系 PET で behavior / stimulus-linked dopamine release proxy を分オーダーで追えることを示しました。ただし、これらは ligand、receptor family、challenge、kinetic / displacement model に依存する <strong>receptor-specific proxy</strong> であり、momentary whole-brain transmitter field の直接読出しではございません。加えて <a href="https://doi.org/10.1038/ncomms12826" target="_blank">Verhoog et al. (2016)</a> と <a href="https://doi.org/10.1523/JNEUROSCI.1455-23.2024" target="_blank">Gulledge et al. (2024)</a> は、同じ cholinergic drive でも layer や projection class に応じて plasticity / output effect が変わることを示しています。したがって本サイトでは、<strong>receptor prior</strong>、<strong>occupancy / release PET</strong>、<strong>receptor-mediated causal effect</strong> を別ラダーとして扱います。
</p>
<table class="data-table">
<thead>
<tr>
<th>route</th>
<th>直接言えること</th>
<th>まだ残るもの</th>
<th>このサイトでの ceiling</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>mixed arousal proxy<br>(pupil / HRV / locomotion)</strong></td>
<td>覚醒・行動 state に結び付いた広域 covariate を出せます。</td>
<td>transmitter mixture、局所 release、receptor family、cell-type-specific effect は残ります。</td>
<td><strong>state covariate まで</strong>です。single-transmitter ground truth とは書きません。</td>
</tr>
<tr>
<td><strong>axon activity / innervation readout</strong></td>
<td>transmitter-line の activity と cortex-wide の共通 signal、局所独立成分の両方を監査できます。</td>
<td>extracellular concentration、clearance、receptor occupancy、downstream effect は残ります。</td>
<td><strong>transmitter-linked axonal proxy まで</strong>です。chemical field や effect size の ground truth とは書きません。</td>
</tr>
<tr>
<td><strong>local transmitter sensor</strong></td>
<td>sensor 近傍の release / clearance dynamics を局所 chemical proxy として読めます。</td>
<td>whole-brain field、receptor occupancy、projection-class-specific effect、region generalization は残ります。</td>
<td><strong>local chemical proxy まで</strong>です。momentary internal state 全体の直接観測とは書きません。</td>
</tr>
<tr>
<td><strong>receptor atlas / autoradiography</strong></td>
<td>どの領域・層・network axis で receptor / transporter density が変わりうるかという regional prior を与えます。</td>
<td>momentary release、current occupancy、trial-level fluctuation、局所 causal effect は残ります。</td>
<td><strong>regional receptor prior まで</strong>です。current neuromodulatory state と同一視しません。</td>
</tr>
<tr>
<td><strong>occupancy / release-sensitive PET</strong></td>
<td>選んだ ligand / receptor family / challenge 下で、regional target engagement や分オーダーの displacement proxy を与えます。</td>
<td>trial-level fluctuation、whole-brain momentary field、receptor-general inference、cell-type-specific effect は残ります。</td>
<td><strong>receptor- and paradigm-specific occupancy / release proxy まで</strong>です。momentary endogenous field や universal transmitter ground truth とは書きません。</td>
</tr>
<tr>
<td><strong>receptor-specific physiology / pharmacology</strong></td>
<td>その回路・その cell class における effect direction と timescale を局所 causal calibration として出せます。</td>
<td>全脳 coverage、別課題・別種への一般化、momentary whole-brain field は残ります。</td>
<td><strong>local causal calibration まで</strong>です。whole-brain completeness には上げません。</td>
</tr>
</tbody>
</table>

<h3>7. glia imaging は slow-state の omission を止めるが、neuromodulatory ladder の代わりにはなりません</h3>
<p>
<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> は、局所的な neurotransmitter input が broad astrocyte network へ minutes-long に符号化されることを示しました。これは glia を背景ノイズとして落とせないことを強く裏づけますが、同時に <strong>glial signal が neuromodulatory release や receptor state を完全に置き換えるわけではない</strong>ことも意味します。したがって本サイトでは、glia imaging を <strong>slow-state calibration</strong> として重視しつつ、neuromodulatory proxy ladder と混ぜて 1 本化しません。
</p>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">この批判から生じる実務ルール</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>augmentation claim には measurement stack を書く：</strong>「transcriptomic label を足した」ではなく、whole-brain atlas か Patch-seq bridge か same-brain link かを区別します。</li>
<li><strong>atlas / bridge / local population window / scaffold / local twin / proxy calibration を混ぜない：</strong>同じ「前進」でも、どの種類の前進かを固定します。</li>
<li><strong>latent state を 1 箱にしない：</strong>cell identity、synaptic efficacy、intrinsic excitability、delay / myelin、neuromodulation、glia、sleep / recovery、chronic unit identity を分け、dominant timescale を添えます。</li>
<li><strong>neuromodulation は compartment を書く：</strong>pupil / axon / sensor / receptor atlas / occupancy PET / displacement PET / pharmacology のどこを測ったかを明示し、chemical signal と receptor effect を混ぜません。</li>
<li><strong>multimodal を state-complete の同義語にしない：</strong>何の latent state が依然として残るかを本文に併記します。</li>
<li><strong>未観測状態を埋めるときは推定と書く：</strong>cell type から threshold / gain / set point を自動補完した場合は latent inference と明記します。</li>
<li><strong>sorted spike を stable neuron identity と書かない：</strong>chronic 記録では sorting version、drift correction、unit-match probability、dropout rate を別に残します。</li>
<li><strong>claim ceiling を超える表現を禁止する：</strong>たとえば EM だけで emulation-complete、Patch-seq だけで whole-brain state-complete、同一 shank の sorted unit だけで cross-day same-neuron claim、pupil だけで transmitter ground truth、receptor atlas だけで momentary release、occupancy / displacement PET だけで momentary whole-brain endogenous field とは書きません。</li>
</ul>
</div>
<table class="data-table">
<thead>
<tr>
<th>今ある stack</th>
<th>次に足すべきもの</th>
<th>一段強くなる主張</th>
<th>それでも止める主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG / fMRI</strong></td>
<td>外部 ground truth、侵襲記録、同一個体の構造/機能対応、介入応答です。</td>
<td>macro decode から weak L2 へ進む根拠が少し強くなります。</td>
<td>cell/synapse state の十分性、whole-brain WBE、state-complete claim は止めます。</td>
</tr>
<tr>
<td><strong>extracellular probes</strong></td>
<td>sorting benchmark、drift correction、unit-match probability、implant age / tissue-response log、cross-day validation です。</td>
<td>implant region の local population dynamics と chronic decode の validity horizon を少し強くできます。</td>
<td>stable same-neuron identity、whole-circuit ground truth、state-complete recording は止めます。</td>
</tr>
<tr>
<td><strong>whole-brain atlas</strong></td>
<td>Patch-seq、same-brain physiology、perturbation / recovery log です。</td>
<td>cell-type prior と spatial prior を局所 parameter prior へ接続しやすくなります。</td>
<td>current network state の十分性や longitudinal maintenance-state は止めます。</td>
</tr>
<tr>
<td><strong>volume EM</strong></td>
<td>same-brain function、cell-type bridge、perturbation、uncertainty 公開です。</td>
<td>structural scaffold から local conditional prediction へ進みやすくなります。</td>
<td>connectome-complete を emulation-complete と言い換えることは止めます。</td>
</tr>
<tr>
<td><strong>local transmitter / glia imaging</strong></td>
<td>coverage、stack 間校正、cross-state / cross-day validation です。</td>
<td>coarse proxy の妥当範囲と slow-state modeling を強くできます。</td>
<td>single-transmitter global field や whole-brain internal state の ground truth は止めます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124-138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <em>Nature</em>, 624, 317-332. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <em>Science</em>, 372(6539), eabf4588. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>Pachitariu, M., et al. (2024). Spike sorting with Kilosort4. <em>Nature Methods</em>, 21, 914-921. <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">doi:10.1038/s41592-024-02595-5</a></li>
<li>Trautmann, E. M., Stavisky, S. D., Lahiri, S., et al. (2019). Accurate estimation of neural population dynamics without spike sorting. <em>Neuron</em>, 103(2), 292-308.e4. <a href="https://doi.org/10.1016/j.neuron.2019.05.003" target="_blank">doi:10.1016/j.neuron.2019.05.003</a></li>
<li>van Beest, E. H., Jia, X., Deng, X., et al. (2024). Tracking neurons across days with high-density probes. <em>Nature Methods</em>. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
<li>Gregory, N. S., et al. (2023). Structural and functional changes of deep layer pyramidal neurons surrounding implanted microelectrode arrays in rat motor cortex. <em>Journal of Neural Engineering</em>, 20(4), 046022. <a href="https://doi.org/10.1088/1741-2552/ace8ac" target="_blank">doi:10.1088/1741-2552/ace8ac</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435-447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497-505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <em>Nature Communications</em>, 7, 13289. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Lohani, S., Moberly, A. H., Benisty, H., et al. (2022). Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. <em>Nature Neuroscience</em>, 25, 1706-1713. <a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">doi:10.1038/s41593-022-01202-6</a></li>
<li>Collins, L., Reddy, C. B., Neal, S., et al. (2023). Cholinergic and noradrenergic axonal activity contains a behavioral-state signal that is coordinated across the dorsal cortex. <em>eLife</em>, 12, RP86800. <a href="https://doi.org/10.7554/eLife.86800.2" target="_blank">doi:10.7554/eLife.86800.2</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <em>Nature Neuroscience</em>, 25, 1569-1580. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Goulas, A., Changeux, J.-P., Wagstyl, K., Amunts, K., Palomero-Gallagher, N., &amp; Hilgetag, C. C. (2021). The natural axis of transmitter receptor distribution in the human cerebral cortex. <em>Proceedings of the National Academy of Sciences</em>, 118(3), e2020574118. <a href="https://doi.org/10.1073/pnas.2020574118" target="_blank">doi:10.1073/pnas.2020574118</a></li>
<li>Zilles, K., &amp; Palomero-Gallagher, N. (2017). Multiple Transmitter Receptors in Regions and Layers of the Human Cerebral Cortex. <em>Frontiers in Neuroanatomy</em>, 11, 78. <a href="https://doi.org/10.3389/fnana.2017.00078" target="_blank">doi:10.3389/fnana.2017.00078</a></li>
<li>Wong, D. F., Kuwabara, H., Hsu, D. J., et al. (2013). D<sub>2</sub> receptor occupancy in the brains of healthy subjects by the novel atypical antipsychotic lurasidone. <em>Journal of Clinical Psychiatry</em>, 74(3), 305-310. <a href="https://doi.org/10.4088/JCP.12m08042" target="_blank">doi:10.4088/JCP.12m08042</a></li>
<li>Koepp, M. J., Gunn, R. N., Lawrence, A. D., et al. (1998). Evidence for striatal dopamine release during a video game. <em>Nature</em>, 393, 266-268. <a href="https://doi.org/10.1038/28364" target="_blank">doi:10.1038/28364</a></li>
<li>Lippert, R. N., Bolding, K. A., Abbott, L. F., et al. (2019). Time-dependent assessment of stimulus-evoked regional dopamine release. <em>Nature Communications</em>, 10, 336. <a href="https://doi.org/10.1038/s41467-019-09897-z" target="_blank">doi:10.1038/s41467-019-09897-z</a></li>
<li>Verhoog, M. B., Goriounova, N. A., Obermayer, J., et al. (2016). Mechanisms underlying the rules for associative plasticity at adult human neocortical synapses. <em>Nature Communications</em>, 7, 12826. <a href="https://doi.org/10.1038/ncomms12826" target="_blank">doi:10.1038/ncomms12826</a></li>
<li>Gulledge, A. T., et al. (2024). M1-type muscarinic receptors inhibit corticofugal pyramidal tract neurons to suppress layer 5 cortical output. <em>Journal of Neuroscience</em>, 44(10), e1455232024. <a href="https://doi.org/10.1523/JNEUROSCI.1455-23.2024" target="_blank">doi:10.1523/JNEUROSCI.1455-23.2024</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Neuroscience</em>, 27, 972-980. <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">doi:10.1038/s41593-023-01536-9</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <em>Cell</em>, 165(1), 180-191. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <em>Neuron</em>, 109(3), 530-544.e6. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <em>Nature Communications</em>, 17, 291. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <em>Science</em>, 344(6183), 1252304. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <em>Science</em>, 346(6207), 318-322. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <em>Nature Neuroscience</em>, 27, 1598-1609. <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">doi:10.1038/s41593-023-01558-3</a></li>
<li>Suzuki, A., et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. <em>Cell</em>, 144(5), 810-823. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">doi:10.1016/j.cell.2011.02.018</a></li>
<li>Logothetis, N. K., Pauls, J., Augath, M., Trinath, T., &amp; Oeltermann, A. (2001). Neurophysiological investigation of the basis of the fMRI signal. <em>Nature</em>, 412, 150-157. <a href="https://doi.org/10.1038/35084005" target="_blank">doi:10.1038/35084005</a></li>
<li>Lee, J. H., Durand, R., Gradinaru, V., et al. (2010). Global and local fMRI signals driven by neurons defined optogenetically by type and wiring. <em>Nature</em>, 465, 788-792. <a href="https://doi.org/10.1038/nature09108" target="_blank">doi:10.1038/nature09108</a></li>
<li>Sirotin, Y. B., &amp; Das, A. (2009). Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity. <em>Nature</em>, 457, 475-479. <a href="https://doi.org/10.1038/nature07664" target="_blank">doi:10.1038/nature07664</a></li>
<li>Cardoso, M. M. B. M., Sirotin, Y. B., Lima, B., Glushenkova, E., &amp; Das, A. (2012). The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components. <em>Nature Neuroscience</em>, 15, 1298-1306. <a href="https://doi.org/10.1038/nn.3170" target="_blank">doi:10.1038/nn.3170</a></li>
<li>Handwerker, D. A., Ollinger, J. M., &amp; D'Esposito, M. (2004). Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. <em>NeuroImage</em>, 21, 1639-1651. <a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">doi:10.1016/j.neuroimage.2003.11.029</a></li>
<li>Bailes, J., Millman, R., Franklin, C., et al. (2023). Resting-state fMRI signals contain spectral signatures of local hemodynamic response timing. <em>eLife</em>. <a href="https://doi.org/10.7554/eLife.86453" target="_blank">doi:10.7554/eLife.86453</a></li>
<li>Kay, K. N., Jamison, K. W., Zhang, R. Y., &amp; Uğurbil, K. (2019). A critical assessment of data quality and venous effects in sub-millimeter fMRI. <em>NeuroImage</em>, 189, 847-869. <a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">doi:10.1016/j.neuroimage.2019.02.006</a></li>
<li>Kurzawski, J. W., Yablonskiy, D. A., Pointer, R., et al. (2022). Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects. <em>Journal of Neuroscience</em>, 42, 7256-7266. <a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">doi:10.1523/JNEUROSCI.2532-21.2022</a></li>
<li>Epp, K. J., Lu, H., Lydon-Staley, D. M., et al. (2025). BOLD signal changes can oppose oxygen metabolism across the human cortex. <em>Nature Neuroscience</em>. <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
  <div class="sidebar-card">
    <h3>このページで固定すること</h3>
    <ul>
      <li>measurement stack ごとの直接観測量</li>
      <li>state variable ごとの timescale と direct / proxy / inferred</li>
      <li>stack ごとの latent state</li>
      <li>本サイトで許す claim ceiling</li>
    </ul>
  </div>

  <div class="sidebar-card">
    <h3>次に読む</h3>
    <ul>
      <li><a href="../verification.html#observability-budget">Observability Budget</a></li>
      <li><a href="../verification.html#state-completeness-gate">状態変数の完全性ゲート</a></li>
      <li><a href="../tech_roadmap.html#qa-m1">M1 観測変数</a></li>
      <li><a href="connectome-is-not-enough.html">配線図だけでは足りない理由</a></li>
      <li><a href="homeostatic-plasticity-and-maintenance-state.html">恒常性可塑性と維持状態</a></li>
    </ul>
  </div>
</aside>
</main>
