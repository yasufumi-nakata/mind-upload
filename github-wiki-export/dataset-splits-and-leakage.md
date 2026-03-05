# Wiki：データ分割とデータリーク

> 高い精度でも、分け方が甘いと評価は壊れます
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Practical guide

## このページの役割
このページは、データセットをどう分けるか、なぜデータリークが危険かを初歩から説明する wiki です。『精度が高いのに信用できない』という事故を減らすために、最小限どこを見ればよいかを整理します。

## 正確さの前提
ここで示すのは基本原則です。最適な分割方法は課題やデータの構造に依存するため、万能の 1 ルールではありません。

## 公開ページへ戻る
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [ハンズオン](https://mind-upload.com/hands_on.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: EEG前処理とQC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 前処理そのものがどこで結果を変えるかを補います。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜリーク対策が『運用の一部』なのかを確認できます。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 学習用ページの全体マップへ戻れます。

## いま分かっていること
- train/test の分け方が甘いと、精度は簡単に過大評価されます。
- 同じ被験者、同じセッション、近い時刻の断片が両側に入ると、見かけ上の性能が上がりやすいです。
- 前処理、正規化、特徴選択も、全データを見てから行うとリーク源になりえます。

## まだ分かっていないこと
- どの分割が最も将来の実運用に近いかは、課題設定と利用場面に依存します。
- リークを完全にゼロにしたと言い切るには、データ構造の深い理解と監査が必要です。

---

<h2>いちばん短い説明</h2>
<p>
データ分割は「答え合わせの前に、どこまで見てよいかを先に決める」作業です。データリークは、その境界をうっかり越えてしまい、<strong>本番では使えない情報を学習や調整に混ぜてしまうこと</strong>です。
</p>

<h2>なぜ分割がそんなに大事なのか</h2>
<p>
学校のテストで、答えを見ながら練習した問題をそのまま本番に出せば、点数は高くなります。ですが、その点数は「本当に新しい問題を解ける力」とは言えません。機械学習でも同じで、<strong>学習時に見た情報が test 側へにじむ</strong>と、数字だけ良く見えてしまいます。
</p>

<h2>まず分ける単位を意識する</h2>
<table>
<thead>
<tr>
<th>分ける単位</th>
<th>どういう場面か</th>
<th>注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>被験者単位</strong></td>
<td>新しい人に一般化できるかを見たいとき。</td>
<td>同じ人の断片が train と test に両方入ると、見かけより簡単になります。</td>
</tr>
<tr>
<td><strong>セッション単位</strong></td>
<td>同じ人でも別日に安定するかを見たいとき。</td>
<td>同日記録だけで分けると、日差や電極状態の違いを見落とします。</td>
</tr>
<tr>
<td><strong>時間単位</strong></td>
<td>未来予測や連続運用を想定するとき。</td>
<td>近い時刻の窓が両側に入ると、ほぼ同じ断片を見てしまうことがあります。</td>
</tr>
</tbody>
</table>

<h2>ありがちなリーク 5 パターン</h2>
<table>
<thead>
<tr>
<th>ありがちな事故</th>
<th>何が起きているか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同じ被験者の断片が両側に入る</strong></td>
<td>個人固有の癖を覚えてしまい、新しい人への一般化性能より高く見えます。</td>
</tr>
<tr>
<td><strong>近接した時間窓を混ぜる</strong></td>
<td>ほぼ同じ波形の切れ端を train/test に分けてしまい、未来予測の難しさを過小評価します。</td>
</tr>
<tr>
<td><strong>全データで正規化や特徴選択をする</strong></td>
<td>test 側の統計量を学習時に使ってしまい、情報が逆流します。</td>
</tr>
<tr>
<td><strong>モデル選択を test で繰り返す</strong></td>
<td>test が実質的に validation の役割を持ち、最後の点数が楽観的になります。</td>
</tr>
<tr>
<td><strong>重複サンプルや派生サンプルを見逃す</strong></td>
<td>元は同じ記録から切ったデータが両側に入り、独立試料でない比較になります。</td>
</tr>
</tbody>
</table>

<h2>最低限これだけは報告したい</h2>

<h4>Report Items</h4>
<ul>
<li><strong>分割単位：</strong>被験者、セッション、時間のどれで分けたか。</li>
<li><strong>分割規則：</strong>何件を train/validation/test に置いたか。</li>
<li><strong>前処理の境界：</strong>正規化や特徴選択を、train のみで fit したか。</li>
<li><strong>ベースライン：</strong>単純な手法と比べてどこが改善したか。</li>
<li><strong>失敗例：</strong>どの条件で崩れたか、除外理由は何か。</li>
</ul>

<h2>最初の 1 本で迷ったときの安全策</h2>
<p>
迷ったら、<strong>被験者単位で train/test を分ける</strong>、<strong>test は最後まで触らない</strong>、<strong>正規化や特徴選択は train だけで fit する</strong>、この 3 点を守るのが安全です。厳しすぎるように見えても、信用できる精度の方が、派手な数字より価値があります。
</p>

<h2>次にどこへ戻るか</h2>
<p>
実際のスターターデータを見直したい場合は <a href="https://mind-upload.com/datasets.html">データ&ベンチ</a>、最小ループを作る作業へ戻りたい場合は <a href="https://mind-upload.com/hands_on.html">ハンズオン</a>、なぜこれが検証基盤の一部なのかを確認したい場合は <a href="https://mind-upload.com/verification.html">検証基盤</a> へ戻ってください。
</p>
