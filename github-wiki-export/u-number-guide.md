# Wiki：U番号ガイド

> U は『未解決問題の名前札』です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-15 / 位置づけ: Reading guide

## このページの役割
このページは、文献地図で出てくる U番号を日常語で読み替えるための補助ページです。番号を暗記することが目的ではなく、『自分はどの塊から読めばよいか』を見つけやすくすることを目標にします。

## 正確さの前提
ここでの説明は入口用の言い換えです。厳密な定義や最新の状態は、必ず文献地図本文へ戻って確認してください。

## 公開ページへ戻る
- [文献地図](https://mind-upload.com/research_harvest_50.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: 文献と証拠ページの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - 文献地図そのものの役割を先に押さえたい人向けです。
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - U番号の背後にある全体像を先に見たい人向けです。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- U は、文献地図の中で未解決問題を整理するための内部コードです。
- 大きな問題群で見れば、どこから読むべきかはかなり分かりやすくなります。
- 引用数や番号の大きさは、主張の強さや重要度そのものではありません。
- 技術・自然科学の読者は、U0/U12/U15 を既定入口に置かない方が読み違えを減らせます。

## まだ分かっていないこと
- 各 U の内容や境界は、今後の文献整理で更新される可能性があります。
- どの U に最も研究資源を集中すべきかは、まだ固定していません。
- U11 の意識指標比較を主導線へ戻すかどうかは、今後の prediction competition と benchmark 整備で変わり得ます。

---

<h2>まず覚えなくてよいこと</h2>
<p>
U番号は試験の暗記項目ではありません。役割は「この文献は、どの未解決問題に関係するか」を揃えるための名前札です。まずは番号そのものより、どの塊の問題かを見る方が大事です。
</p>

<h2>大きな問題群で見る</h2>
<table>
<thead>
<tr>
<th>大きな問題群</th>
<th>主な U</th>
<th>日常語でいうと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>定義と評価</strong></td>
<td>U0 / U11 / U13 / U14</td>
<td>何を「同じ」「成功」「追試できる」と呼ぶかの問題です。</td>
</tr>
<tr>
<td><strong>計測と推定</strong></td>
<td>U1 / U7</td>
<td>脳や行動をどこまで測れ、どこまで推定できるかの問題です。</td>
</tr>
<tr>
<td><strong>因果と実装安定性</strong></td>
<td>U4 / U8 / U10</td>
<td>条件変更への反応、閉ループの安定、物理的コストの問題です。</td>
</tr>
<tr>
<td><strong>境界と本人性</strong></td>
<td>U3 / U12</td>
<td>どこまでを主体に含めるか、分岐後の本人性をどう扱うかの問題です。</td>
</tr>
<tr>
<td><strong>制度と公開運用</strong></td>
<td>U15</td>
<td>停止基準、公開基準、責任の置き方まで含めた運用の問題です。</td>
</tr>
</tbody>
</table>

<h2>関心別の入口</h2>
<table>
<thead>
<tr>
<th>いま気になること</th>
<th>まず見る U 群</th>
</tr>
</thead>
<tbody>
<tr>
<td>EEG や逆問題、時刻同期の限界</td>
<td>U1 / U7</td>
</tr>
<tr>
<td>decode 成功と WBE 主張の違い</td>
<td>U4 / U13</td>
</tr>
<tr>
<td>長期 closed-loop の安定性</td>
<td>U8</td>
</tr>
<tr>
<td>connectome 外の maintenance-state</td>
<td>U3</td>
</tr>
<tr>
<td>物理コストや散逸まで含めたい</td>
<td>U10</td>
</tr>
</tbody>
</table>

<h2>技術・自然科学で先に見る順</h2>
<table>
<thead>
<tr>
<th>順番</th>
<th>U 群</th>
<th>この順で見る理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td><strong>U1 / U7</strong></td>
<td>まず、何が直接観測され、何がまだ推定かを固定しないと、その後の主張レベルが全部ぶれます。</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td><strong>U4 / U13</strong></td>
<td>decode や模倣の成功を、因果保存や emulation と読み違えないためです。</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><strong>U8</strong></td>
<td>within-session の成功が、長期運用の安定とは限らないためです。</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><strong>U3</strong></td>
<td>connectome と cell type の外に残る maintenance-state を確認しないと、長期主張を読みすぎるためです。</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><strong>U10</strong></td>
<td>最後に、散逸と実効コストを反証条件として戻し、計算可能性だけで話を終えないためです。</td>
</tr>
</tbody>
</table>

<strong>主導線から外す群</strong>
<p>
<strong>U0 / U12 / U15</strong> は重要ですが、技術・自然科学の既定入口には置きません。ここで先に必要なのは、本人性や制度論よりも、<strong>何が測れて、どこまで直接妥当化できて、どこで閉ループが壊れ、どの hidden state が残るか</strong>を固定することだからです。
</p>

<h2>U番号で読み違えないために</h2>

<h4>Checklist</h4>
<ul>
<li><strong>番号を暗記しない：</strong> まず問題群から入ります。</li>
<li><strong>引用数で判断しない：</strong> 多いことと、解決済みであることは別です。</li>
<li><strong>厳密定義へ戻る：</strong> 本当に使うときは文献地図本文の定義表へ戻ります。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
番号の意味がつかめたら <a href="https://mind-upload.com/research_harvest_50.html">文献地図</a> に戻ってください。もし文献ページ全体の役割差がまだ曖昧なら、先に <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading">文献と証拠ページの読み方</a> を見るとさらに読みやすくなります。
</p>
