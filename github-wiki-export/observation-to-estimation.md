# Wiki：観測から推定へ

> 観測に合うこと、内部状態が分かること、因果が分かることは別です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Technical / natural science only

## このページの役割
このページは、EEG などの観測信号から脳内状態や因果構造を推定するときに、どこで主張が止まり、何を追加すると一段強く言えるかを整理する wiki です。順問題、逆問題、ESI、DCM、SCM、因果同値類を、『観測→推定→介入→妥当化』の順でつなぎます。

## 正確さの前提
ここで示すのは、どの手法を採用すべきかの固定レシピではありません。どの手法を使っても逃げられない監査項目を先に固定するページです。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: 計測からモデル化まで](https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-and-modeling-terms) - 計測、整理、推定、検証の全体マップへ戻れます。
- [Wiki: EEG前処理とQC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 推定の前段で、何が結果を変えるかを補います。
- [Wiki: 不確実性・校正・棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 点推定ではなく幅と棄権条件をどう残すかを補います。
- [Wiki: 反事実・介入・摂動](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - 観測適合から介入検証へ進む条件を補います。

## いま分かっていること
- 頭皮 EEG から脳内活動を一意に決めることは原理的に難しく、推定には仮定が入ります。
- 高密度 EEG、個体別 MRI、FEM/BEM、経験ベイズ推定は条件を改善しえますが、単独で一意復元を保証しません。
- 観測適合だけでは因果構造は確定せず、候補モデル集合と介入設計が必要です。

## まだ分かっていないこと
- どの計測・モデル化の組み合わせが WBE の検証に最も有効かは未確定です。
- 非侵襲計測だけで、どこまで詳細な因果構造や状態変数を安定に復元できるかは研究途中です。
- どの外部妥当化ラダーを site-wide benchmark に固定するかは、まだ整備途中です。

---

<h2>結論</h2>
<p>
観測信号に合うモデルが見つかっても、それだけで <strong>内部状態が一意に分かった</strong>とも、<strong>因果構造が同定できた</strong>とも言えません。したがって、このサイトでは solver 名や理論名より先に、<strong>幾何・不確実性・候補モデル集合・外部妥当化</strong>の 4 点を監査します。
</p>

<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。技術と自然科学の側面だけから、観測・推定・因果主張の境界を一次文献ベースで整理します。
</p>

<h2>先に固定する 4 つの監査ゲート</h2>
<table>
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

<h2>観測・推定・因果検証を混ぜない</h2>
<table>
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

<h2>順問題と逆問題</h2>
<table>
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

<h2>ESI は solver 名より、まず妥当化ラダーで読む</h2>
<p>
ESI は、頭皮信号から source を推定するための枠組みです。しかし、Mikulan らや Unnwongse らの直接妥当化研究が示す通り、source depth、頭蓋導電率、頭部モデル、電極幾何、solver の選び方で誤差は大きく変わります。したがって、<strong>「高密度 EEG だから」「Bayesian solver だから」だけでは強い主張はできません</strong>。
</p>
<table>
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

<strong>このサイトでの読み替え</strong>
<p>
Bayesian / empirical Bayes / sparse Bayesian learning は、<strong>不確実性を伴う推定</strong>として有力な候補です。ただし、本サイトでは「ベイズだから採用」ではなく、<strong>不確実性をどの形で公開し、どの外部基準で較正したか</strong>を採否条件にします。
</p>

<h2>DCM は「真の因果を自動発見する装置」ではありません</h2>
<p>
DCM は、候補となる生成モデルを明示し、その中でどれが観測を説明しやすいかを比較する枠組みです。Friston らの原論文と Penny らのモデル比較研究が示す通り、DCM の結論は <strong>比較に入れた候補モデル空間</strong>に依存します。したがって、モデル比較で勝ったことは「候補集合の中では良い」という意味であり、<strong>世界で唯一正しい</strong>ことを意味しません。
</p>

<h4>DCM を読むときの 4 点</h4>
<ul>
<li><strong>候補モデル空間：</strong>どのノードと結合候補を最初から比較対象に入れたか。</li>
<li><strong>family 比較：</strong>細部でなく上位 family が安定しているか。</li>
<li><strong>model recovery：</strong>シミュレーションで正解モデルを回収できるか。</li>
<li><strong>介入較正：</strong>刺激や摂動で held-out 予測が当たるか。</li>
</ul>

<h2>SCM と因果発見は、介入が入って初めて強くなる</h2>
<p>
SCM は、介入や反事実を明示的に書き下ろしやすい枠組みです。しかし、観測データだけから学ぶ場合、しばしば <strong>Markov equivalence class</strong> が残ります。Hauser と Buhlmann が示したように、介入データはこの同値類を狭めるために重要です。脳データでも、Vink らは resting-state functional connectivity が causal interaction の弱い予測子にとどまることを示しており、相関だけで方向や機序を確定するのは危険でございます。
</p>

<strong>SCM と DCM の役割差</strong>
<p>
DCM は神経回路の候補生成モデル比較、SCM は介入・反事実を表現する言語として有用です。どちらも重要ですが、どちらか 1 つを入れたから因果が自動で確定するわけではありません。
</p>

<h2>一段強い主張へ進むための外部妥当化ラダー</h2>
<table>
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

<h2>このサイトで採用する運用ルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>solver 名を標準とは書かない：</strong>Bayesian solver、minimum norm、DCM、SCM は候補であり、採否は監査項目で決めます。</li>
<li><strong>観測適合だけで因果主張を上げない：</strong>介入または外部妥当化がない場合は、同値類や候補モデルレベルに留めます。</li>
<li><strong>深部や細粒度は保留条件つきで書く：</strong>detectable と robust reconstruction を混同しません。</li>
<li><strong>不確実性が広いときは棄権する：</strong>解が重なるなら、無理に 1 つへ潰さず保留を明示します。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Wipf, D., &amp; Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging. <em>NeuroImage</em>, 44(3), 947-966. <a href="https://doi.org/10.1016/j.neuroimage.2008.02.059" target="_blank">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li>Aydin, U., Vorwerk, J., Kupper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(1), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, Y., Alhilani, M., Asano, E., et al. (2025). High-density scalp EEG source imaging and directed functional connectivity validated by simultaneous stereo-electroencephalography. <em>Epilepsia</em>. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging extended E/MEG source activation with empirical Bayesian uncertainty quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <em>NeuroImage</em>, 19(4), 1273-1302. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <em>NeuroImage</em>, 22(3), 1157-1172. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Lee, H.-L., Zahneisen, B., Hugger, T., et al. (2017). Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. <em>NeuroImage</em>, 149, 441-451. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.012" target="_blank">doi:10.1016/j.neuroimage.2017.02.012</a></li>
<li>Hauser, A., &amp; Buhlmann, P. (2012). Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. <em>Journal of Machine Learning Research</em>, 13, 2409-2464. <a href="https://jmlr.org/papers/v13/hauser12a.html" target="_blank">JMLR</a></li>
<li>Vink, J. J., Ramos-Nuñez, A. I., Bellesi, A., et al. (2020). The brain's functional connectome is a poor predictor of the brain's causal activity flow. <em>PLOS Computational Biology</em>, 16(1), e1007866. <a href="https://doi.org/10.1371/journal.pcbi.1007866" target="_blank">doi:10.1371/journal.pcbi.1007866</a></li>
</ol>
