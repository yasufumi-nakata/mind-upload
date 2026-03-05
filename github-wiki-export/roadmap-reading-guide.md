# Wiki：ロードマップの読み方

> 技術ロードマップを『長い一覧』ではなく『依存関係の地図』として読む
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Reading guide

## このページの役割
このページは、技術ロードマップの P/M/R/I/V/D が何を意味し、どこから読むと迷いにくいかを説明する補助ページです。ロードマップ本文を要約し直すのではなく、『地図の読み方』そのものを整理します。

## 正確さの前提
このページは読み方の補助です。正式な論点一覧や現時点の整理は、必ず技術ロードマップ本文へ戻って確認してください。

## 公開ページへ戻る
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - この地図が何のために要るのか、全体像から見たい人向けです。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - V 系列で何を固定したいのかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- P は前進の定義、M は計測、R は再構成、I は実装、V は検証、D は社会実装という役割分担です。
- 強い主張ほど後ろにあり、前の層の未整理を飛ばして進めません。
- ロードマップは結論集ではなく依存関係の地図として読むのが適切です。

## まだ分かっていないこと
- どの経路が最短で有効かは、今後のデータ・ベンチ整備で変わり得ます。
- V と D の最終条件は、まだ未解決問題を多く含みます。

---

<h2>まず一言でいうと</h2>
<p>
技術ロードマップは「何を先に解かないと、その先の話が崩れるか」を並べた地図です。長い一覧に見えても、実際には「前提 → 計測 → 推定 → 実装 → 検証 → 社会実装」という依存関係を表しています。
</p>

<strong>読み方の次に、次ページも決めたいとき</strong>
<p>
ロードマップの記号の意味だけでなく、読んだあとに計測、再構成、実装、検証、社会実装のどこへ進むかを 1 枚で見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-next-routes">ロードマップのあとに進む5つの道</a> をご覧ください。
</p>

<h2>P/M/R/I/V/D を日常語にする</h2>
<table>
<thead>
<tr>
<th>記号</th>
<th>何の問いか</th>
<th>これが抜けると何が困るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>何を成功と呼ぶか</td>
<td>目標が定まらず、後から都合よく勝利条件を変えられてしまいます。</td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>何をどの精度で測れるか</td>
<td>そもそも入力に何が入っているか分かりません。</td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>観測から何を推定できるか</td>
<td>測れた信号を、必要以上に強い意味へ読み替えてしまいます。</td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>そのモデルをどう動かすか</td>
<td>紙の上ではよく見えても、実際には回らない可能性があります。</td>
</tr>
<tr>
<td><strong>V</strong></td>
<td>何をどう確かめるか</td>
<td>前進したのか、見かけだけなのかを区別できません。</td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>社会でどう扱うか</td>
<td>技術が動いても、権利や安全の面で運用できません。</td>
</tr>
</tbody>
</table>

<h2>興味別の読み順</h2>
<table>
<thead>
<tr>
<th>いま気になること</th>
<th>まず読む記号</th>
<th>次に追う記号</th>
</tr>
</thead>
<tbody>
<tr>
<td>何を達成したら前進か知りたい</td>
<td><strong>P</strong></td>
<td><strong>V</strong></td>
</tr>
<tr>
<td>EEG や fMRI の限界から入りたい</td>
<td><strong>M</strong></td>
<td><strong>R</strong></td>
</tr>
<tr>
<td>モデルがどう動くか知りたい</td>
<td><strong>R</strong></td>
<td><strong>I</strong></td>
</tr>
<tr>
<td>本人性や社会制度まで見たい</td>
<td><strong>V</strong></td>
<td><strong>D</strong></td>
</tr>
</tbody>
</table>

<h2>これは年表ではなく依存関係です</h2>
<p>
P → M → R → I → V → D と並んでいても、「必ずこの年にここまで行く」という意味ではありません。大事なのは、後ろの主張ほど前の層の失敗に弱いということです。たとえば、M と R が曖昧なまま V で強い本人性主張へ進むと、入力の限界や推定の不確実性がそのまま残ります。
</p>

<h4>Next</h4>
<p>正式な論点一覧と索引は、技術ロードマップ本文で確認してください。</p>
<a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップへ →</a>
