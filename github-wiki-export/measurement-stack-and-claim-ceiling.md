# Wiki：計測スタックごとの observability と claim ceiling

> multimodal は『全部見えた』の同義語ではありません
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: Technical / natural science only

## このページの役割
このページは、WBE の議論で見落としやすい『measurement stack ごとの主張上限』を固定する wiki です。hidden state が重要だというだけでは足りません。EEG/MEG/fMRI、spatial transcriptomics、Patch-seq、volume EM、same-brain functional connectomics、local transmitter / glia imaging が、それぞれ何を直接観測し、何をまだ latent に残すのかを、一次文献ベースで整理します。

## 正確さの前提
以下の『claim ceiling』列は、各論文がそのまま宣言している結論ではありません。一次文献が直接観測した変数と、依然として未観測の状態変数から本サイトが引く運用上の推論でございます。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: 配線図だけでは足りない理由](https://github.com/yasufumi-nakata/mind-upload/wiki/connectome-is-not-enough) - 何の状態変数が抜けるかを先に整理したページです。
- [Wiki: 恒常性可塑性と維持状態](https://github.com/yasufumi-nakata/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state) - 長期 maintenance-state の側から不足変数を深掘りします。
- [Wiki: マルチモーダル統合の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/multimodal-integration-basics) - EEG/MEG/fMRI/侵襲記録の統合監査を詳しく見たいときはこちらです。
- [Wiki: 観測から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 観測値と latent state 推定を混同しないための入口です。

## いま分かっていること
- EEG/MEG/fMRI はマクロな proxy を与えますが、細胞型、シナプス効率、神経修飾場、グリア状態を直接は与えません。
- whole-brain spatial transcriptomics は cell-type taxonomy と空間配置を大きく前進させますが、動的状態の十分性は別問題です。
- Patch-seq と same-brain connectomics は縮退を減らしますが、全脳 coverage と長期 maintenance-state の十分性は残ります。
- local transmitter / glia imaging は coarse proxy の校正に有効ですが、そのまま全脳 ground truth にはなりません。

## まだ分かっていないこと
- どの stack の組み合わせが WBE に対して最も効率よく縮退を減らすかは、まだ固定できません。
- 同一脳・全脳・長期縦断で、どの latent state まで取得すべきかの十分条件は未確定です。
- stack 間の augmentation 順序をどう最適化するかも、課題・種・時定数ごとに変わり得ます。

---

<h2>いちばん短い結論</h2>
<p>
現行サイトの弱点は、<strong>重要な state は列挙できても、どの measurement stack が何を直接観測し、どこで主張上限に当たるか</strong>が前面に出ていなかった点でございました。一次文献を並べると、EEG/MEG/fMRI はマクロ state の tracking、whole-brain spatial atlas は cell-type と空間配置、Patch-seq は cell-type と morpho-electric phenotype の橋渡し、volume EM は structural scaffold、same-brain functional connectomics は局所 conditional prediction、local transmitter / astrocyte imaging は coarse proxy の較正を強くします。しかし、<strong>どの stack も単独では state-complete reconstruction を与えません</strong>。したがって本サイトでは、measurement stack ごとに claim ceiling を明記し、そこを超える表現を禁止します。
</p>

<strong>このページの範囲</strong>
<p>
ここでは哲学、法制度、本人性は扱いません。扱うのは、技術と自然科学の側面だけから見た「どの観測で何が直接見えて、何がまだ latent か」という問題です。
</p>

<h2>今回深掘りする弱点</h2>
<p>
従来の公開ページは、connectome だけでは足りないこと、maintenance-state が残ること、augmentation / ablation で比較すべきことを既に押さえていました。しかし、それだけでは読者が <strong>multimodal</strong>、<strong>atlas</strong>、<strong>same-brain</strong> という語を見たときに、「かなり全部見えた」と過大解釈する余地が残ります。弱点は、<strong>state variable の議論</strong>と<strong>measurement stack の議論</strong>がまだ十分に一体化していなかったことでございます。
</p>
<p>
そこで本ページでは、各 stack の直接観測量、何を少し強く言えるか、何が依然として latent state として残るか、そしてこのサイトで許す <strong>claim ceiling</strong> を 1 つの表に統合します。
</p>

<h2>計測スタックごとの observability と claim ceiling</h2>

<strong>読み方</strong>
<p>
下の表の最後の列は、各論文の要約ではなく、本サイトの運用ルールです。つまり、<strong>その stack が直接観測した変数</strong>と、<strong>依然として未観測の状態変数</strong>から引く、根拠付きの主張上限でございます。
</p>

<table>
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
<td>血行動態 proxy と、領域スケールの遅い network state です。</td>
<td>広域 coverage、recruitment pattern、比較的遅い state occupancy を同一個体内で追えます。</td>
<td>ms timing、興奮/抑制の分離、局所 transmitter dynamics、current synaptic efficacy は直接は見えません。</td>
<td><strong>広域 state atlas と coarse dynamical constraint まで</strong>です。速い causal mechanism や microstate の十分性は主張しません。</td>
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
<td>局所 transmitter dynamics と、その axon activity / pupil / locomotion との関係です。</td>
<td>Neyhart らのように、coarse arousal proxy が何をどこまで代表するかを較正し、transmitter-linked covariate を少し強くできます。</td>
<td>全脳の transmitter field、受容体状態、region-generalizable ground truth、long-timescale maintenance-state は残ります。</td>
<td><strong>限定つき covariate / proxy calibration まで</strong>です。single-transmitter ground truth や全脳 internal state とは書きません。</td>
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

<h2>なぜ ceiling がこれほど違うのか</h2>

<h3>1. atlas は identity を強くするが、current state を直接は与えません</h3>
<p>
Yao らは、whole mouse brain に対して scRNA-seq と MERFISH を組み合わせ、34 classes、338 subclasses、1,201 supertypes、5,322 clusters からなる高解像度 atlas を提示しました。これは cell-type taxonomy と spatial location の面で大きな前進です。しかし、ここから直接言えるのは <strong>その細胞がどの分子 class に属し、どこにいるか</strong>であり、<strong>今この瞬間の threshold、gain、synaptic efficacy、sleep-dependent renormalization、transmitter occupancy</strong> までは含みません。したがって atlas は非常に重要ですが、まず <strong>identity prior</strong> として読むのが安全でございます。
</p>

<h3>2. Patch-seq は bridge だが、coverage の壁を消しません</h3>
<p>
Gouwens らは transcriptomic family 内に morpho-electric variation が連続的に残ることを示し、Gamlin らは Patch-seq で定義された MET-type を large-scale EM へ写像して、Sst MET-type ごとの myelination と synaptic output の差を示しました。これは <strong>cell-type label だけでは足りず、electrophysiology と morphology を足す価値が大きい</strong>ことを意味します。一方で、Patch-seq は sparse で destructive な sampling であり、同一個体の全脳 current state や longitudinal history を与えるわけではありません。したがって、これは <strong>bridge</strong> であって <strong>whole-brain completeness</strong> ではございません。
</p>

<h3>3. EM connectome は scaffold だが、dynamic state を凍結しません</h3>
<p>
Dorkenwald らの adult fly whole-brain connectome は、約 5 × 10<sup>7</sup> chemical synapses と 139,255 neurons を再構成した巨大な前進です。しかし、EM が強いのは structural scaffold であり、current weight、release probability、neuromodulatory context、glial / metabolic background を直接測る方法ではありません。ここから導かれる批判は単純で、<strong>配線が分かった</strong>ことと<strong>その瞬間の生成的状態が分かった</strong>ことを同一視してはならない、という点でございます。
</p>

<h3>4. same-brain function を足すと縮退は減るが、全脳 state-complete には届きません</h3>
<p>
MICrONS は、同一脳で dense calcium imaging、行動状態、EM connectome を結びつけ、mouse visual cortex の multi-area functional connectomics を提示しました。これは connectome-only より一段強く、<strong>同じ脳での structure-function link</strong> を論じられる土台です。しかし、論文自体が扱うのは visual cortex の特定領域、特定課題、特定状態であり、そこから human whole-brain や all-state completeness へ飛躍することはできません。従って、この stack の ceiling は <strong>local functional twin</strong> です。
</p>

<h3>5. neuromodulator / glia imaging は coarse proxy の誤読を減らすが、全脳 ground truth にはなりません</h3>
<p>
Neyhart らは cortical ACh dynamics が cholinergic axon activity と behavioral state からかなり予測できること、同時に局所軸索からの距離と clearance kinetics に依存することを示しました。Cahill らは、局所的な neurotransmitter input が broad astrocyte network へ minutes-long に符号化されることを示しました。これらは、「pupil が上がった」「行動状態が変わった」だけで transmitter state や glial state を単純化してよいわけではないことを教えます。したがって、これらの stack は <strong>proxy calibration</strong> と <strong>glia omission の禁止</strong> には非常に有効ですが、そのまま全脳 internal state の ground truth にはなりません。
</p>

<h2>この批判から生じる実務ルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>augmentation claim には measurement stack を書く：</strong>「transcriptomic label を足した」ではなく、whole-brain atlas か Patch-seq bridge か same-brain link かを区別します。</li>
<li><strong>atlas / bridge / scaffold / local twin / proxy calibration を混ぜない：</strong>同じ「前進」でも、どの種類の前進かを固定します。</li>
<li><strong>multimodal を state-complete の同義語にしない：</strong>何の latent state が依然として残るかを本文に併記します。</li>
<li><strong>未観測状態を埋めるときは推定と書く：</strong>cell type から threshold / gain / set point を自動補完した場合は latent inference と明記します。</li>
<li><strong>claim ceiling を超える表現を禁止する：</strong>たとえば EM だけで emulation-complete、Patch-seq だけで whole-brain state-complete、pupil だけで transmitter ground truth とは書きません。</li>
</ul>

<table>
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

<h2>参考文献</h2>
<ol>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124-138. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <em>Nature</em>, 624, 317-332. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Gouwens, N. W., et al. (2021). Phenotypic variation of transcriptomic cell types in mouse motor cortex. <em>Nature</em>, 598, 144-150. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <em>Nature</em>, 640, 435-447. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <em>Nature</em>, 640, 497-505. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <em>Cell Reports</em>, 43(10), 114808. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <em>Nature</em>, 629, 146-153. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <em>Nature Communications</em>, 15, 3820. <a href="https://doi.org/10.1038/s41467-024-47838-5" target="_blank">doi:10.1038/s41467-024-47838-5</a></li>
</ol>
