# Wiki: 文献と証拠のページの読み方

> 「多数の論文」と「強力な結論」を混同しないでください
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-03-26 / Role: 読書ガイド

## このページの役割
このページは、Mind-Upload 上の文献ページの役割を整理した補助ページです。 1ページに論文が多くなればなるほど、その役割が混同されると読みづらくなるため、本書ではまず「`what the page does'' and `をどの程度まで確定的なものとして扱ってはいけないのか」を説明する。

## 正確性に関する注記
このページは読書補助です。個々の論文や個々の提案の評価については、必ず元のページや元の論文に戻ってご確認ください。

## 公開ページへ戻る
- [文学地図](https://mind-upload.com/research_harvest_50.html)
- [論文集](https://mind-upload.com/mind_uploading_papers.html)
- [技術提案](https://mind-upload.com/issue.html#proposal-integration)

## 関連 Wiki ページ
- [Wiki: ソースタイプ、ステータスラベル、および証拠クラス](https://github.com/yasufumi-nakata/mind-upload/wiki/paper-source-types-and-evidence-status) - Scopus、arXiv、Review、Media、source_logged、およびevidenceクラスの意味を整理します。
- [Wiki: 検証インフラストラクチャの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 証拠の強さと何を探すべきかについての仮定を補ってください。
- [Wiki: WBE の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - それぞれの論文や提案は全体的な問題に対応しています。
- [ウィキホーム](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基本ページに戻ることができます。

## 現在わかっていること
- 役割の異なるページを分けることで、ボリュームと結論の強さを混同しにくくなります。
- 論文集、書誌マップ、企画書のページを読む目的は異なります。
- 重要な決定は、要約ではなく、元の論文やページに戻って行う必要があります。
- 人間による測定紙は、すでに解決されたものではなく、観察可能なものを変えることがよくあります。
- 同じ主題または複数のモードを持つ人間の論文は、依然として同じ状態の結果ではなく、代理構成の問題である可能性があります。

## まだわかっていないこと
- 最終的にどの論文が中心的な基盤として残るかは、将来変わる可能性があります。
- source_logged などの状態は、その後の精査によって更新される可能性があります。

---

<h2>まずは役割を分ける</h2>
<p>
すべての文献ページに同じ役割があるわけではありません。幅広くまとめたページ、未解決の課題ごとにまとめたページ、提案として統合したページに分けることで、読者が今何を見ているのかを見失いにくくしています。
</p>

<strong>文献を読んで次のページを決めたいとき</strong>
<p>
役割の違いだけでなく、論文や文献マップを読んだ後に未解決の問題、提案、課題、コラボレーション候補にどこに戻るかについて知りたい場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-to-action-route">文献から実装、参加までの直線的なパス</a>を参照してください。
</p>

<strong>テクノロジー・自然科学の一次証拠だけを追いたいとき</strong>
<p>
<a href="https://mind-upload.com/mind_uploading_papers.html">論文コレクション</a>は広範なアーカイブであるため、最初の時系列順は必ずしも技術フロンティアの順序と一致しません。デコード、音声人工神経、ESI直接検証、人間可観測性、保守状態などの技術ルートを先にご覧になりたい場合は、論文集の<strong>技術・自然科学優先ルート</strong>からお入りください。
</p>

<strong>新しい人間測定用紙を見たとき</strong>
<p>
まず、その論文が <strong>demo</strong>、<strong>direct validator</strong>、<strong>observability-class Advanced</strong>、または <strong>hidden-stateboundarypaper</strong> であるかどうかを尋ねます。この 1 つの質問は、一般的な科学的深読みをブロックします。<strong>「人間はより多くの測定を行ったので、隠れた状態はほぼ閉じられています。」</strong>
</p>

<strong>論文が生きた人間の全脳状態測定のように聞こえるとき</strong>
<p>
「同じ主題」、「マルチモーダル」、または「プロキシが豊富」で停止しないでください。次に、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition">Wiki: ヒューマン プロキシの構成とルートの成熟度</a> および <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/measurement-stack-and-claim-ceiling">Wiki: 測定スタックの可観測性と要求の上限</a> に戻ります。このサイトでは、実際的な質問はより狭くなります: <strong> 各行が直接観察したものは何ですか、どの共通ドライバーまたは血管/自律神経経路がそれと一緒に移動する可能性がありますか、そしてどの隠れ状態ファミリーがキャリブレーションの外に残っていますか? </strong>
</p>

<h2>3つのページの違い</h2>
<table>
<thead>
<tr>
<th>ページ</th>
<th>ロール</th>
<th>ここでできること</th>
<th>ここではしてはいけないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>論文集</strong></td>
<td>ワイドエントランス</td>
<td>年度ごとの流れ、関連論文の有無、抄録からの推測。技術分野の読者は、優先ルートを通じて主要な一次情報源を入力します。 </td>
<td>各紙の最終評価はここだけでご確認いただけます。 </td>
</tr>
<tr>
<td><strong>書誌マップ</strong></td>
<td>未解決の問題ごとの整理</td>
<td>U 番号ごとに何が解決され、何が未解決であるかを確認します。 </td>
<td>結論の強さは引用の数だけで決まります。 </td>
</tr>
<tr>
<td><strong>技術提案</strong></td>
<td>実装戦略の統合</td>
<td>どのような提案が存在し、どのような状態にあり、どのような影響を与えるかを追跡します。 </td>
<td> 提案の受諾は実装完了と読み替えてください。 </td>
</tr>
</tbody>
</table>

<h2>どのくらい深く読めばいいですか</h2>
<table>
<thead>
<tr>
<th>見ているもの</th>
<th>その場で止められる</th>
<th>原文に戻る</th>
</tr>
</thead>
<tbody>
<tr>
<td>論文カード</td>
<td>自分の主張が自分の主張からかけ離れていることに気づいたとき。 </td>
<td>手法や評価、限界などを証拠として使いたいとき。 </td>
</tr>
<tr>
<td>現在のUナンバーマップ</td>
<td>どの U が自分に関連しているかがわかったとき。 </td>
<td>文献が本当にそのUに使えるか確認したいとき。
</tr>
<tr>
<td>提案概要表</td>
<td>関連するストリームと状態がわかっている場合。 </td>
<td>合否や正当性を判断したいときに。 </td>
</tr>
</tbody>
</table>

<h2>Five rules to prevent misreading</h2>

<h4>Rule</h4>
<ul>
<li><strong>量と強さを混同しないでください:</strong> 論文や引用の数は、結論を確立することと同じではありません。 </li>
<li><strong>要約に止まらないでください:</strong>証拠として使用する場合は、必ず DOI または原文に戻ってください。 </li>
<li><strong>ステータスラベルを読み違えないでください:</strong>source_logged、提案承認、およびドキュメント反映はそれぞれ異なる意味を持っています。 </li>
<li><strong>可観測性を十分なものに崩壊させないでください:</strong> 新しい人間のプロキシまたはアトラスは、状態完全な測定を証明することなく、観測可能なものを引き上げることができます。</li>
<li><strong>プロキシリッチを状態クローズに折りたたまないでください:</strong> 同一被験者またはマルチモーダルな人間の行には、引き続きプロキシクラス、キャリブレーターロール、および共通ドライバーのチェックが必要です。</li>
</ul>

<strong>Scopus/arXiv/source_loggedの意味を先に確認したい場合</strong>
<p>
このページは役割の違いを説明する補足ページです。出版ソース、文書タイプ、サイトステータス、証拠クラスを 1 ページにまとめたい場合は、まず <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/paper-source-types-and-evidence-status">Wiki: ソースタイプ、ステータスラベル、および証拠クラスの読み方</a> を参照すると、論文コレクションと書誌マップの見た目が安定します。
</p>

<h2>次に戻る場所</h2>
<p>
幅広い論文を見たい場合は<a href="https://mind-upload.com/mind_uploading_papers.html">論文集</a>、未解決の問題から始めたい場合は<a href="https://mind-upload.com/research_harvest_50.html">文学地図</a>、提案や実施方針を追いたい場合は<a href="https://mind-upload.com/issue.html#proposal-integration">技術提案</a>へお戻りください。
</p>
<p>
その論文が、脳全体の状態測定に近い生きた人間の測定論文である場合は、「可観測性クラスの進歩」から「状態識別の証拠」まで頭の中で宣伝する前に、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/human-proxy-composition">Human Proxy Composition and Route Maturity</a> の次へ進んでください。
</p>
