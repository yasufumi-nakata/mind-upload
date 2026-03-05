# Wiki：提案と状態ラベルの読み方

> 『採用された』と『終わった』は別です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Reading guide

## このページの役割
このページは、Mind-Upload の提案ページや Issue ページに出てくる状態ラベルを読み違えないための補助ページです。提案が受理されたことと、実装や外部合意まで終わったことは別なので、その差を日常語で整理します。

## 正確さの前提
ここでの説明は読み方の補助です。個別提案の最新状態は、必ず提案ページと Issue 履歴へ戻って確認してください。

## 公開ページへ戻る
- [技術提案](https://mind-upload.com/proposals.html)
- [貢献ガイド](https://mind-upload.com/issue.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: 文献と証拠ページの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - 提案ページが、文献系ページとどう違うかを補います。
- [Wiki: 内製で先にやることと外部依存](https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies) - 外部依存を、今できる準備作業まで分解して読みたい人向けです。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜ達成条件と反証条件を先に置くのかを確認できます。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- 提案受理や文書反映は、コードや共同研究の完了を自動的には意味しません。
- 外部依存タスクは、こちら側の準備と相手側の合意を分けて読む必要があります。
- 状態ラベルは、実装や公開の位置を示すもので、科学的確定そのものではありません。

## まだ分かっていないこと
- 各提案が最終的にどこまで実装されるかは、今後の進行で変わり得ます。
- 外部依存タスクの完了時期や条件は、ラベルだけでは保証できません。

---

<div class="abstract-box">
<h2>まず区別したいこと</h2>
<p>
提案ページでは、「良い案として採った」「本文へ書いた」「コードまで動いた」「外部合意まで終わった」が別の段階です。この差を曖昧にすると、進んでいる作業とまだ保留の作業を混同してしまいます。
</p>
</div>

<section class="section" id="labels">
<h2 class="section-title">状態ラベルを日常語にする</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベルの種類</th>
<th>日常語で言うと</th>
<th>まだ残ること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>提案公開</strong></td>
<td>案として表に出ていて、議論できる状態です。</td>
<td>妥当性や優先順位の確認が残ります。</td>
</tr>
<tr>
<td><strong>提案受理 / 方針反映</strong></td>
<td>方向性としては採る価値が高いと判断した状態です。</td>
<td>実装方法、検証条件、公開物の整備が残ります。</td>
</tr>
<tr>
<td><strong>文書反映</strong></td>
<td>本文には書かれている状態です。</td>
<td>コード、データ、ログが揃っているとは限りません。</td>
</tr>
<tr>
<td><strong>実装済み</strong></td>
<td>実際に動くものがある状態です。</td>
<td>第三者追試や監査が別途必要なことがあります。</td>
</tr>
<tr>
<td><strong>外部依存</strong></td>
<td>こちらだけでは完了できず、相手先や制度が必要な状態です。</td>
<td>合意、契約、実験、資金などが残ります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-not-mean">
<h2 class="section-title">ラベルが意味しないこと</h2>
<div class="key-points">
<h4>Not Mean</h4>
<ul>
<li><strong>提案受理：</strong> 科学的に完全に正しいと確定した、という意味ではありません。</li>
<li><strong>文書反映：</strong> 実装や共同研究まで終わった、という意味ではありません。</li>
<li><strong>実装済み：</strong> 社会実装や制度整備まで済んだ、という意味ではありません。</li>
</ul>
</div>
</section>

<section class="section" id="where-to-return">
<h2 class="section-title">どこへ戻るべきか</h2>
<table class="data-table">
<thead>
<tr>
<th>知りたいこと</th>
<th>戻るページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>提案の中身と根拠</td>
<td><a href="https://mind-upload.com/proposals.html">技術提案</a></td>
</tr>
<tr>
<td>いま誰が何を手伝えるか</td>
<td><a href="https://mind-upload.com/issue.html">貢献ガイド</a></td>
</tr>
<tr>
<td>達成条件や反証条件の前提</td>
<td><a href="https://mind-upload.com/verification.html">検証基盤</a></td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>外部依存を『待ち箱』にしないために</strong>
<p>
このページは段階差の説明です。外部依存になったあとに、こちらで何を先に作れるかまで整理したい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">Wiki: 内製で先にやることと外部依存の切り分け</a> をご覧ください。
</p>
</div>
