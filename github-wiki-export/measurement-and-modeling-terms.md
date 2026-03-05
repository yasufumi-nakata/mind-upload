# Wiki：計測からモデル化までの用語ガイド

> 言葉を点で覚えず、流れでつなぐ
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
このページは、EEG のような計測語、ESI や DCM のようなモデル語、BIDS や QC のような運用語を『観測→整理→推定→検証』の流れでつなげて理解するための wiki です。単語を個別に暗記するより、どの段階で使う言葉かを先に分けることを目的にします。

## 正確さの前提
ここで示す流れは理解のための整理です。実際の研究では往復や例外がありますが、観測と推定、推定と検証を混同しないことは崩しません。

## 公開ページへ戻る
- [用語集](https://mind-upload.com/glossary.html)
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [検証基盤](https://mind-upload.com/verification.html)

## 関連 Wiki
- [Wiki: EEGの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - 計測の入口として、EEG が何を測るかを確認できます。
- [Wiki: EEG前処理とQC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 整理段階で何が結果を変えるかを補います。
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 最後の検証段階で何を固定するかを補います。

## いま分かっていること
- 計測、前処理、推定、検証は役割が違い、それぞれ別の言葉が使われます。
- 観測信号はそのまま脳内状態ではなく、推定には不確実性が伴います。
- BIDS や QC はおまけではなく、比較可能性を支える要素です。

## まだ分かっていないこと
- 非侵襲計測だけで WBE に十分な内部状態をどこまで復元できるかは未解決です。
- どのモデル化の組み合わせが最終的に最も有効かは、まだ研究途中です。

---

<div class="abstract-box">
<h2>いちばん短い地図</h2>
<p>
このサイトで出る言葉は、大きく分けると 4 段階です。<strong>観測する</strong>、<strong>整える</strong>、<strong>推定する</strong>、<strong>確かめる</strong>、でございます。単語が難しく見えても、「今どの段階の話か」を先に分けると混乱が減ります。
</p>
</div>

<section class="section" id="four-steps">
<h2 class="section-title">4段階で見る</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>ここで出やすい言葉</th>
<th>何をしているか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 観測</strong></td>
<td>EEG, MEG, fMRI, ECoG</td>
<td>脳や身体から、まず外に出てくる信号を測ります。</td>
</tr>
<tr>
<td><strong>2. 整理</strong></td>
<td>QC, 前処理, BIDS</td>
<td>ノイズや欠損を確認し、他人が追える形へそろえます。</td>
</tr>
<tr>
<td><strong>3. 推定</strong></td>
<td>逆問題, ESI, DCM, SCM</td>
<td>観測から、脳内の状態や因果構造をどこまで推定できるか考えます。</td>
</tr>
<tr>
<td><strong>4. 検証</strong></td>
<td>ベンチマーク, ベースライン, 事前登録, モデルカード</td>
<td>その推定やモデルが、本当に比較可能な形で成り立つか確かめます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="observation">
<h2 class="section-title">1. 観測: まず信号を取る</h2>
<p>
EEG や MEG は、脳の中を直接見ているのではなく、外から観測できる信号を測っています。ここで大事なのは、<strong>観測したものと、脳内で本当に起きていることは同じではない</strong>という点です。
</p>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ひとことで言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>頭皮上の電位差を高速に測る方法です。時間変化に強い一方、空間的にはぼやけやすいです。</td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>磁場を測る方法です。EEG と補完関係がありますが、高価で装置制約が大きいです。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>血流変化を測る方法です。位置には強いですが、時間分解能は遅いです。</td>
</tr>
<tr>
<td><strong>ECoG</strong></td>
<td>脳表面に近い場所で測る侵襲計測です。高精度ですが、適用範囲に強い制約があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="cleanup">
<h2 class="section-title">2. 整理: 信号をそのまま信じない</h2>
<p>
観測した信号には、まばたき、筋電、体動、機器ノイズなどが混ざります。そのため、次に必要なのが QC と前処理です。ここは見栄えを整える作業ではなく、<strong>どの情報を残し、何を除いたかを記録する作業</strong>です。
</p>
<div class="key-points">
<h4>ここで出る言葉</h4>
<ul>
<li><strong>QC：</strong>欠損、ノイズ、アーティファクト、除外理由を数値で残します。</li>
<li><strong>前処理：</strong>参照法、フィルタ、アーティファクト除去などを設定します。</li>
<li><strong>BIDS：</strong>データとメタデータを他人が追える形でそろえる規格です。</li>
</ul>
</div>
<p>
この段階を飛ばすと、あとで高性能なモデルが出てきても、比較可能な証拠にはなりません。
</p>
</section>

<section class="section" id="estimation">
<h2 class="section-title">3. 推定: 観測から中身をどこまで言えるか</h2>
<p>
整理した信号をもとに、脳内の活動や因果構造を推定したくなります。ここで出てくるのが、逆問題、ESI、DCM、SCM です。ただし、この段階では<strong>推定は推定であり、不確実性が残る</strong>ことを忘れてはいけません。
</p>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>役割</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>逆問題</strong></td>
<td>外から見えた信号から、中の原因を推定する問題です。一般に 1 つに決まりません。</td>
</tr>
<tr>
<td><strong>ESI</strong></td>
<td>EEG から脳内ソースを推定する枠組みです。点推定だけでなく、不確実性も報告する必要があります。</td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>神経回路の結合や動き方を仮定し、どの結合が観測を説明しやすいかを推定します。</td>
</tr>
<tr>
<td><strong>SCM</strong></td>
<td>因果関係を明示して、介入や反事実を扱いやすくするモデルです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>ここで起きやすいすり替え</strong>
<p>
EEG を観測したことと、脳内状態を一意に再構成したことは同じではありません。さらに、相関的な予測が当たることと、因果構造まで分かったことも同じではありません。
</p>
</div>
</section>

<section class="section" id="verification">
<h2 class="section-title">4. 検証: 推定をどう信用するか</h2>
<p>
最後に必要なのは、「この推定やモデルを、他の人が同じ条件で確かめられるか」です。ここで Benchmark、Baseline、Preregistration、Model Card のような言葉が出てきます。
</p>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>何のために要るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>何を比べるか、どの指標で採点するかを固定します。</td>
</tr>
<tr>
<td><strong>ベースライン</strong></td>
<td>改善を主張するための出発点を置きます。</td>
</tr>
<tr>
<td><strong>事前登録</strong></td>
<td>あとから都合よく条件を変えないようにします。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>スコアだけでなく、弱点、失敗例、リーク対策、計算条件も公開します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="boundary">
<h2 class="section-title">この流れで何が分かり、何がまだ分からないか</h2>
<table class="data-table">
<thead>
<tr>
<th>分かること</th>
<th>まだ分からないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>用語が、どの段階の仕事に属するか。</td>
<td>どのモデルが最終的に意識や本人性を十分に説明するか。</td>
</tr>
<tr>
<td>観測、推定、検証を混同しない読み方。</td>
<td>非侵襲計測だけで WBE に十分な情報を取れるかどうか。</td>
</tr>
<tr>
<td>BIDS や QC がなぜ技術の外側ではなく中身なのか。</td>
<td>どのマルチモーダル統合が最終的に最良か。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
短い定義へ戻るなら <a href="https://mind-upload.com/glossary.html">用語集</a>、EEG の役割をもう一度読むなら <a href="https://mind-upload.com/eeg_101.html">EEG入門</a>、比較可能な検証へ進むなら <a href="https://mind-upload.com/verification.html">検証基盤</a> をご利用ください。
</p>
</section>
