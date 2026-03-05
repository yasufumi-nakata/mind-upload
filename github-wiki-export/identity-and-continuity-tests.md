# Wiki：本人性評価と連続性テスト

> 哲学の話を、保留条件つきのテスト設計へ戻す
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
このページは、Mind-Upload における L4『本人性主張』を、哲学用語の紹介ではなく『何をどうテストしたいのか』の観点から整理する wiki です。記憶、価値観、学習、縦断安定性、分岐時の扱いを、事前登録された連続性テストへどう落とすかを初歩から説明します。

## 正確さの前提
ここで述べるのは評価設計の入口です。どの条件で『同じ本人』と最終判定できるかは未解決であり、このページもその結論を与えるものではありません。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: 本人性とコピー問題](https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem) - まず哲学的な土台へ戻りたい人向けです。
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - L4 がどれだけ強い主張かを補います。
- [Wiki: 反事実・介入・摂動](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - 条件変更への反応まで見たい理由を補います。
- [Wiki: state・trait・ドリフト](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - 縦断評価で短期状態と長期特徴をどう分けるかを補います。
- [Wiki: 更新・分岐・停止規則](https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules) - 分岐ログ、版管理、停止条件の初歩を補います。

## いま分かっていること
- 本人性の主張は、L0〜L3 より強く、単なる出力一致だけでは足りません。
- 記憶、価値観、学習履歴、条件変更への反応を分けて見る必要があります。
- 分岐や長期ドリフトがあると、本人性の主張はさらに難しくなります。

## まだ分かっていないこと
- どの組み合わせのテストを満たせば十分条件になるかは未解決です。
- 連続的移行が本人性を十分に守るかも、まだ証明されていません。

---

<h2>いちばん短い考え方</h2>
<p>
本人性を問うときに必要なのは、「同じように話すか」だけではありません。<strong>何が続いていて、何が崩れたら保留にするか</strong>を先に決めることが重要です。
</p>

<h2>なぜ L4 は急に難しくなるのか</h2>
<p>
L1 や L2 では、精度や予測一致のように比較的はっきりした指標を置けます。しかし L4 では、「この記憶の一致だけで十分か」「価値観が少し変わったら別人か」「学習による変化はどこまで許容するか」といった問題が入ってきます。つまり、測定だけでなく<strong>判定ルール</strong>そのものが難しくなります。
</p>

<h2>まず分けて考えたい 5 項目</h2>
<table>
<thead>
<tr>
<th>項目</th>
<th>何を見たいか</th>
<th>それだけでは足りない理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>記憶</strong></td>
<td>自伝的記憶やエピソードの整合性。</td>
<td>記憶再生だけで、主観的連続性まで言えるとは限りません。</td>
</tr>
<tr>
<td><strong>価値観・選好</strong></td>
<td>判断傾向や優先順位の一貫性。</td>
<td>短期の気分変動と長期の人格傾向を分ける必要があります。</td>
</tr>
<tr>
<td><strong>学習履歴</strong></td>
<td>新しい経験をどう取り込み、以前の傾向とどうつながるか。</td>
<td>学習すると変化するのは自然で、変化そのものを即不一致とは言えません。</td>
</tr>
<tr>
<td><strong>条件変更への反応</strong></td>
<td>未学習条件や介入で、どのように応答が分岐するか。</td>
<td>平常時だけ似ていても、分岐で大きく崩れる可能性があります。</td>
</tr>
<tr>
<td><strong>縦断安定性</strong></td>
<td>日内・日間・長期で、何が安定し何が揺れるか。</td>
<td>一度の測定だけでは、本人性の持続は見えません。</td>
</tr>
</tbody>
</table>

<h2>どんな連続性テストを考えたいのか</h2>

<h4>例として置きたいテスト群</h4>
<ul>
<li><strong>自伝的記憶整合：</strong>出来事の内容だけでなく、関連づけや優先度も追います。</li>
<li><strong>選好安定性：</strong>価値判断や選択傾向が、短期ノイズを超えて続いているかを見ます。</li>
<li><strong>学習連続性：</strong>新しい情報を与えたあと、更新の仕方がもとの傾向とつながるかを見ます。</li>
<li><strong>分岐検証：</strong>条件を変えたときに、どの時点から別個体として扱うべきかを記録します。</li>
<li><strong>長期ドリフト監視：</strong>数日から数週間で、変わる特徴と変わらない特徴を分けて追います。</li>
</ul>

<p>特に縦断評価の入口だけ先に整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift">Wiki: state・trait・ドリフト</a> が補講になります。</p>

<h2>なぜ事前登録が特に重要なのか</h2>
<p>
本人性の評価は、あとから見ればいくらでも都合よく解釈できてしまいます。だからこそ、「何を一致とみなすか」「どの程度のズレで保留にするか」「どの分岐を別個体として扱うか」を、<strong>事前登録</strong>しておく必要があります。
</p>

<strong>先に決めておきたいこと</strong>
<p>
テスト項目、採点ルール、観察期間、失敗条件、停止条件、分岐時の扱い、でございます。L4 ではこの部分が曖昧だと、結論全体が揺らぎます。
</p>

<h2>分岐が起きると何が難しいか</h2>
<p>
もし途中から 2 つの系が別々に学習し始めたら、最初はほぼ同じでも、時間とともに別の履歴を持ちます。このとき問題になるのは、「どの時点まで同じ評価単位として扱うか」「どこで別個体として分けるか」です。
</p>
<p>
したがって、L4 の評価では、単に似ているかだけでなく、<strong>分岐ログ</strong>と<strong>バージョン管理</strong>が重要になります。
</p>
<p>
分岐時点、branch ID、停止条件、キルスイッチの違いを先に整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules">Wiki: 更新・分岐・停止規則</a> が補講になります。
</p>

<h2>この段階でまだ言わない方がよいこと</h2>
<table>
<thead>
<tr>
<th>言いすぎやすい表現</th>
<th>より安全な読み替え</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>本人性が証明された</strong></td>
<td>事前登録した連続性テスト群で、いまのところ重大な不一致が出ていない。</td>
</tr>
<tr>
<td><strong>同じ人が完全に保存された</strong></td>
<td>記憶・価値観・学習・分岐に関する暫定評価が成立した。</td>
</tr>
<tr>
<td><strong>長期的にも同一である</strong></td>
<td>観測期間内では、定義した指標に大きなドリフトが見られなかった。</td>
</tr>
</tbody>
</table>

<h2>L4 の話を読むときの最低チェック</h2>

<h4>Checklist</h4>
<ul>
<li><strong>何を続いているとみなすか：</strong>記憶、価値観、学習、分岐、縦断のどれを見ているか。</li>
<li><strong>事前登録があるか：</strong>あと出しで基準を変えていないか。</li>
<li><strong>失敗条件があるか：</strong>どんなズレなら保留にするかが明示されているか。</li>
<li><strong>観測期間が足りているか：</strong>一回の一致で長期本人性を言っていないか。</li>
</ul>

<h2>次にどこへ戻るか</h2>
<p>
哲学寄りの入口へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem">本人性とコピー問題</a>、L4 の位置づけへ戻るなら <a href="https://mind-upload.com/wbe_101.html">WBE入門</a>、検証設計へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a> をご利用ください。
</p>
