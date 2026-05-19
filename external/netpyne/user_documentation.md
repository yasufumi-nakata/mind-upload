---
layout: default
title: "NetPyNE docs: ユーザードキュメント<a href=\"#user-documentation\" class=\"headerlink\" title=\"Link to this heading\"></a>"
description: "NetPyNE docs: user_documentation.md の日本語訳"
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
<p>原典: <a href="http://doc.netpyne.org/user_documentation.html" target="_blank" rel="noopener noreferrer">http://doc.netpyne.org/user_documentation.html</a></p>
<p>ライセンス: MIT License for NetPyNE repository documentation/code。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="user-documentation" class="section">

<span id="package-reference"></span>

# ユーザードキュメント<a href="#user-documentation" class="headerlink" title="Link to this heading"></a>

<div id="model-components-and-structure" class="section">

## モデルのコンポーネントと構造<a href="#model-components-and-structure" class="headerlink" title="Link to this heading"></a>

ネットワーク モデルを作成するには、以下が必要です。

- ネットワークパラメータを持つクラス <span class="pre">`specs.NetParams`</span> のオブジェクト <span class="pre">`netParams`</span>。

- シミュレーション構成オプションを備えたクラス <span class="pre">`specs.SimConfig`</span> のオブジェクト <span class="pre">`simConfig`</span>。

- ネットワーク モデルを作成して実行するためのメソッドの呼び出し。引数として上記の辞書を渡します。 <span class="pre">`createSimulateAnalyze(netParams,`</span>` `<span class="pre">`simConfig)`</span>。

これらのコンポーネントは、単一または複数の Python ファイルに含めることができます。このセクションでは、ネットワーク パラメーターとシミュレーション構成オプションを定義する方法、およびネットワーク モデルの作成と実行に使用できる方法について包括的に説明します。

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

<span class="pre">`netParams`</span> dict への他の任意のエントリを追加し、接続パラメーターのカスタム定義関数で使用できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a> を参照)。

<div id="cell-types" class="section">

<span id="id1"></span>

### セルの種類<a href="#cell-types" class="headerlink" title="Link to this heading"></a>

<span class="pre">`cellParams`</span> 順序付き辞書の各項目は、キーと値で構成されます。キーは、このセルの種類を識別するためのラベルです。値は、次のフィールドを含むセルのプロパティを定義するディクショナリで構成されます。

- **secs** - セルのセクションを含むディクショナリ。各セクションには次のフィールドが含まれます (空のフィールドは省略できます)。

> <div>
  >
  > - **geom**: <span class="pre">`diam`</span>、<span class="pre">`L`</span>、または <span class="pre">`Ra`</span> などのジオメトリ プロパティを含むディクショナリ。
  > オプションで、3D 点のリストを含むフィールド <span class="pre">`pt3d`</span> を含めることができます。各点は <span class="pre">`(x,y,z,diam)`</span> 形式のタプルとして定義されます。 <span class="pre">`diam`</span>、<span class="pre">`L`</span>、または <span class="pre">`Ra`</span> の値は関数として定義できます (「 <a href="#function-string" class="reference internal"><span class="std std-ref">文字列として機能します</span></a>)。
  >
  > - **topol**: トポロジのプロパティを含むディクショナリ。
  > <span class="pre">`parentSec`</span> (親セクションのラベル)、<span class="pre">`parentX`</span> (接続を行う親の場所)、および <span class="pre">`childX`</span> (現在のセクション -子- 接続を行う場所) が含まれます。
  >
  > - **mechs**: 密度/分散メカニズムの辞書。
  > キーにはメカニズムの名前が含まれます (例: 「hh」または「pas」)。 値にはメカニズムのプロパティを含む辞書が含まれます (例: <span class="pre">`{'g':`</span>` `<span class="pre">`0.003,`</span>` `<span class="pre">`'e':`</span>` `<span class="pre">`-70}`</span>)。これらのプロパティは関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > - **イオン**: イオンの辞書。
  > キーにはイオンの名前 (例: 「na」または「k」) が含まれます。 値には、特定のセクションのイオンのプロパティを含む辞書が含まれます (例: <span class="pre">`{'e':`</span>` `<span class="pre">`-70}`</span>)。利用可能なプロパティは、<span class="pre">`'e'`</span>: 逆転電位、<span class="pre">`'i'`</span>: そのセクションのイオンの内部濃度、および <span class="pre">`'o'`</span>: そのセクションのイオンの細胞外濃度です。
  >
  > - **pointps**: 点プロセスの辞書 (シナプス機構を除く)。
  > キーには任意のラベルが含まれます (例: 「Izhi」)。 値にはポイント プロセスのプロパティを含む辞書が含まれます (例: 「Izhi」)。 <span class="pre">`{'mod':'Izhi2007a',`</span>` `<span class="pre">`'a':0.03,`</span>` `<span class="pre">`'b':-2,`</span>` `<span class="pre">`'c':-50,`</span>` `<span class="pre">`'d':100,`</span>` `<span class="pre">`'celltype':1})`</span>。これらのプロパティは関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > 内部ポイント プロセス変数とは別に、次のプロパティを各ポイント プロセスに指定できます。
  >
  > - <span class="pre">`mod`</span>、NEURON メカニズムの名前。 <span class="pre">`'Izhi2007a'`</span>
  >
  > - <span class="pre">`loc`</span>、シナプス機構を配置するセクションの位置。 <span class="pre">`1.0`</span>、デフォルト=0.5
  >
  > - <span class="pre">`vref`</span> (オプション)、細胞膜電圧を含む内部メカニズム変数。 <span class="pre">`'V'`</span>
  >
  > - <span class="pre">`synList`</span> (オプション)、内部メカニズムのシナプスメカニズムのラベルのリスト。 \[「AMPA」、「NMDA」、「GABAB」\]
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

- **vars** - (オプション) このセル タイプの任意のセクションのプロパティで参照できるユーザー定義変数のディクショナリ。
  使用例：

<div class="highlight-default notranslate">

<div class="highlight">

      cellRule['secs']['dend1']['mechs']['pas'] = {'g': 'g_default + 1e-6'}  # cell variable 'g_default' referenced
      cellRule['secs']['dend2']['mechs']['pas'] = {'g': 'g_default + 1.5e-6'}  # cell variable 'g_default' referenced
      cellRule['vars'] = {'g_default': 0.0000357} # cell variable 'g_default' defined

</div>

</div>

セル変数の値自体も関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a> を参照)。 <span class="pre">`cellRule['vars']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'g_default':`</span>` `<span class="pre">`'normal(3.57e-5,`</span>` `<span class="pre">`1e-7)}`</span>

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

セルのプロパティは外部ファイルからインポートできます。詳細と例については、<a href="#importing-cells" class="reference internal"><span class="std std-ref">外部定義セル モデルのインポート</span></a>を参照してください。

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

<span class="pre">`cellModel`</span> が「VecStim」の場合、「spikePattern」辞書を作成することでパターン ジェネレーターを使用できます。

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.popParams['artif1'] = {'cellModel': 'VecStim'
                                     ...
                                     'spikePattern': {'type': 'rhythmic', # can be 'rhythmic', 'evoked', 'poisson', 'gauss'
                                                      ...                 # see netpyne/cell/inputs.py for argument entries
                                                      }
                                     }

</div>

</div>

現在、「rhythmic」、「evoked」、「poisson」、および「gauss」スパイク パターン ジェネレーターが利用可能です。それらの引数エントリは次のとおりです。

- **リズミック** - 継続的な外部入力を作成します（リズミック）

> <div>
  >
  > - **start** - 最初のスパイクの時間。 -1 の場合、startMin と startMax 間の均一な分布 (ミリ秒)
  >
  > - **startMin** - 開始時間の一様分布の最小値 (ミリ秒)
  >
  > - **startMax** - 開始時間の一様分布の最大値 (ミリ秒)
  >
  > - **startStd** - 開始時間の正規分布の標準偏差 (ミリ秒);平均値は開始パラメータによって設定されます。 \> 0.0の場合にのみ使用されます
  >
  > - **freq** - リズミカルパターンの振動周波数 (Hz)
  >
  > - **freqStd** - 発振周波数の標準偏差 (Hz)
  >
  > - **分布** - 発振周波数の分布タイプ。 「普通」か「均一」か
  >
  > - **eventsPerCycle** - サイクルごとのスパイク/バースト。 1 または 2 のいずれかである必要があります
  >
  > - **repeats** - 入力パターンを繰り返す回数 (入力数に相当)
  >
  > - **停止** - パターンの最後のスパイクの最大時間 (ミリ秒)
  >
  > </div>

- **誘発** - 進行中の外部入力（リズミカル）を作成します

> <div>
  >
  > - **start** - 最初のスパイクの時間
  >
  > - **inc** - 最初のスパイク時間の増加。 cfg.inc_evinput から (ミリ秒)
  >
  > - **startStd** - 開始の標準偏差 (ms)
  >
  > - **numspikes** - 生成するスパイクの総数
  >
  > </div>

- **ポアソン** - 外部ポアソン入力を作成します

> <div>
  >
  > - **start** - 最初のスパイクの時間 (ミリ秒)
  >
  > - **停止** - 時間を停止します。 -1 の場合、全期間 (ミリ秒)
  >
  > - **周波数** - 開始の標準偏差 (ms)
  >
  > </div>

- **gauss** - ガウス入力を作成します

> <div>
  >
  > - **mu** - ガウス平均
  >
  > - **シグマ** - ガウス分散
  >
  > </div>

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

- メカニズムパラメータ (<span class="pre">`tau`</span> または <span class="pre">`e`</span> など) - これらは特定の NMODL メカニズムに依存します。これらのパラメーターの値は関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。

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

単一のセクションの名前、セクションのリストとして定義できます。 <span class="pre">`['soma',`</span>` `<span class="pre">`'dend']`</span>、またはシナプス後 cellParams の **secList** 辞書からのキー。

<span class="pre">`synsPerConn`</span> \> 1 でセクションのリストが指定されている場合、シナプスは各セクションの長さを考慮して、指定されたセクションに沿って均一に分散されます。これはデフォルトの動作ですが、変更できます。詳細と例については、<a href="#multisynapse-conn" class="reference internal"><span class="std std-ref">マルチシナプス接続</span></a> を参照してください。

<span class="pre">`synsPerConn`</span> == 1 でセクションのリストが指定されている場合、リストからランダムに選択されたセクションにシナプス (セル間接続ごとに 1 つ) が配置されます。リストの最初のセクションを常に使用するようにするには、<a href="#conn-rand-sec" class="reference internal"><span class="std std-ref">connRandomSecFromList</span></a> を設定します。

- **loc** (オプション) - ターゲット シナプス メカニズムの位置 (例: <span class="pre">`0.3`</span>)
  省略した場合、デフォルトは 0.5 になります。

<span class="pre">`synMechs`</span> のリストがある場合は、すべてに対して 1 つの loc を作成するか、または loc のリスト (synMech ごとに 1 つ、たとえば 2 つの synMech の場合: <span class="pre">`[0.4,`</span>` `<span class="pre">`0.7]`</span>) を作成できます。

<span class="pre">`synsPerConn`</span> \> 1 の場合、すべてに対して 1 つの loc を指定するか、または loc のリスト (シナプスごとに 1 つ、たとえば <span class="pre">`synsPerConn`</span> = 3 の場合) を指定できます。 <span class="pre">`[0.4,`</span>` `<span class="pre">`0.5,`</span>` `<span class="pre">`0.7]`</span>)

<span class="pre">`synMechs`</span> と <span class="pre">`synsPerConn`</span> \> 1 の両方のリストがある場合、各 synMech の各シナプスの 2D リストを持つことができます (たとえば、2 つの synMech と <span class="pre">`synsPerConn`</span> = 3 の場合)。 <span class="pre">`[[0.2,`</span>` `<span class="pre">`0.3,`</span>` `<span class="pre">`0.5],`</span>` `<span class="pre">`[0.5,`</span>` `<span class="pre">`0.6,`</span>` `<span class="pre">`0.7]]`</span>)

これらのマルチシナプス シナリオでは、追加のパラメーターが使用可能になります。詳細については、「<a href="#multisynapse-conn" class="reference internal"><span class="std std-ref">マルチシナプス接続</span></a>」を参照してください。

<span class="pre">`synsPerConn`</span> == 1 で、<span class="pre">`loc`</span> と <span class="pre">`sec`</span> の両方がリストの場合、シナプス (シナプス前セルごとに 1 つ) は、リストからランダムに選択された位置とセクションに配置されます (ランダムなセクションと位置は密接に関係することに注意してください。つまり、両方に同じランダム インデックスが使用されます)。それぞれのリストの最初のセクションと場所を常に使用するようにするには、<a href="#conn-rand-sec" class="reference internal"><span class="std std-ref">connRandomSecFromList</span></a> を設定するか、<span class="pre">`loc`</span> または <span class="pre">`sec`</span> を単一の値として保持します。

- **synMech** (オプション) - シナプス後ニューロン上のターゲット シナプス メカニズムのラベル (またはラベルのリスト) (例: <span class="pre">`'AMPA'`</span> または <span class="pre">`['AMPA',`</span>` `<span class="pre">`'NMDA']`</span>)

> <div>
  >
  > 省略した場合、セルのシナプス機構リストの最初のシナプス機構が使用されます。
  >
  > シナプスメカニズムのリストを使用する場合、メカニズムごとに個別の接続が作成されます。オプションで、重み、遅延、位置の対応するリストを提供できます。詳細については、「<a href="#multisynapse-conn" class="reference internal"><span class="std std-ref">マルチシナプス接続</span></a>」を参照してください。
  >
  > </div>

- **synsPerConn** (オプション) - セル間接続 (*connection*) ごとの個々のシナプス接続 (*synapses*) の数

> <div>
  >
  > 関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > 省略した場合、デフォルトは 1 になります。
  >
  > 各シナプスの重み、遅延、位置、あるいはその両方をリストとして指定することも、単一の値をすべてに使用することもできます。
  >
  > <span class="pre">`synsPerConn`</span> \> 1 で *単一セクション* を指定すると、<span class="pre">`loc`</span> でシナプスの位置をリストとして指定できます。 *ターゲット セクションのリスト* が指定されている場合は、<span class="pre">`loc`</span> を省略する必要があり、シナプスは各セクションの長さを考慮して、指定されたセクションに沿って均一に分散されます。これはデフォルトの動作ですが、変更できます。詳細については、<a href="#multisynapse-conn" class="reference internal"><span class="std std-ref">マルチシナプス接続</span></a>を参照してください。
  >
  > <span class="pre">`synMechs`</span> のリストがある場合は、すべてに対して単一の <span class="pre">`synsPerConn`</span> 値を指定することも、リスト内のシナプス メカニズムごとに 1 つの値のリストを指定することもできます。
  >
  > <div class="highlight-python notranslate">
  >
  > <div class="highlight">
  >
  > # セル間接続ごとに 2 つの AMPA シナプスと 2 つの GABA シナプス:
  > netParams.connParams[...] = {
  > 'synMech': ['AMPA', 'GABA'],
  > 'synsPerConn': 2、
  > # ...
  >
  > # セル間接続ごとに 2 つの AMPA シナプスと 1 つの GABA シナプス:
  > netParams.connParams[...] = {
  > 'synMech': ['AMPA', 'GABA'],
  > 'synsPerConn': [2, 1],
  > # ...
  >
  > </div>
  >
  > </div>
  >
  > </div>

- **重量** (オプション) - シナプス接続の強度 (例: <span class="pre">`0.01`</span>)
  コンダクタンスの変化に関連しますが、シナプス機構と細胞モデルに応じて意味と規模が異なります。

関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。

省略した場合、デフォルトは <span class="pre">`netParams.defaultWeight`</span>` `<span class="pre">`=`</span>` `<span class="pre">`1`</span> になります。

<span class="pre">`synMechs`</span> のリストがある場合は、すべての重みを 1 つ持つことも、重みのリスト (synMech ごとに 1 つ、たとえば 2 つの synMech の場合: <span class="pre">`[0.1,`</span>` `<span class="pre">`0.01]`</span>) を持つこともできます。

<span class="pre">`synsPerConn`</span> \> 1 の場合、すべてに対して単一の重みを指定することも、重みのリストを指定することもできます (シナプスごとに 1 つ、たとえば、<span class="pre">`synsPerConn`</span> = 3 の場合: <span class="pre">`[0.2,`</span>` `<span class="pre">`0.3,`</span>` `<span class="pre">`0.4]`</span>)。

<span class="pre">`synMechs`</span> と <span class="pre">`synsPerConn`</span> \> 1 の両方のリストがある場合、各 synMech の各シナプスの 2D リストを持つことができます (たとえば、2 つの synMech と <span class="pre">`synsPerConn`</span> = 3 の場合)。 <span class="pre">`[[0.2,`</span>` `<span class="pre">`0.3,`</span>` `<span class="pre">`0.4],`</span>` `<span class="pre">`[0.02,`</span>` `<span class="pre">`0.04,`</span>` `<span class="pre">`0.03]]`</span>)

- **遅延** (オプション) - シナプス前スパイクがシナプス後ニューロンに到達するまでの時間 (ミリ秒)
  関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)

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
  > 関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > <span class="pre">`connFunc`</span> を <span class="pre">`probConn`</span> に設定します (内部確率的接続関数)。
  >
  > <span class="pre">`convergence`</span>、<span class="pre">`divergence`</span>、および <span class="pre">`fromList`</span> パラメータをオーバーライドします。
  >
  > </div>

- **収束** (オプション) - 各シナプス後セルに接続されているシナプス前セルの数

> <div>
  >
  > 関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
  >
  > <span class="pre">`connFunc`</span> を <span class="pre">`convConn`</span> に設定します (内部コンバージェンス接続機能)。
  >
  > <span class="pre">`divergence`</span> および <span class="pre">`fromList`</span> パラメータをオーバーライドします。 <span class="pre">`probability`</span> パラメータが含まれている場合は効果がありません。
  >
  > </div>

- **発散** (オプション) - 各シナプス前セルに接続されているシナプス後セルの数

> <div>
  >
  > 関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)。
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

**接続ごとに複数のシナプスを使用する接続ルール**

デフォルトでは、セル間接続ごとに作成されるシナプスは 1 つだけです。ただし、接続には複数の個別のシナプス接触が含まれる場合があり、たとえば、シナプス前細胞の軸索が分岐して、シナプス後細胞の樹状突起の異なる位置で複数のシナプス接触を形成することがあります。これは、<span class="pre">`synsPerConn`</span> を 1 より大きい値に設定するか、<span class="pre">`synMech`</span> をリストとして定義するか、あるいはその両方によって実現できます。

- <span class="pre">`synsPerConn`</span> \> 1 を <span class="pre">`synMech`</span> を単一の値として設定
  <span class="pre">`synsPerConn`</span> が \> 1 の場合、接続ごとにこの数のシナプスが作成されます。重みと遅延はリストとして指定することも、単一の値をすべてに使用することもできます (以下の例を参照)。

- **単一セクション**を指定すると、すべてのシナプスがそのセクション内に作成され、その位置を <span class="pre">`loc`</span> のリストとして指定できます (シナプスごとに 1 つ)。

    > <div>
    >
    > <div class="highlight-python notranslate">
    >
    > <div class="highlight">
    >
    >     netParams.connParams[...] = {
    >             'synsPerConn': 2,
    >             'sec': 'soma',
    >             'synMech': 'AMPA',
    >             'weight': [0.1, 0.2], # individual weights for each synapse
    >             'delay': 0.1, # single delay for all synapses
    >             'loc': [0.5, 1.0] # individual locations for each synapse
    >     # ...
    >
    >     # This will create 2 synapses: one with weight 0.1, delay 0.1, and loc 0.5
    >     # and another with weight 0.2, delay 0.1, and loc 1.0.
    >
    > </div>
    >
    > </div>
    >
    > A single value for <span class="pre">`loc`</span> is not accepted. If it is omitted, synapses are placed at equal distances along the section (e.g. with <span class="pre">`synsPerConn`</span> = 3, synapses will be placed at 0.1666, 0.5 and 0.8333).
    >
    > </div>

- **セクションのリスト** (明示的に、または <span class="pre">`secLists`</span> からのキーとして) が指定されている場合、接続ロジックは <span class="pre">`distributeSynsUniformly`</span> および <span class="pre">`connRandomSecFromList`</span> 属性に依存します。これらは、<a href="#conn-rand-sec" class="reference internal"><span class="std std-ref">simConfig</span></a> を通じてグローバルに設定することも、connParams エントリごとに個別に設定することもできます (例: <span class="pre">`netParams.connParams[...]`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{...,`</span>` `<span class="pre">`'distributeSynsUniformly':`</span>` `<span class="pre">`False}`</span>)、個別の設定が優先されます。次のオプションが利用可能です。

    > <div>
    >
    > - <span class="pre">`distributeSynsUniformly`</span> = True (Default)
    >   Synapses will be distributed uniformly along the specified section(s), taking into account the length of each section. (E.g., if you specify <span class="pre">`'sec':`</span>` `<span class="pre">`['soma',`</span>` `<span class="pre">`'dend']`</span> with lengths of 10 and 20 respectively, and set <span class="pre">`synsPerConn`</span> = 5, the resulting distribution of synapses will be in the sections and locations illustrated in the figure below). Providing location explicitly is not possible in th is case.
    >
    >   <a href="_images/multisyn_0.png" class="reference internal image-reference"><img src="_images/multisyn_0.png" class="align-center" style="width: 50%;" alt="_images/multisyn_0.png" /></a>
    >
    > - <span class="pre">`distributeSynsUniformly`</span> = False
    >   - If <span class="pre">`connRandomSecFromList`</span> is <span class="pre">`True`</span> (default), a random section will be picked from the sections list for each synapse. The <span class="pre">`loc`</span> value should also be a list, and the values will be picked from it randomly and independently from section choice. If the length of sections or locations list is greater or equal to <span class="pre">`synsPerConn`</span>, random choice is guaranteed to be without replacement. If <span class="pre">`loc`</span> is omitted, the value for each synapse is randomly sampled from uniform\[0, 1\].
    >
    >   - If <span class="pre">`connRandomSecFromList`</span> is <span class="pre">`False`</span>, sections and locations are assigned deterministically: the N-th synapse receives the N-th section and N-th location from their respective lists (or if <span class="pre">`loc`</span> is a single value, it is used for all synapses). Ensure that lists of sections and locations both have the length equal to <span class="pre">`synsPerConn`</span>.
    >
    > </div>

- <span class="pre">`synMech`</span> をリストとして設定する
  <span class="pre">`synMech`</span> がリストの場合、リスト内のメカニズムごとにシナプスが作成されます。重み、遅延、および位置は、<span class="pre">`synMech`</span> と同じ長さのリストとして指定することも、単一の値をすべてに使用することもできます。

<div class="highlight-python notranslate">

<div class="highlight">

      netParams.connParams[...] = {
              'synMech': ['AMPA', 'GABA'],
              'weight': [0.1, 0.2], # individual weights for each synapse
              'delay': 0.1, # single delay for all synapses
      # ...

      # This will create 2 synapses: one with AMPA synMech and weight 0.1
      # and another with GABA synMech and weight 0.2. Both will have the same delay of 0.1.

</div>

</div>

ただし、セクションについては、<span class="pre">`synMech`</span> 要素に対するそのような 1 対 1 の対応は適用されません。代わりに、<span class="pre">`secs`</span> の内容が各 synMech に対して繰り返されます。

<div class="highlight-python notranslate">

<div class="highlight">

      netParams.connParams[...] = {
              'synMech': ['AMPA', 'GABA'],
              'sec': ['soma', 'dend']
      # ...
      # Both AMPA and GABA synapses will span 'soma' and 'dend' sections

</div>

</div>

異なるセクションが必要な場合は、シナプス メカニズムごとに個別の接続ルール (<span class="pre">`connParams`</span> エントリ) を定義する必要があります。

- <span class="pre">`synMech`</span> をリストとして設定し、<span class="pre">`synsPerConn`</span> \> 1 を設定します。
  <span class="pre">`synMechs`</span> と <span class="pre">`synsPerConn`</span> \> 1 の N 要素リストの両方がある場合でも、重みと遅延をすべてのシナプスの単一の値、長さ N のリスト (各値は <span class="pre">`synMech`</span> リスト インデックスに対応)、または外側の次元 N が <span class="pre">`synMechs`</span> に対応し、内側の次元が に対応する 2D リストとして指定できます。 <span class="pre">`synsPerConn`</span>。

<a href="_images/multisyn_1.png" class="reference internal image-reference"><img src="_images/multisyn_1.png" class="align-right" style="width: 35%;" alt="_images/multisyn_1.png" /></a>

<div class="highlight-python notranslate">

<div class="highlight">

      netParams.connParams[...] = {
              'synMech': ['AMPA', 'GABA'],
              'sec': 'dend',
              'synsPerConn': [2, 1],
              'loc': [[0.5, 0.75], [0.3]],
              'distributeSynsUniformly': False,
      # ...

</div>

</div>

例に示すように、<span class="pre">`synsPerConn`</span> 自体をリストにすることができるため、各 <span class="pre">`synMech`</span> が個別の数のシナプスに対応できることに注意してください。

- **'connList'** での使用
  さらに、**‘connList’** ベースの接続 (個々のシナプス前セルと後セルの間の接続の明示的なリスト) を使用する場合は、重み、遅延、位置、秒を最大 3 次元のリストとして記述することができます。最も外側の次元は、<span class="pre">`connList`</span> の長さ (つまり、セル間接続の数) に対応します。上で説明したのと同じロジックが、この外側のリストの各要素に適用されます。

<div class="highlight-python notranslate">

<div class="highlight">

      netParams.connParams[...] = {
              'connList': [[0,0], [1,0]],
              'synMech': ['AMPA', 'GABA'],
              'synsPerConn': 3,
              'weight': [[[1, 2, 3], [4, 5, 6]], # first conn: AMPA, GABA, 3 synsPerConn each
                              [[7, 8, 9], [10, 11, 12]]],  # second conn: AMPA, GABA (...)

              'delay': [[0.1, 0.2], # first conn: AMPA, GABA, same for all syns in synsPerConn
                              [0.3, 0.4]],  # second conn: AMPA, GABA (...)
      # ...

</div>

</div>

</div>

<div id="functions-as-strings" class="section">

<span id="function-string"></span>

### 文字列としての機能<a href="#functions-as-strings" class="headerlink" title="Link to this heading"></a>

セル、シナプス、および接続ルールのパラメーターの一部は、関数を含む文字列を使用して提供できます。文字列は NetPyNE によって内部的に解釈され、適切な <a href="https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions" class="reference external">lambda 関数 </a> に変換されます。この文字列には次の要素が含まれる場合があります。

- 数値、例: 「3.56」

- すべての Python 数学演算子: <span class="pre">`+`</span>、<span class="pre">`-`</span>、<span class="pre">`*`</span>、<span class="pre">`/`</span>、<span class="pre">`%`</span>、<span class="pre">`**`</span> (指数) など。

- Python 数学関数: <span class="pre">`sin`</span>、<span class="pre">`cos`</span>、<span class="pre">`tan`</span>、<span class="pre">`exp`</span>、<span class="pre">`sqrt`</span>、<span class="pre">`mean`</span>、<span class="pre">`inf`</span> (詳細については、<a href="https://docs.python.org/2/library/math.html" class="reference external">https://docs.python.org/2/library/math.html</a> を参照)

- NEURON h.Random() メソッド: <span class="pre">`binomial`</span>、<span class="pre">`discunif`</span>、<span class="pre">`erlang`</span>、<span class="pre">`geometric`</span>、<span class="pre">`hypergeo`</span>、<span class="pre">`lognormal`</span>、<span class="pre">`negexp`</span>、<span class="pre">`normal`</span>、 <span class="pre">`poisson`</span>、<span class="pre">`uniform`</span>、<span class="pre">`weibull`</span> (<a href="https://www.neuron.yale.edu/neuron/static/py_doc/programming/math/random.html" class="reference external">https://www.neuron.yale.edu/neuron/static/py_doc/programming/math/random.html</a> を参照)

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

- セルの位置、セル内のセグメントの位置、接続されたセル間の距離などのコンテキスト変数。このような変数の名前は事前に定義されており、関数が使用される場所に固有です (以下を参照)。

文字列としての関数は、次のモデル コンポーネントのエントリのパラメーターとして使用できます (いずれの場合も、上記の要素に加えて、関数に含めることができる特定の変数のセットがあります)。

- 接続ルールの <span class="pre">`weight`</span>、<span class="pre">`delay`</span>、<span class="pre">`probability`</span>、<span class="pre">`convergence`</span>、および <span class="pre">`divergence`</span>。使用可能な変数は次のとおりです。

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

- <span class="pre">`cellParams`</span> ディクショナリ内の <span class="pre">`mechs`</span> および <span class="pre">`pointps`</span>、セクションの <span class="pre">`geom`</span> パラメータ (<span class="pre">`pt3d`</span> を除く) のプロパティ。使用可能な変数は次のとおりです。

> <div>
  >
  > - <span class="pre">`x`</span>、<span class="pre">`y`</span>、<span class="pre">`z`</span>: セル x、y、または z の位置。
  >
  > - <span class="pre">`xnorm`</span>、<span class="pre">`ynorm`</span>、<span class="pre">`znorm`</span>: 正規化されたセル x、y、または z の位置。
  >
  > - <span class="pre">`post_dist_euclidean`</span>: ソーマの中心から指定されたセグメントまでのユークリッド距離 (<span class="pre">`CompartCell`</span> のみに意味を持ちます)
  >
  > - <span class="pre">`post_dist_path`</span>: 相馬の中心から指定されたセグメントまでの距離。トポロジカル パスに沿った中間セクションの長さの合計として定義されます (<span class="pre">`CompartCell`</span> のみに意味を持ちます)
  >
  > - カスタム セル変数。<span class="pre">`cellParams`</span> の <span class="pre">`vars`</span> 辞書でユーザーが定義できます。
  >
  > </div>

- <span class="pre">`cellParams`</span> 辞書のセル変数 (<a href="#cell-types" class="reference internal"><span class="std std-ref">セルの種類</span></a>を参照)。上記と同じ意味を持つ変数 <span class="pre">`x`</span>、<span class="pre">`y`</span>、<span class="pre">`z`</span>、<span class="pre">`xnorm`</span>、<span class="pre">`ynorm`</span>、<span class="pre">`znorm`</span> を含めることができます。

<div class="admonition note">

注記

関数として定義されたセルパラメータの <span class="pre">`mechs`</span> または <span class="pre">`pointps`</span> の各プロパティは、セクションまたはセグメントごとに評価されます。一方、セル変数の値は特定のセル インスタンスに対して 1 回取得されるため、特定のセルのすべてのセグメントについて、この変数を参照するすべての関数に同じ値が代入されます。関数にランダム分布が含まれる場合、この区別は不可欠となる可能性があります。次の例を考えてみましょう。

<span class="pre">`PYRcell['secs']['dend1']['mechs']['pas']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'g':`</span>` `<span class="pre">`'g_base`</span>` `<span class="pre">`+`</span>` `<span class="pre">`uniform(1.1e-5,`</span>` `<span class="pre">`1.2e-5)`</span>` `<span class="pre">`*`</span>` `<span class="pre">`exp(-dist_path/g_decay_const)',`</span>` `<span class="pre">`'e':`</span>` `<span class="pre">`-70}`</span>

<span class="pre">`PYRcell['vars']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'g_base':`</span>` `<span class="pre">`'normal(3.57e-5,`</span>` `<span class="pre">`1e-8)',`</span>` `<span class="pre">`'g_decay_const':`</span>` `<span class="pre">`'uniform(100,`</span>` `<span class="pre">`110)'}`</span>

g の式はセグメントごとに評価されるため、式にランダム関数が明示的に含まれている場合、セグメントごとに新しいランダム値が生成されます (同様に、dist_path などのセグメント依存変数はセグメントごとの値を取得します)。一方、その中のセル変数の値 (ここでは、g_base と g_decay_const) はセルごとに 1 回計算され、このセルのすべてのセグメントにわたって保存されます。つまり、セル変数のすべてのランダム分布はセルごとに 1 回だけ再選択されます)。

</div>

- シナプス機構の特性 (<span class="pre">`synMechParams`</span> 辞書のエントリ)。使用可能な変数は次のとおりです。

> <div>
  >
  > - <span class="pre">`post_x`</span>、<span class="pre">`post_y`</span>、<span class="pre">`post_z`</span>: シナプス後セルの x、y、または z の位置。
  >
  > - <span class="pre">`post_xnorm`</span>、<span class="pre">`post_ynorm`</span>、<span class="pre">`post_znorm`</span>: 正規化されたシナプス後セルの x、y、または z の位置。
  >
  > - <span class="pre">`post_dist_euclidean`</span>: 体細胞の中心からシナプス後細胞のシナプス位置までのユークリッド距離
  >
  > - <span class="pre">`post_dist_path`</span>: 体細胞の中心からシナプス後細胞のシナプス位置までの距離。トポロジカル パスに沿った中間セクションの長さの合計として定義されます。
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
  > > - <span class="pre">`type`</span> - シナプス再分布のタイプ。利用可能なオプション: 1Dmap、2Dmap、または距離。
  > >
  > > \[1Dmap, 2Dmap\] に <span class="pre">`type`</span> がある場合は、さらに以下を含める必要があります:
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
  > > 一方、この選択のためには、シナプス後細胞が 3D 形態を持つ必要があります。単純なセクションの場合、<span class="pre">`netParams.defineCellShapes`</span>` `<span class="pre">`=`</span>` `<span class="pre">`True`</span> を設定することで、これを自動的に生成できます (Y 軸に沿った円柱が上向き)。
  > >
  > > <span class="pre">`type`</span> が <span class="pre">`distance`</span> に設定されている場合、シナプスは参照から指定された距離 (許可されたセクション内) に再配置されます。この場合、さらに次のものが含まれる場合があります。
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
  > > > - <span class="pre">`coord`</span> (オプション) - 距離の計算に使用される座標系。省略した場合、距離は樹枝状ツリーに沿って計算されます。あるいは、ユークリッド空間内の距離 (デカルト座標系における基準からターゲット セグメントまでの距離) を計算するために「デカルト」を使用することもできます。この場合、シナプス後細胞は 3D 形態を持つ必要があります (または <span class="pre">`netParams.defineCellShapes`</span>` `<span class="pre">`=`</span>` `<span class="pre">`True`</span> を設定)。
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
  > >> > </div>
  > >
  > > </div>
  > >
  > > </div>
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
> > 関数として定義できます (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a> を参照)。刺激の場合は、シナプス後細胞のパラメーターを使用することのみが意味があることに注意してください (例: <span class="pre">`'post_ynorm'`</span>)。
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
> 関数として定義可能 (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> - **synMech** (オプション; NetStims のみ) - NetStim を接続するシナプス メカニズムのラベル
>
> - **重み** (オプション; NetStims のみ) - NetStim とセル間の接続の重み
> 関数として定義可能 (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> - **遅延** (オプション; NetStims のみ) - NetStim とセル間の接続の遅延 (デフォルト: 1)
> 関数として定義可能 (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
>
> - **synsPerConn** (オプション; NetStims のみ) - NetStim とセル間の接続のシナプスの数 (デフォルト: 1)
> 関数として定義可能 (<a href="#function-string" class="reference internal"><span class="std std-ref">文字列としての関数</span></a>を参照)
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

**細胞外刺激** - これは分散された刺激メカニズムであり、<span class="pre">`CompartCell`</span> のすべてのセクション/セグメントが関係します。この種類の刺激を指定するには、<span class="pre">`stimSourceParams`</span> で <span class="pre">`'type':`</span>` `<span class="pre">`'XStim'`</span> を設定し、いくつかのパラメーターを指定する必要があります。

> <div>
>
> - <span class="pre">`field`</span>: 刺激の特性を指定する辞書。それは以下によって構成されています:
>
> > <div>
> >
> > - <span class="pre">`class`</span>: 刺激の種類。利用可能なオプション: <span class="pre">`pointSource`</span> および <span class="pre">`uniform`</span>、それぞれ電流または均一な電界を注入する単一点電極用。
> >
> > <span class="pre">`'class':`</span>` `<span class="pre">`'pointSource'`</span> については、<span class="pre">`location`</span> (電極先端の位置) および <span class="pre">`sigma`</span> (脳組織の伝導率 (mS/mm)) を指定する必要があります。
> >
> > <span class="pre">`'class':`</span>` `<span class="pre">`'uniform'`</span> の場合、<span class="pre">`referencePoint`</span> (オプション - フィールドが 0 である点) および <span class="pre">`fieldDirection`</span> (2 つの角度のリストとしてのフィールドの方向: 極角 (0 と 180 の間) と方位角) を指定する必要があります。 -0 ～ 360-)。
> >
> > </div>
>
> - <span class="pre">`waveform`</span>: 時間変調を指定する辞書。それは以下によって構成されています:
>
> > <div>
> >
> > - <span class="pre">`type`</span>: 外部刺激の時間的形状。利用可能なオプション: <span class="pre">`sinusoidal`</span>、<span class="pre">`pulse`</span>、<span class="pre">`external`</span>。指定しない場合、外部刺激は 0 (接地) に設定されます。
> >
> > - <span class="pre">`amp`</span> (オプション): 外部刺激の振幅 (点源刺激の場合は mA、均一な電場の場合は V/m)。<span class="pre">`sinusoidal`</span> または <span class="pre">`pulse`</span> に有効です。指定しない場合は0（刺激なし）となります。
> >
> > - <span class="pre">`del`</span> (オプション): 刺激の開始時間。<span class="pre">`sinusoidal`</span> または <span class="pre">`pulse`</span> に有効です。指定しない場合はシミュレーションの開始時刻となります。
> >
> > - <span class="pre">`dur`</span> (オプション): 刺激の持続時間 (開始時間に続く)。<span class="pre">`sinusoidal`</span> または <span class="pre">`pulse`</span> に有効です。指定しない場合はシミュレーション終了時刻となります。
> >
> > - <span class="pre">`freq`</span> (オプション): <span class="pre">`sinusoidal`</span> 刺激の頻度。指定しない場合は0（刺激なし）となります。
> >
> > - <span class="pre">`time`</span> (オプション): 刺激が外部にアップロードされる場合 (<span class="pre">`type`</span>: <span class="pre">`external`</span>)、このエントリは時間のリストを含む pickle ファイル、または同じ情報を含む numpy 配列のいずれかを指定します。連続する時点間の（固定）時間間隔は、積分タイムステップと一致している必要があります。
> >
> > - <span class="pre">`signal`</span> (オプション): 刺激が外部にアップロードされる場合 (<span class="pre">`type`</span>: <span class="pre">`external`</span>)、このエントリは、<span class="pre">`time`</span> リストとペアになった外部信号の振幅 (点源刺激の場合は mA - 均一電場の場合は V/m) に対応する値のリストを含む pickle ファイル、または同じ情報を持つ numpy 配列。
> >
> > </div>
>
> - <span class="pre">`mod_based`</span>: ブール値 (デフォルト: False)。 NEURON フォーラムのガイドラインに従って、シミュレーションが外部 MOD ファイル (「ex」と呼ばれる POINTER/RANGE と「is」と呼ばれる GLOBAL を持つ xtra.mod) に基づいているかどうかを指定します。これは大規模なネットワークに適していますが、単一の時間変調に制限されます。 <span class="pre">`mod_based`</span>:False を指定すると、多くのソースの重ね合わせを設定できます。 NetPyNE 互換の <span class="pre">`xtra.mod`</span> は、<span class="pre">`support`</span> モジュールからダウンロードできます。
>
> </div>

さらに、<span class="pre">`stimSourceParams`</span> では、ターゲット細胞を満たす必要がある条件を <span class="pre">`source`</span> (細胞外刺激を指定する刺激源のラベル) と <span class="pre">`conds`</span> に設定する必要があります。 <span class="pre">`'conds':`</span>` `<span class="pre">`{'cellList':`</span>` `<span class="pre">`'all'}`</span> は、細胞外 (ユビキタス) ソースによって表される全体的な刺激を提供します。

以下のコードは、外部刺激の重ね合わせ (許可されている) の詳細な例を示しています。

<div class="highlight-python notranslate">

<div class="highlight">

    # Stimulation parameters

    ## Stimulation sources parameters
    netParams.stimSourceParams['XStim1'] =  {
            'type': 'XStim',
            'field': {'class': 'pointSource', 'location': [100,-100,0], 'sigma': 0.276},
            'waveform': {'type': 'sinusoidal', 'amp' : 0.020, 'del' : 20, 'dur' : 80, 'freq': 250}
            }

    netParams.stimSourceParams['XStim2'] =  {
            'type': 'XStim',
            'field': {'class': 'uniform', 'referencePoint': [0,-netParams.sizeY,0], 'fieldDirection': [180,0]},
            'waveform': {'type': 'pulse', 'amp' : 10.0, 'del' : 50, 'dur' : 20}
            }

    ## Stimulation target parameters
    netParams.stimTargetParams['XStim1->all'] = {
            'source': 'XStim1',
            'conds': {'cellList': 'all'}}

    netParams.stimTargetParams['XStim2->all'] = {
            'source': 'XStim2',
            'conds': {'cellList': 'all'}}

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

- **定数** - 文字列ベースの関数などでユーザーが使用する定数を指定する辞書。

各ディクショナリのパラメータは、RxD パッケージで説明されているものと同じ構造に従います: <a href="https://www.neuron.yale.edu/neuron/static/docs/rxd/index.html" class="reference external">https://www.neuron.yale.edu/neuron/static/docs/rxd/index.html</a>

使用例を参照してください: <a href="https://github.com/Neurosim-lab/netpyne/tree/development/examples/rxd_buffering" class="reference external">RxD バッファリングの例</a> および <a href="https://github.com/Neurosim-lab/netpyne/tree/development/examples/rxd_buffering" class="reference external">RxD ネットワークの例</a>。

</div>

</div>

<div id="simulation-configuration" class="section">

<span id="sim-config"></span>

## シミュレーション構成<a href="#simulation-configuration" class="headerlink" title="Link to this heading"></a>

以下は、カテゴリ別に整理されたすべてのシミュレーション構成オプション (つまり、<span class="pre">`SimConfig`</span> オブジェクトの属性) のリストです。

シミュレーションと NetPyNE フレームワークに関連するもの:

- **duration** - シミュレーションの継続時間 (ミリ秒単位) (デフォルト: 1000)

- **dt** - 使用する内部積分タイムステップ (デフォルト: 0.025)

- **hParams** - h モジュールのパラメータを含む辞書 (デフォルト: <span class="pre">`{'celsius':`</span>` `<span class="pre">`6.3,`</span>` `<span class="pre">`'v_init':`</span>` `<span class="pre">`-65.0,`</span>` `<span class="pre">`'clamp_resist':`</span>` `<span class="pre">`0.001}`</span>)

- **cache_efficient** - CVodeのcache_efficientオプションを使用して、多数のコアで実行する場合の負荷を最適化します(デフォルト: False)

- **cvode_active** - CVode 変数タイム ステップを使用します (デフォルト: False)

- **シード** - 接続性、入力刺激、およびセルの位置のランダムなシードを含む辞書 (デフォルト: <span class="pre">`{'conn':`</span>` `<span class="pre">`1,`</span>` `<span class="pre">`'stim':`</span>` `<span class="pre">`1,`</span>` `<span class="pre">`'loc':`</span>` `<span class="pre">`1}`</span>)

- **createNEURONObj** - NetPyNE ネットワーク メタデータをインスタンス化するときに、NEURON で実行可能なネットワークを作成します (デフォルト: True)

- **createPyStruct** - ネットワークをインスタンス化するときに Python 構造体を作成します (シミュレーターに依存しません) (デフォルト: True)

- **includeParamsLabel** - そのセル、conn、または stim を作成した param ルールのラベルを含めます (デフォルト: True)

- **addSynMechs** - シナプス機構を追加するかどうか (デフォルト: True)

- **gatherOnlySimData** - ネットおよびセル データの収集を省略し、gatherData 時間を短縮します (デフォルト: False)

- **compactConnFormat** - dict 形式を conns のコンパクトなリスト形式に置き換えます (含めるキーのリストを提供する必要があります) (デフォルト: False)

<!-- -->

- **connRandomSecFromList** - synsPerConn=1 (デフォルト: True) の場合でも、リストからランダムなセクション (および場所) を選択します。個々の connParams エントリに対してオーバーライドできます。詳細については、「<a href="#multisynapse-conn" class="reference internal"><span class="std std-ref">マルチシナプス接続</span></a>」を参照してください。

- **distributeSynsUniformly** - セクション リスト全体でシナプスを均一に配置します。 false の場合、セクション リストのセクションごとに 1 つの syn を配置します (デフォルト: True)。個々の connParams エントリに対してオーバーライドできます。詳細については、「<a href="#multisynapse-conn" class="reference internal"><span class="std std-ref">マルチシナプス接続</span></a>」を参照してください。

- **pt3dRelativeToCellLocation** - True \# セルの X、Y、Z 位置を基準にしてセルの 3D 点を作成します (デフォルト: True)

- **invertedYCoord** - 視覚化したときに深さを表すように y 軸座標を負にします (上部が 0) (デフォルト: True)

- **allowSelfConns** - セルからセル自体への接続を許可します (デフォルト: False)

- **oneSynPerNetcon** - NetCon ごとに 1 つの個別のシナプス オブジェクトを作成します (False の場合、同じシナプスを共有できます) (デフォルト: True)

- **saveCellSecs** - 各セルのすべてのセクション情報を保存します。時間と空間を削減します (デフォルト: False)

- **saveCellConns** - 各セルのすべての conns 情報を保存します。時間と空間を削減します (デフォルト: False)

- **timing** - 各プロセスのタイミングを表示および記録します (デフォルト: True)

- **saveTiming** - タイミング データを pickle ファイルに保存します (デフォルト: False)

- **printRunTime** - ここで指定した間隔 (秒) での印刷実行時間 (例: 0.1) (デフォルト: False)

- **printPopAvgRates** - 実行後の母集団の平均発火率を出力します (デフォルト: False)

- **printSynsAfterRule** - 各 conn ルールが適用された後の合計接続数を出力します。

- **verbose** - 詳細メッセージを表示します (デフォルト: False)

録音に関連するもの:

- **recordCells** - トレースを記録するセルのリスト。セル gid (例: <span class="pre">`5`</span> または <span class="pre">`[2,`</span>` `<span class="pre">`3]`</span>)、集団ラベル (例: 「S」集団の 1 つのセルから記録する場合は <span class="pre">`'S'`</span>)、またはすべてのセルから記録する場合は <span class="pre">`'all'`</span> を含めることができます。注: <span class="pre">`simConfig.analysis['plotTraces']`</span> の <span class="pre">`include`</span> 引数で選択されたすべてのセルは、自動的に <span class="pre">`recordCells`</span> に組み込まれます。 (デフォルト: <span class="pre">`[]`</span>)

- **recordTraces** - 記録するトレースの辞書 (デフォルト: {} ; 例: {‘V_soma’:{‘sec’:’soma’,’loc’:0.5,’var’:’v’}})

- **recordSpikesGids** - スパイク時間を記録するセルのリスト (すべてから記録するには -1)。セル gid (例: 5)、集団ラベル (例: 「S」集団の 1 つのセルから記録する場合は「S」)、またはすべてのセルから記録する場合は「all」を含めることができます。 (デフォルト: -1)

- **recordStim** - セルスティムのスパイクを記録します (デフォルト: False)

- **recordLFP** - 局所電界電位 (LFP) 電極の 3D 位置。 \[\[50, 100, 50\], \[50, 200, 50\]\] (y 座標は深さを表すため、プロットすると負の値として表されることに注意してください)。各電極の LFP 信号は、「線源近似」を使用し、導電率シグマ = 0.3 mS/mm のオーム媒質を想定して計算された、各神経セグメントによって寄与される細胞外電位を合計することによって得られます。 <span class="pre">`sim.allSimData['LFP']`</span> に格納されます。 (デフォルト: False)。

- **saveLFPCells** - 各セルによって個別に生成された LFP を <span class="pre">`sim.allSimData['LFPCells']`</span> に保存します。保存するセルのサブセットを選択できます。例: \[3, ‘PYR’, (‘PV2’, 5)\] (デフォルト: False)。

- **saveLFPPops** - 各集団によって生成された LFP を <span class="pre">`sim.allSimData['LFPPops']`</span> に保存します。保存する母集団のサブセットを選択できます。 \['PYR', 'PV2'\] (デフォルト: False)。

- **saveIMembrane** - 各セルの各セグメントからの LFP に寄与する膜貫通電流を保存します。 <span class="pre">`sim.allSimData['iMembrane']`</span> に格納されます。保存するセルのサブセットを選択できます。 \[3, ‘PYR’, (‘PV2’, 5)\] (デフォルト: False)。

- **recordStep** - データ記録のステップ サイズ (ミリ秒) (デフォルト: 0.1)

ファイル保存に関連するもの:

- **saveDataInclude** - ファイルに保存するデータ構造 (デフォルト: \['netParams', 'netCells', 'netPops', 'simConfig', 'simData'\])

- **simLabel** - シミュレーションの名前 (何も指定されていない場合はファイル名として使用されます) (デフォルト: '')

- **saveFolder** - 出力データを保存するパス (デフォルト: '')

- **filename** - モデル出力を保存するファイルの名前 (デフォルト: 'model_output')

- **timestampFilename** - 上書きを避けるためにファイル名にタイムスタンプを追加します (デフォルト: False)

- **savePickle** - データを pickle ファイルに保存します (デフォルト: False)

- **saveJson** - dat を json ファイルに保存します (デフォルト: False)

- **saveMat** - データをマット ファイルに保存します (デフォルト: False)

- **saveTxt** - データを txt ファイルに保存します (デフォルト: False)

- **saveDpk** - データを .dpk ピクルス ファイルに保存します (デフォルト: False)

- **saveHDF5** - HDF5 ファイルに保存するデータを保存します (デフォルト: False)

- **backupCfgFile** - cfg ファイルをフォルダーにコピーします。 \[‘cfg.py’, ‘backupcfg/’\] (デフォルト: \[\])

プロットと分析に関連するもの:

- **分析** - 各項目が <span class="pre">`analysis`</span> モジュールからの関数の呼び出しを表すディクショナリ。関数のリストは、\`\`sim.analysis.plotData()\`\` 関数を呼び出した後に実行されます。この関数は、いくつかのラッパー (<span class="pre">`sim.createSimulateAnalyze()`</span> など) の最後にすでに含まれています。

> <div>
  >
  > 辞書キーは関数名を表し、値は <span class="pre">`True`</span> または関数 <span class="pre">`kwargs`</span> を含む辞書に設定できます。つまり、<span class="pre">`simConfig.analysis[funcName]`</span>` `<span class="pre">`=`</span>` `<span class="pre">`kwargs`</span>
  >
  > 例: <span class="pre">`simConfig.analysis['plotRaster']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`True`</span> は、<span class="pre">`sim.analysis.plotRaster()`</span> を呼び出すことと同じです。
  >
  > 例: <span class="pre">`simConfig.analysis['plotRaster']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'include':`</span>` `<span class="pre">`['PYR'],`</span>` `<span class="pre">`'timeRange':`</span>` `<span class="pre">`[200,600],`</span>` `<span class="pre">`'saveFig':`</span>` `<span class="pre">`'PYR_raster.png'}`</span> <span class="pre">`sim.analysis.plotRaster(include=['PYR'],`</span>` `<span class="pre">`timeRange=[200,600],`</span>` `<span class="pre">`saveFig='PYR_raster.png')`</span> を呼び出すことと同じです
  >
  > simConfig オブジェクトにはメソッド <span class="pre">`addAnalysis(func,`</span>` `<span class="pre">`params)`</span> も含まれており、これにはパラメータの構文をチェックする利点があります (例: <span class="pre">`simConfig.addAnalysis('plotRaster',`</span>` `<span class="pre">`{'include':`</span>` `<span class="pre">`['PYR'],`</span>` `<span class="pre">`'timeRage':`</span>` `<span class="pre">`[200,600]})`</span>)
  >
  > 利用可能な分析関数には、<span class="pre">`plotRaster`</span>、<span class="pre">`plotSpikeHist`</span>、<span class="pre">`plotTraces`</span>、<span class="pre">`plotConn`</span>、および <span class="pre">`plot2Dnet`</span> が含まれます。各関数とその引数の詳細な説明は、<a href="#analysis-functions" class="reference internal"><span class="std std-ref">分析関連関数</span></a> で参照できます。
  >
  > </div>

</div>

<div id="recording-configuration" class="section">

<span id="rec-config"></span>

## 録画構成<a href="#recording-configuration" class="headerlink" title="Link to this heading"></a>

任意のまたはすべてのセルからさまざまなトレースを記録できます。セルからのトレースを記録するには、simConfig で 2 つのパラメーター、<span class="pre">`recordCells`</span> および <span class="pre">`recordTraces`</span> を設定する必要があります。

<div id="simconfig-recordcells" class="section">

### simConfig.recordCells<a href="#simconfig-recordcells" class="headerlink" title="Link to this heading"></a>

<span class="pre">`recordCells`</span> リストは、どのセルからトレースを記録するかを指定します。 <span class="pre">`recordCells`</span> には、セル gid および/または集団ラベルを任意の組み合わせで含めることができます。また、<span class="pre">`['all']`</span> に設定してすべてのセルから記録することもできます。このリストで指定されたセルのみに、そこから記録されるトレースが含まれます。 (便宜上、<span class="pre">`simConfig.analysis['plotTraces']`</span> の <span class="pre">`include`</span> パラメータで指定されたセルはすべて <span class="pre">`recordCells`</span> に自動的に追加されることに注意してください。)

**例**

<div class="highlight-python notranslate">

<div class="highlight">

    # record from all cells
    simConfig.recordCells = ['all']

    # record from cell 0 and cell 20
    simConfig.recordCells = [0, 20]

    # record from all cells in the population 'S'
    simConfig.recordCells = ['S']

    # record from all cells in the population 'M' and cells 0 and 20
    simConfig.recordCells = ['M', 0, 20]

    # record from the first cell in populations 'M' and 'S'
    simConfig.recordCells = [('M', [0]), ('S', [0])]

</div>

</div>

記録するセルを指定したら、何を記録するかを指定する必要があります。

</div>

<div id="simconfig-recordtraces" class="section">

### simConfig.recordTraces<a href="#simconfig-recordtraces" class="headerlink" title="Link to this heading"></a>

<span class="pre">`recordTraces`</span> 辞書は、どのトレースを記録するかを指定します (また、「条件」を使用する場合は、<span class="pre">`recordCells`</span> 内のどのセルのサブセットからトレースを記録するかも指定します)。 <span class="pre">`recordTraces`</span> の各エントリは辞書でもあり、そのキーはトレースの名前 (選択できる任意の文字列) であり、その値は目的のトレースの仕様を含む辞書です。

<span class="pre">`recordTraces`</span> の各エントリでは、キーがトレースの名前になり、値は記録するトレースの詳細を指定し、オプションでトレースを記録するセルの条件を設定する別の辞書になります。

**フォーマットの概要**

- **セクション変数** (例: <span class="pre">`soma(0.5).v`</span>):

<div class="highlight-python notranslate">

<div class="highlight">

    {"sec": [string], "loc": [float], "var": [string]}

</div>

</div>

- **分散メカニズム変数** (例: <span class="pre">`soma(0.5).hh.gna`</span>):

<div class="highlight-python notranslate">

<div class="highlight">

    {"sec": [string], "loc": [float], "mech": [string], "var": [string]}

</div>

</div>

- **シナプスメカニズム変数** (例: <span class="pre">`dend(1.0).AMPA._ref_g`</span>):

<div class="highlight-python notranslate">

<div class="highlight">

    {"sec": [string], "loc": [float], "synMech": [string], "var": [string]}

</div>

</div>

- **刺激変数** (例: <span class="pre">`cells[0].stims[0]['hObj'].i`</span>):

<div class="highlight-python notranslate">

<div class="highlight">

    {"sec": [string], "loc": [float], "stim": [string], "var": [string]}

</div>

</div>

- **ポイントプロセス変数** (例: <span class="pre">`soma.myPP.i`</span>):

<div class="highlight-python notranslate">

<div class="highlight">

    {"sec": [string], "pointp": [string], "var": [string]}

</div>

</div>

一般に、セクション (「sec」)、そのセクション内の場所 (「loc」)、およびその場所に記録する NEURON 変数 (「var」) を指定する必要があります。たとえば、次のコードは体細胞の中心の電圧 (NEURON の「v」) を記録します。

**例**

<div class="highlight-python notranslate">

<div class="highlight">

    # record voltage at the center of the 'soma' section
    simConfig.recordTraces['soma_voltage'] = { "sec": "soma", "loc": 0.5, "var": "v"}

    # record the sodium concentration at the distal end of the 'dend' section
    simConfig.recordTraces['dend_Na'] =  { "sec": "dend", "loc": 1.0, "var": "nai"}

    # record the potassium current at the proximal end of the first 'branch' section (branch[0])
    simConfig.recordTraces['branch0_iK'] = {"sec": "branch_0", "loc": 0.0, "var": "ik"}

</div>

</div>

上記の例では、<span class="pre">`recordCells`</span> 内のすべてのセルからトレースを記録しようとします。記録されるセルのサブセットのみからトレースを記録する場合は、トレース ディクショナリに <span class="pre">`'conds'`</span> ディクショナリを含めることによって条件を設定できます。使用可能な条件には、<span class="pre">`'gid'`</span> (セルのグローバル識別番号)、<span class="pre">`'pop'`</span> (集団の名前または名前のリスト)、<span class="pre">`'cellType'`</span> (セルのタイプの文字列名)、および <span class="pre">`'cellList'`</span> (セル gid のリスト) が含まれます。

**条件の例**

<div class="highlight-python notranslate">

<div class="highlight">

    # only record this trace from cell 0
    simConfig.recordTraces['trace_name'] = {'conds': {'gid': [0]}, ... }

    # only record this trace from populations 'M' and 'S'
    simConfig.recordTraces['trace_name'] = {'conds': {'pop': ['M', 'S']}, ... }

    # only record this trace from cells tagged with cellType as 'pyr'
    simConfig.recordTraces['trace_name'] = {'conds': {'cellType': ['pyr']}, ... }

</div>

</div>

特定のセクションと場所から、電圧、電流、濃度などのセクション変数を記録できます。 NEURON メカニズム (「mech」)、シナプス メカニズム (「synMech」)、および刺激 (「stim」) からの変数を記録することもできます。

**メカニズムからの記録の例**

<div class="highlight-python notranslate">

<div class="highlight">

    # record the 'gna' variable (sodium conductance) in the 'hh' (Hodgkin-Huxley) mechanism
    # located in the middle of the 'soma' section.  This is equivalent to recording
    # soma(0.5).hh._ref_gna in NEURON.
    simConfig.recordTraces['gNa'] = {'sec': 'soma', 'loc': 0.5, 'mech': 'hh', 'var': 'gna'}

    # record the 'g' variable (conductance) in the 'AMPA' synaptic mechanism located at the
    # distal end of the 'dend' section.  This is equivalent to recording
    # dend(1.0).AMPA._ref_g in NEURON.
    simConfig.recordTraces['gAMPA'] = {'sec': 'dend', 'loc': 1.0, 'synMech': 'AMPA', 'var': 'g'}

    # record the 'i' variable (current) from the 'IClamp0' stimulation source located in the
    # middle of the 'soma' section in cell 0.  This is equivalent to recording
    # cells[0].stims[0]['hObj'].i in NEURON.
    simConfig.recordTraces['iStim'] = {'sec': 'soma', 'loc': 0.5, 'stim': 'IClamp0', 'var': 'i', 'conds': {'gid': 0}}

    # record the 'V' variable from the 'myPP' point process in the 'soma' section.  This
    # is equivalent to recording soma.myPP.V in NEURON.
    simConfig.recordTraces['VmyPP'] = {'sec': 'soma', 'pointp': 'myPP', 'var': 'V'}

    ## Recording from Synaptic Currents Mechanisms

    # Example of recording from an excitatory synaptic mechanism
    # record the 'i' variable (current) from an excitatory synaptic mechanism located
    # in the middle of the 'dend' section. This is equivalent to recording
    # dend(0.5).exc._ref_i in NEURON.
    simConfig.recordTraces['iExcSyn'] = {'sec': 'dend',  'loc': 0.5, 'synMech': 'exc',  'var': 'i'}

    # Example of recording from an inhibitory synaptic mechanism
    # record the 'i' variable (current) from an inhibitory synaptic mechanism located
    # at 0.3 of the 'soma' section. This is equivalent to recording
    # soma(0.3).inh._ref_i in NEURON.
    simConfig.recordTraces['iInhSyn'] = {'sec': 'soma', 'loc': 0.3, 'synMech': 'inh',  'var': 'i'}

    # Example of recording multiple synaptic currents
    # Recording synaptic currents
    simConfig.recordSynapticCurrents = True
    synaptic_curr = [
            ('AMPA', 'i'),   # Excitatory synaptic current
            ('NMDA', 'i'),   # Excitatory synaptic current
            ('GABA_A', 'i')  # Inhibitory synaptic current
    ]
    if simConfig.recordSynapticCurrents:
    for syn_curr in synaptic_curr:
            trace_label = f'i__soma_0__{syn_curr[0]}__{syn_curr[1]}'
            simConfig.recordTraces.update({trace_label: {'sec': 'soma_0', 'loc': 0.5, 'mech': syn_curr[0], 'var': syn_curr[1]}})

</div>

</div>

名前 <span class="pre">`'iExcSyn'`</span> 、 <span class="pre">`'iInhSyn'`</span> 、 <span class="pre">`'AMPA'`</span> 、 <span class="pre">`'NMDA'`</span> 、 <span class="pre">`'GABA_A'`</span> は、 <span class="pre">`netParams.synMechParams`</span> でユーザーによって定義された名前であり、 <span class="pre">`netParams.synMechParams.keys()`</span> を使用して見つけることができます。 <span class="pre">`synaptic_curr`</span> タプル内のシナプス メカニズムと組み合わせることができる変数は、そのシナプス メカニズムの定義に使用される MOD ファイルを調べることで見つけることができ、記録できる変数は MOD ファイル内で <span class="pre">`RANGE`</span> タイプとして定義されます。

例：

- <span class="pre">`netParams.synMechParamsas`</span> で <span class="pre">`MyExp2SynBB.mod`</span> テンプレートを使用する <span class="pre">`'AMPA'`</span> として定義されたシナプス メカニズム。

> <div>
  >
  > - ユーザーは、ソース <span class="pre">`/mod`</span> フォルダーに移動し、<span class="pre">`MyExp2SynBB.mod`</span> ファイルを開いて、どの変数が <span class="pre">`RANGE`</span> として定義されているかを確認し、それらを記録できます。
  >
  > - ユーザーは変数の型を変更して <span class="pre">`RANGE`</span> として定義し、メカニズムを再コンパイルして netpyne で記録できるようにすることもできます。
  >
  > </div>

- 特定のファイルに記録できる変数の例

> <div>
  >
  > - ユーザーは、<span class="pre">`'tau1'`</span>、<span class="pre">`'tau2'`</span>、<span class="pre">`'e'`</span>、<span class="pre">`'i'`</span>、<span class="pre">`'g'`</span>、<span class="pre">`'Vwt'`</span>、<span class="pre">`'gmax'`</span> を記録できます。
  >
  > </div>

<div class="highlight-python notranslate">

<div class="highlight">

    NEURON {
      POINT_PROCESS MyExp2SynBB
      RANGE tau1, tau2, e, i, g, Vwt, gmax
      NONSPECIFIC_CURRENT i
    }

</div>

</div>

これらは <span class="pre">`synaptic_curr`</span> で次のように指定する必要があります。

<div class="highlight-python notranslate">

<div class="highlight">

    synaptic_curr = [
    ('AMPA', 'i'),    # Excitatory synaptic current
    ('AMPA', 'g'),    # Channel conductance
    ]

</div>

</div>

</div>

</div>

<div id="package-functions" class="section">

<span id="id2"></span>

## パッケージ関数<a href="#package-functions" class="headerlink" title="Link to this heading"></a>

<span class="pre">`simConfig`</span> オブジェクトと <span class="pre">`netParams`</span> オブジェクトを作成したら、パッケージ関数を使用してネットワークをインスタンス化し、シミュレートし、分析できます。利用可能な機能の一覧を以下に示します。

<div id="simulation-related-functions" class="section">

### シミュレーション関連関数<a href="#simulation-related-functions" class="headerlink" title="Link to this heading"></a>

ラッパー:

- **sim.create(simConfig, netParams)** - 初期化、ネットワークの作成、および記録のセットアップのためのラッパー。

- **sim.simulate()** - シミュレーションを実行してデータを収集するラッパー。

- **sim.analyze()** - データを保存してプロットするラッパー。

- **sim.load(filename)** - 初期化し、ファイルからネットをロードし、記録をセットアップするラッパー。

- **sim.createSimulate(simConfig, netParams)** - ネットワークを作成およびシミュレートするラッパー。

- **sim.createSimulateAnalyze(simConfig, netParams)** - ネットワークを作成、シミュレート、分​​析するためのラッパー。

- **sim.intervalCreateSimulateAnalyze(simConfig, cfg, interval=t)** - ネットワークを作成、シミュレート、分​​析するためのラッパーで、シミュレーション出力を t ミリ秒ごとに保存します。

- **sim.createExportNeuroML2(simConfig, netParams)** - ネットワークを作成して NeuroML2 にエクスポートするラッパー。

- **sim.loadSimulate(simConfig, netParams)** - ネットワークをロードしてシミュレートするラッパー。

- **sim.loadSimulateAnalyze(simConfig, netParams)** - ネットワークをロード、シミュレート、分​​析するラッパー。

初期化とセットアップ:

- **sim.initialize(simConfig, netParams)**

- **sim.setNet(ネット)**

- **sim.setNetParams(params)**

- **sim.setSimCfg(cfg)**

- **sim.createParallelContext()**

- **sim.setupRecording()**

実行して収集します。

- **sim.runSim()**

- **sim.runSimWithIntervalFunc(間隔, 関数)**

- **sim.gatherData()**

保存とロード:

- **sim.saveData(ファイル名)**

- **sim.loadSimCfg(ファイル名)**

- **sim.loadNetParams(ファイル名)**

- **sim.loadNet(ファイル名)**

- **sim.loadSimData(ファイル名)**

- **sim.loadAll(ファイル名)**

エクスポートとインポート:

- **sim.exportNeuroML2()**

その他/ユーティリティ:

- **sim.cellByGid()**

- **sim.version()**

- **sim.gitChangeset()**

</div>

<div id="analysis-related-functions" class="section">

<span id="analysis-functions"></span>

### 分析関連機能<a href="#analysis-related-functions" class="headerlink" title="Link to this heading"></a>

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotRaster</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['allCells'\]</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">maxSpikes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100000000.0</span></span>*、 *<span class="n"><span class="pre">orderBy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'gid'</span></span>*、 *<span class="n"><span class="pre">orderInverse</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">labels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'legend'</span></span>*、 *<span class="n"><span class="pre">popRates</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">spikeHist</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">spikeHistBin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*、 *<span class="n"><span class="pre">syncLines</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">lw</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*、 *<span class="n"><span class="pre">marker</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'\|'</span></span>*、 *<span class="n"><span class="pre">markerSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*、 *<span class="n"><span class="pre">popColors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(10,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*、 *<span class="n"><span class="pre">dpi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="_modules/netpyne/analysis/mapping.html#plotRaster" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotRaster" class="headerlink" title="Link to this definition"></a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">iplotRaster</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['allCells'\]</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">maxSpikes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100000000.0</span></span>*、 *<span class="n"><span class="pre">orderBy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'gid'</span></span>*、 *<span class="n"><span class="pre">orderInverse</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">popRates</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">spikeHist</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">spikeHistBin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*、 *<span class="n"><span class="pre">syncLines</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">marker</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'circle'</span></span>*、 *<span class="n"><span class="pre">markerSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*、 *<span class="n"><span class="pre">popColors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="_modules/netpyne/analysis/interactive.html#iplotRaster" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.iplotRaster" class="headerlink" title="Link to this definition"></a>
\<short description of netpyne.analysis.interactive.iplotRaster\> に対する関数/\<short description of netpyne.analysis.interactive.iplotRaster\> への関数

パラメータ<span class="colon">:</span>
- **include** (*list*) – プロットに含めるセル。 **デフォルト:** <span class="pre">`['allCells']`</span> はすべてのセルをプロットします。 **オプション:** <span class="pre">`['all']`</span> はすべてのセルと刺激をプロットします、<span class="pre">`['allNetStims']`</span> は刺激のみをプロットします、<span class="pre">`['popName1']`</span> は単一集団をプロットします、<span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数をプロットします集団、<span class="pre">`[120]`</span> は単一のセルをプロットします、<span class="pre">`[120,`</span>` `<span class="pre">`130]`</span> は複数のセルをプロットします、<span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は特定の集団からのセルをプロットします、 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **timeRange** (*list* *\[start,* *stop\]*) – プロットする時間範囲。 **デフォルト:** <span class="pre">`None`</span> は時間範囲全体をプロットします **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **maxSpikes** (*int*) – プロットされるスパイクの最大数。 **デフォルト:** <span class="pre">`1e8`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **orderBy** (*str*) – Y 軸の順序付けに使用する一意の数値セル プロパティ。 **デフォルト:** <span class="pre">`'gid'`</span> はセル ID で並べ替えます。 **オプション:** <span class="pre">`'y'`</span> はセルの y 位置で並べ替えます。<span class="pre">`'ynorm'`</span> はセルの正規化された y 位置で並べ替えます。

- **orderInverse** (*bool*) – <span class="pre">`True`</span> の場合、y 軸の順序を反転します。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **popRates** (*bool*) – <span class="pre">`True`</span> の場合、プロットに母集団の発火率を含めます。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **spikeHist** (*bool*) – <span class="pre">`True`</span> の場合、プロットにスパイク ヒストグラム (スパイク/ビン) を含めます。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **spikeHistBin** (*int*) – スパイク ヒストグラムに使用するビンのサイズ (ミリ秒)。 **デフォルト:** <span class="pre">`5`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **syncLines** (*bool*) – 同期測定を計算し、<span class="pre">`True`</span> の場合、同期を証明するために各スパイクの垂直線をプロットします。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **マーカー** (*str*) – 各スパイクの<a href="https://docs.bokeh.org/en/latest/docs/gallery/markers.html" class="reference external">ボケマーカー</a>。 **デフォルト:** <span class="pre">`'circle'`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **markerSize** (*int*) – 各スパイクのボケ マーカーのサイズ。 **デフォルト:** <span class="pre">`3`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **popColors** (*dict*) – 各母集団 (キー) に使用されるカスタム色 (値) を含む辞書。 **デフォルト:** <span class="pre">`None`</span> は標準色を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は Figure を自動保存します。<span class="pre">`'/path/filename.html'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.html'`</span> のみです。

- **showFig** (*bool*) – <span class="pre">`True`</span> の場合の図を表示します。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **kwargs** (*\<type\>*) – \<Short description of kwargs\> **デフォルト:** *必須*

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotSpikeHist</span></span><span class="sig-paren">(</span> *<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['eachPop',</span> <span class="pre">'allCells'\]</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">binSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*、 *<span class="n"><span class="pre">graphType</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'line'</span></span>*、 *<span class="n"><span class="pre">measure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'rate'</span></span>*、 *<span class="n"><span class="pre">norm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">smooth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">filtFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">filtOrder</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*、 *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">popColors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(10,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">dpi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="_modules/netpyne/analysis/mapping.html#plotSpikeHist" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotSpikeHist" class="headerlink" title="Link to this definition"></a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotSpikeStats</span></span><span class="sig-paren">(</span> *<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['eachPop',</span> <span class="pre">'allCells'\]</span></span>*、 *<span class="n"><span class="pre">statDataIn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">{}</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">graphType</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'boxplot'</span></span>*、 *<span class="n"><span class="pre">stats</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['rate',</span> <span class="pre">'isicv'\]</span></span>*、 *<span class="n"><span class="pre">bins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">50</span></span>*、 *<span class="n"><span class="pre">histlogy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">histlogx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">histmin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*、 *<span class="n"><span class="pre">density</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">includeRate0</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">legendLabels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">normfit</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">histShading</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">xlim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">popColors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">{}</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(6,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*、 *<span class="n"><span class="pre">dpi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="_modules/netpyne/analysis/spikes_legacy.html#plotSpikeStats" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotSpikeStats" class="headerlink" title="Link to this definition"></a>
\<short description of netpyne.analysis.spikes.plotSpikeStats\> に対する関数/\<short description of netpyne.analysis.spikes.plotSpikeStats\> への関数

パラメータ<span class="colon">:</span>
- **include** (*list*) – プロットに含める母集団とセル。 **デフォルト:** <span class="pre">`['eachPop',`</span>` `<span class="pre">`'allCells']`</span> は各母集団と全体の平均のヒストグラムをプロットします **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします、<span class="pre">`['allNetStims']`</span> は刺激のみをプロットします、<span class="pre">`['popName1']`</span> は単一母集団をプロットします、 <span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。<span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>` `<span class="pre">`130]`</span> は複数のセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は、特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **statDataIn** (*dict*) – インポートする統計データの事前計算された辞書。 **デフォルト:** <span class="pre">`{}`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **timeRange** (*list* *\[start,* *stop\]*) – プロットする時間範囲。 **デフォルト:** <span class="pre">`None`</span> は時間範囲全体をプロットします **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **graphType** (*str*) – 箱ひげ図またはヒストグラムを使用して統計をプロットするかどうか。 **デフォルト:** <span class="pre">`'boxplot'`</span> **オプション:** <span class="pre">`'histogram'`</span>

- **stats** (*list*) – プロットする統計。 **デフォルト:** <span class="pre">`['rate',`</span>` `<span class="pre">`'isicv']`</span> **オプション:** <span class="pre">`['rate',`</span>` `<span class="pre">`'isicv',`</span>` `<span class="pre">`'sync',`</span>` `<span class="pre">`'pairsync']`</span>

- **bins** (*int* *or* *list*) – ヒストグラムのビン (int の場合) またはエッジ (list の場合) の数 **デフォルト:** <span class="pre">`50`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **組織学** (*bool*) – \<Short description of histlogy\> **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **histlogx** (*bool*) – x 軸を対数にするかどうか **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **histmin** (*float*) – 分析に含める最小値。 **デフォルト:** <span class="pre">`0.0`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **密度** (*bool*) – <span class="pre">`True`</span> の場合、値を密度で重み付けします **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **includeRate0** (*bool*) – ドキュメントが必要です。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **legendLabels** (*list?*) – 文書が必要です。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **normfit** (*bool*) – ドキュメントが必要です。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **histShading** (*bool*) – ドキュメントが必要です。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **xlim** (*list* *\[min,* *max\]*) – プロットの x 制限を設定します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **popColors** (*dict*) – 各母集団 (キー) に使用されるカスタム色 (値) を含む辞書。 **デフォルト:** <span class="pre">`{}`</span> は標準色を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **figSize** (*list* *\[width,* *height\]*) – Figure のサイズ (インチ単位)。 **デフォルト:** <span class="pre">`(10,`</span>` `<span class="pre">`8)`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **fontSize** (*int*) – 図のフォント サイズ。 **デフォルト:** <span class="pre">`12`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **dpi** (*int*) – 1 インチあたりのドット数で表した図の解像度。 **デフォルト:** <span class="pre">`100`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は図を自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.png'`</span>、<span class="pre">`'.jpg'`</span>、<span class="pre">`'.eps'`</span>、および <span class="pre">`'.tiff'`</span> です。

- **showFig** (*bool*) – <span class="pre">`True`</span> の場合の図を表示します。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **kwargs** (*\<type\>*) – \<Short description of kwargs\> **デフォルト:** *必須*

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotRatePSD</span></span><span class="sig-paren">(</span> *<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['eachPop',</span> <span class="pre">'allCells'\]</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">binSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*、 *<span class="n"><span class="pre">minFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*、 *<span class="n"><span class="pre">maxFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100</span></span>*、 *<span class="n"><span class="pre">transformMethod</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'morlet'</span></span>*、 *<span class="n"><span class="pre">stepFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*、 *<span class="n"><span class="pre">NFFT</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">256</span></span>*、 *<span class="n"><span class="pre">noverlap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">128</span></span>*、 *<span class="n"><span class="pre">smooth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*、 *<span class="n"><span class="pre">norm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">overlay</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">popColors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">{}</span></span>*、 *<span class="n"><span class="pre">yLogScale</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(10,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*、 *<span class="n"><span class="pre">lineWidth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.5</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>* <span class="sig-paren">)</span><a href="_modules/netpyne/analysis/spikes_legacy.html#plotRatePSD" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotRatePSD" class="headerlink" title="Link to this definition"></a>
\<short description of netpyne.analysis.spikes.plotRatePSD\> に対する関数/\<short description of netpyne.analysis.spikes.plotRatePSD\> への関数

パラメータ<span class="colon">:</span>
- **include** (*list*) – プロットに含める母集団とセル。 **デフォルト:** <span class="pre">`['eachPop',`</span>` `<span class="pre">`'allCells']`</span> は各母集団と全体の平均のヒストグラムをプロットします **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします、<span class="pre">`['allNetStims']`</span> は刺激のみをプロットします、<span class="pre">`['popName1']`</span> は単一母集団をプロットします、 <span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。<span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>` `<span class="pre">`130]`</span> は複数のセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は、特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **timeRange** (*list* *\[start,* *stop\]*) – プロットする時間範囲。 **デフォルト:** <span class="pre">`None`</span> は時間範囲全体をプロットします **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **binSize** (*int*) – スパイク ビンのサイズ (ミリ秒)。 **デフォルト:** <span class="pre">`5`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **minFreq** (*float*) – プロットに表示する最小周波数。 **デフォルト:** <span class="pre">`1`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **maxFreq** (*float*) – プロットに表示する最大周波数。 **デフォルト:** <span class="pre">`100`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **transformMethod** (*str*) – 変換方法を設定します。 **デフォルト:** <span class="pre">`'morlet'`</span> **オプション:** <span class="pre">`'fft'`</span>

- **stepFreq** (*float*) – Morlet 変換のステップ周波数。 **デフォルト:** <span class="pre">`1`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **NFFT** (*int*) – FFT の各ブロックで使用されるデータ ポイントの数 (2 の累乗) **デフォルト:** <span class="pre">`256`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **noverlap** (*int*) – FFT 変換で noverlap を設定します。 **デフォルト:** <span class="pre">`128`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **smooth** (*int*) – スムージング用のウィンドウ サイズ。 <span class="pre">`0`</span> の場合は平滑化なし。 **デフォルト:** <span class="pre">`0`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **norm** (*bool*) – 電力を正規化します。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **overlay** (*bool*) – プロットをオーバーレイするかサブプロットを使用するか。 **デフォルト:** <span class="pre">`True`</span> はプロットをオーバーレイします。 **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **popColors** (*dict*) – 各母集団 (キー) に使用されるカスタム色 (値) を含む辞書。 **デフォルト:** <span class="pre">`None`</span> は標準色を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **yLogScale** (*bool*) – True の場合、電力は対数スケール (dB) で表されます。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **ylim** (*list* *\[min,* *max\]*) – プロットの y 範囲を設定します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **figSize** (*list* *\[width,* *height\]*) – Figure のサイズ (インチ単位)。 **デフォルト:** <span class="pre">`(10,`</span>` `<span class="pre">`8)`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **fontSize** (*int*) – 図のフォント サイズ。 **デフォルト:** <span class="pre">`12`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **lineWidth** (*float*) – プロット内の線の幅。 **デフォルト:** <span class="pre">`1.5`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は図を自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.png'`</span>、<span class="pre">`'.jpg'`</span>、<span class="pre">`'.eps'`</span>、および <span class="pre">`'.tiff'`</span> です。

- **showFig** (*bool*) – <span class="pre">`True`</span> の場合の図を表示します。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotTraces</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">oneFigPer</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'cell'</span></span>*、 *<span class="n"><span class="pre">rerun</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">title</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">subtitles</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">overlay</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">colors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">ylim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">scaleBarLoc</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(10,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>* <span class="sig-paren">)</span><a href="_modules/netpyne/analysis/traces.html#plotTraces" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotTraces" class="headerlink" title="Link to this definition"></a>
\<short description of netpyne.analysis.traces.plotTraces\> に対する関数/\<short description of netpyne.analysis.traces.plotTraces\> への関数

パラメータ<span class="colon">:</span>
- **include** (*list*) – プロットに含める母集団とセル。 **デフォルト:** <span class="pre">`['eachPop',`</span>` `<span class="pre">`'allCells']`</span> は各母集団と全体の平均のヒストグラムをプロットします **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします、<span class="pre">`['allNetStims']`</span> は刺激のみをプロットします、<span class="pre">`['popName1']`</span> は単一母集団をプロットします、 <span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。<span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>` `<span class="pre">`130]`</span> は複数のセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は、特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **timeRange** (*list* *\[start,* *stop\]*) – プロットする時間範囲。 **デフォルト:** <span class="pre">`None`</span> は時間範囲全体をプロットします **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **oneFigPer** (*str*) – セルごと (複数のトレースを表示) またはトレースごと (複数のセルを表示) に 1 つの図をプロットするかどうか。 **デフォルト:** <span class="pre">`'cell'`</span> **オプション:** <span class="pre">`'trace'`</span>

- **rerun** (*bool*) – シミュレーションを再実行して、新しいセルのセットが記録されます。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **title** (*str*) – 図全体のタイトルを設定します。<span class="pre">`oneFigPer='cell'`</span> でのみ機能します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **overlay** (*bool*) – プロットをオーバーレイするかサブプロットを使用するか。 **デフォルト:** <span class="pre">`True`</span> はプロットをオーバーレイします。 **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **colors** (*list*) – トレースに使用する正規化された RGB カラーのリスト。 **デフォルト:** <span class="pre">`None`</span> は標準色を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **ylim** (*list* *\[min,* *max\]*) – プロットの y 範囲を設定します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **axis** (*bool*) – 軸を表示するかどうか。そうでない場合は、スケールバーが含まれます。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **scaleBarLoc** (*int*) – スケール バーの位置を設定します (axis=False の場合に追加されます)。 **デフォルト:** <span class="pre">`1`</span> **オプション:** <span class="pre">`1`</span> 右上、<span class="pre">`2`</span> 左上、<span class="pre">`3`</span> 左下、<span class="pre">`4`</span> 右下、<span class="pre">`5`</span> 右、<span class="pre">`6`</span> 中央左、<span class="pre">`7`</span>中央右、<span class="pre">`8`</span> 中央下、<span class="pre">`9`</span> 中央上、<span class="pre">`10`</span> 中央

- **figSize** (*list* *\[width,* *height\]*) – Figure のサイズ (インチ単位)。 **デフォルト:** <span class="pre">`(10,`</span>` `<span class="pre">`8)`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **fontSize** (*int*) – 図のフォント サイズ。 **デフォルト:** <span class="pre">`12`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は図を自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.png'`</span>、<span class="pre">`'.jpg'`</span>、<span class="pre">`'.eps'`</span>、および <span class="pre">`'.tiff'`</span> です。

- **showFig** (*bool*) – <span class="pre">`True`</span> の場合の図を表示します。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotLFP</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">electrodes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['avg',</span> <span class="pre">'all'\]</span></span>*、 *<span class="n"><span class="pre">pop</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">plots</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['timeSeries',</span> <span class="pre">'PSD',</span> <span class="pre">'spectrogram',</span> <span class="pre">'locations'\]</span></span>*、 *<span class="n"><span class="pre">inputLFP</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">NFFT</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">256</span></span>*、 *<span class="n"><span class="pre">noverlap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">128</span></span>*、 *<span class="n"><span class="pre">nperseg</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">256</span></span>*、 *<span class="n"><span class="pre">minFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*、 *<span class="n"><span class="pre">maxFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">100</span></span>*、 *<span class="n"><span class="pre">stepFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*、 *<span class="n"><span class="pre">smooth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*、 *<span class="n"><span class="pre">separation</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span>*、 *<span class="n"><span class="pre">includeAxon</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">logx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">logy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">normSignal</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">normPSD</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">normSpec</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">filtFreq</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">filtOrder</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*、 *<span class="n"><span class="pre">detrend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">transformMethod</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'morlet'</span></span>*、 *<span class="n"><span class="pre">maxPlots</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8</span></span>*、 *<span class="n"><span class="pre">overlay</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">colors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(8,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">14</span></span>*、 *<span class="n"><span class="pre">lineWidth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.5</span></span>*、 *<span class="n"><span class="pre">dpi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">200</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>* <span class="sig-paren">)</span><a href="_modules/netpyne/analysis/mapping.html#plotLFP" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotLFP" class="headerlink" title="Link to this definition"></a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotShape</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">includePre</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['all'\]</span></span>*、 *<span class="n"><span class="pre">includePost</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['all'\]</span></span>*、 *<span class="n"><span class="pre">showSyns</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">showElectrodes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">synStyle</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'.'</span></span>*、 *<span class="n"><span class="pre">synSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3</span></span>*、 *<span class="n"><span class="pre">synColor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'red'</span></span>*、 *<span class="n"><span class="pre">dist</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.6</span></span>*、 *<span class="n"><span class="pre">elev</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">90</span></span>*、 *<span class="n"><span class="pre">azim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-90</span></span>*、 *<span class="n"><span class="pre">cvar</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">cvals</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">clim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">iv</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">ivprops</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">includeAxon</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">bkgColor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">aspect</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'auto'</span></span>*、 *<span class="n"><span class="pre">axisLabels</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">kind</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'shape'</span></span>*、 *<span class="n"><span class="pre">returnPlotter</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">dpi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*、 *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="_modules/netpyne/plotting/plotShape.html#plotShape" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotShape" class="headerlink" title="Link to this definition"></a>
ネットワークの形態をプロットする関数\>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plotConn</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">includePre</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['all'\]</span></span>*、 *<span class="n"><span class="pre">includePost</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['all'\]</span></span>*、 *<span class="n"><span class="pre">feature</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'strength'</span></span>*、 *<span class="n"><span class="pre">orderBy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'gid'</span></span>*、 *<span class="n"><span class="pre">groupBy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pop'</span></span>*、 *<span class="n"><span class="pre">groupByIntervalPre</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">groupByIntervalPost</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">graphType</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'matrix'</span></span>*、 *<span class="n"><span class="pre">removeWeightNorm</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">synOrConn</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'syn'</span></span>*、 *<span class="n"><span class="pre">synMech</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">connsFile</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">tagsFile</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">clim</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(8,</span> <span class="pre">8)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">logPlot</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>* <span class="sig-paren">)</span><a href="_modules/netpyne/analysis/network.html#plotConn" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plotConn" class="headerlink" title="Link to this definition"></a>
\<short description of netpyne.analysis.network.plotConn\> に対する関数/\<short description of netpyne.analysis.network.plotConn\> への関数

パラメータ<span class="colon">:</span>
- **includePre** (*list*) – 含めるシナプス前細胞のリスト。 **デフォルト:** <span class="pre">`['all']`</span> **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします。<span class="pre">`['allNetStims']`</span> は刺激のみをプロットします。<span class="pre">`['popName1']`</span> は単一集団をプロットします。<span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。 <span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>` `<span class="pre">`130]`</span> は複数のセルをプロットします。<span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **includePost** (*list*) – 含めるシナプス後セルのリスト。 **デフォルト:** <span class="pre">`['all']`</span> **オプション:** includePre と同じ

- **feature** (*str*) – 接続プロットに表示するフィーチャ。 <span class="pre">`groupBy='cell'`</span> に適用できるフィーチャーは、<span class="pre">`'weight'`</span>、<span class="pre">`'delay'`</span>、および <span class="pre">`'numConns'`</span> のみです。 **デフォルト:** <span class="pre">`'strength'`</span> **オプション:** <span class="pre">`'weight'`</span> 接続の重み、<span class="pre">`'delay'`</span> 接続の遅延、<span class="pre">`'numConns'`</span> 接続の数、<span class="pre">`'probability'`</span> 接続の確率、<span class="pre">`'strength'`</span> 重み \* 確率、<span class="pre">`'convergence'`</span> の接続数シナプス後細胞あたりのシナプス前細胞、<span class="pre">`'divergence'`</span> シナプス前細胞あたりのシナプス後細胞の数

- **orderBy** (*str*) – x 軸と y 軸の順序を決定するための一意の数値セル プロパティ。 **デフォルト:** <span class="pre">`'gid'`</span> **オプション:** <span class="pre">`'gid'`</span>、<span class="pre">`'y'`</span>、<span class="pre">`'ynorm'`</span>

- **groupBy** (*str*) – 集団、個々のセル、または <span class="pre">`'y'`</span> などの他の数値タグによる接続性をプロットします。 **デフォルト:** <span class="pre">`'pop'`</span> **オプション:** <span class="pre">`'pop'`</span>、<span class="pre">`'cell'`</span>、<span class="pre">`'y'`</span>

- **groupByIntervalPre** (*int* *or* *float*) – 接続プロットでシナプス前細胞をグループ化するための groupBy 機能の間隔。 <span class="pre">`100`</span> は、皮質深さによって 100 um 単位でグループ化します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **groupByIntervalPost** (*int* *or* *float*) – 接続プロットでシナプス後細胞をグループ化するための groupBy 機能の間隔。 <span class="pre">`100`</span> は、皮質深さによって 100 um 単位でグループ化します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **graphType** (*str*) – データを表すグラフのタイプ。 **デフォルト:** <span class="pre">`'matrix'`</span> **オプション:** <span class="pre">`'matrix'`</span>、<span class="pre">`'bar'`</span>、<span class="pre">`'pie'`</span>

- **removeWeightNorm** (*bool*) – **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **synOrConn** (*str*) – シナプスまたは接続を使用します。 1 つの接続に複数のシナプスを含めることができることに注意してください。 **デフォルト:** <span class="pre">`'syn'`</span> **オプション:** <span class="pre">`'syn'`</span>、<span class="pre">`'conn'`</span>

- **synMech** (*list*) – これらのシナプス機構の結果のみを表示します。 <span class="pre">`['AMPA',`</span>` `<span class="pre">`'GABAA',`</span>` `<span class="pre">`...]`</span>。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **connsFile** (*str*) – プロット元の接続の保存データ ファイルへのパス。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **tagsFile** (*str*) – 接続プロットで使用する保存されたタグ ファイルへのパス。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **clim** (*list* *\[min,* *max\]*) – カラーバーの制限の数値のリスト。 **デフォルト:** <span class="pre">`None`</span> は接続マトリックスの最小値と最大値を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **figSize** (*list* *\[width,* *height\]*) – Figure のサイズ (インチ単位)。 **デフォルト:** <span class="pre">`(8,`</span>` `<span class="pre">`8)`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **fontSize** (*int*) – 図のフォント サイズ。 **デフォルト:** <span class="pre">`12`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は図を自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.png'`</span>、<span class="pre">`'.jpg'`</span>、<span class="pre">`'.eps'`</span>、および <span class="pre">`'.tiff'`</span> です。

- **showFig** (*bool*) – <span class="pre">`True`</span> の場合の図を表示します。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">plot2Dnet</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">include</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\['allCells'\]</span></span>*、 *<span class="n"><span class="pre">view</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'xy'</span></span>*、 *<span class="n"><span class="pre">showConns</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">popColors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">tagsFile</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">figSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(12,</span> <span class="pre">12)</span></span>*、 *<span class="n"><span class="pre">fontSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">12</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">lineWidth</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.1</span></span>* <span class="sig-paren">)</span><a href="_modules/netpyne/analysis/network.html#plot2Dnet" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.plot2Dnet" class="headerlink" title="Link to this definition"></a>
\<short description of netpyne.analysis.network.plot2Dnet\> に対する関数/\<short description of netpyne.analysis.network.plot2Dnet\> への関数

パラメータ<span class="colon">:</span>
- **include** (*list*) – 含めるシナプス前細胞のリスト。 **デフォルト:** <span class="pre">`['allCells']`</span> **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします。<span class="pre">`['allNetStims']`</span> は刺激のみをプロットします。<span class="pre">`['popName1']`</span> は単一集団をプロットします。<span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。 <span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>` `<span class="pre">`130]`</span> は複数のセルをプロットします。<span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **view** (*str*) – ビューの視点。 **デフォルト:** <span class="pre">`'xy'`</span> 正面図、**オプション:** <span class="pre">`'xz'`</span> 上面図

- **showConns** (*bool*) – 接続を表示するかどうか。 **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **popColors** (*dict*) – 各母集団 (キー) に使用されるカスタム色 (値) を含む辞書。 **デフォルト:** <span class="pre">`None`</span> は標準色を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **tagsFile** (*str*) – 接続プロットで使用する保存されたタグ ファイルへのパス。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **figSize** (*list* *\[width,* *height\]*) – Figure のサイズ (インチ単位)。 **デフォルト:** <span class="pre">`(12,`</span>` `<span class="pre">`12)`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **fontSize** (*int*) – 図のフォント サイズ。 **デフォルト:** <span class="pre">`12`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は図を自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.png'`</span>、<span class="pre">`'.jpg'`</span>、<span class="pre">`'.eps'`</span>、および <span class="pre">`'.tiff'`</span> です。

- **showFig** (*bool*) –

<span class="pre">`True`</span> の場合の図を示します。
  **デフォルト:** <span class="pre">`True`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

lineWidth: 浮動小数点
  接続線の幅。 **デフォルト:** <span class="pre">`0.1`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">nTE</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cells1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\[\]</span></span>*、 *<span class="n"><span class="pre">cells2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">\[\]</span></span>*、 *<span class="n"><span class="pre">spks1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">spks2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">binSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">20</span></span>*、 *<span class="n"><span class="pre">numShuffle</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">30</span></span>* <span class="sig-paren">)</span><a href="_modules/netpyne/analysis/info.html#nTE" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#netpyne.analysis.nTE" class="headerlink" title="Link to this definition"></a>
2 つのスパイク列信号間の正規化伝達エントロピー (nTE) を計算する関数。

伝達エントロピーは、確率変数間の時間方向の情報伝達を測定できるモデルフリー統計量であるため、情報伝達を測定するための非対称な方法を提供します。簡単に言うと、nTE は、Y の過去では説明されない、X 自身の過去によって説明される X 内の情報の部分を表します。

Kale, P. 他 (2018 年 7 月)。多源機能性てんかんネットワークを特定するツールとしての正規化された伝達エントロピー IEEE Engineering in Medicine and Biology Society (EMBC) <a href="https://doi.org/10.1109/embc.2018.8512532" class="reference external">https://doi.org/10.1109/embc.2018.8512532</a>

パラメータ<span class="colon">:</span>
- **cells1** (*list*) – スパイク列 1 を取得するセルのサブセット。 **デフォルト:** <span class="pre">`[]`</span> **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします。 <span class="pre">`['allNetStims']`</span> は刺激のみをプロットします。 <span class="pre">`['popName1']`</span> は単一集団をプロットします。 <span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。<span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>Q` `<span class="pre">`130]`</span> は複数のセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は、特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **cells2** (*list*) – スパイク列 2 を取得するセルのサブセット。 **デフォルト:** <span class="pre">`[]`</span> **オプション:** cell1 と同じ

- **spks1** (*リスト*) – スパイク トレイン 1;スパイク時間のリスト。省略した場合は、cell1 からスパイクを取得します。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **spks2** (*リスト*) – スパイク トレイン 2;スパイク時間のリスト。省略した場合は、セルからスパイクを取得します2。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **timeRange** (*list* *\[min,* *max\]*) – nTE を計算する時間の範囲 (ミリ秒)。 **デフォルト:** <span class="pre">`None`</span> はシミュレーション時間範囲全体を使用します **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **binSize** (*int*) – スパイク時間をヒストグラムに変換するために使用されるビン サイズ。 **デフォルト:** <span class="pre">`20`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

- **numShuffle** (*int*) – TEshuffled を計算するためにスパイク トレイン 1 をシャッフルする回数。注: nTE = (TE - TEShuffled)/H(X2F\|X2P)。 **デフォルト:** <span class="pre">`30`</span> **オプション:** <span class="pre">`<option>`</span> \<description of option\>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">netpyne.analysis.</span></span><span class="sig-name descname"><span class="pre">granger</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cells1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">cells2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">spks1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">spks2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">label1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">label2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">timeRange</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">binSize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">5</span></span>*、 *<span class="n"><span class="pre">testGranger</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*、 *<span class="n"><span class="pre">plotFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*、 *<span class="n"><span class="pre">saveData</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">saveFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*、 *<span class="n"><span class="pre">showFig</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="#netpyne.analysis.granger" class="headerlink" title="Link to this definition"></a>
2 つのスパイク列信号間のグレンジャー因果関係を計算する関数。

グレンジャー因果関係検定は、ある時系列が別の時系列の予測に役立つかどうかを判断するための統計的仮説検定です。 G 因果関係は、両方の原因が先行し、その結果の予測に役立つという単純な考え方に基づいています。

セス、A.K.、バレット、A.B.、バーネット、L. (2015)。神経科学とニューロイメージングにおけるグレンジャーの因果関係分析。神経科学ジャーナル、35(8)、3293–3297。 <a href="https://doi.org/10.1523/jneurosci.4399-14.2015" class="reference external">https://doi.org/10.1523/jneurosci.4399-14.2015</a>

パラメータ<span class="colon">:</span>
- **cells1** (*list*) – スパイク列 1 を取得するセルのサブセット。 **デフォルト:** <span class="pre">`None`</span> **オプション:** <span class="pre">`['all']`</span> はすべての細胞と刺激をプロットします。 <span class="pre">`['allNetStims']`</span> は刺激のみをプロットします。 <span class="pre">`['popName1']`</span> は単一集団をプロットします。 <span class="pre">`['popName1',`</span>` `<span class="pre">`'popName2']`</span> は複数の集団をプロットします。<span class="pre">`[120]`</span> は単一のセルをプロットします。<span class="pre">`[120,`</span>Q` `<span class="pre">`130]`</span> は複数のセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`56)]`</span> は、特定の集団からのセルをプロットします。 <span class="pre">`[('popName1',`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1]),`</span>` `<span class="pre">`('popName2',`</span>` `<span class="pre">`[4,`</span>` `<span class="pre">`5,`</span>` `<span class="pre">`6])]`</span>、複数の集団からの細胞をプロットします

- **cells2** (*list*) – スパイク列 2 を取得するセルのサブセット。 **デフォルト:** <span class="pre">`None`</span> **オプション:** cell1 と同じ

- **spks1** (*リスト*) – スパイク トレイン 1;スパイク時間のリスト。省略した場合は、cell1 からスパイクを取得します。 **デフォルト:** <span class="pre">`None`</span>

- **spks2** (*リスト*) – スパイク トレイン 2;スパイク時間のリスト。省略した場合は、セルからスパイクを取得します2。 **デフォルト:** <span class="pre">`None`</span>

- **label1** (*str*) – プロットで使用するスパイク列 1 のラベル。 **デフォルト:** <span class="pre">`None`</span>

- **label2** (*str*) – プロットで使用するスパイク列 2 のラベル。 **デフォルト:** <span class="pre">`None`</span>

- **timeRange** (*list* *\[min,* *max\]*) – nTE を計算する時間の範囲 (ミリ秒)。 **デフォルト:** <span class="pre">`None`</span> はシミュレーション時間範囲全体を使用します

- **binSize** (*int*) – スパイク時間をヒストグラムに変換するために使用されるビン サイズ。 **デフォルト:** <span class="pre">`5`</span>

- **testGranger** (*bool*) – グレンジャーの計算をテストするかどうか。 **デフォルト:** <span class="pre">`False`</span>

- **plotFig** (*bool*) – グレンジャー因果関係 Fx2y および Fy2x を示す図をプロットするかどうか **デフォルト:** <span class="pre">`True`</span>

- **saveData** (*bool* *or* *str*) – プロットの生成に使用されるデータを保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> はデータを自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.pkl'`</span> および <span class="pre">`'.json'`</span> です。

- **saveFig** (*bool* *or* *str*) – Figure を保存するかどうか、および保存する場所。 **デフォルト:** <span class="pre">`False`</span> **オプション:** <span class="pre">`True`</span> は図を自動保存し、<span class="pre">`'/path/filename.ext'`</span> はカスタム パスとファイル名に保存します。有効なファイル拡張子は <span class="pre">`'.png'`</span>、<span class="pre">`'.jpg'`</span>、<span class="pre">`'.eps'`</span>、および <span class="pre">`'.tiff'`</span> です。

- **showFig** (*bool*) – <span class="pre">`True`</span> の場合の図を表示します。 **デフォルト:** <span class="pre">`True`</span>

<!-- -->

注: *include* 引数には次の値を指定できます。
- <span class="pre">`'all'`</span>: すべてのセルとネットスティム

- <span class="pre">`'allCells'`</span>: すべてのセルのみ

- <span class="pre">`'allNetStims'`</span>: すべての NetStim のみ

- <span class="pre">`120`</span>: gid 120 のセル

- <span class="pre">`'L4'`</span>: 集団「L4」内のすべてのセルまたは NetStim

- <span class="pre">`('L2',`</span>` `<span class="pre">`56)`</span>: 集団「L2」からの相対インデックス 56 のセル

- <span class="pre">`('L5',`</span>` `<span class="pre">`[4,5,6])`</span>: 集団「L5」の相対インデックス 4、5、および 6 を持つセル

以下の図は、さまざまな分析機能の使用例を示しています。

<a href="_images/analysis_figs.png" class="reference internal image-reference"><img src="_images/analysis_figs.png" class="align-center" style="width: 90%;" alt="_images/analysis_figs.png" /></a> <a href="_images/spikestats.png" class="reference internal image-reference"><img src="_images/spikestats.png" class="align-center" style="width: 90%;" alt="_images/spikestats.png" /></a>

</div>

<div id="network-class-methods" class="section">

<span id="network-methods"></span>

### ネットワーク クラス メソッド<a href="#network-class-methods" class="headerlink" title="Link to this heading"></a>

ネットワークを設定する方法

- **net.setParams()**

- **net.createPops()**

- **net.createCells()**

- **net.connectCells()**

ネットワークを変更する方法

- **net.modifyCells(params, updateMasterAllCells=False)**

> <div>
  >
  > インスタンス化されたネットワーク内のセルのプロパティを変更します。 <span class="pre">`params`</span> 引数は、次の項目を含む辞書です。
  >
  > - ‘secs’: セル プロパティ ルールの初期設定と同じ形式を使用するセクションの辞書 (<a href="#cell-types" class="reference internal"><span class="std std-ref">セル タイプ</span></a> または <a href="#cell-class-data-model" class="reference internal"><span class="std std-ref">Cell を参照)詳細については class</span></a>)
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'soma':`</span>` `<span class="pre">`{'geom':`</span>` `<span class="pre">`{'L':`</span>` `<span class="pre">`100}}}`</span> は、ソーマの長さを 100 um に設定します。
  > >
  > > </div>
  >
  > </div>

- **net.modifySynMechs(params, updateMasterAllCells=False)**

> <div>
  >
  > インスタンス化されたネットワーク内の synMech のプロパティを変更します。 <span class="pre">`params`</span> 引数は、次の 3 つの項目を含む辞書です。
  >
  > - ‘conds’: 変更する synMech を選択するための条件の辞書。各項目には synMech タグと必要な値 (\[min, max\] 範囲形式が許可されます) が含まれます。
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'label':`</span>` `<span class="pre">`'AMPA',`</span>` `<span class="pre">`'sec':`</span>` `<span class="pre">`'soma',`</span>` `<span class="pre">`'loc':`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`0.5]}`</span>ソーマセクションのラベル「AMPA」を持つ synMech をターゲットにし、位置は 0 ～ 0.5 です。
  > >
  > > </div>
  >
  > - ‘cellConds’: 変更する synMech を含むターゲット セルを選択するための条件の辞書。各項目にはセル タグ (利用可能なタグのリストを参照 <a href="#cell-class-data-model" class="reference internal"><span class="std std-ref">セル クラス</span></a>) と目的の値 (\[min, max\] 範囲形式が許可されます) が含まれます。
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'pop':`</span>` `<span class="pre">`'PYR',`</span>` `<span class="pre">`'ynorm':`</span>` `<span class="pre">`[0.1,`</span>` `<span class="pre">`0.6]}`</span> は、深さが正規化された「PYR」母集団のセルの接続をターゲットとします。 0.1と0.6。
  > >
  > > </div>
  >
  > - ‘\[synMech property\]’ (例: ‘tau1’ または ‘e’): stim プロパティの新しい値 (プロパティは synMech のタイプに依存することに注意してください)。変更する複数の synMech プロパティを含めることができます。
  >
  > </div>

- **net.modifyConns(params, updateMasterAllCells=False)**

> <div>
  >
  > インスタンス化されたネットワーク内の接続のプロパティを変更します。 <span class="pre">`params`</span> 引数は、次の 3 つの項目を含む辞書です。
  >
  > - ‘conds’: 変更する接続を選択するための条件の辞書。各項目には conn タグ (利用可能な conn タグのリストを参照 <a href="#cell-class-data-model" class="reference internal"><span class="std std-ref">Cell class</span></a>) と、目的の値 (\[min, max\] 範囲形式が許可されています) が含まれます。
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'label':`</span>` `<span class="pre">`'M->S'}`</span> は、「M-\>S」というラベルの付いた connParams ルールを使用して作成された接続をターゲットとします。例えば<span class="pre">`{'weight':`</span>` `<span class="pre">`[0.4,`</span>` `<span class="pre">`0.8],`</span>` `<span class="pre">`'sec':`</span>` `<span class="pre">`'soma'}`</span> は、重みが 0.4 から 0.8 以内の接続をターゲットとします。 「ソーマ」セクションに追加されました。
  > >
  > > </div>
  >
  > - ‘postConds’: 変更する接続を含むシナプス後セルを選択するための条件の辞書。各項目にはセル タグ (使用可能なタグのリストを参照 <a href="#cell-class-data-model" class="reference internal"><span class="std std-ref">セル クラス</span></a>) と目的の値 (\[min, max\] 範囲形式が許可されます) が含まれます。
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'pop':`</span>` `<span class="pre">`'PYR',`</span>` `<span class="pre">`'ynorm':`</span>` `<span class="pre">`[0.1,`</span>` `<span class="pre">`0.6]}`</span> は、深さが正規化された「PYR」集団のセルの接続をターゲットとします。 0.1と0.6。
  > >
  > > </div>
  >
  > - 「重量」 \| 「threshold」: 接続の重みまたはしきい値の新しい値。両方を含めることができます。
  >
  > </div>

- **net.modifyStims(params, updateMasterAllCells=False)**

> <div>
  >
  > インスタンス化されたネットワーク内の stim のプロパティを変更します。 <span class="pre">`params`</span> 引数は、次の 3 つの項目を含む辞書です。
  >
  > - ‘conds’: 変更するスティムを選択するための条件の辞書。各項目にはスティム タグ (利用可能なスティム タグのリスト <a href="#cell-class-data-model" class="reference internal"><span class="std std-ref"> セル クラスを参照) および目的の値 (\[min, max\] 範囲形式が許可されています) が含まれます。
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'label':`</span>` `<span class="pre">`'VClamp1->S'}`</span> は、「VClamp1-\>S」というラベルの付いた stimTargetParms ルールを使用して作成されたスティムをターゲットとします。例えば<span class="pre">`{'source':`</span>` `<span class="pre">`'IClamp2',`</span>` `<span class="pre">`'dur':`</span>` `<span class="pre">`[100,`</span>` `<span class="pre">`300]}`</span> は、ソースとして「Netstim2」（で定義されている）を持つスティムをターゲットとします。 stimSourceParams)、期間は 100 ～ 300 ミリ秒です。
  > >
  > > </div>
  >
  > - ‘cellConds’: 変更するスティムを含むターゲット セルを選択するための条件の辞書。各項目にはセル タグ (利用可能なタグのリストを参照 <a href="#cell-class-data-model" class="reference internal"><span class="std std-ref">セル クラス</span></a>) および目的の値 (\[min, max\] 範囲形式が許可されます) が含まれます。
  >
  > > <div>
  > >
  > > 例: <span class="pre">`{'pop':`</span>` `<span class="pre">`'PYR',`</span>` `<span class="pre">`'ynorm':`</span>` `<span class="pre">`[0.1,`</span>` `<span class="pre">`0.6]}`</span> は、深さが正規化された「PYR」集団のセルの接続をターゲットとします。 0.1と0.6。
  > >
  > > </div>
  >
  > - ‘\[stim property\]’ (例: ‘dur’、‘amp’、または ‘lay’): stim プロパティの新しい値 (プロパティは stim のタイプに依存することに注意してください)。変更するいくつかの stim プロパティを含めることができます。
  >
  > </div>

<div class="admonition note">

注記

<span class="pre">`updateMasterAllCells`</span> 引数により、マスター ノード内の <span class="pre">`sim.net.allCells`</span> リストも変更されたパラメーターで更新されます。デフォルトでは、これは変更機能の速度を低下させるため False に設定されており、<span class="pre">`sim.net.allCells`</span> はシミュレーションを実行してデータを収集した後に自動的に更新されます。

</div>

</div>

<div id="population-class-methods" class="section">

### 母集団クラスのメソッド<a href="#population-class-methods" class="headerlink" title="Link to this heading"></a>

- **pop.createCells()**

- **pop.createCellsFixedNum()**

- **pop.createCellsDensity()**

- **pop.createCellsList()**

</div>

<div id="cell-class-methods" class="section">

### セル クラス メソッド<a href="#cell-class-methods" class="headerlink" title="Link to this heading"></a>

- **cell.create()**

- **cell.createPyStruct()**

- **cell.createNEURONObj()**

- **cell.associateGid()**

- **cell.addConn()**

- **cell.addNetStim()**

- **cell.addIClamp()**

- **cell.recordTraces()**

- **cell.recordStimSpikes()**

</div>

</div>

<div id="netpyne-data-model-structure-of-instantiated-network-and-output-data" class="section">

<span id="data-model"></span>

## NetPyNE データ モデル (インスタンス化されたネットワークと出力データの構造)<a href="#netpyne-data-model-structure-of-instantiated-network-and-output-data" class="headerlink" title="Link to this heading"></a>

NetPyNE によって生成されたインスタンス化されたネットワーク構造の表現を以下に示します。

<a href="_images/netstruct.png" class="reference internal image-reference"><img src="_images/netstruct.png" class="align-center" style="width: 90%;" alt="_images/netstruct.png" /></a>

<div id="netpyne-data-model-structure-of-instantiated-network" class="section">

### NetPyNE データ モデル: インスタンス化されたネットワークの構造<a href="#netpyne-data-model-structure-of-instantiated-network" class="headerlink" title="Link to this heading"></a>

モデルは **sim.net** で **Network** オブジェクトとしてインスタンス化されます。このオブジェクトには多くの組み込み属性があり、その他の属性は特定の実装に応じて存在する場合と存在しない場合があります。 「sim.net」を構成する基本要素は次の 2 つです。

- **pops** - ネットワークに実装されたすべての母集団を説明する順序付き辞書。そのエントリは、母集団にラベルを付けるキー (<span class="pre">`netParams.popParams`</span> で定義) と **Pop** オブジェクトを参照する値です。このオブジェクトにはいくつかの属性があります。

> <div>
  >
  > - **タグ**: 母集団を定義する宣言ルールに関連する、母集団のさまざまな属性を説明する辞書。たとえば:
  >
  > > <div>
  > >
  > > <span class="pre">`sim.net.pops['Exc_L4'].tags`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'cellType':`</span>` `<span class="pre">`'PYR',`</span>` `<span class="pre">`'numCells':`</span>` `<span class="pre">`100,`</span>` `<span class="pre">`'pop':`</span>` `<span class="pre">`'Exc_L4'}`</span>
  > >
  > > </div>
  >
  > - **cellGids**: 母集団を構成するニューロン識別子 (グローバル ID) のリスト。たとえば:
  >
  > > <div>
  > >
  > > <span class="pre">`sim.net.pops['Exc_L4'].cellGids`</span>` `<span class="pre">`=`</span>` `<span class="pre">`[0,`</span>` `<span class="pre">`1,`</span>` `<span class="pre">`2,`</span>` `<span class="pre">`3,`</span>` `<span class="pre">`4]`</span>
  > >
  > > </div>
  >
  > - **cellModelClass**: どの特定のセル モデル クラスが実装されたかを説明するタイプ (例: <span class="pre">`compartCell`</span> または <span class="pre">`pointCell`</span>)。
  >
  > </div>

- **セル** - **ローカル**でインスタンス化されたセルのリスト (この区別は、並列コンピューティングを実装する場合に重要です)。リスト内の各要素は、(さまざまなセル モデル クラスの中の) **Cell** オブジェクトです。 Cell オブジェクトとして、いくつかの固有属性があります。

> <div>
  >
  > - **gid**: セルのグローバル識別番号
  >
  > - **タグ**: セルのさまざまな属性を説明するディクショナリ。これには、セルが属する集団からのいくつかのタグが含まれる場合があります (<span class="pre">`netParams.popTagsCopiedToCells`</span> のタグ リスト、たとえば「cellType」)。これらの属性は次のとおりです。
  >
  > > <div>
  > >
  > > - **pop**: 属する集団のラベル。たとえば:
  > >
  > > > <div>
  > > >
  > > > <span class="pre">`sim.net.cells[0].tags['pop']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`'Exc_L4'`</span>
  > > >
  > > > </div>
  > >
  > > - **x**、**y**、**z**: セルの x、y、z 座標。たとえば:
  > >
  > > > <div>
  > > >
  > > > <span class="pre">`sim.net.cells[0].tags['x']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`-2.3535`</span>
  > > >
  > > > </div>
  > >
  > > - **xnorm**、**ynorm**、**znorm**: セルの正規化された x、y、z 座標。
  > >
  > > - 特定の状況に応じたその他のタグ (たとえば、<span class="pre">`netParams.popParams`</span> 内の集団を <span class="pre">`cellsList`</span> で宣言する (<span class="pre">`params`</span> を含む))。
  > >
  > > </div>
  >
  > - **conns**: 接続のリスト (シナプス後側のこのセル)。このリストの各要素 (特定の接続) は、次のエントリを含む辞書です。
  >
  > > <div>
  > >
  > > - **preGid**: シナプス前細胞の ID (Gid)。この接続が接続を必要とする刺激から発生する場合、値は「NetStim」に対応します。
  > >
  > > - **重量**: 接続の重量。
  > >
  > > - **遅延**: 接続の遅延。
  > >
  > > - **synMech**: この接続を管理するシナプス メカニズムのラベル。
  > >
  > > - さまざまなシナリオに応じて、他のエントリが表示されます。
  > >
  > > > <div>
  > > >
  > > > ・セルモデルクラスが点プロセスでない場合、シナプスを乗せるセクション/場所が存在します。次に、次のエントリが表示されます。
  > > > - **sec**: シナプスをホストするセクション。
  > > >
  > > > - **loc**: シナプスが表示されるこのセクション内の場所。
  > > >
  > > > - 接続がギャップジャンクション (<span class="pre">`netParams.connParams['rule']['gapJunction']=`</span>` `<span class="pre">`True`</span>、'compartCell' セル モデル クラスでのみ利用可能) として指定されている場合、この種類の接続に関連付けられたエントリが表示されます。
  > > >
  > > > > <div>
  > > > >
  > > > > - **gapJunction**: ルールで指定された接続側 (「pre」または「post」)。
  > > > >
  > > > > - **preLoc**: ルールで指定されたシナプス前側のギャップ結合の位置 (「ポスト」のセルの場合)。
  > > > >
  > > > > - **gapId**: 接続側のセルの ID。
  > > > >
  > > > > - **preGapId**: 接続相手側のセルの ID。
  > > > >
  > > > > </div>
  > > >
  > > > - **shape**、**plast**、**weightIndex**: 特定の接続パターンまたはプロセスを実装するために使用されるエントリ。
  > > >
  > > > </div>
  > >
  > > - **hObj**: ギャップ ジャンクションの場合を除き、他のすべての接続は NEURON <span class="pre">`NetCon`</span> オブジェクトを介して実装されます。オブジェクト自体がこの「hObj」キーに対応する値です。したがって、NEURON オブジェクトには、たとえば次のようにアクセス (および変更) できます。
  > >
  > > > <div>
  > > >
  > > > <span class="pre">`sim.net.cells[0].conns[0]['hObj']`</span>
  > > >
  > > > </div>
  > >
  > > 特に、これらのオブジェクトに対応するメソッドは、(ネットワークがインスタンス化された後) コマンド ラインから呼び出すことができます。たとえば:
  > >> > > <div>
  > > >
  > > > <span class="pre">`sim.net.cells[0].conns[0]['hObj'].syn()`</span>。
  > > >
  > > > </div>
  > >
  > > </div>
  >
  > - **stims**: セルに入力される刺激のリスト。このリストの各要素は、次のエントリを含む辞書です。
  >
  > > <div>
  > >
  > > - **label**: ターゲットパラメータを指定するルールのラベル
  > >
  > > - **ソース**: 受信スティミュラスを定義するソース ルールのラベル。
  > >
  > > - **タイプ**: 刺激のタイプ。たとえば:
  > >
  > > > <div>
  > > >
  > > > <span class="pre">`sim.net.cells[0].stims[0]['type']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`'NetStim'`</span> または <span class="pre">`sim.net.cells[0].stims[0]['type']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`'IClamp'`</span>
  > > >
  > > > </div>
  > >
  > > - **sec**: 刺激がターゲットとしているセクション。
  > >
  > > - **loc**: 刺激が影響しているセクション内の位置。
  > >
  > > - 入力刺激を定義するプロパティ。たとえば、**NetStim** の場合は、「rate」、「noise」、「start」、および「number」 (さらに、ランダム ジェネレータを初期化するための「seed」)。
  > >
  > > - **hObj**: 刺激に関連付けられた NEURON オブジェクト。たとえば:
  > >
  > > > <div>
  > > >
  > > > <span class="pre">`sim.net.cells[0].stims[0]['hObj']`</span>
  > > >
  > > > </div>
  > >
  > > NEURON オブジェクトに関連付けられたメソッドはすぐに利用できます。たとえば、オブジェクトが「IClamp」の場合、<span class="pre">`sim.net.cells[0].stims[0]['hObj'].dur`</span> を介してその期間を変更できます。
  > >
  > > </div>
  >
  > - セルモデルクラスに応じて、他のエントリが使用可能です。特に、**‘compartCell’** セル モデル クラスの場合は、次のとおりです。
  >
  > > <div>
  > >
  > > - **secs**: セルを構成するセクションの辞書。この辞書には次のエントリがあります。
  > >
  > > > <div>
  > > >
  > > > - **geom**: セクションを構成する円柱の幾何学的特性を含む辞書。たとえば、
  > > >
  > > > > <div>
  > > > >
  > > > > <span class="pre">`sim.net.cells[0].secs['soma']['geom']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{diam:`</span>` `<span class="pre">`18.8,`</span>` `<span class="pre">`L:`</span>` `<span class="pre">`18.8,`</span>` `<span class="pre">`Ra:`</span>` `<span class="pre">`123.0}`</span>
  > > > >
  > > > > </div>
  > > >
  > > > - **topol**: トポロジーの仕様 (他のセクションとどのように接続されているか) を含む辞書。
  > > >
  > > > - **mechs**: 分散メカニズムを備えた辞書。たとえば、
  > > >
  > > > > <div>
  > > > >
  > > > > <span class="pre">`sim.net.cells[0].secs['soma']['mechs']['hh']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{gnabar:`</span>` `<span class="pre">`0.12,`</span>` `<span class="pre">`gkbar:`</span>` `<span class="pre">`0.036,`</span>` `<span class="pre">`gl:`</span>` `<span class="pre">`0.003,`</span>` `<span class="pre">`el:`</span>` `<span class="pre">`-70}`</span>
  > > > >
  > > > > </div>
  > > >
  > > > - **イオン**: このセクションに含まれるイオン機構を指定する辞書。
  > > >
  > > > - **synMechs**: このセクションにあるすべてのシナプスのリスト。このリストの各要素は、それに関連するすべての情報を含む辞書です。
  > > >
  > > > > <div>
  > > > >
  > > > > - **ラベル**: シナプスダイナミクスを指定するルールを説明するラベル。
  > > > >
  > > > > - **loc**: シナプスが表示されるセクション内の位置
  > > > >
  > > > > - シナプス モデルの定義に関連付けられたプロパティ。たとえば、「tau1」、「e」などです。
  > > > >
  > > > > - **hObj**: シナプスに関連付けられた NEURON オブジェクト。例えば> > > >
  > > > > > <div>
  > > > > >
  > > > > > <span class="pre">`sim.net.cells[0].secs['soma']['synMechs'][0]['hObj']`</span>` `<span class="pre">`=`</span>` `<span class="pre">`Exp2Syn[0]`</span>
  > > > > >
  > > > > > </div>
  > > > >
  > > > > </div>
  > > >
  > > > - **pointps**: セクションの電圧ダイナミクスを制御するポイント プロセスを指定するディクショナリ。これには、非線形メカニズムが定義されている「mod」の名前とすべての必要なパラメーターが含まれます。
  > > >
  > > > - その他のスカラー プロパティ: **spikeGenLoc**、**vinit** など。
  > > >
  > > > - **hObj**: セクションに関連付けられた NEURON オブジェクト。たとえば、
  > > >
  > > > > <div>
  > > > >
  > > > > <span class="pre">`type(sim.net.cells[0].secs['soma']['hObj'])`</span>` `<span class="pre">`=`</span>` `<span class="pre">`nrn.Section`</span>
  > > > >
  > > > > </div>
  > > >
  > > > </div>
  > >
  > > </div>
  >
  > </div>

- これら 2 つの要素 (「ポップ」と「セル」) 以外にも、「sim.net」を定義および構成する多数の要素があります。

> <div>
  >
  > - **allPops**: ネットワークを構成するすべての人口を含む辞書。各キーは定義された母集団に対応し、その値はそれに関する情報 (「タグ」、「cellGids」など) を含む辞書になります。
  >
  > - **allCells**: すべてのセルに関する情報を含むリスト (グローバル)。各要素/セルは、このセルを定義するすべての情報を含む辞書です。
  >
  > - **params**: ネットワークを指定する netParams。
  >
  > - **rxd**: 反応拡散モデルのすべての仕様を含む辞書 (<span class="pre">`netParams.rxdParams`</span> と同じ形式) に加え、関連する NEURON オブジェクト。
  >
  > - **recXElectrode**: LFP の記録に関連付けられたオブジェクト (存在する場合)。
  >
  > - **compartCells** および **popForEachGid**: LFP およびダイポール記録中に使用するオブジェクト セルと辞書、{‘gid’: ‘pop’}。
  >
  > - **cells_dpls** および **cells_dpl**: LFP および双極子の記録中に使用する、経時的および一度に各セルの双極子のベクトルを含む辞書。
  >
  > - **gid2lid**: グローバル ID とローカル ID をマッピングする辞書、{‘gid’: ‘lid’}。
  >
  > - **lastGid**: 定義された最後のセルの Gid。ネットワークの開発中に役立ちます。
  >
  > - **lastGapId**: 最後に定義されたギャップ ジャンクション。ネットワークの開発中に役立ちます。
  >
  > - **preGapJunctions**: ギャップ結合について、接続性ルールに書かれた方向に従ってシナプス前側の情報を格納するリスト。
  >
  > </div>

</div>

<div id="accessing-dictionaries-using-dot-notation-dict-and-odict-classes" class="section">

<span id="dicts-dotnotation"></span>

### ドット表記を使用した辞書へのアクセス: Dict クラスと ODict クラス<a href="#accessing-dictionaries-using-dot-notation-dict-and-odict-classes" class="headerlink" title="Link to this heading"></a>

ドット表記法 (a.b.c) で NetPyNE 構造にアクセスできるようにするために、元の Python dict および OrderedDict クラスから継承するサブクラスである Dict および ODict クラスを追加しました。すべての NetPyNE 内部辞書は、クラス Dict または ODict のいずれかです。以下に、Dict クラスのいくつかの機能を示します。

> <div>
>
> - 標準の dict メソッド: <span class="pre">`a['b']['c']`</span>、<span class="pre">`a.iteritems()`</span>、<span class="pre">`a.keys()`</span>、<span class="pre">`a.update()`</span> など)、または属性メソッド/ドット表記: <span class="pre">`a.b.c=2`</span> のいずれかを使用してアクセスできます。
>
> - 欠落している要素が自動的に追加されます (間違ったキーを使用すると、望ましくない影響が生じる可能性があることに注意してください): <span class="pre">`a=Dict();`</span>` `<span class="pre">`a.b.c.d.e=1`</span>
>
> - コンストラクターは dict (ネストされた dict を含む) および/または kwargs を許可します: <span class="pre">`a=Dict(b=1,`</span>` `<span class="pre">`c=2)`</span> または [<span id="id4" class="problematic">\`\`</span>](#id3)a=Dict({‘a’: 1, ‘b’: {‘c’: 2}})\`
>
> - メソッド .todict() は、Dict の dict バージョンを返します: <span class="pre">`a=Dict({'b':1});`</span>` `<span class="pre">`a_dict=a.todict()`</span>
>
> - \_\_getstate\_\_() メソッドによるシリアル化 (ピクル化時など) は、通常の dict を返します (.todict() メソッドを使用)。
>
> </div>

<span class="pre">`netParams`</span> を指定するには、標準の dict または Dict() クラスを使用できます。 Dict クラスを使用するには、まず次の方法でインポートする必要があります。

<div class="highlight-default notranslate">

<div class="highlight">

    from netpyne.specs import Dict

</div>

</div>

ドット表記を使用して NetPyNE 構造にアクセスする例:

> <div>
>
> - <span class="pre">`cellRule`</span>` `<span class="pre">`=`</span>` `<span class="pre">`Dict();`</span>` `<span class="pre">`cellParam.secs.soma.mechs.hh`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'gnabar':`</span>` `<span class="pre">`0.12,`</span>` `<span class="pre">`'gkbar':`</span>` `<span class="pre">`0.036};`</span>` `<span class="pre">`cellParam.conds`</span>` `<span class="pre">`=`</span>` `<span class="pre">`{'cellType':`</span>` `<span class="pre">`'IT'}`</span>
>
> - <span class="pre">`netParams.cellParams.PYR_rule.secs.soma.mechs.hh.gnabar`</span>
>
> - <span class="pre">`simConfig.analysis.plotRaster.include`</span>` `<span class="pre">`=`</span>` `<span class="pre">`['all']`</span>
>
> - <span class="pre">`sim.net.cells[0].secs.soma.mechs.nap.gbar`</span>` `<span class="pre">`=`</span>` `<span class="pre">`0.1`</span>
>
> - <span class="pre">`sim.net.cells[0].secs.soma.hSec(0.5).gbar_nap`</span>` `<span class="pre">`=`</span>` `<span class="pre">`0.1`</span>
>
> - <span class="pre">`sim.net.allCells[5].tags.pop`</span>
>
> - <span class="pre">`sim.net.cells[0].conns[1].weight`</span>
>
> - <span class="pre">`sim.net.cells[0].conns[1].hNetcon.weight[0]`</span>
>
> - <span class="pre">`sim.net.cells[0].stims[0].type`</span>
>
> - <span class="pre">`sim.net.pops.PYRpop.tags`</span>
>
> - <span class="pre">`sim.net.allPops.Mpop.cellGids`</span>
>
> - <span class="pre">`sim.allSimData.spkt`</span>
>
> - <span class="pre">`sim.allSimData.stims.cell_31.Input_4`</span>
>
> - <span class="pre">`sim.allSimData.V_soma.cell_1`</span>
>
> </div>

</div>

<div id="sim-module" class="section">

### Sim モジュール<a href="#sim-module" class="headerlink" title="Link to this heading"></a>

- net (ネットワークオブジェクト)

- cfg (SimConfig オブジェクト)

- pc (h.ParallelContext オブジェクト)

- nhosts (int)

- ランク (int)

- タイミングデータ (辞書)

</div>

<div id="network-class" class="section">

### ネットワーク クラス<a href="#network-class" class="headerlink" title="Link to this heading"></a>

- ポップス (ポップオブジェクトの辞書)

- セル (Cell オブジェクトのリスト)

- params (NetParams オブジェクト)

ノードから収集した後: - allCells (辞書のリスト) - allPops (辞書のリスト)

</div>

<div id="population-class" class="section">

### 人口クラス<a href="#population-class" class="headerlink" title="Link to this heading"></a>

- cellGid (リスト)

- タグ (辞書)

</div>

<div id="cell-class" class="section">

<span id="cell-class-data-model"></span>

### セルクラス<a href="#cell-class" class="headerlink" title="Link to this heading"></a>

- gid (int)

- タグ (辞書)
  - 「ラベル」

- 「ポップ」

- 「セルモデル」

- 「セルタイプ」

- 「x」、「y」、「z」

- 「xnorm」、「ynorm」、「znorm」

- 秒 (辞書)
  - 「secName」 (例: 「soma」) (辞書)
    - ‘hSec’ (NEURON オブジェクト)

    - ‘geom’ (Dict)
      - ‘L’

      - ‘diam’

      - ‘pt3d’ (list of tuples)

      - …

    - ‘topol’ (Dict)
      - ‘parentSec’

      - ‘parentX’

      - ‘childX’

    - ‘mechs’ (Dict)
      - ‘mechName’ (e.g. ‘hh’) (Dict)
        - ‘gnabar’

        - ‘gkbar’

        - …

    - ‘pointps’ (Dict)
      - ‘pointpName’ (e.g. ‘Izhi’) (Dict)
        - ‘hPointp’ (NEURON object)

        - ‘mod’

        - ‘a’

        - ‘b’

        - …

    - ‘synMechs’ (list)
      - \[0\] (Dict)
        - ‘hObj’: NEURON object

        - ‘label’

        - ‘loc’

- secLists (辞書)
  - 「secListName」 (例: 「alldends」) (リスト)

- 短所 (リスト)
  - \[0\] (辞書)
    - 「hNetCon」: NEURON オブジェクト

    - ‘label’

    - ‘preGid’

    - ‘preLabel’

    - ‘sec’

    - ‘loc’

    - ‘synMech’

    - ‘weight’

    - ‘threshold’

- スティム（リスト）
  - \[0\] (辞書)
    - 「hIClamp」 (NEURON オブジェクト)

    - ‘source’

    - ‘type’

    - ‘label’

    - ‘sec’

    - ‘loc’

    - ‘amp’

    - ‘dur’

    - ‘delay’

</div>

<div id="simulation-output-data" class="section">

### シミュレーション出力データ<a href="#simulation-output-data" class="headerlink" title="Link to this heading"></a>

シミュレーションの出力データは、ディクショナリ <span class="pre">`sim.simData`</span> および <span class="pre">`sim.allSimData`</span> に格納されます。前者は単一プロセス環境で使用する必要がありますが、後者には並列コンテキストのすべてのノードから収集されたデータが含まれます。シミュレーション出力データの内容は<span class="pre">`simConfig`</span>の設定に依存し、以下の内容が含まれる場合があります。

**1.細胞の痕跡**

<span class="pre">`simData`</span> のキーは <span class="pre">`simConfig.recordTraces`</span> のキー (例: 「V_soma」) に対応し、各トレースの値には、このトレースが記録されたセルのリストを含む辞書が含まれます。記録されたトレースは、セルごとに <span class="pre">`h.Vector`</span> として保存されます。たとえば、simConfig 設定の場合:

<div class="highlight-default notranslate">

<div class="highlight">

    simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'},
                              'Ina_soma':{'sec':'soma','loc':0.5,'var':'ina'}}
    simConfig.recordCells = [1, 3]
    simConfig.recordStep = 0.1

</div>

</div>

<span class="pre">`simData`</span> 辞書には (特に) 以下が含まれます。

<div class="highlight-default notranslate">

<div class="highlight">

    {'V_soma': {'cell_1': <h.Vector>, 'cell_3': <h.Vector>},
     'Ina_soma': {'cell_1': <h.Vector>, 'cell_3': <h.Vector>}

</div>

</div>

ここで、各ベクトルの長さは <span class="pre">`simConfig.duration`</span> および <span class="pre">`simConfig.recordStep`</span> によって決まります。

**2.スパイク**

<span class="pre">`spkt`</span>、<span class="pre">`spkid`</span> - スパイク時間と各スパイクのセル gid の順序付きリスト。

<span class="pre">`simConfig.recordCellsSpikes`</span> (デフォルトでは True) は、セルのサブセットからのみ記録するか、スパイク記録をオフにするために使用できます。

**3.ネットワークへの刺激**

<span class="pre">`stims`</span>。 <span class="pre">`NetStim`</span> または <span class="pre">`VecStim`</span> の各集団について、各ターゲット セルのスパイク時間 (<span class="pre">`h.Vector`</span>) のリストが含まれています。 <span class="pre">`simConfig.recordStim`</span> が <span class="pre">`True`</span> の場合にのみ使用できます。

**4. LFP 関連データ**

<span class="pre">`LFP`</span>、<span class="pre">`LFPCells`</span>、<span class="pre">`LFPPops`</span>。 <span class="pre">`simConfig`</span> の <span class="pre">`recordLFP`</span>、<span class="pre">`saveLFPCells`</span>、<span class="pre">`saveLFPPops`</span> オプションに応じて異なります。

- <span class="pre">`LFP`</span> - 形状 <span class="pre">`(num`</span>` `<span class="pre">`timesteps,`</span>` `<span class="pre">`num`</span>` `<span class="pre">`electrodes)`</span> の LFP 値の np.array です。

- <span class="pre">`LFPCells`</span> - 各セルから記録された LFP データの辞書 (LFP データは上記の形式です)

- <span class="pre">`LFPPops`</span> - 各母集団から記録された平均 LFP データの辞書 (LFP データは上記の形式です)

- <span class="pre">`iMembrane`</span> - 各細胞の膜貫通電流の辞書。 <span class="pre">`(num`</span>` `<span class="pre">`timesteps,`</span>` `<span class="pre">`num`</span>` `<span class="pre">`segments)`</span> の np.array です。ここで、numセグメントはセルのすべてのセクションにわたるセグメントの総数です。

**5.双極子関連データ**

<span class="pre">`dipoleSum`</span>、<span class="pre">`dipoleCells`</span>、<span class="pre">`dipolePops`</span>。 <span class="pre">`simConfig`</span> の <span class="pre">`recordDipole`</span>、<span class="pre">`saveDipoleCells`</span>、<span class="pre">`saveDipolePops`</span> オプションに依存します。

- <span class="pre">`dipoleSum`</span> - 各タイムステップでの電流双極子モーメントの合計 <span class="pre">`(num`</span>` `<span class="pre">`timesteps,`</span>` `<span class="pre">`3)`</span>; EEG/MEG計算に使用可能

- <span class="pre">`dipoleCells`</span> - 各セルについて記録された現在の双極子モーメントの辞書 (双極子データは上記の形式です)

- <span class="pre">`dipolePops`</span> - 各集団について記録された平均電流双極子モーメントの辞書 (双極子データは上記の形式です)

</div>

<div id="data-saved-to-file" class="section">

### ファイルに保存されたデータ<a href="#data-saved-to-file" class="headerlink" title="Link to this heading"></a>

- simConfig

- netParams

- ネット

- simデータ

</div>

</div>

<div id="importing-externally-defined-cell-models" class="section">

<span id="importing-cells"></span>

## 外部定義されたセル モデルのインポート<a href="#importing-externally-defined-cell-models" class="headerlink" title="Link to this heading"></a>

NetPyNE は、たとえば 1 つまたは複数のコンパートメントを持つホジキン-ハクスリー型セル、または Izhikevich 型セルのセル プロパティを内部定義するためのサポートを提供します (たとえば、<a href="tutorial.html#tutorial" class="reference internal"><span class="std std-ref">NetPyNE Tutorial</span></a> を参照)。ただし、以前に定義したセルを外部ファイルにインポートすることも可能です。ホックセルテンプレートまたはセルクラスで、<span class="pre">`importCellParams()`</span> メソッドを使用します。このメソッドは、すべてのセル情報を必要な NetPyNE 形式に変換します。このようにして、個別に実装されたセルを利用することができます。

の<span class="pre">`cellRule`</span>` `<span class="pre">`=`</span>` `<span class="pre">`netParams.importCellParams(label,`</span>` `<span class="pre">`conds,`</span>` `<span class="pre">`fileName,`</span>` `<span class="pre">`cellName,`</span>` `<span class="pre">`cellArgs={},`</span>` `<span class="pre">`importSynMechs=False)`</span>このメソッドは、新しいセル ルールのラベル、セルが定義されているファイルの名前 (.py または .hoc ファイル)、およびセル テンプレート (hoc) またはクラス (python) の名前を引数として受け取ります。オプションで、一連の引数をセル テンプレート/クラスに渡すことができます (例: <span class="pre">`{'type':`</span>` `<span class="pre">`'RS'}`</span>)。シナプスメカニズムのパラメータをインポートしたい場合は、<span class="pre">`importSynMechs=True`</span> を設定できます。このメソッドは新しいセル ルールを返し、さらに変更できるようにします。

NetPyNE には、インポートされるセル モデルに関する組み込み情報は含まれません。インポートは、外部セル モデルを一時的にインスタンス化し、必要なすべての情報 (ジオメトリ、トポロジ、分散メカニズム、ポイント プロセスなど) を読み取ることに基づいています。

以下に、外部ファイルから 10 個の異なる細胞モデルをインポートする例を示します。それぞれに必要なファイルと NetPyNE コードが提供されます。必ず <span class="pre">`nrnivmodl`</span> を実行して、各例の MOD ファイルをコンパイルしてください。セルモデルの例のリストは次のとおりです。

- <a href="#import-hh" class="reference internal"><span class="std std-ref">ホジキン・ハクスリー モデル</span></a>

- <a href="#import-hh3d-hoc" class="reference internal"><span class="std std-ref">3D ジオメトリを含む Hodgkin-Huxley モデル (.hoc から)</span></a>

- <a href="#import-hh3d-swc" class="reference internal"><span class="std std-ref">3D ジオメトリを含むホジキン・ハクスリー モデル (.swc から)</span></a>

- <a href="#import-traub" class="reference internal"><span class="std std-ref">トラウブモデル</span></a>

- <a href="#import-mainen" class="reference internal"><span class="std std-ref">メインモデル</span></a>

- <a href="#import-friesen" class="reference internal"><span class="std std-ref">フリーゼンモデル</span></a>

- <a href="#import-izhi03a" class="reference internal"><span class="std std-ref">Izhikevich 2003a モデル (独立電圧可変)</span></a>

- <a href="#import-izhi03b" class="reference internal"><span class="std std-ref">Izhikevich 2003b モデル (セクション電圧を使用)</span></a>

- <a href="#import-izhi07a" class="reference internal"><span class="std std-ref">Izhikevich 2007a モデル (独立電圧可変)</span></a>

- <a href="#import-izhi07b" class="reference internal"><span class="std std-ref">Izhikevich 2007b モデル (セクション電圧を使用)</span></a>

さらに、10 個のセル モデルすべてをインポートし、各タイプの母集団を作成し、バックグラウンド入力を提供し、すべてのセルをランダムに接続する NetPyNE ファイルの例 (<a href="_downloads/1355b1c6c896576bcc1108a87fadb5c5/tut_import.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut_import.py</code></span></a>) を提供します。この例を実行するには、セル モデルが定義されているすべてのファイルと MOD ファイルをダウンロードする必要もあります (下記を参照)。結果のラスタ​​ーを以下に示します。

<a href="_images/tut_import_raster.png" class="reference internal image-reference"><img src="_images/tut_import_raster.png" class="align-center" style="width: 50%;" alt="_images/tut_import_raster.png" /></a>

<div id="hodgkin-huxley-model" class="section">

<span id="import-hh"></span>

### ホジキン・ハクスリー モデル<a href="#hodgkin-huxley-model" class="headerlink" title="Link to this heading"></a>

*説明:* <span class="pre">`hh`</span> および <span class="pre">`pas`</span> メカニズム、およびシナプス メカニズムを備えた 2 コンパートメント (細胞体および樹状突起) 細胞。 Python クラスとして定義されます。

*必要なファイル:* <a href="_downloads/fd003a9347985e53bdf44d30f92e2adc/HHCellFile.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">HHCellFile.py</code></span></a>

*NetPyNE コード*

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.importCellParams(
            label='PYR_HH_rule',
            conds={'cellType': 'PYR', 'cellModel': 'HH'},
            fileName='HHCellFile.py',
            cellName='HHCellClass',
            importSynMechs=True)

</div>

</div>

</div>

<div id="hodgkin-huxley-model-with-3d-geometry-from-hoc" class="section">

<span id="import-hh3d-hoc"></span>

### 3D ジオメトリを含む Hodgkin-Huxley モデル (.hoc より)<a href="#hodgkin-huxley-model-with-3d-geometry-from-hoc" class="headerlink" title="Link to this heading"></a>

*説明:* マルチコンパートメントセル。 HOC セル テンプレートとして定義されます。セルのジオメトリのみが含まれます。 NetPyNE からジオメトリのみをインポートし、生​​物物理学 (<span class="pre">`hh`</span> および <span class="pre">`pas`</span> チャネル) を追加する例。

*必要なファイル:* <a href="_downloads/84b10f2bd6c7cbb069921b6824cf11b8/geom.hoc" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">geom.hoc</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    cellRule = netParams.importCellParams(
            label='PYR_HH3D_hoc',
            conds={'cellType': 'PYR', 'cellModel': 'HH3D'},
            fileName='geom.hoc',
            cellName='E21',
            importSynMechs=False)

    cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70} # soma hh mechanism

    for secName in cellRule['secs']:
            cellRule['secs'][secName]['mechs']['pas'] = {'g': 0.0000357, 'e': -70}
            cellRule['secs'][secName]['geom']['cm'] = 1

</div>

</div>

</div>

<div id="hodgkin-huxley-model-with-3d-geometry-from-swc" class="section">

<span id="import-hh3d-swc"></span>

### 3D ジオメトリを含む Hodgkin-Huxley モデル (.swc より)<a href="#hodgkin-huxley-model-with-3d-geometry-from-swc" class="headerlink" title="Link to this heading"></a>

*説明:* SWC ファイルからインポートされた形態を持つマルチコンパートメント セル。セルのジオメトリのみが含まれます。 NetPyNE からジオメトリのみをインポートし、生​​物物理学 (<span class="pre">`hh`</span> および <span class="pre">`pas`</span> チャネル) を追加する例。

SWC ファイルから NetPyNE に形態をインポートするのは簡単ですが、NetPyNE は形態のテストや検証を行わないため、NetPyNE で使用する前に形態ファイルが正確で有効であることを確認する必要があります。

*必要なファイル:* <a href="_downloads/9b8ff172ba6b9cf2b7f89a879447e9fc/BS0284.swc" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">BS0284.swc</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    cellRule = netParams.importCellParams(
            label='PYR_HH3D_swc',
            conds={'cellType': 'PYR', 'cellModel': 'HH3D'},
            fileName='BS0284.swc',
            cellName='swc_cell')

    netParams.renameCellParamsSec('PYR_HH3D_swc_rule', 'soma_0', 'soma')  # rename imported section 'soma_0' to 'soma'

    for secName in cellRule['secs']:
            cellRule['secs'][secName]['mechs']['pas'] = {'g': 0.0000357, 'e': -70}
            cellRule['secs'][secName]['geom']['cm'] = 1
            if secName.startswith('soma'):
                    cellRule['secs'][secName]['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}

</div>

</div>

</div>

<div id="traub-model" class="section">

<span id="import-traub"></span>

### トラウブモデル<a href="#traub-model" class="headerlink" title="Link to this heading"></a>

*説明:* hoc セル テンプレートとして定義された Traub セル モデル。 mod ファイルで定義された複数のメカニズムが必要です。 ModelDB からダウンロードされ、図のプロットなどへの呼び出しを削除するように修正されました。 Traub セル モデルに必要な別の <span class="pre">`km`</span> メカニズムとの衝突を避けるために、<span class="pre">`km`</span> メカニズムは <span class="pre">`km2`</span> という名前に変更されました。 NetPyNE から追加されたシナプス。

ModelDB リンク: <a href="http://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=20756" class="reference external">http://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=20756</a>

*必要なファイル:* <a href="_downloads/ea458eb9d4f2e847e3a67f837a91187f/pyr3_traub.hoc" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">pyr3_traub.hoc</code></span></a>、 <a href="_downloads/161daee69a59cff3e6e2703d06cd82d7/ar.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">ar.mod</code></span></a>、 <a href="_downloads/0e8fdfab16f9a338b062b56db7506cb3/cad.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">cad.mod</code></span></a>、 <a href="_downloads/f5b168e98798c6c52c20f201bd2aec95/cal.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">cal.mod</code></span></a>、 <a href="_downloads/17ac26b8983e1ee35bd12fdf6f5bf51b/cat.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">cat.mod</code></span></a>、 <a href="_downloads/36a4d7863a74aff834fcd80670af1933/k2.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">k2.mod</code></span></a>、 <a href="_downloads/d62b1c118a77f4af29967fe7fda09442/ka.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">ka.mod</code></span></a>、 <a href="_downloads/83686ec32f442bc853014eb6554c5184/kahp.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">kahp.mod</code></span></a>、 <a href="_downloads/43f919c75c2b6dcfa3351f000f96d933/kc.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">kc.mod</code></span></a>、 <a href="_downloads/c589de1deaeb2854bfba1f6e46663ca3/kdr.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">kdr.mod</code></span></a>、 <a href="_downloads/b2f418cbea853fc391f16ad0e8d68442/km2.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">km2.mod</code></span></a>、 <a href="_downloads/01655c2ccfdfc3f84e4eef652dedb95f/naf.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">naf.mod</code></span></a>、 <a href="_downloads/93e82cc8a922d025d5e3111d956f80bc/nap.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">nap.mod</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    cellRule = netParams.importCellParams(
            label='PYR_Traub_rule',
            conds= {'cellType': 'PYR', 'cellModel': 'Traub'},
            fileName='pyr3_traub.hoc',
            cellName='pyr3')

    somaSec = cellRule['secLists']['Soma'][0]

    cellRule['secs'][somaSec]['spikeGenLoc'] = 0.5

</div>

</div>

</div>

<div id="mainen-model" class="section">

<span id="import-mainen"></span>

### メインモデル<a href="#mainen-model" class="headerlink" title="Link to this heading"></a>

*説明:* Python クラスとして定義された Mainen セル モデル。 mod ファイルで定義された複数のメカニズムが必要です。 Adapted to python from hoc ModelDB version. NetPyNE から追加されたシナプス。

ModelDB リンク: <a href="http://senselab.med.yale.edu/ModelDB/showModel.cshtml?model=2488" class="reference external">http://senselab.med.yale.edu/ModelDB/showModel.cshtml?model=2488</a> (旧バージョン)

*必要なファイル:* <a href="_downloads/2ace2a73ef71440a1c1276a8f5728fb2/mainen.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">mainen.py</code></span></a>、 <a href="_downloads/b028e59d9d75c2c0cfd697418958ebc9/cadad.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">cadad.mod</code></span></a>、 <a href="_downloads/e887b5dab8d9348b5b6d728a83b261c2/kca.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">kca.mod</code></span></a>、 <a href="_downloads/44151e617a61f8088fe81e9cdd5b7c14/km.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">km.mod</code></span></a>、 <a href="_downloads/d86525a81cf5f18197bb7d15de5a9bac/kv.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">kv.mod</code></span></a>、 <a href="_downloads/018c2cf1284dfb83235e3e43fa50f01a/naz.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">naz.mod</code></span></a>、 <a href="_downloads/0b74a3837b7f41e7e356603ea10208c8/Nca.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">Nca.mod</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.importCellParams(
            label='PYR_Mainen_rule',
            conds={'cellType': 'PYR', 'cellModel': 'Mainen'},
            fileName='mainen.py',
            cellName='PYR2')

</div>

</div>

</div>

<div id="friesen-model" class="section">

<span id="import-friesen"></span>

### フリーゼンモデル<a href="#friesen-model" class="headerlink" title="Link to this heading"></a>

*必要なファイル:* Python クラスとして定義されたフリーゼン セル モデル。 MOD ファイルで定義された複数のメカニズム (ポイント プロセスを含む) が必要です。スパイクの生成は <span class="pre">`axon`</span> セクション (<span class="pre">`soma`</span> ではありません) で発生します。これは、NetPyNE で <span class="pre">`spikeGenLoc`</span> 項目を <span class="pre">`axon`</span> セクション エントリに追加し、セクションの場所 (例: 0.5) を指定することで示されます。

*必要なファイル:* <a href="_downloads/e668c25c9681ef3c5be036e8f4d3872a/friesen.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">friesen.py</code></span></a>、 <a href="_downloads/bf00fc4452680047008f84184b066041/A.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">A.mod</code></span></a>、 <a href="_downloads/6116be3d1a42bfaf55c3d6e07f2eaf89/GABAa.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">GABAa.mod</code></span></a>、 <a href="_downloads/d757ff23a6fbeed43a12f10e88f90746/AMPA.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">AMPA.mod</code></span></a>、 <a href="_downloads/c42366b26a172dbe16863aeecb40ad0c/NMDA.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">NMDA.mod</code></span></a>、 <a href="_downloads/c0dafcf997edbe098692057ecb510a74/OFThpo.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">OFThpo.mod</code></span></a>、 <a href="_downloads/aebabc8002007a23163c4a177051f96d/OFThresh.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">OFThresh.mod</code></span></a>、 <a href="_downloads/43a63f807924a3df71bcf6587f244569/netcon.inc" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">netcon.inc</code></span></a>、 <a href="_downloads/a1ede0f81d4eb91f1b3588f1d331fd35/ofc.inc" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">ofc.inc</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    cellRule = netParams.importCellParams(
            label='PYR_Friesen_rule',
            conds={'cellType': 'PYR', 'cellModel': 'Friesen'},
            fileName='friesen.py',
            cellName='MakeRSFCELL')

    cellRule['secs']['axon']['spikeGenLoc'] = 0.5  # spike generator location.

</div>

</div>

</div>

<div id="izhikevich-2003a-model-independent-voltage-variable" class="section">

<span id="import-izhi03a"></span>

### Izhikevich 2003a モデル (独立電圧可変)<a href="#izhikevich-2003a-model-independent-voltage-variable" class="headerlink" title="Link to this heading"></a>

*説明:* Izhikevich、2003 年に Python クラスとして定義されたセル モデル。 modファイルで定義されたポイントプロセスが必要です。このバージョンはセクションに追加されますが、セクション電圧またはシナプス メカニズムは使用されません。代わりに、独自の内部電圧変数とシナプス機構を使用します。これは、NetPyNE で <span class="pre">`vref`</span> 項目をポイント プロセス エントリに追加し、内部電圧変数の名前 (<span class="pre">`V`</span>) を指定することで示されます。

Modeldb リンク: <a href="https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948" class="reference external">https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948</a>

*必要なファイル:* <a href="_downloads/8d08bf3426074ba1d2a11b4ce0724c82/izhi2003Wrapper.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2003Wrapper.py</code></span></a>、 <a href="_downloads/7f77449e96e7eb73844d2fd554b6f49f/izhi2003a.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2003a.mod</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    cellRule = netParams.importCellParams(
            label='PYR_Izhi03a_rule',
            conds={'cellType': 'PYR', 'cellModel':'Izhi2003a'},
            fileName='izhi2003Wrapper.py',
            cellName='IzhiCell',
            cellArgs={'type':'tonic spiking', 'host':'dummy'})

    cellRule['secs']['soma']['pointps']['Izhi2003a_0']['vref'] = 'V' # specify that uses its own voltage V

</div>

</div>

</div>

<div id="izhikevich-2003b-model-uses-section-voltage" class="section">

<span id="import-izhi03b"></span>

### Izhikevich 2003b モデル (セクション電圧を使用)<a href="#izhikevich-2003b-model-uses-section-voltage" class="headerlink" title="Link to this heading"></a>

*説明:* Izhikevich、2003 年に Python クラスとして定義されたセル モデル。 modファイルで定義されたポイントプロセスが必要です。このバージョンはセクションに追加され、セクションの電圧とシナプス メカニズムを共有します。シナプス メカニズムは、接続フェーズ中に NetPyNE から追加されます。

Modeldb リンク: <a href="https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948" class="reference external">https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948</a>

*必要なファイル:* <a href="_downloads/8d08bf3426074ba1d2a11b4ce0724c82/izhi2003Wrapper.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2003Wrapper.py</code></span></a>、 <a href="_downloads/a68d222145142bf054af5242677fc8f1/izhi2003b.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2003b.mod</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.importCellParams(
            label='PYR_Izhi03b_rule',
            conds={'cellType': 'PYR', 'cellModel':'Izhi2003b'},
            fileName='izhi2003Wrapper.py',
            cellName='IzhiCell',
            cellArgs={'type':'tonic spiking'})

</div>

</div>

</div>

<div id="izhikevich-2007a-model-independent-voltage-variable" class="section">

<span id="import-izhi07a"></span>

### Izhikevich 2007a モデル (独立電圧可変)<a href="#izhikevich-2007a-model-independent-voltage-variable" class="headerlink" title="Link to this heading"></a>

*説明:* Izhikevich、2007 年のセル モデルは Python クラスとして定義されました。 modファイルで定義されたポイントプロセスが必要です。このバージョンはセクションに追加されますが、セクション電圧またはシナプス メカニズムは使用されません。代わりに、独自の内部電圧変数とシナプス機構を使用します。これは、NetPyNE で <span class="pre">`vref`</span> 項目をポイント プロセス エントリに追加し、内部電圧変数の名前 (<span class="pre">`V`</span>) を指定することで示されます。セル モデルにはいくつかの内部シナプス メカニズムが含まれており、<span class="pre">`synList`</span> 項目をポイント プロセス エントリに追加することで NetPyNE のリストとして指定できます。

Modeldb リンク: <a href="https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948" class="reference external">https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948</a>

*必要なファイル:* <a href="_downloads/86bf4ac58741c2d950ec83cb5cd8e608/izhi2007Wrapper.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2007Wrapper.py</code></span></a>、 <a href="_downloads/78f75a15211ac7ec7d893a735daef5cb/izhi2007a.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2007a.mod</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    cellRule = netParams.importCellParams(
            label='PYR_Izhi07a_rule',
            conds={'cellType': 'PYR', 'cellModel':'Izhi2007a'},
            fileName='izhi2007Wrapper.py',
            cellName='IzhiCell',
            cellArgs={'type':'RS', 'host':'dummy'})

    cellRule['secs']['soma']['pointps']['Izhi2007a_0']['vref'] = 'V' # specify that uses its own voltage V

    cellRule['secs']['soma']['pointps']['Izhi2007a_0']['synList'] = ['AMPA', 'NMDA', 'GABAA', 'GABAB']  # specify its own synapses

</div>

</div>

</div>

<div id="izhikevich-2007b-model-uses-section-voltage" class="section">

<span id="import-izhi07b"></span>

### Izhikevich 2007b モデル (セクション電圧を使用)<a href="#izhikevich-2007b-model-uses-section-voltage" class="headerlink" title="Link to this heading"></a>

*説明:* Izhikevich、2007 年に Python クラスとして定義されたセル モデル。 modファイルで定義されたポイントプロセスが必要です。このバージョンはセクションに追加され、セクションの電圧とシナプス メカニズムを共有します。

Modeldb リンク: <a href="https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948" class="reference external">https://senselab.med.yale.edu/modeldb/showModel.cshtml?model=39948</a>

*必要なファイル:* <a href="_downloads/86bf4ac58741c2d950ec83cb5cd8e608/izhi2007Wrapper.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2007Wrapper.py</code></span></a>、 <a href="_downloads/803a7312bae028b7a24ba7f3e28de705/izhi2007b.mod" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">izhi2007b.mod</code></span></a>

*NetPyNE コード:*

<div class="highlight-default notranslate">

<div class="highlight">

    netParams.importCellParams(
            label='PYR_Izhi07b_rule',
            conds={'cellType': 'PYR', 'cellModel':'Izhi2007b'},
            fileName='izhi2007Wrapper.py',
            cellName='IzhiCell',
            cellArgs={'type':'RS'})

</div>

</div>

上記のすべてのセル モデルをインポートし、それらを使用してネットワークを作成するための完全なコードは、<a href="_downloads/1355b1c6c896576bcc1108a87fadb5c5/tut_import.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut_import.py</code></span></a> から入手できます。

</div>

</div>

<div id="parameter-optimization-of-a-simple-neural-network-using-an-evolutionary-algorithm" class="section">

## 進化的アルゴリズムを使用した単純なニューラル ネットワークのパラメーター最適化<a href="#parameter-optimization-of-a-simple-neural-network-using-an-evolutionary-algorithm" class="headerlink" title="Link to this heading"></a>

このチュートリアルでは、進化的アルゴリズム ツールキットである <a href="https://www.google.com/url?q=https://pypi.python.org/pypi/inspyred&amp;sa=D&amp;ust=1498757041054000&amp;usg=AFQjCNFsnbnVRsDVjaPnkPZvpkGEUhvqmA" class="reference external">inspyred</a> を使用して、目標の平均発火率を達成できるように、以前の <a href="https://www.google.com/url?q=http://www.neurosimlab.org/netpyne/tutorial.html?highlight%3Dtut2%23network-parameters-tutorial-2&amp;sa=D&amp;ust=1498757041054000&amp;usg=AFQjCNHhqESFuColxjg-1qT_Y_qvNbOISg" class="reference external">tut2.py</a>\*\* ニューラル ネットワークのパラメーターを最適化して、ネットワーク シミュレーションの開始と出力表示に関連するコードを削除する方法の例を示します。 (~) 17 Hz あたり。

\*\*ネットワーク シミュレーションの開始と出力表示に関連するコードを削除するには、tut2.py コードの終わり近くでいくつかの変更が必要ですが、これらはすべて新しいトップレベル コードで処理されるようになりました。 (<a href="_downloads/69d79965d70368743cfae5251deffdfd/tut_optimization.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut_optimization.py</code></span></a>):

<div class="highlight-python notranslate">

<div class="highlight">

    # Create network and run simulation
    # sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)   # line commented out

    # import pylab; pylab.show()  # if figures appear empty   # line commented out

</div>

</div>

tut2.py からの抜粋

<div id="additional-background-reading" class="section">

### 追加の背景情報<a href="#additional-background-reading" class="headerlink" title="Link to this heading"></a>

<a href="https://www.google.com/url?q=https://en.wikipedia.org/wiki/Evolutionary_algorithm&amp;sa=D&amp;ust=1498757041056000&amp;usg=AFQjCNH6OIVTnmce_hlIexUok_PoJcZomA" class="reference external">アルゴリズムの説明</a> この例で単純なニューラル ネットワークを最適化するために使用される方法論。

</div>

<div id="introduction" class="section">

### はじめに<a href="#introduction" class="headerlink" title="Link to this heading"></a>

inspyred Python パッケージを使用してニューラル ネットワーク パラメーターを見つけ、ネットワークの一部のプロパティ (発射速度など) が目的のターゲットと一致するようにする手順は、3 つのステップに分けることができます。まず、1) 目的のターゲット モデル (この場合は、何らかの測定可能な値) と適合度関数を定義します。ここでの適合度は、指定されたパラメーターを持つニューラル ネットワークがターゲットにどの程度一致するかを表す計算可能な値として定義されます。次に、2) そのモデル/値を達成するために変更する適切なニューラル ネットワーク パラメーターを決定する必要があります。最後に、3) 進化的アルゴリズムの適切なパラメータが定義されます。最終的に、進化的アルゴリズムへの入力が適切であれば、連続的な反復を通じて、進化的アルゴリズムによって決定されたパラメーターによってターゲットに近いモデルが生成されるはずです。

これら 3 つのステップを例に具体化すると、次のようになります。

<a href="_images/tut_optimization_diagram.png" class="reference internal image-reference"><img src="_images/tut_optimization_diagram.png" class="align-center" style="width: 80%;" alt="_images/tut_optimization_diagram.png" /></a>

1. 目的のターゲット モデルとフィットネス関数を定義します。

目的のターゲット モデルの定義はほとんど任意ですが、結果が以前よりもターゲット モデルに近づくように（または適合度が向上するように）パラメーターを調整する方法が必要であることや、指定されたパラメーターでモデルの適合性を評価する方法が必要であることなどの制約があります。この場合、ターゲット モデルは、平均発火速度 17 Hz を達成するニューラル ネットワークです。このようなモデルの適合性は、特定のモデルの平均発火率と 17 Hz の目標発火率との差として定義できます。

2. 最適化するモデルパラメータを選択します。

パラメーターが何らかの方法で最終モデルの適合性を変更できる場合、モデルが何を達成しようとしているかに応じて、そのパラメーターは最適化の適切な候補となる可能性があります。他の多くのパラメーターと同様に、ニューラル ネットワーク内のシナプス接続の確率、重み、遅延を変更すると、平均発火率に影響を与える可能性があります。この例では、感覚集団から運動集団への接続の確率、重み、遅延の値を最適化します。

3. 進化的アルゴリズムに適切なパラメータを選択します。

inspyred では、次のような進化的アルゴリズムのさまざまなコンポーネントをカスタマイズできます。

- どのパラメータ値のセットが親になるかを決定するセレクター、つまり、進化の反復において次の世代を形成するためにどのパラメータ値が使用されるかを決定します。

- パラメータセットの現在の各反復が前の反復からどのように形成されるかを決定するバリエーター、

- 以前のパラメータ値のセットを次の反復に持ち込むかどうかを決定する置換器、

- 進化の反復をいつ終了するかを定義するターミネータ、

- 進化の各反復を通じてパラメータ値の追跡を可能にするオブザーバー。

</div>

<div id="using-inspyred" class="section">

### inspyred<a href="#using-inspyred" class="headerlink" title="Link to this heading"></a> の使用

進化的アルゴリズムは、inspyred パッケージの ec モジュールに実装されています。

<div class="highlight-python notranslate">

<div class="highlight">

    from inspyred import ec # import evolutionary computation from inspyred

</div>

</div>

tut_optimization.py からの抜粋

ec には、進化的計算アルゴリズムのクラス ec.EevolutionaryComputation() が含まれており、パラメーターを入力してアルゴリズムをカスタマイズできます。進化アルゴリズムにはランダムなプロセス (遺伝子のランダムな変異など) が含まれるため、乱数発生器が必要です。この場合、Python の Random() メソッドを使用します。これは、将来結果を再現できるように、特定のシード値を使用して初期化します。

<div class="highlight-python notranslate">

<div class="highlight">

    # create random seed for evolutionary computation algorithm
    rand = Random()
    rand.seed(1)

    # instantiate evolutionary computation algorithm
    my_ec = ec.EvolutionaryComputation(rand)

</div>

</div>

tut_optimization.py からの抜粋

次に、さまざまなバリエーター、リプレイサー、ターミネーター、オブザーバー要素（基本的にアルゴリズムの特定のコンポーネントを切り替える）を ec.selector、ec.variators、ec.replacers、ec.terminators、ec.observers に割り当てることにより、ec 進化計算インスタンス用に進化アルゴリズムのパラメーターが確立されます。

<div class="highlight-python notranslate">

<div class="highlight">

    #toggle variators
    my_ec.variator = [ec.variators.uniform_crossover, # implement uniform crossover & gaussian replacement
                    ec.variators.gaussian_mutation]
    my_ec.replacer = ec.replacers.generational_replacement   # implement generational replacement

    my_ec.terminator = ec.terminators.evaluation_termination # termination dictated by no. evaluations

    #toggle observers
    my_ec.observer = [ec.observers.stats_observer,  # print evolutionary computation statistics
                    ec.observers.plot_observer,   # plot output of the evolutionary computation as graph
                    ec.observers.best_observer]   # print the best individual in the population to screen

</div>

</div>

ex_optimization.py からの抜粋

どこ：

|  |  |
|----|----|
| ec.variators.uniform_crossover |コインを投げて「お母さん」要素または「お父さん」要素が子孫に継承されるかどうかを決定するバリエーター |
| ec.variators.gaussian_mutation | variator は、my_ec.evolve(…,bounder=ec.Bounder(minParamValues, maxParamValues) ,…) | で指定されている境界関数を利用するガウス突然変異を実装します。
| ec.replacers.generational_replacement | replacer はエリート主義による世代置換を実装します ( my_ec.evolve(…,num_elites=1,…) で指定されているように、既存の世代が子孫に置き換えられ、 \<num_elites\> 既存の個体は子孫よりも適応度が優れている場合に生き残ります。
| ec.terminators.評価_終了 |ターミネーターは、発生した評価の数に基づいて実行されます。
| ec.observers.stats_observer |生成された個体 (パラメータ セット) のうち、次の進化反復で選択される個体の数を示します。 |
| ec.observers.plot_observer |は突然変異の割合、つまり前の世代から取得された各パラメータ (確率、重み、遅延) の値が次の世代で変更される割合を示します。
| ec.observers.best_observer |最適化されるパラメータの数を \[確率、重み、遅延\] の長さに対応する 3 に設定します。 |

これらの事前定義されたセレクター、バリエーター、リプレイサー、ターミネーター、およびオブザーバー要素、およびその他のオプションは、<a href="https://www.google.com/url?q=http://pythonhosted.org/inspyred/reference.html&amp;sa=D&amp;ust=1498757041077000&amp;usg=AFQjCNFBCOo0cPqRvxb64xHSlOOQANVWcw" class="reference external">inspyred ドキュメント</a> にあります。

最後に、進化的計算アルゴリズムのインスタンスには、メソッド my_ec.evolve() が含まれています。このメソッドは、終了条件が達成されるまで、さまざまなパラメーター セットを評価する連続的な進化的反復を実行します。この関数には複数の引数があり、2 つの重要な引数はジェネレーター関数とエバリュエーター関数です。 my_ec.evolve() の関数呼び出しは次のようになります。

<div class="highlight-python notranslate">

<div class="highlight">

    # call evolution iterator

    final_pop = my_ec.evolve(generator=generate_netparams, # assign model parameter generator to iterator generator
                          evaluator=evaluate_netparams, # assign fitness function to iterator evaluator
                          pop_size=10,
                          maximize=False,
                          bounder=ec.Bounder(minParamValues, maxParamValues),
                          max_evaluations=50,
                          num_selected=10,
                          mutation_rate=0.2,
                          num_inputs=3,
                          num_elites=1)

</div>

</div>

tut_optimization.py からの抜粋

どこ：

<table class="docutils align-default">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="row-odd">
<td><p>pop_size=10</p></td>
<td><p>パラメータ セットの各世代が 10 人の個人で構成されることを意味します</p></td>
</tr>
<tr class="row-even">
<td><p>maximize=False</p></td>
<td><p>モデルの発火周波数と 17 Hz の差に関する最小値に対応するためにより高い適合度を採用していることを意味します</p></td>
</tr>
<tr class="row-odd">
<td><dl>
<dt>bounder=ec.Bounder(minParamValues,</dt>
<dd>
<p>maxParamValues)</p>
</dd>
</dl></td>
<td><p>各パラメータの境界を定義します。最適化しようとしているパラメーターの最小値と最大値を記述する形式: minParamValues は [確率、重み、遅延] に対応する最小値の配列であり、maxParamValues は最大値の配列です。</p></td>
</tr>
<tr class="row-even">
<td><p>max_evaluations=50</p></td>
<td><p>進化的反復の終了前に評価されるパラメータ セットの数を示します</p></td>
</tr>
<tr class="row-odd">
<td><p>num_selected=10</p></td>
<td><p>生成された個体 (パラメータ セット) のうち、次の進化反復で選択される個体数を示します。</p></td>
</tr>
<tr class="row-even">
<td><p>変異率=0.2</p></td>
<td><p>突然変異の割合、つまり前の世代から取得された各パラメータ (確率、重み、遅延) の値が次世代で変更される割合を示します</p></td>
</tr>
<tr class="row-odd">
<td><p>num_inputs=3</p></td>
<td><p>[確率、重み、遅延] の長さに対応して、最適化されるパラメーターの数を 3 に設定します。</p></td>
</tr>
<tr class="row-even">
<td><p>num_elites=1</p></td>
<td><p>は、エリートの数を 1 に設定します。つまり、子孫から選択された個体よりも適応度が高い場合、既存の世代から 1 つの個体を (完全な世代置換ではなく) 保持することができます。</p></td>
</tr>
</tbody>
</table>

ジェネレーターとエバリュエーターの引数は入力としてユーザー定義関数を期待します。ジェネレーターは最初の反復の初期パラメーター値セットの母集団を定義するために使用され、エバリュエーターは各モデルがターゲットにどれだけ近いかを評価するために使用される適合度関数です。この例では、ジェネレーターは、パラメーター化された一様分布から描画することによってパラメーター値の初期セット (つまり、 \[確率、重み、遅延\] ) を作成する非常に単純な関数です。

<div class="highlight-python notranslate">

<div class="highlight">

    # return a set of initialParams which contains a [probability, weight, delay]

    def generate_netparams(random, args):

        size = args.get('num_inputs')
        initialParams = [random.uniform(minParamValues[i], maxParamValues[i]) for i in range(size)]

    return initialParams

</div>

</div>

tut_optimization.py からの抜粋

適応度関数には、パラメーター値のセットのリスト、つまり \[ \[ a0, b0, c0\], \[a1, b1, c1\], \[a2, b2, c2\], … , \[an, bn, cn \] \] を取得することが含まれます。ここで、a、b、c はパラメーター値を表し、1 ～ n は母集団内の個々の番号を表し、リストの各要素の適合性スコアを計算して返されます。パラメータ値の初期セットに対応する適応度値のリスト（つまり、 \[ f0, f1, f2, … , fn \] ）として。これは一般的なテンプレートに従います。

<div class="highlight-python notranslate">

<div class="highlight">

    def evaluate_fitness(candidates, args):
       fitness = []
       for candidate in candidates:
           fit = some_fitness_function(candidate)
           fitness.append(fit)
       return fitness

</div>

</div>

tut_optimization.py からの抜粋

some_fitness_function(candidate) として機能するために使用される実際のコードを以下に説明します。

</div>

<div id="overview-of-the-fitness-function" class="section">

### フィットネス機能の概要<a href="#overview-of-the-fitness-function" class="headerlink" title="Link to this heading"></a>

この場合のフィットネス関数には、1) 指定されたパラメーターを使用してニューラル ネットワークを作成し、2) それをシミュレートして平均発火率を見つけ、次に 3) この発火率を目標発火率と比較することが含まれます。

1. 評価するパラメータを使用してニューラル ネットワークを作成する

tut2.py で NetPyNE 定義のネットワークを使用し、\[確率、重み、遅延\] パラメータを変更します。これには、S 母集団と M 母集団の間の接続ルール内にある tut2.py 内の特定の値の再定義が含まれます: netParams.connParams\[‘S-\>M’\]

<div class="highlight-python notranslate">

<div class="highlight">

    ## Cell connectivity rules
    netParams.connParams['S->M'] = {      #  S -> M label
          'preConds': {'popLabel': 'S'},  # conditions of presyn cells
          'postConds': {'popLabel': 'M'}, # conditions of postsyn cells
          'probability': 0.5,             # probability of connection <-- to be optimized by evolutionary algorithm
          'weight': 0.01,                 # synaptic weight           <-- to be optimized by evolutionary algorithm
          'delay': 5,                     # transmission delay (ms)   <-- to be optimized by evolutionary algorithm
          'synMech': 'exc'}               # synaptic mechanism

</div>

</div>

tut2.py からの抜粋

これらの値は、適応度関数内で、進化的アルゴリズムによって生成されたパラメーター値に置き換えられます。適応度関数は候補のリストを反復処理する for ループ内に存在するため (for icand,cand in enumerate(candidates): )、個々のパラメーターには cand\[0\]、cand\[1\]、cand\[2\] としてアクセスできます。 tut_optimization.py のパラメータに値を再割り当てするには、次の行を使用します。

<div class="highlight-python notranslate">

<div class="highlight">

    tut2.netParams.connParams['S->M']['<parameter>'] = <value>

</div>

</div>

2. 作成したニューラルネットワークをシミュレーションし、平均発火率を求める

ネットワーク パラメーターを変更したら、sim.createSimulate() NetPyNE 関数を呼び出してシミュレーションを実行できます。変更したばかりの tut2 netParams オブジェクトと simConfig オブジェクトを引数として渡します。シミュレーションが実行されると、sim.simData を介してシミュレーション出力にアクセスできるようになります。

<div class="highlight-default notranslate">

<div class="highlight">

    # create network
    sim.createSimulate(netParams=tut2.netParams, simConfig=tut2.simConfig)

</div>

</div>

tut_optimization.py からの抜粋

3. 平均発火率と目標平均発火率の比較

ネットワークの平均発火率 (スパイク/秒 = Hz) を計算するには、シミュレーション中に発生したスパイクをニューロンの数と継続時間で除算します。スパイク時間のリストとニューロンのリストには、NetPyNE sim モジュール sim.simData\[‘spkt’\] および sim.net.cells を介してアクセスできます。これらは、 sim.createSimulate() の実行後に設定されます。これらのリストから、スパイク時間とニューロンの数を取得するには、Python の len() 関数を使用します。シミュレーションの継続時間には、tut_optimization.py コードで tut2.simConfig.duration を介してアクセスできます。  したがって、平均発火率の計算は次のようになります。

<div class="highlight-python notranslate">

<div class="highlight">

    # calculate firing rate
    numSpikes = float(len(sim.simData['spkt']))
    numCells = float(len(sim.net.cells))
    duration = tut2.simConfig.duration/1000.0
    netFiring = numSpikes/numCells/duration

</div>

</div>

tut_optimization.py からの抜粋

最後に、モデルの平均発火率が次のように目標発火率と比較されます。

<div class="highlight-python notranslate">

<div class="highlight">

    # calculate fitness for this candidate
    fitness = abs(targetFiring - netFiring)  # minimize absolute difference in firing rate

</div>

</div>

tut_optimization.py からの抜粋

</div>

<div id="displaying-findings" class="section">

### 結果の表示<a href="#displaying-findings" class="headerlink" title="Link to this heading"></a>

進化的アルゴリズムの結果は、標準出力 (端末) に表示されるほか、matplotlib パッケージを使用してプロットされます。次の行は、イテレータ内のさまざまな候補の結果の表示に関連しています。

<div class="highlight-python notranslate">

<div class="highlight">

    for icand,cand in enumerate(candidates):
          ...
          print '\n CHILD/CANDIDATE %d: Network with prob:%.2f, weight:%.2f, delay:%.1f \n  firing rate: %.1f, FITNESS = %.2f \n'\
          %(icand, cand[0], cand[1], cand[2], netFiring, fitness)

</div>

</div>

tut_optimization.py からの抜粋

最初の行: for icand,cand in enumerate(candidates): は、上記の疑似コード例で使用されている反復子 for candidate in candidates: に似ていますが、enumerate() 関数はリスト内の各要素に対して 0 から始まるインデックスも返し、後続の print ステートメントで使用される点が異なります。

この例では、17 Hz に最も近い平均周波数を持つ生成された候補も表示されます。この候補は最終世代に存在し、最高の適合度スコア (最小差に相当) を持ちます。 num_elites=1 なので、前の世代により良い適応度を持つ候補者が存在するリスクはありません。

進化の終了後、最高の適合度スコアを持つ候補にアクセスするために、 my_ec.evolve() 関数によって返される最終世代の候補が逆順に並べ替えられ (最小値から最大値へ)、17 Hz に最も近い平均発火率を達成する (したがって最小の差を持つ) 候補がリストの先頭 (または位置 0) に配置されます。 NetPyNE を使用して、最適化されたパラメーターを設定し、ネットワークをシミュレートし、ラスター プロットをプロットすることにより、このネットワークの出力を視覚化します。このタスクを実行するコードは以下に分離されています。

<div class="highlight-python notranslate">

<div class="highlight">

    final_pop = my_ec.evolve(...)
    ...
    # plot raster of top solutions
    final_pop.sort(reverse=True)         # sort final population so best fitness (minimum difference) is first in list
    bestCand = final_pop[0].candidate   # bestCand <-- candidate in first position of list
    tut2.simConfig.analysis['plotRaster'] = True                      # plotting
    tut2.netParams.connParams['S->M']['probability'] = bestCand[0]    # set tut2 values to corresponding
    tut2.netParams.connParams['S->M']['weight'] = bestCand[1]         # best candidate values
    tut2.netParams.connParams['S->M']['delay'] = bestCand[2]
    sim.createSimulateAnalyze(netParams=tut2.netParams, simConfig=tut2.simConfig) # run simulation

</div>

</div>

tut_optimization.py からの抜粋

このチュートリアルで使用される進化的アルゴリズムによるニューラル ネットワーク最適化のコードは、<a href="_downloads/69d79965d70368743cfae5251deffdfd/tut_optimization.py" class="reference download internal" download=""><span class="pre"><code class="xref download docutils literal notranslate">tut_optimization.py</code></span></a> にあります。

</div>

</div>

<div id="running-a-batch-job-beta" class="section">

## バッチ ジョブの実行 (ベータ)<a href="#running-a-batch-job-beta" class="headerlink" title="Link to this heading"></a>

NetPyNE <span class="pre">`batchtools`</span> サブパッケージは、ディスパッチャ \<-\> ランナー通信モデルに基づいて、シミュレーションの送信を自動化し、結果を分析のために結合する新しい方法を提供します。現在、パラメータの最適化とチェックポイント設定に <span class="pre">`Ray`</span>` `<span class="pre">`Tune`</span> パッケージを使用しています。これにより、幅広い最先端の最適化アルゴリズムと効率的な並列化とスケーラビリティが提供されます。

<span class="pre">`batchtools`</span> オブジェクトとインターフェイスは直接処理できますが、すべてを一般的なユースケースに適用できる単純なラッパー コマンドに統合し、自動化しました。自動パラメーター検索は、<span class="pre">`netpyne.batchtools.search`</span> を通じて検索スペースとアルゴリズムを指定することで実装できます。モデル パラメーターの定義は引き続き <span class="pre">`netpyne.specs`</span> によって処理され、シミュレーション結果の通信は <span class="pre">`netpyne.sim`</span> によって処理されます。

以下は、NetPyNE モデルに必要な 4 つの主要なファイル netParams.py、cfg.py、init.py、search.py​​ (バッチ パラメーターの最適化/検索の定義に使用) 内のラッパー コマンド間の相互作用の図です。

<a href="_images/batchtools_netpyne.png" class="reference internal image-reference"><img src="_images/batchtools_netpyne.png" class="align-center" style="width: 90%;" alt="_images/batchtools_netpyne.png" /></a>

<div id="setting-up-batchtools" class="section">

### 1. バッチツール<a href="#setting-up-batchtools" class="headerlink" title="Link to this heading"></a>のセットアップ

NetPyNE と NEURON のインストールに加えて、次の pip インストールが必要です。

<div class="highlight-default notranslate">

<div class="highlight">

    pip install -U ray
    pip install -U batchtk

</div>

</div>

<span class="pre">`batchtk`</span> は NetPyNE <span class="pre">`batchtools`</span> サブパッケージ、<span class="pre">`ray`</span> はバッチツールの依存関係である Ray Tune パッケージです。

これらのパッケージの最新の修正を可能にするには、NetPyNE とバッチtk を開発用インストールとしてセットアップする必要があります。

<div class="highlight-default notranslate">

<div class="highlight">

    git clone https://github.com/suny-downstate-medical-center/netpyne.git
    cd netpyne
    pip install -e .

    git clone https://github.com/suny-downstate-medical-center/batchtk.git
    cd batchtk
    pip install -e .

</div>

</div>

対話型 Python インスタンスで <span class="pre">`sim.send`</span> メソッドと <span class="pre">`cfg.update`</span> メソッドをチェックすることで、正しいパッケージがインストールされていることを検証できます。

<div class="highlight-default notranslate">

<div class="highlight">

    In [1]: from netpyne import sim, specs
    Warning: no DISPLAY environment variable.
    --No graphics will be displayed.
    numprocs=1

    In [2]: help(sim.send)
    Help on method send in module netpyne.batchtools.comm:

    send(data) method of netpyne.batchtools.comm.Comm instance


    In [3]: cfg = specs.SimConfig()

    In [4]: help(cfg.update)
    Help on method update in module netpyne.batchtools.runners:
    ...

</div>

</div>

インストールに問題がある場合、いずれかの機能のヘルプを呼び出すと、代わりに次のメッセージが表示されます。

<div class="highlight-default notranslate">

<div class="highlight">

    In [2]: help(sim.send)
    Help on function send in module netpyne.sim:

    send(*args, **kwargs)
    This method is implemented in batchtools,
    which requires the batchtk package to be
    installed. If you are seeing this message
    when calling help, it indicates there is
    an issue with your current batchtools
    installation

</div>

</div>

関連するメソッドは例外を発生させずに呼び出すことができますが、プレースホルダーとしてのみ機能します。

</div>

<div id="examples" class="section">

### 2. 例<a href="#examples" class="headerlink" title="Link to this heading"></a>

NetPyNE バッチツールの使用例は、NetPyNE github</a> の <span class="pre">`examples`</span> ディレクトリ <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples" class="reference external"> にあります。

基礎となるバッチtk パッケージの例は、batchtk github</a> の <span class="pre">`examples`</span> ディレクトリ <a href="https://github.com/suny-downstate-medical-center/batchtk/tree/release/examples" class="reference external"> にあります。

</div>

<div id="retrieving-batch-configuration-values-through-the-specs-object" class="section">

### 3. <span class="pre">`specs`</span> オブジェクトを介したバッチ構成値の取得<a href="#retrieving-batch-configuration-values-through-the-specs-object" class="headerlink" title="Link to this heading"></a>

各シミュレーションは、<span class="pre">`specs`</span> オブジェクトを通じて関連するバッチ構成を取得し、<span class="pre">`netpyne.sim`</span> 内の <span class="pre">`send`</span> 関数を通じてバッチ ディスパッチャーと通信できます。

まず、関連するオブジェクトをインポートします。

<div class="highlight-python notranslate">

<div class="highlight">

    from netpyne import specs, sim
    cfg = specs.SimConfig()  # create a SimConfig object, can be provided with a dictionary on initial call to set initial values
    netParams = specs.NetParams()  # create a netParams object

</div>

</div>

<span class="pre">`batchtk`</span> モジュールが適切にインストールされている場合、元の <span class="pre">`specs.SimConfig`</span> オブジェクトが、<span class="pre">`help()`</span> または <span class="pre">`type()`</span> を通じてクエリできる開発版 <span class="pre">`batchtools`</span> バージョンに自動的に置き換えられます。

<div class="highlight-python notranslate">

<div class="highlight">

    cfg = specs.SimConfig()
    help(cfg)

</div>

</div>

上記のコード ブロックの切り詰められた出力:

<div class="highlight-python notranslate">

<div class="highlight">

    # Output
    Help on Runner_SimConfig in module netpyne.batchtools.runners object:

    class Runner_SimConfig(batchtk.runtk.runners.Runner, netpyne.specs.simConfig.SimConfig)

</div>

</div>

この更新された <span class="pre">`cfg`</span> インスタンスは、この特定のバッチ ジョブの初期化時に作成された関連構成マッピングを自動的にキャプチャします。これらのマッピングは、<span class="pre">`cfg.get_mappings()`</span> 経由で取得できます。

次のステップでは、<span class="pre">`cfg.update()`</span> を呼び出して、このバッチ ジョブに関連するマッピングで cfg 値を更新します。

<div class="highlight-python notranslate">

<div class="highlight">

    from netpyne  import specs           # import the custom batch specs
    cfg = specs.SimConfig()              # create a SimConfig object
    cfg.update()                         # update the cfg object with any relevant mappings for this particular batch job

</div>

</div>

以下に示すように、<span class="pre">`update`</span> メソッドは、引数呼び出しで指定された値で *最初に *、次に* バッチ ジョブの構成マッピング (つまり、<span class="pre">`cfg.get_mappings()`</span> によって取得された) で <span class="pre">`SimConfig`</span> オブジェクトを更新します。

<div class="highlight-python notranslate">

<div class="highlight">

    from netpyne import specs                     # import the custom batch specs
    cfg = specs.SimConfig({'foo': 0, 'bar': 1, 'baz': 2})    # create a SimConfig object, initializes it with a dictionary {'foo': 0} such that
    assert cfg.foo == 0                                      # cfg.foo == 0
    assert cfg.bar == 1                                      # cfg.bar == 1
    assert cfg.baz == 2                                      # cfg.baz == 2
    cfg.update({'foo': 3})                                   # update the cfg object with any relevant mappings for this particular batch job
    assert cfg.foo == 3                                      # cfg.foo == 3
    assert cfg.bar == 1                                      # cfg.bar remains unchanged
    assert cfg.baz == 2                                      # cfg.baz remains unchanged

</div>

</div>

これは、バッチ ジョブの送信からのマッピングで SimConfig オブジェクトを更新するための以前の NetPyNE コードを置き換えます。

</div>

<div id="additional-functionality-within-the-simconfig-object" class="section">

### 4. simConfig オブジェクト内の追加機能<a href="#additional-functionality-within-the-simconfig-object" class="headerlink" title="Link to this heading"></a>

メソッド <span class="pre">`cfg.update()`</span> は、オプションの引数 <span class="pre">`force_match`</span> もサポートします。これにより、更新ディクショナリ内の値が <span class="pre">`SimConfig`</span> オブジェクト内の既存の属性と強制的に一致します。実行時に <span class="pre">`SimConfig`</span> オブジェクト内に新しい属性が誤って作成されていないかどうかを確認するために、デバッグ中にこの設定を <span class="pre">`True`</span> に設定することをお勧めします。

<div class="highlight-python notranslate">

<div class="highlight">

    from netpyne.batchtools import specs                     # import the custom batch specs
    cfg = specs.SimConfig({'type': 0})                       # create a SimConfig object, initializes it with a dictionary {'type': 0} such that
    assert cfg.foo == 0                                      # cfg.type == 0
    try:
        cfg.update({'typo': 1}, force_match=True)            # cfg.typo is not defined, so this line will raise an AttributeError
    except Exception as e:
        print(e)
    cfg.update({'typo': 1})                                  # without force_match, the typo attribute is created and set to 1
    assert cfg.type == 0                                     # cfg.type remains unchanged due to a typo in the attribute name 'type' -> 'typo'
    assert cfg.typo == 1                                     # instead, cfg.typo is created and set to the value 1

</div>

</div>

<span class="pre">`specs.SimConfig()`</span> を使用した <span class="pre">`cfg`</span> オブジェクトの初期化と、その後の <span class="pre">`cfg.update()`</span> の呼び出しの両方で、ドット表記とネストされたコンテナーの両方が処理されます。

<div class="highlight-python notranslate">

<div class="highlight">

    from netpyne.batchtools import specs
    cfg = specs.SimConfig({'foo': {'val0': 0, 'arr0': [0, 1, 2]}})
    assert cfg.foo['val0'] == 0
    assert cfg.foo['arr0'][0] == 0
    cfg.update({'foo': {'val0': 10,           # update cfg.foo['val0'] to 10
                        'arr0': {0: 20        # update cfg.arr0[0] to 20
                                 1: 30}}})    # update cfg.arr0[1] to 30
    assert cfg.foo['val0'] == 10
    assert cfg.foo['arr0'][0] == 20
    assert cfg.foo['arr0'][1] == 30
    assert cfg.foo['arr0'][2] == 2            # cfg.arr0[2] remains unchanged

</div>

</div>

提供された辞書による <span class="pre">`cfg`</span> オブジェクトの更新は、バッチ検索で指定されたパラメーターで更新する前に行われます。

</div>

<div id="communicating-results-to-the-search-algorithm-via-sockets-using-the-sim-send-function" class="section">

### 5. <span class="pre">`sim.send`</span> 関数<a href="#communicating-results-to-the-search-algorithm-via-sockets-using-the-sim-send-function" class="headerlink" title="Link to this heading"></a> を使用して、ソケット経由で検索アルゴリズムに結果を伝達します。

以前のバッチ シミュレーションは、データの通信に <span class="pre">`.pkl`</span> ファイルに依存していました。照合を容易にするために、シミュレーションの終了時に特定のデータ値をソケット経由で直接送信できます。

- **sim.send(\<data\>)**: <span class="pre">`<data>`</span> をバッチ <span class="pre">`dispatcher`</span> に送信します

<span class="pre">`search`</span> ジョブの場合、送信されたデータを検索関数で指定されたメトリックと照合することが重要です。たとえば、検索呼び出しでメトリクス「損失」を指定する場合、<span class="pre">`sim.send`</span> はキーと値のペア <span class="pre">`{'loss':`</span>` `<span class="pre">`<value>}`</span> を指定する必要があります。

</div>

<div id="specifying-a-batch-job" class="section">

### 6. バッチジョブの指定<a href="#specifying-a-batch-job" class="headerlink" title="Link to this heading"></a>

バッチ ジョブ処理は <span class="pre">`netpyne.batchtools.search`</span> から実装されます。以下は、<span class="pre">`search`</span> 関数に関連する引数の選択です。引数の完全なリストは、次の呼び出しで入手できます。

<div class="highlight-python notranslate">

<div class="highlight">

    from netpyne.batchtools import search
    help(search)

</div>

</div>

**検索 API (切り捨て):**

<div class="highlight-python notranslate">

<div class="highlight">

    def search(
          job_type: Optional[str] = None, # the submission engine to run a single simulation (e.g. 'sge', 'sh')
          comm_type: Optional[str] = None, # the method of communication between host dispatcher and the simulation (e.g. 'socket', 'filesystem')
          run_config: Optional[dict] = None,  # batch configuration, (keyword: string pairs to customize the submit template)
          params: Optional[dict] = None,  # search space (dictionary of parameter keys: tune search spaces)
          algorithm: Optional[str] = "variant_generator", # search algorithm to use, see SEARCH_ALG_IMPORT for available options
          label: Optional[str] = "search",  # label for the search, any files generated will be prefixed with this string
          output_path: Optional[str] = './batch',  # directory for storing generated files, either relative to the current working directory if starting with '.' or an absolute path if starting with '/'
          checkpoint_path: Optional[str] = './checkpoint',  # directory for storing checkpoint files, either relative to the current working directory if starting with '.' or an absolute path if starting with '/'
          max_concurrent: Optional[int] = 1,  # number of concurrent trials to run at one time
          num_samples: Optional[int] = 1,  # number of trials to run; for parameter grids, a value of 1 means that the search will sample the parameter space of each value in the grid
          metric: Optional[str] = None, # metric to optimize (this should match some key: value pair in the returned data)
          mode: Optional[str] = "min",  # either 'min' or 'max' (whether to minimize or maximize the metric)
          sample_interval: Optional[int] = 15,  # interval to poll for new results (in seconds)
          attempt_restore: Optional[bool] = True, # whether to attempt to restore from a checkpoint
          file_cleanup: Optional[bool] = True, # whether to clean up accessory files after the search is completed
          advanced_logging: Optional[bool|str] = True, # advanced logging including generation of a batch .log file and an sqlite .db file (will be created in a timestamped directory by default).
          ) -> study: # results of the search

</div>

</div>

<span class="pre">`search`</span> 関数で実装されたデフォルトのパラメーター検索は、検索アルゴリズムのバックエンドとして <span class="pre">`ray.tune`</span> を使用し、結果を保存する .csv を作成し、出力を含む <span class="pre">`study`</span> オブジェクトを返します。次の 2 つのパラメータを取ります。

- **job_type**: ジョブの送信方法を指定します。 **「sge」** は、Sun Grid Engine を通じてバッチ ジョブを送信します。 **「sh」** は、ローカル マシン上のシェルを通じてバッチ ジョブを送信します。 **「ssh_slurm」** または「ssh_sge」は、SSH 接続を介して Slurm ワークロード マネージャーまたは Sun Grid Engine を通じてバッチ ジョブを送信します。

- **comm_type**: ジョブがディスパッチャーと通信する方法を指定します。 **「socket」** (INET ソケット)、**「sfs」** (共有ファイル システム)、**「sftp」** (SSH 経由で実行されるジョブ用の安全なファイル転送プロトコル)、または **「なし」**。 <span class="pre">`comm_type`</span> が「なし」として指定されている場合、検索は次のジョブ送信を実行する前にシミュレーションからのデータを待機したり受信したりしません。これは、「グリッド」、「バリアントジェネレーター」、または「ランダム」アルゴリズムで実行される検索にのみ適用され、結果は後続の検索候補を推測するために使用されません。

現在、<span class="pre">`job_type`</span> および <span class="pre">`comm_type`</span> では次の引数のペアが受け入れられます。

<div class="highlight-default notranslate">

<div class="highlight">

    =======================
    job_type    , comm_type
    =======================
    'sge'       , 'socket'    -> job submission through Sun Grid Engine, INET socket based communication
    'sge'       , 'sfs'       -> job submission through Sun Grid Engine, communication via shared file system
    'sge'       , None        -> job submission through Sun Grid Engine, no communication (only grid or random searches)
    'ssh_sge'   , 'sftp'      -> remote SSH onto a gateway, job submission through Sun Grid Engine, communication via Secure FTP
    'ssh_slurm' , 'sftp'      -> remote SSH onto a gateway, job submission through Slurm, communication via Secure FTP
    'ssh_sge'   , None        -> remote SSH onto a gateway, job submission through Sun Grid Engine, no communication (only grid or random searches)
    'ssh_slurm' , None        -> remote SSH onto a gateway, job submission through Slurm, no communication (only grid or random searches)
    'sh'        , 'socket'    -> job run directly on local shell, INET socket based communication
    'sh'        , 'sfs'       -> job run directly on local shell, communication via shared file system
    'sh'        , None        -> job run directly on local shell, no communication (only grid or random searches)

</div>

</div>

- **run_config**: 送信テンプレートをカスタマイズするためのキーワード: 文字列ペアの辞書。予期されるキーワード: 文字列ペアは job_type に依存します。

<div class="highlight-default notranslate">

<div class="highlight">

    =======
    sge (job_type as sge or ssh_sge)
    =======
    queue: the queue to submit the job to (#$ -q {queue})
    cores: the number of cores to request for the job (#$ -pe smp {cores})
    vmem: the amount of memory to request for the job (#$ -l h_vmem={vmem})
    realtime: the amount of time to request for the job (#$ -l h_rt={realtime})
    command: the command to run for the job

    example:
    run_config = {
        'queue': 'cpu.q',       # request job to be run on the 'cpu.q' queue
        'cores': 8,             # request 8 cores for the job
        'vmem': '8G',           # request 8GB of memory for the job
        'realtime': '24:00:00', # set timeout of the job to 24 hours
        'command': 'mpiexec -n $NSLOTS -hosts $(hostname) nrniv -python -mpi init.py'
    } # set the command to be run to 'mpiexec -n $NSLOTS -hosts $(hostname) nrniv -python -mpi init.py'

    =======
    sh (job_type is sh)
    =======
    command: the command to run for the job

    example:
    run_config = {
        'command': 'mpiexec -n 8 nrniv -python -mpi init.py'
    } # set the command to be run

    =======
    slurm (job_type as ssh_slurm)
    =======
    allocation:   the allocation for the job (#SBATCH -A {allocation})
    partition:    the partition for the job (#SBATCH --partition={partition})
    nodes:        the number of nodes to distribute the job (#SBATCH --nodes={nodes})
    coresPerNode: the number of cores per node (#SBATCH --ntasks-per-node={coresPerNode})
    mem:          the amount of memory to request for the job (#SBATCH --mem={mem})
    email:        the user's email for status communication (#SBATCH --mail-user={email})
    custom:       any commands to run before the job command
    command:      the command to run for the job

    example:
    run_config = {
        'allocation': 'aaa111',
        'partition': 'cpu.q',
        'nodes': 1,
        'coresPerNode': 4,
        'mem': '8G',
        'email': 'a.b.c@email.com,
        'custom': 'conda activate myenv',
        'command': 'mpiexec -n 4 nrniv -python -mpi init.py'
    }

</div>

</div>

- **params**: 検索を実行する構成値の辞書。辞書のキーは、更新する構成オブジェクトのキーと一致する必要があります。リストまたは numpy ジェネレーター \> 2 つの値は、値に対してグリッドまたは選択肢の検索を強制します。それ以外の場合、検索アルゴリズムが明示的に「グリッド」に設定されている場合を除き、2 つの値のリストにより一様分布サンプル空間が作成されます。

**使用法 1**: <span class="pre">`SimConfig`</span> オブジェクトで指定された定数値を更新します。

<div class="highlight-python notranslate">

<div class="highlight">

    # take a config object with the following parameter ``foo``
    cfg = specs.SimConfig()
    cfg.foo = 0
    cfg.update()

    # specify a search space for ``foo`` such that a simulation will run with:
    # cfg.foo = 0
    # cfg.foo = 1
    # cfg.foo = 2
    # ...
    # cfg.foo = 9

    # using:
    params = {
        'foo': range(10)
    }

</div>

</div>

**使用法 2**: <span class="pre">`SimConfig`</span> オブジェクト内のネストされたオブジェクトを更新します。

<div class="highlight-python notranslate">

<div class="highlight">

    # to update a nested object, the package uses the `.` operator to specify reflection into the object.
    # take a config object with the following parameter object ``foo``
    cfg = specs.SimConfig()
    cfg.foo = {'bar': 0, 'baz': 0}
    cfg.update()

    # specify a search space for ``foo['bar']`` with `foo.bar` such that a simulation will run:
    # cfg.foo['bar'] = 0
    # cfg.foo['bar'] = 1
    # cfg.foo['bar'] = 2
    # ...
    # cfg.foo['bar'] = 9

    # using:
    params = {
        'foo.bar': range(10)
    }

    # this reflection works with nested objects as well...
    # i.e.
    # cfg.foo = {'bar': {'baz': 0}}
    # params = {'foo.bar.baz': range(10)}

</div>

</div>

**使用法 3**: <span class="pre">`SimConfig`</span> オブジェクト内のリスト オブジェクトを更新します。

<div class="highlight-python notranslate">

<div class="highlight">

    # to update a nested object, the package uses the `.` operator to specify reflection into the object.
    # take a config object with the following
    cfg = specs.SimConfig()
    cfg.foo = [0, 1, 4, 9, 16]
    cfg.update()

    # specify a search space for ``foo[0]`` with `foo.0` such that a simulation will run:
    # cfg.foo[0] = 0
    # cfg.foo[0] = 1
    # cfg.foo[0] = 2
    # ...
    # cfg.foo[0] = 9

    # using:
    params = {
        'foo.0': range(10)
    }

    # this reflection works with nested objects as well...

</div>

</div>

- **algorithm** : 検索アルゴリズム (<span class="pre">`ray.tune`</span> 内でサポートされています)

> <div>
  >
  > **サポートされているアルゴリズム**
  >
  > </div>

<div class="highlight-python notranslate">

<div class="highlight">

    * "grid": forces grid based search over the parameter space, but otherwise functions similar to "variant generator"
    * "variant_generator": grid and random based search of the parameter space (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "random": grid and random based search of the parameter space (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "axe": Ax optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "bayesopt": Bayesian optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "hyperopt": Hyper optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "bohb": Bayesian Optimization HyperBand algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "nevergrad": Nevergrad optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "optuna": Optuna hyperparameter optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "hebo": Heteroscedastic Evolutionary Bayesian Optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)
    * "zoopt": Derivateive-free optimization algorithm (see: https://docs.ray.io/en/latest/tune/api/suggestion.html)

</div>

</div>

- **label**: 検索用のラベル。出力ファイルの名前付けに使用されます。

- **output_path**: 生成されたファイルを保存するディレクトリ。相対パスまたは絶対パスを指定できます。

- **checkpoint_path**: 検索を復元する必要がある場合に備えて、内部レイ チェックポイント ファイル (<span class="pre">`ray.tune`</span> によって維持される) を保存するディレクトリ。相対パスまたは絶対パスを指定できます。このチェックポイント パスは検索状態を維持し、検索の復元を可能にします。検索が正常に完了すると、検索のデフォルトの動作ではチェックポイント ディレクトリが削除されます。

- **max_concurrent**: 一度に実行する同時トライアルの数

- **num_samples**: パラメータ グリッドの場合、実行する試行の数。値 1 は、検索がグリッド内の各値のパラメータ空間をサンプリングすることを意味します。

- **metric**: 最適化するメトリック (これは、返されたデータ内のキーと値のペアに一致する必要があります)。 <span class="pre">`"grid"`</span>、<span class="pre">`"variant_generator"`</span>、および <span class="pre">`"random"`</span> アルゴリズムではオプションで、<span class="pre">`None`</span> が <span class="pre">`comm_type`</span> として指定されますが、最適化アルゴリズムには必須です

- **モード**: 「min」または「max」のいずれか (メトリクスを最小化するか最大化するか)。上記と同様にオプションです。

- **sample_interval**: 新しい結果をポーリングする間隔 (秒単位) (ファイル システム ベースの通信方法のポーリング)。

- **attempt_restore**: True の場合、検索は最初に **checkpoint_path** のチェックポイントからの復元を試みます。これは、中断されたバッチ ジョブを復元するのに役立ちます (同じスクリプトを再度実行するだけです)。

</div>

<div id="batch-searches-on-the-rosenbrock-function-some-simple-examples" class="section">

### 7. Rosenbrock 関数でのバッチ検索 (いくつかの簡単な例)<a href="#batch-searches-on-the-rosenbrock-function-some-simple-examples" class="headerlink" title="Link to this heading"></a>

NetPyNE github</a> の <span class="pre">`examples`</span> ディレクトリ <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples/rosenbrock" class="reference external"> には、2 次元 Rosenbrock 関数の自動パラメーター検索を実行する複数の方法が含まれています。これらの例は、詳細な NEURON シミュレーションでパラメーター検索を実行する完全なプロセス (7. パラメーター最適化検索の実行 (CA3 の例) を参照) ではなく、バッチ通信の機能の一部を簡単に示すために使用されます。そのため、パラメーター スペースと検索メソッドの詳細を記述したスクリプトを含む batch.py ファイルと、探索する関数と、バッチ自動化と通信の適切な宣言と呼び出し (従来の cfg.py、netParams.py、および init.py ファイル)。

1. <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples/rosenbrock/basic_rosenbrock" class="reference external">basic_rosenbrock</a>

これは、新しい <span class="pre">`batchtools`</span> を使用した Rosenbrock 関数の基本的なグリッド検索を示しています。検索空間は、<span class="pre">`params['x0']`</span> と <span class="pre">`params['x1']`</span> のデカルト積として定義されます。

<div class="highlight-python notranslate">

<div class="highlight">

    # from batch.py
    params = {'x0': [0, 3],
              'x1': [0, 3],
             }

</div>

</div>

つまり、値 <span class="pre">`cfg.x0`</span>、<span class="pre">`cfg.x1`</span> を繰り返します。 <span class="pre">`[(0,`</span>` `<span class="pre">`0),`</span>` `<span class="pre">`(0,`</span>` `<span class="pre">`3),`</span>` `<span class="pre">`(3,`</span>` `<span class="pre">`0),`</span>` `<span class="pre">`(3,`</span>` `<span class="pre">`3)]`</span>リスト

2. <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples/rosenbrock/coupled_rosenbrock" class="reference external">coupled_rosenbrock</a>

これは、基本的なペア グリッド検索を示しています。ここで、<span class="pre">`x0`</span> は <span class="pre">`[0,`</span>` `<span class="pre">`1,`</span>` `<span class="pre">`2]`</span>、x1\[n\] は <span class="pre">`x0[n]**2`</span> です。

<div class="highlight-python notranslate">

<div class="highlight">

    # from batch.py
    x0 = numpy.arange(0, 3)
    x1 = x0**2

    x0_x1 = [*zip(x0, x1)]
    params = {'x0_x1': x0_x1
              }

</div>

</div>

<span class="pre">`x0`</span> 値と <span class="pre">`x1`</span> 値がペアになって、以下を繰り返す検索スペース <span class="pre">`x0_x1`</span> が作成されます。 <span class="pre">`[(0,`</span>` `<span class="pre">`0),`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`1),`</span>` `<span class="pre">`(2,`</span>` `<span class="pre">`4)]`</span>リスト

次に、<span class="pre">`rosenbrock.py`</span> ファイル内で、<span class="pre">`x0_x1`</span> 値を取得するために 2 つの値のリスト <span class="pre">`cfg.x0_x1`</span> が作成され、その後、個別の <span class="pre">`x0`</span> 値と <span class="pre">`x1`</span> 値に解凍されます。

<div class="highlight-python notranslate">

<div class="highlight">

    # from rosenbrock.py
    cfg.x0_x1 = [1, 1]

    cfg.update_cfg()

    # -------------- unpacking x0_x1 list  -------------- #
    x0, x1 = cfg.x0_x1

</div>

</div>

次に、Rosenbrock 関数は、アンパックされた <span class="pre">`x0`</span> および <span class="pre">`x1`</span> を使用して評価されます。

3. <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples/rosenbrock/random_rosenbrock" class="reference external">random_rosenbrock</a>

これは、ネストされたオブジェクトに対するグリッド検索を示しています。<span class="pre">`xn`</span> は、次のデカルト積を検索するために個別に変更される 2 つの値のリストです。 <span class="pre">`[0,`</span>` `<span class="pre">`1,`</span>` `<span class="pre">`2,`</span>` `<span class="pre">`3,`</span>` `<span class="pre">`4]`</span> および<span class="pre">`[0,`</span>` `<span class="pre">`1,`</span>` `<span class="pre">`2,`</span>` `<span class="pre">`3,`</span>` `<span class="pre">`4]`</span>

<div class="highlight-python notranslate">

<div class="highlight">

    # from batch.py
    params = {'xn.0': numpy.arange(0, 5),
              'xn.1': numpy.arange(0, 5)
             }

</div>

</div>

<span class="pre">`xn.0`</span> と <span class="pre">`xn.1`</span> を使用すると、rosenbrock.py で作成および変更されたリストの 0 番目と 1 番目の要素を参照できます。

<div class="highlight-python notranslate">

<div class="highlight">

    # from rosenbrock.py
    cfg.xn = [1, 1]

    cfg.update_cfg()

    # ---------------- unpacking x list  ---------------- #
    x0, x1 = cfg.xn

</div>

</div>

</div>

<div id="performing-parameter-optimization-searches-ca3-example" class="section">

### 8. パラメーター最適化検索の実行 (CA3 の例)<a href="#performing-parameter-optimization-searches-ca3-example" class="headerlink" title="Link to this heading"></a>

NetPyNE github</a> の <span class="pre">`examples`</span> ディレクトリ <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples" class="reference external"> には、<span class="pre">`grid`</span> ベースの検索と <span class="pre">`optuna`</span> ベースの最適化の両方が表示されます。

<span class="pre">`CA3`</span> の例では、<span class="pre">`PYR->BC`</span> <span class="pre">`NMDA`</span> および <span class="pre">`AMPA`</span> のシナプス ウェイトと、<span class="pre">`BC->PYR`</span> <span class="pre">`GABA`</span> のシナプス ウェイトを調整します。

optuna ベースのパラメーター最適化の場合、検索スペースの上限と下限は <span class="pre">`optuna_search.py`</span> で次のように定義されます。

<div class="highlight-python notranslate">

<div class="highlight">

    # from optuna_search.py
    params = {'nmda.PYR->BC' : [1e-3, 1.8e-3],
              'ampa.PYR->BC' : [0.2e-3, 0.5e-3],
              'gaba.BC->PYR' : [0.4e-3, 1.0e-3],
             }

</div>

</div>

対照的に、グリッドベースのパラメーター探索の場合、検索対象の <span class="pre">`3x3x3`</span> 固有の値は、<span class="pre">`grid_search.py`</span> で次のように定義されます。

<div class="highlight-python notranslate">

<div class="highlight">

    # from grid_search.py
    params = {'nmda.PYR->BC' : numpy.linspace(1e-3, 1.8e-3, 3),
              'ampa.PYR->BC' : numpy.linspace(0.2e-3, 0.5e-3, 3),
              'gaba.BC->PYR' : numpy.linspace(0.4e-3, 1.0e-3, 3),
             }

</div>

</div>

<span class="pre">`metric`</span> は、レポートと最適化を行う特定の <span class="pre">`string`</span> (<span class="pre">`loss`</span>) を設定することに注意してください。この値は、<span class="pre">`init.py`</span> シミュレーションによって生成および送信されます。

<div class="highlight-python notranslate">

<div class="highlight">

    if sim.rank == 0: # after simulation, handle calculations on the host core.
        # from init.py
        results['PYR_loss'] = (results['PYR'] - 3.33875)**2
        results['BC_loss']  = (results['BC']  - 19.725 )**2
        results['OLM_loss'] = (results['OLM'] - 3.470  )**2
        results['loss'] = (results['PYR_loss'] + results['BC_loss'] + results['OLM_loss']) / 3
        out_json = json.dumps({**inputs, **results})

        print(out_json)
        sim.send(out_json))

</div>

</div>

<span class="pre">`out_json`</span> 出力には、<span class="pre">`loss`</span> メトリック (観測値と期待値の間の MSE として計算) を含むディクショナリが含まれています。

多目的最適化では、関連する <span class="pre">`PYR_loss`</span>、<span class="pre">`BC_loss`</span>、および <span class="pre">`OLM_loss`</span> コンポーネントが追加で含まれます (<span class="pre">`mo_optuna_search.py`</span> を参照)。

</div>

<div id="ray-checkpointing-and-resuming-interrupted-searches" class="section">

### 9. Ray チェックポイントと中断された検索の再開<a href="#ray-checkpointing-and-resuming-interrupted-searches" class="headerlink" title="Link to this heading"></a>

このベータ リリースの新機能は、<span class="pre">`ray`</span> バックエンドを介したチェックポイント設定と検索進行状況の保存です。このデータは、<span class="pre">`search`</span> 関数で指定された <span class="pre">`checkpoint_path`</span> ディレクトリに保存されます (デフォルトは、ソース ディレクトリ内に新しく作成された <span class="pre">`checkpoint`</span> フォルダです。<span class="pre">`search`</span> のデフォルトの動作では、バッチ ジョブが中断された場合に自動的に復元が試行されます)。

検索が正常に完了すると、デフォルトの動作ではこれらのチェックポイント ファイルが削除されます。ユーザーがコーディング エラーにより検索を手動で終了し、検索を再開したい場合は、最初に <span class="pre">`checkpoint_path`</span> を削除する必要があります。

</div>

<div id="parameter-importance-evaluation-using-fanova-unstable" class="section">

### 10. fANOVA を用いたパラメータ重要度評価 (不安定)<a href="#parameter-importance-evaluation-using-fanova-unstable" class="headerlink" title="Link to this heading"></a>

このベータ リリースのもう 1 つの新機能は、<span class="pre">`Optuna`</span> および <span class="pre">`scikit-learn`</span> ライブラリを介して関数 ANOVA にヒントを得たアルゴリズムを使用してパラメーターの重要性を評価する機能です。 (<a href="http://proceedings.mlr.press/v32/hutter14.pdf" class="reference external">ヒッター論文の原文</a>とその引用<a href="https://automl.github.io/fanova/cite.html" class="reference external">引用</a>を参照)

現在、単一メトリック スコアに対するペアになっていない単一パラメーターの重要性のみが、<span class="pre">`NetPyNE.batchtools.analysis`</span> <span class="pre">`Analyzer`</span> オブジェクトを通じてサポートされています。その使用例は <a href="https://github.com/suny-downstate-medical-center/netpyne/tree/batch/netpyne/batchtools/examples/rosenbrock/fanova_rosenbrock" class="reference external">here</a> です。

この例を実行するには、<span class="pre">`batch.py`</span> を使用して出力 <span class="pre">`grid.csv`</span> を生成し、その <span class="pre">`grid.csv`</span> を <span class="pre">`Analyzer`</span> オブジェクトにロードします。最後に、<span class="pre">`run_analysis`</span> を実行すると、パラメーターの推定 <span class="pre">`importance`</span> を示すパラメーターごとに 1 つのスコアが生成されます。つまり、指定された範囲内のモデルの合計分散に対する推定効果です。

<div class="highlight-python notranslate">

<div class="highlight">

    # from analysis.py
    from netpyne.batchtools.analysis import Analyzer

    analyzer = Analyzer(params = ['x.0', 'x.1', 'x.2', 'x.3'], metrics = ['fx']) # specify the parameter space and metrics of the batch function
    analyzer.load_file('grid.csv') # load the grid file generated by the batch run
    results = analyzer.run_analysis() # run fANOVA analysis and store the importance values in a results dictionary

</div>

</div>

</div>

</div>

</div>

</div>

</div>
</section>

</article>
</main>
