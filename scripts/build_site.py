#!/usr/bin/env python3
"""Build the dependency-free bilingual reference site from editorial sources."""
import html
import importlib.util
import json
import re
from pathlib import Path
from diagrams import render as render_diagram

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('site_content', ROOT / 'content/site_content.py')
content = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content)
PAGES = content.PAGES
REFS = json.loads((ROOT / 'content/references.json').read_text())
for source_id, source in REFS.items():
    if not source.get('citation_eligible') or source.get('reading_status') != 'fulltext_reviewed':
        raise ValueError(f'Unreviewed or unavailable source cannot be published: {source_id}')
DATE = '2026-11-04'
BASE = 'https://mind-upload.com'
H = html.escape
NAV = [('science', '科学', 'Science'), ('progress', '到達点', 'Evidence'),
       ('carboncopies', 'Carboncopies', 'Carboncopies'), ('validation', '検証', 'Validation'),
       ('future', '戦略と展望', 'Strategy'), ('action', '研究を始める', 'Research'),
       ('history', '歴史・2050', 'History & 2050'), ('resources', '文献', 'Library')]

DIAGRAMS = {
 'pipeline': ('測定と再現を結ぶ研究工程', 'The measurement-to-emulation pipeline',
              ['保存・計測', '回路の再構成', '状態・規則の推定', '実行と身体', '独立した検証'],
              ['Measure', 'Reconstruct', 'Infer state & rules', 'Run & embody', 'Validate'],
              '不足する情報を、検証結果から計測へ戻します', 'Use failures to decide what to measure next'),
 'state': ('脳モデルの三つの記述', 'Three descriptions of a brain model',
           ['特性 θ(t)：接続・伝達', '状態 x(t)：電位・適応', '規則 F・G：応答・学習'],
           ['Properties θ(t)', 'State x(t)', 'Rules F & G'],
           '入力 u と身体・環境との相互作用を含めて評価します', 'Evaluate inputs and the body–environment loop'),
 'inverse': ('同じ観測に合う、複数のモデル', 'Different models can fit the same observations',
             ['観測データ', '候補モデル A / B / C', '新しい刺激・介入', '候補を比較'],
             ['Observed data', 'Models A / B / C', 'New interventions', 'Compare models'],
             '予測の一致だけで、内部機構が一意に決まるとは限りません', 'Predictive agreement need not identify a unique mechanism'),
 'memory': ('記憶の再現を調べる実験', 'An experiment for retained memory',
            ['同じ個体で学習', '構造と活動を測定', 'モデルを復元', '独立した想起課題'],
            ['Individual learns', 'Measure the brain', 'Reconstruct model', 'Independent recall'],
            '保持・忘却・再学習と、未学習の対照条件を比べます', 'Compare retention, forgetting, relearning, and untrained controls'),
 'preservation': ('保存から機能の復元まで', 'From preservation to restored function',
                  ['微細構造が残る', '必要な状態が残る', '情報を読み出せる', '機能を検証する'],
                  ['Structure retained', 'State retained', 'Information read', 'Function tested'],
                  '各矢印は、それぞれ別の実証を必要とします', 'Every arrow requires its own evidence'),
 'scopes': ('接続図を比較する前に、対象の境界をそろえます', 'Compare boundaries before comparing connectomes',
            ['局所体積', '脳全体', '中枢神経系', '身体との閉ループ'],
            ['Local volume', 'Whole brain', 'Central nervous system', 'Body–environment loop'],
            '領域の広さと機能再現の完成度は、異なる軸です', 'Anatomical coverage and functional fidelity are different axes'),
 'fidelity': ('忠実度は、目的とテストによって定まります', 'Fidelity depends on the target and the tests',
              ['何を保持するか', '測定の精度・費用', 'モデルの詳細度', 'テストで比較'],
              ['Define the target', 'Measurement budget', 'Model detail', 'Compare with tests'],
              '細かいモデルであること自体が、正しさの保証にはなりません', 'A more detailed model is not automatically a more correct model'),
 'validation': ('独立した証拠を組み合わせます', 'Combine independent kinds of evidence',
                ['構造', 'ダイナミクス', '因果応答', '学習・記憶', '身体・環境'],
                ['Structure', 'Dynamics', 'Causal response', 'Learning & memory', 'Embodiment'],
                '学習に使用していない条件で、元の系と対応を調べます', 'Test correspondence to the original on held-out conditions'),
 'roadmap': ('実証を積み上げる技術ロードマップ', 'A roadmap built from demonstrable capabilities',
             ['計測誤差を知る', '再構成誤差を知る', '識別可能性を調べる', '機能を検証する'],
             ['Measure errors', 'Trace reconstruction', 'Test identifiability', 'Validate function'],
             '失敗から必要なデータを決め、工程を繰り返します', 'Use failure to choose the next data, then iterate'),
 'carboncopies': ('Carboncopiesの研究プログラムの関係', 'How the Carboncopies research programmes connect',
                  ['Roadmap：課題を整理', 'BrainGenix：実験基盤', 'Challenge：方法を比較'],
                  ['Roadmap: requirements', 'BrainGenix: platform', 'Challenge: comparison'],
                  '公式情報をもとにした模式図です。達成度を示す図ではありません', 'Schematic based on official sources; not a maturity rating'),
 'individual': ('元の個体に固有の情報を、対照と比べます', 'Test information specific to the original individual',
                ['A由来のモデル', '他個体・平均モデル', '各モデルの予測', 'Aの未使用データと比較'],
                ['Model derived from A', 'Other / average models', 'Predictions from each model', 'Compare with held-out data from A'],
                '評価する記憶の答えを、モデルの学習へ持ち込まない設計にします', 'Keep the answers to memory tests out of model fitting'),
}

def diagram_svg(key, lang):
    specialized = render_diagram(key, lang, DIAGRAMS[key])
    if specialized:
        (ROOT / f'assets/figures/{key}-{lang}.svg').write_text(specialized)
        return
    ja_title, en_title, ja_labels, en_labels, ja_note, en_note = DIAGRAMS[key]
    title = ja_title if lang == 'ja' else en_title
    labels = ja_labels if lang == 'ja' else en_labels
    note = ja_note if lang == 'ja' else en_note
    n = len(labels)
    w, gap, left = (1000 - 100 - 20 * (n - 1)) / n, 20, 50
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 350" role="img" aria-labelledby="title desc"><title id="title">{H(title)}</title><desc id="desc">{H(' → '.join(labels)+'. '+note)}</desc><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101d2c"/><stop offset="1" stop-color="#0d1321"/></linearGradient><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="none" stroke="#6bdaca"/></marker></defs><rect width="1000" height="350" rx="22" fill="url(#bg)"/><text x="50" y="54" fill="#e9edf7" font-family="system-ui,sans-serif" font-size="23" font-weight="650">{H(title)}</text>''']
    for i, label in enumerate(labels):
        x = left + i * (w + gap)
        parts += [f'<rect x="{x}" y="108" width="{w}" height="118" rx="14" fill="#17243a" stroke="#39546b"/>',
                  f'<circle cx="{x+27}" cy="136" r="13" fill="#5ed8c6"/><text x="{x+27}" y="141" text-anchor="middle" font-size="14" font-family="system-ui" fill="#0a0d14">{i+1}</text>',
                  f'<text x="{x+w/2}" y="185" text-anchor="middle" fill="#e9edf7" font-family="system-ui,sans-serif" font-size="{16 if n>4 else 18}">{H(label)}</text>']
        if i < n - 1:
            parts.append(f'<path d="M{x+w+2} 166h{gap-5}" stroke="#6bdaca" stroke-width="2" marker-end="url(#arrow)"/>')
    parts.append(f'<path d="M950 242v22H52v-22" stroke="#7aa2ff" stroke-width="1.5" fill="none" stroke-dasharray="5 5"/><text x="500" y="309" text-anchor="middle" fill="#b6c9de" font-size="17" font-family="system-ui,sans-serif">{H(note)}</text></svg>')
    (ROOT / f'assets/figures/{key}-{lang}.svg').write_text(''.join(parts))

def figure(key, lang):
    if key in DIAGRAMS:
        title = DIAGRAMS[key][0 if lang == 'ja' else 1]
        src = f'/assets/figures/{key}-{lang}.svg'
        credit = '本サイト作成の概念図。' if lang == 'ja' else 'Original schematic by this site. '
        if key == 'carboncopies': credit += ' [[CCRESEARCH]][[CCCHALLENGE]][[CCROADMAP]]'
        elif key in ('fidelity','validation'): credit += ' [[XKB4CG64]]'
        elif key == 'inverse': credit += ' [[274IXB72]]'
        wh = 'width="1000" height="350"'
    elif key == 'flywire':
        title = 'FlyWireによる成体ハエ脳の接続再構成' if lang == 'ja' else 'FlyWire reconstruction of an adult fly brain'
        src = '/assets/figures/flywire-2024-fig1.webp'
        credit = ('Dorkenwald et al. (2024), Figure 1。' if lang == 'ja' else 'Dorkenwald et al. (2024), Figure 1. ')
        credit += ' <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. '
        credit += ('内容の変更なし。表示サイズのみ調整。[[ADD196]]' if lang == 'ja' else 'Unmodified content, resized for display. [[ADD196]]')
        wh = 'width="1417" height="1018"'
    elif key == 'liconn':
        title = 'LICONN：拡大と光学撮像による哺乳類組織の接続再構成' if lang == 'ja' else 'LICONN: expansion and optical reconstruction of mammalian tissue'
        src = '/assets/figures/liconn-2025-fig1.webp'
        credit = ('Tavakoli et al. (2025), Figure 1。' if lang == 'ja' else 'Tavakoli et al. (2025), Figure 1. ')
        credit += ' <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. '
        credit += ('出版社配信のWebP版。内容の変更なし。[[ADD198]]' if lang == 'ja' else 'Publisher-served WebP version; content unmodified. [[ADD198]]')
        wh = 'width="1616" height="2351"'
    else: raise ValueError(key)
    enlarge = '図を大きく表示' if lang == 'ja' else 'Open full-size figure'
    return f'<figure class="research-figure"><a href="{src}" aria-label="{H(enlarge+": "+title)}"><img src="{src}" alt="{H(title)}" {wh} loading="lazy" decoding="async"></a><figcaption><strong>{H(title)}</strong><br>{credit} <a href="{src}">{enlarge}</a></figcaption></figure>'

def citation_record(ref, lang='en'):
    authors = ref.get('author_display') or ref.get('authors') or []
    author = ', '.join(authors[:6]) + (', et al.' if len(authors) > 6 else '')
    venue = ref.get('venue','')
    vi = str(ref.get('volume') or '')
    if ref.get('issue'): vi += '(' + str(ref['issue']) + ')'
    if ref.get('pages'): vi += (':' if vi else '') + str(ref['pages'])
    date = ref.get('year') or 'n.d.'
    title = H(ref['title'])
    if ref.get('url'): title = f'<a class="ref-link" href="{H(ref["url"],quote=True)}">{title}</a>'
    if ref.get('type') == 'bookSection':
        editor = '; '.join(ref.get('editor_display', []))
        editor_text = f' In: {H(editor)}, ed. ' if editor else ' In: '
        txt = f'{H(author.rstrip("."))}. {title}.' + editor_text + f'<i>{H(venue)}</i>. {H(ref.get("publisher", ""))}; {H(str(date))}'
    else:
        txt = f'{H(author.rstrip("."))}. {title}. <i>{H(venue)}</i>. {H(str(date))}'
    if vi: txt += ';' + H(vi)
    txt = txt.rstrip('.') + '.'
    if ref.get('doi'): txt += f' <a href="https://doi.org/{H(ref["doi"],quote=True)}">doi:{H(ref["doi"])}</a>.'
    if ref.get('type') == 'webpage': txt += (' 確認日：' if lang=='ja' else ' Accessed: ') + DATE + '.'
    if ref.get('note'): txt += ' <span class="small">'+H(ref['note'])+'</span>'
    return txt

def publication_type(r, lang):
    labels = {'peer_reviewed': ('査読論文', 'Peer-reviewed article'),
              'peer_reviewed_conference': ('査読会議論文', 'Peer-reviewed conference paper'),
              'preprint': ('プレプリント', 'Preprint'),
              'technical_report': ('技術報告・総説', 'Technical report / review'),
              'book_chapter': ('書籍の章', 'Book chapter'),
              'official_web': ('公式ウェブ資料', 'Official web resource')}
    if r.get('publication_status') in labels:
        return labels[r['publication_status']][0 if lang == 'ja' else 1]
    if r.get('type') == 'webpage': return 'ウェブ資料' if lang=='ja' else 'Web resource'
    if any(t in (r.get('venue','')+' '+r.get('url','')+' '+r.get('doi','')).lower() for t in ('arxiv','10.1101','10.64898','biorxiv')):
        return 'プレプリント／公開原稿' if lang=='ja' else 'Preprint / public manuscript'
    if r.get('type') in ('book','bookSection'): return '書籍・章' if lang=='ja' else 'Book / chapter'
    return '論文・技術資料' if lang=='ja' else 'Article / technical resource'

def library(lang):
    candidates = [r for r in REFS.values() if r.get('category') != 'organizations']
    cats = sorted(set(r.get('category','') for r in candidates))
    label = '題名・著者・DOIで検索' if lang=='ja' else 'Search title, authors, or DOI'
    all_label = 'すべての分野' if lang=='ja' else 'All categories'
    cat_label = '分野' if lang=='ja' else 'Category'
    cat_translation = {'シミュレーション・計算基盤':'Simulation and computing','構造・コネクトミクス':'Structure and connectomics','理論・逆問題':'Theory and inverse problems','計測・顕微鏡':'Measurement and microscopy','同定・検証':'Identification and validation','神経プロテーゼ・BCI':'Neuroprosthetics and BCI','記憶・可塑性':'Memory and plasticity','保存・読み出し':'Preservation and readout','保存・生体状態':'Preservation and biological state','同定・検証・逆問題':'Identification, validation and inverse problems','理論・基礎':'Theory and foundations','計測・画像再構成':'Measurement and image reconstruction','閉ループ・神経補綴':'Closed-loop systems and neuroprosthetics'}
    options = ''.join(f'<option value="{H(c)}">{H(c if lang=="ja" else cat_translation.get(c,c))}</option>' for c in cats)
    rows=[]
    for r in sorted(candidates,key=lambda r:(str(r.get('year','')),r['title']),reverse=True):
        cat=r.get('category','')
        status = '本文確認済み・解説に使用' if lang=='ja' else 'Full text reviewed; used in this guide'
        scope = r.get('review_scope',{}).get(lang,'')
        scope_html = f'<p class="small">{H(scope)}</p>' if scope else ''
        rows.append(f'<li class="library-record" data-category="{H(cat)}" data-search="{H((r["title"]+" "+" ".join(r.get("authors",[]))+" "+r.get("doi","")).lower(),quote=True)}"><p class="record-tags"><span>{H(cat if lang=="ja" else cat_translation.get(cat,cat))}</span><span>{publication_type(r,lang)}</span><span>{status}</span></p><p>{citation_record(r,lang)}</p>{scope_html}</li>')
    return f'<div class="library-controls"><label>{label}<input id="library-search" type="search" placeholder="connectome, Koene, 10.1038…"></label><label>{cat_label}<select id="library-category"><option value="">{all_label}</option>{options}</select></label></div><p id="library-count" role="status" aria-live="polite">{len(candidates)} '+('件' if lang=='ja' else 'records')+f'</p><p><a href="/assets/references.bib" download>BibTeX</a> · <a href="/assets/references.json" download>JSON</a></p><ol class="library-list">'+''.join(rows)+'</ol><p id="library-empty" hidden>'+('該当する文献がありません。検索語か分野を変更してください。' if lang=='ja' else 'No matching records. Change the query or category.')+'</p>'

def calculator(lang):
    fields=[('volume', '撮像体積 V (mm³)', 'Imaged volume V (mm³)',1,0.001,2000000,'any'),
            ('voxel-x', 'ボクセル幅 dₓ (nm)', 'Voxel width dₓ (nm)',10,1,1000,'any'),
            ('voxel-y', 'ボクセル幅 dᵧ (nm)', 'Voxel width dᵧ (nm)',10,1,1000,'any'),
            ('voxel-z', 'ボクセル厚 dᶻ (nm)', 'Voxel depth dᶻ (nm)',10,1,1000,'any'),
            ('bytes-voxel', 'ボクセル当たり b (byte)', 'Bytes per voxel b',1,1,16,1),
            ('synapses', 'シナプス数 S', 'Synapse count S',50000000,1,1e16,1),
            ('bytes-synapse', 'シナプス当たり状態量 m (byte)', 'State bytes per synapse m',16,1,4096,1),
            ('frequency', '1シナプス当たりの更新頻度 f (Hz)', 'Update frequency per synapse f (Hz)',1000,1,1000000,1)]
    labels=''.join(f'<label for="calc-{k}">{H(ja if lang=="ja" else en)}<input id="calc-{k}" type="number" value="{value:g}" min="{lo:g}" max="{hi:g}" step="{step}" required></label>' for k,ja,en,value,lo,hi,step in fields)
    return '<div class="calculator" id="scale-calculator"><div class="calc-fields">'+labels+'</div><div id="calc-result" role="status" aria-live="polite"></div><p class="small"><code>V × 10¹⁸ / (dₓ × dᵧ × dᶻ) × b</code> '+('byte（無圧縮画像）' if lang=='ja' else 'bytes (raw image)')+'<br><code>S × m</code> '+('byte（シナプス状態のみ）' if lang=='ja' else 'bytes (synapse states only)')+'<br><code>S × f</code> '+('回/秒（密な更新。FLOPSではありません）' if lang=='ja' else 'updates/s (dense update count, not FLOPS)')+'</p></div>'

def expand_body(body,lang):
    return re.sub(r'\{\{([a-z]+)\}\}', lambda m: library(lang) if m[1]=='library' else calculator(lang) if m[1]=='calculator' else figure(m[1],lang),body)

def build_page(key,p,lang):
    prefix='/ja/' if lang=='ja' else '/'
    path=prefix if key=='index' else prefix+key+'.html'
    enpath='/' if key=='index' else '/'+key+'.html'
    japath='/ja/' if key=='index' else '/ja/'+key+'.html'
    title=p['title'][lang];desc=p['lead'][lang]
    used=[]
    def cite(m):
        k=m[1]
        if k not in REFS: raise KeyError(f'Missing reference {k} in {key}')
        if k not in used: used.append(k)
        return f'<sup><a href="#ref-{k}" aria-label="{H(REFS[k]["title"],quote=True)}">[{used.index(k)+1}]</a></sup>'
    sections=[]
    for section in p['sections']:
        body=re.sub(r'\[\[([A-Z0-9]+)\]\]',cite,expand_body(section['body'][lang],lang))
        sections.append(f'<section id="{section["id"]}"><h2>{H(section["title"][lang])}</h2>{body}</section>')
    refs='<section id="references"><h2>'+('参考文献' if lang=='ja' else 'References')+'</h2><ol class="refs">'+''.join(f'<li id="ref-{k}">{citation_record(REFS[k],lang)}</li>' for k in used)+'</ol></section>'
    nav=''.join(f'<a href="{prefix+k}.html"'+(' aria-current="page"' if k==key else '')+f'>{ja if lang=="ja" else en}</a>' for k,ja,en in NAV)
    toc='<nav class="toc" aria-label="'+('目次' if lang=='ja' else 'On this page')+'"><span class="tag">'+('このページの内容' if lang=='ja' else 'On this page')+'</span><ol>'+''.join(f'<li><a href="#{s["id"]}">{H(s["title"][lang])}</a></li>' for s in p['sections'])+'</ol></nav>'
    if key == 'index':
        toc = ''
    elif key == 'history':
        jump = [('dashboard', '6領域の進捗', 'Six-domain status'), ('roadmap2050', '2050年への道筋', 'Path to 2050'), ('target', '完成の条件', 'Success criteria'), ('timeline', '技術の歴史', 'Technical history')]
        toc = '<nav class="overview-nav" aria-label="'+('このページの内容' if lang=='ja' else 'On this page')+'">'+''.join(f'<a href="#{sid}">{ja if lang=="ja" else en}</a>' for sid,ja,en in jump)+'</nav>'
    schema={'@context':'https://schema.org','@type':'WebSite' if key=='index' else 'Article','name':title,'headline':title,'description':desc,'url':BASE+path,'inLanguage':lang,'dateModified':DATE,'isPartOf':{'@type':'WebSite','name':'Mind Uploading Research Guide','url':BASE+'/'},'citation':[REFS[k]['url'] for k in used if REFS[k].get('url')]}
    other='/ja/' if lang=='en' else '/'
    badge='研究ガイド · 2026年11月版' if lang=='ja' else 'Research guide · November 2026'
    footer='実証研究、理論、公開計画を区別して読むための資料集です。Carboncopies Foundationの公式サイトではありません。' if lang=='ja' else 'A guide that distinguishes experiments, theory, and published plans. This is not an official Carboncopies Foundation website.'
    out=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H(title)} | Mind Uploading</title><meta name="description" content="{H(desc,quote=True)}">
<link rel="canonical" href="{BASE+path}"><link rel="alternate" hreflang="en" href="{BASE+enpath}"><link rel="alternate" hreflang="ja" href="{BASE+japath}"><link rel="alternate" hreflang="x-default" href="{BASE+enpath}">
<meta property="og:title" content="{H(title,quote=True)}"><meta property="og:description" content="{H(desc,quote=True)}"><meta property="og:type" content="{'website' if key=='index' else 'article'}"><meta property="og:url" content="{BASE+path}"><meta property="og:locale" content="{'ja_JP' if lang=='ja' else 'en_US'}"><meta property="og:image" content="{BASE}/assets/og-image.png?v=20261104-r3"><meta property="og:image:alt" content="Mind Uploading Research Guide"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#0a0d14">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css?v=20261104-r3"><link rel="stylesheet" href="/assets/research.css?v=20261104-r3"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><script src="/assets/site.js?v=20261104-r3" defer></script><script src="/assets/research.js?v=20261104-r3" defer></script></head>
<body id="top" data-page="{key}"><a class="skip-link" href="#main">{'本文へ移動' if lang=='ja' else 'Skip to content'}</a><div id="progress"></div>
<header class="site-header"><div class="nav-inner"><a class="brand" href="{prefix}"><span class="dot"></span>Mind Uploading</a><nav class="primary-nav" aria-label="{'主要ページ' if lang=='ja' else 'Main pages'}">{nav}</nav><div class="lang-switch" role="group" aria-label="Language / 言語"><a href="{enpath}" hreflang="en" {'aria-current="true"' if lang=='en' else ''}>EN</a><a href="{japath}" hreflang="ja" lang="ja" {'aria-current="true"' if lang=='ja' else ''}>日本語</a></div><button class="nav-toggle" aria-label="{'メニュー' if lang=='ja' else 'Menu'}" aria-expanded="false">☰</button></div></header>
<main id="main"><section class="ch-hero"><span class="badge">{badge}</span><h1>{H(title)}</h1><p class="lead">{H(desc)}</p><div class="ch-meta"><span>{'資料確認日' if lang=='ja' else 'Sources checked'}: {DATE}</span><span>{'研究論文・技術報告・公式情報を区別して解説' if lang=='ja' else 'Research, technical reviews and official statements distinguished'}</span></div>{toc}</section>{''.join(sections)}{refs}</main>
<footer class="site-footer"><div class="footer-inner"><a class="brand" href="{prefix}">Mind Uploading</a><p>{footer}</p><nav class="footer-nav">{nav}</nav><p class="small">{'図版の出典・利用条件は各図の下に記載しています。' if lang=='ja' else 'Figure sources and reuse terms appear in each caption.'} · <a href="#top">{'ページ上部へ' if lang=='ja' else 'Back to top'}</a></p></div></footer></body></html>'''
    dest=ROOT/('ja' if lang=='ja' else '')/(key+'.html')
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(out)
    return path

def build():
    (ROOT/'assets/figures').mkdir(exist_ok=True)
    for key in DIAGRAMS:
        for lang in ('en','ja'): diagram_svg(key,lang)
    paths=[]
    for lang in ('en','ja'):
        for key,p in PAGES.items(): paths.append(build_page(key,p,lang))
        prefix='/ja/' if lang=='ja' else '/'
        for old,new in [('philosophy','validation'),('scenario','future')]:
            target=prefix+new+'.html'
            msg='内容を技術研究のページへ更新しました。' if lang=='ja' else 'This content has moved to the updated technical research guide.'
            (ROOT/('ja' if lang=='ja' else '')/(old+'.html')).write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{BASE+target}"><meta name="robots" content="noindex"><title>Mind Uploading — updated page</title></head><body><p>{msg} <a href="{target}">{H(PAGES[new]["title"][lang])}</a></p></body></html>')
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE+p}</loc><lastmod>{DATE}</lastmod></url>' for p in paths)+'</urlset>')
    (ROOT/'assets/references.json').write_text(json.dumps(list(REFS.values()),ensure_ascii=False,indent=2))
    bib=[]
    for k,r in REFS.items():
        vals={'title':r['title'],'author':' and '.join(r.get('bibtex_authors') or ['{'+a+'}' for a in r.get('authors',[])]),'year':r.get('year',''),'journal':r.get('venue',''),'volume':r.get('volume',''),'number':r.get('issue',''),'pages':r.get('pages',''),'doi':r.get('doi',''),'url':r.get('url',''),'urldate':DATE,'note':r.get('note','')}
        vals={key:str(value).replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_') for key,value in vals.items() if value}
        kind = {'book':'book', 'bookSection':'incollection', 'conferencePaper':'inproceedings', 'webpage':'misc', 'report':'techreport'}.get(r.get('type'), 'article' if r.get('venue') else 'misc')
        if kind == 'book' and 'journal' in vals:
            vals['publisher'] = vals.pop('journal')
        if kind == 'techreport' and 'journal' in vals:
            vals['institution'] = vals.pop('journal')
        if kind == 'incollection' and 'journal' in vals:
            vals['booktitle'] = vals.pop('journal')
            if r.get('publisher'): vals['publisher'] = r['publisher']
            if r.get('editors'): vals['editor'] = ' and '.join(r['editors'])
        if kind == 'inproceedings' and 'journal' in vals:
            vals['booktitle'] = vals.pop('journal')
        bib.append('@'+kind+'{'+k+',\n'+',\n'.join('  '+name+' = {'+value+'}' for name,value in vals.items())+'\n}')
    (ROOT/'assets/references.bib').write_text('\n\n'.join(bib)+'\n')
    print(f'Built {len(paths)} pages, 4 legacy redirects, {len(DIAGRAMS)*2} localized diagrams, {len(REFS)} reference records.')

if __name__=='__main__': build()
