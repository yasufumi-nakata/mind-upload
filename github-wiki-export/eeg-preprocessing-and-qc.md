# Wiki：EEG前処理とQC

> 結果が変わるのは、信号が繊細だからです
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Practical guide

## このページの役割
このページは、EEG の前処理と QC がなぜ結果に大きく効くのかを初歩から説明する wiki です。難しいアルゴリズム一覧より先に、『どこで結果が変わりやすいか』『何をログに残すべきか』を理解することを目標にします。

## 正確さの前提
ここで挙げるのは典型的な論点です。最適な処理は課題やデータに依存するため、万能の1手順を示すページではありません。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [ハンズオン](https://mind-upload.com/hands_on.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)

## 関連 Wiki
- [Wiki: EEGの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - 信号そのものの性質から戻りたいときはこちらです。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜ QC が再現性に直結するかを、運用の側から補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- EEG はノイズの影響を受けやすく、前処理の違いで結果が変わりやすいです。
- 参照法、フィルタ、アーティファクト除去、除外基準は最低限残すべき情報です。
- QC ログがない結果は、見た目がよくても追試しにくくなります。

## まだ分かっていないこと
- どの処理がどの課題で最も良いかは、データと目的に依存します。
- EEG だけでどこまで因果構造の推定に迫れるかは、前処理だけでは解決しません。

---

<h2>前処理で何が起きるのか</h2>
<p>
EEG は、脳の信号だけでなく、まばたき、筋電、体動、電源ノイズ、電極接触の問題なども一緒に入ってきます。だから、前処理は「見栄えを整える作業」ではなく、<strong>何を信号として扱うかを決める作業</strong>です。
</p>

<h2>まず意識したい4点</h2>
<table>
<thead>
<tr>
<th>論点</th>
<th>何が変わるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>参照法</strong></td>
<td>どの基準と比べるかで、見える波形の形が変わります。</td>
</tr>
<tr>
<td><strong>フィルタ</strong></td>
<td>残す周波数帯を変えると、強調される情報と消える情報が変わります。</td>
</tr>
<tr>
<td><strong>アーティファクト処理</strong></td>
<td>眼球や筋電をどこまで除くかで、残る信号の解釈が変わります。</td>
</tr>
<tr>
<td><strong>除外基準</strong></td>
<td>どのデータを外したかで、最終結果の分布や難しさが変わります。</td>
</tr>
</tbody>
</table>

<h2>なぜログを残すのか</h2>
<p>
同じデータでも、前処理が違えば結果が変わることがあります。そのため、「この条件で、この結果になった」という再現可能な記録が必要です。最低限、参照法、フィルタ設定、アーティファクト処理、除外基準、失敗例は残すべきです。
</p>

<h4>最低限残したい項目</h4>
<ul>
<li><strong>参照法：</strong>平均参照か、特定電極参照か。</li>
<li><strong>フィルタ：</strong>高域・低域・ノッチの設定。</li>
<li><strong>アーティファクト処理：</strong>ICA などを使ったか、どの成分を除いたか。</li>
<li><strong>除外基準：</strong>どの閾値で、どのチャンネルや区間を外したか。</li>
</ul>

<h2>やりがちな誤解</h2>
<table>
<thead>
<tr>
<th>誤解</th>
<th>実際には</th>
</tr>
</thead>
<tbody>
<tr>
<td>きれいな図が出たから十分</td>
<td>見た目がきれいでも、どう処理したかが残っていなければ再現性は弱いです。</td>
</tr>
<tr>
<td>1つの前処理が常に最適</td>
<td>課題やデータの性質で、よい設定は変わります。</td>
</tr>
<tr>
<td>QC は最後に見るもの</td>
<td>QC は最初から最後まで、入力の信頼性を支える作業です。</td>
</tr>
</tbody>
</table>

<h2>次にどこへ戻るか</h2>
<p>
EEG の信号そのものをもう一度確認したい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics">EEGの基本</a>、実際の作業手順へ戻りたい場合は <a href="https://mind-upload.com/hands_on.html">Hands-on</a>、公開データ選びへ戻りたい場合は <a href="https://mind-upload.com/datasets.html">Datasets</a> が自然です。
</p>
