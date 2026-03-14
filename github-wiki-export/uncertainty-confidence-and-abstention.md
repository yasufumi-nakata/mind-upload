# Wiki：不確実性・校正・棄権

> confidence はそのまま信頼度ではありません。校正と coverage を分けて見ます
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Technical / natural science only

## このページの役割
このページは、Mind-Upload で頻出する『不確実性』『信頼区間』『信用区間』『校正』『棄権』を、EEG source imaging、EEG分類、closed-loop BCI の一次文献に寄せて整理する wiki です。数字が 1 つ出たときにどこまで信じてよいかだけでなく、いつ出力を止めるべきかまで含めて扱います。

## 正確さの前提
ここでは統計学の完全な教科書説明より、技術・自然科学の監査項目を優先します。厳密な定義を省略する箇所はありますが、『confidence と calibration は別』『coverage を下げれば risk は下げられる』『online 系では再較正負荷も性能』という要点は曖昧にしません。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: 観測から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 逆問題や因果推定で、どこまで主張が止まるかへ戻れます。
- [Wiki: state・trait・ドリフト](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - 日内変動、縦断変化、decoder drift を分けて読む補助ページです。
- [Wiki: 反事実・介入・摂動](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - 不確実性を、介入や held-out 条件までどう持ち込むかを補います。
- [Wiki: 閉ループ・遅延・ジッタ・安全停止](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - online 系で棄権や停止をどう分けるかを補います。

## いま分かっていること
- 頭部幾何、導電率、subject shift、session drift、decoder drift は推定幅と実運用性能を大きく動かします。
- accuracy が高くても calibration が悪いと、低信頼条件で過信した誤答を出しやすくなります。
- online BCI では latency だけでなく、棄権率、dropout、recalibration burden、recovery time を別に残す必要があります。

## まだ分かっていないこと
- WBE 向けに site-wide で標準化すべき calibration 指標セットはまだ固定されていません。
- どの coverage / abstention 閾値を L2/L3 の共通 pass/fail にするかは、まだ詰め切れていません。
- source imaging と online BCI をまたぐ統一的不確実性会計は、まだ整備途中です。

---

<h2>結論</h2>
<p>
このサイトでは、<strong>点推定だけ</strong>、<strong>未校正の confidence だけ</strong>、<strong>棄権条件なしの出力</strong>を強い証拠として扱いません。先に監査するのは、<strong>どこ由来の不確実性か</strong>、<strong>その確率や区間がどれだけ校正されているか</strong>、<strong>低信頼時にどこで止めるか</strong>、<strong>online 系なら再較正負荷をどう記録するか</strong>の 4 点でございます。
</p>

<strong>このページの範囲</strong>
<p>
ここでは哲学や法制度を扱いません。EEG source imaging、EEG分類、closed-loop BCI の技術と自然科学の側面だけから、不確実性と校正と棄権を整理します。
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
<td><strong>Gate 1: 出所の切り分け</strong></td>
<td>観測ノイズ、前処理差、頭部幾何、導電率、subject shift、session drift、decoder drift の内訳。</td>
<td>「誤差の原因が分かっている」「改善策が有効だった」とは言えません。</td>
</tr>
<tr>
<td><strong>Gate 2: 校正</strong></td>
<td>区間の被覆、ECE/Brier/NLL、posterior 幅、coverage-risk curve、感度分析。</td>
<td>confidence や posterior を、使える確率や信頼度として読めません。</td>
</tr>
<tr>
<td><strong>Gate 3: 棄権</strong></td>
<td>低信頼時の reject / abstain 条件、coverage 低下と risk 低下の交換、再計測や再解析の分岐。</td>
<td>低信頼条件での誤答抑制や安全側運用を主張できません。</td>
</tr>
<tr>
<td><strong>Gate 4: online 負荷</strong></td>
<td>再較正頻度、dropout、recovery time、hold-last-output / silence / freeze / hard stop の区別。</td>
<td>閉ループでの運用安定性を、平均精度だけで語れません。</td>
</tr>
</tbody>
</table>

<h2>confidence、区間、校正、棄権を混ぜない</h2>
<table>
<thead>
<tr>
<th>概念</th>
<th>何が分かるか</th>
<th>それだけではまだ分からないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>点推定</strong></td>
<td>いまの代表値が分かります。</td>
<td>どれくらい不安定か、条件を変えると崩れるかは分かりません。</td>
</tr>
<tr>
<td><strong>区間</strong></td>
<td>推定値の周りにどれくらい幅があるかが見えます。</td>
<td>その幅が実際に妥当な被覆を持つか、由来がどこかは別に確認が必要です。</td>
</tr>
<tr>
<td><strong>confidence</strong></td>
<td>モデル内部のスコアや確信度の順序づけが見えます。</td>
<td>その数値が現実の的中確率に一致するかは分かりません。</td>
</tr>
<tr>
<td><strong>校正</strong></td>
<td>0.8 と出たときに本当に 8 割程度当たるか、区間が期待通り被覆するかを見られます。</td>
<td>校正が良くても、表現力不足や OOD 一般化の不足は別問題として残ります。</td>
</tr>
<tr>
<td><strong>棄権</strong></td>
<td>低信頼条件で出力を止め、coverage と risk の交換条件を明示できます。</td>
<td>閾値設定が妥当か、棄権後の再計測・再較正フローがあるかは別に必要です。</td>
</tr>
</tbody>
</table>

<strong>このサイトでの読み替え</strong>
<p>
softmax、posterior probability、LLM の自己確信、decoder の class score は、そのままでは <strong>校正済み確率</strong>とみなしません。校正誤差、coverage-risk、または interval coverage を一緒に出して初めて、実運用に使える信頼度として扱います。
</p>

<h2>不確実性は 4 つの層で生まれます</h2>
<table>
<thead>
<tr>
<th>層</th>
<th>代表例</th>
<th>主に効くページ・課題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測ノイズ</strong></td>
<td>電極接触、同期ずれ、筋電・瞬目、欠損、刺激アーチファクト。</td>
<td>EEG 入門、event sync、closed-loop 実装。</td>
</tr>
<tr>
<td><strong>モデル・幾何の不確かさ</strong></td>
<td>頭部モデル、頭蓋導電率、source depth、solver 依存性。</td>
<td>source imaging、multimodal integration、observation-to-estimation。</td>
</tr>
<tr>
<td><strong>分布ずれ</strong></td>
<td>被験者差、別日、薬理状態、麻酔、課題変更、OOD 条件。</td>
<td>decode、forecasting、counterfactual/perturbation。</td>
</tr>
<tr>
<td><strong>運用ドリフト</strong></td>
<td>decoder drift、電極再装着、学習、疲労、再較正負荷。</td>
<td>closed-loop BCI、state-trait-drift、longitudinal evaluation。</td>
</tr>
</tbody>
</table>
<p>
重要なのは、不確実性を 1 つの箱で語らないことでございます。source imaging の幅は幾何と導電率に強く依存し、EEG 分類の過信は校正誤差や subject shift に強く依存し、closed-loop の破綻は drift と再較正負荷に強く依存します。<strong>同じ「不確実性」という語でも、課題ごとに会計方法が違います</strong>。
</p>

<h2>課題ごとに公開すべき指標を変えます</h2>
<table>
<thead>
<tr>
<th>課題</th>
<th>最低限ほしい指標</th>
<th>点推定だけでは危険な理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG source imaging</strong></td>
<td>posterior / interval 幅、頭蓋導電率感度、solver 比較、外部妥当化ラダー。</td>
<td>同じ頭皮信号を、複数の source 配置が説明できるからです。</td>
</tr>
<tr>
<td><strong>offline EEG 分類</strong></td>
<td>ECE、Brier score、NLL、被験者外評価、coverage-risk curve。</td>
<td>accuracy が高くても、confidence が過信なら運用時に危険です。</td>
</tr>
<tr>
<td><strong>希少イベント予測</strong></td>
<td>false alarm rate、sensitivity、calibration curve、risk-controlling threshold。</td>
<td>発作予測のような低頻度課題では、わずかな過信が実用性を大きく損ねます。</td>
</tr>
<tr>
<td><strong>online / closed-loop BCI</strong></td>
<td>abstention rate、dropout、recalibration burden、recovery time、silence / freeze / hard stop の回数。</td>
<td>平均精度だけでは、継続運用での破綻や介入不能時間が隠れるからです。</td>
</tr>
</tbody>
</table>

<h2>一次文献が実際に示していること</h2>

<h3>1. source imaging では、幅を出さない推定は読みすぎです</h3>
<p>
Vorwerk らは頭部組織導電率の不確かさが dipole reconstruction を大きく動かすことを示し、Rimpiläinen らは未知の skull conductivity をベイズ的に扱うことで source localization の不確実性自体を推定対象へ入れました。Feng らの Block-Champagne も、重要なのは solver 名そのものではなく、<strong>empirical Bayesian uncertainty quantification を伴うこと</strong>でございます。したがって本サイトでは、<strong>「どの solver か」より「どの幅を、どの外部妥当化で示したか」</strong>を先に確認します。
</p>

<h3>2. EEG 分類では、accuracy と calibration を分離しないと危険です</h3>
<p>
Duan らの UNCER は motor imagery EEG decoding で uncertainty estimation と confidence calibration を組み合わせ、低信頼試行の扱いが性能解釈を変えることを示しました。Hu らは発作検出 EEG 分類で calibration 改善を明示し、Shafiezadeh らは patient-independent seizure forecasting で deep classifier の calibration を調整すると、実用上の threshold 設計が変わることを示しました。Segal らは risk-controlling prediction calibration により false alarm rate を抑える方向を示しており、<strong>校正は見栄えの問題ではなく、誤警報コストの問題</strong>であることが分かります。
</p>

<h3>3. 棄権は「安全そうだから」ではなく、coverage と risk の公開です</h3>
<p>
Ganeshkumar らは EEG motor imagery BCI に reject option を入れることで false prediction rate を下げられることを示しました。ここで重要なのは、誤りを減らす代わりに <strong>どれだけ coverage を下げたか</strong>を出すことでございます。したがって、棄権率だけ、または accuracy だけを単独で見せるのは不十分であり、coverage-risk の交換条件を一緒に公開する必要があります。
</p>

<h3>4. online BCI では、再較正と silence も性能です</h3>
<p>
Wairagkar らの instantaneous voice-synthesis neuroprosthesis は低遅延 loop を示しましたが、同時に non-speech 区間で silence を返す設計が重要でした。Wilson らは intracortical BCI の長期 unsupervised recalibration を示し、精度だけでなく <strong>どれだけ再較正を要するか</strong>が継続運用のボトルネックであることを示しました。したがって、closed-loop 系では latency や accuracy に加えて、<strong>abstention / silence / recalibration burden / recovery time</strong> を別指標で残します。
</p>

<h2>このサイトで採用する運用ルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>confidence をそのまま確率と読まない：</strong>校正誤差か interval coverage が出ていなければ、内部スコアとして扱います。</li>
<li><strong>source imaging は幅と感度分析を必須にする：</strong>頭蓋導電率、頭部モデル、solver family の違いで解が重なるなら、無理に 1 点へ潰しません。</li>
<li><strong>EEG 分類は coverage-risk を出す：</strong>accuracy だけで通さず、ECE/Brier/NLL と棄権後の coverage を併記します。</li>
<li><strong>発作予測や希少イベントは false alarm を別管理する：</strong>感度だけでなく、誤警報コストと threshold 制御を主指標に入れます。</li>
<li><strong>online BCI は再較正負荷を性能として出す：</strong>再較正回数、所要時間、recovery time、silence / freeze / hard stop の内訳を公開します。</li>
<li><strong>低信頼時は棄権を選べるようにする：</strong>無理に単一解を返すより、要再計測・要再解析・要介入停止へ分岐させます。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Vorwerk, J., Aydin, U., Wolters, C. H., &amp; Butson, C. R. (2019). Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Rimpiläinen, I., Solis-Lemus, J. A., &amp; Särkkä, S. (2019). Improved EEG source localization with Bayesian uncertainty modelling of unknown skull conductivity. <em>NeuroImage</em>, 184, 52-60. <a href="https://doi.org/10.1016/j.neuroimage.2018.11.058" target="_blank">doi:10.1016/j.neuroimage.2018.11.058</a></li>
<li>Feng, Z., Guan, C., &amp; Sun, Y. (2025). Block-Champagne: A Novel Bayesian Framework for Imaging Extended E/MEG Source. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Duan, T., Wang, Z., Liu, S., Yin, Y., &amp; Srihari, S. N. (2023). UNCER: A framework for uncertainty estimation and reduction in neural decoding of EEG signals. <em>Neurocomputing</em>, 538, 126210. <a href="https://doi.org/10.1016/j.neucom.2023.03.071" target="_blank">doi:10.1016/j.neucom.2023.03.071</a></li>
<li>Hu, J., Ur Rahman, M. M., Al-Naffouri, T., &amp; Laleg-Kirati, T.-M. (2024). Uncertainty Estimation and Model Calibration in EEG Signal Classification for Epileptic Seizures Detection. In <em>2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)</em> (pp. 1-5). <a href="https://doi.org/10.1109/EMBC53108.2024.10782858" target="_blank">doi:10.1109/EMBC53108.2024.10782858</a></li>
<li>Shafiezadeh, S., Duma, G. M., Mento, G., Danieli, A., Antoniazzi, L., Del Popolo Cristaldi, F., Bonanni, P., &amp; Testolin, A. (2024). Calibrating Deep Learning Classifiers for Patient-Independent Electroencephalogram Seizure Forecasting. <em>Sensors</em>, 24(9), 2863. <a href="https://doi.org/10.3390/s24092863" target="_blank">doi:10.3390/s24092863</a></li>
<li>Segal, G., Keidar, N., Lotan, R. M., Romano, Y., Herskovitz, M., &amp; Yaniv, Y. (2023). Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. <em>Frontiers in Neuroscience</em>, 17, 1184990. <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">doi:10.3389/fnins.2023.1184990</a></li>
<li>Ganeshkumar, P., Maheswari, U., &amp; Vasant, P. (2017). Reject Option to Reduce False Prediction Rates for EEG-Motor Imagery Based BCI. In <em>2017 International Conference on Advances in Computing, Communications and Informatics (ICACCI)</em>. <a href="https://doi.org/10.1109/ICACCI.2017.8125908" target="_blank">doi:10.1109/ICACCI.2017.8125908</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., Avansino, D. T., Pun, T. K., Gross, R., Hosman, T., Singer-Clark, T., Kapitonava, A., Hochberg, L. R., Simeral, J. D., Shenoy, K. V., Druckmann, S., Henderson, J. M., &amp; Willett, F. R. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a Markov model. <em>Nature Biomedical Engineering</em>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., Hochberg, L. R., Brandman, D. M., &amp; Stavisky, S. D. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644(8075), 145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
</ol>

<h2>次にどこへ戻るか</h2>
<p>
source imaging 側へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">観測から推定へ</a>、closed-loop 側へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ・遅延・ジッタ・安全停止</a>、公開ルール全体へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a> をご利用ください。
</p>
