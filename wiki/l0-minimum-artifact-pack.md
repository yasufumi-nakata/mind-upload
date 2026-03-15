---
layout: default
title: "Wiki：L0で最低限そろえる成果物パック"
description: "dataset version、raw/derivatives、Validator、QCログ、split manifest、GeneratedBy、実行環境、失敗例など、L0 の最低成果物を整理します。"
article_type: Wiki
subtitle: "『最小ループ』を、raw / derivatives / 実行環境まで含めて固定する"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Operational guide"
audience: "L0 を作り始めた人、どこまでそろえば再現可能解析と呼べるかを確認したい人"
reading_time: "10〜15分"
page_intro: "このページは、L0 の再現可能解析を作るときに、最終的に何を一式としてそろえるべきかを整理する補助ページです。2026-03 の更新では、BIDS の raw 入力だけでなく、derivatives の lineage、split manifest、実行環境の pin まで成果物へ含める方針に強化しました。"
accuracy_note: "ここで扱うのは L0 の最低限です。これだけで因果主張や本人性の議論に進めるわけではありませんが、比較可能な出発点としては重要です。BIDS / EEG-BIDS / COBIDAS-MEEG / BIDS Derivatives / BIDS Apps は『最低限の再現可能性の床』を与えますが、研究の妥当性そのものを自動で保証するわけではありません。"
page_highlights:
  - "dataset 名だけでなく、raw dataset identity と derivative lineage を分けて固定します。"
  - "split manifest、seed、git commit、container tag ないし lockfile まで成果物へ含めます。"
  - "『runbook はある』だけでなく、『この出力がどの入力とどの pipeline から出たか』を機械可読に追えることを求めます。"
known_points:
  - "L0 では高精度より、第三者が同じ条件で再実行できることが重要です。"
  - "同じ dataset 名でも、snapshot や version が違えば再現にはなりません。"
  - "cleaned file や feature table は、raw 入力と別の artifact であり、lineage を持つ derivative として扱う方が安全です。"
  - "失敗例や既知のつまずきどころも成果物の一部として残すべきです。"
unknown_points:
  - "split manifest や derivative provenance を、どの共通 schema で site-wide に必須化するかは今後の整備課題です。"
  - "L0 の先で、どこまで L1/L2 の標準成果物へ広げるかは今後の整備次第です。"
wiki_links:
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "BIDS、HED、LSL、MNE-BIDS、MOABB の役割差を補います。"
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "event semantics、clock domain、label provenance を補います。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "split manifest が成果物に入る理由を補います。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "ベースラインや失敗例の役割差を補います。"
recommended_pages:
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず 1 パックで考える</h2>
<p>
L0 の成果物は、1 つのファイルや 1 つのスコアではありません。<strong>どの版の raw 入力か</strong>、<strong>入力の意味と品質</strong>、<strong>どの split で評価したか</strong>、<strong>どの pipeline が何を生成したか</strong>、<strong>その pipeline をどう再実行するか</strong>がそろって、初めて第三者が追える状態になります。
</p>
</div>

<div class="note-box">
<strong>2026-03 の更新で強めた境界</strong>
<p>
従来のページは、dataset version、BIDS、QC、分割、ベースライン、実行手順を押さえる入門としては有用でした。しかし、それだけでは <strong>cleaned file がどの raw 入力とどの前処理から出たか</strong> を監査できません。そこで本サイトでは、<strong>raw と derivative の境界</strong>、<strong><code>GeneratedBy</code> / <code>SourceDatasets</code></strong>、<strong>split manifest</strong>、<strong>container tag ないし lockfile</strong> を L0 成果物へ昇格します。
</p>
</div>

<section class="section" id="artifact-pack">
<h2 class="section-title">L0 で最低限そろえたい 10 点</h2>
<table class="data-table">
<thead>
<tr>
<th>成果物</th>
<th>最低限ほしい中身</th>
<th>欠けると何が困るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. raw dataset identity</strong></td>
<td>OpenNeuro snapshot、PhysioNet version、DOI、取得日、永続 URL。</td>
<td>同じ dataset 名でも別版を混ぜ、再現不能になります。</td>
</tr>
<tr>
<td><strong>2. raw BIDS 骨格</strong></td>
<td>BIDS の骨格、<code>channels.tsv</code>、<code>electrodes.tsv</code>、<code>coordsystem.json</code>、課題説明、参照法や filter 情報。</td>
<td>入力の幾何や取得条件が揃わず、比較の出発点が壊れます。</td>
</tr>
<tr>
<td><strong>3. event semantics と label provenance</strong></td>
<td><code>events.tsv</code> / JSON sidecar、必要に応じた HED、manual scoring / report-derived label の別、clock domain。</td>
<td>同じ列名や同じ label 名でも、意味と出どころが曖昧になり比較不能になります。</td>
</tr>
<tr>
<td><strong>4. 規格確認結果</strong></td>
<td>BIDS Validator の結果、残した warning の理由、必要なら file hash。</td>
<td>共有不能な規格違反や silent drift を見落としやすくなります。</td>
</tr>
<tr>
<td><strong>5. QC ログ</strong></td>
<td>欠損、ノイズ、アーティファクト、bad channel / bad segment、除外理由の数値記録。</td>
<td>どのデータが悪かったかが人依存になり、再現性が壊れます。</td>
</tr>
<tr>
<td><strong>6. derivative lineage</strong></td>
<td><code>derivatives/</code> 配下、<code>dataset_description.json</code> の <code>DatasetType=derivative</code>、<code>GeneratedBy</code>、<code>SourceDatasets</code>、必要に応じた file-level source list。</td>
<td>cleaned file、epochs、feature table、figure、report が、どの raw 入力とどの pipeline から出たか追えません。</td>
</tr>
<tr>
<td><strong>7. split manifest</strong></td>
<td>within-session / cross-session / cross-subject の別、train/validation/test の単位、split hash、test frozen rule。</td>
<td>数字の上振れを見抜けず、評価全体が崩れます。</td>
</tr>
<tr>
<td><strong>8. ベースライン結果</strong></td>
<td>単純な 1 本の指標、採点規則、結果表、比較相手。</td>
<td>改善を主張する出発点が無くなります。</td>
</tr>
<tr>
<td><strong>9. 実行環境と command provenance</strong></td>
<td>コマンド、git commit、主要パラメータ、乱数 seed、software version、container tag ないし lockfile、既知のつまずきどころ。</td>
<td>他の人が同じ pipeline を同じ挙動で再実行できません。</td>
</tr>
<tr>
<td><strong>10. failure registry</strong></td>
<td>除外した条件、うまくいかなかった設定、停止した主張、既知の弱点。</td>
<td>成功だけが残り、次の人が同じ失敗を繰り返します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="derivative-boundary">
<h2 class="section-title">raw と derivative を混ぜない</h2>
<p>
L0 で最も抜けやすいのは、<strong>「cleaned file は raw のちょっときれいな版だ」</strong>という扱いでございます。BIDS の公式仕様では、raw dataset と processing outputs は別の層として扱い、derivatives には pipeline metadata を持たせます。したがって本サイトでは、再参照済み EEG、ICA 後の波形、epoch、feature table、decoder input matrix、QC report、figure を <strong>derivative</strong> とみなし、raw と同じ箱へ曖昧に置きません。
</p>
<table class="data-table">
<thead>
<tr>
<th>層</th>
<th>代表例</th>
<th>最低限残すもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>raw</strong></td>
<td>公開データから取得した EDF / BDF / BrainVision などの入力。</td>
<td>dataset version、BIDS metadata、event semantics、取得条件。</td>
</tr>
<tr>
<td><strong>derivative</strong></td>
<td>cleaned EEG、epochs、features、reports、figures、prediction tables。</td>
<td><code>DatasetType=derivative</code>、<code>GeneratedBy</code>、<code>SourceDatasets</code>、必要な file-level lineage。</td>
</tr>
<tr>
<td><strong>run provenance</strong></td>
<td>split manifest、seed、command、git commit、container tag、parameter JSON。</td>
<td>「どの derivative が、どの条件で生成されたか」を復元できる記録。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="minimum-example">
<h2 class="section-title">最低限の provenance 例</h2>
<p>
値は例ですが、L0 の derivative 側には少なくとも次のような情報を残す方針でございます。ここで重要なのは、見栄えの良い README よりも、<strong>機械可読な lineage</strong> が先にあることです。
</p>

<pre><code class="language-json">{
  "Name": "example-l0-derivatives",
  "BIDSVersion": "1.10.1",
  "DatasetType": "derivative",
  "GeneratedBy": [
    {
      "Name": "example-eeg-pipeline",
      "Version": "0.3.0",
      "CodeURL": "https://example.org/pipeline",
      "Container": {
        "Type": "docker",
        "Tag": "example/eeg-pipeline:0.3.0"
      }
    }
  ],
  "SourceDatasets": [
    {
      "URL": "https://example.org/source-dataset",
      "DOI": "10.0000/example-doi"
    }
  ]
}</code></pre>

<p>
上の JSON だけで完全ではありません。split manifest、parameter file、seed、test frozen rule、failure registry も別 artifact として残します。ただし、この境界を切らずに「runbook があるから十分」と読むのは危険です。
</p>
</section>

<section class="section" id="minimum-shape">
<h2 class="section-title">もっと短く言うと</h2>
<div class="key-points">
<h4>Pack</h4>
<ul>
<li><strong>Input:</strong> raw dataset identity + raw BIDS 骨格</li>
<li><strong>Meaning:</strong> event semantics + label provenance + clock domain</li>
<li><strong>Quality:</strong> Validator + QC + exclusion codes</li>
<li><strong>Lineage:</strong> derivatives + <code>GeneratedBy</code> + <code>SourceDatasets</code></li>
<li><strong>Evaluation:</strong> split manifest + baseline + scoring rule</li>
<li><strong>Execution:</strong> command + parameters + seed + git commit + container tag</li>
<li><strong>Audit:</strong> failure registry + stop claims</li>
</ul>
</div>
</section>

<section class="section" id="common-gaps">
<h2 class="section-title">よくある抜け</h2>
<table class="data-table">
<thead>
<tr>
<th>ありがちな状態</th>
<th>まだ足りないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>dataset 名はある</strong></td>
<td>snapshot、version、DOI、取得日が残っていないことがあります。</td>
</tr>
<tr>
<td><strong>波形ファイルはある</strong></td>
<td>event semantics、clock domain、label provenance が足りないことがあります。</td>
</tr>
<tr>
<td><strong>cleaned EEG はある</strong></td>
<td><code>GeneratedBy</code>、<code>SourceDatasets</code>、parameter file が無く、derivative lineage が切れていることがあります。</td>
</tr>
<tr>
<td><strong>精度はある</strong></td>
<td>split manifest、split hash、baseline、test frozen rule が無いことがあります。</td>
</tr>
<tr>
<td><strong>コードはある</strong></td>
<td>git commit、container tag ないし lockfile、乱数 seed、既知の失敗条件が書かれていないことがあります。</td>
</tr>
<tr>
<td><strong>QC したつもり</strong></td>
<td>数値ログ、除外理由、fail code が残っていないことがあります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="exit-criteria">
<h2 class="section-title">L0 完了の簡易判定</h2>
<table class="data-table">
<thead>
<tr>
<th>質問</th>
<th>はいなら前進</th>
<th>いいえなら次にやること</th>
</tr>
</thead>
<tbody>
<tr>
<td>他の人が同じ raw 入力を持てますか</td>
<td>snapshot / version / DOI と raw BIDS 骨格が揃っています。</td>
<td>raw dataset identity と BIDS metadata を先に固定します。</td>
</tr>
<tr>
<td>同じ label の意味を復元できますか</td>
<td>event semantics、annotation provenance、clock domain が残っています。</td>
<td><code>events.json</code>、HED、manual/report 由来の別を追加します。</td>
</tr>
<tr>
<td>cleaned output がどこから出たか追えますか</td>
<td>derivative 側に <code>GeneratedBy</code> / <code>SourceDatasets</code> が残っています。</td>
<td>raw と derivative を分離し、lineage を追加します。</td>
</tr>
<tr>
<td>数字の作り方を説明できますか</td>
<td>split manifest、baseline、scoring rule が固定されています。</td>
<td>train/test と比較相手を先に固定します。</td>
</tr>
<tr>
<td>他の人が同じ挙動で再実行できますか</td>
<td>command、git commit、主要パラメータ、seed、container tag ないし lockfile が残っています。</td>
<td>runbook を machine-readable provenance 付きへ拡張します。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>このページがしないこと</strong>
<p>
ここでは、どのモデルが最強か、どの指標が最終的に正しいかは決めません。L0 では、まず比較可能な出発点を作ることが目的です。また、container tag や split hash を残しただけで研究の妥当性が保証されるわけでもありません。これはあくまで <strong>監査可能性の床</strong>です。
</p>
</div>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Gorgolewski KJ, Auer T, Calhoun VD, et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. <em>Sci Data</em>. 2016. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Sci Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nat Neurosci</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Gorgolewski KJ, Esteban O, Ellis DG, et al. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. <em>PLoS Comput Biol</em>. 2017. <a href="https://doi.org/10.1371/journal.pcbi.1005209" target="_blank">doi:10.1371/journal.pcbi.1005209</a></li>
<li>BIDS Specification (stable). Derived dataset and pipeline description. <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">official documentation</a></li>
<li>Robbins KA, Touryan J, Mullen T, et al. Building FAIR functionality: Annotating events in time series data using Hierarchical Event Descriptors. <em>Neuroinformatics</em>. 2021. <a href="https://doi.org/10.1007/s12021-021-09513-7" target="_blank">doi:10.1007/s12021-021-09513-7</a></li>
<li>Hermes D, Bigdely-Shamlo N, Niso G, et al. HED library schema for EEG data annotation. <em>Sci Data</em>. 2025. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">doi:10.1038/s41597-025-05791-2</a></li>
</ol>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
実際の手順を追いたい場合は <a href="../datasets.html#l0-practice">ハンズオン</a>、入口データを選び直したい場合は <a href="../datasets.html">データ&ベンチ</a>、この成果物が公共財としてどう積み上がるかを見たい場合は <a href="../verification.html">検証基盤</a> に戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="standards-repositories-validators-and-benchmarks.html">規格・置き場・Validator・ベンチマーク →</a></li>
<li><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ →</a></li>
<li><a href="dataset-splits-and-leakage.html">データ分割とデータリーク →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">ベースライン・事前登録・モデルカード →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
