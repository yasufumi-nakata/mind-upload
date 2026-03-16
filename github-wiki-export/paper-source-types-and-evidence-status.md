# Wiki：文献のソース種別・状態・証拠クラスの読み方

> Badge・掲載元・状態・証拠クラスを混同しないための補助ページ
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-16 / 位置づけ: Reading guide

## このページの役割
このページは、論文集や文献地図に出てくる『Scopus』『arXiv』『Review』『Media』『source_logged』『curated』などのラベルに加えて、『その文献が何を直接増やす証拠か』を、初学者向けに整理する補助ページです。ここで大事なのは、ラベルが何の情報なのかを分けて読むことです。

## 正確さの前提
ラベルは読み方の補助であり、論文内容の正しさを自動的に保証するものではありません。根拠として使うときは、必ず DOI、本文、一次研究へ戻ってください。

## 公開ページへ戻る
- [論文集](https://mind-upload.com/mind_uploading_papers.html)
- [文献地図](https://mind-upload.com/research_harvest_50.html)
- [ケースワーク](https://mind-upload.com/verification.html#casework)

## 関連 Wiki
- [Wiki: 文献と証拠ページの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - 論文集、文献地図、提案ページの役割差を先に整理します。
- [Wiki: 主張と証拠の読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - ラベルの先にある『主張の強さ』をどう読むかを補います。
- [Wiki: U番号ガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/u-number-guide) - 文献地図で、どの未解決問題に関係するかを見る補助ページです。

## いま分かっていること
- 同じ文献でも、掲載元、文献種別、サイト内状態、証拠クラスは別々に見る必要があります。
- Scopus は索引、arXiv はプレプリント置き場、Review は文献種別であり、互いに同じ意味ではありません。
- source_logged と curated は、このサイト内での整理状態を示すラベルです。
- 技術・自然科学では、掲載元よりも『何を直接増やす証拠か』を先に固定した方が誤読を減らせます。

## まだ分かっていないこと
- 個々の論文が最終的にどこまで中心的根拠として残るかは、後続の精査で変わります。
- レビューやニュースから辿った話題が、一次研究へ戻ると弱まる場合もあります。

---

<h2>まず4つに分ける</h2>
<p>
文献ページで混乱しやすいのは、<strong>どこに載っているか</strong>、<strong>どんな種別の文献か</strong>、<strong>このサイト内で今どの状態か</strong>、<strong>その論文が何を直接増やす証拠か</strong>を同じものとして読んでしまうことです。まずこの4つを分けるだけで、かなり誤読が減ります。
</p>

<h2>ラベルには4つの軸があります</h2>
<table>
<thead>
<tr>
<th>軸</th>
<th>何を表すか</th>
<th>例</th>
<th>それだけでは言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>掲載元・Badge</strong></td>
<td>どこから辿れる文献か、どの入口で拾ったかです。</td>
<td>Scopus / arXiv / 学術誌ページ / DOI</td>
<td>内容が強い、正しい、中心的根拠であるとは決まりません。</td>
</tr>
<tr>
<td><strong>文献種別</strong></td>
<td>その文書が一次研究なのか、レビューなのか、ニュースなのかです。</td>
<td>Primary / Review / Media</td>
<td>新規データの有無や、検証に直接使える強さは別途確認が必要です。</td>
</tr>
<tr>
<td><strong>サイト内状態</strong></td>
<td>このサイトで、入力受理済みか、整理済みか、除外済みかを示します。</td>
<td>source_logged / curated / noise_excluded</td>
<td>論文内容が真である、または価値が低い、とまでは決まりません。</td>
</tr>
<tr>
<td><strong>証拠クラス</strong></td>
<td>その文献が、技術的に何を直接強くするかです。</td>
<td>direct validation / system demo / dataset・benchmark・standard / review / context</td>
<td>掲載元や状態だけで、その文献が何を直接増やすかは決まりません。</td>
</tr>
</tbody>
</table>

<strong>同じ文献に複数の属性が重なります</strong>
<p>
たとえば、ある文献が <strong>Scopus に載っているレビュー論文</strong> であることもあれば、<strong>arXiv にある一次研究のプレプリント</strong> であることもあります。ひとつのラベルだけで全体を決めないでください。
</p>

<h2>技術・自然科学では『証拠クラス』を別軸で読みます</h2>
<p>
今回さらに固定すべきだったのは、<strong>掲載元や状態</strong>と、<strong>その論文が何を直接増やすか</strong>を分けることでした。これは普遍的な学術規格そのものではなく、<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> のような <strong>direct validator</strong> と、<a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a>、<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a> のような <strong>task-limited system demo</strong>、<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a>、<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a>、<a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a>、<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a>、<a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a>、<a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> のような <strong>mechanistic boundary / hidden-state evidence</strong>、さらに <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns et al. (2024)</a>、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018)</a>、<a href="https://proceedings.mlr.press/v37/blum15.html" target="_blank">Blum &amp; Hardt (2015)</a>、<a href="https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html" target="_blank">Roelofs et al. (2019)</a> が担う <strong>再現・比較・ガバナンス</strong> の役割差から、本サイトが引く <strong>運用上の分類</strong>でございます。
</p>
<table>
<thead>
<tr>
<th>証拠クラス</th>
<th>典型例</th>
<th>直接強くなるもの</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>direct validator / causal calibration</strong></td>
<td><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan 2020</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse 2023</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao 2025</a></td>
<td>局所妥当化、誤差源、刺激条件、coverage boundary を直接監査できます。</td>
<td>whole-brain ground truth や一般的一意復元までは自動で支えません。</td>
</tr>
<tr>
<td><strong>task-limited system demonstration</strong></td>
<td><a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang 2023</a>、<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli 2025</a>、<a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett 2023</a>、<a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn 2025</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar 2025</a></td>
<td>特定課題・特定サブシステムでの decode、communication、閉ループ性能を押し上げます。</td>
<td>そのまま whole-brain emulation、本人性、state-complete reconstruction を意味しません。</td>
</tr>
<tr>
<td><strong>dataset / benchmark / standard / toolchain</strong></td>
<td><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet 2019</a>、<a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns 2024</a>、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe 2025</a>、<a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant 2018</a>、<a href="https://proceedings.mlr.press/v37/blum15.html" target="_blank">Blum &amp; Hardt 2015</a>、<a href="https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html" target="_blank">Roelofs 2019</a></td>
<td>再利用可能性、比較可能性、同期、split、leaderboard governance を強くします。</td>
<td>生物学的十分性や mechanistic truth を直接は増やしません。</td>
</tr>
<tr>
<td><strong>mechanistic boundary / hidden-state evidence</strong></td>
<td><a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens 2021</a>、<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen 2016</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu 2024</a>、<a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser 2024</a>、<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill 2024</a>、<a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson 2025</a>、<a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar 2025</a></td>
<td>何が latent state として残り、どの simplification が claim ceiling を作るかを強くします。</td>
<td>それ自体は direct validation でも実装完了でもありません。何をまだ省略できないかを示すクラスです。</td>
</tr>
<tr>
<td><strong>review / synthesis</strong></td>
<td>technical review、survey、benchmark synthesis</td>
<td>論点の地図、キーワード、比較軸を素早く揃えられます。</td>
<td>強い根拠に使うときは、一次研究へ戻る必要があります。</td>
</tr>
<tr>
<td><strong>context / philosophy / law / culture</strong></td>
<td>概念整理、法学、倫理、文化論、作品論</td>
<td>話題の周辺文脈や問題設定の広さを理解できます。</td>
<td>技術・自然科学の feasibility や validation frontier の根拠にはしません。</td>
</tr>
</tbody>
</table>

<strong>この分類の使い方</strong>
<p>
同じ文献が <strong>Scopus 掲載</strong>で、かつ<strong>一次研究</strong>で、しかも<strong>dataset / benchmark</strong> クラスに属することはありえます。重要なのは、最後に <strong>何を直接強くする論文なのか</strong> を固定することです。技術・自然科学の主導線では、まず <strong>direct validator</strong>、<strong>task-limited demo</strong>、<strong>mechanistic boundary / hidden-state evidence</strong> のどれかを見分け、その後に <strong>standard / benchmark</strong> で比較条件を整えます。
</p>

<h2>掲載元や種別の読み方</h2>
<table>
<thead>
<tr>
<th>表示</th>
<th>日常語で言うと</th>
<th>役に立つ点</th>
<th>注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scopus</strong></td>
<td>学術文献の索引データベース経由で見つかる文献です。</td>
<td>書誌情報を整理しやすく、学術文献を広く拾う入口になります。</td>
<td>Scopus は索引であり、査読の強さや論点への直結度を自動で保証しません。</td>
</tr>
<tr>
<td><strong>arXiv</strong></td>
<td>プレプリントの公開置き場です。</td>
<td>新しい研究を早く見つけられます。</td>
<td>投稿時点では査読前のことが多く、方法と限界を自分で確認する必要があります。</td>
</tr>
<tr>
<td><strong>Review</strong></td>
<td>複数研究をまとめる総説です。</td>
<td>分野全体の地図や主要論点を掴むのに向いています。</td>
<td>自前の新規実験が主役とは限らないため、強い根拠に使うときは一次研究へ戻ります。</td>
</tr>
<tr>
<td><strong>Media</strong></td>
<td>ニュース記事、解説記事、一般向け紹介です。</td>
<td>話題の入口や一次文献探索の手掛かりになります。</td>
<td>そのままでは学術的根拠として弱く、必ず元の論文や発表へ辿る必要があります。</td>
</tr>
<tr>
<td><strong>Primary</strong></td>
<td>新しいデータ、実験、解析を直接出している一次研究です。</td>
<td>方法、評価、限界を確認すれば、最も直接に根拠を追えます。</td>
<td>一次研究でもサンプル条件、統計、再現性の弱さはあり得るため、無条件では使えません。</td>
</tr>
</tbody>
</table>

<h2>サイト内状態ラベルの読み方</h2>
<table>
<thead>
<tr>
<th>ラベル</th>
<th>日常語で言うと</th>
<th>次に必要なこと</th>
<th>誤読しやすい点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>source_logged</strong></td>
<td>入口として URL や DOI を受け付け、追跡対象に入れた段階です。</td>
<td>関連性確認、一次文献追跡、U番号割当、要約の精査が必要です。</td>
<td>「採用確定」や「高品質確定」を意味しません。</td>
</tr>
<tr>
<td><strong>curated</strong></td>
<td>このサイトの論点に沿って整理し、配置済みの段階です。</td>
<td>重複整理、強い根拠との差し替え、更新追跡は今後も必要です。</td>
<td>「内容が真である」と保証するラベルではありません。</td>
</tr>
<tr>
<td><strong>noise_excluded</strong></td>
<td>関係が薄い、混入が大きい、現時点では使わないと判断した段階です。</td>
<td>除外理由を残し、同種の混入を防ぐことが重要です。</td>
<td>論文自体の価値がゼロという意味ではなく、このサイトの論点とずれた可能性もあります。</td>
</tr>
</tbody>
</table>

<h2>どこで止まり、どこで原文へ戻るか</h2>
<table>
<thead>
<tr>
<th>いまの目的</th>
<th>ここで止めてよい</th>
<th>原文へ戻るべき</th>
</tr>
</thead>
<tbody>
<tr>
<td>広く話題を拾いたい</td>
<td>Badge、要約、5ポイント整理で関心の有無が分かった時点。</td>
<td>その論文を引用して強い主張を支えたいとき。</td>
</tr>
<tr>
<td>source_logged の項目を見ている</td>
<td>「まだ入口段階だ」と理解できた時点。</td>
<td>一次研究へ追えそうか、U番号に入るかを判断したいとき。</td>
</tr>
<tr>
<td>Review や Media を見ている</td>
<td>論点の地図や関連キーワードを掴めた時点。</td>
<td>評価、方法、数値を根拠として使いたいとき。</td>
</tr>
<tr>
<td>dataset / benchmark / standard 論文を見ている</td>
<td>split、同期、メタデータ、submission rule などの比較条件が理解できた時点。</td>
<td>その dataset や benchmark の score を frontier claim に使いたいとき。</td>
</tr>
<tr>
<td>Scopus や arXiv の文献を比較している</td>
<td>どの入口から拾われたかを把握できた時点。</td>
<td>査読状況、実験条件、限界、追試可能性を確認したいとき。</td>
</tr>
</tbody>
</table>

<h2>よくある誤読</h2>

<h4>Misread</h4>
<ul>
<li><strong>「Scopus だから強い」：</strong> Scopus は索引です。論点への効き方は、本文と方法で確認します。</li>
<li><strong>「arXiv だから全部弱い」：</strong> 査読前でも重要な入口はあります。弱いかどうかは内容で見ます。</li>
<li><strong>「Review だから十分」：</strong> 総説は地図として有用ですが、直接の根拠は一次研究へ戻る必要があります。</li>
<li><strong>「dataset 論文だから生物学も証明した」：</strong> 規格・ベンチ・toolchain は比較条件を強くしますが、mechanism の直接証拠ではありません。</li>
<li><strong>「decode demo だから emulation に近い」：</strong> task-limited system demo は subsystem performance を押し上げても、whole-brain claim へは自動昇格しません。</li>
<li><strong>「source_logged だから採用済み」：</strong> まだ受理ログであり、統合や除外の判断は後続作業です。</li>
<li><strong>「curated だから真である」：</strong> 整理済みであることと、最終的に正しいことは別です。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
論文を広く眺めたい場合は <a href="https://mind-upload.com/mind_uploading_papers.html">論文集</a>、未解決問題との対応を見たい場合は <a href="https://mind-upload.com/research_harvest_50.html">文献地図</a>、そもそもの役割差から整理したい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading">文献と証拠ページの読み方</a> に戻ってください。
</p>
