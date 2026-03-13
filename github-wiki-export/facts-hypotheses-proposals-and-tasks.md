# Wiki：事実・仮説・提案・実行タスクの違い

> ページの役割差を、事実・仮説・提案・タスクで整理する
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Reading roles of claims

## このページの役割
このページは、Mind-Upload の各ページが『同じ種類の主張』ではないことを整理する補助ガイドです。観察や文献整理、理論的な作業仮説、提案、今このリポジトリで実行するタスク、外部依存の調整は、役割も証拠の重さも違います。その違いをそろえて読むために使います。

## 正確さの前提
ここで扱うのはページの役割差です。個別の理論や提案の妥当性は、必ず各ページ本文と根拠へ戻って確認してください。

## 公開ページへ戻る
- [研究ノート](https://mind-upload.com/perspective.html)
- [理論フレーム](https://mind-upload.com/perspective.html#design-principles)
- [技術提案](https://mind-upload.com/issue.html#proposal-integration)

## 関連 Wiki
- [Wiki: 公開ページの読み分けガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - ページ全体の役割差を先に見たい人向けです。
- [Wiki: 提案と状態ラベルの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading) - 提案ページの状態ラベルをさらに詳しく見たい人向けです。
- [Wiki: はじめての Issue の書き方](https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics) - 実行タスクへ落とす書き方を補います。

## いま分かっていること
- 各ページは、観察、理論仮説、提案、実装タスク、外部依存で役割分担されています。
- 提案受理や文書反映は、実装完了や外部合意完了を自動では意味しません。
- 実行可能な変更は、Issue や Hands-on に落ちて初めて具体的に動きます。

## まだ分かっていないこと
- どの仮説や提案が最終的に中心線として残るかは、今後の検証で変わります。
- 外部依存の話がどこまで実際の連携へ進むかは、相手先や条件に依存します。

---

<h2>同じ「主張」に見えても、役割は同じではありません</h2>
<p>
文献整理、理論ノート、設計原理、技術提案、Issue、協業候補は、全部が同じ種類の文章ではありません。まず <strong>何を記録しているページか</strong> を分けると、断言の強さと次の行動を読み違えにくくなります。
</p>

<h2>まず 5 種類に分ける</h2>
<table>
<thead>
<tr>
<th>種類</th>
<th>何をしているか</th>
<th>主なページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察 / 整理</strong></td>
<td>何が知られていて、どこが未解決かを記録します。</td>
<td><a href="https://mind-upload.com/research_harvest_50.html">Research Harvest</a> / <a href="https://mind-upload.com/mind_uploading_papers.html">Papers</a> / <a href="https://mind-upload.com/verification.html#casework">Casework</a></td>
</tr>
<tr>
<td><strong>仮説 / 理論フレーム</strong></td>
<td>どう考えると設計条件へ落としやすいかを示します。</td>
<td><a href="https://mind-upload.com/perspective.html">Perspective</a> / <a href="https://mind-upload.com/perspective.html#design-principles">Idea</a></td>
</tr>
<tr>
<td><strong>提案 / 方針</strong></td>
<td>どの方向で進めるか、どのストリームで整理するかを示します。</td>
<td><a href="https://mind-upload.com/issue.html#proposal-integration">Proposals</a></td>
</tr>
<tr>
<td><strong>実行タスク</strong></td>
<td>今このリポジトリで直す変更、完了条件、反証条件を切ります。</td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> / <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a></td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td>共同研究、標準化、IRB、機材、法務など、外部条件が必要な作業を整理します。</td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">Collaborations</a></td>
</tr>
</tbody>
</table>

<h2>似て見えるページの違い</h2>
<table>
<thead>
<tr>
<th>ページ</th>
<th>主な役割</th>
<th>誤読しやすい点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Perspective</strong></td>
<td>文献と限界を並べて、理論の支持点と弱点を追う研究ノートです。</td>
<td>長文でも、最終確定理論の宣言ではありません。</td>
</tr>
<tr>
<td><strong>Idea</strong></td>
<td>採用する設計原理や作業仮説を絞って示す理論フレームです。</td>
<td>立場の整理であり、実験的に証明済みという意味ではありません。</td>
</tr>
<tr>
<td><strong>Proposals</strong></td>
<td>提案の状態、ストリーム、根拠節を追う整理表です。</td>
<td>提案受理は、コード実装や共同研究成立を意味しません。</td>
</tr>
<tr>
<td><strong>Issue</strong></td>
<td>今この場で実行する変更を、完了条件つきで管理する入口です。</td>
<td>大きな理論や外部依存まで同じ箱で扱うと混乱します。</td>
</tr>
<tr>
<td><strong>Collaborations</strong></td>
<td>外部依存の候補と、連携前に必要な準備物を整理する実務ページです。</td>
<td>候補一覧であり、合意済みリストではありません。</td>
</tr>
</tbody>
</table>

<h2>どう移ると自然か</h2>
<table>
<thead>
<tr>
<th>いまいる場所</th>
<th>次に移る自然な先</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察 / 整理</strong></td>
<td><a href="https://mind-upload.com/perspective.html">Perspective</a> / <a href="https://mind-upload.com/issue.html#proposal-integration">Proposals</a></td>
<td>文献整理の次に、どう読むか、どの方針へ使うかを決めるためです。</td>
</tr>
<tr>
<td><strong>仮説 / 理論フレーム</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a></td>
<td>仮説を、そのまま設計条件や検証条件へ落とす必要があるためです。</td>
</tr>
<tr>
<td><strong>提案 / 方針</strong></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> / <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a></td>
<td>提案を実際の変更や最小ループへ落とし込むためです。</td>
</tr>
<tr>
<td><strong>実行タスク</strong></td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a> / <a href="https://mind-upload.com/verification.html">Verification</a></td>
<td>置き場所や完了条件を再確認しながら進めるためです。</td>
</tr>
<tr>
<td><strong>外部依存タスク</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">内製で先にやることと外部依存</a></td>
<td>まず内製できる準備物へ分解する必要があるためです。</td>
</tr>
</tbody>
</table>

<h2>よくある混同</h2>

<h4>Mistake</h4>
<ul>
<li><strong>理論フレームを事実一覧として読む：</strong> Idea は作業仮説を含みます。</li>
<li><strong>提案ページを実装完了と読む：</strong> Proposals は整理表であり、完了報告ではありません。</li>
<li><strong>Issue を大きな構想メモにする：</strong> 今このリポジトリで切れる変更へ落とす方が安全です。</li>
<li><strong>Collaborations を TODO 一覧と読む：</strong> 外部依存の候補と準備物の整理であり、即実行リストではありません。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
公開ページ全体の役割差へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide">公開ページの読み分けガイド</a>、提案ページの状態へ戻るなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading">提案と状態ラベルの読み方</a>、実行タスクへ落とし込むなら <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/issue-writing-basics">はじめての Issue の書き方</a> をご利用ください。
</p>
