# Wiki：イベント同期と観測ログの基本

> 信号だけでなく、ラベルの出どころを残さないと比較は崩れます
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: Practical guide

## このページの役割
このページは、なぜ raw EEG の波形だけでは再現可能な研究にならないのかを、イベントマーカー、刺激ログ、時刻同期、manual scoring、report-derived label の観点から説明する wiki です。『波形ファイルはあるのに比較できない』だけでなく、『label はあるのに provenance が曖昧で比較できない』という事故も防ぐことが目的です。

## 正確さの前提
ここで扱うのは最低限の観測ログと label provenance です。課題によって追加のメタデータが必要になりますが、出来事と注釈の由来を残すという原則は変わりません。

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
- annotation provenance を書かないと、同じ label 名でも再利用不能になることがあります。
- bad channel / bad segment の記録は、除外の透明性に直結します。

## まだ分かっていないこと
- どこまで細かいメタデータを全課題で共通必須にするかは、運用設計の途上です。
- 複雑なマルチモーダル同時計測で、最低限の同期ログをどう統一するかは今後の課題です。
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
<td><strong>`channels.tsv`</strong></td>
<td>各チャンネルの状態や種類を残します。</td>
</tr>
<tr>
<td><strong>JSON メタデータ</strong></td>
<td>サンプリング周波数、参照法、計測条件などを残します。</td>
</tr>
<tr>
<td><strong>QC / 除外ログ</strong></td>
<td>bad channel、bad segment、ノイズ、除外理由を外部ログや派生物で残します。</td>
</tr>
</tbody>
</table>

<h2>後から復元しにくい情報</h2>
<p>
次の情報は、記録していなければ後から推測で埋めるしかなくなります。
</p>
<ul>
<li><strong>刺激提示の正確な時刻：</strong>大まかな順番では代用できません。</li>
<li><strong>実際の遅延やジッタ：</strong>機器やソフトの設定だけでは足りないことがあります。</li>
<li><strong>除外した理由：</strong>後から見ても、なぜ捨てたか分からなくなります。</li>
<li><strong>label provenance：</strong>manual scoring か report-derived label かを書かなければ、同じ正解ラベルでも比較できません。</li>
<li><strong>scoring manual / scorer：</strong>Sleep-EDF のような manual hypnogram は、基準と scorer を失うと再利用の意味が変わります。</li>
<li><strong>report usage flag：</strong>TUH 系では report を見てよい評価か、signal-only かを後から復元できません。</li>
<li><strong>その場の運用メモ：</strong>電極トラブルや同期ミスは、波形だけでは読み取れません。</li>
</ul>

<h2>参考文献</h2>
<ul>
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
