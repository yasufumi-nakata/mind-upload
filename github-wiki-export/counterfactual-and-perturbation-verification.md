# Wiki：反事実・介入・摂動の検証

> 当たることと、条件を変えても正しく反応することは別です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
このページは、held-out 精度が高いこと、介入に正しく反応すること、反事実の分岐を再現できること、摂動に対する応答構造が一致することを、初歩から切り分ける wiki です。『精度が高い = 中身も同じ』という誤解を避けることを目的にします。

## 正確さの前提
ここで扱うのは検証の考え方です。個別の摂動プロトコルや数式は省きますが、因果検証が held-out 精度より厳しいという点は崩しません。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [FAQ](https://mind-upload.com/faq.html)

## 関連 Wiki
- [Wiki: Decode と Emulate](https://github.com/yasufumi-nakata/mind-upload/wiki/decode-vs-emulate) - まず翻訳と生成の違いへ戻りたい人向けです。
- [Wiki: 観測から推定へ](https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation) - 推定モデルと因果モデルの違いを補います。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Benchmark、Registry、Model Card の役割を補います。

## いま分かっていること
- 学習していないデータで当たることは重要ですが、それだけで因果構造の一致は言えません。
- 条件をわざと変えたときの反応を見る検証は、出力一致より強いテストです。
- 反事実や摂動の検証には、失敗条件とログの固定が必要です。

## まだ分かっていないこと
- どの摂動セットが WBE の本人性主張へ最も効くかは未解決です。
- 反事実等価性をどこまで満たせば十分かは、理論と工学の両面で研究途中です。

---

<h2>いちばん短い違い</h2>
<p>
held-out 精度は「見たことのない問題でも当たるか」を見るテストです。介入や反事実の検証は、「条件を変えたとき、どの方向へどう崩れ、どう持ち直すかまで再現できるか」を見るテストです。
</p>

<h2>まず検証の強さを 4 段階で分ける</h2>
<table>
<thead>
<tr>
<th>段階</th>
<th>何を見ているか</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. held-out 精度</strong></td>
<td>見たことのないデータでも当たるか。</td>
<td>条件変更への反応や因果構造の一致はまだ言えません。</td>
</tr>
<tr>
<td><strong>2. OOD / 新規条件</strong></td>
<td>少し違う条件でも崩れにくいか。</td>
<td>介入したときに中の仕組みが同じように動くかまでは言えません。</td>
</tr>
<tr>
<td><strong>3. 介入</strong></td>
<td>刺激や入力条件をわざと変えたとき、応答が正しく変わるか。</td>
<td>「もし別の分岐だったら」という反事実全体まではまだ十分でない場合があります。</td>
</tr>
<tr>
<td><strong>4. 反事実・摂動構造</strong></td>
<td>分岐全体や応答伝播の構造が、生体と同じように動くか。</td>
<td>それでも本人性や社会実装まで即断はできません。</td>
</tr>
</tbody>
</table>

<h2>なぜ精度だけでは足りないのか</h2>
<p>
テスト問題で高得点でも、問題の癖を覚えただけかもしれません。同じように、モデルが高精度でも、それが<strong>本当に中の仕組みを捉えたのか</strong>、それとも表面のパターンを拾っただけかは、精度だけでは分かりません。
</p>

<strong>よくある事故</strong>
<p>
データリーク、分布の偏り、言語モデルの事前分布、評価条件の甘さがあると、見かけのスコアだけが上がります。だから Mind-Upload では、スコアの前に失敗条件と検証条件を固定します。
</p>

<h2>介入と反事実はどう違うのか</h2>
<table>
<thead>
<tr>
<th>用語</th>
<th>ひとことで言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>介入</strong></td>
<td>実際に条件を変えて、その結果を見ます。</td>
</tr>
<tr>
<td><strong>反事実</strong></td>
<td>「もし別の条件だったら」と、起きなかった分岐まで含めて考えます。</td>
</tr>
<tr>
<td><strong>摂動</strong></td>
<td>システムへ小さな変化や刺激を加えて、応答の広がり方を見ることです。</td>
</tr>
</tbody>
</table>
<p>
介入は実験で行いやすい入口で、反事実はより強い問いです。摂動は、その入口として「条件をわざと揺らして、応答構造を見る」具体的なやり方だと考えると分かりやすいです。
</p>

<h2>小さな例で考える</h2>
<table>
<thead>
<tr>
<th>テスト</th>
<th>何を確かめているか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>held-out EEG 分類</strong></td>
<td>未見データでも状態ラベルを当てられるか。</td>
</tr>
<tr>
<td><strong>新規刺激条件での予測</strong></td>
<td>学習していない条件でも、応答傾向が崩れないか。</td>
</tr>
<tr>
<td><strong>仮想摂動の応答比較</strong></td>
<td>条件を変えたときの伝播や回復の仕方が似ているか。</td>
</tr>
<tr>
<td><strong>反事実分岐の比較</strong></td>
<td>「もし刺激位置や条件が違ったら」という分岐構造まで追えるか。</td>
</tr>
</tbody>
</table>

<h2>なぜ Benchmark / Registry / Model Card が要るのか</h2>

<h4>役割分担</h4>
<ul>
<li><strong>Benchmark：</strong>どの介入や摂動を行い、何で採点するかを固定します。</li>
<li><strong>Registry：</strong>どの条件で失敗とみなすか、どこまでを事前に決めるかを固定します。</li>
<li><strong>Model Card：</strong>どの摂動で崩れたか、どの OOD 条件に弱いかを残します。</li>
</ul>

<p>
ここが曖昧だと、後から都合のよい摂動だけを選んで「中身も同じ」と言えてしまいます。
</p>

<h2>因果検証の話を読むときの最低チェック</h2>

<h4>Checklist</h4>
<ul>
<li><strong>ただの held-out 精度ではないか：</strong>条件変更が本当に入っているか。</li>
<li><strong>介入内容が明示されているか：</strong>何をどれだけ変えたかが書かれているか。</li>
<li><strong>失敗条件があるか：</strong>どんな結果なら不一致とみなすかが先に決まっているか。</li>
<li><strong>失敗例が残っているか：</strong>うまくいかなかった摂動も公開されているか。</li>
</ul>

<h2>次にどこへ戻るか</h2>
<p>
翻訳と生成の違いへ戻るなら <a href="https://mind-upload.com/wbe_101.html">WBE入門</a>、検証設計へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、短い Q&A へ戻るなら <a href="https://mind-upload.com/faq.html">FAQ</a> をご利用ください。
</p>
