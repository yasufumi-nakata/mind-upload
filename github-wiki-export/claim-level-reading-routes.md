# Wiki：L0〜L5ごとの読み進め方

> 主張の強さごとに、どの公開ページへ行くかを決めるガイド
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Reading guide

## このページの役割
このページは、Mind-Upload のクレーム階段 L0〜L5 を、単なる定義ではなく『どのレベルの話を追いたいとき、どのページへ行くべきか』で整理する補助ページです。主張の強さが上がるほど、必要なページと証拠も変わります。

## 正確さの前提
このページは読み順の補助です。各レベルの成立条件そのものは、必ず元ページ本文で確認してください。

## 公開ページへ戻る
- [WBE入門](https://mind-upload.com/wbe_101.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [技術ロードマップ](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - L0〜L5 の意味を日常語で確認できます。
- [Wiki: 公開ページの読み分けガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - 公開ページどうしの役割差そのものを整理します。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページへ戻れます。

## いま分かっていること
- L0〜L2 は比較的工学的に進めやすく、L3 以降は追加条件が急に増えます。
- L4 と L5 は、出力一致や精度だけでは進めません。
- 主張レベルごとに、見るべきページが違います。

## まだ分かっていないこと
- どの条件を満たせば最終的に L4 や L5 が成立すると認めるかは、まだ未確定です。
- 今後のデータ、ベンチ、制度整備で読む順が少し変わる可能性があります。

---

<div class="abstract-box">
<h2>まず段階で分ける</h2>
<p>
L0〜L5 は「研究のえらさ」ではなく、<strong>主張の強さ</strong>です。したがって、読みたい主張の強さが変われば、先に見るべきページも変わります。
</p>
</div>

<section class="section" id="routes">
<h2 class="section-title">L0〜L5 ごとの入口</h2>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>いま知りたいこと</th>
<th>まず開くページ</th>
<th>次に補うページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong> 再現可能な解析</td>
<td>他の人が同じ結果を再実行できるかを知りたい。</td>
<td><a href="https://mind-upload.com/hands_on.html">Hands-on</a></td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a> / <a href="https://mind-upload.com/verification.html">Verification</a></td>
</tr>
<tr>
<td><strong>L1</strong> デコーディング</td>
<td>脳信号から何かを予測できた、という話を正しく読みたい。</td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a></td>
<td><a href="https://mind-upload.com/faq.html">FAQ</a> / <a href="https://mind-upload.com/eeg_101.html">EEG 101</a></td>
</tr>
<tr>
<td><strong>L2</strong> 生成・介入予測</td>
<td>未学習条件や条件変更への応答まで見たい。</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a> / <a href="https://mind-upload.com/perspective.html">Perspective</a></td>
</tr>
<tr>
<td><strong>L3</strong> 閉ループ</td>
<td>リアルタイムで安定に動くか、安全停止まで見たい。</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a> / <a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a></td>
</tr>
<tr>
<td><strong>L4</strong> 本人性</td>
<td>記憶、価値観、学習の連続性をどう読むか知りたい。</td>
<td><a href="https://mind-upload.com/wbe_101.html">WBE 101</a></td>
<td><a href="https://mind-upload.com/idea.html">Idea</a> / <a href="https://mind-upload.com/perspective.html">Perspective</a></td>
</tr>
<tr>
<td><strong>L5</strong> 社会実装</td>
<td>権利、安全、停止基準、制度まで含めて見たい。</td>
<td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a></td>
<td><a href="https://mind-upload.com/collaborations.html">Collaborations</a> / <a href="https://mind-upload.com/issue.html">Issue</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-route">
<h2 class="section-title">なぜこの順なのか</h2>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>このページから入る理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>L0 は概念より提出物と手順が重要なので、Hands-on から入る方が早いです。</td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>L1 はニュースで誤読されやすいため、WBE 101 で主張レベルを先にそろえる方が安全です。</td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>L2 は介入や反事実が入るため、評価設計の中心である Verification から入る方がよいです。</td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>L3 はオフライン精度と別問題なので、Verification と Roadmap の両方が必要です。</td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>L4 は本人性の主張なので、WBE 101 で強さを確認したあと、Idea や Perspective で深掘りします。</td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>L5 は制度や外部依存が大きいため、Roadmap と Collaborations を併読する必要があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-misreads">
<h2 class="section-title">よくある読み違い</h2>
<div class="key-points">
<h4>Misread</h4>
<ul>
<li><strong>L0 の話を軽く見る：</strong> 実は比較可能性の土台なので、最初に最も重要です。</li>
<li><strong>L1 の成功をそのまま L4 に伸ばす：</strong> ここが最も典型的なすり替えです。</li>
<li><strong>L3 を精度だけで語る：</strong> 遅延、ジッタ、安全停止が無いと閉ループの主張になりません。</li>
<li><strong>L5 を技術だけで決める：</strong> 制度、権利、責任の層が別にあります。</li>
</ul>
</div>
</section>

<section class="section" id="wiki-helpers">
<h2 class="section-title">各レベルで一緒に見るとよい wiki</h2>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>補助 wiki</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack">L0で最低限そろえる成果物パック</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage">データ分割とデータリーク</a></td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/decode-vs-emulate">Decode と Emulate</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence">主張と証拠の読み方</a></td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification">反事実・介入・摂動の検証</a></td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/closed-loop-latency-jitter-and-safety-stops">閉ループ・遅延・ジッタ・安全停止</a></td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/identity-and-continuity-tests">本人性評価と連続性テスト</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem">本人性とコピー問題</a></td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製と外部依存の切り分け</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules">更新・分岐・停止規則</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
L0〜L5 の定義そのものへ戻るなら <a href="https://mind-upload.com/wbe_101.html">WBE入門</a>、勝利条件の設計へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、依存関係の地図へ戻るなら <a href="https://mind-upload.com/tech_roadmap.html">技術ロードマップ</a> をご利用ください。
</p>
</section>
