# Wiki：更新・分岐・停止規則

> 変わるシステムを、変わるまま監査するための基本
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
このページは、Mind-Upload で頻繁に出てくる『更新』『バージョン』『分岐』『停止規則』『キルスイッチ』を、初歩から切り分ける wiki です。スコアが上がったから同じ系の自然な進歩だ、と短絡せず、変化を履歴つきで監査するための土台として使います。

## 正確さの前提
ここで示すのは運用と検証の基本整理です。どの程度の変化まで同一性を保つか、どの停止規則が十分かの最終基準は、課題や理論によってまだ未確定です。

## 公開ページへ戻る
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [ハンズオン](https://mind-upload.com/hands_on.html)

## 関連 Wiki
- [Wiki: 本人性評価と連続性テスト](https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests) - L4 の連続性テスト全体へ戻れます。
- [Wiki: state・trait・ドリフト](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - 更新と長期変化をどう分けるかを補います。
- [Wiki: ベースライン・事前登録・モデルカード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - 事前登録と結果記録の役割差を補います。
- [Wiki: 閉ループ・遅延・ジッタ・安全停止](https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops) - 安全停止をリアルタイム系でどう考えるかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページへ戻れます。

## いま分かっていること
- 学習やモデル更新を許すなら、履歴管理と差分記録が必要です。
- 分岐が起きると、単一の『同じ個体』という扱いは難しくなります。
- 停止規則は、結果を見たあとではなく、前もって固定する方が強いです。

## まだ分かっていないこと
- どの程度の drift や分岐差までを同一性の範囲内とみなすかは未確定です。
- L4/L5 での分岐後の責任や権利の扱いは、制度面も含めて未解決です。

---

<div class="abstract-box">
<h2>いちばん短い区別</h2>
<p>
<strong>更新</strong>は同じ履歴を引き継いだ変更、<strong>分岐</strong>は同じ起点から複数の履歴が走ること、<strong>停止規則</strong>はどんな結果で中止や保留にするかの事前ルール、<strong>キルスイッチ</strong>は危険時の緊急停止手段です。似ていますが、役割は別です。
</p>
</div>

<section class="section" id="why-this-matters">
<h2 class="section-title">なぜこの区別が必要なのか</h2>
<p>
WBE や本人性の話では、システムが固定物ではありません。学習すれば変わり、複製すれば分かれ、運用すれば停止判断が要ります。ここを曖昧にすると、「前版より点が良いから同じ系の健全な進歩だ」「分岐後も全部まとめて同じ本人だ」といった、強すぎる読み方が起きやすくなります。
</p>
</section>

<section class="section" id="terms">
<h2 class="section-title">まず用語を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ざっくり意味</th>
<th>ここで重要な点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>更新（update）</strong></td>
<td>同じ系に対して、新しい学習や設定変更を入れることです。</td>
<td>何が変わったかを差分で残さないと、評価の意味が曖昧になります。</td>
</tr>
<tr>
<td><strong>バージョン（version）</strong></td>
<td>その時点の固定された状態に付ける ID です。</td>
<td>前版を上書きせず、戻って比較できることが重要です。</td>
</tr>
<tr>
<td><strong>分岐（branch）</strong></td>
<td>同じ起点から、別々の更新履歴が走り始めることです。</td>
<td>分岐後は別の履歴なので、同じ評価単位として混ぜない方が安全です。</td>
</tr>
<tr>
<td><strong>停止規則（stop rule）</strong></td>
<td>どの結果が出たら中止、保留、撤退とするかの事前ルールです。</td>
<td>結果を見たあとで決めるより、先に固定した方が検証として強くなります。</td>
</tr>
<tr>
<td><strong>キルスイッチ / 隔離</strong></td>
<td>安全上の問題が出たときに動作を止めたり切り離したりする仕組みです。</td>
<td>停止規則と違い、統計判断ではなく安全確保が主目的です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="safe-update">
<h2 class="section-title">更新してよいかを見る最低チェック</h2>
<table class="data-table">
<thead>
<tr>
<th>確認項目</th>
<th>最低限やりたいこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>変更点の明示</strong></td>
<td>データ、前処理、モデル、評価指標のどこを変えたかを分けて書きます。</td>
</tr>
<tr>
<td><strong>前版の保存</strong></td>
<td>前の版を上書きせず、同じ入力で再実行できる状態を残します。</td>
</tr>
<tr>
<td><strong>比較条件の固定</strong></td>
<td>同じ test、同じ評価指標、同じベースラインで前版と比べます。</td>
</tr>
<tr>
<td><strong>リーク再点検</strong></td>
<td>更新で train/test の境界や正規化手順が崩れていないかを再確認します。</td>
</tr>
<tr>
<td><strong>失敗時の扱い</strong></td>
<td>性能悪化や不安定化が出た場合に、どこで更新を保留・撤回するかを先に決めます。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>重要</strong>
<p>
スコアが上がっただけでは、安全な更新とは言えません。リーク、評価変更、都合のよいサブセット選択でも数字は上がり得るため、<strong>差分</strong>と<strong>比較条件</strong>をセットで残す必要があります。
</p>
</div>
</section>

<section class="section" id="branching">
<h2 class="section-title">分岐が起きたら何を固定するか</h2>
<table class="data-table">
<thead>
<tr>
<th>固定したいもの</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>分岐時点</strong></td>
<td>どの版、どのデータ時点から枝分かれしたかを明確にするためです。</td>
</tr>
<tr>
<td><strong>親子関係</strong></td>
<td>どの branch がどの parent version を継いだかを監査できるようにします。</td>
</tr>
<tr>
<td><strong>個体 ID / インスタンス ID</strong></td>
<td>複数の履歴を同じ個体として混同しないためです。</td>
</tr>
<tr>
<td><strong>評価期間</strong></td>
<td>分岐直後だけ似ているのか、長く似ているのかを分けて読むためです。</td>
</tr>
<tr>
<td><strong>帰属ルール</strong></td>
<td>どの結果をどの branch の成果・失敗として記録するかを固定するためです。</td>
</tr>
</tbody>
</table>
<p>
特に本人性の議論では、分岐後の結果を全部まとめて「本人」と呼ぶのは危険です。少なくとも、<strong>どの時点まで同じ評価単位として扱うか</strong>を記録する必要があります。
</p>
</section>

<section class="section" id="stop-vs-kill">
<h2 class="section-title">停止規則とキルスイッチは別物</h2>
<table class="data-table">
<thead>
<tr>
<th>仕組み</th>
<th>いつ決めるか</th>
<th>主目的</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>停止規則</strong></td>
<td>実験や評価の前です。</td>
<td>失敗判定や撤退ラインを、あと出しにしないためです。</td>
</tr>
<tr>
<td><strong>保留 / freeze</strong></td>
<td>問題が見つかった時点です。</td>
<td>原因が分かるまで更新や公開を一時停止するためです。</td>
</tr>
<tr>
<td><strong>キルスイッチ / 隔離</strong></td>
<td>安全問題に備えて事前に実装しておきます。</td>
<td>危険な挙動や逸脱が出たときに、速やかに止めるためです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>ありがちな混同</strong>
<p>
「結果が悪かったので止めた」は停止規則の話で、「危険なので即停止した」は安全の話です。同じ『止める』でも、証拠の扱いと安全対策では意味が違います。
</p>
</div>
<p>
特に閉ループ実装では、遅延や異常挙動に対する安全停止が追加で重要になります。リアルタイム系の入口だけ先に整理したい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> をご覧ください。
</p>
</section>

<section class="section" id="logs">
<h2 class="section-title">最低限残したいログ</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>version ID：</strong>今どの版を評価したか。</li>
<li><strong>parent / branch ID：</strong>どこから分岐したか。</li>
<li><strong>変更差分：</strong>データ、前処理、モデル、評価の何を変えたか。</li>
<li><strong>比較結果：</strong>前版との差、改善点、悪化点、不確実性。</li>
<li><strong>停止判断：</strong>どのルールに触れたか、触れなかったか。</li>
<li><strong>失敗例：</strong>うまくいかなかった条件や崩れた条件。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">強い主張を読むときの 3 問</h2>
<ol>
<li><strong>更新前後の差分が残っているか：</strong>何を変えたのかが曖昧なら、改善の意味を読みすぎない方が安全です。</li>
<li><strong>分岐 ID と観測期間があるか：</strong>複数履歴を 1 つにまとめていないかを確認します。</li>
<li><strong>停止規則が先に決まっているか：</strong>悪い結果が出たときの扱いを、あとから書き換えていないかを見ます。</li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
Roadmap の I5 / I8 / V7 へ戻るなら <a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップ</a>、検証基盤の Registry / Audit へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、L0 実務へ戻るなら <a href="https://mind-upload.com/hands_on.html">ハンズオン</a> をご利用ください。
</p>
</section>
