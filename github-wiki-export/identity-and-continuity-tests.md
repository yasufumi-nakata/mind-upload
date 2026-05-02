# Wiki: アイデンティティ評価と連続性テスト

> 予約条件を使用した哲学とテスト設計への回帰
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-06 / Role: 学習ガイド

## このページの役割
このページは哲学用語の紹介ではなく、Mind-UploadのL4「`Individuality Assertion'' from the perspective of `「何をどのようにテストしたいのですか?」をまとめたWikiです。 We will explain from the beginning how to reduce memory, values, learning, longitudinal stability, and handling of divergences to pre-registered continuity tests.

## 正確性に関する注記
ここで説明するのは評価設計の始まりです。どのような条件で最終的に二人が同一人物であると判断できるのかはまだ未解明であり、このページではその結論を示していません。

## 公開ページへ戻る
- [WBE の概要](https://mind-upload.com/wbe_101.html)
- [検証プラットフォーム](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki ページ
- [Wiki: ID とコピーの問題](https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem) - まずは哲学の基礎に立ち返りたい人向けです。
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - これは、L4 の主張の強さを補います。
- [Wiki: 反事実/介入/摂動](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - これは、条件の変化に対する反応を確認する理由を説明します。
- [Wiki: 状態/特性/ドリフト](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - 長期的な評価において短期的な状態と長期的な特性を区別する方法を補足します。
- [Wiki: 更新/分岐/停止ルール](https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules) - ブランチログ、バージョン管理、停止条件の基本を補足します。

## 現在わかっていること
- 同一性の主張は L0 ～ L3 よりも強く、単なる出力一致では十分ではありません。
- 記憶、価値観、学習履歴、状況の変化に対する反応を個別に見る必要があります。
- 分岐や長期にわたる漂流は、アイデンティティの主張をさらに困難にします。

## まだわかっていないこと
- 十分条件を構成するにはどのテストの組み合わせが満たされなければならないかはまだ未解決です。
- 継続的な移行がアイデンティティを保護するのに十分であるかどうかはまだ証明されていません。

---

<h2>最短のアイデア</h2>
<p>
誰かのアイデンティティを尋ねるとき、必要なのは、その人が同じ話し方をしているかどうかを尋ねるだけではありません。まず、何が起こっているのか、問題が発生した場合に何を保留するのかを決めることが重要です。
</p>

<h2>なぜL4が急に難しくなるのか</h2>
<p>
L1 と L2 には、精度や予測一致などの比較的明確な指標を入れることができます。しかし、L4では「`Is this memory match enough?'' ``If a person's values ​​change slightly, are they a different person?'' and `「学習による変化をどこまで許容すべきか」という問題が絡んでくる。つまり、測定だけでなく判定ルール自体も難しくなってしまうのです。
</p>

<h2>まずは分けて検討すべき5つの項目</h2>
<table>
<thead>
<tr>
<th>アイテム</th>
<th>何が見たいですか</th>
<th>それだけでは不十分な理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>メモリ</strong></td>
<td>自伝的記憶とエピソードの一貫性。 </td>
<td>メモリー再生だけでは、必ずしも主観的な連続性を示すわけではありません。 </td>
</tr>
<tr>
<td><strong>値/設定</strong></td>
<td>判断の傾向と優先順位の一貫性。 </td>
<td>短期的な気分の変動と長期的な性格傾向を区別する必要があります。 </td>
</tr>
<tr>
<td><strong>学習履歴</strong></td>
<td>新しい体験を取り入れ、以前のトレンドと結びつける方法。 </td>
<td>学習すれば変化するのは当然であり、変化そのものを直ちにミスマッチとは言えません。 </td>
</tr>
<tr>
<td><strong>状態の変化に対する反応</strong></td>
<td>未学習の条件や介入の下で、反応はどのように分岐しますか? </td>
<td>平常時は似ていても、分岐により大きく崩れる可能性があります。 </td>
</tr>
<tr>
<td><strong>縦方向の安定性</strong></td>
<td>1日内、日ごと、長期にわたって何が安定し、何が変動するのか？ </td>
<td>一度の測定だけでは同一性の持続性を確認することはできません。 </td>
</tr>
</tbody>
</table>

<h2>どのような導通テストを検討しますか</h2>

<h4>T例として含めたいテスト</h4>
<ul>
<li><strong>自伝的記憶の調整: イベントの内容だけでなく、それらの関連性や優先順位も追跡します。 </li>
<li><strong>好みの安定性:</strong>価値判断と選択の傾向が短期的なノイズを超えて持続するかどうかを調べます。 </li>
<li><strong>学習の継続性:</strong>新しい情報を与えた後、更新方法が元の傾向とつながっているかどうかを確認します。 </li>
<li><strong>分岐検証:</strong>条件を変更する場合、別個体として扱うべき点を記録します。 </li>
<li><strong>長期ドリフトモニタリング:</strong> 数日または数週間にわたって変化する特性と変化しない特性を追跡します。 </li>
</ul>

<p>特に縦断評価の入口だけを先に整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift">Wiki:state/trait/drift</a>が補講となります。 </p>

<h2>事前登録が特に重要な理由</h2>
<p>
人の性格の評価は、後から考えるとその人に都合の良いように解釈できます。そのため、<strong> </strong> ``what to consider as a match,'' ``to what degree of deviation to suspend,'' and ``どのブランチを別個体として扱うかを事前登録する必要があります。
</p>

<strong>まず決めるべきこと</strong>
<p>
試験項目、採点ルール、観察期間、故障条件、停止条件、分岐の扱いです。 L4ではこの部分があいまいだと全体の結論が揺らいでしまいます。
</p>

<h2>分岐が発生すると大変なこと</h2>
<p>
2 つのシステムがある時点で別々に学習し始めた場合、最初はほぼ同じになる可能性がありますが、時間の経過とともに異なる履歴を持つことになります。現時点で問題となるのは、「`to what point should they be treated as the same evaluation unit?'' and `をどの時点で別個の存在として分離すべきか」だ。
</p>
<p>
したがって、L4 を評価する際には、類似性だけでなく、<strong> ブランチログ </strong> および <strong> バージョン管理 </strong> も考慮することが重要です。
</p>
<p>
分岐点、分岐ID、停止条件、キルスイッチの違いを先に明確にしたい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules">Wiki:更新・分岐・停止ルール</a>を補講とします。
</p>

<h2>この段階で言ってはいけないこと</h2>
<table>
<thead>
<tr>
<th>誇張しやすい表現</th>
<th>より安全に読書</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>本人確認済み</strong></td>
<td> 事前に登録した導通テストグループでは、これまでのところ大きな差異はありません。 </td>
</tr>
<tr>
<td><strong>同一人物が完全に保存されました</strong></td>
<td>記憶、価値観、学習、分岐に関する事前評価が確立されています。 </td>
</tr>
<tr>
<td><strong>長期的には同じ</strong></td>
<td>観察期間内に、定義された指標に有意な変動は観察されませんでした。 </td>
</tr>
</tbody>
</table>

<h2>L4 ストーリーを読み取る際の最小限のチェック</h2>

<h4>チェックリスト</h4>
<ul>
<li><strong>連続的とは何だと思いますか:</strong>記憶、価値観、学習、分岐、または長期的なものを見ているかどうか。 </li>
<li><strong>事前登録はありますか?</strong>基準は後から変更されますか? </li>
<li><strong>失敗条件はありますか?</strong>プロジェクトが保留される原因となる矛盾はありますか? </li>
<li><strong>観察期間は十分ですか?</strong>単一の一致は長期的な同一性を示しますか? </li>
</ul>

<h2>次に戻る場所</h2>
<p>
理念志向の入り口に戻りたい場合は<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem">Identityとコピー問題</a>を、L4の位置に戻りたい場合は<a href="https://mind-upload.com/wbe_101.html">WBE</a>を、検証設計に戻りたい場合は<a href="https://mind-upload.com/verification.html">検証基盤</a>をご利用ください。
</p>
