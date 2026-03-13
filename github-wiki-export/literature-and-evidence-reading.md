# Wiki：文献と証拠ページの読み方

> 『論文が多い』と『結論が強い』を混同しないために
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Reading guide

## このページの役割
このページは、Mind-Upload にある文献系ページの役割分担を整理する補助ページです。論文が多いページほど、役割を取り違えると読み方が崩れるため、『何をするページか』『どこまで確定扱いしないか』を先に説明します。

## 正確さの前提
このページは読み方の補助です。個別論文や個別提案の評価は、必ず元ページと元論文へ戻って確認してください。

## 公開ページへ戻る
- [文献地図](https://mind-upload.com/research_harvest_50.html)
- [論文集](https://mind-upload.com/mind_uploading_papers.html)
- [技術提案](https://mind-upload.com/issue.html#proposal-integration)

## 関連 Wiki
- [Wiki: 文献のソース種別と状態ラベル](https://github.com/yasufumi-nakata/mind-upload/wiki/paper-source-types-and-evidence-status) - Scopus、arXiv、Review、Media、source_logged などの意味を整理します。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 証拠の強さを、何で見るべきかの前提を補います。
- [Wiki: WBEの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - 各論文や提案が、全体のどの論点に当たるかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- 役割の違うページを分けると、量の多さと結論の強さを混同しにくくなります。
- 論文集、文献地図、提案ページは、それぞれ読む目的が異なります。
- 重要な判断は、要約ではなく元論文や元ページへ戻って行う必要があります。

## まだ分かっていないこと
- どの論文が最終的に中心的根拠として残るかは、今後の整理で変わる可能性があります。
- source_logged などの状態は、後続の精査で更新されることがあります。

---

<h2>まず役割を分ける</h2>
<p>
文献系ページは、全部が同じ役割ではありません。広く拾うページ、未解決問題ごとに整理するページ、提案として統合するページを分けることで、読者が「いま何を見ているのか」を見失いにくくしています。
</p>

<strong>文献を読んだあとに次の1ページを決めたいとき</strong>
<p>
役割差だけでなく、論文や文献地図を読んだあとに未解決問題、提案、Issue、協業候補のどこへ戻るかを一本道で見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装・参加へ戻る一本道</a> をご覧ください。
</p>

<h2>3つのページの違い</h2>
<table>
<thead>
<tr>
<th>ページ</th>
<th>役割</th>
<th>ここでやること</th>
<th>ここだけではしないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>論文集</strong></td>
<td>広く拾う入口</td>
<td>年別の流れ、関連論文の存在、要約からの当たり付け。</td>
<td>各論文の最終評価をここだけで確定すること。</td>
</tr>
<tr>
<td><strong>文献地図</strong></td>
<td>未解決問題ごとの整理</td>
<td>U番号ごとに、何が解けていて何が未解決かを見ること。</td>
<td>引用数だけで結論の強さを決めること。</td>
</tr>
<tr>
<td><strong>技術提案</strong></td>
<td>実装方針の統合</td>
<td>どの提案があり、どの状態で、どこへ影響するかを追うこと。</td>
<td>提案受理を、そのまま実装完了と読むこと。</td>
</tr>
</tbody>
</table>

<h2>どこまで深読みするか</h2>
<table>
<thead>
<tr>
<th>見ているもの</th>
<th>その場で止めてよい</th>
<th>原文へ戻るべき</th>
</tr>
</thead>
<tbody>
<tr>
<td>論文カード</td>
<td>自分の論点と遠いと分かった時点。</td>
<td>方法、評価、限界を根拠として使いたいとき。</td>
</tr>
<tr>
<td>U番号の現状マップ</td>
<td>どの U が自分に関係するか分かった時点。</td>
<td>本当にその U にその文献が効くか確認したいとき。</td>
</tr>
<tr>
<td>提案の要約表</td>
<td>関係するストリームと状態が分かった時点。</td>
<td>採否や妥当性を判断したいとき。</td>
</tr>
</tbody>
</table>

<h2>読み違えを防ぐ3つのルール</h2>

<h4>Rule</h4>
<ul>
<li><strong>量と強さを混同しない：</strong> 論文数や引用数は、結論の確定とは別です。</li>
<li><strong>要約で止めすぎない：</strong> 根拠として使うときは、必ず DOI や原文へ戻ります。</li>
<li><strong>状態ラベルを読み違えない：</strong> source_logged、提案受理、文書反映は、それぞれ意味が違います。</li>
</ul>

<strong>Scopus / arXiv / source_logged の意味だけ先に確認したいとき</strong>
<p>
このページは役割差を説明する補助ページです。掲載元、文献種別、サイト内状態の違いを 1 枚で整理したい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/paper-source-types-and-evidence-status">Wiki: 文献のソース種別と状態ラベルの読み方</a> を先に見ると、論文集や文献地図の見え方が安定します。
</p>

<h2>次にどこへ戻るか</h2>
<p>
広く論文を眺めたい場合は <a href="https://mind-upload.com/mind_uploading_papers.html">論文集</a>、未解決問題から入りたい場合は <a href="https://mind-upload.com/research_harvest_50.html">文献地図</a>、提案と実装方針を追いたい場合は <a href="https://mind-upload.com/issue.html#proposal-integration">技術提案</a> へ戻ってください。
</p>
