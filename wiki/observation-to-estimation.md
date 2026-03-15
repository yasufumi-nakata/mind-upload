---
layout: default
title: "Wiki：観測から推定へ"
description: "順問題、逆問題、ESI、DCM、SCM、因果同値類を、同定可能性と外部妥当化まで含めて整理します。"
article_type: Wiki
subtitle: "観測に合うこと、内部状態が分かること、因果が分かることは別です"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Technical / natural science only"
audience: "逆問題や因果モデルの限界を、一次文献ベースで整理したい人"
reading_time: "12〜18分"
page_intro: "このページは、EEG などの観測信号から脳内状態や因果構造を推定するときに、どこで主張が止まり、何を追加すると一段強く言えるかを整理する wiki です。順問題、逆問題、ESI、DCM、SCM、因果同値類を、『観測→推定→介入→妥当化』の順でつなぎます。"
accuracy_note: "ここで示すのは、どの手法を採用すべきかの固定レシピではありません。どの手法を使っても逃げられない監査項目を先に固定するページです。"
page_highlights:
  - "逆問題は solver 名だけでは評価せず、幾何・導電率・不確実性・外部妥当化まで監査します。"
  - "connectivity は localization の次の段であり、lagged metric だけで leakage 問題が消えるわけではありません。"
  - "DCM は自動発見器ではなく候補モデル比較であり、SCM は介入を記述しやすくする言語です。"
  - "観測データだけで残る因果同値類を、介入や較正でどこまで狭めるかが鍵です。"
known_points:
  - "頭皮 EEG から脳内活動を一意に決めることは原理的に難しく、推定には仮定が入ります。"
  - "高密度 EEG、個体別 MRI、FEM/BEM、経験ベイズ推定は条件を改善しえますが、単独で一意復元を保証しません。"
  - "source-space functional connectivity や directed connectivity は、source localization よりさらに強い仮定と妥当化を要します。"
  - "観測適合だけでは因果構造は確定せず、候補モデル集合と介入設計が必要です。"
unknown_points:
  - "どの計測・モデル化の組み合わせが WBE の検証に最も有効かは未確定です。"
  - "非侵襲計測だけで、どこまで詳細な因果構造や状態変数を安定に復元できるかは研究途中です。"
  - "どの leakage-control / direct-validation 組み合わせを source connectivity の site-wide 既定路線にするかは未確定です。"
  - "どの外部妥当化ラダーを site-wide benchmark に固定するかは、まだ整備途中です。"
wiki_links:
  - label: "Wiki: 計測からモデル化まで"
    url: "/wiki/measurement-and-modeling-terms.html"
    description: "計測、整理、推定、検証の全体マップへ戻れます。"
  - label: "Wiki: EEG前処理とQC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "推定の前段で、何が結果を変えるかを補います。"
  - label: "Wiki: 不確実性・校正・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "点推定ではなく幅と棄権条件をどう残すかを補います。"
  - label: "Wiki: 反事実・介入・摂動"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "観測適合から介入検証へ進む条件を補います。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
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
観測信号に合うモデルが見つかっても、それだけで <strong>内部状態が一意に分かった</strong>とも、<strong>因果構造が同定できた</strong>とも言えません。したがって、このサイトでは solver 名や理論名より先に、<strong>幾何・不確実性・候補モデル集合・外部妥当化</strong>の 4 点を監査します。
</p>
</div>

<div class="note-box">
<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。技術と自然科学の側面だけから、観測・推定・因果主張の境界を一次文献ベースで整理します。
</p>
</div>

<section class="section" id="audit-gates">
<h2 class="section-title">先に固定する 4 つの監査ゲート</h2>
<table class="data-table">
<thead>
<tr>
<th>監査ゲート</th>
<th>最低限ほしいもの</th>
<th>足りないと止まる主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1: 幾何と forward model</strong></td>
<td>電極座標、頭部モデル、導電率仮定、個体別 MRI の有無、感度分析。</td>
<td>解剖学的 source claim を強く言えません。</td>
</tr>
<tr>
<td><strong>Gate 2: 不確実性の可視化</strong></td>
<td>事後分布、信用区間、bootstrap/ensemble 幅、あるいは solver・前処理感度分析。</td>
<td>点推定だけで唯一解のように書くことができません。</td>
</tr>
<tr>
<td><strong>Gate 3: 候補モデル集合の明示</strong></td>
<td>比較したモデル空間、family 比較、同値類の残り方、棄権条件。</td>
<td>DCM や SCM を使っても、因果を一意発見したとは言えません。</td>
</tr>
<tr>
<td><strong>Gate 4: 外部妥当化・介入</strong></td>
<td>シミュレーション、ファントム、同時侵襲記録、頭蓋内刺激、刺激/病変/課題摂動の held-out 予測。</td>
<td>観測適合を、因果妥当化や一般化性能へ昇格できません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="levels">
<h2 class="section-title">観測・推定・因果検証を混ぜない</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>ここでしていること</th>
<th>この段階だけではまだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測</strong></td>
<td>頭皮や外側で見える信号を測ります。</td>
<td>脳内状態を一意に復元したとは言えません。</td>
</tr>
<tr>
<td><strong>推定</strong></td>
<td>頭部モデルや生成モデルを置いて、活動源や結合を推測します。</td>
<td>候補モデルの外側まで含めて真だとは言えません。</td>
</tr>
<tr>
<td><strong>介入・妥当化</strong></td>
<td>刺激、病変、課題変更、頭蓋内刺激、同時侵襲記録で予測を較正します。</td>
<td>これでもなお全脳 WBE の branch-equivalence までは言えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="forward-inverse">
<h2 class="section-title">順問題と逆問題</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>意味</th>
<th>監査で効く点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>順問題</strong></td>
<td>もし脳内にこの活動があるなら、頭皮ではどう見えるかを計算します。</td>
<td>頭部モデル、導電率、電極配置の仮定が前面に出ます。</td>
</tr>
<tr>
<td><strong>逆問題</strong></td>
<td>頭皮で見えた信号を説明しうる脳内活動を推定します。</td>
<td>複数解が同じ観測を作れるため、不確実性と感度分析が必須です。</td>
</tr>
</tbody>
</table>
<p>
逆問題が難しいのは、<strong>複数の内部状態が同じ観測を作れてしまう</strong>からです。したがって、ここで重要なのは「最良の 1 点」を強く主張することではなく、<strong>どの仮定でどこまで絞れたか</strong>を公開することでございます。
</p>
</section>

<section class="section" id="esi">
<h2 class="section-title">ESI は solver 名より、まず妥当化ラダーで読む</h2>
<p>
ESI は、頭皮信号から source を推定するための枠組みです。しかし、Mikulan らや Unnwongse らの直接妥当化研究が示す通り、source depth、頭蓋導電率、頭部モデル、電極幾何、solver の選び方で誤差は大きく変わります。したがって、<strong>「高密度 EEG だから」「Bayesian solver だから」だけでは強い主張はできません</strong>。
</p>
<table class="data-table">
<thead>
<tr>
<th>ESI で先に確認すること</th>
<th>なぜ重要か</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>幾何</strong></td>
<td>電極位置、個体別 MRI、FEM/BEM、導電率仮定が違うと source 誤差が変わります。</td>
</tr>
<tr>
<td><strong>不確実性</strong></td>
<td>経験ベイズや ensemble は有力ですが、必須なのは solver 名ではなく幅の可視化です。</td>
</tr>
<tr>
<td><strong>深部・微小 source の保留</strong></td>
<td>detectable と general reconstruction は別であり、深部一般化は保留条件が必要です。</td>
</tr>
<tr>
<td><strong>外部妥当化</strong></td>
<td>シミュレーション、ファントム、同時侵襲記録、頭蓋内刺激のどこで較正したかが必要です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>このサイトでの読み替え</strong>
<p>
Bayesian / empirical Bayes / sparse Bayesian learning は、<strong>不確実性を伴う推定</strong>として有力な候補です。ただし、本サイトでは「ベイズだから採用」ではなく、<strong>不確実性をどの形で公開し、どの外部基準で較正したか</strong>を採否条件にします。
</p>
</div>
</section>

<section class="section" id="connectivity-gates">
<h2 class="section-title">connectivity は localization の次の段です</h2>
<p>
ここが従来の site でまだ弱かった境界です。source を推定できたとしても、その上に functional connectivity や directed connectivity を載せると、主張はもう 1 段強くなります。なぜなら、reference、source mixing、parcellation、metric choice、stationarity 仮定が、局在誤差とは別の失敗モードを増やすからです。
</p>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>ここで言えること</th>
<th>この段階だけではまだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>sensor-space functional connectivity</strong></td>
<td>指定した reference と前処理の下で、頭皮チャネル間の位相・振幅関係を要約できます。</td>
<td>anatomical coupling や source-level network を直接見たとは言えません。</td>
</tr>
<tr>
<td><strong>source-space functional connectivity</strong></td>
<td>forward / inverse model と parcellation を通して、皮質近傍の相互関係をより解釈しやすくできます。</td>
<td>ghost interaction や leakage が消えたとは言えず、真の inter-areal coupling を一意に回収したとは書けません。</td>
</tr>
<tr>
<td><strong>directed / effective connectivity</strong></td>
<td>Granger、DTF、STE、DCM などで、時間順序や候補モデルに依存した directed influence を比較できます。</td>
<td>metric が一致しただけで causal mechanism や唯一の回路図を同定したとは言えません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 の一次文献が切る境界</strong>
<p>
Vinck らの wPLI は volume-conduction、noise、sample-size bias を減らす候補ですが、Zhang らは scalp EEG functional network が reference choice で動くことを示しました。さらに Palva らは source reconstruction 後にも ghost interaction が残りうると警告し、Haufe らの simulation study は directed connectivity measure 間で結論が割れうることを示しました。一方、Papadopoulou らは同時 cortical recording と reconstructed source の controlled comparison で qualitative な directed pattern の一致を示し、Hao らは simultaneous SEEG/HD-EEG で外部妥当化の道筋を前進させました。したがって、本サイトでは <strong>lagged metric = leakage solved</strong>、<strong>directed metric = causality solved</strong> とは読みません。
</p>
</div>
</section>

<section class="section" id="dcm">
<h2 class="section-title">DCM は「真の因果を自動発見する装置」ではありません</h2>
<p>
DCM は、候補となる生成モデルを明示し、その中でどれが観測を説明しやすいかを比較する枠組みです。Friston らの原論文と Penny らのモデル比較研究が示す通り、DCM の結論は <strong>比較に入れた候補モデル空間</strong>に依存します。したがって、モデル比較で勝ったことは「候補集合の中では良い」という意味であり、<strong>世界で唯一正しい</strong>ことを意味しません。
</p>
<div class="key-points">
<h4>DCM を読むときの 4 点</h4>
<ul>
<li><strong>候補モデル空間：</strong>どのノードと結合候補を最初から比較対象に入れたか。</li>
<li><strong>family 比較：</strong>細部でなく上位 family が安定しているか。</li>
<li><strong>model recovery：</strong>シミュレーションで正解モデルを回収できるか。</li>
<li><strong>介入較正：</strong>刺激や摂動で held-out 予測が当たるか。</li>
</ul>
</div>
</section>

<section class="section" id="scm">
<h2 class="section-title">SCM と因果発見は、介入が入って初めて強くなる</h2>
<p>
SCM は、介入や反事実を明示的に書き下ろしやすい枠組みです。しかし、観測データだけから学ぶ場合、しばしば <strong>Markov equivalence class</strong> が残ります。Hauser と Buhlmann が示したように、介入データはこの同値類を狭めるために重要です。脳データでも、Vink らは resting-state functional connectivity が causal interaction の弱い予測子にとどまることを示しており、相関だけで方向や機序を確定するのは危険でございます。
</p>
<div class="note-box">
<strong>SCM と DCM の役割差</strong>
<p>
DCM は神経回路の候補生成モデル比較、SCM は介入・反事実を表現する言語として有用です。どちらも重要ですが、どちらか 1 つを入れたから因果が自動で確定するわけではありません。
</p>
</div>
</section>

<section class="section" id="validation">
<h2 class="section-title">一段強い主張へ進むための外部妥当化ラダー</h2>
<table class="data-table">
<thead>
<tr>
<th>妥当化ラダー</th>
<th>何が分かるか</th>
<th>まだ残る限界</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>シミュレーション</strong></td>
<td>solver や model recovery の下限性能を見られます。</td>
<td>現実の頭部幾何や生体ノイズを完全には再現しません。</td>
</tr>
<tr>
<td><strong>ファントム</strong></td>
<td>幾何と forward model の妥当性を較正できます。</td>
<td>生体の可塑性や state dependence はありません。</td>
</tr>
<tr>
<td><strong>同時侵襲・非侵襲記録</strong></td>
<td>局所 ground truth に近い比較ができます。</td>
<td>coverage-limited で、全脳 ground truth ではありません。</td>
</tr>
<tr>
<td><strong>頭蓋内刺激・摂動</strong></td>
<td>介入応答と時間順序の検証ができます。</td>
<td>刺激条件と観測窓の設計に強く依存します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-rules">
<h2 class="section-title">このサイトで採用する運用ルール</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>solver 名を標準とは書かない：</strong>Bayesian solver、minimum norm、DCM、SCM は候補であり、採否は監査項目で決めます。</li>
<li><strong>観測適合だけで因果主張を上げない：</strong>介入または外部妥当化がない場合は、同値類や候補モデルレベルに留めます。</li>
<li><strong>connectivity を localization の延長と書かない：</strong>network claim には、reference / leakage / parcellation / metric assumptions の別監査を入れます。</li>
<li><strong>lagged / directed 指標を免罪符にしない：</strong>wPLI、Granger、DTF、STE、DCM は候補であり、source leakage や causal identifiability を自動で解決しません。</li>
<li><strong>深部や細粒度は保留条件つきで書く：</strong>detectable と robust reconstruction を混同しません。</li>
<li><strong>不確実性が広いときは棄権する：</strong>解が重なるなら、無理に 1 つへ潰さず保留を明示します。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Wipf, D., &amp; Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging. <em>NeuroImage</em>, 44(3), 947-966. <a href="https://doi.org/10.1016/j.neuroimage.2008.02.059" target="_blank">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(1), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging extended E/MEG source activation with empirical Bayesian uncertainty quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Vinck, M., Oostenveld, R., van Wingerden, M., et al. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>, 55(4), 1548-1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Zhang, L., Wang, P., Zhang, R., et al. (2020). The Influence of Different EEG References on Scalp EEG Functional Network Analysis During Hand Movement Tasks. <em>Frontiers in Human Neuroscience</em>, 14, 367. <a href="https://doi.org/10.3389/fnhum.2020.00367" target="_blank">doi:10.3389/fnhum.2020.00367</a></li>
<li>Palva, J. M., Wang, S. H., Palva, S., et al. (2018). Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <em>NeuroImage</em>, 173, 632-643. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: A simulation study. <em>NeuroImage</em>, 64, 120-133. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Papadopoulou, M., Friston, K., &amp; Marinazzo, D. (2019). Estimating Directed Connectivity from Cortical Recordings and Reconstructed Sources. <em>Brain Topography</em>, 32(4), 741-752. <a href="https://doi.org/10.1007/s10548-015-0450-6" target="_blank">doi:10.1007/s10548-015-0450-6</a></li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <em>NeuroImage</em>, 19(4), 1273-1302. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Lee, H.-L., Zahneisen, B., Hugger, T., et al. (2017). Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. <em>NeuroImage</em>, 149, 441-451. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.012" target="_blank">doi:10.1016/j.neuroimage.2017.02.012</a></li>
<li>Hauser, A., &amp; Buhlmann, P. (2012). Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. <em>Journal of Machine Learning Research</em>, 13, 2409-2464. <a href="https://jmlr.org/papers/v13/hauser12a.html" target="_blank">JMLR</a></li>
<li>Vink, J. J., Ramos-Nuñez, A. I., Bellesi, A., et al. (2020). The brain's functional connectome is a poor predictor of the brain's causal activity flow. <em>PLOS Computational Biology</em>, 16(1), e1007866. <a href="https://doi.org/10.1371/journal.pcbi.1007866" target="_blank">doi:10.1371/journal.pcbi.1007866</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="measurement-and-modeling-terms.html">計測からモデル化まで →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">不確実性・校正・棄権 →</a></li>
<li><a href="counterfactual-and-perturbation-verification.html">反事実・介入・摂動 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../tech_roadmap.html#qa-r1">R1 逆問題 →</a></li>
</ul>
</div>
</aside>
</main>
