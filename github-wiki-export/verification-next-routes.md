# Wiki：Verificationのあとに進む4つの道

> 検証基盤を読んだあと、次の1ページを迷わず決めるためのガイド
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Reading route

## このページの役割
このページは、Verification を読んだあとに、何を知りたいかに応じて次の公開ページを決める補助ガイドです。L0 の実装へ戻るのか、L2 の介入検証へ進むのか、L3 の閉ループへ進むのか、L4 の本人性へ進むのかで、次の1ページは変わります。

## 正確さの前提
ここで示すのは Verification の次の入口です。各路線の成立条件そのものは、必ず元ページ本文で確認してください。

## 公開ページへ戻る
- [検証基盤](https://mind-upload.com/verification.html)
- [ハンズオン](https://mind-upload.com/datasets.html#l0-practice)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: L0〜L5ごとの読み進め方](https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes) - レベル全体から見た導線に戻りたい人向けです。
- [Wiki: 実務系ページの読み分けガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide) - Verification、Datasets、Hands-on の役割差を先に見たい人向けです。
- [Wiki: EEGからL0までの一本道](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route) - L0 側の具体ルートだけをすぐ見たい人向けです。

## いま分かっていること
- Verification は全体設計図なので、そのままでは次の1ページが広すぎます。
- L0 の実装、L2 の検証、L3 の閉ループ、L4 の本人性では、戻るべきページが違います。
- Verification のあとに路線を固定すると、読み方がかなり安定します。

## まだ分かっていないこと
- どの路線が最終的に最重要になるかは、今後の進捗で変わる可能性があります。
- L4 や L5 の最終成立条件は、まだ未確定です。

---

<h2>次の1ページを決める</h2>
<p>
Verification は設計図として重要ですが、読むだけでは次の作業が広すぎます。ここでは、<strong>何を次に知りたいか</strong>で 4 本の道に分けて、次の1ページを固定します。
</p>

<h2>Verificationのあとに進む4つの道</h2>
<table>
<thead>
<tr>
<th>知りたいこと</th>
<th>次に開くページ</th>
<th>そこで決めること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0 の実装を作りたい</strong></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a></td>
<td>入力、QC、前処理、ベースライン、失敗例を一周つなぐ手順を固定します。</td>
</tr>
<tr>
<td><strong>L2 の介入・反事実検証を知りたい</strong></td>
<td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a></td>
<td>どの課題が因果検証や生成予測へつながるかを依存関係で確認します。</td>
</tr>
<tr>
<td><strong>L3 の閉ループ条件を知りたい</strong></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a> または <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ・遅延・ジッタ・安全停止</a></td>
<td>オフライン精度とリアルタイム安定性の違いを切り分けます。</td>
</tr>
<tr>
<td><strong>L4 の本人性を知りたい</strong></td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a> または <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">本人性評価と連続性テスト</a></td>
<td>何を連続しているとみなしたいのかを、記憶、価値観、学習、分岐で確認します。</td>
</tr>
</tbody>
</table>

<h2>なぜこの分け方なのか</h2>
<table>
<thead>
<tr>
<th>道</th>
<th>Verification のあとにそのページへ行く理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0 実装</strong></td>
<td>Verification で決めた合格条件を、Hands-on で実際の成果物に落とす必要があるからです。</td>
</tr>
<tr>
<td><strong>L2 検証</strong></td>
<td>介入や反事実は、どの論点が先に必要かを Roadmap で見ないと飛びやすいからです。</td>
</tr>
<tr>
<td><strong>L3 閉ループ</strong></td>
<td>閉ループは Verification の評価設計だけでは足りず、計測とリアルタイム制約も一緒に見る必要があるからです。</td>
</tr>
<tr>
<td><strong>L4 本人性</strong></td>
<td>本人性はスコアだけで進めず、何を事前登録してテストしたいかを先に整理する必要があるからです。</td>
</tr>
</tbody>
</table>

<h2>道ごとの補助 wiki</h2>
<table>
<thead>
<tr>
<th>道</th>
<th>一緒に見るとよい wiki</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0 実装</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">EEGからL0までの一本道</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack">L0で最低限そろえる成果物パック</a></td>
</tr>
<tr>
<td><strong>L2 検証</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification">反事実・介入・摂動の検証</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">観測から推定へ</a></td>
</tr>
<tr>
<td><strong>L3 閉ループ</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ・遅延・ジッタ・安全停止</a></td>
</tr>
<tr>
<td><strong>L4 本人性</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">本人性評価と連続性テスト</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem">本人性とコピー問題</a></td>
</tr>
</tbody>
</table>

<h2>よくある迷い方</h2>

<h4>Mistake</h4>
<ul>
<li><strong>Verification を読んだだけで次の作業が決まった気になる：</strong> 実際には路線を 1 本に絞る必要があります。</li>
<li><strong>L0 と L2 を同時に追い始める：</strong> まず再現可能解析を固めた方が手戻りが少ないです。</li>
<li><strong>L3 を精度だけで考える：</strong> 閉ループでは遅延や安全停止が別に必要です。</li>
<li><strong>L4 をスコアの延長で考える：</strong> 本人性は、何を連続しているとみなすかの事前設計が別に必要です。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
Verification の本文へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、レベル全体の導線へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">L0〜L5ごとの読み進め方</a>、実務ページ全体の役割差へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide">実務系ページの読み分けガイド</a> をご利用ください。
</p>
