# Wiki：イベント同期と観測ログの基本

> 信号だけでなく、ラベルの出どころを残さないと比較は崩れます
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: Practical guide

## このページの役割
このページは、なぜ raw EEG の波形だけでは再現可能な研究にならないのかを、イベントマーカー、イベント意味論、時刻同期、manual scoring、report-derived label の観点から説明する wiki です。『波形ファイルはあるのに比較できない』だけでなく、『label はあるのに provenance が曖昧で比較できない』『時刻はあるのに clock domain が曖昧で比較できない』という事故も防ぐことが目的です。

## 正確さの前提
ここで扱うのは最低限の観測ログと label provenance ですが、2026-03 の更新では BIDS の器、HED の意味論、LSL の同期、Motion-BIDS 型 metadata の役割差も明示します。課題ごとに追加のメタデータは必要ですが、出来事・意味・時計系を分けて残すという原則は変わりません。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [ハンズオン](https://mind-upload.com/datasets.html#l0-practice)

## 関連 Wiki
- [Wiki: EEG前処理とQC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 観測後にどこで結果が変わるかを補います。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜログが公共財になるかを補います。
- [Wiki: 閉ループ・遅延・ジッタ・安全停止](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - 遅延やジッタを、L3 の閉ループ評価でどう読むかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 学習用ページ全体へ戻れます。

## いま分かっていること
- 波形ファイルだけでは、課題や刺激との対応を十分に再構成できないことがあります。
- 遅延、ジッタ、ドリフトを記録しないと、時間解像度の強みが崩れます。
- BIDS / EEG-BIDS は events と metadata の器を与えますが、cross-study 再利用には HED のような機械可読な意味論が有効です。
- LSL や trigger 線があっても、clock domain と device-side delay を明示しないと時間忠実度は監査できません。
- annotation provenance を書かないと、同じ label 名でも再利用不能になることがあります。
- bad channel / bad segment の記録は、除外の透明性に直結します。

## まだ分かっていないこと
- どこまで細かいメタデータを全課題で共通必須にするかは、運用設計の途上です。
- 複雑なマルチモーダル同時計測で、最低限の同期ログをどう統一するかは今後の課題です。
- event semantics を HED / ontology / scorer rule のどこまでで共通必須化するかは、まだ調整が要ります。
- report-derived label を signal-only benchmark からどこまで分離すべきかの site-wide schema は、まだ固定途上です。

---

<h2>いちばん短い答え</h2>
<p>
raw EEG は「電気信号の並び」です。しかし研究で知りたいのは、多くの場合「<strong>いつ、何が起きたときの信号か</strong>」です。その対応表がないと、あとから見ても意味があいまいになります。
</p>

<strong>2026-03 文献監査で追加した前提</strong>
<p>
このページでは、event log だけでなく <strong>label provenance</strong> も観測ログとして扱います。つまり、同じ「正解ラベル」でも、それが <strong>annotation channel</strong> なのか、<strong>専門家の区間注釈</strong> なのか、<strong>whole-night hypnogram</strong> なのか、<strong>医師レポート由来ラベル</strong> なのかを書かなければ、比較可能な benchmark にはなりません。
</p>

<strong>今回もっとも修正すべきだった弱点</strong>
<p>
現行サイトは「イベントと同期が重要」とは書けていましたが、<strong>時刻の器</strong>、<strong>イベント意味論</strong>、<strong>clock alignment</strong> をまだ十分に分離できていませんでした。BIDS task events は <code>events.tsv</code> と JSON sidecar による記述枠を与えますが、Robbins ら (2021) と Hermes ら (2025) が示すように、cross-study 再利用には <strong>HED のような機械可読な意味論</strong>が要ります。また Kothe ら (2025) が示す通り、LSL はネットワーク同期を強くしても、<strong>機器内の throughput delay や刺激提示系の遅延</strong>までは自動では与えません。したがって本サイトでは、イベント忠実度を 1 つの箱ではなく 3 層で監査します。
</p>

<h2>なぜ raw EEG だけでは足りないのか</h2>
<p>
たとえば、課題中に刺激が何回出たか、どのタイミングでボタンを押したか、どの区間がノイズで除外されたかが分からないと、同じ波形を見ても人ごとに解釈が変わります。つまり、波形だけでは「何を比べているのか」が崩れることがあります。
</p>

<h2>イベントマーカーと刺激ログ</h2>
<table>
<thead>
<tr>
<th>記録</th>
<th>何のために要るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>イベントマーカー</strong></td>
<td>刺激提示、反応、状態変化などが、波形のどこに対応するかを示します。</td>
</tr>
<tr>
<td><strong>刺激ログ</strong></td>
<td>どの刺激が、どの順番で、どの条件で出たかを残します。</td>
</tr>
<tr>
<td><strong>反応ログ</strong></td>
<td>被験者のボタン押し、回答、失敗試行などを波形と結び付けます。</td>
</tr>
</tbody>
</table>
<p>
イベントマーカーだけがあっても、刺激の中身や条件名が曖昧だと解析し直しにくくなります。逆に刺激ログだけあっても、EEG の時刻と結び付いていなければ十分ではありません。
</p>

<h2>イベント忠実度は 3 層で監査します</h2>
<table>
<thead>
<tr>
<th>層</th>
<th>ここで固定するもの</th>
<th>欠けると起きやすい誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 時間アンカー</strong></td>
<td>onset / duration、sample index、clock domain、刺激・反応ログとの対応です。</td>
<td>「いつ起きた出来事か」が曖昧になり、epoching や遅延評価が崩れます。</td>
</tr>
<tr>
<td><strong>2. イベント意味論</strong></td>
<td><code>trial_type</code>、条件名、HED tags、manual scoring rule、report usage flag です。</td>
<td>同じ label 名でも意味がずれ、cross-study の meta / mega analysis が壊れます。</td>
</tr>
<tr>
<td><strong>3. 同期と輸送</strong></td>
<td>clock offset、遅延、ジッタ、ドリフト、transport path、resampling / smoothing の有無です。</td>
<td>LSL や trigger があるだけで sub-ms ground truth だと誤読しやすくなります。</td>
</tr>
</tbody>
</table>
<p>
BIDS task events は主に <strong>1 層目の器</strong>を与え、HED は <strong>2 層目の意味論</strong>を補い、LSL は <strong>3 層目の network-level 同期</strong>を支えます。したがって、本サイトではこれらを代替可能な 1 個の道具として扱いません。
</p>

<h2>ラベルの出どころは 4 種類に分けて読む</h2>
<table>
<thead>
<tr>
<th>ラベルの型</th>
<th>代表例</th>
<th>直接表しているもの</th>
<th>最低限残すべき補助ログ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>cue-locked annotation channel</strong></td>
<td>EEG Motor Movement/Imagery の T0 / T1 / T2</td>
<td>課題 cue と motion / imagery onset の設計上のタイミングです。</td>
<td>run ID、task ID、subject ID、visual cue 条件、epoching rule を残します。</td>
</tr>
<tr>
<td><strong>expert interval annotation</strong></td>
<td>CHB-MIT の seizure onset / offset</td>
<td>長時間記録中の event 区間です。</td>
<td>file 順序、gap、case-to-subject 対応、montage 変化を残します。</td>
</tr>
<tr>
<td><strong>manual hypnogram</strong></td>
<td>Sleep-EDF の R&amp;K sleep stage</td>
<td>whole-night の coarse state label です。</td>
<td>scoring manual、scorer ID、night / study 条件、label mapping を残します。</td>
</tr>
<tr>
<td><strong>report-derived / triaged label</strong></td>
<td>TUH EEG / TUSZ の report keyword 検索や clinician report</td>
<td>session / file に付く臨床ラベルや triage 情報です。</td>
<td>report usage flag、patient / session ID、signal-only か multimodal かの宣言を残します。</td>
</tr>
</tbody>
</table>

<h2>時刻同期で見るべき 3 つ</h2>
<table>
<thead>
<tr>
<th>用語</th>
<th>意味</th>
<th>何が困るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>遅延</strong></td>
<td>本当の出来事から記録まで、何 ms ずれているか。</td>
<td>刺激後応答の時刻がずれて解釈を誤ります。</td>
</tr>
<tr>
<td><strong>ジッタ</strong></td>
<td>そのずれが毎回どれくらい揺れるか。</td>
<td>平均化するとピークがぼやけ、反応が弱く見えます。</td>
</tr>
<tr>
<td><strong>ドリフト</strong></td>
<td>長時間の中で時計のずれが増えていくこと。</td>
<td>後半になるほど同期誤差が大きくなります。</td>
</tr>
</tbody>
</table>
<p>
ここでは観測ログとしての意味を説明しています。L3 の閉ループ評価で、これらが end-to-end 安定性や安全停止にどう効くかを見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> が補講になります。
</p>

<h2>LSL は有力ですが、hardware ground truth ではありません</h2>
<p>
Lab Streaming Layer (LSL) は、同一 LAN 内の複数ストリームを同期し、clock offset や stream metadata を一貫して扱う基盤として非常に有用です。Kothe ら (2025) は、LSL が software-based 同期で millisecond precision を達成しうることを示しました。しかし同論文は同時に、<strong>input device の throughput delay や on-device processing delay は LSL 単体では推定・補正できない</strong>ことも明示しています。したがって、LSL を使っていても、表示遅延・音声遅延・アンプ内バッファ遅延を別に測る必要があります。
</p>
<table>
<thead>
<tr>
<th>LSL を使っていても別に残すべきもの</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>timestamp domain</strong></td>
<td>presentation PC、acquisition PC、device clock のどれを基準にしたかを書かないと、時刻差の意味が崩れます。</td>
</tr>
<tr>
<td><strong>device-side delay</strong></td>
<td>アンプ、ディスプレイ、音声出力、マイコンの内部遅延は software timestamp だけでは分かりません。</td>
</tr>
<tr>
<td><strong>drift / resync policy</strong></td>
<td>長時間記録では drift 補正の有無で後半の整列誤差が変わります。</td>
</tr>
<tr>
<td><strong>validation method</strong></td>
<td>photodiode、loopback、TTL、共通信号入力など、どの方法で遅延を見積もったかが必要です。</td>
</tr>
</tbody>
</table>

<h2>スターターデータ 4 件で、何をログとして残すか</h2>

<strong>最後の列は本サイトの運用推論です</strong>
<p>
下の表の <strong>止める誤読</strong> は、各データセットの公式説明と一次文献が直接与えるログの粒度から、本サイトが引く運用上の境界でございます。
</p>

<table>
<thead>
<tr>
<th>データセット</th>
<th>今あるログ</th>
<th>追加で残すべきこと</th>
<th>止める誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td><code>.event</code> と annotation channel は同一で、T0 / T1 / T2 が cue-locked onset を示します。</td>
<td>subject、run、task block、epoching 窓、EOG / EMG 監査結果を残します。</td>
<td>cue-locked motor task の成績を、そのまま spontaneous thought readout と読むことを止めます。</td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>summary / <code>.seizure</code> 注釈、case 構造、file 間 gap、surrogate date が残ります。</td>
<td>case-to-subject 対応、gap 長、連続記録か否か、montage summary を残します。</td>
<td>file を独立試料とみなし、連続無欠損の監視ログだと読むことを止めます。</td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>R&amp;K hypnogram、Fpz-Cz / Pz-Oz EEG、1 Hz event marker が残ります。</td>
<td>scoring manual、scorer、study arm、night ID、AASM へ写像した場合の rule を残します。</td>
<td>100 Hz EEG があるから sub-second sleep event onset も benchmark できる、と読むことを止めます。</td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>patient / session 階層、EDF、clinician report、subset によっては expert seizure annotation が残ります。</td>
<td>report usage flag、patient / session split、report keyword 由来の triage を残します。</td>
<td>report-assisted clinical label を pure EEG signal-only 成績として書くことを止めます。</td>
</tr>
</tbody>
</table>

<h2>bad channel / bad segment を残す理由</h2>
<p>
ノイズが大きいチャンネルや、体動で壊れた区間を除外すること自体は普通です。ただし、その記録がないと、後から別の人が同じ除外を再現できません。
</p>

<h4>最低限残したいこと</h4>
<ul>
<li><strong>bad channel：</strong>どのチャンネルを、どんな理由で bad としたか。</li>
<li><strong>bad segment：</strong>どの時間区間を除外したか。</li>
<li><strong>閾値：</strong>どの基準で除外したか。</li>
<li><strong>修正方法：</strong>補間したのか、捨てたのか。</li>
</ul>

<h2>EEG-BIDS で最低限ほしい情報</h2>
<table>
<thead>
<tr>
<th>項目</th>
<th>意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>`events.tsv`</strong></td>
<td>刺激や反応の時刻と種類を残します。</td>
</tr>
<tr>
<td><strong>`events.json` と HED</strong></td>
<td><code>trial_type</code> や列の意味を説明し、必要に応じて HED tags でイベント意味論を機械可読にします。</td>
</tr>
<tr>
<td><strong>`channels.tsv`</strong></td>
<td>各チャンネルの状態や種類を残します。</td>
</tr>
<tr>
<td><strong>JSON メタデータ</strong></td>
<td>サンプリング周波数、参照法、計測条件などを残します。</td>
</tr>
<tr>
<td><strong>clock / sync log</strong></td>
<td>clock domain、遅延、ジッタ、ドリフト、同期手段、測定方法を別ログで残します。</td>
</tr>
<tr>
<td><strong>`*_coordsystem.json` と拡張 schema</strong></td>
<td>電極や motion sensor、pose stream を使う場合は、座標系と計測配置を first-class metadata として残します。</td>
</tr>
<tr>
<td><strong>QC / 除外ログ</strong></td>
<td>bad channel、bad segment、ノイズ、除外理由を外部ログや派生物で残します。</td>
</tr>
</tbody>
</table>

<h2>本サイトで必須にする Event Fidelity Card</h2>
<p>
2026-03 の site rule として、イベントを含む dataset card や runbook には、少なくとも次の 5 項目を付けます。これは「理想的に全部そろうまで待つ」という意味ではなく、<strong>何が足りないからどこで主張を止めるか</strong>を先に公開するためのカードでございます。
</p>
<table>
<thead>
<tr>
<th>項目</th>
<th>最低限書くこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Event anchor</strong></td>
<td>onset / duration / sample、元ファイル、どの clock domain 上の時刻か。</td>
</tr>
<tr>
<td><strong>2. Event semantics</strong></td>
<td><code>trial_type</code>、条件定義、HED または同等の語彙、manual scoring / report 由来の別。</td>
</tr>
<tr>
<td><strong>3. Sync evidence</strong></td>
<td>LSL / TTL / photodiode / loopback などの同期手段、測った遅延・ジッタ・ドリフト、測定方法。</td>
</tr>
<tr>
<td><strong>4. Provenance</strong></td>
<td>scorer ID、scoring manual、report usage flag、signal-only か multimodal か。</td>
</tr>
<tr>
<td><strong>5. Geometry / multimodal metadata</strong></td>
<td>電極座標、座標系、motion / video / physiology 追加ストリームがあればその frame と schema。</td>
</tr>
</tbody>
</table>

<h2>後から復元しにくい情報</h2>
<p>
次の情報は、記録していなければ後から推測で埋めるしかなくなります。
</p>
<ul>
<li><strong>刺激提示の正確な時刻：</strong>大まかな順番では代用できません。</li>
<li><strong>clock domain：</strong>どの時計上の時刻かを書かなければ、複数ストリームの差分が解釈できません。</li>
<li><strong>実際の遅延やジッタ：</strong>機器やソフトの設定だけでは足りないことがあります。</li>
<li><strong>device-side delay：</strong>LSL や trigger を使っていても、ディスプレイ・音声・アンプの内部遅延は別に測る必要があります。</li>
<li><strong>除外した理由：</strong>後から見ても、なぜ捨てたか分からなくなります。</li>
<li><strong>label provenance：</strong>manual scoring か report-derived label かを書かなければ、同じ正解ラベルでも比較できません。</li>
<li><strong>event semantics：</strong><code>trial_type</code> の意味、条件名、HED tags が無いと、同じ名前でも別条件かもしれません。</li>
<li><strong>scoring manual / scorer：</strong>Sleep-EDF のような manual hypnogram は、基準と scorer を失うと再利用の意味が変わります。</li>
<li><strong>report usage flag：</strong>TUH 系では report を見てよい評価か、signal-only かを後から復元できません。</li>
<li><strong>座標系と sensor frame：</strong>motion や pose を足したのに frame を残さないと、multimodal 統合が再利用不能になります。</li>
<li><strong>その場の運用メモ：</strong>電極トラブルや同期ミスは、波形だけでは読み取れません。</li>
</ul>

<h2>参考文献</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html" target="_blank">BIDS Specification: Task events</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS Specification: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">Robbins et al. (2021), Building FAIR functionality: annotating events in time series data using HED</a></li>
<li><a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">Hermes et al. (2025), HED library schema for EEG data annotation</a></li>
<li><a href="https://doi.org/10.1162/imag_a_00136" target="_blank">Kothe et al. (2025), The lab streaming layer for synchronized multimodal recording</a></li>
<li><a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al. (2024), Motion-BIDS</a></li>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), The Temple University Hospital EEG Data Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), The Temple University Hospital Seizure Detection Corpus</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009), Sleep classification according to AASM and Rechtschaffen &amp; Kales</a></li>
</ul>

<h2>次にどこへ戻るか</h2>
<p>
EEG 全体の役割へ戻るなら <a href="https://mind-upload.com/eeg_101.html">EEG入門</a>、スターターデータ選びへ戻るなら <a href="https://mind-upload.com/datasets.html">データ&ベンチ</a>、最小ループの手順へ戻るなら <a href="https://mind-upload.com/datasets.html#l0-practice">ハンズオン</a> をご利用ください。
</p>
