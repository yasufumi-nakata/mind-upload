---
layout: default
title: "NetPyNE docs: NetPyNE モデリング仕様 v1.0<a href=\"#netpyne-modeling-specification-v1-0\" class=\"headerlink\" title=\"Link to this heading\"></a>"
description: "NetPyNE docs: modeling-specification-v1.0.md の日本語訳"
article_type: 翻訳資料
last_updated: '2026-05-20'
audience: 外部資料を日本語で原文順に読みたい読者
reading_time: 原文量に依存
page_intro: "このページは外部資料の日本語訳です。原文の見出し順と本文順を保ち、コード・URL・出典表記はできるだけ原形のまま残しています。"
accuracy_note: "機械翻訳をベースにした日本語訳です。実装手順や引用は必ず原典も確認してください。"
---

<main class="main-container">
<article class="content-column">

<div class="note-box">
<strong>出典とライセンス</strong>
<p>原典: <a href="http://doc.netpyne.org/modeling-specification-v1.0.html" target="_blank" rel="noopener noreferrer">http://doc.netpyne.org/modeling-specification-v1.0.html</a></p>
<p>ライセンス: MIT License for NetPyNE repository documentation/code。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="netpyne-modeling-specification-v1-0" class="section">

<span id="modeling-specification"></span>

# NetPyNE モデリング仕様 v1.0<a href="#netpyne-modeling-specification-v1-0" class="headerlink" title="Link to this heading"></a>

<div class="toctree-wrapper compound">

</div>

<div id="overview-of-specification" class="section">

## 仕様の概要<a href="#overview-of-specification" class="headerlink" title="Link to this heading"></a>

NetPyNE モデリング仕様は、分子スケールから回路スケールまでニューロン ネットワークの生物学的パラメーターを定義するための標準化された宣言言語を提供します。

これらの標準化された仕様は、人間が判読できる、クリーンでコンパクトな、ルールベースの JSON 互換形式を採用しています。この宣言型言語を使用すると、ユーザーは、NEURON での実装に必要な複雑な技術的側面をすべて隠しながら、各生物学的スケールで観察される特性とパターンを正確に記述することができます。たとえば、Python または hoc for ループを使用して潜在的に数百万のセル間接続を作成する代わりに、2 つの母集団間の確率的接続ルールを定義できます。宣言型言語により、すべてのモデル パラメーター (集団、細胞特性、接続性、刺激、分子反応拡散) の構造化された仕様が可能になります。

- 参考文献: Dura-Bernal S、Suter B、Gleeson P、Cantarelli M、Quintana A、Rodriguez F、Kedziora DJ、Chadderdon GL、Kerr CC、Neymotin SA、McDougal R、Hines M、Shepherd GMG、Lytton WW。 (2019) NetPyNE: 脳回路のデータ駆動型マルチスケール モデリングのためのツール。 eLife 2019;8:e44494 - <a href="https://elifesciences.org/articles/44494" class="reference external">https://elifesciences.org/articles/44494</a>

- 仕様 JSON ベースのスキーマ: <a href="https://github.com/suny-downstate-medical-center/netpyne/blob/development/netpyne/metadata/metadata.py" class="reference external">https://github.com/suny-downstate-medical-center/netpyne/blob/development/netpyne/metadata/metadata.py</a>

- スキーマパッケージ経由の仕様検証コード: <a href="https://github.com/suny-downstate-medical-center/netpyne/blob/development/netpyne/sim/validator.py" class="reference external">https://github.com/suny-downstate-medical-center/netpyne/blob/development/netpyne/sim/validator.py</a>

</div>

<div id="authors-and-contributors" class="section">

## 著者と寄稿者<a href="#authors-and-contributors" class="headerlink" title="Link to this heading"></a>

この仕様のオリジナルの作成者は、Salvador Dura-Bernal (<a href="mailto:salvadordura%40gmail.com" class="reference external">salvadordura<span>@</span>gmail<span>.</span>com</a>) です。この仕様への貢献者には、Padraig Gleeson、Joe W Graham、Eugenio Urdapilleta、Valery Bragin、James Chen、William W Lytton、Michael L Hines、Ben Suter、Greg Patrick、Matteo Cantarelli、Dario del Piano、Filippo Ledda、Facundo Rodriguez、Nicolas Gomez、Afonso Pinto、Craig Kelley、Adrian Quintana、が含まれます。シッダールタ・ミトラ、アダム・ニュートン、ジョアン・ヴィトール、クリフ・カー、デヴィッド・ケジオラ。

</div>

<div id="network-parameters" class="section">

## ネットワークパラメータ<a href="#network-parameters" class="headerlink" title="Link to this heading"></a>

クラス <span class="pre">`NetParams`</span> の <span class="pre">`netParams`</span> オブジェクトには、ネットワークを定義するために必要な情報がすべて含まれています。これは、次の順序付けられた辞書で構成されます。

- <span class="pre">`cellParams`</span> - セルのタイプとそれに関連するパラメータ (セルの形状など)

- <span class="pre">`popParams`</span> - ネットワーク内の人口とそのパラメータ

- <span class="pre">`synMechParams`</span> - シナプス機構とそのパラメータ

- <span class="pre">`connParams`</span> - ネットワーク接続ルールとそれに関連するパラメータ。

- <span class="pre">`subConnParams`</span> - ネットワークのセルラー接続ルールとそれに関連するパラメーター。

- <span class="pre">`stimSourceParams`</span> - 刺激源パラメータ。

- <span class="pre">`stimTargetParams`</span> - 刺激源と標的細胞間のマッピング。

- <span class="pre">`rxdParams`</span> - 反応拡散 (RxD) コンポーネントとそのパラメーター。

<a href="_images/netparams.png" class="reference internal image-reference"><img src="_images/netparams.png" class="align-center" style="width: 60%;" alt="_images/netparams.png" /></a>

これらの順序付けされた辞書はそれぞれ、直接入力することも、NetParams オブジェクト メソッドを使用して入力することもできます。どちらの方法も同等ですが、オブジェクト メソッドは追加されるパラメーターの構文をチェックします。以下は、popParams 順序付きディクショナリに項目を追加する 2 つの同等の方法です。

<div class="highlight-default notranslate">

<div class="highlight">

    from netpyne import specs
    netParams = specs.NetParams()

    # Method 1: direct
    netParams.popParams['Pop1'] = {'cellType': 'PYR', 'numCells': 20}

    # Method 2: using object method
    netParams.addPopParams(label='Pop1', params={'cellType': 'PYR', 'numCells': 20})

</div>

</div>

<span class="pre">`netParams`</span> の構成は、フレームワークが内部で実行する標準的なイベント シーケンスと一致しています。

- <span class="pre">`cellParams`</span> に基づいてタイプに応じてセルのプロパティを設定します。

- <span class="pre">`Network`</span> オブジェクトを作成し、その中に <span class="pre">`popParams`</span> に基づく <span class="pre">`Cell`</span> オブジェクトと <span class="pre">`Population`</span> オブジェクトのセットを追加します

- <span class="pre">`connParams`</span> および <span class="pre">`subConnParams`</span> (どのシナプス前セルとシナプス後セルが接続ルールの条件に一致するかを確認) に基づいて、<span class="pre">`synMechParams`</span> のシナプス パラメーターを使用して一連の接続を作成します。

- <span class="pre">`stimSourceParams`</span> および <span class="pre">`stimTargetParams`</span> に基づいて細胞に刺激を追加します

さらに、<span class="pre">`netParams`</span> には、次のカスタマイズ可能な単一値属性が含まれています (例: <span class="pre">`netParams.sizeX`</span>` `<span class="pre">`=`</span>` `<span class="pre">`100`</span>)。

- **scale**: セル数のスケール係数乗数 (デフォルト: 1)

- **形状**: ネットワークの形状: 「直方体」、「円柱」、または「楕円体」 (デフォルト: 「直方体」)

- **sizeX**: x 次元 (水平方向の長さ) ネットワーク サイズ (μm 単位) (デフォルト: 100)

- **sizeY**: y 次元 (垂直高さまたは皮質深さ) ネットワーク サイズ (μm 単位) (デフォルト: 100)

- **sizeZ**: Z 次元 (水平方向の奥行き) ネットワーク サイズ (μm 単位) (デフォルト: 100)

- **rotateCellsRandomly**: y 軸 \[min,max\] ラジアンを中心にセルをランダムに回転します。 \[0, 3.0\] (デフォルト: False)

- **defaultWeight**: デフォルトの接続の重み (デフォルト: 1)

- **defaultDelay**: デフォルトの接続遅延 (ミリ秒単位) (デフォルト: 1)

- **propVelocity**: um/ms 単位の伝導速度 (例: 500 um/ms = 0.5 m/s) (デフォルト: 500)

- **scaleConnWeight**: 接続重みスケール係数 (NetStims を除く) (デフォルト: 1)

- **scaleConnWeightNetStims**: NetStims の接続重みスケール係数 (デフォルト: 1)

- **scaleConnWeightModels**: 各セル モデルの接続重量スケール係数 (例: {'HH': 0.1、'Izhi': 0.2} (デフォルト: {})

- **popTagsCopiedToCells**: 母集団からセルにコピーされるタグのリスト (デフォルト: \[‘pop’, ‘cellModel’, ‘cellType’\])

<span class="pre">`netParams`</span> dict への他の任意のエントリを追加し、接続パラメーターのカスタム定義関数で使用できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a> を参照)。

<div id="cell-types" class="section">

<span id="id1"></span>

### セルの種類<a href="#cell-types" class="headerlink" title="Link to this heading"></a>

<span class="pre">`cellParams`</span> 順序付き辞書の各項目は、キーと値で構成されます。キーは、このセルの種類を識別するためのラベルです。値は、次のフィールドを含むセルのプロパティを定義するディクショナリで構成されます。

- **secs** - セルのセクションを含むディクショナリ。各セクションには次のフィールドが含まれます (空のフィールドは省略できます)。

> <div>
  >
  > - **geom**: <span class="pre">`diam`</span>、<span class="pre">`L`</span>、または <span class="pre">`Ra`</span> などのジオメトリ プロパティを含むディクショナリ。
  > オプションで、3D 点のリストを含むフィールド <span class="pre">`pt3d`</span> を含めることができます。各点は <span class="pre">`(x,y,z,diam)`</span> 形式のタプルとして定義されます。
  >
  > - **topol**: トポロジのプロパティを含むディクショナリ。
  > <span class="pre">`parentSec`</span> (親セクションのラベル)、<span class="pre">`parentX`</span> (接続を行う親の場所)、および <span class="pre">`childX`</span> (現在のセクション -子- 接続を行う場所) が含まれます。
  >
  > - **mechs**: 密度/分散メカニズムの辞書。
  > キーにはメカニズムの名前が含まれます (例: 「hh」または「pas」)。 値にはメカニズムのプロパティを含む辞書が含まれます (例: <span class="pre">`{'g':`</span>` `<span class="pre">`0.003,`</span>` `<span class="pre">`'e':`</span>` `<span class="pre">`-70}`</span>)。
  >
  > - **イオン**: イオンの辞書。
  > キーにはイオンの名前 (例: 「na」または「k」) が含まれます。 値には、特定のセクションのイオンのプロパティを含む辞書が含まれます (例: <span class="pre">`{'e':`</span>` `<span class="pre">`-70}`</span>)。利用可能なプロパティは、<span class="pre">`'e'`</span>: 逆転電位、<span class="pre">`'i'`</span>: そのセクションのイオンの内部濃度、および <span class="pre">`'o'`</span>: そのセクションのイオンの細胞外濃度です。
  >
  > - **pointps**: 点プロセスの辞書 (シナプス機構を除く)。
  > キーには任意のラベルが含まれます (例: 「Izhi」)。 値にはポイント プロセスのプロパティを含む辞書が含まれます (例: 「Izhi」)。 <span class="pre">`{'mod':'Izhi2007a',`</span>` `<span class="pre">`'a':0.03,`</span>` `<span class="pre">`'b':-2,`</span>` `<span class="pre">`'c':-50,`</span>` `<span class="pre">`'d':100,`</span>` `<span class="pre">`'celltype':1})`</span>。
  >
  > 内部ポイント プロセス変数とは別に、次のプロパティを各ポイント プロセスに指定できます。
  >
  > - <span class="pre">`mod`</span>、NEURON メカニズムの名前。 <span class="pre">`'Izhi2007a'`</span>
  >
  > - <span class="pre">`loc`</span>、シナプス機構を配置するセクションの位置。 <span class="pre">`1.0`</span>、デフォルト=0.5
  >
  > - <span class="pre">`vref`</span> (オプション)、細胞膜電圧を含む内部メカニズム変数。 <span class="pre">`'V'`</span>
  >
  > - <span class="pre">`synList`</span> (オプション)、内部メカニズムのシナプスメカニズムラベルのリスト。 \[「AMPA」、「NMDA」、「GABAB」\]
  >
  > - **vinit** - (オプション) セクションの初期膜電圧 (mV 単位) (デフォルト: -65)
  >
  > 例: <span class="pre">`cellRule['secs']['soma']['vinit']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`-72`</span>
  >
  > - **spikeGenLoc** - (オプション) このセクションが (デフォルトの「soma」の代わりに) スパイクの生成を担当することを示し、スパイクが生成される場所 (セグメント) を提供します。
  >
  > 例: <span class="pre">`cellRule['secs']['axon']['spikeGenLoc']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`1.0`</span>
  >
  > - **閾値** - (オプション) セルのこのセクションで発生するスパイクを検出するために使用される閾値電圧 (mV 単位)。省略した場合、デフォルトは <span class="pre">`netParams.defaultThreshold`</span>` `<span class="pre">`=`</span>` `<span class="pre">`10.0`</span>
  >
  > 例: <span class="pre">`cellRule['secs']['soma']['threshold']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`5.0`</span>
  >
  > </div>

- **secLists** - (オプション) セクション リストの辞書 (例: {‘all’: \[‘soma’, ‘dend’\]})

2 つの異なるセル タイプを追加する例:

<div class="highlight-default notranslate">

<div class="highlight">

    ## PYR_HH cell properties
    soma = {'geom': {}, 'mechs': {}}  # soma properties
    soma['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0, 'pt3d': []}
    soma['geom']['pt3d'].append((0, 0, 0, 20))
    soma['geom']['pt3d'].append((0, 0, 20, 20))
    soma['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}

    dend = {'geom': {}, 'topol': {}, 'mechs': {}}  # dend properties
    dend['geom'] = {'diam': 5.0, 'L': 150.0, 'Ra': 150.0, 'cm': 1}
    dend['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}
    dend['mechs']['pas'] = {'g': 0.0000357, 'e': -70}

    PYR_HH_dict = {'secs': {'soma': soma, 'dend': dend}}
    netParams.cellParams['PYR_HH'] = PYR_HH_dict  # add rule dict to list of cell property rules


    ## PYR_Izhi cell properties
    Izhi_dict = {'secs': {'soma': {} }}
    Izhi_dict['secs']['soma'] = {'geom': {}, 'pointps':{}}  # soma properties
    Izhi_dict['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}
    Izhi_dict['secs']['soma']['pointps']['Izhi'] = {'mod':'Izhi2007a', 'vref':'V', 'a':0.03, 'b':-2, 'c':-50, 'd':100, 'celltype':1}

    netParams.cellParams['PYR_Izhi'] = Izhi_dict  # add rule to list of cell property rules

</div>

</div>

<div class="admonition note">

注記

上記の例のように、一時的な変数/構造体 (<span class="pre">`soma`</span> や <span class="pre">`Izhi_dict`</span> など) を使用して、最終的な辞書 <span class="pre">`netParams.cellParams`</span> の作成を容易にすることができます。

</div>

<div class="admonition note">

注記

<span class="pre">`netParams.cellParams`</span> を介してセル パラメータを直接作成または変更できます。 <span class="pre">`netParams.cellParams['PYR_HH']['secs']['soma']['geom']['L']=16`</span>。

</div>

<div class="admonition seealso">

こちらも参照

セルのプロパティは外部ファイルからインポートできます。詳細と例については、<a href="user_documentation.html#importing-cells" class="reference internal"><span class="std std-ref">外部定義セル モデルのインポート</span></a>を参照してください。

</div>

</div>

<div id="population-parameters" class="section">

<span id="pop-params"></span>

### 母集団パラメータ<a href="#population-parameters" class="headerlink" title="Link to this heading"></a>

<span class="pre">`popParams`</span> 順序付き辞書の各項目は、キーと値で構成されます。キーは母集団の任意のラベルであり、タグ <span class="pre">`pop`</span> としてすべてのセルに割り当てられ、特定の接続ルールを適用するための条件として使用できます。

値は母集団のパラメータを含む辞書で構成され、次のフィールドが含まれます。

- **cellType** - この集団内のすべての細胞に使用される細胞タイプ。
  例えば「Pyr」（錐体ニューロン用）または「FS」（高速スパイク介在ニューロン用）

- **numCells**、**density**、または **gridSpacing** - この集団内の細胞の総数、ニューロン/mm3 単位の密度、または固定グリッド間隔 (3 つのうち 1 つだけが必要です)。
  各母集団が占める体積はカスタマイズできます (<span class="pre">`xRange`</span>、<span class="pre">`yRange`</span>、および <span class="pre">`zRange`</span> を参照)。それ以外の場合は、ネットワーク ボリューム全体が使用されます (<span class="pre">`netParams`</span> で定義: <span class="pre">`sizeX`</span>、<span class="pre">`sizeY`</span>、<span class="pre">`sizeZ`</span>)。

<span class="pre">`density`</span> は、文字列に変数と一般的な Python 算術演算子/関数を指定することで、正規化された位置の関数 (<span class="pre">`xnorm`</span>、<span class="pre">`ynorm`</span>、または <span class="pre">`znorm`</span>) として表現できます。例えば<span class="pre">`'1e5`</span>` `<span class="pre">`*`</span>` `<span class="pre">`exp(-ynorm/2)'`</span>。

<span class="pre">`gridSpacing`</span> はセル間の間隔 (μm) です。セルの総数は、間隔と <span class="pre">`sizeX`</span>、<span class="pre">`sizeY`</span>、<span class="pre">`sizeZ`</span> に基づいて決定されます。例えば<span class="pre">`10`</span>。

- **xRange** または **xnormRange** - x 軸のニューロン位置の範囲 (水平方向の長さ)、指定された 2 要素リスト \[min, max\]。
  um 単位の絶対値の場合は <span class="pre">`xRange`</span> (例: \[100,200\])、または <span class="pre">`sizeX`</span> の小数として 0 から 1 までの正規化された値の場合は <span class="pre">`xnormRange`</span> (例: \[0.1,0.2\])。

- **yRange** または **ynormRange** - y 軸のニューロン位置の範囲 (垂直高さ = 皮質深さ)、指定された 2 要素リスト \[min, max\]。
  um 単位の絶対値の場合は <span class="pre">`yRange`</span> (例: \[100,200\])、または <span class="pre">`sizeY`</span> の小数として 0 から 1 までの正規化された値の場合は <span class="pre">`ynormRange`</span> (例: \[0.1,0.2\])。注: NEURON オブジェクトの 3D ポイント (pt3d) <span class="pre">`y`</span> 座標は、Y 軸を深度座標として正しく使用して表すために、NetPyNE/Python <span class="pre">`tags.y`</span> 値と逆の符号を持ちます。 <span class="pre">`cell.tags.y`</span>` `<span class="pre">`=`</span>` `<span class="pre">`500`</span>の場合、<span class="pre">`cell.secs.soma.geom.pt3d[0][1]`</span>` `<span class="pre">`=`</span>` `<span class="pre">`-500`</span> (\[0\] は最初の pt3d を指し、\[1\] は y 座標を指します)

- **zRange** または **znormRange** - Z 軸 (水平方向の深さ) のニューロン位置の範囲、指定された 2 要素リスト \[min, max\]。
  um 単位の絶対値の場合は <span class="pre">`zRange`</span> (例: \[100,200\])、または <span class="pre">`sizeZ`</span> の小数として 0 から 1 までの正規化された値の場合は <span class="pre">`znormRange`</span> (例: \[0.1,0.2\])。

母集団を作成する例:

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.popParams['Sensory'] = {'cellType': 'PYR', 'ynormRange':[0.2, 0.5], 'density': 50000}

</div>

</div>

クラス <span class="pre">`netParams`</span> の <span class="pre">`addPopParams(label,`</span>` `<span class="pre">`params)`</span> メソッドを使用して、項目を <span class="pre">`popParams`</span> に追加できます。対話的に作業する場合、追加されたパラメーターの構文をチェックできるという利点があります。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.addPopParams('Sensory', {'cellType': 'PYR', 'ynormRange':[0.2, 0.5], 'density': 50000})

</div>

</div>

また、スパイク イベントを生成するがセクションを持たない人工細胞の集団、つまり点プロセスを作成することも可能です (例: NEURON オブジェクト: <span class="pre">`NetStim`</span>、<span class="pre">`VecStim`</span>、または <span class="pre">`IntFire2`</span>)。この場合、<span class="pre">`cellModel`</span> フィールドはポイント プロセス メカニズムの名前を指定し、メカニズムのプロパティは追加フィールドとして指定されます。人工セルはより単純であるため、<span class="pre">`netParams.cellParams`</span> 構造体で個別のセル パラメーターを定義する必要がないことに注意してください。たとえば、以下は NetStims (NEURON の人工スパイク ジェネレーター) の母集団を作成するために必要なフィールドです。

- **pop** - すべてのセルに割り当てられるこの集団の任意のラベル (例: 「バックグラウンド」)。特定の接続ルールを適用する条件として使用できます。

- **cellModel** - ポイント プロセス人工セルの名前 (例: <span class="pre">`IntFire2`</span>、<span class="pre">`NetStim`</span>、または <span class="pre">`VecStim`</span>)。

- **numCells** - セルの数

- **人工セルのパラメータ** - 各ポイントプロセス人工セルに固有 (例: <span class="pre">`IntFire2`</span> には「taum」、「taus」、「ib」が含まれます)

<span class="pre">`cellModel`</span> が「NetStim」または「VecStim」の場合、次のパラメータが許可されます。

- **間隔** - スパイク間隔（ミリ秒）

- **rate** - 発火速度 (Hz) (これは NetStim 間隔プロパティの逆数であることに注意してください)

- **ノイズ** - NetStim のノイズの割合 (0 = 決定的; 1 = 完全にランダム)

- **start** - 最初のスパイクの時間 (ミリ秒) (デフォルト = 0)

- **数値** - 生成されるスパイクの最大数 (デフォルト = 1e12)

- **シード** - ランダマイザーのシード (オプション; デフォルトは <span class="pre">`simConfig.seeds['stim']`</span> に設定された値)

- **spkTimes** (「VecStim」のみ) - スパイク時間のリスト (例: \[1, 10, 40, 50\]、range(1,500,10)、または Python リストを含む変数)

- **パルス** (「VecStim」のみ) - スパイクパルスのリスト。各項目には、<span class="pre">`start`</span> (ms)、<span class="pre">`end`</span> (ms)、<span class="pre">`rate`</span> (Hz)、および <span class="pre">`noise`</span> (0 ～ 1) のパルス パラメーターが含まれます。以下の例を参照してください。

点プロセス人工細胞集団の例:

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.popParams['artif1'] = {'cellModel': 'IntFire2', 'taum': 100, 'noise': 0.5, 'numCells': 100}  # Intfire2

    netParams.popParams['artif2'] = {'cellModel': 'NetStim', 'rate': 100, 'noise': 0.5, 'numCells': 100}  # NetsStim

    # create custom list of spike times
    spkTimes = range(0,1000,20) + [138, 155,270]

    # create list of pulses (each item is a dict with pulse params)
    pulses = [{'start': 10, 'end': 100, 'rate': 200, 'noise': 0.5},
            {'start': 400, 'end': 500, 'rate': 1, 'noise': 0.0})]

    netParams.popParams['artif3'] = {'cellModel': 'VecStim', 'numCells': 100, 'spkTimes': spkTimes, 'pulses': pulses}  # VecStim with spike times

</div>

</div>

最後に、<span class="pre">`cellsList`</span> 辞書フィールドにセルのリストを含めることによって、個別に定義されたセルで構成される集団を定義できます。セルのリストの各要素は、<span class="pre">`cellLabel`</span> や場所 (<span class="pre">`x`</span> や <span class="pre">`ynorm`</span> など) などのセル プロパティのセットを含む辞書になります。以下に例を示します。

<div class="highlight-default notranslate">

<div class="highlight">

    cellsList.append({'cellLabel':'gs15', 'x': 1, 'ynorm': 0.4 , 'z': 2})
    cellsList.append({'cellLabel':'gs21', 'x': 2, 'ynorm': 0.5 , 'z': 3})
    netParams.popParams['IT_cells'] = {'cellType':'IT', 'cellsList': cellsList} #  IT individual cells

</div>

</div>

<div class="admonition note">

注記

VecStim を使用するには、 <a href="https://raw.githubusercontent.com/Neurosim-lab/netpyne/development/doc/source/code/mod/vecevent.mod" class="reference external">vecevent.mod ファイル</a> をダウンロードしてコンパイル (nrnivmodl) する必要があります。

</div>

</div>

<div id="synaptic-mechanisms-parameters" class="section">

### シナプス機構パラメータ<a href="#synaptic-mechanisms-parameters" class="headerlink" title="Link to this heading"></a>

シナプス メカニズムのパラメーターを定義するには、<span class="pre">`synMechParams`</span> 順序付き辞書に項目を追加します。 addSynMechParams(label,params) メソッドを使用できます。各 <span class="pre">`synMechParams`</span> 項目はキーと値で構成されます。キーはこのメカニズムの任意のラベルであり、接続ルールで参照するために使用されます。値は、次のフィールドを含むシナプス メカニズム パラメーターの辞書です。

- <span class="pre">`mod`</span> - NMODL メカニズム名 (例: 「ExpSyn」)。これは MOD ファイルの名前と必ずしも一致しないことに注意してください。

- メカニズムパラメータ (<span class="pre">`tau`</span> または <span class="pre">`e`</span> など) - これらは特定の NMODL メカニズムに依存します。

- <span class="pre">`selfNetCon`</span> (オプション) - 恒常性シナプス (hsyn) などの一部のシナプス メカニズムで必要な、セル電圧とシナプスの間の NetCon パラメーターを含む辞書。例えば<span class="pre">`'selfNetCon':`</span>` `<span class="pre">`{'sec':`</span>` `<span class="pre">`'soma'`</span>` `<span class="pre">`,`</span>` `<span class="pre">`'threshold':`</span>` `<span class="pre">`-15,`</span>` `<span class="pre">`'weight':`</span>` `<span class="pre">`-1,`</span>` `<span class="pre">`'delay':`</span>` `<span class="pre">`0}`</span> (デフォルトでは、ソースセクションはソーマに設定されています。例: <span class="pre">`'sec':`</span>` `<span class="pre">`'soma'`</span>)

シナプス機構は、接続フェーズ中に必要に応じて細胞に追加されます。各接続ルールは、適切なラベルを参照することによって、どのシナプス メカニズム パラメーターを使用するかを指定します。

以下は、<span class="pre">`NMDA`</span> というラベルが付いた単純な興奮性シナプス機構のシナプス機構パラメーターの例です。<span class="pre">`Exp2Syn`</span> モデルを使用して実装され、立ち上がり時間 (<span class="pre">`tau1`</span>) が 0.1 ミリ秒、減衰時間 (<span class="pre">`tau2`</span>) が 5 ミリ秒、平衡電位が設定されています。 (<span class="pre">`e`</span>) 0mV:

<div class="highlight-python notranslate">

<div class="highlight">

    ## Synaptic mechanism parameters
    netParams.synMechParams['NMDA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0}  # NMDA synaptic mechanism

</div>

</div>

</div>

<div id="connectivity-rules" class="section">

### 接続ルール<a href="#connectivity-rules" class="headerlink" title="Link to this heading"></a>

接続ルールを使用する理論的根拠は、特定の基準に一致するニューロンのサブセット間に接続を作成できることです。特定の細胞型のシナプス前ニューロン、および特定の集団および/または特定の範囲の位置内のシナプス後ニューロンのみ。

<span class="pre">`connParams`</span> 順序付き辞書の各項目は、キーと値で構成されます。キーは、この接続ルールの参照として使用される任意のラベルです。値には、接続ルールのパラメーターを定義するディクショナリが含まれており、次のフィールドが含まれます。

- **preConds** - シナプス前細胞の条件セット
  シナプス前細胞の属性/タグと必要な値を含む辞書として定義されます。 <span class="pre">`{'cellType':`</span>` `<span class="pre">`'PYR'}`</span>。

値はリストにすることができます。 <span class="pre">`{'pop':`</span>` `<span class="pre">`['Exc1',`</span>` `<span class="pre">`'Exc2']}`</span>。位置プロパティの場合、リストの値は最小値と最大値に対応します。 <span class="pre">`{'ynorm':`</span>` `<span class="pre">`[0.1,`</span>` `<span class="pre">`0.6]}`</span>。

- **postConds** - シナプス後細胞の条件セット
  <span class="pre">`preConds`</span> (上記) と同じ形式。

- **sec** (オプション) - シナプス後ニューロンのターゲット セクションの名前 (例: <span class="pre">`'soma'`</span>)
  省略した場合、デフォルトで「soma」が存在する場合は「soma」が使用され、存在しない場合はセルセクションリストの最初のセクションが使用されます。

<span class="pre">`synsPerConn`</span> \> 1 で、セクションのリストまたはセクションリストが指定されている場合、シナプスは各セクションの長さを考慮して、指定されたセクションに沿って均一に分散されます。

<span class="pre">`synsPerConn`</span> == 1 で、セクションのリストまたはセクションリストが指定されている場合、シナプス (シナプス前セルごとに 1 つ) がリストからランダムに選択されたセクションに配置されます。リストの最初のセクションを常に使用するようにするには、<span class="pre">`cfg.connRandomSecFromList`</span>` `<span class="pre">`=`</span>` `<span class="pre">`False`</span> を設定します。

- **loc** (オプション) - ターゲット シナプス メカニズムの位置 (例: <span class="pre">`0.3`</span>)
  省略した場合、デフォルトは 0.5 になります。

<span class="pre">`synMechs`</span> のリストがある場合は、すべてに対して 1 つの loc を作成するか、または loc のリスト (synMech ごとに 1 つ、たとえば 2 つの synMech の場合: <span class="pre">`[0.4,`</span>` `<span class="pre">`0.7]`</span>) を作成できます。

<span class="pre">`synsPerConn`</span> \> 1 の場合、すべてに対して 1 つの loc を指定するか、または loc のリスト (シナプスごとに 1 つ、たとえば <span class="pre">`synsPerConn`</span> = 3 の場合) を指定できます。 <span class="pre">`[0.4,`</span>` `<span class="pre">`0.5,`</span>` `<span class="pre">`0.7]`</span>)

<span class="pre">`synMechs`</span> と <span class="pre">`synsPerConn`</span> \> 1 の両方のリストがある場合、各 synMech の各シナプスの 2D リストを持つことができます (たとえば、2 つの synMech と <span class="pre">`synsPerConn`</span> = 3 の場合)。 <span class="pre">`[[0.2,`</span>` `<span class="pre">`0.3,`</span>` `<span class="pre">`0.5],`</span>` `<span class="pre">`[0.5,`</span>` `<span class="pre">`0.6,`</span>` `<span class="pre">`0.7]]`</span>)

<span class="pre">`synsPerConn`</span> == 1 で、[<span id="id3" class="problematic">\`\`</span>](#id2)loc\`\`s のリストが指定されている場合、シナプス (シナプス前セルごとに 1 つ) がリストからランダムに選択された位置に配置されます (ランダムなセクションと位置は連動することに注意してください。つまり、両方に同じランダム インデックスが使用されます)。

- **synMech** (オプション) - シナプス後ニューロン上のターゲット シナプス メカニズムのラベル (またはラベルのリスト) (例: <span class="pre">`'AMPA'`</span> または <span class="pre">`['AMPA',`</span>` `<span class="pre">`'NMDA']`</span>)

> <div>
  >
  > 省略した場合、セルのシナプス機構リストの最初のシナプス機構が使用されます。
  >
  > リストがある場合は、各 synMech に対して個別の接続が作成されます。また、重み、遅延、位置のリストを提供することもできます。
  >
  > </div>

- **synsPerConn** (オプション) - セル間接続 (*connection*) ごとの個々のシナプス接続 (*synapses*) の数

> <div>
  >
  > 関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > 省略した場合、デフォルトは 1 になります。
  >
  > 各シナプスの重み、遅延、位置、あるいはその両方をリストとして指定することも、単一の値をすべてに使用することもできます。
  >
  > <span class="pre">`synsPerConn`</span> \> 1 で単一セクションを指定すると、<span class="pre">`loc`</span> でシナプスの位置をリストとして指定できます。
  >
  > <span class="pre">`synsPerConn`</span> \> 1 の場合、<span class="pre">`loc`</span> が単一の値か省略された場合、またはターゲット セクションのリストが指定されている場合、シナプスは各セクションの長さを考慮して、指定されたセクションに沿って均一に分散されます。
  >
  > </div>

- **重量** (オプション) - シナプス接続の強度 (例: <span class="pre">`0.01`</span>)
  コンダクタンスの変化に関連しますが、シナプス機構と細胞モデルに応じて意味と規模が異なります。

関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。

省略した場合、デフォルトは <span class="pre">`netParams.defaultWeight`</span>` `<span class="pre">`=`</span>` `<span class="pre">`1`</span> になります。

<span class="pre">`synMechs`</span> のリストがある場合は、すべての重みを 1 つ持つことも、重みのリスト (synMech ごとに 1 つ、たとえば 2 つの synMech の場合: <span class="pre">`[0.1,`</span>` `<span class="pre">`0.01]`</span>) を持つこともできます。

<span class="pre">`synsPerConn`</span> \> 1 の場合、すべてに対して単一の重みを指定することも、重みのリストを指定することもできます (シナプスごとに 1 つ、たとえば、<span class="pre">`synsPerConn`</span> = 3 の場合: <span class="pre">`[0.2,`</span>` `<span class="pre">`0.3,`</span>` `<span class="pre">`0.4]`</span>)。

<span class="pre">`synMechs`</span> と <span class="pre">`synsPerConn`</span> \> 1 の両方のリストがある場合、各 synMech の各シナプスの 2D リストを持つことができます (たとえば、2 つの synMech と <span class="pre">`synsPerConn`</span> = 3 の場合)。 <span class="pre">`[[0.2,`</span>` `<span class="pre">`0.3,`</span>` `<span class="pre">`0.4],`</span>` `<span class="pre">`[0.02,`</span>` `<span class="pre">`0.04,`</span>` `<span class="pre">`0.03]]`</span>)

- **遅延** (オプション) - シナプス前スパイクがシナプス後ニューロンに到達するまでの時間 (ミリ秒)
  関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)

省略した場合、デフォルトは <span class="pre">`netParams.defaultDelay`</span>` `<span class="pre">`=`</span>` `<span class="pre">`1`</span> になります。

<span class="pre">`synMechs`</span> のリストがある場合は、すべてに対して 1 つの遅延を設定することも、遅延のリスト (synMech ごとに 1 つ、たとえば 2 つの synMech の場合: <span class="pre">`[5,`</span>` `<span class="pre">`7]`</span>) を設定することもできます。

<span class="pre">`synsPerConn`</span> \> 1 の場合、すべてに対して 1 つの重みを使用することも、重みのリスト (シナプスごとに 1 つ、たとえば <span class="pre">`synsPerConn`</span> = 3 の場合) を使用することもできます。 <span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6]`</span>)。

<span class="pre">`synMechs`</span> と <span class="pre">`synsPerConn`</span> \> 1 の両方のリストがある場合、各 synMech の各シナプスの 2D リストを持つことができます (たとえば、2 つの synMech と <span class="pre">`synsPerConn`</span> = 3 の場合)。 <span class="pre">`[[4,`</span>` `<span class="pre">`6,`</span>` `<span class="pre">`5],`</span>` `<span class="pre">`[9,`</span>` `<span class="pre">`10,`</span>` `<span class="pre">`11]]`</span>）。

- **しきい値** (非推奨、使用しないでください)

> <div>
  >
  > ソース セルのしきい値 (mV 単位) を設定するには、<span class="pre">`cellParams`</span> のセル ルールのセクション内で <span class="pre">`threshold`</span> パラメータを使用するか、デフォルト値を設定します (例: <span class="pre">`netParams.defaultThreshold`</span>` `<span class="pre">`=`</span>` `<span class="pre">`10.0`</span>)。
  >
  > </div>

- **確率** (オプション) - 各シナプス前セルと後セル間の接続の確率 (0 ～ 1)

> <div>
  >
  > 関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > <span class="pre">`connFunc`</span> を <span class="pre">`probConn`</span> に設定します (内部確率的接続関数)。
  >
  > <span class="pre">`convergence`</span>、<span class="pre">`divergence`</span>、および <span class="pre">`fromList`</span> パラメータをオーバーライドします。
  >
  > </div>

- **収束** (オプション) - 各シナプス後セルに接続されているシナプス前セルの数

> <div>
  >
  > 関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > <span class="pre">`connFunc`</span> を <span class="pre">`convConn`</span> に設定します (内部コンバージェンス接続機能)。
  >
  > <span class="pre">`divergence`</span> および <span class="pre">`fromList`</span> パラメータをオーバーライドします。 <span class="pre">`probability`</span> パラメータが含まれている場合は効果がありません。
  >
  > </div>

- **発散** (オプション) - 各シナプス前セルに接続されているシナプス後セルの数

> <div>
  >
  > 関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > <span class="pre">`connFunc`</span> を <span class="pre">`divConn`</span> に設定します (内部分岐接続機能)。
  >
  > <span class="pre">`fromList`</span> パラメータをオーバーライドします。 <span class="pre">`probability`</span> または <span class="pre">`convergence`</span> パラメーターが含まれている場合、効果はありません。
  >
  > </div>

- **connList** (オプション) - 個々のシナプス前セルとシナプス後セル間の接続の明示的なリスト

> <div>
  >
  > 各接続は、前集団と後集団のセルの相対 ID で示されます。 <span class="pre">`[[0,1],[3,1]]`</span> は、前セル 0 と後セル 1、前セル 3 と後セル 1 の間の接続を作成します。
  >
  > 重み、遅延、および位置は、個々のセル接続ごとにリストとして指定することもできます。これらのリストは、複数の synMech および synsPerConn \> 1 と組み合わせると 2D または 3D になります (外側の次元は connList に対応します)。
  >
  > <span class="pre">`connFunc`</span> を <span class="pre">`fromList`</span> に設定します (明示的リスト接続機能)。
  >
  > <span class="pre">`probability`</span>、<span class="pre">`convergence`</span>、または <span class="pre">`divergence`</span> パラメータが含まれている場合は効果がありません。
  >
  > </div>

- **connFunc** (オプション) - 使用する内部接続関数

> <div>
  >
  > <span class="pre">`probability`</span>、<span class="pre">`convergence`</span>、<span class="pre">`divergence`</span>、または <span class="pre">`connList`</span> パラメーターが含まれる場合、それぞれ <span class="pre">`probConn`</span>、<span class="pre">`convConn`</span>、<span class="pre">`divConn`</span>、または <span class="pre">`fromList`</span> に自動的に設定されます。それ以外の場合は、デフォルトで <span class="pre">`fullConn`</span>、つまり全対全接続になります。
  >
  > ユーザー定義の接続機能を追加できます。
  >
  > </div>

- **shape** (オプション) - 指定されたパターンに基づいて、シミュレーション中に接続の重みを動的に変更します。

> <div>
  >
  > 次のフィールドを含む辞書が含まれています。
  >
  > > <div>
  > >
  > > <span class="pre">`'switchOnOff'`</span> - 体重のオンとオフを切り替える時間
  > >
  > > <span class="pre">`'pulseType'`</span> - 生成するパルスのタイプ。 「平方」または「ガウス」のいずれか
  > >
  > > <span class="pre">`'pulsePeriod'`</span> - パルスの周期 (ミリ秒単位)
  > >
  > > <span class="pre">`'pulseWidth'`</span> - パルスの幅 (ミリ秒単位)
  > >
  > > </div>
  >
  > 振動や特定の時間にオン/オフする複雑な刺激パターンを生成するために使用できます。
  >
  > 例: <span class="pre">`'shape':`</span>` `<span class="pre">`{'switchOnOff':`</span>` `<span class="pre">`[200,`</span>` `<span class="pre">`800],`</span>` `<span class="pre">`'pulseType':`</span>` `<span class="pre">`'square',`</span>` `<span class="pre">`'pulsePeriod':`</span>` `<span class="pre">`100,`</span>` `<span class="pre">`'pulseWidth':`</span>` `<span class="pre">`50}`</span>
  >
  > </div>

- **可塑性** (オプション) - この接続に使用する可塑性メカニズム

> <div>
  >
  > 2 つのフィールドが必要です。塑性メカニズムの名前を指定する <span class="pre">`mech`</span> と、メカニズムのパラメーターを含む辞書を含む <span class="pre">`params`</span> です。
  >
  > 例: <span class="pre">`{'mech':`</span>` `<span class="pre">`'STDP',`</span>` `<span class="pre">`'params':`</span>` `<span class="pre">`{'hebbwt':`</span>` `<span class="pre">`0.01,`</span>` `<span class="pre">`'antiwt':-0.01,`</span>` `<span class="pre">`'wmax':`</span>` `<span class="pre">`50,`</span>` `<span class="pre">`'RLon':`</span>` `<span class="pre">`1`</span>` `<span class="pre">`'tauhebb':`</span>` `<span class="pre">`10}}`</span>
  >
  > </div>

接続ルールの例を次に示します。

<div class="highlight-python notranslate">

<div class="highlight">

    ## Cell connectivity rules
    netParams.connParams['S->M'] = {    #  S -> M
            'preConds': {'pop': 'S'},
            'postConds': {'pop': 'M'},
            'sec': 'dend',                  # target postsyn section
            'synMech': 'AMPA',              # target synaptic mechanism
            'weight': 0.01,                 # synaptic weight
            'delay': 5,                     # transmission delay (ms)
            'probability': 0.5}             # probability of connection

    netParams.connParams['bg->all'] = {      # background -> S,M in ynorm range
            'preConds': {'pop': 'background'},
            'postConds': {'cellType': ['S','M'],
                                      'ynorm': [0.1, 0.6]},
            'synReceptor': 'AMPA',               # target synaptic mechanism
            'weight': 0.01,                      # synaptic weight
            'delay': 5}                          # transmission delay (ms)

    netParams.connParams['yrange->HH'] = {            # cells with y in range 100 to 600 -> HH cells
        'preConds': {'y': [100, 600]},
        'postConds': {'cellType': 'HH'},
        'synMech': ['AMPA', 'NMDA'],                  # target synaptic mechanisms
        'synsPerConn': 3,                             # number of synapses per cell connection (per synMech, ie. total syns = 2 x 3)
        'weight': 0.02,                               # single weight for all synapses
        'delay': [5, 10],                             # different delays for each of 3 synapses per synMech
        'loc': [[0.1, 0.5, 0.7], [0.3, 0.4, 0.5]]}    # different locations for each of the 6 synapses

</div>

</div>

</div>

<div id="functions-as-strings" class="section">

<span id="function-string"></span>

### 文字列としての機能<a href="#functions-as-strings" class="headerlink" title="Link to this heading"></a>

一部のパラメーター (<span class="pre">`weight`</span>、<span class="pre">`delay`</span>、<span class="pre">`probability`</span>、<span class="pre">`convergence`</span>、および <span class="pre">`divergence`</span>) は、関数を含む文字列を使用して指定できます。文字列は NetPyNE によって内部的に解釈され、適切な <a href="https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions" class="reference external">lambda 関数 </a> に変換されます。この文字列には次の要素が含まれる場合があります。

- 数値、例: 「3.56」

- すべての Python 数学演算子: <span class="pre">`+`</span>、<span class="pre">`-`</span>、<span class="pre">`*`</span>、<span class="pre">`/`</span>、<span class="pre">`%`</span>、<span class="pre">`**`</span> (指数) など。

- Python 数学関数: <span class="pre">`sin`</span>、<span class="pre">`cos`</span>、<span class="pre">`tan`</span>、<span class="pre">`exp`</span>、<span class="pre">`sqrt`</span>、<span class="pre">`mean`</span>、<span class="pre">`inf`</span> (詳細については、<a href="https://docs.python.org/2/library/math.html" class="reference external">https://docs.python.org/2/library/math.html</a> を参照)

- NEURON h.Random() メソッド: <span class="pre">`binomial`</span>、<span class="pre">`discunif`</span>、<span class="pre">`erlang`</span>、<span class="pre">`geometric`</span>、<span class="pre">`hypergeo`</span>、<span class="pre">`lognormal`</span>、<span class="pre">`negexp`</span>、<span class="pre">`normal`</span>、 <span class="pre">`poisson`</span>、<span class="pre">`uniform`</span>、<span class="pre">`weibull`</span> (<a href="https://www.neuron.yale.edu/neuron/static/py_doc/programming/math/random.html" class="reference external">https://www.neuron.yale.edu/neuron/static/py_doc/programming/math/random.html</a> を参照)

- セル位置変数:

> <div>
  >
  > - <span class="pre">`pre_x`</span>、<span class="pre">`pre_y`</span>、<span class="pre">`pre_z`</span>: シナプス前細胞の x、y、または z の位置。
  >
  > - <span class="pre">`pre_ynorm`</span>、<span class="pre">`pre_ynorm`</span>、<span class="pre">`pre_znorm`</span>: 正規化されたシナプス前細胞の x、y、または z の位置。
  >
  > - <span class="pre">`post_x`</span>、<span class="pre">`post_y`</span>、<span class="pre">`post_z`</span>: シナプス後細胞の x、y、または z の位置。
  >
  > - <span class="pre">`post_xnorm`</span>、<span class="pre">`post_ynorm`</span>、<span class="pre">`post_znorm`</span>: 正規化されたシナプス後セルの x、y、または z の位置。
  >
  > - <span class="pre">`dist_x`</span>、<span class="pre">`dist_y`</span>、<span class="pre">`dist_z`</span>: シナプス前細胞とシナプス後細胞の x、y、または z 位置間の絶対ユークリッド距離。
  >
  > - <span class="pre">`dist_xnorm`</span>、<span class="pre">`dist_ynorm`</span>、<span class="pre">`dist_znorm`</span>: 正規化されたシナプス前細胞とシナプス後細胞の x、y、または z 位置間の絶対ユークリッド距離。
  >
  > - <span class="pre">`dist_2D`</span>、<span class="pre">`dist_3D`</span>: シナプス前細胞とシナプス後細胞間の絶対ユークリッド 2D (x および z) または 3D (x、y および z) 距離。
  >
  > - <span class="pre">`dist_norm2D`</span>、<span class="pre">`dist_norm3D`</span>: 正規化されたシナプス前細胞とシナプス後細胞間の絶対ユークリッド 2D (x および z) または 3D (x、y および z) 距離。
  >
  > </div>

- <span class="pre">`netParams`</span> ディクショナリで定義された単一値の数値ネットワーク パラメーター。既存のものをカスタマイズしたり、新たに任意のものを追加したりできます。デフォルトでは、次のパラメータが使用可能です。

> <div>
  >
  > - <span class="pre">`sizeX`</span>、<span class="pre">`sizeY`</span>、<span class="pre">`sizeZ`</span>: ネットワーク サイズ (μm) (デフォルト: 100)
  >
  > - <span class="pre">`defaultWeight`</span>: デフォルトの接続重み (デフォルト: 1)
  >
  > - <span class="pre">`defaultDelay`</span>: デフォルトの接続遅延 (ミリ秒単位) (デフォルト: 1)
  >
  > - <span class="pre">`propVelocity`</span>: 伝導速度 (um/ms) (デフォルト: 500)
  >
  > </div>

文字列ベースの関数は、NetPyNE 接続ルールに優れた柔軟性と機能を追加します。これらにより、ユーザーは、皮質深さに依存する接続確率や距離に依存する接続重みなど、さまざまな接続機能を定義できます。以下にいくつかの具体的な例を示します。

- 収束 (シナプス後細胞をターゲットとするシナプス前細胞の数) は 1 ～ 15 の間で均一に分布します。

> <div>
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > netParams.connParams[...] = {
  > '収束': 'uniform(1, 15)',
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

- 接続遅延を最小値 0.2 に平均 13.0、分散 1.4 のガウス分布値を加えた値に設定します。

> <div>
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > netParams.connParams[...] = {
  > '遅延': '0.2 + 通常(13.0, 1.4)',
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

- 上記と同じですが、<span class="pre">`netParams`</span> 辞書で定義された変数を使用します。

> <div>
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > netParams['遅延最小'] = 0.2
  > netParams['遅延平均'] = 13.0
  > netParams['遅延変数'] = 1.4
  >
  > # ...
  >
  > netParams.connParams[...] = {
  > '遅延': '遅延最小値 + 通常(遅延平均, 遅延変数)',
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

- 接続遅延を <span class="pre">`defaultDelay`</span> の最小値に伝播速度に基づく 3D 距離依存の遅延を加えたものに設定 (<span class="pre">`propVelocity`</span>):

> <div>
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > netParams.connParams[...] = {
  > '遅延': 'defaultDelay + dist_3D/propVelocity',
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

- 接続の確率はシナプス後ニューロンの皮質深さに依存します:

> <div>
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > netParams.connParams[...] = {
  > '確率': '0.1 + 0.2*post_y',
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

- netParams の属性として定義された長さ定数 (<span class="pre">`lengthConst`</span>) を使用して、2D 距離の関数として指数関数的に減衰する接続の確率:

> <div>
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > netParams.lengthConst = 200
  >
  > # ...
  >
  > netParams.connParams[...] = {
  > '確率': 'exp(-dist_2D/lengthConst)',
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

</div>

<div id="sub-cellular-connectivity-rules-redistribution-of-synapses" class="section">

### 細胞内接続ルール - シナプスの再分配<a href="#sub-cellular-connectivity-rules-redistribution-of-synapses" class="headerlink" title="Link to this heading"></a>

<span class="pre">`connParams`</span> 順序付き辞書を介して接続が定義されると、樹状ツリーに沿った特定のプロファイルに従ってシナプスを再分布することが必要になる場合があります。この目的のために、<span class="pre">`subConnParams`</span> 順序付き辞書は、この再配布を管理するルールとパラメータを設定します。このディクショナリ内の各項目は、キーと値で構成されます。キーは、この再配布ルールの参照として使用されるラベルです。値は、このプロセスのパラメータを設定する辞書であり、次のフィールドが含まれます。

- **preConds / postConds** - シナプス前セルとシナプス後セルの条件セット

> <div>
  >
  > <span class="pre">`connParams`</span> 仕様と同様、これらのフィールドは、シナプス前側とシナプス後側で特定の条件を満たす、すでに確立されている接続を選択するための属性/タグを提供します。これらは、適切な属性/タグと必要な値を含む辞書として定義されます。 {‘cellType’: ‘PYR’}、{‘pop’: \[‘Exc1’, ‘Exc2’\]}、{‘ynorm’: \[0.1, 0.6\]}。
  >
  > </div>

- **groupSynMechs (オプション)** – シナプスを再分配するときにグループ化されたシナプス メカニズムのリスト

> <div>
  >
  > 省略した場合、すべての接続のシナプス後の位置 (preConds と postConds を満たす) は、指定されたプロファイル (以下で定義) を使用して独立して再分配されます。リストが提供される場合、共通接続のシナプス (各メカニズムの同じシナプス前およびシナプス後ニューロン) が同じ場所に再配置されます。たとえば、\['AMPA','NMDA'\]。
  >
  > </div>

- **sec (オプション)** – 再分散シナプスを許可するセクションのリスト

> <div>
  >
  > 省略した場合、シナプスの再分配に使用されるセクションは体細胞、または存在しない場合はシナプス後細胞の最初に利用可能なセクションです。たとえば、\['Adend1','Adend2', 'Adend3','Bdend'\] のようになります。
  >
  > </div>

- **密度** - 再配布のタイプ。事前定義されたルールが多数あります。

> <div>
  >
  > - <span class="pre">`uniform`</span> - 条件を満たす各接続は、長さに応じて重み付けされ、指定されたセクションに沿って均一に再配分されます。
  >
  > - さまざまなオプションを持つ辞書:
  >
  > > <div>
  > >
  > > - <span class="pre">`type`</span> - シナプス密度マップのタイプ。利用可能なオプション: 1Dmap または 2Dmap。
  > >
  > > さらに、以下を含める必要があります。
  > >
  > > > <div>
  > > >
  > > > - <span class="pre">`gridY`</span> – y 座標 (深さ) の位置のリスト
  > > >
  > > > - <span class="pre">`gridX`</span> (2Dmap のみ) - x 座標 (または z) の位置のリスト。
  > > >
  > > > - <span class="pre">`fixedSomaY`</span> (オプション) - ソーマの絶対位置 y 座標。gridY をシフトするために使用されます (絶対座標でも提供されます)。
  > > >
  > > > - <span class="pre">`gridValues`</span> – (gridX および) GridY によって定義された座標の (相対) シナプス密度を表す 1 次元または 2 次元のリスト。
  > > >
  > > > </div>
  > >
  > > たとえば、
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.subConnParams[...] = {'type':'1Dmap','gridY': [0,-200,-400,-600,-800], 'fixedSomaY':-700,'gridValues':[0,0.2,0.7,1.0,0]}。
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > 一方、この選択のためには、シナプス後細胞が 3D 形態を持つ必要があります。単純なセクションの場合、<span class="pre">`netParams.defineCellShapes`</span>` `<span class="pre">`=`</span>` `<span class="pre">`True`</span> を設定することにより、これを自動的に生成できます (Y 軸に沿った円柱が上向き)。
  > >
  > > - <span class="pre">`distance`</span> - シナプスは参照から指定された距離 (許可されたセクション内) に再配置されました。
  > >
  > > さらに、次のものが含まれる場合があります。
  > >
  > > > <div>
  > > >
  > > > - <span class="pre">`ref_sec`</span> (オプション) – 文字列
  > > >
  > > > > <div>
  > > > >
  > > > > 距離を計算する基準となるセクション。省略した場合、距離の参照に使用されるセクションはソーマ、またはソーマが存在しない場合は「som」で始まるもの、それ以外の場合はシナプス後セルで最初に使用可能なセクションになります。
  > > > >
  > > > > </div>
  > > >
  > > > - <span class="pre">`ref_seg`</span> (オプション) - 数値
  > > >
  > > > > <div>
  > > > >
  > > > > 距離の参照に使用されるセクション内のセグメント。省略した場合はデフォルト値(0.5)が使用されます。
  > > > >
  > > > > </div>
  > > >
  > > > - <span class="pre">`target_distance`</span> (オプション) - シナプスが再割り当てされるリファレンスからのターゲット距離
  > > >
  > > > > <div>
  > > > >
  > > > > 省略した場合、この値は 0 に設定されます。選択された場所は、許可されたセクションの間で、このターゲットに最も近い場所になります。
  > > > >
  > > > > </div>
  > > >
  > > > - <span class="pre">`coord`</span> (オプション) - 距離の計算に使用される座標系。省略した場合 (または「topol」に設定した場合)、距離は樹状木に沿って計算されます。あるいは、ユークリッド空間内の距離 (デカルト座標系における基準からターゲット セグメントまでの距離) を計算するために「デカルト」を使用することもできます。この場合、シナプス後細胞は 3D 形態を持つ必要があります (または <span class="pre">`netParams.defineCellShapes`</span>` `<span class="pre">`=`</span>` `<span class="pre">`True`</span> を設定)。
  > > >
  > > > </div>
  > >
  > > たとえば、
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.subConnParams[...] = {'type':' distance','ref_sec': 'soma', 'ref_seg': 1,'target_ distance': 500}。
  > >
  > > </div>
  > >
  > > </div>
  > >> > </div>
  >
  > </div>

</div>

<div id="stimulation-parameters" class="section">

<span id="stimulation"></span>

### 刺激パラメータ<a href="#stimulation-parameters" class="headerlink" title="Link to this heading"></a>

2 つのデータ構造を使用して細胞刺激パラメータを指定します。<span class="pre">`stimSourceParams`</span> は刺激源のパラメータを定義します。 <span class="pre">`stimTargetParams`</span> は、どの細胞にどの刺激源を適用するかを指定します (刺激源のセルへのマッピング)。

<span class="pre">`stimSourceParams`</span> 順序付き辞書の各項目はキーと値で構成されます。ここで、キーはこの刺激源を参照するための任意のラベル (例: 「electrode_current」)、値はソース パラメータの辞書です。

> <div>
>
> - **タイプ** - 刺激装置として使用されるポイントプロセス。許可される値: <span class="pre">`'IClamp'`</span>、<span class="pre">`'VClamp'`</span>、<span class="pre">`'SEClamp'`</span>、<span class="pre">`'NetStim'`</span>、および <span class="pre">`'AlphaSynapse'`</span>。
>
> > <div>
> >
> > NetStims は、この方法を使用するか、「cellModel」: 「NetStim」の母集団を作成して適切な接続を追加することによって追加できることに注意してください。
> >
> > </div>
>
> - **stim params** (オプション) - これらはスティミュレーターのタイプによって異なります (たとえば、<span class="pre">`'IClamp'`</span> の場合は、<span class="pre">`'del'`</span>、<span class="pre">`'dur'`</span>、および <span class="pre">`'amp'`</span> になります)
>
> > <div>
> >
> > 関数として定義できます (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a> を参照)。刺激の場合は、シナプス後細胞のパラメーターを使用することのみが意味があることに注意してください (例: <span class="pre">`'post_ynorm'`</span>)。
> >
> > </div>
>
> </div>

<span class="pre">`stimTargetParams`</span> の各項目は、ネットワーク内のセルのサブセットに刺激源をマッピングする方法を指定します。キーはこのマッピングの任意のラベルであり、値は次のパラメータを含む辞書です。

> <div>
>
> - **ソース** - 刺激ソースのラベル (例: <span class="pre">`'electrode_current'`</span>)。
>
> - **条件** - スティムが適用されるセルの条件を含む辞書。
> 選択したセルのサブセット内の相対セル インデックスを含むフィールド <span class="pre">`'cellList'`</span> を含めることができます (例: <span class="pre">`'conds':`</span>` `<span class="pre">`{'cellType':'PYR',`</span>` `<span class="pre">`'y':[100,`</span>` `<span class="pre">`200],`</span>` `<span class="pre">`'cellList':`</span>` `<span class="pre">`[1,`</span>` `<span class="pre">`2,`</span>` `<span class="pre">`3]}`</span>)
>
> - **sec** (オプション) - ターゲットセクション (デフォルト: <span class="pre">`'soma'`</span>)
>
> - **loc** (オプション) - ターゲットの場所 (デフォルト: 0.5)
> 関数として定義可能 (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> - **synMech** (オプション; NetStims のみ) - NetStim を接続するシナプス メカニズムのラベル
>
> - **重み** (オプション; NetStims のみ) - NetStim とセル間の接続の重み
> 関数として定義可能 (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> - **遅延** (オプション; NetStims のみ) - NetStim とセル間の接続の遅延 (デフォルト: 1)
> 関数として定義可能 (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> - **synsPerConn** (オプション; NetStims のみ) - NetStim とセル間の接続のシナプスの数 (デフォルト: 1)
> 関数として定義可能 (<a href="user_documentation.html#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> </div>

以下のコードは、さまざまなタイプの刺激を作成し、それらをセルのさまざまなサブセットにマッピングする方法の例を示しています。

<div class="highlight-python notranslate">

<div class="highlight">

    # Stimulation parameters

    ## Stimulation sources parameters
    netParams.stimSourceParams['Input_1'] =  {'type': 'IClamp', 'del': 10, 'dur': 800, 'amp': 'uniform(0.05, 0.5)'}

    netParams.stimSourceParams['Input_2'] = {'type': 'VClamp', 'dur': [0, 1, 1], 'amp':[1, 1, 1],'gain': 1, 'rstim': 0, 'tau1': 1, 'tau2': 1, 'i': 1}

    netParams.stimSourceParams(['Input_3'] = {'type': 'AlphaSynapse', 'onset': 'uniform(1, 500)', 'tau': 5, 'gmax': 'post_ynorm', 'e': 0}

    netParams.stimSourceParams['Input_4'] = {'type': 'NetStim', 'interval': 'uniform(20, 100)', 'number': 1000, 'start': 5, 'noise': 0.1}

    ## Stimulation mapping parameters
    netParams.stimTargetParams['Input1->PYR'] = {
            'source': 'Input_1',
            'sec': 'soma',
            'loc': 0.5,
            'conds': {'pop':'PYR', 'cellList': range(8)}}

    netParams.stimTargetParams['Input3->Basket'] = {
            'source': 'Input_3',
            'sec': 'soma',
            'loc': 0.5,
            'conds': {'cellType': 'Basket'}}

    netParams.stimTargetParams['Input4->PYR3'] = {
            'source': 'Input_4',
            'sec': 'soma',
            'loc': 0.5,
            'weight': '0.1 + normal(0.2, 0.05)',
            'delay': 1,
            'conds': {'pop': 'PYR3', 'cellList': [0, 1, 2, 5, 10, 14, 15]}}

</div>

</div>

</div>

<div id="reaction-diffusion-rxd-parameters" class="section">

### 反応拡散 (RxD) パラメーター<a href="#reaction-diffusion-rxd-parameters" class="headerlink" title="Link to this heading"></a>

<span class="pre">`rxdParams`</span> 順序付き辞書を使用して、さまざまな RxD コンポーネントを定義できます。

- **領域** - RxD 領域の辞書 (「細胞外」領域の定義にも使用できます)

> <div>
  >
  > このコンポーネントは必須であり、反応が起こる場所を定義するために必要です。 <span class="pre">`rxdParams['regions']`</span> の各項目は、キーが領域の名前 (さらなる定義で使用される) を指定し、値が次のフィールドを含む辞書である。
  >
  > - <span class="pre">`cells`</span>: 種、反応などを指定する必要がある細胞内ドメインの定義に関連する細胞のリスト。このリストには、セル gid (例: <span class="pre">`[1]`</span> または <span class="pre">`[0,`</span>` `<span class="pre">`3]`</span>)、集団ラベル (例: <span class="pre">`['S']`</span> または <span class="pre">`['all']`</span>)、または混合 (例: <span class="pre">`[['S',[0,2]]]`</span> または<span class="pre">`[('S',[0,2])]`</span>)。
  >
  > - <span class="pre">`secs`</span>: 上記のセルに含めるセクションのリスト (有効にするためには、セルの「秒」内にある必要があります)。たとえば、\['soma','Bdend'\] などです。
  >
  > <span class="pre">`cells`</span> と <span class="pre">`secs`</span> は両方とも、(細胞内) RxD が関連コンポーネントである NEURON セクションを指定するために使用されます。
  >
  > - <span class="pre">`nrn_region`</span>: 領域が細胞の細胞内/細胞質ドメイン (膜貫通電圧の計算対象) に対応するかどうかを定義するオプション。利用可能なオプションは次のとおりです: 「i」 (細胞膜のすぐ内側)、「o」 (血漿のすぐ外側)、または None (上記のどれでもない、たとえば細胞内小器官)。
  >
  > - <span class="pre">`geometry`</span>: このエントリは、領域に関連付けられたジオメトリを定義します。 NEURON のさまざまなオプションに応じて、文字列 (「inside」または「membrane」) または 2 つのエントリを持つ辞書のいずれかになります。ジオメトリの種類を示す「class」 (「DistributedBoundary」、「Fractional Volume」、「FixedCrossSection」、「FixedPerimeter」、「ScalableBorder」、「Shell」) と、構造化された定義に必要な特定の引数を含む「args」です。辞書で。たとえば、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['regions'] = {'membrane_in':{'cells': 'all', 'secs': 'all', 'geometry': {'class': 'ScalableBorder', 'args': {'scale': 1, 'on_cell_surface': False}}}}。
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > - <span class="pre">`dimension`</span>: これは整数 (1 または 3) で、シミュレーションが 1D か 3D かを示します。
  >
  > - <span class="pre">`dx`</span>: 離散化を指定する float (または int)。
  >
  > - <span class="pre">`extracellular`</span>: 領域が細胞外空間を表すかどうかを示すブール オプション (指定されていない場合は <span class="pre">`False`</span>)。 <span class="pre">`True`</span> の場合、以前のすべての extries を指定する必要はありません。代わりに、<span class="pre">`rxdParams['extracellular']`</span> (次を参照) に対応するエントリを考慮する必要がありますが、これは辞書階層の同じレベルにあります。たとえば、<span class="pre">`rxdParams['regions']={'ext':{'extracellular':True,`</span>` `<span class="pre">`'xlo':`</span>` `<span class="pre">`-100,`</span>` `<span class="pre">`...}}`</span> のようになります。
  >
  > 例、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['regions'] = {'cyt':{'cells': ['all'], 'secs': ['soma','Bdend'], 'nrn_region': 'i'}}
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > </div>

- **細胞外** - RxD 細胞外領域を指定するために必要なパラメータを含む辞書。

> <div>
  >
  > - <span class="pre">`xlo`</span>、<span class="pre">`ylo`</span>、<span class="pre">`zlo`</span>: 細胞外ドメインを指定するボックスの左下奥の隅を示す値。
  >
  > - <span class="pre">`xhi`</span>、<span class="pre">`yhi`</span>、<span class="pre">`zhi`</span>: 細胞外ドメインを指定するボックスの右上隅を示す値。
  >
  > - <span class="pre">`dx`</span>: 離散化を指定する値 (int、float)。この場合、細胞外領域は、正方形のボクセル以外が必要な場合、3D タプルになる可能性があります。
  >
  > 前のエントリは必須です。次の値はオプションです (デフォルト値が考慮されます。NEURON を参照)。
  >
  > - <span class="pre">`volume_fraction`</span>: 拡散に利用可能なスペースを示す値。
  >
  > - <span class="pre">`tortuosity`</span>: 拡散する直進経路がどの程度制限されているかを示す値。
  >
  > たとえば、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['extracular'] = {'xlo':-100, 'ylo':-100, 'zlo':-100, 'xhi':100, 'yhi':100, 'zhi':100, 'dx':(0.2,0.2,0.4), 'volume_fraction':0.2, 「ねじれ度」: 1.6}。
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > </div>

- **種** - このコンポーネントも必須であり、関連する種とそれらが関与するドメインを指定するためのすべての定義を含む辞書に対応します。キーは種の名前/ラベルで、値は次のエントリを含む辞書です。

> <div>
  >
  > - <span class="pre">`regions`</span>: 種が存在する地域のリスト (<span class="pre">`rxdParams['regions']`</span> にリストされている)。単一の地域の場合は、リストせずに指定することもできます。たとえば、<span class="pre">`'cyt'`</span> または <span class="pre">`['cyt','er']`</span> です。
  >
  > - <span class="pre">`d`</span>: 種の拡散係数。
  >
  > - <span class="pre">`charge`</span>: 種の署名済み請求 (存在する場合)。
  >
  > - <span class="pre">`initial`</span>: 濃度フィールドの初期状態 (mM 単位)。これは、その定義ドメイン全体に対する単一の値、または文字列ベースの関数であり、変数は (RxD のフレームワーク内の) ノード プロパティです。たとえば、 <span class="pre">`'1`</span>` `<span class="pre">`if`</span>` `<span class="pre">`(0.4`</span>` `<span class="pre">`<`</span>` `<span class="pre">`node.x`</span>` `<span class="pre">`<`</span>` `<span class="pre">`0.6)`</span>` `<span class="pre">`else`</span>` `<span class="pre">`0'`</span>。
  >
  > - <span class="pre">`ecs_boundary_conditions`</span>: 細胞外領域が定義されている場合は、境界条件を指定する必要があります。オプションは、ゼロ磁束条件 (ノイマン型) または境界での濃度を示す値 (ディリクレ) の <span class="pre">`None`</span> (デフォルト) です。
  >
  > - <span class="pre">`atolscale`</span>: この特定の種の濃度の可変ステップ積分における絶対許容誤差のスケール係数を示す数値 (デフォルト = 1)。
  >
  > - <span class="pre">`name`</span>: この種にラベルを付ける文字列。この名前は NEURON 範囲変数と同じである必要があるため、RxD が hoc モデルと種を共有する場合に重要です。
  >
  > 例、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['species'] = {'ca':{'regions': 'cyt', 'd': 0.25, 'charge': 2, 'name': 'ca', 'initial': '1 if node.sec in ['Bdend'] else 0'}}
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > </div>

- **states** - シミュレーション中に反応以外を通じて変化する状態変数を宣言する辞書。キーはこの変数に割り当てられた名前で、値は次のエントリを含む辞書です。

> <div>
  >
  > - <span class="pre">`regions`</span>: 状態変数が関連する (つまり、そこで展開される) 領域のリスト。単一の地域の場合は、リストせずに指定することもできます。
  >
  > - <span class="pre">`initial`</span>: この変数の初期状態。ドメイン全体 (この変数が指定されている場所) で有効な単一値、または独立変数としてノード プロパティを持つ文字列ベースの関数のいずれか。
  >
  > - <span class="pre">`name`</span>: この変数を内部的にラベル付けする文字列。
  >
  > 例、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['states'] = {'mgate':{'regions': 'cyt', 'initial': 0.05, 'name': 'mgate'}}
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > </div>

- **反応** - 分析中の反応、誰がどこでしたかを指定する辞書。キーは反応にラベルを付け、値は次のエントリを含む辞書です。

> <div>
  >
  > - <span class="pre">`reactant`</span>: 化学反応の左側を、種と適切な化学量論とともに宣言する文字列。たとえば、<span class="pre">`ca`</span>` `<span class="pre">`+`</span>` `<span class="pre">`2`</span>` `<span class="pre">`*`</span>` `<span class="pre">`cl`</span> のようにします。ここで、「ca」と「cl」は「種」エントリーであり、反応が起こる地域で利用可能です (次を参照)。
  >
  > - <span class="pre">`product`</span>: 化学反応の右側についても同様です。たとえば、<span class="pre">`cacl2`</span> の場合、「cacl2」は適切に定義された種です。
  >
  > - <span class="pre">`rate_f`</span>: 上で定義したスキームの順反応の速度。これは、数値または文字列ベースの関数のいずれかになります (種などに応じて、たとえば、ヒル方程式を実装するため)。
  >
  > - <span class="pre">`rate_b`</span>: 上記と同じ、逆方向の反応の場合。このエントリはオプションです。
  >
  > - <span class="pre">`regions`</span>: このエントリは、領域のリスト内でのみ反応が進行するように制限するために使用されます。単一の地域の場合は、リストせずに指定することもできます。指定しない場合、反応はすべての (妥当な) 領域で進行します。
  >
  > - <span class="pre">`custom_dynamics`</span>: このブール値エントリは、素反応に対する質量作用の法則が適用されるかどうかを指定します。 「True」の場合、各種の濃度のダイナミクスは質量作用スキームを満たします。
  >
  > 例、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['reactions'] = {'リン酸化':{'反応剤': 'E', 'product': 'EP', 'rate_f': 'kmax1 * E/ (k1 + E)', 'rate_b': 'kmax2 * EP/ (k2 + EP)','custom_dynamics': True}}
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > </div>

- **multicompartmentReactions** - 異なる領域に属する種との反応を指定する辞書。前のケースと同様に、キーは反応にラベルを付け、値は以前とまったく同じエントリとさらに 2 つの (オプションの) エントリを含む辞書になります。

> <div>
  >
  > - <span class="pre">`membrane`</span>: ある領域から別の領域へのイオンの通過に関与する領域 (膜または境界と互換性のある幾何学的形状を持つ)。
  >
  > - <span class="pre">`membrane_flux`</span>: このブール値のエントリは、反応によって膜電位に影響を与える細胞膜を横切る電流が生成されるかどうかを示します。
  >
  > </div>

。
注: 「反応物」または「生成物」のエントリに表示される種は、反応スキーム内でそれらが取得された領域とともに指定する必要があることを考慮してください。たとえば、<span class="pre">`'ca[cyt]'`</span> などです。

- **rates** - 選択した種または状態のダイナミクスを制御するレートを指定する辞書。キーは動的スキームにラベルを付け、値は次のエントリを含む辞書です。

> <div>
  >
  > - <span class="pre">`species`</span>: どの種または状態が考慮されているかを示す文字列。
  >
  > - <span class="pre">`rate`</span>: 種/状態の時間的進化を支配する力学方程式における速度の値。
  >
  > - <span class="pre">`regions`</span>: このエントリは、ダイナミクスが領域のリスト内でのみ進行するように制約するために使用されます。単一の地域の場合は、リストせずに指定することもできます。
  >
  > - <span class="pre">`membrane_flux`</span>: 前と同様、電流を考慮するかどうかを指定するブール値エントリ。 「True」の場合、「region」エントリは膜状のジオメトリを持つ固有の領域に対応する必要があります。
  >
  > 例、
  >
  > > <div>
  > >
  > > <div class="highlight-python notranslate">
  > >
  > > <div class="highlight">
  > >
  > > netParams.rxdParams['rates'] = {'h_evol':{'species': h_gate, 'rate': '(1. / (1 + 1000. * ca[cyt] / (0.3)) - h_gate) / tau'}}
  > >
  > > </div>
  > >
  > > </div>
  > >
  > > </div>
  >
  > </div>

各ディクショナリのパラメータは、RxD パッケージで説明されているものと同じ構造に従います: <a href="https://www.neuron.yale.edu/neuron/static/docs/rxd/index.html" class="reference external">https://www.neuron.yale.edu/neuron/static/docs/rxd/index.html</a>

使用例を参照してください: <a href="https://github.com/Neurosim-lab/netpyne/tree/development/examples/rxd_buffering" class="reference external">RxD バッファリングの例</a> および <a href="https://github.com/Neurosim-lab/netpyne/tree/development/examples/rxd_buffering" class="reference external">RxD ネットワークの例</a>。

</div>

</div>

</div>

</div>

</div>
</section>

</article>
</main>
