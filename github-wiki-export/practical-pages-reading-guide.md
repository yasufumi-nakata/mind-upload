# Wiki：実務系ページの読み分けガイド

> 勝利条件、入口データ、作業手順、参照事例、提案整理を混ぜないための地図
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Reading guide

## このページの役割
このページは、Mind-Upload の実務寄り公開ページを読み分けるための補助ガイドです。Verification は勝利条件、Datasets は入口データ、Datasets内のL0実践節は最小ループ手順、Verification内のケースワーク節は参照事例、Issue内の提案統合節は提案整理であり、似て見えても役目が違います。

## 正確さの前提
ここで扱うのはページの役割差です。実際の検証条件や手順の細部は、各本文ページで確認してください。

## 公開ページへ戻る
- [検証基盤](https://mind-upload.com/verification.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [L0実践](https://mind-upload.com/datasets.html#l0-practice)

## 関連 Wiki
- [Wiki: 公開ページの読み分けガイド](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - 公開ページ全体の役割差を見たい人向けです。
- [Wiki: L0で最低限そろえる成果物パック](https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack) - L0実践節の提出物を 1 枚で確認したい人向けです。
- [Wiki: 規格・置き場・Validator・ベンチマーク](https://github.com/yasufumi-nakata/mind-upload/wiki/standards-repositories-validators-and-benchmarks) - Verification内のケースワーク節や Verification で出る運用語の違いを補います。
- [Wiki: ベースライン・事前登録・モデルカード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - 実務ページで何を残すべきかを役割ごとに整理します。

## いま分かっていること
- Verification、Datasets、Datasets内のL0実践節、Verification内のケースワーク節、Issue内の提案統合節 は、どれも実務寄りですが役割が違います。
- Verification は前進の定義、Datasets は入口選定、Datasets内のL0実践節は手順、Verification内のケースワーク節は設計参照、Issue内の提案統合節は提案整理です。
- ページの役割差を先に分けると、実務導線を読み違えにくくなります。

## まだ分かっていないこと
- どの実務ルートが将来の L2 や L3 に最も効くかは、まだ固定していません。
- 将来どの実務ページを独立拡張するかは、運用の蓄積に応じて変わります。

---

<h2>まず5つに分ける</h2>
<p>
実務系ページは、全部が「作業に役立つページ」ではありますが、<strong>何を決めるページか</strong>が違います。先に <strong>勝利条件</strong>、<strong>入口データ</strong>、<strong>作業手順</strong>、<strong>参照事例</strong>、<strong>提案整理</strong> に分けると、実務導線がかなり安定します。
</p>

<strong>EEGからL0までの順番だけを一本道で見たいとき</strong>
<p>
実務ページの役割差よりも、EEG 入門から Datasets、L0実践節、Verification までの順番をそのまま辿りたい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">EEGからL0までの一本道</a> をご覧ください。
</p>

<strong>Verificationのあとに何を見るかだけ決めたいとき</strong>
<p>
実務ページの役割差を理解したあとで、Verification から次にどの路線へ進むかだけを 1 枚で見たい場合は <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Verificationのあとに進む4つの道</a> をご覧ください。
</p>

<h2>実務系ページの役割差</h2>
<table>
<thead>
<tr>
<th>ページ</th>
<th>主な役割</th>
<th>最初に向く疑問</th>
<th>ここだけでは足りないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><a href="https://mind-upload.com/verification.html">Verification</a></strong></td>
<td>勝利条件と反証条件を決める設計図です。</td>
<td>「何を満たしたら前進か」を先に固定したいときです。</td>
<td>実際の入口データや作業手順は、Datasets や L0実践節 で補う必要があります。</td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/datasets.html">Datasets</a></strong></td>
<td>入口データを選ぶページです。</td>
<td>最初にどの公開データで L0 を始めるかを決めたいときです。</td>
<td>何を成果物として残すかは、L0実践節 や Verification で補う必要があります。</td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/datasets.html#l0-practice">L0実践節</a></strong></td>
<td>最小ループを作る手順書です。</td>
<td>今この場で再現可能な解析を一周つなぎたいときです。</td>
<td>その手順がなぜ必要かという設計理由は、Verification で補う必要があります。</td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/verification.html#casework">ケースワーク節</a></strong></td>
<td>他分野の成功事例から設計の型を学ぶ参照集です。</td>
<td>標準、置き場、ベンチ、事前登録がなぜ効いたのかを実例で見たいときです。</td>
<td>この事例だけで WBE の成立を示すことはできません。</td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/issue.html#proposal-integration">提案統合節</a></strong></td>
<td>提案群の状態と根拠をまとめる整理表です。</td>
<td>どの提案が何を目指し、どこまで反映されたかを追いたいときです。</td>
<td>要約だけで実装完了とは言えず、Issue や原文へ戻る必要があります。</td>
</tr>
</tbody>
</table>

<h2>この疑問なら、まずこのページ</h2>
<table>
<thead>
<tr>
<th>いま知りたいこと</th>
<th>まず開くページ</th>
<th>次に行くページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>何を満たせば前進と呼べるか知りたい</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a> で依存関係を見ます。</td>
</tr>
<tr>
<td>最初にどの公開データを使うか決めたい</td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">L0実践節</a> で L0 の作業へ進みます。</td>
</tr>
<tr>
<td>実際に何を一式として残すか知りたい</td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">L0実践節</a></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> と <a href="https://mind-upload.com/datasets.html">Datasets</a> を補います。</td>
</tr>
<tr>
<td>なぜ標準やベンチが必要かを歴史事例で見たい</td>
<td><a href="https://mind-upload.com/verification.html#casework">ケースワーク節</a></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> に戻って現在設計と照合します。</td>
</tr>
<tr>
<td>提案済みと実装済みを区別して追いたい</td>
<td><a href="https://mind-upload.com/issue.html#proposal-integration">提案統合節</a></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> と原文節へ戻ります。</td>
</tr>
<tr>
<td>どこへ追記・更新するかを決めたい</td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> で実行可能な作業へ落とします。</td>
</tr>
</tbody>
</table>

<h2>似て見えるページの違い</h2>
<table>
<thead>
<tr>
<th>似て見える組</th>
<th>違いを一言で言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Verification / L0実践節</strong></td>
<td>Verification は合格条件、L0実践節 は最小ループの作業順です。</td>
</tr>
<tr>
<td><strong>Datasets / L0実践節</strong></td>
<td>Datasets は何で始めるか、L0実践節 はどう一周させるかです。</td>
</tr>
<tr>
<td><strong>Verification / ケースワーク節</strong></td>
<td>Verification は現在の設計、ケースワーク節 は他分野から借りる型です。</td>
</tr>
<tr>
<td><strong>提案統合節 / Issue</strong></td>
<td>提案統合節 は提案の本文整理、Issue は今この場で切る作業と外部依存の管理です。</td>
</tr>
</tbody>
</table>

<h2>よくある迷い方</h2>

<h4>Mistake</h4>
<ul>
<li><strong>Datasets だけ見て進めた気になる：</strong> 何を成果物として残すかは L0実践節 と Verification で固定する必要があります。</li>
<li><strong>L0実践節 を勝利条件の定義と誤読する：</strong> 手順書だけでは、何を前進と呼ぶかまでは決まりません。</li>
<li><strong>ケースワーク節 を直接の証拠と読む：</strong> ここは設計参照であり、WBE が成立した証明ではありません。</li>
<li><strong>提案統合節 を実装完了一覧として読む：</strong> 提案受理や文書反映と、実装完了や外部合意は別です。</li>
</ul>

<h2>次に戻る場所</h2>
<p>
実務の入口へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、L0 の実作業へ戻るなら <a href="https://mind-upload.com/datasets.html#l0-practice">L0実践</a>、更新先を決めたい場合は <a href="https://mind-upload.com/content_hub.html">公開コンテンツ統合ハブ</a> をご利用ください。
</p>
