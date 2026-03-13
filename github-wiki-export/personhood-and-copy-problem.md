# Wiki：本人性とコピー問題

> 見た目が同じでも、『同じ本人』かは別問題です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Beginner guide

## このページの役割
このページは、Mind-Upload の議論でよく出てくる『コピー問題』と『本人性』を初歩から整理する wiki です。哲学の固有名詞を覚えるより先に、なぜこの論点が技術の外に逃げないのかを理解することを目指します。

## 正確さの前提
このページは分かりやすく説明しますが、本人性の最終結論を出すページではありません。未解決のまま残る部分を明示します。

## 公開ページへ戻る
- [理論フレーム](https://mind-upload.com/perspective.html#design-principles)
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - 全体像からこの論点の位置づけを確認できます。
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - L4 の本人性主張がどれだけ強いかを補います。
- [Wiki: 本人性評価と連続性テスト](https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests) - 哲学の論点を、事前登録されたテスト設計へ戻して整理します。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- 見た目の振る舞いが似ていても、それだけで本人性は確定しません。
- コピーが複数ある状況では、『どれが本人か』が自動的には決まりません。
- だから Mind-Upload では、連続性をどう検証するかを別問題として扱います。

## まだ分かっていないこと
- どの条件なら『同じ本人』と見なしてよいかについて、合意はありません。
- 心理的連続性、因果連続性、現象的意識のどれを重視するかで結論が変わります。
- 連続的移行の設計が、本人性を十分に守るかどうかも未証明です。

---

<h2>まず最初の区別</h2>
<p>
誰かとまったく同じように話し、同じ記憶を語り、同じ反応をしたとしても、それだけで「同じ本人」とは限りません。Mind-Upload では、この差を曖昧にしないために、<strong>性能の一致</strong>と<strong>本人性の主張</strong>を別のレベルとして扱います。
</p>

<h2>なぜ難しいのか</h2>
<table>
<thead>
<tr>
<th>問い</th>
<th>なぜ難しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td>同じ記憶を語れたら本人か</td>
<td>記憶の再現と、体験の連続性は同じではないかもしれないからです。</td>
</tr>
<tr>
<td>コピーが1つなら本人か</td>
<td>もし2つ作れたら、どちらが本人かを同じ理屈で決めにくくなるからです。</td>
</tr>
<tr>
<td>少しずつ置き換えたら安全か</td>
<td>連続的移行は直感的に強そうですが、それが十分条件かはまだ分からないからです。</td>
</tr>
</tbody>
</table>

<h2>静的コピーと連続的移行の違い</h2>
<table>
<thead>
<tr>
<th>考え方</th>
<th>何を重視するか</th>
<th>残る疑問</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>静的コピー</strong></td>
<td>ある時点の構造や情報を複製すること。</td>
<td>コピーが複数あれば、どれが本人かが分からなくなります。</td>
</tr>
<tr>
<td><strong>連続的移行</strong></td>
<td>プロセスや相互作用を切らさずに引き継ぐこと。</td>
<td>連続であることが、本人性の十分条件かはまだ未証明です。</td>
</tr>
</tbody>
</table>

<h2>工学に戻すと、何をテストしたいのか</h2>
<p>
この論点を工学に戻すと、ただ「よく似ているか」を見るだけでは足りません。記憶、価値観、学習履歴、条件変更への反応が、どこまで連続しているかを事前登録したテストで見る必要があります。つまり、哲学の話をそのまま放置するのではなく、<strong>どんな失敗なら本人性主張を保留にするか</strong>を定義する方向へ進みます。
</p>
<p>テスト設計の入口だけ先に見たい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">Wiki: 本人性評価と連続性テスト</a> が補講になります。</p>

<h4>Next</h4>
<p>この論点を理論フレームとしてどう扱うかは、こちらで確認できます。</p>
<a href="https://mind-upload.com/perspective.html#design-principles">理論フレームへ →</a>
