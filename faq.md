---
layout: default
title: "FAQ：よくある質問（と、よくある事故）"
description: "Mind-Uploadを読んでいて出やすい疑問に、短く正確に答えます。"
article_type: FAQ
subtitle: "派手な結論より、検証できる前進を"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Human-first"
audience: "まず疑問や誤解を整理したい人、短いQ&Aで全体像をつかみたい人"
reading_time: "8〜15分"
page_intro: "このページは、Mind-Upload を読んでいて多くの人が最初にぶつかる疑問へ、短くても誤解の少ない答えを返すための Q&A です。入口として短く書いていますが、強い主張は必ず根拠ページへ戻れるようにしています。"
accuracy_note: "ここは短い答えを返すページです。結論だけ切り取らず、必要に応じてリンク先の本文と参考文献へ戻ってください。"
page_highlights:
  - "『このサイトは何をするのか』『EEG / brain-to-text で何が言えるのか』など、最初の疑問をまとめて潰せます。"
  - "『コネクトームと cell type で十分か』という誤読にも、current synaptic state・dendritic integration・AIS / excitability・slow maintenance-state を分けて答えます。"
  - "派手な言い切りを避け、何が未解決かも同時に書いています。"
  - "brain-to-text では、Neural Contribution Card に沿って神経寄与と task / language prior を分けて読みます。"
  - "FAQだけで十分な場合と、本文ページへ進むべき場合を分けて読める構成です。"
known_points:
  - "短い Q&A でも、強い主張を弱い主張へ分解して読むだけで誤解は減らせます。"
  - "EEG や LLM の派手な見た目と、WBE の強い主張は分けて扱う必要があり、language prior と brain-derived information の寄与も分離する必要があります。"
  - "配線図や cell type だけでは、current synaptic state・dendritic integration・AIS / excitability・slow maintenance-state が残るため、長期ダイナミクスの主張は別に監査する必要があります。"
  - "FAQ は方向を間違えないための入口として有効です。"
unknown_points:
  - "短い答えだけでは、理論選択や本人性の議論までは決まりません。"
  - "個々の研究発表がどこまで一般化できるかは、元論文と検証条件に依存します。"
wiki_links:
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "FAQ の短い答えを、もう一段ていねいに学びたい人向けです。"
  - label: "Wiki: 公開ページ冒頭ブロックの読み方"
    url: "/wiki/page-header-reading-guide.html"
    description: "FAQ の上部にある案内、既知/未知、wiki導線をどう使うかを整理します。"
  - label: "Wiki: L0〜L5ごとの読み進め方"
    url: "/wiki/claim-level-reading-routes.html"
    description: "FAQ で見た主張が、次にどのページへ進む話かを整理します。"
  - label: "Wiki: 公開ページの読み分けガイド"
    url: "/wiki/public-page-reading-guide.html"
    description: "FAQ のあとに本文のどこへ戻るかを整理します。"
  - label: "Wiki: Decode と Emulate"
    url: "/wiki/decode-vs-emulate.html"
    description: "Q2 で出る違いを、日常例でもう一段噛み砕きます。"
  - label: "Wiki: 意識理論マップ"
    url: "/wiki/consciousness-theory-map.html"
    description: "Q8 の IIT と GNWT の位置づけを、表で整理します。"
  - label: "Wiki: 反事実・介入・摂動"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "Q1〜Q3 で出る因果検証の入口を、初歩から整理します。"
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "Q4 で出る標準化の話を、役割ごとに整理します。"
  - label: "Wiki: 閉ループ・遅延・ジッタ・安全停止"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "オフライン精度と L3 の違いを、リアルタイム系の観点から整理します。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "用語集"
    url: "/glossary.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Read</h2>
<p>
ここは「よくある勘違い」を先に避けるためのページです。主張が大きいほど、(1)言葉の定義、(2)評価の物差し、(3)間違いと判定する条件、(4)再現手順の順で確認します。
</p>
</div>

<div class="note-box">
<strong>FAQの限界</strong>
<p>
FAQは「まず方向を間違えないための短い答え」です。ここで雰囲気だけ掴み、根拠や細部が必要になったらリンク先へ進む使い方を前提にしています。
</p>
</div>
<div class="note-box">
<strong>短い答えのあとに戻る本文で迷ったとき</strong>
<p>
FAQ は入口なので、次に Verification、WBE 101、Datasets、Glossary のどこへ戻るかを決める必要があります。公開ページどうしの役割差を先に整理したい場合は <a href="wiki/public-page-reading-guide.html">Wiki: 公開ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>このサイト全体をどう使うかで迷ったとき</strong>
<p>
FAQ を入口にして、そのあと全体像をつかむのか、wiki で学ぶのか、Issue に落とすのかを 3 モードで見たい場合は <a href="wiki/site-usage-modes.html">Wiki: このサイトの3つの使い方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>FAQ の上部にある案内や既知/未知の使い方で迷ったとき</strong>
<p>
このページの冒頭にある「このページの読み方」「正確さの前提」「いま分かっていること」「wiki で基礎から確認する」は、短いQ&Aを誤読しないための入口です。共通ルールを 1 枚で見たい場合は <a href="wiki/page-header-reading-guide.html">Wiki: 公開ページ冒頭ブロックの読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>いまの疑問が L0〜L5 のどこかで迷ったとき</strong>
<p>
FAQ の質問は、L0 の実務から L5 の社会実装まで混ざっています。主張レベルごとに次のページを整理したい場合は <a href="wiki/claim-level-reading-routes.html">Wiki: L0〜L5ごとの読み進め方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>理論だけ追いたいか、実務だけ追いたいかで迷ったとき</strong>
<p>
FAQ のあとに理論系ページだけへ進みたい場合は <a href="wiki/theory-pages-reading-guide.html">Wiki: 理論系ページの読み分けガイド</a>、Verification や Datasets など実務系ページへ進みたい場合は <a href="wiki/practical-pages-reading-guide.html">Wiki: 実務系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>Verificationを読んだあとに次の1ページで迷ったとき</strong>
<p>
FAQ から Verification へ進んだあとに、L0 実装へ戻るのか、L2・L3・L4 のどれを先に見るのかで迷う場合は <a href="wiki/verification-next-routes.html">Wiki: Verificationのあとに進む4つの道</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>疑問をそのまま Issue に変えたいとき</strong>
<p>
FAQ を読んで「ここが分かりにくい」「この条件が足りない」と感じた箇所を、そのまま価値ある Issue に変えたい場合は <a href="wiki/issue-writing-basics.html">Wiki: はじめての Issue の書き方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>『分かった』と『次に進める』の違いで迷ったとき</strong>
<p>
FAQ を読んで意味は分かったが、次に何を確認すれば修正や判断に進めるか分からない場合は <a href="wiki/understanding-vs-action-readiness.html">Wiki: 『分かった』と『次に進める』の違い</a> をご覧ください。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>こんなとき</th>
<th>先に読む質問</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>このサイトの目的だけ知りたい</strong></td>
<td>Q0「Mind-Uploadは結局、何をするサイト？」から入ると全体像が早いです。</td>
</tr>
<tr>
<td><strong>ニュースの派手な主張を読み違えたくない</strong></td>
<td>Q1「EEGで“思考”は読める？」、Q1b「brain-to-text のデモを見るとき…」、Q2「decode と emulate の違いは？」を先に見てください。</td>
</tr>
<tr>
<td><strong>何を作れば前進かだけ知りたい</strong></td>
<td>Q3「じゃあ、何を作れば“前進”になる？」を見ると、L0〜L2 の最小成果物が分かります。</td>
</tr>
<tr>
<td><strong>コネクトームだけで足りるか知りたい</strong></td>
<td>Q2c「コネクトームと cell type が分かれば、残りはほぼ埋まる？」を見ると、current synaptic state / dendrite / AIS / maintenance-state の抜けが分かります。</td>
</tr>
<tr>
<td><strong>リアルタイムや閉ループの条件が知りたい</strong></td>
<td>Q5b「オフライン精度が高ければ、閉ループでも十分？」から入ると、L3 で何が追加されるかをつかみやすいです。</td>
</tr>
<tr>
<td><strong>哲学や倫理の立場を知りたい</strong></td>
<td>Q6「ハードプロブレム」と Q9「倫理的課題」を読むと、どこまで扱っているかが分かります。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>強い主張を見たときの4点チェック</strong>
<ol>
<li><strong>何を達成した話か：</strong>L0〜L5 のどのレベルかを先に確認します。</li>
<li><strong>何を測ったのか：</strong>出力の一致だけか、介入や反事実まで見ているかを分けます。</li>
<li><strong>何が出たら間違いなのか：</strong>反証条件が明示されているかを見ます。</li>
<li><strong>他の人が追えるか：</strong>データ、コード、ログ、手順が公開されているかを確認します。</li>
</ol>
</div>

<section class="section" id="q0">
<h2 class="section-title">Q. Mind-Uploadは結局、何をするサイト？</h2>
<p>
A. マインドアップロード/WBEを「検証可能な研究プログラム」に寄せるための<strong>検証基盤（Verification Commons）</strong>を作るサイトです。
データ（入力）、評価（出力）、ルール（達成条件/反証条件）、運用（継続）を先に固定します。
</p>
<div class="cta-box">
<h4>Start</h4>
<p>全体像はここから。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

<section class="section" id="q1">
<h2 class="section-title">Q. EEGで“思考”は読める？</h2>
<p>
A. 「限定条件つきで一部を読める」は言えますが、「自由な思考をそのまま読める」とはまだ言えません。Tang et al. (2023) は non-invasive brain recordings を使った連続言語の semantic reconstruction を示しましたが、これは fMRI を用いた被験者別の再構成系です。d'Ascoli et al. (2025) は 723 人・500 万語規模の non-invasive M/EEG から単語 decoding の前進を示しましたが、既知の word onset と課題構造に依存し、MEG と reading が EEG と listening より有利でした。
</p>
<p>
さらに、頭皮信号から内部状態を一意に決められるわけでもありません。Unnwongse et al. (2023) の intracranial stimulation を使った直接妥当化では、ESI の平均 localization error は source depth と skull conductivity に応じて 10.3-26.0 mm でした。Hao et al. (2025) の simultaneous HD-EEG/SEEG でも、ictal ESI は interictal ESI より良かったものの 14.07 ± 4.62 mm 対 17.38 ± 4.16 mm で、精度は source depth と spike power に強く依存しました。
</p>
<p>
Mind-Uploadの立場は、「派手な読み出し」を否定することではなく、まず主張を <strong>課題依存の decoding</strong> と <strong>内部状態の同定</strong> に分け、language prior・校正・棄権条件・直接妥当化の有無を明示することです。ここを省くと、「文字列が出た」ことをそのまま WBE に必要な state reconstruction と誤読します。
</p>
</section>

<div class="note-box">
<strong>Q1の読み替え禁止</strong>
<p>
<code>文字列が出た</code>、<code>脳由来情報だけで出た</code>、<code>real-time に使える</code>、<code>内部状態が分かった</code> は別です。brain-to-text を読むときは、(1) 計測法、(2) 課題制約、(3) language prior、(4) causal / non-causal の別、(5) 直接妥当化、(6) 校正と棄権条件、を分けて確認してください。
</p>
</div>

<section class="section" id="q1b">
<h2 class="section-title" id="brain-to-text">Q. brain-to-text のデモを見るとき、最低限どこを確認する？</h2>
<p>
A. 少なくとも次の 8 点でございます。
</p>
<ul>
<li><strong>計測法：</strong>scalp EEG / MEG / fMRI / ECoG / intracortical array のどれか。高性能 speech neuroprosthesis の代表例は侵襲系です。</li>
<li><strong>課題：</strong>聞いた単語、読んだ単語、発話運動、想起、自由会話のどれか。制約つき知覚課題と自由思考は別です。</li>
<li><strong>prior と baseline：</strong>固定語彙、beam search、外部コーパス、LLM、prompt に加え、<code>LM-only</code> / <code>no-brain</code> / shuffle baseline をどこまで置いたか。出力の流暢さが脳信号だけを反映しているとは限りません。</li>
<li><strong>causal性：</strong>causal decoder か、future context や post-onset auditory feedback を見ている non-causal decoder か。offline の見栄えと real-time deployability は別です。</li>
<li><strong>adaptation / transfer：</strong>participant-specific training がどれだけ必要か、group-derived decoder や transfer learning を使ったか。一般 decoder と個別最適化は別です。</li>
<li><strong>検証：</strong>held-out 条件、反事実テスト、adversarial control、失敗例があるか。訓練条件と近すぎる評価は強い証拠になりません。</li>
<li><strong>信頼度運用：</strong>confidence が校正されているか、低信頼時に silence / abstention を返せるか。高確率表示だけでは安全な解釈になりません。</li>
<li><strong>長期運用：</strong>within-session の速さだけでなく、tail latency、日跨ぎ安定性、再校正負荷を出しているか。速い demo と deployable loop は別です。</li>
</ul>
<div class="note-box">
<strong>2026-03-17 追補：代表論文を同じ物差しで読む</strong>
<p>
<a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a> は、within-subject では recovered time-points が 65〜82% まで上がる一方、cross-subject では 1〜5% に下がり、学習利得も約 7.5 時間で頭打ちになりました。<a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> は 723 人・500 万語規模でも、sentence-level context、test averaging、MEG &gt; EEG、reading &gt; listening に性能が強く依存すると示しました。<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> は 10 ms 未満推論と silence fallback を示しましたが、固定 decoder は約 15 日で有意に劣化しました。したがって、自然な文字列や音声が出ても、まず <strong>training depth</strong>、<strong>subject route</strong>、<strong>task scaffold</strong>、<strong>fixed decoder horizon</strong> を別々に確認してください。
</p>
</div>
<p>
Chen et al. (2024) は、speech decode で non-causal path が post-onset の auditory feedback を使うと offline score が inflate しうることを示しました。Singh et al. (2025) は、distributed brain recordings を用いた transfer learning が speech decoding の信頼性を押し上げても、shared task structure と calibration route が依然として必要だと示しました。Littlejohn et al. (2025) は 80 ms ごとの streaming brain-to-voice、Wairagkar et al. (2025) は 10 ms 未満の neural-to-voice synthesis と silence fallback を示しましたが、いずれも侵襲系の communication route でございます。さらに Wilson et al. (2025) は long-term unsupervised recalibration の必要性を示し、daily supervised recalibration 自体が別の壁であることを明確にしました。したがって、scalp EEG や一般的な non-invasive BCI が同じ条件なしに同水準を名乗ることはできません。
</p>
<p>
提出物として比較したい場合は、<a href="verification.html#neural-contribution-card">Verification の Neural Contribution Card</a> と <a href="wiki/decode-vs-emulate.html#paper-normalization">Wiki: Decode と Emulate の代表論文比較表</a> を見てください。ここでは <strong>task regime</strong>、<strong>prior scaffold</strong>、<strong>no-brain / LM-only / no-LM / shuffle baseline</strong>、<strong>causal deployment guard</strong>、<strong>subject cooperation</strong>、<strong>training depth / subject route</strong>、<strong>generalization surface</strong>、<strong>online fallback</strong> を固定し、派手な出力をそのまま強い証拠へ読み替えません。
</p>
</section>

<section class="section" id="q2">
<h2 class="section-title">Q. decode（デコーディング）と emulate（エミュレーション）の違いは？</h2>
<p>
A. decodeは“観測を翻訳する”ことで、emulateは“内部状態が時間発展し、介入に反応し、出力を生成する”ことです。
WBEに近づくには、後者を評価できるベンチマーク（介入・反事実・閉ループ）へ寄せる必要があります。
</p>
<p>
2025 年の non-invasive word decode や streaming speech neuroprosthesis は、communication route として非常に重要な前進です。しかし Mind-Upload では、<strong>language prior を超える neural contribution</strong>、<strong>OOD / cross-day 一般化</strong>、<strong>介入後の一致</strong>、<strong>tail latency / silence / recalibration burden</strong>、<strong>hidden state の監査</strong>がそろわない限り、それを emulate や WBE とは読み替えません。ここで前進したのは、まず decode あるいは局所 subsystem closed loop でございます。
</p>
<p><a href="wbe_101.html">入門（WBE 101）</a>と<a href="glossary.html">用語集</a>に加え、<a href="wiki/decode-vs-emulate.html">Wiki: Decode と Emulate</a> も近道です。</p>
</section>

<section class="section" id="q2b">
<h2 class="section-title">Q. LLMやデジタルツインが人っぽく話せたら、それはMind-Upload？</h2>
<p>
A. それだけでは言えません。会話が自然でも、それが<strong>外から見える振る舞いの模倣</strong>なのか、<strong>内部状態や因果構造まで連続している</strong>のかは別問題です。
</p>
<p>
Mind-Uploadで重視するのは、「人っぽく見えるか」だけでなく、条件を変えたときの応答、記憶や学習の連続性、反証条件への耐性が公開されているかです。見た目の自然さは参考にはなりますが、それだけで L4 の本人性主張には進めません。
</p>
<p><a href="wiki/counterfactual-and-perturbation-verification.html">Wiki: 反事実・介入・摂動の検証</a> に、なぜ「自然に話せる」だけでは足りないかを段階で整理しています。</p>
</section>

<section class="section" id="q2c">
<h2 class="section-title">Q. コネクトームと cell type が分かれば、残りはほぼ埋まる？</h2>
<p>
A. まだ言えません。理由は、<strong>「配線と cell type でかなり決まる層」</strong>と、<strong>なお latent のまま残る層</strong>を同じ 1 行で読んではいけないからです。<a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> が示したように、同じ transcriptomic type の内部にも morpho-electric phenotype の幅が残ります。さらに <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> と <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> が押し上げたのも、same-brain の structure-function link や connectome-constrained prediction の前進であって、moment-to-moment の state-complete reconstruction ではございません。
</p>
<p>
この FAQ では、少なくとも次の 4 層を分けます。第一に <strong>fast execution state</strong> として、<a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">Holler et al. (2021)</a> が示した structural prior と平均強度の関係、<a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">Dürst et al. (2022)</a> が示した presynaptic release probability、<a href="https://doi.org/10.1038/nature02617" target="_blank">Matsuzaki et al. (2004)</a>、<a href="https://doi.org/10.1038/s41586-022-05483-6" target="_blank">Vardalaki et al. (2022)</a>、<a href="https://doi.org/10.1016/j.neuron.2025.06.002" target="_blank">Li et al. (2025)</a> が押し上げた postsynaptic AMPAR / silent-synapse state、そして <a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">Mittermaier et al. (2024)</a> が示した human tissue の membrane-state-gated consolidation を含む current synaptic state と、<a href="https://doi.org/10.1126/science.aax6239" target="_blank">Gidon et al. (2020)</a> が示す human dendritic action potential のような branch-specific integration state です。第二に <strong>controller state</strong> として、<a href="https://doi.org/10.1038/s41593-025-02152-5" target="_blank">Benoit et al. (2025)</a> や <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> が押し上げた AIS / excitability / recovery controller です。第三に <strong>slow maintenance-state</strong> として、<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>、<a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a> の sleep-homeostasis、<a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> の myelin / oligodendrocyte support、<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a> と <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a> の astrocyte ensemble、<a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">Kim et al. (2025)</a> の clearance / immune support を含みます。
</p>
<p>
第四に、<strong>human observability ceiling</strong> を別に置きます。human 側で前進しているのは、local ex vivo の dendritic mechanism、structural fragment、<a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">Lucchetti et al. (2025)</a> の macro-biochemical scaffold、<a href="https://doi.org/10.1002/mrm.29998" target="_blank">Baadsvik et al. (2024)</a> の myelin bilayer proxy、<a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> の perturbation-gated excitability proxy、<a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">Dagum et al. (2026)</a> の CSF / glymphatic support-state proxy であって、whole-brain in vivo の current synaptic efficacy や cell-specific immune controller の直読ではありません。Mind-Upload では、ここから <strong>connectome-complete を structural scaffold の前進</strong>として扱い、<strong>emulation-complete</strong> とは言い換えません。短い答えの先としては <a href="wiki/connectome-is-not-enough.html">Wiki: 配線図だけでは足りない理由</a> と <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> が最短です。
</p>
</section>

<section class="section" id="q3">
<h2 class="section-title">Q. じゃあ、何を作れば“前進”になる？</h2>
<p>
A. まずは L0〜L2 が現実的です。つまり「再現できる解析」「比較できるベンチ」「介入予測で検証できるモデル」です。
Mind-Uploadでは、これを“サイトとして運用できる形”に落とします（テンプレ・ログ・ルール）。
</p>
<div class="key-points">
<h4>具体的な成果物</h4>
<ul>
<li><strong>入力：</strong>BIDS/EEG-BIDS + メタデータ + QCログ</li>
<li><strong>手順：</strong>固定パイプライン + 実行ログ + 失敗例</li>
<li><strong>出力：</strong>指標（スコア） + ベースライン差分 + 反証条件の結果</li>
</ul>
</div>
<p>この 3 点がどうつながるかを 1 本の EEG 例で見たい場合は、<a href="wiki/verification-example-walkthrough.html">Wiki: Verification の具体例ウォークスルー</a> が最短です。</p>
</section>

<section class="section" id="q4">
<h2 class="section-title">Q. なぜ“標準化”がそんなに大事？</h2>
<p>
A. 標準がないと、同じことを言っているようで違う入力・違う手順・違う指標を比較してしまい、進捗が見えなくなります。
PDBやBIDS+OpenNeuroなどの事例は、分野が違っても「前進を測れる」状態を作った点が共通しています。
</p>
<p><a href="verification.html#casework">ケースワーク集</a>に設計の型をまとめており、BIDS、OpenNeuro、Validator、benchmark の役割差を先に整理したい場合は <a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: 規格・置き場・Validator・ベンチマーク</a> が近道です。</p>
</section>

<section class="section" id="q5">
<h2 class="section-title">Q. “ベンチマークの罠”って何？</h2>
<p>
A. 指標に勝つことが、現実の目的達成とズレる現象です（Goodhartの罠）。
例えば、データリークや過学習でスコアだけ上がる、実装コストが高すぎて実運用されない、などがあります。
Mind-Uploadでは、失敗例・リーク検査・モデルカードを含めて運用設計します。
</p>
<p><a href="wiki/dataset-splits-and-leakage.html">Wiki: データ分割とデータリーク</a> に、train/test の分け方で数字が壊れる典型例をまとめています。</p>
</section>

<section class="section" id="q5b">
<h2 class="section-title">Q. オフライン精度が高ければ、閉ループでも十分？</h2>
<p>
A. それだけでは言えません。閉ループでは、出力が次の入力や環境を変えるため、end-to-end 遅延、ジッタ、ドリフト、安全停止の設計が必要です。あとから記録済みデータを読むのが得意でも、リアルタイムで安定とは限りません。
</p>
<p>
近年の speech neuroprosthesis は real-time text / audio / voice 出力で大きく前進しました。Littlejohn et al. (2025) は 80 ms ごとの streaming brain-to-voice、Wairagkar et al. (2025) は 10 ms 未満の neural-to-voice synthesis を示しましたが、これはあくまで侵襲系 communication subsystem の within-session 達成です。Wilson et al. (2025) が示す通り、daily supervised recalibration を減らしつつ long-term に維持できるかは別の問題でございます。
</p>
<p>
Mind-Upload では、オフライン精度と L3 閉ループ安定性を分けて読みます。特に <strong>P50/P95/P99 latency</strong>、<strong>silence / abstention</strong>、<strong>recalibration burden</strong>、<strong>cross-day 劣化</strong>を accuracy と別に出していなければ、deployable closed loop と読みません。ここを初歩から整理したい場合は <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> が近道です。
</p>
</section>

<section class="section" id="q6">
<h2 class="section-title">Q. 意識の「ハードプロブレム」に対するスタンスは？</h2>
<p>
A. Mind-Uploadは、ハードプロブレム（Chalmers, 1995）について特定の哲学的立場を前提にしません。
機能主義的アプローチを実装基盤として採用しますが、それが現象的意識の十分条件であるとは主張しません。
代わりに、<strong>検証可能な操作的指標</strong>（PCI-ST、反事実テスト、介入応答一致等）を評価基準とし、
哲学的帰結は結果の解釈段階で議論する立場を取ります。
</p>
<div class="note-box">
<strong>透明性</strong>
<p>
これは重大な制約です。機能的等価性が確認されても、現象的意識の同一性は保証されません。
この限界を明示した上で、測定可能な前進を積み上げます。
</p>
</div>
</section>

<section class="section" id="q7">
<h2 class="section-title">Q. コピー問題（分身のパラドックス）をどう扱う？</h2>
<p>
A. 「スキャン＆コピー」方式では、コピー直後にオリジナルとコピーが独立に分岐するため、
どちらが「本人」かは原理的に決定できません（パーフィットの心理的連続性理論）。
Mind-Uploadでは、<strong>Slow Continuous Mind Uploading</strong>（段階的移行）を主軸に据え、
分断を伴わないプロセスの連続性を工学的要件として設計します。
ただし、この戦略も「どの時点で移行が完了したか」の判定基準を事前に固定する必要があり、
これはクレーム階段 L4 の課題として扱います。
</p>
</section>

<section class="section" id="q8">
<h2 class="section-title">Q. IITとGNWTの実験的検証はどうなった？</h2>
<p>
A. 2025年のCogitate Consortium（敵対的共同研究）が、IITとGNWTの予測を大規模に検証しました。
結果は<strong>双方とも完全には支持されなかった</strong>：IITの後方皮質持続活動は部分的支持のみ、
GNWTの前頭前野イグニッションは報告動作と分離困難でした。
Mind-Uploadではこの結果を受け、特定理論への固執を避け、PCI等の理論非依存な経験的指標を中心に据えています。
</p>
<p>理論の違い自体を先に整理したい場合は、<a href="wiki/consciousness-theory-map.html">Wiki: 意識理論マップ</a> を見ると読みやすくなります。</p>
</section>

<section class="section" id="q9">
<h2 class="section-title">Q. 倫理的課題はどう扱っている？</h2>
<p>
A. WBEは固有の倫理的課題を伴います：(1) エミュレートされた存在の法的地位と権利、
(2) 同意の撤回可能性（停止する権利）、(3) 複製による多重人格の倫理、
(4) アクセス格差と社会的公正。Mind-Uploadでは、技術的検証と並行して、
<strong>倫理的レビュー委員会の設計</strong>をクレーム階段 L5（社会実装）の前提条件として位置づけています。
現時点では技術的基盤（L0-L2）に集中していますが、L3以降の計画には倫理ガバナンスの設計を含みます。
</p>
</section>

<section class="section" id="q10">
<h2 class="section-title">Q. 他のWBEプロジェクトとの違いは？</h2>
<p>
A. 主な既存プロジェクトとの位置づけ：
</p>
<ul>
<li><strong>Blue Brain / Human Brain Project：</strong>大規模シミュレーション重視。Mind-Uploadは検証基盤設計を先行させる点が異なる。</li>
<li><strong>全脳アーキテクチャ・イニシアティブ（WBAI）：</strong>構成論的・ロードマップ重視。Mind-Uploadはベンチマークと反証条件を先に固定する点が補完的。</li>
<li><strong>OpenWorm：</strong>C. elegans全コネクトーム実装。Mind-Uploadはヒト脳の非侵襲計測（EEG）からのアプローチ。</li>
</ul>
<p>
Mind-Uploadの差別化点は、<strong>「検証基盤（Verification Commons）を先に作る」</strong>という戦略です。
</p>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（FAQ）</h2>
<ol>
<li>Tang, J., et al. (2023). Semantic reconstruction from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Chen, Z., Yao, D., Wang, M., et al. (2024). A neural speech decoding framework leveraging deep learning and speech synthesis. <a href="https://doi.org/10.1038/s42256-024-00837-5" target="_blank">doi:10.1038/s42256-024-00837-5</a></li>
<li>Singh, V., Papangelou, A., Sharma, M., et al. (2025). Transfer learning via distributed brain recordings enables reliable speech decoding. <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">doi:10.1038/s41467-025-63825-0</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Gouwens, N. W., et al. (2021). Integrated morphoelectric and transcriptomic classification of cortical GABAergic cells. <a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">doi:10.1038/s41586-020-2907-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Holler, S., et al. (2021). Structure and function of a neocortical synapse. <a href="https://doi.org/10.1038/s41586-020-03134-2" target="_blank">doi:10.1038/s41586-020-03134-2</a></li>
<li>Dürst, C. D., Wiegert, J. S., Schulze, C., et al. (2022). Vesicular release probability sets the strength of individual Schaffer collateral synapses. <a href="https://doi.org/10.1038/s41467-022-33565-6" target="_blank">doi:10.1038/s41467-022-33565-6</a></li>
<li>Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., &amp; Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. <a href="https://doi.org/10.1038/nature02617" target="_blank">doi:10.1038/nature02617</a></li>
<li>Vardalaki, D., Chung, K., &amp; Harnett, M. T. (2022). Filopodia are a structural substrate for silent synapses in adult neocortex. <a href="https://doi.org/10.1038/s41586-022-05483-6" target="_blank">doi:10.1038/s41586-022-05483-6</a></li>
<li>Li, J., et al. (2025). Dynamic redistribution of AMPA receptors toward memory-related neuronal ensembles in mice barrel cortex during sensory learning. <a href="https://doi.org/10.1016/j.neuron.2025.06.002" target="_blank">doi:10.1016/j.neuron.2025.06.002</a></li>
<li>Mittermaier, V., Kononenko, N. L., Jin, Y., et al. (2024). Membrane potential states gate synaptic consolidation in human neocortical tissue. <a href="https://doi.org/10.1038/s41467-024-53901-2" target="_blank">doi:10.1038/s41467-024-53901-2</a></li>
<li>Gidon, A., Zolnik, T. A., Fidzinski, P., et al. (2020). Dendritic action potentials and computation in human layer 2/3 cortical neurons. <a href="https://doi.org/10.1126/science.aax6239" target="_blank">doi:10.1126/science.aax6239</a></li>
<li>Benoit, C. M., Ganea, D. A., Paricio-Montesinos, R., et al. (2025). Axon initial segment dynamics during associative fear learning. <a href="https://doi.org/10.1038/s41593-025-02152-5" target="_blank">doi:10.1038/s41593-025-02152-5</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Xu, W., et al. (2024). Sleep restores an optimal computational regime in cortical networks. <a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">doi:10.1038/s41593-023-01536-9</a></li>
<li>Gibson, E. M., et al. (2014). Neuronal activity promotes oligodendrogenesis and adaptive myelination in the mammalian brain. <a href="https://doi.org/10.1126/science.1252304" target="_blank">doi:10.1126/science.1252304</a></li>
<li>McKenzie, I. A., et al. (2014). Motor skill learning requires active central myelination. <a href="https://doi.org/10.1126/science.1254960" target="_blank">doi:10.1126/science.1254960</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">doi:10.1038/s41593-023-01558-3</a></li>
<li>Suzuki, A., et al. (2011). Astrocyte-neuron lactate transport is required for long-term memory formation. <a href="https://doi.org/10.1016/j.cell.2011.02.018" target="_blank">doi:10.1016/j.cell.2011.02.018</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Williamson, N. R., et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">doi:10.1038/s41586-024-08170-w</a></li>
<li>Kim, J., et al. (2025). Meningeal lymphatics-microglia axis regulates synaptic physiology. <a href="https://doi.org/10.1016/j.cell.2025.02.022" target="_blank">doi:10.1016/j.cell.2025.02.022</a></li>
<li>Lee, J.-C., Wang, C.-Y., Lin, C.-L., &amp; Lu, H.-C. (2022). Synaptic memory survives molecular turnover. <a href="https://doi.org/10.1073/pnas.2211572119" target="_blank">doi:10.1073/pnas.2211572119</a></li>
<li>Lucchetti, F., C&eacute;l&eacute;reau, E., Steullet, P., et al. (2025). Constructing the human brain metabolic connectome with MR spectroscopic imaging reveals cerebral biochemical organization. <a href="https://doi.org/10.1038/s41467-025-66124-w" target="_blank">doi:10.1038/s41467-025-66124-w</a></li>
<li>Baadsvik, E. L., Weiger, M., Froidevaux, R., Schildknecht, C. M., Ineichen, B. V., &amp; Pruessmann, K. P. (2024). Myelin bilayer mapping in the human brain in vivo. <a href="https://doi.org/10.1002/mrm.29998" target="_blank">doi:10.1002/mrm.29998</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Dagum, P., et al. (2026). The glymphatic system clears amyloid-beta and tau from brain to plasma in humans. <a href="https://doi.org/10.1038/s41467-026-68374-8" target="_blank">doi:10.1038/s41467-026-68374-8</a></li>
<li>Guo, C., Pleiss, G., Sun, Y., &amp; Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. <a href="https://proceedings.mlr.press/v70/guo17a.html" target="_blank">PMLR 70:1321-1330</a></li>
<li>Geifman, Y., &amp; El-Yaniv, R. (2017). Selective Classification for Deep Neural Networks. <a href="https://papers.neurips.cc/paper/7073-selective-classification-for-deep-neural-networks" target="_blank">NeurIPS 2017</a></li>
<li>Ji, Z., et al. (2023). Survey of Hallucination in NLG. <a href="https://doi.org/10.1145/3571730" target="_blank">doi:10.1145/3571730</a></li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested Counterfactual Identification. <a href="https://arxiv.org/abs/2107.03190" target="_blank">arXiv:2107.03190</a></li>
<li>Gorgolewski, K. J., et al. (2016). BIDS. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Casali, A. G., et al. (2013). PCI. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Chalmers, D. J. (1995). Facing up to the problem of consciousness. <em>Journal of Consciousness Studies</em>, 2(3), 200-219.</li>
<li>Parfit, D. (1984). <em>Reasons and Persons</em>. Oxford University Press.</li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Shortcuts</h4>
<ul>
<li><a href="index.html">Start →</a></li>
<li><a href="verification.html">Verification →</a></li>
<li><a href="wbe_101.html">WBE 101 →</a></li>
<li><a href="eeg_101.html">EEG 101 →</a></li>
<li><a href="datasets.html">Datasets →</a></li>
<li><a href="glossary.html">Glossary →</a></li>
</ul>
</div>

</aside>
</main>
