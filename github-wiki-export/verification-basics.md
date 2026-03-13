# Wiki：検証基盤の基本

> 派手な主張より先に、物差しと記録の置き場を作る
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Beginner guide

## このページの役割
このページは、Mind-Upload がなぜ『標準・ベンチ・登録・監査』を中心に据えているのかを初歩から説明する wiki です。技術の中身だけでなく、比較可能な前進を作るための運用面を学ぶことが目的です。

## 正確さの前提
ここで使うたとえは理解の補助です。たとえで分かった気にならず、実際の設計は公開ページの仕様へ戻って確認してください。

## 公開ページへ戻る
- [検証基盤](https://mind-upload.com/verification.html)
- [ケースワーク](https://mind-upload.com/verification.html#casework)
- [データ&ベンチ](https://mind-upload.com/datasets.html)

## 関連 Wiki
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - この基盤が、なぜ主張の読み分けに必要かを説明します。
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - 全体像から戻って読みたい人向けです。
- [Wiki: ベースライン・事前登録・モデルカード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - 運用語の役割差を、初歩から整理します。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- 比較可能な前進には、入力、評価、ルール、記録の4つが必要です。
- 事前登録や監査がないと、あとから都合よく成功条件を変えられてしまいます。
- PDB や BIDS など、他分野でも公共財の整備が進歩を加速してきました。

## まだ分かっていないこと
- WBE 専用の最終ベンチマークが、まだ完成した形で存在するわけではありません。
- どの追加要件が L4 や L5 に十分かは、まだ研究と社会議論の途中です。

---

<h2>なぜ「物差し」が先なのか</h2>
<p>
もし学校のテストで、答案用紙も採点基準も違うまま「こっちの方が賢い」と比べたら、結果は信用しにくくなります。WBE でも同じで、データ、評価、失敗条件、記録の置き場がそろわないと、「前進した」と言っても比べられません。
</p>

<h2>4つの部品を学校のテストでたとえる</h2>
<table>
<thead>
<tr>
<th>部品</th>
<th>役割</th>
<th>たとえ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>標準（Data Standard）</strong></td>
<td>入力の形をそろえる</td>
<td>同じ答案用紙です。</td>
</tr>
<tr>
<td><strong>ベンチマーク（Benchmark）</strong></td>
<td>比べる課題と指標をそろえる</td>
<td>同じ採点基準です。</td>
</tr>
<tr>
<td><strong>事前登録（Registry / Prereg）</strong></td>
<td>やる前にルールを固定する</td>
<td>試験前に配られる実施要項です。</td>
</tr>
<tr>
<td><strong>監査（Audit / Model Card）</strong></td>
<td>失敗例や弱点まで残す</td>
<td>点数だけでなく、ミスや再試験条件も載った成績表です。</td>
</tr>
</tbody>
</table>

<h2>どれか1つ欠けると何が起こるか</h2>
<table>
<thead>
<tr>
<th>欠けるもの</th>
<th>起こる問題</th>
</tr>
</thead>
<tbody>
<tr>
<td>標準</td>
<td>同じ入力を見ているのか分からなくなります。</td>
</tr>
<tr>
<td>ベンチマーク</td>
<td>誰もが別の物差しで勝ったと言えてしまいます。</td>
</tr>
<tr>
<td>事前登録</td>
<td>あとから都合のよい条件だけを選んで成功扱いしやすくなります。</td>
</tr>
<tr>
<td>監査</td>
<td>点数だけが独り歩きし、弱点やリークが見えなくなります。</td>
</tr>
</tbody>
</table>

<h2>なぜ WBE では特に重要なのか</h2>
<p>
WBE は、話が大きい分だけ、レベルのすり替えが起きやすい分野です。L1 の結果を L4 のように語る、相関を因果のように見せる、部分的な成功を全体の成立のように扱う、といった事故が起きやすくなります。だからこそ、結果だけでなく<strong>どう評価したか</strong>を固定する必要があります。
</p>

<h2>このサイトでの使われ方</h2>
<p>
Mind-Upload では、Verification ページが設計図、Hands-on が最小実装、Datasets が入口データ、Casework が他分野の先例です。wiki は、その前提知識を補うためにあります。
</p>
<p>ベースライン、事前登録、モデルカード、失敗例の役割差をもう一段ていねいに整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards">Wiki: ベースライン・事前登録・モデルカード</a> が補講になります。</p>

<h4>Next</h4>
<p>この基礎を読んだあとで、実際の設計図を見たい場合はこちらです。</p>
<a href="https://mind-upload.com/verification.html">検証基盤ページへ →</a>
