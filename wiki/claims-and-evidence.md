---
layout: default
title: "Wiki：主張と証拠の読み方"
description: "Mind-Upload や脳科学のニュースを、主張の強さ・計測スタック・検証経路で読み分けるための基礎ページです。"
article_type: Wiki
subtitle: "派手な文言を、measurement ceiling と validation route まで分解して読む"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Reading guide (technical / natural science emphasis)"
audience: "ニュースや研究発表を読み違えたくない人、L0〜L5 を measurement ceiling まで含めてつかみたい人"
reading_time: "12〜18分"
page_intro: "このページは、脳科学や Mind-Upload の話で出てくる強い言い方を、主張の強さだけでなく、何を直接見ていて何がまだ latent か、どんな検証経路が通っているかまで含めて読むためのガイドです。"
accuracy_note: "ここで整理するのは安全側の読み方です。可能性を否定するためではなく、直接観測、推定、補助仮説、未解決点を混ぜないために行います。"
page_highlights:
  - "同じ L1 や L2 でも、measurement stack が違えば claim ceiling も違います。"
  - "高い score だけでは、localization、causality、stable single-unit identity、emulation-complete を主張できません。"
  - "主張を 1 段上げるには、direct validation、perturbation、longitudinal maintenance audit が別に必要です。"
known_points:
  - "出力が当たることと、内部の仕組みが正しいことは別です。"
  - "measurement stack ごとに、直接観測量と latent state は異なります。"
  - "chronic invasive recording や connectome reconstruction にも、それぞれ固有の監査上限があります。"
unknown_points:
  - "どこまで multimodal 統合で non-invasive measurement ceiling を押し上げられるかは未確定です。"
  - "長期 claim に必要な maintenance-state artifact pack の最小構成はまだ固定されていません。"
  - "どの evidence bundle で continuity claim を受理するかも、なお研究・運用の課題です。"
wiki_links:
  - label: "Wiki: 計測スタックごとの observability と claim ceiling"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "どの measurement stack が何を直接見て、どこで主張上限に当たるかを整理します。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "観測、推定、localization、directed connectivity をどう分けて読むかを補います。"
  - label: "Wiki: 配線図だけでは足りない理由"
    url: "/wiki/connectome-is-not-enough.html"
    description: "connectome-complete を emulation-complete と読まない理由を整理します。"
  - label: "Wiki: state・trait・ドリフト"
    url: "/wiki/state-trait-and-drift.html"
    description: "chronic recording や longitudinal claim で何を監査するかを補います。"
recommended_pages:
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "論文集"
    url: "/mind_uploading_papers.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>基本ルール</h2>
<p>
研究発表の文言は、しばしば実際の証拠より強く見えます。そこでこのサイトでは、まず <strong>主張の強さ</strong> を L0〜L5 で置き、次に <strong>何を直接見たのか</strong> と <strong>何がまだ latent か</strong> を分け、最後に <strong>どんな検証経路を通ったのか</strong> を確認します。これを飛ばすと、L1 のスコアや局所観測を、そのまま L2/L3/L4 の主張へ読み替えてしまいます。
</p>
</div>

<div class="note-box">
<strong>2026-03 の技術更新</strong>
<p>
このページは、simultaneous SEEG/HD-EEG による source validation、high-density extracellular probe の chronic unit identity audit、connectome の外に残る maintenance-state 文献を反映し、単なる「強い/弱い」ではなく <strong>measurement ceiling と upgrade gate</strong> まで読む構成へ更新しました。
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">L0〜L5 を、主張の強さと upgrade 条件で読む</h2>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>実際に近い意味</th>
<th>最低限ほしい証拠</th>
<th>それだけではまだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>同じ解析を第三者がもう一度回せる</td>
<td>データ、コード、環境、version、ログがそろい、再現実行できることです。</td>
<td>generalization、mechanism、causality、identity claim までは言えません。</td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>ある measurement stack で、条件つきの予測や復元ができる</td>
<td>ベースライン比較、リーク検査、hold-out 条件、score の不確実性、claim ceiling の明記です。</td>
<td>高 score だけでは localization、causal mechanism、state-complete reconstruction は言えません。</td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>条件変更、外部基準、限定的な perturbation に対しても成立する</td>
<td>held-out condition、counterfactual、external validation、family comparison のいずれかです。</td>
<td>長期維持、cross-day stability、same-neuron identity、personhood までは自動では上がりません。</td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>閉ループで、明示した遅延・安全条件の範囲内では安定に動く</td>
<td>real-time latency/jitter log、安全停止、abstention、failure mode、deployment horizon です。</td>
<td>短期の closed-loop 成功だけでは、longitudinal maintenance や本人性は言えません。</td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>連続性や本人性に踏み込む</td>
<td>事前登録した continuity test、branch case、記憶・価値観・学習の分岐検査です。</td>
<td>制度運用や社会実装の成立までは含みません。</td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>社会で運用可能だと主張する</td>
<td>監査、停止基準、責任分界、制度設計、長期安全運用です。</td>
<td>このページの技術・自然科学整理だけで確定できる範囲を超えます。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>重要な読み替え禁止</strong>
<p>
<strong>L1 の結果がある</strong>ことと、<strong>L1 の中で measurement ceiling が高い</strong>ことは別です。さらに、L1 の ceiling が高いことと、L2/L3/L4 へ上がれることも別でございます。
</p>
</div>
</section>

<section class="section" id="stack-ceiling">
<h2 class="section-title">同じ L1 でも、計測スタックが違えば claim ceiling も違います</h2>
<table class="data-table">
<thead>
<tr>
<th>よくある成果</th>
<th>直接見えているもの</th>
<th>まだ latent のもの</th>
<th>安全側の上限</th>
<th>1 段上げる条件</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>scalp EEG で decode が当たる</strong></td>
<td>頭皮電位の時系列、sensor-space の統計的差です。</td>
<td>source mixing、reference 依存性、局所回路、subcortical state、maintenance-state です。</td>
<td>sensor-level correlational readout までに留めます。</td>
<td>external ground truth、direct validation、perturbation、source-level の construct validation が必要です。</td>
</tr>
<tr>
<td><strong>HD-EEG source imaging が SEEG と対応する</strong></td>
<td>特定 cohort・特定条件での source estimate と invasive reference の対応です。</td>
<td>coverage 外の部位、cohort 外一般化、depth / power dependence、whole-brain state completeness です。</td>
<td>validated localization route の前進までは言えます。</td>
<td>別 cohort での追試、perturbation、縦断再現、task family 拡張が要ります。</td>
</tr>
<tr>
<td><strong>high-density extracellular probe で units を長期追跡した</strong></td>
<td>implant 近傍の spike waveform、threshold crossing、local population dynamics です。</td>
<td>same neuron across days の確実性、sorting / matching error、probe drift、tissue response、未記録回路です。</td>
<td>stated validity horizon を持つ local population window までが安全です。</td>
<td>unit-match probability、dropout/new-unit rate、implant age、tissue-response proxy の監査が必要です。</td>
</tr>
<tr>
<td><strong>connectome と cell type atlas がそろった</strong></td>
<td>構造 graph、細胞型ラベル、局所形態の一部です。</td>
<td>synaptic weights、delay / myelin、intrinsic excitability、sleep-homeostasis、glial / metabolic support です。</td>
<td>structural scaffold の前進までは言えます。</td>
<td>同一脳での functional / perturbational / longitudinal validation と maintenance-state 監査が必要です。</td>
</tr>
</tbody>
</table>

<p>
ここで重要なのは、<a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">Vinck et al. (2011)</a> が示した wPLI は <strong>volume-conduction、noise、sample-size bias を減らす候補</strong>であって免罪符ではないこと、<a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">Haufe et al. (2013)</a> と <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">Palva et al. (2018)</a> が connectivity interpretation の不安定さを示していること、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> が source validation route を前進させても whole-brain state-complete measurement を与えたわけではないことです。さらに <a href="https://doi.org/10.1126/science.abf4588" target="_blank">Steinmetz et al. (2021)</a> と <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">van Beest et al. (2024)</a> は chronic probe の前進を示しましたが、そこでも `same neuron` は audit 付きの主張です。
</p>

<p>
また、<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a>、<a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>、<a href="https://doi.org/10.1038/s41593-023-01517-y" target="_blank">Looser et al. (2024)</a>、<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> から本サイトが引く <strong>推論</strong> は、`connectome-complete` をそのまま `emulation-complete` と読んではならない、という点でございます。これは structural scaffold の価値を否定するのではなく、hidden state がまだ残ることを明示するためです。
</p>
</section>

<section class="section" id="headline-translation">
<h2 class="section-title">見出しを technical route に翻訳する</h2>
<table class="data-table">
<thead>
<tr>
<th>見出しの言い方</th>
<th>安全側の読み方</th>
<th>次に確認すべきこと</th>
<th>まず置くレベル</th>
</tr>
</thead>
<tbody>
<tr>
<td>「脳から文章を復元した」</td>
<td>多くは stated setup 内の decoding です。</td>
<td>hold-out 条件、language prior の寄与、OOD、abstention、failure case を見ます。</td>
<td><strong>L1</strong> です。</td>
</tr>
<tr>
<td>「EEG で脳内ネットワークを可視化した」</td>
<td>sensor-space か、限定つき source estimate の話かを分けます。</td>
<td>reference、source validation、ghost interaction、directed metric の根拠を見ます。</td>
<td><strong>L1</strong>、良くて限定つき <strong>L2</strong> です。</td>
</tr>
<tr>
<td>「Neuropixels で同じ神経細胞を何週間も追跡した」</td>
<td>local population window と probabilistic unit tracking の前進です。</td>
<td>unit-match probability、sorting version、probe drift、tissue response を見ます。</td>
<td><strong>L1〜L2</strong> です。</td>
</tr>
<tr>
<td>「コネクトームが完成し、WBE に近づいた」</td>
<td>structural scaffold の前進です。</td>
<td>weights、delay / myelin、sleep-homeostasis、glial / metabolic support、perturbation validation を見ます。</td>
<td><strong>L1 の準備</strong> であり、emulation-complete 宣言ではありません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="upgrade-gates">
<h2 class="section-title">主張を 1 段上げる前の 3 ゲート</h2>
<table class="data-table">
<thead>
<tr>
<th>ゲート</th>
<th>なぜ必要か</th>
<th>通らないときの扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Direct validation</strong></td>
<td>proxy が本当に target state と対応しているかを、外部 ground truth や同時侵襲記録で確かめるためです。</td>
<td>proxy-based correlate として扱い、localization や mechanism claim を上げません。</td>
</tr>
<tr>
<td><strong>2. Perturbation / counterfactual</strong></td>
<td>相関だけでは、別の内部機序でも同じ出力が出る可能性が残るためです。</td>
<td>predictive association に留め、causal explanation とは書きません。</td>
</tr>
<tr>
<td><strong>3. Longitudinal maintenance audit</strong></td>
<td>same-day fit と cross-day stability、short-term success と maintenance-state 一致は別問題だからです。</td>
<td>stated horizon つきの短期 claim に留め、長期維持や stable identity を主張しません。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>この 3 ゲートは代替関係ではありません</strong>
<p>
たとえば direct validation があっても、perturbation が無ければ causal route は弱いままです。長期追跡があっても maintenance-state の監査が無ければ、same-day success を cross-day equivalence へは上げられません。
</p>
</div>
</section>

<section class="section" id="checklist">
<h2 class="section-title">読むときの短い checklist</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>何を直接見たのか：</strong>sensor、source、spike、structure のどれかを先に分けます。</li>
<li><strong>何がまだ latent か：</strong>unmeasured state、source mixing、unit identity、maintenance-state を列挙します。</li>
<li><strong>どの upgrade gate を通ったか：</strong>direct validation、perturbation、longitudinal audit の有無を見ます。</li>
<li><strong>何が出たら失敗か：</strong>反証条件、abstention 条件、stated validity horizon があるかを確認します。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
measurement stack の差を詳しく見たい場合は <a href="measurement-stack-and-claim-ceiling.html">計測スタックごとの observability と claim ceiling</a>、観測から source / connectivity / mechanism へ何段飛ぶのかを見たい場合は <a href="observation-to-estimation.html">観測から推定へ</a>、connectome の不足を深掘りしたい場合は <a href="connectome-is-not-enough.html">配線図だけでは足りない理由</a>、長期 drift や chronic recording の読み方を見たい場合は <a href="state-trait-and-drift.html">state・trait・ドリフト</a> をご覧ください。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>この読み方を標準・ベンチ・登録・監査へ戻したい場合はこちらです。</p>
<a href="verification-basics.html">検証基盤の基本へ →</a>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., &amp; Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>, 55(4), 1548-1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: A simulation study. <em>NeuroImage</em>, 64, 120-133. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva, J. M., Wang, S. H., Palva, S., Zhigalov, A., Monto, S., Brookes, M. J., Schoffelen, J.-M., &amp; Jerbi, K. (2018). Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <em>NeuroImage</em>, 173, 632-643. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <em>Science</em>, 372(6539), eabf4588. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>van Beest, E. H., Bimbard, C., Fabre, J. M. J., et al. (2024). Tracking neurons across days with high-density probes. <em>Nature Methods</em>, 21, 2071-2080. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <em>Neuron</em>, 109(3), 530-544.e6. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <em>Nature Neuroscience</em>, 27, 1584-1598. <a href="https://doi.org/10.1038/s41593-023-01517-y" target="_blank">doi:10.1038/s41593-023-01517-y</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="measurement-stack-and-claim-ceiling.html">計測スタックごとの observability と claim ceiling →</a></li>
<li><a href="observation-to-estimation.html">観測から推定へ →</a></li>
<li><a href="connectome-is-not-enough.html">配線図だけでは足りない理由 →</a></li>
<li><a href="state-trait-and-drift.html">state・trait・ドリフト →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
<li><a href="../verification.html">Verification →</a></li>
<li><a href="../mind_uploading_papers.html">論文集 →</a></li>
</ul>
</div>
</aside>
</main>
