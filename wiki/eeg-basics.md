---
layout: default
title: 'Wiki: 脳波の基礎'
description: 脳波とは何を測るのか、なぜ得意で何が苦手なのかを最初から解説していきます。
article_type: ウィキ
subtitle: 脳波検査が魔法の読心術にならないための基礎知識
author: マインドアップロード研究プロジェクト
last_updated: '2026-04-01'
note: 初心者ガイド
audience: 初めて脳波を学ぶ人、公開データや入門ページの前提を作りたい人
reading_time: 10～15分
page_intro: このページは脳波とは何を測るのかを基礎から解説するwikiです。複雑な数式を超えて、「`what kind of signals are mixed together and where'' and `」の前処理と QC
  がなぜ重要なのかを理解することが目標です。
accuracy_note: 脳波を過大評価しないように脳波の限界を強調しますが、それは役に立たないという意味ではありません。
page_highlights:
- EEG は頭皮で観察される混合電気信号です。
- 時間的変化には強いものの、空間識別や詳細な推定には限界があります。
- 基準システム、電極レイアウト、デバイスチェーン、およびプロトコルは、バックグラウンド実装の詳細ではなく、観察モデルの一部です。
- 頭皮で何かを予測できることと、脳内でソースを一意に決定できることは異なります。
- EEG ソースイメージングの進行は 1 つのはしごではありません。フィールドの可視性、フォワードモデル/伝導率負荷、ソルバーファミリーの不確実性、および検証クラスは分離されたままです。
- ソース空間接続と有向接続は、ソース位置特定よりもさらに強力な主張であり、別個の停止ルールが必要です。
- 同一セッションのマルチモーダル EEG 取得は自己検証されません。同期されたストリーム、共有されたクロスモーダルコンポーネント、およびターゲットの生物学的変数は、異なる成果のままです。
- ウェアラブル OPM-MEG は、ドロップインの自然主義的な読み取り値ではありません。シールドクラス、フィールドコントロール、キャリブレーション/位置合わせ、解剖学的ルート、クロストーク、およびタスクレジームが依然として請求の上限を形成しています。
- EEG-fMRI または EEG-PET-MRI 因子を共有しても、神経、自律神経、血管の寄与が混在する可能性があります。
- QC および前処理の記録は、結果の信頼性と上限を大きく決定します。
known_points:
- EEG は時間の変化をミリ秒単位で見るのが得意です。
- 観測された信号は多くの活動が混合した結果であり、解釈には仮定が必要です。
- 個別の MRI と外部参照を含めることで線源イメージングは​​改善されますが、深部および弱い線源については不確実性が残ります。
- より強力な EEG ソースイメージングペーパーは、他の問題を解決することなく、検出可能性、導電率校正、逆族不確かさレポート、または直接検証を向上させることができます。
- リファレンスの選択、録音セットアップ、チャネル レイアウトによって、ERP、接続性、およびデコードの結論が大きく変わる可能性があります。
- アーティファクトのクリーンアップだけでは、ソース漏洩を解決したり、有向接続を因果関係の証明に変えたりすることはできません。
- fMRI、PET、またはその他のモダリティを追加すると、融合の妥当性、共有因子の特異性、およびバンドルの堅牢性が未解決のままのまま、1 つの監査レイヤーを強化できます。
- ウェアラブル OPM-MEG は、指定されたシールド、フィールド制御、キャリブレーション、解剖学的構造、クロストーク、およびタスク体制条件下でのみ、運動耐性マクロ電気生理学を強化します。
- 公開データは、前処理とベースライン比較に関する豊富な練習を提供します。
unknown_points:
- 脳内の詳細な因果構造を再構築するのに非侵襲的EEGだけで十分であるかどうかは未解決のままである。
- 前処理の選択によって、各タスクの結論が一律に変わるわけではありません。
- どの外部ベンチマークがソース イメージングの標準検証セットになるかはまだ決まっていません。
- ウェアラブル OPM-MEG が、シールドされた概念実証や狭いタスク領域を超えてどこまで一般化するかは未解決のままです。
wiki_links:
- label: 'Wiki: WBE の基本'
  url: /wiki/mind-upload-basics.html
  description: まず EEG が全体的な WBE のどこに当てはまるかを確認したい場合は、ここをクリックしてください。
- label: 'Wiki: EEG の前処理と QC'
  url: /wiki/eeg-preprocessing-and-qc.html
  description: 前処理とロギングの方法を実践的に整理していきます。
- label: 'Wiki: 検証インフラストラクチャの基本'
  url: /wiki/verification-basics.html
  description: EEG にも標準と QC が必要な理由を理解します。
- label: 'Wiki: 観察から推定へ'
  url: /wiki/observation-to-estimation.html
  description: ESI、DCM、および SCM の制限をまとめて整理する場合は、このページを使用します。
- label: 'Wiki: マルチモーダル統合の基本'
  url: /wiki/multimodal-integration-basics.html
  description: EEG を fMRI、PET、MEG、または侵襲的記録と組み合わせ始める場合は、このページを使用してください。
recommended_pages:
- label: 脳波検査の概要
  url: /eeg_101.html
- label: データとベンチ
  url: /datasets.html
- label: 実践
  url: /datasets.html#l0-practice
---
<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>脳波では何が見えますか?</h2>
<p>
脳波検査は、頭皮に配置された電極を使用して電位差を測定する方法です。言い換えれば、私たちはカメラで脳を直接覗いているのではなく、多くの活動が重なり合った結果として外部に送信される混合信号を読み取っているのです。
</p>
</div>

<div class="note-box">
<strong>このページで最初に停止するスイッチ</strong>
<p>
EEG では、<strong> 頭皮信号の観察 </strong>、<strong> 条件付きで脳ソースを推定する </strong>、<strong> 相互作用を推定する </strong>、<strong> 内部状態を独自に識別する </strong> とは異なります。これらを混同すると、初心者は「見た」と「推定した」を同じものであるかのように読んでしまいます。
</p>
</div>

<div class="note-box">
<strong>2026-03初心者ルート修正</strong>
<p>
このサイトの古い初心者ルートは、「EEG が混在しており、信号源のイメージングが難しい」で停止していました。それは弱すぎました。 EEG の場合、<strong> 測定条件そのもの </strong> が重要です。基準システム、電極レイアウト、デバイス チェーン、プロトコルによって、頭皮信号の意味が変わることもあります。また、<strong> 接続マップや有向グラフ </strong> は、センサー トレースやソース推定よりも強力な主張であることを、より明確に伝える必要もありました。
</p>
</div>

<div class="note-box">
<strong>別のモダリティを追加してもEEGは解決済み状態メーターにはなりません</strong>
<p>
次に停止すべき初心者向けショートカットは、<strong>multimodal</strong> という単語です。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">Kothe et al. (2025)</a> は、デバイス側の遅延の真実ではなく、LSL を同期インフラストラクチャとして説明しています。<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024) </a> は、同時マルチモーダル記録が共通の組織と発散的な組織の両方を保持していることを示しています。 (2025)</a> は、EEG-PET-MRI を同時に行うと、結合した全体的なダイナミクスとモダリティ固有の構造が含まれる可能性があることを示しています。したがって、EEG が他のスタックと組み合わされた場合でも、サイトは <strong> 同期取得 </strong>、<strong> 共有統計構造 </strong>、および <strong> 外部で校正された生物学的変数 </strong> を 1 つの成果として扱うのではなく、依然として分離します。
</p>
</div>
<div class="note-box">
<strong>2026-04-01 訂正: ウェアラブル OPM-MEG はポータブル フリーパスではありません</strong>
<p>
初心者ルートには、<strong>wearable MEG</strong> という粗いオブジェクトが 1 つ残っていました。現在の一次文献では、<strong>not</strong> は、動作許容度によってシールド、フィールド制御、解剖学的構造、および校正の負担が自動的に除去されたかのように OPM-MEG を扱うことをサポートしています。 <a href="https://doi.org/10.1038/nature26147" target="_blank">Boto et al. (2018) </a> はウェアラブルの実現可能性を確立しましたが、背景フィールド制御なしでは飽和リスクも示しました。 <a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">Reaら(2021)</a> および <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">Mellor et al. (2022)</a> は、精密フィールド モデリングとヌリングがそのルートの一部であることを示しています。<a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">Holmes et al. (2025)</a> は、軽くシールドされた動作が依然としてアクティブ補償と tSSS に依存していることを示しています。<a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">Rhodes et al. (2025)</a> は、擬似 MRI は有用であるが、ゴールドスタンダードとしての個別の MRI に代わるものではないことを示しています。<a href="https://doi.org/10.1063/5.0273491" target="_blank">Wu et al. (2025)</a> は、クロストークが依然としてアレイレベルの負担であることを示し、<a href="https://doi.org/10.3390/s25134160" target="_blank">Spedden らは、 (2025) </a> は、狭い感覚運動ベータ課題の下で 3 人の健康な成人のみで全身ステッピングの実行可能性を示しました。したがって、この初心者ページでも、論文が強化する<strong>フィールドコントロール</strong>、<strong>軽量シールド展開</strong>、<strong>MRIライト解剖学置換</strong>、<strong>アレイ工学</strong>、それとも<strong>狭いタスクの概念実証</strong>のみを強化するのか、というのが最低限の安全な質問です。その分割がなければ、<strong>wearable OPM-MEG</strong> は粗すぎるオブジェクトです。
</p>
</div>

<section class="section" id="strengths">
<h2 class="section-title">EEG の得意分野</h2>
<table class="data-table">
<thead>
<tr>
<th>得意なこと</th>
<th>理由</th>
</tr>
</thead>
<tbody>
<tr>
<td>時間の経過による変化を見る</td>
<td>EEG はミリ秒単位で信号をキャプチャできるため、変化がいつ発生したかを追跡するのが簡単です。 </td>
</tr>
<tr>
<td>状態遷移とイベント検出</td>
<td>睡眠段階や発作事象など、時間とともに変化する状態の観察に適しています。 </td>
</tr>
<tr>
<td>公開データによる複製実践</td>
<td>PhysioNet には標準データがあり、簡単に L0 の練習を始めることができます。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="limits">
<h2 class="section-title">脳波が苦手なもの</h2>
<table class="data-table">
<thead>
<tr>
<th>苦手なこと</th>
<th>なぜ難しいのか</th>
</tr>
</thead>
<tbody>
<tr>
<td>「脳のどこか」を正確に表現</td>
<td>これは、信号が頭蓋骨や頭皮を通過する際にぼやけてしまい、逆問題を一意に解くことができないためです。 </td>
</tr>
<tr>
<td>深層構造を詳しく知る</td>
<td>頭皮から遠く離れた活動や微弱な信号の観測が困難です。 </td>
</tr>
<tr>
<td>脳波のみを使用してアイデンティティを強く主張する</td>
<td>EEGは重要な手がかりですが、それだけでは記憶や価値観、因果関係の連続性を確認することはできません。 </td>
</tr>
<tr>
<td>T接続マップまたは有向グラフを発見された因果関係として扱う</td>
<td>Reference の選択、センサーの混合、ソースの漏れ、分割、および外部検証の欠落はすべて、波形がきれいに見えた後でもネットワークの結果を変える可能性があります。 </td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="observability">
<h2 class="section-title">観察・推定・同定は異なります</h2>
<table class="data-table">
<thead>
<tr>
<th>ステージ</th>
<th>EEG</th>で言えること
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察</strong></td>
<td>頭皮上の混合電位をmsスケールで測定できます。状態遷移やイベント時間の追跡に優れています。 </td>
<td>細胞の種類や神経細胞の修飾など、どの深部原因が唯一の原因であるかを直接観察したとは言えません。 </td>
</tr>
<tr>
<td><strong>条件付き推定</strong></td>
<td> 個別の MRI、電極座標、およびフォワード モデルを含めることで、皮質付近および一部の深部の活動の推定が向上します。 </td>
<td>深刻な状態を検出できることと、一般に一意性を復元できることは異なります。 </td>
</tr>
<tr>
<td><strong>ネットワーク/有向接続の見積もり</strong></td>
<td>ソース モデリング、分割、および明示的なメトリクスを使用すると、純粋なセンサー レベルよりも強力に条件付き相互作用構造を推定できます。 </td>
<td>それでも、領域間結合や因果方向に漏れがないことは証明されていません。接続と有向接続には、独自の検証ルールと棄権ルールが必要です。 </td>
</tr>
<tr>
<td><strong>識別</strong></td>
<td>頭蓋内刺激、同時 SEEG/ECoG、ファントム、術後の転帰などの外部基準により、エラー監査が可能になります。 </td>
<td>外部基準がなければ「`I have found the source'' or `」は「WBEとして十分な状態に達した」とは言えません。
</tr>
</tbody>
</table>

<div class="note-box">
<strong>2026-03 実測証拠</strong>
<p>
シーバーら。 (2019) は、256ch 頭皮脳波と同時 DBS 記録による皮質下信号の検出可能性を実証しましたが、一般的な独自の再構成については主張しませんでした。 Unnwongse et al. (2023) は、頭蓋内刺激の直接検証において、位置特定エラーが頭蓋伝導率とソースの深さに依存すると報告しました。 (2025) は、同時 HD-EEG/SEEG の 29 件のエラーにソースパワーとソース深度が強く影響することを示しました。したがって、正しい読み方は「`partially auditable if the conditions are strictly fixed'', not `『脳波だけで脳の情報源を独自に読み取ることができる』」となります。
</p>
</div>

<div class="note-box">
<strong>2026-03-30 再監査: 脳波ソースイメージングの改善には依然として 4 つの異なる進歩がある</strong>
<p>
この初心者向けページには、もう 1 つ修正が必要でした。現在の主な文献では、<strong>not</strong> は、すべての EEG ソース イメージングの進行状況を 1 つの連続したラダーとして読み取ることをサポートしています。 <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeberら。 (2019) </a> は、<strong> フィールド形成の可視性を強化します。</strong> は、特定の皮質下領域に対して、<a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a> および <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerk ら。 (2026)</a> は、<strong> 組織と頭蓋骨の導電率の仮定 </strong> が依然として結果を実質的に動かすことを示しています。<a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>、<a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tong 他(2025)</a>、<a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng et al。 (2025) </a> は、明示された逆ファミリー </strong> および <a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank"> 内の <strong> 不確実性曝露を強化する Pascarella et al。 (2023)</a>、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse 他(2023)</a>、<a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025) </a> は、1 つの普遍的なソース回復要求ではなく、<strong> さまざまなソース体制とエラー オブジェクト </strong> を検証します。したがって、このサイトでは、「より良い ESI 結果」が 1 つの進行状況バーではなく 4 つのフロアで表示されるようになりました。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>脳波ソースイメージング用の4フロアスプリット</th>
<th>何が強くなったのか</th>
<th>代表的な一次論文</th>
<th>まだ買えないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1。フィールド形成の可視性</strong></td>
<td>ターゲット ソース クラスが特定の深さ、方向、範囲、モンタージュ領域でセンサーに到達するかどうか。</td>
<td><a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019)</a></td>
<td>それ自体では、導電率感度、逆族拡散、または一般的なソース回復は修正されません。</td>
</tr>
<tr>
<td><strong>2。前進モデル/導電性負担</strong></td>
<td>頭蓋骨または組織の導電率と幾何学的仮定が、どの程度の位置、深さ、または振幅を動かすか。</td>
<td><a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a>; <a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">Vorwerkら(2026)</a></td>
<td>導電率による拡散を低減すること自体は、ソルバー ファミリまたは検証レジームが十分であることを証明するものではありません。
</tr>
<tr>
<td><strong>3。ソルバーファミリーの不確実性</strong></td>
<td>逆ファミリーが事後幅、代替構成、偏りのない間隔、または不確実性マップをどの程度明確に報告するか。</td>
<td><a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a>; <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">Tongら(2025)</a>; <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Fengら(2025)</a></td>
<td>不確実性エクスポージャーの改善は、それ自体で報告された候補が外部的に正しいことを証明するものではありません。</td>
</tr>
<tr>
<td><strong>4。検証クラス</strong></td>
<td>実際に合格した外部基準: 焦点源比較、頭蓋内刺激、同時侵襲的記録、または別の体制固有のラダー。</td>
<td><a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">パスカレラら(2023)</a>; <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse 他(2023)</a>; <a href="https://doi.org/10.1111/epi.18552" target="_blank">ハオら。 (2025)</a></td>
<td>A 1 つのソース レジームでの直接検証の結果は、すべての深さ、ソース範囲、または臨床設定に自動的に転送されません。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Connectivity は単なる脳波出力の 1 つではありません</strong>
<p>
ソース推定値が存在すると、接続性グラフは次の概要にすぎないと考えたくなります。それは強すぎます。ヴィンクら。 (2011) は wPLI をラグゼロ混合に対してより安全にしましたが、Haufe et al. Palva et al. (2013) は、センサーと空間の接続が体積伝導によって依然として強く制限されていることを示しました。 (2018) は、ソース空間の測定であってもゴースト相互作用を引き起こす可能性があることを示しました。 (2025) は、センサー空間ネットワークの結果が、再参照、エポックデザイン、およびメトリックの選択によって変化することを示しました。したがって、このサイトでは、EEG 接続は、自動的に検出された配線としてではなく、<strong> モデルおよびパイプライン条件付き推定器 </strong> として解釈されます。
</p>
</div>
</section>

<section class="section" id="pipeline">
<h2 class="section-title">QC と前処理が重要な理由</h2>
<p>
EEG はノイズの影響を受けやすい測定ですが、重要な修正は、問題はノイズだけではないということです。結果は、まばたき、筋電位、体の動き、電源ノイズ、<strong> 基準選択</strong>、<strong> 電極レイアウト</strong>、<strong> デバイス側フィルタリング</strong>、<strong> 部位固有セットアップ</strong> によって変化する可能性があります。したがって、単にきれいな体型を保つだけでは十分ではありません。また、その数値を可能にした測定条件も記録する必要があります。
</p>
<div class="key-points">
<h4>最低限抑えておきたいこと</h4>
<ul>
<li><strong>参考方法：</strong>電位差の測定に使用した基準は何ですか? </li>
<li><strong>記録セットアップ:</strong>どのデバイスチェーン、サンプリングポリシー、電極レイアウトが使用されましたか? </li>
<li><strong>フィルター:</strong>どの周波数帯域を通過させますか？ </li>
<li><strong>アーティファクト処理:</strong>どのノイズをどのように除去しましたか? </li>
<li><strong>除外基準:</strong>除外されたデータとその理由? </li>
</ul>
</div>

<div class="note-box">
<strong>同じタスクでも同じ測定条件を保証するものではありません</strong>
<p>
徐ら。 (2020) は、クロスデータセットの深層学習の結果が、アンプ、キャップ、サンプリング レート、フィルタリングなどの環境変動に応じて変化することを示しました。このため、このサイトではセットアップをバックグラウンドでの迷惑行為として扱いません。これは観察モデルの一部であり、スコアが解釈される前にログに記録する必要があります。
</p>
</div>

<div class="note-box">
<strong>共有された多峰性因子は依然として混合生理学である可能性がある</strong>
<p>
論文で 1 つの一般的な EEG-fMRI 因子または EEG-PET-MRI 因子が報告されている場合でも、その因子には神経系と非神経系の寄与が混在している可能性があります。 <a href="https://doi.org/10.1162/imag_a_00287" target="_blank">ゴールド他(2024) </a> は、EEG-fMRI と自律神経の同時記録において、警戒が低下するにつれて fMRI と自律神経の共分散が増大することを示しています。<a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">Özbay et al。 (2019)</a> は fMRI 信号に対する交感神経の寄与を示し、<a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">Epp et al. (2025) </a> は、大胆な変更が皮質の大部分にわたる酸素代謝の変化に対抗できることを示しています。したがって、このサイトでは、共通因子はターゲットの神経変数に自動的にプロモートされません。
</p>
</div>
</section>

<section class="section" id="wbe-link">
<h2 class="section-title">WBE</h2>との接続方法
<p>
EEG は、突然 WBE を完了するデバイスではありません。ただし、状態の変化に関する時間情報、ベースラインの比較、公開データとの再現性を提供するためには重要です。 Mind-Upload では、脳波をすべてを読み取る装置としてではなく、巨視的な制約を与える観察ツールとして扱います。実際的な結果は、EEG 結果が宣伝される前に、<strong> 測定条件、ソースイメージング フロア (可視性 / 導電率 / ソルバーの不確実性 / 検証クラス)、および接続上限 </strong> をすべて個別に開示する必要があるということです。
</p>
<div class="note-box">
<strong>マルチモーダルバンドルが実際よりも強く見えるとき</strong>
<p>
モダリティを増やすと、バンドルがまだ脆弱なままでも予測を改善できます。 <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">ローハウトら。 (2024) </a> は実際の多峰性予後利益を示していますが、<a href="https://doi.org/10.1093/brain/awac335" target="_blank">Amiri et al. (2023)</a> および <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">Manasova et al. (2026) </a> は、同一サンプル分析、欠落モダリティの処理、施設間移行、およびモダリティ間の不一致が依然として重要であることを示しています。そのため、このサイトは、EEG プラスその他のスタック引数を <a href="../verification.html#fusion-card">Fusion Card</a> 経由でルーティングし、生きている人間のプロキシ行が混在する場合は、<a href="../verification.html#human-proxy-composition-card">Human Proxy Composition Card</a> も経由します。
</p>
</div>
<div class="cta-box">
<h4>次</h4>
<p> ここをクリックして、主張と証拠の強さに基づく脳波に関する研究をご覧ください。 </p>
<a href="claims-and-evidence.html">クレームと証拠の読み方→</a>
</div>

<div class="cta-box">
<h4>実用的な次へ</h4>
<p>参照メソッド、フィルター、アーティファクト処理で何が変わるのかを実践的な観点から確認したい場合は、ここをクリックしてください。 </p>
<a href="eeg-preprocessing-and-qc.html">脳波前処理とQCへ→</a>
</div>

<div class="cta-box">
<h4>テクニカルネクスト</h4>
<p>観測と推定の境界、ESI、DCM、SCMの関係を知りたい方はこちら。 </p>
<a href="measurement-and-modeling-terms.html">測定からモデリングまで→</a>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考資料</h2>
<ol>
<li>Pernet, C.R.、Appelhoff, S.、Gorgolewski, K.J. 他（2019年）。 EEG-BIDS、脳波検査用の脳画像データ構造の拡張。 <em>S科学的データ</em>、6、103。<a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C.、Garrido, M.I.、Gramfort, A. 他（2020年）。再現可能なEEGおよびMEG研究のためのOHBM COBIDAS MEEG委員会からの問題と推奨事項。 <em>Nature Neuroscience</em>、23、1473-1483。 <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>ミシェル、C.M.、＆amp;ブルーネット、D. (2019)。 EEG ソース イメージング: 分析ステップの実践的なレビュー。 <em>神経学の最前線</em>、10、325。<a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Mikulan, E.、Russo, S.、Bares, M.、他（2020年）。人間の脳内刺激と HD-EEG の同時、音源位置特定方法のグラウンドトゥルース。 <em>S科学データ</em>、7、127。<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Seeber, M.、Cantonas, L.-M.、Hoevels, M.、他。 （2019年）。皮質下の電気生理学的活動は、高密度EEGソースイメージングで検出可能です。 <em>Nature Communications</em>、10、753.<a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse、K.、Achakulvisut、T.、Wu、J.Y.、他。 （2023年）。人間の患者における頭蓋内電気刺激によるEEGソースイメージングの直接検証。 <em>ブレインコミュニケーションズ</em>、5(2)、fcad023。 <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/ブレインコム/fcad023</a></li>
<li>Hao, S.、Zhao, H.、Feng, Z. 他(2025年)。薬剤耐性てんかんにおける HD-EEG ソースイメージングと同時 SEEG 記録。 <em>てんかん</em>、66(11)、4451-4464。 <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Pascarella, A.、Mikulan, E.、Sciacchitano, F.、他。 （2023年）。焦点ソースを使用した ESI メソッドの生体内検証。 <em>NeuroImage</em>、277、120219.<a href="https://doi.org/10.1016/j.neuroimage.2023.120219" target="_blank">doi:10.1016/j.neuroimage.2023.120219</a></li>
<li>Vorwerk、J.、Wolters、C.H.、&amp;バウムガルテン、D. (2024)。組織の伝導率の不確実性に対するEEGソース分析のグローバルな感度。 <em>人間の神経科学のフロンティア</em>、18、1335212。<a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">doi:10.3389/fnhum.2024.1335212</a></li>
<li>Luria, G.、Viani, S.、Pascarella, A. 他（2024年）。 SESAMEEG パッケージ: M/EEG における信号源の位置特定と不確実性の定量化のための確率的ツール。 <em>人間の神経科学のフロンティア</em>、18、1359753.<a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">doi:10.3389/fnhum.2024.1359753</a></li>
<li>Tong、P. F.、Yang、H.、Ding、X.、他(2025年)。時空間 EEG/MEG ソース イメージングのための偏りのない推定と推論。 <em>医用画像に関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TMI.2024.3506596" target="_blank">doi:10.1109/TMI.2024.3506596</a></li>
<li>Feng, Z.、Mishne, G.、Hashemi, A. 他(2025年)。 Block-Champagne: 経験的なベイジアン不確実性定量化を使用した拡張 E/MEG ソース活性化のイメージング。 <em>医用画像に関するIEEEトランザクション</em>。 <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Vorwerk, J.、K&ouml;hler, T.、G&uuml;llmar, D. 他（2026年）。てんかんの術前評価における信号源分析を改善するための EEG および EEG/MEG 頭蓋骨伝導率推定の可能性。 <em>Journal of Neural Engineering</em>、23(1)、016007.<a href="https://doi.org/10.1088/1741-2552/ae2f01" target="_blank">doi:10.1088/1741-2552/ae2f01</a></li>
<li>Xu、M.、Yao、S.、Wei、Z.、他。 （2020年）。深層学習による EEG デコードにおけるデータセット間の変動性の問題。 <em>人間の神経科学のフロンティア</em>、14、103.<a href="https://doi.org/10.3389/fnhum.2020.00103" target="_blank">doi:10.3389/fnhum.2020.00103</a></li>
<li>Vinck、M.、Oostenveld、R.、van Wingerden、M.、Battaglia、F.、およびPennartz、C.M.A. (2011)。体積伝導、ノイズ、サンプルサイズのバイアスが存在する場合の電気生理学的データの位相同期の指標が改善されました。 <em>NeuroImage</em>、55(4)、1548-1565。 <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>ハウフェ、S.、ニクリン、V.V.、ミュラー、K.-R.、&amp;ノルテ、G. (2013)。 EEG データの接続性測定の重要な評価: シミュレーション研究。 <em>NeuroImage</em>、64、120-133。 <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva, J.M.、Wang, S. H.、Palva, S.、他（2018年）。 MEG/EEG ソース空間におけるゴースト インタラクション: エリア間のカップリング対策に関する注意事項。 <em>NeuroImage</em>、173、632-643。 <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Miljevic、A.、Murphy、O.W.、Fitzgerald、P.B.、およびニューウェスト州ベイリー (2025)。センサー空間の EEG 接続性の推定 パート 1: シミュレートされたデータにおける機能的接続性の最もパフォーマンスの高い方法を特定します。 <em>C臨床神経生理学</em>、174、73-83。 <a href="https://doi.org/10.1016/j.clinph.2025.03.043" target="_blank">doi:10.1016/j.clinph.2025.03.043</a></li>
<li>Kothe, C.、Shirazi, S. Y.、Stenner, T. 他(2025年)。同期されたマルチモーダル記録のためのラボ ストリーミング レイヤー。 <em>画像神経科学</em>、3、IMAG.a.136。 <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Vafaii、H.、Mandino、F.、Desrosiers-Grégoire、G.、他。 （2024年）。自発的な脳活動の多峰性測定により、皮質機能組織の共通パターンと多様なパターンの両方が明らかになります。 <em>Nature Communications</em>、15、581.<a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">doi:10.1038/s41467-023-44363-z</a></li>
<li>Chen、J. E.、Lewis、L. D.、Coursey、S. E.、他(2025年)。 EEG-PET-MRI を同時に行うことで、覚醒時とノンレム睡眠時の時間的に結合し、空間的に構造化された脳のダイナミクスを特定します。 <em>Nature Communications</em>、16、8887。<a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">doi:10.1038/s41467-025-64414-x</a></li>
<li>Gold, B.P.、Goodale, S.E.、Zhao, C. 他（2024年）。機能的 MRI 信号は、警戒が低下するにつれて、末梢自律神経の測定値とのより強い共変動を示します。 <em>イメージング神経科学</em>、2、IMAG.a.00287。 <a href="https://doi.org/10.1162/imag_a_00287" target="_blank">doi:10.1162/imag_a_00287</a></li>
<li>Özbay, P.S.、Chang, C.、Picchioni, D. 他（2019年）。交感神経活動は fMRI 信号に寄与します。 <em>コミュニケーション生物学</em>、2、421。<a href="https://doi.org/10.1038/s42003-019-0659-0" target="_blank">doi:10.1038/s42003-019-0659-0</a></li>
<li>Epp、S.M.、Castrillon、G.、Yuan、B. 他(2025年)。大胆な信号変化は、人間の皮質全体の酸素代謝を妨げる可能性があります。 <em>Nature Neuroscience</em>。 <a href="https://doi.org/10.1038/s41593-025-02132-9" target="_blank">doi:10.1038/s41593-025-02132-9</a></li>
<li>Rohaut, B.、Hermann, B.、Kaufmann, B. C.、他。 （2024年）。マルチモーダル評価は、臨床的に反応性のない脳損傷のある救命救急患者の神経予後成績を改善します。 <em>Nature Medicine</em>、30、2482-2491。 <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Amiri、M.、Bødker Andersen、M.、Jørgensen、S.H.、他（2023年）。集中治療室における残留意識のマルチモーダル予測: CONNECT-ME 研究。 <em>ブレイン</em>、146(1)、50-64。 <a href="https://doi.org/10.1093/brain/awac335" target="_blank">doi:10.1093/ブレイン/awac335</a></li>
<li>Manasova, D.、Belloli, L.M.L.、Rosenfelder, M.J. 他（2026年）。意識障害における診断および予後マーカーの多角的多施設研究。 <em>脳</em>。 <a href="https://doi.org/10.1093/brain/awaf412" target="_blank">doi:10.1093/ブレイン/awaf412</a></li>
<li>Boto, E.、Holmes, N.、Leggett, J. 他（2018年）。ウェアラブル システムを使用して、脳磁図を現実世界のアプリケーションに移行します。 <em>ネイチャー</em>、555、657-661。 <a href="https://doi.org/10.1038/nature26147" target="_blank">ドイ:10.1038/nature26147</a></li>
<li>Rea、M.、Holmes、N.、Hill、R.M.、他。 （2021年）。ウェアラブル脳磁計のための高精度の磁場のモデリングと制御。 <em>NeuroImage</em>、241、118401.<a href="https://doi.org/10.1016/j.neuroimage.2021.118401" target="_blank">doi:10.1016/j.neuroimage.2021.118401</a></li>
<li>Mellor, S.J.、Tierney, T.M.、O'Neill, G.C. 他（2022年）。可動OP-MEGの磁場マッピングと補正。 <em>IEEE Transactions on Biomedical Engineering</em>、69(2)、528-536。 <a href="https://doi.org/10.1109/TBME.2021.3100770" target="_blank">doi:10.1109/TBME.2021.3100770</a></li>
<li>Holmes, N.、Leggett, J.、Hill, R.M.、他(2025年)。軽く遮蔽された環境でのウェアラブル脳磁計。 <em>IEEE Transactions on Biomedical Engineering</em>、72(2)、609-618。 <a href="https://doi.org/10.1109/TBME.2024.3465654" target="_blank">doi:10.1109/TBME.2024.3465654</a></li>
<li>Rhodes, N.、Rier, L.、Boto, E.、Hill, R.M.、およびM.J.ブルックス (2025)。光ポンピング磁力計ベースの脳磁図法を使用した、MRI を使用しない信号源再構成。 <em>画像神経科学</em>、3、IMAG.a.8。 <a href="https://doi.org/10.1162/IMAG.a.8" target="_blank">doi:10.1162/IMAG.a.8</a></li>
<li>Wu, T.、Xiao, W.、Peng, X.、Wu, T.、およびGuo、H. (2025)。生体磁気測定用の光ポンピング磁力計アレイにおけるクロストークの低減。 <em>科学機器のレビュー</em>、96(8)、085004。<a href="https://doi.org/10.1063/5.0273491" target="_blank">doi:10.1063/5.0273491</a></li>
<li>Spedden、M.E.、O'Neill、G.C.、West、T.O.、他。 (2025年)。ウェアラブル MEG を使用して人間の歩行動作の神経制御を研究します。 <em>センサー</em>、25(13)、4160。<a href="https://doi.org/10.3390/s25134160" target="_blank">doi:10.3390/s25134160</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBE 基本→</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG 前処理と QC →</a></li>
<li><a href="measurement-and-modeling-terms.html">測定からモデリングまで→</a></li>
<li><a href="verification-basics.html">検証基盤の基礎→</a></li>
<li><a href="claims-and-evidence.html">クレームと証拠の読み方→</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>リファレンス</h4>
<ul>
<li><a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">ミシェル＆amp;ブルネット (2019)</a></li>
<li><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">ミクランら(2020)</a></li>
<li><a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019)</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2024.1335212" target="_blank">Vorwerk et al. (2024)</a></li>
<li><a href="https://doi.org/10.3389/fnhum.2024.1359753" target="_blank">Luria et al. (2024)</a></li>
<li><a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a></li>
<li><a href="https://doi.org/10.1111/epi.18552" target="_blank">ハオら(2025)</a></li>
<li><a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">Feng 他(2025)</a></li>
<li><a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">ハウフェら(2013)</a></li>
<li><a href="https://doi.org/10.1038/s41467-023-44363-z" target="_blank">Vafaii et al. (2024)</a></li>
<li><a href="https://doi.org/10.1038/s41467-025-64414-x" target="_blank">チェンら(2025)</a></li>
<li><a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">Rohaut et al. (2024)</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG 101 →</a></li>
<li><a href="../datasets.html">データ＆ベンチ→</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン→</a></li>
</ul>
</div>
</aside>
</main>
