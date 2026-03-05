# Wiki：『分かった』と『次に進める』の違い

> 理解の段階と、行動できる段階を分けて読む
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Understanding vs action

## このページの役割
このページは、Mind-Upload のページを読んだあとに『分かった』と感じる状態と、『実際に次へ進める』状態の違いを整理する補助ガイドです。要約を読んだだけ、原文まで読んだ、勝利条件や反証条件を確認した、修正位置や外部依存まで切り分けた、では行動の準備度が違います。その差を段階で見えるようにします。

## 正確さの前提
ここで扱うのは理解の段階です。個別の主張や修正案の妥当性は、必ず元ページと根拠へ戻って確認してください。

## 公開ページへ戻る
- [FAQ](https://mind-upload.com/faq.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [貢献ガイド](https://mind-upload.com/issue.html)

## 関連 Wiki
- [Wiki: 要約・原文・Issue履歴の使い分け](https://github.com/yasufumi-nakata/mind-upload/wiki/summary-vs-source-reading) - どこで元ソースへ戻るべきかを先に見たい人向けです。
- [Wiki: はじめての Issue の書き方](https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics) - 実際に行動へ落とす書き方を補います。
- [Wiki: このサイトの3つの使い方](https://github.com/yasufumi-nakata/mind-upload/wiki/site-usage-modes) - いま自分がどのモードにいるかを整理できます。

## いま分かっていること
- 要約を読んだだけでは、まだ修正や引用に十分でない場面が多いです。
- 次に進める状態には、根拠、条件、修正位置のいずれかの確認が必要です。
- 理解の段階を分けると、どこで止まっているかを落ち着いて判断できます。

## まだ分かっていないこと
- どの段階まで確認すれば十分かは、目的によって変わります。
- 外部依存の話では、理解が進んでも相手先条件で止まる場合があります。

---

<h2>理解には段階があります</h2>
<p>
「意味はなんとなく分かった」と、「次にどのページを直すか分かる」は同じではありません。このサイトでは、読む、原文へ戻る、条件を確認する、修正位置を特定する、外部依存を分ける、という段階を分けて考えます。
</p>

<h2>4つの段階</h2>
<table>
<thead>
<tr>
<th>段階</th>
<th>いま言えること</th>
<th>まだ足りないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 要約が分かった</strong></td>
<td>そのページが何の話かは分かります。</td>
<td>根拠として使うには、原文や条件がまだ足りません。</td>
</tr>
<tr>
<td><strong>2. 元ソースを確認した</strong></td>
<td>論文、原文節、Issue 履歴のどこに何が書かれているかを確認できます。</td>
<td>今度は、何を前進条件と反証条件にするかが必要です。</td>
</tr>
<tr>
<td><strong>3. 条件が分かった</strong></td>
<td>何が足りず、何が満たされれば前進かを言えます。</td>
<td>実際にどこを直すか、どこへ戻すかの特定が必要です。</td>
</tr>
<tr>
<td><strong>4. 次に進める</strong></td>
<td>修正位置、戻る先、外部依存の切り分けまで分かります。</td>
<td>あとは実際に変更や記録を行う段階です。</td>
</tr>
</tbody>
</table>

<h2>ページごとに足りないものが違います</h2>
<table>
<thead>
<tr>
<th>ページ</th>
<th>「要約が分かった」の次に要ること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>FAQ</strong></td>
<td>対応する公開ページや wiki に戻って、条件や前提を確認します。</td>
</tr>
<tr>
<td><strong>Papers / Research Harvest</strong></td>
<td>DOI や元論文に戻って、方法、評価、限界を確認します。</td>
</tr>
<tr>
<td><strong>Proposals</strong></td>
<td>原文節と Issue 履歴に戻って、採否と議論の文脈を確認します。</td>
</tr>
<tr>
<td><strong>Issue</strong></td>
<td>対象ページ本文へ戻って、どこを直すかを具体化します。</td>
</tr>
<tr>
<td><strong>Collaborations</strong></td>
<td>今この場で作れる準備物と、外部依存を分けます。</td>
</tr>
</tbody>
</table>

<h2>自己診断</h2>
<table>
<thead>
<tr>
<th>自分に聞くこと</th>
<th>`はい` なら</th>
<th>`いいえ` なら</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>元ソースを確認したか</strong></td>
<td>次は条件や修正位置を確認します。</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/summary-vs-source-reading">要約・原文・Issue履歴の使い分け</a> へ戻ります。</td>
</tr>
<tr>
<td><strong>何が足りないかを 1 文で言えるか</strong></td>
<td>次はどこを直すかを決めます。</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> や <a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a> で条件を確認します。</td>
</tr>
<tr>
<td><strong>どのページのどこを直すか言えるか</strong></td>
<td>Issue や修正に進めます。</td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a> や <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/content-placement-basics">新しい情報の置き場所を決める基本</a> へ戻ります。</td>
</tr>
<tr>
<td><strong>外部依存かどうか分かるか</strong></td>
<td>Issue か Collaborations かを決めます。</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a> へ戻ります。</td>
</tr>
</tbody>
</table>

<h2>よくある止まり方</h2>

<h4>Mistake</h4>
<ul>
<li><strong>要約を読んで、そのまま引用する：</strong> 根拠に使うなら元ソース確認が必要です。</li>
<li><strong>条件が分からないまま Issue を書く：</strong> まず何が足りないかを 1 文で言える状態が必要です。</li>
<li><strong>修正位置が決まらないまま大きな提案にする：</strong> Content Hub や対象ページ本文へ戻る方が安全です。</li>
<li><strong>理解は進んだが外部依存を見落とす：</strong> 実行可能な変更と相手待ちを分ける必要があります。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
元ソース確認へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/summary-vs-source-reading">要約・原文・Issue履歴の使い分け</a>、実行へ落とすなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">はじめての Issue の書き方</a>、サイト全体の使い方へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/site-usage-modes">このサイトの3つの使い方</a> をご利用ください。
</p>
