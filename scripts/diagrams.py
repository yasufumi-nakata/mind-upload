"""Original explanatory SVGs. No quantitative values are implied by geometry."""
from html import escape


def render(key, lang, definition):
    if key not in ('state', 'inverse', 'scopes', 'validation', 'carboncopies', 'individual'):
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
    if key == 'individual':
        for y,label in ((105,labels[0]),(215,labels[1])):
            rect(45,y-25,260,56)
            text(175,y+10,label,17)
            line(305,y+3,370,171)
        rect(370,132,215,78)
        text(477,166,'同じ課題への予測' if ja else 'Predictions on the',17)
        text(477,192,'各モデルを別々に評価' if ja else 'same tasks',15,'#b5c9de')
        line(585,171,650,210)
        rect(650,80,305,50)
        text(802,111,'個体Aの未使用データ' if ja else 'Held-out data from A',18)
        line(802,130,802,169)
        rect(650,169,305,88)
        text(802,202,'予測誤差・介入応答を比較' if ja else 'Compare prediction error',17)
        text(802,232,'元の個体との対応を判定' if ja else 'and intervention responses',16,'#b5c9de')
    elif key == 'state':
        rect(45,80,440,168)
        text(265,111,'脳の状態と更新' if ja else 'Brain states and updates',19)
        text(265,150,'xₜ₊₁ = F(xₜ, uₜ; θₜ)',22,'#a7c4ff')
        text(265,191,'θₜ₊₁ = Gψ(θₜ, xₜ, uₜ)',22,'#a7c4ff')
        text(265,226,'x: 状態 / θ: 特性 / u: 入力' if ja else 'x: state / θ: properties / u: input',17)
        line(485,164,540,164)
        rect(540,80,415,168)
        text(747,111,'測定と前処理 Hφ' if ja else 'Measurement and processing Hφ',19)
        text(747,157,'yₖ = Hφ(x≤tₖ) + ηₖ',23,'#6ce0cc')
        text(747,196,'φ: 較正 / η: 観測誤差' if ja else 'φ: calibration / η: observation error',17)
        text(747,227,'y: 実際に観測する信号' if ja else 'y: the signal actually observed',17)
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
