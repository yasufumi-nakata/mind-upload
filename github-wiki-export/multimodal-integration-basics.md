# Wiki：マルチモーダル統合の基本

> 足し算すると全部分かる、ではなく、弱点を補い合う設計です
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
このページは、なぜ Mind-Upload でマルチモーダル統合が重要になるのかを、EEG、MEG、fMRI、ECoG、MRI の役割差から初歩的に説明する wiki です。『EEG だけでは足りない』の先にある設計を、過大評価せずに理解することを目的にします。

## 正確さの前提
複数モダリティを組み合わせても、本人性や意識の強い主張が自動で成立するわけではありません。ここで扱うのは、測定の補完関係と実務上の注意点です。

## 公開ページへ戻る
- [EEG入門](https://mind-upload.com/eeg_101.html)
- [研究ノート](https://mind-upload.com/perspective.html)
- [データ&ベンチ](https://mind-upload.com/datasets.html)

## 関連 Wiki
- [Wiki: EEGの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - まず EEG 単体の強みと弱みへ戻れます。
- [Wiki: イベント同期と観測ログ](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - 統合で特に重要な同期とログの話を補います。
- [Wiki: 不確実性・信頼区間・棄権](https://github.com/yasufumi-nakata/mind-upload/wiki/uncertainty-confidence-and-abstention) - 統合しても不確実性が消えない理由を補います。

## いま分かっていること
- EEG 単体では空間分解能に限界があり、他モダリティが補助になります。
- MEG、fMRI、ECoG、MRI は、それぞれ別の種類の情報で EEG を補完します。
- 統合時にも不確実性は消えず、座標誤差や同期誤差として残ります。

## まだ分かっていないこと
- どの組み合わせが WBE の各段階に最も効くかは、まだ固定していません。
- 複数モダリティを統合しても、本人性や現象的意識の判定が解決するわけではありません。

---

<div class="abstract-box">
<h2>いちばん短い説明</h2>
<p>
マルチモーダル統合とは、「1つの装置で全部分かる」と考える代わりに、<strong>別々の弱点を持つ測定を組み合わせる</strong>設計です。時間に強い EEG、位置に強い fMRI、高 SNR の侵襲計測などを、目的に応じて補完させます。
</p>
</div>

<section class="section" id="why-not-eeg-alone">
<h2 class="section-title">なぜ EEG 単体では足りないのか</h2>
<p>
EEG は時間変化を見るには強い一方、どこで起きたかを強く言うのは苦手です。特に深部構造や微細な局所回路まで直接読むことはできません。そのため、空間情報や構造情報を補うために、別モダリティが必要になります。
</p>
</section>

<section class="section" id="roles">
<h2 class="section-title">各モダリティの役割差</h2>
<table class="data-table">
<thead>
<tr>
<th>モダリティ</th>
<th>得意</th>
<th>弱い点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>ms スケールの時間変化、状態遷移、閉ループの入口。</td>
<td>空間分解能、深部構造、逆問題の非一意性。</td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>時間分解能を保ったまま、EEG と違う感度分布で補完できます。</td>
<td>高価で設備制約が大きく、全員が簡単に使えるわけではありません。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>空間分解能が高く、どの部位が関与していそうかを見やすいです。</td>
<td>時間分解能が遅く、リアルタイム性には向きません。</td>
</tr>
<tr>
<td><strong>ECoG / 侵襲計測</strong></td>
<td>高 SNR、高時間分解能、局所情報の豊かさ。</td>
<td>倫理・適用範囲の制約が非常に大きいです。</td>
</tr>
<tr>
<td><strong>MRI（構造画像）</strong></td>
<td>頭部形状や解剖情報を与え、順モデルや位置合わせを助けます。</td>
<td>機能の時間変化そのものは直接与えません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="good-combos">
<h2 class="section-title">よくある組み合わせの意味</h2>
<table class="data-table">
<thead>
<tr>
<th>組み合わせ</th>
<th>何を補いたいか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG + fMRI</strong></td>
<td>時間変化と空間分布を補い合います。</td>
</tr>
<tr>
<td><strong>EEG + MEG</strong></td>
<td>異なる感度分布を組み合わせ、ソース推定の制約を強めます。</td>
</tr>
<tr>
<td><strong>EEG + MRI</strong></td>
<td>頭部モデルや座標合わせを改善し、逆問題の仮定を現実に寄せます。</td>
</tr>
<tr>
<td><strong>EEG + ECoG</strong></td>
<td>表面計測と高精細局所計測のギャップを比較できます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-still-doesnt-happen">
<h2 class="section-title">統合しても自動では起きないこと</h2>
<div class="key-points">
<h4>ここは誤解しやすい点です</h4>
<ul>
<li><strong>足し算だけで真実になるわけではありません：</strong>複数データでも仮定と不確実性は残ります。</li>
<li><strong>本人性が自動で証明されるわけではありません：</strong>測定が増えても、L4 の課題は別です。</li>
<li><strong>因果検証が不要になるわけではありません：</strong>統合したうえで、介入や摂動のテストが要ります。</li>
</ul>
</div>
</section>

<section class="section" id="integration-costs">
<h2 class="section-title">統合で増える実務負荷</h2>
<table class="data-table">
<thead>
<tr>
<th>実務項目</th>
<th>何が難しくなるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>時刻同期</strong></td>
<td>遅延、ジッタ、ドリフトが複数系統で増えます。</td>
</tr>
<tr>
<td><strong>座標合わせ</strong></td>
<td>センサー位置、頭部形状、画像座標のずれを管理する必要があります。</td>
</tr>
<tr>
<td><strong>ノイズ構造</strong></td>
<td>各モダリティでノイズの種類が違い、同じ前処理では済みません。</td>
</tr>
<tr>
<td><strong>メタデータ</strong></td>
<td>BIDS や派生ログを丁寧に残さないと、統合後の監査が困難になります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">マルチモーダルの主張を読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>何を補うための統合か：</strong>時間、空間、局所性、構造のどれを補っているか。</li>
<li><strong>同期と座標合わせが書かれているか：</strong>統合の土台が明示されているか。</li>
<li><strong>不確実性を引き継いでいるか：</strong>統合後だけきれいな数字になっていないか。</li>
<li><strong>強い主張へ飛んでいないか：</strong>測定統合を、本人性や意識の証明と混同していないか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
EEG の基本へ戻るなら <a href="https://mind-upload.com/eeg_101.html">EEG入門</a>、長文の設計へ戻るなら <a href="https://mind-upload.com/perspective.html">研究ノート</a>、入口データへ戻るなら <a href="https://mind-upload.com/datasets.html">データ&ベンチ</a> をご利用ください。
</p>
</section>
