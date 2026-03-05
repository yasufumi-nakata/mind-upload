---
layout: default
title: "データ & ベンチ：まず何を使って検証するか"
description: "公開データ（EEG中心）と共有基盤を、Mind-Uploadの目的（比較可能な検証）に沿って整理します。"
article_type: Resource
subtitle: "「データがある」だけでは足りない。規格・メタデータ・評価がセット。"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Curated List (v0)"
audience: "どの公開データから始めるべきか迷っている人、L0の練習台を探している人"
reading_time: "8〜15分"
page_intro: "このページは、『最初にどの公開データで検証を始めるか』を決めるための実務ガイドです。データ名の一覧ではなく、L0の再現解析からL1/L2の比較へ進みやすい順で見ることを意図しています。"
accuracy_note: "ここに載せるデータセットは入口候補です。使いやすさや再現性の観点で挙げており、これだけでWBEの全課題を覆えるわけではありません。"
page_highlights:
  - "まずは共有基盤を押さえ、その後にスターターデータセットを見る順にしています。"
  - "『データがある』だけで終わらせないためのチェックリストを入れています。"
  - "最終目標は、第三者が同じ条件で走らせられる形へ寄せることです。"
known_points:
  - "公開 EEG データは、L0 の再現解析や L1 のベースライン練習に十分役立ちます。"
  - "最初のデータ選びでは、難しさよりも追試しやすさを優先した方が前に進みます。"
  - "データだけでなく、メタデータ、QC、評価ルールがそろって初めて比較可能になります。"
unknown_points:
  - "スターターデータセットだけで WBE の全論点を解くことはできません。"
  - "どのデータが将来の因果・閉ループ検証へ最も効くかは、まだ固定していません。"
wiki_links:
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "データセットを見る前に、EEG の信号そのものを理解したい人向けです。"
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
  - label: "ハンズオン"
    url: "/hands_on.html"
  - label: "検証基盤"
    url: "/verification.html"
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

<section class="section" id="benchmark-mindset">
<h2 class="section-title">3) “データがある”だけで終わらせないチェックリスト</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>再現：</strong>取得手順、ライセンス、前処理条件、乱数、環境が書けるか</li>
<li><strong>メタデータ：</strong>サンプリング、参照、電極配置、イベント定義、同期情報が揃うか</li>
<li><strong>QC：</strong>ノイズ・欠損・アーティファクトが定量化されているか</li>
<li><strong>比較：</strong>ベースラインがあり、同じ指標で比較できるか</li>
<li><strong>反証：</strong>データリーク検査、反事実テスト、失敗例の記録があるか</li>
</ul>
</div>
</section>

<section class="section" id="bids">
<h2 class="section-title">4) Mind-Uploadで「共有できるデータ」にする最短ルート</h2>
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

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="tech_roadmap.html#measurement">Roadmap: 計測 →</a></li>
<li><a href="casework.html#data-standardization">Casework: 規格＋置き場 →</a></li>
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
