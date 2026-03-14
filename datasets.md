---
layout: default
title: "データ & ハンズオン：何で始めて、どうL0まで持っていくか"
description: "公開データ（EEG中心）の選定から、BIDS→QC→前処理→評価の最小ループまでを1ページで整理します。"
article_type: Resource
subtitle: "「何を使うか」と「どう再現するか」を分けずに最短ルートでつなぐ"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Curated List + L0 Practice"
audience: "どの公開データから始めるべきか迷っている人、L0の練習台を探している人"
reading_time: "12〜20分"
page_intro: "このページは、『最初にどの公開データで検証を始めるか』と『その後どうL0の再現可能解析まで持っていくか』を1本で追うための実務ガイドです。データ名の一覧で終わらせず、BIDS、QC、分割、ベースラインまで一本道でつなぎます。"
accuracy_note: "ここに載せるデータセットは入口候補です。使いやすさや再現性の観点で挙げており、これだけでWBEの全課題を覆えるわけではありません。"
page_highlights:
  - "まずは共有基盤を押さえ、その後にスターターデータセットを見る順にしています。"
  - "スターターデータは L0〜L1 の練習台であり、EEG source imaging の ground truth ではありません。"
  - "最終目標は、第三者が同じ条件で走らせられる形へ寄せることです。"
known_points:
  - "公開 EEG データは、L0 の再現解析や L1 のベースライン練習に十分役立ちます。"
  - "最初のデータ選びでは、難しさよりも追試しやすさを優先した方が前に進みます。"
  - "個体別 MRI や侵襲 ground truth がないスターターデータだけで、ESI 精度改善を強く主張することはできません。"
unknown_points:
  - "スターターデータセットだけで WBE の全論点を解くことはできません。"
  - "どのデータが将来の因果・閉ループ検証へ最も効くかは、まだ固定していません。"
  - "どの公開データが source imaging の direct validation 用 benchmark として最も運用しやすいかは、まだ固定していません。"
wiki_links:
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "データセットを見る前に、EEG の信号そのものを理解したい人向けです。"
  - label: "Wiki: L0で最低限そろえる成果物パック"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "BIDS、QC、分割、ベースライン、実行手順など、L0 の提出物を整理します。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "なぜデータだけでなくベンチや登録が必要かを学べます。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "train/test の分け方と、よくあるリーク事故を初歩から説明します。"
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "raw EEG だけでは足りない理由を、イベントと同期の観点から説明します。"
  - label: "Wiki: マルチモーダル統合の基本"
    url: "/wiki/multimodal-integration-basics.html"
    description: "EEG に何を足すと何が補えるかを、初歩から整理します。"
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "BIDS、OpenNeuro、Validator、Benchmark の役割差を整理します。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Use</h2>
<p>
このページは、「最初にどのデータで練習すればよいか」を決めるための実用リストです。まずは公開データで、<strong>同じ結果を再現できる状態（L0）</strong>を作り、その次に<strong>予測できるか・条件変更に耐えるか（L1〜L2）</strong>を確かめます。
</p>
</div>

<div class="note-box">
<strong>選び方の基準</strong>
<p>
最初のデータ選びで大事なのは、「すごく難しいデータ」よりも「手順と結果を他の人が追いやすいデータ」です。最初から全部を狙わず、まずは再現しやすい公開データで最小ループを作るのが近道です。
</p>
</div>
<div class="note-box">
<strong>実務系ページの中での位置づけを知りたいとき</strong>
<p>
このページは、何で始めるかを決める入口と、L0 の最小ループを一周させる手順をまとめた実務ページでございます。何を前進と呼ぶかは <a href="verification.html">検証基盤</a>、他分野の成功例は <a href="verification.html#casework">検証基盤内のケースワーク節</a> が担当します。実務系ページだけの役割差を 1 枚で見たい場合は <a href="wiki/practical-pages-reading-guide.html">Wiki: 実務系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>このページだけで完了させたいとき</strong>
<p>
旧 <code>hands_on.md</code> の最小ループ手順は本ページへ統合しました。したがって、データ選定のあとに別ページへ移らなくても、L0 の骨格、QC、ベースライン、完了条件までそのまま読み進められます。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>やりたいこと</th>
<th>最初に向くデータ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>前処理と分類の基本を練習したい</strong></td>
<td><strong>EEG Motor Movement/Imagery</strong> が入りやすいです。問題設定が比較的分かりやすく、L0〜L1の練習台に向きます。</td>
</tr>
<tr>
<td><strong>長時間データやイベント検出を触りたい</strong></td>
<td><strong>CHB-MIT</strong> が向きます。ノイズや長時間記録の扱いまで含めて練習できます。</td>
</tr>
<tr>
<td><strong>状態遷移を扱いたい</strong></td>
<td><strong>Sleep-EDF</strong> が向きます。状態が時間でどう移るかを見る練習になります。</td>
</tr>
<tr>
<td><strong>大規模データの難しさまで見たい</strong></td>
<td><strong>TUH EEG</strong> が候補です。ただし最初の一本としては重いので、前の3つで慣れてからが安全です。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>最初のデータ選びで期待しすぎないために</strong>
<p>
スターターデータセットは、WBE の全課題を一気に解くためのものではありません。ここでまず得たいのは、<strong>再現可能な入力整理</strong>、<strong>QC の習慣</strong>、<strong>ベースライン比較</strong>です。本人性や因果同一性のような強い論点まで、この段階のデータだけで片付くわけではありません。
</p>
</div>

<div class="note-box">
<strong>精度より先に見ること</strong>
<p>
データセット紹介を見ると、つい「何% 出たか」に目が向きます。しかし最初に確認すべきなのは、<strong>train/test を何単位で分けたか</strong>、<strong>リーク検査をしたか</strong>、<strong>単純なベースラインと比べたか</strong>です。ここで迷う場合は <a href="wiki/dataset-splits-and-leakage.html">Wiki: データ分割とデータリーク</a> を先に読むと判断しやすくなります。
</p>
</div>
<div class="note-box">
<strong>L0 で何を一式そろえるか迷ったとき</strong>
<p>
データ名だけ決めても、提出物の形が曖昧だと止まりやすいです。BIDS、Validator、QC ログ、分割規則、ベースライン、実行手順、失敗例を 1 枚で見たい場合は <a href="wiki/l0-minimum-artifact-pack.html">Wiki: L0で最低限そろえる成果物パック</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>EEGからL0までの全体順を一本道で見たいとき</strong>
<p>
EEG 入門のあとに、このページでデータを選び、L0実践節で一周し、Verification で L0 として確認するまでの流れを一本道で見たい場合は <a href="wiki/eeg-to-l0-route.html">Wiki: EEGからL0までの一本道</a> をご覧ください。
</p>
</div>

<div class="note-box">
<strong>raw EEG があるだけでは足りない</strong>
<p>
波形ファイルが公開されていても、<strong>イベント定義</strong>、<strong>刺激ログ</strong>、<strong>時刻同期</strong>、<strong>bad channel / bad segment の記録</strong>が弱いと、あとから比較し直しにくくなります。この点を初歩から整理したい場合は <a href="wiki/event-sync-and-measurement-logs.html">Wiki: イベント同期と観測ログの基本</a> を先にご覧ください。
</p>
</div>

<div class="note-box">
<strong>BIDS と OpenNeuro と Benchmark は同じではありません</strong>
<p>
BIDS は規格、OpenNeuro や PhysioNet は置き場、Validator は形式点検、Benchmark は比較ルールです。この役割差を初歩から整理したい場合は <a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: 規格・置き場・Validator・ベンチマーク</a> をご利用ください。
</p>
</div>

<div class="note-box">
<strong>将来の拡張先も意識する</strong>
<p>
スターターデータは EEG 中心で十分ですが、将来的に空間情報や構造情報を補いたくなる場面があります。EEG に何を足すと何が補えるかを先に整理したい場合は <a href="wiki/multimodal-integration-basics.html">Wiki: マルチモーダル統合の基本</a> をご利用ください。
</p>
</div>

<section class="section" id="platforms">
<h2 class="section-title">1) まず押さえる共有基盤（置き場）</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>OpenNeuro（BIDS前提の共有）</h4>
<p>BIDS準拠の神経計測データを共有するための基盤。EEG/MEG/fMRIなどを扱う。</p>
<a href="https://openneuro.org/" target="_blank" class="btn-action">Open OpenNeuro</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>PhysioNet（生体信号＋評価文化）</h4>
<p>生体信号データと関連リソースの公開基盤。EEGの定番データセットが多い。</p>
<a href="https://physionet.org/" target="_blank" class="btn-action">Open PhysioNet</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>Human Connectome Project（大規模fMRI等）</h4>
<p>公開データとツールを通じて、ヒト脳の大規模計測を提供してきた代表例。</p>
<a href="https://www.humanconnectome.org/" target="_blank" class="btn-action">Open HCP</a>
</div>
</div>
</div>

<div class="note-box">
<strong>置き場の次に固定する実行鎖</strong>
<p>
OpenNeuro や PhysioNet は入口ですが、それだけでは再現性は固定されません。まず <strong>snapshot / version</strong> を固定し、次に <strong>BIDS / EEG-BIDS</strong> で形をそろえ、<strong>MNE-BIDS</strong> のような読込・変換経路を固定し、最後に <strong>MOABB</strong> のような benchmark harness で <strong>within-session / cross-session / cross-subject</strong> のどれで比べたかを固定してください。repository と loader と benchmark を混ぜると、同じ dataset 名でも比較不能になります。
</p>
</div>
</section>

<section class="section" id="starter">
<h2 class="section-title">2) EEGスターターパック（まずこれでL0〜L1）</h2>
<p>
以下は、使いやすさと参照の多さを重視したEEG入門用データセットの代表例です。前処理パイプラインの練習とL0〜L1到達を意識し、再現されたベースライン比較にすぐ着手できる範囲へ絞り込んでいます。
</p>

<table class="data-table">
<thead>
<tr>
<th>データセット</th>
<th>何ができるか（例）</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>運動/運動想起の分類、前処理の練習、ベースライン比較</td>
<td><a href="https://physionet.org/content/eegmmidb/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>CHB-MIT Scalp EEG</strong></td>
<td>てんかん発作検出、イベント検出、長時間EEGの扱い</td>
<td><a href="https://physionet.org/content/chbmit/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>睡眠段階推定、状態遷移のモデル化、縦断的変動の扱い</td>
<td><a href="https://physionet.org/content/sleep-edfx/" target="_blank">PhysioNet</a></td>
</tr>
<tr>
<td><strong>TUH EEG Corpus（大規模）</strong></td>
<td>スケールするEEG分類、実運用寄りの分布の難しさ、データリーク対策</td>
<td><a href="https://www.isip.piconepress.com/projects/tuh_eeg/" target="_blank">TUH EEG</a></td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>データセット</th>
<th>最初の1本として出したいもの</th>
<th>なぜその出力が向くか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>2クラス分類のベースライン精度と前処理ログ</td>
<td>問題設定が単純で、前処理から評価までの最小ループを作りやすいためです。</td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>発作イベント検出の再現ベースラインと除外理由ログ</td>
<td>長時間データとイベント検出の難しさを、失敗例も含めて学びやすいためです。</td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>睡眠段階分類の基本ベースラインと状態遷移の混同行列</td>
<td>単なる精度だけでなく、状態の移り変わりをどう間違えるかまで見やすいためです。</td>
</tr>
<tr>
<td><strong>TUH EEG Corpus</strong></td>
<td>小さなサブセットでの再現実験とデータ分割ルールの明示</td>
<td>最初から全量を回すより、リーク対策と分割規則を先に固定する方が重要だからです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dataset-audit">
<h2 class="section-title">3) スターターデータを過大評価しないための監査</h2>
<p>
上の 4 件は L0〜L1 の練習台としては非常に有用ですが、EEG source imaging や WBE 寄りの強い主張を直接検証するための ground truth ではありません。ここで必要なのは、「使える / 使えない」の二分法ではなく、<strong>どの主張までなら支えられるか</strong>を固定することでございます。
</p>

<table class="data-table">
<thead>
<tr>
<th>データセット</th>
<th>今すぐ検証しやすいこと</th>
<th>まだ検証しにくいこと</th>
<th>最低限の注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>64ch・160 Hz・109 名の cue-locked 課題なので、前処理、被験者単位 split、単純ベースライン比較の練習に向きます。</td>
<td>個体別 MRI、電極座標、侵襲 ground truth がないため、ESI の精度改善や深部再構成の主張は監査できません。</td>
<td>左/右/上下 cue を画面提示する課題なので、視線、筋電、cue-locked artifact の混入を点検し、被験者単位 split を固定します。</td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>長時間 EEG、発作イベント検出、欠損と除外理由のログ化を学ぶには適しています。</td>
<td>小児・難治性てんかん・薬剤離脱という臨床条件に強く依存するため、一般認知や source imaging の汎用 benchmark にはなりません。</td>
<td>case 単位で split し、記録間の gap と montage summary を保持したまま扱います。発作あり/なしの不均衡も先に明示します。</td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>whole-night PSG による状態遷移、睡眠段階分類、縦断変動の扱いを学ぶには向いています。</td>
<td>主要 EEG は Fpz-Cz / Pz-Oz の 2 誘導、100 Hz なので、空間分解能や source imaging の benchmark にはなりません。</td>
<td>ラベルは Rechtschaffen &amp; Kales 基準の manual scoring なので、新しい睡眠段階研究と比べる場合はラベル対応を明示します。</td>
</tr>
<tr>
<td><strong>TUH EEG Corpus</strong></td>
<td>大規模・臨床ノイズ・反復セッション・医師レポート付きという現実分布の難しさを学ぶのに適しています。</td>
<td>チャネル数や臨床条件のばらつきが大きく、制御された biophysical benchmark ではないため、source imaging 改善の直接検証には向きません。</td>
<td>patient/session 単位 split、固定チャネル subset、montage 正規化、レポート利用時の text leakage 防止を先に固定します。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>BIDS は必要条件ですが、ground truth ではありません</strong>
<p>
BIDS / EEG-BIDS へ寄せることは重要ですが、それだけで source imaging の妥当性は証明できません。BIDS 仕様自体も <code>EEGReference</code>、<code>SamplingFrequency</code>、<code>SoftwareFilters</code> を必須とし、<code>*_electrodes.tsv</code> を出すなら <code>*_coordsystem.json</code> も必須にしています。しかし、これは「第三者が追える形」にする条件であり、「真の発生源が分かる」条件ではありません。
</p>
</div>

<div class="note-box">
<strong>ESI 改善を主張するなら、別系統の証拠鎖が要ります</strong>
<p>
少なくとも次の 4 点を出してください。
</p>
<ul>
<li><strong>個体別 anatomy：</strong>個体別 MRI/CT、または digitized electrode positions と <code>*_electrodes.tsv</code> / <code>*_coordsystem.json</code> を含む EEG-BIDS 記録</li>
<li><strong>順モデルの監査：</strong>採用した head model と skull conductivity 感度分析</li>
<li><strong>外部基準：</strong>phantom、同時侵襲記録、頭蓋内刺激、TMS-EEG などの ground truth</li>
<li><strong>不確実性：</strong>点推定だけでなく localization error と区間推定の報告</li>
</ul>
</div>
</section>

<section class="section" id="validation-ladder">
<h2 class="section-title">4) source imaging を深掘りするなら、データを3段階に分ける</h2>
<p>
このページの弱点になりやすかったのは、「スターターデータは source imaging の direct benchmark ではない」と止めるだけで、では<strong>何を次に選ぶべきか</strong>が弱かった点でございます。ここでは、主張の強さに応じてデータを 3 段階へ分けます。
</p>

<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>代表データ</th>
<th>支えられる主張</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>A: 練習台</strong></td>
<td>EEG Motor Movement/Imagery、CHB-MIT、Sleep-EDF、TUH EEG</td>
<td>L0〜L1 の再現解析、QC、split 設計、ベースライン比較</td>
<td>ESI の localization error 改善、深部 source claim、WBE 寄りの強い再構成主張</td>
</tr>
<tr>
<td><strong>B: 解剖制約つき再構成</strong></td>
<td>個体別 MRI、digitized electrodes、EEG-BIDS の <code>*_electrodes.tsv</code> / <code>*_coordsystem.json</code> を含む記録</td>
<td>forward model の監査、皮質表面近傍での reconstruction 比較、電極配置や conductivity 仮定の感度分析</td>
<td>direct ground truth なしの深部 source 精度保証、一般化した一意復元の主張</td>
</tr>
<tr>
<td><strong>C: 直接妥当化</strong></td>
<td>Localize-MI（Mikulan et al., 2020）、頭蓋内刺激つき scalp EEG、同時 HD-EEG/SEEG、術後転帰つき presurgical cohort</td>
<td>localization error、source depth 依存、conductivity 依存、臨床 concordance の直接評価</td>
<td>その task / cohort / montage を超えた普遍的性能保証</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>いま最も重要なのは C 段階の公開 benchmark です</strong>
<p>
Mikulan et al. (2020) の Localize-MI は、256ch scalp EEG と stereo-EEG による intracerebral stimulation を公開した希少なデータ資源で、source imaging を「既知の刺激位置」に対して直接監査できます。さらに Hao et al. (2025) は同時 HD-EEG/SEEG を用いた 29 例で、ictal ESI の平均局在誤差 14.07 mm、interictal 17.38 mm を報告しており、source power と source depth が精度を大きく左右することを示しました。したがって、source imaging の改善を主張するなら、A 段階のスターターデータではなく、少なくとも C 段階の benchmark と接続する必要があります。
</p>
</div>

<div class="note-box">
<strong>術後転帰は使えるが、ground truth と同一視してはいけません</strong>
<p>
Mouthaan et al. (2019) の systematic review では、presurgical epilepsy における electric source imaging の summary sensitivity は 82%、specificity は 53% でした。つまり、術後転帰や SOZ concordance は有用な外部基準ですが、source imaging 自体を真値として固定できるわけではありません。C 段階でも、いま言えるのは「この benchmark では誤差がどこまで減ったか」であって、「脳内 source を一意に読めた」ではございません。
</p>
</div>

<div class="note-box">
<strong>実務上の読み方</strong>
<p>
データ選定の最初の質問は、「何が面白いか」ではなく、<strong>今回どのレベルの主張を支えたいか</strong>でございます。L0〜L1 の練習なら A 段階で十分です。source imaging の改善主張へ進むなら B 段階で head model を監査し、C 段階で direct validation を取らない限り、主張は保留にしてください。
</p>
</div>
</section>

<section class="section" id="benchmark-mindset">
<h2 class="section-title">5) “データがある”だけで終わらせないチェックリスト</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>版固定：</strong>OpenNeuro snapshot、PhysioNet version、DOI、取得日が残っているか</li>
<li><strong>再現：</strong>取得手順、ライセンス、前処理条件、乱数、環境が書けるか</li>
<li><strong>メタデータ：</strong>サンプリング、参照、電極配置、イベント定義、同期情報が揃うか</li>
<li><strong>QC：</strong>ノイズ・欠損・アーティファクトが定量化されているか</li>
<li><strong>比較：</strong>ベースラインがあり、evaluation family と同じ指標で比較できるか</li>
<li><strong>反証：</strong>データリーク検査、反事実テスト、失敗例の記録があるか</li>
</ul>
</div>
</section>

<section class="section" id="l0-practice">
<h2 class="section-title">6) L0 の最小ループをここで一周させる</h2>
<p>
ここでの目標は、高精度を競うことではなく、<strong>第三者が同じ手順で追える最小ループ</strong>を作ることです。最初に必要なのは、dataset version の固定、BIDS 形式、QC ログ、evaluation family を含む分割規則、前処理条件、ベースラインでございます。
</p>

<div class="key-points">
<h4>L0 Loop</h4>
<ul>
<li><strong>版：</strong>OpenNeuro snapshot / PhysioNet version / DOI / 取得日を残す</li>
<li><strong>入力：</strong>BIDS（データ + メタデータ）で置ける形にする</li>
<li><strong>品質：</strong>欠損、ノイズ、アーティファクト、除外理由を数値で残す</li>
<li><strong>処理：</strong>前処理条件、乱数、ソフトウェア version、分割規則を固定する</li>
<li><strong>評価：</strong>within-session / cross-session / cross-subject のどれかを先に固定する</li>
<li><strong>出力：</strong>単純でもよいので、比較できるベースライン指標を1本置く</li>
<li><strong>監査：</strong>失敗例、リーク検査、保留条件も結果と一緒に残す</li>
</ul>
</div>

<table class="data-table">
<thead>
<tr>
<th>詰まりやすい点</th>
<th>先に切り分けること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同じ dataset 名で再現できると思ってしまう</strong></td>
<td>OpenNeuro snapshot tag や PhysioNet version を先に固定し、取得日と DOI まで runbook に残します。</td>
</tr>
<tr>
<td><strong>BIDSの形で止まる</strong></td>
<td>実データ投入の前に、ディレクトリ骨格、<code>dataset_description.json</code>、<code>participants.tsv</code>、<code>events.tsv</code> の雛形を先に作ります。</td>
</tr>
<tr>
<td><strong>QCをどこまで残すか迷う</strong></td>
<td>欠損、ノイズ、アーティファクト、除外理由の4項目だけでも固定し、あとから増やす方が安全です。</td>
</tr>
<tr>
<td><strong>ベースラインが決められない</strong></td>
<td>複雑なモデルより、運動想起2クラスやスペクトル要約など、単純で再現しやすい1本を先に置きます。</td>
</tr>
<tr>
<td><strong>train/test で迷う</strong></td>
<td>まずは within-session / cross-session / cross-subject のどれで比べるかを決め、その後に被験者単位や session 単位の split を固定します。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>Step 0: 版を凍結する</strong>
<p>
dataset 名だけでは足りません。OpenNeuro は snapshot を semantic version の git tag で管理し、PhysioNet も project ごとに version を表示して引用させます。したがって、最初の runbook には <strong>dataset 名</strong>ではなく <strong>snapshot / version / DOI / 取得日</strong> を残してください。
</p>
</div>

<div class="note-box">
<strong>Step 1: BIDSの骨格を先に作る</strong>
<p>
最初は中身が揃っていなくても、置き方を固定するだけで手戻りが減ります。Validator を通す前提でファイル名とメタデータ雛形を作ると、後続の QC や比較が一気に楽になります。
</p>
</div>

<div class="note-box">
<strong>Step 2: Validatorで規格違反を先に潰す</strong>
<p>
機械で見つかる問題は早い段階で潰してください。BIDS Validator が通ることは研究として十分条件ではありませんが、共有可能な最低条件には近いです。
</p>
</div>

<div class="note-box">
<strong>Step 2.5: loader と benchmark を分けて固定する</strong>
<p>
MNE-BIDS は BIDSPath、読込、metadata 抽出の経路を助ける道具であり、MOABB は paradigm と evaluation family を固定する道具でございます。<strong>読めた</strong>ことと<strong>公平比較できる</strong>ことは別です。特に MNE-BIDS は、modified/preloaded data の書き戻しを例外扱いにしており、前処理済みデータは lineage を明示して derivatives として扱う方が安全です。
</p>
</div>

<div class="note-box">
<strong>Step 3: QCログは波形ではなく数値で残す</strong>
<p>
生の波形だけでは、何が悪くて何を除外したかを第三者が再構成しづらくなります。bad channel、bad segment、イベント同期、刺激ログ、反応ログを数値と閾値で残すことが L0 の本体でございます。
</p>
</div>

<div class="note-box">
<strong>Step 4: ベースラインを1本だけ固定する</strong>
<p>
SOTA ではなく、再現しやすい比較軸を先に置きます。最初のベースラインがあると、前処理更新やモデル更新をしても「何が良くなったか」を比較可能なまま追えます。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>確認項目</th>
<th>L0 の最低ライン</th>
<th>不足しているときに戻る場所</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>データ版</strong></td>
<td>snapshot / version / DOI / 取得日が固定されている</td>
<td><a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: 規格・置き場・Validator・ベンチマーク</a></td>
</tr>
<tr>
<td><strong>データ構造</strong></td>
<td>BIDS 形式で置けている</td>
<td><a href="#bids">共有できるデータにする最短ルート</a></td>
</tr>
<tr>
<td><strong>品質管理</strong></td>
<td>QC ログと除外基準が残っている</td>
<td><a href="wiki/event-sync-and-measurement-logs.html">Wiki: イベント同期と観測ログ</a></td>
</tr>
<tr>
<td><strong>比較可能性</strong></td>
<td>ベースライン1本と evaluation family / train/test ルールが固定されている</td>
<td><a href="wiki/dataset-splits-and-leakage.html">Wiki: データ分割とデータリーク</a></td>
</tr>
<tr>
<td><strong>共有準備</strong></td>
<td>実行手順、環境、失敗例を第三者に渡せる</td>
<td><a href="verification.html">検証基盤</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="bids">
<h2 class="section-title">7) Mind-Uploadで「共有できるデータ」にする最短ルート</h2>
<p>
Mind-Uploadが目指すのは、単にデータを集めることではなく、<strong>第三者が検証できる形</strong>で残すことです。
そのための最短ルートは BIDS/EEG-BIDS に寄せることです。
</p>
<div class="cta-box">
<h4>Verification Commons</h4>
<p>「規格＋置き場＋評価」の設計図はこちら。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">8) 参考文献と公式ページ</h2>
<ul>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS 1.11.1: Electroencephalography</a></li>
<li><a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019), EEG-BIDS</a></li>
<li><a href="https://docs.openneuro.org/git.html" target="_blank">OpenNeuro Docs: Git access and snapshots</a></li>
<li><a href="https://docs.openneuro.org/user_guide.html" target="_blank">OpenNeuro Docs: Dataset landing page and snapshot metadata</a></li>
<li><a href="https://physionet.org/about/" target="_blank">PhysioNet: About and citation policy</a></li>
<li><a href="https://physionet.org/about/content/" target="_blank">PhysioNet: Resources and citation guidance</a></li>
<li><a href="https://doi.org/10.21105/joss.01896" target="_blank">Appelhoff et al. (2019), MNE-BIDS</a></li>
<li><a href="https://mne.tools/mne-bids/stable/generated/mne_bids.write_raw_bids.html" target="_blank">MNE-BIDS Docs: write_raw_bids</a></li>
<li><a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018), MOABB</a></li>
<li><a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB Docs</a></li>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), TUH EEG Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), TUH Seizure Detection Corpus</a></li>
<li><a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020), Localize-MI</a></li>
<li><a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025), HD-EEG source imaging with simultaneous SEEG</a></li>
<li><a href="https://doi.org/10.1016/j.clinph.2018.12.016" target="_blank">Mouthaan et al. (2019), E-PILEPSY systematic review</a></li>
<li><a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023), Validating EEG source imaging using intracranial electrical stimulation</a></li>
<li><a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">Seeber et al. (2019), Subcortical electrophysiological activity is detectable with high-density EEG source imaging</a></li>
</ul>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="tech_roadmap.html#measurement">Roadmap: 計測 →</a></li>
<li><a href="verification.html#casework">Verification: ケースワーク →</a></li>
<li><a href="glossary.html">用語集 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Links</h4>
<ul>
<li><a href="https://bids.neuroimaging.io/" target="_blank">BIDS</a></li>
<li><a href="https://openneuro.org/" target="_blank">OpenNeuro</a></li>
<li><a href="https://physionet.org/" target="_blank">PhysioNet</a></li>
</ul>
</div>

</aside>
</main>
