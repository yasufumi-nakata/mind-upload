# Wiki：Decode と Emulate

> 似ている出力と、同じ仕組みで動いていることは別です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Concept guide

## このページの役割
このページは、Mind-Upload で重要な区別である decode と emulate の違いを、初歩から整理する補助ページです。どちらが上かを決めるのではなく、何を主張しているのかが違うことを分けて読むために使います。

## 正確さの前提
ここでの説明は入口用です。実際の評価条件やベンチマーク設計は、対応する公開ページへ戻って確認してください。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [FAQ](https://mind-upload.com/faq.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - L0〜L5 の強さと必要な証拠へ戻せます。
- [Wiki: EEGの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - decode の入口になる EEG の性質を補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- decode は L1 の主張、emulate は少なくとも L2 以降の主張に近いです。
- 相関的に当てることと、介入に応答できることは別の能力です。
- この区別を入れるだけで、派手なニュースを読み違えにくくなります。

## まだ分かっていないこと
- どの時点で '十分に emulate した' と言えるかの閾値は未確定です。
- 内部因果構造の保存を、どの指標で十分とみなすかは今後の課題です。

---

<div class="abstract-box">
<h2>まず一言でいうと</h2>
<p>
decode は「観測された信号から何かを当てること」、emulate は「中の仕組みが動き、条件変更にも反応すること」です。見た目の出力が似ていても、その中身が同じように動いているとは限りません。
</p>
</div>

<section class="section" id="simple-table">
<h2 class="section-title">いちばん短い違い</h2>
<table class="data-table">
<thead>
<tr>
<th>項目</th>
<th>Decode</th>
<th>Emulate</th>
</tr>
</thead>
<tbody>
<tr>
<td>何をするか</td>
<td>観測から状態や内容を推定する。</td>
<td>内部状態が時間発展し、将来の出力を生む。</td>
</tr>
<tr>
<td>何が強いか</td>
<td>観測された条件での予測。</td>
<td>条件変更や介入への応答。</td>
</tr>
<tr>
<td>足りないと何が起きるか</td>
<td>相関だけで強い主張をしやすい。</td>
<td>内部因果構造が本当に近いか分かりにくい。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="daily-example">
<h2 class="section-title">日常例で考える</h2>
<p>
たとえば、ある人の答案を見て「この人は次にこう答えそうだ」と当てるのは decode に近いです。一方、その人の考え方や迷い方まで再現し、質問の条件を変えても同じように反応する仕組みを作るのは emulate に近いです。
</p>
</section>

<section class="section" id="evidence">
<h2 class="section-title">必要な証拠も違う</h2>
<table class="data-table">
<thead>
<tr>
<th>見たいこと</th>
<th>最低限ほしい証拠</th>
</tr>
</thead>
<tbody>
<tr>
<td>decode を主張したい</td>
<td>ベースライン比較、リーク検査、再現可能な予測精度。</td>
</tr>
<tr>
<td>emulate に近づいたと言いたい</td>
<td>未学習条件、反事実、介入への応答、閉ループでの安定性。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-matters">
<h2 class="section-title">なぜこの区別が重要か</h2>
<p>
この区別がないと、「脳信号から文章を出せた」だけで、WBE に必要な内部の生成や因果構造まで達成したように読んでしまいます。Mind-Upload では、ここを飛ばさないためにクレーム階段と検証基盤を先に置いています。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>主張レベルと必要な証拠の強さを合わせて見たい場合はこちらです。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence">主張と証拠の読み方へ →</a>
</div>
</section>
