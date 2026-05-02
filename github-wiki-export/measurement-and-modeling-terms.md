# Wiki: 測定からモデリングまでの用語ガイド

> 単語を点で覚えるのではなく、流れでつなげて覚えましょう。
>
> この学習ページは GitHub Wiki 用に生成されています。公開ポータルは [mind-upload.com](https://mind-upload.com) で管理しています。

- Updated: 2026-04-04 / Role: 学習ガイド (2026 年 4 月 4 日のコンパニオン カード分割で更新)

## このページの役割
このページは、EEGなどの計測用語、ESIやDCMなどのモデル用語、BIDSやQCなどの運用用語を「観察→整理→推定→検証」の流れで結び付けて理解するためのWikiです。個々の単語を暗記するのではなく、まずどの単語を使用するか、どこで議論をやめるべきかを区別することを目的としています。

## 正確性に関する注記
ここで示したフローは、理解できるように整理したものです。実際の研究では行きつ戻りつや例外はありますが、観察と推定、推定と検証を混同しないことが重要です。

## 公開ページへ戻る
- [用語集](https://mind-upload.com/glossary.html)
- [脳波検査の概要](https://mind-upload.com/eeg_101.html)
- [検証プラットフォーム](https://mind-upload.com/verification.html)

## 関連 Wiki ページ
- [Wiki: 脳波の基礎](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - 測定への入り口として、EEG が何を測定するかを確認できます。
- [Wiki: EEG の前処理と QC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - 組織化段階で結果を変えるものを補償します。
- [Wiki: 検証インフラストラクチャの基本](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - 最終検証ステップで修正すべき部分を補います。

## 現在わかっていること
- 測定、前処理、推定、検証にはそれぞれ役割があり、それぞれに異なる言葉が使われます。
- 観測された信号はそのままの脳の状態ではなく、推定には不確実性や候補モデルの依存性が伴います。
- BIDS と QC は追加のボーナスではありません。それらは比較可能性の根幹です。
- ソルバー名はクレームの強さを決定しません。検証ラダーとルート カードが行います。
- 逆問題の場合、フィールドの可視性、導電率の感度、ソルバーの不確実性、検証クラスは別の問題になります。一方の進歩が他方を消去することはありません。
- 全脳または高速の DCM は扱いやすさを向上させますが、事前分布、スキャン期間、およびサンプル サイズによって設定された候補モデルの依存性、処理感度、または信頼性の制限は消去されません。
- ルート カードとコンパニオン カードはさまざまな質問に答えます。ルート カードは 1 つの測定ルートまたは推定ルートを入力しますが、コンパニオン カードは複数のルート間の関係または連続したステージ間の関係を入力します。
- データが増えれば自動的に設計が強化されるわけではありません。識別可能性の目標、省略されたメカニズムのストレス、および最小十分性の停止ルールにより、さまざまな質問に答えられます。
- 同一セッションのマルチモーダル、同一主題の人間代理、および同一脳言語は、それ自体では融合の妥当性、人間代理の構成、または状態の連続性を解決しません。

## まだわかっていないこと
- 非侵襲的測定だけで WBE の十分な内部状態をどの程度復元できるかは未解決の問題のままです。
- どのモデリングの組み合わせが最終的に最も効果的になるかは、まだ研究中です。
- 観察データのみを使用して因果関係を特定できる程度は、介入デザインによって大きく異なります。
- どの DCM ルート カード バンドルがタスク fMRI、安静状態 fMRI、MEG にわたるサイトのデフォルト ベンチマークとなるべきかは、まだ決まっていません。
- どの逆問題ルートまたは検証ラダーが焦点または臨床ベンチマーク体制を超えて一般化するのかは未解決のままです。
- どのコンパニオン カード バンドルが、マルチモーダル フュージョン、生きた人間のプロキシ バンドル、および連続した同一脳ブリッジを組み合わせた主張に対して、サイトのデフォルトのフロントドア言語となるべきかはまだ決まっていません。

---

<h2>最短マップ</h2>
<p>
このサイトの言葉は大きく4つのレベルに分けられます。これらは、<strong>observe</strong>、<strong>arrange</strong>、<strong>estimate</strong>、<strong>confirm</strong>です。言葉が難しくても、物語がどの段階にあるのかを最初に説明しておくと混乱が少なくなります。
</p>

<strong>2026-03 初心者ルート修正</strong>
<p>
このサイトの古い初心者向けルートでは、ESI、DCM、および SCM を「モデリング用語」としてあまりにも大雑把にグループ化していました。それは弱すぎました。このサイトでは、<strong>ESI は検証ラダー</strong> によって読み取られ、<strong>DCM は候補モデル開示とモデル回復</strong> によって読み取られ、<strong>SCM は介入条件と同値クラス絞り込み</strong> によって読み取られます。
</p>

<strong>2026-03-26初心者ルート修正</strong>
<p>
2 番目の初心者の読みすぎも残っています。より多くのセンサー、同一脳のリンケージ、またはコネクトームの事前分布は、あたかも候補セットがほぼ閉じられているかのように聞こえる可能性があります。このサイトでは、それはまだ強すぎます。同一セッションのマルチモーダル作業には <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/multimodal-integration-basics">Fusion Card</a> が必要で、連続したセイムブレインまたはクロスデイクレームには <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-continuity-bridge">State-Continuity Bridge Card</a> が必要で、コネクトーム制約のある予測子には <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation#identifiability-card">Identifiability Card</a> が必要です。詳細なルールは <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">Wiki: 観測から推定まで </a> にあります。
</p>

<strong>2026-03-27 逆問題ルートの修正</strong>
<p>
初心者向けの読みすぎがもう 1 つ残っています。<strong> 逆問題の進行状況 </strong> は、依然として 1 つの連続した小節のように聞こえる可能性があります。一次文献ではそのショートカットはサポートされていません。 <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a>、<a href="https://doi.org/10.1002/hbm.20571" target="_blank">ゴールデンホルツら。 (2009)</a>、<a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al。 (2021)</a> は、<strong> のフィールド構成とヘッドモデルの詳細を示しています </strong> は、センサーに到達するものをすでに制限しています。 <a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerkら(2024)</a> および <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk et al. (2026)</a> は、<strong> の導電率の不確実性と推定 </strong> が依然として結果を大きく動かすことを示しています。 <a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>、<a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong 他(2025)</a>、<a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> は、<strong> 候補セットと不確実性 </strong> が指定された逆ファミリ内で公開される方法を改善します。 <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">ミクランら(2020)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">パスカレラ 他(2023)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse 他(2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> は、さまざまな <strong> ソース レジームとエラー質問 </strong> を検証します。したがって、このサイトでは、逆論文を 1 つのはしごとして読むことはなくなりました。
</p>

<strong>2026-03-28初心者ルート修正</strong>
<p>
もう 1 つ技術的な読みすぎがまだ残っています。曖昧な点に名前を付けた後でも、読者は次のステップは単に <strong> もっとデータを追加する</strong> または <strong> 1 つモダリティを追加するだけであると考える可能性があります</strong>。一次文献ではそのショートカットはサポートされていません。 <a href="https://doi.org/10.1049/iet-syb.2010.0061" target="_blank">Raue et al. (2011)</a> は、適切な条件下での <strong> 実験計画、</strong>、またはデータの情報内容に合わせた <strong> モデル削減 </strong> によって、非識別性が解決されることを示しました。 <a href="https://doi.org/10.1016/j.mbs.2016.10.009" target="_blank">Chisら。 (2016)</a> は、<strong> のずさんさは識別可能性ではないことを示しました </strong> したがって、設計では、1 つの代理不確実性スコアのみを圧縮するのではなく、識別可能性の基準を最適化する必要があります。 <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">ホワイト 他(2016) </a> は、明らかに相補的な実験が、代わりに <strong> の省略されたメカニズム </strong> を関連させ、モデルの不一致を増大させる可能性があることを示しました。 <a href="https://doi.org/10.1038/s41540-023-00325-1" target="_blank">ゲベルツ&アンプ; Kareva (2024)</a> および <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">Liu et al. (2025) </a> は、識別可能性分析とアクティブ ラーニングが、無制限の収集計画ではなく、<strong>最小限に十分な </strong> スケジュールを導き出せることを示しました。神経科学では、<a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> は、<strong> 小型のターゲット録音セット </strong> がコネクトーム制約のあるネットワークの縮退を除去できることを示しました。 Engel (2025)</a> は、タスク変数 </strong> 間の <strong> 因果的相互作用を保存すると、相関のみの削減では見逃される行動的に関連する計算を回復できることを示しました。したがって、このサイトでは、より安全な初心者ルールは、「さらに収集する」ではなく、「残っている曖昧さの名前を指定し、どの識別可能性の目的が次の条件を選択したかを述べ、新しい条件が省略されたメカニズムのエラーを明らかにするかどうかをテストし、どの最小十分性停止ルールが収集を終了するかを言う」ことです。より長いルールは <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation#identifiability-card">Wiki: 観察から推定まで </a> および <a href="https://mind-upload.com/verification.html#experiment-design-leverage"> 検証: 実験設計の活用 </a> にあります。
</p>

<strong>2026-04-01初心者ルート修正</strong>
<p>
初心者向けの残りの弱点はさらに微妙でした。このページは読者が <strong>DCM</strong> を一般的な因果関係の文言として扱うことをすでに止めていますが、それでも、最近の DCM 論文を因果関係の強さの 1 つの単調な梯子を形成しているかのように読む余地は残していました。一次文献ではそのショートカットはサポートされていません。 <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">ペニーら(2004)</a> および <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">Rosa et al。 (2012)</a>は<strong>の候補機種比較とファミリー検索</strong>を強化。 <a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">Frässle et al. (2021)</a> および <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Wu ら。 (2024) </a> は、<strong> の扱いやすさと拡張性を強化します </strong>。しかし、<a href="https://doi.org/10.1002/hbm.23061" target="_blank">Fr&auml;ssle et al. (2016)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2019.116435" target="_blank">Almgren et al. (2020)</a>、<a href="https://doi.org/10.1002/hbm.26751" target="_blank">Zhang 他(2024)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2024.120604" target="_blank">Ma et al. (2024)</a> は、<strong> の信頼性、事前分布、処理ポリシー、スキャン期間、サンプル サイズが </strong> によって依然として結果に大きく影響していることを示しています。したがって、このサイトでは、DCM の進行状況は 1 つの進行状況バーとしてではなく、<strong>axis</strong> によって読み取られます。
</p>

<strong>2026-04-04 測定モデル境界の修正</strong>
<p>
次の弱点は 1 つのルート内ではなく、ルート間の <strong></strong> でした。このページでは、観察、推定、検証が異なる段階であることをすでに説明しましたが、依然としてコストの高いあいまいさが 1 つ残されています。読者は、<strong> 同じセッション マルチモーダル </strong>、<strong> 同じサブジェクト プロキシ リッチ </strong>、または <strong> 同じ脳シーケンシャル </strong> という表現から、<strong> 測定自体が強化される </strong> という漠然とした考えに移行する可能性があります。現在の一次文献はその圧縮をサポートしていません。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii 他(2024)</a>、<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>、<a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">ボルト 他(2025)</a>、<a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp ら。 (2025)</a> は、同期モダリティまたは結合モダリティが依然としてデフォルトで 1 つの時間的オブジェクトまたは 1 つの生物学的量を定義していない理由を示しています。 <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Liら(2025)</a>、<a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B'gh 他(2024)</a>、<a href="https://doi.org/10.1002/nbm.5256" target="_blank">モーガンら。 (2024)</a>、<a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri 他(2023)</a>、<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026)</a> は、いくつかの生きた人間の行が量のタイプ、動作点、完全なケースの可用性、不一致トポロジーにおいて依然として異なる理由を示しています。 <a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">ボッシュ他(2022)</a>、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONSコンソーシアムほか(2025)</a>、<a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego 他(2020)</a>、<a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">ヴァン・デ・ヴィル他(2021)</a>、<a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz 他(2025)</a>、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">ウィルソンら。 (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairragkar et al。 (2025)</a> は、標本の同一性や経時的な安定した使用から、どの輸送物体が同じままであるかを依然として教えてもらえない理由を示しています。したがって、このページでは、<strong> ルート カード </strong> と <strong> コンパニオン カード </strong> を、1 つの一般的な検証ラベルの下で一緒に混同するのではなく、分離するようになりました。
</p>

<h2>4 レベルで表示</h2>
<table>
<thead>
<tr>
<th>ステージ</th>
<th>ここに出やすい単語</th>
<th>何してるの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1。観測</strong></td>
<td>EEG、MEG、fMRI、ECoG</td>
<td>脳や身体から発せられる信号をまず計測します。 </td>
</tr>
<tr>
<td><strong>2。整理</strong></td>
<td>QC、前処理、BIDS</td>
<td>異音や不具合がないかチェックし、他の人が見習える形に整えます。 </td>
</tr>
<tr>
<td><strong>3。推定</strong></td>
<td>逆問題、ESI、DCM、SCM</td>
<td>観察から脳内の状態や因果構造をどこまで推定できるか、どのルートカードが天井を固定するかを考えます。 </td>
</tr>
<tr>
<td><strong>4。検証</strong></td>
<td>ベンチマーク、ベースライン、事前登録、モデルカード</td>
<td>推定またはモデルが本当に当てはまるかどうかを比較可能な方法で確認します。 </td>
</tr>
</tbody>
</table>

<h2> 分割する必要があった 3 つのコンパニオン カード</h2>
<p>
このページでは、より厳密な区別が使用されるようになりました。 <strong>route カード </strong> は、1 つの測定または推定ルートとその上限を記述します。 <strong> コンパニオン カード </strong> は、1 つのルートだけでは主張を説明できない場合に、複数のルートまたはステージ間の関係を説明します。科学的な理由は単純です。現在の一次文献では、<strong>multimodal</strong>、<strong>proxy-rich</strong>、および <strong>same-brain</strong> を、証拠強度における 1 つの一般的なアップグレードであるかのように扱うことはサポートされていません。
</p>
<table>
<thead>
<tr>
<th>それでもオーバーリードされるクレームパターン</th>
<th>ショートカットが科学的に安全ではない理由</th>
<th>一次文学停止規則</th>
<th>このサイトではコンパニオン カードが必要です</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同一セッションのマルチモーダル/アトラス情報に基づいたクレーム</strong></td>
<td>共有タイムスタンプ、共有係数、および 1 つの外部接地された生物学的量は、異なる成果です。同一セッションまたはアトラス情報に基づいた文言は、それ自体では 1 つの時間的オブジェクトまたは 1 つの数量の橋を証明するものではありません。</td>
<td><a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a>、<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a>、<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">Chen et al. (2025)</a>、<a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">ボルト 他(2025) </a>、および <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp ら。 (2025)</a> は、時間的カーネルの不一致、共有構造と固有構造、自律結合、および数量ブリッジ障害が別々の負担として残る理由を示しています。</td>
<td><strong>フュージョンカード</strong></td>
</tr>
<tr>
<td><strong>1 つの引数内の複数の生きた人間のプロキシ行</strong></td>
<td>S実際の人間のルートは、量のタイプ、証拠の役割、操作点、完全なケースのジオメトリ、および不一致トポロジーにおいて依然として異なる可能性があります。それらを一緒にリストしても、まだ 1 つの同じ対象の状態サンプルは作成されていません。</td>
<td><a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">Li ら(2025)</a>、<a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">B'gh 他(2024)</a>、<a href="https://doi.org/10.1002/nbm.5256" target="_blank">モーガンら。 (2024)</a>、<a href="https://doi.org/10.1093/brain/awac335" target="_blank">アミリ 他(2023)</a>、<a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova 他。 (2026)</a> は、ルートローカルの再現性、メソッドファミリーの不等価性、制限された完全ケーススライス、およびハードグループ内の不一致が個別の監査のままである理由を示します。</td>
<td><strong>人間プロキシ構成カード</strong></td>
</tr>
<tr>
<td><strong>同一主題・同一脳シーケンシャルブリッジ</strong></td>
<td>標本の同一性、局所的な構造と機能の関連性、または安定したインターフェースの使用は、それ自体では、どのオブジェクトが時間、体制、または組織の変化を経ても同じままであるかを示しません。</td>
<td><a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">ボッシュ他(2022)</a>、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONSコンソーシアムほか(2025)</a>、<a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a>、<a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">ヴァン・デ・ヴィル他(2021)</a>、<a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">Karpowicz 他(2025)</a>、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">ウィルソンら。 (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairragkar et al. (2025)</a> は、安定した使用が依然としてアライメント、再キャリブレーション、ローカル監視オブジェクト、または短距離サポートに依存する理由を示しています。</td>
<td><strong>ステート・コンティニュイティ・ブリッジ・カード</strong></td>
</tr>
</tbody>
</table>

<strong>視認性を維持するための 1 つの操作上の特徴</strong>
<p>
1 つのルートが独自の仮定を隠したために要求が失敗した場合、不足しているオブジェクトは <strong>route カード </strong> になります。複数のルートまたはステージが 1 つの引数にサイレントに融合されたために要求が失敗した場合、不足しているオブジェクトは <strong> コンパニオン カード </strong> です。このページでは、これらの障害モードを意図的に分離するようになりました。
</p>

<h2>1。観察: まず信号</h2>を取得します。
<p>
EEG と MEG は脳の内部を直接見るのではなく、外部から観測できる信号を測定します。ここで重要な点は、<strong>あなたが観察していることは</strong>脳で実際に起こっていることと同じではないということです。
</p>
<table>
<thead>
<tr>
<th>期間</th>
<th>一言で</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>頭皮の電位差を迅速に測定する方法です。経年変化に強い反面、空間的にはにじみやすい。 </td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>磁場を測定する方法です。これは EEG を補完するものではありますが、高価であり、機器に大きな制限があります。 </td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>血流の変化を計測する方法です。位置的には強力ですが、時間分解能が遅いです。 </td>
</tr>
<tr>
<td><strong>ECoG</strong></td>
<td>脳表面付近を測定する侵襲的測定です。精度は高いですが、適用範囲に強い制限があります。 </td>
</tr>
</tbody>
</table>

<h2>2。整理: 信号をそのまま信じないでください</h2>
<p>
観察される信号には、瞬き、筋電、体の動き、機器の騒音などが含まれます。したがって、次のステップは QC と前処理です。これは見た目を改善するという問題ではなく、<strong> でどの情報が保持され、どの情報が削除されたかを記録する</strong> の問題です。
</p>

<h4>ここで使用されている言葉</h4>
<ul>
<li><strong>QC:</strong>欠落、ノイズ、アーティファクト、および除外理由を数値形式で残します。 </li>
<li><strong>前処理:</strong> 参照メソッド、フィルター、アーチファクト除去などを設定します。</li>
<li><strong>BIDS:</strong>A 他のユーザーが追跡できるようにデータとメタデータを調整するための標準。 </li>
</ul>

<p>
ここを飛ばしてしまうと、後々高性能モデルが出てきても比較できる証拠にはなりません。
</p>

<h2>3。推定:</h2> の観測からどの程度のことが分かるか
<p>
組織化された信号に基づいて脳活動や因果構造を推定したいと考えています。ここで、逆問題、ESI、DCM、および SCM が登場します。ただし、この段階では、<strong> 推定値は推定値であり、不確実性と候補モデルへの依存性が残っていることに留意する必要があります。
</p>
<table>
<thead>
<tr>
<th>期間</th>
<th>追加機能</th>
<th>まだ開示すべきこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>逆問題</strong></td>
<td>これは、外部で観測された信号から隠れた原因を推定するルートの一般的なファミリーです。 </td>
<td> ソリューションはデフォルトでは一意ではないため、<strong> フィールド可視性 </strong>、<strong> フォワード モデルまたは伝導率負荷 </strong>、<strong> ソルバーの不確かさ </strong>、および <strong> 検証クラス </strong> は結果の一部のままになります。 </td>
</tr>
<tr>
<td><strong>ESI</strong></td>
<td>A ヘッド モデル、事前ソース、推定ルールを組み合わせて候補ソース構成を生成する具体的な逆ワークフロー。 </td>
<td>1 つの洗練されたマップでは十分ではありません。 <strong>フィールド可視性</strong>、<strong>フォワードモデル負荷</strong>、<strong>クロスソルバーまたは事後スプレッド</strong>、および<strong>実際にテストされた検証クラスまたはソースレジーム</strong>を開示します。 </td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>A 候補の生成回路モデルを比較し、どちらが観察をよりよく説明するかを尋ねるためのフレームワーク。 </td>
<td>結果は依然として、候補モデル空間、事前分布、ファミリー比較、回復、および外部検証に依存します。 </td>
</tr>
<tr>
<td><strong>SCM</strong></td>
<td>A 介入と反事実を明示するための言語。 </td>
<td>観察データだけでは同等クラスが残ることが多いため、因果関係の主張がどの程度強くなり得るかは介入設計によって決まります。 </td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th>逆問題ゲート</th>
<th>どんな質問に答えますか</th>
<th>代表的な一次文献</th>
<th>まだ閉まらないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ゲート 1: フィールド形成の可視性</strong></td>
<td> ターゲット ソース クラスは、実際の方向、範囲、解剖学的構造、および頭部モデルの詳細に基づいて使用可能な頭皮フィールドを生成しますか?</td>
<td><a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors et al. (2010)</a>; <a href="https://doi.org/10.1002/hbm.20571" target="_blank">ゴールデンホルツら。 (2009)</a>; <a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra 他(2021)</a></td>
<td>A 可視ソース クラスは依然としてローカライズが不十分、識別が不十分、または検証が不十分なままである可能性があります。</td>
</tr>
<tr>
<td><strong>ゲート 2: フォワードモデル / 導電率負担</strong></td>
<td>頭蓋骨または組織の導電率と幾何学的仮定は、局在化、深さ、大きさ、方向をどの程度動かしますか?</td>
<td><a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a>; <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk 他(2026)</a></td>
<td>導電率による広がりの低減は、それ自体ではソルバーの縮退を崩壊させたり、あらゆる領域でソースの回復を証明したりするものではありません。
</tr>
<tr>
<td><strong>ゲート 3: ソルバーファミリー / 事後不確かさ</strong></td>
<td>この方法は、1 つの洗練されたポイント マップの代わりに、代替の線源構成、間隔、または拡張線源の不確実性を公開しますか?</td>
<td><a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>; <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tongら(2025)</a>; <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Fengら(2025)</a></td>
<td>不確実性への曝露を改善しても、可観測性の欠如、間違ったヘッドモデル、または一致しない検証クラスは修復されません。</td>
</tr>
<tr>
<td><strong>ゲート 4: 検証クラス/ソース体制</strong></td>
<td>実際にテストされたエラー質問はどれですか:既知の刺激部位、焦点源ボード、同時侵襲的一致、または臨床発作局在化?</td>
<td><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">ミクランら(2020)</a>; <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">パスカレラら(2023)</a>; <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a>; <a href="https://doi.org/10.1111/epi.18552" target="_blank">Haoら。 (2025)</a></td>
<td>1 つの体制での検証の成功は、集中的、拡張的、自発的、および深部ソースの回復を組み合わせた場合の普遍的な勝者ではありません。</td>
</tr>
</tbody>
</table>

<strong>ここで起こりそうな変化</strong>
<p>
EEG を観察することは、脳の状態を独自に再構成することと同じではありません。さらに、相関予測が正しいことは、因果構造を知っていることと同じではありません。
</p>

<strong>2026-03補足情報</strong>
<p>
DCM は候補生成モデルの比較であり、SCM は介入と反事実の説明を容易にする言語です。因果等価クラスは観察データのみから残ることが多いため、候補モデル空間、家族比較、外部検証、介入データの有無を個別に読み取る必要があります。詳細については、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">Wiki: 観測から推定まで</a> を参照してください。
</p>

<strong>ソルバー名ではなく、4つのゲートでESIを読み取ります</strong>
<p>
ミッシェル＆amp; Brunet (2019) は、ESI を 1 つの単語のメソッドではなく複数ステップのパイプラインとして要約しています。それに加えて、<a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">Ahlfors ら。 (2010)</a>、<a href="https://doi.org/10.1002/hbm.20571" target="_blank">ゴールデンホルツら。 (2009)</a>、<a href="https://doi.org/10.1002/hbm.25272" target="_blank">Piastra et al。 (2021)</a> は、反転が始まる前に場の形成がすでに選択的であることを示しています。<a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> および <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk ら。 (2026)</a> は、導電率の仮定が依然として結果を動かすことを示し、<a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>、<a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong 他(2025)</a>、<a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al. (2025)</a> は、不確実性を隠すのではなく明らかにする必要がある理由を示しています。最後に<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulanら。 (2020)</a>、<a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">パスカレラ 他(2023)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse 他(2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> はさまざまなソース体制を検証します。このサイトでは、「ESI を使用した」というだけの主張では、まだ十分ではありません。
</p>

<strong>因果関係に基づく表現ではなく、候補モデル ルールによって DCM を読み取ります</strong>
<p>
ペニーら。 Rosa et al. (2004) は、DCM 推論が比較されたモデル セットに相対的であることを修正しました。 (2012) は、事後モデル空間検索をどのように拡張できるかを示しました。 (2021) プラスウーら。 (2024) は全脳とより高速な推定を推進しました。これらは <strong>tractability</strong> の進歩であり、識別可能性に対する自動ソリューションではありません。したがって、このサイトでは、候補空間、観察されたサブシステムの閉包 / 潜在交絡の監査、ノード定義ポリシー、サンプリング / 変換の感度、回復、信頼性、および検証が開示されない限り、DCM は <strong> モデル条件付き因果仮説 </strong> のままです。
</p>

<table>
<thead>
<tr>
<th>DCM軸</th>
<th>実際に強化されるもの</th>
<th>まだ閉まらないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>候補機種比較・ファミリー検索</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">ペニーら(2004)</a>; <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">ローザ他(2012)</a>。明示的に宣言された競合他社間のより強力な比較。</td>
<td>省略されたノード、エッジ、事前分布、またはモデル ファミリが存在しないか無関係であることは証明されません。</td>
</tr>
<tr>
<td><strong>スケーリング/扱いやすさ</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">Frässle et al. (2021)</a>; <a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">Wuら。 (2024)</a>。宣言された DCM ファミリ内のより大規模または高速な検索。</td>
<td>グラフを前処理不変、ノード不変、または競合他社の完全な因果関係の真実にするわけではありません。</td>
</tr>
<tr>
<td><strong>処理/第1レベル設計の堅牢性</strong></td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2019.116435" target="_blank">Almgren et al. (2020)</a>; <a href="https://doi.org/10.1002/hbm.26751" target="_blank">Zhang et al. (2024)</a>。 GSR、GLM 設計、コントラスト定義、およびしきい値処理が推定エッジとパラメーターの確実性をどのように変更するかについてのより強力な開示。</td>
<td>パイプラインの堅牢な効果的な接続を 1 つの合理的なパイプラインで代用することはできません。</td>
</tr>
<tr>
<td><strong>信頼性ウィンドウ</strong></td>
<td><a href="https://doi.org/10.1002/hbm.23061" target="_blank">Fr&auml;ssle et al. (2016)</a>; <a href="https://doi.org/10.1016/j.neuroimage.2024.120604" target="_blank">Maら。 (2024)</a>。名前付き事前分布、セッション構造、スキャン期間、サンプル サイズの下で結果がどの程度安定しているかについての限定されたステートメント。</td>
<td>同じグラフが、異なるサイト、より長い期間、より弱いスキャン、または変更された処理ポリシーでも存続することは示されていません。</td>
</tr>
</tbody>
</table>

<strong>完全なルールが存在する場所</strong>
<p>
このページは初心者用マップです。潜在交絡監査、ノード定義ポリシー、棄権境界を含む完全な DCM / 有効接続提出ルールが必要な場合は、<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation#effective-connectivity-route-card">Wiki: 観察から推定まで</a> に進んでください。
</p>

<h2>4。検証: 推定値を信頼する方法</h2>
<p>
最後の質問は、「他の人が同じ条件でこの推定またはモデルを確認できますか?」です。ここで、ベンチマーク、ベースライン、事前登録、モデル カードなどの言葉が登場します。
</p>
<table>
<thead>
<tr>
<th>期間</th>
<th></th>に必要なものは何ですか
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>何を比較するのか、スコアリングにどの指標を使用するのかを修正します。 </td>
</tr>
<tr>
<td><strong>ベースライン</strong></td>
<td>は改善を主張するための出発点となります。 </td>
</tr>
<tr>
<td><strong>事前登録</strong></td>
<td>後から条件を変更することは避けてください。 </td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>のスコアのほか、弱点、故障例、漏水対策、計算条件なども掲載します。 </td>
</tr>
<tr>
<td><strong>実験設計の活用</strong></td>
<td> の名前、次の測定または摂動ターゲットで生き残る曖昧さ、指定された識別可能性目標によってそれが選択された理由、およびさらなる収集を終了する最小十分性停止ルールは何か。 </td>
</tr>
<tr>
<td><strong>ルートカード</strong></td>
<td>ESI、接続性、または DCM が使用される場合、仮定、検証クラス、棄権境界、および結果でまだ特定されていないものを開示します。 </td>
</tr>
<tr>
<td><strong>コンパニオンカード</strong></td>
<td>クレームが複数のルートまたは段階にまたがる場合、<strong>マルチモーダル</strong>、<strong>同一主題</strong>、または<strong>マルチモーダル</strong>、<strong>同一対象</strong>、または<strong>同じ脳</strong>。 </td>
</tr>
</tbody>
</table>

<strong>検証では、次の条件が選択された理由が尋ねられるようになりました</strong>
<p>
このサイトでは、検証はもはや <strong> 測定された内容 </strong> を列挙するだけの場所ではありません。曖昧さが残る場合、より強力なワークフローは、<strong>どの曖昧クラスが生き残ったか</strong>、<strong>どの識別可能性目標が次の条件を選択したか</strong>、<strong>新しい条件によって省略されたメカニズムのエラーが明らかになったか</strong>、<strong>どの最小十分性設計で十分だったか</strong>も説明する必要があります。そうしないと、たとえ注意深くベンチマークを行ったとしても、あいまいさを解消した設計というよりは、依然として無制限のデータ蓄積のように見える可能性があります。
</p>

<h2>参考資料</h2>
<ol>
<li>Pernet, C.R.、Appelhoff, S.、Gorgolewski, K.J. 他（2019年）。 EEG-BIDS、脳波検査用の脳画像データ構造の拡張。 <em>S科学的データ</em>、6、103。<a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>ミシェル、C.M.、＆amp;ブルーネット、D. (2019)。 EEG ソース イメージング: 分析ステップの実践的なレビュー。 <em>神経学のフロンティア</em>、10、325.<a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Ahlfors、S. P.、Han、J.、Belliveau、J. W.、およびH&auml;m&auml;l&auml;inen、M.S. (2010)。音源方向に対する MEG と EEG の感度。 <em>脳トポグラフィー</em>、23(3)、227-232。 <a href="https://doi.org/10.1007/s10548-010-0154-x" target="_blank">doi:10.1007/s10548-010-0154-x</a></li>
<li>Goldenholz, D.M.、Ahlfors, S.P.、H&auml;m&auml;l&auml;inen, M.S.、Sharon, D.、Ishitobi, M.、Vaina, L.M.、&amp; Stufflebeam、S.M. (2009)。脳磁図と脳波における皮質信号源の信号対雑音比のマッピング。 <em>人間の脳のマッピング</em>、30(4)、1077-1086。 <a href="https://doi.org/10.1002/hbm.20571" target="_blank">doi:10.1002/hbm.20571</a></li>
<li>Piastra、M. C.、N&uuml;szlig;ing、A.、Vorwerk、J.、Clerc、M.、Engwer、C.、およびウォルターズ、C.H. (2021)。皮質および皮質下の信号源に対する脳波検査および脳磁気検査の感度に関する包括的な研究。 <em>人間の脳のマッピング</em>、42(4)、978-992。 <a href="https://doi.org/10.1002/hbm.25272" target="_blank">doi:10.1002/hbm.25272</a></li>
<li>Mikulan, E.、Russo, S.、Bares, M.、他（2020年）。人間の脳内刺激と HD-EEG の同時、音源位置特定方法のグラウンドトゥルース。 <em>S科学データ</em>、7、127。<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Pascarella, A.、Mikulan, E.、Sciacchitano, F. 他（2023年）。焦点ソースを使用した ESI メソッドの生体内検証。 <em>NeuroImage</em>、277、120219.<a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">doi:10.1016/j.neuroimage.2023.120219</a></li>
<li>Unnwongse、K.、Achakulvisut、T.、Wu、J.Y.、他。 （2023年）。人間の患者における頭蓋内電気刺激によるEEGソースイメージングの直接検証。 <em>ブレインコミュニケーションズ</em>、5(2)、fcad023。 <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/ブレインコム/fcad023</a></li>
<li>Vorwerk、J.、Wolters、C.H.、&amp;バウムガルテン、D. (2024)。組織の伝導率の不確実性に対するEEGソース分析のグローバルな感度。 <em>人間の神経科学のフロンティア</em>、18、1335212。<a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">doi:10.3389/fnhum.2024.1335212</a></li>
<li>Luria, G.、Viani, S.、Pascarella, A. 他（2024年）。 SESAMEEG パッケージ: M/EEG における信号源の位置特定と不確実性の定量化のための確率的ツール。 <em>人間の神経科学のフロンティア</em>、18、1359753.<a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">doi:10.3389/fnhum.2024.1359753</a></li>
<li>Tong、P. F.、Yang、H.、Ding、X.、他(2025年)。時空間 EEG/MEG ソース イメージングのための偏りのない推定と推論。 <em>医用画像に関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">doi:10.1109/TMI.2024.3506596</a></li>
<li>Hao, S.、Zhao, H.、Feng, Z. 他(2025年)。薬剤耐性てんかんにおける HD-EEG ソースイメージングと同時 SEEG 記録。 <em>てんかん</em>、66(11)、4451-4464。 <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Feng, Z.、Mishne, G.、Hashemi, A. 他(2025年)。 Block-Champagne: 経験的なベイジアン不確実性定量化を使用した拡張 E/MEG ソース活性化のイメージング。 <em>医用画像に関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Vorwerk, J.、K&ouml;hler, T.、G&uuml;llmar, D. 他（2026年）。てんかんの術前評価における信号源分析を改善するための EEG および EEG/MEG 頭蓋骨伝導率推定の可能性。 <em>Journal of Neural Engineering</em>、23(1)、016007.<a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">doi:10.1088/1741-2552/ae2f01</a></li>
<li>Penny、WD、Stephan、K.E.、Mechelli、A.、およびフリストン、K.J. (2004)。動的因果モデルの比較。 <em>NeuroImage</em>、22(3)、1157-1172。 <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Rosa、M.J.、Friston、K.、およびペニー、W. (2012)。動的因果モデルの事後選択。 <em>Journal of Neuroscience Methods</em>、208(1)、66-78。 <a href="https://doi.org/10.1016/j.jneumeth.2012.04.013" target="_blank">doi:10.1016/j.jneumeth.2012.04.013</a></li>
<li>Frässle, S.、Paulus, F.M.、Krach, S.、およびジャンセン、A. (2016)。顔認識ネットワークにおける効果的な接続の信頼性をテストおよび再テストします。 <em>人間の脳のマッピング</em>、37(2)、730-744。 <a href="https://doi.org/10.1002/hbm.23061" target="_blank">doi:10.1002/hbm.23061</a></li>
<li>Frässle、S.、Manjaly、Z.M.、Do、C.T.、Kasper、L.、Pruessmann、K.P.、およびステファン、K.E. (2021)。人間のコネクトミクスのための有向接続性の全脳推定。 <em>NeuroImage</em>、225、117491.<a href="https://doi.org/10.1016/j.neuroimage.2020.117491" target="_blank">doi:10.1016/j.neuroimage.2020.117491</a></li>
<li>Wu、H.、Hu、X.、およびZeng、Y. (2024)。 fMRI 用の高速動的因果モデリング回帰手法。 <em>NeuroImage</em>、304、120954.<a href="https://doi.org/10.1016/j.neuroimage.2024.120954" target="_blank">doi:10.1016/j.neuroimage.2024.120954</a></li>
<li>Almgren、H.、Van de Steen、F.、Razi、A.、Friston、K.、およびマリナッツォ、D. (2020)。静止状態 fMRI からのノイズと有効接続性の DCM 推定に対するグローバル信号回帰の影響。 <em>NeuroImage</em>、208、116435。<a href="https://doi.org/10.1016/j.neuroimage.2019.116435" target="_blank">doi:10.1016/j.neuroimage.2019.116435</a></li>
<li>Zhang、S.、Jung、K.、Langner、R.、Florin、E.、Eickhoff、S.B.、およびポポヴィチ、O.V. (2024)。タスク fMRI からの有効な接続性の DCM 推定に対するデータ処理の種類の影響。 <em>人間の脳のマッピング</em>、45(8)、e26751。 <a href="https://doi.org/10.1002/hbm.26751" target="_blank">doi:10.1002/hbm.26751</a></li>
<li>Ma、L.、ブラウン、S.E.、スタインバーグ、J.L.、ビョーク、J.M.、マーティン、C.E.、キーン II、L.D.、&amp;; Moeller、F.G. (2024)。安静状態 fMRI 動的因果モデリング解析の信頼性に対するスキャン期間とサンプル サイズの影響。 <em>NeuroImage</em>、292、120604.<a href="https://doi.org/10.1016/j.neuroimage.2024.120604" target="_blank">doi:10.1016/j.neuroimage.2024.120604</a></li>
<li>Raue、A.、Kreutz、C.、Maiwald、T.、Klingmüller、U.、および;ティマー、J. (2011)。モデルベースの実験によるパラメータの識別可能性に対処します。 <em>IET システム生物学</em>、5(2)、120-130。 <a href="https://doi.org/10.1049/iet-syb.2010.0061" target="_blank">doi:10.1049/iet-syb.2010.0061</a></li>
<li>Chis、O.-T.、Villaverde、A.F.、Banga、JR.、およびBalsa-Canto、E. (2016)。ずさんさと識別可能性の関係について。 <em>数理生物科学</em>、282、147-161。 <a href="https://doi.org/10.1016/j.mbs.2016.10.009" target="_blank">doi:10.1016/j.mbs.2016.10.009</a></li>
<li>ホワイト、A.、トルマン、M.、テムズ、H.D.、ウィザーズ、H.R.、メイソン、K.A.、およびトランストラム、M.K. (2016)。ずさんなシステムにおけるモデルベースの実験計画とパラメーター推定の限界。 <em>PLoS 計算生物学</em>、12(12)、e1005227。 <a href="https://doi.org/10.1371/journal.pcbi.1005227" target="_blank">doi:10.1371/journal.pcbi.1005227</a></li>
<li>Gevertz、J.L.、&amp;カレヴァ、I. (2024)。識別可能性分析を使用した最小限で十分な実験計画。 <em>npj システム生物学とアプリケーション</em>、10(1)、2. <a href="https://doi.org/10.1038/s41540-023-00325-1" target="_blank">doi:10.1038/s41540-023-00325-1</a></li>
<li>ベイラン、M.、＆amp;リトウィン・クマール、A. (2025)。コネクトーム制約付きリカレント ネットワークにおける神経活動の予測。 <em>Nature Neuroscience</em>、28、2561-2574。 <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Lラングドン、C.、＆amp;エンゲル、T.A. (2025)。認知課題中の異質な神経反応からの潜在回路推論。 <em>Nature Neuroscience</em>、28、665-675。 <a href="https://doi.org/10.1038/s41593-025-01869-7" target="_blank">doi:10.1038/s41593-025-01869-7</a></li>
<li>Liu、X.、Wanika、L.、Chappell、M.J.、およびブランケ、J. (2025)。アクティブラーニングによる実用的な識別可能性を確立するための効率的なデータ収集。 <em>Computational and Structural Biotechnology Journal</em>、27、4992-5006。 <a href="https://doi.org/10.1016/j.csbj.2025.10.058" target="_blank">doi:10.1016/j.csbj.2025.10.058</a></li>
<li>Kothe, C.、Shirazi, S. Y.、Stenner, T.、Medine, D.、Boulay, C.、Grivich, M. I.、Artoni, F.、Mullen, T.、Delorme, A.、およびMakeig、S. (2025)。同期されたマルチモーダル記録のためのラボ ストリーミング レイヤー。 <em>画像神経科学</em>。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Vafaii, H.、Mandino, F.、Desrosiers-Gréacute;goire, G.、他。 （2024年）。自発的な脳活動の多峰性測定により、皮質機能組織の共通パターンと多様なパターンの両方が明らかになります。 <em>Nature Communications</em>、15、383.<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen、J. E.、Lewis、L. D.、Coursey、S. E.、他(2025年)。 EEG-PET-MRI を同時に行うことで、覚醒時とノンレム睡眠時の時間的に結合し、空間的に構造化された脳のダイナミクスを特定します。 <em>Nature Communications</em>、16、8887。<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Bolt, T.S.、van den Brink, R.L.、Song, C. 他(2025年)。グローバル fMRI 信号の自律生理学的結合。 <em>Nature Neuroscience</em>、28、1001-1014。 <a href="https://doi.org/10.1038/s41593-025-01945-y" target="_blank">doi:10.1038/s41593-025-01945-y</a></li>
<li>Epp、S.M.、Castrillon、G.、Yuan、B.、Andrews-Hanna、J.、Preibisch、C.、およびリードル、V. (2025)。大胆な信号変化は、人間の皮質全体の酸素代謝を妨げる可能性があります。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Li、X.、Zhu、X.-H.、Li、Y.、他。 (2025年)。動的重水素磁気共鳴分光イメージングを使用した、人間の脳における主要なグルコース代謝率の定量的マッピング。 <em>PNAS Nexus</em>、4(3)、pgaf072。 <a href="https://doi.org/10.1093/pnasnexus/pgaf072" target="_blank">doi:10.1093/pnasnexus/pgaf072</a></li>
<li>B'gh、N.、Vaeggemose、M.、Schulte、R.F.、他。 （2024年）。 3 T での健康なボランティアの重水素代謝イメージングの再現性。<em>European Radiology Experimental</em>、8、9。<a href="https://doi.org/10.1186/s41747-024-00426-4" target="_blank">doi:10.1186/s41747-024-00426-4</a></li>
<li>Morgan, C.A.、Thomas, D.L.、Shao, X.、他（2024年）。拡散処理およびマルチエコー動脈スピンラベリングを使用した血液脳関門の水交換率の測定: 定量値と年齢依存性の比較。 Biomedicine</em> の <em>NMR、37(12)、e5256。 <a href="https://doi.org/10.1002/nbm.5256" target="_blank">doi:10.1002/nbm.5256</a></li>
<li>Amiri, M.、Hermann, B.、M&aumltens, B.、他。 （2023年）。集中治療室における残留意識のマルチモーダル予測: CONNECT-ME 研究。 <em>Brain</em>、146(2)、645-661。 <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/ブレイン/awac335</a></li>
<li>Manasova, D.、Hermann, B.、Calligaris, C.、他。 （2026年）。意識障害における診断および予後マーカーの多角的多施設研究。 <em>ブレイン</em>。 <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/脳/awaf412</a></li>
<li>Bosch, C.、Ackels, T.、Pacureanu, A. 他（2022年）。相関生体内生理学、シンクロトロンマイクロトモグラフィー、体積電子顕微鏡法による脳組織の機能的かつマルチスケール 3D 構造研究。 <em>Nature Communications</em>、13、2923。<a href="https://doi.org/10.1038/s41467-022-30199-6" target="_blank">doi:10.1038/s41467-022-30199-6</a></li>
<li>MICrONS コンソーシアム、J.A. Bae、W.-C. Lee A.、ら。 (2025年)。マウス視覚野の複数の領域にわたる機能的コネクトミクス。 <em>Nature</em>、640、435-447。 <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gallego, J.A.、Perrich, M.G.、Chowdhury, R.H. 他（2020年）。一貫した動作の基礎となる皮質集団動態の長期安定性。 <em>Nature Neuroscience</em>、23、260-270。 <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">doi:10.1038/s41593-019-0555-4</a></li>
<li>Van De Ville、D.、Farouj、Y.、Preti、M. G.、Liégeois、R.、およびアミコ、E. (2021)。あなたをユニークにするとき: 人間の脳の指紋の一時性。 <em>Science Advances</em>、7(42)、eabj0751。 <a href="https://doi.org/10.1126/sciadv.abj0751" target="_blank">doi:10.1126/sciadv.abj0751</a></li>
<li>Karpowicz、B.M.、Ali、Y.H.、Wimalasena、L.N.、他(2025年)。潜在的なダイナミクスの調整を通じて脳とコンピューターのインターフェースを安定化します。 <em>Nature Communications</em>、16、4662。<a href="https://doi.org/10.1038/s41467-025-59652-y" target="_blank">doi:10.1038/s41467-025-59652-y</a></li>
<li>Wilson, G. H.、Stein, E. A.、Kamdar, F. 他(2025年)。隠れマルコフ モデルを使用した、カーソルベースの皮質内脳コンピューター インターフェイスの長期教師なし再調整。 <em>Nature Biomedical Engineering</em>。 <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Wairagkar, M.、Card, N.S.、Singer-Clark, T. 他(2025年)。瞬間的に音声を合成する神経人工器官。 <em>Nature</em>、644、145-152。 <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
</ol>

<h2>このプロセスから学んだこと、そしてまだ不明なこと</h2>
<table>
<thead>
<tr>
<th>私たちが知っていること</th>
<th>私たちがまだ知らないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>この用語は作業のどの段階に属しますか? </td>
<td>意識とアイデンティティを最終的に適切に説明するモデルはどれですか? </td>
</tr>
<tr>
<td>観察、推定、検証を混同しない読み方。 </td>
<td>非侵襲的な測定のみで WBE に関する十分な情報を取得することは可能ですか? </td>
</tr>
<tr>
<td>BIDS と QC が外部ではなくテクノロジーの一部であるのはなぜですか? </td>
<td>最終的にどのマルチモーダル統合が最適ですか? </td>
</tr>
<tr>
<td>なぜ逆問題論文は可視性、順モデル負荷、ソルバーの不確実性、検証クラスに分けられなければならないのか。 </td>
<td>どの逆ルートまたは検証ラダーが焦点または臨床ベンチマーク体制を超えて一般化されます。 </td>
</tr>
<tr>
<td>マルチモーダル言語、プロキシリッチ言語、または同一脳言語が強力に読み取られる前に、ルート カードとコンパニオン カードを分離する必要がある理由。 </td>
<td>フュージョン、ヒューマン プロキシ構成、状態継続ブリッジ、および識別可能性カードのどの組み合わせが、クロススタック クレームに対するサイトのデフォルトのフロントドア バンドルになる必要があります。 </td>
</tr>
</tbody>
</table>

<h2>次に戻る場所</h2>
<p>
簡単な定義に戻るには<a href="https://mind-upload.com/glossary.html">用語集</a>を、脳波の役割をもう一度読むには<a href="https://mind-upload.com/eeg_101.html">EEG</a>を、比較検証に進むには<a href="https://mind-upload.com/verification.html">検証インフラストラクチャ</a>を使用してください。
</p>
