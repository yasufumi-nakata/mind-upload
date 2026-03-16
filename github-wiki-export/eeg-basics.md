# Wiki：EEG の基本

> EEG を魔法の読心術にしないための基礎知識
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-16 / 位置づけ: Beginner guide

## このページの役割
このページは、EEG が何を測っているのかを初歩から説明する wiki です。難しい式より先に、『どんな信号がどこで混ざって見えているのか』『なぜ前処理や QC が重要なのか』を理解することを目標にします。

## 正確さの前提
EEG を過大評価しないために限界も強調しますが、だからといって役に立たないと言うページではありません。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [ハンズオン](https://mind-upload.com/datasets.html#l0-practice)

## 関連 Wiki
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - EEG が WBE 全体のどこに入るかを先に見たい場合はこちらです。
- [Wiki: EEG前処理とQC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 前処理やログの取り方を、実務に寄せて整理します。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜ EEG でも標準や QC が必要かを理解できます。

## いま分かっていること
- EEG はミリ秒単位の時間変化を見るのが得意です。
- 観測される信号は多くの活動が混ざった結果であり、解釈には前提が必要です。
- 個体別 MRI と外部基準を入れると source imaging は改善しますが、深部や弱い source の不確実性は残ります。
- 高密度化の効果は sensor count だけでなく、head-surface coverage と外部妥当化の有無で変わります。
- 公開データでも、前処理とベースライン比較の練習は十分できます。

## まだ分かっていないこと
- 非侵襲 EEG だけで、脳内部の詳細な因果構造まで十分に再構成できるかは未解決です。
- 前処理の選び方が、どの課題でどこまで結論を変えるかは一律ではありません。
- どの external benchmark が source imaging の標準妥当化セットになるかはまだ固定されていません。

---

<h2>EEG は何を見ているのか</h2>
<p>
EEG は、頭皮につけた電極で電位差を測る方法です。つまり、脳の中を直接カメラで見ているわけではなく、たくさんの活動が重なって外まで伝わってきた<strong>混ざった信号</strong>を読んでいます。
</p>

<strong>このページで先に止めるすり替え</strong>
<p>
EEG では、<strong>頭皮信号を観測した</strong>こと、<strong>脳内 source を条件付きで推定した</strong>こと、<strong>内部状態が一意に同定できた</strong>ことは別です。この3つを混同すると、初心者ほど「見えた」と「推定した」を同じ意味で読んでしまいます。
</p>

<h2>EEG が得意なこと</h2>
<table>
<thead>
<tr>
<th>得意なこと</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td>時間変化を見ること</td>
<td>EEG はミリ秒単位で信号を取れるため、いつ変化したかを追いやすいからです。</td>
</tr>
<tr>
<td>状態遷移やイベント検出</td>
<td>睡眠段階や発作イベントのように、時間とともに変わる状態の観測に向きます。</td>
</tr>
<tr>
<td>公開データでの再現練習</td>
<td>PhysioNet などに定番データがあり、L0 の練習を始めやすいからです。</td>
</tr>
</tbody>
</table>

<h2>EEG が苦手なこと</h2>
<table>
<thead>
<tr>
<th>苦手なこと</th>
<th>なぜ難しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td>正確に「脳のどこか」を言い切ること</td>
<td>頭蓋骨や頭皮を通るあいだに信号がぼやけ、逆問題も一意に解けないからです。</td>
</tr>
<tr>
<td>深部構造を詳細に知ること</td>
<td>頭皮から遠い活動や弱い信号は、観測しづらいからです。</td>
</tr>
<tr>
<td>EEG 単体で強い本人性主張をすること</td>
<td>EEG は重要な手がかりですが、それだけで記憶・価値観・因果連続性まで確かめられないからです。</td>
</tr>
</tbody>
</table>

<h2>電極を増やすと何が変わるか</h2>
<p>
初心者が誤読しやすいのは、「電極が多いほど全部分かる」か、逆に「128ch を超えたら全部同じ」のどちらかへ振れることでございます。一次文献はそのどちらも支持していません。増やして改善する層はありますが、それでも source の一意復元や WBE に十分な情報量までは到達しません。
</p>
<table>
<thead>
<tr>
<th>問い</th>
<th>一次文献が示すこと</th>
<th>初心者向けの安全な読み方</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>頭皮場の空間サンプリング</strong></td>
<td><a href="https://doi.org/10.1046/j.1460-9568.1998.00269.x" target="_blank">Srinivasan et al. (1998)</a> は頭皮電位の空間平滑化を示し、<a href="https://doi.org/10.1088/1741-2552/ac288c" target="_blank">Iivanainen et al. (2021)</a> は head-surface field 推定が <strong>約 110 spatial samples</strong> までは改善しうると報告しました。</td>
<td>32 / 64ch がいつも十分とは言いませんが、sensor 数をそのまま独立な脳内自由度とは読みません。</td>
</tr>
<tr>
<td><strong>局所情報の取りこぼし</strong></td>
<td><a href="https://doi.org/10.1038/s41598-017-16377-3" target="_blank">Robinson et al. (2017)</a> は、視覚野上の super-Nyquist-density EEG が標準密度 subset より追加情報を与えると示しました。</td>
<td>「高密度化は全部無意味」とは書きません。ただし改善は局所 cortical 情報であり、全脳状態の完全復元ではありません。</td>
</tr>
<tr>
<td><strong>source localization の改善</strong></td>
<td><a href="https://doi.org/10.1046/j.1460-9568.2003.02483.x" target="_blank">Lantz et al. (2003)</a> は 31→63→123 electrodes で局在が改善すると示し、<a href="https://doi.org/10.1016/j.jneumeth.2015.08.015" target="_blank">Song et al. (2015)</a> は inferior surface を含む whole-head coverage が有利だと示しました。</td>
<td>本数だけでなく、被覆、個体別 MRI、conductivity、外部基準を併記してはじめて改善を読みます。</td>
</tr>
<tr>
<td><strong>WBE に十分か</strong></td>
<td><a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> が示すのは条件付き detectability と誤差監査であり、state-complete reconstruction ではありません。</td>
<td>高密度 EEG は強い macro constraint ですが、cell / synapse / glia を直接与える装置ではありません。</td>
</tr>
</tbody>
</table>

<h2>観測・推定・同定は別です</h2>
<table>
<thead>
<tr>
<th>段階</th>
<th>EEG で言えること</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測</strong></td>
<td>頭皮上の混合電位を ms スケールで取れます。状態遷移やイベント時刻を追うのは得意です。</td>
<td>どの深部 source が唯一の原因か、細胞型や神経修飾まで直接見えたとは言えません。</td>
</tr>
<tr>
<td><strong>条件付き推定</strong></td>
<td>個体別 MRI、電極座標、forward model を入れると、皮質近傍や一部深部活動の推定は改善します。</td>
<td>条件が厳しいときに detect できることと、一般に一意復元できることは別です。</td>
</tr>
<tr>
<td><strong>同定</strong></td>
<td>頭蓋内刺激、同時 SEEG/ECoG、ファントム、術後転帰などの外部基準があれば、誤差を監査できます。</td>
<td>外部基準がないまま「source が分かった」「WBE に十分な状態が取れた」とは書けません。</td>
</tr>
</tbody>
</table>

<strong>2026-03 の実測エビデンス</strong>
<p>
Seeber et al. (2019) は 256ch scalp EEG と同時 DBS 記録で subcortical signal の detectability を示しましたが、一般的一意復元を主張していません。Unnwongse et al. (2023) は intracranial stimulation に対する直接妥当化で localization error が頭蓋導電率と source depth に依存すると報告し、Hao et al. (2025) は simultaneous HD-EEG/SEEG の 29 例で source power と source depth が誤差を強く左右すると示しました。したがって、正しい読み方は「条件を厳しく固定すれば一部は監査できる」であって、「EEG 単体で脳内 source が一意に読める」ではありません。
</p>

<h2>なぜ QC と前処理が大事か</h2>
<p>
EEG はノイズの影響を受けやすい計測です。まばたき、筋電、体動、電源ノイズ、参照電極の置き方、フィルタ設定などで結果が変わります。だから、きれいに見える図だけでは足りず、<strong>どう処理したかを残すこと</strong>が必要です。
</p>

<h4>最低限残したいこと</h4>
<ul>
<li><strong>参照方法：</strong>どの基準で電位差を取ったか。</li>
<li><strong>フィルタ：</strong>どの周波数帯を通したか。</li>
<li><strong>アーティファクト処理：</strong>どのノイズをどう除いたか。</li>
<li><strong>除外基準：</strong>どのデータを、なぜ外したか。</li>
</ul>

<h2>WBE とどうつながるか</h2>
<p>
EEG は WBE をいきなり完成させる装置ではありません。しかし、状態変化の時間情報、ベースライン比較、公開データでの再現性づくりには重要です。Mind-Upload では、EEG を「全部を読む装置」ではなく、<strong>マクロな制約を与える観測手段</strong>として扱います。
</p>

<h4>Next</h4>
<p>EEG を含む研究を、主張の強さと証拠で読み分けるにはこちらです。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence">主張と証拠の読み方へ →</a>

<h4>Practical Next</h4>
<p>参照法、フィルタ、アーティファクト処理で何が変わるかを実務寄りに見たい場合はこちらです。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc">EEG前処理とQCへ →</a>

<h4>Technical Next</h4>
<p>観測と推定の境界、ESI、DCM、SCM のつながりを流れで見たい場合はこちらです。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-and-modeling-terms">計測からモデル化までへ →</a>

<h2>参考文献</h2>
<ol>
<li>Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review of the analysis steps. <em>Frontiers in Neurology</em>, 10, 325. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Srinivasan, R., Nunez, P. L., &amp; Silberstein, R. B. (1998). Spatial filtering and neocortical dynamics: estimates of EEG coherence. <em>Electroencephalography and Clinical Neurophysiology</em>, 106(3), 249-260. <a href="https://doi.org/10.1046/j.1460-9568.1998.00269.x" target="_blank">doi:10.1046/j.1460-9568.1998.00269.x</a></li>
<li>Lantz, G., Grave de Peralta, R., Spinelli, L., Seeck, M., &amp; Michel, C. M. (2003). Epileptic source localization with high density EEG: how many electrodes are needed? <em>European Journal of Neuroscience</em>, 17(1), 63-69. <a href="https://doi.org/10.1046/j.1460-9568.2003.02483.x" target="_blank">doi:10.1046/j.1460-9568.2003.02483.x</a></li>
<li>Song, J., Davey, C., Poulsen, C., et al. (2015). EEG source localization: Sensor density and head surface coverage. <em>Journal of Neuroscience Methods</em>, 256, 9-21. <a href="https://doi.org/10.1016/j.jneumeth.2015.08.015" target="_blank">doi:10.1016/j.jneumeth.2015.08.015</a></li>
<li>Robinson, A. K., Venkatesh, P., Boring, M. J., et al. (2017). Very high density EEG elucidates spatiotemporal aspects of early visual processing. <em>Scientific Reports</em>, 7, 16248. <a href="https://doi.org/10.1038/s41598-017-16377-3" target="_blank">doi:10.1038/s41598-017-16377-3</a></li>
<li>Iivanainen, J., Stenroos, M., Nummenmaa, A., &amp; Parkkonen, L. (2021). On the effect of spatial sampling in EEG head-surface field estimation and optimization. <em>Journal of Neural Engineering</em>. <a href="https://doi.org/10.1088/1741-2552/ac288c" target="_blank">doi:10.1088/1741-2552/ac288c</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <em>Scientific Data</em>, 7, 127. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <em>Nature Communications</em>, 10, 753. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <em>Brain Communications</em>, 5(2), fcad023. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <em>Epilepsia</em>, 66(11), 4451-4464. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
</ol>
