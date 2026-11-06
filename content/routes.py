"""Complementary, evidence-grounded research routes toward whole-brain emulation.

These are editorial research proposals. Shared reference IDs keep the Japanese
and English renderings aligned; the site generator resolves [[ID]] citations.
"""

from html import escape


ROUTES = (
    {
        'key': 'structure',
        'title': ('接続図から再構成する', 'Reconstruct from wiring'),
        'question': ('脳の地図を、予測できるモデルへ。', 'Turn a brain map into a model that predicts.'),
        'short': (
            ('ハエ脳の接続図と、感覚運動・視覚を予測するモデルがあります。',
             'Fly connectomes and models predicting sensorimotor and visual responses are available.'),
            ('既存モデルを再現し、接続の誤りや個体の違いで予測がどれだけ変わるか測ります。',
             'Reproduce a model, then measure how wiring errors and individual differences change its predictions.'),
            ('試したモデル・課題で取得精度の候補を絞り、個体固有の応答を確かめる実験へ進めます。',
             'Narrow candidate acquisition tolerances for the tested models and tasks, then test individual responses.'),
        ),
        'steps': (
            ('ハエの接続図を出発点に、Shiuらは感覚運動機能、Lappalainenらは視覚応答の予測を実験と照合しています。公開データとモデルが、次の実験の土台になります。',
             'Starting from fly connectomes, Shiu et al. tested sensorimotor predictions and Lappalainen et al. tested visual responses. Public data and models provide a foundation for the next experiment.'),
            ('まず同じデータ版と評価条件で既存結果を再現します。その後、欠損・誤結合・重みの変化を一つずつ加え、細胞型平均やシャッフル対照と比較します。複数個体を比べる場合は、性・領域・細胞対応をそろえ、まだ使っていない刺激や介入を評価に残します。',
             'First reproduce a result with the same data version and evaluation conditions. Then vary missing edges, false connections and weights, comparing cell-type averages and shuffled controls. For comparisons across individuals, match sex, coverage and cell correspondence, reserving unseen stimuli or interventions for evaluation.'),
            ('予測を保てる誤差の範囲が別モデルでも再現すれば、「どの情報をどの精度で取得するか」を具体化できます。同じ個体の活動記録を加え、平均モデルより元の個体をよく説明できるかを調べる段階へ進めます。',
             'If an error tolerance reproduces in another model, it can guide what to acquire and at what precision. Adding activity from the same individual then enables tests of whether individual measurements outperform an average model.'),
        ),
        'evidence_refs': ('ADD196', 'V4GV7JAJ', 'XMYSQXY8'),
        'extra_refs': ('ISSUE284_SCHLEGEL2024', 'ADD190'),
        'limit': ('接続図の形だけでは、伝達の強さやその時の状態は一意に決まりません。別個体の構造による予測差だけを、個体の記憶を再現した証拠にはしません。',
                  'Wiring alone does not uniquely determine transmission strength or current state. Prediction differences between connectomes alone do not establish reproduction of individual memories.'),
        'branch': ('予測が崩れた場所から、接続の校正、細胞対応、重みの推定のどこを直すかを選びます。構造だけで差を説明できなければ、次のルートで活動・分子・状態情報の追加を試します。',
                   'Use the failure pattern to choose between correcting wiring, cell correspondence or weight estimates. If structure does not explain the differences, use the activity route to test added functional, molecular or state measurements.'),
        'link': ('action.html#projects', '最初の比較実験へ', 'Start the comparison experiment'),
    },
    {
        'key': 'state',
        'title': ('活動から、必要な情報を絞る', 'Identify necessary information from activity'),
        'question': ('測る情報を増やす前に、何が効くかを確かめます。', 'Test which measurements make a difference.'),
        'short': (
            ('構造と活動を対応付けたMICrONS、活動予測のZAPBench、推定の不確実性を扱う手法があります。',
             'MICrONS pairs structure and activity; ZAPBench benchmarks activity prediction; inference methods represent parameter uncertainty.'),
            ('同じ観測に合うモデルを比較し、未知の応答を見分けるために必要な追加測定を選びます。',
             'Compare models that fit the same observations and select measurements that distinguish their unseen responses.'),
            ('機能に必要な状態の候補を絞り、構造からの復元とつなげられます。',
             'Narrow candidate states needed for function and connect them to structural reconstruction.'),
        ),
        'steps': (
            ('MICrONSはマウス視覚野の一部で構造と活動を対応付け、ZAPBenchは幼生ゼブラフィッシュの活動予測を比較します。Gonçalvesらの手法は、神経回路モデルのパラメーターを一つに決めず、観測に適合する事後分布として推定する例を示しています。',
             'MICrONS pairs structure and activity in part of mouse visual cortex; ZAPBench compares activity prediction in larval zebrafish. Gonçalves et al. demonstrate inference of posterior distributions over neural-model parameters, rather than forcing a single parameter solution.'),
            ('正解の分かる人工回路で、観測ノイズと測定項目を変え、推定範囲が正解を含むかを検査します。次に生物のデータで、同じ記録に合うモデルが未知の刺激・介入をどう予測するか比較します。予測が分かれる測定を候補にし、追加データで実際に区別できるかを確かめます。',
             'In synthetic circuits with known truth, vary noise and recorded variables and check whether inferred ranges cover the truth. In biological data, compare predictions for unseen stimuli and interventions across models that fit the same recordings. Select measurements where predictions diverge, then test whether added data distinguish them.'),
            ('追加測定による改善が留保データでも続けば、その測定を取得工程へ組み込む根拠になります。構造の精度だけを上げるのか、分子・活動・可塑性の情報も残すのかを選び、個体の記憶を検証する計画へつなげます。',
             'If improvement persists on held-out data, it supports adding that measurement to acquisition. This helps choose between finer structure and additional molecular, activity or plasticity information, informing a plan to test individual memory.'),
        ),
        'evidence_refs': ('6TNZ57MZ', 'FHPYMIG8', 'ISSUE285_GONCALVES2020'),
        'extra_refs': ('274IXB72', 'ADD190'),
        'limit': ('MICrONSの対象は局所体積で、ZAPBenchの評価入力に接続図は含まれません。事後分布はモデルと事前分布の仮定に依存します。活動予測の一致と、生物の機構を同定したことは分けて判定します。',
                  'MICrONS covers a local volume, and connectomes are not inputs to the ZAPBench evaluation. Posteriors depend on model and prior assumptions. Predictive agreement and identification of biological mechanisms require separate judgments.'),
        'branch': ('候補が絞れない場合は、測定時間や入力条件を変え、予測が分かれる観測を探します。追加測定でも改善しなければ、モデルの形や評価課題を見直します。この結果も、測定の優先順位と残る不確実性を見直す材料になります。',
                   'If candidates remain indistinguishable, vary recording times or inputs to seek discriminating observations. If added measurements do not improve prediction, revisit the model class or evaluation task. The result still helps reassess measurement priorities and remaining uncertainty.'),
        'link': ('future.html#gates', '復元手法を検査する里程標へ', 'Explore the reconstruction milestones'),
    },
    {
        'key': 'integration',
        'title': ('身体と環境につなぎ、動かす', 'Run models with a body and environment'),
        'question': ('回路の予測を、環境の中で働くモデルへ。', 'Make circuit predictions work in an environment.'),
        'short': (
            ('回路シミュレーターと、神経・身体・環境を結ぶ限定モデルが利用できます。',
             'Circuit simulators and limited models linking neurons, bodies and environments are available.'),
            ('身体から感覚が戻る条件で動かし、遅延・状態・学習の違いが行動をどう変えるか測ります。',
             'Run a sensory-feedback loop and measure how delay, state and learning affect behaviour.'),
            ('長く安定して働く条件を揃え、個体の応答と記憶を統合して検証する足場を作れます。',
             'Establish conditions for stable operation and integrated tests of individual responses and memory.'),
        ),
        'steps': (
            ('NEURONとBMTKは回路を計算する基盤を提供し、BAAIWormは限定した神経系・行動で神経、身体、環境を結びます。局所的な神経補綴の研究は、記録と介入を用いて特定機能を評価する別の足場になります。',
             'NEURON and BMTK provide circuit-simulation infrastructure; BAAIWorm links neurons, body and environment for a limited neural and behavioural scope. Local neural-prosthesis studies offer a separate foothold for testing specific functions through recordings and interventions.'),
            ('まず同じ感覚入力を再生し、回路モデルを比較します。次に身体モデルと制御器、初期条件・環境・課題をそろえて回路モデルを入れ替え、行動によって感覚が変わる閉ループで比較します。帰還の遅延、環境、モデル状態、学習条件を一つずつ変え、予測精度と実行費用、長期の安定性を記録します。状態の保存・再開後にも確かめます。',
             'First replay identical sensory inputs to compare circuit models. Then swap circuit models in a closed loop, matching the body model, controller, initial conditions, environment and task while allowing behaviour to change sensory feedback. Vary feedback delay, environment, model state and learning conditions one at a time; record predictive accuracy, execution cost and long-run stability, including after saving and resuming state.'),
            ('回路由来の改善が身体との循環でも維持されれば、測定・同定で得たモデルを統合する判断材料になります。保持・忘却・新たな学習を同じ個体のデータと比較し、別チームが追試できる全工程へ広げます。',
             'If circuit-derived improvements persist in the body–environment loop, they support integrating models obtained through measurement and identification. Compare retention, forgetting and new learning with data from the same individual, then extend the workflow to independent replication.'),
        ),
        'evidence_refs': ('Q8SGY2SV', '9DXWPDVH', 'ADD203'),
        'extra_refs': ('JHS9IFXX', 'ADD195', 'XKB4CG64'),
        'limit': ('身体の制御器や追加学習だけで得た性能を、脳回路の再現として数えません。神経補綴による限定機能の補助は、脳の段階的置換の成立や、個体の記憶を別媒体へ移した実証を意味しません。',
                  'Performance supplied by a body controller or additional training must not be credited to circuit reproduction. Assisting a limited function with a neuroprosthesis does not establish gradual brain replacement or transfer of individual memories to another medium.'),
        'branch': ('動作が崩れたら、回路の予測誤差、身体側の制御、感覚帰還、計算の遅延を分けて調べます。必要な状態が足りなければ測定のルートへ、接続に原因があれば再構成のルートへ戻り、同じ課題で改善を確かめます。',
                   'When behaviour breaks down, separate circuit prediction errors, body control, sensory feedback and computational delay. Return to state measurements or wiring reconstruction as indicated, then verify improvement on the same task.'),
        'link': ('validation.html#individual', '同じ個体との比較設計へ', 'Design the individual comparison'),
    },
)


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
    labels = ('今ある足場', '次の一歩', 'その先へ') if n == 0 else ('Available now', 'Next experiment', 'What it opens')
    parts = ['<div class="research-routes route-overview"><div class="route-grid">']
    for number, route in enumerate(ROUTES, 1):
        parts.append('<article class="route-card"><p class="route-number">'+('ルート ' if n == 0 else 'Route ')+str(number)+'</p><h3>'+escape(route['title'][n])+'</h3>')
        parts.append('<ol class="route-steps">')
        for i, (label, copy) in enumerate(zip(labels, route['short'])):
            citations = _refs(route['evidence_refs']) if i == 0 else ''
            parts.append('<li><h4>'+escape(label)+'</h4><p>'+escape(copy[n])+citations+'</p></li>')
        parts.append('</ol><p class="route-card-link"><a href="'+escape(_url(lang, 'future.html#route-'+route['key']), quote=True)+'">'+('実験と分岐を見る' if n == 0 else 'See the experiment and branches')+'</a></p></article>')
    parts.append('</div>'+_convergence(lang, overview=True)+'</div>')
    return ''.join(parts)


def route_details(lang):
    """Return the detailed future-page route section, without a surrounding section."""
    n = _language(lang)
    labels = ('今ある足場', '次に行う実験', '成功すると開く次の段階') if n == 0 else ('Available now', 'The next experiment', 'What success would open')
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
        limits_title = ('この足場を使う条件', 'Conditions for using this foundation')[n]
        branch_title = ('結果に応じて進路を変えます', 'Choose the next branch from the result')[n]
        parts.append('</ol><details class="route-support"><summary>'+escape(summary)+'</summary><div class="route-support-content"><h4>'+escape(limits_title)+'</h4><p>'+escape(route['limit'][n])+_refs(route['extra_refs'])+'</p><h4>'+escape(branch_title)+'</h4><p>'+escape(route['branch'][n])+'</p></div></details>')
        path, jp, en = route['link']
        parts.append('<p class="route-card-link"><a href="'+escape(_url(lang, path), quote=True)+'">'+escape(jp if n == 0 else en)+'</a></p></article>')
    parts.append(_convergence(lang, overview=False)+'</div>')
    return ''.join(parts)
