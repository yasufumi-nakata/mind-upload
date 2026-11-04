"""Original explanatory SVGs. No quantitative values are implied by geometry."""
from html import escape


def render(key, lang, definition):
    if key not in ('state', 'inverse', 'scopes', 'validation', 'carboncopies'):
        return None
    ja = lang == 'ja'
    title, labels, note = (definition[0], definition[2], definition[4]) if ja else (definition[1], definition[3], definition[5])
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 350" role="img" aria-labelledby="t d"><title id="t">{escape(title)}</title><desc id="d">{escape("; ".join(labels)+". "+note)}</desc><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#12283a"/><stop offset="1" stop-color="#101524"/></linearGradient></defs><rect width="1000" height="350" rx="22" fill="url(#bg)"/>']
    def text(x,y,t,size=18,color='#e9edf7',anchor='middle'):
        p.append(f'<text x="{x}" y="{y}" fill="{color}" text-anchor="{anchor}" font-size="{size}" font-family="system-ui,sans-serif">{escape(t)}</text>')
    def line(x1,y1,x2,y2,color='#5e9dba',dash=''):
        p.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="2" fill="none" stroke-dasharray="{dash}"/>')
    def circle(x,y,r=7,color='#6ce0cc'):
        p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')
    def rect(x,y,w,h,stroke='#42617a',fill='#17283d',rx=14):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" stroke="{stroke}" fill="{fill}"/>')
    text(45,45,title,22,anchor='start')
    if key == 'state':
        for i,label in enumerate(labels):
            x=60+i*310; rect(x,80,280,180)
            if i==0:
                nodes=[(x+95,120),(x+175,112),(x+140,164),(x+205,167),(x+72,172)]
                for a,b in [(0,1),(0,2),(1,2),(2,3),(0,4),(4,2)]: line(*nodes[a],*nodes[b])
                for node in nodes:circle(*node)
            elif i==1:
                line(x+40,173,x+240,173,'#42617a')
                p.append(f'<path d="M{x+40} 163h30l8 -9 8 13 9 -58 9 75 10 -20h33l9 -7 8 8 9 -42 9 51 9 -10h40" stroke="#6ce0cc" stroke-width="3" fill="none"/>')
            else: text(x+140,153,'x′ = F(x, u; θ)',25,'#a7c4ff')
            text(x+140,233,label,19)
    elif key == 'scopes':
        for i,label in enumerate(labels):
            x=40+240*i;rect(x,85,220,175)
            p.append(f'<ellipse cx="{x+110}" cy="145" rx="58" ry="37" fill="#25435d" stroke="#7eadd1" stroke-width="2"/>')
            if i==0:rect(x+104,129,23,20,'#7bf1d5','#5a8f9c',2)
            elif i==1:p.append(f'<ellipse cx="{x+110}" cy="145" rx="58" ry="37" fill="none" stroke="#7bf1d5" stroke-width="4"/>')
            elif i>=2:
                line(x+110,181,x+110,208,'#7bf1d5');line(x+110,191,x+85,204);line(x+110,191,x+135,204)
                if i==3:p.append(f'<path d="M{x+38} 171C{x+12} 98 {x+196} 69 {x+192} 173" fill="none" stroke="#a7c4ff" stroke-dasharray="5 5" stroke-width="2"/>')
            text(x+110,243,label,16)
    elif key == 'inverse':
        rect(38,123,180,90);text(128,174,labels[0],19)
        for i,y in enumerate([100,173,246]):
            line(218,168,302,y);rect(304,y-24,165,48);text(386,y+6,('候補 ' if ja else 'Model ')+chr(65+i),18);line(469,y,555,168)
        rect(555,120,203,96);text(656,160,'未使用の介入' if ja else 'Held-out intervention',17);text(656,190,'応答を予測' if ja else 'Predict responses',16,'#9cb5cf')
        for i,(y,c) in enumerate([(110,'#6ce0cc'),(176,'#a7c4ff'),(240,'#f4bb91')]):
            line(758,168,805,y,c);line(805,y,950,y,c);text(920,y-9,chr(65+i),15,c)
    elif key == 'validation':
        coords=[(500,93),(775,151),(685,244),(315,244),(225,151)]
        for (x,y),label in zip(coords,labels):
            line(500,176,x,y,'#42617a');rect(x-95,y-23,190,46);text(x,y+6,label,16)
        circle(500,176,39,'#254758');text(500,172,'同じ個体' if ja else 'Same',15);text(500,192,'独立テスト' if ja else 'individual',13,'#a6e4db')
    elif key == 'carboncopies':
        centers=[(220,164),(500,164),(780,164)]
        for (x,y),label in zip(centers,labels):
            rect(x-126,88,252,166)
            text(x,128,label.split(':')[0].split('：')[0],21,'#6ce0cc')
            text(x,172,('課題と依存関係' if x==220 else 'モデル・仮想計測' if x==500 else '復元と比較') if ja else ('Questions & dependencies' if x==220 else 'Models & virtual measures' if x==500 else 'Reconstruction & tests'),15)
            text(x,218,('研究計画' if x==220 else '開発基盤' if x==500 else '評価の枠組み') if ja else ('Research programme' if x==220 else 'Development platform' if x==500 else 'Evaluation framework'),14,'#9cb5cf')
        line(346,173,374,173);line(626,173,654,173)
    text(500,318,note,16,'#b5c9de')
    p.append('</svg>')
    return ''.join(p)
