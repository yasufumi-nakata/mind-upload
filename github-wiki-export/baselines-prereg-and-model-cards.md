# Wiki：ベースライン・事前登録・モデルカード

> 『何を比べ、どう固定し、何を残すか』を分けて考える
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-16 / 位置づけ: Learning guide

## このページの役割
このページは、Mind-Upload で繰り返し出てくる『ベースライン』『ベンチマーク』『事前登録』『モデルカード』『失敗例』の役割差を、初歩から整理する wiki です。高いスコアを出すことと、比較可能な前進を作ることの違いを理解する足場として使います。

## 正確さの前提
ここでは運用上の役割差を分かりやすく説明します。実際のテンプレートや仕様は公開ページ側で確認してください。

## 公開ページへ戻る
- [検証基盤](https://mind-upload.com/verification.html)
- [ハンズオン](https://mind-upload.com/datasets.html#l0-practice)
- [ケースワーク](https://mind-upload.com/verification.html#casework)

## 関連 Wiki
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - まず Verification Commons の全体像へ戻れます。
- [Wiki: データ分割とリーク](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - ベンチマーク運用で特に危険なリークを補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の基礎ページへ戻れます。

## いま分かっていること
- 比較可能な前進には、出発点、採点基準、事前ルール、結果の記録が必要です。
- ベースラインなしでは、改善を主張しにくくなります。
- 事前登録やモデルカードがないと、あとから都合よく解釈しやすくなります。

## まだ分かっていないこと
- どのテンプレートを WBE 全体で標準化するかは、まだ運用設計の途中です。
- どこまでの失敗例やネガティブ結果を必須公開にするかは今後の整備対象です。

---

<h2>いちばん短い地図</h2>
<p>
ベースラインは「出発点」、ベンチマークは「採点基準」、事前登録は「やる前の約束」、モデルカードは「結果の成績表」、失敗例は「どこで崩れたかの記録」です。どれか 1 つだけでは、比較可能な前進になりません。
</p>

<strong>2026-03 追補</strong>
<p>
L1 以上の結果では、通常のモデルカードに加えて <a href="https://mind-upload.com/verification.html#observability-budget">Observability Budget</a> を添付し、measurement stack、直接観測量、残る latent state、claim ceiling、abstention 条件を明示する運用にそろえました。さらに <strong>確率・区間・予測集合・棄権</strong> を出す結果では <a href="https://mind-upload.com/verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> を添付し、fit / calibration / test 分離、evaluation family、coverage-risk、fallback policy を固定します。multimodal / atlas prior 結果では <a href="https://mind-upload.com/verification.html#fusion-card">Fusion Card</a> を添付し、取得関係、時計系、登録誤差、融合モデル、single-modality baseline との差分、外部妥当化を同時に残します。加えて因果・閉ループ結果では <a href="https://mind-upload.com/verification.html#intervention-card">Intervention Card</a> を添付し、trigger rule、timing audit、control / sham、安全停止、再較正負荷を固定します。
</p>

<strong>foundation / self-supervised EEG model の追補</strong>
<p>
EEG foundation model を使う結果では、通常の model card だけでは比較可能性が足りません。pretraining corpus も dataset である以上、<strong>corpus identity</strong>、<strong>overlap audit</strong>、<strong>channel / reference / sampling の harmonization</strong>、<strong>adaptation regime</strong>、<strong>evaluation family</strong> を別紙で残す必要があります。本サイトではこれを <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-foundation-models#pretraining-card">Pretraining Card</a> と呼びます。
</p>

<strong>confidence / 区間 / 棄権の追補</strong>
<p>
confidence や posterior を付けた結果、prediction set を返す結果、low-confidence 時に abstain する結果も、通常の model card だけでは比較可能性が足りません。fit / calibration / test を分けずに threshold を調整すると、出力の意味そのものが崩れるためです。本サイトではこれを <a href="https://mind-upload.com/verification.html#calibration-abstention-card">Calibration &amp; Abstention Card</a> で管理し、詳しい読み方は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention">Wiki: 不確実性・校正・棄権</a> にまとめています。
</p>

<h2>まず役割を分ける</h2>
<table>
<thead>
<tr>
<th>用語</th>
<th>役割</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースライン</strong></td>
<td>最低限の比較相手です。改善を言うための出発点になります。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>何を、どのデータで、どの指標で比べるかを固定します。</td>
</tr>
<tr>
<td><strong>事前登録</strong></td>
<td>やる前に、指標、停止条件、分析方針を固定します。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>点数、弱点、リーク対策、失敗例、計算条件、さらに L1 以上では Observability Budget、確率・区間・予測集合・棄権を出す結果では Calibration &amp; Abstention Card、multimodal / atlas prior 結果では Fusion Card、foundation / self-supervised EEG 結果では Pretraining Card、因果・閉ループ結果では Intervention Card を残します。</td>
</tr>
<tr>
<td><strong>失敗例・ネガティブ結果</strong></td>
<td>何が効かなかったか、どこで崩れたかを残します。</td>
</tr>
</tbody>
</table>

<h2>なぜ全部必要なのか</h2>
<table>
<thead>
<tr>
<th>欠けるもの</th>
<th>起こりやすい問題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースラインがない</strong></td>
<td>数字が良いのか悪いのか、改善なのか偶然なのか判断しにくくなります。</td>
</tr>
<tr>
<td><strong>ベンチマークがない</strong></td>
<td>人ごとに違う採点をしてしまい、比較が壊れます。</td>
</tr>
<tr>
<td><strong>事前登録がない</strong></td>
<td>あとから都合のよい条件だけを選びやすくなります。</td>
</tr>
<tr>
<td><strong>モデルカードがない</strong></td>
<td>点数だけが残り、弱点や再現手順が見えなくなります。</td>
</tr>
<tr>
<td><strong>失敗例がない</strong></td>
<td>どこで崩れるかが共有されず、同じ失敗を繰り返しやすくなります。</td>
</tr>
</tbody>
</table>

<h2>最小の流れで見る</h2>

01

<h4>ベースラインを置く</h4>
<p>まず単純でもよいので、比較の出発点を 1 本置きます。</p>

02

<h4>ベンチマークを固定する</h4>
<p>データ、分割、指標、禁止事項をそろえます。</p>

03

<h4>事前登録する</h4>
<p>どの条件で成功・失敗とみなすかを先に決めます。</p>

04

<h4>モデルカードと失敗例を残す</h4>
<p>点数だけでなく、弱点と崩れ方まで公開します。</p>

<h2>因果・閉ループ結果で追加するもの</h2>
<p>
同じ `closed-loop` や `adaptive` という言葉でも、中身は大きく違います。したがって本サイトでは、因果・閉ループ結果を通常の model card だけで受理しません。<a href="https://mind-upload.com/verification.html#intervention-card">Verification の Intervention Card</a> を追加し、<strong>何を変えたか</strong>、<strong>どの state estimate / trigger で変えたか</strong>、<strong>どの comparator と timing で比べたか</strong>、<strong>どれだけ再較正を要したか</strong>まで残します。
</p>

<h4>Intervention Card で固定すること</h4>
<ul>
<li><strong>target / comparator：</strong>刺激部位、アクチュエータ、continuous・sham・fixed decoder などの比較条件。</li>
<li><strong>trigger / timing：</strong>biomarker、threshold、latency、jitter、update cadence、clock domain。</li>
<li><strong>artifact / safety：</strong>artifact window、masking、除外試行、安全停止、manual override。</li>
<li><strong>stability / recovery：</strong>dropout、abstention、recalibration burden、fixed decoder interval、recovery time。</li>
</ul>

<h2>確率や棄権を出す結果で追加するもの</h2>
<p>
同じ `confidence` や `posterior` という語でも、fit split と calibration split を分けたか、within-session なのか cross-day なのか、prediction set を返したのか low-confidence 時に abstain したのかで意味が変わります。したがって本サイトでは、確率・区間・予測集合・棄権を前面に出す結果を通常の model card だけで受理しません。<a href="https://mind-upload.com/verification.html#calibration-abstention-card">Verification の Calibration &amp; Abstention Card</a> を追加し、<strong>出力の型</strong>、<strong>fit / calibration / test の分離</strong>、<strong>evaluation family</strong>、<strong>coverage-risk</strong>、<strong>fallback policy</strong> まで残します。
</p>

<h4>Calibration &amp; Abstention Card で固定すること</h4>
<ul>
<li><strong>uncertainty target：</strong>class probability、interval、prediction set、abstention flag のどれを出したか。</li>
<li><strong>split / slice：</strong>fit / calibration / test の分離、within-session / cross-session / cross-subject / temporal のどれで評価したか。</li>
<li><strong>metrics / validity：</strong>ECE、Brier、NLL、empirical coverage、set size、coverage-risk、false alarm ceiling。</li>
<li><strong>fallback / recalibration：</strong>re-measure、manual review、silence / freeze、recalibration trigger。</li>
</ul>

<h2>失敗例はなぜ大事か</h2>
<p>
成功例だけ集めると、たまたま勝った条件だけが残ります。Mind-Upload のように主張が大きい分野では、<strong>どの条件で崩れたか</strong>を残すことが、成功例を残すのと同じくらい重要です。
</p>

<strong>失敗例に最低限ほしいもの</strong>
<p>
どの条件で、どの指標が、どれだけ崩れたか。リークや分割の問題だったのか、OOD で崩れたのか、計算資源が足りなかったのか、を切り分けて残す必要があります。
</p>

<h2>公開ページを読むときの最低チェック</h2>

<h4>Checklist</h4>
<ul>
<li><strong>ベースラインがあるか：</strong>何と比べたのかが明示されているか。</li>
<li><strong>ベンチマークが固定されているか：</strong>データ、分割、指標が書かれているか。</li>
<li><strong>事前登録があるか：</strong>あとから条件を変えていないか。</li>
<li><strong>モデルカードや失敗例があるか：</strong>弱点や崩れ方に加え、L1 以上では Observability Budget、確率・区間・予測集合・棄権を出す結果では Calibration &amp; Abstention Card、multimodal / atlas prior 結果では Fusion Card、foundation / self-supervised EEG 結果では Pretraining Card、因果・閉ループ結果では Intervention Card が見えるか。</li>
</ul>

<h2>次にどこへ戻るか</h2>
<p>
設計図へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、実務へ戻るなら <a href="https://mind-upload.com/datasets.html#l0-practice">ハンズオン</a>、他分野の先例へ戻るなら <a href="https://mind-upload.com/verification.html#casework">ケースワーク</a> をご利用ください。
</p>
