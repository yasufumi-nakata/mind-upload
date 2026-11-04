"""Authored evidence summaries and a conditional 2050 research plan, in two languages.

The status labels are qualitative editorial summaries, not completion percentages.
The five planning windows are proposed review dates, not literature forecasts.
"""

DOMAINS = [
    dict(key='structure', title=('構造を地図にする', 'Map the wiring'),
         status=('小型動物・局所で実証', 'Small animals / local tissue'),
         short=('ハエ脳・CNS、哺乳類の局所回路', 'Fly brain/CNS; local mammalian circuits'),
         next=('哺乳類全脳と、接続の誤りの管理', 'Whole mammalian brains; control wiring errors'),
         evidence=('FlyWireは雌成体脳の139,255ニューロンを再構成しました。BANCとMaleCNSは脳と腹側神経索を含む別個体の資源です。MICrONSの哺乳類データは視覚野の部分体積です。',
                   'FlyWire reconstructed 139,255 neurons in an adult female brain. BANC and MaleCNS are separate brain-and-cord resources. The mammalian MICrONS dataset covers part of visual cortex.'),
         refs='[[ADD196]][[ADD199]][[ADD188]][[6TNZ57MZ]]',
         tasks=(('必要な解像度と、欠損・誤結合の許容範囲を機能テストから決める。', 'Choose resolution and tolerable missing/false connections using functional tests.'),
                ('切片間の接続と自動校正を含め、全脳の処理時間・費用を測る。', 'Measure whole-brain throughput and cost, including cross-section tracing and automated correction.'))),
    dict(key='recording', title=('活動と状態を読む', 'Read activity and state'),
         status=('大規模記録・部分対応', 'Large recordings; partial pairing'),
         short=('魚の活動予測、マウスの構造との対応', 'Fish activity; paired mouse structure/activity'),
         next=('同じ個体の状態・分子情報との統合', 'Pair state and molecular data in one individual'),
         evidence=('ZAPBenchは幼生ゼブラフィッシュの7万超のニューロンのカルシウム活動を扱います。MICrONSでは15,439細胞を機能記録とEMで手作業対応付けしています。活動記録は、そのまま全状態の読み出しではありません。',
                   'ZAPBench uses calcium activity from over 70,000 neurons in a larval zebrafish. MICrONS manually matched 15,439 cells between functional recordings and EM. Recording activity does not read every relevant state variable.'),
         refs='[[FHPYMIG8]][[6TNZ57MZ]]',
         tasks=(('記録の時間分解能・観測ノイズと、見えない状態の影響を分けて測る。', 'Separate temporal resolution and measurement noise from the effects of unobserved states.'),
                ('同じ個体で構造・活動・必要な分子情報を対応付け、評価用データを確保する。', 'Pair structure, activity and necessary molecular data in one individual; reserve evaluation data.'))),
    dict(key='dynamics', title=('機能をモデル化する', 'Reconstruct function'),
         status=('限定課題で予測を検証', 'Predictions tested on limited tasks'),
         short=('ハエの感覚運動・視覚応答を予測', 'Fly sensorimotor and visual predictions'),
         next=('未知の介入、学習・可塑性への対応', 'Unseen interventions; learning and plasticity'),
         evidence=('Shiuらはハエの感覚運動機能、Lappalainenらは視覚系の接続制約モデルを実験データと照合しました。これらの結果を、元の個体の全機能や学習履歴の復元まで広げることはできません。',
                   'Shiu et al. tested fly sensorimotor functions; Lappalainen et al. compared a connectome-constrained visual model with experimental data. Neither establishes recovery of all functions or the original individual’s learning history.'),
         refs='[[V4GV7JAJ]][[XMYSQXY8]]',
         tasks=(('接続から伝達特性・必要な状態を推定し、未知の刺激と介入で確かめる。', 'Infer transmission properties and necessary states from measurements; test unseen stimuli and interventions.'),
                ('学習則を組み込み、保持・忘却・再学習が長期に対応するかを調べる。', 'Include learning rules and test retention, forgetting and relearning over time.'))),
    dict(key='preservation', title=('必要な情報を残す', 'Preserve the needed information'),
         status=('微細構造の保存を実証', 'Ultrastructure preserved'),
         short=('動物組織の微細構造を保存', 'Preserved ultrastructure in animal tissue'),
         next=('記憶に必要な情報が残るかの実証', 'Show that memory-relevant information survives'),
         evidence=('ASCはウサギ・ブタの脳組織で微細構造の保存を示しました。保存後に機能や記憶を復元した研究ではありません。エングラムの局所構造の研究も、任意の記憶を読み出す手法とは区別します。',
                   'ASC demonstrated preserved ultrastructure in rabbit and pig brain tissue, not restored function or memory. Local engram-structure studies are also distinct from methods for reading arbitrary memories.'),
         refs='[[SDSWEA5J]][[LP5F3H2Q]]',
         tasks=(('保存・固定・撮像で何が失われるかを、構造と分子状態ごとに評価する。', 'Measure which structural and molecular information preservation, fixation and imaging lose.'),
                ('学習済み個体で、保存情報から独立した記憶課題を再現できるか試す。', 'Test whether preserved information supports an independent memory task in a previously trained individual.'))),
    dict(key='compute', title=('計算し、身体とつなぐ', 'Compute and connect to a body'),
         status=('計算基盤・限定モデル', 'Platforms and limited models'),
         short=('回路シミュレーターと身体連成モデル', 'Circuit simulators and embodied models'),
         next=('全脳規模の費用・遅延・長期安定性', 'Whole-brain cost, latency and long-run stability'),
         evidence=('NEURON、BMTK、SpiNNakerはモデル計算の基盤です。BAAIWormは神経・身体・環境を結びますが、神経系と行動の対象は限定されています。計算機の演算性能だけからWBEの実行可能性は決まりません。',
                   'NEURON, BMTK and SpiNNaker support neural-model computation. BAAIWorm links neural, body and environmental models but covers limited neurons and behaviours. Processor arithmetic throughput alone does not establish WBE feasibility.'),
         refs='[[Q8SGY2SV]][[9DXWPDVH]][[ADD206]][[ADD203]][[XKB4CG64]]',
         tasks=(('必要な詳細度で、メモリー・通信・電力・実時間比を実測する。', 'Measure memory, communication, energy and speed relative to real time at the required model detail.'),
                ('身体からの感覚帰還と学習を含め、長時間の動作と状態保存・再開を検証する。', 'Test long runs and state save/resume with sensory feedback and learning.'))),
    dict(key='validation', title=('「その個体」を確かめる', 'Validate the original individual'),
         status=('枠組みあり・統合未実証', 'Frameworks; integrated goal unmet'),
         short=('人工回路の復元比較と機能テスト', 'Synthetic reconstruction and functional tests'),
         next=('個体固有の記憶を含む全工程の検証', 'Validate the full chain, including individual memory'),
         evidence=('Brain Emulation Challengeは正解既知の人工回路で復元法を比較する枠組みです。忠実度研究は用途に応じた機能テストを提案します。本サイトで確認した文献では、人の個体固有の記憶を保持する全脳再現は実証されていません。',
                   'The Brain Emulation Challenge compares reconstruction methods on synthetic circuits with known ground truth. Fidelity research proposes purpose-dependent functional tests. The reviewed literature does not demonstrate whole-brain reproduction retaining a human individual’s memories.'),
         refs='[[CCCHALLENGE]][[XKB4CG64]][[REPORTFINAL]]',
         tasks=(('平均・他個体モデルを対照に、学習に使わない個体固有の応答・記憶で盲検評価する。', 'Use average and other-individual controls; evaluate held-out individual responses and memories under blinded assessment.'),
                ('別チーム・別個体で再現し、成功条件だけでなく失敗範囲も公開する。', 'Reproduce results with independent teams and additional individuals; report failure boundaries.'))),
]

PHASES = [
    dict(year='2030', window='2026–2030', title=('測定と誤差を固める', 'Establish measurements and error limits'),
         short=('何をどこまで測ればよいか', 'What must be measured, and how well?'),
         work=('人工回路と既存のハエモデルでM1・M2を進め、同じ試料の構造・活動データ、再現コード、誤差と機能の関係を揃えます。',
               'Advance M1–M2 with synthetic circuits and existing fly models. Produce paired structure/activity data, reproduction code and links between reconstruction error and function.'),
         gate=('未使用の回路・刺激・介入で予測を検証し、どの測定誤差が結果を壊すかを再現可能に説明できます。',
               'Validate predictions on held-out circuits, stimuli and interventions, and reproducibly identify which measurement errors break them.'),
         stop=('再現できなければ、データの版・測定・モデルを修正し、大規模化の判定を保留します。',
               'If reproduction fails, correct data versions, measurements or models before approving scale-up.')),
    dict(year='2035', window='2031–2035', title=('個体と記憶を実証する', 'Demonstrate individual and memory fidelity'),
         short=('小型動物・局所回路で核心を検証', 'Test the core idea in small systems'),
         work=('M3・M4として、学習した小型動物や哺乳類の局所回路で、構造・状態から元の個体の応答を復元します。学習履歴の異なる個体を比較します。',
               'For M3–M4, reconstruct responses from structure and state in trained small animals or local mammalian circuits. Compare individuals with different learning histories.'),
         gate=('評価する記憶の答えを学習に使わず、元の個体のモデルが平均・他個体モデルより事前基準を満たして優れ、独立に再現されます。',
               'Without training on memory-test answers, the original-individual model meets prespecified superiority criteria against average/other-individual controls, with independent replication.'),
         stop=('構造だけで不足するなら分子・機能情報を追加します。情報の十分性が示せなければ、その取得方式による人への展開を見直します。',
               'Add molecular or functional data if structure is insufficient. Reconsider the acquisition route for humans if information sufficiency remains unsupported.')),
    dict(year='2040', window='2036–2040', title=('哺乳類で統合・拡張する', 'Integrate and scale in mammals'),
         short=('部分の成功を全脳へつなぐ', 'Bridge partial success to whole brains'),
         work=('撮像・再構成・モデル化・身体との相互作用をつなぎ、より大きい哺乳類回路へ拡張します。全脳範囲と長期学習の検証を目標にします。',
               'Connect imaging, reconstruction, modelling and body interaction while expanding to larger mammalian circuits, targeting whole-brain coverage and long-term learning tests.'),
         gate=('拡張しても個体差・学習の検証を維持し、欠落領域、総処理時間、費用、メモリー、実時間比を実測で示せます。',
               'Retain tests of individual differences and learning at larger scale; measure missing coverage, total processing time, cost, memory and speed relative to real time.'),
         stop=('忠実度や計算費用が基準を外れるなら、測定方式・詳細度・並列化を改めます。接続図の完成だけで次へ進みません。',
               'Revise acquisition, model detail or parallelisation if fidelity or cost misses the criteria. A completed wiring map alone does not pass this gate.')),
    dict(year='2045', window='2041–2045', title=('人への適用条件を確かめる', 'Establish conditions for human application'),
         short=('種の違いと全脳取得を検証', 'Test species differences and whole-brain acquisition'),
         work=('人の細胞・局所回路で、動物から移した仮定を評価します。同一個体の生前記録と取得情報を対応付ける設計、全脳取得・モデル構築の工程を整えます。',
               'Test animal-derived assumptions in human cells and local circuits. Establish a design linking prior recordings to acquired data from the same individual, plus whole-brain acquisition and modelling workflows.'),
         gate=('対象機能に必要な情報を取得できる根拠、欠損・領域差の評価、全工程の実行資源、独立した評価データが揃います。',
               'Establish evidence for acquiring functionally necessary information, assessed losses and regional differences, end-to-end resources, and independent evaluation data.'),
         stop=('人で必要な状態を測れない、保存で失う、または元の個体との比較が成立しない場合は、2050年の統合目標を再設定します。',
               'Reset the 2050 integration target if necessary human states cannot be measured or preserved, or valid comparison with the original individual is unavailable.')),
    dict(year='2050', window='2046–2050', title=('人の全脳再現を独立検証する', 'Independently test human whole-brain reproduction'),
         short=('条件を満たした統合プロトタイプ', 'An integrated prototype that passes the gates'),
         work=('それまでの条件を満たした場合に、特定の人の測定情報から全脳モデルを構築し、活動・学習済み情報・学習能力・身体との相互作用を統合評価します。',
               'Only after the preceding gates are met, build a whole-brain model from a particular person’s measurements and evaluate activity, previously learned information, learning capacity and body interaction together.'),
         gate=('事前に定めた機能・時間尺度で元の個体との対応、平均・他個体対照への優位、別チームによる再現、運用の安定性を示せます。',
               'Demonstrate correspondence over prespecified functions and timescales, superiority to average/other-individual controls, independent replication and operational stability.'),
         stop=('一部だけ成功した場合は、その機能と範囲の成果として報告します。残る条件を飛ばして全脳再現の完成とはしません。',
               'Report partial success at its demonstrated functional and anatomical scope; do not declare the whole-brain target met by skipping remaining conditions.')),
]

def status_grid(lang, detail=False):
    n=0 if lang=='ja' else 1
    parts=['<div class="status-grid'+(' status-detail' if detail else '')+'">']
    for i,d in enumerate(DOMAINS,1):
        parts.append(f'<article class="status-card"><div class="status-heading"><span class="status-number">{i:02}</span><h3>{d["title"][n]}</h3></div><p class="status-badge">{d["status"][n]}</p>')
        parts.append('<p class="status-current"><b>'+('到達' if n==0 else 'Now')+'</b> '+(d['evidence'][n] if detail else d['short'][n])+d['refs']+'</p>')
        if detail:
            parts.append('<details><summary>'+('残る主要課題 2件' if n==0 else 'Two major remaining tasks')+'</summary><ol class="remaining-tasks">')
            for j,t in enumerate(d['tasks'],1):
                parts.append(f'<li><span class="task-id">R{2*(i-1)+j:02}</span> {t[n]}</li>')
            parts.append('</ol></details>')
        parts.append('<p class="status-next"><b>'+('次の壁' if n==0 else 'Next barrier')+'</b> '+d['next'][n]+'</p></article>')
    parts.append('</div>')
    return ''.join(parts)

def horizon(lang, detail=False):
    n=0 if lang=='ja' else 1
    parts=['<ol class="horizon'+(' horizon-detail' if detail else ' horizon-mini')+'">']
    for p in PHASES:
        parts.append('<li><span class="horizon-year">'+('〜' if n==0 else 'By ')+p['year']+'</span><h3>'+p['title'][n]+'</h3><p>'+p['short'][n]+'</p>')
        if detail:
            parts.append('<details><summary>'+('達成条件と見直し' if n==0 else 'Gate and fallback')+'</summary><p><strong>'+p['window']+'</strong> '+p['work'][n]+'</p><p><strong>'+('通過条件：' if n==0 else 'Pass: ')+ '</strong>'+p['gate'][n]+'</p><p><strong>'+('未達の場合：' if n==0 else 'If unmet: ')+'</strong>'+p['stop'][n]+'</p></details>')
        parts.append('</li>')
    parts.append('</ol>')
    return ''.join(parts)
