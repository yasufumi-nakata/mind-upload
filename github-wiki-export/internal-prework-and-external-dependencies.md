# Wiki：内製で先にやることと外部依存の切り分け

> 『相手待ち』に見える作業を、準備作業まで分解する
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Operational guide

## このページの役割
このページは、Mind-Upload の運用で何度も出てくる『外部依存』を、止まる理由ではなく分解対象として読むための補助ページです。ここでの焦点は、今このリポジトリで先に作れるものと、相手先や制度が必要なものを分けることです。

## 正確さの前提
このページは作業の切り分けを助けるための補助です。実際の合意、契約、IRB、機材利用の成立は、このページだけでは保証できません。

## 公開ページへ戻る
- [貢献ガイド](https://mind-upload.com/issue.html)
- [協業候補](https://mind-upload.com/collaborations.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: 提案と状態ラベルの読み方](https://github.com/yasufumi-nakata/mind-upload/wiki/proposal-status-reading) - 提案、文書反映、外部依存などの段階差を先に整理します。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - なぜ要求仕様や判定条件を先に作るのかを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページへ戻れます。

## いま分かっていること
- 外部依存タスクでも、要求仕様、判定条件、公開ログ形式、比較表などは先に内製できます。
- 相手先へ声をかける前に、最小成果物と依頼内容を 1 ページに整理した方が前に進みやすいです。
- Issue でも共同研究でも、『何が今すぐ実行可能か』を明示することが重要です。

## まだ分かっていないこと
- どの外部候補が実際に合意するか、どの条件で動けるかは相手側要因に依存します。
- IRB、契約、資金、機材の確保時期は、このページの外側で決まります。

---

<div class="abstract-box">
<h2>まず分けたいこと</h2>
<p>
外部依存タスクとは、<strong>こちらだけでは完了できない</strong>作業です。ただし、それは<strong>こちらで何もできない</strong>という意味ではありません。依頼前の下準備、判定条件、公開ログ形式、比較表などは先に作れます。
</p>
</div>

<div class="note-box">
<strong>参加ページのあとに次の1ページを決めたいとき</strong>
<p>
Issue や Collaborations を読んだあとに、次は小さな修正、条件設計、文献からの作業化、L0 実装準備のどれへ進むべきかを 1 枚で見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/participation-next-routes">参加・協業ページのあとに進む5つの道</a> をご覧ください。
</p>
</div>

<section class="section" id="two-columns">
<h2 class="section-title">内製と外部依存を 2 列で読む</h2>
<table class="data-table">
<thead>
<tr>
<th>種類</th>
<th>今このリポジトリで進められること</th>
<th>外部依存になること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>実験</strong></td>
<td>要求仕様、評価指標、停止条件、公開ログ形式、事前登録ドラフトを作れます。</td>
<td>IRB、被験者募集、機材利用、実測データ取得は外部依存です。</td>
</tr>
<tr>
<td><strong>共同研究</strong></td>
<td>1ページ要約、最小成果物、依頼範囲、比較表、再解析計画を作れます。</td>
<td>共同著者合意、契約、相手先の承認、データ共有条件は外部依存です。</td>
</tr>
<tr>
<td><strong>標準化提案</strong></td>
<td>仕様ドラフト、差分表、サンプルログ、想定ユースケースを作れます。</td>
<td>コミュニティ採択、公式仕様反映、外部レビューは外部依存です。</td>
</tr>
<tr>
<td><strong>資金・制度</strong></td>
<td>目的、最小スコープ、成果物、必要予算の整理はできます。</td>
<td>採択、予算配分、法務判断、制度設計の正式決定は外部依存です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="prework-pack">
<h2 class="section-title">外部依存でも先に作りたい最小準備物</h2>
<table class="data-table">
<thead>
<tr>
<th>準備物</th>
<th>最低限の中身</th>
<th>なぜ必要か</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1ページ要約</strong></td>
<td>目的、相手にお願いしたいこと、こちらが既に持っているもの。</td>
<td>相手が「何の話か」を短時間で判断できるようにするためです。</td>
</tr>
<tr>
<td><strong>最小成果物</strong></td>
<td>今回の最小スコープを 1 つに絞った定義。</td>
<td>依頼が大きすぎると、最初の合意を作りにくいためです。</td>
</tr>
<tr>
<td><strong>判定条件</strong></td>
<td>何が出たら前進か、何が出たら保留か、何が出たら失敗か。</td>
<td>話が進んだ後で目標がずれるのを防ぐためです。</td>
</tr>
<tr>
<td><strong>公開可能な下準備</strong></td>
<td>仕様ドラフト、QC ログ例、比較表、BIDS 雛形、チェックリスト。</td>
<td>こちら側の本気度と具体性を示しやすいためです。</td>
</tr>
<tr>
<td><strong>外部依存の境界</strong></td>
<td>IRB、機材、契約、法務、相手承認など、誰の判断が要るか。</td>
<td>今すぐ進む作業と待ち作業を混同しないためです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="issue-vs-collab">
<h2 class="section-title">Issue と共同研究で少し違う点</h2>
<table class="data-table">
<thead>
<tr>
<th>場面</th>
<th>まず固定したいこと</th>
<th>そのあと外部依存になるもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Issue を立てるとき</strong></td>
<td>どこで止まったか、何が不足か、前進条件、反証条件。</td>
<td>実験や法務が必要なら、別トラックとして切り出します。</td>
</tr>
<tr>
<td><strong>共同研究候補を見るとき</strong></td>
<td>相手に頼みたい範囲と、こちらが先に出せる成果物。</td>
<td>合意、共同著者、データ利用条件、機材使用が残ります。</td>
</tr>
<tr>
<td><strong>標準化提案を出すとき</strong></td>
<td>差分表、サンプル、現行規格で足りない点。</td>
<td>コミュニティレビューと正式採択が残ります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">よくある混同</h2>
<div class="key-points">
<h4>Misread</h4>
<ul>
<li><strong>「外部依存だから今は何もしない」：</strong> 仕様、比較表、ログ形式、最小成果物は先に作れます。</li>
<li><strong>「文書に書いたから進んでいる」：</strong> 相手先へ渡す下準備と、実際の合意成立は別です。</li>
<li><strong>「大きい計画ほどよい」：</strong> 最初は最小スコープを切らないと、依頼も Issue も動きません。</li>
<li><strong>「外部依存を本文で完了扱いする」：</strong> ここは特に避けるべきで、証跡のある内製変更と分けて書きます。</li>
</ul>
</div>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
Issue の書き方へ戻る場合は <a href="https://mind-upload.com/issue.html">貢献ガイド</a>、共同研究候補を整理する場合は <a href="https://mind-upload.com/collaborations.html">協業候補</a>、要求仕様や判定条件の前提を固める場合は <a href="https://mind-upload.com/verification.html">検証基盤</a> に戻ってください。
</p>
</section>
