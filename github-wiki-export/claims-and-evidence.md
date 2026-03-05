# Wiki：主張と証拠の読み方

> 派手な文言を、そのまま強い結論にしないために
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Reading guide

## このページの役割
このページは、脳科学や Mind-Upload の話で出てくる強い言い方を、必要な証拠の強さへ引き戻して読むためのガイドです。『すごそう』と『何が証明されたか』を分ける練習をします。

## 正確さの前提
ここでの整理は、主張を弱めるためではなく、過大評価と過小評価の両方を防ぐためのものです。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [FAQ](https://mind-upload.com/faq.html)

## 関連 Wiki
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - この読み方の前提になる全体像です。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜ証拠の置き方そのものが大事かを説明します。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- 再現可能な解析と本人性の主張は、必要な証拠の強さが大きく異なります。
- 出力が当たることと、内部の仕組みが正しいことは別です。
- 反証条件や再現手順がない強い主張は、いったん保留で読むのが安全です。

## まだ分かっていないこと
- どの段階で L4 の本人性主張へ進めるかは、まだ定まっていません。
- 理論ごとの違いを、1つの評価軸で完全に統合できる段階にはありません。

---

<div class="abstract-box">
<h2>基本ルール</h2>
<p>
研究発表の文言は、しばしば実際の証拠より強く見えます。そこで、まずは「この成果は何をしたのか」を L0〜L5 のどこに置くかを考えます。レベルが上がるほど、必要な証拠も増えます。
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">L0〜L5 を日常語で言い換える</h2>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>ざっくり言うと</th>
<th>最低限ほしい証拠</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>同じ結果をもう一度出せる</td>
<td>データ、コード、環境、ログが揃い、第三者が再現できること。</td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>信号から何かを当てられる</td>
<td>ベースライン比較、リーク検査、条件をそろえた再現精度。</td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>条件を変えても予測できる</td>
<td>未学習条件、反事実、介入に対する予測一致。</td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>閉ループで安定に動く</td>
<td>リアルタイム運用、遅延管理、安全停止条件。</td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>本人性を論じる</td>
<td>事前登録した連続性テスト、記憶・価値観・学習の分岐検証。</td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>社会で運用できる</td>
<td>権利、同意、停止基準、監査体制を含む制度設計。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="phrases">
<h2 class="section-title">よくある文言を翻訳する</h2>
<table class="data-table">
<thead>
<tr>
<th>見出しの言い方</th>
<th>実際には何を言っている可能性が高いか</th>
<th>追加で確認したいこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>「脳から文章を復元した」</td>
<td>多くは L1 のデコーディングです。</td>
<td>未学習条件でも成り立つか、LLM 補完との切り分けがあるかを見ます。</td>
</tr>
<tr>
<td>「脳状態を高精度に再現した」</td>
<td>L1、良くて L2 の入り口かもしれません。</td>
<td>条件変更や介入に対する予測まで見ているかを確認します。</td>
</tr>
<tr>
<td>「人間そっくりに振る舞った」</td>
<td>行動の見た目が似たという話にとどまる可能性があります。</td>
<td>内部状態、記憶連続性、失敗条件の公開があるかを見ます。</td>
</tr>
<tr>
<td>「これで本人を保存できる」</td>
<td>L4 の非常に強い主張です。</td>
<td>事前登録した本人性テストがあるか、代替説明を潰しているかが必要です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="checklist">
<h2 class="section-title">読むときの3点チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>これは L0〜L5 のどこか：</strong>まず主張の強さを置きます。</li>
<li><strong>何を測ったのか：</strong>出力一致だけか、条件変更や介入まで含むかを見ます。</li>
<li><strong>何が出たら失敗なのか：</strong>反証条件と再現手順があるかを確認します。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">一段上の主張へ進むには何が足りないか</h2>
<p>
L1 の結果があっても、すぐ L4 の話へは飛べません。普通は、まず L0 の再現性を固め、次に L2 の条件変更テストを入れ、それでもなお残る論点を分けて進めます。つまり、<strong>上のレベルは下のレベルを飛び越えて成立しません</strong>。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>この読み方を支える「標準・ベンチ・登録・監査」の考え方はこちらです。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics">検証基盤の基本へ →</a>
</div>
</section>
