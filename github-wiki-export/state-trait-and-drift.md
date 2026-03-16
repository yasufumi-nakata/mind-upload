# Wiki：state・trait・ドリフト

> 『今日の状態』『比較的安定な骨格』『運用ドリフト』は別々に監査します
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-16 / 位置づけ: Technical / natural science only

## このページの役割
このページは、Mind-Upload の縦断評価で頻出する state（その場の状態）、trait（比較的安定な骨格）、drift（時間とともに起きる変化）を、EEG・fMRI・慢性記録・BCI の一次文献に沿って整理する wiki です。短期変動と長期変化を言葉だけで分けるのではなく、どの時定数で、どのメカニズム由来で、どの評価系で観測したかまで固定することを目的にしています。

## 正確さの前提
ここでは哲学や法制度は扱いません。state / trait / drift を、技術と自然科学の監査項目として扱います。trait を『不変』とは呼ばず、drift を 1 種類とも扱いません。

## 公開ページへ戻る
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [EEG入門](https://mind-upload.com/eeg_101.html)

## 関連 Wiki
- [Wiki: 不確実性・校正・棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - drift を誤差幅、校正、coverage-risk とどう接続するかを補います。
- [Wiki: 閉ループ・遅延・ジッタ・安全停止](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - online 系で drift と再較正負荷をどう読むかを補います。
- [Wiki: 観測から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 観測変動をどこまで latent state や構造へ持ち上げてよいかを補います。

## いま分かっていること
- 行動状態、覚醒、無意図運動、自発行動は、trial-to-trial neural variance を大きく動かします。
- 単一ユニットや単一 voxel の変化があっても、population-level の構造や latent dynamics がより安定に残る場合があります。
- 慢性 high-density probe では、probe drift、sorting 誤差、unit matching の不確実性、組織応答が single-unit longitudinal claim を動かします。
- fixed decoder の cross-day 劣化と recalibration burden を出さない限り、長期安定性は評価できません。

## まだ分かっていないこと
- どの task でどの骨格を trait と呼ぶべきかを site-wide に統一する基準は、まだ固定されていません。
- 生体側 drift と interface / decoder drift の会計を、EEG と侵襲 BCI とで横断比較する標準形式は未整備です。
- unit-match probability や dropout rate を、どこから chronic same-neuron claim の受理条件にするかは未固定です。
- WBE 向けの長期 benchmark で、どの timescale までを同一の trait backbone と見なすかは未確定です。

---

<h2>いちばん短い結論</h2>
<p>
<strong>state</strong>、<strong>trait</strong>、<strong>drift</strong> は、3 つの箱にデータを仕分けるだけの話ではございません。実際には、同じ記録の中に <strong>その場の行動・覚醒の揺れ</strong>、<strong>比較的安定な population backbone</strong>、<strong>生体側の representational drift</strong>、<strong>電極・前処理・デコーダ側の nonstationarity</strong> が同時に混ざります。したがって、このサイトでは <strong>timescale</strong>、<strong>由来</strong>、<strong>固定 decoder での held-out 劣化</strong>、<strong>再較正負荷</strong> を分けて監査します。
</p>

<strong>このページの範囲</strong>
<p>
ここでは本人性や権利の最終判断には進みません。扱うのは、縦断 neuroscience と BCI の技術・自然科学です。state を trait と誤読しないこと、trait を「単一ニューロンが不変」と言い換えないこと、drift を 1 種類に潰さないことを先に固定します。
</p>

<h2>まず 4 つに分けて読む</h2>
<table>
<thead>
<tr>
<th>層</th>
<th>何を指すか</th>
<th>典型 timescale</th>
<th>最低限ほしい評価</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state fluctuation</strong></td>
<td>覚醒、疲労、無意図運動、自発行動、課題 engagement など、その場の状態です。</td>
<td>秒〜分、長くても同日内です。</td>
<td>within-session 条件差、行動・生理指標との同時計測、state 別性能差です。</td>
</tr>
<tr>
<td><strong>trait-like backbone</strong></td>
<td>latent dynamics、representational geometry、functional fingerprint のような、比較的安定な骨格です。</td>
<td>日〜月、課題によっては年単位です。</td>
<td>cross-session 識別、latent manifold の整合、representational similarity の安定性です。</td>
</tr>
<tr>
<td><strong>biological drift</strong></td>
<td>学習、可塑性、tuning の再配置、responsive neuron の入れ替わりなど、生体側の変化です。</td>
<td>日〜週〜月です。</td>
<td>固定 readout の経時劣化、single-unit / voxel tuning の変化、population geometry の保持率です。</td>
</tr>
<tr>
<td><strong>interface / decoder drift</strong></td>
<td>電極再装着、インピーダンス変化、probe drift、sorting / unit matching error、feature 分布ずれ、decoder mismatch、再較正依存です。</td>
<td>セッション間から長期運用までです。</td>
<td>fixed decoder 劣化、recalibration 頻度、recovery time、unsupervised adaptation の成否です。</td>
</tr>
</tbody>
</table>

<h2>旧来の 3 分類だけでは足りない理由</h2>
<p>
現行の「state は今、trait は長く安定、drift は時間変化」という言い方だけですと、<strong>何が脳由来で、何が装置やデコーダ由来か</strong>が見えません。さらに、trait があたかも単一ニューロンや単一 feature の不変性であるかのようにも読めてしまいます。しかし一次文献が繰り返し示しているのは、<strong>individual unit はかなり動く</strong>一方で、<strong>population-level の関係構造の方が長く保たれることがある</strong>、という点でございます。
</p>

<strong>このサイトでの安全な読み替え</strong>
<p>
trait は「1 本の電極・1 個の neuron・1 本の voxel が不変」という意味ではなく、<strong>state 変動や一部の単位入れ替わりをまたいでも比較的安定に残る骨格</strong>として扱います。逆に、fixed decoder の劣化や再較正依存を見ていない主張は、trait stability を十分に示したことにはなりません。
</p>

<h2>一次文献が実際に示していること</h2>

<h3>1. state fluctuation は「ノイズ」ではなく、しばしば本体です</h3>
<p>
Musall ら (2019) は、課題遂行中の cortex-wide activity が task variable だけでなく、<strong>uninstructed movements</strong> に強く支配されることを示しました。Benisty ら (2024) も、spontaneous behavior が cortical network activity の大きさだけでなく、<strong>functional connectivity の correlational structure</strong> にも高速に刻まれることを示しています。したがって、同じ被験者・同じ日でも、state を明示せずに得た「一致」「不一致」は、そのまま trait や drift の証拠にはなりません。
</p>

<h3>2. trait-like backbone は、unit-level の不変性より上位で読む必要があります</h3>
<p>
Gallego ら (2020) は、サルの sensorimotor cortex を最大 2 年追跡し、記録される neurons が入れ替わっても、<strong>low-dimensional latent dynamics</strong> は安定に保たれ、aligned latent dynamics に基づく decoding は長期間維持できる一方、recorded activity に直接依存した fixed decoder は大きく劣化することを示しました。Finn ら (2015) も、functional connectivity profile が scan session をまたぎ、task と rest をまたいでも個人識別に使えることを示しています。ここから言えるのは、trait があるとしても、それはしばしば <strong>relation や manifold のレベル</strong>で見えるのであって、単一 feature の静止画ではない、ということでございます。
</p>

<h3>3. 慢性 extracellular 記録では、unit identity audit を drift 本体から切り離せません</h3>
<p>
Steinmetz ら (2021) の Neuropixels 2.0 は motion correction を用いた安定長期記録を大きく前進させましたが、これは逆に <strong>motion correction が要るほど probe drift が本質的な問題</strong>であることも示します。Pachitariu ら (2024) の Kilosort4 も、awake recording の drift、low-norm unit、split / merge error を benchmark の中心に置いています。Trautmann ら (2019) は、dense array では population dynamics の多くが spike sorting なしでも推定できることを示し、van Beest ら (2024) は cross-day の same-neuron claim を <strong>probabilistic matching</strong> として実装しました。さらに Gregory ら (2023) は、埋め込み array 周囲の深層 pyramidal neuron に structural / functional change が起こることを示しました。したがって、慢性 invasive 記録で「同じ neuron が何日も安定に見えた」と書くには、<strong>sorting version</strong>、<strong>drift correction</strong>、<strong>unit-match probability</strong>、<strong>dropout / new-unit rate</strong>、<strong>implant age と tissue-response proxy</strong> を別に残す必要がございます。
</p>

<h3>4. representational drift は、生体が安定環境でも起こしうる変化です</h3>
<p>
Roth と Merriam (2023) は human V1 の longitudinal fMRI で、session 間の時間が離れるほど model fit の cvR² が下がることを示し、<strong>representational drift が月単位で累積する</strong>ことを報告しました。一方で representational dissimilarity 自体は比較的安定であり、下流が読める関係構造は残る可能性が示されました。さらに Noda ら (2025) は mouse auditory cortex で、individual neuron の tuning volatility があっても、<strong>population-level representational map は保たれうる</strong>こと、しかも selected neuron loss 後でも数日で回復しうることを示しました。つまり、生体側 drift は存在しても、すべてのレベルが同じ速さで崩れるわけではございません。
</p>

<h3>5. BCI の運用では、decoder drift と recalibration burden が別の壁になります</h3>
<p>
Wilson ら (2025) は、intracortical cursor BCI が accumulating neural nonstationarities により <strong>frequent recalibration</strong> を要し、unsupervised target-inference recalibration がないと長期維持が難しいことを示しました。Wairagkar ら (2025) も、instantaneous voice-synthesis neuroprosthesis で <strong>non-speech 時に silence を返す</strong>ことが重要であり、しかも post-implant day 165 で固定した decoder の性能が <strong>約 15 日後から目立って低下</strong>することを示しています。したがって、online 系では「その日に動いた」だけでは足りず、<strong>fixed decoder が何日持つか</strong>、<strong>再較正にどれだけ依存したか</strong>、<strong>silence / abstention をどう使ったか</strong>まで含めて drift を評価する必要があります。
</p>

<h2>縦断評価で最低限分けて残すもの</h2>
<table>
<thead>
<tr>
<th>監査項目</th>
<th>最低限ほしいもの</th>
<th>足りないと止まる主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state sensitivity</strong></td>
<td>覚醒、行動量、無意図運動、task engagement、薬理状態などの同時計測と、その条件別性能差。</td>
<td>「同じ被験者で安定」「短期不一致は誤差」とは言えません。</td>
</tr>
<tr>
<td><strong>fixed-model stability</strong></td>
<td>再学習なし decoder / readout を何日・何週 hold したか、その interval ごとの劣化曲線。</td>
<td>「trait backbone がある」「長期運用できる」とは言えません。</td>
</tr>
<tr>
<td><strong>unit identity audit</strong></td>
<td>sorting version、drift correction、unit-match method / probability、dropout / new-unit rate、implant age、impedance や tissue-response proxy。</td>
<td>「same neuron across days」「single-unit level での長期安定」が受理できません。</td>
</tr>
<tr>
<td><strong>population backbone</strong></td>
<td>latent dynamics、representational similarity、cross-session identification など、関係構造の安定性。</td>
<td>単一ユニット変化の中でも何が保たれているかを示せません。</td>
</tr>
<tr>
<td><strong>recalibration burden</strong></td>
<td>再較正頻度、所要時間、supervised/unsupervised の別、recovery time、失敗時 fallback。</td>
<td>online 安定性を accuracy や WER だけで語ってしまいます。</td>
</tr>
</tbody>
</table>

<h2>よくある誤読と、このサイトでの降格ルール</h2>
<table>
<thead>
<tr>
<th>危険な読み方</th>
<th>なぜ危険か</th>
<th>このサイトでの扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同日で反応が似たから trait がある</strong></td>
<td>state fluctuation を十分に潰していない可能性があります。</td>
<td>同日一致は state-level evidence に留め、trait claim へ上げません。</td>
</tr>
<tr>
<td><strong>単一 neuron / voxel が変わったから trait はない</strong></td>
<td>population-level の geometry や latent dynamics が保たれている可能性があります。</td>
<td>unit-level drift と population backbone を別に報告させます。</td>
</tr>
<tr>
<td><strong>再較正後に性能が戻ったから drift は問題ない</strong></td>
<td>それは drift が無い証拠ではなく、運用が drift を吸収しただけかもしれません。</td>
<td>再較正回数・時間・失敗率を性能の一部として別出しします。</td>
</tr>
<tr>
<td><strong>fixed decoder が崩れたので脳表現そのものが崩れた</strong></td>
<td>interface、feature extraction、channel turnover の問題かもしれません。</td>
<td>biological drift と interface / decoder drift の切り分けを要求します。</td>
</tr>
<tr>
<td><strong>silence / abstention が多いので性能が低いだけだ</strong></td>
<td>low-confidence 条件を無理に出力しない方が、実運用では安全な場合があります。</td>
<td>coverage と risk、silence 率と誤出力率をセットで出させます。</td>
</tr>
</tbody>
</table>

<h2>この議論を提出物仕様へどう落とすか</h2>
<p>
ここまでの文献整理から見えるのは、state・trait・drift の区別が重要だというだけでは不十分で、<strong>その区別を提出物の欄として固定しないと、same-day の成功が cross-day / longitudinal claim へ再び流れ込む</strong>という点でございます。そこで本サイトでは、<a href="https://mind-upload.com/verification.html#temporal-validity-card">Verification の Temporal Validity Card</a> を追加し、時間軸の外挿を独立に監査します。
</p>
<table>
<thead>
<tr>
<th>Temporal Validity Card で固定すること</th>
<th>このページの概念とどう対応するか</th>
<th>最低限のログ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>evaluation family / horizon</strong></td>
<td>state の議論か、trait backbone の議論か、longitudinal / closed-loop の議論かを混ぜません。</td>
<td>within-session / cross-session / cross-subject / multiday / closed-loop の別、セッション間隔、評価日数。</td>
</tr>
<tr>
<td><strong>state annotation</strong></td>
<td>その日の覚醒、行動、sleep / wake 履歴、薬理状態が結果をどこまで動かしたかを残します。</td>
<td>行動量、覚醒指標、無意図運動、薬理条件、recording context。</td>
</tr>
<tr>
<td><strong>fixed-model interval</strong></td>
<td>trait backbone と fixed decoder の安定性を同一視しません。</td>
<td>再学習なしモデルを何日 hold したか、interval ごとの劣化曲線。</td>
</tr>
<tr>
<td><strong>interface / decoder drift audit</strong></td>
<td>biological drift と、再装着・probe drift・sorting・feature shift を分けます。</td>
<td>再装着有無、impedance、channel dropout、sorting version、unit-match probability、drift correction。</td>
</tr>
<tr>
<td><strong>population backbone metric</strong></td>
<td>unit-level の不安定さがあっても relation / manifold が残るかを別に見ます。</td>
<td>latent dynamics、representational similarity、cross-session identification、map homeostasis 指標。</td>
</tr>
<tr>
<td><strong>recalibration burden / fallback</strong></td>
<td>運用が drift を吸収したのか、そもそも drift が小さいのかを切り分けます。</td>
<td>再較正頻度、所要時間、supervised / unsupervised の別、silence / abstention、recovery time。</td>
</tr>
</tbody>
</table>

<strong>このページから直接出る運用規則</strong>
<p>
Temporal Validity Card が無い場合、本サイトでは原則として <strong>within-session result</strong>、<strong>limited cross-session decode</strong>、または <strong>short-horizon online demo</strong> として扱います。逆に、state annotation、fixed-model interval、interface drift audit、recalibration burden がそろっていれば、同じ cross-day result でもどこまで安全に読めるかを明示できます。
</p>

<h2>このサイトで採用する運用ルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>state と trait を同じ指標で報告しない：</strong>短期変動と長期骨格を別列で残します。</li>
<li><strong>trait は骨格として示す：</strong>latent dynamics、similarity matrix、fingerprint、stable subspace のいずれかを明示します。</li>
<li><strong>drift は 2 系統に分ける：</strong>生体側 representational drift と interface / decoder drift を別ログにします。</li>
<li><strong>fixed decoder interval を必ず出す：</strong>再較正なしで何日もったかを hidden にしません。</li>
<li><strong>recalibration burden も性能です：</strong>再較正頻度、所要時間、fallback の内訳を accuracy と別に出します。</li>
<li><strong>縦断比較には session 日付を入れる：</strong>日内、日間、週単位、月単位のどれかを明記します。</li>
</ul>

<h2>参考文献</h2>
<ol>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <em>Nature Neuroscience</em>, 22, 1677-1686. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Benisty, H., Barson, D., Moberly, A. H., Lohani, S., Tang, L., Coifman, R. R., Crair, M. C., Cardin, J. A., &amp; Higley, M. J. (2024). Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <em>Nature Neuroscience</em>, 27, 148-158. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Gallego, J. A., Perich, M. G., Chowdhury, R. H., Solla, S. A., &amp; Miller, L. E. (2020). Long-term stability of cortical population dynamics underlying consistent behavior. <em>Nature Neuroscience</em>, 23, 260-270. <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">doi:10.1038/s41593-019-0555-4</a></li>
<li>Finn, E. S., Shen, X., Scheinost, D., Rosenberg, M. D., Huang, J., Chun, M. M., Papademetris, X., &amp; Constable, R. T. (2015). Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. <em>Nature Neuroscience</em>, 18(11), 1664-1671. <a href="https://doi.org/10.1038/nn.4135" target="_blank">doi:10.1038/nn.4135</a></li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <em>Science</em>, 372(6539), eabf4588. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>Pachitariu, M., et al. (2024). Spike sorting with Kilosort4. <em>Nature Methods</em>, 21, 914-921. <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">doi:10.1038/s41592-024-02595-5</a></li>
<li>Trautmann, E. M., Stavisky, S. D., Lahiri, S., et al. (2019). Accurate estimation of neural population dynamics without spike sorting. <em>Neuron</em>, 103(2), 292-308.e4. <a href="https://doi.org/10.1016/j.neuron.2019.05.003" target="_blank">doi:10.1016/j.neuron.2019.05.003</a></li>
<li>van Beest, E. H., Jia, X., Deng, X., et al. (2024). Tracking neurons across days with high-density probes. <em>Nature Methods</em>. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
<li>Gregory, N. S., et al. (2023). Structural and functional changes of deep layer pyramidal neurons surrounding implanted microelectrode arrays in rat motor cortex. <em>Journal of Neural Engineering</em>, 20(4), 046022. <a href="https://doi.org/10.1088/1741-2552/ace8ac" target="_blank">doi:10.1088/1741-2552/ace8ac</a></li>
<li>Roth, Z. N., &amp; Merriam, E. P. (2023). Representations in human primary visual cortex drift over time. <em>Nature Communications</em>, 14, 4422. <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">doi:10.1038/s41467-023-40144-w</a></li>
<li>Noda, T., Kienle, E., Eppler, J.-B., Aschauer, D. F., Kaschube, M., Loewenstein, Y., &amp; Rumpel, S. (2025). Homeostasis of a representational map in the neocortex. <em>Nature Neuroscience</em>, 28, 1533-1545. <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">doi:10.1038/s41593-025-01982-7</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., Avansino, D. T., Pun, T. K., Gross, R., Hosman, T., Singer-Clark, T., Kapitonava, A., Hochberg, L. R., Simeral, J. D., Shenoy, K. V., Druckmann, S., Henderson, J. M., &amp; Willett, F. R. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <em>Nature Biomedical Engineering</em>. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., Hou, X., Iacobacci, C., Miller, L. M., Hochberg, L. R., Brandman, D. M., &amp; Stavisky, S. D. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644, 145-152. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
</ol>

<h2>次にどこへ戻るか</h2>
<p>
不確実性や coverage-risk へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention">不確実性・校正・棄権</a>、online 運用のログ設計へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ・遅延・ジッタ・安全停止</a>、全体の合否ルールへ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a> をご利用ください。
</p>
