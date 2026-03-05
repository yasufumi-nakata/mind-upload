# Wiki：『分かっていること / 分かっていないこと』の読み方

> 情報ポータルとして読むために、断言と保留の境界をそろえる
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Reading status and scope

## このページの役割
このページは、Mind-Upload の公開ページにある『いま分かっていること』『まだ分かっていないこと』『このページで言えること / 言えないこと』を、誤読しないための補助ガイドです。公開ページは情報ポータルとして、断言できる範囲と保留すべき範囲を先に示します。その意味をそろえて読むために使います。

## 正確さの前提
ここで扱うのは公開ページの読み方です。個別の理論や技術の真偽は、必ず元ページ本文と根拠へ戻って確認してください。

## 公開ページへ戻る
- [スタートページ](https://mind-upload.com)
- [検証基盤](https://mind-upload.com/verification.html)
- [公開コンテンツ統合ハブ](https://mind-upload.com/content_hub.html)

## 関連 Wiki
- [Wiki: 公開ページの読み分けガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - どの公開ページから読むかを先に決めたい人向けです。
- [Wiki: 部分解決・探索段階・未整備の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/progress-labels-and-open-problem-status) - 進捗ラベルの意味をさらに細かく見たい人向けです。
- [Wiki: 内製で先にやることと外部依存](https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies) - 外部依存と今できる変更の切り分けを詳しく見たい人向けです。

## いま分かっていること
- 公開ページは、断言の強さと保留の範囲を先に示す情報ポータルとして設計されています。
- 『いま分かっていること』は、そのページの範囲で比較的強く言えることを指します。
- 『まだ分かっていないこと』や『外部依存』を分けると、過剰な期待や誤読を減らせます。

## まだ分かっていないこと
- どの論点を今後どこまで『既知』へ移せるかは、研究と整備の進み方で変わります。
- L4 や L5 のような強い主張は、引き続き未解決部分を多く含みます。

---

<div class="abstract-box">
<h2>公開ページは「断言する場所」と「保留する場所」を分けています</h2>
<p>
このサイトの公開ページは、何でも断言するための場所ではありません。むしろ、<strong>いま比較的強く言えること</strong>、<strong>まだ言い切れないこと</strong>、<strong>このページの役割ではないこと</strong>を分けて、読む人が誤って強い結論に飛ばないようにしています。
</p>
</div>

<section class="section" id="four-boxes">
<h2 class="section-title">まず 4 つを分けて読む</h2>
<table class="data-table">
<thead>
<tr>
<th>表示</th>
<th>どう読むか</th>
<th>誤読しやすい点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>いま分かっていること</strong></td>
<td>そのページの範囲で、比較的強く言えることです。</td>
<td>「分野全体で最終決着した」と読むのは行き過ぎです。</td>
</tr>
<tr>
<td><strong>まだ分かっていないこと</strong></td>
<td>未解決、条件不足、証拠不足、合意不足などが残っている部分です。</td>
<td>「不可能だと証明された」と読むのは別の話です。</td>
</tr>
<tr>
<td><strong>正確さの前提</strong></td>
<td>このページが何を断言しないか、どこまでを守備範囲とするかを示します。</td>
<td>注意書きではなく、断言の境界線として読む必要があります。</td>
</tr>
<tr>
<td><strong>外部依存</strong></td>
<td>このリポジトリだけでは完了できない作業や条件です。</td>
<td>「今は何もできない」と読むのは誤りで、準備物は先に作れます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="known-does-not-mean-solved">
<h2 class="section-title">「分かっている」は「全部解けた」ではありません</h2>
<table class="data-table">
<thead>
<tr>
<th>公開ページの言い方</th>
<th>実際の意味</th>
</tr>
</thead>
<tbody>
<tr>
<td>標準、共有基盤、評価、監査が必要</td>
<td>必要条件の整理が比較的安定している、という意味です。実装完了を意味しません。</td>
</tr>
<tr>
<td>EEG で条件付きの前進は作れる</td>
<td>限定された範囲なら比較可能な進歩を作れる、という意味です。WBE 全体が証明された話ではありません。</td>
</tr>
<tr>
<td>本人性や意識は入口ページで断言しない</td>
<td>入口の役割ではない、という意味です。不必要という意味ではありません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="unknown-does-not-mean-impossible">
<h2 class="section-title">「分かっていない」は「不可能」ではありません</h2>
<table class="data-table">
<thead>
<tr>
<th>未知の種類</th>
<th>どういう不足か</th>
<th>次に見る場所</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>証拠不足</strong></td>
<td>必要なデータ、比較、反証条件が足りません。</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
</tr>
<tr>
<td><strong>条件未定</strong></td>
<td>何を満たせば前進か、何が出たら保留かが曖昧です。</td>
<td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a> / <a href="https://mind-upload.com/verification.html">Verification</a></td>
</tr>
<tr>
<td><strong>合意不足</strong></td>
<td>本人性や制度設計のように、分野横断の合意がまだありません。</td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a> / <a href="https://mind-upload.com/collaborations.html">Collaborations</a></td>
</tr>
<tr>
<td><strong>外部依存</strong></td>
<td>IRB、機材、契約、共同研究相手など、外部条件が必要です。</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read-page-top">
<h2 class="section-title">ページ冒頭をどう使うか</h2>
<table class="data-table">
<thead>
<tr>
<th>冒頭の要素</th>
<th>何に使うか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>page intro</strong></td>
<td>そのページの役割を確認します。理論本文なのか、実務なのか、運用ハブなのかを先に固定します。</td>
</tr>
<tr>
<td><strong>accuracy note</strong></td>
<td>そのページが意図的に断言しない範囲を確認します。</td>
</tr>
<tr>
<td><strong>known / unknown</strong></td>
<td>何が比較的安定した土台で、何が未解決として残るかを分けます。</td>
</tr>
<tr>
<td><strong>wiki links</strong></td>
<td>そこで止まりやすい前提を、学習用ページで補います。</td>
</tr>
<tr>
<td><strong>recommended pages</strong></td>
<td>そのページのあとに戻る公開ページを決めます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある誤読</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>「分かっている」を完了報告として読む：</strong> 多くは必要条件や比較的安定した前提の整理です。</li>
<li><strong>「分かっていない」を否定証明として読む：</strong> 未解決や証拠不足と、不可能証明は別です。</li>
<li><strong>accuracy note を飾りとして読む：</strong> 実際には断言の境界を決める重要な情報です。</li>
<li><strong>外部依存を保留箱として放置する：</strong> 先に内製できる準備物を切り出す必要があります。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
公開ページの役割差へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide">公開ページの読み分けガイド</a>、進捗ラベルの細かい意味へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/progress-labels-and-open-problem-status">部分解決・探索段階・未整備の読み方</a>、外部依存の切り分けへ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a> をご利用ください。
</p>
</section>
