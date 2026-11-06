"""Authored evidence summaries and a conditional 2050 research plan, in two languages.

The status labels are qualitative editorial summaries, not completion percentages.
The five planning windows are proposed review dates, not literature forecasts.
"""

from html import escape

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
         tasks=(('記録の時間分解能・観測ノイズと、見えない状態の影響を分けて測る。グリアの活動やペプチドの放出・受容体発現も、追加測定の候補として評価する。', 'Separate temporal resolution and measurement noise from unobserved states. Evaluate glial activity, peptide release and receptor expression as candidates for additional measurement.'),
                ('同じ個体で構造・活動・必要な分子情報を対応付け、評価用データを確保する。シナプス外の信号を省ける範囲も機能テストで調べる。', 'Pair structure, activity and necessary molecular data in one individual; reserve evaluation data. Test which functions tolerate omitting extrasynaptic signals.'))),
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
         tasks=(('保存・固定・撮像で何が失われるかを、構造と分子状態ごとに評価する。グリアやシナプス外伝達についても、形態の保存と機能に必要な状態の保存を区別する。', 'Measure structural and molecular losses during preservation, fixation and imaging. For glia and extrasynaptic signalling, distinguish retained morphology from retained functionally necessary states.'),
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
         tasks=(('平均・他個体モデルを対照に、モデル調整に使わない個体固有の応答・記憶で盲検評価する。', 'Use average and other-individual controls; evaluate held-out individual responses and memories under blinded assessment.'),
                ('別チーム・別個体で追試し、成功条件だけでなく失敗範囲も公開する。', 'Reproduce results with independent teams and additional individuals; report failure boundaries.'))),
]

PHASES = [
    dict(year='2030', window='2026–2030', title=('測定と誤差を固める', 'Establish measurements and error limits'),
         short=('何をどこまで測ればよいか', 'What must be measured, and how well?'),
         work=('人工回路と既存のハエモデルでM1・M2を進め、同じ試料の構造・活動データ、再現コード、誤差と機能の関係を揃えます。取得・校正の速度と費用、計算資源の基準値も実測します。',
               'Advance M1–M2 with synthetic circuits and existing fly models. Produce paired structure/activity data, reproduction code and links between reconstruction error and function. Measure baseline acquisition/correction throughput, costs and computing resources.'),
         gate=('未使用の回路・刺激・介入で予測を検証し、どの測定誤差が結果を壊すかを再現可能に説明できます。撮像体積V、装置1台の実効速度q、台数nから取得年数V/(12qn)を示し、試料準備・校正・独立検証の時間と費用は別に測ります。',
               'Validate held-out circuits, stimuli and interventions, and reproducibly identify errors that break predictions. Report acquisition years V/(12qn) from tissue volume V, effective monthly throughput q per instrument and instrument count n; measure preparation, correction and independent-validation time and cost separately.'),
         stop=('再現できなければ、データの版・測定・モデルを修正し、大規模化の判定を保留します。',
               'If reproduction fails, correct data versions, measurements or models before approving scale-up.')),
    dict(year='2035', window='2031–2035', title=('個体と記憶を実証する', 'Demonstrate individual and memory fidelity'),
         short=('小型動物・局所回路で核心を検証', 'Test the core idea in small systems'),
         work=('M3・M4として、学習した小型動物や哺乳類の局所回路で、構造・状態から元の個体の応答を復元します。学習履歴の異なる個体を比較します。',
               'For M3–M4, reconstruct responses from structure and state in trained small animals or local mammalian circuits. Compare individuals with different learning histories.'),
         gate=('評価する記憶課題の答えをモデル調整に使わず、元の個体のモデルが平均・他個体モデルより事前基準を満たして優れ、独立した追試が成立します。選んだ行動の感覚帰還を検証し、個体数・セッション数、δ・εと区間推定を報告します。取得・校正速度と費用の実測を更新します。',
               'Without training on memory-test answers, the original-individual model meets prespecified superiority criteria against average/other-individual controls, with independent replication. Test sensory feedback for selected behaviours; report individuals, sessions, δ, ε and interval estimates. Update measured acquisition/correction throughput and cost.'),
         stop=('構造だけで不足するなら分子・機能情報を追加します。情報の十分性が示せなければ、その取得方式による人への展開を見直します。',
               'Add molecular or functional data if structure is insufficient. Reconsider the acquisition route for humans if information sufficiency remains unsupported.')),
    dict(year='2040', window='2036–2040', title=('哺乳類で統合・拡張する', 'Integrate and scale in mammals'),
         short=('部分の成功を全脳へつなぐ', 'Bridge partial success to whole brains'),
         work=('撮像・再構成・モデル化・身体との相互作用をつなぎ、より大きい哺乳類回路へ拡張します。全脳範囲と長期学習の検証を目標にします。',
               'Connect imaging, reconstruction, modelling and body interaction while expanding to larger mammalian circuits, targeting whole-brain coverage and long-term learning tests.'),
         gate=('拡張しても個体差・学習の検証を維持し、欠落領域、総処理時間、費用、メモリー、実時間比を実測で示せます。自動追跡・校正が全脳で許容誤差を満たすことを前提とし、手動修正が残る場合はその人時と費用も計上します。',
               'Retain individual-difference and learning tests at scale; measure missing coverage, total time, cost, memory and real-time ratio. Automated tracing/correction must meet whole-brain error tolerances; include person-hours and cost wherever manual correction remains.'),
         stop=('忠実度や計算費用が基準を外れるなら、測定方式・詳細度・並列化を改めます。接続図の完成だけで次へ進みません。',
               'Revise acquisition, model detail or parallelisation if fidelity or cost misses the criteria. A completed wiring map alone does not pass this gate.')),
    dict(year='2045', window='2041–2045', title=('人への適用条件を確かめる', 'Establish conditions for human application'),
         short=('種の違いと全脳取得を検証', 'Test species differences and whole-brain acquisition'),
         work=('人の細胞・局所回路で、動物から移した仮定を評価します。同一個体の生前記録と取得情報を対応付ける設計、全脳取得・モデル構築の工程を整えます。',
               'Test animal-derived assumptions in human cells and local circuits. Establish a design linking prior recordings to acquired data from the same individual, plus whole-brain acquisition and modelling workflows.'),
         gate=('対象機能ごとに、生前記録の種類・期間・反復数・空間範囲と、評価用に留保するデータを事前登録します。試料取得までの経過時間、終末期の状態、固定法と分子・構造の損失を記録し、審査・同意・試料提供の体制と所要時間を工程へ入れます。比較の検出力と全工程の資源を示せなければ通過しません。',
               'Preregister prior-recording modalities, duration, repeats, spatial coverage and held-out evaluation data for each target function. Record acquisition delay, terminal condition, fixation and molecular/structural losses. Include review, consent, sample-provision arrangements and their lead times. Passing requires adequate comparison power and end-to-end resources.'),
         stop=('人で必要な状態を測れない、保存で失う、または元の個体との比較が成立しない場合は、2050年の統合目標を再設定します。',
               'Reset the 2050 integration target if necessary human states cannot be measured or preserved, or valid comparison with the original individual is unavailable.')),
    dict(year='2050', window='2046–2050', title=('人の全脳再現を独立検証する', 'Independently test human whole-brain reproduction'),
         short=('条件を満たした統合プロトタイプ', 'An integrated prototype that passes the gates'),
         work=('それまでの条件を満たした場合に、特定の人の測定情報から全脳モデルを構築し、活動・学習済み情報・学習能力・身体との相互作用を統合評価します。',
               'Only after the preceding gates are met, build a whole-brain model from a particular person’s measurements and evaluate activity, previously learned information, learning capacity and body interaction together.'),
         gate=('生前記録の未使用データと、取得条件が機能を損なう範囲を示し、事前の機能・時間尺度で個体との対応、平均・他個体対照への優位、別チームの追試、運用の安定性を検証します。撮像だけを5年に収める場合でも、表3の丸め値からExLSFMで約6.8倍、EMで約333.4倍の総取得速度が必要です。準備・再構成・校正・機能検証の時間は別枠です。[[EVWH7H32]]',
               'Use held-out prior recordings and assess how acquisition conditions affect function. Test individual correspondence, advantages over average/other-individual controls, independent replication and operational stability at prespecified functions/timescales. Fitting imaging alone into five years would require about 6.8× ExLSFM or 333.4× EM aggregate throughput relative to rounded Table 3 estimates. Preparation, reconstruction, correction and functional validation need separate time allowances.[[EVWH7H32]]'),
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
    note=('各年は、研究の進捗を比較しやすくするために本サイトが5年刻みで置いた点検時期です。実測速度や成功確率から導いた完成年ではなく、条件が満たされなければ後ろへ移します。',
          'Each year is an editorial review window spaced five years apart to compare progress. These are not completion dates derived from measured throughput or success probabilities; unmet conditions move later windows back.')
    parts=['<p class="small">'+note[n]+'</p><ol class="horizon'+(' horizon-detail' if detail else ' horizon-mini')+'">']
    for p in PHASES:
        parts.append('<li><span class="horizon-year">'+p['year']+('年の点検' if n==0 else ' review')+'</span><h3>'+p['title'][n]+'</h3><p>'+p['short'][n]+'</p>')
        if detail:
            parts.append('<details><summary>'+('達成条件と見直し' if n==0 else 'Gate and fallback')+'</summary><p><strong>'+p['window']+'</strong> '+p['work'][n]+'</p><p><strong>'+('通過条件：' if n==0 else 'Pass: ')+ '</strong>'+p['gate'][n]+'</p><p><strong>'+('未達の場合：' if n==0 else 'If unmet: ')+'</strong>'+p['stop'][n]+'</p></details>')
        parts.append('</li>')
    parts.append('</ol>')
    return ''.join(parts)


def acquisition_calculator(lang):
    """Illustrative acquisition time, with pre-expansion-equivalent volume units."""
    ja = lang == 'ja'
    fields = [
        ('volume', '元の組織体積 V (mm³)', 'Original tissue volume V (mm³)', 1200000, 0.001, 2000000, 'any'),
        ('rate', '1台の実効撮像速度 q (mm³/月)', 'Effective rate per instrument q (mm³/month)', 8.8, 0.000001, 1000000000, 'any'),
        ('instruments', '並行稼働する台数 n', 'Instruments operating in parallel n', 333, 1, 1000000000, '1'),
        ('target', '撮像に割り当てる年数 T', 'Years allocated to imaging T', 5, 0.001, 10000, 'any'),
    ]
    labels = ''.join(
        f'<label for="acq-{key}">{escape(jp if ja else en)}<input id="acq-{key}" type="number" value="{value:g}" min="{lo:g}" max="{hi:g}" step="{step}" required></label>'
        for key, jp, en, value, lo, hi, step in fields
    )
    heading = '台数と速度から撮像期間を計算する' if ja else 'Estimate imaging time from instruments and throughput'
    buttons = ('<button type="button" data-acq-preset="exlsfm">ExLSFMの仮定値</button> <button type="button" data-acq-preset="em">EMの投影値</button>' if ja else
               '<button type="button" data-acq-preset="exlsfm">ExLSFM assumptions</button> <button type="button" data-acq-preset="em">EM projected rate</button>')
    scope = ('速度qは、拡大前の組織体積へ換算した実効値です。休止時間を別途もう一度差し引かないでください。初期値はCollinsらの表1・2から、EMは0.3 mm³/月・200台、ExLSFMは802÷4.5³ ≈ 8.8 mm³/月・333台です。解像度と技術成熟度は異なり、同じ性能を実測比較した値ではありません。[[EVWH7H32]]' if ja else
             'Rate q is effective throughput expressed as original, pre-expansion tissue volume. Do not deduct downtime again if it is already included. From Collins et al. Tables 1–2, presets use 0.3 mm³/month and 200 instruments for EM, and 802/4.5³ ≈ 8.8 mm³/month and 333 instruments for ExLSFM. Resolution and maturity differ; these are not measured comparisons at identical performance.[[EVWH7H32]]')
    limits = ('装置を独立に並列運転でき、速度が一定という仮定です。表3の期間は丸め値のため、ここでの速度からの再計算とは小さな差が出ます。試料準備、再撮像、通信、再構成、校正、モデル化、機能検証の時間は含めません。この計算から2050年の実現可能性は判定できません。' if ja else
              'Assumes independent parallel instruments and constant effective throughput. Recalculation from rates differs slightly from the rounded durations in Table 3. Excludes preparation, repeat imaging, transfer, reconstruction, correction, modelling and functional validation. This calculation cannot establish feasibility by 2050.')
    formula = ('撮像年数' if ja else 'Imaging years')+' = V / (12 × q × n); '+('目標に必要な総速度' if ja else 'Required aggregate rate')+' = V / (12 × T).'
    return '<div class="calculator" id="acquisition-calculator"><h3>'+heading+'</h3><p>'+buttons+'</p><p class="small">'+scope+'</p><div class="calc-fields">'+labels+'</div><div id="acq-result" role="status" aria-live="polite"></div><p class="small">'+formula+'</p><p class="small">'+limits+'</p></div>'
