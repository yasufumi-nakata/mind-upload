---
layout: default
title: 'Wiki: ソースタイプ、ステータスラベル、証拠クラスの読み方'
description: Scopus、arXiv、Review、Media、source_logged、curated、およびevidenceクラスのそれぞれが何を意味し、何を意味しないのかを整理します。
article_type: ウィキ
subtitle: バッジ、ソース、ステータス、論文が直接強化する内容の混乱を避けるための補助ページ
author: マインドアップロード研究プロジェクト
last_updated: '2026-03-26'
note: 読書ガイド
audience: 論文集や書誌地図のラベルを読み間違えたくない人、原文のどこに戻ればよいのか知りたい人。
reading_time: 8～12分
page_intro: このページは、「`Scopus,'' ``arXiv,'' ``Review,'' ``Media,'' ``source_logged,'' ``curated」などのラベルや、コレクションや書誌マップに登場する証拠クラスを初心者向けに整理した補助ページです。ここで重要なことは、これらのラベルを個別に読み、それぞれがどのような情報を表しているのかを理解することです。
accuracy_note: ラベルは読みやすさを補助するものであり、記事の内容の正確性を自動的に保証するものではありません。証拠として使用する場合は、必ず DOI、本文、一次研究を参照してください。
page_highlights:
- 出版元、文書の種類、サイトのステータス、証拠のクラスを別の軸として説明します。
- 私たちは、論文が何を直接的に強化するかという問題からソースラベルを分離する方法を示します。
- 表を使用すると、どこで停止して元のテキストに戻るかを確認できます。
- 人間の測定用紙は、可観測性クラスの進歩に応じて、デモまたは非表示状態のビンに折り畳まれるのではなく、別々に保管されます。
- 言語対応のデモは、脳からテキストへの 1 つの解決済みカテゴリーとしてではなく、ルート分割とニューラル貢献監査を通じて読み取られます。
known_points:
- 同じ文書であっても、出版元、文書の種類、サイトのステータス、証拠のクラスを個別に表示する必要があります。
- Scopus はインデックス、arXiv はプレプリント ストレージ、Review はドキュメント タイプであり、同じ意味を持ちません。
- source_logged と curated は、このサイトがどの程度編成されているかを示すラベルです。
- 人間の PET/MRS/MRI 論文は、隠れた状態を閉じたり、因果関係の十分性を証明したりすることなく、観察可能性を強化できます。
- 言語デモは、制限のない思考読み取りになることなく、セマンティック再構築、固定セグメントの取得、既知の開始デコード、プロンプト条件付き生成、またはコミュニケーション パフォーマンスを強化できます。
unknown_points:
- 個々の論文が最終的にどの程度中心的な証拠であり続けるかは、その後の精査によって決まります。
- レビューやニュースから追​​跡されたトップ記事は、一次調査に戻ると弱くなる可能性があります。
wiki_links:
- label: 'Wiki: 文献と証拠のページの読み方'
  url: /wiki/literature-and-evidence-reading.html
  description: まず、論文集、書誌地図、企画書ページの役割の違いを明らかにします。
- label: 'Wiki: 主張と証拠の読み方'
  url: /wiki/claims-and-evidence.html
  description: ラベルに記載されている「主張の強さ」の読み方を理解するのに役立ちます。
- label: 'Wiki: U 番号ガイド'
  url: /wiki/u-number-guide.html
  description: これは、どの未解決の質問が書誌マップに関連しているかを確認するための補助ページです。
recommended_pages:
- label: 論文集
  url: /mind_uploading_papers.html
- label: 文学地図
  url: /research_harvest_50.html
- label: ケースワーク
  url: /verification.html#casework
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まずは4分割</h2>
<p>
文献ページで混乱を招く可能性があるのは、<strong>論文が掲載されている場所</strong>、<strong>文献の種類</strong>、<strong>このサイトの現在のステータス</strong>、<strong>直接強化する内容</strong>がすべて同じものに見えることです。この4つをまず分離することで、読み間違いを大幅に減らすことができます。
</p>
</div>

<section class="section" id="three-axes">
<h2 class="section-title">ラベルには 4 つの軸があります</h2>
<table class="data-table">
<thead>
<tr>
<th>軸</th>
<th>それは何を表していますか</th>
<th>例</th>
<th>それだけではありません</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>発行者/バッジ</strong></td>
<td>書類をどこから辿って、どの入り口から拾ったのか、ということです。 </td>
<td>Scopus / arXiv / 学術雑誌ページ / DOI</td>
<td>コンテンツが強力、正確、または中心的であるとは判断されません。 </td>
</tr>
<tr>
<td><strong>書類タイプ</strong></td>
<td>文書が一次研究、レビュー、またはニュースであるかどうか。 </td>
<td>プライマリー / レビュー / メディア</td>
<td>新しいデータがあるか、直接検証に使用できる強度があるかを別途確認する必要があります。 </td>
</tr>
<tr>
<td><strong>サイトステータス</strong></td>
<td>このサイトで入力が受け入れられたか、整理されたか、または除外されたかを示します。 </td>
<td>source_logged / 厳選 / ノイズ_除外</td>
<td>論文の内容が必ずしも真実である、あるいは価値が低いというわけではありません。 </td>
</tr>
<tr>
<td><strong>証拠クラス</strong></td>
<td> 技術的な読書フローにおいて論文が直接強化している内容を示します。 </td>
<td>Direct バリデータ / システムデモ / 可観測性クラスの進歩 / ベンチマーク / 隠れ状態境界</td>
<td>それでも問題全体が解決したとは言えません。証拠軸が移動した<strong>のみを修正します</strong>.</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>同じドキュメント内で複数の属性が重複している</strong>
<p>
たとえば、ドキュメントは、Scopus</strong> に関する <strong>review 記事、arXiv</strong> に関する一次研究の <strong>preprint、または可観測性クラスアドバンス bin</strong> に属する <strong>curated human-MRI 論文である可能性があります。 1 つのラベルだけに依存しないでください。
</p>
</div>

<section class="section" id="source-kinds">
<h2 class="section-title">出版元とタイプの見方</h2>
<table class="data-table">
<thead>
<tr>
<th>ディスプレイ</th>
<th>日常用語</th>
<th>便利なポイント</th>
<th>メモ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Sコパス</strong></td>
<td>これらは学術文献索引データベース経由で見つかった文書です。 </td>
<td>書誌情報の整理が容易で、幅広い学術文献を手に取る入り口となります。 </td>
<td>Scopus は指標であり、査読の強度や問題との直接的な関連性を自動的に保証するものではありません。 </td>
</tr>
<tr>
<td><strong>arXiv</strong></td>
<td>これはプレプリントの公開保管領域です。 </td>
<td>新しい研究をすぐに見つけることができます。 </td>
<td>投稿時点ではまだ査読されていない論文も多いため、査読方法や制限事項についてはご自身で確認する必要があります。 </td>
</tr>
<tr>
<td><strong>レビュー</strong></td>
<td>これは複数の研究をまとめたレビュー記事です。 </td>
<td>分野全体のマップや主要な論点を把握するのに適しています。 </td>
<td>自分自身の新たな実験が必ずしも主役ではないため、有力な証拠として利用する場合には一次研究に戻ります。 </td>
</tr>
<tr>
<td><strong>メディア</strong></td>
<td>ニュース記事、解説記事、総合紹介。 </td>
<td>トピックへの入り口や一次文献検索の手がかりとして活用できます。 </td>
<td>このままでは学術的根拠としては弱く、元の論文や発表まで遡る必要がある。 </td>
</tr>
<tr>
<td><strong>プライマリ</strong></td>
<td>新しいデータを直接生み出す一次研究、実験、分析。 </td>
<td>証拠は、方法、評価、制限を確認することで最も直接的に追跡できます。 </td>
<td>一次研究であってもサンプル条件や統計性、再現性が弱い場合があり、一概に使用できるわけではありません。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="evidence-class">
<h2 class="section-title">証拠クラスの読み方</h2>
<table class="data-table">
<thead>
<tr>
<th>証拠クラス</th>
<th>直接的に強化されるもの</th>
<th>代表例</th>
<th>それでも正当化されないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>直接バリデータ/因果的校正</strong></td>
<td>エラーソース、キャリブレーション限界、およびローカルグラウンドトゥルースチェック。</td>
<td>ミクラン (2020)、ウンウォンセ (2023)、ハオ (2025)</td>
<td>全脳の一意性回復または完全な隠れ状態の閉鎖。</td>
</tr>
<tr>
<td><strong>タスク限定システムデモ</strong></td>
<td>Tタスク条件付き言語デコード、プロンプト条件付き生成、音素シーケンス デコード、または特定のスキャフォールドおよびインターフェイスでの閉ループ通信パフォーマンス。</td>
<td>Tang (2023)、D&eacute;fossez (2023)、d'Ascoli (2025)、Ye (2025)、Willett (2023)、Littlejohn (2025)、Wiragkar (2025)、Singh (2025)</td>
<td>全脳エミュレーション、無制限の思考読み取り、アイデンティティの連続性、または隠れ状態の完全性。</td>
</tr>
<tr>
<td><strong>データセット / ベンチマーク / 標準 / ツールチェーン</strong></td>
<td>比較可能性、同期、ガバナンス、再現性。</td>
<td>EEG-BIDS、モーション-BIDS、LSL、MOABB</td>
<td>生物学的充足性またはメカニズムの真実。</td>
</tr>
<tr>
<td><strong>可観測性クラスの先進/ヒューマンプロキシラダー</strong></td>
<td>人間が特定の測定クラスで直接観察または近似できるもの。</td>
<td>シャプソンコー (2024)、ヨハンセン (2024)、ルケッティ (2025)、バーズヴィク (2024)、ジェチョルジェク (2022)、ヒルシュラー (2025)</td>
<td>状態完全測定。各プロキシまたはアトラスには依然として請求上限があります。</td>
</tr>
<tr>
<td><strong>機械的境界/隠された状態の証拠</strong></td>
<td>コネクトーム、細胞タイプ、または強力なデモの後でも、まだ潜在しているもの、または省略されているもの。</td>
<td>Gouwens (2021)、Hengen (2016)、Xu (2024)、Looser (2024)、Cahill (2024)</td>
<td>直接検証または完成した実装。</td>
</tr>
<tr>
<td><strong>レビュー/総合</strong></td>
<td>フィールド マップ、用語、および問題のクラスタリング。</td>
<td>レビュー記事とベンチマーク合成</td>
<td>一次研究に立ち返ることのない強力な結論。</td>
</tr>
<tr>
<td><strong>文脈/哲学/法律/文化</strong></td>
<td>トピックとその周囲の議論に関するコンテキスト。</td>
<td>倫理、法的分析、形而上学、文化研究</td>
<td>それ自体が技術的または自然科学のフロンティアです。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>言語対応のデモにはもう 1 つの分割が必要</strong>
<p>
このサイトでは、読者が言語に関連するすべての結果を 1 つの `brain-to-text` カテゴリとして扱う場合、`task-limited system demonstration` はまだ広すぎます。 <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tangら(2023) </a> は <strong> をサブジェクト内の意味再構成に制約します </strong>、<a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">D&eacute;fossez et al. (2023)</a> 制約 <strong> 固定セグメント音声検索</strong>、<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> は <strong> の既知の開始語のデコードを制約します</strong>、<a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">Ye ら。 (2025) </a> は <strong> プロンプト条件付き生成を抑制する </strong>、および <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">ウィレットら(2023)</a>、<a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Lリトルジョンら。 (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairragkar et al. (2025)</a> は、さまざまな侵襲的な音声デコードまたは通信サブシステムのルートを制限します。したがって、論文が流暢なテキストまたは音声を発する場合、このサイトでは、タスク条件付き証拠を超えて宣伝される前に、<a href="../verification.html#neural-contribution-card">Neural Contribution Card</a> を要求します。
</p>
</div>

<section class="section" id="status-labels">
<h2 class="section-title">サイト ステータス ラベルの読み方</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベル</th>
<th>日常用語</th>
<th>次に必要なもの</th>
<th>読み間違えやすい</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>source_logged</strong></td>
<td>これは、URL と DOI をエントリ ポイントとして受け入れ、追跡ターゲットに含める段階です。 </td>
<td>関連性の確認、一次文献追跡、U 番号の割り当て、および抄録の精査が必要です。 </td>
<td>「採用確定」「高品質確定」を意味するものではございません。 </td>
</tr>
<tr>
<td><strong>厳選</strong></td>
<td>このサイトは論点に沿って整理・整理したものです。 </td>
<td>重複を排除し、強力な証拠に置き換え、更新を追跡することが引き続き必要です。 </td>
<td>内容の真実を保証するラベルではありません。 </td>
</tr>
<tr>
<td><strong>ノイズ除外</strong></td>
<td>関係性が弱く、汚染が大きいと判断した段階で、現時点では使用しません。 </td>
<td>除外理由を残し、同種の混入を防ぐことが重要です。 </td>
<td>論文自体に価値がないわけではありませんが、このサイトの主旨とズレている可能性があります。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="when-to-return">
<h2 class="section-title">どこで停止して元のテキストに戻るか</h2>
<table class="data-table">
<thead>
<tr>
<th>今回の目的</th>
<th>ここに停めてもいいです</th>
<th>原文に戻る</th>
</tr>
</thead>
<tbody>
<tr>
<td>幅広い話題を取り上げたい</td>
<td>バッジ、まとめ、5点配置で興味があるかわかると。 </td>
<td>論文を引用して強い主張を裏付けたいとき。 </td>
</tr>
<tr>
<td>source_logged アイテムの確認</td>
<td>自分がまだ入り口の段階にあると理解したとき。 </td>
<td>一次研究を進められるか、Uナンバーに入るかを判断したい場合。 </td>
</tr>
<tr>
<td>レビューやメディアを見る</td>
<td>問題と関連キーワードのマップがある場合。 </td>
<td>評価や方法、数値を証拠として使いたいときに。 </td>
</tr>
<tr>
<td>Scopus と arXiv</td> のドキュメントの比較
<td>どの入り口から受け取ったかわかるとき。 </td>
<td>査読状況、実験条件、限界、追試の可能性などを確認したい場合。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある間違い</h2>
<div class="key-points">
<h4>誤読</h4>
<ul>
<li><strong>「スコーパスは強い」：</strong> スコーパスは指標です。テキストとメソッドを確認して、問題にどのように適用されるかを確認してください。 </li>
<li><strong>「arXivだから弱い」:</strong> 査読の前にも重要な入り口があります。内容が弱いかどうかを確認してください。 </li>
<li><strong>「レビューで十分」:</strong> レビュー記事は地図として役立ちますが、直接的な証拠を得るには一次研究に戻る必要があります。 </li>
<li><strong>「Source_logged, so accepted」:</strong> これはまだ受け入れログであり、統合または除外の決定はフォローアップ作業です。 </li>
<li><strong>「真実であるように厳選」:</strong> 整理されていることと、最終的に正しいことは別のことです。 </li>
<li><strong>「隠された状態を解決した人間の代理用紙」:</strong> 人間の PET/MRS/MRI の進歩により、完全な状態完全な読み出しではなく、可観測性クラスが引き上げられることがよくあります。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
論文を幅広く見たい場合は<a href="../mind_uploading_papers.html">論文集</a>、未解決の問題との対応を見たい場合は<a href="../research_harvest_50.html">文献マップ</a>、役割の違いから整理したい場合は<a href="literature-and-evidence-reading.html">文献・証拠の読み方</a>へ戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="literature-and-evidence-reading.html">文献・エビデンスページの見方→</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方→</a></li>
<li><a href="u-number-guide.html">U番号案内→</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../mind_uploading_papers.html">論文集→</a></li>
<li><a href="../research_harvest_50.html">書誌マップ→</a></li>
<li><a href="../verification.html#casework">ケースワーク→</a></li>
</ul>
</div>
</aside>
</main>
