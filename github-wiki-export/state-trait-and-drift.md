# Wiki：state・trait・ドリフト

> 『今日の状態』と『その人らしさ』は同じではありません
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
このページは、Mind-Upload の縦断評価で重要になる state（その場の状態）、trait（比較的安定な特徴）、drift（時間とともに起きる変化）を初歩から整理する wiki です。『今日の反応が似ている』ことと『長く同じ本人らしさが続いている』ことを混同しないための足場として使います。

## 正確さの前提
ここで示す区別は実務上の整理です。何を trait とみなすか、どの drift を許容するかは課題や理論で変わりうるため、最終基準を固定するページではありません。

## 公開ページへ戻る
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [研究ノート](https://mind-upload.com/perspective.html)

## 関連 Wiki
- [Wiki: 本人性評価と連続性テスト](https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests) - L4 の連続性テスト全体へ戻れます。
- [Wiki: 不確実性・信頼区間・棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 縦断変動の幅をどう読むかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページへ戻れます。

## いま分かっていること
- 同じ人でも、日内・日間で脳状態や反応は揺れます。
- 短期的に揺れる特徴と、比較的安定な特徴を分けて評価する必要があります。
- 学習や更新によるドリフトをログ付きで追わないと、長期評価は崩れます。

## まだ分かっていないこと
- どの特徴を trait とみなし、どこまでの drift を許容するかは未確定です。
- 長期の変化を許容しつつ本人性を保つ境界は、まだ研究途中です。

---

<div class="abstract-box">
<h2>いちばん短い区別</h2>
<p>
state は「今の状態」、trait は「比較的長く安定する特徴」、drift は「時間とともに変わっていくこと」です。本人性や長期評価では、この 3 つを同じ箱に入れないことが重要です。
</p>
</div>

<section class="section" id="three-terms">
<h2 class="section-title">まず 3 つを分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ざっくり意味</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>state</strong></td>
<td>その場その時の状態です。</td>
<td>眠い、集中している、緊張している、麻酔下にある、などです。</td>
</tr>
<tr>
<td><strong>trait</strong></td>
<td>比較的長く安定している特徴です。</td>
<td>選好傾向、反応パターンの一部、長期的な判断傾向などです。</td>
</tr>
<tr>
<td><strong>drift</strong></td>
<td>時間とともに起きる変化です。</td>
<td>学習、忘却、モデル更新、環境変化によるズレです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-separate">
<h2 class="section-title">なぜ分けないと危ないのか</h2>
<p>
もし今日たまたま似た反応が出ただけでも、それを「長期的に同じ本人らしさがある」と読んでしまうと、評価を盛りすぎます。逆に、学習による自然な変化まで全部 drift として不一致扱いすると、今度は変化を許容できません。
</p>
</section>

<section class="section" id="longitudinal">
<h2 class="section-title">縦断評価で見たいこと</h2>
<table class="data-table">
<thead>
<tr>
<th>見たいこと</th>
<th>何を確認するか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>短期 state の揺れ</strong></td>
<td>日内やセッション間で、反応がどれくらい変わるか。</td>
</tr>
<tr>
<td><strong>trait の安定性</strong></td>
<td>短期変動の上に乗っても、比較的保たれる特徴があるか。</td>
</tr>
<tr>
<td><strong>drift の方向</strong></td>
<td>学習や更新で、どの方向へ、どの速さで変わるか。</td>
</tr>
<tr>
<td><strong>許容範囲</strong></td>
<td>どれくらいの変化までを「同一性の範囲内」とみなすか。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="identity">
<h2 class="section-title">本人性の話ではどう使うか</h2>
<p>
本人性の評価では、state を trait と誤読しないことが特に重要です。たとえば、疲労や睡眠不足で一時的に変わった反応を見て「別人になった」とは普通は言いません。一方で、長期にわたる価値観や学習方針の変化が大きい場合は、drift の扱いが難しくなります。
</p>
<div class="note-box">
<strong>安全な読み方</strong>
<p>
まずは「今日の状態の一致」と「長期的な連続性の一致」を分けて報告する方が安全です。短期の一致だけで L4 を強く主張しないことが重要です。
</p>
</div>
</section>

<section class="section" id="learning-drift">
<h2 class="section-title">学習による drift は悪いことか</h2>
<p>
必ずしも悪いことではありません。人間も学習すれば変わります。問題は、<strong>どの変化が自然な更新で、どの変化が同一性評価を壊すほど大きいか</strong>を区別しないまま、長期主張をしてしまうことです。
</p>
<div class="key-points">
<h4>最低限残したいこと</h4>
<ul>
<li><strong>更新ログ：</strong>いつ、何を学習したか。</li>
<li><strong>比較時点：</strong>どの時点どうしを比べたか。</li>
<li><strong>指標の分離：</strong>state 指標、trait 指標、drift 指標を混ぜないこと。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">縦断の話を読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>state と trait を分けているか：</strong>短期変動をそのまま本人性に使っていないか。</li>
<li><strong>観測期間があるか：</strong>日内だけか、日間か、長期か。</li>
<li><strong>drift をログ付きで追っているか：</strong>変化の履歴が残っているか。</li>
<li><strong>許容範囲があるか：</strong>どこまでの変化を認めるかが明示されているか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
L4 の全体像へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">本人性評価と連続性テスト</a>、長文の地図へ戻るなら <a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップ</a>、研究ノートへ戻るなら <a href="https://mind-upload.com/perspective.html">研究ノート</a> をご利用ください。
</p>
</section>
