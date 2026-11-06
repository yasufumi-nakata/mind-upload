"""Versioned editorial rubric, stable task IDs and shared research stages.

Points measure published conditions met in this guide's evidence review, not
scientific success probability, remaining effort, or a forecast of completion.
"""
from html import escape

RUBRIC_VERSION = '1.0'
REVIEW_DATE = '2026-11-07'
TASK_IDS = {
    'structure': ('R01', 'R02'), 'recording': ('R03', 'R04'),
    'dynamics': ('R05', 'R06'), 'preservation': ('R07', 'R08'),
    'compute': ('R09', 'R10'), 'validation': ('R11', 'R12'),
}
DOMAIN_NAMES = {
    'structure': ('構造', 'Structure'), 'recording': ('活動・状態', 'Activity/state'),
    'dynamics': ('機能・学習則', 'Function/learning rules'), 'preservation': ('情報保存', 'Preservation'),
    'compute': ('計算・身体', 'Computation/body'), 'validation': ('個体の検証', 'Individual validation'),
}
ROUTE_NAMES = {
    'structure': ('構造からの復元', 'Structural reconstruction'),
    'state': ('活動からの同定', 'Activity-based identification'),
    'integration': ('身体との統合', 'Embodied integration'),
    'acquisition': ('並行する取得基盤', 'Parallel acquisition foundation'),
}
STAGES = (
    dict(id='S1', title=('要素技術と復元手法', 'Components and reconstruction methods'), year='2030',
         milestones=('M1', 'M2'), tasks=('R01', 'R02', 'R03', 'R04', 'R05', 'R07', 'R09', 'R11', 'R12'),
         routes=('structure', 'state', 'acquisition'),
         description=('測定と予測の成果をつなぎ，復元手法と誤差の範囲を確かめます。', 'Connect measurement and prediction; test reconstruction methods and error tolerances.')),
    dict(id='S2', title=('個体の情報と記憶', 'Individual information and memory'), year='2035',
         milestones=('M3', 'M4'), tasks=('R04', 'R06', 'R08', 'R11', 'R12'),
         routes=('structure', 'state', 'integration', 'acquisition'),
         description=('元の個体の応答と，学習済みの記憶を評価用データで確かめます。', 'Test original-individual responses and previously acquired memories on held-out data.')),
    dict(id='S3', title=('哺乳類の全脳での継続動作', 'Sustained mammalian whole-brain function'), year='2040',
         milestones=('M3', 'M4'), tasks=('R01', 'R02', 'R04', 'R05', 'R06', 'R07', 'R08', 'R09', 'R10', 'R11', 'R12'),
         routes=('structure', 'state', 'integration', 'acquisition'),
         description=('未知条件で確かめた学習則Gを組み込み，全脳での身体相互作用と長期学習を検証します。', 'Integrate learning rules G tested on unseen conditions; test whole-brain body interaction and long-term learning.')),
    dict(id='S4', title=('人の全工程と独立検証', 'Human workflow and independent validation'), year='2045 / 2050',
         milestones=('M3', 'M4'), tasks=tuple(f'R{i:02}' for i in range(1, 13)),
         routes=('structure', 'state', 'integration', 'acquisition'),
         description=('同一人物の取得から実行までをつなぎ，別チームが検証します。', 'Connect acquisition to execution for one person, with independent-team validation.')),
)


def item(key, stage, points, title, scope, criterion, status, evidence, refs, tasks, routes, milestone=None):
    return dict(id=key, stage=stage, points=points, title=title, scope=scope,
                criterion=criterion, status=status, evidence=evidence, refs=refs,
                tasks=tasks, routes=routes, milestone=milestone,
                domains=tuple(d for d, ids in TASK_IDS.items() if set(ids) & set(tasks)), reviewed=REVIEW_DATE)

ITEMS = (
    item('F-STRUCTURE', 'S1', 2.5, ('小動物の全脳コネクトーム', 'Small-animal whole-brain connectome'),
         ('成体ハエ脳・化学シナプスの再構成', 'Adult fly brain; reconstructed chemical synapses'),
         ('全脳を対象とする再構成データと手法が公開され，校正方法・対象範囲・誤りの評価が報告されていること。全シナプス無欠損は条件に含めません。', 'Public whole-brain reconstruction data and methods, with reported proofreading, scope and error assessment. Zero missing synapses is not required.'),
         'met', ('FlyWireは139,255ニューロンを再構成し，公開データと品質評価を提供しています。電気シナプスや全状態の取得を加点したものではありません。', 'FlyWire reports 139,255 reconstructed neurons, public data and quality assessment. This does not award credit for electrical synapses or all state variables.'), ('ADD196',), ('R01', 'R02'), ('structure', 'acquisition')),
    item('F-PAIRED', 'S1', 2.5, ('同じ標本の構造・活動対応', 'Paired structure and activity'),
         ('マウス視覚野の局所体積', 'Local mouse visual cortex'),
         ('同一個体で生体活動と取得後の構造を細胞対応付きで公開し，対応数と空間・時間範囲を報告すること。', 'Public same-individual activity and subsequent structure, with cell correspondences, matched counts and spatial/temporal scope.'),
         'met', ('MICrONSは機能記録とEMで15,439細胞を手作業対応付けしています。局所体積での達成です。', 'MICrONS manually matched 15,439 cells between functional recordings and EM. The result is local, not whole-brain.'), ('6TNZ57MZ',), ('R03', 'R04'), ('state', 'acquisition')),
    item('F-PREDICTION', 'S1', 2.5, ('接続を用いた限定機能の予測', 'Connectome-based prediction of limited function'),
         ('ハエの感覚運動・視覚課題', 'Fly sensorimotor and visual tasks'),
         ('公開モデルが接続情報を用い，モデル調整に使わない実験条件との比較を報告すること。対象機能と対照条件を明示すること。', 'A public connectome-based model reports comparison with experimental conditions not used for model fitting, with explicit functions and controls.'),
         'met', ('Shiuらの感覚運動予測とLappalainenらの視覚応答検証が根拠です。異なる表現・課題のモデルです。元の個体の記憶には加点しません。', 'Supported by Shiu et al. sensorimotor predictions and Lappalainen et al. visual-response tests. The models use different representations and tasks; no individual-memory credit is awarded.'), ('V4GV7JAJ', 'XMYSQXY8'), ('R05',), ('structure',)),
    item('F-PRESERVATION', 'S1', 2.5, ('保存後の微細構造の検証', 'Ultrastructure after preservation'),
         ('ウサギ・ブタ脳の検査部位', 'Examined regions of rabbit and pig brains'),
         ('保存・復温後の神経組織を電子顕微鏡で評価し，手法と検査範囲を公開すること。記憶や機能の保存は別条件です。', 'Electron-microscopic assessment after preservation and rewarming, with public methods and sampled scope. Memory and function are separate criteria.'),
         'met', ('ASCの報告で微細構造の保存が確認されています。全分子状態の保存や記憶の復元を実証したものではありません。', 'ASC reports preserved ultrastructure. It does not establish preservation of all molecular states or recovery of memory.'), ('SDSWEA5J',), ('R07',), ('acquisition',)),
    item('M1', 'S1', 5, ('復元手法の検証', 'Validate reconstruction methods'),
         ('正解既知の人工回路', 'Synthetic circuits with known truth'),
         ('観測過程・ノイズ・欠損・測定項目を変え，推定の被覆確率と未使用介入の予測を評価します。観測信号と潜在状態を分け，独立実装で追試します。', 'Vary observation processes, noise, missingness and modalities; test interval coverage and held-out interventions. Evaluate observed signals and latent states separately and replicate independently.'),
         'not_met', ('Challengeと推定研究は足場になりますが，この全条件を一つの検証工程で満たした報告は今回確認した資料にありません。', 'The Challenge and inference research provide foundations, but the reviewed sources do not demonstrate this complete validation workflow.'), ('CCCHALLENGE', 'ISSUE285_GONCALVES2020', 'NEW_CONFAVREUX2023', 'NEW_MEHTA2024'), ('R03', 'R05', 'R11', 'R12'), ('state',), 'M1'),
    item('M2', 'S1', 5, ('構造誤差と機能の関係', 'Relate structural error to function'),
         ('表現の異なる二つの回路モデル', 'Two circuit models with different representations'),
         ('固定条件で構造を乱す感度と，再同定できる範囲を分けます。C0–C3をモデル別に定義し，未使用課題で評価します。共通の誤差尺度がなければ第二モデルでは傾向の一般性を検証します。', 'Separate fixed-model sensitivity from robustness after refitting. Define model-specific C0–C3 and evaluate held-out tasks. Without a common error scale, test generality of trends in the second model.'),
         'not_met', ('既存論文には構造や重みの対照がありますが，本サイトが提案する全比較工程の完了ではありません。', 'Published controls test structure or weights, but do not complete this guide’s full comparative protocol.'), ('V4GV7JAJ', 'XMYSQXY8'), ('R01', 'R02', 'R05', 'R12'), ('structure', 'acquisition'), 'M2'),
    item('M3', 'S2', 10, ('元の個体への対応', 'Original-individual correspondence'),
         ('同一個体の対データを持つ独立個体群', 'Independent individuals with paired data'),
         ('平均・他個体対照より元個体を良く予測し，事前の効果量・同等性基準を満たします。個体交換検定の分解能と検出力を計画し，別チームが追試します。', 'Outperform average/other-individual controls under prespecified effect and equivalence criteria. Plan individual-permutation resolution and power, and replicate with another team.'),
         'not_met', ('MICrONS等の対応データだけでは，この個体識別と追試の全条件は満たしません。', 'Paired resources such as MICrONS alone do not meet the complete identification and replication criteria.'), ('6TNZ57MZ', 'ISSUE284_SCHLEGEL2024'), ('R04', 'R11', 'R12'), ('structure', 'state'), 'M3'),
    item('M4', 'S2', 15, ('学習済み情報の復元', 'Recover previously learned information'),
         ('履歴の異なる学習済み個体', 'Trained individuals with different histories'),
         ('記憶課題の答えを学習・調整に使わず，取得情報から既得記憶を復元します。保持・忘却・再学習が事前の同等性マージン内で対応することを確かめます。情報損失と独立追試も報告します。', 'Recover prior memory from acquired information without training or tuning on the memory-test answers. Verify retention, forgetting and relearning within prespecified equivalence margins, with information-loss assessment and independent replication.'),
         'not_met', ('局所の可塑性，学習則推定，神経補綴の成果は，取得情報から元の記憶を復元する全条件とは異なります。', 'Local plasticity, learning-rule inference and neuroprostheses do not meet this complete memory-recovery criterion.'), ('NEW_HIGE2015', 'NEW_MEHTA2024', 'JHS9IFXX'), ('R06', 'R08', 'R11', 'R12'), ('state', 'integration', 'acquisition'), 'M4'),
)

# Later criteria remain explicitly unassessed in this initial, scoped scoring review.
_later = (
    ('MAM-FUNCTION', 'S3', 10, ('哺乳類全脳の機能対応', 'Mammalian whole-brain function'), ('同一哺乳類の全脳', 'Whole brain of one mammal'),
     ('必要な構造・状態情報を全脳で取得し，M3の比較を全脳の事前指定機能で満たします。欠落範囲と取得誤差を公開します。', 'Acquire necessary structure and state across a mammalian whole brain; meet M3 comparisons for prespecified whole-brain functions, disclosing missing coverage and errors.'), ('R01','R02','R04','R05','R07','R11')),
    ('MAM-LEARNING', 'S3', 10, ('長期の保持・忘却・学習', 'Long-term retention, forgetting and learning'), ('同じ哺乳類とモデルの長期比較', 'Long-term comparison of the same mammal and model'),
     ('事前登録した時間尺度でM4を拡張し，既得記憶の保持・忘却と新規学習が対応します。評価課題の追加学習で差を隠しません。', 'Extend M4 over preregistered timescales to retention, forgetting and new learning, without hiding discrepancies by training on evaluation tasks.'), ('R06','R08','R11')),
    ('MAM-BODY', 'S3', 5, ('身体相互作用と保存・再開', 'Body interaction and save/resume'), ('哺乳類全脳モデルの継続動作', 'Sustained mammalian whole-brain operation'),
     ('共通の身体・環境で感覚フィードバックを評価し，状態保存・再開後も事前基準を満たします。遅延・費用・制御器の寄与を分離します。', 'Evaluate sensory feedback in a matched body/environment and meet criteria after state save/resume; separate latency, costs and controller contributions.'), ('R09','R10','R12')),
    ('HUM-ACQUIRE', 'S4', 5, ('人の全脳の必要情報取得', 'Acquire necessary information across a human brain'), ('人の全脳・同一人物', 'Whole human brain; one individual'),
     ('機能検証で必要と判定した情報を全脳から取得します。生前記録との対応，保存損失，処理時間，校正と費用を公開します。', 'Acquire functionally necessary information across a human brain; disclose correspondence with prior recordings, preservation losses, time, proofreading and costs.'), ('R01','R02','R03','R04','R07','R08')),
    ('HUM-INTEGRATE', 'S4', 15, ('人の取得・復元・実行の統合', 'Integrate human acquisition, reconstruction and execution'), ('同一人物とその全脳モデル', 'One person and their whole-brain model'),
     ('同一人物の取得から実行を接続し，事前指定の活動・既得記憶・学習能力・身体相互作用が対応します。全脳範囲と継続動作を確認します。', 'Connect acquisition to execution for one person; meet prespecified activity, prior-memory, learning and body-interaction criteria with whole-brain coverage and sustained operation.'), ('R04','R05','R06','R08','R09','R10','R11')),
    ('HUM-INDEPENDENT', 'S4', 10, ('独立追試と運用条件の公開', 'Independent replication and operating conditions'), ('人の統合工程・別チーム', 'Integrated human workflow; independent team'),
     ('別チームが人の統合結果を追試します。許容誤差，未検証範囲，費用，遅延，再開条件を公開し，他の必須項目も満たします。', 'An independent team replicates the integrated human result; publish tolerances, untested scope, cost, latency and restart conditions, with every other required item met.'), ('R09','R10','R11','R12')),
)
ITEMS += tuple(item(k,s,p,t,scope,c,'not_assessed',
    ('初期採点では，この全条件を満たす証拠の項目別審査を行っていません。実証の不存在を断定する状態ではありません。', 'This initial review has not audited evidence against every condition of this item. This is not a claim that no demonstration exists.'), (), tasks, tuple(ROUTE_NAMES), 'M3 / M4' if s=='S3' else None)
    for k,s,p,t,scope,c,tasks in _later)

STATUS = {'met': ('達成済み', 'Met'), 'not_met': ('確認範囲で未達成', 'Not met in reviewed evidence'), 'not_assessed': ('未評価', 'Not assessed')}


def score(items=ITEMS, assume=()):
    """One ID, one award. Unknown items stay in the fixed denominator."""
    ids = [x['id'] for x in items]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate rubric ID')
    selected = set(assume)
    if not selected <= set(ids):
        raise ValueError('unknown assumed item')
    total = sum(x['points'] for x in items)
    if total != 100 or any(x['points'] <= 0 or x['status'] not in STATUS for x in items):
        raise ValueError('rubric must have 100 positive points and known statuses')
    earned = sum(x['points'] for x in items if x['status'] == 'met' or x['id'] in selected)
    unknown = sum(x['points'] for x in items if x['status'] == 'not_assessed' and x['id'] not in selected)
    baseline = sum(x['points'] for x in items if x['status'] == 'met')
    return dict(earned=earned, total=total, percent=earned / total * 100, unknown=unknown, added=earned-baseline)


def stage_complete(stage_id, items=ITEMS, assume=()):
    stage_index = next(i for i,s in enumerate(STAGES) if s['id'] == stage_id)
    required = {x['id'] for x in ITEMS if x['stage'] in {s['id'] for s in STAGES[:stage_index+1]}}
    met = {x['id'] for x in items if x['status'] == 'met'} | (set(assume) & {x['id'] for x in items})
    return required <= met


def _n(lang):
    if lang not in ('ja','en'): raise ValueError('unknown language')
    return 0 if lang=='ja' else 1


def progress_summary(lang):
    n=_n(lang); s=score(); base='/ja/' if n==0 else '/'
    heading=('達成率（本サイト基準）','Achievement rate (this site’s criteria)')[n]
    next_rows=[]
    for keys,label in [(('M1',),('M1：人工回路の復元手法を検証','M1: validate synthetic-circuit reconstruction')), (('M2',),('M2：構造誤差と機能の関係を検証','M2: test structural errors against function')), (('M1','M2'),('M1とM2の両方を達成','Meet both M1 and M2'))]:
        future=score(assume=keys)
        next_rows.append(f'<li>{label[n]} → <strong>{future["percent"]:g}%（+{future["added"]:g}'+('ポイント' if n==0 else ' points')+('）' if n==0 else ')')+'</strong></li>')
    target=('100%：特定の人の全脳について，取得から実行をつなぎ，活動・既得記憶・学習・身体相互作用が対応し，独立検証まで成立すること。', '100%: connect acquisition to execution for a specific human whole brain, validating activity, prior memory, learning and body interaction with independent replication.')[n]
    note=('公開した実証条件の充足を採点しています。成功確率・残り年数・作業量を示す値ではありません。', 'Scores fulfilment of published demonstration criteria, not success probability, remaining years or effort.')[n]
    result = f'<div class="progress-summary"><h3>{heading}</h3><p class="progress-number">{s["percent"]:g}%</p><progress value="{s["earned"]:g}" max="100" aria-label="{heading}">{s["percent"]:g}%</progress><p>'+('確認済み' if n==0 else 'Confirmed')+f' {s["earned"]:g}/100'+('点 ／ 未評価' if n==0 else ' points / unassessed')+f' {s["unknown"]:g}'+('点' if n==0 else ' points')+f' · v{RUBRIC_VERSION} · {REVIEW_DATE}</p><p>{note}</p><ul>'+''.join(next_rows)+f'</ul><p>{target}</p><p><a href="{base}history.html#score-ledger">'+('配点・達成条件・根拠と確認日' if n==0 else 'Weights, criteria, evidence and review dates')+'</a></p></div>'


    return result if n == 0 else result.replace('（+', ' (+')


def stage_path(lang):
    n=_n(lang); parts=['<ol class="distance-path">']
    for i,s in enumerate(STAGES,1):
        points=sum(x['points'] for x in ITEMS if x['stage']==s['id'])
        earned=sum(x['points'] for x in ITEMS if x['stage']==s['id'] and x['status']=='met')
        parts.append(f'<li><span>{earned:g}/{points:g}'+('点' if n==0 else ' points')+f'</span><h3>{s["title"][n]}</h3><p>{s["description"][n]}</p></li>')
    return ''.join(parts)+'</ol>'


def crosswalk(lang):
    n=_n(lang); base='/ja/' if n==0 else '/'; parts=['<div class="tbl"><table><caption>'+('4段階・評価時点・実験・12課題の対応' if n==0 else 'Four stages, review dates, experiments and 12 tasks')+'</caption><thead><tr>']
    for label in [('段階・配点','Stage / points'),('評価時点','Review dates'),('実験','Experiments'),('研究課題と領域','Tasks and domains'),('ルート','Routes')]: parts.append('<th>'+label[n]+'</th>')
    parts.append('</tr></thead><tbody>'); cumulative=0
    for st in STAGES:
        points=sum(x['points'] for x in ITEMS if x['stage']==st['id']); cumulative+=points
        domains=[d for d,ids in TASK_IDS.items() if set(ids)&set(st['tasks'])]
        tasks=', '.join(f'<a href="{base}history.html#{t}">{t}</a>' for t in st['tasks'])
        milestones=', '.join(f'<a href="{base}future.html#gates">{m}</a>' for m in st['milestones'])
        if st['id'] in ('S3','S4'): milestones+=('の基準を拡張' if n==0 else ' criteria extended')
        parts.append(f'<tr><th>{st["id"]} {st["title"][n]}<br>{points:g}'+('点' if n==0 else ' points')+f' / '+('前段まで全達成で' if n==0 else 'all prior criteria met: ')+f'{cumulative:g}%</th><td>{st["year"]}</td><td>{milestones}</td><td>{tasks}<br>'+ ' / '.join(DOMAIN_NAMES[d][n] for d in domains)+'</td><td>'+ ' / '.join(ROUTE_NAMES[r][n] for r in st['routes'])+'</td></tr>')
    parts.append('</tbody></table></div><p class="small">'+('Mは検証実験，Rは継続する研究課題，段階は統合範囲です。複数段階に同じ課題が関わります。2030–2050年は本サイトの評価時点で，完成予測ではありません。', 'M denotes validation experiments; R denotes continuing research tasks; stages denote integration scope. Tasks can span stages. The years 2030–2050 are this site’s review dates, not completion forecasts.')[n]+'</p>')
    return ''.join(parts)


def score_ledger(lang):
    n=_n(lang); parts=[progress_summary(lang)]
    intro=(
        '分母は100点で固定し，達成済みの項目だけを加点します。初期評価は基礎4項目の10点です。M1〜M4の35点は確認した文献では全条件未達成です。後半の55点は今回の項目別審査が未実施で，分母から除きません。',
        'The denominator is fixed at 100; only met items earn points. The initial score is 10 for four foundations. The reviewed evidence does not meet every M1–M4 condition (35 points). Later criteria (55 points) have not yet received an item-by-item evidence audit and remain in the denominator.')
    parts.append('<p>'+intro[n]+'</p><p>'+(
        '配点は編集上の判断です。要素技術20点，個体情報・記憶25点，全脳継続動作25点，人での統合と独立検証30点とし，個体の記憶と全工程の対応を重く扱いました。文献から測定された重要度ではありません。各項目は公開資料で条件を検証できることを最低条件とします。データ・コードの制約も明記します。',
        'Weights are editorial: 20 points for components, 25 for individual information and memory, 25 for sustained whole-brain function, and 30 for human integration and independent validation. They prioritize individual memory and end-to-end correspondence; they are not empirically measured importance weights. Every item requires public evidence adequate to assess its criteria, with any data/code restrictions stated.')[n]+'</p>')
    for st in STAGES:
        subset=[x for x in ITEMS if x['stage']==st['id']]; earned=sum(x['points'] for x in subset if x['status']=='met'); total=sum(x['points'] for x in subset)
        state=('完了','Complete') if stage_complete(st['id']) else ('未完了','Incomplete')
        parts.append(f'<h3>{st["title"][n]}：{earned:g}/{total:g}'+('点' if n==0 else ' points')+f' · {state[n]}</h3>')
        for x in subset:
            refs=''.join('[['+r+']]' for r in x['refs'])
            plus=score(assume=(x['id'],))
            parts.append(f'<details class="score-item" id="score-{x["id"]}"><summary>{x["id"]} · {x["title"][n]} · {STATUS[x["status"]][n]} · '+('獲得' if n==0 else 'earned ')+f'{x["points"] if x["status"]=="met" else 0:g}/{x["points"]:g}</summary><p><strong>'+('対象：' if n==0 else 'Scope: ')+f'</strong>{x["scope"][n]}</p><p><strong>'+('達成条件：' if n==0 else 'Criterion: ')+f'</strong>{x["criterion"][n]}</p><p><strong>'+('判定根拠：' if n==0 else 'Evidence judgment: ')+f'</strong>{x["evidence"][n]}{refs}</p><p>'+('この条件を追加達成すると' if n==0 else 'If this item is newly met: ')+f' {plus["percent"]:g}%（+{plus["added"]:g}'+('ポイント' if n==0 else ' points')+f'）</p><p class="small">'+('対応：' if n==0 else 'Mapping: ')+', '.join(x['tasks'])+'</p><p class="small">'+('領域：' if n==0 else 'Domains: ')+'; '.join(DOMAIN_NAMES[d][n] for d in x['domains'])+'</p><p class="small">'+('ルート：' if n==0 else 'Routes: ')+'; '.join(ROUTE_NAMES[r][n] for r in x['routes'])+'</p><p class="small">'+('実験：' if n==0 else 'Experiment: ')+(x['milestone'] or ('基礎／統合条件' if n==0 else 'foundation/integration criterion'))+f' · {x["reviewed"]}</p></details>')
    parts.append('<h3>'+('集計・変更の規則' if n==0 else 'Aggregation and revision rules')+'</h3><p>'+(
        '同じIDは一度だけ加点します。ページやルートの重複掲載では増えません。次の％も同じ採点表から未獲得分だけを加えます。段階の完了には，その段階と前段階の全必須項目が必要です。別段階の得点で不足を相殺できません。基礎4項目とM1〜M4の達成では45%です。全14項目を満たした場合のみ100%になります。',
        'Each ID earns points once, regardless of pages or routes. Future scores add only unearned points from this same rubric. Stage completion requires every item in that and all preceding stages; other points cannot compensate for a missing requirement. Foundations plus M1–M4 yield 45%. All 14 items are required for 100%.')[n]+'</p><p>'+(
        '証拠の追加・反証・訂正による得点変更は，基準を固定した評価履歴に残します。配点・条件を変える場合は基準の版を更新し，旧得点，新基準での再計算値，変更理由を併記します。',
        'Evidence additions, contrary evidence and corrections change the assessment history under a fixed rubric. Changes to weights or criteria require a new rubric version, the old score, a recalculation under the new rubric and an explanation.')[n]+f'</p><p>v{RUBRIC_VERSION} · {REVIEW_DATE} · '+('初期評価 10/100点。基準導入であり，科学的成果が一日で10点増えたことを意味しません。', 'Initial assessment: 10/100 points. Introducing the rubric does not imply a ten-point scientific advance in one day.')[n]+'</p><p><a href="/data/progress.json">'+('採点データをJSONで取得' if n==0 else 'Download the scoring data as JSON')+'</a></p>')
    return ''.join(parts)


def export_data():
    return dict(rubric_version=RUBRIC_VERSION, reviewed=REVIEW_DATE, score=score(), stages=STAGES, items=ITEMS,
                history=[dict(date=REVIEW_DATE, type='initial_rubric', rubric=RUBRIC_VERSION, earned=score()['earned'])])
