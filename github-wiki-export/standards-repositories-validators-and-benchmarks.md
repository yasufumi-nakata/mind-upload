# Wiki：規格・置き場・Validator・ベンチマーク

> 似て見える基盤群を、版固定と評価固定まで含めて切り分けます
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Operational guide

## このページの役割
このページは、Mind-Upload で何度も出てくる『規格』『置き場』『Validator』『ベンチマーク』に加えて、実務で重要な『版固定』『ローダ / 変換器』『benchmark harness』の役割差を整理する wiki です。名前だけ覚えるのではなく、『どこで再現性が壊れやすいか』まで分けて理解することを目標にします。

## 正確さの前提
ここで説明するのは役割の基本整理です。どの規格やどのベンチマークが最終的に WBE に十分かの結論を与えるページではありません。

## 公開ページへ戻る
- [データ&ベンチ](https://mind-upload.com/datasets.html)
- [検証基盤](https://mind-upload.com/verification.html)
- [ケースワーク](https://mind-upload.com/verification.html#casework)

## 関連 Wiki
- [Wiki: 検証基盤の基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 標準、ベンチ、登録、監査の大きな地図へ戻れます。
- [Wiki: ベースライン・事前登録・モデルカード](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Benchmark の先にある運用語の違いを補います。
- [Wiki: イベント同期と観測ログ](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - 規格に入れたいログ情報の具体例を補います。
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - 他の補助ページへ戻れます。

## いま分かっていること
- 研究を比較可能にするには、データの形、公開先、検査手段、評価ルールを分けて整える必要があります。
- BIDS と EEG-BIDS は『どう置くか』の規格であり、採点ルールそのものではありません。
- OpenNeuro や PhysioNet は公開基盤ですが、入力形式や評価手順を自動で全部保証するわけではありません。
- 同じ dataset 名でも、snapshot / version と evaluation family が違えば比較不能です。

## まだ分かっていないこと
- WBE 向けの最終的な共通 benchmark がどの粒度であるべきかは未確定です。
- どの validator や監査項目を最終標準にするかは、今後の運用設計に依存します。

---

<h2>いちばん短い区別</h2>
<p>
<strong>規格</strong>は「どういう形でそろえるか」、<strong>置き場</strong>は「どこへ公開するか」、<strong>Validator</strong>は「規格どおりかを機械で確かめる道具」、<strong>ベンチマーク</strong>は「何で比べるか」のルールです。同じ『研究基盤』でも役割は別です。
</p>

<h2>なぜ分けて考えるのか</h2>
<p>
この 4 つを混同すると、「OpenNeuro に上げたから benchmark がある」「BIDS だから比較まで済んでいる」といった読み違いが起きます。実際には、データの形をそろえる仕事と、比較のルールを作る仕事は別です。
</p>

<h2>まず用語を分ける</h2>
<table>
<thead>
<tr>
<th>用語</th>
<th>何をするものか</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>規格（standard）</strong></td>
<td>ファイルの置き方、名前、メタデータの書き方をそろえます。</td>
<td>BIDS、EEG-BIDS です。</td>
</tr>
<tr>
<td><strong>置き場 / 共有基盤（repository）</strong></td>
<td>データを公開し、他の人が取得できるようにします。</td>
<td>OpenNeuro、PhysioNet、PDB などです。</td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>規格違反や不足メタデータを機械で点検します。</td>
<td>BIDS Validator です。</td>
</tr>
<tr>
<td><strong>ベンチマーク（benchmark）</strong></td>
<td>課題、分割、指標、禁止事項を固定して比較可能にします。</td>
<td>MOABB、MLPerf、ImageNet 型の運用です。</td>
</tr>
</tbody>
</table>

<h2>実務では 4 つでは足りず、5 層で見ます</h2>
<table>
<thead>
<tr>
<th>層</th>
<th>代表例</th>
<th>ここで固定するもの</th>
<th>まだ保証しないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 規格</strong></td>
<td>BIDS、EEG-BIDS</td>
<td>ファイル名、必須メタデータ、座標系、events/channels/electrodes の形です。</td>
<td>train/test 分割や指標は決まりません。</td>
</tr>
<tr>
<td><strong>2. 公開版</strong></td>
<td>OpenNeuro snapshot、PhysioNet version</td>
<td>どの版を取得したか、第三者が同じ入力へ戻れることです。</td>
<td>その版が benchmark split や前処理条件まで固定するとは限りません。</td>
</tr>
<tr>
<td><strong>3. 変換・読込</strong></td>
<td>MNE-BIDS</td>
<td>BIDSPath、metadata 抽出、MNE への読込経路、必要時の format 変換です。</td>
<td>比較指標や評価族は固定しません。</td>
</tr>
<tr>
<td><strong>4. Benchmark harness</strong></td>
<td>MOABB</td>
<td>paradigm、evaluation family、統計比較、同一 pipeline の横断評価です。</td>
<td>source imaging の真値や実運用安全性までは保証しません。</td>
</tr>
<tr>
<td><strong>5. 学習器</strong></td>
<td>線形分類器、Riemannian pipeline、deep model</td>
<td>どのモデルを、どの前処理・乱数・ハイパーパラメータで回したかです。</td>
<td>上の 1〜4 が固定されていなければ、公平比較にはなりません。</td>
</tr>
</tbody>
</table>

<strong>2026-03 の site rule</strong>
<p>
OpenNeuro は snapshot を semantic version の git tag として扱い、PhysioNet も project ごとに version を明示して引用させます。したがって本サイトでは、dataset 名だけではなく <strong>snapshot / version / DOI または永続 URL</strong> まで成果物へ含めます。さらに、MNE-BIDS は入出力経路を助ける道具であり、MOABB は比較ルールを固定する道具です。この 2 つを混ぜて「BIDS にしたので benchmark まで済んだ」と読まないでください。
</p>

<h2>EEG の例で見ると</h2>
<table>
<thead>
<tr>
<th>段階</th>
<th>そこでやること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 規格へそろえる</strong></td>
<td>EEG ファイル、events.tsv、channels.tsv、メタデータを BIDS 形へそろえます。</td>
</tr>
<tr>
<td><strong>2. Validator で点検する</strong></td>
<td>規格違反や不足項目を機械的に洗い出します。</td>
</tr>
<tr>
<td><strong>3. 置き場へ公開する</strong></td>
<td>OpenNeuro や PhysioNet のような共有基盤に載せ、第三者が取得できるようにします。</td>
</tr>
<tr>
<td><strong>4. ベンチマークで比べる</strong></td>
<td>同じ train/test 分割、同じ指標、同じベースラインでモデルを比較します。</td>
</tr>
</tbody>
</table>

<strong>ここが重要です</strong>
<p>
規格にそろえただけでは、まだ「比べるルール」はありません。逆に benchmark だけあっても、入力の形がバラバラなら比較が崩れます。両方必要です。
</p>

<h2>何が欠けると何が困るか</h2>
<table>
<thead>
<tr>
<th>欠けるもの</th>
<th>起きやすい問題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>規格</strong></td>
<td>ファイル名やメタデータが人ごとに違い、追試の入口で止まります。</td>
</tr>
<tr>
<td><strong>置き場</strong></td>
<td>存在を知っても入手や再利用ができず、比較の輪が広がりません。</td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>規格違反に気づくのが遅れ、共有直前や再解析時に事故が出ます。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>各自が違う分割や指標で評価し、「勝った」の意味が揺れます。</td>
</tr>
</tbody>
</table>

<h2>raw ファイルだけでは足りない理由</h2>
<p>
波形ファイルを置いただけでは、規格も benchmark も十分ではありません。少なくとも、イベント定義、刺激ログ、同期情報、QC ログ、除外理由がないと、同じ課題として追試しにくくなります。
</p>

<strong>安全な読み方</strong>
<p>
「公開されている」ことと「比較可能である」ことは別です。公開は入口、比較可能性はその次の設計です。
</p>

<h2>ありがちな混同</h2>
<table>
<thead>
<tr>
<th>言いがちなこと</th>
<th>より正確な言い換え</th>
</tr>
</thead>
<tbody>
<tr>
<td>「BIDS にしたので benchmark がある」</td>
<td>BIDS は入力形式の規格であり、比較ルールそのものではありません。</td>
</tr>
<tr>
<td>「OpenNeuro に置いたので標準化された」</td>
<td>置き場に載せても、規格やメタデータが十分とは限りません。</td>
</tr>
<tr>
<td>「同じ dataset 名だから同じ入力を使った」</td>
<td>OpenNeuro snapshot や PhysioNet version を固定しない限り、同じ入力とは言えません。</td>
</tr>
<tr>
<td>「Validator が通ったので研究として十分」</td>
<td>Validator は形式点検であり、研究の妥当性や benchmark の強さまでは保証しません。</td>
</tr>
<tr>
<td>「MNE-BIDS で読めたので benchmark になった」</td>
<td>MNE-BIDS は読込・変換の助けであり、evaluation family や比較統計を固定するのは別作業です。</td>
</tr>
<tr>
<td>「MOABB の score は task をまたいでそのまま比較できる」</td>
<td>within-session、cross-session、cross-subject は別の評価族であり、同列には扱えません。</td>
</tr>
<tr>
<td>「前処理済みファイルを raw BIDS に戻しても問題ない」</td>
<td>BIDS と MNE-BIDS は原則として unprocessed ないし minimally processed data を前提にしており、modified data は lineage を明示して derivatives として扱う方が安全です。</td>
</tr>
<tr>
<td>「ベンチマークに勝ったので実運用も十分」</td>
<td>benchmark は比較の物差しであり、実運用や L4/L5 の成立を自動では保証しません。</td>
</tr>
</tbody>
</table>

<h2>最低限固定したい 4 つの ID</h2>
<table>
<thead>
<tr>
<th>ID</th>
<th>最低限ほしいもの</th>
<th>欠けると何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Input ID</strong></td>
<td>OpenNeuro snapshot tag、PhysioNet version、DOI、取得日です。</td>
<td>同じ dataset 名でも別版を混ぜ、追試不能になります。</td>
</tr>
<tr>
<td><strong>Schema ID</strong></td>
<td>BIDS / EEG-BIDS の版、Validator の版、残した warning の理由です。</td>
<td>規格差と実装差を切り分けられません。</td>
</tr>
<tr>
<td><strong>Evaluation ID</strong></td>
<td>within-session / cross-session / cross-subject、指標、split seed、禁止事項です。</td>
<td>score の意味がずれ、公平比較が崩れます。</td>
</tr>
<tr>
<td><strong>Pipeline ID</strong></td>
<td>MNE-BIDS / MOABB / 学習器 / 環境の version、commit、設定です。</td>
<td>同じ版の入力でも再実行時に違う結果が出ます。</td>
</tr>
</tbody>
</table>

<h2>強い主張を読むときの 5 問</h2>
<ol>
<li><strong>入力の規格は何か：</strong>BIDS などで形がそろっているかを確認します。</li>
<li><strong>どの版を使ったか：</strong>snapshot、version、DOI、取得日が固定されているかを見ます。</li>
<li><strong>何で読み書きしたか：</strong>ローダ / 変換器と、その version が明示されているかを見ます。</li>
<li><strong>何で比べているか：</strong>benchmark、evaluation family、分割、指標、禁止事項が固定されているかを見ます。</li>
<li><strong>raw と derivative を分けたか：</strong>前処理済みデータの lineage が追えるかを見ます。</li>
</ol>

<h2>参考文献と公式ページ</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS Specification: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://docs.openneuro.org/git.html" target="_blank">OpenNeuro Docs: Git access and snapshots</a></li>
<li><a href="https://docs.openneuro.org/user_guide.html" target="_blank">OpenNeuro Docs: Dataset landing page and snapshot metadata</a></li>
<li><a href="https://physionet.org/about/" target="_blank">PhysioNet: About and citation policy</a></li>
<li><a href="https://physionet.org/about/content/" target="_blank">PhysioNet: Resources and citation guidance</a></li>
<li><a href="https://doi.org/10.21105/joss.01896" target="_blank">Appelhoff et al. (2019), MNE-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS Docs: write_raw_bids</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018), MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB Docs</a></li>
<li><a href="https://moabb.neurotechx.com/docs/auto_examples/paradigm_examples/index.html" target="_blank">MOABB Docs: paradigm and evaluation examples</a></li>
</ul>

<h2>次にどこへ戻るか</h2>
<p>
実務の入口へ戻るなら <a href="https://mind-upload.com/datasets.html">データ&ベンチ</a>、全体設計へ戻るなら <a href="https://mind-upload.com/verification.html">検証基盤</a>、他分野の実例へ戻るなら <a href="https://mind-upload.com/verification.html#casework">ケースワーク</a> をご利用ください。
</p>
