# Wiki：EEG の基本

> EEG を魔法の読心術にしないための基礎知識
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Beginner guide

## このページの役割
このページは、EEG が何を測っているのかを初歩から説明する wiki です。難しい式より先に、『どんな信号がどこで混ざって見えているのか』『なぜ前処理や QC が重要なのか』を理解することを目標にします。

## 正確さの前提
EEG を過大評価しないために限界も強調しますが、だからといって役に立たないと言うページではありません。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [ハンズオン](https://mind-upload.com/hands_on.html)

## 関連 Wiki
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - EEG が WBE 全体のどこに入るかを先に見たい場合はこちらです。
- [Wiki: EEG前処理とQC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 前処理やログの取り方を、実務に寄せて整理します。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜ EEG でも標準や QC が必要かを理解できます。

## いま分かっていること
- EEG はミリ秒単位の時間変化を見るのが得意です。
- 観測される信号は多くの活動が混ざった結果であり、解釈には前提が必要です。
- 公開データでも、前処理とベースライン比較の練習は十分できます。

## まだ分かっていないこと
- 非侵襲 EEG だけで、脳内部の詳細な因果構造まで十分に再構成できるかは未解決です。
- 前処理の選び方が、どの課題でどこまで結論を変えるかは一律ではありません。

---

<h2>EEG は何を見ているのか</h2>
<p>
EEG は、頭皮につけた電極で電位差を測る方法です。つまり、脳の中を直接カメラで見ているわけではなく、たくさんの活動が重なって外まで伝わってきた<strong>混ざった信号</strong>を読んでいます。
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
