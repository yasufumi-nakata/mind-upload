"""Complementary, evidence-grounded research routes toward whole-brain emulation.

These are editorial research proposals. Shared reference IDs keep the Japanese
and English renderings aligned; the site generator resolves [[ID]] citations.
"""

from html import escape


ROUTES = ({'key': 'structure',
  'title': ['コネクトームから機能モデルを復元する', 'Reconstruct from a connectome'],
  'question': ['脳の地図を、予測できるモデルへ。', 'Turn a brain map into a model that predicts.'],
  'short': [['個々のニューロンの接続を使う感覚運動モデルと、型・位置で接続を共有する視覚モデルがあります。',
             'Sensorimotor models use neuron-specific wiring; visual models can share connections by cell type '
             'and position.'],
            ['一つの結果を再現し、固定する値を決めて、表現できる単位で接続を変えます。',
             'Reproduce one result, specify fixed quantities and vary wiring at units the model represents.'],
            ['その課題・推定条件で必要な精度を絞り、別課題への一般性と個体の応答を検査できます。',
             'Narrow required precision for that task and estimation regime, then test generality and individual '
             'responses.']],
  'steps': [['ShiuらはFlyWireの個々のニューロンの接続から感覚運動機能を予測しました。Lappalainenらは局所の視覚系再構成を組み合わせ、細胞型と相対位置で接続を共有する合意モデルをオプティカルフロー推定課題に合わせています。公開モデルを一つ再現するところから始められます。',
             'Shiu et al. predicted sensorimotor functions using neuron-specific FlyWire connectivity. '
             'Lappalainen et al. combined local visual reconstructions into a consensus model sharing connections '
             'by cell type and relative position, optimized for motion estimation. Begin by reproducing one '
             'public model.'],
            ['最初は他の値を固定し、一種類の接続の誤りを加えます。再同定する場合は、変更した接続を維持し、学習情報・調整可能な値・予算を条件間でそろえます。平均化とシャッフルは各モデルの表現に合わせます。別個体を使う比較は、課題の回路・半球・細胞対応が確かめられた範囲に限ります。',
             'Start by holding other quantities fixed and adding one connectivity-error type. For refitting, '
             'retain altered wiring and match training information, adjustable quantities and budgets across '
             'conditions. Define averaging and shuffles for each representation. Cross-individual comparisons '
             'require verified circuit, hemisphere and cell correspondence.'],
            ['得られた感度曲線は、その課題と固定・再同定条件での取得精度を考える根拠になります。別の表現・課題では、まず傾向の一般性を検査します。同じ個体の活動を対応付けられれば、個別の測定が平均モデルより応答を説明するかを調べられます。',
             'Sensitivity curves can guide acquisition precision for the tested task and fixed/refit regime. '
             'Across representations and tasks, first test whether trends generalize. With activity from the same '
             'individual, test whether individual measurements explain responses better than an average model.']],
  'evidence_refs': ['ADD196', 'V4GV7JAJ', 'XMYSQXY8'],
  'extra_refs': ['ISSUE284_SCHLEGEL2024', 'ADD190'],
  'limit': ['固定試験の低下は、再同定でも回復できないことを意味しません。Lappalainenのモデルでは型×相対位置の平均が既に使われ、個々の細胞の誤りには派生モデルが必要です。複数コネクトームの共通領域が、対象課題の入出力まで覆うとは限りません。',
            'A decline with fixed parameters does not show that refitting cannot recover performance. Lappalainen '
            'already averages by type and relative position; neuron-specific errors require a derived model. '
            'Shared connectome coverage need not include all task inputs and outputs.'],
  'branch': ['基準を再現できなければ版・入力・前処理を確かめます。誤りに敏感なら、取得・校正へ精度の要求を返します。固定試験だけで崩れた場合は、評価データを分けて再同定を試せます。接続だけでは差を説明できなければ、活動・分子・状態の測定へ進みます。',
             'If the baseline fails to reproduce, check versions, inputs and preprocessing. Sensitivity to errors '
             'informs acquisition and proofreading requirements. Failure with fixed parameters can motivate a '
             'refit with separate evaluation data. If wiring does not explain differences, test functional, '
             'molecular or state measurements.'],
  'link': ['action.html#projects', '最初の比較実験へ', 'Start the comparison experiment']},
 {'key': 'state',
  'title': ('活動から、必要な情報を絞る', 'Identify necessary information from activity'),
  'question': ('測る情報を増やす前に、何が効くかを確かめます。', 'Test which measurements make a difference.'),
  'short': (('構造と活動を対応付けたMICrONS、活動予測のZAPBench、推定の不確実性を扱う手法があります。',
             'MICrONS pairs structure and activity; ZAPBench benchmarks activity prediction; inference methods '
             'represent parameter uncertainty.'),
            ('同じ観測に合うモデルを比較し、未知の応答を見分けるために必要な追加測定を選びます。',
             'Compare models that fit the same observations and select measurements that distinguish their unseen '
             'responses.'),
            ('機能に必要な状態の候補を絞り、構造からの復元とつなげられます。',
             'Narrow candidate states needed for function and connect them to structural reconstruction.')),
  'steps': (('MICrONSはマウス視覚野の一部で構造と活動を対応付け、ZAPBenchは幼生ゼブラフィッシュの活動予測を比較します。Gonçalvesらの手法は、神経回路モデルのパラメーターを一つに決めず、観測に適合する事後分布として推定する例を示しています。',
             'MICrONS pairs structure and activity in part of mouse visual cortex; ZAPBench compares activity '
             'prediction in larval zebrafish. Gonçalves et al. demonstrate inference of posterior distributions '
             'over neural-model parameters, rather than forcing a single parameter solution.'),
            ('正解の分かる人工回路で、観測ノイズと測定項目を変え、推定範囲が正解を含むかを検査します。次に生物のデータで、同じ記録に合うモデルが未知の刺激・介入をどう予測するか比較します。予測が分かれる測定を候補にし、追加データで実際に区別できるかを確かめます。 '
             '学習則Gもこのルートで調べます。既知Gの人工回路で観測条件を検査した後、学習中の経過から規則の候補を絞り、未使用の報酬変更・消去・逆転で予測を比べます。予測が再現すれば、長期学習を身体との循環で試すルート3へ進めます。実験の手順と根拠を示します。',
             'In synthetic circuits with known truth, vary noise and recorded variables and check whether '
             'inferred ranges cover the truth. In biological data, compare predictions for unseen stimuli and '
             'interventions across models that fit the same recordings. Select measurements where predictions '
             'diverge, then test whether added data distinguish them. Use this route to identify G as well. First '
             'test observation conditions in artificial circuits with known rules, then constrain candidates with '
             'learning trajectories and compare predictions for held-out reward changes, extinction and reversal. '
             'Reproducible predictions support testing longer learning in route 3 with a body. See the procedure '
             'and evidence.'),
            ('追加測定による改善が留保データでも続けば、その測定を取得工程へ組み込む根拠になります。構造の精度だけを上げるのか、分子・活動・可塑性の情報も残すのかを選び、個体の記憶を検証する計画へつなげます。',
             'If improvement persists on held-out data, it supports adding that measurement to acquisition. This '
             'helps choose between finer structure and additional molecular, activity or plasticity information, '
             'informing a plan to test individual memory.')),
  'evidence_refs': ('6TNZ57MZ', 'FHPYMIG8', 'ISSUE285_GONCALVES2020'),
  'extra_refs': ('274IXB72', 'ADD190'),
  'limit': ('MICrONSの対象は局所体積で、ZAPBenchの評価入力にコネクトームは含まれません。事後分布はモデルと事前分布の仮定に依存します。活動予測の一致と、生物の機構を同定したことは分けて判定します。',
            'MICrONS covers a local volume, and connectomes are not inputs to the ZAPBench evaluation. Posteriors '
            'depend on model and prior assumptions. Predictive agreement and identification of biological '
            'mechanisms require separate judgments.'),
  'branch': ('候補が絞れない場合は、測定時間や入力条件を変え、予測が分かれる観測を探します。追加測定でも改善しなければ、モデルの形や評価課題を見直します。この結果も、測定の優先順位と残る不確実性を見直す材料になります。',
             'If candidates remain indistinguishable, vary recording times or inputs to seek discriminating '
             'observations. If added measurements do not improve prediction, revisit the model class or '
             'evaluation task. The result still helps reassess measurement priorities and remaining uncertainty.'),
  'link': ('future.html#gates', '復元手法を検査するマイルストーンへ', 'Explore the reconstruction milestones')},
 {'key': 'integration',
  'title': ['身体と環境につなぎ、動かす', 'Run models with a body and environment'],
  'question': ['回路の予測を、環境の中で働くモデルへ。', 'Make circuit predictions work in an environment.'],
  'short': [['回路シミュレーターと、神経・身体・環境を結ぶ限定モデルが利用できます。',
             'Circuit simulators and limited models linking neurons, bodies and environments are available.'],
            ['感覚フィードバックのある条件で動かし、遅延・状態・学習の違いが行動をどう変えるか測ります。',
             'Run with sensory feedback and measure how delay, state and learning affect behaviour.'],
            ['長く安定して働く条件を揃え、個体の応答と記憶を統合して検証する足場を作れます。',
             'Establish conditions for stable operation and integrated tests of individual responses and '
             'memory.']],
  'steps': (('NEURONとBMTKは，神経回路を計算する基盤です。BAAIWormは限定した神経系・行動で，神経，身体，環境を結びます。局所的な神経補綴では，記録と介入を用いて特定の機能を評価できます。',
             'NEURON and BMTK provide neural-circuit simulation infrastructure. BAAIWorm links neurons, body and '
             'environment for a limited neural and behavioural scope. Local neural prostheses support evaluation '
             'of specific functions through recordings and interventions.'),
            ('まず同じ感覚入力を再生し、回路モデルを比較します。次に身体モデル、制御器、初期条件、環境、課題をそろえ、行動で感覚が変わる閉ループへ進みます。感覚フィードバックの遅延、モデル状態、学習条件を一つずつ変えます。回路以外を固定した比較と、制御器も再調整する比較を分け、許可した学習情報・予算を記録します。状態の保存・再開後も確かめます。 '
             '学習を加える段階では、先に評価用データで確かめたGの候補を比較します。G自体は再調整せず、その規則による重みの変化を許し、同じ個体の保持・忘却・新たな学習へ対応するかを調べます。失敗した条件から、学習則と身体側の原因を分けて再検査します。',
             'First replay identical sensory inputs to compare circuit models. Then match body model, controller, '
             'initial conditions, environment and task in a closed loop where behaviour changes sensory feedback. '
             'Vary feedback delay, model state and learning one at a time. Separate comparisons holding '
             'non-circuit components fixed from comparisons that retune the controller; record permitted training '
             'information and budgets. Test after saving and resuming state. When adding learning, compare G '
             'candidates already tested on held-out data. Keep G fixed while allowing its weight updates; test '
             'correspondence to retention, forgetting and new learning in the same individual. Use failures to '
             'separate learning-rule errors from body-side causes.'),
            ['回路由来の改善が身体との循環でも維持されれば、測定・同定で得たモデルを統合する判断材料になります。保持・忘却・新たな学習を同じ個体のデータと比較し、別チームが追試できる全工程へ広げます。',
             'If circuit-derived improvements persist in the body–environment loop, they support integrating '
             'models obtained through measurement and identification. Compare retention, forgetting and new '
             'learning with data from the same individual, then extend the workflow to independent replication.']),
  'evidence_refs': ['Q8SGY2SV', '9DXWPDVH', 'ADD203'],
  'extra_refs': ['JHS9IFXX', 'ADD195', 'XKB4CG64'],
  'limit': ['身体の制御器や追加学習だけで得た性能を、脳回路の再現として数えません。神経補綴による限定機能の補助は、脳の段階的置換の成立や、個体の記憶を別媒体へ移した実証を意味しません。',
            'Performance supplied by a body controller or additional training must not be credited to circuit '
            'reproduction. Assisting a limited function with a neuroprosthesis does not establish gradual brain '
            'replacement or transfer of individual memories to another medium.'],
  'branch': ['動作が崩れたら、回路の予測誤差、身体側の制御、感覚フィードバック、計算の遅延を分けて調べます。必要な状態が足りなければ測定へ、接続に原因があれば再構成と取得・校正へ戻り、同じ課題で改善を確かめます。',
             'If behaviour breaks down, separate circuit prediction error, body control, sensory feedback and '
             'computational delay. Return to state measurements, or to reconstruction and '
             'acquisition/proofreading, as indicated; verify improvement on the same task.'],
  'link': ['validation.html#individual', '同じ個体との比較設計へ', 'Design the individual comparison']})

ACQUISITION = {'key': 'acquisition',
 'role': 'shared_foundation_not_fourth_independent_route',
 'title': ['必要な情報を、測れる形で残す', 'Preserve and acquire the information models need'],
 'question': ['三つのルートを支える、取得の共通基盤です。', 'A shared acquisition foundation for all three routes.'],
 'short': [['EMのコネクトーム、保存組織の微細構造、LICONNの光学的な局所再構成が出発点です。',
            'EM connectomes, preserved ultrastructure and LICONN’s local optical reconstruction provide '
            'starting points.'],
           ['小体積で、保存から撮像・再構成・校正までの誤り、時間、データ量を測ります。',
            'Measure errors, time and data volume from preservation through imaging, reconstruction and '
            'proofreading on small volumes.'],
           ['合格する精度と費用が分かれば、必要な情報を残す取得方式と、自動化する工程を選べます。',
            'Accepted accuracy and cost can guide which information to preserve, which modality to use and '
            'which stages to automate.']],
 'steps': [['FlyWireやMICrONSはEM画像をコネクトームへつなぐ工程の足場です。ASCは固定組織の微細構造の保存、LICONNは哺乳類の局所組織の光学的再構成を示しました。これらを一つの方法として組み合わせた実証ではなく、取得工程を作るための別々の足場です。',
            'FlyWire and MICrONS provide foundations for turning EM images into connectomes. ASC '
            'demonstrated preservation of fixed-tissue ultrastructure, and LICONN demonstrated optical '
            'reconstruction of local mammalian tissue. These are separate foundations for developing '
            'acquisition, not a demonstrated combined method.'],
           ['まず公開画像の固定した小体積で、位置合わせ、セグメンテーション、シナプス検出、校正の結果を独立した参照と比べます。過分割・誤併合、見逃し、校正の人時、計算・通信・保存量を記録します。試料を使う比較では、保存・拡大・分子標識の両立も確かめます。三つのルートが求める精度を使い、合格した元の組織体積当たりの速度と費用で方式を比べます。',
            'Begin with a fixed small public image volume. Compare alignment, segmentation, synapse '
            'detection and proofreading with independent references. Record splits, false merges, misses, '
            'proofreading person-hours, compute, transfer and storage. In specimen experiments, also test '
            'compatibility of preservation, expansion and molecular labels. Use accuracy requirements from '
            'the three routes to compare speed and cost per accepted original tissue volume.'],
           ['必要な構造と分子情報を、再現可能な精度と費用で取得できれば、方式の選択と自動化の優先順位を具体化できます。次は対象体積を広げ、切片間の対応と長期稼働を確かめ、同じ個体のモデルへ渡す工程を試します。',
            'Acquiring required structural and molecular information at reproducible accuracy and cost '
            'supports modality selection and automation priorities. Next, expand the volume, verify '
            'correspondence across sections and sustained operation, and test delivery into a model of the '
            'same individual.']],
 'evidence_refs': ['ADD196', '6TNZ57MZ', 'SDSWEA5J', 'ADD198'],
 'extra_refs': ['EVWH7H32'],
 'limit': ['超微細構造の保存は、生理機能や記憶を取り戻した実証ではありません。LICONNの局所的な成果も人の全脳取得を意味しません。高速な撮像だけでは、切片の欠損、再構成の誤り、校正の負担を解消できません。必要な精度がまだ定まらない場合は、構造の評価とモデル機能の評価を分けて報告します。',
           'Ultrastructure preservation does not demonstrate restored physiology or memory. Local LICONN '
           'results do not establish whole-human-brain acquisition. Fast imaging alone does not remove '
           'section loss, reconstruction errors or proofreading work. When required accuracy is unknown, '
           'report structural and model-functional evaluation separately.'],
 'branch': ['必要な精度に届かなければ、解像度・標識・保存条件や校正法を変えます。誤りが局所に偏るなら、その範囲を先に改善します。人手が増え続ける場合は、体積を広げる前に自動化を評価します。追加情報の価値が不明なら、活動とモデル比較のルートへ戻って測定の優先順位を決めます。',
            'If accuracy is insufficient, change resolution, labels, preservation conditions or '
            'proofreading. Address local error concentrations first. If human effort keeps growing, evaluate '
            'automation before scaling volume. If added information has unclear value, return to activity '
            'and model comparisons to set measurement priorities.'],
 'link': ['future.html#scaling', '撮像量と工程の試算へ', 'Estimate imaging volume and workflow requirements']}


def _language(lang):
    if lang not in ('ja', 'en'):
        raise ValueError('lang must be ja or en')
    return 0 if lang == 'ja' else 1


def _refs(ids):
    return ''.join(f'[[{ref}]]' for ref in ids)


def _url(lang, path):
    return ('/ja/' if lang == 'ja' else '/') + path


def _convergence(lang, overview):
    n = _language(lang)
    title = ('合流先：同じ個体の情報をつなぎ、確かめます', 'Converge on the same individual: connect information and test')[n]
    text = (
        '三つは、合流を目指して本サイトが提案する相補的な研究ルートです。それぞれで得た構造・状態・実行の条件を合わせ、元の個体の応答、記憶、学習を未使用のデータで確かめる全工程へつなげます。',
        'These are this site’s proposed complementary research routes. Combine their requirements for structure, state and execution into a workflow that tests the original individual’s responses, memory and learning on held-out data.',
    )[n]
    goal = (
        '一つの実験で分かったことを次の測定へ返せます。まずは公開モデルを一つ動かし、条件を一つ変える比較から始められます。',
        'Each experiment can inform the next measurement. A practical first step is to run one public model and compare one changed condition.',
    )[n]
    links = [('action.html#projects', '最初の実験を選ぶ', 'Choose a first experiment'),
             ('validation.html#individual', '個体との対応を確かめる', 'Test individual correspondence')]
    if overview:
        links.insert(0, ('future.html#routes', '三つのルートを詳しく見る', 'Explore the three routes'))
    anchors = ''.join(f'<a href="{escape(_url(lang, path), quote=True)}">{escape(jp if n == 0 else en)}</a>' for path, jp, en in links)
    return '<div class="route-convergence"><h3>'+escape(title)+'</h3><p>'+escape(text)+'</p><p>'+escape(goal)+'</p><div class="route-actions">'+anchors+'</div></div>'


def route_overview(lang):
    """Return compact home-page cards; details live at /future.html#routes."""
    n = _language(lang)
    labels = ('既存の成果と研究基盤', '次に行う実験', '成功後に検証する課題') if n == 0 else ('Evidence and research foundations', 'Next experiment', 'Tests enabled by success')
    parts = ['<div class="research-routes route-overview"><div class="route-grid">']
    for number, route in enumerate(ROUTES, 1):
        parts.append('<article class="route-card"><p class="route-number">'+('ルート ' if n == 0 else 'Route ')+str(number)+'</p><h3>'+escape(route['title'][n])+'</h3>')
        parts.append('<ol class="route-steps">')
        for i, (label, copy) in enumerate(zip(labels, route['short'])):
            citations = _refs(route['evidence_refs']) if i == 0 else ''
            parts.append('<li><h4>'+escape(label)+'</h4><p>'+escape(copy[n])+citations+'</p></li>')
        parts.append('</ol><p class="route-card-link"><a href="'+escape(_url(lang, 'future.html#route-'+route['key']), quote=True)+'">'+('実験と分岐を見る' if n == 0 else 'See the experiment and branches')+'</a></p></article>')
    parts.append('</div>'+_acquisition(lang, overview=True)+_convergence(lang, overview=True)+'</div>')
    return ''.join(parts)


def route_details(lang):
    """Return the detailed future-page route section, without a surrounding section."""
    n = _language(lang)
    labels = ('既存の成果と研究基盤', '次に行う実験', '成功後に検証する課題') if n == 0 else ('Evidence and research foundations', 'Next experiment', 'Tests enabled by success')
    intro = (
        '構造・活動・実行のどこから着手しても、次の比較実験を設計できます。以下では、論文で示された足場から、本サイトが提案する実験と、その成功が可能にする次の検証へ進みます。',
        'Work can begin with structure, activity or execution. Each route below moves from a published foundation to this site’s proposed experiment and the next test that success would make possible.',
    )[n]
    parts = ['<div class="research-routes route-details"><p class="route-intro">'+escape(intro)+'</p>']
    for number, route in enumerate(ROUTES, 1):
        parts.append('<article class="route-card" id="route-'+route['key']+'"><header class="route-heading"><p class="route-number">'+('ルート ' if n == 0 else 'Route ')+str(number)+'</p><h3>'+escape(route['title'][n])+'</h3><p>'+escape(route['question'][n])+'</p></header><ol class="route-steps">')
        for i, (label, copy) in enumerate(zip(labels, route['steps'])):
            citations = _refs(route['evidence_refs']) if i == 0 else ''
            if i == 0 and route['key'] == 'integration':
                citations += _refs(('JHS9IFXX', 'ADD195'))
            parts.append('<li><h4>'+escape(label)+'</h4><p>'+escape(copy[n])+citations+'</p></li>')
        summary = ('根拠の範囲と、うまくいかなかった時の分岐', 'Evidence boundaries and branches if the test fails')[n]
        limits_title = ('成果の適用範囲と制約', 'Scope and constraints of the evidence')[n]
        branch_title = ('結果に応じて進路を変えます', 'Choose the next branch from the result')[n]
        parts.append('</ol><details class="route-support"><summary>'+escape(summary)+'</summary><div class="route-support-content"><h4>'+escape(limits_title)+'</h4><p>'+escape(route['limit'][n])+_refs(route['extra_refs'])+'</p><h4>'+escape(branch_title)+'</h4><p>'+escape(route['branch'][n])+'</p></div></details>')
        path, jp, en = route['link']
        parts.append('<p class="route-card-link"><a href="'+escape(_url(lang, path), quote=True)+'">'+escape(jp if n == 0 else en)+'</a></p></article>')
    parts.append(_acquisition(lang, overview=False)+_convergence(lang, overview=False)+'</div>')
    return ''.join(parts)


def _acquisition(lang, overview):
    n = _language(lang)
    a = ACQUISITION
    labels = ('既存の成果と研究基盤', '次に行う実験', '成功後に検証する課題') if n == 0 else ('Evidence and research foundations', 'Next experiment', 'Tests enabled by success')
    parts = ['<article class="route-card acquisition-foundation"'+('' if overview else ' id="route-acquisition"')+'><p class="route-number">'+('三つのルートを支える共通基盤' if n==0 else 'Shared foundation for all three routes')+'</p><h3>'+escape(a['title'][n])+'</h3><p>'+escape(a['question'][n])+'</p><ol class="route-steps">']
    for i, text in enumerate(a['short'] if overview else a['steps']):
        parts.append('<li><h4>'+labels[i]+'</h4><p>'+escape(text[n])+(_refs(a['evidence_refs']) if i==0 else '')+'</p></li>')
    parts.append('</ol>')
    if not overview:
        parts.append('<details class="route-support"><summary>'+('成果の適用範囲と制約・結果に応じた見直し' if n==0 else 'Scope, constraints and revisions after the experiment')+'</summary><p>'+escape(a['limit'][n])+_refs(a['extra_refs'])+'</p><p>'+escape(a['branch'][n])+'</p></details>')
    path = 'future.html#route-acquisition' if overview else a['link'][0]
    parts.append('<p><a href="'+_url(lang,path)+'">'+('取得工程の実験と条件へ' if n==0 else 'Acquisition experiments and conditions')+'</a></p></article>')
    return ''.join(parts)
