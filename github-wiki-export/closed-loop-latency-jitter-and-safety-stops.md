# Wiki：閉ループ・遅延・ジッタ・安全停止

> 閉ループの時間要件は 1 つの数値ではなく、ループ種別ごとに変わります
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: Learning guide / evidence refresh

## このページの役割
このページは、Mind-Upload の L3『閉ループ』で重要になる遅延、ジッタ、ドリフト、安全停止の違いを、一次文献に沿って整理する wiki です。オフライン精度が高いモデルでも、ループの帯域とアクチュエータの種類が違えば必要な timing budget も変わることを明確にするのが目的です。

## 正確さの前提
ここでは『全ループに共通の固定閾値』は置きません。課題、対象周波数、出力機構、安全要求に応じて、実測した end-to-end 指標で判断する前提で書いています。

## 公開ページへ戻る
- [検証基盤](https://mind-upload.com/verification.html)
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: イベント同期と観測ログ](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - 遅延、ジッタ、ドリフトを何として残すかを補います。
- [Wiki: 不確実性・校正・棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 低信頼時に『出さない』設計の考え方を補います。
- [Wiki: 更新・分岐・停止規則](https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules) - freeze と停止規則を運用としてどう切り分けるかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページへ戻れます。

## いま分かっていること
- オフライン精度と閉ループ安定性は別の主張であり、同じスコアでは監査できません。
- 遅延とジッタの許容範囲は、state feedback、ERP/command BCI、streaming communication、phase-locked stimulation、burst-driven neuromodulation で異なります。
- 入力、処理、出力、戻りを end-to-end で実測しないと、実運用の timing は分かりません。
- within-session の高速化だけでは不十分で、recalibration burden、clinic/home 転移、programming burden も別に残します。

## まだ分かっていないこと
- WBE に必要な閉ループ帯域が、どのループ種別にどこまで跨るかは未確定です。
- phase-specific な制御で必要な精度を、非侵襲ヒト実験の全タスクへ一般化できるとはまだ言えません。
- 長期運用での drift、再較正頻度、programming burden のどこからを『不安定』または『非実用』とみなすかは課題依存です。

---

<h2>いちばん短い結論</h2>
<p>
<strong>閉ループ</strong>は「出力が次の入力を変える系」です。ただし、そこで要求される timing は 1 つではありません。<strong>alpha neurofeedback</strong>、<strong>P300/ERP BCI</strong>、<strong>streaming speech neuroprosthesis</strong>、<strong>phase-locked stimulation</strong>、<strong>adaptive DBS</strong> では、支配的な時間スケールも壊れ方も違います。したがって、<strong>共通の 1 ms 閾値</strong>や<strong>共通の 10 ms 閾値</strong>をサイト全体の正解として置くのは危険です。
</p>

<strong>今回の整理で先に固定したこと</strong>
<p>
このページでは、「どれくらい速ければ十分か」を抽象論で語るのではなく、<strong>どのループ型を扱っているのか</strong>、<strong>そのループで何を壊す遅延なのか</strong>、<strong>何を hardware で実測したのか</strong>を先に固定します。event marker の高速化、LSL の同期、phase 追跡、停止規則は、それぞれ別の層の話です。
</p>

<h2>なぜ固定閾値が危険なのか</h2>
<p>
Wilson ら (2010) は、mu rhythm 振幅のような比較的ゆっくりした BCI 指標では、<strong>10 ms 程度の小さな遅れ</strong>が直ちに本質を壊すとは限らない一方、系全体の latency/jitter を測らないと出力経路や表示器が律速になることを示しました。逆に、Belinskaia ら (2020) は parietal alpha neurofeedback で、<strong>追加 250 ms / 500 ms 遅延</strong>が学習効果を悪化させることを示しました。さらに、Mansouri ら (2018) と Zrenner ら (2018) のような phase-targeting 系では、遅延は単なる ms 値ではなく、<strong>対象周波数に対する位相誤差</strong>として評価すべきです。
</p>

<strong>読み方の原則</strong>
<p>
「低遅延が良い」は一般論として正しいですが、そこから直ちに「全ループで microsecond 級が必須」「全ループで 1 ms 以下が必須」とは言えません。正しい問いは、<strong>どのループ帯域で、どの誤差が、何を壊すのか</strong>です。
</p>

<h2>まず 5 つのループ型に分ける</h2>
<table>
<thead>
<tr>
<th>ループ型</th>
<th>典型例</th>
<th>文献が示すこと</th>
<th>このサイトで先に残すべきログ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state feedback / neurofeedback</strong></td>
<td>alpha パワーを見て視覚フィードバックを返す系です。</td>
<td>Belinskaia ら (2020) は、追加 250 / 500 ms 遅延が alpha neurofeedback 学習を悪化させると示しました。短い遅延ほど学習に有利でした。</td>
<td>中央値/P95/P99 の feedback latency、表示経路、追加遅延に対する性能劣化曲線です。</td>
</tr>
<tr>
<td><strong>ERP / command BCI</strong></td>
<td>P300 speller や event-related control です。</td>
<td>Wilson ら (2010) は timing を分解して hardware 実測する必要を示し、Mowla ら (2017) は latency jitter が classification を下げるため、補正しても悪影響は完全には消えないと示しました。</td>
<td>block jitter、刺激 onset 実測、trial-to-trial latency variance、分類性能との対応です。</td>
</tr>
<tr>
<td><strong>streaming communication / speech neuroprosthesis</strong></td>
<td>brain-to-text や brain-to-voice を、音声や文字として連続に返す系です。</td>
<td>Littlejohn ら (2025) は 80 ms 刻みの streaming brain-to-voice を示し、Wairagkar ら (2025) は raw neural input から 10 ms 未満で音声合成を返しつつ、non-speech や overlapping speech では silence を返す loop を示しました。ここでは平均 latency だけでなく、tail latency、audio output path、silence / abstention が中心指標です。</td>
<td>per-step inference latency、cue-to-output latency 分布、audio driver latency、silence / false-speech rate、dropout、recalibration event です。</td>
</tr>
<tr>
<td><strong>phase-locked stimulation</strong></td>
<td>EEG 位相に合わせて TMS/tES を打つ系です。</td>
<td>Mansouri ら (2018) は位相遅れを theta/alpha で評価し、Zrenner ら (2018) は millisecond-resolution EEG-triggered TMS で brain state 依存性を実証しました。ここでは ms より位相誤差が中心です。</td>
<td>対象周波数、位相誤差分布、推定位相の信頼度、missed trigger、phase ずれ時の fallback 条件です。</td>
</tr>
<tr>
<td><strong>burst/state-triggered neuromodulation</strong></td>
<td>beta burst を使う adaptive DBS です。</td>
<td>Little ら (2013) は pathological beta を feedback に使う proof-of-principle を示し、Tinkhauser ら (2017) は adaptive DBS が <strong>100–600 ms</strong> の短い burst と <strong>600 ms 超</strong>の長い burst の分布を変えることを示しました。支配時間は phase-locking より遅いです。</td>
<td>biomarker 検出遅延、burst false positive/false negative、ramp-up/ramp-down、停止回数です。</td>
</tr>
</tbody>
</table>

<h2>2026-03 文献監査：長期運用で増える 3 つの壁</h2>
<p>
旧版の弱点は、閉ループを <strong>same-session の timing 問題</strong>として整理しすぎていた点でございます。2024-2026 年の一次文献を並べると、speech BCI と chronic aDBS では、通常の latency/jitter に加えて <strong>tail latency と output path</strong>、<strong>recalibration burden</strong>、<strong>naturalistic deployment / programming burden</strong> が別の壁として立ちます。したがって本サイトでは、ループが「動いた」だけでは L3 を上げず、以下の 3 軸を別ログで要求します。
</p>
<table>
<thead>
<tr>
<th>壁</th>
<th>一次文献が今支持すること</th>
<th>このページでの修正方針</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>tail latency / output path</strong></td>
<td>Littlejohn ら (2025) は 80 ms 刻みの streaming speech を示しつつ、go cue から実音声までの遅延分布を別に出しました。Wairagkar ら (2025) は 10 ms 未満の neural-to-voice synthesis を示しましたが、closed-loop feedback では audio driver が別律速になることも明示しました。</td>
<td>推論器の平均 latency だけでは不十分とし、module-wise latency、cue-to-output tail、audio playback path、silence / abstention の挙動を別々に残します。</td>
</tr>
<tr>
<td><strong>recalibration burden / drift</strong></td>
<td>Wilson ら (2025) は、frequent daily supervised recalibration が日常利用の大きな障害であるとし、multiple timescales の drift を扱う unsupervised recalibration を 1 か月の closed-loop で評価しました。</td>
<td><code>time since last supervised calibration</code>、unsupervised adaptation の有無、性能劣化曲線、recovery time、人手介入時間を主要ログへ上げます。</td>
</tr>
<tr>
<td><strong>naturalistic deployment / programming burden</strong></td>
<td>Oehrn ら (2024) は chronic aDBS を in-clinic と at-home の両方で評価し、naturalistic environment まで含めて比較しました。Cascino ら (2026) は chronic cDBS の連続症例 20 例中 9 例が aDBS 適格、2025 年 7 月時点で 5 例継続と報告し、technical / programming constraints が deployability を左右することを示しました。</td>
<td>lab 内の成功だけでなく、clinic/home 転移、eligibility、continuation、programming changes、stimulation duty cycle を deployment 側の必須ログとして残します。</td>
</tr>
</tbody>
</table>

<strong>ここでの批判点</strong>
<p>
したがって、「速い loop が 1 回動いた」「adaptive controller が症状を少し下げた」だけでは、長期運用可能とは読みません。<strong>tail latency</strong>、<strong>人手再較正</strong>、<strong>在宅での成立</strong>が別々に通って初めて、deployable closed loop に近づいたと読めます。
</p>

<h2>何を end-to-end で測るのか</h2>
<p>
Wilson ら (2010) の重要点は、<strong>signal processing latency だけを測っても不十分</strong>だということです。閉ループで効くのは、入力から出力までの全経路です。表示器、OS、ドライバ、音声系、刺激器が別の律速になることがあります。
</p>
<table>
<thead>
<tr>
<th>区間</th>
<th>最低限知りたいこと</th>
<th>典型的な実測法</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力</strong></td>
<td>センサーが実際にいつ変化を取り込んだかです。</td>
<td>TTL、既知パルス、DAQ 入力、刺激器の marker 出力です。</td>
</tr>
<tr>
<td><strong>処理</strong></td>
<td>前処理、推定、意思決定にどれだけ時間がかかったかです。</td>
<td>software timestamp、block duration、CPU/GPU ログです。</td>
</tr>
<tr>
<td><strong>出力</strong></td>
<td>表示、音、刺激、制御信号がいつ本当に出たかです。</td>
<td>フォトダイオード、マイク、loopback、刺激アーチファクト onset です。</td>
</tr>
<tr>
<td><strong>戻り</strong></td>
<td>出力の影響がいつ次の入力へ返ってきたかです。</td>
<td>closed-loop task 内での再検出、環境センサー、身体応答ログです。</td>
</tr>
</tbody>
</table>

<strong>平均だけでは足りません</strong>
<p>
閉ループでは、平均遅延よりも <strong>P95/P99/worst-case</strong> や <strong>trial-to-trial jitter</strong> が壊しやすいことがあります。特に phase-targeting や safety-critical loop では、平均値だけ出しても安心材料になりません。
</p>

<h2>LSL と event marker は何を保証し、何を保証しないか</h2>
<p>
Kothe ら (2025) の LSL 論文は、LSL が <strong>millisecond-scale で十分な neurobehavioral research</strong> の同期に有用で、offset correction や jitter compensation を提供することを示しています。一方で、これは <strong>LAN 上の software-based synchronization</strong> の話であり、刺激器や表示器の物理出力がいつ起きたかを自動で保証するわけではありません。
</p>
<p>
Appelhoff と Stenner (2021) は、USB microcontroller による event marking が <strong>1 ms 未満の latency</strong> を出せることを示しました。ただし、これも主に <strong>marker path</strong> の精度です。marker が速くても、表示器、音声経路、刺激器、推定器まで含めた end-to-end loop が同じ精度とは限りません。
</p>

<h4>ここで分けるべきこと</h4>
<ul>
<li><strong>LSL：</strong>複数 stream の共通時刻系と offset 補正を助けます。</li>
<li><strong>TTL / MCU marker：</strong>イベントを acquisition 側へ刻む精度を上げます。</li>
<li><strong>photodiode / microphone / loopback：</strong>実際の output onset を外部から検証します。</li>
<li><strong>phase 追跡器：</strong>対象周波数に対して、どれだけ位相ずれが残るかを別に監査します。</li>
</ul>

<h2>棄権と freeze と安全停止は別物です</h2>
<table>
<thead>
<tr>
<th>仕組み</th>
<th>主目的</th>
<th>典型トリガー</th>
<th>最低限残すこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>棄権</strong></td>
<td>低信頼時に無理な出力を避けるためです。</td>
<td>分類確率不足、phase 推定信頼度不足、OOD 検出です。</td>
<td>棄権率、棄権時の信頼度閾値、棄権後の状態です。</td>
</tr>
<tr>
<td><strong>hold-last-output / silence fallback</strong></td>
<td>短い不確実性や非発話区間で、誤出力を増やさず連続性を保つためです。</td>
<td>non-speech 区間、decoder blank、短い dropout、audio buffer underrun です。</td>
<td>発動率、最大継続時間、false speech 抑制率、解除遅延です。</td>
</tr>
<tr>
<td><strong>freeze / 一時停止</strong></td>
<td>再較正や原因確認のためです。</td>
<td>clock offset 増大、packet loss、drift 逸脱、再同期要求です。</td>
<td>発動理由、継続時間、再開条件、再較正内容です。</td>
</tr>
<tr>
<td><strong>安全停止 / containment</strong></td>
<td>危険な actuation を止めるためです。</td>
<td>P99 latency budget 超過、異常振幅、刺激禁止位相、出力飽和です。</td>
<td>停止条件、停止回数、直前の latency/phase/error、手動復帰条件です。</td>
</tr>
</tbody>
</table>

<strong>性能問題と安全問題を混ぜない</strong>
<p>
「うまく出せなかったので出さない」のか、「短い空白を silence でつなぐ」のか、「系が壊れていそうなので保留する」のか、「危険なので止める」のかは、運用上まったく別です。全部を 1 つの『停止』にまとめると、レビュー時に原因が追えなくなります。
</p>

<h2>最低限残したいログ</h2>

<h4>Checklist</h4>
<ul>
<li><strong>loop class：</strong>state feedback、ERP/command、speech / streaming、phase-locked、burst-triggered のどれか。</li>
<li><strong>end-to-end latency：</strong>中央値、P95、P99、worst-case を別々に残します。</li>
<li><strong>module-wise latency：</strong>入力、推論、出力、再帰入力を分け、どこが律速かを残します。</li>
<li><strong>jitter の定義：</strong>SD、IQR、peak-to-peak のどれかを明記します。</li>
<li><strong>clock offset / drift：</strong>LSL や hardware marker の補正前後を残します。</li>
<li><strong>marker 検証法：</strong>TTL、MCU、photodiode、microphone、loopback のどれで実測したかを書きます。</li>
<li><strong>speech / streaming 系の追加指標：</strong>cue-to-output の tail latency、audio driver latency、silence / hold-last-output 率、false speech rate を残します。</li>
<li><strong>phase/burst 系の追加指標：</strong>位相誤差分布、missed trigger、burst 検出遅延、false positive/negative です。</li>
<li><strong>棄権 / freeze / 安全停止：</strong>発動回数、直前状態、復帰条件を残します。</li>
<li><strong>longitudinal burden：</strong>最後の supervised recalibration からの経過時間、unsupervised adaptation の有無、recalibration に要した人手 / 時間を残します。</li>
<li><strong>naturalistic deployment：</strong>clinic / home の成績差、eligibility、continuation、programming change、duty cycle を残します。</li>
<li><strong>性能劣化曲線：</strong>人工的に遅延を足したとき、どこで崩れるかを残します。</li>
</ul>

<h2>L3 の主張を読むときの 6 問</h2>
<ol>
<li><strong>どの loop class を扱っているか書いてあるか：</strong> slow feedback、speech streaming、phase-locked、aDBS を同じ表で語っていないかを見ます。</li>
<li><strong>end-to-end だけでなく module-wise 実測があるか：</strong> software timestamp だけで済ませず、入力・推論・出力 path のどこが律速かを確認します。</li>
<li><strong>speech / streaming 系なら silence と output path が出ているか：</strong> false speech、audio driver、hold-last-output を隠していないかを見ます。</li>
<li><strong>delay を位相誤差や burst 時間へ写像しているか：</strong> ただの ms 値で済ませていないかを見ます。</li>
<li><strong>recalibration burden と clinic/home 転移が出ているか：</strong> within-session 成功だけで deployable と読んでいないかを確認します。</li>
<li><strong>棄権・silence fallback・freeze・安全停止が分離されているか：</strong> 危険時と低信頼時の運用が曖昧でないかを確認します。</li>
</ol>

<h2>参考文献</h2>
<ol>
<li>Wilson JA, Mellinger J, Schalk G, Williams JC. A procedure for measuring latencies in brain-computer interfaces. <em>IEEE Trans Biomed Eng.</em> 2010;57(7):1785-1797. <a href="https://doi.org/10.1109/TBME.2010.2047259" target="_blank">doi:10.1109/TBME.2010.2047259</a></li>
<li>Thompson DE, Warschausky SA, Huggins JE. Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. <em>J Neural Eng.</em> 2013;10(1):016006. <a href="https://doi.org/10.1088/1741-2560/10/1/016006" target="_blank">doi:10.1088/1741-2560/10/1/016006</a></li>
<li>Mowla MR, Huggins JE, Thompson DE. Enhancing P300-BCI performance using latency estimation. <em>Brain Comput Interfaces.</em> 2017;4(3):137-145. <a href="https://doi.org/10.1080/2326263X.2017.1338010" target="_blank">doi:10.1080/2326263X.2017.1338010</a></li>
<li>Belinskaia A, Smetanin N, Lebedev M, Ossadtchi A. Short-delay neurofeedback facilitates training of the parietal alpha rhythm. <em>J Neural Eng.</em> 2020;17(6):066012. <a href="https://doi.org/10.1088/1741-2552/abc8d7" target="_blank">doi:10.1088/1741-2552/abc8d7</a></li>
<li>Mansouri F, Fettes P, Schulze L, et al. A Real-Time Phase-Locking System for Non-invasive Brain Stimulation. <em>Front Neurosci.</em> 2018;12:877. <a href="https://doi.org/10.3389/fnins.2018.00877" target="_blank">doi:10.3389/fnins.2018.00877</a></li>
<li>Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <em>Brain Stimul.</em> 2018;11(2):374-389. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. <em>Ann Neurol.</em> 2013;74(3):449-457. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <em>Brain.</em> 2017;140(4):1053-1067. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Appelhoff S, Stenner T. In COM we trust: Feasibility of USB-based event marking. <em>Behav Res Methods.</em> 2021;53(6):2450-2455. <a href="https://doi.org/10.3758/s13428-021-01571-z" target="_blank">doi:10.3758/s13428-021-01571-z</a></li>
<li>Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. <em>Imaging Neurosci.</em> 2025;3:IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Littlejohn KT, Dabagia M, Ladwig A, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nat Neurosci.</em> 2025. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. <em>Nature.</em> 2025. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. <em>Nat Biomed Eng.</em> 2025. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <em>Nat Med.</em> 2024. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. <em>npj Parkinsons Dis.</em> 2026. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
</ol>

<h2>次にどこへ戻るか</h2>
<p>
L3 の全体設計へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、EEG と同期の実務へ戻るなら <a href="https://mind-upload.com/eeg_101.html">EEG入門</a>、Roadmap の I1 / I8 へ戻るなら <a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップ</a> をご利用ください。
</p>
